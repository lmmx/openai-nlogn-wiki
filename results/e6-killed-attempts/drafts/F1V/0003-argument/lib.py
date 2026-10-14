import re, json
TEXT = open('sources/paper.tex', encoding='utf-8').read()
LINES = TEXT.split('\n')
OFFS = [0]
for l in LINES:
    OFFS.append(OFFS[-1] + len(l) + 1)

POS = {}   # id(quote dict) -> position

def Q(line, a, b=None):
    start = OFFS[max(line - 3, 0)]
    i = TEXT.find(a, start)
    assert i >= 0, ("start not found", line, a)
    ln = TEXT.count('\n', 0, i) + 1
    assert abs(ln - line) <= 3, ("start far from hint", line, ln, a)
    if b is None:
        j = i + len(a)
    else:
        k = TEXT.find(b, i)
        assert k >= 0, ("end not found", line, b)
        j = k + len(b)
    s = TEXT[i:j]
    assert TEXT.count(s) == 1, ("not unique", line, s[:60], TEXT.count(s))
    d = {"source": "paper", "quote": s}
    POS[id(d)] = i
    return d

def M(text, source, quote=None):
    return {"text": text, "source": source, "quote": quote}

def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

def infer(claim, quote, frm=(), page=None, salient=None, deferred=False, adds=None):
    d = {"intention": "infer", "claim": claim, "quote": quote, "from": list(frm)}
    if page: d["page"] = page
    if salient: d["salient"] = salient
    if deferred: d["deferred"] = True
    if adds: d["adds"] = adds
    return d

def show(claim, method, motivation, children, frm=(), page=None, salient=None, adds=None):
    d = {"intention": "show", "claim": claim, "method": method, "motivation": motivation,
         "children": children, "from": list(frm)}
    if page: d["page"] = page
    if salient: d["salient"] = salient
    if adds: d["adds"] = adds
    return d

def number(node, prefix="S0"):
    node["id"] = prefix
    for i, c in enumerate(node.get("children", []), 1):
        number(c, prefix + "." + str(i) if prefix != "S0" else "S" + str(i))
