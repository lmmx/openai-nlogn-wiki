Suppose an array has address fields arranged in a fixed order, and one of them is designated the row field. Collapse the fields before the row field into a prefix, and the fields after it into a suffix. A row is then the set of entries with a fixed prefix $p$ and a fixed row index $r$, which is the complete consecutive block of entries $\{p\} \times \{r\} \times [B]$, where $B$ is the size of the suffix.

In words, a row is the complete ordered suffix, including every active address field after the row field, at one fixed prefix and one fixed row index. Every row therefore contains $B$ entries in the same suffix order.

As a small example, take an array with addresses in $[2] \times [3] \times [2]$, and let the middle field be the row field. Then there are $2 \cdot 3 = 6$ rows, and each row holds $2$ consecutive entries. The row with prefix $0$ and row index $1$ consists of the two entries with addresses $(0, 1, 0)$ and $(0, 1, 1)$.

The [linear network](linear-network-frames.md) distributes whole rows cyclically among its roles. Keeping each row whole means that the row's internal address order is preserved on every role.
