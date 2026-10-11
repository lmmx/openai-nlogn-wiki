The discrete Fourier transform is built as a [Linear map](linear-map.md) that sends a vector of complex numbers to another vector of the same length. It reduces [Radix-digit convolution](radix-digit-convolution.md) to pointwise products of transformed vectors.

Let $q$ be the number of values in each vector. Let $\omega$ be a primitive $q$-th root of unity: $\omega^q=1$, and $\omega^m\neq 1$ for each integer exponent $m$ with $0<m<q$. Write $j$ and $k$ for the input and output positions, each running from $0$ to $q-1$. Write $u=(u_0,\dots,u_{q-1})$ for a vector of $q$ values, and $F_q$ for the transform map:

$$(F_q u)_k=\frac{1}{q}\sum_{j=0}^{q-1}\omega^{jk}u_j.$$

The opposite transform $F_q^+$ replaces $\omega$ by $\omega^{-1}$. Applying $F_q^+$ after $F_q$ gives $u/q$, not $u$, because a sum of powers of $\omega$ over one full period is $q$ when the exponent is a multiple of $q$ and $0$ otherwise.

For vectors $u$ and $v$, the cyclic convolution $u*v$ is defined by $(u*v)_k=\sum_{j=0}^{q-1}u_j\,v_{(k-j)\bmod q}$. Writing $\cdot$ for the entrywise product,

$$F_q^+\big((F_q u)\cdot(F_q v)\big)=\frac{u*v}{q^2}.$$

Expanding the sums, the powers of $\omega$ cancel except for products of entries whose positions add to $k$ modulo $q$; the three factors $1/q$ and the surviving full-period sum, which contributes $q$, leave $1/q^2$.

The paper fixes where each transformed entry is stored<cite data-source="paper">We also specify where each frequency entry is stored, because the opposite transform consumes that same order after a pointwise product</cite>, and the opposite transform reads entries in that same order.
