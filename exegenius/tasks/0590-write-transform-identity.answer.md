This identity computes its transforms by [Gaussian resampling](gaussian-resampling.md), which replaces a transform of arbitrary length by transforms whose axis lengths are powers of two. It is the resampling step of [Integer multiplication below n log n](main-theorem.md), and it keeps the two coordinate permutations inside the transform formula, so they cancel across a convolution.

The usual implementation of Gaussian resampling <cite data-source="paper">sorts twice on each coordinate.</cite> This identity keeps both permutations in the formula, so they need not be <cite data-source="paper">executed as separate full sorts.</cite> The original proof uses two [label-and-sort operations](stable-radix-sort.md), <cite data-source="paper">each costing O(tp log t).</cite> This identity avoids the [label-and-sort operations](stable-radix-sort.md), since $P_s$ and $P_t$ remain in the formula.

The integer product needs lengths of a different kind: <cite data-source="paper">The transform lengths needed for the integer product are pairwise coprime,</cite> whereas the synthetic <cite data-source="paper">transforms use powers of two.</cite> The identity depends on $s$ and $t$ being [coprime](coprime.md), so it pairs a transform of length $s$ with one of length $t$. Here $F_s$ is the normalized discrete Fourier transform of length $s$, $(F_su)_k=\frac1s\sum_{j=0}^{s-1}u_je^{-2\pi ijk/s}$, and $F_t$ is the one of length $t$.

Each permutation is defined by [congruence](congruence-modulo.md) of positions: $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$, with indices taken modulo the length, where $u$ has length $s$ and $v$ has length $t$. For $s=3$ and $t=5$, $P_s$ sends $u$ to $(u_0,u_2,u_1)$.

Let $\gcd(s,t)=1$. By [Bézout's identity](bezout-identity.md) there is an integer $\chi$ with $\chi t\equiv 1 \pmod s$ (the letter $\chi$ changes meaning here). If $tj\equiv tj'\pmod s$ for positions $j,j'$ in $\{0,\dots,s-1\}$, multiplying by $\chi$ gives $j\equiv j'$, so $j\mapsto tj$ is one-to-one, hence a permutation. Each permutation reorders entries by a [bijection](bijection.md) of positions.

The identity is built from two [linear maps](linear-algebra-basics.md). $A$ maps $\mathbb{C}^s$ to $\mathbb{C}^t$ and $B_0$ maps back (here $A$ changes meaning from the machine of other pages). A linear map $\Psi$ is a contraction when $\|\Psi u\|\le\|u\|$, where $\|u\|$ is the largest modulus of an entry of $u$.

Write $\theta=t/s-1$ (the letter $\theta$ changes meaning here). The lemma of the source assumes $2\le\alpha<p$, $\gcd(s,t)=1$ and $\theta>p/\alpha^4$, and states: <cite data-source="paper">There are linear contractions A : Cs → Ct and B0 : Ct → Cs satisfying</cite>
$$P_sF_s=2^{2\alpha^2}\,B_0\,P_tF_t\,A.\qquad(33)$$

The proof starts from the Gaussian identity, which the source proves: <cite data-source="paper">TPs Fs = Pt Ft S,</cite> that is, $\Gamma P_sF_s=P_tF_t\Sigma$, for the resampling maps $\Gamma,\Sigma:\mathbb{C}^s\to\mathbb{C}^t$ (the source's $T$ and $S$).

Let $N$ be the near-identity map of Gaussian resampling on $\mathbb{C}^s$. The source's Gaussian estimate gives <cite data-source="paper">∥N − I∥ < 2.01e−πα θ/2</cite>, which is below $2.01e^{-\pi/2}<1/2$ once $\alpha^2\theta>1$. <cite data-source="paper">Since α2 < p and θ > p/α4 , we have</cite> $\alpha^2\theta>p/\alpha^2>1$: the first inequality multiplies $\theta>p/\alpha^4$ by $\alpha^2$, the second uses $\alpha^2<p$. The invertibility of $N$ is proved with the [Neumann series](neumann-series.md): writing $N=I+E$ with $\|E\|<1$, the series $\sum_{k\ge 0}(-E)^k$ inverts $N$.

The proof builds its left inverse from a [diagonal scaling](diagonal-scaling.md) and $N^{-1}$ and a coordinate selection: a linear map $\Upsilon$ with $\Upsilon\Gamma=I$. Applying $\Upsilon$ to the Gaussian identity gives $P_sF_s=\Upsilon P_tF_t\Sigma$. Scaling $\Sigma$ by $1/2$ and $\Upsilon$ by $2^{-(2\alpha^2-1)}$ gives $A=\Sigma/2$ and $B_0=2^{-(2\alpha^2-1)}\Upsilon$, which are contractions by the source's norm bounds. Since $2^{2\alpha^2}\cdot 2^{-(2\alpha^2-1)}\cdot\tfrac12=1$, this is (33).

Permutations pass through pointwise products. For vectors $u,u'$, the pointwise product $u\cdot u'$ has entries $u_ju'_j$. For a coordinate permutation $\Pi$, which rearranges entries by position, $(\Pi u)\cdot(\Pi u')=\Pi(u\cdot u')$, because <cite data-source="paper">a coordinate permutation commutes with pointwise</cite> products.

For a unit $c$ modulo $s$ (the letter $c$ changes meaning here), the retained permutation $\Pi_c$ sends $z$ to the vector with $(\Pi_cz)_j=z_{cj}$, indices taken modulo $s$. The identity cancels its permutations through the [opposite transform](opposite-transform.md) $F_s^+$, the transform with the exponent's sign reversed: $(F_s^+u)_k=\frac1s\sum_{j}u_je^{+2\pi ijk/s}$. Substituting $h=ck$, a bijection since $c$ is a unit, shows $F_s^+\Pi_c=\Pi_{c^{-1}}F_s^+$, hence $\Pi_cF_s^+\Pi_c=F_s^+$. With the commutation above,

$$\Pi_cF_s^+\big((\Pi_cF_su)\cdot(\Pi_cF_su')\big)=\Pi_cF_s^+\Pi_c\,(F_su\cdot F_su')=F_s^+(F_su\cdot F_su'),$$

so $\Pi_c$ disappears: the retained permutation is cancelled, not executed.
