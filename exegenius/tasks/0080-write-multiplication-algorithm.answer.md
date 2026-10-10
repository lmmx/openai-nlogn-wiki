The multiplication algorithm combines the earlier reductions into one procedure for exact integer multiplication. It splits each input into radix-$2^b$ digits, lays the coefficients on a padded power-of-two box, computes three transforms, multiplies them pointwise, and recovers the integer product by rounding and carries.

Let $q = \lceil n/b \rceil$ and $S$ be the padded length. The two inputs become polynomials of degree below $q$ in $2^b$, so their product has degree at most $2q - 2 < S$. Thus the [radix-digit convolution](radix-digit-convolution.md) is a cyclic convolution of length $S$ with no wraparound. The [parameter choice](parameter-choice.md) fixes $S$, $b$, and $p$.

The main steps, following the paper, are:

1. Apply the coefficient-address map $\Phi$ from the [Chinese-remainder address map](chinese-remainder-map.md) to the two source arrays $u$ and $v$. Their coefficients are exact $p$-bit [grid values](disk-grid-values.md).
2. Compute the forward source transforms $\hat u$ and $\hat v$. These use [Gaussian resampling](gaussian-resampling.md) together with the [Bluestein chirp identity](bluestein-chirp-identity.md), and each layer is a [synthetic transform](synthetic-transform.md) evaluated with [simultaneous butterfly layers](simultaneous-butterfly-layer.md). The coordinate layouts are changed by the [address-field interchange](address-interchange.md) procedure.
3. Multiply the complex coefficients of $\hat u$ and $\hat v$ pointwise, and truncate each part to $p$ fractional bits. Call the result $z$. The products of polynomial records in this step use [signed coefficient packing](signed-packing.md).
4. Compute the opposite-sign transform $\hat z^{+}$, and multiply its numerators by $S$. Call the result $w$. The [phase twist](phase-twist.md) is applied to the last coordinate in these transforms.
5. Multiply the numerators of $w$ by $2^{2b+4} S$, round each value to the nearest integer, and apply $\Phi^{-1}$ to restore the ordinary coefficient order.
6. Propagate radix-$2^{b}$ carries from low to high coefficients, and output exactly $2n$ bits, most significant first.

The two factors of $S$ undo two different normalizations. Without them, the transform identity gives $(u \ast v)/S^2$ as the exact counterpart after the three transforms. After the first scale the result is $(u \ast v)/S$, and the second scale gives $2^{2b+4}(u \ast v)$, whose inverse image under $\Phi$ is the integer coefficient convolution.

The permutations that appear in the transform identity are not executed as separate sorts. The paper shows that they cancel across the two forward transforms, their pointwise product, and the opposite-sign transform, so that the net effect is the identity. The [precision and exact recovery](precision-and-rounding.md) argument shows that the rounding in step 5 returns the true coefficients.
