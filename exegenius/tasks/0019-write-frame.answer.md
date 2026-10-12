A frame of a network vertex is an invertible linear operator attached to a vertex of a network that changes how the array on each wire is represented, without changing the logical array it encodes. Frames make the operator on each route through the network depend only on the route's two endpoints. Each frame acts on the wires of a [Linear network that restores auxiliary values](linear-network.md).

Let $D_v$ denote the frame at a source, gate or sink $v$: an invertible linear operator on the arrays indexed by the common address set, the addresses that every wire's array is indexed by. The stored array is $D_v g$ when the logical array is $g$, the array the computation means. Along an edge from $u$ to $v$, the operator $D_v D_u^{-1}$ turns the stored array $D_u g$ into $D_v g$.

A pointwise linear gate $G$ with $t$ inputs, where $t$ is the number of its input arrays, commutes with a common frame:

$$G(D_v g_1,\ldots,D_v g_t)=D_v\,G(g_1,\ldots,g_t).$$

This holds because $G$ combines its inputs with fixed scalar coefficients, and $D_v$ is linear, so $D_v$ moves across the combination.

The scalar network sends each input role $w$ to $\rho(w)$, the output role assigned to $w$, and multiplies the array by a sign $\varepsilon_w$, which is $+1$ or $-1$ and is fixed by the network. The route runs from the source of $w$ to the sink of $\rho(w)$. Each edge contributes a frame change and each gate passes its frame through, so the intermediate frames cancel and the route applies
$$\varepsilon_w\,D_{\mathrm{sink}(\rho(w))}\,D_{\mathrm{source}(w)}^{-1},$$
where $\mathrm{source}(w)$ and $\mathrm{sink}(\rho(w))$ are the vertices where the route starts and ends.

So the intermediate frames do not affect the route operator and may be chosen freely. The paper uses this freedom to make each edge change cheap, which this page does not need to explain. <cite data-source="paper">intermediate frames can then be chosen to make each edge change inexpensive</cite>.

Undoing the role exchange and the signs gives the endpoint operator on every role array. Undoing the exchange reads the output role $\rho(w)$ as the role $w$ again, and since $\varepsilon_w=\pm 1$, undoing the sign multiplies by $\varepsilon_w$ once more. The route identity holds for every input role, <cite data-source="paper">including the roles that carried auxiliary scalar values</cite>.
