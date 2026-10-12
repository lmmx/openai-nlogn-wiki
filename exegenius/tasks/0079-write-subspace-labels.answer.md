Subspace labels are the intermediate subspaces that a [linear network](linear-network-frames.md) attaches to its wires, chosen so that each change of representation along a wire is cheap. They make the signed exchange of the scalar network affordable.

Subspace labels are based on the fixed bilinear space $F$, whose [bilinear form](bilinear-form.md) $\langle x,y\rangle$ is linear in each argument, where $x$ and $y$ are vectors of $F$. We assume $F$ is nondegenerate: no nonzero vector is orthogonal to every vector of $F$.

A label $U$ is a nondegenerate subspace of $F$, meaning $U\cap U^{\perp}=\{0\}$, where $U^{\perp}$ is the set of vectors orthogonal to every vector of $U$. Each wire carries one label at each stage of the network.

On every edge one label contains the other. For an edge with $U \subseteq V$, the labels $U$ and $V$ are its smaller and larger label. Its orthogonal residual is $R = V\cap U^{\perp}$, the orthogonal complement of the smaller label inside the larger one.

The residual's dimension is the change in label dimension across the edge. Since $U$ is nondegenerate and $F$ is nondegenerate, $F$ splits as $U$ plus $U^{\perp}$, with $U\cap U^{\perp}=\{0\}$ and $\dim U^{\perp}=\dim F-\dim U$ (standard linear algebra). For $v\in V$, write $v=u+w$ with $u\in U$ and $w\in U^{\perp}$. Since $U\subseteq V$, $w=v-u$ lies in $V$, so $w\in R$. Hence $V=U+R$ with $U\cap R=\{0\}$, and $\dim R=\dim V-\dim U$.

Small residuals mean that few dimensions change on each edge, so a change of frame touches little data.

Example. Take $F=\mathbb{C}^3$ with $\langle x,y\rangle=x_1y_1+x_2y_2+x_3y_3$. This form is nondegenerate, since $e_i\cdot e_j=\delta_{ij}$. Let $U=\operatorname{span}(e_1)\subseteq V=\operatorname{span}(e_1,e_2)$. Then $U^{\perp}=\operatorname{span}(e_2,e_3)$, so $R=V\cap U^{\perp}=\operatorname{span}(e_2)$, and $\dim R=1=\dim V-\dim U$.
