# Radix-digit convolution

!!! info "Before this page"

    Radix-digit convolution *reduces* [Exact integer multiplication](exact-integer-multiplication.md "Radix-digit convolution rewrites an integer product as a polynomial product: it reduces exact integer multiplication to a convolution of short digit vectors."). Assumed known: Polynomials.

!!! abstract "Where this fits"

    - Relied on to show: The retained source permutation cancels: $RF_s^{+}R(F_su\cdot F_sv)=(u\ast v)/S^2$ with $S=\prod_i s_i$. ([Cyclic convolution](cyclic-convolution.md "The product of two sequences in which indices wrap around modulo the sequence length."))

Radix-digit convolution rewrites an integer product as a polynomial product: it reduces [exact integer multiplication](exact-integer-multiplication.md "Given binary strings x and y of length n, output the 2n-bit binary representation of their product.") to a convolution of short digit vectors.

Fix a radix $B \ge 2$, the base in which the inputs are written. Let $x$ and $y$ be the two integers to multiply, and let $d$ be the number of radix-$B$ digits of each input, so $x=\sum_{i=0}^{d-1}x_iB^i$ and $y=\sum_{j=0}^{d-1}y_jB^j$, where $x_i$ and $y_j$ are the digits. Let $u=(x_0,\dots,x_{d-1})$ and $v=(y_0,\dots,y_{d-1})$ be the digit vectors.

Multiplying the two expansions gives
$$xy=\sum_{m=0}^{2d-2}\Big(\sum_{i+j=m}u_iv_j\Big)B^m.$$
The inner sum, written $(u\ast v)_m$, is the convolution of $u$ and $v$ at index $m$. Each entry is a sum of at most $d$ products of digits, so the entries are small. Evaluating the list $u\ast v$ at $B$ gives $xy$, and carrying its entries yields the radix-$B$ digits of the product.

For example, with $B=10$, $x=12$ and $y=13$, the digit vectors are $u=(2,1)$ and $v=(3,1)$, their convolution is $u\ast v=(6,5,1)$, and $6+5\cdot 10+1\cdot 10^2=156=12\cdot 13$.

The point of the rewriting is that convolution becomes entrywise multiplication after a [discrete Fourier transform](discrete-fourier-transform.md "The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q."), so the method works with the short convolution instead of the full integers. The source takes this as its starting point.<cite class="exegenius-ref" data-source="paper" data-locator="§11 A consequence for matrix transposition, p. 3" data-quote="Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients" title="Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients"> (see §11 A consequence for matrix transposition, p. 3)</cite>.

## Connections

```mermaid
flowchart LR
  n0["Exact integer multiplication"]
  click n0 href "../exact-integer-multiplication/" "Given binary strings x and y of length n, output the 2n-bit binary representation of their product."
  n1["Radix-digit convolution"]
  class n1 current
  n2["Gaussian resampling"]
  click n2 href "../gaussian-resampling/" "A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies."
  n0 --> n1
  n1 --> n2
  classDef current stroke-width:3px,font-weight:bold
```

Used by:

- [Gaussian resampling](gaussian-resampling.md "Gaussian resampling is applied to a radix-digit convolution: it replaces the Fourier transforms needed for that convolution by transforms whose axis lengths are powers of two.") *is applied to* Radix-digit convolution

??? quote "From the sources"

    > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients
    >
    > — Integer multiplication below n log n (OpenAI, 2026)
