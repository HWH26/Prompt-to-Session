import struct, os

PPQ = 480
T16 = PPQ // 4          # 120 ticks per 16th
BAR = PPQ * 4           # 1920 ticks per bar
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)))

# Live displays middle C (MIDI 60) as C3
PC = {'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
def n(name):
    i = 1
    while name[i] in '#':
        i += 1
    return 60 + (int(name[i:]) - 3) * 12 + PC[name[:i]]

def vlq(v):
    out = bytearray([v & 0x7F])
    v >>= 7
    while v:
        out.insert(0, (v & 0x7F) | 0x80)
        v >>= 7
    return bytes(out)

def write_midi(path, notes, bars, bpm=124.0, name=b'Clip'):
    """notes: list of (bar_index0, step1based, dur_in_16ths, note_name, velocity)"""
    evs = []  # (tick, order, bytes)
    for (b, step, dur, nm, vel) in notes:
        start = b * BAR + (step - 1) * T16
        length = dur * T16
        p = n(nm)
        evs.append((start, 1, bytes([0x90, p, vel])))
        evs.append((start + length, 0, bytes([0x80, p, 64])))
    evs.sort(key=lambda e: (e[0], e[1]))

    trk = bytearray()
    trk += b'\x00\xff\x03' + vlq(len(name)) + name
    us = int(round(60000000.0 / bpm))
    trk += b'\x00\xff\x51\x03' + struct.pack('>I', us)[1:]
    trk += b'\x00\xff\x58\x04\x04\x02\x18\x08'
    last = 0
    for (t, _o, data) in evs:
        trk += vlq(t - last) + data
        last = t
    end = bars * BAR
    trk += vlq(max(0, end - last)) + b'\xff\x2f\x00'

    with open(path, 'wb') as f:
        f.write(b'MThd' + struct.pack('>IHHH', 6, 0, 1, PPQ))
        f.write(b'MTrk' + struct.pack('>I', len(trk)) + bytes(trk))
    print(f"wrote {os.path.basename(path)}  notes={len(notes)}  bars={bars}")

# ---------------- BASS (spec steps 37-41) ----------------
# velocity model (spec 40): root=96, fifth=84, chord-tone accent=88, short passing=70-78
BASS = [
    # bar 1  Am
    (0, 3, 2, 'A0', 96), (0, 7, 1, 'E1', 84), (0, 10, 2, 'G1', 88), (0, 15, 1, 'E1', 76),
    # bar 2  Am
    (1, 3, 2, 'A0', 96), (1, 7, 1, 'C1', 88), (1, 10, 2, 'E1', 84), (1, 12, 1, 'B1', 74), (1, 15, 2, 'G1', 78),
    # bar 3  G
    (2, 3, 2, 'G0', 96), (2, 7, 1, 'D1', 84), (2, 10, 2, 'F#1', 88), (2, 15, 1, 'B0', 76),
    # bar 4  G
    (3, 3, 2, 'G0', 96), (3, 7, 1, 'B0', 88), (3, 10, 2, 'D1', 84), (3, 12, 1, 'A1', 74), (3, 15, 2, 'F#1', 78),
    # bar 5  F
    (4, 3, 2, 'F0', 96), (4, 7, 1, 'C1', 84), (4, 10, 2, 'E1', 88), (4, 15, 1, 'C1', 76),
    # bar 6  F
    (5, 3, 2, 'F0', 96), (5, 7, 1, 'A0', 88), (5, 10, 2, 'C1', 84), (5, 12, 1, 'G1', 74), (5, 15, 2, 'E1', 78),
    # bar 7  E7sus4
    (6, 3, 2, 'E0', 96), (6, 7, 1, 'B0', 84), (6, 10, 2, 'D1', 88), (6, 12, 1, 'A1', 74), (6, 15, 2, 'B0', 78),
    # bar 8  E7
    (7, 3, 2, 'E0', 96), (7, 7, 1, 'B0', 84), (7, 10, 1, 'D1', 88), (7, 12, 1, 'G#1', 74), (7, 15, 1, 'E1', 76),
]
write_midi(os.path.join(OUT, 'BASS_8bar.mid'), BASS, 8, name=b'BASS')

# collision check against kick steps 1,5,9,13
kick = {1, 5, 9, 13}
bad = []
for (b, step, dur, nm, vel) in BASS:
    for s in range(step + 1, step + dur):
        if ((s - 1) % 16) + 1 in kick:
            bad.append((b + 1, step, dur, nm))
print("kick collisions:", bad if bad else "none")
