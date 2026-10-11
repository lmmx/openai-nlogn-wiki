An address is a label that locates one entry of an array, written as a string of bits. Later procedures move entries by rewriting their addresses, so an address has to say exactly which position an entry occupies.

An array is a finite collection of entries stored in a fixed order. Let $N$ be the number of entries in the array, counting every stored entry once. The entries sit at positions $0, 1, \dots, N-1$ in that order.

Let $d$ be the address length, the number of bits in each address. An address is a string $\alpha$ of $d$ bits, and it labels one entry of the array. The entry labelled by $\alpha$ is the one at position $\mathrm{val}(\alpha)$, counting from $0$. An address is implicit in the entry's position in the [Stream](stream.md) that holds the array. <cite data-source="paper">An address is implicit in an entry’s position in this ordered stream; it is not stored beside every data bit.</cite> So the bits of the address are never written next to the data.

An address is sized by the [Base-2 logarithm](base-two-logarithm.md): an array of $N=2^d$ entries needs addresses of $d=\lg N$ bits, and the $2^d$ strings of length $d$ are exactly its addresses.

For example, take $d=3$, so $N=8$. The address $\alpha=101$ has $\mathrm{val}(\alpha)=1\cdot 4+0\cdot 2+1\cdot 1=5$, so it labels the entry at position 5. The eight addresses $000, 001, \dots, 111$ label positions $0$ through $7$ in order.
