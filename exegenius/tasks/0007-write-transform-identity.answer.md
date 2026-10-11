Transform identity with retained permutations keeps the source and target coordinate permutations inside the Gaussian resampling identity, so that they cancel across a convolution instead of being executed as sorts. It is the form of the identity used for exact integer multiplication.

The one-dimensional identity is derived from [Gaussian resampling](gaussian-resampling.md): for coprime $s<t$ with $\theta=t/s-1$ large enough, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, with contractions $A$ and $B_0$. Here $P_s$ and $P_t$ are the permutations of that identity.

Here $d$ is the number of coordinates, and $s_i$ is the length of coordinate $i$. Lifting to $d$ coordinates is a tensor product: each coordinate contributes a factor $2^{2\alpha^2}$, so the factors multiply to $2^{2d\alpha^2}$. $R$ permutes the source coordinates, and $Q$ permutes the target coordinates. The lifted identity is
$$RF_s=2^{2d\alpha^2}B_0QF_tA.$$

Let $F_s^+$ and $R^+$ be the inverses of $F_s$ and $R$, so that $RF_s^+$ is the inverse of $RF_s$ and equals $F_s^+R^+$. The symbol $\cdot$ denotes the pointwise product and $*$ denotes convolution. A permutation commutes with the pointwise product, $R(x)\cdot R(y)=R(x\cdot y)$, so $(RF_su)\cdot(RF_sv)=R\big((F_su)\cdot(F_sv)\big)$. Applying $F_s^+R^+$ removes the outer $R$, because $R^+R$ is the identity. What remains is the untwisted product, which gives the convolution up to scale:
$$(RF_s^+)((RF_su)\cdot(RF_sv))=\frac{u*v}{(\prod_i s_i)^2}.$$
So the source permutation $R$ never has to be executed.

Sorting is avoided because the usual implementation sorts twice on each coordinate, while this formula is computed directly. <cite data-source="paper">We retain both permutations in the transform formula</cite>.
