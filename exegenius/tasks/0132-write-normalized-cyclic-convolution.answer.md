A normalized cyclic convolution is a scaling of the [Cyclic convolution](cyclic-convolution.md) $f \ast g$ by $1/s$. Its purpose is to make a [Discrete Fourier transform](discrete-fourier-transform.md) turn convolution into a pointwise product. On the way to the target, [Bluestein's chirp identity](bluestein-chirp-identity.md) rewrites the middle transform, including its target permutation, as a normalized cyclic convolution.

For sequences $f$ and $g$ of length $s$, the entries of $f \ast g$ are
$$(f \ast g)_k = \sum_{j=0}^{s-1} f_j\, g_{(k-j) \bmod s}, \qquad 0 \le k \le s-1,$$
where $f_j$ is the entry of $f$ at position $j$, and the index $(k-j) \bmod s$ wraps around modulo $s$.

We write $f \circledast g$ for the normalized cyclic convolution of $f$ and $g$, the cyclic convolution $f \ast g$ divided by $s$.
$$f \circledast g = \frac{1}{s}\,(f \ast g).$$

Let $F_s$ be the normalized discrete Fourier transform of length $s$, which is the $F_q$ of the transform page with $q = s$. A normalized cyclic convolution is turned into pointwise products by the [Discrete Fourier transform](discrete-fourier-transform.md) $F_s$, as the rule below states. The source states the rule for the unnormalized product, writing the length as $S$: <cite data-source="paper">The normalized convolution rule is Fs (u ∗ v) = S(Fs u) · (Fs v), while Fs+ Fs = I/S.</cite>

With $S = s$, the rule says $F_s(f \ast g) = s\,(F_s f)(F_s g)$. Dividing both sides by $s$ gives the form used here:
$$F_s(f \circledast g)_k = (F_s f)_k\,(F_s g)_k, \qquad 0 \le k \le s-1.$$
That is, the transform of the normalized product is the pointwise product of the transforms of $f$ and $g$, meaning entry $k$ of one multiplied by entry $k$ of the other.

Take $s = 2$, $f = (1, 2)$ and $g = (3, 4)$. Then $(f \ast g)_0 = 1 \cdot 3 + 2 \cdot 4 = 11$ and $(f \ast g)_1 = 1 \cdot 4 + 2 \cdot 3 = 10$, so $f \circledast g = (11/2,\ 5)$. For $s = 2$ the transform is $F_2 u = \left(\frac{u_0 + u_1}{2},\ \frac{u_0 - u_1}{2}\right)$, so $F_2 f = (3/2,\ -1/2)$ and $F_2 g = (7/2,\ -1/2)$, whose entrywise product is $(21/4,\ 1/4)$. Directly, $F_2(f \circledast g) = \left(\frac{11/2 + 5}{2},\ \frac{11/2 - 5}{2}\right) = (21/4,\ 1/4)$, as the rule predicts.

This is the step the source uses. It states that <cite data-source="paper">The factor QFt in (35) can be computed from a cyclic convolution and two pointwise phase multiplications.</cite> so the transform step reduces to one cyclic convolution and two pointwise phase multiplications.
