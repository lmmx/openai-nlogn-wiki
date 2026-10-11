The frequency domain of a sequence is defined through the [discrete Fourier transform](discrete-fourier-transform.md): it is the list of values that the transform assigns to the sequence. It is the representation in which [cyclic convolution](cyclic-convolution.md) becomes entrywise multiplication. The paper's chain of reductions refers to these transforms at two steps: [Gaussian resampling](gaussian-resampling.md) <cite data-source="paper">expresses each source Fourier transform through a power-of-two tensor transform</cite>, and [Bluestein's chirp identity](bluestein-chirp-identity.md) <cite data-source="paper">converts the middle transform, including its target permutation,</cite> <cite data-source="paper">into normalized cyclic convolution.</cite>

Let $f = (f_0, f_1, \ldots, f_{q-1})$ be a sequence of $q$ complex numbers. Its frequency entries are $(F_q f)_\ell$ for $\ell = 0, 1, \ldots, q-1$, and its frequency domain is the list of all $q$ of them. Each entry is

$$
(F_q f)_\ell = \frac{1}{q}\sum_{s=0}^{q-1} f_s\,\omega^{s\ell}, \qquad \omega = e^{-2\pi i/q},
$$

where $s$ is the input index of the sum and $\ell$ is the output index. The factor $\frac{1}{q}$ makes this the normalized transform, the kind that the paper implements: <cite data-source="paper">the normalized Fourier transforms needed for convolution</cite>.

The frequency domain determines $f$. The opposite transform $F_q^+$ has the same form with the opposite sign in the exponent, $(F_q^+ v)_\ell = \frac{1}{q}\sum_{s} v_s\,\omega^{-s\ell}$. Writing $\ell'$ for the summation index over frequencies, which runs over $0, \ldots, q-1$, and substituting the definition of $F_q f$,

$$
(F_q^+ F_q f)_\ell = \frac{1}{q}\sum_{\ell'=0}^{q-1} (F_q f)_{\ell'}\,\omega^{-\ell'\ell} = \frac{1}{q^2}\sum_{s=0}^{q-1} f_s \sum_{\ell'=0}^{q-1}\omega^{(s-\ell)\ell'}.
$$

The inner sum is $q$ when $s = \ell$. If $s \ne \ell$, then $0 < |s-\ell| < q$, so $\omega^{s-\ell} \ne 1$ (a primitive $q$-th root of unity has $\omega^k = 1$ only when $q$ divides $k$). The geometric sum $\sum_{\ell'}(\omega^{s-\ell})^{\ell'} = \frac{(\omega^{s-\ell})^q-1}{\omega^{s-\ell}-1}$ is then $0$, because $(\omega^{s-\ell})^q = 1$. Only $s = \ell$ survives, so $F_q^+ F_q f = f/q$, and $f = q\,F_q^+(F_q f)$.

Let $a$ and $b$ be sequences of length $q$, using the letters of the convolution page with $q$ in place of its length $n$. For an output position $t$ with $0 \le t \le q-1$, let $s'$ be the second input index, as $s$ is the first. The cyclic convolution has entries

$$
(a \ast b)_t = \sum_{\substack{s,\, s' \in \{0,\ldots,q-1\} \\ s+s' \equiv t \ (\mathrm{mod}\ q)}} a_s b_{s'},
$$

where indices wrap around modulo $q$. The representation turns this into a product:

$$
(F_q(a \ast b))_\ell = q\,(F_q a)_\ell\,(F_q b)_\ell .
$$

To see this, note that $\omega^{t\ell}$ depends only on $t$ modulo $q$, since $\omega^q = 1$. Then

$$
q\,(F_q(a\ast b))_\ell = \sum_{t}(a\ast b)_t\,\omega^{t\ell} = \sum_{s,s'} a_s b_{s'}\,\omega^{(s+s')\ell} = \Big(\sum_s a_s\,\omega^{s\ell}\Big)\Big(\sum_{s'} b_{s'}\,\omega^{s'\ell}\Big).
$$

Each bracket on the right is $q$ times a frequency entry, so the right side is $q^2 (F_q a)_\ell (F_q b)_\ell$. Dividing by $q$ gives the identity.

Worked example. Take $q = 4$, $a = (1,1,0,0)$ and $b = (1,2,0,0)$, with $\omega = -i$. The pairs with $s+s' \equiv t$ give $a \ast b = (1,3,2,0)$. For $t=1$ they are $a_0b_1$ and $a_1b_0$, so the entry is $2+1=3$. Then

$$
F_4 a = \left(\tfrac{1}{2},\ \tfrac{1-i}{4},\ 0,\ \tfrac{1+i}{4}\right), \qquad F_4 b = \left(\tfrac{3}{4},\ \tfrac{1-2i}{4},\ -\tfrac{1}{4},\ \tfrac{1+2i}{4}\right).
$$

Multiplying entry by entry and by $q = 4$ gives $\left(\tfrac{3}{2},\ \tfrac{-1-3i}{4},\ 0,\ \tfrac{-1+3i}{4}\right)$, which is $F_4(1,3,2,0)$. For instance, at $\ell = 1$, $\tfrac{1}{4}(1+3(-i)+2(-1)) = \tfrac{-1-3i}{4}$.

The paper also fixes where each frequency entry is stored. <cite data-source="paper">We also specify where each frequency entry is stored,</cite> because the [opposite transform](opposite-transform.md) must read the entries in the order the forward transform wrote them. Let $q = 2^{\nu}$, where $\nu$ is the number of binary digits of an index. (The letter $\nu$ names another integer on the mixed-radix page; here it is only this count.) Let $\mathrm{rev}(\ell)$ be the index whose $\nu$ binary digits are those of $\ell$ in reverse order. Let $\Pi$ be the record permutation that moves the entry of frequency $\ell$ to slot $\mathrm{rev}(\ell)$. The paper's version of this map does the same: <cite data-source="paper">it moves the entry at j to reva (j)</cite>. The recursion that computes the transform writes its outputs <cite data-source="paper">directly in this order;</cite> <cite data-source="paper">it does not move whole frequency indices.</cite> For $q = 4$, $\mathrm{rev}$ exchanges $1$ and $2$, so the stored $F_4 a$ is $\left(\tfrac{1}{2},\ 0,\ \tfrac{1-i}{4},\ \tfrac{1+i}{4}\right)$.

Applying $\Pi$ to two lists and then multiplying entry by entry gives the same result as multiplying first, because $\Pi$ only moves entries and does not change their values. The paper states this for its own record permutation $LB$: <cite data-source="paper">Pointwise multiplication commutes with applying the same record permutation LB to both</cite> operands. <cite data-source="paper">We may therefore multiply the forward outputs in their retained order</cite>. The product can then be passed to the [opposite transform](opposite-transform.md) in that order, since the opposite procedure reads the stored order: <cite data-source="paper">transform consumes that same order after a pointwise product.</cite>
