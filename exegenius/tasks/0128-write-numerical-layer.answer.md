A numerical layer is one stage of the transform calculation, in which a simultaneous butterfly is applied to a chosen set of selected axes of the array. The numerical layer computes the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) on its selected bits, in one pass rather than one axis at a time.

Each address of the array is written as $D$ consecutive chunks of $K$ address bits, where $K$ is the number of address bits in each chunk. <cite data-source="paper">Each address carries a polynomial record with r complex coefficients</cite>, that is, a polynomial with $r$ complex coefficients stored as its coefficient list. In every chunk one bit is selected, all at one offset: <cite data-source="paper">On each of the D consecutive K-bit address chunks, select bit ρ, numbered from the least significant bit</cite>. So the $D$ selected bits sit at the same position within their chunks.

Applying the two-point map $H_0(u,v) = ((u+v)/2, (u-v)/2)$ to one selected bit combines each pair of records whose addresses differ only in that bit. Applying it to all $D$ selected bits at once is the tensor product $H_0^{\otimes D}$, which combines each group of $2^D$ records that agree outside the selected bits. The map acts on each coefficient separately and fixes every other address bit.

For example, take $D = 2$ and four records whose first coefficients, at the settings $(0,0)$, $(0,1)$, $(1,0)$ and $(1,1)$ of the two selected bits, are $1, 3, 5, 7$. Then $H_0^{\otimes 2}$ gives the first coefficients $4, -1, -2, 0$ at the same four settings. At the setting $(0,1)$ the value is $(1-3+5-7)/4 = -1$.

Doing the same work one axis at a time is more expensive: <cite data-source="paper">whereas separate butterfly factors would require D whole-array passes</cite>, each of which reads every stored bit. The layer does all $D$ selected bits in one pass.

Here $d$ is an upper bound on the number $D$ of selected axes in a layer. Here $\lambda'$ is a fixed exponent below one, so that the cost is $O(V d^{\lambda'})$. <cite data-source="paper">the cost is O(V dλ ) for a fixed λ′ < 1</cite>. Since $\lambda' < 1$, the cost grows more slowly than linearly in $d$.

The layer is computed exactly. Its intermediate values are Gaussian dyadics $\mathbb{D}$, and <cite data-source="paper">The entire layer is evaluated exactly before one final truncation.</cite>

This is what the argument needs from the layer. The argument needs each recursive call to make fewer than $Wm$ smaller calls, where $W$ is the number of roles in the network. <cite data-source="paper">Distribute rows cyclically among the W roles</cite>. The recursive contribution then grows by the factor <cite data-source="paper">multiplying the parameter by m increases the recursive contribution by s/W < m</cite>, so each recursive level saves a power.
