Modular arithmetic is integer arithmetic in which each value is replaced by its remainder on division by a fixed modulus $q$, so an index that passes $q-1$ wraps around to $0$. It lets the transforms below index their entries without special cases at the ends of a vector.

For an integer $m$, $m \bmod q$ denotes the remainder $r$ with $0 \le r < q$ and $m = sq + r$ for some integer $s$. Here $q$ is the modulus, which is also the vector length of the transform.

Modular arithmetic is applied to the indices of the [Discrete Fourier transform](discrete-fourier-transform.md) $F_q$, a map on vectors of $q$ values. Subscripts on a vector of length $q$ are taken modulo $q$ <cite data-source="paper">All subscripts on a vector of length q are taken modulo q.</cite> For example, with $q = 4$, the position after $3$ is $(3+1) \bmod 4 = 0$, and the position before $0$ is $(0-1) \bmod 4 = 3$.
