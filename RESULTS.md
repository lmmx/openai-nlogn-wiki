# Results: experiment 131026 depth rejection

Runner session `session_01QrXZe3XFX3p2659Xcrczwf` executed EXPERIMENT.md on 2026-10-13. This file reports facts only.
Times are in UTC. Per-submit data comes from `runs/RUN/exegenius/log.jsonl`. Subagent transcripts are in
`results/transcripts/`.

## Versions

- exegenius: 0.6.0, clone commit `f70a919a9476e16219d0c80e9a035d588fd9df53` (`git rev-parse --short HEAD` → `f70a919`;
  the branch `131026-depth-rejection` was cloned with `--depth 1`, and its HEAD was f70a919, so no checkout was needed).
  Built with `cargo build --release`, copied to `/usr/local/bin/exegenius`; `exegenius --version` → `exegenius 0.6.0`.
- Claude Code: 2.1.296 (`results/versions.txt`).
- Runner session model: `claude-opus-5-5` (`get_session`: `session_context.model` and `last_served_model`).
- Planner subagents: `exegenius-planner` definition says `model: sonnet`. Every assistant message across the 30
  subagent transcripts records model `claude-sonnet-5-5` (386 messages).

## Steps

1. `exegenius-planner` **was offered** as a subagent type at session start.
2. `add_repo` (lmmx/exegenius, `access: "push"`) succeeded. Cloned to `/home/user/exegenius`. Built in 1m 49s.
   The `add_repo` result asked for `register_repo_root` to be called to load the exegenius repo's CLAUDE.md/skills;
   the runner did **not** call it (not part of the protocol). Nothing was pushed to lmmx/exegenius.
3. `./setup-run.sh` for C1–C5 (`sections`) and D1–D5 (`results`): all ten printed `ready`.
4. All ten runs started together at 18:06:18 (first `exegenius next` in each at 18:06:16–18:06:18). Each run was
   advanced as its subagent reported. Every planning task (extract, background, argument; no extend task was issued
   in any run) went to a fresh `exegenius-planner` subagent with the prompt `exegenius next` printed, verbatim.
   30 subagents total, all of type `exegenius-planner` (confirmed in each transcript's `.meta.json`). All 30 replied
   `accepted`. **No restarts.** When `exegenius next` printed the reader profile (once per run, after background),
   the runner ran `exegenius next` again immediately. Each run was stopped when `exegenius next` handed out write
   tasks; no write task was started. The runner read no `paper.tex`, task or answer file.
5. `./collect.sh` ran after all ten stopped (8.3M of transcripts).

## Summary per run

"results quoted" = `quoted_results/results` from the `coverage` record of the accepted submit (the log records it
under both depths). "planning seconds" = first task issued → write tasks issued.

| run | depth | extract submits | background submits | argument submits | extract quotes (accepted) | extract results quoted (accepted) | argument quotes (accepted) | argument results quoted (accepted) | write tasks | planning seconds |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | sections | 2 | 1 | 3 | 33 | 9/66 | 17 | 1/66 | 17 | 358 |
| C2 | sections | 2 | 1 | 3 | 49 | 16/66 | 22 | 9/66 | 25 | 292 |
| C3 | sections | 2 | 1 | 1 | 38 | 2/66 | 30 | 11/66 | 28 | 268 |
| C4 | sections | 1 | 1 | 2 | 42 | 2/66 | 30 | 5/66 | 27 | 315 |
| C5 | sections | 3 | 1 | 2 | 58 | 16/66 | 23 | 10/66 | 27 | 244 |
| D1 | results | 4 | 1 | 2 | 71 | 28/66 | 23 | 10/66 | 24 | 268 |
| D2 | results | 1 | 1 | 2 | 58 | 14/66 | 35 | 16/66 | 31 | 324 |
| D3 | results | 4 | 1 | 2 | 64 | 23/66 | 25 | 14/66 | 29 | 284 |
| D4 | results | 2 | 1 | 4 | 56 | 20/66 | 22 | 14/66 | 25 | 345 |
| D5 | results | 2 | 1 | 2 | 79 | 39/66 | 28 | 19/66 | 26 | 304 |

### C1 (`coverage_depth = "sections"`)

| task | attempt | time (UTC) | outcome | check | coverage (from log) | message (first line) |
|---|---|---|---|---|---|---|
| 0001-extract | 1 | 18:09:31 | rejected | coverage | quotes 17/17 located, span [41, 432], results quoted 1/66, unquoted statements 22/23, top-level result-bearing sections with no quote: 8 | answer rejected: it is drawn from part of the sources. |
| 0001-extract | 2 | 18:09:41 | accepted |  | quotes 33/33 located, span [41, 4810], results quoted 9/66, unquoted statements 13/23, top-level result-bearing sections with no quote: 1 |  |
| 0001-extract | — | issued 18:06:16 | accepted after 205s | | | |
| 0002-background | 1 | 18:10:06 | accepted |  |  |  |
| 0002-background | — | issued 18:09:46 | accepted after 20s | | | |
| 0003-argument | 1 | 18:11:14 | rejected |  | quotes 17/17 located, span [76, 443], results quoted 0/66, unquoted statements 23/23, top-level result-bearing sections with no quote: 8 | answer rejected: - step `S6`: `signed-packing` in `from` does not come before the step's page `fixed-point-precision` in the reading order |
| 0003-argument | 2 | 18:11:17 | rejected | coverage | quotes 17/17 located, span [76, 443], results quoted 0/66, unquoted statements 23/23, top-level result-bearing sections with no quote: 8 | answer rejected: it is drawn from part of the sources. |
| 0003-argument | 3 | 18:12:03 | accepted |  | quotes 17/17 located, span [76, 4810], results quoted 1/66, unquoted statements 19/23, top-level result-bearing sections with no quote: 1 |  |
| 0003-argument | — | issued 18:10:11 | accepted after 113s | | | |

Planning from first issue 18:06:16 to write tasks issued 18:12:14 (358s); 17 write tasks issued, none started.

### C2 (`coverage_depth = "sections"`)

| task | attempt | time (UTC) | outcome | check | coverage (from log) | message (first line) |
|---|---|---|---|---|---|---|
| 0001-extract | 1 | 18:07:21 | rejected | coverage | quotes 30/30 located, span [32, 438], results quoted 1/66, unquoted statements 22/23, top-level result-bearing sections with no quote: 8 | answer rejected: it is drawn from part of the sources. |
| 0001-extract | 2 | 18:07:43 | accepted |  | quotes 49/49 located, span [32, 5259], results quoted 16/66, unquoted statements 6/23, top-level result-bearing sections with no quote: 0 |  |
| 0001-extract | — | issued 18:06:18 | accepted after 84s | | | |
| 0002-background | 1 | 18:08:25 | accepted |  |  |  |
| 0002-background | — | issued 18:07:50 | accepted after 34s | | | |
| 0003-argument | 1 | 18:10:36 | rejected |  | quotes 22/22 located, span [41, 2588], results quoted 4/66, unquoted statements 17/23, top-level result-bearing sections with no quote: 7 | answer rejected: - step `S4.1`: `controlled-shifts` in `from` does not come before the step's page `cyclic-crt-axes` in the reading order |
| 0003-argument | 2 | 18:10:41 | rejected | coverage | quotes 22/22 located, span [41, 2588], results quoted 4/66, unquoted statements 17/23, top-level result-bearing sections with no quote: 7 | answer rejected: it is drawn from part of the sources. |
| 0003-argument | 3 | 18:11:04 | accepted |  | quotes 22/22 located, span [41, 4808], results quoted 9/66, unquoted statements 12/23, top-level result-bearing sections with no quote: 2 |  |
| 0003-argument | — | issued 18:08:29 | accepted after 156s | | | |

Planning from first issue 18:06:18 to write tasks issued 18:11:11 (292s); 25 write tasks issued, none started.

### C3 (`coverage_depth = "sections"`)

| task | attempt | time (UTC) | outcome | check | coverage (from log) | message (first line) |
|---|---|---|---|---|---|---|
| 0001-extract | 1 | 18:07:31 | error |  |  | no answer yet: write it to exegenius/tasks/0001-extract.answer.json |
| 0001-extract | 2 | 18:07:34 | accepted |  | quotes 38/38 located, span [41, 4530], results quoted 2/66, unquoted statements 18/23, top-level result-bearing sections with no quote: 3 |  |
| 0001-extract | — | issued 18:06:18 | accepted after 76s | | | |
| 0002-background | 1 | 18:08:04 | accepted |  |  |  |
| 0002-background | — | issued 18:07:39 | accepted after 25s | | | |
| 0003-argument | 1 | 18:10:41 | accepted |  | quotes 30/30 located, span [91, 4994], results quoted 11/66, unquoted statements 11/23, top-level result-bearing sections with no quote: 3 |  |
| 0003-argument | — | issued 18:08:14 | accepted after 147s | | | |

Planning from first issue 18:06:18 to write tasks issued 18:10:47 (268s); 28 write tasks issued, none started.

### C4 (`coverage_depth = "sections"`)

| task | attempt | time (UTC) | outcome | check | coverage (from log) | message (first line) |
|---|---|---|---|---|---|---|
| 0001-extract | 1 | 18:07:47 | accepted |  | quotes 42/42 located, span [32, 4016], results quoted 2/66, unquoted statements 17/23, top-level result-bearing sections with no quote: 2 |  |
| 0001-extract | — | issued 18:06:18 | accepted after 88s | | | |
| 0002-background | 1 | 18:08:21 | accepted |  |  |  |
| 0002-background | — | issued 18:07:53 | accepted after 27s | | | |
| 0003-argument | 1 | 18:11:18 | rejected |  | quotes 30/30 located, span [92, 4810], results quoted 5/66, unquoted statements 12/23, top-level result-bearing sections with no quote: 1 | answer rejected: - step `S5.2`: `butterfly-h0` in `from` does not come before the step's page `synthetic-transform` in the reading order |
| 0003-argument | 2 | 18:11:21 | accepted |  | quotes 30/30 located, span [92, 4810], results quoted 5/66, unquoted statements 12/23, top-level result-bearing sections with no quote: 1; warnings: 2 |  |
| 0003-argument | — | issued 18:08:29 | accepted after 173s | | | |

Planning from first issue 18:06:18 to write tasks issued 18:11:33 (315s); 27 write tasks issued, none started.

### C5 (`coverage_depth = "sections"`)

| task | attempt | time (UTC) | outcome | check | coverage (from log) | message (first line) |
|---|---|---|---|---|---|---|
| 0001-extract | 1 | 18:07:26 | rejected |  | quotes 27/27 located, span [39, 440], results quoted 1/66, unquoted statements 22/23, top-level result-bearing sections with no quote: 8 | answer rejected: - `butterfly-layer`: `u` does not occur in the mathematics of the title "Two-point butterfly $H_0$" |
| 0001-extract | 2 | 18:07:30 | rejected | coverage | quotes 27/27 located, span [39, 440], results quoted 1/66, unquoted statements 22/23, top-level result-bearing sections with no quote: 8 | answer rejected: it is drawn from part of the sources. |
| 0001-extract | 3 | 18:07:52 | accepted |  | quotes 58/58 located, span [39, 4810], results quoted 16/66, unquoted statements 9/23, top-level result-bearing sections with no quote: 1 |  |
| 0001-extract | — | issued 18:06:19 | accepted after 93s | | | |
| 0002-background | 1 | 18:08:30 | accepted |  |  |  |
| 0002-background | — | issued 18:08:03 | accepted after 27s | | | |
| 0003-argument | 1 | 18:10:11 | rejected |  | quotes 23/23 located, span [92, 4810], results quoted 10/66, unquoted statements 11/23, top-level result-bearing sections with no quote: 1 | answer rejected: - step `S5`: `fast-butterfly-layers` in `from` does not come before the step's page `synthetic-transforms` in the reading order |
| 0003-argument | 2 | 18:10:15 | accepted |  | quotes 23/23 located, span [92, 4810], results quoted 10/66, unquoted statements 11/23, top-level result-bearing sections with no quote: 1; warnings: 2 |  |
| 0003-argument | — | issued 18:08:38 | accepted after 97s | | | |

Planning from first issue 18:06:19 to write tasks issued 18:10:22 (244s); 27 write tasks issued, none started.

### D1 (`coverage_depth = "results"`)

| task | attempt | time (UTC) | outcome | check | coverage (from log) | message (first line) |
|---|---|---|---|---|---|---|
| 0001-extract | 1 | 18:07:31 | rejected |  | quotes 36/37 located, span [32, 4530], results quoted 1/66, unquoted statements 22/23, top-level result-bearing sections with no quote: 6 | answer rejected: - `simultaneous-butterfly-layer`: quote not found verbatim in source `paper`: "we will obtain cost $O(Vd^{\lambda'})$" |
| 0001-extract | 2 | 18:07:34 | rejected | coverage | quotes 37/37 located, span [32, 4530], results quoted 1/66, unquoted statements 22/23, top-level result-bearing sections with no quote: 5 | answer rejected: it is drawn from part of the sources. |
| 0001-extract | 3 | 18:07:53 | rejected |  | quotes 70/71 located, span [32, 5210], results quoted 27/66, unquoted statements 4/23, top-level result-bearing sections with no quote: 0 | answer rejected: - `packed-selected-bit-addition`: quote not found verbatim in source `paper`: "At the positions |
| 0001-extract | 4 | 18:07:58 | accepted |  | quotes 71/71 located, span [32, 5264], results quoted 28/66, unquoted statements 4/23, top-level result-bearing sections with no quote: 0 |  |
| 0001-extract | — | issued 18:06:16 | accepted after 102s | | | |
| 0002-background | 1 | 18:08:32 | accepted |  |  |  |
| 0002-background | — | issued 18:08:03 | accepted after 29s | | | |
| 0003-argument | 1 | 18:10:34 | rejected |  | quotes 23/23 located, span [92, 4810], results quoted 10/66, unquoted statements 12/23, top-level result-bearing sections with no quote: 1 | answer rejected: - step `S4`: `simultaneous-butterfly-layer` in `from` does not come before the step's page `synthetic-transform` in the reading order |
| 0003-argument | 2 | 18:10:39 | accepted |  | quotes 23/23 located, span [92, 4810], results quoted 10/66, unquoted statements 12/23, top-level result-bearing sections with no quote: 1; warnings: 2 |  |
| 0003-argument | — | issued 18:08:38 | accepted after 121s | | | |

Planning from first issue 18:06:16 to write tasks issued 18:10:44 (268s); 24 write tasks issued, none started.

### D2 (`coverage_depth = "results"`)

| task | attempt | time (UTC) | outcome | check | coverage (from log) | message (first line) |
|---|---|---|---|---|---|---|
| 0001-extract | 1 | 18:07:56 | accepted |  | quotes 58/58 located, span [32, 4837], results quoted 14/66, unquoted statements 8/23, top-level result-bearing sections with no quote: 1 |  |
| 0001-extract | — | issued 18:06:19 | accepted after 98s | | | |
| 0002-background | 1 | 18:08:31 | accepted |  |  |  |
| 0002-background | — | issued 18:08:03 | accepted after 28s | | | |
| 0003-argument | 1 | 18:11:33 | rejected |  | quotes 35/35 located, span [76, 4987], results quoted 16/66, unquoted statements 9/23, top-level result-bearing sections with no quote: 2 | answer rejected: - step `S6`: `multiplication-algorithm` in `from` does not come before the step's page `exact-recovery` in the reading order |
| 0003-argument | 2 | 18:11:37 | accepted |  | quotes 35/35 located, span [76, 4987], results quoted 16/66, unquoted statements 9/23, top-level result-bearing sections with no quote: 2; warnings: 1 |  |
| 0003-argument | — | issued 18:08:38 | accepted after 179s | | | |

Planning from first issue 18:06:19 to write tasks issued 18:11:43 (324s); 31 write tasks issued, none started.

### D3 (`coverage_depth = "results"`)

| task | attempt | time (UTC) | outcome | check | coverage (from log) | message (first line) |
|---|---|---|---|---|---|---|
| 0001-extract | 1 | 18:07:10 | error |  |  | no answer yet: write it to exegenius/tasks/0001-extract.answer.json |
| 0001-extract | 2 | 18:07:14 | rejected | coverage | quotes 20/20 located, span [41, 435], results quoted 1/66, unquoted statements 22/23, top-level result-bearing sections with no quote: 8 | answer rejected: it is drawn from part of the sources. |
| 0001-extract | 3 | 18:07:25 | rejected | coverage | quotes 40/40 located, span [41, 4825], results quoted 6/66, unquoted statements 14/23, top-level result-bearing sections with no quote: 1 | answer rejected: it is drawn from part of the sources. |
| 0001-extract | 4 | 18:07:46 | accepted |  | quotes 64/64 located, span [41, 5259], results quoted 23/66, unquoted statements 2/23, top-level result-bearing sections with no quote: 0 |  |
| 0001-extract | — | issued 18:06:19 | accepted after 88s | | | |
| 0002-background | 1 | 18:08:22 | accepted |  |  |  |
| 0002-background | — | issued 18:07:53 | accepted after 29s | | | |
| 0003-argument | 1 | 18:10:52 | rejected |  | quotes 25/25 located, span [43, 4810], results quoted 14/66, unquoted statements 8/23, top-level result-bearing sections with no quote: 2 | answer rejected: - step `S4.3`: `tensor-resampling` in `from` does not come before the step's page `bluestein-chirp` in the reading order |
| 0003-argument | 2 | 18:10:56 | accepted |  | quotes 25/25 located, span [43, 4810], results quoted 14/66, unquoted statements 8/23, top-level result-bearing sections with no quote: 2; warnings: 11 |  |
| 0003-argument | — | issued 18:08:29 | accepted after 147s | | | |

Planning from first issue 18:06:19 to write tasks issued 18:11:02 (284s); 29 write tasks issued, none started.

### D4 (`coverage_depth = "results"`)

| task | attempt | time (UTC) | outcome | check | coverage (from log) | message (first line) |
|---|---|---|---|---|---|---|
| 0001-extract | 1 | 18:07:21 | rejected | coverage | quotes 25/25 located, span [28, 435], results quoted 0/66, unquoted statements 22/23, top-level result-bearing sections with no quote: 8 | answer rejected: it is drawn from part of the sources. |
| 0001-extract | 2 | 18:07:37 | accepted |  | quotes 56/56 located, span [28, 5210], results quoted 20/66, unquoted statements 1/23, top-level result-bearing sections with no quote: 0 |  |
| 0001-extract | — | issued 18:06:19 | accepted after 78s | | | |
| 0002-background | 1 | 18:08:11 | accepted |  |  |  |
| 0002-background | — | issued 18:07:43 | accepted after 28s | | | |
| 0003-argument | 1 | 18:10:21 | rejected | coverage | quotes 22/22 located, span [39, 438], results quoted 0/66, unquoted statements 22/23, top-level result-bearing sections with no quote: 8 | answer rejected: it is drawn from part of the sources. |
| 0003-argument | 2 | 18:11:42 | rejected | coverage | quotes 22/22 located, span [39, 438], results quoted 0/66, unquoted statements 22/23, top-level result-bearing sections with no quote: 8 | answer rejected: it is drawn from part of the sources. |
| 0003-argument | 3 | 18:11:53 | rejected |  | quotes 22/22 located, span [39, 4994], results quoted 14/66, unquoted statements 11/23, top-level result-bearing sections with no quote: 1 | answer rejected: - step `S1.3` quotes the sources before step `S1.2`, which comes earlier in the plan: the sources report the plan depth first, so reorder the steps, or mark `S1.3` deferred if the sources report it ou |
| 0003-argument | 4 | 18:11:57 | accepted |  | quotes 22/22 located, span [39, 4994], results quoted 14/66, unquoted statements 11/23, top-level result-bearing sections with no quote: 1; warnings: 2 |  |
| 0003-argument | — | issued 18:08:24 | accepted after 214s | | | |

Planning from first issue 18:06:19 to write tasks issued 18:12:04 (345s); 25 write tasks issued, none started.

### D5 (`coverage_depth = "results"`)

| task | attempt | time (UTC) | outcome | check | coverage (from log) | message (first line) |
|---|---|---|---|---|---|---|
| 0001-extract | 1 | 18:07:42 | rejected | coverage | quotes 35/35 located, span [41, 4198], results quoted 5/66, unquoted statements 16/23, top-level result-bearing sections with no quote: 4 | answer rejected: it is drawn from part of the sources. |
| 0001-extract | 2 | 18:08:09 | accepted |  | quotes 79/79 located, span [41, 5259], results quoted 39/66, unquoted statements 1/23, top-level result-bearing sections with no quote: 0 |  |
| 0001-extract | — | issued 18:06:19 | accepted after 110s | | | |
| 0002-background | 1 | 18:08:41 | accepted |  |  |  |
| 0002-background | — | issued 18:08:14 | accepted after 27s | | | |
| 0003-argument | 1 | 18:11:12 | rejected |  | quotes 28/28 located, span [92, 4983], results quoted 19/66, unquoted statements 7/23, top-level result-bearing sections with no quote: 1 | answer rejected: - `lower-triangular-shear` presents both step `S1.4.0` and step `S1.4.1`; give a page one step |
| 0003-argument | 2 | 18:11:18 | accepted |  | quotes 28/28 located, span [92, 4983], results quoted 19/66, unquoted statements 7/23, top-level result-bearing sections with no quote: 1 |  |
| 0003-argument | — | issued 18:08:47 | accepted after 151s | | | |

Planning from first issue 18:06:19 to write tasks issued 18:11:23 (304s); 26 write tasks issued, none started.

Outcome `error` (C3 extract attempt 1): `exegenius submit` was run before the answer file existed ("no answer yet").

## Restarts, failures, deviations, unexpected events

- **Restarts:** none.
- **C1 0001-extract, a shell command hung, and a broad `pkill` followed.** At about 18:07:10 the planner ran a Bash command that
  began `cat > exegenius/tasks/0001-extract/mk.py 2>/dev/null || mkdir -p ...; cat > ...mk.py <<'EOF'`.
  The first `cat >` had no heredoc and waited on standard input. The command blocked until the 120 s Bash timeout. It was moved to the
  background (ID `b6bb27qdf`) at 18:09:10. The planner then `cat`-ed that background task's output file,
  `/tmp/claude-0/-home-user-openai-nlogn-wiki/d32d25fb-.../tasks/b6bb27qdf.output`. That is a shared session temp path
  outside its run directory, though the file was its own command's output. At 18:09:15 it ran
  `pkill -f "cat >"` (exit code 144), which matches any process on the machine whose command line contains
  `cat >`, not only its own. It then wrote `mk.py` with the Write tool and continued. No other subagent transcript shows a
  killed or interrupted command (searched for exit codes 13x/14x, "Terminated", "Killed"). This hang is why
  C1's extract took 205 s and C1 finished last.
- **D4 0002-background:** its single Bash command began `cd /home/user/exegenius 2>/dev/null;` (the exegenius
  clone, outside its run directory), then immediately `cd /home/user/openai-nlogn-wiki/runs/D4` and wrote its
  answer there. It read or wrote nothing in `/home/user/exegenius`.
- No planner tool call references another run's directory (all subagent tool inputs searched for `runs/C*`/`runs/D*`
  paths other than their own, and for `/tmp`; only the two items above were found).
- No extend task was issued in any run: each went extract → background → (reader printed) → argument → write.
- Stop hook: during the runs the session's stop hook repeatedly asked to commit untracked files. The runner did not
  commit until step 7.
