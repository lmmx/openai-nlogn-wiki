import json, re, sys
SRC = open('/home/user/openai-nlogn-wiki/runs/Q2/sources/paper.tex').read()

def exact(q):
    toks = q.split()
    pat = r'\s+'.join(re.escape(t) for t in toks)
    m = list(re.finditer(pat, SRC))
    if not m:
        sys.exit('NOT FOUND: ' + q)
    return m[0].group(0), m[0].start()

def ev(q):
    return {"source": "paper", "quote": exact(q)[0]}

def B(sym, name, meaning, rel="direct"):
    return {"symbol": sym, "name": name, "meaning": meaning, "relation": rel}

def infer(id, claim, quote, page=None, frm=(), salient=None, deferred=None, adds=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": list(frm)}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if deferred: n["deferred"] = True
    if adds: n["adds"] = adds
    return n

def show(id, claim, method, mot, children, page=None, frm=(), salient=None, adds=None):
    text, src, q = mot
    m = {"text": text, "source": src}
    if q: m["quote"] = ev(q)
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": m,
         "children": children, "from": list(frm)}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n

exec(open('/home/user/openai-nlogn-wiki/runs/Q2/exegenius/tasks/0003-argument/tree.py').read())

# order check
pos = []
def walk(n):
    if n["intention"] == "infer":
        _, p = exact(n["quote"]["quote"])
        pos.append((n["id"], p, n.get("deferred", False)))
    for c in n.get("children", []):
        walk(c)
walk(root)
last = -1
for id, p, d in pos:
    if d: continue
    print(id, p, "" if p > last else "  <-- OUT OF ORDER")
    last = max(last, p)
json.dump({"root": root}, open('/home/user/openai-nlogn-wiki/runs/Q2/exegenius/tasks/0003-argument.answer.json', 'w'), indent=1, ensure_ascii=False)
