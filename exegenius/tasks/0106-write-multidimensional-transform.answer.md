A multidimensional transform is a Fourier transform taken over several [transform axes](transform-axis.md) at once, computed by transforming along each axis in turn. [Gaussian resampling](gaussian-resampling.md) uses it in place of the ordinary Fourier transforms of the convolution: the reduction <cite data-source="paper">replaces the Fourier transforms needed for this convolution by multidimensional transforms whose</cite> axis lengths are powers of two.

Let $D \ge 1$ be the number of axes, a positive integer. The transform acts over the [transform axes](transform-axis.md) $1,\dots,D$. Write $s$ for the index of an axis, running from $1$ to $D$. Write $t_s$ for the length of axis $s$, the number of coordinates along it, which is a power of two in the argument. Write $M = t_1 t_2 \cdots t_D$ for the number of entries of the array. Write $X$ for the input array and $Y$ for the output array. Write $m=(m_1,\dots,m_D)$ for a position in $X$ and $h=(h_1,\dots,h_D)$ for a position in $Y$, each with $0\le m_s<t_s$ for every $s$. The multidimensional transform $\mathcal F$ sends $X$ to $Y = \mathcal F X$ by the formula below.

$$
Y_h = \frac{1}{M}\sum_{m}\Big(\prod_{s=1}^{D} e^{-2\pi i\, m_s h_s/t_s}\Big)\, X_m
$$

The sum runs over all positions $m$. The transform $\mathcal F$ is built from the [discrete Fourier transforms](discrete-fourier-transform.md) $F_{t_1},\dots,F_{t_D}$ by tensor product, one on each axis: $\mathcal F = F_{t_1}\otimes\cdots\otimes F_{t_D}$. Each factor carries its own normalization $1/t_s$, and their product is the $1/M$ in the formula.

A line along axis $s$ is the set of positions that agree in every coordinate except $m_s$. Each factor $F_{t_s}$ acts only on the coordinate $m_s$, so the factors commute. Hence $\mathcal F X$ is found in one pass per axis: transform every line along axis 1, then every line along axis 2, and so on. The sources compute it the same way: <cite data-source="paper">For the tensor product, apply the one-dimensional maps to one coordinate line at a time.</cite>

## Worked example

Take $D=2$ and $t_1=t_2=2$, so $M=4$. For length $2$ the root is $e^{-2\pi i/2}=-1$, so the one-dimensional transform sends $(u_0,u_1)$ to $\big((u_0+u_1)/2,\ (u_0-u_1)/2\big)$. Let $X_{0,0}=1$, $X_{0,1}=2$, $X_{1,0}=3$ and $X_{1,1}=4$.

Along axis 2, each row is transformed: the row $(1,2)$ becomes $(3/2,\,-1/2)$ and the row $(3,4)$ becomes $(7/2,\,-1/2)$. Along axis 1, each column is then transformed: $(3/2,\,7/2)$ becomes $(5/2,\,-1)$ and $(-1/2,\,-1/2)$ becomes $(-1/2,\,0)$. So $Y_{0,0}=5/2$, $Y_{0,1}=-1/2$, $Y_{1,0}=-1$ and $Y_{1,1}=0$. The formula agrees at $h=(0,1)$: $\frac14(1-2+3-4)=-\frac12$.

## Why axis lengths are powers of two

A two-point butterfly replaces a pair of entries by their sum and their difference, up to a scalar. When every $t_s$ is a power of two, each one-dimensional transform is a sequence of such butterflies with multiplications by roots of unity between them. In the sources' representation, <cite data-source="paper">the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations.</cite> Restricting the axis lengths to powers of two is what makes the roots of unity signed shifts.
