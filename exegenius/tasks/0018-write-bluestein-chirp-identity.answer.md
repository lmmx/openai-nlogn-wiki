Bluestein's chirp identity rewrites a [discrete Fourier transform](discrete-fourier-transform.md) as a convolution. It is the step that turns the middle transform in the paper's algorithm into a [cyclic convolution](cyclic-convolution.md).

Let $\omega = \zeta^2$ be a root of unity, with $\zeta$ itself a root of unity of twice the order. The DFT entry $\omega^{jk}$ can be split using the identity

$$2jk = j^2 + k^2 - (k - j)^2.$$

So $\zeta^{2jk} = \zeta^{j^2}\,\zeta^{k^2}\,\zeta^{-(k-j)^2}$. The factors $\zeta^{j^2}$ and $\zeta^{-(k-j)^2}$ are the chirp: a quadratic-phase sequence whose phases grow with the square of the index. Substituting into the DFT gives

$$\hat a_k = \zeta^{k^2} \sum_{j} \bigl(a_j \zeta^{j^2}\bigr)\, \zeta^{-(k-j)^2}.$$

The sum is a convolution of the sequence $u_j = a_j \zeta^{j^2}$ with the fixed sequence $v_m = \zeta^{-m^2}$. The output is then multiplied by $\zeta^{k^2}$.

For a small check, take $N = 2$, $\omega = -1$, and $\zeta = i$. The identity gives $\hat a_0 = a_0 + a_1$ and $\hat a_1 = i\,(a_0 \cdot i^{0} \cdot i^{-1} + a_1 \cdot i^{1} \cdot i^{0}) = i(-i\,a_0 + i\,a_1) = a_0 - a_1$, which is the DFT of $(a_0, a_1)$.

The paper applies the identity to a middle transform with its target permutation included. This yields a normalized cyclic convolution on power-of-two axes, which is then handled by the [phase twist](phase-twist.md) and the polynomial-ring convolution. The identity is applied after the [Gaussian resampling](gaussian-resampling.md) step, which reduces the transform to the form it needs.
