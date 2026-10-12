Address-field interchange is a tape procedure, a procedure carried out on the tapes of a Turing machine, that swaps two disjoint, contiguous address fields of an array. The main result uses it to make the transform layers cheap, so its cost matters.

An address field is a block of consecutive address bits. Let the array have stored volume $V$, the number of bits it stores. Each address field has $u$ bits, the width of the field. <cite data-source="paper">The first procedure interchanges two disjoint contiguous address fields of u bits in an array</cite> The procedure runs on a [Fixed-tape machine model](fixed-tape-model.md).

The exponent $\tau$ is a fixed constant with $\tau<1$. Its cost is $O(V u^{\tau})$, so it grows more slowly than $u$ itself.

The procedure is built from a fixed [Linear networks and frames](linear-network-frames.md) network that exchanges two banks of values. The network has scratch wires that hold temporary values, and it restores them. The final permutation is exact for arbitrary initial scratch values. <cite data-source="paper">The final permutation is exact for arbitrary initial auxiliary values</cite>

The network is applied recursively to streams holding a fraction of the volume. Each recursive level costs a strictly smaller power, because the network's edge ranks sum to less than its number of wires. <cite data-source="paper">Because the sum of these ranks is less than the number of wires</cite>

For example, with $u=2$ and addresses written as pairs of 2-bit fields, the entry at address $(01,10)$ moves to address $(10,01)$, and every other entry moves by the same swap.
