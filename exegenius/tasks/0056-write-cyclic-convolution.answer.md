Cyclic convolution is the product of two equal-length sequences in which indices are taken modulo that length, so each output coefficient is a sum of products over residues. It is also called normalized cyclic convolution. Bluestein's chirp identity, which rewrites a Fourier transform as a cyclic convolution with chirp factors before and after it, turns the paper's middle transform into this operation <cite data-source="paper">converts the middle transform, including its target permutation, into normalized cyclic convolution</cite>.

Let $a = (a_0, \ldots, a_{r-1})$ and $b = (b_0, \ldots, b_{r-1})$ be complex sequences, where $r$ is the number of complex coefficients in each. Their cyclic convolution, written $c = a \circledast b$, is the length-$r$ sequence with coefficients

$$c_k = \sum_{j=0}^{r-1} a_j \, b_{(k-j) \bmod r}, \qquad k = 0, \ldots, r-1,$$

where $k$ indexes the output and $j$ the terms of each sum. The index $(k-j) \bmod r$ is the residue of $k-j$ in $\{0, \ldots, r-1\}$, so an index that leaves that range wraps to the other end.

For example, take $r = 3$, $a = (1, 2, 0)$ and $b = (0, 1, 1)$. Then

$$c_0 = a_0 b_0 + a_1 b_2 + a_2 b_1 = 2, \quad c_1 = a_0 b_1 + a_1 b_0 + a_2 b_2 = 1, \quad c_2 = a_0 b_2 + a_1 b_1 + a_2 b_0 = 3,$$

so $c = (2, 1, 3)$.

The wrap-around is exact. Let $x$ be a formal variable, an indeterminate not evaluated at any number, and write $a(x) = \sum_j a_j x^j$ and $b(x) = \sum_j b_j x^j$. In the example, $a(x)\,b(x) = x + 3x^2 + 2x^3$; replacing $x^3$ by $1$ gives $2 + x + 3x^2$, whose coefficients are exactly $c$.

In general, reducing modulo $x^r - 1$ replaces $x^r$ by $1$, so each term $a_j b_l x^{j+l}$ becomes $x^{(j+l) \bmod r}$, where $l$, the index of a term of $b$, runs over $\{0, \ldots, r-1\}$. The coefficient of $x^k$ in the reduced product is therefore the sum of $a_j b_l$ over pairs with $j + l \equiv k \pmod r$. For each $j$, exactly one $l$ qualifies, namely $l = (k-j) \bmod r$, so this sum is $c_k$. Folding merges terms of equal residue and drops none, so the reduced product is exactly $c$.
