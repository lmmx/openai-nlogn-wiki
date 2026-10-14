import json, re, sys

SRC = open('/home/user/openai-nlogn-wiki/runs/Q1/sources/paper.tex').read()


def Q(start, end=None):
    """Exact quote from start snippet (must be unique) through end snippet."""
    n = SRC.count(start)
    if n != 1:
        sys.exit(f'start snippet occurs {n} times: {start!r}')
    i = SRC.index(start)
    if end is None:
        return SRC[i:i + len(start)]
    j = SRC.index(end, i)
    q = SRC[i:j + len(end)]
    if len(q) > 600:
        sys.exit(f'quote too long: {start!r}')
    return q


def ev(q):
    return {"source": "paper", "quote": q}


def infer(id, claim, quote, frm=None, deferred=False, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote)}
    if frm:
        n["from"] = frm
    if deferred:
        n["deferred"] = True
    if salient:
        n["salient"] = salient
    return n


def show(id, claim, method, mot_text, mot_source, children, page=None, frm=None,
         mot_quote=None, salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": {"text": mot_text, "source": mot_source,
                        "quote": ev(mot_quote) if mot_quote else None},
         "children": children}
    if page:
        n["page"] = page
    if frm:
        n["from"] = frm
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = adds
    return n


def B(symbol, name, meaning, relation='direct'):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


# ---------------------------------------------------------------- finite networks
bank = show(
    "S1.1",
    "A scalar linear network of $W$ wires, built from three stages of copy, gather, scatter and side-injection gates on triples, sends the two banks $(X_a,Y_a)$ to $(-Y_a,X_a)$ (a plain swap over $\\mathbb F_2$) and returns every scratch wire to its arbitrary initial value.",
    "Run an eight-row gate schedule per invocation that first subtracts the effect of the old scratch values, then injects $x$ into $y$ and finally undoes its own auxiliary updates; compose a forward, an inverse and a forward invocation over the three triple coordinates.",
    "Subtracting the old scratch contribution before using the scratch wires makes the net effect independent of their arbitrary initial values, and three add/subtract stages $y\\gets y+x$, $x\\gets x-y$, $y\\gets y+x$ realize an exchange of banks.",
    "explicit",
    [
        infer("S1.1.1",
              "For arbitrary initial scratch values a forward invocation adds $x_S$ to $y_S$ and changes nothing else, because the central coefficient ($|S\\cap T|\\bmod 2$, or $(|S\\cap T|-1)/2$) and the side coefficient cancel for all neighbouring distinct triples.",
              Q("For arbitrary initial values of its auxiliary wires, a forward", "unchanged."),
              frm=["triple-construction", "scratch-restoration"]),
        infer("S1.1.2",
              "Forward, inverse and forward invocations at stages 1, 2, 3 take $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
              Q("Starting from $(x,y)$, the three stages give", "then $(-y,x)$.")),
    ],
    page="bank-exchange",
    frm=["linear-network", "scratch-restoration", "triple-construction", "modular-arithmetic"],
    mot_quote=Q("The first two rows of\nthe following schedule remove", "the last two restore the scratch values."),
)

labels = show(
    "S1.2",
    "Every gate and terminal of either network can be labelled by a nondegenerate subspace of the $m$-dimensional space $\\mathcal F=F^{\\otimes3}$ so that labels are nested along every edge and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$; hence the absolute label changes sum to $Wm-2N+2L$ with $L=Ich$.",
    "Pair triple indicator vectors by a form under which neighbouring triples are orthogonal, expose one tensor factor per stage with prescribed incoming and outgoing labels, and assign common gate labels by the decomposition $A\\otimes F=(B\\otimes F)\\perp(P\\otimes F)$.",
    "Because neighbouring triple lines are orthogonal, a side wire's label can grow through $P\\otimes\\langle t_X\\rangle\\subset P\\otimes t_Y^\\perp$ without ever shrinking, so all loss of dimension is confined to the single return of each central wire.",
    "recoverable",
    [
        infer("S1.2.1",
              "With the rational form $x^{\\mathsf T}(I-J/9)y$ (bit network) or the binary dot product (complex network), every triple line is nondegenerate and neighbouring triple lines are orthogonal.",
              Q("Thus every triple line is nondegenerate, and neighboring triple lines", "either construction."),
              frm=["bilinear-forms", "triple-construction", "eigenvalues-of-a-matrix"]),
        infer("S1.2.2",
              "The stage transitions expose one tensor factor at each stage, and the outgoing labels of one stage are exactly the incoming labels of the next, starting at $U_a$ on $X_a$ and ending at $U_a^\\perp$ on $Y_a$.",
              Q("These transitions expose one tensor factor at each stage."),
              frm=["tensor-product"]),
        infer("S1.2.3",
              "Every edge joins comparable nondegenerate labels, the only decreasing edges are central-wire edges from time 3 to time 4 with loss $h$, and in the binary label space every nonzero residual has an orthonormal basis.",
              Q("Every edge joins comparable nondegenerate labels.", "loss is $h$.")),
    ],
    page="subspace-labels",
    frm=["bilinear-forms", "tensor-product", "triple-construction", "linear-algebra", "dot-product-and-orthogonality"],
)

S1 = show(
    "S1",
    "Two fixed finite networks (a bit network over $\\mathbb F_2$ and a complex network over $\\mathbb Z[i,1/2]$) exchange two banks while restoring scratch wires, and their label budgets lose $L<N/2$, so the total number $s$ of smaller calls their edges need satisfies $s<Wm$.",
    "Construct the three-stage bank exchange on triples of a 100-element set, label it with nested nondegenerate subspaces, and count the label-dimension changes.",
    "The number of smaller operations an edge needs is its label-dimension change, so a strict deficit in the total change is exactly what yields the saving.",
    "explicit",
    [
        bank,
        labels,
        infer("S1.3",
              "The loss ratios are $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$, both smaller than $1/2$.",
              Q("In particular, both are smaller than $1/2$."),
              salient="Both networks lose strictly less than half of the $N$ data dimensions, which is what leaves room for the extra source ranks and still gives $s<Wm$."),
    ],
    page="rank-deficit",
    frm=["linear-network", "triple-construction"],
    mot_quote=Q("The saving will come from keeping the total dimension lost on decreasing", "small relative to $N$."),
    salient="The networks must move every one of the $W$ roles, yet the total count $s$ of smaller calls stays strictly below $Wm$; this strict inequality is the only source of the power saving.",
    adds=[B("N", "data pairs", "The number of index triples $a\\in\\mathcal T^3$, i.e. the number of wires in each data bank.", "count"),
          B("L", "lost dimension", "The total dimension lost on decreasing edges of the labelled network.", "count"),
          B("h", "ground-set size", "The size $h=100$ of the ground set whose 3-element subsets index the banks.", "count")],
)

# ---------------------------------------------------------------- chunk interchange
bitif = show(
    "S2.1.1",
    "Assigning the projection $P_U$ to each vertex with label $U$ (and $-P_{U_a}$ to source $X_a$) gives fixed rational matrices with $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m$ on every role and edge ranks summing to $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$.",
    "Use projections onto the nested labels as frame matrices; the rank of a difference of nested projections is the label-dimension change, and the negative source projection adds one rank per data pair.",
    "Frames $\\Phi_M$ compose additively in $M$, so an edge needs a shear by the matrix difference, whose rank is the number of smaller interchanges; projections make that rank equal to the label residual counted in the budget.",
    "recoverable",
    [
        infer("S2.1.1.1",
              "For nested nondegenerate $U\\subset V$, $P_V-P_U$ is the projection onto $V\\cap U^\\perp$, so its rank is $\\dim V-\\dim U$.",
              Q("For $U\\subset V$ nondegenerate,", "orthogonal complement."),
              frm=["projection-onto-a-subspace"]),
        infer("S2.1.1.2",
              "On $X_a$ the endpoint difference is $P_{U_a^\\perp}-(-P_{U_a})=I_m$, and every other role has zero source and identity sink matrix.",
              Q("For an input $X_a$ the endpoint difference is", "=I_m$.")),
    ],
    page="bit-interface",
    frm=["rank-deficit", "subspace-labels", "frames", "address-shear", "linear-algebra", "projection-onto-a-subspace"],
)

shear = show(
    "S2.1.3",
    "For a fixed rational $m\\times m$ matrix $A$ of rank $a$, the shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ takes exactly $a$ interchanges of $b$-digit fields plus $O(V)$ work.",
    "Factor $A=E_1\\Pi E_2$ with lower triangular $E_1,E_2$, apply the triangular factors by controlled shifts, and realize each one of $\\Pi$ by add, interchange, subtract.",
    "Controlled shifts update a later field from earlier ones in linear time, and lower triangular coordinate changes only ever need that direction, so only the $a$ ones of $\\Pi$ need a costly interchange.",
    "explicit",
    [
        infer("S2.1.3.1",
              "Every rational $m\\times m$ matrix of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones.",
              Q("Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"),
              frm=["bruhat", "gaussian-elimination"]),
        infer("S2.1.3.2",
              "A lower triangular transformation of $H$ or of $D$ costs $O(V)$ by updating coordinates in descending physical order.",
              Q("A lower triangular transformation of $H$, or of $D$, costs $O(V)$:", "descending physical order."),
              frm=["controlled-shifts"]),
        infer("S2.1.3.3",
              "Each one of $\\Pi$ is realized as $D_j\\gets D_j+H_i$, $(H_i,D_j)\\gets(D_j,H_i)$, $D_j\\gets H_i-D_j$, using a single interchange.",
              Q("On an initial pair $(h,d)$ this sequence yields $(h+d,d)$.", "It uses just one interchange.")),
    ],
    page="matrix-shear",
    frm=["bruhat", "controlled-shifts", "modular-arithmetic", "linear-algebra", "address-shear"],
    mot_quote=Q("updates a later field using\nearlier fields in linear time.", "performed entirely in this direction."),
)

sched = show(
    "S2.1.7",
    "The recursion runs on one fixed set of tapes with only $O(V)$ extra work per node, for every depth and every spectator length.",
    "Before each child call park the $W-1$ inactive role streams on a stack tape and the descriptor on a descriptor stack, reuse the same role and work tapes in the child, and restore afterwards.",
    "A fixed machine cannot allocate new tapes per recursion depth, and parking costs only the node's own volume, so the recurrence's factor $s/W$ is not spoiled by temporary storage.",
    "explicit",
    [
        infer("S2.1.7.1",
              "Before a recursive call the $W-1$ inactive role streams are appended to the parking stack, the active stream is copied to the child area, and they are popped back on return.",
              Q("Before a recursive call, append the $W-1$ inactive role streams to the", "with separators.")),
        infer("S2.1.7.2",
              "Every push, pop, copy, positioning or erasure moves $O(V)$ symbols at a parent with $s$ children, giving exactly the additional $O(V)$ term.",
              Q("Each push, pop, copy, positioning operation, or erasure moves $O(V)$", "symbols at a parent node.")),
        infer("S2.1.7.3",
              "Descriptor work is $(\\log(2V_0))^{O(1)}=O(V_j)$ at every depth, so one finite machine serves every depth and spectator length.",
              Q("These observations establish one finite machine for every recursion", "every choice of spectator lengths.")),
    ],
    page="fixed-tape-schedule",
    frm=["stacks", "multitape-tm", "row-splitting"],
    mot_quote=Q("Temporary storage is\ntherefore not substituted", "in the factor $s/W$."),
)

pw = show(
    "S2.1",
    "For $e=m^k$, two disjoint chunks of $e$ radix-$q$ digits, preceded by a row field whose length is divisible by $W^k$, can be interchanged in $O(Ve^\\tau)$ time on fixed tapes.",
    "Split rows cyclically among the $W$ roles of the bit network, use shear frames $\\Phi_M$ so the network computes $H\\gets H+D$ on every role, implement each edge by recursive smaller interchanges, finish the interchange with two linear updates, and solve the volume-normalized recurrence.",
    "Each edge of rank $a$ costs $a$ smaller interchanges on streams of volume $V/W$, and the ranks sum to $s<Wm$, so multiplying the width by $m$ multiplies normalized cost by only $s/W<m^\\tau$.",
    "explicit",
    [
        bitif,
        infer("S2.1.2",
              "The relative rank deficits exceed $20\\cdot2^{-50}$, so $s_{\\rm b}/W_{\\rm b}<m^\\tau$ (and $s_{\\rm c}/W_{\\rm c}<m^\\sigma$) with $\\tau=\\sigma=1-2^{-50}$.",
              Q("Both exact deficits displayed above are greater than $20\\cdot2^{-50}$."),
              frm=["logarithms-and-exponent-rules"]),
        shear,
        infer("S2.1.4",
              "On the row-split role streams with frames $\\Phi_{M_v}$, the common-frame identity and $M_{\\rm out}-M_{\\rm in}=I_m$ give $H\\gets H+D$ on every original row, including scratch rows with arbitrary initial values.",
              Q("The result\nis $H\\leftarrow H+D$ on every original row", "whose initial values were arbitrary."),
              frm=["row-splitting", "frames", "address-shear"]),
        infer("S2.1.5",
              "The updates $D\\gets D-H$, $H\\gets H+D$, $D\\gets H-D$ send $(H,D)$ to $(D,H)$, and only the middle shear uses the network.",
              Q("The transformation\nsends $(H,D)$ to $(D,H)$.")),
        infer("S2.1.6",
              "With $F_k$ the time divided by volume, $F_k\\le(s/W)F_{k-1}+O(1)$, and $s/W<m^\\tau$ gives $F_k=O(e^\\tau)$.",
              Q("Hence $F_k=O(e^\\tau)$."),
              frm=["power-saving-recursion", "geometric-series", "recurrences-and-recursion-trees"]),
        sched,
    ],
    page="power-width-interchange",
    frm=["row-splitting", "frames", "address-shear", "power-saving-recursion", "rank-deficit", "elementary-streams"],
    mot_quote=Q("An edge matrix of rank $a$ will require $a$ smaller interchanges.", "saves a power of the chunk width."),
)

S2 = show(
    "S2",
    "The fast address-chunk interchange: one fixed procedure interchanges two disjoint $u$-bit address fields of any array in $O(Vu^\\tau)$ time with $\\tau=1-2^{-50}$.",
    "Prove the power-width case with enough rows first, then supply rows from the top digits of the chunks, split a general width into base-$m$ pieces, and pad binary chunks to radix-$q$ ranges.",
    "A few high digits of the chunks themselves supply the rows the power-width case needs, and moving them costs less than the final bound.",
    "explicit",
    [
        pw,
        infer("S2.2",
              "After interchanging and joining the top $\\rho$ digits of each chunk, those digits form a row field of range $q^{2\\rho}\\ge W^k$ before both remaining chunks, padded to a multiple of $W^k$ at less than twice the volume.",
              Q("In the two middle orders, the first two fields form a row field of range")),
        infer("S2.3",
              "Writing the remaining width in base $m$ and applying the power-width interchange to each piece costs $O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau)$.",
              Q("The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a", "geometric sum of the stated order."),
              frm=["geometric-series"]),
        infer("S2.4",
              "Padding $[2^u]$ to $[q^e]$ changes the volume by a fixed factor and $e=O(u)$, so the bound is $O(Vu^\\tau)$.",
              Q("Since $e=O(u)$ for fixed $q$, the bound is", "$O(Vu^\\tau)$.")),
    ],
    page="chunk-swap",
    frm=["elementary-streams", "array-layout", "bitwise-exclusive-or"],
    mot_quote=Q("Rows for a general array can be supplied by a few of its own high digits.", "cost less than the final bound."),
    salient="A pure permutation of addresses is done faster than $u$ passes over the data, by computing XOR combinations of data that cancel out by the end.",
    adds=[B("u", "chunk width", "The number of address bits in each of the two chunks being interchanged.", "count"),
          B("e", "digit width", "The number of radix-$q$ digits in each chunk handled by one recursive interchange.", "count"),
          B("q", "fixed prime radix", "A fixed odd prime avoiding all denominators of the network's matrices, used as the digit radix.")],
)

# ---------------------------------------------------------------- simultaneous layer
phase = show(
    "S3.1.1",
    "With phase frames $\\mathcal C_U=H^{\\otimes m}\\operatorname{diag}(i^{q_U(x)})H^{\\otimes m}$, each edge's frame change of the complex network is a product of one translation kernel $aI+bX_v$ (or its inverse) per orthonormal residual vector, these total $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}<W_{\\rm c}m$, and after diagonal corrections every role receives $C^{\\otimes m}$.",
    "Use weight additivity modulo four for orthogonal binary vectors to split each frame change into one phase per residual basis vector, conjugate by Hadamard matrices to turn each phase into a translation kernel, and fix the $X_a\\to Y_a$ route with $Z$ signs.",
    "All phase frames are diagonalized by the same $H^{\\otimes m}$, so frame changes are diagonal phases, and an orthonormal residual basis splits such a phase into independent one-direction factors, each one smaller $C$ layer.",
    "recoverable",
    [
        infer("S3.1.1.1",
              "If $z\\cdot w=0$ over $\\mathbb F_2$, then $\\operatorname{wt}(z+w)\\equiv\\operatorname{wt}(z)+\\operatorname{wt}(w)\\pmod 4$, so $q_V-q_U$ is a sum of one term per orthonormal residual vector.",
              Q("If $z\\cdot w=0$, the intersection cardinality is even, so weight is", "additive modulo four."),
              deferred=True, frm=["hamming-weight"]),
        infer("S3.1.1.2",
              "Each such phase $i^{\\pm[v\\cdot x]}$ becomes, after Hadamard conjugation, the kernel $aI+bX_v$ or its inverse.",
              Q("The displayed phase therefore\nbecomes $aI+bX_v$ or its inverse."),
              deferred=True),
        infer("S3.1.1.3",
              "Applying $Z$ signs on the 27 support coordinates and the scalar $i^{27k}$ turns the $X_a\\to Y_a$ route into $C^{\\otimes mk}$ as well.",
              Q("The operator\non this pair is therefore $C^{\\otimes mk}$ as well."),
              deferred=True),
    ],
    page="phase-interface",
    frm=["kernel-c", "subspace-labels", "rank-deficit", "frames", "bilinear-forms", "tensor-product", "hamming-weight"],
)

packed = show(
    "S3.1.6",
    "For three $L$-bit chunks $x,y,z$ with $L=fK$, the XORs $y_{j_i}\\gets y_{j_i}\\oplus x_{j_i}$ at positions $j_i=\\rho+iK$ are performed while restoring $z$, in time $O(V(L^\\tau+1))$ under the layer's parameter growth.",
    "Use eight packed cyclic shifts of whole chunk ranges, each controlled by $x$ and guarded by parities of $z$, which flip the selected parities segment by segment, then correct the small address-determined set where guards overflow by extracting and radix-sorting those records.",
    "The correction depends only on addresses, so the time bound is worst-case over all payloads; and the exceptional set is so small that sorting it costs $o(V)$.",
    "explicit",
    [
        infer("S3.1.6.1",
              "The eight conditional updates flip the parity of $u$ exactly when $c=1$, preserve both quotients by two and restore the auxiliary integer $w$.",
              Q("Thus the parity of $u$\nis flipped precisely when $c=1$", "is restored.")),
        infer("S3.1.6.2",
              "By the union bound over the $2(f-1)$ guards, the exceptional set satisfies $|\\mathcal B|\\le\\delta_{\\rm bad}M$ with $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$.",
              Q("the union bound over the $2(f-1)$ guards gives"),
              frm=["union-bound"]),
        infer("S3.1.6.3",
              "The packed shifts $S_0$ and the ideal map $T_0$ agree off $\\mathcal B$, so $T_0S_0^{-1}$ fixes the complement of $\\mathcal B$ and permutes $\\mathcal B$.",
              Q("Thus $T_0S_0^{-1}$ fixes $\\mathcal B^c$ and permutes $\\mathcal B$.")),
        infer("S3.1.6.4",
              "Extracting the exceptional records with destination ranks, radix-sorting them and reinserting them implements $T_0$ everywhere.",
              Q("This implements $T_0$ everywhere."),
              frm=["radix-sort-and-stable-sorting"]),
    ],
    page="packed-addition",
    frm=["chunk-swap", "controlled-shifts", "elementary-streams", "radix-sort-and-stable-sorting", "union-bound", "bitwise-exclusive-or"],
    mot_quote=Q("The correction depends only on addresses, so the time bound is", "worst-case over all payloads."),
)

rec = show(
    "S3.1",
    "The tensor product $C^{\\otimes D}$ of the kernel $C$ on the selected bits of $D\\le d$ chunks is computed exactly in $O(Vd^{\\lambda'})$ time, by recursion in which a group of $e$ selected axes uses $s_{\\rm c}$ children on $e/m$ axes, each on a stream of volume $V/W$.",
    "Run the complex network on row-split role streams with column phase frames, implement each edge's frame change by a binary change of basis (packed row additions) and one recursive $C^{\\otimes e/m}$ call per residual vector, and unroll the volume-normalized recurrence.",
    "Phase frames express a $C$ tensor product through smaller groups of selected bits separated by binary changes of basis, so the rank deficit $s<Wm$ becomes a power saving in $d$.",
    "explicit",
    [
        phase,
        infer("S3.1.2",
              "Conjugating by an address permutation $\\mathcal P_M$ whose first columns are the residual basis turns each directional kernel into $C^{\\pm1}$ on coordinate slot $h$, i.e. one child operation on the $f$ axes of that slot.",
              Q("This is one child operation\non the $f$ axes in slot $h$."),
              frm=["linear-algebra"]),
        infer("S3.1.3",
              "An inverse kernel needs only one forward child, since $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$.",
              Q("A negative directional kernel still requires only one\nforward child, because")),
        infer("S3.1.4",
              "The change of basis $\\mathcal P_M$ is a fixed number of row additions, each XORing corresponding selected positions of two whole slots.",
              Q("Thus one row addition changes corresponding selected\npositions in two whole slots."),
              frm=["gaussian-elimination"]),
        infer("S3.1.5",
              "Applying the network with these column frames to $e=mf$ selected axes gives exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and yields $C^{\\otimes e}$ on every role.",
              Q("Summing its residual dimensions gives exactly", "the $f=e/m$ axes of one slot.")),
        packed,
        infer("S3.1.7",
              "Each binary change of basis and its inverse cost $O(V((eK)^\\tau+1))$ on a stream of volume $V$.",
              Q("the complete change of basis and its inverse therefore cost", "on a stream of volume $V$.")),
        infer("S3.1.8",
              "Applying $C$ individually to the first $q_0$ chunks lets their bits serve as a row index of range at least $W^{k_0}$, padded to a multiple of $W^{k_0}$.",
              Q("Otherwise apply \\(C\\) individually on the selected bits of the first", "in \\(O(V\\log d)\\) time."),
              frm=["row-splitting"]),
        infer("S3.1.9",
              "The normalized cost satisfies $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$, because the $s$ children run on streams of volume $V/W$.",
              Q("Dividing by\nthe current volume \\(V\\) gives the factor \\(s/W\\)."),
              frm=["power-saving-recursion", "recurrences-and-recursion-trees"]),
        infer("S3.1.10",
              "Summing over the base-$m$ pieces and the row preprocessing gives normalized cost $O(d^{\\lambda'})$ for $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$.",
              Q("Adding their costs and the row preprocessing gives"),
              frm=["geometric-series"]),
    ],
    page="recursive-c-layer",
    frm=["row-splitting", "power-saving-recursion", "fixed-tape-schedule", "kernel-c", "frames", "linear-network", "gaussian-elimination"],
    mot_quote=Q("Its phase\nframes express a $C$ tensor product", "separated by binary changes of basis."),
)

S3 = show(
    "S3",
    "The simultaneous butterfly layer: on an array of polynomial records with $D\\le d$ consecutive $K$-bit chunks, $H_0$ applied to one common bit position of every chunk, followed by truncation $Q_p$, is computed in $O(Vd^{\\lambda'})$ time with error below $\\sqrt2\\,2^{-p}$.",
    "Write $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$, compute $C^{\\otimes D}$ recursively with the complex network, keep every intermediate value exact in a guarded fixed-point format, and truncate once at the end.",
    "Separate butterfly factors would need $D$ whole-array passes, whereas the network recursion gives a power saving in $d$.",
    "explicit",
    [
        rec,
        infer("S3.2",
              "Every chain of arithmetic in one layer has length below $C_0d^{C_1}$, so reserving $p+\\Delta$ fractional and $\\Delta+3$ integer bits ($\\Delta=o(p)$) keeps every intermediate coefficient exact.",
              Q("Thus reserving \\(p+\\Delta\\)\nfractional bits", "prevents overflow."),
              frm=["fixed-point"]),
        infer("S3.3",
              "The identity $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$ converts the exact $C$ layer into the normalized layer $\\mathcal H$.",
              Q("converts the resulting exact $C$-layer to $\\mathcal H$."),
              frm=["kernel-c"]),
        infer("S3.4",
              "$\\mathcal H$ maps disk arrays to disk arrays, and the single final truncation keeps the disk with error below $\\sqrt2\\,2^{-p}$.",
              Q("Thus $\\mathcal H$ maps disk arrays to disk\narrays,", "error less than $\\sqrt2\\,2^{-p}$"),
              frm=["normalized-butterfly"]),
    ],
    page="simultaneous-layer",
    frm=["normalized-butterfly", "kernel-c", "fixed-point", "array-layout"],
    mot_quote=Q("whereas separate butterfly\nfactors would require $D$ whole-array passes."),
    salient="The cost grows only like $d^{\\lambda'}$ with $\\lambda'<1$: applying butterflies on $d$ axes at once is cheaper than $d$ separate passes.",
    adds=[B("D", "active chunks", "The number of consecutive $K$-bit address chunks whose selected bit the layer acts on.", "count"),
          B("K", "chunk width", "The number of address bits in each chunk, $K=\\lfloor d^c\\rfloor$.", "count"),
          B("C", "two-point kernel", "The Gaussian-dyadic $2\\times2$ matrix $aI+bX$ that the complex network applies on every role.")],
)

A = show(
    "A",
    "Two tape procedures save over plain scanning: address chunks of width $u$ are interchanged in $O(Vu^\\tau)$ time, and a simultaneous normalized butterfly layer on $D\\le d$ chunks costs $O(Vd^{\\lambda'})$, with fixed $\\tau,\\lambda'<1$.",
    "Build each procedure from its own fixed linear network that exchanges two banks and restores scratch wires, apply the network pointwise to row-split role streams with frames chosen so every edge is a few smaller calls, and solve the volume-normalized recurrence.",
    "Because the smaller calls number $s<Wm$ and each acts on volume $V/W$, multiplying the parameter by $m$ raises normalized cost by only $s/W<m$; this strict inequality is the source of the power saving.",
    "explicit",
    [S1, S2, S3],
    frm=["linear-network", "row-splitting", "frames", "power-saving-recursion"],
    mot_quote=Q("This strict inequality\nis the source of the power saving."),
    adds=[B("m", "label dimension", "The dimension $m=h^3=10^6$ of the label space, i.e. the factor by which the parameter shrinks per recursion level.", "count"),
          B("W", "wire count", "The number of wires (roles) of a finite network, including scratch wires.", "count"),
          B("s", "smaller calls", "The total number of smaller recursive calls needed over all edges of a network.", "count"),
          B("\\tau", "interchange exponent", "The fixed exponent $1-2^{-50}$ in the interchange cost $O(Vu^\\tau)$."),
          B("\\lambda'", "layer exponent", "The fixed exponent $1-2^{-54}$ in the butterfly-layer cost $O(Vd^{\\lambda'})$.")],
)

# ---------------------------------------------------------------- synthetic convolution
layout = show(
    "S4.1",
    "On $d-1$ power-of-two axes of length $2^{\\ell}$ or $2^{\\ell-1}$ over $\\mathcal R_r$, the forward synthetic transform $LBF_{\\boldsymbol t}^-$ and its opposite $F_{\\boldsymbol t}^+B^{-1}L^{-1}$ are computed with error below $\\sqrt2\\ell\\,2^{-p}$ at cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
    "Use decimation-in-frequency rounds of $H_0$ butterflies and monomial twiddles, leaving outputs in bit-reversed order; move bit slots so each round's selected bits sit at a common offset in consecutive $K$-bit chunks; run each round with the simultaneous layer and truncate once per round.",
    "The simultaneous layer applies only when the participating axes' selected bits sit at a common offset in consecutive $K$-bit chunks, so the layout must be built first.",
    "explicit",
    [
        infer("S4.1.1",
              "The decimation-in-frequency recursion with monomial twiddles computes $F_t^-$ and stores entry $j$ at bit-reversed slot $\\operatorname{rev}_a(j)$.",
              Q("entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$."),
              frm=["synthetic-transform"]),
        infer("S4.1.2",
              "Running the recursion in reverse implements the opposite transform $F_t^+B_t^{-1}$ directly on the stored order.",
              Q("Thus the two\nexact procedures implement")),
        infer("S4.1.3",
              "On several axes the steps of one round group into a parallel butterfly $\\mathcal H$ followed by one recordwise monomial $J_E$.",
              Q("Consequently the individual axis steps may be grouped as a parallel", "$J_E$.")),
        infer("S4.1.4",
              "The layout $L$ uses at most $Dq-1$ chunk exchanges of width $K$, costing $O(Tp\\,pK^{\\tau-1})$.",
              Q("This uses at most $Dq-1$\nexchanges of width-$K$ address chunks", "nonadjacent."),
              frm=["chunk-swap"]),
        infer("S4.1.5",
              "Each round runs the simultaneous layer at cost $O(Tpd^{\\lambda'})$, for $O(Tp\\ell d^{\\lambda'})$ in total.",
              Q("The simultaneous-layer procedure therefore applies at cost", "in total."),
              frm=["simultaneous-layer"]),
        infer("S4.1.6",
              "Because truncation commutes with the signed coefficient permutation $J_E$, each round equals one truncation after an exact contraction, so errors add to below $\\sqrt2\\ell\\,2^{-p}$.",
              Q("Thus the actual forward call sequence returns exactly the result of", "after the exact contraction round."),
              frm=["contraction-errors"]),
    ],
    page="transform-layout",
    frm=["synthetic-transform", "simultaneous-layer", "chunk-swap", "elementary-streams", "contraction-errors", "normalized-butterfly", "negacyclic-ring"],
    mot_quote=Q("To apply Proposition~\\ref{prop:simultaneous-layer} in a transform round,", "consecutive $K$-bit chunks."),
)

packing = show(
    "S4.2",
    "For disk-grid polynomials $f,g\\in\\mathcal R_r$, the normalized product $Q_p(fg/r)$ is computed exactly up to its final truncation in $O(rp\\log(rp))$ time on fixed tapes.",
    "Evaluate the signed integer coefficient polynomials at $B_0=2^{4p}$, multiply four pairs with the established $O(N\\log N)$ multiplier, extract centered coefficients block by block, fold modulo $y^r+1$ and truncate.",
    "Kronecker substitution turns all coefficient products into a few long integer products, which the established multiplier does fast; blocks of $4p$ bits exceed twice every product coefficient, so centered residues recover the signed coefficients exactly.",
    "recoverable",
    [
        infer("S4.2.1",
              "Each signed evaluation $A_u=u(B_0)$ has magnitude below $B_0^r/2$ and fits in $4pr$ bits.",
              Q("shows that each magnitude fits in $4pr$ bits.")),
        infer("S4.2.2",
              "Since every product coefficient satisfies $|h_j|<B_0/2$, the centered residue extracted at block $j$ equals $h_j$.",
              Q("Thus $\\widehat h_j=h_j$.")),
        infer("S4.2.3",
              "Four exact integer products dominate the linear packing, extraction, folding and truncation costs.",
              Q("Four exact integer products dominate the linear", "truncation costs."),
              frm=["hvdh-multiplier"]),
    ],
    page="signed-packing",
    frm=["hvdh-multiplier", "negacyclic-ring", "fixed-point", "two-s-complement-representation", "polynomials"],
)

S4 = show(
    "S4",
    "Normalized cyclic convolution $\\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ is approximated with error below $\\sqrt2M(3\\ell+1)2^{-p}$ at cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
    "Apply two forward synthetic transforms, multiply the records pointwise in their retained stored order by signed packing, apply one opposite transform consuming that order, and scale exactly by $M$.",
    "Pointwise multiplication commutes with applying the same record permutation to both operands, so the stored frequency order never has to be undone between the forward and opposite transforms.",
    "explicit",
    [
        layout,
        packing,
        infer("S4.3",
              "Since $F_{\\boldsymbol t}^-(f*g)=M(F_{\\boldsymbol t}^-f)(F_{\\boldsymbol t}^-g)$ and $F^+_{\\boldsymbol t}F^-_{\\boldsymbol t}=I/M$, scaling the opposite transform of the stored pointwise products by $M$ gives exactly $\\mathcal M_r(f,g)$.",
              Q("The displayed normalization identity identifies its exact scaling", "with $\\mathcal M_r(f,g)$."),
              frm=["dft", "cyclic-convolution"]),
        infer("S4.4",
              "Two forward errors, the product truncation and the opposite error add through contractions, and the scale $M$ gives error below $\\sqrt2M(3\\ell+1)2^{-p}$.",
              Q("The final exact multiplication by $M$ therefore gives error less than"),
              frm=["contraction-errors"]),
    ],
    page="synthetic-convolution",
    frm=["dft", "cyclic-convolution", "negacyclic-ring", "contraction-errors", "synthetic-transform"],
    mot_quote=Q("Pointwise multiplication commutes with applying the same record", "to both operands."),
    adds=[B("T", "box size", "The number $T=\\prod_i t_i$ of entries of the padded power-of-two box.", "count"),
          B("M", "record count", "The number $M=T/r$ of polynomial records, one per address of the first $d-1$ axes.", "count"),
          B("\\ell", "log record length", "The exponent $\\ell=\\log_2 r$ of the record length.", "count")],
)

# ---------------------------------------------------------------- resampling
S5 = show(
    "R.1",
    "For coprime $s<t$ with enough separation, $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ for linear contractions $A,B_0$ that have disk-grid approximations with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$, the coordinate permutations $P_s,P_t$ being kept inside the identity.",
    "Take Harvey and van der Hoeven's Gaussian identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$, invert $\\mathsf T$ on the left by $\\mathsf DN^{-1}C$ with a Neumann series, and normalize the three factors; reuse their ordered numerical algorithms without the two sorts.",
    "The original implementation executes $P_t$ and $P_s^{-1}$ as label-and-sort operations costing $O(tp\\log t)$ each, which is too slow; keeping them in the identity avoids the sorts.",
    "explicit",
    [
        infer("R.1.1",
              "Since $\\alpha^2\\theta>1$, $\\|N-I\\|<1/2$ and $N=C\\mathsf T\\mathsf D$ is invertible.",
              Q("Thus $\\|N-I\\|<1/2$, so $N$ is invertible", "by the Neumann series.")),
        infer("R.1.2",
              "The left inverse $\\mathsf DN^{-1}C$ of $\\mathsf T$ and the normalizations give $B_0P_tF_tA=2^{-2\\alpha^2}P_sF_s$.",
              Q("which is \\eqref{eq:no-sort-one-dimensional}.")),
        infer("R.1.3",
              "The ordered approximations $\\widetilde A$ and $\\widetilde B_0$ have errors $16p<p^2$ and $4+3p^2/4<p^2$.",
              Q("Contraction of the exact maps yields errors less than $16p<p^2$ and", "respectively."),
              frm=["contraction-errors"]),
    ],
    page="resampling-retained",
    frm=["gaussian-resampling", "dft", "contraction-errors", "hvdh-multiplier"],
    mot_quote=Q("The original proof of Proposition~4.7(ii) implements", "each costing $O(tp\\log t)$."),
    adds=[B("\\alpha", "Gaussian width", "The integer width parameter of the Gaussian kernels used in resampling.")],
)

S6 = show(
    "R.2",
    "On $d$ axes, $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$; the linewise approximations of $\\mathcal A,\\mathcal B_0$ have error below $dp^2$, line work $O(dTp^{3/2+\\delta}\\alpha)$ and axis movement $O(Tp\\,d^2(1+\\ell^\\tau))$ in the padded box.",
    "Tensor the one-dimensional identity, apply the one-dimensional maps one axis at a time to the lines of the padded power-of-two box, and expose each axis by fast chunk interchanges.",
    "The chunk-swap procedure supplies the movement of the axis fields at a cost that stays small even as the number of axes grows.",
    "explicit",
    [
        infer("R.2.1",
              "Tensoring the one-dimensional identity gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$.",
              Q("Tensoring \\eqref{eq:no-sort-one-dimensional} proves"),
              frm=["tensor-product"]),
        infer("R.2.2",
              "Each axis map is a contraction with error below $p^2$, so the $d$ axis maps compose to error below $dp^2$.",
              Q("Composing the $d$ axis maps gives error less than $dp^2$."),
              frm=["contraction-errors"]),
        infer("R.2.3",
              "Each adjacent axis interchange costs $O(Tp(1+\\ell^\\tau))$, and exposing and restoring all axes needs $O(d^2)$ of them.",
              Q("Each adjacent interchange therefore\ncosts $O(Tp(1+\\ell^\\tau))$."),
              frm=["chunk-swap"]),
    ],
    page="tensor-resampling",
    frm=["resampling-retained", "tensor-product", "chunk-swap", "elementary-streams", "contraction-errors"],
    mot_quote=Q("The chunk-swap algorithm supplies the movement of the", "when the number of axes grows."),
    adds=[B("\\gamma", "resampling scale", "The exponent $\\gamma=2d\\alpha^2$ of the power of two by which the compressed result is rescaled.", "count")],
)

S7 = show(
    "R.3",
    "The middle factor is a chirped convolution, $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$, and the retained source permutation cancels: $(RF^+_{\\boldsymbol s})[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
    "Compare kernel coefficients for the chirp identity; for the cancellation, use that $F^+_{\\boldsymbol s}$ intertwines the dilation $R$ with $R^{-1}$ and that permutations commute with pointwise products.",
    "The chirp performs the frequency change in $Q$ without executing $Q$ as a separate permutation, and the cancellation means $R$ never has to be executed either.",
    "explicit",
    [
        infer("R.3.1",
              "The coefficient of $u_{\\boldsymbol k}$ in $\\overline a\\cdot(a*(\\overline a\\cdot u))/T$ is $T^{-1}\\exp(2\\pi i\\sum_i s_ij_ik_i/t_i)$, which is the coefficient of $QF_{\\boldsymbol t}$.",
              Q("This is precisely the coefficient in $QF_{\\boldsymbol t}$, because", "negative-sign transform."),
              frm=["bluestein"]),
        infer("R.3.2",
              "Since each $t_i$ is a unit modulo $s_i$, $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$.",
              Q("Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives"),
              frm=["modular-arithmetic"]),
        infer("R.3.3",
              "With the normalized convolution rule, the opposite transform of the product of permuted forward transforms equals $(u*v)/S^2$.",
              Q("proving \\eqref{eq:source-permutation-cancel}."),
              frm=["dft", "cyclic-convolution"]),
    ],
    page="source-perm-cancel",
    frm=["bluestein", "dft", "cyclic-convolution", "resampling-retained", "tensor-product"],
    mot_quote=Q("The chirp identity below performs the frequency change", "separate permutation of the array."),
    salient="The permutation $R$ that resampling leaves behind disappears exactly from the convolution, so it never costs a sort.",
)

R = show(
    "R",
    "The prime-length source transform factors through power-of-two transforms: $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, where $QF_{\\boldsymbol t}$ is a chirped cyclic convolution and the leftover permutation $R$ cancels in the convolution.",
    "Use Gaussian resampling with both coordinate permutations retained in the identity, extend it linewise to many axes, and remove the permutations by Bluestein's chirp and by cancellation.",
    "The usual implementation sorts twice on each coordinate; keeping both permutations in the formula and computing the formula directly avoids those sorts.",
    "explicit",
    [S5, S6, S7],
    frm=["gaussian-resampling", "dft", "bluestein"],
    mot_quote=Q("Its usual implementation sorts twice on each", "compute that formula directly."),
    adds=[B("S", "source size", "The product $S=\\prod_i s_i$ of the distinct prime axis lengths.", "count")],
)

# ---------------------------------------------------------------- assembly
S8 = show(
    "S8",
    "The choices $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, the power of two $T\\in[4n/b,8n/b)$, axis lengths $t_i\\in\\{r/2,r\\}$, distinct odd primes $s_i$ just below $t_i$ and the fixed rational exponents satisfy every hypothesis of the layer, transform and resampling lemmas, with $Tp=\\Theta(n)$ and all parameters found in $o(n)$ time.",
    "Fix conservative rational exponents, derive the size relations, find primes in short intervals below each $t_i$ by an explicit prime-interval bound and trial division, and check the radix-digit capacity.",
    "The prime lengths must be close to the powers of two so that their product fills a fixed fraction of the padded box, while each ratio $t_i/s_i$ leaves enough separation for resampling.",
    "explicit",
    [
        infer("S8.1",
              "The fixed rationals $\\tau=\\sigma=1-2^{-50}$, $\\lambda=1-2^{-52}$, $c=2^{-56}$, $\\lambda'=1-2^{-54}$, $\\epsilon=2^{-75}$ satisfy all layer conditions.",
              Q("The layer conditions hold with room to spare:")),
        infer("S8.2",
              "The sizes satisfy $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$ and $r=2^{\\Theta(p^{1-\\epsilon})}$ with comparison constants fixed for all input lengths.",
              Q("The comparison constants can be fixed for every input length at once."),
              frm=["logarithms-and-exponent-rules"]),
        infer("S8.3",
              "The intervals $(1-2\\eta)t_i<s\\le(1-\\eta)t_i$ contain more than $d$ primes, so distinct odd primes $s_i$ can be chosen there.",
              Q("We may therefore choose distinct odd primes satisfying"),
              frm=["prime-numbers-and-trial-division"]),
        infer("S8.4",
              "Bernoulli's inequality gives $T/2<S<T$.",
              Q("Together with $s_i<t_i$, this gives $T/2<S<T$."),
              frm=["bernoulli-s-inequality"]),
        infer("S8.5",
              "Every hypothesis of the one-dimensional resampling lemma holds for all sufficiently large inputs.",
              Q("Thus every hypothesis of Lemma~\\ref{lem:no-sort-resampling} holds for", "all sufficiently large input lengths.")),
        infer("S8.6",
              "The prime search by trial division takes $n^{o(1)}=o(n)$ time.",
              Q("Since $p=6\\lceil\\log_2 n\\rceil=\\Theta(\\log n)$, the search takes", "$n^{o(1)}=o(n)$ time."),
              frm=["prime-numbers-and-trial-division"]),
        infer("S8.7",
              "The product of the two radix-$2^b$ digit polynomials has degree below $S$, so convolution modulo $x^S-1$ has no wraparound, and its coefficients are below $2^{3b}$.",
              Q("Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
              frm=["radix-reduction"]),
    ],
    page="parameters",
    frm=["big-o", "logarithms-and-exponent-rules", "prime-numbers-and-trial-division", "bernoulli-s-inequality", "resampling-retained", "radix-reduction", "floor-ceiling-and-rounding"],
    mot_quote=Q("their product must occupy a fixed fraction of the padded box,", "enough separation for resampling."),
    adds=[B("b", "digit width", "The number of bits $b=\\lceil\\log_2 n\\rceil$ in each radix digit.", "count")],
)

S9 = show(
    "S9",
    "The map $\\Phi:x\\mapsto\\prod_ix_i^{\\mu_i}$ is a convolution-preserving isomorphism $\\mathbb C[x]/(x^S-1)\\to\\bigotimes_i\\mathbb C[x_i]/(x_i^{s_i}-1)$, and it, its inverse and their padding cost $O(Tp\\,d^2(1+\\ell^\\tau))$ on tape.",
    "Write each coefficient index in mixed radix, compute the axis coordinates by the triangular formula $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j \\bmod s_i$, and realize it by prefix-controlled cyclic shifts after reversing the axis order with chunk interchanges.",
    "Choosing coordinate powers that make the Chinese-remainder change of order triangular turns it into a sequence of controlled cyclic shifts, each linear-time.",
    "explicit",
    [
        infer("S9.1",
              "The image of $x$ has order $S$, so its powers run through all target monomials once, and $\\Phi$ is an isomorphism preserving cyclic convolution.",
              Q("Hence\n$\\Phi$ is an isomorphism and preserves cyclic convolution."),
              frm=["chinese-remainder-theorem", "cyclic-convolution"]),
        infer("S9.2",
              "The axis-$i$ coordinate of $\\Phi(x^k)$ is $a_i+\\mu_i\\sum_{j<i}a_jP_j \\bmod s_i$, depending only on lower-index digits.",
              Q("Indeed terms with $j>i$ are divisible by $s_i$, and $\\mu_iP_i=1$ modulo", "$s_i$.")),
        infer("S9.3",
              "Each triangular step is a bijection of the padded box preserving the valid set, so zero padding stays zero.",
              Q("Consequently\nzero padding remains zero after every step."),
              frm=["controlled-shifts"]),
        infer("S9.4",
              "With $O(d^2)$ axis moves by chunk interchange, $\\Phi$, its inverse and their padding cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
              Q("Therefore the map $\\Phi$, its inverse, and", "their padding operations cost"),
              frm=["chunk-swap"]),
    ],
    page="crt-map",
    frm=["chinese-remainder-theorem", "cyclic-convolution", "controlled-shifts", "chunk-swap", "elementary-streams", "array-layout", "permutations-and-cycle-notation"],
    mot_quote=Q("The following map uses that\nalgebraic split, with coordinate powers", "controlled cyclic shifts."),
)

twist = show(
    "S10.1",
    "Normalized complex cyclic convolution on the $d$ power-of-two axes satisfies $\\mathcal M_{\\mathbb C}(f,g)=D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$, and its computed version is a bilinear approximation built from the ring convolution.",
    "Twist the last coordinate by $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$, regard each last-coordinate line as one record of $\\mathcal R_r$, convolve over the ring, and untwist.",
    "The fast convolution works in $\\mathbb C[y]/(y^r+1)$, whose wrap is negacyclic, while the chirp needs cyclic convolution; the twist's negative wrap reproduces the cyclic wrap exactly once removed.",
    "explicit",
    [
        infer("S10.1.1",
              "For $k+l=j+hr$, a twisted product term carries $\\zeta^{k+l}(-1)^h=\\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
              Q("Untwisting therefore recovers the cyclic coefficient with the correct", "sign."),
              frm=["complex-numbers"]),
        infer("S10.1.2",
              "Because the last coordinate is already the contiguous polynomial suffix, the identification $\\iota$ needs no payload movement.",
              Q("Hence $\\iota$ and\n$\\iota^{-1}$ change only the shape descriptor", "component formats agree.")),
    ],
    page="coefficient-twist",
    frm=["negacyclic-ring", "cyclic-convolution", "synthetic-convolution", "fixed-point", "complex-numbers"],
    mot_quote=Q("A phase twist changes the last cyclic coordinate into a polynomial", "after the twist is removed."),
)

S10 = show(
    "S10",
    "The computed source transform $\\widetilde{\\mathscr F}$ (Gaussian expansion, chirp transform via twisted ring convolution, compression, scale $2^\\gamma$) has exact counterpart $RF_{\\boldsymbol s}$, and its conjugate $\\widetilde{\\mathscr F}^+$ has exact counterpart $RF^+_{\\boldsymbol s}$.",
    "Compose the linewise approximation of $\\mathcal A$, the computed chirp transform $\\overline{\\widetilde a}\\cdot\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,\\overline{\\widetilde a}\\cdot x)$, the linewise approximation of $\\mathcal B_0$, and an exact shift by $\\gamma$; obtain the opposite sign by conjugation.",
    "The tensor resampling identity writes $RF_{\\boldsymbol s}$ as contractions around $QF_{\\boldsymbol t}$, and the chirp identity turns $QF_{\\boldsymbol t}$ into a cyclic convolution that the twisted ring convolution computes, so no permutation is ever executed.",
    "recoverable",
    [
        twist,
        infer("S10.2",
              "With exact phases and exact convolution the computed chirp transform becomes $\\overline a\\cdot\\mathcal M_{\\mathbb C}(a,\\overline a\\cdot x)=QF_{\\boldsymbol t}x$.",
              Q("Replacing the approximations\nby exact phases and exact convolution gives"),
              frm=["bluestein"]),
        infer("S10.3",
              "The opposite-sign procedure $\\widetilde{\\mathscr F}^+(z)=\\overline{\\widetilde{\\mathscr F}(\\overline z)}$ has exact counterpart $RF^+_{\\boldsymbol s}$.",
              Q("its exact counterpart is $RF_{\\boldsymbol s}^{+}$ by", "Lemma~\\ref{lem:chirp-permutation}."),
              frm=["complex-conjugate"]),
    ],
    page="source-transform",
    frm=["tensor-resampling", "source-perm-cancel", "bluestein", "parameters", "resampling-retained"],
)

S11 = infer(
    "S11",
    "The algorithm (radix digits scaled by $2^{-b-2}$, the map $\\Phi$, two computed source transforms, pointwise product, opposite transform, exact scalings by $S$ and $2^{2b+4}S$, rounding, $\\Phi^{-1}$ and carry propagation) has exact counterpart $2^{2b+4}(u*v)$, the original integer coefficient convolution.",
    Q("The two occurrences of $S$ in this algorithm undo different", "normalizations."),
    frm=["radix-reduction", "source-perm-cancel"],
)

S12 = show(
    "S12",
    "Every recovered convolution coefficient is within less than $1/2$ of the true integer, so rounding gives the exact coefficients and carry propagation gives exactly the $2n$-bit product.",
    "Track absolute errors through every stage, using that contractions do not amplify errors, that bilinear contractions add the errors of their operands, and that every computed array keeps a disk margin; then undo the scales and propagate carries.",
    "A linear contraction propagates an input error without increasing it, so the error of the whole pipeline is a sum of the stage errors, scaled only by the known exact normalizations.",
    "explicit",
    [
        infer("S12.1",
              "The returned ring convolution has error below $E_{\\rm ring}=M(3L+2)<5TL$ and keeps the disk margin $\\|\\cdot\\|<.701$.",
              Q("Thus the error of the returned normalized\nconvolution is bounded by"),
              frm=["contraction-errors"]),
        infer("S12.2",
              "The computed chirp transform has error below $8TL\\,2^{-p}$ against $QF_{\\boldsymbol t}x$.",
              Q("Equation~\\eqref{eq:permuted-chirp} identifies the exact result, so")),
        infer("S12.3",
              "The computed source transform has error below $E_s2^{-p}$ with $E_s=9\\cdot2^\\gamma TL$.",
              Q("because $2dp^2<TL$ eventually.")),
        infer("S12.4",
              "The truncated pointwise product $z$ satisfies $\\|z-U\\cdot V_1\\|<(2E_s+2)2^{-p}$.",
              Q("Thus $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$.")),
        infer("S12.5",
              "After both scalings the final error is below $448b\\,2^{-3b/4}<1/2$, so the nearest integer is the correct coefficient.",
              Q("The strict error below $1/2$ makes the nearest integer to", "the unique correct coefficient."),
              frm=["floor-ceiling-and-rounding"]),
        infer("S12.6",
              "Radix-$2^b$ carry propagation in increasing index fixes the radix digits of the full product one by one.",
              Q("The unprocessed terms are multiples of $Q_0^j$, so the identity fixes", "radix digits of the full product."),
              frm=["radix-reduction", "binary-representation-of-integers"]),
    ],
    page="precision-recovery",
    frm=["contraction-errors", "source-perm-cancel", "source-transform", "radix-reduction", "fixed-point", "triangle-inequality"],
    mot_quote=Q("A linear contraction propagates an input error without increasing it."),
    salient="Although every transform is computed only approximately with $O(\\log n)$-bit numbers, the accumulated error ends strictly below $1/2$, so the output is exact.",
)

S13 = show(
    "S13",
    "Every stage's cost divided by $Tp=\\Theta(n)$ is at most a power $p^{1-2\\kappa}$, so the machine runs in $O(n(\\lg n)^{1-\\kappa})$ time for every $n$.",
    "Tabulate the normalized cost of each stage as a power of $p$, compute the margins of the seven dominant powers below one, and absorb setup, exceptional-set sorting and small inputs.",
    "The smallest margin is $2\\kappa$, and that explicit slack covers any remaining fixed power of $\\log p$.",
    "explicit",
    [
        infer("S13.1",
              "The seven dominant powers have margins $g_1,\\ldots,g_7$ below one with $\\min_ig_i=2^{-181}=2\\kappa$.",
              Q("Thus $\\min_i g_i=2^{-181}=2\\kappa$.")),
        infer("S13.2",
              "Descriptor setup over the at most $p^A$ recursion visits costs $p^{A+C}=o(Tp)$.",
              Q("This setup then\ncosts at most $p^{A+C}=o(Tp)$.")),
        infer("S13.3",
              "Sorting the exceptional records of all packed basis changes costs $o(V)$ deterministically in the worst case.",
              Q("This is\na deterministic worst-case bound.")),
        infer("S13.4",
              "Since every power is at most $1-2\\kappa$ and fixed powers of $\\log p$ are eventually below $p^\\kappa$, the bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
              Q("The complete large-input bound is consequently"),
              frm=["big-o", "logarithms-and-exponent-rules"]),
        infer("S13.5",
              "Below a fixed cutoff schoolbook multiplication is used, and the finitely many small lengths only enlarge the constant.",
              Q("The finitely\nmany smaller lengths are included by enlarging the implicit constant.")),
    ],
    page="cost-accounting",
    frm=["parameters", "chunk-swap", "simultaneous-layer", "transform-layout", "tensor-resampling", "crt-map", "hvdh-multiplier", "big-o", "worst-case-running-time"],
    mot_quote=Q("This explicit slack will cover\nany remaining fixed power of $\\log p$."),
    salient="The saving $\\kappa=2^{-182}$ is astronomically small but strictly positive, which is all that is needed to beat $n\\log n$.",
)

root = show(
    "S0",
    "One deterministic fixed-alphabet, fixed-tape Turing machine computes the exact $2n$-bit product of two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$, disproving the $n\\log n$ conjecture in this model.",
    "Reduce the product to radix-digit convolution, move it by a Chinese-remainder map, Gaussian resampling, chirps and a phase twist to convolution over $\\mathbb C[y]/(y^r+1)$ computed by synthetic transforms; speed up the transforms' address movement and butterfly layers with two network-based tape procedures; then prove exact recovery and total the costs.",
    "Scanning $\\Theta(n)$ stored bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so beating $n\\log n$ needs savings in both data movement and arithmetic.",
    "explicit",
    [A, S4, R, S8, S9, S10, S11, S12, S13],
    page="main-theorem",
    frm=["nlogn-conjecture", "hvdh-multiplier", "radix-reduction", "multitape-tm", "big-o", "worst-case-running-time"],
    mot_quote=Q("Scanning an array of $\\Theta(n)$ stored bits at each of", "savings in both movement and arithmetic."),
    salient="The running time is below $n\\log n$ by a power of the logarithm, refuting the conjectured optimal order on multitape machines.",
    adds=[B("V", "logical volume", "The number of stored data bits of the array a tape procedure acts on.", "count"),
          B("p", "working precision", "The number $p=6\\lceil\\log_2 n\\rceil$ of fractional bits of the fixed-point coefficients.", "count"),
          B("d", "number of axes", "The number $d=\\lfloor b^\\epsilon\\rfloor$ of transform axes, which also bounds the chunks a butterfly layer acts on.", "count"),
          B("r", "record length", "The power of two $r$ such that each record is a polynomial modulo $y^r+1$ with $r$ complex coefficients.", "count")],
)

ans = {"root": root}

# ---- checks
quotes = []
def walk(n, depth=0):
    if n["intention"] == "infer":
        pos = SRC.index(n["quote"]["quote"])
        quotes.append((n["id"], pos, n.get("deferred", False)))
    else:
        q = n["motivation"].get("quote")
        if q:
            assert q["quote"] in SRC
    for c in n.get("children", []):
        walk(c, depth + 1)
walk(root)
last = -1
for id_, pos, d in quotes:
    if d:
        continue
    if pos < last:
        print('ORDER PROBLEM', id_, pos, last)
    last = pos
ids = []
def collect(n):
    ids.append(n["id"])
    for c in n.get("children", []):
        collect(c)
collect(root)
assert len(ids) == len(set(ids))
json.dump(ans, open('/home/user/openai-nlogn-wiki/runs/Q1/exegenius/tasks/0003-argument.answer.json', 'w'), indent=1, ensure_ascii=False)
print('ok', len(ids), 'nodes')
