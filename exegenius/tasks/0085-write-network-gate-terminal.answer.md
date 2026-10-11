A network carries values on *wires*. A wire's fixed place in the network is its *role*, and at any moment it carries one scalar. The vertices on a wire are its source, the gates that touch it in time order, and its sink, and consecutive vertices are joined by edges. The source and the sink of a wire are its *terminals*: the ends where the network's values enter or leave.

A *gate* is a fixed linear map on a specified set of wires, <cite data-source="paper">A gate is a fixed linear map on a specified set of</cite> wires. Wires that the gate does not touch keep their values. For a scalar gate, the map acts at each *address*, meaning each position in the arrays that the wires carry: the gate combines the values at one address using only the values at that same address. The gate is <cite data-source="paper">applied pointwise to matching addresses on the roles that it touches</cite>.

Example. Let a gate replace two wire values by their sum and then by their difference. At an address where the two wires hold $3$ and $1$, the gate leaves $4$ and $2$ there, and a third wire at that address keeps its value.

Each gate and each terminal $v$ of a network with frames carries a frame $D_v$, an invertible operator on arrays. Every incidence of one gate uses the same frame, which is why a gate is stated in terms of a single $D_v$. A pointwise linear gate commutes with its frame: <cite data-source="paper">At a pointwise linear gate G, the common frame commutes with the gate</cite>. For a two-wire gate this reads
$$G(D_v g_1,\, D_v g_2) = D_v\, G(g_1, g_2).$$
So the gate can be applied to the stored arrays and the frame taken out afterwards, without changing the logical result.

A gate or terminal is a vertex type of [Linear networks and frames](linear-network-frames.md), since each vertex carries a frame.
