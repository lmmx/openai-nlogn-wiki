# Source and target permutations

A transform of a sequence sends the entry at each input index to a new index in its output, and the output is naturally in a permuted order. The target permutation is the reordering of output coordinates that a transform needs in order to put its results in the required positions.

The paper keeps this reordering symbolically inside the transform identity. The [transform identity](transform-identity.md) expresses each [Gaussian resampling](gaussian-resampling.md) transform through a power-of-two tensor transform together with source and target coordinate permutations. Keeping the target permutation as part of the identity means it does not have to be executed as a separate full sort of the data.

For a small example, a permutation of four outputs might send output position $0, 1, 2, 3$ to positions $0, 2, 1, 3$. Applying it by sorting would rewrite all four entries, while keeping it as part of the transform identity records the swap of the middle two positions and lets it cancel later.

In the paper, the target permutation of the middle transform is included in the [Bluestein chirp identity](bluestein-chirp-identity.md) step. The source permutation is the one that cancels across the two forward transforms, their pointwise product, and the opposite-sign transform.

## Prerequisites

- [Gaussian resampling](gaussian-resampling.md)

## Used by

- [Bluestein chirp identity](bluestein-chirp-identity.md)

## Sources

> Section 8 retains the source and target coordinate permutations in the transform identity
>
> — Integer multiplication below n log n (OpenAI, 2026)
