A linear network with frames is a fixed wiring of linear gates that exchanges two banks of values while restoring its auxiliary (scratch) values. It realises each *tape procedure*, a fixed routine that a Turing machine runs on arrays stored on its tape, so that the [Integer multiplication below n log n](main-theorem.md) bound can count each procedure's cost. The [Address shear](address-shear.md) and [Address-field interchange](address-interchange.md) pages build on it.

A *wire* carries one scalar, and a *gate* is a fixed linear map on the wires it touches; <cite data-source="paper">untouched wires retain their values.</cite> <cite data-source="paper">The vertices on a wire are its source</cite>, the gates that touch it in time order, and its sink. <cite data-source="paper">We call the name of a wire its role</cite>, a fixed place in the network. A *bank* is a set of wires with a common index set, so exchanging two banks swaps the values at matching indices. <cite data-source="paper">Each procedure arises from its own fixed linear network that exchanges two banks of values</cite>, and the network <cite data-source="paper">restores every auxiliary value</cite>.

A *pointwise* gate acts separately at each address of its arrays. The *logical array* $g$ is the array a wire means. Frames are built from invertible linear operators, as defined in [Linear algebra basics](linear-algebra-basics.md). Each vertex $v$ carries such an operator $D_v$, its *frame*, and <cite data-source="paper">the stored array is Dv g when the logical array is g</cite>. <cite data-source="paper">Along an edge from u to v, the operator Dv Du−1 changes the stored array</cite>, so the edge operator $D_v D_u^{-1}$ takes $D_u g$ to $D_v g$.

Let $\Xi$ be a pointwise linear gate with inputs $g_1, g_2, \dots$. For such a gate, <cite data-source="paper">the common frame commutes with the gate</cite>:

$$\Xi(D_v g_1, D_v g_2, \dots) = D_v\,\Xi(g_1, g_2, \dots).$$

This is why frames sit on the wires: a gate adds entrywise, so its inputs must share one frame to add in stored form. Take $\Xi(g_1,g_2)=g_1+g_2$ and let $D_v$ have rows $(1,1)$ and $(0,1)$. For $g_1=(1,0)$ and $g_2=(0,1)$, the stored inputs $(1,0)$ and $(1,1)$ sum to $(2,1)=D_v(g_1+g_2)$.

Let $\ell$ name an input role (this page gives $\ell$ a new meaning). Let $\mathrm{source}(\ell)$ be the source vertex of input role $\ell$. The permutation $\Psi$ sends each input role $\ell$ to an output role $\Psi(\ell)$, with prescribed sign $\varsigma_\ell$, and $\mathrm{sink}(\Psi(\ell))$ is that output role's sink vertex. <cite data-source="paper">The supplied input needs no preliminary change of frame</cite>. The array supplied on wire $\ell$ is $\Upsilon_\ell$, and its logical array is $g_\ell = D_{\mathrm{source}(\ell)}^{-1}\Upsilon_\ell$.

A route $v_0,v_1,\dots,v_{\mathrm{end}}$ of vertices from $v_0=\mathrm{source}(\ell)$ to $v_{\mathrm{end}}=\mathrm{sink}(\Psi(\ell))$ has as operator the composite of its edge operators in route order:

$$(D_{v_{\mathrm{end}}}D_{v_{\mathrm{end}-1}}^{-1})\cdots(D_{v_1}D_{v_0}^{-1}).$$

At each inner vertex $v$ the factor $D_v^{-1}D_v$ is the identity, so the product telescopes to $D_{v_{\mathrm{end}}}D_{v_0}^{-1}$. <cite data-source="paper">Thus the intermediate frames cancel</cite>, and the stored output is

$$\varsigma_\ell\, D_{\mathrm{sink}(\Psi(\ell))}\, D_{\mathrm{source}(\ell)}^{-1}\,\Upsilon_\ell,$$

the endpoint operator, which depends only on the two end frames.

The bit procedure interchanges the values of two equal [Address field](address-field.md) blocks, $H$ and $K$, of each array. <cite data-source="paper">For the bit procedure, that endpoint operator is an address shear</cite>: it replaces $H$ by $H+K$ and keeps $K$. The paper writes this update as <cite data-source="paper">H, D over a common residue ring, are updated by (H, D) 7→ (H + D, D).</cite> This page writes the second field as $K$, not $D$. Over bits, $H+K$ is XOR, and the bit network <cite data-source="paper">uses only pointwise XOR gates</cite>, so it realises the shear.

Each tape procedure is such a network. <cite data-source="paper">The scalar network already has the required signed exchange.</cite> A scalar gate <cite data-source="paper">is then applied pointwise to matching addresses on the roles that it touches</cite>.
