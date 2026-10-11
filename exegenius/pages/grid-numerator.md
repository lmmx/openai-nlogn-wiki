A grid numerator is the integer that stores a grid value exactly, so arithmetic on grid values becomes exact integer arithmetic. It matters for [exact coefficient recovery](recovery-and-error.md), where rounding returns exact integer coefficients.

For a fixed precision $p$, the number of fractional binary places kept, the grid spacing is $2^{-p}$. A grid value has real and imaginary parts that are integer multiples of $2^{-p}$. The integer multiplier of its real part is $\sigma_1$, and of its imaginary part is $\sigma_2$. So the grid value is $2^{-p}(\sigma_1+i\sigma_2)$ with $\sigma_1,\sigma_2\in\mathbb{Z}$, where $i$ is the imaginary unit, and its grid numerator is $\sigma_1+i\sigma_2$. <cite data-source="paper">A p-bit grid array has real and imaginary coefficient parts in 2−p Z.</cite>

A grid numerator is the numerator of a [Gaussian dyadic](gaussian-dyadics.md) with denominator $2^p$. For $p=2$, the grid value $0.75-1.25i$ equals $2^{-2}(3-5i)$, so its grid numerator is $3-5i$. Adding grid values adds their numerators.

The paper's rounding step produces grid values from products. Let $r$ be the record length. Here $\Gamma_j$ is the $j$th output coefficient of the product, a Gaussian integer (the paper's $H_j$). <cite data-source="paper">Gaussian integer coefficient Hj is a sum of exactly r signed products of Gaussian integer input</cite> <cite data-source="paper">coefficients of modulus at most 2p</cite>. So $|\Gamma_j|\le r\,2^{2p}$.

Dividing by $2^p r$ and truncating each part maps $\Gamma_j$ to a grid value. $\mathrm{trunc}_0$ replaces a real number by the integer nearest to it on the side of $0$, so $\mathrm{trunc}_0(-2.7)=-2$. <cite data-source="paper">Finally the p-bit grid numerator of the normalized product is</cite>
$$\mathrm{trunc}_0\!\left(\frac{\operatorname{Re} \Gamma_j}{2^p r}\right)+i\,\mathrm{trunc}_0\!\left(\frac{\operatorname{Im} \Gamma_j}{2^p r}\right).$$
<cite data-source="paper">The returned coefficient is 2−p times this numerator</cite>.

Truncation does not increase magnitude, so each component has magnitude at most $|\Gamma_j|/(2^p r)\le 2^p$. <cite data-source="paper">Each returned component numerator has magnitude at most 2p</cite>. A signed two's-complement word of $\mu$ bits holds every integer from $-2^{\mu-1}$ to $2^{\mu-1}-1$, so $\mu=p+2$ bits hold each component.

Each grid numerator is an input to [Carry propagation](carry-propagation.md), which converts integer coefficients into a binary string.
