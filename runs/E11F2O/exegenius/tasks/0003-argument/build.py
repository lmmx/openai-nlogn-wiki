import json, re, sys

ROOT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E11F2O"
SRC = open(ROOT + "/sources/paper.tex", encoding="utf-8").read()


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


SRCN = norm(SRC)


def B(symbol, name, meaning, relation="direct"):
    return dict(symbol=symbol, name=name, meaning=meaning, relation=relation)


def Q(text):
    return dict(source="paper", quote=text)


def infer(id, claim, quote, frm=(), page=None, deferred=False, salient=None):
    n = dict(id=id, intention="infer", claim=claim, quote=Q(quote), **{"from": list(frm)})
    if page:
        n["page"] = page
    if deferred:
        n["deferred"] = True
    if salient:
        n["salient"] = salient
    return n


def show(id, claim, method, mot, children, frm=(), page=None, adds=(), salient=None):
    text, source, quote = mot
    m = dict(text=text, source=source)
    if quote:
        m["quote"] = Q(quote)
    n = dict(id=id, intention="show", claim=claim, method=method, motivation=m,
             children=children, **{"from": list(frm)})
    if page:
        n["page"] = page
    if adds:
        n["adds"] = list(adds)
    if salient:
        n["salient"] = salient
    return n


# ---------------------------------------------------------------- A: the two tape procedures

A0 = infer("S1.1",
    "In the fixed finite-tape model, fixed tracks and finitely many work tapes change running time only by a fixed factor, so each procedure below may use any fixed number of tapes.",
    r"Fixed tracks and finitely many work tapes change time by a fixed factor.",
    frm=["turing-machine-tapes", "multitape-machine-cost-model-and-linear-time-scans"],
    page="fixed-tape-model")

A1 = infer("S1.2",
    r"On an array stored in lexicographic order with implicit addresses, permuting the digits at two fixed radix-$q$ positions, moving one digit, splitting on a digit and applying a fixed pointwise map, and splitting whole rows cyclically into a fixed number $W$ of streams each take $O(V)$ steps.",
    r"Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes",
    frm=["fixed-tape-model", "lexicographic-order-and-index-tuples", "multitape-machine-cost-model-and-linear-time-scans"],
    page="stream-arrays")

A2 = infer("S1.3",
    r"If a target field $y\in[q^k]$ follows its control fields, the update $y\mapsto y+a(\text{controls})\bmod q^k$ and multiplication of $y$ by a fixed rational unit cost $O(V)$, by splitting each fiber's blocks at $q^k-a$ and merging the two pieces in the opposite order.",
    r"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the fixed number of control values.",
    frm=["stream-arrays", "modular-arithmetic-and-residues", "primes-divisibility-gcd-and-coprimality"],
    page="controlled-shifts")

A3 = show("S1.4",
    r"Performing a forward invocation from $X$ to $Y$ at stage 1, the inverse schedule from $Y$ to $X$ at stage 2 and a forward invocation from $X$ to $Y$ at stage 3 sends $(X_a,Y_a)\mapsto(-Y_a,X_a)$ for every $a\in\mathcal T^3$ and restores every scratch value, which in the bit construction is the plain exchange of $X_a$ and $Y_a$.",
    r"Fix the parameters, build one restoring update $y_S\gets y_S+x_S$ per coordinate from the triple gadget, and compose three such updates with alternating direction, one per tensor coordinate.",
    (r"Three additive updates $y\gets y+x$, $x\gets x-y$, $y\gets y+x$ compose to a signed exchange, so a gadget performing one restoring additive update is all that is needed; doing one coordinate of $a\in\mathcal T^3$ per stage keeps each gadget small.",
     "recoverable", None),
    [
        infer("S1.4.1",
            r"The construction fixes $h=100$, $v=\binom h3=161700$, $N=v^3=4227952113000000$ and $m=h^3=10^6$, with data banks $X_a,Y_a$ indexed by $a\in\mathcal T^3$, and at each stage $j$ there are $v^2$ separate invocations acting on coordinate $j$.",
            r"h=100,\qquad v=\binom h3=161700",
            frm=["lexicographic-order-and-index-tuples"]),
        show("S1.4.2",
            r"For arbitrary initial values of its auxiliary wires, a forward invocation of the eight-row schedule (subtract side injection, subtract scatter, copy, gather, scatter, side injection, undo gather, undo copy) changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.",
            r"Compute the net target change of the schedule, which is independent of the scratch values, and check its coefficients case by case on the intersection size $|S\cap T|$.",
            (r"Subtracting the old scratch contributions before adding the new ones makes the net change independent of arbitrary scratch contents, so only the coefficient pattern of the central and side contributions remains to be checked.",
             "explicit",
             r"The first two rows of the following schedule remove the effect of the old scratch values; the next four introduce the source values and add their effect to the target; the last two restore the scratch values."),
            [
                infer("S1.4.2.1",
                    r"With copy $\mathcal V$, gather $\mathcal G$, side injection $\mathcal J$ and scatter $\mathcal R$, rows 0–1 subtract $\mathcal Ja+\mathcal Rc$, rows 2–3 change the scratch to $a+\mathcal Vx$ and $c+\mathcal Gx$, rows 4–5 add $\mathcal R(c+\mathcal Gx)+\mathcal J(a+\mathcal Vx)$ and rows 6–7 restore $c,a$, so the net target change is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$ whatever $a,c$ are.",
                    r"The net target change is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of $a,c$."),
                infer("S1.4.2.2",
                    r"Bit case (scalars in $\mathbb F_2$, neighbors $|S\cap T|=1$): the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod2$, the side wires cancel exactly the intersection-one cases, intersections zero and two already contribute zero, and the self coefficient $|S\cap S|=3$ gives one.",
                    r"In the bit case, the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod2$."),
                infer("S1.4.2.3",
                    r"Complex case (scalars in $\mathbb Z[i,1/2]$, neighbors the distinct triples with even intersection): the central coefficient is $(|S\cap T|-1)/2$, the side wires cancel it for intersections zero and two, intersection one already contributes zero, and the self coefficient is one, so in both cases the net map is $y\gets y+x$.",
                    r"In the complex case, the central coefficient is $(|S\cap T|-1)/2$."),
            ],
            frm=["bitwise-xor", "rational-numbers-dyadic-rationals-and-exact-arithmetic", "complex-numbers", "discrete-math-proof-techniques"],
            page="triple-gadget",
            salient=r"The same eight-row schedule works over two different scalar rings, $\mathbb F_2$ and $\mathbb Z[i,1/2]$, with complementary neighbor rules (intersection one versus intersection zero or two), and its result does not depend on the arbitrary scratch contents."),
        infer("S1.4.3",
            r"Since the inverse schedule effects $X\gets X-Y$, starting from $(x,y)$ the three stages give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$, and each invocation restores its own auxiliary wires.",
            r"Starting from $(x,y)$, the three stages give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$."),
        infer("S1.4.4",
            r"A fixed triple has $z_{\rm b}=3\binom{97}{2}=13968$ and $z_{\rm c}=\binom{97}{3}+3\cdot97=147731$ neighbors, side wires are counted over ordered pairs ($vz$ per invocation), and with $c_{\rm b}=100$, $c_{\rm c}=101$ central wires per invocation and $I=3v^2$ invocations the wire counts are $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=177176569091445000000$ and $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})=1873807244643542670000$.",
            r"z_{\rm b}=3\binom{97}{2}=13968"),
    ],
    frm=["algebraic-structures-groups-rings-and-isomorphisms", "permutations-and-permutation-matrices"],
    page="bank-exchange-network",
    adds=[B(r"\mathcal T", "triple set", r"The set of three-element subsets of $[h]=\{0,\dots,99\}$; bank positions are triples of such subsets."),
          B("v", "triple count", r"The number $v=\binom{100}{3}=161700$ of three-element subsets of a 100-element set.", "count")],
    salient=r"Every scratch wire is restored whatever its initial contents, and in the bit case the net effect of a network of XOR gates is an exact permutation of the wires.")

A4 = show("S1.5",
    r"If each source, gate and sink $v$ carries an invertible frame $D_v$ shared by all incidences of a gate and each edge $u\to v$ applies $D_vD_u^{-1}$, then the array network implements $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$, so a signed role permutation sends input role $w$ to $\rho(w)$ with operator $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$.",
    r"Keep the invariant that the stored array equals $D_v$ applied to the logical array, using linearity of the pointwise gates to commute the common frame past each gate.",
    (r"Intermediate frames cancel, so the net effect depends only on the endpoint frames; the intermediate frames are then free to be chosen so that every edge change is cheap.",
     "explicit",
     r"Once the scalar routing is fixed, the endpoint frames determine the array operator on each route; the intermediate frames can then be chosen to make each edge change inexpensive."),
    [
        infer("S1.5.1",
            r"At a gate with logical inputs $\varphi_j$, $R$-linearity gives $\sum_jc_jD_v\varphi_j=D_v(\sum_jc_j\varphi_j)$, so the common frame commutes with the pointwise gate and the invariant passes from the sources (where it holds by definition of the logical input $D_{\rm in}^{-1}f$) to the sinks.",
            r"Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks."),
        infer("S1.5.2",
            r"Hence the implemented operator is $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$, and on a signed role permutation every route, auxiliary roles included, applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$.",
            r"All roles, including the auxiliary roles, enter this identity."),
    ],
    frm=["bank-exchange-network", "stream-arrays", "matrices-invertibility-and-rank", "permutations-and-permutation-matrices"],
    page="frames",
    adds=[B("D_v", "frame", r"The invertible linear operator on a wire's address-indexed array at vertex $v$: the stored array is $D_vg$ when the logical array is $g$."),
          B(r"\rho", "role permutation", r"The permutation of wire roles effected by the scalar network: input role $w$ ends at output role $\rho(w)$.")])

A5 = show("S1.6",
    r"The network's sources, gates and sinks carry nondegenerate subspaces of $\mathcal F=F^{\otimes3}$ (of dimension $m$), nested along every edge, whose absolute dimension changes sum to $Wm-2N+2L$ with total decrease $L=Ich$, where $c$ is the number of central wires per invocation, and $L<N/2$.",
    r"Choose bilinear forms in which triple indicator lines are nondegenerate and neighboring lines orthogonal, prescribe terminal labels, expose one tensor factor per stage, assign common gate labels by the order the gates touch the wires, and count every edge's orthogonal residual.",
    (r"Signed dimension changes telescope to the fixed value $Wm-2N$ between source and sink labels, so the only freedom is the total loss on decreasing edges; keeping it below $N/2$ leaves a strict deficit below $Wm$.",
     "explicit",
     r"The saving will come from keeping the total dimension lost on decreasing edges small relative to $N$."),
    [
        infer("S1.6.1",
            r"For the bit network the form $\langle x,y\rangle=x^{\mathsf T}(I-J/9)y$ on $\mathbb Q^h$ (eigenvalues $1$ and $-91/9$) gives $\langle t_S,t_T\rangle=|S\cap T|-1$ and $\langle t_T,t_T\rangle=2$, and for the complex network the dot product on $\mathbb F_2^h$ gives $t_T\cdot t_T=1$, so in either label field every triple line is nondegenerate and neighboring triple lines are orthogonal.",
            r"Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label field belonging to either construction."),
        infer("S1.6.2",
            r"With terminal labels $U_a\to\mathcal F$ on $X_a$, $0\to U_a^\perp$ on $Y_a$ and $0\to\mathcal F$ on scratch roles, source dimensions sum to $N$ and sink dimensions to $Wm-N$; since each touched wire has one incoming and one outgoing incidence with the same gate label, signed changes telescope to $Wm-2N$ and absolute changes total $Wm-2N+2L$.",
            r"If decreasing edges lose a total dimension $L$, the sum of absolute changes is $Wm-2N+2L$."),
        infer("S1.6.3",
            r"At stage $j$, with $A=F^{\otimes(j-1)}$, $P=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle$ and $B=P^\perp$, each $X$ label grows from $A\otimes\langle t\rangle\otimes Q$ to $(A\otimes F)\otimes Q$ and each $Y$ label from $B\otimes\langle t\rangle\otimes Q$ to $(P\otimes\langle t\rangle)^\perp_{A\otimes F}\otimes Q$, which are exactly the next stage's incoming labels.",
            r"These transitions expose one tensor factor at each stage."),
        infer("S1.6.4",
            r"The gates at times $0,\dots,7$ get labels $B\otimes\langle t\rangle$, $B\otimes F$, $(B\otimes F)\perp(P\otimes\langle t\rangle)$, $A\otimes F$, $B\otimes F$, $(B\otimes F)\perp(P\otimes t^\perp)$, $A\otimes F$, $A\otimes F$ (tensored by $Q$), so a central wire returns once from $A\otimes F$ to $B\otimes F$, losing exactly $P\otimes F$.",
            r"The gate order below confines all decreases to this return, while the other edges realize the prescribed stage transitions."),
        infer("S1.6.5",
            r"Case by case, with $a=h^{j-1}$ and $f=h^{3-j}$, the residual dimensions are: $X$ in$\to2$: $(a-1)(h-1)$; $X$ $2\to3$: $h-1$; $Y$ $0\to1$: $(a-1)(h-1)$; $Y$ $4\to5$: $h-1$; center source$\to1$: $(a-1)h$; center $1\to3$, $3\to4$, $4\to6$: $h$ each; side source$\to0$: $a-1$; side $0\to2$: $(a-1)(h-1)+1$; side $2\to5$: $h-2$ (using $t_X\perp t_Y$); side $5\to7$: $1$; scratch last$\to$sink: $ah(f-1)$; all other edges $0$; and the only decreasing edges are the central $3\to4$ edges, each losing $h$, so $L=Ich$.",
            r"The only decreasing edges are the central-wire edges from time 3 to time 4; their dimension loss is $h$."),
        infer("S1.6.6",
            r"Over $\mathbb F_2$ every nonzero residual is nondegenerate and contains a norm-one vector, hence is nonalternating and has an orthonormal basis.",
            r"Thus every nonzero residual is nonalternating."),
        infer("S1.6.7",
            r"The loss ratios are exactly $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both smaller than $1/2$.",
            r"In particular, both are smaller than $1/2$."),
    ],
    frm=["bilinear-orthogonal", "frames", "bank-exchange-network", "triple-gadget", "vector-spaces-basis-and-dimension"],
    page="subspace-labels",
    adds=[B(r"\mathcal F", "label space", r"The tensor cube $F^{\otimes3}$ of $F=\mathbb Q^{100}$ (bit network) or $F=\mathbb F_2^{100}$ (complex network), of dimension $m$."),
          B("L", "dimension loss", r"The total dimension lost on the decreasing edges of the network.", "count"),
          B("t_T", "triple indicator", r"The indicator vector in $F$ of a three-element subset $T$ of the ground set.")],
    salient=r"The loss ratios are exact rationals, $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, and all loss sits on one kind of edge: the central wires returning from time 3 to time 4.")

# ---- chunk interchange (bit variant of the key step)

A6_1_5 = show("S1.7.1.5",
    r"For a fixed finite set of rational $m\times m$ matrices there is a fixed odd prime $q$ such that, for $A$ of rational rank $a$, the address shear $(H,D)\mapsto(H+AD,D)$ on two groups of $m$ fields over $\mathbb Z/q^k\mathbb Z$ takes exactly $a$ interchanges of an $H$ field with a $D$ field plus $O(V)$ further work.",
    r"Factor $A=E_1\Pi E_2$ with lower-triangular invertible $E_1,E_2$ and a partial permutation $\Pi$ with $a$ ones, perform the triangular changes by controlled shifts in tape order, and implement each one of $\Pi$ by a single interchange between two linear updates.",
    (r"Controlled shifts update a later field from earlier ones in linear time, so lower-triangular coordinate changes are cheap; only the rank-many ones of the middle factor need a genuine interchange.",
     "explicit",
     r"Lower triangular changes of coordinates can be performed entirely in this direction."),
    [
        infer("S1.7.1.5.1",
            r"By elimination with the topmost nonzero row and its rightmost nonzero entry as pivot, every rational $m\times m$ matrix of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation matrix with exactly $a$ ones.",
            r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization",
            frm=["matrices-invertibility-and-rank", "permutations-and-permutation-matrices"],
            page="triangular-factorization"),
        infer("S1.7.1.5.2",
            r"With $q$ avoiding every denominator and diagonal numerator of the fixed factors, a lower-triangular transformation of $H$ or $D$ costs $O(V)$ by updating coordinates in descending physical order with controlled shifts and unit scalings.",
            r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$: update coordinates in descending physical order."),
        infer("S1.7.1.5.3",
            r"After transforming $D$ by $E_2$ and $H$ by $E_1^{-1}$, each one at $(i,j)$ of $\Pi$ is realized by $D_j\gets D_j+H_i$, an interchange of $H_i$ and $D_j$, and $D_j\gets H_i-D_j$, which sends $(h,d)$ to $(h+d,d)$ with one interchange, so the shear uses exactly $a$ interchanges.",
            r"On an initial pair $(h,d)$ this sequence yields $(h+d,d)$."),
    ],
    frm=["controlled-shifts", "triangular-factorization", "matrices-invertibility-and-rank", "modular-arithmetic-and-residues", "primes-divisibility-gcd-and-coprimality"],
    page="matrix-shear",
    salient=r"The number of recursive interchanges is exactly the rank of the matrix, however large its entries are.")

A6_1 = show("S1.7.1",
    r"For $e=m^k$, two disjoint chunks of $e$ radix-$q$ digits preceded by a row field of length divisible by $W^k$ can be interchanged in $O(Ve^\tau)$ time on fixed tapes, where $\tau$ is a rational with $s_{\rm b}/W_{\rm b}<m^\tau$.",
    r"Write each chunk as $m$ fields of $e/m$ digits, split rows into $W$ role streams, run the bit network with shear frames $\Phi_{M_v}$, implement each edge change by as many recursive interchanges as its rank, read off $H\gets H+D$ from the frame identity, complete the interchange with two linear updates, and solve the recurrence $F_k\le(s/W)F_{k-1}+O(1)$.",
    (r"Each edge's address shear costs as many smaller interchanges as its rank, so one level makes $s$ calls on volume $V/W$; since $s<Wm$, multiplying the width by $m$ multiplies the per-volume cost by only $s/W<m^\tau$.",
     "explicit",
     r"Because the sum of these ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width."),
    [
        infer("S1.7.1.1",
            r"For nondegenerate labels $U\subset V$, the projection difference $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement, so its rational rank is $\dim V-\dim U$, and reversing the edge only negates it.",
            r"Its rank is $\dim V-\dim U$; reversing the edge negates the matrix without changing its rank.",
            frm=["vector-spaces-basis-and-dimension", "matrices-invertibility-and-rank"],
            page="bilinear-orthogonal"),
        infer("S1.7.1.2",
            r"With matrices $M_v=P_U$ at gates and sinks of label $U$, $-P_{U_a}$ at each source $X_a$ and $0$ at other sources, edge ranks equal label-dimension changes except at the $N$ sources $X_a$, whose first edge matrix $2P_{U_a}$ has rank one where the dimension change was zero, so $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}=177176569088785861287000000<W_{\rm b}m$, a deficit of $N-2L_{\rm b}>0$.",
            r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$."),
        infer("S1.7.1.3",
            r"For every input role $w$ the endpoint difference is $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$: for $X_a$ it is $P_{U_a^\perp}-(-P_{U_a})$, and every other role has zero source matrix and identity sink matrix.",
            r"For an input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$."),
        infer("S1.7.1.4",
            r"The relative deficit $\eta_{\rm b}=(W_{\rm b}m-s_{\rm b})/(W_{\rm b}m)=339/22587335000000$ exceeds $20\cdot2^{-50}$, and $\log m<20$ gives $m^{1-2^{-50}}>m(1-20\cdot2^{-50})>m(1-\eta_{\rm b})$, so $s_{\rm b}/W_{\rm b}<m^\tau$ with $\tau=1-2^{-50}$.",
            r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$."),
        A6_1_5,
        infer("S1.7.1.6",
            r"Splitting whole rows cyclically into $W$ role streams within each prefix gives streams with identical address shapes, each of volume $V/W$ with row count divisible by $W^{k-1}$.",
            r"Each has logical volume $V/W$, and its row count is divisible by $W^{k-1}$."),
        infer("S1.7.1.7",
            r"On every circuit edge $e$ the frame change $\Phi_{A_e}$ with $A_e=M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)}$ is applied to that role stream by the matrix-shear lemma, recursively interchanging each pivot pair of $(e/m)$-digit fields, while each gate acts pointwise at matching addresses.",
            r"On every circuit edge apply $\Phi_{A_e}$ to that role stream; implement it by"),
        infer("S1.7.1.8",
            r"Because a common address permutation commutes with pointwise bit gates, the frame identity with frames $\Phi_{M_v}$ gives output $f'_{\rho(w)}=\Phi_{M_{\mathrm{out}(\rho(w))}}\Phi_{-M_{\mathrm{in}(w)}}f_w=\Phi_{I_m}f_w$, so after undoing $\rho$ every original row, scratch rows included, has undergone $H\gets H+D$.",
            r"The result is $H\leftarrow H+D$ on every original row, including rows assigned to scratch roles, whose initial values were arbitrary."),
        infer("S1.7.1.9",
            r"The updates $D\gets D-H$, $H\gets H+D$, $D\gets H-D$ send $(H,D)$ to $(D,H)$; only the middle shear uses the network, and the other two target the later group at linear cost.",
            r"The transformation sends $(H,D)$ to $(D,H)$."),
        infer("S1.7.1.10",
            r"The number of recursive calls is the sum of the edge ranks, exactly $s$, each on a role stream of volume $V/W$, and splitting, merging, gates and triangular operations cost $O(V)$, so the normalized cost satisfies $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.",
            r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
        infer("S1.7.1.11",
            r"With $s/W<m^\tau$, the geometric sum $\sum_{j\le k}(s/W)^j$ is $O(m^{k\tau})$ whether $s/W\le1$ (at most $k+1$ terms) or $s/W>1$, so $F_k=O(e^\tau)$.",
            r"Hence $F_k=O(e^\tau)$."),
        infer("S1.7.1.12",
            r"The recursion runs depth first on fixed tapes: before each of the fixed number $s$ of child calls the $W-1$ inactive role streams are parked on a stack tape and restored afterwards at $O(V)$ cost per node, and descriptor work is $(\log(2V_0))^{O(1)}=O(V_j)$ at every depth because both chunk ranges stay present.",
            r"There are only the fixed number $s$ of child calls."),
    ],
    frm=["matrix-shear", "subspace-labels", "frames", "bank-exchange-network", "stream-arrays", "controlled-shifts", "bilinear-orthogonal"],
    page="power-width-interchange",
    adds=[B("M_v", "vertex matrix", r"The rational $m\times m$ matrix assigned to a source, gate or sink $v$ of the bit network; its frame is the shear $\Phi_{M_v}$."),
          B("A_e", "edge matrix", r"The difference $M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)}$ of the matrices at the ends of edge $e$; its rank counts the recursive interchanges on that edge."),
          B(r"\Phi_M", "shear frame", r"The address permutation moving the array entry at $(H,D)$ to $(H+MD,D)$, with $\Phi_{M'}\Phi_M=\Phi_{M'+M}$."),
          B("F_k", "normalized interchange cost", r"A uniform bound on the time divided by logical volume for interchanging chunks of width $m^k$.")],
    salient=r"The endpoint shear is the same $H\gets H+D$ on every role, including scratch rows with arbitrary contents, because the endpoint matrix difference is exactly $I_m$ on every route.")

A6 = show("S1.7",
    r"There is one fixed multitape procedure that exchanges two disjoint $u$-bit address chunks of any bit array of volume $V$, preserving all other address fields, in $O(Vu^\tau)$ steps with $\tau=1-2^{-50}$, although its intermediate steps form XOR combinations of the data.",
    r"Interchange power-width chunks of $e=m^k$ radix-$q$ digits recursively with the bit network, then reduce arbitrary widths to power widths by taking rows from a few high digits, writing the remaining width in base $m$, and padding binary ranges to $[q^e]$.",
    (r"The recursion needs a row field divisible by $W^k$ and widths that are powers of $m$; both can be manufactured cheaply, because moving $O(\log e)$ high digits costs only $O(V\log e)=O(Ve^\tau)$.",
     "explicit",
     r"Rows for a general array can be supplied by a few of its own high digits. Their movement will cost less than the final bound."),
    [
        A6_1,
        infer("S1.7.2",
            r"For ranges $[q^e]$, moving the top $O(\log e)$ digits of both chunks into a row field of range $R\ge W^k$ before both remaining chunks costs $O(V\log e)$, and padding it with zero rows to $W^k\lceil R/W^k\rceil<2R$ less than doubles the volume.",
            r"The padded logical volume is less than $2V$."),
        infer("S1.7.3",
            r"Writing the remaining width as $\sum_ja_jm^j$ with $0\le a_j<m$ and applying the power-width interchange to each of the $a_j$ piece pairs of width $m^j$ costs $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$, a geometric sum because $a_j<m$ and $m^k<me$.",
            r"The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a geometric sum of the stated order."),
        infer("S1.7.4",
            r"Binary chunks of $u$ bits are padded numerically from $[2^u]$ to $[q^e]$ with $e$ least such that $q^e\ge2^u$, a fixed-factor volume increase that preserves order, and since $e=O(u)$ the bound is $O(Vu^\tau)$.",
            r"Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$."),
        infer("S1.7.5",
            r"Chunks whose widths differ by one bit are interchanged by one equal-width interchange plus one single-bit move costing $O(V)$.",
            r"Each case uses one single-bit move, costing $O(V)$ by Lemma~\ref{lem:elementary-streams}, in addition to the equal-width interchange."),
    ],
    frm=["stream-arrays", "bank-exchange-network", "frames", "subspace-labels", "bitwise-xor", "binary-representation-of-integers"],
    page="chunk-swap",
    adds=[B("e", "power width", r"The number of radix-$q$ digits in each interchanged chunk; the recursion handles $e=m^k$.", "count"),
          B("q", "prime radix", r"A fixed odd prime avoiding all denominators of the fixed network matrices and their triangular factors; chunk fields range over powers of $q$.")],
    salient=r"The final effect is an exact permutation of addresses, yet the procedure gets its speed by computing XOR combinations of data, so it lies outside models that only move data.")

# ---- simultaneous butterfly layer (complex variant of the key step)

A7_1 = show("S1.8.1",
    r"With $C=\frac{1+i}2I+\frac{1-i}2X$ and phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$ on the binary labels, the complex network turns each edge into one two-point kernel per orthonormal residual basis vector, $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$ in total, and on a group of $e=mf$ selected chunks it produces $C^{\otimes e}$ on every role from $s_{\rm c}$ child calls on $f$ chunks.",
    r"Factor each frame change into translation kernels using additivity of Hamming weight modulo four over orthogonal binary vectors, conjugate the residual basis into coordinate slots by an invertible binary address map, and telescope frames along routes with $Z$-sign corrections at the endpoints.",
    (r"All phase frames are diagonalized by the same $H^{\otimes m}$, so a frame change is a diagonal phase that factors over an orthonormal residual basis, and each factor is exactly the two-point kernel on one direction, an instance of the same operation on fewer axes.",
     "recoverable", None),
    [
        infer("S1.8.1.1",
            r"For orthogonal binary vectors Hamming weight is additive modulo four, so if $V=U\perp E$ with orthonormal basis $\mathcal B$ of $E$ then $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\operatorname{wt}(v)[v\cdot x]\pmod4$, and since $H\operatorname{diag}(1,-1)H=X$ each phase $i^{\pm[v\cdot x]}$ becomes the translation kernel $\frac{1+i}2I+\frac{1-i}2X_v$ or its inverse.",
            r"If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four.",
            deferred=True),
        infer("S1.8.1.2",
            r"Summing basis lengths over all edges gives $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}=1873807244636671267308000000<W_{\rm c}m$, a deficit of $2N-2L_{\rm c}>0$.",
            r"The deficit is $2N-2L_{\rm c}>0$.",
            deferred=True),
        infer("S1.8.1.3",
            r"Zero labels have frame $I$ and full labels frame $C^{\otimes m}$; on the route $X_a\to Y_a$ the operator is $C^{-1}$ on the $27$ coordinates of $\operatorname{supp}(u_a)$ and $C$ elsewhere, which $C=iZC^{-1}Z$ with $Z$ signs before and $i^{27k}Z$ after turns into $C^{\otimes mk}$, so after negating the physical $X$ outputs every role, scratch roles included, carries $C^{\otimes m}$ on each of $k$ columns.",
            r"Every role, including every scratch role, now has the required forward tensor product.",
            deferred=True),
        infer("S1.8.1.4",
            r"Direct multiplication gives $H_0=\frac{1-i}2\mathsf SC\mathsf S$ with $\mathsf S=\operatorname{diag}(1,i)$, $C^2=X$, $C^4=I$ and $C^{-1}=-iZCZ$, all with Gaussian dyadic coefficients.",
            r"These identities use only Gaussian dyadic coefficients."),
        infer("S1.8.1.5",
            r"Taking the residual basis as the first columns of an invertible binary matrix $M$, each edge becomes $\mathcal P_M(\prod_jC_{e_j}^{\pm1})\mathcal P_M^{-1}$, so on $m$ slots of $f$ chunks each residual vector is one child applying $C^{\otimes f}$ to one slot, an inverse kernel being $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$.",
            r"A negative directional kernel still requires only one forward child, because"),
        infer("S1.8.1.6",
            r"Summing residual dimensions gives exactly $s_{\rm c}$ child calls per invocation, each on the $f=e/m$ chunks of one slot, and the corrected network yields $C^{\otimes e}$ on every role.",
            r"Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
    ],
    frm=["frames", "subspace-labels", "bank-exchange-network", "butterfly-layers", "complex-numbers", "euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle", "bitwise-xor", "vector-spaces-basis-and-dimension"],
    page="phase-kernel-network",
    salient=r"An inverse kernel costs no extra recursive call, because $C^{-1}=-iZCZ$ differs from $C$ only by address signs and a fourth root of unity, and every scratch role ends with the same $C^{\otimes m}$.")

A7_3 = show("S1.8.3",
    r"For $K\ge6$ and $f$ selected positions spaced $K$ apart, one fixed procedure performs $y_{j}\gets y_{j}\oplus x_{j}$ at all of them on $fK$-bit chunks $x,y$, restoring a third chunk for every initial value, in time $O(V((fK)^\tau+1))$ plus repair terms bounded by $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$ that are negligible when $K/\log p\to\infty$ and records exceed every power of $p$.",
    r"Pack the $f$ one-bit additions into eight cyclic shifts of whole chunk ranges (each by chunk swaps and a controlled shift) whose segment arithmetic flips the parity of $u$ and restores $w$, then deterministically repair the explicitly bounded set of addresses whose guard values permit carries between segments.",
    (r"A cyclic shift of a whole chunk range is a linear-cost controlled shift, and treating $K$-bit segments as integers lets one shift act on all $f$ selected bits at once; carries between segments happen only on a small, explicitly known address set, which sorting can fix.",
     "explicit",
     r"The construction first uses a constant number of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of addresses."),
    [
        infer("S1.8.3.1",
            r"For a Boolean control $c$, the eight parity-conditioned additions induce the cycle $(00\ 01\ 10)$ and then $(01\ 10\ 11)$ on parity pairs, whose product $(00\ 10)(01\ 11)$ gives $(u',w')=(u+c(1-2(u\bmod2)),w)$: the parity of $u$ flips exactly when $c=1$ and $w$ is restored, with displacement at most four.",
            r"Applying the first cycle and then the second gives $(00\ 10)(01\ 11)$."),
        infer("S1.8.3.2",
            r"Applied simultaneously to the $f-1$ low $K$-bit segments, each line is the single cyclic shift $y\gets y\pm\sum_i2^{j_i}[x_{j_i}=1][z_{j_i}=b]\pmod{2^{fK}}$ (or with $y,z$ interchanged), a bijection because the offset never depends on its target chunk.",
            r"The shift offset never depends on its target chunk, so each line is a bijection of the rectangle."),
        infer("S1.8.3.3",
            r"Outside the set $\mathcal B$ of addresses where some guard value fails $10\le g\le2^{K-1}-11$, no segment carries into the next, so the composition $S_0$ agrees with the ideal permutation $T_0$, and the union bound over $2(f-1)$ guards, each with twenty excluded values among $2^{K-1}$, gives $|\mathcal B|\le\delta_{\rm bad}M$ independently of the payload.",
            r"Since its complete range has $2^{K-1}$ values, the union bound over the $2(f-1)$ guards gives"),
        infer("S1.8.3.4",
            r"Since $T_0$ and $S_0$ are bijections agreeing off $\mathcal B$, $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$, so extracting the bad records, computing their destination ranks and radix-sorting them implements $T_0$ everywhere.",
            r"Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$."),
        infer("S1.8.3.5",
            r"The at most sixteen swaps cost $O(V(fK)^\tau)$ each and the eight rotations $O(V)$ each, the omitted top position is one two-bit XOR in $O(V)$, and after division by $V$ the scan and repair terms tend to zero under the family bounds.",
            r"There are at most sixteen swaps and eight rotations in $S_0$."),
    ],
    frm=["chunk-swap", "controlled-shifts", "stream-arrays", "bitwise-xor", "modular-arithmetic-and-residues"],
    page="packed-selected-bits",
    salient=r"Eight modular additions conditioned on parities implement an XOR of single bits while restoring an arbitrary auxiliary chunk exactly, and the bad fraction $80(f-1)2^{-K}$ does not depend on the data, so the time bound is worst case.")

A7 = show("S1.8",
    r"For $p\ge p_0$, $d=\Theta(p^\epsilon)$, $K=\lfloor d^c\rfloor$ and $r=2^{\Theta(p/d)}$, one fixed procedure applies the tensor product $\mathcal H$ of $H_0$ on one common bit of each of $D\le d$ consecutive $K$-bit chunks to arrays of length-$r$ polynomial records with disk-grid coefficients, returning $Q_p(\mathcal Hz)$ with error below $\sqrt2\,2^{-p}$ in $O(Vd^{\lambda'})$ time.",
    r"Write $H_0^{\otimes D}$ through the Gaussian-dyadic kernel $C$, build $C^{\otimes e}$ recursively from the complex network whose phase frames turn each edge into one child per residual basis vector, realize the binary basis changes by packed selected-bit XORs, take rows from the first chunks, solve the volume-normalized recurrence, bound the dyadic growth, and truncate once.",
    (r"Applying the $D$ factors one at a time costs $D$ full passes; the network replaces this by $s_{\rm c}$ calls on $1/W_{\rm c}$ of the volume each time the number of axes shrinks by $m$, which is cheaper because $s_{\rm c}<W_{\rm c}m$.",
     "explicit",
     r"We will obtain cost $O(Vd^{\lambda'})$, with $\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly factors would require $D$ whole-array passes."),
    [
        A7_1,
        infer("S1.8.2",
            r"Applying $H_0=\frac{1-i}2\mathsf SC\mathsf S$ on all $D$ selected coordinates gives $H_0^{\otimes D}=(\frac{1-i}2)^D\mathcal S_DC^{\otimes D}\mathcal S_D$, where $\mathcal S_D$ multiplies by $i^{x_1+\cdots+x_D}$ and $(\frac{1-i}2)^D=(-i/2)^{\lfloor D/2\rfloor}(\frac{1-i}2)^{D\bmod2}$ is a binary shift and a fourth-root phase with at most one further factor.",
            r"so it is a binary shift and fourth-root phase, with at most one further factor $b$."),
        A7_3,
        infer("S1.8.4",
            r"A binary change of basis of the fixed order $m$ is a fixed number of row additions, each one packed selected-bit addition between two slots of $f$ chunks with a third slot as temporary, so it and its inverse cost $O(V((eK)^\tau+1))$.",
            r"the complete change of basis and its inverse therefore cost $O(V((eK)^\tau+1))$ on a stream of volume $V$."),
        infer("S1.8.5",
            r"One individual $C$ kernel splits the stream on the selected bit and computes $C(u,v)=(\frac{u+v+i(u-v)}2,\frac{u+v-i(u-v)}2)$ on aligned coefficients exactly, so $e$ individual kernels cost $O(Ve)$.",
            r"Thus \(e\) individual kernels cost \(O(Ve)\) on any stream with these complete ranges and record format."),
        infer("S1.8.6",
            r"At an internal node of $e=m^k$ chunks the network makes exactly $s$ calls on slots of $e/m$ chunks, and basis changes, scalar gates, endpoint corrections and reassembly cost $O(V((eK)^\tau+1))$, with polynomial address work absorbed by records of $\Theta(rp)$ bits.",
            r"hence exactly \(s\) calls in one invocation of the network."),
        infer("S1.8.7",
            r"Rows come from the selected bits of the first $q_0=\lceil\log_2W\rceil\lceil\log_m(2d)\rceil$ chunks, processed individually in $O(V\log d)$, whose bits form a row index of range $2^{q_0K}\ge W^{\lceil\log_md\rceil}$ padded to a multiple of that power at most doubling the volume; splitting rows among the $W$ roles gives each child exactly $1/W$ of its parent's volume.",
            r"Each recursive edge call acts on one role stream with volume exactly \(1/W\) of its parent's logical volume."),
        infer("S1.8.8",
            r"With $F(e)$ the time divided by volume, $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ for $e\ge d^{1/2}$ and $F(e)=O(e)$ below, and since $K\le d^c\le e^{2c}$ at internal nodes the overhead is $O(e^{\tau(1+2c)}+1)=O(e^\lambda)$ with $\lambda=1-2^{-52}$.",
            r"The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\)."),
        infer("S1.8.9",
            r"With $s/W\le m^\sigma<m^\lambda$ and $\sigma=1-2^{-50}$, the internal costs sum to $O(e^\lambda\sum_j(s/(Wm^\lambda))^j)=O(e^\lambda)$, and leaves after $j$ levels with $e/m^j<d^{1/2}$ chunks contribute $O((s/W)^je/m^j)\le O(e^\sigma d^{(1-\sigma)/2})$ because $(s/W)^j\le m^{j\sigma}$.",
            r"The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\)."),
        infer("S1.8.10",
            r"Splitting the remaining chunks into at most $(m-1)(1+\lfloor\log_md\rfloor)$ base-$m$ pieces gives total $O(\log(2d)[d^\lambda+d^{\sigma+(1-\sigma)/2}+1])=O(d^{\lambda'})$ for any fixed $\lambda'$ with $\max\{\lambda,\sigma+(1-\sigma)/2\}<\lambda'<1$, here $\lambda'=1-2^{-54}$.",
            r"There are at most \((m-1)(1+\lfloor\log_m d\rfloor)\) pieces."),
        infer("S1.8.11",
            r"For the complex network $s_{\rm c}+64(W_{\rm c}+m+1)^3$ lies strictly between $m^{10}$ and $m^{11}$, so $\nu=11$ and the guard exponent $C_1=20$ exceeds the needed $\nu+3=14$.",
            r"These values give \(m^{10}<B<m^{11}\), hence \(\nu=11\) and \(C_1=20\)."),
        infer("S1.8.12",
            r"The arithmetic depth obeys $A(e)\le s_{\rm c}A(e/m)+E$ at internal nodes, where $E=64(W_{\rm c}+m+1)^3$ exceeds the $24W_{\rm c}^3+4s_{\rm c}+4W_{\rm c}+4$ operations of one invocation, and $A(e)\le8e$ at leaves; since $sx+E\le(s+E)x$ for $x\ge1$ and $(s+E)^{k+1}\le(s+E)^2d^\nu$, this gives $A(e)\le8(s+E)^2d^{\nu+1}$, and with the pieces and diagonals a total below $C_0d^{C_1}$.",
            r"A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}"),
        infer("S1.8.13",
            r"A value at arithmetic depth $j$ lies in $2^{-(p+j)}\mathbb Z[i]$ with modulus at most $2^j$, so $p+\Delta$ fractional and $\Delta+3$ integer bits, $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$ because $\epsilon C_1<1$, represent every intermediate coefficient exactly.",
            r"Thus reserving \(p+\Delta\) fractional bits and \(\Delta+3\) integer and sign bits per real component represents every intermediate coefficient exactly and prevents overflow."),
        infer("S1.8.14",
            r"Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays and the single final truncation $Q_p$ toward zero keeps the disk with error below $\sqrt2\,2^{-p}$.",
            r"Finally, every row of $\mathcal H$ has absolute row sum one."),
    ],
    frm=["phase-kernel-network", "packed-selected-bits", "power-width-interchange", "chunk-swap", "fixed-point-disk-grid", "butterfly-layers", "negacyclic-ring", "subspace-labels", "frames", "rational-numbers-dyadic-rationals-and-exact-arithmetic"],
    page="simultaneous-butterfly-layer",
    adds=[B("C", "two-point kernel", r"The Gaussian-dyadic matrix $C=H\operatorname{diag}(1,i)H=\frac{1+i}2I+\frac{1-i}2X$, with $C^4=I$ and $H_0=\frac{1-i}2\operatorname{diag}(1,i)C\operatorname{diag}(1,i)$."),
          B(r"\mathcal H", "parallel butterfly layer", r"The tensor product of $H_0$ on the selected bit of each of the $D$ chunks, acting coefficientwise on the records."),
          B("Q_p", "truncation to precision", r"Truncation of the real and imaginary parts of every coefficient toward zero to the grid $2^{-p}\mathbb Z$."),
          B(r"\lambda", "internal exponent", r"The fixed exponent $1-2^{-52}$ bounding the per-volume overhead $O(e^\lambda)$ at internal recursion nodes."),
          B(r"\sigma", "complex recurrence exponent", r"The fixed exponent $1-2^{-50}$ with $s_{\rm c}/W_{\rm c}<m^\sigma$."),
          B("C_1", "guard exponent", r"The fixed exponent $20$ in the guard width $\lceil C_0d^{C_1}\rceil$ of extra bits per component."),
          B("e", "group size", r"The number of selected chunks handled by one recursive call of the layer.", "count")],
    salient=r"The layer is evaluated exactly in Gaussian dyadics through intermediate operators that are not contractions, yet a single final truncation suffices and the guard width stays $o(p)$.")

A = show("S1",
    r"Two tape procedures save a power of their parameter: interchanging two disjoint $u$-bit address chunks of an array of volume $V$ costs $O(Vu^\tau)$, and the normalized butterfly $H_0$ on one selected bit of each of $D\le d$ address chunks of polynomial records costs $O(Vd^{\lambda'})$, with fixed $\tau,\lambda'<1$.",
    r"Derive each procedure from a fixed linear network that exchanges two banks and restores scratch values, run the network on $W$ role streams of volume $V/W$ with frames chosen so that every edge costs as many smaller recursive calls as its label-dimension change, and solve the volume-normalized recurrence using $s<Wm$.",
    (r"Normalizing time by stream volume turns the recursion into $F(mf)\le(s/W)F(f)+O(\text{overhead})$; because the network needs only $s<Wm$ smaller calls on streams of $1/W$ the volume, each factor $m$ in the parameter costs a factor less than $m$, which is a power saving.",
     "explicit",
     r"After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving."),
    [A0, A1, A2, A3, A4, A5, A6, A7],
    frm=["fixed-tape-model", "stream-arrays", "multitape-machine-cost-model-and-linear-time-scans"],
    adds=[B("m", "label dimension", r"The dimension $m=h^3=10^6$ of the label space; one recursion level divides the parameter (digits or axes) by $m$.", "count"),
          B("W", "wire count", r"The number of wires (roles) of the network in use, $W_{\rm b}$ for the bit network or $W_{\rm c}$ for the complex one.", "count"),
          B("s", "smaller-call count", r"The total number of smaller recursive calls per network invocation: the sum of the edge ranks or residual dimensions, $s_{\rm b}$ or $s_{\rm c}$.", "count"),
          B(r"\tau", "interchange exponent", r"The fixed exponent $1-2^{-50}$ in the interchange cost $O(Vu^\tau)$, chosen with $s_{\rm b}/W_{\rm b}<m^\tau$."),
          B(r"\lambda'", "layer exponent", r"The fixed exponent $1-2^{-54}$ in the layer cost $O(Vd^{\lambda'})$."),
          B("h", "ground-set size", r"The size $h=100$ of the ground set whose three-element subsets index the banks.", "count"),
          B("N", "bank size", r"The number $N=v^3=4227952113000000$ of values in each of the two data banks.", "count"),
          B("u", "chunk bit width", r"The number of address bits in each of the two interchanged chunks.", "count"),
          B("D", "selected chunk count", r"The number $D\le d$ of consecutive address chunks whose selected bit one butterfly layer acts on.", "count"),
          B("H_0", "normalized butterfly", r"The two-point map $H_0(u,v)=((u+v)/2,(u-v)/2)$, the matrix $\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$.")],
    salient=r"The whole saving rests on a strict but tiny deficit: the relative rank deficits are $339/22587335000000\approx1.5\cdot10^{-11}$ and $73/19906842167500\approx3.7\cdot10^{-12}$, yet any strict inequality $s<Wm$ gives a power saving.")

# ---------------------------------------------------------------- B: ring convolution

B1_4 = show("S2.1.4",
    r"Decimation in frequency (pair $z_k$ with $z_{k+t/2}$ by $H_0$, multiply the second output by $\omega_t^{-k}$, recurse in both branches) computes $B_tF^-_t$, the transform stored in bit-reversed order, and running the levels in reverse computes $F^+_tB_t^{-1}$, consuming that order directly.",
    r"Split the length-$t$ transform into two length-$t/2$ transforms by one butterfly level, track which slot receives each frequency bit, and invert the levels in reverse order.",
    (r"Each level writes one frequency bit into the slot vacated by the paired address bit, so outputs land in bit-reversed order without moving whole frequency indices, and since $H_0^2=I/2$ the reversed levels invert the forward ones up to $1/t$.",
     "recoverable", None),
    [
        infer("S2.1.4.1",
            r"For $b\in\{0,1\}$, $(F^-_tz)_{2h+b}$ is the length-$t/2$ transform, with root $\omega_t^2$, of $\omega_t^{-bk}(z_k+(-1)^bz_{k+t/2})/2$, so one butterfly level followed by the twiddle and two half-length transforms computes $F^-_t$.",
            r"This computes $F_t^-$ because, for $b\in\{0,1\}$,"),
        infer("S2.1.4.2",
            r"By induction on the levels, after all $a=\log_2t$ rounds the named slots hold the frequency bits from low to high, so $(F^-_tz)_j$ occupies slot $\operatorname{rev}_a(j)$.",
            r"the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$."),
        infer("S2.1.4.3",
            r"As $H_0^2=I/2$, each reversed level is half the inverse of its forward level, so the reverse procedure composed with $B_tF^-_t$ is $I/t$, and by character cancellation it equals $F^+_tB_t^{-1}$.",
            r"As $H_0^2=I/2$, the reversed level is half the inverse of the corresponding forward level."),
    ],
    frm=["synthetic-transform", "negacyclic-ring", "binary-representation-of-integers", "permutations-and-permutation-matrices"],
    page="butterfly-layers",
    salient=r"The opposite transform needs no reordering: it consumes the bit-reversed order the forward transform leaves.")

B1 = show("S2.1",
    r"A fixed-tape procedure computes the synthetic transform $LBF^-_{\boldsymbol t}$ on $M$ records of length $r$ over $d-1$ axes of lengths $t_i\in\{2^{\ell-1},2^\ell\}$, and its opposite $F^+_{\boldsymbol t}B^{-1}L^{-1}$ on that stored order, each with error below $\sqrt2\ell\,2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.",
    r"Use the roots $\omega_t=y^{2r/t}$, which act as signed shifts, compute the transform by decimation in frequency, group one level of all axes into a parallel butterfly and one monomial twiddle, and fix a layout $L$ that puts the selected bits of all axes at a common offset in consecutive $K$-bit chunks so each round is one simultaneous layer.",
    (r"The simultaneous layer needs the selected bits of all participating axes at one offset in consecutive $K$-bit chunks; building that layout once with chunk swaps lets each of the $\ell$ rounds be a single fast layer.",
     "explicit",
     r"To apply Proposition~\ref{prop:simultaneous-layer} in a transform round, we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks."),
    [
        infer("S2.1.1",
            r"In $\mathcal R_r=\mathbb C[y]/(y^r+1)$, multiplication by $y^a$ permutes the coefficients and changes some signs, so it is an isometry for the coefficient sup norm.",
            r"Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes some signs; consequently it is an isometry for this norm.",
            frm=["polynomials", "complex-numbers", "norms-and-the-triangle-inequality"],
            page="negacyclic-ring"),
        infer("S2.1.2",
            r"Truncating real and imaginary parts toward zero to the grid $2^{-p}\mathbb Z$ satisfies $\|Q_pz-z\|_\infty<\sqrt2\,2^{-p}$ and $\|Q_pz\|_\infty\le\|z\|_\infty$.",
            r"\|Q_p z-z\|_\infty<\sqrt2\,2^{-p}",
            frm=["complex-numbers", "binary-representation-of-integers", "rational-numbers-dyadic-rationals-and-exact-arithmetic", "norms-and-the-triangle-inequality"],
            page="fixed-point-disk-grid"),
        infer("S2.1.3",
            r"For a power of two $t\mid2r$ and $\omega_t=y^{2r/t}$, $\sum_{k<t}\omega_t^{jk}$ is $t$ if $t\mid j$ and $0$ otherwise, because shifting $k$ by $t/2^{v+1}$ multiplies the sum by $y^{rj_0}=-1$ and $\mathcal R_r$ has no two-torsion, so $F^+_tF^-_t=t^{-1}I$ despite zero divisors.",
            r"Hence the sum is zero, since the additive group of $\mathcal R_r$ has no two-torsion.",
            frm=["negacyclic-ring", "dft-cyclic-convolution", "geometric-series-and-orthogonality-of-sums-of-roots-of-unity"],
            page="synthetic-transform",
            salient=r"Character cancellation holds even though $\mathcal R_r$ has zero divisors, so one cannot divide by $\omega_t^j-1$ as in the complex case."),
        B1_4,
        infer("S2.1.5",
            r"For $D$ axes $F^\pm_{\boldsymbol t}=\bigotimes_iF^\pm_{t_i}$, and since each axis's twiddle depends only on its own address bits it commutes with the other axes' butterflies, so a round is a parallel butterfly $\mathcal H$ followed by one recordwise monomial $J_E$ whose exponent is computed from the address; $\mathcal H$ is a contraction and $J_E$ an isometry.",
            r"Consequently the individual axis steps may be grouped as a parallel butterfly $\mathcal H$, followed by one recordwise monomial operation $J_E$.",
            frm=["multidim-transform", "butterfly-layers"]),
        infer("S2.1.6",
            r"Moving the top slot of each long axis and the lowest $(\ell-1)\bmod K$ slots of every axis to a prefix costs $O(TpdK)$ and leaves each axis with consecutive $K$-bit chunks.",
            r"There are at most $D(b+1)=O(dK)$ listed slots, so the moves cost $O(TpdK)$."),
        infer("S2.1.7",
            r"Reordering the chunks from axis-major to chunk-index-major takes $O(p/K)$ exchanges of $K$-bit chunks, each $O(TpK^\tau)$ by the chunk-swap lemma, for $O(Tp\,pK^{\tau-1})$ in total; these moves define the layout $L$.",
            r"These prefix moves and chunk exchanges define $L$."),
        infer("S2.1.8",
            r"Each round on the remaining chunks sees the complete address set $[P]\times[2^K]^D\times[S]$ with the selected bit at a common offset, so the simultaneous layer applies at cost $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.",
            r"The simultaneous-layer procedure therefore applies at cost $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total."),
        infer("S2.1.9",
            r"The at most $K$ rounds on prefix slots apply $H_0$ individually at exact width $p+D+O(1)$ and cost $O(TpdK)$.",
            r"There are at most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$."),
        infer("S2.1.10",
            r"The monomial $y^E$ is one split of each coefficient list into two pieces merged with a sign change in $O(rp)$ per record, and since truncation toward zero is odd and $J_E$ is a signed coefficient permutation, $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$.",
            r"J_EQ_p(\mathcal H z)=Q_p(J_E\mathcal H z)."),
        infer("S2.1.11",
            r"Each round is a contraction followed by one truncation adding less than $\sqrt2\,2^{-p}$, so from zero error at most $\ell$ rounds give error below $\sqrt2\ell\,2^{-p}$ and keep the disk.",
            r"Starting with zero error, at most $\ell$ rounds therefore give the claimed error and disk bounds."),
        infer("S2.1.12",
            r"Conjugating by $L$ gives the full operators $LBF^-_{\boldsymbol t}$ and $F^+_{\boldsymbol t}B^{-1}L^{-1}$, so frequency $j$ is stored at $L(Bj)$ and the opposite procedure ends in axis-major order.",
            r"In particular, the forward entry with frequency address $j$ is stored at $L(Bj)$."),
    ],
    frm=["simultaneous-butterfly-layer", "chunk-swap", "stream-arrays", "fixed-point-disk-grid", "multidim-transform", "negacyclic-ring"],
    page="transform-layout",
    adds=[B("L", "layout permutation", r"The positional permutation of record addresses that moves prefix slots and reorders the $K$-bit chunks of all axes."),
          B("B", "bit-reversal order", r"The tensor product over the axes of the permutations moving frequency $j$ to the bit reversal of $j$."),
          B(r"\omega_t", "synthetic root", r"The power $y^{2r/t}$ of $y$, a $t$-th root of unity in $\mathbb C[y]/(y^r+1)$ acting by a signed coefficient shift.")],
    salient=r"The twiddles are exact signed coefficient permutations, so each round is a contraction with a single truncation and the error grows only linearly in the number of rounds $\ell$.")

B2 = show("S2.2",
    r"For $r=2^\ell<2^p$, the exact Gaussian-integer numerators of the product of two disk-grid polynomials in $\mathcal R_r$ are computed, and $Q_p(fg/r)$ is returned, in time $O(rp\log(rp))$ on a fixed number of tapes.",
    r"Evaluate the four integer coefficient polynomials at $2^{4p}$ with signed carries, multiply the four pairs with the established multiplier, recover every signed coefficient by centered carries, reduce modulo $y^r+1$, and shift.",
    (r"Packing turns a polynomial product into one integer product that the established $O(N\log N)$ multiplier handles, and $4p$-bit fields are wide enough that every product coefficient, bounded by $r2^{2p}$, is recovered unambiguously from its centered residue.",
     "recoverable", None),
    [
        infer("S2.2.1",
            r"The Harvey and van der Hoeven fixed-tape multiplier multiplies $N$-bit integers in $O(N\log(2N))$ and is used as an independent subroutine, not as a recursive call of the improved algorithm.",
            r"This is an independent subroutine.",
            frm=["fixed-tape-model", "big-o"],
            page="nlogn-subroutine"),
        infer("S2.2.2",
            r"With $f=2^{-p}(a+ib)$ and $g=2^{-p}(c+ie)$ the evaluations at $2^{4p}$ have magnitude below $2^{4pr}/2$, and every coefficient of the ordinary products $ac,be,ae,bc$ satisfies $|h_j|\le r2^{2p}<2^{3p}<2^{4p}/2$.",
            r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
        infer("S2.2.3",
            r"Carries in $\{-1,0\}$ give a two's-complement block encoding of each evaluation, and centered extraction with carries in $\{0,1\}$ recovers each $h_j$ as the unique representative of its residue in $[-2^{4p}/2,2^{4p}/2)$.",
            r"Thus $\widehat h_j=h_j$."),
        infer("S2.2.4",
            r"Reducing $ac-be$ and $ae+bc$ modulo $y^r+1$ gives coefficients $H_j$ that are sums of exactly $r$ signed products, so $|H_j|\le r2^{2p}$ and $\|fg/r\|_\infty\le\|f\|_\infty\|g\|_\infty$.",
            r"in particular the normalized product of disk polynomials lies in the disk."),
        infer("S2.2.5",
            r"Shifting each numerator right by $p+\ell$ bits returns $Q_p(2^{-2p}H_j/r)$, and the four integer products dominate the linear packing, extraction, wrapping and truncation costs.",
            r"Four exact integer products dominate the linear packing, extraction, combination, wrapping, and truncation costs."),
    ],
    frm=["nlogn-subroutine", "negacyclic-ring", "polynomials", "binary-representation-of-integers", "modular-arithmetic-and-residues", "convolution-as-polynomial-multiplication"],
    page="signed-kronecker-packing")

Bstep = show("S2",
    r"The normalized convolution $\mathcal M_r(f,g)=(f*g)/(rM)$ of disk-grid arrays over $\mathcal R_r$ on $d-1$ power-of-two axes with $M=T/r$ records is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.",
    r"Take two forward synthetic transforms that keep their stored order $LB$, multiply corresponding records by signed Kronecker packing with the established multiplier, apply the opposite transform to that order, and scale exactly by $M$.",
    (r"A pointwise product commutes with any common record permutation, so the layout- and bit-reversal-permuted order of the forward transforms never has to be undone: the opposite transform consumes it directly.",
     "explicit",
     r"Pointwise multiplication commutes with applying the same record permutation $LB$ to both operands."),
    [
        B1,
        B2,
        infer("S2.3",
            r"Since $F^-_{\boldsymbol t}(f*g)=M(F^-_{\boldsymbol t}f)(F^-_{\boldsymbol t}g)$ and $F^+_{\boldsymbol t}F^-_{\boldsymbol t}=I/M$, scaling by $M$ the opposite transform of the products $uv/r$ gives exactly $(f*g)/(rM)$, and $P(LBu,LBv)=LBP(u,v)$ lets the opposite procedure consume the retained order.",
            r"Since $LB$ permutes records and leaves their polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$."),
        infer("S2.4",
            r"With forward errors below $\sqrt2\ell\,2^{-p}$ each, the bilinear contraction adds below twice that, its truncation below $\sqrt2\,2^{-p}$, and the contractive opposite transform another $\sqrt2\ell\,2^{-p}$, so the scaled error is below $M(3\sqrt2\ell+\sqrt2)2^{-p}=\sqrt2\,M(3\ell+1)2^{-p}$.",
            r"The final exact multiplication by $M$ therefore gives error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed."),
        infer("S2.5",
            r"The $M=T/r$ pointwise products cost $O(Tp\log(rp))$ in total, beside the three transform costs and a linear final scaling.",
            r"Their total cost is $O(Tp\log(rp))$; the three transform costs are as stated, and the last exact scaling is linear in $Tp$."),
    ],
    frm=["dft-cyclic-convolution", "multidim-transform", "negacyclic-ring", "fixed-point-disk-grid", "convolution-as-polynomial-multiplication"],
    page="ring-convolution",
    adds=[B("M", "record count", r"The number $M=\prod_{i<d}t_i=T/r$ of polynomial records in the ring array.", "count"),
          B(r"\mathcal R_r", "negacyclic ring", r"The ring $\mathbb C[y]/(y^r+1)$ of complex polynomials of degree below $r$ with $y^r=-1$."),
          B(r"\mathcal M_r", "normalized ring convolution", r"Cyclic convolution over the $d-1$ axes of arrays with values in $\mathcal R_r$, divided by $rM=T$.")],
    salient=r"No frequency sort is ever executed: the bit-reversal and layout permutations of the forward transforms are consumed directly by the opposite transform.")

# ---------------------------------------------------------------- C: resampling

C1 = show("S3.1",
    r"For one axis with coprime $s<t$ and $\theta=t/s-1>p/\alpha^4$, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ with $(P_su)_j=u_{tj}$, $(P_tv)_k=v_{-sk}$ and linear contractions $A:\mathbb C^s\to\mathbb C^t$, $B_0:\mathbb C^t\to\mathbb C^s$ whose approximations have error below $p^2$ (units of $2^{-p}$) and cost $O(tp^{3/2+\delta}\alpha)$.",
    r"Spread the length-$s$ input onto the length-$t$ grid with a Gaussian kernel, use the exact Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$, and invert $\mathsf T$ on the left through the nearly-identity matrix $N=C\mathsf T\mathsf D$ by a Neumann series.",
    (r"A Gaussian is its own Fourier transform up to scaling, so smoothing by a Gaussian before a transform of one length corresponds to Gaussian-weighted sampling after a transform of another length; when $t/s$ exceeds one by enough, the nearest-point weights dominate, so the sampling map is nearly the identity and can be inverted.",
     "reconstructed", None),
    [
        infer("S3.1.1",
            r"The Gaussian maps satisfy $\mathsf TP_sF_s=P_tF_t\mathsf S$, and since $\alpha^2\theta>1$, $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}<1/2$ for $N=C\mathsf T\mathsf D$, so $N$ is invertible by the Neumann series.",
            r"Thus $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series."),
        infer("S3.1.2",
            r"With $A=\mathsf S/2$ and $B_0=\mathsf D'\mathsf J'C$ whose normalizations multiply to $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$, the left inverse $\mathsf DN^{-1}C$ of $\mathsf T$ gives $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$.",
            r"$2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$"),
        infer("S3.1.3",
            r"The quoted routines have errors $16p$, $3p^2/4$ and $4$ for $\widetilde{\mathsf S}'$, $\widetilde{\mathsf J}'$ and $\widetilde{\mathsf D}'$, and the selection $C$ is an exact ordered scan, so $\widetilde A$ and $\widetilde B_0$ have errors below $p^2$.",
            r"Contraction of the exact maps yields errors less than $16p<p^2$ and $4+3p^2/4<p^2$, respectively."),
        infer("S3.1.4",
            r"The original algorithm's two label-and-sort operations for $P_t$ and $P_s^{-1}$, each costing $O(tp\log t)$, are dropped because these permutations stay in the identity.",
            r"Its two label-and-sort operations implement $P_t$ and $P_s^{-1}$, each costing $O(tp\log t)$."),
    ],
    frm=["dft-cyclic-convolution", "fixed-point-disk-grid", "gaussian-function", "norms-and-the-triangle-inequality", "primes-divisibility-gcd-and-coprimality"],
    page="gaussian-resampling",
    salient=r"The transform of a prime length is expressed exactly through a transform of a power-of-two length, the mismatch being absorbed by two well-conditioned Gaussian maps.")

Cstep = show("S3",
    r"If each axis pair $(s_i,t_i)$ satisfies the one-axis hypotheses, then $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $R=\bigotimes_iP_{s_i}$, $Q=\bigotimes_iP_{t_i}$ and $\gamma=2d\alpha^2$, where the contractions $\mathcal A,\mathcal B_0$ are computed linewise with error below $dp^2$ in time $O(dTp^{3/2+\delta}\alpha)$ plus axis movement $O(Tpd^2(1+\ell^\tau))$, and the permutations $R,Q$ are never executed.",
    r"Take the one-dimensional Gaussian identity, keep its coordinate permutations in the formula instead of sorting, tensor it over the axes in the padded box, and expose each axis by chunk swaps.",
    (r"The usual resampling algorithm sorts twice per coordinate at cost $O(tp\log t)$, which alone would cost a full logarithmic factor; leaving the permutations in the identity removes those sorts, since the chirp and the convolution later absorb them.",
     "explicit",
     r"Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and compute that formula directly."),
    [
        C1,
        infer("S3.2",
            r"Tensoring gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$, and applying the one-dimensional maps line by line in the padded box keeps each axis map a contraction with error below $p^2$, so the $d$ axes give error below $dp^2$ and cost $\sum_i(T/t_i)O(t_ip^{3/2+\delta}\alpha)=O(dTp^{3/2+\delta}\alpha)$.",
            r"Composing the $d$ axis maps gives error less than $dp^2$."),
        infer("S3.3",
            r"Exposing each axis as the innermost field takes $O(d)$ adjacent interchanges of $\ell$- or $(\ell-1)$-bit fields, each $O(Tp(1+\ell^\tau))$ by the chunk-swap lemma with one single-bit move, so all axes cost $O(Tpd^2(1+\ell^\tau))$.",
            r"Exposing and restoring one axis needs $O(d)$ adjacent interchanges, hence all axes need $O(d^2)$."),
    ],
    frm=["multidim-transform", "fixed-point-disk-grid", "chunk-swap", "stream-arrays", "gaussian-function"],
    page="resampling-no-sort",
    adds=[B(r"\mathcal A", "tensor spreading map", r"The tensor product of the one-axis Gaussian spreading contractions $A_i:\mathbb C^{s_i}\to\mathbb C^{t_i}$."),
          B(r"\mathcal B_0", "tensor compression map", r"The tensor product of the one-axis compression contractions $B_{0,i}:\mathbb C^{t_i}\to\mathbb C^{s_i}$."),
          B("R", "source permutation", r"The tensor product of the coordinate permutations $(P_{s_i}u)_j=u_{t_ij}$ on the prime-length axes."),
          B("Q", "target permutation", r"The tensor product of the coordinate permutations $(P_{t_i}v)_k=v_{-s_ik}$ on the power-of-two axes."),
          B(r"\theta", "length gap", r"The relative excess $t/s-1$ of a power-of-two length over its prime length.")],
    salient=r"The coordinate permutations $u_j\mapsto u_{tj}$ and $v_k\mapsto v_{-sk}$, which the original method sorts at cost $O(tp\log t)$ per coordinate, are never carried out.")

# ---------------------------------------------------------------- D: chirp and cancellation

Dstep = show("S4",
    r"With the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$ and even $t_i$, $QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$, and the retained source permutation cancels: $(RF^+_{\boldsymbol s})[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$.",
    r"Verify the chirp identity coefficientwise, then use that a dilation by a unit commutes with the Fourier transform up to inversion and with pointwise products, and apply the normalized convolution rule.",
    (r"Choosing the chirp exponent $s_ij_i^2/t_i$ builds the frequency dilation $Q$ into the phases of Bluestein's convolution, and $R$ disappears because the convolution theorem is insensitive to a common relabeling of frequencies.",
     "explicit",
     r"The chirp identity below performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array."),
    [
        infer("S4.1",
            r"The chirp has period $t_i$ in coordinate $i$, and the coefficient of $u_{\boldsymbol k}$ in $\overline a\cdot(a*(\overline a\cdot u))/T$ is $T^{-1}\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}=T^{-1}\exp(2\pi i\sum_is_ij_ik_i/t_i)$, exactly the coefficient of $QF_{\boldsymbol t}$.",
            r"This is precisely the coefficient in $QF_{\boldsymbol t}$, because $Q$ reads frequency $(-s_i j_i)_i$ from the negative-sign transform.",
            frm=["dft-cyclic-convolution", "euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle", "convolution-as-polynomial-multiplication"],
            page="bluestein-chirp"),
        infer("S4.2",
            r"For a unit $c$ modulo $q$, $F_q^+R_c=R_c^{-1}F_q^+$, and since each $t_i$ is a unit modulo $s_i$ this tensors to $RF^+_{\boldsymbol s}R=F^+_{\boldsymbol s}$, while $(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)=R(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)$.",
            r"Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives"),
        infer("S4.3",
            r"The normalized convolution rule $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$ and $F^+_{\boldsymbol s}F_{\boldsymbol s}=I/S$ give $F^+_{\boldsymbol s}(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=(u*v)/S^2$.",
            r"The normalized convolution rule is $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\mathbin{\cdot}",
            frm=["convolution-as-polynomial-multiplication", "geometric-series-and-orthogonality-of-sums-of-roots-of-unity", "complex-numbers"],
            page="dft-cyclic-convolution"),
        infer("S4.4",
            r"Complex conjugation changes the Fourier sign and commutes with the real permutation $R$, so conjugating the input and output of an algorithm for $RF_{\boldsymbol s}$ gives one for $RF^+_{\boldsymbol s}$ with the same error.",
            r"Finally, conjugation changes the negative Fourier sign to the positive one and commutes with the real permutation $R$."),
    ],
    frm=["resampling-no-sort", "multidim-transform", "permutations-and-permutation-matrices", "modular-arithmetic-and-residues"],
    page="chirp-permutation-cancel",
    salient=r"Both permutations disappear: $Q$ is absorbed into the chirp phases, and $R$ cancels between the two forward transforms and the opposite one.")

# ---------------------------------------------------------------- E: parameters

Estep = show("S5",
    r"For all large $n$, the choices $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$, axis lengths $t_i\in\{r/2,r\}$ with $\prod_it_i=T$ and $t_d=r$, $\alpha=\lceil(12d^2b)^{1/4}\rceil$, and distinct odd primes $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ with $\eta=1/(4d)$ give $Tp=\Theta(n)$, $T/2<S<T$ and every hypothesis of the layer, transform and resampling interfaces.",
    r"Fix conservative rational exponents with explicit slack, derive the size relations from them, and find the primes deterministically in short intervals using an explicit prime-counting bound and trial division.",
    (r"The interfaces pull in different directions: the layer needs $d$ and $K$ to grow slowly in $p$, resampling needs $t_i/s_i-1>p/\alpha^4$, and the cost table needs $S$ to fill a fixed fraction of $T$; primes in $((1-2\eta)t_i,(1-\eta)t_i]$ meet the last two at once.",
     "explicit",
     r"The distinct prime lengths $s_i$ must be close to the powers of two $t_i$: their product must occupy a fixed fraction of the padded box, while each ratio $t_i/s_i$ must leave enough separation for resampling."),
    [
        infer("S5.1",
            r"The fixed rationals are $\tau=\sigma=1-2^{-50}$, $\beta=1/2$, $\delta=1/16$, $\lambda=1-2^{-52}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$, which satisfy $\tau(1+c/\beta)<\lambda$, $\sigma+\beta(1-\sigma)=1-2^{-51}<\lambda<\lambda'<1$, $\epsilon C_1<1$, $\epsilon(2-\tau)<1-\tau$ and $\frac34+\delta+\frac32\epsilon<1$.",
            r"These constants are deliberately conservative; no optimization is claimed."),
        infer("S5.2",
            r"These choices give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$, with $\frac1{12}p^\epsilon\le d\le p^\epsilon$ and $\frac p{12d}\le\ell\le\frac p{3d}$, so $r$ exceeds every fixed power of $p$ and $K/\log p\to\infty$.",
            r"Thus we fix $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, and $C_\ell=1$ in the layer and transform interfaces."),
        infer("S5.3",
            r"Since $\lceil A\rceil\le2A$ for $A\ge1$, $\gamma=2d\alpha^2<28d^2\sqrt b\le28b^{2/3}$, so $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$.",
            r"It follows that $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$."),
        infer("S5.4",
            r"For $x\in\{r/2,r\}$ the interval $((1-2\eta)x,(1-\eta)x]$ contains at least $x/(8d\log x)>d$ primes and the two intervals are disjoint, so distinct odd primes $s_i$ exist, and Bernoulli's inequality gives $S/T>(1-\frac1{2d})^d>\frac12$.",
            r"We may therefore choose distinct odd primes satisfying"),
        infer("S5.5",
            r"Since $\theta_i=t_i/s_i-1>\eta$, $\alpha^4\theta_i>12d^2b/(4d)=3db\ge6b=p$, and $t_i\le r\le T<2^p$, so every hypothesis of the resampling lemma holds.",
            r"\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p."),
        infer("S5.6",
            r"Scanning both intervals by trial division costs $O(dr^{3/2}\operatorname{poly}(p))=n^{o(1)}=o(n)$, and all other scalar setup is polynomial in $p$, so all parameters are computed by the machine rather than supplied as advice.",
            r"$n^{o(1)}=o(n)$ time."),
    ],
    frm=["gaussian-resampling", "resampling-no-sort", "simultaneous-butterfly-layer", "transform-layout", "primes-divisibility-gcd-and-coprimality", "logarithms-floors-ceilings-and-powers-of-two", "quantifiers-sets-and-basic-asymptotic-notation-beyond-big-o"],
    page="parameter-choice",
    adds=[B("s_i", "prime axis length", r"The $i$-th distinct odd prime length, chosen in $((1-2\eta)t_i,(1-\eta)t_i]$.", "count"),
          B("t_i", "power-of-two axis length", r"The $i$-th axis length of the padded box, $r/2$ or $r$.", "count"),
          B(r"\eta", "prime gap fraction", r"The fraction $\eta=1/(4d)$ fixing the interval in which each prime length lies below its power of two.")],
    salient=r"The exponents are tiny, $\epsilon=2^{-75}$ and $c=2^{-56}$, so the number of axes $d=\lfloor b^{2^{-75}}\rfloor$ exceeds one only for astronomically large inputs.")

# ---------------------------------------------------------------- F: algorithm and exactness

F2 = show("S6.2",
    r"With $\mu_i=(\prod_{j<i}s_j)^{-1}\bmod s_i$, the map $\Phi:x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ onto the product of cyclic axes of lengths $s_i$ that preserves cyclic convolution, and it and its inverse with padding cost $O(Tpd^2(1+\ell^\tau))$.",
    r"Show that the image of $x$ has order $S$, write the new coordinates triangularly in the mixed-radix digits of the index, and execute the triangular update as prefix-controlled cyclic shifts after reordering the axes by chunk swaps.",
    (r"Exponents $\mu_i$ that make each new coordinate depend only on earlier mixed-radix digits turn the Chinese-remainder reindexing, a general permutation, into a sequence of linear-time controlled shifts.",
     "explicit",
     r"The following map uses that algebraic split, with coordinate powers that make the change of order a sequence of controlled cyclic shifts."),
    [
        infer("S6.2.1",
            r"The image of $x$ has order $S$ because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all target monomials once and $\Phi$ is an isomorphism preserving cyclic convolution.",
            r"Hence $\Phi$ is an isomorphism and preserves cyclic convolution."),
        infer("S6.2.2",
            r"For $k=\sum_ja_jP_j$ with $P_j=\prod_{h<j}s_h$, the axis-$i$ coordinate of $\Phi(x^k)$ is $a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, because terms with $j>i$ are divisible by $s_i$ and $\mu_iP_i\equiv1$.",
            r"Indeed terms with $j>i$ are divisible by $s_i$, and $\mu_iP_i=1$ modulo $s_i$."),
        infer("S6.2.3",
            r"After the axes are reordered so lower indices come first, updating targets $i=d,\dots,1$ by prefix-controlled cyclic shifts of the valid interval (the identity elsewhere, so zero padding stays zero) and reversing axes by $O(d^2)$ chunk-swap moves costs $O(Tpd^2(1+\ell^\tau))$.",
            r"Each triangular update is a prefix-controlled cyclic shift."),
    ],
    frm=["controlled-shifts", "chunk-swap", "primes-divisibility-gcd-and-coprimality", "modular-arithmetic-and-residues", "algebraic-structures-groups-rings-and-isomorphisms", "convolution-as-polynomial-multiplication"],
    page="crt-axis-map",
    salient=r"A reindexing that looks like an arbitrary permutation becomes triangular, so it runs as a sequence of linear-time controlled shifts.")

F3 = show("S6.3",
    r"For a source disk-grid tensor of norm at most $.5$, the procedure $\widetilde{\mathscr F}$ (linewise $\widetilde{\mathcal A}$, the computed chirp transform, linewise $\widetilde{\mathcal B}_0$, and an exact scale by $2^\gamma$) has exact counterpart $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, and $\widetilde{\mathscr F}^+(z)=\overline{\widetilde{\mathscr F}(\overline z)}$ has exact counterpart $RF^+_{\boldsymbol s}$.",
    r"Evaluate the middle factor $QF_{\boldsymbol t}$ by the chirp identity, computing its complex cyclic convolution through a coefficient twist as a ring convolution over $\mathcal R_r$, and compose with the Gaussian maps.",
    (r"The fast machinery computes only convolutions over $\mathcal R_r$, so the chirp's complex cyclic convolution on the last axis must become a negacyclic one, which the twist $x_d\mapsto\zeta y$ achieves exactly.",
     "explicit",
     r"The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist."),
    [
        infer("S6.3.1",
            r"With $\zeta=e^{\pi i/r}$, $\Theta:x_d\mapsto\zeta y$ is a well-defined isomorphism $\mathbb C[x_d]/(x_d^r-1)\to\mathcal R_r$ since $\zeta^{k+l}(-1)^h=\zeta^j$ for $k+l=j+hr$, so the normalized complex cyclic convolution is $D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$.",
            r"Untwisting therefore recovers the cyclic coefficient with the correct sign.",
            frm=["negacyclic-ring", "dft-cyclic-convolution", "euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle", "algebraic-structures-groups-rings-and-isomorphisms", "convolution-as-polynomial-multiplication"],
            page="coefficient-twist"),
        infer("S6.3.2",
            r"The computed complex convolution twists both operands by disk-grid approximations of $\zeta^k$, calls the ring convolution, and untwists, with total twist cost $O(Tp^{1+\delta})$.",
            r"Generating every factor anew therefore still gives total twist cost $O(Tp^{1+\delta})$."),
        infer("S6.3.3",
            r"The chirp phases are computed modulo $2r$ from $-\sum_is_ij_i^2(r/t_i)$ in $O(dp^{1+\delta})$ per entry, and the computed chirp transform $Q_p(\overline{\widetilde a}\cdot\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,Q_p(\overline{\widetilde a}\cdot x)))$ has exact counterpart $QF_{\boldsymbol t}x$.",
            r"Thus chirp construction costs $O(Td p^{1+\delta})$ in total."),
        infer("S6.3.4",
            r"Composing gives exact counterpart $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, and the conjugated procedure has exact counterpart $RF^+_{\boldsymbol s}$.",
            r"its exact counterpart is $RF_{\boldsymbol s}^{+}$ by"),
    ],
    frm=["ring-convolution", "resampling-no-sort", "chirp-permutation-cancel", "parameter-choice", "fixed-point-disk-grid"],
    page="source-transform",
    adds=[B(r"\zeta", "twist root", r"The root of unity $\zeta=e^{\pi i/r}$ by whose powers the coefficients of the last axis are twisted.")])

F5 = show("S6.5",
    r"All intermediate arrays stay in the disk and the final coefficient error is below $2^{2b+4}S\cdot28\cdot2^\gamma T^2\log_2T\cdot2^{-6b}<448b\,2^{-3b/4}<\frac12$, so rounding yields the exact coefficients $c_j\in[0,2^{3b})$ and radix-$2^b$ carry propagation outputs exactly $2n$ bits.",
    r"Propagate errors in units of $h_p=2^{-p}$ through the chain of contractions and bilinear contractions (ring convolution, complex convolution, chirp, source transform, pointwise product, opposite transform), multiply by the two exact scales, round, and propagate carries under an exact invariant.",
    (r"Contractions do not amplify input errors and bilinear contractions only add the errors of disk operands, so each stage adds a bounded number of units of $2^{-p}$; with $p=6b$ even the final amplification by $2^{2b+4}S$ leaves the error below $1/2$.",
     "recoverable", None),
    [
        infer("S6.5.1",
            r"The ring convolution has error below $E_{\rm ring}=M(3\log_2T+2)<5T\log_2T$ units, and its output stays below norm $.701$ when one operand has norm at most $.7$.",
            r"This proves the disk margin after the scale $M$, without clipping the output."),
        infer("S6.5.2",
            r"The computed complex convolution adds two input-twist errors and one untwist error, each below $4$, giving error below $(E_{\rm ring}+12)h_p<6T\log_2T\,h_p$.",
            r"(E_{\rm ring}+4+4+4)h_p<6TLh_p"),
        infer("S6.5.3",
            r"The computed chirp transform adds the kernel error $2$ and two endpoint errors $4$, giving error below $(6T\log_2T+10)h_p<8T\log_2T\,h_p$ for inputs of norm at most $.6$.",
            r"(6TL+2+4+4)h_p<8TLh_p"),
        infer("S6.5.4",
            r"The source transform has error below $2^\gamma(2dp^2+8T\log_2T)h_p\le E_sh_p$ with $E_s=9\cdot2^\gamma T\log_2T$, because $2dp^2<T\log_2T$ eventually, and its output norm stays below $.501$.",
            r"E_s=9\,2^\gamma TL,"),
        infer("S6.5.5",
            r"Writing $\widetilde U\cdot\widetilde V_1-U\cdot V_1=(\widetilde U-U)\cdot\widetilde V_1+U\cdot(\widetilde V_1-V_1)$, the pointwise product has error below $(2E_s+2)h_p$ and norm below $.5$, and the opposite transform brings it to below $(3E_s+2)h_p$ from $(u*v)/S^2$.",
            r"Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$."),
        infer("S6.5.6",
            r"The first scale by $S$ gives $\widetilde w$ approximating $w=(u*v)/S$ with error below $E_wh_p$, $E_w=S(3E_s+2)<28\cdot2^\gamma T^2\log_2T$, and $\|\widetilde w\|<1/16+10^{-3}$.",
            r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
        infer("S6.5.7",
            r"Since $S\le T<2^b$, $\log_2T<b$ and $\gamma\le b/4$, the error after the second scale $2^{2b+4}S$ is below $448b\,2^{-3b/4}<\frac12$, so the nearest integer to each real value is the correct coefficient.",
            r"The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient."),
        infer("S6.5.8",
            r"Carries $k_{j+1}=\lfloor(c_j+k_j)/2^b\rfloor$ satisfy $0\le k_j<2^{2b}$ and the invariant $\sum_{h<j}c_h2^{bh}=\sum_{h<j}d_h2^{bh}+k_j2^{bj}$, which fixes the first $j$ radix digits, and the product is below $2^{2n}$, so exactly $2n$ output bits remain.",
            r"The unprocessed terms are multiples of $Q_0^j$, so the identity fixes the first $j$ radix digits of the full product."),
    ],
    frm=["source-transform", "ring-convolution", "chirp-permutation-cancel", "coefficient-twist", "fixed-point-disk-grid", "radix-digit-convolution", "norms-and-the-triangle-inequality", "binary-representation-of-integers"],
    page="exact-recovery",
    salient=r"Precision $p=6b$, only six times the digit width, suffices: the error is amplified by about $2^{5b+\gamma}$ yet still ends below $2^{-3b/4}$ after the final scaling.")

Fstep = show("S6",
    r"The algorithm (split into radix-$2^b$ digits, map by $\Phi$ to the prime axes, compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$, multiply pointwise, apply $\widetilde{\mathscr F}^+$, scale by $S$ and then by $2^{2b+4}S$, round, undo $\Phi$ and propagate carries) outputs exactly $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$.",
    r"Identify the exact counterpart of every stage through the Chinese-remainder isomorphism, the source-transform identity and permutation cancellation, then show the accumulated approximation error after both scalings is below $1/2$, so rounding recovers the integer coefficients.",
    (r"The product's radix-$2^b$ coefficients are the convolution of the digit lists and are integers below $2^{3b}$, so any approximate convolution accurate to within $1/2$ determines them exactly, and carries then give the binary product.",
     "explicit",
     r"Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients."),
    [
        infer("S6.1",
            r"Writing the inputs as polynomials in $2^b$ with $\lceil n/b\rceil$ digits, the product has degree below $2n/b\le T/2<S$, so convolution modulo $x^S-1$ has no wraparound, and every coefficient satisfies $0\le c_j<2^{3b}$.",
            r"Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
            frm=["polynomials", "binary-representation-of-integers", "convolution-as-polynomial-multiplication", "schoolbook-multiplication-and-divide-and-conquer-multiplication"],
            page="radix-digit-convolution"),
        F2,
        F3,
        infer("S6.4",
            r"By permutation cancellation the exact counterpart after the three transforms is $(u*v)/S^2$, so the first scale by $S$ gives $w=(u*v)/S$ and the second scale by $2^{2b+4}S$ gives $2^{2b+4}(u*v)$, which undoes the input scale $2^{-b-2}$ on each digit and whose inverse image under $\Phi$ is the integer coefficient convolution.",
            r"The two occurrences of $S$ in this algorithm undo different normalizations."),
        F5,
    ],
    frm=["radix-digit-convolution", "parameter-choice", "chirp-permutation-cancel", "dft-cyclic-convolution", "fixed-point-disk-grid"],
    page="multiplication-algorithm",
    adds=[B(r"\Phi", "CRT address map", r"The algebra isomorphism $x\mapsto\prod_ix_i^{\mu_i}$ from one cyclic convolution of length $S$ to the product of the prime-length cyclic axes."),
          B(r"\widetilde{\mathscr F}", "computed source transform", r"The numerical procedure approximating $RF_{\boldsymbol s}$ through resampling, the chirp and the ring convolution.")],
    salient=r"A numerical computation that truncates at every stage yields an exact integer product, because the total error is provably below $1/2$.")

# ---------------------------------------------------------------- G: cost

Gstep = show("S7",
    r"The running time is $O(Tp\cdot p^{1-\kappa})=O(n(\log n)^{1-\kappa})$, because every row of the cost table divided by $Tp$ is at most $p^{1-2\kappa}$ times a fixed power of $\log p$, and fixed powers of $\log p$ are eventually at most $p^\kappa$.",
    r"List every operation's cost divided by $V=Tp$ as a power of $p$, compute the seven dominant margins below one from the fixed exponents, show that setup and exceptional streams cost $o(Tp)$, and use schoolbook multiplication below a fixed cutoff.",
    (r"Since $Tp=\Theta(n)$ and $p=\Theta(\log n)$, a normalized cost of $p^{1-2\kappa}$ per row gives the theorem, and the extra margin $\kappa$ absorbs the logarithmic factors from base-$m$ partitions and recursion depth.",
     "explicit",
     r"This explicit slack will cover any remaining fixed power of $\log p$."),
    [
        infer("S7.1",
            r"Case by case, divided by $Tp$: prefix-slot moves and individual rounds cost $dK$ (power $\epsilon(1+c)$); layout chunk exchanges $pK^{\tau-1}$ (power $1-\epsilon c(1-\tau)$); simultaneous butterfly rounds $\ell d^{\lambda'}$ (power $1-\epsilon(1-\lambda')$); CRT and axis layouts $d^2(1+\ell^\tau)$ (power $\tau+\epsilon(2-\tau)$); Gaussian line maps $dp^{1/2+\delta}\alpha$ (power $3/4+\delta+3\epsilon/2$); chirps, twists and scalar products $dp^\delta$ (power $\epsilon+\delta$); packed polynomial products $\log(rp)$ (power $1-\epsilon$); final scaling and rounding $p^\delta$ and input, padding, carries and output $1$, both absorbed.",
            r"Table~\ref{tab:costs} lists costs after division by $V$; a fixed number of repeated transforms and convolutions is included in its constants."),
        infer("S7.2",
            r"The seven margins below one are $g_1=1-\epsilon(1+c)>\frac12$, $g_2=\epsilon c(1-\tau)=2^{-181}$, $g_3=\epsilon(1-\lambda')=2^{-129}$, $g_4=1-\tau-\epsilon(2-\tau)>2^{-51}$, $g_5=\frac14-\delta-\frac32\epsilon>\frac18$, $g_6=1-\delta-\epsilon>\frac12$ and $g_7=\epsilon=2^{-75}$, so $\min_ig_i=2^{-181}=2\kappa$.",
            r"Thus $\min_i g_i=2^{-181}=2\kappa$."),
        infer("S7.3",
            r"The layout's $O(p/K)$ exchanges of width-$K$ chunks cost $O(VK^\tau)$ each, giving $O(p/K)K^\tau=O(pK^{\tau-1})$ normalized, and the at most $\ell$ simultaneous rounds cost $O(Vd^{\lambda'})$ each including basis changes, repair, padding and cleanup.",
            r"O(p/K)\,K^\tau=O(pK^{\tau-1})."),
        infer("S7.4",
            r"Setup at the at most $p^A$ recursion visits costs $p^{A+C}=o(Tp)$, per-record and per-line setup costs $O(dTp^{A+C}/r)=o(Tp)$ because $r$ exceeds every power of $p$, and exceptional repair streams cost $O(Vp^{A'}2^{-K})=o(V)$, all deterministic worst-case bounds.",
            r"This is a deterministic worst-case bound."),
        infer("S7.5",
            r"Each power is at most $1-2\kappa$ and any fixed power of $\log p$ is eventually at most $p^\kappa$, so the large-input bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$, and schoolbook multiplication below one fixed cutoff gives a single machine with worst-case time $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.",
            r"Any fixed power of $\log p$ is at most $p^\kappa$ eventually."),
    ],
    frm=["multiplication-algorithm", "parameter-choice", "chunk-swap", "simultaneous-butterfly-layer", "transform-layout", "ring-convolution", "resampling-no-sort", "crt-axis-map", "signed-kronecker-packing", "nlogn-subroutine", "schoolbook-multiplication-and-divide-and-conquer-multiplication", "big-o", "logarithms-floors-ceilings-and-powers-of-two"],
    page="cost-accounting",
    adds=[B("g_i", "cost margin", r"The amount $g_i$ by which the $i$-th dominant cost power falls below one, for $i=1,\dots,7$.")],
    salient=r"The smallest margin $g_2=\epsilon c(1-\tau)=2^{-75}\cdot2^{-56}\cdot2^{-50}=2^{-181}$ comes from the chunk exchanges of the transform layout, so the address-interchange saving, diluted by the tiny exponents $\epsilon$ and $c$, sets $\kappa$.")

# ---------------------------------------------------------------- root

root = show("S0",
    r"A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes outputs $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$ for every pair of $n$-bit inputs $x,y$ in worst-case time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.",
    r"Build two fast tape procedures (address-chunk interchange and simultaneous butterfly layers) from fixed linear networks with a rank saving, use them inside Harvey and van der Hoeven's Gaussian-resampling reduction of the digit convolution to synthetic polynomial transforms over $\mathbb C[y]/(y^r+1)$, recover the integer coefficients exactly, and bound every row of a cost table by $p^{1-2\kappa}$ times $Tp=\Theta(n)$.",
    (r"Transform-based multiplication scans $\Theta(n)$ bits at each of $\Theta(\log n)$ levels, so beating $n\log n$ requires saving on both data movement and butterfly arithmetic; the two tape procedures provide these savings and the reduction carries them into exact multiplication.",
     "explicit",
     r"Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$. We therefore need savings in both movement and arithmetic."),
    [A, Bstep, Cstep, Dstep, Estep, Fstep, Gstep],
    frm=["n-log-n-conjecture", "fixed-tape-model", "big-o", "turing-machine-tapes", "binary-representation-of-integers"],
    page="main-theorem",
    adds=[B("n", "input length", r"The number of bits of each of the two input integers.", "count"),
          B(r"\kappa", "saving exponent", r"The fixed exponent $\kappa=2^{-182}$ by which the logarithmic factor is reduced."),
          B("b", "digit width", r"The number $b=\lceil\log_2n\rceil$ of bits per radix digit.", "count"),
          B("p", "working precision", r"The number $p=6b$ of fractional bits of the fixed-point grid $2^{-p}\mathbb Z[i]$.", "count"),
          B("d", "axis count", r"The number $d=\lfloor b^\epsilon\rfloor$ of transform axes, which also bounds the chunks selected in one butterfly layer.", "count"),
          B("K", "chunk width", r"The number $K=\lfloor d^c\rfloor$ of address bits in each chunk of the transform layout.", "count"),
          B("r", "record length", r"The number $r=2^{\lceil(\log_2T)/d\rceil}$ of complex coefficients in a polynomial record.", "count"),
          B(r"\ell", "levels per axis", r"The number $\ell=\log_2r$ of butterfly levels on a full-length axis.", "count"),
          B("T", "padded size", r"The number of entries in the padded transform box, the power of two in $[4n/b,8n/b)$.", "count"),
          B("S", "source size", r"The number $S=\prod_is_i$ of entries on the distinct odd prime axes.", "count"),
          B("V", "logical volume", r"The number of stored data bits of the array an operation acts on.", "count"),
          B(r"\epsilon", "dimension exponent", r"The fixed exponent $\epsilon=2^{-75}$ with $d=\Theta(p^\epsilon)$."),
          B("c", "chunk exponent", r"The fixed exponent $c=2^{-56}$ with $K=\lfloor d^c\rfloor$."),
          B(r"\delta", "routine exponent", r"The fixed exponent $\delta=1/16$ in the costs $p^{1+\delta}$ of the quoted exponential and Gaussian routines."),
          B(r"\alpha", "Gaussian width", r"The resampling parameter $\alpha=\lceil(12d^2b)^{1/4}\rceil$."),
          B(r"\gamma", "resampling exponent", r"The exponent $\gamma=2d\alpha^2$ of the power of two by which resampling rescales the source transform.")],
    salient=r"The bound beats $n\log n$ by a strict power of the logarithm in the very multitape model of Schönhage and Strassen's conjecture, yet the saving exponent $\kappa=2^{-182}$ is astronomically small.")

answer = {"root": root}

# ---------------------------------------------------------------- checks
graph = json.load(open(ROOT + "/exegenius/graph.json"))
concepts = {c["id"]: c for c in graph["concepts"]}
order = """n-log-n-conjecture radix-digit-convolution triple-gadget bank-exchange-network fixed-tape-model nlogn-subroutine stream-arrays frames controlled-shifts bilinear-orthogonal subspace-labels triangular-factorization matrix-shear power-width-interchange chunk-swap packed-selected-bits negacyclic-ring signed-kronecker-packing fixed-point-disk-grid dft-cyclic-convolution multidim-transform crt-axis-map gaussian-resampling bluestein-chirp coefficient-twist synthetic-transform butterfly-layers phase-kernel-network simultaneous-butterfly-layer transform-layout ring-convolution resampling-no-sort chirp-permutation-cancel parameter-choice source-transform exact-recovery multiplication-algorithm cost-accounting main-theorem""".split()
pos = {p: i for i, p in enumerate(order)}

errors = []


def walk(n, path=()):
    yield path, n
    for c in n.get("children", []):
        yield from walk(c, path + (n,))


def tokens(latex):
    out = []
    i = 0
    while i < len(latex):
        ch = latex[i]
        if ch == "\\":
            j = i + 1
            if j < len(latex) and latex[j].isalpha():
                while j < len(latex) and latex[j].isalpha():
                    j += 1
                tok = latex[i:j]
            else:
                j = min(i + 2, len(latex))
                tok = latex[i:j]
        else:
            j = i + 1
            tok = ch
        if not (ch.isspace() or tok in ("\\,", "\\;", "\\:", "\\!", "\\ ", "~", "{", "}")):
            out.append(tok)
        i = j
    return out


def maths(text):
    parts = text.split("$")
    if len(parts) % 2 == 0:
        errors.append("unbalanced $ in: " + text[:80])
    return [parts[i] for i in range(1, len(parts), 2)]


def occurs(sym, mlist):
    w = tokens(sym)
    for m in mlist:
        t = tokens(m)
        for i in range(len(t) - len(w) + 1):
            if t[i:i + len(w)] == w:
                return True
    return False


ids = set()
pages = {}
last = None
for path, n in walk(root):
    if n["id"] in ids:
        errors.append("dup id " + n["id"])
    ids.add(n["id"])
    for q in ([n.get("quote")] if n.get("quote") else []) + ([n["motivation"]["quote"]] if n.get("motivation", {}).get("quote") else []):
        if norm(q["quote"]) not in SRCN:
            errors.append(f"quote not found ({n['id']}): {q['quote']}")
    if n["intention"] == "infer" and not n.get("deferred"):
        at = SRCN.find(norm(n["quote"]["quote"]))
        if at >= 0:
            if last and at < last[0]:
                errors.append(f"order: {n['id']} before {last[1]}")
            last = (at, n["id"])
    pg = n.get("page")
    if pg:
        if pg not in pos:
            errors.append("bad page " + pg)
        if pg in pages:
            errors.append(f"page {pg} twice: {pages[pg]} {n['id']}")
        pages[pg] = n["id"]
        for a in path:
            if a.get("page") and pos[a["page"]] < pos[pg]:
                errors.append(f"warning: {n['id']} page {pg} after ancestor page {a['page']}")
    mypage = next((a.get("page") for a in ((n,) + tuple(reversed(path))) if a.get("page")), None)
    for f in n.get("from", []):
        c = concepts.get(f)
        if c is None:
            errors.append(f"{n['id']}: unknown concept {f}")
        elif c.get("known"):
            pass
        elif f not in pos:
            errors.append(f"{n['id']}: {f} not a page")
        elif pos[f] >= pos[mypage]:
            errors.append(f"{n['id']}: from {f} not before {mypage}")
    below = [m for _, d in walk(n) for m in maths(d["claim"])]
    for b in n.get("adds", []):
        if not occurs(b["symbol"], below):
            errors.append(f"{n['id']}: adds {b['symbol']} not below")
        if not (1 <= len(b["name"].split()) <= 4):
            errors.append(f"{n['id']}: name words {b['name']}")
    for fld in ("claim",):
        maths(n[fld])
    if n.get("motivation"):
        maths(n["motivation"]["text"])
    if n.get("method"):
        maths(n["method"])
    if n.get("salient"):
        maths(n["salient"])

used = set()
for _, n in walk(root):
    if n.get("page"):
        used.add(n["page"])
    used.update(n.get("from", []))
unused = [p for p in order if p not in used]
if unused:
    errors.append("unused pages: " + ", ".join(unused))

print("\n".join(errors) if errors else "OK")
print("nodes:", len(list(walk(root))), "pages with steps:", len(pages))
json.dump(answer, open(ROOT + "/exegenius/tasks/0003-argument.answer.json", "w"), ensure_ascii=False, indent=1)
