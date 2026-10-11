The Gaussian dyadics are the number set in which the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) is computed. This page shows that the set is closed under the arithmetic the layer uses, so its intermediate values stay exact.

Let $\mathcal{G}$ denote the set of Gaussian dyadics, and $\mathbb{Z}[i]$ the Gaussian integers, the complex numbers whose real and imaginary parts are integers. A Gaussian dyadic is a number $\sigma/2^{\Gamma}$, where the numerator $\sigma$ is a Gaussian integer and the exponent $\Gamma\ge 0$ is the number of factors of two in the denominator.

Not every rational complex number is one. The number $\frac{1+i}{2}$ is a Gaussian dyadic, with $\sigma=1+i$ and $\Gamma=1$. The number $\frac{1}{3}$ is not: if $\frac{1}{3}=\frac{\sigma}{2^{\Gamma}}$, then $\sigma=\frac{2^{\Gamma}}{3}$ is real, hence an integer, so $3$ divides $2^{\Gamma}$. But $2$ is the only prime factor of $2^{\Gamma}$, which rules this out.

The set is closed under multiplication, addition and negation. For a second element $\sigma'/2^{\Gamma'}$, with $\sigma'$ a Gaussian integer and $\Gamma'$ its number of factors of two,
$$\frac{\sigma}{2^{\Gamma}}\cdot\frac{\sigma'}{2^{\Gamma'}}=\frac{\sigma\sigma'}{2^{\Gamma+\Gamma'}},$$
where $\sigma\sigma'\in\mathbb{Z}[i]$. For a sum, let $\Upsilon=\max(\Gamma,\Gamma')$:
$$\frac{\sigma}{2^{\Gamma}}+\frac{\sigma'}{2^{\Gamma'}}=\frac{2^{\Upsilon-\Gamma}\sigma+2^{\Upsilon-\Gamma'}\sigma'}{2^{\Upsilon}}.$$
The numerator is a Gaussian integer, since $\mathbb{Z}[i]$ is closed under addition and multiplication by integers. Negation changes only the sign of $\sigma$. For example, $\frac{1+i}{2}\cdot\frac{1-i}{2}=\frac{2}{4}=\frac{1}{2}$.

The Gaussian dyadics are closed under the operations of the [Butterfly](butterfly.md): it takes half-sums and half-differences. The butterfly $H_0(u,v)=\left(\frac{u+v}{2},\frac{u-v}{2}\right)$ is a sum, a difference, and a halving. Halving is multiplication by $\frac{1}{2}=\frac{1}{2^1}$, which is a Gaussian dyadic. For example, $H_0(1,i)=\left(\frac{1+i}{2},\frac{1-i}{2}\right)$, and both outputs have exponent $1$.

The layer also multiplies entries by [Phase factor](phase-factor.md)s. The Gaussian dyadics contain the powers of $i$, each a [Phase factor](phase-factor.md), since every power of $i$ is a Gaussian integer.

Each step of the layer is therefore a sum, difference, halving or multiplication by a power of $i$, and each maps Gaussian dyadics to Gaussian dyadics. Rounding after each step would add an error at that step, so the layer does not round inside. <cite data-source="paper">Intermediate values are exact Gaussian dyadics</cite>, and <cite data-source="paper">The entire layer is evaluated exactly before one final truncation.</cite>
