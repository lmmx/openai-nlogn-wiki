Cyclic convolution is the product of two sequences of the same length in which every index is taken modulo the length, so an index that falls off one end wraps to the other end. The paper uses it, written $\ast$, along the displayed axes.

Let $a = (a_0, \dots, a_{q-1})$ and $b = (b_0, \dots, b_{q-1})$ be the two sequences, where $q$ is the number of entries in each sequence. Their cyclic convolution is the sequence $c = a \ast b$ of the same length, with entries

$$c_t = \sum_{i=0}^{q-1} a_i \, b_{(t-i) \bmod q}, \qquad t = 0, \dots, q-1,$$

where $i$ indexes the terms of the sum and $t$ indexes the output entries. The index $(t-i) \bmod q$ is the remainder of $t-i$ on division by $q$; this is the wrap-around.

Equivalently, $c_t$ is the sum of the ordinary convolution entries whose index is congruent to $t$ modulo $q$. Ordinary convolution of two length-$q$ sequences has $2q-1$ entries, and the cyclic version folds the extra ones back onto the first $q$.

Example: take $q = 3$, $a = (1, 2, 0)$ and $b = (3, 0, 1)$. For $t = 0$, the wrapped indices are $(0-0) \bmod 3 = 0$, $(0-1) \bmod 3 = 2$ and $(0-2) \bmod 3 = 1$, so
$$c_0 = a_0 b_0 + a_1 b_2 + a_2 b_1 = 3 + 2 + 0 = 5.$$
The same computation gives $c_1 = 6$ and $c_2 = 1$, so $c = (5, 6, 1)$.
