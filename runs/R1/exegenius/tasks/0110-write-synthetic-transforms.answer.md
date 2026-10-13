Synthetic polynomial transforms are defined over the [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md), where every root of unity is a power of $y$, so the transform avoids general complex multiplications. They serve the remaining axes of the convolution.

**Signed shifts.** In this ring $y^r=-1$. Multiplying by $y^e$, where the exponent $e$ is an integer with $0\le e<2r$, moves each coefficient up $e$ places, and each wrap past the last place negates it. For $r=4$, multiplying $1+2y+3y^2+4y^3$ by $y^2$ gives $-3-4y+y^2+2y^3$, so the coefficient list $(1,2,3,4)$ becomes $(-3,-4,1,2)$.

**The transform.** Let $L$ be the number of entries along the transform axis, a power of two dividing $2r$, and let $z_0,\dots,z_{L-1}$ be the input list of ring elements. The transform maps it to the transformed list $Z_0,\dots,Z_{L-1}$, given by

$$Z_g=\frac1L\sum_{p=0}^{L-1} y^{2rgp/L}\,z_p,\qquad 0\le g<L.$$

Here $p$ is the input index and $g$ the output index, both running from $0$ to $L-1$.

**Why the powers are roots of unity.** Since $y^r=-1$, we get $y^{2r}=(y^r)^2=1$, so $y^{2r/L}$ is an $L$-th root of unity, and $y^{2rgp/L}$ is its power $gp$. The root has order exactly $L$: for $0<m<L$, the exponent $e=2rm/L$ lies strictly between $0$ and $2r$, so $y^e$ is never $1$: it is a monomial other than $1$ when $e<r$, and $-y^{e-r}$ when $e\ge r$.

**Butterflies.** Synthetic transforms follow the butterfly scheme of the [Discrete Fourier transform and butterflies](dft-fft.md). Each level replaces a pair $(u,v)$ by $(u+y^{e}v,\;u-y^{e}v)$ for a suitable exponent $e$. Each $y^{e}v$ is a signed shift, the sum and difference are ring additions, and moving entries between levels is an address rearrangement.

**The factor $1/L$.** This factor is not a power of $y$. The formula is linear, so it can be pulled out of the levels and applied once to the output. It is a division by a power of two, which can round; see [Fixed-point precision and exact recovery](fixed-point-precision.md).

Synthetic transforms are costed on a [fixed-tape machine](fixed-tape-model.md), where the cost is data movement.
