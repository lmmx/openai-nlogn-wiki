Prime source lengths are distinct odd primes, one per padded axis, chosen near powers of two so that their product fills a fixed fraction of the padded box. This makes every term of the cost table fit the bound of the main theorem.

The axis index $\nu$ runs from $1$ to $d$, one value per axis. Here $s_\nu$ is the $\nu$-th prime source length, an odd prime, and $t_\nu$ is the $\nu$-th padded axis length, a power of two. The letters $s$ and $t$ change meaning here. The padded box is the box whose axis lengths are the $t_\nu$.

Two requirements fix how close $s_\nu$ must be to $t_\nu$. First, the product of the $s_\nu$ must fill a fixed fraction of the padded box <cite data-source="paper">their product must occupy a fixed fraction of the padded box</cite>. Second, the ratio $t_\nu/s_\nu$ must leave enough separation for [Gaussian resampling](gaussian-resampling.md), which moves between transforms of length $s_\nu$ and of length $t_\nu$.

We use the window
$$(1-2\eta)\,t_\nu < s_\nu \le (1-\eta)\,t_\nu,$$
where the constant $\eta$, with $0<\eta<1/4$, sets the width of the window. For large $t_\nu$, a prime-interval result, based on explicit estimates of Rosser and Schoenfeld, shows that the window contains many primes <cite data-source="paper">contains at least ηx/(2 log x) primes</cite>, and this count exceeds the number of axes <cite data-source="paper">the stated lower bound for the number of primes is x/(8d log x) and exceeds d</cite>. So distinct odd primes, one per axis, can be chosen from these windows.

For example, take $t_\nu=16$ and $\eta=1/5$. The window is $9.6 < s_\nu \le 12.8$. It contains exactly one prime, $11$, so at this small size the window cannot supply many axes. Also $\gcd(11,16)=1$ because $11$ is odd and $16$ is a power of two.

Since the $s_\nu$ are distinct primes, they are pairwise coprime, so they supply axis lengths to the [Chinese-remainder map](chinese-remainder-map.md), which turns one cyclic convolution into a multidimensional one.
