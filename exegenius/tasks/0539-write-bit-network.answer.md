The bit network is a fixed linear network whose wires carry bits. It exchanges two banks of bits and leaves its scratch wires as they started. It is the building block of the tape step that interchanges two equal address chunks: <cite data-source="paper">We use the bit network to interchange two equal address chunks on tape.</cite>

An address is a bit string, and an address chunk is a block of adjacent address bits. The paper's first tape procedure interchanges two blocks of $u$ bits, the fields of the address: <cite data-source="paper">The first procedure interchanges two disjoint contiguous address fields of u bits</cite>, so each entry moves to the address with its two fields swapped.

The bit network is a binary instance of [linear networks and frames](linear-network-frames.md), since its wires carry scalars of $\mathbb{F}_2$, the field with two elements in which addition is exclusive or and multiplication is AND. <cite data-source="paper">A wire carries one scalar.</cite> It <cite data-source="paper">uses only pointwise XOR gates</cite>, so each gate replaces the bits on some wires by sums of bits on other wires. Over $\mathbb{F}_2$ subtraction is the same as addition, so the signs in the paper's general construction disappear.

Let $T$ be the set of three-element subsets of $[h]$, and let $\sigma$ and $\sigma'$ denote elements of $T$, which we call triples. Two triples are neighbours when $|\sigma\cap\sigma'|=1$. A triple is not its own neighbour, since it meets itself in three elements. The network has these wires:

- The source bank $W$ holds one bit $W_\sigma$ for each triple $\sigma$, and the target bank $Y$ holds one bit $Y_\sigma$ for each triple $\sigma$.
- For each ordered neighbouring pair $(\sigma,\sigma')$ there is a side wire $\zeta_{\sigma\sigma'}$.
- For each element $\upsilon$ of $[h]$ there is a central wire $J_\upsilon$.

The side and central wires are scratch wires. <cite data-source="paper">their initial values may be arbitrary</cite>, so the network must cancel whatever they hold. There are four kinds of gate, each a sum over $\mathbb{F}_2$:

$$\zeta_{\sigma\sigma'} \leftarrow \zeta_{\sigma\sigma'} + W_{\sigma'} \qquad \text{(copy)}$$

$$Y_\sigma \leftarrow Y_\sigma + \sum_{\sigma' \text{ neighbour of } \sigma} \zeta_{\sigma\sigma'} \qquad \text{(side injection)}$$

$$J_\upsilon \leftarrow J_\upsilon + \sum_{\sigma' \ni \upsilon} W_{\sigma'} \qquad \text{(gather)}$$

$$Y_\sigma \leftarrow Y_\sigma + \sum_{\upsilon \in \sigma} J_\upsilon \qquad \text{(scatter)}$$

A forward invocation runs eight rows, numbered 0 to 7: side injection, scatter, copy, gather, scatter, side injection, gather, copy. Rows 0 and 1 add the initial side and central values into $Y$. Rows 2 and 3 load the source bits into the scratch wires. Rows 4 and 5 add the loaded scratch values into $Y$. Rows 6 and 7 apply the gather and copy again. Since no row changes $W$, these two rows undo rows 3 and 2, and each scratch wire returns to its starting value.

The initial scratch values enter $Y$ in rows 0 and 1 and again in rows 4 and 5. The two copies cancel because $1+1=0$ in $\mathbb{F}_2$, whatever the scratch wires held. What remains is the contribution of $W$. The bit $W_{\sigma'}$ reaches $Y_\sigma$ through the side wire $\zeta_{\sigma\sigma'}$ when $\sigma'$ is a neighbour of $\sigma$, and through $J_\upsilon$ for each $\upsilon\in\sigma\cap\sigma'$. The paper's count reads: <cite data-source="paper">In the bit case, the central coefficient from xT to yS is |S ∩ T | mod 2.</cite> Here $S$ is $\sigma$ and $T$ is $\sigma'$. Adding the side route, the coefficient of $W_{\sigma'}$ in the change to $Y_\sigma$ is $|\sigma\cap\sigma'|$ plus one if $\sigma'$ is a neighbour, taken mod 2. This is $0$ when $\sigma'\neq\sigma$: for neighbours $|\sigma\cap\sigma'|=1$ and the two routes give $1+1=0$, and otherwise $|\sigma\cap\sigma'|\in\{0,2\}$. When $\sigma'=\sigma$ the three central routes give $3\equiv 1$. So a forward invocation sets $Y_\sigma\leftarrow Y_\sigma+W_\sigma$ for every triple. The paper states this as <cite data-source="paper">a forward invocation changes yS to yS + xS and leaves every other value unchanged.</cite>

For example, take $h=5$, $\sigma=\{1,2,3\}$ and $\sigma'=\{1,4,5\}$. Then $|\sigma\cap\sigma'|=1$, so $W_{\sigma'}$ reaches $Y_\sigma$ through $\zeta_{\sigma\sigma'}$ and through $J_1$, and the two routes cancel. For $\sigma'=\{2,3,4\}$ there is no side route, since $|\sigma\cap\sigma'|=2$. The central routes through $J_2$ and $J_3$ give $1+1=0$. Only $\sigma'=\sigma$ leaves an odd count.

The exchange uses three invocations: forward, inverse, forward. The inverse is the same eight-row schedule with the roles of the banks swapped, so its gates read $Y$ and update $W$. Over $\mathbb{F}_2$ it sets $W\leftarrow W+Y$; the paper writes <cite data-source="paper">The inverse schedule with logical source Y and target X effects X ← X − Y</cite>. Starting from $(W,Y)$, the three invocations give $(W,Y+W)$, then $(Y,Y+W)$, then $(Y,W)$. In the second step $W\leftarrow W+(Y+W)=Y$. In the third $Y\leftarrow(Y+W)+Y=W$. So the banks are exchanged and the scratch wires are unchanged. Lemma 5 of the paper, in *Integer multiplication below n log n* (OpenAI, 2026), states this result: <cite data-source="paper">In the bit construction this is the permutation exchanging Xa</cite> and $Y$, and the same invocations <cite data-source="paper">restores every auxiliary value.</cite> Because the scratch values may start arbitrary, the exchange must hold for any of them: <cite data-source="paper">The final permutation is exact for arbitrary initial auxiliary values.</cite>

On tape, binary changes of basis are carried out by moving whole address chunks: <cite data-source="paper">We implement those changes by moving whole address chunks.</cite> The bit network performs the chunk interchanges that implement a [binary change of basis](binary-change-of-basis.md) on tape.
