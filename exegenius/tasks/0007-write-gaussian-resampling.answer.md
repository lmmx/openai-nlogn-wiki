Gaussian resampling replaces a [discrete Fourier transform](discrete-fourier-transform.md) of arbitrary length by transforms whose axis lengths are powers of two. <cite data-source="paper">it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose</cite>

Integer multiplication needs this, since the lengths its transforms require are pairwise coprime rather than powers of two. Gaussian resampling replaces the transforms for the [radix-digit convolution](radix-digit-convolution.md) of two integers by transforms on power-of-two axes.

Let $s$ and $t$ be the number of coordinates of source and target vectors. Write $F_s$ and $P_s$ for the normalized Fourier transform and the coordinate permutation of length-$s$ vectors, and likewise $F_t$ and $P_t$ for length-$t$ vectors.

The identity uses two Gaussian-weighted maps $S,T$ from length-$s$ to length-$t$ vectors. The parameter $\alpha$ sets the width of the Gaussian weights. For a length-$s$ vector $u$ with entries $u_j$, $0\le j<s$, and an index $0\le k<t$, they are

$$(Su)_k=\frac{1}{\alpha}\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (Tu)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(tj/s-k)^2}u_j,$$

where subscripts are taken modulo $s$. $S$ gathers the entries of $u$ near the position $sk/t$, and $T$ spreads each entry $u_j$ over the targets near $tj/s$.

Let $\ell_j$ be the integer nearest to $tj/s$, with ties rounded upward, for $0\le j<s$, and let $\beta_j=tj/s-\ell_j$. Let $C:\mathbb C^t\to\mathbb C^s$ be the map $(Cv)_j=v_{\ell_j}$ that selects these coordinates, let $D:\mathbb C^s\to\mathbb C^s$ be the diagonal map $(Du)_j=e^{\pi\alpha^2\beta_j^2}u_j$, and set $N=CTD$, an operator on length-$s$ vectors.

Expanding $(Nu)_j=\sum_i e^{-\pi\alpha^2(ti/s-\ell_j)^2}e^{\pi\alpha^2\beta_i^2}u_i$, the term $i=j$ has $ti/s-\ell_j=\beta_j$, so its two exponentials cancel and the term equals $u_j$. The Gaussian weight at the selected coordinate thus cancels the diagonal factor, and $N$ differs from the identity only through the other terms.

The paper uses a second parameter $\theta$, chosen so that $\alpha^2\theta>1$. With this choice the other terms give $\|N-I\|<1/2$ in the operator norm for the maximum-modulus vector norm. <cite data-source="paper">Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series.</cite>

A Neumann series inverts $N$: write $N=I-E$ with $\|E\|<1/2$. Then $\sum_{m\ge0}E^m$ converges, since $\|E^m\|\le\|E\|^m$, and its sum is $N^{-1}$, which has norm less than $2$.

The other sub-step is the Gaussian identity $TP_sF_s=P_tF_tS$. It says that applying $F_s$, then $P_s$ and $T$, gives the same result as applying $S$, then $F_t$ and $P_t$. The Fourier transform of a Gaussian is again a Gaussian, which is why such weights move between the two sets of frequencies. Its proof is in Harvey and van der Hoeven <cite data-source="paper">proved in [15, Theorem 4.2 and Lemma 4.6]</cite>.

Inverting $N$ turns this identity into the form used in the [transform identity with retained permutations](transform-identity.md).
