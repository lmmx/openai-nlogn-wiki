A bilinear form is a function of two vectors that is linear in each argument, and it is the structure on which the argument's labels are defined. Throughout, $U$ is a vector space over $\mathbb{F}_2$, so the only scalars are $0$ and $1$.

A bilinear form on $U$ is a function $B$ that takes two vectors $u, v$ of $U$ and returns a scalar $B(u,v)$, linear in each argument. Over $\mathbb{F}_2$ the scalar condition is automatic, so linearity reduces to

$$B(u+u',v)=B(u,v)+B(u',v), \qquad B(u,v+v')=B(u,v)+B(u,v').$$

The form is symmetric when $B(u,v)=B(v,u)$ for all $u$ and $v$. Two vectors are orthogonal when $B(u,v)=0$. The form is nondegenerate when no nonzero vector of $U$ is orthogonal to every vector of $U$. A subspace $W$ of $U$ is nondegenerate when no nonzero vector of $W$ is orthogonal to every vector of $W$.

For example, let $U=\mathbb{F}_2^2$ and write $u=(u_1,u_2)$ and $v=(v_1,v_2)$ for its vectors. Take $B(u,v)=u_1v_1+u_2v_2$, the dot product. A vector $(a,b)$ is orthogonal to $(1,0)$ only if $a=0$, and to $(0,1)$ only if $b=0$, so the only vector orthogonal to both is $(0,0)$ and $B$ is nondegenerate. Now take $B'(u,v)=u_1v_1$. Then $B'((0,1),v)=0$ for every $v$, so $(0,1)$ is a nonzero vector orthogonal to everything and $B'$ is degenerate.

The argument's intermediate labels are nondegenerate subspaces of one fixed bilinear space. <cite data-source="paper">A label is a nondegenerate subspace of a fixed bilinear space</cite>. The labels are then chosen so that changes of frame are inexpensive, as the [Subspace labels](subspace-labels.md) page explains.
