Rank-saving recursion is a recursive scheme that runs on a [linear network](linear-network.md). It pays for each edge of the network with smaller calls, and it keeps the total number of those calls below a fixed bound, which is what gives [fast interchange of address chunks](tape-interchange.md) its saving.

An edge matrix is the matrix that says what one edge of the network does to the values it carries. Write $a$ for the rank of one edge matrix. Summing $a$ over all edges gives the total number of smaller calls, $s$. <cite data-source="paper">The number of recursive calls is the sum of the edge ranks, exactly $s$.</cite>

The recursion is stated in the [frame of a vertex](frame.md) at each end of an edge, where the frame is the invertible linear operator that fixes how the array on that vertex's wires is stored. The recursion splits its array into [role streams from a cyclic row split](role-streams.md) across the $W$ roles, the fixed wire places of the network. Each role therefore holds an equal share $V/W$ of the padded volume $V$, and each smaller call acts on one such share.

The cost is measured by [nested subspace labels](subspace-labels.md) on the edges. Each vertex gets a subspace of a fixed $m$-dimensional space, adjacent subspaces are nested, and the drop in dimension across an edge measures the smaller calls that edge needs.

The finite construction of the paper uses three-element subsets, with gather and scatter wires, and it has the property that the total satisfies $s<Wm$. <cite data-source="paper">The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.</cite> So on average each role makes fewer than $m$ smaller calls.

The paper uses this bound for interchange. <cite data-source="paper">Because the sum of these ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width.</cite>
