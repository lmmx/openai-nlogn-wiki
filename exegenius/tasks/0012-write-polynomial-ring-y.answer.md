Here $y$ is the variable of the ring, whose powers serve as roots of unity in the remaining axes. $r$ is the number of coefficients in the coefficient list of one polynomial record, a power of two.

The polynomial ring modulo $y^r+1$ is the set of complex polynomials in $y$ in which $y^r$ is replaced by $-1$, so each element is stored as its list of $r$ complex coefficients, from degree $0$ up to degree $r-1$. It is where the last cyclic coordinate of the transform is stored, so that wrap-around in that coordinate becomes a sign change rather than a general multiplication.

Adding two elements adds their coefficient lists entrywise. Multiplying them takes the ordinary polynomial product and then uses $y^r=-1$ to rewrite every power of $y$ of degree $r$ or more as a negated lower power. In this ring, products are computed by a signed form of [Cyclic convolution](cyclic-convolution.md): the coefficient lists are convolved, and any term that wraps past index $r-1$ returns with a minus sign.

Take $r=4$ and the polynomial $1+2y+3y^2+4y^3$, stored as $(1,2,3,4)$. Multiplying by $y$ gives $y+2y^2+3y^3+4y^4$, and since $y^4=-1$ this equals $-4+y+2y^2+3y^3$. So $(1,2,3,4)$ becomes $(-4,1,2,3)$: each entry moves up one place, and the entry that wraps round is negated.

The step applies a phase twist to the last cyclic coordinate, which makes that coordinate a polynomial modulo $y^r+1$. Its method rests on the example: multiplying by a power of $y$ moves the coefficient list up by that many places, and each entry that wraps round comes back negated. Multiplication by a power of $y$ is therefore a signed cyclic shift <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>, so the twisted coordinate needs no general multiplication.
