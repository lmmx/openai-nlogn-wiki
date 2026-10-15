"""Local mirror of the argument checks (quotes, order, pages, from, adds)."""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
ans = json.load(open(os.path.join(HERE, "..", "0003-argument.answer.json")))
graph = json.load(open(os.path.join(PROJ, "exegenius", "graph.json")))
src = open(os.path.join(PROJ, "sources", "paper.tex")).read()

ORDER = """convolution-multiplication negacyclic-ring hvdh-multiplier multitape-streams controlled-shifts
bank-exchange-network linear-algebra-spaces frames-on-arrays subspace-labels recursive-power-saving
bit-shear-interface lower-triangular-factorization matrix-shear-cost power-width-interchange
chunk-interchange phase-frames packed-selected-bit-addition fixed-point-precision guard-bits
signed-kronecker-packing discrete-fourier-transform radix-two-fft synthetic-transforms
simultaneous-butterfly-layer synthetic-transform-layout synthetic-convolution coefficient-twist
gaussian-resampling bluestein-chirp permutation-cancellation tensor-resampling crt-cyclic-convolution
parameter-choice multiplication-algorithm exact-recovery time-bound-accounting
multiplication-below-nlogn""".split()
pos = {p: i for i, p in enumerate(ORDER)}
concepts = {c["id"]: c for c in graph["concepts"]}


def norm(s):
    tr = {"‘": "'", "’": "'", "‛": "'", "′": "'",
          "“": '"', "”": '"', "‟": '"', "″": '"', "−": "-"}
    out = []
    for ch in s:
        if ch == "­":
            continue
        if "‐" <= ch <= "―":
            ch = "-"
        out.append(tr.get(ch, ch))
    return " ".join("".join(out).split())


NS = norm(src)
# line lookup
line_starts = []


def line_of(q):
    # approximate: find in raw by first 30 chars of normalized words
    i = NS.find(norm(q))
    return i


def tokens(latex):
    out = []
    i = 0
    while i < len(latex):
        c = latex[i]
        if c == "\\":
            j = i + 1
            if j < len(latex) and latex[j].isalpha():
                while j < len(latex) and latex[j].isalpha():
                    j += 1
                tok = latex[i:j]
            else:
                tok = latex[i:j + 1]
                j = j + 1
        else:
            tok = c
            j = i + 1
        if not (c.isspace() or tok in ("\\,", "\\;", "\\:", "\\!", "\\ ", "~") or tok in ("{", "}")):
            out.append(tok)
        i = j
    return out


def maths(text):
    return re.findall(r"\$([^$]+)\$", text)


errors, warns = [], []
ids = set()
pages = {}


def walk(n, path):
    yield path, n
    for c in n.get("children", []):
        yield from walk(c, path + [n])


nodes = list(walk(ans["root"], []))
for path, n in nodes:
    w = f"step {n['id']}"
    if n["id"] in ids:
        errors.append(f"{w} twice")
    ids.add(n["id"])
    if n["intention"] == "show":
        if not n.get("children"):
            errors.append(f"{w} show no children")
        if not n.get("method"):
            errors.append(f"{w} no method")
        m = n.get("motivation")
        if not m:
            errors.append(f"{w} no motivation")
        else:
            if m.get("quote"):
                if norm(m["quote"]["quote"]) not in NS:
                    errors.append(f"{w} motivation quote missing: {m['quote']['quote']}")
            elif m["source"] == "explicit":
                errors.append(f"{w} explicit w/o quote")
    else:
        if n.get("children"):
            errors.append(f"{w} infer with children")
        q = n.get("quote")
        if not q or norm(q["quote"]) not in NS:
            errors.append(f"{w} quote missing: {q and q['quote']}")
        elif NS.count(norm(q["quote"])) > 1:
            warns.append(f"{w} quote occurs {NS.count(norm(q['quote']))} times")
    pg = n.get("page")
    if pg:
        if pg not in pos:
            errors.append(f"{w} page {pg} unknown")
        elif pg in pages:
            errors.append(f"{pg} presents {pages[pg]} and {n['id']}")
        else:
            pages[pg] = n["id"]
    page = next((a.get("page") for a in [n] + path[::-1] if a.get("page")), None)
    for f in n.get("from", []):
        c = concepts.get(f)
        if c is None:
            errors.append(f"{w} from {f} not a concept")
        elif c["known"]:
            pass
        elif f not in pos:
            errors.append(f"{w} from {f} not page")
        elif pos[f] >= pos[page]:
            errors.append(f"{w} from {f} not before {page}")
    below = [m for _, d in walk(n, []) for m in maths(d["claim"])]
    for b in n.get("adds", []):
        t = tokens(b["symbol"])
        ok = any(any(tokens(m)[k:k + len(t)] == t for k in range(len(tokens(m)))) for m in below)
        if not ok:
            errors.append(f"{w} adds {b['symbol']} not in claims below")
        if not (1 <= len(b["name"].split()) <= 4):
            errors.append(f"{w} adds name {b['name']}")
    if pg and pg in pos:
        for a in path:
            if a.get("page") in pos and pos[a["page"]] < pos[pg]:
                warns.append(f"{w} on {pg} after ancestor page {a['page']}")

last = None
for _, n in nodes:
    if n["intention"] != "infer" or n.get("deferred"):
        continue
    at = NS.find(norm(n["quote"]["quote"]))
    if at < 0:
        continue
    if last and at < last[0]:
        errors.append(f"order: {n['id']} before {last[1]}")
    last = (at, n["id"])

used = set()
for _, n in nodes:
    if n.get("page"):
        used.add(n["page"])
    used.update(n.get("from", []))
unused = [p for p in ORDER if p not in used]
if unused:
    errors.append(f"unused pages: {unused}")

# rough check of claims' $ balance
for _, n in nodes:
    for fld in ("claim",):
        if n[fld].count("$") % 2:
            errors.append(f"{n['id']} odd $ in claim")

print("nodes", len(nodes), "infers", sum(1 for _, n in nodes if n["intention"] == "infer"))
print("ERRORS:\n" + "\n".join(errors) if errors else "no errors")
print("WARNINGS:\n" + "\n".join(warns) if warns else "no warnings")
