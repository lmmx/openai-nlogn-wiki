# Middle transform

The middle transform is the central factor in the paper's factorization of a source Fourier transform. Each source transform is written as three factors applied in sequence: a Gaussian resampling map on the input side, a middle transform, and a Gaussian resampling map on the output side, with chirp factors and diagonal phases between them.

The middle transform is a discrete Fourier transform on a grid whose length is not a power of two. It is the factor that cannot be evaluated directly on the power-of-two axes, so the algorithm must convert it. The [Bluestein chirp identity](bluestein-chirp-identity.md) does this, by rewriting the middle transform as a convolution with a chirp.

The paper evaluates the middle factor with the complex convolution that it builds from the synthetic transforms, after the chirp identity has turned it into a convolution. Its target permutation is kept in the transform identity, as described on the [target permutation](target-permutation.md) page.

The middle transform is therefore the piece of the [discrete Fourier transform](discrete-fourier-transform.md) that the rest of the construction must handle. The [Gaussian resampling](gaussian-resampling.md) step is what puts it into a form on which the chirp identity can be used.

## Prerequisites

- [Gaussian resampling](gaussian-resampling.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)

## Used by

- [Bluestein chirp identity](bluestein-chirp-identity.md)

## Sources

> We next use the complex convolution to evaluate the middle factor QFt in (35)
>
> — Integer multiplication below n log n (OpenAI, 2026)
