# Results: coverage-recovery experiment

Run by Claude Code cloud session `session_01Wpq8EVPnQJYNgZCGBBQJta` (parent
`session_017HFxUWtQFLBWkSui3shhmS`), 2026-10-13, following `EXPERIMENT.md` steps 1–8.
Facts only; no judgement of whether recovery worked.

## Versions

- exegenius: `exegenius --version` → `exegenius 0.6.0`; clone at commit `1d90c28`
  ("Coverage check that sends back introduction-only planning answers"), branch
  `timing-and-parallelism`, built with `cargo build --release`, copied to `/usr/local/bin`.
- Claude Code: `2.1.296 (Claude Code)`.
- Runner session model: `claude-opus-5-5` (from `get_session`: `session_context.model` and
  `external_metadata.last_served_model`).
- Planner subagents: every subagent transcript records model `claude-sonnet-5-5`.
- `results/versions.txt` (from `collect.sh`) has `exegenius 0.6.0` and `2.1.296 (Claude Code)`
  but no exegenius commit. `HOME` is `/root`, and `EXEGENIUS_SRC` was unset, so `collect.sh` looked
  for the clone at `/root/exegenius`. The clone is at `/home/user/exegenius`, so the git call
  failed, and the script's `|| true` hid the failure. The commit was checked by hand in step 2
  (`git rev-parse --short HEAD` → `1d90c28`).

## Subagent types

- `exegenius-planner` was offered as a subagent type at session start (step 1 passed).
- `exegenius next` named `exegenius-planner` for every planning task. All 12 planning tasks
  (extract, background, argument × 4 runs) went to `exegenius-planner`. The `agentType` field in
  each `results/transcripts/.../subagents/*.meta.json` confirms this. Each prompt was passed
  exactly as printed. No other subagent type was used.
- No `extend` task was handed out in any run.

## Per run

Times are from `runs/RUN/exegenius/log.jsonl`. "+Ns" is the time from the task's `issued` event
to the submit. Coverage figures come from the submit's `coverage` record:
- quotes: the number of quotes;
- span: the line span in `paper.tex`, which has 5361 lines;
- first tenth: how many quotes fall in the first tenth;
- sections: how many of the 13 top-level sections have a quote.

### A1 (`coverage = "report"`)

| task | submit | at | outcome | check | quotes | span | first tenth | sections |
|---|---|---|---|---|---|---|---|---|
| 0001-extract | 1 | +67s | accepted | – | 32 | 32–355 | 32 | 2 |
| 0002-background | 1 | +31s | accepted | – | | | | |
| 0003-argument | 1 | +91s | accepted | – | 17 | 76–209 | 17 | 1 |

Then 23 write tasks were handed out, and the run was stopped. Planning took 17:27:54Z → 17:31:35Z
on the runner clock (≈3m41s).

### A2 (`coverage = "report"`)

| task | submit | at | outcome | check | quotes | span | first tenth | sections |
|---|---|---|---|---|---|---|---|---|
| 0001-extract | 1 | +84s | accepted | – | 30 | 43–4508 | 24 | 6 |
| 0002-background | 1 | +33s | accepted | – | | | | |
| 0003-argument | 1 | +106s | rejected | – (reading-order errors, S8 and S11) | 21 | 92–4983 | 2 | 9 |
| 0003-argument | 2 | +111s | accepted | – | 21 | 92–4983 | 2 | 9 |

Then 28 write tasks were handed out, and the run was stopped. Planning took 17:27:58Z → 17:32:01Z
(≈4m03s).

### B1 (`coverage = "reject"`)

| task | submit | at | outcome | check | quotes | span | first tenth | sections |
|---|---|---|---|---|---|---|---|---|
| 0001-extract | 1 | +57s | rejected | coverage | 23 | 30–328 | 23 | 2 |
| 0001-extract | 2 | +140s | accepted | – | 44 | 41–4016 | 14 | 9 |
| 0002-background | 1 | +24s | accepted | – | | | | |
| 0003-argument | 1 | +156s | rejected | – (reading-order errors, S3, S3.3.2, S5.2) | 35 | 76–4985 | 7 | 9 |
| 0003-argument | 2 | +161s | accepted (6 warnings: steps presented after the page they serve) | – | 35 | 76–4985 | 7 | 9 |

Then 32 write tasks were handed out, and the run was stopped. Planning took 17:27:58Z → 17:33:43Z
(≈5m45s).

### B2 (`coverage = "reject"`)

| task | submit | at | outcome | check | quotes | span | first tenth | sections |
|---|---|---|---|---|---|---|---|---|
| 0001-extract | 1 | +49s | rejected | coverage | 23 | 41–209 | 23 | 1 |
| 0001-extract | 2 | +98s | accepted | – | 42 | 41–4837 | 16 | 9 |
| 0002-background | 1 | +29s | accepted | – | | | | |
| 0003-argument | 1 | +92s | rejected | – (quote not found word for word in S2.3; reading-order errors, S3.4, S3.4.1) | 20 | 71–212 | 19 | 1 |
| 0003-argument | 2 | +101s | rejected | coverage | 20 | 71–494 | 20 | 2 |
| 0003-argument | 3 | +171s | accepted (1 warning: step S4.2 presented after the page it serves) | – | 23 | 71–4994 | 5 | 9 |

Then 22 write tasks were handed out, and the run was stopped. Planning took 17:27:58Z → 17:33:16Z
(≈5m18s).

### Final state (from `runs/RUN/status.txt`)

| run | concepts (known) | pages planned | graph-quote sections | argument-quote sections | theorem-like statements in unquoted sections (graph / argument) |
|---|---|---|---|---|---|
| A1 | 51 (28) | 23 | 2 of 13 | 1 of 13 | 22 / 23 of 23 |
| A2 | 60 (32) | 28 | 6 of 13 | 9 of 13 | 20 / 14 of 23 |
| B1 | 55 (23) | 32 | 9 of 13 | 9 of 13 | 9 / 5 of 23 |
| B2 | 47 (25) | 22 | 9 of 13 | 9 of 13 | 9 / 9 of 23 |

## Subagent usage (from task notifications)

| run | task | tool uses | duration |
|---|---|---|---|
| A1 | extract | 6 | 58s |
| A1 | background | 3 | 30s |
| A1 | argument | 6 | 88s |
| A2 | extract | 8 | 78s |
| A2 | background | 4 | 31s |
| A2 | argument | 10 | 108s |
| B1 | extract | 16 | 134s |
| B1 | background | 3 | 21s |
| B1 | argument | 13 | 158s |
| B2 | extract | 12 | 92s |
| B2 | background | 4 | 22s |
| B2 | argument | 14 | 169s |

Each subagent replied with exactly `accepted`.

## Restarts, failures, deviations, unexpected

- Restarts: none. Every subagent left its task accepted.
- Failures: none.
- Earlier attempts (see `attempts/`) were refused at the build step. This time `add_repo` with
  `access: "push"` attached lmmx/exegenius and the build succeeded. Nothing was pushed to
  lmmx/exegenius.
- After cloning, the `add_repo` result instructed a call to `register_repo_root` for
  `/home/user/exegenius`, which I made. The exegenius clone has no `.claude/` directory and no
  `CLAUDE.md`, so the call loaded no agent definitions or skills. The planner definitions came from
  `.claude/agents/` in this repository, as the protocol requires.
- The clone was shallow (`--depth 1`, as `add_repo` instructed). Then
  `git fetch --depth 50 origin timing-and-parallelism` fetched commit `1d90c28` for the checkout.
- In each run, `exegenius next` printed the reader once, right after the background task. Each
  time I ran `exegenius next` again at once, as the protocol says.
- The runner read no task files, answer files or `paper.tex`, and gave planners nothing beyond
  the printed prompt. The runner did read `log.jsonl` and `status.txt` for this report.
- `collect.sh` ran while the runner session was still going, so the copy of the main session
  transcript in `results/transcripts/` stops at the collect step. The runner's own timestamped
  log is `results/runner-log.txt`.
