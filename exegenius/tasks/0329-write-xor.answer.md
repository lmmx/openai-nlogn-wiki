Exclusive or (XOR) is a bit operation that the paper uses on the way to [Integer multiplication below n log n](main-theorem.md). A bit is a value 0 or 1, and a bit string is a finite sequence of bits.

For bits $\delta$ and $\epsilon$, the exclusive or $\delta \oplus \epsilon$ is their bitwise sum modulo 2, which is 1 exactly when the bits differ. It is the sum digit $(\delta + \epsilon) \bmod 2$ with the carry removed, where the carry is the bit passed to the next position, which is 1 exactly when both bits are 1. Its four values are

$$0 \oplus 0 = 0, \qquad 0 \oplus 1 = 1, \qquad 1 \oplus 0 = 1, \qquad 1 \oplus 1 = 0.$$

Applied to two bit strings of equal length, $\oplus$ acts pointwise, meaning at each position separately. For example, $1011 \oplus 0110 = 1101$.

XOR is associative and commutative, so $(\delta \oplus \epsilon) \oplus \epsilon = \delta \oplus (\epsilon \oplus \epsilon) = \delta \oplus 0 = \delta$. Applying the same XOR twice restores the original value, so each XOR step can be undone. Hence a sequence of such steps can produce a [permutation](permutation.md) of the data, which is a rearrangement of positions with each position used once.

XOR is a step inside the [address-field interchange procedure](address-interchange.md), which swaps two fields of address bits. There, <cite data-source="paper">its intermediate steps form pointwise XOR combinations of</cite> data, although <cite data-source="paper">its final effect is an exact permutation</cite>.

Pointwise XOR is the only gate of the [bit network](bit-network.md) in the paper, which <cite data-source="paper">uses only pointwise XOR gates</cite>. XOR is the operation of a [gate applied pointwise](network-gate-terminal.md), which acts at each address separately on the bits stored there.
