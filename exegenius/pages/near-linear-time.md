Here $\Xi$ is a fixed real exponent, the power to which the logarithm factor is raised. Near-linear time is built from the [Logarithm](logarithm.md) $\lg n$: it is the class of running times $O\big(n(\lg n)^{\Xi}\big)$, where $n$ is the input length. The paper's main result reaches a bound of this form, so this page defines the target that the rest of the argument aims at.

With $\Xi = 1$ the bound is $n\lg n$, and with $\Xi = 2$ it is $n(\lg n)^2$. A power of $n$ falls outside the class. For $n^{3/2}$, the ratio $n^{3/2}/\big(n(\lg n)^{\Xi}\big) = \sqrt{n}/(\lg n)^{\Xi}$ grows without bound for every fixed $\Xi$, because a power of $n$ outgrows every power of $\lg n$.

The paper's theorem gives its machine $A$ this bound. <cite data-source="paper">Its worst-case running time satisfies</cite> $T_A(n) = O\big(n(\lg n)^{1-\kappa}\big)$ with $\kappa = 2^{-182}$, so $\Xi = 1-\kappa$ and the bound is near-linear. <cite data-source="paper">The bound is asymptotic through all input lengths.</cite>

The exponent $1-\kappa$ is below $1$, so the bound is smaller than $n\lg n$ by the ratio $(\lg n)^{-\kappa}$, which tends to $0$ as $n$ grows. This gap is what the paper's claim rests on that the algorithm <cite data-source="paper">disproves the n log n</cite> optimality conjecture. The gap is invisible at feasible sizes: the ratio equals one half only at $\lg n = 2^{2^{182}}$.
