The bit network is a fixed linear network whose wires carry bits. It exchanges two banks of bits and leaves its scratch wires as they started. It is the building block of the tape step that interchanges two equal address chunks.

An address is a bit string, and an address chunk is a block of adjacent address bits. The paper's first tape procedure interchanges two blocks of $u$ bits, the fields of the address: <cite data-source="paper">The first procedure interchanges two disjoint contiguous address fields of u bits</cite>, so each entry moves to the address with its two fields swapped. The bit network is the building block of the tape step for equal chunks: <cite data-source="paper">We use the bit network to interchange two equal address chunks on tape.</cite>

The bit network is a binary instance of [linear networks and frames](linear-network-frames.md), since its wires carry scalars of $\mathbb{F}_2$, the field with two elements in which addition is exclusive or and multiplication is AND. <cite data-source="paper">A wire carries one scalar.</cite> A gate is a fixed linear map on some of the wires. A pointwise gate applies the same sum at every address. The paper's Proposition 7 states that the bit network <cite data-source="paper">uses only pointwise XOR gates</cite>, so each gate replaces the bits on some wires by sums of bits on other wires. Over $\mathbb{F}_2$ subtraction is addition, so the paper's signs disappear.

Let $\mathcal T$ be the set of three-element subsets of $[h]$, and let $\Delta$ and $\Delta'$ denote elements of $\mathcal T$, which we call triples. Two triples are neighbours when $|\Delta\cap\Delta'|=1$. A triple is not its own neighbour. A bank is a family of bits indexed by triples. The network has these wires:

- The source bank $\Xi$ holds one bit $\Xi_\Delta$ for each triple $\Delta$, and the target bank $Y$ holds one bit $Y_\Delta$ for each triple $\Delta$.
- For each ordered neighbouring pair $(\Delta,\Delta')$ there is a side wire $\zeta_{\Delta\Delta'}$.
- For each element $\upsilon$ of $[h]$ there is a central wire $J_\upsilon$.

The side and central wires are scratch wires, and <cite data-source="paper">their initial values may be arbitrary</cite>, so the network must cancel whatever they hold. Each gate adds a sum of wires over $\mathbb{F}_2$ to the wire on its left. There are four kinds:

$$\zeta_{\Delta\Delta'} \leftarrow \zeta_{\Delta\Delta'} + \Xi_{\Delta'} \qquad \text{(copy)}$$

$$Y_\Delta \leftarrow Y_\Delta + \sum_{\Delta' \text{ neighbour of } \Delta} \zeta_{\Delta\Delta'} \qquad \text{(side injection)}$$

$$J_\upsilon \leftarrow J_\upsilon + \sum_{\Delta' \ni \upsilon} \Xi_{\Delta'} \qquad \text{(gather)}$$

$$Y_\Delta \leftarrow Y_\Delta + \sum_{\upsilon \in \Delta} J_\upsilon \qquad \text{(scatter)}$$

A forward invocation runs eight rows, numbered 0 to 7: side injection, scatter, copy, gather, scatter, side injection, gather, copy. Rows 0 and 1 add the initial side and central values into $Y$. Rows 2 and 3 load the source bits into the scratch wires. Rows 4 and 5 add the loaded scratch values into $Y$. Rows 6 and 7 apply the gather and copy again. No row changes $\Xi$, so rows 6 and 7 undo rows 3 and 2, and each scratch wire returns to its starting value.

The initial scratch values enter $Y$ twice, in rows 0 and 1 and again in rows 4 and 5. The two copies cancel because $1+1=0$ in $\mathbb{F}_2$, whatever the scratch wires held. What remains is the contribution of $\Xi$. The bit $\Xi_{\Delta'}$ reaches $Y_\Delta$ through the side wire $\zeta_{\Delta\Delta'}$ when $\Delta'$ is a neighbour of $\Delta$, and through $J_\upsilon$ for each $\upsilon\in\Delta\cap\Delta'$. The paper's count, where its $S$ and $T$ are $\Delta$ and $\Delta'$ and its $x$ and $y$ are $\Xi$ and $Y$, reads: <cite data-source="paper">In the bit case, the central coefficient from xT to yS is |S ∩ T | mod 2.</cite> The side route adds one more path exactly when $\Delta'$ is a neighbour. For neighbours the two routes give $1+1=0$. Otherwise $|\Delta\cap\Delta'|\in\{0,2\}$ and the central routes already give $0$. When $\Delta'=\Delta$ the three central routes give $3\equiv 1$. So a forward invocation changes $Y_\Delta$ to $Y_\Delta+\Xi_\Delta$ for every triple, and the paper states this as <cite data-source="paper">a forward invocation changes yS to yS + xS and leaves every other value unchanged.</cite>

For example, take $h=5$, $\Delta=\{1,2,3\}$ and $\Delta'=\{1,4,5\}$. Then $|\Delta\cap\Delta'|=1$, so $\Xi_{\Delta'}$ reaches $Y_\Delta$ through $\zeta_{\Delta\Delta'}$ and through $J_1$, and the two routes cancel. For $\Delta'=\{2,3,4\}$ there is no side route, since $|\Delta\cap\Delta'|=2$, and the central routes through $J_2$ and $J_3$ give $1+1=0$. Only $\Delta'=\Delta$ leaves an odd count.

The exchange uses three invocations: forward, inverse, forward. The inverse is the same eight-row schedule with the roles of the banks swapped, so its gates read $Y$ and update $\Xi$. Over $\mathbb{F}_2$ it sets $\Xi\leftarrow\Xi+Y$. The paper writes this as <cite data-source="paper">The inverse schedule with logical source Y and target X effects X ← X − Y</cite>, where its $X$ is $\Xi$. Starting from $(\Xi,Y)$, the three invocations give $(\Xi,Y+\Xi)$, then $(Y,Y+\Xi)$, then $(Y,\Xi)$. In the second step $\Xi\leftarrow\Xi+(Y+\Xi)=Y$, and in the third $Y\leftarrow(Y+\Xi)+Y=\Xi$. So the two banks are exchanged. Lemma 5 of the paper states the result for its banks $X_a$ and $Y_a$: <cite data-source="paper">In the bit construction this is the permutation exchanging Xa and Ya</cite>. The same schedule also <cite data-source="paper">restores every auxiliary value.</cite> Because the scratch values may start arbitrary, the exchange must hold for any of them: <cite data-source="paper">The final permutation is exact for arbitrary initial auxiliary values.</cite>

On tape, binary changes of basis are carried out by moving whole address chunks: <cite data-source="paper">We implement those changes by moving whole address chunks.</cite> The bit network realises a [binary change of basis](binary-change-of-basis.md) on tape by interchanging equal address chunks.
