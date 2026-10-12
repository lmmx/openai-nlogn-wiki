Prime source lengths are distinct odd primes, each chosen just below a power of two, so that their product fills a fixed fraction of the padded box. Here $s_i$ is the $i$-th prime source length, an odd prime, and $t_i$ is the $i$-th padded axis length, a power of two. The padded box is the box whose axis lengths are the $t_i$.

Two requirements fix how close $s_i$ must be to $t_i$. First, their product must occupy a fixed fraction of the padded box <cite data-source="paper">their product must occupy a fixed fraction of the padded box</cite>. Second, each ratio $t_i/s_i$ must leave enough separation for [Gaussian resampling](gaussian-resampling.md), which moves between transforms of length $s_i$ and of length $t_i$.

We use the window
$$(1-2\eta)\,t_i < s_i \le (1-\eta)\,t_i,$$
where $\eta$ is a fixed constant with $0<\eta<1/4$ that sets the window width. Such windows contain primes. A prime-interval estimate due to Rosser and Schoenfeld says that for large $t$ a window of this shape contains many primes <cite data-source="paper">contains at least ηx/(2 log x) primes</cite>. We choose distinct primes from these windows, one per axis.

For example, take $t=16$ and $\eta=1/5$. The window is $9.6 < s \le 12.8$, which contains exactly one prime, $s=11$, and $\gcd(11,16)=1$ because $11$ is odd.

Since the $s_i$ are distinct primes, they are pairwise coprime. Distinct primes give pairwise coprime lengths for the [Chinese-remainder map](chinese-remainder-map.md), which turns one cyclic convolution into a multidimensional one.
