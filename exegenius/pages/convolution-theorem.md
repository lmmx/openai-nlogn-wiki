The convolution theorem says that the transform of a convolution of two sequences is the pointwise product of their transforms. The argument uses it to turn a convolution into a product, so that the coordinate permutations kept in the transforms pass through the convolution unchanged.

Let $d$ be the number of axes of an array, let $s_i$ be the length of axis $i$, and let $S=\prod_i s_i$ be the number of positions in the array. The theorem takes its transforms by the [Discrete Fourier transform](discrete-fourier-transform.md) $F_s$, applied along every axis and normalized by $1/S$. $F_s^+$ is the same transform with $\omega^{-1}$ in place of $\omega$.

Let $u$ and $v$ be arrays of the same shape. The theorem concerns the [Cyclic convolution](cyclic-convolution.md) $u*v$, taken along every axis, so each index wraps around modulo its axis length. It states

$$F_s(u*v)=S\,(F_su)\cdot(F_sv),$$

where $\cdot$ multiplies entries at the same position. The factor $S$ comes from the normalization <cite data-source="paper">Fs (u ∗ v) = S(Fs u) · (Fs v)</cite>.

Example with $d=1$, $s_1=2$, $\omega=-1$, $u=(1,2)$, $v=(3,4)$. Then $u*v=(11,10)$, $F_2u=(1.5,-0.5)$, $F_2v=(3.5,-0.5)$, and the pointwise product is $(5.25,0.25)$. Multiplying by $S=2$ gives $(10.5,0.5)=F_2(u*v)$, as the theorem says.

The product form is what the argument needs. Applying $F_s^+$ and using $F_s^+F_s=I/S$ gives $F_s^+(F_su\cdot F_sv)=(u*v)/S^2$, so the convolution can be recovered from transforms alone.
