The negacyclic polynomial ring is the ring of polynomials with complex coefficients in which a wrap-around past the top degree returns with a minus sign, so every product reduces to a polynomial of lower degree. It is the coefficient setting of the transforms in this argument, and the [Phase twist](phase-twist.md) page turns a cyclic wrap into this sign-flipped wrap.

Here $y$ is the indeterminate of the polynomial ring, whose powers act as roots of unity. Here $r$ is the number of complex coefficients in a polynomial record, a power of two. The ring is written $\mathbb{C}[y]/(y^r+1)$: polynomials in $y$ in which $y^r$ is identified with $-1$. The ring is the coefficient ring of the [Synthetic polynomial transforms](synthetic-transforms.md), whose roots of unity are powers of $y$.

An element is stored as its record $(\alpha_0, \alpha_1, \dots, \alpha_{r-1})$ of $r$ coefficients, standing for $\alpha_0 + \alpha_1 y + \dots + \alpha_{r-1} y^{r-1}$. Here $\alpha_i$ is the coefficient of $y^i$ in the record.

Here $\ell$ is a non-negative integer exponent, so $y^\ell$ is a power of $y$. For $r \le \ell < 2r$, we have $y^\ell = -y^{\ell-r}$, because $y^r=-1$.

For example, with $r = 4$, the record $(\alpha_0, \alpha_1, \alpha_2, \alpha_3)$ stands for $\alpha_0 + \alpha_1 y + \alpha_2 y^2 + \alpha_3 y^3$. Multiplying by $y$ gives $y \cdot \alpha_3 y^3 = \alpha_3 y^4 = -\alpha_3$, so the record becomes $(-\alpha_3, \alpha_0, \alpha_1, \alpha_2)$.

Multiplying by $y$ therefore shifts the coefficients one place and negates the one that wraps around. Since $y^r = -1$, we get $y^{2r} = (-1)^2 = 1$, so $y$ has order $2r$. An ordinary cyclic wrap would return the wrapped coefficient unchanged. Multiplying by any power $y^\ell$ is a signed shift of the record, which is what the transforms rely on <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>.
