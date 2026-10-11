A phase factor is a complex number $\zeta$ of modulus one, $|\zeta| = 1$, where $|\zeta|$ is the distance from $\zeta$ to $0$ in the complex plane. Phase factors are the twists by which the transforms in this paper change coefficients without changing their sizes; the [Synthetic polynomial transforms](synthetic-transforms.md) use powers of the polynomial variable as their roots of unity, and the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) applies such twists on selected bits.

Write $z = \alpha + \beta i$ for a complex number, where $\alpha$ and $\beta$ are real numbers, the real and imaginary parts of $z$. A unit of a ring is an element whose inverse also lies in the ring. The phase factors used here are the fourth roots of unity $1, i, -1, -i$ and fixed constant multiples of them. The modulus of $z$ is $\sqrt{\alpha^2 + \beta^2}$, so multiplying by a phase factor changes the angle of $z$ but not its modulus.

Multiplication by $i$ is the simplest case. Since $i^2 = -1$,
$$
i\,(3 + 2i) = 3i + 2i^2 = -2 + 3i .
$$
The pair $(\alpha, \beta) = (3, 2)$ becomes $(-2, 3)$: <cite data-source="paper">i swaps the real and imaginary components and changes one sign.</cite>

In the butterfly layers, the phase depends on the address. The diagonal operator multiplies the value at an address by a power of $i$ determined by the selected bits of that address, and the exponent is the number of selected bits equal to 1. <cite data-source="paper">Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address.</cite>

A scalar correction is a fixed constant phase factor multiplied into values to undo a sign or an exchange of roles. The paper applies a fixed power of $i$ at each affected sink, <cite data-source="paper">together with the scalar i27f at each</cite> sink, so that each endpoint operator becomes a forward one. The wrappers around the recursive calls are of the same kind: <cite data-source="paper">All inverse wrappers are address signs and constant fourth-root</cite> phases, so they add no recursive calls.

Each phase factor $\zeta$ that is a power of $i$ is a unit of the [Gaussian integer](gaussian-integer.md) ring, so multiplying a Gaussian integer by it gives a Gaussian integer. This is why the phases are exact: <cite data-source="paper">scalar corrections above are exact Gaussian dyadic operations.</cite>
