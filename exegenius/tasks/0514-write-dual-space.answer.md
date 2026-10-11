The dual space of a vector space is the vector space that collects all of its [Linear functional](linear-functional.md)s. The argument relies on it in the [Subset-intersection network](subset-intersection-network.md) and in [Rank-saving recursion](rank-saving-recursion.md).

Let $U$ be a vector space over the field $F$. The dual space $U^*$ collects every [Linear functional](linear-functional.md) on $U$ into one vector space. Under pointwise addition and scalar multiplication, $U^*$ satisfies the axioms of a vector space, as set out in [Linear algebra basics](linear-algebra-basics.md). The elements of $U^*$ are written $f$; each is a map $f: U \to F$ that is linear, so $f(x+y)=f(x)+f(y)$ and $f(cx)=cf(x)$ for vectors $x,y$ and scalars $c$ in $F$.

For example, let $U=\mathbb{R}^2$, the vectors $x=(x_1,x_2)$ with real entries, over the field $F=\mathbb{R}$ of real numbers. Let $\sigma$ be the functional $\sigma(x)=3x_1-x_2$ and $\rho$ the functional $\rho(x)=x_1$. Both are linear. Their sum is taken value by value:

$$(\sigma+\rho)(x)=(3x_1-x_2)+x_1=4x_1-x_2,$$

and scalar multiplication gives $(2\sigma)(x)=6x_1-2x_2$. Both results are again linear functionals on $\mathbb{R}^2$, so they are elements of $U^*$.

The two functionals $x\mapsto x_1$ and $x\mapsto x_2$ form a basis of $U^*$. A basis is a set of vectors from which every vector is a unique combination of the set's members with scalar coefficients, and the number of vectors in a basis is the dimension. So $U^*$ has dimension 2, the same as $U$.
