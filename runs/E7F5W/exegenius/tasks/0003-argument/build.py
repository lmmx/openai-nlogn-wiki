import json, re, sys

SRC = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F5W/sources/paper.tex').read()
OUT = '/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F5W/exegenius/tasks/0003-argument.answer.json'


def ev(q):
    return {"source": "paper", "quote": q}


def mot(text, source, quote=None):
    d = {"text": text, "source": source}
    if quote:
        d["quote"] = ev(quote)
    return d


def infer(id, claim, quote, page=None, frm=None, deferred=False, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": frm or []}
    if page:
        n["page"] = page
    if deferred:
        n["deferred"] = True
    if salient:
        n["salient"] = salient
    return n


def show(id, claim, method, motivation, children, page=None, frm=None, salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children, "from": frm or []}
    if page:
        n["page"] = page
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = adds
    return n


def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


# ---------------------------------------------------------------- toolbox
R1 = show(
    "S1",
    "Linear-time scans on a fixed number of tapes can permute or move digits, split a stream on a digit and merge, split whole rows cyclically into $W$ streams, and shift a target field cyclically by an offset computed from earlier control fields.",
    "State the elementary stream scans once, with their cost $O(V)$, so that later steps can cite them.",
    mot("The interchange and butterfly procedures are built only from these scans, so they are stated first.", "explicit",
        "the elementary scans it uses."),
    [
        infer("S1.1",
              "Fixing a radix $q$, permuting two digit values, moving a digit, splitting on a digit with a pointwise map and merging, and splitting rows cyclically into $W$ streams each take $O(V)$ steps.",
              "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
              page="elementary-streams",
              frm=["multitape-model", "array-layout", "positional-notation-in-any-radix-and-mixed-radix",
                   "stable-radix-sort-and-counting-sort"]),
        infer("S1.2",
              "A target field that follows its control fields can be shifted cyclically by an offset prepared in $b^{O(1)}$ time, or multiplied by a unit modulo $q^b$, in $O(V)$ time.",
              "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
              page="controlled-shifts",
              frm=["elementary-streams", "modular-arithmetic", "extended-euclidean-algorithm"]),
    ],
    frm=["multitape-model", "array-layout"],
)

# ---------------------------------------------------------------- key step: networks and rank saving
N1 = show(
    "S2.2.1",
    "On banks indexed by triples of 3-subsets, three stages of a fixed gather, scatter, copy and side-injection schedule realize the signed exchange $(X_a,Y_a)\\mapsto(-Y_a,X_a)$, because the net coefficient of $y_S\\gets y_S+(\\cdot)x_T$ is $1$ for $T=S$ and $0$ otherwise whatever the scratch wires held.",
    "Give gather and scatter coefficients that depend on the intersection size $|S\\cap T|$, cancel the unwanted ones with side wires, and wrap the update in a subtract, add, undo schedule that restores the scratch values.",
    mot("The sources state that the coefficients depend on the intersection size and that auxiliary wires cancel the unwanted ones.", "explicit",
        "on intersection size, and auxiliary wires cancel the unwanted"),
    [
        infer("S2.2.1.1",
              "In the bit construction the copy map adds $x_T$ to the scratch wire $A_{ST}$ for each neighbour pair, the side injection adds their sum to $y_S$, and gather and scatter go through the central wires $C_i$.",
              "The copy map adds $x_T$ to $A_{ST}$ for each neighbor pair.",
              frm=["counting-subsets-and-binomial-coefficients"]),
        infer("S2.2.1.2",
              "Eight gate rows (subtract side injection, subtract scatter, copy, gather, scatter, side injection, undo gather, undo copy) first remove the effect of the unknown scratch contents, then add the true contribution, then restore the scratch values, so the net target change is independent of the initial scratch values.",
              "the following schedule remove the effect of the old scratch values;",
              page="scratch-restoration",
              frm=["linear-algebra-basics"]),
        infer("S2.2.1.3",
              "The central coefficient from $x_T$ to $y_S$ is $|S\\cap T|\\bmod 2$ (bit case) or $(|S\\cap T|-1)/2$ (complex case); the side wires cancel exactly the intersection-one (resp. zero and two) cases, so the net map is $y\\gets y+x$.",
              "In the bit case, the central coefficient from $x_T$ to $y_S$ is",
              frm=["counting-subsets-and-binomial-coefficients"]),
        infer("S2.2.1.4",
              "Running the forward schedule from $X$ to $Y$, its inverse from $Y$ to $X$, and the forward schedule again gives $(x,y)\\mapsto(x,y+x)\\mapsto(-y,y+x)\\mapsto(-y,x)$.",
              "$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
              frm=[]),
    ],
    page="subset-intersection-network",
    frm=["counting-subsets-and-binomial-coefficients", "linear-algebra-basics"],
    salient="One fixed scratch-cancellation pattern works for every intersection size of two triples (zero, one, two or three), so the exchange is exact with no special case for any pair of banks.",
)

N2 = show(
    "S2.2.2",
    "Assigning each source, gate and sink an invertible frame $D_v$ on the common address set makes the implemented operator $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$, so a route from input role $w$ to output role $\\rho(w)$ costs only the change of frame $D_{\\rm sink}D_{\\rm source}^{-1}$, applied edge by edge.",
    "Check an invariant (the stored array is $D_v$ applied to the logical array) along edges and across pointwise linear gates, which commute with a common frame.",
    mot("A pointwise linear gate commutes with a frame shared by all its wires, so frames only have to be changed between gates, along edges.", "recoverable"),
    [
        infer("S2.2.2.1",
              "At a gate the common frame commutes with the pointwise linear gate, $G(D_vg_1,\\ldots,D_vg_t)=D_vG(g_1,\\ldots,g_t)$, so the invariant continues to the sinks.",
              "the invariant continues to the sinks.",
              frm=["linear-algebra-basics"]),
        infer("S2.2.2.2",
              "For a signed role permutation the route from input role $w$ to output role $\\rho(w)$ applies $\\varepsilon_wD_{\\mathrm{sink}(\\rho(w))}D_{\\mathrm{source}(w)}^{-1}$, including the auxiliary scratch roles.",
              "In particular, if the scalar network is a signed role permutation that",
              frm=["permutations-and-permutation-matrices"]),
    ],
    page="gate-network-frames",
    frm=["array-layout", "linear-algebra-basics", "permutations-and-permutation-matrices"],
)

N3 = show(
    "S2.2.3",
    "Giving every gate and terminal a nested nondegenerate subspace of an $m$-dimensional space makes each edge cost its dimension change; the only decreasing edges are the central-wire edges from time 3 to time 4, each losing $h$, so the total absolute change is $Wm-2N+2L$ with $L<N/2$.",
    "Prescribe terminal labels, expose one tensor factor per stage, tabulate the orthogonal residual of every edge, then telescope signed dimension changes at each gate and add twice the loss on decreasing edges.",
    mot("The labels are chosen so that the changes of frame are inexpensive: an edge's work is its dimension change.", "explicit",
        "choose its intermediate labels to make the changes of frame inexpensive."),
    [
        infer("S2.2.3.1",
              "A label is a nondegenerate subspace of a bilinear space, so the space splits as the label plus its orthogonal complement; for nested labels the orthogonal residual is the complement of the smaller inside the larger, with dimension equal to the change in label dimension.",
              "\\emph{orthogonal residual} is the orthogonal complement of the smaller label inside",
              page="nondegenerate-subspaces",
              frm=["vector-norms-inner-products-and-orthogonality", "linear-algebra-basics"]),
        infer("S2.2.3.2",
              "With the form $x^{\\mathsf T}(I-J/9)y$ (bit network) or the dot product over $\\mathbb F_2$ (complex network), every triple line is nondegenerate and lines of neighbouring triples are orthogonal, since $\\langle t_S,t_T\\rangle=|S\\cap T|-1$.",
              "Thus every triple line is nondegenerate, and neighboring triple lines",
              frm=["counting-subsets-and-binomial-coefficients"]),
        infer("S2.2.3.3",
              "The source dimensions sum to $N$ (label $U_a$ on each $X_a$, zero elsewhere) and the sink dimensions sum to $Wm-N$.",
              "The source dimensions sum to $N$ and the sink dimensions to $Wm-N$.",
              frm=[]),
        infer("S2.2.3.4",
              "Because the contributions at gates cancel, the signed dimension changes sum to $Wm-2N$, and if decreasing edges lose a total $L$ the sum of absolute changes is $Wm-2N+2L$.",
              "dimension $L$, the sum of absolute changes is $Wm-2N+2L$.",
              frm=[]),
        infer("S2.2.3.5",
              "At each stage the incoming and outgoing labels are $A\\otimes\\langle t\\rangle\\otimes Q\\to(A\\otimes F)\\otimes Q$ on $X$ and $B\\otimes\\langle t\\rangle\\otimes Q\\to((B\\otimes F)\\perp(P\\otimes t^\\perp))\\otimes Q$ on $Y$, which fit together from one stage to the next.",
              "These transitions expose one tensor factor at each stage. To see that",
              frm=["vector-norms-inner-products-and-orthogonality"]),
        infer("S2.2.3.6",
              "A central wire returns once from the label $A\\otimes F$ to $B\\otimes F$, losing exactly $P\\otimes F$ of dimension $h$; the gate order confines all decreases to this return.",
              "returns once from the former label to the latter, losing exactly",
              frm=[]),
        infer("S2.2.3.7",
              "Every edge joins comparable nondegenerate labels and the only decreasing edges are the central-wire edges from time 3 to time 4, each of loss $h$.",
              "edges are the central-wire edges from time 3 to time 4; their dimension",
              frm=[]),
        infer("S2.2.3.8",
              "There are $Ic$ decreasing edges of loss $h$, so $L=Ich$; replacing signed changes by absolute changes adds $2L$, giving $Wm-2N+2L$.",
              "There are $Ic$ decreasing edges, each of loss $h$; replacing signed",
              frm=[]),
        infer("S2.2.3.9",
              "Over $\\mathbb F_2$ a nondegenerate symmetric bilinear space is nonalternating exactly when it contains a vector of norm one, and each nonzero residual here has one, so it has an orthonormal basis.",
              "is nonalternating precisely when it contains a vector of norm one.",
              frm=["bitwise-operations-xor-and-hamming-weight"]),
        infer("S2.2.3.10",
              "The loss ratios are $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$, both below $1/2$, which is the inequality that leaves a strict rank saving.",
              "\\frac{L_{\\rm b}}{N}=\\frac{100}{539},\\qquad",
              frm=[],
              salient="Both loss ratios are fixed constants (100/539 and 101/539) just under 1/2, independent of the input length, because only the central wires, one return per invocation, ever lose dimension."),
    ],
    page="subspace-labels",
    frm=["nondegenerate-subspaces", "gate-network-frames", "subset-intersection-network", "linear-algebra-basics"],
    salient="Only central wires ever decrease in label dimension, and each loses exactly $h$ once; this keeps $L$ below $N/2$ so the rank budget stays under $Wm$.",
)

N4 = show(
    "S2.2.4",
    "Using the projections $P_U$ onto the labels as frames, the bit network sends the role exchange to the shear $H\\leftarrow H+D$ on every role, with total rational edge rank $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$.",
    "Take $M_v=P_{U_v}$ as the matrix at each vertex, so each edge difference $P_V-P_U$ has rank equal to the dimension change, and add the one exceptional rank at each negative source projection.",
    mot("The rank of the difference of two projections equals the dimension change, so the earlier label count transfers to a rank count.", "recoverable"),
    [
        infer("S2.2.4.1",
              "The total rank of the edge differences is $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}$.",
              "&=W_{\\rm b}m-N+2L_{\\rm b}",
              frm=[]),
        infer("S2.2.4.2",
              "For nested nondegenerate $U\\subset V$ the matrix $P_V-P_U$ is the identity on $V\\cap U^\\perp$ and zero on its orthogonal complement, so its rank is $\\dim V-\\dim U$, and reversing the edge negates it without changing the rank.",
              "Its rank is $\\dim V-\\dim U$; reversing the",
              frm=["linear-algebra-basics"]),
        infer("S2.2.4.3",
              "The only exceptions to rank equals dimension change are the $N$ negative source projections $-P_{U_a}$ on the $X_a$.",
              "The only exceptions are the $N$ negative source projections.",
              frm=[]),
        infer("S2.2.4.4",
              "At stage 1, $B=0$ and the first gate on $X_a$ has label exactly $U_a$, so its first edge matrix is $2P_{U_a}$ of rational rank one although the dimension change is zero; this adds $N$ to the count.",
              "Its first edge matrix is therefore $2P_{U_a}$, of rational rank one,",
              frm=[]),
        infer("S2.2.4.5",
              "The deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$, so $s_{\\rm b}<W_{\\rm b}m$.",
              "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$.",
              frm=[]),
        infer("S2.2.4.6",
              "For an input $X_a$ the endpoint difference is $P_{U_a^\\perp}-(-P_{U_a})=I_m$, and every other role has source matrix $0$ and sink matrix $I$, so $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m$ on every input role.",
              "For an input $X_a$ the endpoint difference is",
              frm=[]),
    ],
    page="bit-network-interface",
    frm=["subspace-labels", "gate-network-frames", "subset-intersection-network", "linear-algebra-basics"],
)

N5 = show(
    "S2.2.5",
    "For the complex network with binary labels, the frame $\\mathcal C_U=H^{\\otimes m}\\operatorname{diag}(i^{\\operatorname{wt}(P_Ux)})H^{\\otimes m}$ turns each edge into a product of one kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal residual basis, with total length $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}<W_{\\rm c}m$, and the whole network equals $C^{\\otimes m}$ on every role.",
    "Compute the phase difference of nested binary labels by weight additivity on orthogonal vectors, rewrite each one-vector phase as $aI+bX_v$, then telescope and correct the one pair $X_a\\to Y_a$ whose frame difference is not the plain forward tensor power.",
    mot("Orthogonal binary vectors add weights modulo four, so the phase difference of nested labels splits into one factor per residual basis vector.", "recoverable"),
    [
        infer("S2.2.5.1",
              "The sum of the lengths of the residual bases over all edges is $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}$, with deficit $2N-2L_{\\rm c}>0$ (no extra source rank here, unlike the bit network).",
              "s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}",
              frm=[]),
        infer("S2.2.5.2",
              "If $z\\cdot w=0$ the supports meet in an even number of positions, so $\\operatorname{wt}(z+w)=\\operatorname{wt}(z)+\\operatorname{wt}(w)-2|\\operatorname{supp}z\\cap\\operatorname{supp}w|$ is additive modulo four.",
              "If $z\\cdot w=0$, the intersection cardinality is even, so weight is",
              frm=["bitwise-operations-xor-and-hamming-weight"]),
        infer("S2.2.5.3",
              "Each basis vector $v$ has norm one, so $\\operatorname{wt}(v)$ is odd and its phase coefficient is $\\pm1$ modulo four.",
              "Each $v$ has norm one, so $\\operatorname{wt}(v)$ is odd.",
              frm=["bitwise-operations-xor-and-hamming-weight"]),
        infer("S2.2.5.4",
              "The identity $H\\operatorname{diag}(1,-1)H=X$, tensored over $\\operatorname{supp}(v)$, sends the character $(-1)^{v\\cdot x}$ to the translation $X_v$, so the phase becomes $aI+bX_v$ or its inverse.",
              "The identity $H\\operatorname{diag}(1,-1)H=X$, tensored over the",
              frm=["two-point-butterfly"]),
        infer("S2.2.5.5",
              "Each residual vector contributes one factor acting on all $k$ columns, so the product of kernels is the $k$th tensor power of the one-column version.",
              "Thus each residual vector contributes one factor acting on all $k$",
              frm=[]),
        infer("S2.2.5.6",
              "The pair $X_a\\to Y_a$ is the exception: its operator is $C^{-1}$ on the 27 coordinates of $\\operatorname{supp}(u_a)$ and $C$ elsewhere, because $\\operatorname{wt}(u)=27$.",
              "27 coordinates of $\\operatorname{supp}(u)$ and $C$ elsewhere.",
              frm=[]),
        infer("S2.2.5.7",
              "The identity $C=iZC^{-1}Z$ with a sign wrapper $Z_{a,k}$ before and the scalar $i^{27k}Z_{a,k}$ after turns each of the $27k$ inverse factors into $C$.",
              "the identity $C=iZC^{-1}Z$ turns each of them into $C$.",
              frm=[]),
        infer("S2.2.5.8",
              "After negating the physical $X$ outputs and sending role $\\rho(w)$ back to $w$, every role, including every scratch role, carries $C^{\\otimes mk}$.",
              "Every role, including every scratch role, now has",
              frm=[]),
    ],
    page="phase-interface",
    frm=["two-point-butterfly", "subspace-labels", "bit-network-interface", "bitwise-operations-xor-and-hamming-weight"],
    salient="Every edge of the network is a product of one two-point kernel $aI+bX_v$ per residual basis vector, and the whole network collapses to the single kernel $C^{\\otimes m}$ on every role, scratch roles included.",
)

N6 = infer(
    "S2.2.6",
    "Both relative rank deficits exceed $20\\cdot2^{-50}$ and $m^{1-2^{-50}}>m(1-20\\cdot2^{-50})$, so $s_{\\rm b}/W_{\\rm b}<m^\\tau$ and $s_{\\rm c}/W_{\\rm c}<m^\\sigma$ with $\\tau=\\sigma=1-2^{-50}$.",
    "Both exact deficits displayed above are greater than $20\\cdot2^{-50}$.",
    frm=["exponential-and-logarithm-functions"],
    salient="The deficits are only about $10^{-11}$ of the budget, yet they give the fixed rational exponent $1-2^{-50}$ with $m^{\\tau}$ strictly above $s/W$.",
)

K2 = show(
    "S2.2",
    "Two fixed linear networks (a bit network over $\\mathbb F_2$ and a Gaussian-dyadic network) exchange two banks of values, restore every scratch value, and carry frames whose edge ranks sum to $s_{\\rm b}<W_{\\rm b}m$ and $s_{\\rm c}<W_{\\rm c}m$ with $m=10^6$.",
    "Build the scalar exchange from subset-intersection gates, lift it to arrays through frames, label vertices by nested subspaces so that edge cost is dimension change, then read off the two interfaces and the explicit exponent.",
    mot("The saving comes from keeping the total dimension lost on decreasing edges small relative to $N$.", "explicit",
        "The saving will come from keeping the total dimension lost on decreasing"),
    [N1, N2, N3, N4, N5, N6],
    frm=["linear-algebra-basics"],
)

K1 = show(
    "S2.1",
    "If a fixed network of $W$ wires has total edge rank $s<Wm$, a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$, so the per-volume cost obeys $F_k\\le(s/W)F_{k-1}+O(1)$, which is $O(e^\\tau)$ whenever $s/W<m^\\tau$.",
    "Count the smaller calls, divide by volume to get the factor $s/W$, and sum the geometric series, treating the cases $s/W\\le1$ and $s/W>1$ separately.",
    mot("Dividing the cost by the volume turns the $s$ calls on volume $V/W$ into the factor $s/W<m$, which is strictly less than the factor $m$ that growth of the parameter would otherwise cost.", "explicit",
        "increases the recursive contribution by $s/W<m$. This strict inequality"),
    [
        infer("S2.1.1",
              "A recursive call at parameter $mf$ uses $s$ calls at parameter $f$, each on a stream of volume $V/W$.",
              "A recursive call at parameter $mf$ therefore uses $s$ calls at parameter",
              deferred=True, frm=["divide-and-conquer-recurrences"]),
        infer("S2.1.2",
              "After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$.",
              "After dividing cost by volume, multiplying the parameter by $m$",
              deferred=True, frm=["divide-and-conquer-recurrences"]),
        infer("S2.1.3",
              "For $a=s/W<m^\\tau$ the geometric sum $\\sum_{j=0}^ka^j$ is $O(m^{k\\tau})$: if $a\\le1$ it is at most $k+1$, and if $a>1$ it is $O(a^k)$.",
              "most $k+1=O(m^{k\\tau})$; if $a>1$, it is $O(a^k)$.",
              deferred=True, frm=["convergent-series-and-the-geometric-series", "exponential-and-logarithm-functions"]),
    ],
    frm=["divide-and-conquer-recurrences", "convergent-series-and-the-geometric-series"],
)

KEY = show(
    "S2",
    "Two fixed linear networks that exchange two banks of values, restoring all scratch values, have total edge rank $s<Wm$, so a recursive call at parameter $mf$ makes $s$ smaller calls on streams of volume $V/W$ and the per-volume cost grows only like $e^\\tau$ with $\\tau<1$.",
    "Construct the networks with nested subspace labels so that the number of smaller calls equals a dimension count that is provably below $Wm$, then plug $s/W<m^\\tau$ into the divide-and-conquer recurrence.",
    mot("The strict inequality $s/W<m$ is what turns recursion on parameter $m f$ into a power saving rather than a loss.", "explicit",
        "increases the recursive contribution by $s/W<m$. This strict inequality"),
    [K1, K2],
    page="rank-saving-recurrence",
    frm=["array-layout", "elementary-streams", "controlled-shifts", "divide-and-conquer-recurrences",
         "convergent-series-and-the-geometric-series", "exponential-and-logarithm-functions", "big-o"],
    adds=[
        B("W", "wire count", "the number of wires, including scratch wires, in the fixed network", "count"),
        B("m", "label dimension", "the dimension of the label space, which is also the number of fields per chunk in one recursion step", "count"),
        B("s", "total edge rank", "the sum over all edges of the rank (number of smaller calls) of the edge's frame change", "count"),
        B("N", "bank count", "the number of index triples, so that there are $N$ source wires $X_a$ and $N$ sink wires $Y_a$", "count"),
        B("L", "decreasing loss", "the total dimension lost on edges whose label dimension decreases", "count"),
    ],
    salient="The saving is tiny but strict: the relative rank deficits are about $10^{-11}$, so $s/W$ lies below $m$ only through the exponent $\\tau=1-2^{-50}$, and it survives solely because decreasing edges lose less than $N/2$ in total.",
)

# ---------------------------------------------------------------- chunk interchange
R3_1 = infer(
    "S3.1",
    "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones.",
    "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
    page="lower-triangular-factorization",
    frm=["gaussian-elimination", "linear-algebra-basics", "permutations-and-permutation-matrices"],
)

R3_2 = show(
    "S3.2",
    "The address map $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ is performed with exactly $\\operatorname{rank}(A)$ interchanges of $b$-digit fields plus $O(V)$ further work.",
    "Factor $A=E_1\\Pi E_2$, do the lower-triangular parts by controlled shifts in linear time, and implement each one of $\\Pi$ as $H_i\\gets H_i+D_j$ through a single interchange sandwiched between two linear updates.",
    mot("Controlled shifts update a later field from earlier ones in linear time, which suits lower-triangular changes of coordinates; only the $a$ ones of $\\Pi$ then remain.", "recoverable"),
    [
        infer("S3.2.1",
              "First transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, then add $\\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$; the triangular transforms cost $O(V)$.",
              "For $A=E_1\\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,",
              frm=["controlled-shifts", "lower-triangular-factorization"]),
        infer("S3.2.2",
              "Each one in position $(i,j)$ of $\\Pi$ calls for $H_i\\gets H_i+D_j$; the three updates $D_j\\gets D_j+H_i$, swap $(H_i,D_j)$, $D_j\\gets H_i-D_j$ send $(h,d)$ to $(h+d,d)$.",
              "D_j\\leftarrow D_j+H_i,\\qquad",
              frm=["controlled-shifts"]),
        infer("S3.2.3",
              "This uses just one interchange per one of $\\Pi$, and $\\Pi$ has $a$ ones, so exactly $a$ interchanges are needed.",
              "It uses just one interchange.",
              frm=[]),
    ],
    page="matrix-shear-cost",
    frm=["lower-triangular-factorization", "controlled-shifts", "elementary-streams", "modular-arithmetic"],
    salient="Three updates, two of them linear-time controlled shifts, turn the shear $H+D$ into a swap, so the swap costs one interchange and not two.",
)

R3_3 = show(
    "S3.3",
    "Two chunks of $e=m^k$ radix-$q$ digits are interchanged in $O(Ve^\\tau)$ time: split rows into $W$ role streams, run the bit network with every edge shear done by recursive interchanges of $1/m$ the width, and obtain the interchange from three shears.",
    "Give each vertex of the bit network the frame $\\Phi_M$ (an address shear), so the endpoint difference is $\\Phi_{I_m}$, i.e. $H\\gets H+D$ on every row; implement each edge by a rank-many interchanges of width $e/m$ (matrix shear lemma); then solve the recurrence.",
    mot("The bit network turns the role exchange into the shear $H\\gets H+D$, and every edge needs only smaller interchanges, so the recursion has the shape of the rank-saving recurrence.", "recoverable"),
    [
        infer("S3.3.1",
              "Whole rows are split cyclically into $W$ role streams; each stream has volume $V/W$, the same remaining shape and a row count divisible by $W^{k-1}$.",
              "Split whole rows cyclically into $W$ role streams within each prefix",
              frm=["elementary-streams"]),
        infer("S3.3.2",
              "On every circuit edge apply the shear $\\Phi_{A_e}$ to that role stream, implemented by the matrix-shear lemma with recursive interchanges of each pivot pair of $b$-digit fields; gates act pointwise at matching addresses.",
              "$\\Phi_{A_e}$ to that role stream; implement it by",
              frm=["matrix-shear-cost", "gate-network-frames", "bit-network-interface"]),
        infer("S3.3.3",
              "The physical output satisfies $f'_{\\rho(w)}=\\Phi_{M_{\\rm out(\\rho(w))}}\\Phi_{-M_{\\rm in(w)}}f_w=\\Phi_{I_m}f_w$ by the endpoint condition, i.e. $H\\gets H+D$ on every original row including scratch rows with arbitrary values.",
              "=\\Phi_{I_m}f_w,",
              frm=["bit-network-interface"]),
        infer("S3.3.4",
              "The three componentwise updates $D\\gets D-H$, $H\\gets H+D$, $D\\gets H-D$ send $(H,D)$ to $(D,H)$, and only the middle shear uses the circuit.",
              "D\\leftarrow D-H,\\qquad H\\leftarrow H+D,\\qquad D\\leftarrow H-D,",
              frm=["controlled-shifts"]),
        infer("S3.3.5",
              "The number of recursive calls is the sum of the edge ranks, exactly $s$, each on one role stream of volume $V/W$.",
              "The number of recursive calls is the sum of the edge ranks, exactly $s$.",
              frm=["rank-saving-recurrence"]),
        infer("S3.3.6",
              "If $F_k$ bounds time divided by volume then $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
              "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).",
              frm=["rank-saving-recurrence", "divide-and-conquer-recurrences"]),
        infer("S3.3.7",
              "Since $s/W<m^\\tau$ the geometric sum gives $F_k=O(e^\\tau)$.",
              "Hence $F_k=O(e^\\tau)$.",
              frm=["rank-saving-recurrence", "convergent-series-and-the-geometric-series"]),
        infer("S3.3.8",
              "A fixed-tape depth-first schedule parks the $W-1$ inactive role streams on a stack, so each node pays only $O(V)$ for pushing, popping and copying and no step rescans parked ancestors.",
              "Reserve $W$ role tapes, a fixed set of",
              frm=["multitape-model"]),
    ],
    page="power-width-interchange",
    frm=["matrix-shear-cost", "bit-network-interface", "rank-saving-recurrence", "gate-network-frames",
         "elementary-streams", "divide-and-conquer-recurrences"],
    salient="The shear $H\\gets H+D$ (an XOR combination of the data) appears on every role stream, scratch roles included, even though the final effect is an exact permutation of the chunks.",
)

R3_4 = infer(
    "S3.4",
    "For arbitrary widths, peel off the top $\\rho=O(\\log e)$ digits of each chunk as a row index (padded to a multiple of $W^k$), split the remaining width in base $m$ into pieces of width $m^j$, interchange each pair by the power-width procedure at cost $O(V)\\sum_ja_jm^{j\\tau}=O(Ve^\\tau)$, then undo the padding and pad binary ranges to the radix $q$.",
    "Write the remaining width in base $m$:",
    frm=["power-width-interchange", "positional-notation-in-any-radix-and-mixed-radix", "elementary-streams"],
)

R3 = show(
    "S3",
    "Two disjoint address chunks of $u$ bits in an array with complete Cartesian address set can be exchanged in $O(Vu^\\tau)$ time for a fixed $\\tau<1$, although the intermediate steps form XOR combinations of the data.",
    "Run the bit network on rows at power widths $m^k$, with every edge shear performed by recursive interchanges of $1/m$ the width, and then reduce arbitrary widths and row counts to power widths.",
    mot("Because the sum of the ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width.", "explicit",
        "Because the sum of these ranks is less than the number of wires times"),
    [R3_1, R3_2, R3_3, R3_4],
    page="chunk-interchange",
    frm=["rank-saving-recurrence", "bit-network-interface", "elementary-streams", "controlled-shifts"],
)

# ---------------------------------------------------------------- butterfly layer
P_pack = show(
    "S4.6",
    "An XOR of the same bit position in $f$ chunks of one address range into another is done together by a constant number of cyclic shifts of whole chunk ranges, followed by a deterministic repair of the explicitly identified set of exceptional addresses whose density is $O(f2^{-K})$.",
    "Pack the $f$ selected bits with guard bits so a few whole-chunk cyclic shifts add all of them at once; the packing fails only where a guard value is within 10 of an end, an address-determined set that is repaired by sorting.",
    mot("A single chunk interchange per selected bit would cost too much, whereas cyclic shifts of whole chunks are linear-time controlled shifts.", "recoverable"),
    [
        infer("S4.6.1",
              "Eight modular additions with the control bit $c$ leave $(u,w)\\mapsto(u+c(1-2(u\\bmod2)),w)$: they flip the parity of $u$ exactly when $c=1$ and restore the auxiliary $w$.",
              "\\bigl(u+c(1-2(u\\bmod2)),\\ w\\bigr).",
              frm=["controlled-shifts", "modular-arithmetic"]),
        infer("S4.6.2",
              "Each packed addition agrees with the independent additions at every address whose guard values satisfy $10\\le g\\le2^{K-1}-11$, since then no segment carries into or borrows from its neighbour.",
              "There are exactly twenty excluded values for each guard in",
              frm=[]),
        infer("S4.6.3",
              "The union bound over the $2(f-1)$ guards gives $|\\mathcal B|\\le\\delta_{\\rm bad}M$ with $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$, independent of the record values.",
              "the union bound over the $2(f-1)$ guards gives",
              frm=["counting-subsets-and-binomial-coefficients"]),
        infer("S4.6.4",
              "The exceptional records are extracted with a destination key computed from the address, stably radix sorted by key and reinserted, which implements the ideal permutation exactly everywhere.",
              "Hold the full stream untouched",
              frm=["stable-radix-sort-and-counting-sort"]),
        infer("S4.6.5",
              "A binary row addition on whole slots (slot $h'$ as $x$, slot $h$ as $y$, a third slot as $z$) performs $x_{h,j}\\gets x_{h,j}\\oplus x_{h',j}$ for every $j$ at once, so a change of basis costs $O(V((eK)^\\tau+1))$.",
              "To add row $h'$ to row $h$, use slot $h'$ as $x$,",
              frm=["chunk-interchange", "bitwise-operations-xor-and-hamming-weight"]),
    ],
    page="packed-selected-bit-addition",
    frm=["chunk-interchange", "controlled-shifts", "elementary-streams", "bitwise-operations-xor-and-hamming-weight"],
)

R4_8 = show(
    "S4.8",
    "With cutoff $e<d^{\\beta}$, $\\beta=1/2$, the recurrence $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ solves to $O(e^\\lambda)$ internal cost plus $O(e^\\sigma d^{\\beta(1-\\sigma)})$ at the leaves, and a base-$m$ partition of the $D-q_0$ remaining chunks gives $O(d^{\\lambda'})$.",
    "Unroll the recurrence, bounding the overhead at internal nodes by $e^{\\tau(1+c/\\beta)}\\le e^\\lambda$ and the leaves by $a^ju\\le e^\\sigma u^{1-\\sigma}$ with $a=s/W\\le m^\\sigma$.",
    mot("Each internal node pays the overhead of the basis change, while the recursion contributes the factor $s/W<m^\\lambda$, so the geometric series is dominated by its top term.", "recoverable"),
    [
        infer("S4.8.1",
              "If $F(e)$ is time divided by volume then $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ and $F(e)=O(e)$ for $e<d^\\beta$.",
              "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),",
              frm=["rank-saving-recurrence", "divide-and-conquer-recurrences"]),
        infer("S4.8.2",
              "At internal nodes $K\\le d^c\\le e^{c/\\beta}$, so the overhead is $O(e^\\lambda)$ and, since $a=s/W<m^\\lambda$, the internal costs sum to $Ce^\\lambda\\sum_j(a/m^\\lambda)^j=O(e^\\lambda)$.",
              "C e^\\lambda\\sum_{j\\ge0}(a/m^\\lambda)^j=O(e^\\lambda).",
              frm=["convergent-series-and-the-geometric-series"]),
        infer("S4.8.3",
              "The leaves after $j$ levels hold $u=e/m^j<d^\\beta$ chunks and contribute $O(a^ju)\\le O(e^\\sigma u^{1-\\sigma})\\le O(e^\\sigma d^{\\beta(1-\\sigma)})$, using $a^j\\le m^{j\\sigma}=(e/u)^\\sigma$ (also when $a<1$).",
              "O(a^ju)\\le O(e^\\sigma u^{1-\\sigma})",
              frm=["exponential-and-logarithm-functions"]),
        infer("S4.8.4",
              "Writing $D-q_0=\\sum_ja_jm^j$ in base $m$ gives at most $(m-1)(1+\\lfloor\\log_md\\rfloor)$ pieces; the logarithmic number of groups is absorbed by a fixed $\\lambda'$ with $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$, giving $O(d^{\\lambda'})$.",
              "   =O(d^{\\lambda'})",
              frm=["positional-notation-in-any-radix-and-mixed-radix"]),
    ],
    frm=["rank-saving-recurrence", "divide-and-conquer-recurrences"],
)

R4 = show(
    "S4",
    "One $H_0$ butterfly applied at the same bit offset in $D\\le d$ address chunks at once is computed exactly by the phase network with recursive calls on $1/m$ of the axes and one final truncation, in $O(Vd^{\\lambda'})$ time with $\\lambda'<1$.",
    "Write $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$, compute $C^{\\otimes D}$ by the complex network whose edge kernels become $C$ on one slot of $f=e/m$ chunks after packed binary changes of basis, solve the recurrence and bound the exact dyadic growth.",
    mot("Separate butterfly factors would need $D$ whole-array passes, whereas the recursive network needs only $O(d^{\\lambda'})$ amortized passes.", "explicit",
        "$\\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly"),
    [
        infer("S4.1",
              "Each edge frame change is a product $\\prod_j(aI+bX_{v_j})^{\\epsilon_j}$, one directional kernel per vector of an orthonormal basis of the residual.",
              " =\\prod_{j=1}^{\\rho_{\\rm edge}}(aI+bX_{v_j})^{\\epsilon_j},",
              frm=["phase-interface", "two-point-butterfly"]),
        infer("S4.2",
              "Conjugating by the address permutation $\\mathcal P_M$ of a change of basis $M\\in\\mathrm{GL}(m,\\mathbb F_2)$ puts the residual directions in the first coordinate positions, so one child call on the $f$ chunks of slot $h$ is needed for each direction.",
              "To implement \\eqref{eq:phase-edge-coordinate} on the group, first apply",
              frm=["linear-algebra-basics", "bitwise-operations-xor-and-hamming-weight"]),
        infer("S4.3",
              "A negative directional kernel needs only one forward child, since $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$ and the wrappers are address signs and fourth-root phases.",
              "=(-i)^f Z^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}.",
              frm=["two-point-butterfly"]),
        infer("S4.4",
              "Summing the residual dimensions gives exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and $C^{\\otimes e}$ appears on every role including scratch roles with arbitrary initial values.",
              "Summing its residual dimensions gives exactly",
              frm=["phase-interface", "rank-saving-recurrence"]),
        infer("S4.5",
              "Since $H_0=b\\mathsf SC\\mathsf S$ coordinatewise, the normalized layer is $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$, where $\\mathcal S_D$ multiplies by the phase $i^{x_1+\\cdots+x_D}$ and $b^D$ is a shift and a fourth-root phase with at most one further factor $b$.",
              "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.",
              frm=["two-point-butterfly"]),
        P_pack,
        infer("S4.7",
              "The first $q_0$ chunks are processed by individual kernels in $O(V\\log d)$ time and their bits then serve as a row index of range at least $W^{k_0}$; rows are split as $u=Wg+w$ across the $W$ role streams so each child has exactly $1/W$ of the volume.",
              "At a node, write a row index as \\(u=Wg+w\\), with \\(0\\le w<W\\),",
              frm=["elementary-streams"]),
        R4_8,
        infer("S4.9",
              "The operation count along any chain obeys $A(e)\\le sA(e/m)+E$ with $E=64(W+m+1)^3$ and $A(e)\\le8e$ at leaves; since $sx+E\\le(s+E)x$, this gives $A(e)\\le8B^2d^{\\nu+1}$ and, with the diagonal and scalar corrections, at most $C_0d^{C_1}$ fractional and integer bits, which is $o(p)$.",
              "\\hbox{at an internal node},\\qquad A(e)\\le8e",
              frm=["floor-ceiling-and-rounding", "dyadic-rationals-and-binary-fractions", "fixed-point-numerics"]),
        infer("S4.10",
              "The procedure returns $Q_p(\\mathcal Hz)$ in $O(Vd^{\\lambda'})$ time; every row of $\\mathcal H$ has absolute row sum one, so the result stays in the disk and the truncation error is below $\\sqrt2\\,2^{-p}$.",
              "The procedure returns $Q_p(\\mathcal H z)$ in the same array,",
              frm=["fixed-point-numerics"]),
    ],
    page="simultaneous-butterfly-layer",
    frm=["two-point-butterfly", "fixed-point-numerics", "rank-saving-recurrence", "phase-interface", "chunk-interchange",
         "packed-selected-bit-addition", "elementary-streams"],
    adds=[
        B("D", "selected chunks", "the number of address chunks (at most $d$) whose selected bit gets the butterfly", "count"),
        B("e", "chunk group size", "the number of consecutive chunks in the group handled by one recursive call, a power of $m$", "count"),
        B("f", "slot width", "the number of chunks in one of the $m$ slots of a group, so $e=mf$", "count"),
    ],
)

# ---------------------------------------------------------------- transforms over the negacyclic ring
T_rec = show(
    "S5.1.3",
    "A radix-two decimation-in-frequency recursion with $\\log_2t$ rounds, each pairing $z_k$ with $z_{k+t/2}$, applying $H_0$ and a twiddle shift, computes $F_t^-$ leaving frequency $j$ at the bit-reversed position $\\operatorname{rev}_a(j)$; the reversed rounds compute the opposite transform from that order.",
    "Split the sum over $k$ into the pair $z_k\\pm z_{k+t/2}$ and recurse on the two branches with $\\omega_t^2$.",
    mot("Pairing $z_k$ with $z_{k+t/2}$ halves the transform length at the cost of one butterfly and one monomial per pair.", "recoverable"),
    [
        infer("S5.1.3.1",
              "The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$, applies $H_0$ to the pair and multiplies the $b=1$ output by $\\omega_t^{-k}$, which computes $F_t^-$ by the identity for $(F_t^-z)_{2h+b}$.",
              "decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for",
              frm=["two-point-butterfly", "negacyclic-ring"]),
        infer("S5.1.3.2",
              "After all $a=\\log_2t$ rounds the named slots from high to low hold the frequency bits from low to high, so $(F_t^-z)_j$ sits at slot $\\operatorname{rev}_a(j)$ (the permutation $B_t$).",
              "$\\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the",
              frm=["bitwise-operations-xor-and-hamming-weight"]),
        infer("S5.1.3.3",
              "Traversing the recursion in reverse (smaller branches first, then the inverse monomial, then $H_0$) gives half the inverse of each forward level, so the reverse procedure composed with $B_tF_t^-$ is $I/t$.",
              "The procedure consuming this stored order traverses the recursion in",
              frm=[]),
        infer("S5.1.3.4",
              "The two exact procedures therefore implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
              "B_tF_t^-,\\qquad F_t^+B_t^{-1},",
              frm=[]),
    ],
    page="butterfly-recursion",
    frm=["two-point-butterfly", "synthetic-transform", "bitwise-operations-xor-and-hamming-weight", "negacyclic-ring"],
)

T_syn = show(
    "S5.1",
    "On $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ the powers $\\omega_t=y^{2r/t}$ act as roots of unity, so $F_t^\\pm$ are contractions with $F_t^+F_t^-=t^{-1}I$ and every twiddle multiplication is a signed shift of a coefficient list.",
    "Replace complex roots of unity by powers of $y$, verify character cancellation directly (the ring has zero divisors), and group the per-axis rounds as one parallel butterfly followed by one monomial.",
    mot("Powers of $y$ act on coefficient lists by exact signed permutations, so they are exact roots of unity.", "explicit",
        "where the required roots of unity act by exact signed permutations"),
    [
        infer("S5.1.1",
              "For a power of two $t$ dividing $2r$, $\\omega_t=y^{2r/t}$, and the transforms $F_t^\\mp z$ average images of $z_k$ under isometries, hence are contractions.",
              "For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.",
              frm=["negacyclic-ring", "discrete-fourier-transform", "complex-numbers"]),
        infer("S5.1.2",
              "Writing $j=2^vj_0$ with $j_0$ odd, shifting $k$ by $t/2^{v+1}$ permutes the summands and multiplies the sum by $y^{rj_0}=-1$, so $\\sum_k\\omega_t^{jk}=0$ unless $t\\mid j$ and $F_t^+F_t^-=t^{-1}I$.",
              "Write $j=2^v j_0$ with $j_0$ odd",
              frm=["negacyclic-ring", "discrete-fourier-transform"]),
        T_rec,
        infer("S5.1.4",
              "For several axes the twiddle of one axis depends only on that axis's address bits, so the per-axis rounds group as a parallel butterfly $\\mathcal H$ followed by one recordwise monomial $J_E$ with $E=-\\sum_i(2r/u_i)b_ik_i\\pmod{2r}$.",
              "Consequently the individual axis steps may be grouped as a parallel",
              frm=["multidimensional-transform"]),
    ],
    page="synthetic-transform",
    frm=["negacyclic-ring", "discrete-fourier-transform", "multidimensional-transform", "complex-numbers"],
    salient="Every twiddle multiplication is a signed cyclic shift of a coefficient list: there is no multiplication by a complex root of unity anywhere in the transform.",
)

T_lay = show(
    "S5.2",
    "A positional permutation moves selected bits of the $d-1$ axes to a common offset in $K$-bit chunks, so each transform round is one simultaneous layer, giving forward and opposite synthetic transforms costing $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error below $\\sqrt2\\ell2^{-p}$.",
    "Move the first $b+1$ slots of each axis to a prefix by single-bit moves, bring the chunks of the same index together by $O(p/K)$ chunk interchanges, then run the rounds as simultaneous layers on chunks and as individual kernels on the prefix.",
    mot("The simultaneous layer applies one butterfly at the same offset in consecutive $K$-bit chunks, so the selected bits must first be gathered into such chunks.", "explicit",
        "we must place the selected bits of the participating axes at a common"),
    [
        infer("S5.2.1",
              "List the top bit slots of long axes and then slots $h=b-1,\\dots,0$ and move each after the prefix already formed; at most $D(b+1)=O(dK)$ slots move, costing $O(TpdK)$.",
              "Form a list of the slots to move to a prefix.",
              frm=["elementary-streams", "positional-notation-in-any-radix-and-mixed-radix"]),
        infer("S5.2.2",
              "At most $Dq-1$ exchanges of width-$K$ chunks, each costing $O(TpK^\\tau)$, put the chunks in the order $(1,1),(2,1),\\dots,(D,1),(1,2),\\dots$, for a total of $O(Tp\\,pK^{\\tau-1})$.",
              "To obtain this order, scan its target positions from left to right.",
              frm=["chunk-interchange"]),
        infer("S5.2.3",
              "The simultaneous-layer procedure applies at cost $O(Tpd^{\\lambda'})$ per round and $O(Tp\\ell d^{\\lambda'})$ in total.",
              "The simultaneous-layer procedure therefore applies at cost",
              frm=["simultaneous-butterfly-layer", "synthetic-transform"]),
        infer("S5.2.4",
              "In a round on prefix slots the bits are processed individually in $O(Tp)$ each, at most $b+1\\le K$ rounds, costing $O(TpdK)$, with a single truncation per round.",
              "In a round on prefix slots, process the participating bits individually.",
              frm=["fixed-point-numerics"]),
        infer("S5.2.5",
              "The full exact operators are $LBF_{\\boldsymbol t}^-$ and $F_{\\boldsymbol t}^+B^{-1}L^{-1}$, so the forward entry with frequency address $j$ is stored at $L(Bj)$ and the opposite procedure consumes that order.",
              "(L\\mathcal D_-L^{-1})L=LB F_{\\boldsymbol t}^-,",
              frm=["butterfly-recursion"]),
    ],
    page="transform-layout",
    frm=["simultaneous-butterfly-layer", "chunk-interchange", "synthetic-transform", "butterfly-recursion",
         "multidimensional-transform", "fixed-point-numerics"],
)

T_pack = show(
    "S5.3",
    "A product of two disk-grid polynomials modulo $y^r+1$ is computed exactly by evaluating integer parts at base $B_0=2^{4p}$, multiplying with the $O(N\\log N)$ multiplier, and reading centered coefficients back, in time $O(rp\\log(rp))$.",
    "Use signed Kronecker substitution: pack coefficients as $A_u=u(B_0)$, multiply the four pairs of evaluation integers, and recover each coefficient by its centered residue modulo $B_0$ since every coefficient is below $B_0/2$.",
    mot("The established multiplier multiplies integers, and evaluating polynomials at a large base turns polynomial products into integer products.", "explicit",
        "To multiply the polynomial records, we use the fixed-tape integer"),
    [
        infer("S5.3.1",
              "With $f=2^{-p}(a+ib)$, $g=2^{-p}(c+ie)$ set $B_0=2^{4p}$ and $A_u=u(B_0)$; each magnitude fits in $4pr$ bits.",
              "and, for $u\\in\\{a,b,c,e\\}$, define the signed evaluation integer",
              frm=["nlogn-multiplier", "binary-integers"]),
        infer("S5.3.2",
              "Every coefficient of the ordinary products satisfies $|h_j|\\le r2^{2p}<2^{3p}<B_0/2$, so the centered residue modulo $B_0$ identifies it once lower coefficients are removed.",
              "|h_j|\\leq r2^{2p}<2^{3p}<B_0/2.",
              frm=["modular-arithmetic"]),
        infer("S5.3.3",
              "Reducing modulo $y^r+1$ subtracts the coefficient at $j+r$ from the one at $j$; each result is a sum of $r$ signed products, so $|H_j|\\le r2^{2p}$ and the normalized product $fg/r$ lies in the disk.",
              "The real and imaginary numerator streams are respectively",
              frm=["negacyclic-ring"]),
    ],
    page="signed-packing",
    frm=["nlogn-multiplier", "negacyclic-ring", "fixed-point-numerics", "binary-integers", "modular-arithmetic"],
)

T_conv = show(
    "S5.4",
    "Normalized convolution $\\mathcal M_r(f,g)=(f*g)/(rM)$ over the negacyclic ring is computed by two forward synthetic transforms, pointwise polynomial products in the retained frequency order, and the opposite transform, with error below $\\sqrt2M(3\\ell+1)2^{-p}$.",
    "Convolution becomes pointwise product under $F_{\\boldsymbol t}^-$; the order $LB$ commutes with the pointwise product, so the opposite transform can consume the retained order, and the errors of the three transforms and the product add.",
    mot("Pointwise multiplication commutes with a common record permutation, so the frequency order need never be undone.", "explicit",
        "Pointwise multiplication commutes with applying the same record"),
    [
        infer("S5.4.1",
              "Perform both forward transforms, retain their common $LB$ order, multiply corresponding polynomial records with the packed product, apply the opposite procedure to that order and multiply exactly by $M=T/r$.",
              "Perform both forward transforms and retain their common $LB$ order.",
              frm=["transform-layout", "signed-packing"]),
        infer("S5.4.2",
              "Expansion of the finite sums gives $F_{\\boldsymbol t}^-(f*g)=M(F_{\\boldsymbol t}^-f)(F_{\\boldsymbol t}^-g)$, and with $F^+F^-=I/M$ this gives $MF_{\\boldsymbol t}^+((F^-f)(F^-g)/r)=(f*g)/(rM)$.",
              "F_{\\boldsymbol t}^-(f*g)",
              frm=["cyclic-convolution", "multidimensional-transform"]),
        infer("S5.4.3",
              "With $\\delta=\\sqrt2\\ell2^{-p}$ and $\\eta=\\sqrt2\\,2^{-p}$ the forward errors, the bilinear pointwise product ($<2\\delta+\\eta$) and the contractive opposite transform give error below $3\\delta+\\eta$, and the scale $M$ gives $\\sqrt2M(3\\ell+1)2^{-p}$.",
              "For the error estimate, put",
              frm=["fixed-point-numerics"]),
    ],
    page="ring-convolution",
    frm=["transform-layout", "signed-packing", "cyclic-convolution", "multidimensional-transform", "fixed-point-numerics"],
)

R5 = show(
    "S5",
    "Normalized cyclic convolution over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ of $T/r$-record arrays on $d-1$ power-of-two axes is computed by synthetic transforms in $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$ time with explicit error.",
    "Compute the convolution through the synthetic Fourier transform over the negacyclic ring, whose butterfly rounds are the fast simultaneous layers, retaining the stored frequency order, and multiply the records pointwise by signed packing.",
    mot("The synthetic transforms have exactly the shape (address rearrangements, signed shifts, two-point butterflies) that the two tape procedures accelerate.", "explicit",
        "In this representation, the transform calculation consists of address"),
    [T_syn, T_lay, T_pack, T_conv],
    frm=["negacyclic-ring", "discrete-fourier-transform", "cyclic-convolution", "multidimensional-transform"],
)

# ---------------------------------------------------------------- Gaussian resampling
G1 = show(
    "S6.1",
    "For coprime $s<t$ with $\\theta=t/s-1>p/\\alpha^4$ there are contractions $A$ and $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, computable with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$, where the two coordinate permutations stay inside the transform.",
    "Use the Gaussian resampling identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ and the invertibility of $N=C\\mathsf T\\mathsf D$ (with $\\|N-I\\|<2^{-\\alpha^2\\theta}$), then normalize to contractions and cite the ordered numerical maps.",
    mot("Resampling connects the pairwise coprime lengths of the integer product to the powers of two used by the synthetic transforms.", "explicit",
        "whereas the synthetic transforms use powers of two. Gaussian resampling"),
    [
        infer("S6.1.1",
              "The two Gaussian maps $\\mathsf S,\\mathsf T:\\mathbb C^s\\to\\mathbb C^t$ and the diagonal map $\\mathsf D$ satisfy $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ and $\\|N-I\\|<2.01e^{-\\pi\\alpha^2\\theta/2}<2^{-\\alpha^2\\theta}$ for $N=C\\mathsf T\\mathsf D$.",
              "The exact Gaussian identity and inverse estimate proved in",
              frm=["discrete-fourier-transform", "complex-numbers", "exponential-and-logarithm-functions"]),
        infer("S6.1.2",
              "Since $\\alpha^2\\theta>1$, $N$ is invertible by the Neumann series; with $\\mathsf S'=\\mathsf S/2$, $\\mathsf J'=N^{-1}/2$, $\\mathsf D'=2^{-(2\\alpha^2-2)}\\mathsf D$ all contractions, $A=\\mathsf S'$ and $B_0=\\mathsf D'\\mathsf J'C$ give $B_0P_tF_tA=2^{-2\\alpha^2}P_sF_s$.",
              "Now set $A=\\mathsf S'$ and $B_0=\\mathsf D'\\mathsf J'C$.",
              frm=["convergent-series-and-the-geometric-series", "vector-norms-inner-products-and-orthogonality"]),
        infer("S6.1.3",
              "Because the sparse Gaussian window has radius $\\lceil\\sqrt p\\rceil\\alpha$, the quoted maps $\\widetilde{\\mathsf S}'$, $\\widetilde{\\mathsf J}'$, $\\widetilde{\\mathsf D}'$ cost $O(tp^{3/2+\\delta}\\alpha)$ with errors below $16p$, $3p^2/4$ and $4$, and $C$ selects an ordered subsequence by a counter scan in $O(tp)$.",
              "Consequently we may take",
              frm=["floor-ceiling-and-rounding", "fixed-point-numerics"]),
        infer("S6.1.4",
              "Unlike the original proof, the two label-and-sort operations implementing $P_t$ and $P_s^{-1}$ are not executed: the permutations stay inside the transform identity.",
              "In \\eqref{eq:no-sort-one-dimensional} these permutations remain in the",
              frm=["permutations-and-permutation-matrices"]),
    ],
    page="gaussian-resampling",
    frm=["discrete-fourier-transform", "fixed-point-numerics", "nlogn-multiplier", "permutations-and-permutation-matrices"],
)

G2 = show(
    "S6.2",
    "The one-dimensional resampling maps applied line by line along each axis of a zero-padded power-of-two box give $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with error below $dp^2$ and cost $O(dTp^{3/2+\\delta}\\alpha)$ plus $O(Tpd^2(1+\\ell^\\tau))$ for exposing axes by chunk interchanges.",
    "Tensor the one-dimensional identity, expand axes one at a time into the padded box, and expose each axis as the innermost field by adjacent chunk interchanges.",
    mot("Each axis map acts independently on its lines, so the tensor map is a composition of $d$ line maps, with axes brought innermost by chunk interchanges.", "recoverable"),
    [
        infer("S6.2.1",
              "Tensoring the one-dimensional identity gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$.",
              "Tensoring \\eqref{eq:no-sort-one-dimensional} proves",
              frm=["multidimensional-transform"]),
        infer("S6.2.2",
              "At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$, so the cost is $\\sum_{i=1}^d(T/t_i)O(t_ip^{3/2+\\delta}\\alpha)=O(dTp^{3/2+\\delta}\\alpha)$, and the errors of the $d$ axis maps add to less than $dp^2$.",
              "At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$,",
              frm=["gaussian-resampling"]),
        infer("S6.2.3",
              "Moving an axis past its neighbour is an equal-width chunk interchange (after peeling a leading bit if widths differ), costing $O(Tp(1+\\ell^\\tau))$; exposing and restoring all axes needs $O(d^2)$ of them.",
              "costs $O(Tp(1+\\ell^\\tau))$. Exposing and restoring one axis needs",
              frm=["chunk-interchange", "elementary-streams"]),
    ],
    page="tensor-resampling-box",
    frm=["gaussian-resampling", "chunk-interchange", "multidimensional-transform", "elementary-streams"],
)

G3 = show(
    "S6.3",
    "The middle factor $QF_{\\boldsymbol t}$, including its target frequency permutation, equals a pointwise chirp phase, a cyclic convolution with the chirp, and another pointwise chirp phase: $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$.",
    "Expand the coefficient of $u_{\\boldsymbol k}$ on the right side and check that it is $T^{-1}\\exp(2\\pi i\\sum_i s_ij_ik_i/t_i)$, the coefficient of $QF_{\\boldsymbol t}$.",
    mot("The chirp identity performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array.", "explicit",
        "multiplications. The chirp identity below performs the frequency change"),
    [
        infer("S6.3.1",
              "The chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_is_ij_i^2/t_i)$ has period $t_i$ in coordinate $i$ because replacing $j_i$ by $j_i+t_i$ changes the exponent by an integral multiple of $2\\pi i$ (using that $t_i$ is even).",
              "Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by",
              frm=["complex-numbers"]),
        infer("S6.3.2",
              "The coefficient of $u_{\\boldsymbol k}$ on the right side is $\\frac1T\\overline a_{\\boldsymbol j}a_{\\boldsymbol j-\\boldsymbol k}\\overline a_{\\boldsymbol k}=\\frac1T\\exp(2\\pi i\\sum_is_ij_ik_i/t_i)$, which is the coefficient of $QF_{\\boldsymbol t}$ because $Q$ reads frequency $-s_ij_i$ from the negative-sign transform.",
              "The coefficient of $u_{\\boldsymbol k}$ in the right side of",
              frm=["discrete-fourier-transform"]),
    ],
    page="bluestein-chirp",
    frm=["discrete-fourier-transform", "cyclic-convolution", "multidimensional-transform", "complex-numbers"],
)

G4 = show(
    "S6.4",
    "The coordinate permutation $R$ left inside the resampled transform cancels across two forward transforms, their pointwise product and the opposite transform: $RF_{\\boldsymbol s}^+[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
    "Show $F_{\\boldsymbol s}^+R=R^{-1}F_{\\boldsymbol s}^+$ for a dilation $R$ by units, so $RF^+R=F^+$; since a permutation commutes with pointwise products, $R$ disappears, leaving the ordinary convolution rule.",
    mot("A coordinate permutation commutes with pointwise products and, when it is a dilation by a unit, with the opposite Fourier transform up to inverse, so it never has to be executed.", "recoverable"),
    [
        infer("S6.4.1",
              "For a unit $c$ modulo $q$ and $(R_cz)_j=z_{cj}$, substituting $h=ck$ gives $F_q^+R_cz=R_c^{-1}F_q^+z$; since each $t_i$ is a unit modulo $s_i$, tensoring gives $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$.",
              "For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$.",
              frm=["permutations-and-permutation-matrices", "modular-arithmetic", "prime-numbers-coprimality-and-trial-division"]),
        infer("S6.4.2",
              "Because a permutation commutes with pointwise products, $RF^+[R(Fu\\cdot Fv)]=F^+(Fu\\cdot Fv)$, and the convolution rule $F(u*v)=S(Fu)(Fv)$ with $F^+F=I/S$ gives $(u*v)/S^2$.",
              "The normalized convolution rule is",
              frm=["cyclic-convolution", "discrete-fourier-transform"]),
    ],
    page="permutation-cancellation",
    frm=["gaussian-resampling", "discrete-fourier-transform", "cyclic-convolution", "bluestein-chirp"],
    salient="The permutation $R$ appears on both forward transforms and on the opposite transform, and cancels completely, so neither $P_s$ nor $P_t$ is ever sorted on the tape.",
)

R6 = show(
    "S6",
    "For coprime axis lengths $s_i<t_i$ the source transform $RF_{\\boldsymbol s}$ is the power-of-two tensor transform $2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, whose middle factor is a cyclic convolution through the chirp identity and whose permutations cancel in a convolution.",
    "Retain the source and target coordinate permutations inside the transform identity instead of executing them as sorts, use Bluestein's chirp identity for the middle factor, and let the source permutation cancel across the product.",
    mot("The usual implementation of Gaussian resampling sorts twice on each coordinate; retaining the permutations in the formula avoids those sorts.", "explicit",
        "whereas the synthetic transforms use powers of two. Gaussian resampling"),
    [G1, G2, G3, G4],
    frm=["discrete-fourier-transform", "multidimensional-transform", "cyclic-convolution"],
)

# ---------------------------------------------------------------- assembly
A_size = show(
    "S7.1",
    "From $n$ set $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, a power of two $T\\in[4n/b,8n/b)$ and axis lengths $t_i\\in\\{r/2,r\\}$ with $r=2^\\ell$, so that $Tp=\\Theta(n)$ and $r$ exceeds every fixed power of $p$.",
    "Fix all exponents as small rational numbers and define every size as a power of $b$ so that all inequalities needed by the layers, the transforms and the resampling hold at once.",
    mot("Several interface lemmas need $r$ to exceed every fixed power of $p$ and $K/\\log p\\to\\infty$, which a small power $d=\\Theta(p^\\epsilon)$ of the dimension provides.", "recoverable"),
    [
        infer("S7.1.1",
              "The exponents are fixed rationals: $\\tau=\\sigma=1-2^{-50}$, $\\beta=1/2$, $\\delta=1/16$, $\\lambda=1-2^{-52}$, $c=2^{-56}$, $\\lambda'=1-2^{-54}$, $C_1=20$, $\\epsilon=2^{-75}$, $\\kappa=2^{-182}$.",
              "\\tau=\\sigma=1-2^{-50},\\qquad \\beta=\\frac12,\\qquad \\delta=\\frac1{16},",
              frm=["rank-saving-recurrence", "simultaneous-butterfly-layer"]),
        infer("S7.1.2",
              "With $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$ and $K=\\lfloor d^c\\rfloor$ the working precision is $6b$ bits and the number of axes is a tiny power of $b$.",
              "b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,",
              frm=["floor-ceiling-and-rounding", "exponential-and-logarithm-functions"]),
        infer("S7.1.3",
              "Taking $T\\in[4n/b,8n/b)$, $r=2^{\\lceil(\\log_2T)/d\\rceil}$ and $d\\ell-\\log_2T$ axes of length $r/2$, the others $r$, gives $\\prod_it_i=T$, $t_d=r$, $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$ and $r=2^{\\Theta(p^{1-\\epsilon})}$.",
              "Tp=\\Theta(n),\\quad d=\\Theta(p^\\epsilon),\\quad",
              frm=["big-theta-big-omega-and-little-o-notation"]),
        infer("S7.1.4",
              "Setting $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$, $\\gamma=2d\\alpha^2$ and $\\eta=1/(4d)$ gives $2\\le\\alpha<\\sqrt p$ and $\\gamma<28b^{2/3}=o(b)$ eventually.",
              "\\alpha=\\left\\lceil(12d^2b)^{1/4}\\right\\rceil,",
              frm=["floor-ceiling-and-rounding"]),
    ],
    page="size-parameters",
    frm=["rank-saving-recurrence", "simultaneous-butterfly-layer", "gaussian-resampling", "transform-layout"],
)

A_prime = show(
    "S7.2",
    "Distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$, $\\eta=1/(4d)$, exist and are found by trial division in $n^{o(1)}$ time; their product satisfies $T/2<S<T$ and each ratio satisfies $\\alpha^4\\theta_i>p$.",
    "Count primes in the two intervals with the explicit Rosser-Schoenfeld bound, multiply the lower bounds with Bernoulli's inequality, and read off the separation.",
    mot("The distinct prime lengths must be close to the powers of two: their product must fill a fixed fraction of the padded box while each ratio $t_i/s_i$ leaves enough separation for resampling.", "explicit",
        "The distinct prime lengths $s_i$ must be close to the powers of two"),
    [
        infer("S7.2.1",
              "For $0<\\eta<1/4$ and $x>e^{2/\\eta}$ the interval $(1-2\\eta)x<q\\le(1-\\eta)x$ contains at least $\\eta x/(2\\log x)$ primes, which exceeds $d$ for $x\\in\\{r/2,r\\}$, and the two intervals are disjoint.",
              "contains at least $\\eta x/(2\\log x)$ primes.",
              frm=["prime-numbers-coprimality-and-trial-division"]),
        infer("S7.2.2",
              "Multiplying the lower bounds and using strict Bernoulli, $S/T>(1-1/(2d))^d>1/2$, and $s_i<t_i$ gives $T/2<S<T$.",
              "\\left(1-\\frac1{2d}\\right)^d>\\frac12",
              frm=["floor-ceiling-and-rounding"]),
        infer("S7.2.3",
              "The upper bound on $s_i$ gives $\\theta_i=t_i/s_i-1\\ge\\eta/(1-\\eta)>\\eta$, hence $\\alpha^4\\theta_i>12d^2b/(4d)=3db\\ge6b=p$, the hypothesis of the resampling lemma.",
              "\\alpha^4\\theta_i>\\frac{12d^2b}{4d}=3db\\geq6b=p.",
              frm=["gaussian-resampling"]),
        infer("S7.2.4",
              "Scanning the two intervals and testing each candidate by trial division takes $O(dr^{3/2}\\mathrm{poly}(p))=n^{o(1)}=o(n)$ time.",
              "The machine finds these primes by scanning the two intervals",
              frm=["prime-numbers-coprimality-and-trial-division"]),
    ],
    page="prime-lengths",
    frm=["gaussian-resampling", "prime-numbers-coprimality-and-trial-division"],
)

A_radix = infer(
    "S7.3",
    "Writing the two inputs as polynomials in $2^b$ with $q=\\lceil n/b\\rceil$ digits each, the product has degree at most $2q-2<2n/b\\le T/2<S$, so convolution modulo $x^S-1$ has no wraparound, and each coefficient is below $2^{3b}$.",
    "Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
    page="radix-digit-convolution",
    frm=["positional-notation-in-any-radix-and-mixed-radix", "polynomials", "binary-integers",
         "schoolbook-and-karatsuba-multiplication", "cyclic-convolution"],
)

A_crt = show(
    "S7.4",
    "The map $\\Phi:x\\mapsto\\prod_ix_i^{\\mu_i}$ with $\\mu_i=P_i^{-1}\\bmod s_i$ and $P_i=\\prod_{j<i}s_j$ turns a cyclic convolution of length $S=s_1\\cdots s_d$ into a convolution on the product of cyclic axes of lengths $s_i$, and is implemented by triangular controlled shifts and axis moves in $O(Tpd^2(1+\\ell^\\tau))$.",
    "Verify that $\\Phi$ is an algebra isomorphism by the Chinese remainder theorem, write the axis coordinates in mixed radix so each is a function of lower-index digits only, and update them from the highest index down by controlled shifts.",
    mot("A change to coordinates of the product of cyclic axes is needed because the Gaussian resampling acts on a tensor of coprime lengths.", "explicit",
        "To use the source tensor, we first place the ordinary coefficient stream"),
    [
        infer("S7.4.1",
              "The assignment respects $x^S=1$ and the image of $x$ has order $S$ since each $\\mu_i$ is a unit and the $s_i$ are pairwise coprime, so $\\Phi$ is an isomorphism preserving cyclic convolution.",
              "respects $x^S=1$, so it defines an algebra map.",
              frm=["prime-numbers-coprimality-and-trial-division", "modular-arithmetic", "extended-euclidean-algorithm"]),
        infer("S7.4.2",
              "For $k=\\sum_ja_jP_j$ the axis-$i$ coordinate of $\\Phi(x^k)$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}$, since terms with $j>i$ are divisible by $s_i$ and $\\mu_iP_i\\equiv1$.",
              "b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}.",
              frm=["positional-notation-in-any-radix-and-mixed-radix"]),
        infer("S7.4.3",
              "Updating targets in the order $i=d,\\dots,1$ means each target is controlled by still-unchanged lower digits; each update is a prefix-controlled cyclic shift of the valid interval $[0,s_i)$, fixing zero padding.",
              "order $i=d,d-1,\\ldots,1$ using \\eqref{eq:triangular-crt}.",
              frm=["controlled-shifts"]),
        infer("S7.4.4",
              "The $d$ shifts copy valid and invalid intervals in $O(dV)$ time and the $O(d^2)$ axis exchanges cost $O(V(1+\\ell^\\tau))$ each, so $\\Phi$, its inverse and padding cost $O(Tpd^2(1+\\ell^\\tau))$.",
              " O\\bigl(Tp\\,d^2(1+\\ell^\\tau)\\bigr).",
              frm=["chunk-interchange"]),
    ],
    page="crt-prime-axes",
    frm=["controlled-shifts", "chunk-interchange", "prime-lengths", "positional-notation-in-any-radix-and-mixed-radix",
         "cyclic-convolution"],
)

A_twist = show(
    "S7.5",
    "Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ maps $\\mathbb C[x]/(x^r-1)$ isomorphically onto $\\mathbb C[y]/(y^r+1)$, so a complex cyclic convolution of the last axis is computed as $D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$.",
    "The twist $x_d\\mapsto\\zeta y$ is well defined since $(\\zeta y)^r=1$ and diagonal in the coefficient bases; the negative wrap of $y^r=-1$ is exactly undone by $\\zeta^r=-1$.",
    mot("The synthetic transforms need a polynomial ring modulo $y^r+1$, while the chirp convolution has a cyclic last axis.", "explicit",
        "The power-of-two complex convolution used in the chirp identity is"),
    [
        infer("S7.5.1",
              "The map $\\Theta:x_d\\mapsto\\zeta y$ is well defined since $(\\zeta y)^r=(-1)(-1)=1$, diagonal with entries $\\zeta^k$, hence an isomorphism preserving the sup norm.",
              "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.",
              frm=["negacyclic-ring", "complex-numbers"]),
        infer("S7.5.2",
              "For $k+l=j+hr$ with $h\\in\\{0,1\\}$ a twisted product term has factor $\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j$, so untwisting recovers the cyclic coefficient with the right sign.",
              "\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j.",
              frm=["negacyclic-ring", "cyclic-convolution"]),
        infer("S7.5.3",
              "The computed complex convolution twists both operands with grid approximations of $\\zeta^k$ (each phase product truncated by $Q_p$), applies $\\widetilde{\\mathcal M}_r$ and untwists the output.",
              "f'&=Q_p(\\widetilde\\theta^+\\mathbin{\\cdot}f),\\\\",
              frm=["ring-convolution", "fixed-point-numerics"]),
    ],
    page="coefficient-twist",
    frm=["ring-convolution", "negacyclic-ring", "cyclic-convolution", "fixed-point-numerics", "complex-numbers"],
)

R7 = show(
    "S7",
    "Choose precision $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$ axes, box size $T\\approx n/b$ and prime axis lengths $s_i$ with $Tp=\\Theta(n)$, and place the radix-digit coefficient list on the prime axes by a convolution-preserving map into the padded power-of-two box.",
    "Fix the rational exponents first and derive every size from them, then verify the number-theoretic facts (primes close to powers of two) and construct the layout and twist map.",
    mot("Gaussian resampling needs pairwise coprime source lengths close to powers of two, the synthetic transforms need a negacyclic last coordinate, and the box sizes must give $Tp=\\Theta(n)$.", "recoverable"),
    [A_size, A_prime, A_radix, A_crt, A_twist],
    frm=["radix-digit-convolution", "prime-numbers-coprimality-and-trial-division"],
    adds=[
        B("b", "digit bits", "the radix exponent $\\lceil\\log_2n\\rceil$, so digits have $b$ bits", "direct"),
        B("S", "source product", "the product $s_1\\cdots s_d$ of the pairwise coprime prime source lengths", "direct"),
    ],
)

# ---------------------------------------------------------------- source transform, algorithm, recovery, time
B_src = show(
    "S8.1",
    "The source transform procedure $\\widetilde{\\mathscr F}$ applies the linewise Gaussian map $A$, the chirp transform done by complex convolution through the phase twist, the linewise map $B_0$ and an exact $2^\\gamma$ rescale, approximating $RF_{\\boldsymbol s}$; its opposite is obtained by conjugation.",
    "Compose the three exact contractions $\\mathcal A$, $QF_{\\boldsymbol t}$ and $\\mathcal B_0$ of the resampling identity, each replaced by its computed approximation.",
    mot("The resampling identity $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ is already a composition of the three computable maps.", "recoverable"),
    [
        infer("S8.1.1",
              "The computed chirp transform forms $x_0=Q_p(\\overline{\\widetilde a}\\cdot x)$, $y_0=\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,x_0)$ and $Q_p(\\overline{\\widetilde a}\\cdot y_0)$.",
              "x_0&=Q_p(\\overline{\\widetilde a}\\mathbin{\\cdot}x),\\\\",
              frm=["bluestein-chirp", "coefficient-twist"]),
        infer("S8.1.2",
              "For a source disk-grid tensor of norm at most $.5$, $\\widetilde{\\mathscr F}$ applies the linewise approximation to $\\mathcal A$, the computed chirp transform, the linewise approximation to $\\mathcal B_0$ and multiplies the numerators exactly by $2^\\gamma$.",
              "For a source disk-grid tensor of norm at most $.5$, write",
              frm=["tensor-resampling-box", "gaussian-resampling"]),
        infer("S8.1.3",
              "Its exact counterpart is $\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$, and conjugating input and output gives $\\widetilde{\\mathscr F}^+$ with exact counterpart $RF_{\\boldsymbol s}^+$.",
              "\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A",
              frm=["permutation-cancellation"]),
    ],
    page="source-transform",
    frm=["bluestein-chirp", "coefficient-twist", "tensor-resampling-box", "permutation-cancellation", "gaussian-resampling"],
)

B_alg = show(
    "S8.2",
    "The multiplication algorithm splits the operands into radix digits, maps them by $\\Phi$ to prime axes, applies the source transform to each, multiplies pointwise, applies the opposite transform, rescales by $S$ and $2^{2b+4}$, rounds to integers, undoes $\\Phi$ and propagates carries.",
    "Convert the digit convolution into transforms of the two digit tensors and the opposite transform of their product, track the two scalings by $S$ and the digit scale $2^{2b+4}$, and recover the integer coefficients.",
    mot("By the cancellation lemma the three transforms compose to $(u*v)/S^2$, so only known normalizations remain to be removed.", "recoverable"),
    [
        infer("S8.2.1",
              "Each radix-$2^b$ digit $a_j$ is written as the exact grid numerator $a_j2^{p-b-2}$ in a real word followed by a zero imaginary word, so the scaled digits have norm below $1/4$.",
              "For digit $a_j$, write the exact grid numerator",
              frm=["radix-digit-convolution", "positional-notation-in-any-radix-and-mixed-radix"]),
        infer("S8.2.2",
              "Step 1 applies the coefficient-address map $\\Phi$ with its padded layout to obtain source arrays $u,v$.",
              "\\item Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain",
              frm=["crt-prime-axes"]),
        infer("S8.2.3",
              "Step 2 computes $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$, step 3 multiplies them pointwise and truncates to $p$ fractional bits, and step 4 applies $\\widetilde{\\mathscr F}^+$ to the product and multiplies by $S$.",
              "\\item Compute $\\widetilde{\\mathscr F}(u)$ and",
              frm=["source-transform"]),
        infer("S8.2.4",
              "Step 5 multiplies the numerators by $2^{2b+4}S$, rounds the real parts to the nearest integers, undoes $\\Phi$ and removes the padding; step 6 propagates carries.",
              "\\item Multiply the grid numerators of $\\widetilde w$ exactly by",
              frm=["crt-prime-axes"]),
        infer("S8.2.5",
              "The two occurrences of $S$ undo different normalizations: after the three transforms the result is $(u*v)/S^2$, after the first scale $(u*v)/S$, and the second scale gives $2^{2b+4}(u*v)$.",
              "The two occurrences of $S$ in this algorithm undo different",
              frm=["permutation-cancellation"]),
    ],
    page="multiplication-algorithm",
    frm=["source-transform", "crt-prime-axes", "radix-digit-convolution", "permutation-cancellation",
         "positional-notation-in-any-radix-and-mixed-radix"],
)

B_rec = show(
    "S8.3",
    "Disk-margin and error bookkeeping shows that the recovered real coefficients are within $1/2$ of the exact integer convolution coefficients, so rounding is exact, and radix carries give the exact binary product.",
    "Propagate norms and errors through each stage (errors of composed contractions add, bilinear contractions add the two operand errors), then show $2^{2b+4}S\\cdot E_w2^{-p}<1/2$ and bound the carries.",
    mot("A computed value within $1/2$ of an integer determines that integer; the scale factors $2^\\gamma$ and $S$ blow the error up, so $p=6b$ must leave room.", "recoverable"),
    [
        infer("S8.3.1",
              "For disk operands with one operand of norm at most $.7$ the normalized convolution has norm at most $.7$, and the computed output has norm below $.701$, so no clipping occurs.",
              "If one operand has norm at most $.7$, bilinear contraction gives",
              frm=["ring-convolution", "fixed-point-numerics"]),
        infer("S8.3.2",
              "The computed chirp transform satisfies $\\|\\widetilde{\\mathscr C}(x)-QF_{\\boldsymbol t}x\\|<8TLh_p$ with $h_p=2^{-p}$ and $L=\\log_2T$.",
              "\\|\\widetilde{\\mathscr C}(x)-QF_{\\boldsymbol t}x\\|",
              frm=["bluestein-chirp", "coefficient-twist"]),
        infer("S8.3.3",
              "The source transform error is below $E_sh_p$ with $E_s=9\\cdot2^\\gamma TL$, since $2dp^2<TL$ eventually.",
              "E_s=9\\,2^\\gamma TL,",
              frm=["tensor-resampling-box"]),
        infer("S8.3.4",
              "The pointwise product $z=Q_p(\\widetilde U\\cdot\\widetilde V_1)$ has norm at most $.26^2<.5$ and error $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$.",
              "Thus $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$.",
              frm=["fixed-point-numerics"]),
        infer("S8.3.5",
              "By permutation cancellation $G(U\\cdot V_1)=(u*v)/S^2$, so the computed opposite transform has error below $(3E_s+2)h_p$ and $\\widetilde w$ approximates $w=(u*v)/S$ within $E_wh_p$ with $E_w=S(3E_s+2)<28\\cdot2^\\gamma T^2L$.",
              "E_w:=S(3E_s+2)<28\\,2^\\gamma T^2L.",
              frm=["permutation-cancellation"]),
        infer("S8.3.6",
              "After the second scaling the absolute error is below $2^{2b+4}S\\cdot28\\cdot2^\\gamma T^2L\\cdot2^{-6b}<448b\\,2^{-b+\\gamma}\\le448b\\,2^{-3b/4}<1/2$, because $S\\le T<2^b$, $L<b$ and $\\gamma=o(b)$.",
              "2^{2b+4}S\\cdot28\\,2^\\gamma T^2L\\cdot2^{-6b}",
              frm=["exponential-and-logarithm-functions"],
              salient="The error shrinks like $2^{-3b/4}$ even though it is amplified by $2^\\gamma S T^2$; this is why the precision is $p=6b$ and $\\gamma=o(b)$ is essential."),
        infer("S8.3.7",
              "The true coefficients are integers and the error is below $1/2$, so the nearest integer to the represented value $H_j/2^p$ is the unique correct coefficient, lying in $[0,2^{3b})$.",
              "that value the unique correct coefficient.",
              frm=["floor-ceiling-and-rounding"]),
        infer("S8.3.8",
              "The carries of the recurrence $d_j=(c_j+k_j)\\bmod Q_0$, $k_{j+1}=\\lfloor(c_j+k_j)/Q_0\\rfloor$ with $Q_0=2^b$ satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$ and the invariant $\\sum_{h<j}c_hQ_0^h=\\sum_{h<j}d_hQ_0^h+k_jQ_0^j$, giving the exact $2n$-bit product.",
              "k_0=0,\\qquad d_j=(c_j+k_j)\\bmod Q_0,\\qquad",
              frm=["positional-notation-in-any-radix-and-mixed-radix", "mathematical-induction"]),
    ],
    page="exact-recovery",
    frm=["multiplication-algorithm", "ring-convolution", "bluestein-chirp", "coefficient-twist", "permutation-cancellation",
         "fixed-point-numerics"],
)

B_time = show(
    "S8.4",
    "Dividing each cost by $V=Tp$, seven dominant terms have powers of $p$ at most $1-2\\kappa$; the smallest margin $2^{-181}$ fixes $\\kappa=2^{-182}$, and any polylog factor is absorbed, giving $O(n(\\log n)^{1-\\kappa})$.",
    "Tabulate the normalized cost of every operation as a power of $p$, compute the margins $g_i$ below one, and take the minimum; absorb setup and exceptional streams into $o(V)$.",
    mot("The explicit slack in the smallest margin covers any remaining fixed power of $\\log p$.", "explicit",
        "any remaining fixed power of $\\log p$."),
    [
        infer("S8.4.1",
              "The normalized costs include prefix moves $dK$ (power $\\epsilon(1+c)$), chunk exchanges $pK^{\\tau-1}$ (power $1-\\epsilon c(1-\\tau)$), simultaneous rounds $\\ell d^{\\lambda'}$ (power $1-\\epsilon(1-\\lambda')$), layouts $d^2(1+\\ell^\\tau)$, Gaussian lines $dp^{1/2+\\delta}\\alpha$, chirps $dp^\\delta$ and packed products $\\log(rp)$.",
              "Prefix-slot moves and individual butterfly rounds & $dK$ & $\\epsilon(1+c)$\\\\",
              frm=["transform-layout", "tensor-resampling-box", "ring-convolution", "crt-prime-axes"]),
        infer("S8.4.2",
              "The margins below one are $g_1=1-\\epsilon(1+c)$, $g_2=\\epsilon c(1-\\tau)$, $g_3=\\epsilon(1-\\lambda')$, $g_4=1-\\tau-\\epsilon(2-\\tau)$, $g_5=1/4-\\delta-3\\epsilon/2$, $g_6=1-\\delta-\\epsilon$, $g_7=\\epsilon$.",
              "g_1&=1-\\epsilon(1+c),\\qquad",
              frm=["exponential-and-logarithm-functions"]),
        infer("S8.4.3",
              "Direct substitution gives $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$.",
              "g_1>\\frac12,\\quad g_2=2^{-181},\\quad g_3=2^{-129},\\quad",
              frm=[]),
        infer("S8.4.4",
              "Hence $\\min_ig_i=2^{-181}=2\\kappa$, coming from the chunk-exchange row through $g_2=\\epsilon c(1-\\tau)$.",
              "Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
              frm=[],
              salient="The smallest margin is $g_2=\\epsilon c(1-\\tau)=2^{-75}\\cdot2^{-56}\\cdot2^{-50}$, a product of three tiny exponents: the chunk-exchange cost $pK^{\\tau-1}$ with $K=\\lfloor d^c\\rfloor$ barely below $p$."),
        infer("S8.4.5",
              "Setup, descriptor work, polynomial address work per record and the compact sorting of exceptional records over at most $p^A$ visits are each $o(Tp)$, using that $r$ exceeds every fixed power of $p$ and $2^{-K}p^{A'}\\to0$.",
              "\\paragraph{Setup and exceptional streams across all calls.}",
              frm=["packed-selected-bit-addition", "stable-radix-sort-and-counting-sort"]),
        infer("S8.4.6",
              "Each of the seven powers is at most $1-2\\kappa$ and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually, so the large-input bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
              "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa}).",
              frm=["big-o"]),
        infer("S8.4.7",
              "Using schoolbook multiplication below one fixed cutoff gives a single fixed-alphabet, fixed-tape deterministic machine with worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every input length.",
              "Fix one cutoff beyond all the size, precision, margin and layout",
              frm=["schoolbook-and-karatsuba-multiplication", "multitape-model"]),
    ],
    page="time-accounting",
    frm=["transform-layout", "simultaneous-butterfly-layer", "chunk-interchange", "tensor-resampling-box",
         "ring-convolution", "crt-prime-axes", "size-parameters", "big-o"],
    salient="The saving $\\kappa=2^{-182}$ is half the smallest margin $2^{-181}$, which is itself a product of three tiny exponents, so the log factor drops only by an astronomically small power.",
)

R8 = show(
    "S8",
    "Applying the source transform to both digit tensors, multiplying pointwise, applying the opposite transform and rescaling recovers the integer coefficients exactly, and every cost fits $O(n(\\lg n)^{1-\\kappa})$.",
    "Compose the source transforms into the algorithm, then bound its rounding error by a disk-margin and error calculation, and finally tabulate the cost table.",
    mot("Exactness needs the error below $1/2$ and the time bound needs every normalized cost below $p^{1-2\\kappa}$; these two verifications are separate.", "recoverable"),
    [B_src, B_alg, B_rec, B_time],
    frm=["source-transform", "crt-prime-axes"],
)

ROOT = show(
    "S0",
    "A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
    "Reduce the product to a convolution of short digit sequences and evaluate it by Fourier transforms whose address rearrangements and butterfly layers are accelerated by two tape procedures (fast address interchange and fast simultaneous butterfly layers), each driven by a finite linear network with total edge rank below its wire count; then check that rounding is exact and add up the costs.",
    mot("Scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so savings are needed in both data movement and arithmetic.", "explicit",
        "We therefore need savings in both movement and arithmetic."),
    [R1, KEY, R3, R4, R5, R6, R7, R8],
    page="main-theorem",
    frm=["multitape-model", "nlogn-conjecture", "nlogn-multiplier", "big-o", "radix-digit-convolution"],
    adds=[
        B("p", "precision", "the number of fractional bits of the fixed-point complex values, $p=6\\lceil\\log_2n\\rceil$", "count"),
        B("d", "axis count", "the number of axes of the padded transform box", "count"),
        B("T", "box size", "the total number of entries of the padded power-of-two box, $T\\approx n/\\lceil\\log_2 n\\rceil$", "count"),
        B("r", "record length", "the number of complex coefficients in a polynomial record modulo $y^r+1$", "count"),
        B("K", "chunk width", "the number of bits in one address chunk, $K=\\lfloor d^c\\rfloor$", "count"),
        B("\\ell", "record exponent", "the base-two logarithm of $r$", "direct"),
    ],
    salient="The exponent $\\kappa=2^{-182}$ is absurdly small but positive, so the gain is a genuine power of $\\lg n$ and the $n\\log n$ conjecture fails; it is a product of nested tiny exponents ($1-\\tau=2^{-50}$, $c=2^{-56}$, $\\epsilon=2^{-75}$) all resting on the strict inequality $s<Wm$.",
)

json.dump({"root": ROOT}, open(OUT, 'w'), indent=1)


# ---------------------------------------------------------------- self-check
def walk(n, out):
    out.append(n)
    for c in n.get("children", []) or []:
        walk(c, out)
    return out

nodes = walk(ROOT, [])
ids = [n["id"] for n in nodes]
assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]
pos = 0
bad = 0
for n in nodes:
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        if q not in SRC:
            print("MISSING", n["id"], repr(q))
            bad += 1
            continue
        if n.get("deferred"):
            continue
        i = SRC.find(q, pos)
        if i < 0:
            first = SRC.find(q)
            print("OUT OF ORDER", n["id"], repr(q[:60]), "first at", first, "pos", pos)
            bad += 1
        else:
            pos = i + len(q)
    else:
        m = n.get("motivation") or {}
        if m.get("source") == "explicit":
            q = (m.get("quote") or {}).get("quote")
            if not q or q not in SRC:
                print("MISSING MOT", n["id"], repr(q))
                bad += 1
pages = [n.get("page") for n in nodes if n.get("page")]
print("pages", len(pages), len(set(pages)))
print("nodes", len(nodes), "bad", bad)

print("--- non-unique quotes")
prev=-1
for n in nodes:
    if n["intention"]=="infer" and not n.get("deferred"):
        q=n["quote"]["quote"]
        c=SRC.count(q)
        f=SRC.find(q)
        if c>1: print("MULTI",n["id"],c,repr(q[:50]))
        if f<prev: print("FIRST-OCC order issue",n["id"],f,prev)
        prev=max(prev,f)
