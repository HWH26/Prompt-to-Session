import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_midi import write_midi, OUT

# bar ranges are 1-indexed inclusive; internal bar_index is 0-indexed
def rng(a, b):
    return range(a-1, b)  # 0-indexed, inclusive of b

notes = []

# ===================== MAIN DRUMS =====================
# 2-bar pattern (spec section 4), repeated. C1=clap, C#1=closed hat, D1=open hat, D#1=rim, E1=conga
def main_drums_2bar(base):
    out = []
    # bar1 of pair
    out += [(base+0, 5, 2, 'C1', 96), (base+0, 13, 2, 'C1', 96)]
    out += [(base+0, 3, 1, 'C#1', 72), (base+0, 7, 1, 'C#1', 88), (base+0, 11, 1, 'C#1', 76)]
    out += [(base+0, 15, 1, 'D1', 80)]
    out += [(base+0, 4, 1, 'D#1', 65), (base+0, 12, 1, 'D#1', 70)]
    out += [(base+0, 10, 1, 'E1', 60)]
    # bar2 of pair
    out += [(base+1, 5, 2, 'C1', 96), (base+1, 13, 2, 'C1', 96)]
    out += [(base+1, 3, 1, 'C#1', 92), (base+1, 7, 1, 'C#1', 72), (base+1, 11, 1, 'C#1', 88), (base+1, 15, 1, 'C#1', 76)]
    out += [(base+1, 7, 1, 'D1', 78), (base+1, 15, 1, 'D1', 84)]
    out += [(base+1, 12, 1, 'D#1', 68)]
    out += [(base+1, 4, 1, 'E1', 60), (base+1, 10, 1, 'E1', 62), (base+1, 16, 1, 'E1', 66)]
    return out

def add_main_drums_range(a, b):
    bar = a - 1
    while bar + 1 < b:
        notes.extend(main_drums_2bar(bar))
        bar += 2

add_main_drums_range(9, 65)     # bars 9-64
add_main_drums_range(73, 161)   # bars 73-160
write_midi(os.path.join(OUT, 'MAIN_DRUMS_FULL_160.mid'), notes, 160, name=b'MAIN DRUMS FULL')

# ===================== BASS =====================
notes2 = []
BASS8 = [
    (0, 3, 2, 'A0', 96), (0, 7, 1, 'E1', 84), (0, 10, 2, 'G1', 88), (0, 15, 1, 'E1', 76),
    (1, 3, 2, 'A0', 96), (1, 7, 1, 'C1', 88), (1, 10, 2, 'E1', 84), (1, 12, 1, 'B1', 74), (1, 15, 2, 'G1', 78),
    (2, 3, 2, 'G0', 96), (2, 7, 1, 'D1', 84), (2, 10, 2, 'F#1', 88), (2, 15, 1, 'B0', 76),
    (3, 3, 2, 'G0', 96), (3, 7, 1, 'B0', 88), (3, 10, 2, 'D1', 84), (3, 12, 1, 'A1', 74), (3, 15, 2, 'F#1', 78),
    (4, 3, 2, 'F0', 96), (4, 7, 1, 'C1', 84), (4, 10, 2, 'E1', 88), (4, 15, 1, 'C1', 76),
    (5, 3, 2, 'F0', 96), (5, 7, 1, 'A0', 88), (5, 10, 2, 'C1', 84), (5, 12, 1, 'G1', 74), (5, 15, 2, 'E1', 78),
    (6, 3, 2, 'E0', 96), (6, 7, 1, 'B0', 84), (6, 10, 2, 'D1', 88), (6, 12, 1, 'A1', 74), (6, 15, 2, 'B0', 78),
    (7, 3, 2, 'E0', 96), (7, 7, 1, 'B0', 84), (7, 10, 1, 'D1', 88), (7, 12, 1, 'G#1', 74), (7, 15, 1, 'E1', 76),
]
BASS_SIMPLE8 = []
PROG = [('A0','E1'), ('A0','E1'), ('G0','D1'), ('G0','D1'), ('F0','C1'), ('F0','C1'), ('E0','B0'), ('E0','B0')]
for i, (root, fifth) in enumerate(PROG):
    BASS_SIMPLE8.append((i, 1, 8, root, 92))
    BASS_SIMPLE8.append((i, 9, 8, fifth, 80))

def tile(pattern, start_bar1, end_bar1_inclusive, out):
    span = end_bar1_inclusive - start_bar1 + 1
    period = 8
    bar0 = start_bar1 - 1
    off = 0
    while off < span:
        for (b, step, dur, nm, vel) in pattern:
            if b < span - off:
                out.append((bar0 + off + b, step, dur, nm, vel))
        off += period

tile(BASS_SIMPLE8, 17, 24, notes2)
tile(BASS8, 25, 144, notes2)
write_midi(os.path.join(OUT, 'BASS_FULL_160.mid'), notes2, 160, name=b'BASS FULL')

# ===================== CHORD STABS =====================
notes3 = []
CHORDS8 = [
    (0, ['A2','C3','E3','G3','B3']), (1, ['A2','C3','E3','G3','B3']),
    (2, ['G2','B2','D3','F#3','A3']), (3, ['G2','B2','D3','F#3','A3']),
    (4, ['F2','A2','C3','E3','G3']), (5, ['F2','A2','C3','E3','G3']),
    (6, ['E2','A2','B2','D3']),
    (7, ['E2','G#2','B2','D3']),
]
CHORDSTABS8 = []
for (b, tones) in CHORDS8:
    for nm in tones:
        CHORDSTABS8.append((b, 7, 2, nm, 78))
        CHORDSTABS8.append((b, 15, 2, nm, 70))
tile(CHORDSTABS8, 25, 144, notes3)
write_midi(os.path.join(OUT, 'CHORDSTABS_FULL_160.mid'), notes3, 160, name=b'CHORDSTABS FULL')

# ===================== PAD =====================
notes4 = []
PAD8 = []
for (b, tones) in CHORDS8:
    for nm in tones:
        PAD8.append((b, 1, 16, nm, 70))
tile(PAD8, 33, 128, notes4)
write_midi(os.path.join(OUT, 'PAD_FULL_160.mid'), notes4, 160, name=b'PAD FULL')

# ===================== PLUCK =====================
notes5 = []
PLUCK8 = [
    (0, 3, 1, 'E4', 70), (0, 7, 1, 'G4', 66), (0, 11, 2, 'A4', 74), (0, 15, 2, 'E4', 62),
    (1, 3, 1, 'C5', 76), (1, 7, 1, 'B4', 68), (1, 11, 2, 'G4', 72), (1, 15, 2, 'E4', 60),
    (2, 3, 1, 'D4', 68), (2, 7, 1, 'F#4', 66), (2, 11, 2, 'G4', 74), (2, 15, 2, 'D4', 60),
    (3, 3, 1, 'B4', 74), (3, 7, 1, 'A4', 66), (3, 11, 2, 'F#4', 72), (3, 15, 2, 'D4', 60),
    (4, 3, 1, 'C4', 66), (4, 7, 1, 'E4', 64), (4, 11, 2, 'F4', 72), (4, 15, 2, 'C4', 58),
    (5, 3, 1, 'A4', 74), (5, 7, 1, 'G4', 66), (5, 11, 2, 'E4', 72), (5, 15, 2, 'C4', 58),
    (6, 3, 1, 'B3', 66), (6, 7, 1, 'D4', 64), (6, 11, 2, 'E4', 72), (6, 15, 2, 'B3', 58),
    (7, 3, 1, 'G#4', 78), (7, 7, 1, 'E4', 68), (7, 11, 2, 'D4', 74), (7, 15, 2, 'B3', 60),
]
tile(PLUCK8, 49, 128, notes5)
write_midi(os.path.join(OUT, 'PLUCK_FULL_160.mid'), notes5, 160, name=b'PLUCK FULL')

# ===================== TOPS =====================
notes6 = []
SHAKER_VEL = [42,58,48,70,44,60,50,74,42,58,48,70,44,62,52,78]
def tops_bar(base, with_ride):
    out = []
    for step in range(1, 17):
        out.append((base, step, 1, 'C2', SHAKER_VEL[step-1]))  # shaker
    for step in (3,7,11,15):
        out.append((base, step, 1, 'C#2', 60))  # tambourine
    if with_ride:
        for step in (1,5,9,13):
            out.append((base, step, 1, 'D2', 70))  # ride quarter notes
    return out

def add_tops_range(a, b, with_ride):
    for bar1 in range(a, b+1):
        notes6.extend(tops_bar(bar1-1, with_ride))

add_tops_range(49, 64, False)
add_tops_range(97, 120, True)
add_tops_range(121, 128, False)
write_midi(os.path.join(OUT, 'TOPS_FULL_160.mid'), notes6, 160, name=b'TOPS FULL')

# ===================== NOISE FX (sustained riser markers) =====================
notes7 = []
# 8-bar sustained note before bars 33, 81, 97 (i.e. occupying the previous 8 bars)
for start in (25, 73, 89):
    notes7.append((start-1, 1, 16*8, 'C3', 70))
# bar 5 texture (short, from spec item 1: filtered noise texture from bar 5, through bar 8)
notes7.append((4, 1, 16*4, 'C3', 60))
# 4-bar reverse rises before bars 65 and 129
for start in (61, 125):
    notes7.append((start-1, 1, 16*4, 'C3', 65))
write_midi(os.path.join(OUT, 'NOISEFX_FULL_160.mid'), notes7, 160, name=b'NOISE FX FULL')

print("DONE - all full-arrangement MIDI files written")
