# Ableton Live 12 Lite: Bassline-Driven Deep House Production Plan

Below is a deterministic production specification suitable for an AI agent controlling Ableton’s interface.

Live 12 Lite supports eight audio/MIDI tracks, sixteen scenes and two return tracks. It includes Drift, Simpler, Drum Rack and the stock effects used below. [Ableton’s current comparison](https://www.ableton.com/en/upgrade-live/) lists five instruments, sixteen audio effects and ten MIDI effects for Lite. Drift provides two oscillators, filtering, envelopes, modulation and mono/glide operation, making it perfectly adequate for the bass and harmonic parts. [Drift reference](https://www.ableton.com/en/manual/live-instrument-reference/)

## Global specification

- Style: bassline-driven deep house
- Tempo: 124 BPM
- Time signature: 4/4
- Key: A minor
- Length: 160 bars, approximately 5:10
- Tracks: exactly eight
- Returns: exactly two
- External plug-ins: none
- External samples: none
- Main objective: restrained chords and melodies supporting a dominant, syncopated bassline

Avoid unavailable devices such as Operator, Wavetable, EQ Eight, Glue Compressor, Echo, Hybrid Reverb, Limiter and Max for Live.

## 1. Create the Live Set

1. Create a new empty Live Set.

2. Switch to Arrangement View.

3. Set the tempo to `124.00 BPM`.

4. Set the time signature to `4/4`.

5. Set the Arrangement length to 160 bars.

6. Create exactly eight MIDI tracks and rename them:

| Track | Name | Instrument |
|---:|---|---|
| 1 | KICK | Simpler |
| 2 | MAIN DRUMS | Drum Rack |
| 3 | BASS | Drift |
| 4 | CHORD STABS | Drift |
| 5 | PAD | Drift |
| 6 | PLUCK | Drift |
| 7 | NOISE FX | Drift |
| 8 | TOPS | Drum Rack |

7. Create exactly two return tracks:

| Return | Name | Effect |
|---|---|---|
| A | DEEP REVERB | Reverb |
| B | DUB DELAY | Delay |

8. Do not create group tracks because they would complicate the eight-track limit.

9. Save the project as `Deep_House_124_Lite_v01.als`.

## 2. Configure the returns

10. On Return A, load Reverb:

- Dry/Wet: 100%
- Predelay: approximately 15 ms
- Decay Time: 2.4 seconds
- Size: approximately 75%
- Low-cut/input filtering: approximately 250 Hz
- High-frequency damping: approximately 6 kHz
- Stereo width: 100%
- Return volume: `-14 dB`

11. On Return B, load Delay:

- Sync: On
- Link left and right timing: Off
- Left time: 3/16
- Right time: 1/4
- Feedback: 27%
- Filter low cutoff: approximately 300 Hz
- Filter high cutoff: approximately 5 kHz
- Dry/Wet: 100%
- Return volume: `-16 dB`

## 3. Build the kick

12. Load Simpler on KICK.

13. Search the Core Library or Beat Tools for a dry electronic kick. Prefer:

- Short 909-style body
- Strong fundamental around 50–60 Hz
- Minimal reverb
- Tail shorter than approximately 350 ms
- No audible cymbal or percussion layer

14. Load the chosen sample into Simpler and configure:

- Mode: One-Shot
- Trigger mode: Trigger
- Fade In: 0–2 ms
- Fade Out: approximately 10 ms
- Filter: Off unless the sample is excessively bright
- Velocity-to-volume: approximately 15%

15. Add Saturator after Simpler:

- Curve: Analog Clip
- Drive: `+2 dB`
- Soft Clip: On
- Output: `-2 dB`

16. Add Channel EQ:

- Low: `+1 dB` only if the kick lacks weight
- Mid: `-1.5 dB`
- High: `-1 dB`

17. Create a one-bar MIDI clip with kick notes on sixteenth-note steps `1, 5, 9, 13`.

18. Use velocities `118, 115, 120, 116`.

19. Duplicate the kick pattern through bar 160.

20. Set the KICK track so it peaks around `-8 dBFS`.

## 4. Build the main drums

21. Load Drum Rack on MAIN DRUMS.

22. Populate pads using Core Library or Beat Tools one-shots:

- C1: short house clap
- C#1: closed hi-hat
- D1: open hi-hat
- D#1: rimshot
- E1: short conga or wood percussion
- F1: secondary clap or snap

23. Create a two-bar MIDI pattern.

24. Program the clap on steps `5` and `13` of both bars.

25. Program closed hats:

- Bar 1: steps `3, 7, 11`
- Bar 2: steps `3, 7, 11, 15`
- Velocities: alternate approximately `72, 88, 76, 92`

26. Program open hats:

- Bar 1: step `15`
- Bar 2: steps `7, 15`
- Use velocities between 74 and 86.
- Do not place a closed hat on the same step as an open hat.

27. Program rim and percussion:

- Bar 1: rim at steps `4` and `12`; conga at step `10`
- Bar 2: rim at step `12`; conga at steps `4, 10, 16`
- Velocities: 55–76

28. Move hats and percussion occurring on even sixteenth subdivisions approximately 12–16 ms late. Do not move the clap.

29. Add Channel EQ:

- Low: `-10 dB`
- Mid: `-1 dB`
- High: `+1 dB`

30. Add Compressor:

- Ratio: 2:1
- Attack: 20 ms
- Release: 90 ms
- Threshold: adjust for 1–2 dB gain reduction
- Makeup: Off

31. Set Return A send to approximately `-24 dB`.

32. Set the track peak around `-13 dBFS`.

## 5. Create the bass sound

33. Load Drift on BASS and initialise it.

34. Configure Drift:

- Voice Mode: Mono
- Legato: On
- Glide: 35 ms
- Oscillator Retrigger: On
- Oscillator 1: Saturated
- Oscillator 1 Shape: approximately 22%
- Oscillator 1 Gain: `-3 dB`
- Oscillator 2: Sine
- Oscillator 2 Octave: `-1`
- Oscillator 2 Gain: `-10 dB`
- Noise: Off
- Filter: Type II, 24 dB low-pass
- Low-pass cutoff: approximately 260 Hz
- Resonance: 12%
- Key tracking: approximately 30%
- High-pass cutoff: minimum
- Amp Attack: 3 ms
- Amp Decay: 180 ms
- Amp Sustain: 68%
- Amp Release: 65 ms
- Envelope 2 Attack: 0 ms
- Envelope 2 Decay: 140 ms
- Envelope 2 Sustain: 0%
- Envelope 2 Release: 50 ms
- Envelope 2 → LP Frequency: approximately +28%

35. Add Saturator:

- Curve: Analog Clip
- Drive: `+2.5 dB`
- Soft Clip: On
- Output: `-2.5 dB`

36. Add Compressor and enable its external sidechain:

- Sidechain source: KICK, Post FX
- Ratio: 4:1
- Attack: 1 ms
- Release: 115 ms
- Knee: approximately 6 dB
- Makeup: Off
- Threshold: adjust until each kick causes 4–6 dB of gain reduction

Ableton specifically documents this kick-to-bass sidechain technique for controlling competing low frequencies. [Compressor sidechain reference](https://www.ableton.com/en/manual/live-audio-effect-reference/)

## 6. Program the bassline

37. Create an eight-bar BASS clip.

38. Divide each bar into sixteen steps. Steps `1, 5, 9, 13` are the four kick positions.

39. Enter the following notes. The number after the colon is duration in sixteenth notes.

| Bar | Bass notes |
|---:|---|
| 1 | A0@3:2, E1@7:1, G1@10:2, E1@15:1 |
| 2 | A0@3:2, C1@7:1, E1@10:2, B1@12:1, G1@15:2 |
| 3 | G0@3:2, D1@7:1, F#1@10:2, B0@15:1 |
| 4 | G0@3:2, B0@7:1, D1@10:2, A1@12:1, F#1@15:2 |
| 5 | F0@3:2, C1@7:1, E1@10:2, C1@15:1 |
| 6 | F0@3:2, A0@7:1, C1@10:2, G1@12:1, E1@15:2 |
| 7 | E0@3:2, B0@7:1, D1@10:2, A1@12:1, B0@15:2 |
| 8 | E0@3:2, B0@7:1, D1@10:1, G#1@12:1, E1@15:1 |

40. Use approximately:

- Root-note velocity: 96
- Fifths: 84
- Chord-tone accents: 88
- Short passing notes: 70–78

41. Shorten any note that audibly collides with the next kick.

42. Set BASS peak level around `-9 to -10 dBFS`.

## 7. Create the chord stabs

43. Load Drift on CHORD STABS.

44. Configure:

- Voice Mode: Poly
- Voices: 8
- Oscillator 1: Shark Tooth
- Oscillator 1 Gain: `-7 dB`
- Oscillator 2: Triangle
- Oscillator 2 Detune: approximately +0.10 semitones
- Oscillator 2 Gain: `-10 dB`
- Filter: Type I
- Low-pass: approximately 1.8 kHz
- High-pass: approximately 160 Hz
- Resonance: 18%
- Amp Attack: 5 ms
- Decay: 280 ms
- Sustain: 18%
- Release: 220 ms

45. Add Auto Filter after Drift:

- Filter type: Low-pass
- Cutoff: 2.2 kHz
- Resonance: approximately 12%
- Drive: modest or zero

46. Add Chorus-Ensemble:

- Mode: Classic or Chorus
- Amount: approximately 22%
- Rate: slow
- Dry/Wet: 18%

47. Add Compressor sidechained from KICK:

- Ratio: 3:1
- Attack: 2 ms
- Release: 140 ms
- Threshold: 2–3 dB gain reduction

48. Create an eight-bar clip using these voicings:

| Bars | Chord |
|---|---|
| 1–2 | Am9: A2, C3, E3, G3, B3 |
| 3–4 | Gmaj9: G2, B2, D3, F#3, A3 |
| 5–6 | Fmaj9: F2, A2, C3, E3, G3 |
| 7 | E7sus4: E2, A2, B2, D3 |
| 8 | E7: E2, G#2, B2, D3 |

49. Place each chord on steps `7` and `15` of every bar.

50. Give each stab a duration of two sixteenth notes.

51. Use velocity 78 for the first stab and 70 for the second.

52. Send approximately `-20 dB` to Return A and `-25 dB` to Return B.

## 8. Create the pad

53. Load Drift on PAD.

54. Use the same chord voicings as CHORD STABS, but sustain each chord for its complete one- or two-bar harmonic duration.

55. Configure Drift:

- Poly mode
- Oscillator 1: Triangle
- Oscillator 2: Saw, quiet and slightly detuned
- Low-pass: approximately 1.3 kHz
- High-pass: approximately 220 Hz
- Attack: 650 ms
- Decay: 1.2 seconds
- Sustain: 58%
- Release: 1.8 seconds
- Chorus-Ensemble Dry/Wet: approximately 30%

56. Add Compressor sidechained from KICK for 2–3 dB gain reduction.

57. Send approximately `-15 dB` to Return A.

58. Set PAD peak around `-19 dBFS`.

## 9. Create the pluck hook

59. Load Drift on PLUCK.

60. Configure:

- Poly mode
- Oscillator 1: Saw
- Oscillator 2: Triangle, one octave higher and quiet
- Low-pass: approximately 2.4 kHz
- Resonance: 20%
- Attack: 1 ms
- Decay: 170 ms
- Sustain: 0%
- Release: 150 ms

61. Add Auto Pan:

- Rate: 1/2 note
- Phase: 180°
- Amount: 22%

62. Create this eight-bar motif:

| Bar | Notes on steps 3, 7, 11, 15 |
|---:|---|
| 1 | E4, G4, A4, E4 |
| 2 | C5, B4, G4, E4 |
| 3 | D4, F#4, G4, D4 |
| 4 | B4, A4, F#4, D4 |
| 5 | C4, E4, F4, C4 |
| 6 | A4, G4, E4, C4 |
| 7 | B3, D4, E4, B3 |
| 8 | G#4, E4, D4, B3 |

63. Use one-sixteenth-note durations, except steps 11 and 15 may last two sixteenths.

64. Use velocities between 58 and 78.

65. Send approximately `-22 dB` to Return A and `-18 dB` to Return B.

## 10. Create noise transitions

66. Load Drift on NOISE FX.

67. Disable both oscillators and enable Noise only.

68. Configure:

- Noise Gain: `-8 dB`
- Noise routed through filter
- Low-pass initially: 300 Hz
- High-pass initially: 250 Hz
- Amp Attack: 10 ms
- Sustain: 100%
- Release: 300 ms

69. Create eight-bar sustained MIDI notes before major section changes.

70. Automate low-pass cutoff from approximately 300 Hz to 12 kHz over each eight-bar rise.

71. Automate track volume from approximately `-30 dB` to `-15 dB`, then immediately back to silence on the drop.

72. Place risers ending immediately before bars 33, 81 and 97.

73. Place shorter reverse-style four-bar rises before bars 65 and 129.

## 11. Create the top percussion

74. Load Drum Rack on TOPS.

75. Load:

- Shaker
- Tambourine
- Short ride cymbal
- Optional quiet metallic percussion

76. Program the shaker on all sixteen steps with repeating velocities:

`42, 58, 48, 70, 44, 60, 50, 74, 42, 58, 48, 70, 44, 62, 52, 78`

77. Apply the same 12–16 ms swing delay used on MAIN DRUMS.

78. Use tambourine on offbeats `3, 7, 11, 15`.

79. Use the ride on quarter notes only during the peak section.

80. Add Channel EQ with Low set to `-15 dB`.

81. Add Auto Pan:

- Rate: 2 bars
- Amount: 12%
- Phase: 180°

82. Set track peak around `-17 dBFS`.

## 12. Arrange the track

83. Arrange the 160 bars as follows:

| Bars | Section | Active material |
|---|---|---|
| 1–8 | DJ intro 1 | Kick only; filtered noise texture from bar 5 |
| 9–16 | DJ intro 2 | Kick, clap, closed hats |
| 17–24 | Bass tease | Add simplified bass using only root and fifth notes |
| 25–32 | Groove introduction | Full bass; sparse chord stabs; riser into bar 33 |
| 33–48 | Main groove A | Kick, full drums, bass, chords, light pad |
| 49–64 | Main groove A2 | Add pluck and top percussion |
| 65–72 | Breakdown | Remove kick; keep pad, filtered chords and occasional pluck |
| 73–80 | Build | Reintroduce clap, hats and filtered bass; noise rise |
| 81–96 | Drop A | Full kick, drums, bass, chords and pluck |
| 97–112 | Peak | Add ride, top percussion and brightest chord filtering |
| 113–128 | Groove variation | Remove ride after bar 120; vary pluck and percussion |
| 129–144 | Outro groove | Remove pad and pluck; retain bass, kick and drums |
| 145–152 | DJ outro 1 | Remove bass and chords; kick, clap and hats only |
| 153–160 | DJ outro 2 | Kick and sparse closed hat; final clean kick at bar 160 |

## 13. Add variations and fills

84. At bars 32, 64, 80, 96, 128 and 144, remove the kick from the final beat.

85. On those bars, add a short percussion fill over steps `13–16`.

86. Before bars 33, 81 and 97, mute the final bass note to create a brief vacuum.

87. In every second eight-bar bass repetition, lower one passing-note velocity by 10–15 points.

88. In bars 56, 104 and 120, replace the final pluck note with A4 and send it more strongly to DUB DELAY.

89. Automate the relevant track’s Delay send up for the final note and return it to its normal value at the next downbeat.

90. Do not randomise the kick, root bass notes or chord-change timing.

## 14. Filter and energy automation

91. Automate BASS low-pass cutoff:

- Bars 17–24: 140 Hz → 240 Hz
- Bars 25–64: approximately 260 Hz
- Bars 65–72: approximately 110 Hz
- Bars 73–80: 110 Hz → 650 Hz
- Bar 81: immediately return to approximately 260 Hz
- Bars 129–144: gradually close to 170 Hz

92. Automate CHORD STABS cutoff:

- Intro: approximately 700 Hz
- Main groove: 1.8–2.2 kHz
- Breakdown: 500 Hz → 3.5 kHz
- Peak: approximately 2.8 kHz
- Outro: close gradually to 800 Hz

93. Increase PAD reverb send during the breakdown, but reduce it immediately before bar 81.

94. Increase MAIN DRUMS and TOPS by no more than 1 dB during the peak. Avoid large volume jumps.

## 15. Mix and validate

95. Begin with these approximate peak levels:

| Element | Peak target |
|---|---:|
| Kick | -8 dBFS |
| Bass | -9 to -10 dBFS |
| Main drums | -13 dBFS |
| Chord stabs | -15 dBFS |
| Pad | -19 dBFS |
| Pluck | -16 dBFS |
| Noise FX | -20 dBFS |
| Tops | -17 dBFS |

96. Keep kick and bass centred.

97. Keep frequencies below approximately 150 Hz effectively mono by avoiding chorus, delay and reverb on the bass.

98. Verify that every kick produces visible bass compression.

99. If the low end becomes indistinct:

- Shorten bass notes first.
- Then increase sidechain gain reduction.
- Only then reduce bass volume.

100. Check the Main channel. Before final processing, peaks should remain around `-5 to -4 dBFS`.

101. Add Channel EQ to Main only if necessary:

- Low: 0 dB
- Mid: approximately `-0.5 dB`
- High: approximately `+0.5 dB`

102. Add Saturator last on Main:

- Analog Clip
- Drive: `+1 dB`
- Soft Clip: On
- Output: `-1.5 dB`

103. Confirm that the Main channel never exceeds `-1 dBFS`.

104. Do not attempt extreme loudness without a limiter. Preserve a punchy, unclipped master instead.

## 16. Export

105. Save as `Deep_House_124_Lite_v02_Mixed.als`.

106. Use Collect All and Save so every stock sample is stored with the project.

107. Export:

- Rendered Track: Main
- Start: bar 1
- End: bar 161
- Sample rate: 44.1 kHz
- Bit depth: 24-bit
- Normalize: Off
- Dither: None
- Create Analysis File: On
- File type: WAV

108. Export the file as `Deep_House_124_Lite_Master.wav`.

109. Re-import the exported WAV temporarily and confirm:

- No clipping
- No missing samples
- Kick and bass remain distinct
- Breakdown-to-drop contrast is obvious
- Intro and outro are clean enough for DJ mixing
- No unauthorized or unavailable devices are present

The most important creative rule is that the bassline carries the track: chords should supply colour, the pluck should appear selectively, and nothing should obscure the offbeat relationship between the kick and bass.
