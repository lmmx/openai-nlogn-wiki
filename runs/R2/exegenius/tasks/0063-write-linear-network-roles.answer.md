A *finite linear network with roles and frames* is a fixed wiring of linear steps that exchanges two banks of values with prescribed signs and restores every auxiliary value it uses. Each fixed-tape procedure of the argument comes from one such network; this page explains how it computes its result.

A wire's fixed place in the network is its *role*. Let $W$ be the number of roles.

To run the network on an array, regard a row as the complete ordered suffix of the array's address, at a fixed prefix and row index. These rows are the suffixes of [Address fields and array layout on tapes](address-fields.md), so the network acts on rows indexed by those fields. Distribute the rows cyclically among the roles: row $\ell$, the $\ell$th row at a fixed prefix, goes to role $\ell \bmod W$, after the row count for each prefix is padded to a multiple of $W$. Let $V$ be the number of bits stored after padding. Each role stream then holds $V/W$ bits <cite data-source="paper">contains $V/W$ bits</cite>.

Each source, gate and sink $v$ carries an invertible linear operator $D_v$ on arrays indexed by the common address set, its *frame*. The stored array is $D_v g$ when the logical array is $g$. A frame acts on addresses within one wire's array and never mixes wires. Along an edge from $u$ to $v$ the stored array changes by $D_vD_u^{-1}$; here $u$ names a node, not the address field width.

Frames pass through gates. A pointwise linear gate $G$ combines its $t$ input arrays, where $t$ counts them, at each address with fixed scalar coefficients. Since $D_v$ is linear over those scalars and is the same for every input, applying it before the gate equals applying it after:
$$G(D_v g_1,\ldots,D_v g_t)=D_v G(g_1,\ldots,g_t),$$
Here $g_1,\ldots,g_t$ are the logical input arrays. So intermediate frames cancel along a route.

Let $\rho$ be the permutation of roles that the scalar network applies, and for an input role $w$ let $\varepsilon_w$ be the sign on its route to output role $\rho(w)$. Let $\mathrm{source}(w)$ and $\mathrm{sink}(\rho(w))$ be the source and sink nodes at the ends of that route. The route applies $\varepsilon_w D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$. Undoing the exchange moves each output back to its input role, and multiplying by $\varepsilon_w$ again removes the sign. In the paper's complex construction, $\rho$ fixes each scratch role with sign $+1$ <cite data-source="paper">each scratch input to its own output with sign $+1$</cite>, so scratch roles are unchanged by this undoing. Every role keeps the endpoint operator <cite data-source="paper">leaves the endpoint operator on every role array</cite>, auxiliary roles included.

For example, if a route has source frame $I$, the identity, and sink frame $D_v$, its operator is $D_v$, however many gates it passes through.
