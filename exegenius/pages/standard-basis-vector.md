A standard basis vector is a vector with entry $1$ in one fixed coordinate and $0$ in every other coordinate. It is the vector that the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) uses to name one coordinate position, so that an operation can act on that position alone.

Let $F$ be a field and $m$ the number of coordinates, so that the vectors of $F^m$ are the tuples $(x_1,\dots,x_m)$ with entries in $F$. For each coordinate $j$ with $1\le j\le m$, the standard basis vector $\sigma_j$ is the vector of $F^m$ with entry $1$ at coordinate $j$ and $0$ at every other coordinate. Each standard basis vector $\sigma_j$ is a basis vector of $F^m$ as defined in [Linear algebra basics](linear-algebra-basics.md).

Take $F=\mathbb{C}$ and $m=3$. Then $\sigma_1=(1,0,0)$, $\sigma_2=(0,1,0)$ and $\sigma_3=(0,0,1)$. Every vector is a combination of them with its own entries as coefficients:

$$x=\sum_{j=1}^{m} x_j\,\sigma_j.$$

The $j$th term contributes $x_j$ to coordinate $j$ and nothing to any other coordinate. For $x=(4,-1,2)$ this gives $x=4\sigma_1-\sigma_2+2\sigma_3$.

The combination is unique. If $c_1\sigma_1+\dots+c_m\sigma_m=0$, then coordinate $j$ of this vector is $c_j$, so every $c_j$ is $0$. Hence the standard basis vectors are linearly independent and span $F^m$; together they form the standard basis of $F^m$.

For an $m\times m$ matrix $A$ with entries in $F$, the product $A\sigma_j$ is column $j$ of $A$: the vector $\sigma_j$ has entry $1$ at coordinate $j$ and $0$ elsewhere, so $A\sigma_j$ picks out exactly the entries $A_{1j},\dots,A_{mj}$. This is how the paper places a chosen basis into a matrix. It extends the basis to a full basis and <cite data-source="paper">take these vectors as the first</cite> columns of the matrix. Multiplying by $\sigma_j$ then returns the $j$th chosen basis vector.

In the paper the vector $\sigma_j$ is written $e_j$, <cite data-source="paper">where ej is the jth standard basis vector</cite>. This page writes $\sigma_j$ instead, because the letter $e$ already names other objects in this wiki.
