A Gaussian dyadic is a complex number whose real and imaginary parts are integers divided by a common power of two. The [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) is computed in this set, and the closure properties below keep its intermediate values exact, so rounding is needed only once, at the end.

Let $\mathbb{D}$ denote the set of Gaussian dyadics. The Gaussian integers are the complex numbers whose real and imaginary parts are integers, written $\mathbb{Z}[i]$. Each element of $\mathbb{D}$ has the form $\frac{\Upsilon}{2^{\Xi}}$, where $\Upsilon$, the numerator, is a Gaussian integer and $\Xi \ge 0$ counts the factors of two in the denominator.

Not every rational complex number is one. The number $\frac{1+i}{2}$ is a Gaussian dyadic with $\Upsilon=1+i$ and $\Xi=1$. The number $\frac{1}{3}$ is not: if $\frac{1}{3}=\frac{\Upsilon}{2^{\Xi}}$, then $\Upsilon=\frac{2^{\Xi}}{3}$ is real, hence an integer, so $3$ divides $2^{\Xi}$. But $2$ is the only prime factor of $2^{\Xi}$.

The set is closed under the arithmetic of the layer. For a second element $\frac{\Upsilon'}{2^{\Xi'}}$, written with primes, the product is
$$\frac{\Upsilon}{2^{\Xi}}\cdot\frac{\Upsilon'}{2^{\Xi'}}=\frac{\Upsilon\Upsilon'}{2^{\Xi+\Xi'}},$$
and the sum is
$$\frac{\Upsilon}{2^{\Xi}}+\frac{\Upsilon'}{2^{\Xi'}}=\frac{2^{\max(\Xi,\Xi')-\Xi}\,\Upsilon+2^{\max(\Xi,\Xi')-\Xi'}\,\Upsilon'}{2^{\max(\Xi,\Xi')}}.$$
Both numerators are Gaussian integers, because $\mathbb{Z}[i]$ is closed under addition and multiplication. Negation replaces $\Upsilon$ by $-\Upsilon$. For example, $\frac{1+i}{2}\cdot\frac{1-i}{2}=\frac{2}{4}=\frac{1}{2}$.

The Gaussian dyadics are closed under the operations of the [Butterfly](butterfly.md). The butterfly $H_0(\xi,\zeta)=\left(\frac{\xi+\zeta}{2},\frac{\xi-\zeta}{2}\right)$ takes a sum, a difference and a halving. Halving is multiplication by $\frac{1}{2}=\frac{1}{2^1}$, a Gaussian dyadic with $\Upsilon=1$ and $\Xi=1$. For example, $H_0(1,i)=\left(\frac{1+i}{2},\frac{1-i}{2}\right)$, and both outputs have exponent $1$.

The layer also multiplies entries by [phase factors](phase-factor.md). The Gaussian dyadics contain every power of $i$, a [phase factor](phase-factor.md), because each power of $i$ is a Gaussian integer.

The paper states that <cite data-source="paper">Intermediate values are exact Gaussian dyadics,</cite> and that <cite data-source="paper">wrappers, and scalar corrections above are exact Gaussian dyadic operations.</cite> Rounding inside the layer would add an error at each step, so the layer does not round there. <cite data-source="paper">The procedure evaluates the entire layer exactly before this final truncation.</cite>
