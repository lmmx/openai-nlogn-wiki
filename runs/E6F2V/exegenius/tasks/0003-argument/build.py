import json, sys

SRC = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F2V/sources/paper.tex', encoding='utf-8').read()

def ev(q):
    return {"source": "paper", "quote": q}

def mot(text, src, quote=None):
    m = {"text": text, "source": src}
    if quote is not None:
        m["quote"] = ev(quote)
    return m

def inf(id, claim, quote, page=None, frm=None, deferred=False, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": frm or []}
    if page: n["page"] = page
    if deferred: n["deferred"] = True
    if salient: n["salient"] = salient
    return n

def show(id, claim, method, motivation, children, page=None, frm=None, adds=None, salient=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children, "from": frm or []}
    if page: n["page"] = page
    if adds: n["adds"] = adds
    if salient: n["salient"] = salient
    return n

def add(symbol, name, meaning, relation):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

# ---------------------------------------------------------------- known concept ids
BIGO = 'big-o'
POLY = 'polynomials'
CPLX = 'complex-numbers'
TM = 'turing-machine-tapes'
MOD = 'modular-arithmetic-and-residues'
PRIME = 'primes-divisibility-gcd-and-coprimality'
BIN = 'binary-representation-of-integers'
XOR = 'bitwise-xor'
LOG = 'logarithms-floors-ceilings-and-powers-of-two'
MAT = 'matrices-invertibility-and-rank'
VEC = 'vector-spaces-basis-and-dimension'
PERM = 'permutations-and-permutation-matrices'
LEX = 'lexicographic-order-and-index-tuples'
EULER = 'euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle'
GEO = 'geometric-series-and-orthogonality-of-sums-of-roots-of-unity'
NORM = 'norms-and-the-triangle-inequality'
DYAD = 'rational-numbers-dyadic-rationals-and-exact-arithmetic'
ALG = 'algebraic-structures-groups-rings-and-isomorphisms'
PROOF = 'discrete-math-proof-techniques'
SCHOOL = 'schoolbook-multiplication-and-divide-and-conquer-multiplication'
SCAN = 'multitape-machine-cost-model-and-linear-time-scans'
EVAL = 'complex-polynomial-evaluation-and-interpolation'
GAUSS = 'gaussian-function'
CONV = 'convolution-as-polynomial-multiplication'
QUANT = 'quantifiers-sets-and-basic-asymptotic-notation-beyond-big-o'

# ---------------------------------------------------------------- G1: tape machinery
C1 = inf("S1.1", "A fixed permutation of two digits, a digit move, a pointwise map on split streams and a cyclic row split each cost $O(V)$ steps on an array of volume $V$.",
         r"volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
         page="stream-arrays", frm=["fixed-tape-model", LEX, SCAN, PERM])

C1b = inf("S1.2", "Adding to a later field an offset computed from earlier control fields modulo $q^b$, or multiplying it by a fixed unit, costs $O(V)$.",
          r"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
          page="controlled-shifts", frm=["stream-arrays", MOD, PRIME])

# --- S1.3: finite network with rank saving
gadget = show("S1.3.1",
    "A forward invocation of the three-element-subset gadget changes $y_S$ to $y_S+x_S$ and leaves everything else, including arbitrary scratch values, unchanged.",
    "compute the net linear map of gather, scatter and side injection after the scratch values are cancelled, and read off its coefficients by intersection size",
    mot("The net map does not depend on the scratch values, and its entry from $x_T$ to $y_S$ is a function of $|S\\cap T|$ only; so a small side correction can cancel exactly the unwanted intersection sizes.", "recoverable"),
    [
     inf("S1.3.1.1", "Rows 0-7 of the schedule leave the net target change $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$, independent of the initial scratch vectors.",
         r"Rows 6 and 7 restore $c,a$.  The net target change is"),
     inf("S1.3.1.2", "In the bit case the central coefficient from $x_T$ to $y_S$ is $|S\\cap T|\\bmod 2$.",
         r"In the bit case, the central coefficient from $x_T$ to $y_S$ is"),
     inf("S1.3.1.3", "The side contribution cancels the intersection-one cases; distinct triples of intersection zero or two already have coefficient zero and the self coefficient is one.",
         r"intersection-one cases; distinct triples with intersection zero or two"),
    ],
    page="triple-gadget", frm=[XOR, QUANT, PROOF, DYAD],
    salient="The coefficient of $x_T$ in $y_S$ depends only on the intersection size $|S\\cap T|$, and one extra set of side wires removes exactly the unwanted sizes.")

exchange = show("S1.3.2",
    "Three invocations (forward, reversed, forward) send $(X,Y)$ to $(-Y,X)$ and restore every scratch value.",
    "compose three shears of the gadget, the middle one reversed, and track a single pair $(x,y)$ through the stages",
    mot("A single invocation only adds one bank to the other; composing three of them with alternating direction is the classical way to build a swap from shears.", "reconstructed"),
    [
     inf("S1.3.2.1", "Starting from $(x,y)$ the three stages give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
         r"$X\gets X-Y$.  Starting from $(x,y)$, the three stages give"),
     inf("S1.3.2.2", "Each invocation restores its own auxiliary wires.",
         r"Each invocation restores its own auxiliary wires."),
    ],
    page="bank-exchange-network", frm=["triple-gadget", XOR],
    salient="The exchange produces a minus sign, $(X,Y)\\mapsto(-Y,X)$, rather than a plain swap; over bits the sign is invisible.")

frames = inf("S1.3.3",
    "Give every wire at every vertex an invertible frame $D_v$ on its address-indexed array; since pointwise linear gates commute with a shared frame, the network implements $D_{\\rm out}\\mathsf S D_{\\rm in}^{-1}$ and only edge changes cost anything.",
    r"the invariant continues to the sinks.  The implemented operator is therefore",
    page="frames", frm=["bank-exchange-network", MAT, PERM],
    salient="Every intermediate frame cancels: only the frames at the sources and sinks determine the final array operator.")

count = show("S1.3.4",
    "Nested labels make only the $Ic$ central edges decrease, with total loss $L<N/2$, so the total edge rank is $s_{\\rm b}=Wm-N+2L<Wm$.",
    "telescope signed dimension changes over the gates, add twice the loss on decreasing edges, and add one source rank for each of the $N$ negative source projections",
    mot("The deficit $Wm-s$ is a difference of two big quantities; the sources compute it exactly from dimension bookkeeping rather than estimating individual edges.", "recoverable"),
    [
     inf("S1.3.4.1", "The sum of absolute dimension changes over all edges is $Wm-2N+2L$, where $L$ is the total dimension lost on decreasing edges.",
         r"dimension $L$, the sum of absolute changes is $Wm-2N+2L$."),
     inf("S1.3.4.2", "Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing $h$.",
         r"Every edge joins comparable nondegenerate labels.  The only decreasing"),
     inf("S1.3.4.3", "The loss ratios are $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$, both below $1/2$.",
         r"In particular, both are smaller than $1/2$.  We now turn the dimension"),
     inf("S1.3.4.4", "Only the $N$ negative source projections cost one extra rank each.",
         r"The only exceptions are the $N$ negative source projections."),
     inf("S1.3.4.5", "The rank deficit from $Wm$ is $N-2L>0$, so $s<Wm$.",
         r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$."),
     inf("S1.3.4.6", "The endpoint matrices differ by $I_m$ on every input role, which is the shear $H\\gets H+D$.",
         r"For an input $X_a$ the endpoint difference is"),
     inf("S1.3.4.7", "Choosing $\\tau=1-2^{-50}$ gives $s/W<m^\\tau$ with $0<\\tau<1$.",
         r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,"),
    ])

C2 = show("S1.3",
    "A fixed linear network of $W$ wires exchanges two banks, restores all scratch values, and its edge changes have total rank $s<Wm$.",
    "build the exchange from a scalar gadget on three-element subsets, then attach nested subspaces of an $m$-dimensional space to gates and terminals and count the rank of the edge changes",
    mot("Labels are chosen so that an edge whose label grows needs only as many smaller operations as the dimension gained.", "explicit",
        r"choose its intermediate labels to make the changes of frame inexpensive."),
    [gadget, exchange, frames, count],
    page="subspace-labels", frm=["bilinear-orthogonal", "triple-gadget", "bank-exchange-network", "frames", VEC, MAT],
    adds=[add("W", "wire count", "The number of wires (roles, including scratch wires) of the fixed network.", "count"),
          add("m", "label dimension", "The dimension of the ambient label space, equal to the number of coordinates a shear mixes.", "count"),
          add("s", "total edge rank", "The sum over all edges of the rank of the matrix change across the edge, which is the number of smaller operations the network will need.", "count")],
    salient="The total rank $s$ is strictly below $Wm$, although only by a relative margin of about $10^{-11}$; that strict gap is the only property the later recursions use.")

# --- S1.4: chunk swap
tri = inf("S1.4.1",
    "Every rational square matrix of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation matrix with exactly $a$ ones.",
    r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization",
    page="triangular-factorization", frm=[MAT, PERM])

shear = show("S1.4.2",
    "The address update $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ costs exactly $\\operatorname{rank}(A)$ interchanges of pairs of $b$-digit fields plus $O(V)$ further work.",
    "conjugate the partial permutation core of the triangular factorization by triangular controlled shifts, and turn each one of the core into one interchange",
    mot("Triangular changes of coordinates only add earlier fields to later ones, which the controlled shifts do in linear time, so only the rank-many pivot entries are left to cost recursive work.", "recoverable"),
    [
     inf("S1.4.2.1", "A lower triangular transformation of the $H$ fields or of the $D$ fields costs $O(V)$.",
         r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
     inf("S1.4.2.2", "Transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\\Pi D$ to $H$, then undo the triangular changes.",
         r"For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,"),
     inf("S1.4.2.3", "Each one of $\\Pi$ is realized by two controlled shifts around one interchange, so $a$ ones cost $a$ interchanges.",
         r"It uses just one interchange.  There are $a$ ones, which proves the"),
    ],
    page="matrix-shear", frm=["triangular-factorization", "controlled-shifts", MOD])

key = show("S1.4.3",
    "Two chunks of $e=m^k$ radix-$q$ digits (with enough rows) are interchanged in $O(Ve^\\tau)$ time.",
    "run the bank-exchange network on $W$ role streams of volume $V/W$ with shear frames, so that each edge costs rank-many interchanges of $m$-fold narrower chunks, and solve the resulting recurrence for the cost per volume",
    mot("Each level makes $s$ recursive calls but each on a stream $W$ times smaller, so the cost per unit volume is multiplied by only $s/W$ per level while the width grows by the factor $m$.", "explicit",
        r"is the source of the power saving."),
    [
     show("S1.4.3.1",
          "One level of the recursion shears $H\\gets H+D$ on every row, using $W$ role streams of volume $V/W$ and the frame identity.",
          "split whole rows among the $W$ roles, apply the shear frame on each edge by smaller interchanges, run each gate pointwise, then merge the rows back",
          mot("The row split gives every role the same address set, which the common-frame identity needs; the identity then cancels all intermediate shears.", "recoverable"),
          [
           inf("S1.4.3.1.1", "Split whole rows cyclically into $W$ role streams, each of volume $V/W$.",
               r"Split whole rows cyclically into $W$ role streams within each prefix"),
           inf("S1.4.3.1.2", "Apply $\\Phi_{A_e}$ on each edge by recursively interchanging each pivot pair of $b$-digit fields, and execute each gate pointwise.",
               r"Lemma~\ref{lem:matrix-shear}, recursively interchanging each pivot pair"),
           inf("S1.4.3.1.3", "The result is $H\\gets H+D$ on every original row, including rows assigned to scratch roles with arbitrary contents.",
               r"is $H\leftarrow H+D$ on every original row, including rows assigned"),
          ]),
     inf("S1.4.3.2", "Interchanging the two full chunks takes $D\\gets D-H$, $H\\gets H+D$, $D\\gets H-D$, of which only the middle shear uses the circuit.",
         r"componentwise.  Only the middle shear uses the circuit.  The other two"),
     show("S1.4.3.3",
          "The cost per volume obeys $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
          "count the recursive calls of one level and divide their cost by the volume of the parent",
          mot("Dividing by the parent's volume turns the $s$ calls on streams of volume $V/W$ into one factor $s/W$.", "recoverable"),
          [
           inf("S1.4.3.3.1", "The number of recursive calls is the sum of the edge ranks, exactly $s$.",
               r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
           inf("S1.4.3.3.2", "Each call acts on one role stream of volume $V/W$ with other fields as spectators.",
               r"Each acts on one role stream of volume $V/W$, retaining all other"),
           inf("S1.4.3.3.3", "If $F_k$ bounds time per volume then $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
               r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."),
          ]),
     show("S1.4.3.4",
          "Since $a=s/W<m^\\tau$, the recurrence gives $F_k=O(e^\\tau)$.",
          "sum the geometric series of the recurrence, separating the cases $a\\le1$ and $a>1$",
          mot("The sum of the powers of $a=s/W$ is dominated by its last term when $a>1$; being below $m^\\tau$ makes that term at most $e^\\tau$.", "recoverable"),
          [
           inf("S1.4.3.4.1", "For $a=s/W<m^\\tau$ the geometric sum $\\sum_{j=0}^k a^j$ is $O(m^{k\\tau})$.",
               r"For $a=s/W<m^\tau$ the geometric sum"),
           inf("S1.4.3.4.2", "If $a\\le1$ the sum is at most $k+1=O(m^{k\\tau})$; if $a>1$ it is $O(a^k)$.",
               r"most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$."),
           inf("S1.4.3.4.3", "Hence $F_k=O(e^\\tau)$.",
               r"Hence $F_k=O(e^\tau)$."),
          ]),
     inf("S1.4.3.5", "On fixed tapes, the pushes, pops and copies of the depth-first schedule add only $O(V)$ per node, since there are $s$ child calls.",
         r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
    ],
    page="power-width-interchange",
    frm=["matrix-shear", "triangular-factorization", "subspace-labels", "frames", "bank-exchange-network", "stream-arrays", "fixed-tape-model", "controlled-shifts"],
    adds=[add("F_k", "normalized cost", "The time divided by the logical volume for interchanging chunks of $m^k$ digits.", "direct")],
    salient="The cost per volume is $O(e^\\tau)$ with $\\tau<1$ although every level makes $s$ recursive calls: each call is on a stream $W$ times smaller, so the branching factor per volume is $s/W<m$, strictly less than the factor $m$ by which the width grows.")

widen = show("S1.4.4",
    "Any two equal-width bit chunks, in any array, can be interchanged with no row restriction in $O(Vu^\\tau)$.",
    "move the top $\\rho=O(\\log e)$ digits of each chunk into a row field long enough for the splitting, pad the rows, and cut the remaining width into power-width pieces by its base-$m$ expansion",
    mot("The power-width procedure needs a row count divisible by a power of $W$ and a width $m^k$; a few high digits can supply the rows and the base-$m$ digits of the width supply the pieces, at a cost dominated by the main term.", "recoverable"),
    [
     inf("S1.4.4.1", "Write each chunk as its top $\\rho$ digits followed by the rest, exchange the high digits, and join them into a row field of range $R\\ge W^k$.",
         r"Write each chunk as its top $\rho$ digits followed by its remaining"),
     inf("S1.4.4.2", "Append zero rows until the row count is a multiple of $W^k$, at most doubling the volume.",
         r"Append zero rows, separately within"),
     inf("S1.4.4.3", "Write the remaining width $e-\\rho$ in base $m$ and interchange corresponding pieces with the power-width procedure.",
         r"Write the remaining width in base $m$:"),
     inf("S1.4.4.4", "The costs sum to $O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau)$.",
         r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)."),
     inf("S1.4.4.5", "Binary chunks are padded to the next width $q^e\\ge 2^u$, at a fixed-factor volume cost, and the padding is scanned away.",
         r"Finally, for binary chunks let $e$ be the least integer with"),
    ])

C3 = show("S1.4",
    "Two disjoint address chunks of $u$ bits in any bit array of volume $V$ are interchanged in $O(Vu^\\tau)$ steps for a fixed $\\tau<1$.",
    "obtain the interchange from three shears whose middle one runs through the rank-saving bit network recursively on power widths, then lift to arbitrary widths",
    mot("A swap of two chunks is three shears; the shear is exactly what the network with total rank $s<Wm$ computes cheaply by recursion on smaller chunks.", "explicit",
        r"$m$, the resulting recurrence saves a power of the chunk width."),
    [tri, shear, key, widen],
    page="chunk-swap", frm=["power-width-interchange", "stream-arrays", "controlled-shifts", "subspace-labels", XOR, PERM],
    salient="Although the final effect is an exact permutation, the intermediate steps form XOR combinations of data, which is why the rank saving is available.")

# --- S1.5: simultaneous butterfly layer
phase = show("S1.5.1",
    "The kernel $C=H\\mathsf SH=aI+bX$ satisfies $H_0=b\\mathsf SC\\mathsf S$, and the complex bank-exchange network with binary labels makes $C^{\\otimes m}$ on every role from translation kernels, one per residual basis vector.",
    "verify the identities for $C$ by direct multiplication and obtain the network's edge operators from Hamming weight modulo 4 on the binary labels",
    mot("The Gaussian-dyadic kernel $C$ can be built from the same rank-saving network, and a short identity then turns $C$ layers into the needed $H_0$ layers.", "reconstructed"),
    [
     inf("S1.5.1.1", "Each edge's phase-frame change is a product of one translation kernel $aI+bX_v$, or its inverse, per vector of an orthonormal basis of the edge residual.",
         r"kernel $aI+bX_v$, or its inverse, per vector in an orthonormal basis", deferred=True),
     inf("S1.5.1.2", "Telescoping these phase frames, after diagonal corrections and undoing the exchange, gives $C^{\\otimes m}$ on every role including scratch roles.",
         r"bank exchange, telescoping these phase frames gives $C^{\otimes m}$", deferred=True),
     inf("S1.5.1.3", "Direct multiplication gives $H_0=b\\mathsf SC\\mathsf S$, $C^2=X$, $C^4=I$ and $C^{-1}=bI+aX$.",
         r"H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad"),
    ],
    page="phase-kernel-network",
    frm=["bank-exchange-network", "subspace-labels", "bilinear-orthogonal", "frames", "butterfly-layers", MAT, CPLX, XOR],
    salient="The network yields exactly the tensor power $C^{\\otimes m}$ on every role, including roles carrying arbitrary scratch data.")

layerprep = show("S1.5.2",
    "A layer of $C^{\\otimes e}$ on $e=mf$ selected bits reduces to $s$ children on $f$ selected bits each, plus a fixed number of binary row additions and constant phases.",
    "write each edge's residual basis as the first columns of an invertible binary matrix, apply it by packed row additions, run one child kernel per basis vector, and undo the change of basis",
    mot("Directions of the edge residual are arbitrary vectors; moving them to coordinate positions by a change of basis lets each kernel act on a whole slot of selected bits at once.", "recoverable"),
    [
     inf("S1.5.2.1", "Apply the inverse change of basis to each column, one child $(C^{\\epsilon_h})^{\\otimes f}$ per residual direction on the $f$ bits in slot $h$, then the change of basis.",
         r"To implement \eqref{eq:phase-edge-coordinate} on the group, first apply"),
     inf("S1.5.2.2", "Any invertible binary matrix of fixed order is a product of a fixed number of elementary row additions.",
         r"Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$"),
     inf("S1.5.2.3", "The network on $e=mf$ axes uses exactly $s$ child calls, each on the $f=e/m$ axes of one slot.",
         r"$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
     inf("S1.5.2.4", "The normalized layer is $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$, with exact Gaussian dyadic phases and scalar.",
         r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D."),
    ])

packed = show("S1.5.3",
    "A row addition $y\\gets y\\oplus x$ on the selected bit of each of $f$ chunks is done at once, using a third chunk $z$ as temporary space restored for every initial value.",
    "do eight guarded cyclic shifts of whole chunk ranges that are correct away from a small set of bad addresses, then repair those addresses by a deterministic sort",
    mot("Several selected bits cannot be changed independently by shifts without carries across segments; guard bits make carries impossible except at a few addresses, which are rare enough to fix by sorting.", "recoverable"),
    [
     inf("S1.5.3.1", "Eight shifts, each controlled by the other chunk, flip the parity of $u$ exactly when $c=1$ and restore the auxiliary integer $w$.",
         r"We first construct eight rotations that have the required effect away"),
     inf("S1.5.3.2", "The bad addresses $\\mathcal B$ are those where some guard value leaves the interval $[10,2^{K-1}-11]$.",
         r"Let $\mathcal B$ consist of the addresses for which"),
     inf("S1.5.3.3", "Exactly twenty values of each guard are excluded, so $|\\mathcal B|\\le\\delta_{\\rm bad}M$ with $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$.",
         r"There are exactly twenty excluded values for each guard in"),
     inf("S1.5.3.4", "Extract the records at bad addresses with their destination ranks, sort them stably by key, and reinsert them, which implements the ideal map everywhere.",
         r"To implement the correction, scan the stream with a record-rank counter."),
     inf("S1.5.3.5", "The omitted most significant selected position is handled by a two-bit XOR.",
         r"Finally apply the two-bit XOR to $x_{j_{f-1}},y_{j_{f-1}}$ by"),
     inf("S1.5.3.6", "The total time is $O(V(L^\\tau+1))$ when the packed-record family bounds hold.",
         r"The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans"),
    ],
    page="packed-selected-bits",
    frm=["chunk-swap", "controlled-shifts", "stream-arrays", XOR, LOG],
    salient="A chunk holding arbitrary data serves as scratch space and is returned exactly, for every initial value, and the repair of the bad addresses depends only on addresses, not on payloads.")

recur = show("S1.5.4",
    "The cost per volume of a $C^{\\otimes e}$ layer satisfies $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$, which sums to $O(d^{\\lambda'})$ for $d$ chunks.",
    "split the rows among the $W$ roles, count $s$ children on streams of volume $V/W$, stop at $e<d^{1/2}$ and sum the recurrence, then cut $D$ chunks into base-$m$ groups",
    mot("The recursion has the same shape as for chunk interchange; its extra additive term is the cost of packed basis changes, which is polynomial in the chunk width $K$ and is small because $K$ is a small power of $d$.", "recoverable"),
    [
     inf("S1.5.4.1", "An individual $C$ kernel on a selected bit costs $O(V)$, so $e$ individual kernels cost $O(Ve)$.",
         r"To apply one \(C\) kernel, use the split from"),
     inf("S1.5.4.2", "The phase construction supplies one recursive call on a slot per residual basis vector, hence exactly $s$ calls.",
         r"The phase construction supplies one recursive call on a slot for each"),
     inf("S1.5.4.3", "Splitting row index $u=Wg+w$ across roles gives every role stream the same address shape and volume $V/W$.",
         r"At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\),"),
     inf("S1.5.4.4", "Stopping at $e<d^{\\beta}$ with $\\beta=1/2$, the cost per volume satisfies $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$.",
         r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
     inf("S1.5.4.5", "With $a=s/W\\le m^\\sigma<m^\\lambda$ the internal costs sum to $O(e^\\lambda)$.",
         r"Put \(a=s/W\).  Since \(a\le m^\sigma<m^\lambda\), the internal"),
     inf("S1.5.4.6", "Write $D-q_0$ in base $m$ and treat the pieces separately.",
         r"Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\)."),
     inf("S1.5.4.7", "Adding the pieces and row preprocessing gives $O(d^{\\lambda'})$ for any fixed $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$.",
         r"=O(d^{\lambda'})"),
    ])

guard = show("S1.5.5",
    "The whole layer is evaluated exactly in Gaussian dyadics with $o(p)$ guard bits, and only one truncation follows.",
    "bound the depth of additions and halvings along any chain in the recursion, which bounds both denominator and magnitude growth",
    mot("Each addition at most doubles a modulus and each halving adds a denominator bit, so a bound on the arithmetic depth gives the number of extra bits needed.", "recoverable"),
    [
     inf("S1.5.5.1", "The accelerated network is evaluated exactly until an entire normalized butterfly layer is complete; intermediate operators need not be contractions.",
         r"The accelerated network is evaluated exactly until an entire"),
     inf("S1.5.5.2", "Reserving $p+\\Delta$ fractional bits and $\\Delta+3$ integer bits represents every intermediate coefficient exactly, where $\\Delta=\\lceil C_0d^{C_1}\\rceil$.",
         r"Thus reserving \(p+\Delta\)"),
     inf("S1.5.5.3", "With $\\epsilon C_1<1$ the guard width is $o(p)$ and the full coefficient width is $O(p)$.",
         r"Choose \(\epsilon C_1<1\).  Since \(d=\Theta(p^\epsilon)\),"),
    ])

layer_final = inf("S1.5.6",
    "The procedure returns $Q_p(\\mathcal Hz)$ in $O(Vd^{\\lambda'})$ time, in the unit disk and with error below $\\sqrt2\\,2^{-p}$.",
    r"coefficient order, and component format in $O(Vd^{\lambda'})$ time,")

C4 = show("S1.5",
    "The tensor product $\\mathcal H$ of $H_0$ on one selected bit in each of $D\\le d$ address chunks of polynomial records is applied in $O(Vd^{\\lambda'})$ time with $\\lambda'<1$, exactly up to one final truncation.",
    "express $H_0^{\\otimes D}$ through the Gaussian-dyadic kernel $C^{\\otimes D}$, realize $C^{\\otimes e}$ by the rank-saving complex network recursively on slots using packed binary basis changes, and bound guard bits",
    mot("A layer on $D$ axes done one axis at a time costs $D$ passes; the network does all $D$ at once with a per-volume cost $d^{\\lambda'}$.", "explicit",
        r"whereas separate butterfly"),
    [phase, layerprep, packed, recur, guard, layer_final],
    page="simultaneous-butterfly-layer",
    frm=["phase-kernel-network", "packed-selected-bits", "chunk-swap", "power-width-interchange", "butterfly-layers", "fixed-point-disk-grid", "subspace-labels", "frames", CPLX, DYAD],
    adds=[add("K", "chunk width", "The number of address bits in each of the equal-width chunks that carry one selected bit.", "count")],
    salient="One layer on all $D$ axes costs only a power $d^{\\lambda'}$ with $\\lambda'<1$ of the axis count per unit volume, instead of $D$ whole-array passes.")

G1 = show("S1",
    "Two tape procedures cost a power of the width less than one per unit volume: interchange of two $u$-bit address chunks in $O(Vu^\\tau)$ and a simultaneous butterfly layer on $d$ chunks in $O(Vd^{\\lambda'})$.",
    "build the elementary scans and one fixed linear exchange network whose edges have total rank $s<Wm$, and derive from it two recursions in which each level multiplies the cost per volume by $s/W<m$",
    mot("One scan of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both data movement and butterfly arithmetic must be sped up.", "explicit",
        "We therefore need savings in both movement and arithmetic."),
    [C1, C1b, C2, C3, C4],
    adds=[add("V", "stored volume", "The number of stored data bits of the arrays an operation acts on.", "count"),
          add("\\tau", "interchange exponent", "A fixed exponent less than one such that interchanging two $u$-bit chunks costs a factor $u^\\tau$ per stored bit.", "direct")],
    frm=["fixed-tape-model", "stream-arrays"])

# ---------------------------------------------------------------- Synthetic transforms and ring convolution
syn = show("S2.1.1",
    "Over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ with roots $\\omega_t=y^{2r/t}$, the sum $\\sum_k\\omega_t^{jk}$ vanishes unless $t\\mid j$, so $F_t^+F_t^-=t^{-1}I$ despite zero divisors.",
    "pair the sum with a shifted copy of itself that equals its negative, and use that the additive group has no two-torsion",
    mot("In a ring with zero divisors one cannot divide by $\\omega_t^j-1$ to evaluate the geometric sum, so the cancellation is proved directly.", "explicit",
        r"The ring has zero divisors, so we verify character cancellation"),
    [
     inf("S2.1.1.1", "Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies their sum by $y^{rj_0}=-1$.",
         r"Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes"),
     inf("S2.1.1.2", "Hence the sum is zero, since the additive group of $\\mathcal R_r$ has no two-torsion.",
         r"$y^{rj_0}=-1$.  Hence the sum is zero, since the additive group of"),
    ],
    page="synthetic-transform", frm=["negacyclic-ring", "dft-cyclic-convolution", "multidim-transform", GEO, EULER],
    salient="Character cancellation $\\sum_k\\omega_t^{jk}=0$ holds in a ring with zero divisors because shifting the index multiplies the sum by $-1$.")

dif = show("S2.1.2",
    "Decimation in frequency computes $F_t^-$ by $H_0$ butterflies and monomial twiddles, leaves frequencies in bit-reversed order $B_t$, and the opposite procedure consumes that order directly.",
    "pair entries $k$ and $k+t/2$, apply the two-point butterfly and a twiddle monomial, recurse on the two halves, and read off where each frequency lands",
    mot("Keeping the output in bit-reversed order avoids a sort between the forward transform, the pointwise product and the opposite transform, which would cost a full pass per transform.", "recoverable"),
    [
     inf("S2.1.2.1", "Pair $z_k$ with $z_{k+t/2}$, apply $H_0$, multiply the second output by $\\omega_t^{-k}$, and recurse on both branches.",
         r"decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for"),
     inf("S2.1.2.2", "After all $a$ rounds, the named slots from high to low contain the frequency bits from low to high, so entry $j$ sits at $\\operatorname{rev}_a(j)$.",
         r"After all $a$ rounds, the named slots from high to low therefore"),
     inf("S2.1.2.3", "The reversed traversal is half the inverse of the forward level, so the two procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
         r"B_tF_t^-,\qquad F_t^+B_t^{-1},"),
     inf("S2.1.2.4", "For several axes the individual steps group into one parallel butterfly $\\mathcal H$ followed by one monomial $J_E$ depending only on the address.",
         r"Consequently the individual axis steps may be grouped as a parallel"),
    ],
    page="butterfly-layers", frm=["synthetic-transform", "dft-cyclic-convolution", "multidim-transform", "negacyclic-ring"])

layout = show("S2.1",
    "The forward synthetic transform on $d-1$ axes, with error below $\\sqrt2\\,\\ell\\,2^{-p}$, costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ and keeps its output order for the pointwise product and the opposite transform.",
    "choose a layout permutation that puts the selected bit of every axis at a common offset in consecutive $K$-bit chunks, so that each transform round is one simultaneous layer, and add up the costs",
    mot("The layer procedure needs the participating bits at equal offsets in equal-width chunks; a positional permutation made of chunk exchanges supplies that once for all rounds.", "recoverable"),
    [
     syn, dif,
     inf("S2.1.3", "Move the slots of the long axes and the low bits into a prefix; the remaining part of each axis is $q$ consecutive $K$-bit chunks.",
         r"Form a list of the slots to move to a prefix.  First list"),
     inf("S2.1.4", "Exchanging chunks to interleave the axes uses at most $Dq-1$ width-$K$ exchanges, costing $O(Tp\\,pK^{\\tau-1})$.",
         r"=O\bigl(Tp\,pK^{\tau-1}\bigr)."),
     inf("S2.1.5", "Each of the at most $\\ell$ rounds on the remaining chunks is one simultaneous layer, costing $O(Tpd^{\\lambda'})$, so $O(Tp\\ell d^{\\lambda'})$ in total.",
         r"$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total."),
     inf("S2.1.6", "The rounds on prefix slots are done bit by bit, at most $K$ of them, costing $O(TpdK)$.",
         r"most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$."),
     inf("S2.1.7", "Truncation commutes with the signed monomial shift, so a forward round returns the exact contraction truncated once.",
         r"J_EQ_p(\mathcal H z)=Q_p(J_E\mathcal H z)."),
     inf("S2.1.8", "At most $\\ell$ contractive rounds, each adding truncation error below $\\sqrt2\\,2^{-p}$, give error below $\\sqrt2\\,\\ell\\,2^{-p}$; layout permutations add none.",
         r"give the claimed error and disk bounds.  The layout permutations"),
     inf("S2.1.9", "The exact operators are $LBF_{\\boldsymbol t}^-$ for the forward procedure and $F_{\\boldsymbol t}^+B^{-1}L^{-1}$ for the opposite one.",
         r"(L\mathcal D_-L^{-1})L=LB F_{\boldsymbol t}^-,"),
    ],
    page="transform-layout",
    frm=["simultaneous-butterfly-layer", "chunk-swap", "butterfly-layers", "synthetic-transform", "multidim-transform", "stream-arrays", "fixed-point-disk-grid"],
    adds=[add("\\ell", "log record length", "The base-two logarithm of the record length $r$, the number of rounds of a transform.", "direct")])

kron = show("S2.2",
    "Two ring polynomials in $\\mathcal R_r$ are multiplied exactly, and the normalized product $fg/r$ is returned truncated, in $O(rp\\log(rp))$ time.",
    "evaluate the integer parts of the coefficients at the large power of two $B_0=2^{4p}$, multiply the resulting integers with the established multiplier, and read the signed product coefficients back by centered carries",
    mot("Integer multiplication is the one fast product available; evaluating at a power of two larger than any coefficient turns a polynomial product into an integer product and the coefficients can be read back digit by digit.", "reconstructed"),
    [
     inf("S2.2.1", "Set $B_0=2^{4p}$ and evaluate the real and imaginary integer parts $a,b,c,e$ of the inputs at $B_0$.",
         r"where $a,b,c,e\in\mathbb Z[y]$ have degree less than $r$ and"),
     inf("S2.2.2", "Every coefficient of an ordinary product satisfies $|h_j|\\le r2^{2p}<B_0/2$, so centered residues identify them.",
         r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
     inf("S2.2.3", "Extract the coefficients block by block with a constant-size carry, using the centered representative modulo $B_0$.",
         r"Put $\rho_0=0$.  At block $j$, let $\widehat h_j$ be the unique"),
     inf("S2.2.4", "Combine the real and imaginary streams and reduce modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$.",
         r"The real and imaginary numerator streams are respectively"),
     inf("S2.2.5", "Four exact integer products dominate the linear packing, extraction and truncation costs.",
         r"Four exact integer products dominate the linear"),
    ],
    page="signed-kronecker-packing",
    frm=["negacyclic-ring", "nlogn-subroutine", POLY, CONV, "radix-digit-convolution"])

ringconv = show("S2",
    "Normalized convolution over $\\mathcal R_r$ on $d-1$ axes, computed from two forward synthetic transforms, pointwise ring products and the opposite transform in the same frequency order, has error $O(M\\ell 2^{-p})$ and cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
    "transform both operands, multiply pointwise in the retained order, apply the opposite transform, rescale exactly, and bound the errors with the bilinear contraction property",
    mot("Pointwise multiplication commutes with the same record permutation on both operands, so no unsorting is needed between the transforms.", "explicit",
        r"Pointwise multiplication commutes with applying the same record"),
    [
     layout, kron,
     inf("S2.3", "Perform both forward transforms, retain their common $LB$ order, multiply pointwise by signed packing, apply the opposite procedure to that order, and multiply exactly by $M=T/r$.",
         r"Perform both forward transforms and retain their common $LB$ order."),
     inf("S2.4", "The identity $MF_{\\boldsymbol t}^+\\bigl((F_{\\boldsymbol t}^-f)(F_{\\boldsymbol t}^-g)/r\\bigr)=(f*g)/(rM)$ holds exactly.",
         r"F_{\boldsymbol t}^-(f*g)"),
     inf("S2.5", "Since $LB$ permutes records and leaves polynomial suffixes intact, the opposite transform of the pointwise product of stored outputs equals the exact result.",
         r"Since $LB$ permutes records and leaves their polynomial suffixes"),
     inf("S2.6", "The final exact multiplication by $M$ gives error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
         r"The final exact multiplication by $M$ therefore gives error less than"),
     inf("S2.7", "The $M=T/r$ pointwise polynomial products cost $O(Tp\\log(rp))$ in total.",
         r"There are $M=T/r$ pointwise polynomial products.  Their total cost"),
    ],
    page="ring-convolution",
    frm=["transform-layout", "signed-kronecker-packing", "synthetic-transform", "dft-cyclic-convolution", "fixed-point-disk-grid", "negacyclic-ring", NORM],
    adds=[add("T", "total record coefficients", "The total number of complex coefficients $T=rM$ in the padded array, with $M$ records of $r$ coefficients each.", "count")])

# ---------------------------------------------------------------- Resampling and assembly
resamp = show("S3.1",
    "Gaussian resampling gives $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ in one dimension and $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ on $d$ axes, with the permutations $R$ and $Q$ left inside the transform.",
    "keep the coordinate permutations in the transform identity of Harvey and van der Hoeven's resampling, bound the numerical maps $A$ and $B_0$, and tensor them line by line",
    mot("The usual implementation sorts twice per coordinate; leaving the permutations in the identity avoids those sorts, and later they cancel or are absorbed.", "explicit",
        "coordinate. We retain both permutations in the transform formula and"),
    [
     inf("S3.1.1", "For coprime $s<t$ with $t/s-1>p/\\alpha^4$ there are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and $B_0:\\mathbb C^t\\to\\mathbb C^s$.",
         r"There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and"),
     inf("S3.1.2", "They satisfy $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$.",
         r"P_sF_s=2^{2\alpha^2}B_0P_tF_tA."),
     inf("S3.1.3", "Their disk-grid approximations have error below $p^2$ and cost $O(tp^{3/2+\\delta}\\alpha)$.",
         r"O(tp^{3/2+\delta}\alpha)."),
     inf("S3.1.4", "The Gaussian identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ and the estimate $\\|N-I\\|<2^{-\\alpha^2\\theta}$ give an invertible $N$.",
         r"\mathsf T P_sF_s=P_tF_t\mathsf S,"),
     inf("S3.1.5", "Setting $A=\\mathsf S/2$ and $B_0=\\mathsf D'\\mathsf J'C$ makes both contractions.",
         r"Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$."),
     inf("S3.1.6", "Tensoring the one-dimensional identity gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$.",
         r"Tensoring \eqref{eq:no-sort-one-dimensional} proves"),
     inf("S3.1.7", "At most $T/t_i$ lines are processed per axis, for total time $O(dTp^{3/2+\\delta}\\alpha)$.",
         r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$,"),
     inf("S3.1.8", "Exposing and restoring all axes in the padded box costs $O(Tpd^2(1+\\ell^\\tau))$ by chunk interchanges.",
         r"$O(Tp(1+\ell^\tau))$. Exposing and restoring one axis needs"),
    ],
    page="resampling-no-sort",
    frm=["gaussian-resampling", "dft-cyclic-convolution", "multidim-transform", "fixed-point-disk-grid", "chunk-swap", "nlogn-subroutine", GAUSS, NORM],
    adds=[add("s", "source length", "A prime length of one axis of the source transform, with $s<t$.", "direct"),
          add("t", "padded length", "The power-of-two length of one axis of the padded array, coprime to the source length.", "direct"),
          add("\\alpha", "resampling width", "The integer controlling the width of the Gaussian windows in the resampling maps.", "direct")])

chirp = show("S3.2",
    "The chirp formula $QF_{\\boldsymbol t}u=\\overline a\\cdot\\bigl(a*(\\overline a\\cdot u)\\bigr)/T$ leaves $Q$ unexecuted, and $R$ cancels: $(RF_{\\boldsymbol s}^+)[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
    "expand the coefficient of each input entry for the chirp, and for the cancellation commute the permutation past the opposite transform and use the convolution rule",
    mot("The target permutation is absorbed into a Bluestein chirp so it is never executed, and the source permutation commutes through the product so it cancels between the forward and opposite transforms.", "recoverable"),
    [
     inf("S3.2.1", "The chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$ has period $t_i$ in each coordinate and gives the chirp convolution formula for $QF_{\\boldsymbol t}$.",
         r"QF_{\boldsymbol t}u"),
     inf("S3.2.2", "The coefficient of $u_{\\boldsymbol k}$ is $\\frac1T\\exp(2\\pi i\\sum_i s_ij_ik_i/t_i)$, which is the entry of $QF_{\\boldsymbol t}$.",
         r"=\frac1T\exp\left(2\pi i\sum_i"),
     inf("S3.2.3", "Dilation by a unit commutes with $F^+$ up to inverse, so $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$.",
         r"$F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence"),
     inf("S3.2.4", "The normalizations give $F_{\\boldsymbol s}^+(F_{\\boldsymbol s}u\\cdot F_{\\boldsymbol s}v)=(u*v)/S^2$.",
         r"=\frac{u*v}{S^2},"),
    ],
    page="chirp-permutation-cancel",
    frm=["bluestein-chirp", "resampling-no-sort", "multidim-transform", "dft-cyclic-convolution", CPLX, EULER],
    salient="The permutation $R$ appears on both forward transforms but not in the result, because a unit dilation commutes with the inverse-sign transform and with pointwise products.")

params = show("S3.3",
    "Fix $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, a padded size $T\\in[4n/b,8n/b)$, record length $r$, power-of-two axis lengths $t_i$ and distinct odd primes $s_i$ just below $t_i$, so that $Tp=\\Theta(n)$ and all interface hypotheses hold.",
    "choose each size as an explicit rational power of $b$, then check the hypotheses of the resampling, layer and transform interfaces one by one, using the prime-interval estimate for the source lengths",
    mot("Every interface asks for a different growth condition on $d$, $r$, $K$ and $\\alpha$; fixing explicit exponents lets all of them be verified at once.", "recoverable"),
    [
     inf("S3.3.1", "The fixed rational exponents are chosen with $\\kappa=2^{-182}$.",
         r"C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}."),
     inf("S3.3.2", "Put $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$ and $K=\\lfloor d^c\\rfloor$.",
         r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,"),
     inf("S3.3.3", "Take the power of two $T$ in $[4n/b,8n/b)$ and choose axis lengths $t_i\\in\\{r/2,r\\}$ with $\\prod_it_i=T$.",
         r"Take the power of two $T$ in $[4n/b,8n/b)$, and let"),
     inf("S3.3.4", "These give $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$ and $r=2^{\\Theta(p^{1-\\epsilon})}$.",
         r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad"),
     inf("S3.3.5", "Set $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$ and $\\gamma=2d\\alpha^2$, so that $\\gamma=o(b)$.",
         r"\alpha=\left\lceil(12d^2b)^{1/4}\right\rceil,"),
     inf("S3.3.6", "The interval $(1-2\\eta)x<q\\le(1-\\eta)x$ contains many primes, enough for distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$.",
         r"(1-2\eta)t_i<s_i\leq(1-\eta)t_i."),
     inf("S3.3.7", "Then $T/2<S<T$ for $S=\\prod_is_i$.",
         r"Together with $s_i<t_i$, this gives $T/2<S<T$."),
     inf("S3.3.8", "Every hypothesis of the one-dimensional resampling lemma holds for all sufficiently large $n$.",
         r"Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for"),
     inf("S3.3.9", "The deterministic prime search takes $n^{o(1)}=o(n)$ time.",
         r"Since $p=6\lceil\log_2 n\rceil=\Theta(\log n)$, the search takes"),
     inf("S3.3.10", "The product of the radix-$2^b$ digit polynomials has degree below $S$, so convolution modulo $x^S-1$ has no wraparound.",
         r"Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
    ],
    page="parameter-choice",
    frm=["resampling-no-sort", "simultaneous-butterfly-layer", "transform-layout", "ring-convolution", "radix-digit-convolution", "fixed-point-disk-grid", PRIME, LOG],
    adds=[add("b", "digit width", "The number of bits per radix digit, $\\lceil\\log_2 n\\rceil$.", "count"),
          add("p", "precision", "The number of fractional bits of the fixed-point numbers, equal to $6b$.", "count"),
          add("d", "axis count", "The number of axes of the transform arrays, about $b^\\epsilon$.", "count"),
          add("S", "convolution length", "The product of the distinct prime axis lengths $s_i$, larger than the degree of the digit-polynomial product.", "direct")])

crt = show("S3.4",
    "The map $x\\mapsto\\prod_ix_i^{\\mu_i}$ is an algebra isomorphism sending one cyclic convolution of length $S=s_1\\cdots s_d$ to a convolution on $d$ prime cyclic axes, implemented by triangular controlled cyclic shifts.",
    "show the map is well defined and bijective on monomials by the Chinese remainder theorem, and write the new coordinates as a lower-triangular function of the mixed-radix digits so that controlled shifts apply",
    mot("Controlled shifts add earlier fields to later ones in linear time, so the address map must be triangular in physical order.", "recoverable"),
    [
     inf("S3.4.1", "The assignment respects $x^S=1$, so it defines an algebra map between the group algebras.",
         r"respects $x^S=1$, so it defines an algebra map.  The target monomial"),
     inf("S3.4.2", "The image of $x$ has order $S$, so $\\Phi$ is an isomorphism and preserves cyclic convolution.",
         r"$\Phi$ is an isomorphism and preserves cyclic convolution."),
     inf("S3.4.3", "In mixed-radix digits $a_j$, the coordinate in axis $i$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}$.",
         r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}."),
     inf("S3.4.4", "Updating the targets for $i=d,\\dots,1$ gives prefix-controlled cyclic shifts that keep zero padding zero.",
         r"Each triangular update is a prefix-controlled cyclic shift.  The"),
     inf("S3.4.5", "The map, its inverse and their padding operations cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
         r"uses $O(d^2)$ such moves.  Therefore the map $\Phi$, its inverse, and"),
    ],
    page="crt-axis-map",
    frm=["controlled-shifts", "chunk-swap", "radix-digit-convolution", "dft-cyclic-convolution", "multidim-transform", PRIME, MOD, ALG])

twist = show("S3.5.1",
    "Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ is a ring isomorphism from $\\mathbb C[x]/(x^r-1)$ to $\\mathcal R_r$, so the negative wrap becomes the cyclic wrap after untwisting.",
    "check the map is well defined, diagonal in the monomial bases, and compare the sign of a wrapped product term",
    mot("A twist by a root of $-1$ turns the sign in the negacyclic reduction into the identity needed for cyclic reduction.", "recoverable"),
    [
     inf("S3.5.1.1", "The map $x_d\\mapsto\\zeta y$ is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.",
         r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."),
     inf("S3.5.1.2", "A wrapped term after twisting and negacyclic reduction has factor $\\zeta^{k+l}(-1)^h=\\zeta^j$.",
         r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j."),
    ],
    page="coefficient-twist", frm=["negacyclic-ring", "fixed-point-disk-grid", ALG, EULER],
    salient="The factor $(\\zeta^r)^h(-1)^h$ equals $1$ for $h\\in\\{0,1\\}$: the twist root $\\zeta=e^{\\pi i/r}$ is chosen so that $\\zeta^r=-1$ exactly cancels the negacyclic sign.")

srct = show("S3.5",
    "The computed source transform $\\widetilde{\\mathscr F}$ (Gaussian maps $A$, a chirp transform evaluated by a twisted ring convolution, then $B_0$ and exact scaling by $2^\\gamma$) has exact counterpart $RF_{\\boldsymbol s}$.",
    "evaluate the middle factor $QF_{\\boldsymbol t}$ by the chirp formula, whose convolution is a complex convolution obtained from the ring convolution by the coefficient twist, and compose with the resampling maps",
    mot("The power-of-two transform $QF_{\\boldsymbol t}$ in the resampling identity is a chirp convolution; the cyclic convolution on the last axis is made negacyclic by the twist so that the ring convolution applies.", "recoverable"),
    [
     twist,
     inf("S3.5.2", "The computed complex convolution twists both inputs, applies the ring convolution, and untwists, with each phase product truncated to the grid.",
         r"h'&=\widetilde{\mathcal M}_r(\iota f',\iota g'),"),
     inf("S3.5.3", "The computed chirp transform multiplies by $\\overline{\\widetilde a}$, convolves with $\\widetilde a$, and multiplies by $\\overline{\\widetilde a}$ again.",
         r"x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),"),
     inf("S3.5.4", "The source transform applies $\\mathcal A$, the chirp transform, $\\mathcal B_0$, and an exact scaling by $2^\\gamma$.",
         r"For a source disk-grid tensor of norm at most $.5$, write"),
     inf("S3.5.5", "Its exact counterpart is $\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$.",
         r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A"),
    ],
    page="source-transform",
    frm=["resampling-no-sort", "chirp-permutation-cancel", "coefficient-twist", "ring-convolution", "parameter-choice", "gaussian-resampling", "bluestein-chirp", "fixed-point-disk-grid", "multidim-transform"])

G3 = show("S3",
    "Convolution of the radix digits modulo $x^S-1$ is reduced to the power-of-two ring convolution by Gaussian resampling, the Bluestein chirp, the Chinese-remainder axis map and a coefficient twist.",
    "retain the resampling permutations inside the transform identity, absorb the middle transform into a chirp convolution, fix all sizes, move the digit list onto prime axes, and twist the last axis into the ring",
    mot("The synthetic transforms only exist for power-of-two lengths, whereas the digit convolution on pairwise coprime lengths has no wraparound; Gaussian resampling connects the two shapes.", "explicit",
        r"connects these two shapes."),
    [resamp, chirp, params, crt, srct],
    frm=["radix-digit-convolution", "gaussian-resampling", "bluestein-chirp", "dft-cyclic-convolution"])

# ---------------------------------------------------------------- algorithm, recovery, cost
algo = show("S4",
    "The algorithm splits the inputs into radix digits, maps them by $\\Phi$ to prime axes, takes two source transforms, multiplies pointwise, applies the opposite-sign transform with two scalings by $S$, rounds, undoes $\\Phi$ and propagates carries.",
    "list the steps in order and explain the two uses of $S$ and $2^{2b+4}$ as undoing known normalizations",
    mot("By the cancellation identity the three transforms give $(u*v)/S^2$, and the known scalings restore the integer coefficient convolution.", "explicit",
        r"The two occurrences of $S$ in this algorithm undo different"),
    [
     inf("S4.1", "Read each operand in groups of $b$ bits to get $q$ radix-$2^b$ digits and write each as an exact grid value $a_j2^{-b-2}$.",
         r"its least significant end in groups of $b$ bits. This produces the radix-$2^b$ digits"),
     inf("S4.2", "Apply the coefficient-address map $\\Phi$ with its padded layout to obtain the source arrays $u,v$.",
         r"\item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain"),
     inf("S4.3", "Compute $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$.",
         r"\item Compute $\widetilde{\mathscr F}(u)$ and"),
     inf("S4.4", "Multiply the two transforms pointwise, exactly, and truncate to $p$ fractional bits to get $z$.",
         r"\item Multiply corresponding complex coefficients exactly and truncate"),
     inf("S4.5", "Apply $\\widetilde{\\mathscr F}^+(z)$ and scale by $S$.",
         r"\item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid"),
     inf("S4.6", "Scale by $2^{2b+4}S$, round to the nearest integers, and undo $\\Phi$ to restore the ordinary coefficient order.",
         r"\item Multiply the grid numerators of $\widetilde w$ exactly by"),
     inf("S4.7", "Propagate radix-$2^b$ carries and output exactly $2n$ bits.",
         r"\item Propagate radix-$2^b$ carries in increasing coefficient order."),
    ],
    page="multiplication-algorithm",
    frm=["crt-axis-map", "source-transform", "chirp-permutation-cancel", "radix-digit-convolution", "parameter-choice", "exact-recovery"] if False else ["crt-axis-map", "source-transform", "chirp-permutation-cancel", "radix-digit-convolution", "parameter-choice", "fixed-point-disk-grid"])

errors = show("S5.1",
    "Every computed array stays in the disk, and the error of each computed transform adds up predictably: $E_s=9\\cdot2^\\gamma TL$ for the source transform and $E_w<28\\cdot2^\\gamma T^2L$ after the scaling by $S$.",
    "propagate errors through contractions and bilinear contractions, inserting the exact map at the computed input at each step",
    mot("All maps are contractions on the disk, so an input error is never amplified and the errors of consecutive stages simply add.", "explicit",
        r"A linear contraction propagates an input error without increasing it."),
    [
     inf("S5.1.1", "The returned normalized ring convolution has error below $E_{\\rm ring}=M(3L+2)<5TL$ in units of $2^{-p}$.",
         r"less than $3L+2$.  Thus the error of the returned normalized"),
     inf("S5.1.2", "The complex convolution has error below $6TL\\,2^{-p}$.",
         r"<(E_{\rm ring}+4+4+4)h_p<6TLh_p."),
     inf("S5.1.3", "The chirp transform has error below $8TL\\,2^{-p}$.",
         r"<(6TL+2+4+4)h_p<8TLh_p."),
     inf("S5.1.4", "The source transform has error below $E_s2^{-p}$ with $E_s=9\\cdot2^\\gamma TL$.",
         r"E_s=9\,2^\gamma TL,"),
     inf("S5.1.5", "The product $z=Q_p(\\widetilde U\\cdot\\widetilde V_1)$ has error below $(2E_s+2)2^{-p}$.",
         r"Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$."),
     inf("S5.1.6", "After the opposite transform and the scaling by $S$, $\\widetilde w$ approximates $(u*v)/S$ with error below $E_w2^{-p}$, $E_w<28\\cdot2^\\gamma T^2L$.",
         r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
    ],
    frm=["fixed-point-disk-grid", NORM])

recovery = show("S5",
    "After removing the known normalizations $S$ and $2^{2b+4}$, the error in every recovered coefficient is below $1/2$, so rounding gives the exact convolution coefficients, and radix-$2^b$ carries give the $2n$-bit product.",
    "bound the accumulated error through each stage by contractions, check it is below $1/2$ after the final scaling, round, and propagate carries with a recurrence whose invariant fixes the digits",
    mot("The true coefficients are integers, so any error strictly below $1/2$ identifies them uniquely by rounding.", "explicit",
        r"The strict error below $1/2$ makes the nearest integer to"),
    [
     errors,
     inf("S5.2", "The unscaled integer coefficient array is $2^{2b+4}Sw$, where $S$ reverses the normalization of $w$ and $2^{2b+4}$ reverses the two input scales.",
         r"In tensor order, the unscaled integer coefficient array is"),
     inf("S5.3", "The final absolute error is below $448b\\,2^{-b+\\gamma}\\le448b\\,2^{-3b/4}<1/2$.",
         r"\le448b\,2^{-3b/4}<\frac12."),
     inf("S5.4", "The nearest integer to each represented coefficient is therefore the exact convolution coefficient, in $[0,2^{3b})$.",
         r"The strict error below $1/2$ makes the nearest integer to"),
     inf("S5.5", "The carries obey $0\\le k_j\\le q(Q_0-1)<Q_0^2$ with $Q_0=2^b$ and the invariant $\\sum_{h<j}c_hQ_0^h=\\sum_{h<j}d_hQ_0^h+k_jQ_0^j$.",
         r"The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$."),
     inf("S5.6", "The exact product is below $2^{2n}$, so after removing zero padding exactly $2n$ bits remain.",
         r"than $2^{2n}$; all bits above position $2n-1$ are therefore zero."),
    ],
    page="exact-recovery",
    frm=["fixed-point-disk-grid", "chirp-permutation-cancel", "source-transform", "parameter-choice", NORM, DYAD],
    salient="The final error bound $448\\,b\\,2^{-3b/4}$ is far below $1/2$ because the working precision $p=6b$ exceeds the scales $2^{2b+4}S\\,2^{\\gamma}T^2$ by a margin of order $2^{3b/4}$; the loss $2^\\gamma$ with $\\gamma=o(b)$ is what resampling costs.")

cost = show("S6",
    "Divided by $Tp$, each cost in the table is at most $p^{1-2\\kappa}$, because the smallest of seven margins below one is $2^{-181}=2\\kappa$, giving $O(n(\\log n)^{1-\\kappa})$ overall.",
    "tabulate the cost of each operation per stored bit as a power of $p$, compute the margin of each dominant power below one, and absorb logarithmic factors into the slack",
    mot("Every procedure has already been bounded per unit volume; the total is a sum of these normalized costs with a fixed number of repetitions, so only their exponents need to be compared.", "recoverable"),
    [
     inf("S6.1", "Table of costs divided by $V=Tp=\\Theta(n)$, where a fixed number of repeated transforms is included in the constants.",
         r"Table~\ref{tab:costs} lists costs after division"),
     inf("S6.6", "The seven dominant margins are $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$ and $g_7=2^{-75}$.",
         r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad"),
     inf("S6.7", "Thus $\\min_ig_i=2^{-181}=2\\kappa$.",
         r"Thus $\min_i g_i=2^{-181}=2\kappa$."),
     inf("S6.2", "The prefix-slot moves, the chunk exchanges for layout and the simultaneous rounds are the three terms of the transform cost.",
         r"The first three rows are the terms in"),
     inf("S6.3", "Axis exposure and restoration require $O(d^2)$ adjacent axis moves, each costing $O(V(1+\\ell^\\tau))$.",
         r"Axis exposure and restoration require $O(d^2)$ adjacent axis moves."),
     inf("S6.4", "The Gaussian line machines sum to $O(dTp^{3/2+\\delta}\\alpha)$.",
         r"For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines."),
     inf("S6.5", "Chirp construction, twists and scalar products cost $O(dp^{1+\\delta})$ per entry.",
         r"Chirp numerators have $O(p)$ bits and can be computed modulo $2r$ as"),
     inf("S6.8", "Setup, prime search and compact exceptional sorts cost $o(V)$ in total.",
         r"Global setup and prime search cost $o(V)$, as"),
     inf("S6.9", "Each of the seven powers is at most $1-2\\kappa$ and any fixed power of $\\log p$ is at most $p^\\kappa$, so the bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
         r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
     inf("S6.10", "Using schoolbook multiplication below a fixed cutoff, the single machine has worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every input length.",
         r"With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single"),
    ],
    page="cost-accounting",
    frm=["parameter-choice", "simultaneous-butterfly-layer", "chunk-swap", "transform-layout", "resampling-no-sort", "ring-convolution", "multiplication-algorithm", "exact-recovery", BIGO, LOG, QUANT],
    adds=[add("\\kappa", "saving exponent", "The constant $2^{-182}$ such that the cost is $O(n(\\lg n)^{1-\\kappa})$.", "direct")],
    salient="The saving exponent $\\kappa=2^{-182}$ is half the smallest margin $2^{-181}$, which comes from $g_2=\\epsilon c(1-\\tau)$: a product of the three tiny exponents $\\epsilon=2^{-75}$, $c=2^{-56}$ and $1-\\tau=2^{-50}$.")

R0 = inf("S0.1",
    "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.",
    r"convolution of short integer coefficients.",
    frm=["radix-digit-convolution", CONV, POLY, BIN])

ROOT = show("S0",
    "A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$.",
    "start from the Gaussian-resampling reduction of multiplication to transforms, make the transforms cheaper by two tape procedures that each save a power of the logarithm, then recover the product exactly and add up all costs",
    mot("Scanning the whole array at each of the $\\Theta(\\log n)$ transform levels costs $\\Theta(n\\log n)$, so a power saving needs savings in both data movement and arithmetic.", "explicit",
        "We therefore need savings in both movement and arithmetic."),
    [R0, G1, ringconv, G3, algo, recovery, cost],
    page="main-theorem",
    frm=["n-log-n-conjecture", "fixed-tape-model", "nlogn-subroutine", "radix-digit-convolution", SCHOOL, BIGO, TM],
    adds=[add("n", "input length", "The number of bits of each of the two integers to multiply.", "count")])

answer = {"root": ROOT}
json.dump(answer, open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F2V/exegenius/tasks/0003-argument.answer.json', 'w'), indent=1, ensure_ascii=False)

# ---------------------------------------------------------------- local checks
PAGES = """n-log-n-conjecture radix-digit-convolution triple-gadget bank-exchange-network fixed-tape-model nlogn-subroutine stream-arrays frames controlled-shifts bilinear-orthogonal subspace-labels triangular-factorization matrix-shear power-width-interchange chunk-swap packed-selected-bits negacyclic-ring signed-kronecker-packing fixed-point-disk-grid dft-cyclic-convolution multidim-transform crt-axis-map gaussian-resampling bluestein-chirp coefficient-twist synthetic-transform butterfly-layers phase-kernel-network simultaneous-butterfly-layer transform-layout ring-convolution resampling-no-sort chirp-permutation-cancel parameter-choice source-transform exact-recovery multiplication-algorithm cost-accounting main-theorem""".split()
KNOWN = {BIGO, POLY, CPLX, TM, MOD, PRIME, BIN, XOR, LOG, MAT, VEC, PERM, LEX, EULER, GEO, NORM, DYAD, ALG, PROOF, SCHOOL, SCAN, EVAL, GAUSS, CONV, QUANT}
idx = {p: i for i, p in enumerate(PAGES)}
errs = []
ids = set()
usedpages = {}
fromused = set()
last = -1
def walk(n, curpage):
    global last
    if n['id'] in ids: errs.append('dup id ' + n['id'])
    ids.add(n['id'])
    pg = n.get('page') or curpage
    if n.get('page'):
        if n['page'] in usedpages: errs.append('page reused ' + n['page'])
        usedpages[n['page']] = n['id']
    for f in n.get('from', []):
        fromused.add(f)
        if f in KNOWN: continue
        if f not in idx: errs.append('bad from %s in %s' % (f, n['id'])); continue
        if idx[f] >= idx[pg]: errs.append('from %s not before page %s in %s' % (f, pg, n['id']))
    if n['intention'] == 'infer':
        q = n['quote']['quote']
        c = SRC.count(q)
        if c != 1: errs.append('quote count %d in %s: %r' % (c, n['id'], q))
        else:
            pos = SRC.index(q)
            if not n.get('deferred'):
                if pos < last: errs.append('order violation at %s pos %d < %d' % (n['id'], pos, last))
                last = max(last, pos + len(q))
    else:
        m = n['motivation']
        if m['source'] == 'explicit':
            q = m['quote']['quote']
            if SRC.count(q) < 1: errs.append('motivation quote missing in ' + n['id'] + ': ' + q)
        for ch in n['children']:
            walk(ch, pg)
        for a in n.get('adds', []):
            sym = a['symbol']
            found = False
            def dsc(x):
                nonlocal_found = []
                for ch in x.get('children', []):
                    nonlocal_found.append(ch['claim'])
                    nonlocal_found += dsc(ch)
                return nonlocal_found
            import re
            for cl in dsc(n):
                for mm in re.findall(r'\$(.*?)\$', cl):
                    if sym in mm: found = True
            if not found: errs.append('add symbol %s not found in descendants of %s' % (sym, n['id']))
walk(ROOT, None)
for p in PAGES:
    if p not in usedpages and p not in fromused:
        errs.append('page neither used nor in from: ' + p)
print('\n'.join(errs) if errs else 'local checks ok')
