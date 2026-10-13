Rank-saving recursion is a recursive scheme that runs on a [linear network](linear-network.md), paying for each edge with a few smaller calls and keeping the total number of calls small. It is the step that gives [fast interchange of address chunks](tape-interchange.md) its saving.

An edge matrix is the matrix that says what one edge does to the values it carries. Here $a$ is the rank of an edge matrix, not the bank value of the earlier page: an edge matrix of rank $a$ costs $a$ smaller calls. Let $s$ be the total number of smaller calls over all $W$ roles.

The recursion splits its array into [role streams from a cyclic row split](role-streams.md) across the $W$ roles, so each role carries an equal share of the volume, the number of bits stored. It is stated in the [frame of a vertex](frame.md) at each end of an edge, since frame changes cancel along a route.

The cost is measured by [nested subspace labels](subspace-labels.md) on the edges. Each vertex gets a subspace of a fixed $m$-dimensional space, and adjacent subspaces are nested. The drop in dimension across an edge counts the smaller calls that edge needs.

Summing over the edges, the total number $s$ of smaller calls is less than $Wm$ <cite data-source="paper">The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.</cite>. The paper proves this in its finite-network section, using three-element subsets whose gather and scatter wires make coefficients depend on intersection size. Dividing by $W$, each role pays on average fewer than $m$ calls, so the cost per unit volume is below $m$ times the fixed cost of one call.

The main motivation is that interchanging two equal address fields, blocks of bit positions in the array's index, must cost less than linear in the field width per unit volume. The bound on $s$ supplies that saving, as the [fast interchange](tape-interchange.md) page uses it.
