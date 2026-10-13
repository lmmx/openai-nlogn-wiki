# Results: Experiment S1 (screening other models for planning)

Status: **stopped at step 2.1**. No runs were set up or executed.

## Versions

- Branch `131026-exp-s1-models` at `62bb476` when the runner started.
- Claude Code: `2.1.296 (Claude Code)`.
- exegenius: not attached, cloned or built (see step 2). No `exegenius` binary on `PATH`; `/home/user/exegenius` does not exist.

## Step 1: subagent types and parameters

- The session's Agent tool lists the subagent type `exegenius-planner`.
- The Agent tool schema has a `model` parameter (enum: `sonnet`, `opus`, `haiku`, `fable`) and an `effort` parameter (enum: `low`, `medium`, `high`, `xhigh`, `max`).
- Result: passed.

## Step 2: attach and build exegenius

- 2.1: called `add_repo` with `owner: "lmmx"`, `repo: "exegenius"`, `access: "push"`. It was refused with this error:

  > Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Permission Grant].

- Following the protocol ("If a step is refused, stop and report it: do not try another route"), the runner did not attempt 2.2–2.5 or any other route.

## Steps 3–5

- Not done: there was no exegenius binary at `cc70355`. No `runs/` directory, no subagents started, no `./collect.sh`.
- Restarts: none. Subagents: none. Tokens and tool uses: none to report.

## Deviations and anything unexpected

- None beyond the refusal above.
