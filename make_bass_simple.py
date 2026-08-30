import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_midi import write_midi, OUT

# Simplified bass for "Bass tease" (bars 17-24): root + fifth only, half-note rhythm
# Root sustained beats 1-2 (step1, dur=8), fifth sustained beats 3-4 (step9, dur=8)
PROG = [
    ('A0','E1'), ('A0','E1'),   # bar1-2 Am
    ('G0','D1'), ('G0','D1'),   # bar3-4 G
    ('F0','C1'), ('F0','C1'),   # bar5-6 F
    ('E0','B0'), ('E0','B0'),   # bar7-8 E
]
BASS_SIMPLE = []
for i, (root, fifth) in enumerate(PROG):
    BASS_SIMPLE.append((i, 1, 8, root, 92))
    BASS_SIMPLE.append((i, 9, 8, fifth, 80))

write_midi(os.path.join(OUT, 'BASS_SIMPLE_8bar.mid'), BASS_SIMPLE, 8, name=b'BASS SIMPLE')
