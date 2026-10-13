import json, sys

SRC = open('/home/user/openai-nlogn-wiki/runs/G4/sources/paper.tex').read()
pos_log = []


def ev(q):
    assert SRC.count(q) == 1, ("quote not unique/missing", q, SRC.count(q))
    return {"source": "paper", "quote": q}


def infer(id, claim, quote, frm=None, salient=None, page=None):
    assert SRC.count(quote) == 1, (id, quote, SRC.count(quote))
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote)}
    if frm:
        n["from"] = frm
    if salient:
        n["salient"] = salient
    if page:
        n["page"] = page
    return n


def show(id, claim, method, mot_text, mot_src, children, page=None, frm=None,
         salient=None, adds=None, mot_quote=None):
    m = {"text": mot_text, "source": mot_src}
    if mot_src == "explicit":
        assert mot_quote
        m["quote"] = ev(mot_quote)
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": m, "children": children}
    if page:
        n["page"] = page
    if frm:
        n["from"] = frm
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = adds
    return n


def add(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


# ---------------------------------------------------------------- S1
S1_1 = show(
    "S1.1",
    "Three forward invocations of the subset-intersection network, at stages 1, 2 and 3, send $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restore every scratch value, whatever its initial content.",
    "Cancel the old scratch contribution, add the source values to the target through copy, gather, scatter and side wires, then restore the scratch values; check that the net coefficient from $x_T$ to $y_S$ is exactly the identity, and compose three such invocations.",
    "A single invocation adds $x_S$ to $y_S$ regardless of the scratch values; composing three of them (add, subtract, add) turns the addition into a signed exchange of the two banks.",
    "explicit",
    [
        infer("S1.1.1", "The net target change of the eight-row schedule is $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$, independent of the initial scratch values.",
              "Rows 6 and 7 restore $c,a$."),
        infer("S1.1.2", "Side wires cancel the unwanted intersection coefficients, so the net map of one invocation is $y\\gets y+x$.",
              "Thus both net maps are $y\\gets y+x$."),
        infer("S1.1.3", "Stage 1 adds $X$ to $Y$, stage 2 subtracts $Y$ from $X$, stage 3 adds again, giving the signed exchange.",
              "Starting from $(x,y)$, the three stages give"),
    ],
    page="exchange-network",
    frm=["sets-subsets-and-counting", "matrix-algebra", "pointwise-operations-on-lists-and-vectors"],
    salient="The exchange works for arbitrary initial scratch values: the first two rows subtract the old scratch contribution and the last two restore it, so the net map does not depend on it.",
    mot_quote="remove the effect of the old scratch values;",
)

S1_2 = show(
    "S1.2",
    "Attaching nested nondegenerate subspaces to the gates makes each edge's dimension change count the smaller operations it needs, and the total dimension lost on decreasing edges is $L<N/2$, so the sum of absolute changes stays below $Wm$ by a strict margin.",
    "Give each stage a label built from tensor factors $A$, $B$, $P$, $Q$ of triple indicator vectors, tabulate the orthogonal residual of every edge, and sum the dimension changes gate by gate.",
    "The labels turn the cost of a change of representation into a dimension count, and only the central wires between times 3 and 4 ever lose dimension.",
    "explicit",
    [
        infer("S1.2.1", "Every edge joins comparable nondegenerate labels, so its orthogonal residual is defined.",
              "Every edge joins comparable nondegenerate labels."),
        infer("S1.2.2", "The only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$.",
              "edges are the central-wire edges from time 3 to time 4; their dimension"),
        infer("S1.2.3", "Signed changes telescope at each gate, so the sum of absolute changes is $Wm-2N+2L$.",
              "The signed sum of dimension changes telescopes at every gate: each"),
        infer("S1.2.4", "The loss ratios $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$ are both below $1/2$.",
              "In particular, both are smaller than $1/2$."),
    ],
    page="subspace-labels",
    frm=["linear-subspaces", "frames-on-arrays", "exchange-network", "sets-subsets-and-counting"],
    salient="Only the central-wire edges from time 3 to time 4 ever decrease dimension, each by exactly $h$, so the total loss is a fixed fraction $100/539$ (bit) or $101/539$ (complex) of $N$, below one half in both networks.",
    mot_quote="The saving will come from keeping the total dimension lost on decreasing",
)

S1_3 = show(
    "S1.3",
    "In the bit network, assigning the projection $P_U$ to every gate or sink with label $U$ (and $-P_{U_a}$ to the sources $X_a$) gives rational matrices $M_v$ whose endpoint difference is $I_m$, the shear $H\\leftarrow H+D$, with rank sum $s_{\\rm b}<W_{\\rm b}m$.",
    "Take projections onto the labels as the frames, so an edge difference $P_V-P_U$ has rank equal to the dimension change, and the endpoint difference telescopes to the identity.",
    "Frames that are permutations $\\Phi_M$ of the address fields turn an endpoint matrix difference into the shear applied to every role, and the rank of an edge matrix equals the number of smaller interchanges needed.",
    "explicit",
    [
        infer("S1.3.1", "Each source $X_a$ gets the matrix $-P_{U_a}$ and every other source gets zero.",
              "Assign the source matrix $-P_{U_a}$"),
        infer("S1.3.2", "For nested labels $U\\subset V$, the edge difference $P_V-P_U$ has rank $\\dim V-\\dim U$.",
              "$P_V-P_U$ is the identity on $V\\cap U^\\perp$ and zero on its"),
        infer("S1.3.3", "For an input $X_a$ the endpoint difference is $P_{U_a^\\perp}+P_{U_a}=I_m$, and for every other role it is also $I_m$.",
              "For an input $X_a$ the endpoint difference is"),
    ],
    page="bit-network-interface",
    frm=["subspace-labels", "exchange-network", "frames-on-arrays", "linear-subspaces", "matrix-algebra"],
    mot_quote="routed role is exactly the shear applied to that role.",
)

S1_4 = show(
    "S1.4",
    "In the complex network with binary labels, every edge's phase-frame difference is a product of translation kernels $aI+bX_v$, one per vector of an orthonormal basis of the edge residual, with total length $s_{\\rm c}<W_{\\rm c}m$, and the frames telescope to $C^{\\otimes m}$ on every role.",
    "Use the phase frames $i^{\\operatorname{wt}(P_Ux)}$, whose weights add modulo 4 across orthogonal vectors, so each orthonormal residual vector contributes one two-point kernel; repair the single pair $X_a\\to Y_a$ by conjugating with $Z$.",
    "Hamming weight is additive modulo 4 over orthogonal binary vectors, and an orthonormal basis of norm-one vectors makes each residual vector contribute exactly one kernel $aI+bX_v$ of the same form as the two-point kernel $C$.",
    "recoverable",
    [
        infer("S1.4.1", "A single orthonormal residual vector $v$ turns the phase $i^{\\varepsilon[v\\cdot x]}$ into a combination of the identity and the character $(-1)^{v\\cdot x}$.",
              "$i^{\\varepsilon[v\\cdot x]}$ equals"),
        infer("S1.4.2", "After the Hadamard conjugation the character becomes the translation $X_v$, so the phase becomes $aI+bX_v$ or its inverse.",
              "becomes $aI+bX_v$ or its inverse."),
        infer("S1.4.3", "The zero label has frame $I$ and the full label has frame $C^{\\otimes m}$, so only the pair $X_a\\to Y_a$ is not already a forward $C^{\\otimes m}$.",
              "The zero label has frame $I$, while the full label has frame"),
        infer("S1.4.4", "After $Z$ corrections and undoing the signed exchange, every role, scratch roles included, receives $C^{\\otimes m}$.",
              "Every role, including every scratch role, now has"),
    ],
    page="complex-phase-network",
    frm=["phase-kernel-c", "subspace-labels", "frames-on-arrays", "exchange-network",
         "bitwise-operations-and-hamming-weight", "euler-s-formula-and-complex-exponentials", "matrix-algebra"],
    salient="Whatever the network does inside, every role, including every scratch role, ends with exactly the same operator $C^{\\otimes m}$; this uniformity comes from telescoping phase frames.",
)

S1_5 = infer(
    "S1.5",
    "With $\\tau=\\sigma=1-2^{-50}$ the rank ratios satisfy $s_{\\rm b}/W_{\\rm b}<m^\\tau$ and $s_{\\rm c}/W_{\\rm c}<m^\\sigma$.",
    "Both exact deficits displayed above are greater than $20\\cdot2^{-50}$.",
    frm=["recursive-power-saving", "logarithms-exponentials-and-floor-ceiling-in-analysis"],
)

S1 = show(
    "S1",
    "Two fixed linear networks, one over bits and one over complex numbers, exchange two banks of values, restore every scratch value, and have total edge rank $s$ below $Wm$, where $W$ is the number of wires and $m$ the label dimension.",
    "Build a scalar bank-exchange network from three-element subset intersections, lift it to arrays through frames, attach nested subspace labels to its gates, and read off a rational interface for bits and a phase interface for complex values.",
    "The labels make changes of representation cheap: each edge's dimension change counts the smaller operations it needs, and the decisive strict inequality $s<Wm$ is what later gives a power saving.",
    "explicit",
    [S1_1, S1_2, S1_3, S1_4, S1_5],
    adds=[
        add("W", "wire count", "the number of wires in a network, including scratch wires", "count"),
        add("m", "label dimension", "the dimension of the fixed space of subspace labels", "count"),
        add("s", "rank budget", "the total number of smaller operations on all edges of a network", "count"),
    ],
    salient="The rank budget is only barely below $Wm$ (relative deficit about $10^{-11}$), yet strictly below; this strictness is the entire source of the power saving.",
    mot_quote="before constructing the subspace labels that make changes of representation",
)

# ---------------------------------------------------------------- S2
S2_1 = show(
    "S2.1",
    "Every rational matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones.",
    "Eliminate one pivot at a time, choosing the rightmost nonzero entry of the topmost nonzero row and clearing its row and column with lower triangular elementary operations.",
    "Lower triangular changes of coordinates can be performed entirely in the direction in which a later tape field is updated from earlier ones, so they cost only linear time.",
    "explicit",
    [
        infer("S2.1.1", "Pick the topmost nonzero row and its rightmost nonzero entry as pivot and clear its row and column by lower triangular elementary matrices.",
              "nonzero row and its rightmost nonzero entry."),
        infer("S2.1.2", "Delete the pivot row and column and repeat on the active submatrix; the operations stay lower triangular in the original order.",
              "Delete the pivot row and column from the active index sets, retaining"),
        infer("S2.1.3", "Each step isolates a rank-one block, so the final partial permutation matrix has exactly $a$ ones.",
              "permutation matrix has exactly $a$ ones."),
    ],
    page="triangular-factorization",
    frm=["matrix-algebra", "linear-subspaces", "mathematical-induction-and-proof-by-contradiction"],
    mot_quote="can be performed entirely in this direction.",
)

S2_2 = show(
    "S2.2",
    "The map $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ can be performed with exactly $\\operatorname{rank}(A)$ interchanges of $b$-digit fields and $O(V)$ further work.",
    "Factor $A=E_1\\Pi E_2$, apply the lower triangular parts by controlled shifts and the partial permutation $\\Pi$ by one field interchange per entry equal to one.",
    "The triangular parts only need later fields updated from earlier ones, which costs linear time, so the whole expense of the shear is concentrated in the interchanges, one per unit of rank.",
    "recoverable",
    [
        infer("S2.2.1", "A lower triangular transformation of $H$ or of $D$ costs $O(V)$, updating coordinates in descending physical order.",
              "A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
        infer("S2.2.2", "For $A=E_1\\Pi E_2$, transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\\Pi D$ to $H$, then undo the triangular transformations.",
              "For $A=E_1\\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,"),
        infer("S2.2.3", "Each one of $\\Pi$ gives $H_i\\leftarrow H_i+D_j$ through two controlled shifts and one interchange.",
              "It uses just one interchange."),
    ],
    page="matrix-shear",
    frm=["triangular-factorization", "controlled-shift", "elementary-stream-ops",
         "modular-arithmetic-and-residue-rings", "fixed-tape-model"],
)

S2_3 = show(
    "S2.3",
    "Two disjoint chunks of $e=m^k$ radix-$q$ digits, given enough rows, can be interchanged in time $O(Ve^\\tau)$ by running the bit network with a matrix shear on every edge, each shear recursing into smaller interchanges.",
    "Induct on $k$: split rows cyclically among the $W$ roles, apply frames $\\Phi_M$ so every edge is a shear that costs $\\operatorname{rank}$-many half-width interchanges, perform the middle shear with the circuit, and solve the volume-normalized recurrence.",
    "The network turns one interchange of width $m^k$ into $s$ interchanges of width $m^{k-1}$ on streams of volume $V/W$; because $s<Wm$ the normalized cost grows by a factor less than $m$ per level.",
    "recoverable",
    [
        infer("S2.3.1", "Split whole rows cyclically into $W$ role streams, each of volume $V/W$ with the same remaining shape.",
              "Split whole rows cyclically into $W$ role streams within each prefix"),
        infer("S2.3.2", "The row split supplies the common address set for the frame identity, with frame $\\Phi_M$ at a vertex of matrix $M$, so the output is $\\Phi_{I_m}$, the shear $H\\leftarrow H+D$.",
              "The row split supplies the common address set used in the"),
        infer("S2.3.3", "To interchange the two full chunks, perform $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$; only the middle shear uses the circuit.",
              "To interchange the two full chunks, perform"),
        infer("S2.3.4", "The number of recursive calls is the sum of the edge ranks, exactly $s$, each on a stream of volume $V/W$.",
              "The number of recursive calls is the sum of the edge ranks, exactly $s$."),
        infer("S2.3.5", "With $s/W<m^\\tau$ the recurrence $F_k\\le(s/W)F_{k-1}+O(1)$ sums geometrically to $F_k=O(e^\\tau)$.",
              "For $a=s/W<m^\\tau$ the geometric sum"),
        infer("S2.3.6", "A fixed-tape depth-first schedule parks the inactive role streams on a stack, so the overhead per node is $O(V)$ and does not multiply the call count.",
              "Before a recursive call, append the $W-1$ inactive role streams to the"),
    ],
    page="power-width-interchange",
    frm=["recursive-power-saving", "bit-network-interface", "matrix-shear", "frames-on-arrays",
         "elementary-stream-ops", "fixed-tape-model", "stacks-and-call-stacks",
         "recurrence-relations-and-divide-and-conquer", "summations-and-geometric-series"],
    adds=[
        add("e", "chunk width", "the number of radix-$q$ digits in each of the two interchanged chunks, equal to $m^k$", "count"),
        add("k", "recursion depth", "the exponent with $e=m^k$, the number of levels of the recursion", "count"),
    ],
    salient="Each level makes $s$ calls on streams of volume $V/W$, with $s$ nearly $Wm$, yet the cost exponent $\\tau$ is strictly below 1 because $s/W<m^\\tau$.",
)

S2_4 = show(
    "S2.4",
    "The power-of-two width and row-count restrictions can be removed: chunks of any width $u$ are interchanged with the rows supplied by a few high digits, at total cost $O(Vu^\\tau)$.",
    "Move a few high digits of each chunk to form a row field, pad its length to a multiple of $W^k$, write the remaining width in base $m$ and apply the power-width interchange to each piece, then pad binary widths up to a power of the fixed prime $q$.",
    "The power-width interchange needs a width $m^k$ and a row field divisible by $W^k$, so arbitrary widths are cut into base-$m$ pieces and the rows are taken from the chunks' own high digits at a lower cost.",
    "recoverable",
    [
        infer("S2.4.1", "Append zero rows within each prefix so the row count is divisible by $W^k$; the padded volume is less than $2V$.",
              "Append zero rows, separately within"),
        infer("S2.4.2", "Write the remaining width in base $m$ and apply the power-width interchange to each corresponding pair of pieces; the cost is a geometric sum $O(Ve^\\tau)$.",
              "Partition each remaining chunk into corresponding consecutive pieces,"),
        infer("S2.4.3", "For binary chunks of $u$ bits choose the least $e$ with $q^e\\ge2^u$, pad both ranges, and scan away the padding; since $e=O(u)$ the bound is $O(Vu^\\tau)$.",
              "Finally, for binary chunks let $e$ be the least integer with"),
    ],
    frm=["power-width-interchange", "positional-radix-number-representation"],
)

S2 = show(
    "S2",
    "Two equal-width address fields of $u$ bits in an arbitrary array can be exchanged in $O(Vu^\\tau)$ time for a fixed $\\tau<1$, even though intermediate steps XOR data together.",
    "Run the bit exchange network with every edge a rational matrix shear executed by smaller interchanges, using the lower triangular factorization, then remove the width and row restrictions.",
    "An edge matrix of rank $a$ needs $a$ smaller interchanges, and the sum of these ranks is below the number of wires times $m$, so the resulting recurrence saves a power of the chunk width.",
    "explicit",
    [S2_1, S2_2, S2_3, S2_4],
    page="chunk-interchange",
    frm=["bit-network-interface", "recursive-power-saving", "elementary-stream-ops", "fixed-tape-model"],
    salient="The final effect is an exact permutation of the data, although the intermediate streams hold XOR combinations; the cost $Vu^\\tau$ is still a power less than the $Vu$ of moving fields one digit at a time.",
    mot_quote="An edge matrix of rank $a$ will require $a$ smaller interchanges.",
)

# ---------------------------------------------------------------- S3
S3_4 = show(
    "S3.4",
    "Adding corresponding selected bits of two address chunks $x,y$ (a binary row addition $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$), while restoring a third chunk $z$, costs $O(V(L^\\tau+1))$ by a constant number of cyclic shifts of whole chunk ranges plus a deterministic repair of a small exceptional address set.",
    "Mimic the XORs by eight parity-conditioned additions that act as the required bit flip whenever no guard segment carries into its neighbour, bound the exceptional addresses by the guard intervals, and repair them by stable sorting.",
    "A cyclic shift of a whole chunk range by an offset computed from earlier fields is a linear-time tape operation, so the XORs on spaced-out selected positions are traded for shifts away from a small address set that can be corrected exactly.",
    "recoverable",
    [
        infer("S3.4.1", "For a Boolean control $c$ and integers $u,w$, eight conditional additions flip the parity of $u$ exactly when $c=1$ and restore $w$.",
              "For a Boolean control $c$ and arbitrary integers $u,w$, perform the following"),
        infer("S3.4.2", "Applying each line simultaneously to all segment pairs is a single cyclic shift of a chunk, whose offset does not depend on its target.",
              "Apply each line of \\eqref{eq:eight-packed-additions} simultaneously to all"),
        infer("S3.4.3", "Away from the bad set the packed additions agree with the ideal XORs; the bad set is at most a fraction $\\delta_{\\rm bad}$ of the addresses, as there are twenty excluded values per guard.",
              "There are exactly twenty excluded values for each guard in"),
        infer("S3.4.4", "Extract the exceptional records with their destination ranks, sort them stably by key, and reinsert, implementing the ideal map everywhere.",
              "To implement the correction, scan the stream with a record-rank counter."),
        infer("S3.4.5", "The omitted most significant selected position is handled by a two-bit XOR in $O(V)$ time.",
              "Finally apply the two-bit XOR to $x_{j_{f-1}},y_{j_{f-1}}$ by"),
    ],
    page="packed-selected-bit-addition",
    frm=["chunk-interchange", "controlled-shift", "elementary-stream-ops", "bitwise-operations-and-hamming-weight",
         "modular-arithmetic-and-residue-rings", "sets-subsets-and-counting"],
)

S3 = show(
    "S3",
    "Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ to the same bit position of up to $d$ address chunks of $K$ bits at once, exactly in dyadic arithmetic with a single final truncation, takes $O(Vd^{\\lambda'})$ time for a fixed $\\lambda'<1$.",
    "Write the layer as a phase-conjugated tensor power of the two-point kernel $C$, realize $C^{\\otimes e}$ with the complex phase network recursively, with each child on $e/m$ axes and volume $V/W$, implement the binary basis changes by packed selected-bit addition, and bound coefficient growth with guard bits.",
    "Separate butterfly factors would require $D$ whole-array passes; the network replaces them by $s_{\\rm c}$ calls on streams a factor $W_{\\rm c}$ smaller, and $s_{\\rm c}<W_{\\rm c}m$ again gives a power saving.",
    "explicit",
    [
        infer("S3.1", "An edge's frame change is $\\mathcal P_M\\bigl(\\prod_j C_{e_j}^{\\epsilon_j}\\bigr)\\mathcal P_M^{-1}$; apply $\\mathcal P_M^{-1}$ to each column, one $C^{\\otimes f}$ child per residual basis vector in slot $h$, then $\\mathcal P_M$.",
              "To implement \\eqref{eq:phase-edge-coordinate} on the group, first apply"),
        infer("S3.2", "A group of $e=mf$ selected axes needs exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and returns $C^{\\otimes e}$ on every role.",
              "Summing its residual dimensions gives exactly"),
        infer("S3.3", "The normalized layer is recovered exactly from the $C$-layer by $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$.",
              "on all selected coordinates gives"),
        S3_4,
        infer("S3.5", "A row addition between slots $h'$ and $h$ uses a third slot as scratch; the complete binary change of basis and its inverse cost $O(V((eK)^\\tau+1))$.",
              "To add row $h'$ to row $h$, use slot $h'$ as $x$,"),
        infer("S3.6", "Rows are taken from the first $q_0$ chunks and padded; a row index $u=Wg+w$ sends the whole row to role $w$, so each child has volume exactly $V/W$.",
              "At a node, write a row index as \\(u=Wg+w\\), with \\(0\\le w<W\\),"),
        infer("S3.7", "The recurrence $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ unrolls to $O(d^{\\lambda'})$ for a fixed $\\lambda'<1$.",
              "Indeed, the \\(s\\) child calls are executed on streams of volume"),
        infer("S3.8", "Explicit guard widths bound denominator and magnitude growth within one layer by $\\lceil C_0d^{C_1}\\rceil=o(p)$ bits, so all intermediate values are exact.",
              "The accelerated network is evaluated exactly until an entire"),
        infer("S3.9", "Every row of $\\mathcal H$ has absolute row sum one, so $\\mathcal H$ maps the disk to itself and the single truncation has error below $\\sqrt2\\,2^{-p}$.",
              "absolute row sum one."),
    ],
    page="simultaneous-butterfly-layer",
    frm=["complex-phase-network", "phase-kernel-c", "chunk-interchange", "recursive-power-saving",
         "controlled-shift", "elementary-stream-ops", "synthetic-ring", "fixed-point-precision",
         "fft-butterfly", "dyadic-rationals", "permutations-and-bijections"],
    adds=[
        add("K", "chunk width", "the number of address bits in each of the chunks that carry a transform axis", "count"),
    ],
    salient="The layer on $d$ chunks costs $d^{\\lambda'}$ per bit with $\\lambda'<1$, although applying one butterfly per chunk would cost $d$ passes; the saving again rests on $s_{\\rm c}<W_{\\rm c}m$.",
    mot_quote="factors would require $D$ whole-array passes.",
)

# ---------------------------------------------------------------- S4
S4_1 = show(
    "S4.1",
    "A forward synthetic transform of $M$ ring records, after a positional layout permutation $L$ of the record addresses, costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ and leaves the frequencies in bit-reversed order $B$, which the opposite transform consumes.",
    "Move the selected bit slots of every axis to a prefix and permute $K$-bit chunks so that the bits used in each round sit at a common offset, so each of the $\\ell$ rounds is one simultaneous butterfly layer.",
    "The simultaneous layer needs the active bits of all participating axes at the same offset in consecutive $K$-bit chunks, so the layout has to be built by chunk interchanges first.",
    "explicit",
    [
        infer("S4.1.1", "The forward procedure writes frequency $j$ into slot $\\operatorname{rev}(j)$; the reverse procedure consumes that order, implementing $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
              "procedures implement"),
        infer("S4.1.2", "Moving at most $D(b+1)=O(dK)$ listed bit slots to a prefix costs $O(TpdK)$.",
              "listed slots, so the moves cost $O(TpdK)$."),
        infer("S4.1.3", "At most $Dq-1$ exchanges of width-$K$ chunks put the chunks in round order, costing $O(Tp\\cdot pK^{\\tau-1})$.",
              "exchanges of width-$K$ address chunks, even when the chunks are"),
        infer("S4.1.4", "Process the rounds at named positions $h=\\ell-1,\\ldots,0$, each a simultaneous layer on all participating axes.",
              "First process the round at named position $h=\\ell-1$ on the long"),
    ],
    page="synthetic-transform-layout",
    frm=["simultaneous-butterfly-layer", "chunk-interchange", "synthetic-transform", "synthetic-ring", "fft-butterfly",
         "elementary-stream-ops", "fixed-point-precision", "permutations-and-bijections"],
    mot_quote="we must place the selected bits of the participating axes at a common",
)

S4_2 = show(
    "S4.2",
    "Two disk-grid ring polynomials $f,g$ modulo $y^r+1$ are multiplied exactly and returned as $Q_p(fg/r)$ in $O(rp\\log(rp))$ time, by evaluating at $B_0=2^{4p}$, multiplying four pairs of integers with the established multiplier, and reading coefficients back by centered residues.",
    "Signed Kronecker substitution: evaluate each real or imaginary part polynomial at $B_0$, multiply the resulting integers, extract the product coefficients one block at a time using centered residues, then reduce modulo $y^r+1$ and truncate.",
    "A polynomial product becomes one integer product, which the established $O(N\\log N)$ multiplier does on records of only $O(rp)$ bits, so no recursion into the new algorithm is needed.",
    "explicit",
    [
        infer("S4.2.1", "Multiply the four pairs of absolute values with the established multiplier and restore the signs.",
              "pairs of absolute values using the established multiplier and restore"),
        infer("S4.2.2", "Each product coefficient is below $B_0/2$ in magnitude, so after removing lower coefficients its centered residue modulo $B_0$ identifies it.",
              "After the lower coefficients have been removed from an evaluation,"),
        infer("S4.2.3", "Reduce modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$.",
              "To reduce them modulo $y^r+1$, subtract the"),
        infer("S4.2.4", "Shift the magnitude right by $p+\\ell$ bits to obtain the $p$-bit grid numerator of the normalized product.",
              "Finally the $p$-bit grid numerator of the normalized product is"),
    ],
    page="signed-packing",
    frm=["nlogn-multiplier", "synthetic-ring", "fixed-point-precision", "positional-radix-number-representation",
         "signed-binary-numbers-and-rounding", "polynomial"],
    mot_quote="To multiply the polynomial records, we use the fixed-tape integer",
)

S4 = show(
    "S4",
    "Normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ of arrays of $M$ ring records over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ has error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ and costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$, using two forward synthetic transforms, pointwise ring products and the opposite transform.",
    "Apply the convolution theorem in the ring: transform both operands, multiply pointwise with signed packing, and transform back, keeping the same frequency order throughout so that no permutation is executed.",
    "The opposite transform can consume the stored bit-reversed order, so the two forward transforms and the pointwise product never need the frequencies sorted.",
    "explicit",
    [
        S4_1,
        S4_2,
        infer("S4.3", "Perform both forward transforms, retain their common $LB$ order, multiply corresponding records, apply the opposite procedure and scale exactly by $M=T/r$.",
              "Perform both forward transforms and retain their common $LB$ order."),
        infer("S4.4", "Expanding the finite sums gives $F^-_{\\boldsymbol t}(f*g)=M(F^-_{\\boldsymbol t}f)(F^-_{\\boldsymbol t}g)$, so the scaled result is $(f*g)/(rM)$.",
              "To check normalization, expansion of the finite sums gives"),
        infer("S4.5", "The three transform errors and the product truncation add to an error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ after scaling by $M$.",
              "The final exact multiplication by $M$ therefore gives error less than"),
    ],
    page="synthetic-convolution",
    frm=["synthetic-ring", "convolution", "fixed-point-precision", "synthetic-transform", "fft-butterfly"],
    adds=[
        add("r", "record length", "the number of complex coefficients in a ring record, a power of two", "count"),
        add("\\ell", "log record length", "the base-2 logarithm of $r$"),
        add("M", "record count", "the number of ring records in an array, the product of the first $d-1$ axis lengths", "count"),
    ],
    salient="Both forward transforms keep the same bit-reversed frequency order through the pointwise product, and the opposite transform consumes that order, so the permutation never has to be undone.",
    mot_quote="retain the same frequency order through their pointwise product, and",
)

# ---------------------------------------------------------------- S5
S5_1 = show(
    "S5.1",
    "For coprime $s<t$ with $t/s-1>p/\\alpha^4$ there are linear contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, computable to error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$.",
    "Gaussian resampling: combine the exact Gaussian identity $\\mathsf T P_sF_s=P_tF_t\\mathsf S$ with an invertible approximate left inverse $N^{-1}$ of the sampling, normalized so that both maps become contractions.",
    "A Fourier transform of length $s$ is related to one of larger length $t$ by Gaussian weights, which are smooth enough that the sampling error is tiny and the maps can be inverted by a Neumann series.",
    "recoverable",
    [
        infer("S5.1.1", "The exact Gaussian identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ holds, with $\\|N-I\\|<2^{-\\alpha^2\\theta}$.",
              "The exact Gaussian identity and inverse estimate proved in"),
        infer("S5.1.2", "Since $\\alpha^2\\theta>1$, $\\|N-I\\|<1/2$ and $N$ is invertible by the Neumann series.",
              "Thus $\\|N-I\\|<1/2$, so $N$ is invertible"),
        infer("S5.1.3", "Set $A=\\mathsf S'$ and $B_0=\\mathsf D'\\mathsf J'C$; after normalizing, both are contractions.",
              "Now set $A=\\mathsf S'$ and $B_0=\\mathsf D'\\mathsf J'C$."),
        infer("S5.1.4", "Applying the left inverse to the Gaussian identity gives $B_0P_tF_tA=2^{-2\\alpha^2}P_sF_s$.",
              "Applying this left inverse to the first identity in"),
    ],
    page="gaussian-resampling",
    frm=["dft", "euler-s-formula-and-complex-exponentials", "permutations-and-bijections",
         "vector-norms-and-the-triangle-inequality", "fixed-point-precision", "nlogn-multiplier"],
    salient="Both $A$ and $B_0$ are contractions even though the Gaussian weights alone are not, because the normalizations contribute exactly the factor $2^{-2\\alpha^2}$ that is moved to the left side of the identity.",
)

S5_4 = show(
    "S5.4",
    "The source coordinate permutation $R$ retained from resampling cancels across the two forward transforms, their pointwise product and the opposite-sign transform: $RF^+_{\\boldsymbol s}[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
    "Show that $R$ commutes with the transform up to inversion ($RF^+R=F^+$) and with pointwise products, so it disappears, then apply the convolution rule for $F_{\\boldsymbol s}$.",
    "The permutation is left inside the transform so that it never has to be executed as a separate sort; it is enough that it drops out of the final product.",
    "explicit",
    [
        infer("S5.4.1", "For a unit $c$ modulo $q$ and $(R_cz)_j=z_{cj}$, the substitution $h=ck$ gives $F^+_qR_c=R_c^{-1}F^+_q$.",
              "For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$."),
        infer("S5.4.2", "The normalized convolution rule is $F_{\\boldsymbol s}(u*v)=S(F_{\\boldsymbol s}u)\\cdot(F_{\\boldsymbol s}v)$, and $F^+_{\\boldsymbol s}F_{\\boldsymbol s}=I/S$.",
              "The normalized convolution rule is"),
        infer("S5.4.3", "Combining the two normalizations gives $(u*v)/S^2$, proving the cancellation identity.",
              "proving \\eqref{eq:source-permutation-cancel}."),
    ],
    page="permutation-cancellation",
    frm=["chirp-identity", "gaussian-resampling", "dft", "convolution", "permutations-and-bijections",
         "pointwise-operations-on-lists-and-vectors", "modular-arithmetic-and-residue-rings"],
    salient="The permutation $R$ appears twice, once in each forward transform and once in the opposite one, and the result $(u*v)/S^2$ contains no permutation at all.",
    mot_quote="whereas the synthetic transforms use powers of two. Gaussian resampling",
)

S5 = show(
    "S5",
    "The source transform of pairwise coprime lengths $s_i$ equals $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ for power-of-two lengths $t_i$, with $\\mathcal A,\\mathcal B_0$ contractions applied along each axis of the padded box in $O(dTp^{3/2+\\delta}\\alpha)$ time, plus $O(Tp\\,d^2(1+\\ell^\\tau))$ to expose axes.",
    "Tensor the one-dimensional resampling identity over the axes, apply the maps line by line on the padded power-of-two box, expose each axis by chunk interchanges, and leave the permutations $R,Q$ inside the transform.",
    "The synthetic transforms work only for power-of-two lengths whereas the convolution needs pairwise coprime lengths, and Gaussian resampling connects the two shapes without executing the two sorts.",
    "explicit",
    [
        S5_1,
        infer("S5.2", "Tensoring the one-dimensional identity over the $d$ axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$.",
              "Tensoring \\eqref{eq:no-sort-one-dimensional} proves"),
        infer("S5.3", "Moving an axis past its neighbour by chunk interchanges costs $O(Tp(1+\\ell^\\tau))$, so exposing and restoring all axes costs $O(d^2)$ such moves.",
              "To move an axis past its neighbor, interchange their"),
        S5_4,
    ],
    page="tensor-resampling",
    frm=["chunk-interchange", "dft", "permutations-and-bijections", "fixed-point-precision"],
    adds=[
        add("\\alpha", "Gaussian width", "the integer parameter controlling the width of the Gaussian weights in resampling"),
        add("\\gamma", "scale exponent", "the total power of two $\\gamma=2d\\alpha^2$ by which the tensor resampling identity is scaled"),
    ],
    mot_quote="whereas the synthetic transforms use powers of two. Gaussian resampling",
)

# ---------------------------------------------------------------- S6
S6_1 = show(
    "S6.1",
    "With $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, power-of-two axis lengths $t_i\\in\\{r/2,r\\}$ with $\\prod_it_i=T$ and distinct primes $s_i$ just below $t_i$, we have $Tp=\\Theta(n)$ and every hypothesis of the layer, transform and resampling lemmas holds.",
    "Fix explicit rational exponents, compute the sizes from $n$, find the primes in the intervals $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ by deterministic search, and verify each hypothesis in turn.",
    "The primes must be close to the powers of two so that their product fills a fixed fraction of the padded box, while each ratio $t_i/s_i$ stays far enough from 1 for the resampling lemma.",
    "explicit",
    [
        infer("S6.1.1", "Take the fixed rational exponents $\\tau=\\sigma=1-2^{-50}$, $\\epsilon=2^{-75}$, $\\kappa=2^{-182}$ and the others listed, which satisfy all layer conditions with room to spare.",
              "Take the following fixed rational numbers:"),
        infer("S6.1.2", "The sizes satisfy $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$ and $r=2^{\\Theta(p^{1-\\epsilon})}$.",
              "These definitions give"),
        infer("S6.1.3", "Distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ exist, so $T/2<S<T$ and $\\gcd(s_i,t_i)=1$.",
              "We may therefore choose distinct odd primes satisfying"),
        infer("S6.1.4", "Every hypothesis of the one-dimensional resampling lemma holds for all sufficiently large input lengths.",
              "Thus every hypothesis of Lemma~\\ref{lem:no-sort-resampling} holds for"),
        infer("S6.1.5", "The product of the two digit polynomials has degree below $S$, so convolution modulo $x^S-1$ has no wraparound.",
              "Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
    ],
    page="parameter-choices",
    frm=["gaussian-resampling", "radix-digit-convolution", "recursive-power-saving",
         "primes-coprimality-and-the-euclidean-algorithm",
         "logarithms-exponentials-and-floor-ceiling-in-analysis", "simultaneous-butterfly-layer",
         "synthetic-transform-layout", "tensor-resampling"],
    mot_quote="while each ratio $t_i/s_i$ must leave enough separation for resampling.",
)

S6_2 = show(
    "S6.2",
    "The map $x\\mapsto\\prod_ix_i^{\\mu_i}$ with $\\mu_i=P_i^{-1}\\bmod s_i$ and $P_i=\\prod_{j<i}s_j$ takes cyclic convolution of length $S=\\prod_is_i$ to multidimensional cyclic convolution, and is implemented by triangular controlled shifts and axis moves in $O(Tp\\,d^2(1+\\ell^\\tau))$ time.",
    "Use the Chinese remainder theorem as an algebra isomorphism, write each index in mixed radix, and see that axis $i$ depends only on lower digits, so the change of order is a sequence of prefix-controlled cyclic shifts.",
    "The assignment respects $x^S=1$ and sends the powers of $x$ bijectively onto the basis monomials, so it preserves convolution; the choice of coordinate powers makes the change of order triangular.",
    "explicit",
    [
        infer("S6.2.1", "The map is an algebra isomorphism that preserves cyclic convolution.",
              "$\\Phi$ is an isomorphism and preserves cyclic convolution."),
        infer("S6.2.2", "Update the targets in the order $i=d,d-1,\\ldots,1$, so the lower-index controls still hold their original digits.",
              "order $i=d,d-1,\\ldots,1$ using \\eqref{eq:triangular-crt}."),
        infer("S6.2.3", "Each triangular update is a prefix-controlled cyclic shift, preserving zero padding.",
              "Each triangular update is a prefix-controlled cyclic shift."),
        infer("S6.2.4", "Reordering the axes of widths $\\ell$ or $\\ell-1$ uses $O(d^2)$ chunk swaps, so $\\Phi$ and its inverse cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
              "The axis widths are $\\ell$ or $\\ell-1$."),
    ],
    page="crt-axis-map",
    frm=["primes-coprimality-and-the-euclidean-algorithm", "modular-arithmetic-and-residue-rings", "convolution",
         "radix-digit-convolution", "controlled-shift", "chunk-interchange", "lexicographic-order-and-multi-index-addressing"],
    adds=[
        add("\\mu_i", "axis exponent", "the inverse of the prefix product $P_i$ modulo $s_i$, the power of $x_i$ in the image of $x$"),
        add("P_i", "prefix product", "the product $s_1\\cdots s_{i-1}$ of the lengths of the earlier axes"),
    ],
    salient="The image coordinate $b_i$ of an index depends only on its own digit and the lower digits, which is why the whole change of order is a sequence of controlled shifts with controls placed before their targets.",
    mot_quote="sequence of controlled cyclic shifts.",
)

S6_3 = show(
    "S6.3",
    "The map $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ turns cyclic convolution in the last coordinate into convolution modulo $y^r+1$, so the power-of-two complex cyclic convolution reduces to the synthetic one at cost $O(Tp^{1+\\delta})$ for the twists.",
    "Multiply coefficient $k$ by $\\zeta^k$ before and by $\\zeta^{-k}$ after the ring convolution: the factor $(-1)^h$ from the negacyclic wrap cancels the extra factor $\\zeta^{rh}$.",
    "The ring modulo $y^r+1$ wraps with a sign while a cyclic convolution wraps without one, and twisting by a $2r$-th root of unity exactly compensates this sign.",
    "explicit",
    [
        infer("S6.3.1", "The map is well defined since $(\\zeta y)^r=(-1)(-1)=1$.",
              "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$."),
        infer("S6.3.2", "Untwisting recovers the cyclic coefficient with the correct sign.",
              "Untwisting therefore recovers the cyclic coefficient with the correct"),
        infer("S6.3.3", "The ring convolution $\\mathcal M_r$ convolves the first $d-1$ axes over $\\mathcal R$, and the twisted composition equals $(f*g)/T$.",
              "Here $\\mathcal M_r$ convolves the first $d-1$ axes over $\\mathcal R$,"),
        infer("S6.3.4", "Each phase product is computed exactly as a dyadic product and truncated once, at cost $O(p^{1+\\delta})$ per coefficient.",
              "Each phase product is computed exactly as a dyadic product before"),
    ],
    page="convolution-twist",
    frm=["synthetic-convolution", "synthetic-ring", "convolution", "euler-s-formula-and-complex-exponentials",
         "fixed-point-precision", "nlogn-multiplier"],
    adds=[
        add("\\zeta", "twist root", "the primitive $2r$-th root of unity $e^{\\pi i/r}$ used to twist the last coordinate"),
    ],
    mot_quote="obtained from the synthetic convolution by a coefficient twist.",
)

S6 = show(
    "S6",
    "The algorithm maps the digit polynomials by the Chinese-remainder map to prime axes, transforms them by resampling plus chirp convolution, multiplies pointwise, applies the opposite transform, rescales, rounds and propagates carries.",
    "Use the convolution theorem on the prime-axis tensor: the digit convolution equals $F^+(Fu\\cdot Fv)$ up to known scales, with the middle transform $QF_{\\boldsymbol t}$ computed as a chirp convolution through the twist and synthetic convolution.",
    "The source-transform procedures supply the three transforms needed for the radix-digit convolution.",
    "explicit",
    [
        S6_1,
        S6_2,
        S6_3,
        infer("S6.4", "The middle factor $QF_{\\boldsymbol t}$ is evaluated by the chirp transform $\\widetilde{\\mathscr C}(x)=Q_p(\\overline{\\widetilde a}\\cdot\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,x_0))$ using the complex convolution.",
              "We next use the complex convolution to evaluate the middle factor"),
        infer("S6.5", "The source transform applies $\\mathcal A$, the chirp transform, $\\mathcal B_0$ and the exact scale $2^\\gamma$, with exact counterpart $RF_{\\boldsymbol s}$.",
              "For a source disk-grid tensor of norm at most $.5$, write"),
        infer("S6.6", "Convert to digits, apply $\\Phi$, transform both operands, multiply pointwise, apply the opposite transform, scale by $S$ and $2^{2b+4}S$, round, undo $\\Phi$ and propagate carries.",
              "With these streams prepared, perform the following operations."),
    ],
    page="multiplication-algorithm",
    frm=["radix-digit-convolution", "convolution", "dft", "chirp-identity", "tensor-resampling",
         "permutation-cancellation", "synthetic-convolution"],
    mot_quote="The source-transform procedures now supply the three transforms needed",
)

# ---------------------------------------------------------------- S7
S7 = show(
    "S7",
    "The accumulated numerical error on the recovered coefficients is below $1/2$, so rounding gives the exact integer convolution, and propagating radix carries yields the exact $2n$-bit product.",
    "Track the error and the disk margin of every computed array through each contraction and bilinear map, scale by the known factors, and compare the total with $1/2$; then run the exact carry recurrence.",
    "The true coefficients are integers, so any approximation with error strictly below $1/2$ determines them uniquely by rounding.",
    "explicit",
    [
        infer("S7.1", "Errors are measured in units of $h_p=2^{-p}$ in the sup norm; contractions propagate input error and bilinear contractions add the errors of their operands.",
              "Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this"),
        infer("S7.2", "The pointwise product of the computed source transforms satisfies $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$.",
              "Thus $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$."),
        infer("S7.3", "The first exact multiplication by $S$ gives $\\widetilde w$ approximating $w=(u*v)/S$ with error below $E_wh_p$ and keeps it in the disk.",
              "The first exact numerator multiplication by $S$ gives"),
        infer("S7.4", "After the second scaling the final error is below $1/2$, so the nearest integer is the unique correct coefficient.",
              "The strict error below $1/2$ makes the nearest integer to"),
        infer("S7.5", "The carry recurrence $d_j=(c_j+k_j)\\bmod2^b$, $k_{j+1}=\\lfloor(c_j+k_j)/2^b\\rfloor$ keeps carries below $2^{2b}$ and fixes the first $j$ radix digits.",
              "To propagate carries, let $Q_0=2^b$."),
        infer("S7.6", "The exact product is below $2^{2n}$, so removing zero padding bits leaves exactly $2n$ output bits.",
              "than $2^{2n}$; all bits above position $2n-1$ are therefore zero."),
    ],
    page="exact-recovery",
    frm=["fixed-point-precision", "radix-digit-convolution", "signed-binary-numbers-and-rounding",
         "vector-norms-and-the-triangle-inequality", "positional-radix-number-representation"],
    salient="The final error is below $1/2$ despite the amplification by $2^\\gamma$ and $T^2$, because the working precision $p=6b$ is large enough to absorb it: the bound is $448b\\,2^{-3b/4}$.",
    mot_quote="The strict error below $1/2$ makes the nearest integer to",
)

# ---------------------------------------------------------------- S8
S8 = show(
    "S8",
    "Summing the normalized costs of layouts, butterfly rounds, resampling, chirps and packed products, each at most $p^{1-2\\kappa}$ per unit of volume $Tp$, gives the total time $O(n(\\log n)^{1-\\kappa})$.",
    "Tabulate each operation's cost divided by $V=Tp$ as a power of $p$, bound the setup and exceptional streams, check that all seven dominant powers have margin at least $2\\kappa$ below one, and absorb fixed powers of $\\log p$.",
    "Every ingredient costs $O(V)$ times a power of $p$ that is strictly less than 1, and the largest power determines the total.",
    "recoverable",
    [
        infer("S8.1", "The seven dominant margins $g_i$ below one have minimum $2^{-181}=2\\kappa$.",
              "Thus $\\min_i g_i=2^{-181}=2\\kappa$."),
        infer("S8.2", "The first three rows of the cost table are the three terms of the synthetic transform cost.",
              "The first three rows are the terms in"),
        infer("S8.3", "Axis exposure and restoration require $O(d^2)$ adjacent axis moves, each costing $O(V(1+\\ell^\\tau))$.",
              "Axis exposure and restoration require $O(d^2)$ adjacent axis moves."),
        infer("S8.4", "The Gaussian line machines sum to $O(dTp^{3/2+\\delta}\\alpha)$.",
              "For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines."),
        infer("S8.5", "Chirp numerators and the scalar products cost $O(dp^{1+\\delta})$ per entry, and the packed polynomial products cost $O(Tp\\log(rp))$.",
              "Chirp numerators have $O(p)$ bits and can be computed modulo $2r$ as"),
        infer("S8.6", "Global setup and prime search cost $o(V)$, and setup per record or line is $o(Tp)$ since $r$ exceeds every fixed power of $p$.",
              "Global setup and prime search cost $o(V)$, as"),
        infer("S8.7", "Each of the seven powers is at most $1-2\\kappa$ and fixed powers of $\\log p$ are at most $p^\\kappa$, giving the bound $O(n(\\log n)^{1-\\kappa})$; schoolbook multiplication handles lengths below a cutoff.",
              "The complete large-input bound is consequently"),
    ],
    page="cost-accounting",
    frm=["fixed-point-precision", "recurrence-relations-and-divide-and-conquer", "summations-and-geometric-series",
         "theta-omega-and-little-o-notation", "logarithms-exponentials-and-floor-ceiling-in-analysis",
         "parameter-choices", "nlogn-multiplier", "schoolbook-and-karatsuba-multiplication"],
    salient="The exponent $\\kappa$ is exactly half the smallest of the seven margins, $2^{-181}$, which comes from the chunk-exchange row $\\epsilon c(1-\\tau)$; this slack absorbs any remaining fixed power of $\\log p$.",
    mot_quote="Each of the seven displayed powers is at most $1-2\\kappa$ by",
)

# ---------------------------------------------------------------- root
ROOT = show(
    "S0",
    "A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$, disproving the $n\\log n$ optimality conjecture in that model.",
    "Reduce the product to a cyclic convolution of radix digits evaluated by Fourier-type transforms, make the two costly ingredients of those transforms (address rearrangement and butterfly arithmetic) cost a power of the logarithm less than a full scan per level by two rank-saving tape procedures, then assemble the algorithm, prove exactness and total the cost.",
    "Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both the movement and the arithmetic must be sped up.",
    "explicit",
    [S1, S2, S3, S4, S5, S6, S7, S8],
    page="sub-nlogn-multiplication",
    frm=["fixed-tape-model", "convolution", "radix-digit-convolution", "dft", "fft-butterfly",
         "recursive-power-saving", "nlogn-multiplier", "big-o", "turing-machine",
         "theta-omega-and-little-o-notation", "schoolbook-and-karatsuba-multiplication"],
    adds=[
        add("b", "digit width", "the number of bits in each radix digit, $b=\\lceil\\log_2n\\rceil$", "count"),
        add("p", "working precision", "the number of fractional bits of each stored complex coefficient, $p=6b$", "count"),
        add("d", "axis count", "the number of transform axes, a small power of $p$", "count"),
        add("T", "padded box size", "the number of entries of the padded power-of-two box, a power of two with $Tp=\\Theta(n)$", "count"),
    ],
    salient="The saving is a power of the logarithm, $1-\\kappa$ with the tiny $\\kappa=2^{-182}$, yet strictly positive; it traces back to the single strict inequality $s<Wm$ on the finite networks.",
    mot_quote="We therefore need savings in both movement and arithmetic.",
)

# --------------------------------------------------------- order check
def walk(n, out):
    if n["intention"] == "infer":
        out.append((n["id"], SRC.find(n["quote"]["quote"])))
    for c in n.get("children", []):
        walk(c, out)

pos_log = []
walk(ROOT, pos_log)
prev = -1
for id, p in pos_log:
    if p < prev:
        print("ORDER VIOLATION at", id, p, prev)
    prev = max(prev, p)

json.dump({"root": ROOT}, open('/home/user/openai-nlogn-wiki/runs/G4/exegenius/tasks/0003-argument.answer.json', 'w'), indent=1)
print("ok", len(pos_log), "infer steps")
