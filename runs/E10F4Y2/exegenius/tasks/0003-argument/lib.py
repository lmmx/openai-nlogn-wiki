import json, re, sys

BASE = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E10F4Y2"
SRC = open(BASE + "/sources/paper.tex").read()

PAGES = """integer-multiplication-conjecture polynomial-ring-mod fixed-point-truncation established-multiplier
tape-address-model elementary-stream-ops controlled-shift linear-algebra-basics linear-network address-shear
common-frame-principle subset-intersection-labels rank-saving-recurrence address-chunk-interchange
packed-selected-bit-addition signed-packing cyclic-convolution radix-digit-convolution phase-twist exact-recovery
dft multidimensional-dft butterfly synthetic-transform bluestein-chirp phase-frame-kernel fast-butterfly-layer
ring-convolution gaussian-resampling permutation-cancellation crt-address-map parameter-choice
multiplication-algorithm time-accounting main-theorem""".split()
KNOWN = """big-o polynomials complex-numbers multitape-tm logarithms-and-iterated-logarithm-notation
big-omega-theta-and-little-o-notation binary-representation-and-bit-operations modular-arithmetic
primes-coprimality-and-gcd chinese-remainder-theorem roots-of-unity vectors-matrices-and-invertibility
finite-field-f2-arithmetic permutations-and-cartesian-products floor-ceiling-and-summation-notation
recurrences-and-induction norms-absolute-values-and-error-bounds fast-fourier-transform-and-divide-and-conquer
sorting-and-data-movement-on-tapes finite-alphabet-encodings-and-constant-factor-simulation
ring-and-group-notions-for-polynomials""".split()


def ev(q):
    n = SRC.count(q)
    if n != 1:
        raise SystemExit("QUOTE count %d: %r" % (n, q))
    return {"source": "paper", "quote": q}


class Node:
    def __init__(self, kind, claim, **kw):
        self.kind = kind
        self.claim = claim
        self.kw = kw
        self.children = kw.pop("children", [])
        self.id = None

    def to_dict(self):
        kw = self.kw
        d = {"id": self.id, "intention": self.kind, "claim": self.claim}
        if kw.get("frm"):
            d["from"] = kw["frm"]
        if kw.get("page"):
            d["page"] = kw["page"]
        if kw.get("adds"):
            d["adds"] = [{"symbol": s, "name": n, "meaning": m, "relation": r} for (s, n, m, r) in kw["adds"]]
        if kw.get("salient"):
            d["salient"] = kw["salient"]
        if self.kind == "show":
            d["method"] = kw["method"]
            mq = kw.get("mq")
            d["motivation"] = {"text": kw["mtext"], "source": kw["msrc"],
                               "quote": ev(mq) if mq else None}
            assert (kw["msrc"] == "explicit") == bool(mq), self.claim
            d["children"] = [c.to_dict() for c in self.children]
        else:
            d["quote"] = ev(kw["quote"])
            if kw.get("deferred"):
                d["deferred"] = True
        return d


def show(claim, method, mtext, msrc, mq=None, children=(), **kw):
    return Node("show", claim, method=method, mtext=mtext, msrc=msrc, mq=mq, children=list(children), **kw)


def infer(claim, quote, frm=(), deferred=False):
    return Node("infer", claim, quote=quote, frm=list(frm), deferred=deferred)


def assign_ids(n, path="S0"):
    n.id = path
    for i, c in enumerate(n.children, 1):
        assign_ids(c, path + "." + str(i))


def walk(n):
    yield n
    for c in n.children:
        yield from walk(c)
