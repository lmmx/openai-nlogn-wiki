The subset-intersection network is a linear network whose subspace labels come from intersection sizes of three-element subsets. It exchanges the banks $X_a$ and $Y_a$ with signs, and its label changes give the saving used in the main theorem.

The network is based on a [Linear network that restores auxiliary values](linear-network.md) of gates that exchange the banks $X_a$ and $Y_a$ with signs and restore every scratch wire. Each gate and terminal carries a subspace label, and all labels lie in one fixed space whose subspaces are described by [Linear algebra over a field](linear-algebra.md). Here $m$ is the dimension of that space. Here $W$ is the number of wires in the construction. Here $s$ is the total number of smaller calls, the smaller operations needed on all edges.

Labels at the two ends of an edge are nested, so one contains the other. The orthogonal residual of an edge is the orthogonal complement of the smaller label inside the larger, and its dimension is the absolute change in label dimension. Each smaller call on an edge is counted by that change, so the total is the sum of absolute label changes over all edges.

The operator on each role is determined by the endpoint frames of the [Frame of a network vertex](frame.md), so only the frames at the two ends of a route matter.

Intersection sizes enter through inner products. For three-element subsets $S$ and $T$, the bit construction has indicator vectors with $\langle t_S,t_T\rangle=|S\cap T|-1$, and their orthogonality permits the subspace assignments.

The source labels have total dimension $N$, and the sink labels total $Wm-N$. Gate contributions cancel in the signed sum of changes, which leaves $Wm-2N$. Edges that decrease the dimension lose a total $L$. So the sum of absolute changes is $Wm-2N+2L$. The rational interface needs $N$ further ranks, so the total becomes $s=Wm-N+2L$, and $s<Wm$ holds once $L<N/2$.

Decreasing edges occur only at the central wires, and each loses a fixed number of dimensions, so $L$ is a fixed proportion of $N$. The loss ratios $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$ are fixed rationals; <cite data-source="paper">both are smaller than $1/2$</cite>. The deficit $Wm-s=N-2L$ is therefore the fixed rational proportion $1-2L/N$ of $N$.
