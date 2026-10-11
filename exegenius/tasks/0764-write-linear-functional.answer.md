A linear functional is built on the vector spaces and linear maps of [Linear algebra basics](linear-algebra-basics.md). It is a linear map from a vector space to its field of scalars, so each output is a single scalar, the simplest kind of linear map.

The paper's linear networks rely on it. A linear network is a fixed network of wires and gates, and <cite data-source="paper">A gate is a fixed linear map on a specified set of wires</cite>. Composing these gates, each output value of a [linear network](linear-network-frames.md) is a linear functional of its input values.

## Definition

Let $\mathcal{X}$ be a vector space over the field $F$, whose vectors a functional takes as input. A map $\mathcal{L}\colon \mathcal{X}\to F$ is a linear functional when the following holds for all vectors $x,y\in\mathcal{X}$ and all scalars $\gamma,\eta\in F$:

$$\mathcal{L}(\gamma x+\eta y)=\gamma\,\mathcal{L}(x)+\eta\,\mathcal{L}(y).$$

The map $\mathcal{L}$ sends each vector to one scalar. The condition says that it respects both operations: the value on a combination of vectors equals the same combination of the values. Taking $\gamma=\eta=0$ gives $\mathcal{L}(0)=0$ for every linear functional. So the map on $\mathbb{R}^3$ that adds $1$ to the first coordinate is not a linear functional, because it sends $0$ to $1$.

## Example

Let $F=\mathbb{R}$, $\mathcal{X}=\mathbb{R}^3$, and $\mathcal{L}(x)=x_1+2x_2-x_3$, where $x_j$ is the $j$-th coordinate of $x$. Take $x=(1,0,2)$, $y=(0,3,1)$, $\gamma=2$, $\eta=1$. Then $\mathcal{L}(x)=1-2=-1$ and $\mathcal{L}(y)=0+6-1=5$. The combination is $\gamma x+\eta y=(2,3,5)$, so $\mathcal{L}(\gamma x+\eta y)=2+6-5=3$. Also $\gamma\mathcal{L}(x)+\eta\mathcal{L}(y)=-2+5=3$, as the definition requires.

## Every functional on $F^m$ has this form

For $\mathcal{X}=F^m$, let $a_j$ be the value $\mathcal{L}$ takes on the vector with $1$ in coordinate $j$ and $0$ in every other coordinate. The letter $a_j$ has this meaning only in this section; it is not the coefficient $a_k$ of the [transform axis](transform-axis.md) page. Then

$$\mathcal{L}(x)=a_1x_1+a_2x_2+\cdots+a_mx_m.$$

This holds because $x$ is the sum over $j$ of $x_j$ times the vector with $1$ in coordinate $j$ and $0$ elsewhere, and linearity lets $\mathcal{L}$ pass through the sum and the scalars. In the example, $a_1=1$, $a_2=2$ and $a_3=-1$. So each output value of a linear network is a fixed weighted sum of its input values, with the weights $a_j$ fixed by the network.
