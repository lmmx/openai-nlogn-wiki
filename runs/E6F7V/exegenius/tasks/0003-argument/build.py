import json, sys
BASE = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F7V"
SRC = open(BASE + "/sources/paper.tex").read()

def ev(q):
    return {"source": "paper", "quote": q}

def infer(id, claim, quote, frm=None, page=None, deferred=False, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote)}
    if frm: n["from"] = frm
    if page: n["page"] = page
    if deferred: n["deferred"] = True
    if salient: n["salient"] = salient
    return n

def show(id, claim, method, mot_text, mot_src, children, mot_quote=None, frm=None, page=None, salient=None, adds=None):
    m = {"text": mot_text, "source": mot_src}
    if mot_quote: m["quote"] = ev(mot_quote)
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": m, "children": children}
    if frm: n["from"] = frm
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n

def b(symbol, name, meaning, relation):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

# ---------------------------------------------------------------- Section 3 networks
R1 = show("S1.1.1",
  "A fixed linear network on two data banks $X,Y$ and scratch wires maps $(X,Y)$ to $(-Y,X)$ in three stages and returns every scratch wire to its arbitrary initial value.",
  "Schedule eight rows of pointwise gates (subtract, copy, gather, scatter, side injection, then undo) so that one invocation changes $y_S$ to $y_S+x_S$ whatever the scratch contents are, then compose three invocations (forward, inverse, forward).",
  "Because the scratch wires start with arbitrary values, the schedule first subtracts their effect and finally restores them, as in transparent computation; this is what lets the network later be run on rows of data that are not zero-initialised.",
  "explicit",
  [
   infer("S1.1.1.1", "Whatever the initial scratch values, one invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.", "Thus both net maps are $y\\gets y+x$."),
   infer("S1.1.1.2", "Forward at stage 1, inverse at stage 2 and forward at stage 3 send $(x,y)$ to $(-y,x)$ and restore every scratch wire.", "$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$."),
  ],
  mot_quote="This cancellation of arbitrary initial scratch values is a linear",
  page="xor-linear-network",
  frm=["binary-representation-and-bitwise-operations","modular-arithmetic","matrices-and-linear-maps","linear-algebra-prelims"])

R2 = show("S1.1.2",
  "Giving every source, gate and sink an invertible frame $D_v$ and applying $D_vD_u^{-1}$ along each edge makes the network implement $D_{\\rm out}\\mathsf S D_{\\rm in}^{-1}$, so only the endpoint frames matter.",
  "Maintain the invariant that the array stored at a vertex is its frame applied to the logical array, and check that it survives sources, edges and pointwise linear gates.",
  "A pointwise linear gate commutes with a frame shared by all its wires, so the intermediate frames cancel along any route; this leaves them free to be chosen so that every edge change is cheap.",
  "recoverable",
  [
   infer("S1.1.2.1", "A common frame commutes with the pointwise linear gate, so the invariant continues through every gate to the sinks.", "Thus the common frame commutes with the pointwise gate, and"),
   infer("S1.1.2.2", "Once the scalar routing is fixed, the endpoint frames alone determine the array operator on each route, including routes of scratch roles.", "the endpoint frames determine the array operator on each route"),
  ],
  page="frames",
  frm=["linear-algebra-prelims","matrices-and-linear-maps","permutations","xor-linear-network"],
  salient="Every intermediate frame cancels: the operator applied to a route depends only on the frame at its source and the frame at its sink, even for the auxiliary scratch roles, so the intermediate frames are free parameters to be tuned for cheap edges.")

R3 = show("S1.1.3",
  "Nested nondegenerate subspaces of a tensor cube, built from indicator vectors of three-element subsets of $[100]$, can be attached to all gates and terminals so that every edge joins comparable labels and the only decreasing edges are the central-wire edges from time 3 to time 4.",
  "Use lines $\\langle t_T\\rangle$ whose inner products are intersection counts, so neighbouring triple lines are orthogonal; tensor them one factor per stage and tabulate the orthogonal residual of every edge.",
  "Orthogonality of neighbouring triple indicators makes the label of a side wire nest inside the label of the next gate, which keeps every edge non-decreasing except one return of the central wires.",
  "explicit",
  [
   infer("S1.1.3.1", "Over the label field, $\\langle t_S,t_T\\rangle=|S\\cap T|-1$, so every triple line is nondegenerate and neighbouring triple lines are orthogonal.", "\\langle t_S,t_T\\rangle=|S\\cap T|-1,"),
   infer("S1.1.3.2", "Every edge of the network joins comparable nondegenerate labels, with orthogonal residual of known dimension.", "Every edge joins comparable nondegenerate labels."),
   infer("S1.1.3.3", "Label dimension never decreases along an edge except on the central-wire edges from time 3 to time 4, each of which loses $h=100$ dimensions.", "Label dimension is nondecreasing along every edge except center $3\\to4$, which removes"),
  ],
  mot_quote="Orthogonality of the corresponding indicator vectors permits",
  page="subset-labels",
  frm=["linear-algebra-prelims","sets-functions-cartesian-products-and-bijections","xor-linear-network","binary-representation-and-bitwise-operations"])

R4 = show("S1.1.4",
  "The sum of the absolute changes of label dimension over all edges is $Wm-2N+2L$, and the loss $L$ on decreasing edges is below $N/2$.",
  "Telescope the signed dimension changes at each gate (source dimensions sum to $N$, sink dimensions to $Wm-N$), then add twice the total loss on decreasing edges; evaluate $L$ from the number of central wires.",
  "Signed changes cancel at every gate, so the only way the absolute total can exceed $Wm-2N$ is through decreasing edges; the construction was arranged to have very few of them.",
  "explicit",
  [
   infer("S1.1.4.1", "The signed change of label dimension over all edges telescopes to $Wm-2N$.", "The signed increase is therefore $Wm-2N$."),
   infer("S1.1.4.2", "There are $Ic$ decreasing edges, each of loss $h$, so $L=Ich$ and replacing signed by absolute changes adds $2L$.", "There are $Ic$ decreasing edges, each of loss $h$; replacing signed"),
   infer("S1.1.4.3", "The loss ratios are exactly $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$.", "\\frac{L_{\\rm b}}{N}=\\frac{100}{539},\\qquad"),
   infer("S1.1.4.4", "Both loss ratios $L/N$ are below $1/2$, so after the $N$ extra source ranks the total edge rank is $s=Wm-N+2L<Wm$ in the bit network.", "In particular, both are smaller than $1/2$."),
  ],
  mot_quote="dimension $L$, the sum of absolute changes is $Wm-2N+2L$.")

R = show("S1.1",
  "In each of the two networks, with $W$ wires and an $m$-dimensional label space, the nested labels make the total rank $s$ of all edge differences (the number of smaller calls) strictly less than $Wm$, because the loss $L$ on decreasing edges is below $N/2$.",
  "Label every gate and terminal by a nested nondegenerate subspace so that an edge changes the stored array by one smaller operation per unit of residual dimension; build the exchanging network, the frames and the labels, then count the total dimension change.",
  "A frame change along an edge costs one smaller call per dimension of its orthogonal residual, so s is a sum of dimension changes; the whole saving reduces to the signed sum $Wm-2N$ and the small loss on decreasing edges.",
  "explicit",
  [R1, R2, R3, R4],
  mot_quote="The saving will come from keeping the total dimension lost on decreasing",
  page="rank-deficit",
  frm=["linear-algebra-prelims","matrices-and-linear-maps","xor-linear-network","subset-labels","frames"],
  salient="The deficit is minute (a relative deficit of about $10^{-11}$) but strictly positive: all decreasing edges are the single return of the central wires from time 3 to time 4, which loses only $h=100$ dimensions per invocation, so $L/N$ is $100/539$ or $101/539$, below $1/2$, and that is exactly enough to leave $s<Wm$ after the $N$ extra source ranks.",
  adds=[b("W","wire count","the number of wires of the network, including scratch wires","count"),
        b("m","label dimension","the dimension of the label space, the number of fields in each address chunk","count"),
        b("N","source dimension total","the sum of the dimensions of all source labels","count"),
        b("L","decreasing-edge loss","the total dimension lost on edges whose label dimension decreases","count"),
        b("s","total edge rank","the sum of the ranks of all edge differences, i.e. the number of smaller calls","count")])

B1 = show("S1.2",
  "With the permutation frame $\\Phi_M$ (moving the entry at $(H,D)$ to $(H+MD,D)$) the bit network implements the shear $(H,D)\\mapsto(H+D,D)$ on every role, and its total edge rank is $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$.",
  "Take the vertex matrix to be the rational projection onto the vertex label (with $-P_{U_a}$ at the sources $X_a$), so that an edge difference has rank equal to its residual dimension except at the $N$ source edges, and check the endpoint matrices differ by the identity.",
  "Projections onto nested nondegenerate labels differ by projections onto the residual, so ranks equal dimension changes; the negative source projection makes the endpoint difference exactly the identity, which is what a shear needs.",
  "recoverable",
  [
   infer("S1.2.1", "For nested nondegenerate labels $U\\subset V$ the projection difference $P_V-P_U$ has rank $\\dim V-\\dim U$, and reversing the edge does not change it.", "Its rank is $\\dim V-\\dim U$; reversing the"),
   infer("S1.2.2", "The only exceptions to rank equal to dimension change are the $N$ source edges, which cost one extra rank each.", "The only exceptions are the $N$ negative source projections."),
   infer("S1.2.3", "The deficit of the total rank from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$.", "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$."),
   infer("S1.2.4", "The endpoint matrix difference is the identity $I_m$ on every input role, so the same shear $H\\gets H+D$ appears on every role.", "$P_{U_a^\\perp}-(-P_{U_a})=I_m$."),
  ],
  page="bit-shear-interface",
  frm=["frames","rank-deficit","subset-labels","xor-linear-network","linear-algebra-prelims","permutations","modular-arithmetic"])

C1 = show("S1.3",
  "Over Gaussian dyadic values with binary labels and phase frames $\\mathcal C_U$, each edge change is a product of two-point kernels $aI+bX_v$, and telescoping gives $C^{\\otimes m}$ on every role with $s_{\\rm c}<W_{\\rm c}m$ kernel factors.",
  "Replace the rational projections by binary labels and phase operators $H^{\\otimes m}\\operatorname{diag}(i^{\\operatorname{wt}(P_Ux)})H^{\\otimes m}$; weight additivity over an orthonormal residual basis turns each edge change into one kernel per basis vector.",
  "In characteristic two the weight of a sum of orthogonal vectors is additive modulo four, so the phase difference across an edge splits over an orthonormal basis of the residual, one kernel per vector, which is the same count as the rank in the bit network.",
  "recoverable",
  [
   infer("S1.3.1", "Each edge phase-frame difference is a product of one translation kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal basis of the edge residual.", "becomes $aI+bX_v$ or its inverse.  The nonzero residuals have such"),
   infer("S1.3.2", "The number of kernel factors is $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}$, with deficit $2N-2L_{\\rm c}>0$ from $W_{\\rm c}m$.", "The deficit is $2N-2L_{\\rm c}>0$."),
   infer("S1.3.3", "After source and sink diagonal corrections, the operator on every role (also the pair $X_a\\to Y_a$ and the scratch roles) is $C^{\\otimes mk}$ on $k$ columns.", "on this pair is therefore $C^{\\otimes mk}$ as well."),
  ],
  page="phase-frame-network",
  frm=["butterfly","frames","rank-deficit","subset-labels","xor-linear-network","linear-algebra-prelims","complex-numbers","binary-representation-and-bitwise-operations"])

P = show("S1.4",
  "Since $s_{\\rm b}/W_{\\rm b}<m^\\tau$ and $s_{\\rm c}/W_{\\rm c}<m^\\sigma$ for the fixed rational exponent $\\tau=\\sigma=1-2^{-50}$, a recursion that spends $s$ calls on streams of volume $V/W$ per factor $m$ of parameter has normalized cost $F_k=O(e^\\tau)$ at parameter $e=m^k$.",
  "Bound the relative rank deficits explicitly, choose a fixed rational exponent just below one that still exceeds the growth factor $s/W$, and solve the recurrence by a geometric sum.",
  "Any positive deficit gives some exponent below one, but an explicit exponent is needed to state a concrete $\\kappa$; comparing $m^{1-2^{-50}}$ with $m(1-\\eta)$ does this with integer comparisons only.",
  "recoverable",
  [
   infer("S1.4.1", "The relative rank deficits are $\\eta_{\\rm b}=(W_{\\rm b}m-s_{\\rm b})/(W_{\\rm b}m)$ and $\\eta_{\\rm c}$, tiny but positive rational numbers.", "\\eta_{\\rm b}=\\frac{W_{\\rm b}m-s_{\\rm b}}{W_{\\rm b}m}"),
   infer("S1.4.2", "Both deficits exceed $20\\cdot2^{-50}$, and $m^{1-2^{-50}}>m(1-20\\cdot2^{-50})>m(1-\\eta)$ because $\\log m<20$.", "Both exact deficits displayed above are greater than $20\\cdot2^{-50}$."),
   infer("S1.4.3", "Consequently $s_{\\rm b}/W_{\\rm b}<m^\\tau$ and $s_{\\rm c}/W_{\\rm c}<m^\\sigma$ with $0<\\tau=\\sigma<1$.", "\\frac{s_{\\rm b}}{W_{\\rm b}}<m^\\tau,"),
   infer("S1.4.4", "One level makes $s$ calls on volume $V/W$ each, so the normalized cost satisfies $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.", "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).", deferred=True),
   infer("S1.4.5", "For $a=s/W<m^\\tau$ the geometric sum of the recurrence gives $F_k=O(e^\\tau)$ with $e=m^k$.", "Hence $F_k=O(e^\\tau)$.", deferred=True),
  ],
  page="power-saving-recurrence",
  frm=["recursion-and-divide-and-conquer-recurrences","summation-geometric-series-and-products","logarithms-exponentials-floor-and-ceiling","rank-deficit"],
  salient="A relative deficit of only about $10^{-11}$ is enough for a genuine power saving: a recursion whose growth factor $s/W$ is merely slightly below $m$ has cost $O(e^\\tau)$ with $\\tau=1-2^{-50}<1$, so each of the two procedures beats a linear pass per level by a power of its width.")

# ---------------------------------------------------------------- Section 4 interchange
LT = infer("S2.1",
  "Every rational matrix of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones.",
  "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
  page="lower-triangular-factorization",
  frm=["matrices-and-linear-maps","linear-algebra-prelims"])

MS = show("S2.2",
  "For a rational matrix $A$ of rank $a$, the shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ is performed with exactly $a$ interchanges of $b$-digit fields and $O(V)$ other work.",
  "Factor $A=E_1\\Pi E_2$, apply the triangular factors as controlled shifts in descending physical order, and turn each one in $\\Pi$ into three updates around a single field interchange.",
  "A lower triangular change of coordinates updates each field from earlier fields only, which is exactly the direction in which a controlled shift is linear time on tape; so everything except the pivots is linear, and the pivots are the only recursive calls.",
  "explicit",
  [
   infer("S2.2.1", "A lower triangular transformation of $H$, or of $D$, costs $O(V)$ by controlled shifts in descending physical order.", "A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
   infer("S2.2.2", "Each one in $\\Pi$ is realised by $D_j\\leftarrow D_j+H_i$, an interchange of $H_i$ and $D_j$, and $D_j\\leftarrow H_i-D_j$, giving $H_i\\leftarrow H_i+D_j$.", "D_j\\leftarrow D_j+H_i,\\qquad"),
   infer("S2.2.3", "The sequence uses just one interchange per one of $\\Pi$, so the number of recursive calls is the rational rank $a$.", "It uses just one interchange.  There are $a$ ones, which proves the"),
  ],
  mot_quote="earlier fields in linear time.  Lower triangular changes of coordinates",
  page="matrix-shear-cost",
  frm=["lower-triangular-factorization","controlled-shifts","stream-operations","modular-arithmetic","bit-shear-interface"])

PW = show("S2.3",
  "For $e=m^k$ digits, two address chunks of $e$ digits are interchanged in $O(Ve^\\tau)$ time, provided a preceding row field has length divisible by $W^k$.",
  "Split rows into $W$ role streams, run the bit network whose edges $\\Phi_{A_e}$ are shears done by smaller interchanges (Lemma on matrix shears), undo the role permutation to obtain $H\\leftarrow H+D$ on all roles, finish with $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$, and schedule the recursion depth-first on fixed tapes.",
  "The bit network turns an interchange of width $e$ into $s$ interchanges of width $e/m$ on streams $1/W$ as large, which is the recurrence $F_k\\le(s/W)F_{k-1}+O(1)$; the only thing to check besides the frames is that the recursion fits on a fixed number of tapes.",
  "recoverable",
  [
   infer("S2.3.1", "Split whole rows cyclically into $W$ role streams, each of volume $V/W$ with the same remaining shape.", "Split whole rows cyclically into $W$ role streams within each prefix"),
   infer("S2.3.2", "Applying $\\Phi_{A_e}$ on every edge and the gates pointwise yields $H\\leftarrow H+D$ on every original row, including rows assigned to scratch roles.", "is $H\\leftarrow H+D$ on every original row, including rows assigned"),
   infer("S2.3.3", "The interchange follows from the shear by the three updates $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$, only the middle one using the circuit.", "D\\leftarrow D-H,\\qquad H\\leftarrow H+D,\\qquad D\\leftarrow H-D,"),
   infer("S2.3.4", "The number of recursive calls is the sum of the edge ranks, exactly $s$, each on a stream of volume $V/W$.", "The number of recursive calls is the sum of the edge ranks, exactly $s$."),
   infer("S2.3.5", "Parking the inactive role streams on a stack makes each push, pop and copy cost $O(V)$ at a parent node, so scheduling the $s$ calls on fixed tapes adds only $O(V)$.", "Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
  ],
  page="power-width-interchange",
  frm=["stream-operations","bit-shear-interface","matrix-shear-cost","frames","power-saving-recurrence","fixed-tape-model","tapes-scanning-and-sorting-as-basic-machine-procedures"],
  salient="The interchange is an exact permutation of the data, yet it is computed through XOR combinations of role streams, and it comes out right for arbitrary initial contents of the scratch roles because the transparent-computation schedule restores them.")

I = show("S2",
  "Two disjoint contiguous address fields of $u$ bits (any width, any gaps, even one-bit payload) in an array of volume $V$ are interchanged in $O(Vu^\\tau)$ time for a fixed $\\tau=1-2^{-50}<1$; the intermediate steps are XOR combinations although the result is an exact permutation.",
  "Interchange fields of power width $m^k$ recursively by the bit network with shears as edges, then reduce arbitrary widths to power widths by peeling off high digits to make rows, padding the row count, and splitting the width in base $m$.",
  "Each edge of rank $a$ costs $a$ smaller interchanges, and the sum of the ranks is less than the number of wires times $m$, so the recurrence saves a power of the width.",
  "explicit",
  [LT, MS, PW,
   infer("S2.4", "Peel off the top $\\rho$ digits of each chunk to serve as a row field of range at least $W^k$, padding the row count to a multiple of $W^k$ at most doubling the volume.", "Write each chunk as its top $\\rho$ digits followed by its remaining"),
   infer("S2.5", "Write the remaining width in base $m$ and apply the power-width interchange to $a_j$ corresponding pieces of width $m^j$.", "Write the remaining width in base $m$:"),
   infer("S2.6", "The pieces cost $O(V)\\sum_ja_jm^{j\\tau}=O(Ve^\\tau)$ in total, a geometric sum.", "O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau)."),
   infer("S2.7", "Binary widths are padded to the least $e$ with $q^e\\ge2^u$, at a fixed factor in volume, so the bound is $O(Vu^\\tau)$.", "Finally, for binary chunks let $e$ be the least integer with"),
  ],
  mot_quote="An edge matrix of rank $a$ will require $a$ smaller interchanges.",
  page="arbitrary-width-interchange",
  frm=["power-width-interchange","stream-operations","power-saving-recurrence","logarithms-exponentials-floor-and-ceiling"],
  salient="Although the final effect is an exact permutation, the procedure forms pointwise XOR combinations of data on the way, and the exponent $\\tau<1$ does not depend on the width, the gaps between the fields or the payload size.")

# ---------------------------------------------------------------- Section 5 butterfly layers
PK = show("S3.3",
  "A binary row addition $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$ on the selected bit of $f$ address chunks at once, with a third chunk of arbitrary contents restored, costs $O(V(L^\\tau+1))$ for the parameter family used.",
  "Simulate the XORs by eight whole-chunk cyclic shifts that equal the intended parity flips whenever no segment carries, then deterministically repair the explicitly bounded set $\\mathcal B$ of addresses where a guard value fails, by sorting.",
  "Adding $2^{j_i}$ to a chunk flips the selected bit without touching the other bits as long as the neighbouring $K$-bit segment does not carry; a guard margin makes carries rare, and the few exceptional addresses can be extracted and sorted cheaply.",
  "recoverable",
  [
   infer("S3.3.1", "The eight shifts leave the third integer $w$ unchanged and flip the parity of $u$ exactly when the control is one.", "Here $u\\bmod2\\in\\{0,1\\}$, also for negative $u$. Thus the parity of $u$"),
   infer("S3.3.2", "The addresses where a guard value fails form a set $\\mathcal B$ with $|\\mathcal B|\\le\\delta_{\\rm bad}M$ and $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$.", "|\\mathcal B|\\le\\delta_{\\rm bad}M."),
   infer("S3.3.3", "There are at most sixteen swaps and eight rotations, so the movement costs $O(V(L^\\tau+1))$ by the chunk-swap and controlled-shift bounds.", "There are at most sixteen swaps and eight rotations in $S_0$."),
   infer("S3.3.4", "The exceptional records are extracted, sorted by destination rank and reinserted in one forward scan, which implements the ideal map everywhere.", "marked holes. One forward full-stream scan reinserts the sorted records."),
  ],
  page="packed-selected-bit-addition",
  frm=["arbitrary-width-interchange","controlled-shifts","stream-operations","binary-representation-and-bitwise-operations","tapes-scanning-and-sorting-as-basic-machine-procedures"],
  salient="A constant number (eight) of whole-chunk shifts performs the XOR on all $f$ selected positions together, regardless of how many there are, and the repaired set has fraction at most $80(f-1)2^{-K}$ because $K/\\log p\\to\\infty$.")

BL3 = show("S3.4",
  "Sending rows to the $W$ roles gives each of the $s$ children $1/W$ of the volume, and the recurrence $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ unrolls to a layer cost $O(Vd^{\\lambda'})$ with $\\lambda'<1$.",
  "Charge each node its binary changes of basis, split rows into role streams so each child has volume $V/W$, stop the recursion at $e<d^{\\beta}$ and sum the internal and leaf costs over base-$m$ pieces.",
  "The power saving of the interchange survives only if the extra work at each node, the changes of basis, is itself a smaller power of the number of axes; the choice $K=\\lfloor d^c\\rfloor$ small makes that so.",
  "reconstructed",
  [
   infer("S3.4.1", "The binary changes of basis, scalar gates and endpoint corrections cost $O(V((eK)^\\tau+1))$ at a node with $e$ active chunks.", "O\\bigl(V((eK)^\\tau+1)\\bigr)"),
   infer("S3.4.2", "Each recursive edge call acts on one role stream of exactly $1/W$ of the parent's logical volume.", "Each recursive edge call acts on"),
   infer("S3.4.3", "Dividing by the current volume, the normalized cost satisfies $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$.", "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),"),
   infer("S3.4.4", "With $a=s/W<m^\\lambda$ the internal costs sum to at most $Ce^\\lambda\\sum_j(a/m^\\lambda)^j=O(e^\\lambda)$.", "C e^\\lambda\\sum_{j\\ge0}(a/m^\\lambda)^j=O(e^\\lambda)."),
   infer("S3.4.5", "Adding the base-$m$ pieces and the row preprocessing gives $O(d^{\\lambda'})$ for any fixed $\\lambda'$ above $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}$.", "=O(d^{\\lambda'})"),
  ])

BL4 = show("S3.5",
  "All intermediate values of the layer are exact Gaussian dyadics of width $O(p)$, because the arithmetic dependency depth is at most $C_0d^{C_1}=o(p)$.",
  "Bound the depth of the chains of additions, halvings and multiplications by $i$ through the recursion, then convert depth into denominator and magnitude growth.",
  "Each addition at most doubles the modulus and each halving adds one denominator bit, so the growth is bounded by the depth; with $\\epsilon C_1<1$ this is $o(p)$ and no rounding is needed inside a layer.",
  "recoverable",
  [
   infer("S3.5.1", "The dependency depth satisfies $A(e)\\le sA(e/m)+E$ at an internal node, so it is polynomial in $d$.", "A(e)\\le sA(e/m)+E"),
   infer("S3.5.2", "Choosing $\\epsilon C_1<1$ makes the guard width $\\Delta=o(p)$ and the full coefficient width $O(p)$.", "Choose \\(\\epsilon C_1<1\\)."),
  ])

BL = show("S3",
  "A butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied simultaneously at the same bit position of $D\\le d$ address chunks of every polynomial record, followed by one truncation, costs $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$ with error below $\\sqrt2\\,2^{-p}$.",
  "Write $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$, evaluate $C^{\\otimes D}$ by the complex phase network recursively (children on $e/m$ axes, binary bases changed by packed selected-bit additions), evaluate everything exactly in Gaussian dyadics and truncate once.",
  "Separate butterflies on $D$ axes would need $D$ whole-array passes; the phase network does the same layer with a power-saving recursion.",
  "explicit",
  [
   infer("S3.1", "Summing the residual dimensions of the network gives exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot.", "$s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
   infer("S3.2", "The normalized butterfly layer is $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$ with $\\mathcal S_D$ a diagonal phase and $b^D$ a binary shift with a fourth-root phase.", "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D."),
   PK, BL3, BL4,
   infer("S3.6", "Together the row construction and the recurrence analysis give total time $O(Vd^{\\lambda'})$ on fixed tapes, including padding, repair and cleanup.", "above give total time $O(Vd^{\\lambda'})$ on fixed tapes, including"),
   infer("S3.7", "Every row of $\\mathcal H$ has absolute row sum one, so the layer maps disk arrays to disk arrays and one truncation $Q_p$ adds an error below $\\sqrt2\\,2^{-p}$.", "absolute row sum one. Thus $\\mathcal H$ maps disk arrays to disk"),
  ],
  mot_quote="$\\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly",
  page="simultaneous-butterfly-layer",
  frm=["butterfly","phase-frame-network","packed-selected-bit-addition","arbitrary-width-interchange","power-saving-recurrence","fixed-point-disk","negacyclic-ring","stream-operations","controlled-shifts","triangle-inequality-and-norms"],
  salient="The cost exponent $\\lambda'$ is strictly below one for the whole layer: one layer on $D$ axes costs $d^{\\lambda'}$ passes instead of $D$ passes, because the same rank-saving recursion that speeds up address interchange also applies to the numerical butterflies.")

A = show("S1",
  "Two tape procedures cost less than a pass per level: interchanging two disjoint $u$-bit address fields of a volume-$V$ array costs $O(Vu^\\tau)$ and a simultaneous butterfly layer on $D\\le d$ chunks costs $O(Vd^{\\lambda'})$, for fixed $\\tau,\\lambda'<1$.",
  "Give each procedure its own fixed linear network that exchanges two banks of values and restores all scratch values, with total number $s$ of smaller calls below $Wm$, then run the network recursively on role streams of volume $V/W$ (interchange of address fields first, numerical layers second).",
  "A call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$, so the normalized cost grows by $s/W<m$ per level, which is a power of the parameter below one.",
  "explicit",
  [R, B1, C1, P, I, BL],
  mot_quote="is the source of the power saving.",
  frm=["fixed-tape-model","stream-operations","controlled-shifts","recursion-and-divide-and-conquer-recurrences"])

# ---------------------------------------------------------------- Section 6-7 synthetic convolution
ST = show("S4.1",
  "On $\\mathcal R_r^t$ with roots $\\omega_t=y^{2r/t}$ the transforms $F_t^\\mp$ are contractions with $F_t^+F_t^-=t^{-1}I$ despite zero divisors, and $F_t^-$ is computed by decimation-in-frequency rounds of butterflies $H_0$ and monomial twiddles.",
  "Show contraction because every power of $\\omega_t$ is an isometry, prove character cancellation directly by a pairing argument instead of dividing, and derive the radix-two decimation-in-frequency recursion.",
  "The ring $\\mathbb C[y]/(y^r+1)$ has zero divisors, so $\\omega^j-1$ need not be invertible and the usual division proof of orthogonality fails; a direct pairing argument replaces it.",
  "explicit",
  [
   infer("S4.1.1", "Every power of $\\omega_t$ is an isometry and each entry averages $t$ such images, so both transforms are contractions.", "Every power of $\\omega_t$ is an isometry, and each transform entry is"),
   infer("S4.1.2", "Shifting $k$ by $t/2^{v+1}$ multiplies the character sum by $y^{rj_0}=-1$, hence the sum vanishes unless $t\\mid j$, giving $F_t^+F_t^-=t^{-1}I$.", "Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes"),
   infer("S4.1.3", "Pairing $z_k$ with $z_{k+t/2}$ gives the decimation-in-frequency identity for $(F_t^-z)_{2h+b}$, so one round is a butterfly followed by a twiddle $\\omega_t^{-k}$.", "(F_t^-z)_{2h+b}"),
  ],
  mot_quote="The ring has zero divisors, so we verify character cancellation",
  page="synthetic-transform",
  frm=["negacyclic-ring","dft","butterfly","multidimensional-dft","roots-of-unity","triangle-inequality-and-norms"])

RF = show("S4.2",
  "The recursion writes frequencies in bit-reversed slots, the forward transform being $B_tF_t^-$, and the opposite procedure consumes that order as $F_t^+B_t^{-1}$, so no sort is executed.",
  "Write each level's output directly in its slot, then run the levels in reverse for the opposite transform, using $H_0^2=I/2$ for the reversed level.",
  "Because the forward recursion places branch bits into the slots it has just freed, the frequency index comes out bit reversed; reading the same recursion backwards undoes that order for free.",
  "recoverable",
  [
   infer("S4.2.1", "The recursion writes its outputs directly in bit-reversed order and does not move whole frequency indices.", "directly in this order; it does not move whole frequency indices."),
   infer("S4.2.2", "The opposite procedure traverses the recursion in reverse: smaller branches first, then the inverse monomial, then $H_0$.", "The procedure consuming this stored order traverses the recursion in"),
   infer("S4.2.3", "The two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.", "B_tF_t^-,\\qquad F_t^+B_t^{-1},"),
  ],
  page="retained-frequency-order",
  frm=["synthetic-transform","permutations"])

TL = show("S4.3",
  "A layout permutation $L$ places the selected bits of all axes at a common offset in consecutive $K$-bit chunks, so every round is one simultaneous layer; the forward and opposite transforms cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error below $\\sqrt2\\,\\ell\\,2^{-p}$.",
  "Group the rounds of all axes into parallel butterflies followed by one monomial, build $L$ from prefix moves and chunk exchanges, apply the simultaneous layer to each of at most $\\ell$ rounds, and count one truncation per round.",
  "The simultaneous layer needs its selected bits at the same offset of consecutive chunks, so the layout must move them there, and the cost of those moves must itself be a power saving.",
  "explicit",
  [
   infer("S4.3.1", "Each completed round is a parallel butterfly followed by a monomial multiplication, hence a contraction.", "$J_E$ is an isometry, so every completed round is a contraction."),
   infer("S4.3.2", "The prefix-slot moves and individual butterfly rounds cost $O(TpdK)$.", "listed slots, so the moves cost $O(TpdK)$."),
   infer("S4.3.3", "The chunk exchanges that define $L$ cost $O(Tp\\,pK^{\\tau-1})$ by the equal-width interchange bound.", "=O\\bigl(Tp\\,pK^{\\tau-1}\\bigr)."),
   infer("S4.3.4", "The simultaneous layers cost $O(Tp\\ell d^{\\lambda'})$ in total over the rounds.", "per round and $O(Tp\\ell d^{\\lambda'})$ in total."),
   infer("S4.3.5", "At most $\\ell$ rounds, each adding a single truncation, give error below $\\sqrt2\\,\\ell\\,2^{-p}$ and disk output.", "give the claimed error and disk bounds.  The layout permutations"),
  ],
  mot_quote="we must place the selected bits of the participating axes at a common",
  page="transform-layout",
  frm=["simultaneous-butterfly-layer","arbitrary-width-interchange","retained-frequency-order","synthetic-transform","multidimensional-dft","fixed-point-disk","stream-operations"])

SP = show("S4.4",
  "Signed Kronecker packing evaluates polynomial records at $2^{4p}$, multiplies the resulting integers with the established multiplier, extracts the coefficients, wraps negacyclically and truncates, giving the ring product $Q_p(fg/r)$ in $O(rp\\log(rp))$.",
  "Pack the real and imaginary integer parts as signed evaluation integers at $B_0=2^{4p}$, form four integer products, recover coefficients by centered residues and carries, and reduce modulo $y^r+1$.",
  "The established $O(N\\log N)$ multiplier is an ordinary integer multiplier, so polynomial products reduce to it once the coefficient fields are wide enough that neighbouring fields cannot interfere.",
  "recoverable",
  [
   infer("S4.4.1", "Setting $B_0=2^{4p}$, each polynomial becomes the signed integer $A_u=u(B_0)$ of $4pr$ bits.", "Set $B_0=2^{4p}$"),
   infer("S4.4.2", "Every product coefficient satisfies $|h_j|\\le r2^{2p}<B_0/2$, so coefficients are identified by centered residues.", "|h_j|\\leq r2^{2p}<2^{3p}<B_0/2."),
   infer("S4.4.3", "Centered extraction with a carry in $\\{0,1\\}$ returns each $h_j$ exactly in $O(rp)$ time.", "Thus $\\widehat h_j=h_j$.  Subtracting this coefficient and dividing"),
   infer("S4.4.4", "Subtracting coefficient $j+r$ from coefficient $j$ reduces modulo $y^r+1$, and each result is a sum of $r$ signed products.", "coefficient at $j+r$ from the one at $j$ for $0\\leq j<r$, treating"),
   infer("S4.4.5", "Four exact integer products dominate, giving total time $O(rp\\log(rp))$.", "Four exact integer products dominate the linear"),
  ],
  page="signed-packing-product",
  frm=["negacyclic-ring","fixed-point-disk","established-multiplier","polynomials","binary-representation-and-bitwise-operations","complex-numbers"])

SC = show("S4",
  "The normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ on disk-grid arrays is approximated with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
  "Compute two forward synthetic transforms in retained layout order, multiply pointwise in the ring and divide by $r$ by signed packing, apply the opposite transform to that order, and scale exactly by $M$.",
  "The pointwise product commutes with the record permutation, so the permutation never has to be undone between the forward and the opposite transform.",
  "explicit",
  [ST, RF, TL, SP,
   infer("S4.5", "The convolution theorem gives $F_{\\boldsymbol t}^-(f*g)=M(F_{\\boldsymbol t}^-f)(F_{\\boldsymbol t}^-g)$, and with $F^+F^-=I/M$ the scaled pipeline equals $(f*g)/(rM)$.", "=M(F_{\\boldsymbol t}^-f)(F_{\\boldsymbol t}^-g)."),
   infer("S4.6", "The error is $M(3\\delta+\\eta)=\\sqrt2\\,M(3\\ell+1)2^{-p}$: two forward errors, the product truncation and the opposite transform add.", "$M(3\\delta+\\eta)=\\sqrt2\\,M(3\\ell+1)2^{-p}$, as claimed."),
   infer("S4.7", "There are $M=T/r$ pointwise products costing $O(Tp\\log(rp))$ in total, and the three transforms cost as in the layout lemma.", "There are $M=T/r$ pointwise polynomial products.  Their total cost"),
  ],
  mot_quote="Pointwise multiplication commutes with applying the same record",
  page="synthetic-convolution",
  frm=["cyclic-convolution","error-accounting","signed-packing-product","transform-layout","retained-frequency-order","synthetic-transform","multidimensional-dft"],
  salient="No frequency sort is ever executed: the forward outputs stay in bit-reversed layout order through the pointwise product and the opposite transform consumes exactly that order.")

# ---------------------------------------------------------------- Section 8 resampling
GR = show("S5.1",
  "For coprime $s<t$ there are linear contractions $A$ and $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, computable with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$, and the two sorting permutations $P_s,P_t$ stay inside the identity.",
  "Use the Gaussian identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$, invert the near-identity $N=C\\mathsf T\\mathsf D$ by a Neumann series, and normalise so that $A$ and $B_0$ are contractions.",
  "The Fourier transform of length $s$ coprime to $t$ is not directly available on powers of two; a Gaussian smoothing identity lets a transform of length $t$ stand in for it, up to a near-identity correction that a Neumann series inverts.",
  "recoverable",
  [
   infer("S5.1.1", "The Gaussian identity and inverse estimate give $\\|N-I\\|<2.01e^{-\\pi\\alpha^2\\theta/2}<2^{-\\alpha^2\\theta}$.", "\\|N-I\\|<2.01e^{-\\pi\\alpha^2\\theta/2}<2^{-\\alpha^2\\theta}."),
   infer("S5.1.2", "Since $\\|N-I\\|<1/2$, $N$ is invertible by the Neumann series.", "by the Neumann series. Put"),
   infer("S5.1.3", "With the stated normalisations $A=\\mathsf S'$ and $B_0=\\mathsf D'\\mathsf J'C$ are contractions satisfying $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$.", "which is \\eqref{eq:no-sort-one-dimensional}."),
   infer("S5.1.4", "Combining the quoted ordered algorithms for $\\mathsf S'$, $\\mathsf J'$, $\\mathsf D'$ and the coordinate selection $C$, the costs add to the claimed bound.", "The costs add to the claimed bound."),
  ],
  page="gaussian-resampling",
  frm=["dft","error-accounting","fixed-point-disk","established-multiplier","primes-coprimality-and-gcd","complex-numbers","summation-geometric-series-and-products","triangle-inequality-and-norms","rational-numbers-and-rounding"])

TR = show("S5.2",
  "In $d$ dimensions the one-dimensional maps are applied line by line on a zero-padded box of $T=\\prod_it_i$ entries, giving $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ at cost $O(dTp^{3/2+\\delta}\\alpha)$ plus $O(Tpd^2(1+\\ell^\\tau))$ for movement.",
  "Tensor the one-dimensional identity, expand the axes one at a time (and compress them one at a time) by exposing each axis as the innermost field with address-chunk interchanges, and count the lines.",
  "Keeping the array in the full padded box keeps its size fixed so that only the line contents change; exposing one axis at a time needs only $O(d^2)$ adjacent field interchanges.",
  "recoverable",
  [
   infer("S5.2.1", "The tensor identity is $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$.", "=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A,"),
   infer("S5.2.2", "Tensoring the one-dimensional identity proves it, and expansion then compression of axes gives contractions with error below $dp^2$.", "Tensoring \\eqref{eq:no-sort-one-dimensional} proves"),
   infer("S5.2.3", "Axis $i$ has at most $T/t_i$ lines, so the line machines cost $O(dTp^{3/2+\\delta}\\alpha)$.", "=O(dTp^{3/2+\\delta}\\alpha)."),
   infer("S5.2.4", "Exposing and restoring one axis needs $O(d)$ adjacent interchanges, hence all axes need $O(d^2)$, each of cost $O(Tp(1+\\ell^\\tau))$.", "$O(d)$ adjacent interchanges, hence all axes need $O(d^2)$."),
  ],
  page="padded-box-tensor-resampling",
  frm=["gaussian-resampling","multidimensional-dft","arbitrary-width-interchange","stream-operations","error-accounting"])

BC = infer("S5.3",
  "The middle transform together with its target permutation is a chirp multiplication, a cyclic convolution with a chirp array and another chirp multiplication: $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$.",
  "This is precisely the coefficient in $QF_{\\boldsymbol t}$, because",
  page="bluestein-chirp",
  frm=["dft","cyclic-convolution","multidimensional-dft","complex-numbers"])

PC = show("S5.4",
  "The source permutation $R$ left in the resampling identity cancels across two forward transforms, a pointwise product and the opposite-sign transform: $RF_{\\boldsymbol s}^+[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
  "Show that $R$ is its own conjugate on $F^+$, so $RF^+R=F^+$, use that a permutation commutes with pointwise products, and apply the convolution theorem with its two normalizations.",
  "A coordinate dilation by a unit moves a Fourier index to its inverse multiple, so one copy of $R$ on each side of $F^+$ cancels; the pointwise product commutes with $R$, so the permutation is absorbed instead of executed.",
  "recoverable",
  [
   infer("S5.4.1", "Because $t_i$ is a unit modulo $s_i$, $F_{\\boldsymbol s}^+R=R^{-1}F_{\\boldsymbol s}^+$, hence $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$.", "$F_{\\boldsymbol s}^+R=R^{-1}F_{\\boldsymbol s}^+$ and hence"),
   infer("S5.4.2", "Using $F_{\\boldsymbol s}(u*v)=S(F_{\\boldsymbol s}u)\\cdot(F_{\\boldsymbol s}v)$ and $F^+F=I/S$ the two normalizations give $(u*v)/S^2$.", "F_{\\boldsymbol s}^+F_{\\boldsymbol s}=I/S$. The two normalizations give"),
  ],
  page="permutation-cancellation",
  frm=["gaussian-resampling","bluestein-chirp","dft","cyclic-convolution","permutations","primes-coprimality-and-gcd","modular-arithmetic"])

C = show("S5",
  "Fourier transforms of the pairwise coprime lengths $s_i$ are expressed through power-of-two transforms, $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, with the permutations $R,Q$ kept inside the identity, the middle $QF_{\\boldsymbol t}$ a chirp convolution, and $R$ cancelling between forward and opposite transforms.",
  "Apply Gaussian resampling with both permutations retained, tensor it line by line on a padded box, write the middle transform by Bluestein's chirp identity, and show that the source permutation cancels.",
  "The usual implementation of Gaussian resampling sorts twice per coordinate, which would cost a full $O(tp\\log t)$ per line; retaining the permutations in the identity removes those sorts.",
  "explicit",
  [GR, TR, BC, PC],
  mot_quote="We retain both permutations in the transform formula and",
  salient="No sort is executed: both the source and the target permutations stay inside the transform formula, and the source permutation $R$ vanishes by cancellation.")

# ---------------------------------------------------------------- Section 9 assembly
D1 = show("S6.1",
  "The parameters $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, a padded-box size $T\\in[4n/b,8n/b)$, a record length $r=2^\\ell$, axis lengths $t_i\\in\\{r/2,r\\}$ and distinct primes $s_i$ just below $t_i$ satisfy every hypothesis of the transform and resampling interfaces, with $\\epsilon=2^{-75}$, $c=2^{-56}$.",
  "Choose all quantities as fixed rational powers of $b$, find the primes by deterministic search in two disjoint intervals, and verify the hypotheses (size, prime counting, separation $\\alpha^4\\theta_i>p$) interface by interface.",
  "The prime lengths must be close to the powers of two so that the product $S$ fills a fixed fraction of the padded box $T$, while each ratio $t_i/s_i$ stays large enough for resampling.",
  "explicit",
  [
   infer("S6.1.1", "The fixed rational constants include $\\epsilon=2^{-75}$ and $\\kappa=2^{-182}$, with $c=2^{-56}$ and $\\lambda'=1-2^{-54}$.", "C_1=20,\\qquad \\epsilon=2^{-75},\\qquad \\kappa=2^{-182}."),
   infer("S6.1.2", "For large $n$ put $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$ and $K=\\lfloor d^c\\rfloor$.", "b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,"),
   infer("S6.1.3", "Take a power of two $T\\in[4n/b,8n/b)$ and $r=2^{\\lceil(\\log_2T)/d\\rceil}$, with axis lengths $r/2$ or $r$ and product $T$.", "Take the power of two $T$ in $[4n/b,8n/b)$, and let"),
   infer("S6.1.4", "These give $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$ and $r=2^{\\Theta(p^{1-\\epsilon})}$.", "Tp=\\Theta(n),\\quad d=\\Theta(p^\\epsilon),\\quad"),
   infer("S6.1.5", "Each of the two intervals just below $t_i$ contains more than $d$ primes, so distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ exist.", "We may therefore choose distinct odd primes satisfying"),
   infer("S6.1.6", "Multiplying the lower bounds gives $T/2<S<T$ for $S=\\prod_is_i$.", "Together with $s_i<t_i$, this gives $T/2<S<T$."),
   infer("S6.1.7", "With $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$ every hypothesis of the one-dimensional resampling lemma holds for large $n$.", "Thus every hypothesis of Lemma~\\ref{lem:no-sort-resampling} holds for"),
   infer("S6.1.8", "The deterministic prime search takes $n^{o(1)}=o(n)$ time.", "Since $p=6\\lceil\\log_2 n\\rceil=\\Theta(\\log n)$, the search takes"),
  ],
  mot_quote="The distinct prime lengths $s_i$ must be close to the powers of two",
  page="prime-axis-parameters",
  frm=["radix-digit-convolution","crt-map","gaussian-resampling","primes-coprimality-and-gcd","logarithms-exponentials-floor-and-ceiling","summation-geometric-series-and-products"],
  adds=[b("b","digit width","the number of bits of each radix digit, $\\lceil\\log_2 n\\rceil$","count"),
        b("p","working precision","the number of fractional bits kept in every complex coefficient, $6b$","count"),
        b("d","axis count","the number of cyclic axes of the padded box","count"),
        b("K","chunk width","the number of address bits in one chunk, $\\lfloor d^{c}\\rfloor$","count"),
        b("T","padded box size","the number of entries of the padded box, a power of two near $n/b$","count"),
        b("r","record length","the number of complex coefficients in a polynomial record, a power of two","count")],
  salient="Every exponent is tiny ($\\epsilon=2^{-75}$ for the number of axes, $c=2^{-56}$ for the chunk width), so $d$ and $K$ grow like extremely small powers of $\\log n$ yet still tend to infinity, while $r$ grows faster than any fixed power of $p$.")

D2 = show("S6.2",
  "Splitting each $n$-bit input into $q=\\lceil n/b\\rceil$ radix-$2^b$ digits turns the product into a convolution of digit polynomials of degree below $S$, padded so that no cyclic wraparound occurs, and carry propagation yields the $2n$-bit product.",
  "Write both inputs as polynomials in $2^b$, bound the degree of their product by the cyclic length $S$, bound every coefficient by $2^{3b}$, and propagate carries from the least significant end.",
  "A polynomial product evaluated at $2^b$ is the integer product, so it suffices to know the coefficient convolution exactly; padding to length $S$ makes the cyclic convolution agree with the ordinary one.",
  "recoverable",
  [
   infer("S6.2.1", "The product has degree at most $2q-2<2n/b\\le T/2<S$, so cyclic convolution modulo $x^S-1$ has no wraparound.", "2q-2<2n/b\\le T/2<S."),
   infer("S6.2.2", "Every product coefficient satisfies $0\\le c_j\\le q(2^b-1)^2<2^{3b}$.", "0\\le c_j\\le q(2^b-1)^2<2^{3b},"),
   infer("S6.2.3", "The carries obey $0\\le k_j\\le q(Q_0-1)<Q_0^2$ with $Q_0=2^b$, so a left-to-right scan produces the radix digits of the product.", "The carries satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$.", deferred=True),
  ],
  page="radix-digit-convolution",
  frm=["cyclic-convolution","schoolbook-integer-arithmetic","polynomials","binary-representation-and-bitwise-operations","summation-geometric-series-and-products"])

D3 = show("S6.3",
  "For pairwise coprime lengths $s_i$ with product $S$, the algebra isomorphism $\\Phi:x\\mapsto\\prod_ix_i^{\\mu_i}$ turns one cyclic convolution of length $S$ into a multidimensional cyclic convolution on prime axes, and on tape it is a sequence of prefix-controlled cyclic shifts.",
  "Choose exponents $\\mu_i=P_i^{-1}\\bmod s_i$ so that the coordinate of each monomial is triangular in the mixed-radix digits, then implement the triangular update axis by axis as controlled shifts and reorder axes by address-chunk interchanges.",
  "A triangular coordinate map means each target axis is updated from lower-index axes that precede it on tape, which is exactly the direction in which a controlled shift is linear time; a generic Chinese-remainder map would need a sort.",
  "recoverable",
  [
   infer("S6.3.1", "The map is an isomorphism, since the image of $x$ has order $S$ and runs through all target monomials, so it preserves cyclic convolution.", "is an isomorphism and preserves cyclic convolution."),
   infer("S6.3.2", "The coordinate in axis $i$ of $\\Phi(x^k)$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}$.", "b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}."),
   infer("S6.3.3", "Each step preserves the valid box and its complement, so zero padding remains zero after every step.", "zero padding remains zero after every step."),
   infer("S6.3.4", "Each triangular update is a prefix-controlled cyclic shift, since its controls precede its target in the current physical order.", "Each triangular update is a prefix-controlled cyclic shift."),
   infer("S6.3.5", "Together with the $O(d^2)$ axis moves, the map $\\Phi$, its inverse and the padding operations cost $O(Tpd^2(1+\\ell^\\tau))$.", "Therefore the map $\\Phi$, its inverse, and"),
  ],
  page="crt-map",
  frm=["cyclic-convolution","multidimensional-dft","controlled-shifts","arbitrary-width-interchange","modular-arithmetic","primes-coprimality-and-gcd","radix-digit-convolution"])

D4 = show("S6.4",
  "Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ maps $\\mathbb C[x]/(x^r-1)$ isomorphically onto $\\mathcal R_r$, turning the last cyclic axis into a polynomial ring, so complex cyclic convolution is $\\mathcal M_{\\mathbb C}=D_-\\iota^{-1}\\mathcal M_r(\\iota D_+\\cdot,\\iota D_+\\cdot)$.",
  "Define $x_d\\mapsto\\zeta y$, check it is well defined and diagonal in the coefficient bases, and verify that the negative wrap of $y^r+1$ gives the cyclic wrap after untwisting.",
  "The synthetic transforms need a ring in which powers of $y$ are roots of unity, and $y^r=-1$ supplies them only for the negacyclic ring; the twist moves the cyclic convolution into that ring and back.",
  "recoverable",
  [
   infer("S6.4.1", "The map $x_d\\mapsto\\zeta y$ is well defined since $(\\zeta y)^r=(-1)(-1)=1$, diagonal and invertible, and preserves the sup norm.", "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$."),
   infer("S6.4.2", "For $k+l=j+hr$ the twisted negacyclic product term has factor $\\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.", "\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j."),
   infer("S6.4.3", "The normalized complex convolution $\\mathcal M_{\\mathbb C}=(f*g)/T$ follows, with $\\mathcal M_r$ convolving the first $d-1$ axes over the ring.", "Here $\\mathcal M_r$ convolves the first $d-1$ axes over $\\mathcal R$,"),
  ],
  page="phase-twist",
  frm=["negacyclic-ring","cyclic-convolution","synthetic-convolution","roots-of-unity","complex-numbers"])

D5 = show("S6.5",
  "The source transform $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ is computed by Gaussian expansion on each line, a chirp transform (a twisted synthetic convolution) and Gaussian compression, followed by a power-of-two scaling, with tracked disk margins and errors.",
  "Compose the linewise approximation of $\\mathcal A$, the computed chirp transform $\\widetilde{\\mathscr C}$ built on the twisted convolution, the linewise approximation of $\\mathcal B_0$ and an exact shift by $\\gamma$ bits.",
  "Bluestein's identity expresses the middle factor through one convolution, and the convolution is exactly what the twist and the synthetic transforms compute, so the three earlier ingredients compose.",
  "recoverable",
  [
   infer("S6.5.1", "The computed chirp transform forms $x_0=Q_p(\\overline{\\widetilde a}\\cdot x)$, then $y_0=\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,x_0)$, then $Q_p(\\overline{\\widetilde a}\\cdot y_0)$.", "x_0&=Q_p(\\overline{\\widetilde a}\\mathbin{\\cdot}x),\\\\"),
   infer("S6.5.2", "Replacing the approximations by exact phases and exact convolution gives $QF_{\\boldsymbol t}x$ by the chirp identity.", "(a,\\overline a\\mathbin{\\cdot}x)=QF_{\\boldsymbol t}x$ by"),
   infer("S6.5.3", "For a source tensor of norm at most $.5$, the procedure applies $\\mathcal A$, the chirp transform, $\\mathcal B_0$ and multiplies the numerators by $2^\\gamma$; its exact counterpart is $RF_{\\boldsymbol s}$.", "For a source disk-grid tensor of norm at most $.5$, write"),
  ],
  page="source-transform",
  frm=["gaussian-resampling","padded-box-tensor-resampling","bluestein-chirp","phase-twist","synthetic-convolution","permutation-cancellation","error-accounting","fixed-point-disk"])

D6 = show("S6.6",
  "The multiplication algorithm reads radix digits, applies $\\Phi$, computes two source transforms, a truncated pointwise product, the opposite-sign transform, the rescalings by $S$ and $2^{2b+4}S$, rounds, applies $\\Phi^{-1}$ and propagates carries.",
  "Execute the six numbered steps of the algorithm, noting that the two occurrences of $S$ undo different normalizations.",
  "The exact counterpart of the three transforms is $(u*v)/S^2$, one factor $S$ undoes this, and the second scale together with $2^{2b+4}$ restores the integer coefficients from their normalised and downscaled digit encoding.",
  "recoverable",
  [
   infer("S6.6.1", "Apply the coefficient-address map $\\Phi$ with its padded layout to the digit streams to obtain source arrays $u,v$ of norm less than $1/4$.", "\\item Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain"),
   infer("S6.6.2", "Compute the source transforms $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$.", "\\item Compute $\\widetilde{\\mathscr F}(u)$ and"),
   infer("S6.6.3", "Multiply corresponding coefficients exactly and truncate to $p$ fractional bits to obtain $z$.", "\\item Multiply corresponding complex coefficients exactly and truncate"),
   infer("S6.6.4", "Compute the opposite-sign transform of $z$ and multiply the numerators exactly by $S$.", "\\item Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid"),
   infer("S6.6.5", "Multiply exactly by $2^{2b+4}S$, round to integers and apply $\\Phi^{-1}$ to restore the ordinary coefficient order.", "\\item Multiply the grid numerators of $\\widetilde w$ exactly by"),
   infer("S6.6.6", "Propagate radix-$2^b$ carries and output exactly $2n$ bits.", "\\item Propagate radix-$2^b$ carries in increasing coefficient order."),
   infer("S6.6.7", "The two occurrences of $S$ undo different normalizations: after the first scale the result is $w=(u*v)/S$.", "The two occurrences of $S$ in this algorithm undo different"),
  ])

ER = show("S6.7",
  "Each recovered convolution coefficient is within $448\\,b\\,2^{-b+\\gamma}<1/2$ of the true integer, which is below $2^{3b}$, so rounding and carries give the exact product.",
  "Propagate the disk margin and the error through each approximate step (contractions keep errors, bilinear steps add the operand errors), restore the scales, and compare the final error with $1/2$.",
  "Rounding returns the unique true integer exactly when the real value is within one half of it, so everything reduces to a bound on the accumulated error.",
  "explicit",
  [
   infer("S6.7.1", "For a bilinear contraction with all four operands in the disk, the two operand errors simply add.", "When all four operands are in the disk, their two errors therefore add."),
   infer("S6.7.2", "The ring convolution has error $E_{\\rm ring}=M(3L+2)<5TL$ in units of $2^{-p}$.", "E_{\\rm ring}:=M(3L+2)<5TL."),
   infer("S6.7.3", "The complex convolution has error below $6TLh_p$ after adding the two twist errors and the untwist.", "<(E_{\\rm ring}+4+4+4)h_p<6TLh_p."),
   infer("S6.7.4", "The chirp transform has error below $8TLh_p$.", "<(6TL+2+4+4)h_p<8TLh_p."),
   infer("S6.7.5", "The source transform has error below $E_sh_p$ with $E_s=9\\cdot2^\\gamma TL$ and norm below $.501$.", "E_s=9\\,2^\\gamma TL,"),
   infer("S6.7.6", "The pointwise product has $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$.", "Thus $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$."),
   infer("S6.7.7", "The opposite transform contributes at most $(3E_s+2)h_p$, using $G(U\\cdot V_1)=(u*v)/S^2$.", "&<(3E_s+2)h_p."),
   infer("S6.7.8", "After the first scale by $S$ the error is below $E_wh_p$ with $E_w:=S(3E_s+2)<28\\cdot2^\\gamma T^2L$.", "E_w:=S(3E_s+2)<28\\,2^\\gamma T^2L."),
   infer("S6.7.9", "After the second scale by $2^{2b+4}S$ and the division by $2^{6b}$, the final absolute error is below $448\\,b\\,2^{-b+\\gamma}\\le448\\,b\\,2^{-3b/4}<1/2$.", "<448b\\,2^{-b+\\gamma}"),
   infer("S6.7.10", "The strict error below $1/2$ makes the nearest integer the unique correct coefficient, which lies in $[0,2^{3b})$.", "The strict error below $1/2$ makes the nearest integer to"),
   infer("S6.7.11", "The carry recurrence $k_0=0$, $d_j=(c_j+k_j)\\bmod Q_0$, $k_{j+1}=\\lfloor(c_j+k_j)/Q_0\\rfloor$ gives the radix digits of the product.", "k_0=0,\\qquad d_j=(c_j+k_j)\\bmod Q_0,\\qquad"),
  ],
  mot_quote="The strict error below $1/2$ makes the nearest integer to",
  page="exact-recovery",
  frm=["error-accounting","source-transform","permutation-cancellation","radix-digit-convolution","prime-axis-parameters","fixed-point-disk","rational-numbers-and-rounding","binary-representation-and-bitwise-operations"],
  salient="The working precision $p=6b$ leaves $3b$ bits of slack beyond the $3b$-bit coefficients, so the accumulated error $448\\,b\\,2^{-b+\\gamma}$ stays far below one half even after the factors of $2^\\gamma$, $T^2$ and $S$.")

D = show("S6",
  "The algorithm (digits, address map $\\Phi$, two source transforms, truncated pointwise product, opposite-sign transform, rescaling by $S$ and $2^{2b+4}S$, rounding, inverse address map and carries) outputs the exact $2n$-bit product.",
  "Chain the reductions of the flow figure: radix-digit convolution, Chinese-remainder map to distinct prime axes, Gaussian resampling with chirps to power-of-two axes, phase twist to the polynomial ring; fix the parameters, run the six steps, and bound the final error by $1/2$.",
  "Each reduction changes the problem or its representation so that the next primitive applies; the order of the stages is forced by what each stage needs from the previous one.",
  "reconstructed",
  [D1, D2, D3, D4, D5, D6, ER],
  page="multiplication-algorithm",
  frm=["radix-digit-convolution","crt-map","prime-axis-parameters","phase-twist","source-transform","exact-recovery","signed-packing-product","synthetic-convolution"])

E = show("S7",
  "Dividing costs by $V=Tp=\\Theta(n)$, seven dominant terms are each at most $p^{1-2\\kappa}$, the smallest power margin is $2^{-181}=2\\kappa$, and so the total time is $O(n(\\lg n)^{1-\\kappa})$.",
  "Tabulate the normalized cost of each operation as a power of $p$, compute the seven margins below one from the fixed exponents, and let the smallest margin absorb every fixed power of $\\log p$ and the setup costs.",
  "Each procedure is a power saving of its own, so the total is a power saving only if every row of the cost table is a power of $p$ strictly below one with a common margin; the margin must exceed what is needed to absorb logarithmic factors.",
  "explicit",
  [
   infer("S7.1", "For the cost calculation $V=Tp=\\Theta(n)$ and every coefficient has $\\Theta(p)$ bits.", "For the cost calculation put $V=Tp=\\Theta(n)$."),
   infer("S7.2", "Prefix-slot moves and individual butterfly rounds cost $dK$ per unit volume, power $\\epsilon(1+c)$ of $p$.", "Prefix-slot moves and individual butterfly rounds & $dK$ & $\\epsilon(1+c)$"),
   infer("S7.3", "Chunk exchanges for the transform layout cost $pK^{\\tau-1}$, power $1-\\epsilon c(1-\\tau)$.", "Chunk exchanges for transform layout & $pK^{\\tau-1}$ & $1-\\epsilon c(1-\\tau)$"),
   infer("S7.4", "Simultaneous butterfly rounds cost $\\ell d^{\\lambda'}$, power $1-\\epsilon(1-\\lambda')$.", "Simultaneous butterfly rounds & $\\ell d^{\\lambda'}$ & $1-\\epsilon(1-\\lambda')$"),
   infer("S7.5", "CRT and axis layouts cost $d^2(1+\\ell^\\tau)$, power $\\tau+\\epsilon(2-\\tau)$.", "CRT and axis layouts & $d^2(1+\\ell^\\tau)$ & $\\tau+\\epsilon(2-\\tau)$"),
   infer("S7.6", "Gaussian line maps cost $dp^{1/2+\\delta}\\alpha$, power $3/4+\\delta+3\\epsilon/2$.", "Gaussian line maps & $dp^{1/2+\\delta}\\alpha$ & $3/4+\\delta+3\\epsilon/2$"),
   infer("S7.7", "Chirps, twists and scalar products cost $dp^\\delta$, power $\\epsilon+\\delta$.", "Chirps, twists and scalar products & $dp^\\delta$ & $\\epsilon+\\delta$"),
   infer("S7.8", "Packed polynomial products cost $\\log(rp)$, power $1-\\epsilon$.", "Packed polynomial products & $\\log(rp)$ & $1-\\epsilon$"),
   infer("S7.9", "Direct substitution gives margins $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$.", "g_1>\\frac12,\\quad g_2=2^{-181},\\quad g_3=2^{-129},\\quad"),
   infer("S7.10", "Thus $\\min_ig_i=2^{-181}=2\\kappa$, explicit slack that covers any remaining fixed power of $\\log p$.", "Thus $\\min_i g_i=2^{-181}=2\\kappa$."),
   infer("S7.11", "Setup, descriptor work and prime search cost $o(Tp)$, since $r$ exceeds every fixed power of $p$.", "costs at most $p^{A+C}=o(Tp)$."),
   infer("S7.12", "The exceptional-stream repair is a deterministic worst-case bound of $o(V)$.", "a deterministic worst-case bound."),
   infer("S7.13", "Each of the seven displayed powers is at most $1-2\\kappa$ and a fixed power of $\\log p$ is at most $p^\\kappa$, so the total is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.", "Each of the seven displayed powers is at most $1-2\\kappa$ by"),
  ],
  mot_quote="any remaining fixed power of $\\log p$.",
  page="cost-accounting",
  frm=["prime-axis-parameters","transform-layout","simultaneous-butterfly-layer","arbitrary-width-interchange","crt-map","padded-box-tensor-resampling","source-transform","signed-packing-product","established-multiplier"],
  salient="The margin is minuscule but positive: the smallest of the seven margins is $2^{-181}=2\\kappa$ (from the chunk-exchange term, where $K=\\lfloor d^c\\rfloor$ with $c=2^{-56}$ and $d\\approx p^{\\epsilon}$ with $\\epsilon=2^{-75}$), and half of it is spent absorbing logarithmic factors, leaving the exponent $1-\\kappa$ with $\\kappa=2^{-182}$.")

ROOT = show("S0",
  "One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$, refuting the $n\\log n$ optimality conjecture in this model.",
  "Build the two accelerated tape procedures (address interchange and simultaneous butterfly layers), use them inside synthetic transforms and Gaussian resampling to compute a convolution, assemble the multiplication algorithm with exact recovery, and total the cost.",
  "A transform-based product scans $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ levels and so costs $n\\log n$; a power saving needs cheaper movement and cheaper arithmetic, which the two procedures supply, and everything else is built around them.",
  "explicit",
  [A, SC, C, D, E],
  mot_quote="We therefore need savings in both movement and arithmetic.",
  page="main-theorem",
  frm=["nlogn-history","fixed-tape-model","established-multiplier","big-o","turing-machine","asymptotic-notation-beyond-big-o","logarithms-exponentials-floor-and-ceiling"],
  salient="The saving is a genuine power of the logarithm, $(\\lg n)^{1-\\kappa}$, but with the astronomically small $\\kappa=2^{-182}$ and enormous constants; the algorithm refutes the $n\\log n$ optimality conjecture without any claim of practicality.",
  adds=[b("n","input length","the number of bits of each of the two integers being multiplied","count"),
        b("\\kappa","saving exponent","the exponent $2^{-182}$ by which the logarithmic factor is reduced","direct")])

out = {"root": ROOT}

# ----- validation
pos = 0
bad = 0
def walk(n, acc):
    acc.append(n)
    for c in n.get("children", []):
        walk(c, acc)
allnodes = []
walk(ROOT, allnodes)
ids = [n["id"] for n in allnodes]
assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]
for n in allnodes:
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        c = SRC.count(q)
        if c == 0:
            print("MISSING", n["id"], repr(q)); bad += 1
        elif c > 1:
            print("MULTI", c, n["id"], repr(q[:60]))
    else:
        m = n["motivation"]
        if m.get("quote"):
            q = m["quote"]["quote"]
            if SRC.count(q) == 0:
                print("MISSING MOT", n["id"], repr(q)); bad += 1
# order
last = -1
for n in allnodes:
    if n["intention"] == "infer" and not n.get("deferred"):
        q = n["quote"]["quote"]
        i = SRC.find(q, last + 1)
        if i < 0:
            first = SRC.find(q)
            print("ORDER", n["id"], "prev", last, "first at", first, repr(q[:50])); bad += 1
        else:
            last = i
print("nodes", len(allnodes), "bad", bad)

import re as _re
PAGES = """nlogn-history fixed-tape-model established-multiplier stream-operations controlled-shifts linear-algebra-prelims xor-linear-network subset-labels frames rank-deficit power-saving-recurrence bit-shear-interface lower-triangular-factorization matrix-shear-cost power-width-interchange arbitrary-width-interchange packed-selected-bit-addition negacyclic-ring fixed-point-disk signed-packing-product error-accounting dft butterfly phase-frame-network simultaneous-butterfly-layer cyclic-convolution multidimensional-dft bluestein-chirp synthetic-transform retained-frequency-order transform-layout synthetic-convolution gaussian-resampling padded-box-tensor-resampling permutation-cancellation radix-digit-convolution crt-map prime-axis-parameters phase-twist source-transform exact-recovery multiplication-algorithm cost-accounting main-theorem""".split()
KNOWN = """big-o polynomials complex-numbers turing-machine asymptotic-notation-beyond-big-o logarithms-exponentials-floor-and-ceiling binary-representation-and-bitwise-operations schoolbook-integer-arithmetic modular-arithmetic primes-coprimality-and-gcd sets-functions-cartesian-products-and-bijections permutations matrices-and-linear-maps roots-of-unity summation-geometric-series-and-products recursion-and-divide-and-conquer-recurrences worst-case-running-time-and-subroutines triangle-inequality-and-norms rational-numbers-and-rounding newton-s-method tapes-scanning-and-sorting-as-basic-machine-procedures""".split()
idx = {p:i for i,p in enumerate(PAGES)}
used = {}
fromset = set()
def chk(n, anc):
    pg = n.get("page") or anc
    if n.get("page"):
        if n["page"] in used: print("PAGE DUP", n["page"], n["id"], used[n["page"]])
        used[n["page"]] = n["id"]
    for f in n.get("from", []):
        fromset.add(f)
        if f in KNOWN: continue
        if f not in idx: print("UNKNOWN FROM", n["id"], f); continue
        if idx[f] >= idx[pg]: print("FROM NOT BEFORE", n["id"], f, "page", pg)
    for a in n.get("adds", []):
        sym = a["symbol"]
        found = False
        def desc(m):
            global found
            for c in m.get("children", []):
                for mm in _re.findall(r"\$(.+?)\$", c["claim"]):
                    if sym in mm: return True
                if desc(c): return True
            return False
        if not desc(n): print("ADD NOT FOUND", n["id"], sym)
    for c in n.get("children", []):
        chk(c, pg)
chk(ROOT, None)
for p in PAGES:
    if p not in used and p not in fromset: print("PAGE UNUSED", p)
print("pages with steps", len(used))

json.dump(out, open(BASE + "/exegenius/tasks/0003-argument.answer.json", "w"), indent=1, ensure_ascii=False)
