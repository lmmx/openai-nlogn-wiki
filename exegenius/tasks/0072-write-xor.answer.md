Exclusive or (XOR) is the operation that combines two bits into one bit. The paper uses it as a computational step inside its address-handling procedures, where the final result is a permutation but the intermediate steps combine data with XOR.

The bitwise sum modulo 2 of two bits $a$ and $b$, written $a \oplus b$, is 1 exactly when the bits differ. It is the one-bit sum without a carry: $a \oplus b = (a + b) \bmod 2$. Its four values are

$$0 \oplus 0 = 0, \qquad 0 \oplus 1 = 1, \qquad 1 \oplus 0 = 1, \qquad 1 \oplus 1 = 0.$$

Applied to two bit strings of the same length, XOR acts bitwise: it combines the bits in each position separately, and the result has the same length. For example,

$$1011 \oplus 0110 = 1101,$$

because the positions give $1 \oplus 0 = 1$, $0 \oplus 1 = 1$, $1 \oplus 1 = 0$, and $1 \oplus 0 = 1$. Applying the same XOR twice restores the original value, since $a \oplus a = 0$ and $0 \oplus b = b$.

The paper's address-field interchange procedure uses this operation: <cite data-source="paper">its intermediate steps form pointwise XOR combinations of</cite> data. Its final effect is an exact permutation, so XOR is a tool inside the procedure and does not appear in its output. The bit network of the paper likewise <cite data-source="paper">uses only pointwise XOR gates</cite>, where a gate applied pointwise acts at each address separately on the bits stored there.
