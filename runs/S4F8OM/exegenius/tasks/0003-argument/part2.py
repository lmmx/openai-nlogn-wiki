"""S2: the simultaneous butterfly layer."""
from tree_helpers import show, infer, mot, bind

# ---------------------------------------------------------------- S2.1
S211 = show(
    "S2.1.1",
    r"For every edge between binary labels $U\subset V$, the phase-frame change $\mathcal C_V\mathcal C_U^{-1}$ is a product of one translation kernel $aI+bX_v$ or its inverse per vector $v$ of an orthonormal basis of the residual, these kernels number $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$ over the network, and after sign corrections the telescoped endpoint operator is $C^{\otimes m}$ on every role.",
    r"Split the phase difference along an orthonormal residual basis using that Hamming weight is additive modulo four over orthogonal binary vectors, conjugate each factor by $H^{\otimes m}$ into a translation kernel, and repair the exchanged pair with $Z$ signs and a scalar phase.",
    mot(r"All phase frames are diagonalized by the same matrix $H^{\otimes m}$, so a frame change is a diagonal phase that factors along residual directions, and each factor becomes a cheap two-point kernel rather than a general operator.",
        "explicit",
        r"All frames are diagonalized by the same matrix $H^{\otimes m}$."),
    [
        infer("S2.1.1.1",
              r"Every nonzero edge residual of the binary labels is nondegenerate and contains a vector of norm one, so it is nonalternating and, by splitting off unit lines and absorbing alternating planes, has an orthonormal basis.",
              r"Thus every nonzero residual is nonalternating.",
              deferred=True),
        infer("S2.1.1.2",
              r"For binary vectors with $z\cdot w=0$ the supports meet in an even number of points, so $\operatorname{wt}(z+w)\equiv\operatorname{wt}(z)+\operatorname{wt}(w)\pmod4$, and for nested labels $V=U\perp E$ the phase exponent changes by $q_V(x)-q_U(x)=\sum_v\operatorname{wt}(v)[v\cdot x]\pmod4$ over an orthonormal basis of $E$.",
              r"If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four.",
              deferred=True),
        infer("S2.1.1.3",
              r"Each basis vector $v$ has odd weight, so its factor $i^{\pm[v\cdot x]}=\frac{1+i^{\pm1}}2+\frac{1-i^{\pm1}}2(-1)^{v\cdot x}$, conjugated by $H^{\otimes m}$, becomes the translation kernel $aI+bX_v$ or its inverse, where $(X_vg)(x)=g(x+v)$.",
              r"The displayed phase therefore becomes $aI+bX_v$ or its inverse.",
              deferred=True),
        infer("S2.1.1.4",
              r"The residual dimensions, hence the kernels, number $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$, short of $W_{\rm c}m$ by $2N-2L_{\rm c}>0$ since $L_{\rm c}/N=101/539<1/2$.",
              r"The deficit is $2N-2L_{\rm c}>0$.",
              deferred=True),
        infer("S2.1.1.5",
              r"Zero labels have frame $I$ and full labels frame $C^{\otimes m}$; on the exchanged pair $X_a\to Y_a$ the telescoped operator is $C^{-1}$ on the 27 support coordinates of $u_a$ and $C$ elsewhere, which $Z$ sign corrections before and after the network and a scalar $i^{27k}$ on $k$ columns turn into $C^{\otimes mk}$.",
              r"The operator on this pair is therefore $C^{\otimes mk}$ as well.",
              deferred=True),
    ],
    frm=["subset-intersection-labels", "array-frames", "scratch-restoring-exchange", "rank-and-orthogonal-subspaces", "arithmetic-modulo-2-and-xor"],
)

S212 = show(
    "S2.1.2",
    r"On a group of $e=mf$ selected axes split into $m$ slots of $f$ chunks, a binary change of basis per edge turns each kernel into a forward call $C^{\otimes f}$ on one whole slot, so one network invocation makes exactly $s_{\rm c}$ child calls and yields $C^{\otimes e}$ on every role.",
    r"Conjugate by the address permutation $\mathcal P_M$ of a matrix $M\in\operatorname{GL}(m,\mathbb F_2)$ whose first columns are the residual basis, applied column by column, and rewrite inverse kernels through $C^{-1}=-iZCZ$.",
    mot(r"A kernel along an arbitrary direction $v$ would act on scattered address bits; a change of basis that sends $v$ to a coordinate direction makes it act on one slot of contiguous chunks, which is a smaller call of the same procedure.",
        "explicit",
        r"The next step puts those directions into coordinate positions without performing a general transpose."),
    [
        infer("S2.1.2.1",
              r"Choosing $M\in\operatorname{GL}(m,\mathbb F_2)$ whose first columns are a residual basis, $\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}$ turns an edge's kernels into $C^{\pm1}$ applied to whole slots of $f$ chunks between two column-wise changes of basis, and $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$ makes each inverse kernel a single forward call.",
              r"All inverse wrappers are address signs and constant fourth-root phases, so they add no recursive calls."),
        infer("S2.1.2.2",
              r"Summing the residual dimensions, one network invocation on $e=mf$ axes makes exactly $s_{\rm c}$ child calls on $f$ axes and, with the endpoint sign corrections and the undoing of the signed bank exchange, yields $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary.",
              r"Proposition~\ref{prop:complex-motif-interface} therefore gives $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary."),
    ],
    frm=["arithmetic-modulo-2-and-xor", "matrices-vectors-and-linear-maps", "packed-selected-bit-addition"],
)

S21 = show(
    "S2.1",
    r"For a group of $e=mf$ selected axes split into $m$ slots of $f$ chunks, the complex network run with phase frames yields $C^{\otimes e}$ on every role, scratch roles included, using exactly $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$ forward child calls $C^{\otimes f}$, each on the $f$ chunks of one slot, plus a fixed number of binary row additions and exact sign and phase operations.",
    r"Label the complex network with binary subspaces and use the frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$ with $q_U(x)=\operatorname{wt}(P_Ux)\bmod4$, whose edge changes factor into one translation kernel $aI+bX_v$ per orthonormal residual vector; move each kernel's direction onto a slot by an invertible binary change of basis.",
    mot(r"Hamming weight is additive modulo four over orthogonal binary vectors, so a frame change between nested labels splits into independent two-point kernels, one per residual direction; after a change of basis each kernel acts on whole slots and is a smaller instance of the same layer.",
        "explicit",
        r"The phase identities below express an edge's residual operator as a product of two-point kernels on selected directions."),
    [S211, S212],
    page="phase-frame-network",
    frm=["subset-intersection-labels", "array-frames", "scratch-restoring-exchange", "rank-and-orthogonal-subspaces", "arithmetic-modulo-2-and-xor", "complex-numbers"],
    adds=[
        bind("e", "group size", "The number of selected axes handled by one invocation of the complex network.", "count"),
        bind("f", "slot size", r"The number of axis chunks in each of the $m$ slots, $e/m$.", "count"),
    ],
)

# ---------------------------------------------------------------- S2.2
S22 = infer(
    "S2.2",
    r"Since $H_0=b\mathsf SC\mathsf S$ with $\mathsf S=\operatorname{diag}(1,i)$, the normalized layer is $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, where $\mathcal S_D$ multiplies the record at an address by $i$ raised to the number of its selected bits equal to one and $b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}$ is a binary shift with a fourth-root phase, so every correction is an exact Gaussian dyadic operation.",
    r"Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.",
    frm=["fft-butterflies", "complex-numbers", "dyadic-rationals-and-fixed-width-numerators"],
)

# ---------------------------------------------------------------- S2.3
S23 = show(
    "S2.3",
    r"On records over three chunks $x,y,z$ of $fK$ bits each and arbitrary spectator fields, the XORs $y_j\gets y_j\oplus x_j$ at $f$ selected positions spaced $K$ bits apart can be performed, restoring $z$ for every initial value, in $O(V((fK)^\tau+1))$ time whenever the records are longer than every fixed power of $p$ and $K/\log p\to\infty$.",
    r"Read each $K$-bit segment of $y$ and $z$ as an integer, apply eight conditional $\pm1$ updates that flip the parity of the $y$-segment exactly when its control bit is one and restore the $z$-segment, perform each update on all segments at once as one cyclic shift of a whole chunk, then repair by sorting the few addresses where some segment would carry into its neighbor.",
    mot(r"A cyclic shift of a whole chunk by an offset computed from the control chunks adds to all of its segments at once, at the price of a chunk interchange and a linear scan, so one shift does the work of $f$ bit operations; carries between segments occur only near the ends of a guard range, for a fraction $O(f2^{-K})$ of addresses, which is cheap to repair.",
        "recoverable"),
    [
        infer("S2.3.1",
              r"For a control bit $c$ and integers $u,w$, the eight updates induce the cycle $(00\ 01\ 10)$ and then $(01\ 10\ 11)$ on parity pairs, so $(u',w')=(u+c(1-2(u\bmod2)),w)$: the parity of $u$ flips exactly when $c=1$, both quotients by two are kept, and $w$ is restored.",
              r"Thus the parity of $u$ is flipped precisely when $c=1$, both quotients under division by two are preserved, and the arbitrary auxiliary integer $w$ is restored."),
        infer("S2.3.2",
              r"Each update line, applied to all segment pairs below the top selected position at once, is a single cyclic shift of the target chunk by an offset computed from the other two chunks, and outside the set $\mathcal B$ of addresses where some guard value leaves $[10,2^{K-1}-11]$ no segment carries into or borrows from the next, so the composed shifts $S_0$ agree with the ideal XOR map $T_0$.",
              r"Inductively, each packed addition therefore agrees with all the independent segment additions: no segment carries into or borrows from the next segment."),
        infer("S2.3.3",
              r"Each guard excludes twenty of its $2^{K-1}$ values, so a union bound over the $2(f-1)$ guards bounds the fraction of records in $\mathcal B$ by $\min\{1,80(f-1)2^{-K}\}$, independently of the payload.",
              r"Since its complete range has $2^{K-1}$ values, the union bound over the $2(f-1)$ guards gives"),
        infer("S2.3.4",
              r"Since $S_0$ and $T_0$ are bijections that agree off $\mathcal B$ and $T_0$ keeps guard values, $T_0S_0^{-1}$ only permutes $\mathcal B$; the exceptional records are extracted with their destination ranks, radix-sorted and reinserted, which implements $T_0$ everywhere, and one two-bit XOR supplies the top selected position.",
              r"This implements $T_0$ everywhere."),
        infer("S2.3.5",
              r"The shifts and chunk interchanges cost $O(V((fK)^\tau+1))$, while the record scans and the repair cost, per stored bit, a polynomial in $p$ divided by the record length plus $O(p^22^{-K})$, both $o(1)$ when records outgrow every power of $p$ and $K/\log p\to\infty$.",
              r"Under the stated family bounds the first tends to zero, and the second is $O(p^2 2^{-K}(1+A_{\rm rect}/R))=o(1)$."),
    ],
    page="packed-selected-bit-addition",
    frm=["address-chunk-interchange", "controlled-cyclic-shift", "tape-address-model", "arithmetic-modulo-2-and-xor", "sorting-and-its-cost", "cyclic-shifts-and-rotations-of-lists"],
    salient=r"Eight conditional $\pm1$ updates flip the parity of $u$ exactly when $c=1$ and return the arbitrary auxiliary integer $w$ to its initial value, moving each coordinate by at most four.",
    adds=[
        bind(r"\mathcal B", "exceptional set", "The addresses at which some guard value lies within ten of an end of its range, where a packed shift could carry between segments.", "direct"),
    ],
)

# ---------------------------------------------------------------- S2.4
S24 = show(
    "S2.4",
    r"The exact $C^{\otimes D}$ part of the layer costs $O(Vd^{\lambda'})$: per stored bit a node on $e$ chunks costs at most $(s/W)F(e/m)+O((eK)^\tau+1)$, a leaf with $e<d^{1/2}$ costs $O(e)$, and summing over the base-$m$ groups of chunks gives $O(d^{\lambda'})$.",
    r"Bound the work at a node (changes of basis by packed additions, scalar gates, individual kernels), supply rows from the first chunks so that each child gets $1/W$ of the volume, and unroll the volume-normalized recurrence.",
    mot(r"As for address interchange, the rank saving $s/W\le m^\sigma$ with $\sigma<1$ makes the recursive part grow like $e^\sigma$; the node overhead $(eK)^\tau$ is a smaller power because the chunk width $K=\lfloor d^c\rfloor$ is tiny compared with $e\ge d^{1/2}$.",
        "recoverable"),
    [
        infer("S2.4.1",
              r"A binary change of basis of fixed order $m$ is a fixed number of row additions, each one packed selected-bit addition on slots of $(e/m)K$ bits, so a change of basis and its inverse cost $O(V((eK)^\tau+1))$.",
              r"the complete change of basis and its inverse therefore cost $O(V((eK)^\tau+1))$ on a stream of volume $V$."),
        infer("S2.4.2",
              r"An individual kernel $C(u,v)=((u+v+i(u-v))/2,(u+v-i(u-v))/2)$ on one selected bit is a split, an aligned coefficient scan and a merge costing $O(V)$, so $e$ individual kernels cost $O(Ve)$.",
              r"Thus \(e\) individual kernels cost \(O(Ve)\) on any stream with these complete ranges and record format."),
        infer("S2.4.3",
              r"Applying $C$ individually to the first $O(\log d)$ chunks lets their bits serve as a row index of range at least $W^{\lceil\log_md\rceil}$; padded with zero rows and split cyclically among the $W$ roles, it gives every recursive call a stream of exactly $1/W$ of its parent's volume with complete address suffixes.",
              r"Each recursive edge call acts on one role stream with volume exactly \(1/W\) of its parent's logical volume."),
        infer("S2.4.4",
              r"Hence the time $F(e)$ per stored bit satisfies $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, because the $s$ children run on volume $V/W$, with $F(e)=O(e)$ below $e<d^{1/2}$.",
              r"Dividing by the current volume \(V\) gives the factor \(s/W\)."),
        infer("S2.4.5",
              r"At internal nodes $K\le e^{2c}$, so the overhead is $O(e^\lambda)$, and with $s/W\le m^\sigma<m^\lambda$ the internal costs sum to $O(e^\lambda)$, the leaves contribute $O(e^\sigma d^{(1-\sigma)/2})$, and the $O(\log d)$ base-$m$ groups give $O(d^{\lambda'})$ for any fixed $\lambda'$ between $\max\{\lambda,(1+\sigma)/2\}$ and $1$.",
              r"Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most"),
    ],
    frm=["rank-saving-recurrence", "packed-selected-bit-addition", "phase-frame-network", "geometric-series-and-sums"],
    adds=[
        bind(r"\sigma", "network exponent", r"The fixed exponent $1-2^{-50}$ with $s_{\rm c}/W_{\rm c}\le m^\sigma$ for the complex network.", "direct"),
        bind(r"\lambda", "overhead exponent", r"The fixed exponent $1-2^{-52}$ bounding the per-node overhead $(eK)^\tau$ by $e^\lambda$.", "direct"),
    ],
)

# ---------------------------------------------------------------- S2.5
S25 = show(
    "S2.5",
    r"With $p+\Delta$ fractional and $\Delta+3$ integer and sign bits per component, $\Delta=\lceil C_0d^{20}\rceil=o(p)$, every intermediate value of the layer is exact, and the single final truncation returns unit-disk values within $\sqrt2\,2^{-p}$ of $H_0^{\otimes D}$ applied to the input.",
    r"Bound the arithmetic depth of the recursion, use that each elementary operation at most doubles the modulus and adds at most one denominator bit, and use that $H_0^{\otimes D}$ has absolute row sums one.",
    mot(r"The network's intermediate operators are not contractions, so rounding inside the recursion could let errors grow; computing exactly with enough guard bits and truncating once keeps the whole layer's error below one grid unit while the width stays $O(p)$.",
        "explicit",
        r"The accelerated network is evaluated exactly until an entire normalized butterfly layer is complete.  Its intermediate operators need not be contractions."),
    [
        infer("S2.5.1",
              r"A chain of elementary operations gains at most $E=64(W+m+1)^3$ per network invocation and at most $8e$ at a leaf, so $A(e)\le sA(e/m)+E$ gives arithmetic depth at most $8dB^{k+1}\le8B^2d^{\nu+1}$ with $B=s+E$, and at most $C_0d^{20}$ with the outer phases and scale.",
              r"A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}."),
        infer("S2.5.2",
              r"A value at depth $j$ lies in $2^{-(p+j)}\mathbb Z[i]$ with modulus at most $2^j$, since an addition at most doubles the modulus and a halving adds one denominator bit, so $p+\Delta$ fractional and $\Delta+3$ integer and sign bits represent every intermediate coefficient exactly.",
              r"Thus reserving \(p+\Delta\) fractional bits and \(\Delta+3\) integer and sign bits per real component represents every intermediate coefficient exactly and prevents overflow."),
        infer("S2.5.3",
              r"Since $d=\Theta(p^\epsilon)$ with $20\epsilon<1$, $\Delta=o(p)$ and the guarded coefficient width stays $O(p)$, as the time analysis requires.",
              r"Choose \(\epsilon C_1<1\).  Since \(d=\Theta(p^\epsilon)\), \(\Delta=o(p)\), and the full coefficient width is \(O(p)\), as required in the time analysis."),
        infer("S2.5.4",
              r"Every row of $H_0^{\otimes D}$ has absolute row sum one, so it maps disk arrays to disk arrays, and truncating each component toward zero keeps the disk and errs by less than $\sqrt2\,2^{-p}$.",
              r"Finally, every row of $\mathcal H$ has absolute row sum one."),
    ],
    frm=["fixed-point-complex-arithmetic", "dyadic-rationals-and-fixed-width-numerators", "triangle-inequality-and-norms"],
    adds=[
        bind(r"\Delta", "guard width", r"The number of extra fractional bits, and of extra integer bits, reserved per component, $\lceil C_0d^{20}\rceil$.", "count"),
    ],
)

# ---------------------------------------------------------------- S2
S2 = show(
    "S2",
    r"On an array with addresses $[P]\times[2^K]^D\times[S]$, $1\le D\le d$, whose records are polynomials of $r$ complex fixed-point coefficients in the unit disk, applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ at once to the bit at one common offset of each of the $D$ chunks, followed by a single truncation to the $2^{-p}$ grid, takes $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$, with error below $\sqrt2\,2^{-p}$ and output in the unit disk.",
    r"Rewrite $H_0^{\otimes D}$ as diagonal phases around $C^{\otimes D}$ for the two-point kernel $C=aI+bX$; build $C^{\otimes e}$ by running the complex phase network on $W$ row streams with one recursive call on $e/m$ chunks per residual basis vector; realize the binary changes of basis by packed selected-bit additions; and evaluate the whole layer exactly with $o(p)$ guard bits before one truncation.",
    mot(r"Applying the $D$ butterfly factors one at a time costs $D$ passes over the array; the phase network replaces them by a recursion with $s<Wm$ calls on $1/W$ of the volume, the same rank saving as for address interchange, so a whole layer costs fewer than $d$ passes.",
        "explicit",
        r"We will obtain cost $O(Vd^{\lambda'})$, with $\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly factors would require $D$ whole-array passes."),
    [S21, S22, S23, S24, S25],
    page="simultaneous-butterfly-layer",
    frm=["fft-butterflies", "fixed-point-complex-arithmetic", "rank-saving-recurrence", "address-chunk-interchange", "complex-numbers"],
    salient=r"All $D$ butterfly factors together cost $O(Vd^{\lambda'})$, less than the $D$ separate passes they would otherwise need, although every factor touches every coefficient.",
    adds=[
        bind("D", "selected chunk count", r"The number of address chunks whose selected bit the layer acts on, at most $d$.", "count"),
        bind("K", "chunk width", r"The number of bits in each address chunk, $\lfloor d^c\rfloor$.", "count"),
        bind("C", "two-point kernel", r"The matrix $aI+bX$ with $a=(1+i)/2$ and $b=(1-i)/2$, equal to $H\operatorname{diag}(1,i)H$, from which the butterfly layer is built.", "direct"),
        bind(r"\lambda'", "layer exponent", r"The fixed exponent below one, $1-2^{-54}$, in the layer cost.", "direct"),
    ],
)
