A frame of a network vertex is an invertible linear operator attached to a vertex of a network that changes how the array on each wire is stored, without changing the logical array it encodes. Frames make the operator on each route through the network depend only on the route's two endpoints. Each frame acts on the wires of a [Linear network that restores auxiliary values](linear-network.md).

Let $D_r$ denote the frame at a source, gate or sink $r$: an invertible linear operator on the arrays indexed by the common address set, the addresses that every wire's array is indexed by. The stored array is $D_r g$ when the logical array is $g$, the array the computation means. Along an edge from $r$ to $s$, the operator $D_s D_r^{-1}$ turns the stored array $D_r g$ into $D_s g$.

A pointwise linear gate $G$ with $t$ inputs, where $t$ is the number of its input arrays, commutes with a common frame: $G(D_r g_1,\ldots,D_r g_t)=D_r\,G(g_1,\ldots,g_t)$.

This holds because $G$ combines its inputs with fixed scalar coefficients, and $D_r$ is linear, so $D_r$ moves across the combination.

The scalar routing sends each input role $w$ to $\rho(w)$, the output role assigned to $w$, and multiplies the array by a sign $\varepsilon_w$, which is $+1$ or $-1$ and is fixed by the network. Each edge contributes a frame change and each gate passes its frame through, so the intermediate frames cancel and the route applies

$$\varepsilon_w\,D_{\mathrm{sink}(\rho(w))}\,D_{\mathrm{source}(w)}^{-1},$$

where $\mathrm{source}(w)$ and $\mathrm{sink}(\rho(w))$ are the vertices where the route starts and ends.

So the intermediate frames do not affect the route operator and may be chosen freely, <cite data-source="paper">to make each edge change inexpensive</cite>.

Undoing the role exchange and the signs gives the endpoint operator on every role array. Undoing the exchange reads the output role $\rho(w)$ as the role $w$ again, and undoing the sign multiplies by $\varepsilon_w$ once more, which cancels the sign. The route identity therefore holds for every input role, <cite data-source="paper">including the roles that carried auxiliary scalar values</cite>.
