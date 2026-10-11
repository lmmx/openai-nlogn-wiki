Exact coefficient recovery is the error analysis showing that each convolution coefficient, computed through approximate transforms, lies strictly within one half of its true integer, so rounding returns it exactly. It is the last step of the argument for exact integer multiplication.

## Why rounding recovers the integer

<cite data-source="paper">The true coefficients are real integers.</cite> Distinct integers are at least $1$ apart, so if a computed value $x$ satisfies $|x-m|<1/2$ for an integer $m$, then $m$ is the unique nearest integer and rounding returns $m$. So it suffices to bound each coefficient's total error strictly below $1/2$.

## Units and error sources

Each stored value keeps $p$ fractional bits. Write $h_p = 2^{-p}$ for the size of one unit in the last place; an error of $a$ units is an absolute error below $a\,h_p$. The source sets $b = \lceil\log_2 n\rceil$ and <cite data-source="paper">p = 6b,</cite> so $h_p = 2^{-6b}$.

This analysis takes its guard widths from the [Guard-width bound](guard-width-bound.md), so every intermediate value is exact. Errors come only from the transforms and the truncations $Q_p$.

## Errors add across stages

<cite data-source="paper">A linear contraction propagates an input error without increasing it.</cite> For a bilinear map $\mathcal{C}$ that is a contraction, $\|\mathcal{C}(f,g)\|\le\|f\|\,\|g\|$, and bilinearity gives $\mathcal{C}(f',g')-\mathcal{C}(f,g)=\mathcal{C}(f'-f,g')+\mathcal{C}(f,g'-g)$. Products of approximate operands are [Bilinear map](bilinear-map.md)s, and this analysis bounds the error of each product by $\|f'-f\|\,\|g'\|+\|f\|\,\|g'-g\|$: each operand error is weighted by the norm of the other operand. This analysis bounds every operand in the [Array norm](array-norm.md) by one, so each lies in the disk. <cite data-source="paper">When all four operands are in the disk, their two errors therefore add.</cite>

## The polynomial-ring stage

Here $T$ counts the entries of the [Padded transform box](padded-transform-box.md). <cite data-source="paper">bounds on n, T give b/2 ≤ log2 T ≤ b.</cite> Write $L=\log_2 T$, so $L\le b$; the letter $L$ changes meaning here.

This step bounds the error of the [Convolution over the polynomial ring](polynomial-ring-convolution.md), which is computed from two forward synthetic transforms, a pointwise product and an opposite transform. The stage bound includes the error of the [Opposite transform](opposite-transform.md) and of both forward transforms. Each has error less than $L$ units <cite data-source="paper">where L = log2 T</cite>, and truncating the product adds less than $2$ units: <cite data-source="paper">the three transform errors and the polynomial-product truncation total less than</cite> $3L+2$ units of $h_p$. The normalized form scales this by $T/r$, where $r$ is the record length, so the stage error is $E_{\rm ring}=\frac{T}{r}(3L+2)$ units; since $r\ge1$ and $L\ge1$, $E_{\rm ring}<5TL$.

With one operand of norm at most $.7$, the exact output has norm at most $.7$. <cite data-source="paper">output consequently has norm less than .7 + 5T Lhp < .701 for large n.</cite>

The [Phase twist](phase-twist.md) at each end of the ring map adds error too: this analysis bounds the error of the phase twist at each end by $4h_p$. The phase error costs $2\|x\|h_p$, grid truncation adds $2h_p$, and <cite data-source="paper">(2∥x∥ + 2)hp < 4hp</cite> for $\|x\|\le1$. So the complex convolution has error $E_{\rm ring}$ plus three twists: <cite data-source="paper">(Ering + 4 + 4 + 4)hp < 6T Lhp</cite>.

## The source transform

Here $\gamma = 2d\alpha^2$ is the construction constant of the source; the letter $\gamma$ changes meaning here. The source transform multiplies grid numerators by $2^\gamma$. Call the source-transform error $E_s$, in units of $h_p$. <cite data-source="paper">The error before the source scale is less than 2dp2 + 8T L.</cite> Multiplying by $2^\gamma$, and using $2dp^2<TL$ for large $n$, gives <cite data-source="paper">Es = 9 2γ T L,</cite> so $E_s=9\cdot 2^\gamma TL$ units.

The pointwise product adds $2E_s+2$ units and the opposite transform adds $E_s$ more, so the total is $3E_s+2$ units. The first multiplication by $S$, the product of the [Prime source lengths](prime-source-lengths.md), gives the scaled result $\tilde w$, which approximates $w$, the convolution of the digit arrays divided by $S$; call its error $E_w$, in units of $h_p$. Here <cite data-source="paper">Ew := S(3Es + 2)</cite>, and since $S\le T$, $E_w<28\cdot 2^\gamma T^2L$.

## Disk bounds stage by stage

The digit arrays have norm below $1/4$ <cite data-source="paper">The scaled radix digits in u, v are exact p-bit grid values of norm strictly less than 1/4.</cite> The scaled source transform is a contraction, so its outputs have norm below $1/4+E_sh_p<.26$, and the truncated product has norm at most $.262<.5$, which the opposite transform accepts. <cite data-source="paper">Each coefficient of w is an average of S products of coefficients of u and v, so ∥w∥ < 1/16.</cite> For large $n$, $E_sh_p$, $5TLh_p$ and $E_wh_p$ are all below $10^{-3}$, so $\|\tilde w\|<1/16+10^{-3}<1$.

## Scaling and the final bound

Each scaling is exact on the integer [Grid numerator](grid-numerator.md) of each value, so it adds no error. The final scaling undoes the normalizations of the [Normalization scales](normalization-scales.md): $2^{2b+4}$ reverses the two digit scales, and the factor $S$, the product of the [Prime source lengths](prime-source-lengths.md), reverses the division by $S$ left in $\tilde w$. The result approximates $2^{2b+4}S\,w=2^{2b+4}(u*v)$, with error $2^{2b+4}S\,E_w\,h_p$. Using $E_w<28\cdot 2^\gamma T^2L$ and $h_p=2^{-6b}$,
$$2^{2b+4}S\,E_w\,h_p<2^{2b+4}\cdot S\cdot 28\cdot 2^{\gamma}T^2L\cdot 2^{-6b}=448\,S\,T^2L\,2^{\gamma-4b}.$$
<cite data-source="paper">Since S ≤ T < 2b and L < b eventually, the final</cite> bound follows: with $S\le T\le 2^b$ and $L\le b$, the right side is at most $448\,b\,2^{\gamma-b}$. The bound uses the growth rule of [Little-o notation](little-o-notation.md) for $\gamma$: $\gamma=o(b)$. Since <cite data-source="paper">b ≥ 224 implies γ ≤ b/4.</cite> it is at most $448\,b\,2^{-3b/4}$, which is below $1/2$ for large $n$. Rounding therefore returns each coefficient exactly.
