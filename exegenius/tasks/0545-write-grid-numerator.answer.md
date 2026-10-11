A grid numerator is the integer that stores a numerical value exactly on a fixed grid, so arithmetic on it is exact integer arithmetic. The [exact coefficient recovery](recovery-and-error.md) analysis works with these integers.

For a fixed precision $p$, the number of fractional binary places kept, the grid spacing is $2^{-p}$. A grid value of precision $p$ has real and imaginary parts that are integer multiples of $2^{-p}$, so it has the form $2^{-p}(\sigma_1+i\sigma_2)$ with $\sigma_1,\sigma_2\in\mathbb{Z}$ the integer multipliers of the real and imaginary parts. Its grid numerator is $\sigma_1+i\sigma_2$.

A grid numerator is the numerator of a [Gaussian dyadic](gaussian-dyadics.md) with denominator $2^p$. For $p=2$, the grid value $0.75-1.25i$ equals $2^{-2}(3-5i)$, so its grid numerator is $3-5i$. Adding grid values adds their numerators. <cite data-source="paper">A p-bit grid array has real and imaginary coefficient parts in 2−p Z.</cite> So an array of grid values is stored as its array of grid numerators.

In the paper's polynomial multiplication, $W$ denotes one output coefficient (the paper's $H_j$). <cite data-source="paper">each resulting Gaussian integer coefficient Hj is a sum of exactly r signed products of Gaussian integer input coefficients of modulus at most 2p</cite>, where $r$ is the record length. So each input numerator has modulus at most $2^p$, each product at most $2^{2p}$, and $|W|\le r\,2^{2p}$.

Here $\mathrm{trunc}_0$ replaces a real number by the integer nearest to it on the side of $0$, so $\mathrm{trunc}_0(-2.7)=-2$.

<cite data-source="paper">Finally the p-bit grid numerator of the normalized product is</cite>
$$\mathrm{trunc}_0\!\left(\frac{\operatorname{Re} W}{2^p r}\right)+i\,\mathrm{trunc}_0\!\left(\frac{\operatorname{Im} W}{2^p r}\right).$$
<cite data-source="paper">The returned coefficient is 2−p times this numerator</cite>.

Truncation does not increase magnitude, so each component has magnitude at most $|W|/(2^p r)\le 2^p$. <cite data-source="paper">Each returned component numerator has magnitude at most 2p</cite>. A signed two's-complement word of $J$ bits, where $J$ is the number of bits, holds every integer from $-2^{J-1}$ to $2^{J-1}-1$, so $J=p+2$ bits hold each component.

Each grid numerator is an input to [carry propagation](carry-propagation.md), which converts integer coefficients into a binary string.
