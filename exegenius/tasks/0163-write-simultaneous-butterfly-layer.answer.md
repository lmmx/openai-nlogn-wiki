A simultaneous butterfly layer applies the two-point map $H_0$ to several selected address bits at once, in one exact pass over the array, instead of one pass per selected axis. It is the step that makes the transforms of the multiplication cheap.

On the address layout of the multiplication algorithm, the same bit position is selected in each of at most $d$ equal-width address chunks. The layer acts on $D$ selected chunks, where $1 \le D \le d$. It acts coefficientwise on the polynomial record at each address and preserves all other address fields.

The two-point map $H_0$ sends a pair with first input $z_0$ and second input $z_1$ to half their sum and half their difference: $H_0(z_0,z_1) = ((z_0+z_1)/2,\ (z_0-z_1)/2)$. The layer is built from the normalized [discrete Fourier transform](discrete-fourier-transform.md) of length 2, namely $H_0$, applied to each selected bit. On $D$ selected bits, the layer is formed as a [tensor product](tensor-product.md) of $H_0$ with itself $D$ times, so each output combines all $2^D$ values that agree with it on the unselected bits. For $D=2$, the four values $z_{00}, z_{01}, z_{10}, z_{11}$, indexed by the two selected bits, become four sums and differences, each divided by 4. The value at index $00$ becomes $(z_{00}+z_{01}+z_{10}+z_{11})/4$.

Applying $H_0$ one selected bit at a time would take $D$ full passes over the array, one scan per selected axis. The point of the layer is to apply all $D$ bits in one pass, which avoids paying a full scan for each selected axis.

The method has two steps. The complex two-point kernel $C = aI + bX$ is a $2\times 2$ complex matrix. The layer's complex form $C^{\otimes D}$ is realized by a [complex phase network](complex-phase-network.md) with dyadic frame changes. <cite data-source="paper">Its phase frames express a C tensor product using smaller groups of selected bits, separated by binary changes of basis.</cite>

The second step turns this into $H_0$ with phases. Let $S$ be the diagonal $2\times 2$ matrix with diagonal entries $1$ and $i$. Multiplying out the $2\times 2$ matrices shows that $H_0$ on one bit is $SCS$ up to a scalar. The scalar $\beta_D$ is a power of $\tfrac12$ times a fourth root of unity, with at most one further factor $b$. The diagonal map $S_D$ multiplies the value at each address by $i$ raised to the number of selected bits equal to 1. Together these give

$$H_0^{\otimes D} = \beta_D\, S_D\, C^{\otimes D}\, S_D.$$

The layer keeps its intermediate values exact in [Gaussian dyadics](gaussian-dyadics.md). <cite data-source="paper">These identities use only Gaussian dyadic coefficients.</cite>

The frame changes between groups of selected bits are binary changes of basis. The layer moves its address chunks by [address-field interchange](address-interchange.md), which realizes these changes of basis.

The phase frames split the selected bits into smaller groups, so each recursive call handles a smaller volume. Here $\lambda'$ is a fixed exponent below 1, so the cost grows more slowly than $d$ full passes over the array. The layer costs $O(V d^{\lambda'})$ <cite data-source="paper">We will obtain cost O(V dλ ), with λ′ < 1</cite>.
