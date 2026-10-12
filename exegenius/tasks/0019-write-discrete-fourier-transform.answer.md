The discrete Fourier transform is the linear map that sends a vector of complex values to a vector of the same length, each entry a weighted sum of the inputs with powers of a root of unity as weights. It is the tool behind the [radix-digit convolution](radix-digit-convolution.md) step of the paper's integer multiplication.

Let $q$ be the number of entries in each vector. Here $j$ indexes the output entries and $k$ the input entries, both from $0$ to $q-1$. Let $\omega$ be a primitive $q$-th root of unity, so $\omega^q=1$ and $\omega^j\ne1$ for $0<j<q$.

The transform $F_q$ maps the input vector $x = (x_0,\dots,x_{q-1})$ to the output vector $y = F_q x$, with
$$y_j = \frac{1}{q}\sum_{k=0}^{q-1}\omega^{jk}x_k.$$
Here $x$ and $y$ are these vectors, not the integer inputs above.

The map is invertible, with inverse $x_l=\sum_{j=0}^{q-1}\omega^{-jl}y_j$, where $l$ indexes the entries of $x$ and there is no factor $1/q$. Substituting the formula for $y_j$ gives
$$\sum_{j=0}^{q-1}\omega^{-jl}y_j=\frac{1}{q}\sum_{k=0}^{q-1}x_k\sum_{j=0}^{q-1}\omega^{j(k-l)}.$$
Let $m$ be an integer and consider $\sum_{j=0}^{q-1}\omega^{jm}$. If $q$ divides $m$, every term is $1$ and the sum is $q$. Otherwise $\omega^m\ne1$, since $\omega^m=\omega^{m \bmod q}$ with $0<(m \bmod q)<q$, and $(\omega^m-1)\sum_{j}\omega^{jm}=(\omega^m)^q-1=0$, so the sum is $0$. Since $k$ and $l$ lie in $0,\dots,q-1$, $q$ divides $k-l$ only when $k=l$. The $1/q$ then cancels the $q$ from the sum, leaving $x_l$.

The transform [reduces cyclic convolution](cyclic-convolution.md) to a pointwise product. For vectors $a$ and $b$ of length $q$, put $(a\ast b)_l=\sum_{k=0}^{q-1}a_k\,b_{(l-k)\bmod q}$. For fixed $k$, put $t=(l-k)\bmod q$, which runs over $0,\dots,q-1$ as $l$ does. Since $\omega^{jl}=\omega^{jk}\omega^{jt}$ when $\omega^q=1$,
$$\sum_{l}\omega^{jl}(a\ast b)_l=\sum_{k}a_k\omega^{jk}\sum_{t}b_t\omega^{jt}=q^2(F_qa)_j(F_qb)_j,$$
so $(F_q(a\ast b))_j=q\,(F_qa)_j\,(F_qb)_j$. Applying the inverse to this gives
$$\sum_{j}\omega^{-jl}(F_qa)_j(F_qb)_j=\frac{1}{q}\sum_{j}\omega^{-jl}(F_q(a\ast b))_j=\frac{1}{q}(a\ast b)_l.$$
So transforming, multiplying pointwise and inverting gives the convolution divided by $q$.
