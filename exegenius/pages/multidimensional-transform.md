A multidimensional transform is a Fourier transform taken over several [transform axes](transform-axis.md) at once, computed by transforming along one axis at a time. [Gaussian resampling](gaussian-resampling.md) uses it in place of the ordinary Fourier transforms of a convolution: the reduction <cite data-source="paper">replaces the Fourier transforms needed for this convolution by multidimensional transforms whose</cite> axis lengths are powers of two.

Let $D\ge 1$ be the number of axes. For an axis $\varsigma$ with $1\le\varsigma\le D$, let $t_\varsigma$ be the length of that axis, the number of values its coordinate takes. Each $t_\varsigma$ is a power of two, and $N=t_1t_2\cdots t_D$ is the number of entries of the array.

Let $X$ be the input array. A position in $X$ is a tuple $\mathbf{x}=(x_1,\dots,x_D)$ with $0\le x_\varsigma<t_\varsigma$ for every $\varsigma$, where $x_\varsigma$ is the coordinate along axis $\varsigma$. A position $\mathbf{x}'=(x'_1,\dots,x'_D)$ in the output has the same bounds. Let $\mathcal F$ denote the multidimensional transform, which sends $X$ to the array $\mathcal F X$ by

$$
(\mathcal F X)_{\mathbf x'}=\frac1N\sum_{\mathbf x}\Big(\prod_{\varsigma=1}^{D}e^{-2\pi i\,x_\varsigma x'_\varsigma/t_\varsigma}\Big)X_{\mathbf x}.
$$

The multidimensional transform $\mathcal F$ is built from the [discrete Fourier transforms](discrete-fourier-transform.md) $F_{t_1},\dots,F_{t_D}$ by [tensor product](tensor-product.md). Here $F_t$ has entry $\frac1t e^{-2\pi i\,\ell s/t}$ in row $\ell$ and column $s$. The entry of a tensor product of matrices is the product of the entries of its factors, so $F_{t_1}\otimes\cdots\otimes F_{t_D}$ has entry $\prod_\varsigma\frac1{t_\varsigma}e^{-2\pi i\,x'_\varsigma x_\varsigma/t_\varsigma}$ at row $\mathbf x'$ and column $\mathbf x$. Since $\prod_\varsigma t_\varsigma=N$, this is the coefficient of $X_{\mathbf x}$ in the formula above, so $\mathcal F=F_{t_1}\otimes\cdots\otimes F_{t_D}$, where $F_{t_\varsigma}$ acts on coordinate $\varsigma$ alone.

The factors act on different coordinates, so they commute. A line along axis $\varsigma$ is the set of positions that agree in every coordinate except $x_\varsigma$, and $F_{t_\varsigma}$ changes values only within such lines. So $\mathcal F X$ is found in $D$ passes: transform every line along axis 1, then every line along axis 2, and so on.

## Worked example

Take $D=2$ and $t_1=t_2=2$, so $N=4$. For length 2 the root is $e^{-2\pi i/2}=-1$, so a pair $(\xi,\zeta)$ goes to $\big((\xi+\zeta)/2,\ (\xi-\zeta)/2\big)$. Let $X_{0,0}=1$, $X_{0,1}=2$, $X_{1,0}=3$ and $X_{1,1}=4$.

Along axis 2, the positions $(0,0)$ and $(0,1)$ form a line holding $1,2$, which becomes $3/2,\,-1/2$. The line at $(1,0)$ and $(1,1)$ holding $3,4$ becomes $7/2,\,-1/2$. Along axis 1, the line at $(0,0)$ and $(1,0)$ holding $3/2,\,7/2$ becomes $5/2,\,-1$, and the line at $(0,1)$ and $(1,1)$ holding $-1/2,\,-1/2$ becomes $-1/2,\,0$. So $(\mathcal F X)_{0,0}=5/2$, $(\mathcal F X)_{0,1}=-1/2$, $(\mathcal F X)_{1,0}=-1$ and $(\mathcal F X)_{1,1}=0$. The formula agrees at $\mathbf x'=(0,1)$: $\frac14(1-2+3-4)=-\frac12$.

## Why the lengths are powers of two

A [two-point butterfly](butterfly.md) replaces a pair $(\xi,\zeta)$ by $(\xi+\zeta,\ \xi-\zeta)$ up to a scalar; the length-2 step above is one, with scalar $\tfrac12$. Write $\lg t_\varsigma$ for the base-2 logarithm of $t_\varsigma$, the number of radix-two levels of axis $\varsigma$. Each axis transform is computed by the [radix-two factorization](radix-two-factorization.md) as $\lg t_\varsigma$ levels of butterflies, with multiplications by roots of unity between the levels.

The multidimensional transform is written in the representation of [synthetic polynomial transforms](synthetic-transforms.md). In it, one coordinate is stored <cite data-source="paper">as the coefficient list of a polynomial modulo y r + 1, with r a power of two</cite>, so $y^r=-1$. Powers of $y$ then serve <cite data-source="paper">as roots of unity in the remaining axes</cite>: for an axis of length $t_\varsigma$ dividing $2r$, the power $y^{2r/t_\varsigma}$ is a $t_\varsigma$-th root of unity, because its $t_\varsigma$-th power is $y^{2r}=(y^r)^2=1$.

Multiplying a record by $y^\sigma$, with $0\le\sigma<r$, moves the coefficient at position $\rho$ to position $\rho+\sigma$. If $\rho+\sigma\ge r$, then $y^{\rho+\sigma}=-y^{\rho+\sigma-r}$, so the coefficient lands at $\rho+\sigma-r$ with a minus sign. For $r=4$, $y\,(a_0+a_1y+a_2y^2+a_3y^3)=-a_3+a_0y+a_1y^2+a_2y^3$, since $y^4=-1$. This shifts the coefficient list cyclically with the wrapped entry negated. In this representation, the transform turns roots of unity into [signed cyclic shifts](cyclic-shift.md). So <cite data-source="paper">the transform calculation consists of address rearrangements, signed</cite> <cite data-source="paper">shifts, and two-point butterfly operations.</cite>
