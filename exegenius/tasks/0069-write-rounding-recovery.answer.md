Exact recovery by rounding turns the approximate convolution coefficients into the exact binary product. It cancels a retained coordinate permutation, removes known scales, rounds each coefficient to an integer, and propagates carries.

Exact recovery by rounding works on the output of the [Synthetic polynomial transform](synthetic-transform.md) run in the opposite direction. Exact recovery by rounding is based on the normalized cyclic convolution that [Bluestein's chirp identity](bluestein-chirp.md) produces.

Let $\alpha$ and $\beta$ be the arrays of radix-$2^b$ digits of the two integers, each digit scaled by $2^{-b-2}$ and zero-padded to $S$ entries, where $S$ is the number of points of the source transform.

Resampling retains a coordinate permutation $R$, which reindexes an array by $(Rz)_j=z_{cj}$ for a unit $c$ modulo the length. Let $F_S$ be the normalized Fourier transform of length $S$ and $F_S^+$ the transform with the opposite sign. Substituting $h=ck$ in the Fourier sum gives $RF_S^+R=F_S^+$. Since $R$ commutes with pointwise products, the permutation cancels:

$$RF_S^+(RF_S\alpha\cdot RF_S\beta)=F_S^+(F_S\alpha\cdot F_S\beta).$$

The rule $F_S(\alpha*\beta)=S(F_S\alpha\cdot F_S\beta)$ and $F_S^+F_S$ multiplies by $1/S$ give $F_S^+(F_S\alpha\cdot F_S\beta)=(\alpha*\beta)/S^2$, where $*$ is cyclic convolution. Multiplying by $S$, then by $2^{2b+4}S$, gives $2^{2b+4}(\alpha*\beta)$. The factor $2^{2b+4}$ cancels the two digit scales. The integer coefficient of the digit convolution at position $j$ is $\rho_j$, so the integer product is $\sum_j\rho_j2^{bj}$.

Each truncation keeps $p=6b$ fractional bits, so it adds error below $2^{-p}$. Exact recovery by rounding inherits its error from each [simultaneous butterfly layer](simultaneous-butterfly-layer.md), which ends with one truncation. Tracking these errors through the transforms, the product and the scales, the error of each recovered coefficient is strictly below $1/2$ for large $b$ <cite data-source="paper">proves that the recovered coefficient error is strictly below $1/2$</cite>.

Since the $\rho_j$ are integers, a value strictly within $1/2$ of $\rho_j$ has $\rho_j$ as its unique nearest integer, so rounding returns $\rho_j$. At distance exactly $1/2$ two integers are equally near, and rounding can pick the wrong one.

Exact recovery by rounding inverts the [Signed Kronecker packing](kronecker-packing.md), which evaluates the coefficients at $2^b$. Here $\delta_j$ is the $j$-th radix-$2^b$ digit of the product and $\sigma_j$ is the carry into position $j$. Set $\sigma_0=0$ and, for each $j$, $\rho_j+\sigma_j=\delta_j+2^b\sigma_{j+1}$ with $0\le\delta_j<2^b$. Multiplying the $j$-th relation by $2^{bj}$ and summing, the carries cancel in pairs, so the digits $\delta_j$ represent the same integer, with the final carry written as further digits.

Example in base $2$: computed values $2.9$ and $5.2$ round to $(3,5)$, which stands for $13$. Then $3=1+2\cdot 1$ gives digit $1$ and carry $1$; $5+1=0+2\cdot 3$ gives digit $0$ and carry $3$; $3=1+2\cdot 1$ gives digit $1$ and carry $1$, written as digit $1$. The digits $1101_2$ equal $13$.
