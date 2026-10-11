The telescoping identity says that a sum of differences of consecutive terms of a sequence equals the last term minus the first. The paper uses it to add up the dimension changes along each wire of a network and keep only the endpoints, the source and sink dimensions. The [Exact coefficient recovery](recovery-and-error.md) bound and the cost table both depend on this collapse.

A sequence is an ordered list of real or complex numbers. Let $o$ be the index of the last term, so the sequence has $o+1$ terms. The index $k$ is the position of a term, running from $0$ to $o$. The term $\iota_k$ is the number at position $k$, so the sequence is $\iota_0,\iota_1,\dots,\iota_o$. For a list $x$ of numbers, $x_k$ is the entry at position $k$. The sum $\sum_{k=s}^{e} x_k$ stands for $x_s+x_{s+1}+\dots+x_e$, where $s$ is the first position and $e$ the last, and it is $0$ when $e<s$.

For every such sequence,
$$\sum_{k=0}^{o-1}\left(\iota_{k+1}-\iota_k\right)=\iota_o-\iota_0.$$

To prove it, split the sum into two sums and shift the index of the first one:
$$\sum_{k=0}^{o-1}\iota_{k+1}-\sum_{k=0}^{o-1}\iota_k=\sum_{k=1}^{o}\iota_k-\sum_{k=0}^{o-1}\iota_k.$$
Each term $\iota_k$ with $1\le k\le o-1$ appears once in each sum, with opposite signs, so it cancels. What remains is $\iota_o$ from the first sum and $-\iota_0$ from the second, which gives $\iota_o-\iota_0$. When $o=0$ both sides are $0$.

For example, take $\iota_k=k^2$ and $o=4$. The differences $\iota_{k+1}-\iota_k$ for $k=0,1,2,3$ are $1-0$, $4-1$, $9-4$ and $16-9$, that is $1,3,5,7$. Their sum is $16=\iota_4-\iota_0$.

In a network, a wire runs from a source vertex, through gate vertices where wires are combined, to a sink vertex. Applied to a wire, the list $\iota_0,\dots,\iota_o$ is the dimension of the wire at its source, then at each gate it passes, and finally at its sink. At a gate, a wire has one incoming and one outgoing incidence with the same label, so the two changes there cancel. Only the source and sink dimensions remain. The paper states this as <cite data-source="paper">The signed sum of dimension changes telescopes at every gate</cite>. Summing over all wires gives the sum of sink dimensions minus the sum of source dimensions, which is what the paper needs.
