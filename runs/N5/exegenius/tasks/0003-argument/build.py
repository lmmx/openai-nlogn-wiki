import json, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
P = 'paper'
SRC = open(os.path.join(ROOT, 'sources', 'paper.tex')).read()


def ev(q):
    return {"source": P, "quote": q}


def mot(text, source, quote=None):
    d = {"text": text, "source": source}
    if quote is not None:
        d["quote"] = ev(quote)
    return d


def b(sym, name, meaning, rel="direct"):
    return {"symbol": sym, "name": name, "meaning": meaning, "relation": rel}


def infer(id, claim, quote, page=None, frm=(), salient=None, deferred=False):
    d = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": list(frm)}
    if page: d["page"] = page
    if salient: d["salient"] = salient
    if deferred: d["deferred"] = True
    return d


def show(id, claim, method, motivation, children, page=None, frm=(), salient=None, adds=None):
    d = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children, "from": list(frm)}
    if page: d["page"] = page
    if salient: d["salient"] = salient
    if adds: d["adds"] = adds
    return d


# ---------------- Group A: the two tape procedures ----------------
S1 = show("S1",
    r"Arrays of logical volume $V$ stored in lexicographic order admit a toolkit of $O(V)$-time tape operations: digit permutations and moves, splits and merges, cyclic row distribution among $W$ streams, and controlled shifts of a later field.",
    "collect the linear-time scans that every later procedure is built from",
    mot("Every later cost bound is a recurrence on time divided by volume, so the primitives must cost O(V) with constants independent of all field lengths; the paper isolates them first so later steps only count calls.", "recoverable"),
    [
        infer("S1.1",
            r"Permuting or moving a single radix-$q$ digit, splitting and merging on a digit, and distributing rows cyclically among $W$ streams each cost $O(V)$.",
            r"Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
            page="elementary-streams", frm=["tape-array-layout", "binary-counter", "stacks"]),
        infer("S1.2",
            r"An update $y\mapsto y+a(\text{controls})\bmod q^b$ of a target field that follows its control fields, or multiplication of $y$ by a fixed rational unit, costs $O(V)$.",
            r"The next operations are linear because their target field follows their control fields.",
            page="controlled-shifts", frm=["elementary-streams", "modular-arithmetic", "euclidean-algorithm"]),
    ],
    page="tape-array-layout", frm=["multitape-turing-machine", "lexicographic-order", "turing-machine-alphabet-and-simulation-constants"])

S2 = show("S2",
    r"There are two fixed linear networks, one over $\mathbb F_2$ and one over $\mathbb Z[i,1/2]$, each with $W$ wires, that exchange two banks of values, restore all scratch values, and admit nested subspace labels whose edge changes need only $s<Wm$ smaller calls in total.",
    "build the scalar networks from triple-intersection gather/scatter with scratch restoration, lift them to arrays by frames, and count the residual dimensions of nested subspace labels",
    mot("The frame identity shows that only endpoint frames determine the array operator, so intermediate frames can be chosen freely to make each edge cheap; nested subspace labels make an edge's cost its dimension change, and the subset construction keeps the total dimension lost small.", "explicit",
        r"Once the scalar routing is fixed, the endpoint frames determine the array operator on each route; the intermediate frames can then be chosen to make each edge change inexpensive."),
    [
        infer("S2.1",
            r"For arbitrary initial scratch values, the eight-row forward schedule changes $y_S$ to $y_S+x_S$ and restores every scratch wire.",
            r"The net target change is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of $a,c$.",
            page="scratch-restoration", frm=["linear-network"],
            salient="The net effect does not depend at all on the arbitrary initial contents of the scratch wires."),
        infer("S2.2",
            r"Gather/scatter through central wires gives coefficients depending on $|S\cap T|$, side wires cancel the unwanted ones so each invocation is $y\gets y+x$, and three stages give $(X,Y)\mapsto(-Y,X)$.",
            r"Starting from $(x,y)$, the three stages give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
            page="triple-intersection-construction", frm=["scratch-restoration", "binomial-coefficients-and-subsets", "xor-and-arithmetic-modulo-2"],
            salient="Three additive stages compose to an exact signed exchange of banks, which in the bit case is a pure permutation."),
        infer("S2.3",
            r"With an invertible frame $D_v$ at every source, gate and sink, the network on arrays implements $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$, so each route applies only its endpoint frames.",
            r"Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks.",
            page="frames", frm=["linear-network", "linear-maps-and-invertibility", "vectors-and-matrices"],
            salient="All intermediate frames cancel: only the source and sink frames of each route matter."),
        infer("S2.4",
            r"Gates and terminals receive nondegenerate subspaces of an $m$-dimensional bilinear space, nested along every edge, with the only decreasing edges being the central-wire edges from time 3 to time 4.",
            r"Every edge joins comparable nondegenerate labels.",
            page="subspace-labels", frm=["triple-intersection-construction", "frames", "vector-spaces-subspaces-and-dimension", "dot-product-and-orthogonality"]),
        infer("S2.5",
            r"The total dimension lost on decreasing edges satisfies $L/N<1/2$ in both networks, which leaves a strict deficit $s<Wm$.",
            r"In particular, both are smaller than $1/2$.",
            frm=["subspace-labels"]),
    ],
    page="rank-deficit", frm=["linear-network", "rank-of-a-matrix"],
    salient=r"The relative deficit $1-s/(Wm)$ is minute (about $10^{-11}$) yet strictly positive, and it alone produces the power saving.",
    adds=[b("W", "wire count", "The number of wires (roles) of the network, including scratch wires.", "count"),
          b("m", "label dimension", r"The dimension $m=100^3$ of the bilinear label space.", "count"),
          b("s", "smaller-call count", "The total number of smaller calls needed over all edges of the network.", "count")])

S3 = infer("S3",
    r"Since $s/W<m^\tau$ with $\tau=1-2^{-50}$, a call at parameter $mf$ done by $s$ calls at parameter $f$ on volume $V/W$ gives normalized cost $O(f^\tau)$.",
    r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$.",
    page="recursive-saving", frm=["rank-deficit", "elementary-streams", "divide-and-conquer-recurrences", "geometric-series"],
    salient=r"Each level multiplies the parameter by $m$ but the normalized cost by less than $m$, so the exponent drops strictly below one.")

S4 = show("S4",
    r"Two disjoint contiguous $u$-bit address fields of an array of volume $V$ can be interchanged in $O(Vu^\tau)$ time.",
    "implement each edge's matrix shear by rank-many smaller interchanges via a triangular factorization, run the bit network on row-split role streams, recurse on power widths, then pad to arbitrary widths",
    mot("An edge matrix of rank a costs a smaller interchanges, and the ranks sum to less than W m, so the recursion saves a power of the width.", "explicit",
        r"Because the sum of these ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width."),
    [
        infer("S4.1",
            r"Every rational $m\times m$ matrix of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with $a$ ones.",
            r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization",
            page="triangular-factorization", frm=["gaussian-elimination", "rank-of-a-matrix"]),
        infer("S4.2",
            r"The address shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ with $A$ of rank $a$ takes exactly $a$ smaller field interchanges plus $O(V)$ work.",
            r"can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work.",
            page="address-shear", frm=["controlled-shifts", "triangular-factorization"]),
        infer("S4.3",
            r"The bit network with projection frames gives the shear $H\gets H+D$ on every role, with endpoint matrices differing by $I_m$ and edge ranks summing to $s_{\rm b}<W_{\rm b}m$.",
            r"Proposition~\ref{prop:bit-motif-interface} supplies these conditions with $W=W_{\rm b}$ and $s=s_{\rm b}$.",
            page="bit-network-interface", frm=["rank-deficit", "address-shear", "frames"]),
        infer("S4.4",
            r"For widths $e=m^k$ with enough rows, the normalized cost satisfies $F_k\le(s/W)F_{k-1}+O(1)$, hence the interchange costs $O(Ve^\tau)$.",
            r"Hence $F_k=O(e^\tau)$.",
            frm=["recursive-saving", "bit-network-interface"]),
        infer("S4.5",
            r"Supplying rows from high digits, decomposing the width in base $m$ and padding binary chunks to radix $q$ extends the bound to $O(Vu^\tau)$ for every width $u$.",
            r"Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$.",
            frm=["elementary-streams"]),
    ],
    page="fast-address-interchange", frm=["recursive-saving", "elementary-streams", "controlled-shifts"],
    salient=r"The final effect is an exact permutation of data, yet it is computed via XOR combinations of data and works for arbitrary scratch contents.",
    adds=[b("u", "chunk width", "The number of address bits in each of the two interchanged fields.", "count")])

S5 = show("S5",
    r"Applying $H_0$ at one common bit position in each of $D\le d$ equal-width address chunks of polynomial records costs $O(Vd^{\lambda'})$ with $\lambda'<1$, with exact dyadic intermediates and one final truncation.",
    "recurse through the complex network's phase frames, realizing binary basis changes by packed address moves and converting the C-layer to the H_0 layer by phases",
    mot("Separate butterfly factors would need one full pass per selected axis; the phase-frame recursion shares the work across axes and saves a power of d.", "explicit",
        r"We will obtain cost $O(Vd^{\lambda'})$, with $\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly factors would require $D$ whole-array passes."),
    [
        infer("S5.1",
            r"With phase frames $\mathcal C_U$, each edge's frame change is a product of one two-point kernel $aI+bX_v$ per orthonormal residual vector, and telescoping gives $C^{\otimes e}$ on every role by $s_{\rm c}$ child calls on $e/m$ axes.",
            r"Proposition~\ref{prop:complex-motif-interface} therefore gives $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary.",
            page="phase-frames", frm=["subspace-labels", "rank-deficit", "gaussian-dyadics", "normalized-butterfly", "hamming-weight"],
            salient="The same kernel tensor power appears on every role, including scratch roles."),
        infer("S5.2",
            r"Diagonal phases and the scalar $b^D$ convert the exact $C^{\otimes D}$ layer into $H_0^{\otimes D}$ using only Gaussian dyadic operations.",
            r"Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.",
            frm=["normalized-butterfly", "gaussian-dyadics"]),
        infer("S5.3",
            r"Packed changes of selected address bits and the recursion give total time $O(Vd^{\lambda'})$ on fixed tapes.",
            r"The row construction and the recurrence analysis above give total time $O(Vd^{\lambda'})$ on fixed tapes, including all padded and auxiliary streams.",
            frm=["fast-address-interchange", "recursive-saving"]),
        infer("S5.4",
            r"Since $H_0^{\otimes D}$ maps disk arrays to disk arrays, the final truncation $Q_p$ keeps values in the disk with error below $\sqrt2\,2^{-p}$.",
            r"Thus $\mathcal H$ maps disk arrays to disk arrays, and componentwise truncation preserves that disk and has error less than $\sqrt2\,2^{-p}$",
            page="fixed-point-precision", frm=["complex-numbers", "gaussian-dyadics"]),
    ],
    page="simultaneous-butterfly-layer", frm=["recursive-saving", "fast-address-interchange", "polynomial-ring", "normalized-butterfly"],
    adds=[b("d", "axis bound", "The maximum number of address chunks whose selected bits one layer acts on.", "count"),
          b("p", "precision", "The number of fractional bits of the fixed-point grid.", "count")])

A = show("A",
    r"Address-field interchange costs $O(Vu^\tau)$ and a simultaneous butterfly layer costs $O(Vd^{\lambda'})$, with fixed $\tau,\lambda'<1$, where $V$ is the stored bit volume.",
    "turn a strict rank deficit of two finite linear networks into recursive power savings for both tape procedures",
    mot("Each procedure reduces a call at parameter mf to s calls at parameter f on volume V/W; since s<Wm the normalized cost grows by less than m per level, which gives a power saving.", "explicit",
        r"This strict inequality is the source of the power saving."),
    [S1, S2, S3, S4, S5],
    frm=["multitape-turing-machine", "big-o"],
    adds=[b("V", "logical volume", "The number of stored data bits of the array being processed.", "count")])

# ---------------- Group B: transforms and convolution ----------------
S6 = show("S6",
    r"Synthetic transforms over $\mathbb C[y]/(y^r+1)$ on $d-1$ power-of-two axes, with outputs kept in a stored frequency order, cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\ell\,2^{-p}$.",
    "compute Nussbaumer's decimation-in-frequency recursion, group each round into a parallel butterfly plus a monomial, and lay the selected bits out in common-offset chunks for the simultaneous layer",
    mot("The simultaneous layer applies only to selected bits at a common offset in consecutive K-bit chunks, so a layout must be built and its movement charged.", "explicit",
        r"To apply Proposition~\ref{prop:simultaneous-layer} in a transform round, we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks."),
    [
        infer("S6.1",
            r"With root $\omega_t=y^{2r/t}$, decimation-in-frequency butterflies and signed shifts compute $B_tF_t^-$, writing the outputs directly in bit-reversed frequency order.",
            r"The recursion writes its outputs directly in this order; it does not move whole frequency indices.",
            page="synthetic-transform", frm=["polynomial-ring", "normalized-butterfly", "discrete-fourier-transform", "bit-reversal-permutation"]),
        infer("S6.2",
            r"Each round on several axes is a parallel butterfly $\mathcal H$ followed by one recordwise monomial $J_E$.",
            r"Consequently the individual axis steps may be grouped as a parallel butterfly $\mathcal H$, followed by one recordwise monomial operation $J_E$.",
            frm=["multidimensional-transform"]),
        infer("S6.3",
            r"Moving prefix slots and interchanging chunks into the layout, and applying one simultaneous layer per round, gives the stated cost including layout construction and restoration.",
            r"Both layout construction and final restoration are charged in this bound.",
            frm=["simultaneous-butterfly-layer", "fast-address-interchange", "parameter-choice"]),
    ],
    page="transform-layout", frm=["synthetic-transform", "simultaneous-butterfly-layer", "fast-address-interchange"],
    adds=[b("r", "record length", r"The number of complex coefficients in each polynomial record, a power of two.", "count"),
          b("T", "padded box size", r"The number of complex entries in the padded transform array.", "count"),
          b("K", "chunk width", r"The width in bits of the address chunks used by the simultaneous layer.", "count"),
          b(r"\ell", "log record length", r"The base-two logarithm of $r$.", "direct")])

S7 = show("S7",
    r"The normalized cyclic convolution $\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\mathbb C[y]/(y^r+1)$ is computed with error below $\sqrt2M(3\ell+1)2^{-p}$, adding only $O(Tp\log(rp))$ to the transform cost.",
    "transform both operands forward, keep their common stored order, multiply records by signed packing, and apply the opposite transform to that order",
    mot("The opposite transform consumes the stored order directly, so the bit-reversal and layout permutations never have to be undone between the transforms and the pointwise product.", "explicit",
        r"We also specify where each frequency entry is stored, because the opposite transform consumes that same order after a pointwise product."),
    [
        infer("S7.1",
            r"Two polynomial records are multiplied by packing signed coefficients into integers, multiplying with the $O(n\log n)$ multiplier and unpacking, returning $Q_p(fg/r)$ in $O(rp\log(rp))$ time.",
            r"One can compute the exact Gaussian integer numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\log(rp))$ on a fixed number of tapes.",
            page="signed-kronecker-packing", frm=["harvey-hoeven-multiplier", "polynomial-ring", "fixed-point-precision", "two-s-complement-and-signed-integers"]),
        infer("S7.2",
            r"Both forward transforms retain their common $LB$ order, the packed products keep it, and the opposite procedure consumes it.",
            r"Perform both forward transforms and retain their common $LB$ order.",
            frm=["transform-layout"]),
    ],
    page="synthetic-convolution", frm=["transform-layout", "signed-kronecker-packing", "cyclic-convolution"])

S8 = show("S8",
    r"The tensor of prime-length source transforms satisfies $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with power-of-two lengths $t_i$, contractions $\mathcal A,\mathcal B_0$, and the permutations $R,Q$ kept in the formula.",
    "apply Harvey and van der Hoeven's one-dimensional resampling identity with both coordinate permutations retained, then take tensor products line by line using chunk swaps",
    mot("The needed transform lengths are pairwise coprime while synthetic transforms need powers of two; resampling connects the shapes, and keeping the permutations in the formula avoids two full sorts per coordinate.", "explicit",
        r"Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and compute that formula directly."),
    [
        infer("S8.1",
            r"For coprime $s<t$, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ with contractions $A,B_0$ computable with error below $p^2$.",
            r"There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ satisfying",
            frm=["discrete-fourier-transform", "exponential-function-and-gaussians", "prime-numbers-and-gcd"]),
        infer("S8.2",
            r"Linewise tensoring gives the multidimensional identity with contractions $\mathcal A,\mathcal B_0$, and exposing lines costs $O(Tp\,d^2(1+\ell^\tau))$.",
            r"Both $\mathcal A$ and $\mathcal B_0$ are contractions.",
            frm=["multidimensional-transform", "fast-address-interchange"]),
    ],
    page="gaussian-resampling", frm=["multidimensional-transform", "fixed-point-precision"])

S9 = infer("S9",
    r"The middle factor $QF_{\boldsymbol t}u$ equals $\overline a\cdot(a*(\overline a\cdot u))/T$ for a chirp $a$, so it is a normalized cyclic convolution between two phase multiplications.",
    r"The factor $QF_{\boldsymbol t}$ in \eqref{eq:no-sort-tensor} can be computed from a cyclic convolution and two pointwise phase multiplications.",
    page="bluestein-chirp", frm=["discrete-fourier-transform", "cyclic-convolution", "gaussian-resampling"],
    salient=r"The target permutation $Q$ is absorbed into the chirp and never executed.")

S10 = infer("S10",
    r"The retained source permutation $R$ cancels: $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$.",
    r"The second identity shows how the retained source permutation $R$ cancels when computing a convolution.",
    frm=["gaussian-resampling", "cyclic-convolution", "permutations"],
    salient="The permutation is never undone; it cancels between the two forward transforms and the opposite one.")

B = show("B",
    r"Cyclic convolution on distinct prime axes is computed from synthetic transforms over $\mathbb C[y]/(y^r+1)$, Gaussian resampling with retained permutations, and Bluestein chirps.",
    "evaluate the needed transforms as synthetic polynomial transforms on a layout where the fast layers apply, and connect them to the prime-length transforms by resampling and chirps",
    mot("In the polynomial-ring representation every transform step is an address rearrangement, a signed shift or a two-point butterfly, exactly the operations the two tape procedures accelerate.", "explicit",
        r"In this representation, the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations."),
    [S6, S7, S8, S9, S10],
    frm=["fast-fourier-transform", "polynomial-multiplication-via-evaluation-and-interpolation"])

# ---------------- Group C: assembly ----------------
S11 = infer("S11",
    r"A Chinese-remainder map $x\mapsto\prod_ix_i^{\mu_i}$ preserves cyclic convolution and is implemented by triangular controlled shifts and axis moves.",
    r"Hence $\Phi$ is an isomorphism and preserves cyclic convolution.",
    page="crt-address-map", frm=["chinese-remainder-theorem", "controlled-shifts", "fast-address-interchange", "cyclic-convolution"])

S12 = infer("S12",
    r"The twist $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ turns cyclic convolution in the last coordinate into negacyclic arithmetic in $\mathbb C[y]/(y^r+1)$.",
    r"Untwisting therefore recovers the cyclic coefficient with the correct sign.",
    page="coefficient-twist", frm=["polynomial-ring", "cyclic-convolution", "complex-numbers"],
    salient="The negative wrap of $y^r=-1$ reproduces exactly the positive cyclic wrap once the twist is removed.")

S13 = infer("S13",
    r"Splitting each input into radix-$2^b$ digits turns the product into a convolution of short coefficient lists, scaled into the disk and padded to $S$ records.",
    r"This produces the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order.",
    page="radix-digit-convolution", frm=["cyclic-convolution", "binary-representation-of-integers", "schoolbook-integer-arithmetic-with-carries"])

S14 = infer("S14",
    r"After removing the scales $S$ and $2^{2b+4}S$, the coefficient error is below $1/2$, so rounding gives the exact integers, and carry propagation yields the $2n$-bit product.",
    r"The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.",
    page="exact-recovery", frm=["radix-digit-convolution", "fixed-point-precision", "rounding-to-the-nearest-integer", "schoolbook-integer-arithmetic-with-carries"],
    salient=r"Although every transform is computed only approximately, the result is exact.")

S15 = infer("S15",
    r"With $\tau=\sigma=1-2^{-50}$, $\lambda'=1-2^{-54}$, $\epsilon=2^{-75}$, every normalized cost in the table is at most $p^{1-2\kappa}$, so the total time is $O(n(\lg n)^{1-\kappa})$.",
    r"Thus $\min_i g_i=2^{-181}=2\kappa$.",
    page="parameter-choice", frm=["fast-address-interchange", "simultaneous-butterfly-layer", "gaussian-resampling", "big-o", "logarithms-and-exponents"],
    salient=r"The binding margin is $g_2=\epsilon c(1-\tau)=2^{-181}$, from the chunk exchanges of the transform layout.")

C = show("C",
    r"The machine computes the exact $2n$-bit product of $n$-bit inputs in $O(n(\lg n)^{1-\kappa})$ time.",
    "place the radix-digit coefficients on prime axes, reduce to ring convolution by a twist, run the transforms, recover exact coefficients, and sum the normalized cost table under fixed parameters",
    mot("The known normalizations and an error strictly below 1/2 make rounding exact, and a compatible fixed choice of exponents puts every row of the cost table below the target power of p = Θ(log n).", "explicit",
        r"We choose compatible parameters for these procedures, recover the integer coefficients from their approximations, and account for the remaining tape operations."),
    [S11, S12, S13, S14, S15],
    frm=["multitape-turing-machine", "deterministic-algorithm-and-worst-case-running-time"],
    adds=[b("b", "digit width", r"The number of bits $\lceil\log_2 n\rceil$ in each radix digit.", "count"),
          b("S", "source box size", r"The product of the distinct prime source axis lengths.", "count")])

ROOTN = show("S0",
    r"A single deterministic fixed-alphabet multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.",
    "speed up address movement and butterfly arithmetic by recursive linear-network procedures, plug them into Harvey and van der Hoeven's reduction of multiplication to synthetic polynomial transforms, and bound the total cost",
    mot("Scanning Θ(n) bits at each of Θ(log n) transform levels already costs Θ(n log n), so beating n log n requires power savings in both data movement and arithmetic.", "explicit",
        r"Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$. We therefore need savings in both movement and arithmetic."),
    [A, B, C],
    page="main-theorem", frm=["nlogn-conjecture", "harvey-hoeven-multiplier", "multitape-turing-machine", "big-o"],
    salient=r"The bound beats $n\log n$ by a power $(\lg n)^{\kappa}$ of the logarithm, refuting the conjectured optimality, though $\kappa=2^{-182}$ is minute.",
    adds=[b(r"\tau", "interchange exponent", r"The fixed exponent $1-2^{-50}$ below one in the address-interchange cost.", "direct"),
          b(r"\lambda'", "layer exponent", r"The fixed exponent $1-2^{-54}$ below one in the butterfly-layer cost.", "direct")])

ans = {"root": ROOTN}

# verify quotes and order
norm = lambda s: re.sub(r'\s+', ' ', s)
NS = norm(SRC)
pos = -1
def walk(n):
    global pos
    if n["intention"] == "infer":
        q = norm(n["quote"]["quote"])
        i = NS.find(q)
        assert i >= 0, ("missing", n["id"], q)
        assert NS.count(q) == 1, ("dup", n["id"])
        if not n.get("deferred"):
            assert i > pos, ("order", n["id"])
            pos = i
    m = n.get("motivation")
    if m and m.get("quote"):
        assert norm(m["quote"]["quote"]) in NS, ("motq", n["id"])
    for c in n.get("children", []):
        walk(c)
walk(ROOTN)
json.dump(ans, open(os.path.join(ROOT, 'exegenius', 'tasks', '0003-argument.answer.json'), 'w'), ensure_ascii=False, indent=1)
print("ok")
