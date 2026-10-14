from lib import *

# ---- network (scalar exchange network with restored scratch wires)
network = show(
    "S1.3.1",
    r"A fixed network of linear gates on $W$ wires, run in three stages of eight scalar rows per invocation, sends $(X_a,Y_a)$ to $(-Y_a,X_a)$ and returns every scratch wire to its arbitrary initial value.",
    "Subtract the old scratch contribution, add the source's effect through the scratch wires, then undo it, and compose three such invocations into an exchange.",
    ("explicit", "The sources say the scratch cancellation is the standard restoration trick.",
     r"This cancellation of arbitrary initial scratch values is a linear"),
    [
        inf("S1.3.1a",
            r"Whatever the initial side and central values $a,c$, a forward invocation adds $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$ to the target and restores $a$ and $c$, because rows 0 and 1 first subtract $\mathcal J a+\mathcal R c$.",
            r"Rows 6 and 7 restore $c,a$.  The net target change is"),
        inf("S1.3.1b",
            r"The net coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod 2$ centrally and the side injection cancels the intersection-one cases, so in the bit construction the net map is $y\gets y+x$ (complex case: $(|S\cap T|-1)/2$, cancelled for intersections zero and two).",
            r"In the bit case, the central coefficient from $x_T$ to $y_S$ is"),
        inf("S1.3.1c",
            r"A forward invocation at stage 1, the inverse schedule at stage 2 and a forward invocation at stage 3 send $(x,y)\to(x,y+x)\to(-y,y+x)\to(-y,x)$, an exchange of the banks with a sign.",
            r"The inverse schedule with logical source $Y$ and target $X$ effects"),
    ],
    page="network",
    frm=["binary-field-f2-and-xor", "boolean-gates-and-circuits", "sets-subsets-and-basic-combinatorics"],
)

frames = inf(
    "S1.3.2",
    r"If every wire's array is stored under an invertible address operator (frame) $D_v$ common to all wires at a gate, the pointwise gates commute with the frames and the whole network applies $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$, so only the endpoint frames of each role matter and each edge merely changes frame.",
    r"The implemented operator is therefore",
    page="frames",
    frm=["network", "matrix-basics", "vectors-matrices-and-linear-maps"],
    salient=r"The same endpoint operator acts on the auxiliary scratch roles as on the data roles, although their contents are arbitrary: the frame identity holds for every role and every input, so the scratch roles need no special treatment.",
)

subset_labels = show(
    "S1.3.3",
    r"Each gate and terminal gets a nondegenerate subspace of the tensor cube $F^{\otimes 3}$ of dimension $m$, built from indicator vectors of three-element subsets of $[h]$, so that the labels on every edge are nested and neighbouring triples have orthogonal lines.",
    r"Pick triple lines $\langle t_T\rangle$ whose pairings are intersection sizes, expose one tensor factor per stage, and assign the gate labels through the orthogonal splitting $A\otimes F=(B\otimes F)\perp(P\otimes F)$.",
    ("explicit", "The labels are chosen to make the frame changes cheap.",
     r"choose its intermediate labels to make the changes of frame inexpensive."),
    [
        inf("S1.3.3a",
            r"On $\mathbb Q^h$ with the form $x^{\mathsf T}(I-J/9)y$ one has $\langle t_S,t_T\rangle=|S\cap T|-1$ and $\langle t_T,t_T\rangle=2$ (over $\mathbb F_2$ the dot product gives $t_T\cdot t_T=1$), so triple lines are nondegenerate and neighbouring triples give orthogonal lines.",
            r"\langle t_S,t_T\rangle=|S\cap T|-1,"),
        inf("S1.3.3b",
            r"The outgoing labels of each stage equal the incoming labels of the next ($A'=A\otimes F$, $P'=P\otimes\langle t\rangle$, $B'=(P')^\perp_{A'}$), starting from $U_a$ on $X_a$ and $0$ on $Y_a$ and ending at $\mathcal F$ and $U_a^\perp$.",
            r"Thus the prescribed outgoing labels are"),
        inf("S1.3.3c",
            r"On a side wire the remaining component grows through $P\otimes\langle t_X\rangle\subset P\otimes t_Y^\perp\subset P\otimes F$, which needs $t_X\perp t_Y$, while a central wire returns once from $A\otimes F$ to $B\otimes F$, so every dimension decrease sits in that one return.",
            r"The first inclusion is possible because $t_X\perp t_Y$."),
    ],
    page="subset-labels",
    frm=["network", "frames", "matrix-basics", "sets-subsets-and-basic-combinatorics"],
)

# ---- KEY STEP: rank saving
dim_count = show(
    "S1.3.4a",
    r"The sum of the absolute dimension changes of the labels over all edges is $Wm-2N+2L$, with $L=Ich$ the total dimension lost on decreasing edges.",
    "Sum signed changes over sources and sinks, let them telescope at the gates, and add twice the loss on the decreasing edges.",
    ("recoverable", "Absolute changes exceed signed ones by exactly twice the total decrease, so one needs the signed total and the decreasing edges; the sources compute both."),
    [
        inf("S1.3.4a1",
            r"Every edge joins nested nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing the residual $P\otimes F$ of dimension $h$.",
            r"Label dimension is nondecreasing along every edge except center $3\to4$, which removes",
            salient=r"Out of eight gates touching a wire, exactly one edge per central wire shrinks its label, and it shrinks by only $h$ out of $m=h^3$ dimensions.",),
        inf("S1.3.4a2",
            r"Because at each gate every touched wire has the same label on its incoming and outgoing incidence, the signed dimension changes telescope; with source dimensions summing to $N$ and sink dimensions to $Wm-N$ the signed total is $Wm-2N$.",
            r"The signed sum of dimension changes telescopes at every gate: each"),
        inf("S1.3.4a3",
            r"There are $Ic$ decreasing edges of loss $h$ each, so $L=Ich$, and replacing signed by absolute changes adds $2L$, giving $Wm-2N+2L$.",
            r"There are $Ic$ decreasing edges, each of loss $h$; replacing signed"),
        inf("S1.3.4a4",
            r"The loss ratio is exactly $L_{\rm b}/N=100/539<1/2$ for the bit network (and $101/539$ for the phase network), so the absolute dimension total $Wm-2N+2L$ stays below $Wm$.",
            r"In particular, both are smaller than $1/2$.  We now turn the dimension"),
    ],
)

rank_vs_dim = show(
    "S1.3.4b",
    r"For the rational labels of the bit network the sum of edge ranks is $s=Wm-N+2L$, which is still below $Wm$ because $N-2L>0$.",
    "Identify the rank of each edge matrix with the dimension change, then add the single family of edges where rank exceeds dimension change.",
    ("recoverable", "Rank counts the smaller calls while the label count measures dimension; they agree except where the source matrix is a negative projection, which the sources single out."),
    [
        inf("S1.3.4b1",
            r"For nested nondegenerate $U\subset V$ the matrix $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement, so its rank is $\dim V-\dim U$, and reversing the edge only negates the matrix.",
            r"$P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its"),
        inf("S1.3.4b2",
            r"The only exceptions are the $N$ negative source projections $-P_{U_a}$ at the sources of the $X_a$ wires: at stage 1, $B=0$ and the first gate has label exactly $U_a$, so the first edge matrix $2P_{U_a}$ has rank one although the dimension change is zero.",
            r"The only exceptions are the $N$ negative source projections."),
        inf("S1.3.4b3",
            r"The edge ranks therefore total $Wm-N+2L$, whose deficit from $Wm$ is $N-2L>0$ since $L<N/2$.",
            r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$."),
    ],
)

key = show(
    "S1.3.4",
    r"The total rank $s$ of all edge differences of the labelled bit network, which is the number of smaller calls one run makes, is strictly less than $Wm$.",
    "Count dimension changes of the labels along all edges, then correct for the one place where rank exceeds dimension change.",
    ("explicit", "The sources say the saving comes from keeping the dimension lost on decreasing edges small.",
     r"The saving will come from keeping the total dimension lost on decreasing"),
    [dim_count, rank_vs_dim],
    page="rank-saving",
    frm=["subset-labels", "frames", "matrix-basics"],
    adds=[sym("L", "total decrease", "The total dimension lost on the decreasing edges (the central-wire edges from time 3 to 4).", "count")],
    salient=r"The saving is a fixed small fraction: the deficit $Wm-s=N-2L$ is positive only because all decreases are confined to one edge per central wire, giving $L/N=100/539<1/2$; the relative deficit is tiny, about $1.5\cdot10^{-11}$, yet strictly positive.",
)

bit_network = inf(
    "S1.3.5",
    r"The bit network uses only XOR gates and permutes its inputs by $\rho$; its terminal matrices differ by $I_m$ on every input role, so the endpoint operator is the shear $(H,D)\mapsto(H+D,D)$ on every role, scratch roles included, at rank sum $s<Wm$.",
    r"$P_{U_a^\perp}-(-P_{U_a})=I_m$.",
    page="bit-network",
    frm=["subset-labels", "frames", "rank-saving", "binary-field-f2-and-xor"],
    salient=r"All $W$ roles receive the identical shear $H\gets H+D$, because the negative source projection makes the $X_a$ roles differ by $I_m$ and every other role has zero source matrix and identity sink matrix.",
)

exponent = inf(
    "S1.3.6",
    r"With $\tau=1-2^{-50}$ one has $s/W<m^\tau$, since the relative rank deficit exceeds $20\cdot2^{-50}$ while $m^{1-2^{-50}}>m(1-20\cdot2^{-50})$.",
    r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,",
    frm=["rank-saving", "logarithms-and-exponentials"],
    salient=r"The exponent is only $2^{-50}$ below one, because the relative deficit of the rank sum is about $1.5\cdot10^{-11}$; any positive deficit would give some $\tau<1$.",
)

lower = inf(
    "S1.3.7",
    r"Every rational $m\times m$ matrix $A$ of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with exactly $a$ ones.",
    r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization",
    page="lower-triangular",
    frm=["matrix-basics", "vectors-matrices-and-linear-maps"],
)

matrix_shear = show(
    "S1.3.8",
    r"For a rational matrix $A$ of rank $a$, the map $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ takes exactly $a$ interchanges of $b$-digit fields plus $O(V)$ other work.",
    r"Factor $A=E_1\Pi E_2$, do the triangular parts by ordered controlled shifts, and turn each one of $\Pi$ into $H_i\leftarrow H_i+D_j$ using one interchange between two linear updates.",
    ("explicit", "Lower triangular changes of coordinates only use earlier fields as controls, matching tape order.",
     r"earlier fields in linear time.  Lower triangular changes of coordinates"),
    [
        inf("S1.3.8a",
            r"A lower triangular transformation of $H$ or of $D$ costs $O(V)$ by updating coordinates in descending order, each as a unit times itself plus a fixed combination of earlier coordinates.",
            r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
        inf("S1.3.8b",
            r"The update $H_i\leftarrow H_i+D_j$ is done by $D_j\leftarrow D_j+H_i$, an interchange of $H_i,D_j$, and $D_j\leftarrow H_i-D_j$, which uses just one interchange per one of $\Pi$, hence $a$ in all.",
            r"It uses just one interchange."),
    ],
    page="matrix-shear",
    frm=["lower-triangular", "controlled-shifts", "modular-arithmetic"],
)

row_split = inf(
    "S1.3.9",
    r"Split whole rows cyclically into $W$ role streams, each of volume $V/W$ with the same remaining shape and a row count divisible by $W^{k-1}$.",
    r"Split whole rows cyclically into $W$ role streams within each prefix",
)

shear_by_network = inf(
    "S1.3.10",
    r"Applying the shear $\Phi_{A_e}$ on every circuit edge (by smaller interchanges) and the gates pointwise realizes $H\gets H+D$ on every row: the output of role $\rho(w)$ is $\Phi_{M_{\rm out}}\Phi_{-M_{\rm in}}f_w=\Phi_{I_m}f_w$, including rows assigned to scratch roles.",
    r"=\Phi_{I_m}f_w,",
    frm=["frames", "bit-network", "matrix-shear"],
    salient=r"Although intermediate steps form XOR combinations of data, the net effect is an exact permutation of addresses for arbitrary initial scratch contents, because a common address permutation commutes with every pointwise XOR gate.",
)

three_shears = inf(
    "S1.3.11",
    r"The interchange $(H,D)\mapsto(D,H)$ is obtained from three shears $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$, of which only the middle one uses the network.",
    r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,",
)

recurrence = show(
    "S1.3.12",
    r"Making $s$ smaller calls on streams of volume $V/W$ gives normalized cost $F_k\le(s/W)F_{k-1}+O(1)$, and since $s/W<m^\tau$ this solves to $F_k=O(e^\tau)$, a strict power saving.",
    "Unroll the recurrence into a geometric sum and bound the sum separately when the ratio is at most one and when it exceeds one.",
    ("recoverable", "Each level multiplies the normalized cost by $s/W$ while the width grows by $m$, so comparing $s/W$ with $m^\\tau$ decides the growth rate."),
    [
        inf("S1.3.12a",
            r"The number of recursive calls is the sum of the edge ranks, exactly $s$, each acting on one role stream of volume $V/W$; splits, merges, gates and triangular operations are a fixed number of $O(V)$ scans.",
            r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
        inf("S1.3.12b",
            r"If $F_k$ bounds time divided by volume at width $m^k$, then $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.",
            r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."),
        inf("S1.3.12c",
            r"For $a=s/W<m^\tau$ the sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$: if $a\le1$ it is at most $k+1=O(m^{k\tau})$, and if $a>1$ it is $O(a^k)$.",
            r"most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$."),
        inf("S1.3.12d",
            r"Hence $F_k=O(e^\tau)$ for $e=m^k$.",
            r"Hence $F_k=O(e^\tau)$."),
    ],
    page="power-saving-recurrence",
    frm=["rank-saving", "proof-by-induction-and-recursion", "big-o", "logarithms-and-exponentials"],
    salient=r"The cost per bit grows like $e^\tau$ rather than like $e$, since widening the chunk by a factor $m$ multiplies the recursive work only by $s/W<m^\tau$, not by $m$.",
)

schedule = inf(
    "S1.3.13",
    r"On a fixed number of tapes a depth-first schedule parks the $W-1$ inactive role streams on a stack, so each node pays $O(V)$ for pushes, pops, copies and erasures and the $O(1)$ term of the recurrence is justified.",
    r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$",
)

power_interchange = show(
    "S1.3",
    r"For $e=m^k$, two chunks of $e$ radix-$q$ digits can be interchanged in $O(Ve^\tau)$ time (given a row field divisible by $W^k$), by $s$ smaller interchanges on streams of volume $V/W$ with $s/W<m^\tau$.",
    "Run the fixed bit network on $W$ row streams so that each edge's shear is a smaller interchange, compose three shears into an interchange, and solve the recursion.",
    ("explicit", "An edge matrix of rank a costs a smaller interchanges, so total edge rank counts the recursive calls.",
     r"An edge matrix of rank $a$ will require $a$ smaller interchanges."),
    [network, frames, subset_labels, key, bit_network, exponent, lower, matrix_shear,
     row_split, shear_by_network, three_shears, recurrence, schedule],
    page="power-interchange",
    frm=["bit-network", "matrix-shear", "stream-ops", "power-saving-recurrence"],
    adds=[
        sym("W", "wire count", "The number of wires (roles), scratch wires included, of the fixed exchange network; also the number of row streams a call is split into.", "count"),
        sym("m", "label dimension", "The dimension of the label space, equal to the number of $b$-digit fields in each chunk.", "count"),
        sym("s", "smaller calls", "The sum of the ranks of all edge differences, which is the number of smaller interchanges one network run makes.", "count"),
        sym("e", "chunk width", "The width, in digits, of each of the two chunks, a power $m^k$ of $m$.", "count"),
        sym("N", "bank size", "The number of indices $a$ of each data bank, so each bank holds $N$ wires.", "count"),
        sym("h", "ground-set size", "The size ($h=100$) of the set whose three-element subsets index the banks.", "count"),
    ],
)

# ---- removing width and row restrictions
removing = show(
    "S1.4",
    r"For arbitrary width $u$ and arbitrary prefix, gap and suffix lengths, the interchange of two $u$-bit chunks costs $O(Vu^\tau)$.",
    "Swap the top digits of the two chunks pairwise to create a row field of range at least $W^k$, pad rows, split the remaining width in base $m$ into power-width pieces, then undo the preparation; pad binary chunks to radix-$q$ chunks.",
    ("explicit", "A general array has no row field, but its own high digits can serve as one.",
     r"Rows for a general array can be supplied by a few of its own high digits."),
    [
        inf("S1.4a",
            r"After exchanging the top $\rho=O(\log(2e))$ digit pairs, the two middle orders have a row field of range $R=q^{2\rho}\ge W^k$ before both remaining chunks.",
            r"R=q^{2\rho}\ge W^k"),
        inf("S1.4b",
            r"Splitting the remaining width as $\sum_j a_jm^j$ with $a_j<m$ and applying the power-width interchange to each piece costs $O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)$, since $m^k<me$.",
            r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)."),
        inf("S1.4c",
            r"The remaining movement, padding rows and reversing the joins, costs $O(V\log(2e))$, which is $O(Ve^\tau)$.",
            r"remaining movement cost $O(V\log(2e))$ is $O(Ve^\tau)$."),
        inf("S1.4d",
            r"Binary chunks of $u$ bits are padded to radix-$q$ chunks of $e$ digits, with $q^e\ge2^u$ and volume growth below $q^2$, and the padded entries are scanned away afterwards, giving $O(Vu^\tau)$.",
            r"Finally, for binary chunks let $e$ be the least integer with"),
        inf("S1.4e",
            r"Chunks whose widths differ by one bit are handled by one extra single-bit move around an equal-width interchange.",
            r"For widths differing by one bit, choose the leading bit of the longer"),
    ],
)

stream_ops = inf(
    "S1.1",
    r"Fixed permutations of digit values, digit moves, splitting on a digit with a pointwise map and merging, and cyclic splitting of whole rows into a fixed number $W$ of streams all take $O(V)$ steps on a fixed number of tapes.",
    r"volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
    page="stream-ops",
    frm=["array-order", "fixed-tape-model"],
)

controlled = inf(
    "S1.2",
    r"A target field can be updated by an offset computed from earlier control fields modulo $q^b$ (a cyclic shift of blocks), or multiplied by a fixed rational unit, in $O(V)$ time.",
    r"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
    page="controlled-shifts",
    frm=["stream-ops", "modular-arithmetic"],
)

S1 = show(
    "S1",
    r"Two disjoint $u$-bit address chunks of an array of volume $V$ can be interchanged in $O(Vu^\tau)$ tape steps for a fixed $\tau<1$.",
    "Combine elementary tape scans with a recursion driven by a fixed linear exchange network whose total edge rank is below its wire count times its dimension, then remove the width and row restrictions.",
    ("explicit", "Because the total rank is below the wire count times the dimension, the recurrence saves a power of the chunk width.",
     r"Because the sum of these ranks is less than the number of wires times"),
    [stream_ops, controlled, power_interchange, removing],
    page="chunk-interchange",
    frm=["fixed-tape-model", "array-order", "binary-field-f2-and-xor"],
    salient=r"The final effect is an exact permutation of addresses even though the intermediate steps form pointwise XOR combinations of data; this holds because the endpoint operator of the network is the same exact shear on every role, scratch roles included.",
)
