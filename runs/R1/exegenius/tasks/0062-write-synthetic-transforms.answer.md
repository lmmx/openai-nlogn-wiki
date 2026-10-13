Synthetic polynomial transforms are defined over the [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md), where $y^r=-1$, and every twiddle factor is a power of $y$. So they need only signed shifts, address rearrangements and butterflies.

Take $r=4$ and multiply $1+2y+3y^2+4y^3$ by $y^2$: the result is $-3-4y+y^2+2y^3$. In coefficient-list form, $(1,2,3,4)$ becomes $(-3,-4,1,2)$: each coefficient moves up two places, and the two that wrap past the end return negated.

Let the transform act on a list $z_0,\dots,z_{t-1}$ of ring elements, where $t$, the number of entries, is a power of two dividing $2r$. The transformed list $Z_0,\dots,Z_{t-1}$ has entries $Z_g=\frac1t\sum_{s=0}^{t-1} y^{2rgs/t}\,z_s$, where $g$ is the output index and $s$ the input index, both running from $0$ to $t-1$.

The roots of unity are powers of $y$ <cite data-source="paper">Powers of $y$ then serve as roots of unity in the remaining axes</cite>. The root is $y^{2r/t}$. Since $y^r=-1$, $y^{2r}=1$, so its $t$-th power is $1$. It is primitive: for an exponent $m$ with $0<m<t$, the power $y^{2rm/t}$ has exponent strictly between $0$ and $2r$, and no such $y^e$ equals $1$ (for $e\ge r$ it is $-y^{e-r}$).

Each power $y^{2rgs/t}$ is a signed shift, so no term costs a real multiplication. Synthetic transforms follow the butterfly scheme of the [Discrete Fourier transform and butterflies](dft-fft.md): each level combines pairs of entries into their sum and difference, after multiplying one by a power of $y$.

This gives the step directly. Every multiplication is by a power of $y$, hence a signed shift; the rest of each level is addition and subtraction, and moving entries between levels is an address rearrangement. The motivation is that a general complex root would cost real multiplications. Synthetic transforms are costed on a [fixed-tape machine](fixed-tape-model.md), where the cost is data movement.
