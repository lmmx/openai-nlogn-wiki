# Signed coefficient packing

!!! info "Before this page"

    Signed coefficient packing *is computed by* [Established O(n log n) multiplier](glossary.md#established-multiplier "The product of the two packed integers is computed by the Established O(n log n) multiplier, used as a black box."). Assumed known: Polynomials.

!!! abstract "Where this fits"

    1. A deterministic fixed-tape machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time, with $\kappa=2^{-182}$, below the $n\lg n$ conjecture in this model. — how: bound the cost of an exact multiplication whose transform layers are made cheap by two tape procedures, then fix parameters so every cost term fits ([Integer multiplication below n log n](main-theorem.md "A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model."))
    2. The exact product of two $n$-bit integers is obtained from the convolution of their radix-digit coefficients, computed by transforms on a fixed tape layout and then recovered and carried. — how: reduce the convolution by a Chinese-remainder map, Gaussian resampling, Bluestein's identity and a phase twist to a convolution over a polynomial ring, then recover coefficients and propagate carries ([Radix-digit convolution](radix-digit-convolution.md "Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients."))
    3. Convolution on the remaining axes over $\mathbb{C}[y]/(y^r+1)$ is computed by two forward synthetic transforms, a pointwise product, and an opposite transform. — how: forward synthetic transforms that keep frequency order, with polynomial products by signed packing and an established multiplier ([Convolution over the polynomial ring](polynomial-ring-convolution.md "The normalized product of two arrays of records in the polynomial ring, computed by two forward synthetic transforms, a pointwise product, and an opposite transform."))
    4. **This page:** The polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.

Signed coefficient packing is an encoding that turns the coefficients of a polynomial, some of them negative, into one integer, so that multiplying polynomials becomes multiplying integers. It is also called Kronecker substitution.<cite class="exegenius-ref" data-source="paper" data-locator="§11 A consequence for matrix transposition, p. 6" data-quote="Signed coefficient packing is a form of Kronecker substitution" title="Signed coefficient packing is a form of Kronecker substitution"> (see §11 A consequence for matrix transposition, p. 6)</cite>

Fix a block width $w$, the number of bits given to each coefficient. For a polynomial $f$ with integer coefficients, write $F = f(2^w)$ for its packed integer. A negative coefficient simply subtracts from its block.

Packing respects products. If $g$ is a second polynomial with packed integer $G = g(2^w)$ and $h = fg$, then $FG = h(2^w)$ exactly. One integer multiplication thus gives $FG$, and the coefficients of $h$ are read back from it, provided each is below $2^{w-1}$ in absolute value.

Recovery reads the blocks from the bottom as balanced digits in $[-2^{w-1}, 2^{w-1})$, carrying remainders upward. Such a digit string is unique for its value: if two had equal values, their lowest differing block would leave a difference that is a multiple of $2^w$ yet smaller than $2^w$ in absolute value, so it is zero. The coefficients of $h$ form such a string, so they are the recovered digits.

Worked example: take $f = 1-2x$, $g = 3+x$ and $w = 4$, where $x$ is the polynomial variable, not the input string. Then $F = 1-32 = -31$, $G = 3+16 = 19$, and $FG = -589$. The balanced base-16 digits of $-589$ are $3$, $-5$, $-2$, the coefficients of $fg = 3-5x-2x^2$.

The product of the two packed integers is computed by the [Established O(n log n) multiplier](glossary.md#established-multiplier "The known fixed-tape integer multiplier running in O(n log n) time, used here only as a black-box subroutine."), used as a black box.<cite class="exegenius-ref" data-source="paper" data-locator="§11 A consequence for matrix transposition, p. 6" data-quote="Calls to the established O(n log n) multiplier are ordinary subroutine calls; they do not invoke the improved theorem recursively." title="Calls to the established O(n log n) multiplier are ordinary subroutine calls; they do not invoke the improved theorem recursively."> (see §11 A consequence for matrix transposition, p. 6)</cite>

## Connections

```mermaid
flowchart LR
  n0["Established O(n log n) multiplier"]
  click n0 href "../glossary/#established-multiplier" "The known fixed-tape integer multiplier running in O(n log n) time, used here only as a black-box subroutine."
  n1["Signed coefficient packing"]
  class n1 current
  n2["Convolution over the polynomial ring"]
  click n2 href "../polynomial-ring-convolution/" "The normalized product of two arrays of records in the polynomial ring, computed by two forward synthetic transforms, a pointwise product, and an opposite transform."
  n0 --> n1
  n1 --> n2
  classDef current stroke-width:3px,font-weight:bold
```

Used by:

- [Convolution over the polynomial ring](polynomial-ring-convolution.md "Convolution over the polynomial ring computes its products with Signed coefficient packing.") *computes its products with* Signed coefficient packing

??? quote "From the sources"

    > Signed coefficient packing is a form of Kronecker substitution
    >
    > — Integer multiplication below n log n (OpenAI, 2026)
