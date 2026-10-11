Transform identity with retained permutations is the form of the [Gaussian resampling](gaussian-resampling.md) identity in which the source and target coordinate permutations stay in the formula, so that they cancel across a convolution instead of being executed as sorts.

Write $F_s$ and $F_t$ for $F_q$ with $q=s$ and $q=t$, the normalized transforms of vectors of $s$ and $t$ coordinates, and $F_s^+$ for the opposite transform $F_q^+$ with $q=s$. The letters $A$ and $B_0$ denote the one-dimensional contractions below, and after lifting they denote tensor products. The one-dimensional identity holds for [coprime](coprime-integers.md) $s<t$ with $\theta=t/s-1$ large enough: $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, with contractions $A$ and $B_0$. The one-dimensional identity is derived from [Gaussian resampling](gaussian-resampling.md).

Here $d$ is the number of coordinates, not the digit count. Here $s_i$ and $t_i$ are the numbers of entries along coordinate $i$ of the source and target grids. The arrays $u$ and $v$ now live on the source grid of shape $s_1\times\cdots\times s_d$. Here $R=\bigotimes_i P_{s_i}$ permutes the source coordinates, and $Q=\bigotimes_i P_{t_i}$ permutes the target coordinates. The identity is lifted by a [tensor product](tensor-product.md) of the one-dimensional identities to $d$ coordinates. Each one-dimensional identity contributes $2^{2\alpha^2}$, so the factors multiply to $2^{2d\alpha^2}$:

$$RF_s=2^{2d\alpha^2}B_0QF_tA.$$

Write $R_c$ for the permutation $(R_c z)_j=z_{cj}$ of length-$q$ vectors, where $c$ is a unit modulo $q$. Substituting $h=cj$ in the sum defining $F_q^+$ gives $F_q^+R_c=R_c^{-1}F_q^+$. Since $P_{s_i}=R_{t_i}$ and each $t_i$ is a unit modulo $s_i$, tensoring gives $F_s^+R=R^{-1}F_s^+$, hence $RF_s^+R=F_s^+$. Permutations commute with coordinatewise products, so $(RF_su)\cdot(RF_sv)=R\big((F_su)\cdot(F_sv)\big)$, where $\cdot$ is the coordinatewise product. Hence

$$(RF_s^+)\big((RF_su)\cdot(RF_sv)\big)=RF_s^+R\big((F_su)\cdot(F_sv)\big)=F_s^+\big((F_su)\cdot(F_sv)\big).$$

Writing $u*v$ for the cyclic convolution on the source grid. The cancellation is based on the [convolution theorem](convolution-theorem.md): with the $1/q$ factor of $F_q$, $F_s(u*v)=\left(\prod_i s_i\right)(F_su)\cdot(F_sv)$. The same factor gives $F_s^+F_s=\frac{1}{\prod_i s_i}I$, so

$$(RF_s^+)\big((RF_su)\cdot(RF_sv)\big)=\frac{u*v}{(\prod_i s_i)^2}.$$

The source permutation $R$ is never executed. Keeping both permutations avoids the two sorts per coordinate that the usual implementation performs <cite data-source="paper">We retain both permutations in the transform formula</cite>.
