Nested subspace labels assign subspaces of one fixed space to the gates and terminals of a linear network, so that the subspaces at the two ends of each edge are nested. They measure the cost of edges: the drop in dimension across an edge counts the smaller operations that edge needs. This is what lets a recursive scheme pay less per edge when its parameter shrinks, and it supports the claim that interchanging two equal address fields of width $u$ costs less than linear in $u$ per unit volume.

Fix a space $V$ of dimension $m$; $m$ counts the independent directions in $V$, and every label lies in $V$. A label is a subspace $L(x) \subseteq V$ attached to each vertex $x$ of the network, where a vertex is a gate or terminal. Along an edge from $x$ to $y$, the labels are nested: one is contained in the other. The dimension drop across the edge is the difference of the two dimensions. <cite data-source="paper">Their dimension changes count the smaller operations needed on an edge</cite>.

For example, take $m=3$. Let $L(x)$ be a plane, of dimension 2, and let $L(y)$ be a line inside it, of dimension 1. The drop across this edge is $2-1=1$, so the edge needs one smaller operation. Two adjacent vertices with labels of equal dimension have no dimension drop, so the dimension changes alone count no smaller operation there.

Labels are unaffected by a change of [Frame of a vertex](frame.md) along an edge, because such changes cancel between the two ends of a route.

The construction is built from a [Subset-intersection finite network](subset-network.md) on three-element subsets, whose gather and scatter wires create coefficients that depend on intersection size.
