The binary field is the number system in which every quantity is $0$ or $1$. It is the scalar set of the bit-level constructions in the argument, where <cite data-source="paper">In the bit construction, scalars lie in F2</cite>.

A field is a set with an addition and a multiplication that obey the usual rules of arithmetic: both operations are associative and commutative, multiplication distributes over addition, there is a zero and a one, and every nonzero element has a multiplicative inverse. The binary field, written $\mathbb{F}_2$, is the field with the two elements $0$ and $1$, where addition is exclusive or ($\oplus$) and multiplication is AND.

Because $\mathbb{F}_2$ has only two elements, its arithmetic is determined by four facts:

$$0 \oplus 0 = 0, \qquad 0 \oplus 1 = 1, \qquad 1 \oplus 0 = 1, \qquad 1 \oplus 1 = 0.$$

Multiplication is AND, so $1 \cdot 1 = 1$ and every product with a $0$ is $0$. Every element is its own additive inverse, since $x \oplus x = 0$, and $1$ is its own multiplicative inverse. Addition modulo $2$ on integers gives the same table, which is why sums of bits in $\mathbb{F}_2$ are the same as counts taken mod 2.

For example, let $M$ be the $2 \times 2$ matrix with rows $(1, 1)$ and $(0, 1)$ over $\mathbb{F}_2$. Its square is $M^2$ with rows $(1 \oplus 0,\ 1 \oplus 1) = (1, 0)$ and $(0,\ 1)$, so $M^2 = I$ and $M$ is an invertible linear map over $\mathbb{F}_2$ that is its own inverse.

The sources use this field for the bit construction. The coefficient that a copy step places between two sets is computed in $\mathbb{F}_2$ as <cite data-source="paper">the central coefficient from xT to yS is |S ∩ T | mod 2</cite>, and the frame maps that rearrange address entries are <cite data-source="paper">an invertible F2 -linear permutation of array entries</cite>.
