The endpoint operator is realised by a [linear network](linear-network-frames.md) on each role's array once all intermediate frames have cancelled, so it depends only on the frames at the two ends of a route. For the bit procedure it is an [address shear](address-shear.md).

The frame at a vertex $v$ is the invertible operator $D_v$, and the array stored at $v$ is $D_v g$ for the logical array $g$. Take a path of three vertices $a$, $b$, $c$, so that the stored array changes from $D_a g$ to $D_b g$ on the first edge and from $D_b g$ to $D_c g$ on the second. The two edge changes compose to
$$(D_c D_b^{-1})(D_b D_a^{-1}) = D_c D_a^{-1},$$
because $D_b^{-1} D_b$ is the identity. The frame at the middle vertex $b$ cancels, and only the frames at the ends $a$ and $c$ remain.

The same cancellation holds along a route through the whole network. Write $w$ for an input role and $\rho$ for the signed role permutation realised by the scalar network, so that input role $w$ is sent to output role $\rho(w)$. Write $\varepsilon_w$ for the scalar sign carried by that route. Here $\mathrm{source}(w)$ is the vertex where input role $w$ starts and $\mathrm{sink}(\rho(w))$ is the vertex where output role $\rho(w)$ ends. The route applies
$$\varepsilon_w\, D_{\mathrm{sink}(\rho(w))}\, D_{\mathrm{source}(w)}^{-1}$$
to its input array. Undoing the role exchange and those signs, <cite data-source="paper">leaves the endpoint operator on every role array, including the</cite> roles that carry auxiliary scalar values, so the endpoint operator is $D_{\mathrm{sink}(\rho(w))}\, D_{\mathrm{source}(w)}^{-1}$ on each role array.

For the bit procedure, the endpoint operator is an address shear, a map on two address fields that is implemented by a small number of field interchanges. <cite data-source="paper">For the bit procedure, that endpoint operator is an address shear</cite>.
