The Gaussian dyadics are the number set in which the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) is computed. This page shows that the set is closed under the arithmetic the layer uses, so intermediate values stay exact.

Let $\mathbb{D}$ denote the set of Gaussian dyadics. Let $\mathbb{Z}[i]$ denote the Gaussian integers, the complex numbers whose real and imaginary parts are integers, with $i$ the imaginary unit. A Gaussian dyadic is a quotient of a Gaussian integer by a power of two. Write it as $\delta/2^e$, where $\delta$ is the Gaussian integer numerator, and $e\ge 0$ is the number of factors of two in the denominator.

The number $\frac{1+i}{2}$ is a Gaussian dyadic, with $\delta=1+i$ and $e=1$. The number $\frac{1}{3}$ is not. If $\frac{1}{3}=\frac{\delta}{2^e}$, then $\delta=\frac{2^e}{3}$ is real, hence an integer, and $3\delta=2^e$. So $3$ divides $2^e$. But $2$ is the only prime factor of $2^e$, so this is impossible.

The set is closed under multiplication and addition. Take a second element $\nu/2^{e'}$, where $\nu$ is a Gaussian integer and $e'$ is the number of factors of two in its denominator. Then $\frac{\delta}{2^e}\cdot\frac{\nu}{2^{e'}}=\frac{\delta\nu}{2^{e+e'}}$, with $\delta\nu\in\mathbb{Z}[i]$. For the sum, let $\tau=\max(e,e')$ be the larger exponent:
$$\frac{\delta}{2^e}+\frac{\nu}{2^{e'}}=\frac{2^{\tau-e}\delta+2^{\tau-e'}\nu}{2^{\tau}}.$$
The numerator is a Gaussian integer, since $\mathbb{Z}[i]$ is closed under addition and multiplication by integers. For example, $\frac{1+i}{2}\cdot\frac{1-i}{2}=\frac{2}{4}=\frac{1}{2}$.

The Gaussian dyadics are closed under the operations of the [butterfly](butterfly.md): it takes half-sums and half-differences, and halving is multiplication by $\frac{1}{2}=\frac{1}{2^1}$, a Gaussian dyadic.

Gaussian dyadics contain every [phase factor](phase-factor.md) that is a power of $i$, since every power of $i$ is a Gaussian integer.

The simultaneous butterfly layer depends on this set because <cite data-source="paper">Intermediate values are exact Gaussian dyadics,</cite> so no step inside the layer rounds. A rounding after each step would add error, so the layer skips them: every step stays in the set, and <cite data-source="paper">The entire layer is evaluated exactly before one final truncation.</cite>
