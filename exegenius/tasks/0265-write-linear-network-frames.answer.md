A linear network with frames realises each tape procedure on arrays: a fixed wiring of linear gates that exchanges two banks of values and restores its auxiliary (scratch) values. It is the step that lets the main result count the cost of each procedure.

A bank is a set of wires indexed by a common index set, so exchanging two banks swaps the values at matching indices. <cite data-source="paper">Each procedure arises from its own fixed linear network that exchanges two banks of values</cite>, and it <cite data-source="paper">restores every auxiliary value</cite>.

A gate is a fixed linear map on some wires, and <cite data-source="paper">untouched wires retain their values.</cite> <cite data-source="paper">The vertices on a wire are its source, the gates that touch it in time order, and its sink</cite>. <cite data-source="paper">We call the name of a wire its role</cite>.

Each scalar becomes an array indexed by a common set of addresses, and each gate acts separately at each address. The logical array $g$ is the array a wire is meant to represent. Each vertex $v$ carries an invertible linear operator $D_v$, its frame, so the stored array there is $D_v g$. Frames are built from invertible linear operators, as defined in [Linear algebra basics](linear-algebra-basics.md).

Let an edge go from $u$ to $v$, where $u$ is the earlier vertex. <cite data-source="paper">the operator Dv Du−1 changes the stored array</cite>: the edge operator $D_v D_u^{-1}$ takes $D_u g$ to $D_v g$, while $g$ does not change.

Let $G$ be a pointwise linear gate with $t$ inputs, where $t$ is the number of input arrays it takes. Its inputs are logical arrays $g_1,\dots,g_t$, and each input $s$ has a fixed weight $\alpha_s$, the same at every address. <cite data-source="paper">At a pointwise linear gate G, the common frame commutes with the gate:</cite>

$$G(D_v g_1, \dots, D_v g_t) = D_v\, G(g_1, \dots, g_t).$$

This is why frames sit on the wires. A gate adds its inputs entrywise, so inputs in different frames would not add to the stored form of the sum. With one frame $D_v$ on every input and on the output, the gate computes the logical sum in stored form, and the representation is unchanged. For example, take $t = 2$, $G(g_1, g_2) = g_1 + g_2$, and let $D_v$ have rows $(1, 1)$ and $(0, 1)$. For $g_1 = (1, 0)$ and $g_2 = (0, 1)$, the stored inputs $(1, 0)$ and $(1, 1)$ sum to $(2, 1)$, which is $D_v(1, 1)$.

Inputs must share one frame, and <cite data-source="paper">the intermediate frames can then be chosen to make each edge change inexpensive</cite>. <cite data-source="paper">The supplied input needs no preliminary change of frame</cite>. Write $\ell$ for an input wire, $\theta_\ell$ for its supplied physical array, and $\mathrm{source}(\ell)$ for its source vertex. Its logical array is $g_\ell = D_{\mathrm{source}(\ell)}^{-1}\theta_\ell$.

A permutation $\rho$ of roles sends each input role $\ell$ to an output role $\rho(\ell)$, multiplying by a fixed sign $\varepsilon_\ell$. Write $\mathrm{sink}(r)$ for the sink vertex of output role $r$. Along a route through vertices $x_0,\dots,x_k$, where $x_0=\mathrm{source}(\ell)$ and $x_k=\mathrm{sink}(\rho(\ell))$, each inner pair $D_{x_i}^{-1}D_{x_i}$ cancels, so the edge operators telescope to $D_{x_k}D_{x_0}^{-1}$. <cite data-source="paper">Thus the intermediate frames cancel</cite>, leaving the endpoint operator

$$\varepsilon_\ell\, D_{\mathrm{sink}(\rho(\ell))}\, D_{\mathrm{source}(\ell)}^{-1}\,\theta_\ell.$$

<cite data-source="paper">We use the bit network to interchange two equal address chunks on tape.</cite> The bit procedure is realised by the bit network, a linear network on bits, which <cite data-source="paper">uses only pointwise XOR gates</cite>. Its frames act on the [Address field](address-field.md) blocks of each array, with $H$ the first field and $K$ the second, not a frame. <cite data-source="paper">For the bit procedure, that endpoint operator is an address shear</cite>: <cite data-source="paper">two fields, written as vectors H, D over a common residue ring, are updated by (H, D) 7→ (H + D, D)</cite>. Over bits $H+K$ is a bitwise XOR, so the shear is a pointwise XOR of the two fields, which is why an XOR network with frames on the address fields realises it. <cite data-source="paper">Two further linear-cost address updates complete their interchange</cite>, the XOR swap $H\leftarrow H+K$, $K\leftarrow K+H$, $H\leftarrow H+K$.

The claim is that each tape procedure is such a network. <cite data-source="paper">We construct two fixed linear networks that exchange two banks of values while restoring every auxiliary value.</cite> The scalar network (the wiring on single values) <cite data-source="paper">already has the required signed exchange.</cite> The endpoint formula then gives each route's operator.
