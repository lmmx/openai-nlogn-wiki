# Cyclic convolution

!!! info "Before this page"

    Assumed known: Polynomials.

!!! abstract "Where this fits"

    1. With both coordinate permutations kept in the formula, $P_sF_s = 2^{2\alpha^2}B_0P_tF_tA$, and the retained source permutation cancels across a convolution, so no sort is executed. — how: keep the permutations in the Gaussian resampling identity, then cancel the source permutation through the convolution ([Transform identity with retained permutations](transform-identity.md "The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts."))
    2. **This page:** The retained source permutation cancels: $RF_s^{+}R(F_su\cdot F_sv)=(u\ast v)/S^2$ with $S=\prod_i s_i$.

??? note "Symbols from earlier pages"

    - $F_s$ — source transform: The normalized Fourier transform of length s. (on [Gaussian resampling](gaussian-resampling.md "A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies."))
    - $I$ — identity map: The identity map, which leaves every vector unchanged. (on [Gaussian resampling](gaussian-resampling.md "A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies."))
    - $P_s$ — source permutation: The coordinate permutation on vectors of length s, sending g to the vector with entries g_{ti}. (on [Gaussian resampling](gaussian-resampling.md "A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies."))

Cyclic convolution is the product of two sequences in which indices wrap around modulo the sequence length, and it is the operation the permutation step below works with.

For vectors $u$ and $v$ of length $s$, index the entries by $i,j,m \in \mathbb{Z}/s\mathbb{Z}$, that is, by $0,\dots,s-1$ with sums taken modulo $s$. Here $u$ and $v$ are any vectors, not necessarily digit vectors. The cyclic convolution of $u$ and $v$, written $u\ast v$, has entries

$$(u\ast v)_m=\sum_{i+j\equiv m \pmod s} u_i v_j .$$

Cyclic convolution is the wrap-around form of the [convolution of digit vectors](radix-digit-convolution.md "Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients."), in which an index $i+j \ge s$ is reduced to $i+j-s$.

For example, take $s=3$, $u=(1,2,0)$ and $v=(0,1,1)$. The ordinary convolution has entries $(0,1,3,2,0)$ at indices $0$ to $4$. The entries at indices $3$ and $4$ wrap onto $0$ and $1$, so $u\ast v=(2,1,3)$.

For arrays indexed by tuples $(i_1,\dots,i_d)$ with $i_k\in\mathbb{Z}/s_k\mathbb{Z}$, the wrap-around applies in each axis separately, and the source uses $\ast$ this way<cite class="exegenius-ref" data-source="paper" data-locator="§1 X 2 -hk -bk zk + (-1)b zk+t/2, p. 46" data-quote="denote cyclic convolution in the displayed axes" title="denote cyclic convolution in the displayed axes"> (see §1 X 2 -hk -bk zk + (-1)b zk+t/2, p. 46)</cite>. Let $S=s_1s_2\cdots s_d$, the number of entries of such an array (so $S=s$ when $d=1$). Here $S$ means this product, not the Gaussian map $S$ of the earlier page.

Cyclic convolution is turned into pointwise products by the [discrete Fourier transform](discrete-fourier-transform.md "The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q."), which is the normalized convolution rule:

$$F_s(u\ast v)=S\,(F_su)\cdot(F_sv),$$

where $F_s$ is the normalized Fourier transform, and $\cdot$ is the entrywise product. The inverse transform $F_s^{+}$ satisfies $F_s^{+}F_s=I/S$.

Write $R$ for the retained source permutation, the $P_s$ of the resampling identity, with inverse $R^{-1}$. The claim $RF_s^{+}R(F_su\cdot F_sv)=(u\ast v)/S^2$ follows in three steps:

- $F_s^{+}R=R^{-1}F_s^{+}$, so $RF_s^{+}R=F_s^{+}$.
- A permutation commutes with pointwise products, so $(RF_su)\cdot(RF_sv)=R(F_su\cdot F_sv)$. This moves $R$ through the product, so the two copies of $R$ can meet across the inverse transform.
- By the convolution rule and $F_s^{+}F_s=I/S$, we get $S\,F_s^{+}(F_su\cdot F_sv)=F_s^{+}F_s(u\ast v)=(u\ast v)/S$, hence $F_s^{+}(F_su\cdot F_sv)=(u\ast v)/S^2$.

The permutation $R$ disappears exactly because the inverse transform carries $R$ to $R^{-1}$, so the two copies cancel. Nothing remains to reorder the result, because permuting before or after a pointwise product gives the same output. The output is $u\ast v$ in its own order, so no sort is executed.

## Connections

```mermaid
flowchart LR
  n0["Cyclic convolution"]
  class n0 current
  n1["Transform identity with retained permutations"]
  click n1 href "../transform-identity/" "The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts."
  n0 --> n1
  classDef current stroke-width:3px,font-weight:bold
```

Used by:

- [Transform identity with retained permutations](transform-identity.md "The transform identity cancels its retained permutation across a cyclic convolution.") *cancels its retained permutation across* Cyclic convolution

??? quote "From the sources"

    > denote cyclic convolution in the displayed axes
    >
    > — Integer multiplication below n log n (OpenAI, 2026)
