A root of unity is a complex number for which some positive power equals one. The paper's fast multiplication uses such roots, and the pages on Gaussian resampling, polynomial rings, synthetic transforms and phase twists build on this one.

Let $z$ denote a complex number. A transform of the kind this paper uses sums its inputs weighted by powers of a root, so its cost depends on how cheaply those powers can be multiplied.

For example, $i^2 = -1$ gives $i^4 = 1$, so $i$ is a root of unity, and $(-1)^2 = 1$ makes $-1$ one too.

For a root of unity $z$, let $q$ denote the order of $z$, the least positive integer with $z^q = 1$; it is also the number of distinct powers $z, z^2, \ldots, z^q$. For $z = i$ the powers are $i, -1, -i, 1$, so the order is $q = 4$.

A root of unity is defined in any ring with identity by the same condition $z^q = 1$, where $1$ is the identity element. Here $y$ denotes the polynomial variable of the quotient ring $\mathbb{C}[y]/(y^4+1)$, in which $y^4+1$ is zero, so $y^4 = -1$. This changes the meaning of the letter $y$ bound on the logarithm page. Two polynomials are identified in this quotient when their difference is a multiple of $y^4+1$, and every element has a representative of degree below $4$. Then $y^8 = (y^4)^2 = (-1)^2 = 1$, so $y$ is a root of unity.

In the paper, powers of $y$ serve <cite data-source="paper">as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the</cite> coefficient list. For example, the list $(1,2,3,4)$ of $1+2y+3y^2+4y^3$ becomes $(-3,-4,1,2)$ after multiplying by $y^2$, since $y^2(1+2y+3y^2+4y^3) = -3-4y+y^2+2y^3$.

Let $a$ denote any integer exponent. <cite data-source="paper">Multiplication by y a , for any integer a, permutes</cite> the coefficients and changes some signs, so multiplying by $y^a$ moves each coefficient to a new position, with a sign change where needed.

In $\mathbb{C}$, the sum $1 + z + \cdots + z^{q-1}$ over the powers of a root $z \ne 1$ of order $q$ equals $(z^q-1)/(z-1) = 0$, which divides by $z-1$. The quotient ring has zero divisors, meaning nonzero elements whose product is zero: $(y^2-i)(y^2+i) = y^4+1 = 0$, yet neither factor is zero. A polynomial of degree below $4$ is zero in the quotient only if it is the zero polynomial, since every nonzero multiple of $y^4+1$ has degree at least $4$; both factors have degree $2$. The paper avoids division: <cite data-source="paper">The ring has zero divisors, so we verify character cancellation</cite> directly, and the cancellation appears as <cite data-source="paper">Lemma 15 (Synthetic character cancellation)</cite>.
