A multidimensional transform is a Fourier transform taken over several [transform axes](transform-axis.md) at once, computed by transforming along one axis at a time. [Gaussian resampling](gaussian-resampling.md) uses it in place of the ordinary Fourier transforms of a convolution: the reduction <cite data-source="paper">replaces the Fourier transforms needed for this convolution by multidimensional transforms whose</cite> axis lengths are powers of two.

Let $D\ge 1$ be the number of axes. Let $\sigma$ be the index of an axis, with $1\le\sigma\le D$, and let $t_\sigma$ be the length of axis $\sigma$. Each $t_\sigma$ is a power of two, and $N=t_1t_2\cdots t_D$ is the number of entries of the array.

Let $X$ be the input array and $Y$ the output array. A position in $X$ is $\varrho=(\varrho_1,\dots,\varrho_D)$ with $0\le\varrho_\sigma<t_\sigma$ for every $\sigma$, and a position in $Y$ is $\varpi=(\varpi_1,\dots,\varpi_D)$ with the same bounds. Let $\mathcal F$ denote the multidimensional transform, which sends $X$ to $Y=\mathcal F X$ by the formula below.

$$
Y_\varpi=\frac{1}{N}\sum_{\varrho}\Big(\prod_{\sigma=1}^{D}e^{-2\pi i\,\varrho_\sigma\varpi_\sigma/t_\sigma}\Big)X_\varrho
$$

The transform $\mathcal F$ is built from the [discrete Fourier transforms](discrete-fourier-transform.md) $F_{t_1},\dots,F_{t_D}$ by [tensor product](tensor-product.md). Here $F_t$ has entries $\frac1t e^{-2\pi i\,\ell s/t}$. The entry of $A\otimes B$ at row $(a,b)$ and column $(a',b')$ is $A_{aa'}B_{bb'}$. Applying this to the $D$ factors, $F_{t_1}\otimes\cdots\otimes F_{t_D}$ has entry $\prod_{\sigma}\frac{1}{t_\sigma}e^{-2\pi i\,\varpi_\sigma\varrho_\sigma/t_\sigma}$ at row $\varpi$ and column $\varrho$. Since $\prod_\sigma t_\sigma=N$, this is the coefficient of $X_\varrho$ in the formula above. So $\mathcal F=F_{t_1}\otimes\cdots\otimes F_{t_D}$, where $F_{t_\sigma}$ acts on coordinate $\sigma$ alone.

The factors act on different coordinates, so they commute: $(A\otimes I)(I\otimes B)=A\otimes B=(I\otimes B)(A\otimes I)$. A line along axis $\sigma$ is the set of positions that agree in every coordinate except $\sigma$, and $F_{t_\sigma}$ changes values only within such lines. So $\mathcal F X$ is found in $D$ passes: transform every line along axis 1, then every line along axis 2, and so on.

## Worked example

Take $D=2$ and $t_1=t_2=2$, so $N=4$. For length 2 the root is $e^{-2\pi i/2}=-1$, so a pair $(u_0,u_1)$ goes to $\big((u_0+u_1)/2,\ (u_0-u_1)/2\big)$, where $u_0$ and $u_1$ are its entries. Let $X_{0,0}=1$, $X_{0,1}=2$, $X_{1,0}=3$ and $X_{1,1}=4$.

Along axis 2, the positions $(0,0)$ and $(0,1)$ form a line holding $1,2$, which becomes $3/2,\,-1/2$. The line at $(1,0)$ and $(1,1)$ holding $3,4$ becomes $7/2,\,-1/2$. Along axis 1, the line at $(0,0)$ and $(1,0)$ holding $3/2,\,7/2$ becomes $5/2,\,-1$, and the line at $(0,1)$ and $(1,1)$ holding $-1/2,\,-1/2$ becomes $-1/2,\,0$. So $Y_{0,0}=5/2$, $Y_{0,1}=-1/2$, $Y_{1,0}=-1$ and $Y_{1,1}=0$. The formula agrees at $\varpi=(0,1)$: $\frac14(1-2+3-4)=-\frac12$.

## Why the lengths are powers of two

A [two-point butterfly](butterfly.md) replaces a pair $(u_0,u_1)$ by $(u_0+u_1,\,u_0-u_1)$ up to a scalar; the length-2 step above is one, with scalar $\tfrac12$. Let $k$ be the exponent with $t_\sigma=2^k$, so $k$ counts the radix-two levels of the axis (here $k$ means this exponent, not the padded length of earlier pages). The one-dimensional transform along axis $\sigma$ is computed by the [radix-two factorization](radix-two-factorization.md) as $k$ levels of butterflies, with multiplications by roots of unity between the levels.

The multidimensional transform is written in the representation of [synthetic polynomial transforms](synthetic-transforms.md). In it, <cite data-source="paper">one coordinate is stored as the coefficient list of a polynomial modulo y r + 1, with r a power of two</cite>, so $y^r=-1$. <cite data-source="paper">Powers of y then serve as roots of unity in the remaining axes</cite>: for an axis of length $t_\sigma$ dividing $2r$, the power $y^{2r/t_\sigma}$ is a $t_\sigma$-th root of unity, because its $t_\sigma$-th power is $y^{2r}=(y^r)^2=1$.

Multiplying a record by $y^s$, with $0\le s<r$, moves the coefficient at position $d$ to position $d+s$. If $d+s\ge r$, then $y^{d+s}=-y^{d+s-r}$, so the coefficient lands at $d+s-r$ with a minus sign. For $r=4$, $y\,(c_0+c_1y+c_2y^2+c_3y^3)=-c_3+c_0y+c_1y^2+c_2y^3$, since $y^4=-1$. This is a [cyclic shift](cyclic-shift.md) of the coefficient list with the wrapped entries negated. In this representation, the transform turns roots of unity into [signed cyclic shifts](cyclic-shift.md). Consequently <cite data-source="paper">the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations.</cite>
