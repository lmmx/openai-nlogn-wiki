Gaussian resampling replaces a [Discrete Fourier transform](discrete-fourier-transform.md) of arbitrary length by a transform whose length is a power of two. It reshapes the transforms of the [radix-digit convolution](radix-digit-convolution.md) into [multidimensional transforms](multidimensional-transform.md) with power-of-two axes, so that the later steps can use butterfly layers and polynomial transforms.

Let $s$ be the number of entries in the source vector, the transform being replaced, and $t$ the number of entries in the resampled vector, a power of two greater than $s$. The count $\ell$ is the number of halvings, so a length is $2^\ell$.

Gaussian resampling converts the lengths for the [synthetic polynomial transforms](synthetic-transforms.md) into powers of two. <cite data-source="paper">The transform lengths needed for the integer product are pairwise coprime</cite>, so the lengths must change. A transform of length $2^\ell$ splits into two transforms of length $2^{\ell-1}$, one on the even-indexed and one on the odd-indexed entries, combined by one layer of two-point butterflies.

Let $u$ be a generic vector of length $s$, $v$ one of length $t$, and $j$, $k$ positions; these letters are reused here.

<cite data-source="paper">The vector norm is the maximum modulus</cite> of its coordinates, and a linear map is a *contraction* when it never increases this norm. Its *operator norm* $\|L\|$ is the largest $\|Lu\|$ over vectors with $\|u\|\le 1$; <cite data-source="paper">All operator norms are induced by this norm</cite>. A Gaussian weight is $e^{-\pi x^2/\alpha^2}$ for a real number $x$, where $e$ is the base of the natural logarithm and the integer $\alpha$ is the width: the weight is near 1 when $x$ is small against $\alpha$ and near 0 otherwise. Let $\theta = t/s-1$ be the relative gap between the two lengths.

Define the coordinate permutations $P_s$ and $P_t$ by $(P_s u)_j = u_{tj \bmod s}$ and $(P_t v)_k = v_{-sk \bmod t}$.

Gaussian resampling requires that $s$ and $t$ be [coprime](coprime.md), $\gcd(s,t)=1$. Write $a \equiv b \pmod s$ when $s$ divides $a-b$. $P_s$ is a permutation because $tj \equiv tj' \pmod s$ forces $j \equiv j' \pmod s$: $s$ divides $t(j-j')$, and $\gcd(s,t)=1$ then gives $s \mid j-j'$. For positions $j, j'$ in $\{0,\dots,s-1\}$ this means $j=j'$. For $s=5$ and $t=8$, $P_5$ sends $(u_0,\dots,u_4)$ to $(u_0,u_3,u_1,u_4,u_2)$, since $8j \bmod 5$ runs through $0,3,1,4,2$.

<cite data-source="paper">Lemma 19 (Resampling without executing the two permutations)</cite> states the identity. It applies when <cite data-source="paper">with gcd(s, t) = 1 and</cite> <cite data-source="paper">θ := t/s − 1 > p/α4</cite>. Here $E$ maps length-$s$ vectors to length-$t$ vectors, and $U$ maps length-$t$ vectors back to length-$s$ vectors. Both are <cite data-source="paper">linear contractions</cite>. The identity is

$$P_sF_s = 2^{2\alpha^2}\,U\,P_tF_t\,E.$$

Here $\Sigma$ and $\Gamma$ are maps from length-$s$ to length-$t$ vectors, each output entry a Gaussian-weighted sum of input entries. The Gaussian resampling argument <cite data-source="paper">uses two maps</cite>. Let $N$ be the map built from $\Gamma$ and Gaussian corrections. <cite data-source="paper">Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series.</cite> Writing $N=I-X$ with $\|X\|<1/2$, the inverse is $N^{-1}=I+X+X^2+\cdots$. Inverting $N$ and scaling by constants of norm at most one then gives the contractions $E$ and $U$.
