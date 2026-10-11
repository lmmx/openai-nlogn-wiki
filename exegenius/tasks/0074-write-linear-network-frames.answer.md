A linear network is a fixed wiring of linear gates that exchanges two banks of values and restores its scratch values. A frame is built from an invertible [linear operator](linear-algebra-basics.md) attached to a vertex of a network, saying how the array on its wires is stored. Each tape procedure is realised as one such network acting on arrays, and frames let its gates act on those arrays without changing their representation.

A tape procedure is an operation on the tapes of a Turing machine. A scratch (auxiliary) wire carries no input or output and is restored at the end.

A gate is a fixed linear map on a specified set of wires, and <cite data-source="paper">untouched wires retain their values.</cite> <cite data-source="paper">The vertices on a wire are its source, the gates that touch it in time order, and its sink</cite>; the segment between consecutive vertices is an edge. <cite data-source="paper">We call the name of a wire its role</cite>: a role is a fixed place in the network, not the value there.

The logical array $g$ of a wire at a vertex is the array the wire is meant to represent before any frame is applied. To run the network on arrays, let each scalar be an array indexed by a common set of addresses, and let each gate act separately at each address. Let $G$ be a pointwise linear gate. $t$ is the number of input arrays the gate takes, and $g_1,\dots,g_t$ are its logical input arrays. Each $c_j$ is the fixed weight of input $j$, the same at every address, so $G(g_1,\dots,g_t)=\sum_j c_j g_j$ at each address.

At each vertex $v$ (a source, gate or sink) choose an invertible linear operator $D_v$ on arrays over the common addresses, and call $D_v$ the frame of $v$. The stored array at $v$ is $D_v g$. Along an edge from $u$ to $v$, where $u$ is the earlier vertex, <cite data-source="paper">the operator Dv Du−1 changes the stored array</cite> from $D_u g$ to $D_v g$, while $g$ does not change.

The key identity is <cite data-source="paper">At a pointwise linear gate G, the common frame commutes with the gate:</cite>

$$G(D_v g_1, \dots, D_v g_t) = D_v\, G(g_1, \dots, g_t).$$

It holds for every linear $D_v$, because $D_v$ is linear on whole arrays: $\sum_j c_j D_v g_j = D_v \sum_j c_j g_j$, with the same weights at every address. For example, take $t = 2$ and $G(g_1, g_2) = g_1 + g_2$ on arrays with two addresses, and let $D_v$ be the $2\times 2$ matrix with rows $(1, 1)$ and $(0, 1)$. For $g_1 = (1, 0)$ and $g_2 = (0, 1)$, the stored inputs are $(1, 0)$ and $(1, 1)$; the gate gives $(2, 1)$, which is $D_v(1, 1)$.

The inputs of a gate must share one representation for the combination to be the logical sum, and <cite data-source="paper">the intermediate frames can then be chosen to make each edge change inexpensive.</cite>

<cite data-source="paper">The supplied input needs no preliminary change of frame</cite>. Write $\mathrm{sink}(r)$ for the sink vertex of output role $r$. Write $w$ for an input wire, $f_w$ for the supplied physical array on it, and $\mathrm{source}(w)$ for its source vertex. Its logical array is $g_w = D_{\mathrm{source}(w)}^{-1} f_w$.

The scalar network sends input role $w$ to output role $\rho(w)$, where $\rho$ is this permutation of roles, and multiplies the value by a fixed sign $\varepsilon_w$ on the way. The logical array on $\rho(w)$ is therefore $\varepsilon_w g_w$, with stored array $D_{\mathrm{sink}(\rho(w))}\,\varepsilon_w g_w$ at the sink. Along the route the edge operators telescope, <cite data-source="paper">Thus the intermediate frames cancel</cite>, leaving

$$\varepsilon_w\, D_{\mathrm{sink}(\rho(w))}\, D_{\mathrm{source}(w)}^{-1} f_w.$$

The bit procedure is built from a network of pointwise XOR gates, since <cite data-source="paper">The bit network has Wb wires, uses only pointwise XOR gates</cite>, and the frames act on the [address fields](address-field.md) of each array. <cite data-source="paper">For the bit procedure, that endpoint operator is an address shear</cite>, which updates one field by adding the other.

The claim this page supports is that each tape procedure is such a network: <cite data-source="paper">Each procedure arises from its own fixed linear network that exchanges two banks of values</cite>. Its construction chooses a scalar network that exchanges the two banks and restores the scratch values; the endpoint formula then gives the operator on the arrays.
