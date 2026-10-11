A grid numerator is the integer pair that stores a numerical value exactly on a fixed grid, so arithmetic on it is exact integer arithmetic. These integers are worked on by the error analysis and the [carry propagation](carry-propagation.md) that follow.

Here $p$ is the number of fractional binary places kept, so the grid spacing is $2^{-p}$. Here $\mathbb{Z}$ is the set of integers. A grid value of precision $p$ is a complex number whose real and imaginary parts are integer multiples of $2^{-p}$, so it has the form $2^{-p}(a+ib)$ with $a,b\in\mathbb{Z}$.

A grid numerator is the numerator of a [Gaussian dyadic](gaussian-dyadics.md) with denominator $2^p$: for the grid value $2^{-p}(a+ib)$, the grid numerator is the Gaussian integer $a+ib$.

For example, with $p=2$ the grid value $0.75-1.25i$ equals $2^{-2}(3-5i)$, so its grid numerator is $3-5i$. Adding grid values of precision $p$ adds their numerators. Multiplying them multiplies their numerators, giving precision $2p$; returning to precision $p$ requires truncating to the grid, the one approximation.

<cite data-source="paper">A p-bit grid array has real and imaginary coefficient parts in 2−p Z.</cite> So an array of grid values is stored as its array of grid numerators.

In the paper's polynomial multiplication the numerators stay small, where $r$ is the record length. <cite data-source="paper">each resulting Gaussian integer coefficient Hj is a sum of exactly r signed products of Gaussian integer input coefficients of modulus at most 2p</cite>. Dividing this sum by $2^p r$ and truncating toward zero gives the returned numerator. <cite data-source="paper">Each returned component numerator has magnitude at most 2p</cite>, so each fits in a signed word of fixed width.
