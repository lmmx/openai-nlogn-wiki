The negacyclic polynomial ring is the ring of polynomials with complex coefficients in which a wrap-around past the top degree returns with a minus sign, so every product reduces to a polynomial of lower degree. It is the coefficient setting of the transforms in this argument, and the [Phase twist](phase-twist.md) page turns a cyclic wrap into this sign-flipped wrap.

Here $y$ is the indeterminate of the polynomial ring, whose powers act as roots of unity. Here $r$ is the number of complex coefficients in a polynomial record, a power of two. The ring is written $\mathbb{C}[y]/(y^r+1)$: polynomials in $y$ in which $y^r$ is identified with $-1$. It is the coefficient ring of the [Synthetic polynomial transforms](synthetic-transforms.md), whose roots of unity are powers of $y$.

An element is stored as its record $(a_0, a_1, \dots, a_{r-1})$ of $r$ coefficients, standing for $a_0 + a_1 y + \dots + a_{r-1} y^{r-1}$. Here $p$ is the non-negative integer exponent of a power $y^p$. For $r \le p < 2r$, we have $y^p = -y^{p-r}$, because $y^r=-1$.

For example, with $r = 4$, the record $(a_0, a_1, a_2, a_3)$ stands for $a_0 + a_1 y + a_2 y^2 + a_3 y^3$. Multiplying by $y$ gives $y \cdot a_3 y^3 = a_3 y^4 = -a_3$, so the record becomes $(-a_3, a_0, a_1, a_2)$.

Multiplying by $y$ therefore shifts the coefficients one place and negates the one that wraps around. Since $y^r = -1$, we get $y^{2r} = 1$, so $y$ has order $2r$. Multiplying by any power $y^p$ is a signed shift of the record. An ordinary cyclic wrap would return the wrapped coefficient unchanged. The transforms rely on this property. <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>.
