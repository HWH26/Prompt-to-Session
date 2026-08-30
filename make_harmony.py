import os, importlib.util
spec = importlib.util.spec_from_file_location("mm", os.path.join(os.path.dirname(os.path.abspath(__file__)), "make_midi.py"))
mm = importlib.util.module_from_spec(spec); spec.loader.exec_module(mm)
write_midi, OUT = mm.write_midi, mm.OUT

# Harmonic map (spec 48): bars 1-2 Am9, 3-4 Gmaj9, 5-6 Fmaj9, 7 E7sus4, 8 E7
AM9    = ['A2','C3','E3','G3','B3']
GMAJ9  = ['G2','B2','D3','F#3','A3']
FMAJ9  = ['F2','A2','C3','E3','G3']
E7SUS4 = ['E2','A2','B2','D3']
E7     = ['E2','G#2','B2','D3']
BAR_CHORD = {0:AM9,1:AM9,2:GMAJ9,3:GMAJ9,4:FMAJ9,5:FMAJ9,6:E7SUS4,7:E7}

# ---------- CHORD STABS (spec 48-51) ----------
# steps 7 and 15 of every bar, duration 2x16th, vel 78 then 70
stabs = []
for b in range(8):
    for step, vel in ((7, 78), (15, 70)):
        for nm in BAR_CHORD[b]:
            stabs.append((b, step, 2, nm, vel))
write_midi(os.path.join(OUT, 'CHORDSTABS_8bar.mid'), stabs, 8, name=b'CHORD STABS')

# ---------- PAD (spec 54) ----------
# same voicings, sustained for the full harmonic duration
pad = []
for start, bars, chord in ((0, 2, AM9), (2, 2, GMAJ9), (4, 2, FMAJ9), (6, 1, E7SUS4), (7, 1, E7)):
    for nm in chord:
        pad.append((start, 1, 16 * bars, nm, 72))
write_midi(os.path.join(OUT, 'PAD_8bar.mid'), pad, 8, name=b'PAD')

# ---------- PLUCK (spec 62-64) ----------
MOTIF = [
    ['E4','G4','A4','E4'],   ['C5','B4','G4','E4'],
    ['D4','F#4','G4','D4'],  ['B4','A4','F#4','D4'],
    ['C4','E4','F4','C4'],   ['A4','G4','E4','C4'],
    ['B3','D4','E4','B3'],   ['G#4','E4','D4','B3'],
]
STEPS = [3, 7, 11, 15]
DUR   = [1, 1, 2, 2]                 # spec 63: steps 11 & 15 may last two 16ths
VEL_ODD  = [74, 62, 78, 60]          # spec 64: all within 58-78
VEL_EVEN = [70, 66, 74, 58]
pluck = []
for b, notes in enumerate(MOTIF):
    vels = VEL_ODD if b % 2 == 0 else VEL_EVEN
    for i, nm in enumerate(notes):
        pluck.append((b, STEPS[i], DUR[i], nm, vels[i]))
write_midi(os.path.join(OUT, 'PLUCK_8bar.mid'), pluck, 8, name=b'PLUCK')

lo = min(mm.n(x[3]) for x in stabs+pad+pluck); hi = max(mm.n(x[3]) for x in stabs+pad+pluck)
print(f"combined pitch range: midi {lo}-{hi}")
