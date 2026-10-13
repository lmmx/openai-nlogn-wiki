A Gaussian dyadic number is a complex number $z = a + bi$ whose real part $a$ and imaginary part $b$ are both dyadic rationals, that is, rationals $m/2^k$ with $m$ an integer and $k \ge 0$. Write $\mathcal{G}$ for the set of these numbers. The butterfly layer, which applies $H_0$ to one bit of every chunk, keeps its values in $\mathcal{G}$, so it computes them exactly.

For Gaussian dyadics $u$ and $v$, sums and differences of their parts are dyadic, and halving only increases $k$ by one. So $H_0(u,v) = ((u+v)/2, (u-v)/2)$ maps Gaussian dyadics to Gaussian dyadics. For example, $u = 1 + \tfrac12 i$ and $v = \tfrac14 - i$ give
$$\frac{u+v}{2} = \frac58 - \frac14 i, \qquad \frac{u-v}{2} = \frac38 + \frac34 i.$$

Nothing is rounded inside the layer. <cite data-source="paper">Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators.</cite> The stored coefficients are fixed-point numbers: each real and imaginary part is a multiple of $2^{-p}$, where $p$ is the number of fractional bits. A truncation rounds each part toward zero to such a multiple, which changes it by less than $2^{-p}$.

The layer is contractive in the maximum norm: each output has size at most that of the larger input, so an error already present does not grow. Truncating after every round would add an error each round. The paper truncates once instead. <cite data-source="paper">A single truncation follows the completed contractive layer.</cite> The total error is then one truncation error.
