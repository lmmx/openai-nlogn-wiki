The binary field is the scalar set of the bit construction, a network on the three-element subsets of a ground set in which every scalar is a bit. Its matrices also give the shear frames $\Phi_M$ that rearrange array entries in the paper's address arithmetic, and those frames are invertible because of its arithmetic.

The binary field, written $\mathbb{F}_2$, is the field with the two elements $0$ and $1$. Its addition is exclusive or ($\oplus$), which gives $1$ exactly when its two bits differ, and its multiplication is AND, which gives $1$ only when both bits are $1$. A field is a set with an addition and a multiplication obeying the usual rules of arithmetic, in which every nonzero element has a multiplicative inverse.

The addition of $\mathbb{F}_2$ is defined by [Congruence](congruence-modulo.md) modulo $2$. That is, it is integer addition followed by reduction, so $1+1=2$ is congruent to $0$.

Because $\mathbb{F}_2$ has two elements, its arithmetic is fixed by four facts:

$$0 \oplus 0 = 0, \qquad 0 \oplus 1 = 1, \qquad 1 \oplus 0 = 1, \qquad 1 \oplus 1 = 0.$$

Multiplication is AND, so every product with a $0$ is $0$. Every element is its own additive inverse (the element that sums to $0$ with it), since $x \oplus x = 0$.

For example, the $2 \times 2$ matrix with rows $(1, 1)$ and $(0, 1)$ over $\mathbb{F}_2$ squares to rows $(1 \oplus 0,\ 1 \oplus 1) = (1, 0)$ and $(0, 1)$. So its square is the identity $I$, the matrix with ones on the diagonal and zeros elsewhere, and the matrix is its own inverse.

In the bit construction, two three-element subsets $\mathcal{A}$ and $\mathcal{C}$ of the ground set are neighbours when they share exactly one element. <cite data-source="paper">In the bit construction, scalars lie in F2 , and S, T are neighbors when |S ∩ T | = 1.</cite> The central coefficient from the input for $\mathcal{C}$ to the output for $\mathcal{A}$ is $|\mathcal{A} \cap \mathcal{C}| \bmod 2$, the parity of the number of shared elements. <cite data-source="paper">In the bit case, the central coefficient from xT to yS is |S ∩ T | mod 2.</cite> For $\{1,2,3\}$ and $\{3,4,5\}$ the coefficient is $1$, since they share one element. For $\{1,2,3\}$ and $\{1,2,4\}$ it is $2 \bmod 2 = 0$.

The shear frame $\Phi_M$ is an invertible operator on arrays, where $M$ is a matrix over $\mathbb{F}_2$ and $H$ and $K$ are blocks of address bits. It moves the array entry at address $(H, K)$ to $(H+MK, K)$, leaving the other bits unchanged. (The paper writes $D$ for $K$.) <cite data-source="paper">For a matrix M , the frame ΦM moves the array entry at (H, D) to (H + M D, D), leaving the other address fields unchanged.</cite> <cite data-source="paper">Hence ΦM is an invertible F2 -linear permutation of array entries</cite> Addition of bit vectors is exclusive or, so adding $MK$ twice returns $H$. Applying $\Phi_M$ twice is therefore the identity, so $\Phi_M$ is its own inverse.
