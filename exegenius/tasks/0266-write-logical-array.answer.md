A logical array is an instance of an [Array](array.md) indexed by a common address set: it is the array of values that a role presents to a network, and it is the array that the network's gates compute on. The argument uses it to change how a role's values are stored without changing what the gates compute, so that the intermediate changes cancel and the net effect depends only on the endpoints. The page that builds on this one defines the endpoint operator as the operator a network realises on each role's array once all intermediate frames have cancelled.

The logical array of a role is carried by the [Linear networks and frames](linear-network-frames.md) at that role. A *frame* is an invertible linear operator $D_v$ attached to a vertex $v$ of the network. The stored array is the array actually held at $v$, and the frame relates it to the logical array $g$: <cite data-source="paper">the stored array is Dv g when the logical array is g.</cite>

Along an edge the frame changes but the logical array does not: <cite data-source="paper">the frame changes while the logical array stays fixed</cite>. So the stored array is rewritten at each step while the logical array $g$ stays the same.

A pointwise linear gate combines its input arrays entrywise at each address, with fixed weights $c_1,\dots,c_t$ on its $t$ inputs. When all its inputs share one frame $D_v$, the gate commutes with that frame: <cite data-source="paper">At a pointwise linear gate G, the common frame commutes with the gate:</cite>

$$G(D_v g_1,\dots,D_v g_t)=D_v\,G(g_1,\dots,g_t).$$

Worked example. Take arrays with two entries, and let $D_v$ be the operator that swaps the two entries. It is invertible, and it is its own inverse, so the logical array is recovered from the stored array by applying $D_v$ again. Let the logical inputs of a gate be $g_1=(1,5)$ and $g_2=(2,0)$, and let the gate add its inputs entrywise. Then $G(g_1,g_2)=(3,5)$, and applying $D_v$ gives $(5,3)$. On the stored arrays, $D_v g_1=(5,1)$ and $D_v g_2=(0,2)$, and their entrywise sum is $(5,3)$ as well. The gate therefore gives the same result whether the frame is applied before or after it runs.

<cite data-source="paper">Thus the intermediate frames cancel,</cite> so a route through the network changes only the endpoint frames, which is why the endpoint operator is defined in terms of them.
