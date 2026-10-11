Exact coefficient recovery is the error analysis showing that each convolution coefficient, computed through approximate transforms, lies within one half of its true integer value, so rounding returns that integer exactly. It is the last step of the argument for exact integer multiplication: it certifies that the approximate computation yields the exact product.

## Why rounding recovers the integer

The true coefficients are integers, and distinct integers are at least $1$ apart. If a computed value $x$ satisfies $|x-m|<1/2$ for an integer $m$, every other integer is farther than $1/2$ from $x$, so $m$ is the unique nearest integer and rounding returns $m$. For example, $7.3$ rounds to $7$, while $7.6$ rounds to $8$. The goal is therefore to bound the total error of each coefficient strictly below $1/2$. <cite data-source="paper">The strict error below 1/2 makes the nearest integer to that value the</cite> unique correct coefficient, and <cite data-source="paper">The true coefficients are real integers.</cite>

## Units

Each stored value keeps $p$ fractional bits, so it is a multiple of $2^{-p}$. Write $h_p = 2^{-p}$ for the size of one unit in the last place of a stored value; an error of $a$ units is an absolute error below $a\,h_p$. This analysis takes its guard widths from the [Guard-width bound](guard-width-bound.md), so each stored value is exact and only the stated truncations contribute error. The source sets $b = \lceil\log_2 n\rceil$, the number of bits in each radix digit, and <cite data-source="paper">p = 6b,</cite> so $h_p = 2^{-6b}$.

## Errors add across stages

Each stage works on values that already carry error. <cite data-source="paper">A linear contraction propagates an input error without increasing it.</cite> For a [Bilinear map](bilinear-map.md) of two approximate operands, the error of the result sums the errors of the operands, each weighted by the norm of the other. This analysis bounds the norm of every operand by one, where the norm is the [Array norm](array-norm.md), the largest modulus of an entry. An array of norm at most one lies in the unit disk, so the two errors simply add: <cite data-source="paper">When all four operands are in the disk, their two errors therefore add.</cite>

The operand bound holds stage by stage. <cite data-source="paper">The scaled radix digits in u, v are exact p-bit grid values of norm strictly less than 1/4.</cite> The paper's margin argument then keeps each computed ring output below $0.701$, since it <cite data-source="paper">has norm less than .7 + 5T Lhp < .701</cite>.

## The polynomial-ring stage

This step bounds the error of the [Convolution over the polynomial ring](polynomial-ring-convolution.md), computed from two forward transforms, a pointwise product, and an opposite transform. Here $T$ counts the entries of the [Padded transform box](padded-transform-box.md), a power of two in $[4n/b, 8n/b)$, and $L=\log_2 T$; the letter $L$ changes meaning here. The stage bound includes the error of the [Opposite transform](opposite-transform.md), which inverts the forward transform up to a known factor, and of both forward transforms. <cite data-source="paper">the three transform errors and the polynomial-product truncation total less than</cite> $3L+2$ units of $h_p$. The scale $T/r$ is at most $T$ because $r\ge 1$, and $L\ge 1$ gives $3L+2\le 5L$. Call this error $E_{\rm ring}$, in units of $h_p$; so $E_{\rm ring}<5TL$.

Each twist at the ends of the ring map adds an error too. This analysis bounds the error of the [Phase twist](phase-twist.md) at each end of the ring map by $4h_p$, because rounding to the grid adds <cite data-source="paper">(2∥x∥ + 2)hp < 4hp</cite> for an operand of norm at most one. The complex convolution has error $E_{\rm ring}$ plus three such twists: <cite data-source="paper">(Ering + 4 + 4 + 4)hp < 6T Lhp</cite>.

## Summing the stage errors

Summing the stage errors, each in units of $h_p$, gives the total error of the coefficient. The source transform contributes an error $E_s$ in units of $h_p$, with <cite data-source="paper">Es = 9 2γ T L,</cite> and the products and the opposite transform together add $3E_s+2$ units. The first multiplication by $S$ then gives the scaled result with error $E_w$ units, where <cite data-source="paper">Ew := S(3Es + 2)</cite>.

## Scaling and the final bound

Here $\gamma$ is the construction constant of the source. Both scaling multiplications act exactly on the integer [Grid numerator](grid-numerator.md) of each value, so they add no error of their own. The final scaling undoes the normalizations of the [Normalization scales](normalization-scales.md): $S$ reverses the normalization left in the first result, and $2^{2b+4}$ reverses the two input scales. The final bound divides by the product $S$ of the [Prime source lengths](prime-source-lengths.md). The bound uses the growth of $\gamma$ in the [Little-o notation](little-o-notation.md) sense: $\gamma = o(b)$.

<cite data-source="paper">Since S ≤ T < 2b and L < b eventually, the final</cite> absolute error of each coefficient is $\frac{1}{2^{2b+4}S}\cdot 28\cdot 2^{\gamma}\,T^2L\cdot 2^{-6b}$, where $2^{-6b}=h_p$. Using $T<2^b$ and $L<b$, this is at most $448\,b\,2^{-b+\gamma}$. Since $\gamma\le b/4$ for large $n$, it is at most $448\,b\,2^{-3b/4}$, which is below $1/2$ for large $n$.

With the total error below $1/2$, the computed coefficient lies within $1/2$ of the true integer, and rounding to the nearest integer returns it exactly.
