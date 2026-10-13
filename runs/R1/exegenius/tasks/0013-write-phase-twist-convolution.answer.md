A last-coordinate phase twist is a coefficientwise rescaling that makes the last cyclic axis of a convolution behave like a polynomial product modulo $y^r+1$. The twist is applied after [Bluestein's chirp identity](bluestein-chirp.md) has turned the middle transform into a cyclic convolution, and it lets the remaining axes be convolved over a polynomial ring.

Let $k$ be the index of a coefficient on the last axis, $0\le k<r$. Let $x$ be the formal variable of the cyclic ring $\mathbb C[x]/(x^r-1)$, where exponents wrap modulo $r$. Let $\zeta=e^{\pi i/r}$ be the complex number with $\zeta^r=-1$. The twist is the ring map $x\mapsto \zeta y$, where $y$ is the variable of the polynomial ring $\mathbb C[y]/(y^r+1)$. The twist turns the last cyclic coordinate into the [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md).

The map is well defined, because $(\zeta y)^r=(-1)(-1)=1$. On coefficients it multiplies coefficient $k$ by $\zeta^k$, a nonzero number, so it is invertible, and untwisting multiplies coefficient $k$ by $\zeta^{-k}$.

The twist changes how wraparound is signed. Write $k+l=j+hr$ with $0\le l<r$, $0\le j<r$ and $h\in\{0,1\}$, where $l$ indexes a coefficient of the second factor, $j$ is the cyclic index of the product and $h$ records whether the exponent wrapped. In the polynomial ring $y^{j+hr}=(-1)^h y^j$, since $y^r=-1$. The twist gives the term the factor $\zeta^{k+l}=\zeta^j(\zeta^r)^h=(-1)^h\zeta^j$. The two signs cancel, so the term carries $\zeta^j$, and untwisting by $\zeta^{-j}$ leaves the cyclic term with coefficient one.

For example, take $r=2$, so $\zeta=i$. The cyclic product $x\cdot x=x^2=1$. After the twist, $(iy)(iy)=-y^2=1$ modulo $y^2+1$. Untwisting the constant coefficient by $\zeta^0=1$ returns $1$, as required.

The twist converts the cyclic wrap of [Convolution](convolution.md) into a negative wrap, so the polynomial product on the remaining axes is a convolution over the ring, not a cyclic one.
