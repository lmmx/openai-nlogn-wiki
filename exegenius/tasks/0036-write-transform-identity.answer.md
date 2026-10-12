Transform identity with retained permutations is the form of the [Gaussian resampling](gaussian-resampling.md) identity that keeps the coordinate permutations inside the formula instead of executing them as sorts. On the way to exact integer multiplication, its job is to let the source permutation cancel across a convolution.

The transform identity rests on [Gaussian resampling](gaussian-resampling.md). Its one-dimensional form $P_sF_s = 2^{2\alpha^2}B_0P_tF_tA$ holds with linear contractions $A$ and $B_0$, where a contraction is a linear map that does not increase the norm, the measure of a vector's length.

The usual implementation applies $P_s$ and $P_t$ as full sorts, twice on each coordinate. Keeping both permutations in the formula means these sorts are never executed. <cite data-source="paper">We retain both permutations in the transform formula</cite>.

The transform identity cancels its retained permutation across a [cyclic convolution](cyclic-convolution.md). Let $R$ be the source permutation $P_s$ applied along every source axis. Let $\phi$ and $\psi$ be arrays indexed by the source box, which has $M=\prod_i s_i$ entries, where $s_i$ is the length of source axis $i$. Let $F_s^{+}$ be the opposite transform, whose roots of unity have reversed sign. Write $\cdot$ for entrywise multiplication and $\ast$ for cyclic convolution on the box. Then

$$RF_s^{+}R\bigl(F_s\phi\cdot F_s\psi\bigr)=\frac{\phi\ast\psi}{M^2}.$$

The opposite transform sends $R$ to its inverse, $F_s^{+}R=R^{-1}F_s^{+}$, so $RF_s^{+}R=F_s^{+}$ and the left side is $F_s^{+}(F_s\phi\cdot F_s\psi)$. The normalizations $F_s^{+}F_s=I/M$ and $F_s(\phi\ast\psi)=M\,(F_s\phi)\cdot(F_s\psi)$ then give $(\phi\ast\psi)/M^2$.

So the retained permutation is undone inside the opposite transform. The product of two retained transforms yields the convolution directly, scaled by $1/M^2$, and no sort is needed to restore natural order.
