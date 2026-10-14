import json, re, sys
ROOT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/FB1F8"
SRC = open(ROOT + "/sources/paper.tex", encoding="utf-8").read()
LINES = SRC.split("\n")
P = "paper"
NORM_SRC = re.sub(r"\s+", " ", SRC)

ORDER = []  # (line, id, deferred)
FAIL = []

def Q(ls, le, start=None, end=None):
    """Quote lines ls..le (1-based, inclusive), optionally trimmed from `start` to `end` (inclusive), whitespace collapsed."""
    txt = re.sub(r"\s+", " ", "\n".join(LINES[ls - 1:le]))
    if start is not None:
        start = re.sub(r"\s+", " ", start)
    if end is not None:
        end = re.sub(r"\s+", " ", end)
    if start is not None:
        i = txt.find(start)
        if i < 0:
            FAIL.append(("start not found", ls, start)); return "??"
        txt = txt[i:]
    if end is not None:
        j = txt.find(end)
        if j < 0:
            FAIL.append(("end not found", ls, end)); return "??"
        txt = txt[: j + len(end)]
    txt = re.sub(r"\s+", " ", txt).strip()
    assert NORM_SRC.count(txt) >= 1, ("quote missing", ls)
    return txt

def ev(ls, le, start=None, end=None):
    return {"source": P, "quote": Q(ls, le, start, end)}

def bind(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

def show(id, claim, method, mot_text, mot_src, children, page=None, frm=None, salient=None, adds=None, mot_quote=None):
    m = {"text": mot_text, "source": mot_src}
    if mot_src == "explicit":
        assert mot_quote is not None
        m["quote"] = mot_quote
    else:
        m["quote"] = None
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": m,
         "children": children, "page": page, "from": frm or [], "salient": salient, "quote": None}
    if adds:
        n["adds"] = adds
    return n

def infer(id, claim, quote, page=None, frm=None, deferred=False, salient=None, line=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": quote, "page": page,
         "from": frm or [], "children": [], "method": None, "motivation": None, "salient": salient}
    if deferred:
        n["deferred"] = True
    ORDER.append((line, id, deferred))
    return n

# ---------------------------------------------------------------- S1.1 scalar exchange
S1_1 = show("S1.1",
    r"For arbitrary initial values of its auxiliary wires, the eight-row forward schedule changes $y_S$ to $y_S+x_S$ and nothing else, and the three stages (forward, inverse forward with the banks exchanged, forward) send $(X_a,Y_a)\mapsto(-Y_a,X_a)$ while restoring every auxiliary value; over $\mathbb F_2$ this is the permutation exchanging $X_a$ and $Y_a$.",
    "Write the schedule as: subtract the effect of the old scratch values, copy and gather the sources, scatter and side-inject into the targets, undo gather and copy; compute the net target change as a linear map independent of the initial scratch values, and evaluate its coefficient from $x_T$ to $y_S$ by the intersection size $|S\\cap T|$.",
    "Scratch wires start with arbitrary contents, so the schedule first subtracts whatever effect those contents would have on the targets, then adds the source contribution, then undoes its own changes to the scratch wires; this is the linear form of the transparent-computation restoration of Buhrman, Cleve, Koucky, Loff and Speelman.",
    "explicit",
    [
     infer("S1.1.1",
        r"The net change of the target bank is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independent of the initial side and central values $a,c$: rows 0 and 1 subtract $\mathcal Ja+\mathcal Rc$, rows 2 and 3 change the scratch values to $a+\mathcal Vx$ and $c+\mathcal Gx$, rows 4 and 5 add $\mathcal R(c+\mathcal Gx)+\mathcal J(a+\mathcal Vx)$, and rows 6 and 7 restore $c,a$.",
        ev(744, 750, "If the initial side", "$a,c$."), line=744),
     infer("S1.1.2",
        r"The central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod2$ in the bit case and $(|S\cap T|-1)/2$ in the complex case; the side wires cancel exactly the neighboring cases ($|S\cap T|=1$ for bits, $|S\cap T|\in\{0,2\}$ for the complex network), the remaining distinct triples already have coefficient zero, and the self coefficient is one, so both net maps are $y\leftarrow y+x$.",
        ev(752, 759, "In the bit case", "$y\\gets y+x$."), line=752),
     infer("S1.1.3",
        r"The inverse schedule with logical source $Y$ and target $X$ effects $X\leftarrow X-Y$, so the three stages take $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$, and each invocation restores its own auxiliary wires.",
        ev(761, 764, "The inverse schedule", "auxiliary wires."), line=761),
    ],
    page="scratch-restoring-exchange",
    frm=["arithmetic-modulo-2-and-xor", "sets-subsets-and-cartesian-products", "matrices-vectors-and-linear-maps", "dyadic-rationals-and-fixed-width-numerators"],
    salient="Auxiliary wires may start with arbitrary values and are returned to them exactly, so when rows of a real array are later assigned to scratch roles no initialization is needed.",
    adds=[bind("X_a,Y_a", "data banks", "the two banks of data wires, indexed by triples of triples $a\\in\\mathcal T^3$"),
          bind("x_T", "source value", "the control value of the source wire whose varying triple is $T$"),
          bind("y_S", "target value", "the value updated on the target wire whose varying triple is $S$")],
    mot_quote=ev(705, 708, "The first two rows", "restore the scratch values."))

# ---------------------------------------------------------------- S1.2 frames
S1_2 = show("S1.2",
    r"Replacing each scalar by an array in $R^\Omega$ and assigning an invertible frame $D_v$ at each source, gate and sink, with the edge from $u$ to $v$ applying $D_vD_u^{-1}$ and the input interpreted as $g=D_{\rm in}^{-1}f$, the network implements $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$; when the scalar network is a signed role permutation $\rho$, the route from role $w$ applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$, on every role including the auxiliary ones.",
    "Maintain the invariant that the stored array at a vertex equals $D_v$ applied to the logical array there, using $R$-linearity so that a common frame commutes with each pointwise gate; then telescope the frames along each route.",
    "Because the frames cancel across every gate, the operator a role receives depends only on its source and sink frames, which leaves the intermediate frames free to be chosen so that every edge change is cheap.",
    "explicit",
    [
     infer("S1.2.1",
        r"At a vertex $v$ the stored array is $D_v$ applied to the logical array: on an edge with logical array $\varphi$ the operator changes $D_u\varphi$ to $D_v\varphi$, and at a gate $R$-linearity gives $\sum_jc_jD_v\varphi_j=D_v(\sum_jc_j\varphi_j)$, so the common frame commutes with the pointwise gate and the invariant continues to the sinks.",
        ev(806, 813, "At a vertex $v$, the invariant", "continues to the sinks."), line=806),
     infer("S1.2.2",
        r"The implemented operator is $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$; if the scalar network sends input role $w$ to output role $\rho(w)$ with sign $\varepsilon_w$, that route applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ to its input array, and all roles, including auxiliary roles, enter this identity.",
        ev(818, 825, "In particular, if the scalar network", "inexpensive."), line=818),
    ],
    page="array-frames",
    frm=["matrices-vectors-and-linear-maps", "multidimensional-arrays-and-row-major-order", "scratch-restoring-exchange"],
    adds=[bind("D_v", "frame", "the invertible linear operator on arrays assigned to vertex $v$, so that the stored array is $D_v$ applied to the logical array"),
          bind(r"\rho", "role permutation", "the permutation of roles induced by the scalar network, exchanging $X_a$ and $Y_a$ and fixing scratch roles"),
          bind(r"\mathsf S_\Omega", "array network", "the scalar network applied pointwise at every address of the common address set $\\Omega$")],
    mot_quote=ev(823, 825, "Once the scalar routing", "inexpensive."))

# ---------------------------------------------------------------- S1.3 labels and rank budget
S1_3 = show("S1.3",
    r"Nondegenerate subspace labels of the $m$-dimensional space $\mathcal F=F^{\otimes3}$, built from indicator vectors of triples, can be attached to every source, gate and sink so that every edge joins comparable labels, the only decreasing edges are the central-wire edges from time 3 to time 4 with loss $h$, and the sum of absolute dimension changes is $Wm-2N+2L$ with $L=Ich<N/2$; hence the edge rank sums are $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$ and $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$, and $s/W<m^\tau$ for $\tau=1-2^{-50}$.",
    "Use the bilinear form $\\langle x,y\\rangle=x^{\\mathsf T}(I-J/9)y$ on $\\mathbb Q^h$ (the dot product on $\\mathbb F_2^h$ for the complex network) so that neighboring triple lines are orthogonal; prescribe terminal labels $U_a$, $\\mathcal F$ on $X_a$, $0$, $U_a^\\perp$ on $Y_a$ and $0$, $\\mathcal F$ on scratch roles; expose one tensor factor per stage; tabulate the orthogonal residual of every edge; telescope the signed dimension changes at gates and count the decreasing edges.",
    "Each unit of residual dimension on an edge costs one smaller call, and the terminal labels force the signed total to be $Wm-2N$, so the saving must come from keeping the dimension lost on decreasing edges small relative to $N$.",
    "explicit",
    [
     infer("S1.3.1",
        r"With $\langle t_S,t_T\rangle=|S\cap T|-1$ and $\langle t_T,t_T\rangle=2$ over $\mathbb Q$, and $t_T\cdot t_T=1$ for the dot product over $\mathbb F_2$, every triple line is nondegenerate and neighboring triple lines are orthogonal in the label field of either construction.",
        ev(863, 871, "\\langle t_S,t_T\\rangle", "the label field."), line=863),
     infer("S1.3.2",
        r"The source label dimensions sum to $N$ and the sink dimensions to $Wm-N$, so the signed dimension changes sum to $Wm-2N$ because contributions at gates cancel; if decreasing edges lose a total dimension $L$, the absolute changes sum to $Wm-2N+2L$, and $L<N/2$ leaves a strict saving even after the rational interface adds $N$ source ranks.",
        ev(890, 897, "Write $W$ for the wire count", "both constructions."), line=890),
     infer("S1.3.3",
        r"The stage transitions $X\colon A\otimes\langle t\rangle\otimes Q\to(A\otimes F)\otimes Q$ and $Y\colon B\otimes\langle t\rangle\otimes Q\to((B\otimes F)\perp(P\otimes t^\perp))\otimes Q$ fit together: the outgoing labels are exactly the next stage's incoming labels, starting at $U_a$ on $X_a$ and $0$ on $Y_a$ and ending at $\mathcal F$ and $U_a^\perp$ as prescribed at the terminals.",
        ev(932, 937, "Thus the prescribed outgoing labels", "at the terminals."), line=932),
     infer("S1.3.4",
        r"In the residual table, label dimension is nondecreasing along every edge except center $3\to4$, which removes $P\otimes F\otimes Q$ of dimension $h$; the signed sum telescopes at every gate because each touched wire has one incoming and one outgoing incidence with the same gate label, so it equals $Wm-2N$, and the $Ic$ decreasing edges of loss $h$ add $2L$ with $L=Ich$ when signed changes are replaced by absolute ones.",
        ev(1061, 1071, "Label dimension is nondecreasing", "adds $2L$."), line=1061),
     infer("S1.3.5",
        r"The loss ratios are exactly $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both smaller than $1/2$ (and over $\mathbb F_2$ every nonzero residual contains a norm-one vector, hence has an orthonormal basis).",
        ev(1105, 1110, "The loss ratios", "smaller than $1/2$."), line=1105),
     infer("S1.3.6",
        r"Assigning the projection $P_U$ to each gate or sink with label $U$ and $-P_{U_a}$ to source $X_a$, the rank of an edge difference $P_V-P_U$ with $U\subset V$ equals $\dim V-\dim U$; the only exceptions are the $N$ negative source projections, whose first edge matrix $2P_{U_a}$ has rank one where the dimension change is zero, so $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$ with deficit $N-2L_{\rm b}>0$, and the endpoint difference is $I_m$ on every role.",
        ev(1157, 1171, "Lemma~\\ref{lem:scalar-motifs} gives", "proves the interface."), line=1157),
     infer("S1.3.7",
        r"For the complex network with binary labels and frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$, each edge's frame change $\mathcal C_V\mathcal C_U^{-1}$ is a product of one translation kernel $aI+bX_v$, or its inverse, per vector of an orthonormal basis of the residual; the number of factors sums to $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$, and after endpoint corrections every role receives $C^{\otimes m}$.",
        ev(1215, 1228, "For each edge of the complex network", "over columns."), line=1215),
     infer("S1.3.8",
        r"The relative deficits $\eta_{\rm b}=339/22587335000000$ and $\eta_{\rm c}=73/19906842167500$ both exceed $20\cdot2^{-50}$; since $m<2^{20}$, $m^{1-2^{-50}}=m\exp(-2^{-50}\log m)>m(1-20\cdot2^{-50})>m(1-\eta)$, so $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$ with $\tau=\sigma=1-2^{-50}$.",
        ev(1331, 1343, "Both exact deficits", "0<\\tau=\\sigma<1."), line=1331),
    ],
    page="subset-intersection-labels",
    frm=["rank-and-orthogonal-subspaces", "dot-product-inner-product-and-orthogonality", "array-frames", "scratch-restoring-exchange", "arithmetic-modulo-2-and-xor", "sets-subsets-and-cartesian-products", "matrices-vectors-and-linear-maps"],
    salient="Although the label dimensions must climb from a total of $N$ at the sources to $Wm-N$ at the sinks, the only edges that ever lose dimension are the central-wire returns, each losing exactly $h$, so the loss ratio $L/N$ is the fixed number $100/539$ or $101/539$ independent of everything else.",
    adds=[bind(r"\mathcal F", "label space", "the tensor cube $F^{\\otimes3}$ of the triple space, of dimension $m$, whose subspaces label vertices"),
          bind("t_T", "triple indicator", "the indicator vector in $F$ of the three-element subset $T$"),
          bind("U_a", "data line", "the line spanned by $u_a=t_{a_1}\\otimes t_{a_2}\\otimes t_{a_3}$, the source label of $X_a$"),
          bind("A", "earlier stage space", "the tensor space $F^{\\otimes(j-1)}$ of the stages before stage $j$"),
          bind("P", "earlier stage line", "the line spanned by the tensor of the earlier triple indicators inside $A$"),
          bind("B", "earlier complement", "the orthogonal complement $P^\\perp$ of $P$ inside $A$"),
          bind("Q", "later stage line", "the line spanned by the tensor of the later triple indicators"),
          bind("P_U", "projection", "the projection onto the nondegenerate subspace $U$ along $U^\\perp$, the rational matrix at a vertex with label $U$"),
          bind(r"\mathcal C_U", "phase frame", "the binary-label frame $H^{\\otimes m}\\operatorname{diag}_x(i^{q_U(x)})H^{\\otimes m}$ of the complex network"),
          bind(r"\eta", "relative deficit", "the fraction $(Wm-s)/(Wm)$ by which the rank sum falls short of $Wm$"),
          bind(r"\sigma", "complex exponent", "the rational exponent with $s_{\\rm c}/W_{\\rm c}<m^\\sigma$, equal to $\\tau$")],
    mot_quote=ev(849, 854, "A label is a nondegenerate", "relative to $N$."))

# ---------------------------------------------------------------- S1.4 shear factorization
S1_4 = show("S1.4",
    r"For two groups $H=(H_1,\ldots,H_m)$ and $D=(D_1,\ldots,D_m)$ of fields over $\mathbb Z/q^b\mathbb Z$ with every $H_i$ before every $D_j$, and a fixed rational matrix $A$ of rank $a$, the address shear $(H,D)\mapsto(H+AD,D)$ can be performed with exactly $a$ interchanges of pairs of $b$-digit fields, each between an $H$ field and a $D$ field, plus $O(V)$ further work.",
    "Factor $A=E_1\\Pi E_2$ with invertible lower triangular rational $E_1,E_2$ and a partial permutation $\\Pi$ with exactly $a$ ones; perform the triangular changes of coordinates by controlled shifts in descending coordinate order, modulo a fixed odd prime power avoiding all denominators; realize each one of $\\Pi$ by two controlled additions around one field interchange.",
    "A controlled shift costs $O(V)$ only when its target field follows its control fields, so a change of coordinates must be lower triangular in tape order; the Bruhat-type factorization isolates all of the rank in a partial permutation, which is the only part that needs interchanges.",
    "explicit",
    [
     infer("S1.4.0",
        r"If a target field $y\in[Q]$, $Q=q^b$, follows its control fields, the update $y\mapsto y+a(\text{controls})\pmod Q$ costs $O(V)$ whenever the offset is prepared in $b^{O(1)}$ time: for each prefix the fiber of $Q$ blocks is split at $Q-a$ and the two pieces are merged in the opposite order, becoming the ranges $[0,a)$ and $[a,Q)$ of the new target coordinate.",
        ev(575, 584, "Fix all fields before the target", "offset work."),
        page="controlled-cyclic-shift",
        frm=["tape-address-model", "modular-arithmetic", "cyclic-shifts-and-rotations-of-lists"],
        deferred=True, line=575),
     infer("S1.4.1",
        r"Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ having exactly $a$ ones, at most one per row and column: choose the topmost nonzero row and its rightmost nonzero entry as pivot, clear with lower triangular elementary matrices on both sides, delete the pivot row and column and repeat, each step isolating a rank-one block.",
        ev(1384, 1391, "Delete the pivot row", "required form."), line=1384),
     infer("S1.4.2",
        r"Transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$; each one at $(i,j)$ of $\Pi$ is $H_i\leftarrow H_i+D_j$, implemented by $D_j\leftarrow D_j+H_i$, $(H_i,D_j)\leftarrow(D_j,H_i)$, $D_j\leftarrow H_i-D_j$, which on $(h,d)$ yields $(h+d,d)$ with one interchange, so the number of recursive calls is the rational rank $a$ and temporary tapes do not multiply it.",
        ev(1432, 1446, "For $A=E_1\\Pi E_2$, first transform", "multiply that count."), line=1432),
    ],
    page="address-shear-factorization",
    frm=["triangular-and-permutation-matrices", "controlled-cyclic-shift", "modular-arithmetic", "tape-address-model", "primes-coprimality-and-gcd", "matrices-vectors-and-linear-maps"],
    adds=[bind("H,D", "field groups", "the two ordered groups of $m$ address fields forming the two chunks, every $H_i$ before every $D_j$"),
          bind("q", "field radix", "the fixed odd prime in which the address fields are written, avoiding all denominators of the fixed rational matrices"),
          bind("b", "field width", "the number of radix-$q$ digits in one field, so each field ranges over $[q^b]$", "count"),
          bind("a", "edge rank", "the rational rank of the edge matrix, equal to the number of smaller interchanges it needs", "count"),
          bind(r"\Pi", "partial permutation", "the $0/1$ matrix with exactly $a$ ones, at most one per row and column, in the factorization $A=E_1\\Pi E_2$")],
    mot_quote=ev(1357, 1359, "Lemma~\\ref{lem:ordered-affine-streams} updates", "in this direction."))

# ---------------------------------------------------------------- S1.5 power-width interchange
S1_5 = show("S1.5",
    r"Given fixed circuit data with $M_{\mathrm{out}(\rho(w))}-M_{\mathrm{in}(w)}=I_m$ for every input role and $s<Wm$, and a rational $\tau\in(0,1)$ with $s/W<m^\tau$, two disjoint contiguous chunks of $e=m^k$ radix-$q$ digits, preceded by a row field of length divisible by $W^k$, can be interchanged in $O(Ve^\tau)$ time on a fixed number of tapes, with a constant independent of all field lengths.",
    "Split whole rows cyclically into $W$ role streams of volume $V/W$; on each circuit edge apply the shear $\\Phi_{A_e}$ by the factorization lemma, recursively interchanging each pivot pair of $b=e/m$ digit fields; execute gates pointwise; merge the roles back to obtain $H\\leftarrow H+D$ on every row; complete the interchange with two linear updates; bound the per-node overhead by $O(V)$ with a depth-first schedule and solve the recurrence $F_k\\le(s/W)F_{k-1}+O(1)$.",
    "The frame identity makes every role receive the same shear once the endpoint matrices differ by $I_m$, the rank of each edge difference counts the smaller interchanges, and distributing rows among the $W$ roles gives each recursive call volume $V/W$, which is what converts $s<Wm$ into a saving per unit of volume.",
    "recoverable",
    [
     infer("S1.5.1",
        r"Splitting whole rows cyclically into $W$ role streams within each prefix, with row $r=Wg+(w-1)$ sent to stream $w$ as row $g$, yields streams of exactly the same remaining shape, including the full ranges of $H$ and $D$, each of logical volume $V/W$ and with row count divisible by $W^{k-1}$.",
        ev(1497, 1502, "Split whole rows cyclically", "divisible by $W^{k-1}$."), line=1497),
     infer("S1.5.2",
        r"With the frame $\Phi_M$ at a vertex with matrix $M$, a common address permutation commutes with every pointwise bit gate, the logical arrays are $g_w=\Phi_{-M_{\mathrm{in}(w)}}f_w$ with no initial tape operation, and the physical output is $f'_{\rho(w)}=\Phi_{M_{\mathrm{out}(\rho(w))}}\Phi_{-M_{\mathrm{in}(w)}}f_w=\Phi_{I_m}f_w$; merging row $g$ of role $\rho(w)$ back to row $Wg+(w-1)$ undoes $\rho$, so the result is $H\leftarrow H+D$ on every original row, including rows assigned to scratch roles whose initial values were arbitrary.",
        ev(1514, 1533, "The row split supplies", "were arbitrary."), line=1514),
     infer("S1.5.3",
        r"The full interchange is $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ componentwise, which sends $(H,D)$ to $(D,H)$; only the middle shear uses the circuit, and the other two updates target the later group at linear cost.",
        ev(1535, 1541, "To interchange the two full chunks", "to $(D,H)$."), line=1535),
     infer("S1.5.4",
        r"The number of recursive calls is the sum of the edge ranks, exactly $s$, each on one role stream of volume $V/W$ with all other fields as spectators; splitting, merging, gates and triangular operations cost $O(V)$ because their number is fixed, so if $F_k$ bounds time divided by logical volume then $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.",
        ev(1543, 1553, "The number of recursive calls", "F_k\\le(s/W)F_{k-1}+O(1)."), line=1543),
     infer("S1.5.5",
        r"For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^ka^j$ is $O(m^{k\tau})$: if $a\le1$ it is at most $k+1=O(m^{k\tau})$, and if $a>1$ it is $O(a^k)$; hence $F_k=O(e^\tau)$.",
        ev(1554, 1557, "For $a=s/W<m^\\tau$", "$F_k=O(e^\\tau)$."), line=1554),
     infer("S1.5.6",
        r"In the depth-first fixed-tape schedule, each push, pop, copy, positioning operation or erasure moves $O(V)$ symbols at a parent node and there are only the fixed number $s$ of child calls, which gives the additional $O(V)$ term even though each child has volume $V/W$; temporary storage is therefore not substituted for logical volume in the factor $s/W$.",
        ev(1584, 1588, "Each push, pop, copy", "factor $s/W$."), line=1584),
    ],
    page="power-width-interchange",
    frm=["array-frames", "subset-intersection-labels", "address-shear-factorization", "rank-saving-recurrence", "tape-address-model", "divide-and-conquer-and-recurrences", "geometric-series-and-sums"],
    salient="Rows assigned to scratch roles hold genuine data with arbitrary values, yet the final permutation is exact on them too, because the scalar network restores every scratch wire.",
    adds=[bind(r"\Phi_M", "shear frame", "the address permutation moving the entry at $(H,D)$ to $(H+MD,D)$, used as the frame at a vertex with matrix $M$"),
          bind("F_k", "normalized cost", "a uniform upper bound on time divided by logical volume for chunk width $m^k$"),
          bind("g", "row within role", "the quotient in the row number $r=Wg+(w-1)$, the row index inside a role stream", "count"),
          bind("w", "role index", "the remainder in the row number $r=Wg+(w-1)$, the role stream a row is sent to")])

# ---------------------------------------------------------------- S1 key step
S1 = show("S1",
    r"A fixed linear network with $W$ wires, labelled by subspaces of an $m$-dimensional space so that the edge changes need $s<Wm$ smaller calls in total, turns one call at parameter $e=m^k$ on logical volume $V$ into $s$ calls at parameter $e/m$ on role streams of volume $V/W$; the resulting recurrence $F_k\le(s/W)F_{k-1}+O(1)$ for cost per unit volume has solution $F_k=O(e^\tau)$ with $\tau=1-2^{-50}<1$, and in particular two address chunks of $m^k$ digits are interchanged in $O(Ve^\tau)$ time.",
    "Build a scalar three-stage bank exchange that restores its scratch wires; lift scalars to arrays with a frame at each vertex so that only endpoint operators remain on every role; attach nested subspace labels built from three-element subsets so that the total residual dimension is $Wm-2N+2L$ with $L<N/2$; implement each unit of an edge's rank by one smaller interchange after a triangular factorization; split rows among the $W$ roles so each smaller call has volume $V/W$ and solve the recurrence by a geometric sum.",
    "Dividing cost by volume, a call at parameter $mf$ contributes $s/W$ times the normalized cost at parameter $f$; because $s/W<m$ this contribution grows more slowly than the parameter, which is exactly a power saving, and the sources name this strict inequality as the source of the saving.",
    "explicit",
    [S1_1, S1_2, S1_3, S1_4, S1_5],
    page="rank-saving-recurrence",
    frm=["divide-and-conquer-and-recurrences", "geometric-series-and-sums", "tape-address-model", "matrices-vectors-and-linear-maps", "rank-and-orthogonal-subspaces", "subroutines-and-composition-of-algorithms"],
    salient="The saving comes from a strict but minuscule deficit: $s/W$ falls below $m$ by a relative margin of only $339/22587335000000$ for the bit network, yet any strict inequality turns the geometric sum into a power $\\tau<1$ of the chunk width, and the same deficit serves both the address and the arithmetic procedure.",
    adds=[bind("W", "wire count", "the number of wires of the fixed network, scratch wires included; the number of role streams", "count"),
          bind("m", "label dimension", "the dimension $h^3$ of the label space; also the number of fields a chunk is divided into", "count"),
          bind("s", "rank budget", "the total number of smaller calls over all edges, the sum of edge ranks or residual dimensions", "count"),
          bind("V", "logical volume", "the number of stored data bits of the array a call acts on", "count"),
          bind("N", "data pair count", "the number $v^3$ of data wire pairs $(X_a,Y_a)$", "count"),
          bind("L", "lost dimension", "the total label dimension lost over all decreasing edges", "count"),
          bind("h", "ground-set size", "the size $100$ of the ground set whose three-element subsets index the banks", "count"),
          bind("I", "invocation count", "the number $3v^2$ of invocations of the scalar schedule in the three stages", "count"),
          bind("c", "central wires", "the number of central wires per invocation, $100$ or $101$", "count"),
          bind("e", "chunk width", "the number of digits in each of the two chunks, $e=m^k$ at a power-width call", "count"),
          bind("k", "recursion depth", "the exponent with $e=m^k$, the number of recursion levels", "count"),
          bind(r"\tau", "interchange exponent", "the fixed rational exponent $1-2^{-50}$ with $s/W<m^\\tau$, giving the cost $O(Ve^\\tau)$")],
    mot_quote=ev(173, 175, "After dividing cost by volume", "source of the power saving."))

# ---------------------------------------------------------------- S2 arbitrary width interchange
S2 = show("S2",
    r"There are a fixed $0<\tau<1$ and one fixed multitape procedure that, for all positive integers $P,G,B$ and $u\ge1$, applies the address permutation $(p,h,g,d,z)\mapsto(p,d,g,h,z)$ to an arbitrary bit array on $[P]\times[2^u]\times[G]\times[2^u]\times[B]$ in $O(Vu^\tau)$ steps, $V=PGB\,2^{2u}$, including shape processing, all padding and unpadding, and workspace cleanup.",
    "Supply the row field from the top $\\rho=O(\\log(2e))$ digits of the two chunks, pad rows to a multiple of $W^k$, write the remaining width in base $m$ and apply the power-width interchange to each corresponding pair of pieces, then unpad and separate the high parts again; handle binary chunks by numerical padding of each range to $[q^e]$, and widths differing by one bit by one single-bit move.",
    "The power-width proposition needs a row field divisible by $W^k$ and widths that are powers of $m$; a few high digits of the chunks themselves supply the rows at logarithmic cost, and a base-$m$ expansion of the width gives a geometric sum of power-width costs dominated by its top term.",
    "explicit",
    [
     infer("S2.1",
        r"With $k=\lceil\log_me\rceil$ and $\rho=\lceil k\log W/(2\log q)\rceil$, exchanging and joining the top $\rho$ digits of each chunk forms a row field of range $R=q^{2\rho}\ge W^k$ before both remaining chunks at cost $O(V\rho)$, and appending zero rows within each prefix to $R'=W^k\lceil R/W^k\rceil<2R$ keeps the padded logical volume below $2V$.",
        ev(1677, 1690, "In the two middle orders", "less than $2V$."), line=1677),
     infer("S2.2",
        r"Writing $e-\rho=\sum_{j=0}^ka_jm^j$ in base $m$ and applying the power-width interchange to the $a_j$ corresponding pairs of width $m^j$, all with the common row field of length $R'$, the costs sum to $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$ because $a_j<m$ and $m^k<me$; every completed call preserves its row address, so padded zero rows remain zero and no genuine row mixes with a padded one.",
        ev(1696, 1708, "Apply\nProposition", "stated order."), line=1696),
     infer("S2.3",
        r"For binary chunks, pad each chunk range numerically from $[2^u]$ to $[q^e]$ with $e$ least such that $q^e\ge2^u$, a fixed volume factor below $q^2$ that preserves the order of existing entries; interchange, then scan away the entries with an invalid coordinate; since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$.",
        ev(1721, 1734, "Finally, for binary chunks", "$O(Vu^\\tau)$."), line=1721),
     infer("S2.4",
        r"Chunks whose widths differ by one bit are interchanged by one single-bit move of the longer chunk's leading bit, costing $O(V)$, plus one equal-width interchange, with the gap field $g$ remaining between the two full chunks; no unrestricted array transpose is used.",
        ev(1756, 1762, "Here the first step moves", "in these operations."), line=1756),
    ],
    page="address-chunk-interchange",
    frm=["power-width-interchange", "rank-saving-recurrence", "tape-address-model", "positional-notation-in-any-radix", "geometric-series-and-sums"],
    salient="Although the final effect is an exact permutation of the array, the intermediate steps form XOR combinations of the data bits, which places the procedure outside models restricted to moving data without computation, where an $n\\log n$ lower bound is known.",
    adds=[bind("u", "chunk bit width", "the number of bits in each of the two interchanged address chunks", "count"),
          bind(r"\rho", "high-digit count", "the number of top digits of each chunk that are exchanged first and joined to form the row field", "count"),
          bind("q", "field radix", "the fixed odd prime radix of the padded chunk digits"),
          bind("R", "row range", "the range $q^{2\\rho}$ of the row field formed from the high digits", "count"),
          bind("R'", "padded row range", "the row count after padding to a multiple of $W^k$", "count")],
    mot_quote=ev(1627, 1629, "We have proved the fast operation", "the final bound."))

# ---------------------------------------------------------------- S3.1 phase frames
S3_1 = show("S3.1",
    r"With $C=H\mathsf SH=aI+bX$, $a=(1+i)/2$, $b=(1-i)/2$, the Gaussian-dyadic identities $H_0=b\mathsf SC\mathsf S$ and $C^{-1}=-iZCZ$ hold; an edge from label $U_-$ to $U_+$ has frame change $\prod_j(aI+bX_{v_j})^{\epsilon_j}$ over an orthonormal basis of its residual, which after a binary change of coordinates $\mathcal P_M$ becomes $\prod_jC_{e_j}^{\epsilon_j}$ on coordinate directions; so one network invocation on $e=mf$ selected axes yields $C^{\otimes e}$ on every role with exactly $s_{\rm c}$ child calls on $f$ axes each, and $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ converts the completed $C$-layer to normalized butterflies.",
    "Conjugate the translation kernels by the address permutation $\\mathcal P_M$ whose first columns are the residual basis; implement $M$ by elementary row additions on the selected bits of whole slots; obtain each inverse child from one forward child by $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$; wrap the endpoint $C^{\\otimes D}$ in the diagonal phases $\\mathcal S_D$ and the scalar $b^D$.",
    "Working with the kernel $C$ instead of $H_0$ keeps every intermediate value an exact Gaussian dyadic, and the Hadamard conjugations defining the phase frames are only proof devices, so the machine executes nothing but signed shifts, halvings, multiplications by $i$ and address moves.",
    "explicit",
    [
     infer("S3.1.1",
        r"Extending the residual basis $v_1,\ldots,v_{\rho_{\rm edge}}$ to a basis of $\mathbb F_2^m$ as the first columns of $M$, the conjugation $\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}$ turns the edge identity into $\mathcal C_{U_+}\mathcal C_{U_-}^{-1}=\mathcal P_M(\prod_jC_{e_j}^{\epsilon_j})\mathcal P_M^{-1}$ on standard directions; $M$ need only be invertible, not orthogonal.",
        ev(1855, 1865, "Extend $v_1", "its invertibility."), line=1855),
     infer("S3.1.2",
        r"On a group of $e=mf$ consecutive chunks divided into $m$ slots of $f$ chunks, apply $\mathcal P_M^{-1}$ to each column, then $(C^{\epsilon_h})^{\otimes f}$ to the $f$ selected bits of slot $h$ as one child operation for each $h\le\rho_{\rm edge}$, then $\mathcal P_M$; a negative kernel needs only one forward child because $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$, and all inverse wrappers are address signs and constant fourth-root phases adding no recursive calls.",
        ev(1878, 1890, "To implement", "no recursive calls."), line=1878),
     infer("S3.1.3",
        r"Any $M\in\operatorname{GL}(m,\mathbb F_2)$ is a product of at most $m(m-1)+3m$ elementary row additions, a fixed number since $m$ is fixed; adding row $h'$ to row $h$ in every column applies $x_{h,j}\leftarrow x_{h,j}\oplus x_{h',j}$ for all $0\le j<f$, changing corresponding selected positions in two whole slots, which the packed address operation performs together.",
        ev(1892, 1901, "Gaussian elimination expresses", "together."), line=1892),
     infer("S3.1.4",
        r"Summing the residual dimensions gives exactly $s_{\rm c}$ child calls on $f=e/m$ axes each; the source and sink $Z_{a,f}$ signs with the scalar $i^{27f}$ turn every endpoint kernel into a forward one, and negating the prescribed bank and undoing its exchange returns $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary.",
        ev(1903, 1914, "Apply the finite network", "were arbitrary."), line=1903),
     infer("S3.1.5",
        r"With $(\mathcal S_Dz)(x)=i^{x_1+\cdots+x_D}z(x)$ on the selected bits, $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, where $b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}$ is a binary shift and fourth-root phase with at most one factor $b$, so the complete parallel butterfly layer is exact up to its prescribed final truncation.",
        ev(1927, 1940, "Applying\n\\eqref{eq:phase-basic-identities}", "final truncation."), line=1927),
    ],
    page="phase-frame-network",
    frm=["array-frames", "subset-intersection-labels", "rank-and-orthogonal-subspaces", "complex-numbers", "dyadic-rationals-and-fixed-width-numerators", "fixed-point-complex-arithmetic", "matrices-vectors-and-linear-maps", "arithmetic-modulo-2-and-xor", "triangular-and-permutation-matrices"],
    salient="A decreasing edge, whose kernel is an inverse $C^{-1}$, still costs exactly one forward child call, because $C^{-1}=-iZCZ$ turns it into a forward kernel wrapped in address signs and a constant phase.",
    adds=[bind("C", "two-point kernel", "the matrix $H\\mathsf SH=aI+bX$ with $a=(1+i)/2$, $b=(1-i)/2$, whose tensor powers the network computes"),
          bind("M", "basis-change matrix", "an invertible binary matrix whose first columns are the residual basis, implemented as an address permutation $\\mathcal P_M$"),
          bind("X_v", "translation", "the address translation $(X_vf)(x)=f(x+v)$ by a binary vector $v$"),
          bind("e", "group size", "the number $mf$ of selected axes in one network invocation", "count"),
          bind(r"\mathcal S_D", "diagonal phase", "the operator multiplying the value at an address by $i^{x_1+\\cdots+x_D}$ for its selected bits"),
          bind("Z", "sign matrix", "the diagonal matrix $\\operatorname{diag}(1,-1)$, an address-dependent sign")],
    mot_quote=ev(1830, 1833, "These identities use only", "by the machine."))

# ---------------------------------------------------------------- S3.2 packed selected-bit addition
S3_2 = show("S3.2",
    r"On $R$-bit records on $[N_0]\times[2^L]_{\chi_1}\times[N_1]\times[2^L]_{\chi_2}\times[N_2]\times[2^L]_{\chi_3}\times[N_3]$ with $L=fK$, $K\ge6$, one fixed procedure performs $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ at the $f$ selected positions $j_i=\rho+iK$ at once, preserves spectators, other chunk bits and every payload, restores the chunk $z$ for every initial value, and costs $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$, which is $O(V(L^\tau+1))$ when $R$ exceeds every fixed polynomial in $p$, $f\le d\le p$ and $K/\log p\to\infty$.",
    "Apply eight whole-chunk cyclic shifts whose offsets are sums of $2^{j_i}$ over selected bits of the other two chunks; their composition $S_0$ equals the ideal XOR permutation $T_0$ except on a guard-violating set $\\mathcal B$ of fraction at most $80(f-1)2^{-K}$; since $T_0S_0^{-1}$ permutes $\\mathcal B$, extract those records with destination ranks, radix sort them and reinsert; finish the top position by an elementary two-bit XOR.",
    "A cyclic shift of a whole chunk range by a control-dependent offset is a linear-cost primitive, and adding $2^{j_i}$ to a chunk flips bit $j_i$ unless a carry crosses a segment boundary, so a packed addition is right except where guard digits are near their boundary; that exceptional set is small and determined by addresses alone, so it is repaired deterministically.",
    "explicit",
    [
     infer("S3.2.1",
        r"For a Boolean control $c$ and arbitrary integers $u,w$, the eight parity-controlled additions compose the cycles $(00\ 01\ 10)$ and $(01\ 10\ 11)$ on each parity square into $(00\ 10)(01\ 11)$, so the output is $(u',w')=(u+c(1-2(u\bmod2)),w)$: the parity of $u$ flips exactly when $c=1$, both quotients by two are preserved, the auxiliary integer $w$ is restored, and each coordinate moves by at most four.",
        ev(2041, 2052, "Consequently the complete output", "will suffice below."), line=2041),
     infer("S3.2.2",
        r"Outside the set $\mathcal B$ of addresses where some used guard value violates $10\le g\le2^{K-1}-11$, each $K$-bit segment starts in $[20,2^K-21]$ and a displacement of eight keeps it inside $[0,2^K-1]$, so no segment carries into or borrows from the next and the composed shifts $S_0$ agree with the ideal permutation $T_0$; the union bound over the $2(f-1)$ guards, each with twenty excluded values out of $2^{K-1}$, gives $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, independently of record values.",
        ev(2087, 2105, "At an address outside", "enters this count."), line=2087),
     infer("S3.2.3",
        r"$T_0$ preserves all guard values and hence $\mathcal B$; both $T_0$ and $S_0$ are bijections agreeing off $\mathcal B$, so $S_0(\mathcal B^c)=\mathcal B^c$ and $S_0(\mathcal B)=\mathcal B$, and $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$.",
        ev(2107, 2114, "The ideal map $T_0$", "permutes $\\mathcal B$."), line=2107),
     infer("S3.2.4",
        r"Each rotation is realized by moving its target chunk last with at most two width-$L$ chunk swaps at $O(VL^\tau)$ and one $O(V)$ controlled shift whose offset is computed from the two control values in $L^{O(1)}$ time; the exceptional records are extracted with $O(A_{\rm rect})$-bit destination ranks, stably radix sorted and reinserted in one scan; so the movement costs $O(V(L^\tau+1))$, the record scans $O(MA_{\rm rect}^3+V)$ and the sort $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$, and after division by $V=MR$ the extra terms are $A_{\rm rect}^3/R\to0$ and $O(p^22^{-K}(1+A_{\rm rect}/R))=o(1)$ under the family bounds.",
        ev(2195, 2207, "The movement costs", "final assertion."), line=2195),
    ],
    page="packed-selected-bit-addition",
    frm=["address-chunk-interchange", "controlled-cyclic-shift", "tape-address-model", "sorting-and-its-cost", "arithmetic-modulo-2-and-xor", "modular-arithmetic", "permutations-and-bijections"],
    salient="Eight controlled rotations flip the selected bit of each of $f-1$ segments simultaneously while an arbitrary auxiliary chunk returns exactly to its initial value, and the repair of the exceptional addresses never reads a payload, so the bound is worst-case over all data.",
    adds=[bind("L", "slot width", "the number $fK$ of address bits in one slot, the width of each of the three chunks", "count"),
          bind("R", "record width", "the number of payload bits in one record", "count"),
          bind("M", "record count", "the number $2^{3L}\\prod_hN_h$ of records in the rectangle", "count"),
          bind("A_{\\rm rect}", "address width", "the bit length $\\lceil\\log_2(2V)\\rceil$ of a record rank", "count"),
          bind("S_0", "composed shifts", "the composition of the eight packed cyclic shifts"),
          bind("T_0", "ideal permutation", "the permutation performing the required XORs at the selected positions and fixing everything else"),
          bind(r"\mathcal B", "bad set", "the set of addresses at which some guard value lies within ten of its range boundary"),
          bind(r"\delta_{\rm bad}", "bad fraction", "the bound $\\min\\{1,80(f-1)2^{-K}\\}$ on the fraction of exceptional addresses"),
          bind("j_i", "selected positions", "the bit positions $\\rho+iK$, $0\\le i<f$, at which the XOR is performed")],
    mot_quote=ev(1947, 1950, "The construction first uses", "over all payloads."))

# ---------------------------------------------------------------- S3.3 batching and recurrence
S3_3 = show("S3.3",
    r"Running the network on $W$ role streams whose rows come from the first $q_0$ chunks, the normalized cost $F(e)$ of a $C$-layer on $e$ chunks satisfies $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ with $F(e)=O(e)$ for $e<d^\beta$, $\beta=1/2$, and summing over the base-$m$ pieces of $D-q_0$ gives total normalized cost $O(d^{\lambda'})$ for any fixed $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$.",
    "Apply $C$ individually on the first $q_0=\\lceil\\log_2W\\rceil\\lceil\\log_m(2d)\\rceil$ chunks and use their bits as a row index of range at least $W^{k_0}$; charge the basis changes at a node by the packed lemma; unroll the recurrence with $a=s/W\\le m^\\sigma<m^\\lambda$ and stop at $e<d^\\beta$.",
    "The power-width recurrence needs rows divisible by $W^k$; a layer has no row field, but the first $q_0$ chunks, processed individually at $O(V\\log d)$ cost, provide one, and the per-node overhead $(eK)^\\tau$ is a smaller power than $\\lambda$ by the choice $\\tau(1+c/\\beta)<\\lambda$, so the geometric sum is dominated by the top node.",
    "recoverable",
    [
     infer("S3.3.1",
        r"Applying $C$ individually on the selected bits of the first $q_0$ chunks in $O(V\log d)$ time leaves a complete consecutive block whose concatenated bits form a row index of range $R_{\rm row}=2^{q_0K}\ge W^{k_0}$; padding rows to the next multiple of $W^{k_0}$ grows the volume by at most two, and at depth $j\le k_0$ the row count is divisible by $W^{k_0-j}$.",
        ev(2313, 2323, "Otherwise apply", "divisible by \\(W^{k_0-j}\\)."), line=2313),
     infer("S3.3.2",
        r"With $F(e)$ the time divided by the current logical volume, $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ and $F(e)=O(e)$ for $e<d^\beta$: the $s$ children run on volume $V/W$ each, giving the factor $s/W$, and at an internal node $K\le d^c\le e^{c/\beta}$ makes the overhead $O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)$.",
        ev(2402, 2415, "Stop recursion when", "O(e^\\lambda)\\)."), line=2402),
     infer("S3.3.3",
        r"Since $a=s/W\le m^\sigma<m^\lambda$, the internal costs sum to $Ce^\lambda\sum_j(a/m^\lambda)^j=O(e^\lambda)$ and the leaves contribute $O(a^ju)\le O(e^\sigma d^{\beta(1-\sigma)})$; over at most $(m-1)(1+\lfloor\log_md\rfloor)$ pieces plus the row preprocessing the total is $O(\log(2d)[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1])=O(d^{\lambda'})$.",
        ev(2432, 2445, "Write \\(D-q_0", "\\lambda'<1."), line=2432),
    ],
    frm=["rank-saving-recurrence", "power-width-interchange", "packed-selected-bit-addition", "phase-frame-network", "divide-and-conquer-and-recurrences", "geometric-series-and-sums"],
    adds=[bind("q_0", "row chunk count", "the number of leading chunks whose bits serve as the row index", "count"),
          bind("F(e)", "normalized layer cost", "time divided by the current logical volume for a $C$-layer on $e$ chunks"),
          bind(r"\beta", "leaf threshold exponent", "the fixed $1/2$: recursion stops when fewer than $d^\\beta$ chunks remain"),
          bind(r"\lambda,\sigma", "recurrence exponents", "the fixed rational exponents bounding the node overhead and $\\log_m(s/W)$")])

# ---------------------------------------------------------------- S3 simultaneous layer
S3 = show("S3",
    r"For $d=\Theta(p^\epsilon)$, $K=\lfloor d^c\rfloor$, $r=2^{\Theta(p/d)}$ and $1\le D\le d$, one fixed procedure applies the tensor product $\mathcal H$ of $H_0=\frac12\bigl(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\bigr)$ on the selected bit $\rho$ of each of $D$ consecutive $K$-bit address chunks, coefficientwise on polynomial records of $r$ disk-grid coefficients, returning $Q_p(\mathcal Hz)$ in $O(Vd^{\lambda'})$ time with $\lambda'=1-2^{-54}<1$, with error below $\sqrt2\,2^{-p}$ and the unit disk preserved.",
    "Write $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$ with the kernel $C=aI+bX$; evaluate $C^{\\otimes e}$ by the complex network, whose phase frames make each edge a product of translation kernels implemented as binary basis changes by packed selected-bit additions plus $s_{\\rm c}$ recursive calls on slots of $e/m$ chunks and $1/W_{\\rm c}$ of the volume; take rows from the first $q_0$ chunks; unroll the recurrence; bound the growth of the exact dyadic values so that one guarded width $O(p)$ suffices; truncate once at the end.",
    "A round of the multidimensional transform applies a butterfly on every participating axis; done one axis at a time that is $D$ passes over the whole array, so the layer must be applied simultaneously, by the same network recursion that saved a power for address interchange.",
    "explicit",
    [S3_1, S3_2, S3_3,
     infer("S3.4",
        r"A value at arithmetic depth $\ell$ lies in $2^{-(p+\ell)}\mathbb Z[i]$ with modulus at most $2^\ell$, and the depth within a layer is below $\Delta=\lceil C_0d^{C_1}\rceil$ with $C_1=20$; choosing $\epsilon C_1<1$ with $d=\Theta(p^\epsilon)$ gives $\Delta=o(p)$, so the full guarded coefficient width is $O(p)$ and every intermediate coefficient is represented exactly.",
        ev(2582, 2586, "Choose", "per\ncoefficient."), line=2582),
     infer("S3.5",
        r"The procedure returns $Q_p(\mathcal Hz)$ in $O(Vd^{\lambda'})$ time; every row of $\mathcal H$ has absolute row sum one, so disk arrays map to disk arrays, and componentwise truncation toward zero preserves the disk with error less than $\sqrt2\,2^{-p}$.",
        ev(2751, 2757, "Finally, every row", "can hold them."), line=2751),
    ],
    page="simultaneous-butterfly-layer",
    frm=["phase-frame-network", "packed-selected-bit-addition", "fixed-point-complex-arithmetic", "rank-saving-recurrence", "address-chunk-interchange", "fft-butterflies", "geometric-series-and-sums", "divide-and-conquer-and-recurrences"],
    salient="The whole layer is evaluated exactly in Gaussian dyadics through intermediate operators that are not contractions, with only one truncation at the end, so a simultaneous layer on up to $d$ axes has the same error $\\sqrt2\\,2^{-p}$ as a single butterfly.",
    adds=[bind("d", "axis count", "the number of address chunks, the dimension of the transform box", "count"),
          bind("p", "precision", "the number of fractional bits of the coefficient grid $2^{-p}\\mathbb Z[i]$", "count"),
          bind("K", "chunk width", "the number of address bits in each chunk, $\\lfloor d^c\\rfloor$", "count"),
          bind("D", "participating axes", "the number of chunks whose selected bits the layer acts on", "count"),
          bind("f", "slot size", "the number of chunks in one slot of a network invocation, and the number of selected positions in one packed call", "count"),
          bind(r"\lambda'", "layer exponent", "the fixed rational $1-2^{-54}$ with cost $O(Vd^{\\lambda'})$"),
          bind(r"\mathcal H", "butterfly layer", "the tensor product of $H_0$ on the $D$ selected bits, acting coefficientwise"),
          bind("Q_p", "truncation", "truncation of real and imaginary parts toward zero to the grid $2^{-p}\\mathbb Z$")],
    mot_quote=ev(1792, 1794, "We will obtain cost", "whole-array passes."))

# ---------------------------------------------------------------- S4 ring convolution
S4_3 = show("S4.3",
    r"For $t_i\in\{2^{\ell-1},2^\ell\}$, $d\ell\le C_\ell p$ and $1\le K\le\ell-1$, a positional layout permutation $L$ of record addresses lets every transform round be one simultaneous butterfly layer, so that the forward procedure realizes exactly $LBF_{\boldsymbol t}^-$ and the opposite one $F_{\boldsymbol t}^+B^{-1}L^{-1}$, each with error less than $\sqrt2\ell\,2^{-p}$, disk-grid output, and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.",
    "Move $O(dK)$ named slots to a prefix by single-bit moves; reorder the remaining $K$-bit chunks from axis-major to chunk-major by at most $Dq-1$ chunk exchanges; run the rounds as simultaneous layers with the combined twiddle monomial $J_E$ applied exactly after each; process the prefix-slot rounds individually; truncate once per round and identify the stored order.",
    "The simultaneous layer needs the selected bit of each participating axis at a common offset in consecutive $K$-bit chunks, so the axis-major address order must be interleaved chunk by chunk; the chunk interchange does this at cost $O(TpK^\\tau)$ per exchange, sublinear in $K$.",
    "explicit",
    [
     infer("S4.3.1",
        r"Listing the slots $(i,\ell-1)$ of the long axes and then the $b=(\ell-1)\bmod K$ lowest slots of every axis, and moving each immediately after the prefix formed so far, uses $O(dK)$ single-bit moves costing $O(TpdK)$ and leaves each axis as $q=\lfloor(\ell-1)/K\rfloor$ consecutive $K$-bit chunks.",
        ev(3002, 3010, "Form a list of the slots", "$K$-bit chunks."), line=3002),
     infer("S4.3.2",
        r"Reordering the chunks from $(1,1),\ldots,(1,q),(2,1),\ldots,(D,q)$ to $(1,1),(2,1),\ldots,(D,1),(1,2),\ldots,(D,q)$ by scanning target positions and exchanging the chunk present with the required one uses at most $Dq-1$ width-$K$ chunk exchanges at $O(TpK^\tau)$ each, total $O(Tp\,pK^{\tau-1})$; these moves define $L$, and recording them in reverse gives $L^{-1}$.",
        ev(3019, 3032, "To obtain this order", "same cost."), line=3019),
     infer("S4.3.3",
        r"In a round at named position $h$ in the remaining chunks the selected bit has offset $(h-b)\bmod K$ in each of the $D$ chunks with the same index $j$, every combination of the other bits occurs, so the layer sees the complete set $[P]\times[2^K]^D\times[S]$ with $\log_2(2M)\le C_Mp$; the simultaneous-layer procedure therefore applies at $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.",
        ev(3070, 3083, "For a position $h$", "=C_Mp$."), line=3072),
     infer("S4.3.4",
        r"Since $J_E$ is a signed coefficient permutation and truncation toward zero is odd, $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$, so each forward round returns exactly one truncation after the exact contraction round, and the opposite round likewise; a contraction does not increase the error and each truncation adds less than $\sqrt2\,2^{-p}$, so at most $\ell$ rounds give error below $\sqrt2\ell\,2^{-p}$ with the disk preserved.",
        ev(3159, 3178, "Truncation\ntoward zero is odd", "no numerical error."), line=3159),
     infer("S4.3.5",
        r"Executing operations on named slots after $L$ conjugates the exact logical procedures $\mathcal D_-=BF_{\boldsymbol t}^-$ and $\mathcal D_+=F_{\boldsymbol t}^+B^{-1}$ by $L$; the forward procedure moves records by $L$ first and the opposite restores by $L^{-1}$ last, so their full exact operators are $LBF_{\boldsymbol t}^-$ and $F_{\boldsymbol t}^+B^{-1}L^{-1}$, the forward entry of frequency $j$ being stored at $L(Bj)$.",
        ev(3184, 3199, "Executing each operation", "physical order."), line=3184),
    ],
    page="transform-tape-layout",
    frm=["simultaneous-butterfly-layer", "address-chunk-interchange", "stored-frequency-order", "tape-address-model", "fixed-point-complex-arithmetic", "triangle-inequality-and-norms", "fft-butterflies"],
    adds=[bind("L", "layout permutation", "the positional permutation of record addresses produced by the prefix moves and chunk exchanges"),
          bind("q", "chunks per axis", "the number $\\lfloor(\\ell-1)/K\\rfloor$ of complete $K$-bit chunks left in each axis", "count"),
          bind("b", "prefix slot count", "the number $(\\ell-1)\\bmod K$ of lowest slots per axis moved to the prefix", "count"),
          bind("D", "axis count", "the number $d-1$ of transform axes", "count"),
          bind("J_E", "twiddle monomial", "the recordwise multiplication by $y^E$ combining the twiddles of all participating axes in a round"),
          bind("h", "named position", "the original bit slot of an axis processed in the current round")],
    mot_quote=ev(2918, 2921, "To apply Proposition", "$K$-bit chunks."))

S4_4 = show("S4.4",
    r"For disk-grid polynomials $f,g\in\mathcal R_r$ with $r=2^\ell<2^p$, the exact Gaussian integer numerators of $fg$ and then $Q_p(fg/r)$ can be computed in $O(rp\log(rp))$ time on fixed tapes, with output a disk grid polynomial of error below $\sqrt2\,2^{-p}$ from $fg/r$.",
    "Evaluate the four integer coefficient polynomials $a,b,c,e$ at $B_0=2^{4p}$ with signed carries into fixed-width blocks, multiply the four magnitudes with the established $O(N\\log N)$ multiplier, extract coefficients by centered residues modulo $B_0$ since $|h_j|<B_0/2$, form $ac-be$ and $ae+bc$, reduce modulo $y^r+1$, and truncate after shifting by $p+\\ell$ bits.",
    "A product of polynomials with bounded integer coefficients is read off from one product of the integers obtained by evaluating at a large power of two, so the established $O(N\\log N)$ multiplier serves as an ordinary subroutine on $O(rp)$-bit inputs, far shorter than $n$, and the improved theorem is not invoked recursively.",
    "explicit",
    [
     infer("S4.4.1",
        r"With $A_u=u(B_0)$ and $B_0=2^{4p}$, each $|A_u|<B_0^r/2$ fits in $4pr$ bits, the product $A_aA_c$ equals $h(B_0)$ for the ordinary polynomial product $h=ac$, and every coefficient satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so after the lower coefficients are removed the next one is identified by its centered residue modulo $B_0$.",
        ev(3245, 3265, "The bound", "modulo $B_0$."), line=3245),
     infer("S4.4.2",
        r"Reading the product in $J=2r$ blocks with carries $\rho_j\in\{0,1\}$ and centered residues, the residual identity $\sum_{k\ge j}h_kB_0^{k-j}=\sum_{k\ge j}q_kB_0^{k-j}+\rho_j+\varepsilon B_0^{J-j}$ gives $\widehat h_j=h_j$ at every block, a negative product's final carry $1$ being canceled by its sign extension $\varepsilon=-1$, so extraction costs $O(rp)$.",
        ev(3318, 3329, "For $j<J$, reduction modulo", "costs $O(rp)$."), line=3318),
     infer("S4.4.3",
        r"Reducing modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$ makes each $H_j$ a sum of exactly $r$ signed products of Gaussian integers of modulus at most $2^p$, so $|H_j|\le r2^{2p}$, and the same triangle inequality gives $\|fg/r\|_\infty\le\|f\|_\infty\|g\|_\infty$: the normalized product of disk polynomials lies in the disk.",
        ev(3331, 3347, "For each first input index", "lies in the disk."), line=3337),
    ],
    page="signed-packing",
    frm=["n-log-n-barrier", "negacyclic-ring", "positional-notation-in-any-radix", "polynomials", "dyadic-rationals-and-fixed-width-numerators", "integer-division-with-remainder-floor-and-ceiling"],
    adds=[bind("B_0", "packing base", "the power of two $2^{4p}$ at which the integer coefficient polynomials are evaluated"),
          bind("A_u", "evaluation integer", "the signed integer $u(B_0)$ obtained from the coefficient polynomial $u$"),
          bind("h_j", "product coefficient", "a coefficient of the ordinary product of two integer coefficient polynomials"),
          bind("H_j", "wrapped coefficient", "a Gaussian integer coefficient of the product after reduction modulo $y^r+1$"),
          bind(r"\rho_j", "extraction carry", "the carry in $\\{0,1\\}$ at block $j$ of the centered extraction")],
    mot_quote=ev(3211, 3215, "To multiply the polynomial records", "independent subroutine."))

S4 = show("S4",
    r"For arrays $f,g$ of disk-grid records in $\mathcal R_r=\mathbb C[y]/(y^r+1)$ on $\prod_{i<d}\mathbb Z/t_i\mathbb Z$ with $M=\prod_{i<d}t_i$ and $T=rM$, the normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ has an approximation, returned in the original order, with error less than $\sqrt2\,M(3\ell+1)2^{-p}$, $\ell=\log_2r$, at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$, and the output is a disk array when one operand has norm at most $\rho<1$ with that error bound at most $1-\rho$.",
    "Define synthetic transforms over the ring whose roots of unity $\\omega_t=y^{2r/t}$ act by signed coefficient shifts; perform two forward transforms that write outputs in the retained order $LB$; multiply corresponding records pointwise by signed packing divided by $r$; apply the opposite procedure, which consumes that order; scale exactly by $M$; add the three transform errors and one truncation through contractions.",
    "Roots of unity in the ring are signed coefficient shifts, so transform arithmetic needs no complex multiplications; and because a record permutation commutes with pointwise products, the bit-reversed layout order never has to be undone between the forward transforms and the opposite one.",
    "explicit",
    [
     infer("S4.1",
        r"With $\omega_t=y^{2r/t}$ for a power of two $t\mid2r$, the transforms $(F_t^\pm z)_j=\frac1t\sum_k\omega_t^{\pm jk}z_k$ are contractions since every power of $\omega_t$ is an isometry, and $\sum_{k=0}^{t-1}\omega_t^{jk}$ equals $t$ when $t\mid j$ and $0$ otherwise, because for $j=2^vj_0$ with $j_0$ odd the substitution $k\mapsto k+t/2^{v+1}$ multiplies the sum by $y^{rj_0}=-1$ and the ring has no two-torsion; hence $F_t^+F_t^-=t^{-1}I$.",
        ev(2820, 2825, "Only the second case", "final formula."),
        page="synthetic-polynomial-transform",
        frm=["negacyclic-ring", "discrete-fourier-transform", "roots-of-unity-and-euler-s-formula", "geometric-series-and-sums", "polynomials"],
        salient="Every twiddle multiplication is a signed cyclic shift of a coefficient list, exact and free of real arithmetic, even though the ring has zero divisors and the usual division by $\\omega_t^j-1$ is unavailable.",
        line=2820),
     infer("S4.2",
        r"The decimation-in-frequency recursion writes $(F_t^-z)_j$ into slot $\operatorname{rev}_a(j)$ without moving whole frequency indices, and the procedure traversing the recursion in reverse composes with it to $I/t$ because $H_0^2=I/2$ at each of the $a=\log_2t$ levels; so the two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$, and on several axes a round groups as a parallel butterfly $\mathcal H$ followed by one recordwise monomial $J_E$, a contraction followed by an isometry.",
        ev(2872, 2887, "The procedure consuming", "respectively."),
        page="stored-frequency-order",
        frm=["fft-butterflies", "synthetic-polynomial-transform", "binary-numerals-and-bit-strings", "permutations-and-bijections"],
        salient="The forward transform leaves its outputs in bit-reversed order and the opposite transform consumes exactly that order, so no frequency permutation is ever executed.",
        line=2873),
     S4_3, S4_4,
     infer("S4.5",
        r"Expanding the finite sums, $F_{\boldsymbol t}^-(f*g)=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)$ and $F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$ give $MF_{\boldsymbol t}^+((F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)/r)=(f*g)/(rM)$; since $LB$ permutes records leaving their polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$, so the opposite procedure applied to the pointwise product of the retained forward outputs, scaled by $M$, equals $\mathcal M_r(f,g)$.",
        ev(3422, 3441, "To check normalization", "\\mathcal M_r(f,g)$."), line=3423),
     infer("S4.6",
        r"With $\delta=\sqrt2\ell\,2^{-p}$ and $\eta=\sqrt2\,2^{-p}$, bilinearity and the disk bounds give $\|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty<2\delta$, the product truncation adds $\eta$, the contraction $\mathcal T_+$ adds its own $\delta$, and the final exact multiplication by $M$ gives error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$; if one operand has norm at most $\rho$ the returned norm is below $\rho+(1-\rho)=1$.",
        ev(3464, 3476, "If $\\widetilde h$ is the returned", "+(1-\\rho)=1$."), line=3464),
    ],
    page="normalized-ring-convolution",
    frm=["convolution", "negacyclic-ring", "synthetic-polynomial-transform", "stored-frequency-order", "transform-tape-layout", "signed-packing", "contraction-error-propagation", "discrete-fourier-transform", "triangle-inequality-and-norms"],
    salient="The three transforms of the convolution all keep the same bit-reversed layout order, so the only movement between them is none at all; the stored order is consumed, not corrected.",
    adds=[bind(r"\mathcal R_r", "polynomial ring", "the ring $\\mathbb C[y]/(y^r+1)$ of representatives of degree below $r$"),
          bind("r", "record length", "the number of complex coefficients in one polynomial record, a power of two", "count"),
          bind(r"\ell", "record exponent", "the number $\\log_2r$ of bits of a record index; also the number of butterfly levels on a long axis", "count"),
          bind("t_i", "axis length", "the number of entries along axis $i$, a power of two in $\\{2^{\\ell-1},2^\\ell\\}$", "count"),
          bind("M", "record count", "the number $\\prod_{i<d}t_i$ of polynomial records in the array", "count"),
          bind("T", "box size", "the number $rM$ of scalar entries in the padded box", "count"),
          bind(r"F_{\boldsymbol t}^-", "forward tensor transform", "the tensor product of the forward normalized synthetic transforms $F_{t_i}^-$ over the axes"),
          bind(r"F_{\boldsymbol t}^+", "opposite tensor transform", "the tensor product of the opposite normalized synthetic transforms $F_{t_i}^+$ over the axes"),
          bind("B", "bit reversal", "the tensor product of the bit-reversal record permutations $B_{t_i}$ of the axes"),
          bind(r"\mathcal M_r", "normalized convolution", "the bilinear map $(f*g)/T$ on arrays of ring records"),
          bind("P(u,v)", "pointwise product", "the exact recordwise product $uv/r$")],
    mot_quote=ev(3202, 3205, "Pointwise multiplication commutes", "opposite procedure."))

# ---------------------------------------------------------------- S5 resampling
S5 = show("S5",
    r"For pairs $(s_i,t_i)$ with $s_i$ prime, $t_i$ a power of two, $\gcd(s_i,t_i)=1$ and $t_i/s_i-1>p/\alpha^4$, the source transform satisfies $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$, where $R=\bigotimes_iP_{s_i}$ and $Q=\bigotimes_iP_{t_i}$ are coordinate permutations retained in the identity and $\mathcal A,\mathcal B_0$ are linewise Gaussian contractions approximable with error below $dp^2$ in time $O(dTp^{3/2+\delta}\alpha)$; the middle factor $QF_{\boldsymbol t}$ is a chirp-weighted cyclic convolution, and $R$ cancels in $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$.",
    "Use Harvey and van der Hoeven's Gaussian maps $\\mathsf S,\\mathsf T$ with $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ and the Neumann inverse of $N=C\\mathsf T\\mathsf D$, keeping $P_s,P_t$ inside the identity instead of sorting; tensor over axes line by line in the padded box, exposing each axis by chunk interchanges; derive the chirp form of $QF_{\\boldsymbol t}$ from the quadratic phase and the cancellation of $R$ from $F_q^+R_c=R_c^{-1}F_q^+$.",
    "The prime axis lengths required by the Chinese-remainder layout are not powers of two, which the synthetic transforms require; Gaussian resampling bridges the two shapes, but its standard form executes two sorts per coordinate, which would cost $n\\log n$, so both permutations are kept in the formula and computed as part of it.",
    "explicit",
    [
     infer("S5.1",
        r"With $A=\mathsf S/2$ and $B_0=\mathsf D'\mathsf J'C$, both contractions, applying the left inverse $\mathsf DN^{-1}C$ of $\mathsf T$ to $\mathsf TP_sF_s=P_tF_t\mathsf S$ gives $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$, i.e. $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$; the cited ordered algorithms approximate $A$ and $B_0$ with errors $16p<p^2$ and $4+3p^2/4<p^2$ in $O(tp^{3/2+\delta}\alpha)$ time, while the two label-and-sort operations of the original proof are omitted.",
        ev(3625, 3642, "Now set $A=\\mathsf S'$", "no-sort-one-dimensional}."), line=3625),
     infer("S5.2",
        r"Tensoring gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$; applying each one-dimensional map line by line in the full padded box, with zero outside the valid coordinates, gives a contraction per axis with error less than $p^2$, hence $dp^2$ for the composition, line cost $O(dTp^{3/2+\delta}\alpha)$, and exposing and restoring the axes by $O(d^2)$ adjacent chunk interchanges costs $O(Tpd^2(1+\ell^\tau))$.",
        ev(3857, 3870, "For a fixed axis", "same bound."), line=3857),
     infer("S5.3",
        r"With $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$, of period $t_i$ in coordinate $i$ because every $t_i$ is even, $QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$: the coefficient of $u_{\boldsymbol k}$ on the right is $\frac1T\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}=\frac1T\exp(2\pi i\sum_is_ij_ik_i/t_i)$, exactly the coefficient of $QF_{\boldsymbol t}$ since $Q$ reads frequency $-s_ij_i$ from the negative-sign transform.",
        ev(3939, 3951, "Replacing $j_i$ by $j_i+t_i$", "negative-sign transform."),
        page="bluestein-chirp",
        frm=["discrete-fourier-transform", "convolution", "roots-of-unity-and-euler-s-formula", "complex-numbers"],
        salient="The target permutation $Q$ of resampling is absorbed into the chirp phases: the same convolution that computes $F_{\\boldsymbol t}$ computes $QF_{\\boldsymbol t}$ once the chirp is built with the dilated frequencies $-s_ij_i$.",
        line=3939),
     infer("S5.4",
        r"For a unit $c$ modulo $q$, substituting $h=ck$ in the Fourier sum gives $F_q^+R_c=R_c^{-1}F_q^+$; since each $t_i$ is a unit modulo $s_i$, tensoring gives $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$, and since a coordinate permutation commutes with pointwise products, $RF_{\boldsymbol s}^+[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=(u*v)/S^2$ by the rule $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$ and $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$.",
        ev(3953, 3983, "For a unit $c$ modulo $q$", "source-permutation-cancel}."),
        page="permutation-cancellation",
        frm=["discrete-fourier-transform", "convolution", "gaussian-resampling", "permutations-and-bijections", "modular-arithmetic", "primes-coprimality-and-gcd"],
        salient="The source permutation $R$ appears in all three transforms yet disappears from the convolution identity, because a dilation of the frequency axis commutes with the opposite transform up to inversion and with pointwise products exactly.",
        line=3953),
    ],
    page="gaussian-resampling",
    frm=["discrete-fourier-transform", "contraction-error-propagation", "exponential-logarithm-and-gaussian-function", "n-log-n-barrier", "address-chunk-interchange", "permutations-and-bijections", "primes-coprimality-and-gcd", "fixed-point-complex-arithmetic"],
    salient="Both coordinate permutations of resampling, $P_s$ and $P_t$, remain inside the transform identity and are never executed: the target one is absorbed by the chirp and the source one cancels across the two forward transforms, the pointwise product and the opposite transform.",
    adds=[bind("s_i", "source length", "the prime length of axis $i$ of the source transform", "count"),
          bind("t_i", "target length", "the power-of-two length of axis $i$ of the padded box", "count"),
          bind("R", "source permutation", "the tensor product of the coordinate permutations $(P_su)_j=u_{tj}$ on the source axes"),
          bind("Q", "target permutation", "the tensor product of the coordinate permutations $(P_tv)_k=v_{-sk}$ on the target axes"),
          bind(r"\mathcal A,\mathcal B_0", "Gaussian maps", "the linewise expansion and compression contractions of resampling"),
          bind(r"\alpha", "Gaussian width", "the integer parameter of the Gaussian kernels, with $2\\le\\alpha<\\sqrt p$"),
          bind(r"\gamma", "resampling scale exponent", "the exponent $2d\\alpha^2$ of the power of two restoring normalization", "count"),
          bind("S", "source box size", "the product $\\prod_is_i$ of the prime lengths", "count"),
          bind("T", "target box size", "the product $\\prod_it_i$ of the power-of-two lengths", "count"),
          bind("a", "chirp", "the array of quadratic phases $\\exp(-\\pi i\\sum_is_ij_i^2/t_i)$"),
          bind(r"F_{\boldsymbol s}", "source transform", "the tensor product of the normalized scalar transforms $F_{s_i}$ over the prime axes"),
          bind(r"F_{\boldsymbol t}", "target transform", "the tensor product of the normalized scalar transforms $F_{t_i}$ over the power-of-two axes")],
    mot_quote=ev(3500, 3503, "Gaussian resampling\nconnects", "directly."))

# ---------------------------------------------------------------- S6 assembly
S6_3 = show("S6.3",
    r"The map $\Phi\colon x\mapsto\prod_ix_i^{\mu_i}$ with $P_i=\prod_{j<i}s_j$ and $\mu_i=P_i^{-1}\bmod s_i$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ onto the product of the cyclic axes that preserves convolution; it sends the index $k=\sum_ja_jP_j$ to coordinates $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, and together with padding and its inverse it costs $O(Tp\,d^2(1+\ell^\tau))$.",
    "Verify that the image of $x$ has order $S$ so its powers run through all monomials; insert the padding in mixed-radix order by one nested scan; reorder the axes to $(a_1,\\ldots,a_d)$ by $O(d^2)$ adjacent chunk interchanges; update the targets $i=d,\\ldots,1$ by prefix-controlled cyclic shifts of the valid interval.",
    "Choosing the exponents $\\mu_i$ as inverses of prefix products makes each new coordinate depend only on lower-index digits, so the change of order is a sequence of controlled shifts whose controls precede their targets, each of linear cost.",
    "explicit",
    [
     infer("S6.3.1",
        r"$\Phi$ respects $x^S=1$; the image of $x$ has order $S$ because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all $S$ target basis monomials exactly once, and $\Phi$ is an isomorphism preserving cyclic convolution.",
        ev(4216, 4220, "respects $x^S=1$", "cyclic convolution."), line=4216),
     infer("S6.3.2",
        r"In the mixed-radix expression $k=\sum_ja_jP_j$, $0\le a_j<s_j$, the axis-$i$ coordinate of $\Phi(x^k)$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, since terms with $j>i$ are divisible by $s_i$ and $\mu_iP_i=1$ modulo $s_i$.",
        ev(4226, 4231, "The coordinate of", "modulo\n$s_i$."), line=4226),
     infer("S6.3.3",
        r"After reordering the axes to $(a_1,\ldots,a_d)$, updating targets in the order $i=d,\ldots,1$ uses only unchanged lower-index digits; each update is a prefix-controlled cyclic shift of the valid interval $[0,s_i)$, fixing $[s_i,t_i)$ and acting as the identity when a control is invalid, so zero padding stays zero; adjacent axes of unequal width are exchanged by peeling one bit, and reversing all axes needs $O(d^2)$ such moves, so $\Phi$, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$.",
        ev(4283, 4291, "The axis widths are", "d^2(1+\\ell^\\tau)\\bigr)."), line=4283),
    ],
    page="crt-axis-map",
    frm=["primes-coprimality-and-gcd", "modular-arithmetic", "convolution", "controlled-cyclic-shift", "address-chunk-interchange", "polynomials", "positional-notation-in-any-radix", "tape-address-model", "multidimensional-arrays-and-row-major-order"],
    salient="The Chinese-remainder change of order is triangular: coordinate $i$ depends only on the digits of lower index, so it is a sequence of controlled cyclic shifts and needs no sorting.",
    adds=[bind("P_i", "prefix product", "the product $\\prod_{j<i}s_j$ of the earlier prime lengths"),
          bind(r"\mu_i", "CRT exponent", "the inverse of $P_i$ modulo $s_i$, the exponent of $x_i$ in the image of $x$"),
          bind("a_j", "mixed-radix digit", "the digit of the coefficient index $k$ in the mixed radix $(s_1,\\ldots,s_d)$"),
          bind("b_i", "axis coordinate", "the coordinate of $\\Phi(x^k)$ on axis $i$")],
    mot_quote=ev(4198, 4202, "Agarwal and Cooley", "controlled cyclic shifts."))

S6_5 = show("S6.5",
    r"The procedure $\widetilde{\mathscr F}$ (linewise $\widetilde{\mathcal A}$, the computed chirp transform $\widetilde{\mathscr C}$ built on the computed complex convolution $\widetilde{\mathcal M}_{\mathbb C}$, linewise $\widetilde{\mathcal B}_0$, exact scale by $2^\gamma$) has exact counterpart $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, and $\widetilde{\mathscr F}^+(z)=\overline{\widetilde{\mathscr F}(\overline z)}$ has exact counterpart $RF_{\boldsymbol s}^+$.",
    "Compute the complex convolution of the twisted arrays by the ring convolution; evaluate the chirp transform as $x_0=Q_p(\\overline{\\widetilde a}\\cdot x)$, $y_0=\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,x_0)$, $Q_p(\\overline{\\widetilde a}\\cdot y_0)$; compose with the Gaussian line maps and conjugate for the opposite sign.",
    "Each factor of the resampling identity is either a linewise contraction with an established algorithm or the power-of-two tensor transform, which the chirp identity turns into one cyclic convolution of exactly the shape the ring convolution computes after the twist; composing them yields $RF_{\\boldsymbol s}$ without executing $R$ or $Q$.",
    "recoverable",
    [
     infer("S6.5.1",
        r"The computed complex convolution is $f'=Q_p(\widetilde\theta^+\cdot f)$, $g'=Q_p(\widetilde\theta^+\cdot g)$, $h'=\widetilde{\mathcal M}_r(\iota f',\iota g')$, $\widetilde{\mathcal M}_{\mathbb C}(f,g)=Q_p(\widetilde\theta^-\cdot\iota^{-1}h')$, with twist factors $\widetilde\theta^\pm_k$ approximating $\zeta^{\pm k}$ with error below $2\cdot2^{-p}$ and total twist cost $O(Tp^{1+\delta})$.",
        ev(4378, 4392, "Write $\\widetilde{\\mathcal M}_r$", "\\end{aligned}\n\\]"), line=4378),
     infer("S6.5.2",
        r"For a disk-grid target tensor $x$ of norm at most $.6$ the computed chirp transform forms $x_0=Q_p(\overline{\widetilde a}\cdot x)$, $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$ and $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$, whose exact counterpart is $\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)=QF_{\boldsymbol t}x$; the chirp array is built in $O(Tdp^{1+\delta})$ time.",
        ev(4445, 4452, "Thus $\\widetilde a$ is the convolution kernel", "computed convolution."), line=4445),
     infer("S6.5.3",
        r"The source transform applies the linewise approximation to $\mathcal A$, the computed chirp transform, the linewise approximation to $\mathcal B_0$, and an exact multiplication of the grid numerators by $2^\gamma$; its exact counterpart, replacing every numerical subroutine by the exact map and omitting truncations, is $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, and the opposite-sign procedure conjugates input and output.",
        ev(4456, 4469, "For a source disk-grid tensor", "source coordinates."), line=4456),
    ],
    page="tensor-source-transform",
    frm=["gaussian-resampling", "bluestein-chirp", "coefficient-twist", "normalized-ring-convolution", "fixed-point-complex-arithmetic", "contraction-error-propagation", "permutation-cancellation"],
    adds=[bind(r"\widetilde{\mathscr F}", "computed source transform", "the fixed-tape procedure whose exact counterpart is $RF_{\\boldsymbol s}$"),
          bind(r"\widetilde{\mathscr C}", "computed chirp transform", "the procedure with exact counterpart $QF_{\\boldsymbol t}$"),
          bind(r"\widetilde{\mathcal M}_{\mathbb C}", "computed complex convolution", "the procedure with exact counterpart $(f*g)/T$ on complex arrays, built from the ring convolution by the twist"),
          bind(r"\widetilde a", "computed chirp", "the disk-grid approximation of the chirp array $a$"),
          bind(r"\widetilde\theta^\pm", "twist factors", "disk-grid approximations of $\\zeta^{\\pm k}$ with $\\zeta=e^{\\pi i/r}$")])

S6_7 = show("S6.7",
    r"Every call receives a disk-grid input within its margin; the computed first scaled result $\widetilde w$ approximates $w=(u*v)/S$ with error below $E_w2^{-p}$ where $E_w<28\cdot2^\gamma T^2L$, $L=\log_2T$; and after the second scale the absolute error is $2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}<448b\,2^{-3b/4}<1/2$, so rounding gives the unique correct integer coefficients in $[0,2^{3b})$ and carry propagation yields the exact $2n$-bit product.",
    "Propagate errors through linear and bilinear contractions, adding at each stage: ring convolution $E_{\\rm ring}<5TL$, complex convolution $6TL$, chirp transform $8TL$, source transform $E_s=9\\cdot2^\\gamma TL$; combine the two forward errors, the product truncation and the opposite transform; multiply by the exact scales $S$ and $2^{2b+4}S$ and compare with $1/2$ using $S\\le T<2^b$, $L<b$ and $\\gamma\\le b/4$; propagate carries with the invariant on partial sums.",
    "Every map in the pipeline is a linear or bilinear contraction in the sup norm, so errors add rather than multiply, and the digit scale $2^{-b-2}$ with precision $p=6b$ leaves a factor $2^{-6b}$ against scales whose product is about $2^{5b}$ times a polynomial in $b$.",
    "explicit",
    [
     infer("S6.7.1",
        r"For the ring convolution the three transform errors and the polynomial-product truncation total less than $3L+2$ before the scale $M$, so the returned error is bounded by $E_{\rm ring}=M(3L+2)<5TL$; if one operand has norm at most $.7$, bilinear contraction gives $\|\mathcal M_r(f,g)\|\le.7$ and the computed output has norm below $.7+5TLh_p<.701$, the disk margin after the scale without clipping.",
        ev(4586, 4596, "Before that multiplication", "without clipping the output."), line=4586),
     infer("S6.7.2",
        r"Inserting the exact normalized $\mathcal M_r$ at the twisted inputs $\iota f'$ and $\iota g'$, its bilinear contraction propagates the two twist errors (each below $4$), its approximation contributes $E_{\rm ring}$ and the output untwist below $4$, so $\|\widetilde{\mathcal M}_{\mathbb C}(f,g)-\mathcal M_{\mathbb C}(f,g)\|<(E_{\rm ring}+12)h_p<6TLh_p$.",
        ev(4607, 4618, "To compare it with", "<6TLh_p."), line=4607),
     infer("S6.7.3",
        r"For $\|x\|\le.6$ the chirp data operand $x_0$ has norm at most $.6$ and the outputs have norm below $.701$; inserting the exact bilinear $\mathcal M_{\mathbb C}$, the kernel approximation contributes less than $2$, each endpoint phase less than $4$ and the convolution less than $6TL$, so $\|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\|<(6TL+10)h_p<8TLh_p$.",
        ev(4628, 4639, "For its error, the exact operands", "<8TLh_p."), line=4628),
     infer("S6.7.4",
        r"For a source input of norm at most $.5$, the expansion has error below $dp^2$ and norm below $.51$, the chirp output is in the disk, and inserting the exact contractions $\mathcal A$, $QF_{\boldsymbol t}$, $\mathcal B_0$ the error before the scale is below $2dp^2+8TL$; multiplying by $2^\gamma$ gives error below $E_sh_p$ with $E_s=9\cdot2^\gamma TL$ since $2dp^2<TL$ eventually, the scaled output has norm at most $.501$, and conjugation gives the same for the opposite procedure.",
        ev(4646, 4659, "Insert the exact contractions", "disk guarantee."), line=4646),
     infer("S6.7.5",
        r"With $U=RF_{\boldsymbol s}u$, $V_1=RF_{\boldsymbol s}v$ of norm below $1/4$ and computed versions of norm below $.26$, $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has norm below $.5$ and error $(2E_s+2)h_p$; with $G=RF_{\boldsymbol s}^+$ and $G(U\cdot V_1)=(u*v)/S^2$, inserting $G$ at $z$ gives $\|\widetilde{\mathscr F}^+(z)-G(U\cdot V_1)\|<(3E_s+2)h_p$, so the first scale by $S$ gives $\widetilde w$ with error $E_w=S(3E_s+2)<28\cdot2^\gamma T^2L$ and norm below $1/16+10^{-3}<1$.",
        ev(4705, 4716, "The first exact numerator multiplication", "first scaled result."), line=4705),
     infer("S6.7.6",
        r"Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error after the second scale is $2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}<448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<1/2$; the true coefficients are integers, so the nearest integer to the represented value $H_j/2^p$ is the unique correct coefficient, which lies in $[0,2^{3b})$.",
        ev(4718, 4731, "In tensor order", "correct coefficient."), line=4718),
     infer("S6.7.7",
        r"With $Q_0=2^b$ the carry recurrence $d_j=(c_j+k_j)\bmod Q_0$, $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$ keeps $0\le k_j\le q(Q_0-1)<Q_0^2$ and maintains the invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$, which fixes the first $j$ radix digits of the product; the exact product is below $2^{2n}$, so exactly $2n$ bits are output after one reversal of the digit stream.",
        ev(4784, 4806, "The defining relation", "output rule."), line=4785),
    ],
    page="precision-exact-recovery",
    frm=["contraction-error-propagation", "triangle-inequality-and-norms", "tensor-source-transform", "normalized-ring-convolution", "permutation-cancellation", "integer-division-with-remainder-floor-and-ceiling", "radix-digit-reduction", "parameter-regime", "coefficient-twist", "fixed-point-complex-arithmetic"],
    salient="All the accumulated error, through roughly $\\ell+2$ transform rounds, Gaussian maps and chirps on $\\Theta(n)$ values, stays below $1/2$ with a precision of only $p=6b$ bits, six times the digit width, because every stage is a contraction and errors add linearly.",
    adds=[bind("h_p", "unit error", "the grid spacing $2^{-p}$; an error of $a$ means absolute error below $ah_p$"),
          bind(r"E_{\rm ring}", "ring convolution error", "the error bound $M(3L+2)<5TL$ of the computed normalized ring convolution"),
          bind("E_s", "source transform error", "the error bound $9\\cdot2^\\gamma TL$ of the computed source transform"),
          bind("E_w", "first scaled error", "the error bound $S(3E_s+2)$ of $\\widetilde w$"),
          bind("U", "exact first transform", "the exact array $RF_{\\boldsymbol s}u$"),
          bind("V_1", "exact second transform", "the exact array $RF_{\\boldsymbol s}v$"),
          bind("G", "exact opposite transform", "the contraction $RF_{\\boldsymbol s}^+$"),
          bind("Q_0", "carry radix", "the digit radix $2^b$ used in carry propagation"),
          bind("c_j", "recovered coefficient", "the recovered integer convolution coefficient at index $j$"),
          bind("k_j", "carry", "the carry into position $j$ during carry propagation"),
          bind("d_j", "output digit", "the radix-$2^b$ digit of the product at position $j$")],
    mot_quote=ev(4559, 4565, "A linear contraction propagates", "errors therefore add."))

S6 = show("S6",
    r"With the radix-$2^b$ digits of $x$ and $y$ scaled to grid values of norm below $1/4$ and placed on the source box by $\Phi$ as arrays $u,v$, the operations $\widetilde{\mathscr F}(u)$, $\widetilde{\mathscr F}(v)$, pointwise product and truncation to $z$, $\widetilde{\mathscr F}^+(z)$ scaled by $S$, a second exact scale by $2^{2b+4}S$, rounding, $\Phi^{-1}$ with padding removal, and radix-$2^b$ carry propagation output exactly $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$.",
    "Fix the rational exponents and the sizes $b,p,d,K,T,r,t_i$ and primes $s_i$; write the inputs as digit polynomials whose product has no cyclic wrap; map coefficients onto the prime-axis box by the Chinese-remainder address map; twist the last axis into the polynomial ring so that the ring convolution computes complex convolution; compose Gaussian line maps, chirp convolution and exact scaling into the source transform; apply the three-transform convolution identity; bound the error below $1/2$ and round.",
    "The exact counterpart of the three transforms is $(u*v)/S^2$ by the permutation-cancellation identity, so one scale by $S$ undoes the transform normalization and a second scale by $2^{2b+4}S$ undoes the remaining normalization and the two input digit scales, leaving the integer digit convolution, which carries convert to the product.",
    "explicit",
    [
     infer("S6.1",
        r"For large $n$, with $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$ and $t_i\in\{r/2,r\}$ with $\prod_it_i=T$, the bounds $b/2\le\log_2T\le b$ give $\frac1{12}p^\epsilon\le d\le p^\epsilon$ and $\frac p{12d}\le\ell\le\frac p{3d}$, so the comparison constants $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, $C_\ell=1$ of the layer and transform interfaces are fixed for every input length at once, $r$ exceeds every fixed power of $p$, $K/\log p\to\infty$ and $\ell/K\to\infty$; distinct odd primes $(1-2\eta)t_i<s_i\le(1-\eta)t_i$, $\eta=1/(4d)$, exist with $T/2<S<T$ and $\alpha^4\theta_i>p$, so every hypothesis of resampling holds.",
        ev(4073, 4087, "The comparison constants", "all work blocks."),
        page="parameter-regime",
        frm=["asymptotic-notation-beyond-big-o", "primes-coprimality-and-gcd", "exponential-logarithm-and-gaussian-function", "gaussian-resampling", "simultaneous-butterfly-layer", "transform-tape-layout", "normalized-ring-convolution"],
        salient="One fixed set of rational exponents and comparison constants serves every input length: the sizes $d$, $r$, $\\ell$, $K$ are all powers of $p=6\\lceil\\log_2n\\rceil$ within fixed bands, so all cutoffs are absolute constants.",
        line=4073),
     infer("S6.2",
        r"Writing each input as a polynomial in $2^b$ with $q=\lceil n/b\rceil$ nonnegative digits, the product has degree at most $2q-2<2n/b\le T/2<S$, so convolution modulo $x^S-1$ has no nonzero wraparound, and every product coefficient satisfies $0\le c_j\le q(2^b-1)^2<2^{3b}$ since $q\le n\le2^b$.",
        ev(4183, 4193, "Write the two inputs", "$q\\le n\\le2^b$."),
        page="radix-digit-reduction",
        frm=["positional-notation-in-any-radix", "convolution", "schoolbook-and-karatsuba-multiplication", "parameter-regime", "polynomials"],
        line=4183),
     S6_3,
     infer("S6.4",
        r"$\Theta\colon x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ is well defined since $(\zeta y)^r=(-1)(-1)=1$ and is an isomorphism $\mathbb C[x_d]/(x_d^r-1)\to\mathcal R_r$ multiplying coefficient $k$ by $\zeta^k$; for $k+l=j+hr$, $h\in\{0,1\}$, a product term after twisting and negacyclic reduction carries $\zeta^{k+l}(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign, and $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$ is a bilinear contraction.",
        ev(4313, 4320, "For an explicit check", "correct sign."),
        page="coefficient-twist",
        frm=["negacyclic-ring", "convolution", "roots-of-unity-and-euler-s-formula", "complex-numbers", "polynomials"],
        salient="The negative wrap of the ring $y^r=-1$ becomes exactly the positive cyclic wrap after the twist, because $\\zeta^r=-1$ cancels the sign.",
        line=4313),
     S6_5,
     infer("S6.6",
        r"After the input conversion in $O(Tp)$, the algorithm performs: apply $\Phi$ with its padded layout to obtain source arrays $u,v$ of norm below $1/4$; compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$; multiply corresponding coefficients exactly and truncate to $z$; compute $\widetilde{\mathscr F}^+(z)$ and scale its numerators by $S$ to get $\widetilde w$; scale by $2^{2b+4}S$, round the real values to nearest integers written in $(3b+1)$-bit words and apply $\Phi^{-1}$ with padding removal; propagate radix-$2^b$ carries and output exactly $2n$ bits.",
        ev(4506, 4534, "With these streams prepared", "\\end{enumerate}"), line=4506),
     S6_7,
    ],
    page="multiplication-algorithm",
    frm=["radix-digit-reduction", "crt-axis-map", "tensor-source-transform", "permutation-cancellation", "precision-exact-recovery", "parameter-regime", "coefficient-twist", "positional-notation-in-any-radix", "subroutines-and-composition-of-algorithms"],
    adds=[bind("b", "digit width", "the number $\\lceil\\log_2n\\rceil$ of bits per radix digit", "count"),
          bind("p", "precision", "the number $6b$ of fractional grid bits", "count"),
          bind("q", "digit count", "the number $\\lceil n/b\\rceil$ of radix-$2^b$ digits of each input", "count"),
          bind("S", "source box size", "the product of the distinct prime axis lengths $s_i$, the cyclic convolution length", "count"),
          bind("T", "target box size", "the power of two in $[4n/b,8n/b)$ equal to the product of the $t_i$", "count"),
          bind("d", "axis count", "the number $\\lfloor b^\\epsilon\\rfloor$ of axes", "count"),
          bind("r", "record length", "the power of two $2^{\\lceil(\\log_2T)/d\\rceil}$, the last axis length", "count"),
          bind(r"\ell", "record exponent", "$\\log_2r$", "count"),
          bind("K", "chunk width", "$\\lfloor d^c\\rfloor$ address bits per chunk", "count"),
          bind("L", "box exponent", "$\\log_2T$, the bound used for transform errors", "count"),
          bind(r"\gamma", "resampling scale exponent", "$2d\\alpha^2$, with $\\gamma\\le b/4$ eventually", "count"),
          bind(r"\Phi", "CRT address map", "the convolution-preserving isomorphism from $\\mathbb C[x]/(x^S-1)$ onto the product of prime cyclic axes"),
          bind("u,v", "source arrays", "the padded digit arrays of the two inputs on the source box"),
          bind("z", "transform product", "the truncated pointwise product of the two computed source transforms"),
          bind("w", "first scaled result", "the exact array $(u*v)/S$"),
          bind(r"\widetilde w", "computed first scaled result", "the computed approximation of $(u*v)/S$")],
    mot_quote=ev(4536, 4541, "The two occurrences of $S$", "integer coefficient convolution."))

# ---------------------------------------------------------------- S7 cost
S7 = show("S7",
    r"With $V=Tp=\Theta(n)$, every operation's cost divided by $V$ is bounded by one of the powers $p^{\epsilon(1+c)}$, $p^{1-\epsilon c(1-\tau)}$, $p^{1-\epsilon(1-\lambda')}$, $p^{\tau+\epsilon(2-\tau)}$, $p^{3/4+\delta+3\epsilon/2}$, $p^{\epsilon+\delta}$, $p^{1-\epsilon}$, whose margins below one are all at least $2^{-181}=2\kappa$, so the total time is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ for large $n$, and schoolbook multiplication below one cutoff gives one machine with worst-case time $O(n(\lg n)^{1-\kappa})$ for every $n$.",
    "Tabulate the normalized costs of prefix-slot moves, layout chunk exchanges, simultaneous rounds, CRT and axis layouts, Gaussian line maps, chirps and twists, packed polynomial products, scaling and carries; compute the seven margins from the fixed rational exponents; absorb setup, descriptor and exceptional-stream work as $o(V)$.",
    "All work is organized as passes over arrays of $\\Theta(n)$ stored bits, so the natural unit is cost per stored bit, and the theorem follows once every normalized cost is a power of $p=\\Theta(\\log n)$ strictly below one; the smallest margin, from the chunk-exchange term, determines $\\kappa$.",
    "recoverable",
    [
     infer("S7.1",
        r"The seven dominant normalized powers have margins $g_1=1-\epsilon(1+c)$, $g_2=\epsilon c(1-\tau)$, $g_3=\epsilon(1-\lambda')$, $g_4=1-\tau-\epsilon(2-\tau)$, $g_5=1/4-\delta-3\epsilon/2$, $g_6=1-\delta-\epsilon$, $g_7=\epsilon$, and direct substitution gives $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$, so $\min_ig_i=2^{-181}=2\kappa$.",
        ev(4849, 4855, "Direct substitution gives", "power of $\\log p$."), line=4849),
     infer("S7.2",
        r"The transform layout uses $O(p/K)$ exchanges of width-$K$ chunks because $d\ell=O(p)$, each costing $O(VK^\tau)$, so its normalized total is $O(pK^{\tau-1})$; each of the at most $\ell$ simultaneous rounds costs $O(Vd^{\lambda'})$ including basis changes, deterministic repair, row padding and cleanup.",
        ev(4861, 4872, "Its positional layout uses", "fixed-tape cleanup."), line=4861),
     infer("S7.3",
        r"Setup at the at most $p^A$ recursion visits costs $p^{A+C}=o(Tp)$, per-record descriptor work costs $O(Tp^{A+C}/r)=o(Tp)$, per-line setup $O(dTp^C/r)=o(Tp)$, and the compact exceptional-stream sorting over all packed calls costs $O(Vp^{A'}2^{-K})=o(V)$, since $r$ exceeds every fixed power of $p$, $d=O(p^\epsilon)$ and $K=\Theta(p^{\epsilon c})$; this is a deterministic worst-case bound.",
        ev(4964, 4973, "Since there are at most", "worst-case bound."), line=4964),
     infer("S7.4",
        r"Each displayed power is at most $1-2\kappa$ and any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the large-input bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$; fixing one cutoff beyond all size, precision, margin and layout conditions and using schoolbook multiplication below it gives a single deterministic fixed-tape machine with worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length, producing the required $2n$-bit product.",
        ev(4983, 4995, "Each of the seven displayed powers", "$2n$-bit product."), line=4983),
    ],
    page="cost-accounting",
    frm=["parameter-regime", "transform-tape-layout", "crt-axis-map", "gaussian-resampling", "normalized-ring-convolution", "asymptotic-notation-beyond-big-o", "multiplication-algorithm", "simultaneous-butterfly-layer", "address-chunk-interchange", "signed-packing", "precision-exact-recovery", "big-o-notation"],
    salient="The binding term is the layout chunk exchange $pK^{\\tau-1}$ with margin $\\epsilon c(1-\\tau)=2^{-181}$; every other term has a far larger margin, and $\\kappa=2^{-182}$ is half the smallest margin, the other half absorbing all logarithmic factors.",
    adds=[bind(r"\epsilon", "dimension exponent", "the fixed rational $2^{-75}$ with $d=\\Theta(p^\\epsilon)$"),
          bind("c", "chunk exponent", "the fixed rational $2^{-56}$ with $K=\\lfloor d^c\\rfloor$"),
          bind(r"\delta", "Gaussian cost exponent", "the fixed rational $1/16$ in the Gaussian line-map time $O(tp^{3/2+\\delta}\\alpha)$"),
          bind(r"\tau", "interchange exponent", "the fixed rational $1-2^{-50}$ of the chunk interchange cost"),
          bind(r"\lambda'", "layer exponent", "the fixed rational $1-2^{-54}$ of the simultaneous layer cost"),
          bind("g_i", "margins", "the amounts by which the seven dominant powers of $p$ fall below one"),
          bind("V", "logical volume", "the number $Tp=\\Theta(n)$ of stored bits of a full padded array", "count")])

# ---------------------------------------------------------------- root
ROOT_NODE = show("S0",
    r"There is one deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes that computes the exact $2n$-bit product of two $n$-bit integers for every $n\ge1$ in worst-case time $T_A(n)=O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$; hence $n\log n$ is not the optimal order of multiplication cost in this model, contrary to the Schonhage-Strassen conjecture.",
    "Reduce multiplication to a radix-digit convolution computed by approximate Fourier transforms over the polynomial ring $\\mathbb C[y]/(y^r+1)$; accelerate the two operations that would each cost $\\Theta(n\\log n)$, address rearrangement and butterfly layers, by recursive procedures built from fixed linear networks with a rank saving $s<Wm$; then verify exact recovery of the integer coefficients and sum a cost table whose every term is a power of $\\log n$ strictly below one.",
    "In the transform representation the work consists of address rearrangements, signed shifts and butterflies; since even scanning the array once per transform level already costs $n\\log n$, both the data movement and the arithmetic layers must be made sublinear per level, which the two network-based procedures achieve.",
    "explicit",
    [S1, S2, S3, S4, S5, S6, S7],
    page="main-theorem",
    frm=["n-log-n-barrier", "multitape-turing-machine", "big-o-notation", "binary-numerals-and-bit-strings", "subroutines-and-composition-of-algorithms"],
    salient="The saving exponent $\\kappa=2^{-182}$ is minuscule, yet it holds uniformly through all input lengths, and any fixed positive power saving in the logarithm already refutes an eventual $\\Omega(n\\log n)$ lower bound for this machine model.",
    adds=[bind("n", "input length", "the number of bits in each of the two input integers", "count"),
          bind(r"\kappa", "saving exponent", "the fixed exponent $2^{-182}$ by which the logarithmic factor is reduced"),
          bind("T_A(n)", "running time", "the worst-case number of steps of the machine $A$ on $n$-bit inputs", "count")],
    mot_quote=ev(90, 92, "Scanning an array", "movement and arithmetic."))

# ---------------------------------------------------------------- checks
for f in FAIL: print("FAIL", f)
assert not FAIL
ids = set()
def walk(n, depth=0):
    assert n["id"] not in ids, n["id"]; ids.add(n["id"])
    for c in n.get("children", []): walk(c, depth+1)
walk(ROOT_NODE)

# order check on non-deferred infer quotes
LINE = {id_: (line, deferred) for line, id_, deferred in ORDER}
seq = []
def walko(n):
    if n["intention"] == "infer":
        seq.append(n["id"])
    for c in n.get("children", []): walko(c)
walko(ROOT_NODE)
prev = -1
for id_ in seq:
    line, deferred = LINE[id_]
    if deferred: continue
    assert line > prev, ("order", id_, line, prev)
    prev = line
# verify DFS quote order against actual positions in the normalized source
prevpos = -1
def walkq(n):
    global prevpos
    if n["intention"] == "infer" and not n.get("deferred"):
        pos = NORM_SRC.find(n["quote"]["quote"])
        assert pos >= 0, n["id"]
        assert pos > prevpos, ("srcorder", n["id"], pos, prevpos)
        prevpos = pos
    for c in n.get("children", []): walkq(c)
walkq(ROOT_NODE)

# pages: each at most one step
pages = {}
def walkp(n):
    if n.get("page"):
        pages.setdefault(n["page"], []).append(n["id"])
    for c in n.get("children", []): walkp(c)
walkp(ROOT_NODE)
for pg, l in pages.items():
    assert len(l) == 1, (pg, l)

ANS = {"root": ROOT_NODE}
out = ROOT + "/exegenius/tasks/0003-argument.answer.json"
json.dump(ANS, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("written", out, "nodes", len(ids), "pages", len(pages))
