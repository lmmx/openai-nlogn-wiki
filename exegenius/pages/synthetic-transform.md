A synthetic polynomial transform is a transform over the [Polynomial ring modulo y^r + 1](ring-y.md) whose roots of unity are powers of $y$, so every twiddle multiplication (multiplication by a root of unity) is a signed shift of a coefficient list. It lets the other axes of a multidimensional transform be handled without complex multiplications.

In that ring $y^r=-1$, so multiplying a record by $y^s$ moves each coefficient up $s$ places and negates those that wrap past degree $r-1$. Powers of $y$ can therefore serve as roots of unity, and multiplication by such a root is a signed shift of the coefficient list <cite data-source="paper">Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list.</cite>.

For example, take $r=4$: multiplying $a_0+a_1y+a_2y^2+a_3y^3$ by $y^2$ gives $-a_2-a_3y+a_0y^2+a_1y^3$.

Let $t$ be the transform length, the number of ring elements along one axis, a power of two dividing $2r$. Define $\omega_t=y^{2r/t}$ <cite data-source="paper">For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$.</cite>. Since $y^{2r}=1$ and $y^r=-1$, we get $\omega_t^t=1$ and $\omega_t^{t/2}=-1$, as for a primitive $t$-th root of unity in the complex case.

The synthetic transforms are given by the formulas of the [Discrete Fourier transform](dft.md), with $\omega_t$ in place of $e^{2\pi i/q}$:

$$(F_t^-z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{-jk}z_k,\qquad (F_t^+z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{jk}z_k .$$

Here $z=(z_0,\dots,z_{t-1})$ is a list of $t$ ring elements and $0\le j<t$. A signed shift only permutes and negates coefficients, so every power of $\omega_t$ preserves their size; each entry is an average of $t$ such images, hence both transforms are contractions <cite data-source="paper">Every power of $\omega_t$ is an isometry, and each transform entry is an average of $t$ such images.</cite>.

The ring has zero divisors, so one cannot undo $F_t^-$ by dividing by $\omega_t^j-1$ as over the complex numbers. Instead the cancellation of sums of powers of $\omega_t$ is verified directly <cite data-source="paper">The ring has zero divisors, so we verify character cancellation directly instead of dividing by $\omega_t^j-1$.</cite>.

As in the complex case, $F_t^-$ is computed by the layered scheme of [Butterflies and the fast transform](butterfly.md) in $\log_2 t$ layers of two-point averaging and differencing steps. Here each twiddle multiplication in a layer is a signed shift of a record. Later pages choose where the outputs sit on the tape, in which order they are kept, and how the pointwise products between the two transforms are formed.
