import json, sys

def ev(q): return {"source": "paper", "quote": q}

def inf(id, claim, quote, page=None, frm=None, salient=None, deferred=False):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": frm or []}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if deferred: n["deferred"] = True
    return n

def show(id, claim, method, mot, msrc, children, page=None, frm=None, salient=None, adds=None, mquote=None):
    m = {"text": mot, "source": msrc}
    if mquote: m["quote"] = ev(mquote)
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": m,
         "children": children, "from": frm or []}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n

def add(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

# ---------------- S1 chunk interchange
S1_6 = show("S1.6",
  "The bit network sends its input to the permutation $\\rho$ of that vector, with rational matrices $M_v$ at gates and terminals whose endpoint differences equal $I_m$ and whose edge ranks sum to $s<Wm$, so $s/W<m^\\tau$ for the fixed exponent $\\tau=1-2^{-50}$.",
  "Assign the orthogonal projection $P_U$ to each vertex with label $U$ (and $-P_{U_a}$ to the sources), so each edge rank equals the label dimension change; then turn the relative rank deficit into a power exponent",
  "The tape shear needs integer-free rational matrices whose edge differences have rank equal to the dimension change, so the dimension count of the labels transfers directly to a count of smaller interchanges; the exponent step makes the saving a clean power.",
  "recoverable",
  [inf("S1.6.1", "The projections give $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m$ on every input role and the edge ranks sum to $s=Wm-N+2L<Wm$.",
       "The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,",
       frm=["subspace-labels-rank-saving", "linear-algebra-basics", "frames"]),
   inf("S1.6.2", "Because the relative deficit of $s$ below $Wm$ exceeds $20\\cdot2^{-50}$, one fixed exponent $\\tau=1-2^{-50}$ satisfies $s/W<m^\\tau$.",
       "\\frac{s_{\\rm b}}{W_{\\rm b}}<m^\\tau,",
       salient="Although $s/W$ is only a hair below $m$ (relative deficit about $10^{-14}$), a fixed exponent $\\tau=1-2^{-50}<1$ already satisfies the inequality, which is what turns a tiny rank deficit into a power saving.")],
  page="rational-matrix-interface",
  frm=["subspace-labels-rank-saving", "frames", "linear-algebra-basics", "scalar-exchange-network", "matrices-matrix-products-and-inverses", "logarithms-floors-and-ceilings"])

S1_9 = show("S1.9",
  "For $e=m^k$ and a row field of length divisible by $W^k$, two disjoint chunks of $e$ radix-$q$ digits each can be interchanged in $O(Ve^\\tau)$ time on a fixed number of tapes.",
  "Split rows cyclically into the $W$ role streams, apply the network with shear frames on each edge so that each edge is a few recursive interchanges of width $e/m$ on volume $V/W$, and solve the resulting recurrence",
  "The interchange is rewritten as a shear $H\\leftarrow H+D$ of $m$ sub-fields, which the finite network can realise; the cost is then governed by a recurrence in which each of the $s$ recursive calls sees only a $1/W$ share of the volume.",
  "recoverable",
  [inf("S1.9.1", "Splitting rows into $W$ role streams and applying the shear frame $\\Phi_{A_e}$ on every edge of the bit network yields the shear $H\\leftarrow H+D$ on every row, and $D\\leftarrow D-H$, then the shear, then $D\\leftarrow H-D$ interchanges the two chunks.",
       "Split whole rows cyclically into $W$ role streams within each prefix",
       frm=["frames", "elementary-streams", "rational-matrix-interface", "address-shear-cost"]),
   inf("S1.9.2", "The $s$ recursive interchanges each act on one stream of volume $V/W$, so the normalized cost satisfies $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
       "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).",
       frm=["address-shear-cost", "rational-matrix-interface", "recurrences-induction-and-geometric-sums"]),
   inf("S1.9.3", "Since $s/W<m^\\tau$, the geometric sum of the recurrence is $O(m^{k\\tau})$, hence $F_k=O(e^\\tau)$.",
       "For $a=s/W<m^\\tau$ the geometric sum",
       frm=["recurrences-induction-and-geometric-sums"],
       salient="The cost per unit volume grows only like $e^\\tau$ with $\\tau<1$, although each node makes $s$ calls: the calls shrink in volume by $W$ while $s$ is just below $Wm$, and $m=e^{1/k}$ per level, so the per-level multiplier $s/W<m^\\tau$ is strictly below the width ratio $m$."),
   inf("S1.9.4", "The recursive calls run on a fixed set of tapes by parking the $W-1$ inactive role streams on a stack, copying the active stream to the child and restoring on return, at only $O(V)$ extra cost per node.",
       "Before a recursive call, append the $W-1$ inactive role streams to the",
       page="fixed-tape-recursion-schedule",
       frm=["stacks-and-queues", "turing-machine", "elementary-streams", "address-shear-cost", "binary-counters-and-finite-state-bookkeeping"])],
  page="power-width-interchange",
  frm=["address-shear-cost", "rational-matrix-interface", "frames", "elementary-streams", "recurrences-induction-and-geometric-sums"],
  salient="The exponent $\\tau$ is strictly below $1$, so the interchange beats the $\\Theta(Ve)$ cost of moving digits one at a time, even though the network has about $Wm$ edge-ranks.",
  adds=[add("F_k", "normalized interchange cost", "the time, divided by the logical volume, of a power-width interchange of $m^k$ digits")])

S1 = show("S1",
  "Two disjoint address chunks of $u$ bits each, in an array of volume $V$, can be interchanged by $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$ in $O(Vu^\\tau)$ time for a fixed $\\tau<1$, although the intermediate steps are XOR combinations of data.",
  "Realise the interchange as a shear $H\\leftarrow H+D$ computed by a fixed linear exchange network whose edge changes are smaller shears, recurse with total edge rank $s<Wm$, and extend from power widths to arbitrary widths",
  "Moving digits one at a time costs a full pass per digit; a linear network that exchanges two banks while restoring scratch wires lets each recursion level use fewer than $m$ times the volume-share of calls, which is the source of a power saving.",
  "explicit",
  [inf("S1.1", "Digit permutations and moves, splitting on a digit, pointwise maps, merging and cyclic row splitting into a fixed number $W$ of streams each take $O(V)$ steps on a fixed number of tapes.",
       "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
       page="elementary-streams",
       frm=["turing-machine", "binary-counters-and-finite-state-bookkeeping", "stacks-and-queues", "sorting-and-radix-sort"]),
   inf("S1.2", "A target address field can be updated $y\\mapsto y+a(\\text{controls}) \\bmod q^b$, or multiplied by a fixed rational unit, in $O(V)$ time when the controls precede the target on tape.",
       "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
       page="controlled-cyclic-shifts",
       frm=["elementary-streams", "modular-arithmetic-and-congruences", "greatest-common-divisor-and-the-euclidean-algorithm", "stacks-and-queues"]),
   inf("S1.3", "A fixed network of copy, gather, scatter and side-injection gates on triples of an $h$-element set, run in three stages, sends $(X,Y)\\mapsto(-Y,X)$ and restores every scratch wire whatever its initial value.",
       "and restores every auxiliary value.  In the bit construction this is the",
       page="scalar-exchange-network",
       frm=["bitwise-xor", "vectors-and-matrices-over-the-two-element-field", "binomial-coefficients", "sets-functions-bijections-and-permutations"],
       salient="The exchange is exact for arbitrary initial scratch values: the first two rows subtract the old scratch contribution and the last two restore it, so the net target change is independent of those values."),
   inf("S1.4", "With an invertible frame $D_v$ at each vertex, pointwise gates commute with the frame, so a route from input role $w$ to output role $\\rho(w)$ applies only the endpoint operator $D_{\\mathrm{sink}}D_{\\mathrm{source}}^{-1}$.",
       "Thus the common frame commutes with the pointwise gate, and",
       page="frames",
       frm=["scalar-exchange-network", "matrices-matrix-products-and-inverses", "sets-functions-bijections-and-permutations"],
       salient="All intermediate frames cancel along a route, so the operator seen by every role, including scratch roles, depends only on its two endpoint frames; the intermediate frames are free to be chosen so each edge is cheap."),
   inf("S1.5", "Nested nondegenerate subspace labels can be attached to the gates and terminals so that the only decreasing edges are the central-wire returns, and the dimension changes over all edges sum to $Wm-2N+2L$ with $L<N/2$.",
       "Every edge joins comparable nondegenerate labels.  The only decreasing",
       page="subspace-labels-rank-saving",
       frm=["linear-algebra-basics", "tensor-product", "scalar-exchange-network", "frames", "binomial-coefficients", "vectors-and-matrices-over-the-two-element-field"],
       salient="The total edge rank is strictly less than the trivial bound (number of wires) times (space dimension), because gates and sources/sinks telescope and only the $Ich$ dimensions lost on central wires are counted twice."),
   S1_6,
   inf("S1.7", "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones.",
       "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
       page="lower-triangular-factorization",
       frm=["matrices-matrix-products-and-inverses", "gaussian-elimination-and-row-operations", "linear-algebra-basics"]),
   inf("S1.8", "The shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ for a matrix $A$ of rank $a$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work.",
       "can be performed with exactly $a$ interchanges of pairs of $b$-digit",
       page="address-shear-cost",
       frm=["lower-triangular-factorization", "controlled-cyclic-shifts", "elementary-streams", "modular-arithmetic-and-congruences"]),
   S1_9,
   inf("S1.10", "For arbitrary shapes and widths, using a few high digits as supplied rows, padding and the power-width calls, the interchange costs $O(Vu^\\tau)$.",
       "There exist fixed $0<\\tau<1$ and one fixed finite-alphabet multitape",
       frm=["power-width-interchange", "elementary-streams", "recurrences-induction-and-geometric-sums"])],
  page="chunk-interchange",
  frm=["turing-machine", "bitwise-xor", "recurrences-induction-and-geometric-sums"],
  mquote="is the source of the power saving.",
  salient="The cost is $O(Vu^\\tau)$ with $\\tau=1-2^{-50}$ just below $1$: the saving over moving digits one by one is a tiny power of the width, coming from the strict inequality $s<Wm$.",
  adds=[add("W", "number of wires", "the number of wires, including scratch wires, of the fixed bit network", "count"),
        add("m", "label dimension", "the dimension of the ambient subspace space, and the number of address fields per chunk in each recursion step", "count"),
        add("s", "total edge rank", "the sum over all edges of the rational rank of the edge matrix, which equals the number of smaller interchange calls", "count"),
        add("\\tau", "interchange exponent", "the fixed exponent below $1$ in the cost $O(Vu^\\tau)$")])

# ---------------- S2 butterfly layer
S2 = show("S2",
  "The butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ can be applied at once to the same bit position of $D\\le d$ address chunks of a polynomial-record array in $O(Vd^{\\lambda'})$ time for a fixed $\\lambda'<1$, followed by one truncation $Q_p$.",
  "Apply the complex phase network recursively to compute $C^{\\otimes D}$ (which differs from $H_0^{\\otimes D}$ by diagonal phases), implement the binary basis changes by packed whole-chunk shifts, split rows among the network roles to shrink each call, and keep all values exact until one final truncation",
  "Applying $D$ separate butterfly factors would need $D$ whole-array passes; the same exchange network that speeds up address moves gives a recursion with $s$ children on a $1/W$ share of the volume, so the cost per unit volume grows as a power of $d$ below one.",
  "explicit",
  [inf("S2.1", "With phase frames $\\mathcal C_U=H^{\\otimes m}\\operatorname{diag}(i^{\\mathrm{wt}(P_Ux)\\bmod4})H^{\\otimes m}$, each edge change is a product of translation kernels $aI+bX_v$, one per vector of an orthonormal basis of its residual, so $s_{\\rm c}<W_{\\rm c}m$ smaller calls of $C^{\\otimes}$ suffice and the whole network realises $C^{\\otimes m}$ on every role.",
       "bank exchange, telescoping these phase frames gives $C^{\\otimes m}$",
       page="phase-frame-interface", deferred=True,
       frm=["phase-kernel", "fft-butterfly", "scalar-exchange-network", "frames", "subspace-labels-rank-saving", "tensor-product", "linear-algebra-basics", "vectors-and-matrices-over-the-two-element-field", "complex-numbers"],
       salient="Every role, including the auxiliary scratch roles, ends with the same operator $C^{\\otimes m}$, and the number of kernels per edge equals the residual dimension."),
   inf("S2.2", "Applying the network with column frames to a group of $e=mf$ selected axes needs exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and returns $C^{\\otimes e}$ on every role.",
       "$e=mf$ selected axes.  Summing its residual dimensions gives exactly",
       frm=["phase-frame-interface", "chunk-interchange"]),
   inf("S2.3", "The normalized layer equals phase-conjugated $C$ layer: $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$, where $\\mathcal S_D$ multiplies by $i^{x_1+\\cdots+x_D}$ and all phases and scalars are exact Gaussian dyadic operations.",
       "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.",
       frm=["phase-kernel", "fft-butterfly", "complex-numbers"]),
   inf("S2.4", "The XOR $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$ of selected bits of chunks, needed for binary basis changes, is done by a few whole-chunk cyclic shifts and a sorting repair of a small bad set, restoring a scratch chunk $z$, in $O(V(L^\\tau+1))$ time.",
       "record payload; in particular, it restores the entire chunk $z$ for",
       page="packed-selected-bit-addition",
       frm=["chunk-interchange", "controlled-cyclic-shifts", "elementary-streams", "sorting-and-radix-sort", "bitwise-xor", "modular-arithmetic-and-congruences"]),
   inf("S2.5", "Splitting rows among the $W$ roles gives the recurrence $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ for time per unit volume, which unrolls to $O(d^{\\lambda'})$ with $\\lambda'<1$.",
       "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),",
       frm=["packed-selected-bit-addition", "chunk-interchange", "recurrences-induction-and-geometric-sums"],
       salient="The bound is a power $d^{\\lambda'}$ of the number of simultaneous axes rather than linear in $d$, because the children have only $1/W$ of the volume while their number $s$ stays below $Wm$."),
   inf("S2.6", "All intermediate values of one layer are exact Gaussian dyadics, and $\\lceil C_0d^{C_1}\\rceil$ guard bits bound denominator and magnitude growth, so a single truncation after the completed layer suffices.",
       "A(e)\\le sA(e/m)+E",
       page="guard-width-exactness",
       frm=["fixed-point-disk-arithmetic", "phase-frame-interface", "two-s-complement-and-fixed-width-signed-integers", "fft-butterfly"]),
   inf("S2.7", "The recursion, the packed basis changes and the guard-width bound together give total time $O(Vd^{\\lambda'})$, and $\\mathcal H$ maps disk arrays to disk arrays with truncation error below $\\sqrt2\\,2^{-p}$.",
       "The row construction and the recurrence analysis",
       frm=["guard-width-exactness", "packed-selected-bit-addition", "phase-frame-interface"])],
  page="simultaneous-butterfly-layer",
  frm=["fft-butterfly", "phase-kernel", "dft", "fixed-point-disk-arithmetic", "chunk-interchange"],
  mquote="factors would require $D$ whole-array passes.",
  salient="A layer on $D\\le d$ axes costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, which is sublinear in the number of axes, not $D$ passes over the array.",
  adds=[add("D", "number of axes", "the number of address chunks, among at most $d$, on which the layer acts", "count"),
        add("K", "chunk width", "the number of bits in each address chunk"),
        add("\\lambda'", "layer exponent", "the fixed exponent below $1$ in the layer cost $O(Vd^{\\lambda'})$")])

# ---------------- S3 synthetic convolution
S3 = show("S3",
  "Normalized convolution $\\mathcal M_r(f,g)=(f*g)/(rM)$ over $\\mathbb C[y]/(y^r+1)$ of arrays on $M=T/r$ cyclic addresses with disk grid values can be computed with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
  "Perform two forward synthetic transforms whose rounds use the simultaneous butterfly layer on a chunked layout, multiply the transforms pointwise in the retained stored order by signed packing, and apply the opposite transform",
  "Synthetic roots of unity $y^{2r/t}$ turn twiddle factors into signed shifts, so the whole transform consists of butterflies that the fast layer accelerates, plus polynomial products, which are small enough to use the established multiplier.",
  "explicit",
  [inf("S3.1", "The synthetic transform over $\\mathbb C[y]/(y^r+1)$ with roots $\\omega_t=y^{2r/t}$ is computed by butterflies $H_0$ and twiddles that are signed shifts, and it leaves the entry $(F_t^-z)_j$ in the bit-reversed slot $\\operatorname{rev}_a(j)$.",
       "entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$.",
       page="synthetic-transform",
       frm=["polynomial-ring-mod", "dft", "fft-butterfly", "roots-of-unity", "multidimensional-transform", "cyclic-convolution"],
       salient="The outputs are left in bit-reversed frequency order and this order is never undone: the opposite transform consumes exactly that stored order, so no sorting pass is needed."),
   inf("S3.2", "A layout permutation $L$ built from prefix-slot moves and $O(p/K)$ chunk exchanges puts the selected bits of all axes at a common offset of consecutive $K$-bit chunks, so each transform round is one simultaneous layer, at total cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
       "The procedure constructs an explicit positional",
       page="synthetic-transform-layout",
       frm=["synthetic-transform", "simultaneous-butterfly-layer", "chunk-interchange", "elementary-streams", "crt-address-map"],
       ),
   inf("S3.3", "Pointwise multiplication commutes with applying the same record permutation $LB$ to both operands, so the forward outputs can be multiplied in the retained order and passed straight to the opposite procedure.",
       "Pointwise multiplication commutes with applying the same record",
       frm=["synthetic-transform", "synthetic-transform-layout"]),
   inf("S3.4", "Evaluating integer polynomials at $B_0=2^{4p}$, multiplying them with the established multiplier, and extracting signed coefficients by centered residues multiplies ring elements of $\\mathbb C[y]/(y^r+1)$ in $O(rp\\log(rp))$ time.",
       "One can compute the exact Gaussian integer",
       page="signed-packing",
       frm=["harvey-hoeven-multiplier", "polynomial-ring-mod", "binary-representation-of-integers", "two-s-complement-and-fixed-width-signed-integers"]),
   inf("S3.5", "Two forward transforms in the common $LB$ order, the pointwise ring products and the opposite transform followed by an exact scaling by $M$ give $\\mathcal M_r$ within the stated error and cost.",
       "Perform both forward transforms and retain their common $LB$ order.",
       frm=["synthetic-transform-layout", "signed-packing", "synthetic-transform", "cyclic-convolution"])],
  page="synthetic-convolution",
  frm=["signed-packing", "polynomial-ring-mod", "cyclic-convolution", "multidimensional-transform", "dft", "simultaneous-butterfly-layer"],
  mquote="The work here is to apply the simultaneous layers on a suitable tape",
  adds=[add("r", "ring degree", "the number of complex coefficients in a record of the ring $\\mathbb C[y]/(y^r+1)$, a power of two", "count"),
        add("M", "number of records", "the number of polynomial records, the product of the first $d-1$ axis lengths", "count"),
        add("\\ell", "log of ring degree", "the base-two logarithm of $r$, so $r=2^\\ell$")])

# ---------------- S4 resampling
S4 = show("S4",
  "A transform of pairwise coprime lengths $s_i$ is expressed through power-of-two lengths $t_i$ by $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with the permutations $R,Q$ kept inside the formula, the middle factor $QF_{\\boldsymbol t}$ is a chirp convolution, and the retained permutation $R$ cancels in a convolution.",
  "Retain the source and target permutations in the Gaussian resampling identity instead of sorting, compute the middle transform by Bluestein's chirp, and show the source permutation cancels across two forward transforms, a pointwise product and the opposite transform",
  "The product needs transforms of coprime lengths, while the fast layers apply only to powers of two; resampling connects the two shapes, and leaving the permutations inside the formula avoids two full sorts per coordinate, which would cost too much.",
  "explicit",
  [inf("S4.1", "For $\\gcd(s,t)=1$ and $s<t$, there are contractions $A$ and $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, whose disk-grid approximations cost $O(tp^{3/2+\\delta}\\alpha)$ and have error below $p^2$.",
       "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and",
       frm=["dft", "greatest-common-divisor-and-the-euclidean-algorithm", "vector-norms-and-the-triangle-inequality", "fixed-point-disk-arithmetic", "harvey-hoeven-multiplier"]),
   inf("S4.2", "Applying the one-dimensional maps one coordinate line at a time gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$, at cost $O(dTp^{3/2+\\delta}\\alpha)$ plus $O(Tp\\,d^2(1+\\ell^\\tau))$ for axis movement by chunk swaps.",
       "For the tensor product, apply the one-dimensional maps to one coordinate",
       frm=["multidimensional-transform", "chunk-interchange", "dft"]),
   inf("S4.3", "With the chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$, the permuted transform is $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$: pointwise multiplication, a normalized cyclic convolution with the chirp, and another pointwise multiplication.",
       "Then $a$ has period $t_i$ in coordinate $i$, and",
       page="bluestein-chirp",
       frm=["dft", "cyclic-convolution", "multidimensional-transform", "gaussian-resampling", "complex-numbers"]),
   inf("S4.4", "Since $R$ commutes with pointwise products and $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$, the retained permutation cancels: $(RF^+_{\\boldsymbol s})[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
       "$F_{\\boldsymbol s}^+R=R^{-1}F_{\\boldsymbol s}^+$ and hence",
       page="permutation-cancellation",
       frm=["dft", "cyclic-convolution", "multidimensional-transform", "gaussian-resampling", "modular-arithmetic-and-congruences", "sets-functions-bijections-and-permutations"],
       salient="The source permutation $R$ disappears from the final result, which is exactly $(u*v)/S^2$, so it never has to be executed.")],
  page="gaussian-resampling",
  frm=["dft", "multidimensional-transform", "fixed-point-disk-arithmetic", "harvey-hoeven-multiplier", "chunk-interchange"],
  mquote="coordinate. We retain both permutations in the transform formula and",
  adds=[add("\\alpha", "Gaussian width", "the integer parameter of the Gaussian weights, of order $p^{1/4+\\epsilon/2}$"),
        add("\\gamma", "source scale exponent", "the exponent $2d\\alpha^2$ of the exact scale $2^\\gamma$ in the tensor identity")])

# ---------------- S5 algorithm
S5_1 = show("S5.1",
  "For input length $n$ take $b=\\lceil\\log_2 n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, power-of-two axis lengths $t_i\\in\\{r/2,r\\}$ with product $T\\in[4n/b,8n/b)$, and distinct odd primes $s_i$ just below $t_i$ with $T/2<S<T$, so that every hypothesis of the layer, transform and resampling results holds.",
  "Choose all parameters at once as fixed rational powers of $b$, then verify the size relations and the prime-interval hypotheses",
  "The layer, transform and resampling results each carry side conditions on the parameters; fixing the exponents together, with generous room, lets one check that all conditions hold for every large input length.",
  "explicit",
  [inf("S5.1.1", "The sizes satisfy $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$ and $r=2^{\\Theta(p^{1-\\epsilon})}$, with $t_i\\in\\{r/2,r\\}$ and $\\prod_it_i=T$.",
       "Take the power of two $T$ in $[4n/b,8n/b)$, and let",
       frm=["logarithms-floors-and-ceilings", "binary-representation-of-integers", "asymptotic-notation-omega-theta-and-little-o"]),
   inf("S5.1.2", "Distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ exist, so $T/2<S<T$ and each $\\theta_i=t_i/s_i-1$ satisfies the resampling hypothesis $\\alpha^4\\theta_i>p$.",
       "We may therefore choose distinct odd primes satisfying",
       frm=["prime-numbers", "greatest-common-divisor-and-the-euclidean-algorithm", "logarithms-floors-and-ceilings"])],
  page="parameter-choice",
  frm=["prime-numbers", "logarithms-floors-and-ceilings", "gaussian-resampling", "simultaneous-butterfly-layer", "synthetic-transform-layout"],
  mquote="The distinct prime lengths $s_i$ must be close to the powers of two",
  adds=[add("\\epsilon", "dimension exponent", "the tiny fixed exponent $2^{-75}$ with $d=\\lfloor b^\\epsilon\\rfloor$"),
        add("c", "chunk exponent", "the tiny fixed exponent $2^{-56}$ with $K=\\lfloor d^c\\rfloor$")])

S5 = show("S5",
  "The product of two $n$-bit integers is computed by converting the operands to radix-$2^b$ digit lists on a padded prime-axis box via $\\Phi$, applying the source transform to each, multiplying pointwise, applying the opposite transform, scaling by $S$ and $2^{2b+4}$, undoing $\\Phi$, rounding and propagating carries.",
  "Write the integer product as a convolution of radix digits, move it to a cyclic convolution on distinct prime axes by a Chinese-remainder address map, evaluate that convolution with Fourier transforms realised through resampling, a chirp convolution and a coefficient twist to a synthetic convolution, and read off the digits",
  "Multiplication of integers is polynomial multiplication in disguise; Fourier transforms turn convolution into pointwise products, and the preceding results supply fast transforms only on power-of-two axes, so each step of the reduction moves the problem closer to that shape.",
  "explicit",
  [S5_1,
   inf("S5.2", "Writing each operand as a polynomial in $2^b$ with $q=\\lceil n/b\\rceil$ digits makes the product coefficients a convolution, each below $2^{3b}$, with no wraparound modulo $x^S-1$ since $2q-2<S$.",
       "Write the two inputs as polynomials in $2^b$, each with",
       page="multiplication-by-convolution",
       frm=["binary-representation-of-integers", "polynomials", "cyclic-convolution", "schoolbook-binary-addition-with-carries", "divide-and-conquer-multiplication-karatsuba-toom-cook"]),
   inf("S5.3", "The map $\\Phi:x\\mapsto\\prod_ix_i^{\\mu_i}$ is an algebra isomorphism turning cyclic convolution of length $S=\\prod_is_i$ into a $d$-dimensional cyclic convolution on the prime axes, implemented by triangular controlled shifts and axis reordering.",
       "$\\Phi$ is an isomorphism and preserves cyclic convolution.",
       page="crt-address-map",
       frm=["chinese-remainder-theorem", "cyclic-convolution", "multidimensional-transform", "controlled-cyclic-shifts", "chunk-interchange", "modular-arithmetic-and-congruences"]),
   inf("S5.4", "The isomorphism $x\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ multiplies coefficient $k$ by $\\zeta^k$ and turns the negative wrap of $\\mathbb C[y]/(y^r+1)$ into the cyclic wrap, so normalized complex cyclic convolution $f*g/T$ is $\\mathcal M_r$ conjugated by the twist.",
       "multiplying coefficient $k$ by the nonzero number $\\zeta^k$.  It is therefore an",
       page="coefficient-twist",
       frm=["polynomial-ring-mod", "roots-of-unity", "complex-numbers", "multidimensional-transform"]),
   inf("S5.5", "The source transform applies the linewise map $\\mathcal A$, the computed chirp transform (twist, synthetic convolution, endpoint phases) and $\\mathcal B_0$, then scales by $2^\\gamma$, computing $RF_{\\boldsymbol s}$ with error below $E_s2^{-p}$.",
       "$\\widetilde{\\mathscr F}$ for the following procedure: apply the linewise",
       frm=["bluestein-chirp", "gaussian-resampling", "synthetic-convolution", "coefficient-twist"]),
   inf("S5.6", "Algorithm: map digits through $\\Phi$, transform both operands, multiply pointwise and truncate, apply the opposite transform, scale by $S$ and by $2^{2b+4}S$, round, undo $\\Phi$ and propagate carries.",
       "With these streams prepared, perform the following operations.",
       frm=["crt-address-map", "permutation-cancellation", "gaussian-resampling", "multiplication-by-convolution"])],
  page="multiplication-algorithm",
  frm=["cyclic-convolution", "multiplication-by-convolution", "synthetic-convolution", "gaussian-resampling"],
  mquote="Splitting the inputs into radix digits reduces multiplication to",
  adds=[add("b", "digit size", "the number of bits in each radix-$2^b$ digit, equal to $\\lceil\\log_2 n\\rceil$"),
        add("S", "prime-axis size", "the product of the pairwise coprime prime source lengths, the length of the cyclic convolution")])

# ---------------- S6 precision
S6 = show("S6",
  "The recovered convolution coefficients have absolute error below $1/2$, so rounding to nearest integers and propagating radix-$2^b$ carries output the exact $2n$-bit product.",
  "Track the scales and disk margins of every stage with contraction bounds, add the stage errors to bound the final error by $1/2$, then round and carry",
  "The algorithm computes only approximations to the true integer coefficients; a total error strictly below one half determines each integer uniquely, and errors of composed approximations add, so one can verify every stage's margin separately.",
  "explicit",
  [inf("S6.1", "Scales and disk margins: every intermediate array stays inside the unit disk with explicit norm bounds (for example $.5$, $.6$, $.701$), and the source transform has error below $E_sh_p$ with $E_s=9\\cdot2^\\gamma TL$.",
       "Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this",
       frm=["fixed-point-disk-arithmetic", "vector-norms-and-the-triangle-inequality", "permutation-cancellation"]),
   inf("S6.2", "The final absolute error is below $448b\\,2^{-3b/4}<1/2$, so the nearest integer to each represented coefficient is the unique correct coefficient.",
       "The strict error below $1/2$ makes the nearest integer to",
       frm=["fixed-point-disk-arithmetic", "permutation-cancellation"],
       salient="The accumulated error is exponentially small in $b$ ($2^{-3b/4}$ up to polynomial factors), far below the threshold $1/2$ needed to round exactly."),
   inf("S6.3", "Carries propagated in increasing coefficient order with $O(b)$ bits and steps per coefficient give the exact $2n$-bit product in most-significant-first order.",
       "After $\\Phi^{-1}$ the coefficients occur in increasing ordinary index,",
       frm=["schoolbook-binary-addition-with-carries", "binary-representation-of-integers"])],
  page="precision-exact-recovery",
  mquote="The strict error below $1/2$ makes the nearest integer to",
  frm=["fixed-point-disk-arithmetic", "permutation-cancellation", "vector-norms-and-the-triangle-inequality", "schoolbook-binary-addition-with-carries"])

# ---------------- S7 time
S7 = show("S7",
  "Dividing the costs of all stages by $Tp=\\Theta(n)$ gives normalized costs that are powers of $p$ at most $1-2\\kappa$, so the total is $O(n(\\lg n)^{1-\\kappa})$.",
  "Tabulate the normalized cost of every stage as a power of $p$, compare each power with $1$ through an explicit margin, and absorb setup costs and fixed powers of $\\log p$ into the slack",
  "A sum of costs each below $p^{1-2\\kappa}$ (times a fixed number of logarithmic factors absorbed by the slack) is $O(p^{1-\\kappa})$ per unit volume, so each stage's exponent only has to be compared with one.",
  "recoverable",
  [inf("S7.1", "The stages cost, per unit of $Tp$, $dK$, $pK^{\\tau-1}$, $\\ell d^{\\lambda'}$, $d^2(1+\\ell^\\tau)$, $dp^{1/2+\\delta}\\alpha$, $dp^\\delta$ and $\\log(rp)$, which are powers of $p$ listed in a table.",
       "Table~\\ref{tab:costs} lists costs after division",
       frm=["parameter-choice", "simultaneous-butterfly-layer", "chunk-interchange", "synthetic-transform-layout", "gaussian-resampling"]),
   inf("S7.2", "The seven dominant powers have margins $g_1,\\dots,g_7$ below one, the smallest being $g_2=\\epsilon c(1-\\tau)=2^{-181}=2\\kappa$.",
       "Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
       frm=["parameter-choice"],
       salient="The minimum margin $2^{-181}$ comes from the chunk-exchange row ($\\epsilon c(1-\\tau)=2^{-75}\\cdot2^{-56}\\cdot2^{-50}$), and $\\kappa=2^{-182}$ is half of it, an astronomically small but strictly positive power saving."),
   inf("S7.3", "Setup, prime search, descriptor work and the compact sorting of exceptional addresses across all calls cost $o(Tp)$.",
       "\\paragraph{Setup and exceptional streams across all calls.}",
       frm=["parameter-choice", "packed-selected-bit-addition"]),
   inf("S7.4", "Every dominant power is at most $1-2\\kappa$ and a fixed power of $\\log p$ is at most $p^\\kappa$ eventually, so the cost is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
       "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa}).",
       frm=["asymptotic-notation-omega-theta-and-little-o", "logarithms-floors-and-ceilings"])],
  page="time-bound-accounting",
  frm=["parameter-choice", "precision-exact-recovery", "multiplication-algorithm", "simultaneous-butterfly-layer", "chunk-interchange", "synthetic-transform-layout", "synthetic-convolution", "asymptotic-notation-omega-theta-and-little-o"])

S8 = inf("S8", "The bound holds through all input lengths, so $\\liminf_{n\\to\\infty}T_A(n)/(n\\lg n)=0$, which negates the eventual lower bound $T_A(n)\\ge c_An\\lg n$ of the optimality conjecture.",
         "The power saving proved here gives a limit of zero through all input lengths,",
         deferred=True, frm=["optimality-conjecture", "asymptotic-notation-omega-theta-and-little-o"])

root = show("S0",
  "One deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$, refuting the $n\\log n$ optimality conjecture in this model.",
  "Build two fast tape procedures (address interchange and simultaneous butterfly layers), run them inside synthetic transforms, reduce integer multiplication to such a convolution by resampling, chirps and a Chinese-remainder layout, then check precision and total up the time",
  "Scanning $\\Theta(n)$ stored bits at each of $\\Theta(\\log n)$ transform levels costs $\\Theta(n\\log n)$, so a power saving needs a faster way to move addresses and a faster way to do butterfly levels, both inside a multiplication reduction that still gives exact integers.",
  "explicit",
  [S1, S2, S3, S4, S5, S6, S7, S8],
  page="main-theorem",
  frm=["integer-multiplication-problem", "harvey-hoeven-multiplier", "optimality-conjecture", "big-o"],
  mquote="We therefore need savings in both movement and arithmetic.",
  salient="The saving is a power of the logarithm, $(\\lg n)^{1-\\kappa}$ with the tiny $\\kappa=2^{-182}$, and it arises with the same pattern twice: each of the two fast procedures comes from a linear network whose total rank is just below the trivial bound.",
  adds=[add("\\kappa", "power saving", "the fixed exponent $2^{-182}$ by which the logarithmic factor is reduced"),
        add("p", "precision", "the number of fractional bits kept in the real and imaginary part of each fixed-point complex number", "count"),
        add("d", "number of axes", "the number of power-of-two axes, equal to the dimension of the transform", "count"),
        add("T", "box size", "the number of entries of the padded power-of-two box, of order $n/\\log n$", "count")])

json.dump({"root": root}, open(sys.argv[1], "w"), indent=1)

# verify quotes
src = open("/home/user/openai-nlogn-wiki/runs/P2/sources/paper.tex").read()
lines = src.split("\n")
def walk(n, acc):
    if n["intention"] == "infer":
        acc.append(n)
    for c in n.get("children", []): walk(c, acc)
acc = []; walk(root, acc)
pos = 0; bad = False
for n in acc:
    q = n["quote"]["quote"]
    assert "\n" not in q
    i = src.find(q)
    if i < 0: print("MISSING", n["id"], q); bad = True; continue
    if n.get("deferred"): continue
    j = src.find(q, pos)
    if j < 0: print("OUT OF ORDER", n["id"], q); bad = True; continue
    pos = j + len(q)
print("bad" if bad else "ok")
