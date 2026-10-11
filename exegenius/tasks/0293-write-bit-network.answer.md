The bit network is the binary-field case of the [subset-intersection network](subset-intersection-network.md): a fixed linear network on the three-element subsets of a ground set that exchanges two banks of values and restores its scratch wires. It is the building block of the tape step that interchanges two equal address chunks: <cite data-source="paper">We use the bit network to interchange two equal address chunks on tape.</cite>

The bit network is a binary instance of [linear networks and frames](linear-network-frames.md): its wires carry scalars of $\mathbb F_2$, the field with two elements, 0 and 1, in which addition is exclusive or and multiplication is AND. <cite data-source="paper">A wire carries one scalar.</cite> The network <cite data-source="paper">uses only pointwise XOR gates</cite>, so each gate adds a fixed sum of bits into the wires it touches. Over $\mathbb F_2$ subtraction is the same operation as addition, so the signs in the paper's scalar identities disappear.

Let $[h]$ be the ground set and call its three-element subsets triples. Two triples $S$ and $T$ are *neighbours* when $|S\cap T|=1$; a triple is not its own neighbour. In one invocation the network has a source bank and a target bank, with one bit for each triple, and scratch wires that carry no information at the start: <cite data-source="paper">their initial values may be arbitrary</cite>, so the network must cancel whatever they hold.

Write $\chi$ for the source bank, a vector with one bit for each triple.
Write $\chi_T$ for the bit that the source bank holds at the triple $T$.
Write $\nu$ for the target bank, a vector with one bit for each triple.
Write $\nu_S$ for the bit that the target bank holds at the triple $S$.
For each ordered neighbouring pair $(S,T)$, write $\delta_{ST}$ for the side wire of that pair, a scratch wire.
For each element $e$ of $[h]$, write $C_e$ for the central wire of $e$, also a scratch wire.

There are four kinds of gate, each a sum over $\mathbb F_2$:

$$\delta_{ST} \leftarrow \delta_{ST} + \chi_T \qquad \text{(copy, for each neighbouring pair)}$$

$$\nu_S \leftarrow \nu_S + \sum_{T \text{ neighbours } S} \delta_{ST} \qquad \text{(side injection)}$$

$$C_e \leftarrow C_e + \sum_{T \ni e} \chi_T \qquad \text{(gather)}$$

$$\nu_S \leftarrow \nu_S + \sum_{e \in S} C_e \qquad \text{(scatter)}$$

The network applies these in eight rows: side injection, scatter, copy, gather, scatter, side injection, gather again, copy again. The first two rows add the initial scratch contents into the target bank, and rows 4 and 5 add them again. The two copies cancel because $1+1=0$ in $\mathbb F_2$, whatever the scratch wires held. Rows 2 and 3 move the source bits into the scratch wires, and rows 4 and 5 read them into the target bank. Rows 6 and 7 repeat the gather and copy, which restores the scratch wires because each of these sums is its own inverse over $\mathbb F_2$.

What is left is the contribution of the source bits. The bit $\chi_T$ reaches $\nu_S$ by two kinds of route: through $\delta_{ST}$ when $S$ and $T$ are neighbours, and through $C_e$ for each $e\in S\cap T$. Modulo 2 the total coefficient of $\chi_T$ in the change to $\nu_S$ is therefore $|S\cap T|$, plus one when $S$ and $T$ are neighbours. This is $0$ when $T\neq S$: in the neighbour case $|S\cap T|=1$ and the two routes cancel, and otherwise $|S\cap T|\in\{0,2\}$. When $T=S$ there are three central routes and the coefficient is $1$. So one invocation adds $\chi$ into $\nu$, that is $\nu_S \leftarrow \nu_S + \chi_S$ for every $S$, and leaves the scratch wires as they started.

For example, take $h=5$, $S=\{1,2,3\}$ and $T=\{1,4,5\}$. Then $|S\cap T|=1$, so $\chi_T$ reaches $\nu_S$ through $\delta_{ST}$ and through $C_1$, since $1\in S\cap T$. The two routes cancel. With $T=\{2,3,4\}$ instead, $|S\cap T|=2$, the routes go through $C_2$ and $C_3$, and they cancel. Only $T=S$ leaves an odd count.

The exchange needs three invocations, in the pattern forward, inverse, forward. Writing the two banks as $(\chi,\nu)$, the forward invocation gives $(\chi,\nu)\mapsto(\chi,\nu+\chi)$. The inverse invocation adds the target bank into the source bank, giving $(\chi,\nu+\chi)\mapsto(\nu,\nu+\chi)$. A final forward invocation gives $(\nu,\nu+\chi)\mapsto(\nu,\chi)$. Lemma 5 of the paper states the result: <cite data-source="paper">In the bit construction this is the permutation exchanging Xa</cite>, the exchange of the two banks, and the same invocations <cite data-source="paper">restores every auxiliary value</cite>. Scratch values may start arbitrary, yet the final permutation is exact: <cite data-source="paper">The final permutation is exact for arbitrary initial auxiliary values.</cite>

The bit network realises a [binary change of basis](binary-change-of-basis.md) on its wire values, since every gate is a composition of row additions, each of which adds the bit at one position into another position. The total effect on all wire values is an invertible linear map over $\mathbb F_2$: it exchanges the two banks and fixes the scratch wires.
