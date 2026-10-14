import sys, json, re
sys.path.insert(0, ".")
from lib import *
from part1b import S1
from part2 import S2, S3
from part3 import S4, S5

ORDER = """integer-multiplication-conjecture polynomial-ring-mod fixed-point-truncation established-multiplier tape-address-model elementary-stream-ops controlled-shift linear-algebra-basics linear-network address-shear common-frame-principle subset-intersection-labels rank-saving-recurrence address-chunk-interchange packed-selected-bit-addition signed-packing cyclic-convolution radix-digit-convolution phase-twist exact-recovery dft multidimensional-dft butterfly synthetic-transform bluestein-chirp phase-frame-kernel fast-butterfly-layer ring-convolution gaussian-resampling permutation-cancellation crt-address-map parameter-choice multiplication-algorithm time-accounting main-theorem""".split()
KNOWN = """big-o polynomials complex-numbers multitape-tm logarithms-and-iterated-logarithm-notation big-omega-theta-and-little-o-notation binary-representation-and-bit-operations modular-arithmetic primes-coprimality-and-gcd chinese-remainder-theorem roots-of-unity vectors-matrices-and-invertibility finite-field-f2-arithmetic permutations-and-cartesian-products floor-ceiling-and-summation-notation recurrences-and-induction norms-absolute-values-and-error-bounds fast-fourier-transform-and-divide-and-conquer sorting-and-data-movement-on-tapes finite-alphabet-encodings-and-constant-factor-simulation ring-and-group-notions-for-polynomials""".split()

ROOT_NODE = S("S0",
  "A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$.",
  "Reduce the product to a convolution evaluated by transforms whose data movement and butterfly arithmetic are sped up by two tape procedures that each save a power of the logarithm, then assemble the chain of reductions, prove exact recovery of the integer product, and add up the costs.",
  M("Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so savings are needed in both address movement and arithmetic, and two tape procedures supply them.", "explicit",
    "We therefore need savings in both movement and arithmetic. Two tape"),
  [S1, S2, S3, S4, S5],
  page="main-theorem",
  frm=["integer-multiplication-conjecture", "time-accounting", "multiplication-algorithm", "multitape-tm", "big-o", "logarithms-and-iterated-logarithm-notation", "finite-alphabet-encodings-and-constant-factor-simulation"],
  salient="The saving is a genuine power $(\\lg n)^{-\\kappa}$ of the logarithm, though with the astronomically small exponent $\\kappa=2^{-182}$ and astronomically large constants: a power saving, not an iterated-logarithm gain.",
  adds=[B("n", "input length", "The number of bits of each of the two integers being multiplied.", "count"),
        B("\\kappa", "saving exponent", "The constant $2^{-182}$ by which the running time falls short of $n\\lg n$ by the factor $(\\lg n)^{-\\kappa}$.", "direct")])

def walk(n, anc_page=None):
    page = n.get("page") or anc_page
    yield n, page
    for c in n.get("children", []):
        yield from walk(c, page)

def validate(root):
    ids = set(); used_pages = set(); fromset = set()
    last = -1
    errs = []
    for n, page in walk(root):
        if n["id"] in ids: errs.append("dup id " + n["id"])
        ids.add(n["id"])
        if n.get("page"):
            if n["page"] in used_pages: errs.append("page reused " + n["page"])
            used_pages.add(n["page"])
            if n["page"] not in ORDER: errs.append("bad page " + n["page"])
        for f in n.get("from", []):
            fromset.add(f)
            if f in KNOWN: continue
            if f not in ORDER: errs.append("unknown from %s at %s" % (f, n["id"])); continue
            if ORDER.index(f) >= ORDER.index(page): errs.append("from %s not before page %s at %s" % (f, page, n["id"]))
        if n["intention"] == "infer":
            if n.get("children"): errs.append("infer has children " + n["id"])
            if not n.get("deferred"):
                pos = TEXT.index(n["quote"]["quote"])
                if pos <= last: errs.append("order violated at %s (pos %d <= %d)" % (n["id"], pos, last))
                last = pos
        else:
            if not n.get("children"): errs.append("show without children " + n["id"])
            if not n.get("method") or not n.get("motivation"): errs.append("show lacks method/motivation " + n["id"])
        # adds check
        for b in n.get("adds", []):
            found = False
            for d, _ in walk(n):
                if d is n: continue
                for seg in re.findall(r"\$(.+?)\$", d["claim"]):
                    if b["symbol"] in seg: found = True
            if not found: errs.append("adds symbol %s of %s not in descendants' math" % (b["symbol"], n["id"]))
    for pg in ORDER:
        if pg not in used_pages and pg not in fromset: errs.append("page neither step nor from: " + pg)
    if root.get("page") != "main-theorem": errs.append("root page")
    return errs

errs = validate(ROOT_NODE)
print("\n".join(errs) if errs else "VALID")
n_nodes = sum(1 for _ in walk(ROOT_NODE))
print("nodes", n_nodes)
json.dump({"root": ROOT_NODE}, open(ROOT + "/exegenius/tasks/0003-argument.answer.json", "w"), indent=1)
