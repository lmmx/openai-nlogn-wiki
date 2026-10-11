A logical array is the array of values that a role presents to a network, as distinct from the array physically stored at a vertex of that network. The argument keeps it fixed while storage changes, so that the endpoint operator can be read off the endpoints.

A logical array is an instance of an [Array](array.md) indexed by a common address set. It is the array that the network's gates compute on. The logical array of a role is carried by the [Linear networks and frames](linear-network-frames.md) at that role. A *frame* is an invertible linear operator $D_v$ attached to a vertex $v$, and the stored array at $v$ is $D_v g$ when the logical array is $g$:

$$\text{stored array at } v = D_v\,g.$$

<cite data-source="paper">the stored array is Dv g when the logical array is g.</cite>

The edge operator $D_v D_u^{-1}$ carries the stored array at the start $u$ of an edge to the stored array at its end $v$: it sends $D_u g$ to $D_v g$, because $D_v D_u^{-1}(D_u g)=D_v g$. The logical array $g$ does not change: <cite data-source="paper">the frame changes while the logical array stays fixed</cite>.

A *pointwise linear gate* $G$ with fixed input weights $\alpha_1,\dots,\alpha_t$ combines its inputs at each address: $G(g_1,\dots,g_t)=\sum_{s=1}^{t}\alpha_s g_s$. If all its inputs share the frame $D_v$, the gate commutes with that frame, because $D_v$ is linear:

<cite data-source="paper">At a pointwise linear gate G, the common frame commutes with the gate:</cite>

$$G(D_v g_1,\dots,D_v g_t)=\sum_{s=1}^{t}\alpha_s D_v g_s=D_v\,G(g_1,\dots,g_t).$$

Worked example. Let $D_v$ swap the two entries of a two-entry array. It is its own inverse, so applying it again recovers the logical array. Take $g_1=(1,5)$, $g_2=(2,0)$ and $\alpha_1=\alpha_2=1$. Then $G(g_1,g_2)=(3,5)$, and $D_v(3,5)=(5,3)$. On the stored arrays, $D_v g_1=(5,1)$ and $D_v g_2=(0,2)$, whose sum is $(5,3)$ as well, so the gate gives the same result whether the frame is applied before or after it.

A *route* is a sequence of vertices joined by edges, from a source to a sink. Let $L$ be the number of edges on the route, and write its vertices $x_0,x_1,\dots,x_L$, with $x_0$ the source and $x_L$ the sink. Composing its edge operators in order gives

$$(D_{x_L}D_{x_{L-1}}^{-1})\cdots(D_{x_1}D_{x_0}^{-1})=D_{x_L}D_{x_0}^{-1},$$

because each adjacent pair $D_{x_i}^{-1}D_{x_i}$ is the identity and cancels. <cite data-source="paper">Thus the intermediate frames cancel,</cite> so a route changes only the endpoint frames $D_{x_L}$ and $D_{x_0}$. The gates pass the frames through unchanged, so this composite is the whole effect of the route. The endpoint operator is the operator a network realises on each role's array once all intermediate frames have cancelled, so it is determined by those endpoint frames.
