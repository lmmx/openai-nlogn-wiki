# Array with a complete Cartesian address set

An array in the paper has an address set of the form $[a_1] \times \dots \times [a_t]$, where $[a] = \{0, \dots, a-1\}$. This set is the Cartesian product of the $t$ ranges, so its elements are all tuples $(x_1, \dots, x_t)$ with $0 \le x_i < a_i$. The array is complete in the sense that every such tuple is an address.

Such an array is stored in lexicographic order, with the first coordinate most significant. Thus the entries are listed in the order of the tuples read as numbers in a mixed radix, with $x_1$ changing slowest and $x_t$ changing fastest.

For example, the address set $[2] \times [3]$ has six addresses. In lexicographic order they are $(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)$. An address is not stored beside each entry; it is implicit in the position of the entry in the stream.

Because the address set is a full product, an address permutation can be described field by field. The [address-field interchange](address-interchange.md) procedure relies on this: it swaps two fields of such an array, and its cost is measured in the volume $V$ of stored data bits.

## Used by

- [Address-field interchange](address-interchange.md)

## Sources

> is stored in lexicographic order, with the first coordinate most significant
>
> — Integer multiplication below n log n (OpenAI, 2026)
