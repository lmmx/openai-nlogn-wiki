# Full run of exegenius 0.6.0 (LaTeX source)

Branch: `full-v0.6-latex`. Config as given: `rounds = 3`, `stop_early = false`, `[simulation] rounds = 0`. Source `sources/paper.tex`, `exegenius.toml`, and `sources/` were not edited.

Result: `exegenius next` printed `done`; 180 tasks handed out, 180 accepted, 0 pending. Wiki built to `docs/` with `zensical.toml`. Final status is in `run-status.txt`.

## What happened

- **Extraction** (`0001-extract`) accepted on the first submit.
- **Reader profile**: first printed after `0002-background`. Applied the calculus correction once with `exegenius background --redo`, as asked. The re-printed profile included the calculus. I did not wait for a reply.
- **Pages** (`0005`–`0026`, 22 pages): all accepted. Page count ended at 23 pages in 5 parts, 3 in the glossary.
- **Audit rounds 1–3** (`0027`–`0139`): all accepted. Each audit ran in its own fresh `exegenius-task` subagent.
- **Outline / overloads / support** (`0140`–`0158`): accepted. Extend `0049`, argument `0050`, and extend `0094` were also accepted.
- **Rewrites** (`0051`–`0070`, `0095`–`0116`, `0159`–`0169`, `0175`–`0180`): all accepted. Rewrite waves for pages readers got stuck on; the queue ended at 0.
- **Second support wave** (`0171`–`0174`) and overloads (`0170`): accepted.

No submit was rejected in a way that needed a workaround. I did not read the submit logs, so I'm relying on the accepted notifications.

## Things to look at

- **Audit round 3 gaps left on pages.** `exegenius status` reports 58 gaps across 23 pages after round 3, and says they stay because no audit checks rewrites made after round 3. Raising `rounds` would fix them; I left the config alone as you asked.
- **Overloads not fully judged.** After the last overloads round, status says 10 letters with two meanings are still unjudged (41 confirmed). I did not re-run it.
- **Citation support** (30 marks judged): 13 supported, 14 partial, 2 unsupported, 1 contradicted. Only one of those marks had a second judge, and it agreed. The contradicted and unsupported marks are the ones to check first.
- **Reasoning steps added by rewrites**: 54 steps were added for earlier steps during rewriting and sent back to be cited or cut.
- **Support tasks were fast.** Several support subagents (0142–0158, 0171–0174) finished in about 4–8 seconds with 2–3 tool calls. They were accepted, but I did not inspect those answers.
- **No simulated readers.** `[simulation] rounds = 0`, so there is no `exegenius/report.md` and no reader-based evaluation.

## Commands used

`exegenius` is not on the default PATH here; I ran it as `/workspace/bin/exegenius` (PATH prefixed in each subagent). The session's primary directory was `/workspace`; the exegenius project is `/mnt/openai-nlogn`, which is where all commands ran.
