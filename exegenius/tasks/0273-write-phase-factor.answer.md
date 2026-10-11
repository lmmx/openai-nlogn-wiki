Phase factors are the twists that this paper's transforms apply to coefficients without changing their sizes. The [simultaneous butterfly layer](simultaneous-butterfly-layer.md) and [Gaussian resampling](gaussian-resampling.md) rely on them.

A phase factor is a complex number $\zeta$ of modulus one, $|\zeta| = 1$, where $|\zeta|$ is the distance from $\zeta$ to $0$ in the complex plane. Write $\tau = \alpha + \beta i$ for a complex number, where $\alpha$ and $\beta$ are real numbers, the real and imaginary parts of $\tau$.

A unit of a [ring](ring.md) is an element whose inverse also lies in the ring. A Gaussian integer is a complex number whose real and imaginary parts are integers. Each phase factor $\zeta$ that is a power of $i$ is a unit of the [ring](ring.md) of Gaussian integers, so multiplying a Gaussian integer by $\zeta$ gives a Gaussian integer.

The phase factors used here are built from the fourth [roots of unity](root-of-unity.md) $1, i, -1, -i$. Multiplying by $i$ gives $i(\alpha+\beta i) = -\beta + \alpha i$. The paper states it: <cite data-source="paper">i swaps the real and imaginary components and changes one sign.</cite>

In a butterfly layer, the phase depends on the address: for an address $s$ in a layer, let $D$ be the number of selected bits, the address bits on which the layer acts, and write $s_1,\dots,s_D$ for them, each 0 or 1. The layer multiplies the value at $s$ by $i^{s_1+\cdots+s_D}$. <cite data-source="paper">Here the unselected address bits are unchanged, and the same phase is applied to every coefficient</cite> stored at that address.

A scalar correction is a fixed constant phase factor applied at each [sink](network-gate-terminal.md) of a network, undoing a sign or an exchange of roles. The endpoint operator is what the frames leave on each role array: <cite data-source="paper">leaves the endpoint operator on every role array</cite>.

Call $C = \tfrac12\begin{pmatrix}1+i&1-i\\1-i&1+i\end{pmatrix}$ the forward kernel, and $Z = \mathrm{diag}(1,-1)$ the sign matrix. The paper's identity <cite data-source="paper">In particular, C = iZC −1 Z.</cite> gives $C^{-1} = -iZCZ$, so multiplying by $i$ and conjugating by $Z$ turns $C^{-1}$ into $C$. The corrections at each affected sink <cite data-source="paper">turn every endpoint kernel into a forward one.</cite>

An inverse child on $D$ selected bits is $(C^{-1})^{\otimes D} = (-i)^D Z^{\otimes D} C^{\otimes D} Z^{\otimes D}$, where $\otimes D$ is the tensor product of $D$ copies. Signs and phases multiply each stored coefficient without calling the procedure. <cite data-source="paper">Formula (17) supplies each inverse child from one forward call, and none of the corrections adds a child.</cite>
