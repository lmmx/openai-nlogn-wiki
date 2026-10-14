import json, sys, re
BASE = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e4/V1"
SRC = open(BASE + "/sources/paper.tex", encoding="utf-8").read()

ORDER = """nlogn-conjecture convolution polynomial-ring-mod-y-r-plus-1 nlogn-multiplier-subroutine signed-packing
tape-address-arrays elementary-stream-operations row-splitting modular-arithmetic controlled-shifts linear-algebra-basics
linear-network-roles frames triple-subset-gadget subspace-labels-rank-deficit address-shear triangular-factorization
fixed-tape-recursion recursive-power-saving address-chunk-interchange packed-selected-bit-addition fixed-point-disk-grid
guard-bits-dyadic phase-twist dft multidimensional-transform fft-butterfly synthetic-polynomial-transform
butterfly-and-phase-kernels frequency-order-retention binary-phase-interface simultaneous-butterfly-layer
synthetic-transform-layout contractions-and-error synthetic-convolution gaussian-resampling resampling-permutations-retained
bluestein-chirp permutation-cancellation parameter-choice prime-source-lengths integer-as-digit-convolution exact-recovery
crt-address-map source-transform multiplication-algorithm cost-analysis integer-multiplication-below-nlogn""".split()
IDX = {p: i for i, p in enumerate(ORDER)}
KNOWN = """big-o polynomials complex-numbers turing-machine-tapes binary-representation-and-schoolbook-arithmetic
floor-ceiling-and-logarithms exponentials-and-elementary-inequalities summation-telescoping-sums-and-geometric-series
recurrences-and-the-recursion-tree karatsuba-and-classical-multiplication-algorithms recursion-call-stack-and-subroutines
sets-functions-bijections-and-permutations mathematical-induction-and-proof-techniques prime-numbers-and-trial-division
groups-rings-and-fields xor-and-arithmetic-over-f-2 special-matrices-and-matrix-algebra triangle-inequality-and-norm-bounds
rational-numbers-and-dyadic-fractions deterministic-algorithms-and-worst-case-time entrywise-operations-on-arrays-and-vectors""".split()

def ev(q):
    return {"source": "paper", "quote": q}

def I(id, claim, quote, page=None, frm=(), deferred=False, salient=None):
    d = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": list(frm)}
    if page: d["page"] = page
    if deferred: d["deferred"] = True
    if salient: d["salient"] = salient
    return d

def B(sym, name, meaning, rel="count"):
    return {"symbol": sym, "name": name, "meaning": meaning, "relation": rel}

def S(id, claim, method, mtext, msrc, children, mquote=None, page=None, frm=(), adds=(), salient=None):
    d = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": {"text": mtext, "source": msrc, "quote": ev(mquote) if mquote else None},
         "children": children, "from": list(frm)}
    if page: d["page"] = page
    if adds: d["adds"] = list(adds)
    if salient: d["salient"] = salient
    return d

# ---------------- Section 3/4: the key step -----------------
K1 = S("S1.3.1.1",
 r"A fixed network of $W$ linear gates on wires exchanges two banks of values with signs, $(X_a,Y_a)\mapsto(-Y_a,X_a)$, and restores every scratch wire whatever its initial contents.",
 "Build the exchange from one gadget that adds one bank into the other while cancelling arbitrary scratch values, and apply it in three stages (forward, inverse, forward).",
 "Once the gadget adds $x$ into $y$ independently of the scratch values, three applications give an exchange, and the whole network then restores its scratch wires by construction.",
 "recoverable",
 [
  I("S1.3.1.1.1", r"For arbitrary initial scratch values, a forward invocation of the eight-row schedule changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged, because the side wires cancel the unwanted intersection-size coefficients.",
    r"invocation changes $y_S$ to $y_S+x_S$ and leaves every other value",
    page="triple-subset-gadget", frm=["linear-network-roles","linear-algebra-basics","xor-and-arithmetic-over-f-2"],
    salient=r"The net coefficient from $x_T$ to $y_S$ is exactly $\delta_{ST}$ even though gather and scatter produce coefficients depending on $|S\cap T|$: the side wires cancel precisely the neighbouring-triple terms (intersection one in the bit case, even intersection in the complex case)."),
  I("S1.3.1.1.2", r"Three stages (forward from $X$ to $Y$, inverse from $Y$ to $X$, forward from $X$ to $Y$) send $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restore every auxiliary value.",
    r"(X_a,Y_a)\longmapsto(-Y_a,X_a)"),
 ], page="linear-network-roles", frm=["groups-rings-and-fields","xor-and-arithmetic-over-f-2"])

K2 = I("S1.3.1.2", r"Giving every vertex of a wire an invertible frame $D_v$ on that wire's address-indexed array, a common frame commutes with each pointwise linear gate, so only the edge operators $D_vD_u^{-1}$ must be implemented and the endpoint frames fix the net array operator.",
  r"Thus the common frame commutes with the pointwise gate, and",
  page="frames", frm=["linear-network-roles","linear-algebra-basics","entrywise-operations-on-arrays-and-vectors"])

K3 = S("S1.3.1.3",
 r"Nested nondegenerate subspace labels of an $m$-dimensional space can be attached to the gates and terminals so that only one central-wire edge per invocation decreases, losing $h$ dimensions, and the total of absolute dimension changes is $Wm-2N+2L$ with $L<N/2$.",
 "Give each triple the line spanned by its indicator vector, use orthogonality of neighbouring triple lines to make labels nested along every edge, and confine all decreases to one central-wire edge per invocation.",
 "The saving will come from keeping the total dimension lost on decreasing edges small relative to N.",
 "explicit",
 [
  I("S1.3.1.3.1", r"The only decreasing edges are the central-wire edges from time 3 to time 4, each losing $h$ dimensions.",
    r"edges are the central-wire edges from time 3 to time 4"),
  I("S1.3.1.3.2", r"The sum of absolute dimension changes over all edges is $Wm-2N+2L$, where $N$ source dimensions and $Wm-N$ sink dimensions telescope at the gates.",
    r"=Wm-2N+2L"),
  I("S1.3.1.3.3", r"The loss ratios are $L/N=100/539$ and $101/539$ in the two constructions, both smaller than $1/2$.",
    r"In particular, both are smaller than $1/2$."),
 ], mquote=r"The saving will come from keeping the total dimension lost on decreasing",
 page="subspace-labels-rank-deficit", frm=["linear-algebra-basics","frames","triple-subset-gadget"])

K4 = S("S1.3.1.4",
 r"Using the projections $P_U$ onto the labels as vertex matrices, the bit network sends every input role through the same shear $(H,D)\mapsto(H+D,D)$, and the sum $s_{\rm b}$ of the ranks of its edge differences is strictly less than $W_{\rm b}m$.",
 "Take the frame at each vertex to be the address shear by that vertex's rational matrix, so endpoint differences telescope to the identity, and count each edge's rank as its change in label dimension.",
 "Frames reduce the net operator to the endpoint matrices, and rank of a projection difference equals the dimension change, so the earlier dimension count translates directly to a rank count.",
 "recoverable",
 [
  I("S1.3.1.4.1", r"For every input role $w$ the endpoint matrix difference is the identity $I_m$.",
    r"M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m"),
  I("S1.3.1.4.2", r"The sum of edge ranks is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$, which is below $W_{\rm b}m$ because $N-2L_{\rm b}>0$.",
    r"&=W_{\rm b}m-N+2L_{\rm b}"),
 ], page="address-shear", frm=["subspace-labels-rank-deficit","frames","modular-arithmetic","special-matrices-and-matrix-algebra"])

K5 = I("S1.3.1.5", r"With $\tau=1-2^{-50}$ the fixed rank deficit gives $s/W<m^\tau$ for the bit network.",
  r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,", frm=["address-shear","exponentials-and-elementary-inequalities"])

K6 = S("S1.3.1.6",
 r"A shear $(H,D)\mapsto(H+AD,D)$ by a fixed rational matrix $A$ of rank $a$ costs exactly $a$ interchanges of pairs of $b$-digit fields plus $O(V)$ further work.",
 r"Factor $A=E_1\Pi E_2$ with lower triangular $E_1,E_2$, which act in tape order at linear cost, so only the $a$ ones of $\Pi$ remain, and realize each by one interchange sandwiched between two controlled shifts.",
 "Lemma ordered-affine-streams updates a later field using earlier fields in linear time; lower triangular changes of coordinates can be performed entirely in this direction.",
 "explicit",
 [
  I("S1.3.1.6.1", r"Every rational $m\times m$ matrix of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with exactly $a$ ones.",
    r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization"),
  I("S1.3.1.6.2", r"The shear by $A$ is performed with exactly $a$ interchanges of $b$-digit fields and $O(V)$ further work.",
    r"can be performed with exactly $a$ interchanges of pairs of $b$-digit"),
  I("S1.3.1.6.3", r"Each one of $\Pi$ calling for $H_i\leftarrow H_i+D_j$ is done by $D_j\leftarrow D_j+H_i$, an interchange of $H_i,D_j$, then $D_j\leftarrow H_i-D_j$, using one interchange.",
    r"D_j\leftarrow D_j+H_i,\qquad"),
 ], mquote=r"can be performed entirely in this direction.",
 page="triangular-factorization", frm=["linear-algebra-basics","controlled-shifts","elementary-stream-operations","special-matrices-and-matrix-algebra"])

K7 = S("S1.3.1.7",
 r"Splitting whole rows cyclically among the $W$ roles, after padding the row count to a multiple of $W^k$, gives role streams of identical shape whose volume is $V/W$ each.",
 "Send row $r=Wg+w$ to role stream $w$ with row number $g$, keeping every other address field intact.",
 "A pointwise gate must read matching addresses on all $W$ roles, so every role stream needs the same address set, which cyclic row distribution supplies at exactly one $W$th of the volume.",
 "recoverable",
 [
  I("S1.3.1.7.1", r"Whole rows are split cyclically into $W$ role streams within each prefix.",
    r"Split whole rows cyclically into $W$ role streams within each prefix"),
  I("S1.3.1.7.2", r"Each role stream has volume $V/W$ and its row count is still divisible by $W^{k-1}$.",
    r"logical volume $V/W$, and its row count is divisible by $W^{k-1}$."),
 ], page="row-splitting", frm=["elementary-stream-operations","tape-address-arrays"])

K8 = I("S1.3.1.8", r"The interchange $(H,D)\mapsto(D,H)$ is the composition $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$, in which only the middle shear uses the network and the other two updates cost $O(V)$.",
  r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,",
  frm=["address-shear","controlled-shifts"])

K9 = S("S1.3.1.9",
 r"The cost divided by volume satisfies $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$, hence $F_k=O(e^\tau)$ for $e=m^k$.",
 r"Unroll the recurrence into a geometric sum with ratio $a=s/W<m^\tau$ and bound it separately for $a\le1$ and $a>1$.",
 r"Each of the $s$ child calls runs on a stream of volume $V/W$, so dividing by the parent's volume multiplies the child's normalized cost by $s/W$, a ratio below $m^\tau$ rather than $m$.",
 "recoverable",
 [
  I("S1.3.1.9.1", r"The normalized cost satisfies $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.",
    r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."),
  I("S1.3.1.9.2", r"For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$.",
    r"$\sum_{j=0}^k a^j$ is $O(m^{k\tau})$."),
  I("S1.3.1.9.3", r"Hence $F_k=O(e^\tau)$.", r"Hence $F_k=O(e^\tau)$."),
 ], frm=["recurrences-and-the-recursion-tree","summation-telescoping-sums-and-geometric-series","exponentials-and-elementary-inequalities"])

K10 = S("S1.3.1.10",
 r"The recursive calls can be scheduled on a fixed number of tapes at cost $O(V)$ at the parent node, which is the additive term of the recurrence.",
 "Park the $W-1$ inactive role streams on a stack tape, copy the active stream to the child's input area, run the child, copy back and pop the parked streams.",
 "A recursion with $s$ children cannot add tapes with depth, so the parent's streams must wait on a stack, and only the parent's own volume is moved each time.",
 "recoverable",
 [
  I("S1.3.1.10.1", r"Before a recursive call the inactive role streams are appended to a parking stack and the active stream is copied to the child.",
    r"Before a recursive call, append the $W-1$ inactive role streams to the"),
  I("S1.3.1.10.2", r"Each push, pop, copy, positioning or erasure moves $O(V)$ symbols at a parent node, and there are only $s$ child calls.",
    r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
 ], page="fixed-tape-recursion", frm=["recursion-call-stack-and-subroutines","row-splitting","turing-machine-tapes"])

K = S("S1.3.1",
 r"A call at parameter $mf$ that makes $s<Wm$ calls at parameter $f$ on role streams of volume $V/W$ costs $O(Ve^\tau)$ for width $e=m^k$ and some fixed $\tau<1$, instead of $O(Ve)$.",
 "Construct a fixed circuit whose total edge rank $s$ is strictly less than $Wm$, charge each edge one smaller interchange, split rows among the $W$ roles, and sum the resulting recurrence.",
 "After dividing cost by volume, multiplying the parameter by m increases the recursive contribution by s/W<m, so the strict inequality is where the power saving comes from.",
 "explicit",
 [K1, K2, K3, K4, K5, K6, K7, K8, K9, K10],
 mquote=r"increases the recursive contribution by $s/W<m$. This strict inequality",
 page="recursive-power-saving", frm=["recurrences-and-the-recursion-tree","tape-address-arrays"],
 adds=[B("W","wire count","the number of wires (roles) of the fixed network, including scratch wires"),
       B("m","label dimension","the dimension of the label space, equal to the number of address fields per chunk in one recursive step"),
       B("s","total edge rank","the sum over edges of the rational rank of the edge matrix difference, equal to the number of smaller calls"),
       B("e","chunk width","the number of digits in each of the two chunks, a power of $m$")],
 salient=r"The saving is strict but astronomically thin: $s$ is below $Wm$ only by a relative deficit of about $10^{-11}$ to $10^{-13}$ (from $L<N/2$), and $\tau=1-2^{-50}$. Any strict inequality $s/W<m$ suffices, because each level multiplies normalized cost by $s/W<m$ instead of $m$, so the sum over $k=\log_m e$ levels is dominated by $m^{k\tau}=e^\tau$ rather than $e$.")

A2 = S("S1.3.2",
 r"Arbitrary chunk widths and row counts reduce to power widths: the cost of interchanging two $u$-bit chunks stays $O(Vu^\tau)$.",
 r"Interchange the top $\rho$ digits one pair at a time to create a row field, pad rows to a multiple of $W^k$, cut the remaining width into pieces of widths $m^j$ in base $m$, and sum the geometric series.",
 "Rows for a general array can be supplied by a few of its own high digits.",
 "explicit",
 [
  I("S1.3.2.1", r"Padding the row count to $R'=W^k\lceil R/W^k\rceil<2R$ makes it divisible by every $W^j$ needed, at most doubling the volume.",
    r"R'=W^k\left\lceil R/W^k\right\rceil<2R."),
  I("S1.3.2.2", r"The remaining width is written in base $m$ as $e-\rho=\sum_{j=0}^{k}a_jm^j$ with $0\le a_j<m$ and cut into $a_j$ pieces of width $m^j$.",
    r"e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m."),
  I("S1.3.2.3", r"The pieces cost $O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)$ in total.",
    r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)."),
 ], mquote=r"Rows for a general array can be supplied by a few of its own high digits.",
 frm=["elementary-stream-operations","floor-ceiling-and-logarithms","summation-telescoping-sums-and-geometric-series"])

A = S("S1.3",
 r"Two disjoint $u$-bit address chunks of an array of volume $V$ can be interchanged in $O(Vu^\tau)$ time for a fixed rational $\tau=1-2^{-50}<1$, although intermediate steps form XOR combinations of data.",
 "Reduce the interchange to a shear $H\leftarrow H+D$, realize the shear with a fixed bit network whose edges are smaller interchanges, so the width recurses by a factor $m$, and then lift power widths to arbitrary widths.",
 "Because the sum of the edge ranks is less than the number of wires times m, the resulting recurrence saves a power of the chunk width.",
 "explicit",
 [K, A2],
 mquote=r"Because the sum of these ranks is less than the number of wires times",
 page="address-chunk-interchange", frm=["elementary-stream-operations","controlled-shifts","recursive-power-saving","xor-and-arithmetic-over-f-2"])

# -------------- Section 5: butterfly layers ------------------
B1 = S("S1.4.1",
 r"In the complex network with binary labels, each edge's frame change is a product of translation kernels $aI+bX_v$ over an orthonormal basis of the edge residual, and the frames telescope to $C^{\otimes m}$ on every role, with $s_{\rm c}<W_{\rm c}m$ kernels in all.",
 r"Diagonalize all phase frames $\mathcal C_U$ by one Hadamard matrix; orthogonal weight additivity modulo $4$ turns a label change into one translation kernel per residual basis vector.",
 "Bit-network edges needed a permutation; here the frame $\mathcal C_U$ is diagonal in the Hadamard basis, and weights add modulo 4 across orthogonal vectors, so each unit-norm basis vector contributes one two-point kernel.",
 "recoverable",
 [
  I("S1.4.1.1", r"Each edge's frame change is a product of one translation kernel $aI+bX_v$, or its inverse, per vector of an orthonormal basis of the residual.",
    r"kernel $aI+bX_v$, or its inverse, per vector in an orthonormal basis", deferred=True),
  I("S1.4.1.2", r"The number of kernels is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$.",
    r"s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}", deferred=True),
  I("S1.4.1.3", r"After source and sink corrections and undoing the exchange, telescoping the phase frames gives $C^{\otimes m}$ on every role, including scratch roles.",
    r"bank exchange, telescoping these phase frames gives $C^{\otimes m}$", deferred=True),
 ], page="binary-phase-interface",
 frm=["butterfly-and-phase-kernels","subspace-labels-rank-deficit","frames","linear-network-roles","xor-and-arithmetic-over-f-2"])

B2 = I("S1.4.2", r"The kernel $C=aI+bX$ with $a=(1+i)/2$, $b=(1-i)/2$ satisfies $H_0=b\,\mathsf SC\mathsf S$ with $\mathsf S=\mathrm{diag}(1,i)$, so a layer of $H_0$ equals diagonal phases times a layer of $C$.",
  r"H_0=b\mathsf SC\mathsf S,\qquad C^2=X",
  page="butterfly-and-phase-kernels", frm=["complex-numbers","special-matrices-and-matrix-algebra","fft-butterfly"])

B3 = I("S1.4.3", r"An edge's phase-frame difference equals $\mathcal P_M\bigl(\prod_jC_{e_j}^{\epsilon_j}\bigr)\mathcal P_M^{-1}$ for a binary change of basis $M$, so each edge needs one child call on $f$ axes per residual basis vector, plus a fixed number of row additions of selected bits.",
  r"=\mathcal P_M\left(\prod_{j=1}^{\rho_{\rm edge}}C_{e_j}^{\epsilon_j}\right)",
  frm=["binary-phase-interface","xor-and-arithmetic-over-f-2"])

B4 = I("S1.4.4", r"A full layer satisfies $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, where $\mathcal S_D$ multiplies by the phase $i^{x_1+\cdots+x_D}$, so the normalized layer is recovered exactly from the $C$ layer.",
  r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D.",
  frm=["butterfly-and-phase-kernels"])

B5 = S("S1.4.5",
 r"Corresponding selected bits of two address chunks across $f$ chunk positions can be XORed at once, restoring an arbitrary third chunk, in time $O(V(L^\tau+1))$ with $L=fK$ under the family bounds.",
 "Emulate the XORs by eight rotations (cyclic shifts of whole chunk ranges) that agree with them away from a small set of bad addresses, then repair that set by sorting.",
 "Individually XORing the selected bits would need a pass over the array per chunk; shifts act on all packed segments in one pass, and carries between segments only occur when a guard value is extreme, which is rare.",
 "recoverable",
 [
  I("S1.4.5.1", r"Eight conditional $\pm1$ rotations flip the parity of $u$ exactly when the control $c=1$ and restore the auxiliary integer $w$.",
    r"\bigl(u+c(1-2(u\bmod2)),\ w\bigr)."),
  I("S1.4.5.2", r"Packed shifts agree with the independent XORs unless a guard value is within 10 of an end, which happens on at most $\delta_{\rm bad}M$ addresses with $\delta_{\rm bad}\le 80(f-1)2^{-K}$.",
    r"|\mathcal B|\le\delta_{\rm bad}M."),
  I("S1.4.5.3", r"The exceptional addresses are extracted, relabeled by destination rank, stably radix-sorted and reinserted, which implements the exact XOR map everywhere.",
    r"This implements $T_0$ everywhere."),
 ], page="packed-selected-bit-addition",
 frm=["address-chunk-interchange","controlled-shifts","elementary-stream-operations","xor-and-arithmetic-over-f-2"])

B6 = S("S1.4.6",
 r"With rows split among the $W_{\rm c}$ roles and slots of $e/m$ chunks, the normalized cost obeys $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ and the layer costs $O(d^{\lambda'})$ per unit volume.",
 "Recurse on the complex network exactly as for interchange, stop at $e<d^{\\beta}$ with individual kernels, and cut a general $D$ into base-$m$ pieces.",
 "The structure matches the interchange recursion with a strict rank deficit, but now the additive node cost is $(eK)^\\tau$ from packed basis changes, which is still below the geometric growth $m^\\lambda$.",
 "recoverable",
 [
  I("S1.4.6.1", r"Each recursive edge call acts on one role stream of exactly $1/W$ of its parent's logical volume.",
    r"one role stream with volume exactly \(1/W\) of its parent's logical"),
  I("S1.4.6.2", r"The normalized cost satisfies $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$.",
    r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
  I("S1.4.6.3", r"The internal costs sum to $Ce^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)$ since $a=s/W<m^\sigma<m^\lambda$.",
    r"C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)."),
  I("S1.4.6.4", r"Adding the base-$m$ pieces gives $O(d^{\lambda'})$ for any fixed $\lambda'$ with $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$.",
    r"\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1."),
 ], frm=["row-splitting","fixed-tape-recursion","recursive-power-saving","packed-selected-bit-addition","recurrences-and-the-recursion-tree"])

B7 = S("S1.4.7",
 r"Every intermediate value of the whole layer is an exact Gaussian dyadic with $p+\Delta$ fractional and $\Delta+3$ integer and sign bits, where $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$, so only one truncation is needed.",
 "Bound the longest chain of additions, halvings, sign changes and multiplications by $i$ through the recursion, since each can at most double the modulus or add one denominator bit.",
 "A rounding inside the network would break the exactness of the cancellation of scratch values, so intermediate values are kept exact and the only question is how many bits they need.",
 "recoverable",
 [
  I("S1.4.7.1", r"The arithmetic depth satisfies $A(e)\le sA(e/m)+E$ at an internal node.",
    r"A(e)\le sA(e/m)+E"),
  I("S1.4.7.2", r"A value at depth $\ell$ lies in $2^{-(p+\ell)}\mathbb Z[i]$ and has modulus at most $2^\ell$.",
    r"lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most"),
  I("S1.4.7.3", r"Reserving $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits per real component represents every intermediate coefficient exactly.",
    r"Thus reserving \(p+\Delta\)"),
  I("S1.4.7.4", r"Choosing $\epsilon C_1<1$ makes the guard width $\Delta=o(p)$, so the full coefficient width stays $O(p)$.",
    r"Choose \(\epsilon C_1<1\)."),
 ], page="guard-bits-dyadic", frm=["fixed-point-disk-grid","rational-numbers-and-dyadic-fractions","triangle-inequality-and-norm-bounds"])

B8 = I("S1.4.8", r"The procedure returns $Q_p(\mathcal Hz)$ in $O(Vd^{\lambda'})$ time with error below $\sqrt2\,2^{-p}$ after a single truncation toward zero.",
  r"The procedure returns $Q_p(\mathcal H z)$ in the same array,",
  frm=["fixed-point-disk-grid","guard-bits-dyadic"])

Bn = S("S1.4",
 r"Applying $H_0$ at one common bit position in each of $D\le d$ address chunks of every polynomial record, with one final truncation $Q_p$, costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$ and has error below $\sqrt2\,2^{-p}$.",
 r"Express the $H_0$ layer as a layer of the phase kernel $C$ between diagonal phases, compute the $C$ layer by the complex network recursively with binary basis changes done by packed selected-bit addition, evaluate exactly with guard bits, and truncate once.",
 "We first construct tensor products of the auxiliary two-point kernel C, whose phase frames express a tensor product using smaller groups of selected bits.",
 "explicit",
 [B1, B2, B3, B4, B5, B6, B7, B8],
 mquote=r"We first construct tensor products of the auxiliary two-point kernel",
 page="simultaneous-butterfly-layer",
 frm=["recursive-power-saving","address-chunk-interchange","row-splitting","fixed-tape-recursion","fixed-point-disk-grid","packed-selected-bit-addition","guard-bits-dyadic","binary-phase-interface","butterfly-and-phase-kernels"],
 adds=[B("D","selected chunks","the number of consecutive address chunks in which the common bit is selected"),
       B("K","chunk width","the number of bits in each address chunk"),
       B("f","slot size","the number of chunks in each of the $m$ slots of a recursive group")])

G1 = S("S1",
 r"Two tape procedures cost a strict power less than the logarithmic factor: interchanging two address chunks of $u$ bits costs $O(Vu^\tau)$ and a simultaneous butterfly layer over $d$ chunks costs $O(Vd^{\lambda'})$, for fixed $\tau,\lambda'<1$ and logical volume $V$.",
 "Derive both procedures from the same device: a fixed linear network with a rank deficit applied recursively to role streams, after the elementary scan operations that the recursion uses.",
 "Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value.",
 "explicit",
 [
  I("S1.1", r"Moving digits, splitting on a digit and merging, and splitting whole rows cyclically into $W$ streams each take $O(V)$ steps on a fixed number of tapes.",
    r"volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
    page="elementary-stream-operations", frm=["tape-address-arrays","binary-representation-and-schoolbook-arithmetic","turing-machine-tapes"]),
  I("S1.2", r"A later field $y$ in a prime-power range $[Q]$ can be shifted by an offset computed from earlier fields, or scaled by a rational unit, in $O(V)$ time.",
    r"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
    page="controlled-shifts", frm=["modular-arithmetic","tape-address-arrays","elementary-stream-operations"]),
  A, Bn],
 mquote=r"Each procedure arises from its own fixed linear network that exchanges two",
 frm=["tape-address-arrays"],
 adds=[B("V","logical volume","the number of stored data bits of the array, excluding work tapes"),
       B("u","chunk width","the number of bits in each of the two address chunks to be interchanged"),
       B("\\tau","interchange exponent","a fixed rational exponent below one bounding the interchange cost, $1-2^{-50}","direct"),
       B("\\lambda'","layer exponent","a fixed rational exponent below one bounding the simultaneous butterfly layer cost","direct")])

# -------------- Section 6/7: synthetic convolution ------------------
T1 = S("S2.1.1",
 r"Over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ the length-$t$ transforms $F_t^\pm$ with roots $\omega_t=y^{2r/t}$ invert each other up to $1/t$ and are computed by butterflies $H_0$ and signed shifts only.",
 "Choose the roots of unity to be powers of $y$, so that each twiddle multiplication is a signed shift of the coefficient list and only the two-point butterflies cost arithmetic.",
 "Multiplication by such a root is a signed shift of the coefficient list.",
 "explicit",
 [
  I("S2.1.1.1", r"For a power of two $t$ dividing $2r$, the root is $\omega_t=y^{2r/t}$.",
    r"For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$."),
  I("S2.1.1.2", r"Synthetic character cancellation gives $F_t^+F_t^-=t^{-1}I$ although the ring has zero divisors.",
    r"F_t^+F_t^-=t^{-1}I."),
  I("S2.1.1.3", r"The decimation-in-frequency step multiplies the second butterfly output by $\omega_t^{-k}$ and recurses on both halves.",
    r"the $b=1$ output by $\omega_t^{-k}$, and then apply the length-$t/2$"),
 ], mquote=r"such a root is a signed shift of the coefficient list.",
 page="synthetic-polynomial-transform",
 frm=["dft","multidimensional-transform","fft-butterfly","polynomial-ring-mod-y-r-plus-1"])

T2 = I("S2.1.2", r"The recursion writes its outputs directly in bit-reversed order, so the pointwise product and the opposite transform consume the stored order without a separate permutation, and the two procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
  r"directly in this order; it does not move whole frequency indices.",
  page="frequency-order-retention", frm=["fft-butterfly","synthetic-polynomial-transform"])

T3 = I("S2.1.3", r"On $d-1$ axes the twiddles of one round commute with the other axes' butterflies, so a round is one parallel butterfly $\mathcal H$ followed by one recordwise monomial shift $J_E$.",
  r"Consequently the individual axis steps may be grouped as a parallel",
  frm=["synthetic-polynomial-transform"])
T4 = I("S2.1.4", r"Moving the selected bits of the long axes and the low rounds into a prefix costs $O(TpdK)$.",
  r"listed slots, so the moves cost $O(TpdK)$.")
T5 = I("S2.1.5", r"Exchanging the remaining chunks into the order $(1,1),(2,1),\ldots,(D,q)$ costs $O(Tp\cdot pK^{\tau-1})$ via at most $Dq-1$ exchanges of width-$K$ chunks.",
  r"=O\bigl(Tp\,pK^{\tau-1}\bigr).", frm=["address-chunk-interchange"])
T6 = I("S2.1.6", r"Each of at most $\ell$ rounds is one simultaneous butterfly layer, costing $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.",
  r"$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.", frm=["simultaneous-butterfly-layer"])
T7 = I("S2.1.7", r"Each round is a contraction followed by one truncation adding error below $\sqrt2\,2^{-p}$, so after at most $\ell$ rounds the error is below $\sqrt2\,\ell\,2^{-p}$.",
  r"zero error, at most $\ell$ rounds therefore", frm=["fixed-point-disk-grid"])

Tn = S("S2.1",
 r"The forward synthetic transform $LBF_{\boldsymbol t}^-$ and its opposite on $d-1$ axes with $T=rM$ entries cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\,\ell\,2^{-p}$, and the forward output can be kept in its stored layout.",
 "Place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks using bit moves and chunk interchanges, then run each transform round as one simultaneous butterfly layer followed by one monomial shift.",
 "To apply the simultaneous layer in a transform round, we must place the selected bits of the participating axes at a common offset in consecutive K-bit chunks.",
 "explicit",
 [T1, T2, T3, T4, T5, T6, T7],
 mquote=r"we must place the selected bits of the participating axes at a common",
 page="synthetic-transform-layout",
 frm=["simultaneous-butterfly-layer","synthetic-polynomial-transform","frequency-order-retention","address-chunk-interchange","fixed-point-disk-grid","elementary-stream-operations"],
 adds=[B("\\ell","log record length","the base-two logarithm of the record length $r$, the number of rounds per axis")])

SP = S("S2.2",
 r"Two disk-grid polynomials of degree below $r$ are multiplied exactly modulo $y^r+1$, then normalized by $r$ and truncated, in $O(rp\log(rp))$ time.",
 r"Evaluate the real and imaginary integer polynomials at $B_0=2^{4p}$ with signed carries, multiply the four resulting integers with the established multiplier, and read the coefficients back as centered residues.",
 "A polynomial product becomes one integer product once the radix exceeds twice the largest coefficient; signed carries extend this to negative coefficients.",
 "recoverable",
 [
  I("S2.2.1", r"Each polynomial $u$ is packed as the signed evaluation integer $A_u=u(B_0)$ with $B_0=2^{4p}$, using two's-complement blocks with carries in $\{-1,0\}$.",
    r"and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer"),
  I("S2.2.2", r"Every product coefficient satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so centered residues modulo $B_0$ extract it uniquely.",
    r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
  I("S2.2.3", r"Four exact integer products dominate the linear packing, extraction, combination, wrapping and truncation costs.",
    r"Four exact integer products dominate the linear"),
 ], page="signed-packing", frm=["nlogn-multiplier-subroutine","polynomial-ring-mod-y-r-plus-1","convolution"])

S2 = S("S2",
 r"The normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays over $\mathcal R_r$ on $d-1$ cyclic axes is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.",
 "Apply the forward synthetic transform to both operands, multiply the outputs pointwise in the retained layout by signed packing, apply the opposite transform and scale by $M$ (convolution theorem).",
 "Pointwise multiplication commutes with applying the same record permutation to both operands, so the permuted order never has to be undone between the forward and opposite transforms.",
 "recoverable",
 [
  Tn, SP,
  I("S2.3", r"Expansion of the finite sums gives $F^-_{\boldsymbol t}(f*g)=M(F^-_{\boldsymbol t}f)(F^-_{\boldsymbol t}g)$ and $F^+F^-=I/M$, so the opposite transform of the pointwise product, scaled by $M$, equals $(f*g)/(rM)$.",
    r"=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g).", frm=["dft","multidimensional-transform","convolution"]),
  I("S2.4", r"Since $LB$ permutes records and leaves polynomial suffixes intact, the pointwise product commutes with it and the retained order can be passed straight to the opposite transform.",
    r"Since $LB$ permutes records and leaves their polynomial"),
  I("S2.5", r"With forward errors below $\delta$ and product truncation $\eta$, the computed result has error below $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$.",
    r"$M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$", frm=["contractions-and-error"]),
  I("S2.6", r"The $M=T/r$ pointwise products cost $O(Tp\log(rp))$ in total, and the transforms cost as stated.",
    r"is $O(Tp\log(rp))$; the three transform costs are as stated, and"),
 ],
 page="synthetic-convolution",
 frm=["synthetic-transform-layout","signed-packing","contractions-and-error","dft","multidimensional-transform","convolution","polynomial-ring-mod-y-r-plus-1"],
 adds=[B("M","record count","the number of polynomial records, $M=T/r$, equal to the product of the lengths of the first $d-1$ axes")])

# -------------- Section 8: resampling ------------------
R1 = S("S3.1",
 r"Gaussian resampling gives maps $\mathsf S,\mathsf T$ with $\mathsf TP_sF_s=P_tF_t\mathsf S$ and a near-identity $N=C\mathsf T\mathsf D$ with $\|N-I\|<2^{-\alpha^2\theta}$, converting a transform of length $s$ into one of length $t>s$.",
 "Use Harvey and van der Hoeven's Gaussian identity and inverse estimate as cited results, then invert the near-identity $N$ by a Neumann series.",
 "The transform length needed for the integer product is a product of coprime lengths, while the fast synthetic transforms need powers of two, so one must change the transform length at small error.",
 "recoverable",
 [
  I("S3.1.1", r"The Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$ holds exactly.",
    r"\mathsf T P_sF_s=P_tF_t\mathsf S,"),
  I("S3.1.2", r"The near-identity satisfies $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$, hence is invertible by the Neumann series.",
    r"\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}."),
 ], page="gaussian-resampling", frm=["dft","contractions-and-error","complex-numbers"])

R2 = I("S3.2", r"Setting $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$ gives contractions with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, the normalizations multiplying to $2^{-2\alpha^2}$.",
  r"which is \eqref{eq:no-sort-one-dimensional}.", frm=["gaussian-resampling"])
R3 = I("S3.3", r"The permutations $P_t$ and $P_s^{-1}$ remain in the transform identity; executing them would cost two label-and-sort operations of $O(tp\log t)$ each per axis.",
  r"Its two label-and-sort operations", frm=["gaussian-resampling"])
R4 = I("S3.4", r"Tensoring over the axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$, the one-dimensional maps applied line by line in the padded box.",
  r"=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A,")
R5 = I("S3.5", r"The one-dimensional algorithms cost $O(dTp^{3/2+\delta}\alpha)$ in total and exposing and restoring all lines costs $O(Tpd^2(1+\ell^\tau))$ by chunk interchanges.",
  r"then exposing and restoring all the lines costs", frm=["address-chunk-interchange"])
R6 = I("S3.6", r"The chirp identity expresses the target-permuted transform as $QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$, because the coefficient of $u_{\boldsymbol k}$ is $\frac1T\exp(2\pi i\sum_is_ij_ik_i/t_i)$.",
  r"=\frac1T\exp\left(2\pi i\sum_i", page="bluestein-chirp", frm=["dft","convolution"])
R7 = I("S3.7", r"The retained source permutation cancels across two forward source transforms, their pointwise product and the opposite-sign transform, leaving $(u*v)/S^2$, because $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.",
  r"$RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$", page="permutation-cancellation",
  frm=["resampling-permutations-retained","dft","convolution","modular-arithmetic"])

S3 = S("S3",
 r"A Fourier transform on coprime lengths $s_i$ is expressed through transforms on power-of-two lengths $t_i$ with both coordinate permutations kept inside the identity, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, with the middle transform computed as a chirp convolution and the source permutation $R$ cancelling in a convolution.",
 "Resample each axis by Gaussian maps, leave the two permutations in the formula instead of sorting, rewrite the middle factor as a chirp convolution, and cancel the source permutation in the product.",
 "Gaussian resampling connects these two shapes; its usual implementation sorts twice on each coordinate, and the paper retains both permutations in the transform formula instead.",
 "explicit",
 [R1, R2, R3, R4, R5, R6, R7],
 mquote=r"connects these two shapes. Its usual implementation sorts twice on each",
 page="resampling-permutations-retained",
 frm=["gaussian-resampling","multidimensional-transform","dft","address-chunk-interchange"],
 adds=[B("\\alpha","Gaussian width","the integer width parameter controlling the Gaussian weights, with $2\\le\\alpha<\\sqrt p$","direct"),
       B("\\gamma","source scale exponent","the exponent $\\gamma=2d\\alpha^2$ of the power of two scaling the tensor identity","direct"),
       B("s_i","source length","the prime length of source axis $i$","direct"),
       B("t_i","box length","the power-of-two length of axis $i$ in the padded box, $t_i\\in\\{r/2,r\\}$","direct")])

# -------------- Section 9: assembly ------------------
M1 = S("S4.1",
 r"All sizes are fixed from $b=\lceil\log_2n\rceil$: $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$ and axis lengths $t_i\in\{r/2,r\}$ with product $T$, so that $Tp=\Theta(n)$.",
 "Choose every parameter as a fixed rational power of $b$ so that all cost terms and comparison constants can be verified at once.",
 "We choose compatible parameters for these procedures, recover the integer coefficients from their approximations, and account for the remaining tape operations.",
 "explicit",
 [
  I("S4.1.1", r"The fixed rational exponents are $\tau=\sigma=1-2^{-50}$, $\beta=1/2$, $\delta=1/16$, $\lambda=1-2^{-52}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $C_1=20$, $\epsilon=2^{-75}$, $\kappa=2^{-182}$.",
    r"\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},"),
  I("S4.1.2", r"The sizes are $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$.",
    r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,"),
  I("S4.1.3", r"The axis lengths satisfy $t_i\in\{r/2,r\}$ with $\prod_it_i=T$ and $t_d=r$.",
    r"t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r."),
  I("S4.1.4", r"These choices give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$.",
    r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad"),
  I("S4.1.5", r"The Gaussian width is $\alpha=\lceil(12d^2b)^{1/4}\rceil$, with $\gamma=2d\alpha^2=o(b)$.",
    r"\alpha=\left\lceil(12d^2b)^{1/4}\right\rceil,"),
 ], mquote=r"We choose compatible parameters for these procedures, recover",
 page="parameter-choice", frm=["floor-ceiling-and-logarithms","exponentials-and-elementary-inequalities","simultaneous-butterfly-layer","synthetic-transform-layout"])

M2 = S("S4.2",
 r"Distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ and $\eta=1/(4d)$ exist and are found by trial division in $n^{o(1)}$ time; they give $T/2<S<T$ with $S=\prod_is_i$ and $\alpha^4\theta_i>p$.",
 "Count primes in the two disjoint short intervals below $r/2$ and $r$ by an explicit prime-interval bound, then find them by deterministic trial division.",
 "Each ratio $t_i/s_i$ must leave enough room for resampling, while the product $S$ must fill a fixed fraction of the box.",
 "recoverable",
 [
  I("S4.2.1", r"There are distinct odd primes with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$.",
    r"(1-2\eta)t_i<s_i\leq(1-\eta)t_i."),
  I("S4.2.2", r"The product satisfies $T/2<S<T$.",
    r"Together with $s_i<t_i$, this gives $T/2<S<T$."),
  I("S4.2.3", r"The separations $\theta_i=t_i/s_i-1$ satisfy $\alpha^4\theta_i>p$, so Gaussian resampling applies.",
    r"\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p."),
  I("S4.2.4", r"The deterministic trial-division search takes $n^{o(1)}=o(n)$ time.",
    r"$n^{o(1)}=o(n)$ time."),
 ], page="prime-source-lengths", frm=["prime-numbers-and-trial-division","parameter-choice","exponentials-and-elementary-inequalities"])

M3 = S("S4.3",
 r"Writing both inputs in base $2^b$ with $q=\lceil n/b\rceil$ digits, the product is the convolution of the digit lists, whose coefficients are below $2^{3b}$ and which does not wrap modulo $x^S-1$.",
 "Pad to length $S$ above the degree of the product so the cyclic wrap is vacuous, and bound each coefficient by the number of digit products.",
 "Cyclic convolution can only stand in for the ordinary one if no term wraps, and exact recovery needs coefficients small enough to be rounded.",
 "recoverable",
 [
  I("S4.3.1", r"The product has degree at most $2q-2<2n/b\le T/2<S$, so convolution modulo $x^S-1$ has no wraparound.",
    r"2q-2<2n/b\le T/2<S."),
  I("S4.3.2", r"Every product coefficient satisfies $0\le c_j\le q(2^b-1)^2<2^{3b}$.",
    r"0\le c_j\le q(2^b-1)^2<2^{3b},"),
 ], page="integer-as-digit-convolution", frm=["convolution","binary-representation-and-schoolbook-arithmetic","polynomials"])

M4 = S("S4.4",
 r"The map $\Phi:x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism from cyclic convolution of length $S$ to convolution on the product of the cyclic axes of lengths $s_i$, implemented by triangular controlled shifts in $O(Tp\,d^2(1+\ell^\tau))$ time.",
 "Apply the Chinese remainder theorem to map index $k=\\sum a_jP_j$ to axis coordinates $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j$, a triangular shear computed by prefix-controlled cyclic shifts after reordering the axes.",
 "The Chinese-remainder coordinates are a triangular function of the mixed-radix digits, and the tape procedure of controlled shifts only updates a field using earlier fields in linear time.",
 "recoverable",
 [
  I("S4.4.1", r"$\Phi$ respects $x^S=1$, sends $x$ to an element of order $S$, and is therefore an isomorphism preserving cyclic convolution.",
    r"$\Phi$ is an isomorphism and preserves cyclic convolution."),
  I("S4.4.2", r"The coordinate on axis $i$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, triangular in the mixed-radix digits.",
    r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}."),
  I("S4.4.3", r"The map, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$.",
    r"O\bigl(Tp\,d^2(1+\ell^\tau)\bigr)."),
 ], page="crt-address-map", frm=["modular-arithmetic","controlled-shifts","address-chunk-interchange","prime-source-lengths","convolution"])

M5 = S("S4.5",
 r"Multiplying coefficient $k$ of the last cyclic axis by $\zeta^k$ with $\zeta=e^{\pi i/r}$ is an isomorphism from $\mathbb C[x_d]/(x_d^r-1)$ to $\mathbb C[y]/(y^r+1)$, so complex cyclic convolution is computed by ring convolution and the untwist.",
 "Twist the last coordinate by the diagonal map $x_d\\mapsto\\zeta y$ and untwist after the ring convolution.",
 "The synthetic transforms work modulo y^r+1 while the cyclic axis requires x^r-1; a twist by a primitive 2r-th root converts the negative wrap to the positive one.",
 "recoverable",
 [
  I("S4.5.1", r"The map $x_d\mapsto\zeta y$ is well defined since $(\zeta y)^r=(-1)(-1)=1$.",
    r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."),
  I("S4.5.2", r"A product term after twisting and negacyclic reduction has factor $\zeta^{k+l}(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
    r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j."),
  I("S4.5.3", r"The normalized complex cyclic convolution is $D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$.",
    r"\mathcal M_r(\iota D_+f,\iota D_+g)"),
 ], page="phase-twist", frm=["polynomial-ring-mod-y-r-plus-1","convolution","complex-numbers"])

M6 = S("S4.6",
 r"The approximate source transform resamples with $\mathcal A$ along each axis, applies the chirp transform computed by ring convolution, compresses with $\mathcal B_0$ and rescales by $2^\gamma$; its exact counterpart is $RF_{\boldsymbol s}$.",
 "Compose the Gaussian expansion, the chirp transform whose convolution is the twisted synthetic convolution, the compression, and the exact rescale, and identify the composite with the original source transform.",
 "Together these three pieces realize the identity R F_s = 2^gamma B0 Q F_t A, with every permutation inside the formula and only the convolution requiring the fast layers.",
 "recoverable",
 [
  I("S4.6.1", r"The computed complex convolution is $f'=Q_p(\widetilde\theta^+\cdot f)$, $h'=\widetilde{\mathcal M}_r(\iota f',\iota g')$ and then the untwist, with all phases generated on the grid.",
    r"h'&=\widetilde{\mathcal M}_r(\iota f',\iota g'),"),
  I("S4.6.2", r"The computed chirp transform multiplies by $\overline{\widetilde a}$, convolves with $\widetilde a$ and multiplies by $\overline{\widetilde a}$ again, approximating $QF_{\boldsymbol t}$.",
    r"&=Q_p(\overline{\widetilde a}\mathbin{\cdot}y_0)."),
  I("S4.6.3", r"The exact counterpart of the source transform is $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.",
    r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A"),
 ], page="source-transform",
 frm=["resampling-permutations-retained","bluestein-chirp","synthetic-convolution","phase-twist","gaussian-resampling"])

M7 = S("S4",
 r"Two $n$-bit integers are multiplied by six steps: form radix-$2^b$ digits, apply $\Phi$, compute two source transforms, multiply pointwise, apply the opposite transform, and rescale, round and carry.",
 "Reduce the integer product to a cyclic convolution of radix-$2^b$ digit lists and evaluate it as a pointwise product of source transforms, after setting parameters and building the address map and source transform.",
 "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.",
 "explicit",
 [
  M1, M2, M3, M4, M5, M6,
  I("S4.7", r"The digit $a_j$ is written as the exact grid numerator $a_j2^{p-b-2}$, so the digit lists become disk-grid arrays of norm below $1/4$.",
    r"For digit $a_j$, write the exact grid numerator"),
  I("S4.8", r"Step 1: apply the coefficient-address map $\Phi$ with its padded layout to obtain source arrays $u,v$.",
    r"\item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain"),
  I("S4.9", r"Step 2: compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.",
    r"\item Compute $\widetilde{\mathscr F}(u)$ and"),
  I("S4.10", r"Step 3: multiply corresponding complex coefficients exactly and truncate to $p$ fractional bits, giving $z$.",
    r"\item Multiply corresponding complex coefficients exactly and truncate"),
  I("S4.11", r"Step 4: compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$.",
    r"\item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid"),
  I("S4.12", r"Step 5: multiply exactly by $2^{2b+4}S$, round the real values to integers and apply $\Phi^{-1}$.",
    r"\item Multiply the grid numerators of $\widetilde w$ exactly by"),
  I("S4.13", r"Step 6: propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits.",
    r"\item Propagate radix-$2^b$ carries in increasing coefficient order."),
 ], mquote=r"Splitting the inputs into radix digits reduces multiplication to",
 page="multiplication-algorithm",
 frm=["parameter-choice","integer-as-digit-convolution","crt-address-map","source-transform","permutation-cancellation","convolution"],
 adds=[B("b","digit bit length","the number of bits per radix digit, $b=\\lceil\\log_2n\\rceil$"),
       B("q","digit count","the number of radix-$2^b$ digits of each input, $q=\\lceil n/b\\rceil$"),
       B("S","source box size","the product $\\prod_is_i$ of the prime source lengths, with $T/2<S<T$")])

M8 = S("S5",
 r"Removing the known normalizations $S$ and $2^{2b+4}$, the error of the recovered coefficients is below $1/2$, so rounding gives the integer convolution coefficients and radix-$2^b$ carries give the exact $2n$-bit product.",
 "Track the error through each stage using that the exact maps are contractions and the errors add, bound the scaled error by $448b\\,2^{-b+\\gamma}<1/2$, then round and propagate carries.",
 "The strict error below 1/2 makes the nearest integer to the represented value the unique correct coefficient.",
 "explicit",
 [
  I("S5.1", r"After the three transforms the exact counterpart is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$.",
    r"counterpart after the three transforms is $(u*v)/S^2$, so after the"),
  I("S5.2", r"The source transform error is below $E_sh_p$ with $E_s=9\cdot2^\gamma TL$.",
    r"E_s=9\,2^\gamma TL"),
  I("S5.3", r"The computed first scaled result has error below $E_wh_p$ with $E_w=S(3E_s+2)<28\cdot2^\gamma T^2L$ and norm below $1$.",
    r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
  I("S5.4", r"After the second scaling the final absolute error is below $448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<1/2$.",
    r"<448b\,2^{-b+\gamma}"),
  I("S5.5", r"The carries $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$ stay below $Q_0^2$ and give the exact radix-$2^b$ digits of the product.",
    r"k_{j+1}=\left\lfloor\frac{c_j+k_j}{Q_0}\right\rfloor."),
 ], mquote=r"The strict error below $1/2$ makes the nearest integer to",
 page="exact-recovery",
 frm=["contractions-and-error","permutation-cancellation","parameter-choice","integer-as-digit-convolution","prime-source-lengths","gaussian-resampling"])

M9 = S("S6",
 r"Each of seven dominant normalized costs is at most $p^{1-2\kappa}$, the smallest margin being $2^{-181}=2\kappa$, so the total is $O(Tp\cdot p^{1-\kappa})=O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.",
 "Tabulate the cost of each phase divided by $Tp$ as a power of $p$, compute each margin below one, take the smallest, and absorb logarithmic factors in the slack.",
 "A single margin of $2\\kappa$ below one suffices, so it is enough to compare seven explicit exponents, each a fixed rational expression in the chosen parameters.",
 "recoverable",
 [
  I("S6.1", r"Chunk exchanges for the transform layout cost $pK^{\tau-1}$ per unit volume, a power $1-\epsilon c(1-\tau)$ of $p$.",
    r"Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\"),
  I("S6.2", r"Simultaneous butterfly rounds cost $\ell d^{\lambda'}$ per unit volume, a power $1-\epsilon(1-\lambda')$ of $p$.",
    r"Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\"),
  I("S6.3", r"The margins below one are $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$.",
    r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},"),
  I("S6.4", r"The smallest margin is $\min_ig_i=2^{-181}=2\kappa$.",
    r"Thus $\min_i g_i=2^{-181}=2\kappa$."),
  I("S6.5", r"The chunk exchanges for the layout are $O(p/K)$ exchanges of width $K$, of normalized total $O(pK^{\tau-1})$.",
    r"O(p/K)\,K^\tau=O(pK^{\tau-1})."),
  I("S6.6", r"Each of the seven displayed powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually.",
    r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
  I("S6.7", r"The complete large-input bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
    r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})."),
  I("S6.8", r"Below a fixed cutoff schoolbook multiplication is used, so one machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every $n$.",
    r"Fix one cutoff beyond all the size, precision, margin and layout"),
 ],
 page="cost-analysis",
 frm=["synthetic-transform-layout","simultaneous-butterfly-layer","parameter-choice","multiplication-algorithm","exact-recovery","big-o"],
 salient=r"The exponent $\kappa=2^{-182}$ is half of the smallest margin $g_2=\epsilon c(1-\tau)=2^{-75}\cdot2^{-56}\cdot2^{-50}=2^{-181}$, which is the product of the three tiny exponents $\epsilon$ (number of axes), $c$ (chunk width) and $1-\tau$ (interchange saving), the chunk-exchange row of the cost table.")

ROOT = S("S0",
 r"One deterministic fixed-alphabet, fixed-tape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, so no eventual $\Omega(n\log n)$ lower bound holds for it.",
 "Build two fast tape procedures from fixed linear networks with a rank deficit, use them to accelerate synthetic polynomial transforms, reduce integer multiplication through radix digits, Chinese-remainder axes, Gaussian resampling and chirps to such convolutions, then recover the exact product and tally the cost.",
 "Scanning an array of n bits at each of log n transform levels already costs n log n, so we therefore need savings in both movement and arithmetic.",
 "explicit",
 [G1, S2, S3, M7, M8, M9],
 mquote=r"We therefore need savings in both movement and arithmetic.",
 page="integer-multiplication-below-nlogn",
 frm=["nlogn-conjecture","big-o","turing-machine-tapes","deterministic-algorithms-and-worst-case-time","karatsuba-and-classical-multiplication-algorithms"],
 adds=[B("p","working precision","the number of fractional bits of the fixed-point complex values, $p=6\\lceil\\log_2n\\rceil$"),
       B("d","axis count","the number of axes of the transform box, a tiny power of $p$"),
       B("r","record length","the number of complex coefficients in each polynomial record, a power of two"),
       B("T","box size","the number of entries of the padded transform box, a power of two near $4n/b$ to $8n/b$")],
 salient=r"The saving is a genuine power of the logarithm but astronomically small, $\kappa=2^{-182}$: the exponent is the product of three tiny exponents and a strict rank deficit that is only about $10^{-11}$ of the network size.")

# ------------------ validation -----------------------
def walk(n, depth=0):
    yield n
    for c in n.get("children", []) or []:
        yield from walk(c, depth+1)

def check():
    errs = []
    ids = set()
    pos = -1
    pages_used = {}
    for n in walk(ROOT):
        if n["id"] in ids: errs.append("dup id " + n["id"])
        ids.add(n["id"])
        if n.get("page"):
            if n["page"] in pages_used: errs.append("page used twice " + n["page"])
            pages_used[n["page"]] = n["id"]
            if n["page"] not in IDX: errs.append("bad page " + n["page"])
    # effective page
    def rec(n, eff):
        e = n.get("page") or eff
        for f in n.get("from", []):
            if f in IDX:
                if IDX[f] >= IDX[e]: errs.append(f"{n['id']}: from {f} not before page {e}")
            elif f not in KNOWN: errs.append(f"{n['id']}: unknown from {f}")
        for c in n.get("children", []) or []:
            rec(c, e)
    rec(ROOT, "integer-multiplication-below-nlogn")
    # quotes
    last = -1
    def quote_check(q, where):
        c = SRC.count(q)
        if c == 0: errs.append(f"{where}: quote not found: {q!r}")
        elif c > 1: errs.append(f"{where}: quote not unique ({c}): {q!r}")
        return SRC.find(q)
    for n in walk(ROOT):
        if n["intention"] == "infer":
            p = quote_check(n["quote"]["quote"], n["id"])
            if not n.get("deferred"):
                if p <= last: errs.append(f"{n['id']}: out of order (pos {p} <= {last})")
                last = max(last, p)
        else:
            q = n["motivation"].get("quote")
            if q: quote_check(q["quote"], n["id"] + " motivation")
            if n["motivation"]["source"] == "explicit" and not q: errs.append(n["id"] + " explicit without quote")
            if not n.get("children"): errs.append(n["id"] + " show without children")
    # page coverage
    inform = set()
    for n in walk(ROOT):
        for f in n.get("from", []): inform.add(f)
    for p in ORDER:
        if p not in pages_used and p not in inform: errs.append("page unused: " + p)
    # adds
    for n in walk(ROOT):
        for a in n.get("adds", []) or []:
            sym = a["symbol"]
            found = False
            for d in walk(n):
                if d is n: continue
                for m in re.findall(r"\$(.*?)\$", d["claim"]):
                    if sym in m: found = True
            if not found: errs.append(f"{n['id']}: add {sym} not in descendants' math")
    return errs

if __name__ == "__main__":
    errs = check()
    for e in errs: print("ERR", e)
    out = BASE + "/exegenius/tasks/0052-argument.answer.json"
    json.dump({"root": ROOT}, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("written; errors:", len(errs))
