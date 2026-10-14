import json, sys

BO = "big-o"; POLY = "polynomials"; CX = "complex-numbers"; TM = "turing-machine-tapes"
MOD = "modular-arithmetic-and-residues"; PRIME = "primes-divisibility-gcd-and-coprimality"
BIN = "binary-representation-of-integers"; XOR = "bitwise-xor"
LOG = "logarithms-floors-ceilings-and-powers-of-two"; MAT = "matrices-invertibility-and-rank"
VS = "vector-spaces-basis-and-dimension"; PERM = "permutations-and-permutation-matrices"
LEX = "lexicographic-order-and-index-tuples"
EUL = "euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle"
GEO = "geometric-series-and-orthogonality-of-sums-of-roots-of-unity"
NORM = "norms-and-the-triangle-inequality"
RAT = "rational-numbers-dyadic-rationals-and-exact-arithmetic"
ALG = "algebraic-structures-groups-rings-and-isomorphisms"
PROOF = "discrete-math-proof-techniques"
SCHOOL = "schoolbook-multiplication-and-divide-and-conquer-multiplication"
MULTI = "multitape-machine-cost-model-and-linear-time-scans"
EVAL = "complex-polynomial-evaluation-and-interpolation"
GAUSS = "gaussian-function"; CONV = "convolution-as-polynomial-multiplication"
ASYM = "quantifiers-sets-and-basic-asymptotic-notation-beyond-big-o"

# pages
P_CONJ = "n-log-n-conjecture"; P_RADIX = "radix-digit-convolution"; P_TRIPLE = "triple-gadget"
P_BANK = "bank-exchange-network"; P_TAPE = "fixed-tape-model"; P_NLOGN = "nlogn-subroutine"
P_STREAM = "stream-arrays"; P_FRAMES = "frames"; P_CSHIFT = "controlled-shifts"
P_BILIN = "bilinear-orthogonal"; P_LABELS = "subspace-labels"; P_TRI = "triangular-factorization"
P_SHEAR = "matrix-shear"; P_PWI = "power-width-interchange"; P_SWAP = "chunk-swap"
P_PACKED = "packed-selected-bits"; P_NEG = "negacyclic-ring"; P_KRON = "signed-kronecker-packing"
P_DISK = "fixed-point-disk-grid"; P_DFT = "dft-cyclic-convolution"; P_MULTID = "multidim-transform"
P_CRT = "crt-axis-map"; P_GAUSSRES = "gaussian-resampling"; P_BLUE = "bluestein-chirp"
P_TWIST = "coefficient-twist"; P_SYNTH = "synthetic-transform"; P_BFLY = "butterfly-layers"
P_PHASE = "phase-kernel-network"; P_SIM = "simultaneous-butterfly-layer"; P_LAYOUT = "transform-layout"
P_RING = "ring-convolution"; P_NOSORT = "resampling-no-sort"; P_CHIRP = "chirp-permutation-cancel"
P_PARAM = "parameter-choice"; P_SRC = "source-transform"; P_EXACT = "exact-recovery"
P_ALG = "multiplication-algorithm"; P_COST = "cost-accounting"; P_MAIN = "main-theorem"

SRC = "paper"


def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


def M(text, source, quote=None):
    d = {"text": text, "source": source}
    if quote:
        d["quote"] = {"source": SRC, "quote": quote}
    return d


def I(id, claim, quote, frm=(), page=None, salient=None, deferred=False):
    d = {"id": id, "intention": "infer", "claim": claim, "quote": {"source": SRC, "quote": quote},
         "from": list(frm)}
    if page:
        d["page"] = page
    if salient:
        d["salient"] = salient
    if deferred:
        d["deferred"] = True
    return d


def S(id, claim, method, mot, children, frm=(), page=None, salient=None, adds=None):
    d = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": mot,
         "children": children, "from": list(frm)}
    if page:
        d["page"] = page
    if salient:
        d["salient"] = salient
    if adds:
        d["adds"] = adds
    return d


# ---------------------------------------------------------------- S5.1 triple gadget
s51 = S(
    "S5.1",
    r"For arbitrary initial scratch values, the eight-row schedule of copy, gather, scatter and side-injection updates indexed by three-element subsets changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.",
    "Add the net coefficient from each control $x_T$ to each target $y_S$ through the central route (gather then scatter) and through the side route (copy then side injection), and check that the sum is the identity for every pair of triples",
    M("The central coefficient depends only on the intersection size $|S\\cap T|$, so a second route is needed to cancel the unwanted sizes; adding the two routes pair by pair shows exactly what is cancelled.", "recoverable"),
    [
        I("S5.1.1", r"The first two rows of the schedule subtract the effect of the old scratch values, the next four introduce the sources and add their effect to the target, and the last two restore the scratch values.",
          r"the following schedule remove the effect of the old scratch values;", [MOD, XOR]),
        I("S5.1.2", r"With $\mathcal V$ copy, $\mathcal G$ gather, $\mathcal J$ side injection and $\mathcal R$ scatter, the net target change is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independent of the initial side and central values $a,c$.",
          r"$(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of", [MAT]),
        I("S5.1.3", r"In the bit construction over $\mathbb F_2$ the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod 2$; the side injection cancels exactly the intersection-one cases, distinct triples with intersection zero or two already have coefficient zero, and the self coefficient is one.",
          r"intersection-one cases; distinct triples with intersection zero or two", [MOD, XOR]),
        I("S5.1.4", r"In the complex construction over $\mathbb Z[i,1/2]$ the central coefficient is $(|S\cap T|-1)/2$; the side injection cancels it for distinct triples with intersection zero or two, intersection one contributes zero, and the self coefficient is one.",
          r"In the complex case, the central coefficient is $(|S\cap T|-1)/2$.", [CX, RAT]),
    ],
    frm=[MOD, XOR, RAT, CX], page=P_TRIPLE,
    salient=r"Although the gather and scatter coefficients depend on the intersection size $|S\cap T|$, the net coefficient is the identity matrix for every pair of triples, with the self coefficient one and every other coefficient cancelled.",
)

s52 = I(
    "S5.2",
    r"Performing a forward invocation from $X$ to $Y$ at stage 1, the inverse schedule from $Y$ to $X$ at stage 2 and a forward invocation from $X$ to $Y$ at stage 3 sends $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restores every auxiliary scratch value.",
    r"$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
    [P_TRIPLE, XOR], page=P_BANK,
    salient=r"Every scratch wire is restored whatever its initial contents, so the exchange needs no clean workspace.",
)

s53 = S(
    "S5.3",
    r"If every incidence of a gate uses the same invertible frame $D_v$ and each edge applies $D_vD_u^{-1}$, the whole network implements $D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}$, so only the edge changes cost anything.",
    "Maintain the invariant that the stored array is the frame applied to the logical array, and check it at the sources, along each edge and across each pointwise linear gate",
    M("Once the scalar routing is fixed, the endpoint frames alone determine the array operator on each route, and the intermediate frames can then be chosen to make each edge change inexpensive.", "explicit",
      "the endpoint frames determine the array operator on each route; the"),
    [
        I("S5.3.1", r"A pointwise gate that is linear commutes with a shared frame: $G(D_vg_1,\ldots,D_vg_t)=D_vG(g_1,\ldots,g_t)$, so the invariant continues through every gate.",
          r"$\sum_j c_jD_v\varphi_j=D_v(\sum_j c_j\varphi_j)$ for each output combination, with", [MAT, ALG]),
        I("S5.3.2", r"Consequently the intermediate frames cancel and the implemented operator is $D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}$, with $D_{\rm in}=\bigoplus_w D_{\mathrm{source}(w)}$ and $D_{\rm out}=\bigoplus_w D_{\mathrm{sink}(w)}$.",
          r"D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}.", [MAT]),
        I("S5.3.3", r"For a signed role permutation sending input role $w$ to $\rho(w)$ with sign $\varepsilon_w$, the route applies $\varepsilon_w D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ to its array, including the auxiliary roles.",
          r"D_{\mathrm{source}(w)}^{-1}$ to its input array.", [PERM]),
    ],
    frm=[P_BANK, MAT, PERM, ALG], page=P_FRAMES,
    salient=r"The intermediate frames cancel entirely: the array operator on each route depends only on the endpoint frames, so the intermediate frames are free to be chosen to make every edge cheap.",
)

# ---------------------------------------------------------------- S5.4 bit count
s54 = S(
    "S5.4",
    r"For the bit network the sum of the ranks of all edge differences is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$, which is strictly less than $W_{\rm b}m$.",
    "Count how label dimensions change along the edges: the signed changes telescope at each gate to $Wm-2N$, absolute values add twice the loss $L$ on the decreasing edges, rational ranks add $N$ for the negative source projections, and $L<N/2$ leaves a positive deficit",
    M("The saving comes from keeping the total dimension lost on decreasing edges small relative to $N$.", "explicit",
      "The saving will come from keeping the total dimension lost on decreasing"),
    [
        I("S5.4.1", r"Every triple indicator line is nondegenerate and neighbouring triple lines are orthogonal, since $\langle t_S,t_T\rangle=|S\cap T|-1$ over $\mathbb Q$ and the ordinary dot product over $\mathbb F_2$, so the label spaces $\mathcal F=F^{\otimes 3}$ have dimension $m$.",
          r"Thus every triple line is nondegenerate, and neighboring triple lines", [VS, P_BILIN]),
        I("S5.4.2", r"The terminal labels make the source dimensions sum to $N$ and the sink dimensions to $Wm-N$, so the signed dimension changes must sum to $Wm-2N$.",
          r"The source dimensions sum to $N$ and the sink dimensions to $Wm-N$.", [VS]),
        I("S5.4.3", r"Along every side wire the successive labels are nested, because $t_X\perp t_Y$ for the neighbouring triples joined by the wire gives $\langle t_X\rangle\subset t_Y^\perp$.",
          r"The first inclusion is possible because $t_X\perp t_Y$.", [P_BILIN, VS]),
        I("S5.4.4", r"Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing the summand $P\otimes F$ of dimension $h$; the data edges and sink edges have zero or nonnegative residual.",
          r"edges are the central-wire edges from time 3 to time 4; their dimension", [VS, P_BILIN]),
        I("S5.4.5", r"The signed dimension changes telescope at every gate, because each touched wire has one incoming and one outgoing incidence with the same gate label, giving $Wm-2N$; with $Ic$ decreasing edges of loss $h$ the loss is $L=Ich$ and the sum of absolute changes is $Wm-2N+2L$.",
          r"The signed sum of dimension changes telescopes at every gate: each", [VS]),
        I("S5.4.6", r"The loss ratios are exactly $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both smaller than $1/2$.",
          r"\frac{L_{\rm b}}{N}=\frac{100}{539},\qquad", [RAT],
          salient=r"Both loss ratios are about $0.19$, far below the threshold $1/2$ that would destroy the saving, so $N-2L>0$ holds with room to spare."),
        S("S5.4.7",
          r"Each edge difference of the rational matrices has rank equal to the dimension change of its labels, except for the $N$ negative source projections, so $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.",
          "Assign the projection $P_U$ to each vertex with label $U$ and compare the rank of $P_V-P_U$ with the dimension change, treating the source projections separately",
          M("The projection difference of nested labels has a computable rank, so the rank sum can be read off the dimension count with only the source edges as exceptions.", "recoverable"),
          [
              I("S5.4.7.1", r"For nested nondegenerate $U\subset V$, the matrix $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement, so its rank is $\dim V-\dim U$, and reversing an edge negates the matrix without changing the rank.",
                r"$P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its", [MAT, VS, P_BILIN]),
              I("S5.4.7.2", r"The exceptions are the $N$ negative source projections $-P_{U_a}$: at stage 1 the first edge on $X_a$ has matrix $2P_{U_a}$ of rank one although its dimension change is zero, which adds $N$ to the rank sum.",
                r"The only exceptions are the $N$ negative source projections.", [MAT]),
              I("S5.4.7.3", r"Hence $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$, whose deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$ because $L_{\rm b}<N/2$.",
                r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.", [MAT]),
          ], frm=[MAT, VS, P_BILIN]),
    ],
    frm=[P_BILIN, VS, MAT, P_TRIPLE, P_FRAMES],
)

# ---------------------------------------------------------------- S5.5 complex variant
s55 = S(
    "S5.5",
    r"For the complex network with binary labels each edge frame change is a product of translation kernels $aI+bX_v$, one per vector of an orthonormal basis of its residual, so the kernel count is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$ and the network applies $C^{\otimes m}$, $C=aI+bX$, to every role.",
    "Define phase frames from the Hamming weight modulo four, express the change of frame across an edge as a product of two-point translation kernels over a residual basis, count one kernel per basis vector, and telescope the frames with corrections",
    M("The same label construction that gave a rank saving for bit arrays must give a saving for complex phase arrays; only the frame changes, and each orthonormal residual vector yields one smaller call.", "recoverable"),
    [
        I("S5.5.1", r"For binary $z,w$ one has $\operatorname{wt}(z+w)=\operatorname{wt}(z)+\operatorname{wt}(w)-2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|$, so when $z\cdot w=0$ the weight is additive modulo four and $q_V(x)-q_U(x)=\sum_{v}\operatorname{wt}(v)[v\cdot x]$ over an orthonormal basis of the residual.",
          r"If $z\cdot w=0$, the intersection cardinality is even, so weight is", [XOR, MOD]),
        I("S5.5.2", r"Each basis vector $v$ has norm one, hence odd weight, so its phase is $i^{\varepsilon[v\cdot x]}=\frac{1+i^{\varepsilon}}{2}+\frac{1-i^{\varepsilon}}{2}(-1)^{v\cdot x}$ with $\varepsilon=\pm1$, which after conjugating by $H^{\otimes m}$ is the translation kernel $aI+bX_v$ or its inverse.",
          r"+\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}.", [CX, EUL]),
        I("S5.5.3", r"Counting one kernel per residual basis vector gives $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$ with no extra source contribution, a deficit of $2N-2L_{\rm c}>0$ from $W_{\rm c}m$.",
          r"The deficit is $2N-2L_{\rm c}>0$.", [VS]),
        I("S5.5.4", r"Telescoping the phase frames gives $C^{\otimes m}$ on every role, including the scratch roles; the one exceptional pair $X_a\to Y_a$ carries $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u_a)$, which the identity $C=iZC^{-1}Z$ with sign and phase corrections turns into $C$.",
          r"the identity $C=iZC^{-1}Z$ turns each of them into $C$.", [CX, MAT],
          salient=r"The result is the same operator $C^{\otimes m}$ on every role, scratch roles included, although the frames differ along the way."),
        I("S5.5.5", r"The kernel $C=H\mathsf SH=aI+bX$ with $a=(1+i)/2$, $b=(1-i)/2$ satisfies $H_0=b\,\mathsf S C\mathsf S$, so a layer of butterflies $H_0$ is a layer of $C$ conjugated by diagonal phases.",
          r"H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad", [CX], deferred=True),
    ],
    frm=[P_LABELS, P_FRAMES, P_BANK, P_TRIPLE, P_BILIN, CX, XOR, EUL], page=P_PHASE,
    salient=r"The corrected network applies the identical operator $C^{\otimes m}$ on every role, including auxiliary roles whose contents are arbitrary.",
)

# ---------------------------------------------------------------- S5.6 exponent
s56 = S(
    "S5.6",
    r"Both networks satisfy $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$ with the fixed rational exponent $\tau=\sigma=1-2^{-50}<1$.",
    "Compare the relative rank deficits with $20\\cdot2^{-50}$ and bound $m^{1-2^{-50}}$ below by $m(1-20\\cdot2^{-50})$ using $\\log m<20$",
    M("The recursion needs a fixed rational exponent with $s/W<m^\\tau$, so the tiny deficits must be turned into an explicit exponent by an exponential inequality.", "recoverable"),
    [
        I("S5.6.1", r"The relative deficits $\eta_{\rm b}=339/22587335000000$ and $\eta_{\rm c}=73/19906842167500$ both exceed $20\cdot2^{-50}$.",
          r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$.", [RAT]),
        I("S5.6.2", r"Since $m<2^{20}$ gives $\log m<20$, one has $m^{1-2^{-50}}=m\exp(-2^{-50}\log m)>m(1-20\cdot2^{-50})>m(1-\eta)$ for $\eta=\eta_{\rm b}$ or $\eta_{\rm c}$.",
          r"Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence", [LOG]),
        I("S5.6.3", r"Consequently $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$, with $0<\tau=\sigma<1$.",
          r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,", [LOG]),
    ],
    frm=[LOG, RAT],
    salient=r"The saving exponent $\tau=1-2^{-50}$ is extraordinarily close to one because the relative deficits are only about $10^{-14}$; this is the source of the astronomically small $\kappa$.",
)

# ---------------------------------------------------------------- S5.7 / S5.8 triangular, shear
s57 = I(
    "S5.7",
    r"Every rational square matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation matrix with exactly $a$ ones (the zero matrix has $E_1=E_2=I$ and $\Pi=0$).",
    r"$\Pi$ has exactly $a$ entries equal to one, with at most one in each row",
    [MAT, PERM], page=P_TRI,
)

s58 = S(
    "S5.8",
    r"For a fixed finite set of rational matrices there is a fixed odd prime $q$ such that the address update $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ is performed with exactly $\operatorname{rank}(A)$ interchanges of pairs of $b$-digit fields and $O(V)$ further work.",
    "Factor $A=E_1\\Pi E_2$, apply the lower triangular factors as linear-time controlled shifts, and realise each one of $\\Pi$ as an interchange sandwiched between two controlled shifts",
    M("Lower triangular changes of coordinates update a later field from earlier fields and so can be performed entirely in the direction that controlled shifts allow.", "explicit",
      "can be performed entirely in this direction."),
    [
        I("S5.8.1", r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$, because coordinates are updated in descending physical order, each by multiplying by a diagonal unit and adding a fixed combination of earlier coordinates that still hold their original values.",
          r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:", [P_CSHIFT, P_TRI, MOD]),
        I("S5.8.2", r"For $A=E_1\Pi E_2$, transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, then add $\Pi D$ to $H$, and finally transform $H$ by $E_1$ and $D$ by $E_2^{-1}$.",
          r"For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,", [P_TRI, MAT]),
        I("S5.8.3", r"Each one at position $(i,j)$ of $\Pi$ performs $H_i\leftarrow H_i+D_j$ by the sequence $D_j\leftarrow D_j+H_i$, then interchange $(H_i,D_j)\leftarrow(D_j,H_i)$, then $D_j\leftarrow H_i-D_j$, which uses just one interchange.",
          r"(H_i,D_j)\leftarrow(D_j,H_i),\qquad", [P_CSHIFT]),
        I("S5.8.4", r"Since $\Pi$ has exactly $a=\operatorname{rank}(A)$ ones, the number of interchanges, and so of recursive calls, is exactly the rational rank $a$.",
          r"There are $a$ ones, which proves the", [MAT]),
    ],
    frm=[P_TRI, P_CSHIFT, P_STREAM, MOD, MAT], page=P_SHEAR,
)

# ---------------------------------------------------------------- S5.9 power width interchange
s59 = S(
    "S5.9",
    r"Two disjoint contiguous chunks of $e=m^k$ radix-$q$ digits can be interchanged in $O(Ve^\tau)$ time, with a row field of length divisible by $W^k$ preceding both chunks.",
    "Split whole rows cyclically into $W$ role streams of volume $V/W$ and run the bank-exchange network on them, with every edge a shear $\\Phi_{A_e}$ costing rank-many smaller interchanges; turn the middle shear into an interchange; then solve the recurrence $F_k\\le (s/W)F_{k-1}+O(1)$ using $s/W<m^\\tau$",
    M("Because the sum of the edge ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width.", "explicit",
      "$m$, the resulting recurrence saves a power of the chunk width."),
    [
        I("S5.9.1", r"Splitting whole rows cyclically into the $W$ role streams gives streams of the same shape, each of logical volume $V/W$ with row count divisible by $W^{k-1}$.",
          r"logical volume $V/W$, and its row count is divisible by $W^{k-1}$.", [P_STREAM, P_BANK]),
        I("S5.9.2", r"On every circuit edge apply $\Phi_{A_e}$, the address shear $(H,D)\mapsto(H+A_eD,D)$, to that role stream, implemented by recursively interchanging each pivot pair of $b$-digit fields with $b=e/m$.",
          r"Lemma~\ref{lem:matrix-shear}, recursively interchanging each pivot pair", [P_SHEAR]),
        I("S5.9.3", r"By the common-frame identity and the endpoint condition $M_{\mathrm{out}(\rho(w))}-M_{\mathrm{in}(w)}=I_m$, every role array receives the shear $H\leftarrow H+D$, scratch roles with arbitrary contents included.",
          r"routes $g_w$ to role $\rho(w)$. Thus its physical output satisfies", [P_FRAMES, P_LABELS]),
        I("S5.9.4", r"The three updates $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ send $(H,D)$ to $(D,H)$, and only the middle shear uses the circuit.",
          r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,", [P_SHEAR]),
        I("S5.9.5", r"The number of recursive calls at a node is the sum of the edge ranks, exactly $s$, and each acts on one role stream of volume $V/W$.",
          r"The number of recursive calls is the sum of the edge ranks, exactly $s$.", [P_LABELS]),
        S("S5.9.6",
          r"If $F_k$ is the time divided by logical volume for width $m^k$, then $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$, and this solves to $F_k=O(e^\tau)$.",
          "Unroll the recurrence into the geometric sum $\\sum_{j=0}^k a^j$ with $a=s/W<m^\\tau$ and treat the cases $a\\le1$ and $a>1$ separately",
          M("Each call acts on volume $V/W$ and there are $s$ of them, so the normalised cost is multiplied by $s/W$ per level, and a geometric sum with ratio below $m^\\tau$ is of the order of its last term.", "recoverable"),
          [
              I("S5.9.6.1", r"The recurrence is $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$: the $s$ child calls cost $s(V/W)F_{k-1}$, and splitting, merging, gates and triangular operations cost $O(V)$ because their number is fixed.",
                r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1).", [P_LABELS]),
              I("S5.9.6.2", r"If $a=s/W\le1$ the geometric sum $\sum_{j=0}^k a^j$ is at most $k+1=O(m^{k\tau})$.",
                r"If $a\le1$, the sum is at", [GEO, BO]),
              I("S5.9.6.3", r"If $a>1$ the sum is $O(a^k)$, and $a<m^\tau$ gives $a^k<m^{k\tau}$.",
                r"most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$.", [GEO, BO]),
              I("S5.9.6.4", r"Hence $F_k=O(e^\tau)$, since $e=m^k$ gives $m^{k\tau}=e^\tau$.",
                r"Hence $F_k=O(e^\tau)$.", [BO, LOG]),
          ], frm=[BO, GEO, LOG, P_LABELS]),
        I("S5.9.7", r"Scheduling the recursive calls depth first on a fixed number of tapes costs only an additional $O(V)$ at each node, because pushing, popping, copying and erasing the parked role streams move $O(V)$ symbols at the parent.",
          r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$", [P_TAPE, P_STREAM]),
        I("S5.9.8", r"Descriptor processing is also absorbed: the root volume $V_0$ and a depth-$j$ child volume $V_j$ satisfy $\log V_0=\log V_j+j\log W=O(\log(2V_j))$, so setup polynomial in $\log V_0$ costs $O(V_j)$.",
          r"$\log V_0=\log V_j+j\log W=O(\log(2V_j))$.", [LOG, P_STREAM]),
    ],
    frm=[P_SHEAR, P_LABELS, P_FRAMES, P_BANK, P_STREAM, P_TAPE, P_CSHIFT], page=P_PWI,
    salient=r"Although every node of the recursion makes $s$ calls, the cost per unit volume grows only like $e^\tau$ with $\tau<1$, because each call works on a stream of volume $V/W$ and $s/W<m^\tau$.",
    adds=[
        B("e", "chunk width", "the number $m^k$ of radix-$q$ digits in each of the two chunks being interchanged", "count"),
        B("F_k", "normalised cost", "the time to interchange chunks of $m^k$ digits divided by the logical volume", "direct"),
    ],
)

# ---------------------------------------------------------------- S5.10 chunk swap
s510 = S(
    "S5.10",
    r"Two disjoint address chunks of $u$ bits in any bit array on $[P]\times[2^u]\times[G]\times[2^u]\times[B]$ are interchanged in $O(Vu^\tau)$ steps for a fixed $\tau<1$.",
    "Move the top $\\rho$ digits of each chunk into a padded row field, split the remaining width in base $m$ into power-width pieces, interchange each piece with the power-width procedure, and undo the padding and the high-digit moves",
    M("The power-width procedure needs a long row field and a width that is a power of $m$, and rows for a general array can be supplied by a few of its own high digits.", "explicit",
      "Rows for a general array can be supplied by a few of its own high digits."),
    [
        I("S5.10.1", r"Exchanging the top $\rho=\lceil k\log W/(2\log q)\rceil$ digits and joining them gives a row field of range $R=q^{2\rho}\ge W^k$ before both remaining chunks, at cost $O(V\rho)$ with $\rho=O(\log(2e))$.",
          r"R=q^{2\rho}\ge W^k", [P_PWI, P_STREAM]),
        I("S5.10.2", r"Appending zero rows within each prefix until the row count is $R'=W^k\lceil R/W^k\rceil<2R$ makes the row field divisible by $W^k$ and at most doubles the volume.",
          r"R'=W^k\left\lceil R/W^k\right\rceil<2R.", [P_PWI]),
        I("S5.10.3", r"Writing the remaining width in base $m$ as $e-\rho=\sum_{j=0}^{k}a_jm^j$ with $0\le a_j<m$ partitions each chunk into $a_j$ pieces of width $m^j$, and every piece pair is interchanged by the power-width procedure with the same padded row field.",
          r"e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m.", [P_PWI, LOG]),
        I("S5.10.4", r"The costs add up to $O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)$, because $a_j<m$ is bounded and $m^k<me$ makes the sum geometric of the order of its top term.",
          r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau).", [GEO, BO]),
        I("S5.10.5", r"Scanning away the padded rows and reversing the joining moves costs $O(V\log(2e))$, which is $O(Ve^\tau)$.",
          r"remaining movement cost $O(V\log(2e))$ is $O(Ve^\tau)$.", [P_STREAM]),
        I("S5.10.6", r"For binary chunks of $u$ bits, pad each range from $[2^u]$ up to $[q^e]$ with $e$ least such that $q^e\ge2^u$, interchange, and scan away the invalid entries; the volume grows by less than a fixed factor $q^2$ and $e=O(u)$, giving $O(Vu^\tau)$.",
          r"Finally, for binary chunks let $e$ be the least integer with", [P_STREAM, BIN]),
    ],
    frm=[P_PWI, P_STREAM, BIN], page=P_SWAP,
)

# ---------------------------------------------------------------- S5.11 simultaneous layer
packed = S(
    "S5.11.5",
    r"On a rectangle with three chunks of $L=fK$ bits, the binary row addition $y\leftarrow y\oplus x$ on the selected bit of each of $f$ chunks at once, restoring the third chunk $z$, takes $O(V(L^\tau+1))$ time under the family hypotheses.",
    "Perform eight packed cyclic shifts of whole chunk ranges that realise the XORs except at addresses whose guard values are near an end of their range, then repair that small explicitly identified set deterministically by sorting",
    M("The cyclic shifts cost only linear time apart from swaps, and the addresses where a segment could carry into its neighbour form a tiny fraction determined by the guard width.", "explicit",
      "of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of"),
    [
        I("S5.11.5.1", r"For a Boolean control $c$, the eight conditional updates of $u$ and $w$ by parity compose to the permutation that flips the parity of $u$ exactly when $c=1$ (the cycles $(00\ 01\ 10)$ and $(01\ 10\ 11)$ compose to $(00\ 10)(01\ 11)$), preserving both quotients under division by two and restoring the auxiliary integer $w$.",
          r"is flipped precisely when $c=1$, both quotients under division by two are", [XOR, PERM]),
        I("S5.11.5.2", r"At an address whose guard values all lie in $10\le g\le 2^{K-1}-11$, displacement at most eight keeps each $K$-bit segment inside $[0,2^K-1]$, so no segment carries into or borrows from the next and the packed shift agrees with the independent segment additions.",
          r"10\le g\le 2^{K-1}-11.", [MOD]),
        I("S5.11.5.3", r"Each guard excludes exactly twenty values out of $2^{K-1}$, so the union bound over the $2(f-1)$ guards bounds the set $\mathcal B$ of bad addresses by $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, independently of the payload.",
          r"|\mathcal B|\le\delta_{\rm bad}M.", [ASYM]),
        I("S5.11.5.4", r"The ideal map $T_0$ and the packed composition $S_0$ are bijections that agree off $\mathcal B$ and both preserve $\mathcal B$, so $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$.",
          r"Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$.", [PERM]),
        I("S5.11.5.5", r"The shifts use at most sixteen chunk swaps and eight rotations in $S_0$, costing $O(VL^\tau)$ by the arbitrary-width interchange and linear time by the controlled shifts.",
          r"There are at most sixteen swaps and eight rotations in $S_0$.", [P_SWAP, P_CSHIFT]),
        I("S5.11.5.6", r"The correction extracts the records of $\mathcal B$ with destination ranks as keys, sorts them stably by radix passes and reinserts them in one scan, which implements $T_0$ everywhere.",
          r"This implements $T_0$ everywhere.", [P_STREAM]),
        I("S5.11.5.7", r"The movement costs $O(V(L^\tau+1))$, a fixed number of record scans costs $O(MA_{\rm rect}^3+V)$, and the radix passes cost $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$.",
          r"The movement costs $O(V(L^\tau+1))$.", [BO]),
        I("S5.11.5.8", r"When $A_{\rm rect}=O(p)$, $R$ exceeds every fixed polynomial in $p$, $f\le d\le p$ and $K/\log p\to\infty$, the additional normalised terms are $o(1)$, so the time is $O(V(L^\tau+1))$.",
          r"$O(p^2 2^{-K}(1+A_{\rm rect}/R))=o(1)$. This proves the final assertion.", [ASYM]),
        I("S5.11.5.9", r"A fixed binary change of basis on $e$ axis chunks is a fixed number of such row additions, so the change of basis and its inverse cost $O(V((eK)^\tau+1))$.",
          r"$O(V((eK)^\tau+1))$ on a stream of volume $V$.", [MAT, XOR]),
    ],
    frm=[P_SWAP, P_CSHIFT, P_STREAM, XOR], page=P_PACKED,
)

recurrence = S(
    "S5.11.6",
    r"Applying $C^{\otimes e}$ to $e=m^k$ selected axes costs normalised time $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ and this solves to $O(d^{\lambda'})$ for a whole layer.",
    "Recurse on the $m$ slots with $s$ child calls on streams of volume $V/W$ obtained by splitting rows, stop below $d^{\\beta}$ axes, sum the internal costs as a geometric series, bound the leaves, and combine the base-$m$ pieces",
    M("The child calls are executed on streams of volume $V/W$, so dividing their total cost by the current volume leaves the factor $s/W$ in front of the recursion.", "explicit",
      "Indeed, the \\(s\\) child calls are executed on streams of volume"),
    [
        I("S5.11.6.1", r"Applying $e$ individual $C$ kernels costs $O(Ve)$, so recursion stops when $e<d^\beta$ with $\beta=1/2$.",
          r"\(O(Ve)\) on any stream with these complete ranges and record format.", [P_STREAM]),
        I("S5.11.6.2", r"An internal node on $e=m^k$ chunks makes exactly $s$ slot calls and its binary basis changes, scalar gates and reassembly cost $O(V((eK)^\tau+1))$.",
          r"O\bigl(V((eK)^\tau+1)\bigr)", [P_PACKED]),
        I("S5.11.6.3", r"The first $q_0$ chunks are processed individually and their bits form a row index of range $R_{\rm row}=2^{q_0K}\ge W^{k_0}$, padded to a multiple of $W^{k_0}$, so rows can be split among the $W$ roles at each of the depth-$j\le k_0$ levels.",
          r"\(R_{\rm row}=2^{q_0K}\ge W^{k_0}\)", [P_PWI]),
        I("S5.11.6.4", r"Every recursive edge call acts on one role stream with volume exactly $1/W$ of its parent's logical volume, because rows remain complete.",
          r"one role stream with volume exactly \(1/W\) of its parent's logical", [P_PWI, P_FRAMES]),
        S("S5.11.6.5",
          r"With $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, $F(e)=O(e)$ for $e<d^\beta$ and $\tau(1+c/\beta)<\lambda$, the whole layer costs $O(d^{\lambda'})$ per unit volume.",
          "Bound the overhead by $O(e^\\lambda)$, sum the internal levels as a geometric series with ratio $a/m^\\lambda<1$, bound the leaf contribution by $e^\\sigma d^{\\beta(1-\\sigma)}$, then add the logarithmically many base-$m$ pieces",
          M("The overhead exponent and the branching ratio $a=s/W$ must both stay below $m^\\lambda$ for the levels to sum geometrically, which dictates the constraints on $\\lambda$, $\\sigma$ and $\\lambda'$.", "recoverable"),
          [
              I("S5.11.6.5.1", r"At an internal node $e\ge d^\beta$ one has $K\le d^c\le e^{c/\beta}$, so the overhead is $O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)$.",
                r"\(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\)", [BO, LOG]),
              I("S5.11.6.5.2", r"With $a=s/W\le m^\sigma<m^\lambda$ the internal costs sum to at most $Ce^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)$.",
                r"C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda).", [GEO]),
              I("S5.11.6.5.3", r"Leaves after $j$ levels, each with $u=e/m^j<d^\beta$ chunks, contribute at most $O(a^ju)\le O(e^\sigma u^{1-\sigma})\le O(e^\sigma d^{\beta(1-\sigma)})$.",
                r"O(a^ju)\le O(e^\sigma u^{1-\sigma})", [BO]),
              I("S5.11.6.5.4", r"The first inequality uses $a^j\le m^{j\sigma}=(e/u)^\sigma$, and it also covers $a<1$ by taking $\sigma\ge0$.",
                r"\(a^j\le m^{j\sigma}=(e/u)^\sigma\)", [BO]),
              I("S5.11.6.5.5", r"Writing $D-q_0=\sum_j a_jm^j$ in base $m$ partitions the remaining chunks into at most $(m-1)(1+\lfloor\log_m d\rfloor)$ consecutive pieces.",
                r"Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\).", [LOG]),
              I("S5.11.6.5.6", r"Adding the pieces and the row preprocessing gives $O(\log(2d)[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1])=O(d^{\lambda'})$ for any fixed $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$, the strict inequality absorbing the logarithmic number of pieces.",
                r"\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1.", [BO]),
          ], frm=[GEO, BO, LOG]),
    ],
    frm=[P_LABELS, P_PWI, P_PACKED, GEO, BO],
    salient=r"A whole layer on $d$ axes costs $O(d^{\lambda'})$ per unit volume with $\lambda'<1$ instead of the $d$ passes needed for separate butterfly factors.",
)

guard = S(
    "S5.11.7",
    r"Every intermediate coefficient of the exactly evaluated layer is represented in $p+\Delta$ fractional and $\Delta+3$ integer bits with $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$, so the width stays $O(p)$.",
    "Bound the depth of the longest arithmetic chain by the recurrence $A(e)\\le sA(e/m)+E$ over the $k\\le\\lceil\\log_m d\\rceil$ levels and convert depth into denominator and magnitude growth",
    M("The accelerated network is evaluated exactly until an entire normalised butterfly layer is complete, and its intermediate operators need not be contractions, so explicit constants must bound denominator and magnitude growth within one layer.", "explicit",
      "The accelerated network is evaluated exactly until an entire"),
    [
        I("S5.11.7.1", r"Let $A(e)$ bound the number of additions, halvings, sign changes and multiplications by $i$ on any chain into an intermediate coefficient; then $A(e)\le sA(e/m)+E$ at an internal node and $A(e)\le8e$ at a leaf, where $E=64(W+m+1)^3$ bounds the gates and corrections of one network invocation.",
          r"A(e)\le sA(e/m)+E", [BO]),
        I("S5.11.7.2", r"The depth recurrence concatenates all $s$ child calls and therefore uses $s$ rather than the factor $s/W$ of the time recurrence.",
          r"The depth estimate concatenates the \(s\) calls, so it uses \(s\).", [BO]),
        I("S5.11.7.3", r"With $B=s+E$, any bound $x\ge1$ satisfies $sx+E\le(s+E)x=Bx$, so starting from $8e\le8d\le8dB$ at a leaf and applying this inequality through the levels gives $A(e)\le8dB^{k+1}$.",
          r"For any bound \(x\ge1\), \(sx+E\le(s+E)x=Bx\).", [BO]),
        I("S5.11.7.4", r"With $\nu=\min\{j\ge1:m^j\ge B\}$ and $k\le\lceil\log_m d\rceil$, one has $B^{k+1}\le B^{\log_m d+2}=B^2d^{\log_m B}\le B^2d^\nu$.",
          r"=B^2d^{\log_m B}\le B^2d^\nu.", [LOG]),
        I("S5.11.7.5", r"Therefore $A(e)\le8dB^{k+1}\le8B^2d^{\nu+1}$ for one group of $e$ axes.",
          r"A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}.", [BO]),
        I("S5.11.7.6", r"Concatenating at most $md$ pieces, the individual kernels and the outer diagonals gives a common bound $<128mB^2d^{\nu+3}\le C_0d^{C_1}$ for denominator and magnitude growth, with $C_1=\max\{20,\nu+3\}$ and $C_0=128mB^2$.",
          r"<128mB^2d^{\nu+3}\le C_0d^{C_1}.", [BO]),
        I("S5.11.7.7", r"A value at depth $\ell$ lies in $2^{-(p+\ell)}\mathbb Z[i]$ with modulus at most $2^\ell$, since addition at most doubles the modulus and halving adds one denominator bit, so $p+\Delta$ fractional and $\Delta+3$ integer bits suffice.",
          r"lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most", [NORM, RAT]),
        I("S5.11.7.8", r"Choosing $\epsilon C_1<1$ with $d=\Theta(p^\epsilon)$ gives $\Delta=o(p)$, so the full coefficient width is $O(p)$ as the time analysis requires.",
          r"\(\Delta=o(p)\)", [ASYM]),
    ],
    frm=[BO, LOG, NORM, RAT],
)

final_layer = S(
    "S5.11.8",
    r"The procedure returns $Q_p(\mathcal H z)$ in $O(Vd^{\lambda'})$ time, with every coefficient in the unit disk and error below $\sqrt2\,2^{-p}$ from $\mathcal H z$.",
    "Verify the packed-call hypotheses uniformly over the allowed $d$ and $r$, apply the recurrence, convert $C^{\\otimes D}$ to $\\mathcal H$ by diagonal phases, and bound the single final truncation",
    M("The result must hold with one time constant for every allowed pair $(d,r)$ and every payload, so the hypotheses of the packed procedure are checked in bands and the truncation error is bounded once.", "recoverable"),
    [
        I("S5.11.8.1", r"Both extra normalised terms of the packed rectangle bound tend to zero uniformly over all allowed $d,r$, so every packed call has cost $O(M_{\rm child}R_{\rm g}(L^\tau+1))$ with one common constant.",
          r"Both bounds tend to zero uniformly over all current allowed $d,r$.", [ASYM]),
        I("S5.11.8.2", r"The row construction and the recurrence analysis give total time $O(Vd^{\lambda'})$ on fixed tapes, including all padded and auxiliary streams.",
          r"above give total time $O(Vd^{\lambda'})$ on fixed tapes, including", [BO]),
        I("S5.11.8.3", r"Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays.",
          r"absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk", [NORM]),
        I("S5.11.8.4", r"Truncation toward zero cannot increase the absolute value of either component and changes each by less than $2^{-p}$, so the error is below $\sqrt2\,2^{-p}$.",
          r"error less than $\sqrt2\,2^{-p}$: truncation cannot increase the", [NORM]),
    ],
    frm=[BO, NORM],
)

s511 = S(
    "S5.11",
    r"The normalized butterfly $H_0$ is applied to the selected bit in each of $d$ address chunks of polynomial records of a stream of volume $V$, exactly in Gaussian dyadics followed by a single truncation $Q_p$, in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$.",
    "Write the layer as $b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$, realise $C^{\\otimes e}$ on groups of $e=m^k$ axes by the complex network with its $s$ children on slots of $e/m$ axes, implement the binary basis changes by packed selected-bit additions, and solve the resulting recurrence with explicit guard bits",
    M("Applying the butterfly factors one axis at a time would need $D$ whole-array passes, whereas the recursive network gives a power saving over the number of axes.", "explicit",
      "factors would require $D$ whole-array passes."),
    [
        I("S5.11.1", r"On a group of $e=mf$ axes, an edge frame change equals $\mathcal P_M\bigl(\prod_{j}C_{e_j}^{\epsilon_j}\bigr)\mathcal P_M^{-1}$ for an invertible binary matrix $M$ whose first columns are the residual basis, so each basis vector yields one child call on the $f$ axes of one slot.",
          r"=\mathcal P_M\left(\prod_{j=1}^{\rho_{\rm edge}}C_{e_j}^{\epsilon_j}\right)", [P_PHASE, MAT]),
        I("S5.11.3", r"A negative directional kernel still needs only one forward child, because $(C^{-1})^{\otimes f}=(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}$ with address signs and fourth-root phases that add no calls.",
          r"=(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}.", [P_PHASE, CX]),
        I("S5.11.2", r"Gaussian elimination expresses $M\in\operatorname{GL}(m,\mathbb F_2)$ as at most $m(m-1)+3m$ elementary row additions, each of which XORs corresponding selected bits of two whole slots at once.",
          r"Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$", [MAT, XOR]),
        I("S5.11.4", r"Summing the residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and the network gives $C^{\otimes e}$ on every role, including roles with arbitrary scratch values.",
          r"$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot.", [P_PHASE, P_LABELS]),
        I("S5.11.4b", r"Applying the basic identities on all selected coordinates gives $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$ with $b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}$, a binary shift and fourth-root phase, so the layer is exact up to its final truncation.",
          r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D.", [P_PHASE, CX]),
        packed,
        recurrence,
        guard,
        final_layer,
    ],
    frm=[P_PHASE, P_PACKED, P_SWAP, P_PWI, P_BFLY, P_DISK, P_FRAMES, P_LABELS, CX],
    page=P_SIM,
    salient=r"The layer on $d$ axes costs $O(Vd^{\lambda'})$ with $\lambda'<1$, although separate butterfly factors would cost $d$ whole-array passes; the exact Gaussian dyadic arithmetic needs only $o(p)$ extra bits per coefficient.",
    adds=[
        B("d", "axis count", "the number of address chunks, one per axis, on which the layer acts", "count"),
        B("K", "chunk width", "the number of bits in each address chunk", "count"),
        B("\\lambda'", "layer exponent", "a fixed exponent below one bounding the layer cost per unit volume by $d^{\\lambda'}", "direct"),
    ],
)

# ---------------------------------------------------------------- KEY S5
key = S(
    "S5",
    r"Interchanging two address chunks of $u$ bits costs $O(Vu^\tau)$ and a simultaneous butterfly layer on $d$ axes costs $O(Vd^{\lambda'})$, because in both fixed linear networks the total number $s$ of smaller calls is strictly below $Wm$.",
    "Realise each tape operation by a fixed linear network that exchanges two banks and restores every scratch value, attach nested subspace labels so that each edge change needs only rank-many smaller calls, prove the total rank is below the number of wires times the label dimension, and solve the recursion on streams of volume $V/W$",
    M("Each call of the recursion acts on a stream of volume $V/W$, so the recursive contribution grows by the factor $s/W<m$ per level, and this strict inequality is the source of the power saving.", "explicit",
      "is the source of the power saving."),
    [s51, s52, s53, s54, s55, s56, s57, s58, s59, s510, s511],
    frm=[P_BILIN, VS, MAT, P_FRAMES, P_BANK, P_TRIPLE, P_STREAM],
    page=P_LABELS,
    salient=r"The decisive inequality $s<Wm$ is extremely thin (the relative deficit is about $10^{-14}$) yet suffices for a power saving $\tau=1-2^{-50}$; it holds in both the bit network and the complex network, and only the labels and the $N-2L$ or $2N-2L$ count explain why.",
    adds=[
        B("W", "wire count", "the number of wires in the fixed linear network, including its scratch wires", "count"),
        B("m", "label dimension", "the dimension of the fixed ambient label space, equal to the number of digits or axes per recursion step", "count"),
        B("s", "call count", "the sum of the ranks of all edge differences, i.e. the number of smaller calls per node", "count"),
        B("N", "data wire count", "the number of data wires in each of the two banks", "count"),
        B("L", "dimension loss", "the total dimension lost along decreasing edges", "count"),
        B("\\tau", "saving exponent", "a fixed rational exponent below one with $s/W<m^\\tau$", "direct"),
    ],
)

# ================================================================= transforms and ring convolution
rc1 = S(
    "S6.1",
    r"The synthetic Fourier transforms $F_t^\pm$ over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ with roots $\omega_t=y^{2r/t}$ are contractions satisfying $F_t^+F_t^-=t^{-1}I$ despite zero divisors.",
    "Prove the character sum $\\sum_k\\omega_t^{jk}$ equals $t$ or $0$ directly, by shifting the summation index to multiply the sum by $-1$, rather than dividing by $\\omega_t^j-1$",
    M("The ring has zero divisors, so character cancellation is verified directly instead of dividing by $\\omega_t^j-1$.", "explicit",
      "The ring has zero divisors, so we verify character cancellation"),
    [
        I("S6.1.1", r"Every power of $\omega_t$ is an isometry and each transform entry is an average of $t$ such images, so both transforms are contractions.",
          r"Every power of $\omega_t$ is an isometry, and each transform entry is", [NORM, P_NEG]),
        I("S6.1.2", r"The sum $\sum_{k=0}^{t-1}\omega_t^{jk}$ equals $t$ if $t\mid j$ and $0$ if $t\nmid j$.",
          r"=\begin{cases}t,&t\mid j,\\0,&t\nmid j.\end{cases}", [GEO, EUL]),
        I("S6.1.3", r"If $t\nmid j$, write $j=2^vj_0$ with $j_0$ odd; replacing $k$ by $k+t/2^{v+1}$ permutes the summands and multiplies the sum by $y^{rj_0}=-1$.",
          r"Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes", [P_NEG]),
        I("S6.1.4", r"Hence the sum is zero, since the additive group of $\mathcal R_r$ has no two-torsion, and expanding the composite transforms gives $F_t^+F_t^-=t^{-1}I$.",
          r"and applying this identity proves the final formula.", [ALG]),
    ],
    frm=[P_NEG, P_DFT, GEO, EUL, ALG], page=P_SYNTH,
    salient=r"Although $\mathcal R_r$ has zero divisors, the inversion identity $F_t^+F_t^-=t^{-1}I$ holds exactly as for the ordinary Fourier transform.",
)

rc2 = S(
    "S6.2",
    r"Decimation in frequency computes $F_t^-$ by pairing $z_k$ with $z_{k+t/2}$, applying $H_0$ and a twiddle monomial, and leaves the frequencies in bit-reversed order $B_t$; the procedure reversed level by level implements $F_t^+B_t^{-1}$.",
    "Split the transform sum into even and odd frequencies to obtain the recursion, track which slot holds each frequency bit, and traverse the levels in reverse for the opposite transform",
    M("The pairing recursion needs only butterflies and monomial shifts, and writing outputs directly in the slot order avoids moving whole frequency indices.", "recoverable"),
    [
        I("S6.2.1", r"For $b\in\{0,1\}$, $(F_t^-z)_{2h+b}$ is a length-$t/2$ transform of the inputs $\frac{z_k+(-1)^bz_{k+t/2}}2$ twisted by $\omega_t^{-bk}$, which is the decimation-in-frequency step.",
          r"\frac{z_k+(-1)^b z_{k+t/2}}2.", [P_DFT, P_SYNTH]),
        I("S6.2.2", r"After all $a=\log_2t$ rounds the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$, so the stored order is the bit reversal $B_t$.",
          r"entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$.", [PERM, BIN]),
        I("S6.2.3", r"Since $H_0^2=I/2$, each reversed level is half the inverse of the forward level, so the reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$, and the two procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
          r"B_tF_t^-,\qquad F_t^+B_t^{-1},", [MAT]),
        I("S6.2.4", r"For several axes the twiddles depend only on their own axis bits, so a round groups into a parallel butterfly followed by one recordwise monomial $y^{E}$ and is a contraction.",
          r"Consequently the individual axis steps may be grouped as a parallel", [P_MULTID]),
    ],
    frm=[P_SYNTH, P_DFT, P_MULTID, P_NEG], page=P_BFLY,
)

rc3 = S(
    "S6.3",
    r"A layout permutation $L$ puts the selected bits of all axes at a common offset in $K$-bit chunks so that each transform round is one simultaneous layer, and the forward and opposite transforms cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\,\ell\,2^{-p}$.",
    "Move the lowest bit slots to a prefix, exchange $K$-bit chunks so that equal-index chunks of all axes are adjacent, apply one simultaneous layer per remaining round, and track the truncation error",
    M("To apply the simultaneous layer in a transform round, the selected bits of the participating axes must sit at a common offset in consecutive $K$-bit chunks.", "explicit",
      "we must place the selected bits of the participating axes at a common"),
    [
        I("S6.3.1", r"Moving the at most $D(b+1)=O(dK)$ listed bit slots to a prefix costs $O(TpdK)$ and leaves each axis with $q=\lfloor(\ell-1)/K\rfloor$ chunks.",
          r"listed slots, so the moves cost $O(TpdK)$.", [P_STREAM]),
        I("S6.3.2", r"Reordering the chunks uses at most $Dq-1$ exchanges of width-$K$ chunks, each $O(TpK^\tau)$, so with $Dq=O(p/K)$ the total is $O(Tp\,DqK^\tau)=O(Tp\,pK^{\tau-1})$.",
          r"=O\bigl(Tp\,pK^{\tau-1}\bigr).", [P_SWAP]),
        I("S6.3.3", r"Each remaining round is one simultaneous layer, costing $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.",
          r"$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.", [P_SIM]),
        I("S6.3.4", r"At most $b+1\le K$ rounds act on prefix slots, handled individually at cost $O(TpdK)$.",
          r"most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$.", [P_STREAM]),
        I("S6.3.5", r"The monomial $y^E$ with $E=er+s$ is a signed rotation of the coefficient list: split before position $r-s$, put the tail first, negate it and apply the sign $(-1)^e$.",
          r"To implement the monomial, write $E=er+s$ with $0\leq s<r$.", [P_NEG]),
        I("S6.3.6", r"A contraction does not increase the norm of the difference between computed and exact arrays and each round adds one truncation of error below $\sqrt2\,2^{-p}$, so at most $\ell$ rounds give error below $\sqrt2\,\ell\,2^{-p}$ and keep the disk.",
          r"zero error, at most $\ell$ rounds therefore", [NORM, P_DISK]),
        I("S6.3.7", r"Executing the arithmetic on named slots after $L$ conjugates it by $L$, so the full exact operators are $LBF_{\boldsymbol t}^-$ and $F_{\boldsymbol t}^+B^{-1}L^{-1}$, and the forward output order can be kept for the pointwise product.",
          r"(L\mathcal D_-L^{-1})L=LB F_{\boldsymbol t}^-,", [P_BFLY, PERM]),
    ],
    frm=[P_BFLY, P_SYNTH, P_SIM, P_SWAP, P_STREAM, P_MULTID, P_DISK], page=P_LAYOUT,
)

rc4 = S(
    "S6.4",
    r"Two disk-grid ring elements $f,g\in\mathcal R_r$ are multiplied exactly and $Q_p(fg/r)$ is returned in $O(rp\log(rp))$ time by evaluating the integer-coefficient parts at $B_0=2^{4p}$, forming four integer products with the established multiplier, and recovering signed coefficients by centered carries.",
    "Use signed Kronecker substitution: evaluate each coefficient list at $B_0=2^{4p}$, multiply the resulting integers with the $O(N\\log N)$ multiplier, recover coefficients by centered residues, reduce modulo $y^r+1$ and truncate",
    M("A polynomial product becomes an integer product when the base is larger than every product coefficient, so the established fast integer multiplier can be used as an ordinary subroutine.", "recoverable"),
    [
        I("S6.4.1", r"Every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so the centered residue modulo $B_0$ identifies it once the lower coefficients are removed.",
          r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2.", [MOD, POLY]),
        I("S6.4.2", r"Forming $A_u=u(B_0)$ from signed coefficients keeps the carry in $\{-1,0\}$, since $-B_0<u_j+\gamma_j<B_0$, so the blocks are a fixed-width two's-complement encoding with $\gamma_r=-1$ exactly when $A_u<0$.",
          r"Since $-B_0<u_j+\gamma_j<B_0$ whenever", [BIN]),
        I("S6.4.3", r"At block $j$ the unique centered representative of $q_j+\rho_j$ modulo $B_0$ is $h_j$ itself, and the extraction carry $\rho_j$ stays in $\{0,1\}$; the final carry $\rho_J$ cancels the sign extension $\varepsilon$.",
          r"Thus $\widehat h_j=h_j$.", [MOD]),
        I("S6.4.4", r"Reduction modulo $y^r+1$ subtracts the coefficient at $j+r$ from the one at $j$, so each $H_j$ is a sum of exactly $r$ signed products of Gaussian integers of modulus at most $2^p$ and $|H_j|\le r2^{2p}$.",
          r"|H_j|\leq r2^{2p}.", [P_NEG]),
        I("S6.4.5", r"Four exact integer products on $O(rp)$ bits dominate the linear packing, extraction, wrapping and truncation costs, so the cost is $O(rp\log(rp))$.",
          r"Four exact integer products dominate the linear", [P_NLOGN, BO]),
    ],
    frm=[P_NLOGN, P_NEG, MOD, POLY, BIN], page=P_KRON,
)

rc5 = S(
    "S6.6",
    r"The computed convolution has error below $\sqrt2\,M(3\ell+1)2^{-p}$, using $\delta=\sqrt2\,\ell\,2^{-p}$ and $\eta=\sqrt2\,2^{-p}$.",
    "Insert the exact bilinear contraction $P$ at the computed forward outputs, add the two forward errors and the product truncation, pass them through the contraction $\\mathcal T_+$, add the opposite transform error and multiply by $M$",
    M("Each stage is a contraction or a bilinear contraction on disk arrays, so errors add and the chain of estimates can be followed stage by stage.", "recoverable"),
    [
        I("S6.6.1", r"For computed forward outputs $\widetilde u,\widetilde v$ and exact ones $u,v$, $P(\widetilde u,\widetilde v)-P(u,v)=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v)$ has norm below $2\delta$ because $P$ is a bilinear contraction and the operands are in the disk.",
          r"&=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v),\\", [NORM]),
        I("S6.6.2", r"Truncating the product $P(\widetilde u,\widetilde v)$ to the grid gives $\widetilde z$ with $\|\widetilde z-z_*\|_\infty<2\delta+\eta$.",
          r"$\|\widetilde z-z_*\|_\infty<2\delta+\eta$.", [NORM]),
        I("S6.6.3", r"Since $\mathcal T_+$ is a contraction, the opposite transform output $\widetilde h$ satisfies $\|\widetilde h-\mathcal T_+z_*\|_\infty<3\delta+\eta$.",
          r"<3\delta+\eta.", [NORM]),
        I("S6.6.4", r"The final exact multiplication by $M$ gives error below $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$.",
          r"$M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed.", [NORM]),
    ],
    frm=[NORM, P_DISK],
)

s6 = S(
    "S6",
    r"Normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays over $\mathcal R_r$, with $r$ a power of two, $M$ records and $T=rM$, is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.",
    "Apply two forward synthetic transforms keeping their stored frequency order, multiply the entries pointwise exactly by signed packing, apply the opposite transform consuming that same order, scale exactly by $M$, and add the errors",
    M("Pointwise multiplication commutes with applying the same record permutation to both operands, so the forward outputs can be multiplied in their retained order and passed straight to the opposite procedure.", "explicit",
      "forward outputs in their retained order and pass that order directly"),
    [
        rc1, rc2, rc3, rc4,
        I("S6.5", r"The finite sums give $F_{\boldsymbol t}^-(f*g)=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)$ and $F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$, so $MF_{\boldsymbol t}^+\bigl((F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)/r\bigr)=(f*g)/(rM)$.",
          r"=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g).", [P_DFT, P_MULTID]),
        I("S6.5b", r"Because $LB$ permutes records and leaves polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$, so the opposite transform applied to the pointwise product of the stored forward outputs equals $F^+_{\boldsymbol t}P(F^-_{\boldsymbol t}f,F^-_{\boldsymbol t}g)$.",
          r"intact, $P(LBu,LBv)=LBP(u,v)$.", [PERM]),
        rc5,
        I("S6.7", r"There are $M=T/r$ pointwise polynomial products, so their total cost is $O(Tp\log(rp))$ and, with the three transform costs, the stated total.",
          r"is $O(Tp\log(rp))$; the three transform costs are as stated, and", [BO]),
    ],
    frm=[P_SYNTH, P_BFLY, P_LAYOUT, P_KRON, P_NEG, P_DISK, P_DFT, P_MULTID], page=P_RING,
    adds=[
        B("r", "record length", "the number of complex coefficients in a ring element, a power of two", "count"),
        B("M", "record count", "the number of ring elements in the array, $M=T/r$", "count"),
        B("\\ell", "log record length", "$\\ell=\\log_2 r$, also the number of transform rounds", "direct"),
        B("T", "total size", "the number $rM$ of complex coefficients in the padded array", "count"),
    ],
)

# ================================================================= resampling
rd1 = S(
    "S7.1",
    r"There are linear contractions $A$ and $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ and, in tensor form, $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$, whose approximations have error below $dp^2$ and cost $O(dTp^{3/2+\delta}\alpha)$, the permutations $R$ and $Q$ never being executed.",
    "Start from Gaussian resampling $\\mathsf T P_sF_s=P_tF_t\\mathsf S$, invert the near-identity $N=C\\mathsf T\\mathsf D$ by a Neumann series, rescale to contractions, tensor over the axes, and keep the coordinate permutations inside the formula",
    M("The usual implementation sorts twice on each coordinate; retaining both permutations in the transform formula avoids those sorts.", "explicit",
      "We retain both permutations in the transform formula and"),
    [
        I("S7.1.1", r"The exact Gaussian identity gives $\mathsf T P_sF_s=P_tF_t\mathsf S$ for the Gaussian interpolation maps $\mathsf S,\mathsf T$.",
          r"The exact Gaussian identity and inverse estimate proved in", [P_GAUSSRES, GAUSS]),
        I("S7.1.2", r"The near-identity $N=C\mathsf T\mathsf D$ satisfies $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$.",
          r"\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}.", [NORM]),
        I("S7.1.3", r"Since $\alpha^2\theta>p/\alpha^2>1$, one has $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series.",
          r"$\alpha^2\theta>p/\alpha^2>1$.", [GEO, NORM]),
        I("S7.1.4", r"The normalisations of $\mathsf D'$, $\mathsf J'$ and $\mathsf S'$ multiply to $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$, giving $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ with contractions $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$.",
          r"$2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$.", [LOG]),
        I("S7.1.5", r"The selection $C$ of the ordered coordinates $q_j$ is generated with $O(p)$ work per index, so $C$ costs $O(tp)$ with zero numerical error.",
          r"so $C$ takes $O(tp)$ time with zero numerical error.", [MULTI]),
        I("S7.1.6", r"Contraction of the exact maps yields errors below $16p<p^2$ and $4+3p^2/4<p^2$ for $\widetilde A$ and $\widetilde B_0$, each in time $O(tp^{3/2+\delta}\alpha)$.",
          r"Contraction of the exact maps yields errors less than $16p<p^2$ and", [NORM]),
        I("S7.1.7", r"Tensoring the one-dimensional identity over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$.",
          r"Tensoring \eqref{eq:no-sort-one-dimensional} proves", [P_MULTID]),
        I("S7.1.8", r"Composing the $d$ axis maps, each with error below $p^2$, gives error below $dp^2$.",
          r"Composing the $d$ axis maps gives error less than $dp^2$.", [NORM]),
        I("S7.1.9", r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$, so the cost is $\sum_{i=1}^dT/t_i\cdot O(t_ip^{3/2+\delta}\alpha)=O(dTp^{3/2+\delta}\alpha)$.",
          r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$,", [BO]),
        I("S7.1.10", r"Exposing and restoring each of the $d$ axes needs $O(d)$ adjacent interchanges, hence $O(d^2)$ interchanges in all, each costing $O(Tp(1+\ell^\tau))$.",
          r"$O(d)$ adjacent interchanges, hence all axes need $O(d^2)$. These are", [P_SWAP]),
    ],
    frm=[P_GAUSSRES, P_DFT, P_MULTID, P_DISK, P_NLOGN, P_SWAP, P_STREAM, GAUSS, NORM, GEO], page=P_NOSORT,
)

rd2 = S(
    "S7.2",
    r"With $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$, $QF_{\boldsymbol t}u=\overline a\cdot\bigl(a*(\overline a\cdot u)\bigr)/T$, and $RF_{\boldsymbol s}^+\bigl[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)\bigr]=(u*v)/S^2$.",
    "For the first identity expand the coefficient of $u_{\\boldsymbol k}$ and use $-s(j-k)^2+sj^2+sk^2=2sjk$; for the second use $RF^+R=F^+$ so that the permutation $R$ cancels",
    M("The chirp identity performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array, and the retained source permutation cancels when computing a convolution.", "explicit",
      "in $Q$ without applying $Q$ as a separate permutation of the array."),
    [
        I("S7.2.1", r"Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by $-\pi i s_i(2j_i+t_i)$, an integral multiple of $2\pi i$ since $t_i$ is even, so $a$ has period $t_i$.",
          r"$-\pi i s_i(2j_i+t_i)$, an integral multiple of $2\pi i$.", [EUL, MOD]),
        I("S7.2.2", r"The coefficient of $u_{\boldsymbol k}$ on the right side is $\frac1T\exp\bigl(2\pi i\sum_is_ij_ik_i/t_i\bigr)$, which is the coefficient of $QF_{\boldsymbol t}$, because $Q$ reads frequency $(-s_ij_i)_i$ from the negative-sign transform.",
          r"=\frac1T\exp\left(2\pi i\sum_i", [P_DFT, EUL]),
        I("S7.2.3", r"For a unit $c$ modulo $q$, substituting $h=ck$ gives $F_q^+R_c=R_c^{-1}F_q^+$, and since each $t_i$ is a unit modulo $s_i$, tensoring gives $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.",
          r"=(R_c^{-1}F_q^+z)_j.", [P_DFT, PRIME, PERM]),
        I("S7.2.4", r"Therefore $RF_{\boldsymbol s}^+[R(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)]=F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=\frac1SF_{\boldsymbol s}^+F_{\boldsymbol s}(u*v)=(u*v)/S^2$.",
          r"=\frac1S F_{\boldsymbol s}^+F_{\boldsymbol s}(u*v)", [P_DFT, P_MULTID]),
        I("S7.2.5", r"Complex conjugation of the input and output changes the negative Fourier sign to the positive one, commutes with the real permutation $R$ and preserves the disk grid and the norm, so it turns an algorithm for $RF_{\boldsymbol s}$ into one for $RF_{\boldsymbol s}^+$.",
          r"changes the negative Fourier sign to the positive one and commutes with", [CX, NORM]),
    ],
    frm=[P_BLUE, P_NOSORT, P_DFT, P_MULTID, EUL, PRIME, PERM], page=P_CHIRP,
    salient=r"The source permutation $R$ cancels across the two forward transforms, the pointwise product and the opposite transform, so it never has to be executed.",
)

s7 = S(
    "S7",
    r"The source Fourier transform of pairwise coprime prime lengths $\boldsymbol s$ is expressed through power-of-two transforms with the permutations $R$ and $Q$ left inside the transform identities, so that they need not be executed as separate sorts.",
    "Use Gaussian resampling to turn each prime length $s_i$ into a power-of-two length $t_i$ in tensor form, then evaluate the middle transform by a chirp convolution and cancel the source permutation across the convolution",
    M("The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two, and Gaussian resampling connects these two shapes.", "explicit",
      "connects these two shapes."),
    [rd1, rd2],
    frm=[P_GAUSSRES, P_BLUE],
)

# ================================================================= assembly
re1 = S(
    "S8.1",
    r"Choosing $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, a power of two $T\in[4n/b,8n/b)$, record length $r$, power-of-two axis lengths $t_i\in\{r/2,r\}$ and distinct odd primes $s_i$ just below $t_i$ gives $Tp=\Theta(n)$, $T/2<S<T$, and all hypotheses of the interfaces.",
    "Fix rational exponents, derive the sizes from $n$, check the comparison bands for the layer and transform interfaces, and verify by interval estimates for primes that suitable $s_i$ exist with product between $T/2$ and $T$ and large enough ratios $t_i/s_i$",
    M("The prime lengths must be close to the powers of two so that their product occupies a fixed fraction of the padded box, while each ratio $t_i/s_i$ must leave enough separation for resampling.", "explicit",
      "$t_i$: their product must occupy a fixed fraction of the padded box,"),
    [
        I("S8.1.1", r"The fixed rational constants include $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$, chosen with room to spare for the layer conditions.",
          r"C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}.", [RAT, LOG]),
        I("S8.1.2", r"For large $n$ put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $K=\lfloor d^c\rfloor$.",
          r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,", [LOG]),
        I("S8.1.3", r"Take the power of two $T$ in $[4n/b,8n/b)$, let $r=2^{\lceil(\log_2T)/d\rceil}$ and choose $d\ell-\log_2T$ axis lengths $r/2$ and the others $r$, so $t_i\in\{r/2,r\}$ with $\prod_it_i=T$ and the last axis of length $r$.",
          r"Take the power of two $T$ in $[4n/b,8n/b)$, and let", [LOG]),
        I("S8.1.4", r"These definitions give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$.",
          r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad", [BO]),
        I("S8.1.5", r"For large $b$ the bounds $b/2\le\log_2T\le b$ give $\tfrac1{12}p^\epsilon\le d\le p^\epsilon$ and $p/(12d)\le\ell\le p/(3d)$, fixing the comparison constants $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$ and $C_\ell=1$.",
          r"\frac1{12}p^\epsilon\leq d\leq p^\epsilon,", [LOG]),
        I("S8.1.6", r"Set $\alpha=\lceil(12d^2b)^{1/4}\rceil$ and $\gamma=2d\alpha^2$; then $\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}$, so $\gamma=o(b)$ and $2\le\alpha<\sqrt p$.",
          r"\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}.", [LOG]),
        I("S8.1.7", r"For $0<\eta<1/4$ and $x>e^{2/\eta}$ the interval $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes, which exceeds $d$ for $x\in\{r/2,r\}$, so distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ exist with $\eta=1/(4d)$.",
          r"Thus both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$.", [PRIME, LOG]),
        I("S8.1.8", r"Multiplying the lower bounds on $s_i$ and applying the strict Bernoulli inequality gives $S/T>(1-1/(2d))^d>1/2$, and with $s_i<t_i$ this gives $T/2<S<T$.",
          r"Together with $s_i<t_i$, this gives $T/2<S<T$.", [LOG]),
        I("S8.1.9", r"With $\theta_i=t_i/s_i-1\ge\eta/(1-\eta)>\eta$ one has $\alpha^4\theta_i>12d^2b/(4d)=3db\ge6b=p$, the hypothesis of the one-dimensional resampling lemma.",
          r"\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p.", [P_NOSORT]),
        I("S8.1.10", r"The deterministic prime search by trial division takes $n^{o(1)}=o(n)$ time, since its logarithm is $O(\log p+p/d)=o(p)$ and $p=\Theta(\log n)$.",
          r"$n^{o(1)}=o(n)$ time.", [PRIME, BO]),
        I("S8.1.11", r"The two inputs written with $q=\lceil n/b\rceil$ radix-$2^b$ digits have a product of degree at most $2q-2<2n/b\le T/2<S$, so convolution modulo $x^S-1$ has no nonzero wraparound.",
          r"2q-2<2n/b\le T/2<S.", [POLY, CONV]),
        I("S8.1.12", r"Every product coefficient obeys $0\le c_j\le q(2^b-1)^2<2^{3b}$ because $q\le n\le2^b$.",
          r"0\le c_j\le q(2^b-1)^2<2^{3b},", [BIN]),
    ],
    frm=[P_NOSORT, P_LAYOUT, P_RING, P_SIM, P_RADIX, LOG, PRIME, RAT], page=P_PARAM,
    adds=[
        B("b", "digit size", "the radix exponent $\\lceil\\log_2n\\rceil$, so each coefficient holds $b$ bits", "direct"),
        B("p", "precision", "the number $6b$ of fractional bits of the fixed-point numbers", "direct"),
        B("d", "axis count", "the number $\\lfloor b^\\epsilon\\rfloor$ of cyclic axes", "count"),
        B("T", "padded size", "the power of two in $[4n/b,8n/b)$ giving the number of entries of the padded box", "count"),
        B("s_i", "prime length", "the distinct odd prime length of source axis $i$, just below $t_i$", "direct"),
        B("t_i", "power-of-two length", "the power-of-two length of axis $i$, equal to $r/2$ or $r$", "direct"),
        B("\\alpha", "resampling parameter", "the integer $\\lceil(12d^2b)^{1/4}\\rceil$ controlling the Gaussian width", "direct"),
    ],
)

re2 = S(
    "S8.2",
    r"The map $\Phi:\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\ldots,x_d]/(x_i^{s_i}-1)$ with $x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism preserving cyclic convolution, implemented by triangular controlled cyclic shifts in $O(Tp\,d^2(1+\ell^\tau))$ time.",
    "Use the Chinese remainder theorem in the form of Agarwal and Cooley with coordinate powers $\\mu_i=P_i^{-1}\\bmod s_i$, so that each target axis is an earlier-controlled cyclic shift",
    M("The coordinate powers are chosen so that the change of order is a sequence of controlled cyclic shifts.", "explicit",
      "sequence of controlled cyclic shifts."),
    [
        I("S8.2.1", r"The assignment respects $x^S=1$ and so defines an algebra map.",
          r"respects $x^S=1$, so it defines an algebra map.", [ALG]),
        I("S8.2.2", r"The image of $x$ has order $S$ because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all basis monomials once and $\Phi$ is an isomorphism preserving cyclic convolution.",
          r"$\Phi$ is an isomorphism and preserves cyclic convolution.", [PRIME, ALG, CONV]),
        I("S8.2.3", r"For $k=\sum_ja_jP_j$ the coordinate in axis $i$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, since terms with $j>i$ are divisible by $s_i$ and $\mu_iP_i\equiv1\pmod{s_i}$.",
          r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}.", [MOD, PRIME]),
        I("S8.2.4", r"Updating the targets in the order $i=d,d-1,\ldots,1$ uses original digits of lower indices, each update being a prefix-controlled rotation of the valid interval $[0,s_i)$ and the identity elsewhere, so zero padding remains zero.",
          r"order $i=d,d-1,\ldots,1$ using \eqref{eq:triangular-crt}.", [P_CSHIFT]),
        I("S8.2.5", r"The $O(d^2)$ axis moves, each an equal-width chunk swap plus a fixed number of linear passes, make $\Phi$, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$.",
          r"their padding operations cost", [P_SWAP, P_STREAM]),
    ],
    frm=[P_DFT, P_MULTID, P_CSHIFT, P_SWAP, P_STREAM, ALG, PRIME, MOD, CONV], page=P_CRT,
)

re3 = S(
    "S8.3",
    r"The map $\Theta:\mathbb C[x_d]/(x_d^r-1)\to\mathcal R$, $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$, multiplies coefficient $k$ by $\zeta^k$ and is a ring isomorphism turning the negative wrap into the cyclic wrap, so complex cyclic convolution is computed through $\mathcal M_r$.",
    "Twist the last coordinate by $\\zeta^k$ before and untwist by $\\zeta^{-k}$ after the ring convolution, since $\\zeta^r=-1$ turns the negative wrap into the right sign",
    M("The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist.", "explicit",
      "obtained from the synthetic convolution by a coefficient twist."),
    [
        I("S8.3.1", r"The map is well defined since $(\zeta y)^r=(-1)(-1)=1$, and it is diagonal on the bases with nonzero entries $\zeta^k$, hence an isomorphism whose inverse multiplies by $\zeta^{-k}$.",
          r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$.", [P_NEG, ALG, EUL]),
        I("S8.3.2", r"For $k+l=j+hr$ with $h\in\{0,1\}$ a product term acquires the factor $\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
          r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j.", [EUL]),
        I("S8.3.3", r"Hence the normalized complex cyclic convolution is $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$, where $\mathcal M_r$ convolves the first $d-1$ axes over $\mathcal R$.",
          r"Here $\mathcal M_r$ convolves the first $d-1$ axes over $\mathcal R$,", [CONV]),
        I("S8.3.4", r"The computed version forms $f'=Q_p(\widetilde\theta^+\cdot f)$ and $g'=Q_p(\widetilde\theta^+\cdot g)$ with grid approximations of $\zeta^k$ of error below $2\cdot2^{-p}$, applies $\widetilde{\mathcal M}_r$, then untwists, at total cost $O(Tp^{1+\delta})$.",
          r"f'&=Q_p(\widetilde\theta^+\mathbin{\cdot}f),\\", [P_DISK]),
    ],
    frm=[P_NEG, P_DFT, ALG, EUL], page=P_TWIST,
)

re4 = S(
    "S8.4",
    r"The computed source transform $\widetilde{\mathscr F}$ applies the Gaussian map $\mathcal A$, then the chirp transform $\widetilde{\mathscr C}$ evaluated by a twisted ring convolution, then $\mathcal B_0$ and an exact power-of-two scale $2^\gamma$, and has exact counterpart $RF_{\boldsymbol s}$.",
    "Evaluate the middle factor $QF_{\\boldsymbol t}$ by the chirp identity as two phase multiplications around the complex convolution, then compose with the Gaussian maps and the exact scale",
    M("The complex convolution evaluates the middle factor of the resampling identity, which is then composed with the Gaussian maps.", "explicit",
      "We next use the complex convolution to evaluate the middle factor"),
    [
        I("S8.4.1", r"The chirp phase numerator at tensor address $j$ is computed modulo $2r$ as $-\sum_is_ij_i^2(r/t_i)$, with all integers of $O(p)$ bits and multiplications by the established multiplier, so the chirp construction costs $O(Tdp^{1+\delta})$.",
          r"-\sum_i s_i j_i^2(r/t_i)\pmod{2r}.", [P_NLOGN]),
        I("S8.4.2", r"The computed chirp transform forms $x_0=Q_p(\overline{\widetilde a}\cdot x)$, then $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$, then $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$.",
          r"x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),\\", [P_TWIST]),
        I("S8.4.3", r"Replacing the approximations by exact phases and the exact convolution gives $\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)=QF_{\boldsymbol t}x$ by the chirp identity.",
          r"(a,\overline a\mathbin{\cdot}x)=QF_{\boldsymbol t}x$ by", [P_CHIRP]),
        I("S8.4.4", r"The source transform has exact counterpart $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, with the source arrays stored in the padded power-of-two box with zeros outside the valid coordinates.",
          r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A", [P_NOSORT]),
        I("S8.4.5", r"The opposite-sign procedure is $\widetilde{\mathscr F}^{+}(z)=\overline{\widetilde{\mathscr F}(\overline z)}$, with exact counterpart $RF_{\boldsymbol s}^{+}$ by the conjugation remark of the chirp lemma.",
          r"=\overline{\widetilde{\mathscr F}(\overline z)};", [P_CHIRP]),
    ],
    frm=[P_NOSORT, P_CHIRP, P_RING, P_TWIST, P_BLUE, P_GAUSSRES, P_PARAM, P_DISK, P_LAYOUT], page=P_SRC,
)

# multiplication algorithm with exact recovery
re6 = S(
    "S8.5.9",
    r"The recovered coefficient error is below $1/2$, so rounding gives the exact convolution coefficients, and radix-$2^b$ carry propagation yields the exact $2n$-bit product.",
    "Track the errors of the computed transforms by inserting exact contractions at computed inputs, chain them to the error of $w$, remove the scalings $S$ and $2^{2b+4}$ and compare with $1/2$, then verify the carry recurrence",
    M("The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$; it also justifies the rounding, carries, and output length.", "explicit",
      "disk bounds needed by every call and proves that the final error is"),
    [
        I("S8.5.9.2", r"The error of the returned normalized ring convolution is $E_{\rm ring}:=M(3L+2)<5TL$ (in units of $h_p=2^{-p}$), the three transform errors and the polynomial-product truncation totalling less than $3L+2$.",
          r"E_{\rm ring}:=M(3L+2)<5TL.", [P_RING]),
        I("S8.5.9.1", r"With a norm at most $.7$ on one operand and $\mathcal M_r$ a bilinear contraction, the computed grid output has norm less than $.7+5TLh_p<.701$, so no clipping is needed and the output is a legal disk-grid input.",
          r"has norm less than $.7+5TLh_p<.701$ for large $n$.", [NORM, P_DISK]),
        I("S8.5.9.3", r"Inserting the exact $\mathcal M_r$ propagates the two twist errors below $4$ each, adds $E_{\rm ring}$ and an output untwist error below $4$, so $\|\widetilde{\mathcal M}_{\mathbb C}(f,g)-\mathcal M_{\mathbb C}(f,g)\|<6TLh_p$.",
          r"<(E_{\rm ring}+4+4+4)h_p<6TLh_p.", [P_TWIST, NORM]),
        I("S8.5.9.4", r"The chirp transform adds the kernel error $2$, the endpoint phase errors $4$ and $4$, and the convolution error $6TL$, giving $\|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\|<8TLh_p$.",
          r"<(6TL+2+4+4)h_p<8TLh_p.", [P_CHIRP]),
        I("S8.5.9.5", r"The expansion maps contribute error below $dp^2$ each, the chirp below $8TL$, so the source transform has error below $E_sh_p$ with $E_s=9\,2^\gamma TL$, because $2dp^2<TL$ eventually.",
          r"E_s=9\,2^\gamma TL,", [P_NOSORT]),
        I("S8.5.9.6", r"The pointwise product $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has norm at most $.26^2<.5$ and error $\|z-U\cdot V_1\|<(2E_s+2)h_p$, since the two terms of the difference have norm below $2E_sh_p$ and truncation adds below $2h_p$.",
          r"Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$.", [NORM]),
        I("S8.5.9.7", r"The opposite transform satisfies $\|\widetilde{\mathscr F}^{+}(z)-G(U\cdot V_1)\|<(3E_s+2)h_p$ with $G=RF_{\boldsymbol s}^+$ and $G(U\cdot V_1)=(u*v)/S^2$ by the permutation cancellation.",
          r"&<(3E_s+2)h_p.", [P_CHIRP]),
        I("S8.5.9.8", r"The first scaling by $S$ gives $\widetilde w$ approximating $w=(u*v)/S$ with error below $E_wh_p$, where $E_w:=S(3E_s+2)<28\,2^\gamma T^2L$.",
          r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L.", [NORM]),
        I("S8.5.9.9", r"The unscaled integer coefficient array is $2^{2b+4}Sw$, so with $S\le T<2^b$ and $L<b$ the final error is below $2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b}<448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<1/2$, using $\gamma\le b/4$.",
          r"<448b\,2^{-b+\gamma}", [LOG]),
        I("S8.5.9.10", r"Since the true coefficients are integers and the error is strictly below $1/2$, the nearest integer to the represented value is the unique correct coefficient, and it lies in $[0,2^{3b})$.",
          r"that value the unique correct coefficient.", [RAT]),
        I("S8.5.9.11", r"The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$ with $Q_0=2^b$, because $c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1)$, and the invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ fixes the first $j$ radix digits of the product.",
          r"c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1),", [BIN, PROOF]),
    ],
    frm=[P_SRC, P_PARAM, P_RING, P_CHIRP, NORM, P_DISK], page=P_EXACT,
    salient=r"The final error is below $1/2$ despite being multiplied by $2^{2b+4}S$, because the working precision $p=6b$ beats the loss $2^{\gamma}$ and the scalings by a factor $2^{-b/4}$ per bit.",
)

re5 = S(
    "S8.5",
    r"The algorithm splits the inputs into radix-$2^b$ digits, maps them by $\Phi$ to prime axes, takes two source transforms, multiplies pointwise, applies the opposite-sign transform with the two scalings by $S$, rounds, undoes $\Phi$ and propagates carries to output the $2n$-bit product.",
    "Compose the established procedures in the order digits, address map, two source transforms, pointwise product, opposite transform, scaling and rounding, inverse address map, carries, and then verify exactness",
    M("The source-transform procedures supply the three transforms needed for the radix-digit convolution.", "explicit",
      "The source-transform procedures now supply the three transforms needed"),
    [
        I("S8.5.1", r"Each radix-$2^b$ digit $a_j$ is written as the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word followed by a zero imaginary word, so its represented value is exactly $a_j2^{-b-2}$, and $S-q$ zero records are appended.",
          r"$a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero", [BIN, P_DISK]),
        I("S8.5.2", r"Apply the coefficient-address map $\Phi$ with its padded layout to obtain source arrays $u,v$ with coefficients of norm less than $1/4$.",
          r"Apply the coefficient-address map $\Phi$, with its padded layout, to obtain", [P_CRT]),
        I("S8.5.3", r"Compute the source transforms $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.",
          r"Compute $\widetilde{\mathscr F}(u)$ and", [P_SRC]),
        I("S8.5.4", r"Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, obtaining the array $z$.",
          r"Multiply corresponding complex coefficients exactly and truncate", [P_DISK]),
        I("S8.5.5", r"Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, obtaining $\widetilde w$.",
          r"Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid", [P_SRC]),
        I("S8.5.6", r"Multiply the numerators of $\widetilde w$ exactly by $2^{2b+4}S$, round the real values to the nearest integers, write them in signed $(3b+1)$-bit words with zero words at padded addresses, and apply $\Phi^{-1}$.",
          r"Multiply the grid numerators of $\widetilde w$ exactly by", [P_CRT]),
        I("S8.5.7", r"Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits most significant first.",
          r"Propagate radix-$2^b$ carries in increasing coefficient order.", [BIN]),
        I("S8.5.8", r"The two occurrences of $S$ undo different normalisations: after the three transforms the exact counterpart is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$, and the second scale with $2^{2b+4}$ gives the original integer coefficient convolution.",
          r"first scale it is $w=(u*v)/S$.", [P_CHIRP, P_CRT]),
        re6,
    ],
    frm=[P_SRC, P_EXACT, P_CRT, P_PARAM, P_RADIX, P_DISK], page=P_ALG,
)

re7 = S(
    "S8.6",
    r"Every row of the cost table, divided by $Tp$, is at most $p^{1-2\kappa}$ because the seven dominant margins $g_i$ are at least $2^{-181}=2\kappa$, so the total cost is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
    "Tabulate the cost of each operation divided by $Tp$, express each as a power of $p$, and compare the exponents of the seven dominant rows with one using the explicit margins",
    M("The explicit slack in the margins will cover any remaining fixed power of $\\log p$.", "explicit",
      "any remaining fixed power of $\\log p$."),
    [
        I("S8.6.1", r"The table lists each operation with normalised cost and power of $p$: prefix-slot moves and individual rounds $dK$, chunk exchanges $pK^{\tau-1}$, simultaneous rounds $\ell d^{\lambda'}$, CRT and axis layouts $d^2(1+\ell^\tau)$, Gaussian line maps $dp^{1/2+\delta}\alpha$, chirps and twists $dp^\delta$, packed products $\log(rp)$.",
          r"Operation & Normalized cost & Power of $p$\\", [BO]),
        I("S8.6.2", r"Direct substitution of the fixed exponents gives $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$ and $g_7=2^{-75}$, where $g_2=\epsilon c(1-\tau)$ comes from the chunk-exchange row.",
          r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad", [RAT, LOG]),
        I("S8.6.3", r"Thus $\min_ig_i=2^{-181}=2\kappa$.",
          r"Thus $\min_i g_i=2^{-181}=2\kappa$.", [LOG],
          salient=r"$\kappa=2^{-182}$ is exactly half the smallest margin $2^{-181}=\epsilon c(1-\tau)$, set by the chunk-exchange row $pK^{\tau-1}$."),
        I("S8.6.4", r"Prefix-slot moves cost $O(dK)$ linear scans and the positional layout uses $O(p/K)$ exchanges of width-$K$ chunks, each $O(VK^\tau)$, so the normalised total is $O(p/K)K^\tau=O(pK^{\tau-1})$.",
          r"O(p/K)\,K^\tau=O(pK^{\tau-1}).", [P_LAYOUT, P_SWAP]),
        I("S8.6.5", r"The at most $\ell$ simultaneous rounds cost $O(Vd^{\lambda'})$ each, including basis changes, deterministic repair, row padding and base-$m$ groups.",
          r"Proposition~\ref{prop:simultaneous-layer} supplies $O(Vd^{\lambda'})$", [P_SIM]),
        I("S8.6.6", r"Axis exposure and restoration need $O(d^2)$ adjacent moves, each $O(V(1+\ell^\tau))$ by peeling an excess bit, exchanging the equal-width parts and restoring the bit; the $d$ CRT rotations cost $O(dV)$.",
          r"Each costs $O(V(1+\ell^\tau))$: peel a single excess bit when widths", [P_SWAP, P_CRT]),
        I("S8.6.7", r"For Gaussian resampling, the factor $\alpha=\Theta(p^{1/4+\epsilon/2})$ explains the displayed power $3/4+\delta+3\epsilon/2$ of $p$.",
          r"$\alpha=\Theta(p^{1/4+\epsilon/2})$ explains its displayed power of $p$.", [P_NOSORT]),
        I("S8.6.8", r"Chirp numerators computed with the established multiplier and the exponentials cost $O(dp^{1+\delta})$ per entry.",
          r"then generating the exponentials, costs $O(dp^{1+\delta})$ per entry.", [P_NLOGN, P_SRC]),
        I("S8.6.9", r"Four integer products on $O(rp)$ bits for each of the $T/r$ polynomial records cost $O(Tp\log(rp))$ in total, and these use the previously established multiplier, not the improved algorithm.",
          r"$O(Tp\log(rp))$ in total.", [P_KRON, P_NLOGN]),
        I("S8.6.10", r"Setup at visits of the layer and address recursions costs at most $p^{A+C}=o(Tp)$, since there are at most $p^A$ visits and $r$ exceeds every fixed power of $p$.",
          r"costs at most $p^{A+C}=o(Tp)$.", [BO]),
        I("S8.6.11", r"The compact sorting of exceptional records costs $O(Vp^{A'}2^{-K})=o(V)$, a deterministic worst-case bound.",
          r"=O(Vp^{A'}2^{-K})=o(V)", [P_PACKED]),
        I("S8.6.12", r"Each of the seven displayed powers is at most $1-2\kappa$ and any fixed power of $\log p$ is at most $p^\kappa$ eventually.",
          r"Each of the seven displayed powers is at most $1-2\kappa$ by", [LOG]),
        I("S8.6.13", r"The complete large-input bound is therefore $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
          r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}).", [BO]),
    ],
    frm=[P_PARAM, P_LAYOUT, P_SIM, P_SWAP, P_RING, P_NOSORT, P_CRT, P_TWIST, P_SRC, P_EXACT, P_NLOGN, P_KRON, P_PACKED],
    page=P_COST,
    salient=r"$\kappa=2^{-182}$ is half of the smallest of the seven margins, $2^{-181}=\epsilon c(1-\tau)$, so the astronomically small saving is fixed by the chunk-exchange row $pK^{\tau-1}$.",
    adds=[
        B("g_i", "margin", "the gap between $1$ and the exponent of $p$ in the $i$th dominant row of the cost table", "direct"),
    ],
)

s8 = S(
    "S8",
    r"The exact integer product is obtained by choosing compatible parameters, mapping the digit convolution to prime axes and a source transform, recovering exact coefficients, and accounting for every tape operation.",
    "Fix the sizes and precision, place the radix-digit coefficient list on prime axes by the CRT map, build the source transform and the twisted ring convolution, run the multiplication algorithm, prove exactness and add the costs",
    M("The procedures must be given compatible parameters, the integer coefficients recovered from their approximations, and the remaining tape operations accounted for.", "explicit",
      "We choose compatible parameters for these procedures, recover"),
    [re1, re2, re3, re4, re5, re7],
    frm=[P_NOSORT, P_RING, P_LAYOUT, P_SIM],
)

end = I(
    "S9",
    r"Below a fixed cutoff schoolbook multiplication is used, so the finitely many smaller lengths are absorbed in the implicit constant, and one fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and outputs the exact $2n$-bit product.",
    r"Fix one cutoff beyond all the size, precision, margin and layout",
    [SCHOOL, ASYM],
)

root = S(
    "S0",
    r"A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$.",
    "Reduce the product to a convolution of short digits, compute it through multidimensional transforms whose address rearrangements and butterfly layers are accelerated by two power-saving tape procedures, recover the integer product exactly, and total the costs",
    M("Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both movement and arithmetic must be sped up.", "explicit",
      "We therefore need savings in both movement and arithmetic."),
    [
        I("S1", r"Writing each $n$-bit integer as a polynomial in $2^b$ reduces the product to the convolution of the two digit lists, followed by carry propagation.",
          r"Splitting the inputs into radix digits reduces multiplication to", [POLY, CONV, BIN, SCHOOL], page=P_RADIX),
        I("S2", r"The model is one fixed finite alphabet and one fixed finite number of one-dimensional tapes; a step reads and writes at most one cell per tape and moves each head by at most one cell, and cost is the number of steps.",
          r"one-dimensional tapes. A step reads and writes at most one cell on each", [TM, MULTI], page=P_TAPE),
        I("S3", r"Arrays with a product address set are stored in lexicographic order with implicit addresses, and fixed permutations of two digits, digit moves, pointwise maps on split streams and cyclic row splits into $W$ streams each cost $O(V)$ steps for $V$ stored bits.",
          r"volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:", [P_TAPE, LEX, PERM, MULTI], page=P_STREAM),
        I("S4", r"Adding an offset computed from earlier control fields to a later field modulo $q^b$, or multiplying it by a fixed unit, costs $O(V)$ by splitting each fiber into blocks and re-merging them in another order.",
          r"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the", [P_STREAM, P_TAPE, MOD, PRIME], page=P_CSHIFT),
        key,
        s6,
        s7,
        s8,
        end,
    ],
    frm=[P_CONJ, P_NLOGN, BO, TM, ASYM],
    page=P_MAIN,
)


def walk(n, out):
    out.append(n)
    for c in n.get("children", []) or []:
        walk(c, out)


if __name__ == "__main__":
    json.dump({"root": root}, open(sys.argv[1], "w"), indent=1)
    print("ok")
