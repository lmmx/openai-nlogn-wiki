A synthetic polynomial transform is a discrete Fourier transform whose roots of unity are powers of $y$, so each multiplication by a root is a signed shift. It computes the convolution step of the integer product with shifts and butterflies.

The transform is computed over the [Polynomial ring modulo yʳ + 1](polynomial-ring.md). It takes its roots from the powers of $y$, which are a [Root of unity](roots-of-unity.md) of order $2r$. Write the twiddle factors as $y^\sigma$, where $\sigma$ is the exponent of the twiddle factor, an integer from $0$ to $2r-1$. A twiddle factor is the root a butterfly multiplies by.

Multiplying by $y^\sigma$ with $\sigma<r$ moves each coefficient $\sigma$ places up, and a coefficient that passes position $r-1$ returns with its sign reversed; $y^{\sigma+r}=-y^\sigma$ covers the rest. For $r=4$, using $y^4=-1$,
$$y\,(a_0+a_1y+a_2y^2+a_3y^3)=-a_3+a_0y+a_1y^2+a_2y^3.$$
Each such multiplication is a signed shift of the coefficient list <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>.

It computes normalized [Cyclic convolution](cyclic-convolution.md) on the power-of-two axes. Let $\theta$ be a primitive $S$-th root of unity such that $\theta^m-1$ is invertible for $0<m<S$; the powers of $y$ satisfy this with $S=2r$. Let $\xi$ and $\eta$ be lists of $S$ coefficients. The transform of a list $\xi$ is $\hat\xi$, with $\hat\xi_k=\frac1S\sum_{j}\xi_j\theta^{jk}$. Let $\psi$ be their normalized cyclic convolution, $\psi_l=\frac1S\sum_{i+j\equiv l \pmod S}\xi_i\eta_j$. Since $\theta^{lk}$ depends only on $l \bmod S$, $\hat\psi_k=\frac1{S^2}\sum_{i,j}\xi_i\eta_j\theta^{(i+j)k}=\hat\xi_k\,\hat\eta_k$.

The transform is computed by successive layers of [Simultaneous butterfly layer H₀](butterfly-layer.md). Let $\beta$ be the number of layers. A layer pairs records whose indices differ in one selected bit, multiplies one record of each pair by its twiddle factor, and replaces the pair $(u,v)$ by $H_0(u,v)=((u+v)/2,(u-v)/2)$.

Assume the input coefficients are Gaussian dyadic numbers. Signed shifts and sums keep them Gaussian dyadic, and halving $m/2^f$ gives $m/2^{f+1}$, where halving <cite data-source="paper">halving adds at most one denominator bit</cite>. Each layer halves at most once, so after $\beta$ layers every denominator is at most $2^\beta$ times that of the inputs, and all intermediate values stay exact Gaussian dyadic numbers.
