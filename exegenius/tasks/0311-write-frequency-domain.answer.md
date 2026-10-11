The frequency domain of a sequence is defined through the [discrete Fourier transform](discrete-fourier-transform.md): it is the list of values that the transform assigns to the sequence. On the way to the target, the paper uses this representation in two places: <cite data-source="paper">expresses each source Fourier transform through a power-of-two tensor transform</cite> in [Gaussian resampling](gaussian-resampling.md), and [Bluestein's chirp identity](bluestein-chirp-identity.md) <cite data-source="paper">converts the middle transform, including its target permutation,</cite> <cite data-source="paper">into normalized cyclic convolution.</cite>

Let $f = (f_0, f_1, \ldots, f_{q-1})$ be a sequence of $q$ complex numbers, where $q$ is the transform length as on the discrete Fourier transform page. The index $\ell$, running over $0, 1, \ldots, q-1$, names a frequency. Its frequency entry is $(F_q f)_\ell$, and the frequency domain of $f$ is the list of all $q$ entries $(F_q f)_0, \ldots, (F_q f)_{q-1}$. The list determines $f$: the opposite transform $F_q^+$, which has the positive sign in its exponent, satisfies $F_q^+ F_q f = f/q$, so $f = q\, F_q^+(F_q f)$.

The reason for this representation is that it turns convolution into pointwise multiplication, meaning entry-by-entry multiplication of two lists indexed by the same $\ell$. For sequences $f$ and $g$ of length $q$, the cyclic convolution $f \ast g$ has entries $(f\ast g)_k = \sum_{i+j \equiv k \ (\mathrm{mod}\ q)} f_i g_j$, and

$$
(F_q(f \ast g))_\ell = q\,(F_q f)_\ell\,(F_q g)_\ell .
$$

To see this, write $\omega = e^{-2\pi i/q}$ and expand: $\sum_k (f\ast g)_k\,\omega^{k\ell} = \sum_{i,j} f_i g_j\,\omega^{(i+j)\ell} = \left(\sum_i f_i\,\omega^{i\ell}\right)\left(\sum_j g_j\,\omega^{j\ell}\right)$. Each sum on the right is $q$ times a frequency entry, so the right side is $q^2 (F_q f)_\ell (F_q g)_\ell$. The left side of the identity carries one factor $1/q$, which leaves one factor $q$.

Worked example. Take $q = 4$, $f = (1,1,0,0)$ and $g = (1,2,0,0)$. Their cyclic convolution is $f \ast g = (1,3,2,0)$, since the products $f_i g_j$ with $i+j \equiv k$ give $1$ at $k=0$, $1+2=3$ at $k=1$, $2$ at $k=2$, and $0$ at $k=3$. With $\omega = -i$,

$$
F_4 f = \left(\tfrac{1}{2},\ \tfrac{1-i}{4},\ 0,\ \tfrac{1+i}{4}\right), \qquad F_4 g = \left(\tfrac{3}{4},\ \tfrac{1-2i}{4},\ -\tfrac{1}{4},\ \tfrac{1+2i}{4}\right).
$$

Multiplying entry by entry and by $q = 4$ gives $\left(\tfrac{3}{2},\ \tfrac{-1-3i}{4},\ 0,\ \tfrac{-1+3i}{4}\right)$. Applying $F_4$ directly to $(1,3,2,0)$ gives the same list, for instance $\tfrac14(1+3(-i)+2(-1)) = \tfrac{-1-3i}{4}$ at $\ell = 1$.

The paper also fixes where each frequency entry is stored. <cite data-source="paper">We also specify where each frequency entry is stored</cite>, because the opposite transform must read the entries in the same order that the forward transform wrote them. For a power-of-two length, the stored order is the bit-reversed order: the entry of frequency $\ell$ goes to the slot whose address is $\ell$ with its binary digits reversed. <cite data-source="paper">Bt denote this record permutation: it moves the entry at j to reva (j).</cite> The recursion does not move whole frequency indices: <cite data-source="paper">it does not move whole frequency indices.</cite> Because the same permutation is applied to both operands, <cite data-source="paper">We may therefore multiply the forward outputs in their retained order</cite>, and the product can be passed to the opposite transform without a reordering step.
