import json, re

SRC = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E10F3Y/sources/paper.tex').read()


def ev(q):
    return {"source": "paper", "quote": q}


def mot(text, source, quote=None):
    return {"text": text, "source": source, "quote": ev(quote) if quote else None}


def add(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


def infer(id, claim, quote, frm=None, salient=None, deferred=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote)}
    if frm:
        n["from"] = frm
    if salient:
        n["salient"] = salient
    if deferred:
        n["deferred"] = True
    return n


def show(id, claim, method, motivation, children, page=None, frm=None, adds=None, salient=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children}
    if page:
        n["page"] = page
    if frm:
        n["from"] = frm
    if adds:
        n["adds"] = adds
    if salient:
        n["salient"] = salient
    return n
