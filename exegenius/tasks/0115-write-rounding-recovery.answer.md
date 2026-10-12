Exact recovery by rounding is the step that turns the approximate convolution coefficients into the exact binary product. It cancels a retained coordinate permutation, rounds each coefficient to an integer, and propagates carries.

Exact recovery by rounding works on the output of the [Synthetic polynomial transform](synthetic-transform.md) run in the opposite direction. Exact recovery by rounding is based on the normalized cyclic convolution that [Bluestein's chirp identity](bluestein-chirp.md) produces.

Let $\alpha$ and $\beta$ be the arrays of radix-$2^b$ digits of the two integers, each zero-padded to $S$ entries, where $S$ is the source length, the number of entries of each array. The letter $S$ changes meaning from the smaller matrix of earlier pages.

Resampling retains a coordinate permutation $R$, where $(R\alpha)_j=\alpha_{ej}$ for a unit $e$ modulo $S$, an integer coprime to $S$. Let $F_S$ be the discrete Fourier transform of length $S$, and $F_S^+$ the same sum with the opposite sign. Substituting $\eta=ek$, the index $ek$ taken modulo $S$, into the Fourier sum gives $RF_S^+R=F_S^+$. Since $R$ commutes with pointwise products, the permutation cancels:

$$RF_S^+(RF_S\alpha\cdot RF_S\beta)=F_S^+(F_S\alpha\cdot F_S\beta).$$

Write $\rho_j$ for the integer that the $j$-th computed coefficient approximates, once the known scales are removed. The paper's assembly section does this <cite data-source="paper">removes the known normalizations and digit scales</cite>.

Each truncation keeps $p=6b$ fractional bits, so it adds error below $2^{-p}$. Exact recovery by rounding inherits its error from each [simultaneous butterfly layer](simultaneous-butterfly-layer.md), which ends with one truncation. The paper proves the resulting bound on the error under its parameter choice <cite data-source="paper">proves that the recovered coefficient error is strictly below $1/2$</cite>.

If a computed value lies strictly within $1/2$ of an integer $\rho_j$, every other integer is more than $1/2$ away from that value, so $\rho_j$ is its unique nearest integer and rounding returns $\rho_j$. At distance exactly $1/2$ two integers are equally near, and rounding can pick the wrong one.

Exact recovery by rounding inverts the [Signed Kronecker packing](kronecker-packing.md), which evaluates the coefficients at $2^b$. Let $\delta_j$ be the $j$-th radix-$2^b$ digit of the integer being formed and $\sigma_j$ the carry into position $j$. Set $\sigma_0=0$ and, for each $j$, choose $\delta_j$ and $\sigma_{j+1}$ so that $\rho_j+\sigma_j=\delta_j+2^b\sigma_{j+1}$ with $0\le\delta_j<2^b$. Multiplying the $j$-th relation by $2^{bj}$ and summing, the carries cancel in pairs, so the digits represent the same integer as $\sum_j\rho_j2^{bj}$, with the final carry written as further digits. The paper's assembly section gives the exact binary product this way <cite data-source="paper">propagates carries to obtain the exact binary product</cite>.

Example in base $2$ ($b=1$): computed values $2.9$ and $5.2$ round to $\rho_0=3$ and $\rho_1=5$, which stand for $3+2\cdot5=13$. Then $3=1+2\cdot1$ gives $\delta_0=1$ and $\sigma_1=1$; $5+1=0+2\cdot3$ gives $\delta_1=0$ and $\sigma_2=3$; $\rho_2+\sigma_2=0+3=1+2\cdot1$ gives $\delta_2=1$ and $\sigma_3=1$, and the final carry is written as the digit $\delta_3=1$. The digits $1101_2$ equal $13$.
