The transform identity with retained permutations is an exact identity between the normalized Fourier transforms $F_s$ and $F_t$ of two lengths, in which both coordinate permutations $P_s$ and $P_t$ stay as explicit factors. It is obtained by inverting the [Gaussian resampling](gaussian-resampling.md) identity, which keeps both permutations. The usual implementation sorts twice on each coordinate. Keeping both permutations in the formula avoids those sorts and lets them cancel across a convolution. The paper makes this choice explicitly <cite data-source="paper">We retain both permutations in the transform formula</cite>

Here $2\le s<t$, $s$ and $t$ are coprime, $\alpha\ge 2$, and $\theta=t/s-1$ satisfies $\alpha^2\theta>1$. Here $v$ is a generic length-$t$ vector, not the second integer of radix-digit convolution. The permutations are $(P_su)_j=u_{tj}$ for a length-$s$ vector $u$, and $(P_tv)_k=v_{-sk}$ for a length-$t$ vector $v$, with subscripts taken modulo $s$ and $t$. The identity is
$$P_sF_s=2^{2\alpha^2}B_0P_tF_tA,$$
where $A$ is a linear map from length-$s$ to length-$t$ vectors and $B_0$ is a linear map from length-$t$ to length-$s$ vectors. The letters $A$ and $B_0$ mean these new maps here, not the $A=S$ and $B=DN^{-1}C$ of the Gaussian resampling page. The two maps are linear contractions, bounded in the [operator norm](operator-norm.md) by one, meaning each sends a vector to one of norm at most its input norm. The claim is stated in <cite data-source="paper">Lemma 19 (Resampling without executing the two permutations)</cite>.

The proof uses the Gaussian maps $S$ and $T$, which send length-$s$ vectors to length-$t$ vectors, and the Gaussian identity
$$TP_sF_s=P_tF_tS.$$
It says that transforming at length $s$ and then resampling with $T$ agrees with resampling with $S$ and then transforming. Prior work establishes it, with the proof in <cite data-source="paper">[15, Theorem 4.2 and Lemma 4.6]</cite>, and it applies because $S$ and $T$ share the same $s$, $t$ and $\alpha$.

Let $I$ denote the identity map. The operator $N=CTD$ is close to $I$: the inverse estimate of prior work gives $\|N-I\|<2^{-\alpha^2\theta}$ <cite data-source="paper">[15, Theorem 4.2 and Lemma 4.6]</cite>, which is below $1/2$ because $\alpha^2\theta>1$. <cite data-source="paper">Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series.</cite> The Neumann series is the matrix analogue of the geometric series, and it converges when $\|I-N\|<1$.

The scaled maps are $S'=S/2$, $J'=N^{-1}/2$ and $D'=2^{-(2\alpha^2-2)}D$. Set $A=S'$ and $B_0=D'J'C$, where $C$ is the selection map from the Gaussian resampling page. <cite data-source="paper">Because ∥C∥ = 1, both are contractions.</cite>

Since $N=CTD$ and $D$ is invertible, $CT=ND^{-1}$. Hence $(DN^{-1}C)T=DN^{-1}ND^{-1}=I$, so $DN^{-1}C$ is a left inverse of $T$, meaning it maps $T$ back to the identity. Applying it to the Gaussian identity gives $DN^{-1}CP_tF_tS=P_sF_s$. Therefore
$$B_0P_tF_tA=D'J'C\,P_tF_t\,S'=2^{-(2\alpha^2-2)}\cdot\tfrac12\cdot\tfrac12\,DN^{-1}CP_tF_tS=2^{-2\alpha^2}P_sF_s.$$

The constant $2^{2\alpha^2}$ depends only on $\alpha$. The only scalar factors are the three normalizations, whose product is $2^{-(2\alpha^2-2)}\cdot\tfrac12\cdot\tfrac12=2^{-2\alpha^2}$. The Gaussian weights, the factor $1/\alpha$ in $S$, and the lengths $s$ and $t$ sit inside the maps, so they do not appear in the constant.
