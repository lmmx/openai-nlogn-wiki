# Experiment E1: the planner definition against a general-purpose subagent, at a fixed model and effort

This branch is a fixed protocol, run by a separate Claude Code cloud session (the runner).
The development session in lmmx/exegenius designed it and analyses the results; the runner
executes it exactly and reports facts. Background, in lmmx/exegenius on `master`:
`docs/journal/2026-10-13-model-allocation.md` (E1), `2026-10-13-content-judge.md` and
`2026-10-13-effort-dimension.md`.

**Question.** Plans made by `exegenius-planner` subagents on Sonnet derived far less of the
paper than plans made by general-purpose subagents on Sonnet. Those two groups also differed
in effort (medium against high), binary and orchestrator. With the model, effort, binary,
configuration and prompts held fixed, does the subagent type alone change the plans?

**Arms.** Ten planning-only runs, same binary, same configuration, same definitions (written
by `exegenius init` of the binary under test), same prompts:
- `P1`–`P5`: every task goes to a subagent of type `exegenius-planner` (the type
  `exegenius next` names);
- `G1`–`G5`: every task goes to a subagent of type `general-purpose`.

In **both** arms, every Agent call passes `model: "sonnet"` and `effort: "high"`.

## Protocol

Do these steps in order. Do not change exegenius, the configuration, the subagent
definitions or settings in `.claude/`, this protocol, or anything a run produces. If a step
fails, stop that part, record exactly what happened, and go on to the report.

1. **Check the subagent types and parameters.** This session must offer `exegenius-planner`
   and `general-purpose` as subagent types, and its Agent tool must accept `model` and
   `effort` parameters. If any is missing, stop: push nothing but `RESULTS.md` saying which,
   and report it (step 6).
2. **Attach and build exegenius.** lmmx/exegenius is the tool under test and part of this
   session's work: attach it to the session with the `add_repo` tool, `access: "push"` (which
   attaches it as a source of the session). Never push to lmmx/exegenius: this session pushes
   only to this wiki branch. Clone it as `add_repo` instructs, check out commit `cc70355`
   (branch `master`), run `cargo build --release` in it, and put `target/release/exegenius`
   on PATH (for example copy it to `/usr/local/bin`). Check that `exegenius --version` prints
   0.6.0 and `git rev-parse --short HEAD` in the clone prints `cc70355`. If attaching or
   building is refused, stop and report it (step 6): do not try another route.
3. **Set up the runs:** `./setup-run.sh P1` and likewise `P2`–`P5` and `G1`–`G5`.
4. **Run each to the end of planning.** In each run directory, run the exegenius loop as
   `.claude/skills/exegenius/SKILL.md` describes, with these rules. The runs may go on at
   the same time.
   - Give each task to a fresh subagent with exactly the prompt `exegenius next` prints for
     that task: word for word, adding, removing or rewording nothing. Say nothing to a
     subagent about how to read the source or what to put in its answer.
   - **The subagent type:** in the P runs, the type `exegenius next` names
     (`exegenius-planner`); in the G runs, `general-purpose`, whatever type `next` names.
   - **In every Agent call, in both arms:** `model: "sonnet"` and `effort: "high"`. Pass no
     other override.
   - Give each Agent call a description that starts with the run and task id, for example
     `P1 0003-argument`.
   - Do not read `paper.tex` or any task or answer file yourself, do not write or edit
     answers, and do no task yourself.
   - When `exegenius next` prints the reader instead of tasks, run `exegenius next` again:
     no one is following the run.
   - Stop the run as soon as `exegenius next` hands out write tasks. Do not start them.
   - A subagent that replies with an error and leaves its task pending gets a fresh
     subagent of the same type, with the same prompt and parameters, as the skill says.
     Record every such restart.
   - Record any subagent that reads, writes or runs a file in another run's directory or in
     a shared place such as `/tmp`, and any that tries to stop processes by name.
5. **Collect:** `./collect.sh` (copies the transcripts into `results/transcripts/`, each
   run's `exegenius status` into `runs/RUN/status.txt`, and versions into `results/`).
6. **Report** in `RESULTS.md`, facts only:
   - versions (exegenius commit, Claude Code version, the model and effort this session runs
     on);
   - which subagent types, models and effort the planning tasks actually went to, as you
     passed them;
   - for each run: its tasks, and for each task its submits in order with their outcomes and
     any `check` (from `runs/RUN/exegenius/log.jsonl`), and how long it took;
   - every restart, failure, deviation from this protocol, and anything unexpected.

   Do not judge or compare the arms: that analysis is done, blind, from the pushed
   artefacts. A run that ended badly is a result, not something to fix.
7. **Commit and push** everything (runs, results, RESULTS.md) to this branch,
   `131026-exp-e1-config`, as Louis Maddox <louismmx@gmail.com>
   (`git -c user.name="Louis Maddox" -c user.email=louismmx@gmail.com commit ...`), with no
   Co-Authored-By, "Generated with" or session-link lines. Verify the push (local HEAD equals
   the remote branch). Do not open a pull request.
8. **Tell the development session:** send a message to session
   `session_017HFxUWtQFLBWkSui3shhmS` saying the branch and commit pushed and one line of
   status (for example "10 runs completed" or "stopped at step 1: effort parameter missing").
