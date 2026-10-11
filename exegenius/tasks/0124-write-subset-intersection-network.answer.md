A *subset-intersection network* is a fixed linear network whose wires carry single scalars and whose gates combine them according to how much two three-element subsets overlap. It exchanges two banks of values while restoring every scratch wire. It is the finite exchange step on which the main result, [Integer multiplication below n log n](main-theorem.md), builds: the exchange is used to change the representation of data at small cost.

## Banks, wires and the two vectors

Fix $h$, the number of elements of the ground set $[h]=\{1,\dots,h\}$. A *triple* is a three-element subset of $[h]$, and $\mathcal K$ is the set of all triples. The letters $S$ and $T$ denote triples.

A *bank* is a family of scalars indexed by $\beta=(\beta_1,\beta_2,\beta_3)\in\mathcal K^3$. The network has two banks, $X$ and $Y$, with entries $x_\beta$ and $y_\beta$. On this page $x$ and $y$ do not mean the input strings of earlier pages: the letters change meaning here, and $X$ and $Y$ name banks.

Each wire carries one scalar. A gate is a fixed linear map on a chosen set of wires, and wires it does not touch keep their values. A *scratch wire* is an auxiliary wire whose initial value may be arbitrary, and the network must return it to that value.

The network changes one coordinate of $\beta$ at a time. Fix the other two coordinates. The entries of a bank along the varying coordinate then form a vector indexed by $\mathcal K$. Call these two vectors $\xi$ (the source) and $\eta$ (the target), so that $\xi_T$ is the source entry at triple $T$ and $\eta_S$ is the target entry at triple $S$.

## The bit construction

All arithmetic is mod 2: the scalars lie in the binary field $\mathbb F_2=\{0,1\}$, where $-1=1$, so signs vanish. Distinct triples $S$ and $T$ are *neighbours* when they share exactly one element: <cite data-source="paper">S, T are neighbors when |S ∩ T | = 1.</cite>

For each ordered neighbouring pair $(S,T)$ there is a side wire $W_{ST}$. For each element $\ell\in[h]$ there is a central wire $C_\ell$. Four gates act on these wires:

- copy: adds $\xi_T$ to $W_{ST}$ for each neighbouring pair $(S,T)$;
- side injection: adds $\sum_{T\text{ neighbour of }S} W_{ST}$ to $\eta_S$;
- gather: adds $\sum_{T\ni \ell}\xi_T$ to $C_\ell$ for each $\ell\in[h]$;
- scatter: adds $\sum_{\ell\in S}C_\ell$ to $\eta_S$.

A *forward invocation* from $\xi$ to $\eta$ runs the following eight rows in order. Each row is one gate on the wires named in its grouping.

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

Rows 0 and 1 remove the effect of whatever the scratch wires already hold: <cite data-source="paper">the effect of the old scratch values; the next four introduce the source values and add their effect</cite> Rows 2 to 5 load the source values and add their effect to the target, and rows 6 and 7 restore the scratch wires. The net change to the target is the sum of two routes, copy then side injection and gather then scatter, and it does not depend on the scratch values.

**Worked check.** Take $h\ge 5$ and $S=\{1,2,3\}$, and find the coefficient of each $\xi_T$ in the final $\eta_S$. The gather-then-scatter route contributes $|S\cap T| \bmod 2$, because each shared element is counted once. The side route contributes $1$ exactly when $T$ is a neighbour of $S$. Three cases cover all $T$:

- $T=S$: the central route gives $|S\cap S| \bmod 2=1$, and $S$ is not its own neighbour, so the coefficient is $1$.
- $T=\{1,4,5\}$, so $|S\cap T|=1$: the central route gives $1$ and the side route gives $1$, so the total is $1+1=0$.
- $|S\cap T|\in\{0,2\}$: the central route gives $0$, and $T$ is not a neighbour, so the total is $0$.

So the net change is $\eta_S\leftarrow\eta_S+\xi_S$, and every other entry of $\eta$ is unchanged. The side wires exist to cancel the intersection-one terms: <cite data-source="paper">cancels exactly the intersection-one cases; distinct triples with intersection zero or two already</cite>

## Exchanging the banks

Over $\mathbb F_2$ a forward invocation adds its source into its target, and the inverse schedule, with source $Y$ and target $X$, adds $Y$ into $X$. The construction runs three stages, one per coordinate of $\beta$, each on the vectors of one line with the other coordinates fixed. On one line, with $\xi$ the $X$-entries and $\eta$ the $Y$-entries, the stages act as follows:

1. Stage 1, a forward invocation from $X$ to $Y$: $(\xi,\eta)\mapsto(\xi,\ \xi+\eta)$.
2. Stage 2, the inverse schedule from $Y$ to $X$: $(\xi,\ \xi+\eta)\mapsto(\eta,\ \xi+\eta)$, since $\xi+(\xi+\eta)=\eta$.
3. Stage 3, a forward invocation from $X$ to $Y$: $(\eta,\ \xi+\eta)\mapsto(\eta,\ \xi)$, since $(\xi+\eta)+\eta=\xi$.

The paper states the outcome over the integers with signs, as <cite data-source="paper">(Xa , Ya ) 7−→ (−Ya , Xa )</cite> and every auxiliary wire restored. Over $\mathbb F_2$ the signs disappear, so the three invocations exchange the two banks on every line.

## Labels and the cost of a change of representation

The sources do not define the cost of a change of representation. The reading used here is the one the paper's count implies: <cite data-source="paper">count the smaller operations needed on an edge, with an additional source contribution in the bit</cite> so the cost on an edge is governed by its dimension change.

Each gate and terminal is labelled by [Subspace labels](subspace-labels.md): a nondegenerate subspace of a fixed bilinear space. Nondegenerate means the form restricts to a nonsingular form on the subspace, so the whole space splits as the subspace plus its orthogonal complement. <cite data-source="paper">On every edge one label will contain the other.</cite> The orthogonal residual of an edge is the part of the larger label orthogonal to the smaller one, and its dimension is the absolute change in label dimension. <cite data-source="paper">Every edge joins comparable nondegenerate labels.</cite> The paper's only decreasing edges are <cite data-source="paper">central-wire edges from time 3 to time 4; their dimension loss is h.</cite>

Orthogonality and nondegeneracy are tested with the form of [Bilinear form](bilinear-form.md). For the bit network take $\mathbb Q^h$ with the form $\langle x,y\rangle=x^{\mathsf T}(I-J/9)y$, where $I$ is the $h\times h$ identity matrix and $J$ is the all-one matrix. Let $t_T$ be the $0/1$ indicator vector of $T$. Since $t_S^{\mathsf T}t_T=|S\cap T|$ and $t_S^{\mathsf T}Jt_T=9$,

$$\langle t_S,t_T\rangle=|S\cap T|-1,$$

so $\langle t_T,t_T\rangle=2$, and two neighbours $S,T$ satisfy $\langle t_S,t_T\rangle=0$. The paper takes $h=100$, and then $J$ has eigenvalues $h$ and $0$, so the form has eigenvalues $1$ and $1-h/9$. <cite data-source="paper">This form has eigenvalues 1 and 1−h/9 = −91/9, so it is nondegenerate.</cite> Hence <cite data-source="paper">Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label</cite> field of the bit network.

The orthogonality of neighbours is what makes the nesting work. On a side wire joining neighbours $X$ and $Y$, the paper needs the line $\langle t_X\rangle$ to sit inside $t_Y^{\perp}$, and <cite data-source="paper">The first inclusion is possible because tX ⊥ tY .</cite> The gate labels are tensor products built from these lines, and the paper's Lemma 6 checks every edge; this page does not reproduce that table.

The complex variant keeps the same schedule and changes the scalars and the neighbour rule: <cite data-source="paper">In the complex construction, scalars lie in Z[i, 1/2], and neighbors are distinct triples with</cite> even intersection.

The network is built within the framework of [Linear networks and frames](linear-network-frames.md): every wire is a role and every gate carries a frame, so the same scalar gates can act on arrays.
