# Results: Experiment S1, attempt 2 (screening other models for planning)

Status: **all six runs reached the end of planning** (the first `exegenius next` that hands out
write tasks). No write task was started. Steps 1–7 done; step 8 follows the push.
Attempt 1's report is kept as `results-attempt-1.md`.

## Versions

- Branch `131026-exp-s1-models` at `3c70129` when the runner started.
- Claude Code: `2.1.296 (Claude Code)`.
- exegenius: `exegenius 0.6.0`, built with `cargo build --release` from lmmx/exegenius at
  `cc7035544221dc399ee5ed99f02fd682bb43f9ac` (`git rev-parse --short HEAD` printed `cc70355`),
  copied to `/usr/local/bin/exegenius`. Build time: 1m 42s.
- `results/versions.txt` (written by `collect.sh`) has the same three values.

## Step 1: subagent types and parameters

- The session's Agent tool listed the subagent type `exegenius-planner`.
- The Agent tool schema has `model` (enum `sonnet`, `opus`, `haiku`, `fable`) and `effort`
  (enum `low`, `medium`, `high`, `xhigh`, `max`).
- Result: passed.

## Step 2: attach and build exegenius

1. `add_repo` with `owner: "lmmx"`, `repo: "exegenius"`, `access: "push"`: returned
   `status: "appended"`, with instructions to clone with `--depth 1`.
2. Clone: `git clone --depth 500 https://github.com/lmmx/exegenius /home/user/exegenius`. The
   runner used depth 500, not the instructed depth 1, to meet the protocol's requirement to
   include `cc70355`. `git cat-file -t cc70355` printed `commit`.
3. `git checkout cc70355`. `git rev-parse --short HEAD` printed `cc70355`. The commit's
   subject is "Journal: the audit rounds before and after the fixes, and subagent effort in
   the earlier runs", dated 2026-10-13 20:03:02 +0000.
4. `register_repo_root` for lmmx/exegenius at `/home/user/exegenius`: returned
   `status: "context_reload_requested"`. lmmx/exegenius has no `CLAUDE.md` or
   `.claude/CLAUDE.md`, and no context reminder from it appeared.
5. `cargo build --release`, then copied the binary to `/usr/local/bin`.

**Deviation:** the runner issued 2.3 (`git checkout`) and 2.4 (`register_repo_root`) as two
tool calls in the same assistant message, so they may have run concurrently. The protocol
requires each sub-step to finish before the next starts. 2.1, 2.2 and 2.5 each ran on their
own.

Nothing was pushed to lmmx/exegenius.

## Step 3: setup

`./setup-run.sh RUN arm.toml` for O1, O2, Q1, Q2, K1 and K2 each printed `runs/RUN ready`.

## Step 4: runs

All Agent calls used `subagent_type: "exegenius-planner"` (the type `exegenius next` named
for every planning task). Each prompt was exactly the one `exegenius next` printed, and each
description was `RUN TASKID`. Each call passed only `model` and `effort`:

| Arm | `model` passed | `effort` passed | Transcript `.meta.json` | Model on assistant messages in the transcripts |
|---|---|---|---|---|
| O1, O2 | `opus` | `medium` | `model: opus`, `effort: medium` | `claude-opus-5-5` |
| Q1, Q2 | `opus` | `high` | `model: opus`, `effort: high` | `claude-opus-5-5` |
| K1, K2 | `haiku` | `high` | `model: haiku`, `effort: high` | `claude-haiku-5-5` (K2 0003-argument also has one `<synthetic>` message, the rate-limit error) |

Every subagent transcript's metadata records `agentType: exegenius-planner`. Each subagent
transcript's `effort` field matches the effort passed.

Each run printed the reader profile once, after background. The runner then ran
`exegenius next` again, as the protocol says. The first `exegenius next` call that started
all six runs was at 22:00:17 UTC on 2026-10-13.

### Per run: tasks and submits (from `runs/RUN/exegenius/log.jsonl`, UTC)

**O1** (opus, medium)
- 0001-extract: issued 22:00:17; submit 1 accepted 22:02:45.
- 0002-background: issued 22:02:49. Submit 1 rejected 22:04:22 ("Dot product, orthogonality
  and orthonormal bases" is the existing concept `bilinear-form`). Submit 2 rejected 22:04:26
  ("Dot product and orthonormal bases" is the existing concept `bilinear-form`). Submit 3
  accepted 22:04:28.
- 0003-argument: issued 22:04:36; submit 1 accepted 22:08:32.
- 43 write tasks issued 22:08:40. Stopped.
- `status.txt`: 87 concepts (44 known to the reader); 43 pages planned.

**O2** (opus, medium)
- 0001-extract: issued 22:00:17; submit 1 accepted 22:02:52.
- 0002-background: issued 22:02:59. Submit 1 rejected 22:04:36 ("Orthogonality and dot
  product" is the existing concept `linear-algebra-bilinear`). Submit 2 accepted 22:04:38.
- 0003-argument: issued 22:04:45; submit 1 accepted 22:10:17 with 4 warnings (steps
  presented on a page that comes after the page of the step they serve).
- 37 write tasks issued 22:10:22. Stopped.
- `status.txt`: 80 concepts (43 known); 37 pages planned.

**Q1** (opus, high)
- 0001-extract: issued 22:00:17; submit 1 accepted 22:04:30.
- 0002-background: issued 22:04:36. Submit 1 rejected 22:06:27 ("Grade-school binary
  arithmetic" is the existing concept `radix-reduction`; "Bases and orthonormal bases" is the
  existing concept `bilinear-forms`). Submit 2 accepted 22:06:31.
- 0003-argument: issued 22:06:41; submit 1 accepted 22:14:08.
- 53 write tasks issued 22:14:13. Stopped.
- `status.txt`: 92 concepts (39 known); 53 pages planned.

**Q2** (opus, high)
- 0001-extract: issued 22:00:17; submit 1 accepted 22:05:02.
- 0002-background: issued 22:05:06. Submit 1 rejected 22:07:02 ("Boolean and arithmetic
  circuits" is the existing concept `linear-network`). Submit 2 accepted 22:07:05.
- 0003-argument: issued 22:07:10. Submit 1 rejected 22:13:00 (step `S9.1`: `crt-address-map`
  in `from` does not come before the step's page `exact-recovery` in the reading order).
  Submit 2 accepted 22:13:03.
- 51 write tasks issued 22:13:07. Stopped.
- `status.txt`: 94 concepts (43 known); 51 pages planned.

**K1** (haiku, high)
- 0001-extract: issued 22:00:17; submit 1 accepted 22:03:23.
- 0002-background: issued 22:03:28. Submit 1 rejected 22:06:31 ("Omega, Theta and little-o
  notation" is the existing concept `big-o-notation`). Submit 2 accepted 22:06:35.
- 0003-argument: issued 22:06:44; submit 1 accepted 22:14:50 with 4 warnings (same kind as
  O2).
- 36 write tasks issued 22:14:57. Stopped.
- `status.txt`: 66 concepts (30 known); 36 pages planned. Target
  `sub-linearithmic-integer-multiplication` (the other five runs' target is `main-theorem`).

**K2** (haiku, high)
- 0001-extract: issued 22:00:17; submit 1 accepted 22:06:27.
- 0002-background: issued 22:06:32; submit 1 accepted 22:08:59.
- 0003-argument: issued 22:09:05; submit 1 accepted 22:21:16 with 3 warnings (same kind as
  O2).
- 61 write tasks issued 2026-10-14 00:58:18 (see "Unexpected" below). Stopped.
- `status.txt`: 87 concepts (26 known); 61 pages planned.

The full `status.txt` for each run is in `runs/RUN/status.txt`. The full submit records,
including coverage and warning texts, are in `runs/RUN/exegenius/log.jsonl`.

### Per subagent (from the task notifications)

| Run | Task | Duration (ms) | Tokens | Tool uses | Reply |
|---|---|---|---|---|---|
| O1 | 0001-extract | 135138 | 154340 | 5 | accepted |
| O1 | 0002-background | 97307 | 41347 | 12 | accepted |
| O1 | 0003-argument | 231895 | 161750 | 17 | accepted |
| O2 | 0001-extract | 142180 | 90364 | 19 | accepted |
| O2 | 0002-background | 98065 | 39702 | 11 | accepted |
| O2 | 0003-argument | 330696 | 124391 | 20 | accepted |
| Q1 | 0001-extract | 239537 | 162914 | 18 | accepted |
| Q1 | 0002-background | 111377 | 155711 | 13 | accepted |
| Q1 | 0003-argument | 439597 | 195650 | 19 | accepted |
| Q2 | 0001-extract | 272301 | 172588 | 11 | accepted |
| Q2 | 0002-background | 115649 | 72382 | 12 | accepted |
| Q2 | 0003-argument | 349823 | 171119 | 22 | accepted |
| K1 | 0001-extract | 173939 | 88043 | 14 | accepted |
| K1 | 0002-background | 184701 | 91286 | 17 | accepted |
| K1 | 0003-argument | 484089 | 182226 | 31 | accepted |
| K2 | 0001-extract | 357898 | 217985 | 25 | accepted |
| K2 | 0002-background | 145898 | 172210 | 12 | accepted |
| K2 | 0003-argument | — | — | — | status `failed` (see below); no usage block in the notification |

The K2 0003-argument transcript runs from 22:09:11 to 22:21:49 UTC.

### Restarts

None. No subagent left its task pending.

### Cross-run and shared-place access

The runner scanned every subagent tool call in the transcripts. None referenced another
run's directory, `/tmp`, or any path under `/home/user` outside its own run, and none used
`kill`, `pkill` or `killall`.

## Unexpected events and deviations

- **K2 0003-argument subagent failure.** The task notification has status `failed`: "Agent
  terminated early due to an API error: You've hit your session limit · resets 12:50am (UTC)
  (error type rate_limit, HTTP 429, …, model sent to the API: claude-haiku-5-5)". Before that,
  the subagent's submit 1 was accepted at 22:21:16 with 3 warnings. After acceptance, it said
  it would restructure to remove the warnings and edited its scratch file
  `exegenius/tasks/0003-argument/build.py` at 22:21:48. It did not rewrite the answer file
  (last modified 22:21:04) and did not submit again. The accepted answer stands, and the task
  was not pending, so there was no restart.
- **Gap and worker restart.** After that notification, this session's worker process was
  restarted, and the runner resumed at 00:58 UTC on 2026-10-14. That is why K2's write tasks
  were issued about 2.5 hours after its argument was accepted. After the restart, the user
  sent "Try again". The runner checked K2's state, found nothing pending, and continued with
  the protocol. The main-session transcript after the restart is in
  `results/transcripts/-home-user/`, because the project directory changed. The rest is in
  `results/transcripts/-home-user-openai-nlogn-wiki/`.
- **Runner-side broken pipe.** The runner's own `exegenius next | head -3` in K2 made
  exegenius panic with "failed printing to stdout: Broken pipe". This was the call that
  issued K2's 61 write tasks.
- **Step 2 deviations:** 2.3 and 2.4 were issued in the same message (see step 2), and the
  clone used `--depth 500` rather than the `--depth 1` that `add_repo` suggested.
- **The runner's own reads:** the runner read none of the sources, task files or answer
  files. It looked at `log.jsonl`, `status.txt` and the transcripts for this report, and it
  checked the modification time of K2's argument answer file without reading its contents.

## Step 5: collect

`./collect.sh` ran and copied 13M of transcripts into `results/transcripts`. It also wrote
`runs/*/status.txt` and `results/versions.txt`.
