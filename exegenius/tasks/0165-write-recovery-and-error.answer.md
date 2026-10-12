Exact coefficient recovery is the step that turns the computed convolution back into the exact integer coefficients it approximates, so that the product can be carried into binary without error.

Let $\nu$ be the index of a coefficient of the convolution. Write $c_\nu$ for the true integer coefficient at index $\nu$, and $\hat c_\nu$ for the value the machine computes for it. The transforms are carried out with finitely many bits, so $\hat c_\nu$ is only approximately an integer.

Recovery is applied to the output of the [Convolution over the polynomial ring](polynomial-ring-convolution.md), after the known normalizations and digit scales are removed. Recovery undoes the [phase twist](phase-twist.md) before the coefficients are read, which restores the original cyclic wrap-around. Exact recovery is secured by the [Guard-width bound](guard-width-bound.md), which fixes enough extra bits that a single final truncation, discarding those bits, suffices.

The error analysis <cite data-source="paper">proves that the recovered coefficient error is strictly below 1/2</cite>, so $|\hat c_\nu - c_\nu| < 1/2$ for every $\nu$. Without such a bound, a computed value could lie across a half-integer and round to the wrong coefficient.

Given that bound, the nearest integer to $\hat c_\nu$ is $c_\nu$, so rounding recovers the coefficient exactly. For example, if $c_\nu = 7$ and $\hat c_\nu = 6.8$, the error is $0.2 < 1/2$ and rounding gives $7$.
