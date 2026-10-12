Here $O(g)$ means at most a constant times $g$ for all large inputs. $\lg n = \max\{\lceil \log_2 n\rceil, 1\}$ is the base-2 logarithm rounded up and at least 1.

The target theorem is that one fixed deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time, and the rest of the argument proves this claim. The constant $\kappa = 2^{-182}$ is the power-saving exponent, the amount by which the power of $\lg n$ falls below one.

Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time disproves the [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md) in this model. Its running time is below $n\log n$ by the factor $(\lg n)^{\kappa}$, which grows without bound.

The integer product is reduced to a convolution of radix-$2^b$ digit sequences, with carries restored to binary, as in [Multiplication as convolution of digits](convolution-reduction.md). The second step computes that convolution by transforms. Each transform level scans $\Theta(n)$ bits, so only savings in both movement and arithmetic beat $n\log n$ <cite data-source="paper">We therefore need savings in both movement and arithmetic.</cite>.

Two tape procedures supply these savings. The algorithm performs its address permutations by [Fast address interchange](address-interchange.md), whose cost is $O(V u^\tau)$ for $\tau<1$. The algorithm builds each transform level from a [Simultaneous butterfly layer](simultaneous-butterfly-layer.md), which acts on one address bit of every record, and whose cost is $O(V d^{\lambda'})$ for $\lambda'<1$.

The power saving follows from [Recursive power saving](recursive-power-saving.md). A network with $s$ smaller calls on $W$ roles and parameter $m$ multiplies the cost by $s/W$ at each level of recursion while dividing the parameter by $m$. Since $s/W<m$, the cost is a power of the parameter with exponent $\log_m(s/W)<1$.

The algorithm arranges its digits by the [Chinese-remainder address map](chinese-remainder-address-map.md) on distinct prime cyclic axes. It computes its transforms by [Gaussian resampling](gaussian-resampling.md), which expresses each prime-length transform through power-of-two axes. It converts its middle transform by [Bluestein's chirp identity](bluestein-chirp.md) into a normalized cyclic convolution. It places its last cyclic coordinate in the [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md), where its wrap is a signed shift. It computes its forward transforms by [Synthetic polynomial transform](synthetic-transform.md), which keep frequency order through their pointwise product. It computes its polynomial products by the [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md) on packed integers from [Signed Kronecker packing](kronecker-packing.md).

The algorithm recovers its exact product by [Exact recovery by rounding](rounding-recovery.md), which rounds the approximate coefficients to integers and propagates carries.
