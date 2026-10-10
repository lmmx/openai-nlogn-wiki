The sup norm, written $\|\cdot\|_\infty$, of a finite list of complex numbers is the largest absolute value among its entries: $\|(c_0, \dots, c_{m-1})\|_\infty = \max_j |c_j|$. For a polynomial or a coefficient array, it is the sup norm of its list of coefficients.

Take $(3 + 4i, -1, 2)$ as an example. Their absolute values are $5$, $1$, and $2$, so the sup norm is $5$. Replacing a coefficient by a number of the same absolute value leaves the sup norm unchanged, while changing one coefficient to a larger value increases it.

The paper uses the sup norm to measure size, because the coefficients are what can grow beyond a fixed bound. Its bounds on the intermediate values require each coefficient to stay small, so the norm is the natural quantity to control.

The paper's exact maps preserve the sup norm of their coefficients. This matters for the [phase twist](phase-twist.md): multiplying each coefficient by a unit complex number of modulus one keeps the sup norm the same.
