Integer multiplication below $n\lg n$ is the main theorem: a single deterministic Turing machine that runs in the [fixed-tape machine model](fixed-tape-model.md) multiplies two $n$-bit integers exactly, with its logarithmic factor reduced by a fixed power. The power is $\kappa=2^{-182}$, a fixed positive number, so the time is $O(n(\lg n)^{1-\kappa})$. It refutes the [n log n optimality conjecture](n-log-n-conjecture.md) in this model.

Without its constant factor, $n(\lg n)^{1-\kappa}=n\lg n\cdot(\lg n)^{-\kappa}$ is below $n\lg n$ for every $n\ge 3$. There $\lg n>1$ (since $\lg 3\approx 1.58$), so $(\lg n)^{-\kappa}<1$. The ratio to $n\lg n$ tends to $0$, so the order is strictly smaller.

The obstacle is the transform layers, the rounds of the transform. <cite data-source="paper">Scanning an array of Θ(n) stored bits at each of Θ(log n) transform levels already costs Θ(n log n).</cite> The transform calculation consists of address rearrangements, signed shifts and butterfly operations. <cite data-source="paper">We therefore need savings in both movement and arithmetic.</cite> Two tape procedures supply them.

A field is a block of consecutive address bits. The first procedure interchanges two disjoint equal address fields of $u$ bits in an array of stored volume $V$, in time $O(Vu^{\tau})$. <cite data-source="paper">Its cost is O(V uτ ) for a fixed τ < 1.</cite>

The second applies a [simultaneous butterfly layer](simultaneous-butterfly-layer.md) to $d$ selected chunks, in time $O(Vd^{\lambda'})$.

Multiplication is reduced to the [radix-digit convolution](radix-digit-convolution.md) of the two integers' digit coefficients. It computes its transforms on a [transform layout](transform-layout.md) that places the selected bits of each axis at a common offset. It relabels its axis positions by the [Chinese-remainder map](chinese-remainder-map.md). Its movement is organized by [rank-saving recursion](rank-saving-recursion.md). The transform identity is based on the [transform identity with retained permutations](transform-identity.md), so permutations cancel instead of being sorted. It chooses its source lengths as [prime source lengths](prime-source-lengths.md). It converts the last cyclic coordinate by a [phase twist](phase-twist.md). It multiplies its records by [convolution over the polynomial ring](polynomial-ring-convolution.md). It adds selected bits with [packed selected-bit addition](packed-bit-addition.md).

It recovers its coefficients by [exact coefficient recovery](recovery-and-error.md), which rounds them to integers. The result ends with [carry propagation](carry-propagation.md).

Rational parameters are then chosen so that every term of the cost table fits the bound, and the total cost is $O(n(\lg n)^{1-\kappa})$. <cite data-source="paper">A compatible choice of rational parameters makes all terms in its cost table fit Theorem 1.</cite>
