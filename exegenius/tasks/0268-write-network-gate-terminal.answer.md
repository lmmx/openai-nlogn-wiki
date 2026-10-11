A *gate* is the vertex where several wires meet and their values are combined, and a *terminal* is an end of a wire where the network's values enter or leave. The subset-intersection network is built from gates and terminals, so this page fixes what they do and why a gate can be applied to stored arrays.

A network carries values on *wires*. A wire's fixed place in the network is its *role*, and at any moment it carries one scalar. The vertices on a wire are its source, the gates that touch it in time order, and its sink; consecutive vertices are joined by edges. The source and the sink of a wire are its *terminals*.

A gate or terminal is a vertex type of [Linear networks and frames](linear-network-frames.md), since each vertex carries a frame.

A gate is <cite data-source="paper">a fixed linear map on a specified set of</cite> wires. Wires that the gate does not touch keep their values. For a scalar gate, the map acts at each *address*, a position in the arrays that the wires carry, and combines the values at one address using only the values at that same address. The gate is <cite data-source="paper">applied pointwise to matching addresses on the roles that it touches</cite>.

Example. Let a gate act on two wires that hold $3$ and $1$ at an address. It replaces them by their sum and their difference, both computed from the original values: the first wire gets $3+1=4$ and the second gets $3-1=2$. A third wire at that address keeps its value.

Each gate and each terminal $v$ carries a frame $D_v$, an invertible operator on arrays. All incidences of one gate use the same $D_v$, because the gate combines the values at one address across its wires, and that combination means something only when those values are stored in one common frame.

A pointwise linear gate commutes with its frame: <cite data-source="paper">At a pointwise linear gate G, the common frame commutes with the gate</cite>. For a two-wire gate with logical input arrays $g_1$ and $g_2$ (the arrays on its first and second input wire),
$$G(D_v g_1,\, D_v g_2) = D_v\, G(g_1, g_2).$$
The reason is that each output of the gate is a fixed combination $c_1 g_1 + c_2 g_2$ with the same weights at every address. In the example, the outputs are $g_1 + g_2$ and $g_1 - g_2$. Since $D_v$ is linear, $D_v(g_1 + g_2) = D_v g_1 + D_v g_2$ and $D_v(g_1 - g_2) = D_v g_1 - D_v g_2$, so applying the frame before or after the gate gives the same two arrays.

So the gate can be applied to the stored arrays and the frame taken out afterwards, without changing the logical result.
