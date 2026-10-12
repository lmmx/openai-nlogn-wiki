Transform identity with retained permutations is the form of the Gaussian resampling identity that keeps the source and target coordinate permutations inside the formula, instead of executing them as sorts. On the way to exact integer multiplication, its job is to let the source permutation cancel across a convolution.

Let $s$ be the number of entries along the source axis and $t$ the number along the target axis, with $\gcd(s,t)=1$. Let $\alpha$ be an integer parameter of the identity. $P_s$ is the source coordinate permutation, which reorders the $s$ entries of each source axis. $F_s$ applies the one-dimensional transform of length $s$ along each source axis. $P_t$ is the target coordinate permutation, which reorders the $t$ entries of each target axis, and $F_t$ applies the one-dimensional transform of length $t$ along each target axis.

$A$ is a linear contraction from the source axis to the target axis. $B_0$ is a linear contraction from the target axis back to the source axis. A contraction is a linear map that does not increase the norm of a vector.

The identity rests on [Gaussian resampling](gaussian-resampling.md): its one-dimensional form $P_sF_s = 2^{2\alpha^2}B_0P_tF_tA$ holds with linear contractions $A$ and $B_0$.

The usual implementation sorts twice on each coordinate. Keeping both permutations in the formula means those sorts are never executed. <cite data-source="paper">We retain both permutations in the transform formula</cite>.

The cancellation concerns the source side only. Let $R$ be the source permutation kept in the formula, and let $F_s^{+}$ be the opposite transform, the transform with the sign of its roots of unity reversed. Let $u$ and $v$ be arrays indexed by the source box, which has $S=\prod_i s_i$ entries, where $s_i$ is the length of source axis $i$. Writing $\cdot$ for coordinatewise multiplication and $\ast$ for cyclic convolution,
$$RF_s^{+}\bigl((RF_su)\cdot(RF_sv)\bigr)=\frac{u\ast v}{S^2}.$$
The retained permutation $R$ is undone inside the opposite transform, so the product of two retained transforms yields the convolution directly, scaled by $1/S^2$. No sort is needed to bring the result into natural order.
