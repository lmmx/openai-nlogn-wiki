The norm of an array is the largest modulus among its entries, so it measures the size of the worst entry. It is the size measure in which the [convolution over the polynomial ring](polynomial-ring-convolution.md) and the error bound of [exact coefficient recovery](recovery-and-error.md) are stated.

The norm is defined on each finite [array](array.md) of complex values. Let $X$ be such an array, and let $u$ range over its entries. The modulus of $u$ is its distance from $0$ in the complex plane: $|u| = \sqrt{\operatorname{Re}(u)^2 + \operatorname{Im}(u)^2}$. The norm of $X$, written $\|X\|$, is the largest modulus $|u|$ over all entries $u$ of $X$.

For example, let $X$ have the entries $0.6+0.8i$, $-0.3$ and $0.5i$. Their moduli are $1$, $0.3$ and $0.5$, so $\|X\|=1$. Replacing $-0.3$ by $1.2$ gives norm $1.2$.

An array is a disk array when every entry has modulus at most one, that is, lies within distance one of $0$ in the complex plane. Since $\|X\|$ is the largest modulus, this holds exactly when $\|X\| \le 1$. The source records this as: a disk array <cite data-source="paper">has norm at most one.</cite>

The norm extends to arrays over the [polynomial ring](polynomial-ring-mod-yr-plus-1.md). Here $r$ is the number of coefficients in each representative, and the ring is $\mathbb{C}[y]/(y^r+1)$, the polynomials modulo $y^r+1$. Each element $h$ of the ring is written $h = \sum_{s=0}^{r-1} h_s y^s$, where $s$, running from $0$ to $r-1$, indexes the coefficient $h_s$. <cite data-source="paper">We always use representatives of degree less than r.</cite> The norm of $h$ is $\max_s |h_s|$. For an array over the ring, <cite data-source="paper">the same notation denotes the maximum over all coefficients in all entries.</cite>
