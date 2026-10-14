import json, sys

ROOT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F8B"
SRC = open(ROOT + "/sources/paper.tex").read()


def ev(q):
    return {"source": "paper", "quote": q}


def mot(text, src, quote=None):
    return {"text": text, "source": src, "quote": ev(quote) if quote else None}


def infer(id, claim, quote, page=None, frm=None, salient=None, deferred=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": frm or []}
    if page:
        n["page"] = page
    if salient:
        n["salient"] = salient
    if deferred:
        n["deferred"] = True
    return n


def show(id, claim, method, motivation, children, page=None, frm=None, salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children, "from": frm or []}
    if page:
        n["page"] = page
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = adds
    return n


def b(symbol, name, meaning, relation):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


# ---------------------------------------------------------------- S1
s1_3 = show(
    "S1.3",
    "For $e=m^k$, two disjoint chunks of $e$ radix-$q$ digits can be interchanged in time $O(Ve^\\tau)$, provided a row field preceding both chunks has length divisible by $W^k$.",
    "Run a fixed bit network on $W$ role streams of volume $V/W$ whose edge changes are address shears, and implement each shear by smaller interchanges of the same kind.",
    mot("The network exchanges two banks of values and the changes of representation along its edges are address shears; splitting rows among its $W$ roles makes every smaller interchange act on a $1/W$ fraction of the data, so the cost obeys a recurrence in the chunk width.",
        "recoverable"),
    [
        infer("S1.3.1",
              "A forward invocation of the scalar network adds $x_S$ to $y_S$ whatever the initial values of its scratch wires, and three stages compose to the exchange $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ that restores every scratch wire.",
              "invocation changes $y_S$ to $y_S+x_S$ and leaves every other value",
              page="scratch-restoring-exchange",
              frm=["arithmetic-modulo-2-and-xor", "sets-subsets-and-cartesian-products"],
              salient="The exchange restores every scratch wire to its arbitrary initial value, so no scratch array ever has to be cleared or known in advance."),
        infer("S1.3.2",
              "If each wire carries an array stored as $D_vg$ for a frame $D_v$, every pointwise linear gate commutes with its common frame, so the network implements only the endpoint operator $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$.",
              "Thus the common frame commutes with the pointwise gate, and",
              page="array-frames",
              frm=["matrices-vectors-and-linear-maps", "permutations-and-bijections", "scratch-restoring-exchange"]),
        infer("S1.3.3",
              "Labels built from indicator vectors of three-element subsets are nested along every edge, every role is moved by the endpoint difference $I_m$, and the total edge rank satisfies $s<Wm$.",
              "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$.",
              page="subset-intersection-labels",
              frm=["rank-and-orthogonal-subspaces", "dot-product-inner-product-and-orthogonality",
                   "sets-subsets-and-cartesian-products", "scratch-restoring-exchange", "array-frames"],
              salient="The total edge rank $s$ falls short of $Wm$ by a tiny relative amount (about $10^{-14}$), but strictly, and that strict shortfall is the whole source of the power saving."),
        infer("S1.3.4",
              "The shear $(H,D)\\mapsto(H+AD,D)$ for a rational matrix $A$ of rank $a$ is performed with exactly $a$ interchanges of pairs of smaller fields and $O(V)$ further work.",
              "can be performed with exactly $a$ interchanges of pairs of $b$-digit",
              page="address-shear-factorization",
              frm=["triangular-and-permutation-matrices", "matrices-vectors-and-linear-maps",
                   "controlled-cyclic-shift", "tape-address-model", "modular-arithmetic"]),
        infer("S1.3.5",
              "Dividing time by volume, the normalized cost $F_k$ at width $m^k$ satisfies $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
              "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).",
              page="rank-saving-recurrence",
              frm=["divide-and-conquer-and-recurrences", "geometric-series-and-sums",
                   "subset-intersection-labels", "address-shear-factorization"],
              salient="The per-volume cost grows by the factor $s/W$, which is below $m$, each time the width is multiplied by $m$; this is why the cost is a power $e^\\tau$ with $\\tau<1$ instead of $e$."),
        infer("S1.3.6",
              "Since $s/W<m^\\tau$, the geometric sum gives $F_k=O(e^\\tau)$, so the interchange costs $O(Ve^\\tau)$.",
              "Hence $F_k=O(e^\\tau)$.",
              frm=["rank-saving-recurrence", "geometric-series-and-sums"]),
    ],
    page="power-width-interchange",
    frm=["tape-address-model", "controlled-cyclic-shift", "divide-and-conquer-and-recurrences"],
    adds=[
        b("W", "wire count", "The number of wires of the fixed bit network, each of which becomes one role stream.", "count"),
        b("m", "label dimension", "The dimension of the label space, so each chunk is split into $m$ fields.", "count"),
        b("s", "total edge rank", "The sum over all edges of the network of the rank of the edge matrix difference, equal to the number of smaller interchanges per call.", "count"),
        b("e", "chunk width", "The number $m^k$ of radix digits in each of the two interchanged chunks.", "count"),
    ],
)

s1 = show(
    "S1",
    "Two disjoint contiguous address chunks of $u$ bits of an array of volume $V$ can be interchanged in time $O(Vu^\\tau)$ for a fixed $\\tau<1$, although the intermediate steps form XOR combinations of data.",
    "Build the interchange from elementary scans and controlled shifts and a fixed linear network with a rank saving for power widths, then pad to arbitrary widths.",
    mot("A network whose total edge rank is below the wire count times the dimension turns the interchange cost into a recurrence with a power saving, which a plain pass over the array per level cannot give.",
        "explicit", "the resulting recurrence saves a power of the chunk width."),
    [
        infer("S1.1",
              "Digit permutations, digit moves, digit splits and cyclic row splits of an array stored in lexicographic order each cost $O(V)$ on a fixed number of tapes.",
              "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
              page="tape-address-model",
              frm=["multidimensional-arrays-and-row-major-order", "multitape-turing-machine",
                   "binary-numerals-and-bit-strings", "positional-notation-in-any-radix"]),
        infer("S1.2",
              "A target field in $[Q]$ that follows its control fields is shifted by an offset computed from the controls, modulo $Q$, in $O(V)$ time.",
              "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
              page="controlled-cyclic-shift",
              frm=["modular-arithmetic", "cyclic-shifts-and-rotations-of-lists", "tape-address-model"]),
        s1_3,
        infer("S1.4",
              "An arbitrary width after the high digits is written in base $m$ and split into pieces of power widths, each interchanged by the power-width procedure on a padded row field.",
              "Proposition~\\ref{prop:power-interchange} to each corresponding pair.",
              frm=["positional-notation-in-any-radix", "geometric-series-and-sums"]),
        infer("S1.5",
              "Padding the binary chunks of $u$ bits to radix-$q$ chunks and scanning away the padding gives the interchange of two $u$-bit chunks in $O(Vu^\\tau)$.",
              "Since $e=O(u)$ for fixed $q$, the bound is",
              frm=["integer-division-with-remainder-floor-and-ceiling"]),
    ],
    page="address-chunk-interchange",
    frm=["permutations-and-bijections", "arithmetic-modulo-2-and-xor", "multidimensional-arrays-and-row-major-order"],
    adds=[b("u", "chunk width", "The number of bits in each of the two address chunks being interchanged.", "count")],
)

# ---------------------------------------------------------------- S2
s2 = show(
    "S2",
    "Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ to the same bit position in each of $D\\le d$ address chunks of polynomial records at once costs $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$, with a single truncation at the end.",
    "Write the tensor power of $H_0$ through the tensor power of the kernel $C=aI+bX$, evaluate that by the complex phase network recursively with packed changes of selected address bits, and convert back to $H_0$.",
    mot("Doing the $D$ butterflies one after another would need $D$ passes over the whole array, so one network call must serve all the selected bits at once.",
        "explicit", "factors would require $D$ whole-array passes."),
    [
        infer("S2.1",
              "Applying the complex phase network to a group of $e$ selected axes, with column frames built from $C=HSH=aI+bX$, produces $C^{\\otimes e}$ on every role, using $s_{\\rm c}$ child calls on $e/m$ axes each.",
              "$C^{\\otimes e}$ on every role, including roles whose initial scratch",
              page="phase-frame-network",
              frm=["array-frames", "subset-intersection-labels", "rank-and-orthogonal-subspaces",
                   "scratch-restoring-exchange", "complex-numbers", "fixed-point-complex-arithmetic"],
              salient="The endpoint operator is the same tensor power $C^{\\otimes m}$ on every role, including the scratch roles that carried no meaningful data, so one uniform operator results from a very uneven network."),
        infer("S2.2",
              "The basis changes between slots are binary row additions $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$ on selected bits of whole chunks, done by a constant number of whole-chunk cyclic shifts plus a deterministic sorting repair of the few bad addresses.",
              "At the selected positions $j_i=\\rho+iK$, numbered from the least",
              page="packed-selected-bit-addition",
              frm=["address-chunk-interchange", "controlled-cyclic-shift", "tape-address-model",
                   "sorting-and-its-cost", "arithmetic-modulo-2-and-xor"]),
        infer("S2.3",
              "The phase-frame construction reduces $e$ selected bits to $s_{\\rm c}$ children on $e/m$ bits each of $1/W_{\\rm c}$ of the volume, so the total time is $O(Vd^{\\lambda'})$ on fixed tapes.",
              "above give total time $O(Vd^{\\lambda'})$ on fixed tapes, including",
              frm=["rank-saving-recurrence", "divide-and-conquer-and-recurrences"]),
        infer("S2.4",
              "Since $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$ with exact Gaussian dyadic phases, the exact $C$-layer converts to the normalized $H_0$ layer, followed by one truncation $Q_p$.",
              "converts the resulting exact $C$-layer to $\\mathcal H$.",
              frm=["complex-numbers", "dyadic-rationals-and-fixed-width-numerators"]),
    ],
    page="simultaneous-butterfly-layer",
    frm=["fixed-point-complex-arithmetic", "fft-butterflies", "rank-saving-recurrence",
         "address-chunk-interchange", "dyadic-rationals-and-fixed-width-numerators"],
    adds=[b("D", "selected chunks", "The number of address chunks, at most $d$, whose same bit position is acted on by $H_0$ in one layer.", "count")],
)

# ---------------------------------------------------------------- S3
s3 = show(
    "S3",
    "The forward synthetic transform of $d-1$ axes over $\\mathcal R_r$ and its opposite run in $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ time with error below $\\sqrt2\\,\\ell\\,2^{-p}$, and the forward outputs are kept in a retained layout order.",
    "Define the transform by radix-two butterflies with signed-shift twiddles, track where each output lands, and arrange the bits on tape so that each round is one simultaneous butterfly layer.",
    mot("The cheap roots of unity make the arithmetic free of real multiplications, so the remaining cost is address movement and butterflies; the work is to place each round's selected bits where the simultaneous layer can use them.",
        "explicit", "The work here is to apply the simultaneous layers on a suitable tape"),
    [
        infer("S3.1",
              "In $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ the powers of $\\omega_t=y^{2r/t}$ are signed shifts, so the transforms $F_t^\\pm$ are contractions and satisfy $F_t^+F_t^-=t^{-1}I$.",
              "F_t^+F_t^-=t^{-1}I.",
              page="synthetic-polynomial-transform",
              frm=["negacyclic-ring", "discrete-fourier-transform", "fft-butterflies",
                   "roots-of-unity-and-euler-s-formula", "triangle-inequality-and-norms"]),
        infer("S3.2",
              "The forward procedure writes frequency $j$ at the bit-reversed slot, and the opposite procedure consumes that same order, so the permutation $B_t$ is never executed.",
              "directly in this order; it does not move whole frequency indices.",
              page="stored-frequency-order",
              frm=["fft-butterflies", "synthetic-polynomial-transform", "permutations-and-bijections"],
              salient="Nothing ever sorts the frequency indices: the bit-reversal permutation is carried along as the storage order, because the pointwise product commutes with any record permutation."),
        infer("S3.3",
              "Placing the selected bit of every participating axis at a common offset in consecutive $K$-bit chunks by bit moves and chunk interchanges makes each round a simultaneous layer, with all layout and restoration charged in the stated cost.",
              "Both layout construction and final restoration are charged in this",
              frm=["address-chunk-interchange", "simultaneous-butterfly-layer", "tape-address-model"]),
    ],
    page="transform-tape-layout",
    frm=["synthetic-polynomial-transform", "simultaneous-butterfly-layer", "stored-frequency-order",
         "address-chunk-interchange", "fixed-point-complex-arithmetic", "negacyclic-ring"],
)

# ---------------------------------------------------------------- S4
s4 = show(
    "S4",
    "The normalized cyclic convolution $\\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\\mathcal R_r$ is computed from two forward synthetic transforms, a pointwise polynomial product divided by $r$ and the opposite transform, with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
    "Multiply the retained forward outputs pointwise in their stored order, using signed packing and the established $O(n\\log n)$ multiplier for each polynomial product, then scale and account for the errors by contractions.",
    mot("The pointwise product commutes with applying the same record permutation to both operands, so the forward outputs can be multiplied in their retained order and passed on directly.",
        "explicit", "forward outputs in their retained order and pass that order directly"),
    [
        infer("S4.1",
              "Two disk-grid polynomials in $\\mathcal R_r$ are multiplied exactly by evaluating signed coefficients at $B_0=2^{4p}$, multiplying the integers, and extracting coefficients with centered carries, in time $O(rp\\log(rp))$.",
              "$O(rp\\log(rp))$ on a fixed number of tapes.  The output is a disk",
              page="signed-packing",
              frm=["n-log-n-barrier", "negacyclic-ring", "positional-notation-in-any-radix",
                   "binary-numerals-and-bit-strings"]),
        infer("S4.2",
              "Both forward transforms are performed and kept in their common order, the polynomial records are multiplied pointwise in that order, and the opposite procedure then consumes that order.",
              "Perform both forward transforms and retain their common $LB$ order.",
              frm=["transform-tape-layout", "stored-frequency-order"]),
        infer("S4.3",
              "Since $F^-(f*g)=M(F^-f)(F^-g)$ and $F^+F^-=I/M$, the scaled result is $(f*g)/(rM)=(f*g)/T$.",
              "To check normalization, expansion of the finite sums gives",
              frm=["convolution", "discrete-fourier-transform"]),
        infer("S4.4",
              "The three transform errors and the product truncation add, so the final result after the exact scaling by $M$ has error less than $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
              "The final exact multiplication by $M$ therefore gives error less than",
              frm=["contraction-error-propagation"]),
    ],
    page="normalized-ring-convolution",
    frm=["transform-tape-layout", "synthetic-polynomial-transform", "stored-frequency-order",
         "contraction-error-propagation", "convolution", "negacyclic-ring", "fixed-point-complex-arithmetic"],
    adds=[
        b("M", "record count", "The number $T/r$ of ring elements in an array, i.e. the product of the first $d-1$ axis lengths.", "count"),
        b("\\ell", "log record length", "The base-two logarithm of the record length $r$, i.e. the number of butterfly rounds per long axis.", "direct"),
    ],
)

# ---------------------------------------------------------------- S5..S7
s5 = show(
    "S5",
    "The normalized Fourier transform of the prime-length source can be computed, up to the exact factor $2^\\gamma$, from a power-of-two transform: $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with contractions $\\mathcal A,\\mathcal B_0$ and approximations of error below $dp^2$.",
    "Use Harvey and van der Hoeven's Gaussian resampling for one axis, keeping both coordinate permutations in the identity, then tensor it over the $d$ axes.",
    mot("The integer product needs transforms of pairwise coprime lengths while the synthetic transforms need powers of two, and Gaussian resampling connects the two shapes.",
        "explicit", "The transform lengths needed for the integer product are pairwise coprime,"),
    [
        infer("S5.1",
              "For coprime $s<t$ there are linear contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, computable with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$.",
              "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA.",
              frm=[]),
        infer("S5.2",
              "Tensoring over the axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$, applied line by line on the padded box in time $O(dTp^{3/2+\\delta}\\alpha)$ plus axis exposure at cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
              "Tensoring \\eqref{eq:no-sort-one-dimensional} proves",
              frm=["address-chunk-interchange"]),
    ],
    page="gaussian-resampling",
    frm=["discrete-fourier-transform", "contraction-error-propagation", "exponential-logarithm-and-gaussian-function",
         "modular-arithmetic", "primes-coprimality-and-gcd", "fixed-point-complex-arithmetic", "address-chunk-interchange"],
    adds=[
        b("s", "source length", "The prime length of one axis of the source transform.", "count"),
        b("t", "target length", "The power-of-two length, larger than $s$, of the corresponding axis of the padded box.", "count"),
        b("\\alpha", "Gaussian width", "The integer parameter controlling the width of the Gaussian weights in the resampling maps.", "direct"),
        b("\\gamma", "source scale exponent", "The exponent $2d\\alpha^2$ of the exact power-of-two scale factor on the source transform.", "direct"),
    ],
)

s6 = infer(
    "S6",
    "With the chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$, the permuted transform is $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$: pointwise phases around a cyclic convolution.",
    "The coefficient of $u_{\\boldsymbol k}$ in the right side of",
    page="bluestein-chirp",
    frm=["discrete-fourier-transform", "convolution", "roots-of-unity-and-euler-s-formula"],
)

s7 = infer(
    "S7",
    "Since $F^+_{\\boldsymbol s}R=R^{-1}F^+_{\\boldsymbol s}$, the source permutation $R$ cancels across two forward transforms, their pointwise product and the opposite transform: $(RF_{\\boldsymbol s}^+)[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
    "Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives",
    page="permutation-cancellation",
    frm=["discrete-fourier-transform", "bluestein-chirp", "gaussian-resampling", "permutations-and-bijections", "convolution"],
    salient="No sort of the source coordinates is ever executed: the permutation $R$ appears three times and cancels, which only works because every $t_i$ is a unit modulo $s_i$.",
)

# ---------------------------------------------------------------- S8..S10
s8 = show(
    "S8",
    "With $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, a power of two $T\\in[4n/b,8n/b)$ split into axis lengths $t_i\\in\\{r/2,r\\}$ and distinct primes $s_i$ just below them, $Tp=\\Theta(n)$ and every hypothesis of the transform lemmas holds.",
    "Choose all sizes explicitly as functions of $n$ and verify the hypotheses of each lemma, including the existence of enough primes in the intervals just below $r/2$ and $r$.",
    mot("The product of the primes must fill a fixed fraction of the padded box while each ratio $t_i/s_i$ leaves enough separation for the resampling.",
        "explicit", "The distinct prime lengths $s_i$ must be close to the powers of two"),
    [
        infer("S8.1",
              "The power of two $T$ lies in $[4n/b,8n/b)$, the axis lengths are $r$ or $r/2$ with product $T$, and consequently $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$ and $r=2^{\\Theta(p^{1-\\epsilon})}$.",
              "Take the power of two $T$ in $[4n/b,8n/b)$, and let",
              frm=[]),
        infer("S8.2",
              "Distinct odd primes $s_i$ exist with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$, where $\\eta=1/(4d)$, so $T/2<S<T$.",
              "(1-2\\eta)t_i<s_i\\leq(1-\\eta)t_i.",
              frm=["primes-coprimality-and-gcd"]),
        infer("S8.3",
              "Therefore $\\alpha^4\\theta_i>p$ and all hypotheses of the one-dimensional resampling lemma hold for large $n$.",
              "Thus every hypothesis of Lemma~\\ref{lem:no-sort-resampling} holds for",
              frm=["gaussian-resampling"]),
    ],
    page="parameter-regime",
    frm=["gaussian-resampling", "transform-tape-layout", "simultaneous-butterfly-layer",
         "address-chunk-interchange", "primes-coprimality-and-gcd", "asymptotic-notation-beyond-big-o"],
    adds=[
        b("b", "digit width", "The number $\\lceil\\log_2 n\\rceil$ of bits in a radix digit, which also fixes the precision $p=6b$.", "count"),
        b("\\epsilon", "dimension exponent", "The fixed exponent $2^{-75}$ with $d=\\lfloor b^\\epsilon\\rfloor$.", "direct"),
        b("\\eta", "prime separation", "The parameter $1/(4d)$ that sets how far below $t_i$ the prime $s_i$ lies.", "direct"),
        b("S", "source size", "The product of the prime source lengths $s_i$.", "count"),
    ],
)

s9 = infer(
    "S9",
    "Writing each $n$-bit integer as a polynomial in $2^b$ with $q=\\lceil n/b\\rceil$ digits, the product has degree below $S$ so the cyclic convolution modulo $x^S-1$ has no wraparound, and each coefficient is below $2^{3b}$.",
    "Write the two inputs as polynomials in $2^b$, each with",
    page="radix-digit-reduction",
    frm=["positional-notation-in-any-radix", "convolution", "polynomials", "parameter-regime"],
)

s10 = show(
    "S10",
    "The map $x\\mapsto\\prod_i x_i^{\\mu_i}$ is an algebra isomorphism from $\\mathbb C[x]/(x^S-1)$ onto $\\mathbb C[x_1,\\ldots,x_d]/(x_i^{s_i}-1)$ preserving convolution, and it is implemented with triangular controlled shifts and axis reorderings.",
    "Use the Chinese remainder theorem to split the cyclic convolution over the pairwise coprime lengths, choosing the coordinate powers so that the change of order is triangular.",
    mot("The coordinate powers are chosen so that each coordinate depends only on lower-index digits, which turns the reordering into a sequence of controlled cyclic shifts.",
        "explicit", "algebraic split, with coordinate powers that make the change of order a"),
    [
        infer("S10.1",
              "The image of $x$ has order $S$ and runs through all target monomials, so $\\Phi$ is an isomorphism and preserves cyclic convolution.",
              "$\\Phi$ is an isomorphism and preserves cyclic convolution.",
              frm=["primes-coprimality-and-gcd", "modular-arithmetic"]),
        infer("S10.2",
              "Each triangular update $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j$ is a prefix-controlled cyclic shift of the valid interval, and the axis reorderings use chunk interchanges, for a total cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
              "Each triangular update is a prefix-controlled cyclic shift.  The",
              frm=["controlled-cyclic-shift", "address-chunk-interchange"]),
    ],
    page="crt-axis-map",
    frm=["convolution", "controlled-cyclic-shift", "address-chunk-interchange",
         "primes-coprimality-and-gcd", "modular-arithmetic", "polynomials"],
)

# ---------------------------------------------------------------- S11
s11 = show(
    "S11",
    "The computed source transform $\\widetilde{\\mathscr F}$, from linewise Gaussian maps, a chirp convolution of length $T$ on the padded box, linewise $B_0$ and an exact scale $2^\\gamma$, approximates $\\mathscr F=RF_{\\boldsymbol s}$ on the prime-length source.",
    "Compute the middle factor $QF_{\\boldsymbol t}$ by the chirp identity, obtain its cyclic convolution on the last axis from the synthetic ring convolution by a coefficient twist, and sandwich it between the Gaussian maps.",
    mot("The synthetic convolution is negacyclic in the last coordinate while the chirp identity needs a cyclic convolution on every axis, so a twist is needed before the ring convolution can be used.",
        "recoverable"),
    [
        infer("S11.1",
              "Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ maps cyclic convolution on the last axis to convolution modulo $y^r+1$, and untwisting recovers the cyclic coefficients with the correct sign.",
              "Untwisting therefore recovers the cyclic coefficient with the correct",
              page="coefficient-twist",
              frm=["negacyclic-ring", "convolution", "roots-of-unity-and-euler-s-formula"]),
        infer("S11.2",
              "The computed chirp transform $\\widetilde{\\mathscr C}(x)$ forms $x_0=Q_p(\\overline{\\widetilde a}\\cdot x)$, the twisted convolution $y_0$ with the chirp, and $Q_p(\\overline{\\widetilde a}\\cdot y_0)$.",
              "Thus $\\widetilde a$ is the convolution kernel and $x_0$ is the data",
              frm=["bluestein-chirp", "normalized-ring-convolution"]),
        infer("S11.3",
              "Composing the linewise map $\\mathcal A$, the chirp transform, the linewise $\\mathcal B_0$ and the exact scale $2^\\gamma$ gives a procedure whose exact counterpart is $2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$.",
              "\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A",
              frm=["gaussian-resampling"]),
    ],
    page="tensor-source-transform",
    frm=["gaussian-resampling", "bluestein-chirp", "permutation-cancellation", "normalized-ring-convolution",
         "coefficient-twist", "parameter-regime", "crt-axis-map", "fixed-point-complex-arithmetic",
         "contraction-error-propagation"],
)

# ---------------------------------------------------------------- S12
s12 = infer(
    "S12",
    "Digit conversion, $\\Phi$, two forward source transforms, a pointwise product, one opposite transform, scalings by $S$ and $2^{2b+4}$, rounding, $\\Phi^{-1}$ and carry propagation output the $2n$-bit product, the two scalings undoing the transform normalization and the digit scale.",
    "$2^{2b+4}(u*v)$, whose inverse image under $\\Phi$ is the original",
    page="multiplication-algorithm",
    frm=["radix-digit-reduction", "crt-axis-map", "tensor-source-transform", "permutation-cancellation",
         "parameter-regime", "convolution"],
)

# ---------------------------------------------------------------- S13
s13 = show(
    "S13",
    "Every call receives a disk-grid input, and the recovered convolution coefficients are within an error below $1/2$ of integers below $2^{3b}$, so rounding and carry propagation give the exact product.",
    "Track the maximum-modulus norm and the accumulated error through each computed step, using contractions and bilinear contractions, then compare the scaled error with $1/2$.",
    mot("Each step is an exact contraction or bilinear contraction composed with a bounded truncation, so errors add and norms stay in the unit disk, which is exactly what the later steps need as hypotheses.",
        "recoverable"),
    [
        infer("S13.1",
              "The ring convolution has error below $E_{\\rm ring}=M(3L+2)<5TL$ in units of $2^{-p}$ and its output norm stays below $.701$.",
              "E_{\\rm ring}:=M(3L+2)<5TL.",
              frm=["contraction-error-propagation", "triangle-inequality-and-norms"]),
        infer("S13.2",
              "The computed source transform has error below $E_sh_p$ with $E_s=9\\,2^\\gamma TL$, and its output norm stays below $.501$.",
              "E_s=9\\,2^\\gamma TL,",
              frm=["contraction-error-propagation", "gaussian-resampling"]),
        infer("S13.3",
              "After the two scalings by $S$ and $2^{2b+4}$ the final absolute error is below $448b\\,2^{-3b/4}<1/2$, so the nearest integer to each coefficient is the correct one.",
              "\\le448b\\,2^{-3b/4}<\\frac12.",
              frm=["permutation-cancellation"]),
        infer("S13.4",
              "Carries $k_{j+1}=\\lfloor(c_j+k_j)/Q_0\\rfloor$ with $Q_0=2^b$ propagate in increasing order and yield the exact $2n$ output bits.",
              "To propagate carries, let $Q_0=2^b$.  The recovered ordinary",
              frm=["positional-notation-in-any-radix", "integer-division-with-remainder-floor-and-ceiling", "radix-digit-reduction"]),
    ],
    page="precision-exact-recovery",
    frm=["contraction-error-propagation", "fixed-point-complex-arithmetic", "gaussian-resampling",
         "permutation-cancellation", "normalized-ring-convolution", "parameter-regime", "radix-digit-reduction",
         "tensor-source-transform", "triangle-inequality-and-norms"],
)

# ---------------------------------------------------------------- S14
s14 = show(
    "S14",
    "Dividing every cost by $V=Tp$ gives normalized costs at most $p^{1-2\\kappa}$, so the total time is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$ with $\\kappa=2^{-182}$.",
    "List the normalized cost of each operation as a power of $p$, take the seven dominant powers, and compare their margins below one with $2\\kappa$.",
    mot("Each of the seven displayed powers is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually, so the slack of $\\kappa$ in the exponent absorbs the remaining logarithmic factors.",
        "explicit", "Each of the seven displayed powers is at most $1-2\\kappa$ by"),
    [
        infer("S14.1",
              "The seven margins below one are $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$, so the smallest is $2^{-181}=2\\kappa$.",
              "Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
              frm=["asymptotic-notation-beyond-big-o"],
              salient="The smallest margin, $2^{-181}$, comes from the chunk-exchange term $pK^{\\tau-1}$, whose power of $p$ is $1-\\epsilon c(1-\\tau)$ with three tiny exponents multiplied together; it is why $\\kappa$ is as small as $2^{-182}$."),
        infer("S14.2",
              "The first three rows of the table, from layout chunk exchanges, individual and simultaneous butterfly rounds, are the terms of the transform cost bound.",
              "The first three rows are the terms in",
              frm=["transform-tape-layout", "simultaneous-butterfly-layer", "address-chunk-interchange"]),
        infer("S14.3",
              "Hence the complete large-input bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
              "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa}).",
              frm=["big-o-notation", "parameter-regime"]),
    ],
    page="cost-accounting",
    frm=["parameter-regime", "precision-exact-recovery", "transform-tape-layout", "simultaneous-butterfly-layer",
         "address-chunk-interchange", "multiplication-algorithm", "normalized-ring-convolution",
         "gaussian-resampling", "asymptotic-notation-beyond-big-o", "big-o-notation"],
)

root = show(
    "S0",
    "A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
    "Reduce the product to a convolution of radix digits evaluated by approximate Fourier transforms over a polynomial ring, make the transform's address movement and arithmetic cheaper with two new tape procedures, then show the result is exact and add up the cost.",
    mot("Scanning the data once per transform level already costs $\\Theta(n\\log n)$, so a power saving needs savings in both address movement and arithmetic, one tape procedure for each.",
        "explicit", "We therefore need savings in both movement and arithmetic."),
    [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14],
    page="main-theorem",
    frm=["n-log-n-barrier", "convolution", "multitape-turing-machine", "big-o-notation"],
    salient="The saving is a genuine power of the logarithm, but an astronomically small one, $\\kappa=2^{-182}$, equal to half the smallest margin $2^{-181}$ among the cost terms; the proof must explain why such a tiny uniform saving survives all the overheads.",
    adds=[
        b("p", "working precision", "The number of fractional bits of the fixed-point grid on which complex numbers are stored.", "count"),
        b("d", "axis count", "The number of axes of the power-of-two box on which the convolution is computed.", "count"),
        b("r", "record length", "The number of complex coefficients in a polynomial record, a power of two.", "count"),
        b("T", "box size", "The number of entries of the padded power-of-two box, the product of the axis lengths.", "count"),
        b("K", "chunk length", "The number of bits in each address chunk handled by a simultaneous butterfly layer.", "count"),
        b("\\tau", "interchange exponent", "The fixed exponent below one in the cost $O(Vu^{\\tau})$ of interchanging chunks.", "direct"),
        b("\\lambda'", "butterfly exponent", "The fixed exponent below one in the cost $O(Vd^{\\lambda'})$ of a simultaneous butterfly layer.", "direct"),
    ],
)

def walk(n, out):
    if n["intention"] == "infer":
        out.append(n)
    for c in n.get("children", []):
        walk(c, out)


out = []
walk(root, out)
prev = -1
bad = 0
for n in out:
    q = n["quote"]["quote"]
    i = SRC.find(q)
    if i < 0:
        print("MISSING", n["id"], q)
        bad += 1
        continue
    cnt = SRC.count(q)
    flag = "" if i > prev else "  <-- OUT OF ORDER"
    if cnt > 1:
        flag += "  <-- not unique"
    if i <= prev:
        bad += 1
    print(n["id"], i, flag)
    prev = max(prev, i) if i > prev else prev

def mq(n):
    m = n.get("motivation")
    if m and m.get("quote"):
        q = m["quote"]["quote"]
        if SRC.find(q) < 0:
            print("MOTIV MISSING", n["id"], q)
    for c in n.get("children", []):
        mq(c)

mq(root)
json.dump({"root": root}, open(ROOT + "/exegenius/tasks/0003-argument.answer.json", "w"), indent=1)
print("bad", bad)
