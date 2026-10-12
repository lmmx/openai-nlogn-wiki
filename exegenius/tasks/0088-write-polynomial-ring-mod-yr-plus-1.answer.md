The negacyclic polynomial ring is the ring of polynomials with complex coefficients in which a wrap-around past the top degree comes back with a minus sign, so every product reduces to a polynomial of lower degree. The transforms in this argument use it as their coefficient setting, and the [Phase twist](phase-twist.md) page turns a cyclic wrap into this sign-flipped wrap.

Here $y$ is the indeterminate of the polynomial ring, whose powers act as roots of unity. Here $r$ is the number of complex coefficients in a polynomial record, a power of two. The ring is written $\mathbb{C}[y]/(y^r+1)$: polynomials in $y$ in which $y^r$ is identified with $-1$. It is the coefficient ring of the [Synthetic polynomial transforms](synthetic-transforms.md), whose roots of unity are powers of $y$.

An element is stored as its record of $r$ coefficients. Here $k$ is the exponent of a power $y^k$, a non-negative integer. A term $y^k$ with $r \le k < 2r$ equals $-y^{k-r}$, because $y^r=-1$.

For example, with $r = 4$, the record $(a_0, a_1, a_2, a_3)$ stands for $a_0 + a_1 y + a_2 y^2 + a_3 y^3$. Multiplying by $y$ gives $y \cdot a_3 y^3 = a_3 y^4 = -a_3$, so the record becomes $(-a_3, a_0, a_1, a_2)$.

Multiplying by $y$ therefore shifts the coefficients one place and negates the one that wraps around. Since $y^r = -1$, we get $y^{2r} = 1$, so $y$ has order $2r$. Multiplying by any power $y^k$ is a signed shift of the record: a wrapped coefficient returns with a minus sign, the negative wrap of this ring. An ordinary cyclic wrap would return it unchanged. The transforms use this property <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>.
