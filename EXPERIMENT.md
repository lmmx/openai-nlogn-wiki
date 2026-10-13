# Experiment E3: the planner at medium effort, against E1's planner at high

This branch is a fixed protocol, run by a separate Claude Code cloud session (the runner).
The development session in lmmx/exegenius designed it and analyses the results; the runner
executes it exactly and reports facts. Background, in lmmx/exegenius on `master`:
`docs/journal/2026-10-13-e1-config.md` and `2026-10-13-effort-dimension.md`.

**Question.** At Sonnet and high effort, `exegenius-planner` plans stated and derived far
more of the paper than the same planner's plans at medium in an earlier experiment, which
differed also in time, binary and judging. Holding the binary, configuration, definitions,
prompts and runner protocol of E1, how do plans made at medium effort compare?

**Arm.** Five planning-only runs, `M1`–`M5`, identical to E1's P arm (wiki branch
`131026-exp-e1-config`) except for one parameter: every Agent call passes
`effort: "medium"` instead of `"high"`. E1's five P runs are the high arm; the development
session judges both arms in one blind batch.

## Protocol

Do these steps in order. Do not change exegenius, the configuration, the subagent
definitions or settings in `.claude/`, this protocol, or anything a run produces. If a step
fails, stop that part, record exactly what happened, and go on to the report.

1. **Check the subagent type and parameters.** This session must offer `exegenius-planner`
   as a subagent type, and its Agent tool must accept `model` and `effort` parameters. If
   either is missing, stop: push nothing but `RESULTS.md` saying which, and report it
   (step 6).
2. **Attach and build exegenius.** lmmx/exegenius is the tool under test and part of this
   session's work: attach it to the session with the `add_repo` tool, `access: "push"` (which
   attaches it as a source of the session). Never push to lmmx/exegenius: this session pushes
   only to this wiki branch. Clone it as `add_repo` instructs, check out commit `cc70355`,
   run `cargo build --release` in it, and put `target/release/exegenius` on PATH (for
   example copy it to `/usr/local/bin`). Check that `exegenius --version` prints 0.6.0 and
   `git rev-parse --short HEAD` in the clone prints `cc70355`. If attaching or building is
   refused, stop and report it (step 6): do not try another route.
3. **Set up the runs:** `./setup-run.sh M1` and likewise `M2`–`M5`.
4. **Run each to the end of planning.** In each run directory, run the exegenius loop as
   `.claude/skills/exegenius/SKILL.md` describes, with these rules. The runs may go on at
   the same time.
   - Give each task to a fresh subagent of exactly the type `exegenius next` names
     (`exegenius-planner`), with exactly the prompt it prints for that task: word for word,
     adding, removing or rewording nothing. Say nothing to a subagent about how to read the
     source or what to put in its answer.
   - **In every Agent call:** `model: "sonnet"` and `effort: "medium"`. Pass no other
     override.
   - Give each Agent call a description that starts with the run and task id, for example
     `M1 0003-argument`.
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
6. **Report** in `RESULTS.md`, facts only, in the form of E1's `RESULTS.md`:
   - versions (exegenius commit, Claude Code version, the model this session runs on);
   - which subagent types, models and effort the planning tasks actually went to, as you
     passed them and as the transcripts record them;
   - for each run: its tasks, and for each task its submits in order with their outcomes and
     any `check` (from `runs/RUN/exegenius/log.jsonl`), and how long it took;
   - each subagent's duration, tokens and tool uses, from the task notifications;
   - every restart, failure, deviation from this protocol, and anything unexpected.

   Do not judge the plans: that is done, blind, from the pushed artefacts. A run that ended
   badly is a result, not something to fix.
7. **Commit and push** everything (runs, results, RESULTS.md) to this branch,
   `131026-exp-e3-effort`, as Louis Maddox <louismmx@gmail.com>
   (`git -c user.name="Louis Maddox" -c user.email=louismmx@gmail.com commit ...`), with no
   Co-Authored-By, "Generated with" or session-link lines. Verify the push (local HEAD equals
   the remote branch). Do not open a pull request.
8. **Tell the development session:** send a message to session
   `session_017HFxUWtQFLBWkSui3shhmS` saying the branch and commit pushed and one line of
   status.
