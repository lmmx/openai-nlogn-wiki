This page fixes every exponent and size for $n$-bit inputs, so that the hypotheses of the [simultaneous butterfly layer](simultaneous-layer.md) and of [Gaussian resampling](gaussian-resampling.md) are all satisfied. Because the constants are fixed rationals, each inequality among them is an integer comparison.

## Exponents

Here $\tau$ is the exponent in the cost $O(Vw^\tau)$ of swapping two address chunks of width $w$ on bit volume $V$. The exponent $\sigma$ is a rational upper bound for the logarithmic exponent of the layer's recurrence. The recursion stops below size $d^\beta$, so $\beta$ is the exponent setting that threshold. The exponent $\lambda$ governs the overhead at each internal node of the recursion. The exponent $\lambda'$ is the one in the layer cost $O(Vd^{\lambda'})$. The exponent $c$ gives the address-chunk width $K=\lfloor d^c\rfloor$ in bits. The exponent $\epsilon$ gives the axis count $d=\lfloor b^\epsilon\rfloor$. The exponent $C_1$ is the one in the guard-width bound $O(d^{C_1})$ on reserved extra bits. On earlier pages $\sigma$ and $c$ meant other things; here they have these meanings.

Take $\tau=\sigma=1-2^{-50}$, $\beta=1/2$ and $\delta=1/16$. Take $\lambda=1-2^{-52}$ and $c=2^{-56}$. Take $\lambda'=1-2^{-54}$. Take $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$. These constants are deliberately conservative, with no optimization claimed <cite data-source="paper">These constants are deliberately conservative; no optimization is claimed.</cite>

The layer needs $\max\{\tau,\sigma\}<\lambda<1$, $\tau(1+c/\beta)<\lambda$, $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$ and $\epsilon C_1<1$. The layer conditions hold with room to spare: $\tau(1+c/\beta)<1-31\cdot2^{-55}<\lambda$, since $\tau(1+c/\beta)=(1-2^{-50})(1+2^{-55})=1-31\cdot2^{-55}-2^{-105}$ and $\lambda=1-8\cdot2^{-55}$. Also $\sigma+\beta(1-\sigma)=1-2^{-51}<\lambda<\lambda'<1$, and $\epsilon C_1=20\cdot2^{-75}<1$.

## Sizes

For large $n$ put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$. Here $b$ is the digit width, $p$ sets the precision of the [Fixed-point Gaussian dyadic records](fixed-point.md), and $d$ is the axis count. Put $K=\lfloor d^c\rfloor$. Take the power of two $T$ in $[4n/b,8n/b)$, so $Tp\in[24n,48n)$.

Let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$; choose $d\ell-\log_2T\in[0,d)$ of the axis lengths to be $r/2$ and the others $r$, with the last axis of length $r$. The count lies in $[0,d)$ because $\ell$ rounds up, so some axis has length $r$; the product is $r^d/2^{d\ell-\log_2T}=T$. Thus $t_i\in\{r/2,r\}$, $\prod_it_i=T$ and $t_d=r$.

The lemmas assume $a_dp^\epsilon\le d\le b_dp^\epsilon$, $2^{a_rp/d}\le r\le2^{b_rp/d}$ and $d\ell\le C_\ell p$, where $a_d\le b_d$, $a_r\le b_r$ and $C_\ell$ are fixed positive constants bounding $d$, $r$ and $d\ell$. Since $2^{b-1}<n\le2^b$, we get $b/2\le\log_2T\le b$ for large $b$; with $b^\epsilon/2\le d\le b^\epsilon\le b$ this yields $\frac1{12}p^\epsilon\le d\le p^\epsilon$ and $\frac p{12d}\le\ell\le\frac p{3d}$. These choices give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$, $r=2^{\Theta(p^{1-\epsilon})}$, so the comparison constants $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, $C_\ell=1$ can be fixed for all lengths at once.

## Primes

Put $\alpha=\lceil(12d^2b)^{1/4}\rceil$, the Gaussian width of resampling. Put $\gamma=2d\alpha^2$ and $\eta=1/(4d)$. Here $\gamma$ is the exponent of the scale factor $2^\gamma$ of $d$-axis resampling, and $\eta$ is the smallest relative distance at which a prime $s_i$ may lie below $t_i$. As $\lceil A\rceil\le2A$ for real $A\ge1$, then $\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}$, so $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$.

The prime-interval lemma of Harvey and van der Hoeven is used without proof. For $0<\eta<1/4$ and a real number $x>e^{2/\eta}$ (the scale of the interval), the integers greater than $(1-2\eta)x$ and at most $(1-\eta)x$ include at least $\eta x/(2\log x)$ primes <cite data-source="paper">contains at least $\eta x/(2\log x)$ primes</cite>, with $\log$ the natural logarithm.

Here $\eta x/(2\log x)=x/(8d\log x)$ and $2/\eta=8d$. Both $x=r/2$ and $x=r$ qualify: $\log(r/2)/d=\Theta(p^{1-2\epsilon})\to\infty$, so $\log x>8d$. The count exceeds $d$ once $x>8d^2\log x$, which holds eventually because $\log x=\Theta(p^{1-\epsilon})$ while $\log(8d^2\log x)=O(\log p)=o(\log x)$. The two intervals are disjoint since $(1-\eta)r/2<(1-2\eta)r$, and lie above $2$.

Choose distinct odd primes with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$; $\gcd(s_i,t_i)=1$ as $t_i$ is a power of two. This choice supplies the prime axis lengths of the [Chinese-remainder address map](crt-map.md). Put $S=\prod_is_i$.

Multiplying the lower bounds and applying strict Bernoulli gives $S/T>(1-1/(2d))^d>1/2$ for $d\ge2$, because $(1-1/(2d))^d>1-d/(2d)$. With $s_i<t_i$ this gives $T/2<S<T$.

For the separation, $s_i\le(1-\eta)t_i$ gives $t_i/s_i\ge1/(1-\eta)$. With $\theta_i=t_i/s_i-1\ge\eta/(1-\eta)>\eta$ we get $\alpha^4\theta_i>12d^2b/(4d)=3db\ge6b=p$, the separation hypothesis of the resampling lemma; also $t_i\le r\le T<2^p$.

Trial division on the candidates costs $O(dr^{3/2}\operatorname{poly}(p))$, whose logarithm is $o(p)$. The deterministic search for the primes takes $n^{o(1)}=o(n)$ time, since its logarithm is $o(p)$ and $p=\Theta(\log n)$; all primes and length parameters are generated by the machine, not given as advice <cite data-source="paper">the search takes $n^{o(1)}=o(n)$ time</cite>.
