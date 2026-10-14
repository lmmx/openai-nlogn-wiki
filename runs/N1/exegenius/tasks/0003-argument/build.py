import json
P = "paper"
def Q(q): return {"source": P, "quote": q}
def infer(id, claim, quote, page=None, frm=(), deferred=False, salient=None, adds=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": Q(quote), "page": page, "from": list(frm)}
    if deferred: n["deferred"] = True
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n
def show(id, claim, method, mot, src, children, page=None, frm=(), quote=None, salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": {"text": mot, "source": src, "quote": Q(quote) if quote else None},
         "page": page, "from": list(frm), "children": children}
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n
def B(sym, name, meaning, rel="direct"):
    return {"symbol": sym, "name": name, "meaning": meaning, "relation": rel}

# ---------- S1: chunk interchange ----------
S1_3 = show("S1.3",
  "The bit network with $W_{\\rm b}$ wires and only pointwise XOR gates exchanges the banks $X_a,Y_a$, and its rational projection matrices satisfy $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m$ on every role while the edge ranks sum to $s_{\\rm b}<W_{\\rm b}m$.",
  "build the bank exchange from three stages of scratch-restoring invocations, carry it to arrays through common frames, label gates by nested rational subspaces, and use their projections as frames",
  "The network's routing and the cost of its frame changes are separate questions: once the routing is fixed only endpoint frames matter, so the intermediate labels can be chosen purely to make each edge's rank change small.",
  "explicit",
  [
    infer("S1.3.1", "An eight-row schedule (subtract side injection and scatter, copy, gather, scatter, side injection, undo gather, undo copy) adds $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$ to the targets whatever the initial scratch values, and restores the scratch wires.",
          "the following schedule remove the effect of the old scratch values;", page="scratch-restoration", frm=["linear-network"],
          salient="the net effect is independent of the arbitrary initial scratch contents"),
    infer("S1.3.2", "With gates indexed by three-element subsets of $[100]$, the gather/scatter coefficient $|S\\cap T|\\bmod 2$ (bit case) or $(|S\\cap T|-1)/2$ (complex case) is cancelled by the side wires except on the diagonal, so each invocation performs $y\\gets y+x$.",
          "Thus both net maps are $y\\gets y+x$.", page="triple-gadget", frm=["linear-network", "scratch-restoration", "binomial-coefficients", "exclusive-or"],
          salient="the unwanted off-diagonal coefficients cancel exactly, leaving the identity coefficient one"),
    infer("S1.3.3", "Three stages $X\\to Y$, $Y\\to X$ (inverse schedule), $X\\to Y$ send $(X_a,Y_a)\\mapsto(-Y_a,X_a)$, which over $\\mathbb F_2$ is the exchange of the two banks, restoring all auxiliary values.",
          "$X\\gets X-Y$.  Starting from $(x,y)$, the three stages give", frm=["linear-network"]),
    infer("S1.3.4", "If each vertex $v$ stores a wire's array through an invertible frame $D_v$ common to all incidences of a gate, pointwise gates commute with frames and the network implements $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$, so only endpoint frames determine each route's operator.",
          "$c_j\\in R$.  Thus the common frame commutes with the pointwise gate, and", page="frame-invariant", frm=["linear-network", "invertible-matrices"]),
    infer("S1.3.5", "Labelling gates and terminals by nondegenerate subspaces of $\\mathcal F=F^{\\otimes 3}$ (dimension $m=10^6$), every edge joins nested labels and the only decreasing edges are the central-wire edges from time 3 to 4, each losing dimension $h=100$.",
          "Every edge joins comparable nondegenerate labels.  The only decreasing", page="subspace-labels",
          frm=["triple-gadget", "linear-network", "vector-spaces-subspaces-and-dimension"]),
    infer("S1.3.6", "Using the projections $P_U$ as matrices, the edge ranks sum to $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}$, a deficit $N-2L_{\\rm b}>0$ below $W_{\\rm b}m$.",
          "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$.", page="rank-deficit", frm=["subspace-labels", "matrix-rank"],
          salient="the total rank $s_{\\rm b}$ is strictly less than $W_{\\rm b}m$, by the margin $N-2L_{\\rm b}$ since $L_{\\rm b}/N=100/539<1/2$"),
    infer("S1.3.7", "For every input role the endpoint matrix difference is $I_m$, since $P_{U_a^\\perp}+P_{U_a}=I_m$ on $X_a$ and all other roles go from the zero to the full label.",
          "$P_{U_a^\\perp}-(-P_{U_a})=I_m$.  Every other role has zero source", frm=["address-shear", "frame-invariant"]),
  ],
  page="bit-motif-interface", frm=["linear-network", "frame-invariant", "address-shear"],
  quote="Once the scalar routing is fixed,",
  salient="the endpoint operator is the same shear $H\\gets H+D$ on every role, including scratch roles",
  adds=[B("W_{\\rm b}", "bit wire count", "The number of wires of the bit network, including all scratch wires.", "count"),
        B("s_{\\rm b}", "bit rank sum", "The number of smaller interchanges the bit network needs, the sum of the rational ranks of its edge matrix differences.", "count"),
        B("m", "label dimension", "The dimension $10^6$ of the ambient label space, equal to the number of fields in each chunk group.", "count")])

S1_4 = show("S1.4",
  "For a fixed rational $m\\times m$ matrix $A$ of rank $a$, the address shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ costs exactly $a$ interchanges of $b$-digit field pairs plus $O(V)$ work.",
  "factor $A=E_1\\Pi E_2$ with lower triangular invertible factors, apply the triangular factors as controlled shifts, and realise each one of $\\Pi$ by a single interchange between two controlled additions",
  "Lower triangular coordinate changes only update later fields from earlier ones, which is exactly the direction in which controlled shifts run in linear time, so only the partial permutation $\\Pi$ needs recursive interchanges.",
  "explicit",
  [
    infer("S1.4.1", "Every rational $m\\times m$ matrix of rank $a$ factors as $E_1\\Pi E_2$ with invertible lower triangular $E_1,E_2$ and a partial permutation $\\Pi$ with exactly $a$ ones.",
          "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization", page="lower-triangular-factorization",
          frm=["triangular-and-diagonal-matrices", "gaussian-elimination", "matrix-rank", "permutation-matrices", "rational-numbers"]),
    infer("S1.4.2", "Each one of $\\Pi$ at $(i,j)$ is realised by $D_j\\leftarrow D_j+H_i$, an interchange of $(H_i,D_j)$, and $D_j\\leftarrow H_i-D_j$, using one interchange.",
          "It uses just one interchange.  There are $a$ ones, which proves the", frm=["controlled-shifts"]),
  ],
  page="matrix-shear-cost", frm=["controlled-shifts", "address-shear", "lower-triangular-factorization"],
  quote="Lower triangular changes of coordinates\ncan be performed entirely in this direction.")

S1_5 = show("S1.5",
  "For widths $e=m^k$ with a row field divisible by $W^k$, two chunks of $e$ radix-$q$ digits can be interchanged in $O(Ve^\\tau)$ time.",
  "split rows cyclically among the $W$ roles, run the bit network with shear frames $\\Phi_M$, recurse on each unit of edge rank, and finish the interchange with two linear-cost shears",
  "Each recursive call acts on one role stream of volume $V/W$ and there are $s$ of them, so after dividing cost by volume the recursive factor is $s/W<m^\\tau$, giving a geometric sum.",
  "recoverable",
  [
    infer("S1.5.1", "Splitting whole rows cyclically into $W$ role streams gives streams of identical address shape, each of volume $V/W$.",
          "Split whole rows cyclically into $W$ role streams within each prefix", frm=["row-splitting", "elementary-stream-ops"]),
    infer("S1.5.2", "The network performs $H\\leftarrow H+D$ on every row using exactly $s$ recursive interchanges of width $e/m$, each on a stream of volume $V/W$.",
          "The number of recursive calls is the sum of the edge ranks, exactly $s$.", frm=["bit-motif-interface", "matrix-shear-cost", "frame-invariant"]),
    infer("S1.5.3", "The normalized cost satisfies $F_k\\le(s/W)F_{k-1}+O(1)$, so $F_k=O(e^\\tau)$.",
          "Hence $F_k=O(e^\\tau)$.", frm=["volume-recurrence", "geometric-series"]),
  ])

S1 = show("S1",
  "Two disjoint equal-width address chunks of $u$ bits in an array of logical volume $V$ can be interchanged on a fixed number of tapes in $O(Vu^\\tau)$ time with $\\tau=1-2^{-50}$.",
  "turn the bit network's rank deficit into a volume-normalized recurrence for power widths, then supply rows from high digits and pad to arbitrary widths",
  "An edge matrix of rank $a$ costs $a$ smaller interchanges, and because the total rank is below the wire count times $m$, the recurrence saves a power of the width.",
  "explicit",
  [
    infer("S1.1", "Moving or permuting a fixed-radix digit, splitting and merging on a digit, and splitting rows cyclically into a fixed number of streams each take $O(V)$ time.",
          "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:", page="elementary-stream-ops",
          frm=["stream-array-layout", "multitape-turing-machine", "lexicographic-order"]),
    infer("S1.2", "An update $y\\mapsto y+a(\\text{controls})\\pmod{q^b}$ of a field that follows its control fields, or a scaling by a fixed rational unit, costs $O(V)$.",
          "The next operations are linear because their target field follows their", page="controlled-shifts",
          frm=["stream-array-layout", "elementary-stream-ops", "modular-arithmetic"]),
    S1_3,
    infer("S1.3b", "The relative rank deficit of each network exceeds $20\\cdot 2^{-50}$, so $s/W<m^\\tau$ with $\\tau=1-2^{-50}$.",
          "Both exact deficits displayed above are greater than $20\\cdot2^{-50}$.", frm=["rank-deficit"]),
    S1_4,
    S1_5,
    infer("S1.6", "Arbitrary widths and row counts are reduced to power widths by using the top $\\rho$ digits of both chunks as a row field, padding rows, decomposing the remaining width in base $m$, and padding binary chunks to radix $q$.",
          "Rows for a general array can be supplied by a few of its own high digits.", frm=["elementary-stream-ops"]),
  ],
  page="chunk-interchange", frm=["address-shear", "row-splitting", "volume-recurrence", "stream-array-layout"],
  quote="Because the sum of these ranks is less than the number of wires times\n$m$, the resulting recurrence saves a power of the chunk width.",
  salient="an exact permutation of data is computed in less time than the $\\Theta(V\\log)$-type cost of moving data, by forming XOR combinations of data",
  adds=[B("\\tau", "swap exponent", "The fixed exponent $1-2^{-50}$ below one in the chunk-interchange cost."),
        B("u", "chunk width", "The number of address bits in each of the two chunks being interchanged.", "count")])

# ---------- S2: simultaneous layer ----------
S2_1 = show("S2.1",
  "In the complex network with binary labels each edge's phase-frame change is a product of one kernel $aI+bX_v$ or its inverse per residual basis vector, these number $s_{\\rm c}<W_{\\rm c}m$ in total, and after endpoint corrections the network applies $C^{\\otimes m}$ on every role.",
  "attach phase frames $\\mathcal C_U$ to the binary subspace labels, factor each edge change by orthogonal weight additivity, and telescope the frames along each route",
  "All phase frames are diagonalised by the same $H^{\\otimes m}$, and orthonormal residual bases make Hamming weight additive modulo four, so each residual direction contributes exactly one two-point kernel.",
  "recoverable",
  [
    infer("S2.1.1", "For an orthonormal basis of the residual, $\\mathcal C_V\\mathcal C_U^{-1}$ factors into one kernel $aI+bX_v$ or its inverse per basis vector.",
          "becomes $aI+bX_v$ or its inverse.  The nonzero residuals have such", page="phase-frames", deferred=True,
          frm=["subspace-labels", "frame-invariant", "complex-numbers", "exclusive-or"]),
    infer("S2.1.2", "After diagonal $Z$ corrections at the 27 support coordinates of $u_a$ and undoing the signed exchange, every role, scratch roles included, receives $C^{\\otimes m}$.",
          "back to role $w$.  Every role, including every scratch role, now has", deferred=True, frm=["frame-invariant"]),
  ],
  page="complex-motif-interface", frm=["linear-network", "frame-invariant", "subspace-labels", "rank-deficit", "scratch-restoration", "triple-gadget"],
  salient="the same forward kernel tensor power $C^{\\otimes m}$ appears on every role, including roles carrying arbitrary scratch values",
  adds=[B("C", "two-point kernel", "The matrix $aI+bX$ with $a=(1+i)/2$, $b=(1-i)/2$, equal to $H\\,\\mathrm{diag}(1,i)\\,H$."),
        B("s_{\\rm c}", "complex call count", "The number of smaller kernel calls the complex network needs, the sum of its edge residual dimensions.", "count"),
        B("W_{\\rm c}", "complex wire count", "The number of wires of the complex network.", "count")])

S2 = show("S2",
  "On arrays $[P]\\times[2^K]^D\\times[S]$ of polynomial records with $D\\le d$, the tensor product of $H_0$ on one selected bit in each of the $D$ chunks, followed by one truncation $Q_p$, costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$ and error below $\\sqrt2\\,2^{-p}$.",
  "write $H_0^{\\otimes D}$ through the kernel $C^{\\otimes D}$, apply $C^{\\otimes e}$ recursively by the complex network on groups of $e=mf$ axes with packed binary basis changes, and bound the exact dyadic growth before a single truncation",
  "Separate butterfly factors would need $D$ whole-array passes; the complex network replaces them by $s_{\\rm c}$ calls on streams of volume $V/W_{\\rm c}$, so the normalized recursive factor $s_{\\rm c}/W_{\\rm c}<m^\\sigma$ saves a power of $d$.",
  "explicit",
  [
    S2_1,
    infer("S2.2", "Applying the network with column frames to $e=mf$ selected axes uses exactly $s_{\\rm c}$ child calls, each on the $f$ axes of one slot, and yields $C^{\\otimes e}$; inverse children cost one forward call.",
          "$s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot.", frm=["complex-motif-interface", "phase-frames"]),
    infer("S2.3", "The normalized layer is $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$, so it differs from the $C$ layer only by diagonal phases and a dyadic scale.",
          " H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.", frm=["butterfly", "complex-motif-interface", "gaussian-dyadics"]),
    infer("S2.4", "XORing selected bits of one address chunk into another, restoring a third chunk, costs $O(V(L^\\tau+1))$ via eight packed cyclic shifts with guard bits and a deterministic repair of the bounded exceptional set.",
          "This implements $T_0$ everywhere.", page="packed-selected-bit",
          frm=["chunk-interchange", "controlled-shifts", "elementary-stream-ops", "exclusive-or"]),
    infer("S2.5", "Splitting rows among the $W$ roles gives each of the $s$ child calls volume $V/W$, so $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$, which unrolls to $O(d^{\\lambda'})$.",
          "\\(V/W\\), so their total cost is \\(s(V/W)F(e/m)\\).  Dividing by", frm=["row-splitting", "volume-recurrence", "packed-selected-bit"]),
    infer("S2.6", "Every intermediate value is a Gaussian dyadic of depth at most $C_0d^{C_1}=o(p)$, so $O(p)$-bit words represent the whole layer exactly until the final truncation.",
          "the same as \\(t\\) successive halvings.  Thus reserving \\(p+\\Delta\\)", frm=["gaussian-dyadics", "fixed-point-numbers"]),
  ],
  page="simultaneous-layer", frm=["butterfly", "gaussian-dyadics", "chunk-interchange", "row-splitting", "volume-recurrence"],
  quote="whereas separate butterfly\nfactors would require $D$ whole-array passes.",
  adds=[B("\\lambda'", "layer exponent", "The fixed exponent $1-2^{-54}$ below one in the cost of a simultaneous butterfly layer."),
        B("K", "chunk width", "The number of address bits in each axis chunk, $\\lfloor d^c\\rfloor$.", "count"),
        B("D", "selected chunk count", "The number of address chunks on which a bit is selected in one layer.", "count")])

# ---------- S3: synthetic convolution ----------
S3 = show("S3",
  "Normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\\mathbb C[y]/(y^r+1)$ on $d-1$ power-of-two axes is computed with error below $\\sqrt2M(3\\ell+1)2^{-p}$ at cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
  "compute two forward synthetic transforms in a layout where simultaneous layers apply, multiply records pointwise in the retained stored order by signed packing, and apply the opposite transform consuming that order",
  "The forward outputs are stored in a permuted frequency order, and since pointwise multiplication commutes with a common record permutation, the opposite transform can consume that order directly without sorting.",
  "explicit",
  [
    infer("S3.1", "Over $\\mathbb C[y]/(y^r+1)$ the roots $\\omega_t=y^{2r/t}$ make twiddles signed shifts, and decimation in frequency computes $B_tF_t^-$ with entry $j$ stored at $\\operatorname{rev}_a(j)$, while the reverse recursion computes $F_t^+B_t^{-1}$.",
          "entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$.", page="synthetic-fft", frm=["negacyclic-ring", "butterfly", "dft"]),
    infer("S3.2", "A positional layout permutation $L$ places the bits of each round at a common offset in consecutive $K$-bit chunks, so each round is one simultaneous layer, and the transforms $LBF^-_{\\boldsymbol t}$ and $F^+_{\\boldsymbol t}B^{-1}L^{-1}$ cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error below $\\sqrt2\\ell 2^{-p}$.",
          "These prefix moves and chunk exchanges define $L$.  We use the same", page="transform-layout",
          frm=["synthetic-fft", "simultaneous-layer", "chunk-interchange", "elementary-stream-ops"]),
    infer("S3.3", "Pointwise multiplication commutes with applying the same record permutation $LB$ to both operands, so products can be taken in the retained order.",
          "Pointwise multiplication commutes with applying the same record", frm=["transform-layout", "permutations"]),
    infer("S3.4", "Each normalized ring product $Q_p(fg/r)$ is computed exactly by evaluating at $B_0=2^{4p}$, four calls to the established multiplier, and centered-residue extraction, in $O(rp\\log(rp))$ time.",
          "Four exact integer products dominate the linear", page="signed-packing",
          frm=["hvdh-multiplier", "negacyclic-ring", "two-s-complement", "carry-propagation"]),
    infer("S3.5", "Multiplying the opposite transform of the pointwise products by $M$ gives exactly $(f*g)/(rM)$.",
          "The displayed normalization identity identifies its exact scaling", frm=["dft", "cyclic-convolution"]),
  ],
  page="synthetic-convolution", frm=["negacyclic-ring", "cyclic-convolution", "transform-layout", "signed-packing"],
  quote="We also specify where each frequency entry\nis stored, because the opposite transform consumes that same order\nafter a pointwise product.")

# ---------- S4: source transform by resampling ----------
S4 = show("S4",
  "The source transform $RF_{\\boldsymbol s}$ on distinct prime axis lengths $s_i$ equals $2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with power-of-two lengths $t_i$, its middle factor is a normalized cyclic convolution between chirps, and the retained permutation $R$ cancels in a convolution.",
  "keep the coordinate permutations inside the Gaussian resampling identity, tensor it over the axes, convert the permuted middle transform by Bluestein's chirp identity, and show the source permutation cancels",
  "Executing the two permutations would require full sorts on each coordinate, costing a logarithmic factor; leaving them in the identity avoids these sorts entirely.",
  "explicit",
  [
    infer("S4.1", "For coprime $s<t$ there are contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, approximable with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$, without executing $P_s$ or $P_t$.",
          "In \\eqref{eq:no-sort-one-dimensional} these permutations remain in the", page="retained-permutations",
          frm=["gaussian-resampling", "dft", "permutations"]),
    infer("S4.2", "Tensoring over $d$ axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with linewise maps of error below $dp^2$, and exposing all lines by chunk interchanges costs $O(Tpd^2(1+\\ell^\\tau))$.",
          "Tensoring \\eqref{eq:no-sort-one-dimensional} proves", page="tensor-resampling",
          frm=["retained-permutations", "chunk-interchange", "elementary-stream-ops"]),
    infer("S4.3", "The permuted transform satisfies $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$ for the chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$.",
          "This is precisely the coefficient in $QF_{\\boldsymbol t}$, because", page="bluestein-chirp",
          frm=["dft", "cyclic-convolution", "retained-permutations", "exponential-function-and-euler-s-formula"]),
    infer("S4.4", "The retained permutation cancels: $(RF^+_{\\boldsymbol s})[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
          "proving \\eqref{eq:source-permutation-cancel}. Finally, conjugation", frm=["retained-permutations", "dft", "cyclic-convolution"],
          salient="no permutation is ever executed, yet the convolution comes out in the original coordinate order"),
  ],
  quote="Its usual implementation sorts twice on each\ncoordinate. We retain both permutations in the transform formula and\ncompute that formula directly.",
  frm=["gaussian-resampling", "dft"],
  adds=[B("R", "source permutation", "The tensor product of the coordinate permutations $P_{s_i}$ on the prime axes."),
        B("Q", "target permutation", "The tensor product of the coordinate permutations $P_{t_i}$ on the power-of-two axes."),
        B("\\gamma", "resampling scale exponent", "The exponent $2d\\alpha^2$ of the power of two that undoes the resampling normalizations.")])

# ---------- S5: exact product ----------
S5 = show("S5",
  "The algorithm forms radix-$2^b$ digit arrays, places them on prime axes by $\\Phi$, computes $(u*v)/S^2$ through two source transforms, a pointwise product and an opposite transform, and recovers the exact $2n$-bit product by rescaling, rounding and carries.",
  "reduce the integer product to a digit convolution, map it to a multidimensional cyclic convolution on prime axes, evaluate it with the source transforms whose middle convolution uses the phase twist, then round and propagate carries",
  "Each change of problem preserves convolution exactly, and the accumulated numerical error is pushed strictly below $1/2$, so rounding recovers integer coefficients exactly.",
  "recoverable",
  [
    infer("S5.1", "Writing the inputs in radix $2^b$ makes the product a convolution of $q=\\lceil n/b\\rceil$-digit lists with coefficients below $2^{3b}$ and no wraparound modulo $x^S-1$ since $2q-2<S$.",
          "Thus convolution modulo $x^S-1$ has no nonzero wraparound.  Every product", page="radix-digit-convolution",
          frm=["cyclic-convolution", "polynomials", "binary-representation-of-integers"]),
    infer("S5.2", "The map $x\\mapsto\\prod_i x_i^{\\mu_i}$ is an isomorphism turning one cyclic convolution of length $S=\\prod_i s_i$ into a multidimensional one, implemented by triangular controlled shifts and axis moves in $O(Tpd^2(1+\\ell^\\tau))$ time.",
          "$\\Phi$ is an isomorphism and preserves cyclic convolution.", page="crt-address-map",
          frm=["chinese-remainder-theorem", "cyclic-convolution", "controlled-shifts", "chunk-interchange"]),
    infer("S5.3", "The twist $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ converts cyclic convolution along the last axis into multiplication modulo $y^r+1$, so $\\mathcal M_{\\mathbb C}(f,g)=(f*g)/T$ is computed by the synthetic convolution.",
          "Untwisting therefore recovers the cyclic coefficient with the correct", page="phase-twist",
          frm=["negacyclic-ring", "cyclic-convolution", "exponential-function-and-euler-s-formula"]),
    infer("S5.4", "After the three transforms the exact counterpart is $(u*v)/S^2$, and the two exact scalings by $S$ and $2^{2b+4}S$ return the integer coefficient convolution.",
          "The two occurrences of $S$ in this algorithm undo different", frm=["bluestein-chirp", "tensor-resampling"]),
    infer("S5.5", "The final coefficient error is below $448b\\,2^{-3b/4}<1/2$, so rounding gives the exact integer coefficients, and radix-$2^b$ carry propagation yields the $2n$-bit product.",
          "$H_j/2^p$.  The strict error below $1/2$ makes the nearest integer to", page="exact-recovery",
          frm=["rounding-to-the-nearest-integer", "carry-propagation", "radix-digit-convolution", "gaussian-dyadics"]),
  ],
  frm=["radix-digit-convolution", "crt-address-map", "phase-twist", "exact-recovery", "synthetic-convolution"],
  adds=[B("b", "digit width", "The number of bits $\\lceil\\log_2 n\\rceil$ in each radix digit.", "count"),
        B("S", "source length", "The product of the distinct odd primes $s_i$, the length of the cyclic convolution.", "count"),
        B("\\Phi", "CRT address map", "The algebra isomorphism sending $x$ to $\\prod_i x_i^{\\mu_i}$.")])

S6 = infer("S6",
  "With $\\tau=1-2^{-50}$, $\\epsilon=2^{-75}$, $c=2^{-56}$, $\\lambda'=1-2^{-54}$, $\\delta=1/16$, every row of the cost table divided by $Tp$ is at most $p^{1-2\\kappa}$, so the total time is $O(n(\\lg n)^{1-\\kappa})$.",
  "Thus $\\min_i g_i=2^{-181}=2\\kappa$.  This explicit slack will cover", page="cost-table",
  frm=["chunk-interchange", "simultaneous-layer", "transform-layout", "tensor-resampling", "crt-address-map", "signed-packing", "big-o"],
  salient="the smallest margin $g_2=\\epsilon c(1-\\tau)=2^{-181}$ comes from the chunk exchanges of the transform layout")

root = show("S0",
  "One deterministic fixed-alphabet multitape Turing machine computes the exact $2n$-bit product of two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$.",
  "build two tape procedures that beat a scan per level (fast chunk interchange and simultaneous butterfly layers) from finite linear networks with a rank deficit, place them in the Gaussian-resampling and synthetic-transform reduction of multiplication to convolution, recover the product exactly, and total the costs",
  "Scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both data movement and butterfly arithmetic must be done in less than a scan per level.",
  "explicit",
  [S1, S2, S3, S4, S5, S6],
  page="main-theorem", frm=["nlogn-conjecture", "multitape-turing-machine", "big-o", "schoolbook-multiplication", "hvdh-multiplier"],
  quote="We therefore need savings in both movement and arithmetic.",
  salient="a fixed power saving $(\\lg n)^{-\\kappa}$ below $n\\log n$, uniformly through all input lengths, refuting the conjectured $n\\log n$ lower bound",
  adds=[B("n", "input length", "The number of bits of each input integer.", "count"),
        B("V", "logical volume", "The number of stored data bits of the array being processed.", "count"),
        B("p", "working precision", "The number $6\\lceil\\log_2 n\\rceil$ of fractional bits in each coefficient.", "count"),
        B("d", "axis count", "The number of transform axes, about $p^\\epsilon$.", "count"),
        B("r", "polynomial length", "The power-of-two number of coefficients in each polynomial record.", "count"),
        B("T", "padded box size", "The power-of-two total number of entries in the padded transform box.", "count"),
        B("\\kappa", "saving exponent", "The fixed exponent $2^{-182}$ of the logarithmic saving.")])

json.dump({"root": root}, open("/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N1/exegenius/tasks/0003-argument.answer.json", "w"), indent=1, ensure_ascii=False)

# self-check quotes
src = open("/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N1/sources/paper.tex").read()
def walk(n):
    yield n
    for c in n.get("children", []): yield from walk(c)
last = -1
for n in walk(root):
    for q in ([n["quote"]] if n.get("quote") else []) + ([n["motivation"]["quote"]] if n.get("motivation") and n["motivation"].get("quote") else []):
        i = src.find(q["quote"])
        print(n["id"], i, "NOTFOUND" if i < 0 else "")
    if n["intention"] == "infer" and not n.get("deferred"):
        i = src.find(n["quote"]["quote"])
        if i < last: print("ORDER", n["id"])
        last = max(last, i)
