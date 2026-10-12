# Prime axes and prime-length transforms

The digit sequence must be placed where a cyclic convolution can be computed with transforms of convenient length. The [Chinese-remainder address map](../chinese-remainder-address-map.md "A rearrangement that places a digit sequence on a product of distinct prime cyclic axes while preserving convolution, implemented with address interchanges.") places it on distinct prime cyclic axes using address interchanges. [Gaussian resampling](../gaussian-resampling.md "An identity that expresses a Fourier transform of length given by a prime as a multidimensional transform with power-of-two axis lengths, with the source and target permutations kept in the identity.") then rewrites a prime-length transform as a multidimensional transform with power-of-two axes, and [Bluestein's chirp identity](../bluestein-chirp.md "The identity that converts a Fourier transform into a cyclic convolution by multiplying by chirp factors before and after it.") turns the middle transform into a normalized cyclic convolution.

## Pages

1. [Chinese-remainder address map](../chinese-remainder-address-map.md "A rearrangement that places a digit sequence on a product of distinct prime cyclic axes while preserving convolution, implemented with address interchanges.") — A rearrangement that places a digit sequence on a product of distinct prime cyclic axes while preserving convolution, implemented with address interchanges.
2. [Gaussian resampling](../gaussian-resampling.md "An identity that expresses a Fourier transform of length given by a prime as a multidimensional transform with power-of-two axis lengths, with the source and target permutations kept in the identity.") — An identity that expresses a Fourier transform of length given by a prime as a multidimensional transform with power-of-two axis lengths, with the source and target permutations kept in the identity.
3. [Bluestein's chirp identity](../bluestein-chirp.md "The identity that converts a Fourier transform into a cyclic convolution by multiplying by chirp factors before and after it.") — The identity that converts a Fourier transform into a cyclic convolution by multiplying by chirp factors before and after it.

## Map

Arrows point from a page to the pages that build on it.

```mermaid
flowchart LR
  n0["Chinese-remainder address map"]
  click n0 href "../chinese-remainder-address-map/" "A rearrangement that places a digit sequence on a product of distinct prime cyclic axes while preserving convolution, implemented with address interchanges."
  n1["Gaussian resampling"]
  click n1 href "../gaussian-resampling/" "An identity that expresses a Fourier transform of length given by a prime as a multidimensional transform with power-of-two axis lengths, with the source and target permutations kept in the identity."
  n2["Bluestein's chirp identity"]
  click n2 href "../bluestein-chirp/" "The identity that converts a Fourier transform into a cyclic convolution by multiplying by chirp factors before and after it."
  n0 --> n1
  n1 --> n2
```
