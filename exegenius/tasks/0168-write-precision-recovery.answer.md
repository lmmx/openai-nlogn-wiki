Error tracking and exact recovery shows that the computed convolution coefficients lie within $1/2$ of the true integers, so rounding returns them exactly and carry propagation gives the binary product.

The computation runs on [Fixed-point Gaussian dyadic records](fixed-point.md) with $p=6b$ fractional bits, where $b=\lceil\log_2n\rceil$ is the digit width. Write $h_p=2^{-p}$ for the grid spacing and $L=\log_2T$. Norms are sup norms, an error of $a$ means error below $ah_p$, and every array stays in the unit disk (norm $\le1$). For large $n$, $T<8n/b$ gives $S\le T<2^b$ and $L<b$. Each [synthetic transform](synthetic-transform.md) has error below $L$ <cite data-source="paper">$\sqrt2\ell\,2^{-p}<L2^{-p}$</cite>.

## Adding errors

Errors add through the [Contractions and bilinear contractions](contraction-maps.md) that make up each transform and product. A linear contraction passes an input error on without increasing it. For a bilinear contraction $\mathcal M$ with $\|\mathcal M(f,g)\|\le\|f\|\|g\|$, replacing operands $f,g$ by $f',g'$ gives
$$\|\mathcal M(f',g')-\mathcal M(f,g)\|=\|\mathcal M(f'-f,g')+\mathcal M(f,g'-g)\|\le\|f'-f\|\|g'\|+\|f\|\|g'-g\|,$$
so for disk operands the two input errors add, not multiply.

Take a unit phase $e$, a grid approximation $\widetilde e$ with $|\widetilde e-e|<2h_p$, and a disk operand $x$. Then $\widetilde ex$ differs from $ex$ by under $2\|x\|h_p$, and truncation $Q_p$ moves each of the real and imaginary parts by under $h_p$, so $\|Q_p(\widetilde ex)-ex\|<(2\|x\|+\sqrt2)h_p<4h_p$. Since $|\widetilde e|\le1$ and $Q_p$ does not increase the norm, $\|Q_p(\widetilde ex)\|\le\|x\|$.

## The convolution and chirp transform

The ring convolution $\mathcal M_r$ of [Phase twist](phase-twist.md) applies two forward synthetic transforms, a pointwise polynomial product divided by $r$ (truncation error under $2$) and one opposite transform, which gives $(f*g)/(rM^2)$. Here $M=T/r$ is the number of records of $r$ coefficients. These steps err by under $3L+2$; the exact multiplication by $M$ then gives $(f*g)/T$ and error
$$E_{\rm ring}:=M(3L+2)<5TL$$
<cite data-source="paper">E_{\rm ring}:=M(3L+2)<5TL.</cite> A cutoff such as $b\ge2^{24}$ makes $8TLh_p$ and the similar margins below $10^{-3}$ <cite data-source="paper">$b\ge2^{24}$, together with the other eventual construction conditions,</cite>. So if one operand has norm at most $.7$, the exact output has norm at most $.7$ by contraction, and the computed one is below $.701$.

The complex convolution inserts a twist on each input and an untwist on the output, each adding under $4$. Hence its error is under
$$(E_{\rm ring}+4+4+4)h_p<6TLh_p.$$

The computed chirp transform $\widetilde{\mathscr C}$ is built from the [Bluestein chirp identity](chirp.md): a phase product, a complex convolution with the chirp kernel, and a last phase product. With $\boldsymbol t$ the axis lengths, $F_{\boldsymbol t}$ the exact transform and $Q$ the target permutation, the errors are $2$ (kernel approximation), $4$, $6TL$ and $4$, so
$$\|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\|<(6TL+2+4+4)h_p<8TLh_p.$$

## Source transforms

The computed source transform $\widetilde{\mathscr F}$ applies the expansion map $\mathcal A$ of [Gaussian resampling](gaussian-resampling.md), then $\widetilde{\mathscr C}$, then the compression map $\mathcal B_0$, then an exact scaling by $2^\gamma$. Each of $\mathcal A,\mathcal B_0$ is a contraction whose axis-by-axis implementation errs by under $dp^2$ ($d$ axes, each line under $p^2$). The error before scaling is therefore under $2dp^2+8TL$. As $2dp^2<TL$ eventually, scaling gives error under $E_sh_p$ with
$$E_s=9\cdot2^\gamma TL$$
<cite data-source="paper">E_s=9\,2^\gamma TL,</cite> and $b\ge2^{24}$ gives $\gamma\le b/4$ <cite data-source="paper">$b\ge2^{24}$ implies $\gamma\le b/4$</cite>. The same cutoff keeps $E_sh_p<10^{-3}$.

Here $u,v$ are the scaled digit arrays, not integers: each radix digit is stored as its value times $2^{-b-2}$, so norm is below $1/4$. Let $U=RF_{\boldsymbol s}u$ and $V_1=RF_{\boldsymbol s}v$ be the exact source transforms, and $\widetilde U,\widetilde V_1$ the computed ones, of norm under $1/4+E_sh_p<.26$. Then $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has norm under $.26^2<.5$, and
$$\widetilde U\cdot\widetilde V_1-U\cdot V_1=(\widetilde U-U)\cdot\widetilde V_1+U\cdot(\widetilde V_1-V_1)$$
has two terms under $E_sh_p$; truncation adds under $2h_p$. So $\|z-U\cdot V_1\|<(2E_s+2)h_p$.

With $F_{\boldsymbol s}$ the normalized transform (factor $1/S$) and $F_{\boldsymbol s}^+$ its opposite-sign version, the retained permutation cancels ([Retained permutation cancellation](retained-permutations.md)): the exact opposite transform $G=RF_{\boldsymbol s}^+$ satisfies $G(U\cdot V_1)=(u*v)/S^2$ <cite data-source="paper">=\frac{u*v}{S^2}.</cite> The computed opposite transform is within $E_sh_p$ of $Gz$, and $G$ is a contraction, so
$$\|\widetilde{\mathscr F}^{+}(z)-G(U\cdot V_1)\|\le\|\widetilde{\mathscr F}^{+}(z)-Gz\|+\|G(z-U\cdot V_1)\|<(3E_s+2)h_p.$$
Multiplying exactly by $S$, $\widetilde w$ approximates $w=(u*v)/S$ with error under $E_wh_p$, where
$$E_w:=S(3E_s+2)<28\cdot2^\gamma T^2L,$$
because $2S<2^\gamma T^2L$. Each coefficient of $w$ averages $S$ products of norm below $1/16$, so $\widetilde w$ stays in the disk.

## Rounding

The integer coefficients are $2^{2b+4}Sw$: $2^{2b+4}$ undoes the two digit scales and $S$ undoes the remaining $1/S$. Both multiplications are exact, but they scale the error. With $h_p=2^{-6b}$, $S\le T<2^b$ and $L<b$, the absolute error is under
$$2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}<448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<\tfrac12$$
<cite data-source="paper">\le448b\,2^{-3b/4}<\frac12.</cite> The factors $2^{2b+4}ST^2<2^{5b+4}$ use up about $5b$ of the $6b$ fractional bits, and $\gamma\le b/4$ costs at most $b/4$ more. The true coefficients are integers and the computed value is strictly within $1/2$ of one, so its nearest integer is the unique correct coefficient.

## Carries

Carry propagation rebuilds the binary product from the coefficients $c_j$ of the [Multiplication as radix-digit convolution](radix-digit-reduction.md), where $c_j\le q(2^b-1)^2$ and $q=\lceil n/b\rceil\le2^b$. Put $Q_0=2^b$ and $k_0=0$. Here $j$ is a coefficient index, $k_j$ the carry into position $j$, and $d_j$ the $j$-th output digit (not a packed block):
$$d_j=(c_j+k_j)\bmod Q_0,\qquad k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor.$$
Then $0\le k_j\le q(Q_0-1)<Q_0^2$. This holds at $j=0$; if it holds at $j$, then $c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1)$, so $k_{j+1}\le q(Q_0-1)$. Since $c_j+k_j=d_j+Q_0k_{j+1}$, adding $c_jQ_0^j$ to the invariant
$$\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$$
gives it at $j+1$, and it holds at $j=0$. The full product is $\sum_hc_hQ_0^h$, and its unprocessed terms are multiples of $Q_0^j$, so the first $j$ radix digits are $d_0,\dots,d_{j-1}$. The product is below $2^{2n}$, so all bits above position $2n-1$ are zero and exactly $2n$ bits are output.
