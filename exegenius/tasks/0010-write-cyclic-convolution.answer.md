A cyclic convolution is the product of two sequences of equal length in which indices are taken modulo that length, so each output coefficient is a sum of products over residues. It is also called normalized cyclic convolution. The paper's middle transform becomes this operation under Bluestein's chirp identity, so the argument needs its definition and a reason the wrap-around is not an error.

Let $a = (a_0, \ldots, a_{r-1})$ and $b = (b_0, \ldots, b_{r-1})$ be sequences of complex numbers, where $r$ is the number of complex coefficients in each sequence. Their cyclic convolution, written $c = a \circledast b$, is the sequence of length $r$ whose coefficients are

$$c_k = \sum_{j=0}^{r-1} a_j \, b_{(k-j) \bmod r}, \qquad k = 0, \ldots, r-1,$$

where $k$ indexes the output coefficients and $j$ the terms of each sum. The index $(k-j) \bmod r$ is the residue of $k-j$ in $\{0, \ldots, r-1\}$, so an index that leaves the range wraps back to the other end.

For example, take $r = 3$, $a = (1, 2, 0)$ and $b = (0, 1, 1)$. Then

$$c_0 = a_0 b_0 + a_1 b_2 + a_2 b_1 = 2, \quad c_1 = a_0 b_1 + a_1 b_0 + a_2 b_2 = 1, \quad c_2 = a_0 b_2 + a_1 b_1 + a_2 b_0 = 3,$$

so $c = (2, 1, 3)$.

The wrap-around is exact. Write $a(x) = \sum_j a_j x^j$ and $b(x)$ likewise, where $x$ is a formal variable, an indeterminate that is not evaluated at any number. In the example, $a(x) b(x) = x + 3x^2 + 2x^3$. Replacing $x^3$ by $1$, which is reducing modulo $x^3 - 1$, gives $2 + x + 3x^2$, whose coefficients are exactly $c$. In general, $c$ is the coefficient list of $a(x)\,b(x)$ reduced modulo $x^r - 1$, so no information is lost.
