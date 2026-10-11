A grid numerator is the integer pair that stores a numerical value exactly on a fixed grid of precision $p$. The error analysis and the carry propagation that follow both work with these integers, so the arithmetic can be exact while the only approximation sits in the choice of grid.

For a positive integer $p$, a grid value of precision $p$ is a complex number whose real and imaginary parts are integer multiples of $2^{-p}$. So it has the form $2^{-p}(a+ib)$ with $a,b\in\mathbb{Z}$. A grid numerator is the numerator of a [Gaussian dyadic](gaussian-dyadics.md) with denominator $2^p$: for the grid value $2^{-p}(a+ib)$, the grid numerator is the Gaussian integer $a+ib$, the integer multiplier of the fixed power $2^{-p}$.

<cite data-source="paper">A p-bit grid array has real and imaginary coefficient parts in 2−p Z.</cite> Thus a grid array is an array whose entries are grid values of one precision, and its entries are stored as their numerators.

For example, with $p=2$ the grid value $0.75-1.25i$ equals $2^{-2}(3-5i)$, so its grid numerator is $3-5i$. Adding two grid values of the same precision adds their numerators, so sums of grid values are computed exactly with integer arithmetic.

In the multiplication algorithm the numerators of returned coefficients are small enough to store in fixed-width words: <cite data-source="paper">Each returned component numerator has magnitude at most 2p</cite>, so each numerator is written as a signed word of fixed width.
