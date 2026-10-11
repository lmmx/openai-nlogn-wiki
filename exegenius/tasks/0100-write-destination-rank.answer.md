A destination rank is the position a record takes in the final order after a move, given by its rank among the records in that order. It is the key that lets displaced records return to their places in one pass over the stream.

Each destination rank is the key on which the extracted records are sorted by [Stable radix sort](stable-radix-sort.md).

Each record is stored at an address made of three chunks, named $1$, $2$ and $3$ on this page. Let $q$ be the address of a record before the move, and let $q'$ be its address after the move.

The position of the record at $q$ among the records in stream order is its rank, written $\operatorname{rank}(q)$. A counter that moves through the stream computes it: <cite data-source="paper">scan the stream with a record-rank counter</cite>.

For chunk $h \in \{1,2,3\}$, let $q_h$ and $q'_h$ be the current and destination values of chunk $h$, and let $\sigma_h$ be the record stride of chunk $h$, the amount by which the rank changes when chunk $h$ rises by one with the other chunks fixed.

The destination rank follows from the current rank by a signed sum over the chunks: <cite data-source="paper">the fixed spectator coordinates give</cite>

$$\operatorname{rank}(q') = \operatorname{rank}(q) + \sum_{h=1}^{3} (q'_h - q_h)\,\sigma_h.$$

<cite data-source="paper">The differences are signed.</cite> A chunk can therefore lower the rank as well as raise it.

For example, take strides $\sigma_1 = 1$, $\sigma_2 = 4$ and $\sigma_3 = 12$, as for chunks with 4 and 3 values. In this example the rank of $(a_1, a_2, a_3)$ is $a_1 \cdot 1 + a_2 \cdot 4 + a_3 \cdot 12$. The record at $q = (1, 2, 0)$ has rank $1 \cdot 1 + 2 \cdot 4 = 9$, and its destination is $q' = (3, 0, 1)$. The formula gives $\operatorname{rank}(q') = 9 + (3-1)\cdot 1 + (0-2)\cdot 4 + (1-0)\cdot 12 = 15$, which agrees with the direct count $3 \cdot 1 + 0 \cdot 4 + 1 \cdot 12 = 15$.

Here $M$ is the number of records in the stream, and $A_{\mathrm{rect}}$ is a bit-size bound for the integers the rectangular routine handles. <cite data-source="paper">All involved integers have O(Arect ) bits</cite>.

The algorithm attaches this destination rank, padded to $\lceil \log_2 M \rceil \le A_{\mathrm{rect}}$ bits, to each extracted record.

Each extracted record also marks its hole, the position it returns to, on a fixed track of the stream: <cite data-source="paper">mark its hole on a fixed track of the full stream</cite>. Since the move permutes the exceptional addresses, the destination ranks are distinct and are exactly the ranks of the marked holes: <cite data-source="paper">these keys are distinct and are exactly the ranks of the marked</cite>. Sorting the records by destination rank therefore puts each record into its own hole. <cite data-source="paper">One forward full-stream scan reinserts the sorted records.</cite>

The sort runs one pass per bit of the key, and <cite data-source="paper">the at most Arect radix passes</cite> bound how many passes there are, so the width of the rank sets the number of passes in the cost bound.
