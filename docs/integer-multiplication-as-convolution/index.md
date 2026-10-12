# Integer multiplication as convolution

This part fixes the target problem and the first reduction. [Exact integer multiplication](../exact-integer-multiplication.md "Given binary strings x and y of length n, output the 2n-bit binary representation of their product.") is the goal, and [radix-digit convolution](../radix-digit-convolution.md "Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.") rewrites it as a product of polynomials whose coefficients are digits. The reader needs this framing to see why the later transforms must compute convolutions.

## Pages

1. [Exact integer multiplication](../exact-integer-multiplication.md "Given binary strings x and y of length n, output the 2n-bit binary representation of their product.") — Given binary strings x and y of length n, output the 2n-bit binary representation of their product.
2. [Radix-digit convolution](../radix-digit-convolution.md "Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.") — Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.

## Map

Arrows point from a page to the pages that build on it.

```mermaid
flowchart LR
  n0["Exact integer multiplication"]
  click n0 href "../exact-integer-multiplication/" "Given binary strings x and y of length n, output the 2n-bit binary representation of their product."
  n1["Radix-digit convolution"]
  click n1 href "../radix-digit-convolution/" "Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients."
  n0 --> n1
```
