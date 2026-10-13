Gaussian resampling is a rewriting of a Fourier transform as a transform with power-of-two axis lengths, with the source and target coordinate permutations kept inside the identity. The integer product needs pairwise coprime transform lengths, while the synthetic transforms use powers of two. <cite data-source="paper">Gaussian resampling connects these two shapes.</cite>

Let $s$ be the length of the source transform, the number of coordinates it acts on. Let $t>s$ be the target length, with $\gcd(s,t)=1$. Here $F_q$ is the transform of length $q$.

$$(F_q u)_k=\frac1q\sum_{j=0}^{q-1}u_j e^{-2\pi i jk/q}.$$

Gaussian resampling rewrites each [Discrete Fourier transform](fourier-transform.md) of length $s$ as follows. Let $P_s$ and $P_t$ be the coordinate permutations $(P_s u)_j=u_{tj}$ and $(P_t v)_k=v_{-sk}$, with indices taken modulo $s$ and $t$.

Here $\alpha$ is a fixed integer parameter that sets the width of the Gaussian weights below. The maps $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ are contractions, that is, linear maps that never increase the maximum-modulus norm of a vector.

The claim is the identity

$$P_sF_s=2^{2\alpha^2}B_0P_tF_tA.$$

Read the left side as transforming by $F_s$ and then permuting by $P_s$. The right side maps the input to length $t$ by $A$, applies $F_t$, permutes by $P_t$, and returns to length $s$ by $B_0$. The factor $2^{2\alpha^2}$ absorbs the normalizations of the maps.

The proof builds $A$ and $B_0$ from Gaussian-weighted resampling. Each output coordinate of one resampling map is a sum over all integers $j$ of $e^{-\pi\alpha^{-2}(j-sk/t)^2}$ times an input entry, a Gaussian weight centred at $sk/t$. An exact Fourier identity relates these sums to $P_sF_s$ and $P_tF_t$. A correction map close to the identity is inverted by a Neumann series, which gives the contraction bounds.

Its usual implementation sorts twice on each coordinate. This is the point of the identity. <cite data-source="paper">We retain both permutations in the transform formula and compute that formula directly.</cite>

Thus Gaussian resampling expresses each source transform through a [Multidimensional transform with power-of-two axes](multidim-transform.md). The sources compute approximations to $A$ and $B_0$ on Gaussian dyadic inputs, with error bounds; this page states only the exact identity.
