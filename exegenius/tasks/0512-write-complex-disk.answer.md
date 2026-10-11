A closed disk in the complex plane is the set of complex numbers within a fixed distance of a fixed center. The paper keeps the coefficients of its intermediate arrays inside such a disk, which bounds their size and gives the error analysis a fixed bound to work with.

Let $\mathbb{C}$ be the set of complex numbers. Let $\xi$ be the center of the disk, a complex number, and $\rho$ the radius, a nonnegative real number. Let $\zeta$ be a generic point of the plane. The closed disk $\mathcal{D}(\xi,\rho)$ is the set of points within distance $\rho$ of $\xi$:
$$\mathcal{D}(\xi,\rho) = \{\zeta \in \mathbb{C} : |\zeta - \xi| \le \rho\}.$$
Here $|\zeta - \xi|$ is the modulus of $\zeta - \xi$, the distance from $\zeta$ to $\xi$. The disk is closed because the boundary circle, where the distance equals $\rho$, belongs to it.

For example, the unit disk $\mathcal{D}(0,1)$ contains the point $1$, since $|1| = 1 \le 1$, and it contains $\tfrac{1+i}{2}$, whose modulus is $\tfrac{\sqrt{2}}{2} \approx 0.71$. It does not contain $1+i$, since $|1+i| = \sqrt{2} > 1$.

The paper uses a grid version of the unit disk. Let $\mathbb{Z}[i]$ be the Gaussian integers, the complex numbers whose real and imaginary parts are both integers. Let $\varepsilon$ be a generic Gaussian integer. For a precision $p$, the grid disk $\mathcal{D}_p$ is the set
$$\mathcal{D}_p = \{\, 2^{-p}\varepsilon : \varepsilon \in \mathbb{Z}[i],\ |\varepsilon| \le 2^{p} \,\}.$$
Its points are the points of the unit disk whose real and imaginary parts are multiples of $2^{-p}$. The paper stores each such point as a pair of integers: <cite data-source="paper">Represent 2−p (a + ib) ∈ Dp by a</cite>. For $p = 1$, the point $1 = 2^{-1}\cdot 2$ lies in $\mathcal{D}_1$, and so does $\tfrac{1+i}{2} = 2^{-1}(1+i)$, since $|1+i|^2 = 2 \le 4$. The point $\tfrac{2+i}{2}$ does not, since $|2+i|^2 = 5 > 4$.

The paper's record coefficients start in the unit disk on the grid $2^{-p}\mathbb{Z}[i]$, which is the set $\mathcal{D}_p$ above: <cite data-source="paper">initially in the unit disk on the grid 2−p Z[i]</cite>. Its routines keep their returned values in the disk as well: <cite data-source="paper">coefficient belongs to the complex unit disk, and, in the maximum coefficient norm,</cite>.
