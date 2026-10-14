"""S1: the address chunk interchange (the key step's subtree)."""
from tree_helpers import show, infer, mot, bind

# ---------------------------------------------------------------- S1.1.1.1
S1111 = show(
    "S1.1.1.1",
    r"For arbitrary initial values on its auxiliary wires, a forward invocation of the eight-row schedule adds each source value to its target ($y\gets y+x$) and leaves every other value unchanged, so a forward stage, an inverse stage with the banks' roles exchanged and a forward stage send $(X_a,Y_a)\mapsto(-Y_a,X_a)$ and restore every auxiliary wire; over $\mathbb F_2$ this is the exchange of the two banks.",
    r"First subtract the effect of the old scratch values, then copy and gather the sources into scratch, scatter and side-inject the scratch into the targets, and finally undo the copy and gather; check the net coefficient between two triples by the size of their intersection.",
    mot(r"The scratch wires must be allowed to hold arbitrary values, because on tape their roles are filled by ordinary data rows; subtracting their old contribution first and restoring them last leaves a net linear map that does not depend on them.",
        "explicit",
        r"The first two rows of the following schedule remove the effect of the old scratch values; the next four introduce the source values and add their effect to the target; the last two restore the scratch values."),
    [
        infer("S1.1.1.1.1",
              r"With copy $\mathcal V$, gather $\mathcal G$, side injection $\mathcal J$ and scatter $\mathcal R$, and initial side and central scratch vectors $a,c$, the first two rows subtract $\mathcal Ja+\mathcal Rc$ from the targets, the middle rows add $\mathcal R(c+\mathcal Gx)+\mathcal J(a+\mathcal Vx)$, and the last two rows restore $a,c$, so the targets change by $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$ whatever $a,c$ are.",
              r"The net target change is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of $a,c$."),
        infer("S1.1.1.1.2",
              r"In the bit network the gather-then-scatter coefficient from a source triple to a target triple is the size of their intersection modulo $2$, the side wires cancel exactly the pairs of triples meeting in one point, distinct triples meeting in zero or two points already get $0$, and a triple with itself gets $3\equiv1$, so the net map is $y\gets y+x$.",
              r"In the bit case, the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod2$."),
        infer("S1.1.1.1.3",
              r"Starting from $(x,y)$, the three stages give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$, and each invocation restores its own auxiliary wires.",
              r"Starting from $(x,y)$, the three stages give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$."),
    ],
    page="scratch-restoring-exchange",
    frm=["sets-subsets-and-cartesian-products", "arithmetic-modulo-2-and-xor", "matrices-vectors-and-linear-maps"],
    salient=r"The exchange is exact whatever values the scratch wires start with, and every scratch wire ends with its initial value.",
)

# ---------------------------------------------------------------- S1.1.1.2
S1112 = show(
    "S1.1.1.2",
    r"If every scalar is replaced by an array on a common address set, every gate acts pointwise, and each source, gate or sink $v$ carries an invertible linear frame $D_v$, with $D_vD_u^{-1}$ applied on an edge from $u$ to $v$, then the network implements $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$, so a route from input role $w$ to output role $\rho(w)$ applies only $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$.",
    r"Maintain the invariant that the stored array at each vertex is its frame applied to the logical array there, using the linearity of each gate across the wires it touches.",
    mot(r"Because only the endpoint frames affect the result, the intermediate frames are free choices, and they can be chosen so that every edge's change of frame is cheap to perform on tape.",
        "explicit",
        r"Once the scalar routing is fixed, the endpoint frames determine the array operator on each route; the intermediate frames can then be chosen to make each edge change inexpensive."),
    [
        infer("S1.1.1.2.1",
              r"The invariant holds at the sources by definition: a supplied physical input $f$ is interpreted as the logical array $g=D_{\rm in}^{-1}f$, which needs no physical preprocessing.",
              r"For a supplied physical input $f$, define its logical interpretation to be $g=D_{\rm in}^{-1}f$; this definition requires no physical preprocessing."),
        infer("S1.1.1.2.2",
              r"An edge changes $D_u\varphi$ into $D_v\varphi$, and at a gate whose wires share the frame $D_v$ linearity gives $\sum_jc_jD_v\varphi_j=D_v(\sum_jc_j\varphi_j)$, so the frame commutes with the pointwise gate and the invariant reaches the sinks.",
              r"Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks."),
        infer("S1.1.1.2.3",
              r"Hence, when the scalar network is a signed role permutation sending role $w$ to $\rho(w)$ with sign $\varepsilon_w$, that route applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$, for every role, auxiliary roles included.",
              r"that route applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))} D_{\mathrm{source}(w)}^{-1}$ to its input array."),
    ],
    page="array-frames",
    frm=["matrices-vectors-and-linear-maps", "permutations-and-bijections", "tape-address-model", "scratch-restoring-exchange"],
    salient=r"All intermediate frames cancel: whatever they are, each route's operator depends only on its source and sink frames.",
)

# ---------------------------------------------------------------- S1.1.1.3
S1113 = show(
    "S1.1.1.3",
    r"Labels can be attached so that every edge joins nested nondegenerate subspaces, the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$, and the absolute dimension changes sum to $Wm-2N+2L$ with $L=Ich$; for the bit network $L_{\rm b}/N=100/539<1/2$.",
    r"Use indicator vectors of triples under a bilinear form that makes neighboring triples orthogonal, expose one tensor factor of $\mathcal F=F^{\otimes3}$ per stage, order the gates so that every decrease falls on one central edge, and telescope the signed changes at the gates.",
    mot(r"Orthogonal neighboring triple lines let a side wire's label pass from one triple's line into the other triple's orthogonal complement without shrinking, so the only losses are the central wires' returns, whose total $Ich$ is the fixed fraction $100/539$ of $N$.",
        "explicit",
        r"Orthogonality of the corresponding indicator vectors permits the subspace assignments."),
    [
        infer("S1.1.1.3.1",
              r"Under the form $\langle x,y\rangle=x^{\mathsf T}(I-J/9)y$ on $F=\mathbb Q^h$ with $h=100$, triple indicators satisfy $\langle t_S,t_{S'}\rangle=|S\cap S'|-1$ and $\langle t_S,t_S\rangle=2$, so every triple line is nondegenerate and triples meeting in one point span orthogonal lines.",
              r"Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label field belonging to either construction."),
        infer("S1.1.1.3.2",
              r"Each stage exposes one tensor factor: the labels leaving stage $j$ on the data wires are exactly those entering stage $j+1$, starting from $U_a=\langle u_a\rangle$ on $X_a$ and $0$ on $Y_a$ and ending at $\mathcal F$ on $X_a$ and $U_a^\perp$ on $Y_a$, as the terminals prescribe.",
              r"These transitions expose one tensor factor at each stage."),
        infer("S1.1.1.3.3",
              r"On a side wire joining neighboring triples with indicators $t_X,t_Y$, the label grows from $(B\otimes F)\perp(P\otimes\langle t_X\rangle)$ at time 2 to $(B\otimes F)\perp(P\otimes t_Y^\perp)$ at time 5, an inclusion only because $t_X\perp t_Y$.",
              r"The side edge $2\to5$ uses the neighbor relation essentially."),
        infer("S1.1.1.3.4",
              r"With the time-ordered gate labels, every edge joins comparable nondegenerate labels and dimension decreases only on the central-wire edges from time 3 to time 4, which remove $P\otimes F\otimes Q$ of dimension $h$; with $I=3v^2$ invocations of $c$ central wires each, the total loss is $L=Ich$.",
              r"Label dimension is nondecreasing along every edge except center $3\to4$, which removes $P\otimes F\otimes Q$."),
        infer("S1.1.1.3.5",
              r"Each touched wire has one incoming and one outgoing incidence with the same gate label, so the signed changes telescope to the sink total $Wm-N$ minus the source total $N$, and counting absolute instead of signed changes adds $2L$, giving $Wm-2N+2L$.",
              r"The signed sum of dimension changes telescopes at every gate: each touched wire has one incoming and one outgoing incidence with the same gate label."),
        infer("S1.1.1.3.6",
              r"For the bit network, with $c_{\rm b}=100$ central wires per invocation, the exact loss ratio is $L_{\rm b}/N=100/539<1/2$.",
              r"In particular, both are smaller than $1/2$."),
    ],
    frm=["rank-and-orthogonal-subspaces", "dot-product-inner-product-and-orthogonality", "sets-subsets-and-cartesian-products"],
)

# ---------------------------------------------------------------- S1.1.1.4
S1114 = show(
    "S1.1.1.4",
    r"Assigning $P_U$ to each gate and sink with label $U$, $-P_{U_a}$ to the source $X_a$ and $0$ to the other sources gives edge differences of total rational rank $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$, short of $W_{\rm b}m$ by $N-2L_{\rm b}>0$, and endpoint differences equal to $I_m$ on every role.",
    r"Compute the rank of a difference of projections onto nested labels, then account separately for the negative source projections that make every endpoint difference the identity.",
    mot(r"Projections turn the label budget into a rank budget, since a projection difference between nested labels has rank equal to the dimension change; the negative source projections, needed to make every endpoint difference $I_m$, cost $N$ extra ranks, which $L<N/2$ still covers.",
        "explicit",
        r"The rational interface below will require an additional $N$ source ranks, so this inequality will leave a strict saving in both constructions."),
    [
        infer("S1.1.1.4.1",
              r"For nested nondegenerate labels $U\subset V$, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement, so its rank equals the dimension change $\dim V-\dim U$; a decreasing edge only negates the matrix.",
              r"Its rank is $\dim V-\dim U$; reversing the edge negates the matrix without changing its rank."),
        infer("S1.1.1.4.2",
              r"The only exceptions are the $N$ negative source projections: at stage 1 the first gate on $X_a$ has label exactly $U_a$, so that edge's matrix is $P_{U_a}-(-P_{U_a})=2P_{U_a}$, of rank one although the dimension does not change, which adds $N$ to the rank sum.",
              r"Its first edge matrix is therefore $2P_{U_a}$, of rational rank one, where the corresponding dimension change was zero."),
        infer("S1.1.1.4.3",
              r"Hence $s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N=W_{\rm b}m-N+2L_{\rm b}$, which falls short of $W_{\rm b}m$ by $N-2L_{\rm b}>0$ because $L_{\rm b}/N<1/2$.",
              r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$."),
        infer("S1.1.1.4.4",
              r"On the route $X_a\to Y_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$, and every other route runs from a zero source matrix to the identity sink matrix $P_{\mathcal F}$, so $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ for every role $w$.",
              r"For an input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$."),
    ],
    frm=["rank-and-orthogonal-subspaces", "matrices-vectors-and-linear-maps", "array-frames"],
)

# ---------------------------------------------------------------- S1.1.1
S111 = show(
    "S1.1.1",
    r"With the projection $P_U$ onto its label $U$ (along $U^\perp$) at every gate and sink, $-P_{U_a}$ at each source $X_a$ and $0$ at every other source, the bit network on $W_{\rm b}$ wires realizes the role permutation $\rho$ exchanging the banks $X_a$ and $Y_a$, satisfies $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ for every role $w$, and has edge differences whose rational ranks sum to $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.",
    r"Build a bank-exchange network from copy, gather, scatter and side-injection gates indexed by three-element subsets of a 100-point set; attach to its gates and terminals nested nondegenerate subspaces of $(\mathbb Q^{100})^{\otimes3}$ built from triple indicator vectors, so that label dimension falls on only one kind of edge; and turn dimension changes into ranks of projection differences.",
    mot(r"An edge's frame change costs as many recursive calls as the rank of its matrix, and between nested labels that rank is the dimension change; since the changes must add up to $Wm-2N$ plus twice the dimension $L$ lost on decreasing edges, keeping $L<N/2$ leaves the total below $Wm$ even after $N$ extra source ranks.",
        "explicit",
        r"The saving will come from keeping the total dimension lost on decreasing edges small relative to $N$."),
    [S1111, S1112, S1113, S1114],
    page="subset-intersection-labels",
    frm=["rank-and-orthogonal-subspaces", "sets-subsets-and-cartesian-products", "matrices-vectors-and-linear-maps", "dot-product-inner-product-and-orthogonality"],
    adds=[
        bind("N", "bank size", r"The number of values in each of the two data banks, $\binom{100}{3}^3$.", "count"),
        bind("L", "dimension loss", "The total label dimension lost along the edges on which labels shrink.", "count"),
        bind("h", "ground set size", "The number of points, 100, from which the three-element subsets (triples) are drawn.", "count"),
    ],
)

# ---------------------------------------------------------------- S1.1.2
S112 = show(
    "S1.1.2",
    r"For a fixed rational $m\times m$ matrix $A$ of rank $a$ and a fixed odd prime $q$ avoiding the denominators of its factors, the address permutation $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ can be performed with exactly $a$ interchanges of pairs of $b$-digit fields, each between an $H$ field and a $D$ field, plus $O(V)$ further work.",
    r"Factor $A=E_1\Pi E_2$ with invertible lower-triangular $E_1,E_2$ and a partial permutation $\Pi$ with $a$ ones; apply the triangular factors as controlled shifts that update later fields from earlier ones, and realize each one of $\Pi$ by a single field interchange between two such updates.",
    mot(r"Tape order makes it cheap to update a later field from earlier ones (a controlled shift in linear time), so a factorization whose invertible parts are lower triangular leaves only the rank-$a$ partial permutation to be done by genuine interchanges.",
        "explicit",
        r"Lemma~\ref{lem:ordered-affine-streams} updates a later field using earlier fields in linear time.  Lower triangular changes of coordinates can be performed entirely in this direction."),
    [
        infer("S1.1.2.1",
              r"Every rational $A$ of rank $a$ factors as $A=E_1\Pi E_2$: elimination takes the topmost nonzero row and its rightmost nonzero entry as pivot, clears with lower-triangular row and column operations, and isolates one rank-one block per pivot, so $\Pi$ has exactly $a$ ones (for $A=0$, $\Pi=0$ and $E_1=E_2=I$).",
              r"Thus the final partial permutation matrix has exactly $a$ ones."),
        infer("S1.1.2.2",
              r"Choosing once a fixed odd prime $q$ that avoids every denominator, and every diagonal numerator of the invertible factors, in the finite table of factors and inverses, all these identities hold over $\mathbb Z/q^b\mathbb Z$ with invertible triangular factors.",
              r"All these rational identities then specialize to $\mathbb Z/q^b\mathbb Z$, and the triangular factors remain invertible there."),
        infer("S1.1.2.3",
              r"A lower-triangular change of $H$ or of $D$ costs $O(V)$: updating coordinates in descending physical order, each is multiplied by a unit and increased by a fixed combination of earlier, still original coordinates, which is a controlled shift.",
              r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$: update coordinates in descending physical order."),
        infer("S1.1.2.4",
              r"After $D$ is transformed by $E_2$ and $H$ by $E_1^{-1}$, each one of $\Pi$ at $(i,j)$ asks for $H_i\gets H_i+D_j$, done as $D_j\gets D_j+H_i$, an interchange of $H_i$ and $D_j$, and $D_j\gets H_i-D_j$, which takes $(h,d)$ to $(h+d,d)$; undoing the triangular transforms then gives $H+AD$.",
              r"On an initial pair $(h,d)$ this sequence yields $(h+d,d)$."),
        infer("S1.1.2.5",
              r"Since $\Pi$ has exactly $a$ ones, the number of recursive interchanges is exactly the rational rank $a$; the temporary tapes of the other operations do not multiply that count.",
              r"In particular, the number of recursive calls is the rational rank $a$; temporary tapes used for the other operations do not multiply that count."),
    ],
    page="address-shear-factorization",
    frm=["controlled-cyclic-shift", "triangular-and-permutation-matrices", "matrices-vectors-and-linear-maps", "modular-arithmetic", "primes-coprimality-and-gcd"],
    adds=[
        bind("a", "matrix rank", r"The rational rank of the matrix $A$, which is the number of field interchanges the shear needs.", "count"),
        bind(r"\Pi", "partial permutation", r"A 0-1 matrix with exactly $a$ ones, at most one in each row and column.", "direct"),
    ],
)

# ---------------------------------------------------------------- S1.1.3
S113 = show(
    "S1.1.3",
    r"Splitting whole rows cyclically into $W$ role streams of volume $V/W$, executing each gate pointwise and applying on each network edge the address shear given by its matrix difference performs $H\gets H+D$ on every original row, including rows that served as scratch roles, and two linear-cost updates turn this shear into the interchange $(H,D)\mapsto(D,H)$.",
    r"Use the address shears $\Phi_M:(H,D)\mapsto(H+MD,D)$ as frames in the frame identity, and merge the output rows back by undoing the role permutation.",
    mot(r"Address shears compose additively ($\Phi_{M'}\Phi_M=\Phi_{M'+M}$) and, being address permutations, commute with pointwise XOR gates, so the frame identity applies; the endpoint condition then makes every route apply $\Phi_{I_m}$, the same shear on every role.",
        "recoverable"),
    [
        infer("S1.1.3.1",
              r"Writing the row number as $Wg+(w-1)$ and sending the row to stream $w$ gives $W$ streams with the same remaining shape, including the full ranges of $H$ and $D$, each of volume $V/W$ and with row count divisible by $W^{k-1}$.",
              r"Each has logical volume $V/W$, and its row count is divisible by $W^{k-1}$."),
        infer("S1.1.3.2",
              r"With frame $\Phi_M$ at a vertex whose matrix is $M$, each edge changes the frame by $\Phi$ of its matrix difference, and the frame invariant holds because a common address permutation commutes with every pointwise bit gate.",
              r"The same invariant proof applies because a common address permutation commutes with every pointwise bit gate."),
        infer("S1.1.3.3",
              r"By the endpoint condition, input $f_w$ leaves at role $\rho(w)$ as $\Phi_{M_{\mathrm{out}(\rho(w))}}\Phi_{-M_{\mathrm{in}(w)}}f_w=\Phi_{I_m}f_w$, and returning row $g$ of role $\rho(w)$ to row $Wg+(w-1)$ undoes $\rho$, so every original row, scratch rows with arbitrary contents included, has undergone $H\gets H+D$.",
              r"The result is $H\leftarrow H+D$ on every original row, including rows assigned to scratch roles, whose initial values were arbitrary."),
        infer("S1.1.3.4",
              r"The componentwise updates $D\gets D-H$, $H\gets H+D$, $D\gets H-D$ send $(H,D)$ to $(D,H)$; only the middle shear uses the network, and the outer two update the later group at linear cost.",
              r"The transformation sends $(H,D)$ to $(D,H)$."),
    ],
    frm=["array-frames", "scratch-restoring-exchange", "tape-address-model", "permutations-and-bijections"],
)

# ---------------------------------------------------------------- S1.1.4
S114 = show(
    "S1.1.4",
    r"If $F_k$ bounds the time per stored bit for chunks of $m^k$ digits, the $s$ recursive calls on streams of volume $V/W$ give $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$, and since $s_{\rm b}/W_{\rm b}<m^\tau$ for $\tau=1-2^{-50}$, $F_k=O(m^{k\tau})=O(e^\tau)$.",
    r"Count the recursive calls (the rank sum $s$) and their volumes ($V/W$ each), divide the cost by the volume, and sum the resulting geometric series using the explicit rank deficit.",
    mot(r"After division by volume each recursion level multiplies the cost by $s/W$ while the width grows by the factor $m$; because $s/W<m$, this multiplier is $m^\tau$ for a fixed $\tau<1$, so the total grows like $e^\tau$ instead of $e$.",
        "explicit",
        r"This strict inequality is the source of the power saving."),
    [
        infer("S1.1.4.1",
              r"The recursive calls number exactly the rank sum $s$, each acting on one role stream of volume $V/W$ and on fields of $m^{k-1}$ digits, while splitting, merging, gates and triangular updates are a fixed number of $O(V)$ operations.",
              r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
        infer("S1.1.4.2",
              r"Dividing the time by $V$ gives $F_0=O(1)$, since a single digit pair is interchanged by one elementary scan, and $F_k\le(s/W)F_{k-1}+O(1)$.",
              r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1).",
              frm=["tape-address-model"]),
        infer("S1.1.4.3",
              r"The relative deficit $\eta_{\rm b}=(W_{\rm b}m-s_{\rm b})/(W_{\rm b}m)=339/22587335000000$ exceeds $20\cdot2^{-50}$ and $\log m<20$, so $m^{1-2^{-50}}=m\exp(-2^{-50}\log m)>m(1-20\cdot2^{-50})>m(1-\eta_{\rm b})=s_{\rm b}/W_{\rm b}$.",
              r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$.",
              deferred=True),
        infer("S1.1.4.4",
              r"With $s/W<m^\tau$ the geometric sum $\sum_{j\le k}(s/W)^j$ is $O(m^{k\tau})$, whether $s/W\le1$ (at most $k+1$ terms) or $s/W>1$ (dominated by its last term), hence $F_k=O(e^\tau)$.",
              r"Hence $F_k=O(e^\tau)$."),
    ],
    page="rank-saving-recurrence",
    frm=["divide-and-conquer-and-recurrences", "geometric-series-and-sums", "exponential-logarithm-and-gaussian-function"],
    adds=[
        bind("F_k", "normalized cost", r"The worst-case time divided by the logical volume for interchanging chunks of $m^k$ digits.", "direct"),
    ],
)

# ---------------------------------------------------------------- S1.1.5
S115 = show(
    "S1.1.5",
    r"The recursion runs depth first on one fixed set of tapes ($W$ role tapes, a parking stack and a descriptor stack), and parking the inactive role streams, copying the active one and descriptor work cost $O(V)$ at each node, so temporary storage does not enter the factor $s/W$.",
    r"Park the inactive role streams on a stack so that the same role and work tapes serve every depth, charge every copy and erasure to the current node's volume, and bound descriptor work at a child by a fixed power of $\log V$.",
    mot(r"A fixed machine has a fixed number of tapes, so the $W$ role streams of all recursion levels must share them; parking on a stack keeps each node's copying proportional to its own volume, so the overhead stays $O(V)$ per node and the recurrence keeps its factor $s/W$.",
        "recoverable"),
    [
        infer("S1.1.5.1",
              r"Before a child call the $W-1$ inactive role streams are pushed on the parking stack and the active one is copied to the child's input area; on return they are popped in reverse order, so no scan passes through a parked ancestor.",
              r"No scan passes through a parked ancestor."),
        infer("S1.1.5.2",
              r"Each push, pop, copy, positioning and erasure moves $O(V)$ symbols at the parent and there are only $s$ children, so scheduling adds $O(V)$ per node although each child has volume $V/W$.",
              r"This gives precisely the additional $O(V)$ term claimed above, even though each child itself has volume $V/W$."),
        infer("S1.1.5.3",
              r"Both original chunk ranges stay present as spectators, so a child at depth $j$ has volume $V_j\ge q^{2e_0}$ and $\log V_0=O(\log V_j)$, and descriptor work $(\log V_0)^{O(1)}$ is $O(V_j)$ at every child, even for one-bit payloads.",
              r"It follows that $\log V_0=\log V_j+j\log W=O(\log(2V_j))$."),
    ],
    frm=["tape-address-model", "multitape-turing-machine", "subroutines-and-composition-of-algorithms"],
)

# ---------------------------------------------------------------- S1.1
S11 = show(
    "S1.1",
    r"For every $e=m^k$, two disjoint chunks of $e$ radix-$q$ digits each, preceded by a row field whose length is divisible by $W^k$, can be interchanged in $O(Ve^\tau)$ time with $\tau=1-2^{-50}$, preserving every other address field.",
    r"Split each chunk into $m$ fields of $b=e/m$ digits ($H$ and $D$), obtain the shear $H\gets H+D$ by running the fixed bit network pointwise on $W$ row streams whose frames are address shears, implement each edge's frame change by as many recursive $b$-digit interchanges as its rational rank, convert the shear into the interchange with two linear-cost updates, and solve the volume-normalized recurrence.",
    mot(r"Splitting rows among the $W$ roles makes every recursive call act on a $1/W$ share of the volume, while the network needs only $s<Wm$ calls on fields $m$ times narrower; per stored bit, multiplying the width by $m$ multiplies the recursive cost by $s/W<m$, which compounds into a power saving.",
        "explicit",
        r"After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$."),
    [S111, S112, S113, S114, S115],
    page="power-width-interchange",
    frm=["tape-address-model", "divide-and-conquer-and-recurrences", "matrices-vectors-and-linear-maps", "modular-arithmetic"],
    salient=r"A strict inequality $s<Wm$ is all the saving needs, and here it is extremely thin (the relative deficit is $339/22587335000000$), yet it already gives cost $e^\tau$ per stored bit with a fixed $\tau<1$ instead of $e$.",
    adds=[
        bind("s", "rank sum", "The total rational rank of the network's edge matrices, which is the number of recursive calls made at one level.", "count"),
        bind("b", "field width", r"The number of digits in each of the $m$ fields of a chunk, $e/m$.", "count"),
        bind("H", "first chunk", r"The first chunk read as a vector of $m$ fields over $\mathbb Z/q^b\mathbb Z$.", "direct"),
        bind("D", "second chunk", r"The second chunk read as a vector of $m$ fields over $\mathbb Z/q^b\mathbb Z$.", "direct"),
        bind(r"\rho", "role permutation", r"The permutation of wire roles realized by the network, exchanging $X_a$ and $Y_a$ and fixing every scratch role.", "direct"),
    ],
)

# ---------------------------------------------------------------- S1.2 - S1.4
S12 = infer(
    "S1.2",
    r"For a general width $e$, interchanging the top $O(\log e)$ digits of the two chunks pair by pair and joining them in front of the remaining parts creates a row field of range at least $W^k$ before both remaining chunks, which zero rows pad to a multiple of $W^k$, at cost $O(V\log e)$ and with padded volume below $2V$.",
    r"Exchanging and joining the high parts costs $O(V\rho)$ by Lemma~\ref{lem:elementary-streams}.",
    frm=["tape-address-model", "power-width-interchange"],
)
S13 = infer(
    "S1.3",
    r"Writing the remaining width as $\sum_ja_jm^j$ with $0\le a_j<m$ and interchanging the corresponding pieces of width $m^j$ by the power-width procedure costs $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$, and since every call preserves row addresses the padded rows stay zero and are scanned away afterwards.",
    r"The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a geometric sum of the stated order.",
    frm=["geometric-series-and-sums", "positional-notation-in-any-radix", "power-width-interchange"],
)
S14 = infer(
    "S1.4",
    r"For binary chunks, padding each range $[2^u]$ numerically to $[q^e]$ with $q^e\ge2^u$ minimal multiplies the volume by less than $q^2$, keeps the order of the existing entries, and has $e=O(u)$, so interchanging $u$-bit chunks costs $O(Vu^\tau)$.",
    r"Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$.",
    frm=["binary-numerals-and-bit-strings", "positional-notation-in-any-radix"],
)

# ---------------------------------------------------------------- S1
S1 = show(
    "S1",
    r"For a fixed $\tau<1$, two disjoint contiguous address fields of $u$ bits each, in an array of logical volume $V$ with arbitrary prefix, gap and suffix fields, can be interchanged in $O(Vu^\tau)$ time on a fixed number of tapes.",
    r"Prove the bound for chunks of $m^k$ radix-$q$ digits preceded by enough rows, by recursion on a fixed bit network, then reduce every width to that case by borrowing a few high digits as rows, splitting the rest into base-$m$ pieces, and padding binary ranges to powers of $q$.",
    mot(r"Each edge matrix of rank $a$ costs $a$ smaller interchanges, and the ranks of the bit network sum to less than its wire count times $m$; since each smaller interchange acts on a $1/W$ share of the rows, the recursion saves a power of the chunk width instead of paying one pass per digit.",
        "explicit",
        r"Because the sum of these ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width."),
    [S11, S12, S13, S14],
    page="address-chunk-interchange",
    frm=["tape-address-model", "multitape-turing-machine", "binary-numerals-and-bit-strings", "multidimensional-arrays-and-row-major-order"],
    salient=r"The final effect is an exact permutation of addresses, yet the procedure beats moving the $u$ bits one at a time ($O(Vu)$) because its intermediate streams are XOR combinations of data; it is exact for arbitrary initial auxiliary values.",
    adds=[
        bind("u", "chunk width", "The number of bits in each of the two interchanged address fields.", "count"),
        bind(r"\tau", "interchange exponent", r"The fixed exponent below one, $1-2^{-50}$, in the interchange cost.", "direct"),
        bind("e", "chunk digits", r"The number of radix-$q$ digits in each chunk, equal to $m^k$ in the power-width case.", "count"),
        bind("m", "label dimension", r"The dimension $10^6$ of the network's label space, which is also the number of fields each chunk is split into.", "count"),
        bind("q", "prime radix", r"The fixed odd prime used as the radix of address digits, chosen so that the network's rational matrices make sense modulo $q^b$.", "direct"),
        bind("W", "wire count", "The number of wires, or roles, of the fixed bit network.", "count"),
        bind("k", "recursion level", r"The exponent with $e=m^k$, which is the depth of the recursion.", "count"),
    ],
)
