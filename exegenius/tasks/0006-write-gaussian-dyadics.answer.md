A Gaussian dyadic is a complex number whose real and imaginary parts are integers divided by a common power of two. The simultaneous butterfly layer depends on this set: its intermediate values stay in it, so the layer is computed exactly and rounding happens only once, at the end.

Let $\mathbb{D}$ denote the set of Gaussian dyadics. Each element of $\mathbb{D}$ has the form $a/2^k$, in which $a$ is a Gaussian integer, an element of $\mathbb{Z}[i]$, and $k$ is a non-negative integer, the power of two in the denominator. Since $a$ has integer real and imaginary parts, the real and imaginary parts of $a/2^k$ are integers divided by $2^k$.

The number $\frac{1+i}{2}$ is a Gaussian dyadic with $a = 1+i$ and $k = 1$. The number $\frac{1}{3}$ is not one, because $\frac{1}{3} = \frac{a}{2^k}$ would require $3a = 2^k$, which has no solution with $a$ a Gaussian integer.

The set is closed under addition and multiplication. For a product, $\frac{a}{2^k}\cdot\frac{b}{2^l} = \frac{ab}{2^{k+l}}$ with $ab \in \mathbb{Z}[i]$. For a sum, write both terms over $2^{\max(k,l)}$. For instance, $\frac{1+i}{2}\cdot\frac{1-i}{2} = \frac{2}{4} = \frac{1}{2}$.

The paper's kernels stay in this set. The kernel and its inverse have entries that are Gaussian integers divided by $2^m$, <cite data-source="paper">so both preserve arrays over Z[i, 1/2].</cite> <cite data-source="paper">The kernels implemented below have Gaussian dyadic coefficients.</cite>

For the layer itself, <cite data-source="paper">Intermediate values are exact Gaussian dyadics,</cite> and the phase factors and scalar corrections stay in the same set: <cite data-source="paper">wrappers, and scalar corrections above are exact Gaussian dyadic operations.</cite> Because every step is exact, <cite data-source="paper">The entire layer is evaluated exactly before one final truncation.</cite>
