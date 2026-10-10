# Signed coefficient packing

Signed coefficient packing, a form of Kronecker substitution, computes a product of polynomials by multiplying two integers. It is the tool that lets an integer multiplier compute polynomial products inside the [polynomial ring modulo $y^r + 1$](polynomial-ring-mod-yr-plus-1.md).

Let $w$ be a bit spacing. Pack a polynomial $f(y) = \sum_i f_i y^i$ with small signed coefficients into the integer $F = f(2^w)$. Packing two polynomials and multiplying the integers gives $FG = (fg)(2^w)$. If the coefficients of $fg$ are small enough, the coefficients can be read back out of $FG$ as $w$-bit signed digits.

Here is a worked example with $w = 5$, so the spacing is $32$. Take $f = 3 - 2y$ and $g = 1 + 5y$. Then $F = 3 - 64 = -61$ and $G = 1 + 160 = 161$. Their product is $FG = -9821$. The product polynomial is $fg = 3 + 13y - 10y^2$, and indeed $3 + 13 \cdot 32 - 10 \cdot 32^2 = -9821$.

To decode, take the residue of $-9821$ modulo $32$ in the window $[-16, 16)$. This gives $3$. Subtract it, divide by $32$, and repeat: the digits are $3$, $13$, and $-10$, which are the coefficients of $fg$. Decoding works because every coefficient lies in the window of width $2^w$ centred at zero.

This decoding step is what the paper calls *centred extraction*: each coefficient is read as the representative in the window $[-2^{w-1}, 2^{w-1})$, so a negative coefficient is not mistaken for a large positive one. The paper lists it with signed packing, negacyclic wrapping, and copying as linear stream passes.

For the negacyclic ring, the same packing is followed by reduction modulo $y^r + 1$ using the sign rule from the ring page. The paper's Lemma 17 combines exact packing, centred extraction, and negacyclic reduction, and gives its time as $O(rp \log(rp))$, using the [established multiplier](established-multiplier.md) on the packed integers.

## Prerequisites

- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Established O(n log n) multiplier](established-multiplier.md)

## Used by

- [Multiplication algorithm](multiplication-algorithm.md)

## Sources

> Signed coefficient packing is a form of Kronecker substitution
>
> — Integer multiplication below n log n (OpenAI, 2026)
