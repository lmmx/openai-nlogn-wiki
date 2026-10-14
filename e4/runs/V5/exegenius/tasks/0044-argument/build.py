import json, sys

BASE = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e4/V5"
SRC = open(BASE + "/sources/paper.tex").read()


def ev(q):
    return {"source": "paper", "quote": q}


def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


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


def show(id, claim, method, motivation, children, page=None, frm=None, adds=None, salient=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children, "from": frm or []}
    if page:
        n["page"] = page
    if adds:
        n["adds"] = adds
    if salient:
        n["salient"] = salient
    return n


# ---------------------------------------------------------------- S1 streams
S1 = show(
    "S1",
    "Splitting, merging, fixed digit permutations and controlled cyclic shifts of address fields of an array of volume $V$ each cost $O(V)$ on a fixed number of tapes.",
    "split the stream on a digit or field into aligned substreams, process them in lockstep scans, and merge them back",
    mot("Every later procedure moves address fields by tape scans; the reader needs to know which rearrangements are linear and which (growing-width interchanges) are not.", "recoverable"),
    [
        infer("S1.1",
              "Fixed permutations of digit values, digit moves, split-apply-merge and cyclic row splitting into $W$ streams each take $O(V)$ steps.",
              r"takes $O(V)$ steps on a fixed number of one-dimensional tapes"),
        infer("S1.2",
              "Adding to a later address field an offset computed from earlier fields, or multiplying it by a fixed unit modulo $q^b$, costs $O(V)$ by splitting the fiber at the offset and merging the two pieces in the opposite order.",
              r"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
              page="controlled-shifts",
              frm=["modular-arithmetic", "division-with-remainder", "primes-divisibility-and-coprimality", "streams"]),
    ],
    page="streams",
    frm=["tape-basics", "fixed-tape-model", "lexicographic-order-and-mixed-radix-indices", "two-s-complement-and-truncation"],
)

# ---------------------------------------------------------------- S2 chunk interchange
S2_1 = show(
    "S2.1",
    "A fixed linear network of copy, gather, scatter and side-injection gates on banks $X,Y$ and scratch wires sends $(X_a,Y_a)$ to $(-Y_a,X_a)$ in three stages and restores arbitrary initial scratch values.",
    "build one invocation that adds the source value $x_S$ to the target $y_S$ after cancelling the scratch wires' contribution, then compose three invocations",
    mot("The first two rows of the schedule subtract what the old scratch values would contribute and the last two rows put them back, so the net effect cannot depend on the scratch contents.", "recoverable"),
    [
        infer("S2.1.1",
              "For arbitrary initial scratch values a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.",
              r"Thus both net maps are $y\gets y+x$."),
        infer("S2.1.2",
              "Three alternating stages send $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
              r"$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$."),
    ],
    page="scalar-exchange-network",
    frm=["three-subset-pairing", "xor-and-arithmetic-over-f₂", "matrices-and-linear-maps"],
    salient="The exchange is correct for arbitrary initial scratch values, because the scratch contribution is subtracted before the source is introduced and added back afterwards.",
)

S2_2 = show(
    "S2.2",
    "If every wire's stored array is a frame $D_v$ applied to its logical array, pointwise linear gates commute with the common frame, so the network implements $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$ and only the edge changes $D_vD_u^{-1}$ have to be paid for.",
    "maintain the invariant stored array $=D_v$ applied to the logical array along the network, by induction over sources, edges and gates",
    mot("An invariant that is preserved at every vertex lets the intermediate frames cancel, leaving only endpoint frames in the result.", "reconstructed"),
    [
        infer("S2.2.1",
              "The invariant holds at the sources by definition of the logical interpretation of the input.",
              r"It holds at the sources by definition."),
        infer("S2.2.2",
              "A pointwise linear gate commutes with the common frame $D_v$, so the invariant continues through gates to the sinks.",
              r"Thus the common frame commutes with the pointwise gate, and"),
        infer("S2.2.3",
              "The implemented operator is therefore $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$.",
              r"D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}."),
    ],
    page="frames",
    frm=["matrices-and-linear-maps", "scalar-exchange-network"],
    salient="All intermediate frames cancel: the result depends only on the endpoint frames, while each edge pays only for the difference $D_vD_u^{-1}$ of the frames it joins.",
)

S2_3 = show(
    "S2.3",
    "Nested nondegenerate subspaces of an $m$-dimensional space can be attached to gates and terminals so that the dimension lost on decreasing edges is below $N/2$, leaving the total rank $s$ of edge changes strictly below $Wm$.",
    "label each wire with tensor powers of triple-indicator lines so that all dimension loss is confined to one decreasing edge per central wire, then count dimensions along edges",
    mot("Orthogonality of neighbouring triple lines is what allows the nested labels to exist, and the decreasing edges are few enough to count exactly.", "explicit",
        r"Orthogonality of the corresponding indicator vectors permits"),
    [
        infer("S2.3.1",
              "Every triple line is nondegenerate and neighbouring triple lines are orthogonal, in the label field of either construction.",
              r"Thus every triple line is nondegenerate, and neighboring triple lines"),
        infer("S2.3.2",
              "Every edge joins comparable labels and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$, so the total absolute dimension change is $Wm-2N+2L$ with $L=Ich$.",
              r"edges are the central-wire edges from time 3 to time 4; their dimension"),
        infer("S2.3.3",
              "The loss ratios $L/N$ equal $100/539$ and $101/539$ in the two constructions, both below $1/2$, so $L<N/2$.",
              r"In particular, both are smaller than $1/2$."),
    ],
    page="subspace-labels",
    frm=["linear-algebra", "three-subset-pairing", "frames", "scalar-exchange-network"],
    salient="The strict inequality $s<Wm$ holds only by a tiny relative margin (about $10^{-11}$ of $Wm$): the saving is a deficit of $N-2L$ ranks out of $Wm$, positive only because the decreasing edges lose $L<N/2$.",
)

S2_4 = show(
    "S2.4",
    "The $\\mathbb F_2$ bit network on $W_{\\rm b}$ wires, with projection matrices as labels, has endpoint matrices differing by the identity $I_m$ on every input role, so it performs the address shear $H\\leftarrow H+D$, and its total edge rank satisfies $s_{\\rm b}<W_{\\rm b}m$, hence $s_{\\rm b}/W_{\\rm b}<m^\\tau$ for $\\tau=1-2^{-50}$.",
    "assign the projection $P_U$ at every gate or sink labelled $U$ and $-P_{U_a}$ at the source of $X_a$, then read the endpoint difference and sum the edge ranks as label-dimension changes plus one per source",
    mot("Projections are fixed rational matrices whose differences along an edge have rank equal to the label-dimension change, so the dimension count of the labels becomes a count of smaller shears.", "recoverable"),
    [
        infer("S2.4.1",
              "For every input role the endpoint matrix difference is $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m$.",
              r"M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m"),
        infer("S2.4.2",
              "The sum of the edge ranks is $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$.",
              r"=177176569088785861287000000<W_{\rm b}m."),
        infer("S2.4.3",
              "Because the relative deficit is far larger than $20\\cdot2^{-50}$, the fixed exponent $\\tau=1-2^{-50}$ gives $s_{\\rm b}/W_{\\rm b}<m^\\tau$ with $0<\\tau<1$.",
              r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,"),
    ],
    page="bit-network",
    frm=["subspace-labels", "frames", "scalar-exchange-network", "linear-algebra", "matrices-and-linear-maps"],
    salient="The same shear $H\\leftarrow H+D$ results on every role, including the auxiliary roles, although the stored matrices differ on every edge of the network.",
)

S2_5 = show(
    "S2.5",
    "The permutation $(H,D)\\mapsto(H+AD,D)$ of address fields over $\\mathbb Z/q^b\\mathbb Z$ is performed with exactly $\\operatorname{rank}(A)$ interchanges of $b$-digit fields plus $O(V)$ further work.",
    "factor $A=E_1\\Pi E_2$ with lower triangular $E_1,E_2$ and a partial permutation $\\Pi$; the triangular parts are controlled shifts and each one in $\\Pi$ costs one interchange",
    mot("Controlled shifts update a later field from earlier ones in linear time, which is exactly what lower triangular coordinate changes need.", "explicit",
        r"Lower triangular changes of coordinates"),
    [
        infer("S2.5.1",
              "Every rational matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$ with $E_1,E_2$ lower triangular and $\\Pi$ a partial permutation with $a$ ones.",
              r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization",
              page="lower-triangular-factorization",
              frm=["linear-algebra", "matrices-and-linear-maps"]),
        infer("S2.5.2",
              "A lower triangular transformation of the field vector $H$ or $D$ costs $O(V)$ by updating coordinates in descending physical order.",
              r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
        infer("S2.5.3",
              "Each one of $\\Pi$ at position $(i,j)$ is realized by $D_j\\leftarrow D_j+H_i$, an interchange of $H_i,D_j$, and $D_j\\leftarrow H_i-D_j$, using exactly one interchange.",
              r"It uses just one interchange."),
    ],
    page="address-shear",
    frm=["controlled-shifts", "streams", "linear-algebra", "modular-arithmetic", "matrices-and-linear-maps"],
)

K9 = show(
    "S2.6.9",
    "Scheduling the $s$ recursive calls depth-first on a fixed number of tapes costs only $O(V)$ extra at each node, without substituting temporary storage for logical volume in the factor $s/W$.",
    "park the inactive role streams on a stack tape, run the child on the same reserved tapes, and restore the parked streams on return",
    mot("The recurrence is only valid if the bookkeeping for the $W$ role streams at a node costs time proportional to that node's own volume, so the schedule has to be checked.", "reconstructed"),
    [
        infer("S2.6.9.1",
              "Before a recursive call the $W-1$ inactive role streams are appended to a parking stack and the active stream is copied to the child's input area.",
              r"Before a recursive call, append the $W-1$ inactive role streams to the"),
        infer("S2.6.9.2",
              "Each push, pop, copy, positioning or erasure moves $O(V)$ symbols at a parent node, and there are only the fixed number $s$ of child calls.",
              r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
        infer("S2.6.9.3",
              "Temporary storage is not substituted for logical volume in the factor $s/W$.",
              r"therefore not substituted for logical volume in the factor $s/W$."),
    ],
)

S2_6 = show(
    "S2.6",
    "Because the network makes $s<Wm$ calls on role streams of volume $V/W$, the time per unit volume $F_k$ of interchanging two chunks of $e=m^k$ digits satisfies $F_k\\le(s/W)F_{k-1}+O(1)$, and hence $F_k=O(e^\\tau)$.",
    "run the network on the row-split role streams, count the smaller interchanges its edges require, and solve the per-volume recurrence by a geometric sum",
    mot("Each edge of the network costs interchanges of $1/m$ the width on streams of $1/W$ the volume, so the cost recurrence is controlled by the ratio $s/W$ against $m^\\tau$.", "explicit",
        r"$m$, the resulting recurrence saves a power of the chunk width."),
    [
        infer("S2.6.1",
              "Whole rows are split cyclically into $W$ role streams, all of the same shape.",
              r"Split whole rows cyclically into $W$ role streams within each prefix"),
        infer("S2.6.2",
              "Each role stream has logical volume $V/W$ and a row count still divisible by $W^{k-1}$, so the recursion can split again.",
              r"logical volume $V/W$, and its row count is divisible by $W^{k-1}$."),
        infer("S2.6.3",
              "Each edge change $\\Phi_{A_e}$ is executed by interchanging the pivot pairs of $b=e/m$-digit fields, recursively, one interchange per unit of rank.",
              r"recursively interchanging each pivot pair"),
        infer("S2.6.4",
              "Merging the streams back undoes the role permutation $\\rho$ and gives $H\\leftarrow H+D$ on every row, including rows that played scratch roles.",
              r"This undoes $\rho$ and restores row order."),
        infer("S2.6.5",
              "The full interchange is three componentwise updates $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$, of which only the middle shear uses the network.",
              r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,"),
        infer("S2.6.6",
              "The number of recursive calls is the sum of the edge ranks, exactly $s$.",
              r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
        infer("S2.6.7",
              "Dividing the cost by the volume gives $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
              r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."),
        infer("S2.6.8",
              "For $s/W<m^\\tau$ the geometric sum is $O(m^{k\\tau})$, so $F_k=O(e^\\tau)$.",
              r"For $a=s/W<m^\tau$ the geometric sum"),
        K9,
    ],
    page="power-saving-recursion",
    frm=["frames", "subspace-labels", "scalar-exchange-network", "streams", "recurrences-and-divide-and-conquer"],
    adds=[
        B("e", "chunk width", "The number of radix-$q$ digits in each of the two address chunks, equal to $m^k$.", "count"),
        B("k", "recursion depth", "The number of times the chunk width has been divided by $m$ to reach a single digit.", "count"),
        B("F_k", "cost per volume", "The time of the interchange of chunks of width $m^k$, divided by the logical volume of the stream.", "direct"),
    ],
    salient="Each level multiplies the work per unit volume by $s/W$, which is strictly below $m^\\tau$ where $\\tau<1$, while the width grows by the factor $m$; so the total grows like $e^\\tau$, a strict power below the $e$ of a naive pass per digit.",
)

S2_7 = show(
    "S2.7",
    "The restrictions to power widths and enough rows can be removed: two arbitrary $u$-bit chunks of an array of volume $V$ are interchanged in $O(Vu^\\tau)$ time.",
    "supply rows from the chunks' own high digits, pad the row count to a multiple of $W^k$, and split the remaining width in base $m$ into power-width pieces",
    mot("Rows for a general array can be supplied by a few of its own high digits.", "explicit",
        r"Rows for a general array can be supplied by a few of its own high digits."),
    [
        infer("S2.7.1",
              "Padding with zero rows brings the row count to $R'=W^k\\lceil R/W^k\\rceil<2R$, at most doubling the volume.",
              r"R'=W^k\left\lceil R/W^k\right\rceil<2R."),
        infer("S2.7.2",
              "Writing the remaining width in base $m$ and applying the power-width interchange to each piece costs $O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau)$.",
              r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)."),
    ],
)

S2 = show(
    "S2",
    "Two disjoint $u$-bit address chunks of an array of volume $V$ can be interchanged in $O(Vu^\\tau)$ time for a fixed $\\tau<1$, although the intermediate steps compute XOR combinations of the data.",
    "turn the interchange into the address shear $H\\leftarrow H+D$ and perform that by a fixed linear bit network on $W$ role streams whose edge changes are themselves smaller interchanges, then solve the resulting recursion",
    mot("An edge matrix of rank $a$ will require $a$ smaller interchanges.", "explicit",
        r"An edge matrix of rank $a$ will require $a$ smaller interchanges."),
    [S2_1, S2_2, S2_3, S2_4, S2_5, S2_6, S2_7],
    page="chunk-interchange",
    frm=["streams", "controlled-shifts", "recurrences-and-divide-and-conquer", "lexicographic-order-and-mixed-radix-indices"],
    adds=[
        B("W", "wire count", "The number of wires of the fixed linear network, which is also the number of role streams a node is split into.", "count"),
        B("m", "label dimension", "The dimension of the fixed space carrying the labels, equal to the number of digit fields per address chunk of the network's matrices.", "count"),
        B("s", "call count", "The sum of the ranks of all edge matrices of the network, which is the number of smaller interchanges one call makes.", "count"),
        B("\\tau", "interchange exponent", "The fixed exponent below 1 with $s/W<m^\\tau$, giving the interchange cost $O(Vu^\\tau)$.", "direct"),
    ],
    salient="Although the network computes XOR combinations of intermediate data, its final effect is an exact permutation, valid for arbitrary initial values of the auxiliary wires.",
)

# ---------------------------------------------------------------- S3 simultaneous layer
C1 = show(
    "S3.1",
    "Phase frames $\\mathcal C_U=H^{\\otimes m}\\operatorname{diag}(i^{q_U(x)})H^{\\otimes m}$ turn each edge of the complex network into a product of two-point kernels $aI+bX_v$ and give $C^{\\otimes m}$ on every role, where $C=H\\,\\mathrm{diag}(1,i)\\,H$; since $H_0=b\\mathsf SC\\mathsf S$, a layer of $H_0$ on $D$ selected bits equals $b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$.",
    "conjugate each edge's binary basis change into coordinate directions, run one smaller call per residual direction, and convert the resulting $C$ layer to $H_0$ by diagonal phases and a dyadic scale",
    mot("Gaussian dyadic coefficients make every kernel exact, and conjugating by a change of basis lets each residual direction become a coordinate direction on one slot of axes.", "recoverable"),
    [
        infer("S3.1.1",
              "The phase-frame change on an edge is a product of one translation kernel $aI+bX_v$, or its inverse, per vector of an orthonormal basis of the edge residual.",
              r"$\mathcal C_V\mathcal C_U^{-1}$ is a product of one translation",
              deferred=True),
        infer("S3.1.2",
              "After the endpoint corrections and undoing the bank exchange, the telescoped phase frames give $C^{\\otimes m}$ on every role, scratch roles included.",
              r"telescoping these phase frames gives $C^{\otimes m}$",
              deferred=True),
        infer("S3.1.3",
              "Direct multiplication gives $H_0=b\\mathsf SC\\mathsf S$, $C^2=X$ and $C^4=I$ with Gaussian dyadic coefficients.",
              r"H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad"),
        infer("S3.1.4",
              "Conjugating by an address permutation $\\mathcal P_M$ whose first columns are the residual basis, the edge change becomes a product of coordinate kernels $C_{e_j}^{\\epsilon_j}$.",
              r"=\mathcal P_M\left(\prod_{j=1}^{\rho_{\rm edge}}C_{e_j}^{\epsilon_j}\right)"),
        infer("S3.1.5",
              "An inverse kernel needs only one forward child, since $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$.",
              r"=(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}."),
        infer("S3.1.6",
              "Summing the residual dimensions gives exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
              r"Summing its residual dimensions gives exactly"),
        infer("S3.1.7",
              "The butterfly layer is $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$.",
              r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D."),
    ],
    page="phase-frames",
    frm=["butterfly", "subspace-labels", "frames", "scalar-exchange-network", "linear-algebra", "complex-numbers", "xor-and-arithmetic-over-f₂"],
    salient="The same kernel $C^{\\otimes}$ appears on every role of the network, scratch roles included, and every coefficient stays a Gaussian dyadic.",
)

C2 = show(
    "S3.2",
    "Adding corresponding selected bits of two address chunks, a binary row addition on $f$ selected positions, restores an arbitrary third chunk and costs $O(V(L^\\tau+1))$ using whole-chunk cyclic shifts and a repair of an explicitly bounded exceptional set.",
    "perform eight packed cyclic shifts that equal the desired XORs except at addresses whose guard values lie near the ends of their ranges, then repair those few addresses by stable sorting",
    mot("Cyclic shifts of whole chunks are linear-time controlled shifts, and the only failure is carries between packed segments, which are confined to a small, address-determined set.", "recoverable"),
    [
        infer("S3.2.1",
              "Eight carry-propagating additions flip the parity of $u$ exactly when the control is 1 and restore the auxiliary integer $w$.",
              r"\bigl(u+c(1-2(u\bmod2)),\ w\bigr)."),
        infer("S3.2.2",
              "The set of addresses where a guard value falls in the 20 excluded values has size at most $\\delta_{\\rm bad}M$, whatever the payload.",
              r"|\mathcal B|\le\delta_{\rm bad}M."),
        infer("S3.2.3",
              "Sorting the extracted exceptional records by their destination ranks and reinserting them implements the ideal XOR map everywhere.",
              r"This implements $T_0$ everywhere."),
        infer("S3.2.4",
              "The movement costs $O(V(L^\\tau+1))$ using the arbitrary-width chunk interchange.",
              r"The movement costs $O(V(L^\tau+1))$."),
    ],
    page="packed-selected-bits",
    frm=["chunk-interchange", "controlled-shifts", "streams", "binary-representation-and-integer-arithmetic", "xor-and-arithmetic-over-f₂"],
    salient="The auxiliary third chunk may hold any value and is restored, because the eight additions are arranged so that its parity changes cancel.",
)

C3 = show(
    "S3.3",
    "With $s$ child calls on streams of volume $V/W$, the time per unit volume of a layer on $e$ axes satisfies $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$, which solves to $O(d^{\\lambda'})$.",
    "unroll the same rank-deficit recurrence as for chunk interchange, with the packed basis changes as node overhead and individual kernels below a cutoff",
    mot("The saving factor $s/W<m^\\sigma$ again makes the sum of node overheads geometric, and the cutoff $e<d^{1/2}$ keeps the leaves cheap.", "recoverable"),
    [
        infer("S3.3.1",
              "Normalizing by volume, $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ with $F(e)=O(e)$ below the cutoff.",
              r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
        infer("S3.3.2",
              "Since $a=s/W<m^\\lambda$, the internal costs sum to $O(e^\\lambda)$.",
              r"C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)."),
        infer("S3.3.3",
              "Splitting $D$ chunks into base-$m$ pieces and adding the leaf contribution gives total cost $O(d^{\\lambda'})$ per unit volume.",
              r"=O(d^{\lambda'})"),
    ],
)

C4 = show(
    "S3.4",
    "Reserving $p+\\Delta$ fractional bits and $\\Delta+3$ integer bits per real component, with $\\Delta=\\lceil C_0d^{C_1}\\rceil=o(p)$, represents every intermediate value of one whole layer exactly, with width still $O(p)$.",
    "bound the arithmetic dependency depth of a layer, since each addition at most doubles the modulus and each halving adds one denominator bit",
    mot("Because the layer is evaluated exactly and truncated only once, one only needs to know how many guard bits the longest chain of operations can consume.", "recoverable"),
    [
        infer("S3.4.1",
              "The dependency depth obeys $A(e)\\le sA(e/m)+E$ at an internal node, with $E$ a fixed constant.",
              r"A(e)\le sA(e/m)+E"),
        infer("S3.4.2",
              "A value at depth $\\ell$ lies in $2^{-(p+\\ell)}\\mathbb Z[i]$ and has modulus at most $2^\\ell$.",
              r"lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most \(2^\ell\)."),
        infer("S3.4.3",
              "Reserving $\\Delta$ extra fractional bits and $\\Delta+3$ integer and sign bits represents every intermediate coefficient exactly.",
              r"fractional bits and \(\Delta+3\) integer and sign bits per real"),
        infer("S3.4.4",
              "Choosing $\\epsilon C_1<1$ makes $\\Delta=o(p)$, so the full coefficient width stays $O(p)$.",
              r"Choose \(\epsilon C_1<1\)."),
    ],
    frm=["dyadic-exact", "fixed-point"],
)

C5 = infer(
    "S3.5",
    "Since $\\mathcal H$ has absolute row sums one it maps disk arrays to disk arrays, and the single final truncation $Q_p$ toward zero adds error below $\\sqrt2\\,2^{-p}$.",
    r"Finally, every row of $\mathcal H$ has",
)

S3 = show(
    "S3",
    "Applying $H_0$ simultaneously to the same bit position of $D\\le d$ address chunks of a polynomial array of volume $V$ costs $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$, with exact Gaussian dyadic intermediate values and one final truncation.",
    "express the layer through the complex phase network, recurse on groups of $e=mf$ axes with the same rank saving, implement the binary basis changes by packed selected-bit addition, evaluate exactly with guard bits and truncate once",
    mot("Applying the butterflies as separate factors would take D passes over the array; combining them in the network gives a saving through the rank deficit.", "explicit",
        r"factors would require $D$ whole-array passes."),
    [C1, C2, C3, C4, C5],
    page="simultaneous-layer",
    frm=["fixed-point", "dyadic-exact", "butterfly", "chunk-interchange", "power-saving-recursion", "subspace-labels", "recurrences-and-divide-and-conquer", "inequalities-for-error-bounds"],
    adds=[
        B("d", "axis bound", "The maximum number of address chunks (axes) on which the butterfly layer acts at once.", "count"),
        B("K", "chunk width", "The number of address bits in each chunk, about $d^c$ for a small fixed $c$.", "count"),
        B("\\lambda'", "layer exponent", "The fixed exponent below 1 in the layer cost $O(Vd^{\\lambda'})$.", "direct"),
    ],
    salient="One layer on $d$ axes costs $O(d^{\\lambda'})$ per unit volume with $\\lambda'<1$, instead of $d$ separate passes.",
)

# ---------------------------------------------------------------- S4 transform layout
D1 = show(
    "S4.1",
    "Over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ the roots $\\omega_t=y^{2r/t}$ are powers of $y$, so $F_t^\\pm$ are contractions with $F_t^+F_t^-=t^{-1}I$, and $F_t^-$ is computed by radix-two butterfly rounds whose twiddle multiplications are signed shifts.",
    "verify character cancellation directly in the ring, then split a length-$t$ transform into two half-length ones after one butterfly and a twiddle (decimation in frequency)",
    mot("The ring has zero divisors, so character cancellation is verified directly instead of dividing by $\\omega_t^j-1$.", "explicit",
        r"The ring has zero divisors, so we verify character cancellation"),
    [
        infer("S4.1.1",
              "Character cancellation gives $\\sum_k\\omega_t^{jk}=t$ if $t\\mid j$ and $0$ otherwise, hence $F_t^+F_t^-=t^{-1}I$.",
              r"F_t^+F_t^-=t^{-1}I."),
        infer("S4.1.2",
              "The decimation-in-frequency identity expresses $(F_t^-z)_{2h+b}$ as a half-length transform of $(z_k+(-1)^bz_{k+t/2})/2$ times a twiddle.",
              r"\frac{z_k+(-1)^b z_{k+t/2}}2."),
    ],
    page="synthetic-transform",
    frm=["ring-mod-yr-plus-1", "butterfly", "dft", "convolution", "fast-fourier-transform-as-an-algorithm", "complex-numbers", "polynomials"],
)

D2 = show(
    "S4.2",
    "The forward synthetic transform leaves entry $j$ in slot $\\operatorname{rev}_a(j)$, and a reverse-order procedure consumes that same order, implementing $B_tF_t^-$ and $F_t^+B_t^{-1}$, so no reordering is executed.",
    "write each butterfly output in place so that frequency bits accumulate in reverse order, and run the recursion backwards for the opposite transform",
    mot("The recursion writes its outputs directly in this order; it does not move whole frequency indices.", "explicit",
        r"directly in this order; it does not move whole frequency indices."),
    [
        infer("S4.2.1",
              "After all rounds the entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$.",
              r"entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$."),
        infer("S4.2.2",
              "The reversed procedure and the forward one implement $B_tF_t^-$ and $F_t^+B_t^{-1}$ respectively.",
              r"B_tF_t^-,\qquad F_t^+B_t^{-1},"),
    ],
    page="stored-order",
    frm=["synthetic-transform", "butterfly", "ring-mod-yr-plus-1"],
    salient="The frequencies come out in bit-reversed order, yet no step pays to unscramble them: a pointwise product commutes with any common record permutation, and the opposite transform reads the same order.",
)

S4 = show(
    "S4",
    "A synthetic transform of $M$ degree-$<r$ polynomial records on $d-1$ axes can be laid out so that every round is a simultaneous butterfly layer, with error below $\\sqrt2\\,\\ell\\,2^{-p}$ and total cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
    "move the selected bits of the participating axes to a common offset in consecutive $K$-bit chunks using single-bit moves and chunk interchanges, so that each round is one call of the simultaneous layer",
    mot("To apply the simultaneous layer in a transform round, the selected bits of the participating axes must be at a common offset in consecutive chunks.", "explicit",
        r"we must place the selected bits of the participating axes at a common"),
    [
        D1,
        D2,
        infer("S4.3",
              "Moving the $O(dK)$ listed bit slots of the long axes and bottom positions to a prefix costs $O(TpdK)$.",
              r"listed slots, so the moves cost $O(TpdK)$."),
        infer("S4.4",
              "The $Dq$ chunk exchanges of width $K$ that interleave the axes cost $O(Tp\\cdot pK^{\\tau-1})$.",
              r"=O\bigl(Tp\,pK^{\tau-1}\bigr)."),
        infer("S4.5",
              "The rounds on the remaining chunks call the simultaneous layer, costing $O(Tpd^{\\lambda'})$ per round and $O(Tp\\ell d^{\\lambda'})$ in total.",
              r"$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total."),
        infer("S4.6",
              "The at most $K$ rounds on prefix slots are done by individual butterflies, costing $O(TpdK)$.",
              r"most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$."),
        infer("S4.7",
              "Each round is a contraction followed by one truncation, so after at most $\\ell$ rounds the error is below $\\sqrt2\\,\\ell\\,2^{-p}$ and the output is a disk grid array.",
              r"give the claimed error and disk bounds."),
    ],
    page="transform-layout",
    frm=["simultaneous-layer", "chunk-interchange", "streams", "synthetic-transform", "stored-order", "ring-mod-yr-plus-1", "fixed-point"],
)

# ---------------------------------------------------------------- S5 synthetic convolution
F1 = show(
    "S5.1",
    "A product in $\\mathbb C[y]/(y^r+1)$ of two disk polynomials with $p$-bit grid coefficients reduces to four integer products of $4pr$-bit numbers by evaluation at $B_0=2^{4p}$, and the normalized product $Q_p(fg/r)$ costs $O(rp\\log(rp))$ with the established multiplier.",
    "signed Kronecker substitution: evaluate each polynomial at $2^{4p}$ with carries, multiply the evaluation integers, recover the centered coefficients, and reduce modulo $y^r+1$",
    mot("The established integer multiplier works on integers, so polynomial coefficients are packed with enough room that adjacent fields cannot interact, with negative values handled by centered residues.", "recoverable"),
    [
        infer("S5.1.1",
              "Each polynomial is packed into a signed evaluation integer $A_u=u(B_0)$ with $B_0=2^{4p}$.",
              r"and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer"),
        infer("S5.1.2",
              "Four products of absolute values are formed by the established multiplier and their signs restored.",
              r"pairs of absolute values using the established multiplier and restore"),
        infer("S5.1.3",
              "Every coefficient of an ordinary product satisfies $|h_j|\\le r2^{2p}<2^{3p}<B_0/2$, so fields do not overlap.",
              r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
        infer("S5.1.4",
              "Extraction of the centered residues with carry recovers each coefficient exactly: $\\widehat h_j=h_j$.",
              r"Thus $\widehat h_j=h_j$."),
        infer("S5.1.5",
              "Four exact integer products dominate the linear packing, extraction, wrapping and truncation costs.",
              r"Four exact integer products dominate the linear"),
    ],
    page="signed-packing",
    frm=["hvdh-multiplier", "ring-mod-yr-plus-1", "polynomials", "two-s-complement-and-truncation", "fixed-point"],
    salient="Negative coefficients are packed with no sign bookkeeping beyond a carry in $\\{-1,0\\}$, and extraction by centered residues is unambiguous because $|h_j|<B_0/2$.",
)

S5 = show(
    "S5",
    "Two forward synthetic transforms kept in the same order, a pointwise ring product by signed packing, and the opposite transform give the normalized convolution $\\mathcal M_r(f,g)=f*g/T$ over $\\mathbb C[y]/(y^r+1)$ with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
    "multiply the two forward transforms pointwise in their retained stored order and apply the opposite transform, tracking the error by bilinear contraction",
    mot("Pointwise multiplication commutes with applying the same record permutation to both operands, so the stored order never has to be undone.", "explicit",
        r"Pointwise multiplication commutes with applying the same record"),
    [
        F1,
        infer("S5.2",
              "Expansion of the finite sums gives $F^-_{\\boldsymbol t}(f*g)=M(F^-_{\\boldsymbol t}f)(F^-_{\\boldsymbol t}g)$.",
              r"=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)."),
        infer("S5.3",
              "Since $LB$ permutes records and leaves their polynomial suffixes intact, the pointwise product of the stored forward outputs equals the stored product, so the opposite transform of it gives the convolution.",
              r"Since $LB$ permutes records and leaves their polynomial suffixes"),
        infer("S5.4",
              "The two forward errors and the product truncation propagate through contractions to a total error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ after the exact scaling by $M$.",
              r"$M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed."),
        infer("S5.5",
              "There are $M=T/r$ pointwise polynomial products, costing $O(Tp\\log(rp))$ in total, in addition to the three transforms.",
              r"There are $M=T/r$ pointwise polynomial products."),
    ],
    page="synthetic-convolution",
    frm=["transform-layout", "signed-packing", "stored-order", "convolution", "dft", "ring-mod-yr-plus-1", "fixed-point", "inequalities-for-error-bounds"],
)

# ---------------------------------------------------------------- S6 retained permutations
S6 = show(
    "S6",
    "Gaussian resampling gives $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ with both coordinate permutations left inside the transform: the target permutation is absorbed by a chirp convolution and the source permutation cancels across two forward transforms, a pointwise product and the opposite transform, so neither is executed as a sort.",
    "keep both permutations in the transform identity, tensorize over the axes, apply Bluestein's chirp identity to the middle transform, and use a dilation identity to cancel the source permutation",
    mot("Its usual implementation sorts twice on each coordinate; we retain both permutations in the transform formula and compute that formula directly.", "explicit",
        r"coordinate. We retain both permutations in the transform formula and"),
    [
        infer("S6.1",
              "For coprime $s<t$ with $t/s-1>p/\\alpha^4$ there are contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$.",
              r"P_sF_s=2^{2\alpha^2}B_0P_tF_tA."),
        infer("S6.2",
              "There are fixed multitape algorithms for approximations of $A$ and $B_0$ with error below $p^2$ and time $O(tp^{3/2+\\delta}\\alpha)$.",
              r"There are fixed multitape algorithms for approximations"),
        infer("S6.3",
              "Tensoring over the axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$.",
              r"=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A,"),
        infer("S6.4",
              "The linewise maps cost $O(dTp^{3/2+\\delta}\\alpha)$ in total.",
              r"$O(dTp^{3/2+\delta}\alpha)$, with a constant independent of $d$."),
        infer("S6.5",
              "Exposing and restoring each axis uses adjacent interchanges, bounded by the equal-width chunk-swap cost.",
              r"using the equal-width chunk-swap bound $O(Vu^\tau)$ and the fixed-digit"),
        infer("S6.6",
              "The chirp identity gives $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$, so the target permutation $Q$ is absorbed by the chirp.",
              r"This is precisely the coefficient in $QF_{\boldsymbol t}$, because"),
        infer("S6.7",
              "Since each $t_i$ is a unit modulo $s_i$, $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$.",
              r"$F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence"),
        infer("S6.8",
              "By the convolution rule the source permutation cancels: $RF_{\\boldsymbol s}^+[(RF_{\\boldsymbol s}u)(RF_{\\boldsymbol s}v)]=u*v/S^2$.",
              r"The normalized convolution rule is"),
    ],
    page="retained-permutations",
    frm=["gaussian-resampling", "dft", "bluestein-chirp", "convolution", "chunk-interchange", "hvdh-multiplier", "fixed-point", "inequalities-for-error-bounds"],
    salient="Neither coordinate permutation is ever applied to the data: $Q$ is swallowed by the chirp phases and $R$ cancels because $RF_s^+R=F_s^+$ for the coprime lengths.",
)

# ---------------------------------------------------------------- S7 multiplication algorithm
G1 = show(
    "S7.1",
    "The choice $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, a power of two $T\\in[4n/b,8n/b)$, axis lengths $r/2$ or $r$ with product $T$, and distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ gives $Tp=\\Theta(n)$, $T/2<S<T$, and $r$ exceeding every power of $p$.",
    "fix the rational exponents first, then express every size in terms of $b$ and find the primes in two disjoint intervals just below the power-of-two axis lengths, using a prime-interval estimate",
    mot("The distinct prime lengths must be close to the powers of two so that their product fills a fixed fraction of the padded box and each ratio leaves enough separation for resampling.", "explicit",
        r"The distinct prime lengths $s_i$ must be close to the powers of two"),
    [
        infer("S7.1.1",
              "The exponents are fixed rationals: $\\tau=\\sigma=1-2^{-50}$, $\\beta=1/2$, $\\delta=1/16$.",
              r"\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},"),
        infer("S7.1.2",
              "The remaining exponents are $C_1=20$, $\\epsilon=2^{-75}$ and $\\kappa=2^{-182}$.",
              r"C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}."),
        infer("S7.1.3",
              "The sizes are $b=\\lceil\\log_2n\\rceil$, $p=6b$ and $d=\\lfloor b^\\epsilon\\rfloor$.",
              r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,"),
        infer("S7.1.4",
              "These give $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$, $\\ell=\\Theta(p^{1-\\epsilon})$ and $r=2^{\\Theta(p^{1-\\epsilon})}$.",
              r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad"),
        infer("S7.1.5",
              "There are enough primes in the two disjoint intervals, so distinct odd primes with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ exist.",
              r"(1-2\eta)t_i<s_i\leq(1-\eta)t_i."),
        infer("S7.1.6",
              "Multiplying the lower bounds and using Bernoulli's inequality gives $T/2<S<T$.",
              r"Together with $s_i<t_i$, this gives $T/2<S<T$."),
        infer("S7.1.7",
              "Every hypothesis of the resampling lemma holds for all sufficiently large input lengths.",
              r"Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for"),
    ],
    page="size-parameters",
    frm=["primes-divisibility-and-coprimality", "logarithms-floors-and-ceilings", "inequalities-for-error-bounds", "gaussian-resampling", "simultaneous-layer", "transform-layout", "retained-permutations"],
)

G2 = show(
    "S7.2",
    "Writing both inputs in radix $2^b$ with $q=\\lceil n/b\\rceil$ digits, the product's coefficients are the convolution of the digit sequences, with no wraparound modulo $x^S-1$ and every coefficient below $2^{3b}$.",
    "bound the degree of the product polynomial against the padded length and the size of each coefficient against the working precision",
    mot("Reading the integer product as a cyclic convolution of length $S$ is only valid if the degree stays below $S$, and the later rounding needs the coefficient range.", "reconstructed"),
    [
        infer("S7.2.1",
              "The product has degree at most $2q-2<2n/b\\le T/2<S$.",
              r"2q-2<2n/b\le T/2<S."),
        infer("S7.2.2",
              "Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
              r"Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
        infer("S7.2.3",
              "Every product coefficient obeys $0\\le c_j\\le q(2^b-1)^2<2^{3b}$.",
              r"0\le c_j\le q(2^b-1)^2<2^{3b},"),
    ],
    page="digit-convolution",
    frm=["convolution", "schoolbook-and-karatsuba-multiplication", "binary-representation-and-integer-arithmetic"],
)

G3 = show(
    "S7.3",
    "For pairwise coprime lengths $s_i$ with $S=\\prod s_i$, the map $x\\mapsto\\prod x_i^{\\mu_i}$ is an isomorphism from $\\mathbb C[x]/(x^S-1)$ to the product of cyclic axes that preserves convolution, and is realized by triangular controlled shifts in $O(Tp\\,d^2(1+\\ell^\\tau))$ time.",
    "use the Chinese-remainder map of Agarwal and Cooley with coordinate powers chosen so that the index change is triangular",
    mot("The coordinate powers are chosen so that the change of order becomes a sequence of controlled cyclic shifts.", "explicit",
        r"algebraic split, with coordinate powers that make the change of order a"),
    [
        infer("S7.3.1",
              "The map $\\Phi$ is an isomorphism and preserves cyclic convolution.",
              r"$\Phi$ is an isomorphism and preserves cyclic convolution."),
        infer("S7.3.2",
              "Axis $i$ of the image of $x^k$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}$, a shift controlled by lower-index digits.",
              r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}."),
        infer("S7.3.3",
              "Updating the targets in the order $i=d,d-1,\\ldots,1$ uses the original lower-index digits.",
              r"order $i=d,d-1,\ldots,1$ using \eqref{eq:triangular-crt}."),
        infer("S7.3.4",
              "Reordering the axes with chunk interchanges makes $\\Phi$, its inverse and their padding cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
              r"their padding operations cost"),
    ],
    page="crt-cyclic-axes",
    frm=["convolution", "controlled-shifts", "chunk-interchange", "modular-arithmetic", "primes-divisibility-and-coprimality", "lexicographic-order-and-mixed-radix-indices"],
)

G4 = show(
    "S7.4",
    "Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ maps $\\mathbb C[x]/(x^r-1)$ isomorphically onto $\\mathbb C[y]/(y^r+1)$, so cyclic convolution on the last axis is computed over the ring after the twist and recovered after the untwist.",
    "twist by a $2r$-th root of unity so that the relation $x^r=1$ becomes $y^r=-1$ and negative wrap turns into cyclic wrap",
    mot("The synthetic transforms work in a ring where $y^r=-1$, whereas the chirp convolution is cyclic, so an invertible diagonal change of basis is needed between them.", "recoverable"),
    [
        infer("S7.4.1",
              "The map $x_d\\mapsto\\zeta y$ is well defined because $(\\zeta y)^r=(-1)(-1)=1$.",
              r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."),
        infer("S7.4.2",
              "For $k+l=j+hr$ a twisted product term has factor $\\zeta^{k+l}(-1)^h=\\zeta^j$.",
              r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j."),
        infer("S7.4.3",
              "Untwisting recovers the cyclic coefficient with the correct sign.",
              r"Untwisting therefore recovers the cyclic coefficient with the correct"),
    ],
    page="phase-twist",
    frm=["ring-mod-yr-plus-1", "convolution", "complex-numbers", "polynomials"],
    salient="The sign of the negative wrap and the extra factor from the twist cancel for both wrap values $h\\in\\{0,1\\}$, leaving $\\zeta^j$ independent of $h$.",
)

G5 = infer(
    "S7.5",
    "The source transform (resample by $\\mathcal A$, apply the chirp transform, resample by $\\mathcal B_0$, scale by $2^\\gamma$) has exact counterpart $RF_{\\boldsymbol s}$.",
    r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A",
)

G6 = show(
    "S7.6",
    "Digits are placed on the prime axes, transformed twice, multiplied pointwise, transformed back, rescaled by $S$ and $2^{2b+4}$, rounded and carried to give the $2n$-bit product.",
    "evaluate the convolution as the opposite transform of the pointwise product of two forward source transforms, then undo the known normalizations",
    mot("A convolution is the inverse transform of a pointwise product of transforms; the scales $S$ and $2^{2b+4}$ undo the normalizations that the transforms and digit placement introduced.", "reconstructed"),
    [
        infer("S7.6.1", "Apply the coefficient-address map $\\Phi$ with its padded layout to obtain the source arrays $u,v$.",
              r"\item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain"),
        infer("S7.6.2", "Compute the source transforms $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$.",
              r"\item Compute $\widetilde{\mathscr F}(u)$ and"),
        infer("S7.6.3", "Multiply corresponding coefficients exactly and truncate to $p$ fractional bits, giving $z$.",
              r"\item Multiply corresponding complex coefficients exactly and truncate"),
        infer("S7.6.4", "Compute the opposite transform of $z$ and multiply by $S$.",
              r"\item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid"),
        infer("S7.6.5", "Multiply by $2^{2b+4}S$ and round to nearest integers, then undo $\\Phi$.",
              r"\item Multiply the grid numerators of $\widetilde w$ exactly by"),
        infer("S7.6.6", "Propagate radix-$2^b$ carries in increasing coefficient order and output $2n$ bits.",
              r"\item Propagate radix-$2^b$ carries in increasing coefficient order."),
        infer("S7.6.7", "The two occurrences of $S$ undo different normalizations: the exact counterpart after three transforms is $(u*v)/S^2$.",
              r"The two occurrences of $S$ in this algorithm undo different"),
    ],
)

G7 = show(
    "S7.7",
    "After undoing the known scales $S$ and $2^{2b+4}$, every computed coefficient is within $1/2$ of the true integer coefficient of the digit convolution, so rounding is exact, and propagating radix-$2^b$ carries yields the exact $2n$-bit product.",
    "track the error of each computed map through contractions and bilinear products, multiply by the rescaling factors, and compare the final error with $1/2$",
    mot("Every computed map is only an approximation on a $2^{-p}$ grid, so exactness of the product rests on showing that the accumulated error, after being scaled up, is still below one half.", "recoverable"),
    [
        infer("S7.7.1", "The normalized ring convolution has error below $E_{\\rm ring}:=M(3L+2)<5TL$ in units of $2^{-p}$.",
              r"E_{\rm ring}:=M(3L+2)<5TL."),
        infer("S7.7.2", "The computed chirp transform has error below $8TL$.",
              r"<(6TL+2+4+4)h_p<8TLh_p."),
        infer("S7.7.3", "The source transform has error at most $E_s=9\\,2^\\gamma TL$.",
              r"E_s=9\,2^\gamma TL,"),
        infer("S7.7.4", "After the opposite transform and the scale by $S$ the error is below $E_w:=S(3E_s+2)<28\\,2^\\gamma T^2L$.",
              r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
        infer("S7.7.5", "After the second scaling by $2^{2b+4}S$ the absolute error is below $448b\\,2^{-b+\\gamma}\\le448b\\,2^{-3b/4}<1/2$.",
              r"<448b\,2^{-b+\gamma}"),
        infer("S7.7.6", "The strict error below $1/2$ makes the nearest integer the unique correct coefficient.",
              r"that value the unique correct coefficient."),
        infer("S7.7.7", "Carries obey $k_0=0$, $d_j=(c_j+k_j)\\bmod Q_0$, $k_{j+1}=\\lfloor(c_j+k_j)/Q_0\\rfloor$.",
              r"k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad"),
        infer("S7.7.8", "The carries stay bounded: $0\\le k_j\\le q(Q_0-1)<Q_0^2$.",
              r"The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$."),
    ],
    page="exact-recovery",
    frm=["fixed-point", "digit-convolution", "inequalities-for-error-bounds", "two-s-complement-and-truncation", "division-with-remainder"],
    salient="The final error is below $448b\\,2^{-3b/4}$, far below $1/2$ even though the scales $2^\\gamma$, $S$ and $2^{2b+4}$ amplify the $2^{-p}$ grid errors, because the precision is $p=6b$.",
)

S7 = show(
    "S7",
    "Placing radix-$2^b$ digits on prime cyclic axes by the Chinese-remainder map, taking two source transforms by Gaussian resampling with chirp convolution over the ring, a pointwise product and one opposite transform, then rescaling, rounding and propagating carries, computes the exact $2n$-bit product.",
    "compose the reductions of integer product to radix-digit convolution, to cyclic convolution on prime axes, to normalized convolution on power-of-two axes, and to convolution over the polynomial ring, then undo the scalings",
    mot("The remaining proof places these procedures inside the multiplication reduction and accounts for every change of representation.", "explicit",
        r"reduction and accounts for every change of representation."),
    [G1, G2, G3, G4, G5, G6, G7],
    page="multiplication-algorithm",
    frm=["convolution", "synthetic-convolution", "retained-permutations", "digit-convolution", "crt-cyclic-axes", "phase-twist", "exact-recovery", "size-parameters", "bluestein-chirp"],
    adds=[
        B("b", "digit width", "The number of bits per radix digit, $\\lceil\\log_2n\\rceil$, so inputs have $q=\\lceil n/b\\rceil$ digits in radix $2^b$.", "direct"),
        B("p", "working precision", "The number of fractional bits of the fixed-point grid, equal to $6b$.", "count"),
        B("T", "box size", "The power-of-two number of entries of the padded box on which the transforms act, about $n/b$.", "count"),
        B("S", "product of prime lengths", "The product of the distinct odd prime axis lengths $s_i$, between $T/2$ and $T$.", "direct"),
    ],
)

# ---------------------------------------------------------------- S8 cost accounting
H1 = show(
    "S8.1",
    "The normalized costs of the stages, divided by $Tp$, are $dK$, $pK^{\\tau-1}$, $\\ell d^{\\lambda'}$, $d^2(1+\\ell^\\tau)$, $dp^{1/2+\\delta}\\alpha$, $dp^\\delta$ and $\\log(rp)$, with powers of $p$ below one.",
    "tabulate the cost of each stage per unit of $Tp$ using the bounds proved for each procedure",
    mot("Each procedure was shown to cost its volume times a small factor, so the total is a sum of rows, one per procedure.", "recoverable"),
    [
        infer("S8.1.1", "Prefix-slot moves and individual butterfly rounds cost $dK$, a power $\\epsilon(1+c)$ of $p$.",
              r"Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\"),
        infer("S8.1.2", "Chunk exchanges for the transform layout cost $pK^{\\tau-1}$, a power $1-\\epsilon c(1-\\tau)$.",
              r"Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\"),
        infer("S8.1.3", "Simultaneous butterfly rounds cost $\\ell d^{\\lambda'}$, a power $1-\\epsilon(1-\\lambda')$.",
              r"Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\"),
        infer("S8.1.4", "CRT and axis layouts cost $d^2(1+\\ell^\\tau)$, a power $\\tau+\\epsilon(2-\\tau)$.",
              r"CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\"),
        infer("S8.1.5", "Gaussian line maps cost $dp^{1/2+\\delta}\\alpha$, a power $3/4+\\delta+3\\epsilon/2$.",
              r"Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\"),
        infer("S8.1.6", "Chirps, twists and scalar products cost $dp^\\delta$, a power $\\epsilon+\\delta$.",
              r"Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\"),
        infer("S8.1.7", "Packed polynomial products cost $\\log(rp)$, a power $1-\\epsilon$.",
              r"Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\"),
    ],
)

S8 = show(
    "S8",
    "Dividing each term of the cost by $Tp$ gives powers of $p$ with margins $g_i$ below one, the smallest being $2\\kappa$ with $\\kappa=2^{-182}$, which absorbs any polylogarithmic factor, so the whole algorithm runs in $O(n(\\lg n)^{1-\\kappa})$.",
    "tabulate each stage's cost per unit volume $Tp=\\Theta(n)$ as a power of $p$, compute its margin below one, and compare the smallest margin with $2\\kappa$",
    mot("This explicit slack will cover any remaining fixed power of $\\log p$.", "explicit",
        r"any remaining fixed power of $\log p$."),
    [
        H1,
        infer("S8.2", "The margins are $g_1=1-\\epsilon(1+c)$, $g_2=\\epsilon c(1-\\tau)$, $g_3=\\epsilon(1-\\lambda')$, $g_4$, $g_5$, $g_6$ and $g_7=\\epsilon$.",
              r"g_1&=1-\epsilon(1+c),\qquad"),
        infer("S8.3", "Direct substitution gives $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, and $g_7=2^{-75}$.",
              r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad"),
        infer("S8.4", "Thus $\\min_ig_i=2^{-181}=2\\kappa$.",
              r"Thus $\min_i g_i=2^{-181}=2\kappa$."),
        infer("S8.5", "Setup, prime search and descriptor work cost $o(Tp)$ because $r$ exceeds every fixed power of $p$.",
              r"costs at most $p^{A+C}=o(Tp)$."),
        infer("S8.6", "The sorting of exceptional records is a deterministic worst-case $o(V)$ bound.",
              r"a deterministic worst-case bound."),
        infer("S8.7", "Each of the seven displayed powers is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually.",
              r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
        infer("S8.8", "The complete large-input bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
              r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})."),
        infer("S8.9", "Using schoolbook multiplication below a fixed cutoff, the single fixed machine has worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every input length.",
              r"$O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely"),
    ],
    page="cost-accounting",
    frm=["size-parameters", "multiplication-algorithm", "transform-layout", "simultaneous-layer", "chunk-interchange", "retained-permutations", "signed-packing", "hvdh-multiplier", "asymptotic-notation-beyond-big-o", "logarithms-floors-and-ceilings"],
    salient="The exponent $\\kappa=2^{-182}$ is astronomically small, yet the saving is a genuine power of the logarithm, because every one of the seven cost terms has a margin below one of at least $2\\kappa$.",
)

# ---------------------------------------------------------------- root
ROOT = show(
    "S0",
    "A deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time, with $\\kappa=2^{-182}$.",
    "reduce the product to a convolution evaluated by Fourier-type transforms, make the two bottlenecks (address movement and butterfly layers) cheaper by recursive linear networks, then assemble the exact algorithm and total the cost",
    mot("Scanning an array at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both movement and arithmetic must be made cheaper.", "explicit",
        r"We therefore need savings in both movement and arithmetic."),
    [S1, S2, S3, S4, S5, S6, S7, S8],
    page="main-theorem",
    frm=["fixed-tape-model", "nlogn-conjecture", "big-o", "asymptotic-notation-beyond-big-o", "logarithms-floors-and-ceilings"],
    salient="The saving is a strict power of the logarithm, $(\\lg n)^{-\\kappa}$, even though $\\kappa=2^{-182}$ is astronomically small: the algorithm beats $n\\log n$ in the model where $n\\log n$ was conjectured optimal.",
)

out = {"root": ROOT}

# ------------------------------------------------------------ verification
def walk(n):
    yield n
    for c in n.get("children", []) or []:
        yield from walk(c)

pos = 0
ok = True
ids = set()
for n in walk(ROOT):
    assert n["id"] not in ids, n["id"]
    ids.add(n["id"])
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        cnt = SRC.count(q)
        if cnt == 0:
            print("MISSING", n["id"], repr(q)); ok = False; continue
        if cnt > 1:
            print("MULTI", n["id"], cnt, repr(q))
        if n.get("deferred"):
            continue
        i = SRC.find(q, pos)
        if i < 0:
            print("OUT OF ORDER", n["id"], repr(q), "first at", SRC.find(q), "pos", pos); ok = False
        else:
            pos = i + len(q)
    else:
        m = n["motivation"]
        if m.get("quote"):
            q = m["quote"]["quote"]
            if SRC.count(q) == 0:
                print("MISSING MOTIVATION QUOTE", n["id"], repr(q)); ok = False
pages = [n["page"] for n in walk(ROOT) if n.get("page")]
assert len(pages) == len(set(pages)), "dup page"
print("pages", len(pages))
print("ok" if ok else "PROBLEMS")
json.dump(out, open(BASE + "/exegenius/tasks/0044-argument.answer.json", "w"), indent=1, ensure_ascii=False)
