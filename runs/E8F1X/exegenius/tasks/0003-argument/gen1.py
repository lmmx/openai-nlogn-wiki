# Part 1: helpers and branches S1 (chunk interchange)
import json, re, sys

def ev(q): return {"source": "paper", "quote": q}

def infer(id, claim, quote, page=None, frm=None, deferred=False, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote)}
    if page: n["page"] = page
    if frm: n["from"] = frm
    if deferred: n["deferred"] = True
    if salient: n["salient"] = salient
    return n

def show(id, claim, method, motiv, children, page=None, frm=None, adds=None, salient=None):
    # motiv = (source, text, quote or None)
    src, text, q = motiv
    m = {"text": text, "source": src}
    if q: m["quote"] = ev(q)
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": m, "children": children}
    if page: n["page"] = page
    if frm: n["from"] = frm
    if adds: n["adds"] = adds
    if salient: n["salient"] = salient
    return n

def add(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

# ---------------------------------------------------------------- S1 branch
network = show(
 "N0",
 r"A fixed linear network on the data wires and extra scratch wires sends $(X_a,Y_a)$ to $(-Y_a,X_a)$ (a plain swap of the two banks over $\mathbb F_2$) and returns every scratch wire to its arbitrary initial value.",
 r"Build the exchange from three stages, each a forward invocation $y_S\leftarrow y_S+x_S$ that first subtracts the effect of the unknown scratch values, then adds the source's effect through copy, gather, scatter and side-injection gates, then restores the scratch values; chain the stages as $(x,y)\to(x,y+x)\to(-y,y+x)\to(-y,x)$.",
 ("explicit", "A swap needs nothing to be remembered between invocations, so the unknown scratch values are cancelled by subtracting their effect first and adding it back at the end, as in transparent computation.", r"This cancellation of arbitrary initial scratch values is a linear"),
 [
  infer("N0.1", r"If the scratch (side and central) vectors start at arbitrary values $a,c$, the eight-row schedule changes the target by $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, a quantity that does not depend on $a,c$.",
        r"Rows 6 and 7 restore $c,a$.  The net target change is"),
  infer("N0.2", r"In the bit construction the net coefficient from $x_T$ to $y_S$ is one for $T=S$ and zero otherwise: the central part gives $|S\cap T|\bmod 2$, the side injection cancels exactly the intersection-one cases, and distinct triples meeting in zero or two elements already have coefficient zero.",
        r"$|S\cap T|\bmod2$.  The side contribution cancels exactly the"),
  infer("N0.3", r"In the complex construction the central coefficient is $(|S\cap T|-1)/2$; the side injection cancels it for distinct triples meeting in zero or two elements, intersection one contributes zero, and the self coefficient is one.",
        r"In the complex case, the central coefficient is $(|S\cap T|-1)/2$."),
  infer("N0.4", r"Performing a forward invocation from $X$ to $Y$ at stage 1, the inverse schedule from $Y$ to $X$ at stage 2, and a forward invocation at stage 3 gives $(x,y)\to(x,y+x)\to(-y,y+x)\to(-y,x)$, with every scratch wire restored.",
        r"Starting from $(x,y)$, the three stages give"),
 ],
 page="network",
 frm=["binary-field-f2-and-xor","boolean-gates-and-circuits","sets-subsets-and-basic-combinatorics"],
 salient=r"The net change of the target is independent of the initial values on all scratch wires, so the exchange works with whatever those wires happen to hold.")

frames = show(
 "F0",
 r"If the array on each wire is stored through an invertible operator (a frame) $D_v$ at every vertex $v$, with all incidences of a gate sharing one frame, then the whole network acts as $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$: only the endpoint frames matter, and each edge merely changes the frame by $D_vD_u^{-1}$.",
 r"Maintain the invariant that the stored array at each vertex equals the frame applied to the logical array; it holds at the sources by definition, along edges by the choice of edge operator, and across gates because a common frame commutes with a pointwise linear gate.",
 ("explicit", "Once the routing is fixed only the endpoint frames matter, so the intermediate frames are free to be chosen to make each edge change cheap.", r"intermediate frames can then be chosen to make each edge change inexpensive."),
 [
  infer("F0.1", r"At a vertex the stored array equals $D_v$ applied to the logical array; this holds at the sources by defining the logical input to be $D_{\rm in}^{-1}f$, so no physical preprocessing is needed.",
        r"At a vertex $v$, the invariant is that the stored array equals $D_v$ applied"),
  infer("F0.2", r"At a pointwise linear gate $G$ the common frame commutes with the gate, $G(D_vg_1,\ldots,D_vg_t)=D_vG(g_1,\ldots,g_t)$, so the invariant continues through every gate.",
        r"Thus the common frame commutes with the pointwise gate, and"),
  infer("F0.3", r"The implemented operator on the vector of wire arrays is $D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}$, so every intermediate frame cancels.",
        r"the invariant continues to the sinks.  The implemented operator is therefore"),
  infer("F0.4", r"For a signed role permutation, the route from input role $w$ to output role $\rho(w)$ applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ to its array, on scratch roles as well.",
        r"sends input role $w$ to output role $\rho(w)$ with scalar sign"),
 ],
 page="frames",
 frm=["vectors-matrices-and-linear-maps","functions-bijections-and-permutations","graphs"],
 salient=r"Intermediate frames cancel completely: the result depends only on the frames at the sources and sinks, whatever frames are used in between.")

labels = show(
 "L0",
 r"Every gate and terminal of the network can be given a nondegenerate subspace label of the cube space $\mathcal F=F^{\otimes3}$ of dimension $m=h^3$, built from indicator vectors of three-element subsets, so that labels along every edge are nested, neighboring triples have orthogonal lines, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing $h$ dimensions.",
 r"Take indicator vectors $t_T$ of triples with the pairing $\langle t_S,t_T\rangle=|S\cap T|-1$ over $\mathbb Q$ or the dot product over $\mathbb F_2$, tensor three copies, and define the labels stage by stage through orthogonal complements $B=P^\perp$ so that each stage exposes one tensor factor; then read every edge's orthogonal residual from a table.",
 ("explicit", "The subspace assignment needs the lines of neighboring triples to be orthogonal, which the intersection-size pairings supply.", r"Orthogonality of the corresponding indicator vectors permits"),
 [
  infer("L0.1", r"Over $\mathbb Q$ with the form $x^{\mathsf T}(I-J/9)y$ one has $\langle t_S,t_T\rangle=|S\cap T|-1$, and over $\mathbb F_2$ the dot product gives $|S\cap T|\bmod2$; so every triple line is nondegenerate and neighboring triple lines are orthogonal in the label field of either construction.",
        r"are orthogonal, in the label field belonging to either construction."),
  infer("L0.2", r"The prescribed incoming and outgoing labels of the $X$ and $Y$ wires at consecutive stages agree ($A'=A\otimes F$, $P'=P\otimes\langle t\rangle$, $B'=(P')^\perp_{A'}$), starting at $U_a$ on $X_a$ and $0$ on $Y_a$ and ending at $\mathcal F$ and $U_a^\perp$.",
        r"the next incoming labels. At stage 1 they start at $U_a$ on $X_a$"),
  infer("L0.3", r"On a side wire between neighboring triples the labels $P\otimes\langle t_X\rangle\subset P\otimes t_Y^\perp\subset P\otimes F$ are nested, because neighboring triples satisfy $t_X\perp t_Y$.",
        r"The first inclusion is possible because $t_X\perp t_Y$."),
  infer("L0.4", r"Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing exactly $h$ dimensions.",
        r"Every edge joins comparable nondegenerate labels.  The only decreasing"),
  infer("L0.5", r"For the binary label space every nonzero orthogonal residual of an edge has an orthonormal basis.",
        r"For the binary label space, every nonzero orthogonal residual of an"),
 ],
 page="subset-labels",
 frm=["matrix-basics","sets-subsets-and-basic-combinatorics","binary-field-f2-and-xor","vectors-matrices-and-linear-maps"],
 salient=r"Neighbors are orthogonal in both label fields although the two networks use different pairings: $|S\cap T|-1$ over the rationals and $|S\cap T|\bmod 2$ over $\mathbb F_2$.")

rank_saving = show(
 "R0",
 r"In both networks the sum over all edges of the label-dimension changes equals $Wm-2N+2L$, and since the loss $L$ on decreasing edges satisfies $L<N/2$ this total is strictly below $Wm$; this strict deficit is the source of the power saving.",
 r"Count dimensions: the signed changes telescope through each gate to the difference of sink and source dimensions, and the absolute total adds twice the loss on the few decreasing edges.",
 ("explicit", "Only the decreasing edges make the absolute total exceed the signed total, so it is enough to bound their loss.", r"contributions at gates cancel."),
 [
  network, frames, labels,
  infer("R0.1", r"The signed dimension changes telescope at every gate, since each touched wire has one incoming and one outgoing incidence with the same gate label; the sources total $N$ and the sinks $Wm-N$, so the signed increase is $Wm-2N$.",
        r"sink dimensions is $Wm-N$.  The signed increase is therefore $Wm-2N$."),
  infer("R0.2", r"There are $Ic$ decreasing edges each of loss $h$, so $L=Ich$, and replacing signed changes by absolute changes adds $2L$, giving the absolute total $Wm-2N+2L$.",
        r"There are $Ic$ decreasing edges, each of loss $h$; replacing signed"),
  infer("R0.3", r"The loss ratios have the exact values $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both smaller than $1/2$.",
        r"In particular, both are smaller than $1/2$."),
 ],
 page="rank-saving",
 frm=["matrix-basics","vectors-matrices-and-linear-maps","sets-subsets-and-basic-combinatorics"],
 adds=[add("N","bank size","the number of triples-indexed data wires in one bank, $v^3$ with $v=\\binom h3$","count"),
       add("L","total loss","the total dimension lost on decreasing edges, equal to the number of central wires times $h$","count")],
 salient=r"Exactly one kind of edge ever decreases (a central wire between times 3 and 4), so the absolute total is only $2L<N$ above the signed total.")

bit_network = show(
 "B0",
 r"The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates and sends its input to the role permutation $\rho$ of itself; rational matrices $M_v$ on its gates satisfy $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ for every input role, and the edge ranks sum to $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.",
 r"Assign to each vertex the projection onto its label along the orthogonal complement, so each edge matrix has rank equal to the label-dimension change; add the $N$ extra ranks of the negative source projections that are needed for the endpoint identity.",
 ("recoverable", "With frames given by address shears, an edge costs as many smaller interchanges as the rank of its matrix difference, and the endpoint difference of matrices must be the identity so every role undergoes the shear $H\\leftarrow H+D$.", None),
 [
  rank_saving,
  infer("B0.1", r"For nondegenerate $U\subset V$, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement, so its rank is $\dim V-\dim U$, and reversing the edge does not change the rank.",
        r"$P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its"),
  infer("B0.2", r"The only exceptions to rank equal to dimension change are the $N$ negative source projections: at stage 1 the first edge of each $X_a$ has matrix $2P_{U_a}$ of rank one where the dimension change was zero, so $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$.",
        r"The only exceptions are the $N$ negative source projections."),
  infer("B0.3", r"The deficit of the rank sum from $W_{\rm b}m$ is $N-2L_{\rm b}>0$ because $L_{\rm b}<N/2$.",
        r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$."),
  infer("B0.4", r"For an input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$, and every other role has zero source matrix and identity sink matrix, so $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ on all roles.",
        r"For an input $X_a$ the endpoint difference is"),
  infer("B0.5", r"Both exact relative deficits exceed $20\cdot2^{-50}$ and $m<2^{20}$, so $m^{1-2^{-50}}>m(1-20\cdot2^{-50})>m(1-\eta)$; hence $s_{\rm b}/W_{\rm b}<m^\tau$ (and $s_{\rm c}/W_{\rm c}<m^\sigma$) with $\tau=\sigma=1-2^{-50}$.",
        r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$."),
 ],
 page="bit-network",
 frm=["network","frames","subset-labels","rank-saving","matrix-basics"],
 adds=[add("W_{\\rm b}","bit wire count","the number of wires of the bit network, data wires plus scratch wires","count"),
       add("s_{\\rm b}","bit rank sum","the sum over all edges of the rational rank of the edge matrix difference in the bit network","count"),
       add("L_{\\rm b}","bit loss","the total dimension lost on decreasing edges in the bit network","count")],
 salient=r"The rank sum falls short of $W_{\rm b}m$ by only a relative amount of order $10^{-11}$, yet any strict deficit suffices for a power saving.")

lower_tri = show(
 "T0",
 r"Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation matrix with exactly $a$ ones.",
 r"Eliminate pivot by pivot: take the topmost nonzero row and its rightmost nonzero entry, clear to the left by right multiplication and below by left multiplication with lower triangular elementary matrices, delete that row and column from the active indices and repeat.",
 ("explicit", "Lower triangular changes of coordinates are exactly the updates a later field can take from earlier fields in linear time, so the factors must be lower triangular, which is a Bruhat factorization with coordinate order reversed.", r"can be performed entirely in this direction. The required factorization"),
 [
  infer("T0.1", r"If $A=0$ take $E_1=E_2=I$ and $\Pi=0$; otherwise the topmost nonzero row and its rightmost nonzero entry give a pivot, with nothing to its right in the pivot row.",
        r"If $A=0$, take $E_1=E_2=I$ and $\Pi=0$.  Otherwise choose the topmost"),
  infer("T0.2", r"Elementary operations on the remaining active indices are still lower triangular in the original order and leave earlier pivot rows and columns unchanged.",
        r"their original orders, and repeat.  Elementary operations on the active"),
  infer("T0.3", r"Each step isolates a rank-one block and leaves the remaining rank in the active submatrix, so the final partial permutation has exactly $a$ ones.",
        r"been cleared.  Each step isolates a rank-one block and leaves the"),
 ],
 page="lower-triangular",
 frm=["vectors-matrices-and-linear-maps","proof-by-induction-and-recursion"])

matrix_shear = show(
 "MS0",
 r"For a fixed finite set of rational matrices there is a fixed odd prime $q$ such that, for $A$ of rational rank $a$, the permutation $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ costs exactly $a$ interchanges of $b$-digit $H$ and $D$ fields plus $O(V)$ further work.",
 r"Factor $A=E_1\Pi E_2$, conjugate by the triangular maps (each linear time by controlled shifts) so only $\Pi$ remains, and realize each one of $\Pi$ by one interchange framed by two controlled shifts.",
 ("explicit", "Triangular changes of coordinates cost only $O(V)$ because each field follows earlier control fields, so the cost of a shear is concentrated in the ones of $\\Pi$.", r"earlier fields in linear time.  Lower triangular changes of coordinates"),
 [
  lower_tri,
  infer("MS0.1", r"Choose the factorizations for the fixed finite set once, and an odd prime $q$ avoiding every denominator and every numerator of a diagonal entry of an invertible factor, so all identities specialize to $\mathbb Z/q^b\mathbb Z$ and the triangular factors stay invertible.",
        r"Choose an odd prime avoiding every denominator"),
  infer("MS0.2", r"A lower triangular transformation of $H$ or of $D$ costs $O(V)$: update coordinates in descending physical order, multiplying by a diagonal unit and adding a fixed combination of earlier coordinates that still hold their original values.",
        r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
  infer("MS0.3", r"For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, then add $\Pi D$ to $H$, and finally transform $H$ by $E_1$ and $D$ by $E_2^{-1}$.",
        r"For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,"),
  infer("MS0.4", r"Each one at position $(i,j)$ of $\Pi$ is realized by $D_j\leftarrow D_j+H_i$, then interchanging $H_i$ and $D_j$, then $D_j\leftarrow H_i-D_j$, which sends $(h,d)$ to $(h+d,d)$ with exactly one interchange; so exactly $a$ interchanges are used.",
        r"It uses just one interchange.  There are $a$ ones, which proves the"),
 ],
 page="matrix-shear",
 frm=["lower-triangular","controlled-shifts","modular-arithmetic","vectors-matrices-and-linear-maps"])

recurrence = show(
 "PR0",
 r"Calling $s$ smaller operations of width $e/m$ on role streams of volume $V/W$ gives normalized cost $F_k\le(s/W)F_{k-1}+O(1)$ for $e=m^k$, and because $s/W<m^\tau$ this solves to $F_k=O(e^\tau)$, a strict power saving.",
 r"Count the recursive calls as the sum of the edge ranks, divide the cost by the volume so that each child contributes the factor $s/W$, and unroll the recurrence as a geometric sum, treating a ratio at most one and a ratio above one separately.",
 ("explicit", "Dividing by volume turns the $s$ child calls on streams of volume $V/W$ into the single factor $s/W$, and this factor being below $m$ is what yields the power saving.", r"After dividing cost by volume, multiplying the parameter by $m$"),
 [
  infer("PR0.1", r"Each recursive call comes from one unit of rank of one edge, so a node makes exactly $s$ calls; temporary tapes do not multiply that count.",
        r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
  infer("PR0.2", r"Each of the $s$ calls acts on one role stream of volume $V/W$ with all other fields as spectators, while splitting, merging, gates and triangular operations cost $O(V)$ in total at the node.",
        r"Each acts on one role stream of volume $V/W$, retaining all other"),
  infer("PR0.3", r"If $F_k$ bounds time divided by logical volume at width $m^k$, then $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.",
        r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."),
  infer("PR0.4", r"For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^ka^j$ is $O(m^{k\tau})$: if $a\le1$ it is at most $k+1$, and if $a>1$ it is $O(a^k)$.",
        r"most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$."),
  infer("PR0.5", r"Hence $F_k=O(e^\tau)$ for $e=m^k$.",
        r"Hence $F_k=O(e^\tau)$."),
  infer("PR0.6", r"Scheduling the child calls on a fixed number of tapes (parking the $W-1$ inactive role streams on a stack, copying the active stream to a child area and back) adds only $O(V)$ at the node, so the additive term of the recurrence stays $O(V)$.",
        r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
 ],
 page="power-saving-recurrence",
 frm=["proof-by-induction-and-recursion","logarithms-and-exponentials","asymptotic-notation-beyond-big-o"],
 adds=[add("F_k","normalized cost","the time of an interchange of width $m^k$ divided by the logical volume of the array"),
       add("a","call ratio","the average number $s/W$ of smaller calls per wire","direct")],
 salient=r"Multiplying the width by $m$ multiplies the work per unit volume by only $s/W<m$ rather than by $m$, so the cost per volume grows like $e^\tau$ with $\tau<1$ instead of linearly in the width $e$.")

power_interchange = show(
 "K0",
 r"Assume a fixed restoring circuit with $W$ wires and label dimension $m$ whose edge matrices have total rank $s<Wm$, and choose $\tau\in(0,1)$ with $s/W<m^\tau$; then for $e=m^k$ two chunks of $e$ radix-$q$ digits can be interchanged in $O(Ve^\tau)$ time, provided a row field before both is divisible by $W^k$.",
 r"Run the shear $H\leftarrow H+D$ on every row by splitting rows among the $W$ roles and executing the exchange network edge by edge, with each edge's address shear done by recursive smaller interchanges; compose three shears into the swap, count the $s$ smaller calls per node on streams of volume $V/W$, and solve the resulting recurrence.",
 ("explicit", "An edge of rank $a$ costs $a$ smaller interchanges, and the sum of the ranks being below $Wm$ makes the recurrence save a power of the width.", r"the resulting recurrence saves a power of the chunk width."),
 [
  bit_network,
  matrix_shear,
  infer("K0.1", r"Split whole rows cyclically into the $W$ role streams within each prefix; the streams have the same remaining shape, each has volume $V/W$, and its row count is divisible by $W^{k-1}$.",
        r"Split whole rows cyclically into $W$ role streams within each prefix",
        frm=["stream-ops"]),
  infer("K0.2", r"Applying $\Phi_{A_e}$ on every circuit edge and the gates pointwise, the common-frame identity with frames $\Phi_{M_v}$ makes the output on role $\rho(w)$ equal $\Phi_{I_m}f_w$; after merging, $H\leftarrow H+D$ holds on every original row, including rows assigned to scratch roles with arbitrary initial values.",
        r"is $H\leftarrow H+D$ on every original row, including rows assigned",
        frm=["frames","bit-network","matrix-shear","network"]),
  infer("K0.3", r"The three updates $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ send $(H,D)$ to $(D,H)$; only the middle shear uses the circuit and the other two are linear-cost shifts.",
        r"To interchange the two full chunks, perform"),
  recurrence,
 ],
 page="power-interchange",
 frm=["stream-ops","controlled-shifts","binary-field-f2-and-xor","vectors-matrices-and-linear-maps"],
 adds=[add("W","wire count","the number of wires of the fixed exchange circuit, scratch wires included","count"),
       add("m","label dimension","the number of fields in each of the address vectors $H,D$, equal to the dimension of the label space","count"),
       add("s","call count","the sum of the ranks of all edge matrices, the number of smaller interchanges per node","count"),
       add("e","chunk width","the number of radix-$q$ digits in each interchanged chunk, equal to $m^k$","count")],
 salient=r"The final effect is an exact permutation of the data although the intermediate steps are XOR combinations of data, and it is exact for arbitrary initial contents of the scratch roles.")
