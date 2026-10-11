A prime number is an [Integer](integer.md) greater than one whose only positive divisors are one and itself. In the argument, primes serve as the lengths of cyclic axes: the radix-digit coefficients are placed on distinct prime cyclic axes by a Chinese-remainder map, <cite data-source="paper">prime cyclic axes by a Chinese-remainder map that preserves convolution</cite>, and that map needs its axis lengths to be pairwise coprime.

A positive integer $a$ is a divisor of an integer $m$ when $m=ak$ for some integer $k$. Write $p$ for a prime number. Then $p>1$, and the only positive integers that divide $p$ are $1$ and $p$.

Examples: $2$, $3$, $5$, $7$ and $13$ are prime. The number $1$ is not prime, since it fails $p>1$. The number $12$ is not prime, since $12=3\cdot4$ and $2$ divides it. The number $91=7\cdot13$ is not prime.

Let $p$ and $q$ be distinct primes. Their only common positive divisor is $1$. A common divisor $a>1$ would divide $p$, so $a=p$, and it would divide $q$, so $a=q$, which contradicts $p\neq q$. Hence $p$ and $q$ are [Coprime](coprime.md), and any collection of distinct primes is pairwise coprime. This is the property the [Chinese remainder theorem](chinese-remainder-theorem.md) needs of its moduli, so distinct primes are a convenient source of axis lengths that can be combined by that theorem.
