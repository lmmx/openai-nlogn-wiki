The transform identity with retained permutations is an exact identity between the normalized Fourier transforms $F_s$ and $F_t$ of two lengths, in which the coordinate permutations $P_s$ and $P_t$ stay as explicit factors. Because they remain factors, they can cancel across a convolution instead of being executed as sorts. It is the step that lets transforms of power-of-two length stand in for the coprime transform lengths of the integer product.

It is obtained by inverting the [Gaussian resampling](gaussian-resampling.md) identity, which keeps both permutations. The usual implementation sorts twice on each coordinate, and the paper makes the alternative explicit. <cite data-source="paper">We retain both permutations in the transform formula</cite>. Its motivation is that computing the formula directly avoids those sorts.

Let $2\le s<t$ with $s$ and $t$ coprime, let $\alpha\ge 2$, and let $\theta=t/s-1$ satisfy $\alpha^2\theta>1$. Here $P_s$ permutes the coordinates of length-$s$ vectors and $P_t$ permutes those of length-$t$ vectors, with subscripts taken modulo $s$ and $t$. Here $A$ is a linear map from length-$s$ to length-$t$ vectors. $B_0$ is a linear map from length-$t$ to length-$s$ vectors. The identity is
$$P_sF_s=2^{2\alpha^2}B_0P_tF_tA,$$
The claim is stated in <cite data-source="paper">Lemma 19 (Resampling without executing the two permutations)</cite>. The two maps are linear contractions, bounded in the [operator norm](operator-norm.md) by one, meaning each sends a vector to one of norm at most its input norm.

The proof uses the Gaussian maps $S$ and $T$, which send length-$s$ vectors to length-$t$ vectors, and the Gaussian identity $TP_sF_s=P_tF_tS$. Let $N=CTD$, where $C$ selects the coordinates $\ell_j$ and $D$ is the diagonal factor. The inverse estimate of prior work, proved in [15, Theorem 4.2 and Lemma 4.6], gives $\|N-I\|<2^{-\alpha^2\theta}$, which is below $1/2$ because $\alpha^2\theta>1$. So $\|E\|<1$ for $E=I-N$, and the Neumann series $\sum_{r\ge 0}E^r$, the matrix analogue of the geometric series, converges, so $N$ is invertible.

Set $S'=S/2$, $J'=N^{-1}/2$ and $D'=2^{-(2\alpha^2-2)}D$, and take $A=S'$ and $B_0=D'J'C$. Both are linear contractions, since $\|C\|=1$ and $\|S'\|$, $\|J'\|$, $\|D'\|$ are below their stated bounds.

Since $N=CTD$ and $D$ is invertible, $CT=ND^{-1}$, so $(DN^{-1}C)T=I$. The map $DN^{-1}C$ is a left inverse of $T$. Applying it to the Gaussian identity gives $DN^{-1}CP_tF_tS=P_sF_s$, and hence
$$B_0P_tF_tA=2^{-(2\alpha^2-2)}\cdot\tfrac12\cdot\tfrac12\,DN^{-1}CP_tF_tS=2^{-2\alpha^2}P_sF_s.$$
Multiplying by $2^{2\alpha^2}$ gives the identity.

The constant depends only on $\alpha$. Its scalar factors multiply to $2^{-(2\alpha^2-2)}\cdot\tfrac12\cdot\tfrac12=2^{-2\alpha^2}$, a power of two whose exponent is set by $\alpha$ alone. The lengths $s$ and $t$ and the Gaussian weights sit inside $S$, $T$ and $N$, and never reach the constant.
