Cyclic convolution is the product of two sequences of the same length in which an index that runs past the end wraps around to the start. The paper needs it because its coefficient layout and its middle transform both become cyclic convolutions, which is how the multiplication algorithm of [Integer multiplication below n log n](main-theorem.md) reduces to a product it can compute.

Let $s$ be the number of entries in each sequence. Let $f = (f_0, \dots, f_{s-1})$ and $g = (g_0, \dots, g_{s-1})$ be two sequences of the same length $s$. Indices are read modulo $s$, so $g_{-1}$ means $g_{s-1}$. Here $k$ is an output position, and $j$ runs over the entries of $f$. The cyclic convolution $f \ast g$ is the sequence with entries

$$(f \ast g)_k = \sum_{j=0}^{s-1} f_j \, g_{(k-j) \bmod s}, \qquad 0 \le k < s.$$

Each product $f_j g_l$ lands at output position $(j+l) \bmod s$. A product whose index sum reaches $s$ wraps back to the start instead of extending the sequence. This differs from ordinary (linear) convolution, whose output has length $2s-1$.

Identify $f$ with the polynomial $f(x) = \sum_{j=0}^{s-1} f_j x^j$, where $x$ is a formal variable. The entries of $f \ast g$ are then the coefficients of $f(x)g(x)$ reduced modulo $x^s - 1$, because $x^s = 1$ in that quotient. This is the reason the operation is called cyclic: multiplying by $x$ rotates the entries of a sequence by one position.

Take $s = 4$, $f = (1, 2, 3, 4)$ and $g = (1, 1, 0, 0)$. The ordinary product of the two polynomials is $(1, 3, 5, 7, 4)$, which has length $5$. Reducing modulo $x^4 - 1$ sends the last entry $4$ to position $0$, so $f \ast g = (1+4, 3, 5, 7) = (5, 3, 5, 7)$. The same result follows from the formula: $(f \ast g)_0 = f_0 g_0 + f_3 g_1 = 1 + 4 = 5$.

The paper uses this operation on the product of several coordinate groups. Agarwal and Cooley's split is the model: <cite data-source="paper">Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional</cite>. The map $\Phi$ of the paper's Section 9.3 takes the cyclic convolution on one coordinate to a multidimensional one, and the paper states that <cite data-source="paper">Hence Φ is an isomorphism and preserves cyclic</cite> convolution. The paper also states that <cite data-source="paper">The factor QFt in (35) can be computed from a cyclic convolution</cite>, which is how the middle transform becomes a cyclic convolution.
