# S4, S5, E8, E8b and FB1: argument runs on E6's extractions

Records of experiments S4, S5, E8, E8b and the FB1 pilot. They were run in the development session of lmmx/exegenius. Plans, criteria and ledgers are in `calibration/plans/S4.md`, `S5.md`, `E8.md`, `E8b.md` and `FB1.md`, each committed before its runs. The analysis is in `docs/journal/2026-10-14-s4-s5-e8.md` and the plans' result sections.

This branch starts from `141026-exp-s3-opus-floor`, so it also holds the comparisons:
- E7FkW (Sonnet `high`, E7 instructions);
- S3F8OX.

**The runs** are copies of E6's projects (background accepted). Each prompt went word for word, as `exegenius next` printed it, to a fresh `general-purpose` subagent:

| Run dir | Experiment | Instructions (task rendered by) | Model, effort |
|---|---|---|---|
| `runs/S4F8OM` | S4 | E7, `141026-exp-key-step-identity` (91c4fed) | Opus, `max` |
| `runs/S5F8OX` | S5, a repeat of S3F8OX | E7 (91c4fed) | Opus, `xhigh` |
| `runs/E8F1X`, `E8F4X`, `E8F8X` | E8 | E7 + the variant sentence, `141026-exp-variants-chains` (4f5ee26) | Sonnet, `high` |
| `runs/E8F2X`, `E8F3X`, `E8F5X`, `E8F6X`, `E8F7X`, `E8F4X2` | E8b (`E8F4X2` repeats F4) | as E8 (4f5ee26) | Sonnet, `high` |
| `runs/FB1F8` | FB1 pilot | E7 (91c4fed) | Fable, `high` |

- Every task file was checked by diff against its comparison's, apart from the project path and the instruction sentence.
- E8F1X and FB1F8 were accepted at their second submit; the first was rejected by `submit`'s checks (the logs record why). The other ten were accepted at their first. E8F6X's log also records a third `submit` after acceptance, refused as not pending. None stopped on `max_tokens`.
- Helper files are kept. `__pycache__` and build output are not, and `sources/` is ignored as elsewhere.

**Transcripts:** `results/transcripts/s4-e8-fb1/subagents/` holds the twelve argument subagents' transcripts and `.meta.json` files. Their descriptions are `S4F8OM 0003-argument`, `E8bF2X 0003-argument` and so on. There were no restarts.
