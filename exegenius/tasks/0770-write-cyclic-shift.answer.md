A *cyclic shift* rotates the values stored in a block of positions, and a *controlled* cyclic shift takes its rotation from control bits stored elsewhere. It presents Lemma 4 of the paper, which changes coordinates in linear tape time, a [Running time cost](running-time-cost.md) linear in the stored bits. [Packed selected-bit addition](packed-bit-addition.md) is built from such shifts.

A controlled cyclic shift rotates the values of a target [address field](address-field.md) whose offset is set by control bits before it. A *prefix* is the set of fields before the target, and a *fiber* is the set of entries that share one prefix.

Let $J$ be the number of positions in the block. Let $\zeta$ be a position, numbered $0$ to $J-1$, and let $\xi_\zeta$ be the value stored there. Let $\upsilon$ be the offset, an integer taken modulo $J$. The shift moves the value at $\zeta$ to $(\zeta+\upsilon) \bmod J$. For $J=4$ and $\upsilon=1$, $(\xi_0,\xi_1,\xi_2,\xi_3)$ becomes $(\xi_3,\xi_0,\xi_1,\xi_2)$.

Let $V$ be the number of stored bits. <cite data-source="paper">The logical volume V is the number of stored data bits.</cite> Lemma 4 states that an update of the target <cite data-source="paper">costs O(V ) if the offset can be prepared in bO(1) time from the fixed number of control values.</cite> A controlled cyclic shift measures its cost in [Running time cost](running-time-cost.md).

The proof splits the block at $J-\upsilon=3$ into $(\xi_0,\xi_1,\xi_2)$ and $(\xi_3)$, and appends <cite data-source="paper">two pieces to two tapes, doing so successively for all prefix fibers.</cite> <cite data-source="paper">In the merge read the second piece</cite> and then the first piece. Each bit moves onto a tape and back a bounded number of times, so the cost is proportional to $V$.

The method is needed because the paper's coordinate changes are triangular, so each new coordinate depends on earlier ones. <cite data-source="paper">Lemma 4 updates a later field using earlier fields in linear time.</cite> Its coordinate powers <cite data-source="paper">make the change of order a sequence of controlled cyclic shifts</cite>, each prefix-controlled: <cite data-source="paper">Each triangular update is a prefix-controlled cyclic shift.</cite>

In [Packed selected-bit addition](packed-bit-addition.md), the updates are shifts of whole chunk ranges: <cite data-source="paper">The construction in Lemma 4 cyclically shifts the complete range of a target</cite> chunk.
