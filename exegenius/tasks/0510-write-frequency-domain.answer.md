The frequency domain of a sequence is defined through the [discrete Fourier transform](discrete-fourier-transform.md): it is the list of values that the transform assigns to the sequence. It is the representation in which convolution becomes a product of entries. On the way to the target, the paper uses it in two places: <cite data-source="paper">expresses each source Fourier transform through a power-of-two tensor transform</cite> in [Gaussian resampling](gaussian-resampling.md), and [Bluestein's chirp identity](bluestein-chirp-identity.md) <cite data-source="paper">converts the middle transform, including its target permutation,</cite> <cite data-source="paper">into normalized cyclic convolution.</cite>

Let $f = (f_0, f_1, \ldots, f_{q-1})$ be a sequence of $q$ complex numbers, where $q$ is the transform length. Its frequency entries are $(F_q f)_\ell$ for $\ell = 0, 1, \ldots, q-1$, and its frequency domain is the list of all $q$ of them. Each entry is

$$
(F_q f)_\ell = \frac{1}{q}\sum_{s=0}^{q-1} f_s\,\omega^{s\ell}, \qquad \omega = e^{-2\pi i/q},
$$

where $s$ is the input index of the sum. The factor $\frac{1}{q}$ belongs to the transform. Without it, every identity below carries an extra factor $q$.

The frequency domain determines $f$. The opposite transform $F_q^+$ has the same form with the opposite sign, $(F_q^+ v)_\ell = \frac{1}{q}\sum_{s=0}^{q-1} v_s\,\omega^{-s\ell}$. Substituting the definition of $F_q f$, with $\zeta$ as the summation index over frequencies,

$$
(F_q^+ F_q f)_\ell = \frac{1}{q}\sum_{\zeta=0}^{q-1} (F_q f)_\zeta\,\omega^{-\zeta\ell} = \frac{1}{q^2}\sum_{s=0}^{q-1} f_s \sum_{\zeta=0}^{q-1}\omega^{(s-\ell)\zeta}.
$$

The inner sum is $q$ when $s = \ell$. If $s \ne \ell$, then $0 < |s-\ell| < q$, so $\omega^{s-\ell} \ne 1$, and the geometric sum $\sum_{\zeta}(\omega^{s-\ell})^\zeta = \frac{(\omega^{s-\ell})^q-1}{\omega^{s-\ell}-1}$ is $0$, because $(\omega^{s-\ell})^q = 1$. Only $s = \ell$ survives, so $F_q^+ F_q f = f/q$ and $f = q\,F_q^+(F_q f)$.

Let $\sigma$ and $\rho$ be the input positions and $m$ the output position, all running over $0, \ldots, q-1$. For sequences $a$ and $b$ of length $q$, the cyclic convolution $a \ast b$ has entries

$$
(a \ast b)_m = \sum_{\substack{\sigma,\rho \in \{0,\ldots,q-1\} \\ \sigma+\rho \equiv m \ (\mathrm{mod}\ q)}} a_\sigma b_\rho,
$$

Indices wrap around modulo $q$. The representation turns this into a product:

$$
(F_q(a \ast b))_\ell = q\,(F_q a)_\ell\,(F_q b)_\ell .
$$

To see this, note that $\omega^{m\ell}$ depends only on $m$ modulo $q$, since $\omega^q = 1$. Then

$$
q\,(F_q(a\ast b))_\ell = \sum_{m}(a\ast b)_m\,\omega^{m\ell} = \sum_{\sigma,\rho} a_\sigma b_\rho\,\omega^{(\sigma+\rho)\ell} = \Big(\sum_\sigma a_\sigma\,\omega^{\sigma\ell}\Big)\Big(\sum_\rho b_\rho\,\omega^{\rho\ell}\Big).
$$

Each bracket on the right is $q$ times a frequency entry, by the definition above, so the right side is $q^2 (F_q a)_\ell (F_q b)_\ell$. Dividing by $q$ gives the identity.

Worked example. Take $q = 4$, $a = (1,1,0,0)$ and $b = (1,2,0,0)$, with $\omega = -i$. The pairs with $\sigma+\rho \equiv m$ give $a \ast b = (1,3,2,0)$; for $m=1$ they are $a_0b_1$ and $a_1b_0$, so the entry is $2+1=3$. Then

$$
F_4 a = \left(\tfrac{1}{2},\ \tfrac{1-i}{4},\ 0,\ \tfrac{1+i}{4}\right), \qquad F_4 b = \left(\tfrac{3}{4},\ \tfrac{1-2i}{4},\ -\tfrac{1}{4},\ \tfrac{1+2i}{4}\right).
$$

Multiplying entry by entry and by $q = 4$ gives $\left(\tfrac{3}{2},\ \tfrac{-1-3i}{4},\ 0,\ \tfrac{-1+3i}{4}\right)$, which is $F_4(1,3,2,0)$. For instance, at $\ell = 1$, $\tfrac{1}{4}(1+3(-i)+2(-1)) = \tfrac{-1-3i}{4}$.

The paper also fixes where each frequency entry is stored. <cite data-source="paper">We also specify where each frequency entry is stored</cite>, because the opposite transform must read entries in the order the forward transform wrote them. Let $q = 2^{\xi}$, where $\xi$ is the number of binary digits of an index, and let $\mathrm{rev}(\ell)$ be the index whose $\xi$ binary digits are those of $\ell$ in reverse order. <cite data-source="paper">If reva (j) reverses the a binary digits of j, the entry (Ft− z)j occupies slot reva (j).</cite> Here $\xi$ is the paper's $a$, and $\mathrm{rev}$ is its $\mathrm{rev}_a$. Let $\Pi$ be the permutation that moves the entry of frequency $\ell$ to slot $\mathrm{rev}(\ell)$. The recursion that computes the transform writes its outputs into these slots directly; <cite data-source="paper">it does not move whole frequency indices.</cite> For $q = 4$, $\mathrm{rev}$ exchanges $1$ and $2$, so the stored $F_4 a$ is $\left(\tfrac{1}{2},\ 0,\ \tfrac{1-i}{4},\ \tfrac{1+i}{4}\right)$.

Applying $\Pi$ to two lists and then multiplying entry by entry gives the same result as multiplying first, because $\Pi$ only moves entries. <cite data-source="paper">Pointwise multiplication commutes with applying the same record permutation LB to both</cite> operands. <cite data-source="paper">We may therefore multiply the forward outputs in their retained order</cite>. The product can then be passed to the [opposite transform](opposite-transform.md) without a reordering step, because that transform reads entries in the stored order.
