A destination rank is the position a record takes in the final order after a move, given by its rank among the records in that order. It is the sort key that returns each record extracted by the correction to its hole.

Each destination rank is the key on which the extracted records are sorted by [Stable radix sort](stable-radix-sort.md).

Each record is stored at an address made of three chunks, named $1$, $2$ and $3$ on this page. Let $q$ be the address of a record before the move, and let $q'$ be its address after the move. The rank $\operatorname{rank}(q)$ is the position of the record at $q$ among the records in stream order, counted from $0$. The rank $\operatorname{rank}(q)$ is computed by a scan of the [Stream](stream.md) in order, with a counter: <cite data-source="paper">scan the stream with a record-rank counter</cite>.

Let $h \in \{1,2,3\}$ index a chunk, let $q_h$ and $q'_h$ be the values of chunk $h$ in $q$ and $q'$, and let $\sigma_h$ be the record stride of chunk $h$, the amount by which the rank changes when chunk $h$ rises by one with the other two chunks fixed. The strides are mixed-radix: the stride of a chunk is the product of the numbers of values of the chunks before it.

To go from $q$ to $q'$, change one chunk at a time. Changing chunk $h$ by $q'_h - q_h$ with the others fixed changes the rank by $(q'_h - q_h)\sigma_h$, and these changes add. <cite data-source="paper">the fixed spectator coordinates give</cite>

$$\operatorname{rank}(q') = \operatorname{rank}(q) + \sum_{h=1}^{3} (q'_h - q_h)\,\sigma_h.$$

<cite data-source="paper">The differences are signed.</cite> A chunk can therefore lower the rank as well as raise it.

For example, let chunk 1 take 4 values and chunk 2 take 3 values, so $\sigma_1 = 1$, $\sigma_2 = 4$ and $\sigma_3 = 12$. The record at $q = (1, 2, 0)$ has rank $1 + 2\cdot 4 = 9$, and its destination is $q' = (3, 0, 1)$. The formula gives $9 + (3-1)\cdot 1 + (0-2)\cdot 4 + (1-0)\cdot 12 = 15$, matching the direct count $3 + 0 + 12 = 15$.

Let $B$ be the set of exceptional addresses, the addresses whose records the correction extracts, so $|B|$ counts them. <cite data-source="paper">Since T0 S0−1 permutes B</cite>, the destinations of these records are exactly the addresses of $B$. Each extracted record marks its hole, the address it returns to, <cite data-source="paper">mark its hole on a fixed track of the full stream</cite>. Distinct addresses have distinct ranks, so the destination ranks are distinct and are exactly the ranks of the marked holes: <cite data-source="paper">these keys are distinct and are exactly the ranks of the marked</cite>.

Here $M$ is the number of records in the stream, and $A_{\mathrm{rect}}$ is a bit-size bound for the integers the rectangular routine handles. <cite data-source="paper">All involved integers have O(Arect ) bits</cite>. Each extracted record gets its destination rank as a key, <cite data-source="paper">Attach this destination rank, padded to</cite> $\lceil \log_2 M \rceil \le A_{\mathrm{rect}}$ bits.

Stable radix sort makes one pass per key bit, least significant bit first, and keeps equal keys in their earlier order. So the sort runs at most $A_{\mathrm{rect}}$ passes: <cite data-source="paper">the at most Arect radix passes</cite>. Each pass scans the $|B|$ extracted records, each with $R$ payload bits and its key, where $R$ is the number of payload bits in a record. The total cost is $O(|B|\,A_{\mathrm{rect}}(R + A_{\mathrm{rect}}))$.

The sorted keys are the hole ranks in increasing order, so the $j$-th record in sorted order goes into the $j$-th hole in stream order. <cite data-source="paper">One forward full-stream scan reinserts the sorted records.</cite>
