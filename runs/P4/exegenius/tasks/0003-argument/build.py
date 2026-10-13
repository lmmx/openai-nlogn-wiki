import json, sys

SRC = open('/home/user/openai-nlogn-wiki/runs/P4/sources/paper.tex', encoding='utf-8').read()


def ev(q):
    return {"source": "paper", "quote": q}


def mot(text, source, quote=None):
    return {"text": text, "source": source, "quote": ev(quote) if quote else None}


def show(id, claim, method, motivation, children, page=None, frm=None, salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children}
    if page:
        n["page"] = page
    if frm:
        n["from"] = frm
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = adds
    return n


def infer(id, claim, quote, deferred=False, frm=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote)}
    if deferred:
        n["deferred"] = True
    if frm:
        n["from"] = frm
    return n


def sym(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


# ---------------------------------------------------------------- tools
stream_ops = show(
    "T1", "Splitting on a digit, applying a fixed pointwise map to aligned streams, merging, moving one digit, and splitting rows cyclically into $W$ streams each cost $O(V)$ steps on a fixed number of tapes, for an array of volume $V$.",
    "Split the array into streams according to the relevant digit or row class so that the streams share one address set in the same order, then scan the aligned entries once and merge.",
    mot("Splitting on a digit leaves every stream with the same remaining address set in the same order, so aligned scans suffice and each stream is read a fixed number of times.", "recoverable"),
    [infer("T1.1", "Splitting on one digit gives streams with the same remaining address set in the same order, so a fixed pointwise map can be applied to aligned entries and the results merged.",
           r"shows that splitting on one digit gives streams with the same remaining")],
    page="stream-ops",
    frm=["address-fields-volume", "multitape-model", "sets-products-of-ranges-and-lexicographic-order", "permutations-and-bijections"])

controlled_shifts = show(
    "T2", "A target field updated by $y\\mapsto y+a(\\text{controls})\\bmod Q$, with the controls earlier on the tape than the target, costs $O(V)$, and so does multiplication by a fixed rational unit modulo $q^b$.",
    "Fix the control prefix, cut the $Q$ blocks of the target fiber at the offset into two pieces and merge them in the opposite order; handle unit multiplication by splitting into increasing pieces.",
    mot("A cyclic shift of a fiber is a cut and a re-merge of two consecutive pieces, and the controls are already read before the target is reached, so one pass suffices.", "recoverable"),
    [infer("T2.1", "For a fixed offset, splitting the target blocks at $Q-a$ and merging the two pieces in the opposite order rotates the target coordinate in linear time.",
           r"For an offset $a\in[Q]$, split these blocks at $Q-a$.  Append the two")],
    page="controlled-shifts",
    frm=["stream-ops", "modular-arithmetic-and-residue-classes", "permutations-and-bijections"])

# ---------------------------------------------------------------- networks
n_scalar = show(
    "N1", "A fixed network of copy, gather, scatter and side-injection gates on banks $X$ and $Y$ sends $(X_a,Y_a)$ to $(-Y_a,X_a)$ in three stages and restores every scratch wire to its arbitrary initial value.",
    "In one forward invocation first subtract the effect of the old scratch values, then copy and gather the source, scatter and inject into the target, then undo copy and gather; use the intersection-size coefficients so that the unwanted ones cancel; compose a forward, an inverse and a forward invocation.",
    mot("Restoring scratch wires with arbitrary contents follows the transparent-computation pattern of subtracting the initial value, computing, adding back and reversing.", "explicit",
        r"This cancellation of arbitrary initial scratch values is a linear"),
    [infer("N1.1", "The net change of the target is independent of the initial scratch values, and the central and side coefficients combine to give $y\\gets y+x$.",
           r"Thus both net maps are $y\gets y+x$."),
     infer("N1.2", "A forward, an inverse and a forward invocation compose to the signed exchange $(x,y)\\mapsto(-y,x)$, restoring every invocation's scratch wires.",
           r"Starting from $(x,y)$, the three stages give")],
    page="scalar-exchange-network",
    frm=["linear-algebra-basics", "f2-vectors", "subset-pairing-formulas", "boolean-and-arithmetic-circuits-as-networks", "elementary-counting-and-the-union-bound"],
    salient="The exchange is exact for arbitrary initial scratch values: the net target change $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$ does not depend on them, and the intersection-one coefficients cancel exactly against the side wires.")

n_frames = show(
    "N2", "If each wire's scalar is replaced by an array and every gate and terminal carries an invertible frame operator, the network acts as $D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}$, so only the endpoint frames matter and each edge from $u$ to $v$ is implemented by $D_vD_u^{-1}$.",
    "Maintain the invariant that the stored array equals the frame applied to the logical array, and use that a common frame commutes with every pointwise linear gate.",
    mot("A pointwise linear gate combines arrays address by address while a frame mixes addresses within one array, so a frame shared by all wires of the gate passes through it.", "recoverable"),
    [infer("N2.1", "The common frame commutes with the pointwise gate, so the invariant continues from the sources to the sinks.",
           r"Thus the common frame commutes with the pointwise gate, and")],
    page="network-frames",
    frm=["scalar-exchange-network", "linear-algebra-basics"],
    salient="The intermediate frames cancel completely: the operator on every route, including the auxiliary scratch roles, depends only on the source and sink frames, so the intermediate frames can be chosen to make each edge cheap.")

n_labels = show(
    "N3", "Gates and terminals can be labelled by nested nondegenerate subspaces of the $m$-dimensional space $\\mathcal F=F^{\\otimes 3}$, built from tensor powers of triple indicator vectors, so that the total dimension change over the edges of a network with $W$ wires is below $W\\cdot m$.",
    "Label the data wires stage by stage with tensor products of triple lines and their orthogonal complements, order the gates so that every decrease is confined to the central wires' return, and count residual dimensions edge by edge.",
    mot("The cost of an edge will be its dimension change, so the labels must keep the total dimension lost on decreasing edges small relative to the number of data banks.", "explicit",
        r"The saving will come from keeping the total dimension lost on decreasing"),
    [infer("N3.1", "Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$.",
           r"Every edge joins comparable nondegenerate labels.  The only decreasing"),
     infer("N3.2", "The loss ratios $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$ are below $1/2$, which leaves a strict saving once the extra source ranks are counted.",
           r"In particular, both are smaller than $1/2$.")],
    page="subspace-labels-rank-saving",
    frm=["subset-pairing-formulas", "network-frames", "tensor-products", "bilinear-orthogonality", "f2-vectors", "linear-algebra-basics"],
    salient="The total number of smaller calls is strictly below $W\\cdot m$, although the network moves a full $m$-dimensional label on every wire: only the central wires ever lose dimension, and their total loss $L$ stays below half of the number $N$ of data banks.")

n_bit = show(
    "N4", "The bit network with $W_{\\rm b}$ XOR-gate wires and rational projection matrices on gates and terminals sends its input to the role-permuted vector, obeys $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m$ for every input role $w$, and has total edge rank $s_{\\rm b}<W_{\\rm b}m$.",
    "Assign the projection $P_U$ onto each label to the gates and sinks and $-P_{U_a}$ to the source of $X_a$; edge differences are projections onto residuals, whose rank is the dimension change.",
    mot("The tape application needs, on every role, the same address shear $H\\gets H+D$ as endpoint operator, and edges whose matrices differ by a low-rank projection are the cheap ones.", "recoverable"),
    [infer("N4.1", "The rank sum falls short of $W_{\\rm b}m$ by $N-2L_{\\rm b}>0$.",
           r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$."),
     infer("N4.2", "For an input $X_a$ the endpoint difference is $P_{U_a^\\perp}-(-P_{U_a})=I_m$, and every other role has zero source matrix and identity sink matrix.",
           r"For an input $X_a$ the endpoint difference is")],
    page="bit-network-interface",
    frm=["subspace-labels-rank-saving", "network-frames", "address-shear"],
    salient="The endpoint matrix difference is the same identity on every role, including the scratch roles whose contents are arbitrary, so one shear is applied uniformly to all role streams.")

n_cplx = show(
    "N5", "In the Gaussian-dyadic network with binary-vector labels and phase frames $i^{\\mathrm{wt}(P_Ux)\\bmod 4}$, each edge's frame change is a product of translation kernels $aI+bX_v$ over an orthonormal basis of the residual, the lengths sum to $s_{\\rm c}<W_{\\rm c}m$, and telescoping gives $C^{\\otimes m}$ on every role.",
    "Use that Hamming weight is additive modulo four on orthogonal vectors to turn each frame difference into one kernel per basis vector, then telescope the frames and fix the one exceptional pair of roles with $C=iZC^{-1}Z$.",
    mot("Over $\\mathbb F_2$ the residuals have orthonormal bases, and a norm-one vector has odd weight, so its phase factor is a single two-point kernel or its inverse.", "recoverable"),
    [infer("N5.1", "Each residual vector contributes one kernel factor acting on all columns, and there are $s_{\\rm c}$ such factors over the network.",
           r"Thus each residual vector contributes one factor acting on all $k$"),
     infer("N5.2", "The identity $C=iZC^{-1}Z$ turns the $27k$ inverse factors on the pair $X_a\\to Y_a$ into forward ones.",
           r"Put $Z=\operatorname{diag}(1,-1)$.  Direct multiplication gives"),
     infer("N5.3", "After undoing the bank exchange and the sign, every role, including every scratch role, carries the required forward tensor product.",
           r"Every role, including every scratch role, now has")],
    page="complex-network-interface",
    frm=["subspace-labels-rank-saving", "network-frames", "phase-kernel", "f2-vectors", "bilinear-orthogonality", "complex-numbers"],
    salient="Every role, even the pair $X_a\\to Y_a$ whose phase frame differs, ends with exactly the same operator $C^{\\otimes m}$ because the sign corrections turn each inverse kernel into a forward one.")

n_block = show(
    "N", "There are two fixed linear networks, one over bits and one over Gaussian dyadics, that exchange two banks of values while restoring every scratch wire, and whose array versions have total frame-change rank $s$ strictly below $W\\cdot m$ for $W$ wires and an $m$-dimensional label space.",
    "Build the scalar exchange network first, lift it to arrays with frames, then choose nested subspace labels that make the frame changes cheap, and read off the bit and complex interfaces.",
    mot("The scalar network already has the required signed exchange, so what remains is to choose the intermediate frames so that each edge costs few smaller calls; the representation invariant is explained before the labels.", "explicit",
        r"before constructing the subspace labels that make changes of representation"),
    [n_scalar, n_frames, n_labels, n_bit, n_cplx,
     infer("N6", "The relative rank deficits of both networks exceed $20\\cdot 2^{-50}$, so $s/W<m^\\tau$ holds with the fixed exponent $\\tau=1-2^{-50}$.",
           r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$.")],
    adds=[sym("W", "wire count", "The number of wires of the fixed network, including its scratch wires.", "count"),
          sym("m", "label dimension", "The dimension of the fixed label space on which subspace labels live."),
          sym("s", "total edge rank", "The sum over all edges of the rank of the frame change, equal to the number of smaller calls.", "count")])

# ---------------------------------------------------------------- chunk swap
lower_fact = show(
    "C1.1.1", "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation matrix with exactly $a$ ones.",
    "Eliminate pivot by pivot, taking the topmost nonzero row and its rightmost nonzero entry, clearing with lower triangular elementary matrices, and repeat on the remaining active indices.",
    mot("Lower triangular changes of coordinates are exactly those that can be applied as controlled shifts in tape order, so the elimination is done in the order that keeps factors lower triangular.", "recoverable"),
    [infer("C1.1.1.1", "Each pivot step isolates a rank-one block using lower triangular elementary operations, leaving a partial permutation with exactly $a$ ones.",
           r"If $A=0$, take $E_1=E_2=I$ and $\Pi=0$.  Otherwise choose the topmost")],
    page="lower-factorization",
    frm=["linear-algebra-basics"])

matrix_shear = show(
    "C1.1.2", "The shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ with a rational matrix $A$ of rank $a$ is performed with exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work.",
    "Factor $A=E_1\\Pi E_2$, apply the triangular factors as linear-time controlled shifts, and realize each pivot $H_i\\leftarrow H_i+D_j$ by two controlled shifts around one interchange.",
    mot("Controlled shifts update a later field from earlier fields in linear time, and lower triangular coordinate changes can be done entirely in this direction.", "explicit",
        r"earlier fields in linear time.  Lower triangular changes of coordinates"),
    [lower_fact,
     infer("C1.1.2.1", "First transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, then add $\\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$.",
           r"For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,"),
     infer("C1.1.2.2", "Each pivot costs one interchange between an $H$ field and a $D$ field, and there are $a$ pivots.",
           r"It uses just one interchange.  There are $a$ ones, which proves the")],
    page="matrix-shear-cost",
    frm=["lower-factorization", "address-shear", "controlled-shifts"])

row_split = show(
    "C1.1.3", "Whole rows can be dealt cyclically into $W$ role streams, with the row count padded per prefix to a multiple of $W$, so that each stream has volume $V/W$ and the same remaining shape and gates act pointwise on matching addresses.",
    "Write the row number as $r=Wg+(w-1)$ and send the whole row to stream $w$, indexed there by $g$.",
    mot("A pointwise gate needs its touched roles to have one common address set, which holds when every stream has exactly the same shape.", "recoverable"),
    [infer("C1.1.3.1", "Splitting whole rows cyclically gives $W$ streams of the same remaining shape, each of logical volume $V/W$.",
           r"Split whole rows cyclically into $W$ role streams within each prefix")],
    page="row-splitting-roles",
    frm=["stream-ops", "scalar-exchange-network", "network-frames"])

rank_rec = show(
    "C1.1.4", "If a call at width $e=mf$ makes $s$ calls at width $f$, each on a stream of volume $V/W$, then the normalized cost satisfies $F_k\\le(s/W)F_{k-1}+O(1)$, and since $s/W<m^\\tau$ with $\\tau<1$ this solves to $F_k=O(e^\\tau)$.",
    "Divide the cost by the volume to get a recurrence with ratio $s/W$ and sum the resulting geometric series.",
    mot("Dividing by the volume turns the $s$ calls on streams of volume $V/W$ into a factor $s/W$, so the solution is controlled by whether $s/W$ is below $m$.", "recoverable"),
    [infer("C1.1.4.1", "For $a=s/W<m^\\tau$ the geometric sum $\\sum_{j\\le k}a^j$ is $O(m^{k\\tau})$, hence $F_k=O(e^\\tau)$.",
           r"For $a=s/W<m^\tau$ the geometric sum")],
    page="rank-deficit-recurrence",
    frm=["subspace-labels-rank-saving", "big-o", "recurrences-and-geometric-series"],
    salient="A strict inequality $s<Wm$ that is tiny in relative terms (of order $10^{-14}$) already gives a power saving $e^{\\tau}$ with $\\tau=1-2^{-50}<1$, because the saving compounds over the $\\log_m e$ levels of the recursion.")

dfs_sched = show(
    "C1.1.5", "Recursive calls on $W$ role streams can be run on one fixed set of tapes by parking the inactive streams on a stack, copying the active stream to the child and restoring afterwards, at cost $O(V)$ per node.",
    "Keep reusable work tapes empty at call boundaries, push the $W-1$ inactive streams on a parking stack and the call descriptor on a second stack, and reverse these operations on return.",
    mot("The network has a fixed but large number of roles, yet the machine may only have a fixed number of tapes, so recursion must reuse the same tapes at every depth.", "recoverable"),
    [infer("C1.1.5.1", "Before a recursive call the inactive role streams are pushed to the parking stack and the active stream is copied to the child's input area.",
           r"Before a recursive call, append the $W-1$ inactive role streams to the"),
     infer("C1.1.5.2", "Each push, pop, copy and erasure moves $O(V)$ symbols at a parent node, and there are only a fixed number $s$ of child calls.",
           r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$")],
    page="fixed-tape-dfs-schedule",
    frm=["stacks-and-recursion", "stream-ops", "multitape-model"])

power_width = show(
    "C1.1", "Two disjoint chunks of $e=m^k$ radix-$q$ digits each can be interchanged in $O(Ve^\\tau)$ time, provided a preceding row field has length divisible by $W^k$.",
    "Perform the interchange as the three shears $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$ and run the middle shear through the bit network on $W$ role streams, applying an address shear to every edge by recursive smaller interchanges.",
    mot("An edge matrix of rank $a$ needs only $a$ smaller interchanges and the total rank is below the number of wires times $m$, so the recurrence saves a power of the chunk width.", "explicit",
        r"Because the sum of these ranks is less than the number of wires times"),
    [matrix_shear, row_split,
     infer("C1.1.a", "On every circuit edge apply the address shear $\\Phi_{A_e}$ to that role stream, and execute every gate pointwise; the endpoint matrices then give $H\\leftarrow H+D$ on every row.",
           r"On every circuit edge apply"),
     infer("C1.1.b", "Two further updates that target the later group, $D\\leftarrow D-H$ and $D\\leftarrow H-D$, complete the interchange of the two full chunks around the shear.",
           r"To interchange the two full chunks, perform"),
     rank_rec, dfs_sched],
    page="power-width-interchange",
    frm=["bit-network-interface", "matrix-shear-cost", "row-splitting-roles", "rank-deficit-recurrence", "fixed-tape-dfs-schedule", "address-shear", "network-frames"],
    salient="Although the intermediate steps form XOR combinations of data, the net effect is an exact permutation, and it is exact for arbitrary initial contents of the scratch role streams.",
    adds=[sym("e", "chunk width", "The number of radix-$q$ digits in each of the two chunks, a power of $m$.", "count")])

chunk_swap = show(
    "C1", "There is a fixed $\\tau<1$ and one fixed multitape procedure that interchanges two disjoint address chunks of $u$ bits, $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$, in $O(Vu^\\tau)$ steps on an arbitrary bit array of volume $V$.",
    "Peel off the top digits of both chunks to supply rows, pad the rows to a multiple of $W^k$, decompose the remaining width in base $m$ and apply the power-width interchange to each piece, then remove padding and reverse the high-digit moves.",
    mot("The power-width interchange needs a row field divisible by a power of $W$ and a power-of-$m$ width, and a general array can supply the rows from a few of its own high digits.", "explicit",
        r"Rows for a general array can be supplied by a few of its own high digits."),
    [power_width,
     infer("C1.2", "Write each chunk as its top $\\rho$ digits followed by the rest, exchange and join the high parts to form a row field of range at least $W^k$, and pad the rows.",
           r"Write each chunk as its top $\rho$ digits followed by its remaining"),
     infer("C1.3", "Write the remaining width in base $m$ and apply the power-width interchange to the corresponding pieces; the costs form a geometric sum $O(Ve^\\tau)$.",
           r"Write the remaining width in base $m$:"),
     infer("C1.4", "For binary chunks pad each range from $[2^u]$ to $[q^e]$ and scan the padding away afterwards, which gives the bound $O(Vu^\\tau)$.",
           r"Finally, for binary chunks let $e$ be the least integer with")],
    page="chunk-swap",
    frm=["power-width-interchange", "stream-ops", "address-fields-volume", "sorting-and-radix-sort"])

# ---------------------------------------------------------------- butterfly layer
packed_rot = show(
    "L1.3.1", "Eight cyclic shifts of whole chunk ranges, conditioned on parities and a control bit $c$, flip the parity of $u$ when $c=1$ and restore the auxiliary integer $w$, so XORs on $f$ selected bit positions can be done at once whenever the $K$-bit segments have unused guard room.",
    "Compose two three-cycles on the parity pairs $(u,w)$ into a transposition, and realize each of the eight lines for all $f-1$ segment pairs simultaneously as one cyclic shift of the target chunk.",
    mot("A cyclic shift of a whole chunk range by an offset taken from the other chunks is linear in volume and acts on all segments at once, provided no segment carries into the next.", "recoverable"),
    [infer("L1.3.1.1", "For $c=1$ the first four operations induce the cycle $(00\\ 01\\ 10)$ and the last four induce $(01\\ 10\\ 11)$ on parity pairs; together they flip the parity of $u$ and fix $w$.",
           r"If $c=0$, these operations do nothing. If $c=1$, the first four operations"),
     infer("L1.3.1.2", "Each line applied to all segment pairs together is a single cyclic shift of one chunk by an offset depending only on the other two chunks.",
           r"Apply each line of \eqref{eq:eight-packed-additions} simultaneously to all")],
    page="packed-rotations",
    frm=["controlled-shifts", "chunk-swap"],
    salient="The auxiliary integer $w$ is restored for every initial value, because the net permutation of parity pairs is $(00\\ 10)(01\\ 11)$ and the quotients under division by two are preserved.")

exc_repair = show(
    "L1.3.2", "The packed rotations fail only on a set $\\mathcal B$ of addresses whose guard values lie near a segment boundary, a fraction at most $80(f-1)2^{-K}$ of all addresses; extracting these records, sorting them by destination rank with a stable radix sort and reinserting them repairs the result in the worst case.",
    "Bound the exceptional set by a union bound over the guards, observe that the ideal map and the rotations are bijections that agree off the set, then compute each exceptional record's destination, sort and reinsert.",
    mot("The exceptional set is defined by addresses alone and is a tiny fraction of them, so handling it by a deterministic sort costs little and keeps the bound worst-case over all payloads.", "recoverable"),
    [infer("L1.3.2.1", "The bad set $\\mathcal B$ consists of the addresses at which some guard value leaves the interval $[10,2^{K-1}-11]$.",
           r"Let $\mathcal B$ consist of the addresses for which"),
     infer("L1.3.2.2", "Twenty values are excluded for each guard, so a union bound over the $2(f-1)$ guards bounds the bad fraction independently of the records.",
           r"There are exactly twenty excluded values for each guard in"),
     infer("L1.3.2.3", "Stable binary radix sorting of the extracted records by destination rank, followed by one forward scan that reinserts them, implements the ideal map on $\\mathcal B$.",
           r"while stable binary radix sorting scans only the extracted records and")],
    page="exceptional-address-repair",
    frm=["packed-rotations", "stream-ops", "sorting-and-radix-sort", "elementary-counting-and-the-union-bound"],
    salient="The bad fraction $80(f-1)2^{-K}$ is tiny because $K$ grows faster than $\\log p$, so the repair costs only a negligible term although it is executed deterministically.")

packed_add = show(
    "L1.3", "One fixed multitape procedure XORs the selected bit at offset $\\rho$ of each of the $f$ chunks of $K$ bits of chunk $x$ into chunk $y$ while restoring chunk $z$, in time $O(V(L^\\tau+1))$ plus negligible repair terms.",
    "Apply the eight packed rotations, each as a chunk interchange, a controlled shift and the undoing interchange, then repair the exceptional addresses deterministically, and finish with the top selected position by a direct two-bit XOR.",
    mot("A constant number of shifts of whole chunk ranges is cheap, and the places where they misbehave are an explicitly bounded set of addresses, which can be corrected without depending on the payload.", "explicit",
        r"addresses. The correction depends only on addresses, so the time bound is"),
    [packed_rot, exc_repair,
     infer("L1.3.3", "The omitted most significant selected position is handled by a two-bit XOR, and the movement costs $O(V(L^\\tau+1))$ with all counters and cleanup included.",
           r"Finally apply the two-bit XOR to $x_{j_{f-1}},y_{j_{f-1}}$ by"),
     infer("L1.3.4", "The total is $O(V(L^\\tau+1))$ plus the descriptor and repair terms, which vanish after division by the volume.",
           r"The movement costs $O(V(L^\tau+1))$.")],
    page="packed-selected-bit-addition",
    frm=["packed-rotations", "exceptional-address-repair", "chunk-swap"])

phase_layer = show(
    "L1", "To apply $C^{\\otimes e}$ on $e=mf$ selected bits, group them into $m$ slots of $f$ chunks, change the binary basis by packed row additions, apply the $f$-fold forward child on each of the $s_{\\rm c}$ residual-basis slots, and change back; inverse children cost no extra call because $C^{-1}=-iZCZ$.",
    "Write each edge's frame change as $\\mathcal P_M\\bigl(\\prod_j C_{e_j}^{\\epsilon_j}\\bigr)\\mathcal P_M^{-1}$, implement the invertible matrix $M$ by elementary row additions on corresponding bits of whole slots, and recurse on the slots.",
    mot("A residual basis need not be the standard basis, but any basis can be moved to the first coordinates by an invertible change of variables, and a row addition acts on corresponding selected bits of whole slots.", "recoverable"),
    [infer("L1.1", "Conjugating by the address permutation $\\mathcal P_M$ turns each edge's frame change into a product of kernels on standard coordinates, one child on the $f$ axes of slot $h$ per basis vector.",
           r"To implement \eqref{eq:phase-edge-coordinate} on the group, first apply"),
     infer("L1.2", "Summing the residual dimensions gives exactly $s_{\\rm c}$ child calls, each on $f=e/m$ axes, and the corrections add no further child.",
           r"Apply the finite network with these column frames to a group of"),
     infer("L1.2b", "On all selected coordinates the identities for $C$ give $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$, which returns the layer to normalized butterflies exactly.",
           r"\eqref{eq:phase-basic-identities} on all selected coordinates gives"),
     packed_add,
     infer("L1.4", "The complete change of basis and its inverse cost $O(V((eK)^\\tau+1))$ on a stream of volume $V$.",
           r"the complete change of basis and its inverse therefore cost")],
    page="phase-frame-layer",
    frm=["complex-network-interface", "phase-kernel", "packed-selected-bit-addition", "f2-vectors"],
    salient="Each inverse kernel costs one forward child, not an extra call, since $C^{-1}=-iZCZ$ differs from $C$ only by sign and phase wrappers; the number of children is exactly the rank sum $s_{\\rm c}$.")

guard_w = show(
    "L3", "The whole recursive $C$-layer is evaluated exactly with $p+\\Delta$ fractional bits and $\\Delta+3$ integer bits, where $\\Delta=\\lceil C_0d^{C_1}\\rceil$ bounds the arithmetic depth through $A(e)\\le sA(e/m)+E$; since $\\epsilon C_1<1$, $\\Delta=o(p)$ and all widths stay $O(p)$.",
    "Bound the longest chain of additions, halvings and sign changes from input to intermediate coefficient by a recurrence, then turn the depth into bounds on denominator and magnitude growth.",
    mot("The accelerated network is evaluated exactly and its intermediate operators need not be contractions, so exact representation needs explicit bounds on growth within one layer.", "explicit",
        r"The accelerated network is evaluated exactly until an entire"),
    [infer("L3.1", "The paired kernel evaluation uses at most eight elementary operations, which starts the depth recurrence $A(e)\\le sA(e/m)+E$ with $A(e)\\le 8e$ at leaves.",
           r"The paired evaluation in \eqref{eq:individual-C-pair} uses at most"),
     infer("L3.2", "A value at depth $\\ell$ lies in $2^{-(p+\\ell)}\\mathbb Z[i]$ with modulus at most $2^\\ell$, so reserving $p+\\Delta$ fractional and $\\Delta+3$ integer bits represents everything exactly.",
           r"To see how this count controls numerical size, start with disk-valued"),
     infer("L3.3", "Choosing $\\epsilon C_1<1$ with $d=\\Theta(p^\\epsilon)$ gives $\\Delta=o(p)$, so the full coefficient width is $O(p)$.",
           r"Choose \(\epsilon C_1<1\).  Since \(d=\Theta(p^\epsilon)\),")],
    page="guard-width",
    frm=["fixed-point-arithmetic", "complex-network-interface", "disk-grid-truncation", "rank-deficit-recurrence"])

simult = show(
    "L", "The normalized butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ can be applied at once to the same bit offset of $D\\le d$ address chunks of every polynomial record in $O(Vd^{\\lambda'})$ time with $\\lambda'<1$, exactly up to one final truncation.",
    "Write $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$, compute $C^{\\otimes D}$ by the recursive phase-frame layer on rows split among the wire roles, evaluate everything exactly with guard bits and truncate once at the end.",
    mot("Applying the $D$ butterfly factors one after another would need $D$ whole-array passes, whereas one pass through the recursive layer costs only a power of $D$.", "explicit",
        r"factors would require $D$ whole-array passes."),
    [phase_layer,
     infer("L2.1", "At an internal node with $e=m^k$ chunks the basis changes, scalar gates and reassembly cost $O(V((eK)^\\tau+1))$, with $s$ child calls on streams of volume $V/W$.",
           r"First consider an internal node containing \(e=m^k\) consecutive"),
     infer("L2.2", "The rows come from the first $q_0$ chunks, padded to a multiple of $W^{k_0}$; a row index $u=Wg+w$ sends the whole row to role $w$.",
           r"At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\),"),
     infer("L2.3", "With exponents $\\tau,\\sigma,\\lambda$ chosen so that $a=s/W<m^\\lambda$, the recurrence $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ sums to $O(e^\\lambda)$.",
           r"Fix \(\beta=1/2\), and choose real exponents satisfying"),
     infer("L2.4", "Splitting $D-q_0$ in base $m$ and adding the piece costs and the row preprocessing gives $O(d^{\\lambda'})$ per unit volume.",
           r"Adding their costs and the row preprocessing gives"),
     guard_w,
     infer("L4.1", "The phase-frame construction reduces a group of $e$ selected bits to $s_{\\rm c}$ children on $e/m$ bits, each with a $1/W_{\\rm c}$ share of the volume, and the packed procedure supplies the basis changes with a common time constant.",
           r"The phase-frame construction reduces a group of $e$ selected bits to"),
     infer("L4.2", "Every row of $\\mathcal H$ has absolute row sum one, so $\\mathcal H$ maps disk arrays to disk arrays and the single truncation has error below $\\sqrt2\\,2^{-p}$.",
           r"Finally, every row of $\mathcal H$ has")],
    page="simultaneous-layer",
    frm=["phase-frame-layer", "row-splitting-roles", "guard-width", "rank-deficit-recurrence", "fixed-tape-dfs-schedule", "disk-grid-truncation", "polynomial-ring-negacyclic", "fft-butterfly"])

g1 = show(
    "G1", "Two tape procedures exist for fixed exponents $\\tau,\\lambda'<1$: one interchanges two disjoint address chunks of $u$ bits in $O(Vu^\\tau)$ time, and one applies a normalized butterfly layer on up to $d$ address chunks in $O(Vd^{\\lambda'})$ time, where $V$ is the logical bit volume.",
    "Obtain both from one fixed linear network that exchanges two banks of values and restores every auxiliary value, whose edge frame changes are smaller calls of the same procedure; the strict inequality $s<Wm$ on their number gives a recursion with a power saving.",
    mot("After dividing cost by volume, multiplying the parameter by $m$ raises the recursive contribution by $s/W<m$, and this strict inequality is the source of the power saving.", "explicit",
        r"increases the recursive contribution by $s/W<m$. This strict inequality"),
    [stream_ops, controlled_shifts, n_block, chunk_swap, simult],
    adds=[sym("V", "logical volume", "The number of stored data bits of the array being processed, not counting work tapes.", "count"),
          sym("\\tau", "interchange exponent", "A fixed exponent below one in the cost $O(Vu^\\tau)$ of interchanging two address chunks."),
          sym("\\lambda'", "layer exponent", "A fixed exponent below one in the cost $O(Vd^{\\lambda'})$ of a simultaneous butterfly layer.")])

# ---------------------------------------------------------------- synthetic convolution
syn_tr = show(
    "H1", "The normalized transforms $F_t^\\pm$ over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ with synthetic roots $\\omega_t=y^{2r/t}$ are computed by radix-two butterflies plus monomial twiddles, and $F_t^+F_t^-=t^{-1}I$ even though the ring has zero divisors.",
    "Prove character cancellation directly by pairing summands, then compute the transform by the decimation-in-frequency recursion that halves the length at each level.",
    mot("The ring has zero divisors, so character sums cannot be evaluated by dividing by $\\omega_t^j-1$ and must be checked directly.", "explicit",
        r"The ring has zero divisors, so we verify character cancellation"),
    [infer("H1.1", "For $t\\nmid j$, shifting $k$ by $t/2^{v+1}$ permutes the summands and multiplies the sum by $y^{rj_0}=-1$, so the sum is zero.",
           r"Only the second case needs proof.  Write $j=2^v j_0$ with $j_0$ odd"),
     infer("H1.2", "A step pairs $z_k$ with $z_{k+t/2}$ by $H_0$, multiplies the second output by $\\omega_t^{-k}$ and recurses on both halves, computing $F_t^-$ in $\\log_2 t$ levels.",
           r"The length-one procedure is the identity.  For $t\geq2$, the")],
    page="synthetic-transform",
    frm=["synthetic-roots", "fft-butterfly", "multidim-dft", "polynomial-ring-negacyclic", "dft", "roots-of-unity"],
    salient="The identity $F_t^+F_t^-=t^{-1}I$ holds in a ring with zero divisors because each non-vanishing character sum pairs its terms into cancelling pairs, using that multiplication by $y^r=-1$ flips the sign and the additive group has no two-torsion.")

freq_ord = show(
    "H2", "The recursion writes frequency $j$ in slot $\\mathrm{rev}(j)$, the bit reversal of $j$; the forward procedure $B_tF_t^-$ keeps this order and the opposite procedure $F_t^+B_t^{-1}$ consumes it directly, so no sort is needed between the pointwise product and the inverse transform.",
    "Track the address bits level by level to identify the stored order, and run the recursion in reverse for the opposite transform.",
    mot("The reversed level is half the inverse of the forward level, so traversing the levels backwards undoes the forward transform up to the factor $1/t$ without moving frequency indices.", "recoverable"),
    [infer("H2.1", "After all $a$ rounds the named slots from high to low contain the frequency bits from low to high, so the entry $(F_t^-z)_j$ occupies slot $\\mathrm{rev}_a(j)$.",
           r"After all $a$ rounds, the named slots from high to low therefore"),
     infer("H2.2", "The opposite procedure processes the smaller branches first, applies the inverse monomial and then $H_0$; the composite with $B_tF_t^-$ is $2^{-a}I=I/t$.",
           r"The procedure consuming this stored order traverses the recursion in")],
    page="frequency-order",
    frm=["synthetic-transform"])

transf_layout = show(
    "H3", "A positional permutation $L$ moves chosen bit slots to a prefix and groups the remaining bits into $K$-bit chunks so that each transform round is a simultaneous butterfly layer; each transform costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error below $\\sqrt2\\,\\ell\\,2^{-p}$.",
    "Move the top slots of each axis to a prefix, interleave the remaining chunks of the axes by chunk interchanges so that equal chunk indices are adjacent, then run one simultaneous layer per round and individual butterflies on the prefix rounds.",
    mot("The simultaneous layer applies one butterfly to the same bit offset in consecutive chunks, so the participating axes' selected bits must be placed at a common offset in consecutive $K$-bit chunks.", "explicit",
        r"we must place the selected bits of the participating axes at a common"),
    [infer("H3.1", "The axis steps of one round group into a parallel butterfly followed by a single recordwise monomial multiplication $J_E$ whose exponent depends only on the address.",
           r"Consequently the individual axis steps may be grouped as a parallel"),
     infer("H3.2", "A list of at most $D(b+1)=O(dK)$ slots is moved to a prefix, leaving each axis as consecutive $K$-bit chunks.",
           r"Form a list of the slots to move to a prefix.  First list"),
     infer("H3.3", "Scanning the target positions and exchanging chunks reorders the axes' chunks using at most $Dq-1$ interchanges, costing $O(Tp\\,pK^{\\tau-1})$.",
           r"To obtain this order, scan its target positions from left to right."),
     infer("H3.4", "Each round on the remaining chunks is one call of the simultaneous layer, costing $O(Tp\\,d^{\\lambda'})$, hence $O(Tp\\,\\ell d^{\\lambda'})$ in total.",
           r"The simultaneous-layer procedure therefore applies at cost"),
     infer("H3.5", "The monomial $y^E$ is a split of the coefficient list into two pieces, a negation of the tail and a merge in the other order, costing $O(rp)$ per record.",
           r"To implement the monomial, write $E=er+s$ with $0\leq s<r$."),
     infer("H3.6", "Truncation commutes with the signed coefficient permutation, so one truncation after each exact round gives error below $\\sqrt2\\,\\ell\\,2^{-p}$ over at most $\\ell$ rounds.",
           r"Thus the actual forward call sequence returns exactly the result of")],
    page="transform-layout",
    frm=["simultaneous-layer", "chunk-swap", "synthetic-transform", "frequency-order", "disk-grid-truncation", "contraction-error-budget"])

signed_pack = show(
    "H4", "Two disk-grid polynomials in $\\mathcal R_r$ are multiplied exactly by evaluating their coefficients at $B_0=2^{4p}$ as signed integers, multiplying with the established integer multiplier, extracting centered coefficients, wrapping negacyclically and truncating, in $O(rp\\log(rp))$ time.",
    "Use signed Kronecker substitution: pack coefficients into fixed-width blocks of an integer, multiply four pairs of integers, and unpack with centered residues and a carry.",
    mot("The established multiplier multiplies integers, and a polynomial with small coefficients becomes an integer by evaluation at a large base so that the product's coefficients do not overlap.", "explicit",
        r"reduction is a signed form of Kronecker substitution; compare"),
    [infer("H4.1", "Each evaluation integer fits in $4pr$ bits, so four products of the evaluated real and imaginary parts are formed by the established multiplier and their signs restored.",
           r"shows that each magnitude fits in $4pr$ bits.  Multiply the four"),
     infer("H4.2", "Because every product coefficient has absolute value below $B_0/2$, the centered residue modulo $B_0$ identifies the next coefficient once the lower ones are removed.",
           r"After the lower coefficients have been removed from an evaluation,"),
     infer("H4.3", "The real and imaginary numerator streams $ac-be$ and $ae+bc$ are reduced modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$.",
           r"The real and imaginary numerator streams are respectively")],
    page="signed-packing",
    frm=["established-multiplier", "polynomial-ring-negacyclic", "disk-grid-truncation"])

syn_conv = show(
    "H", "Normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ over $\\mathcal R_r$ on disk-grid arrays is approximated with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
    "Apply the forward synthetic transform to both operands and keep their layout, multiply the corresponding length-$r$ records pointwise by signed packing, and apply the opposite transform, which consumes the same stored order.",
    mot("Pointwise multiplication commutes with the same record permutation applied to both operands, so the product can be formed in the retained order and handed directly to the opposite procedure.", "explicit",
        r"forward outputs in their retained order and pass that order directly"),
    [syn_tr, freq_ord, transf_layout, signed_pack,
     infer("H5", "Perform both forward transforms and retain their common $LB$ order, multiply the records by signed packing, apply the opposite procedure and scale exactly by $M=T/r$.",
           r"Perform both forward transforms and retain their common $LB$ order."),
     infer("H6", "The two forward errors, the product truncation and the opposite transform total less than $3\\delta+\\eta$ before the scaling by $M$, giving the stated error.",
           r"For the error estimate, put")],
    page="synthetic-convolution",
    frm=["transform-layout", "signed-packing", "cyclic-convolution", "frequency-order", "contraction-error-budget"],
    adds=[sym("r", "record length", "The number of complex coefficients in a polynomial record of the ring, a power of two.", "count")])

# ---------------------------------------------------------------- resampling
gauss = show(
    "I1", "For coprime lengths $s<t$ with $t/s-1>p/\\alpha^4$ there are contractions $A$ and $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, and algorithms approximating them with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$.",
    "Use the two Gaussian maps of Harvey and van der Hoeven with their exact identity and Neumann-series inverse estimate, choose $A$ and $B_0$ with the normalizations absorbed, and leave the two coordinate permutations in the identity.",
    mot("The usual implementation sorts twice on each coordinate, so leaving both permutations in the transform formula and computing the formula directly avoids executing them.", "explicit",
        r"coordinate. We retain both permutations in the transform formula and"),
    [infer("I1.1", "The Gaussian maps $\\mathsf S,\\mathsf T$, the selection $C$ and the diagonal $\\mathsf D$ give $\\mathsf T P_sF_s=P_tF_t\\mathsf S$ and $\\|N-I\\|<1/2$ for $N=C\\mathsf T\\mathsf D$.",
           r"The Gaussian resampling argument uses two maps"),
     infer("I1.2", "Applying the left inverse $\\mathsf D N^{-1}C$ of $\\mathsf T$ to the first identity gives $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ with both maps contractions.",
           r"Applying this left inverse to the first identity in"),
     infer("I1.3", "The ordered numerical maps of Harvey and van der Hoeven supply algorithms for $A$ and $B_0$ with the stated errors and times, using that $C$ selects an ordered subsequence.",
           r"Lemmas~4.8, 4.9 and 4.12 of")],
    page="gaussian-resampling",
    frm=["dft", "contraction-error-budget", "disk-grid-truncation"],
    salient="The two coordinate permutations $P_s$ and $P_t$ stay in the identity instead of being executed as sorts, which would cost $O(tp\\log t)$ per coordinate.")

tens_res = show(
    "I2", "Applying the resampling identity along each of $d$ axes of a padded power-of-two box gives $R F_{\\boldsymbol s}=2^\\gamma\\mathcal B_0 QF_{\\boldsymbol t}\\mathcal A$ with line-map cost $O(dTp^{3/2+\\delta}\\alpha)$ and data movement $O(Tp\\,d^2(1+\\ell^\\tau))$.",
    "Tensor the one-dimensional identity, expand and compress one axis at a time on lines whose other coordinates are valid, and expose and restore each axis by adjacent chunk interchanges.",
    mot("The one-dimensional maps act on a single coordinate line, so the axes must be brought to the innermost address field one at a time, and the chunk interchange supplies that movement.", "explicit",
        r"line at a time. The chunk-swap algorithm supplies the movement of the"),
    [infer("I2.1", "Tensoring the one-dimensional identity proves the identity for $d$ axes, and the box is expanded by padding with zeros outside the valid source coordinates.",
           r"Tensoring \eqref{eq:no-sort-one-dimensional} proves"),
     infer("I2.2", "Moving an axis past its neighbor is an interchange of equal-width address fields (after peeling one extra bit), costing $O(Tp(1+\\ell^\\tau))$, and $O(d^2)$ of them expose and restore all axes.",
           r"To move an axis past its neighbor, interchange their"),
     infer("I2.3", "At most $2dT/r$ lines are processed, so per-line setup of fixed polynomial degree in $p$ is $o(Tp)$.",
           r"Since $t_i\geq r/2$, each tensor map invokes at most")],
    page="tensor-resampling",
    frm=["gaussian-resampling", "multidim-dft", "chunk-swap", "address-fields-volume"])

bluestein = show(
    "I3", "For the chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$ one has $QF_{\\boldsymbol t}u=\\overline a\\cdot\\bigl(a*(\\overline a\\cdot u)\\bigr)/T$, so the middle transform with its frequency permutation is a normalized cyclic convolution between two phase products.",
    "Compare the coefficient of $u_{\\boldsymbol k}$ on both sides, using that the chirp has period $t_i$ in coordinate $i$.",
    mot("Completing the square $-s(j-k)^2+sj^2+sk^2$ in the exponent turns the frequency product $jk$ into a convolution, and the permutation $Q$ is absorbed by the chirp.", "reconstructed"),
    [infer("I3.1", "The coefficient of $u_{\\boldsymbol k}$ on the right equals $T^{-1}\\exp(2\\pi i\\sum_i s_ij_ik_i/t_i)$, which is the coefficient in $QF_{\\boldsymbol t}$.",
           r"The coefficient of $u_{\boldsymbol k}$ in the right side of")],
    page="bluestein-chirp",
    frm=["cyclic-convolution", "multidim-dft"])

src_perm = show(
    "I4", "The retained source permutation $R$ cancels across the two forward source transforms, their pointwise product and the opposite-sign transform: $(RF_{\\boldsymbol s}^+)\\bigl[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)\\bigr]=(u*v)/S^2$.",
    "Show $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$ by substituting a dilation in the Fourier sum, move $R$ through the pointwise product, and then use the normalized convolution theorem.",
    mot("A coordinate dilation by a unit can be moved across a Fourier sum, and a coordinate permutation commutes with pointwise products, so the permutation appears twice and cancels.", "recoverable"),
    [infer("I4.1", "Substituting $h=ck$ in the Fourier sum gives $F_q^+R_c=R_c^{-1}F_q^+$, hence $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$.",
           r"For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$. Substituting $h=ck$"),
     infer("I4.2", "The normalized convolution rule $F_{\\boldsymbol s}(u*v)=S(F_{\\boldsymbol s}u)\\cdot(F_{\\boldsymbol s}v)$ and $F_{\\boldsymbol s}^+F_{\\boldsymbol s}=I/S$ give the factor $S^{-2}$.",
           r"The normalized convolution rule is")],
    page="source-permutation-cancel",
    frm=["gaussian-resampling", "cyclic-convolution", "multidim-dft"],
    salient="The permutation $R$ appears once in each forward transform and once in the opposite transform, so the three occurrences cancel in pairs and no sort of the source coordinates is ever needed.")

g3 = show(
    "G3", "Fourier transforms of pairwise coprime lengths $s_i$ can be replaced by transforms of power-of-two lengths $t_i$ using Gaussian resampling, with the source and target permutations retained in the identity and the middle transform computed as a chirp convolution.",
    "Apply Gaussian resampling along each axis with both coordinate permutations kept inside the transform identity, evaluate the middle transform by Bluestein's chirp as a cyclic convolution, and cancel the source permutation across the convolution.",
    mot("The usual implementation sorts twice on each coordinate, which would cost a full extra movement per axis, so the permutations are kept in the identity and compute the formula directly.", "explicit",
        r"coordinate. We retain both permutations in the transform formula and"),
    [gauss, tens_res, bluestein, src_perm])

# ---------------------------------------------------------------- assembly
par = show(
    "A1", "From the input length $n$, the choices $b=\\lceil\\log_2 n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, a power of two $T\\in[4n/b,8n/b)$ and axis lengths $t_i\\in\\{r/2,r\\}$ with $\\prod t_i=T$ give $Tp=\\Theta(n)$ and satisfy every hypothesis of the layer, transform and resampling interfaces.",
    "Fix all exponents as tiny explicit rationals, derive the sizes from $n$ by exact comparisons, and check the hypotheses of the interfaces with explicit inequalities.",
    mot("The constants are chosen conservatively so that every hypothesis of the interfaces holds with room to spare and no optimization is attempted.", "explicit",
        r"These constants are deliberately conservative; no optimization is claimed."),
    [infer("A1.1", "The exponents are the fixed rationals $\\tau=\\sigma=1-2^{-50}$, $\\delta=1/16$, $\\lambda=1-2^{-52}$, $c=2^{-56}$, $\\lambda'=1-2^{-54}$, $C_1=20$, $\\epsilon=2^{-75}$ and $\\kappa=2^{-182}$.",
           r"Take the following fixed rational numbers:"),
     infer("A1.2", "After counting the input bits, put $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$ and $K=\\lfloor d^c\\rfloor$, and take the power of two $T$ in $[4n/b,8n/b)$.",
           r"After obtaining $n$, compute the size parameters below with the"),
     infer("A1.3", "The comparison constants can be fixed for every input length at once, giving $Tp=\\Theta(n)$ and $d=\\Theta(p^\\epsilon)$.",
           r"The comparison constants can be fixed for every input length at once."),
     infer("A1.4", "With $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$ one gets $2\\le\\alpha<\\sqrt p$ and $\\gamma=2d\\alpha^2=o(b)$ eventually.",
           r"It follows that $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$.")],
    page="parameter-choice",
    frm=["multiplication-as-convolution", "polynomial-ring-negacyclic", "gaussian-resampling", "simultaneous-layer"],
    salient="Every exponent is astronomically small, for example $\\epsilon=2^{-75}$ and $\\kappa=2^{-182}$, because all the constraints between the exponents must hold at once with strict inequalities.")

primes = show(
    "A2", "Pairwise-distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ are found by trial division in $n^{o(1)}$ time; they give $\\gcd(s_i,t_i)=1$, $T/2<S<T$ for $S=\\prod s_i$ and the separation $t_i/s_i-1>\\eta$ needed by Gaussian resampling.",
    "Cite the prime-counting lemma for intervals, check that both intervals contain more than $d$ primes, apply Bernoulli's inequality to the product, and search the intervals deterministically.",
    mot("The product of the source lengths must fill a fixed fraction of the padded box while each ratio $t_i/s_i$ stays separated from one, so each $s_i$ is taken just below its power of two.", "explicit",
        r"The distinct prime lengths $s_i$ must be close to the powers of two"),
    [infer("A2.1", "The prime-interval lemma gives more than $d$ primes in each of the two intervals once $\\log x>8d$.",
           r"The prime-interval result"),
     infer("A2.2", "Every $\\gcd(s_i,t_i)$ equals one because $t_i$ is a power of two.",
           r"Every $\gcd(s_i,t_i)$ equals one because $t_i$ is a power of two."),
     infer("A2.3", "The machine finds the primes by scanning the intervals and testing candidates by trial division, in time $n^{o(1)}$.",
           r"The machine finds these primes by scanning the two intervals")],
    page="prime-lengths",
    frm=["parameter-choice", "gaussian-resampling", "crt-address-map", "divisibility-primes-and-gcd"])

digits = infer("A3", "Writing each input as a polynomial in $2^b$ with $q=\\lceil n/b\\rceil$ digits makes the product a non-wrapping convolution modulo $x^S-1$ with coefficients below $2^{3b}$.",
               r"Write the two inputs as polynomials in $2^b$, each with",
               frm=["multiplication-as-convolution", "binary-and-radix-b-representation-of-integers"])

crt = show(
    "A4", "With pairwise coprime $s_i$ the map $x\\mapsto\\prod_i x_i^{\\mu_i}$, $\\mu_i=P_i^{-1}\\bmod s_i$, is an isomorphism from cyclic convolution of length $S=\\prod_i s_i$ to multidimensional cyclic convolution on the prime axes, implemented by triangular controlled shifts on padded axes in $O(Tp\\,d^2(1+\\ell^\\tau))$.",
    "Use the Chinese-remainder split of Agarwal and Cooley with prefix products inverted, so that the coordinate of axis $i$ depends only on lower-index digits and the change of order is a sequence of controlled cyclic shifts.",
    mot("Choosing coordinate powers as inverses of prefix products makes the change of order triangular, so every target is shifted by amounts determined by controls that precede it on tape.", "explicit",
        r"algebraic split, with coordinate powers that make the change of order a"),
    [infer("A4.1", "The assignment $x\\mapsto\\prod_ix_i^{\\mu_i}$ respects $x^S=1$, so it defines an algebra map, and it is an isomorphism preserving cyclic convolution.",
           r"respects $x^S=1$, so it defines an algebra map."),
     infer("A4.2", "After reordering the padded axes to $(a_1,\\ldots,a_d)$ the targets are updated from $i=d$ down to $1$, each by a rotation of the valid interval.",
           r"Now reorder the complete padded axes to $(a_1,\ldots,a_d)$.  In this"),
     infer("A4.3", "Each triangular update is a prefix-controlled cyclic shift, with offsets set up for at most $T/t_i$ control prefixes.",
           r"Each triangular update is a prefix-controlled cyclic shift.  The"),
     infer("A4.4", "Reversing all axes uses $O(d^2)$ equal-width chunk interchanges, so the map, its inverse and the padding cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
           r"uses $O(d^2)$ such moves.  Therefore the map $\Phi$, its inverse, and")],
    page="crt-address-map",
    frm=["cyclic-convolution", "multidim-dft", "controlled-shifts", "chunk-swap", "modular-arithmetic-and-residue-classes"],
    salient="Because the coordinate of axis $i$ depends only on the digits below it, the CRT reorder is lower triangular, so it runs as linear-time controlled shifts rather than as a general sort.")

twist = show(
    "A5", "The isomorphism $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ sends cyclic convolution of length $r$ to the ring modulo $y^r+1$ by multiplying coefficient $k$ by $\\zeta^k$; the negative wrap cancels the factor $\\zeta^r$, so untwisting recovers the cyclic result.",
    "Check well-definedness and invertibility of the diagonal twist on bases, and verify directly that terms that wrap around pick up $(-1)\\cdot\\zeta^r=1$.",
    mot("A cyclic wrap multiplies by one and a negacyclic wrap by $-1$, and a twist by an $r$th root of $-1$ exchanges the two.", "recoverable"),
    [infer("A5.1", "The map is well defined since $(\\zeta y)^r=(-1)(-1)=1$, and it is diagonal on the monomial bases with nonzero entries $\\zeta^k$, hence an isomorphism.",
           r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."),
     infer("A5.2", "For $k+l=j+hr$ a product term after twisting and negacyclic reduction has factor $\\zeta^{k+l}(-1)^h=\\zeta^j$.",
           r"For an explicit check on the wrap, write $k+l=j+hr$, where"),
     infer("A5.3", "Untwisting therefore recovers the cyclic coefficient with the correct sign.",
           r"Untwisting therefore recovers the cyclic coefficient with the correct")],
    page="coefficient-twist",
    frm=["polynomial-ring-negacyclic", "cyclic-convolution", "complex-numbers", "roots-of-unity"],
    salient="The negative sign of the wrap exactly cancels the factor $\\zeta^r=-1$ picked up by wrapped terms, so the twist converts a cyclic convolution into a negacyclic one without changing the result.")

chirp_t = show(
    "A6", "The padded power-of-two transform $QF_{\\boldsymbol t}$ is computed by a chirp phase product, a complex cyclic convolution obtained through the coefficient twist and the synthetic convolution, and a final chirp product, with error below $8TL\\,2^{-p}$.",
    "Compose the Bluestein identity with the computed complex convolution, evaluating chirps by exponential routines and truncating after each phase product.",
    mot("The chirp identity expresses the middle transform as a normalized cyclic convolution, which the coefficient twist and synthetic convolution evaluate.", "explicit",
        r"We next use the complex convolution to evaluate the middle factor"),
    [infer("A6.1", "The twist arrays $\\widetilde\\theta^\\pm_k$ approximate $\\zeta^{\\pm k}$ to within $2\\cdot2^{-p}$, and the computed complex convolution twists, convolves over the ring and untwists.",
           r"For $0\le k<r$, obtain disk-grid approximations"),
     infer("A6.2", "The chirp transform multiplies by the conjugate chirp, convolves with the chirp kernel and multiplies by the conjugate chirp again.",
           r"Thus $\widetilde a$ is the convolution kernel and $x_0$ is the data"),
     infer("A6.3", "Inserting the exact bilinear contraction and adding the kernel, endpoint and convolution errors gives error below $8TL\\,2^{-p}$.",
           r"Equation~\eqref{eq:permuted-chirp} identifies the exact result, so", deferred=True)],
    page="chirp-transform",
    frm=["bluestein-chirp", "coefficient-twist", "synthetic-convolution", "disk-grid-truncation"])

src_t = show(
    "A7", "The computed transform of a source array on the prime axes expands the axes by $\\mathcal A$, applies the chirp transform on the power-of-two axes, compresses with $\\mathcal B_0$ and scales by $2^\\gamma$; its exact counterpart is $RF_{\\boldsymbol s}$, and the opposite-sign version is obtained by conjugation.",
    "Compose the linewise resampling expansion, the chirp transform and the linewise compression, and read off the exact counterpart from the tensor resampling identity.",
    mot("The tensor identity writes the source transform as a compression, the middle transform and an expansion, so the procedure applies those three factors in order.", "recoverable"),
    [infer("A7.1", "The procedure applies the linewise approximation to $\\mathcal A$, the computed chirp transform, the linewise approximation to $\\mathcal B_0$, and multiplies the numerators exactly by $2^\\gamma$.",
           r"For a source disk-grid tensor of norm at most $.5$, write"),
     infer("A7.2", "Conjugating the input and output of the procedure gives the opposite-sign transform, whose exact counterpart is $RF_{\\boldsymbol s}^+$.",
           r"Define the opposite-sign procedure by")],
    page="source-transform",
    frm=["tensor-resampling", "chirp-transform", "source-permutation-cancel"])

algo_steps = [
    infer("A8", "The algorithm applies $\\Phi$ to both digit arrays, computes the two source transforms, multiplies pointwise and truncates, computes the opposite transform, scales by $S$ and $2^{2b+4}S$, rounds, applies $\\Phi^{-1}$ and propagates carries.",
          r"With these streams prepared, perform the following operations."),
    infer("A9", "The two occurrences of $S$ undo different normalizations: the exact counterpart after the three transforms is $(u*v)/S^2$, and the scale $2^{2b+4}S$ restores the integer coefficient convolution.",
          r"The two occurrences of $S$ in this algorithm undo different"),
]

mult_alg = show(
    "A", "Convert the inputs to radix-$2^b$ digits, map them to the prime axes by the CRT map, compute the two source transforms, multiply pointwise, compute the opposite transform, rescale by $S$ and $2^{2b+4}$, round, undo the CRT map and propagate carries to output the exact $2n$-bit product.",
    "Instantiate the earlier procedures with explicit compatible parameters and chain them in the order digits, CRT map, source transforms, pointwise product, opposite transform, rescaling, rounding, inverse map, carries.",
    mot("The procedures must be given compatible parameters, their approximations must be recovered into integer coefficients, and the remaining tape operations must be accounted for.", "explicit",
        r"exact.  We choose compatible parameters for these procedures, recover"),
    [par, primes, digits, crt, twist, chirp_t, src_t] + algo_steps,
    page="multiplication-algorithm",
    frm=["crt-address-map", "source-transform", "parameter-choice", "prime-lengths", "exact-recovery", "multiplication-as-convolution", "disk-grid-truncation"],
    adds=[sym("b", "radix exponent", "The least integer with $2^b\\ge n$, so that digits of $b$ bits are used."),
          sym("p", "working precision", "The number of fractional bits of fixed-point values, equal to $6b$.", "count"),
          sym("d", "axis count", "The number of axes of the padded power-of-two box.", "count"),
          sym("T", "box size", "The number of entries of the padded power-of-two box, a power of two near $n/b$.", "count"),
          sym("S", "source size", "The product of the pairwise coprime prime source lengths.")])

exact_rec = show(
    "E", "The scaled computed convolution has error below $1/2$, so rounding each real part to the nearest integer gives the true integer coefficients, and carries propagated from the least significant digit produce the exact $2n$-bit product.",
    "Track disk margins and errors through every call by contraction and bilinear error propagation, bound the final error explicitly after the exact scalings, then round and propagate radix carries.",
    mot("Each computed array approximates an exact contraction, and the error bounds of the interfaces add up without amplification, so the total error can be bounded call by call.", "recoverable"),
    [infer("E1", "Using the sup norm and units $h_p=2^{-p}$, linear contractions propagate errors without increase and bilinear contractions add the errors of their operands.",
           r"Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this"),
     infer("E2", "The source transform of norm at most $.5$ has error below $9\\cdot 2^\\gamma TL\\,h_p$ and norm below $.501$.",
           r"Finally let the input to a source transform have norm at most $.5$."),
     infer("E3", "The cancellation lemma gives $G(U\\cdot V_1)=(u*v)/S^2$, and the computed opposite transform is within $(3E_s+2)h_p$ of it.",
           r"Lemma~\ref{lem:chirp-permutation}, applied to"),
     infer("E4", "After the exact scalings the final absolute error is below $448\\,b\\,2^{-b+\\gamma}\\le448\\,b\\,2^{-3b/4}<1/2$.",
           r"Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than"),
     infer("E5", "Carries propagated in increasing coefficient order stay below $Q_0^2$ and, with the invariant $\\sum_{h<j}c_hQ_0^h=\\sum_{h<j}d_hQ_0^h+k_jQ_0^j$, produce the exact digits of the product.",
           r"To propagate carries, let $Q_0=2^b$.  The recovered ordinary")],
    page="exact-recovery",
    frm=["disk-grid-truncation", "contraction-error-budget", "multiplication-as-convolution", "source-permutation-cancel", "triangle-inequality-and-error-bounds"],
    salient="The error stays below $1/2$ although the exact scalings multiply it by $2^{2b+4}S\\cdot 2^{\\gamma}$-sized factors, because the precision $p=6b$ leaves about $4b$ spare bits and $\\gamma=o(b)$.")

cost = show(
    "K", "Dividing all costs by $Tp=\\Theta(n)$ gives a table of seven dominant terms whose powers of $p$ are at most $1-2\\kappa$ for $\\kappa=2^{-182}$, so the total is $O(n(\\lg n)^{1-\\kappa})$, with schoolbook multiplication below a cutoff.",
    "Tabulate the normalized cost of each operation, express each dominant term as a power of $p$ with an explicit margin below one, and take the smallest margin.",
    mot("Every fixed power of $\\log p$ is eventually below $p^\\kappa$, so the explicit slack between the smallest margin and $\\kappa$ absorbs any remaining logarithmic factor.", "explicit",
        r"Thus $\min_i g_i=2^{-181}=2\kappa$.  This explicit slack will cover"),
    [infer("K1", "With $V=Tp=\\Theta(n)$ the costs divided by $V$ are listed in a table, in which a fixed number of repeated transforms is absorbed into constants.",
           r"For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient"),
     infer("K2", "The seven dominant powers of $p$ have margins $g_1,\\ldots,g_7$ below one, given by explicit expressions in $\\epsilon,c,\\tau,\\delta,\\lambda'$.",
           r"The seven dominant powers in Table~\ref{tab:costs} have the following"),
     infer("K3", "Direct substitution gives $g_2=2^{-181}$ as the smallest margin, so $\\min_ig_i=2\\kappa$.",
           r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad"),
     infer("K4", "The Gaussian line maps cost $O(dTp^{3/2+\\delta}\\alpha)$, giving the fifth row, and the other rows follow from the transform, interchange and packing bounds.",
           r"For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines."),
     infer("K5", "Each displayed power is at most $1-2\\kappa$ and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually, so the total is $O(Tp\\,p^{1-\\kappa})$.",
           r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
     infer("K6", "Using schoolbook multiplication below a fixed cutoff gives a single machine with worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every input length.",
           r"Fix one cutoff beyond all the size, precision, margin and layout")],
    page="cost-analysis",
    frm=["chunk-swap", "simultaneous-layer", "transform-layout", "tensor-resampling", "chirp-transform", "signed-packing", "crt-address-map", "parameter-choice"],
    salient="The exponent $\\kappa=2^{-182}$ is half the smallest margin $g_2=2^{-181}=\\epsilon c(1-\\tau)$, which comes from the chunk exchanges of the transform layout, so the weakest of the seven terms fixes the final saving.")

root = show(
    "R", "A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
    "Reduce multiplication to convolution over $\\mathbb C[y]/(y^r+1)$ through radix digits, Chinese-remainder axes, Gaussian resampling and chirps, speed up the data movement and the butterfly arithmetic with two network-based tape procedures with a strict rank saving, recover the exact product by rounding and carries, and add up the costs.",
    mot("Scanning the whole array at each of the logarithmically many transform levels already costs $n\\log n$, so both the data movement and the arithmetic need savings.", "explicit",
        r"We therefore need savings in both movement and arithmetic."),
    [g1, syn_conv, g3, mult_alg, exact_rec, cost],
    page="main-theorem",
    frm=["multiplication-algorithm", "cost-analysis", "nlogn-conjecture", "multitape-model", "established-multiplier", "schoolbook-multiplication-and-karatsuba"])

answer = {"root": root}


# ---------------------------------------------------------------- checks
def walk(n, out):
    out.append(n)
    for c in n.get("children", []):
        walk(c, out)


nodes = []
walk(root, nodes)
last = -1
ids = set()
bad = False
for n in nodes:
    assert n["id"] not in ids, n["id"]
    ids.add(n["id"])
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        cnt = SRC.count(q)
        if cnt == 0:
            print("MISSING", n["id"], repr(q))
            bad = True
            continue
        pos = SRC.find(q)
        if cnt > 1:
            print("MULTI", n["id"], cnt, repr(q))
        if not n.get("deferred"):
            if pos <= last:
                print("ORDER", n["id"], pos, last)
                bad = True
            last = max(last, pos)
    else:
        m = n["motivation"]
        if m["quote"]:
            q = m["quote"]["quote"]
            if q not in SRC:
                print("MOTMISSING", n["id"], repr(q))
                bad = True
        assert m["source"] != "explicit" or m["quote"], n["id"]

pages = {}
for n in nodes:
    if n.get("page"):
        assert n["page"] not in pages, n["page"]
        pages[n["page"]] = n["id"]
print(len(nodes), "nodes;", len(pages), "pages")
used_from = set()
for n in nodes:
    used_from.update(n.get("from", []))
allpages = ["multitape-model", "nlogn-conjecture", "fixed-point-arithmetic", "established-multiplier", "address-fields-volume", "stream-ops", "controlled-shifts", "linear-algebra-basics", "tensor-products", "address-shear", "f2-vectors", "bilinear-orthogonality", "subset-pairing-formulas", "scalar-exchange-network", "network-frames", "row-splitting-roles", "subspace-labels-rank-saving", "rank-deficit-recurrence", "bit-network-interface", "lower-factorization", "matrix-shear-cost", "fixed-tape-dfs-schedule", "power-width-interchange", "chunk-swap", "packed-rotations", "exceptional-address-repair", "packed-selected-bit-addition", "polynomial-ring-negacyclic", "dft", "synthetic-roots", "fft-butterfly", "phase-kernel", "complex-network-interface", "phase-frame-layer", "multidim-dft", "synthetic-transform", "frequency-order", "contraction-error-budget", "disk-grid-truncation", "guard-width", "simultaneous-layer", "transform-layout", "signed-packing", "gaussian-resampling", "tensor-resampling", "cyclic-convolution", "multiplication-as-convolution", "bluestein-chirp", "source-permutation-cancel", "synthetic-convolution", "parameter-choice", "crt-address-map", "prime-lengths", "coefficient-twist", "chirp-transform", "source-transform", "exact-recovery", "multiplication-algorithm", "cost-analysis", "main-theorem"]
idx = {p: i for i, p in enumerate(allpages)}
for p in allpages:
    if p not in pages and p not in used_from:
        print("UNUSED PAGE", p)
# from-order check
def check(n, curpage):
    pg = n.get("page") or curpage
    for f in n.get("from", []):
        if f in idx and idx[f] >= idx[pg]:
            print("FROM ORDER", n["id"], f, pg)
    for c in n.get("children", []):
        check(c, pg)
check(root, None)
if bad:
    sys.exit(1)
json.dump(answer, open('/home/user/openai-nlogn-wiki/runs/P4/exegenius/tasks/0003-argument.answer.json', 'w'), indent=1, ensure_ascii=False)
print("written")
