Subspace labels are the intermediate subspaces that a linear network attaches to its wires, chosen so that each change of representation along a wire is cheap. They are the step that makes the signed exchange of the scalar network affordable.

Let $F$ be the fixed bilinear space, with bilinear form $\langle x,y\rangle$, which is linear in each argument, and assume $F$ is nondegenerate. A label $U$ is a nondegenerate subspace of $F$, meaning $U\cap U^{\perp}=\{0\}$, where $U^{\perp}$ is the set of vectors orthogonal to every vector of $U$. The labels are attached to the wires of a [linear network](linear-network-frames.md), and each wire carries one label at each stage.

On every edge one label contains the other. For an edge with $U \subseteq V$, the labels $U$ and $V$ are its smaller and larger label. Its orthogonal residual is $R = V\cap U^{\perp}$, the orthogonal complement of the smaller label inside the larger one. Since $U$ is nondegenerate, $\dim R = \dim V-\dim U$, so the residual's dimension is the change in label dimension across the edge: $\dim R = |\dim V-\dim U|$ <cite data-source="paper">its dimension is the absolute change in label dimension</cite>.

Small residuals mean that few dimensions change on each edge, and so a change of frame touches little data.

Example. Take $F=\mathbb{C}^3$ with $x\cdot y=x_1y_1+x_2y_2+x_3y_3$. This form is nondegenerate, since $e_i\cdot e_j=\delta_{ij}$. Let $U=\operatorname{span}(e_1)\subseteq V=\operatorname{span}(e_1,e_2)$. Then $U^{\perp}=\operatorname{span}(e_2,e_3)$, so $R=V\cap U^{\perp}=\operatorname{span}(e_2)$, and $\dim R=1=\dim V-\dim U$.
