A phase factor is a complex number $\phi$ with $|\phi| = 1$, where $|\phi|$ is the distance from $\phi$ to $0$ in the complex plane. The [simultaneous butterfly layer](simultaneous-butterfly-layer.md) and [Gaussian resampling](gaussian-resampling.md) rely on phase factors.

Write $\operatorname{Re}\phi$ and $\operatorname{Im}\phi$ for the real and imaginary parts of $\phi$, so $\phi = \operatorname{Re}\phi + i\,\operatorname{Im}\phi$. A Gaussian integer is a complex number whose real and imaginary parts are both integers. A unit of a [ring](ring.md) is an element whose inverse also lies in that ring.

Each phase factor that is a power of $i$ is a unit of the [ring](ring.md) of Gaussian integers. Indeed $i\cdot(-i)=1$ and $-i$ is a Gaussian integer, so $i$ has an inverse among the Gaussian integers, and so does each power of $i$. Hence multiplying a Gaussian integer by such a phase factor gives a Gaussian integer.

A phase factor used here is built from the fourth [roots of unity](root-of-unity.md), namely $1$, $i$, $-1$ and $-i$. Multiplying by $i$ swaps the real and imaginary parts and changes one sign, so $i(1+2i) = -2+i$. The paper states the same rule: <cite data-source="paper">i swaps the real and imaginary components and changes one sign.</cite>

A scalar correction is a fixed constant phase factor applied at each sink of a [network of gates and terminals](network-gate-terminal.md). A sink is an output terminal, the end of a wire where values leave the network.

Because $|\phi| = 1$, multiplying an entry by $\phi$ leaves its modulus unchanged, so the largest modulus among an array's entries, its array norm, is unchanged too.
