An address field is a run of bits in the [Address](address.md) of an array, consecutive in position, and it is the unit that an address interchange exchanges with another field of the same width. The paper's tape multiplication depends on these interchanges to change how an array's entries are laid out on the tape: <cite data-source="paper">Fast address interchanges organize the layouts</cite>.

The paper also calls a field an address chunk or a chunk: <cite data-source="paper">We use the bit network to interchange two equal address chunks on tape</cite>. Both names mean the same run of bits.

Write $\rho$ for the field width, the number of bits in each of the two fields being interchanged. This letter has other meanings on earlier pages; here it denotes only the width. Bit positions are numbered from 1 at the most significant end, so position 1 is the leftmost bit. A field is a run of $\rho$ consecutive positions, and two fields are disjoint when they share no position.

The paper's first procedure <cite data-source="paper">interchanges two disjoint contiguous address fields of u bits in an array</cite>. It applies to arrays <cite data-source="paper">whose addresses form a complete Cartesian product</cite>, meaning that every combination of coordinate values, each coordinate ranging over all its values, occurs as an address.

An array is stored as one ordered stream, the sequence of its entries in the order of their addresses: <cite data-source="paper">stored in lexicographic order, with the first coordinate most significant</cite>. Lexicographic order is dictionary order: the first coordinate decides, and later coordinates break ties. <cite data-source="paper">An address is implicit in an entry’s position in this ordered stream</cite>, so no address is written beside each bit.

Take $\rho = 2$ and an array of 16 entries with 4-bit addresses, with the two fields at bit positions 1–2 and 3–4. The interchange sends address $0110$ to $1001$, because the field $01$ and the field $10$ trade places. So the entry stored at $0110$ moves to $1001$. Likewise the fields $00$ and $11$ of $0011$ trade places, and the entry at $0011$ moves to $1100$.

The interchange's <cite data-source="paper">final effect is an exact permutation</cite>. Each address field is moved by a [Permutation](permutation.md) of addresses. The paper defines this action: <cite data-source="paper">An address permutation f moves the entry at x to f (x).</cite>

Contiguity keeps each move local in the stream. Take the field at positions 3–4 in the example, and fix the bits before it, the prefix $01$. The four entries beginning with $01$ occupy stream positions $4$ to $7$, counting from $0$, and their last two bits take every value. So a tape head can carry out this move in one left-to-right sweep over that run. If the field were not contiguous, the entries it moves would be spread across the stream, and the head would have to jump between them.
