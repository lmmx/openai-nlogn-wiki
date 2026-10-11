A multidimensional transform is a Fourier transform taken over several [transform axes](transform-axis.md) at once, computed by transforming along one axis at a time. [Gaussian resampling](gaussian-resampling.md) uses it in place of the ordinary Fourier transforms of the convolution: the reduction <cite data-source="paper">replaces the Fourier transforms needed for this convolution by multidimensional transforms whose</cite> axis lengths are powers of two.

Let $D\ge 1$ be the number of axes. Let $s$ be the index of an axis, with $1\le s\le D$, and let $t_s$ be the length of axis $s$. Each $t_s$ is a power of two. Let $N=t_1t_2\cdots t_D$ be the number of entries of the array. Here $\pi$ is the ratio of a circle's circumference to its diameter.

Let $X$ be the input array and $Y$ the output array. A position in $X$ is $\nu=(\nu_1,\dots,\nu_D)$ with $0\le\nu_s<t_s$ for every $s$, and a position in $Y$ is $\kappa=(\kappa_1,\dots,\kappa_D)$ with the same bounds. Let $\mathcal F$ denote the multidimensional transform, which sends $X$ to $Y=\mathcal F X$ by the formula below.

$$
Y_\kappa=\frac{1}{N}\sum_{\nu}\Big(\prod_{s=1}^{D}e^{-2\pi i\,\nu_s\kappa_s/t_s}\Big)X_\nu
$$

Here $i$ is the imaginary unit.

The transform $\mathcal F$ is built from the [discrete Fourier transforms](discrete-fourier-transform.md) $F_{t_1},\dots,F_{t_D}$ by [tensor product](tensor-product.md). The tensor product $\otimes$ applies each factor to its own coordinate and leaves the other coordinates unchanged, so $\mathcal F=F_{t_1}\otimes\cdots\otimes F_{t_D}$. Each $F_{t_s}$ acts on coordinate $s$ alone, with root $e^{-2\pi i/t_s}$ and normalization $1/t_s$; these multiply to $1/N$.

Since the factors act on different coordinates, they commute. A line along axis $s$ is the set of positions that agree in every coordinate except $\nu_s$, and the factor for axis $s$ changes values only along such lines. So $\mathcal F X$ is found in $D$ passes: transform every line along axis 1, then every line along axis 2, and so on.

## Worked example

Take $D=2$ and $t_1=t_2=2$, so $N=4$. For length $2$ the root is $e^{-2\pi i/2}=-1$, so the one-dimensional transform sends a pair $(u_0,u_1)$ to $\big((u_0+u_1)/2,\ (u_0-u_1)/2\big)$, with $u_0,u_1$ the entries of the pair. Let $X_{0,0}=1$, $X_{0,1}=2$, $X_{1,0}=3$ and $X_{1,1}=4$.

Along axis 2, the positions $(0,0)$ and $(0,1)$ form a line holding $1,2$, which becomes $3/2,\,-1/2$. The line at $(1,0)$ and $(1,1)$ holding $3,4$ becomes $7/2,\,-1/2$. Along axis 1, the line at $(0,0)$ and $(1,0)$ holding $3/2,\,7/2$ becomes $5/2,\,-1$, and the line at $(0,1)$ and $(1,1)$ holding $-1/2,\,-1/2$ becomes $-1/2,\,0$. So $Y_{0,0}=5/2$, $Y_{0,1}=-1/2$, $Y_{1,0}=-1$ and $Y_{1,1}=0$. The formula agrees at $\kappa=(0,1)$: $\frac14(1-2+3-4)=-\frac12$.

## Why the lengths are powers of two

A [two-point butterfly](butterfly.md) replaces a pair $(u_0,u_1)$ by $(u_0+u_1,\,u_0-u_1)$ up to a scalar; the length-2 step above is one, with scalar $1/2$. For $t_s=2^k$, the standard radix-two factorization writes the one-dimensional transform as $k$ levels of such butterflies, with multiplications by roots of unity between the levels.

In the paper's representation those root multiplications become cheap. Here $y$ is the variable of the polynomial storing one coordinate. <cite data-source="paper">Powers of y then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list.</cite> A multidimensional transform with power-of-two lengths turns the roots of unity into [signed shifts](cyclic-shift.md), which rotate a coefficient list and negate the entries that wrap around. In this representation, <cite data-source="paper">the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations.</cite>
