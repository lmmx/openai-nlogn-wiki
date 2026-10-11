The binary field is the scalar set of the bit construction, a network on the three-element subsets of a ground set in which every scalar is a bit.

The binary field, written $\mathbb{F}_2$, is the field with the two elements $0$ and $1$, where addition is exclusive or ($\oplus$), which gives $1$ exactly when its two bits differ, and multiplication is AND.

A field is a set with an addition and a multiplication obeying the usual rules of arithmetic, and every nonzero element has a multiplicative inverse. The addition of $\mathbb{F}_2$ is defined by [congruence](congruence-modulo.md) modulo $2$. That is, it is integer addition followed by reduction, so $1+1=2$ is congruent to $0$.

Because $\mathbb{F}_2$ has two elements, its arithmetic is fixed by four facts:

$$0 \oplus 0 = 0, \qquad 0 \oplus 1 = 1, \qquad 1 \oplus 0 = 1, \qquad 1 \oplus 1 = 0.$$

Multiplication is AND, so every product with a $0$ is $0$. Every element is its own additive inverse, since $x \oplus x = 0$.

For example, the $2 \times 2$ matrix with rows $(1, 1)$ and $(0, 1)$ over $\mathbb{F}_2$ squares to rows $(1 \oplus 0,\ 1 \oplus 1) = (1, 0)$ and $(0, 1)$. So its square is the identity $I$, and the matrix is its own inverse.

In the bit construction, two three-element subsets are neighbours when they share exactly one element. Let $\sigma$ and $\sigma'$ be three-element subsets of the ground set. The central coefficient from the input for $\sigma$ to the output for $\sigma'$ is $|\sigma \cap \sigma'| \bmod 2$, the parity of the number of shared elements. <cite data-source="paper">the central coefficient from xT to yS is |S ∩ T | mod 2</cite> For $\{1,2,3\}$ and $\{3,4,5\}$ the coefficient is $1$, since they share one element. For $\{1,2,3\}$ and $\{1,2,4\}$ it is $2 \bmod 2 = 0$.

The matrix frame $\Phi_M$ is the second use. For a matrix $M$, $\Phi_M$ moves the array entry at address $(H, K)$ to $(H+MK, K)$, where $H$ and $K$ are binary address chunks. <cite data-source="paper">Hence ΦM is an invertible F2 -linear permutation of array entries</cite> Addition of bit vectors is exclusive or, so adding $MK$ twice returns $H$. Applying $\Phi_M$ twice is the identity, so $\Phi_M$ is its own inverse.
