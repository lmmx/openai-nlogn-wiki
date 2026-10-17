A multidimensional transform is the Fourier transform of an array with several coordinates, computed along one axis at a time. The argument replaces the long Fourier transforms of the integer product by multidimensional transforms whose axis lengths are powers of two <cite data-source="paper">multidimensional transforms whose axis lengths are powers of two</cite>.

Let $d$ be the number of axes and $q_i$ the number of positions along axis $i$, so $\boldsymbol q=(q_1,\dots,q_d)$. An entry of the array $u$ has an index tuple $j=(j_1,\dots,j_d)$ with $0\le j_i<q_i$. A line along axis $i$ is the set of $q_i$ entries obtained by fixing all other coordinates. For operators $G_i$ acting on sequences of length $q_i$, the tensor product $\bigotimes_i G_i$ applies $G_i$ to every line along axis $i$, for each $i$. Here $F_{q_i}$ is the one-dimensional normalized [Discrete Fourier transform](dft.md) of length $q_i$, and $F_{\boldsymbol q}:=\bigotimes_iF_{q_i}$ <cite data-source="paper">F_{\boldsymbol q}:=\bigotimes_iF_{q_i}</cite> is the tensor product of these. Its entries are
$$(F_{\boldsymbol q}u)_k=\frac1{\prod_i q_i}\sum_j u_j\,e^{-2\pi i\sum_i j_ik_i/q_i},$$
where $k$ is an output index tuple of the same shape as $j$.

## Cost for power-of-two axes

Write $t_i$ for the axis lengths when each is a power of two, and $T=\prod_it_i$. Each line transform is computed by the [Butterflies and the fast transform](butterfly.md) in $O(t_i\log t_i)$ operations. Axis $i$ has $T/t_i$ lines, so its pass costs $O(T\log t_i)$ and all passes cost $O(T\log T)$. For the prime lengths $s_i$ of the integer product there is no such bound.

## Lifting the resampling identity

The one-dimensional lemma of [Gaussian resampling](gaussian-resampling.md) treats coprime $s_i<t_i$, with $t_i$ a power of two sufficiently larger than $s_i$. Let $p$ be the number of fractional bits of the stored values, $\alpha$ an integer resampling parameter with $2\le\alpha<\sqrt p$, and $\delta$ a fixed constant with $0<\delta<1/8$. With index permutations $P_{s_i},P_{t_i}$ there are linear maps $A_i,B_{0,i}$ with
$$P_{s_i}F_{s_i}=2^{2\alpha^2}B_{0,i}P_{t_i}F_{t_i}A_i.$$
Both are contractions, as in [Contractions and bilinear contractions](contraction-maps.md), so an input error does not grow. Fixed-point algorithms approximate each with error less than $p^2$, meaning the output is within $p^22^{-p}$ of the exact one, in time $O(t_ip^{3/2+\delta}\alpha)$.

Tensor the $d$ identities, with the same $p,\alpha,\delta$ on every axis. Operators on separate axes compose axis by axis, so $(\bigotimes_i X_i)(\bigotimes_i Y_i)=\bigotimes_i X_iY_i$ for operators $X_i,Y_i$ on axis $i$, and the scalars multiply. With $\boldsymbol s=(s_1,\dots,s_d)$, $\boldsymbol t=(t_1,\dots,t_d)$, $\gamma=2d\alpha^2$, and, writing $R$ and $Q$ here as permutation products, not the scalar ring, $R=\bigotimes_iP_{s_i}$, $Q=\bigotimes_iP_{t_i}$, $\mathcal A=\bigotimes_iA_i$, $\mathcal B_0=\bigotimes_iB_{0,i}$:
$$RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A.$$

A pass applies a line map to every line, so its norm is the maximum over lines; hence $\mathcal A$ and $\mathcal B_0$ are contractions <cite data-source="paper">Both $\mathcal A$ and $\mathcal B_0$ are contractions.</cite>. A pass has error the maximum of the line errors, less than $p^2$, and earlier errors do not grow in later passes, so the $d$ passes give error less than $dp^2$ <cite data-source="paper">Composing the $d$ axis maps gives error less than $dp^2$.</cite>. Summing $T/t_i$ lines per axis, the one-dimensional algorithms take $O(dTp^{3/2+\delta}\alpha)$ in total.
