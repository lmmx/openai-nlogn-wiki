Gaussian resampling replaces a [discrete Fourier transform](discrete-fourier-transform.md) of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies. It replaces the transforms for the [radix-digit convolution](radix-digit-convolution.md) of two integers by such transforms. <cite data-source="paper">replaces the Fourier transforms needed for this convolution by multidimensional transforms whose</cite>

Let $s$ and $t$ be the lengths of the source and target vectors, with $\gcd(s,t)=1$ and $\theta=t/s-1$ the relative gap between them. Here $s$ and $t$ are lengths, not the binary string and output index of earlier pages. Let $u$ be a length-$s$ source vector and $b$ a length-$t$ target vector, so the letters $u$ and $b$ change meaning from the integers of earlier pages. Entries of $u$ are indexed by $j$, entries of $b$ by $k$, and an index is read modulo the length, so $u_j=u_{j \bmod s}$ for every integer $j$.

Let $F_s$ and $P_s$ be the normalized Fourier transform and the coordinate permutation $(P_su)_j=u_{tj}$ on length-$s$ vectors, and let $F_t$ and $P_t$ be the transform and the permutation $(P_tb)_k=b_{-sk}$ on length-$t$ vectors.

Let $S$ and $T$ be the maps from length-$s$ to length-$t$ vectors given by
$$(Su)_k=\frac1\alpha\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (Tu)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(tj/s-k)^2}u_j.$$
The integer $\alpha$ sets the width of the Gaussian weights, which are bell-shaped functions of $j$ that decay quickly away from their centres. $S$ gathers the entries of $u$ near $sk/t$, and $T$ spreads each $u_j$ over the targets near $tj/s$.

For $0\le j<s$, let $\ell_j$ be the integer nearest $tj/s$, ties rounded up, and $\beta_j=tj/s-\ell_j$. The same rule defines $\ell_i$ and $\beta_i$ for every integer $i$, the summation index over all integers used below. Since $\ell_{i+s}=\ell_i+t$, we get $\beta_{i+s}=\beta_i$, so $\beta_i$ depends only on $i \bmod s$. For example, with $s=2$ and $t=3$, $\ell_1=2$ and $\beta_1=-\tfrac12$.

Let $C$ select coordinates, $(Cb)_j=b_{\ell_j}$, let $D$ be the diagonal map $(Du)_j=e^{\pi\alpha^2\beta_j^2}u_j$, and set $N=CTD$, a map from length-$s$ to length-$s$ vectors. Expanding,
$$(Nu)_j=\sum_{i\in\mathbb Z}e^{-\pi\alpha^2(ti/s-\ell_j)^2}e^{\pi\alpha^2\beta_i^2}u_i,$$
where $i$ is the summation index. The term $i=j$ has $ti/s-\ell_j=\beta_j$, so its two exponentials cancel and it equals $u_j$. The Gaussian weight of $T$ at the selected coordinate cancels the factor of $D$.

Here $I$ is the identity map on length-$s$ vectors. The other terms form $N-I$, whose size is measured in the [operator norm](operator-norm.md) for the maximum-modulus vector norm. Write $N=I-E$, where $E=I-N$ is the error, so $\|E\|=\|N-I\|$.

The Gaussian identity $TP_sF_s=P_tF_tS$ holds, and Poisson summation explains it: a sum over all integers of a Gaussian equals a Fourier series, which is a periodic function written as a weighted sum of complex exponentials. Harvey and van der Hoeven establish this identity and the inverse estimate $\|N-I\|<2^{-\alpha^2\theta}$ <cite data-source="paper">proved in [15, Theorem 4.2 and Lemma 4.6]</cite>.

Here $p>100$ is an integer precision parameter, and the estimate applies when $\alpha$ is an integer with $2\le\alpha<p$, $\gcd(s,t)=1$ and $\theta>p/\alpha^4$. Since $\alpha^2<p$, we get $\alpha^2\theta>p/\alpha^2>1$, so $\|E\|<2^{-\alpha^2\theta}<1/2$.

The Neumann series $\sum_{r\ge0}E^r$, with $r$ its summation index, is the operator version of the geometric series. Let $M$ be the last index of a partial sum $\sum_{r=0}^{M}E^r$. Multiplying it by $I-E=N$ telescopes to $I-E^{M+1}$. Since $\|E^r\|\le\|E\|^r$, the series converges absolutely and $\|E^{M+1}\|\to0$, so the series sums to $N^{-1}$.

Multiply $TP_sF_s=P_tF_tS$ on the left by $C$, and use $CT=ND^{-1}$, which holds since $D$ is invertible. This gives $ND^{-1}P_sF_s=CP_tF_tS$. Multiplying on the left by $N^{-1}$ and then by $D$ gives $P_sF_s=DN^{-1}C\,P_tF_tS$. This has the form $P_sF_s=BP_tF_tA$, where $A=S$ and $B=DN^{-1}C$ are linear maps. It is the form used on the [transform identity with retained permutations](transform-identity.md) page.
