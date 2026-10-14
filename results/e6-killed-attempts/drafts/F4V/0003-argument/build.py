import json, sys
base = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F4V"
src = open(base + "/sources/paper.tex").read()
POS = [0]
LOG = []

def Q(sub):
    i = src.find(sub, POS[0])
    if i < 0:
        j = src.find(sub)
        LOG.append(("OUT-OF-ORDER" if j >= 0 else "MISSING", sub[:70], j))
        return {"source": "paper", "quote": sub}
    POS[0] = i + len(sub)
    return {"source": "paper", "quote": sub}

def QM(sub):  # motivation quote: no ordering
    assert sub in src, sub
    return {"source": "paper", "quote": sub}

def B(symbol, name, meaning, rel="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": rel}

def inf(id, claim, quote, frm=None, page=None, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": Q(quote), "from": frm or []}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    return n

def show(id, claim, method, mot, children, page=None, frm=None, adds=None, salient=None):
    # mot = (text, source, quote-or-None)
    text, srcv, quote = mot
    m = {"text": text, "source": srcv, "quote": QM(quote) if quote else None}
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": m,
         "children": children, "from": frm or []}
    if page: n["page"] = page
    if adds: n["adds"] = adds
    if salient: n["salient"] = salient
    return n

# ---------------------------------------------------------------- S1 toolbox
S1 = show("S1",
  r"A small toolbox of tape scans (digit permutations, splits and merges, row dealing, controlled cyclic shifts) costs $O(V)$ on an array of logical volume $V$.",
  "list the elementary linear-time scans that every later procedure is assembled from",
  ("Every later tape procedure is built from these scans, so their cost must be linear in the volume.", "explicit",
   "combinations of intermediate data streams. The present section supplies"),
  [
    inf("S1.1", r"Permuting two radix-$q$ digits, moving a digit, splitting on a digit, applying a pointwise map and merging, and dealing whole rows cyclically to $W$ streams each take $O(V)$ steps.",
        r"volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:"),
    inf("S1.2", r"A controlled cyclic shift $y\mapsto y+a(\text{controls}) \bmod Q$ of a target field that follows its control fields, and multiplication by a fixed unit, take $O(V)$ steps.",
        r"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
        page="controlled-shift",
        frm=["elementary-stream-ops", "modular-arithmetic", "primes-coprimality-and-gcd"]),
  ],
  page="elementary-stream-ops",
  frm=["tape-address-model", "multitape-tm", "sorting-and-data-movement-on-tapes",
       "finite-alphabet-encodings-and-constant-factor-simulation"])

# ---------------------------------------------------------------- S2 procedure 1
S2_1 = show("S2.1",
  r"A fixed linear network of copy, gather, scatter and side-injection gates on $W$ wires exchanges two banks of values with signs, $(X,Y)\mapsto(-Y,X)$, and restores every scratch wire whatever its initial value.",
  "run an eight-row schedule in three stages (forward, inverse, forward), the first rows cancelling the unknown scratch contribution and the last rows restoring it",
  ("The unknown initial scratch values must not leak into the result, so the schedule first subtracts their effect, then adds the source effect, then restores them.", "recoverable", None),
  [
    inf("S2.1.1", r"For arbitrary initial scratch values, one forward invocation changes the target bank by $y_S\mapsto y_S+x_S$ and leaves everything else unchanged.",
        r"Rows 6 and 7 restore $c,a$.  The net target change is"),
    inf("S2.1.2", r"Three stages (forward $X\to Y$, inverse, forward) send $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
        r"$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$."),
  ],
  page="linear-network",
  frm=["finite-field-f2-arithmetic", "permutations-and-cartesian-products", "vectors-matrices-and-invertibility"])

S2_2 = show("S2.2",
  r"If every wire carries an array and every vertex $v$ an invertible frame $D_v$, pointwise linear gates commute with frames, so intermediate frames cancel and a route from input role $w$ to output role $\rho(w)$ applies only $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$.",
  "track the invariant that the stored array is $D_v$ applied to the logical array at each vertex",
  ("A gate acts across wires at one address while a frame acts within one wire's address set, so a common frame commutes with the gate; the invariant therefore survives every gate and only edges pay.", "recoverable", None),
  [
    inf("S2.2.1", r"A linear gate $G$ whose incident arrays all carry the same frame $D_v$ satisfies $G(D_vg_1,\ldots,D_vg_t)=D_vG(g_1,\ldots,g_t)$.",
        r"$c_j\in R$.  Thus the common frame commutes with the pointwise gate, and"),
    inf("S2.2.2", r"Once the scalar routing is fixed, the endpoint frames alone determine the array operator on each route, and the intermediate frames can be chosen to make each edge inexpensive.",
        r"the endpoint frames determine the array operator on each route; the"),
  ],
  page="common-frame-principle",
  frm=["linear-network", "vectors-matrices-and-invertibility", "tape-address-model"],
  salient="The operator applied to a role depends only on its two endpoint frames, however the intermediate frames are chosen, so the interior of the network costs nothing.")

S2_3 = show("S2.3",
  r"Nested nondegenerate subspace labels built from 3-element subsets can be attached to the gates and terminals so that the total rank change $s$ over all edges is less than $Wm$, in both the bit network and the complex network.",
  "attach tensor products of triple-indicator lines whose pairings equal $|S\\cap T|-1$, so gather and scatter coefficients depend on intersection size and side wires cancel the unwanted ones, then count dimension changes edge by edge",
  ("The labels use three-element subsets so that gather and scatter give coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients.", "explicit",
   "on intersection size, and auxiliary wires cancel the unwanted"),
  [
    inf("S2.3.1", r"For triples $S,T$ with indicator vectors $t_S,t_T$ the bilinear pairing is $\langle t_S,t_T\rangle=|S\cap T|-1$, so every triple line is nondegenerate and neighbouring triple lines are orthogonal.",
        r"\langle t_S,t_T\rangle=|S\cap T|-1,"),
    inf("S2.3.2", r"If the decreasing edges lose total dimension $L$, the sum of the absolute dimension changes over all edges is $Wm-2N+2L$.",
        r"dimension $L$, the sum of absolute changes is $Wm-2N+2L$."),
    inf("S2.3.3", r"Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$.",
        r"Every edge joins comparable nondegenerate labels.  The only decreasing"),
    inf("S2.3.4", r"The total decrease $L$ is below half the source dimension $N$ in both constructions.",
        r"In particular, both are smaller than $1/2$.  We now turn the dimension"),
    inf("S2.3.5", r"In the bit network the total rational rank of the edge differences is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.",
        r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$."),
    inf("S2.3.6", r"In the complex network the total number of directional kernels over the edges is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$.",
        r"The deficit is $2N-2L_{\rm c}>0$."),
    inf("S2.3.7", r"With $\tau=1-2^{-50}$ one has $s/W<m^\tau$ for both networks, since the relative deficits exceed $20\cdot 2^{-50}$.",
        r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,"),
  ],
  page="subset-intersection-labels",
  frm=["linear-network", "common-frame-principle", "linear-algebra-basics", "finite-field-f2-arithmetic"])

S2_4 = show("S2.4",
  r"A shear $(H,D)\mapsto(H+AD,D)$ with a rational matrix $A$ of rank $a$ costs exactly $a$ interchanges of pairs of $b$-digit fields plus $O(V)$ further work, and three shears $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ interchange $H$ and $D$.",
  "factor $A=E_1\\Pi E_2$ with lower-triangular $E_1,E_2$ so that only the $a$ ones of the partial permutation $\\Pi$ need interchanges and the triangular parts are linear-time controlled shifts",
  ("Controlled shifts update a later field from earlier ones in linear time, so only lower-triangular changes of coordinates are free.", "explicit",
   "earlier fields in linear time.  Lower triangular changes of coordinates"),
  [
    inf("S2.4.1", r"Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation matrix with exactly $a$ ones.",
        r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization"),
    inf("S2.4.2", r"Each one of $\Pi$ calls for $H_i\leftarrow H_i+D_j$, done by two controlled shifts and one interchange, so the shear uses exactly $a$ interchanges.",
        r"It uses just one interchange.  There are $a$ ones, which proves the"),
  ],
  page="address-shear",
  frm=["controlled-shift", "elementary-stream-ops", "linear-algebra-basics", "modular-arithmetic"])

S2_5 = show("S2.5",
  r"Performing the middle shear through the network, with each edge change done by smaller interchanges on role streams of volume $V/W$ and $s<Wm$, interchanges two chunks of $e=m^k$ digits in $O(Ve^\tau)$ time.",
  "cost recurrence: express the cost per unit volume of a call on $m^k$ digits through $s$ calls on $m^{k-1}$ digits, each on $1/W$ of the volume, and sum the geometric series",
  ("Multiplying the parameter by $m$ multiplies the recursive contribution by $s/W<m$, and this strict inequality is the source of the power saving.", "explicit",
   "increases the recursive contribution by $s/W<m$. This strict inequality"),
  [
    show("S2.5.1",
      r"Splitting rows into $W$ role streams and using the endpoint frames $\Phi_M$ turns the network into the shear $H\leftarrow H+D$ on every original row, scratch rows included.",
      "apply the common-frame identity to address permutations as frames",
      ("Address permutations commute with pointwise bit gates, so the common-frame argument applies and only the edges need work.", "recoverable", None),
      [
        inf("S2.5.1.1", r"Dealing whole rows cyclically into $W$ role streams gives streams of logical volume $V/W$ whose row count is divisible by $W^{k-1}$.",
            r"Split whole rows cyclically into $W$ role streams within each prefix"),
        inf("S2.5.1.2", r"Each role stream has volume $V/W$ and the same remaining shape, so a smaller call on one stream costs $F_{k-1}\cdot V/W$.",
            r"logical volume $V/W$, and its row count is divisible by $W^{k-1}$."),
        inf("S2.5.1.3", r"After the edge shears and the pointwise gates, the result is $H\leftarrow H+D$ on every original row, including scratch rows with arbitrary initial values.",
            r"is $H\leftarrow H+D$ on every original row, including rows assigned"),
      ],
      frm=["common-frame-principle", "linear-network", "address-shear"]),
    inf("S2.5.2", r"The sequence $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ sends $(H,D)$ to $(D,H)$, and only the middle shear uses the network.",
        r"sends $(H,D)$ to $(D,H)$.",
        frm=["address-shear"]),
    show("S2.5.3",
      r"The cost per unit volume satisfies $F_0=O(1)$ and $F_k\le (s/W)F_{k-1}+O(1)$, where $F_k$ bounds time divided by volume for chunks of $m^k$ digits.",
      "count the smaller calls and the cost of the node itself",
      ("Each of the $s$ smaller calls runs on a stream of $1/W$ of the volume, so after dividing by the volume only the factor $s/W$ remains.", "recoverable", None),
      [
        inf("S2.5.3.1", r"The number of smaller calls equals the sum of the edge ranks, which is exactly $s$.",
            r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
        inf("S2.5.3.2", r"Splitting, merging, gates and triangular operations cost $O(V)$ at a node, giving $F_k\le (s/W)F_{k-1}+O(1)$.",
            r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."),
      ]),
    show("S2.5.4",
      r"Because $s/W<m^\tau$ the recurrence solves to $F_k=O(e^\tau)$ with $e=m^k$.",
      "sum the geometric series in the ratio $s/W$ and compare with $m^{k\\tau}$",
      ("The ratio $s/W$ is strictly below $m^\\tau$, so the geometric sum is dominated by its last term and grows like $e^\\tau$, not $e$.", "recoverable", None),
      [
        inf("S2.5.4.1", r"For $a=s/W<m^\tau$ the sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$.",
            r"For $a=s/W<m^\tau$ the geometric sum"),
        inf("S2.5.4.2", r"Hence $F_k=O(e^\tau)$.", r"Hence $F_k=O(e^\tau)$."),
      ]),
    inf("S2.5.5", r"A fixed-tape depth-first schedule parks the inactive role streams on a stack, so that each node moves only $O(V)$ symbols and the $O(V)$ term of the recurrence is honest.",
        r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
  ],
  page="rank-saving-recurrence",
  frm=["address-shear", "common-frame-principle", "subset-intersection-labels", "linear-network",
       "recurrences-and-induction", "elementary-stream-ops"],
  adds=[B("e", "chunk width", "The number of radix-$q$ digits in each of the two chunks, a power $m^k$.", "count"),
        B("F_k", "cost per volume", "A uniform upper bound on running time divided by logical volume for a call on chunks of $m^k$ digits.")],
  salient="The ratio $s/W$ is smaller than $m$ by a relative margin of only about $10^{-11}$, yet this strict inequality alone turns the cost per volume from linear in $e$ into $O(e^\\tau)$ with $\\tau<1$.")

S2_6 = show("S2.6",
  r"Two equal-width chunks of arbitrary width $u$, with arbitrary prefix, gap and suffix, can be interchanged in $O(Vu^\tau)$ steps, by supplying the rows from a few high digits and splitting the remaining width into power-of-$m$ pieces.",
  "borrow the row field from the top digits of the chunks, pad it, and cut the remaining width into $a_j$ pieces of width $m^j$ for the power-width procedure",
  ("The power-width procedure needs a row count divisible by $W^k$ and a width that is a power of $m$, which a general array does not supply.", "recoverable", None),
  [
    inf("S2.6.1", r"Interchanging the top $\rho$ digits of both chunks one pair at a time makes them a row field of range at least $W^k$ before the remaining chunks.",
        r"Write each chunk as its top $\rho$ digits followed by its remaining"),
    inf("S2.6.2", r"The remaining width is written in base $m$ as $e-\rho=\sum_j a_jm^j$ and cut into $a_j$ pieces of width $m^j$.",
        r"Write the remaining width in base $m$:"),
    inf("S2.6.3", r"Applying the power-width procedure to each pair of pieces costs $O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)$.",
        r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)."),
    inf("S2.6.4", r"Binary chunks are padded to the radix $q$ and the padding is scanned away afterwards, giving the bound $O(Vu^\tau)$.",
        r"Finally, for binary chunks let $e$ be the least integer with"),
  ],
  frm=["address-shear", "rank-saving-recurrence", "elementary-stream-ops"])

S2 = show("S2",
  r"Two disjoint contiguous address fields of $u$ bits in an array of volume $V$ can be interchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$.",
  "build the interchange from three address shears, execute the middle shear through a fixed linear exchange network whose edge changes are smaller interchanges, and solve the resulting recursion",
  ("Because the total of the edge ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width.", "explicit",
   "$m$, the resulting recurrence saves a power of the chunk width."),
  [S2_1, S2_2, S2_3, S2_4, S2_5, S2_6],
  page="address-chunk-interchange",
  frm=["tape-address-model", "elementary-stream-ops", "controlled-shift", "linear-algebra-basics", "linear-network",
       "common-frame-principle", "subset-intersection-labels", "address-shear", "rank-saving-recurrence"],
  adds=[B("W", "number of wires", "The number of wires, equivalently roles, of the fixed network, scratch wires included.", "count"),
        B("m", "label dimension", "The dimension of the fixed label space; a chunk is split into $m$ fields at each recursion level.", "count"),
        B("s", "total rank change", "The sum over all network edges of the rank of the edge change, which is the number of smaller calls.", "count")])

# ---------------------------------------------------------------- S3 procedure 2
S3_1 = show("S3.1",
  r"With phase frames built from Hamming-weight phases, each edge change of the complex network is a product of two-point kernels $C=aI+bX$, so a simultaneous $C$-layer on $e=mf$ axes needs $s$ layers on $f$ axes, and $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$.",
  "express each edge's frame change by directional kernels conjugated by a binary change of basis, count one child layer per residual direction, then convert $C$ layers to the normalized butterfly by diagonal phases",
  ("The phase frames express a $C$ tensor product using smaller groups of selected bits separated by binary changes of basis.", "explicit",
   "frames express a $C$ tensor product using smaller groups of"),
  [
    inf("S3.1.1", r"With $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ and $C=H\mathsf SH=aI+bX$ one has $H_0=b\mathsf SC\mathsf S$, $C^2=X$ and $C^4=I$.",
        r"H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad"),
    inf("S3.1.2", r"An edge's frame change is a product of kernels $(aI+bX_{v_j})^{\epsilon_j}$, one for each vector $v_j$ of an orthonormal basis of its residual.",
        r"=\prod_{j=1}^{\rho_{\rm edge}}(aI+bX_{v_j})^{\epsilon_j},"),
    inf("S3.1.3", r"A negative directional kernel still needs only one forward child, because $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$.",
        r"=(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}."),
    inf("S3.1.4", r"Applying the network with these column frames to $e=mf$ axes gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
        r"$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
    inf("S3.1.5", r"The network therefore yields $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary.",
        r"$C^{\otimes e}$ on every role, including roles whose initial scratch"),
    inf("S3.1.6", r"On $D$ selected bits, $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ with $\mathcal S_D$ a diagonal phase operator.",
        r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D."),
  ],
  page="phase-frame-kernel",
  frm=["linear-network", "common-frame-principle", "subset-intersection-labels", "butterfly",
       "linear-algebra-basics", "finite-field-f2-arithmetic", "complex-numbers"],
  adds=[B("e", "axes in a group", "The number of selected axes, a power of $m$, handled by one call of the layer procedure.", "count"),
        B("f", "axes per slot", "The number $e/m$ of axes in each of the $m$ slots of a group.", "count")])

S3_2 = show("S3.2",
  r"A binary row addition $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ on the same bit position of $f$ address chunks of $K$ bits at once, restoring a third chunk $z$ of arbitrary contents, costs $O(V(L^\tau+1))$ with $L=fK$.",
  "eight chunk-wide cyclic shifts that agree with the XORs except on a small explicit set of exceptional addresses, which are then repaired deterministically by sorting",
  ("A constant number of cyclic shifts of whole chunk ranges is followed by a correction of an explicitly bounded set of addresses.", "explicit",
   "of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of"),
  [
    inf("S3.2.1", r"Eight conditional $\pm1$ updates of two integers $u,w$ flip the parity of $u$ exactly when $c=1$ and restore $w$.",
        r"Here $u\bmod2\in\{0,1\}$, also for negative $u$. Thus the parity of $u$"),
    inf("S3.2.2", r"Outside the set of addresses with a small guard value, no segment carries into or borrows from the next, so the packed shifts agree with the independent XORs.",
        r"$[0,2^K-1]$. Inductively, each packed addition therefore agrees with all"),
    inf("S3.2.3", r"The exceptional set $\mathcal B$ has at most a fraction $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$ of the addresses, independently of the payload.",
        r"|\mathcal B|\le\delta_{\rm bad}M."),
    inf("S3.2.4", r"The records at exceptional addresses are extracted with destination keys, stably radix-sorted and reinserted, which implements the exact permutation everywhere.",
        r"while stable binary radix sorting scans only the extracted records and"),
    inf("S3.2.5", r"The movement costs $O(V(L^\tau+1))$ and the correction is negligible when $K/\log p\to\infty$.",
        r"The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans"),
  ],
  page="packed-selected-bit-addition",
  frm=["address-chunk-interchange", "controlled-shift", "elementary-stream-ops",
       "binary-representation-and-bit-operations", "sorting-and-data-movement-on-tapes"],
  salient="The third chunk is restored for every initial value even though the eight updates use it as a parity control for the other chunk.")

S3_3 = show("S3.3",
  r"Batching the layer over $e$ chunks gives a cost per volume $F(e)\le (s/W)F(e/m)+O((eK)^\tau+1)$, hence $O(Vd^{\lambda'})$ for $d$ axes with a fixed $\lambda'<1$.",
  "reuse the rank-saving recursion with the packed basis changes as node overhead, row splitting to supply the roles, and individual kernels at the leaves",
  ("The same strict inequality $s/W<m$ gives a power saving once the extra address work of changing numerical coordinates is shown to be of lower order.", "recoverable", None),
  [
    inf("S3.3.1", r"The first $q_0$ chunks are used as a row index, padded to a multiple of $W^{k_0}$, and a row $u=Wg+w$ is sent to role $w$.",
        r"At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\),"),
    inf("S3.3.2", r"The cost per volume obeys $F(e)\le (s/W)F(e/m)+O((eK)^\tau+1)$ with $F(e)=O(e)$ below $d^\beta$.",
        r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
    inf("S3.3.3", r"At an internal node $K\le e^{c/\beta}$, so the overhead is $O(e^{\lambda})$ and the internal costs sum to $O(e^\lambda)$.",
        r"\(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\)."),
    inf("S3.3.4", r"Adding the base-$m$ pieces of the $d$ axes and the leaves gives total cost $O(d^{\lambda'})$ per unit volume.",
        r"=O(d^{\lambda'})"),
  ],
  frm=["rank-saving-recurrence", "phase-frame-kernel", "packed-selected-bit-addition",
       "address-chunk-interchange", "recurrences-and-induction"])

S3_4 = show("S3.4",
  r"The whole layer is evaluated exactly with $p+O(d^{20})$ fractional bits and one final truncation $Q_p$ leaves a disk array with error below $\sqrt2\,2^{-p}$.",
  "bound denominator and magnitude growth by the arithmetic depth of the recursion, reserve that many guard bits, and truncate once",
  ("The intermediate operators are not contractions, so exactness is bought with guard bits instead of rounding after each step.", "recoverable", None),
  [
    inf("S3.4.1", r"Reserving $p+\Delta$ fractional and $\Delta+3$ integer bits per real component represents every intermediate coefficient exactly.",
        r"Thus reserving \(p+\Delta\)"),
    inf("S3.4.2", r"Choosing $\epsilon C_1<1$ makes $\Delta=o(p)$, so the full coefficient width stays $O(p)$.",
        r"Choose \(\epsilon C_1<1\).  Since \(d=\Theta(p^\epsilon)\),"),
    inf("S3.4.3", r"Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays and truncation toward zero adds error below $\sqrt2\,2^{-p}$.",
        r"absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk"),
  ],
  frm=["fixed-point-truncation", "norms-absolute-values-and-error-bounds", "butterfly"])

S3 = show("S3",
  r"The normalized two-point butterfly $H_0$ can be applied at the same bit offset in $D\le d$ address chunks of a polynomial-record array of volume $V$ in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$, with one final truncation.",
  "evaluate the layer exactly through the phase-frame network, with child layers as recursive calls, packed chunk moves for the binary basis changes, and a single truncation",
  ("Separate butterfly factors would require $D$ whole-array passes, whereas the recursive network costs $O(Vd^{\\lambda'})$.", "explicit",
   "factors would require $D$ whole-array passes."),
  [S3_1, S3_2, S3_3, S3_4],
  page="fast-butterfly-layer",
  frm=["address-chunk-interchange", "packed-selected-bit-addition", "phase-frame-kernel", "rank-saving-recurrence",
       "common-frame-principle", "subset-intersection-labels", "linear-network", "fixed-point-truncation",
       "butterfly", "polynomial-ring-mod", "complex-numbers"])

# ---------------------------------------------------------------- S4 ring convolution
S4_1 = show("S4.1",
  r"Over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ the transform $F_t^-$ with roots $\omega_t=y^{2r/t}$ is computed by radix-two butterfly rounds with monomial twiddles, leaves its output in bit-reversed order, and the opposite transform $F_t^+B_t^{-1}$ consumes that order.",
  "decimation in frequency with twiddles that are signed coefficient shifts, then run the same recursion backwards for the opposite transform",
  ("Powers of $y$ are exact roots of unity that act as signed shifts, so the transform needs no rounding for its twiddles and its output order can be left permuted.", "recoverable", None),
  [
    inf("S4.1.1", r"Character sums satisfy $\sum_{k}\omega_t^{jk}=t$ if $t\mid j$ and $0$ otherwise, so $F_t^+F_t^-=t^{-1}I$ despite zero divisors.",
        r"=\begin{cases}t,&t\mid j,\\0,&t\nmid j.\end{cases}"),
    inf("S4.1.2", r"The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$, applies $H_0$, multiplies the second output by $\omega_t^{-k}$ and recurses on both halves.",
        r"decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for",
        page="butterfly", frm=["dft", "fast-fourier-transform-and-divide-and-conquer"]),
    inf("S4.1.3", r"After all rounds the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$, so the output is stored in bit-reversed order.",
        r"entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$."),
    inf("S4.1.4", r"Running the rounds in reverse implements $F_t^+B_t^{-1}$, which consumes the stored order.",
        r"B_tF_t^-,\qquad F_t^+B_t^{-1},"),
  ],
  page="synthetic-transform",
  frm=["polynomial-ring-mod", "butterfly", "dft", "multidimensional-dft", "roots-of-unity",
       "ring-and-group-notions-for-polynomials", "fast-fourier-transform-and-divide-and-conquer"])

S4_2 = show("S4.2",
  r"A layout permutation $L$ places the selected bits of all axes at common offsets of consecutive $K$-bit chunks, so $LBF^-_{\boldsymbol t}$ and its opposite cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\,\ell\,2^{-p}$.",
  "move a few slots to a prefix, interchange chunks to group equal-index chunks of all axes, then run one fast simultaneous layer per round",
  ("Proposition on the simultaneous layer needs the selected bits of the participating axes at a common offset in consecutive chunks.", "explicit",
   "we must place the selected bits of the participating axes at a common"),
  [
    inf("S4.2.1", r"Moving the at most $d(b+1)$ listed slots to a prefix costs $O(TpdK)$.",
        r"listed slots, so the moves cost $O(TpdK)$."),
    inf("S4.2.2", r"Grouping equal-index chunks takes at most $dq$ width-$K$ chunk exchanges costing $O(Tp\cdot pK^{\tau-1})$.",
        r"=O\bigl(Tp\,pK^{\tau-1}\bigr)."),
    inf("S4.2.3", r"Each round on the remaining chunks is one fast simultaneous layer, costing $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.",
        r"$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total."),
    inf("S4.2.4", r"The at most $K$ rounds on prefix slots are done bit by bit at cost $O(TpdK)$.",
        r"most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$."),
    inf("S4.2.5", r"Starting with zero error, each of the at most $\ell$ rounds adds less than $\sqrt2\,2^{-p}$ and preserves the disk, giving the stated error.",
        r"Both the contraction and truncation preserve the disk.  Starting with"),
  ],
  frm=["fast-butterfly-layer", "address-chunk-interchange", "synthetic-transform",
       "fixed-point-truncation", "multidimensional-dft"])

S4_3 = show("S4.3",
  r"For disk-grid $f,g\in\mathcal R_r$ the exact product $fg$ and then $Q_p(fg/r)$ are computed with four integer multiplications of $O(rp)$-bit numbers in time $O(rp\log(rp))$.",
  "signed Kronecker substitution: evaluate the integer coefficients at $B_0=2^{4p}$, multiply with the established multiplier and read the coefficients back by centred residues and carries",
  ("The ring product is a polynomial product, which the established integer multiplier computes once the coefficients are packed into one integer.", "recoverable", None),
  [
    inf("S4.3.1", r"Each polynomial is packed into the signed evaluation integer $A_u=u(B_0)$ with $B_0=2^{4p}$.",
        r"coefficients of absolute value at most $2^p$.  Set $B_0=2^{4p}$"),
    inf("S4.3.2", r"Every coefficient of a product satisfies $|h_j|\le r2^{2p}<B_0/2$, so a centred residue modulo $B_0$ identifies it.",
        r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
    inf("S4.3.3", r"Block by block, the unique centred representative of $q_j+\rho_j$ modulo $B_0$ is the coefficient $h_j$ and the carry stays in $\{0,1\}$.",
        r"At block $j$, let $\widehat h_j$ be the unique"),
    inf("S4.3.4", r"Each reduced coefficient is a sum of exactly $r$ signed products of Gaussian integers of modulus at most $2^p$, so $|H_j|\le r2^{2p}$.",
        r"resulting Gaussian integer coefficient $H_j$ is a sum of exactly"),
    inf("S4.3.5", r"The four exact integer products dominate the cost, which is $O(rp\log(rp))$.",
        r"Four exact integer products dominate the linear"),
  ],
  page="signed-packing",
  frm=["established-multiplier", "polynomial-ring-mod", "fixed-point-truncation", "binary-representation-and-bit-operations"])

S4_4 = show("S4.4",
  r"Two forward transforms in the same retained order, pointwise products divided by $r$, the opposite transform and an exact multiplication by $M$ compute $\mathcal M_r(f,g)=f*g/T$ with error below $\sqrt2\,M(3\ell+1)2^{-p}$.",
  "use the convolution theorem for the transforms, commute the pointwise product with the retained permutation, and add up the errors with contraction bounds",
  ("Pointwise multiplication commutes with the same record permutation applied to both operands, so the permuted frequency order can be passed straight to the opposite transform.", "explicit",
   "permutation $LB$ to both operands.  We may therefore multiply the"),
  [
    inf("S4.4.1", r"Expanding the finite sums gives $F_{\boldsymbol t}^-(f*g)=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)$, so with $F^+F^-=I/M$ one gets $f*g/(rM)$.",
        r"=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)."),
    inf("S4.4.2", r"Since $LB$ permutes records and leaves their polynomial suffixes intact, the pointwise product of stored forward outputs is the stored image of the product.",
        r"Since $LB$ permutes records and leaves their polynomial suffixes"),
    inf("S4.4.3", r"The three transform errors and the product truncation, multiplied by $M$, give error less than $\sqrt2\,M(3\ell+1)2^{-p}$.",
        r"$M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed."),
    inf("S4.4.4", r"There are $M=T/r$ pointwise products costing $O(Tp\log(rp))$ in total, which adds the last term of the cost.",
        r"There are $M=T/r$ pointwise polynomial products.  Their total cost"),
  ],
  frm=["dft", "multidimensional-dft", "cyclic-convolution", "synthetic-transform", "signed-packing",
       "norms-absolute-values-and-error-bounds"])

S4 = show("S4",
  r"Normalized convolution $\mathcal M_r(f,g)=f*g/T$ on $d-1$ axes of arrays over $\mathbb C[y]/(y^r+1)$ is approximated with error $<\sqrt2\,M(3\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.",
  "two forward synthetic transforms that keep the same frequency order, pointwise polynomial products by signed packing, then the opposite transform, all on the fast layers and chunk exchanges",
  ("A ring with an exact root of unity turns each transform round into cheap butterflies and signed shifts, and these rounds are exactly the layers that the tape procedures accelerate.", "reconstructed", None),
  [S4_1, S4_2, S4_3, S4_4],
  page="ring-convolution",
  frm=["cyclic-convolution", "dft", "multidimensional-dft", "synthetic-transform", "signed-packing",
       "fast-butterfly-layer", "address-chunk-interchange", "polynomial-ring-mod",
       "fixed-point-truncation", "established-multiplier"],
  adds=[B("M", "number of records", "The number $T/r$ of polynomial records, equal to the product of the first $d-1$ axis lengths.", "count"),
        B(r"\ell", "log record length", r"The base-2 logarithm of $r$, which is also the number of rounds on a long axis.")])

# ---------------------------------------------------------------- S5 resampling
S5 = show("S5",
  r"For coprime $s<t$ with $t/s-1>p/\alpha^4$ there are linear contractions $A,B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computed in $O(tp^{3/2+\delta}\alpha)$ per line, and the tensor version $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ costs $O(dTp^{3/2+\delta}\alpha)$ plus $O(Tpd^2(1+\ell^\tau))$ axis moves.",
  "Gaussian resampling of Harvey and van der Hoeven: relate a transform of length $s$ to a power-of-two transform of length $t$ through Gaussian-weighted contractions, invert a near-identity by a Neumann series, and apply line by line, leaving both coordinate permutations inside the formula",
  ("The transform lengths needed for the product are pairwise coprime whereas the synthetic transforms need powers of two, and Gaussian resampling connects these two shapes.", "explicit",
   "whereas the synthetic transforms use powers of two. Gaussian resampling"),
  [
    inf("S5.1", r"The Gaussian maps $\mathsf S,\mathsf T$ satisfy $\mathsf TP_sF_s=P_tF_t\mathsf S$, and the near-identity $N=C\mathsf T\mathsf D$ has $\|N-I\|<2^{-\alpha^2\theta}$.",
        r"\mathsf T P_sF_s=P_tF_t\mathsf S,"),
    inf("S5.2", r"Since $\|N-I\|<1/2$, $N$ is invertible by the Neumann series.",
        r"by the Neumann series. Put"),
    inf("S5.3", r"With $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$ the normalizations multiply to $2^{-2\alpha^2}$, giving $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ with both maps contractions.",
        r"$2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$. Hence"),
    inf("S5.4", r"Ordered algorithms for $A$ and $B_0$ have error below $p^2$ and cost $O(tp^{3/2+\delta}\alpha)$, with the two coordinate permutations not executed.",
        r"$4+3p^2/4<p^2$, respectively. The costs add to the claimed bound."),
    inf("S5.5", r"Tensoring over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$.",
        r"=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A,"),
    inf("S5.6", r"Composing the $d$ axis maps gives error less than $dp^2$.",
        r"Composing the $d$ axis maps gives error less than $dp^2$."),
    inf("S5.7", r"At most $T/t_i$ lines are processed on axis $i$, for total cost $O(dTp^{3/2+\delta}\alpha)$.",
        r"=O(dTp^{3/2+\delta}\alpha)."),
    inf("S5.8", r"Exposing and restoring one axis by adjacent chunk interchanges costs $O(Tp(1+\ell^\tau))$ each, $O(d)$ of them per axis.",
        r"costs $O(Tp(1+\ell^\tau))$. Exposing and restoring one axis needs"),
  ],
  page="gaussian-resampling",
  frm=["dft", "multidimensional-dft", "fixed-point-truncation", "established-multiplier", "address-chunk-interchange",
       "elementary-stream-ops", "norms-absolute-values-and-error-bounds", "permutations-and-cartesian-products"],
  adds=[B("s", "source length", "The length of the source transform, a prime, on one axis.", "count"),
        B("t", "padded length", "The length of the power-of-two transform that replaces it, larger than $s$.", "count"),
        B(r"\alpha", "Gaussian width", "The width parameter of the Gaussian weights."),
        B(r"\gamma", "total scale exponent", r"The exponent $2d\alpha^2$ of the power of two by which the tensor identity is scaled.")])

# ---------------------------------------------------------------- S6 chirp
S6 = show("S6",
  r"For even $t_i$ and the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$, the permuted transform is a chirp-weighted normalized cyclic convolution, $QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$.",
  "expand the coefficient of $u_{\\boldsymbol k}$ on the right-hand side and match it with the entry of $QF_{\\boldsymbol t}$",
  ("The exponent of a chirp difference expands into two squares and a cross term, and the cross term is exactly the Fourier kernel.", "reconstructed", None),
  [
    inf("S6.1", r"The chirp $a$ has period $t_i$ in coordinate $i$, because shifting $j_i$ by $t_i$ changes the exponent by an integral multiple of $2\pi i$.",
        r"Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by"),
    inf("S6.2", r"The coefficient of $u_{\boldsymbol k}$ on the right is $T^{-1}\exp(2\pi i\sum_i s_ij_ik_i/t_i)$, which is the coefficient in $QF_{\boldsymbol t}$.",
        r"This is precisely the coefficient in $QF_{\boldsymbol t}$, because"),
  ],
  page="bluestein-chirp",
  frm=["dft", "multidimensional-dft", "cyclic-convolution", "roots-of-unity", "modular-arithmetic"])

# ---------------------------------------------------------------- S7 cancellation
S7 = show("S7",
  r"The retained source permutation $R$ cancels: $(RF_{\boldsymbol s}^+)\bigl[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)\bigr]=(u*v)/S^2$.",
  "show $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$ by substituting $h=ck$ in the Fourier sum, then apply the convolution rule to the unpermuted transforms",
  ("The permutation never needs to be executed, because it commutes through the pointwise product and meets its inverse in the opposite transform.", "explicit",
   "retained source permutation $R$ cancels when computing a convolution."),
  [
    inf("S7.1", r"For a unit $c$ modulo $q$ and $(R_cz)_j=z_{cj}$, substituting $h=ck$ gives $F_q^+R_cz=R_c^{-1}F_q^+z$.",
        r"=(R_c^{-1}F_q^+z)_j."),
    inf("S7.2", r"Tensoring, $F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$, hence $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.",
        r"$F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence"),
    inf("S7.3", r"A coordinate permutation commutes with pointwise products, so $(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)=R(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)$.",
        r"because a coordinate permutation commutes with pointwise products."),
    inf("S7.4", r"The convolution rule $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)(F_{\boldsymbol s}v)$ and $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$ give $F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=(u*v)/S^2$.",
        r"=\frac{u*v}{S^2}."),
  ],
  page="permutation-cancellation",
  frm=["dft", "multidimensional-dft", "gaussian-resampling", "cyclic-convolution",
       "permutations-and-cartesian-products", "modular-arithmetic"],
  salient="The permutation $R$ of Gaussian resampling is never executed as a sort: it commutes with pointwise products and cancels against its twin in the opposite-sign transform.")

# ---------------------------------------------------------------- S8 algorithm
S8_1 = show("S8.1",
  r"With $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^{\epsilon}\rfloor$, $K=\lfloor d^c\rfloor$, padded size $T\in[4n/b,8n/b)$, axis lengths $t_i\in\{r/2,r\}$ and distinct odd primes $s_i$ just below $t_i$, one has $Tp=\Theta(n)$, $T/2<S<T$ and every hypothesis of the resampling lemma.",
  "fix explicit rational exponents, choose the sizes from $n$, and check by a prime-interval estimate that enough primes lie just below each $t_i$",
  ("The prime lengths must be close to the powers of two, so that their product fills a fixed fraction of the padded box, while each ratio $t_i/s_i$ leaves enough separation for resampling.", "explicit",
   "$t_i$: their product must occupy a fixed fraction of the padded box,"),
  [
    inf("S8.1.1", r"The exponents are fixed rationals: $\tau=1-2^{-50}$, $\delta=1/16$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\epsilon=2^{-75}$, $\kappa=2^{-182}$.",
        r"\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\"),
    inf("S8.1.2", r"The sizes are $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $K=\lfloor d^c\rfloor$.",
        r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,"),
    inf("S8.1.3", r"These choices give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$.",
        r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad"),
    inf("S8.1.4", r"Distinct odd primes exist with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ and $\eta=1/(4d)$.",
        r"(1-2\eta)t_i<s_i\leq(1-\eta)t_i."),
    inf("S8.1.5", r"Strict Bernoulli gives $S/T>1/2$, hence $T/2<S<T$.",
        r"Together with $s_i<t_i$, this gives $T/2<S<T$."),
    inf("S8.1.6", r"Hence $\alpha^4\theta_i>p$ for every axis, so the hypotheses of the Gaussian resampling lemma hold.",
        r"\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p."),
  ],
  page="parameter-choice",
  frm=["gaussian-resampling", "ring-convolution", "fast-butterfly-layer", "primes-coprimality-and-gcd",
       "logarithms-and-iterated-logarithm-notation", "floor-ceiling-and-summation-notation"],
  salient=None)

S8_2 = show("S8.2",
  r"Writing each input as a polynomial in $2^b$ with $q=\lceil n/b\rceil$ digits, the product has degree below $S$, so convolution modulo $x^S-1$ has no wraparound, and its coefficients are below $2^{3b}$.",
  "multiply the digit polynomials and bound degree and coefficient size",
  ("An integer is its radix polynomial evaluated at $2^b$, so the product is the polynomial product followed by carries, provided the cyclic length leaves no wraparound.", "recoverable", None),
  [
    inf("S8.2.1", r"The product degree satisfies $2q-2<2n/b\le T/2<S$.",
        r"2q-2<2n/b\le T/2<S."),
    inf("S8.2.2", r"Every product coefficient obeys $0\le c_j\le q(2^b-1)^2<2^{3b}$.",
        r"0\le c_j\le q(2^b-1)^2<2^{3b},"),
  ],
  page="radix-digit-convolution",
  frm=["cyclic-convolution", "polynomials", "binary-representation-and-bit-operations", "floor-ceiling-and-summation-notation"],
  adds=None)

S8_3 = show("S8.3",
  r"The Chinese-remainder map $\Phi:\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\ldots,x_d]/(x_i^{s_i}-1)$, $x\mapsto\prod_ix_i^{\mu_i}$, is an isomorphism preserving cyclic convolution, and it and its padding cost $O(Tpd^2(1+\ell^\tau))$ on tape.",
  "use pairwise coprimality for the isomorphism, make its coordinates triangular in the physical axis order, and perform them as prefix-controlled cyclic shifts after reordering axes by chunk interchanges",
  ("The triangular form lets every coordinate update be a controlled shift whose controls precede its target, which costs only linear time.", "recoverable", None),
  [
    inf("S8.3.1", r"The assignment $x\mapsto\prod_ix_i^{\mu_i}$ respects $x^S=1$ and the images of powers of $x$ run through all monomials once.",
        r"\qquad x\longmapsto\prod_i x_i^{\mu_i}"),
    inf("S8.3.2", r"Hence $\Phi$ is an isomorphism and preserves cyclic convolution.",
        r"$\Phi$ is an isomorphism and preserves cyclic convolution."),
    inf("S8.3.3", r"The coordinate in axis $i$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j \pmod{s_i}$, depending only on lower-index digits.",
        r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}."),
    inf("S8.3.4", r"Each triangular update is a prefix-controlled cyclic shift of the valid interval, costing linear time.",
        r"Each triangular update is a prefix-controlled cyclic shift.  The"),
    inf("S8.3.5", r"Reversing the axes uses $O(d^2)$ adjacent interchanges, so $\Phi$ with padding costs $O(Tpd^2(1+\ell^\tau))$.",
        r"O\bigl(Tp\,d^2(1+\ell^\tau)\bigr)."),
  ],
  page="crt-address-map",
  frm=["cyclic-convolution", "chinese-remainder-theorem", "controlled-shift", "address-chunk-interchange",
       "primes-coprimality-and-gcd", "ring-and-group-notions-for-polynomials"])

S8_4 = show("S8.4",
  r"The coefficient twist $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ is an isomorphism $\mathbb C[x_d]/(x_d^r-1)\to\mathbb C[y]/(y^r+1)$, and untwisting turns the negative wrap into the original cyclic wrap.",
  "check that the map is well defined and diagonal on the monomial bases, then verify the wrap factor on a product term",
  ("A cyclic coordinate cannot carry a signed-shift root of unity, so it is converted to the ring modulo $y^r+1$ by a diagonal rescaling that is exactly undone afterwards.", "reconstructed", None),
  [
    inf("S8.4.1", r"The map is well defined since $(\zeta y)^r=(-1)(-1)=1$, and diagonal in the bases, multiplying coefficient $k$ by $\zeta^k$.",
        r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$.  On the bases"),
    inf("S8.4.2", r"A product term with $k+l=j+hr$ has twisted factor $\zeta^{k+l}(-1)^h=\zeta^j$.",
        r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j."),
    inf("S8.4.3", r"Untwisting therefore recovers the cyclic coefficient with the correct sign.",
        r"Untwisting therefore recovers the cyclic coefficient with the correct"),
  ],
  page="phase-twist",
  frm=["polynomial-ring-mod", "cyclic-convolution", "roots-of-unity"])

S8_5 = inf("S8.5",
  r"Normalized complex cyclic convolution on all $d$ axes is $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=f*g/T$.",
  r"=\frac{f*g}{T}.",
  frm=["phase-twist", "ring-convolution", "cyclic-convolution"])

S8_6 = show("S8.6",
  r"The chirp transform $\widetilde{\mathscr C}$ approximates $QF_{\boldsymbol t}$ by a chirped complex convolution, and the source transform $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ equals $RF_{\boldsymbol s}$.",
  "form the chirp-weighted convolution from the twisted ring convolution and sandwich it between the two Gaussian maps",
  ("The permuted power-of-two transform is a chirped convolution, so each source transform reduces to the ring convolution already built.", "recoverable", None),
  [
    inf("S8.6.1", r"With exact phases and exact convolution the chirp procedure gives $\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)=QF_{\boldsymbol t}x$.",
        r"by exact phases and exact convolution gives"),
    inf("S8.6.2", r"The source transform applies $\mathcal A$, the chirp transform, $\mathcal B_0$ and the scale $2^\gamma$, with exact counterpart $RF_{\boldsymbol s}$.",
        r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A"),
  ],
  frm=["bluestein-chirp", "gaussian-resampling", "permutation-cancellation", "ring-convolution", "fixed-point-truncation"])

S8_7 = show("S8.7",
  r"The pipeline forms the radix digits, applies $\Phi$, runs two source transforms, multiplies pointwise, runs the opposite-sign source transform, rescales by $S$ and $2^{2b+4}$, rounds, undoes $\Phi$ and propagates carries.",
  "compose the preceding reductions in order",
  ("Each stage is one of the procedures already built, so the algorithm is their composition with the right rescalings.", "recoverable", None),
  [
    inf("S8.7.1", r"Radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ are written as scaled grid values and padded with $S-q$ zero records.",
        r"Append $S-q$ zero coefficient records."),
    inf("S8.7.2", r"Apply the coefficient-address map $\Phi$ with its padded layout to obtain the source arrays $u,v$.",
        r"\item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain"),
    inf("S8.7.3", r"Compute the source transforms $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.",
        r"\item Compute $\widetilde{\mathscr F}(u)$ and"),
    inf("S8.7.4", r"Multiply corresponding complex coefficients exactly and truncate to $p$ fractional bits to get $z$.",
        r"\item Multiply corresponding complex coefficients exactly and truncate"),
    inf("S8.7.5", r"Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its numerators by $S$.",
        r"\item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid"),
    inf("S8.7.6", r"Multiply by $2^{2b+4}S$, round to the nearest integers, undo $\Phi$ and remove the padding.",
        r"\item Multiply the grid numerators of $\widetilde w$ exactly by"),
    inf("S8.7.7", r"Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits.",
        r"\item Propagate radix-$2^b$ carries in increasing coefficient order."),
  ],
  frm=["crt-address-map", "radix-digit-convolution", "permutation-cancellation", "fixed-point-truncation", "established-multiplier"])

S8 = show("S8",
  r"With the fixed parameters, the algorithm forming radix digits, applying $\Phi$, running two source transforms, a pointwise product and an opposite-sign transform, rescaling, rounding and carrying outputs the exact $2n$-bit product.",
  "reduce the product to a cyclic convolution of radix digits, move it to prime axes by the Chinese-remainder map, trade the prime-length transforms for power-of-two ones by resampling and chirps, and finish with the ring convolution",
  ("We choose compatible parameters for the procedures, recover the integer coefficients from their approximations, and account for the remaining tape operations.", "explicit",
   "exact.  We choose compatible parameters for these procedures, recover"),
  [S8_1, S8_2, S8_3, S8_4, S8_5, S8_6, S8_7],
  page="multiplication-algorithm",
  frm=["cyclic-convolution", "radix-digit-convolution", "crt-address-map", "phase-twist", "parameter-choice",
       "gaussian-resampling", "bluestein-chirp", "permutation-cancellation", "ring-convolution", "exact-recovery",
       "fixed-point-truncation"],
  adds=[B("b", "digit width", r"The radix exponent $\lceil\log_2 n\rceil$: the number of bits in each radix digit."),
        B("q", "digit count", r"The number $\lceil n/b\rceil$ of radix-$2^b$ digits in each input.", "count"),
        B("S", "cyclic length", r"The product $s_1\cdots s_d$ of the distinct prime axis lengths, the length of the cyclic convolution.", "count")])

# ---------------------------------------------------------------- S9 recovery
S9_2 = show("S9.2",
  r"The computed coefficients $\widetilde w$ approximate $w=(u*v)/S$ with error below $E_wh_p$ where $E_w<28\cdot2^\gamma T^2L$, and the final scaled error is below $448b\,2^{-3b/4}<1/2$.",
  "insert the exact contraction at each computed input in turn, add the errors with the bilinear contraction bound, and multiply by the exact scales",
  ("A contraction does not increase the error of its input, so the errors of the successive stages add and only the final exact rescalings amplify them.", "recoverable", None),
  [
    inf("S9.2.1", r"A source transform has error below $E_sh_p$ with $E_s=9\cdot 2^\gamma TL$.",
        r"E_s=9\,2^\gamma TL,"),
    inf("S9.2.2", r"The pointwise product satisfies $\|z-U\cdot V_1\|<(2E_s+2)h_p$.",
        r"Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$."),
    inf("S9.2.3", r"The opposite transform adds error: $\|\widetilde{\mathscr F}^{+}(z)-G(U\cdot V_1)\|<(3E_s+2)h_p$.",
        r"<(3E_s+2)h_p."),
    inf("S9.2.4", r"After the first scale by $S$ the error is below $E_wh_p$ with $E_w:=S(3E_s+2)<28\cdot2^\gamma T^2L$.",
        r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
    inf("S9.2.5", r"After the second scale $2^{2b+4}S$ the absolute error on the integer coefficients is below $448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<1/2$.",
        r"<448b\,2^{-b+\gamma}"),
  ],
  frm=["norms-absolute-values-and-error-bounds", "fixed-point-truncation"],
  adds=[B("E_s", "source error", r"The bound, in units of $h_p$, on the error of a computed source transform."),
        B("h_p", "grid spacing", r"The spacing $2^{-p}$ of the fixed-point grid.")])

S9_4 = show("S9.4",
  r"Radix-$2^b$ carry propagation, with carries $k_j<Q_0^2$, turns the coefficients $c_j$ into the exact digits of the product.",
  "an invariant on the processed prefix of the coefficient sum",
  ("The integer coefficients exceed one digit but only by a bounded carry, which a left-to-right scan with the invariant that processed digits are final can resolve.", "recoverable", None),
  [
    inf("S9.4.1", r"The recurrence $d_j=(c_j+k_j)\bmod Q_0$, $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$ keeps the carries within $0\le k_j<Q_0^2$.",
        r"k_{j+1}=\left\lfloor\frac{c_j+k_j}{Q_0}\right\rfloor."),
    inf("S9.4.2", r"The invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ shows the first $j$ digits are final.",
        r"=\sum_{h<j}d_hQ_0^h+k_jQ_0^j."),
  ],
  frm=["radix-digit-convolution"])

S9 = show("S9",
  r"The error in the recovered coefficients is below $1/2$, so rounding gives the exact integer coefficients and carry propagation yields the exact $2n$-bit product.",
  "propagate approximation errors through the pipeline with contraction bounds, check the disk margins, undo the known scalings $S$ and $2^{2b+4}$, then round and carry",
  ("The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$.", "explicit",
   "disk bounds needed by every call and proves that the final error is"),
  [
    inf("S9.1", r"The two occurrences of $S$ undo different normalizations: the exact counterpart after three transforms is $(u*v)/S^2$, and the second scale restores the integer convolution.",
        r"The two occurrences of $S$ in this algorithm undo different"),
    S9_2,
    inf("S9.3", r"Because the true coefficients are integers and the error is strictly below $1/2$, the nearest integer is the unique correct coefficient.",
        r"$H_j/2^p$.  The strict error below $1/2$ makes the nearest integer to"),
    S9_4,
  ],
  page="exact-recovery",
  frm=["radix-digit-convolution", "cyclic-convolution", "fixed-point-truncation",
       "norms-absolute-values-and-error-bounds", "floor-ceiling-and-summation-notation"])

# ---------------------------------------------------------------- S10 accounting
S10_1 = show("S10.1",
  r"Dividing by $V=Tp$, seven stages dominate, with normalized costs $dK$, $pK^{\tau-1}$, $\ell d^{\lambda'}$, $d^2(1+\ell^\tau)$, $dp^{1/2+\delta}\alpha$, $dp^\delta$ and $\log(rp)$.",
  "tabulate each stage's cost from its own lemma, divided by the volume",
  ("Dividing every cost by the common volume $V$ lets each stage be compared by the power of $p$ it contributes.", "recoverable", None),
  [
    inf("S10.1.1", r"Prefix-slot moves and individual butterfly rounds cost $dK$ per unit volume, a power $\epsilon(1+c)$ of $p$.",
        r"Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\"),
    inf("S10.1.2", r"Chunk exchanges for the transform layout cost $pK^{\tau-1}$, a power $1-\epsilon c(1-\tau)$.",
        r"Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\"),
    inf("S10.1.3", r"Simultaneous butterfly rounds cost $\ell d^{\lambda'}$, a power $1-\epsilon(1-\lambda')$.",
        r"Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\"),
    inf("S10.1.4", r"CRT and axis layouts cost $d^2(1+\ell^\tau)$, a power $\tau+\epsilon(2-\tau)$.",
        r"CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\"),
    inf("S10.1.5", r"Gaussian line maps cost $dp^{1/2+\delta}\alpha$, a power $3/4+\delta+3\epsilon/2$.",
        r"Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\"),
    inf("S10.1.6", r"Chirps, twists and scalar products cost $dp^\delta$, a power $\epsilon+\delta$.",
        r"Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\"),
    inf("S10.1.7", r"Packed polynomial products cost $\log(rp)$, a power $1-\epsilon$.",
        r"Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\"),
  ],
  frm=["fast-butterfly-layer", "address-chunk-interchange", "ring-convolution", "gaussian-resampling",
       "crt-address-map", "multiplication-algorithm"],
  adds=None)

S10_2 = show("S10.2",
  r"Each of the seven powers of $p$ is at most $1-2\kappa$ with $\kappa=2^{-182}$, so the total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
  "compute the margins $g_i$ below one for the seven powers and take their minimum",
  ("The margins below one are explicit rationals, so the smallest one gives a concrete $\\kappa$ with room to absorb any fixed power of $\\log p$.", "recoverable", None),
  [
    inf("S10.2.1", r"The margins satisfy $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$.",
        r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad"),
    inf("S10.2.2", r"The smallest margin is $\min_ig_i=2^{-181}=2\kappa$, which leaves slack to absorb any fixed power of $\log p$.",
        r"Thus $\min_i g_i=2^{-181}=2\kappa$.  This explicit slack will cover"),
    inf("S10.2.3", r"Setup, prime search and exceptional-address repair cost $o(V)$.",
        r"alphabet symbols.  Global setup and prime search cost $o(V)$, as"),
    inf("S10.2.4", r"Each of the seven displayed powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually.",
        r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
    inf("S10.2.5", r"The complete large-input bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
        r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})."),
    inf("S10.2.6", r"Below a fixed cutoff schoolbook multiplication is used, absorbed into the implicit constant, giving one machine for every $n$.",
        r"conditions, and use schoolbook multiplication below it.  The finitely"),
  ],
  frm=["logarithms-and-iterated-logarithm-notation", "big-omega-theta-and-little-o-notation"])

S10 = show("S10",
  r"Dividing every cost by $V=Tp=\Theta(n)$ gives seven dominant powers of $p$, each at most $1-2\kappa$ with $\kappa=2^{-182}$, so the total time is $O(n(\lg n)^{1-\kappa})$.",
  "tabulate the normalized cost of every stage, then compare each power of $p$ with $1-2\\kappa$",
  ("Normalizing by the common volume turns the many costs into a table of powers of $p$ that can be compared with one threshold.", "recoverable", None),
  [S10_1, S10_2],
  page="time-accounting",
  frm=["fast-butterfly-layer", "address-chunk-interchange", "ring-convolution", "gaussian-resampling",
       "crt-address-map", "parameter-choice", "multiplication-algorithm", "exact-recovery",
       "logarithms-and-iterated-logarithm-notation", "big-omega-theta-and-little-o-notation"],
  adds=[B("V", "logical volume", r"The number $Tp$ of stored bits of the padded array, which is $\Theta(n)$.", "count")],
  salient="The saving $\\kappa=2^{-182}$ is astronomically small: it is half the smallest margin $g_2=\\epsilon c(1-\\tau)=2^{-181}$, a product of the tiny exponents $\\epsilon=2^{-75}$, $c=2^{-56}$ and $1-\\tau=2^{-50}$.")

# ---------------------------------------------------------------- root
ROOT = show("S0",
  r"A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture.",
  "reduce multiplication to a convolution, compute that convolution with Fourier-type transforms whose address movement and butterfly layers are accelerated by two recursive tape procedures that save a power of the logarithm, recover the exact product, and add up the costs",
  ("Scanning an array of size $n$ at each of $\\log n$ transform levels costs $n\\log n$ already, so savings are needed in both data movement and arithmetic, which the two tape procedures supply.", "explicit",
   r"$\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$."),
  [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10],
  page="main-theorem",
  frm=["integer-multiplication-conjecture", "multiplication-algorithm", "time-accounting", "multitape-tm", "big-o"],
  adds=[B("p", "working precision", "The number of fractional bits kept in each real or imaginary component of the stored complex values.", "count"),
        B("d", "number of axes", "The number of axes of the multidimensional transform and of address chunks per layer.", "count"),
        B("K", "chunk width", "The number of address bits in each chunk selected by a butterfly layer.", "count"),
        B("T", "padded size", "The number of entries of the padded power-of-two box on which the transforms act.", "count"),
        B("r", "record length", "The number of complex coefficients in a polynomial record modulo $y^r+1$.", "count")])

json.dump({"root": ROOT}, open(base + "/exegenius/tasks/0003-argument.answer.json", "w"), indent=1)
for l in LOG:
    print(l)
print("done")
