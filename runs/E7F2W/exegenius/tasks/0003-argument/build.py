import json, re, sys
ROOT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F2W"
SRC = open(ROOT + "/sources/paper.tex", encoding="utf-8").read()
LINES = SRC.split("\n")

def ql(n, sub=None):
    t = LINES[n - 1].strip()
    if sub is not None:
        assert sub in t, (n, sub, t)
        t = sub
    return {"source": "paper", "quote": t, "_line": n}

def qt(text):
    assert text in SRC, text
    idx = SRC.index(text)
    line = SRC[:idx].count("\n") + 1
    return {"source": "paper", "quote": text, "_line": line}

def mot(text, source, quote=None):
    d = {"text": text, "source": source}
    d["quote"] = None if quote is None else {"source": quote["source"], "quote": quote["quote"]}
    return d

def inf(id, claim, quote, page=None, frm=None, salient=None, deferred=False):
    d = {"id": id, "intention": "infer", "claim": claim, "quote": quote, "children": [], "from": frm or []}
    if page: d["page"] = page
    if salient: d["salient"] = salient
    if deferred: d["deferred"] = True
    return d

def show(id, claim, method, motivation, children, page=None, frm=None, adds=None, salient=None):
    d = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": motivation,
         "children": children, "from": frm or []}
    if page: d["page"] = page
    if adds: d["adds"] = adds
    if salient: d["salient"] = salient
    return d

def add(symbol, name, meaning, relation):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

# ---------------------------------------------------------------- key step
K1a = show("K1.a",
    "A forward invocation of the three-element-subset gadget changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged, whatever the initial scratch values.",
    "Write the net change of the target as a sum of a side-injection part and a gather/scatter part computed through eight scratch-restoring rows, then compute the coefficient from $x_T$ to $y_S$ from the intersection size $|S\\cap T|$.",
    mot("Gather and scatter alone create a coefficient that depends on the intersection size; side wires are added only to cancel the unwanted coefficients.", "explicit",
        qt("on intersection size, and auxiliary wires cancel the unwanted")),
    [
     inf("K1.a.1", "Rows 0 and 1 remove the old scratch contribution, rows 2 to 5 add the source's effect, and rows 6 and 7 restore the scratch values, so the net target change is $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$, independent of the initial scratch vectors $a,c$.",
         ql(749), salient=None, frm=["bitwise-xor"]),
     inf("K1.a.2", "Over $\\mathbb F_2$ the central coefficient from $x_T$ to $y_S$ is $|S\\cap T|\\bmod 2$; the side injection cancels exactly the intersection-one cases, while distinct triples with intersection zero or two already have coefficient zero and the self coefficient is one.",
         ql(753), frm=["bitwise-xor","modular-arithmetic-and-residues"]),
     inf("K1.a.3", "In the complex construction the central coefficient is $(|S\\cap T|-1)/2$; the side wires cancel it for intersection zero or two, intersection one already contributes zero, and the self coefficient is one, so both gadgets act as $y\\gets y+x$.",
         ql(756), frm=["rational-numbers-dyadic-rationals-and-exact-arithmetic"]),
    ],
    page="triple-gadget",
    frm=["quantifiers-sets-and-basic-asymptotic-notation-beyond-big-o","bitwise-xor","discrete-math-proof-techniques","rational-numbers-dyadic-rationals-and-exact-arithmetic"],
    salient="The coefficient of the gadget depends only on the size of the intersection $|S\\cap T|$ of two three-element subsets, and a single family of side wires turns that intersection-dependent coefficient into the identity map $y_S\\gets y_S+x_S$.")

K1 = show("K1",
    "A fixed network of linear gates, in three stages, sends $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ on two banks and restores every auxiliary scratch value, whatever its initial content.",
    "Compose three gadget invocations: a forward one from $X$ to $Y$, the inverse schedule from $Y$ to $X$, and a forward one from $X$ to $Y$.",
    mot("Three shears $y\\gets y+x$, $x\\gets x-y$, $y\\gets y+x$ compose to an exchange with one sign, and each shear is exactly what the gadget supplies; this is the same pattern as the three updates of the final chunk interchange.", "recoverable"),
    [
     K1a,
     inf("K1.b", "Starting from $(x,y)$ the three stages give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$, and each invocation restores its own auxiliary wires, so every auxiliary value returns unchanged.",
         ql(762)),
    ],
    page="bank-exchange-network",
    frm=["triple-gadget","matrices-invertibility-and-rank"],
    salient="The exchange needs three stages because each gadget only adds one bank to the other; the exchange comes out signed ($X\\mapsto -Y$) and every scratch wire, with arbitrary initial value, is restored.")

K2 = show("K2",
    "If every gate acts pointwise and linearly on address-indexed arrays and every incidence of a gate uses one invertible frame $D_v$, then the whole network implements $D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}$, so only the edge changes $D_vD_u^{-1}$ cost anything.",
    "Show by induction along each wire that the stored array always equals the frame applied to the logical array, using that a common frame commutes with a pointwise linear gate.",
    mot("Once the scalar routing is fixed, only the endpoint frames matter, so the intermediate frames can be picked freely to make each edge change cheap.", "explicit",
        qt("intermediate frames can then be chosen to make each edge change inexpensive.")),
    [
     inf("K2.a", "At every vertex the stored array equals $D_v$ applied to the logical array; this holds at the sources by definition and an edge from $u$ to $v$ changes $D_u\\varphi$ to $D_v\\varphi$ by $D_vD_u^{-1}$.",
         ql(806)),
     inf("K2.b", "At a gate, $R$-linearity gives $\\sum_j c_jD_v\\varphi_j=D_v(\\sum_j c_j\\varphi_j)$, so the common frame commutes with the pointwise gate and the invariant continues to the sinks.",
         ql(812), frm=["matrices-invertibility-and-rank"]),
     inf("K2.c", "For a signed role permutation the route from input role $w$ applies $\\varepsilon_w D_{{\\rm sink}(\\rho(w))}D_{{\\rm source}(w)}^{-1}$, on auxiliary roles too, so the endpoint frames alone determine the array operator on each route.",
         ql(823), frm=["permutations-and-permutation-matrices"]),
    ],
    page="frames",
    frm=["bank-exchange-network","matrices-invertibility-and-rank","permutations-and-permutation-matrices"],
    salient="The intermediate frames cancel completely: the result depends only on the source and sink frames, so the interior frames can be chosen to make every edge a cheap smaller operation.")

K3A = show("K3.A",
    "With nested nondegenerate labels the sum of absolute dimension changes over all edges is $Wm-2N+2L$, where $L$ is the dimension lost on decreasing edges, and $L<N/2$.",
    "Telescope the signed dimension changes at each gate, then locate the few decreasing edges and total their loss.",
    mot("Every gate sees the same label on its incoming and outgoing incidences, so signed changes cancel at gates and only the terminals contribute.", "recoverable"),
    [
     inf("K3.A.1", "The source dimensions sum to $N$ and the sink dimensions to $Wm-N$, so the signed dimension changes sum to $Wm-2N$ and the sum of absolute changes is $Wm-2N+2L$.",
         ql(891)),
     inf("K3.A.2", "Every edge joins comparable nondegenerate labels, and the only decreasing edges are the $Ic$ central-wire edges from time 3 to time 4, each losing dimension $h$, so $L=Ich$.",
         ql(998)),
     inf("K3.A.3", "The loss ratios are $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$, both smaller than $1/2$, which leaves a strict saving.",
         ql(1107)),
    ])

K3B = show("K3.B",
    "For the bit network the sum of rational ranks of all edge differences is $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$.",
    "Replace each dimension change by the rank of the difference of two projection matrices; this equals the dimension change on every edge except the source edges of the $X_a$ roles.",
    mot("The tape operation on an edge costs one smaller interchange per unit of rational rank, so ranks, not dimensions, must be summed.", "recoverable"),
    [
     inf("K3.B.1", "The total of edge ranks has the form $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}$: the dimension-change total $W_{\\rm b}m-2N+2L_{\\rm b}$ plus $N$ extra source ranks.",
         ql(1151)),
     inf("K3.B.2", "For nondegenerate $U\\subset V$ the difference $P_V-P_U$ is the identity on $V\\cap U^\\perp$ and zero on its orthogonal complement, so its rank is $\\dim V-\\dim U$, and reversing the edge negates the matrix without changing rank.",
         ql(1160), frm=["bilinear-orthogonal"]),
     inf("K3.B.3", "The only exceptions are the $N$ negative source projections $-P_{U_a}$: at stage 1 the first gate on $X_a$ has label exactly $U_a$, so that first edge matrix is $2P_{U_a}$ of rank one although its dimension change is zero.",
         ql(1162)),
     inf("K3.B.4", "The deficit of the rank total from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$ because $L_{\\rm b}<N/2$, hence $s_{\\rm b}<W_{\\rm b}m$.",
         ql(1167)),
    ])

K3 = show("K3",
    "Attaching nested nondegenerate subspaces of an $m$-dimensional space to gates and terminals makes each edge's frame change cost its rank, and the total number $s$ of smaller calls satisfies $s<Wm$, indeed $s/W<m^{\\tau}$ with $\\tau=1-2^{-50}$.",
    "Count edge dimension changes by telescoping, convert them to matrix ranks (with the exceptional source edges), and compare the relative deficit with $20\\cdot 2^{-50}$.",
    mot("The saving will come from keeping the total dimension lost on decreasing edges small relative to $N$.", "explicit",
        qt("The saving will come from keeping the total dimension lost on decreasing")),
    [
     K3A, K3B,
     inf("K3.C", "Since the relative deficit exceeds $20\\cdot 2^{-50}$ and $\\log m<20$, $m^{1-2^{-50}}>m(1-20\\cdot2^{-50})>m(1-\\eta)$, so $s/W<m^{\\tau}$ for $\\tau=1-2^{-50}$.",
         ql(1336), salient="The saving is astronomically thin (relative rank deficit about $1.5\\times10^{-11}$) yet strict, and a strict gap is all the recursion needs to lose a power of the chunk width.",
         frm=["logarithms-floors-ceilings-and-powers-of-two"]),
    ],
    page="subspace-labels",
    frm=["bilinear-orthogonal","frames","bank-exchange-network","triple-gadget","vector-spaces-basis-and-dimension","matrices-invertibility-and-rank","logarithms-floors-ceilings-and-powers-of-two"])

K4 = inf("K4",
    "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation matrix with exactly $a$ ones.",
    ql(1366), page="triangular-factorization",
    frm=["matrices-invertibility-and-rank","permutations-and-permutation-matrices","rational-numbers-dyadic-rationals-and-exact-arithmetic"])

K5 = show("K5",
    "The address update $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b$ is performed with exactly ${\\rm rank}(A)$ interchanges of pairs of $b$-digit fields plus $O(V)$ further work.",
    "Factor $A=E_1\\Pi E_2$, perform the triangular changes of coordinates by controlled shifts in linear time, and turn each one of $\\Pi$ into a three-update shear containing a single interchange.",
    mot("Lower triangular changes of coordinates update a later field from earlier ones, which is exactly the direction in which controlled shifts run in linear time.", "explicit",
        qt("Lower triangular changes of coordinates")),
    [
     inf("K5.a", "A lower triangular transformation of $H$ or of $D$ costs $O(V)$: update coordinates in descending physical order, multiplying by a diagonal unit and adding a fixed combination of earlier coordinates.",
         ql(1425), frm=["controlled-shifts"]),
     inf("K5.b", "For $A=E_1\\Pi E_2$, transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$.",
         ql(1432)),
     inf("K5.c", "Each one of $\\Pi$ calls for $H_i\\leftarrow H_i+D_j$, done by $D_j\\leftarrow D_j+H_i$, an interchange of $H_i,D_j$, then $D_j\\leftarrow H_i-D_j$; the two outer updates are linear-cost, and since $\\Pi$ has exactly $a$ ones there are exactly $a$ interchanges.",
         ql(1443)),
    ],
    page="matrix-shear",
    frm=["triangular-factorization","controlled-shifts","stream-arrays","modular-arithmetic-and-residues","primes-divisibility-gcd-and-coprimality"])

K10 = show("K10",
    "Solving the recurrence $F_0=O(1)$, $F_k\\le(s/W)F_{k-1}+O(1)$ with $s/W<m^\\tau$ gives $F_k=O(e^{\\tau})$ for $e=m^k$.",
    "Unroll the recurrence into the geometric sum $\\sum_{j\\le k}(s/W)^j$ and bound it separately when the ratio $a=s/W$ is at most one and when it exceeds one.",
    mot("Dividing a call's cost by its volume leaves the factor $s/W$ per level, and the number of levels is $k=\\log_m e$.", "recoverable"),
    [
     inf("K10.a", "Per unit volume the cost satisfies $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$, because each of the $s$ child calls runs on a stream of volume $V/W$ and the remaining node work is $O(V)$.",
         ql(1552)),
     inf("K10.b", "For $a=s/W<m^\\tau$ the geometric sum $\\sum_{j=0}^k a^j$ is $O(m^{k\\tau})$.",
         ql(1554)),
     inf("K10.c", "The two cases of the sum: if $a\\le1$ the sum is at most $k+1=O(m^{k\\tau})$, and if $a>1$ it is $O(a^k)=O(m^{k\\tau})$ because $a<m^{\\tau}$.",
         ql(1556)),
     inf("K10.d", "Hence $F_k=O(e^{\\tau})$, since $m^{k\\tau}\\le (me)^{\\tau}$.",
         ql(1557)),
    ],
    salient="Cost per unit volume grows only like $e^{\\tau}$ with $\\tau<1$, not like $e$ or $\\log e$: each level multiplies the work by $s/W$, which is strictly less than the factor $m$ by which the chunk width grows.")

KS = show("KS",
    "Two disjoint chunks of $e=m^k$ radix-$q$ digits each can be interchanged, preserving every other address field, in $O(Ve^{\\tau})$ time for a fixed rational $\\tau<1$.",
    "Run the bank-exchange network on $W$ role streams of volume $V/W$, putting each edge's frame change into the smaller interchanges given by the rank of its matrix; the recursion then costs $s/W<m^{\\tau}$ per level in volume-normalized terms.",
    mot("A recursive call at parameter $mf$ uses $s$ calls at parameter $f$ on streams of volume $V/W$, so multiplying the parameter by $m$ multiplies the normalized cost by $s/W<m$; this strict inequality is the source of the power saving.", "explicit",
        qt("is the source of the power saving.")),
    [
     K1, K2, K3, K4, K5,
     inf("KS.base", "For $k=0$ the interchange of single digits is the elementary stream operation, costing $O(V)$.",
         ql(1492), frm=["stream-arrays"]),
     inf("KS.split", "Split whole rows cyclically into $W$ role streams within each prefix; each stream has the same remaining address shape and volume exactly $V/W$.",
         ql(1497), frm=["stream-arrays"]),
     inf("KS.frame", "Take the frame at a vertex with matrix $M$ to be the address shear $\\Phi_M:(H,D)\\mapsto(H+MD,D)$; the endpoint condition $M_{{\\rm out}(\\rho(w))}-M_{{\\rm in}(w)}=I_m$ then gives $H\\gets H+D$ on every row, scratch rows included.",
         ql(1529), frm=["frames"]),
     inf("KS.swap", "The chunk interchange is $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$ componentwise; only the middle shear uses the circuit and the other two updates are linear-cost.",
         ql(1535), frm=["controlled-shifts"]),
     inf("KS.count", "The number of recursive calls is the sum of the edge ranks, exactly $s$, each acting on one role stream of volume $V/W$.",
         ql(1543)),
     K10,
     inf("KS.sched", "On a fixed number of tapes the $s$ child calls are scheduled depth first by parking the $W-1$ inactive role streams on a stack, which costs $O(V)$ at the parent node and so does not change the factor $s/W$.",
         ql(1584), frm=["multitape-machine-cost-model-and-linear-time-scans"]),
     inf("KS.desc", "Descriptor work at depth $j$ is polynomial in $\\log V_0=O(\\log (2V_j))$ because both original chunk ranges remain present in every child, so it is $O(V_j)$.",
         ql(1602)),
    ],
    page="power-width-interchange",
    frm=["stream-arrays","controlled-shifts","bank-exchange-network","triple-gadget","frames","subspace-labels","triangular-factorization","matrix-shear","geometric-series-and-orthogonality-of-sums-of-roots-of-unity","logarithms-floors-ceilings-and-powers-of-two","big-o"],
    adds=[add("m","digit-field count","The dimension $m=h^3=10^6$ of the label space, which is also the number of digit fields into which a chunk is split in one recursion step.","count"),
          add("W","wire count","The number of wires of the bit network, each of which receives one role stream of volume $V/W$.","count"),
          add("s","smaller-call count","The sum of the ranks of all edge differences, i.e. the number of smaller interchanges one run of the network needs.","count"),
          add("\\tau","chunk-swap exponent","A fixed rational exponent below one with $s/W<m^{\\tau}$, namely $\\tau=1-2^{-50}$.","direct")],
    salient="The cost per volume is a fixed power $e^{\\tau}$ of the chunk width with $\\tau<1$, although the recursion has $s$ children per level and $s$ is almost $Wm$: the whole saving comes from the strict inequality $s<Wm$ on the total rank.")

S2 = show("S2",
    "Two disjoint address chunks of $u$ bits in any bit array can be interchanged in $O(Vu^{\\tau})$ steps for a fixed $\\tau<1$, with intermediate XOR combinations but an exact final permutation.",
    "Prove the fast interchange first for power widths $e=m^k$ with enough rows, then reach arbitrary widths by padding the row count, splitting the width in base $m$ and padding the binary range up to a power of the radix.",
    mot("Because the sum of the edge ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width.", "explicit",
        qt("$m$, the resulting recurrence saves a power of the chunk width.")),
    [
     inf("S2.1", "Arrays with a product address set are stored in lexicographic order with addresses implicit in position, and any fixed permutation of digit values, digit move, pointwise map on aligned streams, and cyclic row split into a fixed number of streams costs $O(V)$ for $V$ stored bits.",
         ql(494), page="stream-arrays",
         frm=["fixed-tape-model","lexicographic-order-and-index-tuples","multitape-machine-cost-model-and-linear-time-scans","permutations-and-permutation-matrices"]),
     inf("S2.2", "Adding an offset computed from earlier control fields to a later target field modulo $q^b$, or multiplying it by a fixed unit, costs $O(V)$ by splitting each fibre into two pieces and merging them in the opposite order.",
         ql(566), page="controlled-shifts",
         frm=["stream-arrays","modular-arithmetic-and-residues","primes-divisibility-gcd-and-coprimality","fixed-tape-model"]),
     KS,
     inf("S2.3", "To supply the $W^k$ rows the power-width call needs, exchange the top $\\rho=O(\\log e)$ digits of each chunk one pair at a time and pad the row count to a multiple of $W^k$, at most doubling the volume.",
         ql(1660)),
     inf("S2.4", "Write the remaining width in base $m$ as $e-\\rho=\\sum_j a_jm^j$ with $a_j<m$ and interchange the $a_j$ pieces of width $m^j$ with power-width calls.",
         ql(1692), frm=["logarithms-floors-ceilings-and-powers-of-two"]),
     inf("S2.5", "The costs sum to $O(V)\\sum_j a_jm^{j\\tau}=O(Ve^{\\tau})$, since $a_j<m$ and $m^k<me$ make this geometric.",
         ql(1705)),
     inf("S2.6", "For binary chunks of $u$ bits take the least $e$ with $q^e\\ge2^u$ and pad both ranges to $[q^e]$, increasing volume by a constant factor, so the bound is $O(Vu^{\\tau})$ because $e=O(u)$.",
         ql(1721)),
    ],
    page="chunk-swap",
    frm=["fixed-tape-model","stream-arrays","controlled-shifts","power-width-interchange","matrix-shear","frames","subspace-labels","bank-exchange-network","logarithms-floors-ceilings-and-powers-of-two"])

# ---------------------------------------------------------------- simultaneous butterfly layer
S31 = show("S3.1",
    "The two-point kernel $C=H\\mathsf SH=aI+bX$ satisfies $H_0=b\\mathsf S C\\mathsf S$, and the complex bank-exchange network with binary labels realizes $C^{\\otimes e}$ on a group of $e=mf$ selected bits by $s_{\\rm c}$ calls on $f$ bits each.",
    "Express every edge's phase frame change as a product of translation kernels $aI+bX_v$, one per vector of an orthonormal basis of the edge residual, and telescope the frames.",
    mot("The bit network works on permutations of data; for a butterfly one needs the same exchange-and-restore structure with Gaussian dyadic scalars, which the phase frames $\\mathcal C_U$ supply.", "reconstructed"),
    [
     inf("S3.1.a", "Direct multiplication gives $H_0=b\\mathsf S C\\mathsf S$, $C^2=X$, $C^4=I$ and $C^{-1}=bI+aX=-iZCZ$, using only Gaussian dyadic coefficients.",
         ql(1827), frm=["complex-numbers","matrices-invertibility-and-rank"]),
     inf("S3.1.b", "The frame change of an edge from label $U_-$ to $U_+$ is $\\prod_{j=1}^{\\rho_{\\rm edge}}(aI+bX_{v_j})^{\\epsilon_j}$, one directional kernel per vector $v_j$ of an orthonormal basis of the edge residual, including on decreasing edges.",
         ql(1840), frm=["subspace-labels","bilinear-orthogonal"]),
     inf("S3.1.c", "A negative directional kernel needs only one forward child, because $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$ and the wrappers are address signs and fourth-root phases.",
         ql(1887)),
     inf("S3.1.d", "Summing the residual dimensions of the network on $e=mf$ selected axes gives exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
         ql(1905), frm=["bank-exchange-network","frames"]),
     inf("S3.1.e", "After the source and sink corrections and undoing the bank exchange, the telescoped phase frames give $C^{\\otimes e}$ on every role, including roles whose initial scratch values were arbitrary.",
         ql(1912)),
     inf("S3.1.f", "On all $D$ selected bits $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$, where $\\mathcal S_D$ multiplies by $i^{x_1+\\cdots+x_D}$ and $b^D$ is a binary shift and a fourth-root phase with at most one extra factor $b$.",
         ql(1930), frm=["butterfly-layers"]),
    ],
    page="phase-kernel-network",
    frm=["bank-exchange-network","frames","subspace-labels","bilinear-orthogonal","butterfly-layers","complex-numbers","euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle"])

S32 = show("S3.2",
    "A binary row addition $y\\gets y\\oplus x$ on the selected bit $j_i=\\rho+iK$ of each of $f$ chunks at once, using a third chunk as restored temporary space, costs $O(V(L^{\\tau}+1))$ in the family of parameters used.",
    "Apply eight conditional cyclic shifts of whole chunk ranges that act correctly away from an explicit small set $\\mathcal B$ of bad addresses, then correct $\\mathcal B$ deterministically by a sort.",
    mot("A chunk interchange per selected bit would again cost one pass per bit; packing all selected bits of the chunks into whole-chunk shifts handles all of them with a constant number of fast chunk interchanges.", "reconstructed"),
    [
     inf("S3.2.a", "Eight conditional additions of $\\pm1$ to two integers $u,w$ with control $c$ perform the net map $(u',w')=(u+c(1-2(u\\bmod2)),w)$: the parity of $u$ flips exactly when $c=1$ and the auxiliary integer $w$ is restored.",
         ql(2016), frm=["bitwise-xor","modular-arithmetic-and-residues"]),
     inf("S3.2.b", "Each line applied simultaneously to all $f-1$ segment pairs is a single cyclic shift of a whole chunk by an offset that does not depend on the target, so it is a bijection costing $O(V)$ after one chunk swap by controlled shifts.",
         ql(2066), frm=["chunk-swap","controlled-shifts"]),
     inf("S3.2.c", "The packed result agrees with the ideal XOR map except on addresses where some guard value lies within 10 of an end of its range; the union bound over the $2(f-1)$ guards, each with twenty excluded values among $2^{K-1}$, gives $|\\mathcal B|\\le\\delta_{\\rm bad}M$ with $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$.",
         ql(2099), frm=["quantifiers-sets-and-basic-asymptotic-notation-beyond-big-o"]),
     inf("S3.2.d", "The ideal map $T_0$ and the shift composition $S_0$ are bijections that agree off $\\mathcal B$, so $T_0S_0^{-1}$ fixes the complement of $\\mathcal B$ and permutes $\\mathcal B$.",
         ql(2114), frm=["permutations-and-permutation-matrices"]),
     inf("S3.2.e", "The exceptional records are extracted with destination keys, sorted by stable radix sort, and reinserted by one full-stream scan, and the last selected position is handled by a two-bit XOR, so the total is $O(V(L^{\\tau}+1))$ plus negligible terms.",
         ql(2195)),
    ],
    page="packed-selected-bits",
    frm=["chunk-swap","controlled-shifts","stream-arrays","bitwise-xor","modular-arithmetic-and-residues"],
    salient="The worst-case bound survives although the packed shifts are wrong on a few addresses: the bad set depends only on addresses, never on data, and its measure shrinks as $2^{-K}$.")

S33 = show("S3.3",
    "The cost per unit volume of a layer on $e$ chunks satisfies $F(e)\\le(s/W)F(e/m)+O((eK)^{\\tau}+1)$, which sums to $O(d^{\\lambda'})$ for the whole $d$-chunk layer.",
    "Repeat the key recursion for the complex network, with children on volume $V/W$, stop at $e<d^{\\beta}$ with individual kernels, and sum the internal and leaf contributions over a base-$m$ decomposition of the chunk count.",
    mot("Separate butterfly factors would require $D$ whole-array passes; the recursion makes the cost a power of $d$ below one by the same mechanism as the chunk interchange.", "explicit",
        qt("factors would require $D$ whole-array passes.")),
    [
     inf("S3.3.a", "The phase construction supplies one recursive call on a slot for each vector in an edge residual basis, hence exactly $s$ calls per network invocation, while binary basis changes, scalar gates and reassembly cost $O(V((eK)^{\\tau}+1))$ at the node.",
         ql(2289), frm=["power-width-interchange","phase-kernel-network"]),
     inf("S3.3.b", "Rows come from the first $q_0$ chunks, whose concatenated bits form a row index of range $2^{q_0K}\\ge W^{k_0}$, padded to a multiple of $W^{k_0}$ with at most a factor-two growth, so each child gets a $1/W$ share of the volume.",
         ql(2317)),
     inf("S3.3.c", "With normalized cost $F(e)$, $F(e)\\le (s/W)F(e/m)+O((eK)^{\\tau}+1)$ and $F(e)=O(e)$ for $e<d^{\\beta}$.",
         ql(2407)),
     inf("S3.3.d", "The $s$ child calls run on streams of volume $V/W$, so their total cost is $s(V/W)F(e/m)$, which after dividing by $V$ gives the factor $s/W$.",
         ql(2410)),
     inf("S3.3.e", "Internal nodes have $K\\le d^c\\le e^{c/\\beta}$, so the overhead is $O(e^{\\lambda})$, and with $a=s/W\\le m^{\\sigma}<m^{\\lambda}$ the internal costs sum to $O(e^{\\lambda})$.",
         ql(2419), frm=["geometric-series-and-orthogonality-of-sums-of-roots-of-unity"]),
     inf("S3.3.f", "Leaves with $u<d^{\\beta}$ chunks contribute at most $O(a^ju)\\le O(e^{\\sigma}d^{\\beta(1-\\sigma)})$, using $a^j\\le m^{j\\sigma}=(e/u)^{\\sigma}$.",
         ql(2426)),
     inf("S3.3.g", "Adding the at most $(m-1)(1+\\lfloor\\log_m d\\rfloor)$ base-$m$ pieces and the row preprocessing gives $O(d^{\\lambda'})$ for any fixed $\\lambda'$ with $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$.",
         ql(2440)),
    ],
    salient="This is the same strict-saving mechanism as for chunk interchange: with $a=s/W<m^{\\sigma}$ and $\\sigma<1$ the per-level factor beats the growth $m$, giving a fixed power $d^{\\lambda'}$ of the number of chunks below $d$.")

S34 = show("S3.4",
    "The layer can be evaluated exactly in Gaussian dyadics with $p+\\lceil C_0d^{C_1}\\rceil$ fractional bits and then truncated once, with the width still $O(p)$.",
    "Bound the arithmetic depth $A(e)$ of the recursion, which controls how many halvings and doublings an intermediate value can undergo.",
    mot("Intermediate operators of the accelerated network need not be contractions, so their growth must be bounded explicitly to allow exact evaluation before one truncation.", "explicit",
        qt("need not be contractions.  We now give explicit constants that bound")),
    [
     inf("S3.4.a", "The depth satisfies $A(e)\\le sA(e/m)+E$ at an internal node and $A(e)\\le 8e$ at a leaf, with $E=64(W+m+1)^3$, since depth concatenates the $s$ calls rather than dividing by $W$.",
         ql(2515)),
     inf("S3.4.b", "With $B=s+E$ and $\\nu=\\min\\{j: m^j\\ge B\\}$ this gives $A(e)\\le 8dB^{k+1}\\le 8B^2d^{\\nu+1}$.",
         ql(2534)),
     inf("S3.4.c", "A value at depth $\\ell$ lies in $2^{-(p+\\ell)}\\mathbb Z[i]$ with modulus at most $2^\\ell$, so reserving $p+\\Delta$ fractional bits and $\\Delta+3$ integer bits, $\\Delta=\\lceil C_0d^{C_1}\\rceil$, represents every intermediate exactly.",
         ql(2569)),
     inf("S3.4.d", "Choosing $\\epsilon C_1<1$ with $d=\\Theta(p^{\\epsilon})$ makes $\\Delta=o(p)$ and the total width $O(p)$.",
         ql(2582)),
    ])

S35 = inf("S3.5",
    "The procedure returns $Q_p(\\mathcal H z)$ in the same array and format in $O(Vd^{\\lambda'})$ time, with error below $\\sqrt2\\,2^{-p}$ and values in the unit disk.",
    ql(2663))
S36 = inf("S3.6",
    "Every row of $\\mathcal H$ has absolute row sum one, so $\\mathcal H$ maps disk arrays to disk arrays, and truncation toward zero keeps the disk and changes each component by less than $2^{-p}$.",
    ql(2752), frm=["fixed-point-disk-grid","norms-and-the-triangle-inequality"])

S3 = show("S3",
    "A normalized butterfly layer $H_0(u,v)=((u+v)/2,(u-v)/2)$ on one bit position in each of $D\\le d$ address chunks of polynomial records is applied exactly, followed by one truncation, in $O(Vd^{\\lambda'})$ time for a fixed $\\lambda'<1$.",
    "Run the key recursion with the complex phase network instead of the bit network, using the packed XOR of selected bits for the binary changes of basis, evaluate everything exactly in Gaussian dyadics and truncate once at the end.",
    mot("Separate butterfly factors would require $D$ whole-array passes.", "explicit", qt("factors would require $D$ whole-array passes.")),
    [S31, S32, S33, S34, S35, S36],
    page="simultaneous-butterfly-layer",
    frm=["phase-kernel-network","packed-selected-bits","chunk-swap","power-width-interchange","subspace-labels","butterfly-layers","fixed-point-disk-grid","negacyclic-ring","controlled-shifts","stream-arrays","geometric-series-and-orthogonality-of-sums-of-roots-of-unity"],
    adds=[add("d","axis count","The number of address chunks, equivalently transform axes, on which a layer acts simultaneously; $d=\\Theta(p^{\\epsilon})$.","count"),
          add("K","chunk width","The number of address bits in one chunk, $K=\\lfloor d^{c}\\rfloor$.","count"),
          add("\\lambda'","layer exponent","A fixed rational exponent below one for the layer cost $O(Vd^{\\lambda'})$.","direct")],
    salient="One pass over the array handles $d$ butterfly bits at cost $d^{\\lambda'}$ per bit-volume with $\\lambda'<1$, instead of $d$ whole-array passes.")

# ---------------------------------------------------------------- ring convolution
S41 = show("S4.1",
    "In the ring $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ with $\\omega_t=y^{2r/t}$, the transforms $F_t^-$, $F_t^+$ satisfy $F_t^+F_t^-=t^{-1}I$ even though the ring has zero divisors.",
    "Prove directly that $\\sum_k\\omega_t^{jk}$ vanishes when $t\\nmid j$, by shifting the summation index, instead of dividing by $\\omega_t^j-1$.",
    mot("The ring has zero divisors, so character cancellation is verified directly instead of dividing by $\\omega_t^j-1$.", "explicit",
        qt("The ring has zero divisors, so we verify character cancellation")),
    [
     inf("S4.1.a", "For a power of two $t$ dividing $2r$ put $\\omega_t=y^{2r/t}$; powers of $\\omega_t$ are signed coefficient shifts and isometries, so both normalized transforms are contractions.",
         ql(2798), frm=["negacyclic-ring"]),
     inf("S4.1.b", "Write $j=2^vj_0$ with $j_0$ odd and $0\\le v<\\log_2 t$; replacing $k$ by $k+t/2^{v+1}$ permutes the summands and multiplies their sum by $y^{rj_0}=-1$.",
         ql(2820), frm=["modular-arithmetic-and-residues"]),
     inf("S4.1.c", "Hence the sum is zero, since the additive group of $\\mathcal R_r$ has no two-torsion, and expanding the composite transforms gives $F_t^+F_t^-=t^{-1}I$.",
         ql(2824), frm=["geometric-series-and-orthogonality-of-sums-of-roots-of-unity"]),
    ],
    page="synthetic-transform",
    frm=["negacyclic-ring","dft-cyclic-convolution","algebraic-structures-groups-rings-and-isomorphisms","geometric-series-and-orthogonality-of-sums-of-roots-of-unity","norms-and-the-triangle-inequality"],
    salient="Roots of unity are powers of $y$, so twiddle multiplications are free signed shifts, and the inverse identity still holds despite zero divisors because $y^{rj_0}=-1$ and the ring has no two-torsion.")

S42 = show("S4.2",
    "The radix-2 decimation-in-frequency recursion computes $F_t^-$ with its outputs stored in bit-reversed order $B_t$, and the opposite procedure consumes that stored order directly.",
    "Split each length-$t$ transform into a butterfly $H_0$, a twiddle monomial on the second half, and two length-$t/2$ transforms, and track which address bit holds which frequency bit.",
    mot("Keeping the frequencies in the order the recursion writes them avoids moving whole frequency indices and lets the opposite transform run the recursion backwards.", "recoverable"),
    [
     inf("S4.2.a", "The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for $0\\le k<t/2$ and applies $H_0$, writing the two outputs in the same slots with high address bit $b=0$ or $1$.",
         ql(2833)),
     inf("S4.2.b", "This computes $F_t^-$ because $(F_t^-z)_{2h+b}=\\frac1{t/2}\\sum_{k<t/2}(\\omega_t^2)^{-hk}\\omega_t^{-bk}\\frac{z_k+(-1)^bz_{k+t/2}}2$.",
         ql(2840)),
     inf("S4.2.c", "After all $a=\\log_2t$ rounds the named slots from high to low contain the frequency bits from low to high, so entry $j$ is stored at slot ${\\rm rev}_a(j)$.",
         ql(2864)),
     inf("S4.2.d", "The consuming procedure runs the recursion in reverse, each level being half the inverse of the forward level because $H_0^2=I/2$, so the pair implements $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
         ql(2872)),
     inf("S4.2.e", "For several axes the individual axis steps group into one parallel butterfly $\\mathcal H$ followed by one recordwise monomial $J_E$, because each twiddle depends only on its own axis's address bits.",
         ql(2899), frm=["multidim-transform"]),
    ],
    page="butterfly-layers",
    frm=["synthetic-transform","multidim-transform","dft-cyclic-convolution","permutations-and-permutation-matrices","discrete-math-proof-techniques"])

S43 = show("S4.3",
    "A positional layout permutation $L$ puts the selected bits of all axes at a common offset in $K$-bit chunks, so every round is one simultaneous layer and the transform costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error below $\\sqrt2\\ell 2^{-p}$.",
    "Move the top slots into a prefix, rearrange the remaining chunks by chunk interchanges, then run the rounds with one truncation per round.",
    mot("A layer needs the same bit offset in consecutive chunks of every participating axis, which the stored axis-major order does not provide.", "recoverable"),
    [
     inf("S4.3.a", "The transform cost is $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ and the forward procedure may retain its output layout for the pointwise product and the opposite procedure.",
         ql(2983)),
     inf("S4.3.b", "At most $D(b+1)=O(dK)$ slots are moved into a prefix, costing $O(TpdK)$; rounds on prefix slots are done bit by bit.",
         ql(3008)),
     inf("S4.3.c", "The remaining chunks are reordered by at most $Dq-1$ exchanges of width-$K$ chunks, each $O(TpK^{\\tau})$, so all cost $O(Tp\\,pK^{\\tau-1})$ since $Dq=O(p/K)$.",
         ql(3026), frm=["chunk-swap"]),
     inf("S4.3.d", "The simultaneous layer applies per round at cost $O(Tpd^{\\lambda'})$, and in total at most $\\ell$ rounds cost $O(Tp\\ell d^{\\lambda'})$.",
         ql(3104), frm=["simultaneous-butterfly-layer"]),
     inf("S4.3.e", "The monomial $y^E$ with $E=er+s$ is a split of the coefficient list before position $r-s$, the tail put before the head and negated, with the common sign $(-1)^e$.",
         ql(3151), frm=["negacyclic-ring"]),
     inf("S4.3.f", "Starting with zero error each of at most $\\ell$ rounds adds less than $\\sqrt2\\,2^{-p}$ because contractions do not increase the error and the layout permutations are isometries.",
         ql(3176), frm=["fixed-point-disk-grid"]),
     inf("S4.3.g", "The exact operators are $LBF^-_{\\boldsymbol t}$ forward and $F^+_{\\boldsymbol t}B^{-1}L^{-1}$ for the opposite procedure; the final charged movement $L^{-1}$ restores axis-major physical order.",
         ql(3199)),
    ],
    page="transform-layout",
    frm=["synthetic-transform","butterfly-layers","simultaneous-butterfly-layer","chunk-swap","fixed-point-disk-grid","negacyclic-ring","multidim-transform"])

S44 = show("S4.4",
    "Two disk-grid polynomials in $\\mathcal R_r$ can be multiplied exactly and returned as $Q_p(fg/r)$ in time $O(rp\\log(rp))$ by signed Kronecker packing and the established $O(N\\log N)$ multiplier.",
    "Evaluate the integer-coefficient parts at $B_0=2^{4p}$ with centered carries, multiply the four pairs of integers, and recover signed coefficients by centered residues modulo $B_0$.",
    mot("An integer multiplier multiplies integers, not polynomials; evaluating a polynomial at a large power of two turns a polynomial product into an integer product from which the coefficients can be read back.", "reconstructed"),
    [
     inf("S4.4.a", "Write $f=2^{-p}(a+ib)$, $g=2^{-p}(c+ie)$ with integer polynomials and set $A_u=u(B_0)=\\sum_ju_jB_0^j$ with $B_0=2^{4p}$ for $u\\in\\{a,b,c,e\\}$; each magnitude fits in $4pr$ bits.",
         ql(3243), frm=["polynomials"]),
     inf("S4.4.b", "Every coefficient of any of the ordinary products satisfies $|h_j|\\le r2^{2p}<2^{3p}<B_0/2$, so the fields never overlap and the next coefficient is the centered residue modulo $B_0$.",
         ql(3260)),
     inf("S4.4.c", "At block $j$ the unique integer $\\widehat h_j\\in[-B_0/2,B_0/2)$ congruent to $q_j+\\rho_j$ modulo $B_0$ equals $h_j$, and the carry $\\rho_{j+1}=(q_j+\\rho_j-\\widehat h_j)/B_0$ stays in $\\{0,1\\}$.",
         ql(3299), frm=["modular-arithmetic-and-residues"]),
    ],
    page="signed-kronecker-packing",
    frm=["nlogn-subroutine","negacyclic-ring","polynomials","convolution-as-polynomial-multiplication","binary-representation-of-integers","modular-arithmetic-and-residues"])
# extra children continue after S4.4
S44["children"].append(
    inf("S4.4.d", "The real and imaginary numerator streams $ac-be$ and $ae+bc$ reduce modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$, and the result is shifted right by $p+\\ell$ bits to give $Q_p(fg/r)$.",
        ql(3332)))

S4_rest = [
    inf("S4.5", "Perform both forward transforms, retain their common $LB$ order, multiply corresponding records, apply the opposite procedure to that order and multiply exactly by $M=T/r$.",
        ql(3415)),
    inf("S4.6", "Expanding the finite sums gives $F^-_{\\boldsymbol t}(f*g)=M(F^-_{\\boldsymbol t}f)(F^-_{\\boldsymbol t}g)$, hence $MF^+_{\\boldsymbol t}((F^-f)(F^-g)/r)=(f*g)/(rM)$.",
        ql(3425), frm=["dft-cyclic-convolution","multidim-transform"]),
    inf("S4.7", "Since $LB$ permutes records and leaves their polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$, so the opposite procedure applied to the pointwise product of the stored forward outputs equals the exact normalized convolution up to the scale $M$.",
        ql(3437)),
    inf("S4.8", "With $\\delta=\\sqrt2\\ell2^{-p}$ and $\\eta=\\sqrt2\\,2^{-p}$ the bilinear contraction bound gives error below $3\\delta+\\eta$ before the exact scale and $\\sqrt2\\,M(3\\ell+1)2^{-p}$ after multiplying by $M$.",
        ql(3473), frm=["norms-and-the-triangle-inequality"]),
]

S4 = show("S4",
    "Normalized convolution $\\mathcal M_r(f,g)=(f*g)/(rM)$ of arrays over $\\mathbb C[y]/(y^r+1)$ is computed with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$ by two forward synthetic transforms, pointwise ring products and the opposite transform.",
    "Transform both operands to the frequency domain of the polynomial ring, multiply pointwise by signed packing, and transform back, keeping the stored frequency order throughout.",
    mot("Pointwise multiplication commutes with applying the same record permutation to both operands, so the forward outputs can be multiplied in their retained order and passed directly to the opposite procedure.", "explicit",
        qt("permutation $LB$ to both operands.  We may therefore multiply the")),
    [S41, S42, S43, S44] + S4_rest,
    page="ring-convolution",
    frm=["synthetic-transform","butterfly-layers","transform-layout","signed-kronecker-packing","negacyclic-ring","dft-cyclic-convolution","multidim-transform","fixed-point-disk-grid","simultaneous-butterfly-layer"],
    adds=[add("r","record length","The number of complex coefficients of a polynomial record in $\\mathbb C[y]/(y^r+1)$; $r=2^{\\ell}$ is a power of two.","count")])

# ---------------------------------------------------------------- resampling
S5a = [
    inf("S5.1", "The Gaussian identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ and the estimate $\\|N-I\\|<2^{-\\alpha^2\\theta}$ from Harvey and van der Hoeven make $N=C\\mathsf T\\mathsf D$ invertible by a Neumann series.",
        ql(3604), frm=["gaussian-function","gaussian-resampling"]),
    inf("S5.2", "Set $A=\\mathsf S'$ and $B_0=\\mathsf D'\\mathsf J'C$, both contractions, where $\\mathsf S'=\\mathsf S/2$, $\\mathsf J'=N^{-1}/2$, $\\mathsf D'=2^{-(2\\alpha^2-2)}\\mathsf D$.",
        ql(3625)),
    inf("S5.3", "The normalizations multiply to $2^{-2\\alpha^2}$, giving $B_0P_tF_tA=2^{-2\\alpha^2}P_sF_s$, i.e. $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ with both permutations $P_s,P_t$ left inside the identity.",
        ql(3640), salient="The two coordinate permutations of the usual resampling identity stay in the formula instead of being executed as sorts, saving two sorts per coordinate."),
    inf("S5.4", "Tensoring over the $d$ axes gives $RF_{\\boldsymbol s}=2^{\\gamma}\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$ and contractions $\\mathcal A,\\mathcal B_0$.",
        ql(3813), frm=["multidim-transform"]),
    inf("S5.5", "Axis $i$ has at most $T/t_i$ lines, so the one-dimensional algorithms cost $\\sum_iT/t_i\\cdot O(t_ip^{3/2+\\delta}\\alpha)=O(dTp^{3/2+\\delta}\\alpha)$.",
        qt("At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$,")),
    inf("S5.6", "Exposing and restoring each axis of the padded box needs $O(d)$ adjacent interchanges, hence $O(d^2)$ in all, each costing $O(Tp(1+\\ell^{\\tau}))$ by the chunk swap.",
        ql(3887), frm=["chunk-swap"]),
]

S52 = show("S5.b",
    "For even $t_i$ the chirp identity $QF_{\\boldsymbol t}u=\\overline a\\cdot\\frac{a*(\\overline a\\cdot u)}{T}$ leaves the target permutation $Q$ unexecuted, and the source permutation $R$ cancels: $(RF^+_{\\boldsymbol s})[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
    "Verify the chirp coefficient identity entry by entry, and prove $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$ by a change of summation variable because each $t_i$ is a unit modulo $s_i$.",
    mot("Executing $Q$ and $R$ would cost two sorts per coordinate; if the chirp formula absorbs $Q$ and the opposite transform absorbs $R$, no sort is needed.", "recoverable"),
    [
     inf("S5.b.1", "The coefficient of $u_{\\boldsymbol k}$ on the right side is $\\frac1T\\exp(2\\pi i\\sum_is_ij_ik_i/t_i)$, precisely the coefficient of $QF_{\\boldsymbol t}$ because $Q$ reads frequency $(-s_ij_i)_i$.",
         qt("This is precisely the coefficient in $QF_{\\boldsymbol t}$, because"), frm=["bluestein-chirp","euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle"]),
     inf("S5.b.2", "Substituting $h=ck$ gives $(F_q^+R_cz)_j=(R_c^{-1}F_q^+z)_j$ for a unit $c$ modulo $q$, so $F^+_{\\boldsymbol s}R=R^{-1}F^+_{\\boldsymbol s}$ and $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$.",
         ql(3961), frm=["primes-divisibility-gcd-and-coprimality","permutations-and-permutation-matrices"]),
     inf("S5.b.3", "Using the convolution rule $F_{\\boldsymbol s}(u*v)=S(F_{\\boldsymbol s}u)\\cdot(F_{\\boldsymbol s}v)$ and $F^+_{\\boldsymbol s}F_{\\boldsymbol s}=I/S$ gives $F^+_{\\boldsymbol s}(F_{\\boldsymbol s}u\\cdot F_{\\boldsymbol s}v)=(u*v)/S^2$.",
         ql(3981), frm=["dft-cyclic-convolution","multidim-transform"]),
    ],
    page="chirp-permutation-cancel",
    frm=["bluestein-chirp","resampling-no-sort","dft-cyclic-convolution","multidim-transform","gaussian-resampling","primes-divisibility-gcd-and-coprimality","permutations-and-permutation-matrices"],
    salient="The source permutation $R$ vanishes from the product: the two forward transforms each carry one $R$, and the opposite transform carries the matching $R$, so $RF^+R=F^+$ removes all three.")

S5 = show("S5",
    "Gaussian resampling $RF_{\\boldsymbol s}=2^{\\gamma}\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ expresses a source transform of pairwise coprime lengths through a power-of-two tensor transform, with the permutations $R,Q$ retained in the identity and never executed as sorts, at tape cost $O(dTp^{3/2+\\delta}\\alpha+Tp\\,d^2(1+\\ell^{\\tau}))$.",
    "Derive the one-dimensional identity from the Gaussian identity and an invertible correction, tensor it over the axes, and move axes with chunk interchanges; then absorb $Q$ into a chirp formula and cancel $R$ across the convolution.",
    mot("Its usual implementation sorts twice on each coordinate; retaining both permutations in the transform formula avoids that.", "explicit",
        qt("Its usual implementation sorts twice on each")),
    S5a + [S52],
    page="resampling-no-sort",
    frm=["gaussian-resampling","multidim-transform","dft-cyclic-convolution","chunk-swap","fixed-point-disk-grid","gaussian-function","norms-and-the-triangle-inequality"],
    salient="The target permutation $Q$ and the source permutation $R$ are never executed, so no full sort per coordinate is needed.")

# ---------------------------------------------------------------- assembly
S61 = show("S6.1",
    "Fixing $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^{\\epsilon}\\rfloor$, padded size $T\\in[4n/b,8n/b)$, record length $r$, power-of-two axis lengths $t_i\\in\\{r/2,r\\}$ and distinct odd primes $s_i\\in((1-2\\eta)t_i,(1-\\eta)t_i]$ makes $Tp=\\Theta(n)$ and satisfies every hypothesis of the interfaces.",
    "Choose fixed rational exponents with enough slack, define the sizes from $n$, find the primes by a deterministic search in intervals that provably contain more than $d$ of them, and check the resampling hypotheses.",
    mot("The prime lengths $s_i$ must be close to the powers of two $t_i$: their product must fill a fixed fraction of the padded box while each ratio $t_i/s_i$ leaves enough separation for resampling.", "explicit",
        qt("The distinct prime lengths $s_i$ must be close to the powers of two")),
    [
     inf("S6.1.a", "The exponents are fixed rationals $\\tau=\\sigma=1-2^{-50}$, $\\beta=\\tfrac12$, $\\delta=\\tfrac1{16}$, $\\lambda=1-2^{-52}$, $c=2^{-56}$, $\\lambda'=1-2^{-54}$, $C_1=20$, $\\epsilon=2^{-75}$, $\\kappa=2^{-182}$.",
         ql(4010), frm=["rational-numbers-dyadic-rationals-and-exact-arithmetic"]),
     inf("S6.1.b", "For large $n$ put $b=\\lceil\\log_2 n\\rceil$, $p=6b$, $d=\\lfloor b^{\\epsilon}\\rfloor$, $K=\\lfloor d^{c}\\rfloor$.",
         ql(4055), frm=["logarithms-floors-ceilings-and-powers-of-two"]),
     inf("S6.1.c", "These choices give $Tp=\\Theta(n)$, $d=\\Theta(p^{\\epsilon})$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$ and $r=2^{\\Theta(p^{1-\\epsilon})}$, so $r$ exceeds every fixed power of $p$.",
         ql(4069)),
     inf("S6.1.d", "In the interval $((1-2\\eta)x,(1-\\eta)x]$ there are at least $\\eta x/(2\\log x)$ primes, which exceeds $d$ for $x=r/2$ and $x=r$ with $\\eta=1/(4d)$, so distinct odd primes $s_i$ with $\\gcd(s_i,t_i)=1$ exist.",
         ql(4118), frm=["primes-divisibility-gcd-and-coprimality"]),
     inf("S6.1.e", "Multiplying the lower bounds and using the strict Bernoulli inequality gives $S/T>(1-\\tfrac1{2d})^d>\\tfrac12$, so $T/2<S<T$ for $S=\\prod_is_i$.",
         ql(4145)),
     inf("S6.1.f", "With $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$ one gets $\\alpha^4\\theta_i>3db\\ge6b=p$, the hypothesis $\\theta>p/\\alpha^4$ of the resampling lemma.",
         ql(4149)),
     inf("S6.1.g", "Writing the inputs as polynomials in $2^b$ with $q=\\lceil n/b\\rceil$ digits gives a product of degree at most $2q-2<T/2<S$, so cyclic convolution modulo $x^S-1$ has no wraparound, and every coefficient is below $2^{3b}$.",
         ql(4183), frm=["radix-digit-convolution"]),
    ],
    page="parameter-choice",
    frm=["primes-divisibility-gcd-and-coprimality","logarithms-floors-ceilings-and-powers-of-two","radix-digit-convolution","resampling-no-sort","rational-numbers-dyadic-rationals-and-exact-arithmetic","fixed-point-disk-grid","simultaneous-butterfly-layer","transform-layout","chunk-swap"])

S62 = show("S6.2",
    "The map $\\Phi:\\mathbb C[x]/(x^S-1)\\to\\mathbb C[x_1,\\dots,x_d]/(x_i^{s_i}-1)$, $x\\mapsto\\prod_ix_i^{\\mu_i}$, is an isomorphism preserving cyclic convolution and is implemented in $O(Tp\\,d^2(1+\\ell^{\\tau}))$ time by triangular controlled cyclic shifts.",
    "Use the Chinese remainder theorem with prefix products $P_i$ and $\\mu_i=P_i^{-1}\\bmod s_i$, so that the new coordinate $b_i$ depends only on lower digits and can be updated in the order $i=d,\\dots,1$.",
    mot("A map whose coordinates depend only on earlier ones is a controlled cyclic shift, which the tape does in linear time, while a general Chinese-remainder reordering would need a sort.", "recoverable"),
    [
     inf("S6.2.a", "The assignment $\\Phi:\\mathbb C[x]/(x^S-1)\\to\\mathbb C[x_1,\\ldots,x_d]/(x_1^{s_1}-1,\\ldots,x_d^{s_d}-1)$, $x\\mapsto\\prod_ix_i^{\\mu_i}$ respects $x^S=1$ and so defines an algebra map.",
         ql(4212), frm=["algebraic-structures-groups-rings-and-isomorphisms"]),
     inf("S6.2.b", "The image of $x$ has order $S$ because each $\\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all basis monomials once, and $\\Phi$ is an isomorphism preserving cyclic convolution.",
         ql(4220), frm=["primes-divisibility-gcd-and-coprimality"]),
     inf("S6.2.c", "For $k=\\sum_ja_jP_j$ the coordinate in axis $i$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}$, since terms with $j>i$ are divisible by $s_i$ and $\\mu_iP_i\\equiv1$.",
         ql(4228), frm=["modular-arithmetic-and-residues"]),
     inf("S6.2.d", "After reordering the axes to $(a_1,\\ldots,a_d)$ update the targets in the order $i=d,d-1,\\ldots,1$, so no lower-index control has yet changed when target $i$ is updated.",
         ql(4252), frm=["controlled-shifts"]),
     inf("S6.2.e", "Insertion and deletion of padding cost $O(Tp)$ each and the axis reversals cost $O(d^2)$ chunk swaps, so $\\Phi$, its inverse and the padding cost $O(Tp\\,d^2(1+\\ell^{\\tau}))$.",
         ql(4291), frm=["chunk-swap"]),
    ],
    page="crt-axis-map",
    frm=["dft-cyclic-convolution","multidim-transform","controlled-shifts","stream-arrays","chunk-swap","modular-arithmetic-and-residues","primes-divisibility-gcd-and-coprimality","algebraic-structures-groups-rings-and-isomorphisms"])

S63 = show("S6.3",
    "The map $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ is a ring isomorphism from $\\mathbb C[x_d]/(x_d^r-1)$ to $\\mathcal R_r$, so complex cyclic convolution on the power-of-two axes equals $D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$.",
    "Multiply coefficient $k$ by $\\zeta^k$; the negative wrap of $y^r=-1$ becomes the cyclic wrap after untwisting because $\\zeta^r=-1$.",
    mot("The synthetic transforms only handle the negacyclic ring, while the chirp identity gives a cyclic convolution; a diagonal twist converts one to the other.", "recoverable"),
    [
     inf("S6.3.a", "The map $x_d\\mapsto\\zeta y$ is well defined because $(\\zeta y)^r=(-1)(-1)=1$, and on the bases it multiplies coefficient $k$ by the nonzero number $\\zeta^k$, so it is an isomorphism with inverse $\\zeta^{-k}$.",
         ql(4308), frm=["negacyclic-ring","algebraic-structures-groups-rings-and-isomorphisms","euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle"]),
     inf("S6.3.b", "For $k+l=j+hr$ with $h\\in\\{0,1\\}$ a product term after twisting and negacyclic reduction has factor $\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j$.",
         ql(4317)),
     inf("S6.3.c", "Hence normalized complex cyclic convolution is $\\mathcal M_{\\mathbb C}(f,g)=D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$, and $\\mathcal M_{\\mathbb C}$ is a bilinear contraction.",
         qt("by $T$ is already part of $\\mathcal M_r$.  The maps $D_\\pm$ and"), frm=["negacyclic-ring"]),
    ],
    page="coefficient-twist",
    frm=["negacyclic-ring","dft-cyclic-convolution","algebraic-structures-groups-rings-and-isomorphisms","euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle","complex-numbers","fixed-point-disk-grid"])

S64 = show("S6.4",
    "The source transform $\\widetilde{\\mathscr F}$ applies the Gaussian map $\\mathcal A$, a chirp transform evaluated by a twisted ring convolution, the map $\\mathcal B_0$ and an exact scale by $2^{\\gamma}$; its exact counterpart is $RF_{\\boldsymbol s}$.",
    "Compose the pieces in the order of the resampling identity, replacing the middle factor $QF_{\\boldsymbol t}$ by chirp multiplications around a complex convolution.",
    mot("The resampling identity expresses $RF_{\\boldsymbol s}$ through $QF_{\\boldsymbol t}$, and the chirp lemma turns $QF_{\\boldsymbol t}$ into a convolution, which the twisted ring convolution computes.", "recoverable"),
    [
     inf("S6.4.a", "$\\widetilde{\\mathscr F}$ applies the linewise approximation to $\\mathcal A$, then the computed chirp transform $\\widetilde{\\mathscr C}$, then the linewise approximation to $\\mathcal B_0$, then multiplies the grid numerators exactly by $2^{\\gamma}$.",
         ql(4457), frm=["resampling-no-sort","chirp-permutation-cancel","coefficient-twist","ring-convolution"]),
     inf("S6.4.b", "Its exact counterpart is $\\mathscr F=2^{\\gamma}\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$, and the opposite-sign version is obtained by conjugating input and output.",
         ql(4463)),
    ],
    page="source-transform",
    frm=["resampling-no-sort","chirp-permutation-cancel","coefficient-twist","ring-convolution","parameter-choice","crt-axis-map","fixed-point-disk-grid","gaussian-resampling","bluestein-chirp"])

S66 = show("S6.6",
    "The recovered coefficients have error below $1/2$, so rounding gives the exact convolution coefficients, and propagating radix-$2^b$ carries yields the $2n$-bit product.",
    "Track the disk norms and the error of each computed object in units of $2^{-p}$, rescale by the known factors $S$ and $2^{2b+4}$, and compare the total with $1/2$.",
    mot("The true coefficients are integers, so any approximation with error below one half determines them uniquely by rounding.", "recoverable"),
    [
     inf("S6.6.a", "A computed ring convolution has error $E_{\\rm ring}:=M(3L+2)<5TL$ in units of $2^{-p}$ and, if one operand has norm at most $.7$, norm below $.701$.",
         ql(4591), frm=["ring-convolution","norms-and-the-triangle-inequality"]),
     inf("S6.6.b", "Inserting the exact normalized convolution gives $\\|\\widetilde{\\mathcal M}_{\\mathbb C}(f,g)-\\mathcal M_{\\mathbb C}(f,g)\\|<(E_{\\rm ring}+4+4+4)h_p<6TLh_p$ with $h_p=2^{-p}$.",
         ql(4617), frm=["coefficient-twist"]),
     inf("S6.6.c", "The chirp transform has error below $8TLh_p$, and the source transform before scaling has error below $2dp^2+8TL$, hence $E_s=9\\cdot2^{\\gamma}TL$ after the scale $2^{\\gamma}$.",
         ql(4652), frm=["source-transform"]),
     inf("S6.6.d", "Applying the exact opposite contraction $G=RF^+_{\\boldsymbol s}$ to the computed pointwise product and scaling by $S$ gives error $E_w:=S(3E_s+2)<28\\cdot2^{\\gamma}T^2L$ for $w=(u*v)/S$.",
         ql(4709), frm=["chirp-permutation-cancel"]),
     inf("S6.6.e", "After the exact scale by $2^{2b+4}S$ the absolute error is below $448b\\,2^{-b+\\gamma}\\le448b\\,2^{-3b/4}<\\tfrac12$ because $p=6b$, $S\\le T<2^b$ and $\\gamma\\le b/4$.",
         ql(4726)),
     inf("S6.6.f", "The true coefficients are integers and the error is strictly below $1/2$, so the nearest integer to $H_j/2^p$ is the unique correct coefficient, which lies in $[0,2^{3b})$.",
         ql(4730), frm=["rational-numbers-dyadic-rationals-and-exact-arithmetic"]),
     inf("S6.6.g", "The carry recurrence $k_0=0$, $d_j=(c_j+k_j)\\bmod Q_0$, $k_{j+1}=\\lfloor(c_j+k_j)/Q_0\\rfloor$ with $Q_0=2^b$ keeps $0\\le k_j\\le q(Q_0-1)<Q_0^2$.",
         ql(4776), frm=["modular-arithmetic-and-residues","discrete-math-proof-techniques"]),
     inf("S6.6.h", "The invariant $\\sum_{h<j}c_hQ_0^h=\\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ shows the digits $d_j$ are the first radix digits of the product.",
         ql(4787)),
     inf("S6.6.i", "The exact product is less than $2^{2n}$, so all bits above position $2n-1$ are zero; removing only those padding bits (and zero inputs obeying the same rule) gives exactly $2n$ output bits.",
         ql(4802)),
    ],
    page="exact-recovery",
    frm=["source-transform","parameter-choice","fixed-point-disk-grid","norms-and-the-triangle-inequality","radix-digit-convolution","chirp-permutation-cancel","coefficient-twist","ring-convolution","rational-numbers-dyadic-rationals-and-exact-arithmetic"])

S6 = show("S6",
    "The algorithm splits the inputs into radix-$2^b$ digits, maps them by $\\Phi$ to prime axes, takes two source transforms, multiplies pointwise, applies the opposite-sign transform with the two scalings by $S$, rounds, undoes $\\Phi$ and propagates carries to output the $2n$-bit product exactly.",
    "Choose the sizes, build each ingredient (axis map, twist, source transform) in the order the algorithm uses it, run the six steps, and prove that rounding and carries give the exact product.",
    mot("The three transforms evaluate a convolution of the digit lists; applying the transform of one prime-length convolution as a product of transforms is exactly how convolution becomes pointwise multiplication.", "reconstructed"),
    [S61, S62, S63, S64,
     inf("S6.5.a", "Apply the coefficient-address map $\\Phi$ with its padded layout to the digit lists, obtaining source arrays $u,v$ of exact $p$-bit grid values of norm below $1/4$.",
         ql(4508), frm=["crt-axis-map","radix-digit-convolution"]),
     inf("S6.5.b", "Compute the two source transforms $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$.",
         ql(4511), frm=["source-transform"]),
     inf("S6.5.c", "Multiply corresponding complex coefficients exactly and truncate each part toward zero to $p$ fractional bits to get the array $z$.",
         ql(4513), frm=["fixed-point-disk-grid"]),
     inf("S6.5.d", "Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, which by the cancellation identity yields an approximation of $w=(u*v)/S$.",
         ql(4517), frm=["chirp-permutation-cancel"]),
     inf("S6.5.e", "Multiply by $2^{2b+4}S$, round the real values to the nearest integers, write the coefficients in $(3b+1)$-bit words and apply $\\Phi^{-1}$ with removal of padding to restore the ordinary coefficient order.",
         ql(4521)),
     inf("S6.5.f", "Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits.",
         ql(4530)),
     S66],
    page="multiplication-algorithm",
    frm=["exact-recovery","source-transform","crt-axis-map","parameter-choice","radix-digit-convolution","coefficient-twist","ring-convolution","fixed-point-disk-grid"],
    adds=[add("b","digit width","The number of bits in one radix digit, $b=\\lceil\\log_2 n\\rceil$.","count"),
          add("T","padded size","The number of entries of the padded power-of-two box $\\prod_it_i$, a power of two in $[4n/b,8n/b)$.","count"),
          add("S","prime-axis size","The product $s_1\\cdots s_d$ of the pairwise coprime prime source lengths, with $T/2<S<T$.","count")])

# ---------------------------------------------------------------- cost accounting
S7a = show("S7.a",
    "Dividing by $Tp$, the dominant costs are seven normalized terms with powers of $p$ that all lie strictly below one.",
    "List each operation's cost per unit volume $Tp$ and its power of $p$ in a table.",
    mot("Each primitive was proved in terms of the volume $V=Tp$, so its cost in the multiplication is its normalized factor times $Tp$.", "recoverable"),
    [
     inf("S7.a.1", "Prefix-slot moves and individual butterfly rounds cost $dK$ per unit volume, a power $p^{\\epsilon(1+c)}$.", ql(4822)),
     inf("S7.a.2", "Chunk exchanges for the transform layout cost $pK^{\\tau-1}$, a power $p^{1-\\epsilon c(1-\\tau)}$.", ql(4823)),
     inf("S7.a.3", "Simultaneous butterfly rounds cost $\\ell d^{\\lambda'}$, a power $p^{1-\\epsilon(1-\\lambda')}$.", ql(4824)),
     inf("S7.a.4", "CRT and axis layouts cost $d^2(1+\\ell^{\\tau})$, a power $p^{\\tau+\\epsilon(2-\\tau)}$.", ql(4825)),
     inf("S7.a.5", "Gaussian line maps cost $dp^{1/2+\\delta}\\alpha$, a power $p^{3/4+\\delta+3\\epsilon/2}$.", ql(4826)),
     inf("S7.a.6", "Chirps, twists and scalar products cost $dp^{\\delta}$, a power $p^{\\epsilon+\\delta}$.", ql(4827)),
     inf("S7.a.7", "Packed polynomial products cost $\\log(rp)$, a power $p^{1-\\epsilon}$.", ql(4828)),
    ])

S7b = show("S7.b",
    "Each of the seven powers is at most $1-2\\kappa$, the smallest margin being $g_2=\\epsilon c(1-\\tau)=2^{-181}=2\\kappa$.",
    "Subtract each power from one to get margins $g_1,\\dots,g_7$ and compare them by direct substitution of the fixed exponents.",
    mot("This explicit slack will cover any remaining fixed power of $\\log p$.", "explicit",
        qt("Thus $\\min_i g_i=2^{-181}=2\\kappa$.  This explicit slack will cover")),
    [
     inf("S7.b.1", "Direct substitution gives $g_1>\\frac12$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>\\frac18$, $g_6>\\frac12$, $g_7=2^{-75}$.", ql(4851)),
     inf("S7.b.2", "Thus $\\min_ig_i=2^{-181}=2\\kappa$, and this explicit slack covers any remaining fixed power of $\\log p$.", ql(4854),
         salient="The smallest margin $g_2=\\epsilon c(1-\\tau)$ comes from the chunk-exchange row and contains the factor $1-\\tau=2^{-50}$, so the exponent $\\kappa$ is limited by how much the interchange saves."),
    ])

S7c = show("S7.c",
    "The rows of the table follow from the stated procedures, setup and exceptional streams are lower order, and the total is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
    "Re-derive the normalized factor of each row from the cost lemma that supplies it, bound the setup and sorting terms, then multiply by $Tp$.",
    mot("Rows must be justified individually since each combines a different lemma's cost with the parameter choice.", "recoverable"),
    [
     inf("S7.c.1", "The layout uses $O(p/K)$ exchanges of width-$K$ chunks, each costing $O(VK^{\\tau})$, so the normalized total is $O(p/K)K^{\\tau}=O(pK^{\\tau-1})$.", ql(4866), frm=["chunk-swap"]),
     inf("S7.c.2", "Gaussian resampling lines cost $\\sum_iT/t_i\\cdot O(t_ip^{3/2+\\delta}\\alpha)$, and dividing by $V=Tp$ with $\\alpha=\\Theta(p^{1/4+\\epsilon/2})$ gives the fifth row.", ql(4888), frm=["resampling-no-sort"]),
     inf("S7.c.3", "Setup at layer and layout recursions costs at most $p^{A+C}=o(Tp)$ because there are at most $p^A$ visits.", ql(4925)),
     inf("S7.c.4", "Each of the seven displayed powers is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^{\\kappa}$ eventually.", ql(4984)),
     inf("S7.c.5", "The large-input bound is therefore $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.", ql(4987)),
     inf("S7.c.6", "Below a fixed cutoff beyond all size, precision and layout conditions, schoolbook multiplication is used, and the finitely many smaller lengths are absorbed into the implicit constant.", ql(4990)),
    ])

S7 = show("S7",
    "The total time is $O(n(\\log n)^{1-\\kappa})$ because each of the seven dominant normalized costs, divided by $Tp=\\Theta(n)$, is at most $p^{1-2\\kappa}$.",
    "Tabulate costs divided by $Tp$ with their powers of $p$, compare the margins below one, justify each row, and add.",
    mot("The saving over $n\\log n$ is a power of $\\log n$ exactly when every term is at most a fixed power of $p$ below one.", "recoverable"),
    [S7a, S7b, S7c],
    page="cost-accounting",
    frm=["multiplication-algorithm","parameter-choice","chunk-swap","simultaneous-butterfly-layer","transform-layout","ring-convolution","resampling-no-sort","crt-axis-map","signed-kronecker-packing","big-o","logarithms-floors-ceilings-and-powers-of-two"],
    salient="Seven different operations each save a power of $p$, and the weakest margin $2^{-181}=2\\kappa$ fixes the final exponent.")

S1 = inf("S1",
    "Splitting each input into radix-$2^b$ digits reduces the integer product to the convolution of two short digit lists, whose coefficients are then carried into a binary product.",
    ql(76), page="radix-digit-convolution",
    frm=["polynomials","binary-representation-of-integers","schoolbook-multiplication-and-divide-and-conquer-multiplication","convolution-as-polynomial-multiplication"])

ROOT_NODE = show("S0",
    "A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$.",
    "Reduce the product to a digit convolution, evaluate it by Gaussian resampling and synthetic ring transforms, speed up the two bottlenecks (address interchange and butterfly layers) by one rank-saving linear network, then recover the integer exactly and total the cost.",
    mot("Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both movement and arithmetic must be sped up.", "explicit",
        qt("We therefore need savings in both movement and arithmetic. Two tape")),
    [S1, S2, S3, S4, S5, S6, S7],
    page="main-theorem",
    frm=["n-log-n-conjecture","fixed-tape-model","nlogn-subroutine","big-o","turing-machine-tapes","convolution-as-polynomial-multiplication","quantifiers-sets-and-basic-asymptotic-notation-beyond-big-o"],
    adds=[add("p","precision","The number of fractional bits kept in each fixed-point coefficient, $p=6\\lceil\\log_2 n\\rceil$.","count"),
          add("\\kappa","saving exponent","The tiny positive exponent $2^{-182}$ by which the power of $\\lg n$ is lowered.","direct")],
    salient="The saving is a genuine power of $\\lg n$, $(\\lg n)^{-\\kappa}$, but with $\\kappa=2^{-182}$ it is astronomically small, so the theorem refutes the $n\\log n$ conjecture without being practical.")

tree = ROOT_NODE
def strip(n):
    if isinstance(n.get("quote"), dict):
        n["quote"] = {"source": n["quote"]["source"], "quote": n["quote"]["quote"]}
    for c in n.get("children", []):
        strip(c)
# collect lines before strip
order = []
def walk(n, out):
    if n["intention"] == "infer":
        out.append((n["id"], n["quote"]["_line"], n.get("deferred", False)))
    for c in n.get("children", []):
        walk(c, out)
walk(tree, order)
strip(tree)

# validation
pages_order = """n-log-n-conjecture radix-digit-convolution triple-gadget bank-exchange-network fixed-tape-model nlogn-subroutine stream-arrays frames controlled-shifts bilinear-orthogonal subspace-labels triangular-factorization matrix-shear power-width-interchange chunk-swap packed-selected-bits negacyclic-ring signed-kronecker-packing fixed-point-disk-grid dft-cyclic-convolution multidim-transform crt-axis-map gaussian-resampling bluestein-chirp coefficient-twist synthetic-transform butterfly-layers phase-kernel-network simultaneous-butterfly-layer transform-layout ring-convolution resampling-no-sort chirp-permutation-cancel parameter-choice source-transform exact-recovery multiplication-algorithm cost-accounting main-theorem""".split()
known = """big-o polynomials complex-numbers turing-machine-tapes modular-arithmetic-and-residues primes-divisibility-gcd-and-coprimality binary-representation-of-integers bitwise-xor logarithms-floors-ceilings-and-powers-of-two matrices-invertibility-and-rank vector-spaces-basis-and-dimension permutations-and-permutation-matrices lexicographic-order-and-index-tuples euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle geometric-series-and-orthogonality-of-sums-of-roots-of-unity norms-and-the-triangle-inequality rational-numbers-dyadic-rationals-and-exact-arithmetic algebraic-structures-groups-rings-and-isomorphisms discrete-math-proof-techniques schoolbook-multiplication-and-divide-and-conquer-multiplication multitape-machine-cost-model-and-linear-time-scans complex-polynomial-evaluation-and-interpolation gaussian-function convolution-as-polynomial-multiplication quantifiers-sets-and-basic-asymptotic-notation-beyond-big-o""".split()
assert len(pages_order) == 39, len(pages_order)
errors = []
used_pages = {}
ids = set()
from_union = set()
def check(n, eff):
    if n["id"] in ids: errors.append("dup id " + n["id"])
    ids.add(n["id"])
    pg = n.get("page") or None
    if pg:
        if pg not in pages_order: errors.append("bad page " + pg)
        if pg in used_pages: errors.append("page reused " + pg)
        used_pages[pg] = n["id"]
        eff = pg
    for f in n.get("from", []):
        from_union.add(f)
        if f in known: continue
        if f not in pages_order: errors.append(f"{n['id']}: unknown from {f}")
        elif pages_order.index(f) >= pages_order.index(eff): errors.append(f"{n['id']}: from {f} not before {eff}")
    for c in n.get("children", []):
        check(c, eff)
    if n["intention"] == "show" and not n.get("children"): errors.append("show without children " + n["id"])
    if n["intention"] == "infer" and not n.get("quote"): errors.append("infer without quote " + n["id"])
check(tree, None)
for p in pages_order:
    if p not in used_pages and p not in from_union: errors.append("page unused " + p)
# order
last = 0
for (i, ln, d) in order:
    if d: continue
    if ln < last: errors.append(f"order: {i} line {ln} < {last}")
    last = max(last, ln)
# uniqueness of quotes
def allq(n, out):
    if n["intention"] == "infer": out.append((n["id"], n["quote"]["quote"]))
    for c in n.get("children", []): allq(c, out)
qs = []; allq(tree, qs)
for i, q in qs:
    cnt = SRC.count(q)
    if cnt != 1: errors.append(f"quote {i} occurs {cnt} times: {q!r}")
# adds check
def collect_claims(n):
    out = [n["claim"]]
    for c in n.get("children", []): out += collect_claims(c)
    return out
def check_adds(n):
    for a in n.get("adds", []):
        below = []
        for c in n.get("children", []): below += collect_claims(c)
        maths = []
        for cl in below: maths += re.findall(r"\$(.+?)\$", cl)
        if not any(a["symbol"] in m for m in maths): errors.append(f"adds {a['symbol']} at {n['id']} not in descendants' math")
    for c in n.get("children", []): check_adds(c)
check_adds(tree)
print("\n".join(errors) if errors else "OK")
print(len(qs), "infer steps;", len(used_pages), "pages used")
json.dump({"root": tree}, open(ROOT + "/exegenius/tasks/0003-argument.answer.json", "w"), indent=1, ensure_ascii=False)
