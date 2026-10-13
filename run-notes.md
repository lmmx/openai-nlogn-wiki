# Run notes: exegenius 0.6.0, LaTeX source, explanation depth

Branch `full-v0.6-latex-depth`. Project directory `/mnt/openai-nlogn`, not `/workspace`. The CLI lives at `/workspace/bin/exegenius` and is not on PATH for subagents.

## Outcome

- `exegenius next` printed `done`. 234 tasks handed out, all accepted. The wiki is in `docs/` (32 pages, 7 parts, 3 glossary pages) with `zensical.toml`.
- Settings kept as configured: Haiku, `stop_early = false`, 3 audit rounds, `[simulation] rounds = 0` (no simulated readers), reader profile, source, word budgets, and page-extension policy unchanged. `exegenius.toml` and `sources/` were not edited.
- The reader correction was applied once: when the reader was first shown, `exegenius background --redo` was run with the calculus correction, and the redo was accepted.

## Problems and workarounds

1. **CLI not on PATH for subagents.** Several subagents reported `exegenius: command not found` and wrote their answer files without submitting. I submitted those myself with `/workspace/bin/exegenius submit` (0030), and later subagents were given the full path in their prompts.

2. **Rejections and fixes.**
   - 0021 (write): symbol `a` was used before it was explained. A fresh subagent fixed it and it was accepted.
   - 0200, 0205, 0214 (rewrites): the checker accepts only changes to notes on letters and citations, and each rewrite added a new display equation. Fresh subagents removed the new display and resubmitted, and all three were accepted. For 0205 the audit's index-clarity point was not kept as a display; it was left to prose.

3. **Duplicate audit launches overwrote accepted answer files.**
   - Audit 0052 (round 1) was launched twice. The second agent found the task already accepted and rewrote `0052-audit-multiplier-subroutine.answer.json` at 23:42:40.
   - Audit 0058 (round 1) was launched twice in the same way. Its second agent rewrote `0058-audit-fixed-tape-multiplication.answer.json` at 23:43:15.
   - Both tasks were accepted before the rewrite. The files on disk may no longer match what was accepted. The original contents were not kept, so I could not restore them. Treat audit round 1's 0052 and 0058 answers as unverified.

4. **Concurrency limit.** At one point 20 subagents was the cap and some audit launches were refused. They were relaunched once slots freed; no task was run twice except the two duplicates above.

5. **Round 3 audit gaps left on the pages.** The final audit round found 89 gaps across the 32 pages. No later audit checks rewrites for them, so they remain. Raise `rounds` to have them fixed. This is recorded in the `exegenius status` output.

## Observations for the comparison

- Support tasks finished in roughly 4 to 10 seconds with short label answers. That is their expected size; I checked a sample of answer files and they contain citation labels, not prose.
- Citation support at the end: 41 marks judged, 16 supported, 19 partial, 6 unsupported, 0 contradicted.
- Letters with two meanings: 52 confirmed, 14 left unjudged after the last overloads round.
- The status target reads `fixed-tape-multiplication`, the name the extract task chose. The `target` text in `exegenius.toml` is unchanged.

## Not done

- Nothing was pushed.
- No simulated-reader evaluation (`rounds = 0`).
