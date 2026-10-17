This page fixes every exponent and size for $n$-bit inputs so that the hypotheses of the [simultaneous butterfly layer](simultaneous-layer.md) and of [Gaussian resampling](gaussian-resampling.md) hold at once.

Fixed rational exponents with explicit slack turn each required inequality into an integer comparison that can be checked exactly. In the layer, $\tau$ is the exponent of the cost of a chunk interchange, $\sigma$ bounds the exponent of the recursion's branching ratio, $\beta$ (an exponent here, not a unit modulo a prime) sets the threshold $d^\beta$ below which active chunks are handled singly, $\lambda$ is the exponent of the per-node overhead, and $\lambda'$ is the exponent in the final cost $O(Vd^{\lambda'})$ on bit volume $V$. Further, $c$ is the exponent of the address-chunk width in terms of $d$ (not the scaling integer of [Controlled shifts and rational scalings](controlled-shifts.md)), $\epsilon$ is the exponent of the axis count in terms of $b$, $C_1$ is the exponent bounding the guard bits, and $\delta$ is the resampling-cost slack.

Take $\tau=\sigma=1-2^{-50}$, $\beta=1/2$ and $\delta=1/16$. Take $\lambda=1-2^{-52}$ and $c=2^{-56}$. Take $\lambda'=1-2^{-54}$. Take $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$. These constants are deliberately conservative<cite data-source="paper">These constants are deliberately conservative; no optimization is claimed.</cite>.

The layer needs $\max\{\tau,\sigma\}<\lambda<1$, $\tau(1+c/\beta)<\lambda$, $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$ and $\epsilon C_1<1$. The layer conditions hold with room to spare: $\tau(1+c/\beta)<1-31\cdot2^{-55}<\lambda$, since $\tau(1+c/\beta)=(1-2^{-50})(1+2^{-55})=1-31\cdot2^{-55}-2^{-105}$ and $\lambda=1-8\cdot2^{-55}$. Also $\sigma+\beta(1-\sigma)=1-2^{-51}<\lambda<\lambda'<1$, and $\epsilon C_1=20\cdot2^{-75}<1$.

## Sizes

For large $n$ put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$. Here $b$ is the digit width, $d$ is the axis count, and $p$ sets the number of fractional bits of the [Fixed-point Gaussian dyadic records](fixed-point.md). Put $K=\lfloor d^c\rfloor$, the width of an address chunk. Take the power of two $T$ in $[4n/b,8n/b)$; the interval has ratio $2$, so it holds exactly one, and $Tp\in[24n,48n)$.

Let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$; choose $d\ell-\log_2T\in[0,d)$ of the axis lengths to be $r/2$ and the others $r$, with the last axis of length $r$. The count lies in $[0,d)$ because $\ell$ rounds up, so some axis has length $r$, and the product is $r^d/2^{d\ell-\log_2T}=T$. Thus $t_i\in\{r/2,r\}$, $\prod_it_i=T$ and $t_d=r$.

The lemmas assume $a_dp^\epsilon\le d\le b_dp^\epsilon$, $2^{a_rp/d}\le r\le2^{b_rp/d}$ and $d\ell\le C_\ell p$, with fixed constants $a_d,b_d,a_r,b_r,C_\ell$. Since $2^{b-1}<n\le2^b$, we get $b/2\le\log_2T\le b$ for large $b$. With $b^\epsilon/2\le d\le b^\epsilon\le b$ this yields $\frac1{12}p^\epsilon\le d\le p^\epsilon$ and $\frac p{12d}\le\ell\le\frac p{3d}$. These choices give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$, $r=2^{\Theta(p^{1-\epsilon})}$, so the comparison constants $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, $C_\ell=1$ can be fixed for all lengths at once.

## Resampling parameters

Put $\alpha=\lceil(12d^2b)^{1/4}\rceil$, the Gaussian width of resampling. Put $\gamma=2d\alpha^2$ and $\eta=1/(4d)$, where $\gamma$ is the exponent of the scale factor $2^\gamma$ of $d$-axis resampling, and $\eta$ is the least relative distance at which a prime $s_i$ may lie below $t_i$. As $\lceil A\rceil\le2A$ for real $A\ge1$ and $8\sqrt{12}<28$, then $\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}$, so $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$.

## Primes

Each $s_i$ is a prime whose relative distance below $t_i$ lies in $[\eta,2\eta)$. The nearer end gives the gap resampling needs; the farther end keeps $S$, the product of the $s_i$, a fixed fraction of $T$.

By the prime-interval lemma of Harvey and van der Hoeven, used here without proof, for $0<\eta<1/4$ and real $x>e^{2/\eta}$ the interval of integers $q$ with $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes<cite data-source="paper">contains at least $\eta x/(2\log x)$ primes</cite>. Here $q$ is an integer in the interval, not a radix or a sequence length as on earlier pages.

Both $x=r/2$ and $x=r$ qualify since $\log x>8d=2/\eta$, because $\log(r/2)/d=\Theta(p^{1-2\epsilon})\to\infty$. The count $x/(8d\log x)$ exceeds $d$ because $x>8d^2\log x$, as $\log(8d^2\log x)=\Theta(\log p)=o(\log x)$. The two intervals are disjoint since $(1-\eta)r/2<(1-2\eta)r$, and lie above $2$.

Choose distinct odd primes with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$; $\gcd(s_i,t_i)=1$ as $t_i$ is a power of two. This choice supplies the prime axis lengths of the [Chinese-remainder address map](crt-map.md). Put $S=\prod_is_i$.

Multiplying the lower bounds and applying strict Bernoulli gives $S/T>(1-1/(2d))^d>1/2$ for $d\ge2$, because $(1-1/(2d))^d>1-d/(2d)$. With $s_i<t_i$ this gives $T/2<S<T$.

For the separation, $s_i\le(1-\eta)t_i$ gives $t_i/s_i\ge1/(1-\eta)$. With $\theta_i=t_i/s_i-1\ge\eta/(1-\eta)>\eta$ we get $\alpha^4\theta_i>12d^2b/(4d)=3db\ge6b=p$, which meets the separation hypothesis of [Gaussian resampling](gaussian-resampling.md); also $t_i\le r\le T<2^p$.

Trial division of every candidate costs $O(dr^{3/2}\operatorname{poly}(p))$, with logarithm $o(p)$. The deterministic search for the primes takes $n^{o(1)}=o(n)$ time, since its logarithm is $o(p)$ and $p=\Theta(\log n)$<cite data-source="paper">the search takes $n^{o(1)}=o(n)$ time</cite>; all primes and length parameters are generated by the machine, not given as advice.
