import json, re, sys, os

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SRC = open(os.path.join(BASE, "sources/paper.tex")).read()
OUT = os.path.join(BASE, "exegenius/tasks/0003-argument.answer.json")

problems = []


def fix(q):
    """Return q exactly as in the source; '¶' marks a line break.
    If the exact text is missing, match with flexible whitespace and use the source text."""
    q = q.replace("¶", "\n")
    if q in SRC:
        return q
    pat = r"\s+".join(re.escape(part) for part in q.split())
    m = re.search(pat, SRC)
    if m:
        return m.group(0)
    problems.append(q)
    return q


def ev(q):
    return {"source": "paper", "quote": fix(q)}


def mot(text, source, quote=None):
    d = {"text": text, "source": source}
    if quote is not None:
        d["quote"] = ev(quote)
    return d


def bind(symbol, name, meaning, relation):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


def show(id, claim, method, motivation, children, page=None, frm=(), salient=None, adds=None):
    d = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children}
    if page:
        d["page"] = page
    d["from"] = list(frm)
    if salient:
        d["salient"] = salient
    if adds:
        d["adds"] = adds
    return d


def infer(id, claim, quote, frm=(), page=None, deferred=False, salient=None):
    d = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote)}
    if page:
        d["page"] = page
    d["from"] = list(frm)
    if deferred:
        d["deferred"] = True
    if salient:
        d["salient"] = salient
    return d


# ---------------------------------------------------------------- S1.1 key step
S111 = show(
    "S1.1.1",
    r"The fixed scalar network on banks $X_a,Y_a$ (indexed by triples $a$ of three-element subsets of $[100]$), whose three stages run forward, inverse and forward eight-row invocations, sends $(X_a,Y_a)\mapsto(-Y_a,X_a)$, which over $\mathbb F_2$ is the exchange of the two banks, and restores every scratch wire whatever its initial value.",
    "Show that one eight-row invocation adds $x$ to $y$ independently of the scratch values by computing its net copy, gather, scatter and side-injection coefficients, then compose the three stages.",
    mot("Subtracting the effect of the old scratch values first and restoring them last makes the net map independent of the scratch contents, so arbitrary rows of the array can later serve as scratch wires.",
        "explicit",
        r"The first two rows of¶the following schedule remove the effect of the old scratch values;¶the next four introduce the source values and add their effect to the¶target; the last two restore the scratch values."),
    [
        infer("S1.1.1.1",
              r"With initial side and central vectors $a,c$, rows 0–1 subtract $\mathcal Ja+\mathcal Rc$, rows 2–3 change the scratch to $a+\mathcal Vx$, $c+\mathcal Gx$, rows 4–5 add $\mathcal R(c+\mathcal Gx)+\mathcal J(a+\mathcal Vx)$ and rows 6–7 restore $a,c$, so the net effect is $y\gets y+(\mathcal J\mathcal V+\mathcal R\mathcal G)x$ for every $a,c$.",
              r"The net target change is¶$(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of¶$a,c$."),
        infer("S1.1.1.2",
              r"In the bit case the gather–scatter coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod 2$; side wires join exactly the pairs with $|S\cap T|=1$ and cancel them, pairs with intersection $0$ or $2$ already have coefficient $0$, and $S=T$ gives $1$, so $\mathcal J\mathcal V+\mathcal R\mathcal G=I$ and the invocation performs $y\gets y+x$.",
              r"In the bit case, the central coefficient from $x_T$ to $y_S$ is¶$|S\cap T|\bmod2$.  The side contribution cancels exactly the¶intersection-one cases"),
        infer("S1.1.1.3",
              r"Running stage 1 forward ($Y\gets Y+X$), stage 2 inverse ($X\gets X-Y$) and stage 3 forward gives $(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x)$, and each invocation restores its own scratch wires.",
              r"Starting from $(x,y)$, the three stages give¶$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$."),
    ],
    page="linear-network",
    frm=["linear-algebra-basics", "finite-field-f2-arithmetic", "vectors-matrices-and-invertibility"],
    salient="The exchange is exact for every initial content of the scratch wires, so scratch roles never need to be cleared.",
)

S112 = show(
    "S1.1.2",
    r"If each scalar is replaced by an array on a common address set $\Omega$, each source, gate and sink $v$ is given an invertible linear frame $D_v$, and $D_vD_u^{-1}$ is applied on each edge from $u$ to $v$, then the network implements $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$, so a route from role $w$ to role $\rho(w)$ with scalar sign $\varepsilon_w$ applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$.",
    "Maintain along edges and through pointwise gates the invariant that the stored array at each vertex is its frame applied to the logical array.",
    mot("Separating the endpoint operator, which only the terminal frames determine, from the intermediate frames leaves the latter free to be chosen so that every edge change is cheap.",
        "explicit",
        r"Once the scalar routing is fixed,¶the endpoint frames determine the array operator on each route; the¶intermediate frames can then be chosen to make each edge change inexpensive."),
    [
        infer("S1.1.2.1",
              r"All incidences of a gate share the frame $D_v$, and linearity gives $\sum_jc_jD_v\varphi_j=D_v(\sum_jc_j\varphi_j)$, so the common frame commutes with the pointwise gate and the invariant passes from the sources to the sinks.",
              r"Thus the common frame commutes with the pointwise gate, and¶the invariant continues to the sinks."),
        infer("S1.1.2.2",
              r"Hence the implemented operator is $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$, and for a signed role permutation each route, auxiliary routes included, applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$.",
              r"All roles, including¶the auxiliary roles, enter this identity."),
    ],
    page="common-frame-principle",
    frm=["linear-network", "linear-algebra-basics", "vectors-matrices-and-invertibility"],
    salient="The intermediate frames cancel completely: only the two endpoint frames of a route affect what it does.",
)

S113 = show(
    "S1.1.3",
    r"Giving each gate and sink the projection $M_v=P_U$ onto its label $U$, a nondegenerate subspace of $\mathcal F=(\mathbb Q^{h})^{\otimes3}$ of dimension $m=h^3$ built from triple indicators, and giving $X_a$ the source matrix $-P_{U_a}$, makes every endpoint difference $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}$ equal to $I_m$ while the ranks of all edge differences sum to $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.",
    r"Use the bilinear form $x^{\mathsf T}(I-J/9)y$, under which neighboring triple indicators are orthogonal, to prescribe nested labels stage by stage, count dimension changes edge by edge (they telescope at gates), and add the extra rank of the negative source projections.",
    mot("The signed dimension changes are fixed by the terminal labels at $Wm-2N$ and ranks equal absolute changes, so the only freedom is the total loss on decreasing edges, which must stay below $N/2$ for the rank sum to fall below $Wm$.",
        "explicit",
        r"The saving will come from keeping the total dimension lost on decreasing¶edges small relative to $N$."),
    [
        infer("S1.1.3.1",
              r"Under $\langle x,y\rangle=x^{\mathsf T}(I-J/9)y$ on $\mathbb Q^{h}$ (eigenvalues $1$ and $-91/9$, so nondegenerate), triple indicators satisfy $\langle t_S,t_T\rangle=|S\cap T|-1$ and $\langle t_T,t_T\rangle=2$, so every triple line is nondegenerate and neighboring triples ($|S\cap T|=1$) are orthogonal.",
              r"Thus every triple line is nondegenerate, and neighboring triple lines¶are orthogonal, in the label field belonging to either construction."),
        infer("S1.1.3.2",
              r"On a side wire joining neighboring triples with indicators $t_X,t_Y$, the remaining label component can pass through $P\otimes\langle t_X\rangle\subset P\otimes t_Y^\perp\subset P\otimes F$, which is possible only because $t_X\perp t_Y$.",
              r"The first inclusion is possible because $t_X\perp t_Y$."),
        infer("S1.1.3.3",
              r"Every edge joins comparable nondegenerate labels and label dimension never decreases along an edge, with one exception: the central-wire edge from time 3 to time 4, which loses $P\otimes F\otimes Q$ of dimension $h$; with $I$ invocations and $c$ central wires each, the total loss is $L=Ich$.",
              r"The only decreasing¶edges are the central-wire edges from time 3 to time 4; their dimension¶loss is $h$."),
        infer("S1.1.3.4",
              r"Each touched wire has one incoming and one outgoing incidence at a gate with the same label, so the signed dimension changes telescope to the sink total $Wm-N$ minus the source total $N$, i.e. $Wm-2N$, and the absolute changes sum to $Wm-2N+2L$.",
              r"The signed sum of dimension changes telescopes at every gate: each¶touched wire has one incoming and one outgoing incidence with the same¶gate label."),
        infer("S1.1.3.5",
              r"The loss ratio is $L_{\rm b}/N=100/539$, smaller than $1/2$.",
              r"In particular, both are smaller than $1/2$."),
        infer("S1.1.3.6",
              r"For nested nondegenerate $U\subset V$, $P_V-P_U$ is the projection onto $V\cap U^\perp$, so its rank is $\dim V-\dim U$; the only exceptions are the $N$ first edges on the $X_a$, whose matrix $P_{U_a}-(-P_{U_a})=2P_{U_a}$ has rank one where the dimension change is zero, so $s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N=W_{\rm b}m-N+2L_{\rm b}$, short of $W_{\rm b}m$ by $N-2L_{\rm b}>0$.",
              r"The only exceptions are the $N$ negative source projections."),
        infer("S1.1.3.7",
              r"For an input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$, and every other role has zero source matrix and identity sink matrix, so every route differs by exactly $I_m$.",
              r"For an input $X_a$ the endpoint difference is¶$P_{U_a^\perp}-(-P_{U_a})=I_m$."),
    ],
    page="subset-intersection-labels",
    frm=["linear-network", "common-frame-principle", "linear-algebra-basics", "vectors-matrices-and-invertibility", "finite-field-f2-arithmetic"],
    salient="The total rank of all edge changes is strictly below the trivial count $Wm$, and the gap comes only from intersection sizes of three-element subsets through $\\langle t_S,t_T\\rangle=|S\\cap T|-1$.",
    adds=[
        bind("N", "bank pair count", "The number $\\binom{100}{3}^3$ of index triples $a$, that is, of data pairs $(X_a,Y_a)$ the network exchanges.", "count"),
        bind("L", "lost dimension", "The total label dimension lost on the decreasing edges of the network.", "count"),
        bind("h", "ground set size", "The number $100$ of points whose three-element subsets index the data.", "count"),
    ],
)

S115 = show(
    "S1.1.5",
    r"For a rational $m\times m$ matrix $A$ of rank $a$, the address permutation $(H,D)\mapsto(H+AD,D)$ on two groups of $m$ fields over $\mathbb Z/q^b$ (with $q$ a fixed prime avoiding all denominators) costs exactly $a$ interchanges of pairs of $b$-digit fields plus $O(V)$ further work, and the three shears $D\gets D-H$, $H\gets H+D$, $D\gets H-D$ interchange $H$ and $D$.",
    r"Factor $A=E_1\Pi E_2$ with invertible lower-triangular $E_1,E_2$ and a partial permutation $\Pi$ with $a$ ones, apply the triangular factors as controlled shifts in linear time, and realize each one of $\Pi$ by a single field interchange between two controlled shifts.",
    mot("Controlled shifts update a later field from earlier fields in linear time, so lower-triangular coordinate changes are cheap and only the rank-many entries of $\\Pi$ call for genuine interchanges.",
        "explicit",
        r"Lemma~\ref{lem:ordered-affine-streams} updates a later field using¶earlier fields in linear time.  Lower triangular changes of coordinates¶can be performed entirely in this direction."),
    [
        infer("S1.1.5.1",
              r"Every rational $m\times m$ matrix of rank $a$ factors as $E_1\Pi E_2$ with invertible lower-triangular $E_1,E_2$ and $\Pi$ having exactly $a$ ones, at most one per row and column (a Bruhat factorization with the coordinate order reversed, found by eliminating with the rightmost entry of the topmost nonzero row as pivot).",
              r"where $E_1,E_2$ are invertible lower triangular rational matrices and¶$\Pi$ has exactly $a$ entries equal to one"),
        infer("S1.1.5.2",
              r"A lower-triangular transformation of $H$ or of $D$ costs $O(V)$: coordinates are updated in descending physical order, each by a controlled shift from earlier coordinates that still hold their original values.",
              r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:¶update coordinates in descending physical order."),
        infer("S1.1.5.3",
              r"A one of $\Pi$ at $(i,j)$, i.e. $H_i\gets H_i+D_j$, is done by $D_j\gets D_j+H_i$, $(H_i,D_j)\gets(D_j,H_i)$, $D_j\gets H_i-D_j$, which takes $(h,d)$ to $(h+d,d)$ with one interchange, so the number of recursive calls is exactly the rank $a$.",
              r"On an initial pair $(h,d)$ this sequence yields $(h+d,d)$.¶It uses just one interchange."),
        infer("S1.1.5.4",
              r"The updates $D\gets D-H$, $H\gets H+D$, $D\gets H-D$ send $(H,D)$ to $(D,H)$; only the middle shear needs the network, while the outer two target the later group and cost $O(V)$.",
              r"The other two¶updates target the later group and have linear cost.",
              deferred=True),
    ],
    page="address-shear",
    frm=["linear-algebra-basics", "controlled-shift", "elementary-stream-ops", "vectors-matrices-and-invertibility", "modular-arithmetic", "primes-coprimality-and-gcd"],
)

S11 = show(
    "S1.1",
    r"For $e=m^k$, two disjoint chunks of $e$ radix-$q$ digits preceded by a row field whose length is divisible by $W^k$ can be interchanged in $O(Ve^\tau)$ time, because the time per volume obeys $F_k\le(s/W)F_{k-1}+O(1)$ with $s/W<m^\tau$.",
    r"Deal whole rows cyclically to $W$ role streams, run the fixed bit network on them pointwise with address-shear frames whose endpoint differences are the identity, implement each edge's change of frame by as many smaller interchanges as the rank of its matrix, and solve the resulting recurrence.",
    mot("Dividing cost by volume, one level of recursion multiplies the parameter by $m$ but the recursive contribution only by $s/W$; the strict inequality $s<Wm$ is exactly what turns the trivial cost linear in $e$ into $e^\\tau$ with $\\tau<1$.",
        "explicit",
        r"Because the sum of these ranks is less than the number of wires times¶$m$, the resulting recurrence saves a power of the chunk width."),
    [
        S111,
        S112,
        S113,
        infer("S1.1.4",
              r"The relative deficit $(W_{\rm b}m-s_{\rm b})/(W_{\rm b}m)=339/22587335000000$ exceeds $20\cdot2^{-50}$, and $\log m<20$ gives $m^{1-2^{-50}}>m(1-20\cdot2^{-50})$, so $s/W<m^\tau$ with $\tau=1-2^{-50}$.",
              r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$.",
              frm=["logarithms-and-iterated-logarithm-notation"]),
        S115,
        infer("S1.1.6",
              r"Within each prefix, row $Wg+(w-1)$ goes to role stream $w$ as row $g$, so the $W$ streams have the same address shape, including the full ranges of $H$ and $D$, each with logical volume $V/W$ and a row count divisible by $W^{k-1}$; this supplies the common address set of the frame identity.",
              r"These streams have exactly the same remaining shape, including the¶full ranges of $H$ and $D$.",
              frm=["elementary-stream-ops", "tape-address-model"]),
        infer("S1.1.7",
              r"With the frame $\Phi_{M_v}$ moving $(H,D)$ to $(H+M_vD,D)$, which commutes with pointwise XOR gates, the output on role $\rho(w)$ is $\Phi_{M_{\mathrm{out}(\rho(w))}}\Phi_{-M_{\mathrm{in}(w)}}f_w=\Phi_{I_m}f_w$, so after the rows are merged back every original row, scratch rows included, has undergone $H\gets H+D$.",
              r"The result¶is $H\leftarrow H+D$ on every original row, including rows assigned¶to scratch roles, whose initial values were arbitrary."),
        infer("S1.1.8",
              r"An edge whose matrix has rank $a$ costs $a$ recursive interchanges of $(e/m)$-digit fields on one stream of volume $V/W$, so one invocation makes exactly $s$ smaller calls, while splitting, merging, gates and triangular updates are fixed in number and cost $O(V)$; hence $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.",
              r"The number of recursive calls is the sum of the edge ranks, exactly $s$.",
              frm=["recurrences-and-induction"]),
        infer("S1.1.9",
              r"With $s/W<m^\tau$ the unrolled sum $\sum_{j\le k}(s/W)^j$ is $O(m^{k\tau})$ (at most $k+1$ if $s/W\le1$), so $F_k=O(e^\tau)$.",
              r"Hence $F_k=O(e^\tau)$.",
              frm=["recurrences-and-induction", "big-o"]),
        infer("S1.1.10",
              r"Parking the $W-1$ inactive role streams on a stack around each child call and restoring them costs $O(V)$ at a node with only $s$ children, so the fixed-tape schedule adds nothing to the factor $s/W$.",
              r"Temporary storage is¶therefore not substituted for logical volume in the factor $s/W$.",
              frm=["sorting-and-data-movement-on-tapes"]),
    ],
    page="rank-saving-recurrence",
    frm=["linear-network", "common-frame-principle", "subset-intersection-labels", "address-shear", "elementary-stream-ops", "tape-address-model", "recurrences-and-induction", "big-o"],
    salient="The exponent $\\tau<1$ is strict although the deficit is minute: $s_{\\rm b}/(W_{\\rm b}m)$ falls short of one only by $339/22587335000000$, yet any strict deficit compounds over the $\\log_m e$ recursion levels into a power saving in $e$.",
    adds=[
        bind("W", "wire count", "The number of wires of the fixed bit network, scratch wires included; rows of the array are dealt cyclically to these roles.", "count"),
        bind("m", "label dimension", "The dimension $100^3$ of the label space, which is also the number of digit fields each chunk is cut into at one recursion level.", "count"),
        bind("s", "smaller call count", "The sum of the ranks of all edge matrices, that is, the number of smaller interchanges one run of the network makes.", "count"),
        bind("F_k", "normalized cost", "An upper bound on time divided by logical volume for interchanging two chunks of $m^k$ digits.", "direct"),
    ],
)

S1 = show(
    "S1",
    r"Two disjoint contiguous address chunks of $u$ bits in an arbitrary bit array on $[P]\times[2^u]\times[G]\times[2^u]\times[B]$ can be interchanged, $(p,h,g,d,z)\mapsto(p,d,g,h,z)$, in $O(Vu^\tau)$ steps with a fixed $\tau<1$, where $V=PGB\,2^{2u}$.",
    r"Prove the bound for chunks of $e=m^k$ radix-$q$ digits with a row field divisible by $W^k$ through the bit network, then manufacture that row field from a few high digits, split the remaining width in base $m$, and pad binary chunks to radix $q$.",
    mot("The network recursion needs a row field long enough to be split $k$ times into $W$ role streams; borrowing $O(\\log e)$ high digits of the chunks supplies it at a cost below the target bound.",
        "explicit",
        r"Rows for a general array can be supplied by a few of its own high digits.¶Their movement will cost less than the final bound."),
    [
        S11,
        infer("S1.2",
              r"For $e$-digit chunks with $k=\lceil\log_me\rceil$, exchanging and joining the top $\rho=O(\log e)$ digits of both chunks creates a row field of range $q^{2\rho}\ge W^k$ in front of the remaining chunks at cost $O(V\rho)$, and zero rows pad its count to a multiple of $W^k$ at most doubling the volume.",
              r"In the two middle orders, the first two fields form a row field of range"),
        infer("S1.3",
              r"Writing $e-\rho=\sum_ja_jm^j$ with $0\le a_j<m$ and interchanging corresponding pieces of width $m^j$ costs $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$, a geometric sum because $a_j<m$ and $m^k<me$.",
              r"The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a¶geometric sum of the stated order."),
        infer("S1.4",
              r"Binary chunks of $u$ bits are padded numerically to $[q^e]$ with $e=O(u)$, which enlarges the volume by a fixed factor, so the interchange costs $O(Vu^\tau)$.",
              r"Since $e=O(u)$ for fixed $q$, the bound is¶$O(Vu^\tau)$."),
    ],
    page="address-chunk-interchange",
    frm=["rank-saving-recurrence", "tape-address-model", "elementary-stream-ops", "permutations-and-cartesian-products", "big-o"],
    salient="The result is an exact permutation of the data, yet it is computed through XOR combinations of intermediate data and costs fewer scans than moving the $u$ address bits one at a time.",
)

# ---------------------------------------------------------------- S2 butterfly layer
S21 = show(
    "S2.1",
    r"With phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{\operatorname{wt}(P_Ux)\bmod 4})H^{\otimes m}$ on the binary labels, each edge's frame change is a product of one kernel $aI+bX_v$ or its inverse per vector $v$ of an orthonormal basis of the edge residual; hence on $e=mf$ selected axes the complex network yields $C^{\otimes e}$ on every role from $s_{\rm c}<W_{\rm c}m$ forward child calls on $f$ axes, and $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$.",
    r"Use additivity of Hamming weight modulo four on orthogonal vectors to factor frame changes into translation kernels, move those directions to coordinate slots with a binary change of basis $\mathcal P_M$, and fix endpoint signs with $C=iZC^{-1}Z$.",
    mot("The two-point kernel plays the role the address shear plays for bits: frame changes become products of $C$ on fewer selected axes, so the same rank-saving recursion applies to butterflies.",
        "explicit",
        r"Its phase¶frames express a $C$ tensor product using smaller groups of¶selected bits, separated by binary changes of basis."),
    [
        infer("S2.1.1",
              r"For binary $z,w$ with $z\cdot w=0$ the supports meet in an even number of points, so $\operatorname{wt}(z+w)\equiv\operatorname{wt}(z)+\operatorname{wt}(w)\pmod4$; for $V=U\perp E$ this gives $q_V-q_U=\sum_{v}\operatorname{wt}(v)[v\cdot x]$ over an orthonormal basis of $E$, and each odd-weight $v$ contributes the kernel $aI+bX_v$ or its inverse.",
              r"If $z\cdot w=0$, the intersection cardinality is even, so weight is¶additive modulo four.",
              frm=["finite-field-f2-arithmetic"], deferred=True),
        infer("S2.1.2",
              r"The number of residual basis vectors over the whole complex network is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$, short of $W_{\rm c}m$ by $2N-2L_{\rm c}>0$ since $L_{\rm c}/N=101/539<1/2$.",
              r"The deficit is $2N-2L_{\rm c}>0$.",
              deferred=True),
        infer("S2.1.3",
              r"Conjugating by the address permutation $\mathcal P_M$ whose first columns are the residual basis turns the edge change into coordinate kernels, and $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$, so each basis vector costs exactly one forward child $C^{\otimes f}$ on the $f$ axes of one slot.",
              r"A negative directional kernel still requires only one¶forward child, because"),
        infer("S2.1.4",
              r"$\mathcal P_M$ is a product of at most $m(m-1)+3m$ elementary row additions over $\mathbb F_2$, each of which XORs corresponding selected bits of two whole slots.",
              r"Thus one row addition changes corresponding selected¶positions in two whole slots."),
        infer("S2.1.5",
              r"Summing residual dimensions gives exactly $s_{\rm c}$ child calls on $f=e/m$ axes, and the endpoint $Z$ signs, the scalar $i^{27f}$ and negation of the physical $X$ outputs make every role, scratch roles included, receive $C^{\otimes e}$.",
              r"Summing its residual dimensions gives exactly¶$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
        infer("S2.1.6",
              r"Since $H_0=b\mathsf SC\mathsf S$, $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ with $b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod 2}$, so converting to normalized butterflies costs only a binary shift and fourth-root phases.",
              r"so it is a binary shift and fourth-root phase, with at most one further¶factor $b$."),
    ],
    page="phase-frame-kernel",
    frm=["common-frame-principle", "subset-intersection-labels", "linear-network", "rank-saving-recurrence", "butterfly", "linear-algebra-basics", "finite-field-f2-arithmetic", "complex-numbers"],
    adds=[bind("C", "two-point kernel", "The $2\\times2$ matrix $aI+bX$ with $a=(1+i)/2$ and $b=(1-i)/2$, from which the butterfly layer is assembled.", "direct")],
)

S22 = show(
    "S2.2",
    r"On a rectangle with three $L=fK$-bit address chunks $x,y,z$ and $R$-bit records, the XORs $y_{j_i}\gets y_{j_i}\oplus x_{j_i}$ at the $f$ positions $j_i=\rho+iK$ can be done together, restoring $z$ for every initial value, in $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$ time with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, which is $O(V(L^\tau+1))$ for the layer's parameters.",
    r"Realize the XOR by eight parity-controlled $\pm1$ updates applied to all $K$-bit segments at once as single cyclic shifts of whole chunks, then repair deterministically the few addresses whose guard values let a segment carry into the next.",
    mot("A chunk-wide cyclic shift updates all $f$ segments in one linear pass; carries between segments can occur only at a fraction $O(f2^{-K})$ of addresses, small enough to fix by sorting just those records.",
        "explicit",
        r"Also $K/\log p\to\infty$, which will¶make the exceptional set in a packed change of address bits small enough¶to repair by sorting."),
    [
        infer("S2.2.1",
              r"With a Boolean control $c$, the eight updates induce the cycle $(00\ 01\ 10)$ and then $(01\ 10\ 11)$ on the parities of $(u,w)$, so the result is $(u+c(1-2(u\bmod2)),w)$: the parity of $u$ flips exactly when $c=1$, both quotients by two are kept, the auxiliary $w$ is restored, and no coordinate ever moves by more than four.",
              r"Thus the parity of $u$¶is flipped precisely when $c=1$, both quotients under division by two are¶preserved, and the arbitrary auxiliary integer $w$ is restored."),
        infer("S2.2.2",
              r"Applied to all segments $[j_i,j_i+K)$, $i<f-1$, at once, each update is the single cyclic shift $y\gets y+\varepsilon\sum_i2^{j_i}[x_{j_i}=1][z_{j_i}=b]\pmod{2^L}$ (or the same with $y,z$ exchanged), whose offset never depends on its target, so it is a bijection done by chunk swaps and one controlled shift.",
              r"The shift offset never depends on its target chunk, so each line is a¶bijection of the rectangle."),
        infer("S2.2.3",
              r"Outside the set $\mathcal B$ of addresses where some guard value $g$ fails $10\le g\le2^{K-1}-11$, no segment carries into or borrows from the next, so the composed shifts $S_0$ agree with the ideal map $T_0$; the addresses in $\mathcal B$ are the only exceptions.",
              r"no segment carries into or borrows¶from the next segment."),
        infer("S2.2.4",
              r"Each guard excludes twenty of its $2^{K-1}$ values and the full $y,z$ ranges give every spectator the same guard distribution, so the union bound over $2(f-1)$ guards gives $|\mathcal B|\le\delta_{\rm bad}M$ independently of the records.",
              r"Indeed, the complete $y,z$ ranges give the same guard distribution at¶each choice of spectator coordinates."),
        infer("S2.2.5",
              r"Both $S_0$ and $T_0$ are bijections that agree off $\mathcal B$, and $T_0$ preserves $\mathcal B$, so the correction $T_0S_0^{-1}$ only permutes $\mathcal B$; its records are extracted with destination ranks, radix-sorted and reinserted.",
              r"Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$.",
              frm=["sorting-and-data-movement-on-tapes"]),
        infer("S2.2.6",
              r"The omitted top position $j_{f-1}$ is done by one two-bit XOR in $O(V)$; when $f=1$ this is the whole procedure.",
              r"This costs $O(V)$ and supplies the omitted selected position."),
        infer("S2.2.7",
              r"After division by $V$ the extra terms are $A_{\rm rect}^3/R\to0$ and $O(p^22^{-K}(1+A_{\rm rect}/R))=o(1)$ when $R$ exceeds every polynomial in $p$ and $K/\log p\to\infty$.",
              r"Under the stated family bounds¶the first tends to zero, and the second is¶$O(p^2 2^{-K}(1+A_{\rm rect}/R))=o(1)$."),
    ],
    page="packed-selected-bit-addition",
    frm=["controlled-shift", "address-chunk-interchange", "elementary-stream-ops", "binary-representation-and-bit-operations", "modular-arithmetic"],
    salient="The time bound is worst-case and deterministic although the cheap shifts are wrong on some addresses: the exceptional set depends only on addresses, never on the data.",
)

S24 = show(
    "S2.4",
    r"Dealing rows to the $W=W_{\rm c}$ roles, the time per volume of $C^{\otimes e}$ obeys $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ with leaves $F(e)=O(e)$ for $e<d^{1/2}$, and summing over the base-$m$ pieces of the selected chunks gives $O(d^{\lambda'})$ for the whole layer.",
    r"Take the row index from the first $q_0=O(\log d)$ chunks after applying their kernels individually, pad rows to a multiple of $W^{k_0}$, recurse on slots, and unroll the recurrence over a base-$m$ partition of the remaining chunks.",
    mot("Each child call then acts on a stream of volume $V/W$, which turns the $s$ child calls into the factor $s/W<m^\\sigma$.",
        "explicit",
        r"Splitting complete rows among¶the network's wire roles then reduces the volume of each recursive¶call."),
    [
        infer("S2.4.1",
              r"Individual $C$ kernels on the selected bits of the first $q_0=\lceil\log_2W\rceil\lceil\log_m(2d)\rceil$ chunks cost $O(V\log d)$, and the bits of those chunks form a row index of range $2^{q_0K}\ge W^{k_0}$; if $D\le q_0$ all kernels are applied individually.",
              r"regard their concatenated bits as one row index."),
        infer("S2.4.2",
              r"Each child acts on one role stream of exactly $1/W$ of the parent's volume and the node overhead is $O(V((eK)^\tau+1))$, so $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$.",
              r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),",
              frm=["recurrences-and-induction"]),
        infer("S2.4.3",
              r"With $K\le e^{c/\beta}$ at internal nodes and $s/W\le m^\sigma<m^\lambda$, internal costs sum to $O(e^\lambda)$ and leaves to $O(e^\sigma d^{\beta(1-\sigma)})$, so the $O(\log d)$ base-$m$ pieces cost $O(d^{\lambda'})$ for any $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$.",
              r"Adding their costs and the row preprocessing gives",
              frm=["big-o"]),
    ],
    frm=["elementary-stream-ops", "recurrences-and-induction", "big-o"],
)

S2 = show(
    "S2",
    r"On an array $[P]\times[2^K]^D\times[S]$ with $D\le d$ whose records are polynomials with $r$ complex disk-grid coefficients, applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ to the bit at a common offset of each of the $D$ chunks and truncating once returns $Q_p(\mathcal Hz)$, with error less than $\sqrt2\,2^{-p}$, in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$.",
    r"Write $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, compute $C^{\otimes e}$ recursively with the complex phase network on row streams whose binary changes of basis are packed selected-bit additions, unroll the recurrence, and reserve guard bits so that the whole layer is exact before one truncation.",
    mot("Applying the $D$ butterflies axis by axis costs $D$ full passes, which over all transform rounds would restore the $n\\log n$ cost; a simultaneous layer in $O(Vd^{\\lambda'})$ saves a power of $d$.",
        "explicit",
        r"We will obtain cost $O(Vd^{\lambda'})$, with¶$\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly¶factors would require $D$ whole-array passes."),
    [
        S21,
        S22,
        infer("S2.3",
              r"A fixed binary change of basis on $e=mf$ axes is a fixed number of row additions, each one packed selected-bit addition with two slots as $x,y$ and a third slot as $z$, so it and its inverse cost $O(V((eK)^\tau+1))$.",
              r"the complete change of basis and its inverse therefore cost¶$O(V((eK)^\tau+1))$ on a stream of volume $V$."),
        S24,
        infer("S2.5",
              r"Every arithmetic chain in one layer has depth at most $C_0d^{C_1}$ with $C_1=20$, and a value at depth $j$ lies in $2^{-(p+j)}\mathbb Z[i]$ with modulus at most $2^j$, so $p+\Delta$ fractional and $\Delta+3$ integer bits with $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$ hold every intermediate value exactly.",
              r"Thus reserving \(p+\Delta\)¶fractional bits and \(\Delta+3\) integer and sign bits per real¶component represents every intermediate coefficient exactly and¶prevents overflow.",
              frm=["fixed-point-truncation"]),
        infer("S2.6",
              r"Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays, and the single truncation $Q_p$ keeps the disk and changes each component by less than $2^{-p}$, an error below $\sqrt2\,2^{-p}$.",
              r"Finally, every row of $\mathcal H$ has¶absolute row sum one.",
              frm=["fixed-point-truncation"]),
    ],
    page="fast-butterfly-layer",
    frm=["phase-frame-kernel", "packed-selected-bit-addition", "rank-saving-recurrence", "address-chunk-interchange", "fixed-point-truncation", "polynomial-ring-mod", "butterfly", "tape-address-model"],
    salient="$D$ butterfly factors on different axes together cost fewer than $D$ scans of the array, $O(d^{\\lambda'})$ with $\\lambda'<1$, yet the result is exact up to a single final truncation.",
)

# ---------------------------------------------------------------- S3 ring convolution
S31 = show(
    "S3.1",
    r"For a power of two $t\mid 2r$ and $\omega_t=y^{2r/t}$, the normalized transforms $F_t^\mp$ on $\mathcal R_r^t$ are contractions with $F_t^+F_t^-=I/t$; radix-two decimation-in-frequency rounds compute $B_tF_t^-$ with outputs in bit-reversed order, the reversed rounds compute $F_t^+B_t^{-1}$ from that order, and on several axes each round is a parallel butterfly $\mathcal H$ followed by a recordwise monomial $J_E$.",
    r"Prove character cancellation directly (the ring has zero divisors), follow the decimation-in-frequency recursion to see where each branch bit is written, and group the axis steps of one round.",
    mot("The opposite transform must consume the forward output after a pointwise product, so the order in which the forward rounds store frequencies has to be tracked exactly rather than undone by a permutation.",
        "explicit",
        r"We also specify where each frequency entry¶is stored, because the opposite transform consumes that same order¶after a pointwise product."),
    [
        infer("S3.1.1",
              r"If $t\nmid j$, shifting $k$ by $t/2^{v+1}$ multiplies $\sum_k\omega_t^{jk}$ by $y^{rj_0}=-1$, so the sum vanishes because $\mathcal R_r$ has no two-torsion; hence $F_t^+F_t^-=t^{-1}I$.",
              r"Hence the sum is zero, since the additive group of¶$\mathcal R_r$ has no two-torsion."),
        infer("S3.1.2",
              r"Pairing $z_k$ with $z_{k+t/2}$, applying $H_0$ and multiplying the second output by $\omega_t^{-k}$ computes $F_t^-$ recursively, and after $\log_2t$ rounds the entry $(F_t^-z)_j$ sits at slot $\operatorname{rev}(j)$.",
              r"the¶entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$."),
        infer("S3.1.3",
              r"Since $H_0^2=I/2$, each reversed level is half the inverse of its forward level, so the reverse procedure composed with $B_tF_t^-$ is $I/t$, and it therefore equals $F_t^+B_t^{-1}$.",
              r"The forward procedure¶is invertible, so these two reverse operators agree."),
        infer("S3.1.4",
              r"A twiddle on one axis commutes with butterflies on the other axes, so a round on several axes is a parallel butterfly $\mathcal H$ followed by multiplication of each record by $y^E$ with an address-dependent exponent $E$, an isometry.",
              r"Consequently the individual axis steps may be grouped as a parallel¶butterfly $\mathcal H$, followed by one recordwise monomial operation¶$J_E$."),
    ],
    page="synthetic-transform",
    frm=["polynomial-ring-mod", "dft", "multidimensional-dft", "butterfly", "roots-of-unity", "fixed-point-truncation", "fast-fourier-transform-and-divide-and-conquer"],
    salient="No bit-reversal permutation is ever executed: the forward procedure leaves its output in bit-reversed order and the opposite procedure consumes exactly that order.",
)

S32 = show(
    "S3.2",
    r"On $d-1$ axes of lengths $t_i\in\{r/2,r\}$, the forward and opposite synthetic procedures, with exact counterparts $LBF_{\boldsymbol t}^-$ and $F_{\boldsymbol t}^+B^{-1}L^{-1}$ for a layout permutation $L$, have error less than $\sqrt2\ell\,2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.",
    r"Move a few bit slots to a prefix and interleave the remaining $K$-bit chunks by chunk interchanges so that each round's selected bits sit at one offset in consecutive chunks, then call the simultaneous layer once per round.",
    mot("The simultaneous layer applies only when the selected bits of all participating axes occupy a common offset in consecutive $K$-bit chunks, so the transform must first be laid out that way.",
        "explicit",
        r"To apply Proposition~\ref{prop:simultaneous-layer} in a transform round,¶we must place the selected bits of the participating axes at a common¶offset in consecutive $K$-bit chunks."),
    [
        infer("S3.2.1",
              r"Moving at most $O(dK)$ slots to a prefix costs $O(TpdK)$, and reordering the remaining chunks takes at most $Dq-1$ interchanges of width-$K$ chunks with $Dq=O(p/K)$, costing $O(Tp\,pK^{\tau-1})$.",
              r"This uses at most $Dq-1$¶exchanges of width-$K$ address chunks, even when the chunks are¶nonadjacent."),
        infer("S3.2.2",
              r"Each of the at most $\ell$ rounds on the chunks sees the complete address set $[P]\times[2^K]^D\times[S]$ and is one simultaneous-layer call of cost $O(Tpd^{\lambda'})$.",
              r"The simultaneous-layer procedure therefore applies at cost¶$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total."),
        infer("S3.2.3",
              r"Twiddles $y^E$ are split-and-merge signed copies, and truncation toward zero commutes with signed coefficient permutations, $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$, so each round is one truncated contraction and $\ell$ rounds err by less than $\sqrt2\ell\,2^{-p}$.",
              r"Starting with¶zero error, at most $\ell$ rounds therefore¶give the claimed error and disk bounds.",
              frm=["fixed-point-truncation"]),
    ],
    frm=["fast-butterfly-layer", "address-chunk-interchange", "elementary-stream-ops", "synthetic-transform"],
)

S33 = show(
    "S3.3",
    r"For disk-grid $f,g\in\mathcal R_r$ the exact Gaussian-integer numerators of $fg$, and then $Q_p(fg/r)$ (in the disk, error below $\sqrt2\,2^{-p}$), are computed in $O(rp\log(rp))$ time from four products of $4pr$-bit integers by the established multiplier.",
    r"Evaluate the numerator polynomials at $B_0=2^{4p}$ with signed carries, multiply the evaluations, read the coefficients back as centered residues with a carry in $\{0,1\}$, reduce modulo $y^r+1$, and truncate.",
    mot("Kronecker substitution turns each polynomial product into one integer product, which the established $O(N\\log N)$ multiplier handles, and the field width $4p$ is chosen so that adjacent coefficients can never overlap.",
        "recoverable"),
    [
        infer("S3.3.1",
              r"Writing $f=2^{-p}(a+ib)$, $g=2^{-p}(c+ie)$, each evaluation $A_u=u(B_0)$ satisfies $|A_u|<B_0^r/2$, so it fits in $r$ blocks of $4p$ bits, produced with carries in $\{-1,0\}$.",
              r"shows that each magnitude fits in $4pr$ bits."),
        infer("S3.3.2",
              r"Every coefficient of the ordinary products obeys $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, because $r<2^p$.",
              r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
        infer("S3.3.3",
              r"Reading the product block by block with a carry $\rho_j\in\{0,1\}$, the centered residue of $q_j+\rho_j$ modulo $B_0$ is $h_j$ by the separation bound, and the final carry cancels the sign extension.",
              r"Thus $\widehat h_j=h_j$."),
        infer("S3.3.4",
              r"Reducing $ac-be$ and $ae+bc$ modulo $y^r+1$ makes each coefficient a sum of exactly $r$ signed products, so $\|fg/r\|_\infty\le\|f\|_\infty\|g\|_\infty$ and the normalized product of disk polynomials stays in the disk.",
              r"The same triangle inequality before imposing the disk bound gives¶$\|fg/r\|_\infty\leq\|f\|_\infty\|g\|_\infty$; in particular the¶normalized product of disk polynomials lies in the disk."),
        infer("S3.3.5",
              r"The four exact integer products on $O(rp)$ bits dominate the linear packing, extraction, wrapping and truncation scans, giving $O(rp\log(rp))$.",
              r"Four exact integer products dominate the linear¶packing, extraction, combination, wrapping, and truncation costs."),
    ],
    page="signed-packing",
    frm=["polynomial-ring-mod", "established-multiplier", "fixed-point-truncation", "binary-representation-and-bit-operations", "modular-arithmetic"],
)

S3 = show(
    "S3",
    r"For disk-grid arrays $f,g$ on $\prod_{i<d}\mathbb Z/t_i$ with entries in $\mathcal R_r=\mathbb C[y]/(y^r+1)$, the normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ is approximated with error less than $\sqrt2\,M(3\ell+1)2^{-p}$, where $M=T/r$, in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.",
    r"Apply two forward synthetic transforms keeping their stored order, multiply corresponding polynomial records by signed packing and divide by $r$, apply the opposite transform to that order, and scale exactly by $M$.",
    mot("In $\\mathcal R_r$ the roots of unity the transforms need are powers of $y$, so twiddle multiplications are exact signed coefficient shifts and the transforms reduce to address moves, shifts and butterflies, which the two tape procedures accelerate.",
        "explicit",
        r"Powers of $y$ then¶serve as roots of unity in the remaining axes, and multiplication by¶such a root is a signed shift of the coefficient list."),
    [
        S31,
        S32,
        S33,
        infer("S3.4",
              r"From $F_{\boldsymbol t}^-(f*g)=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)$ and $F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$, the exact pipeline gives $(f*g)/T$, and the stored order is harmless because a record permutation commutes with the pointwise product: $P(LBu,LBv)=LBP(u,v)$.",
              r"Since $LB$ permutes records and leaves their polynomial suffixes¶intact, $P(LBu,LBv)=LBP(u,v)$.",
              frm=["cyclic-convolution", "dft"]),
        infer("S3.5",
              r"Two forward errors below $\sqrt2\ell\,2^{-p}$ add through the bilinear product, the product truncation adds below $\sqrt2\,2^{-p}$, the opposite transform is a contraction adding its own error, and the exact scale by $M$ gives error below $\sqrt2\,M(3\ell+1)2^{-p}$.",
              r"The final exact multiplication by $M$ therefore gives error less than¶$M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed.",
              frm=["norms-absolute-values-and-error-bounds"]),
    ],
    page="ring-convolution",
    frm=["synthetic-transform", "signed-packing", "fast-butterfly-layer", "address-chunk-interchange", "cyclic-convolution", "multidimensional-dft", "polynomial-ring-mod", "fixed-point-truncation"],
)

# ---------------------------------------------------------------- S4 resampling
S41 = show(
    "S4.1",
    r"For coprime $s<t<2^p$ with $\theta=t/s-1>p/\alpha^4$ and $2\le\alpha<\sqrt p$, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ with contractions $A,B_0$ approximable to error below $p^2$ in $O(tp^{3/2+\delta}\alpha)$ time; over $d$ axes this gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$, linewise error below $dp^2$, line work $O(dTp^{3/2+\delta}\alpha)$ and axis movement $O(Tp\,d^2(1+\ell^\tau))$.",
    r"Use the Gaussian maps $\mathsf S,\mathsf T$ with $\mathsf TP_sF_s=P_tF_t\mathsf S$, invert $N=C\mathsf T\mathsf D$, which is close to the identity, by a Neumann series, normalize the factors into contractions, then apply the one-dimensional maps line by line, exposing each axis by chunk interchanges.",
    mot("The Chinese-remainder split needs pairwise coprime lengths, while cheap synthetic transforms need powers of two; Gaussian resampling expresses a transform of one length through a transform of the other.",
        "explicit",
        r"The transform lengths needed for the integer product are pairwise coprime,¶whereas the synthetic transforms use powers of two. Gaussian resampling¶connects these two shapes."),
    [
        infer("S4.1.1",
              r"Since $\|N-I\|<2^{-\alpha^2\theta}$ and $\alpha^2\theta>p/\alpha^2>1$, $\|N-I\|<1/2$ and $N$ is invertible by the Neumann series.",
              r"Thus $\|N-I\|<1/2$, so $N$ is invertible¶by the Neumann series."),
        infer("S4.1.2",
              r"Applying the left inverse $\mathsf DN^{-1}C$ of $\mathsf T$ and the normalizations $\mathsf S/2$, $N^{-1}/2$, $2^{-(2\alpha^2-2)}\mathsf D$ (of norms below $3/4$, $7/8$, $1$) gives $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$.",
              r"Applying this left inverse to the first identity in¶\eqref{eq:gaussian-public-facts} gives"),
        infer("S4.1.3",
              r"The cited algorithms approximate the normalized Gaussian maps and $C$ is an exact ordered selection, so $\widetilde A$ and $\widetilde B_0$ err by less than $16p<p^2$ and $4+3p^2/4<p^2$.",
              r"Contraction of the exact maps yields errors less than $16p<p^2$ and¶$4+3p^2/4<p^2$, respectively.",
              frm=["norms-absolute-values-and-error-bounds"]),
        infer("S4.1.4",
              r"Unlike the original algorithm, which sorts to implement $P_t$ and $P_s^{-1}$ at cost $O(tp\log t)$ each, the two permutations stay in the identity and are never executed.",
              r"In \eqref{eq:no-sort-one-dimensional} these permutations remain in the¶transform identity."),
        infer("S4.1.5",
              r"Tensoring gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$; applied axis by axis inside the padded box of $T$ entries, each axis map is a contraction with error below $p^2$, so the composite errs by less than $dp^2$.",
              r"Composing the $d$ axis maps gives error less than $dp^2$."),
        infer("S4.1.6",
              r"Exposing an axis takes $O(d)$ adjacent interchanges of $\ell$- or $(\ell-1)$-bit fields, each an equal-width chunk swap plus one bit move costing $O(Tp(1+\ell^\tau))$.",
              r"Each adjacent interchange therefore¶costs $O(Tp(1+\ell^\tau))$."),
    ],
    page="gaussian-resampling",
    frm=["dft", "multidimensional-dft", "fixed-point-truncation", "address-chunk-interchange", "established-multiplier", "complex-numbers", "norms-absolute-values-and-error-bounds", "primes-coprimality-and-gcd"],
    adds=[bind("\\alpha", "Gaussian width", "The integer width parameter of the Gaussian kernels, of order $p^{1/4+\\epsilon/2}$.", "direct")],
)

S42 = show(
    "S4.2",
    r"For even $t_i$ and the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$, which has period $t_i$ in coordinate $i$, $QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$.",
    r"Check the periodicity of $a$, then compare the coefficient of each $u_{\boldsymbol k}$ on both sides.",
    mot("The chirp identity carries out the frequency change of $Q$ inside a convolution, so $Q$ is never applied as a separate permutation of the array.",
        "explicit",
        r"The chirp identity below performs the frequency change¶in $Q$ without applying $Q$ as a separate permutation of the array."),
    [
        infer("S4.2.1",
              r"Replacing $j_i$ by $j_i+t_i$ changes the exponent of $a$ by $-\pi is_i(2j_i+t_i)$, a multiple of $2\pi i$ because $t_i$ is even.",
              r"Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by¶$-\pi i s_i(2j_i+t_i)$, an integral multiple of $2\pi i$."),
        infer("S4.2.2",
              r"The coefficient of $u_{\boldsymbol k}$ on the right is $T^{-1}\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}=T^{-1}\exp(2\pi i\sum_is_ij_ik_i/t_i)$, which is the coefficient of $QF_{\boldsymbol t}$ because $Q$ reads frequency $(-s_ij_i)_i$.",
              r"This is precisely the coefficient in $QF_{\boldsymbol t}$, because¶$Q$ reads frequency $(-s_i j_i)_i$ from the negative-sign transform."),
    ],
    page="bluestein-chirp",
    frm=["dft", "cyclic-convolution", "multidimensional-dft", "complex-numbers", "roots-of-unity"],
)

S43 = show(
    "S4.3",
    r"With $S=\prod_is_i$, $RF_{\boldsymbol s}^+[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$.",
    r"Pass the dilation $R$ through the opposite transform and the pointwise product, then apply the normalized convolution theorem.",
    mot("The source permutation is a dilation by units modulo the $s_i$, and a dilation passes through a Fourier transform as the inverse dilation, so its two occurrences cancel.",
        "recoverable"),
    [
        infer("S4.3.1",
              r"For a unit $c$ modulo $q$, substituting $h=ck$ gives $F_q^+R_c=R_c^{-1}F_q^+$; each $t_i$ is a unit modulo $s_i$, so $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.",
              r"Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives",
              frm=["modular-arithmetic"]),
        infer("S4.3.2",
              r"A coordinate permutation commutes with pointwise products, so $(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)=R(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)$.",
              r"because a coordinate permutation commutes with pointwise products."),
        infer("S4.3.3",
              r"By $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$ and $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$, $F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=(u*v)/S^2$.",
              r"proving \eqref{eq:source-permutation-cancel}.",
              frm=["cyclic-convolution", "dft"]),
    ],
    frm=["dft", "cyclic-convolution", "modular-arithmetic"],
    salient="The permutation $R$ drops out exactly, so the convolution comes out in the original coordinates although $R$ is never computed.",
)

S4 = show(
    "S4",
    r"The source transform on the prime axes satisfies $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with contractions $\mathcal A,\mathcal B_0$ and a power-of-two transform $F_{\boldsymbol t}$; the middle factor $QF_{\boldsymbol t}$, permutation included, is a chirp-weighted normalized convolution, and the unexecuted source permutation $R$ cancels: $RF_{\boldsymbol s}^+[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$.",
    r"Keep the two coordinate permutations of Gaussian resampling inside the transform identity, absorb the target permutation $Q$ into Bluestein's chirp, and cancel the source permutation $R$ through the convolution theorem.",
    mot("Executing the two permutations as label-and-sort operations would cost $O(tp\\log t)$ per line, a full logarithmic factor; left in the identity they cost nothing, since $Q$ is absorbed by the chirp and $R$ cancels.",
        "recoverable"),
    [
        S41,
        S42,
        S43,
        infer("S4.4",
              r"Conjugating the input and output of an algorithm for $RF_{\boldsymbol s}$ gives one for $RF_{\boldsymbol s}^+$ with the same error, since conjugation flips the Fourier sign, commutes with the real permutation $R$ and preserves the disk grid.",
              r"Finally, conjugation¶changes the negative Fourier sign to the positive one and commutes with¶the real permutation $R$.",
              frm=["complex-numbers"]),
    ],
    page="permutation-cancellation",
    frm=["gaussian-resampling", "bluestein-chirp", "dft", "multidimensional-dft", "cyclic-convolution", "modular-arithmetic", "primes-coprimality-and-gcd"],
    salient="Neither coordinate permutation of Gaussian resampling is ever performed, yet the computed convolution is exactly the one wanted.",
    adds=[
        bind("R", "source permutation", "The coordinate permutation $\\bigotimes_iP_{s_i}$, reading coordinate $t_ij_i$, that Gaussian resampling leaves on the prime-length transform.", "direct"),
        bind("Q", "target permutation", "The coordinate permutation $\\bigotimes_iP_{t_i}$, reading frequency $-s_ik_i$, that Gaussian resampling leaves on the power-of-two transform.", "direct"),
    ],
)

# ---------------------------------------------------------------- S5 algorithm
S51 = show(
    "S5.1",
    r"With $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, $T$ the power of two in $[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$, axis lengths $t_i\in\{r/2,r\}$ with $\prod_it_i=T$, $\alpha=\lceil(12d^2b)^{1/4}\rceil$ and distinct primes $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ with $\eta=1/(4d)$, one has $Tp=\Theta(n)$, $T/2<S<T$ and every hypothesis of the layer, transform and resampling interfaces for all large $n$, and the machine finds these parameters in $o(n)$ time.",
    r"Fix conservative rational exponents, derive the size relations from $n$, obtain the primes from an explicit prime-interval bound, and check each interface's inequalities.",
    mot("The primes must be close to the powers of two in two directions at once: their product must fill a fixed fraction of the padded box, while each ratio $t_i/s_i$ must stay far enough above one for the resampling estimate.",
        "explicit",
        r"their product must occupy a fixed fraction of the padded box,¶while each ratio $t_i/s_i$ must leave enough separation for resampling."),
    [
        infer("S5.1.1",
              r"The fixed rationals $\tau=\sigma=1-2^{-50}$, $\lambda=1-2^{-52}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $\epsilon=2^{-75}$, $\delta=1/16$ and $C_1=20$ satisfy all the layer conditions and $\epsilon C_1<1$.",
              r"The layer conditions hold with room to spare:"),
        infer("S5.1.2",
              r"These choices give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$, so $r$ exceeds every fixed power of $p$ and $K/\log p\to\infty$.",
              r"These bounds also give that $r$ exceeds every fixed power of $p$,¶$K/\log p\to\infty$, and",
              frm=["logarithms-and-iterated-logarithm-notation"]),
        infer("S5.1.3",
              r"For $x\in\{r/2,r\}$ the interval $((1-2\eta)x,(1-\eta)x]$ holds at least $\eta x/(2\log x)>d$ primes and the two intervals are disjoint, so distinct odd primes $s_i$, coprime to the $t_i$, exist.",
              r"We may therefore choose distinct odd primes satisfying",
              frm=["primes-coprimality-and-gcd"]),
        infer("S5.1.4",
              r"Bernoulli's inequality gives $S/T>(1-1/(2d))^d>1/2$, so $T/2<S<T$, and $\theta_i>\eta$ gives $\alpha^4\theta_i>3db\ge p$.",
              r"Together with $s_i<t_i$, this gives $T/2<S<T$."),
        infer("S5.1.5",
              r"Trial-division search costs $O(dr^{3/2}\operatorname{poly}(p))$, whose logarithm is $o(p)=o(\log n)$, so it takes $n^{o(1)}$ time.",
              r"the search takes¶$n^{o(1)}=o(n)$ time."),
    ],
    page="parameter-choice",
    frm=["gaussian-resampling", "crt-address-map", "fast-butterfly-layer", "synthetic-transform", "polynomial-ring-mod", "primes-coprimality-and-gcd", "logarithms-and-iterated-logarithm-notation", "floor-ceiling-and-summation-notation"],
)

S52 = show(
    "S5.2",
    r"Writing each input as a polynomial in $2^b$ with $q=\lceil n/b\rceil$ digits, the product polynomial has degree $2q-2<S$, so its convolution modulo $x^S-1$ has no wraparound, and its coefficients satisfy $0\le c_j<2^{3b}$.",
    r"Bound the degree by $2n/b\le T/2<S$ and each coefficient by $q(2^b-1)^2$.",
    mot("Padding the digit lists to length $S$ makes the cyclic convolution equal the ordinary product, and the coefficient bound fixes how large the integers to be recovered are.",
        "recoverable"),
    [
        infer("S5.2.1",
              r"$2q-2<2n/b\le T/2<S$, so the cyclic convolution modulo $x^S-1$ has no nonzero wraparound.",
              r"Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
        infer("S5.2.2",
              r"Each coefficient is a sum of at most $q$ products of digits below $2^b$, and $q\le n\le2^b$, so $0\le c_j\le q(2^b-1)^2<2^{3b}$.",
              r"since $q\le n\le2^b$."),
    ],
    page="radix-digit-convolution",
    frm=["polynomials", "cyclic-convolution", "binary-representation-and-bit-operations"],
)

S53 = show(
    "S5.3",
    r"For pairwise coprime $s_i$ with $S=\prod_is_i$, $P_i=\prod_{j<i}s_j$ and $\mu_i=P_i^{-1}\bmod s_i$, the map $\Phi:x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism $\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$ that preserves cyclic convolution, and on tape it and its inverse, with padding, cost $O(Tp\,d^2(1+\ell^\tau))$.",
    r"Show that the image of $x$ has order $S$, express its coordinates as triangular functions of the mixed-radix digits of the index, and implement each triangular update as a prefix-controlled cyclic shift after reordering the axes by chunk interchanges.",
    mot("Choosing the coordinate powers $\\mu_i$ makes the change of order triangular, so it is a sequence of controlled cyclic shifts rather than a general permutation.",
        "explicit",
        r"The following map uses that¶algebraic split, with coordinate powers that make the change of order a¶sequence of controlled cyclic shifts."),
    [
        infer("S5.3.1",
              r"The image of $x$ has order $S$ because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all $S$ basis monomials and $\Phi$ is an isomorphism.",
              r"Hence¶$\Phi$ is an isomorphism and preserves cyclic convolution.",
              frm=["chinese-remainder-theorem", "ring-and-group-notions-for-polynomials"]),
        infer("S5.3.2",
              r"For $k=\sum_ja_jP_j$ the axis-$i$ coordinate of $\Phi(x^k)$ is $a_i+\mu_i\sum_{j<i}a_jP_j\bmod s_i$, since terms with $j>i$ vanish modulo $s_i$ and $\mu_iP_i\equiv1$.",
              r"Indeed terms with $j>i$ are divisible by $s_i$, and $\mu_iP_i=1$ modulo¶$s_i$.",
              frm=["modular-arithmetic"]),
        infer("S5.3.3",
              r"With lower-index controls placed before each target, the updates for $i=d,\dots,1$ are prefix-controlled cyclic shifts of the valid interval $[0,s_i)$ that fix the padded addresses, so zero padding stays zero.",
              r"Each triangular update is a prefix-controlled cyclic shift."),
        infer("S5.3.4",
              r"Reversing the axes takes $O(d^2)$ adjacent moves, each an equal-width chunk swap plus a bit move, so $\Phi$ and $\Phi^{-1}$ cost $O(Tp\,d^2(1+\ell^\tau))$.",
              r"Therefore the map $\Phi$, its inverse, and¶their padding operations cost"),
    ],
    page="crt-address-map",
    frm=["cyclic-convolution", "chinese-remainder-theorem", "primes-coprimality-and-gcd", "controlled-shift", "address-chunk-interchange", "elementary-stream-ops", "ring-and-group-notions-for-polynomials", "modular-arithmetic"],
)

S54 = show(
    "S5.4",
    r"With $\zeta=e^{\pi i/r}$, $\Theta:x_d\mapsto\zeta y$ is an isomorphism $\mathbb C[x_d]/(x_d^r-1)\to\mathbb C[y]/(y^r+1)$ that multiplies coefficient $k$ by $\zeta^k$, and normalized complex cyclic convolution satisfies $D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$.",
    r"Check that $(\zeta y)^r=1$, that the map is diagonal with nonzero entries, and that the negacyclic sign cancels $\zeta^r$ in the wrap.",
    mot("The ring convolution wraps its last coordinate negacyclically while the chirp needs a cyclic convolution; multiplying coefficient $k$ by $\\zeta^k$ converts one wrap into the other exactly.",
        "recoverable"),
    [
        infer("S5.4.1",
              r"$\Theta$ is well defined because $(\zeta y)^r=(-1)(-1)=1$, and it is diagonal with nonzero entries $\zeta^k$, hence a norm-preserving isomorphism.",
              r"It is therefore an¶isomorphism, with inverse multiplying that coefficient by¶$\zeta^{-k}$."),
        infer("S5.4.2",
              r"For $k+l=j+hr$ a twisted product term acquires $\zeta^{k+l}(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
              r"Untwisting therefore recovers the cyclic coefficient with the correct¶sign.",
              frm=["roots-of-unity"]),
        infer("S5.4.3",
              r"Hence $\mathcal M_{\mathbb C}(f,g):=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$, and since $D_\pm$, $\iota^{\pm1}$ are isometries it is a bilinear contraction.",
              r"The maps $D_\pm$ and¶$\iota^{\pm1}$ are isometries, so $\mathcal M_{\mathbb C}$ is also a¶bilinear contraction."),
    ],
    page="phase-twist",
    frm=["polynomial-ring-mod", "cyclic-convolution", "roots-of-unity", "complex-numbers"],
)

S55 = show(
    "S5.5",
    r"The computed chirp transform $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,Q_p(\overline{\widetilde a}\cdot x)))$ has exact counterpart $QF_{\boldsymbol t}x$, the computed source transform $\widetilde{\mathscr F}$ (expand by $\widetilde{\mathcal A}$, chirp, compress by $\widetilde{\mathcal B}_0$, scale by $2^\gamma$) has exact counterpart $RF_{\boldsymbol s}$, and $\widetilde{\mathscr F}^+(z)=\overline{\widetilde{\mathscr F}(\overline z)}$ has exact counterpart $RF_{\boldsymbol s}^+$.",
    "Compose the computed maps and replace each by the exact map it approximates.",
    mot("Because $QF_{\\boldsymbol t}$ is a chirp-weighted convolution, the twisted ring convolution evaluates the whole middle factor, permutation included, and resampling around it yields the source transform.",
        "recoverable"),
    [
        infer("S5.5.1",
              r"Chirp phases are computed modulo $2r$ from $d$ terms $s_ij_i^2(r/t_i)$ at $O(dp^{1+\delta})$ per entry, $O(Tdp^{1+\delta})$ in total.",
              r"Thus chirp¶construction costs $O(Td p^{1+\delta})$ in total."),
        infer("S5.5.2",
              r"Replacing approximations by exact phases and the exact convolution gives $\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)=QF_{\boldsymbol t}x$.",
              r"Replacing the approximations¶by exact phases and exact convolution gives"),
        infer("S5.5.3",
              r"The source procedure's exact counterpart is $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.",
              r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A"),
        infer("S5.5.4",
              r"Conjugating input and output gives the opposite procedure, whose exact counterpart is $RF_{\boldsymbol s}^+$.",
              r"its exact counterpart is $RF_{\boldsymbol s}^{+}$ by¶Lemma~\ref{lem:chirp-permutation}."),
    ],
    frm=["bluestein-chirp", "gaussian-resampling", "permutation-cancellation", "phase-twist", "ring-convolution"],
)

S57 = show(
    "S5.7",
    r"The recovered array $2^{2b+4}S\widetilde w$ differs from the true integer coefficients by less than $1/2$, so rounding gives every $c_j$ exactly, and propagating radix-$2^b$ carries yields exactly the $2n$-bit product.",
    r"Propagate errors through contractions and bilinear contractions, where errors add when the operands lie in the disk, multiply by the known scales, and use that the true coefficients are integers.",
    mot("Every computed stage is a contraction or a bilinear contraction applied to disk-grid data, so errors only add; the final scale $2^{2b+4}S$ together with $2^\\gamma$ is far below $2^p=2^{6b}$, leaving room under $1/2$.",
        "recoverable"),
    [
        infer("S5.7.1",
              r"For a bilinear contraction, replacing the operands changes the output by at most $\|f'-f\|\|g'\|+\|f\|\|g'-g\|$, so when all operands lie in the disk the two errors add.",
              r"When all four operands are in the disk, their two errors therefore add.",
              frm=["norms-absolute-values-and-error-bounds"]),
        infer("S5.7.2",
              r"The source transform errs by less than $9\cdot2^\gamma T\log_2T$ grid units, and after the pointwise product, the opposite transform and the scale by $S$, $\widetilde w$ approximates $w=(u*v)/S$ within $28\cdot2^\gamma T^2\log_2T$ grid units of size $2^{-p}$.",
              r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
        infer("S5.7.3",
              r"Scaling by $2^{2b+4}S$ with $S\le T<2^b$, $\log_2T<b$ and $\gamma\le b/4$ gives a final error below $448b\,2^{-3b/4}<1/2$.",
              r"\le448b\,2^{-3b/4}<\frac12."),
        infer("S5.7.4",
              r"Since the true coefficients are integers, the nearest integer to each recovered value is the correct coefficient.",
              r"The strict error below $1/2$ makes the nearest integer to¶that value the unique correct coefficient."),
        infer("S5.7.5",
              r"Carries satisfy $0\le k_j<2^{2b}$ and the invariant $\sum_{h<j}c_h2^{bh}=\sum_{h<j}d_h2^{bh}+k_j2^{bj}$, so the digits are those of the product, which is below $2^{2n}$; exactly $2n$ bits are output.",
              r"The exact product is less¶than $2^{2n}$; all bits above position $2n-1$ are therefore zero.",
              frm=["floor-ceiling-and-summation-notation"]),
    ],
    page="exact-recovery",
    frm=["radix-digit-convolution", "fixed-point-truncation", "norms-absolute-values-and-error-bounds", "floor-ceiling-and-summation-notation"],
    salient="Although every transform is computed approximately in fixed point, the output is exact, with a working precision of only $p=6b$ bits.",
)

S5 = show(
    "S5",
    r"For all sufficiently large $n$, the pipeline of radix-$2^b$ digits, the map $\Phi$, two computed source transforms, a truncated pointwise product, the opposite transform, exact scalings by $S$ and $2^{2b+4}S$, rounding, $\Phi^{-1}$ and carry propagation outputs exactly $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$.",
    r"Fix parameters meeting every interface's hypotheses, turn the digit product into a cyclic convolution on distinct prime axes, compute each source transform by resampling around a twisted ring convolution, cancel the retained permutation, and show the accumulated error stays below $1/2$.",
    mot("Radix digits turn the product into a convolution of short coefficients, and Gaussian resampling turns the transforms for that convolution into power-of-two transforms, the only shape on which the cheap synthetic butterflies apply.",
        "explicit",
        r"it replaces the Fourier transforms needed for¶this convolution by multidimensional transforms whose axis lengths are¶powers of two."),
    [
        S51,
        S52,
        S53,
        S54,
        S55,
        infer("S5.6",
              r"Digits enter as $a_j2^{-b-2}$, so $u,v$ have norm below $1/4$; the exact counterpart after the three transforms is $(u*v)/S^2$, scaling by $S$ gives $w=(u*v)/S$, and scaling by $2^{2b+4}S$ gives $2^{2b+4}(u*v)$, whose preimage under $\Phi$ is the integer coefficient convolution.",
              r"The second scale gives¶$2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original¶integer coefficient convolution."),
        S57,
    ],
    page="multiplication-algorithm",
    frm=["radix-digit-convolution", "crt-address-map", "gaussian-resampling", "permutation-cancellation", "bluestein-chirp", "phase-twist", "ring-convolution", "exact-recovery", "parameter-choice", "cyclic-convolution", "dft"],
    adds=[
        bind("b", "digit width", "The number $\\lceil\\log_2n\\rceil$ of bits in each radix digit of the inputs.", "count"),
        bind("\\Phi", "CRT address map", "The algebra isomorphism sending one long cyclic convolution to a convolution on the distinct prime axes.", "direct"),
    ],
)

# ---------------------------------------------------------------- S6 time
S6 = show(
    "S6",
    r"Divided by $V=Tp=\Theta(n)$, every cost of the algorithm is $O(p^{1-2\kappa})$ up to fixed powers of $\log p$, and setup, prime search and exceptional streams cost $o(V)$, so the running time is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$, with schoolbook multiplication below a fixed cutoff.",
    r"Tabulate the normalized cost of each operation as a power of $p$, compute each power's margin below one, and absorb the remaining logarithmic factors into the spare $\kappa$.",
    mot("Each dominant cost is a power of $p$ at most $1-2\\kappa$, and the extra $\\kappa$ of slack absorbs every remaining fixed power of $\\log p$, so dividing by $V=Tp=\\Theta(n)$ gives the bound directly.",
        "explicit",
        r"This explicit slack will cover¶any remaining fixed power of $\log p$."),
    [
        infer("S6.1",
              r"The seven dominant normalized costs $dK$, $pK^{\tau-1}$, $\ell d^{\lambda'}$, $d^2(1+\ell^\tau)$, $dp^{1/2+\delta}\alpha$, $dp^\delta$ and $\log(rp)$ are powers of $p$ whose margins below one have minimum $\epsilon c(1-\tau)=2^{-181}=2\kappa$.",
              r"Thus $\min_i g_i=2^{-181}=2\kappa$."),
        infer("S6.2",
              r"The transform layout uses $O(p/K)$ exchanges of width-$K$ chunks because $d\ell=O(p)$, each costing $O(VK^\tau)$, so its normalized cost is $O(pK^{\tau-1})$, the row with the smallest margin.",
              r"Each exchange costs¶$O(VK^\tau)$ by Lemma~\ref{lem:chunk-swap}, so the normalized total is",
              frm=["address-chunk-interchange"]),
        infer("S6.3",
              r"The $T/r$ packed polynomial products of $O(rp)$ bits cost $O(Tp\log(rp))$ through the established multiplier on records of length $o(n)$, never through the improved algorithm.",
              r"they do not call the improved algorithm being constructed.",
              frm=["established-multiplier"]),
        infer("S6.4",
              r"Descriptor setup over at most $p^A$ recursion visits and sorting of the exceptional addresses cost $O(Vp^{A'}2^{-K})=o(V)$, because $r$ and $2^K$ exceed every fixed power of $p$.",
              r"=O(Vp^{A'}2^{-K})=o(V)"),
        infer("S6.5",
              r"Every displayed power is at most $1-2\kappa$ and every fixed power of $\log p$ is eventually at most $p^\kappa$, so the total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
              r"Any fixed power of $\log p$ is at most $p^\kappa$¶eventually.",
              frm=["logarithms-and-iterated-logarithm-notation"]),
        infer("S6.6",
              r"Below one fixed cutoff the machine uses schoolbook multiplication, and the finitely many short lengths only enlarge the constant.",
              r"Fix one cutoff beyond all the size, precision, margin and layout¶conditions, and use schoolbook multiplication below it."),
    ],
    page="time-accounting",
    frm=["multiplication-algorithm", "parameter-choice", "address-chunk-interchange", "fast-butterfly-layer", "ring-convolution", "synthetic-transform", "gaussian-resampling", "crt-address-map", "established-multiplier", "big-o", "logarithms-and-iterated-logarithm-notation"],
    salient="The binding margin $\\epsilon c(1-\\tau)=2^{-181}=2\\kappa$ comes from the chunk exchanges of the transform layout, so $\\kappa$ is set by the interchange exponent $\\tau$ and the chunk width $K$, not by the butterfly layers.",
)

ROOT = show(
    "S0",
    r"One deterministic Turing machine with a fixed finite alphabet and a fixed number of one-dimensional tapes outputs $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$ for every $n\ge1$ and all $n$-bit inputs $x,y$, in worst-case time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.",
    r"Reduce multiplication to a cyclic convolution evaluated by Fourier transforms on power-of-two axes, accelerate the transforms' address rearrangements and butterfly layers by two tape procedures built from fixed linear networks with a rank saving, and bound every cost divided by the volume $V=Tp=\Theta(n)$.",
    mot("A transform-based multiplier that scans its $\\Theta(n)$-bit array once per level of a $\\Theta(\\log n)$-level transform already costs $\\Theta(n\\log n)$; beating the conjecture requires making both the data movement and the butterfly arithmetic of the levels cheaper than full scans.",
        "explicit",
        r"Scanning an array of $\Theta(n)$ stored bits at each of¶$\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$.¶We therefore need savings in both movement and arithmetic."),
    [
        infer("S0.1",
              r"To refute the eventual $\Omega(n\lg n)$ lower bound in the fixed-tape model it suffices to give one machine with $\liminf_{n\to\infty}T_A(n)/(n\lg n)=0$, and a bound $O(n(\lg n)^{1-\kappa})$ gives limit zero through all input lengths.",
              r"Its negation requires one machine satisfying¶$\liminf_{n\to\infty}T_A(n)/(n\lg n)=0$.",
              frm=["integer-multiplication-conjecture", "big-omega-theta-and-little-o-notation"]),
        S1,
        S2,
        S3,
        S4,
        S5,
        S6,
    ],
    page="main-theorem",
    frm=["integer-multiplication-conjecture", "multitape-tm", "big-o", "logarithms-and-iterated-logarithm-notation", "big-omega-theta-and-little-o-notation", "finite-alphabet-encodings-and-constant-factor-simulation"],
    salient="The saving is a fixed power of the logarithm, $(\\lg n)^{-\\kappa}$ with the tiny explicit exponent $\\kappa=2^{-182}$, so $T_A(n)/(n\\lg n)$ tends to zero through all input lengths, not just along a subsequence.",
    adds=[
        bind("V", "stored bit volume", "The number of data bits stored in the array an operation acts on; every cost is measured relative to it.", "count"),
        bind("p", "working precision", "The number of fractional bits kept for each real or imaginary component, $6\\lceil\\log_2n\\rceil$ in the final algorithm.", "count"),
        bind("T", "padded box size", "The number of entries of the power-of-two transform array, of order $n/\\log n$.", "count"),
        bind("d", "number of axes", "The number of tensor axes of the transform, of order $p^\\epsilon$, which also bounds the axes one butterfly layer touches.", "count"),
        bind("r", "record length", "The number of complex coefficients in each polynomial record, a power of two.", "count"),
        bind("K", "chunk width", "The number of address bits in each chunk from which a simultaneous layer selects one bit.", "count"),
        bind("\\ell", "rounds per axis", "The base-two logarithm of $r$, which bounds the number of butterfly rounds per axis.", "count"),
        bind("S", "prime box size", "The product of the distinct prime source lengths $s_i$, between $T/2$ and $T$.", "count"),
    ],
)

answer = {"root": ROOT}

# ---------------------------------------------------------------- checks
order = []


def walk(n, depth=0):
    if n["intention"] == "infer":
        order.append(n)
    for c in n.get("children", []):
        walk(c, depth + 1)


walk(ROOT)
pos = -1
for n in order:
    q = n["quote"]["quote"]
    cnt = SRC.count(q)
    first = SRC.find(q)
    line = SRC[:first].count("\n") + 1
    flag = ""
    if n.get("deferred"):
        flag = "deferred"
    else:
        if first < pos:
            flag = "OUT OF ORDER"
        pos = max(pos, first)
    if cnt != 1:
        flag += f" count={cnt}"
    print(f"{n['id']:10s} line {line:5d} {flag}")

ids = []


def collect(n):
    ids.append(n["id"])
    for c in n.get("children", []):
        collect(c)


collect(ROOT)
assert len(ids) == len(set(ids)), "duplicate ids"

if problems:
    print("MISSING QUOTES:")
    for p in problems:
        print(repr(p))
    sys.exit(1)

json.dump(answer, open(OUT, "w"), ensure_ascii=False, indent=1)
print("wrote", OUT, "infer steps:", len(order))
