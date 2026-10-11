The telescoping identity says that a sum of differences of consecutive terms of a sequence equals the difference of its last and first terms. The argument uses it to add up a chain of small changes, one per stage, and keep only the two endpoints; the [Exact coefficient recovery](recovery-and-error.md) bound and the [Cost table](cost-table.md) both depend on this collapse.

A sequence is an ordered list of numbers. Let $o$ be the index of the last term of a sequence of real or complex numbers, so the sequence has $o+1$ terms. The index $k$ is the position of a term, running from $0$ to $o$; the letter $k$ changes meaning here. The term $\iota_k$ is the number at position $k$, so the sequence is $\iota_0,\iota_1,\dots,\iota_o$. The sum $\sum_{k=a}^{b} x_k$ stands for $x_a+x_{a+1}+\dots+x_b$, and it is $0$ when $b<a$.

For every such sequence,
$$\sum_{k=0}^{o-1}\left(\iota_{k+1}-\iota_k\right)=\iota_o-\iota_0.$$

To prove it, split the sum into two sums and shift the index of the first one:
$$\sum_{k=0}^{o-1}\iota_{k+1}-\sum_{k=0}^{o-1}\iota_k=\sum_{k=1}^{o}\iota_k-\sum_{k=0}^{o-1}\iota_k.$$
Each term $\iota_k$ with $1\le k\le o-1$ appears once in each sum, with opposite signs, so it cancels. What remains is $\iota_o$ from the first sum and $-\iota_0$ from the second, which gives $\iota_o-\iota_0$. When $o=0$ both sides are $0$.

For example, take $\iota_k=k^2$ and $o=4$. The differences $\iota_{k+1}-\iota_k$ for $k=0,1,2,3$ are $1-0$, $4-1$, $9-4$ and $16-9$, that is $1,3,5,7$. Their sum is $16=\iota_4-\iota_0$.

The identity turns a sum over many stages into a difference of two numbers. If stage $k$ changes a quantity from $\iota_k$ to $\iota_{k+1}$, the total change over all stages is the final value minus the initial value, whatever the intermediate values are. The paper applies the same collapse to signed dimension changes: <cite data-source="paper">The signed sum of dimension changes telescopes at every gate</cite>, which leaves only the source and sink dimensions.
