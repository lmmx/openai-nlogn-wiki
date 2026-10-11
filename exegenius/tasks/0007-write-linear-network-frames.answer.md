A linear network is a fixed wiring of linear gates that exchanges two banks of values and restores its scratch values. A frame is an invertible operator attached to a vertex of such a network, saying how the array on a wire is stored. Each tape procedure in the argument is realised as one such network acting on arrays, and frames are what let its gates act on those arrays without changing their representation.

Here a tape procedure is an operation that rearranges the contents of the tapes of a Turing machine. A scratch (auxiliary) wire is a wire that carries no input or output and whose value must be restored at the end.

The network is built from wires, gates and roles. A gate is a fixed linear map on a specified set of wires; untouched wires keep their values. <cite data-source="paper">A gate is a fixed linear map on a specified set of wires; untouched wires retain their values.</cite> Each wire runs from its source through the gates that touch it, in time order, to its sink. <cite data-source="paper">A wire’s fixed place in the network is called its role.</cite> A role names a position in the network, not the value currently sitting there.

The claim this page supports is that each tape procedure is such a network: <cite data-source="paper">Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value.</cite>

To run the network on arrays, replace each scalar by an array indexed by a common set of addresses, and apply each gate pointwise, meaning separately at each address. <cite data-source="paper">A scalar gate is then applied pointwise to matching addresses on the roles that it touches.</cite> Then, at each source, gate and sink $v$, choose an invertible linear operator $D_v$ on these arrays. Here $g$ is the logical array, the array a wire is meant to represent before any frame is applied. <cite data-source="paper">We call Dv its frame: the stored array is Dv g when the logical array is g.</cite> The stored array on a wire is therefore $D_v g$ at vertex $v$, and <cite data-source="paper">All incidences of one gate have the same frame.</cite>

A wire’s stored representation can change from one vertex to the next. <cite data-source="paper">Along an edge from u to v, the operator</cite> $D_v D_u^{-1}$ changes the stored array from $D_u g$ to $D_v g$, while the logical array $g$ stays the same.

Frames are what make the gates cheap. Write $G$ for a pointwise linear gate, which combines the entries of several wires at each address. <cite data-source="paper">At a pointwise linear gate G, the common frame commutes with the gate:</cite>

$$G(D_v g_1, \dots, D_v g_t) = D_v\, G(g_1, \dots, g_t).$$

So a gate that receives stored arrays in the common frame $D_v$ returns a stored array still in frame $D_v$. The gate never converts representations; changes of representation happen on edges.

Worked example. Take $t = 2$, the gate $G(a, b) = a + b$ on arrays with two addresses, and let $D_v$ be the matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ acting on column vectors. For logical arrays $g_1 = (1, 0)$ and $g_2 = (0, 1)$, the stored inputs are $D_v g_1 = (1, 0)$ and $D_v g_2 = (1, 1)$. The gate applied to the stored arrays gives $(2, 1)$. The logical sum is $g_1 + g_2 = (1, 1)$, and $D_v (1, 1) = (2, 1)$. The two computations agree, so the gate can run directly on the stored arrays.

Frames also fix the endpoints. <cite data-source="paper">The supplied input needs no preliminary change of frame</cite>: its logical interpretation is defined by applying the inverse input frame. A route from an input wire $w$ to an output role $\rho(w)$ therefore applies $D_{\mathrm{sink}(\rho(w))} D_{\mathrm{source}(w)}^{-1}$ to the array, together with the scalar sign of that route. <cite data-source="paper">Thus the intermediate frames cancel</cite>, so only the endpoint frames remain. The scalar network carries the exchange of the two banks; the endpoint frames turn it into a fixed operator on the stored arrays.

For the bit procedure, the endpoint operator is a shear of two address fields, <cite data-source="paper">For the bit procedure, that endpoint operator is an address shear</cite>, which is the operation of the address shear page that builds on this one.
