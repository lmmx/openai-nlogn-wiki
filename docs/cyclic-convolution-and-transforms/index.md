# Cyclic convolution and transforms

Cyclic convolution is the operation that the transform computes efficiently, since the discrete Fourier transform turns it into pointwise multiplication. [Cyclic convolution](../cyclic-convolution.md "The product of two sequences in which indices wrap around modulo the sequence length.") defines it with indices wrapping modulo the sequence length. [Discrete Fourier transform](../discrete-fourier-transform.md "The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.") defines the transform over a $q$-th root of unity, normalized by $1/q$, which the rest of the wiki uses at arbitrary length $s$ and at power-of-two lengths.

## Pages

1. [Cyclic convolution](../cyclic-convolution.md "The product of two sequences in which indices wrap around modulo the sequence length.") — The product of two sequences in which indices wrap around modulo the sequence length.
2. [Discrete Fourier transform](../discrete-fourier-transform.md "The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.") — The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.

## Map

Arrows point from a page to the pages that build on it.

```mermaid
flowchart LR
  n0["Cyclic convolution"]
  click n0 href "../cyclic-convolution/" "The product of two sequences in which indices wrap around modulo the sequence length."
  n1["Discrete Fourier transform"]
  click n1 href "../discrete-fourier-transform/" "The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q."
  n0 --> n1
```
