A prime source length is an odd prime $s_i$ chosen just below the padded length of its axis. Here $t_i$ is a power of two, the padded length of axis $i$, and $s_i$ lies just below it. Write $S=\prod_i s_i$ for the product of the source lengths and $T=\prod_i t_i$ for the padded box. The primes are chosen so that $S$ fills a fixed fraction of $T$. The lengths $s_i$ are the moduli of the [Chinese-remainder map](chinese-remainder-map.md) that turns one cyclic convolution of length $S$ into a multidimensional one over the $s_i$.

Let $d$ be the number of axes and $\eta$ a fixed gap with $0<\eta<1/4$. Each prime is taken in the window $(1-2\eta)t_i<s_i\le(1-\eta)t_i$, so the ratio $t_i/s_i$ stays a fixed amount above one. The primes are sized for [Gaussian resampling](gaussian-resampling.md), since each ratio $t_i/s_i$ must leave separation for it.

A prime in each window exists. For $0<\eta<1/4$ and $x>e^2/\eta$, the interval $(1-2\eta)x<q\le(1-\eta)x$ holds at least $\eta x/(2\log x)$ primes <cite data-source="paper">the interval (1 − 2η)x < q ≤ (1 − η)x contains at least ηx/(2 log x) primes</cite>. For large padded lengths this count exceeds $d$, so each axis has a prime to pick from. Windows for padded lengths that differ by a factor of two are disjoint when $\eta<1/4$, so the chosen primes are distinct, and they are odd because the windows lie above $2$. Each $\gcd(s_i,t_i)$ equals one, since $s_i$ is odd and $t_i$ is a power of two.

Let $S/T=\prod_i s_i/t_i$. Each factor lies in $(1-2\eta,1-\eta]$, so $S/T\le(1-\eta)^d<1$. The strict Bernoulli inequality gives $S/T>(1-2\eta)^d>1-2d\eta$ for $d\ge 2$, and this exceeds $1/2$ when $2d\eta\le 1/2$. Hence $T/2<S<T$.

The result holds although each prime is chosen independently, because every ratio is pinned in a window of width $\eta$ just below one. With $2d\eta\le 1/2$, the $d$ ratios cannot drift far enough apart to push their product out of the range between one half and one.

For example, take $d=2$, $t_1=8$, $t_2=16$ and $\eta=1/8$. The windows are $(6,7]$ and $(12,14]$, which hold the primes $s_1=7$ and $s_2=13$. Then $S=91$, $T=128$, and $64<91<128$.
