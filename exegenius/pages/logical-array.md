A logical array is the array of values that a role presents to a network, which can differ from the array physically stored at a vertex by a frame. The argument keeps the logical array fixed while the storage changes, so that the effect of a network can be read off its endpoints, as the [Subset-intersection network](subset-intersection-network.md) relies on.

A logical array is an instance of an [Array](array.md) indexed by a common address set. It is the array that the network's gates compute on. The logical array of a role is carried by the [Linear networks and frames](linear-network-frames.md) at that role. A *frame* is an invertible linear operator $D_v$ attached to a vertex $v$, acting on arrays indexed by that address set. The stored array at $v$ is $D_v g$ when the logical array is $g$:

$$\text{stored array at } v = D_v\,g.$$

<cite data-source="paper">the stored array is Dv g when the logical array is g.</cite>

Along an edge from $u$ to $v$, the edge operator $D_v D_u^{-1}$ changes the stored array from $D_u g$ to $D_v g$, because $D_v D_u^{-1}(D_u g)=D_v g$. The logical array does not change: <cite data-source="paper">the frame changes while the logical array stays fixed</cite>.

A *pointwise linear gate* $G$ combines its $t$ input arrays $g_1,\dots,g_t$ the same way at every address. The scalars $\upsilon_1,\dots,\upsilon_t$ are the fixed weights of the gate, elements of $F$. The gate computes

$$G(g_1,\dots,g_t)=\upsilon_1 g_1+\dots+\upsilon_t g_t.$$

If all inputs share the frame $D_v$, the gate commutes with it, because $D_v$ is linear: <cite data-source="paper">At a pointwise linear gate G, the common frame commutes with the gate:</cite>

$$G(D_v g_1,\dots,D_v g_t)=D_v\,G(g_1,\dots,g_t).$$

Worked example. Let $D_v$ swap the two entries of a two-entry array, so $D_v$ is its own inverse. Take $g_1=(1,5)$, $g_2=(2,0)$ and $\upsilon_1=\upsilon_2=1$. Then $G(g_1,g_2)=(3,5)$ and $D_v(3,5)=(5,3)$. On the stored arrays, $D_v g_1=(5,1)$ and $D_v g_2=(0,2)$, whose sum is $(5,3)$ as well.

A *route* is a sequence of vertices joined by edges, from a source to a sink. Here $\mathrm{last}$ is the index of the sink, which equals the number of edges on the route. Its vertices are $x_0,x_1,\dots,x_{\mathrm{last}}$, with $x_0$ the source and $x_{\mathrm{last}}$ the sink. Composing its edge operators in order gives

$$(D_{x_{\mathrm{last}}}D_{x_{\mathrm{last}-1}}^{-1})\cdots(D_{x_1}D_{x_0}^{-1})=D_{x_{\mathrm{last}}}D_{x_0}^{-1}.$$

Each interior vertex $x_1,\dots,x_{\mathrm{last}-1}$ appears once as $D_{x}$ and once as $D_{x}^{-1}$ in adjacent factors, so those factors multiply to the identity. <cite data-source="paper">Thus the intermediate frames cancel,</cite> and the route changes only its endpoint frames. The gates pass the frames through unchanged, so this composite is the whole effect of the route on the logical array.

The endpoint operator is the operator that a network realises on each role's array once all intermediate frames have cancelled. It therefore depends only on the endpoint frames $D_{x_{\mathrm{last}}}$ and $D_{x_0}^{-1}$.
