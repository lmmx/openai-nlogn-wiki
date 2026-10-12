Prime source lengths are distinct odd primes $s_\nu$, one for each axis $\nu$, chosen so that their product fills a fixed fraction of the padded box. Here $T_\nu$, a power of two, is the $\nu$-th padded axis length, and the padded box is the box whose axis lengths are the $T_\nu$. Each $s_\nu$ is chosen near $T_\nu$. The letters $s$ and $T$ change meaning here.

Two requirements fix how close $s_\nu$ must be to $T_\nu$. First, the product of the $s_\nu$ must fill a fixed fraction of the padded box <cite data-source="paper">their product must occupy a fixed fraction of the padded box</cite>. Second, the ratio $T_\nu/s_\nu$ must leave enough separation for [Gaussian resampling](gaussian-resampling.md), which moves between transforms of length $s_\nu$ and of length $T_\nu$.

We use the window
$$(1-2\eta)\,T_\nu < s_\nu \le (1-\eta)\,T_\nu,$$
where $\eta$, a fixed constant with $0<\eta<1/4$, sets the width of the window.

For large $T_\nu$, a prime-interval result, based on explicit estimates of Rosser and Schoenfeld, shows that the window holds many primes <cite data-source="paper">contains at least ηx/(2 log x) primes</cite>. Taking $\eta=1/(4K)$ gives at least $T_\nu/(8K\log T_\nu)$ primes in each window, which exceeds $K$ for large $T_\nu$ <cite data-source="paper">the stated lower bound for the number of primes is x/(8d log x) and exceeds d</cite>, so one distinct prime per axis can be chosen.

For example, take $T_\nu=16$ and $\eta=1/5$. The window is $9.6 < s_\nu \le 12.8$, which contains only the prime $11$, so at this small size the window cannot supply many axes. Also $\gcd(11,16)=1$, since $11$ is odd and $16$ is a power of two.

Distinct primes are pairwise coprime, so the $s_\nu$ supply axis lengths to the [Chinese-remainder map](chinese-remainder-map.md), which turns one cyclic convolution into a multidimensional one.
