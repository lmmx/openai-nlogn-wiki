Nested subspace labels are subspaces of one fixed space, attached to the gates and terminals of a network so that the dimension drop along each edge counts the smaller operations that edge needs. They give the cost bound for interchanging two equal address fields below linear in the field width.

Fix a space $E$ of dimension $m$, the common space of all labels; here $m$ is that dimension, not the numerator of a dyadic rational. The labels are built on a [Subset-intersection finite network](subset-network.md). Each vertex $w$ of the network, a gate or a terminal, carries a label $L(w)$, a subspace of $E$. Each label sits at a gate or at a [Source, sink and terminal of a network](network-terminal.md).

An edge runs from its tail $\sigma$ to its head $\nu$; these letters name vertices, not bank values. Along it the labels are nested, $L(\nu)\subseteq L(\sigma)$, and the drop of the edge is $\dim L(\sigma)-\dim L(\nu)$. <cite data-source="paper">The subspaces at adjacent vertices are nested.</cite> For example, a plane $L(\sigma)$ containing a line $L(\nu)$ has drop $2-1=1$.

Each gate or sink with label $U$ has a projection $P_U$ onto $U$ along its orthogonal complement $U^\perp$. For an edge from $\sigma$ to $\nu$, the difference $P_{L(\sigma)}-P_{L(\nu)}$ is the projection onto the part of $L(\sigma)$ orthogonal to $L(\nu)$, a space of dimension $\dim L(\sigma)-\dim L(\nu)$. The edge matrix is this difference up to sign, so its rank is the drop.

The labels are chosen to make cheap the changes of [Frame of a vertex](frame.md) on each edge: the stored array at $w$ is $D_w g$ when the logical array is $g$, and along an edge from $\sigma$ to $\nu$ it changes by $D_\nu D_\sigma^{-1}$. Along a route the intermediate frames cancel, so only the two end frames fix the operator on the route.

Let $s$ be the total number of smaller calls, the sum of the drops over all edges. <cite data-source="paper">The number of recursive calls is the sum of the edge ranks, exactly $s$.</cite> A smaller call is the same procedure run on one role stream. <cite data-source="paper">Each acts on one role stream of volume $V/W$</cite>, where $W$ is the number of roles.

The claim is that $s$ is below $Wm$. <cite data-source="paper">The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.</cite>
