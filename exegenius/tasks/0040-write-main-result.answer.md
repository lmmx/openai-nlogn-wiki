Power-saving integer multiplication is the main result: for $n$, the number of bits in each input, and $\kappa=2^{-182}$, the exponent saved from the power of $\lg n$, a fixed Turing machine multiplies two $n$-bit integers exactly in time $O(n(\lg n)^{1-\kappa})$, which is $o(n\log n)$, so it refutes the [Schönhage–Strassen optimality conjecture](conjecture.md) in this model.

The machine is one deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, and is correct for every $n\ge1$ <cite data-source="paper">There is one deterministic Turing machine $A$, with a fixed finite</cite>. This disproves the conjecture of Schönhage and Strassen in this model <cite data-source="paper">disproves the $n\log n$ optimality conjecture</cite>.

The saving is strictly positive, however small. Since $(\lg n)^{1-\kappa}=\lg n/(\lg n)^{\kappa}$ and $(\lg n)^{\kappa}\to\infty$ for any fixed $\kappa>0$, the ratio of the running time to $n\lg n$ tends to $0$.

## Why the usual route stalls

Scanning $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$. Beating that needs cheaper address movement and cheaper butterfly arithmetic <cite data-source="paper">We therefore need savings in both movement and arithmetic.</cite>

## How the saving is built

1. Two tape primitives, the interchange of address chunks and the simultaneous butterfly layer, are built from fixed finite linear networks. Each costs the data volume times a power below one of its width, by [Recursive power saving](rank-recurrence.md).
2. These speed up the synthetic transforms over the ring $\mathbb C[y]/(y^r+1)$ ([Tape layout for synthetic transforms](transform-layout.md)) and the ring convolution built on them ([Convolution from the retained transform layout](ring-convolution.md)).
3. Gaussian resampling and Bluestein chirps turn the prime-length transforms needed for the integer product into these power-of-two transforms, with the coordinate permutations cancelled rather than sorted ([Retained permutation cancellation](retained-permutations.md)).
4. The exact $2n$-bit product follows from radix digits, the Chinese-remainder address map, two forward transforms, a pointwise product, the opposite transform, rescaling, rounding and carry propagation, with total error below $1/2$, as set out in [The multiplication algorithm](multiplication-algorithm.md).

## Totaling the cost

Let $p$ be the number of bits of precision of each stored coefficient, of order $\lg n$, and $V=\Theta(n)$ the volume of stored data. Dividing every cost by $V$, the dominant terms are powers of $p$ below one, and the smallest margin below one is $2^{-181}=2\kappa$ <cite data-source="paper">Thus $\min_i g_i=2^{-181}=2\kappa$.</cite> This slack also covers any fixed power of $\log p$, so the total time is bounded by $O(n(\lg n)^{1-\kappa})$, as [Cost accounting and the exponent κ](cost-accounting.md) shows.
