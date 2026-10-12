Exact coefficient recovery is the step that turns the computed convolution back into the exact integer coefficients it approximates, so that the product can be carried into binary without error.

Here $k$ is the index of a coefficient of the convolution. Write $c_k$ for the true integer coefficient at index $k$, and $\hat c_k$ for the value the machine computes for it. The transforms are carried out with finitely many bits, so $\hat c_k$ is only approximately an integer.

Recovery is applied to the output of the [Convolution over the polynomial ring](polynomial-ring-convolution.md), after the known normalizations and digit scales are removed. Recovery undoes the [phase twist](phase-twist.md) before the coefficients are read, which restores the original cyclic wrap. Exact recovery is secured by the [Guard-width bound](guard-width-bound.md), which fixes enough extra bits that a single final truncation, discarding those bits, suffices.

The error analysis <cite data-source="paper">proves that the recovered coefficient error is strictly below 1/2</cite>, so $|\hat c_k - c_k| < 1/2$ for every $k$. This is the claim the step establishes. Without a bound below $1/2$, a computed value could lie across a half-integer and round to the wrong coefficient.

Given that bound, the nearest integer to $\hat c_k$ is $c_k$, so rounding recovers the coefficient exactly. For example, if $c_k = 7$ and $\hat c_k = 6.8$, the error is $0.2 < 1/2$ and rounding gives $7$.
