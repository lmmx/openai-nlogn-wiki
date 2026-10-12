Cyclic convolution is the product of two sequences of the same length in which every index is taken modulo the length, so an index that falls off one end wraps to the other end. The paper writes it $\ast$ <cite data-source="paper">denote cyclic convolution in the displayed axes</cite>, and the transform identity below depends on it.

Let $a = (a_0, \dots, a_{q-1})$ and $b = (b_0, \dots, b_{q-1})$ be two sequences, where $q$ is the number of entries in each sequence. Their cyclic convolution is the sequence $c = a \ast b$ of the same length, with entries

$$c_t = \sum_{i=0}^{q-1} a_i \, b_{(t-i) \bmod q}, \qquad t = 0, \dots, q-1,$$

where $t$ indexes the output entries and $i$ indexes the terms of the sum; here $i$ changes meaning from its use for digit indices on earlier pages. The index $(t-i) \bmod q$ is the remainder of $t-i$ on division by $q$; this is the wrap-around.

Equivalently, $c_t$ adds up the entries of the ordinary convolution whose index is congruent to $t$ modulo $q$. The ordinary convolution, which sums the products of entries of $a$ and $b$ whose indices add to the same total with no wrap-around, has $2q-1$ entries, and the cyclic version folds the extra ones back onto the first $q$.

Example: take $q = 3$, $a = (1, 2, 0)$ and $b = (3, 0, 1)$. For $t = 0$, the wrapped indices are $(0-0) \bmod 3 = 0$, $(0-1) \bmod 3 = 2$ and $(0-2) \bmod 3 = 1$, so
$$c_0 = a_0 b_0 + a_1 b_2 + a_2 b_1 = 3 + 2 + 0 = 5.$$
The same computation gives $c_1 = 6$ and $c_2 = 1$, so $c = (5, 6, 1)$.
