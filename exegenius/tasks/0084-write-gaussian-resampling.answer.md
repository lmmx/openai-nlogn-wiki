Gaussian resampling rewrites a Fourier transform of length $s$, the number of its coordinates, as a transform with target length $t>s$ and power-of-two axis lengths, keeping the source and target coordinate permutations inside the identity. It is needed because the integer product's transform lengths are pairwise coprime, while the synthetic transforms use powers of two. <cite data-source="paper">Gaussian resampling connects these two shapes.</cite>

Gaussian resampling rewrites each [Discrete Fourier transform](fourier-transform.md) of length $s$ as follows. Let $F_q$ be the normalized transform of length $q$, $(F_q u)_k=\frac1q\sum_{j=0}^{q-1}u_j e^{-2\pi i jk/q}$.

Let $\alpha\ge2$ be a fixed integer, the Gaussian width.

$P_s$ and $P_t$ are the maps $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$, where $u$ has length $s$, $v$ has length $t$ (here $v$ is new, not its earlier meaning), and indices are taken modulo $s$ and $t$. With $\gcd(s,t)=1$, both only rearrange coordinates.

A linear map $L$ is a *contraction* if $\|Lu\|\le\|u\|$ for every $u$, where $\|u\|$ is the largest modulus of an entry of $u$.

$G$ is the map whose $k$-th output is a Gaussian-weighted sum centred at $sk/t$, and $T$ weights each input $u_j$ by a Gaussian centred at $tj/s$:
$$(Gu)_k=\frac1\alpha\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (Tu)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(tj/s-k)^2}u_j,$$
with $u_j$ read modulo $s$. Harvey and van der Hoeven prove the exact identity $TP_sF_s=P_tF_tG$ (their Theorem 4.2), but $T$ is not square, so we build a left inverse.

Let $E$ multiply entry $j$ by $e^{\pi\alpha^2\beta_j^2}$, where $q_j=\lfloor tj/s+\tfrac12\rfloor$ is the integer nearest $tj/s$ (ties rounded up) and $\beta_j=tj/s-q_j$, so $|\beta_j|\le\tfrac12$. Let $C$ map $\mathbb C^t$ to $\mathbb C^s$ by $(Cv)_j=v_{q_j}$, and let $N=CTE$, a map from $\mathbb C^s$ to itself.

In $(Nu)_j$ the term with index $j$ is exactly $u_j$, since $E$ cancels the Gaussian factor at $q_j$. The Neumann series $\sum_{m\ge0}(I-N)^m$, where $I$ is the identity map, converges to $N^{-1}$ when $\|I-N\|<\tfrac12$, so $\|N^{-1}\|\le2$. The other terms are small: $\|I-N\|<2^{-\alpha^2(t/s-1)}<\tfrac12$ under the sources' hypotheses.

Since $CT=NE^{-1}$, we have $EN^{-1}CT=I$, so multiplying the identity by $EN^{-1}C$ on the left gives $P_sF_s=EN^{-1}CP_tF_tG$. Let $R=\tfrac12G$ and $Q=2^{1-2\alpha^2}EN^{-1}C$, with $R$ mapping $\mathbb C^s$ to $\mathbb C^t$ and $Q$ mapping back. Then $P_sF_s=2^{2\alpha^2}QP_tF_tR$: the factor $2^{2\alpha^2}$ undoes the constants in $R$ and $Q$.

Both are contractions. $\|R\|<\tfrac34$ by the bound in Harvey and van der Hoeven's Proposition 4.7(i), and $\|Q\|\le1$, since $\|C\|\le1$, $\|N^{-1}\|\le2$ and $\|E\|\le e^{\pi\alpha^2/4}\le2^{2\alpha^2-2}$ for $\alpha\ge2$.

The usual implementation sorts coordinates twice. <cite data-source="paper">We retain both permutations in the transform formula and compute that formula directly.</cite>

In the application $t=2^a$ is a power of two, so $F_t$ has power-of-two length. Thus Gaussian resampling expresses each source transform through a [Multidimensional transform with power-of-two axes](multidim-transform.md).
