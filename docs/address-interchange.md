# Address-field interchange

An address permutation moves each entry of an array from one address to another. Here the arrays are stored as streams of bits on a [multitape Turing machine](turing-machine-model.md), and an address is implicit in an entry's position in the stream. Swapping two fields of an address means exchanging the positions of two groups of address digits, while keeping every other field fixed.

The procedure in this paper handles the case where the two fields are disjoint, contiguous, and each has $u$ bits, inside an [array with a complete Cartesian address set](cartesian-address-array.md). For a fixed array of logical volume $V$ (the number of stored data bits), the procedure runs in $O(V u^{\tau})$ steps for a fixed exponent $\tau < 1$, and it works for arbitrary $u$.

The name "interchange" describes the effect. Take an address written as $(p, h, g, d, z)$ with $h$ and $d$ fields of width $u$. The procedure produces the address $(p, d, g, h, z)$, which swaps the two $u$-bit fields.

The procedure is not a simple sequence of digit moves. Its intermediate steps form pointwise XOR combinations of data: a stored value at one position can be the exclusive-or of two entries of the input. The final effect is still an exact permutation, and the result is exact for any initial contents of the auxiliary wires used as scratch space. The paper's [linear network](linear-network-frames.md) construction is what organizes these combinations so that the scratch contents are restored.

The cost exponent $\tau$ matters because the transform layout needs many such swaps. A procedure that costs $O(V u^{\tau})$ with $\tau < 1$ grows more slowly than $u$, and the saving compounds over the levels of the recursion, as explained in the [rank saving](rank-saving-recursion.md) page.

## Prerequisites

- [Multitape Turing machine](turing-machine-model.md)
- [Array with a complete Cartesian address set](cartesian-address-array.md)

## Used by

- [Multiplication algorithm](multiplication-algorithm.md)
- [Recursive rank saving](rank-saving-recursion.md)

## Sources

> interchanges two disjoint contiguous address fields of u bits in an array
>
> — Integer multiplication below n log n (OpenAI, 2026)
