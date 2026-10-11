A phase factor is a complex number $\zeta$ with $|\zeta| = 1$, where $|\zeta|$ is the distance from $\zeta$ to $0$ in the complex plane. The [simultaneous butterfly layer](simultaneous-butterfly-layer.md) and [Gaussian resampling](gaussian-resampling.md) rely on them.

Write $\operatorname{Re}\zeta$ and $\operatorname{Im}\zeta$ for the real and imaginary parts of $\zeta$. A Gaussian integer has integer real and imaginary parts. A unit of a ring is an element whose inverse also lies in the ring. Each phase factor $\zeta$ that is a power of $i$ is a unit of the [ring](ring.md) of Gaussian integers, so multiplying a Gaussian integer by $\zeta$ gives a Gaussian integer.

The phase factors used here are built from the fourth [roots of unity](root-of-unity.md) $1, i, -1, -i$. Multiplying by $i$ swaps the parts and changes one sign: $i(1+2i) = -2+i$. The paper states it: <cite data-source="paper">i swaps the real and imaginary components and changes one sign.</cite>

A butterfly layer applies a two-point butterfly to each pair of entries whose addresses differ in one selected bit. Here $D$ counts the selected bits, not axes. For an address $x$ (here $x$ is an address), write $x_1,\dots,x_D\in\{0,1\}$ for its selected bits. The diagonal operator $S_D$ multiplies the value stored at $x$ by $i^{x_1+\cdots+x_D}$, a phase factor depending only on the bits. <cite data-source="paper">Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address.</cite>

Let $C=\tfrac12\begin{pmatrix}1+i&1-i\\1-i&1+i\end{pmatrix}$ be the forward kernel, and $Z=\mathrm{diag}(1,-1)$ the sign matrix. The paper states <cite data-source="paper">In particular, C = iZC −1 Z.</cite> Conjugating by $Z$ gives $ZCZ = iC^{-1}$, so $C^{-1} = -i\,ZCZ$ since $1/i=-i$.

Let $A^{\otimes D}$ denote the $D$-fold tensor (Kronecker) product of a matrix $A$. An inverse child on $D$ selected bits is a recursive call that must apply $(C^{-1})^{\otimes D}$ to those bits. Tensor products respect matrix products, $(A\otimes B)(A'\otimes B')=AA'\otimes BB'$, and scalars, so

$$(C^{-1})^{\otimes D} = (-i)^D\, Z^{\otimes D}\, C^{\otimes D}\, Z^{\otimes D}.$$

The middle factor $C^{\otimes D}$ is one forward call. <cite data-source="paper">All inverse wrappers are address signs and constant fourth-root phases, so they add no recursive calls.</cite> <cite data-source="paper">Formula (17) supplies each inverse child from one forward call, and none of the corrections adds a child.</cite>

A scalar correction is a fixed constant phase factor applied at each sink of a [network of gates and terminals](network-gate-terminal.md). An endpoint kernel is the kernel that a network applies to a role at its end. The paper's sign matrices, <cite data-source="paper">together with the scalar i27f at each affected sink, turn every endpoint kernel into a forward one.</cite>
