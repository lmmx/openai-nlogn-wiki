The norm of an array is the largest modulus among its entries, so it measures the size of the worst entry. It is the size measure in which the [convolution over the polynomial ring](polynomial-ring-convolution.md) and the error bound of [exact coefficient recovery](recovery-and-error.md) are stated.

Let $X$ be a finite array of complex values. Let $w$ range over the entries of $X$, each a complex number. The modulus of $w$ is its distance from $0$ in the complex plane: $|w| = \sqrt{\operatorname{Re}(w)^2 + \operatorname{Im}(w)^2}$. The norm of $X$, written $\|X\|$, is the largest modulus $|w|$ over all entries $w$ of $X$.

For example, let $X$ have the three entries $0.6+0.8i$, $-0.3$ and $0.5i$. Their moduli are $\sqrt{0.36+0.64}=1$, $0.3$ and $0.5$, so $\|X\|=1$. Replacing $-0.3$ by $1.2$ gives norm $1.2$, which is larger than one.

An array has norm at most one exactly when every entry has modulus at most one, that is, lies in the closed unit disk of the complex plane. The source calls such arrays disk arrays, and a disk array <cite data-source="paper">has norm at most one.</cite>

Because one bound on the norm controls every entry at once, the norm is a convenient quantity to track through a chain of operations on arrays.

The norm is extended to arrays over the [polynomial ring modulo $y^r + 1$](polynomial-ring-mod-yr-plus-1.md), where it is the maximum over all coefficients in all entries. <cite data-source="paper">the same notation denotes the maximum over all coefficients in all entries.</cite>
