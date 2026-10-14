import json, re
from lib import *
from asm2 import ROOT

root = ROOT()
assign_ids(root)

# validation
errs = []
pidx = {p: i for i, p in enumerate(PAGES)}
used_pages = {}
def eff_page(n, anc):
    return n.kw.get("page") or anc
def walk2(n, anc, path):
    ep = n.kw.get("page") or anc
    yield n, ep
    for c in n.children:
        yield from walk2(c, ep, path)
froms = set()
pos = -1
for n, ep in walk2(root, None, None):
    pg = n.kw.get("page")
    if pg:
        if pg in used_pages: errs.append("page twice " + pg)
        used_pages[pg] = n.id
        if pg not in pidx: errs.append("bad page " + pg)
    for f in n.kw.get("frm") or []:
        froms.add(f)
        if f in KNOWN: continue
        if f not in pidx: errs.append("bad from %s at %s" % (f, n.id)); continue
        if pidx[f] >= pidx[ep]: errs.append("from %s not before page %s at %s" % (f, ep, n.id))
    if n.kind == "infer" and not n.kw.get("deferred"):
        p = SRC.find(n.kw["quote"])
        if p <= pos: errs.append("out of order %s (%d <= %d) %r" % (n.id, p, pos, n.kw["quote"][:50]))
        pos = max(pos, p) if p > pos else pos
        # also check line
for p in PAGES:
    if p not in used_pages and p not in froms:
        errs.append("page unused: " + p)
if root.kw.get("page") != "main-theorem": errs.append("root page")
# adds
def math(s):
    return " ".join(re.findall(r"\$(.*?)\$", s))
for n in walk(root):
    for (sym, name, meaning, rel) in n.kw.get("adds") or []:
        found = False
        for c in n.children:
            for d in walk(c):
                if sym in math(d.claim): found = True; break
            if found: break
        if not found: errs.append("add %s at %s not in descendants" % (sym, n.id))
        if len(name.split()) > 4: errs.append("name too long " + name)
print("\n".join(errs) if errs else "VALID")
out = {"root": root.to_dict()}
json.dump(out, open("../0003-argument.answer.json", "w"), ensure_ascii=False, indent=1)
print(len(list(walk(root))), "nodes")
