Prime source lengths are distinct odd primes, one for each axis of a multidimensional transform. They are chosen so that their product fills a fixed fraction of the padded box (defined below), which lets the [integer multiplication below n log n](main-theorem.md) algorithm fit every term in its cost table within the bound of the theorem.

Let $d$ be the number of axes, and for $i=1,\dots,d$ let $s_i$ be the prime source length of axis $i$. An *axis* is one coordinate direction of a multidimensional array. Axis $i$ is padded to the power of two $t_i$, so the padded array is a box with sides $t_1,\dots,t_d$.

### What the primes must satisfy

Two requirements fix how close each $s_i$ must be to $t_i$. The first is coprimality. The distinct primes supply pairwise coprime lengths to the [Chinese-remainder map](chinese-remainder-map.md), which relabels coefficient positions by mixed-radix digits. <cite data-source="paper">Every gcd(si , ti ) equals one because ti is a power of two.</cite> Distinct primes are pairwise coprime, and each $s_i$ is coprime to $t_i$.

The second is separation. Each ratio $t_i/s_i$ must leave enough separation for [Gaussian resampling](gaussian-resampling.md). <cite data-source="paper">The distinct prime lengths si must be close to the powers of two ti</cite>: the product must be a large fraction of the box, and each ratio must be large enough for the resampling step.

### Finding the primes

Here $n$ is the bit length of each input, and $b=\lceil\log_2 n\rceil$ is the number of bits needed to write $n$. The padded box has size $T$, a power of two with $4n/b \le T < 8n/b$. <cite data-source="paper">Choose dℓ − log2 T of the d axis lengths to be r/2 and the others to be r</cite>. Thus the padded axis lengths take the two values $u/2$ and $u$, where $u$ is a power of two and the longer of the two lengths.

The counting tool is a prime-interval result. Here $x$ is a real number that sets the scale of the interval, $q$ is a prime in it, and $\eta$ is a slack fraction with $0<\eta<1/4$. For $x>e^{2/\eta}$, the interval $(1-2\eta)x < q \le (1-\eta)x$ contains at least $\eta x/(2\log x)$ primes, where $\log$ is the natural logarithm. The slack fraction is $\eta = 1/(4d)$, so $\eta x/(2\log x) = x/(8d\log x)$.

Apply this with $x = u/2$ and with $x = u$. The two intervals are disjoint, because $(1-\eta)u/2 < (1-2\eta)u$ for $\eta < 1/4$. Each interval contains more primes than there are axes: <cite data-source="paper">the stated lower bound for the number of primes is x/(8d log x) and exceeds d</cite>. So distinct odd primes can be chosen, one per axis, with
$$(1-2\eta)\,t_i < s_i \le (1-\eta)\,t_i.$$

The search is deterministic. <cite data-source="paper">The machine finds these primes by scanning the two intervals deterministically and testing each candidate by trial division through its square root.</cite> The source bounds the total search time: <cite data-source="paper">the search takes no(1) = o(n) time</cite>.

### Product and separation

Multiplying the lower bounds on the $s_i$ gives a product $S = s_1 s_2\cdots s_d$ that fills most of the box. The source derives this from the <cite data-source="paper">bounds on si and applying strict Bernoulli inequality gives</cite> $S/T > (1-1/(2d))^d > 1/2$ for $d \ge 2$, since $2\eta = 1/(2d)$. Because each $s_i < t_i$, <cite data-source="paper">Together with si < ti , this gives T /2 < S < T</cite>.

For the separation, write $\theta_i = t_i/s_i - 1$. Since $s_i \le (1-\eta)t_i$ gives $t_i/s_i \ge 1/(1-\eta)$, we get $\theta_i \ge \eta/(1-\eta) > \eta$. This is the separation that the resampling step needs to be large.

### Worked example

Take $d = 2$, so $\eta = 1/8$, and $u = 16$, so the padded lengths are $t_1 = 16$ and $t_2 = 8$, and $T = 128$. For $t_1$, the interval $(12, 14]$ contains only $13$. For $t_2$, the interval $(6, 7]$ contains only $7$. So $s_1 = 13$ and $s_2 = 7$, with $S = 91$ and $64 < 91 < 128$. The ratio is $\theta_1 = 16/13 - 1 = 3/13 \approx 0.23$, which exceeds $\eta/(1-\eta) = 1/7 \approx 0.14$. At this size the counting lemma does not apply, so the example picks the primes by hand.
