import json, re, sys

SRC = open('/home/user/openai-nlogn-wiki/runs/G2/sources/paper.tex', encoding='utf-8').read()

def ev(q):
    return {"source": "paper", "quote": q}

def expl(text, q):
    return {"text": text, "source": "explicit", "quote": ev(q)}

def rec(text):
    return {"text": text, "source": "recoverable", "quote": None}

def recon(text):
    return {"text": text, "source": "reconstructed", "quote": None}

def add(sym, name, meaning, rel):
    return {"symbol": sym, "name": name, "meaning": meaning, "relation": rel}

def show(id, claim, method, mot, children, page=None, frm=(), adds=None, salient=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": mot, "children": children, "from": list(frm)}
    if page: n["page"] = page
    if adds: n["adds"] = adds
    if salient: n["salient"] = salient
    return n

def infer(id, claim, quote, frm=(), deferred=False):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": list(frm)}
    if deferred: n["deferred"] = True
    return n

# ---------------------------------------------------------------- S1 networks
S1_1 = show("S1.1",
  r"A fixed circuit of linear gates on the wires, with arbitrary initial values on its scratch wires, sends the data banks $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restores every scratch value.",
  "Build one invocation that adds a control bank into a target bank while the unknown scratch values cancel, using a schedule that first subtracts the effect of the old scratch values, then adds the effect of the source values, then restores the scratch; compose three such invocations (add, subtract, add) in three stages to obtain the signed exchange.",
  expl("A schedule that first removes, then uses, then restores the scratch values makes the net map independent of what the scratch wires held.",
       "the following schedule remove the effect of the old scratch values;"),
  [infer("S1.1.1",
         r"One forward invocation changes the target value $y_S$ to $y_S+x_S$ and leaves every other value, scratch wires included, unchanged, whatever the initial scratch values.",
         "For arbitrary initial values of its auxiliary wires, a forward",
         frm=["finite-fields-and-the-field-f-2", "sets-subsets-and-cartesian-products"]),
   infer("S1.1.2",
         r"A forward invocation from $X$ to $Y$, the inverse invocation from $Y$ to $X$, and another forward invocation from $X$ to $Y$ send $(x,y)$ through $(x,y+x)$ and $(-y,y+x)$ to $(-y,x)$, restoring all scratch values.",
         "Performing a forward invocation from $X$ to $Y$ at stage 1,",
         frm=["vectors-matrices-and-linear-maps"])],
  page="linear-network",
  frm=["vectors-matrices-and-linear-maps", "finite-fields-and-the-field-f-2", "sets-subsets-and-cartesian-products"],
  salient="The net effect on the data banks does not depend on the initial values of the scratch wires, even though the scratch wires take part in the computation and are restored afterwards.")

S1_2 = show("S1.2",
  r"If every source, gate and sink $v$ gives each wire's array an invertible linear frame $D_v$, so that the stored array is $D_v$ applied to the logical array, then pointwise gates commute with the common frame and the network implements $D_{\rm out}\mathsf S D_{\rm in}^{-1}$, so that only the edge changes $D_vD_u^{-1}$ cost anything.",
  "Replace each scalar by an array, apply each gate pointwise at every address, and maintain the invariant that the stored array equals the frame applied to the logical array, along edges by construction and through gates by linearity.",
  expl("Once the scalar routing is fixed, the endpoint frames fix the array operator on each route, leaving the intermediate frames free to be chosen so that every edge change is cheap.",
       "intermediate frames can then be chosen to make each edge change inexpensive."),
  [infer("S1.2.1",
         r"At every vertex the stored array equals the frame $D_v$ applied to the logical array; at the sources this holds by defining the logical input to be $D_{\rm in}^{-1}f$, so no preliminary change of frame is needed.",
         "At a vertex $v$, the invariant is that the stored array equals $D_v$ applied",
         frm=["vectors-matrices-and-linear-maps"]),
   infer("S1.2.2",
         r"At a pointwise linear gate the common frame commutes with the gate, $G(D_vg_1,\ldots,D_vg_t)=D_vG(g_1,\ldots,g_t)$, so the invariant continues through the gate to the sinks.",
         "Thus the common frame commutes with the pointwise gate, and",
         frm=["vectors-matrices-and-linear-maps"]),
   infer("S1.2.3",
         r"When the scalar network is a signed role permutation $w\mapsto\rho(w)$, the route from input role $w$ applies $D_{{\rm sink}(\rho(w))}D_{{\rm source}(w)}^{-1}$ times its sign, auxiliary roles included.",
         "In particular, if the scalar network is a signed role permutation that",
         frm=["functions-bijections-and-permutations"])],
  page="frames",
  frm=["linear-network", "vectors-matrices-and-linear-maps", "arrays-records-and-matrix-transposition", "functions-bijections-and-permutations"])

S1_3 = show("S1.3",
  r"The bit network can be given nested nondegenerate subspace labels on its gates and terminals such that the endpoint matrices of every route differ by the identity $I_m$ and the total rank of all edge differences is $s<W m$.",
  "Label each wire's data by tensor products of the indicator lines of the three triples and their orthogonal complements; tabulate the orthogonal residual of every edge; observe that only the central wires lose dimension; and read off the rank sum, in which the source projections contribute $N$ extra ranks.",
  expl("The labels are chosen so that each change of frame costs only as much as the dimension of its orthogonal residual.",
       "choose its intermediate labels to make the changes of frame inexpensive."),
  [infer("S1.3.1",
         r"Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$, so the sum of absolute dimension changes is $W m-2N+2L$ with $L<N/2$.",
         "Every edge joins comparable nondegenerate labels.  The only decreasing",
         frm=["rank-basis-and-dimension", "inner-product-norm-and-orthonormal-basis"]),
   infer("S1.3.2",
         r"With the projections $P_U$ as matrices and a negated projection at each source $X_a$, the endpoint difference is $I_m$ on every route and the sum of the rational ranks of all edge differences is $s<W m$.",
         "The sum of the rational ranks of all edge differences is",
         frm=["rational-numbers-and-exact-fractions", "rank-basis-and-dimension"])],
  page="rank-deficit-labels",
  frm=["linear-network", "frames", "triple-subset-gadgets", "linear-algebra-orthogonality",
       "finite-fields-and-the-field-f-2", "rank-basis-and-dimension", "rational-numbers-and-exact-fractions",
       "inner-product-norm-and-orthonormal-basis", "sets-subsets-and-cartesian-products"],
  salient="Dimension never decreases on any edge except the central-wire edges from time 3 to time 4, and their total loss is less than half of $N$, which is exactly what pushes the rank sum strictly below $W m$.")

S1_4 = show("S1.4",
  r"For the complex network with binary labels, the phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{\operatorname{wt}(P_Ux)\bmod 4})H^{\otimes m}$ change along each edge by a product of translation kernels $aI+bX_v$, one per vector of an orthonormal basis of the edge residual, for $s<W m$ kernels in all, and telescope to $C^{\otimes m}$ on every role.",
  "Use that Hamming weight is additive modulo 4 on orthogonal binary vectors to turn each edge's phase change into one factor $i^{\\pm[v\\cdot x]}$ per basis vector, convert that factor into the kernel $aI+bX_v$ by conjugating with $H$, then telescope the frames along each route, repairing the one exceptional route $X_a\\to Y_a$ by conjugation with $Z$.",
  rec("All frames are diagonalized by the same matrix $H^{\\otimes m}$, so composing edges telescopes, and weight modulo 4 is the quadratic phase that makes orthogonal summands add."),
  [infer("S1.4.1",
         r"For orthogonal binary vectors the intersection of supports is even, so weight is additive modulo 4 and the phase difference of an edge is $\sum_v\operatorname{wt}(v)[v\cdot x]$ over an orthonormal basis of the residual, with every $\operatorname{wt}(v)$ odd.",
         "If $z\\cdot w=0$, the intersection cardinality is even, so weight is",
         frm=["finite-fields-and-the-field-f-2", "xor-bits"]),
   infer("S1.4.2",
         r"Since $i^{\varepsilon[v\cdot x]}=\frac{1+i^\varepsilon}{2}+\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}$ and $H\operatorname{diag}(1,-1)H=X$, each such factor becomes the translation kernel $aI+bX_v$ or its inverse.",
         "The identity $H\\operatorname{diag}(1,-1)H=X$, tensored over the",
         frm=["complex-numbers"]),
   infer("S1.4.3",
         r"Applying the common-frame identity with $D_v=\mathcal C_{U_v}$, an input role $w$ reaches output role $\rho(w)$ with its sign and the operator $\mathcal C_{U_{{\rm sink}(\rho(w))}}\mathcal C_{U_{{\rm source}(w)}}^{-1}$, which is $C^{\otimes m}$ for every pair with zero and full labels.",
         "Applying \\eqref{eq:common-frame-identity} with $D_v=\\mathcal C_{U_v}$,",
         frm=["frames"]),
   infer("S1.4.4",
         r"For the remaining pair $X_a\to Y_a$ the operator is $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u_a)$ and $C$ elsewhere, and the identity $C=iZC^{-1}Z$ with sign corrections before and after turns it into $C^{\otimes mk}$ as well.",
         "For the remaining pair, write $u=u_a$.  Its binary norm is one and",
         frm=["complex-numbers"])],
  page="phase-frames",
  frm=["rank-deficit-labels", "frames", "linear-network", "linear-algebra-orthogonality", "two-point-butterfly",
       "fixed-point-dyadics", "finite-fields-and-the-field-f-2", "xor-bits", "complex-numbers",
       "inner-product-norm-and-orthonormal-basis", "vectors-matrices-and-linear-maps"],
  salient="Every route, the auxiliary scratch roles included, ends with the same operator $C^{\\otimes m}$, and every edge change is built from copies of the same two-point kernel $aI+bX_v$.")

S1 = show("S1",
  r"There are two fixed linear networks of $W$ wires, one over bits and one over Gaussian dyadic numbers, each exchanging two banks of values with a sign while restoring every scratch wire, whose frames can be chosen so that the edge changes have total rank $s<W m$.",
  "Construct the scalar exchange network, lift it to arrays with frames, then attach nested subspace labels to its gates and terminals and count the dimension changes, once for bits and once for phases.",
  expl("Frames are chosen so that each edge can be carried out by smaller calls of the same procedure, and the decisive property is that there are fewer such calls than wires times the dimension.",
       "so that every edge can be implemented by smaller calls to the same"),
  [S1_1, S1_2, S1_3, S1_4],
  frm=["finite-fields-and-the-field-f-2", "vectors-matrices-and-linear-maps", "rank-basis-and-dimension"])

# ---------------------------------------------------------------- S2 interchange
S2_1_1 = show("S2.1.1",
  r"Every rational $m\times m$ matrix $A$ of rank $a$ equals $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ having exactly $a$ ones, at most one in each row and column.",
  "Eliminate by choosing the topmost nonzero row and its rightmost nonzero entry as pivot, clearing its row to the left and its column below with lower triangular elementary operations, deleting that row and column, and repeating on the active indices.",
  rec("The tape operations available in linear time are exactly the lower triangular ones, because a target field must follow its control fields, so the factors must be lower triangular."),
  [infer("S2.1.1.1",
         r"If $A=0$ take $E_1=E_2=I$ and $\Pi=0$; otherwise pick the pivot, clear to its left by right multiplication and below it by left multiplication with lower triangular elementary matrices, and scale it to one.",
         "If $A=0$, take $E_1=E_2=I$ and $\\Pi=0$.  Otherwise choose the topmost",
         frm=["gaussian-elimination"]),
   infer("S2.1.1.2",
         r"Deleting the pivot row and column and repeating leaves a partial permutation with exactly $a$ ones, since each step isolates a rank-one block.",
         "Delete the pivot row and column from the active index sets, retaining",
         frm=["rank-basis-and-dimension"])],
  page="lower-triangular-factorization",
  frm=["gaussian-elimination", "rank-basis-and-dimension", "vectors-matrices-and-linear-maps", "rational-numbers-and-exact-fractions"])

S2_1 = show("S2.1",
  r"For a rational $m\times m$ matrix $A$ of rank $a$, the address permutation $(H,D)\mapsto(H+AD,D)$ modulo $q^b$ costs exactly $a$ interchanges of pairs of $b$-digit fields plus $O(V)$ further work.",
  "Factor $A=E_1\\Pi E_2$, perform the lower triangular parts as controlled shifts in linear time, and realize each one of $\\Pi$ as a shear sandwiched around a single interchange of a field of $H$ with a field of $D$.",
  expl("Lower triangular changes of coordinates update a later field from earlier ones, which is the direction in which controlled shifts run in linear time.",
       "earlier fields in linear time.  Lower triangular changes of coordinates"),
  [S2_1_1,
   infer("S2.1.2",
         r"A lower triangular transformation of the vector of fields $H$ (or of $D$) costs $O(V)$, by updating the coordinates in descending physical order with controlled shifts and multiplications by units.",
         "A lower triangular transformation of $H$, or of $D$, costs $O(V)$:",
         frm=["controlled-shift"]),
   infer("S2.1.3",
         r"For $A=E_1\Pi E_2$, transform by $E_2$ and $E_1^{-1}$, add $\Pi D$ to $H$, and transform back; each one of $\Pi$ at $(i,j)$ gives $H_i\leftarrow H_i+D_j$ through $D_j\leftarrow D_j+H_i$, one interchange of $H_i$ and $D_j$, and $D_j\leftarrow H_i-D_j$.",
         "For $A=E_1\\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,",
         frm=["controlled-shift"])],
  page="matrix-shear",
  frm=["controlled-shift", "lower-triangular-factorization", "tape-streams", "modular-arithmetic-and-congruences", "rank-basis-and-dimension"])

S2_2 = show("S2.2",
  r"For $e=m^k$ digits and a row field divisible by $W^k$, interchanging two chunks of $e$ digits costs $O(V e^\tau)$, because the shear $H\leftarrow H+D$ is made of $s$ calls on $e/m$ digits, each on a role stream of volume $V/W$, and $s/W<m^\tau$ with $\tau<1$.",
  "Split the rows cyclically into $W$ role streams, run the network with address-shear frames so that each edge change becomes a smaller shear costing as many smaller interchanges as its rank, and solve the recurrence $F_k\\le(s/W)F_{k-1}+O(1)$ for the cost per unit volume by a geometric sum.",
  expl("Dividing cost by volume, each of the $s$ calls on $1/W$ of the volume contributes a factor $s/W$, so multiplying the parameter by $m$ increases the cost per volume by a factor less than $m$.",
       "After dividing cost by volume, multiplying the parameter by $m$"),
  [infer("S2.2.1",
         r"Splitting whole rows cyclically into $W$ role streams within each prefix gives streams of identical shape, each of logical volume $V/W$.",
         "Split whole rows cyclically into $W$ role streams within each prefix",
         frm=["tape-streams"]),
   infer("S2.2.2",
         r"Taking as the frame at a vertex of matrix $M$ the address permutation $\Phi_M:(H,D)\mapsto(H+MD,D)$, each edge applies $\Phi_{A_e}$ as a smaller shear, gates act pointwise, and the endpoint condition $M_{{\rm out}(\rho(w))}-M_{{\rm in}(w)}=I_m$ yields $H\leftarrow H+D$ on every row, scratch rows included.",
         "For a rational matrix $M$, let $\\Phi_M$ act on an array by moving its",
         frm=["frames", "rank-deficit-labels"]),
   infer("S2.2.3",
         r"The interchange of the two full chunks is $D\leftarrow D-H$, then $H\leftarrow H+D$, then $D\leftarrow H-D$; only the middle shear uses the network.",
         "To interchange the two full chunks, perform",
         frm=["tape-streams"]),
   infer("S2.2.4",
         r"The number of recursive calls is the sum of the edge ranks, exactly $s$, each on one role stream of volume $V/W$.",
         "The number of recursive calls is the sum of the edge ranks, exactly $s$.",
         frm=["rank-deficit-labels"]),
   infer("S2.2.5",
         r"With $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$ for $s/W<m^\tau$, the geometric sum gives $F_k=O(e^\tau)$.",
         "For $a=s/W<m^\\tau$ the geometric sum",
         frm=["divide-and-conquer-and-recurrences", "summation-and-product-notation"]),
   infer("S2.2.6",
         r"A fixed-tape depth-first schedule parks the inactive role streams on a stack, so each node pays only an additional $O(V)$ and the recursion needs a fixed number of tapes.",
         "Here we complete the implementation assertion used in",
         frm=["tape-streams"])],
  page="recursive-power-saving",
  frm=["rank-deficit-labels", "frames", "linear-network", "tape-streams", "divide-and-conquer-and-recurrences", "summation-and-product-notation"],
  salient="The inequality $s/W<m$ is strict, so the cost per volume grows like $m^\\tau$ with $\\tau<1$ rather than like $m$; a non-strict inequality would give only linear cost.")

S2_3 = show("S2.3",
  r"For arbitrary $u\ge1$ and arbitrary prefix, gap and suffix lengths, the interchange $(h,g,d)\mapsto(d,g,h)$ of two $u$-bit chunks of an array of volume $V$ costs $O(V u^\tau)$.",
  "Peel the top $\\rho=O(\\log u)$ digits off each chunk and exchange them one pair at a time so that they supply a row field of length divisible by $W^k$ (padding rows if needed), cover the remaining width by base-$m$ pieces handled by power-width calls, remove the padding, and handle binary widths by padding to a power of the prime $q$.",
  expl("Rows for a general array can be supplied by a few of its own high digits, and moving them costs less than the final bound.",
       "Rows for a general array can be supplied by a few of its own high digits."),
  [infer("S2.3.1",
         r"Writing each chunk as its top $\rho$ digits followed by the rest, exchanging the high digits one pair at a time and joining them produces a row field of length at least $W^k$ before both remaining chunks, at cost $O(V\rho)$.",
         "Write each chunk as its top $\\rho$ digits followed by its remaining",
         frm=["tape-streams", "logarithms-and-binary-logarithm"]),
   infer("S2.3.2",
         r"Writing the remaining width in base $m$ as $\sum_ja_jm^j$ with $a_j<m$ and applying a power-width call to each of the $a_j$ pieces of width $m^j$ costs $O(V)\sum_ja_jm^{j\tau}=O(V e^\tau)$.",
         "Write the remaining width in base $m$:",
         frm=["radix-representation-and-digits", "summation-and-product-notation"]),
   infer("S2.3.3",
         r"Binary chunks of $u$ bits are padded to $q^e$ with $e=O(u)$, which costs a fixed factor in volume, and the padded entries are scanned away after the interchange.",
         "Finally, for binary chunks let $e$ be the least integer with",
         frm=["binary-representation-of-integers"])],
  frm=["tape-streams", "matrix-shear", "recursive-power-saving", "lexicographic-order", "radix-representation-and-digits"])

S2 = show("S2",
  r"For a fixed $\tau<1$, two disjoint contiguous address chunks of $u$ bits in an array of volume $V$ can be interchanged in $O(V u^\tau)$ time on a fixed number of tapes, although the intermediate streams are XOR combinations of the data.",
  "Reduce the interchange to the shear $H\\leftarrow H+D$ of the two chunks, perform that shear with the bit network by calls on smaller chunks over role streams of volume $V/W$, solve the resulting recurrence, and then remove the restrictions on width and number of rows.",
  expl("A call at parameter $mf$ uses only $s$ calls at parameter $f$ on streams of volume $V/W$, and $s<W m$ is what makes the cost per volume grow slower than the parameter.",
       "A recursive call at parameter $mf$ therefore uses $s$ calls at parameter"),
  [S2_1, S2_2, S2_3],
  page="fast-chunk-interchange",
  frm=["tape-streams", "controlled-shift", "rank-deficit-labels", "frames", "linear-network", "matrix-shear",
       "recursive-power-saving", "xor-bits", "modular-arithmetic-and-congruences", "lexicographic-order",
       "arrays-records-and-matrix-transposition"],
  salient="The exponent $\\tau$ is strictly below 1 (indeed $\\tau=1-2^{-50}$), although a naive interchange of $u$ digits one at a time costs linear time in $u$ per bit.")

# ---------------------------------------------------------------- S3 butterfly layer
S3_4 = show("S3.4",
  r"Under the stated growth of the parameters, the selected-bit additions $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ at positions $j_i=\rho+i K$, $0\le i<f$, of two chunks of $L=f K$ bits can be performed, with a third chunk lent as temporary and restored, in time $O(V(L^\tau+1))$.",
  "Perform all additions at once as eight cyclic shifts of whole chunks by offsets read from control bits, which agree with the intended XORs except at addresses whose guard values lie within 20 of the segment boundary, a small explicit set, then repair exactly that set by extracting its records, sorting them by destination rank and reinserting them.",
  rec("A cyclic shift of a whole chunk costs linear time, and when the guard bits keep segments from carrying into each other it performs all the bit additions in parallel; only addresses with extreme guard values can fail."),
  [infer("S3.4.1",
         r"For a Boolean control $c$ and arbitrary integers $u,w$, eight conditional additions in the displayed order flip the parity of $u$ exactly when $c=1$ and restore the auxiliary integer $w$.",
         "For a Boolean control $c$ and arbitrary integers $u,w$, perform the following",
         frm=["modular-arithmetic-and-congruences", "xor-bits"]),
   infer("S3.4.2",
         r"The guard values fail the interval test only for a fraction $\delta_{\rm bad}\le80(f-1)2^{-K}$ of the addresses, and outside that set the packed shifts agree with the ideal XORs.",
         "There are exactly twenty excluded values for each guard in",
         frm=["binary-representation-of-integers"]),
   infer("S3.4.3",
         r"The exceptional addresses are extracted, given destination ranks, stably sorted by radix passes and reinserted, which implements the exact permutation everywhere in worst-case time.",
         "To implement the correction, scan the stream with a record-rank counter.",
         frm=["lexicographic-order", "functions-bijections-and-permutations"])],
  page="packed-selected-bit-addition",
  frm=["fast-chunk-interchange", "controlled-shift", "tape-streams", "xor-bits", "binary-representation-of-integers", "modular-arithmetic-and-congruences"])

S3 = show("S3",
  r"The map $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied at one common bit offset in each of $D\le d$ equal-width $K$-bit address chunks of an array of records, each a polynomial with $r$ complex coefficients on the grid $2^{-p}\mathbb Z[i]$, of total volume $V$, with a single final truncation, costs $O(V d^{\lambda'})$ for a fixed $\lambda'<1$.",
  "Rewrite $H_0^{\\otimes D}$ as phase-diagonal conjugates of $C^{\\otimes D}$, compute $C^{\\otimes e}$ on $e=mf$ selected bits with the complex network (each of the $s<W m$ calls acts on $f$ bits, and the binary changes of basis are packed selected-bit additions), unroll the resulting recurrence, and bound the exact intermediate dyadics so that one truncation suffices.",
  expl("The phase frames express a tensor power of the kernel $C$ through smaller groups of selected bits, separated by binary changes of basis, and the whole layer can then be evaluated exactly before one truncation.",
       "frames express a $C$ tensor product using smaller groups of"),
  [infer("S3.1",
         r"An invertible binary change of basis of fixed order $m$ is a product of at most $m(m-1)+3m$ row additions, each adding the selected bits $x_{h,j}\leftarrow x_{h,j}\oplus x_{h',j}$ of two slots of $f$ chunks.",
         "Gaussian elimination expresses any $M\\in\\operatorname{GL}(m,\\mathbb F_2)$",
         frm=["gaussian-elimination", "finite-fields-and-the-field-f-2"]),
   infer("S3.2",
         r"Applying the network with these column frames to a group of $e=mf$ selected axes gives exactly $s$ child calls on the $f$ axes of one slot and yields $C^{\otimes e}$ on every role, each inverse child coming from one forward call.",
         "Apply the finite network with these column frames to a group of",
         frm=["phase-frames", "rank-deficit-labels"]),
   infer("S3.3",
         r"Since $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$ with the diagonal phase operator $\mathcal S_D$, a layer of $H_0$ follows from a layer of $C$ exactly in Gaussian dyadics.",
         "For an address $x$ in a full layer, write $x_1,\\ldots,x_D$ for its",
         frm=["two-point-butterfly", "fixed-point-dyadics"]),
   S3_4,
   infer("S3.5",
         r"One $C$ kernel on one selected bit costs $O(V)$ by splitting on that bit and scanning aligned record pairs, so $e$ kernels cost $O(V e)$.",
         "To apply one \\(C\\) kernel, use the split from",
         frm=["fixed-point-dyadics", "tape-streams"]),
   infer("S3.6",
         r"At an internal node of $e=m^k$ active chunks, the $s$ recursive calls act on slots of $e/m$ chunks and the binary changes of basis, scalar gates and reassembly cost $O(V((e K)^\tau+1))$ at the node.",
         "First consider an internal node containing \\(e=m^k\\) consecutive",
         frm=["packed-selected-bit-addition", "recursive-power-saving"]),
   infer("S3.7",
         r"The first chunks supply a row index $u=Wg+w$; sending row $u$ to role $w$ gives each child exactly $1/W$ of the parent's volume while every row keeps its full polynomial suffix of $r$ coefficients.",
         "At a node, write a row index as \\(u=Wg+w\\), with \\(0\\le w<W\\),",
         frm=["tape-streams"]),
   infer("S3.8",
         r"The recurrence $F(e)\le(s/W)F(e/m)+O((e K)^\tau+1)$ for the cost per unit volume unrolls to $O(d^{\lambda'})$ for a fixed $\lambda'<1$, because $s/W<m$ strictly.",
         "Indeed, the \\(s\\) child calls are executed on streams of volume",
         frm=["recursive-power-saving", "divide-and-conquer-and-recurrences"]),
   infer("S3.9",
         r"The number of extra guard bits needed to keep every intermediate coefficient of one layer exact grows only like a fixed power of $d$, which is $o(p)$ for $d$ a small enough power of $p$, so coefficients keep width $O(p)$.",
         "For the complex network, let",
         frm=["fixed-point-dyadics"]),
   infer("S3.10",
         r"Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays and the final truncation $Q_p$ changes each coefficient by less than $\sqrt2\,2^{-p}$.",
         "Finally, every row of $\\mathcal H$ has",
         frm=["fixed-point-dyadics", "two-point-butterfly"])],
  page="simultaneous-butterfly-layer",
  frm=["phase-frames", "recursive-power-saving", "packed-selected-bit-addition", "fast-chunk-interchange",
       "fixed-point-dyadics", "two-point-butterfly", "ring-mod-y-r-plus-1", "tape-streams", "rank-deficit-labels",
       "complex-numbers", "polynomials"],
  salient="The exponent $\\lambda'$ is below 1, so applying the butterfly on $d$ chunks at once beats the $D$ whole-array passes that separate butterfly factors would need.")

# ---------------------------------------------------------------- S4 convolution over the ring
S4_1 = show("S4.1",
  r"Over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ with $\omega_t=y^{2r/t}$, the transform $F_t^-$ is computed by $\log_2 t$ levels of two-point butterflies $H_0$ and multiplications by powers of $y$, which are signed cyclic shifts of the $r$ coefficients; its output sits in bit-reversed order $B_tF_t^-$ and the reverse procedure computes $F_t^+B_t^{-1}$ from that order, so no reordering is needed.",
  "Run a radix-2 decimation-in-frequency fast Fourier transform in which every twiddle factor is a power of $y$, verify inversion through cancellation of character sums, keep the outputs in the order the recursion writes them, and group the axes into parallel rounds.",
  expl("Powers of $y$ serve as roots of unity, and multiplication by such a root is a signed shift of the coefficient list, so only butterflies remain as arithmetic.",
       "serve as roots of unity in the remaining axes, and multiplication by"),
  [infer("S4.1.1",
         r"Character sums cancel, $\sum_k\omega_t^{jk}=0$ when $t\nmid j$, so $F_t^+F_t^-=t^{-1}I$ even though the ring has zero divisors.",
         "If $j$ is an integer, then",
         frm=["roots-of-unity-and-euler-s-formula"]),
   infer("S4.1.2",
         r"Decimation in frequency pairs $z_k$ with $z_{k+t/2}$, applies $H_0$, multiplies the second output by $\omega_t^{-k}$, and recurses on the two halves.",
         "The length-one procedure is the identity.",
         frm=["two-point-butterfly", "fast-fourier-transform-and-fft-multiplication"]),
   infer("S4.1.3",
         r"After all rounds the named slots hold the frequency bits in reverse order, so the output is $B_tF_t^-$ without moving frequency indices, and the reverse recursion computes $F_t^+B_t^{-1}$.",
         "After all $a$ rounds, the named slots from high to low therefore",
         frm=["binary-representation-of-integers"]),
   infer("S4.1.4",
         r"For $D$ axes the individual steps group into one parallel butterfly $\mathcal H$ followed by one recordwise monomial $J_E$ whose exponent depends only on the address, and each round is a contraction.",
         "For $D$ axes of lengths $t_1,\\ldots,t_D$, put",
         frm=["multidimensional-transform"])],
  page="synthetic-transform",
  frm=["ring-mod-y-r-plus-1", "dft", "two-point-butterfly", "cyclic-convolution", "multidimensional-transform",
       "roots-of-unity-and-euler-s-formula", "fast-fourier-transform-and-fft-multiplication"],
  salient="Multiplying by a root of unity costs only a signed shift of coefficients, so the sole arithmetic left in each round is the two-point butterfly.")

S4_2 = show("S4.2",
  r"On a layout that places the selected bits of the $d-1$ participating axes at a common offset in consecutive $K$-bit chunks, the forward transform $L B F_{\boldsymbol t}^-$ and the opposite transform $F_{\boldsymbol t}^+B^{-1}L^{-1}$ each have error below $\sqrt2\,\ell\,2^{-p}$ and cost $O(T p[d K+p K^{\tau-1}+\ell d^{\lambda'}])$.",
  "Move the low-order bit slots of the axes to a prefix, exchange chunks so that chunk $j$ of every axis is consecutive, then run each round either as individual kernels on the prefix slots or as one simultaneous butterfly layer on the chunk groups, truncating once per round and keeping the frequency order.",
  expl("The simultaneous layer applies only when the selected bits of the participating axes sit at a common offset in consecutive chunks, so the arrangement must be built first.",
       "we must place the selected bits of the participating axes at a common"),
  [infer("S4.2.1",
         r"Moving the $O(d K)$ low-order bit slots to a prefix and exchanging at most $d q$ chunks of $K$ bits, with $q=\lfloor(\ell-1)/K\rfloor$, places chunk $j$ of all axes consecutively at cost $O(T p\,p K^{\tau-1})$.",
         "Form a list of the slots to move to a prefix.",
         frm=["fast-chunk-interchange"]),
   infer("S4.2.2",
         r"The rounds are processed from the highest named position down, so that all axes in a common round have equal current length, and each round on chunk groups is one call of the simultaneous layer costing $O(T p\,d^{\lambda'})$.",
         "First process the round at named position $h=\\ell-1$ on the long",
         frm=["simultaneous-butterfly-layer"]),
   infer("S4.2.3",
         r"Rounds on prefix slots process the participating bits individually, each in $O(T p)$ time, and there are at most $K$ of them, for a total $O(T p\,d K)$.",
         "In a round on prefix slots, process the participating bits individually.",
         frm=["fixed-point-dyadics"]),
   infer("S4.2.4",
         r"Since truncation is odd and $J_E$ is a signed coefficient permutation, $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$, so each round truncates once, and at most $\ell$ rounds give error below $\sqrt2\,\ell\,2^{-p}$.",
         "For a forward round on a group of $D$ chunks, the layer call returns",
         frm=["two-point-butterfly"]),
   infer("S4.2.5",
         r"The exact operators of the two procedures are $LB F_{\boldsymbol t}^-$ and $F_{\boldsymbol t}^+B^{-1}L^{-1}$, so the forward entry with frequency address $j$ is stored at $L(Bj)$.",
         "It remains to identify the order of the full procedures.",
         frm=["functions-bijections-and-permutations"])],
  page="synthetic-transform-layout",
  frm=["simultaneous-butterfly-layer", "synthetic-transform", "fast-chunk-interchange", "tape-streams",
       "ring-mod-y-r-plus-1", "multidimensional-transform", "fixed-point-dyadics"])

S4_3 = show("S4.3",
  r"Two disk-grid polynomials $f,g$ in $\mathcal R_r$ with $p$-bit components can be multiplied exactly and returned as $Q_p(fg/r)$ in time $O(r p\log(r p))$, by packing signed coefficients into big integers (Kronecker substitution) and calling an $O(N\log N)$ integer multiplier on four pairs.",
  "Evaluate the real and imaginary numerator polynomials at the base $B_0=2^{4p}$ with signed carries, multiply the four pairs of evaluation integers with the established integer multiplier, extract each product coefficient from its centered residue, and reduce modulo $y^r+1$ and truncate.",
  rec("A polynomial product is an integer product when the coefficients are packed in blocks wide enough that no coefficient of the product can spill into the next block."),
  [infer("S4.3.1",
         r"With base $B_0=2^{4p}$ the evaluation integers $A_u=u(B_0)$ of the numerator polynomials fit in $4pr$ bits, and four products of absolute values give $ac,be,ae,bc$ evaluated at $B_0$.",
         "Set $B_0=2^{4p}$",
         frm=["polynomials", "binary-representation-of-integers"]),
   infer("S4.3.2",
         r"Since every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<B_0/2$, centered residues with a carry in $\{0,1\}$ recover each coefficient exactly from the product integer.",
         "Now let $Z$ be one of the four signed product integers, and let $h$",
         frm=["modular-arithmetic-and-congruences", "schoolbook-multiplication-and-carries"]),
   infer("S4.3.3",
         r"The real and imaginary numerator streams are $ac-be$ and $ae+bc$; reduction modulo $y^r+1$ subtracts the coefficient at $j+r$ from the one at $j$.",
         "The real and imaginary numerator streams are respectively",
         frm=["complex-numbers"]),
   infer("S4.3.4",
         r"Shifting each numerator magnitude right by $p+\ell$ bits and restoring the sign yields $Q_p(fg/r)$ with error below $\sqrt2\,2^{-p}$.",
         "Finally the $p$-bit grid numerator of the normalized product is",
         frm=["floor-and-ceiling-functions"])],
  page="kronecker-packing",
  frm=["nlogn-multiplier", "ring-mod-y-r-plus-1", "polynomials", "complex-numbers", "binary-representation-of-integers"])

S4 = show("S4",
  r"On disk-grid arrays over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ indexed by a product of cyclic axes with $T$ coefficients in all and $M=T/r$ records, the normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ is approximated with error below $\sqrt2 M(3\ell+1)2^{-p}$ in time $O(T p[d K+p K^{\tau-1}+\ell d^{\lambda'}+\log(r p)])$, where $\ell=\log_2 r$.",
  "Compute the convolution as the scaled opposite transform of the pointwise product of two forward transforms kept in the same frequency order, evaluating the transforms by synthetic radix-2 layers on a layout where the simultaneous butterfly layers apply, and the pointwise polynomial products by signed packing into integer products.",
  expl("In a quotient where the required roots of unity act by exact signed permutations of coefficient lists, the Fourier transforms needed for convolution need only butterflies.",
       "where the required roots of unity act by exact signed permutations"),
  [S4_1, S4_2, S4_3,
   infer("S4.4",
         r"Both forward transforms are kept in their common order $LB$, the polynomial records are multiplied pointwise by signed packing, and the opposite procedure then consumes that order, followed by an exact scaling by $M$.",
         "Perform both forward transforms and retain their common $LB$ order.",
         frm=["synthetic-transform-layout", "kronecker-packing"]),
   infer("S4.5",
         r"Because $F_{\boldsymbol t}^-(f*g)=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)$ and $F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$, the scaled opposite transform of the pointwise product equals $(f*g)/(rM)$, and the common record permutation $LB$ cancels.",
         "To check normalization, expansion of the finite sums gives",
         frm=["cyclic-convolution"]),
   infer("S4.6",
         r"By bilinear contraction the three transform errors and the polynomial-product truncation add up to error below $\sqrt2 M(3\ell+1)2^{-p}$, and the cost is the sum of the transform costs, $M$ ring products and a linear scaling.",
         "For the error estimate, put",
         frm=["inner-product-norm-and-orthonormal-basis"])],
  page="synthetic-convolution",
  frm=["synthetic-transform", "synthetic-transform-layout", "kronecker-packing", "simultaneous-butterfly-layer",
       "ring-mod-y-r-plus-1", "dft", "cyclic-convolution", "multidimensional-transform", "fast-chunk-interchange",
       "nlogn-multiplier"],
  adds=[add("T", "total size", "The total number of polynomial coefficient-slots (records times record length) in a transform array, $T=rM$.", "count"),
        add("M", "record count", "The number of ring-valued records in an array, $M=T/r$.", "count"),
        add("\\ell", "log record length", "The base-2 logarithm of the record length, $\\ell=\\log_2 r$.", "direct")])

# ---------------------------------------------------------------- S5 resampling
S5_1 = show("S5.1",
  r"For coprime $s_i<t_i$ with $\theta=t_i/s_i-1>p/\alpha^4$, the Gaussian maps $\mathsf S,\mathsf T$ satisfy $\mathsf TP_{s_i}F_{s_i}=P_{t_i}F_{t_i}\mathsf S$ and $N=C\mathsf T\mathsf D$ is within $2^{-\alpha^2\theta}$ of the identity, which gives contractions $A,B_0$ with $P_{s_i}F_{s_i}=2^{2\alpha^2}B_0P_{t_i}F_{t_i}A$.",
  "Express the length-$s_i$ transform through Gaussian-weighted resampling onto a grid of length $t_i$, invert the near-identity selection $N$ by a Neumann series, and normalize the resulting maps so that both are contractions.",
  expl("Gaussian resampling connects the pairwise coprime lengths needed for the integer product to the powers of two used by the synthetic transforms.",
       "whereas the synthetic transforms use powers of two. Gaussian resampling"),
  [infer("S5.1.1",
         r"The Gaussian maps $\mathsf S,\mathsf T:\mathbb C^{s_i}\to\mathbb C^{t_i}$ are sums of Gaussians centred at the rescaled points $s_ik/t_i$ and $t_ij/s_i$, and $C$ selects the coordinates nearest $t_ij/s_i$.",
         "The Gaussian resampling argument uses two maps",
         frm=["complex-numbers", "floor-and-ceiling-functions"]),
   infer("S5.1.2",
         r"The diagonal map $\mathsf D$ cancels the Gaussian factor at the selected coordinate, so $N-I$ collects only the other summands, $\|N-I\|<2^{-\alpha^2\theta}$, and $N$ is invertible by a Neumann series.",
         "Set $N=C\\mathsf T\\mathsf D$. In $(Nu)_j$, the summand with index $j$",
         frm=["inner-product-norm-and-orthonormal-basis"]),
   infer("S5.1.3",
         r"Setting $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$ with $\mathsf J'=N^{-1}/2$ gives contractions with $B_0P_{t_i}F_{t_i}A=2^{-2\alpha^2}P_{s_i}F_{s_i}$.",
         "Now set $A=\\mathsf S'$ and $B_0=\\mathsf D'\\mathsf J'C$.",
         frm=["dft"]),
   infer("S5.1.4",
         r"The ordered numerical algorithms for the Gaussian maps run in time $O(t_ip^{3/2+\delta}\alpha)$ with errors below $p^2$, and $C$ is a linear scan selecting an ordered subsequence.",
         "Lemmas~4.8, 4.9 and 4.12 of",
         frm=["dft"])],
  page="gaussian-resampling",
  frm=["dft", "complex-numbers", "floor-and-ceiling-functions", "inner-product-norm-and-orthonormal-basis", "roots-of-unity-and-euler-s-formula"])

S5 = show("S5",
  r"For coprime $s_i<t_i$ with enough separation, the tensor Fourier transform $RF_{\boldsymbol s}$ together with its source permutation $R$ equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ for contractions $\mathcal A,\mathcal B_0$ computed line by line on a padded box of $T$ entries in time $O(d T p^{3/2+\delta}\alpha)$ plus axis movements $O(T p\,d^2(1+\ell^\tau))$, with both coordinate permutations left inside the formula.",
  "Use Gaussian resampling on each axis but keep the permutations $P_{s_i}$ and $P_{t_i}$ in the identity instead of sorting twice, tensor the one-dimensional identity over $d$ axes, and implement the expansion and compression line by line on the padded box, moving axes into the innermost position with chunk interchanges.",
  expl("The usual implementation of Gaussian resampling sorts twice on each coordinate; retaining both permutations in the transform formula avoids executing them.",
       "coordinate. We retain both permutations in the transform formula and"),
  [S5_1,
   infer("S5.2",
         r"Tensoring the one-dimensional identity over the $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$.",
         "Tensoring \\eqref{eq:no-sort-one-dimensional} proves",
         frm=["multidimensional-transform"]),
   infer("S5.3",
         r"Expanding the axes one at a time inside a padded box of $T$ entries and applying the line algorithms to valid lines only implements $\mathcal A$ and $\mathcal B_0$ with error below $d p^2$ and time $O(d T p^{3/2+\delta}\alpha)$.",
         "To implement $\\mathcal A$, first embed its",
         frm=["arrays-records-and-matrix-transposition"]),
   infer("S5.4",
         r"Exposing each axis as the innermost field needs $O(d^2)$ adjacent interchanges of $\ell$-bit or $(\ell-1)$-bit address fields, each costing $O(T p(1+\ell^\tau))$ by the chunk interchange.",
         "To move an axis past its neighbor, interchange their",
         frm=["fast-chunk-interchange"])],
  page="resampling-without-sorting",
  frm=["dft", "multidimensional-transform", "gaussian-resampling", "fast-chunk-interchange", "nlogn-multiplier",
       "arrays-records-and-matrix-transposition", "functions-bijections-and-permutations"],
  adds=[add("s_i", "source length", "The length of the source Fourier transform along axis $i$, a distinct odd prime.", "direct"),
        add("t_i", "target length", "The length of the power-of-two target transform along axis $i$, coprime to $s_i$ and slightly larger.", "direct"),
        add("\\alpha", "Gaussian width", "The width parameter of the Gaussian resampling maps.", "direct"),
        add("\\gamma", "scale exponent", "The exponent $\\gamma=2d\\alpha^2$ of the known scale $2^\\gamma$ relating the two sides of the identity.", "direct"),
        add("\\delta", "small exponent", "A fixed small exponent in the cost $p^{3/2+\\delta}$ of the Gaussian line maps.", "direct"),
        add("T", "padded size", "The number of entries of the padded box, the product of the target lengths.", "count"),
        add("\\ell", "log axis length", "The base-2 logarithm of the largest axis length.", "direct")],
  salient="The permutations $P_s$ and $P_t$ are never executed: they stay inside the transform identity, and the later chirp step absorbs the target one while the source one cancels.")

# ---------------------------------------------------------------- S6 Bluestein
S6 = show("S6",
  r"For even $t_i$, the permuted transform satisfies $QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}{T}$ with the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$, and the source permutation cancels, $(RF^+_{\boldsymbol s})[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$ with $S=\prod_i s_i$.",
  "Complete the square in the phase so that the transform with its frequency permutation becomes a pointwise chirp multiplication, a cyclic convolution with the chirp and another chirp multiplication; then show the source permutation cancels using that a unit dilation commutes with the transform up to inversion and with pointwise products.",
  expl("The chirp identity performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array.",
       "in $Q$ without applying $Q$ as a separate permutation of the array."),
  [infer("S6.1",
         r"The chirp has period $t_i$ in coordinate $i$, and the coefficient of $u_{\boldsymbol k}$ on the right is $\frac1T\exp(2\pi i\sum_is_ij_ik_i/t_i)$, which is exactly the coefficient of $QF_{\boldsymbol t}$.",
         "Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by",
         frm=["roots-of-unity-and-euler-s-formula", "modular-arithmetic-and-congruences"]),
   infer("S6.2",
         r"For a unit $c$ modulo $q$ the dilation $R_c$ satisfies $F_q^+R_c=R_c^{-1}F_q^+$, so $RF^+_{\boldsymbol s}R=F^+_{\boldsymbol s}$, and a coordinate permutation commutes with pointwise products.",
         "For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$. Substituting $h=ck$",
         frm=["primes-divisibility-and-coprimality", "functions-bijections-and-permutations"]),
   infer("S6.3",
         r"With the normalized convolution rule $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$ and $F^+_{\boldsymbol s}F_{\boldsymbol s}=I/S$, the retained permutation cancels and the result is $(u*v)/S^2$.",
         "The normalized convolution rule is",
         frm=["cyclic-convolution"])],
  page="bluestein-chirp",
  frm=["dft", "cyclic-convolution", "multidimensional-transform", "resampling-without-sorting",
       "roots-of-unity-and-euler-s-formula", "modular-arithmetic-and-congruences",
       "primes-divisibility-and-coprimality", "functions-bijections-and-permutations"],
  salient="Because the source permutation commutes with pointwise products and conjugates the opposite transform into itself, it cancels across the two forward transforms, their product and the opposite transform, and so is never executed.")

# ---------------------------------------------------------------- S7 assembly
S7_1 = show("S7.1",
  r"With fixed rational exponents $\tau=\sigma=1-2^{-50}$, $\epsilon=2^{-75}$, $\kappa=2^{-182}$ and sizes $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$ and $r=2^{\lceil\log_2T/d\rceil}$, every layer and resampling hypothesis holds, $T p=\Theta(n)$, every cost term is a power of $p$ below one, and there are distinct odd primes $s_i$ just below the axis lengths $t_i\in\{r/2,r\}$ with $T/2<S<T$ for $S=\prod_i s_i$.",
  "Fix explicit rational exponents so that every inequality required by the earlier propositions holds with room to spare, derive all sizes from the input length $n$, and obtain the prime source lengths from a prime-counting estimate on intervals just below each $t_i$.",
  expl("The prime source lengths must be close enough to the powers of two for their product to fill a fixed fraction of the box and for each ratio to leave enough separation for resampling.",
       "The distinct prime lengths $s_i$ must be close to the powers of two"),
  [infer("S7.1.1",
         r"The exponents $\tau,\sigma,\beta,\delta,\lambda,c,\lambda',C_1,\epsilon,\kappa$ are fixed rational numbers satisfying every layer condition with room to spare.",
         "Take the following fixed rational numbers:",
         frm=["rational-numbers-and-exact-fractions"]),
   infer("S7.1.2",
         r"Taking $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$ and a power of two $T\in[4n/b,8n/b)$ gives $T p=\Theta(n)$ and $d$ axes of lengths $t_i\in\{r/2,r\}$ with product $T$.",
         "Take the power of two $T$ in $[4n/b,8n/b)$, and let",
         frm=["floor-and-ceiling-functions", "logarithms-and-binary-logarithm"]),
   infer("S7.1.3",
         r"The interval $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes, so distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ exist, giving $T/2<S<T$ and enough separation for resampling.",
         "contains at least $\\eta x/(2\\log x)$ primes.",
         frm=["primes-divisibility-and-coprimality"]),
   infer("S7.1.4",
         r"Writing the inputs as polynomials in $2^b$ with $\lceil n/b\rceil$ digits, the product has degree below $S$, so convolution modulo $x^S-1$ has no wraparound and every product coefficient is below $2^{3b}$.",
         "Write the two inputs as polynomials in $2^b$, each with",
         frm=["radix-representation-and-digits", "multiplication-as-convolution"])],
  page="parameter-choice",
  frm=["simultaneous-butterfly-layer", "synthetic-convolution", "resampling-without-sorting", "bluestein-chirp",
       "fast-chunk-interchange", "floor-and-ceiling-functions", "logarithms-and-binary-logarithm",
       "primes-divisibility-and-coprimality", "radix-representation-and-digits"],
  salient="The smallest of the margins by which the dominant cost exponents fall below one is exactly $2^{-181}=2\\kappa$, which is where $\\kappa=2^{-182}$ comes from.")

S7_2 = show("S7.2",
  r"With $P_i=\prod_{j<i}s_j$ and $\mu_i=P_i^{-1}\bmod s_i$, the map $\Phi:x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\ldots,x_d]/(x_i^{s_i}-1)$ that turns cyclic convolution of length $S$ into convolution on the product of cyclic axes, and it and its inverse are implemented by triangular controlled shifts in time $O(T p\,d^2(1+\ell^\tau))$.",
  "Apply the Chinese remainder theorem to the exponents, so that each new axis coordinate depends only on lower-index digits and the change of order is a sequence of prefix-controlled cyclic shifts after reordering the axes by chunk interchanges.",
  expl("The map is chosen with coordinate powers that make the change of order a sequence of controlled cyclic shifts.",
       "algebraic split, with coordinate powers that make the change of order a"),
  [infer("S7.2.1",
         r"The assignment $x\mapsto\prod_ix_i^{\mu_i}$ respects $x^S=1$ and its image has order $S$, so it is an isomorphism preserving cyclic convolution.",
         "respects $x^S=1$, so it defines an algebra map.",
         frm=["primes-divisibility-and-coprimality", "modular-arithmetic-and-congruences"]),
   infer("S7.2.2",
         r"Each index $k=\sum_ja_jP_j$ has axis coordinates $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, which depend only on lower-index digits, so the change is triangular.",
         "Every ordinary coefficient index has a unique mixed-radix expression",
         frm=["integer-division-with-remainder"]),
   infer("S7.2.3",
         r"After reordering the axes so that lower indices come first, updating targets $i=d,\ldots,1$ uses the original digits as controls, zero padding stays zero, and an explicit inverse exists.",
         "Now reorder the complete padded axes to $(a_1,\\ldots,a_d)$.  In this",
         frm=["controlled-shift"]),
   infer("S7.2.4",
         r"Each triangular update is a prefix-controlled cyclic shift of linear cost, and reordering the axes needs $O(d^2)$ chunk interchanges of $\ell$-bit or $(\ell-1)$-bit fields, for a total $O(T p\,d^2(1+\ell^\tau))$.",
         "The axis widths are $\\ell$ or $\\ell-1$.  To exchange two adjacent axes",
         frm=["fast-chunk-interchange"])],
  page="crt-address-map",
  frm=["controlled-shift", "fast-chunk-interchange", "cyclic-convolution", "multidimensional-transform",
       "multiplication-as-convolution", "parameter-choice", "modular-arithmetic-and-congruences",
       "primes-divisibility-and-coprimality"],
  salient="The coordinate change is triangular, because axis $i$ depends only on lower-index digits, so every update is a controlled shift and no general transpose is needed.")

S7_3 = show("S7.3",
  r"The map $\Theta:x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ is a norm-preserving algebra isomorphism from $\mathbb C[x_d]/(x_d^r-1)$ onto $\mathbb C[y]/(y^r+1)$, diagonal in the coefficient bases, so a cyclic wrap on the last axis becomes a negacyclic wrap and back.",
  "Define the map by $x_d\\mapsto\\zeta y$, check it is well defined because $(\\zeta y)^r=1$, observe that it multiplies coefficient $k$ by $\\zeta^k$, and verify the wrap by computing the factor of a product term.",
  expl("The power-of-two complex convolution needed in the chirp identity is obtained from the synthetic convolution by a coefficient twist.",
       "obtained from the synthetic convolution by a coefficient twist."),
  [infer("S7.3.1",
         r"The map is well defined because $(\zeta y)^r=(-1)(-1)=1$, and it is diagonal in the bases $(x_d^k)$ and $(y^k)$, multiplying coefficient $k$ by the nonzero number $\zeta^k$, so it is an isomorphism preserving the sup norm.",
         "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.  On the bases",
         frm=["complex-numbers", "roots-of-unity-and-euler-s-formula"]),
   infer("S7.3.2",
         r"For $k+l=j+hr$ with $h\in\{0,1\}$ a product term acquires the factor $\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
         "For an explicit check on the wrap, write $k+l=j+hr$, where",
         frm=["polynomials"])],
  page="phase-twist",
  frm=["ring-mod-y-r-plus-1", "cyclic-convolution", "complex-numbers", "roots-of-unity-and-euler-s-formula", "polynomials"],
  salient="The twist factor $\\zeta^k$ makes the sign $(-1)^h$ of the negacyclic wrap cancel exactly against $\\zeta^{rh}=(-1)^h$.")

S7_8 = show("S7.8",
  r"Every computed step approximates a contraction with bounded error and every scaling is known, so the recovered coefficients lie within error less than $1/2$ of the true integers, rounding to the nearest integer gives them exactly, and carry propagation gives the exact $2n$-bit product.",
  "Measure errors in units of $2^{-p}$, bound each computed step against its exact counterpart by inserting the exact map at the computed input, accumulate through the pipeline while keeping all norms inside the disk with margins, then multiply by the known scales and compare with $1/2$.",
  expl("Composing approximations adds their errors, provided at each step the exact contraction is inserted at the computed input.",
       "adds their errors: at each step, insert the exact map at the computed"),
  [infer("S7.8.1",
         r"A linear contraction propagates an input error without increasing it, and for a bilinear contraction with all operands in the disk the two operand errors add.",
         "A linear contraction propagates an input error without increasing it.",
         frm=["inner-product-norm-and-orthonormal-basis"]),
   infer("S7.8.2",
         r"The normalized ring convolution has error less than $5TL2^{-p}$ with $L=\log_2T$, the chirp transform less than $8TL2^{-p}$, and the source transform less than $9\cdot2^\gamma TL\,2^{-p}$ while keeping norm below $.501$.",
         "For disk-grid ring arrays $f,g$, put $M=T/r$.  Two normalized synthetic",
         frm=["dft"]),
   infer("S7.8.3",
         r"The computed opposite transform of the truncated product of the two forward transforms differs from the exact value $(u*v)/S^2$ by less than $(3E_s+2)2^{-p}$.",
         "Let $G:=RF_{\\boldsymbol s}^+$ be the exact opposite contraction.",
         frm=["dft"]),
   infer("S7.8.4",
         r"After the two exact scalings by $S$ and $2^{2b+4}S$ the final absolute error is below $448b\,2^{-3b/4}<1/2$.",
         "Since $S\\le T<2^b$ and $L<b$ eventually, the final absolute error is less than",
         frm=["logarithms-and-binary-logarithm"]),
   infer("S7.8.5",
         r"The true coefficients are integers in $[0,2^{3b})$, so the nearest integer to the represented value is the unique correct coefficient.",
         "The true coefficients are real integers.  If $H_j$ is the real",
         frm=["integer-division-with-remainder"]),
   infer("S7.8.6",
         r"Propagating radix-$2^b$ carries from the least significant coefficient keeps $0\le k_j<Q_0^2$ and the invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$, giving the exact product bits.",
         "To propagate carries, let $Q_0=2^b$.",
         frm=["schoolbook-multiplication-and-carries", "mathematical-induction-and-proof-by-cases"])],
  page="error-and-exact-recovery",
  frm=["dft", "inner-product-norm-and-orthonormal-basis", "roots-of-unity-and-euler-s-formula",
       "schoolbook-multiplication-and-carries", "radix-representation-and-digits", "integer-division-with-remainder"])

S7 = show("S7",
  r"The procedure that extracts radix-$2^b$ digits, applies the Chinese-remainder address map $\Phi$, computes two forward source transforms, a pointwise product and the opposite transform with exact rescalings, rounds, and propagates carries outputs the exact $2n$-bit product.",
  "Choose the parameters, place the digits on a product of distinct prime cyclic axes by the Chinese-remainder map, compute the cyclic convolution through resampled transforms in which the middle transform is a chirp convolution evaluated over the polynomial ring after a phase twist, undo the known normalizations, bound the error below $1/2$, round, and propagate carries.",
  expl("The remaining proof places the fast tape procedures inside the multiplication reduction and accounts for every change of representation.",
       "The remaining proof places these procedures inside the multiplication"),
  [S7_1, S7_2, S7_3,
   infer("S7.4",
         r"Normalized complex cyclic convolution on the power-of-two axes is $D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$, obtained from the ring convolution with twists applied linewise.",
         "The linewise extension of $\\Theta$ is $\\iota D_+$, with inverse",
         frm=["synthetic-convolution", "phase-twist"]),
   infer("S7.5",
         r"The chirp transform $\overline{\widetilde a}\cdot\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,\overline{\widetilde a}\cdot x)$ evaluates $QF_{\boldsymbol t}x$ by a chirp multiplication, a complex convolution with the chirp kernel and a second chirp multiplication.",
         "$x$ of norm at most $.6$, the computed chirp transform forms the arrays",
         frm=["bluestein-chirp", "synthetic-convolution"]),
   infer("S7.6",
         r"The source transform applies the Gaussian expansion $\mathcal A$, the chirp transform, the Gaussian compression $\mathcal B_0$ and an exact scaling by $2^\gamma$, and has exact counterpart $RF_{\boldsymbol s}$.",
         "For a source disk-grid tensor of norm at most $.5$, write",
         frm=["resampling-without-sorting", "gaussian-resampling"]),
   infer("S7.7",
         r"The procedure applies $\Phi$, two source transforms, a pointwise product truncated to $p$ fractional bits, the opposite source transform scaled by $S$, a second scaling by $2^{2b+4}S$, rounding, $\Phi^{-1}$ and carry propagation, and outputs exactly $2n$ bits.",
         "With these streams prepared, perform the following operations.",
         frm=["crt-address-map", "parameter-choice"]),
   infer("S7.7b",
         r"By the permutation-cancellation identity the exact result of the three transforms is $(u*v)/S^2$, so the first scale by $S$ gives $(u*v)/S$ and the second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the integer coefficient convolution.",
         "The two occurrences of $S$ in this algorithm undo different",
         frm=["bluestein-chirp"]),
   S7_8],
  page="multiplication-algorithm",
  frm=["multiplication-as-convolution", "cyclic-convolution", "nlogn-multiplier", "dft", "synthetic-convolution",
       "resampling-without-sorting", "bluestein-chirp", "parameter-choice", "crt-address-map", "phase-twist",
       "error-and-exact-recovery", "schoolbook-multiplication-and-carries", "radix-representation-and-digits"],
  adds=[add("b", "digit width", "The number of bits in each radix digit of the inputs, about $\\log_2 n$.", "count"),
        add("S", "prime product", "The product $S=\\prod_i s_i$ of the distinct prime source lengths, the length of the cyclic convolution.", "direct"),
        add("s_i", "source length", "The distinct odd prime length of the source transform along axis $i$.", "direct"),
        add("t_i", "target length", "The power-of-two length $r/2$ or $r$ of axis $i$ in the padded box.", "direct"),
        add("T", "padded size", "The number of entries of the padded box, a power of two with $T p=\\Theta(n)$.", "count"),
        add("\\ell", "log axis length", "The base-2 logarithm of the longest axis length $r$.", "direct"),
        add("\\gamma", "scale exponent", "The exponent of the known power-of-two scale applied after each source transform.", "direct")])

# ---------------------------------------------------------------- S8 tally
S8 = show("S8",
  r"Divided by $V=T p$, every cost term is $p$ to a power at most $1-2\kappa$, setup and exceptional repairs are $o(V)$, and powers of $\log p$ are absorbed, so the single fixed machine runs in time $O(n(\lg n)^{1-\kappa})$.",
  "Tabulate the normalized cost of every operation, check the seven dominant exponents against explicit margins, and show that setup, prime search and exceptional-address repairs are negligible.",
  expl("The explicit slack between the smallest margin and $\\kappa$ covers any remaining fixed power of $\\log p$.",
       "This explicit slack will cover"),
  [infer("S8.1",
         r"Costs are tabulated after division by $V=T p=\Theta(n)$ with a fixed number of repeated transforms and convolutions absorbed into constants.",
         "For the cost calculation put $V=Tp=\\Theta(n)$.",
         frm=["big-o"]),
   infer("S8.2",
         r"Direct substitution gives the seven margins below one, the smallest being $2^{-181}=2\kappa$.",
         "Direct substitution gives",
         frm=["asymptotic-notation-beyond-big-o"]),
   infer("S8.3",
         r"Setup at recursion nodes, prime search and the compact exceptional streams of the packed changes of basis all cost $o(V)$ deterministically.",
         "We next separate setup at recursion nodes from work repeated for every",
         frm=["packed-selected-bit-addition"]),
   infer("S8.4",
         r"Each of the seven displayed powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the total is $O(T p\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
         "Each of the seven displayed powers is at most $1-2\\kappa$ by",
         frm=["logarithms-and-binary-logarithm"]),
   infer("S8.5",
         r"Using schoolbook multiplication below a fixed cutoff, the single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and outputs exactly the $2n$-bit product.",
         "With $\\lg n=\\max\\{\\lceil\\log_2n\\rceil,1\\}$, the resulting single",
         frm=["schoolbook-multiplication-and-carries", "turing-machine-running-time-and-model-conventions"])],
  frm=["parameter-choice", "synthetic-convolution", "resampling-without-sorting", "crt-address-map",
       "simultaneous-butterfly-layer", "fast-chunk-interchange", "big-o", "logarithms-and-binary-logarithm"])

# ---------------------------------------------------------------- root
S0 = show("S0",
  r"A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.",
  "Reduce the product to a convolution over a polynomial ring computed by Fourier-type transforms; supply the two fast tape procedures that remove the logarithmic factor from address movement and from butterfly arithmetic, both obtained from linear networks that save a power; then assemble the algorithm and tally every cost.",
  expl("Scanning the data once per transform level already costs $n\\log n$, so the logarithmic factor can only be reduced by savings in both data movement and arithmetic.",
       "We therefore need savings in both movement and arithmetic."),
  [S1, S2, S3, S4, S5, S6, S7, S8],
  page="main-theorem",
  frm=["nlogn-conjecture", "multiplication-as-convolution", "fast-fourier-transform-and-fft-multiplication",
       "big-o", "multitape-turing-machine", "turing-machine-running-time-and-model-conventions",
       "logarithms-and-binary-logarithm", "asymptotic-notation-beyond-big-o"],
  adds=[add("V", "logical volume", "The number of stored data bits of the array being processed.", "count"),
        add("\\tau", "interchange exponent", "The fixed exponent below one in the cost $O(V u^\\tau)$ of interchanging address chunks.", "direct"),
        add("\\lambda'", "layer exponent", "The fixed exponent below one in the cost $O(V d^{\\lambda'})$ of a simultaneous butterfly layer.", "direct"),
        add("W", "wire count", "The number of wires of a fixed linear network, scratch wires included.", "count"),
        add("m", "label dimension", "The dimension of the fixed space of subspace labels, equal to the number of digit fields in a chunk vector.", "count"),
        add("s", "call count", "The total number of smaller calls an edge-by-edge implementation of the network needs, the sum of the ranks of its edge changes.", "count"),
        add("p", "precision", "The number of fractional bits of the fixed-point coefficients.", "count"),
        add("d", "axis count", "The number of axes (address chunks) acted on together.", "count"),
        add("K", "chunk width", "The number of bits in each address chunk.", "count"),
        add("r", "record length", "The number of complex coefficients in a polynomial record.", "count")])

answer = {"root": S0}
open('/home/user/openai-nlogn-wiki/runs/G2/exegenius/tasks/0003-argument.answer.json', 'w', encoding='utf-8').write(
    json.dumps(answer, indent=1, ensure_ascii=False))

# ------------------------------------------------------------ self-checks
PAGES = """nlogn-conjecture linear-network frames tape-streams fixed-point-dyadics controlled-shift linear-algebra-orthogonality triple-subset-gadgets rank-deficit-labels recursive-power-saving lower-triangular-factorization matrix-shear fast-chunk-interchange packed-selected-bit-addition ring-mod-y-r-plus-1 dft two-point-butterfly cyclic-convolution multiplication-as-convolution multidimensional-transform synthetic-transform gaussian-resampling error-and-exact-recovery phase-twist nlogn-multiplier phase-frames simultaneous-butterfly-layer synthetic-transform-layout kronecker-packing synthetic-convolution resampling-without-sorting bluestein-chirp parameter-choice crt-address-map multiplication-algorithm main-theorem""".split()
KNOWN = """big-o polynomials complex-numbers multitape-turing-machine xor-bits asymptotic-notation-beyond-big-o logarithms-and-binary-logarithm floor-and-ceiling-functions binary-representation-of-integers radix-representation-and-digits schoolbook-multiplication-and-carries divide-and-conquer-and-recurrences fast-fourier-transform-and-fft-multiplication mathematical-induction-and-proof-by-cases sets-subsets-and-cartesian-products functions-bijections-and-permutations modular-arithmetic-and-congruences primes-divisibility-and-coprimality rational-numbers-and-exact-fractions finite-fields-and-the-field-f-2 vectors-matrices-and-linear-maps rank-basis-and-dimension gaussian-elimination inner-product-norm-and-orthonormal-basis roots-of-unity-and-euler-s-formula summation-and-product-notation newton-s-method integer-division-with-remainder lexicographic-order arrays-records-and-matrix-transposition turing-machine-running-time-and-model-conventions""".split()
idx = {p: i for i, p in enumerate(PAGES)}
errors = []
ids = set(); used_pages = []; froms = set()
pos = -1
def walk(n, anc_page, path_adds):
    global pos
    if n["id"] in ids: errors.append("dup id " + n["id"])
    ids.add(n["id"])
    pg = n.get("page") or anc_page
    if n.get("page"):
        used_pages.append(n["page"])
        if n["page"] not in idx: errors.append("bad page " + n["page"])
    for f in n.get("from", []):
        froms.add(f)
        if f in idx:
            if idx[f] >= idx[pg]: errors.append(f"{n['id']}: from {f} not before page {pg}")
        elif f not in KNOWN: errors.append(f"{n['id']}: unknown from {f}")
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        if "\n" in q: errors.append("multiline quote " + n["id"])
        if n.get("deferred"):
            if q not in SRC: errors.append(f"{n['id']}: quote missing")
        else:
            i = SRC.find(q, pos + 1)
            if i < 0:
                j = SRC.find(q)
                errors.append(f"{n['id']}: quote {'out of order (first at %d, pos %d)'%(j,pos) if j>=0 else 'MISSING'}: {q[:50]}")
            else:
                pos = i
        if n.get("children"): errors.append("infer with children " + n["id"])
    else:
        m = n.get("motivation")
        if not m or not n.get("method"): errors.append("show lacks method/motivation " + n["id"])
        if m and m["source"] == "explicit":
            if not m.get("quote") or m["quote"]["quote"] not in SRC: errors.append("motivation quote missing " + n["id"] + ": " + (m["quote"]["quote"] if m.get("quote") else ""))
        if not n.get("children"): errors.append("show without children " + n["id"])
        for c in n["children"]:
            walk(c, pg, path_adds)
    # adds occurrence
    for a in n.get("adds", []):
        sym = a["symbol"]
        found = False
        def desc(x):
            for c in x.get("children", []) or []:
                yield c
                yield from desc(c)
        for d in desc(n):
            for mm in re.findall(r"\$(.+?)\$", d["claim"], flags=re.S):
                if re.search(r"(?<![A-Za-z\\])" + re.escape(sym) + r"(?![A-Za-z])", mm):
                    found = True
        if not found: errors.append(f"{n['id']}: add symbol {sym} not found below")
walk(S0, None, [])
for p in PAGES:
    if p not in used_pages and p not in froms: errors.append("page unused: " + p)
if len(set(used_pages)) != len(used_pages): errors.append("page used twice")
print("\n".join(errors) if errors else "self-check OK")
