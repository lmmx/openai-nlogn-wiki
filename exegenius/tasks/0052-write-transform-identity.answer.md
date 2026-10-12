The transform identity with retained permutations is an exact identity between the normalized Fourier transforms $F_s$ and $F_t$ of two lengths, in which both coordinate permutations stay as explicit factors, so that they can cancel across a convolution. It is obtained by inverting the [Gaussian resampling](gaussian-resampling.md) identity, which keeps both permutations. The usual implementation sorts twice on each coordinate, and keeping both permutations in the formula avoids those sorts. The paper makes this choice explicitly <cite data-source="paper">We retain both permutations in the transform formula</cite>.

Here $2\le s<t$, $s$ and $t$ are coprime, $\alpha\ge 2$, and $\theta=t/s-1$ satisfies $\alpha^2\theta>1$. The permutations $P_s$ and $P_t$ are those of the Gaussian resampling page: $P_s$ permutes coordinates of length-$s$ vectors and $P_t$ permutes coordinates of length-$t$ vectors, with subscripts taken modulo $s$ and $t$. The identity is
$$P_sF_s=2^{2\alpha^2}B_0P_tF_tA,$$
Here $A$ is a linear map from length-$s$ to length-$t$ vectors and $B_0$ is a linear map from length-$t$ to length-$s$ vectors. The letters $A$ and $B_0$ are new maps here, not the $A=S$ and $B=DN^{-1}C$ of the Gaussian resampling page. The two maps are linear contractions, bounded in the [operator norm](operator-norm.md) by one, meaning each sends a vector to one of norm at most its input norm. The claim is stated in <cite data-source="paper">Lemma 19 (Resampling without executing the two permutations)</cite>.

The proof uses the Gaussian maps $S$ and $T$, which send length-$s$ vectors to length-$t$ vectors, and the Gaussian identity
$$TP_sF_s=P_tF_tS.$$
It says that transforming at length $s$ and then resampling with $T$ agrees with resampling with $S$ and then transforming. It applies because $S$ and $T$ share the same $s$, $t$ and $\alpha$, and prior work proves it.

The inverse estimate of prior work gives $\|N-I\|<2^{-\alpha^2\theta}$ <cite data-source="paper">inverse estimate proved in [15, Theorem 4.2 and Lemma 4.6]</cite>, which is below $1/2$ because $\alpha^2\theta>1$. So $\|E\|<1$ with $E=I-N$, and the Neumann series $\sum_{r\ge 0}E^r$, the matrix analogue of the geometric series, converges, so $N$ is invertible.

The scaled maps are $S'=S/2$, $J'=N^{-1}/2$ and $D'=2^{-(2\alpha^2-2)}D$. Set $A=S'$ and $B_0=D'J'C$, where $C$ is the selection map of the Gaussian resampling page. Both are linear contractions, since $\|C\|=1$ and $\|S'\|$, $\|J'\|$, $\|D'\|$ are below their bounds.

Since $N=CTD$ and $D$ is invertible, $CT=ND^{-1}$, so $(DN^{-1}C)T=DN^{-1}ND^{-1}=I$. Thus $DN^{-1}C$ is a left inverse of $T$. Applying it to the Gaussian identity gives $DN^{-1}CP_tF_tS=P_sF_s$, and therefore
$$B_0P_tF_tA=2^{-(2\alpha^2-2)}\cdot\tfrac12\cdot\tfrac12\,DN^{-1}CP_tF_tS=2^{-2\alpha^2}P_sF_s.$$
Multiplying by $2^{2\alpha^2}$ gives the identity.

The constant $2^{2\alpha^2}$ depends only on $\alpha$. Its three normalizations multiply to $2^{-(2\alpha^2-2)}\cdot\tfrac12\cdot\tfrac12=2^{-2\alpha^2}$. The Gaussian weights, the factor $1/\alpha$ in $S$, and the lengths $s$ and $t$ sit inside the maps $S$, $T$ and $N$, so they never reach the constant.
