The binary field, written $\mathbb{F}_2$, is the field with the two elements $0$ and $1$, where addition is exclusive or ($\oplus$), which gives $1$ exactly when its two bits differ, and multiplication is AND. It is the scalar set of the bit construction, a subset-intersection network whose scalars lie in $\mathbb{F}_2$, so every coefficient of that construction is a bit.

A field is a set with an addition and a multiplication that obey the usual rules of arithmetic: both operations are associative and commutative, multiplication distributes over addition, there is a zero and a one, and every nonzero element has a multiplicative inverse. The addition of $\mathbb{F}_2$ is defined by [congruence](congruence-modulo.md) modulo $2$: integer addition followed by reduction, since $1+1=2$ is congruent to $0$.

Because $\mathbb{F}_2$ has only two elements, its arithmetic is determined by four facts:

$$0 \oplus 0 = 0, \qquad 0 \oplus 1 = 1, \qquad 1 \oplus 0 = 1, \qquad 1 \oplus 1 = 0.$$

Multiplication is AND, so $1 \cdot 1 = 1$ and every product with a $0$ is $0$. Let $\tau$ denote an arbitrary element of $\mathbb{F}_2$. Then $\tau \oplus \tau = 0$, so every element is its own additive inverse, and $1$ is its own multiplicative inverse.

For example, let $K$ be the $2 \times 2$ matrix with rows $(1, 1)$ and $(0, 1)$ over $\mathbb{F}_2$. Its square has rows $(1 \oplus 0,\ 1 \oplus 1) = (1, 0)$ and $(0,\ 1)$, so $K^2 = I$, where $I$ is the identity matrix. Thus $K$ is an invertible linear map over $\mathbb{F}_2$ that is its own inverse.

The sources use this field for the bit construction. The coefficient of the bit case is computed in $\mathbb{F}_2$: <cite data-source="paper">the central coefficient from xT to yS is |S ∩ T | mod 2</cite>. The matrix frame $\Phi_M$ is <cite data-source="paper">an invertible F2 -linear permutation of array entries</cite>, so it is an invertible linear map over $\mathbb{F}_2$ of the kind the example above shows.
