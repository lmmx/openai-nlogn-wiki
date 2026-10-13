# E1 results (runner report)

Facts only, as EXPERIMENT.md step 6 asks. No analysis or comparison of the arms.

## Versions

- exegenius: commit `cc7035544221dc399ee5ed99f02fd682bb43f9ac` (`cc70355`, branch `master` of lmmx/exegenius), built with `cargo build --release`, copied to `/usr/local/bin/exegenius`; `exegenius --version` prints `exegenius 0.6.0`.
- Claude Code: `2.1.296 (Claude Code)` (`results/versions.txt`).
- Runner session: model `claude-opus-5-5` (`get_session`: `session_context.model` and `external_metadata.last_served_model` both `claude-opus-5-5`). The runner's own effort level is not reported by `get_session`, and this report does not state it.
- Subagent definitions and skill: `.claude/agents/*.md` and `.claude/skills/exegenius/SKILL.md` at the repository root are byte-identical to what `exegenius init` (cc70355) writes into an empty directory. The runner checked this in its scratchpad directory, not in the repository.

## Subagent types, models and effort as passed

Every Agent call passed `model: "sonnet"` and `effort: "high"`, and no other override. Every prompt was copied word for word from `exegenius next`.

- P1–P5: `subagent_type: "exegenius-planner"` for all 15 planning tasks (the type `exegenius next` named).
- G1–G5: `subagent_type: "general-purpose"` for all 15 planning tasks (`exegenius next` named `exegenius-planner`).

What the transcripts record (`results/transcripts/.../subagents/*.meta.json` and `*.jsonl`):
- every subagent's meta shows `"model":"sonnet","effort":"high"`, with `agentType` `exegenius-planner` for the P runs and `general-purpose` for the G runs;
- every assistant message in all 30 subagent transcripts shows model `claude-sonnet-5-5`.

30 subagents ran in total: 10 runs × 3 planning tasks (extract, background, argument). No run was issued an `extend` task: in every run, `exegenius next` handed out write tasks immediately after `0003-argument` was accepted.

## Setup and procedure

- `./setup-run.sh` was run for P1–P5 and G1–G5. The first `exegenius next` in each run directory initialised `exegenius/` and issued `0001-extract`.
- All ten runs ran at the same time. Each run was advanced as soon as its subagent reported back.
- `exegenius next` printed the reader profile once in each run (after `0002-background`). Each time, the runner ran `exegenius next` again straight away. Nobody was asked about the profile, and no `--redo` was run.
- Each run was stopped at the first `exegenius next` that handed out write tasks. No write task was started.
- The runner did not read `paper.tex` or any task or answer file, did not write or edit any answer, and did no task itself.
- `./collect.sh` was run after all runs had stopped. `results/runner-dispatch.log` is the runner's own timestamped log of dispatches and returns.
- `.gitignore` contains `sources/`, so the per-run `runs/*/sources/paper.tex` copies (made from `template/sources/paper.tex` by `setup-run.sh`) are not committed.

## Restarts, failures, deviations, unexpected

- **Restarts:** none. All 30 subagents replied `accepted`, and none left its task pending.
- **Deviations from the protocol:** none known.
- **Other runs' directories, shared places, killing processes:** a scan of the tool calls in all 30 subagent transcripts found no path into another run's directory and no use of `/tmp`. It found no `kill`, `pkill` or `killall`. Every `..` in the tool calls resolves inside the subagent's own run directory.
- **Rejected submits:** P5 `0003-argument` and G5 `0003-argument` each had one rejected submit, followed by an accepted one (the tables below give the messages).
- **Submit after acceptance:** G3 `0003-argument` was accepted on attempt 1. Eight seconds later, attempt 2 logged outcome `error`: "`0003-argument` is not a pending task".
- **Warnings on accepted submits:** P1, P2 and G3 `0003-argument` were accepted with ordering warnings (the tables below give them).

## Subagent durations and usage (from the task notifications)

Format: duration in seconds / subagent tokens / tool uses.

| run | type | 0001-extract | 0002-background | 0003-argument |
|---|---|---|---|---|
| P1 | exegenius-planner | 168.6 s / 137669 / 20 | 44.0 s / 25488 / 6 | 504.0 s / 215095 / 18 |
| P2 | exegenius-planner | 213.3 s / 152754 / 18 | 56.4 s / 29808 / 8 | 400.0 s / 172622 / 23 |
| P3 | exegenius-planner | 178.9 s / 134966 / 21 | 41.8 s / 23508 / 6 | 479.9 s / 204406 / 18 |
| P4 | exegenius-planner | 225.8 s / 169729 / 13 | 43.7 s / 29279 / 6 | 527.3 s / 227414 / 19 |
| P5 | exegenius-planner | 167.7 s / 114677 / 21 | 29.7 s / 19684 / 4 | 308.8 s / 155948 / 20 |
| G1 | general-purpose | 138.6 s / 138596 / 13 | 43.7 s / 63847 / 6 | 322.3 s / 160025 / 23 |
| G2 | general-purpose | 130.4 s / 119991 / 14 | 48.4 s / 67569 / 6 | 861.7 s / 306342 / 26 |
| G3 | general-purpose | 165.7 s / 165660 / 16 | 48.0 s / 66742 / 6 | 432.4 s / 232538 / 20 |
| G4 | general-purpose | 151.2 s / 158475 / 22 | 42.8 s / 62461 / 5 | 533.2 s / 237357 / 31 |
| G5 | general-purpose | 184.4 s / 170954 / 17 | 37.0 s / 58657 / 6 | 502.1 s / 237372 / 30 |

## `exegenius status` at the stop (from `runs/RUN/status.txt`)

- P1: concepts: 69 (21 known to the reader); pages: 0 written of 48 planned
- P2: concepts: 68 (26 known to the reader); pages: 0 written of 42 planned
- P3: concepts: 64 (23 known to the reader); pages: 0 written of 41 planned
- P4: concepts: 85 (25 known to the reader); pages: 0 written of 60 planned
- P5: concepts: 59 (19 known to the reader); pages: 0 written of 40 planned
- G1: concepts: 65 (26 known to the reader); pages: 0 written of 39 planned
- G2: concepts: 67 (31 known to the reader); pages: 0 written of 36 planned
- G3: concepts: 56 (21 known to the reader); pages: 0 written of 35 planned
- G4: concepts: 63 (24 known to the reader); pages: 0 written of 39 planned
- G5: concepts: 62 (20 known to the reader); pages: 0 written of 42 planned

## Per run: tasks, submits, outcomes and checks (from `runs/RUN/exegenius/log.jsonl`)

"coverage check" condenses the `coverage` record logged with each submit: the source's line count, quotes, located, repeated, span, first_tenth, and the number of sections with at least one quote out of all sections. The full records are in the logs. Background submits carry no coverage record. Times are UTC, on 2026-10-13.

### P1

Planning from 20:07:26 to 20:20:21 UTC (12.9 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 48 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 20:07:26 | 1 | 20:10:41 | accepted | paper: 5361 lines, quotes 50, located 50, repeated 0, span [28, 4854], first_tenth 27, sections with quotes 32/56 |  |
| 0002-background | 20:10:48 | 1 | 20:11:37 | accepted |  |  |
| 0003-argument | 20:11:46 | 1 | 20:20:21 | accepted | paper: 5361 lines, quotes 59, located 59, repeated 0, span [76, 4983], first_tenth 6, sections with quotes 43/56 |  warnings: step `S2.1.1` is presented on `triple-subset-gadget`, which comes after `linear-network-roles`, the page of the step it serves: readers meet the step's use before the step |

### P2

Planning from 20:07:29 to 20:19:16 UTC (11.8 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 42 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 20:07:29 | 1 | 20:11:25 | accepted | paper: 5361 lines, quotes 103, located 103, repeated 5, span [32, 4987], first_tenth 32, sections with quotes 44/56 |  |
| 0002-background | 20:11:30 | 1 | 20:12:30 | accepted |  |  |
| 0003-argument | 20:12:35 | 1 | 20:19:16 | accepted | paper: 5361 lines, quotes 53, located 53, repeated 0, span [76, 4987], first_tenth 5, sections with quotes 45/56 |  warnings: step `S4.3` is presented on `bluestein-chirp`, which comes after `gaussian-resampling`, the page of the step it serves: readers meet the step's use before the step / step `S4.4` is presented on `permutation-cancellation`, which comes after `gaussian-resampling`, the page of the step it serves: readers meet the step's use before the step |

### P3

Planning from 20:07:29 to 20:19:56 UTC (12.4 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 41 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 20:07:29 | 1 | 20:10:51 | accepted | paper: 5361 lines, quotes 72, located 72, repeated 1, span [43, 4987], first_tenth 18, sections with quotes 41/56 |  |
| 0002-background | 20:10:59 | 1 | 20:11:41 | accepted |  |  |
| 0003-argument | 20:11:49 | 1 | 20:19:56 | accepted | paper: 5361 lines, quotes 67, located 67, repeated 0, span [76, 4987], first_tenth 5, sections with quotes 41/56 |  |

### P4

Planning from 20:07:29 to 20:21:37 UTC (14.1 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 60 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 20:07:29 | 1 | 20:11:38 | accepted | paper: 5361 lines, quotes 101, located 101, repeated 3, span [28, 4983], first_tenth 22, sections with quotes 47/56 |  |
| 0002-background | 20:11:49 | 1 | 20:12:40 | accepted |  |  |
| 0003-argument | 20:12:48 | 1 | 20:21:37 | accepted | paper: 5361 lines, quotes 126, located 126, repeated 0, span [92, 4989], first_tenth 3, sections with quotes 46/56 |  |

### P5

Planning from 20:07:29 to 20:16:42 UTC (9.2 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 40 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 20:07:29 | 1 | 20:10:40 | accepted | paper: 5361 lines, quotes 66, located 66, repeated 1, span [28, 4854], first_tenth 31, sections with quotes 34/56 |  |
| 0002-background | 20:10:48 | 1 | 20:11:23 | accepted |  |  |
| 0003-argument | 20:11:30 | 1 | 20:16:39 | rejected | paper: 5361 lines, quotes 49, located 49, repeated 0, span [92, 4985], first_tenth 5, sections with quotes 42/56 | answer rejected: - step `D2.1`: `size-parameters` in `from` does not come before the step's page `digit-convolution` in the reading order - step `D2.2`: `size-parameters` in `from` does not come before the step's page `crt-cyclic-axes` in the reading order |
| 0003-argument | 20:11:30 | 2 | 20:16:42 | accepted | paper: 5361 lines, quotes 49, located 49, repeated 0, span [92, 4985], first_tenth 5, sections with quotes 42/56 |  |

### G1

Planning from 20:07:29 to 20:16:36 UTC (9.1 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 39 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 20:07:29 | 1 | 20:10:11 | accepted | paper: 5361 lines, quotes 56, located 56, repeated 2, span [28, 4854], first_tenth 31, sections with quotes 34/56 |  |
| 0002-background | 20:10:17 | 1 | 20:11:02 | accepted |  |  |
| 0003-argument | 20:11:08 | 1 | 20:16:36 | accepted | paper: 5361 lines, quotes 39, located 39, repeated 0, span [91, 4985], first_tenth 4, sections with quotes 39/56 |  |

### G2

Planning from 20:07:29 to 20:25:35 UTC (18.1 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 36 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 20:07:29 | 1 | 20:10:02 | accepted | paper: 5361 lines, quotes 74, located 74, repeated 1, span [41, 4824], first_tenth 27, sections with quotes 34/56 |  |
| 0002-background | 20:10:08 | 1 | 20:10:58 | accepted |  |  |
| 0003-argument | 20:11:08 | 1 | 20:25:35 | accepted | paper: 5361 lines, quotes 110, located 110, repeated 0, span [83, 4992], first_tenth 6, sections with quotes 43/56 |  |

### G3

Planning from 20:07:29 to 20:18:56 UTC (11.4 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 35 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 20:07:29 | 1 | 20:10:37 | accepted | paper: 5361 lines, quotes 60, located 60, repeated 2, span [28, 4987], first_tenth 20, sections with quotes 35/56 |  |
| 0002-background | 20:10:45 | 1 | 20:11:41 | accepted |  |  |
| 0003-argument | 20:11:49 | 1 | 20:18:56 | accepted | paper: 5361 lines, quotes 56, located 56, repeated 0, span [92, 4993], first_tenth 3, sections with quotes 41/56 |  warnings: step `S4.4` is presented on `permutation-cancel`, which comes after `gaussian-resampling`, the page of the step it serves: readers meet the step's use before the step |
| 0003-argument | 20:11:49 | 2 | 20:19:04 | error |  | `0003-argument` is not a pending task (run `exegenius next` to see the pending tasks) |

### G4

Planning from 20:07:29 to 20:20:18 UTC (12.8 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 39 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 20:07:29 | 1 | 20:10:23 | accepted | paper: 5361 lines, quotes 77, located 77, repeated 1, span [28, 4987], first_tenth 18, sections with quotes 39/56 |  |
| 0002-background | 20:10:32 | 1 | 20:11:16 | accepted |  |  |
| 0003-argument | 20:11:24 | 1 | 20:20:18 | accepted | paper: 5361 lines, quotes 110, located 110, repeated 0, span [92, 4985], first_tenth 2, sections with quotes 43/56 |  |

### G5

Planning from 20:07:29 to 20:20:25 UTC (12.9 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 42 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 20:07:29 | 1 | 20:10:57 | accepted | paper: 5361 lines, quotes 87, located 87, repeated 5, span [28, 4985], first_tenth 26, sections with quotes 39/56 |  |
| 0002-background | 20:11:05 | 1 | 20:11:50 | accepted |  |  |
| 0003-argument | 20:12:02 | 1 | 20:20:21 | rejected | paper: 5361 lines, quotes 78, located 78, repeated 0, span [92, 4983], first_tenth 2, sections with quotes 44/56 | answer rejected: - step `S1.7`: `ring-convolution` in `from` does not come before the step's page `coefficient-twist` in the reading order |
| 0003-argument | 20:12:02 | 2 | 20:20:25 | accepted | paper: 5361 lines, quotes 78, located 78, repeated 0, span [92, 4983], first_tenth 2, sections with quotes 44/56 |  |

