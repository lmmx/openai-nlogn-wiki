# E4: the key-step instruction, paired on E1's extractions

Records of experiment E4, run in the development session of lmmx/exegenius (plan:
`calibration/plans/E4.md` at ec4a2b6; analysis: `docs/journal/2026-10-14-e4-key-step.md`).
This branch starts from `131026-exp-e1-config`, whose runs P1–P5 supplied the extractions and
backgrounds.

- `runs/B1`–`B5`: each of E1's P1–P5 projects reset to just before the argument task, the
  argument task rendered by the baseline binary (master af36d6d), answered by a fresh
  `general-purpose` subagent on Sonnet at high effort.
- `runs/V1`–`V5`: the same, with the argument task rendered by the variant binary
  (exegenius branch `131026-exp-key-step`, 0c29556), whose task file differs only by the
  key-step paragraph.
- `transcripts/`: every argument subagent's transcript with its `.meta.json` (the
  description names the run). Eight first attempts were killed by the account's rate limit
  (HTTP 429) and their tasks retried with the same prompt and parameters; both attempts are
  kept. B2 and B3 completed on their first attempt.

The sources (`paper.tex`) are omitted from the runs: they are byte-identical to
`template/sources/paper.tex`.
