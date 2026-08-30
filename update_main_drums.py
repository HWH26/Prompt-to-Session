import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_midi import write_midi, OUT

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

# 9-16: DJ intro 2 -> clap + hats only (no rim/conga)
add_main_drums_range(9, 17, full=False)
# 17-64: full pattern
add_main_drums_range(17, 65, full=True)
# 73-144: full pattern
add_main_drums_range(73, 145, full=True)
# 145-160: DJ outro -> clap + hats only (no rim/conga)
add_main_drums_range(145, 161, full=False)

write_midi(os.path.join(OUT, 'MAIN_DRUMS_FULL_160.mid'), notes, 160, name=b'MAIN DRUMS FULL')
print("Rebuilt MAIN_DRUMS_FULL_160.mid with rim/conga muted in bars 9-16 and 145-160")
