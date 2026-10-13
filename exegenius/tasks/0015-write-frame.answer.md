A frame of a vertex is an invertible linear operator attached to a gate or terminal in a [Linear network](linear-network.md) that fixes how the array on each wire there is stored. Frames let the network keep data in different stored forms at different vertices, while the net effect of a route on each role's array stays a single endpoint operator, which the interchange argument needs.

Let $u$ and $v$ be vertices joined by an edge from $u$ to $v$, where a vertex is a source, gate or sink of the network. The frame $D_v$ is an invertible linear operator on the space of arrays indexed by the common address set, and all incidences of one gate share its frame. If $g$ is the logical array, the stored array is $D_v g$.

Along the edge, the frame change $D_vD_u^{-1}$ converts the stored form at $u$ into the stored form at $v$. <cite data-source="paper">changes the stored array from $D_ug$ to $D_vg$</cite> For example, if $D_u$ is the identity and $D_v = 2I$, then a logical array $g$ is stored as $g$ at $u$ and as $2g$ at $v$, and the change along the edge doubles it.

A pointwise linear gate commutes with its common frame, so it computes on stored arrays as it would on logical ones.

The argument needs frames because a role's array may change representation along the network. Composing the frame changes along a route leaves only the frames at its two ends, which is the cancellation the argument uses. <cite data-source="paper">the intermediate frames cancel</cite>
