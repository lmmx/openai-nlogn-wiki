Prime source lengths are distinct odd [Prime number](prime-number.md)s $s_1,\dots,s_d$, one for each axis of a padded array, each just below the padded length of its axis. Their product $S$ is the length of the cyclic convolution modulo $x^S-1$ used by the [integer multiplication below n log n](main-theorem.md) algorithm, so they must fill a fixed fraction of the padded box.

## Padded box and axis lengths

An axis is one coordinate direction of a multidimensional array; padding an axis to length $t$ adds unused positions until it has $t$ entries. Let $d$ be the number of axes, $b=\lceil\log_2 n\rceil$ (so $2^{b-1}<n\le2^b$), and $T$ the padded box size, the product of the padded lengths $t_1,\dots,t_d$. The construction takes <cite data-source="paper">Take the power of two T in [4n/b, 8n/b)</cite>, so $4n/b\le T<8n/b$, and $d=\lfloor b^{\epsilon}\rfloor$ with $\lfloor x\rfloor$ the greatest integer at most $x$ and $\epsilon$ the size exponent, <cite data-source="paper">ϵ = 2−75</cite>. Since $\epsilon<1/2$, $d\to\infty$, and $d\ge2$ for large $n$.

Let $\ell=\lceil(\log_2T)/d\rceil$ (the least integer at least $(\log_2T)/d$) and $u=2^\ell$. Here $u$ is the common length of the longest axes, which the source calls $r$; the letter changes meaning. Since $T$ is a power of two, $\log_2T$ is an integer, and $\ell-1<(\log_2T)/d\le\ell$ gives $0\le w<d$ for $w=d\ell-\log_2T$, the number of axes whose length is $u/2$ (the letter changes meaning here). <cite data-source="paper">Choose dℓ − log2 T of the d axis lengths to be r/2 and the others to be r.</cite> So $w$ axes get $t_i=u/2$ and the rest get $t_i=u$; which axes are which does not matter. The product is $(u/2)^wu^{d-w}=2^{d\ell-w}=T$, and $w<d$ means some axis has length $u$.

## Choosing the primes

The counting tool is a prime-interval bound with a slack fraction $\eta$ and a real scale $\xi$ (the letter changes meaning here), where $\ln$ is the natural logarithm and $e\approx2.718$ is Euler's number, the base of $\ln$. <cite data-source="paper">The prime-interval result [15, Lemma 5.1], based on explicit estimates of Rosser and Schoenfeld [23], gives the following bound</cite>: for $0<\eta<1/4$ and $\xi>e^{2/\eta}$, the interval $((1-2\eta)\xi,(1-\eta)\xi]$ contains at least $\eta\xi/(2\ln\xi)$ primes.

Set $\eta=1/(4d)$, which is below $1/4$ since $d\ge2$. Then $2/\eta=8d$, and the count is $\xi/(8d\ln\xi)$, which exceeds $d$ when $\xi>8d^2\ln\xi$. We apply the bound to $\xi=u/2$ and $\xi=u$, the two lengths an axis can take.

For $\xi=u/2$, write $\Upsilon=\ln(u/2)$, a real number (the letter changes meaning here). Since $T\ge4n/b>2^{b+1}/b$, we have $\log_2T>b+1-\log_2b$, so $\Upsilon\ge(\log_2T/d-1)\ln2$. Dividing by $d\le b^\epsilon$ gives $\Upsilon/d\ge\big((b+1-\log_2b)/b^{2\epsilon}-1\big)\ln2\to\infty$, since $2\epsilon<1$. So for large $n$, $\Upsilon>8d$ (that is, $\ln\xi>8d$) and $d<\Upsilon$. Since $e^\Upsilon/\Upsilon^3\to\infty$, $u/2=e^\Upsilon>8\Upsilon^3\ge8d^2\Upsilon$, which is $\xi>8d^2\ln\xi$. For $\xi=u$: $\ln u>8d$, and $x\mapsto x-8d^2\ln x$ increases for $x\ge8d^2$, so $u-8d^2\ln u\ge u/2-8d^2\ln(u/2)>0$.

Both intervals lie above $2$, since $(1-2\eta)u/2\ge\frac34\cdot\frac u2>2$, so their primes are odd. They are disjoint, since $(1-\eta)u/2<(1-2\eta)u$ when $3\eta<1$. Each holds more than $d$ primes, so the axes with $t_i=u/2$ take distinct primes from the first interval and the others take distinct primes from the second. For each axis $i$, its prime source length $s_i$ satisfies
$$(1-2\eta)\,t_i<s_i\le(1-\eta)\,t_i.$$

<cite data-source="paper">Every gcd(si , ti ) equals one because ti is a power of two.</cite> The lengths are chosen as distinct [Prime number](prime-number.md)s. Distinct primes are pairwise coprime, so the lengths satisfy the pairwise form of [Coprime](coprime.md). The distinct primes supply pairwise coprime lengths to the [Chinese-remainder map](chinese-remainder-map.md).

## Product and separation

Let $S=s_1s_2\cdots s_d$, the total number of positions. The lengths $s_1,\dots,s_d$ set the place values of the [Mixed-radix digits](mixed-radix-digits.md) of the $S$ positions, digit $i$ running from $0$ to $s_i-1$.

Since $s_i>(1-\frac1{2d})t_i$ and $\prod_i t_i=T$, we get $S>(1-\frac1{2d})^dT$. <cite data-source="paper">bounds on si and applying strict Bernoulli inequality gives</cite> $(1-\frac1{2d})^d>\frac12$. Bernoulli's inequality $(1+x)^d\ge1+dx$ holds for $x\ge-1$, and is strict for $x\ne0$, $d\ge2$: induction on $d$ with $(1+x)^d-1-dx=(1+x)\big[(1+x)^{d-1}-1-(d-1)x\big]+(d-1)x^2$ shows it. Taking $x=-\frac1{2d}$ gives $1+dx=\frac12$. Since $s_i<t_i$ for each $i$, <cite data-source="paper">Together with si < ti , this gives T /2 < S < T .</cite>

Let $\theta_i=t_i/s_i-1$, the relative gap of axis $i$. From $s_i\le(1-\eta)t_i$, $\theta_i\ge\eta/(1-\eta)>\eta$. Each ratio $t_i/s_i$ must leave enough separation for [Gaussian resampling](gaussian-resampling.md). The source needs $\alpha^4\theta_i>p$ on every axis, where $\alpha=(12d^2b)^{1/4}$ and $p=6b$ are its parameters (here $\alpha$ is a real number, not the integer width of that page). Since $\alpha^4\eta=12d^2b/(4d)=3db\ge6b=p$, the bound $\theta_i>\eta$ gives this.

## Cost of the search

The machine tests each candidate in the two intervals by trial division, dividing by the integers up to its square root $\sqrt{\cdot}$. Each interval has at most $u$ candidates, each needs at most $\sqrt u$ divisions, and each division of $O(b)$-bit numbers costs $\mathrm{poly}(b)$ operations. The cost is $O(u^{3/2}\mathrm{poly}(b))$. Since $T<8n/b\le2^{b+3}$, $\ell<1+(b+3)/d$, so the logarithm of the cost is $O(\log b)+O(b/d)=o(b)$, because $d\to\infty$. As $b<\log_2n+1$, this is $n^{o(1)}$, and <cite data-source="paper">the search takes no(1) = o(n) time.</cite>

## Worked example

Take $d=2$, so $\eta=1/8$, and $T=128$. Then $\ell=4$, $u=16$, and $w=1$, so $t_1=16$ and $t_2=8$. The interval $(12,14]$ contains only $13$, and $(6,7]$ contains only $7$, so $s_1=13$ and $s_2=7$, with $S=91$ and $64<91<128$. The gap $\theta_1=16/13-1\approx0.23$ exceeds $\eta/(1-\eta)=1/7$. The bound needs $\xi>e^{16}\approx8.9\times10^6$, far above $8$ and $16$, so the example picks the primes by hand.
