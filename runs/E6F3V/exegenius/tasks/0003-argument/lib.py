import json, sys
BASE = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F3V"
SRC = open(BASE + "/sources/paper.tex", encoding="utf-8").read()
LINES = SRC.split("\n")

PAGES = """schonhage-strassen-conjecture hh-multiplier tape-stream-operations controlled-shift exchange-network frames
subspace-labels rank-saving matrix-factorization matrix-shear power-width-interchange chunk-interchange
packed-selected-bit-addition negacyclic-ring kronecker-packing contraction-error guard-bits cyclic-convolution
radix-digit-convolution phase-twist exact-recovery dft fft-butterfly chirp-identity phase-frames
simultaneous-butterfly-layer multidimensional-transform synthetic-transform bit-reversed-order transform-layout
ring-convolution gaussian-resampling permutation-cancellation crt-axis-map prime-axis-lengths parameter-choice
multiplication-algorithm time-bound main-theorem""".split()
PORDER = {p: i for i, p in enumerate(PAGES)}
KNOWN = """big-o-notation polynomials complex-numbers multitape-turing-machine asymptotic-notation-beyond-big-o
limits-and-limit-inferior logarithms-exponentials-floors-and-ceilings recurrences-and-geometric-sums
positional-number-systems-and-carries schoolbook-and-karatsuba-multiplication bitwise-operations-and-xor
modular-arithmetic primes-coprimality-and-the-extended-euclidean-algorithm roots-of-unity matrices-and-linear-maps
vector-spaces-subspaces-dimension-and-rank inner-products-bilinear-forms-and-orthogonal-complements
gaussian-elimination-and-triangular-matrices permutations-bijections-and-permutation-matrices
arithmetic-modulo-2-and-linear-algebra-over-f-2 finite-sets-subsets-and-counting circuits-and-directed-acyclic-graphs
vector-norms-and-the-triangle-inequality fixed-point-numbers-dyadic-rationals-and-rounding
row-major-order-and-matrix-transposition subroutines-and-reductions-between-problems convolution-of-sequences""".split()

import re
def _pat(t):
    return r"\s+".join(re.escape(x) for x in t.split())

def quote(a, b, begin, end=None):
    lo = max(1, a - 6); hi = min(len(LINES), b + 6)
    text = "\n".join(LINES[lo - 1:hi])
    m = re.search(_pat(begin), text)
    if not m:
        raise SystemExit("begin not found near %d-%d: %r" % (a, b, begin))
    i = m.start()
    if end is None:
        j = text.find("\n", m.end())
        j = len(text) if j < 0 else j
    else:
        m2 = re.compile(_pat(end)).search(text, m.start())
        if not m2:
            raise SystemExit("end not found near %d-%d: %r" % (a, b, end))
        j = m2.end()
    res = text[i:j]
    if SRC.count(res) != 1:
        raise SystemExit("quote not unique (%d): %r" % (SRC.count(res), res))
    return {"source": "paper", "quote": res}

def mot(kind, text, q=None):
    d = {"text": text, "source": kind}
    if q is not None:
        d["quote"] = q
    return d

def adds(*items):
    return [{"symbol": s, "name": n, "meaning": m, "relation": r} for (s, n, m, r) in items]

def show(id, claim, method, motivation, children, page=None, frm=(), salient=None, ad=None):
    d = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": motivation,
         "children": children, "from": list(frm)}
    if page: d["page"] = page
    if salient: d["salient"] = salient
    if ad: d["adds"] = ad
    return d

def infer(id, claim, q, page=None, frm=(), salient=None, deferred=False):
    d = {"id": id, "intention": "infer", "claim": claim, "quote": q, "from": list(frm)}
    if page: d["page"] = page
    if salient: d["salient"] = salient
    if deferred: d["deferred"] = True
    return d

def validate(root):
    ids = set(); pages = {}; last = [-1]; problems = []
    def walk(n, anc_page):
        if n["id"] in ids: problems.append("dup id " + n["id"])
        ids.add(n["id"])
        pg = n.get("page") or anc_page
        if n.get("page"):
            if n["page"] in pages: problems.append("page twice " + n["page"])
            pages[n["page"]] = n["id"]
            if n["page"] not in PORDER: problems.append("bad page " + n["page"])
        for f in n.get("from", []):
            if f in KNOWN: continue
            if f not in PORDER: problems.append("%s: unknown from %s" % (n["id"], f)); continue
            if pg is None or PORDER[f] >= PORDER[pg]:
                problems.append("%s (page %s): from %s not earlier" % (n["id"], pg, f))
        if n["intention"] == "infer":
            q = n["quote"]["quote"]; s = SRC.find(q)
            if not n.get("deferred"):
                if s <= last[0]:
                    problems.append("%s: quote out of order (pos %d <= %d) line %d" % (n["id"], s, last[0], SRC.count("\n", 0, s) + 1))
                last[0] = max(last[0], s)
        for c in n.get("children", []):
            walk(c, pg)
    walk(root, None)
    allfrom = set()
    def coll(n):
        allfrom.update(n.get("from", []))
        for c in n.get("children", []): coll(c)
    coll(root)
    for p in PAGES:
        if p not in pages and p not in allfrom:
            problems.append("page unused: " + p)
    # adds symbols occur in descendant claims
    def descl(n):
        out = []
        for c in n.get("children", []):
            out.append(c["claim"]); out += descl(c)
        return out
    def chk(n):
        for a in n.get("adds", []):
            if a["symbol"] not in " ".join(descl(n)):
                problems.append("%s: symbol %s not in descendant claims" % (n["id"], a["symbol"]))
        for c in n.get("children", []): chk(c)
    chk(root)
    return problems
