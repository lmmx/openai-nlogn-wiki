The norm of an array is the largest modulus among its entries, so it measures the size of the worst entry. The [convolution over the polynomial ring](polynomial-ring-convolution.md) and the error bound of [exact coefficient recovery](recovery-and-error.md) are stated in this size measure.

Let $X$ be a finite array of complex values, and let $u$ range over its entries. The modulus of $u$ is its distance from $0$ in the complex plane: $|u| = \sqrt{\operatorname{Re}(u)^2 + \operatorname{Im}(u)^2}$. The norm of $X$, written $\|X\|$, is the largest modulus $|u|$ over all entries $u$ of $X$.

For example, let $X$ have the entries $0.6+0.8i$, $-0.3$ and $0.5i$. Their moduli are $1$, $0.3$ and $0.5$, so $\|X\|=1$. Replacing $-0.3$ by $1.2$ gives norm $1.2$.

An array is a disk array when every entry has modulus at most one, that is, lies in the closed unit disk of the complex plane. Since $\|X\|$ is the largest modulus, this holds exactly when $\|X\| \le 1$. The source states that a disk array <cite data-source="paper">has norm at most one.</cite>

The norm is extended to arrays over the [polynomial ring](polynomial-ring-mod-yr-plus-1.md). Here $y$ is the polynomial variable, $r$ is the number of coefficients in each representative, and the ring is the polynomials modulo $y^r + 1$. Each element $g$ of this ring is represented by $g = \sum_{t=0}^{r-1} g_t y^t$, where the coefficient index $t$ runs from $0$ to $r-1$. <cite data-source="paper">We always use representatives of degree less than r.</cite> The norm of $g$ is $\max_t |g_t|$. For an array over the ring, the norm is the maximum over all coefficients in all entries: <cite data-source="paper">the same notation denotes the maximum over all coefficients in all entries.</cite>
