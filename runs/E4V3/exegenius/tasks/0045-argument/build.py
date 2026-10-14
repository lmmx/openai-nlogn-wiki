import json, re, sys

SRC = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e4/V3/sources/paper.tex', encoding='utf-8').read()

def EV(q):
    return {"source": "paper", "quote": q}

def infer(id, claim, quote, frm=(), page=None, salient=None, deferred=False):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": EV(quote), "from": list(frm)}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if deferred: n["deferred"] = True
    return n

def show(id, claim, method, mot_text, mot_src, children, mot_quote=None, frm=(), page=None, adds=(), salient=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": {"text": mot_text, "source": mot_src, "quote": EV(mot_quote) if mot_quote else None},
         "children": children, "from": list(frm)}
    if page: n["page"] = page
    if adds: n["adds"] = [{"symbol": a[0], "name": a[1], "meaning": a[2], "relation": a[3]} for a in adds]
    if salient: n["salient"] = salient
    return n

# ---------------------------------------------------------------- S1: chunk interchange
cs = show("S1.2",
  r"Updating a later address field by $y\mapsto y+a(\text{controls}) \bmod q^b$, or multiplying it by a fixed rational unit, costs $O(V)$ on tape.",
  "Treat each fibre of the target field as $Q=q^b$ consecutive blocks, cut it at the offset and merge the two pieces in swapped order; handle a unit multiplier as several increasing pieces.",
  "A cyclic shift of a list is exactly 'second piece then first piece', and both pieces can be written to tapes and read back in one scan each, so the whole update is a split and a merge of linear cost.",
  "recoverable",
  [
   infer("S1.2.1", r"Cutting each fibre of $Q$ blocks at $Q-a$ and merging the two pieces in the opposite order shifts the target field by $a$ cyclically.",
         r"For an offset $a\in[Q]$, split these blocks at $Q-a$.  Append the two", ["stream-ops","modular-arithmetic"]),
   infer("S1.2.2", r"The $b^{O(1)}$ work to prepare the offset is absorbed by the $QB\ge Q$ bits of the fibre, because $b^C=O(Q)$ for each fixed $C$.",
         r"b^C=O(q^b)=O(Q)", ["stream-ops"]),
   infer("S1.2.3", r"Multiplication by a fixed unit $c$ splits each fibre into $c$ increasing pieces which are merged by a finite residue counter.",
         r"$y\mapsto cy\pmod Q$ has $c$ increasing pieces, classified by", ["modular-arithmetic"]),
   infer("S1.2.4", r"Negation reverses the order of the non-zero blocks, using stacks that also restore the bit order inside each block.",
         r"Negation leaves the block at zero fixed and reverses the order of the", ["tape-based-subroutines-and-stacks"]),
  ],
  frm=["stream-ops","modular-arithmetic","tape-based-subroutines-and-stacks"], page="controlled-shift",
  adds=[(r"Q","fibre length",r"The size $q^b$ of the range of the target field, so a fibre is $Q$ consecutive blocks.","count"),
        (r"a","offset",r"The amount by which the target field is shifted cyclically.","direct")])

so = show("S1.1",
  r"Splitting on a digit, merging, moving a digit and splitting whole rows cyclically into $W$ streams each cost $O(V)$ on a fixed number of tapes for an array of stored volume $V$.",
  "Treat each operation as a split of the array into aligned streams indexed by the specified digits, a pointwise map on the streams, and a merge.",
  "Once the specified digits are fixed, the order of all other digits is unchanged, so streams have the same shape and can be scanned in step.",
  "recoverable",
  [
   infer("S1.1.1", r"An array on a product address set $[a_1]\times\cdots\times[a_t]$ is stored in lexicographic order, so an entry's address is implicit in its position.",
         r"An array with address set $[a_1]\times\cdots\times[a_t]$ is stored in", ["lexicographic-order-and-mixed-radix-indexing"]),
   infer("S1.1.2", r"A fixed permutation of two digit values, or the move of one digit, splits the array into $q^2$ or $q$ streams with identical remaining address order and reads them back in output order.",
         r"For the first operation split into $q^2$ streams according to the two", ["lexicographic-order-and-mixed-radix-indexing"]),
   infer("S1.1.3", r"Writing a row number as $r=Wg+w$ and sending the whole row to stream $w$ gives $W$ streams of the same shape, each of volume $V/W$.",
         r"$0\le w<W$, and send the whole row to stream $w$.  If $W$ divides $R$,", ["lexicographic-order-and-mixed-radix-indexing"]),
   infer("S1.1.4", r"Counters, shape preparation and tape rewinds add only $O(V)$ in total.",
         r"Here are the counter details used in these scans and later ones.  A", ["tape-based-subroutines-and-stacks","multitape-tm"]),
  ],
  frm=["lexicographic-order-and-mixed-radix-indexing","multitape-tm","sorting-merging-and-radix-sort","tape-based-subroutines-and-stacks"], page="stream-ops",
  adds=[(r"V","stored volume","The number of data bits stored in the array.","count"),
        (r"W","number of streams","The number of role streams into which whole rows are split cyclically.","count")])

# ---- K : rank saving
ka_gadget = show("S1.3.1.3",
  r"Gather and scatter over three-element subsets create central coefficients $|S\cap T|\bmod 2$ (bit case) or $(|S\cap T|-1)/2$ (complex case), and side wires cancel the unwanted intersection sizes, so $\mathcal J\mathcal V+\mathcal R\mathcal G$ acts as the identity $y\gets y+x$.",
  "Pick the coefficients by the size of the intersection of the two triples: the central path contributes a coefficient depending only on $|S\cap T|$, and a side wire is added for each neighbouring pair to correct exactly the intersection sizes where this disagrees with the identity.",
  "Triples of a ground set can intersect in only 0,1,2 or 3 elements, so a coefficient that depends only on the intersection size leaves just a few cases to cancel, and the cancelling side wires are needed only between neighbouring triples.",
  "recoverable",
  [
   infer("S1.3.1.3.1", r"In the bit construction the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod 2$; the side injection cancels exactly the intersection-one cases, since intersections zero and two already give zero and the self coefficient is one.",
         r"In the bit case, the central coefficient from $x_T$ to $y_S$ is", ["sets-subsets-and-binomial-coefficients","xor-and-mod-2-arithmetic"]),
   infer("S1.3.1.3.2", r"In the complex construction the central coefficient is $(|S\cap T|-1)/2$; the side cancels intersections zero and two, intersection one contributes zero, and the self coefficient is one.",
         r"In the complex case, the central coefficient is $(|S\cap T|-1)/2$.", ["sets-subsets-and-binomial-coefficients"]),
   infer("S1.3.1.3.3", r"Thus both net maps are $y\gets y+x$.",
         r"Thus both net maps are $y\gets y+x$.", ["sets-subsets-and-binomial-coefficients"]),
  ],
  frm=["linear-network","linear-algebra","sets-subsets-and-binomial-coefficients"], page="subset-gadget",
  salient="The unwanted coefficients are cancelled for every pair of triples simultaneously, so one fixed gadget realizes $y\\gets y+x$ whatever the arbitrary values on the scratch wires are.",
  adds=[(r"S","target triple","The three-element subset indexing the updated value $y_S$.","direct"),
        (r"T","control triple","The three-element subset indexing the control value $x_T$.","direct")])

ka = show("S1.3.1",
  r"An eight-row schedule of copy, gather, scatter and side-injection gates changes each target $y_S$ by a fixed linear map of the sources whatever the initial scratch values, and three stages of it exchange the two banks as $(X_a,Y_a)\mapsto(-Y_a,X_a)$.",
  "Subtract the effect of the old scratch contents first, then add the source contribution, then undo the scratch additions; so the arbitrary initial scratch values cancel and every scratch wire is restored.",
  "A linear update that is applied, and then reversed on the scratch wires only, leaves a net effect that does not depend on what the scratch wires held.",
  "explicit",
  [
   infer("S1.3.1.1", r"Rows 0 and 1 remove the effect of the old side and central values, rows 2 to 5 introduce the source values and add their effect to the target, and rows 6 and 7 restore the scratch values.",
         r"the next four introduce the source values and add their effect to the", ["linear-algebra"]),
   infer("S1.3.1.2", r"With initial side and central vectors $a,c$ the net target change is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of $a,c$.",
         r"$(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of", ["linear-algebra"]),
   ka_gadget,
   infer("S1.3.1.4", r"A forward invocation from $X$ to $Y$, the inverse schedule from $Y$ to $X$, and a forward invocation again send $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$, restoring every scratch wire.",
         r"Starting from $(x,y)$, the three stages give", ["linear-algebra"]),
   infer("S1.3.1.5", r"The numbers of wires $W_{\rm b}$ and $W_{\rm c}$ in the two networks are fixed constants, independent of the input length.",
         r"All these numbers are fixed, independently of any eventual input length.", ["sets-subsets-and-binomial-coefficients"]),
  ],
  mot_quote=r"the following schedule remove the effect of the old scratch values;",
  frm=["linear-algebra"], page="linear-network",
  adds=[(r"\mathcal V","copy map",r"The gate adding each control value $x_T$ to its side wire $A_{ST}$.","direct"),
        (r"\mathcal J","side injection",r"The gate adding the side wires to the target value $y_S$.","direct"),
        (r"\mathcal G","gather",r"The gate adding the control values of triples through an index to the central wires.","direct"),
        (r"\mathcal R","scatter",r"The gate adding the central wires to the target value $y_S$.","direct")],
  salient="Every wire has a fixed place in the network, its role, so the same schedule is applied to scratch wires as to data wires and nothing needs to be known about the scratch contents.")

kb = show("S1.3.2",
  r"If all wires at a gate are stored in the same invertible frame $D_v$ and gates are pointwise linear, the whole network implements $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$, and an edge only needs the change of frame $D_vD_u^{-1}$.",
  "Define the logical array as the inverse frame applied to the stored array and check the invariant 'stored array equals the frame applied to the logical array' at sources, along edges, and across gates.",
  "A gate that is linear and pointwise commutes with any operator that acts within one wire's array, so a common frame passes through it unchanged.",
  "explicit",
  [
   infer("S1.3.2.1", r"The supplied physical input $f$ needs no preliminary change of frame: its logical interpretation is defined as $g=D_{\rm in}^{-1}f$.",
         r"For a supplied physical input $f$, define its logical interpretation to be", ["matrices-and-matrix-vector-products"]),
   infer("S1.3.2.2", r"At a gate with logical inputs $\varphi_j$, linearity gives $\sum_j c_jD_v\varphi_j=D_v(\sum_jc_j\varphi_j)$, so the common frame commutes with the pointwise gate and the invariant continues to the sinks.",
         r"$\sum_j c_jD_v\varphi_j=D_v(\sum_j c_j\varphi_j)$ for each output combination, with", ["matrices-and-matrix-vector-products"]),
   infer("S1.3.2.3", r"The implemented operator is therefore $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$: all intermediate frames cancel.",
         r"D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}.", ["matrices-and-matrix-vector-products"]),
   infer("S1.3.2.4", r"A route from input role $w$ to output role $\rho(w)$ with sign $\varepsilon_w$ therefore applies $\varepsilon_wD_{{\rm sink}(\rho(w))}D_{{\rm source}(w)}^{-1}$, including on auxiliary roles.",
         r"In particular, if the scalar network is a signed role permutation that", ["permutations"]),
  ],
  mot_quote=r"arrays, a common representation on all wires at a gate lets that gate act",
  frm=["linear-network","matrices-and-matrix-vector-products"], page="frames",
  adds=[(r"D_v","frame",r"An invertible linear operator on the array of one wire at vertex $v$; the stored array is $D_v$ applied to the logical array.","direct"),
        (r"\Omega","address set",r"The finite set of addresses shared by all wire arrays.","direct"),
        (r"\mathsf S_\Omega","array network",r"The scalar network applied pointwise at every address of $\Omega$.","direct")],
  salient="The intermediate frames cancel along every route, so the operator on every role, scratch roles included, depends only on the two endpoint frames, while each edge may use whichever frame makes its change cheap.")

# K.c  label dimension budget
kc = show("S1.3.3",
  r"Labels can be assigned so that the sum of absolute dimension changes over all edges is $Wm-2N+2L$, where the decreasing edges lose total dimension $L=Ich$ and $L<N/2$.",
  "Assign terminal labels, then follow the nested labels along each wire stage by stage and gate by gate; dimension changes telescope at gates, so only the terminals and the few decreasing edges matter.",
  "At a gate every touched wire enters and leaves with the same label, so signed changes cancel there, leaving the terminals' total and a correction for edges that lose dimension.",
  "recoverable",
  [
   infer("S1.3.3.1", r"The terminal labels have source dimensions summing to $N$ and sink dimensions summing to $Wm-N$.",
         r"The source dimensions sum to $N$ and the sink dimensions to $Wm-N$.", ["linear-algebra"]),
   infer("S1.3.3.2", r"At stage $j$ the outgoing labels $A'\otimes\langle t_{a_{j+1}}\rangle\otimes Q'$ on $X$ and $B'\otimes\langle t_{a_{j+1}}\rangle\otimes Q'$ on $Y$ equal the next stage's incoming labels, starting from $U_a$ on $X_a$ and $0$ on $Y_a$ and ending at $\mathcal F$ and $U_a^\perp$.",
         r"These transitions expose one tensor factor at each stage. To see that", ["linear-algebra"]),
   infer("S1.3.3.3", r"On a side wire joining neighbouring triples, $P\otimes\langle t_X\rangle\subset P\otimes t_Y^\perp$, because neighbouring triple lines are orthogonal.",
         r"The first inclusion is possible because $t_X\perp t_Y$.", ["linear-algebra"]),
   infer("S1.3.3.4", r"Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each of dimension loss $h$.",
         r"Every edge joins comparable nondegenerate labels.  The only decreasing", ["linear-algebra"]),
   infer("S1.3.3.5", r"The side edge from time 2 to time 5 is nested only because neighbouring triples are orthogonal.",
         r"The side edge $2\to5$ uses the neighbor relation", ["linear-algebra"]),
   infer("S1.3.3.6", r"The signed dimension changes telescope at each gate, so the signed increase over the network is $Wm-2N$.",
         r"The signed sum of dimension changes telescopes at every gate: each", ["linear-algebra"]),
   infer("S1.3.3.7", r"There are $Ic$ decreasing edges of loss $h$, so $L=Ich$ and the sum of absolute changes is $Wm-2N+2L$.",
         r"There are $Ic$ decreasing edges, each of loss $h$; replacing signed", ["linear-algebra"]),
   infer("S1.3.3.8", r"Over $\mathbb F_2$ every nonzero orthogonal residual is nonalternating and so has an orthonormal basis, so it is a sum of norm-one directions.",
         r"Now work over $\mathbb F_2$.  A nondegenerate symmetric bilinear space", ["linear-algebra","xor-and-mod-2-arithmetic"]),
   infer("S1.3.3.9", r"The loss ratios are $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$.",
         r"The loss ratios have the exact values", ["linear-algebra"]),
   infer("S1.3.3.10", r"Both loss ratios are below $1/2$, so $L<N/2$ in both networks.",
         r"In particular, both are smaller than $1/2$.", ["linear-algebra"]),
  ],
  frm=["linear-network","frames","subset-gadget","linear-algebra"],
  adds=[(r"N","number of data banks",r"The number $v^3$ of index tuples $a$, equal to the total source dimension.","count"),
        (r"L","total dimension lost",r"The total dimension lost on the decreasing edges.","count"),
        (r"h","ground-set size",r"The size $100$ of the ground set whose triples index the banks, also the loss on each decreasing edge.","count")])

kd = show("S1.3.4",
  r"The bit network sends its input to the role permutation $\rho$, its rational vertex matrices satisfy $M_{{\rm sink}(\rho(w))}-M_{{\rm source}(w)}=I_m$ for every input role $w$, and its edge-difference ranks sum to $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.",
  "Attach to each vertex the orthogonal projection onto its label (and minus the projection at the sources $X_a$); the rank of a difference of nested projections is the dimension change, so the dimension budget becomes a rank budget.",
  "The rank of $P_V-P_U$ for nested nondegenerate labels equals $\\dim V-\\dim U$, which converts the label counting of the previous step directly into the number of smaller calls.",
  "recoverable",
  [
   infer("S1.3.4.1", r"Each vertex $v$ gets a rational matrix $M_v$: $P_U$ at a gate or sink with label $U$, $-P_{U_a}$ at source $X_a$, and zero at every other source.",
         r"each gate or sink with label $U$.  Assign the source matrix $-P_{U_a}$", ["matrices-and-matrix-vector-products"]),
   infer("S1.3.4.2", r"The frame $\Phi_M$ moves the array entry at $(H,D)$ to $(H+MD,D)$; it is an invertible permutation with $\Phi_{M'}\Phi_M=\Phi_{M'+M}$.",
         r"of $m$ fields.  For a matrix $M$, the frame $\Phi_M$ moves the array entry", ["matrices-and-matrix-vector-products","modular-arithmetic"]),
   infer("S1.3.4.3", r"For nested nondegenerate labels $U\subset V$, $P_V-P_U$ has rank $\dim V-\dim U$, so an edge's rational rank equals its dimension change.",
         r"$P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its", ["linear-algebra"]),
   infer("S1.3.4.4", r"The only exceptions are the $N$ negative source projections.",
         r"The only exceptions are the $N$ negative source projections.", ["linear-algebra"]),
   infer("S1.3.4.5", r"The first edge matrix at a source $X_a$ is $2P_{U_a}$, of rank one where the dimension change was zero, adding $N$ to the rank sum.",
         r"Its first edge matrix is therefore $2P_{U_a}$, of rational rank one,", ["linear-algebra"]),
   infer("S1.3.4.6", r"Hence $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$, with deficit $N-2L_{\rm b}>0$ from $W_{\rm b}m$.",
         r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.", ["linear-algebra"]),
   infer("S1.3.4.7", r"For input $X_a$ the endpoint difference is $P_{U_a^\perp}+P_{U_a}=I_m$, and every other role has zero source matrix and identity sink matrix, so every role undergoes the same shear $H\gets H+D$.",
         r"For an input $X_a$ the endpoint difference is", ["matrices-and-matrix-vector-products"]),
  ],
  frm=["frames","subset-gadget","rank-saving","matrices-and-matrix-vector-products"], page="bit-network-shear",
  adds=[(r"M_v","vertex matrix",r"The rational $m\times m$ matrix assigned to vertex $v$: the projection onto its label.","direct"),
        (r"P_U","projection",r"The projection onto the label $U$ along its orthogonal complement.","direct"),
        (r"\Phi_M","address shear",r"The permutation of array entries that moves the entry at $(H,D)$ to $(H+MD,D)$.","direct")],
  salient="Data wires and scratch wires alike end with the same endpoint difference $I_m$, so the single shear $H\\gets H+D$ is applied to every role, including roles holding arbitrary values.")

ke = show("S1.3.5",
  r"In the complex network with binary labels and phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{q_U(x)})H^{\otimes m}$, each edge difference is a product of two-point kernels $aI+bX_v$, there are $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$ of them in all, and telescoping gives $C^{\otimes m}$ on every role.",
  "Replace the rational projection of a label by the Hamming weight of its binary projection taken modulo 4 as a phase; orthogonal directions add weights modulo 4, so each orthonormal basis vector of an edge residual contributes one two-point kernel.",
  "Over $\\mathbb F_2$ orthogonal vectors have even overlap, so weight is additive modulo four, which is exactly what lets a phase frame difference factor into one simple factor per residual direction.",
  "recoverable",
  [
   infer("S1.3.5.1", r"The phase frame of a label $U$ is $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$ with $q_U(x)=\operatorname{wt}(P_Ux)\bmod 4$.",
         r"\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}.", ["hamming-weight","complex-numbers"]),
   infer("S1.3.5.2", r"For orthogonal binary vectors $z,w$ the Hamming weight is additive modulo four.",
         r"If $z\cdot w=0$, the intersection cardinality is even, so weight is", ["hamming-weight","xor-and-mod-2-arithmetic"]),
   infer("S1.3.5.3", r"Each norm-one residual vector $v$ has odd weight, so its phase coefficient is $\pm1$ modulo four.",
         r"Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd.  Its", ["hamming-weight"]),
   infer("S1.3.5.4", r"The phase $i^{\varepsilon[v\cdot x]}$ becomes the kernel $aI+bX_v$ or its inverse, one per residual basis vector.",
         r"becomes $aI+bX_v$ or its inverse.  The nonzero residuals have such", ["euler-s-formula-and-complex-conjugation"]),
   infer("S1.3.5.5", r"The kernel count is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$, with deficit $2N-2L_{\rm c}>0$.",
         r"The deficit is $2N-2L_{\rm c}>0$.", ["linear-algebra"]),
   infer("S1.3.5.6", r"By the common-frame identity an input role reaches its output role with operator $\mathcal C_{U_{\rm sink}}\mathcal C_{U_{\rm source}}^{-1}$ and the route's sign.",
         r"Applying \eqref{eq:common-frame-identity} with $D_v=\mathcal C_{U_v}$,", ["frames"]),
   infer("S1.3.5.7", r"The zero label has frame $I$ and the full label has frame $C^{\otimes m}$, which settles every pair of roles except $X_a\to Y_a$.",
         r"The zero label has frame $I$, while the full label has frame", ["hamming-weight"]),
   infer("S1.3.5.8", r"For the pair $X_a\to Y_a$ the operator is $C^{-1}$ on the 27 coordinates in the support of $u_a$ and $C$ elsewhere.",
         r"For the remaining pair, write $u=u_a$.  Its binary norm is one and", ["hamming-weight"]),
   infer("S1.3.5.9", r"Conjugating with $Z$ and a fourth-root phase turns each inverse factor into $C$ (since $C=iZC^{-1}Z$), so every role, including scratch roles, receives $C^{\otimes mk}$.",
         r"the identity $C=iZC^{-1}Z$ turns each of them into $C$.", ["matrices-and-matrix-vector-products"]),
  ],
  frm=["frames","subset-gadget","rank-saving","hamming-weight","xor-and-mod-2-arithmetic"], page="complex-phase-network",
  adds=[(r"C","two-point kernel",r"The matrix $aI+bX=H\,\mathrm{diag}(1,i)\,H$ with $a=(1+i)/2$, $b=(1-i)/2$, acting on one bit.","direct"),
        (r"\mathcal C_U","phase frame",r"The frame of label $U$ built from the Hamming-weight phase of the projection onto $U$.","direct")],
  salient="Every role, scratch roles included, ends with the same tensor power $C^{\\otimes m}$, exactly parallel to the uniform shear of the bit network.")

kf = infer("S1.3.6", r"With $\tau=\sigma=1-2^{-50}$ both exact relative rank deficits exceed $20\cdot2^{-50}$, so $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$.",
           r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$.", ["logarithms-floors-and-ceilings"])

K = show("S1.3",
  r"Two fixed linear networks on $W$ wires, each exchanging two banks of values and restoring every scratch wire, can be labelled by nested nondegenerate subspaces of an $m$-dimensional space so that the sum $s$ of the ranks of the edge differences stays strictly below $Wm$.",
  "Give each vertex of the network a nondegenerate subspace label so that the labels along every edge are nested; then an edge costs exactly its dimension change in smaller calls, and counting dimension changes over the whole network gives $s$.",
  "Nested labels make each edge's change of representation a number of smaller operations equal to the dimension it adds or removes, and almost all edges add dimension, so the total can be counted from the terminals and the few edges that lose dimension.",
  "explicit",
  [ka, kb, kc, kd, ke, kf],
  mot_quote=r"count the smaller operations needed on an edge, with an additional",
  frm=["linear-algebra","sets-subsets-and-binomial-coefficients"], page="rank-saving",
  adds=[(r"W","number of wires",r"The number of scalar wires of the network, scratch wires included.","count"),
        (r"m","label dimension",r"The dimension of the ambient space of labels, equal to the number of address fields shifted together.","count"),
        (r"s","total edge rank",r"The sum over all edges of the rank of the edge difference, i.e. the number of smaller calls.","count")],
  salient="The saving is razor thin: the relative deficit of $s$ below $Wm$ is only about $10^{-14}$ in both networks, yet this strict gap, uniform over all wires, is the only source of the power saving $\\tau=1-2^{-50}<1$.")

# ---- S1.4 matrix shear
tf = show("S1.4.1",
  r"Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation matrix with exactly $a$ ones.",
  "Eliminate pivot by pivot: choose the topmost nonzero row and its rightmost nonzero entry, clear its column to the left and its row below by lower-triangular elementary matrices, then repeat on the remaining active indices.",
  "Clearing only to the left of the pivot (by column operations) and below it (by row operations) uses only lower-triangular elementary matrices, so the order of coordinates on tape is respected.",
  "recoverable",
  [
   infer("S1.4.1.1", r"If $A=0$ take $E_1=E_2=I$, $\Pi=0$; otherwise choose the topmost nonzero row and its rightmost nonzero entry as pivot, clear its column to the left, clear below it, and scale it to one.",
         r"If $A=0$, take $E_1=E_2=I$ and $\Pi=0$.  Otherwise choose the topmost", ["matrices-and-matrix-vector-products","linear-algebra"]),
   infer("S1.4.1.2", r"Deleting the pivot row and column from the active indices and repeating leaves earlier pivots untouched and ends with a partial permutation matrix with exactly $a$ ones.",
         r"Delete the pivot row and column from the active index sets, retaining", ["linear-algebra"]),
  ],
  frm=["linear-algebra","matrices-and-matrix-vector-products"], page="triangular-factorization",
  adds=[(r"E_1","left triangular factor","An invertible lower triangular rational matrix on the left of the partial permutation.","direct"),
        (r"E_2","right triangular factor","An invertible lower triangular rational matrix on the right of the partial permutation.","direct"),
        (r"\Pi","partial permutation","A matrix with exactly $a$ ones, at most one in each row and column.","direct")])

ms = show("S1.4",
  r"For a rational $m\times m$ matrix $A$ of rank $a$, the shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work.",
  "Factor $A=E_1\\Pi E_2$ with lower triangular $E_i$; triangular changes of coordinates are linear-time controlled shifts, so only the $a$ pivots of $\\Pi$ need an actual field interchange.",
  "A later field can be updated from earlier fields in linear time, and lower triangular changes of coordinates can be performed entirely in this direction.",
  "explicit",
  [
   tf,
   infer("S1.4.2", r"A lower triangular transformation of $H$ or of $D$ costs $O(V)$: update coordinates in descending physical order, multiplying by a unit and adding a fixed combination of earlier coordinates.",
         r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:", ["controlled-shift"]),
   infer("S1.4.3", r"For $A=E_1\Pi E_2$, transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$.",
         r"For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,", ["controlled-shift"]),
   infer("S1.4.4", r"A pivot $H_i\gets H_i+D_j$ is done by $D_j\gets D_j+H_i$, an interchange $(H_i,D_j)\gets(D_j,H_i)$, and $D_j\gets H_i-D_j$, where the first and last updates target a later field controlled by an earlier one.",
         r"The first and last updates target a later field controlled by an earlier", ["controlled-shift"]),
   infer("S1.4.5", r"Each of the $a$ ones of $\Pi$ costs exactly one interchange, so the shear uses exactly $a$ interchanges.",
         r"It uses just one interchange.  There are $a$ ones, which proves the", ["controlled-shift"]),
  ],
  mot_quote=r"earlier fields in linear time.  Lower triangular changes of coordinates",
  frm=["controlled-shift","linear-algebra","modular-arithmetic"], page="matrix-shear",
  adds=[(r"a","rank",r"The rational rank of the matrix $A$, which counts the field interchanges needed.","count"),
        (r"H","high address vector",r"The ordered group of $m$ address fields $H_1,\ldots,H_m$ that precede the fields of $D$.","direct"),
        (r"D","low address vector",r"The ordered group of $m$ address fields $D_1,\ldots,D_m$, each ranging over $[q^b]$.","direct")])

# ---- S1.5 power-width interchange
pw = show("S1.5",
  r"For chunks of $e=m^k$ digits, running the bit network on $W$ row-split role streams, with each edge done by smaller interchanges, gives $F_k\le(s/W)F_{k-1}+O(1)$ and hence an interchange cost of $O(Ve^\tau)$.",
  "Induction on $k$: split rows into $W$ role streams of volume $V/W$, apply the finite bit network so that each role undergoes the shear $H\\gets H+D$, implement each of its $s$ edge changes by smaller interchanges, obtain the full interchange from three shears, and solve the recurrence.",
  "Each call produces $s$ children but on streams of only $1/W$ of the volume, so the cost per unit volume is multiplied by $s/W$ per level while the width is multiplied by $m$.",
  "recoverable",
  [
   infer("S1.5.1", r"Splitting whole rows cyclically into $W$ role streams gives streams of the same shape, each of volume $V/W$ with row count divisible by $W^{k-1}$.",
         r"Split whole rows cyclically into $W$ role streams within each prefix", ["stream-ops"]),
   infer("S1.5.2", r"On every circuit edge apply the shear $\Phi_{A_e}$ to that role stream, implemented by recursively interchanging each pivot pair of $b$-digit fields; gates act pointwise at matching addresses.",
         r"$\Phi_{M'}\Phi_M=\Phi_{M'+M}$.  On every circuit edge apply", ["matrix-shear","bit-network-shear"]),
   infer("S1.5.3", r"By the endpoint contract the physical output on role $\rho(w)$ is $\Phi_{M_{\rm out}}\Phi_{-M_{\rm in}}f_w=\Phi_{I_m}f_w$.",
         r"=\Phi_{I_m}f_w,", ["frames","bit-network-shear"]),
   infer("S1.5.4", r"Merging rows back undoes $\rho$ and the result is $H\gets H+D$ on every original row, including rows assigned to scratch roles with arbitrary values.",
         r"is $H\leftarrow H+D$ on every original row, including rows assigned", ["frames","bit-network-shear"]),
   infer("S1.5.5", r"Three componentwise updates $D\gets D-H$, $H\gets H+D$, $D\gets H-D$ interchange $H$ and $D$; only the middle shear uses the circuit.",
         r"To interchange the two full chunks, perform", ["matrix-shear"]),
   infer("S1.5.6", r"The number of recursive calls is the sum of the edge ranks, exactly $s$, each on one role stream of volume $V/W$.",
         r"The number of recursive calls is the sum of the edge ranks, exactly $s$.", ["rank-saving"]),
   infer("S1.5.7", r"The cost per unit volume satisfies $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.",
         r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1).", ["divide-and-conquer-and-recurrences"]),
   infer("S1.5.8", r"Since $s/W<m^\tau$, the geometric sum $\sum_{j\le k}(s/W)^j$ is $O(m^{k\tau})$, so $F_k=O(e^\tau)$.",
         r"For $a=s/W<m^\tau$ the geometric sum", ["divide-and-conquer-and-recurrences","rank-saving"]),
   infer("S1.5.9", r"On fixed tapes, parking the inactive role streams on a stack and reusing the same tapes at every depth adds only $O(V)$ at each node.",
         r"Before a recursive call, append the $W-1$ inactive role streams to the", ["tape-based-subroutines-and-stacks"]),
   infer("S1.5.10", r"Descriptor processing also fits the $O(V)$ term, even for one-bit payloads, because $\log V_0=O(\log(2V_j))$ at every depth $j$.",
         r"j\log W\le(\log_m e_0)\log W=O(e_0)=O(\log V_j).", ["logarithms-floors-and-ceilings"]),
  ],
  frm=["stream-ops","controlled-shift","frames","rank-saving","bit-network-shear","matrix-shear","divide-and-conquer-and-recurrences"], page="power-width-interchange",
  adds=[(r"e","chunk width",r"The number $m^k$ of radix-$q$ digits in each of the two chunks to be interchanged.","count"),
        (r"k","recursion depth",r"The exponent with $e=m^k$, i.e. the depth of the recursion.","count"),
        (r"F_k","cost per volume",r"A uniform upper bound on running time divided by logical volume for chunks of $m^k$ digits.","direct")],
  salient="Each level multiplies the work per unit volume by the ratio $s/W$, which is almost the width growth factor $m$, yet the total grows like $e^\\tau$ with $\\tau<1$ only because $s/W<m^\\tau$ strictly.")

aw = show("S1.6",
  r"For arbitrary prefix, gap and suffix lengths, the interchange $(p,h,g,d,z)\mapsto(p,d,g,h,z)$ of two $u$-bit chunks costs $O(Vu^\tau)$.",
  "Supply the rows that the power-width procedure needs from a few of the chunks' own top digits, split the remaining width in base $m$ into power-width pieces, and pad binary widths up to powers of the prime $q$.",
  "The power-width procedure needs a row field divisible by $W^k$ and a width $m^k$; the top $\\rho=O(\\log e)$ digits give enough rows cheaply, and a base-$m$ expansion turns any width into a geometric sum of such pieces.",
  "explicit",
  [
   infer("S1.6.1", r"Exchange the top $\rho=O(\log e)$ digits of each chunk one pair at a time, and join them to make a row field of range $R=q^{2\rho}\ge W^k$ in front of the remaining chunks.",
         r"Write each chunk as its top $\rho$ digits followed by its remaining", ["stream-ops"]),
   infer("S1.6.2", r"Append zero rows within each prefix until the row count is a multiple of $W^k$, which less than doubles the volume.",
         r"Append zero rows, separately within", ["stream-ops"]),
   infer("S1.6.3", r"Writing the remaining width as $\sum_ja_jm^j$ with $a_j<m$ splits each chunk into $a_j$ pieces of width $m^j$, each handled by the power-width interchange.",
         r"Write the remaining width in base $m$:", ["power-width-interchange"]),
   infer("S1.6.4", r"The sum of costs is $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$.",
         r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau).", ["divide-and-conquer-and-recurrences"]),
   infer("S1.6.6", r"For binary chunks of $u$ bits, pad each range from $[2^u]$ to $[q^e]$ with $e=O(u)$ (a fixed-factor volume increase), interchange, and scan the padding away, giving $O(Vu^\tau)$.",
         r"Finally, for binary chunks let $e$ be the least integer with", ["stream-ops","binary-representation-of-integers"]),
   infer("S1.6.5", r"Chunks of widths differing by one bit reduce to the equal-width case by one extra single-bit move.",
         r"For widths differing by one bit, choose the leading bit of the longer", ["stream-ops"]),
  ],
  mot_quote=r"Rows for a general array can be supplied by a few of its own high digits.",
  frm=["power-width-interchange","stream-ops"])

S1 = show("S1",
  r"Interchanging two disjoint $u$-bit address fields of an array in which all address combinations occur costs $O(Vu^{\tau})$ for a fixed $\tau<1$.",
  "Write the interchange as three shears; obtain the middle shear $H\\gets H+D$ from a fixed linear bit network run on $W$ row-split role streams, so that each of its $s<Wm$ edge changes is a smaller interchange, giving a recurrence with ratio $s/W<m^\\tau$.",
  "Doing the interchange by sorting would cost a logarithmic factor; the network lets the same operation recurse into pieces whose total size is only slightly less than a naive $m$-fold branching, which is already enough for a power saving.",
  "explicit",
  [so, cs, K, ms, pw, aw],
  mot_quote=r"Because the sum of these ranks is less than the number of wires times",
  frm=["modular-arithmetic","xor-and-mod-2-arithmetic","lexicographic-order-and-mixed-radix-indexing"], page="chunk-interchange",
  adds=[(r"u","chunk width",r"The number of bits in each of the two address fields to be interchanged.","count"),
        (r"\tau","interchange exponent",r"A fixed exponent $\tau=1-2^{-50}<1$ in the interchange cost $O(Vu^\tau)$.","direct")],
  salient="Although the final effect is an exact permutation of the data, the intermediate steps compute XOR-style combinations of the data and still return it exactly, whatever the arbitrary values of the scratch rows were.")

# ---------------------------------------------------------------- Y : simultaneous layer
Y1 = show("S2.1",
  r"$H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, and $C^{\otimes e}$ on $e=mf$ selected axes reduces to $s_{\rm c}$ calls of $C^{\otimes f}$ on $f=e/m$ axes plus binary changes of basis of the selected bits.",
  "Write the phase-frame difference on each edge as a product of two-point kernels in a coordinate basis completed from the residual basis and conjugated by an address permutation $\\mathcal P_M$; realize $\\mathcal P_M$ by elementary row additions of selected bits.",
  "A kernel $C_v$ in a general direction $v$ is conjugate to a kernel on a standard axis, so the recursive calls can all be made on whole slots, with only fixed binary basis changes between them.",
  "recoverable",
  [
   infer("S2.1.1", r"$H_0=b\mathsf SC\mathsf S$, $C^2=X$, $C^4=I$ and $C^{-1}=bI+aX=-iZCZ$, so the butterfly is the kernel $C$ conjugated by diagonal phases.",
         r"H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad", ["complex-phase-network","butterfly-fft"]),
   infer("S2.1.2", r"An edge from label $U_-$ to $U_+$ has frame change $\prod_{j\le\rho_{\rm edge}}(aI+bX_{v_j})^{\epsilon_j}$ over an orthonormal basis of its residual.",
         r"Proposition~\ref{prop:complex-motif-interface} gives the frame change", ["complex-phase-network"]),
   infer("S2.1.3", r"Completing the residual basis to $M\in\mathrm{GL}(m,\mathbb F_2)$ puts the directions on coordinate axes: the frame change equals $\mathcal P_M\bigl(\prod_jC_{e_j}^{\epsilon_j}\bigr)\mathcal P_M^{-1}$.",
         r"Extend $v_1,\ldots,v_{\rho_{\rm edge}}$ to a basis of $\mathbb F_2^m$ and take these vectors as", ["linear-algebra","xor-and-mod-2-arithmetic"]),
   infer("S2.1.4", r"Dividing $e=mf$ chunks into $m$ slots of $f$ chunks, each directional kernel becomes one child operation $(C^{\epsilon_h})^{\otimes f}$ on the $f$ selected bits of slot $h$.",
         r"$f$ bits $x_{h,0},\ldots,x_{h,f-1}$.  This is one child operation", ["complex-phase-network"]),
   infer("S2.1.5", r"An inverse kernel needs no extra child: $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$.",
         r"=(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}.", ["complex-phase-network"]),
   infer("S2.1.6", r"The basis change $\mathcal P_M$ is a product of a fixed number of elementary row additions, each XOR-ing corresponding selected bits in two whole slots.",
         r"Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$", ["xor-and-mod-2-arithmetic"]),
   infer("S2.1.7", r"Summing residual dimensions, one invocation of the network has exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
         r"$e=mf$ selected axes.  Summing its residual dimensions gives exactly", ["rank-saving"]),
   infer("S2.1.8", r"On all selected coordinates $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, with $b^D$ and the phases exact Gaussian dyadic operations.",
         r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D.", ["butterfly-fft","dyadic-and-rational-numbers"]),
  ],
  frm=["complex-phase-network","rank-saving","butterfly-fft","linear-algebra","xor-and-mod-2-arithmetic"], page="phase-frame-reduction",
  adds=[(r"e","group size",r"The number $mf$ of consecutive selected axis chunks in a group handled by one call of the network.","count"),
        (r"f","slot size",r"The number $e/m$ of axis chunks in each of the $m$ slots of a group.","count"),
        (r"b","kernel coefficient",r"The complex number $(1-i)/2$ appearing in $H_0=b\mathsf SC\mathsf S$.","direct")])

Y2 = show("S2.2",
  r"For chunks $x,y,z$ of width $L=fK$, the XOR $y_{j_i}\gets y_{j_i}\oplus x_{j_i}$ at the selected bit positions $j_i=\rho+iK$, with $z$ restored, costs $O(V(L^\tau+1))$ up to a deterministic repair of an exponentially small set of addresses.",
  "Eight conditional $\\pm1$ additions to packed integer segments flip the parity of the target while restoring the auxiliary chunk; these are exact except where a segment is near the end of its range, and those addresses are repaired by sorting.",
  "A parity flip of a number is an addition of $\\pm1$ depending on its own parity, and doing it for all $f$ segments at once is one cyclic shift of the whole chunk, so no per-bit pass is needed.",
  "explicit",
  [
   infer("S2.2.1", r"For a Boolean control $c$ the eight operations induce the cycle $(00\,01\,10)$ and then $(01\,10\,11)$ on parity pairs of $(u,w)$ and do nothing if $c=0$.",
         r"If $c=0$, these operations do nothing. If $c=1$, the first four operations", ["xor-and-mod-2-arithmetic","permutations"]),
   infer("S2.2.2", r"The net effect is $u'=u+c(1-2(u\bmod2))$ and $w'=w$: the parity of $u$ flips exactly when $c=1$, and the auxiliary integer $w$ is restored.",
         r"is flipped precisely when $c=1$, both quotients under division by two are", ["xor-and-mod-2-arithmetic"]),
   infer("S2.2.3", r"Packed segments at positions $j_i=\rho+iK$ with guard values at least 10 away from the ends of their ranges neither carry nor borrow, so the packed additions agree with independent ones except on a fraction $\delta_{\rm bad}\le80(f-1)2^{-K}$ of addresses.",
         r"There are exactly twenty excluded values for each guard in", ["modular-arithmetic"]),
   infer("S2.2.4", r"Each of the eight lines is a cyclic shift of one chunk by an offset computed from the other two; after moving the target to the rightmost chunk position by chunk swaps costing $O(VL^\tau)$ it is a controlled shift.",
         r"Pass only $L$ and these three positive canonical lengths to", ["chunk-interchange"]),
   infer("S2.2.5", r"By the controlled-shift lemma each rotation then costs $O(V)$, since the offset work is absorbed by the $2^L$ nonempty target blocks of each fibre.",
         r"therefore gives an $O(V)$ rotation: its offset work is absorbed by the", ["controlled-shift"]),
   infer("S2.2.6", r"The exceptional addresses are extracted, labelled with their destination ranks, sorted by stable radix sort, and reinserted by one forward scan of the stream.",
         r"while stable binary radix sorting scans only the extracted records and", ["sorting-merging-and-radix-sort"]),
   infer("S2.2.7", r"The total cost is $O(V(L^\tau+1)+MA^3+\delta_{\rm bad}MA(R+A))$, which is $O(V(L^\tau+1))$ when records are far longer than any power of $p$ and $K/\log p\to\infty$.",
         r"The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans", ["constant-factors-versus-asymptotic-dominance"]),
   infer("S2.2.8", r"A fixed binary change of basis on $e=mf$ axes and its inverse therefore cost $O(V((eK)^\tau+1))$.",
         r"the complete change of basis and its inverse therefore cost", ["xor-and-mod-2-arithmetic"]),
  ],
  mot_quote=r"of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of",
  frm=["chunk-interchange","controlled-shift","stream-ops","sorting-merging-and-radix-sort","xor-and-mod-2-arithmetic"], page="packed-bit-addition",
  adds=[(r"L","slot width",r"The number $fK$ of address bits in each of the three chunks.","count"),
        (r"\rho","bit offset",r"The position, counted from the least significant end, of the selected bit inside each $K$-bit chunk.","direct"),
        (r"\delta_{\rm bad}","bad fraction",r"The fraction of addresses at which packed segments may carry, at most $80(f-1)2^{-K}$.","direct")])

Y3 = show("S2.3",
  r"Batching a common layer on a fixed number of tapes gives time per unit volume $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, hence cost $O(Vd^{\lambda'})$ for $D\le d$ selected chunks.",
  "Reserve $O(\\log d)$ chunks as a row index, split rows among the $W$ roles so each recursive call has volume $V/W$, recurse down to $e<d^\\beta$ where individual kernels are used, and sum the resulting recurrence over a base-$m$ partition of the chunks.",
  "The same volume-splitting trick as for the interchange makes the branching ratio $s/W$ rather than $s$, so the recursion again has a geometric cost below the linear one.",
  "recoverable",
  [
   infer("S2.3.1", r"A single kernel $C$ on one selected bit costs $O(V)$ by splitting on the bit, one paired exact arithmetic scan, and a merge, so $e$ individual kernels cost $O(Ve)$.",
         r"Thus \(e\) individual kernels cost", ["stream-ops"]),
   infer("S2.3.2", r"At an internal node the phase construction makes $s$ recursive calls, and basis changes, scalar gates and reassembly cost $O(V((eK)^\tau+1))$.",
         r"The phase construction supplies one recursive call on a slot for each", ["phase-frame-reduction","packed-bit-addition"]),
   infer("S2.3.3", r"The first $q_0=O(\log d)$ chunks are handled by individual kernels and then serve as a row index of range at least $W^{k_0}$, padded with zero rows to a multiple of $W^{k_0}$.",
         r"Otherwise apply \(C\) individually on the selected bits of the first", ["stream-ops"]),
   infer("S2.3.4", r"Writing a row index as $u=Wg+w$ and sending the entire row to role $w$ makes each recursive edge call act on a stream of exactly $1/W$ of its parent's volume.",
         r"At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\),", ["stream-ops"]),
   infer("S2.3.5", r"Parking the inactive role streams on a LIFO tape lets a fixed number of tapes serve the whole recursion, at cost proportional to the node's own volume.",
         r"The \(W\) role streams use a fixed number of tapes.  Before entering a", ["tape-based-subroutines-and-stacks"]),
   infer("S2.3.6", r"The normalized cost satisfies $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ with $F(e)=O(e)$ for $e<d^\beta$.",
         r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),", ["divide-and-conquer-and-recurrences"]),
   infer("S2.3.7", r"With $a=s/W\le m^\sigma<m^\lambda$ the internal costs sum to $O(e^\lambda)$, and the leaves contribute $O(e^\sigma d^{\beta(1-\sigma)})$.",
         r"Put \(a=s/W\).  Since \(a\le m^\sigma<m^\lambda\), the internal", ["divide-and-conquer-and-recurrences"]),
   infer("S2.3.8", r"Decomposing the remaining chunks in base $m$ into at most $(m-1)(1+\lfloor\log_md\rfloor)$ pieces gives total cost $O(d^{\lambda'})$ per unit volume.",
         r"Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\).", ["logarithms-floors-and-ceilings"]),
  ],
  frm=["complex-phase-network","rank-saving","chunk-interchange","divide-and-conquer-and-recurrences"],
  adds=[(r"\beta","cutoff exponent",r"The fixed exponent $1/2$ with recursion stopped when $e<d^\beta$.","direct"),
        (r"\lambda","internal exponent",r"A fixed exponent with $\max\{\tau,\sigma\}<\lambda<1$ bounding the cost at internal nodes.","direct"),
        (r"\sigma","branching exponent",r"A fixed exponent $1-2^{-50}$ with $s/W\le m^\sigma$.","direct")])

Y4 = show("S2.4",
  r"The whole layer can be evaluated exactly with $p+\Delta$ fractional bits and $\Delta+3$ integer bits per component, where $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$.",
  "Bound the arithmetic dependency depth $A(e)$ of any chain of additions, halvings and sign changes by a recurrence $A(e)\\le sA(e/m)+E$, and convert depth into growth of denominators and magnitudes.",
  "Each elementary operation can at most double the modulus and add one denominator bit, so bounding chain length bounds both exactly, and exact dyadic arithmetic needs no rounding inside the layer.",
  "recoverable",
  [
   infer("S2.4.1", r"At internal nodes the dependency depth satisfies $A(e)\le sA(e/m)+E$ with $E=64(W+m+1)^3$, since the depth estimate concatenates the $s$ calls.",
         r"A(e)\le sA(e/m)+E", ["divide-and-conquer-and-recurrences"]),
   infer("S2.4.2", r"Unrolling gives $A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}$ with $B=s+E$.",
         r"A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}.", ["divide-and-conquer-and-recurrences"]),
   infer("S2.4.3", r"With the base-$m$ pieces and the outer diagonals the total depth is below $C_0d^{C_1}$ with $C_1=20$.",
         r"&<128mB^2d^{\nu+3}\le C_0d^{C_1}.", ["constant-factors-versus-asymptotic-dominance"]),
   infer("S2.4.4", r"A value at depth $\ell$ lies in $2^{-(p+\ell)}\mathbb Z[i]$ with modulus at most $2^\ell$, so $p+\Delta$ fractional bits and $\Delta+3$ integer bits per component represent every intermediate value exactly.",
         r"To see how this count controls numerical size, start with disk-valued", ["dyadic-and-rational-numbers","two-s-complement-and-signed-integers"]),
   infer("S2.4.5", r"Choosing $\epsilon C_1<1$ with $d=\Theta(p^\epsilon)$ makes $\Delta=o(p)$, so the full coefficient width stays $O(p)$.",
         r"Choose \(\epsilon C_1<1\).  Since \(d=\Theta(p^\epsilon)\),", ["big-o"]),
  ],
  frm=["fixed-point","divide-and-conquer-and-recurrences","dyadic-and-rational-numbers"],
  adds=[(r"\Delta","guard bits",r"The number $\lceil C_0d^{C_1}\rceil$ of extra fractional bits reserved to keep every intermediate value exact.","count"),
        (r"A(e)","dependency depth",r"The largest number of arithmetic operations on a chain from an input coefficient to an intermediate coefficient of a group of $e$ axes.","count")])

Y5a = infer("S2.5", r"On records of $r$ coefficients the procedure returns $Q_p(\mathcal Hz)$ in the same array and format in $O(Vd^{\lambda'})$ time, uniformly over the allowed parameters.",
            r"coefficient order, and component format in $O(Vd^{\lambda'})$ time,", ["fixed-point"])
Y5b = infer("S2.6", r"The packed-call overhead terms $A_*^3/R_{\rm g}$ and $80(f-1)2^{-K}A_*(1+A_*/R_{\rm g})$ both tend to zero uniformly, so every packed call has the lemma's cost with one common constant.",
            r"Both bounds tend to zero uniformly over all current allowed $d,r$.", ["constant-factors-versus-asymptotic-dominance"])
Y5c = infer("S2.7", r"Equation $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ converts the exact $C$-layer into the normalized layer $\mathcal H$.",
            r"converts the resulting exact $C$-layer to $\mathcal H$.", ["butterfly-fft"])
Y5d = infer("S2.8", r"Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays and the single truncation $Q_p$ adds error less than $\sqrt2\,2^{-p}$.",
            r"absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk", ["fixed-point","vector-norms-and-the-triangle-inequality"])

Y = show("S2",
  r"Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ at once to the same bit position in $D\le d$ address chunks of polynomial records, exactly in Gaussian dyadics and followed by one truncation, costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$.",
  "Rewrite the $H_0$ layer through the phase kernel $C$, evaluate $C^{\\otimes e}$ by the complex network with $s$ calls on $e/m$ axes whose binary basis changes are packed selected-bit additions, bound the recurrence, and show that $o(p)$ guard bits keep everything exact.",
  "Doing the $D$ butterflies one after another needs $D$ passes over the data; a network whose recursion again splits into pieces with total size only slightly below the naive branching makes the cost per volume $d^{\\lambda'}$ instead of $d$.",
  "explicit",
  [Y1, Y2, Y3, Y4, Y5a, Y5b, Y5c, Y5d],
  mot_quote=r"factors would require $D$ whole-array passes.",
  frm=["chunk-interchange","complex-phase-network","rank-saving","fixed-point","ring-mod-yr","butterfly-fft"], page="simultaneous-layer",
  adds=[(r"d","axis bound",r"The maximum number of axis chunks on which a layer acts at once, $d=\Theta(p^\epsilon)$.","count"),
        (r"D","selected chunks",r"The number of consecutive $K$-bit chunks in which the same bit position is selected.","count"),
        (r"K","chunk width",r"The number $\lfloor d^c\rfloor$ of bits in each address chunk.","count"),
        (r"r","record length",r"The number of complex coefficients in each polynomial record, a power of two.","count"),
        (r"p","precision",r"The number of fractional bits of each stored real or imaginary component.","count"),
        (r"\lambda'","layer exponent",r"A fixed exponent $\lambda'<1$ in the layer cost $O(Vd^{\lambda'})$.","direct")],
  salient="The cost per unit volume is $d^{\\lambda'}$ with $\\lambda'<1$, strictly better than the $d$ passes of separate butterflies, for the same reason as in the interchange: $s/W<m^\\sigma$ with $\\sigma<1$.")

# ---------------------------------------------------------------- Z : ring convolution
Z1 = show("S3.1",
  r"In $\mathcal R_r=\mathbb C[y]/(y^r+1)$ the roots $\omega_t=y^{2r/t}$ act as exact signed shifts of the coefficient list, so the butterfly transforms $F_t^\mp$ are contractions computed with cheap shifts, and they leave frequencies in bit-reversed order $B_t$.",
  "Run the usual decimation-in-frequency recursion with the ring's own roots of unity: pair $z_k$ with $z_{k+t/2}$, apply $H_0$, twist the second output by $\\omega_t^{-k}$ and recurse on both halves.",
  "Powers of $y$ serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list.",
  "explicit",
  [
   infer("S3.1.1", r"Every power of $\omega_t$ is an isometry and each transform entry is an average of such images, so both transforms are contractions.",
         r"Every power of $\omega_t$ is an isometry, and each transform entry is", ["contraction-error","ring-mod-yr"]),
   infer("S3.1.2", r"Despite the zero divisors of the ring, character sums vanish unless $t\mid j$, giving $F_t^+F_t^-=t^{-1}I$.",
         r"Only the second case needs proof.  Write $j=2^v j_0$ with $j_0$ odd", ["dft","ring-mod-yr"]),
   infer("S3.1.3", r"Pairing $z_k$ with $z_{k+t/2}$, applying $H_0$, twisting the second output by $\omega_t^{-k}$ and recursing on both halves computes $F_t^-$.",
         r"procedure separately within the two branches.  This computes", ["butterfly-fft"]),
   infer("S3.1.4", r"The entry $(F_t^-z)_j$ lands in slot $\operatorname{rev}_a(j)$: the recursion writes its outputs directly in bit-reversed order $B_t$ without moving whole frequency indices.",
         r"After all $a$ rounds, the named slots from high to low therefore", ["butterfly-fft"]),
   infer("S3.1.5", r"Traversing the recursion in reverse on the stored order implements $F_t^+B_t^{-1}$, so the opposite transform consumes the retained frequency order.",
         r"The procedure consuming this stored order traverses the recursion in", ["butterfly-fft","dft"]),
   infer("S3.1.6", r"On several axes a round is one parallel butterfly $\mathcal H$ followed by a single monomial multiplication $J_E$ by $y^E$ at each address.",
         r"Consequently the individual axis steps may be grouped as a parallel", ["multidim-transform"]),
   infer("S3.1.7", r"Each $\mathcal H$ is a contraction and each $J_E$ an isometry, so every completed round is a contraction.",
         r"$J_E$ is an isometry, so every completed round is a contraction.", ["contraction-error"]),
  ],
  mot_quote=r"serve as roots of unity in the remaining axes, and multiplication by",
  frm=["ring-mod-yr","dft","butterfly-fft","contraction-error","multidim-transform"], page="synthetic-transform",
  adds=[(r"\omega_t","synthetic root",r"The element $y^{2r/t}$ of $\mathcal R_r$, acting as a signed shift, that plays the role of a primitive $t$th root of unity.","direct"),
        (r"B_t","bit reversal",r"The record permutation moving the entry at $j$ to $\operatorname{rev}_a(j)$.","direct")],
  salient="Although $\\mathcal R_r$ has zero divisors, the usual cancellation $F_t^+F_t^-=t^{-1}I$ still holds, because the character sum is annihilated by $y^{rj_0}=-1$.")

Z2 = show("S3.2",
  r"On the stored layout $L$ the forward synthetic transform has exact counterpart $LBF^-_{\boldsymbol t}$, the opposite one $F^+_{\boldsymbol t}B^{-1}L^{-1}$, each with error below $\sqrt2\,\ell\,2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.",
  "Bring the selected bits of all axes to a common offset in consecutive $K$-bit chunks by prefix-slot moves and chunk interchanges, then run each round of the transform as one simultaneous butterfly layer followed by a monomial multiplication, truncating once per round.",
  "The simultaneous layer applies only when the selected bits of the participating axes lie at the same offset in consecutive equal chunks.",
  "explicit",
  [
   infer("S3.2.1", r"The $O(dK)$ listed slots of the long axes and low bits are moved to a prefix, costing $O(TpdK)$, and the bottom rounds on prefix slots are done by individual butterflies.",
         r"so the moves cost $O(TpdK)$", ["stream-ops"]),
   infer("S3.2.2", r"At most $Dq-1$ exchanges of width-$K$ chunks bring the chunks into the order $(1,1),\dots,(D,1),(1,2),\dots,(D,q)$, costing $O(Tp\cdot pK^{\tau-1})$.",
         r"To obtain this order, scan its target positions from left to right.", ["chunk-interchange"]),
   infer("S3.2.3", r"Each round on the remaining chunks is one simultaneous layer of cost $O(Tpd^{\lambda'})$, so the at most $\ell$ rounds cost $O(Tp\ell d^{\lambda'})$.",
         r"The simultaneous-layer procedure therefore applies at cost", ["simultaneous-layer"]),
   infer("S3.2.4", r"Rounds on prefix slots process their bits individually at $O(Tp)$ each, in all $O(TpdK)$.",
         r"In a round on prefix slots, process the participating bits individually.", ["butterfly-fft"]),
   infer("S3.2.5", r"Multiplication by $y^E$ with $E=er+s$ splits the coefficient list in two pieces, swaps them and negates the moved tail, at $O(rp)$ per record.",
         r"To implement the monomial, write $E=er+s$ with $0\leq s<r$.", ["ring-mod-yr"]),
   infer("S3.2.6", r"Truncation toward zero commutes with the signed coefficient permutation $J_E$, so each round is one exact contraction followed by a single truncation.",
         r"Thus the actual forward call sequence returns exactly the result of", ["fixed-point"]),
   infer("S3.2.7", r"Each of the at most $\ell$ rounds contributes less than $\sqrt2\,2^{-p}$ and keeps the unit disk, and the layout permutations are isometries, giving error below $\sqrt2\,\ell\,2^{-p}$.",
         r"give the claimed error and disk bounds.", ["contraction-error","fixed-point"]),
   infer("S3.2.8", r"The forward entry with frequency address $j$ is stored at $L(Bj)$, and the final movement $L^{-1}$ restores axis-major order after the opposite transform.",
         r"In particular, the forward entry with frequency address $j$ is", ["butterfly-fft"]),
  ],
  mot_quote=r"we must place the selected bits of the participating axes at a common",
  frm=["simultaneous-layer","chunk-interchange","synthetic-transform","fixed-point","ring-mod-yr"], page="transform-layout",
  adds=[(r"L","layout permutation",r"The positional permutation of record addresses that brings the selected bits of all axes to common offsets in consecutive chunks.","direct"),
        (r"q","chunks per axis",r"The number $\lfloor(\ell-1)/K\rfloor$ of $K$-bit chunks left on each axis after the prefix moves.","count"),
        (r"D","number of axes",r"The number $d-1$ of power-of-two axes outside the ring coordinate.","count")])

Z3 = show("S3.3",
  r"Two disk-grid polynomials in $\mathcal R_r$ are multiplied exactly by evaluating their signed integer coefficient polynomials at $B_0=2^{4p}$, multiplying with the established $O(N\log N)$ integer multiplier, recovering coefficients by centred residues, reducing modulo $y^r+1$ and truncating after division by $r$, in time $O(rp\log(rp))$ with error below $\sqrt2\,2^{-p}$.",
  "Signed Kronecker substitution: pack the coefficients as digits of an integer in a base wide enough that no product coefficient overflows into its neighbour, multiply the integers, and read the coefficients back.",
  "A product coefficient is a sum of at most $r$ products of numbers of size $2^p$, so it is far below the base and each coefficient is determined by a residue modulo the base.",
  "recoverable",
  [
   infer("S3.3.1", r"Evaluating at $B_0=2^{4p}$ gives integers of at most $4pr$ bits, and four integer products give $A_aA_c$, $A_bA_e$, $A_aA_e$, $A_bA_c$.",
         r"shows that each magnitude fits in $4pr$ bits.  Multiply the four", ["schoolbook-multiplication-and-carries","two-s-complement-and-signed-integers"]),
   infer("S3.3.2", r"Every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<B_0/2$, so no field overlaps the next.",
         r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2.", ["modular-arithmetic"]),
   infer("S3.3.3", r"Reading the product in blocks with a carry in $\{0,1\}$, each coefficient is the centred residue of its block plus the carry.",
         r"Put $\rho_0=0$.  At block $j$, let $\widehat h_j$ be the unique", ["modular-arithmetic"]),
   infer("S3.3.4", r"The real and imaginary numerators are $ac-be$ and $ae+bc$; reduction modulo $y^r+1$ subtracts the coefficient at $j+r$ from that at $j$.",
         r"The real and imaginary numerator streams are respectively", ["complex-numbers","polynomials"]),
   infer("S3.3.5", r"Four exact integer products on $O(rp)$ bits dominate the linear packing, extraction, wrapping and truncation costs, giving $O(rp\log(rp))$.",
         r"Four exact integer products dominate the linear", ["big-o"]),
  ],
  frm=["ring-mod-yr","fixed-point","schoolbook-multiplication-and-carries","two-s-complement-and-signed-integers","modular-arithmetic"], page="signed-packing",
  adds=[(r"B_0","packing base",r"The integer $2^{4p}$ at which coefficient polynomials are evaluated to pack them into one integer.","direct")])

Zown = [
  infer("S3.4", r"The normalized convolution $\mathcal M_r(f,g)=f*g/(rM)$ averages $rM$ signed scalar products per output coefficient, so it is a bilinear contraction.",
        r"negacyclic wrap supplies the sign.  Thus that coefficient averages", ["contraction-error","convolution"]),
  infer("S3.5", r"Perform both forward transforms and retain their common $LB$ order, multiply the records pointwise by the ring product lemma, apply the opposite procedure to that order, and multiply exactly by $M$.",
        r"Perform both forward transforms and retain their common $LB$ order.", ["convolution"]),
  infer("S3.6", r"By the convolution theorem $F^-_{\boldsymbol t}(f*g)=M(F^-_{\boldsymbol t}f)(F^-_{\boldsymbol t}g)$, and $F^+F^-=I/M$ gives $MF^+((F^-f)(F^-g)/r)=f*g/(rM)$.",
        r"=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g).", ["convolution","multidim-transform"]),
  infer("S3.7", r"Since $LB$ permutes whole records, $P(LBu,LBv)=LBP(u,v)$, so the opposite transform of the pointwise product of the stored outputs equals $F^+P(F^-f,F^-g)$.",
        r"Since $LB$ permutes records and leaves their polynomial suffixes", ["permutations"]),
  infer("S3.8", r"The error is below $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, from two forward errors, the product truncation, and the contraction property of the opposite transform.",
        r"The final exact multiplication by $M$ therefore gives error less than", ["contraction-error"]),
  infer("S3.9", r"There are $M=T/r$ pointwise polynomial products costing $O(Tp\log(rp))$ in total, plus the three transform costs.",
        r"There are $M=T/r$ pointwise polynomial products.  Their total cost", ["big-o"]),
]

Z = show("S3",
  r"Forward synthetic transforms over $\mathbb C[y]/(y^r+1)$, pointwise ring products by signed packing, and the opposite transform in the same stored order compute the normalized convolution $f*g/(rM)$ with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.",
  "Compute the convolution through the convolution theorem, but with transforms whose roots of unity are exact shifts, placed on a layout where simultaneous layers apply, and keep the bit-reversed frequency order from the forward to the opposite transform instead of sorting it.",
  "Pointwise multiplication commutes with applying the same record permutation to both operands, so the permutation never needs to be undone between the transforms.",
  "explicit",
  [Z1, Z2, Z3] + Zown,
  mot_quote=r"Pointwise multiplication commutes with applying the same record",
  frm=["simultaneous-layer","chunk-interchange","contraction-error","convolution","multidim-transform","dft","butterfly-fft","ring-mod-yr","fixed-point"], page="ring-convolution",
  adds=[(r"T","total size",r"The product $rM$ of the record length and the number of polynomial records, i.e. the number of complex entries of the padded box.","count"),
        (r"M","number of records",r"The product of the lengths of the axes outside the ring coordinate, i.e. the number of polynomial records.","count"),
        (r"\ell","log record length",r"The binary logarithm of the record length $r$.","count")])

# ---------------------------------------------------------------- Q : resampling
Q1 = show("S4.1",
  r"For coprime $s<t$ with $\theta=t/s-1>p/\alpha^4$ there are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computable to error below $p^2$ in time $O(tp^{3/2+\delta}\alpha)$.",
  "Use the Gaussian-resampling identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ of Harvey and van der Hoeven, and invert the near-identity $N=C\\mathsf T\\mathsf D$ by a Neumann series.",
  "The Gaussian weights make the longer transform of length $t$ reproduce the shorter one of length $s$ up to a small, invertible distortion $N-I$, which can be undone using a convergent series.",
  "recoverable",
  [
   infer("S4.1.1", r"Two Gaussian-weighted maps $\mathsf S,\mathsf T:\mathbb C^s\to\mathbb C^t$ are defined by sums over $j\in\mathbb Z$ of $e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j$ and $e^{-\pi\alpha^2(tj/s-k)^2}u_j$.",
         r"The Gaussian resampling argument uses two maps", ["euler-s-formula-and-complex-conjugation"]),
   infer("S4.1.2", r"The Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$ holds.",
         r"\mathsf T P_sF_s=P_tF_t\mathsf S,", ["dft","permutations"]),
   infer("S4.1.3", r"The distortion $N=C\mathsf T\mathsf D$ satisfies $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$.",
         r"\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}.", ["vector-norms-and-the-triangle-inequality"]),
   infer("S4.1.4", r"Since $\alpha^2\theta>p/\alpha^2>1$, $\|N-I\|<1/2$ and $N$ is invertible by the Neumann series.",
         r"Thus $\|N-I\|<1/2$, so $N$ is invertible", ["matrices-and-matrix-vector-products"]),
   infer("S4.1.5", r"Setting $A=\mathsf S'=\mathsf S/2$ and $B_0=\mathsf D'\mathsf J'C$ gives contractions, since $\|\mathsf S'\|<3/4$, $\|\mathsf J'\|<7/8$, $\|\mathsf D'\|<1$ and $\|C\|=1$.",
         r"Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$.", ["vector-norms-and-the-triangle-inequality"]),
   infer("S4.1.6", r"The normalizations multiply to $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$, which gives $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$.",
         r"which is \eqref{eq:no-sort-one-dimensional}.", ["dft"]),
   infer("S4.1.7", r"Harvey and van der Hoeven's ordered Gaussian algorithms and a zero-error ordered selection $C$ approximate $A$ and $B_0$ with errors below $p^2$ at cost $O(tp^{3/2+\delta}\alpha)$.",
         r"Contraction of the exact maps yields errors less than $16p<p^2$ and", ["big-o"]),
  ],
  frm=["dft","contraction-error","permutations","vector-norms-and-the-triangle-inequality","euler-s-formula-and-complex-conjugation","fixed-point"], page="gaussian-resampling",
  adds=[(r"A","Gaussian expansion",r"The contraction $\mathsf S/2$ that resamples a length-$s$ vector onto $t$ points with Gaussian weights.","direct"),
        (r"B_0","Gaussian compression",r"The contraction that selects $s$ of $t$ coordinates and undoes the Gaussian distortion.","direct"),
        (r"\theta","separation",r"The relative gap $t/s-1$ between the target and source lengths.","direct"),
        (r"\alpha","Gaussian width",r"The integer parameter, $2\le\alpha<\sqrt p$, controlling the width of the Gaussian weights.","direct"),
        (r"P_s","source permutation",r"The coordinate permutation $(P_su)_j=u_{tj}$ of a length-$s$ vector.","direct"),
        (r"P_t","target permutation",r"The coordinate permutation $(P_tv)_k=v_{-sk}$ of a length-$t$ vector.","direct")],
  salient="The accuracy $\\|N-I\\|<2^{-\\alpha^2\\theta}$ is extremely good because the Gaussian weights decay as $e^{-\\pi\\alpha^2\\theta^2}$-like away from the nearest sample, so a modest $\\alpha^2\\theta>p/\\alpha^2$ already makes the distortion tiny.")

Q2 = show("S4.2",
  r"Tensoring over $d$ axes, $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$, and the linewise implementation of $\mathcal A$ and $\mathcal B_0$ on the padded box has error below $dp^2$ and costs $O(dTp^{3/2+\delta}\alpha)$ plus $O(Tpd^2(1+\ell^\tau))$ to expose and restore the axes.",
  "Apply the one-dimensional map one coordinate line at a time on the full padded power-of-two box, exposing each axis as the innermost field by chunk interchanges.",
  "A tensor product of maps acts on each coordinate line independently, so a one-dimensional algorithm applied line by line, with the axes brought innermost one at a time, evaluates it.",
  "recoverable",
  [
   infer("S4.2.1", r"Tensoring the one-dimensional identity over the $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$, where $R=\bigotimes P_{s_i}$ and $Q=\bigotimes P_{t_i}$.",
         r"Tensoring \eqref{eq:no-sort-one-dimensional} proves", ["multidim-transform"]),
   infer("S4.2.2", r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$, so all axes cost $\sum_i(T/t_i)O(t_ip^{3/2+\delta}\alpha)=O(dTp^{3/2+\delta}\alpha)$.",
         r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$,", ["big-o"]),
   infer("S4.2.3", r"Exposing and restoring one axis needs $O(d)$ adjacent interchanges, each costing $O(Tp(1+\ell^\tau))$, so all axes cost $O(Tpd^2(1+\ell^\tau))$.",
         r"Exposing and restoring one axis needs", ["chunk-interchange"]),
  ],
  frm=["chunk-interchange","gaussian-resampling","multidim-transform"],
  adds=[(r"\gamma","scale exponent",r"The exponent $2d\alpha^2$ of the power of two by which the tensor identity is scaled.","direct"),
        (r"R","source permutation tensor",r"The tensor product $\bigotimes_iP_{s_i}$ of the source coordinate permutations.","direct"),
        (r"Q","target permutation tensor",r"The tensor product $\bigotimes_iP_{t_i}$ of the target coordinate permutations.","direct")])

Q3 = show("S4.3",
  r"With $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$ and even $t_i$, $QF_{\boldsymbol t}u=\overline a\cdot\bigl(a*(\overline a\cdot u)\bigr)/T$: a chirp multiplication, a cyclic convolution with the chirp array, and a second chirp multiplication.",
  "Expand the right side coefficientwise and check that the three chirp factors multiply to the Fourier phase $\\exp(2\\pi i\\sum_is_ij_ik_i/t_i)$.",
  "The product of the three chirp factors has an exponent quadratic in $j$, $j-k$ and $k$, and the squares cancel in pairs leaving the cross term $jk$ of the Fourier kernel.",
  "recoverable",
  [
   infer("S4.3.1", r"The chirp $a_{\boldsymbol j}$ has period $t_i$ in coordinate $i$, because replacing $j_i$ by $j_i+t_i$ changes its exponent by an integral multiple of $2\pi i$ when $t_i$ is even.",
         r"Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by", ["euler-s-formula-and-complex-conjugation","convolution"]),
   infer("S4.3.2", r"The coefficient of $u_{\boldsymbol k}$ on the right is $\frac1T\exp(2\pi i\sum_is_ij_ik_i/t_i)$, which is exactly the coefficient in $QF_{\boldsymbol t}$.",
         r"This is precisely the coefficient in $QF_{\boldsymbol t}$, because", ["dft","convolution"]),
  ],
  frm=["convolution","dft","multidim-transform","euler-s-formula-and-complex-conjugation"], page="bluestein",
  adds=[(r"a_{\boldsymbol j}","chirp",r"The quadratic-phase array $\exp(-\pi i\sum_is_ij_i^2/t_i)$ of period $t_i$ in coordinate $i$.","direct")])

Q4 = show("S4.4",
  r"The source permutation $R$ cancels: $(RF^+_{\boldsymbol s})\bigl[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)\bigr]=(u*v)/S^2$ with $S=\prod_is_i$, and conjugating input and output of an algorithm for $RF_{\boldsymbol s}$ gives one for $RF^+_{\boldsymbol s}$.",
  "Show that $RF^+R=F^+$ so the permutation $R$ disappears from the product formula, then apply the convolution theorem with its normalizations.",
  "A coordinate permutation commutes with pointwise products, so after $R$ is pulled through the pointwise product it meets the $R$ in front of $F^+$ and the two cancel.",
  "recoverable",
  [
   infer("S4.4.1", r"For a unit $c$ modulo $q$, substituting $h=ck$ in the Fourier sum gives $F_q^+R_c=R_c^{-1}F_q^+$, hence $RF^+_{\boldsymbol s}R=F^+_{\boldsymbol s}$.",
         r"For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$.", ["modular-arithmetic","permutations"]),
   infer("S4.4.2", r"With $F(u*v)=S(Fu)\cdot(Fv)$ and $F^+F=I/S$, the product becomes $F^+(Fu\cdot Fv)=(u*v)/S^2$.",
         r"The normalized convolution rule is", ["convolution","multidim-transform"]),
   infer("S4.4.3", r"Complex conjugation turns a negative-sign algorithm into a positive-sign one, commutes with the real permutation $R$, and preserves the grid, the norm and the error bound.",
         r"proving \eqref{eq:source-permutation-cancel}. Finally, conjugation", ["euler-s-formula-and-complex-conjugation"]),
  ],
  frm=["convolution","multidim-transform","permutations","dft"],
  salient="An arbitrary-looking permutation $R$ of the frequency coordinates never has to be executed: it appears in both forward transforms and in the opposite one, and cancels.")

Q = show("S4",
  r"Gaussian resampling with both coordinate permutations kept in the transform computes $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$: the chirp absorbs the target permutation $Q$, and the source permutation $R$ cancels across the two forward source transforms, the pointwise product and the opposite transform.",
  "Tensor the Harvey--van der Hoeven resampling identity over the axes, evaluate the middle factor by Bluestein's chirp identity, and use a permutation-cancellation identity instead of sorting twice per coordinate.",
  "Sorting twice on each coordinate would cost an extra logarithmic factor on every axis; leaving the permutations inside the formula lets them be absorbed by the chirp and cancelled in the product.",
  "explicit",
  [Q1, Q2, Q3, Q4],
  mot_quote=r"connects these two shapes. Its usual implementation sorts twice on each",
  frm=["dft","convolution","multidim-transform","contraction-error","chunk-interchange","permutations"], page="retained-permutations",
  adds=[(r"s_i","source length",r"The prime length of the $i$th source axis, just below $t_i$.","count"),
        (r"t_i","target length",r"The power-of-two length of the $i$th axis of the padded box.","count")])

# ---------------------------------------------------------------- A : multiplication algorithm
A1 = show("S5.1",
  r"For large $n$, put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$ split into $d$ axes $t_i\in\{r/2,r\}$, and distinct primes $s_i\in((1-2\eta)t_i,(1-\eta)t_i]$ with $\eta=1/(4d)$, so that $Tp=\Theta(n)$ and $T/2<S<T$.",
  "Choose fixed rational exponents with room to spare, derive the sizes from $n$, and find primes just below each power of two by an explicit interval estimate and deterministic search.",
  "The prime lengths must be close to the powers of two so that their product fills a fixed fraction of the padded box, while the ratios must leave enough separation for the resampling.",
  "explicit",
  [
   infer("S5.1.1", r"Fixed rational constants $\tau=\sigma=1-2^{-50}$, $\delta=1/16$, $\lambda=1-2^{-52}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$ satisfy all layer and exponent conditions with room to spare.",
         r"Take the following fixed rational numbers:", ["dyadic-and-rational-numbers"]),
   infer("S5.1.2", r"From $n$ put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $K=\lfloor d^c\rfloor$.",
         r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,", ["logarithms-floors-and-ceilings"]),
   infer("S5.1.3", r"Take a power of two $T\in[4n/b,8n/b)$ and $r=2^{\lceil(\log_2T)/d\rceil}$, so that the box has $d$ axes of lengths $r/2$ or $r$ with product $T$.",
         r"Take the power of two $T$ in $[4n/b,8n/b)$, and let", ["logarithms-floors-and-ceilings"]),
   infer("S5.1.4", r"Since $d\ell-\log_2T$ is an integer in $[0,d)$, at least one axis has length $r$, and it is chosen as the last axis.",
         r"Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis", ["logarithms-floors-and-ceilings"]),
   infer("S5.1.5", r"The sizes satisfy $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$.",
         r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad", ["big-o"]),
   infer("S5.1.6", r"The Gaussian width is $\alpha=\lceil(12d^2b)^{1/4}\rceil$, so that $\gamma=2d\alpha^2=o(b)$ and $2\le\alpha<\sqrt p$.",
         r"\alpha=\left\lceil(12d^2b)^{1/4}\right\rceil,", ["logarithms-floors-and-ceilings"]),
   infer("S5.1.7", r"Rosser--Schoenfeld-type estimates give at least $\eta x/(2\log x)$ primes in $((1-2\eta)x,(1-\eta)x]$ for $x>e^{2/\eta}$.",
         r"contains at least $\eta x/(2\log x)$ primes. Here $\log$ is the natural", ["primes-divisibility-coprimality-and-gcd"]),
   infer("S5.1.8", r"Both intervals, for $x=r/2$ and $x=r$, are disjoint and contain more than $d$ primes, so distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ exist.",
         r"We may therefore choose distinct odd primes satisfying", ["primes-divisibility-coprimality-and-gcd"]),
   infer("S5.1.9", r"Multiplying the lower bounds with Bernoulli's inequality gives $T/2<S<T$ for $S=\prod_is_i$.",
         r"Together with $s_i<t_i$, this gives $T/2<S<T$.", ["primes-divisibility-coprimality-and-gcd"]),
   infer("S5.1.10", r"Since $\theta_i>\eta$, $\alpha^4\theta_i>3db\ge p$, so every hypothesis of the resampling lemma holds for large $n$.",
         r"\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p.", ["gaussian-resampling"]),
   infer("S5.1.11", r"A deterministic scan with trial division finds the primes in $n^{o(1)}$ time, so they are generated by the machine rather than supplied as advice.",
         r"Since $p=6\lceil\log_2 n\rceil=\Theta(\log n)$, the search takes", ["primes-divisibility-coprimality-and-gcd"]),
  ],
  mot_quote=r"$t_i$: their product must occupy a fixed fraction of the padded box,",
  frm=["gaussian-resampling","primes-divisibility-coprimality-and-gcd","logarithms-floors-and-ceilings","constant-factors-versus-asymptotic-dominance","dyadic-and-rational-numbers"], page="parameters",
  adds=[(r"\epsilon","dimension exponent",r"The fixed exponent $2^{-75}$ with $d=\Theta(p^\epsilon)$ axes.","direct"),
        (r"\eta","prime-gap parameter",r"The fraction $1/(4d)$ below $t_i$ in which a prime source length $s_i$ is chosen.","direct"),
        (r"\ell","log record length",r"The binary logarithm of the record length $r$.","count"),
        (r"c","chunk exponent",r"The fixed exponent $2^{-56}$ with $K=\lfloor d^c\rfloor$.","direct")],
  salient="Every exponent is a tiny fixed rational, e.g. $\\epsilon=2^{-75}$, and every later inequality is checked against these exact values, which is why $\\kappa$ comes out as $2^{-182}$.")

A2 = show("S5.2",
  r"Writing both inputs as polynomials in $2^b$ with $q=\lceil n/b\rceil$ digits, their product is a cyclic convolution modulo $x^S-1$ without wraparound, with coefficients $c_j<2^{3b}$.",
  "Split the inputs into radix-$2^b$ digits and observe that the product of the two digit polynomials is the digit convolution, padded below the cyclic length.",
  "A product of two polynomials of degree below $T/4$ has degree below $S$, so reducing modulo $x^S-1$ changes nothing.",
  "recoverable",
  [
   infer("S5.2.1", r"Both inputs are written as polynomials in $2^b$, each with $q=\lceil n/b\rceil$ nonnegative digits.",
         r"Write the two inputs as polynomials in $2^b$, each with", ["binary-representation-of-integers","schoolbook-multiplication-and-carries"]),
   infer("S5.2.2", r"The product has degree at most $2q-2<S$, so convolution modulo $x^S-1$ has no nonzero wraparound.",
         r"Thus convolution modulo $x^S-1$ has no nonzero wraparound.  Every product", ["polynomials"]),
   infer("S5.2.3", r"Every product coefficient obeys $0\le c_j\le q(2^b-1)^2<2^{3b}$.",
         r"0\le c_j\le q(2^b-1)^2<2^{3b},", ["schoolbook-multiplication-and-carries"]),
  ],
  frm=["binary-representation-of-integers","schoolbook-multiplication-and-carries","polynomials","convolution"], page="integer-as-convolution",
  adds=[(r"q","number of digits",r"The number $\lceil n/b\rceil$ of radix-$2^b$ digits of each input.","count"),
        (r"c_j","product coefficient",r"The $j$th coefficient of the product of the two digit polynomials.","direct")])

A3 = show("S5.3",
  r"The map $\Phi:x\mapsto\prod_ix_i^{\mu_i}$ with $\mu_i=P_i^{-1}\bmod s_i$ is an isomorphism $\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$ preserving cyclic convolution, and on tape it is $d$ triangular controlled shifts costing $O(Tpd^2(1+\ell^\tau))$ with the axis reordering.",
  "Use the Chinese-remainder (Agarwal--Cooley) split with coordinate exponents chosen so that each new coordinate depends only on lower-index old coordinates, which turns the change of order into controlled cyclic shifts in tape order.",
  "A change of coordinates in which each new coordinate is its old value plus a function of earlier coordinates is exactly what a prefix-controlled cyclic shift of the target field performs in linear time.",
  "explicit",
  [
   infer("S5.3.1", r"The assignment $x\mapsto\prod_ix_i^{\mu_i}$ respects $x^S=1$, so it defines an algebra map.",
         r"respects $x^S=1$, so it defines an algebra map.", ["polynomials"]),
   infer("S5.3.2", r"Its image of $x$ has order $S$ because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so powers of it run through all target monomials once and $\Phi$ is an isomorphism preserving cyclic convolution.",
         r"therefore run through all target basis monomials exactly once.  Hence", ["primes-divisibility-coprimality-and-gcd","modular-arithmetic"]),
   infer("S5.3.3", r"For $k=\sum_ja_jP_j$ with $P_i=\prod_{j<i}s_j$, the coordinate on axis $i$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j \pmod{s_i}$, a triangular update.",
         r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}.", ["lexicographic-order-and-mixed-radix-indexing"]),
   infer("S5.3.4", r"Updating targets in the order $i=d,\dots,1$ uses the original lower-index digits as controls, and zero padding stays zero since each step is a bijection preserving the valid set.",
         r"$i$ is updated, none of its lower-index controls has yet changed, so", ["controlled-shift"]),
   infer("S5.3.5", r"Each triangular update is a prefix-controlled cyclic shift: prepare the offset, split the valid target interval in two pieces and merge them in the opposite order.",
         r"Each triangular update is a prefix-controlled cyclic shift.  The", ["controlled-shift"]),
   infer("S5.3.6", r"With $O(d^2)$ axis moves for the reordering, $\Phi$, its inverse and their padding cost $O(Tpd^2(1+\ell^\tau))$.",
         r"uses $O(d^2)$ such moves.  Therefore the map $\Phi$, its inverse, and", ["chunk-interchange"]),
  ],
  mot_quote=r"algebraic split, with coordinate powers that make the change of order a",
  frm=["controlled-shift","chunk-interchange","convolution","multidim-transform","primes-divisibility-coprimality-and-gcd","modular-arithmetic","lexicographic-order-and-mixed-radix-indexing"], page="crt-map",
  adds=[(r"P_i","prefix product",r"The integer product $\prod_{j<i}s_j$ of the source lengths before axis $i$.","direct"),
        (r"\mu_i","CRT exponent",r"The inverse of $P_i$ modulo $s_i$ used as the exponent of $x_i$.","direct"),
        (r"\Phi","CRT map",r"The algebra isomorphism sending $x$ to $\prod_ix_i^{\mu_i}$.","direct")])

A41 = show("S5.4.1",
  r"Normalized cyclic convolution on all $d$ power-of-two axes is $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=f*g/T$: twist the last coordinate into the ring, convolve the other axes over $\mathcal R_r$, and untwist.",
  "Twisting the last coordinate by $\\zeta^k$ turns its cyclic wrap into the negative wrap of the ring $\\mathcal R_r$, so the ring convolution of the previous section computes the complex cyclic convolution.",
  "The cyclic axis cannot carry the synthetic roots, but after the twist its wraparound sign is exactly cancelled, so the ring does the job.",
  "explicit",
  [
   A_pt := show("S5.4.1.1",
     r"The map $\Theta:\mathbb C[x_d]/(x_d^r-1)\to\mathcal R_r$, $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$, is an isomorphism acting on coefficient $k$ by $\zeta^k$, and the negative wrap of $\mathcal R_r$ gives exactly the cyclic wrap after untwisting.",
     "Check that $x_d\\mapsto\\zeta y$ is well defined, diagonal on the coefficient bases and hence invertible, and then check the wrap sign term by term.",
     "A product term with $k+l=j+hr$ picks up $(-1)^h$ from the negative wrap and $\\zeta^{hr}=(-1)^h$ from the twist, which cancel.",
     "recoverable",
     [
      infer("S5.4.1.1.1", r"The map is well defined since $(\zeta y)^r=(-1)(-1)=1$.",
            r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$.", ["euler-s-formula-and-complex-conjugation"]),
      infer("S5.4.1.1.2", r"On the coefficient bases it is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$, hence an isomorphism with inverse $\zeta^{-k}$.",
            r"multiplying coefficient $k$ by the nonzero number $\zeta^k$.  It is therefore an", ["complex-numbers"]),
      infer("S5.4.1.1.3", r"For $k+l=j+hr$ a product term has factor $\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
            r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j.", ["euler-s-formula-and-complex-conjugation"]),
     ],
     frm=["ring-mod-yr","complex-numbers","euler-s-formula-and-complex-conjugation"], page="phase-twist",
     adds=[(r"\zeta","twist root",r"The root of unity $e^{\pi i/r}$ with $\zeta^r=-1$.","direct")]),
   infer("S5.4.1.2", r"Normalized complex cyclic convolution is $D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=f*g/T$, the division by $T$ being already part of $\mathcal M_r$.",
         r"by $T$ is already part of $\mathcal M_r$.", ["convolution"]),
   infer("S5.4.1.3", r"With component width $w=w_{\rm c}=p+2$ the scalar and synthetic formats agree, so $\iota$ and $\iota^{-1}$ change only the shape descriptor and need no payload movement.",
         r"For the tape representation, use the scalar format of", ["two-s-complement-and-signed-integers"]),
   infer("S5.4.1.4", r"The twists $D_\pm$ multiply by disk-grid approximations of $\zeta^{\pm k}$ with error below $2\cdot2^{-p}$, at total cost $O(Tp^{1+\delta})$.",
         r"For $0\le k<r$, obtain disk-grid approximations", ["fixed-point"]),
  ],
  mot_quote=r"obtained from the synthetic convolution by a coefficient twist.",
  frm=["phase-twist","ring-convolution","fixed-point","convolution"], page="complex-convolution-twist",
  adds=[(r"\iota","ring identification",r"The identification of the scalar array with an array of polynomial records in $\mathcal R_r$.","direct"),
        (r"D_\pm","twist",r"The diagonal operators multiplying coefficient $k$ by $\zeta^{\pm k}$.","direct")])

A4rest = [
   infer("S5.4.2", r"The chirp array is computed from the phase numerator $-\sum_is_ij_i^2(r/t_i)\bmod 2r$ at every address, costing $O(Tdp^{1+\delta})$ in total.",
         r"All integers have $O(p)$ bits and $r/t_i\in\{1,2\}$.  Scan the stored", ["modular-arithmetic"]),
   infer("S5.4.3", r"The computed chirp transform multiplies by $\overline{\widetilde a}$ to get $x_0$, convolves with the kernel $\widetilde a$ via the complex convolution, and multiplies by $\overline{\widetilde a}$ again, with error below $8TL\,2^{-p}$.",
         r"Thus $\widetilde a$ is the convolution kernel and $x_0$ is the data", ["bluestein"]),
   infer("S5.4.4", r"The source transform applies the Gaussian map $\mathcal A$ on each line, the chirp transform, the Gaussian map $\mathcal B_0$, and then scales the grid numerators exactly by $2^\gamma$.",
         r"For a source disk-grid tensor of norm at most $.5$, write", ["gaussian-resampling","retained-permutations"]),
   infer("S5.4.5", r"Its exact counterpart is $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.",
         r"=RF_{\boldsymbol s}.", ["retained-permutations"]),
   infer("S5.4.6", r"The opposite-sign procedure is $\widetilde{\mathscr F}^+(z)=\overline{\widetilde{\mathscr F}(\overline z)}$, with exact counterpart $RF^+_{\boldsymbol s}$.",
         r"=\overline{\widetilde{\mathscr F}(\overline z)};", ["euler-s-formula-and-complex-conjugation"]),
]

A4 = show("S5.4",
  r"The procedure $\widetilde{\mathscr F}$ evaluates $RF_{\boldsymbol s}$ (and by complex conjugation $RF^+_{\boldsymbol s}$): Gaussian map $\mathcal A$ on each line, the chirp-based transform via complex convolution, Gaussian map $\mathcal B_0$, then scaling by $2^\gamma$.",
  "Compose the three factors of $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, evaluating the middle factor by Bluestein's chirp identity and the power-of-two complex convolution.",
  "The Gaussian maps handle the change from prime to power-of-two length, and the middle transform, a transform on power-of-two axes with chirp factors, is a convolution which the ring machinery already computes.",
  "explicit",
  [A41] + A4rest,
  mot_quote=r"We next use the complex convolution to evaluate the middle factor",
  frm=["gaussian-resampling","retained-permutations","bluestein","ring-convolution"], page="source-transform",
  adds=[(r"\widetilde{\mathscr F}","source transform procedure",r"The computed approximation of $RF_{\boldsymbol s}$ built from the Gaussian maps and the chirp transform.","direct"),
        (r"x_0","chirped operand",r"The data operand after the first endpoint chirp multiplication.","direct")])

A5 = [
  infer("S5.5.1", r"Read each operand backward in groups of $b$ bits to obtain the radix-$2^b$ digits in increasing coefficient order, and write digit $a_j$ as the exact grid value $a_j2^{-b-2}$.",
        r"its least significant end in groups of $b$ bits. This produces the radix-$2^b$ digits", ["binary-representation-of-integers"]),
  infer("S5.5.2", r"Step 1: apply the coefficient-address map $\Phi$ with its padded layout to obtain source arrays $u,v$.",
        r"\item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain", ["crt-map"]),
  infer("S5.5.3", r"Step 2: compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.",
        r"\item Compute $\widetilde{\mathscr F}(u)$ and", ["source-transform"]),
  infer("S5.5.4", r"Step 3: multiply corresponding coefficients exactly and truncate to $p$ fractional bits to get $z$.",
        r"\item Multiply corresponding complex coefficients exactly and truncate", ["fixed-point"]),
  infer("S5.5.5", r"Step 4: compute $\widetilde{\mathscr F}^+(z)$ and multiply its grid numerators exactly by $S$ to get $\widetilde w$.",
        r"\item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid", ["source-transform"]),
  infer("S5.5.6", r"Step 5: multiply by $2^{2b+4}S$, round the real parts to the nearest integers and apply $\Phi^{-1}$ to restore the ordinary coefficient order.",
        r"\item Multiply the grid numerators of $\widetilde w$ exactly by", ["crt-map"]),
  infer("S5.5.7", r"Step 6: propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits.",
        r"\item Propagate radix-$2^b$ carries in increasing coefficient order.", ["schoolbook-multiplication-and-carries"]),
  infer("S5.5.8", r"The two occurrences of $S$ undo different normalizations.",
        r"The two occurrences of $S$ in this algorithm undo different", ["retained-permutations"]),
  infer("S5.5.9", r"After the three transforms the exact counterpart is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$.",
        r"counterpart after the three transforms is $(u*v)/S^2$, so after the", ["retained-permutations"]),
]

A6 = show("S5.6",
  r"After removing the known scales each recovered digit-convolution coefficient has error below $448b\,2^{-3b/4}<1/2$, so rounding gives the exact integer coefficients and radix-$2^b$ carries give the $2n$-bit product.",
  "Track disk membership and absolute error through every computed map using contraction bounds and the rule that errors of composed approximations add, then bound the total after the final rescalings.",
  "Every map is a contraction or bilinear contraction of norm one, so each approximation adds only its own local error, and the working precision $p=6b$ leaves a huge margin over the scale factors.",
  "explicit",
  [
   infer("S5.6.1", r"For a bilinear contraction $\mathcal M$, replacing its operands changes the output by at most $\|f'-f\|\,\|g'\|+\|f\|\,\|g'-g\|$, so when all operands are in the disk the two errors add.",
         r"For a bilinear contraction $\mathcal M$, replacing its operands gives", ["contraction-error"]),
   infer("S5.6.2", r"A computed phase product has error $(2\|x\|+\sqrt2)h_p<4h_p$ and does not increase the norm.",
         r"(2\|x\|+\sqrt2)h_p<4h_p,", ["fixed-point"]),
   infer("S5.6.3", r"The ring convolution has error $E_{\rm ring}=M(3L+2)<5TL$ in units of $h_p$ and output norm below $.701$.",
         r"E_{\rm ring}:=M(3L+2)<5TL.", ["ring-convolution"]),
   infer("S5.6.4", r"The computed complex convolution has error below $6TL\,h_p$.",
         r"<(E_{\rm ring}+4+4+4)h_p<6TLh_p.", ["phase-twist"]),
   infer("S5.6.5", r"The computed chirp transform has error below $8TL\,h_p$.",
         r"<(6TL+2+4+4)h_p<8TLh_p.", ["bluestein"]),
   infer("S5.6.6", r"The source transform has error below $E_sh_p$ with $E_s=9\,2^\gamma TL$.",
         r"E_s=9\,2^\gamma TL,", ["gaussian-resampling"]),
   infer("S5.6.7", r"The pointwise product satisfies $\|z-U\cdot V_1\|<(2E_s+2)h_p$.",
         r"Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$.", ["contraction-error"]),
   infer("S5.6.8", r"After the opposite transform and the first scale by $S$, $\widetilde w$ approximates $w=(u*v)/S$ with error below $E_wh_p$, $E_w=S(3E_s+2)<28\,2^\gamma T^2L$.",
         r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L.", ["retained-permutations"]),
   infer("S5.6.9", r"After the second scale the absolute error is below $448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<1/2$.",
         r"\le448b\,2^{-3b/4}<\frac12.", ["constant-factors-versus-asymptotic-dominance"]),
   infer("S5.6.10", r"The true coefficients are integers, so with error below $1/2$ the nearest integer to the computed value is the unique correct coefficient.",
         r"The true coefficients are real integers.  If $H_j$ is the real", ["binary-representation-of-integers"]),
   infer("S5.6.11", r"The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$, and the invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ fixes the radix digits.",
         r"The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$.  If this holds at", ["schoolbook-multiplication-and-carries"]),
   infer("S5.6.12", r"The exact product is less than $2^{2n}$, so after removing zero padding bits exactly $2n$ output bits remain.",
         r"than $2^{2n}$; all bits above position $2n-1$ are therefore zero.", ["binary-representation-of-integers"]),
  ],
  mot_quote=r"When all four operands are in the disk, their two errors therefore add.",
  frm=["contraction-error","fixed-point","ring-convolution","gaussian-resampling","retained-permutations","bluestein","phase-twist","integer-as-convolution"], page="exact-recovery",
  adds=[(r"h_p","grid unit",r"The grid spacing $2^{-p}$ in which absolute errors are measured.","direct"),
        (r"E_s","source error",r"The bound, in units of $h_p$, on the error of the computed source transform after the scale $2^\gamma$.","direct"),
        (r"E_w","scaled error",r"The bound, in units of $h_p$, on the error of the computed first scaled result.","direct")],
  salient="The final error $448b\\,2^{-3b/4}$ is far below $1/2$ because the working precision $p=6b$ dwarfs the scale $2^{2b+4}S$ and the Gaussian loss $2^\\gamma$ with $\\gamma=o(b)$.")

A = show("S5",
  r"The algorithm forms radix-$2^b$ digits, applies the CRT map $\Phi$, computes two forward source transforms, multiplies pointwise, applies the opposite transform, rescales by $S$ and $2^{2b+4}S$, rounds, inverts $\Phi$ and propagates carries to output the exact $2n$-bit product.",
  "Express the integer product as a cyclic convolution of radix-$2^b$ digit lists, compute that convolution through the transform pipeline with enough precision that rounding recovers the exact integer coefficients, and finish with carries.",
  "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients, which the transform pipeline can compute.",
  "explicit",
  [A1, A2, A3, A4] + A5 + [A6],
  mot_quote=r"Splitting the inputs into radix digits reduces multiplication to",
  frm=["binary-representation-of-integers","schoolbook-multiplication-and-carries","source-transform"], page="multiplication-algorithm",
  adds=[(r"b","digit width",r"The number $\lceil\log_2n\rceil$ of bits in each radix digit.","count"),
        (r"S","cyclic length",r"The product $\prod_is_i$ of the prime source lengths, with $T/2<S<T$.","count"),
        (r"T","padded box size",r"The power of two $T\in[4n/b,8n/b)$ equal to the product of the axis lengths $t_i$.","count"),
        (r"p","precision",r"The working precision $6b$ in fractional bits.","count")],
  salient="The factor $S$ is removed twice, once to undo the normalizations of the three transforms and once to undo the normalization of the pointwise product $w=(u*v)/S$, together with the digit scales $2^{2b+4}$.")

# ---------------------------------------------------------------- C : cost accounting
C = show("S6",
  r"Divided by $Tp=\Theta(n)$, every cost row has a power of $p$ at most $1-2\kappa$, with smallest margin $2^{-181}=2\kappa$, so all polylogarithmic losses are absorbed and the total time is $O(n(\log n)^{1-\kappa})$.",
  "Tabulate the normalized cost of each stage in powers of $p$, bound the seven dominant powers by explicit margins $g_i$ below one, and absorb the remaining setup, repair and logarithmic factors.",
  "Each stage costs $Tp$ times a power of $p$ that is strictly below one, so the largest exponent decides the total, and any fixed power of $\\log p$ is smaller than the slack.",
  "explicit",
  [
   infer("S6.1", r"Put $V=Tp=\Theta(n)$; the coefficient formats use $\Theta(p)$ bits so a full padded array has $\Theta(V)$ stored bits, and the table lists costs divided by $V$.",
         r"For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient", ["constant-factors-versus-asymptotic-dominance"]),
   infer("S6.2", r"The seven dominant powers have margins $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$, hence $\min_ig_i=2^{-181}=2\kappa$.",
         r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad", ["dyadic-and-rational-numbers"]),
   infer("S6.3", r"The first three table rows are the synthetic-transform cost terms $dK$, $pK^{\tau-1}$ and $\ell d^{\lambda'}$.",
         r"The first three rows are the terms in", ["transform-layout"]),
   infer("S6.4", r"The $O(p/K)$ chunk exchanges each cost $O(VK^\tau)$, so the normalized total is $O(pK^{\tau-1})$.",
         r"$O(VK^\tau)$ by Lemma~\ref{lem:chunk-swap}, so the normalized total is", ["chunk-interchange"]),
   infer("S6.5", r"The at most $\ell$ simultaneous rounds cost $O(Vd^{\lambda'})$ each, which already includes basis changes, repair and padding.",
         r"Proposition~\ref{prop:simultaneous-layer} supplies $O(Vd^{\lambda'})$", ["simultaneous-layer"]),
   infer("S6.6", r"Axis exposure and restoration take $O(d^2)$ adjacent axis moves, each costing $O(V(1+\ell^\tau))$.",
         r"Axis exposure and restoration require $O(d^2)$ adjacent axis moves.", ["chunk-interchange","crt-map"]),
   infer("S6.7", r"Gaussian resampling processes at most $T/t_i$ lines on axis $i$, so the line machines sum to $O(dTp^{3/2+\delta}\alpha)$.",
         r"For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines.", ["gaussian-resampling"]),
   infer("S6.8", r"Chirp numerators are computed modulo $2r$ as sums of $d$ terms with the established multiplier, at cost $O(dp^{1+\delta})$ per entry.",
         r"Chirp numerators have $O(p)$ bits and can be computed modulo $2r$ as", ["bluestein"]),
   infer("S6.9", r"The pointwise ring products need four integer products on $O(rp)$ bits per record, in total $O(Tp\log(rp))$.",
         r"products on $O(rp)$ bits per record therefore cost", ["signed-packing"]),
   infer("S6.10", r"Setup at recursion nodes and per-record or per-line descriptor work cost $o(Tp)$, because $r$ exceeds every fixed power of $p$.",
         r"We next separate setup at recursion nodes from work repeated for every", ["parameters"]),
   infer("S6.11", r"The compact exceptional stream and its stable sorting cost $O(Vp^{A'}2^{-K})=o(V)$, a deterministic worst-case bound.",
         r"for another fixed exponent $A'$.  Here $d=O(p^\epsilon)$ and", ["packed-bit-addition"]),
   infer("S6.12", r"Each of the seven displayed powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually.",
         r"Each of the seven displayed powers is at most $1-2\kappa$ by", ["constant-factors-versus-asymptotic-dominance"]),
   infer("S6.13", r"The complete large-input bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
         r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}).", ["big-o"]),
   infer("S6.14", r"Below a fixed cutoff use schoolbook multiplication; the finitely many smaller lengths are absorbed in the implicit constant, giving one fixed machine for every input length.",
         r"Fix one cutoff beyond all the size, precision, margin and layout", ["schoolbook-multiplication-and-carries"]),
  ],
  mot_quote=r"Thus $\min_i g_i=2^{-181}=2\kappa$.  This explicit slack will cover",
  frm=["multiplication-algorithm","parameters","simultaneous-layer","chunk-interchange","ring-convolution","gaussian-resampling","crt-map","constant-factors-versus-asymptotic-dominance"], page="cost-accounting",
  adds=[(r"g_i","margin",r"The distance below one of the exponent of $p$ in the $i$th dominant cost row.","direct")],
  salient="The smallest margin is $g_2=\\epsilon c(1-\\tau)=2^{-181}=2\\kappa$, a product of three tiny exponents; it, and not the cost of the butterfly layers, decides the value of $\\kappa$.")

ROOT = show("S0",
  r"A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.",
  "Build the algorithm bottom-up: two fast tape primitives (address-chunk interchange and simultaneous butterfly layers), synthetic transforms and ring convolution built on them, Gaussian resampling with retained permutations to reach prime-length transforms, the digit-convolution algorithm with its exactness proof, and a cost table.",
  "Scanning the data at each of the logarithmically many transform levels already costs $n\\log n$, so the saving has to come from both data movement and arithmetic.",
  "explicit",
  [S1, Y, Z, Q, A, C],
  mot_quote=r"We therefore need savings in both movement and arithmetic. Two tape",
  frm=["history","multitape-tm","big-o"], page="main-theorem",
  adds=[(r"n","input length",r"The number of bits of each of the two integers to be multiplied.","count"),
        (r"\kappa","saving exponent",r"The fixed exponent $2^{-182}$ by which the power of the logarithm is reduced.","direct"),
        (r"V","stored volume",r"The number of data bits stored on tape in the array a primitive operates on.","count")],
  salient="The exponent $\\kappa=2^{-182}$ is astronomically small but positive: it survives only because the rank saving $s<Wm$ is strict, and each later loss is absorbed by a margin of at least $2\\kappa$.")

# ---------------------------------------------------------------- validation
READING = ["history","stream-ops","controlled-shift","linear-algebra","linear-network","frames","subset-gadget","rank-saving","bit-network-shear","complex-phase-network","triangular-factorization","matrix-shear","power-width-interchange","chunk-interchange","packed-bit-addition","ring-mod-yr","fixed-point","signed-packing","dft","butterfly-fft","phase-frame-reduction","simultaneous-layer","contraction-error","convolution","multidim-transform","synthetic-transform","crt-map","bluestein","phase-twist","transform-layout","ring-convolution","gaussian-resampling","retained-permutations","integer-as-convolution","exact-recovery","parameters","complex-convolution-twist","source-transform","multiplication-algorithm","cost-accounting","main-theorem"]
KNOWN = ["big-o","polynomials","complex-numbers","multitape-tm","binary-representation-of-integers","modular-arithmetic","primes-divisibility-coprimality-and-gcd","logarithms-floors-and-ceilings","divide-and-conquer-and-recurrences","sorting-merging-and-radix-sort","schoolbook-multiplication-and-carries","permutations","sets-subsets-and-binomial-coefficients","xor-and-mod-2-arithmetic","hamming-weight","matrices-and-matrix-vector-products","vector-norms-and-the-triangle-inequality","lexicographic-order-and-mixed-radix-indexing","two-s-complement-and-signed-integers","dyadic-and-rational-numbers","euler-s-formula-and-complex-conjugation","tape-based-subroutines-and-stacks","constant-factors-versus-asymptotic-dominance"]

def validate(root):
    errs = []
    ids = set()
    pages_used = {}
    from_used = set()
    pos = [0]
    order = []
    def math_of(s):
        return " ".join(re.findall(r"\$(.+?)\$", s))
    def descendants(n):
        out = []
        for c in n.get("children", []):
            out.append(c); out += descendants(c)
        return out
    def walk(n, eff_page):
        if n["id"] in ids: errs.append("dup id " + n["id"])
        ids.add(n["id"])
        pg = n.get("page") or eff_page
        if n.get("page"):
            if n["page"] in pages_used: errs.append("page reused " + n["page"])
            pages_used[n["page"]] = n["id"]
            if n["page"] not in READING: errs.append("bad page " + n["page"])
        idx = READING.index(pg) if pg in READING else -1
        for f in n.get("from", []):
            from_used.add(f)
            if f in KNOWN: continue
            if f not in READING: errs.append("%s: unknown from %s" % (n["id"], f)); continue
            if READING.index(f) >= idx: errs.append("%s: from %s not before page %s" % (n["id"], f, pg))
        if n["intention"] == "infer":
            q = n["quote"]["quote"]
            c = SRC.count(q)
            if c != 1: errs.append("%s: quote count %d: %r" % (n["id"], c, q[:60]))
            else:
                p = SRC.index(q)
                line = SRC.count("\n", 0, p) + 1
                order.append((n["id"], p, line, n.get("deferred", False)))
            if n.get("children"): errs.append(n["id"] + " infer has children")
        else:
            if not n.get("children"): errs.append(n["id"] + " show without children")
            m = n["motivation"]
            if m["source"] == "explicit":
                if not m.get("quote"): errs.append(n["id"] + " explicit w/o quote")
                else:
                    q = m["quote"]["quote"]
                    if SRC.count(q) < 1: errs.append("%s: motivation quote missing %r" % (n["id"], q[:60]))
            for a in n.get("adds", []):
                ds = descendants(n)
                text = " ".join(math_of(d["claim"]) for d in ds)
                sym = a["symbol"]
                if re.fullmatch(r"[A-Za-z]", sym):
                    t2 = re.sub(r"\\[A-Za-z]+", " ", text)
                    ok = re.search(r"(?<![A-Za-z])" + sym + r"(?![A-Za-z])", t2) is not None
                else:
                    ok = sym in text
                if not ok: errs.append("%s: add symbol %s not in descendants' math" % (n["id"], sym))
            for c in n["children"]: walk(c, pg)
    walk(root, None)
    # order check
    last = -1
    for (i, p, line, d) in order:
        if d: continue
        if p <= last: errs.append("order violation at %s (line %d)" % (i, line))
        last = max(last, p)
    prs = set(pages_used)
    for pg in READING:
        if pg not in prs and pg not in from_used: errs.append("page not covered: " + pg)
    if pages_used.get("main-theorem") != "S0": errs.append("root page")
    return errs, order

if __name__ == "__main__":
    errs, order = validate(ROOT)
    for e in errs: print("ERR", e)
    print(len(order), "infer steps;", len(errs), "errors")
    json.dump({"root": ROOT}, open("/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e4/V3/exegenius/tasks/0045-argument.answer.json", "w"), ensure_ascii=False, indent=1)
