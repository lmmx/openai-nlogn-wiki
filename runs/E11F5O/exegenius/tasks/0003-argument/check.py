import json, re, sys

ROOT = sys.argv[1]
src = open(ROOT + "/sources/paper.tex").read()
norm = lambda s: re.sub(r"\s+", " ", s).strip()
nsrc = norm(src)
ans = json.load(open(ROOT + "/exegenius/tasks/0003-argument.answer.json"))
task = open(ROOT + "/exegenius/tasks/0003-argument.md").read()
pages = re.findall(r"^- `([a-z0-9-]+)`: ", task.split("## Pages, in reading order")[1].split("## Concepts the reader knows")[0], re.M)
known = re.findall(r"^- `([a-z0-9-]+)`: ", task.split("## Concepts the reader knows")[1].split("## Sources")[0], re.M)
pidx = {p: i for i, p in enumerate(pages)}
errs = []
ids = set()
page_steps = {}
last = -1
fromused = set()


def walk(n, page, depth=0, anc_adds=()):
    global last
    if n["id"] in ids:
        errs.append("dup id " + n["id"])
    ids.add(n["id"])
    pg = n.get("page") or page
    if n.get("page"):
        page_steps.setdefault(n["page"], []).append(n["id"])
    for f in n.get("from", []):
        fromused.add(f)
        if f in known:
            continue
        if f not in pidx:
            errs.append(f"{n['id']}: unknown from {f}")
        elif pidx[f] >= pidx[pg]:
            errs.append(f"{n['id']}: from {f} not before page {pg}")
    m = n.get("motivation")
    if m and m.get("quote"):
        q = norm(m["quote"]["quote"])
        if q not in nsrc:
            errs.append(f"{n['id']}: motivation quote not found: {q[:80]}")
    if n["intention"] == "infer":
        q = norm(n["quote"]["quote"])
        pos = nsrc.find(q)
        cnt = nsrc.count(q)
        if pos < 0:
            errs.append(f"{n['id']}: quote not found: {q[:80]}")
        else:
            if cnt > 1:
                print(f"  note {n['id']} quote occurs {cnt} times")
            if not n.get("deferred"):
                # earliest occurrence >= last
                p2 = nsrc.find(q, last if last >= 0 else 0)
                if pos < last:
                    errs.append(f"{n['id']}: order (first occurrence {pos} < last {last}); later occ {p2}")
                last = max(last, pos)
    for c in n.get("children", []):
        walk(c, pg, depth + 1)


walk(ans["root"], "main-theorem")
for p, s in page_steps.items():
    if len(s) > 1:
        errs.append(f"page {p} has steps {s}")
for p in pages:
    if p not in page_steps and p not in fromused:
        errs.append(f"page {p} neither presents a step nor in from")


# adds check
def claims_below(n):
    out = []
    for c in n.get("children", []):
        out.append(c["claim"])
        out += claims_below(c)
    return out


def maths(s):
    return re.findall(r"\$([^$]*)\$", s)


def walk2(n):
    if n.get("adds"):
        mm = " ".join(m for c in claims_below(n) for m in maths(c))
        for b in n["adds"]:
            sym = b["symbol"]
            tok = lambda x: re.findall(r"\\[A-Za-z]+|\\.|[A-Za-z]|\d|\S", x)
            st = tok(sym); mt = tok(mm)
            found = any(mt[i:i+len(st)] == st for i in range(len(mt)))
            if not found:
                errs.append(f"{n['id']}: add {sym} not in math below")
    for c in n.get("children", []):
        walk2(c)


walk2(ans["root"])
print("\n".join(errs) if errs else "OK")
print("steps:", len(ids), "pages with steps:", len(page_steps))
