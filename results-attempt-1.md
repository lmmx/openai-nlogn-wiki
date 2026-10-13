# Experiment E3: results

**Status: stopped at step 2.** Building exegenius was refused, so no run was set up or
started (steps 3–5 not done).

## Versions

- exegenius: not built. The clone at `/home/user/exegenius` (master, depth 1) is at
  `05454dc`; commit `cc70355` was fetched (`git cat-file -t cc70355` → `commit`) but
  never checked out, because the checkout and build ran in the refused command.
- Claude Code: 2.1.296.
- Model this session runs on: claude-opus-5-5 (configured).

## Steps

1. **Subagent type and parameters:** passed. `exegenius-planner` is offered as a subagent
   type, and the Agent tool accepts `model` and `effort`.
2. **Attach and build exegenius:**
   - `add_repo` with `owner: lmmx`, `repo: exegenius`, `access: "push"`: succeeded
     (status `appended`).
   - `git clone --depth 1 https://github.com/lmmx/exegenius /home/user/exegenius`:
     succeeded. `git fetch --depth=200 origin master`: succeeded. `cc70355` exists in the clone.
   - The command `git checkout -q cc70355 && git rev-parse --short HEAD && cargo build --release
     && cp target/release/exegenius /usr/local/bin/ && exegenius --version` was denied by
     the Claude Code auto mode classifier, giving the reason `[Code from External]`. Nothing in it ran:
     HEAD stayed at `05454dc`, and no `target/` exists.
   - `register_repo_root` (lmmx/exegenius, `/home/user/exegenius`), sent in the same turn,
     was denied for the same reason.
   - The protocol says to stop if building is refused, so I tried no other route.
3. **Set up the runs:** not done.
4. **Runs M1–M5:** not done. No subagent was started.
5. **Collect:** not done.

## Planning tasks

None. No Agent calls were made, so there are no subagent types, models, effort, submits,
durations, tokens or tool uses to report.

## Restarts, failures, deviations, unexpected

- Failure: the exegenius build (step 2) was refused by the auto mode classifier
  (`[Code from External]`).
- No deviations from the protocol. Nothing outside `RESULTS.md` was changed on this branch.
