Gaussian resampling expresses a Fourier transform of prime length $s$ through one of nearby power-of-two length $t$, so only power-of-two transforms need a fast algorithm.

Here $s<t<2^p$ are coprime integers, $p$ is the number of bits of precision of each real and imaginary component, and $\alpha$ is an integer with $2\le\alpha<\sqrt p$. Assume the relative gap $\theta:=t/s-1>p/\alpha^4$. Here $F_q$ is the normalised [Discrete Fourier transform](dft.md) of length $q$, and the resampling expresses $F_s$ through $F_t$. Define the permutations $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$ (coordinate indices $j$, $k$ taken modulo $s$, $t$), never executed as sorts.

There are linear contractions $A$, $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, a contraction being a norm-nonincreasing map. The resampling reduces $F_s$ to a power-of-two $F_t$, which is a [Multidimensional transforms](multidim-transform.md) over short axes.

## Exact construction

Harvey and van der Hoeven's Gaussian maps $\mathsf S,\mathsf T:\mathbb C^s\to\mathbb C^t$ (see the [Established O(n log n) multiplier](hvdh-multiplier.md)) satisfy $\mathsf TP_sF_s=P_tF_t\mathsf S$. To undo $\mathsf T$, let $q_j$ be the integer nearest $tj/s$, $\beta_j=tj/s-q_j$, let $C:\mathbb C^t\to\mathbb C^s$ copy coordinate $q_j$ into position $j$, and let $\mathsf D$ be the diagonal map $(\mathsf Du)_j=e^{\pi\alpha^2\beta_j^2}u_j$. In $N=C\mathsf T\mathsf D$ the factor in $\mathsf D$ cancels the Gaussian weight at $q_j$, so $(Nu)_j$ contains $u_j$ exactly, and the other summands form $((N-I)u)_j$. The Gaussian identity and estimate give $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$, where $N=C\mathsf T\mathsf D$ and $C$ selects the nearest coordinates <cite data-source="paper">\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}.</cite>.

Since $\alpha^2<p$ and $\theta>p/\alpha^4$, $\alpha^2\theta>p/\alpha^2>1$, so $\|N-I\|<1/2$ and $N$ is invertible by the Neumann series $N^{-1}=\sum_i(-1)^i(N-I)^i$.

Set $\mathsf S'=\mathsf S/2$, $\mathsf J'=N^{-1}/2$, $\mathsf D'=2^{-(2\alpha^2-2)}\mathsf D$, which are contractions with norms below $3/4$, $7/8$, $1$ <cite data-source="paper">\|\mathsf S'\|<\frac34,\qquad \|\mathsf J'\|<\frac78,\qquad \|\mathsf D'\|<1.</cite>. Put $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$; as $\|C\|=1$, both are contractions.

Since $C\mathsf T=N\mathsf D^{-1}$, the map $\mathsf DN^{-1}C$ is a left inverse of $\mathsf T$; applying it to the identity gives $\mathsf DN^{-1}CP_tF_t\mathsf S=P_sF_s$. The normalizations multiply to $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$, so $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$.

## Computing it

Records lie in $\mathbb D_p$ ([Fixed-point Gaussian dyadic records](fixed-point.md)); fix $0<\delta<1/8$. The three ordered numerical maps $\widetilde{\mathsf S}'$, $\widetilde{\mathsf J}'$, $\widetilde{\mathsf D}'$ have errors $16p$, $3p^2/4$, $4$ and times $O(tp^{3/2+\delta}\alpha)$, $O(tp^{3/2+\delta}\alpha)$, $O(tp^{1+\delta})$ <cite data-source="paper">\widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)\\</cite><cite data-source="paper">\widetilde{\mathsf J}'&3p^2/4&O(tp^{3/2+\delta}\alpha)\\</cite><cite data-source="paper">\widetilde{\mathsf D}'&4&O(tp^{1+\delta}).</cite>.

The selection $C$ picks an ordered subsequence (since $t/s>1$), and the indices are generated in order with $O(p)$ work each, so $C$ takes $O(tp)$ time with zero error <cite data-source="paper">also cost $O(tp)$, so $C$ takes $O(tp)$ time with zero numerical error.</cite>.

Take $\widetilde A=\widetilde{\mathsf S}'$ and $\widetilde B_0=\widetilde{\mathsf D}'\widetilde{\mathsf J}'C$. Contraction of the exact maps yields errors less than $16p<p^2$ and $4+3p^2/4<p^2$, and the costs add to $O(tp^{3/2+\delta}\alpha)$.

Let $E=N-I$ and $k=\lceil p/(\alpha^2\theta)\rceil$, the number of series terms kept (here $k$ changes meaning). Iterates are $\widetilde v^{(0)}=u/2$ rounded and $\widetilde v^{(j)}=\widetilde E\widetilde v^{(j-1)}$, where $\|\widetilde Ez\|<0.42\|z\|+(p/3)2^{-p}<1$ <cite data-source="paper">\|\widetilde E z\|<0.42\|z\|+(p/3)2^{-p}<1</cite>. The Neumann series with $E=N-I$ and $k=\lceil p/(\alpha^2\theta)\rceil$ is evaluated as $\widetilde{\mathsf J}'u=\sum_{j=0}^{k-1}(-1)^j\widetilde v^{(j)}$ with every iterate kept in $\mathbb D_p$.
