import json, re, sys

SRC = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e4/V4/sources/paper.tex').read()

def E(q):
    return {"source": "paper", "quote": q}

def M(text, src, quote=None):
    d = {"text": text, "source": src}
    d["quote"] = E(quote) if quote else None
    return d

def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

def show(id, claim, method, motivation, children, page=None, frm=None, salient=None, adds=None):
    d = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children, "from": frm or []}
    if page: d["page"] = page
    if salient: d["salient"] = salient
    if adds: d["adds"] = adds
    return d

def infer(id, claim, quote, page=None, frm=None, deferred=False, salient=None):
    d = {"id": id, "intention": "infer", "claim": claim, "quote": E(quote), "from": frm or []}
    if page: d["page"] = page
    if deferred: d["deferred"] = True
    if salient: d["salient"] = salient
    return d

# ---------------------------------------------------------------- S1.1 finite networks
s111 = show(
    "S1.1.1",
    r"A fixed linear network of copy, gather, scatter and side-injection gates on banks $X$ and $Y$ sends $(X,Y)$ to $(-Y,X)$ in three stages and restores every scratch wire to its arbitrary initial value.",
    "Show that one eight-row invocation adds the source bank to the target bank whatever the scratch values are, then compose three invocations (forward, inverse, forward).",
    M("The old scratch contents are first subtracted out and later restored, so the net map cannot depend on them; composing $y\\leftarrow y+x$, $x\\leftarrow x-y$, $y\\leftarrow y+x$ then gives the signed exchange.", "recoverable"),
    [
        infer("S1.1.1.1", r"The central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod 2$ (bit case), and the side injection cancels exactly the intersection-one cases, leaving only the self coefficient.",
              r"In the bit case, the central coefficient from $x_T$ to $y_S$ is"),
        infer("S1.1.1.2", r"For arbitrary initial scratch values, a forward invocation performs $y\leftarrow y+x$ and changes nothing else.",
              r"Thus both net maps are $y\gets y+x$."),
        infer("S1.1.1.3", r"Three invocations, from $X$ to $Y$, inverse from $Y$ to $X$, and from $X$ to $Y$, send $(x,y)$ to $(-y,x)$.",
              r"Starting from $(x,y)$, the three stages give"),
    ],
    page="scalar-exchange-network",
    frm=["subset-pairing-formulas", "f2-vectors", "boolean-and-arithmetic-circuits-as-networks", "modular-arithmetic-and-residue-classes"],
)

s112 = infer(
    "S1.1.2",
    r"If every wire's scalar is replaced by an array and each gate and terminal $v$ gets an invertible frame $D_v$, then pointwise linear gates commute with the common frame and the whole network acts as $D_{\rm out}\,\mathsf S\,D_{\rm in}^{-1}$, so only endpoint frames matter.",
    r"Thus the common frame commutes with the pointwise gate, and",
    page="network-frames",
    frm=["linear-algebra-basics", "scalar-exchange-network", "boolean-and-arithmetic-circuits-as-networks"],
    salient="Every intermediate frame cancels, so the operator on a route depends only on its two endpoint frames; the edge frames can therefore be chosen freely for cheapness, and the same endpoint operator lands on every role including the auxiliary scratch roles.",
)

s113 = show(
    "S1.1.3",
    r"Gates and terminals can be labeled by nested nondegenerate subspaces of an $m$-dimensional space so that the only dimension-decreasing edges are the central-wire returns, with total loss $L$ below half the number $N$ of source ranks; the sum of absolute dimension changes is then $Wm-2N+2L$.",
    "Build the labels from tensor powers of indicator vectors of three-element subsets, whose neighbor-orthogonality makes the labels nest, and confine every decrease to a single edge per central wire.",
    M("Neighboring triples have orthogonal indicator lines, which is exactly what is needed for one label to contain the next.", "explicit",
      r"The first inclusion is possible because $t_X\perp t_Y$."),
    [
        infer("S1.1.3.1", r"Every triple line is nondegenerate and neighboring triple lines are orthogonal, over $\mathbb Q$ with the form $I-J/9$ and over $\mathbb F_2$ with the dot product.",
              r"Thus every triple line is nondegenerate, and neighboring triple lines"),
        infer("S1.1.3.2", r"Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$.",
              r"Every edge joins comparable nondegenerate labels."),
        infer("S1.1.3.3", r"Signed dimension changes telescope at every gate, so they sum to $Wm-2N$, and absolute changes add $2L$ with $L=Ich$.",
              r"The signed sum of dimension changes telescopes at every gate: each"),
        infer("S1.1.3.4", r"Over $\mathbb F_2$ every nonzero orthogonal residual is nonalternating and so has an orthonormal basis.",
              r"For completeness, every nondegenerate nonalternating binary symmetric"),
        infer("S1.1.3.5", r"The loss ratios are $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both smaller than $1/2$.",
              r"In particular, both are smaller than $1/2$."),
    ],
    page="subspace-labels-rank-saving",
    frm=["linear-algebra-basics", "tensor-products", "f2-vectors", "bilinear-orthogonality", "subset-pairing-formulas", "network-frames", "scalar-exchange-network"],
    salient="All the dimension lost over the whole network is concentrated in one edge per central wire, and the loss ratios 100/539 and 101/539 are the same for every stage and every invocation; this is why the total change falls below $Wm$ by a fixed fraction.",
)

s114 = show(
    "S1.1.4",
    r"The bit network with rational projection matrices on its gates has endpoint difference $I_m$ on every input role, and its edge differences have total rank $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.",
    "Assign the projection $P_U$ onto each label, so that an edge difference has rank equal to the dimension change, and charge one extra rank for each negative source projection.",
    M("A difference of projections onto nested nondegenerate subspaces has rank equal to the dimension gap, so the label dimension count transfers directly to a rank count.", "recoverable"),
    [
        infer("S1.1.4.1", r"For nondegenerate nested $U\subset V$, the matrix $P_V-P_U$ has rank $\dim V-\dim U$.",
              r"Its rank is $\dim V-\dim U$; reversing the"),
        infer("S1.1.4.2", r"The $N$ negative source projections each add one rank beyond the dimension change.",
              r"Its first edge matrix is therefore $2P_{U_a}$, of rational rank one,"),
        infer("S1.1.4.3", r"The deficit of the rank sum from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.",
              r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$."),
        infer("S1.1.4.4", r"For input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$, and every other role has zero source matrix and identity sink matrix.",
              r"$P_{U_a^\perp}-(-P_{U_a})=I_m$."),
    ],
    page="bit-network-interface",
    frm=["address-shear", "subspace-labels-rank-saving", "linear-algebra-basics", "bilinear-orthogonality", "network-frames"],
)

s115 = show(
    "S1.1.5",
    r"For the Gaussian-dyadic network with binary labels, each edge's phase-frame change is a product of translation kernels $aI+bX_v$ (or inverses), one per vector of an orthonormal basis of the edge residual; the total length is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$, and telescoping gives $C^{\otimes m}$ on every role.",
    "Use phase frames $i^{\\operatorname{wt}(P_Ux)}$, because Hamming weight is additive mod 4 across orthogonal directions, so each orthonormal residual vector contributes one two-point kernel.",
    M("Weight is additive modulo four across orthogonal binary vectors, which turns a change of label into a sum of one-vector phase changes.", "explicit",
      r"If $z\cdot w=0$, the intersection cardinality is even, so weight is"),
    [
        infer("S1.1.5.1", r"Each orthonormal residual vector $v$ has odd weight, so its phase coefficient is $\pm1$ mod four.",
              r"Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd."),
        infer("S1.1.5.2", r"Conjugating by $H$ sends the character $(-1)^{v\cdot x}$ to the translation $X_v$, so the phase $i^{\varepsilon[v\cdot x]}$ becomes $aI+bX_v$ or its inverse.",
              r"The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the"),
        infer("S1.1.5.3", r"The residual dimensions sum to $s_{\rm c}$, which is below $W_{\rm c}m$ by $2N-2L_{\rm c}>0$.",
              r"The same lemma gives the count $s_{\rm c}$."),
        infer("S1.1.5.4", r"On the pair $X_a\to Y_a$ the operator has 27 inverse factors, and $C=iZC^{-1}Z$ turns each of them into $C$ at the price of address signs and a constant phase.",
              r"Apply $Z_{a,k}$ before the network at $X_a$, and apply"),
        infer("S1.1.5.5", r"After undoing the bank exchange and the minus sign, every role, including every scratch role, carries the forward tensor product $C^{\otimes m}$.",
              r"Every role, including every scratch role, now has"),
    ],
    page="complex-network-interface",
    frm=["phase-kernel", "f2-vectors", "bilinear-orthogonality", "subspace-labels-rank-saving", "network-frames", "tensor-products", "complex-numbers"],
    salient="The same operator $C^{\\otimes m}$ arrives on every wire role, including the auxiliary roles whose initial values are arbitrary and the special pair $X_a\\to Y_a$ whose 27 inverse factors are converted back to forward ones.",
)

s116 = infer(
    "S1.1.6",
    r"The explicit rank deficits give $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$ with the fixed rational exponent $\tau=\sigma=1-2^{-50}<1$.",
    r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$.",
)

s11 = show(
    "S1.1",
    r"There are two fixed linear networks, one over bits with rational subspace labels and one over Gaussian dyadics with binary labels, that exchange two banks, restore every scratch wire, and have total frame-change rank $s<Wm$.",
    "Give explicit gate schedules from triple-intersection formulas, observe that a common frame commutes with pointwise gates, then label gates by nested subspaces so that frame changes have small total rank.",
    M("The recursion on tape needs the number $s$ of smaller calls to be strictly below $W$ times the factor $m$ by which the width shrinks.", "explicit",
      r"number $s$ of smaller calls satisfies $s<Wm$."),
    [s111, s112, s113, s114, s115, s116],
    frm=[],
)

# ---------------------------------------------------------------- S1.2 chunk swap
k_solve = show(
    "S1.2.1.4.4",
    r"Since $s/W<m^\tau$, the sum $\sum_{j\le k}(s/W)^j$ is $O(m^{k\tau})$, so $F_k=O(e^\tau)$.",
    "Split on whether the ratio $a=s/W$ is at most one or greater than one and bound the geometric sum in each case.",
    M("In both cases the sum of powers of $a$ is dominated by $m^{k\\tau}$, because $a<m^\\tau$.", "recoverable"),
    [
        infer("S1.2.1.4.4.1", r"For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$.",
              r"For $a=s/W<m^\tau$ the geometric sum"),
        infer("S1.2.1.4.4.2", r"If $a\le1$ the sum is at most $k+1$, and if $a>1$ it is $O(a^k)$, in either case $O(m^{k\tau})$.",
              r"most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$."),
        infer("S1.2.1.4.4.3", r"Hence $F_k=O(e^\tau)$ for $e=m^k$.",
              r"Hence $F_k=O(e^\tau)$."),
    ],
)

key = show(
    "S1.2.1.4",
    r"If a call at width $e=m^k$ makes $s$ calls at width $e/m$, each on a stream of volume $V/W$, then time per unit volume satisfies $F_k\le(s/W)F_{k-1}+O(1)$, and because $s/W<m^\tau$ with $\tau<1$ this solves to $F_k=O(e^\tau)$.",
    "Count the recursive calls, divide the cost by the volume so that each child contributes a factor $s/W$ rather than $s$, and solve the resulting recurrence as a geometric series.",
    M("Dividing by volume turns the $s$ calls on streams of volume $V/W$ into a factor $s/W$ per level, and since the width grows by $m$ per level the strict inequality $s/W<m$ is what yields a power saving.", "explicit",
      r"is the source of the power saving."),
    [
        infer("S1.2.1.4.1", r"The number of recursive calls is the sum of the edge ranks, exactly $s$.",
              r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
        infer("S1.2.1.4.2", r"Each call acts on one role stream of volume $V/W$ with all other fields as spectators; splitting, merging, gates and triangular operations cost $O(V)$ at the node.",
              r"Each acts on one role stream of volume $V/W$, retaining all other"),
        infer("S1.2.1.4.3", r"Hence a uniform bound $F_k$ on time divided by logical volume satisfies $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.",
              r"uniform upper bound for time divided by logical volume, then"),
        k_solve,
    ],
    page="rank-deficit-recurrence",
    frm=["recurrences-and-geometric-series", "row-splitting-roles", "subspace-labels-rank-saving", "network-frames", "big-o", "logarithms-exponentials-floors-and-ceilings"],
    salient="The cost per unit volume grows only like the power $e^\\tau$ with $\\tau<1$ in the chunk width, because the width is multiplied by $m$ at each level while the work is multiplied only by $s/W<m^\\tau$; the strict rank deficit $s<Wm$ is exactly what buys $\\tau<1$.",
)

dfs = show(
    "S1.2.1.5",
    r"The $s$ child calls can be scheduled on one fixed set of tapes by parking the inactive role streams on a stack, copying the active stream to the child and restoring afterwards, at cost $O(V)$ per node.",
    "Use a stack discipline: park the other $W-1$ streams, copy the active one down, and pop the parked streams on return, so no scan ever crosses a parked ancestor.",
    M("The recurrence assumes $O(V)$ overhead per node; this must be checked on fixed tapes where a naive schedule could sweep through ancestors' data.", "explicit",
      r"Here we complete the implementation assertion used in"),
    [
        infer("S1.2.1.5.1", r"Before a recursive call the $W-1$ inactive role streams are appended to the parking stack and the active stream is copied to the child's input area.",
              r"Before a recursive call, append the $W-1$ inactive role streams to the"),
        infer("S1.2.1.5.2", r"On return, the child output is copied into the active role and the inactive streams are popped in reverse order.",
              r"On return, copy the child output into the designated active role."),
        infer("S1.2.1.5.3", r"Each push, pop, copy or erasure moves $O(V)$ symbols at a parent node, and there are only $s$ child calls.",
              r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
    ],
    page="fixed-tape-dfs-schedule",
    frm=["stacks-and-recursion", "multitape-model", "row-splitting-roles"],
)

pw = show(
    "S1.2.1",
    r"For $e=m^k$ and a row field of length divisible by $W^k$, two chunks of $e$ radix-$q$ digits are interchanged in $O(Ve^\tau)$ time.",
    "Run the fixed bit network on $W$ role streams of whole rows, implementing each edge's address shear by smaller interchanges of the same kind, then turn the shear $H\\leftarrow H+D$ into an interchange by two linear-cost updates.",
    M("An XOR network can act as an exact permutation while making each edge cost only as many smaller interchanges as its rank, which is what lets the same procedure call itself on narrower chunks.", "recoverable"),
    [
        infer("S1.2.1.1", r"Every rational $m\times m$ matrix $A$ of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with exactly $a$ ones.",
              r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization",
              page="lower-factorization",
              frm=["linear-algebra-basics"]),
        show(
            "S1.2.1.2",
            r"The shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ of rank $a$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work.",
            "Factor $A=E_1\\Pi E_2$, perform the triangular changes as controlled shifts and each pivot by one interchange.",
            M("Triangular changes update a later field from earlier fields, which is the direction in which controlled shifts are linear; only the pivots need a genuine interchange.", "recoverable"),
            [
                infer("S1.2.1.2.1", r"A lower triangular transformation of $H$ or of $D$ costs $O(V)$, updating coordinates in descending physical order.",
                      r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
                infer("S1.2.1.2.2", r"Each one of $\Pi$ calls for $H_i\leftarrow H_i+D_j$, implemented by two linear updates around a single interchange.",
                      r"It uses just one interchange."),
                infer("S1.2.1.2.3", r"The number of recursive calls equals the rational rank $a$.",
                      r"rank $a$; temporary tapes used for the other operations do not multiply"),
            ],
            page="matrix-shear-cost",
            frm=["lower-factorization", "controlled-shifts", "address-shear", "linear-algebra-basics", "modular-arithmetic-and-residue-classes"],
        ),
        infer("S1.2.1.3", r"Whole rows are dealt cyclically into $W$ role streams within each prefix, each of identical remaining shape and volume $V/W$, so that gates act pointwise at matching addresses.",
              r"Split whole rows cyclically into $W$ role streams within each prefix",
              page="row-splitting-roles",
              frm=["stream-ops", "address-fields-volume", "network-frames"]),
        infer("S1.2.1.3b", r"Applying the shear $\Phi_{A_e}$ on every edge and the gates pointwise, the common-frame identity gives the shear $H\leftarrow H+D$ on every original row, including rows of scratch roles.",
              r"is $H\leftarrow H+D$ on every original row, including rows assigned"),
        infer("S1.2.1.3c", r"The updates $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ interchange the two full chunks, and only the middle shear uses the network.",
              r"To interchange the two full chunks, perform"),
        key,
        dfs,
    ],
    page="power-width-interchange",
    frm=["bit-network-interface", "network-frames", "address-shear", "stream-ops", "address-fields-volume", "permutations-and-bijections"],
    adds=[B("e", "chunk width", "The number of radix-$q$ digits in each of the two chunks, a power $m^k$ of the label dimension.", "count")],
)

swap2 = show(
    "S1.2.2",
    r"Arbitrary-width interchange of two $u$-bit chunks reduces to the power-width case by peeling top digits to supply rows, padding the row count to a multiple of $W^k$, cutting the rest in base $m$, and padding binary ranges to radix-$q$ ranges.",
    "Supply the missing rows from the chunks' own high digits and decompose the remaining width as a base-$m$ sum of power widths.",
    M("The fast operation needs many rows and power widths; a few high digits of the array itself can serve as rows and any width is a short base-$m$ sum of powers.", "explicit",
      r"Rows for a general array can be supplied by a few of its own high digits."),
    [
        infer("S1.2.2.1", r"Write each chunk as its top $\rho$ digits followed by the remaining digits; interchange the high parts one pair at a time and join them to form a row field of range $q^{2\rho}\ge W^k$.",
              r"Write each chunk as its top $\rho$ digits followed by its remaining"),
        infer("S1.2.2.2", r"Appending zero rows within each prefix raises the row count to a multiple of $W^k$ with less than doubling the volume.",
              r"Append zero rows, separately within"),
        infer("S1.2.2.3", r"Write the remaining width in base $m$ and apply the power-width interchange to each corresponding pair of pieces.",
              r"Write the remaining width in base $m$:"),
        infer("S1.2.2.4", r"The costs of the pieces sum geometrically to $O(Ve^\tau)$ because $a_j<m$ and $m^k<me$.",
              r"The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a"),
        infer("S1.2.2.5", r"For binary chunks, pad each range from $[2^u]$ to $[q^e]$ with $e$ least such that $q^e\ge2^u$, at a fixed-factor cost, and scan the padding away afterwards.",
              r"Finally, for binary chunks let $e$ be the least integer with"),
        infer("S1.2.2.6", r"Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$.",
              r"Since $e=O(u)$ for fixed $q$, the bound is"),
    ],
    frm=["stream-ops", "sets-products-of-ranges-and-lexicographic-order"],
)

s12 = show(
    "S1.2",
    r"For a fixed $\tau<1$, any two disjoint address chunks of $u$ bits in an array whose addresses form a complete Cartesian product of volume $V$ can be interchanged in $O(Vu^\tau)$ steps.",
    "Use the fixed bit network recursively for widths that are powers of $m$ and have enough rows, then reduce arbitrary widths to that case.",
    M("An edge matrix of rank $a$ costs $a$ smaller interchanges, and the total rank is below the number of wires times $m$, so the recurrence saves a power of the chunk width.", "explicit",
      r"the resulting recurrence saves a power of the chunk width."),
    [pw, swap2],
    page="chunk-swap",
    frm=["stream-ops", "address-fields-volume", "sets-products-of-ranges-and-lexicographic-order", "permutations-and-bijections"],
    salient="The final effect is an exact permutation of the data for arbitrary initial contents of the scratch rows, although the intermediate steps form XOR combinations of data across rows.",
)

# ---------------------------------------------------------------- S1.3 simultaneous layer
pfl = show(
    "S1.3.1",
    r"$C^{\otimes e}$ on $e=mf$ selected bits is computed by changing binary basis with packed row additions, applying $(C^{\epsilon})^{\otimes f}$ on each of $s_{\rm c}$ residual-basis slots of $f$ chunks, and changing back, with inverse kernels costing no extra child.",
    "Conjugate each edge's residual basis to coordinate directions by an invertible binary matrix, so that every directional kernel acts on one slot of $f$ chunks and becomes a child call.",
    M("An edge's frame change is a product of kernels along arbitrary directions; the invertible binary change of basis moves these to coordinate directions without needing to preserve the dot product.", "recoverable"),
    [
        infer("S1.3.1.1", r"Extending the residual basis to a basis of $\mathbb F_2^m$ gives $M$ with $\mathcal C_{U_+}\mathcal C_{U_-}^{-1}=\mathcal P_M\big(\prod_j C_{e_j}^{\epsilon_j}\big)\mathcal P_M^{-1}$.",
              r"Extend $v_1,\ldots,v_{\rho_{\rm edge}}$ to a basis of $\mathbb F_2^m$ and take these vectors as"),
        infer("S1.3.1.2", r"On a group of $m$ slots of $f$ chunks, apply $\mathcal P_M^{-1}$ to each column, one child $(C^{\epsilon_h})^{\otimes f}$ per slot $h$, then $\mathcal P_M$.",
              r"To implement \eqref{eq:phase-edge-coordinate} on the group, first apply"),
        infer("S1.3.1.3", r"A negative directional kernel still needs only one forward child because $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$.",
              r"A negative directional kernel still requires only one"),
        infer("S1.3.1.4", r"Gaussian elimination writes $M$ as at most $m(m-1)+3m$ elementary row additions, each acting on corresponding selected bits of two whole slots.",
              r"Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$"),
        infer("S1.3.1.5", r"One network invocation on $e=mf$ axes has exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
              r"$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
        infer("S1.3.1.6", r"Each inverse child comes from one forward call, and none of the corrections adds a child.",
              r"each inverse child from one forward call, and none of the corrections"),
    ],
    page="phase-frame-layer",
    frm=["phase-kernel", "complex-network-interface", "f2-vectors", "linear-algebra-basics", "tensor-products"],
    adds=[B("e", "selected axes", "The number of consecutive axis chunks whose selected bits receive the kernel in one call, equal to $mf$.", "count"),
          B("f", "chunks per slot", "The number of consecutive $K$-bit chunks in each of the $m$ slots of a group.", "count")],
)

h0c = infer(
    "S1.3.2",
    r"The normalized layer is obtained from the phase-kernel layer by $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, with $\mathcal S_D$ a diagonal fourth-root phase and $b^D$ a binary shift and phase.",
    r"\eqref{eq:phase-basic-identities} on all selected coordinates gives",
    frm=["phase-kernel"],
)

packed_rot = show(
    "S1.3.3.1",
    r"Eight conditional cyclic shifts flip the parity of $u$ when the control $c$ is $1$ and restore $w$; applied simultaneously to the $f-1$ disjoint $K$-bit segments as single cyclic shifts of whole chunk ranges, they agree with the ideal XORs unless a guard value is near the segment boundary.",
    "Compose eight carry-free parity-conditioned additions into a parity flip, and place the segments side by side so that one shift of the target chunk applies all of them.",
    M("Each shift offset depends only on the two control chunks and never on the target, so a shift of a whole chunk range is a bijection that can be done at linear cost, and many segments share one shift.", "recoverable"),
    [
        infer("S1.3.3.1.1", r"The eight operations flip the parity of $u$ precisely when $c=1$, preserve both quotients under division by two, and restore the arbitrary auxiliary integer $w$.",
              r"Here $u\bmod2\in\{0,1\}$, also for negative $u$. Thus the parity of $u$"),
        infer("S1.3.3.1.2", r"Each line applied simultaneously to all segment pairs is a single cyclic shift $y\leftarrow y+\varepsilon\sum_i2^{j_i}[x_{j_i}=1][z_{j_i}=b]\pmod{2^L}$.",
              r"Apply each line of \eqref{eq:eight-packed-additions} simultaneously to all"),
        infer("S1.3.3.1.3", r"The shift offset never depends on its target chunk, so each line is a bijection of the rectangle.",
              r"The shift offset never depends on its target chunk, so each line is a"),
    ],
    page="packed-rotations",
    frm=["f2-vectors", "modular-arithmetic-and-residue-classes"],
)

exc_rep = show(
    "S1.3.3.2",
    r"The packed rotations agree with the ideal map off a set $\mathcal B$ of addresses of fraction at most $80(f-1)2^{-K}$; the rotations are realized by chunk swaps and controlled shifts, and the records of $\mathcal B$ are extracted, sorted by destination rank and reinserted, keeping the bound worst-case.",
    "Count the bad addresses by a union bound over guard values, observe that the ideal and rotated maps are bijections that agree off the bad set, and repair that set separately by stable radix sort.",
    M("The failure set depends only on addresses, not payloads, and is a tiny fraction of the stream, so sorting just those records is cheap and the time bound holds for every payload.", "recoverable"),
    [
        infer("S1.3.3.2.1", r"At an address outside $\mathcal B$ each segment lies in $[20,2^K-21]$, so even displacement eight causes no carry into or borrow from the next segment.",
              r"At an address outside $\mathcal B$, each segment initially lies"),
        infer("S1.3.3.2.2", r"There are exactly twenty excluded values per guard out of $2^{K-1}$, and the union bound over $2(f-1)$ guards gives $|\mathcal B|\le\delta_{\rm bad}M$.",
              r"the union bound over the $2(f-1)$ guards gives"),
        infer("S1.3.3.2.3", r"$T_0S_0^{-1}$ fixes the complement of $\mathcal B$ and permutes $\mathcal B$.",
              r"Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$."),
        infer("S1.3.3.2.4", r"Each rotation moves its target after its controls using one chunk swap of cost $O(VL^\tau)$.",
              r"Pass only $L$ and these three positive canonical lengths to"),
        infer("S1.3.3.2.5", r"The controlled cyclic shift then costs $O(V)$ because its offset work is absorbed by the $2^L$ target blocks in each fiber.",
              r"therefore gives an $O(V)$ rotation: its offset work is absorbed by the"),
        infer("S1.3.3.2.6", r"Scan the stream with a record-rank counter, test membership in $\mathcal B$, and extract just those records with their destination ranks.",
              r"Test membership in $\mathcal B$ and extract just"),
        infer("S1.3.3.2.7", r"Stable binary radix sorting on the destination keys scans only the extracted records.",
              r"while stable binary radix sorting scans only the extracted records and"),
        infer("S1.3.3.2.8", r"One forward full-stream scan reinserts the sorted records, implementing $T_0$ everywhere.",
              r"One forward full-stream scan reinserts the sorted records."),
    ],
    page="exceptional-address-repair",
    frm=["sorting-and-radix-sort", "elementary-counting-and-the-union-bound", "permutations-and-bijections", "chunk-swap", "controlled-shifts"],
)

psba = show(
    "S1.3.3",
    r"One fixed multitape procedure XORs the selected bit (offset $\rho$) of each of $f$ chunks of $K$ bits of chunk $x$ into chunk $y$ while restoring chunk $z$, in time $O(V(L^\tau+1))$ plus negligible repair terms.",
    "Do $f-1$ of the XORs at once by packed carry-free rotations, repair the exceptional addresses where guards fail, and do the last bit directly.",
    M("A binary row addition is needed on selected bits of whole chunks; doing the $f$ bits one by one would be too slow, while packing them into one cyclic shift uses the fast chunk interchange.", "recoverable"),
    [
        packed_rot,
        exc_rep,
        infer("S1.3.3.3", r"Finally the two-bit XOR on the omitted most significant selected position is applied by an elementary stream operation in $O(V)$.",
              r"Finally apply the two-bit XOR to $x_{j_{f-1}},y_{j_{f-1}}$ by"),
        infer("S1.3.3.4", r"Movement costs $O(V(L^\tau+1))$ and the full-record scans and radix passes add only terms that vanish after division by $V$.",
              r"Equation~\eqref{eq:packed-bad-fraction} proves"),
        infer("S1.3.3.5", r"A fixed binary change of basis and its inverse therefore cost $O(V((eK)^\tau+1))$.",
              r"the complete change of basis and its inverse therefore cost"),
    ],
    page="packed-selected-bit-addition",
    frm=["chunk-swap", "controlled-shifts", "stream-ops", "f2-vectors"],
)

unroll = show(
    "S1.3.4.7",
    r"With $F(e)$ the time divided by volume, $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ and $F(e)=O(e)$ below $d^\beta$; this solves to $O(d^{\lambda'})$ for the whole layer.",
    "Unroll the recurrence of the rank-deficit lemma, charging the overhead at internal nodes $O(e^\\lambda)$ and the leaves $O(e^\\sigma d^{\\beta(1-\\sigma)})$, then sum over the base-$m$ pieces.",
    M("The same strict rank deficit $s/W<m^\\sigma$ makes the internal costs a convergent geometric series and keeps the leaf cost a power of $d$ below one.", "recoverable"),
    [
        infer("S1.3.4.7.1", r"The $s$ child calls run on streams of volume $V/W$, so dividing by $V$ gives the factor $s/W$.",
              r"Indeed, the \(s\) child calls are executed on streams of volume"),
        infer("S1.3.4.7.2", r"At an internal node $e\ge d^\beta$, hence $K\le d^c\le e^{c/\beta}$, so the overhead is $O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)$.",
              r"At an internal node \(e\ge d^\beta\), hence"),
        infer("S1.3.4.7.3", r"Since $a=s/W\le m^\sigma<m^\lambda$, the internal costs sum to $O(e^\lambda)$.",
              r"Since \(a\le m^\sigma<m^\lambda\), the internal"),
        infer("S1.3.4.7.4", r"The leaves with $u<d^\beta$ chunks contribute $O(e^\sigma d^{\beta(1-\sigma)})$.",
              r"contribution is at most"),
        infer("S1.3.4.7.5", r"Writing $D-q_0$ in base $m$ and adding the costs of the pieces and of the row preprocessing gives $O(d^{\lambda'})$.",
              r"Adding their costs and the row preprocessing gives"),
    ],
    frm=["rank-deficit-recurrence", "recurrences-and-geometric-series"],
)

batch = show(
    "S1.3.4",
    r"A common $C^{\otimes D}$ layer on $D\le d$ chunks is run on a fixed number of tapes in time $O(Vd^{\lambda'})$ by recursing on $e=m^k$ chunks with rows dealt among the $W$ wire roles.",
    "Obtain the rows from the first few chunks, deal them cyclically to the wire roles so each child has volume $V/W$, run the children on a stack, and unroll the resulting recurrence.",
    M("The strict saving $s/W<m^\\sigma$ only helps if each child really has $1/W$ of the volume, which requires enough rows to split among the roles.", "recoverable"),
    [
        infer("S1.3.4.1", r"Individual $C$ kernels are applied by splitting on the selected bit, scanning aligned record pairs, and merging; $e$ of them cost $O(Ve)$.",
              r"Thus \(e\) individual kernels cost"),
        infer("S1.3.4.2", r"At an internal node with $e=m^k$ chunks there is one recursive call on a slot for each residual basis vector, hence exactly $s$ calls, and the basis changes and scalar gates cost $O(V((eK)^\tau+1))$.",
              r"The phase construction supplies one recursive call on a slot for each"),
        infer("S1.3.4.3", r"If $D>q_0$, apply $C$ individually on the first $q_0$ chunks, whose concatenated bits serve as the row index.",
              r"Otherwise apply \(C\) individually on the selected bits of the first"),
        infer("S1.3.4.4", r"Zero rows are added within each prefix to reach the next multiple of $W^{k_0}$, at most doubling the volume.",
              r"the same number of zero rows to reach the next multiple of \(W^{k_0}\);"),
        infer("S1.3.4.5", r"Writing a row index as $u=Wg+w$, the whole row goes to role $w$, so every role stream has the same shape and each child has exactly $1/W$ of the parent's volume.",
              r"At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\),",
              frm=["row-splitting-roles"]),
        infer("S1.3.4.6", r"The other role streams are pushed on a LIFO tape while a child runs and popped on return, at a cost of a constant times the node's volume.",
              r"child, push the other role streams onto a LIFO work tape, copy the",
              frm=["fixed-tape-dfs-schedule"]),
        unroll,
    ],
    frm=["fixed-point-arithmetic", "row-splitting-roles", "fixed-tape-dfs-schedule", "rank-deficit-recurrence", "chunk-swap"],
)

gw = show(
    "S1.3.5",
    r"The whole recursive $C$-layer is evaluated exactly with $p+\Delta$ fractional bits and $\Delta+3$ integer bits, where $\Delta=\lceil C_0d^{C_1}\rceil$ bounds the arithmetic depth via $A(e)\le sA(e/m)+E$, so $\Delta=o(p)$ and all widths are $O(p)$.",
    "Bound the number of additions, halvings and phase operations on any chain from an input coefficient to an intermediate one by a recurrence, then convert depth to growth of magnitude and denominator.",
    M("Each addition at most doubles the modulus and each halving adds one denominator bit, so a bound on the arithmetic depth bounds the number of extra bits needed.", "recoverable"),
    [
        infer("S1.3.5.1", r"Every wire occurs in at most twelve scalar gates, so all gates, corrections and bank exchanges cost fewer than $E=64(W+m+1)^3$ operations per node.",
              r"The scalar schedule \eqref{eq:motif-schedule} touches a data wire"),
        infer("S1.3.5.2", r"A paired evaluation of a single $C$ kernel uses at most eight elementary operations, so $A(e)\le8e$ at a leaf.",
              r"The paired evaluation in \eqref{eq:individual-C-pair} uses at most"),
        infer("S1.3.5.3", r"There are at most $\lceil\log_md\rceil$ internal levels, and the recurrence gives $A(e)\le8B^2d^{\nu+1}$ with $B=s+E$.",
              r"There are at most \(k\le\lceil\log_m d\rceil\) internal levels."),
        infer("S1.3.5.4", r"A value at depth $\ell$ lies in $2^{-(p+\ell)}\mathbb Z[i]$ and has modulus at most $2^\ell$.",
              r"lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most"),
        infer("S1.3.5.5", r"Since $\epsilon C_1<1$ and $d=\Theta(p^\epsilon)$, $\Delta=o(p)$ and the full coefficient width is $O(p)$.",
              r"\(\Delta=o(p)\), and the full coefficient width is \(O(p)\), as"),
    ],
    page="guard-width",
    frm=["fixed-point-arithmetic", "recurrences-and-geometric-series", "complex-network-interface", "phase-frame-layer"],
)

s13 = show(
    "S1.3",
    r"The normalized butterfly $H_0$ is applied at once to the same bit offset of $D\le d$ address chunks of every polynomial record in $O(Vd^{\lambda'})$ time with $\lambda'<1$; the layer is evaluated exactly and followed by one truncation with error below $\sqrt2\,2^{-p}$.",
    "Write $H_0^{\\otimes D}$ through the phase-kernel power $C^{\\otimes D}$, evaluate that by the complex phase network recursively with packed binary basis changes and rows dealt among the wire roles, keep all intermediate values exact, and truncate once.",
    M("Separate butterfly factors would need $D$ whole-array passes; the recursive network with a strict rank deficit does the $D$ factors together for a power of $d$ instead of $D$ passes.", "explicit",
      r"factors would require $D$ whole-array passes."),
    [
        pfl, h0c, psba, batch, gw,
        infer("S1.3.6", r"The row construction and the recurrence analysis give total time $O(Vd^{\lambda'})$ on fixed tapes, including all padded and auxiliary streams.",
              r"The row construction and the recurrence analysis"),
        infer("S1.3.7", r"The guard-width bound is $o(p)$, so every intermediate coefficient of a record of $r$ coefficients is represented exactly in $O(p)$ bits before the final truncation.",
              r"The guard-width calculation above bounds both denominator and magnitude"),
        infer("S1.3.8", r"Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays and truncation toward zero adds error less than $\sqrt2\,2^{-p}$.",
              r"Finally, every row of $\mathcal H$ has",
              frm=["disk-grid-truncation", "contraction-error-budget"]),
    ],
    page="simultaneous-layer",
    frm=["fixed-point-arithmetic", "disk-grid-truncation", "contraction-error-budget", "polynomials", "complex-numbers"],
    salient="One simultaneous layer on $D$ chunks costs a power $d^{\\lambda'}$ with $\\lambda'<1$ per unit volume, instead of the $D$ separate passes that $D$ individual butterflies would take.",
    adds=[B("D", "selected chunks", "The number of address chunks in which the layer acts on the same bit offset, at most $d$.", "count"),
          B("d", "chunk bound", "The upper bound on the number of axes, a small power of the precision $p$.", "direct"),
          B("K", "chunk width", "The number of bits in each address chunk, a small power of $d$.", "count"),
          B("p", "precision", "The number of fractional bits of each real or imaginary coefficient part.", "count"),
          B("r", "record length", "The number of complex coefficients in each polynomial record.", "count")],
)

s1 = show(
    "S1",
    r"Two fixed-tape procedures save a power of the width: an interchange of two $u$-bit address chunks in $O(Vu^\tau)$ and a simultaneous butterfly layer on $D\le d$ chunks in $O(Vd^{\lambda'})$, both from linear networks with $s<Wm$ and logical volume $V$.",
    "Build one finite linear network per primitive that exchanges two banks and restores all scratch values, then turn the strict deficit $s<Wm$ in its frame changes into a recursion on narrower fields that saves a power.",
    M("Scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels costs $\\Theta(n\\log n)$, so address rearrangement and butterfly arithmetic each need a saving.", "explicit",
      r"We therefore need savings in both movement and arithmetic."),
    [s11, s12, s13],
    adds=[B("V", "logical volume", "The number of stored data bits of an array.", "count"),
          B("W", "wire count", "The number of wires, counting scratch wires, of the finite network.", "count"),
          B("m", "label dimension", "The dimension of the label space, equal to the number of fields into which a chunk is cut.", "count"),
          B("s", "total rank", "The sum over all edges of the ranks of the frame changes, equal to the number of smaller calls.", "count")],
)

# ---------------------------------------------------------------- S2 synthetic convolution
st = show(
    "S2.1",
    r"The normalized transforms $F_t^\pm$ over $\mathcal R_r$ with synthetic roots $\omega_t=y^{2r/t}$ are contractions, satisfy $F_t^+F_t^-=t^{-1}I$ despite zero divisors, and are computed by radix-two butterflies and monomial twiddles.",
    "Prove the character sum vanishes by pairing summands with a shift that multiplies the sum by $-1$, then expand the composite transform; compute the transform by decimation in frequency.",
    M("The ring has zero divisors, so one cannot divide by $\\omega_t^j-1$ to evaluate the character sum.", "explicit",
      r"The ring has zero divisors, so we verify character cancellation"),
    [
        infer("S2.1.1", r"Every power of $\omega_t$ is an isometry and each transform entry is an average of $t$ such images, so both transforms are contractions.",
              r"Every power of $\omega_t$ is an isometry, and each transform entry is"),
        infer("S2.1.2", r"Replacing $k$ by $k+t/2^{v+1}$ permutes the summands and multiplies the sum by $-1$, so it is zero and $F_t^+F_t^-=t^{-1}I$.",
              r"Hence the sum is zero, since the additive group of"),
        infer("S2.1.3", r"The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$, applies $H_0$, multiplies the second output by $\omega_t^{-k}$ and recurses within the two branches, which computes $F_t^-$.",
              r"procedure separately within the two branches."),
    ],
    page="synthetic-transform",
    frm=["polynomial-ring-negacyclic", "dft", "synthetic-roots", "fft-butterfly", "roots-of-unity"],
)

fo = show(
    "S2.2",
    r"The decimation-in-frequency recursion writes frequency $j$ in slot $\operatorname{rev}(j)$; the forward $B_tF_t^-$ keeps this order and the opposite procedure $F_t^+B_t^{-1}$ consumes it directly.",
    "Track which address bits hold branch bits at each level, then run the recursion backwards, using $H_0^2=I/2$ to see that the reversed levels compose with the forward ones to $I/t$.",
    M("Writing outputs where the recursion leaves them avoids a sort between the forward and opposite transforms.", "recoverable"),
    [
        infer("S2.2.1", r"After all $a$ rounds the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$.",
              r"entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$."),
        infer("S2.2.2", r"The reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$, so the two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
              r"so the reverse procedure composed with $B_tF_t^-$ is"),
    ],
    page="frequency-order",
    frm=["fft-butterfly", "synthetic-transform", "permutations-and-bijections"],
)

tl = show(
    "S2.3",
    r"A positional layout permutation $L$ moves chosen bit slots to a prefix and groups the rest into $K$-bit chunks, so each of the $\ell$ rounds is a simultaneous butterfly layer; each transform costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\,\ell\,2^{-p}$.",
    "Place the selected bits of all participating axes at a common offset in consecutive $K$-bit chunks by prefix moves and chunk exchanges, then apply the simultaneous layer once per round.",
    M("The simultaneous layer needs the selected bits of the participating axes at a common offset in consecutive chunks.", "explicit",
      r"we must place the selected bits of the participating axes at a common"),
    [
        infer("S2.3.1", r"The individual axis steps of a round group into a parallel butterfly followed by one recordwise monomial multiplication $J_E$.",
              r"Consequently the individual axis steps may be grouped as a parallel"),
        infer("S2.3.2", r"Moving the at most $D(b+1)=O(dK)$ listed slots to a prefix costs $O(TpdK)$.",
              r"listed slots, so the moves cost $O(TpdK)$."),
        infer("S2.3.3", r"The remaining chunks are reordered by scanning target positions left to right and exchanging chunks.",
              r"To obtain this order, scan its target positions from left to right."),
        infer("S2.3.4", r"At most $Dq-1$ exchanges of width-$K$ chunks cost $O(Tp\cdot pK^{\tau-1})$ in total.",
              r"exchanges of width-$K$ address chunks, even when the chunks are"),
        infer("S2.3.5", r"The simultaneous-layer procedure applies at cost $O(Tp\,d^{\lambda'})$ per round and $O(Tp\,\ell d^{\lambda'})$ in total.",
              r"The simultaneous-layer procedure therefore applies at cost"),
        infer("S2.3.6", r"At most $b+1\le K$ rounds on prefix slots are done bit by bit, giving cost $O(TpdK)$.",
              r"most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$."),
        infer("S2.3.7", r"The monomial commutes with truncation, so the call sequence returns exactly the result of truncating once after the exact contraction round.",
              r"Thus the actual forward call sequence returns exactly the result of"),
        infer("S2.3.8", r"Each contraction round adds at most one truncation error less than $\sqrt2\,2^{-p}$, so at most $\ell$ rounds give the claimed error and disk bounds.",
              r"give the claimed error and disk bounds."),
    ],
    page="transform-layout",
    frm=["synthetic-transform", "frequency-order", "simultaneous-layer", "chunk-swap", "stream-ops", "multidim-dft", "contraction-error-budget", "disk-grid-truncation"],
    adds=[B(r"\ell", "ring exponent", "The base-two logarithm of the record length $r$.", "direct"),
          B("T", "box size", "The total number of coefficient slots, the product of $r$ and the number of records.", "count")],
)

sp = show(
    "S2.4",
    r"Two disk-grid polynomials in $\mathcal R_r$ are multiplied exactly by evaluating coefficients at $B_0=2^{4p}$ as signed integers, multiplying with the established multiplier, extracting centered coefficients, wrapping negacyclically and truncating, in $O(rp\log(rp))$.",
    "Use a signed form of Kronecker substitution: pack coefficients as digits of a large integer with enough room that products do not overlap, multiply the integers, then read the digits back.",
    M("The established integer multiplier is available as a subroutine, so ring products reduce to integer products once the coefficients are packed with room for the sums.", "recoverable"),
    [
        infer("S2.4.1", r"The four products $A_aA_c$, $A_bA_e$, $A_aA_e$, $A_bA_c$ of absolute values are computed by the established multiplier, each on $O(rp)$ bits.",
              r"pairs of absolute values using the established multiplier and restore"),
        infer("S2.4.2", r"Since $|h_j|<B_0/2$, the centered residue modulo $B_0$ after removing lower coefficients identifies each coefficient.",
              r"this strict bound identifies the next coefficient by its centered"),
        infer("S2.4.3", r"Each reduced coefficient is a sum of exactly $r$ signed products of coefficients of modulus at most $2^p$, so $|H_j|\le r2^{2p}$.",
              r"resulting Gaussian integer coefficient $H_j$ is a sum of exactly"),
        infer("S2.4.4", r"Shifting the magnitude right by $p+\ell$ bits and restoring the sign gives the grid numerator of the normalized product.",
              r"To implement it, shift the absolute magnitude right by $p+\ell$"),
        infer("S2.4.5", r"The four exact integer products dominate the linear packing, extraction, combination, wrapping and truncation costs.",
              r"Four exact integer products dominate the linear"),
    ],
    page="signed-packing",
    frm=["established-multiplier", "polynomial-ring-negacyclic", "disk-grid-truncation", "binary-and-radix-b-representation-of-integers", "schoolbook-multiplication-and-karatsuba"],
)

s2 = show(
    "S2",
    r"Normalized convolution $\mathcal M_r(f,g)=(f*g)/(rM)$ over $\mathcal R_r$ on $M$ records is computed from two forward synthetic transforms that keep their layout, pointwise ring products by signed packing and the opposite transform, with error below $\sqrt2\,M(3\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.",
    "Apply the convolution theorem in the ring: transform both operands, multiply pointwise, apply the opposite transform, passing the stored frequency order straight through.",
    M("Pointwise multiplication commutes with the same record permutation applied to both operands, so the forward outputs can be multiplied in their retained order.", "explicit",
      r"forward outputs in their retained order and pass that order directly"),
    [
        st, fo, tl, sp,
        infer("S2.5", r"The normalized convolution $\mathcal M_r$ averages $rM$ signed scalar products per coefficient and is a bilinear contraction.",
              r"$rM$ signed scalar products, and $\mathcal M_r$ is a bilinear"),
        infer("S2.6", r"Perform both forward transforms and retain their common $LB$ order, multiply corresponding records by signed packing, apply the opposite procedure and scale exactly by $M$.",
              r"Perform both forward transforms and retain their common $LB$ order."),
        infer("S2.7", r"Expansion of the finite sums gives $F^-_{\boldsymbol t}(f*g)=M(F^-_{\boldsymbol t}f)(F^-_{\boldsymbol t}g)$, and with $F^+F^-=I/M$ the scaled result is $(f*g)/(rM)$.",
              r"To check normalization, expansion of the finite sums gives"),
        infer("S2.8", r"Since $LB$ permutes records and leaves polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$, so the opposite transform applied to the pointwise product of stored outputs equals $F^+P(F^-f,F^-g)$.",
              r"Since $LB$ permutes records and leaves their polynomial suffixes"),
        infer("S2.9", r"With forward errors below $\delta=\sqrt2\ell2^{-p}$, the bilinear map and the contraction $\mathcal T_+$ give error below $M(3\delta+\eta)=\sqrt2M(3\ell+1)2^{-p}$.",
              r"For the error estimate, put",
              frm=["contraction-error-budget", "triangle-inequality-and-error-bounds"]),
        infer("S2.10", r"There are $M=T/r$ pointwise products, costing $O(Tp\log(rp))$ in total, and the three transforms cost as stated.",
              r"There are $M=T/r$ pointwise polynomial products."),
    ],
    page="synthetic-convolution",
    frm=["cyclic-convolution", "contraction-error-budget", "polynomial-ring-negacyclic"],
    salient="The frequency order is never undone between the pointwise product and the opposite transform: the stored layout permutation $LB$ commutes with pointwise multiplication, so no sort is executed there.",
    adds=[B("M", "record count", "The number of polynomial records in the array, equal to $T/r$.", "count")],
)

# ---------------------------------------------------------------- S3 reduction
gr = show(
    "S3.1.1",
    r"For coprime $s<t$ with $t/s-1>p/\alpha^4$ there are contractions $A,B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computed with error below $p^2$ in $O(tp^{3/2+\delta}\alpha)$, and the two coordinate permutations stay in the identity.",
    "Take the Gaussian resampling maps of Harvey and van der Hoeven, use the left inverse of $N=C\\mathsf T\\mathsf D$ to cancel the inverse Gaussian, and normalize to contractions.",
    M("The Neumann series inverts $N$ because $\\|N-I\\|<1/2$ under the stated separation of $s$ and $t$.", "recoverable"),
    [
        infer("S3.1.1.1", r"The exact Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$ and the estimate $\|N-I\|<2^{-\alpha^2\theta}$ are quoted from Harvey and van der Hoeven.",
              r"The exact Gaussian identity and inverse estimate proved in"),
        infer("S3.1.1.2", r"Set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$, both contractions.",
              r"Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$."),
        infer("S3.1.1.3", r"Applying the left inverse $\mathsf DN^{-1}C$ of $\mathsf T$ to the Gaussian identity gives $P_sF_s$, and the normalizations multiply to $2^{-2\alpha^2}$.",
              r"Applying this left inverse to the first identity in"),
        infer("S3.1.1.4", r"The ordered numerical maps have errors below $16p$ and $4+3p^2/4$ and time $O(tp^{3/2+\delta}\alpha)$.",
              r"Consequently we may take"),
        infer("S3.1.1.5", r"In the original proof the permutations $P_t$ and $P_s^{-1}$ are executed by two label-and-sort operations; here they remain in the transform identity.",
              r"In \eqref{eq:no-sort-one-dimensional} these permutations remain in the"),
    ],
    page="gaussian-resampling",
    frm=["dft", "contraction-error-budget", "disk-grid-truncation", "established-multiplier", "divisibility-primes-and-gcd", "real-and-imaginary-parts-rounding-and-truncation"],
)

tr = show(
    "S3.1.2",
    r"Applying the resampling identity along each of $d$ axes of a padded power-of-two box gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ at cost $O(dTp^{3/2+\delta}\alpha)$ for the line maps plus $O(Tp\,d^2(1+\ell^\tau))$ for data movement.",
    "Tensor the one-dimensional identity, expand and compress one axis at a time in the zero-padded box, and expose each axis by chunk interchanges.",
    M("The chunk-swap algorithm supplies the movement of the physical axis fields, including its cost when the number of axes grows.", "explicit",
      r"line at a time. The chunk-swap algorithm supplies the movement of the"),
    [
        infer("S3.1.2.1", r"Tensoring the one-dimensional identity proves $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$.",
              r"Tensoring \eqref{eq:no-sort-one-dimensional} proves"),
        infer("S3.1.2.2", r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$, so the line maps cost $O(dTp^{3/2+\delta}\alpha)$.",
              r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$,"),
        infer("S3.1.2.3", r"Each adjacent interchange of axis fields costs $O(Tp(1+\ell^\tau))$ by the chunk swap.",
              r"costs $O(Tp(1+\ell^\tau))$. Exposing and restoring one axis needs"),
        infer("S3.1.2.4", r"Exposing and restoring all axes needs $O(d^2)$ adjacent interchanges.",
              r"$O(d)$ adjacent interchanges, hence all axes need $O(d^2)$. These are"),
        infer("S3.1.2.5", r"Since $t_i\ge r/2$, at most $2dT/r$ lines are invoked, so setup per line is negligible.",
              r"Since $t_i\geq r/2$, each tensor map invokes at most"),
    ],
    page="tensor-resampling",
    frm=["chunk-swap", "tensor-products", "gaussian-resampling", "stream-ops", "multidim-dft"],
)

bl = infer(
    "S3.1.3",
    r"The middle transform is a chirp convolution: $QF_{\boldsymbol t}u=\overline a\cdot\big(a*(\overline a\cdot u)\big)/T$ for the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$.",
    r"This is precisely the coefficient in $QF_{\boldsymbol t}$, because",
    page="bluestein-chirp",
    frm=["dft", "cyclic-convolution", "multidim-dft", "roots-of-unity"],
)

spc = show(
    "S3.1.4",
    r"The retained source permutation $R$ cancels: $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$ with $S=\prod_is_i$.",
    "Show that the dilation $R$ satisfies $RF^+R=F^+$ and commutes with pointwise products, then use the convolution theorem and $F^+F=I/S$.",
    M("The opposite-sign transform undoes the dilation by $R$ that the forward transforms introduced, so the permutation never needs to be executed.", "recoverable"),
    [
        infer("S3.1.4.1", r"Since each $t_i$ is a unit mod $s_i$, $F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.",
              r"$F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence"),
        infer("S3.1.4.2", r"A coordinate permutation commutes with pointwise products.",
              r"because a coordinate permutation commutes with pointwise products."),
        infer("S3.1.4.3", r"With $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$ and $F^+F=I/S$, the product is $(u*v)/S^2$.",
              r"The normalized convolution rule is"),
        infer("S3.1.4.4", r"Conjugating input and output of an algorithm for $RF_{\boldsymbol s}$ gives one for $RF_{\boldsymbol s}^+$.",
              r"proving \eqref{eq:source-permutation-cancel}. Finally, conjugation"),
    ],
    page="source-permutation-cancel",
    frm=["dft", "cyclic-convolution", "multidim-dft", "permutations-and-bijections", "modular-arithmetic-and-residue-classes", "gaussian-resampling"],
    salient="The right-hand side contains no permutation at all: the same retained permutation appears in both forward transforms and in the opposite transform, so the product $RF^+[(RFu)(RFv)]$ is the pure scaled convolution $(u*v)/S^2$.",
)

s31 = show(
    "S3.1",
    r"Each source Fourier transform $RF_{\boldsymbol s}$ of pairwise coprime lengths equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with the permutations retained, the middle power-of-two transform $QF_{\boldsymbol t}$ is a chirp convolution, and $R$ cancels across the two forward transforms, the pointwise product and the opposite transform.",
    "Use Gaussian resampling along each axis to pass from coprime lengths to powers of two, keeping both coordinate permutations inside the formula, and Bluestein's chirp identity to write the permuted power-of-two transform as a convolution.",
    M("Gaussian resampling usually sorts twice on each coordinate; retaining both permutations in the formula avoids executing them as separate sorts.", "explicit",
      r"coordinate. We retain both permutations in the transform formula and"),
    [gr, tr, bl, spc],
    frm=["dft", "cyclic-convolution"],
    salient="The two coordinate permutations of Gaussian resampling are never executed: they stay inside the transform identity and the source one cancels, which is what removes the full sorts that would cost $\\Theta(n\\log n)$ again.",
)

pc = show(
    "S3.2",
    r"From the input length $n$ the parameters are $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$ and axis lengths $t_i\in\{r/2,r\}$ with $\prod_it_i=T$, so that $Tp=\Theta(n)$.",
    "Fix tiny rational exponents so that every layer, transform and resampling hypothesis holds at once, then derive the sizes from $n$.",
    M("The layer, transform, resampling and cost conditions must all hold for one choice, so the exponents are chosen compatibly and deliberately conservatively.", "recoverable"),
    [
        infer("S3.2.1", r"Fix rational exponents $\tau=\sigma=1-2^{-50}$, $\lambda=1-2^{-52}$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\epsilon=2^{-75}$, $\delta=1/16$ and $\kappa=2^{-182}$.",
              r"Take the following fixed rational numbers:"),
        infer("S3.2.2", r"Take the power of two $T$ in $[4n/b,8n/b)$ and $r=2^{\lceil(\log_2T)/d\rceil}$, with $d\ell-\log_2T$ axis lengths $r/2$ and the rest $r$.",
              r"Take the power of two $T$ in $[4n/b,8n/b)$, and let"),
        infer("S3.2.3", r"The comparison constants can be fixed for every input length at once: $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$ and $C_\ell=1$.",
              r"Thus we fix $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, and $C_\ell=1$"),
    ],
    page="parameter-choice",
    frm=["logarithms-exponentials-floors-and-ceilings", "binary-and-radix-b-representation-of-integers", "simultaneous-layer", "transform-layout"],
    adds=[B("b", "bit length", "The ceiling of the base-two logarithm of the input length $n$.", "direct"),
          B("p", "working precision", "The number of fractional bits kept, equal to $6b$.", "count"),
          B("T", "padded box size", "The power-of-two number of entries of the padded box, about $n/b$.", "count")],
)

pl = show(
    "S3.3",
    r"Pairwise-distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ are found by trial division in time $n^{o(1)}$ and give $\gcd(s_i,t_i)=1$, $T/2<S<T$ and $\alpha^4\theta_i>p$.",
    "Count primes in the two explicit intervals using a prime-interval bound, take products to bound $S/T$, and read off the separation $\\theta_i=t_i/s_i-1$.",
    M("The product of the $s_i$ must fill a fixed fraction of the padded box while each ratio $t_i/s_i$ leaves enough separation for resampling.", "explicit",
      r"The distinct prime lengths $s_i$ must be close to the powers of two"),
    [
        infer("S3.3.1", r"The interval $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes, which exceeds $d$ for $x\in\{r/2,r\}$.",
              r"contains at least $\eta x/(2\log x)$ primes. Here $\log$ is the natural"),
        infer("S3.3.2", r"Distinct odd primes can therefore be chosen with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$, and $\gcd(s_i,t_i)=1$ since $t_i$ is a power of two.",
              r"We may therefore choose distinct odd primes satisfying"),
        infer("S3.3.3", r"By strict Bernoulli, $S/T>(1-1/(2d))^d>1/2$, and with $s_i<t_i$ this gives $T/2<S<T$.",
              r"Together with $s_i<t_i$, this gives $T/2<S<T$."),
        infer("S3.3.4", r"The separation satisfies $\theta_i>\eta$ and hence $\alpha^4\theta_i>3db\ge p$, as Gaussian resampling needs.",
              r"$\theta_i\geq\eta/(1-\eta)>\eta$. Therefore"),
        infer("S3.3.5", r"Scanning the intervals and trial division through square roots takes $n^{o(1)}=o(n)$ time.",
              r"Since $p=6\lceil\log_2 n\rceil=\Theta(\log n)$, the search takes"),
    ],
    page="prime-lengths",
    frm=["parameter-choice", "divisibility-primes-and-gcd", "elementary-counting-and-the-union-bound"],
)

digit = infer(
    "S3.4",
    r"The radix-$2^b$ digit polynomials have product of degree below $S$, so cyclic convolution modulo $x^S-1$ has no wraparound and each product coefficient is below $2^{3b}$.",
    r"Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
    frm=["multiplication-as-convolution", "binary-and-radix-b-representation-of-integers", "cyclic-convolution"],
)

crt = show(
    "S3.5",
    r"The map $x\mapsto\prod_ix_i^{\mu_i}$ with $\mu_i=P_i^{-1}\bmod s_i$ is an isomorphism from cyclic convolution of length $S=\prod_is_i$ to multidimensional cyclic convolution on the prime axes, implemented on padded axes by triangular controlled shifts in time $O(Tp\,d^2(1+\ell^\tau))$.",
    "Use the Chinese remainder split of Agarwal and Cooley with exponents chosen so that axis $i$ depends only on lower digits, making the change of order triangular controlled cyclic shifts.",
    M("The coordinate powers are chosen so that the change of order is a sequence of controlled cyclic shifts, which the controlled-shift lemma performs in linear time.", "explicit",
      r"algebraic split, with coordinate powers that make the change of order a"),
    [
        infer("S3.5.1", r"The map respects $x^S=1$, sends $x$ to an element of order $S$, and so is an isomorphism preserving cyclic convolution.",
              r"$\Phi$ is an isomorphism and preserves cyclic convolution."),
        infer("S3.5.2", r"The coordinate in axis $i$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, because terms with $j>i$ are divisible by $s_i$ and $\mu_iP_i=1$.",
              r"Indeed terms with $j>i$ are divisible by $s_i$, and $\mu_iP_i=1$ modulo"),
        infer("S3.5.3", r"Updating targets in the order $i=d,d-1,\ldots,1$ uses the original lower digits as controls.",
              r"the offset is computed from the original digits $a_j$ required by the"),
        infer("S3.5.4", r"Each step preserves the valid set and its complement, so zero padding remains zero after every step.",
              r"Each step preserves $\mathcal V$ and its complement."),
        infer("S3.5.5", r"The map, its inverse and their padding operations cost $O(Tp\,d^2(1+\ell^\tau))$.",
              r"their padding operations cost"),
    ],
    page="crt-address-map",
    frm=["controlled-shifts", "chunk-swap", "cyclic-convolution", "multiplication-as-convolution", "modular-arithmetic-and-residue-classes", "divisibility-primes-and-gcd"],
)

ct = show(
    "S3.6",
    r"The isomorphism $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ multiplies coefficient $k$ by $\zeta^k$ and turns cyclic convolution of length $r$ into convolution in $\mathcal R_r$; the negative wrap cancels the factor $\zeta^r$, so complex cyclic convolution $f*g/T$ is $D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)$.",
    "Twist coefficients by powers of $\\zeta$, so the cyclic wrap of the last coordinate becomes the negacyclic wrap, apply the ring convolution, and untwist.",
    M("The power-of-two complex convolution of the chirp identity is obtained from the synthetic convolution by a coefficient twist.", "explicit",
      r"The power-of-two complex convolution used in the chirp identity is"),
    [
        infer("S3.6.1", r"The map is well defined since $(\zeta y)^r=(-1)(-1)=1$.",
              r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."),
        infer("S3.6.2", r"It is diagonal in the monomial bases, multiplying coefficient $k$ by the nonzero number $\zeta^k$, hence an isomorphism.",
              r"multiplying coefficient $k$ by the nonzero number $\zeta^k$."),
        infer("S3.6.3", r"A wrapped term has factor $\zeta^{k+l}(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
              r"Untwisting therefore recovers the cyclic coefficient with the correct"),
        infer("S3.6.4", r"With $\mathcal M_r$ the normalized ring convolution, $\mathcal M_{\mathbb C}(f,g)=f*g/T$ is a bilinear contraction.",
              r"Consequently, with $\mathcal M_r$ from"),
        infer("S3.6.5", r"Generating the twist factors anew costs $O(Tp^{1+\delta})$ in total.",
              r"twist cost $O(Tp^{1+\delta})$."),
    ],
    page="coefficient-twist",
    frm=["polynomial-ring-negacyclic", "synthetic-convolution", "cyclic-convolution", "roots-of-unity", "complex-numbers"],
)

cht = show(
    "S3.7",
    r"The padded power-of-two transform $QF_{\boldsymbol t}$ is computed by a chirp phase product, a complex cyclic convolution obtained through the coefficient twist and the synthetic convolution, and a final chirp product, with error below $8TL\,2^{-p}$.",
    "Evaluate Bluestein's identity with approximated chirp phases, using the twisted synthetic convolution for the middle step.",
    M("The factor $QF_{\\boldsymbol t}$ can be computed from a cyclic convolution and two pointwise phase multiplications.", "explicit",
      r"computed from a cyclic convolution and two pointwise phase"),
    [
        infer("S3.7.1", r"The chirp array is computed from phase numerators modulo $2r$ with the established multiplier at total cost $O(Tdp^{1+\delta})$.",
              r"Let $\widetilde a$ be the resulting disk-grid array, so"),
        infer("S3.7.2", r"The computed transform forms $x_0=Q_p(\overline{\widetilde a}\cdot x)$, convolves with $\widetilde a$, and multiplies by $\overline{\widetilde a}$ again.",
              r"Thus $\widetilde a$ is the convolution kernel and $x_0$ is the data"),
        infer("S3.7.3", r"The exact result is $QF_{\boldsymbol t}x$ and the computed chirp transform differs from it by less than $8TL\,2^{-p}$.",
              r"Equation~\eqref{eq:permuted-chirp} identifies the exact result, so",
              deferred=True),
    ],
    page="chirp-transform",
    frm=["bluestein-chirp", "coefficient-twist", "synthetic-convolution", "disk-grid-truncation", "contraction-error-budget", "established-multiplier"],
)

srct = show(
    "S3.8",
    r"The computed source transform expands axes by $\mathcal A$, applies the chirp transform on the power-of-two axes, compresses with $\mathcal B_0$ and scales by $2^\gamma$; its exact counterpart is $RF_{\boldsymbol s}$, and the opposite-sign version is obtained by conjugation.",
    "Compose the linewise Gaussian maps with the chirp transform and an exact power-of-two scaling, then compare with the exact resampling identity.",
    M("The resampling identity expresses the source transform as these four factors, so applying them in sequence computes it.", "recoverable"),
    [
        infer("S3.8.1", r"Apply the linewise approximation to $\mathcal A$, the computed chirp transform, the linewise approximation to $\mathcal B_0$ and multiply the numerators by $2^\gamma$.",
              r"$\widetilde{\mathscr F}$ for the following procedure: apply the linewise"),
        infer("S3.8.2", r"The exact counterpart replaces each numerical subroutine by the exact map it approximates, giving $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.",
              r"Here an exact counterpart replaces every numerical subroutine by the"),
        infer("S3.8.3", r"The opposite-sign procedure is $\widetilde{\mathscr F}^{+}(z)=\overline{\widetilde{\mathscr F}(\overline z)}$ with exact counterpart $RF_{\boldsymbol s}^{+}$.",
              r"Define the opposite-sign procedure by"),
    ],
    page="source-transform",
    frm=["gaussian-resampling", "tensor-resampling", "chirp-transform", "source-permutation-cancel", "fixed-point-arithmetic", "established-multiplier"],
)

s3 = show(
    "S3",
    r"Integer multiplication reduces to normalized cyclic convolution on pairwise coprime prime axes: the digit list is placed there by the Chinese-remainder map, the two source transforms are computed through resampling and chirps, multiplied pointwise, and the opposite transform, rescaling, rounding and carries give the product.",
    "Pass from the integer product to the radix-digit convolution to a convolution on prime axes, replace each prime-length transform by a power-of-two one, and use the ring convolution for the middle transform.",
    M("The transform lengths needed for the integer product are pairwise coprime while the synthetic transforms use powers of two, and Gaussian resampling connects the two shapes.", "explicit",
      r"whereas the synthetic transforms use powers of two. Gaussian resampling"),
    [
        s31, pc, pl, digit, crt, ct, cht, srct,
        infer("S3.9", r"Read each operand backward in groups of $b$ bits to obtain radix-$2^b$ digits $a_j$, written as exact grid values $a_j2^{-b-2}$, and append $S-q$ zero records.",
              r"its least significant end in groups of $b$ bits."),
        infer("S3.10", r"Apply the coefficient-address map $\Phi$ to obtain source arrays $u,v$.",
              r"Apply the coefficient-address map $\Phi$, with its padded layout, to obtain"),
        infer("S3.11", r"Compute the two source transforms $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.",
              r"Compute $\widetilde{\mathscr F}(u)$ and"),
        infer("S3.12", r"Multiply corresponding complex coefficients exactly and truncate to $p$ fractional bits, giving the array $z$.",
              r"Multiply corresponding complex coefficients exactly and truncate"),
        infer("S3.13", r"Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its numerators exactly by $S$.",
              r"Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid"),
        infer("S3.14", r"Multiply by $2^{2b+4}S$, round the real values to the nearest integers, and undo $\Phi$ to restore the ordinary coefficient order.",
              r"Multiply the grid numerators of $\widetilde w$ exactly by"),
        infer("S3.15", r"Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits.",
              r"Propagate radix-$2^b$ carries in increasing coefficient order."),
        infer("S3.16", r"The two occurrences of $S$ undo different normalizations: after the first scale the array is $(u*v)/S$, and the second scale gives $2^{2b+4}(u*v)$.",
              r"The two occurrences of $S$ in this algorithm undo different"),
    ],
    page="multiplication-algorithm",
    frm=["multiplication-as-convolution", "cyclic-convolution", "crt-address-map", "source-transform", "source-permutation-cancel"],
)

# ---------------------------------------------------------------- S4 exact recovery
s4 = show(
    "S4",
    r"The scaled computed convolution has error below $1/2$, so rounding each real part gives the true integer coefficients, and radix carries propagated least significant first produce the exact $2n$-bit product.",
    "Track the norm and error of every computed array, using that contractions do not amplify errors and that a bilinear contraction adds the two operand errors, then rescale and compare with $1/2$.",
    M("A linear contraction propagates an input error without increasing it, so errors of composed steps only add.", "explicit",
      r"A linear contraction propagates an input error without increasing it."),
    [
        infer("S4.1", r"Each synthetic transform has error below $\sqrt2\,\ell\,2^{-p}<L2^{-p}$ with $L=\log_2T$.",
              r"Lemma~\ref{lem:synthetic-transform-cost} therefore applies to every"),
        infer("S4.2", r"If one operand has norm at most $.7$, the ring convolution stays below $.7$ and its computed output has norm below $.701$.",
              r"If one operand has norm at most $.7$, bilinear contraction gives"),
        infer("S4.3", r"The computed complex convolution differs from the exact one by less than $6TL\,2^{-p}$.",
              r"To compare it with $\mathcal M_{\mathbb C}(f,g)$, insert the exact"),
        infer("S4.4", r"The chirp transform differs from $QF_{\boldsymbol t}x$ by less than $8TL\,2^{-p}$.",
              r"For its error, the exact operands $a$ and $\overline a\cdot x$ are in"),
        infer("S4.5", r"A source transform of norm at most $.5$ has error below $E_s2^{-p}$ with $E_s=9\cdot2^\gamma TL$.",
              r"Finally let the input to a source transform have norm at most $.5$."),
        infer("S4.6", r"The pointwise product $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has norm below $.5$ and error below $(2E_s+2)2^{-p}$.",
              r"To estimate its error, write"),
        infer("S4.7", r"By the cancellation lemma $G(U\cdot V_1)=(u*v)/S^2$ for $G=RF^+_{\boldsymbol s}$, and the computed opposite transform has error below $(3E_s+2)2^{-p}$.",
              r"Lemma~\ref{lem:chirp-permutation}, applied to"),
        infer("S4.8", r"The first scaling by $S$ gives $\widetilde w$ approximating $w=(u*v)/S$ with error below $E_w2^{-p}$, $E_w<28\cdot2^\gamma T^2L$.",
              r"The first exact numerator multiplication by $S$ gives"),
        infer("S4.9", r"After the second scaling the absolute error is below $448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<1/2$.",
              r"Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than"),
        infer("S4.10", r"The true coefficients are integers, so the strict error bound below $1/2$ makes the nearest integer the unique correct coefficient.",
              r"The true coefficients are real integers."),
        infer("S4.11", r"After $\Phi^{-1}$ the carry scan proceeds from least to most significant, with carries below $Q_0^2$.",
              r"After $\Phi^{-1}$ the coefficients occur in increasing ordinary index,"),
        infer("S4.12", r"The exact product is less than $2^{2n}$, so removing zero padding bits leaves exactly $2n$ output bits.",
              r"than $2^{2n}$; all bits above position $2n-1$ are therefore zero."),
    ],
    page="exact-recovery",
    frm=["contraction-error-budget", "disk-grid-truncation", "triangle-inequality-and-error-bounds", "real-and-imaginary-parts-rounding-and-truncation", "source-transform", "chirp-transform"],
    salient="The working precision $p=6b$ is far more than the $3b$ bits a coefficient needs: after rescaling by $2^{2b+4}S$ the error is only about $448b\\,2^{-3b/4}$, which is what lets the $2^\\gamma$ resampling loss and the accumulated transform errors be absorbed.",
)

# ---------------------------------------------------------------- S5 cost
s5 = show(
    "S5",
    r"Dividing all costs by $Tp=\Theta(n)$ gives a table of seven dominant terms whose powers of $p$ are all at most $1-2\kappa$ with $\kappa=2^{-182}$, so the total is $O(n(\lg n)^{1-\kappa})$, with schoolbook multiplication below a cutoff.",
    "Tabulate the normalized cost of every operation as a power of $p$, bound each power by one minus the margin $g_i$, and absorb any fixed power of $\\log p$ into the slack.",
    M("The smallest margin below one is $2\\kappa$, so the explicit slack covers any remaining fixed power of $\\log p$.", "explicit",
      r"This explicit slack will cover"),
    [
        infer("S5.1", r"For the cost calculation put $V=Tp=\Theta(n)$; a full padded array has $\Theta(V)$ stored bits.",
              r"For the cost calculation put $V=Tp=\Theta(n)$."),
        infer("S5.2", r"The seven dominant margins are $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$.",
              r"Direct substitution gives"),
        infer("S5.3", r"Thus $\min_ig_i=2^{-181}=2\kappa$.",
              r"Thus $\min_i g_i=2^{-181}=2\kappa$."),
        infer("S5.4", r"The first three rows of the table are the terms of the synthetic transform cost, with $O(p/K)$ chunk exchanges each costing $O(VK^\tau)$.",
              r"The first three rows are the terms in"),
        infer("S5.5", r"The at most $\ell$ simultaneous rounds cost $O(Vd^{\lambda'})$ each.",
              r"For the at most $\ell$ simultaneous rounds,"),
        infer("S5.6", r"Axis exposure and restoration need $O(d^2)$ adjacent axis moves, each $O(V(1+\ell^\tau))$.",
              r"Axis exposure and restoration require $O(d^2)$ adjacent axis moves."),
        infer("S5.7", r"The Gaussian line maps cost $O(dTp^{3/2+\delta}\alpha)$ in total.",
              r"For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines."),
        infer("S5.8", r"Chirps, twists and scalar products cost $O(dp^{1+\delta})$ per entry, and the four integer products per record cost $O(Tp\log(rp))$ in total.",
              r"Chirp numerators have $O(p)$ bits and can be computed modulo $2r$ as"),
        infer("S5.9", r"Setup at recursion nodes costs at most $p^{A+C}=o(Tp)$ and setup per record or per line is negligible since $r$ exceeds every fixed power of $p$.",
              r"We next separate setup at recursion nodes from work repeated for every"),
        infer("S5.10", r"The compact exceptional stream of a packed change of basis costs $O(Vp^{A'}2^{-K})=o(V)$ to sort.",
              r"For one packed change of basis, let $V_{\rm call}$ be its current"),
        infer("S5.11", r"Each of the seven displayed powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually, giving $O(n(\log n)^{1-\kappa})$.",
              r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
        infer("S5.12", r"Using schoolbook multiplication below one fixed cutoff, a single fixed-alphabet fixed-tape deterministic machine runs in $O(n(\lg n)^{1-\kappa})$ for every input length.",
              r"Fix one cutoff beyond all the size, precision, margin and layout"),
    ],
    page="cost-analysis",
    frm=["parameter-choice", "established-multiplier", "chunk-swap", "simultaneous-layer", "transform-layout", "tensor-resampling", "crt-address-map", "gaussian-resampling", "chirp-transform", "asymptotic-notation-beyond-big-o", "logarithms-exponentials-floors-and-ceilings", "sorting-and-radix-sort"],
    salient="The exponent $\\kappa=2^{-182}$ is half the smallest margin below one, $g_2=\\epsilon c(1-\\tau)=2^{-75}\\cdot2^{-56}\\cdot2^{-50}$, so its tininess is the product of the three tiny exponents $\\epsilon$, $c$ and $1-\\tau$ chosen for the layer and chunk-exchange rows.",
)

root = show(
    "S0",
    r"A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.",
    "Build two fast tape primitives (address-chunk interchange and simultaneous butterfly layers), use them to compute exact convolution over the polynomial ring, plug that into the Gaussian-resampling and chirp reduction of integer multiplication, then verify exact recovery and the cost.",
    M("Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both data movement and arithmetic must be sped up.", "explicit",
      r"Scanning an array of $\Theta(n)$ stored bits at each of"),
    [s1, s2, s3, s4, s5],
    page="main-theorem",
    frm=["multitape-model", "nlogn-conjecture", "big-o", "turing-tapes", "polynomials", "complex-numbers"],
)

out = {"root": root}

# ----------------------------------------------------------------- checks
def walk(n, depth=0):
    yield n, depth
    for c in n.get("children", []) or []:
        yield from walk(c, depth + 1)

ok = True
pos = 0
ids = set()
for n, dpt in walk(root):
    if n["id"] in ids:
        print("DUP id", n["id"]); ok = False
    ids.add(n["id"])
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        cnt = SRC.count(q)
        if cnt == 0:
            print("MISSING", n["id"], q); ok = False
            continue
        if cnt > 1:
            print("MULTI(%d)" % cnt, n["id"], q)
        if n.get("deferred"):
            continue
        i = SRC.find(q, pos)
        if i < 0:
            first = SRC.find(q)
            print("ORDER", n["id"], "at", SRC[:first].count("\n") + 1, "prev pos line", SRC[:pos].count("\n") + 1, q); ok = False
        else:
            pos = i + len(q)
    else:
        mo = n["motivation"]
        if mo["source"] == "explicit":
            q = mo["quote"]["quote"]
            if SRC.count(q) == 0:
                print("MISSING motivation", n["id"], q); ok = False
        else:
            assert mo["quote"] is None

# pages
pages = {}
for n, dpt in walk(root):
    if n.get("page"):
        if n["page"] in pages:
            print("PAGE twice", n["page"], pages[n["page"]], n["id"]); ok = False
        pages[n["page"]] = n["id"]
print(len(pages), "pages used")

# adds check
def math_of(s):
    return re.findall(r"\$(.*?)\$", s)
for n, dpt in walk(root):
    for a in n.get("adds", []) or []:
        sym = a["symbol"]
        found = False
        for c, _ in walk(n):
            if c is n: continue
            for m in math_of(c["claim"]):
                if re.search(re.escape(sym) + r"(?![A-Za-z])", m) or sym in m:
                    found = True
        if not found:
            print("ADD not found", n["id"], sym); ok = False

json.dump(out, open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e4/V4/exegenius/tasks/0064-argument.answer.json', 'w'), indent=1)
print("ok" if ok else "PROBLEMS")
