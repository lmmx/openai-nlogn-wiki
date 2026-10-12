A phase twist is a coefficientwise multiplication by roots of unity that turns the wrap-around of one cyclic axis into a sign change, so that a cyclic convolution along that axis can be computed in a polynomial ring.

The phase twist follows [Bluestein's chirp identity](bluestein-chirp-identity.md), which has already turned the middle transform into a normalized cyclic convolution. A phase twist is based on the [polynomial ring modulo $y^r+1$](polynomial-ring-mod-yr-plus-1.md), into which it maps that axis. Without the twist, the ring product would negate every wrapped term, which the cyclic product does not do.

Let $a$ and $b$ be length-$r$ sequences with cyclic product $c_k=\sum_{i+j\equiv k \pmod r} a_i b_j$. Let $\theta$, a primitive $2r$-th root of unity, be the twist root. The twisted input of $a$ is $A(y)=\sum_j \theta^j a_j y^j$. The twisted input of $b$ is $B(y)=\sum_j \theta^j b_j y^j$.

Since $y^r=-1$, a term with $i+j\ge r$ becomes $-y^{i+j-r}$. Fix an output index $k$ with $0\le k<r$. The pairs with $i+j\equiv k \pmod r$ have either $i+j=k$ or $i+j=k+r$. The first kind contributes $\theta^k a_i b_j y^k$. The second kind contributes $\theta^{k+r}a_i b_j y^{k+r}=\theta^k a_i b_j y^k$, because $\theta^r=-1$ and $y^r=-1$. So the coefficient of $y^k$ in $A(y)B(y)$ is $\theta^k c_k$, and multiplying by $\theta^{-k}$ recovers $c_k$. <cite data-source="paper">its negative wrap gives precisely the original cyclic wrap after the twist is removed</cite>.

For $r=2$ and $\theta=\sqrt{-1}$, let $A(y)=a_0+\theta a_1 y$ and $B(y)=b_0+\theta b_1 y$. Their product is $a_0b_0+\theta(a_0b_1+a_1b_0)y+\theta^2a_1b_1y^2$. With $y^2=-1$ and $\theta^2=-1$, this is $(a_0b_0+a_1b_1)+\theta(a_0b_1+a_1b_0)y$, so the two coefficients are $c_0$ and $\theta c_1$.
