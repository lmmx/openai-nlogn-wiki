The opposite transform $F_q^+$ is the sign-reversed form of the [Discrete Fourier transform](discrete-fourier-transform.md). It maps products in the [frequency domain](frequency-domain.md) back to coefficients. It is applied to the result of a [pointwise product](pointwise-product.md) of forward transforms. It is therefore the final step of a convolution.

For a vector $u$ of $q$ complex numbers, indexed by $j$ and $\ell$ from $0$ to $q-1$, the opposite transform is
$$(F_q^+ u)_\ell = \frac{1}{q}\sum_{j=0}^{q-1} \omega^{-j\ell}\, u_j, \qquad \omega = e^{-2\pi i/q}.$$
The forward transform $F_q$ uses $\omega^{j\ell}$ in place of $\omega^{-j\ell}$, with the same factor $1/q$. So the opposite transform reverses the sign in the exponent, which the source states as <cite data-source="paper">conjugation changes the negative Fourier sign to the positive one</cite>.

The factor $1/q$ is a normalization. Let $\|u\|$ be the largest modulus of the coordinates of $u$, the norm of $u$. <cite data-source="paper">each output averages inputs multiplied by complex numbers of modulus one</cite>. Each $\omega^{-j\ell}$ has modulus one, so $|(F_q^+ u)_\ell| \le \frac{1}{q}\sum_{j} |u_j| \le \|u\|$. The transform therefore does not enlarge the norm of its input.

The two transforms undo each other up to the factor $q$:
$$(F_q^+ F_q u)_\ell = \frac{1}{q^2}\sum_{m=0}^{q-1} u_m \sum_{j=0}^{q-1} \omega^{j(m-\ell)}.$$
The inner sum is a geometric series with ratio $z = \omega^{m-\ell}$. If $m = \ell$, then $z = 1$ and the sum is $q$. If $m \ne \ell$, then $z \ne 1$ but $z^q = 1$, so the sum is $(z^q-1)/(z-1) = 0$. Hence $(F_q^+ F_q u)_\ell = u_\ell/q$ for every $u$.

For $q = 4$, $F_4$ is the forward transform of length $4$, with $\omega = -i$. For $u = (1,0,0,0)$, $v = F_4 u = (\tfrac14, \tfrac14, \tfrac14, \tfrac14)$. Then $(F_4^+ v)_\ell = \frac{1}{16}\sum_{j=0}^{3} i^{j\ell}$, which is $\tfrac14$ for $\ell = 0$ and $0$ for $\ell = 1, 2, 3$. So $F_4^+ F_4 u = u/4$.

The synthetic transforms of the paper use the same convention, with polynomial entries. Here $f$ and $g$ are two disk-grid ring arrays, and $M$ is the number of pointwise polynomial products, not the record count of earlier pages. <cite data-source="paper">Two normalized synthetic forwards, pointwise polynomial multiplication divided by r, and the normalized opposite transform give</cite> $(f*g)/(rM^2)$.

The product must also keep its frequency order, since <cite data-source="paper">the opposite transform consumes that order.</cite>
