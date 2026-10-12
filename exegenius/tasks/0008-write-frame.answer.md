A frame of a network vertex is an invertible linear operator attached to a vertex of a network that changes how the array on each wire is represented. Each frame acts on the wires of a [Linear network that restores auxiliary values](linear-network.md). The logical array it encodes stays the same, so the representation can change along the network without changing the computation.

Let $D_v$ denote the frame at a source, gate or sink $v$: an invertible linear operator on the space of arrays indexed by the common address set. The stored array is $D_v g$ when the logical array is $g$, and all incidences of one gate share one frame. Along an edge from $u$ to $v$, the operator $D_v D_u^{-1}$ turns the stored array $D_u g$ into $D_v g$.

Pointwise linear gates are what make the frames cancel. For a pointwise linear gate $G$ with frame $D_v$, the common frame commutes with the gate:

$$G(D_v g_1,\ldots,D_v g_t)=D_v\,G(g_1,\ldots,g_t).$$

On a route from an input role $w$ to the output role $\rho(w)$ assigned to it, the intermediate frames cancel along the path, leaving the operator $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$, where $\mathrm{source}(w)$ and $\mathrm{sink}(\rho(w))$ are the vertices at which the route starts and ends, times its prescribed scalar sign. Thus the operator on a route depends only on its two endpoint frames. For example, a route from a source with frame $D_a$ through a gate with frame $D_b$ to a sink with frame $D_c$ applies $D_b D_a^{-1}$ and then $D_c D_b^{-1}$, which multiply to $D_c D_a^{-1}$.

Since intermediate frames do not affect the route operator, they are free to choose, and each edge can be made cheap. <cite data-source="paper">intermediate frames can then be chosen to make each edge change inexpensive</cite>.

After the role exchange and the signs are undone, the endpoint operator applies to every role array, <cite data-source="paper">including the roles that carried auxiliary scalar values</cite>. Later pages apply this to the [Subset-intersection network](subset-network.md).
