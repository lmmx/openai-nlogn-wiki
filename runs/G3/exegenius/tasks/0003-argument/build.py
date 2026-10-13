import json, sys
SRC = "/home/user/openai-nlogn-wiki/runs/G3/sources/paper.tex"
LINES = open(SRC, encoding="utf-8").read().split("\n")
TEXT = "\n".join(LINES)

def ev(line, sub=None):
    l = LINES[line - 1]
    if sub is None:
        sub = l.strip()
    assert sub in l, (line, sub, l)
    return {"source": "paper", "quote": sub}, line

POS = []  # (line, id) for infer quotes in DFS order

def infer(id, claim, line, sub=None, page=None, frm=(), salient=None):
    q, ln = ev(line, sub)
    POS.append((ln, id))
    n = {"id": id, "intention": "infer", "claim": claim, "quote": q}
    if page: n["page"] = page
    n["from"] = list(frm)
    if salient: n["salient"] = salient
    return n

def show(id, claim, method, mot, children, page=None, frm=(), salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": mot}
    if page: n["page"] = page
    n["from"] = list(frm)
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    n["children"] = children
    return n

def mot(text, source, line=None, sub=None):
    m = {"text": text, "source": source}
    if source == "explicit":
        q, _ = ev(line, sub)
        m["quote"] = q
    return m

def add(symbol, name, meaning, rel):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": rel}

# ---------------- S1: address interchange ----------------
s1_1 = infer("S1.1",
    "Splitting, merging, digit moves and row-wise stream splitting on a lexicographically stored array cost $O(V)$ steps for volume $V$ on a fixed number of tapes.",
    494, "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
    page="stream-scans",
    frm=["turing-machine", "time-and-bit-complexity-of-turing-machine-computation", "permutations-of-indices", "binary-representation-of-integers-and-radix-expansions"])

s1_2 = infer("S1.2",
    "Updating a target address field $y \\bmod q^b$ by an offset computed from earlier control fields, or multiplying it by a unit, costs $O(V)$ by splitting each fiber at the offset and merging the pieces swapped.",
    566, "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
    page="controlled-shifts",
    frm=["stream-scans", "modular-crt", "divisibility-gcd-and-coprime-integers"])

s1_3 = infer("S1.3",
    "A fixed network of pointwise linear gates over three-element subsets exchanges two data banks in three stages and returns every scratch wire to its arbitrary initial value.",
    730, "invocation changes $y_S$ to $y_S+x_S$ and leaves every other value",
    page="scratch-network",
    frm=["linear-maps-and-matrices", "bitwise-xor-and-hamming-weight", "integers-rationals-and-gaussian-integers"],
    salient="The exchange is exact for arbitrary initial scratch values: the net effect of the eight-row schedule does not depend on what the scratch wires held, because the first rows subtract exactly the contribution that the last rows restore.")

s1_4 = infer("S1.4",
    "Giving every wire at a gate the same invertible linear frame on its address-indexed array lets the pointwise linear gate commute with the frame, so only the endpoint frames determine the net operator and an edge only changes frames.",
    812, "Thus the common frame commutes with the pointwise gate, and",
    page="common-frame",
    frm=["linear-maps-and-matrices", "permutations-of-indices"])

s1_5_1 = infer("S1.5.1",
    "Every edge joins comparable nondegenerate labels and the only decreasing edges are the central-wire returns, so the sum of absolute dimension changes over edges is $Wm-2N+2L$ with $L<N/2$.",
    998, "Every edge joins comparable nondegenerate labels.")
s1_5_2 = infer("S1.5.2",
    "With rational projection matrices at gates and terminals, the bit network sends its input to the permutation $\\rho$ with endpoint difference $I_m$ on every role, and the sum $s$ of edge ranks is strictly less than $Wm$.",
    1139, "The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,")
s1_5 = show("S1.5",
    "Subspaces of an $m$-dimensional space attached to the gates and terminals, nested along edges, make the sum $s$ of edge ranks strictly less than the wire count $W$ times $m$.",
    "Attach tensor-product subspace labels built from triple indicator vectors, check that every edge is nested and only the central returns lose dimension, and convert dimension changes to ranks of projection differences.",
    mot("A nested label costs rank only where its dimension changes, so keeping the dimension lost on decreasing edges small is what keeps the total rank below the trivial bound.", "explicit", 853),
    [s1_5_1, s1_5_2], page="subspace-labels",
    frm=["linear-spaces", "common-frame", "scratch-network", "linear-maps-and-matrices"],
    salient="The rank sum falls short of $Wm$ by $N-2L>0$ because the decreasing edges lose only the fraction $L/N=100/539$ of the source dimension, which is below $1/2$; the whole speed-up rests on this strict deficit.")

s1_6_1 = infer("S1.6.1",
    "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation matrix with exactly $a$ ones.",
    1366, "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization")
s1_6_2 = infer("S1.6.2",
    "Conjugating by the triangular factors, which are controlled shifts of linear cost, leaves one field interchange per one in $\\Pi$, so the shear costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$.",
    1406, "can be performed with exactly $a$ interchanges of pairs of $b$-digit")
s1_6 = show("S1.6",
    "The address map $(H,D)\\mapsto(H+AD,D)$ for a rational matrix $A$ of rank $a$ is done with exactly $a$ interchanges of $b$-digit fields and $O(V)$ further work.",
    "Factor $A=E_1\\Pi E_2$ with lower triangular $E_1,E_2$, do the triangular parts as linear-cost controlled shifts, and spend one interchange per entry of $\\Pi$.",
    mot("Lower triangular coordinate changes update a later field from earlier ones, which is exactly the direction in which controlled shifts run in linear time.", "explicit", 1359, "can be performed entirely in this direction."),
    [s1_6_1, s1_6_2], page="matrix-shear",
    frm=["controlled-shifts", "modular-crt", "linear-maps-and-matrices", "permutations-of-indices"],
    salient="The cost of the shear is its rank $a$, not its size: the triangular factors are free, so only the pivots of the partial permutation cost recursive interchanges.")

s1_7 = infer("S1.7",
    "A call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$, so the normalized cost obeys $F_k\\le(s/W)F_{k-1}+O(1)$ and, because $s/W<m^\\tau$, grows like $m^{k\\tau}=O(e^\\tau)$ with $\\tau<1$.",
    1552, "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).",
    page="rank-saving-recurrence",
    frm=["subspace-labels", "common-frame", "stream-scans", "matrix-shear", "recurrences-induction-and-geometric-series"],
    salient="Without the strict inequality $s/W<m$ the cost would be $\\Theta(m^k)=\\Theta(e)$ per bit, no better than the naive interchange; the power saving $e^\\tau$ with $\\tau<1$ appears exactly because the ratio $s/W$ is slightly smaller than $m$.")

s1_8 = infer("S1.8",
    "Padding to power widths and enough rows, and handling the remaining widths in base $m$, extends the interchange to arbitrary equal widths $u$ in $O(Vu^\\tau)$ steps.",
    1643, "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.")

s1 = show("S1",
    "Two disjoint address chunks of $u$ bits each in an array of bit volume $V$ can be interchanged in $O(Vu^\\tau)$ time for a fixed $\\tau<1$, although the intermediate steps form XOR combinations of the data.",
    "Realize the shear $H\\leftarrow H+D$ by a fixed bit network of pointwise XOR gates with scratch wires and nested subspace labels, perform each edge by smaller interchanges on role streams, and solve the resulting recurrence.",
    mot("The saving comes from a strict rank inequality: each recursive call spends fewer than $m$ units of cost per wire, so the cost per bit grows as a power of the width below one.", "explicit", 175, "is the source of the power saving."),
    [s1_1, s1_2, s1_3, s1_4, s1_5, s1_6, s1_7, s1_8], page="address-interchange",
    frm=["stream-scans", "controlled-shifts", "scratch-network", "common-frame", "subspace-labels", "matrix-shear", "rank-saving-recurrence", "permutations-of-indices", "bitwise-xor-and-hamming-weight"],
    salient="The interchange is an exact permutation yet costs only $O(Vu^\\tau)$ with $\\tau=1-2^{-50}$ because intermediate streams hold XOR combinations of data rather than moved copies; the final result is exact for arbitrary scratch contents.",
    adds=[add("s", "edge rank sum", "the total of the ranks of all edge matrices of the network, equal to the number of smaller interchange calls one call makes", "count"),
          add("W", "wire count", "the number of wires of the network, including scratch wires, equal to the number of role streams a call splits into", "count"),
          add("m", "label dimension", "the dimension of the label space, equal to the number of address fields a chunk is divided into", "count")])

# ---------------- S2: butterfly layer ----------------
s2_1 = infer("S2.1",
    "Over binary labels the phase frames $\\mathcal C_U$ turn each edge into a product of translation kernels $aI+bX_v$ built from $C=H\\mathsf SH$, and $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$ returns from a $C$ layer to the normalized butterfly layer.",
    1930, "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.",
    page="phase-frames",
    frm=["subspace-labels", "common-frame", "complex-numbers", "euler-s-formula-and-complex-exponentials", "bitwise-xor-and-hamming-weight"],
    salient="The kernel $C=aI+bX$ is a square root of the bit flip ($C^2=X$, $C^4=I$) and $H_0=b\\mathsf SC\\mathsf S$, which is why every edge residual vector contributes exactly one translation kernel and a $C$ layer converts to a butterfly layer by diagonal phases alone.")

s2_2_1 = infer("S2.2.1",
    "Eight conditional additions of a control bit to two integers act on every square of parities as two three-cycles, which together flip the parity of $u$ exactly when $c=1$ and restore the auxiliary integer $w$.",
    2032, "If $c=0$, these operations do nothing. If $c=1$, the first four operations")
s2_2_2 = infer("S2.2.2",
    "The addresses where a guard value leaves its safe interval form a set $\\mathcal B$ with $|\\mathcal B|\\le\\delta_{\\rm bad}M$, independently of the record payload, and off $\\mathcal B$ the packed shifts agree with the ideal XORs.",
    2102, "|\\mathcal B|\\le\\delta_{\\rm bad}M.")
s2_2_3 = infer("S2.2.3",
    "Each shift is a chunk interchange costing $O(VL^\\tau)$, and the permutation that repairs the small set $\\mathcal B$ is applied by sorting only the exceptional records, so the total time is $O(V(L^\\tau+1))$.",
    2130, "descriptor has $O(A_{\\rm rect})$ bits. The swap costs $O(VL^\\tau)$, including")
s2_2 = show("S2.2",
    "A binary row addition $y_j\\leftarrow y_j\\oplus x_j$ on the same bit position of several address chunks is done by a constant number of whole-chunk cyclic shifts plus a deterministic repair of a small exceptional address set, in $O(V(L^\\tau+1))$ time.",
    "Simulate the XORs of all chunks at once by eight packed cyclic shifts that are correct away from a small bad set of addresses, then repair exactly that set.",
    mot("The repair set depends only on addresses, so the bound is a worst-case bound over all payloads.", "explicit", 1949, "The correction depends only on addresses, so the time bound is"),
    [s2_2_1, s2_2_2, s2_2_3], page="packed-bit-addition",
    frm=["address-interchange", "controlled-shifts", "stream-scans", "bitwise-xor-and-hamming-weight"],
    salient="Cyclic shifts of packed fields reproduce XOR on all but a fraction $O(f2^{-K})$ of addresses, and that fraction does not depend on the data at all.")

s2_3 = infer("S2.3",
    "Applying the complex network with column frames to a group of $e$ selected axes reduces it to $s_{\\rm c}$ child layers on $e/m$ axes, each on $1/W_{\\rm c}$ of the parent's volume.",
    2691, "The phase-frame construction reduces a group of $e$ selected bits to")
s2_4 = infer("S2.4",
    "Together with the packed basis changes, the row construction and the recurrence give total time $O(Vd^{\\lambda'})$ on fixed tapes, with intermediate values exact and one final truncation of error below $\\sqrt2\\,2^{-p}$.",
    2737, "above give total time $O(Vd^{\\lambda'})$ on fixed tapes, including")

s2 = show("S2",
    "The two-point butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied at one common bit position of each of $D\\le d$ address chunks of polynomial records costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, with exact intermediate values and a single truncation.",
    "Express the layer through the kernel $C$, evaluate the $C$ layer by the complex network with phase frames so that each edge is a smaller layer on $e/m$ axes, implement the binary basis changes by packed additions, and convert back to $H_0$.",
    mot("Doing the $D$ butterflies one axis at a time takes $D$ whole-array passes, which is the cost to be beaten.", "explicit", 1794),
    [s2_1, s2_2, s2_3, s2_4], page="butterfly-layer",
    frm=["phase-frames", "packed-bit-addition", "rank-saving-recurrence", "address-interchange", "fixed-point-grid", "contraction-error", "complex-numbers"],
    salient="All $D$ butterflies cost $O(Vd^{\\lambda'})$, strictly less than the $D$ passes of cost $O(V)$ each that separate butterflies would need, again because the strict rank saving $s_{\\rm c}<W_{\\rm c}m$ is inherited by the recursion.",
    adds=[add("e", "group size", "the number of selected axis chunks handled by one call of the layer procedure", "count")])

# ---------------- S3: synthetic convolution ----------------
s3_1 = infer("S3.1",
    "The synthetic transforms $F_t^\\pm$ over $\\mathbb C[y]/(y^r+1)$ use the roots $\\omega_t=y^{2r/t}$, so multiplication by a root is a free signed shift, and their character sums cancel to give $F_t^+F_t^-=I/t$.",
    2816, "F_t^+F_t^-=t^{-1}I.",
    page="synthetic-transforms",
    frm=["negacyclic-ring", "dft-convolution", "multidim-transform", "vector-norms-and-the-triangle-inequality"],
    salient="Character sums vanish although the ring has zero divisors: shifting the summation index by $t/2^{v+1}$ multiplies the sum by $y^{r j_0}=-1$, and the additive group has no two-torsion.")
s3_2 = infer("S3.2",
    "The decimation-in-frequency recursion applies $H_0$ and a twiddle shift at each level, writing the outputs in bit-reversed order $B_tF_t^-$ that the opposite transform $F_t^+B_t^{-1}$ consumes directly.",
    2867, "entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$.",
    page="butterfly-order",
    frm=["synthetic-transforms", "bitwise-xor-and-hamming-weight", "permutations-of-indices"],
    salient="The stored order is bit-reversed and never undone: the opposite transform runs the recursion backwards on that order, so no permutation of whole frequency indices is ever executed.")
s3_3 = infer("S3.3",
    "A positional layout permutation $L$ of record addresses puts the selected bits of all participating axes at a common offset in consecutive $K$-bit chunks, so each transform round is one simultaneous butterfly layer and a transform costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
    2983, "O\\left(Tp\\left[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}\\right]\\right).",
    page="transform-layout",
    frm=["synthetic-transforms", "butterfly-order", "butterfly-layer", "address-interchange", "stream-scans"])
s3_4 = infer("S3.4",
    "Two disk-grid polynomials in the negacyclic ring multiply exactly by evaluating at $2^{4p}$, multiplying the resulting integers with the established multiplier and extracting signed coefficients, in $O(rp\\log(rp))$ time.",
    3260, "|h_j|\\leq r2^{2p}<2^{3p}<B_0/2.",
    page="signed-packing",
    frm=["negacyclic-ring", "radix-convolution", "binary-representation-of-integers-and-radix-expansions", "schoolbook-arithmetic-and-carries"],
    salient="Every product coefficient is below $2^{3p}$, less than half the base $2^{4p}$, so signed coefficients are separated by their centered residues and negative values cause no ambiguity.")
s3_5 = infer("S3.5",
    "Performing both forward transforms, retaining their common $LB$ order, multiplying the $M$ polynomial records pointwise by signed packing and applying the opposite transform gives the normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
    3415, "Perform both forward transforms and retain their common $LB$ order.")
s3 = show("S3",
    "The normalized cyclic convolution of arrays of polynomials over $\\mathbb C[y]/(y^r+1)$ on power-of-two axes is computed from the retained transform layout in time $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
    "Compute two forward synthetic transforms on a layout where every round is a simultaneous butterfly layer, multiply the transformed records pointwise by signed packing in the stored frequency order, and apply the opposite transform.",
    mot("Pointwise multiplication commutes with applying the same record permutation to both operands, so the frequency order produced by the forward transforms can be kept and passed straight to the opposite transform.", "explicit", 3202),
    [s3_1, s3_2, s3_3, s3_4, s3_5], page="synthetic-convolution",
    frm=["transform-layout", "signed-packing", "synthetic-transforms", "butterfly-order", "contraction-error", "negacyclic-ring"],
    salient="The convolution never sorts: the frequency order left by the forward transforms is the order the opposite transform needs, so the permutation $LB$ cancels through the pointwise product.",
    adds=[add("r", "ring size", "the number of complex coefficients in a ring element, a power of two", "count"),
          add("M", "record count", "the number of polynomial records on the axes being convolved, equal to $T/r$", "count")])

# ---------------- S4: Gaussian resampling ----------------
s4_1 = infer("S4.1",
    "For coprime $s<t$ with $t/s-1>p/\\alpha^4$ there are contractions $A$ and $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, computable with error below $p^2$ in $O(tp^{3/2+\\delta}\\alpha)$ time.",
    3562, "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA.")
s4_2 = infer("S4.2",
    "Tensoring over $d$ axes and applying the maps one coordinate line at a time gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with line cost $O(dTp^{3/2+\\delta}\\alpha)$ plus the cost of exposing the lines.",
    3822, "$O(dTp^{3/2+\\delta}\\alpha)$, with a constant independent of $d$.")
s4_3 = infer("S4.3",
    "Multiplying by the chirp $\\overline a$ before and after a cyclic convolution with the chirp $a$ gives $QF_{\\boldsymbol t}u$, so the middle transform with its permutation becomes a convolution.",
    3923, "\\frac{a*(\\overline a\\mathbin{\\cdot}u)}{T}.",
    page="chirp-identity",
    frm=["dft-convolution", "multidim-transform", "euler-s-formula-and-complex-exponentials"],
    salient="The quadratic phase $a_j=\\exp(-\\pi i s j^2/t)$ turns $e^{2\\pi i s jk/t}$ into $\\overline a_j a_{j-k}\\overline a_k$, so the frequency scaling by $-s$ inside $Q$ is absorbed without applying the permutation $Q$.")
s4_4 = infer("S4.4",
    "The source permutation $R$ retained in the transform cancels across the two forward transforms, their pointwise product and the opposite-sign transform, so $(RF^+_{\\boldsymbol s})[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=u*v/S^2$.",
    3931, "=\\frac{u*v}{S^2}.",
    page="permutation-cancel",
    frm=["gaussian-resampling", "chirp-identity", "dft-convolution", "multidim-transform", "permutations-of-indices", "modular-crt", "divisibility-gcd-and-coprime-integers"],
    salient="The result is the plain normalized convolution $u*v/S^2$ with no trace of $R$, because $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$ and a coordinate permutation commutes with pointwise products.")
s4 = show("S4",
    "A Fourier transform on axes of pairwise coprime prime lengths $s_i$ equals, up to the scale $2^\\gamma$, a power-of-two transform sandwiched between Gaussian contractions, $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, with the coordinate permutations kept inside the formula.",
    "Prove the one-dimensional Gaussian resampling identity, tensor it over the axes, turn the middle transform into a convolution by the chirp identity, and show that the retained source permutation cancels in a convolution.",
    mot("The usual implementation of Gaussian resampling sorts twice on each coordinate, which is too expensive, so both permutations are left inside the transform formula and computed implicitly.", "explicit", 3501),
    [s4_1, s4_2, s4_3, s4_4], page="gaussian-resampling",
    frm=["multidim-transform", "dft-convolution", "address-interchange", "contraction-error", "euler-s-formula-and-complex-exponentials"],
    salient="Both coordinate permutations stay inside the identity and the source one disappears again after the pointwise product, so the sorts that normally accompany Gaussian resampling are never run.")

# ---------------- S5: algorithm ----------------
s5_1_1 = infer("S5.1.1",
    "Precision $p=6b$, axis count $d=\\lfloor b^\\epsilon\\rfloor$, chunk width $K=\\lfloor d^c\\rfloor$ and padded box $T\\in[4n/b,8n/b)$ with ring size $r$ give $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$ and $r=2^{\\Theta(p^{1-\\epsilon})}$.",
    4055, "b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,")
s5_1_2 = infer("S5.1.2",
    "Distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ exist below each power-of-two axis length $t_i$ and can be found by trial division in $n^{o(1)}$ time.",
    4135, "(1-2\\eta)t_i<s_i\\leq(1-\\eta)t_i.")
s5_1_3 = infer("S5.1.3",
    "With $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$ every ratio satisfies $\\alpha^4\\theta_i>p$ and $T/2<S<T$, so the hypotheses of the resampling lemma hold for all large $n$.",
    4149, "\\alpha^4\\theta_i>\\frac{12d^2b}{4d}=3db\\geq6b=p.")
s5_1 = show("S5.1",
    "The padded box size $T$, precision $p=6b$, number of axes $d$, chunk width $K$, ring size $r$ and distinct odd primes $s_i$ just below the power-of-two axis lengths $t_i$ can be chosen so that the resampling and layer hypotheses hold.",
    "Fix rational exponents once, derive all sizes from $b=\\lceil\\log_2 n\\rceil$, choose the primes in disjoint intervals just below the axis lengths, and verify the separation needed for resampling.",
    mot("The prime lengths must be close to the powers of two so that their product fills a fixed fraction of the padded box, while the ratios $t_i/s_i$ must leave enough separation for Gaussian resampling.", "explicit", 4105),
    [s5_1_1, s5_1_2, s5_1_3], page="parameter-choice",
    frm=["gaussian-resampling", "synthetic-convolution", "transform-layout", "butterfly-layer", "prime-numbers-and-primality-testing-by-trial-division", "floor-ceiling-rounding-and-logarithms"],
    salient="The primes are chosen just below the powers of two, within a factor $1-1/(2d)$, so the product $S$ exceeds $T/2$ (padding wastes less than half the box) while each ratio $t_i/s_i$ still exceeds $1+1/(4d)$, which is exactly what the resampling bound $\\alpha^4\\theta>p$ requires.")

s5_2 = infer("S5.2",
    "Writing each $n$-bit input in radix $2^b$ gives digit polynomials of $q=\\lceil n/b\\rceil$ digits whose product has degree below $S$ and coefficients below $2^{3b}$, so the integer product is a cyclic convolution of digit lists followed by carry propagation.",
    4191, "0\\le c_j\\le q(2^b-1)^2<2^{3b},",
    page="radix-convolution",
    frm=["binary-representation-of-integers-and-radix-expansions", "schoolbook-arithmetic-and-carries", "fast-fourier-transform-and-the-convolution-theorem", "polynomials"],
    salient="Choosing the digit width $b=\\lceil\\log_2 n\\rceil$ keeps the coefficients below $2^{3b}$, polylogarithmically many bits, so each convolution coefficient fits in the working precision $p=6b$ with room for rounding.")

s5_3_1 = infer("S5.3.1",
    "The assignment $x\\mapsto\\prod_i x_i^{\\mu_i}$ with $\\mu_i=P_i^{-1}\\bmod s_i$ is an algebra isomorphism from $\\mathbb C[x]/(x^S-1)$ onto the product of cyclic axes and preserves cyclic convolution.",
    4220, "$\\Phi$ is an isomorphism and preserves cyclic convolution.")
s5_3_2 = infer("S5.3.2",
    "The induced address change $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j \\bmod s_i$ is a sequence of triangular prefix-controlled cyclic shifts, so padding and reordering cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
    4273, "Each triangular update is a prefix-controlled cyclic shift.")
s5_3 = show("S5.3",
    "A ring isomorphism $x\\mapsto\\prod_i x_i^{\\mu_i}$ places a length-$S$ cyclic coefficient list on a product of cyclic axes of pairwise coprime prime lengths, preserving convolution, and the induced address change is a sequence of triangular controlled shifts.",
    "Define the Chinese-remainder algebra map, prove it is a bijection on monomials, and implement its address change coordinate by coordinate with controlled shifts.",
    mot("The coordinate powers $\\mu_i$ are chosen so that the change of order becomes a sequence of controlled cyclic shifts, which are linear-time operations.", "explicit", 4202),
    [s5_3_1, s5_3_2], page="crt-prime-axes",
    frm=["modular-crt", "controlled-shifts", "radix-convolution", "multidim-transform", "divisibility-gcd-and-coprime-integers"],
    salient="Coordinate $i$ of the new address depends only on the lower-index digits, because terms with $j>i$ are divisible by $s_i$ and $\\mu_iP_i=1$ modulo $s_i$; this triangular shape is what makes the reordering a controlled shift.")

s5_4 = infer("S5.4",
    "Multiplying coefficient $k$ of the last cyclic axis by $e^{\\pi ik/r}$ turns a length-$r$ cyclic coordinate into a polynomial modulo $y^r+1$, and the negative wrap becomes the correct cyclic wrap after untwisting.",
    4319, "Untwisting therefore recovers the cyclic coefficient with the correct",
    page="phase-twist",
    frm=["negacyclic-ring", "synthetic-convolution", "euler-s-formula-and-complex-exponentials", "dft-convolution"],
    salient="The wrap sign $(-1)^h$ of the negacyclic product is cancelled exactly by the twist factor $(\\zeta^r)^h=(-1)^h$, so the cyclic coefficient is recovered with no sign error.")
s5_5 = infer("S5.5",
    "The source transform applies the Gaussian expansion $\\mathcal A$, the chirp transform, the compression $\\mathcal B_0$ and the exact scale $2^\\gamma$ to a tensor on the padded box, and has exact counterpart $RF_{\\boldsymbol s}$.",
    4457, "$\\widetilde{\\mathscr F}$ for the following procedure: apply the linewise")
s5_6 = infer("S5.6",
    "The algorithm applies the address map, the source transform to both inputs, a pointwise product, the opposite transform, the two rescalings by $S$ and $2^{2b+4}$, rounding, the inverse address map and carry propagation, and the two factors $S$ undo different normalizations.",
    4536, "The two occurrences of $S$ in this algorithm undo different",
    salient="The factor $S$ is applied twice for different reasons: the first cancels the $1/S^2$ left by the three normalized transforms, the second reverses the $1/S$ normalization of the digit convolution.")

e1 = infer("S5.7.1",
    "The error of a normalized ring convolution, a complex convolution and a chirp transform is less than $5TL$, $6TL$ and $8TL$ units of $2^{-p}$ respectively, where $L=\\log_2T$.",
    4617, "<(E_{\\rm ring}+4+4+4)h_p<6TLh_p.")
e2 = infer("S5.7.2",
    "The source transform has error less than $E_s 2^{-p}$ with $E_s=9\\,2^\\gamma TL$ and keeps all values in the unit disk.",
    4652, "E_s=9\\,2^\\gamma TL,")
e3 = infer("S5.7.3",
    "After the second pointwise product and the opposite transform, the scaled array $\\widetilde w$ approximates $(u*v)/S$ with error less than $E_w 2^{-p}$, where $E_w<28\\,2^\\gamma T^2L$.",
    4709, "E_w:=S(3E_s+2)<28\\,2^\\gamma T^2L.")
e4 = infer("S5.7.4",
    "After the final scaling by $2^{2b+4}S$ the absolute error on every coefficient is less than $448b\\,2^{-3b/4}<1/2$.",
    4726, "\\le448b\\,2^{-3b/4}<\\frac12.")
e5 = infer("S5.7.5",
    "Radix-$2^b$ carry propagation with carries below $2^{2b}$ yields the product bits, and the product is less than $2^{2n}$, so exactly $2n$ bits are output.",
    4803, "than $2^{2n}$; all bits above position $2n-1$ are therefore zero.")
s5_7 = show("S5.7",
    "The accumulated numerical error on every recovered coefficient is below $1/2$, so rounding gives the exact integer convolution coefficients and radix-$2^b$ carry propagation yields the $2n$-bit product.",
    "Follow the norm and the error of the computed arrays through every step using contraction and bilinear-contraction bounds, then bound the error after the final rescaling and round.",
    mot("An error strictly below $1/2$ makes the nearest integer the unique correct coefficient, since the true coefficients are integers.", "explicit", 4730, "The strict error below $1/2$ makes the nearest integer to"),
    [e1, e2, e3, e4, e5], page="exact-recovery",
    frm=["contraction-error", "fixed-point-grid", "permutation-cancel", "parameter-choice", "radix-convolution", "schoolbook-arithmetic-and-carries", "floor-ceiling-rounding-and-logarithms"],
    salient="The error stays below $1/2$ even after amplification by $2^\\gamma$, $S$ and $2^{2b+4}$, because the working precision $p=6b$ leaves a factor $2^{-6b}$ against a total amplification of only about $2^{2b+\\gamma}T^2L$ with $\\gamma=o(b)$.")

s5 = show("S5",
    "The algorithm converts the inputs to radix-$2^b$ digit lists, maps them by the Chinese-remainder address map, applies the resampled chirp source transform to each, multiplies pointwise, applies the opposite transform, rescales, rounds, undoes the address map and propagates carries, giving the exact $2n$-bit product.",
    "Choose the parameters, express the product as a cyclic convolution of digit lists on prime axes, evaluate that convolution through resampling, the chirp identity and the ring convolution after a phase twist, then recover exact integers by rounding and carries.",
    mot("The three transforms needed for the radix-digit convolution are now available as procedures, so the product can be assembled from them.", "explicit", 4488),
    [s5_1, s5_2, s5_3, s5_4, s5_5, s5_6, s5_7], page="multiplication-algorithm",
    frm=["parameter-choice", "radix-convolution", "crt-prime-axes", "phase-twist", "gaussian-resampling", "chirp-identity", "permutation-cancel", "synthetic-convolution", "address-interchange"],
    adds=[add("b", "digit width", "the number of bits in one radix digit, $b=\\lceil\\log_2 n\\rceil$", "count"),
          add("S", "cyclic length", "the product of the distinct prime axis lengths $s_i$, the length of the digit convolution", "count")])

# ---------------- S6: cost ----------------
c1 = infer("S6.1",
    "The seven dominant margins below one are $g_1>1/2$, $g_2=\\epsilon c(1-\\tau)=2^{-181}$, $g_3=\\epsilon(1-\\lambda')=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$ and $g_7=\\epsilon=2^{-75}$.",
    4851, "g_1>\\frac12,\\quad g_2=2^{-181},\\quad g_3=2^{-129},\\quad")
c2 = infer("S6.2",
    "The smallest margin is $\\min_i g_i=2^{-181}=2\\kappa$, so every dominant power of $p$ is at most $1-2\\kappa$, and the exponents $\\epsilon$ and $c$ are fixed small rational numbers.",
    4854, "Thus $\\min_i g_i=2^{-181}=2\\kappa$.")
c3 = infer("S6.3",
    "Global setup, prime search and the finitely many small lengths cost $o(V)$ or are absorbed in the constant.",
    4980, "alphabet symbols.  Global setup and prime search cost $o(V)$, as")
c4 = infer("S6.4",
    "Any fixed power of $\\log p$ is at most $p^\\kappa$ eventually, so the total time is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
    4987, "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa}).")
c5 = infer("S6.5",
    "Using schoolbook multiplication below a fixed cutoff gives one fixed-alphabet, fixed-tape deterministic machine with worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every input length.",
    4993, "fixed-alphabet, fixed-tape deterministic machine has worst-case time")
s6 = show("S6",
    "Dividing every step's cost by the volume $Tp$ gives seven dominant powers of $p$, each at most $1-2\\kappa$, which with $\\kappa=2^{-182}$ yields total time $O(n(\\lg n)^{1-\\kappa})$.",
    "Tabulate the cost of each operation divided by $Tp$ as a power of $p$, compare the seven dominant exponents with one, and absorb setup and polylogarithmic factors into the margin.",
    mot("Every operation acts on arrays of $\\Theta(Tp)$ bits with $O(p)$ bits per coefficient, so normalizing by $Tp$ puts all costs on the common scale of powers of $p=\\Theta(\\log n)$ and the saving is read off from exponents below one.", "recoverable"),
    [c1, c2, c3, c4, c5], page="cost-table",
    frm=["transform-layout", "synthetic-convolution", "address-interchange", "butterfly-layer", "gaussian-resampling", "parameter-choice", "rank-saving-recurrence", "exact-recovery", "crt-prime-axes"],
    salient="The exponent $\\kappa=2^{-182}$ is half of the smallest of the seven margins, $g_2=\\epsilon c(1-\\tau)=2^{-75}\\cdot2^{-56}\\cdot2^{-50}=2^{-181}$ coming from the chunk exchanges of the transform layout; the savings are minuscule but strictly positive.",
    adds=[add("\\epsilon", "axis exponent", "the fixed exponent for which the number of axes is $d=\\Theta(p^\\epsilon)$", "direct"),
          add("c", "chunk exponent", "the fixed exponent for which the chunk width is $K=\\lfloor d^c\\rfloor$", "direct")])

root = show("S0",
    "A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$, refuting the $n\\log n$ optimality conjecture in this model.",
    "Reduce the product to a cyclic convolution of radix digits, evaluate it with Fourier-type transforms whose data movement and butterfly layers are accelerated by two power-saving tape procedures, recover the exact integers by rounding and carries, and add up the costs.",
    mot("Scanning the whole array at each of the $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so savings are needed in both data movement and arithmetic, which the two tape procedures supply.", "explicit", 92, "We therefore need savings in both movement and arithmetic."),
    [s1, s2, s3, s4, s5, s6], page="main-theorem",
    frm=["mult-history", "big-o", "turing-machine", "time-and-bit-complexity-of-turing-machine-computation"],
    salient="The logarithmic factor is lowered by a genuine power $(\\lg n)^{-\\kappa}$, but with the astronomically small exponent $\\kappa=2^{-182}$, on one fixed finite-tape machine that is exact for every input length.",
    adds=[add("V", "bit volume", "the number of bits stored in the array a tape procedure acts on", "count"),
          add("p", "working precision", "the number of fractional bits kept in every fixed-point complex value, $p=6\\lceil\\log_2 n\\rceil$", "count"),
          add("T", "padded box size", "the number of entries of the padded power-of-two array of transform coordinates, with $Tp=\\Theta(n)$", "count")])

# order check
lines = [l for l, _ in POS]
for (a, ia), (b, ib) in zip(POS, POS[1:]):
    if not a < b:
        print("ORDER VIOLATION", ia, a, ib, b, file=sys.stderr)
# page uniqueness
pages = []
def walk(n):
    if n.get("page"): pages.append(n["page"])
    for c in n.get("children", []): walk(c)
walk(root)
assert len(pages) == len(set(pages)), [p for p in pages if pages.count(p) > 1]
print(len(pages), "pages", file=sys.stderr)
json.dump({"root": root}, open("/home/user/openai-nlogn-wiki/runs/G3/exegenius/tasks/0003-argument.answer.json", "w"), indent=1, ensure_ascii=False)
