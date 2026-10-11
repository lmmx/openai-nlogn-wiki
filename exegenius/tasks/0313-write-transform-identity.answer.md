This identity computes its transforms by [Gaussian resampling](gaussian-resampling.md), which replaces a transform of arbitrary length by transforms whose axis lengths are powers of two. It is the resampling step of [Integer multiplication below n log n](main-theorem.md), and it keeps the two coordinate permutations inside the transform formula, so they cancel across a convolution.

The usual implementation of Gaussian resampling <cite data-source="paper">sorts twice on each coordinate.</cite> This identity keeps both permutations in the formula, so they need not be <cite data-source="paper">executed as separate full sorts.</cite>

The sides differ: <cite data-source="paper">The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic</cite> transforms have power-of-two lengths. The identity pairs a length-$s$ transform with a length-$t$ one.

Each permutation is defined by [congruence](congruence-modulo.md) of positions: $(P_su)_j=u_{tj}$ and $(P_tw)_k=w_{-sk}$, with indices taken modulo the length, where $u$ and $w$ are complex vectors. For example, with $s=3$ and $t=5$, $P_3$ sends $u$ to $(u_0,u_2,u_1)$.

The identity depends on $s$ and $t$ being [coprime](coprime.md), making both permutations bijections. Let $\gcd(s,t)$ be the greatest common divisor. If $\gcd(s,t)=1$, Bézout's identity gives $\chi$ with $\chi t\equiv 1 \pmod s$, an inverse of $t$ modulo $s$. Then $tj\equiv tj'$ forces $j\equiv j'$, so $j\mapsto tj$ is one-to-one. Each permutation reorders entries by a [bijection](bijection.md) of positions.

The identity is built from two [linear maps](linear-algebra-basics.md): $A$ is a linear contraction from length-$s$ to length-$t$ vectors, and $B_0$ goes back (the lemma's letters). A linear map $\Psi$ is a contraction when $\|\Psi u\|\le\|u\|$, where $\|u\|$ is the largest modulus of an entry of $u$. For example, $u\mapsto(u_0+u_1)/2$ is one. Lemma 19 states: <cite data-source="paper">There are linear contractions A : Cs → Ct and B0 : Ct → Cs satisfying</cite>
$$P_sF_s=2^{2\alpha^2}\,B_0\,P_tF_t\,A.$$
The Gaussian identity reads <cite data-source="paper">TPs Fs = Pt Ft S,</cite> that is, $TP_sF_s=P_tF_tS$. Let $\Gamma$ select the coordinates nearest $tj/s$, and let $N=\Gamma T\Lambda$, a map from length-$s$ vectors to themselves, where $\Lambda$ is a [diagonal scaling](diagonal-scaling.md).

$\|N-I\|$ is the operator norm, the largest $\|(N-I)u\|$ over $\|u\|\le1$; the source gives <cite data-source="paper">∥N − I∥ < 2.01e−πα θ/2</cite>. <cite data-source="paper">Since α2 < p and θ > p/α4 , we have</cite> $\alpha^2\theta>p/\alpha^2>1$, which is why the lemma needs $\theta>p/\alpha^4$. <cite data-source="paper">Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series.</cite> If $\|E\|<1$, the Neumann series $\sum_{k\ge 0}(-E)^k$ inverts $I+E$.

Put $\Upsilon=\Lambda N^{-1}\Gamma$: the proof builds its left inverse from the [diagonal scaling](diagonal-scaling.md) $\Lambda$. It is a left inverse of $T$, since $\Gamma T=N\Lambda^{-1}$ gives $\Upsilon T=\Lambda N^{-1}N\Lambda^{-1}=I$. Multiplying the Gaussian identity by $\Upsilon$ gives $P_sF_s=\Upsilon P_tF_tS$; with $A=S/2$ and $B_0=2^{-(2\alpha^2-1)}\Upsilon$, this is the identity above.

The original proof uses two [label-and-sort operations](stable-radix-sort.md), one for $P_t$ and one for $P_s^{-1}$, <cite data-source="paper">each costing O(tp log t).</cite> This identity avoids the [label-and-sort operations](stable-radix-sort.md), since $P_s$ and $P_t$ remain in the formula.

Permutations pass through pointwise products: for a coordinate permutation $\Pi$ and entrywise product $\cdot$, $(\Pi u)\cdot(\Pi w)=\Pi(u\cdot w)$, because <cite data-source="paper">a coordinate permutation commutes with pointwise</cite> products. The retained permutation is $R$, with $(R_cz)_j=z_{cj}$ for a unit $c$ modulo $s$ on each axis. The identity cancels its permutations through the [opposite transform](opposite-transform.md) $F_s^+$, the opposite-sign transform. <cite data-source="paper">Each ti is a unit modulo si , so tensoring this identity gives Fs+ R = R−1 Fs+ and hence RFs+ R = Fs+</cite>. So
$$RF_s^+\big((RF_su)\cdot(RF_sv)\big)=RF_s^+R\,(F_su\cdot F_sv)=F_s^+(F_su\cdot F_sv),$$
and $R$ disappears.
