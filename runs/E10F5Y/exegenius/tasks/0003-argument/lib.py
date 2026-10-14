import json, re, sys
TEX = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E10F5Y/sources/paper.tex', encoding='utf-8').read()
NT = re.sub(r'\s+', ' ', TEX)

def Q(s):
    return {"source": "paper", "quote": s}

def inf(id, claim, quote, frm=None, deferred=False, page=None, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": Q(quote)}
    if frm: n["from"] = frm
    if deferred: n["deferred"] = True
    if page: n["page"] = page
    if salient: n["salient"] = salient
    return n

def sh(id, claim, method, mtext, msrc, children, mquote=None, page=None, frm=None, adds=None, salient=None):
    mot = {"text": mtext, "source": msrc}
    if mquote: mot["quote"] = Q(mquote)
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": mot, "children": children}
    if page: n["page"] = page
    if frm: n["from"] = frm
    if adds: n["adds"] = adds
    if salient: n["salient"] = salient
    return n

def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

def verify(root):
    bad = 0
    ids = set()
    pos_list = []
    pages = {}
    def walk(n, anc_page, depth):
        nonlocal bad
        if n["id"] in ids:
            print("DUP id", n["id"]); bad += 1
        ids.add(n["id"])
        pg = n.get("page") or anc_page
        if n.get("page"):
            if n["page"] in pages:
                print("DUP page", n["page"]); bad += 1
            pages[n["page"]] = n["id"]
        def chk(ev, what):
            nonlocal bad
            q = re.sub(r'\s+', ' ', ev["quote"]).strip()
            c = NT.count(q)
            if c == 0:
                print("MISSING quote", n["id"], what, repr(q[:100])); bad += 1; return -1
            if c > 1:
                print("MULTI(%d) quote" % c, n["id"], what, repr(q[:100]))
            return NT.find(q)
        if n["intention"] == "infer":
            p = chk(n["quote"], "quote")
            if not n.get("deferred"):
                pos_list.append((p, n["id"]))
            if n.get("children"):
                print("infer with children", n["id"]); bad += 1
        else:
            if not n.get("children"):
                print("show without children", n["id"]); bad += 1
            m = n.get("motivation")
            if m["source"] == "explicit":
                if not m.get("quote"):
                    print("explicit without quote", n["id"]); bad += 1
                else:
                    chk(m["quote"], "motquote")
            for c in n.get("children", []):
                walk(c, pg, depth + 1)
    walk(root, None, 0)
    last = -1
    for p, i in pos_list:
        if p < last:
            print("ORDER violation at", i, p, "prev", last); bad += 1
        last = max(last, p)
    # adds check
    def allclaims(n):
        out = [n["claim"]]
        for c in n.get("children", []):
            out += allclaims(c)
        return out
    def chkadds(n):
        nonlocal bad
        for a in n.get("adds", []):
            sym = a["symbol"]
            found = False
            for cl in sum([allclaims(c) for c in n.get("children", [])], []):
                for mm in re.findall(r'\$(.+?)\$', cl, flags=re.S):
                    if sym in mm:
                        found = True
            if not found:
                print("adds symbol not in descendants' math:", n["id"], sym); bad += 1
        for c in n.get("children", []):
            chkadds(c)
    chkadds(root)
    print("pages used:", len(pages), "ids:", len(ids), "bad:", bad)
    return bad, pages
