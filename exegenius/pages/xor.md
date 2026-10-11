Exclusive or (XOR) is the bit operation that the paper uses to rearrange data on the way to [Integer multiplication below n log n](main-theorem.md). Each XOR can be undone by applying it again, so a sequence of XOR steps moves data around without losing any of it.

A bit is a value 0 or 1, and a bit string is a finite sequence of bits. For bits $\sigma$ and $\sigma'$, the exclusive or $\sigma \oplus \sigma'$ is their bitwise sum modulo 2, which is 1 exactly when the bits differ.

Applied to two bit strings of equal length, $\oplus$ acts pointwise, meaning separately at each position: $1011 \oplus 0110 = 1101$.

XOR is associative and commutative, and $\sigma' \oplus \sigma' = 0$, so $(\sigma \oplus \sigma') \oplus \sigma' = \sigma$. Applying the same XOR twice restores the original value. Each XOR step is therefore a bijection, a map that is one-to-one and onto, and it is its own inverse.

Three XOR steps swap two bit strings. Starting from $(1011, 0110)$:

$$(1011, 0110) \to (1101, 0110) \to (1101, 1011) \to (0110, 1011).$$

Each arrow is one XOR step: the first string is replaced by its XOR with the second, then the second by its XOR with the first, then the first again. So a sequence of XOR steps can produce a [Permutation](permutation.md) of the data, a rearrangement in which each value lands at exactly one position.

XOR is a step inside the [Address-field interchange](address-interchange.md), which swaps two disjoint fields of address bits. Although <cite data-source="paper">its final effect is an exact permutation</cite>, <cite data-source="paper">its intermediate steps form pointwise XOR combinations of</cite> data.

XOR is the only gate of the [Bit network](bit-network.md). The paper states that the bit network <cite data-source="paper">uses only pointwise XOR gates</cite>.

XOR is computed at each address by a [Gate and terminal of a network](network-gate-terminal.md), which combines the two bits stored at that address by a fixed linear map.
