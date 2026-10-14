import json, sys, re

SRC = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/S6F4HH/sources/paper.tex"
OUT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/S6F4HH/exegenius/tasks/0003-argument.answer.json"

PAGES = ["integer-multiplication-conjecture", "polynomial-ring-mod", "fixed-point-truncation",
 "established-multiplier", "tape-address-model", "elementary-stream-ops", "controlled-shift",
 "linear-algebra-basics", "linear-network", "address-shear", "common-frame-principle",
 "subset-intersection-labels", "rank-saving-recurrence", "address-chunk-interchange",
 "packed-selected-bit-addition", "signed-packing", "cyclic-convolution", "radix-digit-convolution",
 "phase-twist", "exact-recovery", "dft", "multidimensional-dft", "butterfly", "synthetic-transform",
 "bluestein-chirp", "phase-frame-kernel", "fast-butterfly-layer", "ring-convolution",
 "gaussian-resampling", "permutation-cancellation", "crt-address-map", "parameter-choice",
 "multiplication-algorithm", "time-accounting", "main-theorem"]

def ev(q):
    return {"source": "paper", "quote": q}

def mot(text, source, q=None):
    return {"text": text, "source": source, "quote": (ev(q) if q else None)}

def B(symbol, name, meaning, relation):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

def infer(id_, claim, q, page=None, frm=None, deferred=False, adds=None):
    n = {"id": id_, "intention": "infer", "claim": claim, "quote": ev(q)}
    if page: n["page"] = page
    if frm: n["from"] = frm
    if deferred: n["deferred"] = True
    if adds: n["adds"] = adds
    return n

def show(id_, claim, method, motivation, children, page=None, frm=None, salient=None, adds=None):
    n = {"id": id_, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children}
    if page: n["page"] = page
    if frm: n["from"] = frm
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n

# ---------------- root ----------------
root_adds = [
 B("n", "input length", "the bit length of each of the two input integers", "count"),
 B(r"\kappa", "saving exponent", "the fixed exponent $\\kappa=2^{-182}$, so the bound is $n(\\lg n)^{1-\\kappa}$", "direct"),
 B("b", "digit bits", "the number of bits per radix digit, $b=\\lceil\\log_2 n\\rceil$", "count"),
 B("p", "precision", "the working precision in fractional bits, $p=6b$", "count"),
 B("r", "record length", "the number of complex coefficients in a polynomial record, a power of two", "count"),
 B(r"\ell", "record exponent", "the base-two logarithm $\\ell=\\log_2 r$ of the record length", "direct"),
 B("T", "padded size", "the size of the padded power-of-two box, $T\\in[4n/b,8n/b)$", "count"),
 B("S", "prime product", "the product $S=\\prod_i s_i$ of the distinct prime source lengths", "count"),
 B("V", "volume", "the stored bit volume $V=Tp=\\Theta(n)$ of the padded arrays", "count"),
 B(r"\alpha", "Gaussian width", "the integer Gaussian width parameter with $2\\le\\alpha<\\sqrt p$", "direct"),
 B(r"\gamma", "source scale exponent", "the scaling exponent $\\gamma=2d\\alpha^2$ of the source transform", "direct"),
]

conj = show("R.1",
 "The bound is of smaller order than $n\\log n$, so it refutes the conjecture that $n\\log n$ is optimal in this model.",
 "compare the bound with the conjectured $n\\log n$ order",
 mot("The conjecture takes $n\\log n$ to be the optimal order, so a bound of smaller order refutes it.", "recoverable"),
 [infer("R.1.1",
   "The algorithm disproves the $n\\log n$ optimality conjecture of Schönhage and Strassen in this model.",
   "disproves the $n\\log n$ optimality conjecture", ),],
 page="integer-multiplication-conjecture")

# ---------------- key: tape procedures save a power ----------------
key_adds = [
 B("W", "wire count", "the number of wires of a finite linear network", "count"),
 B("m", "label dimension", "the dimension of the label space $\\mathcal F=F^{\\otimes 3}$, with $m=h^3$ and $h=100$", "count"),
 B("s", "rank total", "the sum of the ranks of the edge changes of a network", "count"),
 B(r"\tau", "bit exponent", "the fixed rational exponent $\\tau=1-2^{-50}$ with $s/W<m^\\tau$ for the bit network", "direct"),
 B(r"\lambda'", "layer exponent", "the fixed exponent $\\lambda'<1$ of the simultaneous butterfly layer", "direct"),
 B("d", "axis count", "the number of selected axes of a butterfly layer, $d=\\Theta(p^{\\epsilon})$", "count"),
 B("K", "chunk bits", "the width in bits of each address chunk of a layer, $K=\\lfloor d^c\\rfloor$", "count"),
 B("N", "source rank", "the total source dimension of the two data banks", "count"),
 B("L", "lost rank", "the total dimension lost on decreasing edges of a network", "count"),
]

n_linear = show("R.2.1",
 "A fixed network of linear gates exchanges two banks of values with prescribed signs and restores every scratch wire, for arbitrary initial scratch values.",
 "run three stages of copy, gather, scatter and side-injection gates, so that each auxiliary value is cancelled and then restored",
 mot("The scratch values are arbitrary, so each auxiliary wire must be cancelled by a schedule that undoes its own update.", "recoverable"),
 [infer("R.2.1.1",
   "A forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged, for arbitrary initial auxiliary values.",
   "invocation changes $y_S$ to $y_S+x_S$ and leaves every other value"),
  infer("R.2.1.2",
   "Each invocation restores its own auxiliary wires, so the three stages send $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restore every auxiliary value.",
   "Each invocation restores its own auxiliary wires.")],
 page="linear-network", frm=["linear-algebra-basics"])

n_frame = show("R.2.2",
 "Every edge changes the stored array by $D_vD_u^{-1}$, and the common frame commutes with each pointwise gate, so only the endpoint frames determine the operator on each route.",
 "attach an invertible frame to each vertex, check that a common frame passes through each pointwise gate, and telescope the intermediate frames",
 mot("A common frame passes through each linear gate, so the intermediate frames cancel along a route.", "recoverable"),
 [infer("R.2.2.1",
   "A common frame commutes with a pointwise linear gate: $G(D_vg_1,\\ldots,D_vg_t)=D_vG(g_1,\\ldots,g_t)$.",
   "Thus the common frame commutes with the pointwise gate, and"),
  infer("R.2.2.2",
   "A signed role permutation sends input role $w$ to output role $\\rho(w)$ by the endpoint operator $\\varepsilon_wD_{\\mathrm{sink}(\\rho(w))}D_{\\mathrm{source}(w)}^{-1}$.",
   "In particular, if the scalar network is a signed role permutation that")],
 page="common-frame-principle", frm=["linear-algebra-basics", "linear-network"])

n_labels = show("R.2.3",
 "Subspaces spanned by indicators of three-element subsets satisfy $\\langle t_S,t_T\\rangle=|S\\cap T|-1$, and the signed dimension changes of all edges sum to $Wm-2N$.",
 "label each gate and terminal by a nested subspace spanned by triple indicators, then telescope the dimension changes at each gate",
 mot("The gather and scatter coefficients depend on intersection sizes, and triple indicators are orthogonal in the right way, so the labels can be nested.", "recoverable"),
 [infer("R.2.3.1",
   "Triple indicators satisfy $\\langle t_S,t_T\\rangle=|S\\cap T|-1$, which makes neighboring labels nested and nondegenerate.",
   r"\langle t_S,t_T\rangle=|S\cap T|-1,"),
  infer("R.2.3.2",
   "The signed dimension changes sum to $Wm-2N$, because each gate has equal incoming and outgoing label dimensions.",
   "Thus the signed dimension changes will sum to $Wm-2N$, because the"),
  infer("R.2.3.3",
   "Only the central return from time $3$ to time $4$ decreases a label, losing $L$ in total, so the sum of absolute changes is $Wm-2N+2L$.",
   "Label dimension is nondecreasing along every edge except center $3\\to4$, which removes")],
 page="subset-intersection-labels", frm=["linear-algebra-basics", "common-frame-principle", "linear-network"])

n_rank = show("R.2.4",
 "The total rank change of each network is below $Wm$, so the average change per wire is $s/W<m^{\\tau}$ for the bit network and $s/W<m^{\\sigma}$ for the complex network.",
 "compare the sum of the ranks of the edge differences with the wire count times the label dimension, and bound the loss of the decreasing edges",
 mot("The saving will come from keeping the total dimension lost on decreasing edges small relative to $N$.", "explicit",
     "The saving will come from keeping the total dimension lost on decreasing"),
 [infer("R.2.4.1",
   "The loss ratios are $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$, both below $1/2$.",
   "In particular, both are smaller than $1/2$."),
  infer("R.2.4.2",
   "The sum of the rational ranks of the bit network's edge differences is $s=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$.",
   "The sum of the rational ranks of all edge differences is"),
  infer("R.2.4.3",
   "The deficit $Wm-s$ equals $N-2L$, which is positive because $L<N/2$.",
   "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$."),
  infer("R.2.4.4",
   "The bit network satisfies $s/W<m^{\\tau}$ with $\\tau=1-2^{-50}$.",
   r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,"),
  infer("R.2.4.5",
   "The complex network satisfies $s/W<m^{\\sigma}$ with $\\sigma=\\tau$.",
   r"\frac{s_{\rm c}}{W_{\rm c}}<m^\sigma,")],
 page="rank-saving-recurrence", frm=["linear-network", "subset-intersection-labels", "linear-algebra-basics"],
 salient="the average rank change per wire is below the label dimension $m$, a bound that does not grow with the number of wires $W$",
 adds=[B(r"\sigma", "complex exponent", "the fixed exponent of the complex network, $\\sigma=\\tau=1-2^{-50}$", "direct")])

n_shear = show("R.2.5",
 "The shear $(H,D)\\mapsto(H+AD,D)$ for a rational matrix $A$ of rank $a$ costs exactly $a$ pair interchanges plus linear work.",
 "factor $A=E_1\\Pi E_2$ with lower-triangular $E_1,E_2$, and realize each one of $\\Pi$ by one interchange",
 mot("Lower-triangular updates are linear-time, so only the permutation part of the factorization costs interchanges.", "recoverable"),
 [infer("R.2.5.1",
   "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$, with $E_1,E_2$ lower triangular and $\\Pi$ having $a$ ones.",
   "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"),
  infer("R.2.5.2",
   "Each one of $\\Pi$ at position $(i,j)$ calls for one update $H_i\\leftarrow H_i+D_j$.",
   "Each one in position $(i,j)$ of $\\Pi$ calls for"),
  infer("R.2.5.3",
   "The sequence $D_j\\leftarrow D_j+H_i$, swap, $D_j\\leftarrow H_i-D_j$ realizes the update with one interchange.",
   "It uses just one interchange.")],
 page="address-shear", frm=["controlled-shift", "linear-algebra-basics"])

n_chunk = show("R.2.6",
 "Two disjoint contiguous chunks of $u$ bits are interchanged in $O(Vu^{\\tau})$ time with $\\tau<1$, because each shear costs $a$ smaller interchanges and the recursion sums to a power of the chunk width.",
 "build the chunk swap from three shears, implement each shear on the bit network as $s$ smaller calls on volume $V/W$, and unroll the recursion",
 mot("An edge matrix of rank $a$ will require $a$ smaller interchanges, so the recursion saves a power of the chunk width.", "explicit",
     "An edge matrix of rank $a$ will require $a$ smaller interchanges."),
 [infer("R.2.6.1",
   "Two equal chunks of $e=m^k$ digits can be interchanged in $O(Ve^{\\tau})$ time.",
   "The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every"),
  infer("R.2.6.2",
   "Three componentwise shears interchange $H$ and $D$, and only the middle one uses the circuit.",
   r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,"),
  infer("R.2.6.3",
   "The number of recursive calls is the sum of the edge ranks, which is $s$.",
   "The number of recursive calls is the sum of the edge ranks, exactly $s$."),
  infer("R.2.6.4",
   "The volume-normalized cost satisfies $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
   r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."),
  infer("R.2.6.5",
   "Since $s/W<m^{\\tau}$, the geometric sum gives $F_k=O(e^{\\tau})$.",
   "Hence $F_k=O(e^\\tau)$."),
  infer("R.2.6.6",
   "An interchange of arbitrary-width chunks of $u$ bits costs $O(Vu^{\\tau})$, with $V=PGB\\,2^{2u}$.",
   "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.")],
 page="address-chunk-interchange", frm=["tape-address-model", "elementary-stream-ops", "controlled-shift", "linear-algebra-basics", "address-shear", "rank-saving-recurrence"],
 salient="the cost per unit of volume is a power $u^{\\tau}$ of the chunk width with $\\tau<1$, not linear in $u$",
 adds=[B("e", "digit chunk", "the chunk width in radix digits, $e=m^k$", "count"),
       B("u", "bit chunk", "the chunk width in bits", "count")])

n_cplx_kernel = show("R.2.7",
 "Each edge of the complex network changes the phase frame by a product of two-point kernels $C$, one for each direction of the residual basis.",
 "write each residual direction as a Hamming-weight phase, turn it into a two-point kernel on one coordinate, and place the directions on coordinates by a change of basis",
 mot("Phase identities turn a frame change into products of two-point kernels, and a change of basis puts those kernels on coordinate directions.", "recoverable"),
 [infer("R.2.7.1",
   "The phase-frame difference $\\mathcal C_{U_+}\\mathcal C_{U_-}^{-1}$ of an edge is a product of kernels $C$, one for each residual direction.",
   "Proposition~\\ref{prop:complex-motif-interface} gives the frame change"),
  infer("R.2.7.2",
   "The inverse kernel costs one forward child, because $C^{-1}=-iZCZ$ with $Z=\\mathrm{diag}(1,-1)$.",
   "A negative directional kernel still requires only one"),
  infer("R.2.7.3",
   "Gaussian elimination writes any $M\\in\\operatorname{GL}(m,\\mathbb F_2)$ as a constant number of row additions, so the change of basis costs a fixed number of packed operations.",
   "Gaussian elimination expresses any $M\\in\\operatorname{GL}(m,\\mathbb F_2)$")],
 page="phase-frame-kernel", frm=["linear-algebra-basics", "common-frame-principle", "rank-saving-recurrence", "packed-selected-bit-addition"],
 adds=[B("C", "two-point kernel", "the two-point kernel $C=H\\mathsf SH=aI+bX$ with $a=(1+i)/2$ and $b=(1-i)/2$", "direct")])

n_packed = show("R.2.8",
 "A binary row addition $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$ on $f$ selected bits of two $K$-bit chunks is performed in $O(V((fK)^{\\tau}+1))$ time, restoring the third chunk, by eight cyclic shifts and a deterministic repair.",
 "apply eight chunk-wide cyclic shifts whose segments cannot carry into each other, except at a small exceptional set of addresses, then repair that set by a sort",
 mot("The construction first uses a constant number of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of addresses.", "explicit",
     "then corrects an explicitly bounded set of"),
 [infer("R.2.8.1",
   "Each guarded line either does nothing or moves a guard pair, so the eight operations act as a cycle on each square.",
   "If $c=0$, these operations do nothing. If $c=1$, the first four operations"),
  infer("R.2.8.2",
   "The composed operations give $(u',w')=(u+c(1-2(u\\bmod 2)),w)$, so the third chunk is restored.",
   "Consequently the complete output is"),
  infer("R.2.8.3",
   "Exactly twenty guard values are excluded per guard, so the exceptional fraction is at most $80(f-1)2^{-K}$.",
   "There are exactly twenty excluded values for each guard in"),
  infer("R.2.8.4",
   "The chunk swaps, rotations and sorting of the exceptional set together cost $O(V((fK)^{\\tau}+1))$.",
   "The movement costs $O(V(L^\\tau+1))$.")],
 page="packed-selected-bit-addition", frm=["elementary-stream-ops", "controlled-shift", "address-chunk-interchange", "tape-address-model"],
 adds=[B("f", "selected bits", "the number of selected bit positions of a packed addition, $f\\le d$", "count")])

n_fast = show("R.2.9",
 "A simultaneous normalized butterfly layer on $D\\le d$ selected bits costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, and its output is truncated once after an exact guarded evaluation.",
 "split the selected axes into $m$ slots, apply $s$ child layers on $e/m$ axes, unroll the recursion, and truncate once after the exact layer",
 mot("Separate butterfly factors would need $D$ whole-array passes, whereas one packed layer costs a power of $d$.", "explicit",
     "factors would require $D$ whole-array passes."),
 [infer("R.2.9.1",
   "Per unit volume, the layer cost satisfies $F(e)\\le (s/W)F(e/m)+O((eK)^{\\tau}+1)$ for $e$ axes.",
   r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
  infer("R.2.9.2",
   "Dividing the child cost by the current volume gives the factor $s/W$, which is below $m^{\\tau}$.",
   r"the current volume \(V\) gives the factor \(s/W\)."),
  infer("R.2.9.3",
   "Summing the levels and the groups gives $O(d^{\\lambda'})$ for a fixed $\\lambda'<1$ above the exponents $\\lambda$ and $\\sigma+\\tfrac12(1-\\sigma)$.",
   "=O(d^{\\lambda'})"),
  infer("R.2.9.4",
   "The guard width is controlled by $E=64(W+m+1)^3$ and $B=s+E$, so intermediate coefficients are exact in $O(p)$ bits.",
   r"E=64(W+m+1)^3,\qquad B=s+E,"),
  infer("R.2.9.5",
   "The layer returns $Q_p(\\mathcal H z)$ in $O(Vd^{\\lambda'})$ time.",
   "in $O(Vd^{\\lambda'})$ time,")],
 page="fast-butterfly-layer", frm=["fixed-point-truncation", "address-chunk-interchange", "packed-selected-bit-addition", "phase-frame-kernel", "rank-saving-recurrence"],
 salient="the layer costs $d^{\\lambda'}$ per unit volume, a power below one of the number of axes, instead of $d$ whole-array passes",
 adds=[B("E", "guard constant", "the guard constant $E=64(W+m+1)^3$ bounding the arithmetic depth", "direct"),
       B("B", "guard bound", "the depth bound $B=s+E$ for the layer recursion", "direct")])

key = show("R.2",
 "Each tape procedure costs a power with exponent $\\tau$ or $\\lambda'$ below one per unit volume, because its finite network has total rank change $s<Wm$.",
 "count the rank change of a fixed linear network with restored scratch wires, implement each edge change by smaller calls on streams of volume $V/W$, and unroll the recursion",
 mot("An edge matrix of rank $a$ will require $a$ smaller interchanges, and the sum of the ranks is below $Wm$, so the recurrence saves a power.", "explicit",
     "the resulting recurrence saves a power of the chunk width."),
 [n_linear, n_frame, n_labels, n_rank, n_shear, n_chunk, n_cplx_kernel, n_packed, n_fast],
 adds=key_adds)

# ---------------- pipeline ----------------
n_deferred = infer("R.3.1",
 "The digit sums obey $2q-2<2n/b\\le T/2<S$, so the cyclic convolution modulo $x^S-1$ has no wraparound.",
 r"2q-2<2n/b\le T/2<S.", deferred=True)

n_syn = show("R.3.2",
 "The synthetic transform has entries in $\\mathcal R_r$, and its roots $\\omega_t=y^{2r/t}$ act as signed shifts, so both transforms are contractions.",
 "radix-two decimation-in-frequency rounds with monomial twiddles, leaving the output in bit-reversed order",
 mot("Roots of unity in the polynomial ring act as signed permutations of coefficients, so only butterflies and shifts are needed.", "recoverable"),
 [infer("R.3.2.1",
   "Define $\\omega_t=y^{2r/t}$ for each transform length $t$ dividing $2r$.",
   r"For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$."),
  infer("R.3.2.2",
   "Both transforms $F_t^{\\pm}$ are contractions, since each entry averages $t$ isometric images.",
   "Thus both transforms are contractions."),
  show("R.3.2.3",
   "The two-point averaging $H_0(u,v)=((u+v)/2,(u-v)/2)$ is the round from which the transform is built, pairing entries $k$ and $k+t/2$.",
   "decimation in frequency: one averaging round, then transforms of half length in the two branches",
   mot("A power-of-two transform is built from averaging rounds, so the two-point butterfly is the basic step.", "recoverable"),
   [infer("R.3.2.3.1",
     "The length-one transform is the identity, and each round pairs $z_k$ with $z_{k+t/2}$.",
     "The length-one procedure is the identity."),
    infer("R.3.2.3.2",
     "The two outputs of $H_0$ occupy the slots with high bit $0$ and $1$, and the second is multiplied by $\\omega_t^{-k}$.",
     "The two outputs of $H_0$ occupy these same slots,")],
   page="butterfly", frm=["dft"],
   adds=[B("H_0", "averaging butterfly", "the two-point averaging map $H_0(u,v)=((u+v)/2,(u-v)/2)$", "direct")]),
  infer("R.3.2.4",
   "After $a=\\log_2 t$ rounds the stored frequency order is bit-reversed, so the record permutation $B_t$ sends entry $j$ to $\\operatorname{rev}_a(j)$.",
   "After all $a$ rounds, the named slots from high to low therefore"),
  infer("R.3.2.5",
   "The $D$-axis transform is the tensor product $F_{\\boldsymbol t}^{\\pm}=\\bigotimes_i F_{t_i}^{\\pm}$ of one-dimensional transforms.",
   "For $D$ axes of lengths $t_1,\\ldots,t_D$, put")],
 page="synthetic-transform", frm=["polynomial-ring-mod", "fixed-point-truncation", "multidimensional-dft"],
 adds=[B(r"\omega_t", "synthetic root", "the root of unity $y^{2r/t}$ of order $t$ in the polynomial ring", "direct"),
       B("t", "transform length", "the length of a synthetic transform, a power of two dividing $2r$", "count")])

n_ring = show("R.3.3",
 "Normalized convolution over $\\mathcal R_r$ on the $d-1$ power-of-two axes gives $\\mathcal M_r(f,g)=(f*g)/T$, computed by two forward synthetic transforms, a pointwise signed-packed product and the opposite transform.",
 "transform along the axes, multiply pointwise with the established multiplier through signed packing, and transform back in the retained order",
 mot("The forward and opposite transforms share one record order, so the pointwise product needs no sort between them.", "recoverable"),
 [infer("R.3.3.1",
   "The layout permutation $L$ and the synthetic transform cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$, with error $\\sqrt2\\,\\ell 2^{-p}$.",
   "Both layout construction and final restoration are charged in this"),
  show("R.3.3.2",
   "Signed packing turns the product of two ring elements into one integer product of $O(rp)$ bits, and centered residues with carries recover the coefficients in $O(rp\\log(rp))$ time.",
   "evaluate the coefficient polynomials at $B_{\\rm pk}=2^{4p}$, multiply the packed integers with the established multiplier, and read the coefficients back by centered residues",
   mot("A base large enough to separate every coefficient of the product lets one integer product carry the whole ring product.", "recoverable"),
   [infer("R.3.3.2.1",
     "Each evaluation integer fits in $4pr$ bits.",
     "shows that each magnitude fits in $4pr$ bits."),
    infer("R.3.3.2.2",
     "Each coefficient of the ordinary product satisfies $|h_j|\\le r2^{2p}<2^{3p}<B_{\\rm pk}/2$, so its centered residue is itself.",
     r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2.")],
   page="signed-packing", frm=["established-multiplier", "polynomial-ring-mod"],
   adds=[B(r"B_{\rm pk}", "packing base", "the base $2^{4p}$ at which the coefficient polynomials are evaluated", "direct")]),
  infer("R.3.3.3",
   "The two forward transforms share the record order $LB$, so their pointwise product lies in that order.",
   "Perform both forward transforms and retain their common $LB$ order."),
  infer("R.3.3.4",
   "The opposite transform of the product is multiplied by $M=T/r$, which gives $\\mathcal M_r(f,g)=(f*g)/T$.",
   "multiply its result exactly by $M=T/r$.")],
 page="ring-convolution", frm=["polynomial-ring-mod", "fixed-point-truncation", "synthetic-transform", "fast-butterfly-layer"])

n_gauss = show("R.3.4",
 "Resampling expresses a length-$s$ transform through a power-of-two transform of length $t>s$, with the permutations kept in the formula: $RF_{\\boldsymbol s}=2^{\\gamma}\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$.",
 "express each coordinate line through Gaussian-weighted contractions, then tensor the one-dimensional identity over the $d$ axes",
 mot("Gaussian resampling connects the pairwise coprime lengths of the integer product with the power-of-two shapes of the synthetic transforms.", "explicit",
     "connects these two shapes."),
 [infer("R.3.4.1",
   "There are linear contractions $A$ and $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$.",
   r"There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and"),
  infer("R.3.4.2",
   "Tensoring the one-dimensional identity gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$.",
   r"Tensoring \eqref{eq:no-sort-one-dimensional} proves"),
  infer("R.3.4.3",
   "Each axis invokes at most $2dT/r$ lines, so exposing and restoring the lines costs $O(Tp\\,d^2(1+\\ell^\\tau))$.",
   r"Since $t_i\geq r/2$, each tensor map invokes at most")],
 page="gaussian-resampling", frm=["dft", "multidimensional-dft", "fixed-point-truncation", "established-multiplier"])

n_chirp = show("R.3.5",
 "With the chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$, the transform satisfies $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$, a normalized cyclic convolution.",
 "write the transform kernel as a chirp, so each coefficient is a product of two chirps around a cyclic convolution",
 mot("The exponent is quadratic in each index, so the kernel factors into chirps that a cyclic convolution can absorb.", "recoverable"),
 [infer("R.3.5.1",
   "Shifting $j_i$ by $t_i$ changes the exponent of $a$ by a multiple of $2\\pi i$, so $a$ has period $t_i$.",
   "Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by"),
  infer("R.3.5.2",
   "The coefficient of $u_{\\boldsymbol k}$ on the right side is that of $QF_{\\boldsymbol t}$, which proves the chirp identity.",
   "This is precisely the coefficient in $QF_{\\boldsymbol t}$, because")],
 page="bluestein-chirp", frm=["dft", "multidimensional-dft", "cyclic-convolution"],
 adds=[B("a", "chirp array", "the chirp array $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_i j_i^2/t_i)$", "direct")])

n_perm = show("R.3.6",
 "The retained source permutation cancels: $RF_{\\boldsymbol s}^+[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
 "commute the coordinate permutation through the transform by unit multiplications, then apply the convolution rule with its two normalizations",
 mot("The coordinate permutation commutes with pointwise products and with the transform up to the inverse unit map.", "recoverable"),
 [infer("R.3.6.1",
   "Since each $t_i$ is a unit modulo $s_i$, $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$.",
   r"$RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$. Also"),
  infer("R.3.6.2",
   "The two normalizations combine to $F_{\\boldsymbol s}^+(F_{\\boldsymbol s}u\\cdot F_{\\boldsymbol s}v)=(u*v)/S^2$.",
   r"proving \eqref{eq:source-permutation-cancel}.")],
 page="permutation-cancellation", frm=["dft", "bluestein-chirp", "gaussian-resampling"])

n_params = show("R.3.7",
 "The sizes $b=\\lceil\\log_2 n\\rceil$, $p=6b$ and $d=\\lfloor b^{\\epsilon}\\rfloor$, with a power of two $T\\in[4n/b,8n/b)$, yield distinct primes $s_i$ near $t_i$ with $T/2<S<T$, so the resampling hypotheses hold.",
 "fill the padded box with powers of two $t_i\\in\\{r/2,r\\}$, then pick distinct primes just below each $t_i$ by the prime-interval bound",
 mot("The prime source lengths must multiply to a fixed fraction of the padded box, while each ratio $t_i/s_i$ leaves room for resampling.", "recoverable"),
 [infer("R.3.7.1",
   "Take a power of two $T\\in[4n/b,8n/b)$ and $r=2^{\\lceil(\\log_2 T)/d\\rceil}$, so the axis lengths $t_i\\in\\{r/2,r\\}$ have product $T$.",
   "Take the power of two $T$ in $[4n/b,8n/b)$, and let"),
  infer("R.3.7.2",
   "The primes $s_i$ satisfy $T/2<S<T$, so the convolution modulo $x^S-1$ fits the padded box.",
   "Together with $s_i<t_i$, this gives $T/2<S<T$.")],
 page="parameter-choice", frm=["established-multiplier", "gaussian-resampling", "primes-coprimality-and-gcd"],
 adds=[B(r"\epsilon", "dimension exponent", "the fixed exponent $\\epsilon=2^{-75}$ with $d=\\lfloor b^{\\epsilon}\\rfloor$", "direct")])

n_radix = show("R.3.9",
 "Writing each $n$-bit input as a polynomial in $2^b$ with $q$ digits gives a product whose coefficients are below $2^{3b}$.",
 "write the inputs as polynomials in $2^b$, then bound each product coefficient by the number of digit pairs",
 mot("Splitting the inputs into radix digits reduces multiplication to convolution of short coefficients.", "recoverable"),
 [infer("R.3.9.1",
   "The two inputs are polynomials in $2^b$, each with $q=\\lceil n/b\\rceil$ digits.",
   "Write the two inputs as polynomials in $2^b$, each with"),
  infer("R.3.9.2",
   "Each product coefficient satisfies $0\\le c_j\\le q(2^b-1)^2<2^{3b}$.",
   r"0\le c_j\le q(2^b-1)^2<2^{3b},")],
 page="radix-digit-convolution", frm=["cyclic-convolution"],
 adds=[B("q", "digit count", "the number of radix-$2^b$ digits of each input, $q=\\lceil n/b\\rceil$", "count")])

n_crt = show("R.3.8",
 "The map $\\Phi:x\\mapsto\\prod_i x_i^{\\mu_i}$ is an algebra isomorphism from $\\mathbb C[x]/(x^S-1)$ onto the product of prime-length group algebras, so it preserves cyclic convolution.",
 "use the Agarwal–Cooley isomorphism, and realize the change of order by triangular controlled shifts on the padded axes",
 mot("Distinct prime axes turn one long cyclic convolution into a multidimensional one whose axes can be reordered by controlled shifts.", "recoverable"),
 [infer("R.3.8.1",
   "$\\Phi$ respects $x^S=1$, so it defines an algebra map.",
   "respects $x^S=1$, so it defines an algebra map."),
  infer("R.3.8.2",
   "$\\Phi$ is an isomorphism and preserves cyclic convolution.",
   "$\\Phi$ is an isomorphism and preserves cyclic convolution."),
  infer("R.3.8.3",
   "The $i$th coordinate of $\\Phi(x^k)$ is $a_i+\\mu_i\\sum_{j<i}a_jP_j \\pmod{s_i}$, because $\\mu_iP_i=1$ modulo $s_i$ for the prefix product $P_i$.",
   "Indeed terms with $j>i$ are divisible by $s_i$, and $\\mu_iP_i=1$ modulo"),
  infer("R.3.8.4",
   "Each triangular update is a prefix-controlled cyclic shift, costing $O(V)$.",
   "Each triangular update is a prefix-controlled cyclic shift.")],
 page="crt-address-map", frm=["controlled-shift", "elementary-stream-ops", "tape-address-model", "cyclic-convolution", "address-chunk-interchange"],
 adds=[B("P_i", "prefix product", "the prefix product $P_i=\\prod_{j<i}s_j$ of the source lengths", "direct"),
       B(r"\mu_i", "inverse residue", "the inverse $\\mu_i=P_i^{-1}\\bmod s_i$", "direct")])

n_twist = show("R.3.10",
 "The map $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ is an isomorphism from $\\mathbb C[x_d]/(x_d^r-1)$ onto $\\mathbb C[y]/(y^r+1)$, and untwisting restores the cyclic wrap.",
 "multiply coefficient $k$ by $\\zeta^k$, so the negative wrap of the ring becomes the cyclic wrap after untwisting",
 mot("A twist by powers of a root of order $2r$ converts the cyclic last coordinate into a negacyclic one without changing norms.", "recoverable"),
 [infer("R.3.10.1",
   "The map $\\Theta$ is well defined, since $(\\zeta y)^r=1$.",
   "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$."),
  infer("R.3.10.2",
   "A product term after twisting and negacyclic reduction has factor $\\zeta^{k+l}(-1)^h=\\zeta^j$.",
   "For an explicit check on the wrap, write $k+l=j+hr$, where"),
  infer("R.3.10.3",
   "Untwisting recovers the cyclic coefficient with the correct sign.",
   "Untwisting therefore recovers the cyclic coefficient with the correct")],
 page="phase-twist", frm=["polynomial-ring-mod", "cyclic-convolution"],
 adds=[B(r"\zeta", "twist root", "the root $\\zeta=e^{\\pi i/r}$ of order $2r$ used to twist the last coordinate", "direct")])

n_cconv = show("R.3.11",
 "The computed complex convolution, chirp transform and source transform are exact up to a fixed error and map disk arrays to disk arrays.",
 "compute each phase product exactly before one truncation, and insert the exact contractions at each computed input",
 mot("Each computed stage is an exact map plus one controlled error, so the errors of the stages add.", "recoverable"),
 [infer("R.3.11.1",
   "Each phase product is exact before a single truncation.",
   "Each phase product is computed exactly as a dyadic product before"),
  infer("R.3.11.2",
   "The chirp transform uses the kernel $\\widetilde a$ and data $x_0=Q_p(\\overline{\\widetilde a}\\cdot x)$.",
   "Thus $\\widetilde a$ is the convolution kernel and $x_0$ is the data"),
  infer("R.3.11.3",
   "Replacing the approximations by exact phases and exact convolution gives $QF_{\\boldsymbol t}x$.",
   "by exact phases and exact convolution gives"),
  infer("R.3.11.4",
   "The source transform has exact counterpart $2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$.",
   "Here an exact counterpart replaces every numerical subroutine by the")])

n_steps = show("R.3.12",
 "Six steps compute the address map, three source transforms, the pointwise product, the opposite transform with its rescaling, the rounding, and then the carries.",
 "apply the address map and two source transforms, multiply pointwise, run the opposite transform and rescale by $S$ and $2^{2b+4}$, round, and propagate carries",
 mot("Each step applies one of the exact or approximate maps above in the order the convolution identity requires.", "recoverable"),
 [infer("R.3.12.1",
   "Three source-transform calls supply the transforms needed for the radix-digit convolution.",
   "The source-transform procedures now supply the three transforms needed"),
  infer("R.3.12.2",
   "The address map $\\Phi$ gives source arrays $u,v$ of norm less than $1/4$.",
   "Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain"),
  infer("R.3.12.3",
   "The pointwise product of the transforms is truncated to $p$ fractional bits, giving $z$.",
   "Multiply corresponding complex coefficients exactly and truncate"),
  infer("R.3.12.4",
   "The opposite transform of $z$ is scaled by $S$, giving an approximation of $w=(u*v)/S$.",
   "Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid"),
  infer("R.3.12.5",
   "The two scalings by $S$ and $2^{2b+4}$ undo the normalizations, so the scaled array is the integer convolution.",
   "The two occurrences of $S$ in this algorithm undo different")])

n_recover = show("R.3.13",
 "Rounding and carry propagation recover the exact $2n$-bit product from the approximate coefficients.",
 "bound the final coefficient error below $1/2$, round to the nearest integers, and propagate radix-$2^b$ carries",
 mot("The error bound is what turns an approximation into exact integer coefficients.", "recoverable"),
 [infer("R.3.13.1",
   "The final coefficient error is below $448b\\,2^{-b+\\gamma}<1/2$.",
   "Since $S\\le T<2^b$ and $L<b$ eventually, the final absolute error is less than"),
  infer("R.3.13.2",
   "Rounding $H_j/2^p$ to the nearest integer recovers each coefficient exactly.",
   "The strict error below $1/2$ makes the nearest integer to"),
  infer("R.3.13.3",
   "Radix-$2^b$ carries in increasing coefficient order give the $2n$-bit product.",
   "To propagate carries, let $Q_0=2^b$.")])

pipe = show("R.3",
 "The algorithm computes the exact $2n$-bit product: it reduces to a cyclic convolution of radix digits, evaluates it by source transforms, a pointwise product and the opposite transform, and then rounds and propagates carries.",
 "reduce to convolution by radix digits and a CRT address map, compute the convolution by Gaussian resampling with chirps and polynomial-ring products, then recover the integers by rounding and carries",
 mot("Each reduction preserves the convolution, so their composition computes the product once the coefficients are recovered exactly.", "recoverable"),
 [n_deferred, n_syn, n_ring, n_gauss, n_chirp, n_perm, n_params, n_radix, n_crt, n_twist, n_cconv, n_steps, n_recover],
 page="multiplication-algorithm", frm=["exact-recovery", "cyclic-convolution"])

# ---------------- cost ----------------
cost = show("R.4",
 "Each cost term, divided by $V=Tp$, is a power $p^{\\theta}$ with $\\theta\\le 1-2\\kappa$, so the total is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
 "divide every cost by $V=Tp$, bound each of seven dominant powers of $p$ by $1-2\\kappa$, and absorb the remaining powers of $\\log p$",
 mot("Every term of the cost is a fixed power of $p$ times $V$, so the largest exponent decides the bound.", "recoverable"),
 [infer("R.4.1",
   "The seven dominant powers of $p$ in the cost table have margins $g_1,\\ldots,g_7$ below one.",
   "The seven dominant powers in Table~\\ref{tab:costs} have the following"),
  infer("R.4.2",
   "Each margin satisfies $g_i\\ge 2\\kappa$, so $\\min_i g_i=2\\kappa$.",
   "Thus $\\min_i g_i=2^{-181}=2\\kappa$.  This explicit slack will cover"),
  infer("R.4.3",
   "Hence each of the seven powers is at most $1-2\\kappa$.",
   "Each of the seven displayed powers is at most $1-2\\kappa$ by"),
  infer("R.4.4",
   "Absorbing the remaining powers of $\\log p$ gives $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$, since $Tp=\\Theta(n)$.",
   "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})")],
 page="time-accounting",
 frm=["address-chunk-interchange", "fast-butterfly-layer", "crt-address-map", "gaussian-resampling", "bluestein-chirp", "signed-packing", "parameter-choice", "multiplication-algorithm"],
 salient="the smallest of the seven margins is exactly $2\\kappa=2^{-181}$, so $\\kappa=2^{-182}$ is half of it",
 adds=[B("g_i", "margin", "the margin $1-\\theta_i$ below one of the $i$th dominant power $p^{\\theta_i}$", "direct")])

root = show("R",
 "$T_A(n)=O(n(\\lg n)^{1-\\kappa})$ for one deterministic multitape machine $A$ that computes the exact product of two $n$-bit integers, with $\\kappa=2^{-182}$.",
 "reduce the product to a convolution, evaluate the convolution on tapes by transform layers whose recursions save a power of the logarithm, and sum the costs",
 mot("Each transform level of the convolution scans all stored bits, so a saving in movement and arithmetic is needed, and the convolution reduction exposes both.", "recoverable"),
 [conj, key, pipe, cost],
 page="main-theorem",
 adds=root_adds)

answer = {"root": root}

# ---------------- local checks ----------------
src = re.sub(r"\s+", " ", open(SRC, encoding="utf-8").read())
order = []
def walk(node, page_eff, depth=0):
    if node.get("page"):
        pg = node["page"]
    else:
        pg = page_eff
    node["_eff"] = pg
    if node["intention"] == "infer":
        if node["quote"] is not None:
            q = re.sub(r"\s+", " ", node["quote"]["quote"]).strip()
            c = src.count(q)
            assert c == 1, ("quote count", c, node["id"], q[:80])
            if not node.get("deferred"):
                order.append((src.index(q), node["id"]))
            node["_pos"] = src.index(q)
    for ch in node.get("children", []):
        walk(ch, pg, depth+1)
walk(root, None)
for a, b in zip(order, order[1:]):
    assert a[0] < b[0], ("order violated", a, b)
# page presentation counts
pres = {}
def collect(node):
    if node.get("page"):
        pres.setdefault(node["page"], []).append(node["id"])
    for ch in node.get("children", []):
        collect(ch)
collect(root)
for p, ids in pres.items():
    assert len(ids) == 1, ("page presented twice", p, ids)
    assert p in PAGES, p
# from rules
def check_from(node):
    eff = node["_eff"]
    for f in node.get("from", []):
        if f in PAGES:
            assert PAGES.index(f) < PAGES.index(eff), ("from not before page", node["id"], f, eff)
    for ch in node.get("children", []):
        check_from(ch)
check_from(root)
# every page presented or in some from
used = set(pres.keys())
def collect_from(node):
    for f in node.get("from", []):
        used.add(f)
    for ch in node.get("children", []):
        collect_from(ch)
collect_from(root)
missing = [p for p in PAGES if p not in used]
assert not missing, ("uncovered pages", missing)
# drop private keys
def clean(node):
    node.pop("_eff", None); node.pop("_pos", None)
    for ch in node.get("children", []):
        clean(ch)
clean(root)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(answer, f, ensure_ascii=False, indent=1)
print("ok: wrote", OUT, "infer quotes in order:", len(order))
print("pages presented:", sorted(pres.keys()))
