import json, re, sys
ROOT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E8F4X"
TEXT = open(ROOT + "/sources/paper.tex").read()

def ev(q):
    assert "\n" not in q, q
    assert TEXT.count(q) == 1, (TEXT.count(q), q)
    return {"source": "paper", "quote": q}

def M(text, src, quote=None):
    d = {"text": text, "source": src}
    d["quote"] = ev(quote) if quote else None
    if src == "explicit":
        assert quote
    return d

def B(symbol, name, meaning, rel="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": rel}

def I(id, claim, quote, frm=None, page=None, salient=None, deferred=False):
    d = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": frm or []}
    if page: d["page"] = page
    if salient: d["salient"] = salient
    if deferred: d["deferred"] = True
    return d

def S(id, claim, method, mot, children, page=None, frm=None, salient=None, adds=None):
    d = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": mot,
         "children": children, "from": frm or []}
    if page: d["page"] = page
    if salient: d["salient"] = salient
    if adds: d["adds"] = adds
    return d
