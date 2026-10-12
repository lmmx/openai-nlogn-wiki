Write $n$ for the number of bits in each input. The constant $\kappa=2^{-182}$ is a fixed positive number. Integer multiplication below $n\lg n$ is the main theorem: a single deterministic Turing machine that runs in the [fixed-tape machine model](fixed-tape-model.md) multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time.

The bound refutes the [n log n optimality conjecture](n-log-n-conjecture.md) in this model, since $n(\lg n)^{1-\kappa}$ is of strictly smaller order than $n\lg n$. The factor $(\lg n)^{-\kappa}$ is below $1$ whenever $n\ge 3$, because then $\lg n\ge 2$.

The transform layers are the obstacle. <cite data-source="paper">Scanning an array of Θ(n) stored bits at each of Θ(log n) transform levels already costs Θ(n log n).</cite> The savings must come from both movement and arithmetic, so two tape procedures are used.

Here $V$ is the stored volume, the number of stored bits in the array. Here $u$ is the width in bits of each address field. The first procedure interchanges two disjoint equal address fields of $u$ bits in an array of stored volume $V$, at cost $O(Vu^{\tau})$, where $\tau$ is a fixed exponent below $1$. <cite data-source="paper">Its cost is O(V uτ ) for a fixed τ < 1.</cite>

The second applies a [simultaneous butterfly layer](simultaneous-butterfly-layer.md) to $d$, the number of selected chunks, at cost $O(Vd^{\lambda'})$, where $\lambda'$ is a fixed exponent below $1$.

Multiplication is reduced to the [radix-digit convolution](radix-digit-convolution.md) of the two integers' digit coefficients. On the tapes, it computes its transforms on a [transform layout](transform-layout.md) that places the selected bits of each axis at a common offset. It relabels its axis positions by the [Chinese-remainder map](chinese-remainder-map.md), and its movement is organized by [rank-saving recursion](rank-saving-recursion.md). The transform identity is based on the [transform identity with retained permutations](transform-identity.md), so permutations cancel instead of being sorted. It chooses its source lengths as [prime source lengths](prime-source-lengths.md). It converts the last cyclic coordinate by a [phase twist](phase-twist.md), and its records are multiplied by [convolution over the polynomial ring](polynomial-ring-convolution.md). It adds selected bits with [packed selected-bit addition](packed-bit-addition.md).

It recovers its coefficients by [exact coefficient recovery](recovery-and-error.md), which rounds them to integers. After this, the result ends with [carry propagation](carry-propagation.md).

A compatible choice of fixed rational parameters makes every term of the cost table fit the bound, so the total cost is $O(n(\lg n)^{1-\kappa})$ for every large input.
