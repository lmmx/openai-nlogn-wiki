import json, re, sys

PROJ = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E11F3O"
SRC = open(PROJ + "/sources/paper.tex").read()
NSRC = re.sub(r"\s+", " ", SRC)

PAGES = """schonhage-strassen-conjecture hh-multiplier tape-stream-operations controlled-shift exchange-network frames
subspace-labels rank-saving matrix-factorization matrix-shear power-width-interchange chunk-interchange
packed-selected-bit-addition negacyclic-ring kronecker-packing contraction-error guard-bits cyclic-convolution
radix-digit-convolution phase-twist exact-recovery dft fft-butterfly chirp-identity phase-frames
simultaneous-butterfly-layer multidimensional-transform synthetic-transform bit-reversed-order transform-layout
ring-convolution gaussian-resampling permutation-cancellation crt-axis-map prime-axis-lengths parameter-choice
multiplication-algorithm time-bound main-theorem""".split()
KNOWN = """big-o-notation polynomials complex-numbers multitape-turing-machine asymptotic-notation-beyond-big-o
limits-and-limit-inferior logarithms-exponentials-floors-and-ceilings recurrences-and-geometric-sums
positional-number-systems-and-carries schoolbook-and-karatsuba-multiplication bitwise-operations-and-xor
modular-arithmetic primes-coprimality-and-the-extended-euclidean-algorithm roots-of-unity matrices-and-linear-maps
vector-spaces-subspaces-dimension-and-rank inner-products-bilinear-forms-and-orthogonal-complements
gaussian-elimination-and-triangular-matrices permutations-bijections-and-permutation-matrices
arithmetic-modulo-2-and-linear-algebra-over-f-2 finite-sets-subsets-and-counting circuits-and-directed-acyclic-graphs
vector-norms-and-the-triangle-inequality fixed-point-numbers-dyadic-rationals-and-rounding
row-major-order-and-matrix-transposition subroutines-and-reductions-between-problems convolution-of-sequences""".split()
ORDER = {p: i for i, p in enumerate(PAGES)}


def ev(q):
    return {"source": "paper", "quote": q}


def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


def infer(id, claim, quote, page=None, frm=(), salient=None, deferred=False):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote)}
    if page:
        n["page"] = page
    if frm:
        n["from"] = list(frm)
    if salient:
        n["salient"] = salient
    if deferred:
        n["deferred"] = True
    return n


def show(id, claim, method, mot_text, mot_source, children, mot_quote=None, page=None, frm=(), salient=None, adds=()):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": {"text": mot_text, "source": mot_source, "quote": ev(mot_quote) if mot_quote else None}}
    if page:
        n["page"] = page
    if frm:
        n["from"] = list(frm)
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = list(adds)
    n["children"] = children
    return n


exec(open(PROJ + "/exegenius/tasks/0003-argument/tree.py").read())

ans = {"root": ROOT}
json.dump(ans, open(PROJ + "/exegenius/tasks/0003-argument.answer.json", "w"), indent=1, ensure_ascii=False)

# ---------------- validation ----------------
errs = []
ids = set()
pages_used = {}
froms = set()
positions = []


def norm(q):
    return re.sub(r"\s+", " ", q).strip()


def math_of(claim):
    return " ".join(re.findall(r"\$([^$]*)\$", claim))


def walk(n, page_ctx, depth):
    if n["id"] in ids:
        errs.append("dup id " + n["id"])
    ids.add(n["id"])
    pg = n.get("page") or page_ctx
    if n.get("page"):
        if n["page"] not in ORDER:
            errs.append("bad page " + n["page"])
        if n["page"] in pages_used:
            errs.append("page used twice " + n["page"] + " " + pages_used[n["page"]] + " " + n["id"])
        pages_used[n["page"]] = n["id"]
    for f in n.get("from", []):
        froms.add(f)
        if f in KNOWN:
            continue
        if f not in ORDER:
            errs.append(f"{n['id']}: unknown from {f}")
        elif ORDER[f] >= ORDER[pg]:
            errs.append(f"{n['id']}: from {f} not before page {pg}")
    if n["claim"].count("$") % 2:
        errs.append(n["id"] + ": odd $ in claim")
    if n["intention"] == "infer":
        q = norm(n["quote"]["quote"])
        pos = NSRC.find(q)
        if pos < 0:
            errs.append(f"{n['id']}: quote not found: {q[:80]}")
        elif NSRC.count(q) > 1:
            errs.append(f"{n['id']}: quote occurs {NSRC.count(q)} times")
        positions.append((n["id"], pos, n.get("deferred", False)))
        if n.get("children"):
            errs.append(n["id"] + " infer with children")
    else:
        m = n["motivation"]
        if m["source"] == "explicit":
            q = norm(m["quote"]["quote"])
            if NSRC.find(q) < 0:
                errs.append(f"{n['id']}: motivation quote not found: {q[:80]}")
        # adds check
        desc_math = []

        def collect(c):
            desc_math.append(math_of(c["claim"]))
            for cc in c.get("children", []):
                collect(cc)
        for c in n["children"]:
            collect(c)
        dm = " ".join(desc_math)
        for b in n.get("adds", []):
            if b["symbol"] not in dm:
                errs.append(f"{n['id']}: adds symbol {b['symbol']} not in descendant math")
        for c in n["children"]:
            walk(c, pg, depth + 1)


walk(ROOT, "main-theorem", 0)
last = -1
for id, pos, d in positions:
    if d:
        continue
    if pos < last:
        errs.append(f"order violation at {id}")
    last = max(last, pos)
for p in PAGES:
    if p not in pages_used and p not in froms:
        errs.append("page uncovered " + p)
if ROOT.get("page") != "main-theorem":
    errs.append("root page")
print("nodes", len(ids), "infer", len(positions))
print("\n".join(errs) if errs else "OK")
