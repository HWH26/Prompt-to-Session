import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_midi import write_midi, OUT

FILL_BARS = [32, 64, 80, 96, 128, 144]  # bars 1-indexed

# ===================== KICK (steps 1,5,9,13; remove beat4/step13 on fill bars) =====================
kick_notes = []
def kick_bar(bar0, drop_beat4):
    out = [(bar0, 1, 1, 'C1', 118), (bar0, 5, 1, 'C1', 115), (bar0, 9, 1, 'C1', 120)]
    if not drop_beat4:
        out.append((bar0, 13, 1, 'C1', 116))
    return out

for bar1 in list(range(1, 65)) + list(range(81, 161)):
    kick_notes.extend(kick_bar(bar1 - 1, bar1 in FILL_BARS))
write_midi(os.path.join(OUT, 'KICK_FULL_160.mid'), kick_notes, 160, name=b'KICK FULL')

# ===================== MAIN DRUMS (existing pattern + hat-roll fill on steps 13-16) =====================
notes = []
def main_drums_2bar(base, full=True):
    out = []
    out += [(base+0, 5, 2, 'C1', 96), (base+0, 13, 2, 'C1', 96)]
    out += [(base+0, 3, 1, 'C#1', 72), (base+0, 7, 1, 'C#1', 88), (base+0, 11, 1, 'C#1', 76)]
    out += [(base+0, 15, 1, 'D1', 80)]
    if full:
        out += [(base+0, 4, 1, 'D#1', 65), (base+0, 12, 1, 'D#1', 70)]
        out += [(base+0, 10, 1, 'E1', 60)]
    out += [(base+1, 5, 2, 'C1', 96), (base+1, 13, 2, 'C1', 96)]
    out += [(base+1, 3, 1, 'C#1', 92), (base+1, 7, 1, 'C#1', 72), (base+1, 11, 1, 'C#1', 88), (base+1, 15, 1, 'C#1', 76)]
    out += [(base+1, 7, 1, 'D1', 78), (base+1, 15, 1, 'D1', 84)]
    if full:
        out += [(base+1, 12, 1, 'D#1', 68)]
        out += [(base+1, 4, 1, 'E1', 60), (base+1, 10, 1, 'E1', 62), (base+1, 16, 1, 'E1', 66)]
    return out

def add_main_drums_range(a, b, full=True):
    bar = a - 1
    while bar + 1 < b:
        notes.extend(main_drums_2bar(bar, full))
        bar += 2

add_main_drums_range(9, 17, full=False)
add_main_drums_range(17, 65, full=True)
add_main_drums_range(73, 145, full=True)
add_main_drums_range(145, 161, full=False)

# remove existing clap/hat hits on beat4 (steps 13-16) of fill bars, replace with a rising fill
def is_fill_bar(bar0, step):
    bar1 = bar0 + 1
    return bar1 in FILL_BARS and step >= 13

notes = [nt for nt in notes if not is_fill_bar(nt[0], nt[1])]
for bar1 in FILL_BARS:
    bar0 = bar1 - 1
    fill_vels = [70, 82, 94, 108]
    for i, step in enumerate((13, 14, 15, 16)):
        notes.append((bar0, step, 1, 'C#1', fill_vels[i]))

write_midi(os.path.join(OUT, 'MAIN_DRUMS_FULL_160.mid'), notes, 160, name=b'MAIN DRUMS FULL')

# ===================== BASS (mute final note before 33/81/97; every-2nd-repeat velocity dip) =====================
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

MUTE_BEFORE = {32, 80, 96}   # absolute bar1 whose final note gets muted
PASSING_VEL_NOTES = {70,72,74,76,78}  # short passing-note velocities per spec (70-78)

bass_notes = []
def tile_bass(pattern, start_bar1, end_bar1, out, repeat_index_start=0):
    span = end_bar1 - start_bar1 + 1
    period = 8
    bar0 = start_bar1 - 1
    off = 0
    rep = repeat_index_start
    while off < span:
        for (b, step, dur, nm, vel) in pattern:
            if b >= span - off:
                continue
            abs_bar1 = bar0 + off + b + 1
            # mute final note (last event, bar index 7, step 15) before section changes
            if abs_bar1 in MUTE_BEFORE and b == 7 and step == 15:
                continue
            # every 2nd repeat: lower one passing note by 12
            if rep % 2 == 1 and vel in PASSING_VEL_NOTES and step == 15 and b in (0,2,4):
                vel = max(40, vel - 12)
            out.append((bar0 + off + b, step, dur, nm, vel))
        off += period
        rep += 1

tile_bass(BASS_SIMPLE8, 17, 24, bass_notes)
tile_bass(BASS8, 25, 144, bass_notes, repeat_index_start=0)
write_midi(os.path.join(OUT, 'BASS_FULL_160.mid'), bass_notes, 160, name=b'BASS FULL')

# ===================== PLUCK (bars 56/104/120: final note -> A4) =====================
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
SUB_BARS = {56, 104, 120}
pluck_notes = []
def tile_pluck(pattern, start_bar1, end_bar1, out):
    span = end_bar1 - start_bar1 + 1
    period = 8
    bar0 = start_bar1 - 1
    off = 0
    while off < span:
        for (b, step, dur, nm, vel) in pattern:
            if b < span - off:
                abs_bar1 = bar0 + off + b + 1
                if abs_bar1 in SUB_BARS and b == 7 and step == 15:
                    nm = 'A4'
                    vel = 88  # stronger, to read clearly through the delay send
                out.append((bar0 + off + b, step, dur, nm, vel))
        off += period

tile_pluck(PLUCK8, 49, 128, pluck_notes)
write_midi(os.path.join(OUT, 'PLUCK_FULL_160.mid'), pluck_notes, 160, name=b'PLUCK FULL')

print("Phase 13 files regenerated: KICK, MAIN_DRUMS, BASS, PLUCK")
