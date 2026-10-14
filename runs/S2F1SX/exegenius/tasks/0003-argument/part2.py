from lib import *

phase_network = inf(
    "S2.1",
    r"The complex network with binary labels, whose frames are the phase operators $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{\operatorname{wt}(P_Ux)\bmod 4})H^{\otimes m}$, has edge changes that are products of kernels $aI+bX_v$ (one per vector of an orthonormal basis of the residual), endpoint operator $C^{\otimes m}$ on every role, and edge-rank sum $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$.",
    r"s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}",
    page="phase-network",
    frm=["subset-labels", "frames", "rank-saving", "butterfly-fft", "binary-field-f2-and-xor", "complex-numbers"],
    deferred=True,
    salient=r"Unlike the bit network, the count $s_{\rm c}$ has no extra source ranks, because the source and sink corrections are diagonal sign operators $Z$ and scalar phases that cost no recursive call; the deficit $2N-2L_{\rm c}$ is still positive.",
)

edge_frame = inf(
    "S2.2",
    r"On a group of $e=mf$ axes an edge's frame change is done by undoing a basis change $\mathcal P_M^{-1}$ on each column of selected bits, applying $(C^{\epsilon_h})^{\otimes f}$ to the $f$ axes of slot $h$ for each residual direction $h\le\rho_{\rm edge}$, then applying $\mathcal P_M$; an inverse kernel needs only one forward call by $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$.",
    r"$1\le h\le\rho_{\rm edge}$, apply $(C^{\epsilon_h})^{\otimes f}$ to the",
    frm=["phase-network", "butterfly-fft"],
)

child_calls = inf(
    "S2.3",
    r"One invocation of the network on $e=mf$ selected axes makes exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and none of the endpoint corrections adds a call, so $C^{\otimes e}$ results on every role including scratch roles of arbitrary initial value.",
    r"$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
)

back_to_h0 = inf(
    "S2.4",
    r"The normalized layer is recovered from the $C$-layer by exact diagonal phases and a dyadic scalar: $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$.",
    r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D.",
    frm=["butterfly-fft", "dyadic-rationals-and-binary-fractions"],
)

packed = show(
    "S2.5",
    r"On $f$ chunks at once, $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ at the positions $j_i=\rho+iK$ is performed in $O(V(L^\tau+1))$ time, $L=fK$, restoring a third chunk $z$ of arbitrary initial value, once exceptional addresses are repaired.",
    "Add controlled unit steps to the packed integers by eight cyclic shifts of whole chunk ranges that act as the required XOR away from a small bad set, then repair that explicitly identified set by sorting only its records.",
    ("explicit", "The sources first use a constant number of chunk rotations and then correct an explicitly bounded set of addresses.",
     r"of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of"),
    [
        inf("S2.5a",
            r"For a control bit $c$ and arbitrary integers $u,w$, the eight chronological operations compose to $(u,w)\mapsto(u+c(1-2(u\bmod2)),w)$: the first four induce the cycle $(00\ 01\ 10)$ and the last four $(01\ 10\ 11)$ on parities, which compose to $(00\ 10)(01\ 11)$, so the parity of $u$ flips exactly when $c=1$ and $w$ is restored.",
            r"\bigl(u+c(1-2(u\bmod2)),\ w\bigr).",
            salient=r"The scratch integer $w$ is returned to its initial value for every $w$, because the two three-cycles on the parity squares multiply to a product of two transpositions that fixes the parity of $w$."),
        inf("S2.5b",
            r"Away from the bad set $\mathcal B$ (an address where some guard value falls outside $10\le g\le2^{K-1}-11$), displacement at most eight keeps each $K$-bit segment inside its range, so no segment carries into or borrows from its neighbour and the packed shifts equal the ideal XORs.",
            r"Inductively, each packed addition therefore agrees with all"),
        inf("S2.5c",
            r"Each guard excludes exactly twenty of its $2^{K-1}$ values, so a union bound over the $2(f-1)$ guards gives $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, independently of the payload.",
            r"the union bound over the $2(f-1)$ guards gives"),
        inf("S2.5d",
            r"The ideal map $T_0$ and the shift composition $S_0$ are bijections agreeing off $\mathcal B$ and both preserve $\mathcal B$, so $T_0S_0^{-1}$ fixes $\mathcal B^c$ and merely permutes $\mathcal B$.",
            r"Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$."),
        inf("S2.5e",
            r"The permutation of $\mathcal B$ is applied by extracting those records with their distinct destination ranks, stable radix sorting only the extracted records and keys, and reinserting them in one forward scan.",
            r"while stable binary radix sorting scans only the extracted records and"),
        inf("S2.5f",
            r"The total time is $O\!\left(V(L^\tau+1)+MA^3+\delta_{\rm bad}MA(R+A)\right)$, and the last two terms are $o(V)$ when the record width $R$ exceeds every polynomial in $p$ and $K/\log p\to\infty$; for $f=1$ the shifts and $\mathcal B$ are trivial.",
            r"The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans"),
    ],
    page="packed-bit-addition",
    frm=["chunk-interchange", "controlled-shifts", "binary-field-f2-and-xor"],
)

change_of_basis = inf(
    "S2.6",
    r"Any fixed invertible binary change of basis on $e=mf$ chunks, being a fixed number of row additions, costs $O(V((eK)^\tau+1))$.",
    r"$O(V((eK)^\tau+1))$ on a stream of volume $V$.  Here $e$ counts",
    frm=["packed-bit-addition", "chunk-interchange"],
)

unroll = show(
    "S2.7",
    r"The whole layer recurrence $F(e)\le(s_{\rm c}/W_{\rm c})F(e/m)+O((eK)^\tau+1)$ solves to cost $O(Vd^{\lambda'})$ with $\lambda'<1$.",
    "Take rows from the first few chunks, split each row index among the $W_{\rm c}$ roles, and solve the recursion as a geometric sum with a cutoff for small groups.",
    ("recoverable", r"Splitting a row index among the roles makes each child's volume $V/W_{\rm c}$, so the ratio $s_{\rm c}/W_{\rm c}<m^\sigma$ controls the geometric sum, as in the interchange recursion."),
    [
        inf("S2.7a",
            r"Rows come from the first $q_0$ chunks, padded to a multiple of $W_{\rm c}^{k_0}$; at each node a row index $u=Wg+w$ sends the whole row to role $w$, so every child stream has exactly $1/W_{\rm c}$ of the parent's volume and keeps the full suffix.",
            r"At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\),"),
        inf("S2.7b",
            r"With $\beta=1/2$ and individual kernels below $d^\beta$ chunks, $F(e)\le(s_{\rm c}/W_{\rm c})F(e/m)+O((eK)^\tau+1)$ and $F(e)=O(e)$ for $e<d^\beta$.",
            r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
        inf("S2.7c",
            r"At an internal node $e\ge d^\beta$, so $K\le d^c\le e^{c/\beta}$ and the overhead is $O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)$ when $\tau(1+c/\beta)<\lambda$.",
            r"\(K\le d^c\le e^{c/\beta}\).  The overhead is therefore"),
        inf("S2.7d",
            r"With $a=s_{\rm c}/W_{\rm c}\le m^\sigma<m^\lambda$ the internal costs sum to $Ce^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)$, while leaves of $u<d^\beta$ chunks contribute $O(e^\sigma d^{\beta(1-\sigma)})$.",
            r"C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)."),
        inf("S2.7e",
            r"Partitioning $D-q_0$ in base $m$ into at most $(m-1)(1+\lfloor\log_m d\rfloor)$ pieces gives total $O(\log(2d)[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1])=O(d^{\lambda'})$ for any $\lambda'$ with $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$.",
            r"\bigl[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1\bigr]\right)"),
    ],
    frm=["power-saving-recurrence"],
)

guard = show(
    "S2.8",
    r"The exact $C$-layer needs at most $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$ extra fractional and integer bits, so all intermediate Gaussian dyadics fit in width $O(p)$ and nothing is rounded until the last truncation.",
    "Bound the number of additions, halvings and sign changes on any dependency chain by a recursion with branching $s_{\\rm c}$, then convert depth to denominator and magnitude growth.",
    ("explicit", "Intermediate operators of the accelerated network are not contractions, so the layer must be evaluated exactly and only then truncated.",
     r"need not be contractions."),
    [
        inf("S2.8a",
            r"The depth $A(e)$ of arithmetic on any dependency chain satisfies $A(e)\le sA(e/m)+E$ at an internal node (branching $s$, not $s/W$) and $A(e)\le8e$ at a leaf.",
            r"A(e)\le sA(e/m)+E"),
        inf("S2.8b",
            r"With $B=s+E$ and at most $\lceil\log_m d\rceil$ levels, $A(e)\le8dB^{k+1}\le8B^2d^{\nu+1}$.",
            r"A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}."),
        inf("S2.8c",
            r"Adding the piece count, the diagonal phases and the dyadic shift gives a common bound $C_0d^{C_1}$ with $C_1=20$ on denominator growth and magnitude growth.",
            r"&<128mB^2d^{\nu+3}\le C_0d^{C_1}."),
        inf("S2.8d",
            r"A value at depth $\ell$ lies in $2^{-(p+\ell)}\mathbb Z[i]$ with modulus at most $2^\ell$, so $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits per component represent every intermediate value exactly, and $\epsilon C_1<1$ makes this $O(p)$.",
            r"the same as \(t\) successive halvings.  Thus reserving \(p+\Delta\)"),
    ],
    frm=["fixed-point-disk-grid", "dyadic-rationals-and-binary-fractions"],
    adds=[sym("\\Delta", "guard width", "The number $\\lceil C_0d^{C_1}\\rceil$ of extra fractional bits and integer bits reserved for the exact layer.", "count")],
)

final_layer = inf(
    "S2.9",
    r"Every row of $H_0^{\otimes D}$ has absolute row sum one, so it maps disk arrays to disk arrays, and the single truncation $Q_p$ keeps the disk and errs by less than $\sqrt2\,2^{-p}$.",
    r"absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk",
    frm=["fixed-point-disk-grid", "vector-norms-and-error-bounds"],
)

S2 = show(
    "S2",
    r"A simultaneous normalized butterfly layer $H_0^{\otimes D}$ on one common bit position of each of $D\le d$ consecutive $K$-bit address chunks of polynomial records of precision $p$ runs in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$, with one final truncation of error below $\sqrt2\,2^{-p}$.",
    "Evaluate the layer exactly through the complex phase network, whose edge changes become kernels on groups of $e/m$ axes (smaller layers on streams of volume $V/W_{\\rm c}$), implement its binary basis changes by packed selected-bit addition, and truncate once at the end.",
    ("explicit", "Separate butterfly factors would need D whole-array passes, so all D are done in one recursive layer.",
     r"factors would require $D$ whole-array passes."),
    [phase_network, edge_frame, child_calls, back_to_h0, packed, change_of_basis, unroll, guard, final_layer],
    page="simultaneous-layer",
    frm=["phase-network", "packed-bit-addition", "power-saving-recurrence", "butterfly-fft", "fixed-point-disk-grid", "chunk-interchange"],
    adds=[
        sym("f", "slot width", "The number of chunks in each of the $m$ slots of a group of $e=mf$ selected axes.", "count"),
        sym("W_{\\rm c}", "complex wire count", "The number of wires of the complex phase network.", "count"),
        sym("s_{\\rm c}", "complex call count", "The sum of the ranks of the edge changes of the phase network, which is the number of child layers one run makes.", "count"),
        sym("\\beta", "cutoff exponent", "The exponent $\\beta=1/2$ below which groups of fewer than $d^\\beta$ chunks are handled by individual kernels.", "direct"),
        sym("\\sigma", "recurrence exponent", "A fixed exponent with $\\log_m(s_{\\rm c}/W_{\\rm c})\\le\\sigma<1$ bounding the growth of the recursive calls.", "direct"),
        sym("\\lambda", "internal-cost exponent", "A fixed exponent with $\\max\\{\\tau,\\sigma\\}<\\lambda<1$ bounding the per-node overhead after unrolling.", "direct"),
        sym("\\lambda'", "layer exponent", "A fixed exponent with $0<\\lambda'<1$ in the cost $O(Vd^{\\lambda'})$ of a layer.", "direct"),
    ],
    salient=r"The cost per bit is $d^{\lambda'}$ with $\lambda'<1$ although $D$ butterflies are applied, whereas applying them one after another would cost a factor $D$; as for the interchange, this holds because the recursion makes $s_{\rm c}$ calls on streams of $1/W_{\rm c}$ the volume with $s_{\rm c}/W_{\rm c}<m^\sigma$.",
)
