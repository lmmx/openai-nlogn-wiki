A *cyclic shift* rotates the values stored in a block of positions, and a *controlled* cyclic shift takes its amount of rotation from control bits stored elsewhere. The algorithm uses controlled cyclic shifts to change the coordinates of its arrays with linear-time tape work, and the packed selected-bit addition is built from them.

A controlled cyclic shift rotates the values of a target [address field](address-field.md) whose offset is set by control bits that lie before it.

Let $L$ be the number of positions in the block. Let $i$ be a position in the block, numbered $0$ to $L-1$. Let $k$ be the offset, an integer taken modulo $L$. The shift by $k$ moves the value at position $i$ to position $(i+k) \bmod L$, so a value that passes the last position re-enters at the first. For $L=4$ and $k=1$, the block $(a,b,c,d)$ becomes $(d,a,b,c)$.

The offset is computed from the control bits before the rotation starts, and the rotation then acts only on the target block.

Let $V$ be the stored bit volume, the number of bits held in the array. On a multitape machine, the shift takes time linear in $V$ when the offset is cheap to compute, as Lemma 4 states: <cite data-source="paper">costs O(V ) if the offset can be prepared in bO(1) time from the fixed number of control values.</cite>

The tape method rotates the block by swapping two consecutive pieces. Split each block at position $L-k$; in the example, the pieces are $(a,b,c)$ and $(d)$. Write the pieces to two tapes, then read the second piece before the first: <cite data-source="paper">In the merge read the second piece and then the first piece for each prefix.</cite> Reading $(d)$ and then $(a,b,c)$ gives $(d,a,b,c)$.

This is why the method is used. <cite data-source="paper">Lemma 4 updates a later field using earlier fields in linear time.</cite> The change of coordinate order in the multiplication algorithm is also a sequence of such shifts: <cite data-source="paper">make the change of order a sequence of controlled cyclic shifts</cite>. In the packed selected-bit addition on the [packed selected-bit addition](packed-bit-addition.md) page, the updates are shifts of whole chunk ranges: <cite data-source="paper">The construction in Lemma 4 cyclically shifts the complete range of a target</cite> chunk.
