import json, sys, re

SRC = "paper"

def Q(q):
    return {"source": SRC, "quote": q}

def infer(id, claim, quote, frm=(), page=None, salient=None, deferred=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": Q(quote), "from": list(frm)}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if deferred: n["deferred"] = True
    return n

def show(id, claim, method, mot_text, mot_source, children, frm=(), page=None, mot_quote=None, salient=None, adds=None):
    mot = {"text": mot_text, "source": mot_source}
    if mot_quote: mot["quote"] = Q(mot_quote)
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": mot,
         "children": children, "from": list(frm)}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n

def add(symbol, name, meaning, relation):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

# ---------------- C0: linear-cost tape toolkit ----------------
C0 = show("S1", "Elementary address manipulations on a fixed-tape machine cost time linear in the stored volume $V$.",
  "State the two linear-time primitives that every later procedure calls: scans that split and merge streams, and controlled cyclic shifts of a later field.",
  "Every later recursion calls these primitives a bounded number of times per node, so their cost per call must be $O(V)$ for the recursion overhead not to swamp the saving.",
  "recoverable",
  [
    infer("S1.1", "Fixed digit permutations, digit moves, pointwise maps on split streams and cyclic row splits each take $O(V)$ steps for $V$ stored bits.",
          "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
          ["fixed-tape-model", "lexicographic-order-and-index-tuples", "multitape-machine-cost-model-and-linear-time-scans", "permutations-and-permutation-matrices"],
          page="stream-arrays"),
    infer("S1.2", "Adding an offset computed from earlier control fields to a later target field modulo $q^b$, or multiplying it by a fixed unit, costs $O(V)$.",
          "y\\longmapsto y+a(\\text{controls})\\pmod Q",
          ["stream-arrays", "modular-arithmetic-and-residues", "rational-numbers-dyadic-rationals-and-exact-arithmetic"],
          page="controlled-shifts"),
  ],
  frm=["fixed-tape-model", "multitape-machine-cost-model-and-linear-time-scans"])

# ---------------- C1: finite networks ----------------
C1_3 = show("S2.3", "Subspaces of an $m$-dimensional space can be attached to the gates and terminals so adjacent labels are nested and the total number $s$ of smaller operations on edges is strictly below $Wm$.",
  "Attach to each gate a nondegenerate subspace built from the triple indicator vectors, check that every edge joins comparable labels with only one family of decreasing edges, and add up the dimension changes (and ranks of the projection differences).",
  "The scalar network already has the signed exchange; choosing the intermediate labels well is what makes each change of frame cheap.",
  "explicit",
  [
    infer("S2.3.1", "Every edge joins comparable nondegenerate labels; the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$, so the absolute dimension changes total $Wm-2N+2L$ with $L<N/2$.",
          "edges are the central-wire edges from time 3 to time 4; their dimension",
          ["bilinear-orthogonal", "triple-gadget", "vector-spaces-basis-and-dimension"]),
    infer("S2.3.2", "For the bit network the rational ranks of the edge differences of projection matrices sum to $s_{\\rm b}<W_{\\rm b}m$, and the endpoint difference on every input role is the identity matrix $I_m$.",
          "=177176569088785861287000000<W_{\\rm b}m.",
          ["bilinear-orthogonal", "matrices-invertibility-and-rank", "frames"]),
  ],
  frm=["bilinear-orthogonal", "bank-exchange-network", "frames", "triple-gadget"],
  page="subspace-labels",
  mot_quote="choose its intermediate labels to make the changes of frame inexpensive.",
  salient="The saving is real but tiny: $s$ is below $Wm$ only by a relative margin of about $10^{-11}$, because only the $Ich$ central-wire decreases and the $N$ source ranks eat into the budget, and the inequality is strict only since $L<N/2$.")

C1 = show("S2", "There are two fixed linear networks that exchange two banks of values, restore every scratch value, and allow subspace labels whose edge changes total fewer than $Wm$ smaller operations.",
  "Build the three-stage bank-exchange network from the subset-intersection gadgets, state the common-frame invariant for arrays on wires, attach nested subspace labels, and read off the bit (matrix) and complex (phase) interfaces.",
  "A numerical or bit array can only be exchanged by pointwise gates if a change of representation on each edge is cheap, and the cost of those changes is controlled by the label ranks.",
  "recoverable",
  [
    infer("S2.1", "Three stages of forward invocations send $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ and restore every auxiliary scratch value, whatever its initial contents.",
          "(X_a,Y_a)\\longmapsto(-Y_a,X_a)",
          ["triple-gadget", "bitwise-xor", "rational-numbers-dyadic-rationals-and-exact-arithmetic"],
          page="bank-exchange-network",
          salient="The scratch wires may start with arbitrary values and still come out unchanged, and the net map is independent of them; the first two rows of the schedule cancel the old scratch values, and the last two rows put them back."),
    infer("S2.2", "If every wire's array is stored in a frame $D_v$ common to all incidences of a gate, pointwise linear gates commute with the frame, so the network implements $D_{\\rm out}\\,\\mathsf S\\,D_{\\rm in}^{-1}$ and only edge changes $D_vD_u^{-1}$ cost anything.",
          "Thus the common frame commutes with the pointwise gate, and",
          ["matrices-invertibility-and-rank", "algebraic-structures-groups-rings-and-isomorphisms", "bank-exchange-network"],
          page="frames"),
    C1_3,
    infer("S2.4", "On the complex network with binary labels each edge's phase-frame change is a product of translation kernels $aI+bX_v$, one per residual basis vector, and the total number of such factors is $s_{\\rm c}<W_{\\rm c}m$; telescoping gives $C^{\\otimes m}$ on every role.",
          "bank exchange, telescoping these phase frames gives $C^{\\otimes m}$",
          ["subspace-labels", "bank-exchange-network", "frames", "bilinear-orthogonal", "complex-numbers", "bitwise-xor"],
          page="phase-kernel-network"),
  ],
  frm=["triple-gadget"])

# ---------------- C2: chunk interchange ----------------
C2_3 = show("S3.3", "Two chunks of $e=m^k$ digits can be interchanged in $O(Ve^\\tau)$ time when enough rows are available.",
  "Split rows cyclically into $W$ role streams, run the bank-exchange network with frame $\\Phi_M$ on each, implementing every edge as rank-many smaller chunk interchanges on streams of volume $V/W$, and solve the resulting recurrence.",
  "Each smaller interchange acts on volume $V/W$, so the cost per volume grows by the factor $s/W$ per level; since $s/W<m$ this is a power saving.",
  "explicit",
  [
    infer("S3.3.1", "The shear $H\\leftarrow H+D$ on every role stream gives, together with two linear updates, the interchange $(H,D)\\mapsto(D,H)$ of the $e$-digit chunks using $s$ calls on streams of volume $V/W$.",
          "D\\leftarrow D-H,\\qquad H\\leftarrow H+D,\\qquad D\\leftarrow H-D,",
          ["frames", "bank-exchange-network", "subspace-labels", "matrix-shear", "stream-arrays"]),
    infer("S3.3.2", "If $F_k$ bounds time per volume for width $m^k$, then $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
          "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).",
          ["discrete-math-proof-techniques", "big-o"]),
    infer("S3.3.3", "Because $s/W<m^\\tau$, the geometric sum gives $F_k=O(e^\\tau)$.",
          "Hence $F_k=O(e^\\tau)$.",
          ["geometric-series-and-orthogonality-of-sums-of-roots-of-unity", "logarithms-floors-ceilings-and-powers-of-two"]),
  ],
  frm=["frames", "bank-exchange-network", "subspace-labels", "matrix-shear", "stream-arrays"],
  page="power-width-interchange",
  mot_quote="is the source of the power saving.",
  salient="The cost per volume is $O(e^\\tau)$ with $\\tau<1$: the recursion branches into $s$ calls each of volume $V/W$ and $s/W$ is strictly less than $m$, the factor by which the width grows, so the exponent falls strictly below one.",
  adds=[
    add("W", "wire count", "the number of wires, i.e. role streams, of the bank-exchange network", "count"),
    add("s", "total rank", "the sum of the rational ranks of all edge matrices, i.e. the number of smaller interchanges per call", "count"),
    add("m", "field count", "the number of fields into which each chunk is cut at one recursion level", "count"),
    add("e", "chunk width", "the number of radix-$q$ digits in each chunk, a power of $m$", "count"),
  ])

C2 = show("S3", "Two disjoint address chunks of $u$ bits in any bit array can be interchanged in $O(Vu^\\tau)$ steps for a fixed $\\tau<1$.",
  "Factor each rational edge matrix as lower-triangular times partial permutation times lower-triangular so a shear costs one smaller interchange per unit of rank, recurse on power widths using the bit bank-exchange network, then remove the width and row restrictions by padding and a base-$m$ split.",
  "The strict rank saving $s<Wm$ of the bit network can only be cashed in if each rank unit costs exactly one smaller interchange, so the shear must be factored in an order matching the tape direction.",
  "explicit",
  [
    infer("S3.1", "Every rational square matrix of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation matrix with exactly $a$ ones.",
          "A=E_1\\Pi E_2,",
          ["matrices-invertibility-and-rank", "permutations-and-permutation-matrices"],
          page="triangular-factorization"),
    infer("S3.2", "The address update $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ costs exactly $\\operatorname{rank}(A)$ interchanges of pairs of $b$-digit fields plus $O(V)$ work.",
          "can be performed with exactly $a$ interchanges of pairs of $b$-digit",
          ["triangular-factorization", "controlled-shifts", "stream-arrays", "modular-arithmetic-and-residues"],
          page="matrix-shear"),
    C2_3,
    infer("S3.4", "Padding rows to a multiple of $W^k$ and cutting the remaining width in base $m$ into power-width pieces gives an interchange of arbitrary equal-width chunks in $O(Ve^\\tau)$.",
          "O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau).",
          ["power-width-interchange", "stream-arrays", "geometric-series-and-orthogonality-of-sums-of-roots-of-unity"]),
    infer("S3.5", "Padding binary chunk ranges $[2^u]$ up to $[q^e]$ changes the volume only by a constant factor, so the bound holds for bit chunks of $u$ bits.",
          "Since $e=O(u)$ for fixed $q$, the bound is",
          ["power-width-interchange", "binary-representation-of-integers"]),
  ],
  frm=["power-width-interchange", "matrix-shear", "stream-arrays", "fixed-tape-model"],
  page="chunk-swap",
  mot_quote="Because the sum of these ranks is less than the number of wires times",
  salient="Although the procedure forms XOR combinations of the data at intermediate steps, its final effect is an exact permutation, correct for arbitrary initial auxiliary values.",
  adds=None)

# ---------------- C3: simultaneous butterfly layer ----------------
C3 = show("S4", "One normalized butterfly $H_0$ applied to the same bit position in each of $d$ address chunks of polynomial records is computed exactly, then truncated once, in $O(Vd^{\\lambda'})$ time for a fixed $\\lambda'<1$.",
  "Express the tensor of $H_0$ through the two-point kernel $C$, evaluate $C^{\\otimes e}$ by the complex bank-exchange network whose child calls act on $e/m$ axes, implement the binary basis changes with packed XORs of selected bits, and bound the intermediate dyadic widths.",
  "Doing the $d$ butterfly factors separately needs $d$ whole-array passes; the network recursion replaces them by a recursion whose per-volume cost grows only like $d^{\\lambda'}$.",
  "explicit",
  [
    infer("S4.1", "Applying the complex network with column frames to $e=mf$ selected axes needs exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and yields $C^{\\otimes e}$ on every role.",
          "$s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
          ["phase-kernel-network", "power-width-interchange", "frames", "chunk-swap"]),
    infer("S4.2", "The normalized layer is recovered from the $C$ layer by exact diagonal phases: $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$.",
          "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.",
          ["phase-kernel-network", "complex-numbers"]),
    infer("S4.3", "Row addition $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$ on the selected bit of each of $f$ chunks costs $O(V(L^\\tau+1))$ using a third chunk as restored temporary space.",
          "y_{j_i}\\longleftarrow y_{j_i}\\mathbin\\oplus x_{j_i}",
          ["chunk-swap", "controlled-shifts", "stream-arrays", "bitwise-xor"],
          page="packed-selected-bits"),
    infer("S4.4", "With the row split giving each child $1/W_{\\rm c}$ of the parent's volume, the recurrence and packed basis changes give total time $O(Vd^{\\lambda'})$ on fixed tapes.",
          "give total time $O(Vd^{\\lambda'})$ on fixed tapes, including",
          ["power-width-interchange", "packed-selected-bits"]),
    infer("S4.5", "Intermediate coefficients are exact Gaussian dyadics whose denominator and magnitude growth is bounded by $\\lceil C_0d^{C_1}\\rceil$, which is $o(p)$, so the width stays $O(p)$.",
          "The guard-width calculation above bounds both denominator and magnitude",
          ["rational-numbers-dyadic-rationals-and-exact-arithmetic", "fixed-point-disk-grid"]),
    infer("S4.6", "Every row of $\\mathcal H$ has absolute row sum one, so the layer maps the disk to the disk and the single final truncation $Q_p$ has error below $\\sqrt2\\,2^{-p}$.",
          "Finally, every row of $\\mathcal H$ has",
          ["fixed-point-disk-grid", "norms-and-the-triangle-inequality"]),
  ],
  frm=["phase-kernel-network", "packed-selected-bits", "chunk-swap", "fixed-point-disk-grid"],
  page="simultaneous-butterfly-layer",
  mot_quote="factors would require $D$ whole-array passes.",
  salient="The layer on $d$ axes costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, strictly less than the $d$ passes of separate butterflies, for the same reason as the chunk interchange: $s_{\\rm c}/W_{\\rm c}<m^\\sigma$ with $\\sigma<1$.")

# ---------------- C4: ring convolution ----------------
C4_3 = show("S5.3", "A forward or opposite synthetic transform on $d-1$ polynomial axes, arranged by a layout permutation, has error below $\\sqrt2\\,\\ell\\,2^{-p}$ and costs $O\\bigl(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}]\\bigr)$.",
  "Place the selected bits of all axes at a common offset in consecutive $K$-bit chunks by prefix-slot moves and chunk exchanges, run one simultaneous layer per round, and handle the first few rounds one bit at a time.",
  "The simultaneous layer applies only when the participating bits sit at the same offset in consecutive equal-width chunks, so the stored axes must first be rearranged by a permutation that is itself cheap.",
  "explicit",
  [
    infer("S5.3.1", "The layout permutation is a product of at most $Dq-1$ exchanges of width-$K$ chunks, costing $O(Tp\\cdot pK^{\\tau-1})$ in total.",
          "=O\\bigl(Tp\\,pK^{\\tau-1}\\bigr).",
          ["chunk-swap"]),
    infer("S5.3.2", "Each round on the remaining chunks is one simultaneous layer followed by a signed coefficient shift, so all $\\ell$ rounds cost $O(Tp\\,\\ell d^{\\lambda'})$.",
          "$O(Tpd^{\\lambda'})$ per round and $O(Tp\\ell d^{\\lambda'})$ in total.",
          ["simultaneous-butterfly-layer", "butterfly-layers", "synthetic-transform"]),
    infer("S5.3.3", "The at most $K$ rounds on prefix slots are done bit by bit with signed monomial shifts and cost $O(TpdK)$.",
          "most $b+1\\leq K$ rounds on prefix slots, giving cost $O(TpdK)$.",
          ["butterfly-layers", "negacyclic-ring"]),
    infer("S5.3.4", "Each round is a contraction followed by one truncation, so at most $\\ell$ rounds keep the output in the disk with error below $\\sqrt2\\,\\ell\\,2^{-p}$.",
          "give the claimed error and disk bounds.",
          ["fixed-point-disk-grid", "norms-and-the-triangle-inequality"]),
  ],
  frm=["synthetic-transform", "butterfly-layers", "chunk-swap", "simultaneous-butterfly-layer"],
  page="transform-layout",
  mot_quote="To apply Proposition~\\ref{prop:simultaneous-layer} in a transform round,",
  )

C4 = show("S5", "Normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\\mathbb C[y]/(y^r+1)$ is computed from the retained transform layout with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$ time.",
  "Apply the synthetic forward transform to both operands, multiply pointwise in the retained frequency order with signed packed products, apply the opposite transform that consumes that order, and scale by $M$.",
  "Pointwise multiplication commutes with any common record permutation, so the frequency order left by the forward transforms need not be restored before the product.",
  "explicit",
  [
    infer("S5.1", "The synthetic roots $\\omega_t=y^{2r/t}$ satisfy character cancellation despite zero divisors, so $F_t^+F_t^-=t^{-1}I$.",
          "F_t^+F_t^-=t^{-1}I.",
          ["negacyclic-ring", "geometric-series-and-orthogonality-of-sums-of-roots-of-unity", "algebraic-structures-groups-rings-and-isomorphisms"],
          page="synthetic-transform"),
    infer("S5.2", "Decimation in frequency leaves the frequencies in bit-reversed order, so the two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
          "B_tF_t^-,\\qquad F_t^+B_t^{-1},",
          ["synthetic-transform", "negacyclic-ring", "permutations-and-permutation-matrices"],
          page="butterfly-layers"),
    C4_3,
    infer("S5.4", "Two polynomials of the ring with $p$-bit grid coefficients can be multiplied exactly by signed Kronecker packing and the established multiplier, returning $Q_p(fg/r)$ in $O(rp\\log(rp))$.",
          "$O(rp\\log(rp))$ on a fixed number of tapes.",
          ["negacyclic-ring", "nlogn-subroutine", "polynomials", "binary-representation-of-integers"],
          page="signed-kronecker-packing"),
    infer("S5.5", "Expanding the finite sums gives $F^-_{\\boldsymbol t}(f*g)=M(F^-_{\\boldsymbol t}f)(F^-_{\\boldsymbol t}g)$, which together with $F^+F^-=I/M$ identifies the retained-order pipeline with $\\mathcal M_r(f,g)$.",
          "=M(F_{\\boldsymbol t}^-f)(F_{\\boldsymbol t}^-g).",
          ["synthetic-transform", "butterfly-layers", "transform-layout", "convolution-as-polynomial-multiplication"]),
    infer("S5.6", "Using contraction of the transforms and the bilinear product, the three transform errors and the product truncation add up to $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
          "$M(3\\delta+\\eta)=\\sqrt2\\,M(3\\ell+1)2^{-p}$, as claimed.",
          ["fixed-point-disk-grid", "norms-and-the-triangle-inequality"]),
    infer("S5.7", "There are $M=T/r$ pointwise polynomial products, so the total cost is the three transform costs plus $O(Tp\\log(rp))$, with the last scaling by $M$ linear.",
          "the last exact scaling is linear in $Tp$.",
          ["transform-layout", "signed-kronecker-packing"]),
  ],
  frm=["transform-layout", "signed-kronecker-packing", "synthetic-transform", "butterfly-layers"],
  page="ring-convolution",
  mot_quote="forward outputs in their retained order and pass that order directly",
  adds=[add("r", "record length", "the number of complex coefficients in a polynomial record modulo $y^r+1$, a power of two", "count")])

# ---------------- C5: resampling without sorting ----------------
C5_1 = show("S6.1", "For coprime lengths $s<t$ the coordinate permutations $P_s,P_t$ stay inside the identity $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, and tensoring it over $d$ axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with line-wise maps costing $O(dTp^{3/2+\\delta}\\alpha)$.",
  "Take Harvey and van der Hoeven's Gaussian identity, absorb the two label-and-sort permutations into the transform formula so that only $A$ and $B_0$ are executed, tensor the one-dimensional identity, and apply the maps line by line, moving axes with the chunk interchange.",
  "Executing the source and target permutations as separate sorts would cost a full $O(tp\\log t)$ sort per coordinate; leaving them in the formula avoids all of it.",
  "recoverable",
  [
    infer("S6.1.1", "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and $B_0:\\mathbb C^t\\to\\mathbb C^s$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$.",
          "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA.",
          ["gaussian-resampling", "dft-cyclic-convolution", "permutations-and-permutation-matrices", "gaussian-function"]),
    infer("S6.1.2", "Fixed multitape algorithms approximate $A$ and $B_0$ with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$.",
          "There are fixed multitape algorithms for approximations",
          ["gaussian-resampling", "fixed-point-disk-grid"]),
    infer("S6.1.3", "Tensoring over $d$ axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$.",
          "=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A,",
          ["multidim-transform"]),
    infer("S6.1.4", "Exposing and restoring all the lines costs $O(Tp\\,d^2(1+\\ell^\\tau))$ by chunk interchanges of the axis fields.",
          "exposing and restoring all the lines costs",
          ["chunk-swap", "stream-arrays"]),
  ],
  frm=["gaussian-resampling", "multidim-transform", "chunk-swap", "fixed-point-disk-grid", "dft-cyclic-convolution"],
  page="resampling-no-sort",
  salient="Both permutations $R$ and $Q$ need never be executed; they remain inside the transform identity, which is why the cost has no sorting term.")

C5_2 = show("S6.2", "The chirp identity $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$ evaluates the target-permuted transform without applying $Q$, and the source permutation cancels: $(RF^+_{\\boldsymbol s})[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
  "Check the chirp formula coefficient by coefficient, and show that $R$ commutes with the inverse transform and with pointwise products, so it cancels between the two forward transforms and the opposite transform.",
  "A chirp turns the transform with its frequency permutation into a cyclic convolution of ordinary arrays, and a permutation that appears on both sides of a pointwise product can be cancelled by commuting it through.",
  "recoverable",
  [
    infer("S6.2.1", "The coefficient of $u_{\\boldsymbol k}$ in $\\overline a\\cdot(a*(\\overline a\\cdot u))/T$ equals the coefficient in $QF_{\\boldsymbol t}$.",
          "\\frac{a*(\\overline a\\mathbin{\\cdot}u)}{T}.",
          ["bluestein-chirp", "euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle"]),
    infer("S6.2.2", "Since $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$ and pointwise products commute with permutations, the source permutation $R$ drops out and only the normalization $1/S^2$ remains.",
          "\\bigl[(RF_{\\boldsymbol s}u)\\mathbin{\\cdot}",
          ["dft-cyclic-convolution", "permutations-and-permutation-matrices", "primes-divisibility-gcd-and-coprimality"]),
  ],
  frm=["bluestein-chirp", "resampling-no-sort", "dft-cyclic-convolution", "multidim-transform"],
  page="chirp-permutation-cancel",
  salient="The source permutation $R$ does not appear in the final answer at all: it is applied by both forward transforms, undone by the opposite transform, and leaves only the factor $1/S^2$.")

C5 = show("S6", "Gaussian resampling can express the transforms of pairwise coprime lengths through power-of-two transforms while the source and target permutations are never executed as separate sorts.",
  "Keep the source and target permutations inside the tensor transform identity, then use a chirp identity for the middle power-of-two transform and cancel the source permutation across the product.",
  "The usual implementation of Gaussian resampling sorts twice on each coordinate, which is itself a full $\\log$-factor cost.",
  "explicit",
  [C5_1, C5_2],
  frm=["gaussian-resampling"],
  mot_quote="We retain both permutations in the transform formula and")

# ---------------- C6: the multiplication algorithm ----------------
C6_1 = show("S7.1", "Fixed rational exponents, the digit width $b$, precision $p$, axis count $d$, padded size $T$ and distinct odd prime lengths $s_i$ can be chosen so that $Tp=\\Theta(n)$ and every hypothesis of the interfaces holds.",
  "Fix the exponents as explicit rationals, set sizes from $b=\\lceil\\log_2 n\\rceil$, select the primes in intervals just below the power-of-two lengths, and check the resampling and capacity hypotheses.",
  "The interfaces demand many inequalities at once (resampling separation, prime availability, no wraparound), which can only be met by choosing all sizes together from one parameter.",
  "reconstructed",
  [
    infer("S7.1.1", "With $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$ and $T\\in[4n/b,8n/b)$ we get $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$, $\\ell=\\Theta(p^{1-\\epsilon})$ and $r=2^{\\Theta(p^{1-\\epsilon})}$.",
          "Tp=\\Theta(n),\\quad d=\\Theta(p^\\epsilon),\\quad",
          ["logarithms-floors-ceilings-and-powers-of-two", "big-o"]),
    infer("S7.1.2", "Distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ exist, so $T/2<S<T$ and $\\gcd(s_i,t_i)=1$.",
          "(1-2\\eta)t_i<s_i\\leq(1-\\eta)t_i.",
          ["primes-divisibility-gcd-and-coprimality"]),
    infer("S7.1.3", "Every hypothesis of the one-dimensional resampling lemma holds for large $n$, in particular $\\alpha^4\\theta_i>p$ and $2\\le\\alpha<\\sqrt p$.",
          "Thus every hypothesis of Lemma~\\ref{lem:no-sort-resampling} holds for",
          ["resampling-no-sort"]),
    infer("S7.1.4", "The product of the digit polynomials has degree $2q-2<2n/b\\le T/2<S$, so cyclic convolution modulo $x^S-1$ has no wraparound.",
          "2q-2<2n/b\\le T/2<S.",
          ["radix-digit-convolution", "convolution-as-polynomial-multiplication"]),
  ],
  frm=["radix-digit-convolution", "resampling-no-sort", "simultaneous-butterfly-layer", "logarithms-floors-ceilings-and-powers-of-two"],
  page="parameter-choice")

C6_2 = show("S7.2", "The radix-digit coefficient list can be placed on a product of $d$ distinct prime cyclic axes by an isomorphism $\\Phi$ that preserves cyclic convolution and is realized by triangular controlled shifts.",
  "Use the Chinese-remainder isomorphism $x\\mapsto\\prod_i x_i^{\\mu_i}$, compute each axis coordinate from lower ones by a formula that is triangular in tape order, and implement the updates as controlled cyclic shifts with axis moves.",
  "A convolution on a long cyclic axis of composite length cannot be tensored, but one on a product of coprime cyclic axes can be tensored axis by axis.",
  "explicit",
  [
    infer("S7.2.1", "The map $\\Phi:x\\mapsto\\prod_i x_i^{\\mu_i}$ is an algebra isomorphism that preserves cyclic convolution.",
          "$\\Phi$ is an isomorphism and preserves cyclic convolution.",
          ["primes-divisibility-gcd-and-coprimality", "modular-arithmetic-and-residues", "algebraic-structures-groups-rings-and-isomorphisms"]),
    infer("S7.2.2", "Axis coordinates are $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j \\pmod{s_i}$, triangular in tape order, so each axis is one prefix-controlled cyclic shift.",
          "b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}.",
          ["controlled-shifts", "lexicographic-order-and-index-tuples"]),
    infer("S7.2.3", "$\\Phi$, its inverse and the padding operations cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
          "their padding operations cost",
          ["chunk-swap", "stream-arrays"]),
  ],
  frm=["controlled-shifts", "chunk-swap", "stream-arrays", "radix-digit-convolution", "dft-cyclic-convolution", "multidim-transform"],
  page="crt-axis-map",
  mot_quote="To use the source tensor, we first place the ordinary coefficient stream")

C6_3 = infer("S7.3", "Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ is a ring isomorphism from $x^r=1$ to $y^r=-1$, and the negative wrap becomes the cyclic wrap after untwisting.",
          "\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j.",
          ["negacyclic-ring", "dft-cyclic-convolution", "euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle"],
          page="coefficient-twist")

C6_4 = show("S7.4", "A source Fourier transform of prime lengths is computed by Gaussian maps $\\mathcal A$, a chirp transform evaluated by a twisted ring convolution, $\\mathcal B_0$ and an exact scale $2^\\gamma$, with exact counterpart $RF_{\\boldsymbol s}$.",
  "Compose the computed Gaussian expansion, the chirp transform (a convolution with the chirp array between two phase multiplications, computed by the twisted ring convolution), the Gaussian compression, and the power-of-two scale.",
  "The prime-length transform has no fast algorithm itself; resampling reduces it to a power-of-two tensor transform whose middle factor is a convolution, which is exactly what the ring convolution computes.",
  "explicit",
  [
    infer("S7.4.1", "Normalized complex convolution of arrays on the power-of-two axes is $D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$.",
          "\\mathcal M_r(\\iota D_+f,\\iota D_+g)",
          ["coefficient-twist", "ring-convolution", "negacyclic-ring"]),
    infer("S7.4.2", "Replacing approximations by exact phases and convolution, the computed chirp transform has exact counterpart $QF_{\\boldsymbol t}x$.",
          "(a,\\overline a\\mathbin{\\cdot}x)=QF_{\\boldsymbol t}x$ by",
          ["chirp-permutation-cancel", "bluestein-chirp"]),
    infer("S7.4.3", "The computed source transform has exact counterpart $\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$.",
          "\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A",
          ["resampling-no-sort"]),
    infer("S7.4.4", "Conjugating input and output gives the opposite-sign procedure with exact counterpart $RF^+_{\\boldsymbol s}$.",
          "its exact counterpart is $RF_{\\boldsymbol s}^{+}$ by",
          ["chirp-permutation-cancel"]),
  ],
  frm=["resampling-no-sort", "chirp-permutation-cancel", "ring-convolution", "coefficient-twist", "bluestein-chirp"],
  page="source-transform",
  mot_quote="We next use the complex convolution to evaluate the middle factor")

C6_7 = show("S7.8", "Removing the known normalizations $S$ and $2^{2b+4}$ leaves the integer coefficient convolution with error below $1/2$, so rounding recovers it exactly and carries produce the $2n$-bit product.",
  "Track errors through the disk margins of each stage, accumulate them into a final bound after the two scalings, round to the nearest integer, and propagate radix-$2^b$ carries.",
  "All stages are contractions on the unit disk with one truncation each, so errors simply add and the final bound is a sum of explicit terms compared with $1/2$.",
  "recoverable",
  [
    infer("S7.8.1", "The computed source transform has error below $E_sh_p$ with $E_s=9\\,2^\\gamma TL$, and stays in the disk.",
          "E_s=9\\,2^\\gamma TL,",
          ["fixed-point-disk-grid", "norms-and-the-triangle-inequality"]),
    infer("S7.8.2", "After the opposite transform and the first scale by $S$, the error is below $E_wh_p$ with $E_w=S(3E_s+2)<28\\,2^\\gamma T^2L$.",
          "E_w:=S(3E_s+2)<28\\,2^\\gamma T^2L.",
          ["chirp-permutation-cancel", "fixed-point-disk-grid"]),
    infer("S7.8.3", "After the second scale the absolute error is below $448b\\,2^{-3b/4}<1/2$.",
          "\\le448b\\,2^{-3b/4}<\\frac12.",
          ["parameter-choice", "logarithms-floors-ceilings-and-powers-of-two"],
          salient="The final error bound leaves a huge margin: it is exponentially small in $b$ because the precision $p=6b$ exceeds the $2b+4$ bits of the scaling plus the loss $2^{\\gamma}$ with $\\gamma=o(b)$."),
    infer("S7.8.4", "Since the true coefficients are integers and the error is below $1/2$, the nearest integer is the unique correct coefficient.",
          "that value the unique correct coefficient.",
          ["rational-numbers-dyadic-rationals-and-exact-arithmetic"]),
    infer("S7.8.5", "The carry recurrence $d_j=(c_j+k_j)\\bmod 2^b$, $k_{j+1}=\\lfloor(c_j+k_j)/2^b\\rfloor$ keeps carries below $2^{2b}$ and yields the radix-$2^b$ digits of the product.",
          "k_0=0,\\qquad d_j=(c_j+k_j)\\bmod Q_0,\\qquad",
          ["schoolbook-multiplication-and-divide-and-conquer-multiplication", "binary-representation-of-integers", "discrete-math-proof-techniques"]),
    infer("S7.8.6", "The exact product is less than $2^{2n}$, so removing the zero padding bits leaves exactly the $2n$-bit output.",
          "than $2^{2n}$; all bits above position $2n-1$ are therefore zero.",
          ["binary-representation-of-integers"]),
  ],
  frm=["fixed-point-disk-grid", "parameter-choice", "source-transform", "chirp-permutation-cancel"],
  page="exact-recovery")

C6 = show("S7", "The multiplication algorithm, run on $x\\#y$, outputs exactly the $2n$-bit product of the two $n$-bit integers.",
  "Split the inputs into radix digits, map them by $\\Phi$ to prime axes, take two source transforms, multiply pointwise, apply the opposite-sign transform with two rescalings by $S$, round, undo $\\Phi$ and propagate carries.",
  "The product of digit polynomials is a convolution of the digit lists, and convolution becomes pointwise multiplication under a normalized Fourier transform.",
  "explicit",
  [
    C6_1, C6_2, C6_3, C6_4,
    infer("S7.5", "The two digit arrays $u,v$ placed on the prime axes by $\\Phi$ have each their source transform computed by $\\widetilde{\\mathscr F}$.",
          "\\item Compute $\\widetilde{\\mathscr F}(u)$ and",
          ["source-transform", "crt-axis-map"]),
    infer("S7.6", "Multiplying the two transforms coefficientwise and truncating each part toward zero gives the array $z$.",
          "\\item Multiply corresponding complex coefficients exactly and truncate",
          ["fixed-point-disk-grid", "complex-numbers"]),
    infer("S7.7", "Applying the opposite-sign transform and multiplying by $S$ gives the array $w=(u*v)/S$.",
          "\\item Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid",
          ["source-transform", "chirp-permutation-cancel"]),
    infer("S7.7b", "Multiplying by $2^{2b+4}S$ and rounding gives the integer convolution coefficients on the prime axes; undoing $\\Phi$ and removing padding restores the ordinary coefficient order.",
          "\\item Multiply the grid numerators of $\\widetilde w$ exactly by",
          ["crt-axis-map"]),
    infer("S7.7c", "The two occurrences of $S$ undo different normalizations: the exact counterpart is $(u*v)/S^2$ after the three transforms, and $2^{2b+4}(u*v)$ after both scales.",
          "$2^{2b+4}(u*v)$, whose inverse image under $\\Phi$ is the original",
          ["chirp-permutation-cancel", "dft-cyclic-convolution"]),
    C6_7,
  ],
  frm=["parameter-choice", "crt-axis-map", "coefficient-twist", "source-transform", "exact-recovery", "radix-digit-convolution"],
  page="multiplication-algorithm",
  mot_quote="The source-transform procedures now supply the three transforms needed",
  adds=[
    add("b", "digit width", "the bit length of a radix digit, $\\lceil\\log_2 n\\rceil$", "direct"),
    add("p", "precision", "the number of fractional bits of the fixed-point grid, $6b$", "count"),
    add("d", "axis count", "the number of transform axes", "count"),
    add("T", "padded size", "the number of entries of the padded power-of-two box", "count"),
    add("S", "prime-axis product", "the product of the distinct odd prime axis lengths", "direct"),
  ])

# ---------------- C8: cost ----------------
C8 = show("S8", "The total running time of the machine is $O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$.",
  "Tabulate each operation's cost divided by $Tp$, show each is at most $p^{1-2\\kappa}$ using explicit exponent margins, add the setup and exceptional-address costs, absorb powers of $\\log p$, and use schoolbook multiplication below a cutoff.",
  "A table of exponents makes the dominant costs comparable and the smallest margin directly gives the saving exponent.",
  "recoverable",
  [
    infer("S8.1", "The seven dominant margins below one have minimum $2^{-181}=2\\kappa$.",
          "Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
          ["logarithms-floors-ceilings-and-powers-of-two"],
          salient="The saving exponent $\\kappa=2^{-182}$ is half the smallest of the seven margins $g_i$, and the smallest, $g_2=\\epsilon c(1-\\tau)=2^{-181}$, comes from the chunk-exchange term $pK^{\\tau-1}$."),
    infer("S8.2", "Layout chunk exchanges cost $O(p/K)\\cdot K^\\tau$ per volume, i.e. $O(pK^{\\tau-1})$.",
          "$O(VK^\\tau)$ by Lemma~\\ref{lem:chunk-swap}, so the normalized total is",
          ["chunk-swap", "transform-layout"]),
    infer("S8.3", "The CRT rotations and axis layouts cost $O(d^2(1+\\ell^\\tau))$ per volume.",
          "The $d$ CRT rotations copy valid and invalid intervals in $O(dV)$ time.",
          ["crt-axis-map", "chunk-swap"]),
    infer("S8.4", "The Gaussian line maps cost $O(dp^{1/2+\\delta}\\alpha)$ per volume.",
          "Dividing by $V=Tp$ gives the fifth row.",
          ["resampling-no-sort"]),
    infer("S8.5", "Chirps, twists and scalar products cost $O(dp^{\\delta})$ per volume.",
          "then generating the exponentials, costs $O(dp^{1+\\delta})$ per entry.",
          ["source-transform", "nlogn-subroutine"]),
    infer("S8.6", "The calls to the established multiplier use records of length $o(n)$ and do not call the improved algorithm recursively.",
          "they do not call the improved algorithm being constructed.",
          ["nlogn-subroutine", "signed-kronecker-packing"]),
    infer("S8.7", "Setup over all recursion visits costs at most $p^{A+C}=o(Tp)$.",
          "costs at most $p^{A+C}=o(Tp)$.",
          ["parameter-choice"]),
    infer("S8.8", "The deterministic repair of the exceptional addresses costs $o(V)$ in the worst case.",
          "a deterministic worst-case bound.",
          ["packed-selected-bits"]),
    infer("S8.9", "Each of the seven displayed powers is at most $1-2\\kappa$, and any power of $\\log p$ is at most $p^\\kappa$ eventually.",
          "Each of the seven displayed powers is at most $1-2\\kappa$ by",
          ["logarithms-floors-ceilings-and-powers-of-two"]),
    infer("S8.10", "The total is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
          "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa}).",
          ["big-o"]),
    infer("S8.11", "Below a fixed cutoff schoolbook multiplication is used, giving one fixed machine with worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every input length.",
          "$O(n(\\lg n)^{1-\\kappa})$ for every input length and produces precisely",
          ["schoolbook-multiplication-and-divide-and-conquer-multiplication", "fixed-tape-model"]),
  ],
  frm=["transform-layout", "chunk-swap", "crt-axis-map", "resampling-no-sort", "nlogn-subroutine", "multiplication-algorithm", "parameter-choice"],
  page="cost-accounting")

C0.pop("page", None)
root = show("S0", "A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$.",
  "Start from the Gaussian-resampling reduction of integer multiplication to convolution; replace the two costly operations of the synthetic transforms (address rearrangement and butterfly layers) by faster procedures built from one recursive linear-network exchange, assemble the exact algorithm, and account for its cost.",
  "Scanning the whole array at each of the logarithmically many transform levels already costs $n\\log n$, so both movement and arithmetic must be sped up.",
  "explicit",
  [C0, C1, C2, C3, C4, C5, C6, C8],
  frm=["n-log-n-conjecture", "fixed-tape-model", "nlogn-subroutine", "big-o", "turing-machine-tapes", "schoolbook-multiplication-and-divide-and-conquer-multiplication"],
  page="main-theorem",
  mot_quote="We therefore need savings in both movement and arithmetic.",
  salient="The saving $\\kappa=2^{-182}$ is minuscule but positive: every one of the many cost terms is a power of $p$ below $p^{1-2\\kappa}$, so a fixed power of $\\log n$ is saved rather than any larger factor.")

out = {"root": root}
json.dump(out, open(sys.argv[1], "w"), indent=2, ensure_ascii=False)

# verify quotes order
text = open("sources/paper.tex").read()
quotes = []
def walk(n):
    if n["intention"] == "infer":
        quotes.append((n["id"], n["quote"]["quote"]))
    for c in n.get("children", []):
        walk(c)
walk(root)
pos = -1
ok = True
for i, q in quotes:
    c = text.count(q)
    p = text.find(q)
    flag = ""
    if c == 0: flag = "MISSING"; ok = False
    elif c > 1: flag = "MULTI(%d)" % c
    if p < pos: flag += " OUT-OF-ORDER"; ok = False
    print(i, p, flag)
    pos = max(pos, p)
print("OK" if ok else "PROBLEMS")
