A Gaussian dyadic number is a complex number $z = a + bi$ whose real part $a$ and imaginary part $b$ are both dyadic rationals, that is, rationals $m/2^k$ with $m$ an integer and $k \ge 0$. Write $\mathcal{G}$ for the set of these numbers. They matter because the butterfly layer keeps its values in $\mathcal{G}$.

The butterfly layer applies a map $H_0(u,v) = ((u+v)/2, (u-v)/2)$ to pairs $u, v$ of values. A chunk is one of the equal-width blocks into which the array's addresses are divided; the layer applies $H_0$ to pairs in every chunk at once.

For Gaussian dyadics $u$ and $v$, sums and differences of their parts are dyadic, and halving raises each $k$ by one, so $H_0$ maps Gaussian dyadic pairs to Gaussian dyadic pairs. Take $u = 1 + \tfrac12 i$ and $v = \tfrac14 - i$. Then
$$\frac{u+v}{2} = \frac58 - \frac14 i, \qquad \frac{u-v}{2} = \frac38 + \frac34 i.$$

The layer's inputs are intermediate values, and these lie in $\mathcal{G}$. <cite data-source="paper">Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators.</cite> Every output of $H_0$ is again in $\mathcal{G}$, so the layer computes exactly and rounds nothing.

Each stored part is a multiple of $2^{-p}$, where $p$ is the number of fractional bits. A truncation rounds each part toward zero to such a multiple, so it changes a part by less than $2^{-p}$.

The layer is contractive in the maximum norm: each output has size at most that of the larger input, so an error already present does not grow. The paper truncates once. <cite data-source="paper">A single truncation follows the completed contractive layer.</cite> Starting with no error, since its inputs are exact, the layer adds none, so the total error is one truncation error.

The letters $m$, $u$ and $v$ mean what is said above only on this page; the later pages that use them give them other meanings.
