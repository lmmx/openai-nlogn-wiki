#!/usr/bin/env python3
import json, re, sys

SRC = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E9F8Y/sources/paper.tex').read()

def ev(q):
    return {"source": "paper", "quote": q}

def mot(text, src, quote=None):
    d = {"text": text, "source": src}
    d["quote"] = ev(quote) if quote else None
    return d

def B(symbol, name, meaning, rel="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": rel}

def infer(id, claim, quote, page=None, frm=None, deferred=False, salient=None):
    d = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote)}
    if page: d["page"] = page
    if frm: d["from"] = frm
    if deferred: d["deferred"] = True
    if salient: d["salient"] = salient
    return d

def show(id, claim, method, motivation, children, page=None, frm=None, adds=None, salient=None):
    d = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children}
    if page: d["page"] = page
    if frm: d["from"] = frm
    if adds: d["adds"] = adds
    if salient: d["salient"] = salient
    return d

# ---------------------------------------------------------------- S1
S1 = show(
 "S1",
 r"On a fixed number of tapes, arrays stored in lexicographic order admit digit moves, splits, row splitting and controlled cyclic shifts of a target field in $O(V)$ time, where $V$ is the logical bit volume.",
 "State the elementary scans once, with counters, rewinds and cleanup charged, then build the controlled cyclic shift of a target field out of one split and one merge, and count every later procedure in units of one such scan.",
 mot("Every later procedure (interchange, butterfly layer, CRT map) is assembled from these scans, so their linear cost is the unit in which all later bounds are stated; the machine model has to be pinned down before any saving can be measured.", "recoverable"),
 [
  infer("S1.1",
   r"For a fixed radix $q$, permuting the digit values at two positions, moving one digit, splitting on a digit with a fixed pointwise map and merging back, and splitting whole rows cyclically into $W$ streams of volume $V/W$ (and merging them) each take $O(V)$ steps on a fixed number of tapes.",
   r"takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
   page="tape-address-model",
   frm=["multitape-turing-machine","multidimensional-arrays-and-row-major-order","binary-numerals-and-bit-strings","positional-notation-in-any-radix"]),
  infer("S1.2",
   r"A target field $y\in[Q]$, $Q=q^b$, that follows its control fields can be updated by $y\mapsto y+a(\text{controls}) \pmod Q$ in $O(V)$ time by splitting each fibre at $Q-a$ and merging the two pieces in the opposite order; multiplication by a fixed rational unit is likewise $O(V)$.",
   r"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the"),
 ],
 page="controlled-cyclic-shift",
 frm=["tape-address-model","modular-arithmetic","cyclic-shifts-and-rotations-of-lists","primes-coprimality-and-gcd"],
)

# ---------------------------------------------------------------- S2.1 scratch-restoring exchange
S21 = show(
 "S2.1",
 r"With $h=100$, $v=\binom h3=161700$, $N=v^3=4227952113000000$ and $I=3v^2=78440670000$ invocations, three stages of forward invocations $y_S\mapsto y_S+x_S$ send $(X_a,Y_a)\mapsto(-Y_a,X_a)$ (a plain swap over $\mathbb F_2$) and return every scratch wire to its arbitrary initial value; the bit network has $W_{\rm b}=177176569091445000000$ wires and the complex network $W_{\rm c}=1873807244643542670000$.",
 "Write the net effect of an eight-row gate schedule as a fixed matrix times the source bank; make the first rows subtract exactly what the later rows re-add from the same scratch contents, and choose the side-injection and scatter coefficients so that the net matrix is the identity.",
 mot("A scratch wire holds an arbitrary value (on tape it will be a row of other data), so the exchange must not depend on it; subtracting the old scratch effect first, using the wires, and then undoing the loading makes the net change independent of that value (the transparent-computation trick).", "recoverable"),
 [
  infer("S2.1.0",
   r"Fix $h=100$, $v=\binom h3=161700$, $N=v^3$, $m=h^3=1000000$; the data banks $X_a,Y_a$ are indexed by $a\in\mathcal T^3$ where $\mathcal T$ is the set of three-element subsets of $[h]$, and each of the three stages runs $v^2$ separate invocations, $I=3v^2$ in all, each with its own scratch wires.",
   r"h=100,\qquad v=\binom h3=161700,\qquad"),
  infer("S2.1.1",
   r"Bit construction: scalars lie in $\mathbb F_2$, triples $S,T$ are neighbours when $|S\cap T|=1$; copy adds $x_T$ to the side wire $A_{ST}$, side injection adds $\sum_{T:|S\cap T|=1}A_{ST}$ to $y_S$, gather adds $\sum_{T\ni i}x_T$ to a central wire $C_i$ and scatter adds $\sum_{i\in S}C_i$ to $y_S$.",
   r"$S,T$ are neighbors when $|S\cap T|=1$."),
  infer("S2.1.2",
   r"Complex construction: scalars lie in $\mathbb Z[i,1/2]$, neighbours are distinct triples with even intersection, side injection adds $-\sum_T\frac{|S\cap T|-1}{2}A_{ST}$, and scatter adds $(\sum_{i\in S}C_i-C_\ast)/2$ using one extra central wire $C_\ast$.",
   r"$\mathbb Z[i,1/2]$, and neighbors are distinct triples with even"),
  infer("S2.1.3",
   r"The forward schedule has eight rows: subtract side injection, subtract scatter (removing the old scratch effect), copy, gather, scatter, side injection (loading the source and adding its effect to the target), undo gather, undo copy (restoring scratch).",
   r"the next four introduce the source values and add their effect to the"),
  infer("S2.1.4",
   r"With copy $\mathcal V$, gather $\mathcal G$, side injection $\mathcal J$ and scatter $\mathcal R$, the net change of the target is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$ for any initial scratch vectors, because rows 0-1 subtract $\mathcal J a+\mathcal R c$ and rows 4-5 add back $\mathcal J(a+\mathcal Vx)+\mathcal R(c+\mathcal Gx)$.",
   r"$(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of"),
  infer("S2.1.5",
   r"Bit case: the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod 2$; the side injection cancels exactly the intersection-one cases, distinct triples with intersection zero or two already have coefficient zero, and the self coefficient is one, so the net map is $y\gets y+x$.",
   r"intersection-one cases; distinct triples with intersection zero or two"),
  infer("S2.1.6",
   r"Complex case: the central coefficient is $(|S\cap T|-1)/2$; the side injection cancels it for distinct triples with intersection zero or two, intersection one contributes zero, and the self coefficient is one, so the net map is again $y\gets y+x$.",
   r"In the complex case, the central coefficient is $(|S\cap T|-1)/2$."),
  infer("S2.1.7",
   r"Running the forward invocation from $X$ to $Y$, the inverse schedule from $Y$ to $X$, and the forward invocation again gives $(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x)$.",
   r"$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$."),
  infer("S2.1.8",
   r"Counting ordered neighbour pairs (there are $vz$ side wires per invocation, with $z_{\rm b}=3\binom{97}{2}=13968$ and $z_{\rm c}=\binom{97}{3}+3\cdot97=147731$ neighbours per triple) and $c_{\rm b}=100$, $c_{\rm c}=101$ central wires gives $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})$ and $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})$, fixed finite numbers.",
   r"W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b})"),
 ],
 page="scratch-restoring-exchange",
 frm=["sets-subsets-and-cartesian-products","arithmetic-modulo-2-and-xor","matrices-vectors-and-linear-maps","permutations-and-bijections"],
 adds=[
  B("h","ground-set size","Size $100$ of the ground set $[h]$ whose three-element subsets index the data banks."),
  B("v","triples per coordinate","Number $\\binom h3=161700$ of three-element subsets of $[h]$.","count"),
  B("N","bank size","Number $v^3$ of data wires in each of the two banks $X$ and $Y$.","count"),
  B("I","invocations","Number $3v^2$ of separate invocations of the eight-row schedule, each with private scratch wires.","count"),
 ],
 salient="The exchange is exact for arbitrary initial values of every scratch wire, so the roles that carry other data can serve as scratch and still be restored.",
)

# ---------------------------------------------------------------- S2.2 frames
S22 = show(
 "S2.2",
 r"Replacing each scalar wire by an array in $R^\Omega$ and assigning an invertible frame $D_v$ to every vertex (shared by all incidences of a gate) makes the implemented operator $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$, so only the endpoint frames determine the result and each edge needs only the change $D_vD_u^{-1}$.",
 "Prove the invariant that the stored array at a vertex equals the frame applied to the logical array, using that a pointwise linear gate commutes with a common frame.",
 mot("Once the scalar routing is fixed, the endpoint frames fix the array operator on each route, leaving the intermediate frames free to be chosen so that every edge change is cheap.", "explicit", r"intermediate frames can then be chosen to make each edge change inexpensive."),
 [
  infer("S2.2.1",
   r"The supplied input $f$ needs no preprocessing: its logical array is defined as $g=D_{\rm in}^{-1}f$, and at every vertex the stored array equals $D_v$ applied to the logical array (true at the sources by definition; an edge from $u$ to $v$ changes $D_u\varphi$ to $D_v\varphi$ by $D_vD_u^{-1}$).",
   r"At a vertex $v$, the invariant is that the stored array equals $D_v$ applied"),
  infer("S2.2.2",
   r"At a gate all wires share the frame $D_v$, and $R$-linearity gives $\sum_j c_jD_v\varphi_j=D_v(\sum_j c_j\varphi_j)$, so the pointwise gate commutes with the frame and the invariant continues through it.",
   r"$\sum_j c_jD_v\varphi_j=D_v(\sum_j c_j\varphi_j)$ for each output combination, with"),
  infer("S2.2.3",
   r"The implemented operator is therefore $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$; for a signed role permutation sending input role $w$ to $\rho(w)$ with sign $\varepsilon_w$, the route applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ on every role, auxiliary roles included.",
   r"D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}."),
 ],
 page="array-frames",
 frm=["scratch-restoring-exchange","matrices-vectors-and-linear-maps","permutations-and-bijections"],
 salient="Intermediate frames cancel along a route: the operator on each role depends only on the frames at its source and its sink.",
)

# ---------------------------------------------------------------- S2.3 labels
S23 = show(
 "S2.3",
 r"Nondegenerate subspaces of the $m$-dimensional space $F^{\otimes3}$ ($m=h^3=10^6$) can be attached to gates and terminals of the bit network so that adjacent labels are nested, only one edge per central wire decreases (by $h$), and the total edge rank is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.",
 "Label each vertex by a subspace built from indicator vectors of three-element subsets, count the dimension change on every edge, and add the one extra rank per negative source projection.",
 mot("The saving will come from keeping the total dimension lost on decreasing edges small relative to $N$.", "explicit", r"The saving will come from keeping the total dimension lost on decreasing"),
 [
  infer("S2.3.1",
   r"On $F=\mathbb Q^h$ with the form $x^{\mathsf T}(I-J/9)y$ the triple indicators satisfy $\langle t_S,t_T\rangle=|S\cap T|-1$ and $\langle t_T,t_T\rangle=2$, so every triple line is nondegenerate and neighbouring triple lines are orthogonal; over $\mathbb F_2$ with the dot product (complex network) $t_T\cdot t_T=1$.",
   r"\langle t_S,t_T\rangle=|S\cap T|-1,"),
  infer("S2.3.2",
   r"On $\mathcal F=F^{\otimes3}$ put $u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$ and $U_a=\langle u_a\rangle$; the terminal labels are $X_a$: source $U_a$, sink $\mathcal F$; $Y_a$: source $0$, sink $U_a^\perp$; scratch: source $0$, sink $\mathcal F$, so source dimensions sum to $N$, sink dimensions to $Wm-N$, and the signed dimension changes to $Wm-2N$.",
   r"The source dimensions sum to $N$ and the sink dimensions to $Wm-N$."),
  show("S2.3.3",
   r"For every edge the labels are nested and nondegenerate; the only decreasing edges are the central-wire edges from time 3 to time 4, each losing $P\otimes F$ of dimension $h$, so $L=Ich$ and the sum of absolute dimension changes is $Wm-2N+2L$.",
   "Prescribe the stage-to-stage transitions of the data wires and the eight gate labels, tabulate the orthogonal residual of every edge, and observe where the dimension drops.",
   mot("The residual of an edge (orthogonal complement of the smaller label in the larger) has dimension equal to the label change, so tabulating all residuals gives the exact rank budget.", "recoverable"),
   [
    infer("S2.3.3.1",
     r"With $A=F^{\otimes(j-1)}$, $P=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle$, $B=P^\perp$ and $Q$ the trailing tensor line, the outgoing labels of stage $j$ equal the incoming labels of stage $j+1$ ($A'=A\otimes F$, $P'=P\otimes\langle t\rangle$, $B'=(P')^\perp_{A'}$), starting from $U_a$ on $X_a$ and $0$ on $Y_a$ and ending at $\mathcal F$ and $U_a^\perp$.",
     r"the next incoming labels. At stage 1 they start at $U_a$ on $X_a$"),
    infer("S2.3.3.2",
     r"The eight gate labels (suppressing $Q$) are: time 0 $Y$-side $B\otimes\langle t\rangle$; 1 $Y$-centre $B\otimes F$; 2 $X$-side $(B\otimes F)\perp(P\otimes\langle t\rangle)$; 3 $X$-centre $A\otimes F$; 4 $Y$-centre $B\otimes F$; 5 $Y$-side $(B\otimes F)\perp(P\otimes t^\perp)$; 6 $X$-centre $A\otimes F$; 7 $X$-side $A\otimes F$; the gate order confines every decrease to the return of a central wire from $A\otimes F$ to $B\otimes F$.",
     r"0&Y,\ \text{its side wires}&B\otimes\langle t\rangle\\"),
    infer("S2.3.3.3",
     r"The residual dimensions are, with $a=h^{j-1}$ and $f=h^{3-j}$: $X$: in$\to$2 $(a-1)(h-1)$, 2$\to$3 $h-1$, 3$\to$6 and 6$\to$7 zero; $Y$: in$\to$0 zero, 0$\to$1 $(a-1)(h-1)$, 1$\to$4 zero, 4$\to$5 $h-1$; centre: source$\to$1 $(a-1)h$, 1$\to$3 $h$, 3$\to$4 $h$, 4$\to$6 $h$; side: source$\to$0 $a-1$, 0$\to$2 $(a-1)(h-1)+1$, 2$\to$5 $h-2$ (uses $\langle t_X\rangle\subset t_Y^\perp$ for neighbours), 5$\to$7 $1$; scratch: last$\to$sink $ah(f-1)$.",
     r"\mathrm{center}:\ 3\to4&P\otimes F&h\\"),
    infer("S2.3.3.4",
     r"Label dimension is nondecreasing along every edge except the centre edge 3$\to$4, which removes $P\otimes F\otimes Q$.",
     r"Label dimension is nondecreasing along every edge except center $3\to4$, which removes"),
    infer("S2.3.3.5",
     r"The signed dimension changes telescope at every gate (each touched wire enters and leaves with the same gate label), giving a signed increase $Wm-2N$; with $Ic$ decreasing edges ($c$ central wires per invocation) each of loss $h$, $L=Ich$, and replacing signed by absolute changes adds $2L$.",
     r"The signed sum of dimension changes telescopes at every gate: each"),
    infer("S2.3.3.6",
     r"Over $\mathbb F_2$ every nonzero residual is nonalternating (it contains a norm-one coordinate vector outside the supports of the earlier tensor vectors), hence has an orthonormal basis, which the complex network needs.",
     r"For completeness, every nondegenerate nonalternating binary symmetric"),
   ],
   salient="Exactly one edge per central wire decreases, and it loses only $h=100$ dimensions, out of $m=10^6$ per edge.",
  ),
  infer("S2.3.4",
   r"The loss ratios are exactly $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both below $1/2$.",
   r"\frac{L_{\rm b}}{N}=\frac{100}{539},\qquad"),
  show("S2.3.5",
   r"In the bit network, with matrix $M_v=P_U$ (projection onto the label) at each gate or sink and $-P_{U_a}$ at the source of $X_a$, every input role has endpoint difference $I_m$ and the sum of rational ranks of edge differences is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}=177176569088785861287000000<W_{\rm b}m$.",
   r"Identify the rank of each edge difference with the label's dimension change, correct for the $N$ negative source projections, and compare with $W_{\rm b}m$.",
   mot("The frame on the tape is a shear $(H,D)\\mapsto(H+MD,D)$ whose cost is its rank, so the rank sum $s$ is exactly the number of smaller calls.", "recoverable"),
   [
    infer("S2.3.5.1",
     r"The sum of ranks is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$.",
     r"=W_{\rm b}m-N+2L_{\rm b}"),
    infer("S2.3.5.2",
     r"For nested nondegenerate $U\subset V$, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement, so its rank is $\dim V-\dim U$ and reversing the edge does not change it.",
     r"$P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its"),
    infer("S2.3.5.3",
     r"The only exceptions are the $N$ negative source projections: at stage 1, $B=0$ and the first gate on $X_a$ has label exactly $U_a$, so the first edge matrix is $2P_{U_a}$ of rank one where the dimension change was zero; this adds $N$ to the rank sum.",
     r"Its first edge matrix is therefore $2P_{U_a}$, of rational rank one,"),
    infer("S2.3.5.4",
     r"The deficit of $s_{\rm b}$ from $W_{\rm b}m$ is $N-2L_{\rm b}>0$, because $L_{\rm b}<N/2$.",
     r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$."),
    infer("S2.3.5.5",
     r"For an input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$, and every other role has source matrix zero and sink matrix identity.",
     r"$P_{U_a^\perp}-(-P_{U_a})=I_m$."),
   ],
   salient=r"The strict inequality $s_{\rm b}<W_{\rm b}m$ survives although the negative source projections cost $N$ extra ranks, because the decreasing edges lose only $2L_{\rm b}=\frac{200}{539}N<N$.",
  ),
 ],
 page="subset-intersection-labels",
 frm=["rank-and-orthogonal-subspaces","scratch-restoring-exchange","array-frames","dot-product-inner-product-and-orthogonality","triangular-and-permutation-matrices"],
 adds=[
  B("L","decreasing-edge loss","Total dimension lost on the decreasing edges of the network."),
  B("F","label field space","The one-dimensional-factor space $\\mathbb Q^h$ (or $\\mathbb F_2^h$) whose triple tensor power carries the labels."),
  B("P","earlier-triple line","The line spanned by the tensor of the indicators of the already fixed triple coordinates at stage $j$."),
  B("B","complement of the earlier line","The orthogonal complement $P^\\perp$ in the tensor power of the earlier coordinates."),
 ],
)

# ---------------------------------------------------------------- S2.4 complex phase network
S24 = show(
 "S2.4",
 r"In the complex network, each edge frame $\mathcal C_V\mathcal C_U^{-1}$ is a product of one translation kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal basis of the edge residual, the kernel counts sum to $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}=1873807244636671267308000000<W_{\rm c}m$, and telescoping gives $C^{\otimes m}$ on every role.",
 "Use binary labels and phase frames $\\mathcal C_U=H^{\\otimes m}\\mathrm{diag}(i^{q_U(x)})H^{\\otimes m}$ with $q_U(x)=\\mathrm{wt}(P_Ux)\\bmod4$, so that a change of label is a Hamming-weight phase that the Hadamard conjugation turns into translation kernels.",
 mot("Over $\\mathbb F_2$ with orthonormal residual bases, weight is additive mod 4 across orthogonal vectors, so each basis vector contributes one two-point kernel; this is what lets every edge be done by smaller calls of the same butterfly procedure.", "recoverable"),
 [
  infer("S2.4.1",
   r"For orthogonal binary vectors the weight is additive modulo four, so for $V=U\perp E$ with orthonormal basis $\mathcal B$ of $E$, $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\mathrm{wt}(v)[v\cdot x]\pmod4$.",
   r"If $z\cdot w=0$, the intersection cardinality is even, so weight is"),
  infer("S2.4.2",
   r"Each basis vector has norm one, so its weight is odd and its phase coefficient is $\varepsilon\in\{1,-1\}$ modulo four.",
   r"Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd."),
  infer("S2.4.3",
   r"The phase $i^{\varepsilon[v\cdot x]}=\frac{1+i^\varepsilon}2+\frac{1-i^\varepsilon}2(-1)^{v\cdot x}$ becomes the translation kernel $aI+bX_v$ (or its inverse) under the identity $H\,\mathrm{diag}(1,-1)H=X$, with $a=\frac{1+i}2$, $b=\frac{1-i}2$.",
   r"becomes $aI+bX_v$ or its inverse."),
  infer("S2.4.4",
   r"Summing the basis lengths gives $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$ (no extra source ranks, unlike the bit network), with deficit $2N-2L_{\rm c}>0$.",
   r"The deficit is $2N-2L_{\rm c}>0$."),
  infer("S2.4.5",
   r"For the pair $X_a\to Y_a$, with $u=u_a$ of weight $27$, $q_{U_a^\perp}(x)-q_{U_a}(x)=\mathrm{wt}(x)+2[u\cdot x]\pmod4$.",
   r"&=\operatorname{wt}(x)+2[u\cdot x]\pmod4."),
  infer("S2.4.6",
   r"The operator on $X_a\to Y_a$ is $C^{-1}$ on the $27$ coordinates of $\mathrm{supp}(u)$ and $C$ elsewhere; since $C=iZC^{-1}Z$ with $Z=\mathrm{diag}(1,-1)$, applying $Z$ before at $X_a$ and $i^{27k}Z$ after at $Y_a$ turns each inverse factor into $C$.",
   r"27 coordinates of $\operatorname{supp}(u)$ and $C$ elsewhere."),
  infer("S2.4.7",
   r"After negating the physical $X$ outputs and sending output role $\rho(w)$ back to $w$, every role, scratch roles included, carries $C^{\otimes m}$ (and $C^{\otimes mk}$ on $k$ columns).",
   r"the required forward tensor product."),
 ],
 page="phase-frame-network",
 frm=["array-frames","scratch-restoring-exchange","subset-intersection-labels","rank-and-orthogonal-subspaces","complex-numbers","arithmetic-modulo-2-and-xor","dyadic-rationals-and-fixed-width-numerators"],
 salient="Every role, including the auxiliary roles that merely carry other data, ends up with the same two-point-kernel tensor power $C^{\\otimes m}$.",
)

# ---------------------------------------------------------------- S2.5 numeric margin
S25 = show(
 "S2.5",
 r"With $\tau=\sigma=1-2^{-50}$, $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$, so the strict rank saving becomes a power-exponent saving.",
 "Compare the exact relative rank deficits with the factor lost in replacing $m$ by $m^{1-2^{-50}}$, using $\\log m<20$.",
 mot("The recursion needs a rational exponent below one with $s/W<m^\\tau$; the rank deficits are about $10^{-11}$ of $Wm$, so an exponent within $20\\cdot2^{-50}$ of one fits inside it.", "recoverable"),
 [
  infer("S2.5.1",
   r"The relative rank deficits are $\eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m}=\frac{339}{22587335000000}$ and $\eta_{\rm c}=\frac{73}{19906842167500}$.",
   r"\eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m}"),
  infer("S2.5.2",
   r"Both exact deficits are greater than $20\cdot2^{-50}$.",
   r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$."),
  infer("S2.5.3",
   r"Since $m<2^{20}$ and $\log2<1$ we have $\log m<20$.",
   r"Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence"),
  infer("S2.5.4",
   r"Hence $m^{1-2^{-50}}=m\exp(-2^{-50}\log m)>m(1-20\cdot2^{-50})>m(1-\eta)$ for $\eta=\eta_{\rm b}$ or $\eta_{\rm c}$.",
   r">m(1-20\cdot2^{-50})>m(1-\eta)"),
  infer("S2.5.5",
   r"Consequently $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$ with $\tau=\sigma=1-2^{-50}$.",
   r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,"),
 ],
)

# ---------------------------------------------------------------- S2.6 shear
S26 = show(
 "S2.6",
 r"For a rational matrix $A$ of rank $a$ the address shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ is performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ other work.",
 "Factor $A=E_1\\Pi E_2$ with lower-triangular invertible $E_1,E_2$ and a partial permutation $\\Pi$ with $a$ ones, do the triangular factors by controlled shifts, and realize each one of $\\Pi$ by one interchange.",
 mot("Lower triangular changes of coordinates can be performed entirely in the tape direction (a later field updated from earlier ones in linear time), so only the permutation part needs a real interchange.", "explicit", r"can be performed entirely in this direction."),
 [
  infer("S2.6.1",
   r"Every rational $m\times m$ matrix $A$ of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ having exactly $a$ ones, at most one per row and column.",
   r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization"),
  infer("S2.6.2",
   r"Proof by elimination: take the topmost nonzero row and its rightmost nonzero entry as pivot, clear its row to the left by right multiplication and its column below by left multiplication with lower triangular elementary matrices, scale the pivot to one, delete that row and column and repeat.",
   r"lower triangular elementary matrices, and scale the pivot to one."),
  infer("S2.6.3",
   r"A lower triangular transformation of $H$ or of $D$ costs $O(V)$: update coordinates in descending physical order, each by a unit multiple plus a fixed combination of earlier coordinates, using the controlled shifts of linear cost (a fixed odd prime $q$ avoiding all denominators and diagonal numerators is chosen once).",
   r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
  infer("S2.6.4",
   r"For $A=E_1\Pi E_2$: transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$.",
   r"For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,"),
  infer("S2.6.5",
   r"Each one of $\Pi$ at position $(i,j)$ asks for $H_i\leftarrow H_i+D_j$, done by $D_j\leftarrow D_j+H_i$, then interchange $(H_i,D_j)\leftarrow(D_j,H_i)$, then $D_j\leftarrow H_i-D_j$, which sends $(h,d)$ to $(h+d,d)$.",
   r"this sequence yields $(h+d,d)$."),
  infer("S2.6.6",
   r"This uses just one interchange per one of $\Pi$, hence exactly $a$ interchanges for rank $a$.",
   r"It uses just one interchange."),
 ],
 page="address-shear-factorization",
 frm=["controlled-cyclic-shift","tape-address-model","triangular-and-permutation-matrices","matrices-vectors-and-linear-maps","modular-arithmetic"],
 adds=[
  B("A","shear matrix","Rational matrix defining the shear $(H,D)\\mapsto(H+AD,D)$."),
  B("a","matrix rank","Rank of the matrix $A$, equal to the number of interchanges."),
  B("\\Pi","partial permutation","Matrix with exactly $a$ ones, at most one in each row and column, in the factorization $A=E_1\\Pi E_2$."),
 ],
 salient="The cost of a shear is exactly its rank in interchanges, not $m$: low-rank edge changes are the cheap ones.",
)

# ---------------------------------------------------------------- S2.7 power width
S27 = show(
 "S2.7",
 r"Given the circuit data with endpoint differences $I_m$ and $s<Wm$, two chunks of $e=m^k$ radix-$q$ digits (row field length divisible by $W^k$) can be interchanged in $O(Ve^\tau)$ time, because the normalised cost satisfies $F_k\le(s/W)F_{k-1}+O(1)$ with $s/W<m^\tau$.",
 "Run the bit network on $W$ row streams of volume $V/W$ with frames given by the shear permutations $\\Phi_M$, implement every edge by recursive smaller interchanges via the rank factorisation, and solve the resulting recurrence as a geometric sum.",
 mot("Each of the $s$ recursive calls works on only a $1/W$ fraction of the volume, so the cost per unit volume is multiplied by $s/W$ per level; a ratio below $m^\\tau$ gives growth $m^{k\\tau}=e^\\tau$ rather than $e$.", "recoverable"),
 [
  infer("S2.7.1",
   r"Write each chunk as $m$ fields of $b=e/m$ digits (vectors $H,D$) and split whole rows cyclically into $W$ role streams, row $r=Wg+(w-1)$ going to stream $w$ with row number $g$; each stream has the same shape, volume $V/W$ and a row count divisible by $W^{k-1}$.",
   r"Split whole rows cyclically into $W$ role streams within each prefix"),
  infer("S2.7.2",
   r"Using the frame $\Phi_{M}$ (move the entry at $(H,D)$ to $(H+MD,D)$) at each vertex and applying $\Phi_{A_e}$ on every edge, the physical output on role $\rho(w)$ is $\Phi_{M_{\rm out}}\Phi_{-M_{\rm in}}f_w=\Phi_{I_m}f_w$, i.e. the shear $H\leftarrow H+D$ on every row, scratch rows included.",
   r"=\Phi_{I_m}f_w,"),
  infer("S2.7.3",
   r"The full interchange is $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$, componentwise; only the middle shear uses the circuit and the others have linear cost.",
   r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,"),
  infer("S2.7.4",
   r"The number of recursive calls is the sum of the edge ranks, exactly $s$, each on a stream of volume $V/W$.",
   r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
  infer("S2.7.5",
   r"If $F_k$ bounds time divided by logical volume at width $m^k$, then $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.",
   r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."),
  infer("S2.7.6",
   r"For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$: if $a\le1$ it is at most $k+1$, and if $a>1$ it is $O(a^k)$.",
   r"For $a=s/W<m^\tau$ the geometric sum"),
  infer("S2.7.7",
   r"Hence $F_k=O(e^\tau)$ and the interchange costs $O(Ve^\tau)$.",
   r"Hence $F_k=O(e^\tau)$."),
  infer("S2.7.8",
   r"Scheduling the recursive calls on a fixed number of tapes (parking the $W-1$ inactive role streams on a stack, copying the active one to the child, popping on return) costs only $O(V)$ per node, so it does not change the factor $s/W$.",
   r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
  infer("S2.7.9",
   r"Descriptor processing is also absorbed: both chunk ranges stay present in every child, so $\log V_0=O(\log(2V_j))$ and fixed powers of the descriptor length cost $O(V_j)$ at depth $j$.",
   r"For completeness, descriptor processing also fits this term when the"),
 ],
 page="power-width-interchange",
 frm=["scratch-restoring-exchange","array-frames","subset-intersection-labels","address-shear-factorization","rank-saving-recurrence","divide-and-conquer-and-recurrences","geometric-series-and-sums"],
 adds=[
  B("e","chunk width","Number $m^k$ of radix-$q$ digits in each of the two chunks."),
  B("k","recursion depth","Exponent with $e=m^k$, the number of levels of the recursion.","count"),
  B("F_k","normalised cost","Time divided by logical volume for interchanging chunks of $m^k$ digits."),
 ],
 salient="Although intermediate values are XOR combinations of data, the final effect is an exact permutation, correct for arbitrary initial scratch contents.",
)

# ---------------------------------------------------------------- S2.8 arbitrary width
S28 = show(
 "S2.8",
 r"Two disjoint contiguous address fields of $u$ bits of an array on $[P]\times[2^u]\times[G]\times[2^u]\times[B]$ can be interchanged, $(p,h,g,d,z)\mapsto(p,d,g,h,z)$, in $O(Vu^\tau)$ steps for the fixed $\tau=1-2^{-50}$, for arbitrary $u$ and with no assumption on the number of rows.",
 "Supply the needed rows from the top $\\rho=O(\\log e)$ digits of the chunks themselves, pad the row count to a multiple of $W^k$, split the remaining width in base $m$ into pieces of $m^j$ digits, apply the power-width interchange to each piece, and reduce binary widths to radix $q$ by padding.",
 mot("Rows for a general array can be supplied by a few of its own high digits.", "explicit", r"Rows for a general array can be supplied by a few of its own high digits."),
 [
  infer("S2.8.1",
   r"For chunks of $e$ radix-$q$ digits set $k=\lceil\log_m e\rceil$.",
   r"k=\lceil\log_m e\rceil,\qquad"),
  infer("S2.8.2",
   r"Set $\rho=\left\lceil\frac{k\log W}{2\log q}\right\rceil$, so that $1\le\rho<e$ and $\rho=O(\log(2e))$ for large $e$ (bounded widths are done digit by digit).",
   r"\rho=\left\lceil\frac{k\log W}{2\log q}\right\rceil."),
  infer("S2.8.3",
   r"Write each chunk as its top $\rho$ digits followed by the rest ($h^+,h^-$ and $d^+,d^-$), interchange the high digits one pair at a time and join them, giving the orders $(h^+,h^-,g,d^+,d^-)\to(d^+,h^+,h^-,g,d^-)\to(d^+,h^+,d^-,g,h^-)\to(d^+,d^-,g,h^+,h^-)$.",
   r"Write each chunk as its top $\rho$ digits followed by its remaining"),
  infer("S2.8.4",
   r"In the two middle orders the first two fields form a row field of range $R=q^{2\rho}\ge W^k$ before both remaining chunks.",
   r"R=q^{2\rho}\ge W^k"),
  infer("S2.8.5",
   r"Padding with zero rows to $R'=W^k\lceil R/W^k\rceil<2R$ makes the row count divisible by every needed $W^j$ and at most doubles the volume.",
   r"R'=W^k\left\lceil R/W^k\right\rceil<2R."),
  infer("S2.8.6",
   r"Write the remaining width in base $m$, $e-\rho=\sum_{j=0}^{k}a_jm^j$ with $0\le a_j<m$, and cut the chunks into $a_j$ pieces of width $m^j$, each pair interchanged by the power-width procedure.",
   r"e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m."),
  infer("S2.8.7",
   r"The total cost is $O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)$, a geometric sum since $a_j<m$ and $m^k<me$; the remaining movement costs $O(V\log(2e))$.",
   r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)."),
  infer("S2.8.8",
   r"For binary chunks take the least $e$ with $q^e\ge2^u$ and pad each range from $[2^u]$ to $[q^e]$; the volume grows by less than $q^2$, a fixed factor, and $e=O(u)$, so the cost is $O(Vu^\tau)$.",
   r"Finally, for binary chunks let $e$ be the least integer with"),
  infer("S2.8.9",
   r"Chunks whose widths differ by one bit are handled by moving the extra leading bit with one linear single-bit move and interchanging the equal-width parts.",
   r"For widths differing by one bit, choose the leading bit of the longer"),
 ],
 page="address-chunk-interchange",
 frm=["power-width-interchange","rank-saving-recurrence","tape-address-model","controlled-cyclic-shift","positional-notation-in-any-radix"],
 adds=[
  B("u","chunk bit width","Number of bits in each of the two address chunks being interchanged."),
  B("\\rho","row digits","Number of top digits of each chunk used to supply the row field."),
  B("a_j","base-$m$ digit","Coefficient of $m^j$ in the base-$m$ expansion of the remaining width $e-\\rho$."),
 ],
)

# ---------------------------------------------------------------- S2.9 butterfly layer
for _c in S24["children"]:
    _c["deferred"] = True

S291 = show(
 "S2.9.1",
 r"A layer $C^{\otimes e}$ on $e=mf$ selected axis-chunks reduces to $s_{\rm c}$ calls of the same procedure on $f=e/m$ chunks, using phase frames, a basis change $\mathcal P_M$ done by at most $m(m-1)+3m$ row additions, and the identity $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$.",
 "Conjugate each edge's kernel product by an address permutation so that the residual directions become standard basis directions, apply one child per direction on the $f$ axes of a slot, and express the permutation by row additions on selected bits.",
 mot("Each edge frame is a product of kernels along arbitrary directions; conjugating by an invertible $\\mathcal P_M$ puts the directions in coordinate positions, and an invertible binary matrix is a fixed product of row additions, which act on selected bits of whole slots at once.", "recoverable"),
 [
  infer("S2.9.1.1",
   r"With $C=H\mathsf SH=aI+bX$ the direct identities $H_0=b\mathsf SC\mathsf S$, $C^2=X$, $C^4=I$ and $C^{-1}=bI+aX=-iZCZ$ hold, using only Gaussian dyadic coefficients.",
   r"H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad"),
  infer("S2.9.1.2",
   r"For $M\in\mathrm{GL}(m,\mathbb F_2)$ the address permutation $\mathcal P_M$ satisfies $\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}$.",
   r"\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}."),
  infer("S2.9.1.3",
   r"Extending the residual basis to a basis of $\mathbb F_2^m$ as the first columns of $M$ gives $\mathcal C_{U_+}\mathcal C_{U_-}^{-1}=\mathcal P_M\bigl(\prod_{j}C_{e_j}^{\epsilon_j}\bigr)\mathcal P_M^{-1}$; invertibility of $M$ suffices.",
   r"=\mathcal P_M\left(\prod_{j=1}^{\rho_{\rm edge}}C_{e_j}^{\epsilon_j}\right)"),
  infer("S2.9.1.4",
   r"On a group of $e=mf$ chunks, cut into $m$ slots of $f$ chunks with columns $(x_{1,j},\dots,x_{m,j})$, apply $\mathcal P_M^{-1}$ to each column, then $(C^{\epsilon_h})^{\otimes f}$ to the $f$ bits $x_{h,0},\dots,x_{h,f-1}$ of slot $h$ (one child per residual direction), then $\mathcal P_M$.",
   r"$1\le h\le\rho_{\rm edge}$, apply $(C^{\epsilon_h})^{\otimes f}$ to the"),
  infer("S2.9.1.5",
   r"A negative kernel needs only one forward child: $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$, with the wrappers being address signs and fourth-root phases.",
   r"=(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}."),
  infer("S2.9.1.6",
   r"Gaussian elimination writes any $M\in\mathrm{GL}(m,\mathbb F_2)$ as a product of at most $m(m-1)+3m$ elementary row additions (a swap is three additions), each applying $x_{h,j}\leftarrow x_{h,j}\oplus x_{h',j}$ for all $j<f$ at once.",
   r"Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$"),
  infer("S2.9.1.7",
   r"Summing residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot; the endpoint signs and the scalar $i^{27f}$ turn every endpoint kernel into a forward one, so the result is $C^{\otimes e}$ on every role.",
   r"$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
  infer("S2.9.1.8",
   r"On all selected coordinates $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ with $(\mathcal S_Dz)(x)=i^{x_1+\dots+x_D}z(x)$ and $b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}$, a shift, a fourth-root phase and at most one factor $b$.",
   r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D."),
 ],
 frm=["phase-frame-network","packed-selected-bit-addition","complex-numbers","roots-of-unity-and-euler-s-formula","matrix-transposition"],
)

S292 = show(
 "S2.9.2",
 r"One binary row addition $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ at the selected positions $j_i=\rho+iK$ ($0\le i<f$) of two chunks of $L=fK$ bits, with a third chunk $z$ restored for every initial value, costs $O(V(L^\tau+1))$ when $R$ exceeds every fixed polynomial in $p$, $f\le d\le p$ and $K/\log p\to\infty$.",
 "Apply eight whole-chunk cyclic shifts that implement the XORs correctly away from a small exceptional set of guard-violating addresses, then repair that set deterministically by extracting, sorting and reinserting only those records.",
 mot("The construction first uses a constant number of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of addresses.", "explicit", r"of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of"),
 [
  infer("S2.9.2.1",
   r"For a Boolean control $c$, eight conditional $\pm1$ updates of two integers $u,w$ (tested on the parity of the other) act on each square $\{2a,2a+1\}\times\{2b,2b+1\}$: the first four induce the cycle $(00\ 01\ 10)$ on the parities of $(u,w)$ and the last four the cycle $(01\ 10\ 11)$.",
   r"induce the cycle $(00\ 01\ 10)$ in every square"),
  infer("S2.9.2.2",
   r"Composed, the eight operations give $(u',w')=(u+c(1-2(u\bmod2)),w)$: the parity of $u$ flips exactly when $c=1$, both quotients by two are preserved, and the auxiliary integer $w$ is restored; each coordinate moves by at most four.",
   r"\bigl(u+c(1-2(u\bmod2)),\ w\bigr)."),
  infer("S2.9.2.3",
   r"Applied simultaneously to $f-1$ disjoint $K$-bit segments, each line is a single cyclic shift of a whole chunk range, $y\leftarrow y+\varepsilon\sum_{i=0}^{f-2}2^{j_i}[x_{j_i}=1][z_{j_i}=b]\pmod{2^L}$, with an offset that does not depend on the target chunk.",
   r"\varepsilon\sum_{i=0}^{f-2}2^{j_i}"),
  infer("S2.9.2.4",
   r"Writing the segments as $u_i=2g_i+a_i$ and $w_i=2h_i+b_i$ with guard values $g_i,h_i$, an address is good when every used guard satisfies $10\le g\le2^{K-1}-11$; then no segment carries into or borrows from the next, and the shifts agree with the ideal XOR permutation $T_0$.",
   r"10\le g\le 2^{K-1}-11."),
  infer("S2.9.2.5",
   r"Exactly twenty values are excluded for each of the $2(f-1)$ guards, so the bad set $\mathcal B$ satisfies $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, independently of any record value.",
   r"|\mathcal B|\le\delta_{\rm bad}M."),
  infer("S2.9.2.6",
   r"Both $T_0$ and the shift composition $S_0$ are bijections that agree off $\mathcal B$, so $T_0S_0^{-1}$ fixes the complement of $\mathcal B$ and permutes $\mathcal B$.",
   r"Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$."),
  infer("S2.9.2.7",
   r"Each rotation is made after swapping the target to the rightmost of the three chunk positions (with the chunk interchange of cost $O(VL^\tau)$) and costs $O(V)$ by the controlled-shift lemma, since the offset work is absorbed by the $2^L$ target blocks; $S_0$ has at most sixteen swaps and eight rotations.",
   r"There are at most sixteen swaps and eight rotations in $S_0$."),
  infer("S2.9.2.8",
   r"The correction scans the stream with a record-rank counter, extracts the records of $\mathcal B$ with their destination ranks, sorts them stably by key (the keys are distinct and equal the ranks of the marked holes) and reinserts them in one scan, implementing $T_0$ everywhere.",
   r"$\mathcal B$, these keys are distinct and are exactly the ranks of the"),
  infer("S2.9.2.9",
   r"The movement costs $O(V(L^\tau+1))$, the full record scans $O(MA_{\rm rect}^3+V)$ and the radix passes $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$.",
   r"The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans"),
  infer("S2.9.2.10",
   r"After division by $V$ the extra terms are at most $A_{\rm rect}^3/R\to0$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)=O(p^22^{-K}(1+A_{\rm rect}/R))=o(1)$ under the family bounds, leaving $O(V(L^\tau+1))$.",
   r"$O(p^2 2^{-K}(1+A_{\rm rect}/R))=o(1)$"),
 ],
 page="packed-selected-bit-addition",
 frm=["address-chunk-interchange","controlled-cyclic-shift","tape-address-model","sorting-and-its-cost","arithmetic-modulo-2-and-xor","modular-arithmetic"],
 adds=[
  B("K","chunk width","Number of bits in each address chunk, $K=\\lfloor d^c\\rfloor$."),
  B("f","chunks per slot","Number of $K$-bit chunks in a slot, so a slot has $L=fK$ address bits.","count"),
  B("\\mathcal B","bad address set","Set of addresses at which some used guard value falls outside the safe interval."),
  B("\\delta_{\\rm bad}","bad fraction","Bound $\\min\\{1,80(f-1)2^{-K}\\}$ on the fraction of addresses in the bad set."),
 ],
 salient="All $f$ selected bits are XORed by a constant number (eight) of whole-chunk shifts, independent of $f$, and the only exceptions are exponentially rare in $K$.",
)

S293 = infer("S2.9.3",
 r"The complete binary change of basis of a group of $e$ chunks and its inverse cost $O(V((eK)^\tau+1))$ on a stream of volume $V$.",
 r"the complete change of basis and its inverse therefore cost")

S294 = show(
 "S2.9.4",
 r"For $e=m^k$ active chunks the normalised cost satisfies $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, $F(e)=O(e)$ below the cutoff $d^\beta$, and unrolling gives $O(d^{\lambda'})$ for the whole layer.",
 "Split rows among the $W$ roles so each of the $s$ child calls sees volume $V/W$, stop the recursion at $e<d^{\\beta}$ and use individual kernels, then sum the internal and leaf contributions and decompose a general $D$ in base $m$.",
 mot("Each child sees $1/W$ of the parent's volume, so the recursion multiplies the normalised cost by $s/W$ where the number of axes is multiplied by $m$; the strict inequality $s/W<m$ makes the sum geometric.", "explicit", r"After dividing cost by volume, multiplying the parameter by $m$"),
 [
  infer("S2.9.4.1",
   r"Applying one $C$ kernel by splitting on the selected bit, computing $C(u,v)$ coefficientwise and merging costs $O(V)$, so $e$ individual kernels cost $O(Ve)$.",
   r"\(O(Ve)\) on any stream with these complete ranges and record format."),
  infer("S2.9.4.2",
   r"An internal node with $e=m^k$ chunks makes exactly $s$ calls, one per vector of an edge residual basis, on slots of $e/m$ chunks.",
   r"vector in an edge residual basis, hence exactly \(s\) calls in one"),
  infer("S2.9.4.3",
   r"Basis changes, scalar gates, endpoint corrections and reassembly cost $O(V((eK)^\tau+1))$ at the node.",
   r"O\bigl(V((eK)^\tau+1)\bigr)"),
  infer("S2.9.4.4",
   r"Define $q_0=\lceil\log_2W\rceil\lceil\log_m(2d)\rceil$ and $k_0=\lceil\log_md\rceil$; if $D>q_0$, apply $C$ individually on the first $q_0$ chunks (cost $O(V\log d)$) and use their concatenated bits as a row index of range $2^{q_0K}\ge W^{k_0}$.",
   r"\qquad k_0=\lceil\log_m d\rceil."),
  infer("S2.9.4.5",
   r"Padding with zero rows to a multiple of $W^{k_0}$ at most doubles the volume, and at recursion depth $j\le k_0$ the row count is divisible by $W^{k_0-j}$.",
   r"row count is divisible by \(W^{k_0-j}\)."),
  infer("S2.9.4.6",
   r"Sending row $u=Wg+w$ to role $w$ gives role streams with the same remaining shape, each of volume exactly $1/W$ of its parent's logical volume.",
   r"one role stream with volume exactly \(1/W\) of its parent's logical"),
  infer("S2.9.4.7",
   r"Fix $\beta=1/2$ and rational exponents with $0<\tau<1$, $\max\{0,\log_m(s/W)\}\le\sigma<1$, $\max\{\tau,\sigma\}<\lambda<1$ and $\tau(1+c/\beta)<\lambda$.",
   r"\tau(1+c/\beta)<\lambda."),
  infer("S2.9.4.8",
   r"Stopping when $e<d^\beta$, $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ and $F(e)=O(e)$ at leaves.",
   r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
  infer("S2.9.4.9",
   r"At an internal node $e\ge d^\beta$, so $K\le d^c\le e^{c/\beta}$ and the overhead is $O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)$.",
   r"\(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\)."),
  infer("S2.9.4.10",
   r"With $a=s/W\le m^\sigma<m^\lambda$ the internal costs sum to at most $Ce^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)$.",
   r"C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)."),
  infer("S2.9.4.11",
   r"The leaves, after $j$ levels with $u=e/m^j<d^\beta$ chunks each, contribute at most $O(a^ju)\le O(e^\sigma u^{1-\sigma})\le O(e^\sigma d^{\beta(1-\sigma)})$, using $a^j\le m^{j\sigma}=(e/u)^\sigma$.",
   r"\le O(e^\sigma d^{\beta(1-\sigma)})."),
  infer("S2.9.4.12",
   r"Writing $D-q_0=\sum_ja_jm^j$ in base $m$ gives at most $(m-1)(1+\lfloor\log_md\rfloor)$ pieces of $m^j$ chunks, whose costs add up with the row preprocessing.",
   r"Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\)."),
  infer("S2.9.4.13",
   r"The total is $O(\log(2d)[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1])=O(d^{\lambda'})$ for any fixed $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$.",
   r"\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1."),
 ],
 salient=r"The overhead per node is a small power $(eK)^\tau$, and because $K\le d^c$ with tiny $c$ it still stays below $e^\lambda$; the recursion's ratio $a/m^\lambda<1$ keeps the sum geometric.",
)

S295 = show(
 "S2.9.5",
 r"All intermediate dyadic values of a layer are exact in $p+\Delta$ fractional and $\Delta+3$ integer and sign bits per component, with $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$, $E=64(W+m+1)^3$, $B=s+E$, $\nu=\min\{j:m^j\ge B\}=11$, $C_1=20$ and $C_0=128mB^2$.",
 "Bound the arithmetic dependency depth $A(e)$ of any chain by a recurrence, convert depth into growth of denominator and modulus, and choose $\\epsilon C_1<1$ so the extra width is $o(p)$.",
 mot("The accelerated network's intermediate operators need not be contractions, so exactness requires enough guard bits for the worst chain of additions and halvings.", "explicit", r"need not be contractions."),
 [
  infer("S2.9.5.1",
   r"For the complex network put $E=64(W+m+1)^3$, $B=s+E$, $\nu=\min\{j\ge1:m^j\ge B\}$, $C_1=\max\{20,\nu+3\}$, $C_0=128mB^2$ and $\Delta=\lceil C_0d^{C_1}\rceil$.",
   r"E=64(W+m+1)^3,\qquad B=s+E,"),
  infer("S2.9.5.2",
   r"With $m=1{,}000{,}000$, $W=W_{\rm c}$ and $s=s_{\rm c}$, one has $m^{10}<B<m^{11}$, hence $\nu=11$ and $C_1=20$.",
   r"These values give \(m^{10}<B<m^{11}\), hence \(\nu=11\) and"),
  infer("S2.9.5.3",
   r"The dependency depth satisfies $A(e)\le sA(e/m)+E$ at an internal node and $A(e)\le8e$ at a leaf, since the scalar gates and corrections of one invocation take fewer than $E$ operations.",
   r"A(e)\le sA(e/m)+E"),
  infer("S2.9.5.4",
   r"For any $x\ge1$, $sx+E\le(s+E)x=Bx$, so through the at most $\lceil\log_md\rceil$ levels.",
   r"For any bound \(x\ge1\), \(sx+E\le(s+E)x=Bx\)."),
  infer("S2.9.5.5",
   r"Using $B^{k+1}\le B^2d^{\nu}$ this gives $A(e)\le8dB^{k+1}\le8B^2d^{\nu+1}$.",
   r"A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}."),
  infer("S2.9.5.6",
   r"Adding the piece concatenation, the individual kernels and the outer phases yields a total below $128mB^2d^{\nu+3}\le C_0d^{C_1}$.",
   r"&<128mB^2d^{\nu+3}\le C_0d^{C_1}."),
  infer("S2.9.5.7",
   r"A value at depth $\ell$ lies in $2^{-(p+\ell)}\mathbb Z[i]$ and has modulus at most $2^\ell$, so reserving $p+\Delta$ fractional and $\Delta+3$ integer and sign bits represents every intermediate coefficient exactly and prevents overflow.",
   r"To see how this count controls numerical size, start with disk-valued"),
  infer("S2.9.5.8",
   r"Choosing $\epsilon C_1<1$ with $d=\Theta(p^\epsilon)$ gives $\Delta=o(p)$, so the full coefficient width remains $O(p)$.",
   r"Choose \(\epsilon C_1<1\).  Since \(d=\Theta(p^\epsilon)\),"),
 ],
 frm=["fixed-point-complex-arithmetic","dyadic-rationals-and-fixed-width-numerators"],
)

S296 = infer("S2.9.6",
 r"The layer procedure returns $Q_p(\mathcal Hz)$ in the same array and component format in $O(Vd^{\lambda'})$ time, each returned coefficient lies in the unit disk and $\|Q_p(\mathcal Hz)-\mathcal Hz\|_\infty<\sqrt2\,2^{-p}$, since every row of $\mathcal H$ has absolute row sum one and truncation toward zero changes each component by less than $2^{-p}$.",
 r"coefficient order, and component format in $O(Vd^{\lambda'})$ time,")

S29 = show(
 "S2.9",
 r"A normalised butterfly layer $\mathcal H=H_0^{\otimes D}$ (with $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$) on the same bit position of $D\le d$ address chunks of $K=\lfloor d^c\rfloor$ bits, on records that are polynomials with $r$ complex coefficients in the unit disk on the grid $2^{-p}\mathbb Z[i]$, is computed exactly and truncated once in $O(Vd^{\lambda'})$ time, with $\tau=\sigma=1-2^{-50}$, $\beta=1/2$, $C_1=20$ and (as fixed for the multiplier) $c=2^{-56}$, $\epsilon=2^{-75}$, $\lambda=1-2^{-52}$, $\lambda'=1-2^{-54}$.",
 "Apply the complex network with column phase frames to groups of $m^k$ chunks, implement the binary basis changes by packed selected-bit additions, split rows among the $W$ roles, unroll the recursion, and keep every intermediate value exact with guard bits until one final truncation.",
 mot("Separate butterfly factors would require $D$ whole-array passes.", "explicit", r"factors would require $D$ whole-array passes."),
 [S24, S291, S292, S293, S294, S295, S296],
 page="simultaneous-butterfly-layer",
 frm=["phase-frame-network","packed-selected-bit-addition","fixed-point-complex-arithmetic","rank-saving-recurrence","address-chunk-interchange","array-frames","complex-numbers"],
 adds=[
  B("d","axis count","Number of address chunks (axes) that can take part in one layer, $d=\\Theta(p^\\epsilon)$."),
  B("p","precision","Number of fractional bits of the complex fixed-point grid $2^{-p}\\mathbb Z[i]$."),
  B("r","record length","Number of complex coefficients per polynomial record, $r=2^{\\Theta(p/d)}$."),
  B("\\lambda'","layer exponent","Fixed rational $1-2^{-54}$ with $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$ bounding the layer cost $O(Vd^{\\lambda'})$."),
  B("\\sigma","complex recurrence exponent","Rational $1-2^{-50}$ upper bound for the logarithmic exponent $\\log_m(s/W)$ of the complex recurrence."),
  B("\\Delta","guard width","Number $\\lceil C_0d^{C_1}\\rceil$ of extra bits reserved so intermediate dyadic values are exact."),
  B("W","wire count","Number $W_{\\rm c}=1873807244643542670000$ of wires of the complex exchange network.","count"),
  B("m","label dimension","Dimension $10^6$ of the binary label space, also the factor by which the number of axes is divided per level.","count"),
  B("s","total edge rank","Sum $s_{\\rm c}<W_{\\rm c}m$ of the residual dimensions of all edges, the number of child calls per node.","count"),
  B("V","logical volume","Number of stored data bits of the array being processed.","count"),
 ],
)

# ---------------------------------------------------------------- S2 interchange (key, bit variant)
S2A = show(
 "S2A",
 r"A fixed linear network of $W$ wires exchanging two banks with endpoint frames of rank-one shears, run on $W$ row streams of volume $V/W$, turns an exchange of width $mf$ into $s$ exchanges of width $f$ with total edge rank $s<Wm$ (strictly), so the cost per unit volume is multiplied by $s/W<m^\tau$ when the width is multiplied by $m$, with $m=h^3=10^6$ and $\tau=1-2^{-50}$.",
 "Realise the exchange as a fixed linear network that swaps two banks and restores all scratch wires; store each wire's array in a frame so that every edge needs only a shear of the address fields; label the network so the sum of the shear ranks is $s<Wm$; implement each shear with exactly as many smaller interchanges as its rank.",
 mot("This strict inequality is the source of the power saving.", "explicit", r"is the source of the power saving."),
 [S21, S22, S23, S25, S26],
 page="rank-saving-recurrence",
 frm=["tape-address-model","controlled-cyclic-shift","array-frames","subset-intersection-labels","address-shear-factorization","divide-and-conquer-and-recurrences","geometric-series-and-sums","matrices-vectors-and-linear-maps"],
 salient="The saving is a genuine power of the parameter even though the rank deficit $Wm-s$ is only about $10^{-11}$ of $Wm$: the exponent $\\tau=1-2^{-50}$ fits inside the deficit, and the strict inequality $s<Wm$ survives although the negative source projections cost $N$ extra ranks, because the decreasing edges lose only $2L<N$.",
)

S2 = show(
 "S2",
 r"Two disjoint contiguous address fields of $u$ bits of an array of logical volume $V$ can be interchanged in $O(Vu^{\tau})$ steps for the fixed exponent $\tau=1-2^{-50}<1$ (so less than a scan per bit of width), although the intermediate steps form XOR combinations of the data and the final effect is an exact permutation.",
 r"Obtain a recursion for the interchange of $e=m^k$-digit chunks from the rank-saving exchange network, solve it as a geometric sum with ratio $s/W<m^\tau$, and extend the result to arbitrary widths by supplying rows from the chunks' own high digits.",
 mot("We use the bit network to interchange two equal address chunks on tape; because the sum of the edge ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width.", "explicit", r"$m$, the resulting recurrence saves a power of the chunk width."),
 [S2A, S27] + S28["children"],
 page="address-chunk-interchange",
 frm=["rank-saving-recurrence","power-width-interchange","tape-address-model","controlled-cyclic-shift","positional-notation-in-any-radix"],
 adds=[
  B("W","wire count","Number of wires (scratch wires included) of the bit exchange network, $W_{\\rm b}=177176569091445000000$.","count"),
  B("m","label dimension","Dimension $h^3=10^6$ of the label space, which is also the factor by which the chunk width is divided per level.","count"),
  B("s","total edge rank","Sum over all edges of the rank of the shear of the edge, equal to the number of smaller interchanges per node; $s_{\\rm b}<W_{\\rm b}m$.","count"),
  B("V","logical volume","Number of stored data bits of the array being processed.","count"),
  B("\\tau","interchange exponent","Rational exponent $1-2^{-50}<1$ with $s_{\\rm b}/W_{\\rm b}<m^\\tau$ governing the interchange cost $O(Vu^\\tau)$."),
 ],
)

# ---------------------------------------------------------------- S3 ring convolution
S31 = show(
 "S3.1",
 r"For $t\mid2r$ a power of two, the transforms $(F_t^\pm z)_j=\frac1t\sum_k\omega_t^{\pm jk}z_k$ over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ with $\omega_t=y^{2r/t}$ are contractions with $F_t^+F_t^-=t^{-1}I$, and $F_t^-$ is computed by $\log_2t$ levels of $H_0$ butterflies and twiddles that are signed shifts.",
 "Use powers of $y$ as the roots of unity (multiplication by them is an isometric signed coefficient shift), prove character cancellation directly because the ring has zero divisors, and obtain the fast version by decimation in frequency.",
 mot("Roots of unity that are powers of $y$ are exact signed shifts, so no twiddle multiplication needs real arithmetic, but the ring has zero divisors so the usual division by $\\omega^j-1$ is unavailable.", "recoverable"),
 [
  infer("S3.1.1",
   r"Every power of $\omega_t$ is an isometry and each transform entry is an average of $t$ such images, so $F_t^\pm$ are contractions.",
   r"Every power of $\omega_t$ is an isometry, and each transform entry is"),
  infer("S3.1.2",
   r"For an integer $j$, $\sum_{k=0}^{t-1}\omega_t^{jk}$ equals $t$ if $t\mid j$ and $0$ otherwise, whence $F_t^+F_t^-=t^{-1}I$.",
   r"F_t^+F_t^-=t^{-1}I."),
  infer("S3.1.3",
   r"If $j=2^vj_0$ with $j_0$ odd and $v<\log_2t$, replacing $k$ by $k+t/2^{v+1}$ multiplies the sum by $y^{rj_0}=-1$, so it vanishes because the additive group of $\mathcal R_r$ has no two-torsion.",
   r"$\mathcal R_r$ has no two-torsion."),
  infer("S3.1.4",
   r"The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$, applies $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ in place, multiplies the $b=1$ output by $\omega_t^{-k}$, and recurses on the two branches of length $t/2$, which computes $F_t^-$.",
   r"the $b=1$ output by $\omega_t^{-k}$, and then apply the length-$t/2$"),
 ],
 page="synthetic-polynomial-transform",
 frm=["negacyclic-ring","discrete-fourier-transform","fft-butterflies","roots-of-unity-and-euler-s-formula","polynomials"],
 adds=[
  B("t","transform length","Power of two dividing $2r$ giving the length of the axis being transformed."),
  B("\\omega_t","synthetic root","The ring element $y^{2r/t}$, a primitive $t$th root of unity acting as a signed shift."),
 ],
)

S32 = show(
 "S3.2",
 r"The forward transform on $2^a$ points writes the entry of frequency $j$ in slot $\mathrm{rev}_a(j)$ (bit-reversed), and the opposite procedure consumes that same stored order; the two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$, so no frequency permutation is ever executed.",
 "Track which frequency bit each address slot holds after each level of the recursion, then run the recursion backwards (inverse monomial, then $H_0$) so that it starts from the stored order.",
 mot("Because pointwise multiplication commutes with applying the same permutation to both operands, the forward outputs may be multiplied in whatever order they are produced and handed unchanged to the opposite transform.", "recoverable"),
 [
  infer("S3.2.1",
   r"After all $a$ rounds the named address slots, from high to low, contain the frequency bits from low to high, so the entry $(F_t^-z)_j$ occupies slot $\mathrm{rev}_a(j)$.",
   r"After all $a$ rounds, the named slots from high to low therefore"),
  infer("S3.2.2",
   r"The recursion writes its outputs directly in this order; it does not move whole frequency indices.",
   r"directly in this order; it does not move whole frequency indices."),
  infer("S3.2.3",
   r"The procedure consuming this order traverses the recursion in reverse (smaller branches first, then the inverse monomial on the second branch, then $H_0$); as $H_0^2=I/2$ each reversed level is half the inverse of the forward level, giving composite $2^{-a}I=I/t$ with $B_tF_t^-$.",
   r"The procedure consuming this stored order traverses the recursion in"),
  infer("S3.2.4",
   r"Thus the two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$ respectively.",
   r"B_tF_t^-,\qquad F_t^+B_t^{-1},"),
 ],
 page="stored-frequency-order",
 frm=["synthetic-polynomial-transform","fft-butterflies","permutations-and-bijections"],
 salient="No bit-reversal permutation is ever carried out: the order produced by the forward transform is exactly the order consumed by the opposite transform.",
)

S33 = show(
 "S3.3",
 r"With $t_i\in\{2^{\ell-1},2^\ell\}$, $M=\prod t_i$, $T=rM$ and $K=\lfloor d^c\rfloor$, a layout permutation $L$ made of prefix-slot moves and $O(p/K)$ chunk interchanges lets each round of the multidimensional transform be one simultaneous butterfly layer; each of the forward procedure ($LBF^-_{\boldsymbol t}$) and the opposite procedure has error less than $\sqrt2\,\ell\,2^{-p}$ and costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.",
 r"Move the top bits of the long axes and the lowest $b=(\ell-1)\bmod K$ slots of every axis to a prefix, reorder the remaining $q$ chunks per axis so that the selected bit of every axis sits at one common offset of consecutive $K$-bit chunks, and then call the simultaneous layer once per round.",
 mot("To apply the simultaneous layer in a transform round, we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks.", "explicit", r"we must place the selected bits of the participating axes at a common"),
 [
  infer("S3.3.1",
   r"For $D$ axes a round applies one current $H_0$ per axis followed by one recordwise monomial $y^{E}$, $E=-\sum_i\frac{2r}{u_i}b_ik_i \pmod{2r}$, because each axis's twiddle depends only on its own address bits and commutes with the other axes' butterflies.",
   r"butterfly $\mathcal H$, followed by one recordwise monomial operation"),
  infer("S3.3.2",
   r"With $b=(\ell-1)\bmod K$ and $q=\lfloor(\ell-1)/K\rfloor$, moving the top slot of each long axis and slots $b-1,\dots,0$ of every axis to a prefix involves $D(b+1)=O(dK)$ slots and costs $O(TpdK)$.",
   r"There are at most $D(b+1)=O(dK)$"),
  infer("S3.3.3",
   r"Reordering the remaining $q$ chunks per axis from axis-major to chunk-major takes at most $Dq-1$ exchanges of width-$K$ chunks at $O(TpK^\tau)$ each, i.e. $O(Tp\,pK^{\tau-1})$ in total, since $Dq=O(p/K)$; the prefix moves and these exchanges define the layout permutation $L$.",
   r"=O\bigl(Tp\,pK^{\tau-1}\bigr)."),
  infer("S3.3.4",
   r"For a position $h$ in the remaining chunks the selected bit has offset $(h-b)\bmod K$ in each of the $D$ consecutive chunks of the same index $j$, and every combination of other address bits occurs, so the complete address set $[P]\times[2^K]^D\times[S]$ of $M$ records is presented to the layer.",
   r"For a position $h$ in the remaining chunks, the selected bit has"),
  infer("S3.3.5",
   r"The simultaneous-layer procedure applies at cost $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ over at most $\ell$ rounds.",
   r"$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total."),
  infer("S3.3.6",
   r"Rounds on prefix slots handle each participating bit individually (move it before the polynomial suffix, scan pairs of records into half-sums and half-differences) at $O(Tp)$ each, at most $b+1\le K$ of them, for $O(TpdK)$, with $p+D+O(1)$ bits sufficing.",
   r"most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$."),
  infer("S3.3.7",
   r"Multiplication by $y^E$ with $E=er+s$, $0\le s<r$, splits the coefficient list before position $r-s$, puts the tail before the head, negates the moved tail and applies the sign $(-1)^e$, in $O(rp)$ per record and with no sort.",
   r"Split the coefficient list before position $r-s$, put its tail"),
  infer("S3.3.8",
   r"Truncation toward zero is odd and acts separately on every part, so $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$: the call sequence equals one truncation after the exact contraction round.",
   r"J_EQ_p(\mathcal H z)=Q_p(J_E\mathcal H z)."),
  infer("S3.3.9",
   r"A contraction does not increase the error already present and one truncation adds less than $\sqrt2\,2^{-p}$, so starting from zero error at most $\ell$ rounds give error less than $\sqrt2\,\ell\,2^{-p}$ and disk output; layout permutations are isometries.",
   r"zero error, at most $\ell$ rounds therefore"),
 ],
 page="transform-tape-layout",
 frm=["simultaneous-butterfly-layer","address-chunk-interchange","stored-frequency-order","synthetic-polynomial-transform","fixed-point-complex-arithmetic","negacyclic-ring","tape-address-model"],
 adds=[
  B("T","padded box size","Total number $rM$ of entries of the padded array, with $Tp=\\Theta(n)$ bits."),
  B("\\ell","record exponent","Base-two logarithm of the record length $r$, equal to the number of butterfly rounds on a long axis."),
  B("M","ring-array size","Number $\\prod_i t_i=T/r$ of polynomial records in the array."),
  B("L","layout permutation","Positional permutation of record addresses (prefix moves and chunk exchanges) preceding the rounds."),
 ],
)

S34 = show(
 "S3.4",
 r"Two polynomials $f,g\in\mathcal R_r$ with disk-grid coefficients (given with $p$ fractional bits, $r=2^\ell<2^p$) are multiplied exactly and returned as $Q_p(fg/r)$, error less than $\sqrt2\,2^{-p}$ from $fg/r$, in $O(rp\log(rp))$ time using four integer products by the $O(N\log N)$ multiplier.",
 "Evaluate each coefficient polynomial at $B_0=2^{4p}$ with centred (signed) carries, multiply the four resulting integer pairs, and recover the product coefficients by centred residues modulo $B_0$, which are unambiguous because the coefficients are small.",
 mot("Evaluating at a large power of two (Kronecker substitution) turns a short polynomial product into one integer product, so the established $O(n\\log n)$ multiplier can be used as an ordinary subroutine on the short records; signs need centred carries.", "recoverable"),
 [
  infer("S3.4.1",
   r"Write $f=2^{-p}(a+ib)$, $g=2^{-p}(c+ie)$ with integer polynomials of degree $<r$ and coefficients at most $2^p$ in absolute value, and put $B_0=2^{4p}$ and $A_u=u(B_0)$; each $|A_u|<B_0^r/2$ fits in $4pr$ bits.",
   r"Set $B_0=2^{4p}$"),
  infer("S3.4.2",
   r"Every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so after removing lower coefficients the next one is identified by its centred residue modulo $B_0$.",
   r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
  infer("S3.4.3",
   r"To form $A_u$ with signed coefficients, take digits $d_j\equiv u_j+\gamma_j\pmod{B_0}$ with carry $\gamma_{j+1}\in\{-1,0\}$; the blocks are then a two's-complement encoding of $A_u$ and are complemented and incremented when negative.",
   r"d_j\equiv u_j+\gamma_j\pmod{B_0},\quad 0\leq d_j<B_0,"),
  infer("S3.4.4",
   r"Extraction: let $\widehat h_j\in[-B_0/2,B_0/2)$ be congruent to $q_j+\rho_j$ modulo $B_0$ and put $\rho_{j+1}=(q_j+\rho_j-\widehat h_j)/B_0$; by the separation bound $\widehat h_j=h_j$, and the carry stays in $\{0,1\}$.",
   r"integer in $[-B_0/2,B_0/2)$ congruent to $q_j+\rho_j$ modulo $B_0$,"),
  infer("S3.4.5",
   r"The real and imaginary numerator streams are $ac-be$ and $ae+bc$; reducing modulo $y^r+1$ subtracts the coefficient at $j+r$ from the one at $j$, so each $H_j$ is a sum of exactly $r$ signed products and $|H_j|\le r2^{2p}$.",
   r"coefficient at $j+r$ from the one at $j$ for $0\leq j<r$, treating"),
  infer("S3.4.6",
   r"Four exact integer products dominate the linear packing, extraction, wrapping and truncation passes, giving $O(rp\log(rp))$.",
   r"Four exact integer products dominate the linear"),
 ],
 page="signed-packing",
 frm=["n-log-n-barrier","negacyclic-ring","convolution","positional-notation-in-any-radix","integer-division-with-remainder-floor-and-ceiling"],
)

S3_conv = [
  infer("S3.5",
   r"For arrays over $\mathcal R_r$ on axes $\prod_i\mathbb Z/t_i\mathbb Z$ the normalised convolution $\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}$ is a bilinear contraction: each output coefficient averages $rM$ signed scalar products.",
   r"$rM$ signed scalar products, and $\mathcal M_r$ is a bilinear"),
  infer("S3.6",
   r"Since $F^-_{\boldsymbol t}(f*g)=M(F^-_{\boldsymbol t}f)(F^-_{\boldsymbol t}g)$ and $F^+_{\boldsymbol t}F^-_{\boldsymbol t}=I/M$, one has $MF^+_{\boldsymbol t}\bigl(\tfrac{(F^-f)(F^-g)}{r}\bigr)=\frac{f*g}{rM}$.",
   r"=\frac{f*g}{rM}."),
  infer("S3.7",
   r"The record permutation $LB$ commutes with the pointwise polynomial product $P(u,v)=uv/r$, so the opposite procedure applied to the product of the retained-order outputs equals $F^+_{\boldsymbol t}P(F^-_{\boldsymbol t}f,F^-_{\boldsymbol t}g)$ and no permutation is executed.",
   r"Since $LB$ permutes records and leaves their polynomial suffixes"),
  show("S3.8",
   r"The computed normalised convolution has error less than $\sqrt2\,M(3\ell+1)2^{-p}$ (with $\delta=\sqrt2\,\ell\,2^{-p}$ and $\eta=\sqrt2\,2^{-p}$) and, when one operand has norm at most $\rho$ and the error is at most $1-\rho$, is again a disk array.",
   "Chain the errors: each forward transform has error less than $\\delta$, the bilinear contraction $P$ doubles it, the truncation adds $\\eta$, the opposite transform (a contraction) passes it on while adding $\\delta$, and the final exact scaling multiplies by $M$.",
   mot("Composing approximations of linear contractions adds their errors, so the final bound is a sum of the stage errors times the exact scale.", "recoverable"),
   [
    infer("S3.8.1",
     r"With exact forward outputs $u,v$ and computed ones $\widetilde u,\widetilde v$ (all in the disk, each error less than $\delta$), bilinearity gives $\|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty<2\delta$.",
     r"\|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty"),
    infer("S3.8.2",
     r"After the truncation $Q_p$, $\|\widetilde z-z_*\|_\infty<2\delta+\eta$.",
     r"$\|\widetilde z-z_*\|_\infty<2\delta+\eta$."),
    infer("S3.8.3",
     r"The opposite transform is a contraction and adds at most $\delta$, so $\|\widetilde h-\mathcal T_+z_*\|_\infty<3\delta+\eta$.",
     r"<3\delta+\eta."),
    infer("S3.8.4",
     r"Multiplying exactly by $M$ gives error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$.",
     r"The final exact multiplication by $M$ therefore gives error less than"),
   ]),
  infer("S3.9",
   r"There are $M=T/r$ pointwise polynomial products at $O(Tp\log(rp))$ in all; with the three transforms the cost is $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.",
   r"is $O(Tp\log(rp))$; the three transform costs are as stated, and"),
]

S3 = show(
 "S3",
 r"The normalised cyclic convolution $\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ on axes of lengths $t_i\in\{r/2,r\}$ is computed with error less than $\sqrt2\,M(3\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.",
 "Use the convolution theorem for the synthetic transforms: two forward transforms kept in their stored order, a pointwise polynomial product divided by $r$ (signed packing with the $O(N\\log N)$ multiplier), the opposite transform, and an exact scale by $M$.",
 mot("A convolution becomes pointwise products after a Fourier-type transform, and the pointwise products are products of short polynomials of $O(rp)$ bits each, to which the known $O(N\\log N)$ multiplier can be applied as an ordinary subroutine with negligible log factor.", "recoverable"),
 [S31, S32, S33, S34] + S3_conv,
 page="normalized-ring-convolution",
 frm=["synthetic-polynomial-transform","stored-frequency-order","transform-tape-layout","signed-packing","contraction-error-propagation","simultaneous-butterfly-layer","negacyclic-ring","convolution","n-log-n-barrier"],
)

# ---------------------------------------------------------------- S4 source transform
S41 = show(
 "S4.1",
 r"For coprime lengths $s<t$ with $\theta=t/s-1>p/\alpha^4$ there are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, where $(P_su)_j=u_{tj}$, $(P_tv)_k=v_{-sk}$, computable with error less than $p^2$ in time $O(tp^{3/2+\delta}\alpha)$.",
 "Follow the Gaussian resampling argument: two Gaussian maps $\\mathsf S,\\mathsf T$ with $\\mathsf TP_sF_s=P_tF_t\\mathsf S$, an approximate left inverse of $\\mathsf T$ by a Neumann series, and normalisations making both maps contractions, keeping the two coordinate permutations inside the identity.",
 mot("Its usual implementation sorts twice on each coordinate; retaining both permutations in the transform formula avoids executing them.", "explicit", r"connects these two shapes. Its usual implementation sorts twice on each"),
 [
  infer("S4.1.1",
   r"The Gaussian maps are $(\mathsf Su)_k=\frac1\alpha\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j$ and $(\mathsf Tu)_k=\sum_je^{-\pi\alpha^2(tj/s-k)^2}u_j$.",
   r"(\mathsf S u)_k=\frac1\alpha\sum_{j\in\mathbb Z}"),
  infer("S4.1.2",
   r"The exact Gaussian identity is $\mathsf TP_sF_s=P_tF_t\mathsf S$.",
   r"\mathsf T P_sF_s=P_tF_t\mathsf S,"),
  infer("S4.1.3",
   r"With $N=C\mathsf T\mathsf D$ (where $C$ selects coordinates $q_j$ nearest to $tj/s$ and $\mathsf D$ is diagonal), $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}<1/2$.",
   r"\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}."),
  infer("S4.1.4",
   r"Hence $N$ is invertible by the Neumann series.",
   r"by the Neumann series. Put"),
  infer("S4.1.5",
   r"With $\mathsf S'=\mathsf S/2$, $\mathsf J'=N^{-1}/2$ and $\mathsf D'=2^{-(2\alpha^2-2)}\mathsf D$, the normalisations multiply to $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$.",
   r"$2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$. Hence"),
  infer("S4.1.6",
   r"Setting $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$ gives contractions with $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$, i.e. $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$.",
   r"=2^{-2\alpha^2}P_sF_s,"),
  infer("S4.1.7",
   r"The ordered numerical maps have errors and times $\widetilde{\mathsf S}'$: $16p$, $O(tp^{3/2+\delta}\alpha)$; $\widetilde{\mathsf J}'$: $3p^2/4$, same time; $\widetilde{\mathsf D}'$: $4$, $O(tp^{1+\delta})$.",
   r"\widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)\\"),
  infer("S4.1.8",
   r"The selection $C$ picks an ordered subsequence ($q_0=0$, $q_{s-1}<t$, $q_{j+1}>q_j$ because $t/s>1$), generated in order with $O(p)$ work per index, at zero numerical error.",
   r"observe that $q_0=0$, $q_{s-1}<t$, and $q_{j+1}>q_j$,"),
  infer("S4.1.9",
   r"With $\widetilde A=\widetilde{\mathsf S}'$ and $\widetilde B_0=\widetilde{\mathsf D}'\widetilde{\mathsf J}'C$ the errors are less than $16p<p^2$ and $4+3p^2/4<p^2$, and the costs add to $O(tp^{3/2+\delta}\alpha)$.",
   r"Contraction of the exact maps yields errors less than $16p<p^2$ and"),
 ],
 page="gaussian-resampling",
 frm=["contraction-error-propagation","discrete-fourier-transform","exponential-logarithm-and-gaussian-function","permutations-and-bijections","n-log-n-barrier","primes-coprimality-and-gcd"],
 adds=[
  B("\\alpha","Gaussian width parameter","Integer $2\\le\\alpha<\\sqrt p$ controlling the width of the Gaussian weights."),
  B("\\theta","length ratio excess","The quantity $t/s-1$, required to exceed $p/\\alpha^4$."),
 ],
 salient="The identity $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ keeps both coordinate permutations $P_s,P_t$ inside the formula, so neither is ever executed as a sort.",
)

S42 = show(
 "S4.2",
 r"Tensoring the one-dimensional identity over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$, and the linewise implementations of $\mathcal A$ and $\mathcal B_0$ on the padded box of $T=\prod t_i$ entries have error less than $dp^2$ and time $O(dTp^{3/2+\delta}\alpha)$, plus $O(Tp\,d^2(1+\ell^\tau))$ to expose and restore axes.",
 "Embed the source in the padded power-of-two box with zeros outside the valid coordinates, apply the one-dimensional map line by line along one axis at a time, and expose each axis as the innermost field with chunk interchanges.",
 mot("The tensor product of the one-dimensional identity needs the maps applied along one axis at a time, and the physical axis fields must be moved to the innermost position, which the chunk interchange does cheaply.", "recoverable"),
 [
  infer("S4.2.1",
   r"Tensoring gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $R=\bigotimes P_{s_i}$, $Q=\bigotimes P_{t_i}$ and $\gamma=2d\alpha^2$.",
   r"=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A,"),
  infer("S4.2.2",
   r"The total time in the one-dimensional algorithms for both maps is $O(dTp^{3/2+\delta}\alpha)$, since axis $i$ has at most $T/t_i$ lines each costing $O(t_ip^{3/2+\delta}\alpha)$.",
   r"$O(dTp^{3/2+\delta}\alpha)$, with a constant independent of $d$."),
  infer("S4.2.3",
   r"Composing the $d$ axis maps (each a contraction acting independently on its valid lines) gives error less than $dp^2$.",
   r"Composing the $d$ axis maps gives error less than $dp^2$."),
  infer("S4.2.4",
   r"Exposing and restoring one axis needs $O(d)$ adjacent interchanges, each costing $O(Tp(1+\ell^\tau))$ (equal widths by the chunk interchange; unequal widths by moving the extra leading bit), so all axes cost $O(Tp\,d^2(1+\ell^\tau))$.",
   r"costs $O(Tp(1+\ell^\tau))$. Exposing and restoring one axis needs"),
 ],
 frm=["address-chunk-interchange"],
)

S43 = show(
 "S4.3",
 r"With $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$, $QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}{T}$: the middle transform, including its target permutation, is two pointwise chirp phases around one cyclic convolution with the chirp.",
 "Check that the coefficient of $u_{\\boldsymbol k}$ on the right is $\\frac1T\\exp(2\\pi i\\sum s_ij_ik_i/t_i)$, the entry of $QF_{\\boldsymbol t}$, using $-(j-k)^2+j^2+k^2=2jk$ in the exponent.",
 mot("The chirp identity below performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array.", "explicit", r"multiplications. The chirp identity below performs the frequency change"),
 [
  infer("S4.3.1",
   r"The chirp $a$ has period $t_i$ in coordinate $i$, because replacing $j_i$ by $j_i+t_i$ changes the exponent by $-\pi is_i(2j_i+t_i)$, an integral multiple of $2\pi i$ (here every $t_i$ is even).",
   r"Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by"),
  infer("S4.3.2",
   r"The coefficient of $u_{\boldsymbol k}$ on the right side is $\frac1T\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}=\frac1T\exp(2\pi i\sum_is_ij_ik_i/t_i)$.",
   r"=\frac1T\exp\left(2\pi i\sum_i"),
  infer("S4.3.3",
   r"This is exactly the coefficient of $QF_{\boldsymbol t}$, because $Q$ reads frequency $(-s_ij_i)_i$ from the negative-sign transform.",
   r"This is precisely the coefficient in $QF_{\boldsymbol t}$, because"),
 ],
 page="bluestein-chirp",
 frm=["discrete-fourier-transform","convolution","roots-of-unity-and-euler-s-formula","exponential-logarithm-and-gaussian-function"],
)

S44 = show(
 "S4.4",
 r"Because each $t_i$ is a unit modulo $s_i$, the source permutation $R$ cancels: $(RF^+_{\boldsymbol s})[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=\frac{u*v}{S^2}$ with $S=\prod s_i$.",
 "Show that dilation by a unit commutes with $F^+$ up to inversion ($F_q^+R_c=R_c^{-1}F_q^+$), hence $RF^+R=F^+$, that permutations commute with pointwise products, and then apply the convolution rule.",
 mot("The retained permutation costs nothing if it cancels between the two forward transforms, the pointwise product and the opposite-sign transform, so a full sort of the array is never needed.", "recoverable"),
 [
  infer("S4.4.1",
   r"For a unit $c$ modulo $q$ and $(R_cz)_j=z_{cj}$, substituting $h=ck$ in the Fourier sum gives $F_q^+R_c=R_c^{-1}F_q^+$.",
   r"For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$. Substituting $h=ck$"),
  infer("S4.4.2",
   r"Each $t_i$ is a unit modulo $s_i$, so tensoring gives $F^+_{\boldsymbol s}R=R^{-1}F^+_{\boldsymbol s}$, hence $RF^+_{\boldsymbol s}R=F^+_{\boldsymbol s}$, and a coordinate permutation commutes with pointwise products, so $RF^+_{\boldsymbol s}[R(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)]=F^+_{\boldsymbol s}(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)$.",
   r"Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives"),
  infer("S4.4.3",
   r"With the normalised convolution rule $F_{\boldsymbol s}(u*v)=S\,(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$ and $F^+_{\boldsymbol s}F_{\boldsymbol s}=I/S$, the two normalisations give $F^+_{\boldsymbol s}(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=\frac{u*v}{S^2}$.",
   r"$F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$. The two normalizations give"),
 ],
 page="permutation-cancellation",
 frm=["gaussian-resampling","discrete-fourier-transform","convolution","permutations-and-bijections","modular-arithmetic","primes-coprimality-and-gcd"],
 salient="The permutation $R$ appears once in each of the three transforms (two forward, one opposite-sign) yet leaves no trace in the product.",
)

S45 = show(
 "S4.5",
 r"The computed source transform is $\widetilde{\mathscr F}=2^\gamma\mathcal B_0\widetilde{\mathscr C}\mathcal A$ with chirp transform $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,Q_p(\overline{\widetilde a}\cdot x)))$; its exact counterpart is $RF_{\boldsymbol s}$ on the padded box.",
 "Compose the linewise Gaussian map $\\mathcal A$, the chirp transform (two endpoint phases around a complex convolution of length $T$ on the padded box), the linewise map $\\mathcal B_0$ and the exact power-of-two scale $2^\\gamma$.",
 mot("The source Fourier transform is by the tensor identity a composition of linewise resampling maps and the middle transform, and the middle transform is a chirp convolution.", "recoverable"),
 [
  infer("S4.5.1",
   r"The chirp phase numerator at tensor address $j$ is computed modulo $2r$ as $-\sum_is_ij_i^2(r/t_i)$, with $O(p)$-bit integers.",
   r"-\sum_i s_i j_i^2(r/t_i)\pmod{2r}.",
   deferred=True),
  infer("S4.5.2",
   r"For a disk-grid target tensor $x$ of norm at most $.6$ the chirp transform forms $x_0=Q_p(\overline{\widetilde a}\cdot x)$, then $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$, then $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$.",
   r"x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),",
   deferred=True),
  infer("S4.5.3",
   r"The exact counterpart of the source transform is $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$.",
   r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A",
   deferred=True),
  infer("S4.5.4",
   r"By the tensor identity this equals $RF_{\boldsymbol s}$ on the prime-length source stored in the padded box, and the opposite-sign procedure is $\widetilde{\mathscr F}^+(z)=\overline{\widetilde{\mathscr F}(\overline z)}$.",
   r"=RF_{\boldsymbol s}.",
   deferred=True),
 ],
 frm=["coefficient-twist","normalized-ring-convolution","bluestein-chirp","gaussian-resampling","permutation-cancellation"],
)

S4 = show(
 "S4",
 r"A source Fourier transform $RF_{\boldsymbol s}$ on pairwise coprime lengths $s_i$ is computed on the padded power-of-two box of $T$ entries by linewise Gaussian maps $\mathcal A$, a chirp convolution of length $T$, linewise $\mathcal B_0$ and an exact scale $2^\gamma$, with the source and target permutations left inside the formula so that no full sort is executed and the source permutation cancels across the two forward transforms, the pointwise product and the opposite-sign transform.",
 "Replace the length-$s_i$ transforms by Gaussian resampling to power-of-two lengths $t_i$, carry out the middle power-of-two transform with Bluestein's chirp as a convolution, and keep every coordinate permutation in the formula, where the source permutation cancels.",
 mot("The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two; Gaussian resampling connects these two shapes.", "explicit", r"whereas the synthetic transforms use powers of two. Gaussian resampling"),
 [S41, S42, S43, S44, S45],
 page="tensor-source-transform",
 frm=["gaussian-resampling","bluestein-chirp","permutation-cancellation","coefficient-twist","normalized-ring-convolution","address-chunk-interchange","contraction-error-propagation","discrete-fourier-transform"],
 adds=[
  B("\\gamma","source scale exponent","The integer $2d\\alpha^2$ giving the exact power-of-two scale $2^\\gamma$ of the source transform."),
  B("R","source permutation","The tensor product of the coordinate permutations $P_{s_i}$ retained in the transform identity."),
 ],
)

# ---------------------------------------------------------------- S5 assembly
S51 = show(
 "S5.1",
 r"For input length $n$ choose $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$, axis lengths $t_i\in\{r/2,r\}$ with $\prod t_i=T$ and distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$, $\eta=1/(4d)$, $\alpha=\lceil(12d^2b)^{1/4}\rceil$ and $\gamma=2d\alpha^2$; then $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $T/2<S<T$ and every hypothesis of the earlier lemmas holds.",
 "Fix rational exponents once and for all, derive all sizes from $n$, and check each hypothesis (prime counts, ratio separation, super-polynomial $r$) against them.",
 mot("The distinct prime lengths $s_i$ must be close to the powers of two $t_i$: their product must occupy a fixed fraction of the padded box, while each ratio $t_i/s_i$ must leave enough separation for resampling.", "explicit", r"The distinct prime lengths $s_i$ must be close to the powers of two"),
 [
  infer("S5.1.1",
   r"The fixed rational exponents are $\tau=\sigma=1-2^{-50}$, $\beta=1/2$, $\delta=1/16$, $\lambda=1-2^{-52}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$; they are deliberately conservative and satisfy $\epsilon C_1<1$, $\tau(1+c/\beta)<\lambda$ and $\sigma+\beta(1-\sigma)=1-2^{-51}<\lambda<\lambda'<1$.",
   r"\lambda=1-2^{-52},\qquad c=2^{-56},\qquad"),
  infer("S5.1.2",
   r"Put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $K=\lfloor d^c\rfloor$.",
   r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,"),
  infer("S5.1.3",
   r"Take the power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$, and choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others $r$, with the last axis of length $r$.",
   r"Take the power of two $T$ in $[4n/b,8n/b)$, and let"),
  infer("S5.1.4",
   r"These give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$, with comparison constants $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, $C_\ell=1$.",
   r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad"),
  infer("S5.1.5",
   r"Set $\alpha=\lceil(12d^2b)^{1/4}\rceil$, $\gamma=2d\alpha^2$ and $\eta=1/(4d)$.",
   r"\alpha=\left\lceil(12d^2b)^{1/4}\right\rceil,"),
  infer("S5.1.6",
   r"One gets $\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}$, so $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$.",
   r"\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}."),
  infer("S5.1.7",
   r"By the prime-interval estimate (for $0<\eta<1/4$ and $x>e^{2/\eta}$ the interval $((1-2\eta)x,(1-\eta)x]$ contains at least $\eta x/(2\log x)$ primes) applied to $x=r/2$ and $x=r$, there are more than $d$ primes in each disjoint interval, so distinct odd primes with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ exist.",
   r"(1-2\eta)t_i<s_i\leq(1-\eta)t_i."),
  infer("S5.1.8",
   r"Multiplying the lower bounds and applying Bernoulli's inequality gives $S/T>(1-\frac1{2d})^d>\frac12$, so $T/2<S<T$.",
   r"this gives $T/2<S<T$."),
  infer("S5.1.9",
   r"Since $\theta_i=t_i/s_i-1\ge\eta/(1-\eta)>\eta$, one has $\alpha^4\theta_i>3db\ge6b=p$, and $t_i\le T<2^p$, so every hypothesis of the resampling lemma holds.",
   r"\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p."),
  infer("S5.1.10",
   r"The deterministic prime search by trial division costs $O(dr^{3/2}\mathrm{poly}(p))$, whose logarithm is $o(p)$, so it takes $n^{o(1)}=o(n)$ time.",
   r"Since $p=6\lceil\log_2 n\rceil=\Theta(\log n)$, the search takes"),
 ],
 page="parameter-regime",
 frm=["primes-coprimality-and-gcd","exponential-logarithm-and-gaussian-function","integer-division-with-remainder-floor-and-ceiling","asymptotic-notation-beyond-big-o"],
 adds=[
  B("b","digit width","Number $\\lceil\\log_2n\\rceil$ of bits per radix digit."),
  B("t_i","power-of-two axis length","Length of axis $i$, equal to $r/2$ or $r$, with $\\prod_it_i=T$."),
  B("s_i","prime source length","Distinct odd prime just below $t_i$, the length of source axis $i$."),
  B("S","source size","Product $\\prod_is_i$ of the prime lengths, satisfying $T/2<S<T$."),
  B("\\eta","relative gap","The ratio $1/(4d)$ fixing how far below $t_i$ the prime $s_i$ lies."),
 ],
 salient="The fixed exponents are extremely small ($\\epsilon=2^{-75}$, $c=2^{-56}$) yet they keep $r$ larger than every power of $p$ while making $d$ grow, which is all that the savings need.",
)

S52 = show(
 "S5.2",
 r"Writing each $n$-bit input as a polynomial in $2^b$ with $q=\lceil n/b\rceil$ digits, the product has degree at most $2q-2<2n/b\le T/2<S$, so convolution modulo $x^S-1$ has no wraparound, and each product coefficient obeys $0\le c_j\le q(2^b-1)^2<2^{3b}$.",
 "Count the degree and size of the digit convolution, using $q\\le n\\le2^b$.",
 mot("The integer product equals the digit polynomial product evaluated at $2^b$, so after the convolution only carries have to be propagated.", "recoverable"),
 [
  infer("S5.2.1",
   r"Write the two inputs as polynomials in $2^b$, each with $q=\lceil n/b\rceil$ nonnegative digits.",
   r"Write the two inputs as polynomials in $2^b$, each with"),
  infer("S5.2.2",
   r"Their product has degree at most $2q-2<2n/b\le T/2<S$, so cyclic convolution modulo $x^S-1$ produces no nonzero wraparound.",
   r"2q-2<2n/b\le T/2<S."),
  infer("S5.2.3",
   r"Every product coefficient satisfies $0\le c_j\le q(2^b-1)^2<2^{3b}$, since $q\le n\le2^b$.",
   r"0\le c_j\le q(2^b-1)^2<2^{3b},"),
 ],
 page="radix-digit-reduction",
 frm=["convolution","positional-notation-in-any-radix","polynomials","schoolbook-and-karatsuba-multiplication","integer-division-with-remainder-floor-and-ceiling"],
)

S53 = show(
 "S5.3",
 r"The map $\Phi:\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$, $x\mapsto\prod x_i^{\mu_i}$ with $P_i=\prod_{j<i}s_j$ and $\mu_i=P_i^{-1}\bmod s_i$, is an algebra isomorphism preserving cyclic convolution, sends index $k=\sum a_jP_j$ to coordinates $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, and with its padding and inverse costs $O(Tp\,d^2(1+\ell^\tau))$.",
 "Show that $\\Phi$ respects $x^S=1$ and maps the powers of $x$ bijectively onto the monomials (Chinese remainder theorem), then implement it as triangular controlled cyclic shifts of the valid target interval, processing targets in the order $d,d-1,\\dots,1$ after reordering the padded axes.",
 mot("Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution; coordinates with these powers make the change of order a sequence of controlled cyclic shifts.", "explicit", r"The following map uses that"),
 [
  infer("S5.3.1",
   r"Since $x\mapsto\prod x_i^{\mu_i}$ respects $x^S=1$, it defines an algebra map; the image of $x$ has order $S$ because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all target monomials once and $\Phi$ is an isomorphism preserving cyclic convolution.",
   r"$\Phi$ is an isomorphism and preserves cyclic convolution."),
  infer("S5.3.2",
   r"For $k=\sum_ja_jP_j$ with $0\le a_j<s_j$, the coordinate in axis $i$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, since terms with $j>i$ are divisible by $s_i$ and $\mu_iP_i\equiv1$.",
   r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}."),
  infer("S5.3.3",
   r"After reordering the padded axes to $(a_1,\dots,a_d)$, targets are updated in the order $i=d,d-1,\dots,1$, so when target $i$ is updated its lower-index controls still hold the original digits.",
   r"order $i=d,d-1,\ldots,1$ using"),
  infer("S5.3.4",
   r"On a fixed control prefix each update rotates the valid target interval $[0,s_i)$ and fixes $[s_i,t_i)$, a bijection of the padded box that preserves the valid set and its complement, so zero padding remains zero.",
   r"zero padding remains zero after every step."),
  infer("S5.3.5",
   r"Each triangular update is a prefix-controlled cyclic shift: split the valid interval into two consecutive pieces and merge them in the opposite order; offsets for the at most $T/t_i$ prefixes cost $o(Tp)$ since $r$ exceeds every fixed power of $p$.",
   r"two consecutive pieces, and merge those pieces in the opposite order."),
  infer("S5.3.6",
   r"Reversing the order of the $d$ axes of width $\ell$ or $\ell-1$ uses $O(d^2)$ chunk interchanges (with one extra bit move when widths differ), so $\Phi$, its inverse and their padding operations cost $O(Tp\,d^2(1+\ell^\tau))$.",
   r"their padding operations cost"),
 ],
 page="crt-axis-map",
 frm=["controlled-cyclic-shift","address-chunk-interchange","tape-address-model","convolution","modular-arithmetic","primes-coprimality-and-gcd","polynomials"],
 adds=[
  B("P_i","prefix product","Integer product $\\prod_{j<i}s_j$ of the earlier source lengths."),
  B("\\mu_i","inverse of prefix product","Inverse of $P_i$ modulo $s_i$, used as the exponent of $x_i$ in $\\Phi$."),
  B("\\Phi","CRT map","Algebra isomorphism from the cyclic polynomial ring modulo $x^S-1$ to the product of cyclic axes."),
 ],
)

S54 = show(
 "S5.4",
 r"With $\zeta=e^{\pi i/r}$, the map $\Theta:\mathbb C[x_d]/(x_d^r-1)\to\mathcal R_r$, $x_d\mapsto\zeta y$, multiplies coefficient $k$ by $\zeta^k$ and is an isomorphism preserving the sup norm, so the normalised complex cyclic convolution is $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$, computed with twist cost $O(Tp^{1+\delta})$.",
 "Twist the last cyclic coordinate by $\\zeta^k$ so that the negative wrap of the ring $\\mathcal R_r$ becomes the original cyclic wrap after untwisting, and apply the ring convolution on the other $d-1$ axes.",
 mot("The negacyclic ring $y^r+1$ supplies the signed shifts that the fast transform needs, while the chirp identity needs an ordinary cyclic convolution; the twist converts one to the other at the price of a diagonal scaling.", "recoverable"),
 [
  infer("S5.4.1",
   r"$\Theta$ is well defined since $(\zeta y)^r=(-1)(-1)=1$, diagonal in the monomial bases, hence an isomorphism with inverse multiplying coefficient $k$ by $\zeta^{-k}$.",
   r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."),
  infer("S5.4.2",
   r"For $k+l=j+hr$ with $h\in\{0,1\}$, a twisted product term after negacyclic reduction has factor $\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
   r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j."),
  infer("S5.4.3",
   r"With the identification $\iota$ of a scalar array with $M$ ring records and $D_\pm$ multiplying by $\zeta^{\pm k}$, the ring convolution on the first $d-1$ axes gives the scalar convolution on all $d$ axes, divided by $T$.",
   r"Here $\mathcal M_r$ convolves the first $d-1$ axes over $\mathcal R$,"),
  infer("S5.4.4",
   r"In the machine, with disk-grid approximations $\widetilde\theta^\pm_k$ of $\zeta^{\pm k}$, the computed convolution is $f'=Q_p(\widetilde\theta^+\cdot f)$, $g'=Q_p(\widetilde\theta^+\cdot g)$, $h'=\widetilde{\mathcal M}_r(\iota f',\iota g')$ and $Q_p(\widetilde\theta^-\cdot\iota^{-1}h')$.",
   r"h'&=\widetilde{\mathcal M}_r(\iota f',\iota g'),"),
  infer("S5.4.5",
   r"Generating every phase factor anew costs $O(p^{1+\delta})$ per coefficient, so the total twist cost is $O(Tp^{1+\delta})$.",
   r"twist cost $O(Tp^{1+\delta})$."),
 ],
 page="coefficient-twist",
 frm=["negacyclic-ring","convolution","roots-of-unity-and-euler-s-formula","complex-numbers"],
)

S55 = show(
 "S5.5",
 r"The algorithm converts the input to $b$-bit digits, applies $\Phi$, computes two source transforms, multiplies pointwise, applies one opposite transform, scales by $S$ twice, rounds, applies $\Phi^{-1}$ and propagates carries, outputting exactly $2n$ bits of the product.",
 "Run the six listed operations and verify that the two occurrences of $S$ undo the normalisations, so that the exact counterpart of the pipeline gives $2^{2b+4}(u*v)$ whose preimage under $\\Phi$ is the integer coefficient convolution.",
 mot("The pointwise product of two transforms has the retained source permutation cancel (so the exact result is $(u*v)/S^2$), and the two scalings by $S$ remove the transform normalisations while $2^{2b+4}$ removes the digit scales.", "recoverable"),
 [
  infer("S5.5.1",
   r"Read each operand backward in groups of $b$ bits to obtain the digits $a_0,\dots,a_{q-1}$; for digit $a_j$ write the grid numerator $a_j2^{p-b-2}$ in a signed $(p+2)$-bit real word and a zero imaginary word (value $a_j2^{-b-2}$), and append $S-q$ zero records.",
   r"For digit $a_j$, write the exact grid numerator"),
  infer("S5.5.2",
   r"Apply the coefficient-address map $\Phi$ with its padded layout to obtain source arrays $u,v$ of exact $p$-bit grid values of norm less than $1/4$.",
   r"\item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain"),
  infer("S5.5.3",
   r"Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.",
   r"\item Compute $\widetilde{\mathscr F}(u)$ and"),
  infer("S5.5.4",
   r"Multiply corresponding complex coefficients exactly and truncate toward zero to $p$ fractional bits, giving $z$.",
   r"\item Multiply corresponding complex coefficients exactly and truncate"),
  infer("S5.5.5",
   r"Compute $\widetilde{\mathscr F}^+(z)$ and multiply the numerators exactly by $S$, giving the dyadic array $\widetilde w$ in signed width $w_{\rm c}+b$.",
   r"\item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid"),
  infer("S5.5.6",
   r"Multiply the numerators of $\widetilde w$ exactly by $2^{2b+4}S$, round the real values to the nearest integers, write each valid coefficient in a signed $(3b+1)$-bit word and padded addresses as zero, then apply $\Phi^{-1}$ with removal of padding.",
   r"\item Multiply the grid numerators of $\widetilde w$ exactly by"),
  infer("S5.5.7",
   r"Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits most significant first.",
   r"\item Propagate radix-$2^b$ carries in increasing coefficient order."),
  infer("S5.5.8",
   r"The two occurrences of $S$ undo different normalisations: after the three transforms the exact counterpart is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$, and the second scale gives $2^{2b+4}(u*v)$.",
   r"counterpart after the three transforms is $(u*v)/S^2$, so after the"),
 ],
 frm=[],
)

S5 = show(
 "S5",
 r"Two $n$-bit integers are multiplied by splitting them into $b$-bit digits, mapping the digit convolution by $\Phi$ onto cyclic axes of the distinct prime lengths $s_i$, computing it with two forward source transforms $\widetilde{\mathscr F}$, a pointwise product and one opposite transform, rescaling, rounding and propagating carries, with all sizes fixed by $n$.",
 "Fix parameters from $n$, reduce the product to a digit convolution of length $S$, move it to the product of prime cyclic axes by the Chinese-remainder map, evaluate it by the convolution theorem using the source transform (whose permutation cancels), and recover the integer coefficients.",
 mot("Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.", "explicit", r"Splitting the inputs into radix digits reduces multiplication to"),
 [S51, S52, S53, S54, S55],
 page="multiplication-algorithm",
 frm=["parameter-regime","radix-digit-reduction","crt-axis-map","coefficient-twist","tensor-source-transform","permutation-cancellation","normalized-ring-convolution","convolution","fixed-point-complex-arithmetic"],
)

# ---------------------------------------------------------------- S6 precision
S6 = show(
 "S6",
 r"All computed arrays stay in the unit disk, and the recovered coefficients $H_j/2^p$ differ from the true integer coefficients (which lie in $[0,2^{3b})$) by less than $448b\,2^{-3b/4}<\tfrac12$, so rounding and carry propagation give the exact product.",
 "Track norms with disk margins and errors with contraction and bilinear-contraction bounds through the ring convolution, the complex convolution, the chirp transform, the source transform, the pointwise product and the two scalings, and compare the final error with $1/2$.",
 mot("Composing approximations adds their errors, and an approximation of a bilinear contraction with disk operands adds the two operand errors, so a chain of stage errors multiplied by the exact later scalings bounds the final error.", "recoverable"),
 [
  infer("S6.1",
   r"The ring convolution error is $E_{\rm ring}=M(3L+2)<5TL$ (in units $h_p=2^{-p}$, $L=\log_2T$), and its output has norm less than $.7+5TLh_p<.701$ when one operand has norm at most $.7$.",
   r"E_{\rm ring}:=M(3L+2)<5TL."),
  infer("S6.2",
   r"The complex convolution through the twist has error less than $(E_{\rm ring}+4+4+4)h_p<6TLh_p$ (two input twist errors, the ring error and the output untwist).",
   r"<(E_{\rm ring}+4+4+4)h_p<6TLh_p."),
  infer("S6.3",
   r"The chirp transform of a disk-grid input of norm at most $.6$ has error less than $(6TL+2+4+4)h_p<8TLh_p$ and output norm less than $.701$.",
   r"<(6TL+2+4+4)h_p<8TLh_p."),
  infer("S6.4",
   r"The source transform has error less than $2dp^2+8TL$ before the scale $2^\gamma$, hence less than $E_sh_p$ with $E_s=9\,2^\gamma TL$, and its output has norm less than $.501$.",
   r"E_s=9\,2^\gamma TL,"),
  infer("S6.5",
   r"For $z=Q_p(\widetilde U\cdot\widetilde V_1)$, the product of two source transforms with norms less than $.26$, $\|z-U\cdot V_1\|<(2E_s+2)h_p$ and $\|z\|<.5$.",
   r"Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$."),
  infer("S6.6",
   r"Since $G(U\cdot V_1)=(u*v)/S^2$ and $G$ is a contraction, the opposite transform has error $\|\widetilde{\mathscr F}^+(z)-G(U\cdot V_1)\|<(3E_s+2)h_p$.",
   r"&<(3E_s+2)h_p."),
  infer("S6.7",
   r"The first scaling by $S$ approximates $w=(u*v)/S$ with error less than $E_wh_p$, $E_w=S(3E_s+2)<28\,2^\gamma T^2L$, and $\|w\|<1/16$ so $\|\widetilde w\|<1$.",
   r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
  infer("S6.8",
   r"Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error after multiplying by $2^{2b+4}S$ is less than $2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b}$.",
   r"Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than"),
  infer("S6.9",
   r"This is less than $448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<\frac12$, using $\gamma\le b/4$ for large $b$.",
   r"\le448b\,2^{-3b/4}<\frac12."),
  infer("S6.10",
   r"The error below $1/2$ makes the nearest integer to $H_j/2^p$ the unique correct coefficient, which lies in $[0,2^{3b})$ and fits a signed $(3b+1)$-bit word.",
   r"makes the nearest integer to"),
  infer("S6.11",
   r"Carry propagation with $k_0=0$, $d_j=(c_j+k_j)\bmod Q_0$, $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$, $Q_0=2^b$, has carries $0\le k_j\le q(Q_0-1)<Q_0^2$ and the invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$, so the radix digits are those of the full product.",
   r"The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$."),
 ],
 page="precision-exact-recovery",
 frm=["contraction-error-propagation","fixed-point-complex-arithmetic","parameter-regime","radix-digit-reduction","normalized-ring-convolution","tensor-source-transform","triangle-inequality-and-norms"],
 adds=[
  B("E_s","source error","Bound $9\\,2^\\gamma TL$ on the error (in units of $2^{-p}$) of the computed source transform."),
  B("E_w","scaled error","Bound $S(3E_s+2)$ on the error of the first scaled result $\\widetilde w$ in units of $2^{-p}$."),
 ],
 salient="The final error bound $448b\\,2^{-3b/4}$ is tiny compared with $1/2$: the working precision $p=6b$ leaves a margin of about $2^{-b}$ after the input scales $2^{2b+4}$ and the factors $S,T^2\\le2^{3b}$, and the loss $2^\\gamma$ of resampling is only $2^{o(b)}$.",
)

# ---------------------------------------------------------------- S7 cost
S71 = show(
 "S7.1",
 r"Divided by $V=Tp=\Theta(n)$, the costs of the stages are $dK$, $pK^{\tau-1}$, $\ell d^{\lambda'}$, $d^2(1+\ell^\tau)$, $dp^{1/2+\delta}\alpha$, $dp^\delta$, $\log(rp)$, $p^\delta$ and $1$, of dominant powers of $p$ equal to $\epsilon(1+c)$, $1-\epsilon c(1-\tau)$, $1-\epsilon(1-\lambda')$, $\tau+\epsilon(2-\tau)$, $3/4+\delta+3\epsilon/2$, $\epsilon+\delta$ and $1-\epsilon$.",
 "List the normalised cost of each stage with its power of $p$, one row of the cost table at a time.",
 mot("A table makes every stage's contribution visible so that the largest power can be read off.", "recoverable"),
 [
  infer("S7.1.1",
   r"Prefix-slot moves and individual butterfly rounds cost $dK$, power of $p$ equal to $\epsilon(1+c)$.",
   r"Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\"),
  infer("S7.1.2",
   r"Chunk exchanges for the transform layout cost $pK^{\tau-1}$, power $1-\epsilon c(1-\tau)$ (since $K=\Theta(p^{\epsilon c})$).",
   r"Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\"),
  infer("S7.1.3",
   r"Simultaneous butterfly rounds cost $\ell d^{\lambda'}$, power $1-\epsilon(1-\lambda')$ (since $\ell=\Theta(p^{1-\epsilon})$ and $d=\Theta(p^\epsilon)$).",
   r"Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\"),
  infer("S7.1.4",
   r"CRT and axis layouts cost $d^2(1+\ell^\tau)$, power $\tau+\epsilon(2-\tau)$.",
   r"CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\"),
  infer("S7.1.5",
   r"Gaussian line maps cost $dp^{1/2+\delta}\alpha$, power $3/4+\delta+3\epsilon/2$ (since $\alpha=\Theta(p^{1/4+\epsilon/2})$).",
   r"Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\"),
  infer("S7.1.6",
   r"Chirps, twists and scalar products cost $dp^\delta$, power $\epsilon+\delta$.",
   r"Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\"),
  infer("S7.1.7",
   r"Packed polynomial products cost $\log(rp)$, power $1-\epsilon$.",
   r"Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\"),
  infer("S7.1.8",
   r"Final scaling and rounding cost $p^\delta$, absorbed by the rows above.",
   r"Final scaling and rounding & $p^\delta$ & absorbed above\\"),
  infer("S7.1.9",
   r"Input, padding, carries and output cost $1$, absorbed by the rows above.",
   r"Input, padding, carries and output & $1$ & absorbed above\\"),
 ],
)

S72 = show(
 "S7.2",
 r"The seven margins $g_i$ below one are $g_1=1-\epsilon(1+c)>\frac12$, $g_2=\epsilon c(1-\tau)=2^{-181}$, $g_3=\epsilon(1-\lambda')=2^{-129}$, $g_4=1-\tau-\epsilon(2-\tau)>2^{-51}$, $g_5=\frac14-\delta-\frac{3\epsilon}2>\frac18$, $g_6=1-\delta-\epsilon>\frac12$, $g_7=\epsilon=2^{-75}$, so $\min_ig_i=2^{-181}=2\kappa$.",
 "Substitute the fixed rational exponents ($\\epsilon=2^{-75}$, $c=2^{-56}$, $1-\\tau=2^{-50}$, $1-\\lambda'=2^{-54}$, $\\delta=1/16$) into each margin; the smallest comes from the chunk-exchange row.",
 mot("The chunk-exchange term $pK^{\\tau-1}$ is smaller than $p$ only by $K^{-(1-\\tau)}=p^{-\\epsilon c(1-\\tau)}$, the product of three tiny exponents, so it limits the saving.", "recoverable"),
 [
  infer("S7.2.1",
   r"The margins are $g_1=1-\epsilon(1+c)$, $g_2=\epsilon c(1-\tau)$, $g_3=\epsilon(1-\lambda')$.",
   r"g_1&=1-\epsilon(1+c),\qquad"),
  infer("S7.2.2",
   r"Further $g_4=1-\tau-\epsilon(2-\tau)$, $g_5=1/4-\delta-3\epsilon/2$, $g_6=1-\delta-\epsilon$, $g_7=\epsilon$.",
   r"g_4&=1-\tau-\epsilon(2-\tau),\qquad"),
  infer("S7.2.3",
   r"Direct substitution gives $g_1>\frac12$, $g_2=2^{-181}$ (that is $2^{-75}\cdot2^{-56}\cdot2^{-50}$) and $g_3=2^{-129}$.",
   r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad"),
  infer("S7.2.4",
   r"Also $g_4>2^{-51}$, $g_5>\frac18$, $g_6>\frac12$ and $g_7=2^{-75}$.",
   r"g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}."),
  infer("S7.2.5",
   r"Thus $\min_ig_i=2^{-181}=2\kappa$, which has explicit slack to cover any remaining fixed power of $\log p$.",
   r"Thus $\min_i g_i=2^{-181}=2\kappa$."),
 ],
 adds=[
  B("g_i","margin","Gap below one of the $i$th dominant power of $p$ in the normalised cost table."),
 ],
 salient="The smallest margin, $2^{-181}=2\\kappa$, comes from the chunk-exchange term and is the product $\\epsilon\\cdot c\\cdot(1-\\tau)$ of three tiny exponents; this is why $\\kappa=2^{-182}$ is so small.",
)

S73 = show(
 "S7.3",
 r"Each table row is derived from the stage's costs: the layout needs $O(p/K)$ chunk exchanges of cost $O(VK^\tau)$, axis exposure needs $O(d^2)$ interchanges of cost $O(V(1+\ell^\tau))$, the Gaussian line maps cost $O(dTp^{3/2+\delta}\alpha)$ in total, and the packed products cost $O(Tp\log(rp))$.",
 "Divide the stage costs obtained earlier by $V=Tp$ and substitute the sizes $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$, $\\alpha=\\Theta(p^{1/4+\\epsilon/2})$.",
 mot("Each earlier lemma states its cost as volume times a function of the parameters, so the normalised cost is that function.", "recoverable"),
 [
  infer("S7.3.1",
   r"The layout uses $O(p/K)$ exchanges of width-$K$ chunks, each $O(VK^\tau)$, so the normalised total is $O(p/K)K^\tau=O(pK^{\tau-1})$.",
   r"O(p/K)\,K^\tau=O(pK^{\tau-1})."),
  infer("S7.3.2",
   r"Axis exposure and restoration take $O(d^2)$ adjacent moves, each $O(V(1+\ell^\tau))$.",
   r"Each costs $O(V(1+\ell^\tau))$: peel a single excess bit when widths"),
  infer("S7.3.3",
   r"Axis $i$ has at most $T/t_i$ processed lines, so the Gaussian line maps cost $O(dTp^{3/2+\delta}\alpha)$ and, divided by $V=Tp$, give the fifth row.",
   r"Dividing by $V=Tp$ gives the fifth row."),
 ],
)

S74 = show(
 "S7.4",
 r"Setup, descriptor work and the sorting of exceptional addresses over all calls cost $o(V)$ in total.",
 "Bound the number of visits of the layer and layout recursions by $p^A$, charge $p^C$ setup per visit and per record or line, and sum the sorted exceptional streams over all calls.",
 mot("The packed-addition repair costs a bad-address fraction of the volume, which is exponentially small in $K$, so summed over polynomially many calls it is a negligible $o(V)$.", "recoverable"),
 [
  infer("S7.4.1",
   r"The layer and layout recursions have constant branching and depth $O(\log p)$, so the total number of visits is at most $p^A$ and the setup costs at most $p^{A+C}=o(Tp)$.",
   r"total number of visits is at most $p^A$"),
  infer("S7.4.2",
   r"Per record the setup $O(p^C)$ totals $O(Tp^{A+C}/r)=o(Tp)$, per Gaussian line $O(dTp^C/r)=o(Tp)$, since $r$ exceeds every fixed power of $p$.",
   r"Setup before each Gaussian line call has a"),
  infer("S7.4.3",
   r"The compact exceptional stream of a packed change of basis has length $O(V_{\rm call}d2^{-K})$; summing the stable bit sorts over all calls gives $O(Vp^{A'}2^{-K})=o(V)$, a deterministic worst-case bound.",
   r"=O(Vp^{A'}2^{-K})=o(V)"),
 ],
)

S75 = infer("S7.5",
 r"Each of the seven displayed powers is at most $1-2\kappa$ and any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the large-input cost is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
 r"Each of the seven displayed powers is at most $1-2\kappa$ by")

S76 = infer("S7.6",
 r"Below a fixed cutoff schoolbook multiplication is used, so one fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product.",
 r"$O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely")

S7 = show(
 "S7",
 r"Dividing every cost by $V=Tp=\Theta(n)$, all normalised costs are at most $p^{1-2\kappa}$, the smallest margin $2^{-181}$ coming from the chunk-exchange term, so the total time is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ with $\kappa=2^{-182}$.",
 "Tabulate the normalised cost of each stage as a power of $p$, compute the margin of each below one, show that setup and exceptional repairs are $o(V)$, and absorb any fixed power of $\\log p$ into the slack.",
 mot("Costs are stated as volume times a power of the parameters, so dividing by the volume puts all stages in a common unit where the largest power decides the exponent.", "recoverable"),
 [S71, S72, S73, S74, S75, S76],
 page="cost-accounting",
 frm=["parameter-regime","simultaneous-butterfly-layer","transform-tape-layout","address-chunk-interchange","crt-axis-map","normalized-ring-convolution","tensor-source-transform","multiplication-algorithm","asymptotic-notation-beyond-big-o"],
)

# ---------------------------------------------------------------- root
ROOT = show(
 "S0",
 r"A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in this model.",
 "Build the multiplier bottom-up: power-saving tape procedures from linear exchange networks with a rank saving; a fast convolution over a polynomial ring by synthetic transforms; extension to coprime-length axes by Gaussian resampling and chirps; then the integer reduction with exact recovery and the cost accounting.",
 mot("Scanning $\\Theta(n)$ stored bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both data movement and arithmetic must be sped up by a power of the logarithm.", "explicit", r"We therefore need savings in both movement and arithmetic."),
 [S1, S2, S29, S3, S4, S5, S6, S7],
 page="main-theorem",
 frm=["n-log-n-barrier","multitape-turing-machine","big-o-notation","subroutines-and-composition-of-algorithms"],
 adds=[
  B("\\kappa","saving exponent","The constant $2^{-182}$ in the time bound $O(n(\\lg n)^{1-\\kappa})$."),
 ],
)

def relabel(n, label):
    n["id"] = label
    for i, c in enumerate(n.get("children", []), 1):
        relabel(c, label + "." + str(i) if label != "S0" else "S" + str(i))
relabel(ROOT, "S0")
out = {"root": ROOT}

# ---------------------------------------------------------------- validation
PAGES = """n-log-n-barrier convolution negacyclic-ring coefficient-twist signed-packing tape-address-model controlled-cyclic-shift scratch-restoring-exchange array-frames rank-and-orthogonal-subspaces subset-intersection-labels address-shear-factorization rank-saving-recurrence power-width-interchange address-chunk-interchange crt-axis-map packed-selected-bit-addition fixed-point-complex-arithmetic phase-frame-network discrete-fourier-transform fft-butterflies synthetic-polynomial-transform simultaneous-butterfly-layer bluestein-chirp stored-frequency-order transform-tape-layout contraction-error-propagation gaussian-resampling permutation-cancellation normalized-ring-convolution parameter-regime radix-digit-reduction tensor-source-transform precision-exact-recovery multiplication-algorithm cost-accounting main-theorem""".split()
KNOWN = """big-o-notation polynomials complex-numbers multitape-turing-machine binary-numerals-and-bit-strings positional-notation-in-any-radix integer-division-with-remainder-floor-and-ceiling modular-arithmetic arithmetic-modulo-2-and-xor primes-coprimality-and-gcd roots-of-unity-and-euler-s-formula exponential-logarithm-and-gaussian-function asymptotic-notation-beyond-big-o geometric-series-and-sums divide-and-conquer-and-recurrences schoolbook-and-karatsuba-multiplication sorting-and-its-cost permutations-and-bijections sets-subsets-and-cartesian-products multidimensional-arrays-and-row-major-order matrices-vectors-and-linear-maps triangular-and-permutation-matrices dot-product-inner-product-and-orthogonality dyadic-rationals-and-fixed-width-numerators matrix-transposition triangle-inequality-and-norms mathematical-induction-and-proof-by-contradiction cyclic-shifts-and-rotations-of-lists subroutines-and-composition-of-algorithms""".split()
IDX = {p: i for i, p in enumerate(PAGES)}

errs = []
used_pages = {}
from_used = set()
ids = set()
infer_quotes = []  # (id, quote, deferred)

def walk(n, anc_page, anc_chain):
    if n["id"] in ids: errs.append("dup id " + n["id"])
    ids.add(n["id"])
    page = n.get("page") or anc_page
    if n.get("page"):
        if n["page"] in used_pages: errs.append("page reused: %s (%s, %s)" % (n["page"], used_pages[n["page"]], n["id"]))
        used_pages[n["page"]] = n["id"]
        if n["page"] not in IDX: errs.append("unknown page " + n["page"])
    if page is None: errs.append("no page for " + n["id"])
    for f in n.get("from", []):
        from_used.add(f)
        if f in KNOWN: continue
        if f not in IDX: errs.append("unknown from %s at %s" % (f, n["id"])); continue
        if page and IDX[f] >= IDX[page]: errs.append("from %s not before page %s at %s" % (f, page, n["id"]))
    if n["intention"] == "infer":
        if n.get("children"): errs.append("infer with children " + n["id"])
        infer_quotes.append((n["id"], n["quote"]["quote"], n.get("deferred", False)))
    else:
        if not n.get("children"): errs.append("show w/o children " + n["id"])
        if not n.get("method"): errs.append("no method " + n["id"])
        m = n.get("motivation")
        if not m: errs.append("no motivation " + n["id"])
        elif m["source"] == "explicit":
            if not m.get("quote"): errs.append("explicit w/o quote " + n["id"])
            else:
                q = m["quote"]["quote"]
                if SRC.count(q) < 1: errs.append("motivation quote not found %s: %s" % (n["id"], q))
        # adds
        desc_claims = []
        def collect(x):
            for c in x.get("children", []):
                desc_claims.append(c["claim"]); collect(c)
        collect(n)
        maths = []
        for cl in desc_claims:
            maths += re.findall(r"\$(.+?)\$", cl)
        allmath = "\n".join(maths)
        for a in n.get("adds", []):
            if a["symbol"] not in allmath:
                errs.append("adds symbol %s of %s not in descendant math" % (a["symbol"], n["id"]))
        for c in n["children"]:
            walk(c, page, anc_chain + [n["id"]])

walk(ROOT, None, [])
if ROOT["page"] != "main-theorem": errs.append("root page")
for p in PAGES:
    if p not in used_pages and p not in from_used:
        errs.append("page neither presented nor in from: " + p)

# quotes: unique and ordered
pos = 0
last_line = 0
for (i, q, d) in infer_quotes:
    c = SRC.count(q)
    if c == 0:
        errs.append("QUOTE NOT FOUND %s: %s" % (i, q)); continue
    if c > 1:
        errs.append("quote not unique (%d) %s: %s" % (c, i, q))
    if d: continue
    k = SRC.find(q, pos)
    if k < 0:
        k0 = SRC.find(q)
        errs.append("ORDER violation %s (line %d, after pos line %d): %s" % (i, SRC[:k0].count("\n") + 1, SRC[:pos].count("\n") + 1, q))
    else:
        pos = k + len(q)

for e in errs: print(e)
print("nodes:", len(ids), "errors:", len(errs))
json.dump(out, open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E9F8Y/exegenius/tasks/0003-argument.answer.json', 'w'), indent=1)
