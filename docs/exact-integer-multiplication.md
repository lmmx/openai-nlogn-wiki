# Exact integer multiplication

!!! info "Before this page"

    Assumed known: Turing machines and tapes.

!!! abstract "Where this fits"

    - Relied on to show: With both coordinate permutations kept in the formula, $P_sF_s = 2^{2\alpha^2}B_0P_tF_tA$, and the retained source permutation cancels across a convolution, so no sort is executed. ([Transform identity with retained permutations](transform-identity.md "The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts."))

Exact integer multiplication is the problem of multiplying two binary integers and returning every bit of the product, with no rounding or truncation. The target result is a faster algorithm for this problem, so this page fixes its exact input and output.

Here $n$ is the number of bits in each input. Let $x$ and $y$ be binary strings of length $n$, the two inputs.

For a binary string $x$, $\mathrm{val}(x)$ is its nonnegative integer value, with the leftmost bit most significant. Here $k$ is the number of bits of the padded representation and $z$ is an integer with $0 \le z < 2^k$. Then $\mathrm{bin}_k(z)$ is the binary representation of $z$ padded on the left with zeros to exactly $k$ bits.

On input $x\#y$, where $\#$ separates the two strings, the machine must output $\mathrm{bin}_{2n}(\mathrm{val}(x)\,\mathrm{val}(y))$. The width $2n$ suffices because each value is at most $2^n-1$, so the product is at most $(2^n-1)^2<2^{2n}$. For example, take $n=2$, $x=10$ and $y=11$. Then $\mathrm{val}(x)=2$, $\mathrm{val}(y)=3$, and the output is $\mathrm{bin}_4(6)=0110$.

Schönhage and Strassen proved in 1971 that the problem can be solved in $O(n\log n\log\log n)$ time<cite class="exegenius-ref" data-source="paper" data-locator="§11 A consequence for matrix transposition, p. 3" data-quote="two n-bit integers can be multiplied in O(n log n log log n) time on a multitape Turing machine" title="two n-bit integers can be multiplied in O(n log n log log n) time on a multitape Turing machine"> (see §11 A consequence for matrix transposition, p. 3)</cite>. Harvey and van der Hoeven later reached the unconditional $O(n\log n)$ upper bound<cite class="exegenius-ref" data-source="paper" data-locator="§11 A consequence for matrix transposition, p. 3" data-quote="unconditional O(n log n) upper bound" title="unconditional O(n log n) upper bound"> (see §11 A consequence for matrix transposition, p. 3)</cite>.

The target result improves the $O(n\log n)$ bound<cite class="exegenius-ref" data-source="paper" data-locator="§11 A consequence for matrix transposition, p. 3" data-quote="We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model" title="We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model"> (see §11 A consequence for matrix transposition, p. 3)</cite>. This model is a Turing machine with<cite class="exegenius-ref" data-source="paper" data-locator="§11 A consequence for matrix transposition, p. 3" data-quote="a fixed finite alphabet and a fixed finite number of one-dimensional tapes" title="a fixed finite alphabet and a fixed finite number of one-dimensional tapes"> (see §11 A consequence for matrix transposition, p. 3)</cite>.

## Connections

```mermaid
flowchart LR
  n0["Exact integer multiplication"]
  class n0 current
  n1["Radix-digit convolution"]
  click n1 href "../radix-digit-convolution/" "Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients."
  n0 --> n1
  classDef current stroke-width:3px,font-weight:bold
```

Used by:

- [Radix-digit convolution](radix-digit-convolution.md "Radix-digit convolution rewrites an integer product as a polynomial product: it reduces exact integer multiplication to a convolution of short digit vectors.") *reduces* Exact integer multiplication

??? quote "From the sources"

    > We consider exact multiplication
    >
    > — Integer multiplication below n log n (OpenAI, 2026)
