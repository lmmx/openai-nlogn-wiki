The transform identity is the equation that the paper uses to rewrite each source Fourier transform. After [Gaussian resampling](gaussian-resampling.md), a source transform is expressed through a power-of-two tensor transform, in which the axis lengths are powers of two, together with coordinate permutations that move entries to the right positions.

In the paper's notation, the coordinate permutations appear on the two sides of the tensor transform. The algorithm uses the identity as an equation, so it never performs the two coordinate maps as separate passes over the data.

The identity is what makes the rest of the construction possible. The power-of-two axes are the ones on which the [synthetic transform](synthetic-transform.md) and the simultaneous butterfly layers act, and the coordinate maps are the source and target permutations described on the [target permutation](target-permutation.md) page.

Its use in the algorithm is a bookkeeping step. The paper's [multiplication algorithm](multiplication-algorithm.md) applies the identity to the three transforms, and the source permutation cancels across them, so the net effect is the convolution with no permutation left over.
