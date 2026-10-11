A bilinear map takes one vector from each of two vector spaces and returns a vector in a third, and it is linear in each argument while the other is held fixed. Multiplying two polynomials is the standard example. The paper's error analysis relies on such a map, because bilinearity lets an error in one operand be bounded while the other operand is kept fixed.

## Definition

A bilinear map is defined through the linear maps of [Linear algebra basics](linear-algebra-basics.md): fixing one argument must give a linear map in the other.

Let $\beta: V \times W \to U$ be a map, which sends each pair $(v,w)$ with $v \in V$ and $w \in W$ to a vector $\beta(v,w)$ in $U$, where $V$, $W$ and $U$ are vector spaces over the same field of scalars. The map $\beta$ is *bilinear* when, for each fixed $w \in W$, the map $v \mapsto \beta(v,w)$ is linear, and for each fixed $v \in V$, the map $w \mapsto \beta(v,w)$ is linear. Linearity in one argument alone is not enough.

## Example

Let $V = W = \mathbb{C}^2$ and $U = \mathbb{C}$, and let $\beta$ send a pair of vectors to the sum of their coordinatewise products. Then $\beta\big((1,2),(3,4)\big) = 1\cdot 3 + 2\cdot 4 = 11$. Doubling the first argument doubles the output, $\beta\big((2,4),(3,4)\big) = 22$, as linearity requires.

Adding a constant breaks bilinearity. If $\beta(v,w)+1$ replaces $\beta(v,w)$, the map sends $(0,w)$ to $1$, but a linear map in $v$ must send $0$ to $0$.

Multiplying polynomials is bilinear: a sum of polynomials times a fixed polynomial is the sum of the products, and a scalar multiple of one factor scales the product by that scalar.

## Use in the argument

The paper's error analysis works with an exact bilinear map: <cite data-source="paper">The exact map P is bilinear and satisfies</cite> a coefficient bound. For a bilinear contraction, <cite data-source="paper">replacing one operand changes the output by at most the norm</cite> distance between the two values when the other operand is a disk array. When the operands lie in the disk, <cite data-source="paper">their two errors therefore add</cite>.
