Prime source lengths are distinct odd primes, one per padded axis, chosen near powers of two so that their product fills a fixed fraction of the padded box. They are chosen so that every term of the cost table fits the bound of the main theorem.

The letters $s$ and $t$ take new meanings here. Here $s_i$ is the $i$-th prime source length, an odd prime, and $t_i$ is the $i$-th padded axis length, a power of two. The padded box is the box whose axis lengths are the $t_i$.

Two requirements fix how close $s_i$ must be to $t_i$. First, their product must fill a fixed fraction of the padded box <cite data-source="paper">their product must occupy a fixed fraction of the padded box</cite>. Second, the ratio $t_i/s_i$ must leave enough separation for [Gaussian resampling](gaussian-resampling.md), which moves between transforms of length $s_i$ and of length $t_i$.

We use the window
$$(1-2\eta)\,t_i < s_i \le (1-\eta)\,t_i,$$
where the constant $\eta$, with $0<\eta<1/4$, sets the width of the window. For $t$ large enough, such a window contains primes. A prime-interval result, based on explicit estimates of Rosser and Schoenfeld, shows that it contains many primes, at least a fixed multiple of $t/\log t$ <cite data-source="paper">contains at least ηx/(2 log x) primes</cite>. We choose distinct odd primes, one per axis, from these windows <cite data-source="paper">We may therefore choose distinct odd primes satisfying</cite>.

For example, take $t=16$ and $\eta=1/5$. The window is $9.6 < s \le 12.8$, where $s$ is a candidate for some $s_i$. It contains exactly one prime, $s=11$, and $\gcd(11,16)=1$ because $11$ is odd and $16$ is a power of two.

Since the $s_i$ are distinct primes, they are pairwise coprime, so they supply axis lengths to the [Chinese-remainder map](chinese-remainder-map.md), which turns one cyclic convolution into a multidimensional one.
