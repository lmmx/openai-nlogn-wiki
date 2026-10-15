import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import bind, infer, show
import p1, p2, p3, p4

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = open(os.path.join(PROJ, "sources", "paper.tex")).read()


def s2():
    return show(
        "S2",
        r"Two tape procedures save a power of their parameter: interchanging two disjoint $u$-bit address fields costs $O(Vu^\tau)$, and a simultaneous normalized butterfly layer on at most $d$ chunks of polynomial records costs $O(Vd^{\lambda'})$, with $\tau,\lambda'<1$ fixed.",
        r"Derive both from fixed finite linear networks that exchange two banks while restoring scratch values and whose total edge rank $s$ is below $Wm$: run each network on row-split role streams of volume $V/W$ with frames, implement each edge change by smaller calls of the same procedure, and solve the volume-normalized recurrence.",
        r"Multiplying the parameter by $m$ multiplies the normalized recursive cost only by $s/W<m$, so the cost grows like a power of the parameter below one.",
        "explicit",
        [p1.s21(), p1.s22(), p2.s23(), p2.s24()],
        mot_quote=r"After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving.",
        frm=["tape-address-model", "linear-network", "common-frame-principle", "multitape-tm", "big-o"],
        adds=[
            bind("m", "label dimension",
                 r"The dimension $m=h^3=10^6$ of the networks' label space; a call with parameter $mf$ makes smaller calls with parameter $f$.", "count"),
            bind("W", "wire count",
                 r"The number of wires (roles) of the network in use, $W_{\rm b}=177176569091445000000$ for the bit network and $W_{\rm c}=1873807244643542670000$ for the complex one; rows are dealt cyclically among them.", "count"),
            bind("s", "smaller-call count",
                 r"The number of smaller calls one network invocation makes, the sum over edges of the edge rank (bit network) or residual dimension (complex network), with $s<Wm$.", "count"),
            bind("q", "radix",
                 r"A fixed radix of address digits; for the interchange, a fixed odd prime avoiding all denominators of the bit network's matrices."),
            bind("u", "field width",
                 r"The number of bits in each of the two interchanged address fields.", "count"),
            bind(r"\sigma", "complex exponent",
                 r"The fixed exponent $\sigma=1-2^{-50}$ with $s_{\rm c}/W_{\rm c}<m^\sigma$, governing the butterfly-layer recursion."),
        ],
        salient=r"A procedure whose final effect is an exact permutation of data is made cheaper than moving the data, because its intermediate steps form linear combinations of data streams.",
    )


def s3():
    return show(
        "S3",
        r"Multiplication reduces to normalized convolution over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ on $d-1$ axes: radix digits give an integer convolution, the Chinese-remainder map places it on distinct prime axes of lengths $s_i$, Gaussian resampling and chirps express the permuted prime-length transforms $RF_{\boldsymbol s}$ through convolutions on power-of-two axes of lengths $t_i$, and a phase twist turns these into ring convolutions, with errors small enough for exact recovery.",
        r"Build the ring convolution from synthetic transforms and packed products, express the permuted prime-length transforms through it by resampling and chirps, show that the retained permutation cancels, and assemble the algorithm with its error analysis.",
        r"Over $\mathbb C[y]/(y^r+1)$ the transforms consist only of address rearrangements, signed shifts and two-point butterflies, exactly the operations the two fast tape procedures accelerate.",
        "explicit",
        [p3.s31(), p3.s32(), p3.s33(), p3.s34(), p4.s35()],
        mot_quote=r"In this representation, the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations.",
        frm=["cyclic-convolution", "dft", "multidimensional-dft", "polynomial-ring-mod",
             "established-multiplier"],
        adds=[
            bind("t_i", "power-of-two axis length",
                 r"The length of axis $i$ of the padded box, $t_i\in\{r/2,r\}$ with $\prod_it_i=T$.", "count"),
            bind("s_i", "prime axis length",
                 r"The distinct odd prime length of source axis $i$, with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$.", "count"),
            bind("S", "source size",
                 r"The product $S=\prod_is_i$ of the prime lengths, the cyclic length of the digit convolution, with $T/2<S<T$.", "count"),
            bind(r"\alpha", "Gaussian width",
                 r"The resampling width parameter $\alpha=\lceil(12d^2b)^{1/4}\rceil=\Theta(p^{1/4+\epsilon/2})$."),
            bind(r"\gamma", "resampling scale",
                 r"The exponent $\gamma=2d\alpha^2=o(b)$ of the power of two by which the resampled transform is rescaled."),
            bind(r"\delta", "exponential-cost exponent",
                 r"The fixed exponent $\delta=1/16$ in the cost $O(p^{1+\delta})$ of computing one complex exponential and in the Gaussian map costs."),
            bind("R", "source permutation",
                 r"The coordinate permutation $\bigotimes_iP_{s_i}$, $(P_su)_j=u_{tj}$, left in the transform identity on the prime side."),
            bind("Q", "target permutation",
                 r"The coordinate permutation $\bigotimes_iP_{t_i}$, $(P_tv)_k=v_{-sk}$, left in the transform identity on the power-of-two side."),
        ],
    )


def root():
    return show(
        "S0",
        r"One deterministic multitape Turing machine with a fixed finite alphabet and a fixed number of tapes computes the exact $2n$-bit product of two $n$-bit integers in worst-case time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Schonhage and Strassen in this model.",
        r"Build two tape procedures (address-chunk interchange and simultaneous butterfly layers) whose volume-normalized costs save a power of their parameter through a finite linear network with a rank deficit, embed them in a chain of reductions from integer multiplication to convolution over $\mathbb C[y]/(y^r+1)$, recover the exact product, and divide every cost by the volume $V=Tp=\Theta(n)$.",
        r"Scanning the $\Theta(n)$ stored bits once per transform level over $\Theta(\log n)$ levels already costs $\Theta(n\log n)$, so beating $n\log n$ requires saving on both data movement and butterfly arithmetic.",
        "explicit",
        [p1.s1(), s2(), s3(), p4.s4()],
        mot_quote=r"Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$. We therefore need savings in both movement and arithmetic.",
        frm=["integer-multiplication-conjecture", "multiplication-algorithm", "time-accounting",
             "address-chunk-interchange", "fast-butterfly-layer", "multitape-tm", "big-o"],
        page="main-theorem",
        adds=[
            bind("n", "input length", r"The number of bits in each of the two integers multiplied.", "count"),
            bind(r"\kappa", "saving exponent",
                 r"The fixed exponent $\kappa=2^{-182}$ by which the running time beats $n\lg n$, half the smallest margin $2^{-181}$ of the cost table."),
            bind("V", "logical volume",
                 r"The number of stored data bits of the array being processed; for the full padded array $V=Tp=\Theta(n)$.", "count"),
            bind("b", "digit width",
                 r"The number $b=\lceil\log_2n\rceil$ of bits in one radix-$2^b$ digit of the inputs.", "count"),
            bind("p", "working precision",
                 r"The number $p=6b$ of fractional bits of every fixed-point coefficient.", "count"),
            bind("d", "number of axes",
                 r"The number $d=\lfloor b^\epsilon\rfloor=\Theta(p^\epsilon)$ of transform axes, which also bounds the chunks a butterfly layer selects.", "count"),
            bind("K", "chunk width",
                 r"The number $K=\lfloor d^c\rfloor$ of address bits in one chunk of the transform layout.", "count"),
            bind("r", "record length",
                 r"The number $r=2^{\lceil(\log_2T)/d\rceil}=2^{\Theta(p^{1-\epsilon})}$ of complex coefficients in one polynomial record of $\mathbb C[y]/(y^r+1)$.", "count"),
            bind(r"\ell", "record exponent",
                 r"The exponent $\ell=\log_2r=\Theta(p^{1-\epsilon})$, the number of radix-two levels of an axis of length $r$.", "count"),
            bind("T", "padded box size",
                 r"The number of entries of the padded power-of-two box, the power of two in $[4n/b,8n/b)$.", "count"),
            bind(r"\tau", "interchange exponent",
                 r"The fixed exponent $\tau=1-2^{-50}$ of the address-interchange cost $O(Vu^\tau)$."),
            bind(r"\lambda'", "layer exponent",
                 r"The fixed exponent $\lambda'=1-2^{-54}$ of the butterfly-layer cost $O(Vd^{\lambda'})$."),
            bind(r"\epsilon", "axis exponent",
                 r"The fixed exponent $\epsilon=2^{-75}$ with $d=\Theta(p^\epsilon)$."),
            bind("c", "chunk exponent",
                 r"The fixed exponent $c=2^{-56}$ with $K=\lfloor d^c\rfloor$."),
        ],
        salient=r"The bound beats the conjectured optimum $n\log n$ by the factor $(\lg n)^{\kappa}$ with $\kappa=2^{-182}$: tiny, but a genuine power of the logarithm, valid for every input length.",
    )


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


NSRC = norm(SRC)


def walk(n, depth=0):
    yield n, depth
    for c in n.get("children", []) or []:
        yield from walk(c, depth + 1)


def math_segments(s):
    return re.findall(r"\$(.+?)\$", s)


def check(rootn):
    ok = True
    ids = set()
    last = -1
    pages = {}
    for n, dep in walk(rootn):
        if n["id"] in ids:
            print("dup id", n["id"]); ok = False
        ids.add(n["id"])
        if n.get("page"):
            if n["page"] in pages:
                print("page twice", n["page"], pages[n["page"]], n["id"]); ok = False
            pages[n["page"]] = n["id"]
        if n["intention"] == "infer":
            q = norm(n["quote"]["quote"])
            cnt = NSRC.count(q)
            if cnt == 0:
                print("QUOTE MISSING", n["id"], q); ok = False; continue
            if cnt > 1:
                print("quote occurs", cnt, n["id"])
            pos = NSRC.find(q)
            if not n.get("deferred"):
                if pos < last:
                    print("ORDER", n["id"], pos, last); ok = False
                last = max(last, pos)
        else:
            mq = n["motivation"].get("quote")
            if mq and norm(mq["quote"]) not in NSRC:
                print("MOT QUOTE MISSING", n["id"], mq["quote"]); ok = False
        # adds check
        for b in n.get("adds", []) or []:
            sym = b["symbol"]
            pat = re.compile(r"(?<![A-Za-z\\])" + re.escape(sym) + r"(?![A-Za-z])")
            found = False
            for d, _ in walk(n):
                if d is n:
                    continue
                for seg in math_segments(d["claim"]):
                    if pat.search(seg):
                        found = True
                        break
                if found:
                    break
            if not found:
                print("ADDS not found below", n["id"], sym); ok = False
    return ok, pages


if __name__ == "__main__":
    r = root()
    ok, pages = check(r)
    g = json.load(open(os.path.join(PROJ, "exegenius", "graph.json")))
    order = []
    md = open(os.path.join(PROJ, "exegenius", "tasks", "0003-argument.md")).read()
    sec = md.split("## Pages, in reading order")[1].split("## Concepts")[0]
    order = re.findall(r"^- `([^`]+)`", sec, re.M)
    known = [c["id"] for c in g["concepts"] if c.get("known")]
    pos = {p: i for i, p in enumerate(order)}
    # from check
    def chk(n, inh):
        nonlocal_ok = True
        pg = n.get("page") or inh
        for f in n.get("from", []) or []:
            if f in known:
                continue
            if f not in pos:
                print("unknown from", n["id"], f); nonlocal_ok = False
            elif pos[f] >= pos[pg]:
                print("from not before page", n["id"], f, pg); nonlocal_ok = False
        for c in n.get("children", []) or []:
            nonlocal_ok &= chk(c, pg)
        return nonlocal_ok
    ok &= chk(r, "main-theorem")
    used_from = set()
    for n, _ in walk(r):
        used_from.update(n.get("from", []) or [])
    for p in order:
        if p not in pages and p not in used_from:
            print("page unused", p); ok = False
    print("pages presenting steps:", len(pages), "nodes:", sum(1 for _ in walk(r)))
    out = os.path.join(PROJ, "exegenius", "tasks", "0003-argument.answer.json")
    json.dump({"root": r}, open(out, "w"), indent=1, ensure_ascii=False)
    print("OK" if ok else "PROBLEMS", out)
