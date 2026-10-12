Transform identity with retained permutations is the form of the identity from [Gaussian resampling](gaussian-resampling.md) that keeps the source and target coordinate permutations inside the formula instead of executing them as sorts. On the way to exact integer multiplication, its job is to let the source permutation cancel across a convolution.

The identity rests on [Gaussian resampling](gaussian-resampling.md): its one-dimensional form $P_sF_s = 2^{2\alpha^2}B_0P_tF_tA$ holds with linear contractions $A$ and $B_0$. A contraction is a linear map that does not increase the norm, a measure of a vector's length.

The usual implementation sorts twice on each coordinate. Keeping both permutations in the formula means those sorts are never executed. <cite data-source="paper">We retain both permutations in the transform formula</cite>.

The cancellation concerns the source side alone: the retained source permutation cancels across a [cyclic convolution](cyclic-convolution.md). Let $R$ be the source permutation $P_s$ applied along every source axis, and let $F_s^{+}$ be the opposite transform, the transform with the sign of its roots of unity reversed. Let $f$ and $g$ be arrays indexed by the source box, which has $M=\prod_i s_i$ entries, where $s_i$ is the length of source axis $i$. Writing $\cdot$ for coordinatewise multiplication and $\ast$ for cyclic convolution on the box,
$$RF_s^{+}R\bigl(F_sf\cdot F_sg\bigr)=\frac{f\ast g}{M^2}.$$

Each $t_i$ is a unit modulo $s_i$ because $\gcd(s,t)=1$, so $RF_s^{+}R=F_s^{+}$. Since $R$ commutes with pointwise products, the left side is $F_s^{+}(F_sf\cdot F_sg)$. The normalizations give $F_s^{+}F_s=I/M$, where $I$ is the identity map on the box, and $F_s(f\ast g)=M\,(F_sf)\cdot(F_sg)$. Hence $F_s^{+}(F_sf\cdot F_sg)=(f\ast g)/M^2$.

So the retained permutation is undone inside the opposite transform, and the product of two retained transforms yields the convolution directly, scaled by $1/M^2$. No sort is needed to bring the result into natural order.
