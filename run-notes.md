# Pilot run notes: exegenius 0.6.0, LaTeX source, pages = 5

## Outcome

- `exegenius next` printed `done`. 37 tasks were handed out and all 37 were accepted.
- Output: 5 pages in `docs/`, 4 parts, `zensical.toml` at the repo root.
- Full status is in `run-status.txt`.

## What went wrong or needed a workaround

1. **Working directory and binary.** The project is `/mnt/openai-nlogn`, not `/workspace`. `exegenius` is not on PATH; the binary is `/workspace/bin/exegenius`. I ran it with `PATH=/workspace/bin:$PATH` from the project directory.
2. **Calculus correction, first attempts refused.** `exegenius background --redo "...calculus..."` was refused twice with "can be redone only right after `next` shows it, before any later task". I did not retry further. The original background task 0002 was answered and accepted with the pre-correction profile.
3. **Calculus correction, applied later.** After the reader profile was printed by `next`, the same redo command succeeded once. It produced a new background task, 0003, which was answered and accepted. The reader profile printed afterwards includes limits, convergence of sequences and series, and basic integrals. Task 0002 stays in the record as the superseded answer.
4. **Stray agent.** I launched one placeholder subagent ("reply noop") by mistake. It did nothing to the project.
5. **No subagent rejections.** Every subagent reported "accepted". No submit was rejected, so no answer had to be reworked.

## Quality warnings from `exegenius status`

- **Audit rounds stopped early.** The tool stopped after audit round 2, not round 3 as `rounds = 3` in `exegenius.toml` would allow. Its reason: step and symbol gaps on the pages audited in both rounds fell from 33 to 17, which it judged not converging. 29 gaps from round 2 remain on the pages. Status says raising `rounds` would have them fixed.
- **Citation support.** Of 5 citation marks, 0 are supported, 4 partial, 1 unsupported. A second judge agreed on 1 of 1 marks checked.
- **Simulated readers did not run.** `[simulation] rounds = 0` in `exegenius.toml` is unchanged, so no goal-question reader test was run. The wiki has not been checked by a simulated reader.
- **Scope of the pilot.** Status shows `pilot: subset-network`, so this pilot explains only the subset-intersection network part of the target, not the whole main theorem.

## Files

- Untouched: `sources/`, `exegenius.toml`, and anything else not under `exegenius/`, `docs/`, `zensical.toml`, or the two run files at the root.
- Added: `exegenius/` (tasks, answers, graph, state), `docs/`, `zensical.toml`, `run-status.txt`, `run-notes.md`.
