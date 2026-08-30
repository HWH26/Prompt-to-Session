# Instruction Manual: Using the Prompt-to-Session Prompt

Repository: https://github.com/HWH26/Prompt-to-Session

This guide explains how to use the repository's production-plan prompt to reproduce (or adapt) the Prompt-to-Session experiment yourself — copying the prompt out of the repo and pasting it into an AI agent that can control Ableton Live 12 Lite.

This is not a guide to making the track by hand. It is a guide to running the same prompt-driven, agentic workflow the repo documents.

## 1. What you're actually copying

The "prompt" lives at:

```
docs/Ableton_Live_12_Lite_Deep_House_Production_Plan.md
```

It is a long, deterministic, step-by-step production specification (109 numbered steps across 16 sections) written so an AI agent — not a human — can follow it literally: exact BPM, exact track names and instruments, exact device settings, exact automation values, and an exact export procedure. The README calls this the project's "phased production plan," and it is the same document that was pasted into ChatGPT, Claude Cowork, and Codex during the original run.

You do not need to modify this file to use it. Copying it verbatim is the intended use.

## 2. What you need before you start

- **Ableton Live 12 Lite** (or a compatible higher edition) installed and able to open on your machine.
- **An AI agent with desktop/computer-use control**, such as Claude Cowork (Claude with computer-use tools), Codex with a desktop/browser-automation tool, or an equivalent agent that can take screenshots, click, type, and run shell commands on the same computer Ableton is running on. A plain chat model with no computer control cannot execute this prompt — it can only discuss it.
- A blank starting point. The prompt assumes Ableton is currently closed or on an empty project; it begins with "Create a new empty Live Set."

## 3. Step-by-step: copying and pasting the prompt

1. Open the repository on GitHub: https://github.com/HWH26/Prompt-to-Session
2. Navigate to `docs/Ableton_Live_12_Lite_Deep_House_Production_Plan.md`.
3. Click the "Raw" button (or open the file and use "Copy raw contents") so you copy the plain Markdown text, not a rendered/re-formatted version.
4. Select all the text in the file (from the `# Ableton Live 12 Lite: Bassline-Driven Deep House Production Plan` title down to the final paragraph) and copy it.
5. Open your AI agent session (the one with desktop/computer-use tools enabled) and make sure it has access to the computer where Ableton Live 12 Lite is installed.
6. Paste the entire document as your first message to the agent. Do not summarize or shorten it — the agent relies on exact numbers (BPM, dB values, Hz values, bar numbers) that a paraphrase would lose.
7. Send the message. The agent should begin at Section 1 ("Create the Live Set") and work through the numbered steps in order.

That's the whole "copy and paste" part. Everything after this is the agent executing the plan, which is where the remaining sections of this manual come in.

## 4. What happens after you paste it

Based on how the original run behaved, expect the agent to:

- Open Ableton Live 12 Lite and create the 8 MIDI tracks and 2 return tracks specified in Section 1.
- Work through sections in order: return-track effects, instrument setup, drum programming, bassline, harmony, arrangement, fills, automation, mixing, and finally export.
- At some point, decide that entering every MIDI note by clicking in the piano roll is too slow, and instead generate Standard MIDI files with a small script, then drag/import those files into Ableton. This is expected and matches the original workflow (see `scripts/` in this repo for examples of what those generator scripts looked like).
- Periodically save the project and, ideally, tell you what it just completed and what's next.

You are the supervisor in this workflow, not a passive spectator. Plan to:

- Keep the computer unlocked and Ableton in the foreground when the agent needs it.
- Respond to occasional clarifying questions (for example, when the agent hits ambiguity the prompt doesn't fully resolve).
- Periodically ask the agent to save, and periodically check the project yourself.
- Expect interruptions. The original run was stalled at various points by usage limits, lock screens, application-focus changes, and collapsed/stale UI elements, and had to resume mid-task more than once. If your agent session ends or errors out, you can generally just tell a fresh session to "continue from where the last agent left off" — a capable agent will open the `.als` file, inspect its current state, and pick up from there rather than starting over.

## 5. Running it in stages instead of one long session

Because the full plan is long, you don't have to paste it and walk away for one continuous session. Two practical approaches:

- **One paste, multiple sessions.** Paste the full document once. If the session is interrupted or hits a usage limit, start a new agent session, tell it the project file's location, and ask it to inspect the current state of the `.als` file and continue from the next incomplete step. This is exactly how the original project moved between Claude Cowork and Codex.
- **Section-by-section pasting.** If you'd rather supervise more closely, paste only one numbered section at a time (e.g., just Section 6, "Program the drums") and confirm the result before pasting the next section. This is slower but gives you more checkpoints.

Either way, keep the full document handy (or committed in your own working copy) so you can re-paste any section the agent needs to re-read.

## 6. Verifying the result

Don't rely only on what the agent tells you. The repo's own validation approach (see `docs/validation-results.md`) checked the *rendered file*, not just the on-screen state:

- Confirm the exported WAV's sample rate, bit depth, and duration match the spec (44.1 kHz, 24-bit, ~160 bars at 124 BPM).
- Check peak level and RMS level, and confirm there's no clipping.
- Listen for the qualitative checks the prompt itself calls out in Section 16: kick and bass stay distinct, breakdown-to-drop contrast is obvious, and the intro/outro are clean enough for DJ mixing.

You can ask your agent to run this validation pass itself (measuring the exported audio programmatically) rather than eyeballing it in the DAW.

## 7. If you just want to see the finished result instead

If you don't want to re-run the workflow yourself, you don't need the prompt at all:

1. Clone or download the repository.
2. Open `project/Deep_House_124_Lite_v02_Mixed.als` directly in Ableton Live 12 Lite.
3. Optionally listen to the preview in `media/` first.

The prompt in `docs/` is only needed if you want to reproduce or adapt the process — not to listen to or inspect the final project.

## 8. Adapting the prompt for your own track

Because the document is a literal specification rather than a vague brief, you can reuse its structure for a different track by editing the values while keeping the format intact:

- Change the **Global specification** block (tempo, key, length, style).
- Change track names/instruments in the Section 1 table if you want different sounds (keeping in mind Live 12 Lite's 8-track / 2-return limit if you're targeting that edition).
- Keep the imperative, numbered, one-instruction-per-line style throughout — that's what makes the document reliably followable by an agent. Vague instructions ("make it sound deep and moody") are far more likely to produce inconsistent results than "Set Predelay to approximately 15 ms."

## Quick reference

| Step | Action |
|---|---|
| 1 | Open `docs/Ableton_Live_12_Lite_Deep_House_Production_Plan.md` on GitHub |
| 2 | Copy the raw file contents |
| 3 | Open Ableton Live 12 Lite on your machine |
| 4 | Open an AI agent session with desktop/computer-use control of that machine |
| 5 | Paste the full document as your message to the agent |
| 6 | Supervise: keep the machine available, answer questions, ask for saves |
| 7 | If interrupted, start a new session and ask the agent to inspect the `.als` file and continue |
| 8 | Validate the final export against Section 16 and `docs/validation-results.md` |
