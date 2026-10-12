Gaussian resampling replaces a [discrete Fourier transform](discrete-fourier-transform.md) of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies. It replaces the transforms for the [radix-digit convolution](radix-digit-convolution.md) of two integers by such transforms. <cite data-source="paper">replaces the Fourier transforms needed for this convolution by multidimensional transforms whose</cite>

Let $s$ and $t$ be the numbers of coordinates of source and target vectors, with $\gcd(s,t)=1$ and $\theta=t/s-1$, the relative gap between the lengths. Here $u$ is a length-$s$ source vector, $b$ a length-$t$ target vector, and $j$ and $k$ index their entries. Let $F_s$ and $P_s$ be the normalized Fourier transform and the coordinate permutation $(P_su)_j=u_{tj}$ on length-$s$ vectors, and let $F_t$ and $P_t$ be the same on length-$t$ vectors with $(P_tb)_k=b_{-sk}$.

$S$ and $T$ are Gaussian-weighted maps from length-$s$ to length-$t$ vectors. The parameter $\alpha$ sets the width of their weights, which are bell-shaped functions that decay quickly away from their centres. $S$ gathers the entries of $u$ near $sk/t$, and $T$ spreads each $u_j$ over the targets near $tj/s$:
$$(Su)_k=\frac1\alpha\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (Tu)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(tj/s-k)^2}u_j,$$
where $u_j=u_{j \bmod s}$.

For $0\le j<s$, let $\ell_j$ be the integer nearest $tj/s$, ties rounded up, and $\beta_j=tj/s-\ell_j$. Let $C$ select coordinates, $(Cb)_j=b_{\ell_j}$, let $D$ be diagonal with $(Du)_j=e^{\pi\alpha^2\beta_j^2}u_j$, and set $N=CTD$. Expanding,
$$(Nu)_j=\sum_{i\in\mathbb Z}e^{-\pi\alpha^2(ti/s-\ell_j)^2}e^{\pi\alpha^2\beta_i^2}u_i,$$
where $i$ is a summation index over all integers and $\beta_i$ depends only on $i \bmod s$. The term $i=j$ has $ti/s-\ell_j=\beta_j$, so its exponentials cancel and it equals $u_j$. The other terms form $N-I$, whose size is measured in the [operator norm](operator-norm.md) for the maximum-modulus vector norm.

These other terms are small. Harvey and van der Hoeven bound them by $2^{-\alpha^2\theta}$, which shrinks as $\theta$ grows. <cite data-source="paper">Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series.</cite> Here $p$ is the integer precision of the cited lemma. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, the bound is below $1/2$, as $\alpha^2\theta>p/\alpha^2>1$.

Write $N=I-E$, where $E=I-N$ is the error, and $\|E\|<1/2$. The Neumann series $\sum_{m\ge0}E^m$, with $m$ its summation index, has partial sums of norm at most $1/(1-\|E\|)<2$, since $\|E^m\|\le\|E\|^m$. Here $M$ is the last index of the partial sum $\sum_{m=0}^{M}E^m$, which multiplied by $I-E$ telescopes to $I-E^{M+1}$. Since $\|E^{M+1}\|\to0$, the series sums to $N^{-1}$, whose norm is less than $2$.

The Gaussian identity $TP_sF_s=P_tF_tS$ rests on Poisson summation: a sum of Gaussians over the integers is a Fourier series whose coefficients are Gaussians of reciprocal width. The weights in $S$ have Fourier transform constant $\alpha$, which cancels the $1/\alpha$ in $S$. The full bookkeeping is in Harvey and van der Hoeven, <cite data-source="paper">proved in [15, Theorem 4.2 and Lemma 4.6]</cite>.

Multiply $TP_sF_s=P_tF_tS$ on the left by $C$, and use $CT=ND^{-1}$, which holds since $D$ is invertible. This gives $ND^{-1}P_sF_s=CP_tF_tS$. Multiplying on the left by $N^{-1}$ and then by $D$ gives $P_sF_s=DN^{-1}C\,P_tF_tS$. This has the form $P_sF_s=BP_tF_tA$, where $A=S$ and $B=DN^{-1}C$ are maps. It is the form used on the [transform identity with retained permutations](transform-identity.md) page.
