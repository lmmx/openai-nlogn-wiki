Gaussian resampling is an identity that replaces the [Discrete Fourier transform](discrete-fourier-transform.md) of an arbitrary length by transforms whose lengths are powers of two. It serves the [Radix-digit convolution](radix-digit-convolution.md) of digit vectors, which needs such transforms. The identity is restricted to [coprime integers](coprime-integers.md) $s<t$, where $s$ is the number of coordinates of the source vector and $t$ the number of coordinates of the target. Write $F_s$ and $F_t$ for the normalized transforms of length $s$ and $t$, that is, $F_q$ with $q=s$ or $q=t$.

Let $\theta=t/s-1$ be the relative excess of $t$ over $s$. The identity needs $\theta>p/\alpha^4$, where $\alpha\ge 2$ is an integer Gaussian width and $p$ is the integer precision of the numerical approximation. The permutations $P_s$ and $P_t$ are defined using [modular arithmetic](modular-arithmetic.md) on their indices, with subscripts taken modulo the length:
$$(P_s u)_j=u_{tj},\qquad (P_t v)_k=v_{-sk}.$$
Here $u$ has $s$ coordinates and $v$ has $t$.

The two Gaussian maps $S$ and $T$ are built from the [Gaussian function](gaussian-function.md).
$$(Su)_k=\frac{1}{\alpha}\sum_{j\in\mathbb{Z}} e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (Tu)_k=\sum_{j\in\mathbb{Z}} e^{-\pi\alpha^{2}(tj/s-k)^2}u_j.$$
Harvey and van der Hoeven's Gaussian identity states $TP_sF_s=P_tF_tS$: transforming on the source grid and then applying $T$ agrees with applying $S$ and then transforming on the target grid. <cite data-source="paper">Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven</cite>

$C$ maps length-$t$ vectors to length-$s$ vectors by taking, for each $j$ with $0\le j<s$, the entry at $\mu_j$, the integer nearest to $tj/s$. The diagonal map $D$ is $(Du)_j=e^{\pi\alpha^2(tj/s-\mu_j)^2}u_j$ on length-$s$ vectors, which cancels the Gaussian factor of $T$ at that entry. Put $N=CTD$. Its $j$th entry is $u_j$ plus other terms, so $N$ is close to $I$, the identity map, which leaves every vector unchanged.

The size of $N-I$ is measured by its [operator norm](operator-norm.md), $\|N-I\|$. The sources bound it by $2^{-\alpha^2\theta}$. <cite data-source="paper">∥N − I∥ < 2.01e−πα θ/2 < 2−α θ</cite> The sources assume $\alpha^2<p$, so $\alpha^2\theta>p/\alpha^2>1$ and $\|N-I\|<1/2$. <cite data-source="paper">Since α2 < p and θ > p/α4</cite> Here $\nu$ is the summation index, and its $\nu$th term has norm at most $2^{-\nu}$, so the series converges. Hence $N$ is invertible by the Neumann series $N^{-1}=\sum_{\nu\ge 0}(I-N)^\nu$.

Since $N=CTD$, we have $CT=ND^{-1}$, so $DN^{-1}C$ is a left inverse of $T$: $DN^{-1}CT=I$. Applying it to the Gaussian identity gives $DN^{-1}CP_tF_tS=P_sF_s$. The two Gaussian maps relate the two frequency grids, and this inverse turns the identity into one for $P_sF_s$ alone.

Write $D'=2^{-(2\alpha^2-2)}D$ for the scaled diagonal map. $A$ maps length-$s$ vectors to length-$t$ vectors, and $B_0$ maps them back, where $A=S/2$ and $B_0=D'N^{-1}C/2$. Both are contractions, linear maps of norm at most one. The sources bound $\|S/2\|<3/4$, $\|N^{-1}/2\|<7/8$ and <cite data-source="paper">∥D′ ∥ < 1</cite>, and $\|C\|=1$ because $C$ only copies entries. So $\|A\|<3/4$ and $\|B_0\|<7/8$.

The scalars $2^{-(2\alpha^2-2)}$, $1/2$ and $1/2$ multiply to $2^{-2\alpha^2}$, so $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$. This is the one-dimensional identity $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$. The constant $2^{2\alpha^2}$ is uniform in $p,s,t,\alpha$ because the bounds $3/4$, $7/8$ and $1$ are fixed numbers, and $\alpha$ enters only through the scalar $2^{-(2\alpha^2-2)}$ in $D'$, which the constant cancels. <cite data-source="paper">The constant is uniform in p, s, t, α.</cite>
