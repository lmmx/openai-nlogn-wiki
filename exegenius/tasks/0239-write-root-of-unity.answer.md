A root of unity is a complex number $z$ for which some positive power of $z$ equals one. The transforms in this paper sum their inputs weighted by powers of a root, so the cost of a transform depends on how cheaply those powers can be multiplied.

For example, $i^2 = -1$ gives $i^4 = 1$, so $i$ is a root of unity, and $(-1)^2 = 1$ makes $-1$ one too.

Write $m$ for the order of $z$, the least positive integer with $z^m = 1$; it is also the number of distinct powers $z, z^2, \ldots, z^m$. For $z = i$ the powers are $i, -1, -i, 1$, so the order is $m = 4$.

A root of unity is defined in any ring with identity $1$ by the same condition $z^m = 1$. Let $y$ denote the polynomial variable in $\mathbb{C}[y]/(y^4+1)$, the ring of complex polynomials in $y$ in which $y^4+1$ is treated as zero, so that $y^4 = -1$. Then $y^8 = (y^4)^2 = (-1)^2 = 1$, so $y$ is a root of unity of order at most $8$. The paper uses powers of such a $y$ as roots in its transforms: <cite data-source="paper">as roots of unity in the remaining axes</cite>, and <cite data-source="paper">multiplication by such a root is a signed shift of the</cite> coefficient list. Multiplying the coefficient list by $y^k$ moves each coefficient to a new position and changes its sign when it wraps past the end, so no complex multiplication is needed.

In $\mathbb{C}$, a root $z \ne 1$ satisfies $1 + z + \cdots + z^{m-1} = (z^m - 1)/(z - 1) = 0$. This cancellation is what makes a sum over all powers of a root vanish, and it uses division by $z - 1$. The quotient ring has zero divisors: $(y^2 - i)(y^2 + i) = y^4 + 1 = 0$, although neither factor is zero. The paper therefore does not divide: <cite data-source="paper">The ring has zero divisors, so we verify character cancellation directly</cite> instead.
