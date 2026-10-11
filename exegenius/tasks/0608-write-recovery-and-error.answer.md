Exact coefficient recovery is the error analysis showing that each convolution coefficient, computed through approximate transforms, lies strictly within $1/2$ of its true integer, so rounding returns that integer. It closes the argument for exact integer multiplication.

<cite data-source="paper">The true coefficients are real integers.</cite> Distinct integers differ by at least $1$. So if a computed value is within $1/2$ of an integer $m$, then $m$ is the unique nearest integer and rounding returns $m$.

## Units and error sources

The source sets $b=\lceil\log_2 n\rceil$ and <cite data-source="paper">p = 6b,</cite> and <cite data-source="paper">Take the power of two T in [4n/b, 8n/b)</cite>. The error analysis bounds the error over the $T$ entries of the [Padded transform box](padded-transform-box.md). Write $h_p=2^{-p}$ for the size of one unit in the last place: a value with $p$ fractional bits is a multiple of $h_p$, and an error of $a$ units is an absolute error below $a\,h_p$.

This analysis takes its guard widths from the [Guard-width bound](guard-width-bound.md), so every intermediate value is exact. Errors come only from transforms and from [truncation](truncation.md) $Q_p$, which moves a coefficient by less than $\sqrt2\,h_p<2h_p$. <cite data-source="paper">applies to every synthetic transform here, with error less than 2ℓ 2−p < L2−p , where L = log2 T</cite>, so each transform has error below $\log_2 T$ units.

<cite data-source="paper">A linear contraction propagates an input error without increasing it.</cite> This analysis handles each product as a [bilinear map](bilinear-map.md) $\mathcal{B}$ of approximate operands $f'$ and $g'$, which approximate $f$ and $g$. Bilinearity gives $\mathcal{B}(f',g')-\mathcal{B}(f,g)=\mathcal{B}(f'-f,g')+\mathcal{B}(f,g'-g)$, so for a contraction $\mathcal{B}$ the error is at most $\|f'-f\|\,\|g'\|+\|f\|\,\|g'-g\|$. The analysis keeps every operand within the [Array norm](array-norm.md) bound of one. Thus the analysis keeps every entry in the [closed disk in the complex plane](complex-disk.md) of radius one. <cite data-source="paper">When all four operands are in the disk, their two errors therefore add.</cite>

## Stage errors

This step bounds the error of the [Convolution over the polynomial ring](polynomial-ring-convolution.md), which is computed by two forward synthetic transforms, a pointwise product and an opposite transform. For disk-grid ring arrays $f$ and $g$, the normalized convolution is $(f*g)/(r(T/r)^2)$. Multiplying by $T/r$ gives $(f*g)/T$.

<cite data-source="paper">the three transform errors and the polynomial-product truncation total less than</cite> $3\log_2 T+2$ units before that multiplication. So the ring stage error is $E_{\rm ring}=\frac{T}{r}(3\log_2 T+2)$ units, and since $r\ge1$ and $\log_2T\ge1$, $E_{\rm ring}<5T\log_2 T$.

The normalized convolution is a bilinear contraction, so with $\|f\|\le.7$ and $\|g\|\le1$ its computed output has norm below $.701$ for large $n$.

This analysis bounds the error of the [Phase twist](phase-twist.md) at each end by $4h_p$. A computed unit phase lies within $2h_p$ of the exact one, and truncation adds $2h_p$, so <cite data-source="paper">(2∥x∥ + 2)hp < 4hp</cite> for every operand of norm at most $1$. The complex convolution therefore has error $E_{\rm ring}$ plus three twists, <cite data-source="paper">(Ering + 4 + 4 + 4)hp < 6T Lhp</cite>.

Here $\gamma=2d\alpha^2$ is the construction constant of the source, where $d=\lfloor b^{\epsilon}\rfloor$ is the number of axes and $\alpha=\lceil(12d^2b)^{1/4}\rceil$. Since $\alpha\le2(12d^2b)^{1/4}$ and $d\le b^\epsilon$, $\gamma<28d^2\sqrt b\le28\,b^{1/2+2\epsilon}$. This uses the growth rule of [Little-o notation](little-o-notation.md) to conclude $\gamma=o(b)$, since $1/2+2\epsilon<1$.

The source transform multiplies grid numerators by $2^\gamma$. <cite data-source="paper">The error before the source scale is less than 2dp2 + 8T L.</cite> <cite data-source="paper">bounds on n, T give b/2 ≤ log2 T ≤ b.</cite> So $T\log_2T\ge2n$, and $2dp^2<T\log_2T$ for large $n$, since $2dp^2$ is polylogarithmic. Each source transform has error $E_s=9\cdot2^\gamma T\log_2T$ units, where $E_s$ is measured in units of $h_p$.

## Digit arrays and the final coefficients

Let $\delta$ and $\delta'$ be the radix-$2^b$ digit arrays of the two inputs, as in [Radix-digit convolution](radix-digit-convolution.md), and let $\sigma=2^{-b-2}$. Each entry of $\sigma\delta$ lies in $[0,1/4)$, so the scaled digit arrays have norm below $1/4$.

Let $\varpi=(\sigma\delta\ast\sigma\delta')/S$ be the normalized digit convolution. This analysis takes its scale from the [Prime source lengths](prime-source-lengths.md), whose product is $S$. <cite data-source="paper">Together with si < ti , this gives T /2 < S < T .</cite>

<cite data-source="paper">The exact source transform RFs is a contraction</cite>, so the computed transforms of $\sigma\delta$ and $\sigma\delta'$ have norm below $.26$ and error below $E_sh_p$ each. Their pointwise product, truncated, has error below $(2E_s+2)h_p$, since each factor's error is weighted by a norm at most $1$, and truncation adds $2h_p$. Its norm is at most $.262<.5$, and <cite data-source="paper">Finally let the input to a source transform have norm at most .5.</cite>

The stage bound includes the error of the [Opposite transform](opposite-transform.md), which adds $E_s$ units. As a linear contraction, it passes the input error on unchanged; the total is $3E_s+2$ units. Multiplying by $S$ gives $\tilde\varpi$, which approximates $\varpi$ with error $E_{\varpi}=S(3E_s+2)$ units. Since $S\le T$ and $2T<2^\gamma T\log_2T$, $E_{\varpi}<28\cdot2^\gamma T^2\log_2T$.

In the source's notation, $w=\varpi$. <cite data-source="paper">Each coefficient of w is an average of S products of coefficients of u and v, so ∥w∥ < 1/16.</cite> Hence $\|\tilde\varpi\|<1/16+E_{\varpi}h_p<1$, because $E_{\varpi}h_p\le28\cdot2^\gamma T^2\log_2T\,2^{-6b}\to0$.

The final scaling undoes the normalizations of the [Normalization scales](normalization-scales.md): $2^{2b+4}$ reverses the two digit scales ($\sigma^2=2^{-2b-4}$), and $S$ reverses the division by $S$. Each scaling is exact on the integer [Grid numerator](grid-numerator.md) of each value, so it adds no error. The result approximates $2^{2b+4}S\varpi=\delta\ast\delta'$, the integer convolution of the digits, with error $2^{2b+4}SE_{\varpi}h_p$.

Using $E_{\varpi}<28\cdot2^\gamma T^2\log_2T$ and $h_p=2^{-6b}$,
$$2^{2b+4}SE_{\varpi}h_p<448\,S\,T^2\log_2T\,2^{\gamma-4b}.$$
Since $S\le T\le2^b$ and $\log_2T\le b$ (because $n\le2^b$ and $T<8n/b$), the right side is at most $448\,b\,2^{\gamma-b}$. <cite data-source="paper">b ≥ 224 implies γ ≤ b/4.</cite> The error is therefore below $448\,b\,2^{-3b/4}<1/2$ for large $n$, and rounding returns each coefficient exactly.
