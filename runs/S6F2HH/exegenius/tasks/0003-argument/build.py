import json, sys

SRC = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/S6F2HH/sources/paper.tex"
OUT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/S6F2HH/exegenius/tasks/0003-argument.answer.json"
TEXT = open(SRC, encoding="utf-8").read()

PAGES = ["n-log-n-conjecture", "radix-digit-convolution", "triple-gadget", "bank-exchange-network",
         "fixed-tape-model", "nlogn-subroutine", "stream-arrays", "frames", "controlled-shifts",
         "bilinear-orthogonal", "subspace-labels", "triangular-factorization", "matrix-shear",
         "power-width-interchange", "chunk-swap", "packed-selected-bits", "negacyclic-ring",
         "signed-kronecker-packing", "fixed-point-disk-grid", "dft-cyclic-convolution",
         "multidim-transform", "crt-axis-map", "gaussian-resampling", "bluestein-chirp",
         "coefficient-twist", "synthetic-transform", "butterfly-layers", "phase-kernel-network",
         "simultaneous-butterfly-layer", "transform-layout", "ring-convolution", "resampling-no-sort",
         "chirp-permutation-cancel", "parameter-choice", "source-transform", "exact-recovery",
         "multiplication-algorithm", "cost-accounting", "main-theorem"]
KNOWN = ["big-o", "polynomials", "complex-numbers", "turing-machine-tapes",
         "modular-arithmetic-and-residues", "primes-divisibility-gcd-and-coprimality",
         "binary-representation-of-integers", "bitwise-xor",
         "logarithms-floors-ceilings-and-powers-of-two", "matrices-invertibility-and-rank",
         "vector-spaces-basis-and-dimension", "permutations-and-permutation-matrices",
         "lexicographic-order-and-index-tuples",
         "euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle",
         "geometric-series-and-orthogonality-of-sums-of-roots-of-unity",
         "norms-and-the-triangle-inequality", "rational-numbers-dyadic-rationals-and-exact-arithmetic",
         "algebraic-structures-groups-rings-and-isomorphisms", "discrete-math-proof-techniques",
         "schoolbook-multiplication-and-divide-and-conquer-multiplication",
         "multitape-machine-cost-model-and-linear-time-scans",
         "complex-polynomial-evaluation-and-interpolation", "gaussian-function",
         "convolution-as-polynomial-multiplication",
         "quantifiers-sets-and-basic-asymptotic-notation-beyond-big-o"]


def ev(q):
    return {"source": "paper", "quote": q}


def infer(id_, claim, quote, page=None, frm=None, deferred=False, salient=None):
    n = {"id": id_, "intention": "infer", "claim": claim, "quote": ev(quote)}
    if page:
        n["page"] = page
    if frm:
        n["from"] = frm
    if deferred:
        n["deferred"] = True
    if salient:
        n["salient"] = salient
    return n


def show(id_, claim, method, motivation, children, page=None, frm=None, adds=None, salient=None):
    n = {"id": id_, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children}
    if page:
        n["page"] = page
    if frm:
        n["from"] = frm
    if adds:
        n["adds"] = adds
    if salient:
        n["salient"] = salient
    return n


def mot(text, source, quote=None):
    return {"text": text, "source": source, "quote": ev(quote) if quote else None}


def bind(symbol, name, meaning, relation):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


ROOT_ADDS = [
    bind("\\kappa", "saving exponent", "the fixed exponent $\\kappa=2^{-182}$ by which the logarithmic factor is reduced", "direct"),
    bind("V", "stored volume", "the number of stored data bits of an array", "count"),
    bind("m", "label dimension", "the dimension $m=h^3=10^6$ of the ambient label space, with ground set size $h=100$", "count"),
    bind("W", "wire count", "the number of wires of the network under consideration", "count"),
    bind("s", "rank sum", "the sum of the rational ranks of all edge differences of a network", "count"),
    bind("N", "source dimension", "the total source dimension of a network, $N=v^3$ with $v=\\binom{100}{3}$", "count"),
    bind("L", "lost dimension", "the total dimension lost on decreasing edges of a network", "count"),
    bind("\\tau", "chunk exponent", "the fixed exponent $\\tau=1-2^{-50}$ with $s/W<m^\\tau$", "direct"),
    bind("u", "chunk width", "the number of bits in each of the two address chunks", "count"),
    bind("\\lambda'", "layer exponent", "the fixed exponent $\\lambda'=1-2^{-54}$ for simultaneous layers", "direct"),
    bind("d", "axis count", "the number of transform axes, $d=\\lfloor b^{\\epsilon}\\rfloor$", "count"),
    bind("K", "chunk bits", "the number of bits in each address chunk of a layer, $K=\\lfloor d^{c}\\rfloor$", "count"),
    bind("b", "radix digit width", "the digit width $b=\\lceil\\log_2 n\\rceil$ of the radix-$2^b$ digits", "count"),
    bind("p", "working precision", "the fixed-point precision $p=6b$ in bits", "count"),
    bind("T", "padded box size", "the padded box size, a power of two in $[4n/b,8n/b)$", "count"),
    bind("S", "prime length product", "the product $S=\\prod_i s_i$ of the distinct prime source lengths", "count"),
    bind("r", "record length", "the number of coefficients in a polynomial record, $r=2^{\\lceil(\\log_2 T)/d\\rceil}$", "count"),
    bind("\\ell", "log record length", "the exponent $\\ell=\\log_2 r$", "count"),
]

# ---- Section 1: finite networks with a rank saving (pre-order leaves in source order)
S1 = show(
    "S1",
    r"The bit network and the complex network have total edge rank $s<Wm$ with a fixed relative deficit, so that $s/W<m^{\tau}$ for both.",
    "label the gates and terminals with nested subspaces of a fixed bilinear space, so that every edge change is an orthogonal residual, and sum the residual dimensions",
    mot("Dimension lost on decreasing edges is the only obstruction to a total rank below $Wm$, so keeping it small gives the deficit the recursion needs.",
        "explicit", "The saving will come from keeping the total dimension lost on decreasing"),
    [
        infer("S1.1", r"A forward invocation adds $x_S$ to $y_S$ and leaves every other value unchanged, whatever the scratch wires initially hold.",
              "invocation changes $y_S$ to $y_S+x_S$ and leaves every other value", page="triple-gadget"),
        infer("S1.2", r"Three invocations, the middle one reversed, send $(X_a,Y_a)\mapsto(-Y_a,X_a)$ and restore every scratch wire.",
              r"(X_a,Y_a)\longmapsto(-Y_a,X_a)", page="bank-exchange-network", frm=["triple-gadget", "matrices-invertibility-and-rank"]),
        infer("S1.3", r"On each edge the orthogonal residual of the smaller label inside the larger has dimension equal to the absolute change in label dimension.",
              "its dimension is the absolute change in label dimension.", page="bilinear-orthogonal",
              frm=["vector-spaces-basis-and-dimension", "frames"]),
        infer("S1.4", r"Neighboring triple lines are orthogonal in either label field, so the labels at adjacent gates are nested.",
              "are orthogonal, in the label field belonging to either construction."),
        infer("S1.5", r"Summing absolute label changes gives $Wm-2N+2L$, the signed sum $Wm-2N$ plus twice the lost dimension $L$.",
              "dimension $L$, the sum of absolute changes is $Wm-2N+2L$."),
        infer("S1.6", r"The lost dimension is kept below half the source dimension, $L<N/2$.",
              "We will obtain $L<N/2$."),
        infer("S1.7", r"The lost dimension is $L=Ich$, with $I$ invocations and $c$ central wires each losing $h$.",
              "L=Ich"),
        infer("S1.8", r"The bit network loses $L_{\rm b}=\frac{100}{539}N$ of dimension.",
              r"\frac{L_{\rm b}}{N}=\frac{100}{539}"),
        infer("S1.9", r"Both loss ratios are below one half.", "both are smaller than $1/2$."),
        infer("S1.10", r"The bit network's total rational rank is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$.",
              r"=W_{\rm b}m-N+2L_{\rm b}"),
        infer("S1.11", r"The bit network's total rational rank is strictly below $W_{\rm b}m$.",
              r"=177176569088785861287000000<W_{\rm b}m"),
        infer("S1.12", r"The complex network's residual kernel count is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$, strictly below $W_{\rm c}m$.",
              r"s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}", page="phase-kernel-network",
              frm=["complex-numbers", "euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle", "bilinear-orthogonal", "frames", "subspace-labels"]),
        infer("S1.13", r"The same fixed exponent $\tau=\sigma=1-2^{-50}$ serves both recurrences.",
              r"\tau=\sigma=1-2^{-50}"),
        infer("S1.14", r"The bit network's ratio satisfies $s_{\rm b}/W_{\rm b}<m^{\tau}$.",
              r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau"),
        infer("S1.15", r"The complex network's ratio satisfies $s_{\rm c}/W_{\rm c}<m^{\sigma}$.",
              r"\frac{s_{\rm c}}{W_{\rm c}}<m^\sigma"),
    ],
    page="subspace-labels",
    frm=["frames", "stream-arrays", "matrices-invertibility-and-rank", "vector-spaces-basis-and-dimension"],
    salient="the total rank $s$ is strictly below $W\\cdot m$, a deficit that holds for both networks with a fixed margin",
)

# ---- Section 2: chunk interchange in O(V u^tau)
S2_power = show(
    "S2.2",
    r"Interchanging two chunks of $e=m^k$ digits costs $O(Ve^\tau)$ time, by recursion on $W$ role streams of volume $V/W$.",
    "split the rows into $W$ role streams, run the rank network on them so that each edge becomes smaller calls, and bound the recursion by a geometric sum",
    mot("Each recursive level multiplies the cost per volume by $s/W$, so a total rank below $Wm$ makes the factor $m^{\\tau}$ or less per level.",
        "explicit", "A recursive call at parameter $mf$ therefore uses $s$ calls at parameter"),
    [
        infer("S2.2.1", r"The recursion makes exactly $s$ calls, one per unit of edge rank, each on a stream of volume $V/W$.",
              "The number of recursive calls is the sum of the edge ranks, exactly $s$."),
        infer("S2.2.2", r"The cost per volume obeys $F_k\le(s/W)F_{k-1}+O(1)$.",
              r"F_k\le(s/W)F_{k-1}+O(1)."),
        infer("S2.2.3", r"Since $a=s/W<m^{\tau}$, the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$.",
              "For $a=s/W<m^\\tau$ the geometric sum"),
        infer("S2.2.4", r"Hence $F_k=O(e^\tau)$, so one power-width call costs $O(Ve^\tau)$.",
              r"Hence $F_k=O(e^\tau)$."),
    ],
    page="power-width-interchange",
    frm=["stream-arrays", "fixed-tape-model", "matrix-shear"],
)

S2 = show(
    "S2",
    r"Two disjoint address chunks of $u$ bits are interchanged in $O(Vu^\tau)$ steps for a fixed $\tau<1$, on any bit array.",
    "realize the interchange by a fixed shear network whose edges become smaller interchanges, then recurse on the chunk width, so that each level's cost is multiplied by $s/W<m^{\\tau}$",
    mot("Each edge of rank $a$ costs $a$ smaller interchanges, and the total rank is below $Wm$, so the recursion saves a power of the chunk width.",
        "explicit", "Because the sum of these ranks is less than the number of wires times"),
    [
        infer("S2.1", r"A rational shear $(H,D)\mapsto(H+AD,D)$ of rank $a$ is performed by exactly $a$ interchanges of field pairs plus linear extra work.",
              "can be performed with exactly $a$ interchanges of pairs of $b$-digit", page="matrix-shear",
              frm=["triangular-factorization", "controlled-shifts", "matrices-invertibility-and-rank"]),
        S2_power,
        infer("S2.3", r"An arbitrary width $e$ is written in base $m$ as $e-\rho=\sum_j a_jm^j$ with $0\le a_j<m$, giving power-width pieces.",
              "Write the remaining width in base $m$:"),
        infer("S2.4", r"The pieces together cost $O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)$.",
              r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)."),
    ],
    page="chunk-swap",
    frm=["fixed-tape-model", "stream-arrays", "controlled-shifts", "triangular-factorization"],
    salient="the final effect is an exact permutation, although the intermediate steps are pointwise XOR combinations of data",
)

# ---- Section 3: simultaneous butterfly layer
S3 = show(
    "S3",
    r"A normalized butterfly $H_0$ on one bit of each of $d$ address chunks of polynomial records is applied in one pass at cost $O(Vd^{\lambda'})$, with $\lambda'<1$, followed by a single truncation.",
    "write $H_0$ as a conjugated two-point phase kernel, realize the kernel products as smaller calls on the selected bits of slots, and truncate once after the whole layer",
    mot("Separate butterfly factors would need $D$ passes over the whole array, whereas the simultaneous layer shares one pass and costs $d^{\\lambda'}$ per unit of volume.",
        "explicit", "factors would require $D$ whole-array passes."),
    [
        infer("S3.1", r"The two-point kernel is $C=\mathsf H\mathsf S\mathsf H=aI+bX$, a combination of the identity and the bit flip.",
              "C=H\\mathsf SH=aI+bX"),
        infer("S3.2", r"The normalized butterfly satisfies $H_0=b\,\mathsf S\,C\,\mathsf S$, so a butterfly layer is a phase-conjugated kernel layer.",
              "H_0=b\\mathsf SC\\mathsf S,"),
        infer("S3.3", r"A binary row addition on the selected bits of several chunks takes a constant number of cyclic shifts and a deterministic repair of an explicit small set of addresses.",
              "We implement a binary row addition on corresponding selected bits in two", page="packed-selected-bits",
              frm=["chunk-swap", "controlled-shifts", "bitwise-xor"]),
        infer("S3.4", r"The whole layer is evaluated exactly and then truncated once, so the result is within $\sqrt2\,2^{-p}$ of $\mathcal H z$.",
              "The procedure evaluates the entire layer exactly before this final"),
        infer("S3.5", r"The recurrence analysis and the packed changes give total time $O(Vd^{\lambda'})$ on fixed tapes.",
              "above give total time $O(Vd^{\\lambda'})$ on fixed tapes, including"),
    ],
    page="simultaneous-butterfly-layer",
    frm=["phase-kernel-network", "butterfly-layers", "packed-selected-bits", "chunk-swap", "power-width-interchange", "complex-numbers"],
    salient="the layer is exact before one truncation, so its error stays below $\\sqrt2\\,2^{-p}$ however many factors it combines",
)

# ---- Section 4: synthetic transform layout cost
S4 = show(
    "S4",
    r"A synthetic transform on $T$ coefficients in records of length $r$ costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$, since each round is one simultaneous layer on a common-offset layout.",
    "place the selected bits of all axes at a common offset in $K$-bit chunks by a fixed layout permutation, run each round as one simultaneous layer, and restore the layout",
    mot("Each transform round must see its selected bits at one common offset in consecutive chunks, so a fixed layout permutation makes every round one simultaneous layer.",
        "explicit", "we must place the selected bits of the participating axes at a common"),
    [
        infer("S4.1", r"The layout transform costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ in total, including layout construction and restoration.",
              "O\\left(Tp\\left[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}\\right]\\right)."),
        infer("S4.2", r"The prefix moves and chunk exchanges define the record permutation $L$, whose inverse costs the same.",
              "These prefix moves and chunk exchanges define $L$."),
        infer("S4.3", r"Each round costs $O(Tpd^{\lambda'})$, so the $\ell$ rounds cost $O(Tp\ell d^{\lambda'})$ in total.",
              "$O(Tp\\ell d^{\\lambda'})$ in total."),
    ],
    page="transform-layout",
    frm=["synthetic-transform", "butterfly-layers", "fixed-point-disk-grid", "simultaneous-butterfly-layer", "chunk-swap", "stream-arrays"],
)

# ---- Section 5: the multiplication algorithm
S5_params = show(
    "S5.1",
    r"The sizes are $b=\lceil\log_2 n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, with $Tp=\Theta(n)$ and distinct prime lengths $S$ close to $T$.",
    "fix the exponents, then choose the padded size, the record length and distinct odd prime lengths just below the power-of-two lengths",
    mot("The distinct prime lengths must be close to the powers of two, so that their product fills a fixed fraction of the padded box while each ratio leaves room for resampling.",
        "explicit", "The distinct prime lengths $s_i$ must be close to the powers of two"),
    [
        infer("S5.1.1", r"The sizes are $b=\lceil\log_2 n\rceil$, $p=6b$ and $d=\lfloor b^\epsilon\rfloor$.",
              "b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,"),
        infer("S5.1.2", r"The padded size satisfies $Tp=\Theta(n)$, with $d=\Theta(p^\epsilon)$.",
              "Tp=\\Theta(n),\\quad d=\\Theta(p^\\epsilon),\\quad"),
        infer("S5.1.3", r"Each $s_i$ is coprime to its power-of-two length $t_i$.",
              "Every $\\gcd(s_i,t_i)$ equals one because $t_i$ is a power of two."),
        infer("S5.1.4", r"The product of the prime lengths satisfies $T/2<S<T$.",
              "Together with $s_i<t_i$, this gives $T/2<S<T$."),
    ],
    page="parameter-choice",
    frm=["primes-divisibility-gcd-and-coprimality", "logarithms-floors-ceilings-and-powers-of-two", "rational-numbers-dyadic-rationals-and-exact-arithmetic"],
)

S5_radix = show(
    "S5.2",
    r"The two $n$-bit inputs are polynomials in $2^b$ with $q=\lceil n/b\rceil$ digits, and their product is the digit convolution with no wraparound.",
    "write both inputs as polynomials in $2^b$, and note that the product degree stays below the padded length $S$",
    mot("Writing integers in radix $2^b$ turns multiplication into a convolution of short digit lists, which the later transforms can handle.",
        "recoverable", None),
    [
        infer("S5.2.1", r"The two inputs are polynomials in $2^b$, each with $q=\lceil n/b\rceil$ nonnegative digits.",
              "Write the two inputs as polynomials in $2^b$, each with"),
        infer("S5.2.2", r"The convolution modulo $x^S-1$ has no nonzero wraparound.",
              "Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
    ],
    page="radix-digit-convolution",
    frm=["binary-representation-of-integers", "polynomials", "convolution-as-polynomial-multiplication"],
)

S5_crt = infer("S5.3", r"The map $\Phi$ is an isomorphism that preserves cyclic convolution, so the digit convolution lives on the prime axes.",
               "$\\Phi$ is an isomorphism and preserves cyclic convolution.", page="crt-axis-map",
               frm=["algebraic-structures-groups-rings-and-isomorphisms", "modular-arithmetic-and-residues", "dft-cyclic-convolution", "multidim-transform", "primes-divisibility-gcd-and-coprimality"])

S5_source = show(
    "S5.4",
    r"The source transform, computed by a chirp transform and two Gaussian maps, has exact counterpart $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.",
    "rewrite the length-$s$ transform as Gaussian maps around a power-of-two tensor transform, evaluate the middle factor as a chirp convolution, and keep the permutations inside the identity",
    mot("Retaining the permutations in the transform formula avoids two full sorts per coordinate, and a power-of-two transform with a chirp is cheaper than a prime-length transform.",
        "explicit", "We retain both permutations in the transform formula and"),
    [
        infer("S5.4.1", r"The middle factor is a normalized cyclic convolution with a chirp kernel: $QF_{\boldsymbol t}u=\bar a\,(a*(\bar a u))/T$.",
              "\\frac{a*(\\overline a\\mathbin{\\cdot}u)}{T}", page="chirp-permutation-cancel",
              frm=["bluestein-chirp", "dft-cyclic-convolution", "multidim-transform", "crt-axis-map"], deferred=True),
        infer("S5.4.1.1", r"The normalized convolution over the ring modulo $y^r+1$ is $\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}$, a bilinear contraction.",
              "\\mathcal M_r(f,g)=\\frac{f*g}{rM}=\\frac{f*g}{T}.", page="ring-convolution",
              frm=["synthetic-transform", "negacyclic-ring", "signed-kronecker-packing", "nlogn-subroutine", "transform-layout", "coefficient-twist"], deferred=True),
        infer("S5.4.2", r"Gaussian resampling without executing the permutations gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with contractive $\mathcal A$ and $\mathcal B_0$.",
              "=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A", page="resampling-no-sort",
              frm=["gaussian-resampling", "multidim-transform", "dft-cyclic-convolution", "fixed-point-disk-grid"], deferred=True),
        infer("S5.4.3", r"The computed source transform has exact counterpart $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$.",
              "\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A"),
    ],
    page="source-transform",
    frm=["gaussian-resampling", "bluestein-chirp", "coefficient-twist", "synthetic-transform", "dft-cyclic-convolution",
         "multidim-transform", "transform-layout", "simultaneous-butterfly-layer", "signed-kronecker-packing",
         "negacyclic-ring", "fixed-point-disk-grid", "butterfly-layers", "chunk-swap", "crt-axis-map", "parameter-choice"],
)

S5_exact = show(
    "S5.8",
    r"The rounded coefficients are the exact convolution coefficients, because their error is below $1/2$, and radix carries then give the $2n$-bit product.",
    "bound the total error by a chain of scaled estimates, round to the nearest integer, then propagate radix-$2^b$ carries",
    mot("The strict error below $1/2$ makes the nearest integer to each scaled value the unique correct coefficient.",
        "explicit", "The strict error below $1/2$ makes the nearest integer to"),
    [
        infer("S5.8.1", r"The source transform has error at most $E_s h_p$ with $E_s=9\cdot2^\gamma TL$.",
              "E_s=9\\,2^\\gamma TL"),
        infer("S5.8.2", r"The product of the two computed transforms is accurate to $(2E_s+2)h_p$.",
              "Thus $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$."),
        infer("S5.8.3", r"The opposite-transform error gives $E_w$, with $E_w=S(3E_s+2)<28\,2^\gamma T^2L$.",
              "E_w:=S(3E_s+2)<28\\,2^\\gamma T^2L."),
        infer("S5.8.4", r"After the scalings the final error is below $448b\,2^{-3b/4}<\frac12$.",
              "448b\\,2^{-3b/4}<\\frac12"),
        infer("S5.8.5", r"Radix carries $k_{j+1}=\lfloor (c_j+k_j)/Q_0\rfloor$ with $Q_0=2^b$ give the digits of the exact product.",
              "To propagate carries, let $Q_0=2^b$."),
        infer("S5.8.6", r"The exact product is less than $2^{2n}$, so after removing padding it is exactly the $2n$-bit output.",
              "The exact product is less"),
    ],
    page="exact-recovery",
    frm=["parameter-choice", "source-transform", "fixed-point-disk-grid", "rational-numbers-dyadic-rationals-and-exact-arithmetic", "binary-representation-of-integers"],
)

S5 = show(
    "S5",
    r"The algorithm outputs the exact $2n$-bit product of two $n$-bit integers by radix digits, prime-axis mapping, two source transforms, a pointwise product, the opposite transform, rescaling, rounding and carries.",
    "radix-digit convolution, prime-axis Chinese-remainder map, two source transforms, pointwise product, opposite transform, two scalings, rounding and carry propagation, in that order",
    mot("A transform turns a cyclic convolution into a pointwise product, so each operand is transformed once, the products are formed pointwise, and one inverse transform recovers the convolution.",
        "recoverable", None),
    [
        S5_params,
        S5_radix,
        S5_crt,
        S5_source,
        infer("S5.5", r"The pointwise product of the two source transforms is computed exactly and truncated once, giving $z$.",
              "Multiply corresponding complex coefficients exactly and truncate"),
        infer("S5.6", r"The opposite transform of $z$ is computed and its grid numerators are scaled exactly by $S$.",
              "Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid"),
        infer("S5.7", r"A second exact scaling by $2^{2b+4}S$ followed by rounding recovers the integer convolution coefficients.",
              "Multiply the grid numerators of $\\widetilde w$ exactly by"),
        S5_exact,
    ],
    page="multiplication-algorithm",
    frm=["nlogn-subroutine", "convolution-as-polynomial-multiplication", "schoolbook-multiplication-and-divide-and-conquer-multiplication"],
)

# ---- Section 6: cost accounting
S6 = show(
    "S6",
    r"Every dominant row of the cost table is at most $p^{1-2\kappa}$ times $Tp$, so the total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
    "divide each cost row by $Tp$, read off its power of $p$, bound each power by $1-2\\kappa$ using the stated margins, and absorb fixed powers of $\\log p$",
    mot("Each row is a power of $p$ times $Tp$, so the largest exponent and its margin determine the overall saving.",
        "recoverable", None),
    [
        infer("S6.1", r"Seven dominant powers of $p$ appear in the cost table, each with a margin below one.",
              "The seven dominant powers in Table~\\ref{tab:costs} have the following"),
        infer("S6.2", r"The margin $g_2=\epsilon c(1-\tau)$ equals $2^{-181}$.", "g_2=2^{-181}"),
        infer("S6.3", r"The smallest margin is $\min_i g_i=2^{-181}=2\kappa$.",
              "Thus $\\min_i g_i=2^{-181}=2\\kappa$."),
        infer("S6.4", r"Each dominant power is at most $1-2\kappa$.",
              "Each of the seven displayed powers is at most $1-2\\kappa$ by"),
        infer("S6.5", r"Any fixed power of $\log p$ is at most $p^{\kappa}$ eventually, so it is absorbed.",
              "Any fixed power of $\\log p$ is at most $p^\\kappa$"),
        infer("S6.6", r"The total cost is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
              "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})."),
    ],
    page="cost-accounting",
    frm=["parameter-choice", "transform-layout", "chunk-swap", "power-width-interchange", "simultaneous-butterfly-layer",
         "ring-convolution", "resampling-no-sort", "chirp-permutation-cancel", "exact-recovery", "multiplication-algorithm"],
    salient="all seven dominant margins are at least $2\\kappa=2^{-181}$, so one fixed $\\kappa$ serves every row",
)

ROOT = show(
    "S0",
    r"A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$.",
    "compute the exact product by a Gaussian-resampling convolution whose transform layers are made cheap by two tape procedures, then sum the costs of every stage",
    mot("A plain scan of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ levels already costs $\\Theta(n\\log n)$, so the savings in movement and arithmetic are needed.",
        "explicit", "We therefore need savings in both movement and arithmetic."),
    [S1, S2, S3, S4, S5, S6],
    page="main-theorem",
    frm=["n-log-n-conjecture", "fixed-tape-model"],
    adds=ROOT_ADDS,
    salient="the saving is a fixed power of the logarithm, $(\\lg n)^{-\\kappa}$, valid for every input length, which refutes the $n\\log n$ conjecture in this model",
)


# ---------------- validation -----------------
errors = []
flat_nodes = []


def walk(n, parent_page, depth=0):
    flat_nodes.append((n, parent_page))
    kids = n.get("children", [])
    page = n.get("page") or parent_page
    for c in kids:
        walk(c, page)


walk(ROOT, None)

# unique ids
ids = [n["id"] for n, _ in flat_nodes]
if len(ids) != len(set(ids)):
    errors.append("duplicate ids")

# quote presence and DFS order for non-deferred infer nodes
prev = -1
pos_report = []
for n, _ in flat_nodes:
    if n["intention"] != "infer":
        continue
    q = n["quote"]["quote"]
    first = TEXT.find(q)
    if first < 0:
        errors.append(f"quote not found: {n['id']}: {q!r}")
        continue
    if n.get("deferred"):
        pos_report.append((n["id"], first, "deferred"))
        continue
    # require the first occurrence to be after the previous non-deferred quote
    if first <= prev:
        errors.append(f"out of order: {n['id']} at {first} <= prev {prev}")
    prev = max(prev, first)
    pos_report.append((n["id"], first, ""))

# pages: every page presented at most once; from ids valid and earlier than page
presented = {}
for n, _ in flat_nodes:
    if n.get("page"):
        if n["page"] in presented:
            errors.append(f"page presented twice: {n['page']} by {presented[n['page']]} and {n['id']}")
        presented[n["page"]] = n["id"]
for n, inh in flat_nodes:
    own = n.get("page") or inh
    own_idx = PAGES.index(own) if own in PAGES else None
    for f in n.get("from", []) or []:
        if f in KNOWN:
            continue
        if f not in PAGES:
            errors.append(f"unknown from id {f} in {n['id']}")
            continue
        if own_idx is None or PAGES.index(f) >= own_idx:
            errors.append(f"from {f} not before page {own} in {n['id']}")
# coverage: every page presented or used in a from
used = set(presented)
for n, _ in flat_nodes:
    for f in n.get("from", []) or []:
        used.add(f)
missing = [p for p in PAGES if p not in used]
if missing:
    errors.append(f"pages not covered: {missing}")

# quotes that are the main page's own step
root_page_check = ROOT.get("page")

answer = {"root": ROOT}
with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(answer, fh, ensure_ascii=False, indent=2)

print("nodes:", len(flat_nodes))
print("infer quotes:")
for r in pos_report:
    print("  ", r)
print("presented pages:", len(presented), "covered:", len(used))
print("ERRORS:" if errors else "no errors")
for e in errors:
    print("  ", e)
