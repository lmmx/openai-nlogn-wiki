A *cyclic shift* rotates the values stored in a block of positions, and a *controlled* cyclic shift takes its amount of rotation from control bits stored elsewhere. The paper uses controlled shifts to change the coordinates of its arrays in linear tape time, and [packed selected-bit addition](packed-bit-addition.md) is built from them.

A controlled cyclic shift rotates the values of a target [address field](address-field.md) whose offset is set by control bits that lie before it.

Let $L$ be the number of positions in the block. Let $t$ be a position in the block, numbered $0$ to $L-1$, and let $v_t$ be the value stored at position $t$. Let $s$ be the offset, an integer taken modulo $L$. The shift by $s$ moves the value at position $t$ to position $(t+s) \bmod L$, so a value that passes the last position re-enters at the first. For $L=4$ and $s=1$, the block $(v_0,v_1,v_2,v_3)$ becomes $(v_3,v_0,v_1,v_2)$.

Let $V$ be the number of bits held in the array. Lemma 4 of the paper gives a cost linear in $V$: <cite data-source="paper">costs O(V ) if the offset can be prepared in bO(1) time from the fixed number of control values.</cite> Here "cheap" means the offset can be prepared in time polynomial in the number of digits of its control values.

The paper's method splits each block at position $L-s$; in the example the pieces are $(v_0,v_1,v_2)$ and $(v_3)$. A prefix is one setting of the fields before the target. <cite data-source="paper">two pieces to two tapes, doing so successively for all prefix fibers.</cite> <cite data-source="paper">In the merge read the second piece</cite> and then the first piece. Reading $(v_3)$ and then $(v_0,v_1,v_2)$ gives $(v_3,v_0,v_1,v_2)$.

The method is used because <cite data-source="paper">Lemma 4 updates a later field using earlier fields in linear time.</cite> The paper's [integer multiplication below n log n](main-theorem.md) algorithm changes its coordinate order with <cite data-source="paper">make the change of order a sequence of controlled cyclic shifts</cite>. Each such shift is of this kind: <cite data-source="paper">Each triangular update is a prefix-controlled cyclic shift.</cite>

In [packed selected-bit addition](packed-bit-addition.md), the updates are shifts of whole chunk ranges: <cite data-source="paper">The construction in Lemma 4 cyclically shifts the complete range of a target</cite> chunk.
