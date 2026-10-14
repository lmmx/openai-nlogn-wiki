import json, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SRC = open(os.path.join(PROJ, 'sources', 'paper.tex')).read()


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


NSRC = norm(SRC)


def ev(q):
    return {"source": "paper", "quote": q}


def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


def infer(id, claim, quote, frm=None, page=None, deferred=None, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote)}
    if page:
        n["page"] = page
    if frm:
        n["from"] = frm
    if deferred:
        n["deferred"] = True
    if salient:
        n["salient"] = salient
    return n


def show(id, claim, method, mot_text, mot_source, children, mot_quote=None,
         frm=None, page=None, salient=None, adds=None):
    mot = {"text": mot_text, "source": mot_source}
    if mot_quote:
        mot["quote"] = ev(mot_quote)
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": mot}
    if page:
        n["page"] = page
    if frm:
        n["from"] = frm
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = adds
    n["children"] = children
    return n


# ---------------------------------------------------------------- tape procedures
S1_1 = infer(
    "S1.1",
    "On an array of logical volume $V$ stored in lexicographic order, a fixed permutation of the digits at two radix-$q$ positions, moving one digit, splitting on a digit to apply a fixed pointwise map and merging back, and cyclically splitting whole rows into a fixed number of streams (and merging them) each cost $O(V)$ steps.",
    "Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
    frm=["multitape-turing-machine", "multidimensional-arrays-and-row-major-order",
         "positional-notation-in-any-radix", "big-o-notation"],
    page="tape-address-model")

S1_2 = infer(
    "S1.2",
    "If a target field $y\\in[Q]$, $Q=q^b$, follows its control fields, the update $y\\mapsto y+a(\\text{controls})\\bmod Q$ costs $O(V)$ whenever the offset is computable in $b^{O(1)}$ time, by splitting each fiber's $Q$ blocks at $Q-a$ and merging the two pieces in the opposite order; multiplying $y$ by a fixed rational unit also costs $O(V)$.",
    "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the fixed number of control values.",
    frm=["tape-address-model", "modular-arithmetic", "cyclic-shifts-and-rotations-of-lists"],
    page="controlled-cyclic-shift")

# ---- key step
K1 = show(
    "S1.3.1",
    "For arbitrary initial scratch values, a forward invocation of the eight-row schedule (copy, gather, scatter, side injection and their undoings) effects $y\\gets y+x$, and a forward, an inverse and a forward stage send $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ while restoring every auxiliary wire; over $\\mathbb F_2$ this is the bank exchange.",
    "Track the old scratch vectors through the schedule, compute the net coefficient from each $x_T$ to $y_S$ from the size of $S\\cap T$, and compose the three stages.",
    "The schedule first cancels the effect of the unknown scratch contents and finally restores them, so the net effect is a fixed linear map that can be computed as if the scratch were zero; only its coefficients, which depend on triple intersections, remain to be checked.",
    "explicit",
    [
        infer("S1.3.1.1",
              "With initial side and central vectors $a,c$, rows 0 and 1 subtract $\\mathcal Ja+\\mathcal Rc$, rows 2 to 5 add $\\mathcal R(c+\\mathcal Gx)+\\mathcal J(a+\\mathcal Vx)$ and rows 6 and 7 restore $a,c$, so the target changes by $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$ whatever $a,c$ are.",
              "The net target change is $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$, independently of $a,c$."),
        infer("S1.3.1.2",
              "In the bit construction the central (gather then scatter) coefficient from $x_T$ to $y_S$ is $|S\\cap T|\\bmod 2$; the side wires cancel exactly the neighbours with $|S\\cap T|=1$, triples meeting in $0$ or $2$ points already have coefficient $0$, and the self coefficient ($|S\\cap S|=3$) is $1$, so the net map is $y\\gets y+x$.",
              "The side contribution cancels exactly the intersection-one cases; distinct triples with intersection zero or two already have coefficient zero, and the self coefficient is one."),
        infer("S1.3.1.3",
              "In the complex construction the central coefficient is $(|S\\cap T|-1)/2$; the side wires cancel it for distinct triples meeting in $0$ or $2$ points, intersection one contributes $0$, and the self coefficient is $(3-1)/2=1$, so again $y\\gets y+x$.",
              "The side cancels it for distinct triples with intersection zero or two; intersection one contributes zero, and the self coefficient is one."),
        infer("S1.3.1.4",
              "Since the inverse schedule effects $X\\gets X-Y$, the three stages take $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$, and each invocation restores its own auxiliary wires.",
              "Starting from $(x,y)$, the three stages give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$."),
    ],
    mot_quote="The first two rows of the following schedule remove the effect of the old scratch values;",
    frm=["arithmetic-modulo-2-and-xor", "sets-subsets-and-cartesian-products",
         "matrices-vectors-and-linear-maps"],
    page="scratch-restoring-exchange",
    salient="The exchange is exact for arbitrary, unknown initial scratch values, so scratch roles can later be filled with genuine data rows instead of reserved blank space.")

K2 = show(
    "S1.3.2",
    "If each wire's scalar is replaced by an array on a common address set and each vertex $v$ gets an invertible frame $D_v$, shared by all incidences of a gate, with $D_vD_u^{-1}$ applied on each edge, then the pointwise network implements $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$: a route from input role $w$ to output role $\\rho(w)$ applies only $\\varepsilon_wD_{\\mathrm{sink}(\\rho(w))}D_{\\mathrm{source}(w)}^{-1}$.",
    "Maintain the invariant that the stored array at each vertex is its frame applied to the logical array, and verify it at sources, along edges and through gates.",
    "A gate combines values at one address while a frame mixes addresses within one wire, so a shared frame commutes with the gate by linearity; hence intermediate frames telescope and can be chosen freely to make edges cheap.",
    "recoverable",
    [
        infer("S1.3.2.1",
              "At a gate whose touched wires all carry frame $D_v$, linearity gives $\\sum_jc_jD_v\\varphi_j=D_v(\\sum_jc_j\\varphi_j)$, so the invariant passes through every gate to the sinks.",
              "Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks."),
        infer("S1.3.2.2",
              "Consequently, for a signed role permutation, every route, auxiliary roles included, applies its sign times the endpoint operator $D_{\\mathrm{sink}(\\rho(w))}D_{\\mathrm{source}(w)}^{-1}$, and the intermediate frames are free.",
              "Once the scalar routing is fixed, the endpoint frames determine the array operator on each route; the intermediate frames can then be chosen to make each edge change inexpensive."),
    ],
    frm=["scratch-restoring-exchange", "tape-address-model", "matrices-vectors-and-linear-maps"],
    page="array-frames")

K3 = show(
    "S1.3.3",
    "Each vertex can be labelled by a nondegenerate subspace of $\\mathcal F=F^{\\otimes3}$, of dimension $m$, so that the labels on every edge are nested and the absolute label-dimension changes over all edges sum to $Wm-2N+2L$, where the dimension $L$ lost on decreasing edges satisfies $L/N=100/539$ (bit network) or $101/539$ (complex network), both below $1/2$.",
    "Build labels from tensor products of indicator lines of three-element subsets of $[100]$, verify nesting along each edge from the orthogonality of neighbouring triples, and telescope the signed dimension changes at the gates.",
    "Neighbouring triples have orthogonal indicator lines in the chosen bilinear form, so one triple's line fits inside the other's orthogonal complement; this lets almost every edge only enlarge its label, confining all losses to the central wires.",
    "explicit",
    [
        infer("S1.3.3.1",
              "For the form $\\langle x,y\\rangle=x^{\\mathsf T}(I-J/9)y$ on $\\mathbb Q^{100}$ (nondegenerate, eigenvalues $1$ and $-91/9$) indicator vectors of triples satisfy $\\langle t_S,t_T\\rangle=|S\\cap T|-1$ and $\\langle t_T,t_T\\rangle=2$, and over $\\mathbb F_2$ the dot product gives $t_T\\cdot t_T=1$ and $t_S\\cdot t_T=|S\\cap T|\\bmod2$; so triple lines are nondegenerate and neighbouring ones orthogonal in either label field.",
              "Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label field belonging to either construction.",
              frm=["dot-product-inner-product-and-orthogonality", "rank-and-orthogonal-subspaces"]),
        infer("S1.3.3.2",
              "The terminal labels are $U_a=\\langle u_a\\rangle$ at source $X_a$ and $0$ at every other source, and $\\mathcal F$ at sinks $X_a$ and scratch, $U_a^\\perp$ (dimension $m-1$) at sinks $Y_a$; so the source dimensions sum to $N$ and the sink dimensions to $Wm-N$.",
              "The source dimensions sum to $N$ and the sink dimensions to $Wm-N$."),
        infer("S1.3.3.3",
              "On a side wire joining neighbouring triples with indicators $t_X,t_Y$, the varying label component passes through $\\langle t_X\\rangle\\subset t_Y^\\perp\\subset F$ (tensored with fixed factors), which is possible precisely because $t_X\\perp t_Y$.",
              "The first inclusion is possible because $t_X\\perp t_Y$."),
        infer("S1.3.3.4",
              "Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h=100$, so $L$ is $100$ times the number of central wires over all invocations.",
              "The only decreasing edges are the central-wire edges from time 3 to time 4; their dimension loss is $h$."),
        infer("S1.3.3.5",
              "Signed changes telescope at each gate, since each touched wire enters and leaves it with the same gate label, so they sum to $(Wm-N)-N=Wm-2N$; turning the signed losses on decreasing edges into absolute values adds $2L$.",
              "The signed sum of dimension changes telescopes at every gate: each touched wire has one incoming and one outgoing incidence with the same gate label."),
        infer("S1.3.3.6",
              "Over $\\mathbb F_2$ every nonzero edge residual (orthogonal complement of the smaller label in the larger) contains a vector of norm one, so it is nondegenerate and nonalternating and therefore has an orthonormal basis.",
              "Thus every nonzero residual is nonalternating."),
        infer("S1.3.3.7",
              "The exact loss ratios are $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$, both smaller than $1/2$.",
              "In particular, both are smaller than $1/2$."),
    ],
    mot_quote="Orthogonality of the corresponding indicator vectors permits the subspace assignments.",
    frm=["rank-and-orthogonal-subspaces", "scratch-restoring-exchange", "array-frames",
         "sets-subsets-and-cartesian-products", "dot-product-inner-product-and-orthogonality"],
    page="subset-intersection-labels")

K4 = show(
    "S1.3.4",
    "In the bit network, assigning the projection $P_U$ (onto $U$ along $U^\\perp$) to each gate or sink with label $U$, $-P_{U_a}$ to source $X_a$ and $0$ to other sources gives $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m$ on every role and total edge rank $s=s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$.",
    "Read off the rank of each edge difference of projections from the label dimensions, and add the exceptional first edges at the sources separately.",
    "For nested nondegenerate labels the difference of the two projections is itself a projection whose rank is the dimension change, so the label budget transfers to ranks, except on the edges where the negative source projection breaks this rule.",
    "recoverable",
    [
        infer("S1.3.4.1",
              "For nondegenerate $U\\subset V$, $P_V-P_U$ is the identity on $V\\cap U^\\perp$ and zero on its orthogonal complement, so its rank equals $\\dim V-\\dim U$, and reversing the edge only negates it.",
              "Its rank is $\\dim V-\\dim U$; reversing the edge negates the matrix without changing its rank."),
        infer("S1.3.4.2",
              "The exceptions are the $N$ negative source projections: at stage 1 the first gate on $X_a$ has label $U_a$, so its first edge matrix is $P_{U_a}-(-P_{U_a})=2P_{U_a}$, of rank one where the dimension change is zero, adding $N$ to the rank sum.",
              "Its first edge matrix is therefore $2P_{U_a}$, of rational rank one, where the corresponding dimension change was zero."),
        infer("S1.3.4.3",
              "Hence $s_{\\rm b}=(W_{\\rm b}m-2N+2L_{\\rm b})+N$, whose deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$ because $L_{\\rm b}<N/2$.",
              "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$."),
        infer("S1.3.4.4",
              "The negative source matrix is what makes the endpoint uniform: on $X_a$ the endpoint difference is $P_{U_a^\\perp}+P_{U_a}=I_m$, and every other role has zero source and identity sink matrix.",
              "For an input $X_a$ the endpoint difference is $P_{U_a^\\perp}-(-P_{U_a})=I_m$."),
    ],
    frm=["rank-and-orthogonal-subspaces", "subset-intersection-labels", "array-frames",
         "matrices-vectors-and-linear-maps"])

K5 = show(
    "S1.3.5",
    "In the complex network with binary labels and phase frames $\\mathcal C_U=H^{\\otimes m}\\operatorname{diag}_x(i^{\\operatorname{wt}(P_Ux)\\bmod 4})H^{\\otimes m}$, each edge's frame change is a product of one translation kernel $aI+bX_v$ or its inverse per vector $v$ of an orthonormal basis of the edge residual, so the network needs $s=s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}<W_{\\rm c}m$ kernels in all.",
    "Show that Hamming weight modulo four is additive over orthogonal binary vectors, so the phase of a residual factors into one two-valued character per orthonormal basis vector, and conjugate each character by Hadamard matrices into a translation kernel.",
    "The phase $i^{\\operatorname{wt}(P_Ux)}$ splits along an orthogonal decomposition only if weights add modulo four, which holds exactly when supports meet evenly, i.e. for orthogonal binary vectors; that is why orthonormal residual bases give one kernel per unit of dimension.",
    "recoverable",
    [
        infer("S1.3.5.1",
              "Because $\\operatorname{wt}(z+w)=\\operatorname{wt}(z)+\\operatorname{wt}(w)-2|\\operatorname{supp}(z)\\cap\\operatorname{supp}(w)|$, weight is additive modulo $4$ when $z\\cdot w=0$, so $q_V-q_U$ is a sum of one term $\\operatorname{wt}(v)[v\\cdot x]$ per orthonormal basis vector of the residual.",
              "If $z\\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four."),
        infer("S1.3.5.2",
              "Each basis vector has odd weight, so it contributes a phase $i^{\\pm[v\\cdot x]}=\\frac{1+i^{\\pm1}}2+\\frac{1-i^{\\pm1}}2(-1)^{v\\cdot x}$, and $H\\operatorname{diag}(1,-1)H=X$ turns it into $aI+bX_v$ or its inverse.",
              "The displayed phase therefore becomes $aI+bX_v$ or its inverse."),
        infer("S1.3.5.3",
              "A zero residual uses the empty basis, so the kernel count equals the absolute label budget $W_{\\rm c}m-2N+2L_{\\rm c}$ with no exceptional source term, a deficit of $2N-2L_{\\rm c}>0$.",
              "The deficit is $2N-2L_{\\rm c}>0$."),
    ],
    frm=["subset-intersection-labels", "array-frames", "complex-numbers",
         "arithmetic-modulo-2-and-xor", "roots-of-unity-and-euler-s-formula"])

K6 = infer(
    "S1.3.6",
    "The relative deficits $1-s_{\\rm b}/(W_{\\rm b}m)=339/22587335000000$ and $1-s_{\\rm c}/(W_{\\rm c}m)=73/19906842167500$ both exceed $20\\cdot2^{-50}$, and $m<2^{20}$ gives $\\log m<20$, so $m^{1-2^{-50}}>m(1-20\\cdot2^{-50})$ and hence $s_{\\rm b}/W_{\\rm b}<m^{\\tau}$ and $s_{\\rm c}/W_{\\rm c}<m^{\\sigma}$ with $\\tau=\\sigma=1-2^{-50}$.",
    "Both exact deficits displayed above are greater than $20\\cdot2^{-50}$.",
    frm=["exponential-logarithm-and-gaussian-function"])

K7 = show(
    "S1.3.7",
    "For a fixed rational $m\\times m$ matrix $A$ of rank $a$ and two groups of $m$ fields over $\\mathbb Z/q^b\\mathbb Z$ ($q$ a fixed odd prime avoiding all denominators), with every $H_i$ before every $D_j$, the shear $(H,D)\\mapsto(H+AD,D)$ costs exactly $a$ interchanges of $b$-digit field pairs plus $O(V)$ work, so each edge of the bit network costs as many smaller interchanges as its rank.",
    "Factor $A=E_1\\Pi E_2$ with invertible lower-triangular $E_1,E_2$ and a partial permutation $\\Pi$ with $a$ ones, apply the triangular factors as linear-time controlled shifts, and realise each one of $\\Pi$ by a single interchange between two controlled updates.",
    "Controlled shifts are linear-time only when the target field follows its controls, which is exactly what a lower-triangular change of coordinates needs; the factorization pushes all non-triangular work into the $a$ ones of $\\Pi$.",
    "explicit",
    [
        infer("S1.3.7.1",
              "Eliminating from the topmost nonzero row with its rightmost nonzero pivot uses only lower-triangular operations and isolates one rank-one block per step, giving $A=E_1\\Pi E_2$ with exactly $a$ ones in $\\Pi$ (a Bruhat factorization in reversed coordinate order).",
              "Each step isolates a rank-one block and leaves the remaining rank in the active submatrix."),
        infer("S1.3.7.2",
              "A lower-triangular transformation of $H$ or of $D$ costs $O(V)$: update coordinates in descending physical order, each by a unit multiple plus a fixed combination of earlier, still unchanged coordinates.",
              "A lower triangular transformation of $H$, or of $D$, costs $O(V)$: update coordinates in descending physical order."),
        infer("S1.3.7.3",
              "Each one of $\\Pi$ at $(i,j)$, i.e. $H_i\\gets H_i+D_j$, is done as $D_j\\gets D_j+H_i$, one interchange of $(H_i,D_j)$, and $D_j\\gets H_i-D_j$, so the number of recursive interchanges is exactly the rank $a$.",
              "In particular, the number of recursive calls is the rational rank $a$; temporary tapes used for the other operations do not multiply that count."),
    ],
    mot_quote="Lower triangular changes of coordinates can be performed entirely in this direction.",
    frm=["controlled-cyclic-shift", "triangular-and-permutation-matrices",
         "rank-and-orthogonal-subspaces", "primes-coprimality-and-gcd"],
    page="address-shear-factorization")

KEY = show(
    "S1.3",
    "Two fixed linear networks with $W$ wires each exchange two banks of $N$ values while restoring every scratch value, and their frame changes need in total only $s<Wm$ smaller calls on role streams of volume $V/W$, indeed $s/W<m^{\\tau}$ with $\\tau=1-2^{-50}$; so when the recursion parameter is multiplied by $m$ the volume-normalized cost is multiplied by less than $m^{\\tau}$, a power saving.",
    "Label every vertex of each network by a subspace of an $m$-dimensional space, count the dimension changes along edges, convert them into rational ranks (bit network) or orthonormal residual bases (complex network), and compare the total with $Wm$.",
    "A recursion that replaces one call at parameter $mf$ by $s$ calls at parameter $f$, each on volume $V/W$, multiplies the normalized cost by $s/W$ per factor $m$; only a strict deficit $s<Wm$ makes this factor $m^{\\tau}$ with $\\tau<1$, so the exact count of edge ranks decides whether any saving exists.",
    "explicit",
    [K1, K2, K3, K4, K5, K6, K7],
    mot_quote="This strict inequality is the source of the power saving.",
    frm=["subset-intersection-labels", "array-frames", "address-shear-factorization",
         "scratch-restoring-exchange", "rank-and-orthogonal-subspaces",
         "divide-and-conquer-and-recurrences"],
    page="rank-saving-recurrence",
    salient="The relative deficit $1-s/(Wm)$ is minute (about $1.5\\cdot10^{-11}$ for the bit network), yet any strict deficit already yields a power saving.",
    adds=[
        B("W", "wire count", "The number of wires (roles) of the network, scratch wires included, which is also the number of role streams the rows are split into.", "count"),
        B("m", "label dimension", "The dimension $100^3$ of the label space, which is also the number of digit fields or slots a chunk is cut into at each recursion level."),
        B("s", "total edge rank", "The number of smaller recursive calls the network's edges need: the sum of edge ranks or residual dimensions.", "count"),
        B("N", "bank size", "The number of index triples $a$, i.e. of values in each of the two exchanged banks.", "count"),
        B("L", "dimension loss", "The total label dimension lost along decreasing edges of the network."),
    ])

# ---- address chunk interchange
A1 = show(
    "S1.4.1",
    "If $s/W<m^{\\tau}$, two disjoint chunks of $e=m^k$ radix-$q$ digits each, preceded by a row field whose length is divisible by $W^k$, can be interchanged in $O(Ve^{\\tau})$ time on a fixed number of tapes, preserving all other fields.",
    "Split whole rows cyclically into $W$ role streams, run the bit network with frames $\\Phi_M:(H,D)\\mapsto(H+MD,D)$ so that every role ends with the shear $H\\gets H+D$, implement each edge shear by recursive interchanges of $e/m$-digit fields, and solve the recurrence $F_k\\le(s/W)F_{k-1}+O(1)$.",
    "Splitting whole rows gives all role streams the same address set, which the frame identity needs, and makes every recursive call act on only $1/W$ of the volume, so the rank count $s$ enters the cost only through $s/W$.",
    "explicit",
    [
        infer("S1.4.1.1",
              "Cyclically splitting whole rows into $W$ role streams within each prefix gives streams with the same remaining shape, including full ranges of $H$ and $D$, each of logical volume $V/W$ and with row count divisible by $W^{k-1}$.",
              "Each has logical volume $V/W$, and its row count is divisible by $W^{k-1}$."),
        infer("S1.4.1.2",
              "Since $\\Phi_{M'}\\Phi_M=\\Phi_{M'+M}$ commutes with pointwise XOR gates, the frame identity and $M_{\\mathrm{out}(\\rho(w))}-M_{\\mathrm{in}(w)}=I_m$ give $\\Phi_{I_m}$, i.e. $H\\gets H+D$, on every original row after merging, scratch rows with arbitrary contents included.",
              "The result is $H\\leftarrow H+D$ on every original row, including rows assigned to scratch roles, whose initial values were arbitrary."),
        infer("S1.4.1.3",
              "The updates $D\\gets D-H$, $H\\gets H+D$, $D\\gets H-D$ interchange the chunks; only the middle shear uses the network, the other two are linear-time controlled updates.",
              "The transformation sends $(H,D)$ to $(D,H)$."),
        infer("S1.4.1.4",
              "The node makes exactly $s$ recursive calls (the sum of edge ranks), each on a role stream of volume $V/W$, plus $O(V)$ work, so $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
              "The number of recursive calls is the sum of the edge ranks, exactly $s$."),
        infer("S1.4.1.5",
              "With $s/W<m^{\\tau}$ the geometric sum $\\sum_{j\\le k}(s/W)^j$ is $O(m^{k\\tau})$, whether $s/W\\le1$ or not, so $F_k=O(e^{\\tau})$.",
              "Hence $F_k=O(e^\\tau)$."),
        infer("S1.4.1.6",
              "Parking the inactive role streams on a stack and reusing the same tapes at every depth costs $O(V)$ per node, so temporary storage does not enter the factor $s/W$.",
              "Temporary storage is therefore not substituted for logical volume in the factor $s/W$."),
    ],
    mot_quote="The row split supplies the common address set used in the frame identity~\\eqref{eq:common-frame-identity}.",
    frm=["rank-saving-recurrence", "address-shear-factorization", "array-frames",
         "tape-address-model", "geometric-series-and-sums", "divide-and-conquer-and-recurrences"],
    page="power-width-interchange")

A2 = show(
    "S1.4.2",
    "For chunks of $e$ radix-$q$ digits, borrowing the top $O(\\log e)$ digits of both chunks as a row field of range at least $W^k$, padding the row count, and splitting the remaining width into base-$m$ pieces gives an interchange in $O(Ve^{\\tau})$; padding binary ranges $[2^u]$ to $[q^e]$ then gives $O(Vu^{\\tau})$.",
    "Exchange and join the high digits to form rows, apply the power-width interchange to each base-$m$ piece, then undo the joins, the row padding and the radix padding.",
    "The power-width procedure needs a row field and widths that are powers of $m$; high digits supply rows at only $O(V\\log e)$ movement cost, and a base-$m$ expansion with digits below $m$ makes the piece costs a geometric sum dominated by its top term.",
    "recoverable",
    [
        infer("S1.4.2.1",
              "Exchanging and joining the high digits costs $O(V\\log e)$, and padding the row count to a multiple of $W^k$ less than doubles the volume.",
              "Exchanging and joining the high parts costs $O(V\\rho)$ by Lemma~\\ref{lem:elementary-streams}."),
        infer("S1.4.2.2",
              "Writing the remaining width as $\\sum_ja_jm^j$ with $a_j<m$, the pieces cost $O(V)\\sum_ja_jm^{j\\tau}=O(Ve^{\\tau})$ because $m^k<me$.",
              "The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a geometric sum of the stated order."),
        infer("S1.4.2.3",
              "Padding each binary range $[2^u]$ to $[q^e]$ with $q^e\\ge2^u$ preserves order and raises the volume by less than the fixed factor $q^2$, and $e=O(u)$, so the interchange costs $O(Vu^{\\tau})$.",
              "Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\\tau)$."),
    ],
    frm=["power-width-interchange", "tape-address-model", "geometric-series-and-sums",
         "positional-notation-in-any-radix"])

A = show(
    "S1.4",
    "One fixed-tape procedure transforms any bit array on $[P]\\times[2^u]\\times[G]\\times[2^u]\\times[B]$ by $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$ in $O(Vu^{\\tau})$ steps, with $\\tau=1-2^{-50}$.",
    "Prove the bound for power widths with enough rows by running the bit network on role streams, then supply rows from high digits, split a general width into base-$m$ pieces, and pad binary chunks to radix $q$.",
    "The network recursion needs a row field divisible by $W^k$ and widths that are powers of $m$; borrowing a few high digits as rows and summing base-$m$ pieces meets both requirements at a cost below the final bound.",
    "explicit",
    [A1, A2],
    mot_quote="Rows for a general array can be supplied by a few of its own high digits.",
    frm=["power-width-interchange", "rank-saving-recurrence", "tape-address-model",
         "geometric-series-and-sums"],
    page="address-chunk-interchange",
    salient="The final effect is an exact permutation of addresses, yet the procedure forms XOR combinations of the data along the way, and that is what lets it beat moving the $u$ bits one at a time.")

# ---- simultaneous butterfly layer
B1 = show(
    "S1.5.1",
    "On a group of $e=mf$ selected bits arranged in $m$ slots of $f$ bits, the complex network with phase frames applies $C^{\\otimes e}$, where $C=aI+bX$ with $a=(1+i)/2$, $b=(1-i)/2$, on every role using exactly $s_{\\rm c}$ forward child calls on the $f$ bits of one slot plus a fixed number of binary row additions and exact Gaussian-dyadic scalar operations; and $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$ recovers the normalized butterflies.",
    "Conjugate each edge's product of translation kernels by an invertible binary change of basis so that the kernels act on whole slots, turn inverse kernels into forward ones with $Z$ signs and fourth-root phases, and telescope the frames to $C^{\\otimes m}$ on every role.",
    "A translation kernel in a general direction $v$ is not a slot operation, but after a basis change that makes $v$ a coordinate vector it acts on one slot, where it is a smaller instance of the same layer; the basis change itself only XORs address bits.",
    "recoverable",
    [
        infer("S1.5.1.1",
              "By the complex interface, an edge frame change is $\\prod_j(aI+bX_{v_j})^{\\epsilon_j}$ over an orthonormal basis of its residual, so the number of directional kernels is the residual dimension, also on decreasing edges.",
              "The number of directional kernels is precisely $\\rho_{\\rm edge}$, including on decreasing edges."),
        infer("S1.5.1.2",
              "Taking an invertible binary matrix $M$ whose first columns are the basis vectors, $\\mathcal P_MX_v\\mathcal P_M^{-1}=X_{Mv}$ turns the edge into slot kernels conjugated by $\\mathcal P_M$, which uses only invertibility of $M$, not orthogonality.",
              "The matrix $M$ need not preserve the dot product: equation~\\eqref{eq:phase-conjugation} only uses its invertibility."),
        infer("S1.5.1.3",
              "An inverse kernel still costs one forward child, because $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$ with $Z=\\operatorname{diag}(1,-1)$.",
              "A negative directional kernel still requires only one forward child, because"),
        infer("S1.5.1.4",
              "Gaussian elimination writes $\\mathcal P_M$ as at most $m(m-1)+3m$ row additions, and one row addition XORs corresponding selected bits of two whole slots.",
              "Thus one row addition changes corresponding selected positions in two whole slots."),
        infer("S1.5.1.5",
              "With the source and sink $Z$ signs, the scalar $i^{27f}$ and negation of the physical $X$ bank, the network gives $C^{\\otimes e}$ on every role from exactly $s_{\\rm c}$ children on $e/m$ axes, scratch roles included.",
              "Proposition~\\ref{prop:complex-motif-interface} therefore gives $C^{\\otimes e}$ on every role, including roles whose initial scratch values were arbitrary."),
        infer("S1.5.1.6",
              "Since $H_0=b\\mathsf SC\\mathsf S$ with $\\mathsf S=\\operatorname{diag}(1,i)$, the normalized layer is $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$, where $b^D=(-i/2)^{\\lfloor D/2\\rfloor}b^{D\\bmod2}$ is a shift and a fourth-root phase with at most one factor $b$.",
              "so it is a binary shift and fourth-root phase, with at most one further factor $b$."),
    ],
    frm=["subset-intersection-labels", "array-frames", "fixed-point-complex-arithmetic",
         "rank-saving-recurrence", "complex-numbers"],
    page="phase-frame-network")

B2 = show(
    "S1.5.2",
    "For three disjoint $L$-bit chunks $x,y,z$ of $R$-bit records, $L=fK$, the XORs $y_{j_i}\\gets y_{j_i}\\oplus x_{j_i}$ at the positions $j_i=\\rho+iK$ ($0\\le i<f$) are performed while restoring $z$ and every payload, in time $O(V(L^{\\tau}+1))$ when $R$ exceeds every fixed power of $p$ and $K/\\log p\\to\\infty$.",
    "Realise all $f$ XORs by eight whole-chunk cyclic shifts that flip parities of $K$-bit segments, show these agree with the ideal map outside an explicit set $\\mathcal B$ of guard-violating addresses, and repair $\\mathcal B$ deterministically by extracting and sorting its records.",
    "Whole-chunk shifts act on all segments at once but can carry between segments; this happens only at addresses with extreme guard values, a set defined by addresses alone and small in advance, so sorting those few records restores exactness with a worst-case bound.",
    "explicit",
    [
        infer("S1.5.2.1",
              "The eight controlled $\\pm1$ updates of two integers $u,w$, with parity predicates, flip the parity of $u$ exactly when the control $c$ is $1$, preserve both quotients by two, restore $w$, and move each coordinate by at most four.",
              "Thus the parity of $u$ is flipped precisely when $c=1$, both quotients under division by two are preserved, and the arbitrary auxiliary integer $w$ is restored."),
        infer("S1.5.2.2",
              "Applied to all $K$-bit segments at once, each line is one controlled cyclic shift of a whole chunk; at addresses whose guard values satisfy $10\\le g\\le2^{K-1}-11$ no segment carries into or borrows from the next, so the composite $S_0$ agrees with the ideal XOR permutation $T_0$ there.",
              "Inductively, each packed addition therefore agrees with all the independent segment additions: no segment carries into or borrows from the next segment."),
        infer("S1.5.2.3",
              "Each guard excludes exactly twenty of its $2^{K-1}$ values, so the union bound over the $2(f-1)$ guards gives $|\\mathcal B|\\le\\min\\{1,80(f-1)2^{-K}\\}M$, independently of the payload.",
              "Since its complete range has $2^{K-1}$ values, the union bound over the $2(f-1)$ guards gives"),
        infer("S1.5.2.4",
              "Since $T_0$ preserves guard values and $S_0,T_0$ are bijections agreeing off $\\mathcal B$, both map $\\mathcal B$ onto itself, so $T_0S_0^{-1}$ fixes the complement and permutes $\\mathcal B$.",
              "Thus $T_0S_0^{-1}$ fixes $\\mathcal B^c$ and permutes $\\mathcal B$."),
        infer("S1.5.2.5",
              "Extracting the records of $\\mathcal B$ with their destination ranks, radix-sorting them and reinserting them into the marked holes implements $T_0$ everywhere.",
              "This implements $T_0$ everywhere."),
        infer("S1.5.2.6",
              "Divided by $V$, the scan and sorting terms are $O(A_{\\rm rect}^3/R)$ and $O(p^22^{-K}(1+A_{\\rm rect}/R))$, both $o(1)$, leaving $O(V(L^{\\tau}+1))$ from at most sixteen chunk swaps and eight rotations.",
              "Under the stated family bounds the first tends to zero, and the second is $O(p^2 2^{-K}(1+A_{\\rm rect}/R))=o(1)$."),
    ],
    mot_quote="The correction depends only on addresses, so the time bound is worst-case over all payloads.",
    frm=["address-chunk-interchange", "controlled-cyclic-shift", "tape-address-model",
         "sorting-and-its-cost", "arithmetic-modulo-2-and-xor",
         "cyclic-shifts-and-rotations-of-lists"],
    page="packed-selected-bit-addition",
    salient="A constant number of rotations of whole chunks performs $f$ independent bit XORs at once, and the failure set is defined by addresses alone, so the bound is deterministic and worst-case.")

B3 = show(
    "S1.5.3",
    "Taking rows from the first $O(\\log d)$ chunks and splitting them among the $W$ roles gives $F(e)\\le(s/W)F(e/m)+O((eK)^{\\tau}+1)$ for the time per unit volume on $e$ chunks, with individual kernels ($F(e)=O(e)$) once $e<d^{1/2}$, so a whole layer on $D\\le d$ chunks costs $O(d^{\\lambda'})$ per unit volume.",
    "Unroll the recurrence, bounding internal nodes by a geometric sum with ratio $(s/W)/m^{\\lambda}<1$ and leaves by $(s/W)^ju\\le e^{\\sigma}u^{1-\\sigma}$, then sum over the base-$m$ pieces of the active chunks.",
    "Each level multiplies normalized cost by $s/W\\le m^{\\sigma}$ while its basis changes cost only $(eK)^{\\tau}$; stopping at about $d^{1/2}$ chunks balances the leaf cost against this overhead, leaving a power of $d$ below one.",
    "recoverable",
    [
        infer("S1.5.3.1",
              "Applying $C$ individually on the first $q_0=O(\\log d)$ chunks costs $O(V\\log d)$ and frees their bits as a row index of range $2^{q_0K}\\ge W^{k_0}$, padded to a multiple of $W^{k_0}$ with at most doubling.",
              "Otherwise apply \\(C\\) individually on the selected bits of the first \\(q_0\\) chunks, in \\(O(V\\log d)\\) time."),
        infer("S1.5.3.2",
              "Each row goes whole to one role, so every role stream keeps the same complete suffix, scratch roles are filled from existing rows, and each recursive call acts on exactly $1/W$ of its parent's volume.",
              "Each recursive edge call acts on one role stream with volume exactly \\(1/W\\) of its parent's logical volume."),
        infer("S1.5.3.3",
              "The $s$ children cost $s(V/W)F(e/m)$, so dividing by $V$ gives the factor $s/W$ in the recurrence.",
              "Dividing by the current volume \\(V\\) gives the factor \\(s/W\\)."),
        infer("S1.5.3.4",
              "At an internal node $e\\ge d^{1/2}$, so $K\\le e^{2c}$ and the overhead is $O(e^{\\tau(1+2c)}+1)=O(e^{\\lambda})$; as $s/W\\le m^{\\sigma}<m^{\\lambda}$ the internal costs sum to $O(e^{\\lambda})$.",
              "The overhead is therefore \\(O(e^{\\tau(1+c/\\beta)}+1)=O(e^\\lambda)\\)."),
        infer("S1.5.3.5",
              "Adding the leaves $O(e^{\\sigma}d^{(1-\\sigma)/2})$ over the at most $(m-1)(1+\\lfloor\\log_md\\rfloor)$ base-$m$ pieces gives $O(\\log(2d)[d^{\\lambda}+d^{\\sigma+(1-\\sigma)/2}+1])=O(d^{\\lambda'})$.",
              "Adding their costs and the row preprocessing gives"),
    ],
    frm=["rank-saving-recurrence", "phase-frame-network", "packed-selected-bit-addition",
         "divide-and-conquer-and-recurrences", "geometric-series-and-sums"])

B4 = show(
    "S1.5.4",
    "Every intermediate coefficient of a layer is an exact Gaussian dyadic with at most $p+\\Delta$ fractional and $\\Delta+3$ integer and sign bits per component, where $\\Delta=\\lceil C_0d^{20}\\rceil=o(p)$, so the whole layer is evaluated exactly at width $O(p)$.",
    "Bound the arithmetic dependency depth by $A(e)\\le sA(e/m)+E$ through the recursion, and note that each elementary operation adds at most one denominator bit or doubles the modulus.",
    "Inside the network the operators are not contractions, so value growth cannot be bounded by norms; counting operations along every dependency chain bounds both denominators and magnitudes.",
    "explicit",
    [
        infer("S1.5.4.1",
              "Each network invocation adds at most $E=64(W+m+1)^3$ operations to a chain and leaves need at most $8e$, so with $B=s+E$ and $m^{10}<B<m^{11}$ the depth is at most $8B^2d^{12}$.",
              "Starting with \\(8e\\le8d\\le8dB\\) at a leaf and applying this inequality through the levels gives the first bound below."),
        infer("S1.5.4.2",
              "A value at depth $\\ell$ lies in $2^{-(p+\\ell)}\\mathbb Z[i]$ with modulus at most $2^{\\ell}$, so $p+\\Delta$ fractional and $\\Delta+3$ integer bits prevent both rounding and overflow.",
              "Thus reserving \\(p+\\Delta\\) fractional bits and \\(\\Delta+3\\) integer and sign bits per real component represents every intermediate coefficient exactly and prevents overflow."),
        infer("S1.5.4.3",
              "Choosing $20\\epsilon<1$ with $d=\\Theta(p^{\\epsilon})$ gives $\\Delta=o(p)$, so the coefficient width stays $O(p)$.",
              "Since \\(d=\\Theta(p^\\epsilon)\\), \\(\\Delta=o(p)\\), and the full coefficient width is \\(O(p)\\), as required in the time analysis."),
    ],
    mot_quote="Its intermediate operators need not be contractions.",
    frm=["fixed-point-complex-arithmetic", "dyadic-rationals-and-fixed-width-numerators",
         "divide-and-conquer-and-recurrences"])

B5 = infer(
    "S1.5.5",
    "Every row of $\\mathcal H$ has absolute row sum one, so $\\mathcal H$ maps disk arrays to disk arrays, and the single final truncation toward zero keeps the disk with error below $\\sqrt2\\,2^{-p}$.",
    "Thus $\\mathcal H$ maps disk arrays to disk arrays, and componentwise truncation preserves that disk and has error less than $\\sqrt2\\,2^{-p}$",
    frm=["fixed-point-complex-arithmetic", "triangle-inequality-and-norms"])

BL = show(
    "S1.5",
    "For records that are polynomials of length $r=2^{\\Theta(p/d)}$ with disk-valued coefficients on the grid $2^{-p}\\mathbb Z[i]$, $d=\\Theta(p^{\\epsilon})$ and $K=\\lfloor d^c\\rfloor$, the tensor product $\\mathcal H$ of $H_0$ on one selected bit in each of $D\\le d$ consecutive $K$-bit chunks, followed by one truncation $Q_p$, costs $O(Vd^{\\lambda'})$ with $\\lambda'=1-2^{-54}$ and has error below $\\sqrt2\\,2^{-p}$.",
    "Realise $C^{\\otimes D}$ by the complex network with phase frames, implement its binary basis changes by packed selected-bit additions, split rows among roles to get a volume recurrence, evaluate exactly with guard bits, and convert to $H_0^{\\otimes D}$ by diagonal phases.",
    "Doing the $D$ butterflies one at a time costs $D$ full passes; the network recursion replaces this by a power $d^{\\lambda'}$, and exact evaluation with one final truncation keeps the error of a whole layer at a single rounding.",
    "explicit",
    [B1, B2, B3, B4, B5],
    mot_quote="whereas separate butterfly factors would require $D$ whole-array passes.",
    frm=["phase-frame-network", "packed-selected-bit-addition", "rank-saving-recurrence",
         "fft-butterflies", "fixed-point-complex-arithmetic"],
    page="simultaneous-butterfly-layer",
    salient="All $D$ butterflies of a layer together cost less than $D$ passes, $O(d^{\\lambda'})$ with $\\lambda'<1$, and the whole layer incurs only one rounding.")

S1 = show(
    "S1",
    "Two fixed-tape procedures beat one pass per level: interchanging two disjoint contiguous $u$-bit address fields of an array costs $O(Vu^{\\tau})$, and a normalized butterfly $H_0$ applied simultaneously to one selected bit in each of $D\\le d$ equal $K$-bit address chunks costs $O(Vd^{\\lambda'})$, with fixed $\\tau,\\lambda'<1$.",
    "Build fixed linear networks that exchange two banks while restoring scratch values, give each wire a frame so that every edge change is a smaller call of the same procedure, and solve the resulting volume-normalized recurrences.",
    "A network whose wires carry whole arrays turns one large operation into a fixed number of smaller instances of itself, so its cost obeys a recurrence, and well-chosen frames make every edge such an instance.",
    "explicit",
    [S1_1, S1_2, KEY, A, BL],
    mot_quote="The intermediate frames are chosen so that every edge can be implemented by smaller calls to the same procedure.",
    frm=["multitape-turing-machine", "tape-address-model", "fft-butterflies"],
    adds=[
        B("u", "field width", "The number of address bits in each of the two interchanged fields.", "count"),
        B("D", "layer chunk count", "The number of address chunks whose selected bit receives a butterfly in one simultaneous layer.", "count"),
    ])

# ---------------------------------------------------------------- ring convolution
C1 = show(
    "S2.1",
    "For a power of two $t$ dividing $2r$ and $\\omega_t=y^{2r/t}$, the normalized transforms $F_t^{\\pm}$ on $\\mathcal R_r^t$ are contractions with $F_t^+F_t^-=t^{-1}I$, and $F_t^-$ is computed by $\\log_2t$ decimation-in-frequency levels, each an $H_0$ butterfly followed by multiplication by a power of $y$.",
    "Check character cancellation directly in the ring and derive the radix-two decimation-in-frequency recursion.",
    "The usual geometric-series argument divides by $\\omega_t^j-1$, which is impossible in a ring with zero divisors, so cancellation is shown instead by shifting the summation index.",
    "explicit",
    [
        infer("S2.1.1",
              "Every power of $\\omega_t$ is a signed coefficient permutation, hence an isometry for the coefficient sup norm, and each transform entry averages $t$ such images, so $F_t^{\\pm}$ are contractions.",
              "Every power of $\\omega_t$ is an isometry, and each transform entry is an average of $t$ such images."),
        infer("S2.1.2",
              "For $t\\nmid j=2^vj_0$ with $j_0$ odd, shifting $k$ by $t/2^{v+1}$ multiplies $\\sum_k\\omega_t^{jk}$ by $y^{rj_0}=-1$, so the sum vanishes because $\\mathcal R_r$ has no two-torsion; hence $F_t^+F_t^-=t^{-1}I$.",
              "Hence the sum is zero, since the additive group of $\\mathcal R_r$ has no two-torsion."),
        infer("S2.1.3",
              "Pairing $z_k$ with $z_{k+t/2}$ by $H_0$ and multiplying the second output by $\\omega_t^{-k}$ reduces $F_t^-$ to two transforms of length $t/2$.",
              "This computes $F_t^-$ because, for $b\\in\\{0,1\\}$,"),
    ],
    mot_quote="The ring has zero divisors, so we verify character cancellation directly instead of dividing by $\\omega_t^j-1$.",
    frm=["negacyclic-ring", "discrete-fourier-transform", "fft-butterflies"],
    page="synthetic-polynomial-transform",
    adds=[B("\\omega_t", "synthetic root", "The power $y^{2r/t}$ of $y$, a principal $t$-th root of unity in $\\mathcal R_r$ whose powers are signed coefficient shifts.")])

C2 = infer(
    "S2.2",
    "The forward recursion writes $(F_t^-z)_j$ at slot $\\operatorname{rev}_a(j)$ for $t=2^a$, so it implements $B_tF_t^-$ with $B_t$ the bit-reversal record permutation, and running the levels in reverse implements $F_t^+B_t^{-1}$, consuming that order; no frequency index is ever moved.",
    "The recursion writes its outputs directly in this order; it does not move whole frequency indices.",
    frm=["synthetic-polynomial-transform", "fft-butterflies", "permutations-and-bijections"],
    page="stored-frequency-order")

C3 = show(
    "S2.3",
    "After an explicit layout permutation $L$ of record addresses, the forward and opposite synthetic transforms on $d-1$ axes of lengths $t_i\\in\\{r/2,r\\}$ have exact counterparts $LBF_{\\boldsymbol t}^-$ and $F_{\\boldsymbol t}^+B^{-1}L^{-1}$, error below $\\sqrt2\\,\\ell2^{-p}$, and cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
    "Group each round's axis butterflies into one parallel layer followed by a recordwise monomial, move the selected bits of all axes to a common offset in consecutive $K$-bit chunks by bit moves and chunk interchanges, apply the simultaneous layer per round, and truncate once per round.",
    "The fast layer applies only when every participating axis's current bit sits at the same offset of consecutive equal chunks, so a layout must be built, and its moves are themselves cheap chunk interchanges.",
    "explicit",
    [
        infer("S2.3.1",
              "Each axis's twiddle depends only on that axis's address bits and so commutes with the other axes' butterflies; a round therefore groups into a parallel butterfly $\\mathcal H$ followed by one monomial $J_E$, multiplication by $y^E$ with $E=-\\sum_i(2r/u_i)b_ik_i\\bmod2r$.",
              "Consequently the individual axis steps may be grouped as a parallel butterfly $\\mathcal H$, followed by one recordwise monomial operation $J_E$."),
        infer("S2.3.2",
              "Moving the $O(dK)$ leftover low and leading slots to a prefix costs $O(TpdK)$, and their rounds are done by individual butterflies in the same bound.",
              "There are at most $D(b+1)=O(dK)$ listed slots, so the moves cost $O(TpdK)$."),
        infer("S2.3.3",
              "Reordering the remaining $K$-bit chunks needs fewer than $(d-1)\\ell/K=O(p/K)$ chunk interchanges of cost $O(TpK^{\\tau})$ each, $O(Tp\\,pK^{\\tau-1})$ in total.",
              "Each costs $O(TpK^\\tau)$, so all these exchanges cost"),
        infer("S2.3.4",
              "Each of the at most $\\ell$ rounds on the chunks is one simultaneous layer, so they cost $O(Tp\\ell d^{\\lambda'})$.",
              "The simultaneous-layer procedure therefore applies at cost $O(Tpd^{\\lambda'})$ per round and $O(Tp\\ell d^{\\lambda'})$ in total."),
        infer("S2.3.5",
              "Multiplication by $y^E$ splits the coefficient list, puts the negated tail first and applies a common sign, in $O(rp)$ per record with no sort.",
              "This is multiplication by $y^E$ modulo $y^r+1$."),
        infer("S2.3.6",
              "Truncation toward zero is odd and $J_E$ is a signed coefficient permutation, so $J_EQ_p(\\mathcal Hz)=Q_p(J_E\\mathcal Hz)$: each round truncates once after an exact contraction.",
              "Thus the actual forward call sequence returns exactly the result of truncating once after the exact contraction round."),
        infer("S2.3.7",
              "Contraction rounds do not increase the accumulated error and each truncation adds less than $\\sqrt2\\,2^{-p}$, so at most $\\ell$ rounds give error below $\\sqrt2\\,\\ell2^{-p}$.",
              "Starting with zero error, at most $\\ell$ rounds therefore give the claimed error and disk bounds."),
    ],
    mot_quote="To apply Proposition~\\ref{prop:simultaneous-layer} in a transform round, we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks.",
    frm=["synthetic-polynomial-transform", "stored-frequency-order", "address-chunk-interchange",
         "simultaneous-butterfly-layer", "tape-address-model", "negacyclic-ring"],
    page="transform-tape-layout")

C4 = show(
    "S2.4",
    "For disk-grid $f,g\\in\\mathcal R_r$ with $r<2^p$, evaluating the four integer numerator polynomials at $B_0=2^{4p}$, multiplying them in pairs with the established $O(N\\log N)$ multiplier and extracting centered base-$B_0$ digits gives the exact numerators of $fg$, hence $Q_p(fg/r)$ with error below $\\sqrt2\\,2^{-p}$, in time $O(rp\\log(rp))$.",
    "Kronecker substitution with signed carries: pack coefficients as base-$B_0$ digits, multiply the integers, read product coefficients back as centered residues, reduce modulo $y^r+1$, and truncate.",
    "The records are short, $O(rp)$ bits, so the established multiplier is cheap on them, and packing into digits much wider than any product coefficient makes one integer product carry the whole polynomial product without ambiguity.",
    "recoverable",
    [
        infer("S2.4.1",
              "Every coefficient of the integer polynomial products satisfies $|h_j|\\le r2^{2p}<2^{3p}<B_0/2$, so after removing the lower coefficients the next one is the centered residue modulo $B_0$.",
              "After the lower coefficients have been removed from an evaluation, this strict bound identifies the next coefficient by its centered residue modulo $B_0$."),
        infer("S2.4.2",
              "By the residual identity with carries $\\rho_j\\in\\{0,1\\}$, the centered representative equals $h_j$ at every block, including the padded top block, and a negative product's final carry cancels its sign extension.",
              "Thus $\\widehat h_j=h_j$."),
        infer("S2.4.3",
              "The four exact products on $O(rp)$-bit integers dominate the linear packing, extraction, negacyclic wrapping and truncation.",
              "Four exact integer products dominate the linear packing, extraction, combination, wrapping, and truncation costs."),
    ],
    frm=["n-log-n-barrier", "negacyclic-ring", "binary-numerals-and-bit-strings",
         "modular-arithmetic", "positional-notation-in-any-radix"],
    page="signed-packing")

C5 = show(
    "S2.5",
    "Retaining the $LB$ order through the pointwise products and scaling by $M$ yields $\\mathcal M_r(f,g)$ exactly in the exact counterpart, and the computed result has error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
    "Use the convolution theorem for normalized transforms, commute the common record permutation past the pointwise products, and add the errors propagated through contractions and the bilinear product.",
    "A pointwise product commutes with applying the same record permutation to both operands, so the stored order never needs undoing, and since all maps are contractions or bilinear contractions on disk arrays their errors simply add.",
    "recoverable",
    [
        infer("S2.5.1",
              "Since $F_{\\boldsymbol t}^-(f*g)=M(F_{\\boldsymbol t}^-f)(F_{\\boldsymbol t}^-g)$, $F_{\\boldsymbol t}^+F_{\\boldsymbol t}^-=I/M$ and $P(LBu,LBv)=LBP(u,v)$ for the product $P(u,v)=uv/r$, the opposite transform of the stored products, scaled by $M$, is $(f*g)/(rM)$.",
              "Thus $\\mathcal T_+$ applied to the pointwise product of the exact stored forward outputs equals"),
        infer("S2.5.2",
              "Forward errors $\\delta=\\sqrt2\\,\\ell2^{-p}$ give a product error below $2\\delta$, truncation adds $\\sqrt2\\,2^{-p}$, the opposite transform adds $\\delta$, and the exact scaling by $M$ gives error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
              "The final exact multiplication by $M$ therefore gives error less than"),
    ],
    frm=["contraction-error-propagation", "discrete-fourier-transform", "convolution",
         "stored-frequency-order", "transform-tape-layout", "signed-packing"])

C = show(
    "S2",
    "For arrays of $M$ disk-grid records in $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ on $d-1$ axes of lengths $t_i\\in\\{r/2,r\\}$, with $T=rM$, the normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ is computed with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
    "Apply two forward synthetic transforms and keep their output order, multiply corresponding polynomial records by signed packing and divide by $r$, apply the opposite synthetic transform to that order, and scale by $M$.",
    "In $\\mathcal R_r$ the roots of unity are powers of $y$, which act as signed coefficient shifts, so the transforms need no twiddle arithmetic and their cost is only data layout and butterfly layers, both accelerated by the tape procedures, plus short pointwise products.",
    "explicit",
    [C1, C2, C3, C4, C5],
    mot_quote="Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list.",
    frm=["transform-tape-layout", "stored-frequency-order", "signed-packing",
         "contraction-error-propagation", "convolution", "negacyclic-ring",
         "discrete-fourier-transform"],
    page="normalized-ring-convolution",
    adds=[B("M", "record count", "The number $\\prod_{i<d}t_i=T/r$ of polynomial records, one per address on the first $d-1$ axes.", "count")])

# ---------------------------------------------------------------- the algorithm
D1 = show(
    "S3.1",
    "For coprime $2\\le s<t<2^p$ with $t/s-1>p/\\alpha^4$, there are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and $B_0:\\mathbb C^t\\to\\mathbb C^s$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, where $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$, and $A,B_0$ are computed on the $p$-bit grid with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$ without executing $P_s$ or $P_t$.",
    "Start from Harvey and van der Hoeven's Gaussian identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$, invert $\\mathsf T$ on nearest selected coordinates by a Neumann series, and leave both coordinate permutations inside the identity instead of sorting.",
    "Gaussian resampling relates a prime-length transform to a power-of-two one, but its usual implementation spends $O(tp\\log t)$ on two sorts per line, a full logarithmic factor; keeping the permutations in the formula avoids that cost.",
    "explicit",
    [
        infer("S3.1.1",
              "With $C$ selecting the nearest coordinates $q_j$ of $tj/s$ and $\\mathsf D$ the compensating diagonal, $N=C\\mathsf T\\mathsf D$ satisfies $\\|N-I\\|<2^{-\\alpha^2\\theta}<1/2$, so it is invertible by the Neumann series.",
              "Thus $\\|N-I\\|<1/2$, so $N$ is invertible by the Neumann series."),
        infer("S3.1.2",
              "With $A=\\mathsf S/2$ and $B_0=2^{-(2\\alpha^2-2)}\\mathsf D\\,(N^{-1}/2)\\,C$ both are contractions, and $\\mathsf DN^{-1}C$ is a left inverse of $\\mathsf T$, which yields $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$.",
              "Because $\\|C\\|=1$, both are contractions."),
        infer("S3.1.3",
              "The original implementation applies $P_t$ and $P_s^{-1}$ by label-and-sort at cost $O(tp\\log t)$ each; here both stay in the identity and only the ordered maps are computed.",
              "In \\eqref{eq:no-sort-one-dimensional} these permutations remain in the transform identity."),
    ],
    mot_quote="Its usual implementation sorts twice on each coordinate.",
    frm=["discrete-fourier-transform", "contraction-error-propagation",
         "exponential-logarithm-and-gaussian-function", "primes-coprimality-and-gcd",
         "permutations-and-bijections"],
    page="gaussian-resampling")

D2 = show(
    "S3.2",
    "Tensoring over the $d$ axes gives $RF_{\\boldsymbol s}=2^{\\gamma}\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$, where linewise $\\mathcal A,\\mathcal B_0$ have error below $dp^2$ and cost $O(dTp^{3/2+\\delta}\\alpha)$, and exposing and restoring every axis in the padded box costs $O(Tp\\,d^2(1+\\ell^{\\tau}))$.",
    "Apply the one-dimensional maps one axis at a time on a zero-padded power-of-two box, exposing each axis by adjacent field interchanges.",
    "Keeping the full padded box makes every axis a complete address field, so axes can be moved by the fast chunk interchange rather than by sorting.",
    "recoverable",
    [
        infer("S3.2.1",
              "Tensoring the one-dimensional identity over the axes gives the tensor identity with scale $2^{\\gamma}$.",
              "Tensoring \\eqref{eq:no-sort-one-dimensional} proves \\eqref{eq:no-sort-tensor}."),
        infer("S3.2.2",
              "Each axis map is a contraction acting on its valid lines with error below $p^2$, and composing the $d$ axis maps gives error below $dp^2$.",
              "Composing the $d$ axis maps gives error less than $dp^2$."),
        infer("S3.2.3",
              "Moving an axis past a neighbour by an equal-width chunk interchange plus a single-bit move costs $O(Tp(1+\\ell^{\\tau}))$, and $O(d^2)$ such moves expose and restore all axes.",
              "Each adjacent interchange therefore costs $O(Tp(1+\\ell^\\tau))$."),
    ],
    frm=["gaussian-resampling", "address-chunk-interchange",
         "multidimensional-arrays-and-row-major-order"])

D3 = infer(
    "S3.3",
    "With the chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_is_ij_i^2/t_i)$, which has period $t_i$ in coordinate $i$ when every $t_i$ is even, $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$: the middle transform, including its frequency permutation $Q$, is a normalized cyclic convolution between two pointwise phase multiplications.",
    "This is precisely the coefficient in $QF_{\\boldsymbol t}$, because $Q$ reads frequency $(-s_i j_i)_i$ from the negative-sign transform.",
    frm=["discrete-fourier-transform", "convolution", "roots-of-unity-and-euler-s-formula"],
    page="bluestein-chirp")

D4 = infer(
    "S3.4",
    "With $S=\\prod_is_i$, $(RF_{\\boldsymbol s}^+)[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$: each $t_i$ is a unit modulo $s_i$, so $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$, the permutation commutes with the pointwise product, and the normalized convolution theorem gives the factor $1/S^2$.",
    "Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives $F_{\\boldsymbol s}^+R=R^{-1}F_{\\boldsymbol s}^+$ and hence $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$.",
    frm=["gaussian-resampling", "discrete-fourier-transform", "convolution",
         "modular-arithmetic", "permutations-and-bijections"],
    page="permutation-cancellation",
    salient="The source permutation $R$ is never executed: it cancels exactly between the two forward transforms, the pointwise product and the opposite-sign transform.")

D5 = show(
    "S3.5",
    "Taking $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^{\\epsilon}\\rfloor$, $K=\\lfloor d^c\\rfloor$, a power of two $T\\in[4n/b,8n/b)$, $r=2^{\\lceil\\log_2T/d\\rceil}$, axis lengths $t_i\\in\\{r/2,r\\}$ with product $T$ and $t_d=r$, and distinct primes $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ with $\\eta=1/(4d)$, gives $Tp=\\Theta(n)$, $T/2<S<T$, and every hypothesis of the layer, transform and resampling interfaces for all large $n$.",
    "Fix conservative rational exponents satisfying all the layer inequalities, derive the size relations, and obtain the primes from an explicit prime-interval estimate and trial division.",
    "The primes must be close to the powers of two so the source box fills a fixed fraction of the padded box, yet far enough below them for Gaussian resampling to converge; $\\eta=1/(4d)$ achieves both, and $p=6b$ leaves room for exact rounding.",
    "explicit",
    [
        infer("S3.5.1",
              "The fixed choice $\\tau=\\sigma=1-2^{-50}$, $\\beta=1/2$, $\\delta=1/16$, $\\lambda=1-2^{-52}$, $c=2^{-56}$, $\\lambda'=1-2^{-54}$, $C_1=20$, $\\epsilon=2^{-75}$, $\\kappa=2^{-182}$ satisfies all the layer and dimension inequalities with room to spare.",
              "These constants are deliberately conservative; no optimization is claimed."),
        infer("S3.5.2",
              "The sizes give $Tp=\\Theta(n)$, $d=\\Theta(p^{\\epsilon})$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$ and $r=2^{\\Theta(p^{1-\\epsilon})}$, so $r$ exceeds every fixed power of $p$ and $K/\\log p\\to\\infty$.",
              "These bounds also give that $r$ exceeds every fixed power of $p$, $K/\\log p\\to\\infty$, and $\\ell/K\\to\\infty$."),
        infer("S3.5.3",
              "The prime-interval estimate gives more than $d$ primes in each of the disjoint intervals for $r/2$ and $r$, so distinct odd primes $s_i$ exist, and $S/T>(1-1/(2d))^d>1/2$.",
              "We may therefore choose distinct odd primes satisfying"),
        infer("S3.5.4",
              "Then $t_i/s_i-1>\\eta$ gives $\\alpha^4(t_i/s_i-1)>3db\\ge p$ for $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$, and $2\\le\\alpha<\\sqrt p$, so the resampling hypotheses hold for every axis.",
              "Thus every hypothesis of Lemma~\\ref{lem:no-sort-resampling} holds for all sufficiently large input lengths."),
        infer("S3.5.5",
              "The machine finds the primes by trial division in $n^{o(1)}$ time, so all parameters are computed, not supplied as advice.",
              "All primes and length parameters are therefore generated by the machine; they are not advice."),
    ],
    mot_quote="their product must occupy a fixed fraction of the padded box, while each ratio $t_i/s_i$ must leave enough separation for resampling.",
    frm=["simultaneous-butterfly-layer", "gaussian-resampling", "negacyclic-ring",
         "crt-axis-map", "primes-coprimality-and-gcd", "asymptotic-notation-beyond-big-o"],
    page="parameter-regime")

D6 = infer(
    "S3.6",
    "Writing each input as a polynomial in $2^b$ with $q=\\lceil n/b\\rceil$ digits, the product has degree $2q-2<S$, so cyclic convolution modulo $x^S-1$ has no wraparound, and every product coefficient satisfies $0\\le c_j\\le q(2^b-1)^2<2^{3b}$.",
    "Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
    frm=["convolution", "polynomials", "positional-notation-in-any-radix"],
    page="radix-digit-reduction")

D7 = show(
    "S3.7",
    "With $P_i=\\prod_{j<i}s_j$ and $\\mu_i=P_i^{-1}\\bmod s_i$, the map $\\Phi:x\\mapsto\\prod_ix_i^{\\mu_i}$ is an algebra isomorphism $\\mathbb C[x]/(x^S-1)\\to\\mathbb C[x_1,\\dots,x_d]/(x_1^{s_1}-1,\\dots,x_d^{s_d}-1)$ preserving cyclic convolution, and $\\Phi$, its inverse and their padding to the box cost $O(Tp\\,d^2(1+\\ell^{\\tau}))$.",
    "Express the new coordinates of a mixed-radix index as triangular offsets $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\bmod s_i$, apply them as prefix-controlled cyclic shifts in decreasing $i$, and reorder axes by chunk interchanges.",
    "A general Chinese-remainder reindexing would be a sort; the exponents $\\mu_i$ make each new coordinate depend only on earlier digits, so every step is a linear-cost controlled cyclic shift.",
    "explicit",
    [
        infer("S3.7.1",
              "$\\Phi$ respects $x^S=1$, and the image of $x$ has order $S$ because each $\\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all $S$ target monomials once and $\\Phi$ is an isomorphism.",
              "Hence $\\Phi$ is an isomorphism and preserves cyclic convolution."),
        infer("S3.7.2",
              "For $k=\\sum_ja_jP_j$, axis $i$ of $\\Phi(x^k)$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\bmod s_i$, since terms with $j>i$ are divisible by $s_i$ and $\\mu_iP_i\\equiv1$.",
              "Indeed terms with $j>i$ are divisible by $s_i$, and $\\mu_iP_i=1$ modulo $s_i$."),
        infer("S3.7.3",
              "Updating targets in the order $i=d,\\dots,1$ uses the original digits as controls, and on the padded box each step rotates the valid interval $[0,s_i)$ and fixes the rest, so the padding stays zero.",
              "Consequently zero padding remains zero after every step."),
        infer("S3.7.4",
              "Each triangular update is a prefix-controlled cyclic shift of linear cost, with offset setup $o(Tp)$.",
              "Each triangular update is a prefix-controlled cyclic shift."),
        infer("S3.7.5",
              "Adjacent axes of widths $\\ell$ and $\\ell-1$ are exchanged by moving one bit and interchanging equal-width fields, and $O(d^2)$ exchanges give the total $O(Tp\\,d^2(1+\\ell^{\\tau}))$.",
              "Therefore the map $\\Phi$, its inverse, and their padding operations cost"),
    ],
    mot_quote="The following map uses that algebraic split, with coordinate powers that make the change of order a sequence of controlled cyclic shifts.",
    frm=["convolution", "controlled-cyclic-shift", "address-chunk-interchange",
         "primes-coprimality-and-gcd", "modular-arithmetic"],
    page="crt-axis-map")

D8 = infer(
    "S3.8",
    "With $\\zeta=e^{\\pi i/r}$, $x_d\\mapsto\\zeta y$ is an isomorphism $\\mathbb C[x_d]/(x_d^r-1)\\to\\mathbb C[y]/(y^r+1)$ multiplying coefficient $k$ by $\\zeta^k$; for $k+l=j+hr$ with $h\\in\\{0,1\\}$ one has $\\zeta^{k+l}(-1)^h=\\zeta^j$, so after untwisting the negacyclic product gives the cyclic convolution on the last axis with the correct sign.",
    "Untwisting therefore recovers the cyclic coefficient with the correct sign.",
    frm=["negacyclic-ring", "convolution", "roots-of-unity-and-euler-s-formula", "complex-numbers"],
    page="coefficient-twist",
    salient="The sign $-1$ from the negacyclic wrap $y^r=-1$ is cancelled exactly by $\\zeta^r=-1$, so a diagonal phase twist turns cyclic into negacyclic convolution.")

D9 = show(
    "S3.9",
    "The computed source transform $\\widetilde{\\mathscr F}$ (linewise $\\widetilde A$ on the padded box, the chirp transform $\\overline{\\widetilde a}\\cdot\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,\\overline{\\widetilde a}\\cdot x)$ with the complex convolution evaluated through the twist and $\\widetilde{\\mathcal M}_r$, linewise $\\widetilde B_0$, and an exact scale $2^{\\gamma}$) has exact counterpart $2^{\\gamma}\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$, and conjugating input and output gives $RF_{\\boldsymbol s}^+$.",
    "Turn the ring convolution into normalized complex convolution by the twist, wrap it between chirp phases to obtain $QF_{\\boldsymbol t}$, and sandwich that between the Gaussian line maps.",
    "Every factor of the tensor resampling identity has a procedure: the Gaussian line maps give $\\mathcal A$ and $\\mathcal B_0$, and the chirp identity and twist reduce $QF_{\\boldsymbol t}$ to the fast ring convolution, so composing them evaluates $RF_{\\boldsymbol s}$ with no sort.",
    "recoverable",
    [
        infer("S3.9.1",
              "Normalized complex cyclic convolution is $\\mathcal M_{\\mathbb C}(f,g)=D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$, where $D_\\pm$ multiply coefficient $k$ by $\\zeta^{\\pm k}$ and $\\iota$ reads the last axis as a polynomial; it is a bilinear contraction because these maps are isometries.",
              "The maps $D_\\pm$ and $\\iota^{\\pm1}$ are isometries, so $\\mathcal M_{\\mathbb C}$ is also a bilinear contraction."),
        infer("S3.9.2",
              "With exact phases and exact convolution the chirp procedure gives $\\overline a\\cdot\\mathcal M_{\\mathbb C}(a,\\overline a\\cdot x)=QF_{\\boldsymbol t}x$.",
              "Replacing the approximations by exact phases and exact convolution gives $\\overline a\\mathbin{\\cdot}\\mathcal M_{\\mathbb C} (a,\\overline a\\mathbin{\\cdot}x)=QF_{\\boldsymbol t}x$ by \\eqref{eq:permuted-chirp}."),
        infer("S3.9.3",
              "The opposite-sign procedure $\\widetilde{\\mathscr F}^+(z)=\\overline{\\widetilde{\\mathscr F}(\\overline z)}$ has exact counterpart $RF_{\\boldsymbol s}^+$, since conjugation flips the Fourier sign and commutes with the real permutation $R$.",
              "its exact counterpart is $RF_{\\boldsymbol s}^{+}$ by Lemma~\\ref{lem:chirp-permutation}."),
    ],
    frm=["gaussian-resampling", "bluestein-chirp", "coefficient-twist",
         "normalized-ring-convolution", "permutation-cancellation", "address-chunk-interchange"],
    page="tensor-source-transform")

D10 = infer(
    "S3.10",
    "By the permutation cancellation the exact counterpart after the two forward source transforms of $u=\\Phi(\\text{digits})$ and $v$, their pointwise product and the opposite transform is $(u*v)/S^2$; scaling by $S$ gives $w=(u*v)/S$, and scaling by $2^{2b+4}S$ gives $2^{2b+4}(u*v)$, whose image under $\\Phi^{-1}$ is the integer digit convolution.",
    "The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\\Phi$ is the original integer coefficient convolution.",
    frm=["permutation-cancellation", "crt-axis-map", "radix-digit-reduction"])

D11 = show(
    "S3.11",
    "All intermediate arrays stay in the unit disk with explicit margins, each source transform has error below $9\\cdot2^{\\gamma}T\\log_2T$ grid units of $2^{-p}$, and the recovered coefficients have absolute error below $448b\\,2^{-3b/4}<1/2$, so rounding and radix-$2^b$ carry propagation give exactly the $2n$-bit product.",
    "Propagate errors through contractions and bilinear contractions, check the disk margin at every call, and compare the error after the final known scalings with $1/2$.",
    "Every stage is a contraction or a bilinear contraction of disk arrays, so errors only add along the pipeline and the final known scalings multiply them by explicit factors; with $p=6b$ the result stays below $1/2$.",
    "explicit",
    [
        infer("S3.11.1",
              "Three synthetic transform errors and one product truncation give normalized ring convolution error below $5T\\log_2T$ grid units, and output norm below $0.701$ whenever one operand has norm at most $0.7$.",
              "This proves the disk margin after the scale $M$, without clipping the output."),
        infer("S3.11.2",
              "The chirp transform errs by less than $8T\\log_2T$ units, so the source transform errs by less than $2^{\\gamma}(2dp^2+8T\\log_2T)\\le9\\cdot2^{\\gamma}T\\log_2T$ units, as $2dp^2<T\\log_2T$ eventually.",
              "because $2dp^2<TL$ eventually."),
        infer("S3.11.3",
              "The pointwise product of the two source transforms and the opposite transform give $\\widetilde w$ approximating $w=(u*v)/S$ within $28\\cdot2^{\\gamma}T^2\\log_2T$ units, with $\\|\\widetilde w\\|<1$.",
              "The first exact numerator multiplication by $S$ gives $\\widetilde w$, approximating $w=(u*v)/S$ with error less than $E_wh_p$, where"),
        infer("S3.11.4",
              "Scaling by $2^{2b+4}S$ with $S\\le T<2^b$ and $\\gamma\\le b/4$ gives final error below $448b\\,2^{-b+\\gamma}\\le448b\\,2^{-3b/4}<1/2$, so rounding gives the unique correct integer coefficient in $[0,2^{3b})$.",
              "The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient."),
        infer("S3.11.5",
              "Carry propagation keeps $\\sum_{h<j}c_h2^{bh}=\\sum_{h<j}d_h2^{bh}+k_j2^{bj}$ with carries $0\\le k_j<2^{2b}$, and the product is below $2^{2n}$, so exactly $2n$ output bits are written.",
              "The exact product is less than $2^{2n}$; all bits above position $2n-1$ are therefore zero."),
    ],
    mot_quote="Composing such algorithms adds their errors: at each step, insert the exact map at the computed input and use its contraction bound on the accumulated input error.",
    frm=["contraction-error-propagation", "tensor-source-transform", "radix-digit-reduction",
         "fixed-point-complex-arithmetic", "triangle-inequality-and-norms"],
    page="precision-exact-recovery")

D = show(
    "S3",
    "Above a fixed cutoff, the algorithm (radix digits, the map $\\Phi$, two forward source transforms, a pointwise product, one opposite transform, two scalings by $S$, rounding, $\\Phi^{-1}$ and carry propagation) outputs exactly $\\operatorname{bin}_{2n}(\\operatorname{val}(x)\\operatorname{val}(y))$.",
    "Write the digit convolution through Fourier transforms of prime lengths on a Chinese-remainder product of axes, compute those transforms by Gaussian resampling to power-of-two lengths and a chirp convolution evaluated over $\\mathcal R_r$ after a phase twist, and prove the final coefficient error is below $1/2$.",
    "The Chinese-remainder split needs pairwise coprime axis lengths while the fast synthetic machinery needs powers of two; Gaussian resampling and Bluestein's chirp bridge the two shapes, and an error bound below $1/2$ turns approximate complex arithmetic into exact integers.",
    "explicit",
    [D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11],
    mot_quote="The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two.",
    frm=["radix-digit-reduction", "crt-axis-map", "tensor-source-transform",
         "precision-exact-recovery", "parameter-regime", "convolution"],
    page="multiplication-algorithm",
    adds=[
        B("s_i", "prime source length", "The distinct odd prime length of source axis $i$, chosen just below the power of two $t_i$."),
        B("S", "source size", "The product $\\prod_is_i$ of the prime source lengths, the length of the cyclic digit convolution.", "count"),
        B("b", "digit width", "The number $\\lceil\\log_2n\\rceil$ of bits per radix digit of the inputs.", "count"),
        B("R", "source permutation", "The tensor product of the coordinate dilations $(P_{s_i}u)_j=u_{t_ij}$ on the prime-length source axes."),
        B("Q", "target permutation", "The tensor product of the frequency dilations $(P_{t_i}v)_k=v_{-s_ik}$ on the power-of-two axes."),
    ])

# ---------------------------------------------------------------- cost
E = show(
    "S4",
    "With $V=Tp=\\Theta(n)$, every cost divided by $V$ is a power of $p$ at most $p^{1-2\\kappa}$, so the multiplier runs in $O(n(\\log n)^{1-\\kappa})$ for large $n$ and, with schoolbook multiplication below a cutoff, in $O(n(\\lg n)^{1-\\kappa})$ for every $n\\ge1$.",
    "Tabulate each operation's cost divided by $Tp$ as a power of $p$, compute the margins of the seven dominant powers below one, and absorb setup, descriptors and exceptional sorting as $o(V)$.",
    "Since $Tp=\\Theta(n)$ and $p=\\Theta(\\log n)$, a normalized cost $p^{1-\\kappa}$ is exactly the target bound, so it suffices that each row of the cost table is a power of $p$ strictly below one with an explicit margin.",
    "recoverable",
    [
        infer("S4.1",
              "Put $V=Tp=\\Theta(n)$; each coefficient uses $\\Theta(p)$ bits, so a full padded array has $\\Theta(V)$ stored bits.",
              "For the cost calculation put $V=Tp=\\Theta(n)$."),
        infer("S4.2",
              "The seven dominant normalized costs have margins $g_1>1/2$, $g_2=\\epsilon c(1-\\tau)=2^{-181}$, $g_3=\\epsilon(1-\\lambda')=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$ and $g_7=2^{-75}$ below one, so the smallest is $2^{-181}=2\\kappa$.",
              "Thus $\\min_i g_i=2^{-181}=2\\kappa$."),
        infer("S4.3",
              "The smallest margin comes from the transform layout: $O(p/K)$ chunk exchanges of cost $O(VK^{\\tau})$ each, normalized $O(pK^{\\tau-1})=O(p^{1-\\epsilon c(1-\\tau)})$.",
              "Each exchange costs $O(VK^\\tau)$ by Lemma~\\ref{lem:chunk-swap}, so the normalized total is"),
        infer("S4.4",
              "Descriptor setup at the $p^{O(1)}$ recursion visits, per-record address work and per-line setup cost $o(Tp)$ because $r$ exceeds every fixed power of $p$.",
              "These estimates all use that $r$ exceeds every fixed power of $p$."),
        infer("S4.5",
              "The exceptional records of all packed basis changes have total sorting cost $O(Vp^{A'}2^{-K})=o(V)$, independently of the data.",
              "This is a deterministic worst-case bound."),
        infer("S4.6",
              "Each power is at most $1-2\\kappa$ and any fixed power of $\\log p$ is eventually at most $p^{\\kappa}$, so the total is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
              "Any fixed power of $\\log p$ is at most $p^\\kappa$ eventually."),
        infer("S4.7",
              "Below one fixed cutoff the machine uses schoolbook multiplication, and enlarging the constant covers these finitely many lengths.",
              "Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it."),
    ],
    frm=["multiplication-algorithm", "address-chunk-interchange", "simultaneous-butterfly-layer",
         "parameter-regime", "big-o-notation", "asymptotic-notation-beyond-big-o"],
    page="cost-accounting",
    salient="The bottleneck is not the butterfly arithmetic but the chunk exchanges of the transform layout, whose margin $\\epsilon c(1-\\tau)=2^{-181}$ is why $\\kappa=2^{-182}$ is so small.")

F = infer(
    "S5",
    "Since $T_A(n)/(n\\lg n)=O((\\lg n)^{-\\kappa})\\to0$, no constants $c_A>0$ and $N_A$ give $T_A(n)\\ge c_An\\lg n$ for all $n\\ge N_A$, so the eventual $n\\log n$ lower bound conjectured by Sch\\\"onhage and Strassen fails in this model.",
    "The power saving proved here gives a limit of zero through all input lengths, which is a stronger conclusion.",
    frm=["n-log-n-barrier", "asymptotic-notation-beyond-big-o"],
    deferred=True)

ROOT = show(
    "S0",
    "One deterministic Turing machine with a fixed finite alphabet and a fixed number of one-dimensional tapes outputs $\\operatorname{bin}_{2n}(\\operatorname{val}(x)\\operatorname{val}(y))$ for all $n$-bit inputs $x,y$ in time $T_A(n)=O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$, so the $n\\log n$ optimality conjecture fails in this model.",
    "Build two network-derived tape procedures that beat one pass per transform level, use them to compute convolution over $\\mathbb C[y]/(y^r+1)$ by synthetic transforms, reduce exact multiplication to that convolution through radix digits, a Chinese-remainder map, Gaussian resampling, chirps and a phase twist, then bound the error and sum the normalized costs.",
    "In a transform-based multiplier, merely scanning the $\\Theta(n)$ stored bits at each of $\\Theta(\\log n)$ transform levels costs $\\Theta(n\\log n)$, so going below $n\\log n$ needs savings in both address movement and butterfly arithmetic; the reduction isolates exactly those two operations.",
    "explicit",
    [S1, C, D, E, F],
    mot_quote="We therefore need savings in both movement and arithmetic.",
    frm=["n-log-n-barrier", "convolution", "multitape-turing-machine", "big-o-notation"],
    page="main-theorem",
    salient="The saving $\\kappa=2^{-182}$ in the exponent of $\\log n$ is minute, but it is a genuine power saving, which is already enough to refute the $n\\log n$ conjecture.",
    adds=[
        B("V", "logical volume", "The number of stored data bits of the array an operation acts on, excluding temporary work streams.", "count"),
        B("p", "working precision", "The number $6\\lceil\\log_2n\\rceil$ of fractional bits of the fixed-point complex coefficients.", "count"),
        B("d", "axis count", "The number $\\lfloor\\lceil\\log_2n\\rceil^{\\epsilon}\\rfloor$ of transform axes, $\\Theta(p^{\\epsilon})$.", "count"),
        B("r", "record length", "The power of two $2^{\\ell}$ giving the number of complex coefficients of each polynomial record in $\\mathbb C[y]/(y^r+1)$.", "count"),
        B("\\ell", "record exponent", "The exponent $\\log_2r$, which also bounds the number of rounds of each synthetic transform.", "count"),
        B("T", "padded box size", "The power of two $\\prod_it_i$ of complex entries in the padded transform array, with $Tp=\\Theta(n)$.", "count"),
        B("t_i", "power-of-two axis length", "The length $r/2$ or $r$ of axis $i$ of the padded box."),
        B("K", "chunk width", "The number $\\lfloor d^c\\rfloor$ of address bits in each chunk on which a simultaneous layer selects one bit.", "count"),
        B("\\tau", "interchange exponent", "The fixed exponent $1-2^{-50}$ in the address-interchange cost $O(Vu^{\\tau})$."),
        B("\\lambda'", "layer exponent", "The fixed exponent $1-2^{-54}$ in the simultaneous-layer cost $O(Vd^{\\lambda'})$."),
    ])

ANSWER = {"root": ROOT}

# ---------------------------------------------------------------- validation
PAGES = """n-log-n-barrier convolution negacyclic-ring coefficient-twist signed-packing tape-address-model controlled-cyclic-shift scratch-restoring-exchange array-frames rank-and-orthogonal-subspaces subset-intersection-labels address-shear-factorization rank-saving-recurrence power-width-interchange address-chunk-interchange crt-axis-map packed-selected-bit-addition fixed-point-complex-arithmetic phase-frame-network discrete-fourier-transform fft-butterflies synthetic-polynomial-transform simultaneous-butterfly-layer bluestein-chirp stored-frequency-order transform-tape-layout contraction-error-propagation gaussian-resampling permutation-cancellation normalized-ring-convolution parameter-regime radix-digit-reduction tensor-source-transform precision-exact-recovery multiplication-algorithm cost-accounting main-theorem""".split()
KNOWN = """big-o-notation polynomials complex-numbers multitape-turing-machine binary-numerals-and-bit-strings positional-notation-in-any-radix integer-division-with-remainder-floor-and-ceiling modular-arithmetic arithmetic-modulo-2-and-xor primes-coprimality-and-gcd roots-of-unity-and-euler-s-formula exponential-logarithm-and-gaussian-function asymptotic-notation-beyond-big-o geometric-series-and-sums divide-and-conquer-and-recurrences schoolbook-and-karatsuba-multiplication sorting-and-its-cost permutations-and-bijections sets-subsets-and-cartesian-products multidimensional-arrays-and-row-major-order matrices-vectors-and-linear-maps triangular-and-permutation-matrices dot-product-inner-product-and-orthogonality dyadic-rationals-and-fixed-width-numerators matrix-transposition triangle-inequality-and-norms mathematical-induction-and-proof-by-contradiction cyclic-shifts-and-rotations-of-lists subroutines-and-composition-of-algorithms""".split()
IDX = {p: i for i, p in enumerate(PAGES)}

errors = []
ids = set()
pages_used = {}
from_used = set()
order = []


def walk(n, anc_page, depth=0):
    if n["id"] in ids:
        errors.append("dup id " + n["id"])
    ids.add(n["id"])
    page = n.get("page") or anc_page
    if n.get("page"):
        if n["page"] in pages_used:
            errors.append("page twice " + n["page"])
        pages_used[n["page"]] = n["id"]
        if anc_page and n["page"] != anc_page and IDX[n["page"]] > IDX[anc_page]:
            errors.append("child page after ancestor page: %s %s > %s" % (n["id"], n["page"], anc_page))
    for f in n.get("from", []):
        from_used.add(f)
        if f in KNOWN:
            continue
        if f not in IDX:
            errors.append("unknown from %s in %s" % (f, n["id"]))
        elif IDX[f] >= IDX[page]:
            errors.append("from %s not before page %s in %s" % (f, page, n["id"]))
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        nq = norm(q)
        pos = NSRC.find(nq)
        cnt = NSRC.count(nq)
        if pos < 0:
            errors.append("quote not found %s: %s" % (n["id"], q))
        if cnt > 1:
            print("WARN quote occurs %d times: %s" % (cnt, n["id"]))
        order.append((n["id"], pos, n.get("deferred", False)))
        if n.get("children"):
            errors.append("infer has children " + n["id"])
    else:
        m = n["motivation"]
        if m.get("quote"):
            if NSRC.find(norm(m["quote"]["quote"])) < 0:
                errors.append("motivation quote not found %s" % n["id"])
        if m["source"] == "explicit" and not m.get("quote"):
            errors.append("explicit without quote " + n["id"])
        # adds check
        desc_claims = []

        def collect(c):
            for ch in c.get("children", []):
                desc_claims.append(ch["claim"])
                collect(ch)
        collect(n)
        maths = " ".join(" ".join(re.findall(r'\$([^$]*)\$', c)) for c in desc_claims)
        for a in n.get("adds", []):
            if a["symbol"] not in maths:
                errors.append("adds symbol %s not in descendant maths of %s" % (a["symbol"], n["id"]))
        for ch in n["children"]:
            walk(ch, page, depth + 1)


walk(ROOT, None)
for p in PAGES:
    if p not in pages_used and p not in from_used:
        errors.append("page unused " + p)
last = -1
for id_, pos, dfr in order:
    if dfr:
        continue
    if pos < last:
        errors.append("order violation at %s (%d < %d)" % (id_, pos, last))
    last = max(last, pos)
print("pages without step:", [p for p in PAGES if p not in pages_used])
print("errors:", *errors, sep="\n  ")
out = os.path.join(PROJ, 'exegenius', 'tasks', '0003-argument.answer.json')
with open(out, 'w') as fh:
    json.dump(ANSWER, fh, indent=1, ensure_ascii=False)
print("wrote", out, "infer steps:", len(order))
