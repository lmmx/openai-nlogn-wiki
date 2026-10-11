Exact coefficient recovery is the error analysis that makes the final rounding return the true integer convolution coefficients. It is the last step of the argument for exact integer multiplication: the convolution is computed through approximate transforms, and this page shows that the accumulated error stays below one half, so rounding gives exactly the integers the product needs.

## Why rounding recovers the integer

The true coefficients are integers, and distinct integers are at least $1$ apart. If a computed value $x$ satisfies $|x - m| < 1/2$ for an integer $m$, then every other integer is farther than $1/2$ from $x$, so $m$ is the unique nearest integer and rounding returns $m$. For example, if the true coefficient is $7$, a computed value $7.3$ (error $0.3$) rounds to $7$, while a computed value $7.6$ (error $0.6$) rounds to $8$. The goal is therefore to bound the total error of each coefficient by a quantity strictly below $1/2$. <cite data-source="paper">The strict error below 1/2 makes the nearest integer to that value the</cite> unique correct coefficient, and <cite data-source="paper">The true coefficients are real integers.</cite>

## Units

Each stored value keeps $p$ fractional bits, the number of binary places after the point. Write $h_p = 2^{-p}$ for the size of one unit in the last place of a stored value, so an error measured in units of $h_p$ is an absolute error below that multiple of $h_p$. It takes its guard widths from the [guard-width bound](guard-width-bound.md), so each stored value is exact and only the stated truncations contribute error. The source sets $b = \lceil \log_2 n\rceil$, the number of bits in each radix digit, and $p = 6b$, so $h_p = 2^{-6b}$. <cite data-source="paper">p = 6b,</cite>

## Errors add across stages

Each stage works on values that already carry error from the stages before it. A linear map never increases an input error. <cite data-source="paper">A linear contraction propagates an input error without increasing it.</cite> For a bilinear product of two approximate operands, the operand errors add: the error of the product is at most the error of the first operand times the norm of the second, plus the norm of the first times the error of the second. Here the operands lie in the unit disk, arrays of norm at most one, so every norm is at most one and the two errors simply add. <cite data-source="paper">When all four operands are in the disk, their two errors therefore add.</cite> Summing the stage errors, each measured in units of $h_p$, gives the total error of the coefficient.

## The polynomial-ring stage

The convolution over the polynomial ring is computed from two forward transforms, a pointwise product, and an opposite transform, with one truncation in the product. Here $T$ is the number of entries in the padded transform box, a power of two chosen in $[4n/b, 8n/b)$, and $L = \log_2 T$. This step bounds the error of [Convolution over the polynomial ring](polynomial-ring-convolution.md) by $5TL\,h_p$. Before the exact scale, <cite data-source="paper">the three transform errors and the polynomial-product truncation total less than</cite> $3L+2$ units of $h_p$. <cite data-source="paper">Thus the error of the returned normalized convolution is bounded by</cite> $5TL\,h_p$.

The twists at the two ends of the ring map also carry error. It counts the error of the [phase twist](phase-twist.md) at each end, each below $4h_p$, so these errors enter the same sum.

## Scaling and the final bound

Two exact multiplications by known scales undo the normalizations. Each acts exactly on grid numerators, so it adds no error of its own and only rescales the error already present. Here $S$ is the product of the pairwise coprime source lengths, and $\gamma$ is a construction constant with $\gamma = o(b)$. <cite data-source="paper">Since S ≤ T < 2b and L < b eventually, the final</cite> absolute error of each coefficient is bounded by $\frac{1}{2^{2b+4}S}\cdot 28\sqrt{2}\,\gamma\,T^2 L\cdot 2^{-6b}$. This is at most $448\,b\,2^{-b+\gamma} \le 448\,b\,2^{-3b/4}$, which is less than $1/2$ for large $n$. The last factor $2^{-6b}$ is $h_p$, one unit of the stored precision.

With the error below $1/2$, the computed coefficient lies within $1/2$ of the true integer, and rounding to the nearest integer returns it exactly.
