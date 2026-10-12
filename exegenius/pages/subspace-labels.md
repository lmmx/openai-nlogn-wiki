Subspace labels are the intermediate subspaces that a [linear network](linear-network-frames.md) attaches to its wires, chosen so that each change of representation along a wire is cheap. They make the scalar network's signed exchange affordable.

Subspace labels are based on the fixed bilinear space $F$, whose [Bilinear form](bilinear-form.md) $\langle p,q\rangle$ is linear in each argument, where $p$ and $q$ are vectors of $F$. We assume $F$ is nondegenerate: no nonzero vector is orthogonal to every vector of $F$.

A label $L$ is a nondegenerate subspace of $F$, meaning $L\cap L^{\perp}=\{0\}$, where $L^{\perp}$ is the set of vectors orthogonal to every vector of $L$. Each wire carries one label at each stage of the network.

On every edge one label contains the other. For an edge with $L\subseteq M$, $L$ and $M$ are its smaller and larger label. Its orthogonal residual is $R=M\cap L^{\perp}$, the orthogonal complement of the smaller label inside the larger one.

The residual's dimension is the change in label dimension across the edge. Since $L$ and $F$ are nondegenerate, $F=L\oplus L^{\perp}$ and $\dim L^{\perp}=\dim F-\dim L$ (standard linear algebra). For $p\in M$, write $p=c+r$ with $c\in L$ and $r\in L^{\perp}$; then $r=p-c\in M$, so $r\in R$. Hence $M=L+R$ with $L\cap R=\{0\}$, and $\dim R=\dim M-\dim L$.

Small residuals mean that few dimensions change on each edge, so a change of frame touches little data.

Example. Take $F=\mathbb{C}^3$ with $\langle p,q\rangle=p_1q_1+p_2q_2+p_3q_3$. This form is nondegenerate: if $\langle p,q\rangle=0$ for every $q$, then each $p_i=0$. Let $L=\operatorname{span}((1,0,0))\subseteq M=\operatorname{span}((1,0,0),(0,1,0))$. Then $L^{\perp}=\operatorname{span}((0,1,0),(0,0,1))$, so $R=M\cap L^{\perp}=\operatorname{span}((0,1,0))$, and $\dim R=1=\dim M-\dim L$.
