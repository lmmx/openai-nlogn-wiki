# Experiment: does a coverage rejection make the planner recover?

Earlier attempts are recorded in `attempts/`: their runner had only this repository attached,
so building exegenius was refused as code from outside the session. This branch is a fixed protocol, run by a separate Claude Code cloud session (the runner).
The development session in lmmx/exegenius designed it and analyses the results; the runner
executes it exactly and reports facts. Background: `docs/journal/2026-10-13-coverage-recovery.md`
in lmmx/exegenius (branch `timing-and-parallelism`).

**Question.** In run `full-v0.6-latex-planner-handoff`, the planning subagents
(`exegenius-planner`, on Sonnet) read only the introduction (lines 1–440) of the 5,361-line
`paper.tex`. With `[checks] coverage = "reject"`, exegenius sends such an answer back, naming
the unread sections. Does the planner then read them and produce a better plan?

**Replication.** This branch repeats the experiment of branch `131026-exp-coverage-recovery`
(results at commit 52704ba, runs A1, A2, B1, B2) with four more runs per condition.

**Conditions.** Eight planning-only runs, same binary, same config, same definitions:
- `A3`, `A4`, `A5`, `A6`: `[checks] coverage = "report"` (control: nothing is sent back)
- `B3`, `B4`, `B5`, `B6`: `[checks] coverage = "reject"` (treatment: sent back at most twice)

## Protocol

Do these steps in order. Do not change exegenius, the configuration, the subagent
definitions in `.claude/`, this protocol, or anything a run produces. If a step fails, stop
that part, record exactly what happened, and go on to the report.

1. **Check the planner definition loaded.** This session must offer `exegenius-planner` as a
   subagent type (it loads from `.claude/agents/` at the repository root when the session
   starts). If it does not, stop: push nothing, and report that as the blocker (step 6).
2. **Attach and build exegenius.** lmmx/exegenius is the tool under test and part of this
   session's work: attach it to the session with the `add_repo` tool, `access: "push"` (which
   attaches it as a source of the session; `read` only reports that a public repository is
   readable and attaches nothing). Never push to lmmx/exegenius: this session pushes only to
   this wiki branch. Clone it as `add_repo` instructs, check out commit `1d90c28` (branch
   `timing-and-parallelism`), run `cargo build --release` in it, and put
   `target/release/exegenius` on PATH (for example copy it to `/usr/local/bin`). Check that
   `exegenius --version` prints 0.6.0 and `git rev-parse --short HEAD` in the clone prints
   `1d90c28`. If attaching or building is refused, stop and report it (step 6): do not try
   another route.
3. **Set up the runs:** `./setup-run.sh A3 report` and likewise `A4`, `A5`, `A6` with
   `report`; `./setup-run.sh B3 reject` and likewise `B4`, `B5`, `B6` with `reject`.
4. **Run each to the end of planning.** In each run directory, run the exegenius loop as
   `.claude/skills/exegenius/SKILL.md` describes, with these rules. The runs may go on at
   the same time.
   - Give each task to a fresh subagent of exactly the type `exegenius next` names, with
     exactly the prompt it prints for that task: word for word, adding, removing or
     rewording nothing. Say nothing to a subagent about how to read the source.
   - Do not read `paper.tex` or any task or answer file yourself, do not write or edit
     answers, and do no task yourself.
   - When `exegenius next` prints the reader instead of tasks, run `exegenius next` again:
     no one is following the run.
   - Stop the run as soon as `exegenius next` hands out write tasks. Do not start them.
   - A subagent that replies with an error and leaves its task pending gets a fresh
     subagent with the same prompt, as the skill says. Record every such restart.
5. **Collect:** `./collect.sh` (copies the transcripts into `results/transcripts/`, each
   run's `exegenius status` into `runs/RUN/status.txt`, and versions into `results/`).
6. **Report** in `RESULTS.md`, facts only:
   - versions (exegenius commit, Claude Code version, the model this session runs on);
   - whether `exegenius-planner` was offered as a subagent type, and which subagent types the
     planning tasks actually went to;
   - for each run: its tasks, and for each task its submits in order with their outcomes and
     any `check` (from `runs/RUN/exegenius/log.jsonl`), and how long it took;
   - every restart, failure, deviation from this protocol, and anything unexpected.

   Do not judge whether recovery worked: that analysis is done from the pushed artefacts.
   A run that ended badly is a result, not something to fix.
7. **Commit and push** everything (runs, results, RESULTS.md) to this branch,
   `131026-exp-coverage-recovery-2`, as Louis Maddox <louismmx@gmail.com>
   (`git -c user.name="Louis Maddox" -c user.email=louismmx@gmail.com commit ...`), with no
   Co-Authored-By, "Generated with" or session-link lines. Verify the push (local HEAD equals
   the remote branch). Do not open a pull request.
8. **Tell the development session:** send a message to session
   `session_017HFxUWtQFLBWkSui3shhmS` saying the branch and commit pushed and one line of
   status (for example "8 runs completed" or "stopped at step 1: planner type not offered").
