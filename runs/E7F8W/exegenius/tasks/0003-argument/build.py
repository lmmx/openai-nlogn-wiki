import json, sys, re
PROJ = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F8W"
SRC = open(PROJ + "/sources/paper.tex").read()

def ev(q):
    return {"source": "paper", "quote": q}

def inf(id, claim, quote, frm=None, page=None, deferred=False, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": frm or []}
    if page: n["page"] = page
    if deferred: n["deferred"] = True
    if salient: n["salient"] = salient
    return n

def show(id, claim, method, mot_text, mot_src, children, mot_quote=None, frm=None, page=None, adds=None, salient=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": {"text": mot_text, "source": mot_src, "quote": ev(mot_quote) if mot_quote else None},
         "children": children, "from": frm or []}
    if page: n["page"] = page
    if adds: n["adds"] = adds
    if salient: n["salient"] = salient
    return n

def B(symbol, name, meaning, rel="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": rel}

# ---------------- S1 : address chunk interchange ----------------
S1_1 = inf("S1.1",
  r"A fixed linear network of copy, gather, scatter and side-injection gates, run forward, then backward, then forward, exchanges two banks of values (up to a sign) and returns every scratch wire to its arbitrary initial value.",
  r"For arbitrary initial values of its auxiliary wires, a forward",
  page="scratch-restoring-exchange",
  frm=["arithmetic-modulo-2-and-xor"],
  salient="The net effect on the data does not depend on the initial contents of the scratch wires: the first two schedule rows subtract the old scratch contribution, so the result holds for arbitrary scratch values.")

S1_2 = inf("S1.2",
  r"If each scalar wire is replaced by an array stored as $D_vg$ for an invertible operator $D_v$ (its frame), a pointwise linear gate commutes with its frame, so along a route only the endpoint operator $D_{\rm out}D_{\rm in}^{-1}$ remains.",
  r"Thus the common frame commutes with the pointwise gate, and",
  page="array-frames", frm=["scratch-restoring-exchange", "tape-address-model", "matrices-vectors-and-linear-maps"])

S1_3_1 = inf("S1.3.1",
  r"Indicator vectors $t_T$ of three-element subsets $T$ of $[h]$ satisfy $\langle t_S,t_T\rangle=|S\cap T|-1$, so each triple line is nondegenerate and neighbouring triple lines are orthogonal.",
  r"\langle t_S,t_T\rangle=|S\cap T|-1,")

S1_3_2 = show("S1.3.2",
  r"With the prescribed terminal labels, the sum of absolute dimension changes over all edges equals $Wm-2N+2L$, where $L$ is the total dimension lost on decreasing edges.",
  "Count dimension changes edge by edge: the signed changes telescope at every gate, and absolute values add twice the loss.",
  "Labels are nested along every edge, so the cost of an edge is its dimension change; only decreasing edges make the absolute sum exceed the signed (telescoped) sum.",
  "recoverable",
  [
   inf("S1.3.2.1",
     r"The only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$.",
     r"edges are the central-wire edges from time 3 to time 4; their dimension"),
   inf("S1.3.2.2",
     r"The signed sum of dimension changes telescopes at every gate, because each touched wire has one incoming and one outgoing incidence with the same gate label; with source dimensions summing to $N$ and sink dimensions to $Wm-N$, the signed increase is $Wm-2N$.",
     r"The signed sum of dimension changes telescopes at every gate: each"),
   inf("S1.3.2.3",
     r"There are $Ic$ decreasing edges, each of loss $h$, so $L=Ich$ and replacing signed changes by absolute changes adds $2L$.",
     r"There are $Ic$ decreasing edges, each of loss $h$; replacing signed"),
  ])

S1_3_3 = inf("S1.3.3",
  r"The loss is a fraction of the source total: $L_{\rm b}/N=100/539<1/2$.",
  r"\frac{L_{\rm b}}{N}=\frac{100}{539},\qquad")

S1_3_4 = show("S1.3.4",
  r"Taking rational matrices $P_U$ (projection onto the label $U$) at vertices, the total rank of the edge differences is $s=Wm-N+2L<Wm$, with deficit $N-2L>0$.",
  "Turn dimension changes into matrix ranks: an edge matrix $P_V-P_U$ has rank $\\dim V-\\dim U$, with one stated exception, then substitute the budget.",
  "The tape recursion pays one smaller interchange per unit of edge rank, so the dimension budget must be converted into a rank budget before it can be used.",
  "recoverable",
  [
   inf("S1.3.4.1",
     r"For nested nondegenerate labels $U\subset V$, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement, so its rank is $\dim V-\dim U$, and reversing the edge does not change the rank.",
     r"$P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its"),
   inf("S1.3.4.2",
     r"The only exceptions to rank equal to dimension change are the $N$ negative source projections: each first edge matrix $2P_{U_a}$ has rank one although the dimension change is zero.",
     r"The only exceptions are the $N$ negative source projections."),
   inf("S1.3.4.3",
     r"Hence $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$, and its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$ because $L_{\rm b}<N/2$.",
     r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.",
     salient="The inequality $s<Wm$ is strict but the relative deficit is only about $10^{-11}$; the whole power saving rests on this thin margin, which exists because the negative source projections and the loss $L$ together use less than $N$ of the budget."),
  ])

S1_3_5 = inf("S1.3.5",
  r"Since the relative deficit exceeds $20\cdot2^{-50}$ and $\log m<20$, the exponent $\tau=1-2^{-50}$ satisfies $s/W<m^\tau$.",
  r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,")

S1_3 = show("S1.3",
  r"Subspaces of a fixed $m$-dimensional space can be attached to the gates and terminals of the exchange network so that adjacent labels are nested and the total number $s$ of edge ranks is strictly less than $Wm$, the number of wires times the dimension.",
  "Label gates with subspaces built from tensor products of indicator vectors of three-element subsets, then count dimension and rank changes along every edge.",
  "The recursion that follows needs a network in which the total rank of the changes of representation is smaller than the number of wires times $m$; nested labels make each edge cost only its dimension change, so the count can be done exactly.",
  "recoverable",
  [S1_3_1, S1_3_2, S1_3_3, S1_3_4, S1_3_5],
  page="subset-intersection-labels",
  frm=["rank-and-orthogonal-subspaces", "array-frames", "scratch-restoring-exchange", "sets-subsets-and-cartesian-products", "dot-product-inner-product-and-orthogonality"])

S1_4 = show("S1.4",
  r"For a rational $m\times m$ matrix $A$ of rank $a$, the address map $(H,D)\mapsto(H+AD,D)$ can be performed with exactly $a$ interchanges of pairs of smaller fields and $O(V)$ further work.",
  "Factor $A=E_1\\Pi E_2$ with lower triangular $E_1,E_2$ and a partial permutation $\\Pi$ with $a$ ones, do the triangular parts as linear-time controlled updates, and realise each one of $\\Pi$ by a single interchange.",
  "Lower triangular changes of coordinates can be performed in tape order in linear time (a later field is updated from earlier fields), so only the $a$ pivots of the partial permutation need genuine interchanges.",
  "explicit",
  [
   inf("S1.4.1",
     r"Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with exactly $a$ ones.",
     r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization"),
   inf("S1.4.2",
     r"To apply $H\leftarrow H+AD$, transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$.",
     r"For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,"),
   inf("S1.4.3",
     r"Each one of $\Pi$ calls for $H_i\leftarrow H_i+D_j$, done by two controlled updates around exactly one interchange of $H_i$ and $D_j$, so the number of interchanges is the rank $a$.",
     r"The first and last updates target a later field controlled by an earlier"),
  ],
  mot_quote="can be performed entirely in this direction.",
  page="address-shear-factorization",
  frm=["controlled-cyclic-shift", "rank-and-orthogonal-subspaces", "triangular-and-permutation-matrices", "matrices-vectors-and-linear-maps"])

# power width + key step
KEY = show("S1.5.5",
  r"The time per unit volume of the power-width interchange satisfies $F_k\le(s/W)F_{k-1}+O(1)$ and hence $F_k=O(e^\tau)$ with $e=m^k$, because $s/W<m^\tau<m$: each factor of $m$ in the width multiplies the cost per volume by less than $m$.",
  "Count the recursive calls and their volumes, write the recurrence for time divided by volume, and sum the resulting geometric series, treating the cases $s/W\\le1$ and $s/W>1$.",
  "Multiplying the parameter by $m$ replaces one call by $s$ calls each on $1/W$ of the volume, so the cost per volume is multiplied by $s/W$; since $s<Wm$ this factor is strictly below $m$, which is exactly a power saving.",
  "explicit",
  [
   inf("S1.5.5.1",
     r"The number of recursive calls is exactly $s=\sum_e\operatorname{rank}A_e$: each edge $e$ applies the shear $\Phi_{A_e}$, which by the shear lemma costs exactly $\operatorname{rank}A_e$ interchanges of $b$-digit fields (including the rank-one negative source projections), and no other recursive calls are made.",
     r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
   inf("S1.5.5.2",
     r"Each recursive call acts on one role stream of volume $V/W$, because the rows were split evenly among the $W$ roles and every stream keeps all the remaining address fields.",
     r"Each acts on one role stream of volume $V/W$, retaining all other"),
   inf("S1.5.5.3",
     r"Splitting, merging, the pointwise gates and the triangular updates at one node cost $O(V)$ in total, because their number is fixed.",
     r"merging, gates, and triangular operations have total cost $O(V)$ because"),
   inf("S1.5.5.4",
     r"If $F_k$ bounds time divided by logical volume, then $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$: the $s$ calls on volume $V/W$ cost $s(V/W)F_{k-1}$, which divided by $V$ gives the factor $s/W$.",
     r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1).",
     frm=["divide-and-conquer-and-recurrences"]),
   inf("S1.5.5.5",
     r"For $a=s/W<m^\tau$, the geometric sum $\sum_{j=0}^k a^j$ bounds the unrolled recurrence.",
     r"For $a=s/W<m^\tau$ the geometric sum",
     frm=["geometric-series-and-sums"]),
   inf("S1.5.5.6",
     r"The sum is $O(m^{k\tau})$ in both cases: if $a\le1$ it is at most $k+1=O(m^{k\tau})$, and if $a>1$ it is $O(a^k)=O(m^{k\tau})$ since $a<m^\tau$.",
     r"most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$."),
   inf("S1.5.5.7",
     r"Hence $F_k=O(e^\tau)$, since $m^{k\tau}=e^\tau$.",
     r"Hence $F_k=O(e^\tau)$."),
   inf("S1.5.5.8",
     r"Scheduling the $s$ recursive calls on a fixed number of tapes by parking the inactive streams on a stack adds only $O(V)$ per node, so the recurrence overhead is not increased, even though each child has volume $V/W$.",
     r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
  ],
  mot_quote="is the source of the power saving.",
  page="rank-saving-recurrence",
  frm=["subset-intersection-labels", "array-frames", "address-shear-factorization", "divide-and-conquer-and-recurrences", "geometric-series-and-sums"],
  salient="The exponent $\\tau$ is strictly below 1 although $s/W$ is within a relative $10^{-11}$ of $m$: the growth factor per level is $s/W<m$ rather than $m$, so the cost per volume is a power $e^\\tau$ of the width instead of linear in it.")

S1_5 = show("S1.5",
  r"For $e=m^k$, two disjoint chunks of $e$ radix-$q$ digits can be interchanged in $O(Ve^\tau)$ time by running the bit network on $W$ role streams, each edge being an address shear done by smaller interchanges.",
  "Split rows among the $W$ roles, apply the network with address-shear frames so that every role receives the shear $H\\leftarrow H+D$, turn the shear into an interchange by two triangular updates, and solve the cost recurrence.",
  "The network exchanges banks and restores scratch, and its edge frames are address shears; running it row-wise on role streams reduces a chunk interchange to $s$ interchanges of chunks $m$ times smaller on $1/W$ of the volume.",
  "recoverable",
  [
   inf("S1.5.0",
     r"For $k=0$ a single digit is interchanged by the elementary stream operation in $O(V)$ time.",
     r"For $k=0$ apply the single-digit operation of"),
   inf("S1.5.1",
     r"Rows are split cyclically into $W$ role streams within each prefix, so each stream has the same remaining shape and volume $V/W$.",
     r"Split whole rows cyclically into $W$ role streams within each prefix"),
   inf("S1.5.2",
     r"On every circuit edge the address shear $\Phi_{A_e}$ is applied to that role stream, implemented by recursively interchanging each pivot pair of $b$-digit fields; each gate acts pointwise at matching addresses.",
     r"Lemma~\ref{lem:matrix-shear}, recursively interchanging each pivot pair"),
   inf("S1.5.3",
     r"By the common-frame identity and $M_{\mathrm{out}(\rho(w))}-M_{\mathrm{in}(w)}=I_m$, the result is $H\leftarrow H+D$ on every original row, including rows assigned to scratch roles.",
     r"is $H\leftarrow H+D$ on every original row, including rows assigned"),
   inf("S1.5.4",
     r"The three updates $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ interchange the chunks, and only the middle shear uses the circuit.",
     r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,"),
   KEY,
  ],
  mot_quote=None,
  page="power-width-interchange",
  frm=["address-shear-factorization", "subset-intersection-labels", "array-frames", "scratch-restoring-exchange"],
  adds=[
    B("m", "field count", "the number of fields into which each chunk is split, equal to the dimension of the label space", "count"),
    B("W", "wire count", "the number of wires of the network, equal to the number of role streams", "count"),
    B("s", "total edge rank", "the sum over the edges of the network of the rank of the edge matrix, which is the number of smaller interchanges per call", "count"),
    B("\\tau", "interchange exponent", "a fixed rational exponent below 1 with $s/W<m^\\tau$"),
  ])

S1_6 = show("S1.6",
  r"For arbitrary widths and row counts, any two equal-width chunks of $u$ bits can be interchanged in $O(Vu^\tau)$ steps.",
  "Borrow rows from the top digits of the chunks, pad the row count to a multiple of $W^k$, write the remaining width in base $m$, and apply the power-width interchange to each piece.",
  "The power-width interchange needs a power-of-$m$ width and enough rows; a base-$m$ decomposition and a few high digits used as rows remove both restrictions at a cost below the final bound.",
  "recoverable",
  [
   inf("S1.6.1",
     r"Rows for a general array can be supplied by the top $\rho=O(\log e)$ digits of the chunks themselves, which are moved separately.",
     r"Rows for a general array can be supplied by a few of its own high digits."),
   inf("S1.6.2",
     r"The row count $R=q^{2\rho}\ge W^k$ is padded with zero rows to $R'=W^k\lceil R/W^k\rceil<2R$, at most doubling the volume.",
     r"R'=W^k\left\lceil R/W^k\right\rceil<2R."),
   inf("S1.6.3",
     r"The remaining width is written in base $m$ as $e-\rho=\sum_{j=0}^k a_jm^j$ with $0\le a_j<m$, giving $a_j$ pieces of width $m^j$.",
     r"e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m."),
   inf("S1.6.4",
     r"Applying the power-width interchange to each pair of pieces costs $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$, a geometric sum because $a_j<m$ and $m^k<me$.",
     r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)."),
   inf("S1.6.5",
     r"Binary chunks of $u$ bits are padded to radix-$q$ ranges $[q^e]$ with $q^e\ge2^u$ at a fixed-factor volume increase, so the bound is $O(Vu^\tau)$.",
     r"Finally, for binary chunks let $e$ be the least integer with"),
  ])

S1 = show("S1",
  r"Two disjoint contiguous address fields of $u$ bits in an array of bit volume $V$ can be interchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$, using XOR combinations of intermediate data although the final effect is an exact permutation.",
  "Use a fixed linear network that exchanges two banks of values and restores its scratch wires; give its wires labelled representations so that each edge is an address shear made of smaller interchanges, and exploit that the total number of smaller interchanges is less than $W$ times the field count $m$.",
  "A plain scan of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ levels already costs $n\\log n$, so address movement must beat linear cost per level; a recursion whose branching $s$ is less than $W m$ gives that power saving.",
  "recoverable",
  [S1_1, S1_2, S1_3, S1_4, S1_5, S1_6],
  page="address-chunk-interchange",
  frm=["tape-address-model", "controlled-cyclic-shift", "permutations-and-bijections"])

# ---------------- S2 : simultaneous butterfly layer ----------------
S2_5 = show("S2.5",
  r"For $f$ chunks at once, $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ on the selected bits $j_i=\rho+iK$ takes a constant number of whole-chunk cyclic shifts that are correct away from a set of addresses of fraction at most $80(f-1)2^{-K}$, which is repaired deterministically by sorting.",
  "Emulate the bitwise XOR of $f$ selected bits by eight rotations of whole chunk ranges, then identify and correct exactly the guard-violating addresses.",
  "A bit-by-bit XOR over $f$ chunks would cost $f$ passes; shifting whole chunks does all the selected bits in one pass and fails only on a few addresses, whose number is small because $K/\\log p\\to\\infty$.",
  "recoverable",
  [
   inf("S2.5.1",
     r"With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$ the time of one packed addition on a rectangle of $R$-bit records is $O(V(L^\tau+1)+MA^3+\delta_{\rm bad}MA(R+A))$, where $L=fK$.",
     r"With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, its time is"),
   inf("S2.5.2",
     r"Eight rotations of the target ranges, controlled by predicates of the current values, have the required effect away from a small set of addresses.",
     r"We first construct eight rotations that have the required effect away"),
   inf("S2.5.3",
     r"The exceptional addresses depend only on addresses, not payloads; they are corrected exactly by sorting the compact exceptional stream, so the bound is worst-case over payloads.",
     r"from a small set of addresses. We then correct exactly that set."),
  ],
  page="packed-selected-bit-addition",
  frm=["address-chunk-interchange", "controlled-cyclic-shift", "arithmetic-modulo-2-and-xor", "sorting-and-its-cost"],
  salient="The exceptional set has relative size $O(f2^{-K})$, which is tiny because the chunk width $K$ grows faster than $\\log p$.")

S2_6 = show("S2.6",
  r"The tensor $C^{\otimes D}$ layer, and hence the whole layer, costs $O(Vd^{\lambda'})$: with $F(e)$ the time per unit volume for $e=m^k$ chunks, $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ and base cases $F(e)=O(e)$ for $e<d^\beta$.",
  "Split rows among the $W$ roles, solve the same cost recurrence as for address interchange with an extra overhead term from the packed basis changes, and handle a general $D$ by a base-$m$ partition.",
  "The phase network has the same rank-saving property $s<Wm$ as the bit network, so the same recursion gives a power saving; the overhead of basis changes $(eK)^\\tau$ is lower order for $e\\ge d^\\beta$.",
  "recoverable",
  [
   inf("S2.6.1",
     r"Each recursive edge call acts on one role stream of volume exactly $1/W$ of its parent's logical volume, since every row is sent whole to one role.",
     r"scratch roles from existing rows.  Each recursive edge call acts on"),
   inf("S2.6.2",
     r"With $F(e)$ the time divided by logical volume, $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ and $F(e)=O(e)$ for $e<d^\beta$.",
     r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
   inf("S2.6.3",
     r"The internal costs sum to $O(e^\lambda)$ since $a=s/W\le m^\sigma<m^\lambda$ and the overhead is $O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)$ for $e\ge d^\beta$.",
     r"Since \(a\le m^\sigma<m^\lambda\), the internal"),
   inf("S2.6.4",
     r"The leaves contribute at most $O(a^ju)\le O(e^\sigma u^{1-\sigma})\le O(e^\sigma d^{\beta(1-\sigma)})$ because $a^j\le m^{j\sigma}=(e/u)^\sigma$.",
     r"O(a^ju)\le O(e^\sigma u^{1-\sigma})"),
   inf("S2.6.5",
     r"Writing $D-q_0$ in base $m$ and adding at most $(m-1)(1+\lfloor\log_md\rfloor)$ pieces gives total cost $O(d^{\lambda'})$ per unit volume for any fixed $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$.",
     r"Partition the remaining chunks into \(a_j\) consecutive pieces"),
  ])

S2 = show("S2",
  r"The two-point butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ can be applied at the same bit position in each of $D\le d$ address chunks of an array of polynomial records of complex fixed-point coefficients in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$, with one final truncation.",
  "Write the butterfly layer as a tensor power of the kernel $C$, realise $C^{\\otimes e}$ by the complex phase network with rank saving, perform the network's binary changes of basis by packed selected-bit additions and chunk interchanges, and unroll the cost recurrence.",
  "Applying the butterflies one axis at a time takes $D$ whole-array passes; the phase network handles all $D$ selected bits at once at a power saving in $d$.",
  "explicit",
  [
   inf("S2.1",
     r"The complex phase network over Gaussian dyadics with binary labels has edge frames that are products of translation kernels $aI+bX_v$, one per orthonormal basis vector of the edge residual, with $s<Wm$ of them in all, and after corrections its endpoint operator is $C^{\otimes m}$ on every role, scratch roles included.",
     r"bank exchange, telescoping these phase frames gives $C^{\otimes m}$",
     deferred=True, page="phase-frame-network",
     frm=["subset-intersection-labels", "array-frames", "fixed-point-complex-arithmetic", "dyadic-rationals-and-fixed-width-numerators"],
     salient="Although each edge is a different product of translation kernels, telescoping the frames gives the same $C^{\\otimes m}$ on every role, including the auxiliary scratch roles, because $C=iZC^{-1}Z$ turns every inverse factor into a forward one."),
   inf("S2.2",
     r"Gaussian elimination writes any invertible binary change of basis $M\in\operatorname{GL}(m,\mathbb F_2)$ as a fixed number (at most $m(m-1)+3m$) of row additions, each of which XORs corresponding selected bits of two whole slots, so the basis changes need only packed selected-bit additions.",
     r"Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$"),
   inf("S2.3",
     r"A network invocation on $e=mf$ selected axes uses exactly $s$ child calls, each on the $f=e/m$ axes of one slot, with no extra calls from the inverse wrappers.",
     r"$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
   inf("S2.4",
     r"The normalized layer is recovered from the $C$ layer by diagonal phases: $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, all exact Gaussian dyadic operations.",
     r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D."),
   S2_5,
   S2_6,
   inf("S2.7",
     r"The whole layer is evaluated exactly with at most $p+\lceil C_0d^{C_1}\rceil$ fractional bits, an $O(p)$ width since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, before a single truncation.",
     r"The accelerated network is evaluated exactly until an entire"),
   inf("S2.8",
     r"Every row of $\mathcal H$ has absolute row sum one, so the layer maps disk arrays to disk arrays and the single truncation adds error less than $\sqrt2\,2^{-p}$.",
     r"Finally, every row of $\mathcal H$ has"),
  ],
  mot_quote="$\\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly".replace("\\\\","\\"),
  page="simultaneous-butterfly-layer",
  frm=["fixed-point-complex-arithmetic", "fft-butterflies", "address-chunk-interchange", "rank-saving-recurrence", "phase-frame-network", "packed-selected-bit-addition"],
  adds=[
    B("d", "chunk bound", "the maximum number of address chunks acted on by one layer", "count"),
    B("K", "chunk width", "the number of bits in each address chunk", "count"),
  ])

# ---------------- S3 : normalized ring convolution ----------------
S3_1 = show("S3.1",
  r"Over $\mathcal R_r=\mathbb C[y]/(y^r+1)$, the transforms $F_t^\pm$ with roots $\omega_t=y^{2r/t}$ satisfy $F_t^+F_t^-=t^{-1}I$, are contractions, and are computed by $\log_2t$ rounds of $H_0$ butterflies with twiddles that are signed coefficient shifts.",
  "Use the decimation-in-frequency recursion of the FFT with roots of unity taken to be powers of $y$, and check character cancellation directly because the ring has zero divisors.",
  "Powers of $y$ are exact isometries acting as signed shifts of the coefficient list, so twiddle multiplications need no real arithmetic and add no error.",
  "explicit",
  [
   inf("S3.1.1",
     r"For a power of two $t$ dividing $2r$, $\omega_t=y^{2r/t}$, and the transforms $F_t^\pm$ average $t$ copies of the input weighted by powers of $\omega_t^{\mp1}$.",
     r"For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$."),
   inf("S3.1.2",
     r"Every power of $\omega_t$ is an isometry and each output averages $t$ such images, so both transforms are contractions.",
     r"Thus both transforms are contractions."),
   inf("S3.1.3",
     r"Character cancellation $\sum_{k=0}^{t-1}\omega_t^{jk}=0$ for $t\nmid j$ holds because replacing $k$ by $k+t/2^{v+1}$ multiplies the sum by $y^{rj_0}=-1$ and the additive group has no two-torsion, so $F_t^+F_t^-=t^{-1}I$.",
     r"Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes"),
   inf("S3.1.4",
     r"The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$, applies $H_0$, multiplies the second output by $\omega_t^{-k}$ and recurses on both halves, computing $F_t^-$.",
     r"the $b=1$ output by $\omega_t^{-k}$, and then apply the length-$t/2$"),
  ],
  mot_quote="such a root is a signed shift of the coefficient list. These are the",
  page="synthetic-polynomial-transform",
  frm=["negacyclic-ring", "discrete-fourier-transform", "fft-butterflies", "roots-of-unity-and-euler-s-formula"],
  salient="The roots of unity are powers of $y$, which are exact signed shifts of the coefficient list, so twiddle multiplications cost no arithmetic and contribute no numerical error.")

S3_2_PLACEHOLDER = 0
S3_2 = show("S3.2",
  r"By placing the selected bit of each participating axis at a common offset in consecutive $K$-bit chunks, every transform round is one simultaneous butterfly layer, and the forward or opposite transform costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error less than $\sqrt2\ell\,2^{-p}$.",
  "Move the top bits of each axis to a prefix with bit moves, then rearrange the remaining $K$-bit chunks by chunk interchanges so that chunks of the same index of all axes are adjacent, and apply the layer to each round.",
  "The simultaneous layer needs the selected bits of all participating axes at one offset inside consecutive equal chunks, which the original axis-major layout does not provide.",
  "explicit",
  [
   inf("S3.2.0",
     r"Across several axes, the twiddles of the individual axes commute with the other axes' butterflies, so one round is a parallel butterfly $\mathcal H$ followed by one recordwise monomial $y^E$ with $E=-\sum_i(2r/u_i)b_ik_i\pmod{2r}$; every round is a contraction.",
     r"Consequently the individual axis steps may be grouped as a parallel"),
   inf("S3.2.1",
     r"The transform costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with the three terms from prefix moves, chunk exchanges and simultaneous rounds, and layout construction and restoration are charged in it.",
     r"O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right)."),
   inf("S3.2.2",
     r"A list of at most $D(b+1)=O(dK)$ slots (the top bit of long axes and the low $b$ bits) is moved to a prefix by bit moves costing $O(TpdK)$.",
     r"Form a list of the slots to move to a prefix."),
   inf("S3.2.3",
     r"The remaining chunks are reordered by scanning target positions left to right and exchanging chunks: at most $Dq-1=O(p/K)$ exchanges of width-$K$ chunks, each costing $O(TpK^\tau)$, for a total of $O(Tp\,pK^{\tau-1})$.",
     r"To obtain this order, scan its target positions from left to right."),
   inf("S3.2.4",
     r"Each round of at most $\ell$ rounds is one call of the simultaneous layer at cost $O(Tpd^{\lambda'})$, so the rounds cost $O(Tp\ell d^{\lambda'})$ in total.",
     r"The simultaneous-layer procedure therefore applies at cost"),
  ],
  mot_quote="we must place the selected bits of the participating axes at a common",
  page="transform-tape-layout",
  frm=["synthetic-polynomial-transform", "address-chunk-interchange", "simultaneous-butterfly-layer", "stored-frequency-order"])

S3_3 = show("S3.3",
  r"Two polynomials of degree less than $r$ with small signed coefficients can be multiplied exactly, and $Q_p(fg/r)$ returned, in time $O(rp\log(rp))$ using the $O(N\log N)$ integer multiplier.",
  "Evaluate the polynomials at $B_0=2^{4p}$ by packing signed coefficients with carries, multiply the resulting integers, and extract the product coefficients by centered residues.",
  "Evaluation at a large power of two turns polynomial multiplication into integer multiplication, so the Harvey-van der Hoeven multiplier does the work on short inputs.",
  "recoverable",
  [
   inf("S3.3.1",
     r"The exact Gaussian integer numerators of $fg$ are computed and $Q_p(fg/r)$ returned in time $O(rp\log(rp))$ on a fixed number of tapes, with error less than $\sqrt2\,2^{-p}$.",
     r"numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time"),
   inf("S3.3.2",
     r"With $B_0=2^{4p}$, each signed coefficient polynomial $u$ is packed into the integer $A_u=u(B_0)$, which fits in $4pr$ bits.",
     r"Set $B_0=2^{4p}$"),
   inf("S3.3.3",
     r"Every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so fields never overlap and the next coefficient is the unique centered residue modulo $B_0$.",
     r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
   inf("S3.3.4",
     r"Signed coefficients are packed using carries $\gamma_j\in\{-1,0\}$ so the blocks are a two's-complement encoding of $A_u$, with $\gamma_r=-1$ exactly when $A_u<0$.",
     r"d_j\equiv u_j+\gamma_j\pmod{B_0},\quad 0\leq d_j<B_0,"),
   inf("S3.3.5",
     r"Coefficients are extracted block by block as the unique integer in $[-B_0/2,B_0/2)$ congruent to $q_j+\rho_j$ modulo $B_0$, with carry $\rho_j\in\{0,1\}$, in time $O(rp)$.",
     r"integer in $[-B_0/2,B_0/2)$ congruent to $q_j+\rho_j$ modulo $B_0$,"),
   inf("S3.3.6",
     r"Four exact integer products dominate the linear packing, extraction, wrapping modulo $y^r+1$ and truncation costs.",
     r"Four exact integer products dominate the linear"),
  ],
  page="signed-packing",
  frm=["n-log-n-barrier", "negacyclic-ring", "binary-numerals-and-bit-strings"])

S3 = show("S3",
  r"Arrays over $\mathcal R_r$ on power-of-two axes can be convolved to give $(f*g)/T$ with error less than $\sqrt2M(3\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.",
  "Perform two forward synthetic transforms retaining their common stored order, multiply pointwise in the ring by signed packing, apply the opposite transform to that order and scale by $M$, tracking error with contractions.",
  "Pointwise multiplication commutes with applying one record permutation to both operands, so no permutation of the transformed data is needed between the transforms.",
  "explicit",
  [
   S3_1,
   show("S3.1.5",
     r"The forward procedure writes frequencies in bit-reversed order, and the reverse procedure consumes that order, so the two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$ with $B_t$ never executed.",
     "Track which address-bit slot holds each frequency bit through the recursion, then run the recursion backwards for the opposite transform.",
     "The pointwise product treats all entries alike, so it does not care in which order the frequencies are stored; keeping the stored order avoids a permutation of the whole array.",
     "recoverable",
     [
      inf("S3.1.5.1",
        r"After all rounds, the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$, so the recursion writes its outputs directly in bit-reversed order.",
        r"entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$."),
      inf("S3.1.5.2",
        r"The reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$, because $H_0^2=I/2$ and each of the $a=\log_2t$ levels is invertible, so it equals $F_t^+B_t^{-1}$.",
        r"so the reverse procedure composed with $B_tF_t^-$ is"),
     ],
     page="stored-frequency-order",
     frm=["synthetic-polynomial-transform", "permutations-and-bijections"],
     salient="No frequency permutation is ever executed: the forward transform, the pointwise product and the opposite transform all use the same bit-reversed order."),
   S3_2, S3_3,
   inf("S3.4",
     r"Both forward transforms are performed retaining their common order, the polynomial records are multiplied pointwise with the packing lemma, the opposite transform is applied to that order, and the result is multiplied exactly by $M=T/r$.",
     r"Perform both forward transforms and retain their common $LB$ order."),
   inf("S3.5",
     r"Normalization holds because $F_{\boldsymbol t}^-(f*g)=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)$ and $F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$, giving $MF^+_{\boldsymbol t}((F^-_{\boldsymbol t}f)(F^-_{\boldsymbol t}g)/r)=(f*g)/(rM)$.",
     r"To check normalization, expansion of the finite sums gives"),
   inf("S3.6",
     r"The error is less than $M(3\delta+\eta)=\sqrt2M(3\ell+1)2^{-p}$ because the two forward errors and the product truncation add through the bilinear contraction $P$ and the contraction $\mathcal T_+$.",
     r"For the error estimate, put",
     frm=["contraction-error-propagation", "triangle-inequality-and-norms"]),
  ],
  mot_quote="Pointwise multiplication commutes with applying the same record",
  page="normalized-ring-convolution",
  frm=["contraction-error-propagation", "convolution", "negacyclic-ring"])

# ---------------- S4 : tensor source transform ----------------
S4_2 = show("S4.2",
  r"A Fourier transform of length $s$ is obtained from one of length $t>s$ with $\gcd(s,t)=1$ as $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, for Gaussian-weighted linear contractions $A$ and $B_0$, with the two coordinate permutations $P_s,P_t$ kept in the formula.",
  "Use the Gaussian identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ of Harvey and van der Hoeven, invert $N=C\\mathsf T\\mathsf D$ by a Neumann series, and renormalise the pieces into contractions.",
  "Resampling by Gaussians replaces a transform of a prime length by one of a power-of-two length, the shape that the synthetic transforms handle.",
  "recoverable",
  [
   inf("S4.2.1",
     r"There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$.",
     r"P_sF_s=2^{2\alpha^2}B_0P_tF_tA."),
   inf("S4.2.2",
     r"The Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$ holds.",
     r"\mathsf T P_sF_s=P_tF_t\mathsf S,"),
   inf("S4.2.3",
     r"The correction $N=C\mathsf T\mathsf D$ satisfies $\|N-I\|<2^{-\alpha^2\theta}<1/2$, so $N$ is invertible by a Neumann series.",
     r"\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}."),
   inf("S4.2.4",
     r"Setting $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$, with normalizations of product $2^{-2\alpha^2}$, gives contractions with the claimed identity.",
     r"Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$."),
  ],
  mot_quote="whereas the synthetic transforms use powers of two. Gaussian resampling",
  page="gaussian-resampling",
  frm=["discrete-fourier-transform", "contraction-error-propagation", "exponential-logarithm-and-gaussian-function", "triangle-inequality-and-norms"])

S4_5 = show("S4.5",
  r"With the source permutation $R$ kept in the transform formula, $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$, so no full sort is executed.",
  "Show $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$ by substituting $h=ck$ in the Fourier sum, use that permutations commute with pointwise products, then apply the convolution rule.",
  "Gaussian resampling forces a permutation on each side of the transform; if it cancels between the two forward transforms, the pointwise product and the opposite transform, the sorts are never needed.",
  "explicit",
  [
   inf("S4.5.1",
     r"For a unit $c$ modulo $q$, $F_q^+R_c=R_c^{-1}F_q^+$; each $t_i$ is a unit modulo $s_i$, so tensoring gives $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.",
     r"Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives"),
   inf("S4.5.2",
     r"With $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$ and $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$, the cancelled expression equals $(u*v)/S^2$.",
     r"proving \eqref{eq:source-permutation-cancel}."),
  ],
  mot_quote="coordinate. We retain both permutations in the transform formula and",
  page="permutation-cancellation",
  frm=["gaussian-resampling", "discrete-fourier-transform", "permutations-and-bijections", "modular-arithmetic"],
  salient="The permutation $R$ appears in each of the three transforms yet disappears from the result, because a coordinate permutation by a unit commutes with the opposite-sign transform up to inversion ($RF^+R=F^+$) and with pointwise products.")

S4_4 = show("S4.4",
  r"The middle transform with its frequency permutation is a pointwise chirp phase around a cyclic convolution with the chirp: $QF_{\boldsymbol t}u=\bar a\cdot(a*(\bar a\cdot u))/T$ for $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$.",
  "Expand the right side coefficientwise and see that the chirp phases combine to the Fourier kernel with permuted frequencies.",
  "A convolution can be computed by the ring convolution already built, so rewriting the transform as a convolution reuses it, including the frequency permutation $Q$.",
  "recoverable",
  [
   inf("S4.4.1",
     r"The chirp $a$ has period $t_i$ in coordinate $i$ because replacing $j_i$ by $j_i+t_i$ changes the exponent by an integral multiple of $2\pi i$.",
     r"Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by"),
   inf("S4.4.2",
     r"The coefficient of $u_{\boldsymbol k}$ on the right is $\frac1T\exp(2\pi i\sum_is_ij_ik_i/t_i)$, precisely the coefficient of $QF_{\boldsymbol t}$.",
     r"This is precisely the coefficient in $QF_{\boldsymbol t}$, because"),
  ],
  page="bluestein-chirp",
  frm=["discrete-fourier-transform", "convolution", "roots-of-unity-and-euler-s-formula"])

S4_6 = show("S4.6",
  r"Multiplying coefficient $k$ of the last axis by $\zeta^k$ with $\zeta=e^{\pi i/r}$ is an isomorphism from $\mathbb C[x_d]/(x_d^r-1)$ onto $\mathbb C[y]/(y^r+1)$ carrying cyclic convolution on that axis to negacyclic convolution, and untwisting recovers the cyclic result.",
  "Check that $x_d\\mapsto\\zeta y$ is well defined and diagonal in the monomial bases, then verify the sign at the wrap.",
  "The chirp convolution is a cyclic convolution on every axis, but the synthetic transform needs the last axis to be negacyclic, so the cyclic wrap must be converted by a phase.",
  "recoverable",
  [
   inf("S4.6.1",
     r"The map $x_d\mapsto\zeta y$ is well defined since $(\zeta y)^r=(-1)(-1)=1$, and diagonal with entries $\zeta^k$, so it is an isomorphism preserving the sup norm.",
     r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$.", deferred=True),
   inf("S4.6.2",
     r"At the wrap $k+l=j+hr$ with $h\in\{0,1\}$, the twisted and negacyclically reduced term has factor $\zeta^{k+l}(-1)^h=\zeta^j$.",
     r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j.", deferred=True),
   inf("S4.6.3",
     r"Untwisting therefore recovers the cyclic coefficient with the correct sign.",
     r"Untwisting therefore recovers the cyclic coefficient with the correct", deferred=True),
  ],
  page="coefficient-twist",
  frm=["negacyclic-ring", "convolution", "roots-of-unity-and-euler-s-formula", "complex-numbers"])

S4 = show("S4",
  r"The source Fourier transform $RF_{\boldsymbol s}$ on the prime-length source, stored in the padded power-of-two box, is approximated by linewise Gaussian maps $\mathcal A$, the chirp convolution of length $T$, linewise maps $\mathcal B_0$ and an exact scale $2^\gamma$.",
  "Apply Gaussian resampling line by line to reach power-of-two lengths, rewrite the power-of-two transform as a chirp convolution, evaluate that convolution over the polynomial ring after a coefficient twist, and compose with the maps back.",
  "The transform lengths needed for the product are pairwise coprime primes, whereas the fast synthetic transforms need powers of two; resampling connects the two shapes.",
  "explicit",
  [
   S3, S4_2,
   inf("S4.3b",
     r"Exposing and restoring all lines of the padded box costs $O(Tpd^2(1+\ell^\tau))$ by the equal-width chunk interchange, and the line maps cost $O(dTp^{3/2+\delta}\alpha)$ in total.",
     r"using the equal-width chunk-swap bound $O(Vu^\tau)$ and the fixed-digit",
     frm=["address-chunk-interchange"]),
   inf("S4.3",
     r"Tensoring the one-dimensional identity gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$; $\mathcal A$ and $\mathcal B_0$ are applied line by line on the padded box, expanding and compressing one axis at a time.",
     r"Tensoring \eqref{eq:no-sort-one-dimensional} proves",
     frm=["multidimensional-arrays-and-row-major-order"]),
   S4_4, S4_5, S4_6,
   inf("S4.7",
     r"The computed source transform applies the linewise approximation to $\mathcal A$, the computed chirp transform, the linewise approximation to $\mathcal B_0$ and an exact multiplication of the numerators by $2^\gamma$; its exact counterpart is $RF_{\boldsymbol s}$.",
     r"For a source disk-grid tensor of norm at most $.5$, write", deferred=True),
  ],
  mot_quote="whereas the synthetic transforms use powers of two. Gaussian resampling",
  page="tensor-source-transform",
  frm=["gaussian-resampling", "bluestein-chirp", "coefficient-twist", "normalized-ring-convolution", "permutation-cancellation", "address-chunk-interchange", "fixed-point-complex-arithmetic"])

# ---------------- S5.. ----------------
S5 = show("S5",
  r"Choosing precision $p=6b$, dimension $d\approx p^\epsilon$, record length $r=2^{\Theta(p^{1-\epsilon})}$, power-of-two axis lengths $t_i\in\{r/2,r\}$ with $\prod_it_i=T$, and distinct primes $s_i$ just below $t_i$ gives $Tp=\Theta(n)$ and satisfies the hypotheses of every interface.",
  "Fix explicit rational exponents, define the sizes from the input length $n$, find the primes by an $n^{o(1)}$ search, and verify each hypothesis of the layer, transform and resampling lemmas.",
  "The primes must be close to the powers of two so that their product fills a fixed fraction of the padded box, while each ratio $t_i/s_i$ must leave enough separation for resampling.",
  "explicit",
  [
   inf("S5.1",
     r"Fixed rational choices $\tau=\sigma=1-2^{-50}$, $\lambda=1-2^{-52}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$ satisfy all layer conditions.",
     r"\lambda=1-2^{-52},\qquad c=2^{-56},\qquad"),
   inf("S5.2",
     r"The sizes are $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $K=\lfloor d^c\rfloor$.",
     r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,"),
   inf("S5.3",
     r"A power of two $T\in[4n/b,8n/b)$ and $r=2^{\lceil(\log_2T)/d\rceil}$ are chosen, with some axis lengths $r/2$ and the rest $r$ so that $\prod_it_i=T$.",
     r"Take the power of two $T$ in $[4n/b,8n/b)$, and let"),
   inf("S5.4",
     r"These definitions give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$.",
     r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad"),
   inf("S5.5",
     r"The resampling parameter $\alpha=\lceil(12d^2b)^{1/4}\rceil$ satisfies $2\le\alpha<\sqrt p$ and $\gamma=2d\alpha^2=o(b)$.",
     r"\alpha=\left\lceil(12d^2b)^{1/4}\right\rceil,"),
   inf("S5.6",
     r"By the prime-interval estimate, distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ exist and give $T/2<S<T$ with $S=\prod_is_i$.",
     r"(1-2\eta)t_i<s_i\leq(1-\eta)t_i."),
   inf("S5.7",
     r"Thus every hypothesis of the one-dimensional resampling lemma holds for all sufficiently large input lengths.",
     r"Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for"),
  ],
  mot_quote="$t_i$: their product must occupy a fixed fraction of the padded box,",
  page="parameter-regime",
  frm=["simultaneous-butterfly-layer", "gaussian-resampling", "negacyclic-ring", "crt-axis-map", "primes-coprimality-and-gcd", "asymptotic-notation-beyond-big-o"],
  adds=[
    B("b", "digit width", "the number of bits in each radix digit, $b=\\lceil\\log_2n\\rceil$"),
    B("p", "precision", "the number of fractional bits of the fixed-point numbers, $p=6b$", "count"),
    B("r", "record length", "the number of complex coefficients in a polynomial record", "count"),
    B("T", "box size", "the number of entries of the padded power-of-two box, equal to the product of the axis lengths", "count"),
  ])

S6 = show("S6",
  r"Writing each $n$-bit input as $q=\lceil n/b\rceil$ digits in base $2^b$, the integer product is the digit convolution followed by carry propagation, with no wraparound modulo $x^S-1$ and coefficients below $2^{3b}$.",
  "Count the degree and coefficient size of the product of the two digit polynomials.",
  "Splitting into radix digits reduces multiplication to convolution of short integer coefficients, which a Fourier transform can compute.",
  "explicit",
  [
   inf("S6.1",
     r"The product has degree at most $2q-2<2n/b\le T/2<S$, so convolution modulo $x^S-1$ has no nonzero wraparound.",
     r"Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
   inf("S6.2",
     r"Every product coefficient satisfies $0\le c_j\le q(2^b-1)^2<2^{3b}$ since $q\le n\le2^b$.",
     r"0\le c_j\le q(2^b-1)^2<2^{3b},"),
  ],
  mot_quote="Splitting the inputs into radix digits reduces multiplication to",
  page="radix-digit-reduction",
  frm=["convolution", "polynomials", "positional-notation-in-any-radix", "schoolbook-and-karatsuba-multiplication"])

S7 = show("S7",
  r"An algebra isomorphism $\Phi$ sends $\mathbb C[x]/(x^S-1)$ onto a product of pairwise coprime cyclic axes preserving convolution, and $\Phi$ and its inverse are implemented by triangular controlled shifts and axis reorderings in $O(Tpd^2(1+\ell^\tau))$ time.",
  "Apply the Chinese remainder theorem with $x\\mapsto\\prod_ix_i^{\\mu_i}$, where $\\mu_i=P_i^{-1}\\bmod s_i$ makes the coordinate of axis $i$ depend only on earlier mixed-radix digits.",
  "These coordinate powers make the change of order a sequence of controlled cyclic shifts, each controlled by earlier fields, which the tape performs in linear time.",
  "explicit",
  [
   inf("S7.1",
     r"The assignment $x\mapsto\prod_ix_i^{\mu_i}$ respects $x^S=1$, and since each $\mu_i$ is a unit and the $s_i$ are pairwise coprime its powers run through all target monomials exactly once.",
     r"\qquad x\longmapsto\prod_i x_i^{\mu_i}",
     frm=["primes-coprimality-and-gcd"]),
   inf("S7.2",
     r"Hence $\Phi$ is an isomorphism and preserves cyclic convolution.",
     r"$\Phi$ is an isomorphism and preserves cyclic convolution."),
   inf("S7.3",
     r"For $k=\sum_ja_jP_j$ in mixed radix, the axis-$i$ coordinate of $\Phi(x^k)$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, because terms with $j>i$ are divisible by $s_i$ and $\mu_iP_i=1$.",
     r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}."),
   inf("S7.4",
     r"Each triangular update is a prefix-controlled cyclic shift of the valid target interval, performed by splitting into two pieces and merging in opposite order, and zero padding stays zero.",
     r"Each triangular update is a prefix-controlled cyclic shift."),
   inf("S7.5",
     r"Reversing all axes uses $O(d^2)$ interchanges, so $\Phi$, its inverse and the padding scans cost $O(Tpd^2(1+\ell^\tau))$.",
     r"Reversing all axes"),
  ],
  mot_quote="sequence of controlled cyclic shifts.",
  page="crt-axis-map",
  frm=["convolution", "controlled-cyclic-shift", "address-chunk-interchange", "primes-coprimality-and-gcd", "modular-arithmetic"])

S8 = show("S8",
  r"Converting to digits, applying $\Phi$, computing two forward source transforms, multiplying pointwise, applying one opposite transform, scaling twice by $S$, rounding, applying $\Phi^{-1}$ and propagating carries outputs the $2n$-bit product.",
  "Run the six listed operations in order, tracking the normalization at each: the source permutation cancels, one scale by $S$ undoes the transform normalization and the second undoes the digit scaling.",
  "The transforms compute the digit convolution, so the product is recovered after undoing the known normalizations and rounding to integers.",
  "recoverable",
  [
   inf("S8.1",
     r"Each operand is read backward in groups of $b$ bits to give the digits $a_0,\ldots,a_{q-1}$, written as the exact grid values $a_j2^{-b-2}$ followed by $S-q$ zero records.",
     r"Read each stored operand backward from"),
   inf("S8.2",
     r"Apply the coefficient-address map $\Phi$ to obtain source arrays $u,v$ of norm less than $1/4$.",
     r"\item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain"),
   inf("S8.3",
     r"Compute the two source transforms $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.",
     r"\item Compute $\widetilde{\mathscr F}(u)$ and"),
   inf("S8.4",
     r"Multiply corresponding coefficients exactly and truncate to $p$ fractional bits, giving $z$.",
     r"\item Multiply corresponding complex coefficients exactly and truncate"),
   inf("S8.5",
     r"Compute the opposite source transform of $z$ and multiply the numerators exactly by $S$.",
     r"\item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid"),
   inf("S8.6",
     r"Multiply by $2^{2b+4}S$, round to the nearest integers, and apply $\Phi^{-1}$ with padding removal.",
     r"\item Multiply the grid numerators of $\widetilde w$ exactly by"),
   inf("S8.7",
     r"Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits.",
     r"\item Propagate radix-$2^b$ carries in increasing coefficient order."),
   inf("S8.8",
     r"The two occurrences of $S$ undo different normalizations: after the three transforms the exact result is $(u*v)/S^2$, the first scale gives $(u*v)/S$ and the second, with $2^{2b+4}$, gives the original integer convolution.",
     r"The two occurrences of $S$ in this algorithm undo different",
     salient="The factor $S$ is applied twice and the source permutation never has to be undone, because $1/S^2$ is the exact normalization after the cancelled transforms."),
  ],
  page="multiplication-algorithm",
  frm=["radix-digit-reduction", "crt-axis-map", "tensor-source-transform", "permutation-cancellation", "precision-exact-recovery", "parameter-regime", "integer-division-with-remainder-floor-and-ceiling"])

S9 = show("S9",
  r"The recovered convolution coefficients are within error below $1/2$ of integers below $2^{3b}$, so rounding and carry propagation give the exact product.",
  "Propagate errors through the pipeline with contractions and disk margins: transform error bounds add through bilinear contractions, then multiply by the known scales and compare with $1/2$.",
  "Every approximate subroutine is a contraction plus a bounded error, and errors of composed maps add, so a worst-case error bound follows from adding the contributions and scaling.",
  "recoverable",
  [
   inf("S9.1",
     r"The returned normalized ring convolution has error below $E_{\rm ring}:=M(3L+2)<5TL$ in units of $2^{-p}$.",
     r"E_{\rm ring}:=M(3L+2)<5TL."),
   inf("S9.2",
     r"The source transform has error $E_s=9\,2^\gamma TL$ and the scaled approximation stays within norm $.501$.",
     r"E_s=9\,2^\gamma TL,"),
   inf("S9.3",
     r"The exact opposite contraction $G=RF_{\boldsymbol s}^+$ satisfies $G(U\cdot V_1)=(u*v)/S^2$, so the permutation cancels in the error analysis.",
     r"G(U\cdot V_1)=(u*v)/S^2."),
   inf("S9.4",
     r"After the first scaling by $S$, $\widetilde w$ approximates $w=(u*v)/S$ with error below $E_wh_p$, $E_w:=S(3E_s+2)<28\,2^\gamma T^2L$.",
     r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
   inf("S9.5",
     r"After the second scaling by $2^{2b+4}S$ the absolute error is less than $448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<1/2$.",
     r"<448b\,2^{-b+\gamma}"),
   inf("S9.6",
     r"The true coefficients are integers and the error is strictly below $1/2$, so the nearest integer to the represented value is the unique correct coefficient, in $[0,2^{3b})$.",
     r"The strict error below $1/2$ makes the nearest integer to"),
   inf("S9.7",
     r"Radix-$2^b$ carries satisfy $k_0=0$, $d_j=(c_j+k_j)\bmod Q_0$, $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$ with $0\le k_j<Q_0^2$, which yields the binary digits of the product.",
     r"k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad"),
  ],
  page="precision-exact-recovery",
  frm=["contraction-error-propagation", "tensor-source-transform", "radix-digit-reduction", "fixed-point-complex-arithmetic", "triangle-inequality-and-norms"])

S10 = show("S10",
  r"Dividing every cost by $V=Tp$, each normalized cost is at most $p^{1-2\kappa}$, with smallest margin $2^{-181}=2\kappa$ coming from the chunk-exchange term, so the total time is $O(n(\log n)^{1-\kappa})$.",
  "Tabulate the normalized cost of each operation as a power of $p$ and subtract each exponent from one to obtain margins, then take the smallest.",
  "Each operation was bounded earlier in terms of $V$, $d$, $K$, $\\ell$ and the exponents; expressing them as powers of $p$ makes them directly comparable to $p$.",
  "explicit",
  [
   inf("S10.1",
     r"With $V=Tp=\Theta(n)$, a full padded array has $\Theta(V)$ stored bits, and costs are tabulated after division by $V$.",
     r"For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient"),
   inf("S10.2",
     r"Prefix-slot moves and individual butterfly rounds cost $dK$, a power $\epsilon(1+c)$ of $p$.",
     r"Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\"),
   inf("S10.2b",
     r"Chunk exchanges for the transform layout cost $pK^{\tau-1}$, a power $1-\epsilon c(1-\tau)$ of $p$.",
     r"Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\"),
   inf("S10.4",
     r"The simultaneous butterfly rounds cost $\ell d^{\lambda'}$ with power $1-\epsilon(1-\lambda')$.",
     r"Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\"),
   show("S10.3",
     r"The seven dominant powers of $p$ have margins below one of at least $2^{-181}$, and the smallest, $g_2=\epsilon c(1-\tau)=2^{-181}=2\kappa$, comes from the chunk-exchange term.",
     "Subtract each exponent from one to get the margins $g_1,\\ldots,g_7$ and compare them; for the smallest, count the $O(p/K)$ chunk exchanges of width $K$ costing $O(VK^\\tau)$ each.",
     "The exchange bound has exponent $\\tau$ close to 1 on the chunk width $K=\\Theta(p^{\\epsilon c})$, a tiny power of $p$, so the saving on this term is the product of three tiny exponents.",
     "recoverable",
     [
      inf("S10.3.2",
        r"The margins are $g_2=\epsilon c(1-\tau)=2^{-181}$, $g_3=2^{-129}$, $g_7=2^{-75}$ and the others larger, so $\min_ig_i=2^{-181}=2\kappa$.",
        r"Thus $\min_i g_i=2^{-181}=2\kappa$."),
      inf("S10.3.3",
        r"The positional layout uses $O(p/K)$ exchanges of width-$K$ chunks, because $d\ell=O(p)$, each costing $O(VK^\tau)$ by the arbitrary-width interchange.",
        r"use $O(dK)$ linear scans. Its positional layout uses $O(p/K)$ exchanges"),
      inf("S10.3.4",
        r"The normalized total of the exchanges is $O(p/K)K^\tau=O(pK^{\tau-1})$, whose exponent gap from one is $\epsilon c(1-\tau)$.",
        r"O(p/K)\,K^\tau=O(pK^{\tau-1})."),
     ],
     salient="The smallest margin is a product of three tiny exponents, $\\epsilon=2^{-75}$ for the dimension, $c=2^{-56}$ for the chunk width and $1-\\tau=2^{-50}$ for the interchange exponent, giving $2^{-181}=2\\kappa$."),
   inf("S10.5",
     r"Each of the seven displayed powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually.",
     r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
   inf("S10.6",
     r"Hence the complete bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
     r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})."),
   inf("S10.7",
     r"Below a fixed cutoff, schoolbook multiplication is used, so one fixed machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every $n$.",
     r"Fix one cutoff beyond all the size, precision, margin and layout"),
  ],
  mot_quote="$\\Theta(V)$ stored bits. Table~\\ref{tab:costs} lists costs after division".replace("\\\\","\\"),
  page="cost-accounting",
  frm=["multiplication-algorithm", "address-chunk-interchange", "simultaneous-butterfly-layer", "parameter-regime", "asymptotic-notation-beyond-big-o"])

ROOT = show("S0",
  r"A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in this model.",
  "Reduce multiplication to a convolution computed by Fourier transforms on power-of-two grids, and make the address movement and the butterfly layers cheaper by a power of the logarithm using two tape procedures from fixed linear networks with a rank saving; then choose compatible parameters and add up the costs.",
  "Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $n\\log n$, so savings in both movement and arithmetic are needed.",
  "explicit",
  [S1, S2, S4, S5, S6, S7, S8, S9, S10],
  mot_quote=r"$\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$.",
  page="main-theorem",
  frm=["n-log-n-barrier", "multitape-turing-machine", "big-o-notation", "multiplication-algorithm", "cost-accounting", "subroutines-and-composition-of-algorithms"])

# ---------------- validation ----------------
order = ["n-log-n-barrier","convolution","negacyclic-ring","coefficient-twist","signed-packing","tape-address-model","controlled-cyclic-shift","scratch-restoring-exchange","array-frames","rank-and-orthogonal-subspaces","subset-intersection-labels","address-shear-factorization","rank-saving-recurrence","power-width-interchange","address-chunk-interchange","crt-axis-map","packed-selected-bit-addition","fixed-point-complex-arithmetic","phase-frame-network","discrete-fourier-transform","fft-butterflies","synthetic-polynomial-transform","simultaneous-butterfly-layer","bluestein-chirp","stored-frequency-order","transform-tape-layout","contraction-error-propagation","gaussian-resampling","permutation-cancellation","normalized-ring-convolution","parameter-regime","radix-digit-reduction","tensor-source-transform","precision-exact-recovery","multiplication-algorithm","cost-accounting","main-theorem"]
g = json.load(open(PROJ + "/exegenius/graph.json"))
known = {c["id"] for c in g["concepts"] if c["known"]}
ok = True
ids = set(); pages_used = set(); from_used = set()
cursor = 0
errs = []
def walk(n, eff):
    global cursor
    if n["id"] in ids: errs.append("dup id " + n["id"])
    ids.add(n["id"])
    pg = n.get("page") or eff
    if n.get("page"):
        if n["page"] in pages_used: errs.append("page reused " + n["page"])
        pages_used.add(n["page"])
    for f in n.get("from", []):
        from_used.add(f)
        if f in known: continue
        if f not in order: errs.append("unknown from %s at %s" % (f, n["id"])); continue
        if order.index(f) >= order.index(pg): errs.append("from %s not before page %s at %s" % (f, pg, n["id"]))
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        c = SRC.count(q)
        if c == 0: errs.append("QUOTE NOT FOUND %s: %r" % (n["id"], q))
        elif not n.get("deferred"):
            i = SRC.find(q, cursor)
            if i < 0:
                errs.append("OUT OF ORDER %s: %r (cursor line %d)" % (n["id"], q, SRC.count("\n", 0, cursor)+1))
            else:
                cursor = i + len(q)
        if n.get("children"): errs.append("infer has children " + n["id"])
    else:
        m = n["motivation"]
        if m["source"] == "explicit":
            if not m["quote"] or SRC.count(m["quote"]["quote"]) == 0:
                errs.append("MOTIV QUOTE NOT FOUND %s: %r" % (n["id"], m["quote"]))
        for ch in n["children"]: walk(ch, pg)
        for a in n.get("adds", []):
            # symbol must occur in math of descendant claims
            pass
walk(ROOT, None)
# adds check
def descendants(n):
    for ch in n.get("children", []):
        yield ch
        yield from descendants(ch)
def mathparts(s):
    return re.findall(r"\$(.*?)\$", s, flags=re.S)
def check_adds(n):
    for a in n.get("adds", []):
        sym = a["symbol"]
        found = any(sym in "".join(mathparts(d["claim"])) for d in descendants(n))
        if not found: errs.append("adds symbol %s unused below %s" % (sym, n["id"]))
    for ch in n.get("children", []): check_adds(ch)
check_adds(ROOT)
missing = [p for p in order if p not in pages_used and p not in from_used]
if missing: errs.append("pages neither hosted nor in from: %s" % missing)
if errs:
    print("\n".join(errs)); sys.exit(1)
json.dump({"root": ROOT}, open(PROJ + "/exegenius/tasks/0003-argument.answer.json", "w"), indent=1)
print("ok", len(ids), "nodes")
