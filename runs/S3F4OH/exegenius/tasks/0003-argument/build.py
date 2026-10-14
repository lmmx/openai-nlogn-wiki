import json, sys, re

SRC = open(sys.argv[1]).read()
OUT = sys.argv[2]

def ev(q):
    return {"source": "paper", "quote": q}

def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

def infer(id, claim, quote, frm=(), page=None, deferred=False, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": list(frm)}
    if page: n["page"] = page
    if deferred: n["deferred"] = True
    if salient: n["salient"] = salient
    return n

def show(id, claim, method, mot_text, mot_src, children, frm=(), page=None, mot_quote=None, adds=None, salient=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": {"text": mot_text, "source": mot_src, "quote": ev(mot_quote) if mot_quote else None},
         "from": list(frm), "children": children}
    if page: n["page"] = page
    if adds: n["adds"] = adds
    if salient: n["salient"] = salient
    return n

# ---------------- key step: power-width interchange ----------------
linear_network = show(
    "S2.3.1.1",
    r"For arbitrary initial scratch values, the bit network on $W$ wires (a forward invocation at stage 1, an inverse one at stage 2 and a forward one at stage 3) sends $(X_a,Y_a)\mapsto(-Y_a,X_a)$, which over $\mathbb F_2$ is the exchange of the two banks, and restores every scratch wire.",
    r"Compute the net effect of one invocation's eight-row schedule, check its coefficients by the intersection sizes of three-element subsets, and compose the three stages.",
    r"Subtracting the readout of the old scratch values before adding the readout of the new ones makes the net update independent of whatever the scratch wires held, so arbitrary rows of the array can serve as scratch.",
    "explicit",
    [
        infer("S2.3.1.1.1",
              r"If the side and central scratch vectors start at $a,c$, rows 0–1 subtract $\mathcal Ja+\mathcal Rc$, rows 2–5 add $\mathcal R(c+\mathcal Gx)+\mathcal J(a+\mathcal Vx)$, and rows 6–7 restore $c,a$, so one invocation changes the targets by $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$ independently of $a,c$.",
              r"$(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of",
              ["linear-algebra-basics"]),
        infer("S2.3.1.1.2",
              r"In the bit construction the gather–scatter coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod 2$; the side wires cancel exactly the pairs with intersection one, distinct triples with intersection zero or two already have coefficient zero, and the self coefficient is one, so the net map is $y\gets y+x$.",
              r"""The side contribution cancels exactly the
intersection-one cases""",
              ["finite-field-f2-arithmetic", "permutations-and-cartesian-products"]),
        infer("S2.3.1.1.3",
              r"The inverse schedule effects $X\gets X-Y$, so the three stages give $(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x)$, each invocation restoring its own scratch wires.",
              r"$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
              ["linear-algebra-basics"]),
    ],
    frm=["linear-algebra-basics", "finite-field-f2-arithmetic", "permutations-and-cartesian-products"],
    page="linear-network",
    mot_quote=r"""The first two rows of
the following schedule remove the effect of the old scratch values;
the next four introduce the source values and add their effect to the
target; the last two restore the scratch values.""",
    salient=r"The exchange is exact for every initial content of the scratch wires, even though the gates combine scratch values with data.",
)

frames = show(
    "S2.3.1.2",
    r"If every source, gate and sink $v$ carries an invertible operator $D_v$ (its frame) on wire arrays and each edge from $u$ to $v$ applies $D_vD_u^{-1}$, the array network implements $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$, so a route from role $w$ to role $\rho(w)$ with scalar sign $\varepsilon_w$ applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$.",
    r"Maintain the invariant that the stored array at each vertex is its frame applied to the logical array, from the sources through edges and gates to the sinks.",
    r"Only the endpoint frames determine the operator on each route, so the intermediate frames are free to be chosen to make every edge change cheap.",
    "explicit",
    [
        infer("S2.3.1.2.1",
              r"Defining the logical input as $D_{\rm in}^{-1}f$ makes the invariant hold at the sources with no physical preprocessing, and an edge operator turns $D_u\varphi$ into $D_v\varphi$.",
              r"It holds at the sources by definition.",
              ["vectors-matrices-and-invertibility"]),
        infer("S2.3.1.2.2",
              r"At a pointwise gate with coefficients $c_j\in R$, linearity gives $\sum_jc_jD_v\varphi_j=D_v(\sum_jc_j\varphi_j)$, so the common frame commutes with the gate and the invariant reaches the sinks.",
              r"Thus the common frame commutes with the pointwise gate, and",
              ["linear-algebra-basics"]),
    ],
    frm=["linear-network", "vectors-matrices-and-invertibility", "linear-algebra-basics"],
    page="common-frame-principle",
    mot_quote=r"""Once the scalar routing is fixed,
the endpoint frames determine the array operator on each route; the
intermediate frames can then be chosen to make each edge change inexpensive.""",
)

labels = show(
    "S2.3.1.3",
    r"Nested nondegenerate subspaces of $\mathcal F=F^{\otimes3}$, $F=\mathbb Q^{h}$, can be attached to the gates and terminals of the bit network so that every edge joins comparable labels, the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$, and the absolute dimension changes sum to $W m-2N+2L$ with $L_{\rm b}/N=100/539<1/2$.",
    r"Pair indicator vectors of three-element subsets by the form $I-J/9$, prescribe stage transitions that expose one tensor factor per stage, choose gate labels so that every decrease happens on one central return, and telescope the signed changes at the gates.",
    r"Each unit of label dimension change on an edge will cost one smaller call, so the labels must keep the total dimension lost on decreasing edges small compared with $N$.",
    "explicit",
    [
        infer("S2.3.1.3.1",
              r"Under $\langle x,y\rangle=x^{\mathsf T}(I-J/9)y$ on $\mathbb Q^{h}$, which is nondegenerate with eigenvalues $1$ and $-91/9$, the triple indicators satisfy $\langle t_S,t_T\rangle=|S\cap T|-1$, with the self pairing $\langle t_T,t_T\rangle=2$ as the exception, so every triple line is nondegenerate and neighboring triples (intersection one) give orthogonal lines.",
              r"\langle t_S,t_T\rangle=|S\cap T|-1,",
              ["linear-algebra-basics"]),
        infer("S2.3.1.3.2",
              r"With $A'=A\otimes F$, $P'=P\otimes\langle t\rangle$ and $B'=(P')^\perp_{A'}$, the outgoing labels of stage $j$ are exactly the incoming labels of stage $j+1$, starting from $U_a$ on $X_a$ and $0$ on $Y_a$ and ending at $\mathcal F$ and $U_a^\perp$ as the terminals prescribe.",
              r"Thus the prescribed outgoing labels are",
              ["linear-algebra-basics"]),
        infer("S2.3.1.3.3",
              r"A side wire joining neighboring triples passes through $P\otimes\langle t_X\rangle\subset P\otimes t_Y^\perp\subset P\otimes F$, which is possible because $t_X\perp t_Y$.",
              r"The first inclusion is possible because $t_X\perp t_Y$.",
              ["linear-algebra-basics"]),
        infer("S2.3.1.3.4",
              r"Listing every edge's orthogonal residual shows that label dimension never decreases except on the central edge $3\to4$, which removes $P\otimes F\otimes Q$ of dimension $h$; so $L=Ich$ over the $I$ invocations with $c$ central wires each.",
              r"Label dimension is nondecreasing along every edge except center $3\to4$, which removes",
              ["linear-algebra-basics"]),
        infer("S2.3.1.3.5",
              r"Signed changes telescope at each gate, since every touched wire has one incoming and one outgoing incidence with the gate's label; sources sum to $N$ and sinks to $W m-N$, so the signed total is $W m-2N$ and the absolute total adds $2L$.",
              r"The signed sum of dimension changes telescopes at every gate: each",
              ["linear-algebra-basics"]),
        infer("S2.3.1.3.6",
              r"With $c_{\rm b}=100$ central wires per invocation, $L_{\rm b}=I c_{\rm b}h$ gives exactly $L_{\rm b}/N=100/539<1/2$.",
              r"\frac{L_{\rm b}}{N}=\frac{100}{539},\qquad",
              []),
    ],
    frm=["linear-algebra-basics", "linear-network", "common-frame-principle", "permutations-and-cartesian-products"],
    page="subset-intersection-labels",
    mot_quote=r"""The saving will come from keeping the total dimension lost on decreasing
edges small relative to $N$.""",
    adds=[B("h", "ground-set size", "The size 100 of the ground set whose three-element subsets index the banks and whose indicator vectors span the label space.", "count")],
    salient=r"All dimension loss is confined to one edge per central wire, and the loss ratio $100/539$ is a fixed number below $1/2$.",
)

rank_sum = show(
    "S2.3.1.4",
    r"Assigning the projection $P_U$ to every gate and sink with label $U$, and $-P_{U_a}$ to the source of $X_a$, makes every route's endpoint difference $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ and the edge-rank sum $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.",
    r"Compute each edge difference's rank from the label dimensions, correct for the negative source projections, and check the endpoint identity role by role.",
    r"The rank of an edge matrix is the number of smaller interchanges it will cost, and for nested projections the rank equals the dimension change, so the label count becomes the call count.",
    "recoverable",
    [
        infer("S2.3.1.4.1",
              r"For nested nondegenerate $U\subset V$, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement, so its rank is $\dim V-\dim U$, and reversing the edge only negates it.",
              r"Its rank is $\dim V-\dim U$; reversing the",
              ["linear-algebra-basics"]),
        infer("S2.3.1.4.2",
              r"The exceptions are the $N$ negative source projections: at stage 1 the first edge on $X_a$ has matrix $2P_{U_a}$ of rank one where the dimension change is zero, adding $N$ to the rank sum.",
              r"Its first edge matrix is therefore $2P_{U_a}$, of rational rank one,",
              []),
        infer("S2.3.1.4.3",
              r"Hence $s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N$, whose deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$ because $L_{\rm b}<N/2$.",
              r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.",
              []),
        infer("S2.3.1.4.4",
              r"For input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$, and every other role has zero source matrix and identity sink matrix.",
              r"$P_{U_a^\perp}-(-P_{U_a})=I_m$.",
              []),
    ],
    frm=["subset-intersection-labels", "linear-algebra-basics"],
)

tau_bound = infer(
    "S2.3.1.5",
    r"The relative deficit $\eta_{\rm b}=339/22587335000000$ exceeds $20\cdot2^{-50}$ and $\log m<20$, so $m^{1-2^{-50}}>m(1-20\cdot2^{-50})>m(1-\eta_{\rm b})$, that is $s_{\rm b}/W_{\rm b}<m^\tau$ with $\tau=1-2^{-50}$.",
    r">m(1-20\cdot2^{-50})>m(1-\eta)",
    ["logarithms-and-iterated-logarithm-notation"],
)

shear = show(
    "S2.3.1.6",
    r"For a fixed rational $m\times m$ matrix $A$ of rank $a$, the address permutation $(H,D)\mapsto(H+AD,D)$ on two groups of $m$ fields over $\mathbb Z/q^b$ costs exactly $a$ interchanges of pairs of $b$-digit fields plus $O(V)$ work.",
    r"Factor $A=E_1\Pi E_2$ with invertible lower-triangular $E_1,E_2$ and a partial permutation $\Pi$ with $a$ ones; perform the triangular changes as controlled shifts and each one of $\Pi$ with a single field interchange.",
    r"Controlled shifts update a later field from earlier fields in linear time, and lower-triangular coordinate changes only ever update in that direction, so only the $a$ ones of $\Pi$ need a costly interchange.",
    "explicit",
    [
        infer("S2.3.1.6.1",
              r"Pivoting on the rightmost nonzero entry of the topmost nonzero row and clearing with lower-triangular elementary operations factors every rational matrix of rank $a$ as $A=E_1\Pi E_2$.",
              r"A=E_1\Pi E_2,",
              ["vectors-matrices-and-invertibility"]),
        infer("S2.3.1.6.2",
              r"A lower-triangular change of $H$ or $D$ costs $O(V)$ by updating coordinates in descending physical order with controlled shifts, since the earlier coordinates still hold their original values; the prime $q$ avoids all denominators so the factors stay invertible modulo $q^b$.",
              r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:",
              ["controlled-shift", "modular-arithmetic"]),
        infer("S2.3.1.6.3",
              r"Each one of $\Pi$, $H_i\leftarrow H_i+D_j$, is done as $D_j\leftarrow D_j+H_i$, an interchange of $(H_i,D_j)$, then $D_j\leftarrow H_i-D_j$, so the shear uses exactly $a$ interchanges.",
              r"It uses just one interchange.  There are $a$ ones, which proves the",
              []),
    ],
    frm=["linear-algebra-basics", "controlled-shift", "elementary-stream-ops", "vectors-matrices-and-invertibility", "modular-arithmetic"],
    page="address-shear",
    mot_quote=r"""Lemma~\ref{lem:ordered-affine-streams} updates a later field using
earlier fields in linear time.  Lower triangular changes of coordinates
can be performed entirely in this direction.""",
)

transfer = infer(
    "S2.3.1.7",
    r"With frames the address shears $\Phi_{M_v}$, which commute with every pointwise XOR gate, the physical output on role $\rho(w)$ is $\Phi_{M_{\mathrm{out}(\rho(w))}}\Phi_{-M_{\mathrm{in}(w)}}f_w=\Phi_{I_m}f_w$: the shear $H\leftarrow H+D$ on every original row, including rows that served as scratch.",
    r"because a common address permutation commutes with every pointwise",
    ["common-frame-principle"],
)

three_shears = infer(
    "S2.3.1.8",
    r"The updates $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ send $(H,D)$ to $(D,H)$; only the middle one uses the network, the other two are linear-cost controlled shifts of the later group.",
    r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,",
    ["controlled-shift"],
)

recurrence = show(
    "S2.3.1.9",
    r"The time per volume obeys $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$, hence $F_k=O(e^\tau)$.",
    r"Count the recursive calls and their volumes, bound the per-node overhead including the fixed-tape call schedule, and sum the geometric series.",
    r"The $s$ child calls each see volume $V/W$, so after division by $V$ the recursive term carries the factor $s/W<m^\tau$ while the parameter grows by $m$ per level.",
    "recoverable",
    [
        infer("S2.3.1.9.1",
              r"There are exactly $s$ recursive calls (the sum of the edge ranks), each on one role stream of volume $V/W$, and splitting, merging, gates and triangular updates are a fixed number of $O(V)$ operations.",
              r"The number of recursive calls is the sum of the edge ranks, exactly $s$.",
              ["elementary-stream-ops"]),
        infer("S2.3.1.9.2",
              r"Dividing time by logical volume gives $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.",
              r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1).",
              ["recurrences-and-induction"]),
        infer("S2.3.1.9.3",
              r"With $a=s/W<m^\tau$, the sum $\sum_{j\le k}a^j$ is at most $k+1$ when $a\le1$ and $O(a^k)$ when $a>1$, in both cases $O(m^{k\tau})$, so $F_k=O(e^\tau)$.",
              r"Hence $F_k=O(e^\tau)$.",
              ["recurrences-and-induction", "big-o"]),
        infer("S2.3.1.9.4",
              r"A depth-first schedule that parks the $W-1$ inactive role streams on a stack moves $O(V)$ symbols per parent node, so temporary storage is not counted as logical volume in the factor $s/W$.",
              r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$",
              ["sorting-and-data-movement-on-tapes"]),
    ],
    frm=["recurrences-and-induction", "big-o", "elementary-stream-ops"],
)

key = show(
    "S2.3.1",
    r"For chunks of $e=m^k$ radix-$q$ digits and a preceding row field whose length is divisible by $W^k$, the two chunks can be interchanged in $O(Ve^\tau)$ time, because the time per volume satisfies $F_k\le(s/W)F_{k-1}+O(1)$ with $s/W<m^\tau$.",
    r"Deal rows cyclically into $W$ role streams, run the bit network pointwise with address-shear frames $\Phi_{M_v}$ so that every role ends with the shear $H\leftarrow H+D$, implement each edge change $\Phi_{A_e}$ by $\operatorname{rank}A_e$ recursive interchanges of $e/m$-digit fields, finish with two linear shears, and solve the recurrence.",
    r"Each recursion level multiplies the width parameter by $m$ but the per-volume recursive cost only by $s/W$; a strict fixed deficit $s<W m$ therefore turns the linear factor $e$ into a power $e^\tau$ with $\tau<1$.",
    "explicit",
    [linear_network, frames, labels, rank_sum, tau_bound, shear, transfer, three_shears, recurrence],
    frm=["linear-network", "common-frame-principle", "subset-intersection-labels", "address-shear",
         "elementary-stream-ops", "controlled-shift", "recurrences-and-induction", "big-o"],
    page="rank-saving-recurrence",
    mot_quote=r"""After dividing cost by volume, multiplying the parameter by $m$
increases the recursive contribution by $s/W<m$. This strict inequality
is the source of the power saving.""",
    adds=[
        B("W", "wire count", "The number of wires (roles) of the fixed bit network, including all scratch wires; rows are dealt cyclically among them.", "count"),
        B("m", "label dimension", "The dimension $h^3=10^6$ of the label space, which is also the factor by which the width parameter grows per recursion level.", "count"),
        B("s", "smaller-call count", "The number of smaller recursive calls one network invocation makes, the sum of the ranks (label dimension changes) of all edge changes.", "count"),
        B("N", "bank size", "The number $v^3$ of data pairs $(X_a,Y_a)$ in each of the two banks.", "count"),
        B("L", "lost dimension", "The total label dimension lost on decreasing edges of the network.", "count"),
        B("F_k", "cost per volume", "A uniform bound on running time divided by logical volume for interchanging chunks of width $m^k$.", "direct"),
    ],
    salient=r"A pure permutation of addresses is computed in time sublinear in the number $e$ of digits moved, by forming XOR combinations of data and restoring every scratch row, and the exponent $\tau<1$ comes from a fixed rank deficit of relative size only about $1.5\cdot10^{-11}$.",
)

interchange = show(
    "S2.3",
    r"Two disjoint $u$-bit address chunks of a bit array on $[P]\times[2^u]\times[G]\times[2^u]\times[B]$ can be interchanged, $(p,h,g,d,z)\mapsto(p,d,g,h,z)$, in $O(Vu^\tau)$ time with the fixed exponent $\tau=1-2^{-50}$.",
    r"Prove the bound first for radix-$q$ chunks of power width $e=m^k$ with a row field divisible by $W^k$, by recursion through the bit network; then make a row field from the top digits of both chunks, split the remaining width in base $m$, and pad binary chunks to radix $q$.",
    r"The recursion deals rows among $W$ roles at each of $k$ levels, so it needs $W^k$ rows and widths that are powers of $m$; a general array can supply its rows from a few of its own high digits, whose movement costs less than the final bound.",
    "explicit",
    [
        key,
        infer("S2.3.2",
              r"For general $e$, interchanging and joining the top $\rho=O(\log e)$ digits of both chunks costs $O(V\rho)$ and gives a row field of range $R=q^{2\rho}\ge W^k$, padded with zero rows to a multiple of $W^k$ at most doubling the volume.",
              r"R=q^{2\rho}\ge W^k",
              ["elementary-stream-ops"]),
        infer("S2.3.3",
              r"Writing $e-\rho=\sum_ja_jm^j$ with $0\le a_j<m$ and interchanging corresponding power-width pieces costs $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$, a geometric sum since $m^k<me$.",
              r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau).",
              ["big-o"]),
        infer("S2.3.4",
              r"Binary chunks are padded numerically from $[2^u]$ to $[q^e]$, which multiplies the volume by less than $q^2$ and preserves order, and $e=O(u)$ gives $O(Vu^\tau)$.",
              r"Since $e=O(u)$ for fixed $q$, the bound is",
              ["binary-representation-and-bit-operations"]),
    ],
    frm=["rank-saving-recurrence", "address-shear", "elementary-stream-ops", "tape-address-model"],
    page="address-chunk-interchange",
    mot_quote=r"""We have proved the fast operation for power widths with enough rows.
Rows for a general array can be supplied by a few of its own high digits.
Their movement will cost less than the final bound.""",
    adds=[
        B("q", "radix prime", "A fixed odd prime, avoiding all denominators of the network's matrices, used as the radix of the address digits.", "direct"),
        B("e", "chunk width", "The number of radix-$q$ digits in each of the two chunks being interchanged.", "count"),
    ],
)

# ---------------- fast butterfly layer ----------------
phase = show(
    "S2.4.1",
    r"With phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{q_U(x)})H^{\otimes m}$ on binary labels, each edge of the complex network changes frame by one kernel $(aI+bX_v)^{\pm1}$ per vector of an orthonormal residual basis, so $C^{\otimes e}$ on $e=mf$ axes costs $s_{\rm c}<W_{\rm c}m$ child $C$-layers on $f$ axes plus binary basis changes, and $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$.",
    r"Use additivity of Hamming weight modulo four on orthogonal binary vectors to factor each frame change into two-point translation kernels, move each kernel's direction onto a coordinate slot by a binary address permutation, and convert inverse kernels and the final layer by diagonal phases.",
    r"Frames diagonalized by the same Hadamard transform turn a label change of dimension one into one two-point kernel acting on a whole selected direction, so each residual dimension costs exactly one smaller layer, which is what the rank-saving recurrence needs.",
    "recoverable",
    [
        infer("S2.4.1.1",
              r"For binary $z\cdot w=0$ the supports meet in an even number of places, so $\operatorname{wt}(z+w)\equiv\operatorname{wt}(z)+\operatorname{wt}(w)\pmod 4$; hence $q_V-q_U$ is a sum over an orthonormal residual basis, and each phase $i^{\pm[v\cdot x]}$ becomes $aI+bX_v$ or its inverse after Hadamard conjugation.",
              r"If $z\cdot w=0$, the intersection cardinality is even, so weight is",
              ["finite-field-f2-arithmetic", "linear-algebra-basics"], deferred=True),
        infer("S2.4.1.2",
              r"The residual bases have total length $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$, whose deficit $2N-2L_{\rm c}>0$ from $W_{\rm c}m$ holds because $L_{\rm c}/N=101/539<1/2$.",
              r"The deficit is $2N-2L_{\rm c}>0$.",
              ["subset-intersection-labels"], deferred=True),
        infer("S2.4.1.3",
              r"For $M\in\operatorname{GL}(m,\mathbb F_2)$ whose first columns are the residual basis, $\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}$, so an edge change is $\mathcal P_M$ applied columnwise, one $(C^{\pm1})^{\otimes f}$ per basis slot, and $\mathcal P_M^{-1}$.",
              r"\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}.",
              ["linear-algebra-basics", "vectors-matrices-and-invertibility"]),
        infer("S2.4.1.4",
              r"A negative kernel still needs only one forward child, because $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$ with address signs and a fourth-root phase.",
              r"A negative directional kernel still requires only one",
              ["complex-numbers"]),
        infer("S2.4.1.5",
              r"So one network invocation on $e=mf$ axes makes exactly $s_{\rm c}$ child calls on the $f$ axes of one slot, and after the source and sink sign corrections it yields $C^{\otimes e}$ on every role.",
              r"$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
              ["common-frame-principle"]),
        infer("S2.4.1.6",
              r"From $H_0=b\mathsf SC\mathsf S$ on each selected coordinate, $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, where $b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}$ is a binary shift and a fourth-root phase.",
              r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D.",
              ["butterfly", "roots-of-unity"]),
    ],
    frm=["common-frame-principle", "subset-intersection-labels", "butterfly", "linear-algebra-basics",
         "finite-field-f2-arithmetic", "complex-numbers", "roots-of-unity"],
    page="phase-frame-kernel",
    adds=[B("f", "child axis count", "The number of selected axes handled by each child call, $e/m$, one slot of the group.", "count")],
)

packed = show(
    "S2.4.2",
    r"In a rectangle with three chunks $x,y,z$ of $L=fK$ bits, the XORs $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ at positions $j_i=\rho+iK$, $0\le i<f$, can be done in $O(V(L^\tau+1))$ time, restoring $z$ for every initial value, when $K/\log p\to\infty$ and records are longer than every fixed power of $p$.",
    r"Apply eight chunk-wide controlled cyclic shifts that flip the parity of every $K$-bit segment of $y$ whose control bit is set and restore $z$; these agree with the ideal XORs except on an explicit set of addresses whose guard values lie near a segment end; repair that set by extracting and sorting its records.",
    r"One packed cyclic shift changes all $f$ segments at once, so a basis change costs a constant number of chunk swaps instead of $f$ separate bit operations, and because the exceptional set depends only on addresses the repair keeps the bound worst-case.",
    "explicit",
    [
        infer("S2.4.2.1",
              r"With control $c=1$ the first four operations induce the cycle $(00\ 01\ 10)$ on the parity corners of $(u,w)$ and the last four $(01\ 10\ 11)$, composing to $(00\ 10)(01\ 11)$: the parity of $u$ flips, both quotients by two are kept, $w$ is restored, and each coordinate moves by at most four.",
              r"$(00\ 10)(01\ 11)$. These facts follow by substituting the four parity",
              ["modular-arithmetic"]),
        infer("S2.4.2.2",
              r"Each line is one cyclic shift of a whole chunk by $\varepsilon\sum_i2^{j_i}[x_{j_i}=1][z_{j_i}=b]$; at addresses whose guard values lie in $[10,2^{K-1}-11]$ no segment carries into or borrows from the next, so the composite $S_0$ equals the ideal XOR map $T_0$ there.",
              r"the independent segment additions: no segment carries into or borrows",
              ["controlled-shift", "binary-representation-and-bit-operations"]),
        infer("S2.4.2.3",
              r"Each guard excludes exactly twenty of its $2^{K-1}$ values, and the complete chunk ranges give the same guard distribution at every spectator address, so a union bound over the $2(f-1)$ guards gives $|\mathcal B|\le\min\{1,80(f-1)2^{-K}\}M$, independent of the payload.",
              r"There are exactly twenty excluded values for each guard in",
              []),
        infer("S2.4.2.4",
              r"Since $T_0$ preserves $\mathcal B$ and both maps are bijections that agree off $\mathcal B$, $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$, so only the extracted bad records are sorted by destination rank and reinserted.",
              r"Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$.",
              ["sorting-and-data-movement-on-tapes", "permutations-and-cartesian-products"]),
        infer("S2.4.2.5",
              r"The omitted top position $j_{f-1}$ is supplied by one two-bit XOR among the elementary stream operations in $O(V)$; when $f=1$ this is the whole algorithm.",
              r"This costs $O(V)$ and supplies the omitted selected position.",
              ["elementary-stream-ops"]),
        infer("S2.4.2.6",
              r"After division by $V$ the record scans and the sort cost $O(A^3/R)$ and $O(p^22^{-K}(1+A/R))$, both $o(1)$, leaving $O(V(L^\tau+1))$ from the chunk swaps.",
              r"$O(p^2 2^{-K}(1+A_{\rm rect}/R))=o(1)$. This proves the final assertion.",
              ["big-omega-theta-and-little-o-notation"]),
    ],
    frm=["controlled-shift", "address-chunk-interchange", "elementary-stream-ops",
         "binary-representation-and-bit-operations", "sorting-and-data-movement-on-tapes"],
    page="packed-selected-bit-addition",
    mot_quote=r"""The correction depends only on addresses, so the time bound is
worst-case over all payloads.""",
    salient=r"The bad addresses form a fraction at most $80(f-1)2^{-K}$ fixed by the addresses alone, so a deterministic repair gives a worst-case bound over all payloads.",
)

layer_rec = show(
    "S2.4.5",
    r"The per-volume cost of the $C$-layer satisfies $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ with leaves $F(e)=O(e)$ for $e<d^{1/2}$, which sums to $O(d^{\lambda'})$ over a base-$m$ partition of the chunks.",
    r"Bound the overhead at internal nodes by $e^\lambda$ using $K\le e^{c/\beta}$, sum the geometric series using $s/W\le m^\sigma<m^\lambda$, bound the leaves, and add the $O(\log d)$ pieces.",
    r"The chunk-swap overhead $(eK)^\tau$ grows with the chunk width $K$, so recursion must stop once $e<d^\beta$ to keep $K$ small relative to $e$; the leaves stay cheap because $e^\sigma d^{\beta(1-\sigma)}$ is still a power below one.",
    "recoverable",
    [
        infer("S2.4.5.1",
              r"The $s$ child calls run on streams of volume $V/W$, so dividing by $V$ gives $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$.",
              r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),",
              ["recurrences-and-induction"]),
        infer("S2.4.5.2",
              r"At an internal node $e\ge d^\beta$, so $K\le d^c\le e^{c/\beta}$ and the overhead is $O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)$; with $a=s/W\le m^\sigma<m^\lambda$ the internal costs sum to $O(e^\lambda)$.",
              r"\(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\).",
              ["big-o"]),
        infer("S2.4.5.3",
              r"Leaves with $u<d^\beta$ chunks after $j$ levels contribute $O(a^ju)\le O(e^\sigma u^{1-\sigma})$, since $a^j\le m^{j\sigma}=(e/u)^\sigma$, also when $a<1$ because $\sigma\ge0$.",
              r"O(a^ju)\le O(e^\sigma u^{1-\sigma})",
              ["big-o"]),
        infer("S2.4.5.4",
              r"Summing over the $O(\log d)$ base-$m$ pieces and the row preprocessing gives $O(\log(2d)[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1])=O(d^{\lambda'})$.",
              r"=O(d^{\lambda'})",
              ["big-o"]),
    ],
    frm=["recurrences-and-induction", "big-o", "rank-saving-recurrence"],
)

layer = show(
    "S2.4",
    r"On an array $[P]\times[2^K]^D\times[S]$ of length-$r$ polynomial records with disk-grid coefficients, the tensor product $\mathcal H$ of $H_0$ on one common bit of each of the $D\le d$ chunks is returned as $Q_p(\mathcal Hz)$, with error below $\sqrt2\,2^{-p}$, in $O(Vd^{\lambda'})$ time with $\lambda'=1-2^{-54}$.",
    r"Write $H_0^{\otimes D}$ through the kernel $C=aI+bX$, build $C^{\otimes e}$ by recursion through the complex network with phase frames, implement the binary changes of basis by packed selected-bit additions, supply rows from the first chunks, and evaluate everything exactly with guard bits before one final truncation.",
    r"Applying the $D$ butterfly factors one at a time costs $D$ whole-array passes; the network recursion replaces that factor by the sublinear power $d^{\lambda'}$.",
    "explicit",
    [
        phase,
        packed,
        infer("S2.4.3",
              r"An invertible $m\times m$ binary matrix is a fixed product of row additions, each done on whole slots by one packed selected-bit addition, so a change of basis on $e$ axes and its inverse cost $O(V((eK)^\tau+1))$.",
              r"the complete change of basis and its inverse therefore cost",
              ["packed-selected-bit-addition"]),
        infer("S2.4.4",
              r"Applying $C$ individually on the first $q_0=O(\log d)$ chunks in $O(V\log d)$ time lets their bits serve as a row index of range $R_{\rm row}=2^{q_0K}\ge W^{k_0}$, padded to a multiple of $W^{k_0}$, so every recursive edge call acts on one role stream of volume $V/W$.",
              r"R_{\rm row}=2^{q_0K}\ge W^{k_0}",
              ["elementary-stream-ops"]),
        layer_rec,
        infer("S2.4.6",
              r"The arithmetic depth of one layer is below $C_0d^{C_1}$ with $C_1=20$, so $p+\Delta$ fractional bits and $\Delta+3$ integer bits, $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$ because $\epsilon C_1<1$, hold every intermediate Gaussian dyadic exactly.",
              r"Thus reserving \(p+\Delta\)",
              ["fixed-point-truncation", "norms-absolute-values-and-error-bounds"]),
        infer("S2.4.7",
              r"Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays, and the single final truncation $Q_p$ stays in the disk with error below $\sqrt2\,2^{-p}$.",
              r"error less than $\sqrt2\,2^{-p}$: truncation cannot increase the",
              ["fixed-point-truncation"]),
    ],
    frm=["phase-frame-kernel", "packed-selected-bit-addition", "rank-saving-recurrence", "fixed-point-truncation",
         "polynomial-ring-mod", "address-chunk-interchange", "butterfly", "elementary-stream-ops"],
    page="fast-butterfly-layer",
    mot_quote=r"""We will obtain cost $O(Vd^{\lambda'})$, with
$\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly
factors would require $D$ whole-array passes.""",
    adds=[
        B("K", "chunk width", r"The number of address bits in each axis chunk, $\lfloor d^c\rfloor$.", "count"),
        B("C", "two-point kernel", "The matrix $aI+bX$ with $a=(1+i)/2$, $b=(1-i)/2$, whose tensor powers the complex network builds.", "direct"),
        B("e", "group axis count", "The number of selected axes in the group handled by one recursive call.", "count"),
    ],
    salient=r"All $D$ butterfly factors are applied for less than the cost of $D^{\lambda'}$ passes, with intermediate values that are not contracted yet need only $o(p)$ guard bits.",
)

procedures = show(
    "S2",
    r"On a fixed number of tapes, two $u$-bit address chunks in an array of volume $V$ can be interchanged in $O(Vu^\tau)$ time, and a coefficientwise $H_0$ layer on one selected bit in each of $D\le d$ chunks can be applied in $O(Vd^{\lambda'})$ time, with fixed $\tau,\lambda'<1$.",
    r"Supply linear-time stream primitives, then derive each procedure from its own fixed linear network that exchanges two banks while restoring scratch, with frames whose edge changes are carried out by smaller recursive calls on row-role streams.",
    r"A single scan already costs $O(V)$, so beating one scan per transform level needs procedures whose per-volume cost grows sublinearly in the bits or axes handled; a recursion that divides the volume by $W$ while multiplying the parameter by $m$ with fewer than $W m$ calls gives exactly that.",
    "recoverable",
    [
        infer("S2.1",
              r"Permuting or moving a fixed-radix digit, splitting on a digit to apply a pointwise map and merging, and dealing whole rows cyclically into $W$ streams of volume $V/W$ each cost $O(V)$, including counters and cleanup.",
              r"volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
              ["tape-address-model", "sorting-and-data-movement-on-tapes", "big-o"],
              page="elementary-stream-ops"),
        infer("S2.2",
              r"An update $y\mapsto y+a(\text{controls})\bmod Q$ of a target field that follows its controls, and multiplication of $y$ by a fixed rational unit, cost $O(V)$, by splitting each fiber at $Q-a$ and merging the two pieces in the opposite order.",
              r"For an offset $a\in[Q]$, split these blocks at $Q-a$.",
              ["elementary-stream-ops", "modular-arithmetic"],
              page="controlled-shift"),
        interchange,
        layer,
    ],
    frm=["tape-address-model", "multitape-tm", "finite-alphabet-encodings-and-constant-factor-simulation"],
)

# ---------------- ring convolution ----------------
synthetic = show(
    "S3.1",
    r"With $\omega_t=y^{2r/t}$, the normalized transforms $F_{\boldsymbol t}^\mp$ over $\mathcal R_r$ on axes $t_i\in\{r/2,r\}$ are computed through a layout permutation $L$ and radix-two rounds with exact counterparts $LBF_{\boldsymbol t}^-$ and $F_{\boldsymbol t}^+B^{-1}L^{-1}$ ($B$ the bit reversal), error below $\sqrt2\ell2^{-p}$, and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.",
    r"Verify character cancellation in the ring, run decimation-in-frequency rounds that leave outputs bit-reversed, group each round's axis butterflies into one parallel layer and one record monomial, lay the selected bits out at a common offset of consecutive $K$-bit chunks by slot moves and chunk exchanges, and truncate once per round.",
    r"The simultaneous layer only acts on one common bit offset in consecutive equal-width chunks, so the transform's address bits must first be laid out that way.",
    "explicit",
    [
        infer("S3.1.1",
              r"Although $\mathcal R_r$ has zero divisors, $\sum_k\omega_t^{jk}=0$ for $t\nmid j$, because shifting $k$ by $t/2^{v+1}$ multiplies the sum by $y^{rj_0}=-1$ and the ring has no two-torsion; hence $F_t^+F_t^-=t^{-1}I$.",
              r"Hence the sum is zero, since the additive group of",
              ["roots-of-unity", "ring-and-group-notions-for-polynomials"]),
        infer("S3.1.2",
              r"Each decimation-in-frequency level applies $H_0$ to $z_k,z_{k+t/2}$ and multiplies the second output by $\omega_t^{-k}$; after all $a$ levels $(F_t^-z)_j$ sits in slot $\operatorname{rev}_a(j)$.",
              r"entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$.",
              ["fast-fourier-transform-and-divide-and-conquer", "butterfly"]),
        infer("S3.1.3",
              r"Running the levels in reverse, inverse monomial then $H_0$ with $H_0^2=I/2$, consumes that stored order, so the two procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
              r"B_tF_t^-,\qquad F_t^+B_t^{-1},",
              ["dft"]),
        infer("S3.1.4",
              r"A twiddle on one axis commutes with the butterflies of other axes, so a round is one parallel butterfly $\mathcal H$ followed by one record monomial $y^E$ whose exponent is computed from the address.",
              r"Consequently the individual axis steps may be grouped as a parallel",
              ["multidimensional-dft"]),
        infer("S3.1.5",
              r"The layout uses $O(dK)$ single-slot moves and at most $Dq-1$ exchanges of $K$-bit chunks, costing $O(Tp\,DqK^\tau)=O(Tp\,pK^{\tau-1})$.",
              r"O\bigl(Tp\,DqK^\tau\bigr)",
              ["address-chunk-interchange", "elementary-stream-ops"]),
        infer("S3.1.6",
              r"Each round on the chunks is one simultaneous-layer call costing $O(Tpd^{\lambda'})$, so the $\ell$ rounds cost $O(Tp\ell d^{\lambda'})$, while the at most $K$ prefix-slot rounds are done individually in $O(TpdK)$.",
              r"$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.",
              ["big-o"]),
        infer("S3.1.7",
              r"Truncation toward zero commutes with the signed coefficient permutation $J_E$, so each round is one exact contraction followed by one truncation, and at most $\ell$ rounds accumulate error below $\sqrt2\ell2^{-p}$.",
              r"J_EQ_p(\mathcal H z)=Q_p(J_E\mathcal H z).",
              ["fixed-point-truncation", "norms-absolute-values-and-error-bounds"]),
    ],
    frm=["dft", "polynomial-ring-mod", "butterfly", "multidimensional-dft", "fixed-point-truncation",
         "address-chunk-interchange", "elementary-stream-ops", "roots-of-unity"],
    page="synthetic-transform",
    mot_quote=r"""To apply Proposition~\ref{prop:simultaneous-layer} in a transform round,
we must place the selected bits of the participating axes at a common
offset in consecutive $K$-bit chunks.""",
    adds=[B("\\ell", "log of record length", "The exponent with $r=2^\\ell$, which is also the number of radix-two rounds on a full-length axis.", "count")],
)

signed = show(
    "S3.2",
    r"For disk-grid $f,g\in\mathcal R_r$, the exact numerators of $fg$ and the truncation $Q_p(fg/r)$ are computed in $O(rp\log(rp))$ time, with error below $\sqrt2\,2^{-p}$.",
    r"Evaluate the four integer coefficient polynomials at $B_0=2^{4p}$ with signed carries, multiply four pairs with the established multiplier, read the product coefficients back as centered residues, reduce modulo $y^r+1$, and shift.",
    r"Packing turns one record product into four long integer products, which the established $O(N\log N)$ multiplier handles on $O(rp)$-bit inputs; fields of $4p$ bits are wide enough that adjacent coefficients never interfere.",
    "recoverable",
    [
        infer("S3.2.1",
              r"Every coefficient of the four ordinary integer polynomial products satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$.",
              r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2.",
              ["polynomials"]),
        infer("S3.2.2",
              r"With carries $\rho_j\in\{0,1\}$, the residual identity reduced modulo $B_0$ makes the centered representative of $q_j+\rho_j$ equal to $h_j$, including the padded top coefficient $h_{J-1}=0$, so extraction is exact.",
              r"Thus $\widehat h_j=h_j$.",
              ["modular-arithmetic"]),
        infer("S3.2.3",
              r"The numerators $ac-be$ and $ae+bc$ are reduced modulo $y^r+1$ by subtracting the coefficient at $j+r$ from that at $j$, each result is a sum of $r$ signed products bounded by $r2^{2p}$, and the four exact integer products dominate the cost.",
              r"Four exact integer products dominate the linear",
              ["established-multiplier"]),
    ],
    frm=["polynomial-ring-mod", "established-multiplier", "fixed-point-truncation",
         "binary-representation-and-bit-operations", "polynomials"],
    page="signed-packing",
)

ring = show(
    "S3",
    r"For disk-grid arrays $f,g$ on $d-1$ power-of-two axes with entries in $\mathcal R_r=\mathbb C[y]/(y^r+1)$, the normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ is approximated with error below $\sqrt2\,M(3\ell+1)2^{-p}$ at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$, where $M=T/r$.",
    r"Apply two forward synthetic transforms keeping their common stored order $LB$, multiply corresponding records by signed packing with division by $r$, apply the opposite transform to that order, and scale exactly by $M$.",
    r"In $\mathbb C[y]/(y^r+1)$ the roots of unity are powers of $y$, so every twiddle is an exact signed coefficient shift; the transforms then consist of butterflies and address work, which the fast procedures accelerate, and the only genuine multiplications are the short pointwise polynomial products.",
    "explicit",
    [
        synthetic,
        signed,
        infer("S3.3",
              r"Expanding the sums gives $F_{\boldsymbol t}^-(f*g)=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)$, and with $F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$ the scaled opposite transform of the products divided by $r$ is $(f*g)/(rM)$; since $LB$ permutes whole records, multiplying in the retained order commutes with it.",
              r"=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g).",
              ["dft", "cyclic-convolution"]),
        infer("S3.4",
              r"The forward errors $\delta=\sqrt2\ell2^{-p}$ add through the bilinear product, the product truncation adds $\sqrt2\,2^{-p}$, and the contractive opposite transform adds $\delta$, so after scaling by $M$ the error is below $\sqrt2M(3\ell+1)2^{-p}$.",
              r"$M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed.",
              ["norms-absolute-values-and-error-bounds"]),
    ],
    frm=["synthetic-transform", "signed-packing", "fast-butterfly-layer", "cyclic-convolution",
         "address-chunk-interchange", "polynomial-ring-mod", "dft"],
    page="ring-convolution",
    mot_quote=r"""Their entries will be short polynomials in a quotient
where the required roots of unity act by exact signed permutations
of coefficient lists.""",
    adds=[B("M", "record count", "The number $T/r$ of polynomial records, the product of the first $d-1$ axis lengths.", "count")],
)

# ---------------- source transforms ----------------
gauss = show(
    "S4.1",
    r"For coprime $s<t$ with $\theta=t/s-1>p/\alpha^4$ there are contractions $A,B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ whose approximations have error below $p^2$ in time $O(tp^{3/2+\delta}\alpha)$; tensoring over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$, $\gamma=2d\alpha^2$, with axis exposure costing $O(Tp\,d^2(1+\ell^\tau))$.",
    r"Take the Harvey–van der Hoeven Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$, invert the selected Gaussian $N=C\mathsf T\mathsf D$ by a Neumann series, normalize the factors into contractions, apply them linewise, and move axes with chunk interchanges.",
    r"Sampling a Gaussian-smoothed length-$s$ transform at $t$ points equals a length-$t$ transform of Gaussian-smoothed data, and the smoothing is invertible with a small condition number when $t/s$ is separated from one; this turns prime lengths into powers of two without sorting.",
    "reconstructed",
    [
        infer("S4.1.1",
              r"The Gaussian maps satisfy $\mathsf TP_sF_s=P_tF_t\mathsf S$ and $\|N-I\|<2^{-\alpha^2\theta}$ by Harvey and van der Hoeven's Theorem 4.2 and Lemma 4.6.",
              r"\mathsf T P_sF_s=P_tF_t\mathsf S,",
              ["dft", "complex-numbers"]),
        infer("S4.1.2",
              r"Since $\alpha^2\theta>p/\alpha^2>1$, $\|N-I\|<1/2$ and $N$ is invertible by the Neumann series.",
              r"Thus $\|N-I\|<1/2$, so $N$ is invertible",
              ["norms-absolute-values-and-error-bounds"]),
        infer("S4.1.3",
              r"$\mathsf DN^{-1}C$ is a left inverse of $\mathsf T$, and the normalizations of $\mathsf D',\mathsf J',\mathsf S'$ multiply to $2^{-2\alpha^2}$, so $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$.",
              r"=2^{-2\alpha^2}P_sF_s,",
              ["vectors-matrices-and-invertibility"]),
        infer("S4.1.4",
              r"The approximations of $A$ and $B_0$ use only the ordered selection $C$ and the three quoted Gaussian maps; the two sorts that would implement $P_t$ and $P_s^{-1}$ are never executed.",
              r"In \eqref{eq:no-sort-one-dimensional} these permutations remain in the",
              ["sorting-and-data-movement-on-tapes"]),
        infer("S4.1.5",
              r"Tensoring gives the $d$-axis identity, with linewise error below $dp^2$ and line-machine time $O(dTp^{3/2+\delta}\alpha)$.",
              r"Tensoring \eqref{eq:no-sort-one-dimensional} proves",
              ["multidimensional-dft"]),
        infer("S4.1.6",
              r"Each adjacent axis interchange costs $O(Tp(1+\ell^\tau))$ by the chunk swap and a single-bit move, and exposing and restoring all axes needs $O(d^2)$ of them.",
              r"$O(Tp(1+\ell^\tau))$. Exposing and restoring one axis needs",
              ["address-chunk-interchange", "elementary-stream-ops"]),
    ],
    frm=["dft", "multidimensional-dft", "complex-numbers", "fixed-point-truncation", "address-chunk-interchange",
         "elementary-stream-ops", "norms-absolute-values-and-error-bounds", "primes-coprimality-and-gcd"],
    page="gaussian-resampling",
    adds=[B("\\alpha", "Gaussian width", "The integer width parameter of the Gaussian kernels used for resampling.", "direct")],
)

bluestein = infer(
    "S4.2",
    r"With $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$, periodic because every $t_i$ is even, $QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$: the coefficient $\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}/T=\exp(2\pi i\sum_is_ij_ik_i/t_i)/T$ is the entry of $QF_{\boldsymbol t}$, since $Q$ reads frequency $-s_ij_i$.",
    r"This is precisely the coefficient in $QF_{\boldsymbol t}$, because",
    ["dft", "cyclic-convolution", "multidimensional-dft", "complex-numbers"],
    page="bluestein-chirp",
    salient=r"The target permutation $Q$ is absorbed into the chirp exponents and costs nothing.",
)

perm = show(
    "S4.3",
    r"For $S=\prod_is_i$, $RF_{\boldsymbol s}^+[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$, and conjugating the input and output of an algorithm for $RF_{\boldsymbol s}$ gives one for $RF_{\boldsymbol s}^+$.",
    r"Show that a dilation by a unit passes through $F^+$ as its inverse, so $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$; pull $R$ out of the pointwise product; apply the normalized convolution rule.",
    r"$R$ is a dilation by the units $t_i$ modulo $s_i$, and a Fourier transform turns a dilation into the inverse dilation, so the permutation applied by both forward transforms is undone by the opposite transform without ever being executed.",
    "recoverable",
    [
        infer("S4.3.1",
              r"Substituting $h=ck$ gives $F_q^+R_c=R_c^{-1}F_q^+$ for a unit $c$ modulo $q$; each $t_i$ is a unit modulo $s_i$, so $F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.",
              r"$F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence",
              ["modular-arithmetic", "permutations-and-cartesian-products"]),
        infer("S4.3.2",
              r"A coordinate permutation commutes with pointwise products, and $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)(F_{\boldsymbol s}v)$ with $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$, so the left side equals $(u*v)/S^2$.",
              r"=\frac{u*v}{S^2},",
              ["cyclic-convolution", "dft"]),
    ],
    frm=["gaussian-resampling", "bluestein-chirp", "dft", "cyclic-convolution", "modular-arithmetic",
         "permutations-and-cartesian-products"],
    page="permutation-cancellation",
    salient=r"The source permutation $R$ is never executed, yet it disappears exactly from the convolution.",
)

source = show(
    "S4",
    r"For pairwise coprime $s_i$ and powers of two $t_i$, the source transform $RF_{\boldsymbol s}$, with its coordinate permutation $R$ left in place, equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$; its middle factor $QF_{\boldsymbol t}$ is a chirp-weighted normalized cyclic convolution; and $R$ cancels when two forward transforms are multiplied and fed to the opposite transform.",
    r"Apply Gaussian resampling linewise, keeping both permutations in the identity; convert the permuted power-of-two transform to convolution by Bluestein's chirp; and show that the source permutation cancels in a convolution.",
    r"The usual resampling sorts twice per coordinate, a logarithmic factor the saving cannot afford, so both permutations stay in the formula and are absorbed by the chirp and by cancellation.",
    "explicit",
    [gauss, bluestein, perm],
    frm=["dft", "multidimensional-dft", "cyclic-convolution"],
    mot_quote=r"""Its usual implementation sorts twice on each
coordinate. We retain both permutations in the transform formula and
compute that formula directly.""",
    adds=[
        B("R", "source permutation", "The tensor product of the coordinate permutations $(P_{s_i}u)_j=u_{t_ij}$ on the prime-length axes.", "direct"),
        B("Q", "target permutation", "The tensor product of the coordinate permutations $(P_{t_i}v)_k=v_{-s_ik}$ on the power-of-two axes.", "direct"),
    ],
)

# ---------------- the algorithm ----------------
params = show(
    "S5.1",
    r"With $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, $T\in[4n/b,8n/b)$, $t_i\in\{r/2,r\}$ and distinct primes $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ with $\eta=1/(4d)$, every resampling, layer and transform hypothesis holds, $T/2<S<T$, and the setup costs $o(n)$.",
    r"Derive the size relations, find primes in short intervals below each $t_i$ from an explicit prime-count estimate, check the resampling separation $\alpha^4\theta_i>p$, and bound the deterministic prime search.",
    r"The prime lengths must be close to the powers of two so that their product fills a fixed fraction of the padded box, while each ratio $t_i/s_i$ must stay far enough from one for resampling.",
    "explicit",
    [
        infer("S5.1.1",
              r"The choices give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$, so $r$ exceeds every fixed power of $p$ and $K/\log p\to\infty$.",
              r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad",
              ["logarithms-and-iterated-logarithm-notation", "big-omega-theta-and-little-o-notation"]),
        infer("S5.1.2",
              r"Each interval $((1-2\eta)x,(1-\eta)x]$ with $x\in\{r/2,r\}$ contains more than $d$ primes and the two intervals are disjoint, so distinct odd primes $s_i$, coprime to $t_i$, exist.",
              r"(1-2\eta)t_i<s_i\leq(1-\eta)t_i.",
              ["primes-coprimality-and-gcd"]),
        infer("S5.1.3",
              r"Bernoulli's inequality gives $S/T>(1-1/(2d))^d>1/2$, so $T/2<S<T$.",
              r"Together with $s_i<t_i$, this gives $T/2<S<T$.",
              []),
        infer("S5.1.4",
              r"Since $\theta_i>\eta$, $\alpha^4\theta_i>3db\ge p$, the separation the resampling lemma needs.",
              r"\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p.",
              []),
        infer("S5.1.5",
              r"The trial-division search costs $O(dr^{3/2}\operatorname{poly}(p))=n^{o(1)}=o(n)$.",
              r"$n^{o(1)}=o(n)$ time.",
              ["big-omega-theta-and-little-o-notation"]),
    ],
    frm=["crt-address-map", "gaussian-resampling", "polynomial-ring-mod", "radix-digit-convolution",
         "primes-coprimality-and-gcd", "logarithms-and-iterated-logarithm-notation"],
    page="parameter-choice",
    mot_quote=r"""The distinct prime lengths $s_i$ must be close to the powers of two
$t_i$: their product must occupy a fixed fraction of the padded box,
while each ratio $t_i/s_i$ must leave enough separation for resampling.""",
)

crt = show(
    "S5.3",
    r"$\Phi:x\mapsto\prod_ix_i^{\mu_i}$ with $\mu_i=P_i^{-1}\bmod s_i$ is an isomorphism $\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\dots,x_d]/(x_1^{s_1}-1,\dots,x_d^{s_d}-1)$ that preserves cyclic convolution, and it and its inverse, with padding, cost $O(Tp\,d^2(1+\ell^\tau))$.",
    r"Check that the image of $x$ has order $S$, write each new coordinate as a triangular function of the mixed-radix digits, perform the updates as prefix-controlled cyclic shifts in descending target order, and reorder axes with chunk interchanges.",
    r"Choosing the powers $\mu_i$ with prefix products makes the change of order triangular, so it becomes a sequence of controlled cyclic shifts, which cost linear time, instead of a general sort.",
    "explicit",
    [
        infer("S5.3.1",
              r"The image of $x$ has order $S$ because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all $S$ target monomials and $\Phi$ is an isomorphism.",
              r"$\Phi$ is an isomorphism and preserves cyclic convolution.",
              ["chinese-remainder-theorem", "ring-and-group-notions-for-polynomials"]),
        infer("S5.3.2",
              r"For $k=\sum_ja_jP_j$ the axis-$i$ coordinate is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\bmod s_i$, since terms with $j>i$ vanish modulo $s_i$ and $\mu_iP_i\equiv1$.",
              r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}.",
              ["modular-arithmetic"]),
        infer("S5.3.3",
              r"Updating targets $i=d,\dots,1$ keeps every control at its original digit; each update rotates the valid interval $[0,s_i)$, fixes the padding, and needs offsets costing $o(Tp)$ to prepare.",
              r"Each triangular update is a prefix-controlled cyclic shift.",
              ["controlled-shift"]),
        infer("S5.3.4",
              r"Reversing the axis order takes $O(d^2)$ adjacent axis interchanges, for a total of $O(Tp\,d^2(1+\ell^\tau))$.",
              r"O\bigl(Tp\,d^2(1+\ell^\tau)\bigr).",
              ["address-chunk-interchange"]),
    ],
    frm=["cyclic-convolution", "polynomials", "controlled-shift", "chinese-remainder-theorem",
         "address-chunk-interchange", "primes-coprimality-and-gcd"],
    page="crt-address-map",
    mot_quote=r"""The following map uses that
algebraic split, with coordinate powers that make the change of order a
sequence of controlled cyclic shifts.""",
)

twist = show(
    "S5.4",
    r"With $\zeta=e^{\pi i/r}$, $\Theta:x_d\mapsto\zeta y$ is a norm-preserving isomorphism $\mathbb C[x_d]/(x_d^r-1)\to\mathbb C[y]/(y^r+1)$, so $D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$ convolves all $d$ axes.",
    r"Check that $\zeta y$ has $r$-th power one in the ring, verify the sign of the negacyclic wrap after twisting, and extend the twist linewise to the last axis.",
    r"The ring convolution computes negacyclic products in the last coordinate, while the chirp needs ordinary cyclic convolution; a diagonal phase twist converts one into the other exactly.",
    "explicit",
    [
        infer("S5.4.1",
              r"$\Theta$ is well defined since $(\zeta y)^r=(-1)(-1)=1$, and it is diagonal on monomials, multiplying coefficient $k$ by $\zeta^k$.",
              r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$.",
              ["roots-of-unity", "polynomial-ring-mod"]),
        infer("S5.4.2",
              r"For $k+l=j+hr$ with $h\in\{0,1\}$, a twisted product term carries $\zeta^{k+l}(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
              r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j.",
              ["complex-numbers"]),
        infer("S5.4.3",
              r"Extending linewise, $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$, a bilinear contraction.",
              r"\mathcal M_r(\iota D_+f,\iota D_+g)",
              ["cyclic-convolution"]),
    ],
    frm=["polynomial-ring-mod", "cyclic-convolution", "complex-numbers", "roots-of-unity"],
    page="phase-twist",
    mot_quote=r"""A phase twist changes the last cyclic coordinate into a polynomial
modulo $y^r+1$; its negative wrap gives precisely the original cyclic
wrap after the twist is removed.""",
    salient=r"The negative wrap of $y^r=-1$ becomes exactly the positive cyclic wrap, $\zeta^{k+l}(-1)^h=\zeta^j$.",
)

recovery = show(
    "S5.7",
    r"After the final scaling, every computed coefficient differs from the true integer coefficient by less than $1/2$, so rounding recovers it exactly, and radix-$2^b$ carry propagation yields the $2n$-bit product.",
    r"Propagate errors through contractions and bilinear contractions while keeping disk margins, multiply by the known scales, compare with $2^{-p}=2^{-6b}$, and run the carry recurrence with an exact invariant.",
    r"All errors are fixed multiples of $2^{-p}$ times quantities like $2^\gamma T^2L$, and the scales multiply them by at most $2^{3b}$, so $p=6b$ fractional bits leave the final error below the integer spacing.",
    "recoverable",
    [
        infer("S5.7.1",
              r"Each computed source transform has error below $E_s2^{-p}$ with $E_s=9\cdot2^\gamma TL$, $L=\log_2T$, and its output stays in the disk.",
              r"E_s=9\,2^\gamma TL,",
              ["norms-absolute-values-and-error-bounds", "fixed-point-truncation"]),
        infer("S5.7.2",
              r"The pointwise product, the opposite transform and the scaling by $S$ give $\widetilde w$ approximating $w=(u*v)/S$ with error below $E_w2^{-p}$, where $E_w=S(3E_s+2)<28\cdot2^\gamma T^2L$.",
              r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L.",
              ["norms-absolute-values-and-error-bounds"]),
        infer("S5.7.3",
              r"Scaling by $2^{2b+4}S$ with $S\le T<2^b$, $L<b$ and $\gamma\le b/4$ makes the final error below $448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<1/2$.",
              r"<448b\,2^{-b+\gamma}",
              ["logarithms-and-iterated-logarithm-notation"]),
        infer("S5.7.4",
              r"The true coefficients are integers, so the nearest integer to each computed value is the unique correct coefficient.",
              r"The strict error below $1/2$ makes the nearest integer to",
              ["floor-ceiling-and-summation-notation"]),
        infer("S5.7.5",
              r"Carries $k_{j+1}=\lfloor(c_j+k_j)/2^b\rfloor$ stay below $2^{2b}$ and the invariant $\sum_{h<j}c_h2^{bh}=\sum_{h<j}d_h2^{bh}+k_j2^{bj}$ fixes the low digits, so the output is the exact $2n$-bit product.",
              r"The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$.",
              ["recurrences-and-induction", "binary-representation-and-bit-operations"]),
    ],
    frm=["radix-digit-convolution", "fixed-point-truncation", "norms-absolute-values-and-error-bounds"],
    page="exact-recovery",
)

algorithm = show(
    "S5",
    r"For all sufficiently large $n$, the pipeline (radix digits, $\Phi$, two computed source transforms, pointwise product, opposite transform, scalings by $S$ and $2^{2b+4}S$, rounding, $\Phi^{-1}$, carries) outputs exactly $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$.",
    r"Fix parameters meeting every interface hypothesis, identify the exact counterpart of the pipeline with the integer digit convolution, and bound the accumulated numerical error below $1/2$ so that rounding and carries are exact.",
    r"Every stage's exact counterpart is a known linear map, so the pipeline is exact once the composed counterpart is the digit convolution and the composed approximation error is smaller than half the integer spacing.",
    "recoverable",
    [
        params,
        infer("S5.2",
              r"With $q=\lceil n/b\rceil$ digits in base $2^b$, the product polynomial has degree $2q-2<T/2<S$, so convolution modulo $x^S-1$ has no wraparound, and every coefficient satisfies $0\le c_j<2^{3b}$.",
              r"Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
              ["polynomials", "cyclic-convolution", "floor-ceiling-and-summation-notation"],
              page="radix-digit-convolution"),
        crt,
        twist,
        infer("S5.5",
              r"The computed source transform (linewise $\mathcal A$, the chirp transform built on the twisted ring convolution, linewise $\mathcal B_0$, and exact scaling by $2^\gamma$) has exact counterpart $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, and conjugation gives the opposite procedure.",
              r"=RF_{\boldsymbol s}.",
              ["bluestein-chirp", "gaussian-resampling", "phase-twist", "ring-convolution"]),
        infer("S5.6",
              r"By the cancellation identity the three transforms give $(u*v)/S^2$; scaling by $S$ gives $w=(u*v)/S$, and scaling by $2^{2b+4}S$ gives $2^{2b+4}(u*v)$, whose $\Phi$-preimage is the integer digit convolution.",
              r"The two occurrences of $S$ in this algorithm undo different",
              ["permutation-cancellation", "crt-address-map"]),
        recovery,
    ],
    frm=["radix-digit-convolution", "crt-address-map", "gaussian-resampling", "permutation-cancellation",
         "bluestein-chirp", "phase-twist", "ring-convolution", "exact-recovery", "parameter-choice"],
    page="multiplication-algorithm",
    adds=[B("b", "digit width", "The number of bits $\\lceil\\log_2n\\rceil$ in each radix-$2^b$ input digit.", "count")],
)

timing = show(
    "S6",
    r"Divided by $V=Tp=\Theta(n)$, every cost is at most $p^{1-2\kappa}$ times a fixed power of $\log p$, so the total time is $O(n(\lg n)^{1-\kappa})$.",
    r"Tabulate the normalized cost of every operation as a power of $p$, compute each margin below one from the fixed rational exponents, and show that setup and exceptional-repair work is $o(V)$.",
    r"Since $V=\Theta(n)$ and $p=\Theta(\log n)$, a normalized cost of $p^{1-\kappa}$ is exactly the claimed bound.",
    "recoverable",
    [
        infer("S6.1",
              r"The seven dominant normalized costs $dK$, $pK^{\tau-1}$, $\ell d^{\lambda'}$, $d^2(1+\ell^\tau)$, $dp^{1/2+\delta}\alpha$, $dp^\delta$ and $\log(rp)$ have margins below one whose minimum is $g_2=\epsilon c(1-\tau)=2^{-181}=2\kappa$, from the chunk exchanges of the transform layout.",
              r"Thus $\min_i g_i=2^{-181}=2\kappa$.",
              ["big-o"]),
        infer("S6.2",
              r"Descriptor setup over the $p^{O(1)}$ recursion visits and the sorting of exceptional records total $o(V)$, because $r$ and $2^K$ exceed every fixed power of $p$.",
              r"=O(Vp^{A'}2^{-K})=o(V)",
              ["big-omega-theta-and-little-o-notation"]),
        infer("S6.3",
              r"Absorbing any fixed power of $\log p$ into $p^\kappa$ gives $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$, with schoolbook multiplication below a fixed cutoff.",
              r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}).",
              ["big-o", "logarithms-and-iterated-logarithm-notation"]),
    ],
    frm=["multiplication-algorithm", "parameter-choice", "address-chunk-interchange", "fast-butterfly-layer",
         "established-multiplier", "ring-convolution", "gaussian-resampling", "big-o"],
    page="time-accounting",
    salient=r"The whole saving $\kappa=2^{-182}$ is set by one bottleneck, $g_2=\epsilon c(1-\tau)$: the chunk-swap exponent $\tau=1-2^{-50}$ diluted by the chunk-width exponent $\epsilon c$.",
)

root = show(
    "S0",
    r"One deterministic multitape Turing machine with a fixed finite alphabet and a fixed finite number of tapes multiplies two $n$-bit integers exactly in worst-case time $T_A(n)=O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.",
    r"Build two tape procedures that beat one scan per level (an address-chunk interchange and a simultaneous butterfly layer) from fixed linear networks with a strict rank deficit; use them inside the Harvey–van der Hoeven reduction of multiplication to convolution (radix digits, Chinese-remainder axes, Gaussian resampling with chirps, a phase twist to $\mathbb C[y]/(y^r+1)$); recover the exact product; and divide every cost by $V=Tp=\Theta(n)$.",
    r"The transform calculation consists of address rearrangements, signed shifts and butterflies, and a single scan per transform level already costs $\Theta(n\log n)$; so both data movement and butterfly arithmetic must be done faster than one scan per level.",
    "explicit",
    [
        infer("S1",
              r"Schönhage and Strassen proposed $n\log n$ as the optimal multitape order and Harvey and van der Hoeven reached $O(n\log n)$, so a bound $O(n(\lg n)^{1-\kappa})$ gives $T_A(n)/(n\lg n)\to0$ and refutes an eventual $\Omega(n\log n)$ lower bound for every fixed machine.",
              r"proposed $n\log n$ as the optimal order of growth",
              ["big-o", "multitape-tm", "big-omega-theta-and-little-o-notation"],
              page="integer-multiplication-conjecture"),
        procedures,
        ring,
        source,
        algorithm,
        timing,
    ],
    frm=["integer-multiplication-conjecture", "multiplication-algorithm", "time-accounting", "multitape-tm", "big-o"],
    page="main-theorem",
    mot_quote=r"""Scanning an array of $\Theta(n)$ stored bits at each of
$\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$.
We therefore need savings in both movement and arithmetic.""",
    adds=[
        B("V", "stored bit volume", "The logical number of stored data bits of the array being processed, $\\Theta(n)$ for the full transform arrays.", "count"),
        B("p", "working precision", "The number $6\\lceil\\log_2n\\rceil$ of fractional bits in every fixed-point coefficient.", "count"),
        B("d", "axis count", "The number $\\lfloor b^\\epsilon\\rfloor$ of transform axes, which bounds the number of chunks in a butterfly layer.", "count"),
        B("T", "padded box size", "The power of two in $[4n/b,8n/b)$ that is the product of the power-of-two axis lengths.", "count"),
        B("r", "record length", "The power of two giving the number of complex coefficients of each polynomial record in $\\mathbb C[y]/(y^r+1)$.", "count"),
        B("S", "source size", "The product of the distinct prime axis lengths $s_i$.", "count"),
    ],
    salient=r"The saving is a fixed power of the logarithm, uniform over all input lengths, below the $n\log n$ order that Schönhage and Strassen conjectured optimal, and the address part is obtained for a pure permutation by computing XOR combinations of data.",
)

ans = {"root": root}
json.dump(ans, open(OUT, "w"), ensure_ascii=False, indent=1)

# -------- self checks --------
order = """integer-multiplication-conjecture polynomial-ring-mod fixed-point-truncation established-multiplier tape-address-model elementary-stream-ops controlled-shift linear-algebra-basics linear-network address-shear common-frame-principle subset-intersection-labels rank-saving-recurrence address-chunk-interchange packed-selected-bit-addition signed-packing cyclic-convolution radix-digit-convolution phase-twist exact-recovery dft multidimensional-dft butterfly synthetic-transform bluestein-chirp phase-frame-kernel fast-butterfly-layer ring-convolution gaussian-resampling permutation-cancellation crt-address-map parameter-choice multiplication-algorithm time-accounting main-theorem""".split()
known = set("""big-o polynomials complex-numbers multitape-tm logarithms-and-iterated-logarithm-notation big-omega-theta-and-little-o-notation binary-representation-and-bit-operations modular-arithmetic primes-coprimality-and-gcd chinese-remainder-theorem roots-of-unity vectors-matrices-and-invertibility finite-field-f2-arithmetic permutations-and-cartesian-products floor-ceiling-and-summation-notation recurrences-and-induction norms-absolute-values-and-error-bounds fast-fourier-transform-and-divide-and-conquer sorting-and-data-movement-on-tapes finite-alphabet-encodings-and-constant-factor-simulation ring-and-group-notions-for-polynomials""".split())
idx = {p: i for i, p in enumerate(order)}
pages_used = {}
froms = set()
ids = set()
last = -1
problems = []
def walk(n, page):
    global last
    assert n["id"] not in ids, n["id"]; ids.add(n["id"])
    pg = n.get("page") or page
    if n.get("page"):
        if n["page"] in pages_used: problems.append("page twice " + n["page"])
        pages_used[n["page"]] = n["id"]
    for f in n.get("from", []):
        froms.add(f)
        if f in known: continue
        if f not in idx: problems.append(f"{n['id']}: unknown {f}")
        elif idx[f] >= idx[pg]: problems.append(f"{n['id']} (page {pg}): from {f} not before")
    for q in ([n["quote"]] if n.get("quote") else []) + ([n["motivation"]["quote"]] if n.get("motivation") and n["motivation"].get("quote") else []):
        if q["quote"] not in SRC: problems.append(f"{n['id']}: quote not found: {q['quote'][:60]!r}")
    if n["intention"] == "infer":
        pos = SRC.find(n["quote"]["quote"])
        if SRC.count(n["quote"]["quote"]) > 1: problems.append(f"{n['id']}: quote ambiguous")
        if not n.get("deferred"):
            if pos < last: problems.append(f"{n['id']}: out of order (line {SRC[:pos].count(chr(10))+1})")
            last = max(last, pos)
    for c in n.get("children", []): walk(c, pg)
walk(root, None)
for p in order:
    if p not in pages_used and p not in froms: problems.append("page unused " + p)
print("\n".join(problems) or "ok")
