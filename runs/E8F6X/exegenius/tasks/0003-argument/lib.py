import json, re
SRC = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E8F6X/sources/paper.tex').read()
LINES = SRC.split('\n')
LINEOF = {}

def Q(line, text):
    cands=[i+1 for i,l in enumerate(LINES) if text in l]
    assert cands, ("NOTFOUND", line, text)
    best=min(cands,key=lambda c:abs(c-line))
    if abs(best-line)>6: print("WARN far", line, best, text[:50])
    if len(cands)>1: print("WARN multi", cands, text[:50])
    return {"source": "paper", "quote": text, "_line": best}

def inf(id, claim, line, text, frm=None, page=None, deferred=False, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": Q(line, text)}
    if frm: n["from"] = frm
    if page: n["page"] = page
    if deferred: n["deferred"] = True
    if salient: n["salient"] = salient
    return n

def show(id, claim, method, mtext, msrc, children, mline=None, mquote=None, page=None, frm=None, adds=None, salient=None):
    mot = {"text": mtext, "source": msrc}
    if msrc == "explicit":
        mot["quote"] = Q(mline, mquote)
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": mot, "children": children}
    if page: n["page"] = page
    if frm: n["from"] = frm
    if adds: n["adds"] = [{"symbol": s, "name": nm, "meaning": mn, "relation": rel} for (s, nm, mn, rel) in adds]
    if salient: n["salient"] = salient
    return n
