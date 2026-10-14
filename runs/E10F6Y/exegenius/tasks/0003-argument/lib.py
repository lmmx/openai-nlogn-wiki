import json, re, sys

SRC = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E10F6Y/sources/paper.tex', encoding='utf-8').read()

PAGES = """convolution-multiplication negacyclic-ring hvdh-multiplier multitape-streams controlled-shifts
bank-exchange-network linear-algebra-spaces frames-on-arrays subspace-labels recursive-power-saving
bit-shear-interface lower-triangular-factorization matrix-shear-cost power-width-interchange chunk-interchange
phase-frames packed-selected-bit-addition fixed-point-precision guard-bits signed-kronecker-packing
discrete-fourier-transform radix-two-fft synthetic-transforms simultaneous-butterfly-layer synthetic-transform-layout
synthetic-convolution coefficient-twist gaussian-resampling bluestein-chirp permutation-cancellation tensor-resampling
crt-cyclic-convolution parameter-choice multiplication-algorithm exact-recovery time-bound-accounting
multiplication-below-nlogn""".split()
PIDX = {p: i for i, p in enumerate(PAGES)}

CONCEPTS = """big-o polynomials complex-numbers turing-machines modular-arithmetic-and-congruences
primes-coprimality-and-gcd euclidean-algorithm-and-modular-inverses trial-division-and-primality-search
binary-representation-bit-strings-and-xor radix-representation-and-carry-propagation logarithms-floor-and-ceiling
recurrences-and-induction divide-and-conquer-multiplication permutations-and-bijections matrices-invertibility-and-rank
gaussian-elimination vector-spaces-bases-and-dimension cartesian-products-and-lexicographic-order
rational-numbers-and-dyadic-fractions norms-absolute-value-and-triangle-inequality euler-s-formula-and-roots-of-unity
rounding-and-square-roots polynomial-time-and-computational-cost-on-tapes fast-fourier-transform-as-a-known-algorithm""".split()


def ev(sub):
    return {"source": "paper", "quote": sub}


def mot(text, src, quote=None):
    d = {"text": text, "source": src}
    d["quote"] = ev(quote) if quote else None
    return d


def ad(symbol, name, meaning, rel="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": rel}


def inf(id, claim, quote, frm=(), deferred=False, salient=None, page=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": list(frm)}
    if deferred:
        n["deferred"] = True
    if salient:
        n["salient"] = salient
    if page:
        n["page"] = page
    return n


def sh(id, claim, method, motiv, kids, page=None, frm=(), adds=(), salient=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": motiv,
         "children": list(kids), "from": list(frm)}
    if page:
        n["page"] = page
    if adds:
        n["adds"] = list(adds)
    if salient:
        n["salient"] = salient
    return n


def walk(n, f, depth=0):
    f(n, depth)
    for c in n.get("children", []):
        walk(c, f, depth + 1)


def check(root, verbose=True):
    problems = []
    ids = set()
    quotes = []
    used_pages = {}

    def visit(n, d):
        if n["id"] in ids:
            problems.append("dup id " + n["id"])
        ids.add(n["id"])
        if n.get("page"):
            if n["page"] in used_pages:
                problems.append("page reused %s: %s %s" % (n["page"], used_pages[n["page"]], n["id"]))
            used_pages[n["page"]] = n["id"]
            if n["page"] not in PIDX:
                problems.append("bad page " + n["page"])
        if n["intention"] == "infer":
            q = n["quote"]["quote"]
            c = SRC.count(q)
            if c == 0:
                problems.append("QUOTE NOT FOUND %s: %r" % (n["id"], q))
            else:
                if c > 1:
                    problems.append("quote not unique (%d) %s: %r" % (c, n["id"], q))
                quotes.append((n["id"], SRC.find(q), n.get("deferred", False)))
            if n.get("children"):
                problems.append("infer with children " + n["id"])
        else:
            if not n.get("children"):
                problems.append("show without children " + n["id"])
            m = n.get("motivation")
            if m and m["source"] == "explicit":
                if not m.get("quote") or SRC.count(m["quote"]["quote"]) < 1:
                    problems.append("motivation quote not found %s: %r" % (n["id"], m.get("quote")))
            if m and m["source"] != "explicit" and m.get("quote"):
                problems.append("non-explicit with quote " + n["id"])
    walk(root, visit)
    # order check
    last = -1
    lastid = None
    for id, pos, dfd in quotes:
        if dfd:
            continue
        if pos < last:
            problems.append("ORDER: %s at %d (line %d) precedes previous %s at %d (line %d)" % (
                id, pos, SRC.count("\n", 0, pos) + 1, lastid, last, SRC.count("\n", 0, last) + 1))
        else:
            last = pos
            lastid = id
    # from checks
    def page_of(n, inherited):
        return n.get("page") or inherited

    def fchk(n, inh):
        pg = page_of(n, inh)
        for f in n.get("from", []):
            if f in CONCEPTS:
                continue
            if f not in PIDX:
                problems.append("unknown from %s in %s" % (f, n["id"]))
            elif pg is None or PIDX[f] >= PIDX[pg]:
                problems.append("from %s not before page %s (node %s)" % (f, pg, n["id"]))
        for c in n.get("children", []):
            fchk(c, pg)
    fchk(root, None)
    # pages unused must be in from
    allfrom = set()
    def collect(n, d):
        allfrom.update(n.get("from", []))
    walk(root, collect)
    for p in PAGES:
        if p not in used_pages and p not in allfrom:
            problems.append("page neither step nor from: " + p)
    # adds check
    def mathof(n):
        s = ""
        def g(m, d):
            nonlocal s
            s += " ".join(re.findall(r"\$(.+?)\$", m["claim"], flags=re.S)) + " "
        for c in n.get("children", []):
            walk(c, g)
        return s
    def achk(n, d):
        for a in n.get("adds", []):
            if a["symbol"] not in mathof(n):
                problems.append("adds symbol %s of %s not in descendants' math" % (a["symbol"], n["id"]))
    walk(root, achk)
    # deferred count
    nd = sum(1 for q in quotes if q[2])
    if verbose:
        print("nodes:", len(ids), "infer quotes:", len(quotes), "deferred:", nd)
        for p in problems:
            print("PROBLEM:", p)
    return problems
