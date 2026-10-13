A Gaussian dyadic number is a complex number $z = a + bi$ whose real part $a$ and imaginary part $b$ are both dyadic rationals, that is, rationals $m/2^k$ with $m$ an integer and $k \ge 0$. Write $\mathcal{G}$ for the set of all such numbers. The concept matters because the values produced inside the butterfly layer stay in $\mathcal{G}$, so the layer can compute them exactly.

Let $u$ and $v$ be two Gaussian dyadic numbers. The real and imaginary parts of $u+v$, $u-v$ and $uv$ are sums, differences and products of dyadic rationals, hence dyadic rationals, so $\mathcal{G}$ is closed under addition, subtraction and multiplication. Halving is closed too, since $m/2^k$ divided by $2$ is $m/2^{k+1}$.

The butterfly $H_0(u,v) = ((u+v)/2, (u-v)/2)$ takes two Gaussian dyadics $u$ and $v$ and returns two Gaussian dyadics, each with denominator at most $2^{k+1}$ when the real and imaginary parts of $u$ and $v$ have denominators dividing $2^k$. For example, take $u = 1 + \tfrac12 i$ and $v = \tfrac14 - i$. Then
$$\frac{u+v}{2} = \frac58 - \frac14 i, \qquad \frac{u-v}{2} = \frac38 + \frac34 i.$$
The inputs have denominators dividing $4$, and the outputs have denominators dividing $8$, as the rule predicts.

Nothing is rounded inside the layer, because its intermediate values are exact. <cite data-source="paper">Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators.</cite> Rounding is needed only once, at a single truncation after the layer is complete.
