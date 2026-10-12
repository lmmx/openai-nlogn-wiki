Let $n$ be a positive integer, the order of the root. A primitive $n$-th root of unity is a complex number whose successive powers are all different until the first return to $1$. This is what lets it label the positions of a transform of length $n$: transforms of the kind used later weight a sequence by powers of such a number, so the choice of root determines which values are combined.

A complex number $\omega$ is a primitive $n$-th root of unity if $\omega^n = 1$ and $\omega^k \neq 1$ for every integer $k$ with $1 \le k < n$.

The condition on $k$ is what separates a primitive root from an ordinary one. For $n = 4$, $i$ is primitive: $i^4 = 1$, while $i$, $i^2 = -1$ and $i^3 = -i$ are not $1$. The number $-1$ is a fourth root of unity but not a primitive one, since $(-1)^2 = 1$ already. The number $1$ is a primitive root only when $n = 1$.

The condition makes the powers distinct. If $\omega$ is primitive and $\omega^j = \omega^k$ with $0 \le j < k < n$, then $\omega^{k-j} = 1$ with $0 < k-j < n$, which is impossible. So the $n$ powers $1, \omega, \dots, \omega^{n-1}$ are pairwise different, and a transform of length $n$ that uses them as weights never repeats a weight.
