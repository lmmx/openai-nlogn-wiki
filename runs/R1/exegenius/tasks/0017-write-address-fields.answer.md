Address fields are contiguous blocks of address bits, and they give the layout of an array on a tape. The transform calculation needs them because it works by rearranging addresses, and rearranging is not free.

An array is stored in tape order: the item at position $p$ sits in the $p$-th cell, and its address is $p$ written in binary. Write $u$ for the number of bits in one address field. Splitting the address bits into contiguous blocks of $u$ bits gives address fields. An address is then a tuple of field values, and the set of all addresses is the Cartesian product of the fields' value sets.

Example. A 4-item array has two one-bit fields, the high bit and the low bit. Address 01 has high field 0 and low field 1. Interchanging the two fields sends the item at address 01 to address 10, the item at 10 to 01, and leaves the items at 00 and 11 in place. The items are unchanged; only their cells move.

A layout's cost is counted in the [Fixed-tape machine model and stream operations](fixed-tape-model.md), where each step touches one cell per tape, so moving data is the cost to minimize. Write $V$ for the stored bit volume, the total number of bits the array holds. Write $n$ for the size of the input, so the array holds $\Theta(n)$ bits. Scanning all stored bits at each level costs $\Theta(n\log n)$ over $\Theta(\log n)$ levels <cite data-source="paper">$\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$</cite>.

The layout matters because each transform level may need a rearrangement, so the cost of a rearrangement is paid at every level.
