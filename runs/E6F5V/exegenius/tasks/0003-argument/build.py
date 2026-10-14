import json, re, sys

SRC = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F5V/sources/paper.tex').read()


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


NSRC = norm(SRC)


def ev(q):
    return {"source": "paper", "quote": q}


def infer(id, claim, quote, frm=None, page=None, deferred=False, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": frm or []}
    if page:
        n["page"] = page
    if deferred:
        n["deferred"] = True
    if salient:
        n["salient"] = salient
    return n


def show(id, claim, method, mot, children, frm=None, page=None, adds=None, salient=None):
    text, source, quote = mot
    m = {"text": text, "source": source}
    if quote:
        m["quote"] = ev(quote)
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": m,
         "children": children, "from": frm or []}
    if page:
        n["page"] = page
    if adds:
        n["adds"] = adds
    if salient:
        n["salient"] = salient
    return n


def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


# ---------------------------------------------------------------- tree

K = show(
    "S1",
    r"If a network of $W$ wires has total edge rank $s<Wm$, a call at parameter $e=mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$, so the cost per unit volume obeys $F_k\le(s/W)F_{k-1}+O(1)$ and grows only like $e^{\tau}$ with $\tau<1$.",
    "Unroll the recursion after dividing each level's cost by its volume: every level multiplies the width by $m$ but the cost only by $s/W<m$, and the resulting geometric sum is a power of the width.",
    ("A level multiplies the parameter by $m$ yet the per-volume cost only by $s/W$; because $s/W<m$ strictly, the sum over levels is $O(e^\\tau)$ with $\\tau<1$, a genuine power saving.",
     "explicit",
     r"After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving."),
    [
        infer("S1.1", r"The decisive property of the finite networks is that the total number $s$ of smaller calls satisfies $s<Wm$.",
              r"The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$."),
        infer("S1.2", r"A recursive call at parameter $mf$ uses $s$ calls at parameter $f$, each on a stream of volume $V/W$.",
              r"A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$."),
        infer("S1.3", r"After dividing by the volume, passing from $f$ to $mf$ multiplies the recursive contribution to $F_k$ by only $s/W<m$.",
              r"After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$."),
        infer("S1.4", r"For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$, so $F_k=O(e^\tau)$ with $e=m^k$.",
              r"For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$.", deferred=True),
    ],
    frm=["divide-and-conquer-recurrences", "convergent-series-and-the-geometric-series", "exponential-and-logarithm-functions", "array-layout", "big-o"],
    page="rank-saving-recurrence",
    adds=[
        B("f", "child parameter", "The size parameter (number of field digits or selected axes) of a smaller call, equal to $e/m$.", "count"),
        B("F_k", "normalized cost", "The time of a call at parameter $m^k$ divided by its logical volume."),
    ],
    salient="A relative gap between $s/W$ and $m$ that is astronomically small (about $10^{-11}$) still yields a genuine power of the width, $e^{\\tau}$ with $\\tau<1$, rather than merely a constant factor, because the saving compounds once per level of the recursion.",
)

S2 = show(
    "S2",
    r"Moving a digit, splitting a stream on a digit, cyclically splitting rows among $W$ streams and merging them, and cyclically shifting or rescaling a later field by control fields all take $O(V)$ steps on a fixed number of tapes.",
    "Prove two lemmas on single scans with counters, splitting into streams and merging.",
    ("Every later recurrence charges a node's own work as one or a few $O(V)$ passes, so the primitive operations must be shown to be linear.",
     "explicit",
     r"The present section supplies the elementary scans it uses."),
    [
        infer("S2.1", r"Four basic stream operations (permuting two digit values, moving one digit, split-map-merge on a digit, and cyclic row splitting into $W$ streams) each cost $O(V)$.",
              r"Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
              frm=["array-layout", "multitape-model", "stable-radix-sort-and-counting-sort", "lexicographic-order-and-cartesian-products-of-index-sets"],
              page="elementary-streams"),
        show("S2.2",
             r"A later target field $y\in[Q]$, $Q=q^b$, can be shifted cyclically by an offset computed from earlier control fields, or multiplied by a rational unit modulo $Q$, in $O(V)$ time.",
             "Split each fibre of the target into two consecutive pieces and merge them in the opposite order; for multiplication by a fixed integer, split into increasing pieces.",
             ("The target field follows its control fields, so one scan can read the offset and rotate the fibre without looking back.",
              "recoverable", None),
             [
                 infer("S2.2.1", r"For an offset $a$, splitting the fibre of $Q$ blocks at $Q-a$ and merging the pieces in the opposite order rotates the target field by $a$.",
                       r"For an offset $a\in[Q]$, split these blocks at $Q-a$."),
                 infer("S2.2.2", r"The permutation $y\mapsto cy\bmod Q$ for a fixed integer $c$ prime to $q$ has $c$ increasing pieces and is performed by one split and merge.",
                       r"For positive fixed integer $c$ prime to $q$, the permutation $y\mapsto cy\pmod Q$ has $c$ increasing pieces, classified by"),
             ],
             frm=["elementary-streams", "modular-arithmetic", "extended-euclidean-algorithm", "prime-numbers-coprimality-and-trial-division"],
             page="controlled-shifts"),
    ],
    frm=["array-layout", "multitape-model", "turing-machine-basics"],
)

S3 = show(
    "S3",
    r"There are two fixed linear networks, a bit network over $\mathbb F_2$ and a complex network over $\mathbb Z[i,1/2]$, that exchange two banks of values with prescribed signs, restore every scratch wire, and have total edge rank $s<Wm$.",
    "Build a scalar exchange network from subset-intersection gates, attach nested nondegenerate subspaces to its gates so that an edge costs only its dimension change, and count the dimension changes.",
    ("The scalar network already does the exchange; the free choice left is the intermediate frames, and these are chosen so that each change of frame is cheap.",
     "explicit",
     r"The scalar network already has the required signed exchange. We now choose its intermediate labels to make the changes of frame inexpensive."),
    [
        show("S3.1",
             r"Three stages of copy, gather, scatter and side-injection gates, whose net coefficient depends on the intersection size of two 3-subsets and is cancelled by scratch wires, realize $(X,Y)\mapsto(-Y,X)$ and restore every scratch wire.",
             "Make the net coefficient from a source $x_T$ to a target $y_S$ vanish except for $T=S$ by adding side wires that cancel the central coefficient, and wrap the update in a subtract-add-undo schedule.",
             ("A few central wires carry a low-rank summary that gives the wanted coordinate plus unwanted contributions from neighbouring coordinates, and the side wires subtract exactly those contributions.",
              "explicit",
              r"a low-rank linear summary gives the wanted coordinate plus contributions from known neighboring coordinates, and those contributions are subtracted."),
             [
                 infer("S3.1.1", r"Subtracting the effect of the old scratch values, adding the real contribution, then undoing the scratch effect changes the target by a net map independent of the scratch values.",
                       r"The net target change is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of $a,c$.",
                       frm=[], page="scratch-restoration"),
                 infer("S3.1.2", r"In the bit case the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod 2$, and the side contribution cancels exactly the intersection-one cases, leaving $y_S\leftarrow y_S+x_S$.",
                       r"In the bit case, the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod2$."),
                 infer("S3.1.3", r"Three stages (a forward invocation, an inverse one, a forward one) send $(x,y)$ to $(-y,x)$.",
                       r"Starting from $(x,y)$, the three stages give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$."),
             ],
             frm=["counting-subsets-and-binomial-coefficients", "modular-arithmetic", "linear-algebra-basics"],
             page="subset-intersection-network"),
        show("S3.2",
             r"If every vertex of the network carries an invertible frame $D_v$ on its wire arrays, the network implements $D_{\rm out}\mathsf S D_{\rm in}^{-1}$, so only the changes of frame $D_vD_u^{-1}$ along edges cost work.",
             "Keep each wire's array in the frame of its current vertex and observe that a pointwise linear gate commutes with a common frame.",
             ("The intermediate frames cancel along each route, so they can be chosen freely to make each edge change cheap.",
              "explicit",
              r"intermediate frames can then be chosen to make each edge change inexpensive."),
             [
                 infer("S3.2.1", r"On an edge from $u$ to $v$ the stored array is changed from $D_ug$ to $D_vg$ by applying $D_vD_u^{-1}$.",
                       r"On an edge from $u$ to $v$, apply $D_vD_u^{-1}$ to that wire's array."),
                 infer("S3.2.2", r"A pointwise linear gate commutes with the common frame of its incidences, so the frame invariant passes through every gate to the sinks.",
                       r"Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks."),
             ],
             frm=["linear-algebra-basics", "permutations-and-permutation-matrices", "array-layout"],
             page="gate-network-frames"),
        show("S3.3",
             r"Attaching to each gate and terminal a nondegenerate subspace of an $m$-dimensional space, nested along every edge, makes an edge cost its dimension change; only the central wires lose dimension, with total loss $L<N/2$, so the sum of absolute dimension changes is $Wm-2N+2L$.",
             "Choose labels from tensor products of 3-subset indicator lines and their orthogonal complements, and read off the dimension change on each edge.",
             ("Ordering the gates so that every decrease happens on one return edge per central wire keeps the loss small and makes all other edges increase.",
              "explicit",
              r"The gate order below confines all decreases to this return, while the other edges realize the prescribed stage transitions."),
             [
                 infer("S3.3.1", r"Every triple line is nondegenerate and neighbouring triple lines are orthogonal, so the label spaces can be nested along every edge.",
                       r"Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label field belonging to either construction."),
                 infer("S3.3.2", r"Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$.",
                       r"The only decreasing edges are the central-wire edges from time 3 to time 4; their dimension loss is $h$."),
                 infer("S3.3.3", r"Signed dimension changes telescope to $Wm-2N$, and replacing them by absolute changes adds $2L$.",
                       r"There are $Ic$ decreasing edges, each of loss $h$; replacing signed changes by absolute changes adds $2L$."),
                 infer("S3.3.4", r"The loss ratios are $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both below $1/2$.",
                       r"In particular, both are smaller than $1/2$."),
             ],
             frm=["nondegenerate-subspaces", "gate-network-frames", "subset-intersection-network", "vector-norms-inner-products-and-orthogonality", "linear-algebra-basics", "counting-subsets-and-binomial-coefficients"],
             page="subspace-labels",
             adds=[
                 B("N", "number of banks", "The number of index triples, equal to the sum of the source label dimensions.", "count"),
                 B("L", "total dimension loss", "The total dimension lost on decreasing edges.", "count"),
             ],
             salient="All dimension loss is confined to a single return edge on each central wire, each losing exactly the same amount $h$, in all three stages and all invocations, and the loss ratios $100/539$ and $101/539$ are both below one half."),
        show("S3.4",
             r"Using the projection matrices of the labels as frames, the XOR network turns the role exchange into the shear $H\leftarrow H+D$ on every role, with total rational edge rank $s<Wm$.",
             "Assign to each gate the projection onto its label and count the rank of each edge difference as the change of label dimension, with one extra rank per negative source projection.",
             ("The frame $\\Phi_M$ is the address shear $(H,D)\\mapsto(H+MD,D)$, so the endpoint matrix difference on a route is exactly the shear applied to that role.",
              "explicit",
              r"Using $D_v=\Phi_{M_v}$ in \eqref{eq:common-frame-identity}, the endpoint matrix difference on each routed role is exactly the shear applied to that role."),
             [
                 infer("S3.4.1", r"For nested nondegenerate $U\subset V$ the difference $P_V-P_U$ has rank $\dim V-\dim U$, so edge ranks equal the dimension changes.",
                       r"Its rank is $\dim V-\dim U$; reversing the edge negates the matrix without changing its rank."),
                 infer("S3.4.2", r"The rank sum is $s=Wm-N+2L<Wm$, since its deficit $N-2L$ is positive.",
                       r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$."),
                 infer("S3.4.3", r"The endpoint matrix difference is the identity $I_m$ on every input role, which is the shear $H\leftarrow H+D$.",
                       r"For an input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$."),
             ],
             frm=["subspace-labels", "gate-network-frames", "rank-saving-recurrence", "linear-algebra-basics", "modular-arithmetic"],
             page="bit-network-interface"),
        show("S3.5",
             r"With binary labels and the phase frame $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{\operatorname{wt}(P_Ux)})H^{\otimes m}$, every edge changes by a product of two-point kernels $aI+bX_v$, one per residual basis vector, and the whole complex network equals $C^{\otimes m}$ on every role, with total edge rank $s<Wm$.",
             "Use Hamming weight modulo 4 as a phase, which is additive over orthogonal pieces, so that each unit-norm residual vector contributes a Gaussian combination of the identity and a translation.",
             ("Weight is additive modulo four over orthogonal binary vectors and each residual vector has odd weight, so its phase $i^{\\pm[v\\cdot x]}$ is exactly a combination $aI+bX_v$ of the identity and a translation, the kernel the butterfly needs.",
              "recoverable", None),
             [
                 infer("S3.5.1", r"If $z\cdot w=0$ the weight of $z+w$ is additive modulo four, so the phase difference of an edge is a sum over an orthonormal basis of its residual.",
                       r"If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four."),
                 infer("S3.5.2", r"Each residual vector gives the kernel $aI+bX_v$ or its inverse, so an edge is a product of two-point kernels.",
                       r"The displayed phase therefore becomes $aI+bX_v$ or its inverse."),
                 infer("S3.5.3", r"The number of kernels over the network is $s=Wm-2N+2L<Wm$, since the deficit $2N-2L$ is positive.",
                       r"The deficit is $2N-2L_{\rm c}>0$."),
                 infer("S3.5.4", r"After source and sink diagonal corrections and undoing the bank exchange, every role, including every scratch role, carries the tensor product $C^{\otimes m}$.",
                       r"Every role, including every scratch role, now has the required forward tensor product."),
             ],
             frm=["subspace-labels", "gate-network-frames", "two-point-butterfly", "bit-network-interface", "bitwise-operations-xor-and-hamming-weight", "complex-numbers"],
             page="phase-interface"),
        infer("S3.6", r"Both networks satisfy $s/W<m^{\tau}$ with the explicit rational exponent $\tau=1-2^{-50}$.",
              r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,"),
    ],
    frm=["linear-algebra-basics", "counting-subsets-and-binomial-coefficients"],
    salient="The rank saving is minute: the relative deficits are only $339/22587335000000$ for the bit network and $73/19906842167500$ for the complex network, yet strictly positive, which is all the recursion needs.",
)

S4 = show(
    "S4",
    r"Two disjoint address chunks of $u$ bits in an array with complete Cartesian address set can be exchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$, although the intermediate steps form XOR combinations of the data.",
    "Realize the exchange as a shear $H\leftarrow H+D$ run through the bit network on $W$ role streams, with each edge shear done by smaller interchanges, and then remove the restrictions on width and rows.",
    ("An edge of rank $a$ costs $a$ smaller interchanges, and the ranks sum to less than $Wm$, so the recurrence saves a power of the chunk width.",
     "explicit",
     r"An edge matrix of rank $a$ will require $a$ smaller interchanges. Because the sum of these ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width."),
    [
        infer("S4.1", r"Every rational matrix $A$ of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with exactly $a$ ones.",
              r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization",
              frm=["gaussian-elimination", "linear-algebra-basics", "permutations-and-permutation-matrices"],
              page="lower-triangular-factorization"),
        show("S4.2",
             r"The address map $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ is performed with exactly $\operatorname{rank}(A)$ interchanges of $b$-digit fields plus $O(V)$ further work.",
             "Factor $A=E_1\\Pi E_2$, perform the triangular factors by controlled shifts, and turn each one of $\\Pi$ into a single interchange.",
             ("Lower triangular changes of coordinates update each later field from earlier ones, which is the direction in which controlled shifts run in linear time.",
              "explicit",
              r"Lower triangular changes of coordinates can be performed entirely in this direction."),
             [
                 infer("S4.2.1", r"A lower triangular transformation of the fields $H$ or $D$ costs $O(V)$ by updating coordinates in descending order.",
                       r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
                 infer("S4.2.2", r"For $A=E_1\Pi E_2$ transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$, and undo the transformations.",
                       r"For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,"),
                 infer("S4.2.3", r"The sequence $D_j\leftarrow D_j+H_i$, swap, $D_j\leftarrow H_i-D_j$ yields $(h+d,d)$ with just one interchange.",
                       r"On an initial pair $(h,d)$ this sequence yields $(h+d,d)$."),
             ],
             frm=["lower-triangular-factorization", "controlled-shifts", "modular-arithmetic", "extended-euclidean-algorithm", "linear-algebra-basics"],
             page="matrix-shear-cost"),
        show("S4.3",
             r"Two chunks of $e=m^k$ radix-$q$ digits are interchanged in $O(Ve^\tau)$ time: split rows into $W$ role streams, run the bit network with each edge shear done by recursive interchanges of chunks of $e/m$ digits, and finish with three shears.",
             "Run the bit network on cyclic row splits with frames given by address shears, so the network's endpoint operator is the shear on every row, then complete the interchange by two linear shears around it.",
             ("The network is the only place a shear that costs fewer than $m$ times a smaller interchange can come from; an interchange is a shear between two cheap shears.",
              "reconstructed", None),
             [
                 infer("S4.3.1", r"Splitting whole rows cyclically into $W$ role streams gives streams of the same shape, each of volume $V/W$.",
                       r"Split whole rows cyclically into $W$ role streams within each prefix"),
                 infer("S4.3.2", r"Running the network with frames $\Phi_M$ and merging the rows back applies $H\leftarrow H+D$ to every original row, including scratch rows with arbitrary values.",
                       r"The result is $H\leftarrow H+D$ on every original row, including rows assigned to scratch roles, whose initial values were arbitrary."),
                 infer("S4.3.3", r"The interchange is $D\leftarrow D-H$, then $H\leftarrow H+D$, then $D\leftarrow H-D$, and only the middle shear uses the circuit.",
                       r"Only the middle shear uses the circuit."),
                 infer("S4.3.4", r"The number of recursive calls is the sum of the edge ranks, exactly $s$, each on a stream of volume $V/W$.",
                       r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
                 infer("S4.3.5", r"The per-volume cost obeys $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.",
                       r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."),
                 infer("S4.3.6", r"For $s/W<m^\tau$ the geometric sum gives $F_k=O(e^\tau)$.",
                       r"Hence $F_k=O(e^\tau)$."),
                 infer("S4.3.7", r"Scheduling the recursive calls depth-first on fixed tapes by parking inactive streams on a stack costs only an additional $O(V)$ at each node.",
                       r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
             ],
             frm=["rank-saving-recurrence", "bit-network-interface", "matrix-shear-cost", "gate-network-frames", "elementary-streams", "controlled-shifts", "array-layout"],
             page="power-width-interchange"),
        show("S4.4",
             r"An interchange of chunks of arbitrary width $u$ in an arbitrary array costs $O(Vu^\tau)$: supply the rows from a few high digits, pad, and write the width in base $m$ as pieces of power width.",
             "Exchange a few high digits one pair at a time to create the row field, then split the remaining width into $a_j$ pieces of width $m^j$ and apply the power-width interchange to each.",
             ("The power-width interchange needs a row count divisible by $W^k$, and a general array can supply that many rows from its own high digits.",
              "explicit",
              r"Rows for a general array can be supplied by a few of its own high digits."),
             [
                 infer("S4.4.1", r"The corresponding high digits of the two chunks are interchanged one pair at a time, which creates a row field of range at least $W^k$ at cost $O(V\log u)$.",
                       r"Interchange the corresponding high digits one pair at a time."),
                 infer("S4.4.2", r"The remaining width is written in base $m$ and each corresponding pair of pieces of width $m^j$ is interchanged by the power-width procedure.",
                       r"Write the remaining width in base $m$:"),
                 infer("S4.4.3", r"The piece costs sum geometrically to $O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)$.",
                       r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)."),
                 infer("S4.4.4", r"Padding to the radix $q$ costs a constant factor and gives $O(Vu^\tau)$ for binary chunks of width $u$.",
                       r"Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$."),
             ],
             frm=["power-width-interchange", "positional-notation-in-any-radix-and-mixed-radix", "floor-ceiling-and-rounding", "elementary-streams"]),
    ],
    frm=["rank-saving-recurrence", "bit-network-interface", "elementary-streams", "array-layout"],
    page="chunk-interchange",
    salient="The final effect is an exact permutation of the data, yet the intermediate steps compute XOR combinations of the data, and the result is exact for arbitrary initial contents of the scratch roles.",
)

S5 = show(
    "S5",
    r"One $H_0$ butterfly applied at the same bit offset in $D\le d$ address chunks at once is computed exactly, with a single final truncation, in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$.",
    "Compute the layer of the auxiliary kernel $C=H\\mathsf SH$ through the complex rank-saving network, recursing on $1/m$ of the axes, do the binary changes of basis by packed selected-bit addition, and convert to $H_0$ by the identity $H_0=b\\mathsf SC\\mathsf S$.",
    ("The phase frames of the complex network express a tensor product of $C$ on many bits through smaller groups of bits separated by binary changes of basis, which can be done by moving whole address chunks.",
     "explicit",
     r"Its phase frames express a $C$ tensor product using smaller groups of selected bits, separated by binary changes of basis."),
    [
        infer("S5.1", r"An edge's frame change is $\mathcal P_M\big(\prod_j C_{e_j}^{\epsilon_j}\big)\mathcal P_M^{-1}$: apply a binary change of basis to each column, one child call per residual vector on the $f$ axes of a slot, and change back.",
              r"To implement \eqref{eq:phase-edge-coordinate} on the group, first apply $\mathcal P_M^{-1}$ separately to each column."),
        infer("S5.2", r"Summing the residual dimensions gives exactly $s$ child calls, each on the $f=e/m$ axes of one slot.",
              r"Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
        infer("S5.3", r"The network therefore gives $C^{\otimes e}$ on every role, including roles whose scratch values were arbitrary.",
              r"Proposition~\ref{prop:complex-motif-interface} therefore gives $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary."),
        infer("S5.4", r"The normalized layer is recovered from the $C$ layer by $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, with exact Gaussian dyadic phases.",
              r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D."),
        show("S5.5",
             r"An XOR of the same bit position in $f$ chunks of one address range into another is done together by a constant number of cyclic shifts of whole chunk ranges, followed by a deterministic repair of the small explicitly identified set of exceptional addresses.",
             "Pack the $f$ segment pairs into one long integer pair, apply eight conditional rotations that flip the parity of one integer and restore the other, and repair the addresses whose guard values leave the safe range.",
             ("Cyclic shifts of whole chunk ranges move all $f$ segments at once, and the only trouble is carries between segments, which happen only at an explicitly bounded set of addresses.",
              "explicit",
              r"The construction first uses a constant number of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of addresses."),
             [
                 infer("S5.5.1", r"Eight conditional additions flip the parity of $u$ exactly when the control is set and restore the auxiliary integer $w$.",
                       r"Thus the parity of $u$ is flipped precisely when $c=1$, both quotients under division by two are preserved, and the arbitrary auxiliary integer $w$ is restored."),
                 infer("S5.5.2", r"Each line applied simultaneously to all segment pairs is a single cyclic shift of a whole chunk range by an offset that does not depend on the target.",
                       r"Physically, a line updating $y$ by sign $\varepsilon$ and testing parity $b$ of $z$ is the single cyclic shift"),
                 infer("S5.5.3", r"The packed shifts agree with the ideal XORs except on the set $\mathcal B$ of addresses where some guard value leaves the safe interval.",
                       r"Let $\mathcal B$ consist of the addresses for which at least one used guard value, in either $y$ or $z$, fails"),
                 infer("S5.5.4", r"A union bound over the $2(f-1)$ guards makes the bad set a fraction at most $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$ of all addresses.",
                       r"the union bound over the $2(f-1)$ guards gives"),
                 infer("S5.5.5", r"The remaining correction $T_0S_0^{-1}$ fixes the good addresses and only permutes the bad set, so it can be repaired by sorting the small exceptional stream.",
                       r"Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$."),
             ],
             frm=["chunk-interchange", "controlled-shifts", "elementary-streams", "array-layout", "binary-integers"],
             page="packed-selected-bit-addition"),
        show("S5.6",
             r"The cost per unit volume of the $C$ layer obeys $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ and unrolls to $O(d^{\lambda'})$ for the whole layer.",
             "Stop the recursion when $e<d^{\\beta}$, sum the internal-node overheads as a geometric series, bound the leaves, and treat the base-$m$ digits of the number of chunks as separate pieces.",
             ("Each child sits on a stream of volume $1/W$ of its parent's, so dividing by the volume leaves the factor $s/W$, and the binary basis changes at a node add only $O((eK)^\\tau+1)$.",
              "recoverable", None),
             [
                 infer("S5.6.1", r"The phase construction supplies one recursive call on a slot for each vector of an edge residual basis, hence exactly $s$ calls per invocation.",
                       r"The phase construction supplies one recursive call on a slot for each vector in an edge residual basis, hence exactly \(s\) calls in one invocation of the network."),
                 infer("S5.6.2", r"Splitting complete rows among the $W$ roles gives each recursive edge call a stream of exactly $1/W$ of its parent's logical volume.",
                       r"Each recursive edge call acts on one role stream with volume exactly \(1/W\) of its parent's logical volume."),
                 infer("S5.6.3", r"The normalized cost satisfies $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ with $F(e)=O(e)$ below the cutoff.",
                       r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
                 infer("S5.6.4", r"At an internal node the overhead is $O(e^{\lambda})$, so the internal costs sum to $O(e^\lambda)$.",
                       r"The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\)."),
                 infer("S5.6.5", r"Adding the costs of the base-$m$ pieces and the row preprocessing gives $O(d^{\lambda'})$ for any fixed $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$.",
                       r"Adding their costs and the row preprocessing gives"),
             ],
             frm=["rank-saving-recurrence", "phase-interface", "packed-selected-bit-addition", "chunk-interchange", "divide-and-conquer-recurrences"]),
        infer("S5.7", r"Intermediate coefficients are exact Gaussian dyadics whose denominator and magnitude growth is bounded by $\lceil C_0d^{C_1}\rceil=o(p)$ bits, so the whole layer is evaluated exactly before the single truncation $Q_p$.",
              r"The guard-width calculation above bounds both denominator and magnitude growth by $\lceil C_0d^{C_1}\rceil$."),
        infer("S5.8", r"Every row of $H_0^{\otimes D}$ has absolute row sum one, so the layer maps the disk to the disk and a single truncation adds an error below $\sqrt2\,2^{-p}$.",
              r"Finally, every row of $\mathcal H$ has absolute row sum one."),
    ],
    frm=["two-point-butterfly", "phase-interface", "rank-saving-recurrence", "chunk-interchange", "packed-selected-bit-addition", "fixed-point-numerics", "elementary-streams", "dyadic-rationals-and-binary-fractions", "complex-numbers"],
    page="simultaneous-butterfly-layer",
    salient="Applying $D$ butterflies at once costs only $O(Vd^{\\lambda'})$ with $\\lambda'<1$, sublinear in the number $D\\le d$ of axes, whereas separate butterflies would need $D$ whole-array passes.",
)

S6 = show(
    "S6",
    r"A positional permutation moves selected bits of the $d-1$ axes to a common offset in $K$-bit chunks so that each transform round is one simultaneous layer, giving a forward and an opposite synthetic transform each costing $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.",
    "Run radix-two decimation-in-frequency rounds over the negacyclic ring, group the rounds of all axes into one parallel butterfly plus one monomial, and lay out the bits so that every round is a simultaneous layer.",
    ("Each round pairs entries differing in one address bit on every axis, and the simultaneous layer applies only when those bits sit at a common offset of consecutive chunks.",
     "explicit",
     r"To apply Proposition~\ref{prop:simultaneous-layer} in a transform round, we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks."),
    [
        infer("S6.1", r"With $\omega_t=y^{2r/t}$ the transforms satisfy $F_t^+F_t^-=t^{-1}I$ although the ring has zero divisors, because shifting $k$ multiplies the sum by $y^{rj_0}=-1$.",
              r"Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies their sum by",
              frm=["negacyclic-ring", "discrete-fourier-transform", "multidimensional-transform"],
              page="synthetic-transform"),
        infer("S6.2", r"Decimation-in-frequency rounds leave the entry of frequency $j$ in the slot with the bit-reversed address, and the opposite transform consumes that order.",
              r"After all $a$ rounds, the named slots from high to low therefore contain the frequency bits from low to high.",
              frm=["synthetic-transform", "two-point-butterfly", "discrete-fourier-transform"],
              page="butterfly-recursion"),
        infer("S6.3", r"The steps of all axes in one round group into a parallel butterfly $\mathcal H$ followed by one recordwise monomial multiplication $J_E$.",
              r"Consequently the individual axis steps may be grouped as a parallel butterfly $\mathcal H$, followed by one recordwise monomial operation"),
        infer("S6.4", r"Moving the at most $D(b+1)=O(dK)$ listed bit slots to a prefix costs $O(TpdK)$.",
              r"listed slots, so the moves cost $O(TpdK)$."),
        infer("S6.5", r"At most $Dq-1$ exchanges of width-$K$ chunks bring the remaining bits into consecutive chunks of equal offset, costing $O(Tp\cdot pK^{\tau-1})$.",
              r"This uses at most $Dq-1$ exchanges of width-$K$ address chunks, even when the chunks are nonadjacent."),
        infer("S6.6", r"Each simultaneous round applies with cost $O(Tpd^{\lambda'})$, so the at most $\ell$ rounds cost $O(Tp\ell d^{\lambda'})$ in total.",
              r"The simultaneous-layer procedure therefore applies at cost $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total."),
        infer("S6.7", r"The at most $b+1\le K$ rounds on prefix slots are done by individual kernels, giving cost $O(TpdK)$.",
              r"There are at most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$."),
        infer("S6.8", r"Contractions and one truncation per round give total error below $\sqrt2\,\ell\,2^{-p}$ and keep the disk grid.",
              r"Starting with zero error, at most $\ell$ rounds therefore give the claimed error and disk bounds."),
        infer("S6.9", r"The forward entry of frequency address $j$ is stored at $L(Bj)$, and the opposite procedure consumes that retained order.",
              r"In particular, the forward entry with frequency address $j$ is stored at $L(Bj)$."),
    ],
    frm=["simultaneous-butterfly-layer", "chunk-interchange", "negacyclic-ring", "multidimensional-transform", "two-point-butterfly", "fixed-point-numerics", "elementary-streams"],
    page="transform-layout",
)

S7 = show(
    "S7",
    r"Normalized convolution over the negacyclic ring is computed by two forward synthetic transforms, pointwise polynomial products in the retained frequency order, and the opposite transform, with error below $\sqrt2\,M(3\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.",
    "Transform both operands keeping the layout $LB$, multiply the records pointwise in that order using signed packing and the $O(N\\log N)$ multiplier, and apply the opposite transform to the retained order.",
    ("Pointwise multiplication commutes with the same record permutation applied to both operands, so the frequency order never has to be restored between the transforms.",
     "explicit",
     r"Pointwise multiplication commutes with applying the same record permutation $LB$ to both operands. We may therefore multiply the forward outputs in their retained order and pass that order directly to the opposite procedure."),
    [
        show("S7.1",
             r"A product of two disk-grid polynomials is computed exactly by evaluating their integer parts at the base $2^{4p}$, multiplying the resulting integers with the $O(N\log N)$ multiplier, reading centered coefficients back out, and wrapping modulo $y^r+1$, in time $O(rp\log(rp))$.",
             "Use Kronecker substitution with signs: pack each coefficient list into one integer, multiply, and extract each product coefficient as the centered residue modulo the base.",
             ("The established integer multiplier is the only fast product available on the fixed-tape model, so polynomial products are turned into integer products.",
              "explicit",
              r"To multiply the polynomial records, we use the fixed-tape integer multiplier of Harvey and van der Hoeven"),
             [
                 infer("S7.1.1", r"The four products of the absolute values of the packed integers are computed with the established multiplier and their signs restored.",
                       r"Multiply the four pairs of absolute values using the established multiplier and restore each product's sign."),
                 infer("S7.1.2", r"Every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<B_0/2$, so coefficients cannot collide at base $B_0=2^{4p}$.",
                       r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
                 infer("S7.1.3", r"Reading blocks with a bounded carry and centering modulo $B_0$ recovers each coefficient $h_j$ exactly.",
                       r"Thus $\widehat h_j=h_j$."),
                 infer("S7.1.4", r"The product is reduced modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$.",
                       r"To reduce them modulo $y^r+1$, subtract the coefficient at $j+r$ from the one at $j$ for $0\leq j<r$,"),
                 infer("S7.1.5", r"Four exact integer products dominate all the linear packing, extraction and truncation costs.",
                       r"Four exact integer products dominate the linear packing, extraction, combination, wrapping, and truncation costs."),
             ],
             frm=["nlogn-multiplier", "negacyclic-ring", "fixed-point-numerics", "binary-integers"],
             page="signed-packing"),
        infer("S7.2", r"Perform both forward transforms and keep their common $LB$ order.",
              r"Perform both forward transforms and retain their common $LB$ order."),
        infer("S7.3", r"The exact scaling by $M$ of the opposite transform of the pointwise products is the normalized convolution $\mathcal M_r(f,g)=(f*g)/(rM)$.",
              r"The displayed normalization identity identifies its exact scaling by $M$ with $\mathcal M_r(f,g)$."),
        infer("S7.4", r"The two forward errors, the product truncation and the opposite transform give total error $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$.",
              r"The final exact multiplication by $M$ therefore gives error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed."),
        infer("S7.5", r"There are $M=T/r$ pointwise polynomial products, together costing $O(Tp\log(rp))$ beside the three transforms.",
              r"There are $M=T/r$ pointwise polynomial products."),
    ],
    frm=["transform-layout", "signed-packing", "negacyclic-ring", "cyclic-convolution", "multidimensional-transform", "fixed-point-numerics"],
    page="ring-convolution",
)

S8 = show(
    "S8",
    r"The Fourier transform of coprime source lengths $s_i$ is expressed, with its two coordinate permutations left inside the identity, through transforms on the padded power-of-two box of lengths $t_i$, using linewise Gaussian maps, a Bluestein chirp convolution, and a cancellation of the retained source permutation across a convolution.",
    "Apply Gaussian resampling line by line along each axis of the padded box, rewrite the middle power-of-two transform as a convolution with a chirp, and show that the leftover permutation cancels in a product.",
    ("The usual resampling implementation sorts twice on each coordinate; keeping both permutations in the transform formula avoids those full sorts.",
     "explicit",
     r"Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and compute that formula directly."),
    [
        show("S8.1",
             r"For coprime $s_i<t_i$ with $t_i/s_i-1>p/\alpha^4$ there are linear contractions $A$ and $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computable with error below $p^2$ in time $O(t_ip^{3/2+\delta}\alpha)$.",
             "Pass between lengths $s_i$ and $t_i$ with Gaussian-weighted sums satisfying an exact identity, and invert the near-identity correction by a Neumann series.",
             ("The lengths needed for the product are pairwise coprime whereas the synthetic transforms need powers of two, and Gaussian resampling converts one shape to the other.",
              "explicit",
              r"The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two. Gaussian resampling connects these two shapes."),
             [
                 infer("S8.1.1", r"An exact Gaussian identity $\mathsf T P_sF_s=P_tF_t\mathsf S$ holds, and the correction $N=C\mathsf T\mathsf D$ satisfies $\|N-I\|<2^{-\alpha^2\theta}$.",
                       r"The exact Gaussian identity and inverse estimate proved in"),
                 infer("S8.1.2", r"Since $\|N-I\|<1/2$, $N$ is invertible by the Neumann series.",
                       r"Thus $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series."),
                 infer("S8.1.3", r"Setting $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$ gives two contractions.",
                       r"Because $\|C\|=1$, both are contractions."),
                 infer("S8.1.4", r"The normalizations multiply to $2^{-2\alpha^2}$, which gives the identity $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ with both permutations left inside.",
                       r"which is \eqref{eq:no-sort-one-dimensional}."),
                 infer("S8.1.5", r"The numerical algorithms for $A$ and $B_0$ have error below $p^2$ and add up to time $O(t_ip^{3/2+\delta}\alpha)$.",
                       r"$4+3p^2/4<p^2$, respectively. The costs add to the claimed bound."),
             ],
             frm=["discrete-fourier-transform", "fixed-point-numerics", "nlogn-multiplier", "linear-algebra-basics", "convergent-series-and-the-geometric-series"],
             page="gaussian-resampling",
             adds=[
                 B("A", "Gaussian expansion", "The contraction from length $s_i$ to length $t_i$ obtained from the Gaussian-weighted map $\\mathsf S$."),
                 B("B_0", "Gaussian compression", "The contraction from length $t_i$ back to length $s_i$ built from the inverse of the near-identity correction."),
             ]),
        show("S8.2",
             r"The one-dimensional resampling maps are applied line by line along each axis of a zero-padded power-of-two box, with axes exposed by chunk interchanges, giving error below $dp^2$ and cost $O(dTp^{3/2+\delta}\alpha)$ plus $O(Tp\,d^2(1+\ell^\tau))$ for movement.",
             "Tensor the one-dimensional identity and apply the maps to one coordinate line at a time, exposing each axis as the innermost field by adjacent chunk interchanges.",
             ("A tensor product of maps acts on one axis at a time, so only the line being processed has to be contiguous, and the chunk interchange supplies that movement.",
              "explicit",
              r"For the tensor product, apply the one-dimensional maps to one coordinate line at a time. The chunk-swap algorithm supplies the movement of the physical axis fields"),
             [
                 infer("S8.2.1", r"Tensoring the one-dimensional identity gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$.",
                       r"Tensoring \eqref{eq:no-sort-one-dimensional} proves"),
                 infer("S8.2.2", r"Composing the $d$ axis maps gives error less than $dp^2$.",
                       r"Composing the $d$ axis maps gives error less than $dp^2$."),
                 infer("S8.2.3", r"At most $T/t_i$ lines invoke the one-dimensional algorithm on axis $i$, so the line costs sum to $O(dTp^{3/2+\delta}\alpha)$.",
                       r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$,"),
                 infer("S8.2.4", r"Exposing and restoring each axis takes $O(d)$ adjacent interchanges, each costing $O(Tp(1+\ell^\tau))$.",
                       r"Each adjacent interchange therefore costs $O(Tp(1+\ell^\tau))$."),
             ],
             frm=["gaussian-resampling", "chunk-interchange", "elementary-streams", "fixed-point-numerics", "multidimensional-transform"],
             page="tensor-resampling-box"),
        infer("S8.3", r"A Fourier transform including its target permutation equals a pointwise chirp phase, a cyclic convolution with the chirp, and another pointwise chirp phase: $QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$.",
              r"This is precisely the coefficient in $QF_{\boldsymbol t}$, because $Q$ reads frequency $(-s_i j_i)_i$ from the negative-sign transform.",
              frm=["discrete-fourier-transform", "cyclic-convolution", "multidimensional-transform"],
              page="bluestein-chirp"),
        show("S8.4",
             r"The coordinate permutation $R$ left inside the resampled transform cancels across two forward transforms, their pointwise product and the opposite transform: $RF_{\boldsymbol s}^+[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=u*v/S^2$.",
             "Show that $R$ is a dilation by a unit modulo each $s_i$, so that $F^+R=R^{-1}F^+$ and $RF^+R=F^+$, then apply the convolution theorem.",
             ("Because pointwise products commute with coordinate permutations, the permutation sitting between the transforms can be moved through them and absorbed by its inverse.",
              "recoverable", None),
             [
                 infer("S8.4.1", r"Each $t_i$ is a unit modulo $s_i$, so tensoring $F_q^+R_c=R_c^{-1}F_q^+$ gives $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.",
                       r"Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives"),
                 infer("S8.4.2", r"The pointwise product is passed through $R$, and the normalized convolution rule applies to the remaining transforms.",
                       r"The normalized convolution rule is"),
                 infer("S8.4.3", r"The two normalizations give $F^+_{\boldsymbol s}(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=u*v/S^2$.",
                       r"proving \eqref{eq:source-permutation-cancel}."),
             ],
             frm=["discrete-fourier-transform", "multidimensional-transform", "gaussian-resampling", "cyclic-convolution", "modular-arithmetic", "permutations-and-permutation-matrices"],
             page="permutation-cancellation",
             salient="The permutation $R$ appears twice and yet leaves no trace in the final convolution $u*v/S^2$: the two occurrences cancel because $R$ is a dilation by a unit modulo each $s_i$, which satisfies $RF^+R=F^+$."),
    ],
    frm=["discrete-fourier-transform", "multidimensional-transform", "fixed-point-numerics", "nlogn-multiplier"],
)

S9 = show(
    "S9",
    r"Choosing compatible parameters, the radix-digit convolution is mapped to prime axes, transformed, multiplied pointwise, inverted, rescaled, rounded and carried to give the exact binary product in time $O(n(\lg n)^{1-\kappa})$.",
    "Fix the parameters, place the digits on a product of prime cyclic axes, run the source transform on each operand, multiply and invert, then bound the error to round exactly and add up the costs.",
    ("The earlier procedures must be placed inside the multiplication reduction, with every change of representation accounted for.",
     "explicit",
     r"The remaining proof places these procedures inside the multiplication reduction and accounts for every change of representation."),
    [
        infer("S9.0", r"The exponents are fixed rationally, for instance $\tau=\sigma=1-2^{-50}$, $\lambda=1-2^{-52}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $\epsilon=2^{-75}$, $\kappa=2^{-182}$, and satisfy every layer condition with room to spare.",
              r"These constants are deliberately conservative; no optimization is claimed."),
        show("S9.1",
             r"From $n$ set $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, box size $T\approx n/b$ and axis lengths $t_i\in\{r/2,r\}$ with $r=2^\ell$, so that $Tp=\Theta(n)$, $r$ exceeds every fixed power of $p$, and the radix-$2^b$ digit product has no wraparound modulo $x^S-1$.",
             "Choose the number of axes polynomially small in the precision so that the polynomial length $r$ is superpolynomial in $p$ while the box still holds $\\Theta(n/b)$ digits.",
             ("A record of length $r$ must pay for polynomial work on its address, and $K/\\log p$ must grow so that the exceptional set in a packed address change is small enough to repair by sorting.",
              "explicit",
              r"The polynomial length $r$ grows faster than every fixed power of $p$, so a scan of a record pays for polynomial work on its address."),
             [
                 infer("S9.1.1", r"The digit size, precision, number of axes and chunk width are $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$.",
                       r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,"),
                 infer("S9.1.2", r"The box size $T$ is a power of two in $[4n/b,8n/b)$ and $r=2^{\lceil(\log_2T)/d\rceil}$, with the axis lengths $t_i$ equal to $r/2$ or $r$ and product $T$.",
                       r"Take the power of two $T$ in $[4n/b,8n/b)$, and let"),
                 infer("S9.1.3", r"These sizes give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$.",
                       r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),"),
                 show("S9.1.4",
                      r"Distinct odd primes $s_i$ in $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ are found by trial division, so their product $S$ fills at least half the padded box while each ratio $t_i/s_i$ leaves the separation resampling needs.",
                      "Count primes in a window of relative width $\\eta=1/(4d)$ below each power of two with an explicit prime-density bound, then multiply the lower bounds and check the Gaussian hypothesis.",
                      ("The product of the primes must occupy a fixed fraction of the padded box, while each ratio $t_i/s_i$ must leave enough separation for resampling.",
                       "explicit",
                       r"their product must occupy a fixed fraction of the padded box, while each ratio $t_i/s_i$ must leave enough separation for resampling."),
                      [
                          infer("S9.1.4.1", r"Each window contains at least $\eta x/(2\log x)$ primes, which exceeds $d$ for large $n$, so distinct primes can be chosen.",
                                r"contains at least $\eta x/(2\log x)$ primes."),
                          infer("S9.1.4.2", r"The lower bounds on the $s_i$ give $S/T>1/2$, hence $T/2<S<T$.",
                                r"Together with $s_i<t_i$, this gives $T/2<S<T$."),
                          infer("S9.1.4.3", r"The upper bound on $s_i$ gives $\alpha^4\theta_i>p$, the separation the Gaussian resampling lemma requires.",
                                r"\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p."),
                          infer("S9.1.4.4", r"The machine finds the primes deterministically by scanning the intervals with trial division in $n^{o(1)}$ time.",
                                r"The machine finds these primes by scanning the two intervals"),
                      ],
                      frm=["prime-numbers-coprimality-and-trial-division", "gaussian-resampling", "exponential-and-logarithm-functions", "floor-ceiling-and-rounding"],
                      page="prime-lengths"),
                 infer("S9.1.5", r"The product of the two digit polynomials has degree below $S$, so cyclic convolution modulo $x^S-1$ has no wraparound and each coefficient is below $2^{3b}$.",
                       r"Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
                       frm=["radix-digit-convolution", "positional-notation-in-any-radix-and-mixed-radix", "polynomials"]),
             ],
             frm=["transform-layout", "gaussian-resampling", "fixed-point-numerics", "exponential-and-logarithm-functions", "floor-ceiling-and-rounding"],
             page="size-parameters",
             adds=[]),
        show("S9.2",
             r"A cyclic convolution of length $S=s_1\cdots s_d$ with pairwise coprime $s_i$ becomes a convolution on the product of cyclic axes of lengths $s_i$ via $x\mapsto\prod_ix_i^{\mu_i}$, implemented by triangular controlled shifts and axis moves in time $O(Tp\,d^2(1+\ell^\tau))$.",
             "Use the Chinese remainder theorem with coordinate powers $\\mu_i=P_i^{-1}\\bmod s_i$ chosen so that the change of order is a sequence of controlled cyclic shifts, each target depending only on earlier axes.",
             ("The map uses the Chinese-remainder split of Agarwal and Cooley, with coordinate powers that make the change of order a sequence of controlled cyclic shifts.",
              "explicit",
              r"The following map uses that algebraic split, with coordinate powers that make the change of order a sequence of controlled cyclic shifts."),
             [
                 infer("S9.2.1", r"The monomial map $\Phi$ is an algebra isomorphism and therefore preserves cyclic convolution.",
                       r"Hence $\Phi$ is an isomorphism and preserves cyclic convolution."),
                 infer("S9.2.2", r"Updating the targets in the order $i=d,d-1,\ldots,1$ by $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$ uses only unchanged lower-index controls.",
                       r"Update the targets in the order $i=d,d-1,\ldots,1$ using \eqref{eq:triangular-crt}."),
                 infer("S9.2.3", r"Each triangular update is a prefix-controlled cyclic shift of the valid target interval and costs linear time.",
                       r"Each triangular update is a prefix-controlled cyclic shift."),
                 infer("S9.2.4", r"The reordering of axes needs $O(d^2)$ interchanges, so the map, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$.",
                       r"Therefore the map $\Phi$, its inverse, and their padding operations cost"),
             ],
             frm=["chunk-interchange", "controlled-shifts", "prime-lengths", "size-parameters", "cyclic-convolution", "modular-arithmetic", "extended-euclidean-algorithm", "positional-notation-in-any-radix-and-mixed-radix"],
             page="crt-prime-axes"),
        show("S9.3",
             r"Multiplying coefficient $k$ by $\zeta^k$ with $\zeta=e^{\pi i/r}$ maps $\mathbb C[x]/(x^r-1)$ isomorphically onto the polynomial ring modulo $y^r+1$, so cyclic convolution is computed over the ring and untwisted.",
             "Send $x_d$ to $\\zeta y$, which is well defined because $(\\zeta y)^r=1$, check that the negative wrap of $y^r=-1$ is cancelled by the twist, and extend line by line.",
             ("The power-of-two complex convolution needed in the chirp identity is obtained from the synthetic convolution by a coefficient twist.",
              "explicit",
              r"The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist."),
             [
                 infer("S9.3.1", r"The map $x_d\mapsto\zeta y$ is well defined because $(\zeta y)^r=(-1)(-1)=1$.",
                       r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."),
                 infer("S9.3.2", r"A wrapped product term picks up the factor $\zeta^r(-1)=1$, so untwisting recovers the cyclic coefficient with the correct sign.",
                       r"Untwisting therefore recovers the cyclic coefficient with the correct sign."),
                 infer("S9.3.3", r"The twist and untwist are isometries, so the normalized complex cyclic convolution $\mathcal M_{\mathbb C}(f,g)=f*g/T$ is a bilinear contraction.",
                       r"The maps $D_\pm$ and $\iota^{\pm1}$ are isometries, so $\mathcal M_{\mathbb C}$ is also a"),
             ],
             frm=["negacyclic-ring", "cyclic-convolution", "ring-convolution", "complex-numbers"],
             page="coefficient-twist"),
        show("S9.4",
             r"The computed source transform $\widetilde{\mathscr F}$ applies the linewise Gaussian map $A$, the chirp transform done by complex convolution through the phase twist, the linewise map $B_0$ and an exact $2^\gamma$ rescale, and approximates $RF_{\boldsymbol s}$.",
             "Compose the Gaussian maps around the Bluestein chirp transform of the padded box.",
             ("The middle factor $QF_{\\boldsymbol t}$ of the resampling identity can be computed from one cyclic convolution and two pointwise phase multiplications.",
              "explicit",
              r"The factor $QF_{\boldsymbol t}$ in \eqref{eq:no-sort-tensor} can be computed from a cyclic convolution and two pointwise phase multiplications."),
             [
                 infer("S9.4.1", r"Replacing the approximations by exact phases and exact convolution gives $\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)=QF_{\boldsymbol t}x$.",
                       r"Replacing the approximations by exact phases and exact convolution gives"),
                 infer("S9.4.2", r"The source transform applies the linewise approximation of $A$, the computed chirp transform, the linewise approximation of $B_0$, and an exact multiplication by $2^\gamma$.",
                       r"apply the linewise approximation to $\mathcal A$, apply the computed chirp transform $\widetilde{\mathscr C}$, apply the linewise approximation to $\mathcal B_0$, and multiply the grid numerators exactly by $2^\gamma$."),
                 infer("S9.4.3", r"Its exact counterpart is $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.",
                       r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A"),
                 infer("S9.4.4", r"The opposite-sign procedure is obtained by conjugating input and output.",
                       r"Define the opposite-sign procedure by"),
             ],
             frm=["bluestein-chirp", "gaussian-resampling", "tensor-resampling-box", "coefficient-twist", "ring-convolution", "fixed-point-numerics"],
             page="source-transform"),
        show("S9.5",
             r"Split the operands into radix digits, map them by $\Phi$ to the prime axes, apply the source transform to each, multiply pointwise, apply the opposite transform, rescale by $S$ and $2^{2b+4}$, round to integers, undo $\Phi$ and propagate carries.",
             "Do the digit convolution in the source frequency domain and let the retained permutation cancel between the two forward transforms and the opposite transform.",
             ("The source permutation retained during resampling cancels across the two forward source transforms, their pointwise product and the opposite-sign transform, so it never has to be executed.",
              "explicit",
              r"Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform."),
             [
                 infer("S9.5.1", r"Each operand is read backward in groups of $b$ bits to give radix-$2^b$ digits, placed as grid values with zero padding.",
                       r"Read each stored operand backward from its least significant end in groups of $b$ bits."),
                 infer("S9.5.2", r"The coefficient-address map $\Phi$ gives the source arrays $u,v$ with coefficients of norm below $1/4$.",
                       r"Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$."),
                 infer("S9.5.3", r"The forward source transforms $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$ are computed.",
                       r"Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$."),
                 infer("S9.5.4", r"Corresponding coefficients are multiplied exactly and truncated to the grid, giving the array $z$.",
                       r"Multiply corresponding complex coefficients exactly and truncate"),
                 infer("S9.5.5", r"The opposite transform of $z$ is computed and its numerators multiplied exactly by $S$.",
                       r"Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$,"),
                 infer("S9.5.6", r"A further exact scale by $2^{2b+4}S$, rounding to integers and applying $\Phi^{-1}$ restores the integer coefficients in ordinary order.",
                       r"Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$,"),
                 infer("S9.5.7", r"Radix-$2^b$ carries are propagated in increasing coefficient order to produce the $2n$ output bits.",
                       r"Propagate radix-$2^b$ carries in increasing coefficient order."),
                 infer("S9.5.8", r"The two scales by $S$ undo different normalizations: after the three transforms the result is $(u*v)/S^2$, after the first scale $(u*v)/S$.",
                       r"The two occurrences of $S$ in this algorithm undo different normalizations."),
             ],
             frm=["permutation-cancellation", "source-transform", "crt-prime-axes", "size-parameters", "radix-digit-convolution", "discrete-fourier-transform"],
             page="multiplication-algorithm"),
        show("S9.6",
             r"Disk-margin and error bookkeeping shows the error in each recovered coefficient is below $1/2$, so rounding gives the exact integer convolution coefficients and carries give the exact binary product.",
             "Track norm bounds and additive errors through every computed step, using that contractions pass errors through unchanged and errors of composed steps add, then compare the final error with $1/2$.",
             ("A linear contraction does not enlarge an input error, so the errors of composed steps simply add and can be tallied step by step.",
              "explicit",
              r"A linear contraction propagates an input error without increasing it."),
             [
                 infer("S9.6.1", r"Every computed ring convolution output is a disk grid array of norm below $.701$, so no clipping occurs.",
                       r"Its computed grid output consequently has norm less than $.7+5TLh_p<.701$ for large $n$."),
                 infer("S9.6.2", r"The computed chirp transform differs from $QF_{\boldsymbol t}x$ by less than $8TLh_p$.",
                       r"(6TL+2+4+4)h_p<8TLh_p."),
                 infer("S9.6.3", r"The source transform has error below $E_sh_p$ with $E_s=9\,2^\gamma TL$, and its output stays in the disk.",
                       r"E_s=9\,2^\gamma TL,"),
                 infer("S9.6.4", r"The pointwise product satisfies $\|z-U\cdot V_1\|<(2E_s+2)h_p$.",
                       r"Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$."),
                 infer("S9.6.5", r"After the first scale by $S$ the error is below $E_wh_p$ with $E_w=S(3E_s+2)<28\,2^\gamma T^2L$.",
                       r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
                 infer("S9.6.6", r"After the second scale the absolute error is below $448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<1/2$.",
                       r"\le448b\,2^{-3b/4}<\frac12."),
                 infer("S9.6.7", r"Since the true coefficients are integers and the error is below $1/2$, the nearest integer is the unique correct coefficient.",
                       r"The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient."),
                 infer("S9.6.8", r"The carries obey $0\le k_j\le q(Q_0-1)<Q_0^2$, so the carry propagation yields exactly the digits of the product.",
                       r"The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$."),
             ],
             frm=["multiplication-algorithm", "source-transform", "fixed-point-numerics", "ring-convolution", "permutation-cancellation", "radix-digit-convolution", "floor-ceiling-and-rounding"],
             page="exact-recovery",
             adds=[
                 B("h_p", "grid spacing", "The spacing $2^{-p}$ of the fixed-point grid, in units of which errors are measured."),
                 B("E_s", "source error", "The multiplier $9\\,2^{\\gamma}TL$ bounding the source-transform error in units of $h_p$."),
                 B("E_w", "scaled error", "The multiplier bounding the error of the first scaled result in units of $h_p$."),
                 B("L", "log of box size", "The logarithm $\\log_2T$ of the box size."),
             ],
             salient="Although Gaussian resampling inflates errors by $2^{\\gamma}$ and the scales multiply them by $S$ and $2^{2b+4}$, the final error $448b\\,2^{-3b/4}$ stays below $1/2$ with precision only $p=6b$, because $\\gamma=o(b)$."),
        show("S9.7",
             r"Dividing each cost by $V=Tp$, seven dominant terms have powers of $p$ at most $1-2\kappa$ below one; the smallest margin $2^{-181}$ fixes $\kappa=2^{-182}$, and any polylog factor is absorbed.",
             "Tabulate the normalized cost of each operation as a power of $p$, take the seven dominant exponents, and compare their margins below one with $2\\kappa$.",
             ("Each cost is divided by the volume so its power of $p$ can be read off, and the margins below one are the savings available to $\\kappa$.",
              "recoverable", None),
             [
                 infer("S9.7.1", r"Costs are listed divided by $V=Tp$ in a table of normalized costs, with a fixed number of repeated transforms absorbed in constants.",
                       r"Table~\ref{tab:costs} lists costs after division by $V$"),
                 infer("S9.7.2", r"The seven dominant powers have margins $g_1,\dots,g_7$ below one.",
                       r"The seven dominant powers in Table~\ref{tab:costs} have the following margins below one:"),
                 infer("S9.7.3", r"The smallest margin is $\min_ig_i=2^{-181}=2\kappa$.",
                       r"Thus $\min_i g_i=2^{-181}=2\kappa$."),
                 infer("S9.7.4", r"The layout's $O(p/K)$ chunk exchanges of width $K$ give normalized cost $O(pK^{\tau-1})$.",
                       r"O(p/K)\,K^\tau=O(pK^{\tau-1})."),
                 infer("S9.7.5", r"Axis exposure and restoration take $O(d^2)$ adjacent axis moves each costing $O(V(1+\ell^\tau))$.",
                       r"Axis exposure and restoration require $O(d^2)$ adjacent axis moves."),
                 infer("S9.7.6", r"The Gaussian line costs sum to $O(dTp^{3/2+\delta}\alpha)$, which is the fifth row after dividing by $V=Tp$.",
                       r"Dividing by $V=Tp$ gives the fifth row."),
                 infer("S9.7.7", r"Global setup and prime search cost $o(V)$.",
                       r"Global setup and prime search cost $o(V)$, as proved earlier."),
                 infer("S9.7.8", r"Each of the seven powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually.",
                       r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
                 infer("S9.7.9", r"The complete large-input bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
                       r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})."),
                 infer("S9.7.10", r"Schoolbook multiplication below a fixed cutoff handles the finitely many small lengths, giving one machine with time $O(n(\lg n)^{1-\kappa})$ for every $n$.",
                       r"use schoolbook multiplication below it."),
             ],
             frm=["size-parameters", "exact-recovery", "chunk-interchange", "simultaneous-butterfly-layer", "transform-layout", "ring-convolution", "tensor-resampling-box", "crt-prime-axes", "exponential-and-logarithm-functions"],
             page="time-accounting",
             salient="The saving $\\kappa=2^{-182}$ is astronomically small: it is half the smallest of seven margins, $g_2=\\epsilon c(1-\\tau)=2^{-75}\\cdot2^{-56}\\cdot2^{-50}=2^{-181}$, a product of three tiny exponents."),
    ],
    frm=["transform-layout", "ring-convolution", "gaussian-resampling", "permutation-cancellation"],
    adds=[
        B("b", "digit width", "The number $\\lceil\\log_2 n\\rceil$ of bits in each radix digit.", "count"),
    ],
)

ROOT = show(
    "S0",
    r"A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, using fast address interchange and fast simultaneous butterfly layers inside a Gaussian-resampling, chirp and synthetic-transform reduction.",
    "Reduce the product to a convolution evaluated through Gaussian-resampled, chirped synthetic transforms, make the two costly tape operations (address movement and butterfly layers) cheaper by a power of the logarithm using networks with a rank saving, and then assemble the algorithm and add up its costs.",
    ("Scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so beating $n\\log n$ requires cheaper address movement and cheaper arithmetic.",
     "explicit",
     r"We therefore need savings in both movement and arithmetic."),
    [K, S2, S3, S4, S5, S6, S7, S8, S9],
    frm=["multitape-model", "nlogn-multiplier", "nlogn-conjecture", "big-o", "turing-machine-basics", "binary-integers", "schoolbook-and-karatsuba-multiplication"],
    page="main-theorem",
    adds=[
        B("V", "logical volume", "The number of stored data bits of the array being processed.", "count"),
        B("W", "wire count", "The number of wires, including scratch wires, in a fixed linear network.", "count"),
        B("m", "label dimension", "The dimension of the space whose subspaces label the network, and the factor by which a call's parameter is divided."),
        B("s", "total edge rank", "The sum of the ranks (dimension changes) over all edges of the network, equal to the number of smaller calls.", "count"),
        B("e", "call parameter", "The number of field digits or selected axes handled by one call, a power of $m$.", "count"),
        B("\\tau", "interchange exponent", "A fixed exponent below one with $s/W<m^{\\tau}$, giving the cost $O(Vu^{\\tau})$ of address interchange."),
        B("\\lambda'", "layer exponent", "A fixed exponent below one giving the cost $O(Vd^{\\lambda'})$ of a simultaneous butterfly layer."),
        B("\\kappa", "saving exponent", "The power saving $2^{-182}$ in the final bound $O(n(\\lg n)^{1-\\kappa})$."),
        B("p", "precision", "The number of fractional bits of each stored complex coordinate.", "count"),
        B("d", "axis count", "The number of axes of the transform array, polynomially small in $p$.", "count"),
        B("K", "chunk width", "The number of bits in each address chunk of an axis, with $K=\\lfloor d^c\\rfloor$.", "count"),
        B("r", "record length", "The power-of-two number of complex coefficients in each polynomial record modulo $y^r+1$.", "count"),
        B("\\ell", "record log-length", "The binary logarithm of $r$.", "count"),
        B("T", "box size", "The number of polynomial coefficients in the padded power-of-two box, with $Tp=\\Theta(n)$.", "count"),
        B("s_i", "source length", "The prime length of the $i$th cyclic axis of the source tensor.", "count"),
        B("t_i", "padded length", "The power-of-two length $r/2$ or $r$ of the $i$th axis of the padded box.", "count"),
        B("S", "source size", "The product of the source lengths $s_i$, the length of the cyclic convolution.", "count"),
        B("\\alpha", "Gaussian width", "A parameter controlling the width of the Gaussian weights used in resampling."),
        B("\\epsilon", "axis exponent", "The exponent $2^{-75}$ with $d=\\lfloor b^{\\epsilon}\\rfloor$."),
        B("c", "chunk exponent", "The exponent $2^{-56}$ with $K=\\lfloor d^{c}\\rfloor$."),
        B("F_k", "normalized cost", "The time of a call of parameter $m^k$ divided by its logical volume."),
    ],
)

# remove duplicate F_k binding from K (already at root)
K["adds"] = [x for x in K["adds"] if x["symbol"] != "F_k"]

ANS = {"root": ROOT}


# ---------------------------------------------------------------- checks

def walk(n, out):
    out.append(n)
    for c in n.get("children", []):
        walk(c, out)


nodes = []
walk(ROOT, nodes)
ids = [n["id"] for n in nodes]
assert len(ids) == len(set(ids)), "dup ids"

pos = 0
bad = False
for n in nodes:
    if n["intention"] == "infer":
        q = norm(n["quote"]["quote"])
        i = NSRC.find(q)
        if i < 0:
            print("QUOTE NOT FOUND", n["id"], q[:100])
            bad = True
            continue
        if n.get("deferred"):
            continue
        j = NSRC.find(q, pos)
        if j < 0:
            print("OUT OF ORDER", n["id"], q[:80], "first at", i, "pos", pos)
            bad = True
        else:
            pos = j + len(q)
    else:
        m = n["motivation"]
        if m["source"] == "explicit":
            q = norm(m["quote"]["quote"])
            if NSRC.find(q) < 0:
                print("MOTIVATION QUOTE NOT FOUND", n["id"], q[:100])
                bad = True

pages = [n.get("page") for n in nodes if n.get("page")]
assert len(pages) == len(set(pages)), "dup pages: " + str([p for p in pages if pages.count(p) > 1])

ORDER = """two-point-butterfly multitape-model nlogn-multiplier nlogn-conjecture array-layout gate-network-frames elementary-streams controlled-shifts scratch-restoration subset-intersection-network nondegenerate-subspaces subspace-labels rank-saving-recurrence bit-network-interface phase-interface lower-triangular-factorization matrix-shear-cost power-width-interchange chunk-interchange packed-selected-bit-addition negacyclic-ring cyclic-convolution radix-digit-convolution discrete-fourier-transform multidimensional-transform synthetic-transform bluestein-chirp butterfly-recursion fixed-point-numerics simultaneous-butterfly-layer transform-layout signed-packing ring-convolution gaussian-resampling permutation-cancellation tensor-resampling-box prime-lengths size-parameters crt-prime-axes coefficient-twist source-transform multiplication-algorithm exact-recovery time-accounting main-theorem""".split()
KNOWN = """big-o polynomials complex-numbers turing-machine-basics binary-integers modular-arithmetic linear-algebra-basics big-theta-big-omega-and-little-o-notation divide-and-conquer-recurrences schoolbook-and-karatsuba-multiplication positional-notation-in-any-radix-and-mixed-radix bitwise-operations-xor-and-hamming-weight floor-ceiling-and-rounding exponential-and-logarithm-functions convergent-series-and-the-geometric-series prime-numbers-coprimality-and-trial-division extended-euclidean-algorithm counting-subsets-and-binomial-coefficients permutations-and-permutation-matrices lexicographic-order-and-cartesian-products-of-index-sets vector-norms-inner-products-and-orthogonality gaussian-elimination dyadic-rationals-and-binary-fractions stable-radix-sort-and-counting-sort mathematical-induction""".split()
idx = {p: i for i, p in enumerate(ORDER)}

used_from = set()


def check(n, page_inh):
    page = n.get("page") or page_inh
    for f in n.get("from", []):
        used_from.add(f)
        if f in KNOWN:
            continue
        if f not in idx:
            print("UNKNOWN from", n["id"], f)
            continue
        if idx[f] >= idx[page]:
            print("FROM NOT BEFORE PAGE", n["id"], f, "page", page)
    for c in n.get("children", []):
        check(c, page)


check(ROOT, None)
for p in ORDER:
    if p not in pages and p not in used_from:
        print("PAGE WITHOUT STEP NOT IN FROM:", p)

# adds check
def math_of(n):
    s = n["claim"]
    return " ".join(re.findall(r'\$(.*?)\$', s))


def below(n):
    out = []
    for c in n.get("children", []):
        w = []
        walk(c, w)
        out += w
    return out


for n in nodes:
    for a in n.get("adds", []):
        sym = a["symbol"]
        found = any(sym in math_of(d) for d in below(n))
        if not found:
            print("ADD NOT IN DESCENDANT MATH", n["id"], sym)

if bad:
    print("PROBLEMS")
json.dump(ANS, open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F5V/exegenius/tasks/0003-argument.answer.json', 'w'), indent=1)
print("written", len(nodes), "nodes")
