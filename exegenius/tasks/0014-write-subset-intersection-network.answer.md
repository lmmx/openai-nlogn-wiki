A subset-intersection network is a fixed linear network whose wires carry single scalars and whose gates combine them according to how much two three-element subsets overlap. It exchanges two banks of values while restoring every scratch wire, and this exchange is the finite step on which the main result, [Integer multiplication below n log n](main-theorem.md), builds.

Fix $h$, the number of elements in the ground set $[h]=\{1,\dots,h\}$. A *triple* is a three-element subset of $[h]$, and $\mathcal{K}$ is the set of all triples. A *bank* is a family of values indexed by $a=(a_1,a_2,a_3)\in\mathcal{K}^3$; the two banks are $X$ and $Y$, with entries $x_a$ and $y_a$.

Each wire carries one scalar. A gate is a fixed linear map on a chosen set of wires, and wires it does not touch keep their values. A *scratch wire* is an auxiliary wire whose initial value may be arbitrary; the network must return every scratch wire to the value it started with.

For a triple $T$, its indicator vector $t_T$ is the $0/1$ vector on $[h]$ with a $1$ in the coordinate of each element $i$ of $T$ and $0$ elsewhere. Two distinct triples $S$ and $T$ are *neighbours* when they share exactly one element. In the bit construction the source uses this definition: <cite data-source="paper">and S, T are neighbors when |S ∩ T | = 1.</cite>

**The bit construction.** All arithmetic is mod 2. For each ordered neighbouring pair $(S,T)$ there is a side wire $A_{ST}$, and for each element $i\in[h]$ there is a central wire $C_i$. Four gates act on the wires:

- copy: adds $x_T$ to $A_{ST}$ for each neighbouring pair $(S,T)$;
- side injection: adds $\sum_{T \text{ neighbour of } S} A_{ST}$ to $y_S$;
- gather: adds $\sum_{T\ni i} x_T$ to $C_i$ for each $i\in[h]$;
- scatter: adds $\sum_{i\in S} C_i$ to $y_S$.

A *forward invocation* from $X$ to $Y$ runs the following eight rows in order. Each row is one gate, applied to the wires named in its grouping.

| row | operation | gate grouping |
|---|---|---|
| 0 | subtract side injection | one gate per target |
| 1 | subtract scatter | one gate on targets and centre |
| 2 | copy | one gate per source |
| 3 | gather | one gate on sources and centre |
| 4 | scatter | one gate on targets and centre |
| 5 | side injection | one gate per target |
| 6 | undo gather | one gate on sources and centre |
| 7 | undo copy | one gate per source |

Rows 0 and 1 subtract whatever the scratch wires already hold, so the arbitrary starting values cancel. Rows 2 to 5 load the source values and add their effect to the target, and rows 6 and 7 restore the scratch wires. <cite data-source="paper">the effect of the old scratch values; the next four introduce the source values and add their effect</cite>

**Worked check.** Take $h\ge 5$, $S=\{1,2,3\}$, and look at the coefficient of each $x_T$ in the final $y_S$. The central route (gather then scatter) contributes $|S\cap T| \bmod 2$ to that coefficient, because each shared element is counted once. The side route contributes $1$ exactly when $T$ is a neighbour of $S$. Three cases cover all $T$:

- $T=S$: the central route gives $|S\cap S| \bmod 2 = 1$, and $S$ is not its own neighbour, so the coefficient is $1$.
- $T=\{1,4,5\}$, so $|S\cap T|=1$: the central route gives $1$ and the side route gives $1$, so the total is $1+1=0$.
- $|S\cap T|\in\{0,2\}$: the central route gives $0$, and $T$ is not a neighbour, so the total is $0$.

So the net change is $y_S\leftarrow y_S+x_S$, and every other $y$ value is unchanged, whatever the scratch wires held at the start. The side wires exist to cancel the intersection-one terms. <cite data-source="paper">cancels exactly the intersection-one cases; distinct triples with intersection zero or two already</cite>

**Exchanging the banks.** Using the forward invocation, the construction runs three stages, one per coordinate of $a$, with the other coordinates fixed. Over $\mathbb{F}_2$ signs disappear, and the three-invocation sequence from $X$ to $Y$, from $Y$ to $X$, and from $X$ to $Y$ takes $(x,y)$ to $(x,\,x+y)$, then $(y,\,x+y)$, then $(y,\,x)$. The paper states the outcome as <cite data-source="paper">In the bit construction this is the permutation exchanging Xa</cite> and Ya, with every auxiliary wire restored.

**Why the wires carry subspaces.** A subspace labelled on a gate tells the network how much work a change of representation costs. Each gate is labelled by [Subspace labels](subspace-labels.md): a nondegenerate subspace of a fixed bilinear space, meaning one on which the form restricts to a nonsingular form, so that the whole space splits as the subspace plus its orthogonal complement. On every edge one label contains the other, and the change in dimension between them is the dimension of the orthogonal residual, the part of the larger label orthogonal to the smaller one. <cite data-source="paper">count the smaller operations needed on an edge, with an additional source contribution in the bit</cite>, so keeping the dimension change small keeps the cost small.

The labels are chosen from the indicator vectors. Each indicator line $\langle t_T\rangle$ is nondegenerate, so it splits off its complement cleanly. Neighbouring lines are orthogonal to each other, so the line of a neighbour lies inside the complement of $t_T$ and can be split from it without disturbing the rest of the label. Hence moving from one triple's label to a neighbour's changes the label by one nondegenerate piece, and the orthogonality of neighbours is what makes the nesting work. <cite data-source="paper">Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label</cite> <cite data-source="paper">of the corresponding indicator vectors permits the subspace assignments.</cite>

The complex variant uses the same schedule with the scalars and neighbour rule changed: <cite data-source="paper">In the complex construction, scalars lie in Z[i, 1/2], and neighbors are distinct triples with</cite> even intersection.

The network is built within the framework of [Linear networks and frames](linear-network-frames.md): every wire is a role and every gate carries a frame, so the same scalar gates can act on arrays.
