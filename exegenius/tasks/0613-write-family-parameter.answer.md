A family parameter is the integer that picks out one member of a family of constructions and fixes how large that member is. The proof chooses the parameters so that every term in the [cost table](cost-table.md) is $O(n(\lg n)^{1-\kappa})$ for the fixed constant $\kappa$, which gives the bound of [Integer multiplication below n log n](main-theorem.md).

Let $\theta$ be a nonnegative integer, the family parameter, and let $C_\theta$ be the member of the family built with parameter $\theta$. A family is one such construction for each allowed value of $\theta$. Each member takes exactly $2^\theta$ input entries, so each increase of $\theta$ by one doubles the size.

A family parameter sets the sizes of the calls of the [Rank-saving recursion](rank-saving-recursion.md). That recursion splits each call into smaller calls, each on a stream of a fixed fraction of the volume, and bounds their count in terms of those sizes. So the sizes of all members must be controlled by one index.

For example, let $C_\theta$ be the cyclic convolution of an input sequence of $2^\theta$ entries with a fixed sequence of length $2^\theta$. Then $\theta = 3$ gives a member with $8$ input entries, and $\theta = 4$ gives one with $16$.

To use the family for an input of length $n \ge 1$, take $\theta = \lceil \log_2 n \rceil$, the least integer that is at least $\log_2 n$. Then $\theta \ge \log_2 n$, so $2^\theta \ge n$. Also $\theta < \log_2 n + 1$, so $2^\theta < 2n$. Hence $C_\theta$ takes between $n$ and $2n$ input entries. The input, padded with zeros to $2^\theta$ entries, fills $C_\theta$, and the padding is fewer than $n$ entries.
