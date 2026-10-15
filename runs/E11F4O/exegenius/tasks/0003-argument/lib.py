def ev(q):
    return {"source": "paper", "quote": q}


def bind(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


def infer(id, claim, quote, frm=None, page=None, salient=None, deferred=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote)}
    if page:
        n["page"] = page
    if frm:
        n["from"] = frm
    if salient:
        n["salient"] = salient
    if deferred:
        n["deferred"] = True
    return n


def show(id, claim, method, mot_text, mot_source, children, mot_quote=None,
         frm=None, page=None, adds=None, salient=None):
    mot = {"text": mot_text, "source": mot_source}
    if mot_quote:
        mot["quote"] = ev(mot_quote)
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": mot, "children": children}
    if page:
        n["page"] = page
    if frm:
        n["from"] = frm
    if adds:
        n["adds"] = adds
    if salient:
        n["salient"] = salient
    return n
