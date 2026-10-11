An address is the label that locates one entry of an array, written as a string of bits. Later procedures move entries by rewriting their addresses, so an address has to say exactly which position an entry occupies.

An array is a finite collection of entries stored in a fixed order. Let $N$ be the number of entries in the array, counting every stored entry once. The entries sit at positions $0, 1, \dots, N-1$ in that order.

Let $d$ be the address length, the number of bits in each address. An address is a string $\alpha$ of $d$ bits, and it labels one entry of the array. The entry labelled by $\alpha$ is the one at position $\mathrm{val}(\alpha)$, counting from $0$, where $\mathrm{val}$ is the value of a binary string. The array is held in an ordered stream of its entries. <cite data-source="paper">An address is implicit in an entry’s position in this ordered stream; it is not stored beside every data bit.</cite> So the address bits are never written next to the data.

An address is sized by the [Base-2 logarithm](base-two-logarithm.md): an array of $N \ge 2$ entries needs addresses of $d=\lg N$ bits. There are $2^d$ strings of length $d$, so $N$ distinct addresses of length $d$ are available exactly when $2^d \ge N$. For $N \ge 2$, the least such $d$ is $\lg N$, because $\lg N$ is the least integer $k$ with $2^k \ge N$. When $N=2^d$, the $2^d$ strings of length $d$ are exactly the addresses of the array.

For example, take $d=3$, so $N=8$. The address $\alpha=101$ has $\mathrm{val}(\alpha)=1\cdot 4+0\cdot 2+1\cdot 1=5$, so it labels the entry at position 5. The eight addresses $000, 001, \dots, 111$ label positions $0$ through $7$ in order.
