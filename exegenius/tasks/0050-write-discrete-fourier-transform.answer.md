The discrete Fourier transform is the linear map that sends a vector of complex values to a vector of the same length, each entry a weighted sum of the inputs with powers of a root of unity as weights. It is the tool behind the [radix-digit convolution](radix-digit-convolution.md) step of the paper's integer multiplication <cite data-source="paper">We now implement the normalized Fourier transforms needed for convolution</cite>.

Let $q$ be the number of entries in each vector. Here $j$ indexes the output entries, $k$ the input entries and $l$ the entries of the inverse, all from $0$ to $q-1$. Let $\omega$ be a primitive $q$-th root of unity, so $\omega^q=1$ and $\omega^j\ne1$ for $0<j<q$.

The transform $F_q$ maps the input vector $x = (x_0,\dots,x_{q-1})$ to the output vector $y = F_q x$, with
$$y_j = \frac{1}{q}\sum_{k=0}^{q-1}\omega^{jk}x_k.$$
Here $x$ and $y$ are these vectors, not the integer inputs above.

The map is invertible, with inverse $x_l=\sum_{j=0}^{q-1}\omega^{-jl}y_j$ and no factor $1/q$. To check this, substitute the formula for $y_j$:
$$\sum_{j=0}^{q-1}\omega^{-jl}y_j=\frac{1}{q}\sum_{k=0}^{q-1}x_k\sum_{j=0}^{q-1}\omega^{j(k-l)}.$$
For an integer $d$, $\sum_{j=0}^{q-1}\omega^{jd}$ equals $q$ if $q$ divides $d$, since every term is $1$. Otherwise $\omega^d=\omega^{d \bmod q}\ne1$, and $(\omega^d-1)\sum_{j}\omega^{jd}=(\omega^d)^q-1=0$, so the sum is $0$. Since $k,l\in\{0,\dots,q-1\}$, $q$ divides $k-l$ only when $k=l$, so the $1/q$ cancels the $q$ and leaves $x_l$.

The transform [reduces cyclic convolution](cyclic-convolution.md) to a pointwise product, the entrywise product of two vectors. For vectors $a$ and $b$ of length $q$, let $c=a\ast b$, so $c_l=\sum_{k=0}^{q-1}a_k\,b_{(l-k)\bmod q}$. For fixed $k$, put $r=(l-k)\bmod q$, which runs over $0,\dots,q-1$ as $l$ does. Since $\omega^{jl}=\omega^{jk}\omega^{jr}$,
$$\sum_{l}\omega^{jl}c_l=\sum_{k}a_k\omega^{jk}\sum_{r}b_r\omega^{jr}=q^2(F_qa)_j(F_qb)_j,$$
so $(F_qc)_j=q\,(F_qa)_j(F_qb)_j$. Applying the inverse gives
$$\sum_{j}\omega^{-jl}(F_qa)_j(F_qb)_j=\frac{1}{q}\sum_{j}\omega^{-jl}(F_qc)_j=\frac{1}{q}c_l.$$
So transforming, multiplying pointwise and inverting gives the convolution divided by $q$.
