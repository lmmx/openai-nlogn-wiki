A bilinear map takes one vector from each of two vector spaces and returns a vector in a third, and it is linear in each argument while the other is held fixed. The paper's error analysis uses it to bound the error of a product of two approximate values, one operand at a time.

A bilinear map is defined through the linear maps of [Linear algebra basics](linear-algebra-basics.md): fixing one argument must give a linear map in the other. Let $\pi: E \times H \to K$ send each pair $(e,d)$, with $e \in E$ and $d \in H$, to a vector $\pi(e,d)$ in $K$, where $E$ and $H$ are the argument spaces, $K$ is the output space, and all three are vector spaces over the same field $F$ of scalars. The map $\pi$ is *bilinear* when $e \mapsto \pi(e,d)$ is linear for each fixed $d$, and $d \mapsto \pi(e,d)$ is linear for each fixed $e$.

Let $E = H = \mathbb{C}^2$, $K = \mathbb{C}$, and let $\pi$ send a pair of vectors to the sum of their coordinatewise products. Then $\pi\big((1,2),(3,4)\big) = 1\cdot 3 + 2\cdot 4 = 11$, and doubling the first argument doubles the output: $\pi\big((2,4),(3,4)\big) = 22$. Adding a constant breaks bilinearity: $(e,d)\mapsto \pi(e,d)+1$ sends $(0,d)$ to $1$, but a linear map in $e$ must send $0$ to $0$.

A bilinear map is called a *bilinear contraction* when it is bounded in the [Array norm](array-norm.md): $\|\pi(e,d)\| \le \|e\|\,\|d\|$.

The paper's error analysis works with an exact bilinear map, written $P$ in that analysis: <cite data-source="paper">The exact map P is bilinear and satisfies</cite> a coefficient bound, so it is a bilinear contraction.

The map is applied to disk arrays, which are [Array](array.md) of norm at most one. Bilinearity lets an error in one operand be bounded while the other is fixed. For $d \in H$ and $e, e' \in E$, linearity in the first argument gives $\pi(e',d)-\pi(e,d)=\pi(e'-e,d)$, so $\|\pi(e',d)-\pi(e,d)\| \le \|e'-e\|\,\|d\|$. A disk array <cite data-source="paper">has norm at most one</cite>, so with $d$ a disk array, <cite data-source="paper">replacing one operand changes the output by at most the norm</cite> distance between its two values.

Writing $\pi(e',d')-\pi(e,d)=\pi(e'-e,d')+\pi(e,d'-d)$ and bounding each term the same way gives $\|\pi(e',d')-\pi(e,d)\| \le \|e'-e\|+\|d'-d\|$ when $e, e', d, d'$ are disk arrays. <cite data-source="paper">When all four operands are in the disk, their two errors therefore add.</cite>
