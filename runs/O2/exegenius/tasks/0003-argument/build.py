import json, sys
SRC = open('/home/user/openai-nlogn-wiki/runs/O2/sources/paper.tex').read()

def ev(q):
    assert q in SRC, ("MISSING", q)
    return {"source": "paper", "quote": q}

def mot(text, src, q=None):
    return {"text": text, "source": src, "quote": ev(q) if q else None}

def infer(id, claim, q, page=None, frm=(), salient=None, deferred=False):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(q)}
    if page: n["page"] = page
    if frm: n["from"] = list(frm)
    if salient: n["salient"] = salient
    if deferred: n["deferred"] = True
    return n

def show(id, claim, method, motivation, children, page=None, frm=(), salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children}
    if page: n["page"] = page
    if frm: n["from"] = list(frm)
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n

def b(sym, name, meaning, rel="direct"):
    return {"symbol": sym, "name": name, "meaning": meaning, "relation": rel}

S1 = show("S1",
  "On a fixed number of tapes, digit moves, permutations of two digit values, splits with fixed pointwise maps, cyclic row splits, controlled shifts and fixed rational scalings of an address field each cost $O(V)$ on an array of volume $V$.",
  "stream each operation in lexicographic address order, splitting the array into a fixed number of aligned streams and merging them back",
  mot("Addresses are implicit in the position of an entry in the ordered stream, so any operation that needs only a fixed number of aligned streams, or a target field that follows its controls, can be done in a bounded number of scans.", "recoverable"),
  [
    infer("S1.1", "Fixed digit-pair permutations, single-digit moves, splits with a pointwise map, and cyclic splits of whole rows into $W$ streams each cost $O(V)$.",
      "Each of the following operations on an array of\nvolume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
      frm=["lexicographic-order", "binary-counter", "multitape-turing-machine"]),
    infer("S1.2", "An update $y\\mapsto y+a(\\text{controls})\\bmod q^b$ of a target field that follows its control fields, and multiplication of $y$ by a fixed rational unit, cost $O(V)$.",
      "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the\nfixed number of control values.",
      page="controlled-shifts",
      frm=["fixed-tape-model", "modular-arithmetic", "greatest-common-divisor-and-modular-inverses", "cyclic-shift"]),
  ],
  page="fixed-tape-model",
  frm=["multitape-turing-machine", "lexicographic-order", "deterministic-worst-case-time-complexity"])

S2 = show("S2",
  "Two fixed linear networks, a bit network over $\\mathbb F_2$ and a complex network over $\\mathbb Z[i,1/2]$, exchange two data banks while restoring every scratch value, and the total number $s$ of smaller operations their frame changes need is strictly below $Wm$, with $s/W<m^{1-2^{-50}}$.",
  "build a three-stage bank-exchange network on three-element subsets of a 100-element set, carry arrays through it in frames that commute with the gates, label vertices by nested nondegenerate subspaces whose residual dimensions count the smaller calls, and check both interfaces and the explicit deficits",
  mot("A strict deficit $s<Wm$ means that multiplying the recursion parameter by $m$ multiplies the per-bit recursive cost by $s/W<m$, which is what yields a power saving.", "explicit",
      "This strict inequality\nis the source of the power saving."),
  [
    show("S2.1",
      "For arbitrary initial scratch values, a forward invocation at stage 1, an inverse invocation at stage 2 and a forward invocation at stage 3 send $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ and restore every auxiliary value.",
      "run an eight-row schedule per invocation that first subtracts the effect of the old scratch values, then copies, gathers, scatters and injects to add $x$ to $y$, then restores the scratch; compose three such invocations",
      mot("Subtracting the scratch contribution before adding the source contribution, and undoing copy and gather afterwards, makes the net change independent of whatever the scratch wires held.", "explicit",
          "The first two rows of\nthe following schedule remove the effect of the old scratch values;\nthe next four introduce the source values and add their effect to the\ntarget; the last two restore the scratch values."),
      [
        infer("S2.1.1", "Within one invocation the net change of the target bank is $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$, independent of the initial side and central values.",
          "The net target change is\n$(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$, independently of\n$a,c$.",
          frm=["linear-maps-and-matrices"]),
        infer("S2.1.2", "Gather and scatter through central wires give the coefficient $|S\\cap T|\\bmod 2$ (bit network) or $(|S\\cap T|-1)/2$ (complex network) from $x_T$ to $y_S$, and side wires cancel the neighbor terms, so each invocation performs $y\\gets y+x$.",
          "In the bit case, the central coefficient from $x_T$ to $y_S$ is\n$|S\\cap T|\\bmod2$.",
          page="triple-intersection-construction",
          frm=["sets-subsets-and-cartesian-products", "xor-and-arithmetic-modulo-2", "bank-exchange-network"]),
        infer("S2.1.3", "The three stages take $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
          "Starting from $(x,y)$, the three stages give\n$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$."),
      ],
      page="bank-exchange-network",
      frm=["linear-maps-and-matrices", "xor-and-arithmetic-modulo-2"],
      salient="The exchange works for arbitrary, unknown initial scratch values, which all come back unchanged."),
    infer("S2.2",
      "If each vertex $v$ has an invertible frame $D_v$ common to all incidences of a gate and each edge applies $D_vD_u^{-1}$, the network implements $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$, so a route from role $w$ to $\\rho(w)$ applies only $D_{\\mathrm{sink}(\\rho(w))}D_{\\mathrm{source}(w)}^{-1}$ with its sign.",
      "Thus the common frame commutes with the pointwise gate, and\nthe invariant continues to the sinks.",
      page="frames",
      frm=["bank-exchange-network", "invertible-matrices", "linear-maps-and-matrices"]),
    show("S2.3",
      "Labelling every vertex by a nondegenerate subspace of $\\mathcal F=F^{\\otimes3}$, of dimension $m=10^6$, makes adjacent labels nested, with the only decreases on central wires, so the residual dimensions sum to $Wm-2N+2L$ with $L/N=100/539$ or $101/539$, below $1/2$.",
      "choose bilinear forms in which triple indicator vectors are nondegenerate and neighbouring ones orthogonal, expose one tensor factor per stage, and tabulate the orthogonal residual of every edge",
      mot("Edge costs are measured by residual dimensions, so the labels must grow along edges except for a small total loss, which is kept small relative to $N$.", "explicit",
          "The saving will come from keeping the total dimension lost on decreasing\nedges small relative to $N$."),
      [
        infer("S2.3.1", "With $\\langle t_S,t_T\\rangle=|S\\cap T|-1$ over $\\mathbb Q$ or the dot product over $\\mathbb F_2$, every triple line is nondegenerate and neighbouring triple lines are orthogonal.",
          "Thus every triple line is nondegenerate, and neighboring triple lines\nare orthogonal, in the label field belonging to either construction.",
          frm=["linear-algebra-bilinear", "triple-intersection-construction"]),
        infer("S2.3.2", "Every edge joins comparable labels, the only decreasing edges are the central-wire edges from time 3 to time 4, each losing $h$ dimensions, and the absolute dimension changes sum to $Wm-2N+2L$ with $L=Ich$.",
          "The only decreasing\nedges are the central-wire edges from time 3 to time 4; their dimension\nloss is $h$.",
          frm=["tensor-products", "linear-algebra-bilinear"]),
        infer("S2.3.3", "The loss ratios are $L_b/N=100/539$ and $L_c/N=101/539$, both smaller than $1/2$.",
          "In particular, both are smaller than $1/2$."),
      ],
      page="subspace-labels",
      frm=["linear-algebra-bilinear", "tensor-products", "vector-spaces-subspaces-basis-and-dimension", "frames"]),
    show("S2.4",
      "Using the address shears $\\Phi_{M_v}$ with $M_v=P_U$ as frames in the bit network, the edge ranks sum to $s_b=W_bm-N+2L_b<W_bm$ and the endpoint operator is the same shear $H\\gets H+D$ on every role.",
      "assign the projection $P_U$ to each gate and sink and $-P_{U_a}$ to the source of $X_a$, so edge ranks equal dimension changes and endpoint differences equal $I_m$",
      mot("For nested nondegenerate subspaces, $P_V-P_U$ has rank $\\dim V-\\dim U$, so the dimension count becomes a rank count, and the negative source projection makes every route's endpoint difference the identity matrix.", "recoverable"),
      [
        infer("S2.4.1", "The rank sum exceeds the dimension count only by the $N$ rank-one source edges, leaving a deficit $N-2L_b>0$ below $W_bm$.",
          "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$."),
        infer("S2.4.2", "For each input $X_a$ the endpoint difference is $P_{U_a^\\perp}+P_{U_a}=I_m$, and every other role also has endpoint difference $I_m$.",
          "For an input $X_a$ the endpoint difference is\n$P_{U_a^\\perp}-(-P_{U_a})=I_m$."),
      ],
      page="address-shears",
      frm=["frames", "subspace-labels", "rank-of-a-matrix", "modular-arithmetic", "linear-algebra-bilinear"]),
    show("S2.5",
      "In the complex network with binary labels and frames $\\mathcal C_U=H^{\\otimes m}\\operatorname{diag}(i^{\\operatorname{wt}(P_Ux)})H^{\\otimes m}$, each edge change is a product of one kernel $aI+bX_v$ or its inverse per orthonormal residual vector, in total $s_c=W_cm-2N+2L_c<W_cm$, and after diagonal corrections every role receives $C^{\\otimes m}$.",
      "use that Hamming weight is additive modulo four over orthogonal binary vectors, turn each resulting character phase into a translation kernel by Hadamard conjugation, and fix the inverse factors on the $X_a\\to Y_a$ routes by $Z$ conjugations",
      mot("Phases $i^{\\operatorname{wt}}$ split into one odd factor per orthonormal residual vector exactly when weights add modulo four, so a binary orthonormal basis turns each dimension of residual into one two-point kernel.", "recoverable"),
      [
        infer("S2.5.1", "For orthogonal binary vectors, Hamming weight is additive modulo four, so $q_V-q_U$ is a sum of one odd-weight character per orthonormal residual vector.",
          "If $z\\cdot w=0$, the intersection cardinality is even, so weight is\nadditive modulo four.",
          frm=["hamming-weight", "xor-and-arithmetic-modulo-2"]),
        infer("S2.5.2", "Hadamard conjugation turns each such phase into the translation kernel $aI+bX_v$ or its inverse.",
          "The displayed phase therefore\nbecomes $aI+bX_v$ or its inverse."),
        infer("S2.5.3", "With $Z$ corrections and the scalar $i^{27k}$, negating the physical $X$ outputs and undoing the exchange leaves $C^{\\otimes m}$ on every role, including scratch roles.",
          "Every role, including every scratch role, now has\nthe required forward tensor product."),
      ],
      page="phase-frames",
      frm=["frames", "subspace-labels", "tensor-products", "gaussian-dyadics", "linear-algebra-bilinear", "complex-numbers"]),
    infer("S2.6",
      "The relative deficits $\\eta_b,\\eta_c$ exceed $20\\cdot2^{-50}$, so $s_b/W_b<m^{\\tau}$ and $s_c/W_c<m^{\\sigma}$ with $\\tau=\\sigma=1-2^{-50}$.",
      "Both exact deficits displayed above are greater than $20\\cdot2^{-50}$.",
      frm=["address-shears", "logarithms-and-exponentials"]),
  ],
  page="rank-saving",
  frm=["linear-algebra-bilinear", "tensor-products", "rank-of-a-matrix"],
  salient="The deficit is minute (relative deficit near $10^{-11}$) yet strict, and the same triple-subset design achieves it over two different scalar domains.",
  adds=[
    b("W", "wire count", "The number of wires (roles) in the fixed network, including scratch wires.", "count"),
    b("m", "label dimension", "The dimension $h^3=10^6$ of the label space $F^{\\otimes3}$ whose subspaces label the vertices."),
    b("s", "smaller-call count", "The number of smaller recursive operations needed over all edges, the sum of edge residual dimensions or ranks.", "count"),
    b("N", "bank size", "The number of data wires in each of the two banks, $v^3$ for $v=\\binom{100}{3}$.", "count"),
  ])

S3 = show("S3",
  "Two disjoint $u$-bit address fields of a stored array of volume $V$ can be interchanged in $O(Vu^\\tau)$ time with $\\tau=1-2^{-50}$.",
  "factor each edge shear into rank-many smaller interchanges plus linear triangular updates, run the bit network on row-split role streams so its endpoint is the shear $H\\gets H+D$, recurse on the field width, and remove the width and row restrictions by padding",
  mot("Each edge of rank $a$ costs $a$ smaller interchanges, so the strict rank saving turns into a recurrence that saves a power of the width.", "explicit",
      "Because the sum of these ranks is less than the number of wires times\n$m$, the resulting recurrence saves a power of the chunk width."),
  [
    infer("S3.1", "Every rational $m\\times m$ matrix of rank $a$ factors as $E_1\\Pi E_2$ with invertible lower triangular $E_1,E_2$ and a partial permutation $\\Pi$ with $a$ ones.",
      "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
      page="lower-triangular-factorization",
      frm=["gaussian-elimination", "triangular-matrices", "rank-of-a-matrix"]),
    infer("S3.2", "A shear $(H,D)\\mapsto(H+AD,D)$ with $A$ of rational rank $a$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ work.",
      "can be performed with exactly $a$ interchanges of pairs of $b$-digit\nfields and $O(V)$ further work.",
      frm=["lower-triangular-factorization", "controlled-shifts"]),
    show("S3.3",
      "For widths $e=m^k$ with a row field of length divisible by $W^k$, chunk interchange costs $O(Ve^\\tau)$, because time per bit obeys $F_k\\le(s/W)F_{k-1}+O(1)$.",
      "split rows cyclically into $W$ role streams of volume $V/W$, apply each edge shear by recursive smaller interchanges, merge, and complete the interchange with two linear updates; then solve the geometric recurrence",
      mot("Dividing by volume, multiplying the width by $m$ multiplies the recursive cost by $s/W<m$, so the per-bit cost grows like a power $e^\\tau$ with $\\tau<1$.", "explicit",
          "After dividing cost by volume, multiplying the parameter by $m$\nincreases the recursive contribution by $s/W<m$."),
      [
        infer("S3.3.1", "Running the bit network with frames $\\Phi_{M_v}$ on the role streams and merging rows back yields $H\\gets H+D$ on every original row, including scratch rows.",
          "The result\nis $H\\leftarrow H+D$ on every original row, including rows assigned\nto scratch roles, whose initial values were arbitrary."),
        infer("S3.3.2", "The updates $D\\gets D-H$, $H\\gets H+D$, $D\\gets H-D$ send $(H,D)$ to $(D,H)$.",
          "The transformation\nsends $(H,D)$ to $(D,H)$."),
        infer("S3.3.3", "Since $s/W<m^\\tau$, the recurrence gives $F_k=O(e^\\tau)$.",
          "Hence $F_k=O(e^\\tau)$.",
          frm=["geometric-series", "recurrence-relations"]),
      ],
      page="power-saving-recursion",
      frm=["rank-saving", "address-shears", "frames", "fixed-tape-model", "recurrence-relations"]),
    infer("S3.4", "Borrowing high digits as a row field and padding binary chunks to radix $q$, any two $u$-bit chunks are interchanged in $O(Vu^\\tau)$ time.",
      "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.",
      frm=["power-saving-recursion", "fixed-tape-model"]),
  ],
  page="fast-interchange",
  frm=["rank-saving", "address-shears", "frames", "controlled-shifts", "fixed-tape-model"],
  salient="Its final effect is a pure permutation, yet it beats the cost of moving data field by field because its intermediate steps form XOR combinations of the data.",
  adds=[
    b("u", "field width", "The number of bits in each of the two address fields being interchanged.", "count"),
    b("\\tau", "interchange exponent", "The fixed exponent $1-2^{-50}$ in the interchange cost $O(Vu^\\tau)$."),
  ])

S4 = show("S4",
  "On the layouts used, applying $H_0$ to the same bit of up to $d$ equal-width $K$-bit address chunks, coefficientwise on polynomial records with $p$-bit grid coefficients, costs $O(Vd^{\\lambda'})$ with $\\lambda'=1-2^{-54}$ and error below $\\sqrt2\\,2^{-p}$.",
  "build $C^{\\otimes e}$ recursively through the complex phase network, implementing residual bases by packed binary row additions on address bits, batch the calls on fixed tapes, bound the guard width, and convert $C^{\\otimes D}$ to $H_0^{\\otimes D}$ by diagonal phases and a dyadic scale before one truncation",
  mot("Separate butterfly factors would need $D$ passes over the whole array; the network recursion replaces them by a power $d^{\\lambda'}$ with $\\lambda'<1$.", "explicit",
      "We will obtain cost $O(Vd^{\\lambda'})$, with\n$\\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly\nfactors would require $D$ whole-array passes."),
  [
    infer("S4.1", "On a group of $e=mf$ selected axes, the complex network with column phase frames uses $s_c$ child calls on $f$ axes each and gives $C^{\\otimes e}$ on every role.",
      "Proposition~\\ref{prop:complex-motif-interface} therefore gives\n$C^{\\otimes e}$ on every role, including roles whose initial scratch\nvalues were arbitrary.",
      frm=["phase-frames", "power-saving-recursion"]),
    infer("S4.2", "The normalized layer is $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$, using only Gaussian dyadic phases and scales.",
      "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.",
      frm=["butterfly-h0", "gaussian-dyadics"]),
    infer("S4.3", "A packed operation XORs the selected bits of one chunk into another, restoring a temporary chunk, by whole-chunk cyclic shifts and a sorted correction of an explicitly bounded exceptional set.",
      "It preserves the spectator coordinates, all other chunk bits, and every\nrecord payload; in particular, it restores the entire chunk $z$ for\nevery initial value.",
      page="packed-selected-bit-addition",
      frm=["fast-interchange", "controlled-shifts", "fixed-tape-model", "xor-and-arithmetic-modulo-2", "stable-sorting-and-radix-sort"]),
    infer("S4.4", "The recursion, with individual kernels applied by splitting on the selected bit, is scheduled on a fixed number of tapes.",
      "We now turn the finite complex network into an algorithm for a whole\nlayer."),
    infer("S4.5", "Intermediate values within one layer need only $O(d^{C_1})$ extra guard bits, which is $O(p)$.",
      "The accelerated network is evaluated exactly until an entire\nnormalized butterfly layer is complete.",
      frm=["gaussian-dyadics", "error-accounting"]),
    infer("S4.6", "The procedure returns $Q_p$ of the exact layer in $O(Vd^{\\lambda'})$ time with error below $\\sqrt2\\,2^{-p}$.",
      "The procedure returns $Q_p(\\mathcal H z)$ in the same array,\ncoefficient order, and component format in $O(Vd^{\\lambda'})$ time,",
      frm=["error-accounting"]),
  ],
  page="simultaneous-butterfly-layer",
  frm=["phase-frames", "butterfly-h0", "gaussian-dyadics", "error-accounting", "ring-y-r-plus-1", "fast-interchange"],
  salient="Applying $D$ butterfly factors costs less than $D$ passes over the data, since $\\lambda'<1$.",
  adds=[
    b("d", "axis bound", "The maximum number of address chunks whose selected bits are processed in one layer.", "count"),
    b("K", "chunk width", "The width in bits of each address chunk carrying one selected bit.", "count"),
    b("\\lambda'", "layer exponent", "The fixed exponent $1-2^{-54}$ in the layer cost $O(Vd^{\\lambda'})$."),
  ])

S5 = show("S5",
  "A multidimensional synthetic transform $F^-_{\\boldsymbol t}$ on $M$ records of $\\mathcal R_r$ with $r=2^\\ell$, and its opposite transform consuming the same stored order, have error below $\\sqrt2\\ell\\,2^{-p}$ and cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ where $T=rM$.",
  "compute radix-two decimation-in-frequency rounds of butterflies and monomial twiddles in $\\mathcal R_r$, arranging the axes so each round's selected bits sit at a common offset in $K$-bit chunks, moved by chunk interchanges and processed by simultaneous layers",
  mot("The simultaneous layer applies only when the selected bits of the participating axes lie at a common offset in consecutive $K$-bit chunks, so a layout must be constructed for every round.", "explicit",
      "To apply Proposition~\\ref{prop:simultaneous-layer} in a transform round,\nwe must place the selected bits of the participating axes at a common\noffset in consecutive $K$-bit chunks."),
  [
    infer("S5.1", "With $\\omega_t=y^{2r/t}$, a $H_0$ butterfly followed by a twiddle $\\omega_t^{-k}$ and two half-length transforms computes $F_t^-$, leaving outputs in bit-reversed stored frequency order.",
      "This computes\n$F_t^-$ because, for $b\\in\\{0,1\\}$,",
      page="synthetic-transforms",
      frm=["ring-y-r-plus-1", "dft", "butterfly-h0", "roots-of-unity"]),
    infer("S5.2", "Each forward or opposite transform procedure has error below $\\sqrt2\\ell\\,2^{-p}$ and costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
      "Each procedure has error less than\n$\\sqrt2\\ell\\,2^{-p}$, returns disk grid coefficients in the same\ncomponent format, and costs",
      frm=["simultaneous-butterfly-layer", "fast-interchange", "error-accounting"]),
  ],
  page="synthetic-transform-layout",
  frm=["synthetic-transforms", "simultaneous-butterfly-layer", "fast-interchange", "ring-y-r-plus-1"],
  adds=[
    b("r", "record length", "The number of complex coefficients in each polynomial record of $\\mathcal R_r$.", "count"),
    b("\\ell", "log record length", "The binary logarithm of $r$, the number of radix-two rounds on a full axis.", "count"),
    b("T", "transform size", "The total number of complex coefficients $rM$ in the transformed array.", "count"),
  ])

S6 = show("S6",
  "The normalized cyclic convolution $\\mathcal M_r(f,g)=(f*g)/T$ of $\\mathcal R_r$-valued arrays is approximated with error below $\\sqrt2M(3\\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
  "apply two forward synthetic transforms kept in their stored frequency order, multiply pointwise by signed packing, and apply the opposite transform, which consumes that order",
  mot("Because the opposite transform consumes the stored frequency order left by the forward transforms, no reordering is needed around the pointwise product.", "explicit",
      "We also specify where each frequency entry\nis stored, because the opposite transform consumes that same order\nafter a pointwise product."),
  [
    infer("S6.1", "Two disk-grid polynomials of $\\mathcal R_r$ are multiplied exactly by packing their signed coefficients into integers for the $O(N\\log N)$ multiplier, returning $Q_p(fg/r)$ in time $O(rp\\log(rp))$.",
      "One can compute the exact Gaussian integer\nnumerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time\n$O(rp\\log(rp))$ on a fixed number of tapes.",
      page="signed-packing",
      frm=["hvdh-multiplier", "ring-y-r-plus-1", "gaussian-dyadics", "two-s-complement-and-signed-integers"]),
    infer("S6.2", "Composing the transforms and products gives $\\mathcal M_r$ with error below $\\sqrt2M(3\\ell+1)2^{-p}$.",
      "$\\mathcal M_r$ on disk grid operands has an approximation with error\nless than",
      frm=["error-accounting"]),
  ],
  page="synthetic-convolution",
  frm=["synthetic-transform-layout", "signed-packing", "cyclic-convolution", "error-accounting"])

S7 = show("S7",
  "With the source and target coordinate permutations $R,Q$ kept inside the resampling identity, $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$; the factor $QF_{\\boldsymbol t}$ is a chirp-wrapped cyclic convolution, and $R$ cancels across forward and inverse source transforms in a convolution.",
  "keep both permutations in the Gaussian resampling identity, apply it line by line in growing dimension, absorb $Q$ into the Bluestein chirp, and cancel $R$ in the convolution",
  mot("Executing the two permutations would require full sorts on every coordinate; keeping them in the formula avoids those sorts.", "explicit",
      "Its usual implementation sorts twice on each\ncoordinate. We retain both permutations in the transform formula and\ncompute that formula directly."),
  [
    infer("S7.1", "Gaussian resampling expresses a Fourier transform of prime length $s$ through one of power-of-two length $t$, between Gaussian contractions.",
      "Gaussian resampling\nconnects these two shapes.",
      page="gaussian-resampling",
      frm=["dft", "hvdh-multiplier", "gaussian-function", "error-accounting"]),
    infer("S7.2", "In one dimension, $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ with contractions $A,B_0$ approximable with error below $p^2$.",
      "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA.",
      frm=["gaussian-resampling", "permutations"]),
    infer("S7.3", "Taking tensor products gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, with axis movement supplied by chunk interchanges as the number of axes grows.",
      "The chunk-swap algorithm supplies the movement of the\nphysical axis fields, including its cost when the number of axes grows.",
      frm=["tensor-products", "fast-interchange"]),
    infer("S7.4", "With chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$, $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$, so the target permutation is absorbed by the chirp.",
      "The chirp identity below performs the frequency change\nin $Q$ without applying $Q$ as a separate permutation of the array.",
      page="bluestein-chirp",
      frm=["retained-permutations", "cyclic-convolution", "dft"]),
    infer("S7.5", "$(RF^+_{\\boldsymbol s})[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$, so the source permutation cancels.",
      "The second identity shows how the\nretained source permutation $R$ cancels when computing a convolution.",
      frm=["cyclic-convolution", "permutations"]),
  ],
  page="retained-permutations",
  frm=["gaussian-resampling", "dft", "tensor-products", "permutations"],
  adds=[
    b("\\gamma", "resampling scale exponent", "The exponent $2d\\alpha^2$ of the power-of-two scale in the tensor resampling identity."),
  ])

P1 = infer("S8",
  "Fix the rational exponents $\\tau=\\sigma=1-2^{-50}$, $\\lambda=1-2^{-52}$, $\\lambda'=1-2^{-54}$, $c=2^{-56}$, $\\epsilon=2^{-75}$, $\\delta=1/16$ and $\\kappa=2^{-182}$, which satisfy all layer and transform conditions.",
  "These constants are deliberately conservative; no optimization is claimed.")
P2 = infer("S9",
  "With $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$ and $T$ a power of two in $[4n/b,8n/b)$, one has $Tp=\\Theta(n)$ and $d=\\Theta(p^\\epsilon)$.",
  "Tp=\\Theta(n),\\quad d=\\Theta(p^\\epsilon),\\quad")

S10 = show("S10",
  "The $2n$-bit product is the carried radix-$2^b$ digit list of $2^{2b+4}S\\,w$, where $w=(u*v)/S$ is computed from the source transforms of the CRT-mapped digit arrays $u,v$ with final error below $1/2$.",
  "map the radix digits by the CRT address map, compute two forward source transforms by resampling, chirps and twisted synthetic convolution, multiply pointwise, apply the opposite transform, rescale, round and propagate carries",
  mot("Each reduction preserves convolution, so solving the final polynomial-ring convolution evaluates all the transforms needed upstream, and known scales can then be undone exactly.", "recoverable"),
  [
    show("S10.1",
      "The map $x\\mapsto\\prod_ix_i^{\\mu_i}$ is an algebra isomorphism from $\\mathbb C[x]/(x^S-1)$ to the multidimensional cyclic ring on prime axes, and its address change is triangular, so it is done by controlled shifts.",
      "use the Agarwal–Cooley split with coordinate powers $\\mu_i=P_i^{-1}\\bmod s_i$ so each new coordinate is an earlier-controlled shift of a mixed-radix digit",
      mot("The chosen coordinate powers make the change of order a sequence of controlled cyclic shifts, which cost linear time.", "explicit",
          "The following map uses that\nalgebraic split, with coordinate powers that make the change of order a\nsequence of controlled cyclic shifts."),
      [
        infer("S10.1.1", "$\\Phi$ is an isomorphism and preserves cyclic convolution.",
          "Hence\n$\\Phi$ is an isomorphism and preserves cyclic convolution.",
          frm=["chinese-remainder-theorem"]),
        infer("S10.1.2", "The axis-$i$ coordinate is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j \\bmod s_i$, a shift controlled by earlier digits.",
          "b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}.",
          frm=["controlled-shifts", "positional-radix-number-systems"]),
      ],
      page="crt-address-map",
      frm=["chinese-remainder-theorem", "cyclic-convolution", "controlled-shifts", "radix-digit-convolution", "greatest-common-divisor-and-modular-inverses"]),
    infer("S10.2", "The twist $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ turns cyclic convolution along the last axis into multiplication in $\\mathcal R_r$, and untwisting recovers the cyclic wrap with the correct sign.",
      "Untwisting therefore recovers the cyclic coefficient with the correct\nsign.",
      page="coefficient-twist",
      frm=["ring-y-r-plus-1", "cyclic-convolution", "roots-of-unity"]),
    infer("S10.3", "The source transform procedure, linewise $\\mathcal A$, the chirp transform, linewise $\\mathcal B_0$ and a scale $2^\\gamma$, has exact counterpart $RF_{\\boldsymbol s}$.",
      "\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A",
      frm=["retained-permutations", "bluestein-chirp", "coefficient-twist", "synthetic-convolution"]),
    infer("S10.4", "After the two forward transforms, pointwise product and opposite transform, the exact counterpart is $(u*v)/S^2$, and the scales $S$ and $2^{2b+4}S$ restore the integer coefficient convolution.",
      "By \\eqref{eq:source-permutation-cancel}, the exact\ncounterpart after the three transforms is $(u*v)/S^2$,",
      frm=["radix-digit-convolution", "retained-permutations"]),
    infer("S10.5", "The final absolute coefficient error is below $1/2$, so rounding gives the exact integer coefficients, and radix-$2^b$ carries give the $2n$-bit product.",
      "The strict error below $1/2$ makes the nearest integer to\nthat value the unique correct coefficient.",
      page="exact-recovery",
      frm=["error-accounting", "radix-digit-convolution", "floor-ceiling-and-rounding", "schoolbook-multiplication-and-carries"]),
  ],
  frm=["radix-digit-convolution", "cyclic-convolution"])

S11 = show("S11",
  "Every per-bit cost term is $O(p^{1-2\\kappa})$ up to fixed powers of $\\log p$, so the total time is $O(n(\\lg n)^{1-\\kappa})$ for all $n$.",
  "divide each cost by $V=Tp$, write each term as a power of $p$, compute the margins below one, and use schoolbook multiplication below a fixed cutoff",
  mot("The smallest margin is $2\\kappa$, leaving a factor $p^{\\kappa}$ of slack to absorb any fixed power of $\\log p$.", "explicit",
      "This explicit slack will cover\nany remaining fixed power of $\\log p$."),
  [
    infer("S11.1", "The seven dominant powers in the cost table have margins below one whose minimum is $2^{-181}=2\\kappa$.",
      "Thus $\\min_i g_i=2^{-181}=2\\kappa$."),
    infer("S11.2", "The large-input bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
      "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})."),
    infer("S11.3", "Below one fixed cutoff, schoolbook multiplication handles the finitely many smaller lengths.",
      "Fix one cutoff beyond all the size, precision, margin and layout\nconditions, and use schoolbook multiplication below it.",
      frm=["schoolbook-multiplication-and-carries"]),
  ],
  page="parameter-choice",
  frm=["synthetic-convolution", "fast-interchange", "simultaneous-butterfly-layer", "logarithms-and-exponentials", "big-o-notation"],
  salient="The worst margin is the chunk-exchange term $g_2=\\epsilon c(1-\\tau)=2^{-181}$, which alone determines $\\kappa=2^{-182}$.")

root = show("S0",
  "One deterministic fixed-tape Turing machine computes the exact $2n$-bit product of two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
  "build two linear-network tape procedures, fast address interchange and simultaneous butterfly layers, from fixed networks with a strict rank saving; use them in synthetic transforms; place these in the Harvey–van der Hoeven reduction through radix digits, a CRT map, Gaussian resampling with retained permutations, Bluestein chirps and a phase twist; and bound every cost term",
  mot("A single scan per transform level already costs $\\Theta(n\\log n)$, so going below $n\\log n$ needs savings in both address movement and butterfly arithmetic.", "explicit",
      "Scanning an array of $\\Theta(n)$ stored bits at each of\n$\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$.\nWe therefore need savings in both movement and arithmetic."),
  [S1, S2, S3, S4, S5, S6, S7, P1, P2, S10, S11],
  page="main-theorem",
  frm=["nlogn-conjecture", "radix-digit-convolution", "hvdh-multiplier", "multitape-turing-machine", "big-o-notation"],
  salient="The exponent saving $\\kappa=2^{-182}$ is tiny but fixed, so the cost is $o(n\\log n)$ through all input lengths, refuting the Schönhage–Strassen conjecture in this model.",
  adds=[
    b("V", "stored bit volume", "The number of data bits in the array a tape procedure operates on.", "count"),
    b("p", "working precision", "The number of fractional bits $6\\lceil\\log_2 n\\rceil$ of the fixed-point grid.", "count"),
  ])

# order check
quotes=[]
def walk(n):
    if n["intention"]=="infer": quotes.append((n["id"], n["quote"]["quote"]))
    for c in n.get("children",[]): walk(c)
walk(root)
pos=-1
for i,q in quotes:
    p=SRC.find(q, pos+1)
    if p<0: print("ORDER PROBLEM", i, SRC.find(q))
    else: pos=p
json.dump({"root": root}, open('/home/user/openai-nlogn-wiki/runs/O2/exegenius/tasks/0003-argument.answer.json','w'), ensure_ascii=False, indent=1)
print("ok", len(quotes))
