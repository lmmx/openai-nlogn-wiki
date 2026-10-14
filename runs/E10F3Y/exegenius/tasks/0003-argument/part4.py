from lib import *

# ---------------------------------------------------------------- R2.1 synthetic transform
r21 = show(
    "S2.1",
    r"Over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ with $\omega_t=y^{2r/t}$ the transforms $F_t^\mp$ are contractions with $F_t^+F_t^-=t^{-1}I$, and $F_t^-$ is computed by a decimation-in-frequency recursion in which every twiddle multiplication is a signed shift of the coefficient list, so only butterflies cost arithmetic.",
    r"Mimic the radix-two FFT with the root of unity $\omega_t=y^{2r/t}$: prove character cancellation $\sum_k\omega_t^{jk}=t$ or $0$ directly (the ring has zero divisors), then split $F_t^-$ into the butterfly $H_0$, a twiddle $\omega_t^{-k}$ on the odd half, and two transforms of length $t/2$.",
    mot("The ring has zero divisors, so character cancellation must be verified directly instead of dividing by $\\omega_t^j-1$.", "explicit",
        r"The ring has zero divisors, so we verify character cancellation"),
    [
        infer("S2.1a",
              r"Every power of $\omega_t$ is an isometry for the coefficient norm and each transform entry averages $t$ such images, so both $F_t^-$ and $F_t^+$ are contractions.",
              r"Every power of $\omega_t$ is an isometry, and each transform entry is"),
        infer("S2.1b",
              r"$\sum_{k=0}^{t-1}\omega_t^{jk}$ equals $t$ if $t\mid j$ and $0$ otherwise: for $j=2^vj_0$ with $j_0$ odd, replacing $k$ by $k+t/2^{v+1}$ permutes the summands and multiplies the sum by $y^{rj_0}=-1$, so the sum vanishes since $\mathcal R_r$ has no additive two-torsion; expanding gives $F_t^+F_t^-=t^{-1}I$.",
              r"Write $j=2^v j_0$ with $j_0$ odd"),
        infer("S2.1c",
              r"For $t\ge2$ pair $z_k$ with $z_{k+t/2}$, apply $H_0$ in place, multiply the $b=1$ output by $\omega_t^{-k}$ and recurse on both branches; this computes $F_t^-$ since $(F_t^-z)_{2h+b}=\frac1{t/2}\sum_k(\omega_t^2)^{-hk}\omega_t^{-bk}\frac{z_k+(-1)^bz_{k+t/2}}2$.",
              r"decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for"),
    ],
    page="synthetic-transform",
    frm=["negacyclic-ring", "dft", "fft-butterfly", "roots-of-unity", "contraction-error", "polynomials", "complex-numbers"],
    adds=[
        add(r"\omega_t", "synthetic root", "The ring element $y^{2r/t}$ serving as a root of unity of order $t$ (for $t$ a power of two dividing $2r$).", "direct"),
        add(r"F_t^-", "normalized transform", "The map $(F_t^-z)_j=\\frac1t\\sum_k\\omega_t^{-jk}z_k$ on $t$ ring entries; $F_t^+$ is the opposite-sign version.", "direct"),
    ])

# ---------------------------------------------------------------- R2.2 bit-reversed order
r22 = show(
    "S2.2",
    r"The recursion writes its outputs in bit-reversed order, $B_tF_t^-$, and the opposite procedure consumes that same order, implementing $F_t^+B_t^{-1}$, so no reordering is executed between the forward transforms and the inverse; for $D$ axes a round groups into a parallel butterfly $\mathcal H$ followed by one monomial $J_E$.",
    r"Track the address bits through the recursion to see that frequency bit $j$ lands in slot $\mathrm{rev}_a(j)$, run the recursion backwards for the opposite transform (each level is half the inverse of the forward level since $H_0^2=I/2$), and group the per-axis twiddles into one combined exponent.",
    mot("The recursion writes its outputs directly in bit-reversed order and does not move whole frequency indices, so the opposite transform can simply consume that order.", "explicit",
        r"directly in this order; it does not move whole frequency indices."),
    [
        infer("S2.2a",
              r"After all $a=\log_2t$ rounds the named slots from high to low contain the frequency bits from low to high, so $(F_t^-z)_j$ occupies slot $\mathrm{rev}_a(j)$; $B_t$, the record permutation $j\mapsto\mathrm{rev}_a(j)$, is therefore produced for free.",
              r"After all $a$ rounds, the named slots from high to low therefore"),
        infer("S2.2b",
              r"The consuming procedure traverses the recursion in reverse (smaller branches, then the inverse monomial, then $H_0$); as $H_0^2=I/2$ each reversed level is half the inverse of the forward level, so after $a=\log_2t$ levels the composite with $B_tF_t^-$ is $2^{-a}I=I/t$, and by character cancellation it coincides with $F_t^+B_t^{-1}$.",
              r"of the corresponding forward level.  There are $a=\log_2t$ levels,"),
        infer("S2.2c",
              r"For $D$ axes of lengths $t_1,\ldots,t_D$ with $M=\prod t_i$, $F_{\boldsymbol t}^\pm=\bigotimes F_{t_i}^\pm$ and $B=\bigotimes B_{t_i}$; since the twiddle of axis $i$ depends only on that axis's address bits and commutes with the other axes' butterflies, a round is a parallel butterfly $\mathcal H$ followed by $J_E$, multiplication by $y^E$ with $E=-\sum_i\frac{2r}{u_i}b_ik_i\pmod{2r}$, and every completed round is a contraction.",
              r"Consequently the individual axis steps may be grouped as a parallel"),
    ],
    page="bit-reversed-order",
    frm=["synthetic-transform", "fft-butterfly", "multidimensional-transform", "dft", "contraction-error"],
    adds=[
        add(r"B_t", "bit-reversal permutation", "The record permutation moving the entry at $j$ to position $\\mathrm{rev}_a(j)$, with $a=\\log_2t$.", "direct"),
        add(r"M", "cyclic address count", "The product $\\prod_it_i$ of the axis lengths, the number of ring records in an array.", "count"),
    ])

# ---------------------------------------------------------------- R2.3 transform layout
r23 = show(
    "S2.3",
    r"With $d-1$ axes of lengths $t_i\in\{2^{\ell-1},2^\ell\}$ and $T=rM$ entries of $p$-bit coefficients, a layout permutation $L$ puts the selected bits of all axes at a common offset in consecutive $K$-bit chunks, so that the forward procedure with exact counterpart $LBF_{\boldsymbol t}^-$ and its opposite $F_{\boldsymbol t}^+B^{-1}L^{-1}$ each have error below $\sqrt2\,\ell\,2^{-p}$ and cost $O\bigl(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}]\bigr)$.",
    r"Move the top bit slots of each axis (at most $D(b+1)$ of them) to a prefix, interchange $K$-bit chunks so that chunk $j$ of every axis is consecutive, then run the rounds: those on prefix slots individually, the remaining $\ell$ rounds by the simultaneous butterfly layer; each round truncates once and is a contraction.",
    mot("To apply the simultaneous layer in a transform round the selected bits of the participating axes must sit at a common offset in consecutive $K$-bit chunks.", "explicit",
        r"we must place the selected bits of the participating axes at a common"),
    [
        infer("S2.3a",
              r"Put $b=(\ell-1)\bmod K$ and $q=\lfloor(\ell-1)/K\rfloor$; list the top slots $(i,\ell-1)$ of the long axes and then $(i,h)$ for $h=b-1,\ldots,0$ and move them to a prefix. There are at most $D(b+1)=O(dK)$ listed slots, so the moves cost $O(TpdK)$, and what is left of each axis is $q$ consecutive $K$-bit chunks.",
              r"slots in their relative order.  There are at most $D(b+1)=O(dK)$"),
        infer("S2.3b",
              r"Reordering the chunks from axis-major $(1,1),\ldots,(D,q)$ to chunk-major $(1,1),(2,1),\ldots,(D,1),(1,2),\ldots,(D,q)$ uses at most $Dq-1$ exchanges of width-$K$ chunks, each $O(TpK^\tau)$, so in total $O(TpDqK^\tau)=O(Tp\,pK^{\tau-1})$ because $DqK\le d\ell=O(p)$; $L$ and $L^{-1}$ cost the same.",
              r"nonadjacent.  Each costs $O(TpK^\tau)$, so all these exchanges cost"),
        infer("S2.3c",
              r"Rounds run in the order $h=\ell-1$ (long axes only), $h=\ell-2,\ldots,b$ in the $qK$ rounds on the remaining chunks, and the bottom positions $h=b-1,\ldots,0$; in a round on a chunk offset the layer sees the complete address set $[P]\times[2^K]^D\times[S]$ and costs $O(Tpd^{\lambda'})$, so all $\ell$ rounds cost $O(Tp\ell d^{\lambda'})$.",
              r"$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total."),
        infer("S2.3d",
              r"There are at most $b+1\le K$ rounds on prefix slots; each halves a bit individually by buffering a pair of records, in $O(Tp)$ per round with exact dyadics on a grid of $p+D+O(1)=O(p)$ bits, so these rounds cost $O(TpdK)$ in total.",
              r"most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$."),
        infer("S2.3e",
              r"Because truncation toward zero is odd and the monomial $J_E$ is a signed coefficient permutation, $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$: each round is one exact contraction followed by a single truncation adding less than $\sqrt2\,2^{-p}$; a contraction does not increase the error already present, so starting from zero error at most $\ell$ rounds give error below $\sqrt2\,\ell\,2^{-p}$, and the layout permutations are isometries.",
              r"zero error, at most $\ell$ rounds therefore"),
        infer("S2.3f",
              r"Executing operations on named slots after $L$ conjugates them by $L$, so the forward procedure has exact operator $LBF_{\boldsymbol t}^-$ (frequency address $j$ stored at $L(Bj)$) and the opposite one has $F_{\boldsymbol t}^+B^{-1}L^{-1}$, its final charged move $L^{-1}$ restoring axis-major order.",
              r"In particular, the forward entry with frequency address $j$ is"),
    ],
    page="transform-layout",
    frm=["simultaneous-butterfly-layer", "chunk-interchange", "synthetic-transform", "bit-reversed-order", "multidimensional-transform", "contraction-error", "tape-stream-operations", "guard-bits"],
    adds=[
        add(r"T", "entry count", "The total number $rM$ of complex coefficients in the array, so the logical bit volume is $\\Theta(Tp)$.", "count"),
        add(r"\ell", "log record length", "The integer $\\log_2r$, so $r=2^\\ell$ and each axis length is $2^\\ell$ (long) or $2^{\\ell-1}$ (short).", "count"),
        add(r"L", "layout permutation", "The positional permutation of record addresses that places the selected bits of all axes at a common offset in consecutive $K$-bit chunks.", "direct"),
        add(r"b", "prefix offset", "The remainder $(\\ell-1)\\bmod K$ giving the number of bottom slots handled individually.", "count"),
        add(r"q", "chunk count", "The quotient $\\lfloor(\\ell-1)/K\\rfloor$ giving the number of $K$-bit chunks left on each axis.", "count"),
    ],
    salient=r"Three separate terms add up in the cost $dK+pK^{\tau-1}+\ell d^{\lambda'}$, one for each way an address bit is moved or combined: individual prefix rounds, chunk exchanges of width $K$, and simultaneous butterfly layers; the middle term has $\tau-1<0$ so it shrinks as $K$ grows while the first grows.")

# ---------------------------------------------------------------- R2.4 kronecker packing
r24 = show(
    "S2.4",
    r"For disk-grid polynomials $f,g\in\mathcal R_r$ with $r=2^\ell<2^p$ one can compute the exact Gaussian integer numerators of $fg$ and then $Q_p(fg/r)$, a disk-grid polynomial within $\sqrt2\,2^{-p}$ of $fg/r$, in $O(rp\log(rp))$ time on a fixed number of tapes.",
    r"Signed Kronecker substitution: evaluate the integer polynomials $a,b,c,e$ (real and imaginary numerators) at $B_0=2^{4p}$, multiply the four pairs of evaluation integers with the established multiplier, recover the product coefficients by centered residues with carries, combine and reduce modulo $y^r+1$, and truncate after division by $r2^{p}$.",
    mot("Every product coefficient is smaller than $B_0/2$ in absolute value, so after removing lower coefficients the centered residue modulo $B_0$ identifies the next one uniquely.", "explicit",
        r"this strict bound identifies the next coefficient by its centered"),
    [
        infer("S2.4a",
              r"Write $f=2^{-p}(a+ib)$, $g=2^{-p}(c+ie)$ with integer polynomials of degree below $r$ and coefficients at most $2^p$ in absolute value; the evaluation integers $A_u=u(B_0)$ satisfy $|A_u|\le2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2$ and so fit in $4pr$ bits.",
              r"shows that each magnitude fits in $4pr$ bits."),
        infer("S2.4b",
              r"Every coefficient of an ordinary product has $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, which is the separation condition making the packing injective.",
              r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
        infer("S2.4c",
              r"Forming $A_u$ from the signed coefficients uses digits $d_j\equiv u_j+\gamma_j\pmod{B_0}$ with carry $\gamma_{j+1}\in\{-1,0\}$ (since $-B_0<u_j+\gamma_j<B_0$), giving a two's-complement encoding of $A_u$ with $\gamma_r=-1$ exactly for negative values; a constant number of scans costs $O(rp)$.",
              r"Since $-B_0<u_j+\gamma_j<B_0$ whenever"),
        infer("S2.4d",
              r"To extract coefficients from a product integer $Z=h(B_0)$, take the centered residue $\widehat h_j\in[-B_0/2,B_0/2)$ of $q_j+\rho_j$ modulo $B_0$ with carry $\rho_{j+1}=(q_j+\rho_j-\widehat h_j)/B_0\in\{0,1\}$; the residual identity $\sum_{k\ge j}h_kB_0^{k-j}=\sum_{k\ge j}q_kB_0^{k-j}+\rho_j+\varepsilon B_0^{J-j}$ and the separation bound give $\widehat h_j=h_j$, and the final carry cancels the sign extension.",
              r"The carry belongs to $\{0,1\}$: if $\rho_j$ has this property, then"),
        infer("S2.4e",
              r"The real and imaginary numerator streams are $ac-be$ and $ae+bc$; subtracting the coefficient at $j+r$ from that at $j$ reduces modulo $y^r+1$, each result $H_j$ being a sum of exactly $r$ signed products so $|H_j|\le r2^{2p}$ and $\|fg/r\|_\infty\le\|f\|_\infty\|g\|_\infty$.",
              r"The real and imaginary numerator streams are respectively"),
        infer("S2.4f",
              r"The grid numerator of the normalized product is $\mathrm{trunc}_0(\Re H_j/2^{p+\ell})+i\,\mathrm{trunc}_0(\Im H_j/2^{p+\ell})$, i.e. $Q_p(2^{-2p}H_j/r)$, written as a $w$-bit word; four exact integer products of $4pr$ bits dominate the linear packing, extraction, combination and wrapping costs, giving $O(rp\log(rp))$.",
              r"Four exact integer products dominate the linear"),
    ],
    page="kronecker-packing",
    frm=["hh-multiplier", "negacyclic-ring", "positional-number-systems-and-carries", "fixed-point-numbers-dyadic-rationals-and-rounding", "tape-stream-operations", "polynomials", "schoolbook-and-karatsuba-multiplication"],
    adds=[
        add(r"B_0", "packing base", "The evaluation point $2^{4p}$ at which integer polynomials with coefficients of absolute value at most $2^p$ are evaluated.", "direct"),
    ])

# ---------------------------------------------------------------- R2.5 convolution proposition pieces
r25 = show(
    "S2.5",
    r"The normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays over $\mathcal R_r$ is approximated with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in $O\bigl(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)]\bigr)$ time, returned in the original order.",
    r"Compute the two forward synthetic transforms in the retained $LB$ order, multiply corresponding polynomial records, apply the opposite transform to that order, and scale exactly by $M$; use $F^-(f*g)=M(F^-f)(F^-g)$ and $F^+F^-=I/M$ for exactness and bilinear contraction bounds for the error.",
    mot("Pointwise multiplication commutes with applying the same record permutation $LB$ to both operands, so the product can be formed in the retained order and handed directly to the opposite procedure.", "explicit",
        r"Pointwise multiplication commutes with applying the same record"),
    [
        infer("S2.5a",
              r"Expansion of the finite sums gives $F_{\boldsymbol t}^-(f*g)=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)$, and since $F^+F^-=I/M$, $MF^+_{\boldsymbol t}\bigl(\frac{(F^-f)(F^-g)}r\bigr)=\frac{f*g}{rM}$; because $LB$ permutes records and leaves polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$ for the pointwise product $P(u,v)=uv/r$.",
              r"To check normalization, expansion of the finite sums gives"),
        infer("S2.5b",
              r"With $\delta=\sqrt2\,\ell\,2^{-p}$ and $\eta=\sqrt2\,2^{-p}$ the two forward errors are below $\delta$, the bilinear contraction $P$ gives $\|P(\widetilde u,\widetilde v)-P(u,v)\|<2\delta$, the product lemma adds truncation $\eta$, and the contractive opposite transform gives total error below $3\delta+\eta$; the exact scaling by $M$ yields error below $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$.",
              r"The final exact multiplication by $M$ therefore gives error less than"),
        infer("S2.5c",
              r"There are $M=T/r$ pointwise polynomial products costing $O(Tp\log(rp))$ in total, the three transforms cost as in the layout lemma, and the final exact scaling by $M=2^{m_M}$ (appending $m_M=\log_2M$ zero bits, output width $w_M=w+m_M$) is linear in $Tp$.",
              r"There are $M=T/r$ pointwise polynomial products.  Their total cost"),
    ])

r2 = show(
    "S2",
    r"Normalized convolution over the polynomial ring: for arrays on a product of cyclic axes with entries in $\mathcal R_r=\mathbb C[y]/(y^r+1)$, $\mathcal M_r(f,g)=(f*g)/T$ is approximated with error below $\sqrt2\,M(3\ell+1)2^{-p}$ and cost $O\bigl(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)]\bigr)$.",
    r"Compute synthetic Fourier transforms over $\mathcal R_r$, whose roots of unity are signed shifts, with the simultaneous butterfly layers and chunk interchanges of the key step, retain their common frequency order through the pointwise polynomial products (done by Kronecker packing and the established multiplier), and apply the opposite transform.",
    mot("The only arithmetic in a synthetic transform is the butterfly and the only multiplications are pointwise polynomial products, so the saving from the tape procedures applies to everything except those short products.", "recoverable"),
    [r21, r22, r23, r24, r25],
    page="ring-convolution",
    frm=["transform-layout", "kronecker-packing", "synthetic-transform", "bit-reversed-order", "contraction-error", "multidimensional-transform", "cyclic-convolution", "negacyclic-ring", "convolution-of-sequences"],
    adds=[
        add(r"\mathcal M_r", "normalized convolution", "The bilinear map $(f,g)\\mapsto(f*g)/T$ on arrays over $\\mathcal R_r$, a contraction in the sup norm.", "direct"),
        add(r"t_i", "axis length", "The length of the $i$th cyclic axis, a power of two equal to $r/2$ or $r$.", "count"),
        add(r"w", "component width", "The width in bits of the two's-complement word storing one real or imaginary component, with $p+2\\le w\\le C_wp$.", "count"),
    ])
