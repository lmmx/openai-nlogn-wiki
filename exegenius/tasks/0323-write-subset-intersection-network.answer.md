A *subset-intersection network* is a fixed linear network that exchanges two families of scalars, indexed by triples of a ground set, and returns every auxiliary wire to its starting value. It is the exchange step on which [Integer multiplication below n log n](main-theorem.md) builds.

## Banks, wires and the two vectors

Fix $h$, the number of elements of the ground set $[h]=\{1,\dots,h\}$. A *triple* is a three-element subset of $[h]$, and $\mathcal T$ denotes the set of all triples.

A *bank* is a family of scalars indexed by $\tau=(\tau_1,\tau_2,\tau_3)\in\mathcal T^3$. The network has two banks, $X$ and $Y$, with entries $X_\tau$ and $Y_\tau$. These letters change meaning here.

Each wire carries one scalar. A *gate* is a fixed linear map on some wires, and untouched wires keep their values. A *scratch wire* is an auxiliary wire whose starting value may be arbitrary; the network must return it to that value.

The network changes one coordinate of $\tau$ at a time. Fix the other two. The entries of a bank along the varying coordinate form a vector indexed by $\mathcal T$. Call these two vectors $\xi$ (the source) and $\eta$ (the target), so that $\xi_T$ and $\eta_S$ are their entries. These letters change meaning here.

## The bit construction

The scalars lie in the [binary field](binary-field.md) $\mathbb F_2=\{0,1\}$, where $-1=1$, so signs vanish. Two distinct triples are *neighbours* when they share exactly one element. The source gives the rule as <cite data-source="paper">S, T are neighbors when |S ∩ T | = 1.</cite>

For each ordered neighbouring pair $(S,T)$ there is a side wire $W_{ST}$. For each $\ell\in[h]$ there is a central wire $C_\ell$, where $\ell$ is an element of $[h]$ here. Four gates act on these wires:

- copy: adds $\xi_T$ to $W_{ST}$ for each neighbouring pair $(S,T)$;
- side injection: adds $\sum_{T\text{ neighbour of }S} W_{ST}$ to $\eta_S$;
- gather: adds $\sum_{T\ni \ell}\xi_T$ to $C_\ell$ for each $\ell\in[h]$;
- scatter: adds $\sum_{\ell\in S}C_\ell$ to $\eta_S$.

A *forward invocation* from $\xi$ to $\eta$ applies these gates in the eight rows below, in order.

| row | gate |
|---|---|
| 0 | subtract side injection |
| 1 | subtract scatter |
| 2 | copy |
| 3 | gather |
| 4 | scatter |
| 5 | side injection |
| 6 | undo gather |
| 7 | undo copy |

Rows 0 and 1 cancel the contribution of the starting scratch values. The source describes the rest: <cite data-source="paper">the next four introduce the source values and add their effect</cite> to the target, and <cite data-source="paper">the last two restore the scratch values</cite>. Rows 6 and 7 undo rows 3 and 2, so the scratch wires end where they began. The net change to the target is the sum of two routes, copy then side injection and gather then scatter, independent of the starting scratch values.

**Worked check.** Take $h\ge 5$ and $S=\{1,2,3\}$, and find the coefficient of $\xi_T$ in $\eta_S$. The gather-then-scatter route gives $|S\cap T| \bmod 2$, since each shared element is counted once: <cite data-source="paper">In the bit case, the central coefficient from xT to yS is |S ∩ T | mod 2.</cite> The side route gives $1$ exactly when $T$ is a neighbour of $S$. Three cases cover all $T$:

- $T=S$: the central route gives $1$ and the side route $0$, since $S$ is not its own neighbour: total $1$.
- $|S\cap T|=1$: both routes give $1$, total $0$.
- $|S\cap T|\in\{0,2\}$: both routes give $0$, total $0$.

So $\eta_S\leftarrow\eta_S+\xi_S$, and every other entry of $\eta$ is unchanged. The side route cancels the intersection-one terms: <cite data-source="paper">cancels exactly the intersection-one cases; distinct triples with intersection zero or two already</cite> have coefficient zero.

## Exchanging the banks

The source's Lemma 5 gives the net effect of one forward invocation, whatever the scratch wires held: <cite data-source="paper">yS + xS and leaves every other value unchanged.</cite> Over $\mathbb F_2$ this adds the source into the target.

The exchange also needs the inverse, which runs the rows in reverse order, each inverted. The source states this for the middle stage: <cite data-source="paper">At stage 2 it uses the inverse of row 7 − r, with the logical banks</cite> exchanged, and <cite data-source="paper">The inverse schedule with logical source Y and target X effects X ← X − Y .</cite> Over $\mathbb F_2$ this adds $Y$ into $X$.

The exchange has three stages. On one line, with $\xi$ the $X$-entries and $\eta$ the $Y$-entries:

1. Stage 1, a forward invocation from $X$ to $Y$: $(\xi,\eta)\mapsto(\xi,\ \xi+\eta)$.
2. Stage 2, the inverse schedule from $Y$ to $X$: $(\xi,\ \xi+\eta)\mapsto(\eta,\ \xi+\eta)$, since $\xi+(\xi+\eta)=\eta$.
3. Stage 3, a forward invocation from $X$ to $Y$: $(\eta,\ \xi+\eta)\mapsto(\eta,\ \xi)$, since $(\xi+\eta)+\eta=\xi$.

With signs, the source states <cite data-source="paper">(Xa , Ya ) 7−→ (−Ya , Xa )</cite>, restoring every auxiliary wire. Over $\mathbb F_2$ the signs disappear, so the banks are swapped on every line.

## Labels and the cost of a change of representation

The network is built within the framework of [Linear networks and frames](linear-network-frames.md): each wire is a role, and each gate carries a frame, so the same scalar gates can act on arrays. The network labels its gates and terminals with [Subspace labels](subspace-labels.md): nondegenerate subspaces of a fixed bilinear space $E$. A subspace $U$ is *nondegenerate* when $U\cap U^\perp=\{0\}$, where $U^\perp$ is the set of vectors of $E$ orthogonal to every vector of $U$.

<cite data-source="paper">On every edge one label will contain the other.</cite> Write $U'$ for the larger label of an edge and $U$ for the smaller. The residual of the edge is <cite data-source="paper">the orthogonal complement of the smaller label inside the larger one</cite>, namely $U'\cap U^\perp$. Its dimension is $\dim U'-\dim U$: since $U'$ is nondegenerate, the form identifies $U'$ with its dual, so restriction $U'\to U^*$ is onto with kernel $U'\cap U^\perp$. Also $U\cap U^\perp=\{0\}$ by nondegeneracy of $U$, so $U'=U\oplus(U'\cap U^\perp)$.

The source counts an edge's cost as <cite data-source="paper">count the smaller operations needed on an edge, with an additional source contribution in the bit</cite> construction. This page reads the cost of an edge as its dimension change, so the total cost is their sum. The construction needs the loss on decreasing edges to stay small: <cite data-source="paper">The saving will come from keeping the total dimension lost on decreasing</cite> edges.

The source's Lemma 6 checks every edge: <cite data-source="paper">Every edge joins comparable nondegenerate labels.</cite> The only dimension loss is on <cite data-source="paper">central-wire edges from time 3 to time 4; their dimension loss is h.</cite> At stages 1 and 3 time is the row number, so on a central wire $C_\ell$ the decreasing edge joins gather (time 3) to scatter (time 4).

The nesting that the change of frame needs follows from orthogonality, a step the sources leave to the reader. On a side wire joining neighbours $S$ and $T$, the smaller label $\langle t_S\rangle$ must sit inside $t_T^\perp$, the orthogonal complement of the indicator vector $t_T$ of $T$. It does, because $\langle t_S,t_T\rangle=0$ (shown below): every multiple $\lambda t_S$ satisfies $\langle\lambda t_S,t_T\rangle=0$, so $\langle t_S\rangle\subseteq t_T^\perp$. The source states it as <cite data-source="paper">The first inclusion is possible because tX ⊥ tY</cite>. The residual $\langle t_S,t_T\rangle^\perp$ then has dimension $h-2$, since $t_T^\perp$ has dimension $h-1$.

## The bit network's form

For the bit network take $E=\mathbb Q^h$ with the form $\langle\delta,\delta'\rangle=\delta^{\mathsf T}(I-J/9)\delta'$, where $\delta,\delta'$ are vectors of $E$, $I$ is the identity matrix and $J$ the all-ones matrix. Orthogonality and nondegeneracy are tested with the form of [Bilinear form](bilinear-form.md). Let $t_T$ be the $0/1$ indicator vector of $T$, which has three entries equal to $1$. Since $t_S^{\mathsf T}t_T=|S\cap T|$ and $t_S^{\mathsf T}Jt_T=3\cdot 3=9$,
$$\langle t_S,t_T\rangle=|S\cap T|-1.$$
So $\langle t_T,t_T\rangle=2\neq 0$, and two neighbours satisfy $\langle t_S,t_T\rangle=0$.

The network checks nondegeneracy through [Eigenvalue](eigenvalue.md)s of its form matrix $I-J/9$. The matrix $J$ has eigenvalue $h$ on the all-ones vector and $0$ on every vector whose entries sum to zero, so $I-J/9$ has eigenvalues $1$ and $1-h/9$. The source uses <cite data-source="paper">with the ground-set size changed to h = 100</cite>, and <cite data-source="paper">This form has eigenvalues 1 and 1−h/9 = −91/9, so it is nondegenerate.</cite> No zero eigenvalue means no nonzero vector of $E$ is orthogonal to all of $E$. Hence every triple line $\langle t_T\rangle$ is a nondegenerate label, and <cite data-source="paper">Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal</cite>.

## The complex variant

The complex construction keeps the schedule and changes the scalars and the neighbour rule. <cite data-source="paper">In the complex construction, scalars lie in Z[i, 1/2], and neighbors are distinct triples with</cite> even intersection, that is, $|S\cap T|\in\{0,2\}$. Its central coefficient is <cite data-source="paper">In the complex case, the central coefficient is</cite> $(|S\cap T|-1)/2$, which the side wires cancel on distinct triples with intersection zero or two. Its label space $\mathbb F_2^h$ with the dot product also makes neighbouring triple lines orthogonal.
