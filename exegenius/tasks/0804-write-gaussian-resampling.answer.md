Gaussian resampling replaces a [Discrete Fourier transform](discrete-fourier-transform.md) of arbitrary length $q$ by a transform of power-of-two length, so that the later steps can use butterfly layers and polynomial transforms. Here $W$ denotes the target length, a count of entries that is a power of two greater than $q$; this letter changes meaning here.

It reshapes the transforms of the [radix-digit convolution](radix-digit-convolution.md) that the integer product needs.

Gaussian resampling replaces the Fourier transforms by [multidimensional transforms](multidimensional-transform.md) whose axis lengths are powers of two. The paper states this step as <cite data-source="paper">replaces the Fourier transforms needed for this convolution by multidimensional transforms whose</cite> axis lengths are powers of two.

Gaussian resampling converts the lengths for the [synthetic polynomial transforms](synthetic-transforms.md) into powers of two. <cite data-source="paper">The transform lengths needed for the integer product are pairwise coprime</cite>, whereas the synthetic <cite data-source="paper">transforms use powers of two.</cite>

The sources leave the motive implicit. A transform whose length is a power of two splits into levels of two-point butterflies. When its length divides $2r$, its roots of unity are powers of $y$ in $\mathbb{C}[y]/(y^r+1)$, because $y^{2r}=1$, and multiplying by such a root is a signed shift: <cite data-source="paper">multiplication by such a root is a signed shift of the</cite> coefficient list.

Let $\sigma$ be the Gaussian width, an integer with $2\le\sigma$ and $\sigma^2<p$, where $p>100$ is the precision; this letter changes meaning here. Gaussian resampling requires its lengths to be [coprime](coprime.md), $\gcd(q,W)=1$. It also requires $W/q-1>p/\sigma^4$, and <cite data-source="paper">Lemma 19 (Resampling without executing the two permutations)</cite> states the identity below. For a real $x$, the Gaussian weight $\exp(-\pi x^2/\sigma^2)$ is near 1 when $|x|$ is small against $\sigma$, and near 0 otherwise.

Gaussian resampling measures contraction with the [array norm](array-norm.md). <cite data-source="paper">The vector norm is the maximum modulus</cite> of a vector's entries. A linear map $L$ is a contraction when $\|L\|\le1$, where $\|L\|=\sup_{\|u\|\le1}\|Lu\|$.

For a length-$q$ vector $u$ with entries $u_j$ ($0\le j<q$, indices read modulo $q$) and an output index $k$ with $0\le k<W$ (this letter changes meaning here), let $\Psi$ and $\Xi$ be the maps defined by the weighted sums below, where $\Psi$ gathers the inputs $j$ near $qk/W$ and $\Xi$ spreads entry $j$ over the outputs $k$ near $Wj/q$:
$$(\Psi u)_k=\frac1\sigma\sum_{j\in\mathbb Z}\exp\Big(-\pi\sigma^{-2}\big(j-\tfrac{qk}{W}\big)^2\Big)u_j,\qquad (\Xi u)_k=\sum_{j\in\mathbb Z}\exp\Big(-\pi\sigma^{2}\big(\tfrac{Wj}{q}-k\big)^2\Big)u_j.$$

Let $\mathcal J$ take, for $0\le j<q$, entry $\lfloor Wj/q+\tfrac12\rfloor$ of a length-$W$ vector, the integer nearest $Wj/q$ with ties upward. Let $\Upsilon$ multiply entry $j$ by $\exp\big(\pi\sigma^2(Wj/q-\lfloor Wj/q+\tfrac12\rfloor)^2\big)$, which cancels the weight of $\Xi$ at the selected output. Set $\mathcal N=\mathcal J\,\Xi\,\Upsilon$, a map from length $q$ to length $q$. In $(\mathcal N u)_j$, <cite data-source="paper">the summand with index j is exactly uj</cite>, and the other summands are the error. <cite data-source="paper">Gaussian identity and inverse estimate proved in [15, Theorem 4.2 and Lemma 4.6] give</cite> $\|\mathcal N-I\|<2^{-\sigma^2(W/q-1)}$. Since $\sigma^2(W/q-1)>p/\sigma^2>1$, <cite data-source="paper">Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series.</cite> So $\mathcal N^{-1}=\sum_{l\ge0}(I-\mathcal N)^l$ and $\|\mathcal N^{-1}\|\le2$.

Let $\Pi_q$ and $\Pi_W$ be the coordinate permutations $(\Pi_q u)_j=u_{Wj \bmod q}$ and $(\Pi_W u)_k=u_{-qk \bmod W}$. For $q=5$ and $W=8$, $\Pi_5$ sends $(u_0,\dots,u_4)$ to $(u_0,u_3,u_1,u_4,u_2)$, since $8j \bmod 5$ runs through $0,3,1,4,2$.

Let $F_q$ and $F_W$ be the normalized transforms of lengths $q$ and $W$. Writing $\mathcal E=\Psi/2$ and $\mathcal U=2^{1-2\sigma^2}\,\Upsilon\mathcal N^{-1}\mathcal J$, the identity reads

$$\Pi_qF_q=2^{2\sigma^2}\,\mathcal U\,\Pi_WF_W\,\mathcal E.$$

<cite data-source="paper">The proof of Proposition 4.7(i) in the cited paper gives</cite> $\|\mathcal E\|<3/4$ and $\|\mathcal U\|<1$. The selection map $\mathcal J$ is the paper's $C$, and <cite data-source="paper">Because ∥C∥ = 1, both are contractions.</cite>
