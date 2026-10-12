The transform identity with retained permutations is an exact identity relating two Fourier transforms of different lengths, with both coordinate permutations kept as explicit factors. It is obtained by inverting the [Gaussian resampling](gaussian-resampling.md) identity, which keeps both permutations. <cite data-source="paper">Its usual implementation sorts twice on each coordinate.</cite> Keeping the permutations as factors lets them cancel across a convolution instead of being executed as sorts.

The integer $s$ is the number of coordinates of a source vector. The integer $t$ is the number of coordinates of a target vector, with $2\le s<t$ and $\gcd(s,t)=1$. The integer $\alpha\ge 2$ sets the width of the Gaussian weights. $F_s$ is the normalized Fourier transform of length $s$, and $F_t$ that of length $t$. $P_s$ is the permutation $(P_su)_j=u_{tj}$ of length-$s$ vectors, with subscripts taken modulo $s$. $P_t$ is the permutation $(P_tv)_k=v_{-sk}$ of length-$t$ vectors, with subscripts taken modulo $t$.

A linear contraction is a linear map of norm at most one. $A$ is a linear contraction from length-$s$ to length-$t$ vectors. $B_0$ is a linear contraction from length-$t$ to length-$s$ vectors. The step claims
$$P_sF_s=2^{2\alpha^2}B_0P_tF_tA,$$
and its proof sits under <cite data-source="paper">Lemma 19 (Resampling without executing the two permutations)</cite>.

The proof uses two Gaussian-weighted maps $S$ and $T$ from length-$s$ to length-$t$ vectors, defined by the sums below.
$$(Su)_k=\frac{1}{\alpha}\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (Tu)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(tj/s-k)^2}u_j.$$
They satisfy the Gaussian identity $TP_sF_s=P_tF_tS$.

For $0\le j<s$, $q_j$ is the integer nearest $tj/s$, with ties rounded upward. The map $C$ selects the coordinates $q_0,\dots,q_{s-1}$ from a length-$t$ vector. The map $D$ is the diagonal map $(Du)_j=e^{\pi\alpha^2(tj/s-q_j)^2}u_j$ on length-$s$ vectors, whose factor cancels the Gaussian factor of $T$ at $q_j$.

The operator $N=CTD$ is near the identity. Its $j$-th output is $u_j$ plus a small error, so $\|N-I\|<1/2$. Hence $N$ is invertible, with $N^{-1}=\sum_{k\ge 0}(I-N)^k$ by the Neumann series.

Since $(DN^{-1}C)T=I$, the map $DN^{-1}C$ is a left inverse of $T$. Applying it to the Gaussian identity gives $DN^{-1}CP_tF_tS=P_sF_s$.

Scaled copies $S'=S/2$, $J'=N^{-1}/2$ and $D'=2^{-(2\alpha^2-2)}D$ have norms $\|S'\|<3/4$, $\|J'\|<7/8$ and $\|D'\|<1$. With $\|C\|=1$, this makes $A=S'$ and $B_0=D'J'C$ contractions. The three normalizations multiply to $2^{-(2\alpha^2-2)}\cdot 2^{-1}\cdot 2^{-1}=2^{-2\alpha^2}$, so
$$B_0P_tF_tA=2^{-2\alpha^2}DN^{-1}CP_tF_tS=2^{-2\alpha^2}P_sF_s,$$
which is the claimed identity.

The constant is a power of two that depends only on $\alpha$, because the only scalar factors are these three normalizations. The $s$- and $t$-dependence lies in $C$, $T$, $D$ and $N$, none of which carries such a factor.
