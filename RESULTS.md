# Results: experiment 131026-2 (A3–A6, B3–B6)

Runner session: session_016hUw8KoTNEQrXHMBkGKMAF. All times are UTC, 2026-10-13.

## Versions

- exegenius: 0.6.0, built from lmmx/exegenius commit `1d90c28da6690820913760451ff084012aab0689` (branch `timing-and-parallelism`). `exegenius --version` printed `exegenius 0.6.0`, and `git rev-parse --short HEAD` printed `1d90c28`.
- Claude Code: 2.1.296.
- Model of this runner session: `claude-opus-5-5`, from `get_session` (`session_context.model` and `last_served_model`). The subagents' models are set by their definitions in `.claude/agents/`; their transcripts record the model of each turn.
- See `results/versions.txt`.

## Steps 1–3

1. `exegenius-planner` was offered as a subagent type, along with `exegenius-reader` and `exegenius-task`.
2. `add_repo` (lmmx/exegenius, `access: "push"`) succeeded. The clone was `git clone --depth 50 --branch timing-and-parallelism` rather than the `--depth 1` default-branch command `add_repo` suggested, so that commit `1d90c28` was in the history. After checking out `1d90c28`, `cargo build --release` finished in 1m48s, and the binary was copied to `/usr/local/bin`. Nothing was pushed to lmmx/exegenius.
3. `./setup-run.sh` was run for A3–A6 with `report` and for B3–B6 with `reject`.

## Step 4: subagent types and restarts

- 24 subagents were started, all of type `exegenius-planner`: 8 runs × 3 planning tasks (extract, background, argument). The types are in each `results/transcripts/*/*/subagents/*.meta.json`. No `extend` task was handed out in any run.
- Every subagent replied `accepted`, so none was restarted.
- Each prompt was passed word for word as `exegenius next` printed it.
- In every run, `exegenius next` printed the reader profile once, after the background task. Each time, `exegenius next` was run again.
- Each run was stopped at the first `exegenius next` that handed out write tasks. No write task was started.

| run | mode | write tasks handed out at stop |
|---|---|---|
| A3 | report | 24 |
| A4 | report | 24 |
| A5 | report | 21 |
| A6 | report | 19 |
| B3 | reject | 24 |
| B4 | reject | 26 |
| B5 | reject | 34 |
| B6 | reject | 25 |

## Per-run submits (from `runs/RUN/exegenius/log.jsonl`)

Only 2 of the 39 planning submits carry `check`: B3 0001-extract attempts 1 and 2, both `"coverage"`. In the tables, "warnings" is the number of entries in the submit's `warnings` field; messages are cut to their first lines. Full events are in the logs.

### A3

| task | issued | submit | at | outcome | check | warnings | message (first line) |
|---|---|---|---|---|---|---|---|
| 0001-extract | 17:39:29 | 1 | 17:40:32 | rejected |  |  | answer rejected: / - `main-theorem`: quote not found verbatim in source `paper`: "$T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right)," |
| 0001-extract | 17:39:29 | 2 | 17:40:38 | accepted |  |  |  |
| 0002-background | 17:40:47 | 1 | 17:41:11 | accepted |  |  |  |
| 0003-argument | 17:41:15 | 1 | 17:44:01 | rejected |  |  | answer rejected: / - step `S1.2.2`: `restoring-auxiliary` in `from` does not come before the step's page `linear-networks-frames` in the reading order / - `recursive-saving` presents both step `S1.2` and step `S1.2.4`; g |
| 0003-argument | 17:41:15 | 2 | 17:44:06 | accepted |  |  |  |

Planning: first task issued 17:39:29, last planning submit 17:44:06 UTC (4.6 min). Write tasks issued: 24.

### A4

| task | issued | submit | at | outcome | check | warnings | message (first line) |
|---|---|---|---|---|---|---|---|
| 0001-extract | 17:39:29 | 1 | 17:40:28 | rejected |  |  | answer rejected: / - `address-shear`: quote not found verbatim in source `paper`: "the endpoint operator is an address shear:" |
| 0001-extract | 17:39:29 | 2 | 17:40:31 | accepted |  |  |  |
| 0002-background | 17:40:40 | 1 | 17:40:59 | accepted |  |  |  |
| 0003-argument | 17:41:07 | 1 | 17:42:34 | rejected |  |  | answer rejected: / - `ring-products` presents both step `S3.5.2` and step `S3.5.2.2`; give a page one step |
| 0003-argument | 17:41:07 | 2 | 17:42:37 | accepted |  | 5 |  |

Planning: first task issued 17:39:29, last planning submit 17:42:37 UTC (3.1 min). Write tasks issued: 24.

### A5

| task | issued | submit | at | outcome | check | warnings | message (first line) |
|---|---|---|---|---|---|---|---|
| 0001-extract | 17:39:29 | 1 | 17:40:29 | accepted |  |  |  |
| 0002-background | 17:40:36 | 1 | 17:41:00 | accepted |  |  |  |
| 0003-argument | 17:41:11 | 1 | 17:42:25 | accepted |  | 4 |  |

Planning: first task issued 17:39:29, last planning submit 17:42:25 UTC (2.9 min). Write tasks issued: 21.

### A6

| task | issued | submit | at | outcome | check | warnings | message (first line) |
|---|---|---|---|---|---|---|---|
| 0001-extract | 17:39:29 | 1 | 17:40:22 | accepted |  |  |  |
| 0002-background | 17:40:26 | 1 | 17:40:47 | accepted |  |  |  |
| 0003-argument | 17:40:56 | 1 | 17:41:51 | rejected |  |  | answer rejected: / - step `S6`: `phase-twist` in `from` does not come before the step's page `synthetic-transforms` in the reading order |
| 0003-argument | 17:40:56 | 2 | 17:41:54 | accepted |  | 7 |  |

Planning: first task issued 17:39:29, last planning submit 17:41:54 UTC (2.4 min). Write tasks issued: 19.

### B3

| task | issued | submit | at | outcome | check | warnings | message (first line) |
|---|---|---|---|---|---|---|---|
| 0001-extract | 17:39:29 | 1 | 17:40:35 | rejected | "coverage" |  | answer rejected: it is drawn from part of the sources. /  / The quotes from `sources/paper.tex` come from lines 28–1364 of its 5361 lines, and none comes from these sections, which develop results in theorems, lemmas, de |
| 0001-extract | 17:39:29 | 2 | 17:41:04 | rejected | "coverage" |  | answer rejected: it is drawn from part of the sources. /  / The quotes from `sources/paper.tex` come from lines 28–1364 of its 5361 lines, and none comes from these sections, which develop results in theorems, lemmas, de |
| 0001-extract | 17:39:29 | 3 | 17:41:44 | rejected |  |  | answer rejected: / - `poly-ring-mod-yr1`: quote not found verbatim in source `paper`: "$\mathcal R_r=\mathbb C[y]/(y^r+1)$" |
| 0001-extract | 17:39:29 | 4 | 17:41:49 | accepted |  |  |  |
| 0002-background | 17:41:56 | 1 | 17:42:22 | accepted |  |  |  |
| 0003-argument | 17:42:26 | 1 | 17:45:07 | rejected |  |  | answer rejected: / - step `S3.4`: `transform-layout` in `from` does not come before the step's page `exact-ring-products` in the reading order |
| 0003-argument | 17:42:26 | 2 | 17:45:12 | accepted |  | 1 |  |

Planning: first task issued 17:39:29, last planning submit 17:45:12 UTC (5.7 min). Write tasks issued: 24.

### B4

| task | issued | submit | at | outcome | check | warnings | message (first line) |
|---|---|---|---|---|---|---|---|
| 0001-extract | 17:39:29 | 1 | 17:40:38 | rejected |  |  | answer rejected: / - `butterfly-h0`: quote not found verbatim in source `paper`: "$H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr)$" / - `main-theorem`: quote not found verbatim in source `paper`: "$T_A(n)=O\!\left(n(\lg n)^{1-\kap |
| 0001-extract | 17:39:29 | 2 | 17:40:42 | accepted |  |  |  |
| 0002-background | 17:40:51 | 1 | 17:41:12 | accepted |  |  |  |
| 0003-argument | 17:41:21 | 1 | 17:42:43 | rejected |  |  | answer rejected: / - step `S2`: `simultaneous-butterfly-layer` in `from` does not come before the step's page `synthetic-transform` in the reading order / - step `S2`: `fast-address-interchange` in `from` does not come b |
| 0003-argument | 17:41:21 | 2 | 17:42:47 | accepted |  |  |  |

Planning: first task issued 17:39:29, last planning submit 17:42:47 UTC (3.3 min). Write tasks issued: 26.

### B5

| task | issued | submit | at | outcome | check | warnings | message (first line) |
|---|---|---|---|---|---|---|---|
| 0001-extract | 17:39:29 | 1 | 17:41:25 | rejected |  |  | answer rejected: / - `synthetic-ring`: `\mathbb C` does not occur in the mathematics of the title "Polynomial ring modulo $y^r+1$" |
| 0001-extract | 17:39:29 | 2 | 17:41:28 | accepted |  |  |  |
| 0002-background | 17:41:32 | 1 | 17:41:59 | accepted |  |  |  |
| 0003-argument | 17:42:05 | 1 | 17:45:07 | rejected |  |  | answer rejected: / - step `S3.4`: quote not found in source `paper` word for word: "$(p,h,g,d,z)\longmapsto(p,d,g,h,z)$" |
| 0003-argument | 17:42:05 | 2 | 17:45:10 | rejected |  |  | answer rejected: / - step `S3.4`: quote not found in source `paper` word for word: "$(p,h,g,d,z)\longmapsto(p,d,g,h,z)$" |
| 0003-argument | 17:42:05 | 3 | 17:45:21 | accepted |  | 2 |  |

Planning: first task issued 17:39:29, last planning submit 17:45:21 UTC (5.9 min). Write tasks issued: 34.

### B6

| task | issued | submit | at | outcome | check | warnings | message (first line) |
|---|---|---|---|---|---|---|---|
| 0001-extract | 17:39:29 | 1 | 17:40:34 | accepted |  |  |  |
| 0002-background | 17:40:44 | 1 | 17:41:10 | accepted |  |  |  |
| 0003-argument | 17:41:15 | 1 | 17:43:17 | rejected |  |  | answer rejected: / - step `S4`: `simultaneous-butterfly-layers` in `from` does not come before the step's page `synthetic-transforms` in the reading order / - step `S5.2`: `hh-subroutine` in `from` does not come before t |
| 0003-argument | 17:41:15 | 2 | 17:43:28 | accepted |  | 1 |  |

Planning: first task issued 17:39:29, last planning submit 17:43:28 UTC (4.0 min). Write tasks issued: 25.

### Coverage of each planning submit (the `coverage` field of the submit event)

| run | task | attempt | outcome | quotes | located | span (lines of 5361) |
|---|---|---|---|---|---|---|
| A3 | extract | 1 | rejected | 23 | 22 | 76–4306 |
| A3 | extract | 2 | accepted | 32 | 32 | 28–1364 |
| A3 | argument | 1 | rejected | 23 | 23 | 76–4854 |
| A3 | argument | 2 | accepted | 23 | 23 | 76–4854 |
| A4 | extract | 1 | rejected | 38 | 37 | 30–446 |
| A4 | extract | 2 | accepted | 38 | 38 | 30–446 |
| A4 | argument | 1 | rejected | 18 | 18 | 76–325 |
| A4 | argument | 2 | accepted | 18 | 18 | 76–325 |
| A5 | extract | 1 | accepted | 24 | 24 | 41–438 |
| A5 | argument | 1 | accepted | 17 | 17 | 76–210 |
| A6 | extract | 1 | accepted | 31 | 31 | 29–555 |
| A6 | argument | 1 | rejected | 16 | 16 | 76–209 |
| A6 | argument | 2 | accepted | 16 | 16 | 76–209 |
| B3 | extract | 1 | rejected (coverage) | 32 | 32 | 28–1364 |
| B3 | extract | 2 | rejected (coverage) | 32 | 32 | 28–1364 |
| B3 | extract | 3 | rejected | 47 | 46 | 28–4812 |
| B3 | extract | 4 | accepted | 47 | 47 | 28–4812 |
| B3 | argument | 1 | rejected | 25 | 25 | 41–4983 |
| B3 | argument | 2 | accepted | 25 | 25 | 41–4983 |
| B4 | extract | 1 | rejected | 37 | 35 | 30–4488 |
| B4 | extract | 2 | accepted | 37 | 37 | 30–4488 |
| B4 | argument | 1 | rejected | 23 | 23 | 491–4985 |
| B4 | argument | 2 | accepted | 23 | 23 | 491–4985 |
| B5 | extract | 1 | rejected | 38 | 38 | 28–4808 |
| B5 | extract | 2 | accepted | 38 | 38 | 28–4808 |
| B5 | argument | 1 | rejected | 35 | 34 | 92–4983 |
| B5 | argument | 2 | rejected | 35 | 34 | 92–4983 |
| B5 | argument | 3 | accepted | 35 | 35 | 92–4983 |
| B6 | extract | 1 | accepted | 25 | 25 | 28–3515 |
| B6 | argument | 1 | rejected | 29 | 29 | 76–4983 |
| B6 | argument | 2 | accepted | 29 | 29 | 76–4983 |

## Deviations, incidents and unexpected events

1. **Planner subagents in different runs shared a scratch file, `/tmp/claude-0/gen.py`.** Several planners wrote their answer-generating Python script to the same path outside their run directory:
   - A5 extract at 17:40:28;
   - B3 extract at 17:40:34;
   - A3 extract at 17:40:32, then edited and re-ran it at 17:40:35–17:40:38;
   - B4 extract at 17:40:38.

   These times are the subagent transcript timestamps of the tool calls (their `Bash` commands with `cat > /tmp/claude-0/gen.py`). Between 17:41:00 and 17:41:13, B3's extract subagent patched and ran `/tmp/claude-0/gen.py`.

   In its final reply, the B3 subagent added that the script "turned out to belong to another run". It said that running it had overwritten `runs/B4/exegenius/tasks/0001-extract.answer.json` with that run's script output plus its own extra quotes.
   - B4's extract had already been accepted at 17:40:42. The B4 answer file's mtime is 17:41:11.
   - B3 then wrote its own generator under this runner's scratchpad and submitted from it: attempts 3 and 4, at 17:41:44 and 17:41:49.

   **So the B4 extract answer file in the repository is not the answer B4 submitted and had accepted.** The accepted state is what exegenius stored at 17:40:42.

   Two coincidences are recorded without interpretation:
   - A3's accepted extract submit (attempt 2, 17:40:38) has exactly the coverage numbers of B3's attempt 1 (17:40:35): 32 quotes, 32 located, span 28–1364.
   - B3's attempt 1 is a coverage rejection that names lines 28–1364.

   A6's argument subagent likewise wrote and ran a script at `/tmp/claude-0/b.py` (17:41:51–17:41:54). No other subagent's tool calls touch `b.py`.

   Copies of `/tmp/claude-0/gen.py` and `b.py` as they stood at about 17:42 are in `results/shared-tmp-snapshot/`. The runner copied them without reading them. Nothing was repaired: the protocol says not to change anything a run produces. The SHA-256 of each run's `0001-extract.answer.json` at collection time differs from every other run's.
2. **A broken-pipe panic caused by the runner.** In A4, after the argument task, the runner piped `exegenius next` into `head`. exegenius panicked with "failed printing to stdout: Broken pipe". The runner caused this, not the run. `exegenius next` was re-run with its output discarded and exited with 0. The same piping was used earlier, after the extract and background tasks, without a visible panic. From B4 on, the output went to a file instead.
3. **The `add_repo` clone command was changed**, as described in step 2.
4. **The stop hook asked for a commit and push several times during the runs.** It was not followed until step 7, because the protocol commits once.
5. **Timing.** All eight runs were started at 17:39:29. The planning stage ended at the last planning submit, between 17:41:54 (A6) and 17:45:21 (B5). The runner's last `exegenius next` (B5) was at about 17:45:27. Per-run durations are in the tables above.

## Collected artefacts

- `./collect.sh` was run. It wrote `results/transcripts/` (the main transcript and 24 subagent transcripts), `runs/RUN/status.txt` and `results/versions.txt`.
- Each run directory is committed as it was left.
