The polynomial ring modulo a power-of-two length is the ring in which one coordinate is stored after a phase twist, so that wrap-around becomes a sign change. The variable of the ring is $y$, an indeterminate that is not evaluated at any number. The number of complex coefficients in the list of one element is $r$, a power of two. The ring is the set of polynomials in $y$ in which $y^r$ is replaced by $-1$.

Each element is stored as its list of $r$ complex coefficients, from degree $0$ up to degree $r-1$, and adding two elements adds their lists entrywise. Multiplication in this ring computes products by a signed form of [Cyclic convolution](cyclic-convolution.md): the coefficient lists are convolved, and any term that wraps past index $r-1$ returns with a minus sign.

Take $r=4$ and $1+2y+3y^2+4y^3$, stored as $(1,2,3,4)$. Multiplying by $y$ gives $y+2y^2+3y^3+4y^4$, and since $y^4=-1$ this equals $-4+y+2y^2+3y^3$, so $(1,2,3,4)$ becomes $(-4,1,2,3)$.

Multiplying by $y$ moves each entry up one place, and the entry at degree $r-1$ wraps to degree $0$ with a minus sign, as in the example. Since $y^k=-y^{k-r}$ for $r\le k<2r$ and $y^{2r}=1$, every power of $y$ acts this way some number of times. Hence multiplication by a power of $y$ is a signed cyclic shift of the list <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>.

The step applies a phase twist. The phase twist multiplies the $j$-th entry of a coefficient list by $\theta^j$, where $\theta$ is the twist factor, a complex $2r$-th root of unity with $\theta^r=-1$. The twist is useful because it turns the wrap into a sign change, which the powers of $y$ then exhibit as signed shifts.

Cyclic convolution of length $r$ works modulo $x^r-1$, where $x$ is the formal variable and $x^r$ is replaced by $1$. Substituting $x=\theta y$ gives $(\theta y)^r-1=-(y^r+1)$, so the rule $x^r=1$ becomes $y^r=-1$. The substitution preserves sums and products and sends multiples of $x^r-1$ to multiples of $y^r+1$. So the product of two twisted lists is the twist of their cyclic convolution.
