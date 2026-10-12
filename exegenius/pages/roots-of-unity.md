Let $n$ be a positive integer, the order of the root. Here $n$ has this meaning, not the bit length used on earlier pages.

A complex number $\omega$ is a primitive $n$-th root of unity if $\omega^n = 1$ and $\omega^k \neq 1$ for every integer exponent $k$ with $1 \le k < n$. Its successive powers $\omega, \omega^2, \dots$ are therefore all different until the first return to $1$, at $\omega^n$. This lets $\omega$ label the positions of a transform of length $n$: a map that combines a sequence of $n$ values by weighting each value with a power of $\omega$. The choice of root decides which values are combined.

The condition on $k$ is what separates a primitive root from an ordinary one. For $n = 4$, $i$ is primitive: $i^4 = 1$, while $i$, $i^2 = -1$ and $i^3 = -i$ are not $1$. The number $-1$ is a fourth root of unity but not a primitive one, since $(-1)^2 = 1$ already.

The condition also makes the powers distinct. Suppose $\omega^j = \omega^k$ for integer exponents $j$ and $k$ with $0 \le j < k < n$; here $j$ and $k$ are positions in the list of powers. Multiplying by $\omega^{-j}$ gives $\omega^{k-j} = 1$ with $0 < k-j < n$, which contradicts primitivity. So $1, \omega, \dots, \omega^{n-1}$ are pairwise different, and a transform of length $n$ never repeats a weight.
