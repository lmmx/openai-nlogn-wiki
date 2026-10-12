Carry propagation is the final step that turns the recovered integer coefficients of a convolution into the binary string of an exact product.

It is applied to the coefficients of the [Radix-digit convolution](radix-digit-convolution.md) once they are recovered.

The coefficients are integers that can be larger than the digit base, so they cannot be read off as bits. Carry propagation processes them from the least significant position upward. At each position it adds the coefficient to the carry from the previous position, writes the low bit of the sum as the next output bit, and passes the remaining high part on as the carry. Each step preserves the total, since coefficient plus carry equals bit plus twice the new carry, so the output bits spell the same integer as the coefficients.

Worked example: take base 2 and coefficients 3, 2, 1, which stand for $3 + 2\cdot 2 + 1\cdot 4 = 11$. Position 0 gives $3 = 1 + 2\cdot 1$, so bit 1 and carry 1. Position 1 gives $2 + 1 = 3 = 1 + 2\cdot 1$, so bit 1 and carry 1. Position 2 gives $1 + 1 = 2 = 0 + 2\cdot 1$, so bit 0 and carry 1. The last carry is written as the top bit. The bits from least to most significant are 1, 1, 0, 1; reversing them gives 1011, which is 11.

On the fixed-tape machine, the bits are written to a work tape in the order they are produced, and the stream is then reversed. <cite data-source="paper">Write the resulting bits from least to most significant on a work tape, then reverse that stream and output exactly 2n bits in most-significant-first order.</cite>
