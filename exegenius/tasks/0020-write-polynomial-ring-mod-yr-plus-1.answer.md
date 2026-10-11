Here $y$ is the polynomial variable, an indeterminate (a symbol with no numeric value) whose powers act as roots of unity. Here $r$ is the record length, the number of complex coefficients in a polynomial record, which is a power of two.

The polynomial ring modulo $y^r + 1$ is the ring of polynomials with complex coefficients in which $y^r$ is identified with $-1$, so that $y$ has order $2r$ and wrap-around flips a sign. The argument stores one coordinate of its array in this ring, and the [convolution over this ring](polynomial-ring-convolution.md) is the next step built on that storage.

Write $R_r$ for this ring, where $R_r = \mathbb{C}[y]/(y^r+1)$, the polynomials over $\mathbb{C}$ with two polynomials identified when they differ by a multiple of $y^r+1$.

In the argument, one coordinate of the array is stored <cite data-source="paper">as the coefficient list of a polynomial modulo y r + 1, with r a power of two</cite>. Each element of $R_r$ is a polynomial $z$ with complex coefficients, and a polynomial of any degree is reduced by replacing each power $y^m$ with $m \ge r$ by $-y^{m-r}$. So every element has a unique representative $z = \sum_{k=0}^{r-1} z_k y^k$ of degree less than $r$, where $z_k$ is the $k$-th coefficient of $z$ for $0 \le k < r$, and the list $(z_0, \dots, z_{r-1})$ is the coefficient list of $z$. <cite data-source="paper">We always use representatives of degree less than r.</cite> Addition is coefficientwise.

A root of unity is a number $\omega$ with $\omega^m = 1$ for some positive integer $m$, and the order of $\omega$ is the least such $m$. Since $y^r = -1$, we get $y^{2r} = (-1)^2 = 1$. No smaller positive power of $y$ equals $1$: for $0 < k < r$, $y^k$ is a representative of degree less than $r$ other than $1$, and for $r \le k < 2r$, $y^k = -y^{k-r}$, which is not $1$. So $y$ has order $2r$.

Take $r = 4$. Then $y^4 = -1$, and $z = 1 + 2y$ has coefficient list $(1, 2, 0, 0)$. Multiplying by $y^3$ gives $z\,y^3 = y^3 + 2y^4 = y^3 - 2$, with coefficient list $(-2, 0, 0, 1)$. The coefficient $1$ at position $0$ moves to position $3$, and the coefficient $2$ at position $1$ would move to position $4$, which wraps to position $0$ with its sign reversed.

Here $s$ is the shift amount, the number of positions by which the coefficient list moves, with $0 \le s < r$. Multiplying by $y^s$ therefore moves the coefficient $z_k$ to position $k+s$ when $k+s<r$, and otherwise to position $k+s-r$ with its sign reversed. Powers of $y$ serve as roots of unity here, and <cite data-source="paper">multiplication by such a root is a signed shift of the</cite> coefficient list.

The reason for this representation is that the transforms need roots of unity, and powers of $y$ supply them: $y^k$ for $0 \le k < 2r$ are roots of unity of order dividing $2r$. Multiplying a record by one of them moves coefficients and changes some signs, so it costs data movement rather than complex multiplications. The ring is also called the negacyclic polynomial ring, since its wrap-around reverses sign where a cyclic wrap-around would not.

This ring gives the arithmetic for the [synthetic polynomial transforms](synthetic-transforms.md), whose roots of unity are powers of $y$.
