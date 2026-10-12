# Discrete Fourier transform

!!! info "Before this page"

    Assumed known: Complex numbers.

!!! abstract "Where this fits"

    - Relied on to show: The one-dimensional Gaussian resampling identity $P_sF_s = 2^{2\alpha^2}B_0P_tF_tA$ holds with contractions $A$ and $B_0$. ([Gaussian resampling](gaussian-resampling.md "A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies."))
    - Relied on to show: The retained source permutation cancels: $RF_s^{+}R(F_su\cdot F_sv)=(u\ast v)/S^2$ with $S=\prod_i s_i$. ([Cyclic convolution](cyclic-convolution.md "The product of two sequences in which indices wrap around modulo the sequence length."))

The discrete Fourier transform, also called the normalized Fourier transform, is the linear map that sends a list of complex numbers to another list of the same length. It is the transform the paper implements for convolution<cite class="exegenius-ref" data-source="paper" data-locator="§11 A consequence for matrix transposition, p. 38" data-quote="We now implement the normalized Fourier transforms needed for convolution" title="We now implement the normalized Fourier transforms needed for convolution"> (see §11 A consequence for matrix transposition, p. 38)</cite>. Each output entry is a sum of all the input entries weighted by powers of a root of unity, scaled by a normalizing factor.

Let $q$ be the number of entries in the vector. Let $\omega$ be a primitive $q$-th root of unity, so $\omega^q = 1$ and the powers $\omega^0, \omega^1, \dots, \omega^{q-1}$ are distinct.

Let $j$ and $k$ be indices running from $0$ to $q-1$, where $j$ runs over input positions and $k$ over output positions.

Let $a = (a_0, a_1, \dots, a_{q-1})$ be the input vector, where $a_j$ is the entry at position $j$. Its transform $\hat a = (\hat a_0, \dots, \hat a_{q-1})$ has $q$ entries, where $\hat a_k$ is the output at position $k$. Here $k$ no longer denotes the padded width of earlier pages. The transform is

$$\hat a_k = \frac{1}{q} \sum_{j=0}^{q-1} \omega^{jk} a_j, \qquad k = 0, 1, \dots, q-1.$$

Each output is a linear combination of all the inputs, so the transform is a linear map with a $q \times q$ matrix whose $(k, j)$ entry is $\omega^{jk}/q$. The factor $1/q$ is the normalization; without it the map differs from this one by the factor $q$.

For example, take $q = 2$. Then $\omega = -1$ is a primitive square root of unity, and $\hat a_0 = (a_0 + a_1)/2$ and $\hat a_1 = (a_0 - a_1)/2$. For $a = (3, 1)$ this gives $\hat a = (2, 1)$.

## Connections

```mermaid
flowchart LR
  n0["Discrete Fourier transform"]
  class n0 current
  n1["Gaussian resampling"]
  click n1 href "../gaussian-resampling/" "A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies."
  n0 --> n1
  classDef current stroke-width:3px,font-weight:bold
```

Used by:

- [Gaussian resampling](gaussian-resampling.md "Gaussian resampling is a technique that replaces a Discrete Fourier transform of arbitrary length by transforms whose axis lengths are powers of two.") *replaces* Discrete Fourier transform

??? quote "From the sources"

    > We now implement the normalized Fourier transforms needed for convolution
    >
    > — Integer multiplication below n log n (OpenAI, 2026)
