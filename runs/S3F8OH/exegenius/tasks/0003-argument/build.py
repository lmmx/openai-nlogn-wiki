import json, re, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(BASE, '..', '..', '..'))
SRC = open(os.path.join(PROJ, 'sources', 'paper.tex')).read()


def ev(q):
    return {"source": "paper", "quote": q}


def infer(id, claim, quote, frm=(), page=None, deferred=False, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": list(frm)}
    if page:
        n["page"] = page
    if deferred:
        n["deferred"] = True
    if salient:
        n["salient"] = salient
    return n


def show(id, claim, method, mot_text, mot_src, children, frm=(), page=None, mot_quote=None, adds=None, salient=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": {"text": mot_text, "source": mot_src, "quote": ev(mot_quote) if mot_quote else None},
         "from": list(frm), "children": children}
    if page:
        n["page"] = page
    if adds:
        n["adds"] = [{"symbol": s, "name": nm, "meaning": me, "relation": rel} for (s, nm, me, rel) in adds]
    if salient:
        n["salient"] = salient
    return n


exec(open(os.path.join(BASE, 'tree.py')).read())

ans = {"root": ROOT}

# checks
errs = []
pos = 0
def walk(n, depth=0):
    global pos
    q = n.get("quote")
    if q:
        s = q["quote"]
        c = SRC.count(s)
        if c == 0:
            errs.append(f"MISSING {n['id']}: {s!r}")
        else:
            i = SRC.find(s, pos) if not n.get("deferred") else SRC.find(s)
            if not n.get("deferred"):
                if i < 0:
                    errs.append(f"ORDER {n['id']}: {s!r} (first at line {SRC[:SRC.find(s)].count(chr(10))+1}, pos line {SRC[:pos].count(chr(10))+1})")
                else:
                    pos = i
            if c > 1:
                errs.append(f"note multiple({c}) {n['id']}")
    m = n.get("motivation")
    if m and m.get("quote"):
        if m["quote"]["quote"] not in SRC:
            errs.append(f"MISSING MOT {n['id']}: {m['quote']['quote']!r}")
    for ch in n.get("children", []):
        walk(ch, depth + 1)
walk(ROOT)

def claims_below(n):
    out = []
    for ch in n.get("children", []):
        out.append(ch["claim"])
        out += claims_below(ch)
    return out

def maths(s):
    return re.findall(r"\$([^$]*)\$", s)

def walk2(n):
    for a in n.get("adds", []):
        sym = a["symbol"]
        ok = any(sym in m for c in claims_below(n) for m in maths(c))
        if not ok:
            errs.append(f"ADDS {n['id']} symbol {sym} not in descendant math")
    for ch in n.get("children", []):
        walk2(ch)
walk2(ROOT)

ids = []
pages = []
def walk3(n):
    ids.append(n["id"])
    if n.get("page"):
        pages.append(n["page"])
    for ch in n.get("children", []):
        walk3(ch)
walk3(ROOT)
if len(ids) != len(set(ids)):
    errs.append("dup ids")
if len(pages) != len(set(pages)):
    errs.append("dup pages " + str([p for p in pages if pages.count(p) > 1]))

print("\n".join(errs))
json.dump(ans, open(os.path.join(PROJ, 'exegenius', 'tasks', '0003-argument.answer.json'), 'w'), indent=1, ensure_ascii=False)
print("nodes", len(ids), "pages", len(pages))
