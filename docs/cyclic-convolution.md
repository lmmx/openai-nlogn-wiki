# Cyclic convolution

!!! info "Before this page"

    Assumed known: Polynomials.

!!! abstract "Where this fits"

    - Relied on to show: The transform identity $P_s F_s = 2^{2\alpha^2} B_0 P_t F_t A$ holds with linear contractions $A$ and $B_0$, so the source permutation $P_s$ and target permutation $P_t$ stay in the formula instead of being executed as sorts. ([Transform identity with retained permutations](transform-identity.md "The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts."))

Cyclic convolution is the product of two sequences of the same length in which every index is taken modulo the length, so an index that falls off one end wraps to the other end. The paper writes it $\ast$<cite class="exegenius-ref" data-source="paper" data-locator="§1 X 2 -hk -bk zk + (-1)b zk+t/2, p. 46" data-quote="denote cyclic convolution in the displayed axes" title="denote cyclic convolution in the displayed axes"> (see §1 X 2 -hk -bk zk + (-1)b zk+t/2, p. 46)</cite>, and the transform identity below depends on it.

Let $a = (a_0, \dots, a_{q-1})$ and $b = (b_0, \dots, b_{q-1})$ be two sequences, where $q$ is the number of entries in each sequence. Their cyclic convolution is the sequence $c = a \ast b$ of the same length, with entries

$$c_o = \sum_{i=0}^{q-1} a_i \, b_{(o-i) \bmod q}, \qquad o = 0, \dots, q-1,$$

where $o$ indexes the output entries and $i$ indexes the terms of the sum; here $i$ changes meaning from its use for digit indices on earlier pages. The index $(o-i) \bmod q$ is the remainder of $o-i$ on division by $q$; this is the wrap-around.

Equivalently, $c_o$ adds up the entries of the ordinary convolution whose index is congruent to $o$ modulo $q$. The ordinary convolution sums the products of entries of $a$ and $b$ whose indices add to the same total, with no wrap-around. It has $2q-1$ entries, and the cyclic version folds the extra ones back onto the first $q$.

Example: take $q = 3$, $a = (1, 2, 0)$ and $b = (3, 0, 1)$. For $o = 0$, the wrapped indices are $(0-0) \bmod 3 = 0$, $(0-1) \bmod 3 = 2$ and $(0-2) \bmod 3 = 1$, so
$$c_0 = a_0 b_0 + a_1 b_2 + a_2 b_1 = 3 + 2 + 0 = 5.$$
The same computation gives $c_1 = 6$ and $c_2 = 1$, so $c = (5, 6, 1)$.

## Connections

```mermaid
flowchart LR
  n0["Cyclic convolution"]
  class n0 current
  n1["Discrete Fourier transform"]
  click n1 href "../discrete-fourier-transform/" "The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q."
  n0 --> n1
  classDef current stroke-width:3px,font-weight:bold
```

Used by:

- [Discrete Fourier transform](discrete-fourier-transform.md "The transform reduces cyclic convolution to a pointwise product, the entrywise product of two vectors.") *reduces* Cyclic convolution

??? quote "From the sources"

    > denote cyclic convolution in the displayed axes
    >
    > — Integer multiplication below n log n (OpenAI, 2026)
