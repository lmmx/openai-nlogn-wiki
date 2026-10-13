Rank-saving recursion is a recursive scheme in which each edge of a network is paid for by a few smaller calls, and the total number of those calls is kept small. It is the step that gives [fast interchange of address chunks](tape-interchange.md) its saving.

Let $a$ be the rank of an edge matrix; this counts the smaller calls that edge costs, so an edge matrix of rank $a$ costs $a$ smaller calls. The recursion runs over $W$ fixed wire roles, where $W$ is the number of roles. Let $s$ be the total number of smaller calls over all roles, and let $m$ be the dimension of the fixed space that holds the subspace labels.

The recursion splits its array into [role streams from a cyclic row split](role-streams.md) across the $W$ roles, so each role carries an equal share of the volume. The recursion is stated in the [frame of a vertex](frame.md) at each end of an edge, since frame changes cancel along a route. The total cost is measured by [nested subspace labels](subspace-labels.md) on the edges, whose dimension drops count the smaller operations on each edge.

Summing over the edges, the total number $s$ of smaller calls is less than $Wm$ <cite data-source="paper">The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.</cite>. The method therefore shows its claim by counting: each edge's cost is its rank, the roles split that cost evenly, and the label dimensions bound the sum. Because $s<Wm$, multiplying the parameter by $m$ multiplies the cost by less than $m$ per unit volume.

The main motivation is that the interchange of two equal address fields of width $u$ must cost less than linear in $u$ per unit volume, and this bound supplies that saving.
