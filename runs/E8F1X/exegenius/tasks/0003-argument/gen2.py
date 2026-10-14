# Part 2: S1 (chunk interchange) and S2 (simultaneous layer)
import os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"gen1.py")).read())

stream_ops = infer(
 "S1.1",
 r"Permuting the values of two radix-$q$ digit positions, moving one digit, splitting on a digit with a pointwise map and merging, and splitting whole rows cyclically into $W$ equal streams each take $O(V)$ steps on a fixed number of tapes.",
 r"volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
 page="stream-ops", frm=["fixed-tape-model","array-order","positional-number-representation-and-carries"])

controlled = infer(
 "S1.2",
 r"Updating a target field $y\mapsto y+a\pmod{q^b}$ by an offset computed from earlier control fields, or multiplying it by a fixed rational unit, costs $O(V)$ because the update is a cyclic shift of blocks that can be done by one split and merge.",
 r"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
 page="controlled-shifts", frm=["stream-ops","array-order","modular-arithmetic"])

widen = show(
 "S1.4",
 r"An interchange of two chunks of $u$ bits with arbitrary prefix, gap and suffix reduces to power-width calls with a row field whose length is divisible by $W^k$.",
 r"Take a few high digits of the two chunks as a row field, pad the rows to a multiple of $W^k$, interchange the remaining digits by power-width calls on pieces whose widths are the base-$m$ digits of the remaining width, and undo the high-digit moves.",
 ("explicit", "A general array has no row field of its own, but a few of its own high digits can serve as rows and moving them costs less than the final bound.", r"Rows for a general array can be supplied by a few of its own high digits."),
 [
  infer("S1.4.1", r"For all large $e$ put $k=\lceil\log_me\rceil$ and $\rho=\lceil k\log W/(2\log q)\rceil$ so that $\rho=O(\log 2e)$; the bounded set of small widths is handled by $e$ single-digit interchanges, absorbed in the constant.",
        r"Write each chunk as its top $\rho$ digits followed by its remaining"),
  infer("S1.4.2", r"Exchanging and joining the $\rho$ high digits gives a row field of range $R=q^{2\rho}\ge W^k$ before both remaining chunks, at cost $O(V\rho)$; zero rows are appended to reach $R'=W^k\lceil R/W^k\rceil<2R$, so the padded volume is less than $2V$.",
        r"Append zero rows, separately within"),
  infer("S1.4.3", r"Write the remaining width as $e-\rho=\sum_{j=0}^ka_jm^j$ with $0\le a_j<m$ and apply the power-width interchange to $a_j$ corresponding pieces of width $m^j$, all sharing the same row field.",
        r"Write the remaining width in base $m$:"),
  infer("S1.4.4", r"The total cost is $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$ because $a_j<m$ and $m^k<me$ make the sum geometric; the leftover movement $O(V\log 2e)$ is within the bound.",
        r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)."),
  infer("S1.4.5", r"For binary chunks pad each coordinate range from $[2^u]$ up to $[q^e]$ with zero entries, where $q^e\ge2^u$ is least; the volume grows by less than a fixed factor $q^2$, and since $e=O(u)$ the bound is $O(Vu^\tau)$.",
        r"Finally, for binary chunks let $e$ be the least integer with"),
  infer("S1.4.6", r"For chunks whose widths differ by one bit, peel the leading bit of the longer chunk, interchange the equal-width parts, and move that bit back, which adds only a single-bit move of cost $O(V)$.",
        r"For widths differing by one bit, choose the leading bit of the longer"),
 ])

chunk_interchange = show(
 "S1",
 r"Two disjoint address chunks of $u$ bits each, with arbitrary prefix, gap and suffix fields, in an array of volume $V$ can be interchanged in $O(Vu^\tau)$ tape steps for a fixed $\tau<1$.",
 r"Interchange the chunks by the three shears $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$, running the middle shear through a fixed restoring linear exchange network whose edge changes are smaller interchanges of the same kind, so that a recurrence gives a power saving; then remove the power-width and row restrictions by padding rows and splitting the width in base $m$.",
 ("explicit", "The method gives a saving because the number of smaller calls satisfies $s<Wm$, so each level of the recursion costs strictly less than a factor $m$ more per unit volume.", r"number $s$ of smaller calls satisfies $s<Wm$."),
 [stream_ops, controlled, power_interchange, widen],
 page="chunk-interchange",
 frm=["fixed-tape-model","array-order"],
 adds=[add("u","chunk width","the number of bits in each of the two interchanged address chunks","count"),
       add("V","volume","the number of stored data bits in the array being rearranged","count")],
 salient=r"The saving is a power $u^\tau$ with $\tau=1-2^{-50}$ extremely close to one, and the interchange is an exact permutation even though it passes through XOR combinations of the data.")

# ---------------------------------------------------------------- S2: simultaneous layer
phase_network = show(
 "P0",
 r"In the complex network with binary labels, each edge's phase-frame change $\mathcal C_V\mathcal C_U^{-1}$ is a product of one kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal basis of the edge residual, the endpoint operator is $C^{\otimes m}$ on every role, and the number of kernels is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$.",
 r"Use the phase function $q_U(x)=\operatorname{wt}(P_Ux)\bmod4$, whose change across an orthogonal sum is a sum of odd weights $\operatorname{wt}(v)[v\cdot x]$ over an orthonormal basis, and turn each term into a two-point translation kernel by Hadamard conjugation.",
 ("recoverable", "Weight is additive modulo four on orthogonal vectors and every basis vector has odd weight, so each basis vector contributes exactly one kernel and the number of kernels equals the dimension change.", None),
 [
  infer("P0.1", r"For orthogonal binary vectors $z,w$ the intersection of supports is even, so $\operatorname{wt}(z+w)=\operatorname{wt}(z)+\operatorname{wt}(w)-2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|$ is additive modulo four.",
        r"If $z\cdot w=0$, the intersection cardinality is even, so weight is", deferred=True),
  infer("P0.2", r"For $V=U\perp E$ with orthonormal basis $\mathcal B$ of $E$, $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\operatorname{wt}(v)[v\cdot x]\pmod4$, negated on a decreasing edge.",
        r"q_V(x)-q_U(x)=\sum_{v\in\mathcal B}", deferred=True),
  infer("P0.3", r"Each basis vector has norm one so its weight is odd; the phase factor $i^{\varepsilon[v\cdot x]}$ with $\varepsilon=\pm1$ equals $\frac{1+i^\varepsilon}2+\frac{1-i^\varepsilon}2(-1)^{v\cdot x}$, and $H\operatorname{diag}(1,-1)H=X$ turns the character into a translation, giving the kernel $aI+bX_v$ or its inverse.",
        r"The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the", deferred=True),
  infer("P0.4", r"The nonzero residuals have orthonormal bases by the residual lemma, so the kernels are counted by dimension changes and total $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$; unlike the bit network no extra source ranks occur.",
        r"The same lemma gives the count $s_{\rm c}$.", deferred=True),
  infer("P0.5", r"The deficit of the kernel count from $W_{\rm c}m$ is $2N-2L_{\rm c}>0$.",
        r"The deficit is $2N-2L_{\rm c}>0$.", deferred=True),
  infer("P0.6", r"For the pair $X_a\to Y_a$ the binary norm of $u_a$ is one and its weight is $27$, so $q_{U_a^\perp}-q_{U_a}=\operatorname{wt}(x)+2[u_a\cdot x]$ and the operator is $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u_a)$ and $C$ elsewhere; every other pair has zero and full labels with frames $I$ and $C^{\otimes m}$.",
        r"For the remaining pair, write $u=u_a$.  Its binary norm is one and", deferred=True),
  infer("P0.7", r"With $Z=\operatorname{diag}(1,-1)$ one has $C=iZC^{-1}Z$, so applying $Z_{a,k}$ before the network at $X_a$ and $i^{27k}Z_{a,k}$ after it at $Y_a$ turns each of the $27k$ inverse factors into $C$.",
        r"identity $C=iZC^{-1}Z$ turns each of them into $C$.", deferred=True),
  infer("P0.8", r"Negating the physical $X$ outputs and sending output role $\rho(w)$ back to $w$ leaves $C^{\otimes mk}$ on every role, scratch roles included.",
        r"Only the physical $X$ outputs still carry the minus sign of the", deferred=True),
 ],
 page="phase-network",
 frm=["butterfly-fft","network","frames","subset-labels","rank-saving","binary-field-f2-and-xor","complex-numbers"],
 adds=[add("s_{\\rm c}","complex rank sum","the number of two-point kernels, summed over all edges of the complex network","count"),
       add("W_{\\rm c}","complex wire count","the number of wires of the complex network","count"),
       add("L_{\\rm c}","complex loss","the total dimension lost on decreasing edges in the complex network","count")],
 salient=r"Every kernel is a two-point butterfly-type factor because each orthonormal basis vector has odd weight, and the one pair that is not already forward (27 inverse factors) is repaired by the single identity $C=iZC^{-1}Z$.")

edge_to_children = show(
 "Y0",
 r"A $C^{\otimes e}$ layer on $e=mf$ selected axes reduces to exactly $s_{\rm c}$ child layers on the $f=e/m$ axes of one slot each, plus a fixed number of binary row additions between slots and coefficientwise scalar operations.",
 r"Conjugate each edge's kernel product by a binary change of basis $\mathcal P_M$ that moves its residual basis into the first coordinate slots, do each kernel as one child layer on the $f$ axes of its slot, and write $M$ as a product of elementary row additions.",
 ("recoverable", "A kernel $C_{e_j}$ acts on one coordinate slot, so after conjugation by an invertible change of basis each residual basis vector costs one layer on the $f$ axes of its slot.", None),
 [
  infer("Y0.1", r"Extending the residual basis $v_1,\ldots,v_{\rho_{\rm edge}}$ to a basis of $\mathbb F_2^m$ as the first columns of $M$ gives $\mathcal C_{U_+}\mathcal C_{U_-}^{-1}=\mathcal P_M\bigl(\prod_jC_{e_j}^{\epsilon_j}\bigr)\mathcal P_M^{-1}$; only invertibility of $M$ is used.",
        r"Extend $v_1,\ldots,v_{\rho_{\rm edge}}$ to a basis of $\mathbb F_2^m$ and take these vectors as"),
  infer("Y0.2", r"A negative directional kernel needs only one forward child, because $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$ and the wrappers are address signs and fourth-root phases.",
        r"A negative directional kernel still requires only one"),
  infer("Y0.3", r"Gaussian elimination writes any $M\in\operatorname{GL}(m,\mathbb F_2)$ as a product of at most $m(m-1)+3m$ elementary row additions (a row swap being three additions), a constant because $m$ is fixed.",
        r"Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$"),
  infer("Y0.4", r"Summing the residual dimensions gives exactly $s_{\rm c}$ child calls in one invocation of the network, each on the $f=e/m$ axes of one slot.",
        r"$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
  infer("Y0.5", r"The normalized butterfly layer is recovered from the $C$ layer by diagonal phases: $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$, all exact Gaussian dyadic operations.",
        r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D."),
 ])

packed = show(
 "A0",
 r"On a rectangle of records with three chunks $x,y,z$ of $L=fK$ bits, the update $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ at the $f$ selected positions $j_i=\rho+iK$ can be performed together, restoring $z$ for every initial value, in time $O(V(L^\tau+1))$ in the regime $A_{\rm rect}=O(p)$, $R$ super-polynomial in $p$ and $K/\log p\to\infty$.",
 r"Use eight cyclic shifts of whole chunk ranges, a three-chunk rotation trick that restores the scratch chunk, which realize all the XORs whenever no $K$-bit segment carries into its neighbor; then repair exactly the small explicitly identified set of addresses where a guard value fails, by extraction, stable radix sorting and reinsertion.",
 ("explicit", "Because the correction depends only on addresses, the time bound holds in the worst case over all payloads.", r"The correction depends only on addresses, so the time bound is"),
 [
  infer("A0.1", r"Eight conditional unit additions to two integers $u,w$ compose to $(u,w)\mapsto(u+c(1-2(u\bmod2)),w)$: the parity of $u$ flips exactly when $c=1$, both quotients by two are preserved, and the auxiliary integer $w$ is restored.",
        r"If $c=0$, these operations do nothing. If $c=1$, the first four operations"),
  infer("A0.2", r"Each line applied simultaneously to all segment pairs is a single cyclic shift of a whole chunk by an offset depending only on the other chunks, so each costs $O(V)$ by controlled shifts after at most two chunk swaps; the composition $S_0$ has eight shifts and at most sixteen swaps.",
        r"Apply each line of \eqref{eq:eight-packed-additions} simultaneously to all"),
  infer("A0.3", r"At an address whose guard values all lie in $10\le g\le2^{K-1}-11$, no segment carries into or borrows from the next, so $S_0$ agrees with the ideal map $T_0$ performing the required XORs.",
        r"At an address outside $\mathcal B$, each segment initially lies in"),
  infer("A0.4", r"Exactly twenty values are excluded for each of the $2(f-1)$ guards, so by the union bound the bad set satisfies $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, independently of the record payloads.",
        r"There are exactly twenty excluded values for each guard in"),
  infer("A0.5", r"Both $S_0$ and $T_0$ are bijections that agree off $\mathcal B$ and preserve $\mathcal B$, so $T_0S_0^{-1}$ fixes the complement and permutes $\mathcal B$.",
        r"Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$."),
  infer("A0.6", r"Extract the exceptional records with destination ranks as keys, sort them by stable binary radix sort (the keys are distinct and equal the ranks of the marked holes), and reinsert them in one forward scan.",
        r"while stable binary radix sorting scans only the extracted records and"),
  infer("A0.7", r"The total time is $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$; after division by $V=MR$ the extra terms are bounded by $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$, both $o(1)$ in the stated family.",
        r"$80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. Under the stated family bounds"),
  infer("A0.8", r"Adding row $h'$ to row $h$ in all columns is one application with slot $h'$ as $x$, slot $h$ as $y$ and a third slot as $z$, so a complete change of basis and its inverse cost $O(V((eK)^\tau+1))$.",
        r"Under the asymptotic hypotheses in the final assertion of that lemma,"),
 ],
 page="packed-bit-addition",
 frm=["chunk-interchange","controlled-shifts","stream-ops","binary-field-f2-and-xor","modular-arithmetic"],
 salient=r"A fixed small fraction $80(f-1)2^{-K}$ of addresses is the only place the cheap shifts fail, and repairing them by sorting costs less than the main term.")

batching = show(
 "Z0",
 r"Let $F(e)$ be the time divided by the current logical volume for a layer on $e$ axes; then $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ with $F(e)=O(e)$ below $d^\beta$, which solves to a cost $O(Vd^{\lambda'})$ for a layer on $D\le d$ chunks.",
 r"Take the first $q_0$ chunks by individual kernels and use their bits as a row index, zero-padded to a multiple of $W^{k_0}$; recurse with each child on volume $V/W$; stop at $e<d^\beta$ and apply the kernels individually; sum the internal and leaf contributions and split $D-q_0$ in base $m$.",
 ("recoverable", "The role split needs many rows, which the first few chunks supply, and the child volume $V/W$ is what lets the recurrence carry the factor $s/W<m$.", None),
 [
  infer("Z0.1", r"Applying $e$ separate kernels costs $O(Ve)$ on any stream with complete ranges and common record format, which is the leaf cost.",
        r"scan also costs \(O(V)\).  Thus \(e\) individual kernels cost"),
  infer("Z0.2", r"At an internal node with $e=m^k$ chunks, the binary changes of basis, inverses, scalar gates, endpoint corrections and reassembly cost $O(V((eK)^\tau+1))$.",
        r"O\bigl(V((eK)^\tau+1)\bigr)"),
  infer("Z0.3", r"Apply $C$ individually to the first $q_0=\lceil\log_2W\rceil\lceil\log_m(2d)\rceil$ chunks at cost $O(V\log d)$ and use their bits as a row index of range at least $W^{k_0}$; if $D\le q_0$ use individual kernels throughout.",
        r"If \(D\le q_0\), use individual \(C\) kernels, at cost \(O(V\log d)\)."),
  infer("Z0.4", r"Each recursive edge call acts on one role stream with volume exactly $1/W$ of its parent's, and every row keeps its complete suffix, so the packed lemma applies to each child.",
        r"Each recursive edge call acts on"),
  infer("Z0.5", r"The $s$ child calls on streams of volume $V/W$ give, after division by $V$, the recurrence $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$.",
        r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
  infer("Z0.6", r"At an internal node $e\ge d^\beta$, so $K\le d^c\le e^{c/\beta}$ and the overhead is $O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)$ using $\tau(1+c/\beta)<\lambda$.",
        r"At an internal node \(e\ge d^\beta\), hence"),
  infer("Z0.7", r"With $a=s/W\le m^\sigma<m^\lambda$ the internal costs sum to at most $Ce^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)$.",
        r"Put \(a=s/W\).  Since \(a\le m^\sigma<m^\lambda\), the internal"),
  infer("Z0.8", r"The leaves, with $u=e/m^j<d^\beta$ chunks each, contribute at most $O(a^ju)\le O(e^\sigma u^{1-\sigma})\le O(e^\sigma d^{\beta(1-\sigma)})$, using $a^j\le m^{j\sigma}=(e/u)^\sigma$ (which also covers $a<1$).",
        r"O(a^ju)\le O(e^\sigma u^{1-\sigma})"),
  infer("Z0.9", r"Write $D-q_0=\sum_ja_jm^j$ in base $m$ with $0\le a_j<m$, giving at most $(m-1)(1+\lfloor\log_md\rfloor)$ pieces, one call per piece.",
        r"Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\)."),
  infer("Z0.10", r"Adding the pieces and the row preprocessing gives $O(\log(2d)[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1])=O(d^{\lambda'})$ for any fixed $\lambda'$ with $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$, the strict inequality absorbing the logarithmic number of groups.",
        r"=O(d^{\lambda'})"),
 ],
 frm=["power-saving-recurrence","chunk-interchange","packed-bit-addition"],
 adds=[add("\\beta","stopping exponent","the exponent $1/2$ such that recursion stops once fewer than $d^\\beta$ chunks remain","direct"),
       add("F(e)","normalized layer cost","the time of a layer on $e$ axes divided by the current logical stream volume")])

guard = show(
 "G0",
 r"Every intermediate coefficient of the layer is represented exactly with $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits per real component, where $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$, so coefficient width stays $O(p)$.",
 r"Bound the arithmetic dependency depth $A(e)$ of the recursion by a recurrence, then use that each elementary operation at most doubles the modulus and adds at most one denominator bit.",
 ("recoverable", "Intermediate values are not contractions, so exactness requires reserving enough bits for the worst growth along a chain of operations, and the chain length is the recursion's depth.", None),
 [
  infer("G0.1", r"Concatenating all scalar gates and edge calls of one invocation, the depth satisfies $A(e)\le sA(e/m)+E$ at an internal node and $A(e)\le8e$ at a leaf, with $E=64(W+m+1)^3$; here $s$, not $s/W$, appears because depth is concatenated, not volume.",
        r"A(e)\le sA(e/m)+E"),
  infer("G0.2", r"Since $sx+E\le(s+E)x=Bx$ for $x\ge1$, and $B^{k+1}\le B^{\log_md+2}=B^2d^{\log_mB}\le B^2d^\nu$, one gets $A(e)\le8dB^{k+1}\le8B^2d^{\nu+1}$.",
        r"B^{k+1}\le B^{\log_m d+2}"),
  infer("G0.3", r"Concatenating the at most $md$ pieces and adding the outer diagonals and the scalar $b^D$ gives total depth at most $128mB^2d^{\nu+3}\le C_0d^{C_1}$ with $C_0=128mB^2$ and $C_1\ge\nu+3$.",
        r"<128mB^2d^{\nu+3}\le C_0d^{C_1}."),
  infer("G0.4", r"A value at dependency depth $j$ lies in $2^{-(p+j)}\mathbb Z[i]$ and has modulus at most $2^j$, because addition at most doubles the modulus and halving adds one denominator bit.",
        r"lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most"),
  infer("G0.5", r"Choosing $\epsilon C_1<1$ with $d=\Theta(p^\epsilon)$ makes $\Delta=o(p)$ and the full coefficient width $O(p)$, so addition, shifts, copying and phase changes cost $O(p)$ bit operations per coefficient.",
        r"Choose \(\epsilon C_1<1\).  Since \(d=\Theta(p^\epsilon)\),"),
 ],
 frm=["fixed-point-disk-grid","dyadic-rationals-and-binary-fractions"])

simult = show(
 "B0x",
 r"Given $D\le d$ equal-width chunks, the tensor product of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on one common bit position of each chunk, applied coefficientwise to polynomial records of complex fixed-point coefficients, can be computed with a single final truncation in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$.",
 r"Compute the unnormalized layer $C^{\otimes D}$ exactly with the complex phase network, whose edge frames are products of two-point kernels on groups of $f=e/m$ axes so that each edge costs one smaller layer; do its binary basis changes by packed whole-chunk operations with deterministic repair; unroll the recurrence; bound the guard widths; convert $C^{\otimes D}$ to $H_0^{\otimes D}$ by phases and truncate once.",
 ("explicit", "Separate butterfly factors would need $D$ whole-array passes, so the layer must be done at once with a cost per volume below $d$.", r"factors would require $D$ whole-array passes."),
 [
  phase_network, edge_to_children, packed, batching, guard,
  infer("B0x.1", r"Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays; truncating each real and imaginary part toward zero keeps the disk and changes each coefficient by less than $\sqrt2\,2^{-p}$, and the truncated numerators have magnitude at most $2^p$.",
        r"Finally, every row of $\mathcal H$ has"),
 ],
 page="simultaneous-layer",
 frm=["butterfly-fft","fixed-point-disk-grid","chunk-interchange","dyadic-rationals-and-binary-fractions","complex-numbers"],
 adds=[add("D","chunk count","the number of address chunks in which the same bit position is butterflied at once, at most $d$","count"),
       add("d","axis bound","the maximum number of axes, a small power $p^\\epsilon$ of the precision","count"),
       add("K","chunk width","the number of bits in each address chunk, $\\lfloor d^c\\rfloor$","count"),
       add("\\lambda'","layer exponent","the fixed exponent below one in the layer cost $O(Vd^{\\lambda'})$")],
 salient=r"The cost per unit volume is $d^{\lambda'}$ with $\lambda'<1$, strictly below the $D\le d$ whole-array passes that separate butterflies would need.")
