# E3 results (runner report)

Facts only, as EXPERIMENT.md step 6 asks. No analysis of the plans or comparison with E1.

**Status:** steps 1–5 done; all five runs (M1–M5) reached write tasks and were stopped there.

## Versions

- exegenius: commit `cc7035544221dc399ee5ed99f02fd682bb43f9ac` (`cc70355`) of lmmx/exegenius, built with `cargo build --release`, copied to `/usr/local/bin/exegenius`; `exegenius --version` prints `exegenius 0.6.0`; `git rev-parse --short HEAD` in the clone prints `cc70355` (`results/versions.txt`).
- Claude Code: `2.1.296 (Claude Code)` (`results/versions.txt`).
- Runner session: model `claude-opus-5-5` (`get_session`: `configured_model`, `session_context.model` and `external_metadata.last_served_model` all `claude-opus-5-5`). `get_session` does not report the runner's own effort level, and this report does not state it.

## Steps 1–2

1. `exegenius-planner` is offered as a subagent type; the Agent tool accepts `model` and `effort`. Passed.
2. Each sub-step was its own tool call, in order, each finished before the next:
   1. `add_repo` (`lmmx`, `exegenius`, `access: "push"`): status `appended`.
   2. `git clone --depth 1 https://github.com/lmmx/exegenius /home/user/exegenius` (HEAD then `cdee3f4`), then `git fetch --depth=200 origin master`; `git cat-file -t cc70355` → `commit`.
   3. `git checkout -q cc70355`; `git rev-parse --short HEAD` → `cc70355`.
   4. `register_repo_root` (lmmx/exegenius, `/home/user/exegenius`): status `context_reload_requested`. No CLAUDE.md system-reminder followed; neither `/home/user/exegenius/CLAUDE.md` nor `/home/user/exegenius/.claude/CLAUDE.md` exists.
   5. `cargo build --release` (finished in 2m 08s), copy to `/usr/local/bin`, `exegenius --version` → `exegenius 0.6.0`. Nothing was refused.

## Subagent types, models and effort as passed

Every Agent call passed `subagent_type: "exegenius-planner"` (the type `exegenius next` named), `model: "sonnet"` and `effort: "medium"`, and no other override. Every prompt was copied word for word from `exegenius next`. Every description began with the run and task id (e.g. `M1 0003-argument`).

What the transcripts record (`results/transcripts/-home-user-openai-nlogn-wiki/.../subagents/*.meta.json` and `*.jsonl`):
- all 15 subagent metas show `"agentType":"exegenius-planner","model":"sonnet","effort":"medium"`;
- all 173 assistant messages in the 15 subagent transcripts show model `claude-sonnet-5-5`.

15 subagents ran in total: 5 runs × 3 planning tasks (extract, background, argument). No run was issued an `extend` task: in every run, `exegenius next` handed out write tasks immediately after `0003-argument` was accepted.

## Setup and procedure

- `./setup-run.sh` was run for M1–M5. The first `exegenius next` in each run directory initialised `exegenius/` and issued `0001-extract`.
- All five runs ran at the same time. Each run was advanced when its subagent reported back.
- `exegenius next` printed the reader profile once in each run (after `0002-background`). Each time, the runner ran `exegenius next` again straight away. Nobody was asked about the profile, and no `--redo` was run.
- Each run was stopped at the first `exegenius next` that handed out write tasks. No write task was started.
- The runner did not read `paper.tex` or any task or answer file, did not write or edit any answer, and did no task itself.
- `./collect.sh` was run after all runs had stopped. `results/runner-dispatch.log` is the runner's own log of subagent returns, usage and stops.
- `.gitignore` contains `sources/`, so the per-run `runs/*/sources/paper.tex` copies are not committed.

## Restarts, failures, deviations, unexpected

- **Restarts:** none. All 15 subagents replied `accepted`, and none left its task pending.
- **Deviations from the protocol:** none known.
- **Shared place:** the M4 `0003-argument` subagent wrote, edited and ran a script at `/tmp/claude-0/gen.py` (3 Bash tool calls: `cat > /tmp/claude-0/gen.py …; python3 /tmp/claude-0/gen.py && exegenius submit 0003-argument`, then a `sed -i` on it, then a Python rewrite of it, each followed by running it and submitting). The file was still there after the runs (11530 bytes). No other subagent's tool calls name a path under `/tmp` or any path outside its own run directory.
- **Other runs' directories, killing processes:** a scan of the tool calls in all 15 subagent transcripts found no path into another run's directory and no `kill`, `pkill` or `killall`. Every `../` in the tool calls (M2, M3, M4, M5) resolves inside the subagent's own run directory.
- **Rejected submits:** every run had at least one rejected submit before acceptance: M1 extract (1) and argument (1); M2 extract (1); M3 extract (1) and argument (1); M4 extract (1) and argument (2); M5 extract (1) and argument (1). The tables below give the messages.
- **Submit after acceptance:** M3 `0001-extract` was accepted on attempt 2; three seconds later attempt 3 logged outcome `error`: "`0001-extract` is not a pending task".
- **Warnings on accepted submits:** M3 `0001-extract` was accepted with the warning "`lower-triangular-factorization`: no supporting quote from the sources".
- **Task notifications vs. hand-backs:** each subagent's reply arrived as a hand-back message, and the usage figures below came in a separate task notification.

## Subagent durations and usage (from the task notifications)

Format: duration in seconds / subagent tokens / tool uses.

| run | type | 0001-extract | 0002-background | 0003-argument |
|---|---|---|---|---|
| M1 | exegenius-planner | 53.7 s / 36304 / 7 | 18.4 s / 13023 / 4 | 90.5 s / 39048 / 9 |
| M2 | exegenius-planner | 61.3 s / 42678 / 10 | 28.4 s / 14607 / 5 | 97.4 s / 42041 / 7 |
| M3 | exegenius-planner | 59.9 s / 47851 / 10 | 22.5 s / 14328 / 4 | 118.0 s / 53465 / 13 |
| M4 | exegenius-planner | 72.9 s / 47171 / 9 | 21.4 s / 12246 / 3 | 179.2 s / 69373 / 13 |
| M5 | exegenius-planner | 59.3 s / 40626 / 8 | 22.5 s / 14986 / 4 | 109.0 s / 44298 / 11 |

## `exegenius status` at the stop (from `runs/RUN/status.txt`)

- M1: concepts: 38 (17 known to the reader); pages: 0 written of 21 planned
- M2: concepts: 44 (24 known to the reader); pages: 0 written of 20 planned
- M3: concepts: 48 (22 known to the reader); pages: 0 written of 26 planned
- M4: concepts: 48 (27 known to the reader); pages: 0 written of 21 planned
- M5: concepts: 45 (20 known to the reader); pages: 0 written of 25 planned

## Per run: tasks, submits, outcomes and checks (from `runs/RUN/exegenius/log.jsonl`)

"coverage check" condenses the `coverage` record logged with each submit: the source's line count, quotes, located, repeated, span, first_tenth, and the number of sections with at least one quote out of all sections. The full records are in the logs. Background submits carry no coverage record. Times are UTC, on 2026-10-13.

### M1

Planning from 21:10:19 to 21:13:23 UTC (3.1 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 21 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 21:10:19 | 1 | 21:11:21 | rejected | paper: 5361 lines, quotes 39, located 39, repeated 1, span [32, 3907], first_tenth 29, sections with quotes 16/56 | answer rejected: - `butterfly`: `u` does not occur in the mathematics of the title "Two-point butterfly $H_0$" - `butterfly`: `v` does not occur in the mathematics of the title "Two-point butterfly $H_0$" |
| 0001-extract | 21:10:19 | 2 | 21:11:24 | accepted | paper: 5361 lines, quotes 39, located 39, repeated 1, span [32, 3907], first_tenth 29, sections with quotes 16/56 |  |
| 0002-background | 21:11:29 | 1 | 21:11:50 | accepted |  |  |
| 0003-argument | 21:11:57 | 1 | 21:13:19 | rejected | paper: 5361 lines, quotes 17, located 17, repeated 0, span [43, 4810], first_tenth 3, sections with quotes 19/56 | answer rejected: - step `S4.4`: `gaussian-resampling` in `from` does not come before the step's page `bluestein-chirp` in the reading order |
| 0003-argument | 21:11:57 | 2 | 21:13:23 | accepted | paper: 5361 lines, quotes 17, located 17, repeated 0, span [43, 4810], first_tenth 3, sections with quotes 19/56 |  |

### M2

Planning from 21:10:21 to 21:14:06 UTC (3.7 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 20 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 21:10:21 | 1 | 21:11:18 | rejected | paper: 5361 lines, quotes 27, located 27, repeated 0, span [29, 3515], first_tenth 25, sections with quotes 8/56 | answer rejected: it is drawn from part of the sources.  The quotes from `sources/paper.tex` come from lines 29–3515 of its 5361 lines, and none comes from these sections, which develop results in theorems, lemmas, definitions or displayed equations: - §3 Two finite networks with a rank saving (lines 640–1346): 4 theorem-like statements, 8 displayed equations - §4 Faster interchange of address chunks (lines 1347–1762): 4 theorem-like statements, 2 displayed equations - §5 Fast simultaneous synthetic butterfly layers (lines 1763–2758): 2 theorem-like statements, 13 displayed equations - §6 Synthetic transforms and their tape layout (lines 2759–3207): 2 theorem-like statements, 5 displayed equations - §7 Exact normalized polynomial products (lines 3208–3495): 2 theorem-like statements, 2 displayed equations - §9 Exact integer multiplication and its cost (lines 3989–4995): 0 theorem-like statements, 8 displayed equations - §A Packed additions on grouped rectangles (lines 5199–5361): 2 theorem-like statements, 1 displayed equations  An introduction summarises results; the sections after it develop them, and the target depends on that development. Read each source to its last line, in parts (the Read tool's offset and limit), and revise the answer: keep what holds, add what the target depends on, and quote each concept or step where the sources develop it rather than where the introduction mentions it. A section the target does not depend on may stay unquoted. |
| 0001-extract | 21:10:21 | 2 | 21:11:32 | accepted | paper: 5361 lines, quotes 49, located 49, repeated 0, span [29, 4810], first_tenth 26, sections with quotes 27/56 |  |
| 0002-background | 21:11:39 | 1 | 21:12:12 | accepted |  |  |
| 0003-argument | 21:12:18 | 1 | 21:14:06 | accepted | paper: 5361 lines, quotes 16, located 16, repeated 0, span [76, 4985], first_tenth 7, sections with quotes 14/56 |  |

### M3

Planning from 21:10:21 to 21:14:27 UTC (4.1 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 26 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 21:10:21 | 1 | 21:11:11 | rejected | paper: 5361 lines, quotes 27, located 27, repeated 0, span [42, 435], first_tenth 27, sections with quotes 6/56 | answer rejected: it is drawn from part of the sources.  The quotes from `sources/paper.tex` come from lines 42–435 of its 5361 lines, and none comes from these sections, which develop results in theorems, lemmas, definitions or displayed equations: - §3 Two finite networks with a rank saving (lines 640–1346): 4 theorem-like statements, 8 displayed equations - §4 Faster interchange of address chunks (lines 1347–1762): 4 theorem-like statements, 2 displayed equations - §5 Fast simultaneous synthetic butterfly layers (lines 1763–2758): 2 theorem-like statements, 13 displayed equations - §6 Synthetic transforms and their tape layout (lines 2759–3207): 2 theorem-like statements, 5 displayed equations - §7 Exact normalized polynomial products (lines 3208–3495): 2 theorem-like statements, 2 displayed equations - §8 Resampling with the permutations left in the transform (lines 3496–3988): 3 theorem-like statements, 5 displayed equations - §9 Exact integer multiplication and its cost (lines 3989–4995): 0 theorem-like statements, 8 displayed equations - §A Packed additions on grouped rectangles (lines 5199–5361): 2 theorem-like statements, 1 displayed equations  An introduction summarises results; the sections after it develop them, and the target depends on that development. Read each source to its last line, in parts (the Read tool's offset and limit), and revise the answer: keep what holds, add what the target depends on, and quote each concept or step where the sources develop it rather than where the introduction mentions it. A section the target does not depend on may stay unquoted. |
| 0001-extract | 21:10:21 | 2 | 21:11:27 | accepted | paper: 5361 lines, quotes 55, located 55, repeated 1, span [42, 4810], first_tenth 28, sections with quotes 25/56 |  warnings: `lower-triangular-factorization`: no supporting quote from the sources |
| 0001-extract | 21:10:21 | 3 | 21:11:30 | error |  | `0001-extract` is not a pending task (run `exegenius next` to see the pending tasks) |
| 0002-background | 21:11:37 | 1 | 21:12:07 | accepted |  |  |
| 0003-argument | 21:12:15 | 1 | 21:14:23 | rejected | paper: 5361 lines, quotes 23, located 23, repeated 0, span [76, 4994], first_tenth 9, sections with quotes 23/56 | answer rejected: - step `S3.1`: `butterfly` in `from` does not come before the step's page `synthetic-transforms` in the reading order - step `S6`: `normalized-convolution` in `from` does not come before the step's page `phase-twist` in the reading order |
| 0003-argument | 21:12:15 | 2 | 21:14:27 | accepted | paper: 5361 lines, quotes 23, located 23, repeated 0, span [76, 4994], first_tenth 9, sections with quotes 23/56 |  |

### M4

Planning from 21:10:21 to 21:15:28 UTC (5.1 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 21 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 21:10:21 | 1 | 21:11:17 | rejected | paper: 5361 lines, quotes 25, located 25, repeated 1, span [29, 326], first_tenth 25, sections with quotes 6/56 | answer rejected: it is drawn from part of the sources.  The quotes from `sources/paper.tex` come from lines 29–326 of its 5361 lines, and none comes from these sections, which develop results in theorems, lemmas, definitions or displayed equations: - §2 The machine model and elementary streams (lines 432–639): 2 theorem-like statements, 1 displayed equations - §3 Two finite networks with a rank saving (lines 640–1346): 4 theorem-like statements, 8 displayed equations - §4 Faster interchange of address chunks (lines 1347–1762): 4 theorem-like statements, 2 displayed equations - §5 Fast simultaneous synthetic butterfly layers (lines 1763–2758): 2 theorem-like statements, 13 displayed equations - §6 Synthetic transforms and their tape layout (lines 2759–3207): 2 theorem-like statements, 5 displayed equations - §7 Exact normalized polynomial products (lines 3208–3495): 2 theorem-like statements, 2 displayed equations - §8 Resampling with the permutations left in the transform (lines 3496–3988): 3 theorem-like statements, 5 displayed equations - §9 Exact integer multiplication and its cost (lines 3989–4995): 0 theorem-like statements, 8 displayed equations - §A Packed additions on grouped rectangles (lines 5199–5361): 2 theorem-like statements, 1 displayed equations  An introduction summarises results; the sections after it develop them, and the target depends on that development. Read each source to its last line, in parts (the Read tool's offset and limit), and revise the answer: keep what holds, add what the target depends on, and quote each concept or step where the sources develop it rather than where the introduction mentions it. A section the target does not depend on may stay unquoted. |
| 0001-extract | 21:10:21 | 2 | 21:11:43 | accepted | paper: 5361 lines, quotes 51, located 51, repeated 2, span [29, 4825], first_tenth 27, sections with quotes 27/56 |  |
| 0002-background | 21:11:49 | 1 | 21:12:12 | accepted |  |  |
| 0003-argument | 21:12:18 | 1 | 21:14:10 | rejected | paper: 5361 lines, quotes 16, located 16, repeated 0, span [76, 209], first_tenth 16, sections with quotes 4/56 | answer rejected: - step `S7.2`: `address-interchange` in `from` does not come before the step's page `synthetic-transforms` in the reading order - step `S7.2`: `fast-butterfly-layers` in `from` does not come before the step's page `synthetic-transforms` in the reading order |
| 0003-argument | 21:12:18 | 2 | 21:14:12 | rejected | paper: 5361 lines, quotes 16, located 16, repeated 0, span [76, 209], first_tenth 16, sections with quotes 4/56 | answer rejected: it is drawn from part of the sources.  The quotes from `sources/paper.tex` come from lines 76–209 of its 5361 lines, and none comes from these sections, which develop results in theorems, lemmas, definitions or displayed equations: - §2 The machine model and elementary streams (lines 432–639): 2 theorem-like statements, 1 displayed equations - §3 Two finite networks with a rank saving (lines 640–1346): 4 theorem-like statements, 8 displayed equations - §4 Faster interchange of address chunks (lines 1347–1762): 4 theorem-like statements, 2 displayed equations - §5 Fast simultaneous synthetic butterfly layers (lines 1763–2758): 2 theorem-like statements, 13 displayed equations - §6 Synthetic transforms and their tape layout (lines 2759–3207): 2 theorem-like statements, 5 displayed equations - §7 Exact normalized polynomial products (lines 3208–3495): 2 theorem-like statements, 2 displayed equations - §8 Resampling with the permutations left in the transform (lines 3496–3988): 3 theorem-like statements, 5 displayed equations - §9 Exact integer multiplication and its cost (lines 3989–4995): 0 theorem-like statements, 8 displayed equations - §A Packed additions on grouped rectangles (lines 5199–5361): 2 theorem-like statements, 1 displayed equations  An introduction summarises results; the sections after it develop them, and the target depends on that development. Read each source to its last line, in parts (the Read tool's offset and limit), and revise the answer: keep what holds, add what the target depends on, and quote each concept or step where the sources develop it rather than where the introduction mentions it. A section the target does not depend on may stay unquoted. |
| 0003-argument | 21:12:18 | 3 | 21:15:28 | accepted | paper: 5361 lines, quotes 17, located 17, repeated 0, span [76, 4730], first_tenth 3, sections with quotes 24/56 |  |

### M5

Planning from 21:10:21 to 21:14:17 UTC (3.9 min, first issue to last accepted submit). After the argument was accepted, `exegenius next` issued 25 write tasks (not started).

| task | issued (UTC) | submit | at (UTC) | outcome | coverage check | message / warnings |
|---|---|---|---|---|---|---|
| 0001-extract | 21:10:21 | 1 | 21:11:16 | rejected | paper: 5361 lines, quotes 35, located 35, repeated 0, span [30, 1364], first_tenth 34, sections with quotes 9/56 | answer rejected: it is drawn from part of the sources.  The quotes from `sources/paper.tex` come from lines 30–1364 of its 5361 lines, and none comes from these sections, which develop results in theorems, lemmas, definitions or displayed equations: - §3 Two finite networks with a rank saving (lines 640–1346): 4 theorem-like statements, 8 displayed equations - §5 Fast simultaneous synthetic butterfly layers (lines 1763–2758): 2 theorem-like statements, 13 displayed equations - §6 Synthetic transforms and their tape layout (lines 2759–3207): 2 theorem-like statements, 5 displayed equations - §7 Exact normalized polynomial products (lines 3208–3495): 2 theorem-like statements, 2 displayed equations - §8 Resampling with the permutations left in the transform (lines 3496–3988): 3 theorem-like statements, 5 displayed equations - §9 Exact integer multiplication and its cost (lines 3989–4995): 0 theorem-like statements, 8 displayed equations - §A Packed additions on grouped rectangles (lines 5199–5361): 2 theorem-like statements, 1 displayed equations  An introduction summarises results; the sections after it develop them, and the target depends on that development. Read each source to its last line, in parts (the Read tool's offset and limit), and revise the answer: keep what holds, add what the target depends on, and quote each concept or step where the sources develop it rather than where the introduction mentions it. A section the target does not depend on may stay unquoted. |
| 0001-extract | 21:10:21 | 2 | 21:11:30 | accepted | paper: 5361 lines, quotes 53, located 53, repeated 1, span [30, 4546], first_tenth 34, sections with quotes 28/56 |  |
| 0002-background | 21:11:37 | 1 | 21:12:07 | accepted |  |  |
| 0003-argument | 21:12:12 | 1 | 21:13:41 | rejected | paper: 5361 lines, quotes 14, located 14, repeated 0, span [92, 210], first_tenth 14, sections with quotes 4/56 | answer rejected: it is drawn from part of the sources.  The quotes from `sources/paper.tex` come from lines 92–210 of its 5361 lines, and none comes from these sections, which develop results in theorems, lemmas, definitions or displayed equations: - §2 The machine model and elementary streams (lines 432–639): 2 theorem-like statements, 1 displayed equations - §3 Two finite networks with a rank saving (lines 640–1346): 4 theorem-like statements, 8 displayed equations - §4 Faster interchange of address chunks (lines 1347–1762): 4 theorem-like statements, 2 displayed equations - §5 Fast simultaneous synthetic butterfly layers (lines 1763–2758): 2 theorem-like statements, 13 displayed equations - §6 Synthetic transforms and their tape layout (lines 2759–3207): 2 theorem-like statements, 5 displayed equations - §7 Exact normalized polynomial products (lines 3208–3495): 2 theorem-like statements, 2 displayed equations - §8 Resampling with the permutations left in the transform (lines 3496–3988): 3 theorem-like statements, 5 displayed equations - §9 Exact integer multiplication and its cost (lines 3989–4995): 0 theorem-like statements, 8 displayed equations - §A Packed additions on grouped rectangles (lines 5199–5361): 2 theorem-like statements, 1 displayed equations  An introduction summarises results; the sections after it develop them, and the target depends on that development. Read each source to its last line, in parts (the Read tool's offset and limit), and revise the answer: keep what holds, add what the target depends on, and quote each concept or step where the sources develop it rather than where the introduction mentions it. A section the target does not depend on may stay unquoted. |
| 0003-argument | 21:12:12 | 2 | 21:14:17 | accepted | paper: 5361 lines, quotes 14, located 14, repeated 0, span [92, 4771], first_tenth 1, sections with quotes 21/56 |  |

