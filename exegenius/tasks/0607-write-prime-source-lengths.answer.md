Prime source lengths are distinct odd [Prime number](prime-number.md)s $s_1,\dots,s_d$, one for each axis of a padded array, where $i$ indexes the axes from $1$ to $d$, and $s_i$ is just below the padded length $t_i$ of axis $i$. Their product $S=s_1\cdots s_d$ is the length of the cyclic convolution that the multiplication algorithm computes, so the lengths must fill a fixed fraction of the padded box.

## Padded box and axis lengths

An axis is one coordinate direction of a multidimensional array, and padding an axis to length $t$ adds unused positions until it has $t$ entries. Let $b=\lceil\log_2 n\rceil$ be the bit length of $n$, so $2^{b-1}<n\le2^b$, where $\lceil x\rceil$ is the least integer at least $x$. Let $d$ be the number of axes, and let $T$ be the padded box size, the product of the padded lengths $t_1,\dots,t_d$.

The construction begins: <cite data-source="paper">Take the power of two T in [4n/b, 8n/b)</cite>. This gives $4n/b\le T<8n/b$, and $T$ is a power of two. Here $\epsilon$ is the size exponent, a fixed constant, and $d=\lfloor b^{\epsilon}\rfloor$, where $\lfloor x\rfloor$ is the greatest integer at most $x$. The source sets <cite data-source="paper">ϵ = 2−75</cite>. Since $\epsilon<1/2$, we get $d\to\infty$ and $d\ge2$ for large $n$.

Let $\ell=\lceil(\log_2T)/d\rceil$ be the least integer at least $(\log_2T)/d$. Let $u=2^\ell$ be the common length of the longest axes (the letter changes meaning here; the source calls it $r$). Since $T$ is a power of two, $\log_2T$ is an integer. The number of axes whose length is $u/2$ is $w=d\ell-\log_2T$ (the letter $w$ changes meaning here), an integer in $[0,d)$ because $\ell-1<(\log_2T)/d\le\ell$. <cite data-source="paper">Choose dℓ − log2 T of the d axis lengths to be r/2 and the others to be r.</cite> So $w$ axes get $t_i=u/2$ and the rest get $t_i=u$. The product is $(u/2)^w u^{d-w}=2^{d\ell-w}=T$, and since $w<d$, at least one axis has length $u$.

## Choosing the primes

The counting tool is a prime-interval bound with a slack fraction $\eta$ and a real scale $\xi$ (both letters change meaning here). <cite data-source="paper">The prime-interval result [15, Lemma 5.1], based on explicit estimates of Rosser and Schoenfeld [23], gives the following bound</cite>: for $0<\eta<1/4$ and $\xi>e^{2/\eta}$, the interval $((1-2\eta)\xi,(1-\eta)\xi]$ contains at least $\eta\xi/(2\ln\xi)$ primes. Here $\ln$ is the natural logarithm. The page takes this bound from the source without proof.

Set $\eta=1/(4d)$, which is below $1/4$ because $d\ge2$. Then $2/\eta=8d$, and the bound gives $\xi/(8d\ln\xi)$ primes. This exceeds $d$ exactly when $\xi>8d^2\ln\xi$. We apply the bound at $\xi=u/2$ and $\xi=u$, the two lengths an axis can take.

Let $L=\ln(u/2)=(\ell-1)\ln2$. From $T\ge4n/b>2^{b+1}/b$ we get $\log_2T\ge b/2$ for large $n$. Then $\ell\ge(\log_2T)/d\ge b^{1-\epsilon}/2$, because $d\le b^\epsilon$. Hence $L\ge\frac{\ln2}{4}b^{1-\epsilon}$ for large $n$.

Since $8d\le8b^\epsilon$ and $\epsilon<1/2$, we have $8d<L\le\ln u$ for large $n$, so $\xi>e^{8d}$ for both values. For $\xi=u/2$, the condition $\xi>8d^2\ln\xi$ says $e^L>8d^2L$. The function $e^x/x$ is increasing for $x\ge1$, and $e^y/y$ with $y=\frac{\ln2}{4}b^{1-\epsilon}$ grows faster than any power of $b$, so $e^L/L\ge e^y/y>8d^2$ for large $n$. For $\xi=u$, the function $f(x)=x-8d^2\ln x$ has $f'(x)=1-8d^2/x\ge0$ for $x\ge8d^2$. Since $u/2>8d^2\ln(u/2)\ge8d^2$, $f$ is nondecreasing on $[u/2,u]$, so $f(u)\ge f(u/2)>0$, which is $u>8d^2\ln u$.

Both intervals lie above $2$, since $\eta\le1/8$ gives $(1-2\eta)u/2\ge\frac34\cdot\frac u2>2$, so their primes are odd. They are disjoint, since $(1-\eta)u/2<(1-2\eta)u$ when $3\eta<1$. Each holds more than $d$ primes, so the $w$ axes with $t_i=u/2$ take distinct primes from the first interval, and the others take distinct primes from the second. For each axis $i$, its prime source length $s_i$ satisfies $(1-2\eta)\,t_i<s_i\le(1-\eta)\,t_i$.

<cite data-source="paper">Every gcd(si , ti ) equals one because ti is a power of two.</cite> The lengths are chosen as distinct [Prime number](prime-number.md)s. Distinct primes are pairwise coprime, so the lengths satisfy the pairwise form of [Coprime](coprime.md). The distinct primes supply pairwise coprime lengths to the [Chinese-remainder map](chinese-remainder-map.md).

## Product and separation

Let $S=s_1\cdots s_d$. The lengths $s_1,\dots,s_d$ set the place values of the [Mixed-radix digits](mixed-radix-digits.md) of the $S$ positions, with digit $i$ running from $0$ to $s_i-1$.

Since $s_i>(1-\frac1{2d})t_i$ for each $i$ and $\prod_i t_i=T$, we get $S>(1-\frac1{2d})^dT$. <cite data-source="paper">bounds on si and applying strict Bernoulli inequality gives</cite> $(1-\frac1{2d})^d>\frac12$. <cite data-source="paper">Together with si < ti , this gives T /2 < S < T .</cite>

Let $\theta_i=t_i/s_i-1$, the relative gap of axis $i$. From $s_i\le(1-\eta)t_i$ we get $\theta_i\ge\eta/(1-\eta)>\eta$.

The lengths must give the separation that [Gaussian resampling](gaussian-resampling.md) needs. Here $\alpha=\lceil(12d^2b)^{1/4}\rceil$ is the integer width of the Gaussian weights, and $p=6b$ is the working precision in bits (the letter $p$ changes meaning here, since it is not a prime). The requirement is $\alpha^4\theta_i>p$ on every axis. The resampling inverts an operator close to the identity, which needs $\alpha^2\theta>1$. <cite data-source="paper">Since α2 < p and θ > p/α4 , we have α2 θ > p/α2 > 1.</cite>

The choice of $\alpha$ gives $\alpha^4\ge12d^2b$, so $\alpha^4\eta\ge3db\ge6b=p$, and $\alpha^4\theta_i>\alpha^4\eta\ge p$. Also $\alpha\le2(12d^2b)^{1/4}$, since the ceiling of $A\ge1$ is at most $2A$. This gives $\alpha^2\le4\sqrt{12}\,d\sqrt b<6b=p$ for large $n$, so $\alpha^2\theta>p/\alpha^2>1$ holds.

## Cost of the search

The machine tests each candidate by trial division. There are at most $u$ candidates per interval, each needing at most $\sqrt u$ divisions of $\mathrm{poly}(b)$ operations, so the search costs $O(u^{3/2}\mathrm{poly}(b))$. Since $\ell<1+(b+3)/d$, this is $2^{O(b/d)+O(\log b)}=n^{o(1)}$, because $d\to\infty$.

## Worked example

Take $d=2$, so $\eta=1/8$, and $T=128$. Then $\ell=4$, $u=16$, and $w=1$, so $t_1=16$ and $t_2=8$. The interval $(12,14]$ contains only $13$, and $(6,7]$ contains only $7$, so $s_1=13$ and $s_2=7$, with $S=91$ and $64<91<128$. The gap $\theta_1=16/13-1\approx0.23$ exceeds $\eta/(1-\eta)=1/7$. Here $e^{2/\eta}=e^{16}$ exceeds $\xi$, so the bound does not apply and the primes are picked by hand.
