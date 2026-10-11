Negacyclic convolution is the product of two equal-length sequences in which a term whose index runs past the end wraps back to the start with a minus sign. It is the convolution the paper needs after a phase twist: the twist puts the last cyclic coordinate into a polynomial in $y$ modulo $y^r+1$, where $r$ is the record length, and <cite data-source="paper">its negative wrap gives precisely the original cyclic wrap after the twist is removed</cite>.

Negacyclic convolution is obtained from [Cyclic convolution](cyclic-convolution.md) by changing the sign of each term that wraps. Let $a = (a_0, \dots, a_{n-1})$ and $b = (b_0, \dots, b_{n-1})$ be the two sequences. Write $\sigma = (\sigma_0,\dots,\sigma_{n-1})$ for the negacyclic convolution of $a$ and $b$, a sequence of $n$ complex numbers defined by

$$\sigma_m = \sum_{\substack{0 \le i,j < n \\ i+j=m}} a_i b_j \;-\; \sum_{\substack{0 \le i,j < n \\ i+j=m+n}} a_i b_j, \qquad 0 \le m < n.$$

Here $m$ is the output position, and $i$ and $j$ are the positions in $a$ and $b$ of a term $a_i b_j$. The first sum collects the terms that stay in range. The second collects the wrapped terms, those with $i+j \ge n$: each one lands at position $i+j-n$ and enters with the sign $-1$. Since $i+j \le 2n-2$, the condition $i+j=m+n$ with $0 \le m < n$ selects exactly these terms.

Equivalently, identify $a$ with the polynomial $\sum_{i=0}^{n-1} a_i y^i$ and $b$ with $\sum_{j=0}^{n-1} b_j y^j$. Then $\sigma$ lists the coefficients of their product in the [polynomial ring modulo $y^r+1$](polynomial-ring-mod-yr-plus-1.md) with $r = n$, where $y^n = -1$: a power $y^k$ with $n \le k \le 2n-2$ is replaced by $-y^{k-n}$. This is the same sign rule as the sum above.

Take $n = 2$, $a = (1, 2)$ and $b = (3, 4)$. Then $\sigma_0 = a_0 b_0 - a_1 b_1 = 3 - 8 = -5$ and $\sigma_1 = a_0 b_1 + a_1 b_0 = 4 + 6 = 10$. As a check, $(1+2y)(3+4y) = 3 + 10y + 8y^2$, and $y^2 = -1$ turns this into $-5 + 10y$. Cyclic convolution of the same sequences gives $(11, 10)$, because the wrapped term $8$ keeps a plus sign there.
