# T1 results (facts; analysis in lmmx/exegenius docs/journal/2026-10-13-t1-depth-rule.md)

- **Design:** lmmx/exegenius `calibration/plans/T1.md` (bd104f5).
- **Execution:** T1 ran in the development session, not in a runner. Each copy needed a single rewrite, and a runner would have needed an allow rule the author had authorised only for S1.
- **Binary:** exegenius `cc70355` (`exegenius 0.6.0`), on PATH as `exegenius`.
- **The project:** this branch's root, the planner-and-handoff run as it ended (72f1de8).

## Setup

- **The copies:** `./setup-run.sh R0`–`R3` copy the project with `rounds = 4`.
- **Raising `rounds` alone does nothing.** `exegenius next` printed `done`. When the last round ends, `submit` clears the rewrite queue (`graph.rewrite`, `note_depth`), so the dropped notes cannot be recovered that way. The status hint that said otherwise is corrected in lmmx/exegenius af36d6d.
- **Restoring the notes.** In R1–R3, `tools/restore_notes.py` rebuilt the page `subset-intersection-construction`'s round-3 notes from `exegenius/audit.json`, in `cc70355`'s wording, into `graph.json`. Its output is in each run's `restore-notes.txt`:
  - eight notes: six "Cite or cut this step", one "The reader cannot follow this step", and one symbol note;
  - `note_depth` 2;
  - the "candidate concept" gap was left out, since restoring it would make `next` issue an extend task first.
- **The rewrite:** `exegenius next` then issued `0213-write-subset-intersection-construction` in each of R1–R3. Each was given, with the printed prompt word for word, to a fresh `general-purpose` subagent with `model: "haiku"`, `effort: "medium"`. Every subagent was accepted (`results/writers-effort.tsv`: `claude-haiku-5-5`, effort medium every turn; transcripts in `results/transcripts/`).
- **The rebuild:** `exegenius next` again in R1–R3 printed `done` and rebuilt `docs/`.
- **The control:** R0, with no notes restored, was rebuilt the same way, so that the control is built by the same binary.

## Correctness of the original page

`results/correctness-of-original-page.json`, from an Opus judge:
- **Claims:** 30 checked; 21 correct, 9 correct but incomplete, 0 wrong.
- **The derivation:** rank as dimension change → $s=Wm-N+2L$ → $L/N=100/539<1/2$ holds, with 6 gaps in unstated premises.

## The rewritten page, mechanically

| Run | Words (original 524) | Marked sentences kept verbatim | "100/539" | "2L" | `<cite>` marks (original 2) |
|---|---|---|---|---|---|
| R1 | 654 | 0 of 6 | yes | 4 | 5 |
| R2 | 646 | 0 of 6 | yes | 4 | 4 |
| R3 | 643 | 0 of 6 | yes | 6 | 5 |
