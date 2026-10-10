On a [multitape Turing machine](turing-machine-model.md), a linear network is a fixed directed graph whose nodes are sources, gates and sinks, which exchange banks of values along its edges. Each wire at a fixed place in the network is called a *role*. To run the network on a tape array, the array's rows are distributed cyclically among $W$ roles, so each role receives a stream of $V/W$ bits. A pointwise scalar gate is applied to matching addresses on the roles it touches.

The new idea is a *frame*. At each source, gate, or sink $v$ we choose an invertible linear operator $D_v$ on the space of arrays indexed by the common address set. The stored array on that node is $D_v g$, where $g$ is the logical array. All edges of one gate use the same frame.

Along an edge from $u$ to $v$, the stored array changes from $D_u g$ to $D_v g$, so the change of representation is $D_v D_u^{-1}$. For example, if $D_u = 2$ and $D_v = 1$ on scalar arrays, the edge multiplies the stored value by $1/2$. Along a route through the network, these changes cancel in pairs, so a route from input role $w$ to output role $\rho(w)$ applies only $D_{\text{sink}}\, D_{\text{source}}^{-1}$.

The frames also commute with pointwise linear gates: if $G$ is a pointwise linear gate, then $G(D_v g_1, \dots, D_v g_t) = D_v\, G(g_1, \dots, g_t)$. So a gate can be placed anywhere in the network without changing its effect on the frames.

The network exchanges two banks of values with prescribed signs, and it restores every auxiliary value it touches, so scratch registers can start with arbitrary contents. The [subset-intersection construction](subspace-intersection-network.md) attaches subspaces to these gates, and the [address-field interchange](address-interchange.md) is built from such a network.
