import re, json

ROOTDIR = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E8F7X"
SRC = open(ROOTDIR + "/sources/paper.tex").read()
LINES = SRC.split("\n")
LS = []
_o = 0
for _l in LINES:
    LS.append(_o)
    _o += len(_l) + 1
LS.append(_o)

READING = """nlogn-history fixed-tape-model established-multiplier stream-operations controlled-shifts
linear-algebra-prelims xor-linear-network subset-labels frames rank-deficit power-saving-recurrence
bit-shear-interface lower-triangular-factorization matrix-shear-cost power-width-interchange
arbitrary-width-interchange packed-selected-bit-addition negacyclic-ring fixed-point-disk
signed-packing-product error-accounting dft butterfly phase-frame-network simultaneous-butterfly-layer
cyclic-convolution multidimensional-dft bluestein-chirp synthetic-transform retained-frequency-order
transform-layout synthetic-convolution gaussian-resampling padded-box-tensor-resampling
permutation-cancellation radix-digit-convolution crt-map prime-axis-parameters phase-twist
source-transform exact-recovery multiplication-algorithm cost-accounting main-theorem""".split()
RIDX = {p: i for i, p in enumerate(READING)}
KNOWN = """big-o polynomials complex-numbers turing-machine asymptotic-notation-beyond-big-o
logarithms-exponentials-floor-and-ceiling binary-representation-and-bitwise-operations
schoolbook-integer-arithmetic modular-arithmetic primes-coprimality-and-gcd
sets-functions-cartesian-products-and-bijections permutations matrices-and-linear-maps roots-of-unity
summation-geometric-series-and-products recursion-and-divide-and-conquer-recurrences
worst-case-running-time-and-subroutines triangle-inequality-and-norms rational-numbers-and-rounding
newton-s-method tapes-scanning-and-sorting-as-basic-machine-procedures""".split()


def rx(s):
    parts = re.split(r"\s+", s.strip())
    return r"\s+".join(re.escape(p) for p in parts)


def span(hint, start, end=None):
    lo = LS[max(hint - 4, 0)]
    hi = LS[min(hint + 14, len(LINES))]
    m = re.compile(rx(start)).search(SRC, lo)
    assert m and m.start() < hi, "start not found near line %d: %r" % (hint, start)
    e = m.end()
    if end:
        m2 = re.compile(rx(end)).search(SRC, m.start())
        assert m2, "end not found: %r" % end
        e = m2.end()
    text = SRC[m.start():e]
    assert SRC.count(text) == 1, "quote not unique: %r" % text[:80]
    return text, m.start(), e


OFFS = []  # (order, start, end, id) of non-deferred infer quotes, filled at build


ERRS = []


def ev(hint, start, end=None):
    try:
        t, s, e = span(hint, start, end)
    except AssertionError as ex:
        ERRS.append("line~%d: %s" % (hint, ex))
        return {"source": "paper", "quote": "??"}, 10**9, 10**9
    return {"source": "paper", "quote": t}, s, e


class N:
    def __init__(self, intention, claim, **kw):
        self.intention = intention
        self.claim = claim
        self.kw = kw
        self.children = []


def infer(claim, hint, start, end=None, page=None, frm=None, salient=None, deferred=False, adds=None):
    q, s, e = ev(hint, start, end)
    n = N("infer", claim, page=page, frm=frm or [], salient=salient, deferred=deferred, adds=adds or [])
    n.quote = q
    n.s, n.e = s, e
    return n


def mot(text, source, quote=None):
    d = {"text": text, "source": source, "quote": None}
    if quote:
        hint, start, *rest = quote
        d["quote"] = ev(hint, start, rest[0] if rest else None)[0]
    return d


def show(claim, method, motivation, children, page=None, frm=None, salient=None, adds=None):
    n = N("show", claim, method=method, motivation=motivation, page=page, frm=frm or [], salient=salient,
          adds=adds or [], deferred=False)
    n.children = children
    return n


def bind(symbol, name, meaning, relation):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


def to_json(n, nid):
    d = {"id": nid, "intention": n.intention, "claim": n.claim}
    kw = n.kw
    if n.intention == "show":
        d["method"] = kw["method"]
        d["motivation"] = kw["motivation"]
        d["children"] = [to_json(c, nid + "." + str(i + 1)) for i, c in enumerate(n.children)]
    else:
        d["quote"] = n.quote
        if kw.get("deferred"):
            d["deferred"] = True
    if kw.get("page"):
        d["page"] = kw["page"]
    d["from"] = kw.get("frm", [])
    if kw.get("salient"):
        d["salient"] = kw["salient"]
    if kw.get("adds"):
        d["adds"] = kw["adds"]
    return d


def walk(n, page=None, path="S0", out=None):
    out = [] if out is None else out
    p = n.kw.get("page") or page
    out.append((path, n, p))
    for i, c in enumerate(n.children):
        walk(c, p, path + "." + str(i + 1), out)
    return out


def validate(root):
    items = walk(root)
    pages_used = {}
    problems = []
    last_s = -1
    last_e = -1
    for path, n, p in items:
        pg = n.kw.get("page")
        if pg:
            if pg in pages_used:
                problems.append("page used twice: " + pg)
            pages_used[pg] = path
            if pg not in RIDX:
                problems.append("unknown page " + pg)
        for f in n.kw.get("frm", []):
            if f in KNOWN:
                continue
            if f not in RIDX:
                problems.append("%s: unknown from %s" % (path, f))
            elif p is None or RIDX[f] >= RIDX[p]:
                problems.append("%s: from %s not before page %s" % (path, f, p))
        if n.intention == "infer" and not n.kw.get("deferred") and n.s < 10**9:
            if n.s < last_s:
                problems.append("%s: out of order (line %d < prev %d)" % (path, src_line(n.s), src_line(last_s)))
            elif n.s < last_e:
                problems.append("%s: overlaps previous quote" % path)
            last_s, last_e = max(last_s, n.s), max(last_e, n.e)
    froms = set()
    for path, n, p in items:
        froms.update(n.kw.get("frm", []))
    for pg in READING:
        if pg not in pages_used and pg not in froms:
            problems.append("page neither presented nor in from: " + pg)
    # adds check
    for path, n, p in items:
        for b in n.kw.get("adds", []):
            sym = b["symbol"]
            found = False
            for path2, n2, p2 in walk(n, p, path)[1:]:
                for mm in re.findall(r"\$(.+?)\$", n2.claim, flags=re.S):
                    if sym in mm:
                        found = True
            if not found:
                problems.append("%s: added symbol %s not in claims below" % (path, sym))
    return problems


def src_line(off):
    import bisect
    return bisect.bisect_right(LS, off)
