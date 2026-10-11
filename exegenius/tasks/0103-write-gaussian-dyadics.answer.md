The Gaussian dyadics are the number set in which the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) is computed. This page shows that the set is closed under the operations the layer uses, so intermediate values stay exact.

Let $\mathbb{D}$ denote the set of Gaussian dyadics. Each element of $\mathbb{D}$ has the form $a/2^k$, in which $a$ is a Gaussian integer, an element of $\mathbb{Z}[i]$, and $k$ is the number of factors of two in the denominator. Equivalently, the real and imaginary parts of $a/2^k$ are integers divided by $2^k$.

The number $\frac{1+i}{2}$ is in $\mathbb{D}$, with $a=1+i$ and $k=1$. The number $\frac{1}{3}$ is not. If $\frac{1}{3}=\frac{a}{2^k}$, then $a=\frac{2^k}{3}$ is real, so it is an integer, because a Gaussian integer with zero imaginary part has an integer real part. Then $3$ would divide $2^k$, which is impossible.

The set is closed under addition and multiplication. For a second element $\frac{b}{2^l}$, with $b$ a Gaussian integer and $l$ the number of factors of two in its denominator, the product is $\frac{a}{2^k}\cdot\frac{b}{2^l}=\frac{ab}{2^{k+l}}$, where $ab\in\mathbb{Z}[i]$. For a sum, rewrite both terms over $2^{\max(k,l)}$. For example, $\frac{1+i}{2}\cdot\frac{1-i}{2}=\frac{2}{4}=\frac{1}{2}$.

Gaussian dyadics contain every [phase factor](phase-factor.md) that is a power of $i$, since $i^j$ is a Gaussian integer.

A kernel is a fixed linear map applied to an array of values. The paper's kernels stay in this set: <cite data-source="paper">Each entry of CU and its inverse is a</cite> Gaussian integer divided by a power of two, <cite data-source="paper">so both preserve arrays over Z[i, 1/2].</cite>

The simultaneous butterfly layer applies a two-point map to several selected address bits in one pass. It depends on this set because <cite data-source="paper">Intermediate values are exact Gaussian dyadics,</cite> so no step inside the layer rounds. <cite data-source="paper">wrappers, and scalar corrections above are exact Gaussian dyadic operations.</cite> <cite data-source="paper">The entire layer is evaluated exactly before one final truncation.</cite>
