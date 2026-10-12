The transform identity with retained permutations is an exact identity relating the normalized Fourier transforms of two lengths, with both coordinate permutations kept as explicit factors. It is obtained by inverting the [Gaussian resampling](gaussian-resampling.md) identity, which keeps both permutations. The usual implementation sorts twice on each coordinate; explicit permutation factors can cancel across a convolution instead.

Here $2\le s<t$, $s$ and $t$ are coprime, $\alpha\ge 2$, and $\theta=t/s-1$ satisfies $\alpha^2\theta>1$. The permutations are $(P_su)_j=u_{tj}$ for a length-$s$ vector $u$, and $(P_tv)_k=v_{-sk}$ for a length-$t$ vector $v$, with subscripts taken modulo $s$ and $t$. The step claims
$$P_sF_s=2^{2\alpha^2}B_0P_tF_tA,$$
where $A$ is the first contraction, a linear map from length-$s$ to length-$t$ vectors, and $B_0$ is the second contraction, a linear map from length-$t$ to length-$s$ vectors. The claim is stated in <cite data-source="paper">Lemma 19 (Resampling without executing the two permutations)</cite>.

The proof uses the Gaussian maps $S$ and $T$, which send length-$s$ vectors to length-$t$ vectors, and the Gaussian identity
$$TP_sF_s=P_tF_tS.$$
It says that transforming at length $s$ and then resampling with $T$ agrees with resampling with $S$ and then transforming. Prior work establishes it <cite data-source="paper">The exact Gaussian identity and inverse estimate proved in [15, Theorem 4.2 and Lemma 4.6]</cite>, and it applies because $S$ and $T$ share the same $s$, $t$ and $\alpha$.

Let $I$ denote the identity map. The operator $N=CTD$ is close to $I$. In $(Nu)_j$, the summand with index $j$ is exactly $u_j$, since the factor $e^{\pi\alpha^2\beta_j^2}$ in $D$ cancels the Gaussian factor of $T$ at $\ell_j$. The other summands form $(N-I)u$, and the same prior-work estimate gives $\|N-I\|<2^{-\alpha^2\theta}$, which is below $1/2$ because $\alpha^2\theta>1$. So the Neumann series $\sum_{i\ge 0}(I-N)^i$, the matrix analogue of the geometric series, converges to $N^{-1}$, and $\|N^{-1}\|\le 1+\sum_{i\ge 1}\|I-N\|^i<2$.

The map $C$ selects $\ell_0$ through $\ell_{s-1}$ from a length-$t$ vector. These indices are distinct: the points $tj/s$ are spaced $t/s>1$ apart, and rounding to the nearest integer keeps points more than one apart in order. So each row of $C$ has a single entry $1$. The operator norm for the maximum-modulus vector norm is the largest absolute row sum, so $\|C\|=1$.

Define the scaled copies $S'=S/2$, $J'=N^{-1}/2$ and $D'=2^{-(2\alpha^2-2)}D$. Since $|\beta_j|\le 1/2$, $\|D\|\le e^{\pi\alpha^2/4}$, so $\|D'\|\le 2^{-(2\alpha^2-2)}e^{\pi\alpha^2/4}$. Each row of $S$ has weights $\frac1\alpha e^{-\pi\alpha^{-2}(j-sk/t)^2}$. Their sum is at most $\frac1\alpha(\alpha+1)=1+\frac1\alpha\le\frac32$, because the Gaussian integral equals $\alpha$ and a unimodal function summed over the integers is at most its integral plus its maximum. So $\|S'\|\le 3/4$, and $\|J'\|=\|N^{-1}\|/2<1$. Both maps are linear contractions, that is, linear maps bounded in the [operator norm](operator-norm.md) by one. Hence $A=S'$ and $B_0=D'J'C$.

Since $N=CTD$, we have $CT=ND^{-1}$, so $(DN^{-1}C)T=I$. So $DN^{-1}C$ is a left inverse of $T$, and applying it to the Gaussian identity gives $DN^{-1}CP_tF_tS=P_sF_s$. Therefore
$$B_0P_tF_tA=D'J'C\,P_tF_t\,S'=2^{-(2\alpha^2-2)}\,\tfrac12\,\tfrac12\,DN^{-1}CP_tF_tS=2^{-2\alpha^2}P_sF_s,$$

The constant $2^{2\alpha^2}$ depends only on $\alpha$: the only scalar factors introduced are the three normalizations, while $1/\alpha$, the Gaussian factors and the lengths sit inside the maps.
