# Prompt to Session

A proof of concept for prompt-driven DAW automation using ChatGPT, Claude Cowork, Codex, and Ableton Live 12 Lite. AI agents generated MIDI, operated the DAW, diagnosed errors, repaired project state, and validated the export—demonstrating a human-in-the-loop workflow rather than autonomous music production.

## Overview

This project explores agentic automation inside a professional digital audio workstation. The workflow began with ChatGPT, which was used to develop the initial prompt and phased production plan. Claude Cowork and Codex then took turns executing that plan inside Ableton Live 12 Lite.

The agents configured the project, imported structured data, created and repaired automation, diagnosed routing and MIDI-mapping problems, inspected the underlying project structure, measured output levels, managed project assets, and produced a technically validated export.

The purpose of the experiment was not to produce a release-ready track. It was to investigate whether prompt-driven AI agents could meaningfully participate in a complex, stateful desktop production workflow.

## Reproducing the Workflow

If you want to run the same prompt-driven process yourself rather than just inspecting the finished project, see [`HOW_TO_USE.md`](HOW_TO_USE.md). It covers copying the production plan in [`docs/`](docs/) and pasting it into an AI agent with desktop control of Ableton Live, along with tips on supervising the session, handling interruptions/handoffs, and validating the export.

## Tools Used

- **ChatGPT** — initial prompt development and production planning
- **Claude Cowork** — agentic execution and DAW interaction
- **Codex** — agentic execution, diagnosis, repair, and validation
- **Ableton Live 12 Lite** — target production environment

## Hybrid Automation Approach

During execution, the agents determined that entering large quantities of MIDI notes manually through the DAW interface would be too slow and unreliable.

The agents therefore generated the MIDI files separately and imported them into Ableton Live. This created a hybrid workflow combining deterministic file generation with accessibility-based interface control:

1. Structured MIDI data was generated programmatically.
2. MIDI files were imported into Ableton Live.
3. Accessibility-based controls were used to operate the DAW interface.
4. The agents configured arrangement, devices, routing, automation, and output settings.
5. Project-file inspection was used to diagnose and repair issues that were difficult to resolve through the interface alone.
6. The completed export was measured and technically validated.

No external samples, plug-ins, or instruments were imported. The project was completed using only the instruments, devices, presets, sounds, and resources available within Ableton Live 12 Lite.

## Agent Handoffs

The project was not completed by one uninterrupted agent session. Claude Cowork and Codex worked on the same stateful project at different stages.

Each agent had to:

- Interpret the existing production plan
- Inspect the current application state
- Understand work completed by the previous agent
- Continue from an incomplete project
- Identify and correct earlier mistakes
- Select an appropriate execution method for each task
- Preserve the existing project while making changes
- Validate the resulting state before continuing

This demonstrated a form of asynchronous agent collaboration in which one system could inherit and continue another system’s desktop work.

## Diagnosis and Recovery

The agents encountered problems that could not be solved by repeating a fixed sequence of interface actions. These included:

- Incorrect automation values
- Collapsed or inaccessible automation lanes
- MIDI notes mapped to the wrong device inputs
- Differences between visible interface state and underlying project state
- Stale accessibility information
- Application-focus changes
- Interrupted sessions
- Lock screens
- Usage limits

Resolving these problems required the agents to inspect the project, form hypotheses, test changes, measure results, and select alternative methods when interface automation was insufficient.

## Validation

The final workflow included technical validation rather than relying only on visual confirmation inside the DAW.

Validation included:

- Inspecting the Ableton project structure
- Confirming track and device configuration
- Checking automation data
- Verifying MIDI mappings
- Measuring individual output levels
- Confirming output headroom
- Checking the rendered file format
- Confirming duration and sample rate
- Measuring peak and RMS levels
- Checking for clipping
- Confirming that project assets were collected

This created a closed-loop workflow:

> Prompt → Action → Inspection → Diagnosis → Repair → Measurement → Validation

## Limitations

This experiment exposed several important limitations.

Usage limits across Claude Cowork and Codex interrupted longer workflows and required handoffs between agents. Lock screens, application-focus changes, collapsed interface elements, and stale UI state also stalled progress.

Because Ableton Live does not provide a general-purpose agent automation interface for this workflow, many operations depended on accessibility controls and visible application state. This made some actions fragile and sensitive to interface changes.

Human involvement remained necessary to:

- Restore access after interruptions
- Keep the workstation available
- Resolve ambiguous situations
- Supervise agent decisions
- Evaluate the final result
- Decide whether the output met an acceptable creative standard

The resulting output is not intended to be release-ready. It demonstrates technical feasibility rather than complete creative autonomy.

## What This Project Demonstrates

This project does not suggest that agentic AI can replace a human producer.

Instead, it points toward a collaborative workflow in which a person defines intent, constraints, and quality expectations while AI agents:

- Translate natural-language instructions into application actions
- Choose execution methods based on reliability
- Generate structured assets outside the target application
- Perform repetitive interface operations
- Inspect application and project state
- Diagnose failures
- Repair incorrect or incomplete work
- Recover from interruptions
- Continue work started by another agent
- Measure and validate deliverables

The most significant outcome is not the finished track itself. It is evidence that prompt-driven agents can participate meaningfully in a complex desktop production workflow while still depending on human judgment, supervision, and creative direction.

## Repository Contents

The repository may include:

```text
Prompt-to-Session/
├── README.md
├── LICENSE
├── project/
│   └── Deep_House_124_Lite_v02_Mixed.als
├── midi/
│   └── generated MIDI files
├── docs/
│   └── production plan and workflow notes
└── media/
    └── optional audio preview
```

Ableton backup files, analysis files, temporary files, lock files, and full-resolution exports should normally be excluded from the repository.

## Opening the Project

To inspect the project:

1. Install Ableton Live 12 Lite or a compatible edition of Ableton Live.
2. Download or clone this repository.
3. Open the `.als` project file in Ableton Live.
4. Allow Ableton to locate its included factory resources if prompted.

The project does not require external plug-ins, instruments, or sample libraries. It may reference factory resources included with Ableton Live 12 Lite, depending on the local installation.

## Disclaimer

This is an independent experimental project and is not affiliated with or endorsed by Ableton, OpenAI, or Anthropic.

Ableton, Ableton Live, ChatGPT, Claude, and Codex are trademarks or product names belonging to their respective owners. Resources supplied with Ableton Live remain subject to Ableton’s applicable licence terms and are not relicensed by this repository.

## License

The original materials in this repository are available under the [MIT License](LICENSE).

Third-party software, product names, trademarks, and resources referenced by the project remain the property of their respective owners and are subject to their own licence terms.

## MIDI Generation Scripts

The Python scripts in [`scripts/`](scripts/) document an important decision made by the agents during the project.

The agents determined that entering every MIDI note manually through Ableton Live’s interface would be slow, fragile, and difficult to validate. They therefore generated Standard MIDI Files programmatically and imported them into the DAW.

The scripts define note timing, duration, velocity, arrangement position, and other structured MIDI data. They use only Python’s standard library and do not require an external MIDI-generation package.

The generated files were not treated as a replacement for the DAW workflow. Ableton Live was still used for importing, arrangement, instrument configuration, routing, automation, mixing, and export.

Some scripts represent intermediate development stages, while later scripts modify or regenerate earlier outputs. They have been retained to show how the agentic workflow evolved through iteration, diagnosis, and repair.
