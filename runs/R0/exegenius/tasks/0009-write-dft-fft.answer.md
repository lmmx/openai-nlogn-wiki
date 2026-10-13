The discrete Fourier transform (DFT) evaluates a coefficient list at the powers of a root of unity, and it reduces [Convolution](convolution.md) to a pointwise product, the operation that multiplies entries with equal index.

Let $n$ be a power of two, the number of coefficients in a list $a=(a_0,\dots,a_{n-1})$. Let $\omega$ be a primitive $n$-th root of unity, a complex number with $\omega^n=1$ whose smaller powers $\omega^m$, $0<m<n$, are all different from $1$. The transform of $a$ is the list $A=(A_0,\dots,A_{n-1})$ with

$$A_k=\sum_{j=0}^{n-1} a_j\,\omega^{jk}.$$

Each $A_k$ is the value of the polynomial $\sum_j a_j x^j$ at $x=\omega^k$.

A butterfly is the two-point operation $(u,v)\mapsto(u+\omega^s v,\; u-\omega^s v)$ for some power $\omega^s$. The fast transform applies butterflies in $\log_2 n$ levels: at each level it pairs entries whose indices differ in one bit and replaces each pair by its butterfly, so the total work is $O(n\log n)$. The tape-level transform in the source is built the same way, from <cite data-source="paper">two-point butterfly operations</cite> together with address rearrangements and signed shifts.

Why this helps: let $b$ be a second list and let $c_k=\sum_i a_i\,b_{(k-i)\bmod n}$ be the cyclic convolution of $a$ and $b$. Its transform $C_m=\sum_k c_k\omega^{km}$ equals $A_m B_m$ for every $m$. To see this, set $l=(k-i)\bmod n$; since $\omega^n=1$, $\omega^{km}=\omega^{(i+l)m}$, so $C_m=\sum_i a_i\omega^{im}\sum_l b_l\omega^{lm}=A_mB_m$. Transforming both lists, multiplying entrywise, and transforming back therefore gives the convolution.

For example, with $n=2$ we have $\omega=-1$ and $A_0=a_0+a_1$, $A_1=a_0-a_1$. This is a single butterfly with $u=a_0$, $v=a_1$, $s=0$.
