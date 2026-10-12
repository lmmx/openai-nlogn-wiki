The subset-intersection network is a linear network whose labels are subspaces chosen from intersection sizes of three-element subsets. It shows that its number of smaller calls is less than its number of wires times the label dimension, the saving the main theorem uses.

It is based on a [Linear network that restores auxiliary values](linear-network.md) of gates that exchange the banks $X_a$ and $Y_a$ with signs. Each gate and terminal carries a subspace label of one fixed space, so the network is built on [Linear algebra over a field](linear-algebra.md). Here $W$ is the number of wires, $m=h^3$ is the dimension of the label space, and $s$ is the total number of smaller calls.

For a three-element subset $T$, let $t_T\in\mathbb Q^h$ be its indicator vector, with entry 1 at each element of $T$ and 0 elsewhere. Take the form
$$\langle x,y\rangle=\sum_i x_iy_i-\tfrac19\Bigl(\sum_i x_i\Bigr)\Bigl(\sum_i y_i\Bigr)$$
on $\mathbb Q^h$. The first sum counts common elements, and each indicator sums to 3, so $\langle t_S,t_T\rangle=|S\cap T|-\tfrac19\cdot3\cdot3=|S\cap T|-1$ and $\langle t_T,t_T\rangle=2$. The bank label $U_a$ is the span of $t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$, a line.

Labels at the two ends of an edge are nested, so one contains the other. <cite data-source="paper">Every edge joins comparable nondegenerate labels</cite>. Changing a label's dimension by some amount costs that many smaller calls, since the projections onto the two labels differ by a matrix of that rank, and each unit of rational rank is one smaller interchange. So $s$ is the sum of the ranks of all edge differences.

Each gate's label enters and leaves it, so gate contributions cancel in the signed sum of changes, leaving sinks minus sources. The sources total $N$, the number of banks $X_a$, since each $U_a$ is a line. Every sink label is the whole space, except the $N$ sinks $U_a^\perp$ of the $Y_a$, which have one dimension less, so the sinks total $Wm-N$. The signed sum is $Wm-2N$. Let $L$ be the total dimension lost on decreasing edges. The sum of absolute changes is the signed sum plus $2L$, namely $Wm-2N+2L$.

The rational interface adds one rank per bank: the source matrix of $X_a$ is minus the projection onto $U_a$, of rank one, on an edge with no label change. The operator on each role is computed from the endpoint frames of the [Frame of a network vertex](frame.md), so only the two ends of a route matter. Hence $s=Wm-N+2L$, and $s<Wm$ exactly when $L<N/2$.

The only decreasing edges are central-wire returns, each losing $h$ dimensions. For the two constructions the paper gives $L/N=100/539$ and $101/539$; <cite data-source="paper">both are smaller than $1/2$</cite>. So the deficit is $Wm-s=N-2L=\tfrac{339}{539}N$ for the bit network, a fixed fraction of $N$ independent of the input length.
