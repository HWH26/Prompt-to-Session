import struct, os
PPQ, T16, BAR = 480, 120, 1920
OUT = os.path.dirname(os.path.abspath(__file__))

def vlq(v):
    out = bytearray([v & 0x7F]); v >>= 7
    while v:
        out.insert(0, (v & 0x7F) | 0x80); v >>= 7
    return bytes(out)

def write_ticks(path, notes, bars, bpm=124.0, name=b'Clip'):
    """notes: list of (start_tick, length_tick, midi_pitch, velocity)"""
    evs = []
    for (st, ln, p, vel) in notes:
        evs.append((st, 1, bytes([0x90, p, vel])))
        evs.append((st + ln, 0, bytes([0x80, p, 64])))
    evs.sort(key=lambda e: (e[0], e[1]))
    trk = bytearray()
    trk += b'\x00\xff\x03' + vlq(len(name)) + name
    trk += b'\x00\xff\x51\x03' + struct.pack('>I', int(round(60000000.0/bpm)))[1:]
    trk += b'\x00\xff\x58\x04\x04\x02\x18\x08'
    last = 0
    for (t, _o, data) in evs:
        trk += vlq(t - last) + data; last = t
    trk += vlq(max(0, bars*BAR - last)) + b'\xff\x2f\x00'
    open(path, 'wb').write(b'MThd' + struct.pack('>IHHH', 6, 0, 1, PPQ)
                           + b'MTrk' + struct.pack('>I', len(trk)) + bytes(trk))
    print(f"wrote {os.path.basename(path)}  notes={len(notes)}  bars={bars}")

SHAKER, TAMB, RIDE = 36, 37, 38      # C1, C#1, D1  (verified in Live)
SWING = 15                            # ticks ≈ 15.1 ms at 124 BPM — matches MAIN DRUMS
HIT   = 60                            # note length (1/32) — Drum Rack pads are One-Shot

# spec 76: shaker velocities across the 16 steps, repeating each bar
SHAKER_VEL = [42,58,48,70,44,60,50,74,42,58,48,70,44,62,52,78]
TAMB_STEPS = {3:70, 7:62, 11:70, 15:66}     # spec 78 (velocities chosen)
RIDE_STEPS = {1:72, 5:64, 9:70, 13:66}      # spec 79 (velocities chosen)

def build(with_ride):
    notes = []
    for b in range(2):
        for i, vel in enumerate(SHAKER_VEL):
            step = i + 1
            # spec 77: even 16th subdivisions pushed late, same as MAIN DRUMS
            off = SWING if step % 2 == 0 else 0
            notes.append((b*BAR + i*T16 + off, HIT, SHAKER, vel))
        for step, vel in TAMB_STEPS.items():
            notes.append((b*BAR + (step-1)*T16, HIT, TAMB, vel))
        if with_ride:
            for step, vel in RIDE_STEPS.items():
                notes.append((b*BAR + (step-1)*T16, HIT, RIDE, vel))
    return notes

write_ticks(os.path.join(OUT, 'TOPS_2bar.mid'),      build(False), 2, name=b'TOPS')
write_ticks(os.path.join(OUT, 'TOPS_RIDE_2bar.mid'), build(True),  2, name=b'TOPS RIDE')

swung = [s for s in range(1,17) if s % 2 == 0]
print("swung steps:", swung, f"({SWING} ticks = {SWING*60000.0/124/480:.1f} ms)")
