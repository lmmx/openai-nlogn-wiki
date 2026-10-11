A linear functional is built on the vector spaces and linear maps of [Linear algebra basics](linear-algebra-basics.md): it is a linear map from a vector space to its field of scalars. Its output is a single scalar, so it is the simplest kind of linear map. Each output value of a linear network is a linear functional of its input values, so a linear network is a collection of such maps, one for each output value.

## Definition

Let $V$ be a vector space over the field $F$, whose vectors a functional takes as input. A map $f: V \to F$ is a linear functional when the following holds for all vectors $x, y$ in $V$ and all scalars $c, d$ in $F$:

$$f(cx + dy) = c f(x) + d f(y).$$

The map $f$ sends each vector to one scalar, so its codomain is $F$ itself. The condition says that $f$ respects both operations: applying $f$ to a combination of vectors gives the same result as combining the values of $f$ on the vectors.

Taking $c = d = 0$ gives $f(0) = 0$ for every linear functional. So the map $x \mapsto x_1 + 1$ on $\mathbb{R}^3$ is not a linear functional, because it sends $0$ to $1$.

## Example

Let $F = \mathbb{R}$, $V = \mathbb{R}^3$, and $f(x) = x_1 + 2x_2 - x_3$. Take $x = (1, 0, 2)$, $y = (0, 3, 1)$, $c = 2$, $d = 1$. Then $f(x) = 1 - 2 = -1$ and $f(y) = 0 + 6 - 1 = 5$. The combination is $cx + dy = (2, 3, 5)$, so $f(cx + dy) = 2 + 6 - 5 = 3$. Also $c f(x) + d f(y) = -2 + 5 = 3$, as the definition requires.

## Every functional on $F^m$ has this form

On $V = F^m$, every linear functional has the form

$$f(x) = a_1 x_1 + a_2 x_2 + \cdots + a_m x_m,$$

where $a_j$ is the value $f$ takes on the vector with $1$ in coordinate $j$ and $0$ in every other coordinate. This holds because $x$ is the sum over $j$ of $x_j$ times that vector, and linearity lets $f$ pass through the sum and the scalars. In the example, $a_1 = 1$, $a_2 = 2$ and $a_3 = -1$.
