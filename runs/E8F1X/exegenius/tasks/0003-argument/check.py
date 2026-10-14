import json, re, sys, os
D = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(D, "gen4.py")).read())
src = open("/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E8F1X/sources/paper.tex").read()

ids = []
pos = 0
bad = 0
def walk(n):
    global pos, bad
    ids.append(n["id"])
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        if q not in src:
            print("MISSING", n["id"], repr(q)); bad += 1; return
        if src.count(q)>1: print('NONUNIQUE', n['id'], src.count(q), repr(q[:60]))
        if n.get("deferred"): return
        i = src.find(q)
        if i >= 0 and i < pos: i = -1
        if i < 0:
            j = src.find(q)
            print("ORDER", n["id"], "at", src[:j].count("\n")+1, "prev pos line", src[:pos].count("\n")+1, repr(q[:50])); bad += 1
        else:
            pos = i + len(q)
    else:
        m = n["motivation"]
        if m.get("quote") and m["quote"]["quote"] not in src:
            print("MISSING motivation", n["id"], repr(m["quote"]["quote"])); bad += 1
        for c in n["children"]: walk(c)
walk(answer["root"])
print("dup ids:", [i for i in set(ids) if ids.count(i) > 1])
# pages
pages = []
def wp(n):
    if n.get("page"): pages.append(n["page"])
    for c in n.get("children", []): wp(c)
wp(answer["root"])
print("pages used:", len(pages), "dups:", [p for p in set(pages) if pages.count(p) > 1])
order = "fixed-tape-model nlogn-conjecture nlogn-multiplier array-order stream-ops controlled-shifts matrix-basics network frames subset-labels rank-saving bit-network lower-triangular matrix-shear power-saving-recurrence power-interchange chunk-interchange packed-bit-addition polynomial-ring-mod kronecker-packing cyclic-convolution int-as-convolution dft butterfly-fft phase-network fixed-point-disk-grid negacyclic-twist simultaneous-layer convolution-theorem multidim-transform synthetic-transform gaussian-resampling chirp-identity permutation-cancellation transform-layout ring-convolution crt-axis-map prime-lengths complex-convolution source-transform exact-recovery mult-algorithm parameter-balance main-theorem".split()
known = "big-o polynomials complex-numbers tape-machines asymptotic-notation-beyond-big-o logarithms-and-exponentials floor-ceiling-and-rounding proof-by-induction-and-recursion sets-subsets-and-basic-combinatorics functions-bijections-and-permutations graphs modular-arithmetic primes-coprimality-and-gcd binary-field-f2-and-xor positional-number-representation-and-carries dyadic-rationals-and-binary-fractions exponential-function-and-gaussian-function vectors-matrices-and-linear-maps vector-norms-and-error-bounds boolean-gates-and-circuits determinism-and-exact-versus-approximate-computation".split()
idx = {p: i for i, p in enumerate(order)}
print("pages missing:", [p for p in order if p not in pages and p not in set(f for f in [])][:50])
allfrom = set()
def wf(n, curpage):
    pg = n.get("page") or curpage
    for f in n.get("from", []):
        allfrom.add(f)
        if f in known: continue
        if f not in idx: print("UNKNOWN from", n["id"], f); continue
        if idx[f] >= idx[pg]: print("FROM ORDER", n["id"], f, "page", pg)
    for c in n.get("children", []): wf(c, pg)
wf(answer["root"], None)
print("pages without step and not in from:", [p for p in order if p not in pages and p not in allfrom])
# adds check
def math_segments(s):
    return re.findall(r"\$(.+?)\$", s)
def desc_claims(n):
    out = []
    for c in n.get("children", []):
        out.append(c["claim"]); out += desc_claims(c)
    return out
def chk(n):
    for a in n.get("adds", []):
        sym = a["symbol"]
        segs = " ".join(" ".join(math_segments(c)) for c in desc_claims(n))
        pat = r"(?<![A-Za-z\\])" + re.escape(sym) + r"(?![A-Za-z])" if re.match(r"^[A-Za-z]$", sym) else re.escape(sym)
        if not re.search(pat, segs): print("ADDS not found:", n["id"], sym)
        # symbol in own claim? ok
    for c in n.get("children", []): chk(c)
chk(answer["root"])
print("bad:", bad)
json.dump(answer, open(os.path.join(D, "..", "0003-argument.answer.json"), "w"), indent=1)
