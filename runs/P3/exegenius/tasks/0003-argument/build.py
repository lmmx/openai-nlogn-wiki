import json, sys

SRC = open('/home/user/openai-nlogn-wiki/runs/P3/sources/paper.tex').read()

ORDER = """history stream-ops controlled-shift linear-algebra linear-network frames subset-gadget rank-saving
bit-network-shear complex-phase-network triangular-factorization matrix-shear power-width-interchange
chunk-interchange packed-bit-addition ring-mod-yr fixed-point signed-packing dft butterfly-fft
phase-frame-reduction simultaneous-layer contraction-error convolution multidim-transform synthetic-transform
crt-map bluestein phase-twist transform-layout ring-convolution gaussian-resampling retained-permutations
integer-as-convolution exact-recovery parameters complex-convolution-twist source-transform
multiplication-algorithm cost-accounting main-theorem""".split()

KNOWN = """big-o polynomials complex-numbers multitape-tm binary-representation-of-integers modular-arithmetic
primes-divisibility-coprimality-and-gcd logarithms-floors-and-ceilings divide-and-conquer-and-recurrences
sorting-merging-and-radix-sort schoolbook-multiplication-and-carries permutations
sets-subsets-and-binomial-coefficients xor-and-mod-2-arithmetic hamming-weight
matrices-and-matrix-vector-products vector-norms-and-the-triangle-inequality
lexicographic-order-and-mixed-radix-indexing two-s-complement-and-signed-integers
dyadic-and-rational-numbers euler-s-formula-and-complex-conjugation tape-based-subroutines-and-stacks
constant-factors-versus-asymptotic-dominance""".split()


def Q(q):
    return {"source": "paper", "quote": q}


def mot(text, source, quote=None):
    return {"text": text, "source": source, "quote": Q(quote) if quote else None}


def infer(id, claim, quote, page=None, frm=None, salient=None, adds=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": Q(quote), "from": frm or []}
    if page:
        n["page"] = page
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = adds
    return n


def show(id, claim, method, motivation, children, page=None, frm=None, salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": motivation,
         "children": children, "from": frm or []}
    if page:
        n["page"] = page
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = adds
    return n


def b(symbol, name, meaning, relation="count"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


# ---------------------------------------------------------------- common ingredients
net = show(
    "G.3", r"Two fixed linear networks on $W$ wires with a rank saving exist: they exchange two banks of values, restore every scratch wire, and give each wire's array a frame whose edge changes have total rank $s<Wm$.",
    "build the scalar exchange network, then put frames and nested subspace labels on it, once for bits and once for complex phases",
    mot("The representation (frame) of each wire's array must change cheaply along edges; the invariant is explained first, then the labels that make the changes cheap.", "explicit",
        "before constructing the subspace labels that make changes of representation"),
    [
        infer("G.3.1", r"A fixed network of linear gates on $W$ scalar wires, run on a schedule whose first rows cancel the old scratch values and last rows restore them, adds a source bank into a target bank whatever the arbitrary initial scratch values are.",
              "the following schedule remove the effect of the old scratch values;", page="linear-network",
              frm=["matrices-and-matrix-vector-products", "xor-and-mod-2-arithmetic"]),
        infer("G.3.2", r"With gather and scatter over three-element subsets of a ground set, and side wires cancelling the unwanted intersection-size coefficients, three stages realize $(X_a,Y_a)\mapsto(-Y_a,X_a)$ and restore every scratch wire.",
              r"(X_a,Y_a)\longmapsto(-Y_a,X_a)", page="subset-gadget",
              frm=["linear-network", "sets-subsets-and-binomial-coefficients", "xor-and-mod-2-arithmetic"],
              salient="The net map is independent of the arbitrary initial contents of the scratch wires, and a map built only from additions into targets still produces an exact signed exchange."),
        infer("G.3.3", r"If each wire's array is stored as $D_vg$ for a frame $D_v$ common to all incidences of a gate, pointwise linear gates commute with the frame and the network implements $D_{\rm out}\mathsf S D_{\rm in}^{-1}$, with edge cost $D_vD_u^{-1}$.",
              "Thus the common frame commutes with the pointwise gate, and", page="frames",
              frm=["linear-network", "matrices-and-matrix-vector-products"]),
        infer("G.3.4", r"Attaching nested nondegenerate subspaces of an $m$-dimensional space to the gates makes the sum $s$ of the edge-difference ranks strictly smaller than $Wm$.",
              "Every edge joins comparable nondegenerate labels.", page="rank-saving",
              frm=["linear-algebra", "subset-gadget", "frames", "sets-subsets-and-binomial-coefficients"],
              salient="The total rank is strictly below the trivial bound $Wm$ (each edge could cost up to $m$), although only by a tiny relative amount; this strict deficit is the whole source of the power saving."),
        infer("G.3.5", r"For the bit network the edge matrices $P_V-P_U$ have rank $\dim V-\dim U$ and the endpoint difference is $I_m$ on every role, so frames $\Phi_M$ make every role undergo the shear $(H,D)\mapsto(H+D,D)$ with total rank $s<Wm$.",
              r"M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m", page="bit-network-shear",
              frm=["rank-saving", "frames", "linear-network", "subset-gadget", "linear-algebra", "xor-and-mod-2-arithmetic"],
              salient="Every role, including scratch roles carrying arbitrary values, undergoes the same shear, although the scalar network merely exchanges banks."),
        infer("G.3.6", r"For the complex network with binary labels and phase frames $\mathcal C_U$, each edge difference is a product of two-point kernels $aI+bX_v$, their total number is $s_{\rm c}<W_{\rm c}m$, and telescoping gives $C^{\otimes m}$ on every role.",
              r"telescoping these phase frames gives $C^{\otimes m}$", page="complex-phase-network",
              frm=["rank-saving", "frames", "linear-network", "subset-gadget", "linear-algebra", "hamming-weight",
                   "complex-numbers", "euler-s-formula-and-complex-conjugation", "xor-and-mod-2-arithmetic"]),
    ],
    adds=[b("W", "wire count", "The number of scalar wires of the network, including scratch wires."),
          b("m", "label dimension", "The dimension of the space whose subspaces label the gates."),
          b("s", "total edge rank", "The sum over all edges of the rank of the matrix difference across the edge, i.e. the number of smaller calls.")],
)

common = show(
    "G", r"The two fast procedures rest on elementary linear-time scans on tape and on two finite linear networks with a rank saving.",
    "state the elementary tape scans and the finite networks that both fast tape procedures reuse",
    mot("Both procedures arise from their own fixed linear network and use the same linear-cost scans, so these are established once before either procedure.", "explicit",
        "Each procedure arises from its own fixed linear network that exchanges two"),
    [
        infer("G.1", r"Splitting an array on a digit, merging, moving a digit and cyclically splitting whole rows into $W$ streams each cost $O(V)$ on a fixed number of tapes.",
              r"volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:", page="stream-ops",
              frm=["multitape-tm", "lexicographic-order-and-mixed-radix-indexing", "sorting-merging-and-radix-sort",
                   "tape-based-subroutines-and-stacks", "permutations"]),
        infer("G.2", r"Updating a later address field $y$ by $y+a(\text{controls})$ modulo $q^b$, or multiplying it by a fixed rational unit, costs $O(V)$ by splitting each fibre in two pieces and merging them in swapped order.",
              r"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the", page="controlled-shift",
              frm=["stream-ops", "modular-arithmetic", "dyadic-and-rational-numbers", "primes-divisibility-coprimality-and-gcd"]),
        net,
    ],
    frm=["multitape-tm", "tape-based-subroutines-and-stacks"],
)

# ---------------------------------------------------------------- fast address interchange
matrix_shear = show(
    "S1.1.1", r"The shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ for a rank-$a$ rational matrix $A$ takes exactly $a$ interchanges of $b$-digit fields plus $O(V)$ work.",
    "factor $A$ into lower-triangular pieces and a partial permutation, so the triangular parts become controlled shifts and each pivot costs one interchange",
    mot("Controlled shifts update a later field from earlier ones in linear time, so only changes of coordinates that are lower triangular in tape order are cheap; the factorization puts the whole rank into the partial permutation.", "explicit",
        "can be performed entirely in this direction."),
    [
        infer("S1.1.1.1", r"Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with exactly $a$ ones.",
              r"A=E_1\Pi E_2,", page="triangular-factorization",
              frm=["matrices-and-matrix-vector-products", "permutations"]),
        infer("S1.1.1.2", r"Transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$ using one interchange per one of $\Pi$ between two controlled updates, and undo the triangular changes; this uses exactly $a$ interchanges and $O(V)$ further work.",
              r"can be performed with exactly $a$ interchanges of pairs of $b$-digit",
              frm=["controlled-shift", "triangular-factorization", "modular-arithmetic"]),
    ],
    page="matrix-shear",
    frm=["controlled-shift", "matrices-and-matrix-vector-products"],
)

power = show(
    "S1.1", r"For $e=m^k$, two disjoint chunks of $e$ radix-$q$ digits can be interchanged in $O(Ve^\tau)$ time when the row field is divisible by $W^k$, where $\tau<1$ satisfies $s/W<m^\tau$.",
    "run the bit network on $W$ row-split role streams with each edge done as a matrix shear by smaller interchanges, and solve the resulting recurrence",
    mot("A recursive call at parameter $mf$ uses $s$ calls at parameter $f$ on streams of volume $V/W$, so dividing by volume multiplies the recursive contribution by $s/W<m$.", "explicit",
        r"increases the recursive contribution by $s/W<m$. This strict inequality"),
    [
        matrix_shear,
        infer("S1.1.2", r"Split rows cyclically into $W$ role streams, apply the frame shear $\Phi_{A_e}$ on every edge and each gate pointwise; the frame identity gives $H\leftarrow H+D$ on every row, and the updates $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ turn this into the interchange.",
              r"Split whole rows cyclically into $W$ role streams within each prefix",
              frm=["stream-ops", "matrix-shear", "bit-network-shear", "frames"]),
        infer("S1.1.3", r"There are $s$ recursive calls, each on a stream of volume $V/W$, so the time per unit volume satisfies $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.",
              r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1).",
              frm=["divide-and-conquer-and-recurrences", "rank-saving"]),
        infer("S1.1.4", r"Since $s/W<m^\tau$, the geometric sum $\sum_{j\le k}(s/W)^j$ is $O(m^{k\tau})$, hence $F_k=O(e^\tau)$.",
              r"Hence $F_k=O(e^\tau)$.",
              frm=["divide-and-conquer-and-recurrences", "logarithms-floors-and-ceilings"],
              salient="The exponent $\tau$ is strictly less than $1$ only because the number $s$ of recursive calls per volume fraction $1/W$ stays strictly below the branching factor $m$."),
    ],
    page="power-width-interchange",
    frm=["stream-ops", "controlled-shift", "rank-saving", "bit-network-shear", "frames"],
    adds=[b("e", "chunk width", "The number of radix-$q$ digits in each of the two chunks, a power $m^k$ of $m$."),
          b("k", "recursion depth", "The number of recursion levels, so that the chunk width is $e=m^k$.")],
)

interchange = show(
    "S1", r"Interchanging two disjoint $u$-bit address fields of an array whose addresses form a complete product costs $O(Vu^\tau)$ for a fixed $\tau<1$, where $V$ is the stored volume.",
    "recursion on the chunk width through the bit network's shear, first for power widths with enough rows and then for arbitrary widths",
    mot("Because the sum of the edge ranks is less than the number of wires times $m$, the recurrence saves a power of the chunk width.", "explicit",
        r"$m$, the resulting recurrence saves a power of the chunk width."),
    [
        power,
        infer("S1.2", r"For arbitrary widths, move $\rho=O(\log e)$ high digits to supply rows, pad them, write the remaining width in base $m$ as power-width pieces interchanged separately, and pad radix $2$ to radix $q$; this realizes $(p,h,g,d,z)\mapsto(p,d,g,h,z)$ in $O(Vu^\tau)$ steps.",
              r"in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$.",
              frm=["power-width-interchange", "stream-ops", "binary-representation-of-integers"]),
    ],
    page="chunk-interchange",
    frm=["permutations", "xor-and-mod-2-arithmetic", "divide-and-conquer-and-recurrences", "big-o"],
    salient="Although the final effect is an exact permutation of the data, the algorithm computes XOR combinations of intermediate streams, which is what lets the cost be a power $u^\\tau$ with $\\tau<1$ instead of $u$.",
)

# ---------------------------------------------------------------- fast simultaneous butterfly layers
phase = show(
    "S2.1", r"Since $H_0=b\,\mathsf S C\mathsf S$, the layer $H_0^{\otimes D}$ equals $b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, and the network turns $C^{\otimes e}$ on $e=mf$ axes into $s_{\rm c}$ calls on $f$ axes plus binary basis changes of selected bits.",
    "conjugate the butterfly by diagonal phases to the kernel $C$, then use the complex network's phase frames and realize its binary basis changes by packed bit additions",
    mot("The phase frames express an edge's residual operator as a product of two-point kernels on selected directions, which are $C$ kernels rather than $H_0$.", "explicit",
        "two-point kernels on selected directions."),
    [
        infer("S2.1.1", r"Applying the complex network with column frames to $e=mf$ selected axes gives exactly $s_{\rm c}$ child calls on the $f=e/m$ axes of one slot, plus a fixed number of binary row additions and coefficientwise scalar operations.",
              r"$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
              frm=["complex-phase-network", "matrices-and-matrix-vector-products"]),
        infer("S2.1.2", r"With $\mathsf S=\mathrm{diag}(1,i)$, $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ exactly in Gaussian dyadics.",
              r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D.",
              frm=["complex-numbers", "butterfly-fft"],
              salient="The kernel $C=aI+bX$ is a fourth root of the identity ($C^4=I$, $C^{-1}=-iZCZ$), so even a decreasing edge needs only one forward child call plus signs and fourth-root phases."),
        infer("S2.1.3", r"A binary row addition on corresponding selected bits of two address chunks, with a third chunk as restored scratch, costs $O(V(L^\tau+1))$ using eight packed cyclic shifts plus deterministic repair of an exponentially small set of exceptional addresses.",
              "eight operations in the displayed chronological order.", page="packed-bit-addition",
              frm=["chunk-interchange", "controlled-shift", "stream-ops", "xor-and-mod-2-arithmetic", "binary-representation-of-integers"]),
    ],
    page="phase-frame-reduction",
    frm=["complex-phase-network", "butterfly-fft", "complex-numbers", "matrices-and-matrix-vector-products"],
)

layer = show(
    "S2", r"Applying $H_0$ to the same bit position in $D\le d$ address chunks of polynomial records at once, exactly in Gaussian dyadics followed by one truncation, costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$.",
    "reduce the layer to the kernel $C$ by phase frames, evaluate it recursively through the complex network on row-split role streams, and bound the guard bits so everything is exact until the final truncation",
    mot("The phase frames express a $C$ tensor product using smaller groups of selected bits, so the same recursion that saved a power for address interchange applies to the numerical layer.", "explicit",
        r"frames express a $C$ tensor product using smaller groups of"),
    [
        phase,
        infer("S2.2", r"With $F(e)$ the time per unit volume for $e=m^k$ active chunks, the $s$ child calls on streams of volume $V/W$ give $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$.",
              r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),",
              frm=["divide-and-conquer-and-recurrences", "chunk-interchange", "complex-phase-network", "packed-bit-addition"]),
        infer("S2.3", r"Because $a=s/W<m^\lambda$ the internal costs form a geometric series $O(e^\lambda)$, and a base-$m$ partition of the $D$ chunks yields the total $O(Vd^{\lambda'})$ with $\lambda'<1$.",
              r"C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda).",
              frm=["divide-and-conquer-and-recurrences", "logarithms-floors-and-ceilings"]),
        infer("S2.4", r"Reserving $p+\Delta$ fractional bits and $\Delta+3$ integer bits per component, with $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$, represents every intermediate coefficient exactly, so the layer is exact until one truncation $Q_p$ with error below $\sqrt2\,2^{-p}$.",
              r"Thus reserving \(p+\Delta\)",
              frm=["fixed-point", "dyadic-and-rational-numbers", "two-s-complement-and-signed-integers"]),
    ],
    page="simultaneous-layer",
    frm=["fixed-point", "butterfly-fft", "complex-numbers", "dyadic-and-rational-numbers", "chunk-interchange"],
    salient="The cost has the same power-saving shape as the address interchange: $d^{\\lambda'}$ with $\\lambda'<1$ per unit volume, instead of the $D$ whole-array passes of separate butterflies, again from the strict inequality $s_{\\rm c}<W_{\\rm c}m$.",
    adds=[b("C", "phase kernel", "The two-point kernel $C=aI+bX$ with $a=(1+i)/2$, $b=(1-i)/2$, obtained from $H_0$ by diagonal phases.", "direct")],
)

# ---------------------------------------------------------------- synthetic transforms and layout
layout = show(
    "S3", r"A forward synthetic transform of an array of polynomial records on $d-1$ power-of-two axes, with selected bits brought to a common offset in $K$-bit chunks, leaves frequencies in a stored order $LB$ that the opposite transform consumes, and costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.",
    "lay the axes out by chunk interchanges so that each round is a simultaneous butterfly layer, and add up layout, layer, prefix-round and error costs",
    mot("The simultaneous layer applies only when the selected bits of the participating axes sit at a common offset in consecutive $K$-bit chunks, so such a layout must be constructed.", "explicit",
        "we must place the selected bits of the participating axes at a common"),
    [
        infer("S3.1", r"Over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ the roots $\omega_t=y^{2r/t}$ act as signed shifts of the coefficient list, so butterfly transforms $F_t^\pm$ have cheap twiddle multiplications and satisfy $F_t^+F_t^-=I/t$.",
              r"For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$.", page="synthetic-transform",
              frm=["ring-mod-yr", "dft", "butterfly-fft", "contraction-error", "multidim-transform"],
              salient="Multiplying by a root of unity costs no arithmetic at all, since $\\omega_t$ is a monomial and acts by a signed cyclic shift; and yet character sums still cancel because $y^r=-1$ gives a sign flip and the additive group has no two-torsion."),
        infer("S3.2", r"The decimation-in-frequency recursion writes its outputs directly in bit-reversed order, so $(F_t^-z)_j$ occupies slot $\mathrm{rev}(j)$, a record permutation $B_t$ that the reversed procedure consumes.",
              r"Let $B_t$ denote this record permutation: it moves the entry at $j$",
              frm=["butterfly-fft", "synthetic-transform"]),
        infer("S3.3", r"A grouped round of one butterfly per participating axis is a parallel butterfly $\mathcal H$ followed by one recordwise monomial $y^E$, so each completed round is a contraction.",
              r"Each $\mathcal H$ is a contraction and each",
              frm=["synthetic-transform", "contraction-error"]),
        infer("S3.4", r"Moving at most $D(b+1)=O(dK)$ named bit slots into a prefix costs $O(TpdK)$.",
              r"listed slots, so the moves cost $O(TpdK)$.",
              frm=["stream-ops"]),
        infer("S3.5", r"At most $Dq-1$ exchanges of width-$K$ address chunks bring the remaining chunks of all axes into the order required, at total cost $O(Tp\cdot pK^{\tau-1})$.",
              r"exchanges of width-$K$ address chunks, even when the chunks are",
              frm=["chunk-interchange", "stream-ops"]),
        infer("S3.6", r"Each of the $\ell$ rounds on the remaining chunks is one simultaneous-layer call costing $O(Tpd^{\lambda'})$.",
              r"The simultaneous-layer procedure therefore applies at cost",
              frm=["simultaneous-layer"]),
        infer("S3.7", r"The at most $K$ rounds on prefix slots are done bit by bit, individually, at cost $O(TpdK)$.",
              r"most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$.",
              frm=["stream-ops", "fixed-point"]),
        infer("S3.8", r"Each round truncates once, with error below $\sqrt2\,2^{-p}$, and contractions do not amplify earlier error, so $\ell$ rounds give error below $\sqrt2\,\ell\,2^{-p}$.",
              r"zero error, at most $\ell$ rounds therefore",
              frm=["contraction-error", "fixed-point"]),
        infer("S3.9", r"The forward procedure has exact counterpart $LBF^-_{\boldsymbol t}$ and stores the entry with frequency address $j$ at $L(Bj)$; the opposite procedure $F^+_{\boldsymbol t}B^{-1}L^{-1}$ consumes exactly this order.",
              r"In particular, the forward entry with frequency address $j$ is",
              frm=["synthetic-transform", "permutations"],
              salient="The opposite transform accepts precisely the bit-reversed, laid-out order the forward transform produces, so no sorting is needed between forward transform, pointwise product and opposite transform."),
    ],
    page="transform-layout",
    frm=["chunk-interchange", "simultaneous-layer", "fixed-point", "ring-mod-yr", "contraction-error",
         "butterfly-fft", "dft", "multidim-transform"],
)

# ---------------------------------------------------------------- ring convolution
ringconv = show(
    "S4", r"Forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform in the same stored order compute $f*g/(rM)$ on $d-1$ axes over $\mathbb C[y]/(y^r+1)$ with error below $\sqrt2\,M(3\ell+1)2^{-p}$.",
    "multiply the retained-order transforms pointwise using signed packing, then check normalization by the convolution theorem and add the errors by contraction bounds",
    mot("Pointwise multiplication commutes with the same record permutation applied to both operands, so the forward outputs can be multiplied in their retained order and passed directly to the opposite procedure.", "explicit",
        "forward outputs in their retained order and pass that order directly"),
    [
        infer("S4.1", r"Polynomials with small signed coefficients are evaluated at a large power of two to give integers, multiplied by the established $O(N\log N)$ integer multiplier, and recovered by centered residues, giving normalized products in $\mathbb C[y]/(y^r+1)$ in time $O(rp\log(rp))$.",
              r"$O(rp\log(rp))$ on a fixed number of tapes.", page="signed-packing",
              frm=["ring-mod-yr", "fixed-point", "history", "binary-representation-of-integers", "two-s-complement-and-signed-integers"]),
        infer("S4.2", r"Perform both forward transforms retaining their common order $LB$, multiply corresponding records by signed packing, apply the opposite procedure, and scale exactly by $M$.",
              r"Perform both forward transforms and retain their common $LB$ order.",
              frm=["transform-layout", "signed-packing"]),
        infer("S4.3", r"By the convolution theorem $F^-_{\boldsymbol t}(f*g)=M(F^-_{\boldsymbol t}f)(F^-_{\boldsymbol t}g)$, so $MF^+_{\boldsymbol t}\bigl((F^-_{\boldsymbol t}f)(F^-_{\boldsymbol t}g)/r\bigr)=f*g/(rM)$.",
              r"=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g).",
              frm=["convolution", "multidim-transform"]),
        infer("S4.4", r"The two forward errors and the product truncation add through the bilinear contraction bound, giving error below $3\delta+\eta$ before the exact scaling by $M$, hence below $\sqrt2\,M(3\ell+1)2^{-p}$.",
              r"The final exact multiplication by $M$ therefore gives error less than",
              frm=["contraction-error", "vector-norms-and-the-triangle-inequality"]),
        infer("S4.5", r"There are $M=T/r$ pointwise polynomial products, costing $O(Tp\log(rp))$ in total, in addition to the three transform costs.",
              r"There are $M=T/r$ pointwise polynomial products.",
              frm=["transform-layout", "signed-packing"]),
    ],
    page="ring-convolution",
    frm=["transform-layout", "signed-packing", "convolution", "multidim-transform", "contraction-error"],
    salient="The error bound $\\sqrt2\\,M(3\\ell+1)2^{-p}$ grows only linearly in the number $\\ell$ of rounds: contractions do not amplify earlier errors, and each transform adds one truncation per round.",
)

# ---------------------------------------------------------------- Gaussian resampling with retained permutations
resamp = show(
    "S5", r"Gaussian resampling gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with both coordinate permutations $R,Q$ left in the transform; the chirp absorbs $Q$, and $R$ cancels across the two forward transforms, the pointwise product and the opposite transform, giving $u*v/S^2$.",
    "tensor the one-dimensional resampling identity over the axes, convert the middle transform to a convolution by Bluestein's chirp identity, and show that the source permutation cancels",
    mot("The usual implementation sorts twice on each coordinate; keeping both permutations in the transform formula avoids executing them.", "explicit",
        "We retain both permutations in the transform formula and"),
    [
        infer("S5.1", r"For coprime $s<t$ the Fourier transform of length $s$ equals a transform of length $t$ sandwiched between Gaussian-weighted contractions: $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$.",
              r"P_sF_s=2^{2\alpha^2}B_0P_tF_tA.", page="gaussian-resampling",
              frm=["dft", "complex-numbers", "permutations", "primes-divisibility-coprimality-and-gcd", "vector-norms-and-the-triangle-inequality"]),
        infer("S5.2", r"Tensoring over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with contractions $\mathcal A,\mathcal B_0$, each applied line by line with error below $dp^2$.",
              r"=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A,",
              frm=["gaussian-resampling", "multidim-transform", "chunk-interchange"]),
        infer("S5.3", r"The chirp identity gives $QF_{\boldsymbol t}u=\overline a\cdot\bigl(a*(\overline a\cdot u)\bigr)/T$: a pointwise chirp product, a cyclic convolution with the chirp array, and a second chirp product, with the permutation $Q$ absorbed into the chirp.",
              r"\frac{a*(\overline a\mathbin{\cdot}u)}{T}.", page="bluestein",
              frm=["dft", "convolution", "multidim-transform", "euler-s-formula-and-complex-conjugation"]),
        infer("S5.4", r"Since $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$ and permutations commute with pointwise products, $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=u*v/S^2$.",
              r"=\frac{u*v}{S^2}.",
              frm=["convolution", "multidim-transform", "permutations", "primes-divisibility-coprimality-and-gcd"]),
    ],
    page="retained-permutations",
    frm=["dft", "multidim-transform", "convolution", "contraction-error", "chunk-interchange", "fixed-point"],
    salient="The source permutation $R$ cancels completely: although each Gaussian transform acts on permuted data, the combination $(RF_{\\boldsymbol s}^+)[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]$ equals $u*v/S^2$ with no sorting executed.",
)

# ---------------------------------------------------------------- assembly
twist = show(
    "S6.4.1", r"Normalized cyclic convolution on all $d$ power-of-two axes is $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=f*g/T$: twist the last coordinate into the ring, convolve the other axes over the ring, untwist.",
    r"twist the last coordinate by $\zeta^k$ so that its cyclic wrap becomes the ring's negative wrap, apply the ring convolution to the remaining axes, and untwist",
    mot("The power-of-two complex convolution used in the chirp identity can be obtained from the synthetic ring convolution by a coefficient twist.", "explicit",
        "obtained from the synthetic convolution by a coefficient twist."),
    [
        infer("S6.4.1.1", r"Multiplying coefficient $k$ by $\zeta^k$ with $\zeta=e^{\pi i/r}$ maps $\mathbb C[x]/(x^r-1)$ isomorphically onto $\mathbb C[y]/(y^r+1)$, because a wrapped term has factor $\zeta^{k+l}(-1)^h=\zeta^j$.",
              r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j.", page="phase-twist",
              frm=["ring-mod-yr", "complex-numbers", "euler-s-formula-and-complex-conjugation", "polynomials"],
              salient="The sign $(-1)^h$ of the negative wrap is cancelled exactly by $\\zeta^{rh}=(-1)^h$, since $\\zeta^r=-1$; so the ring's negacyclic wrap becomes the cyclic wrap after untwisting."),
        infer("S6.4.1.2", r"With $D_\pm$ the twists, $\iota$ the identification of the last coordinate with polynomial records, and $\mathcal M_r$ from the ring convolution, $\mathcal M_{\mathbb C}(f,g):=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)$ equals $f*g/T$.",
              r":=D_-\iota^{-1}",
              frm=["ring-convolution", "phase-twist"]),
    ],
    page="complex-convolution-twist",
    frm=["ring-convolution", "phase-twist", "ring-mod-yr", "convolution"],
)

srctrans = show(
    "S6.4", r"The procedure $\widetilde{\mathscr F}$ computes $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$: the Gaussian map $\mathcal A$ on each line, the chirp-based transform by complex convolution, the Gaussian map $\mathcal B_0$, then scaling by $2^\gamma$; the opposite sign by complex conjugation.",
    "compose the tensor resampling identity with the chirp identity, evaluating the power-of-two cyclic convolution by the coefficient twist and the ring convolution",
    mot("The middle factor $QF_{\\boldsymbol t}$ of the resampling identity is computed from a cyclic convolution and two pointwise phase products.", "explicit",
        "We next use the complex convolution to evaluate the middle factor"),
    [
        twist,
        infer("S6.4.2", r"The computed chirp transform multiplies pointwise by the conjugate chirp, convolves with the chirp array through the complex convolution, and multiplies again by the conjugate chirp, approximating $QF_{\boldsymbol t}$.",
              r"Thus $\widetilde a$ is the convolution kernel and $x_0$ is the data",
              frm=["complex-convolution-twist", "bluestein"]),
        infer("S6.4.3", r"Composing the linewise $\mathcal A$, the chirp transform, the linewise $\mathcal B_0$ and the exact scale $2^\gamma$ has exact counterpart $\mathscr F=RF_{\boldsymbol s}$; conjugating input and output gives the opposite-sign procedure.",
              r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A",
              frm=["retained-permutations", "bluestein", "complex-convolution-twist"]),
    ],
    page="source-transform",
    frm=["retained-permutations", "bluestein", "complex-convolution-twist", "gaussian-resampling"],
)

recovery = show(
    "S6.6", r"After removing the known scales, each recovered digit-convolution coefficient has error below $1/2$, so rounding gives the exact integer coefficients and radix-$2^b$ carries give the $2n$-bit product.",
    "bound the error of every computed quantity, conclude that the final error is below $1/2$, then round and propagate carries",
    mot("The true coefficients are real integers, so an error strictly below $1/2$ makes the nearest integer the unique correct coefficient.", "explicit",
        "The true coefficients are real integers."),
    [
        infer("S6.6.1", r"The accumulated error of the transforms, pointwise product and two scalings by $S$ gives final absolute error below $448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<1/2$.",
              r"\le448b\,2^{-3b/4}<\frac12.",
              frm=["contraction-error", "vector-norms-and-the-triangle-inequality", "constant-factors-versus-asymptotic-dominance"]),
        infer("S6.6.2", r"The strict error bound below $1/2$ makes the nearest integer to each recovered value the unique correct coefficient, which lies in $[0,2^{3b})$.",
              r"The strict error below $1/2$ makes the nearest integer to",
              frm=["dyadic-and-rational-numbers", "binary-representation-of-integers"]),
        infer("S6.6.3", r"Radix-$2^b$ carries propagated from least to most significant coefficient fix every radix digit and produce the exact $2n$-bit product.",
              r"After $\Phi^{-1}$ the coefficients occur in increasing ordinary index,",
              frm=["schoolbook-multiplication-and-carries", "binary-representation-of-integers"]),
    ],
    page="exact-recovery",
    frm=["contraction-error", "schoolbook-multiplication-and-carries", "integer-as-convolution", "dyadic-and-rational-numbers"],
    salient="The target error $1/2$ is met with a huge margin, since the working precision $p=6b$ far exceeds the $b$ bits of each digit scale and the resampling loss $\\gamma=o(b)$.",
)

mult = show(
    "S6", r"Forming radix-$2^b$ digits, applying the CRT map $\Phi$, computing two forward source transforms, multiplying pointwise, applying the opposite transform, rescaling by $S$ and $2^{2b+4}S$, rounding, inverting $\Phi$ and propagating carries outputs the exact $2n$-bit product.",
    "reduce the integer product to a cyclic convolution of radix-digit lists on a product of distinct prime axes, compute that convolution with three source transforms, and recover the exact coefficients by rounding",
    mot("Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.", "explicit",
        "Splitting the inputs into radix digits reduces multiplication to"),
    [
        infer("S6.1", r"Choose $b=\lceil\log_2 n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, a power of two $T\approx n/b$ split into $d$ axes of length $r/2$ or $r$, and distinct primes $s_i$ just below each $t_i$ found by deterministic search, so that $T/2<S<T$ and every hypothesis of resampling holds.",
              r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,", page="parameters",
              frm=["logarithms-floors-and-ceilings", "primes-divisibility-coprimality-and-gcd", "binary-representation-of-integers"],
              salient="Each prime $s_i$ lies just below the power of two $t_i$, so the product $S$ of the primes fills more than half of the padded box $T$ while each ratio $t_i/s_i$ still leaves the separation resampling needs."),
        infer("S6.2", r"Writing both inputs as polynomials in $2^b$ with $b$-bit digits, the product is a convolution of digit lists; the degree is below $S$, so there is no wraparound, and coefficients stay below $2^{3b}$.",
              r"Thus convolution modulo $x^S-1$ has no nonzero wraparound.", page="integer-as-convolution",
              frm=["polynomials", "schoolbook-multiplication-and-carries", "binary-representation-of-integers"]),
        infer("S6.3", r"With pairwise coprime axis lengths $s_i$, the map $x\mapsto\prod_i x_i^{\mu_i}$ is an isomorphism from $\mathbb C[x]/(x^S-1)$ onto the multi-axis cyclic ring, converting one long cyclic convolution into a multidimensional one, and acts on tape by triangular controlled shifts.",
              r"$\Phi$ is an isomorphism and preserves cyclic convolution.", page="crt-map",
              frm=["primes-divisibility-coprimality-and-gcd", "modular-arithmetic", "polynomials", "controlled-shift", "multidim-transform"]),
        srctrans,
        infer("S6.5", r"The two scalings by $S$ undo different normalizations: after the three transforms the result is $(u*v)/S^2$, and the final scale $2^{2b+4}S$ gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the integer coefficient convolution.",
              r"$2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original",
              frm=["retained-permutations", "crt-map", "source-transform"]),
        recovery,
    ],
    page="multiplication-algorithm",
    frm=["retained-permutations", "ring-convolution", "crt-map", "parameters", "integer-as-convolution", "source-transform",
         "schoolbook-multiplication-and-carries"],
)

cost = show(
    "S7", r"Dividing the costs by $Tp=\Theta(n)$, seven dominant terms have powers of $p$ at most $1-2\kappa$, so every polylogarithmic loss is absorbed and the total is $O(n(\log n)^{1-\kappa})$.",
    "tabulate the normalized cost of every operation, compare each power of $p$ with one, and absorb the remaining logarithmic factors in the smallest margin",
    mot("The smallest margin below one is an explicit slack that covers any remaining fixed power of $\\log p$.", "explicit",
        "This explicit slack will cover"),
    [
        infer("S7.1", r"The seven dominant normalized costs, from layout, simultaneous rounds, CRT and axis layouts, Gaussian line maps, chirps and packed products, have margins below one whose minimum is $2^{-181}=2\kappa$.",
              r"Thus $\min_i g_i=2^{-181}=2\kappa$.",
              frm=["chunk-interchange", "simultaneous-layer", "transform-layout", "ring-convolution", "retained-permutations", "parameters"],
              salient="The smallest margin $g_2=\\epsilon c(1-\\tau)=2^{-75-56-50}=2^{-181}$ is the product of three tiny exponents, so $\\kappa=2^{-182}$ is half of it; the saving is real but astronomically small."),
        infer("S7.2", r"Each of the seven powers is at most $1-2\kappa$ and any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
              r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}).",
              frm=["constant-factors-versus-asymptotic-dominance", "logarithms-floors-and-ceilings", "big-o"]),
    ],
    page="cost-accounting",
    frm=["parameters", "multiplication-algorithm", "transform-layout", "simultaneous-layer", "chunk-interchange",
         "ring-convolution", "constant-factors-versus-asymptotic-dominance"],
)

root = show(
    "S0", r"A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time, with $\kappa=2^{-182}$.",
    "build two fast tape procedures (address interchange and simultaneous butterfly layers), use them for a fast synthetic-transform convolution over a polynomial ring, wrap that in the Gaussian-resampling, Bluestein and CRT reduction of integer multiplication, then recover the exact product and total the cost",
    mot("Scanning the whole array at each of the Theta(log n) transform levels already costs n log n, so a saving is needed in both data movement and arithmetic, and these are what the two tape procedures supply.", "explicit",
        "We therefore need savings in both movement and arithmetic."),
    [common, interchange, layer, layout, ringconv, resamp, mult, cost],
    page="main-theorem",
    frm=["history", "big-o", "multitape-tm", "binary-representation-of-integers", "schoolbook-multiplication-and-carries",
         "logarithms-floors-and-ceilings", "constant-factors-versus-asymptotic-dominance"],
    salient="The saving is a genuine power of the logarithm, yet $\\kappa=2^{-182}$ is astronomically small: it comes from the strict inequality $s<Wm$ for fixed finite networks, which survives as exponents $\\tau,\\lambda'<1$ in two tape procedures, and every other cost has power of $p$ at most $1-2\\kappa$.",
)

ans = {"root": root}

# ------------------------------------------------------------------ checks
pos_prev = -1
problems = []
pages_seen = {}


def walk(n, page, order):
    page = n.get("page") or page
    if n.get("page"):
        if n["page"] in pages_seen:
            problems.append("page twice: " + n["page"])
        pages_seen[n["page"]] = n["id"]
    for f in n.get("from", []):
        if f in KNOWN:
            continue
        if f not in ORDER:
            problems.append(f"{n['id']}: unknown from {f}")
        elif ORDER.index(f) >= ORDER.index(page):
            problems.append(f"{n['id']}: from {f} not before page {page}")
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        c = SRC.count(q)
        if c != 1:
            problems.append(f"{n['id']}: quote count {c}: {q}")
        if "\n" in q:
            problems.append(f"{n['id']}: newline in quote")
        p = SRC.find(q)
        order.append((n["id"], p))
    else:
        if n["motivation"]["source"] == "explicit":
            q = n["motivation"]["quote"]["quote"]
            if SRC.count(q) < 1:
                problems.append(f"{n['id']}: motivation quote missing: {q}")
        for ch in n["children"]:
            walk(ch, page, order)


order = []
walk(root, None, order)
last = -1
for i, p in order:
    if p <= last:
        problems.append(f"order violation at {i}: {p} <= {last}")
    last = p
used = set(pages_seen)
allfrom = set()


def collect(n):
    allfrom.update(n.get("from", []))
    for c in n.get("children", []):
        collect(c)


collect(root)
for pg in ORDER:
    if pg not in used and pg not in allfrom:
        problems.append("page unused: " + pg)
print("pages with steps:", len(used))
print("order:", [(i, SRC.count('\n', 0, p) + 1) for i, p in order])
print("PROBLEMS:", problems)
json.dump(ans, open('/home/user/openai-nlogn-wiki/runs/P3/exegenius/tasks/0003-argument.answer.json', 'w'), indent=1, ensure_ascii=False)
