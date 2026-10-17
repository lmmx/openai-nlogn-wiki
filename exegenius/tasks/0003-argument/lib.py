import json, re
SRC = open('/home/user/e2e-run/sources/paper.tex').read()

PAGES = """ring-y exchange-network array-frames subspace-labels rank-recurrence machine-model conjecture stream-ops fixed-point hvdh-multiplier signed-packing controlled-shifts matrix-shear address-interchange packed-bit-addition convolution radix-digit-reduction phase-twist precision-recovery dft butterfly multidim-transform synthetic-transform crt-map gaussian-resampling chirp retained-permutations frequency-order phase-kernel phase-frames simultaneous-layer transform-layout ring-convolution parameter-choice multiplication-algorithm cost-accounting main-result""".split()
KNOWN = """big-o polynomials complex-numbers turing-machines schoolbook-and-karatsuba-multiplication divide-and-conquer-recurrences binary-and-radix-representation two-s-complement-integers bitwise-xor-and-arithmetic-mod-2 logarithms-and-floors-ceilings modular-arithmetic-and-primes roots-of-unity vector-spaces-subspaces-dimension-and-rank matrices-and-linear-operators gaussian-elimination-and-triangular-factorization orthogonality-and-inner-products norms-and-the-triangle-inequality permutations-and-bijections cartesian-products-and-multi-index-arrays directed-acyclic-graphs-and-networks-of-gates summation-geometric-series-and-induction rounding-to-the-nearest-integer-and-exactness multitape-turing-machine-running-time integer-exponentials-and-tuple-notation""".split()

def ev(q): return {"source": "paper", "quote": q}
def B(sym, name, meaning, rel="direct"):
    return {"symbol": sym, "name": name, "meaning": meaning, "relation": rel}

def inf(id, claim, quote, frm=None, salient=None, deferred=False):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": frm or []}
    if salient: n["salient"] = salient
    if deferred: n["deferred"] = True
    return n

def show(id, claim, method, mot, msrc, mquote=None, children=(), page=None, frm=None, adds=None, salient=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": {"text": mot, "source": msrc, "quote": ev(mquote) if mquote else None},
         "children": list(children), "from": frm or []}
    if page: n["page"] = page
    if adds: n["adds"] = adds
    if salient: n["salient"] = salient
    return n

def walk(n):
    yield n
    for c in n.get("children", []):
        yield from walk(c)

def check(root):
    ids = [n["id"] for n in walk(root)]
    assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]
    # quotes in order
    pos = 0
    last_line = 0
    for n in walk(root):
        if n["intention"] == "infer":
            q = n["quote"]["quote"]
            cnt = SRC.count(q)
            assert cnt >= 1, ("quote not found", n["id"], q)
            i = SRC.find(q, pos)
            if i < 0:
                print("OUT OF ORDER", n["id"], q[:60]); continue
            if cnt > 1: print("note: quote occurs", cnt, "times", n["id"], q[:50])
            line = SRC.count("\n", 0, i) + 1
            if line < last_line: print("ORDER", n["id"])
            last_line = line
            pos = i + len(q)
            n["_line"] = line
        m = n.get("motivation")
        if m and m.get("quote"):
            assert m["quote"]["quote"] in SRC, ("motivation quote not found", n["id"], m["quote"]["quote"])
            assert m["source"] == "explicit"
        if m and m["source"] == "explicit":
            assert m.get("quote"), n["id"]
    # pages
    used = {}
    def rec(n, eff):
        p = n.get("page") or eff
        if n.get("page"):
            assert n["page"] in PAGES, n["page"]
            assert n["page"] not in used, ("page used twice", n["page"])
            used[n["page"]] = n["id"]
        for f in n.get("from", []):
            if f in KNOWN: continue
            assert f in PAGES, ("unknown from", n["id"], f)
            assert PAGES.index(f) < PAGES.index(p), ("from not before page", n["id"], f, p)
        for c in n.get("children", []):
            rec(c, p)
    rec(root, None)
    froms = set(f for n in walk(root) for f in n.get("from", []))
    missing = [p for p in PAGES if p not in used and p not in froms]
    print("pages without step or from:", missing)
    # adds appear in descendant claims
    for n in walk(root):
        for a in n.get("adds", []):
            if not any(a["symbol"] in d["claim"] for d in walk(n)):
                print("add symbol not in claims:", n["id"], a["symbol"])
    print("nodes:", len(ids), "pages used:", len(used))

def strip(n):
    n = dict(n)
    n.pop("_line", None)
    n["children"] = [strip(c) for c in n.get("children", [])] if "children" in n else None
    if n["children"] is None: del n["children"]
    return n
