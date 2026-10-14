def ev(q):
    return {"source": "paper", "quote": q}

def sym(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

def inf(id, claim, quote, page=None, frm=None, salient=None, deferred=False, adds=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "children": [], "from": frm or []}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if deferred: n["deferred"] = True
    if adds: n["adds"] = adds
    return n

def show(id, claim, method, mot, children, page=None, frm=None, salient=None, adds=None):
    # mot = (source, text) or (source, text, quote)
    m = {"text": mot[1], "source": mot[0]}
    if mot[0] == "explicit":
        m["quote"] = ev(mot[2])
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": m,
         "children": children, "from": frm or []}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n
