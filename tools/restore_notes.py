"""Restore the rewrite notes the last audit round queued for one page, which ending the run
cleared (task.rs: graph.rewrite.clear() and graph.note_depth.clear()).

usage: python3 -I restore_notes.py PROJECT_DIR PAGE

Rebuilds each note from exegenius/audit.json's last round, in the wording of exegenius-core
cc70355 (audit.rs: apply_gaps, apply_audit, term_action), and puts them in graph.json's
`rewrite` and `note_depth` for PAGE. A gap whose action is "candidate concept" is left out,
since restoring it would make `next` hand out an extend task first. A step's depth is taken
from the page's recorded added sentences as the run ended. Prints the notes it restored.
"""
import json
import pathlib
import re
import sys

STEP_NOTE = "The reader cannot follow this step:"
CITE_NOTE = "Cite or cut this step:"
OWED = (" It is inside reasoning added for an earlier step. If it is part of how this page's own "
        "step of the argument works (see \"This page in the argument\"), develop it here; if it "
        "concerns a result that step uses, say what the result states and cite it.")


def normalise(s):
    return re.sub(r"\s+", " ", s).strip()


def main():
    root, page = pathlib.Path(sys.argv[1]), sys.argv[2]
    ex = root / "exegenius"
    rounds = json.load(open(ex / "audit.json"))
    last = rounds[-1]
    entry = next(p for p in last["pages"] if p["page"] == page)
    graph = json.load(open(ex / "graph.json"))
    added = graph.get("added", {}).get(page, [])
    argument = json.load(open(ex / "argument.json"))
    presents = page in json.dumps(argument)  # the page is named by a step of the argument
    notes, deepest = [], 0
    for g in entry["gaps"]:
        action = g["action"]
        depth = next((s["depth"] for s in added if normalise(g["quote"]) in normalise(s["sentence"])), 0)
        if g["kind"] == "step":
            deepest = max(deepest, depth)
        if action.startswith("rewrite: cite or cut"):
            notes.append(f"{CITE_NOTE} \"{g['quote']}\" ({g['note']}). It is inside reasoning added for an "
                         f"earlier step, so do not explain it further: cite the source for it, or remove the claim.")
        elif action == "rewrite: explain the step":
            owed = OWED if depth > 0 and presents else ""
            notes.append(f"{STEP_NOTE} \"{g['quote']}\" ({g['note']}). Give the reasoning on this page. If the "
                         f"step rests on a result from prior work, say what the result states and why it applies "
                         f"here, and cite the source for its proof: a citation alone does not explain a step.{owed}")
        elif action == "rewrite: say what the symbol denotes":
            notes.append(f"Say what ${g['term']}$ denotes where it is first used (for a size or count, what it "
                         f"counts): \"{g['quote']}\" ({g['note']})")
        elif action == "rewrite: say what the symbol denotes at its first use":
            notes.append(f"Say what ${g['term']}$ denotes where it is first used: the page uses it before saying "
                         f"so in \"{g['quote']}\"")
        elif action == "candidate concept":
            print(f"left out (candidate concept): {g['term']}")
            continue
        else:
            sys.exit(f"unhandled action {action!r}")
    graph.setdefault("rewrite", {})[page] = notes
    graph.setdefault("note_depth", {})[page] = deepest
    json.dump(graph, open(ex / "graph.json", "w"), indent=1)
    print(f"restored {len(notes)} notes for {page} (note_depth {deepest}, page presents a step: {presents})")
    for n in notes:
        print(" -", n[:160])


main()
