"""Helpers to build argument nodes."""

def mot(text, source, quote=None):
    m = {"text": text, "source": source}
    if quote is not None:
        m["quote"] = {"source": "paper", "quote": quote}
    return m

def bind(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

def show(id, claim, method, motivation, children, page=None, frm=None, adds=None, salient=None):
    n = {"id": id, "intention": "show", "claim": claim, "from": frm or [],
         "method": method, "motivation": motivation}
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = adds
    if page:
        n["page"] = page
    n["children"] = children
    return n

def infer(id, claim, quote, page=None, frm=None, deferred=False, adds=None, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "from": frm or [],
         "quote": {"source": "paper", "quote": quote}}
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = adds
    if page:
        n["page"] = page
    if deferred:
        n["deferred"] = True
    return n
