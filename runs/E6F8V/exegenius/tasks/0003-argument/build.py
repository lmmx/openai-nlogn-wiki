import json, sys

SRC = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F8V/sources/paper.tex').read()

def ev(q):
    return {"source": "paper", "quote": q}

def mot(text, source, quote=None):
    d = {"text": text, "source": source}
    if quote:
        d["quote"] = ev(quote)
    return d

def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

def show(id, claim, method, motivation, children, page=None, frm=None, salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children}
    if page: n["page"] = page
    if frm: n["from"] = frm
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n

def infer(id, claim, quote, page=None, frm=None, salient=None, deferred=False):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote)}
    if page: n["page"] = page
    if frm: n["from"] = frm
    if salient: n["salient"] = salient
    if deferred: n["deferred"] = True
    return n

# ---------------------------------------------------------------- A0
A0_1 = infer("A0.1",
    "Fixed digit permutations, digit moves, splits on a digit and cyclic row splits of an array of logical volume $V$ stored in lexicographic order each take $O(V)$ steps on a fixed number of tapes.",
    r"volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
    page="tape-address-model",
    frm=["multitape-turing-machine", "multidimensional-arrays-and-row-major-order", "positional-notation-in-any-radix", "big-o-notation"])

A0_2 = show("A0.2",
    "Adding to a target address field $y\\in[Q]$ an offset computed from earlier control fields, modulo $Q=q^b$, costs $O(V)$ although the fields may be arbitrarily long.",
    "Treat each fiber of $Q$ blocks as a list: split it at $Q-a$ into two pieces and merge them in the opposite order, which is a cyclic rotation of the blocks.",
    mot("A cyclic shift of the target coordinate by $a$ is just moving the last $a$ blocks of the fiber in front of the first $Q-a$ blocks, which is one split and one reordered merge on tapes.", "recoverable"),
    [
        infer("A0.2.1", "For each prefix fiber, split its $Q$ consecutive blocks at $Q-a$ and append the two pieces to two tapes.",
              r"For an offset $a\in[Q]$, split these blocks at $Q-a$."),
        infer("A0.2.2", "Merging by reading the second piece and then the first piece gives the shifted coordinate in one more pass, so only the offset computation $b^{O(1)}=O(Q)$ remains, absorbed by the fiber.",
              r"merge read the second piece and then the first piece for each prefix."),
    ],
    page="controlled-cyclic-shift",
    frm=["tape-address-model", "modular-arithmetic", "cyclic-shifts-and-rotations-of-lists"])

A0 = show("A0",
    "The elementary tape operations that every later procedure calls cost $O(V)$ in the logical volume $V$.",
    "State the linear-time scans (digit moves, splits, row splits) and the controlled cyclic shift that follow from them.",
    mot("The later address and butterfly procedures are built from a fixed number of such scans, so their costs are only meaningful once these are known to be linear.", "explicit",
        "the elementary scans it uses."),
    [A0_1, A0_2])

# ---------------------------------------------------------------- A: networks
A1 = show("A.1",
    "A fixed linear network of copy, gather, scatter and side-injection gates exchanges two banks, sending $(X_a,Y_a)$ to $(-Y_a,X_a)$ in three stages, and returns every scratch wire to its arbitrary initial value.",
    "Give each invocation an eight-row schedule whose first and last rows cancel the unknown scratch values, so that the net map is $y\\leftarrow y+x$; then chain three such invocations.",
    mot("Scratch wires may start with arbitrary values, so the schedule first subtracts their effect and finally restores them.", "explicit",
        "the following schedule remove the effect of the old scratch values;"),
    [
        infer("A.1.1", "For arbitrary initial scratch values, one invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.",
              r"invocation changes $y_S$ to $y_S+x_S$ and leaves every other value"),
        infer("A.1.2", "Three invocations (forward, inverse, forward) turn $(x,y)$ into $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$, which is the bank exchange with a sign.",
              r"$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$."),
    ],
    page="scratch-restoring-exchange",
    frm=["arithmetic-modulo-2-and-xor", "matrices-vectors-and-linear-maps", "permutations-and-bijections", "sets-subsets-and-cartesian-products"],
    salient="The net effect of the network is independent of the arbitrary initial values of all auxiliary (scratch) wires, and each scratch wire ends with its own initial value.")

A2 = show("A.2",
    "If each scalar wire is replaced by an array and stored as $D_vg$ for an invertible frame $D_v$, a pointwise linear gate commutes with the frame, so the implemented operator is only $D_{\\rm out}\\mathsf S D_{\\rm in}^{-1}$.",
    "Assign an invertible operator (frame) to every source, gate and sink, apply $D_vD_u^{-1}$ on each edge, and check that the common frame passes through each linear pointwise gate.",
    mot("A pointwise linear gate acts on matching addresses, and a linear operator that is common to all wires at the gate can be pulled through it; hence only the endpoint frames are felt.", "recoverable"),
    [
        infer("A.2.1", "On an edge from $u$ to $v$ the wire's array is changed from $D_ug$ to $D_vg$ by $D_vD_u^{-1}$, the logical array staying fixed.",
              r"$D_vD_u^{-1}$ to that wire's array."),
        infer("A.2.2", "Because all incidences of a gate share the frame $D_v$ and the gate is linear and pointwise, the frame commutes with the gate and the invariant continues to the sinks.",
              r"Thus the common frame commutes with the pointwise gate, and"),
        infer("A.2.3", "The implemented operator is $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$: the intermediate frames cancel.",
              r"D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}."),
        infer("A.2.4", "Once the scalar routing is fixed, the endpoint frames determine the operator on every route, so the intermediate frames can be chosen to make each edge cheap.",
              r"intermediate frames can then be chosen to make each edge change inexpensive."),
    ],
    page="array-frames",
    frm=["matrices-vectors-and-linear-maps", "scratch-restoring-exchange", "permutations-and-bijections"],
    salient="Only the endpoint frames matter: all intermediate frames cancel along a route, for every role including the auxiliary ones.")

A3 = show("A.3",
    "Attaching nested nondegenerate subspaces built from indicator vectors of three-element subsets to the gates and terminals of the bit network gives a total edge rank $s_{\\rm b}$ strictly less than $W_{\\rm b}m$.",
    "Choose labels as tensor products of triple lines so that neighbouring labels are nested, count the dimension change of every edge, and show that only the central edges from time 3 to 4 decrease, losing $L<N/2$ in total.",
    mot("The saving must come from keeping the total dimension lost on decreasing edges small relative to $N$; the sources promise $L<N/2$ so that the extra $N$ source ranks still leave a strict saving.", "explicit",
        r"We will obtain $L<N/2$. The rational interface below will require"),
    [
        infer("A.3.1", "The signed dimension changes over all edges sum to $Wm-2N$; if decreasing edges lose a total dimension $L$, the sum of absolute changes is $Wm-2N+2L$.",
              r"dimension $L$, the sum of absolute changes is $Wm-2N+2L$."),
        infer("A.3.2", "Every edge joins comparable nondegenerate labels, the only decreasing edges are the central-wire edges from time 3 to 4 (loss $h$ each), and hence $L=Ich$.",
              r"The only decreasing"),
        infer("A.3.3", "The loss ratio is $L_{\\rm b}/N=100/539<1/2$ (and $101/539$ for the complex network).",
              r"\frac{L_{\rm b}}{N}=\frac{100}{539}"),
        infer("A.3.4", "With the projection matrices as frames, every input role sees endpoint difference $I_m$, and the rank sum $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}$ falls short of $W_{\\rm b}m$ by $N-2L_{\\rm b}>0$.",
              r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$."),
    ],
    page="subset-intersection-labels",
    frm=["rank-and-orthogonal-subspaces", "scratch-restoring-exchange", "array-frames", "sets-subsets-and-cartesian-products", "matrices-vectors-and-linear-maps", "dot-product-inner-product-and-orthogonality"],
    salient="The rank budget is strictly below the trivial value $Wm$: the deficit is $N-2L>0$ because the loss ratio $L/N$ is only $100/539$ (bit network) and $101/539$ (complex network), both under $1/2$.",
    adds=[B("N", "bank size", "the number of data wires in one bank, $N=v^3$ with $v=\\binom{h}{3}$, equal to the total of the source dimensions", "count"),
          B("L", "dimension loss", "the total dimension lost on decreasing edges of the labelled network", "count")])

A4 = show("A.4",
    "In the second network, over Gaussian dyadics with binary labels, each edge frame change is a product of translation kernels $aI+bX_v$, one per orthonormal basis vector of its residual, their total number is $s_{\\rm c}<W_{\\rm c}m$, and the endpoint operator is $C^{\\otimes m}$ on every role.",
    "Use phase frames diagonalised by $H^{\\otimes m}$: the weight modulo 4 of the projection gives a phase whose conjugate by $H$ is a product of two-point kernels $C=aI+bX$; then telescope the frames along each route.",
    mot("Frames diagonal in the Fourier basis make each edge difference a diagonal phase, and conjugating by the Hadamard transform turns each phase on one basis direction into a translation kernel, so the number of kernels equals the residual dimension.", "recoverable"),
    [
        infer("A.4.1", "For an orthonormal basis vector $v$ of the residual, the phase $i^{\\varepsilon[v\\cdot x]}$ conjugated by $H$ becomes the kernel $aI+bX_v$ or its inverse.",
              r"becomes $aI+bX_v$ or its inverse."),
        infer("A.4.2", "The residual bases have dimensions given by the residual lemma, so the number of kernel factors over the network is $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}<W_{\\rm c}m$.",
              r"The same lemma gives the count $s_{\rm c}$."),
        infer("A.4.3", "After diagonal corrections, using $C=iZC^{-1}Z$ to turn inverse factors into forward ones, and undoing the signed exchange, every role carries the forward tensor product $C^{\\otimes m}$.",
              r"the required forward tensor product."),
    ],
    page="phase-frame-network",
    frm=["array-frames", "subset-intersection-labels", "rank-and-orthogonal-subspaces", "fixed-point-complex-arithmetic", "roots-of-unity-and-euler-s-formula", "scratch-restoring-exchange"],
    salient="The endpoint operator is the same $C^{\\otimes m}$ on every role, including the roles that only carried auxiliary scratch values.",
    adds=[B("C", "two-point kernel", "the $2\\times2$ matrix $C=H\\mathsf S H=aI+bX$ whose tensor powers the network applies")])

A5 = infer("A.5",
    "The relative rank deficits of both networks exceed $20\\cdot2^{-50}$, so with $\\tau=\\sigma=1-2^{-50}$ one has $s_{\\rm b}/W_{\\rm b}<m^\\tau$ and $s_{\\rm c}/W_{\\rm c}<m^\\sigma$.",
    r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,",
    salient="The saving is tiny but strict: the relative deficits are about $1.5\\cdot10^{-11}$ and $3.7\\cdot10^{-12}$, so the exponent is only $1-2^{-50}$.")

A = show("A",
    "There are two fixed linear networks on $W$ wires with labels of dimension $m$ whose edge changes cost $s<Wm$ smaller operations in total, one acting by bit address shears and one by phase kernels.",
    "Design a scalar network that exchanges banks and restores scratch, lift it to arrays through frames, then choose subspace labels so each edge change is cheap and the total rank $s$ is below $Wm$.",
    mot("When values are arrays, a common representation at each gate lets the gate act pointwise without disturbing the representation, so the question reduces to how cheap the changes of representation along edges are.", "explicit",
        "pointwise without disturbing the representation."),
    [A1, A2, A3, A4, A5],
    adds=[B("W", "wire count", "the number of wires (roles) of the network, including scratch wires", "count"),
          B("m", "label dimension", "the dimension of the label space, equal to the number of address fields on which an edge acts", "count"),
          B("s", "total edge rank", "the sum over all edges of the rank of the frame change, equal to the number of smaller calls", "count")])

# ---------------------------------------------------------------- B: address chunk interchange
B1 = show("B.1",
    "An address shear $(H,D)\\mapsto(H+AD,D)$ for a rational matrix $A$ of rank $a$ is performed with exactly $a$ interchanges of pairs of smaller fields plus $O(V)$ other work.",
    "Factor $A=E_1\\Pi E_2$ with lower-triangular $E_1,E_2$ and a partial permutation $\\Pi$ with $a$ ones; triangular maps are controlled shifts, and each one of $\\Pi$ is one field interchange.",
    mot("Controlled shifts only update a later field from earlier ones, so changes of coordinates must be lower triangular, and a lower-triangular elimination leaves only a rank-sized partial permutation.", "explicit",
        "earlier fields in linear time.  Lower triangular changes of coordinates"),
    [
        infer("B.1.1", "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ having exactly $a$ ones.",
              r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization"),
        infer("B.1.2", "A lower triangular transformation of $H$ or of $D$ costs $O(V)$, by controlled shifts in descending physical order.",
              r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
        infer("B.1.3", "Each one of $\\Pi$ calls for $H_i\\leftarrow H_i+D_j$, done as $D_j\\leftarrow D_j+H_i$, an interchange, $D_j\\leftarrow H_i-D_j$, using just one interchange.",
              r"It uses just one interchange."),
    ],
    page="address-shear-factorization",
    frm=["controlled-cyclic-shift", "triangular-and-permutation-matrices", "matrices-vectors-and-linear-maps", "modular-arithmetic"],
    salient="The number of recursive interchanges is the rank $a$ of the shear matrix, not the dimension $m$.",
    adds=[B("A", "shear matrix", "the rational matrix of the address shear"),
          B("a", "matrix rank", "the rank of the shear matrix $A$, equal to the number of interchanges", "count")])

K1 = infer("B.2.4.1", "The number of recursive calls is the sum of the edge ranks, exactly $s$.",
           r"The number of recursive calls is the sum of the edge ranks, exactly $s$.")
K2 = infer("B.2.4.2", "Each call acts on one role stream of volume $V/W$, with all other fields kept as spectators.",
           r"Each acts on one role stream of volume $V/W$")
K3 = infer("B.2.4.3", "Splitting, merging, gates and triangular operations cost $O(V)$ at a node, so the cost per volume satisfies $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
           r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1).")
K4 = infer("B.2.4.4", "Since $s/W<m^\\tau$, the geometric sum $\\sum_{j\\le k}(s/W)^j$ is $O(m^{k\\tau})$, whether $s/W\\le1$ or $s/W>1$.",
           r"For $a=s/W<m^\tau$ the geometric sum")
K5 = infer("B.2.4.5", "Hence the normalized cost is $F_k=O(e^\\tau)$ for width $e=m^k$.",
           r"Hence $F_k=O(e^\tau)$.")
K6 = infer("B.2.4.6", "The fixed-tape depth-first schedule (parking the inactive streams, copying) moves $O(V)$ symbols per node, so the additive term is $O(V)$ even though each child has volume $V/W$.",
           r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$")

KEY = show("B.2.4",
    "The cost per unit volume of interchanging two chunks of width $e=m^k$ satisfies $F_k\\le(s/W)F_{k-1}+O(1)$ with $s/W<m^\\tau$, hence $F_k=O(e^\\tau)$: a power saving.",
    "Count the calls, normalize by volume (each child has $1/W$ of the volume), and unroll the recurrence as a geometric sum.",
    mot("Multiplying the width by $m$ multiplies the work per volume only by $s/W<m$, and this strict inequality is the source of the power saving.", "explicit",
        "is the source of the power saving."),
    [K1, K2, K3, K4, K5, K6],
    page="rank-saving-recurrence",
    frm=["subset-intersection-labels", "address-shear-factorization", "geometric-series-and-sums", "divide-and-conquer-and-recurrences", "big-o-notation"],
    salient="The factor per level is $s/W<m$ although the width grows by the factor $m$: the margin is tiny (exponent $\\tau=1-2^{-50}$) yet any strict margin yields a polynomial saving $e^{\\tau}$ instead of a factor $e$.",
    adds=[B("F_k", "normalized cost", "the time of an interchange of width $m^k$ divided by the logical volume", "direct")])

B2 = show("B.2",
    "Two disjoint chunks of $e=m^k$ digits can be interchanged in $O(Ve^\\tau)$ time provided the row field is divisible by $W^k$, by running the bit network on $W$ role streams with every edge shear done recursively.",
    "Split rows among the $W$ roles, apply the address shear on each edge with smaller interchanges, run the gates pointwise so the frame identity gives $H\\leftarrow H+D$ on every row, then finish with $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$.",
    mot("The row split supplies the common address set on which the pointwise gates and the address-permutation frames act, so the frame identity applies.", "explicit",
        "The row split supplies the common address set used in the"),
    [
        infer("B.2.1", "Within each prefix, whole rows are split cyclically into $W$ role streams, each with the same remaining shape and volume $V/W$.",
              r"Split whole rows cyclically into $W$ role streams within each prefix"),
        infer("B.2.2", "With frames $\\Phi_M$ and the endpoint matrix difference $I_m$ on every role, the physical output satisfies $f'_{\\rho(w)}=\\Phi_{I_m}f_w$: the shear $H\\leftarrow H+D$ on every row, including scratch rows.",
              r"=\Phi_{I_m}f_w,"),
        infer("B.2.3", "The interchange follows from the shear: $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$, only the middle step using the network.",
              r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,"),
        KEY,
    ],
    page="power-width-interchange",
    frm=["array-frames", "address-shear-factorization", "scratch-restoring-exchange", "subset-intersection-labels", "tape-address-model", "controlled-cyclic-shift"],
    adds=[B("e", "power width", "the number of radix digits in each of the two chunks, $e=m^k$", "count"),
          B("k", "recursion depth", "the exponent in $e=m^k$, the number of recursion levels", "count")])

B3 = show("B.3",
    "Arbitrary widths $u$ and general arrays can be handled by supplying rows from a few high digits, decomposing the width in base $m$, and padding binary chunks, still in $O(Vu^\\tau)$.",
    "Exchange a few high digits directly to create enough rows, split the remaining width into pieces of widths $m^j$, and apply the power-width interchange to each piece.",
    mot("Power-width interchange needs a row field divisible by $W^k$, and rows can be taken from a few of the array's own high digits, whose movement costs less than the final bound.", "explicit",
        "Rows for a general array can be supplied by a few of its own high digits."),
    [
        infer("B.3.1", "Taking the top $\\rho$ digits of each chunk as a row field gives $R=q^{2\\rho}\\ge W^k$ rows.",
              r"R=q^{2\rho}\ge W^k"),
        infer("B.3.2", "Writing the remaining width in base $m$ and interchanging each piece, the total cost is $O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau)$.",
              r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)."),
        infer("B.3.3", "Padding binary chunks of $u$ bits to radix-$q$ ranges, with $e=O(u)$, gives the bound $O(Vu^\\tau)$.",
              r"Since $e=O(u)$ for fixed $q$, the bound is"),
    ])

B_ = show("B",
    "Two disjoint contiguous address fields of $u$ bits of an array of volume $V$ can be interchanged in $O(Vu^\\tau)$ time for a fixed $\\tau<1$.",
    "Run the bit exchange network of the previous section on role streams: its endpoint operator is an address shear, each edge shear is implemented by smaller interchanges, and the rank saving yields a power recurrence; then remove width and row restrictions.",
    mot("An edge matrix of rank $a$ requires $a$ smaller interchanges, and because the ranks sum to less than $Wm$ the recurrence saves a power of the chunk width.", "explicit",
        "$m$, the resulting recurrence saves a power of the chunk width."),
    [B1, B2, B3],
    page="address-chunk-interchange",
    frm=["scratch-restoring-exchange", "array-frames", "subset-intersection-labels", "address-shear-factorization", "tape-address-model"],
    salient="Although the intermediate steps form XOR combinations of data, the final effect is an exact permutation, valid for arbitrary initial contents of the auxiliary roles.",
    adds=[B("\\tau", "interchange exponent", "a fixed exponent below 1 with $s/W<m^\\tau$, here $1-2^{-50}$"),
          B("u", "chunk width", "the number of bits in each of the two interchanged address chunks", "count")])

# ---------------------------------------------------------------- C: butterfly layers
C1 = show("C.1",
    "A $C$-tensor layer on $e=mf$ selected chunks is computed by $s_{\\rm c}$ child layers on $f$ chunks each, after binary changes of basis, and converts to the normalized $H_0$ layer exactly.",
    "Express each edge frame change as a product of two-point kernels, move the residual directions to coordinate positions by binary row additions, call children on the $m$ slots, and use $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$.",
    mot("The phase frames express a $C$ tensor product using smaller groups of selected bits, separated by binary changes of basis, which are implemented by moving whole address chunks.", "explicit",
        "selected bits, separated by binary changes of basis."),
    [
        infer("C.1.1", "Direct multiplication gives the identities $H_0=b\\mathsf SC\\mathsf S$, $C^2=X$, $C^4=I$.",
              r"H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad"),
        infer("C.1.2", "An edge's frame change is a product of $\\rho_{\\rm edge}$ directional kernels $(aI+bX_{v_j})^{\\epsilon_j}$, one per orthonormal basis vector of its residual.",
              r"=\prod_{j=1}^{\rho_{\rm edge}}(aI+bX_{v_j})^{\epsilon_j},"),
        infer("C.1.3", "A negative directional kernel still needs only one forward child, since $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$.",
              r"=(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}."),
        infer("C.1.4", "Any invertible binary change of basis is a product of at most $m(m-1)+3m$ elementary row additions, each changing corresponding selected bits in two whole slots.",
              r"as a product of at most $m(m-1)+3m$ elementary row additions: one clears"),
        infer("C.1.5", "Summing residual dimensions gives exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
              r"$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
        infer("C.1.6", "Applying the basic identities on all selected coordinates gives $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$.",
              r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D."),
    ],
    frm=["phase-frame-network", "fft-butterflies", "fixed-point-complex-arithmetic"])

C2 = show("C.2",
    "A binary row addition $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$ on the selected bits of $f$ chunks, with a third chunk restored, costs $O(V(L^\\tau+1))$ in the family of parameters used here.",
    "Apply eight whole-chunk cyclic shifts that are correct away from a small guard-violating set of addresses, then repair that set deterministically by extracting, sorting by destination and reinserting.",
    mot("Whole-chunk cyclic shifts are cheap but fail only where a segment carries into its neighbour, which happens for few addresses, so a cheap exact repair of those addresses suffices.", "explicit",
        "from a small set of addresses. We then correct exactly that set."),
    [
        infer("C.2.1", "Eight conditional additions induce, for a Boolean control, a flip of the parity of $u$ and restore the auxiliary integer $w$: $(u',w')=(u+c(1-2(u\\bmod2)),w)$.",
              r"\bigl(u+c(1-2(u\bmod2)),\ w\bigr)."),
        infer("C.2.2", "Each line is a single cyclic shift of a whole chunk whose offset does not depend on its target chunk, so it costs $O(V)$ after chunk swaps.",
              r"The shift offset never depends on its target chunk, so each line is a"),
        infer("C.2.3", "Outside the guard-violating set $\\mathcal B$ the packed shifts agree with the ideal XOR permutation, and $|\\mathcal B|\\le\\delta_{\\rm bad}M$ with $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$.",
              r"There are exactly twenty excluded values for each guard in"),
        infer("C.2.4", "The exceptional records are extracted with destination ranks and stably radix-sorted, then reinserted, which implements the ideal permutation everywhere.",
              r"while stable binary radix sorting scans only the extracted records and"),
        infer("C.2.5", "The movement costs $O(V(L^\\tau+1))$ and the extra terms vanish after division by $V$ in the stated family of parameters.",
              r"The movement costs $O(V(L^\tau+1))$."),
    ],
    page="packed-selected-bit-addition",
    frm=["address-chunk-interchange", "controlled-cyclic-shift", "tape-address-model", "sorting-and-its-cost", "arithmetic-modulo-2-and-xor"],
    salient="Only a tiny fraction (at most $80(f-1)2^{-K}$) of addresses violates the guard condition, so repairing them by sorting costs $o(V)$ and the bound is worst-case over all payloads.")

C3 = show("C.3",
    "Unrolling the recursion over $e$ selected chunks, with node cost $O((eK)^\\tau+1)$ and $s/W<m^\\sigma$, gives total normalized cost $O(d^{\\lambda'})$ for a layer on at most $d$ chunks.",
    "Split rows among the $W$ roles so each child has volume $V/W$, write the normalized cost recurrence $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$, stop the recursion below $d^\\beta$ chunks, and sum the geometric series.",
    mot("Dividing the total cost of the $s$ children, each on a stream of volume $V/W$, by the current volume gives the factor $s/W$, the same rank saving as for address interchange.", "explicit",
        "gives the factor \\(s/W\\)."),
    [
        infer("C.3.1", "Binary changes of basis, scalar gates, endpoint corrections and reassembly cost $O(V((eK)^\\tau+1))$ at a node, using the packed row addition.",
              r"endpoint corrections and reassembly of the physical banks cost"),
        infer("C.3.2", "Row indices are split among the $W$ roles, so each recursive edge call acts on a stream of volume exactly $1/W$ of its parent's.",
              r"one role stream with volume exactly \(1/W\) of its parent"),
        infer("C.3.3", "Time divided by volume obeys $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$, with $F(e)=O(e)$ below the cut-off $e<d^\\beta$.",
              r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
        infer("C.3.4", "Summing internal and leaf contributions and the base-$m$ pieces gives $O(d^{\\lambda'})$ for any fixed $\\lambda'$ with $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$.",
              r"=O(d^{\lambda'})"),
    ])

C4 = show("C.4",
    "All intermediate Gaussian dyadic values of a layer are exact with $p+\\Delta$ fractional and $\\Delta+3$ integer bits, where $\\Delta=\\lceil C_0d^{C_1}\\rceil=o(p)$, so only one truncation follows the layer.",
    "Bound the arithmetic dependency depth $A(e)\\le sA(e/m)+E$ along the recursion, and note each operation at most doubles the modulus or adds one denominator bit.",
    mot("The accelerated network is evaluated exactly until the whole normalized layer is complete, and its intermediate operators need not be contractions, so explicit growth bounds are needed.", "explicit",
        "need not be contractions.  We now give explicit constants that bound"),
    [
        infer("C.4.1", "The depth of a chain of arithmetic operations obeys $A(e)\\le sA(e/m)+E$ at an internal node, hence it is polynomial $O(d^{C_1})$ in $d$.",
              r"A(e)\le sA(e/m)+E"),
        infer("C.4.2", "Reserving $p+\\Delta$ fractional bits and $\\Delta+3$ integer and sign bits per real component represents every intermediate coefficient exactly and prevents overflow.",
              r"Thus reserving \(p+\Delta\)"),
    ])

C5 = show("C.5",
    "The simultaneous normalized butterfly layer returns $Q_p(\\mathcal Hz)$ in $O(Vd^{\\lambda'})$ time with error below $\\sqrt2\\,2^{-p}$, staying in the unit disk.",
    "Combine the cost of the recursion with the exact evaluation and the single truncation, using that $\\mathcal H$ has row sums of modulus one.",
    mot("Every row of $\\mathcal H$ has absolute row sum one, so $\\mathcal H$ is a contraction, and the single final truncation adds less than $\\sqrt2\\,2^{-p}$.", "recoverable"),
    [
        infer("C.5.1", "The row construction and recurrence analysis give total time $O(Vd^{\\lambda'})$ on fixed tapes, including padding, repair and cleanup.",
              r"above give total time $O(Vd^{\lambda'})$ on fixed tapes, including"),
        infer("C.5.2", "$\\mathcal H$ maps disk arrays to disk arrays and componentwise truncation preserves the disk with error below $\\sqrt2\\,2^{-p}$.",
              r"Thus $\mathcal H$ maps disk arrays to disk"),
    ])

C_ = show("C",
    "Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ to the same bit position in each of $D\\le d$ address chunks of $K$ bits at once, on polynomial records with complex fixed-point coefficients, costs $O(Vd^{\\lambda'})$ with one final truncation.",
    "Run the complex phase network on groups of $e=mf$ chunks, implement its binary changes of basis by packed selected-bit additions, split rows among the $W$ roles, and unroll the resulting recurrence with exact dyadic arithmetic.",
    mot("Separate butterfly factors would need $D$ whole-array passes, so the $D$ butterflies must be applied simultaneously through the rank-saving network.", "explicit",
        "factors would require $D$ whole-array passes."),
    [C1, C2, C3, C4, C5],
    page="simultaneous-butterfly-layer",
    frm=["phase-frame-network", "address-chunk-interchange", "fft-butterflies", "fixed-point-complex-arithmetic", "array-frames", "subset-intersection-labels", "rank-saving-recurrence"],
    salient="A layer on $d$ chunks costs only $O(Vd^{\\lambda'})$ with $\\lambda'=1-2^{-54}<1$, rather than the $d$ full passes of separate butterflies.",
    adds=[B("K", "chunk width", "the number of bits in each address chunk of an axis", "count"),
          B("\\lambda'", "layer exponent", "a fixed exponent below 1 in the layer cost $O(Vd^{\\lambda'})$"),
          B("D", "chunk count", "the number of address chunks (axes) on which the layer acts, at most $d$", "count")])

# ---------------------------------------------------------------- D: synthetic transforms
D1 = show("D.1",
    "Over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ the transforms $F_t^\\pm$ with roots $\\omega_t=y^{2r/t}$ are contractions with $F_t^+F_t^-=t^{-1}I$, and $F_t^-$ is computed by decimation-in-frequency butterflies whose twiddles are signed shifts.",
    "Use powers of $y$ as roots of unity (isometries), verify character cancellation directly since the ring has zero divisors, and recurse with an $H_0$ butterfly followed by a monomial twiddle.",
    mot("In the quotient by $y^r+1$ multiplication by a power of $y$ is a signed shift of the coefficient list, so the twiddle multiplications cost no real arithmetic.", "explicit",
        "serve as roots of unity in the remaining axes, and multiplication by"),
    [
        infer("D.1.1", "Every power of $\\omega_t$ is an isometry and each output averages $t$ such images, so both transforms are contractions.",
              r"Thus both transforms are contractions."),
        infer("D.1.2", "Character cancellation holds directly: $\\sum_k\\omega_t^{jk}$ is $t$ if $t\\mid j$ and $0$ otherwise, giving $F_t^+F_t^-=t^{-1}I$.",
              r"F_t^+F_t^-=t^{-1}I."),
        infer("D.1.3", "The decimation-in-frequency step applies $H_0$ to the pairs $(z_k,z_{k+t/2})$, multiplies the $b=1$ output by $\\omega_t^{-k}$, and recurses on both halves.",
              r"the $b=1$ output by $\omega_t^{-k}$, and then apply the length-$t/2$"),
    ],
    page="synthetic-polynomial-transform",
    frm=["negacyclic-ring", "discrete-fourier-transform", "fft-butterflies", "roots-of-unity-and-euler-s-formula", "polynomials"],
    salient="Although $\\mathcal R_r$ has zero divisors, the transforms are still inverse up to $1/t$, because shifting the summation index by $t/2^{v+1}$ multiplies the sum by $y^{rj_0}=-1$.")

D2 = show("D.2",
    "The forward transform writes its outputs in bit-reversed order, the pointwise product and the opposite transform use that same order, so no permutation is ever executed.",
    "Track the address bits through the levels to see that entry $j$ lands in slot $\\mathrm{rev}(j)$, then run the levels in reverse order to invert it.",
    mot("The opposite transform consumes the same frequency order after the pointwise product, so it is better to leave the output where the recursion writes it.", "explicit",
        "is stored, because the opposite transform consumes that same order"),
    [
        infer("D.2.1", "After all levels the entry $(F_t^-z)_j$ occupies slot $\\mathrm{rev}_a(j)$.",
              r"entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$."),
        infer("D.2.2", "Traversing the recursion in reverse gives the opposite procedure, so the two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
              r"B_tF_t^-,\qquad F_t^+B_t^{-1},"),
        infer("D.2.3", "On $D$ axes the individual axis steps of a round group into one parallel butterfly $\\mathcal H$ followed by one recordwise monomial $J_E$.",
              r"Consequently the individual axis steps may be grouped as a parallel"),
    ],
    page="stored-frequency-order",
    frm=["synthetic-polynomial-transform", "fft-butterflies", "permutations-and-bijections"],
    salient="No bit-reversal permutation is executed: the forward transform stores it, and pointwise products commute with applying the same permutation to both operands.")

D3 = show("D.3",
    "Placing the selected bit of each axis at a common offset in consecutive $K$-bit chunks makes each transform round one simultaneous layer, so a synthetic transform of $T$ records of $p$-bit coefficients costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error below $\\sqrt2\\,\\ell\\,2^{-p}$.",
    "Move a few slots to a prefix with bit moves, bring chunks with equal index together by chunk interchanges, then run each round as one simultaneous layer, charging layout and its inverse.",
    mot("To apply the simultaneous layer in a transform round the selected bits of the participating axes must sit at a common offset in consecutive $K$-bit chunks.", "explicit",
        "we must place the selected bits of the participating axes at a common"),
    [
        infer("D.3.1", "Moving at most $D(b+1)=O(dK)$ listed slots of the $M$ records to a prefix costs $O(TpdK)$.",
              r"listed slots, so the moves cost $O(TpdK)$."),
        infer("D.3.2", "At most $Dq$ exchanges of width-$K$ chunks, each costing $O(TpK^\\tau)$, cost $O(Tp\\,pK^{\\tau-1})$ in total.",
              r"=O\bigl(Tp\,pK^{\tau-1}\bigr)."),
        infer("D.3.3", "The rounds on the remaining chunks use the simultaneous-layer procedure, at cost $O(Tpd^{\\lambda'})$ per round and $O(Tp\\ell d^{\\lambda'})$ in total.",
              r"The simultaneous-layer procedure therefore applies at cost"),
        infer("D.3.4", "A contraction does not increase the error and each round truncates once, so at most $\\ell$ rounds give error below $\\sqrt2\\,\\ell\\,2^{-p}$ and stay in the disk.",
              r"give the claimed error and disk bounds."),
    ],
    page="transform-tape-layout",
    frm=["simultaneous-butterfly-layer", "address-chunk-interchange", "tape-address-model", "stored-frequency-order", "synthetic-polynomial-transform"],
    adds=[B("\\ell", "record exponent", "the base-2 logarithm of the record length, $r=2^\\ell$", "count"),
          B("M", "record count", "the number of polynomial records, $M=T/r$", "count")])

D_ = show("D",
    "Normalized synthetic Fourier transforms over $\\mathcal R_r$ on $d-1$ axes can be run with the opposite order retained, at tape cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
    "Define the transforms with signed-shift roots, record where each frequency is stored, and lay the bits out so that each round is one simultaneous butterfly layer.",
    mot("The normalized Fourier transforms needed for convolution have entries that are short polynomials where roots of unity act by exact signed permutations, and the frequency order must be known so the opposite transform can consume it.", "explicit",
        "We now implement the normalized Fourier transforms needed for"),
    [D1, D2, D3])

# ---------------------------------------------------------------- E: ring convolution
E1 = show("E.1",
    "Two polynomials in $\\mathcal R_r$ with small signed Gaussian integer coefficients can be multiplied exactly, and $Q_p(fg/r)$ returned, in $O(rp\\log(rp))$ time with the $O(N\\log N)$ integer multiplier.",
    "Evaluate each polynomial at $B_0=2^{4p}$ (Kronecker substitution) with signed carries, multiply four pairs of integers, and extract the coefficients by centered residues modulo $B_0$.",
    mot("The integer multiplier of Harvey and van der Hoeven has cost $O(N\\log(2N))$ and is used here only as an independent subroutine on short inputs.", "explicit",
        r"O(N\log(2N))$ on $N$-bit inputs.  This is an independent subroutine."),
    [
        infer("E.1.1", "Each polynomial is turned into an integer by evaluation at $B_0$, $A_u=u(B_0)=\\sum_j u_jB_0^j$.",
              r"A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j."),
        infer("E.1.2", "The product coefficients satisfy $|h_j|\\le r2^{2p}<2^{3p}<B_0/2$, so adjacent fields do not collide.",
              r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
        infer("E.1.3", "Coefficients are recovered one block at a time as the centered residue modulo $B_0$ of $q_j+\\rho_j$, with a carry in $\\{0,1\\}$.",
              r"integer in $[-B_0/2,B_0/2)$ congruent to $q_j+\rho_j$ modulo $B_0$,"),
        infer("E.1.4", "Four exact integer products on $O(rp)$-bit inputs dominate the linear packing, extraction and wrapping, giving $O(rp\\log(rp))$.",
              r"Four exact integer products dominate the linear"),
    ],
    page="signed-packing",
    frm=["n-log-n-barrier", "negacyclic-ring", "polynomials", "positional-notation-in-any-radix"],
    salient="The records have only $O(rp)=o(n)$ bits, so the established $O(n\\log n)$ multiplier is called as an ordinary subroutine and the improved algorithm is not invoked recursively.")

E_ = show("E",
    "On arrays of ring elements, two forward synthetic transforms, a pointwise polynomial product divided by $r$, and the opposite transform followed by a scaling by $M$ compute $(f*g)/T$ with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
    "Multiply the forward outputs in their retained order, pass them to the opposite procedure, and track the normalization and the accumulated truncation errors by contraction bounds.",
    mot("Pointwise multiplication commutes with applying the same record permutation to both operands, so the forward outputs can be multiplied in the retained order and passed straight to the opposite procedure.", "explicit",
        "permutation $LB$ to both operands.  We may therefore multiply the"),
    [
        E1,
        infer("E.2", "Expanding the finite sums, $F^-_{\\boldsymbol t}(f*g)=M(F^-_{\\boldsymbol t}f)(F^-_{\\boldsymbol t}g)$, so $MF^+_{\\boldsymbol t}$ of the pointwise product divided by $r$ is $(f*g)/(rM)$.",
              r"=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)."),
        infer("E.3", "Since $LB$ permutes records and leaves their polynomial suffixes intact, the opposite procedure applied to the pointwise product of the stored outputs gives the exact convolution.",
              r"Since $LB$ permutes records and leaves their polynomial suffixes"),
        infer("E.4", "Each forward error is below $\\delta=\\sqrt2\\ell2^{-p}$, the product adds $2\\delta+\\eta$, the opposite transform is a contraction, and the final scaling by $M$ gives error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
              r"The final exact multiplication by $M$ therefore gives error less than"),
        infer("E.5", "There are $M=T/r$ pointwise polynomial products, costing $O(Tp\\log(rp))$ in total, in addition to the three transforms.",
              r"There are $M=T/r$ pointwise polynomial products."),
    ],
    page="normalized-ring-convolution",
    frm=["transform-tape-layout", "stored-frequency-order", "synthetic-polynomial-transform", "signed-packing", "contraction-error-propagation", "convolution", "negacyclic-ring", "discrete-fourier-transform"],
    salient="No permutation of the frequency order is ever executed between the forward transforms, the pointwise product and the opposite transform.")

# ---------------------------------------------------------------- F: resampling and chirp
F1 = show("F.1",
    "A Fourier transform of prime length $s$ equals $2^{2\\alpha^2}B_0P_tF_tA$ for a power-of-two length $t>s$ with Gaussian contractions $A$ and $B_0$ and with the coordinate permutations kept in the formula; on $d$ axes this tensors to $RF_{\\boldsymbol s}=2^{\\gamma}\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$.",
    "Use the Gaussian resampling identity of Harvey and van der Hoeven, normalise the resampling maps so they are contractions, keep the permutations $P_s,P_t$ explicit, and apply the one-dimensional maps line by line on the padded box.",
    mot("The tensor transform on a growing number of axes is built from one-dimensional maps applied along one coordinate line at a time, with axis movement done by chunk interchanges.", "recoverable"),
    [
        infer("F.1.1", "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and $B_0:\\mathbb C^t\\to\\mathbb C^s$ built from the Gaussian maps.",
              r"There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and"),
        infer("F.1.2", "They satisfy $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ with the permutations $P_s,P_t$ left in the identity.",
              r"P_sF_s=2^{2\alpha^2}B_0P_tF_tA."),
        infer("F.1.3", "Approximations $\\widetilde A,\\widetilde B_0$ with error below $p^2$ run in time $O(tp^{3/2+\\delta}\\alpha)$ on a line of length $t$.",
              r"There are fixed multitape algorithms for approximations"),
        infer("F.1.4", "Tensoring over $d$ axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$.",
              r"=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A,"),
        infer("F.1.5", "The linewise implementations have error below $dp^2$ and total time $O(dTp^{3/2+\\delta}\\alpha)$ over the padded box.",
              r"one-dimensional algorithms for both maps is"),
    ],
    page="gaussian-resampling",
    frm=["discrete-fourier-transform", "contraction-error-propagation", "exponential-logarithm-and-gaussian-function", "primes-coprimality-and-gcd", "permutations-and-bijections", "address-chunk-interchange"],
    salient="The Gaussian identity keeps both coordinate permutations in the transform formula, so no sort of the data is performed to resample.")

F2 = show("F.2",
    "The middle transform with its frequency permutation is $QF_{\\boldsymbol t}u=\\overline a\\cdot\\bigl(a*(\\overline a\\cdot u)\\bigr)/T$ for the chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$: chirp phases around one cyclic convolution.",
    "Expand the product of the chirp phases $\\overline a_{\\boldsymbol j}a_{\\boldsymbol j-\\boldsymbol k}\\overline a_{\\boldsymbol k}$ so that the squares cancel and only the cross term $2\\pi i\\sum s_ij_ik_i/t_i$ remains.",
    mot("The chirp identity performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array.", "explicit",
        "multiplications. The chirp identity below performs the frequency change"),
    [
        infer("F.2.1", "For the chirp $a$, $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$.",
              r"\frac{a*(\overline a\mathbin{\cdot}u)}{T}."),
        infer("F.2.2", "The chirp $a$ has period $t_i$ in coordinate $i$, so it is a well defined cyclic kernel.",
              r"Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by"),
        infer("F.2.3", "The coefficient of $u_{\\boldsymbol k}$ in the right side is $\\frac1T\\exp(2\\pi i\\sum_i s_ij_ik_i/t_i)$, exactly the coefficient in $QF_{\\boldsymbol t}$.",
              r"=\frac1T\exp\left(2\pi i\sum_i"),
    ],
    page="bluestein-chirp",
    frm=["discrete-fourier-transform", "convolution", "complex-numbers", "roots-of-unity-and-euler-s-formula", "modular-arithmetic"])

F3 = show("F.3",
    "With the source permutation $R$ retained, $RF^+_{\\boldsymbol s}[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$: the permutation cancels between the two forward transforms, the pointwise product and the opposite transform.",
    "Show $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$ by substituting $h=ck$ in the sum, and use that a coordinate permutation commutes with pointwise products.",
    mot("The usual implementation of resampling sorts twice on each coordinate; keeping both permutations in the formula and cancelling them avoids the full sorts.", "explicit",
        "coordinate. We retain both permutations in the transform formula and"),
    [
        infer("F.3.1", "For a unit $c$ modulo $q$, $F_q^+R_c=R_c^{-1}F_q^+$; tensoring, $F^+_{\\boldsymbol s}R=R^{-1}F^+_{\\boldsymbol s}$ and hence $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$.",
              r"$F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence"),
        infer("F.3.2", "A coordinate permutation commutes with pointwise products, so $(RFu)\\cdot(RFv)=R(Fu\\cdot Fv)$.",
              r"because a coordinate permutation commutes with pointwise products."),
        infer("F.3.3", "The normalizations $F_{\\boldsymbol s}(u*v)=S(F_{\\boldsymbol s}u)(F_{\\boldsymbol s}v)$ and $F^+_{\\boldsymbol s}F_{\\boldsymbol s}=I/S$ give $(u*v)/S^2$.",
              r"The two normalizations give"),
    ],
    page="permutation-cancellation",
    frm=["gaussian-resampling", "discrete-fourier-transform", "convolution", "permutations-and-bijections", "modular-arithmetic", "primes-coprimality-and-gcd"],
    salient="The source permutation $R$ appears once on each of the two forward transforms and once on the opposite transform, and it cancels exactly, so no sort is ever run.")

F_ = show("F",
    "A source Fourier transform on pairwise coprime (prime) lengths can be computed through power-of-two transforms, with the middle transform as a chirp convolution and with the coordinate permutations cancelling rather than being executed.",
    "Use Gaussian resampling to pass from prime lengths to power-of-two lengths, Bluestein's chirp to turn the middle transform into a cyclic convolution, and an algebraic cancellation of the retained permutations.",
    mot("The transform lengths needed for the product are pairwise coprime whereas the synthetic transforms use powers of two, and Gaussian resampling connects these two shapes.", "explicit",
        "whereas the synthetic transforms use powers of two. Gaussian resampling"),
    [F1, F2, F3])

# ---------------------------------------------------------------- G: assembly
G1 = show("G.1",
    "Parameters $p=6b$, $d\\approx p^\\epsilon$, $T\\in[4n/b,8n/b)$, $r=2^{\\Theta(p^{1-\\epsilon})}$, axis lengths $t_i\\in\\{r/2,r\\}$ and distinct odd primes $s_i$ just below $t_i$ give $Tp=\\Theta(n)$, $T/2<S<T$ and all the hypotheses of the lemmas.",
    "Fix rational exponents once and for all, derive the sizes from $b=\\lceil\\log_2n\\rceil$, and choose primes in disjoint intervals $((1-2\\eta)t_i,(1-\\eta)t_i]$ using a prime-counting estimate.",
    mot("The prime lengths must be close to the powers of two: their product must fill a fixed fraction of the padded box, while each ratio $t_i/s_i$ leaves enough separation for resampling.", "explicit",
        "their product must occupy a fixed fraction of the padded box,"),
    [
        infer("G.1.1", "The fixed rational exponents include $\\epsilon=2^{-75}$ and $\\kappa=2^{-182}$.",
              r"C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}."),
        infer("G.1.2", "With $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$ one has $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$ and $r=2^{\\Theta(p^{1-\\epsilon})}$.",
              r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,"),
        infer("G.1.3", "There are distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$, each coprime to $t_i$.",
              r"(1-2\eta)t_i<s_i\leq(1-\eta)t_i."),
        infer("G.1.4", "The product $S=\\prod_is_i$ satisfies $T/2<S<T$.",
              r"Together with $s_i<t_i$, this gives $T/2<S<T$."),
        infer("G.1.5", "Every hypothesis of the resampling lemma holds for all sufficiently large input lengths.",
              r"Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for"),
    ],
    page="parameter-regime",
    frm=["gaussian-resampling", "simultaneous-butterfly-layer", "transform-tape-layout", "normalized-ring-convolution", "primes-coprimality-and-gcd", "asymptotic-notation-beyond-big-o", "exponential-logarithm-and-gaussian-function"])

G2 = show("G.2",
    "Writing each $n$-bit integer as a polynomial in $2^b$ with $q=\\lceil n/b\\rceil$ digits reduces the product to a convolution modulo $x^S-1$ without wraparound, with coefficients below $2^{3b}$.",
    "Split into $b$-bit digits, observe that the product has degree below $S$, and bound each convolution coefficient.",
    mot("Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.", "explicit",
        "Splitting the inputs into radix digits reduces multiplication to"),
    [
        infer("G.2.1", "Each input is a polynomial in $2^b$ with $q=\\lceil n/b\\rceil$ nonnegative digits.",
              r"Write the two inputs as polynomials in $2^b$, each with"),
        infer("G.2.2", "The product has degree at most $2q-2<T/2<S$, so convolution modulo $x^S-1$ has no nonzero wraparound.",
              r"2q-2<2n/b\le T/2<S."),
        infer("G.2.3", "Every product coefficient satisfies $0\\le c_j\\le q(2^b-1)^2<2^{3b}$.",
              r"0\le c_j\le q(2^b-1)^2<2^{3b},"),
    ],
    page="radix-digit-reduction",
    frm=["positional-notation-in-any-radix", "polynomials", "convolution", "integer-division-with-remainder-floor-and-ceiling", "parameter-regime"])

G3 = show("G.3",
    "The map $\\Phi:x\\mapsto\\prod_ix_i^{\\mu_i}$ is an algebra isomorphism from $\\mathbb C[x]/(x^S-1)$ onto the product of pairwise coprime cyclic axes that preserves convolution, and it costs $O(Tp\\,d^2(1+\\ell^\\tau))$.",
    "Use the Chinese remainder theorem in the form of a triangular coordinate change, implemented as controlled shifts in descending axis order plus axis reorderings by chunk interchanges.",
    mot("The coordinate powers are chosen so that the change of order becomes a sequence of controlled cyclic shifts.", "explicit",
        "sequence of controlled cyclic shifts."),
    [
        infer("G.3.1", "$\\Phi$ respects $x^S=1$ and runs through all target monomials, hence is an isomorphism preserving cyclic convolution.",
              r"$\Phi$ is an isomorphism and preserves cyclic convolution."),
        infer("G.3.2", "The coordinate of $\\Phi(x^k)$ on axis $i$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\bmod s_i$, depending only on lower-index digits.",
              r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}."),
        infer("G.3.3", "Updating targets in the order $i=d,d-1,\\dots,1$ makes each update a controlled shift whose controls are unchanged and precede the target on tape.",
              r"order $i=d,d-1,\ldots,1$ using"),
        infer("G.3.4", "With $O(d^2)$ axis moves by chunk interchanges, the map and its inverse cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
              r"Therefore the map $\Phi$, its inverse, and"),
    ],
    page="crt-axis-map",
    frm=["controlled-cyclic-shift", "address-chunk-interchange", "tape-address-model", "primes-coprimality-and-gcd", "modular-arithmetic", "convolution", "polynomials", "triangular-and-permutation-matrices"],
    salient="Each coordinate depends only on lower-index digits (a triangular system), and zero padding stays zero after every step.")

G4 = show("G.4",
    "The map $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ multiplies coefficient $k$ by $\\zeta^k$ and carries cyclic convolution on the last axis to convolution modulo $y^r+1$; untwisting recovers the cyclic result.",
    "Check that $(\\zeta y)^r=1$, that the map is diagonal in the monomial bases, and that the sign $(-1)^h$ of a wrap is cancelled by $\\zeta^r=-1$.",
    mot("The power-of-two complex convolution needed for the chirp is obtained from the synthetic convolution over the ring by this coefficient twist.", "explicit",
        "The power-of-two complex convolution used in the chirp identity is"),
    [
        infer("G.4.1", "The map is well defined since $(\\zeta y)^r=(-1)(-1)=1$, and it is diagonal on the bases with inverse multiplying by $\\zeta^{-k}$.",
              r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."),
        infer("G.4.2", "A product term with $k+l=j+hr$ carries the factor $\\zeta^{k+l}(-1)^h=\\zeta^j$, so untwisting recovers the cyclic coefficient with the right sign.",
              r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j."),
        infer("G.4.3", "Hence normalized complex cyclic convolution is $D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$.",
              r"normalized complex cyclic"),
    ],
    page="coefficient-twist",
    frm=["convolution", "negacyclic-ring", "roots-of-unity-and-euler-s-formula", "complex-numbers", "polynomials"])

G5 = show("G.5",
    "The approximate source transform, linewise $A$, chirp convolution of length $T$ on the padded box, linewise $B_0$ and an exact scale $2^\\gamma$, equals $RF_{\\boldsymbol s}$ on the prime-length source.",
    "Compose the computed linewise Gaussian map, the computed chirp transform built from the twisted ring convolution, the linewise compression, and the exact scaling.",
    mot("The middle factor $QF_{\\boldsymbol t}$ is evaluated by the complex convolution and then composed with the Gaussian maps.", "explicit",
        r"$QF_{\boldsymbol t}$ in \eqref{eq:no-sort-tensor}, and then compose it"),
    [
        infer("G.5.1", "The computed chirp transform forms $x_0=Q_p(\\overline{\\widetilde a}\\cdot x)$, convolves with the kernel $\\widetilde a$, and multiplies by $\\overline{\\widetilde a}$.",
              r"Thus $\widetilde a$ is the convolution kernel and $x_0$ is the data"),
        infer("G.5.2", "The exact counterpart of the source transform is $\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$.",
              r"\mathscr F=2^\gamma"),
        infer("G.5.3", "The opposite-sign procedure is obtained by conjugating input and output, with exact counterpart $RF^+_{\\boldsymbol s}$.",
              r"=\overline{\widetilde{\mathscr F}(\overline z)};"),
    ],
    page="tensor-source-transform",
    frm=["gaussian-resampling", "bluestein-chirp", "permutation-cancellation", "coefficient-twist", "normalized-ring-convolution", "parameter-regime", "contraction-error-propagation", "fixed-point-complex-arithmetic"])

G6 = show("G.6",
    "The multiplier converts the inputs to digits, applies $\\Phi$, takes two forward source transforms, multiplies pointwise, applies one opposite transform, scales by $S$ twice, rounds, applies $\\Phi^{-1}$ and propagates carries to output the $2n$-bit product.",
    "List the pipeline step by step and explain that the two occurrences of $S$ undo different normalizations.",
    mot("The source-transform procedures now supply the three transforms needed for the radix-digit convolution.", "explicit",
        "The source-transform procedures now supply the three transforms needed"),
    [
        infer("G.6.1", "Each radix-$2^b$ digit $a_j$ is written as the exact grid numerator $a_j2^{p-b-2}$ with a zero imaginary word, followed by $S-q$ zero records.",
              r"For digit $a_j$, write the exact grid numerator"),
        infer("G.6.2", "Apply the coefficient-address map $\\Phi$ to obtain source arrays $u,v$ of norm below $1/4$.",
              r"Apply the coefficient-address map $\Phi$, with its padded layout, to obtain"),
        infer("G.6.3", "Compute the two forward source transforms $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$.",
              r"Compute $\widetilde{\mathscr F}(u)$ and"),
        infer("G.6.4", "Multiply corresponding coefficients exactly and truncate to $p$ fractional bits to get $z$.",
              r"Multiply corresponding complex coefficients exactly and truncate"),
        infer("G.6.5", "Compute one opposite transform $\\widetilde{\\mathscr F}^+(z)$ and multiply its numerators exactly by $S$.",
              r"Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid"),
        infer("G.6.6", "Multiply by $2^{2b+4}S$, round to the nearest integers, and apply $\\Phi^{-1}$ with padding removed.",
              r"Multiply the grid numerators of $\widetilde w$ exactly by"),
        infer("G.6.7", "Propagate radix-$2^b$ carries in increasing order and output exactly $2n$ bits.",
              r"Propagate radix-$2^b$ carries in increasing coefficient order."),
        infer("G.6.8", "After the first scale the array is $w=(u*v)/S$; the second scale and $2^{2b+4}$ restore the integer coefficient convolution.",
              r"first scale it is $w=(u*v)/S$."),
    ],
    page="multiplication-algorithm",
    frm=["crt-axis-map", "tensor-source-transform", "permutation-cancellation", "radix-digit-reduction", "parameter-regime", "coefficient-twist"],
    salient="The factor $S$ is applied twice and $2^{2b+4}$ once, and each undoes a different normalization: $S^2$ from the permutation cancellation, and the input scales.")

G7 = show("G.7",
    "The recovered convolution coefficients are within error below $1/2$ of integers below $2^{3b}$, so rounding and carry propagation give the exact product.",
    "Track disk membership and errors of each computed map by contraction bounds, accumulate $E_{\\rm ring}$, the chirp, source and scaled errors, and compare the final error with $1/2$.",
    mot("The disk bounds needed by every call must be verified, and the final error must be shown to be less than $1/2$.", "explicit",
        "disk bounds needed by every call and proves that the final error is"),
    [
        infer("G.7.1", "The error of the normalized ring convolution is $E_{\\rm ring}=M(3L+2)<5TL$ with $L=\\log_2T$, and the output stays in the disk.",
              r"E_{\rm ring}:=M(3L+2)<5TL."),
        infer("G.7.2", "The computed chirp transform has error below $8TL\\,2^{-p}$.",
              r"<8TLh_p."),
        infer("G.7.3", "The source transform has error at most $E_s\\,2^{-p}$ with $E_s=9\\cdot2^\\gamma TL$.",
              r"E_s=9\,2^\gamma TL,"),
        infer("G.7.4", "After the first scale, the array $\\widetilde w$ approximates $w=(u*v)/S$ with error below $E_w2^{-p}$, $E_w=S(3E_s+2)<28\\cdot2^\\gamma T^2L$.",
              r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
        infer("G.7.5", "After the second scaling the absolute error is below $448b\\,2^{-3b/4}<1/2$, so the nearest integer is the correct coefficient.",
              r"\le448b\,2^{-3b/4}<\frac12."),
        infer("G.7.6", "The carries satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$ with $Q_0=2^b$, so carry propagation yields the exact radix digits of the product.",
              r"The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$."),
    ],
    page="precision-exact-recovery",
    frm=["contraction-error-propagation", "fixed-point-complex-arithmetic", "normalized-ring-convolution", "tensor-source-transform", "parameter-regime", "radix-digit-reduction", "permutation-cancellation"],
    salient="Working precision $p=6b$ against scale factors of about $2^{3b+o(b)}$ leaves a final error of about $2^{-b+\\gamma}$ with $\\gamma=o(b)$, so it is far below $1/2$.")

G8 = show("G.8",
    "Dividing every cost by $V=Tp$ gives normalized costs at most $p^{1-2\\kappa}$, the smallest margin $2^{-181}$ coming from the chunk-exchange term, so the total time is $O(n(\\log n)^{1-\\kappa})$.",
    "List the normalized cost of every operation as a power of $p$, compute the margins below one, and absorb setup, repair and all logarithmic factors.",
    mot("Costs are measured per unit of logical volume, so that the normalized costs can be compared with the power of $p$ allowed.", "explicit",
        "stored bits. Table~\\ref{tab:costs} lists costs after division"),
    [
        infer("G.8.1", "With $V=Tp=\\Theta(n)$, each coefficient has $O(p)$ bits, so a full padded array has $\\Theta(V)$ stored bits.",
              r"For the cost calculation put $V=Tp=\Theta(n)$."),
        infer("G.8.2", "The seven dominant powers have margins $g_1,\\dots,g_7$ below one, with $\\min_ig_i=2^{-181}=2\\kappa$.",
              r"Thus $\min_i g_i=2^{-181}=2\kappa$."),
        show("G.8.3",
             "The chunk-exchange term for the transform layout has normalized cost $pK^{\\tau-1}=p^{1-\\epsilon c(1-\\tau)}$, with margin $g_2=\\epsilon c(1-\\tau)=2^{-181}$.",
             "Count $O(p/K)$ exchanges of width $K$, each of normalized cost $K^\\tau$, and substitute the fixed exponents.",
             mot("The chunk interchanges are the only operation whose exponent margin is exceedingly small, because it multiplies the three small exponents $\\epsilon$, $c$ and $1-\\tau$.", "reconstructed"),
             [
                 infer("G.8.3.1", "The layout uses $O(p/K)$ exchanges of width-$K$ chunks, each costing $O(VK^\\tau)$.",
                       r"use $O(dK)$ linear scans. Its positional layout uses $O(p/K)$ exchanges"),
                 infer("G.8.3.2", "The normalized total is $O(p/K)K^\\tau=O(pK^{\\tau-1})$.",
                       r"O(p/K)\,K^\tau=O(pK^{\tau-1})."),
             ],
             salient="The smallest margin $2^{-181}=\\epsilon\\,c\\,(1-\\tau)=2^{-75}\\cdot2^{-56}\\cdot2^{-50}$ comes from the chunk-exchange term, and it forces $\\kappa=2^{-182}$."),
        infer("G.8.4", "Setup, prime search, sorting of exceptional streams and descriptor work are $o(V)$, each of the seven powers is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^\\kappa$.",
              r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
        infer("G.8.5", "The complete large-input bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
              r"=O(n(\log n)^{1-\kappa})."),
        infer("G.8.6", "Below a fixed cutoff schoolbook multiplication is used, so the single fixed machine has worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every input length.",
              r"conditions, and use schoolbook multiplication below it."),
    ],
    page="cost-accounting",
    frm=["parameter-regime", "address-chunk-interchange", "simultaneous-butterfly-layer", "transform-tape-layout", "normalized-ring-convolution", "crt-axis-map", "gaussian-resampling", "bluestein-chirp", "precision-exact-recovery", "multiplication-algorithm"],
    salient="The exponent is a power saving of only $\\kappa=2^{-182}$, because the smallest of the seven margins is $2^{-181}$, the chunk-exchange term.")

G_ = show("G",
    "The pieces assemble into a multiplier that is correct for every input and whose cost table fits the theorem.",
    "Choose compatible parameters, set up digits, the CRT layout, the twist and the source transforms, state the algorithm, verify precision and add up the costs.",
    mot("The remaining proof places the procedures inside the multiplication reduction, with compatible parameters for all of them.", "explicit",
        "We choose compatible parameters for these procedures, recover"),
    [G1, G2, G3, G4, G5, G6, G7, G8],
    adds=[B("b", "digit width", "the number of bits in each radix digit of the inputs, $b=\\lceil\\log_2n\\rceil$", "count"),
          B("S", "source size", "the product of the pairwise coprime source lengths $s_i$, with $T/2<S<T$"),
          B("\\epsilon", "dimension exponent", "the fixed exponent in $d=\\Theta(p^\\epsilon)$, equal to $2^{-75}$")])

# ---------------------------------------------------------------- root
ROOT = show("S0",
    "A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
    "Build two faster tape procedures (address chunk interchange and simultaneous butterfly layers) from rank-saving linear networks, use them in synthetic polynomial transforms and resampled source transforms for a convolution, reduce integer multiplication to that convolution, then prove exactness and add up costs.",
    mot("Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so savings are needed both in data movement and in arithmetic.", "explicit",
        "We therefore need savings in both movement and arithmetic."),
    [A0, A, B_, C_, D_, E_, F_, G_],
    page="main-theorem",
    frm=["n-log-n-barrier", "multitape-turing-machine", "schoolbook-and-karatsuba-multiplication", "big-o-notation", "binary-numerals-and-bit-strings", "subroutines-and-composition-of-algorithms"],
    salient="The saving is a genuine power of $\\log n$, but the exponent $\\kappa=2^{-182}$ is minuscule; it comes from a chain of strict inequalities ($s<Wm$, $\\tau<1$, $\\lambda'<1$) each only barely below its trivial value.",
    adds=[B("V", "logical volume", "the number of stored data bits of an array", "count"),
          B("p", "working precision", "the number of fractional bits of each stored complex coordinate", "count"),
          B("d", "axis count", "the number of axes (chunks) of the padded box, $d=\\Theta(p^\\epsilon)$", "count"),
          B("r", "record length", "the number of complex coefficients in one polynomial record", "count"),
          B("T", "box size", "the number of entries of the padded power-of-two box, the product of the axis lengths", "count"),
          B("t_i", "axis length", "the power-of-two length of axis $i$ of the padded box"),
          B("s_i", "source length", "the prime length of axis $i$ of the source, slightly less than $t_i$"),
          B("\\alpha", "Gaussian width", "the Gaussian width parameter of the resampling maps"),
          B("\\gamma", "scale exponent", "the exponent $\\gamma=2d\\alpha^2$ of the exact scale $2^\\gamma$ of the source transform")])

ans = {"root": ROOT}
json.dump(ans, open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F8V/exegenius/tasks/0003-argument.answer.json', 'w'), indent=1, ensure_ascii=False)

# ------------------------------------------------------------ validation
PAGES = """n-log-n-barrier convolution negacyclic-ring coefficient-twist signed-packing tape-address-model controlled-cyclic-shift scratch-restoring-exchange array-frames rank-and-orthogonal-subspaces subset-intersection-labels address-shear-factorization rank-saving-recurrence power-width-interchange address-chunk-interchange crt-axis-map packed-selected-bit-addition fixed-point-complex-arithmetic phase-frame-network discrete-fourier-transform fft-butterflies synthetic-polynomial-transform simultaneous-butterfly-layer bluestein-chirp stored-frequency-order transform-tape-layout contraction-error-propagation gaussian-resampling permutation-cancellation normalized-ring-convolution parameter-regime radix-digit-reduction tensor-source-transform precision-exact-recovery multiplication-algorithm cost-accounting main-theorem""".split()
KNOWN = """big-o-notation polynomials complex-numbers multitape-turing-machine binary-numerals-and-bit-strings positional-notation-in-any-radix integer-division-with-remainder-floor-and-ceiling modular-arithmetic arithmetic-modulo-2-and-xor primes-coprimality-and-gcd roots-of-unity-and-euler-s-formula exponential-logarithm-and-gaussian-function asymptotic-notation-beyond-big-o geometric-series-and-sums divide-and-conquer-and-recurrences schoolbook-and-karatsuba-multiplication sorting-and-its-cost permutations-and-bijections sets-subsets-and-cartesian-products multidimensional-arrays-and-row-major-order matrices-vectors-and-linear-maps triangular-and-permutation-matrices dot-product-inner-product-and-orthogonality dyadic-rationals-and-fixed-width-numerators matrix-transposition triangle-inequality-and-norms mathematical-induction-and-proof-by-contradiction cyclic-shifts-and-rotations-of-lists subroutines-and-composition-of-algorithms""".split()
pidx = {p: i for i, p in enumerate(PAGES)}
errors = []
ids = set()
used_pages = {}
pos = [0]
from_used = set()

def walk(n, anc_page):
    if n['id'] in ids: errors.append("dup id " + n['id'])
    ids.add(n['id'])
    page = n.get('page') or anc_page
    if n.get('page'):
        if n['page'] in used_pages: errors.append("page reused " + n['page'])
        used_pages[n['page']] = n['id']
        if n['page'] not in pidx: errors.append("bad page " + n['page'])
    for f in n.get('from', []):
        from_used.add(f)
        if f in KNOWN: continue
        if f not in pidx: errors.append("bad from %s in %s" % (f, n['id'])); continue
        if page is None or pidx[f] >= pidx[page]:
            errors.append("from %s not before page %s in %s" % (f, page, n['id']))
    if n['intention'] == 'infer':
        q = n['quote']['quote']
        c = SRC.count(q)
        if c == 0: errors.append("quote missing in %s: %r" % (n['id'], q))
        else:
            if c > 1: errors.append("quote not unique (%d) in %s: %r" % (c, n['id'], q))
            if not n.get('deferred'):
                i = SRC.find(q, pos[0])
                if i < 0: errors.append("out of order %s: %r" % (n['id'], q))
                else: pos[0] = i + len(q)
        if n.get('children'): errors.append("infer with children " + n['id'])
    else:
        m = n.get('motivation')
        if m and m['source'] == 'explicit':
            if SRC.find(m['quote']['quote']) < 0: errors.append("motivation quote missing in %s: %r" % (n['id'], m['quote']['quote']))
        for c in n['children']:
            walk(c, page)

walk(ROOT, None)
for p in PAGES:
    if p not in used_pages and p not in from_used:
        errors.append("page unused: " + p)
print("pages with steps:", len(used_pages))
print("\n".join(errors) if errors else "OK")
