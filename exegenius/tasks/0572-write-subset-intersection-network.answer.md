A *subset-intersection network* is a fixed linear network that exchanges two banks of scalars, indexed by triples of a ground set, and returns every auxiliary wire to its starting value. It is the exchange step that [Integer multiplication below n log n](main-theorem.md) uses to swap its two data banks, and its wire labels control how cheaply the arrays it carries change representation.

## Triples, banks and vectors

Let $[h]=\{1,\dots,h\}$ be the ground set. Let $\mathcal T$ be the set of all three-element subsets of $[h]$, whose members are *triples*. The letters $S$ and $T$ always denote triples. A *bank* is a family of scalars indexed by $\sigma=(\sigma_1,\sigma_2,\sigma_3)\in\mathcal T^3$. The network has two banks $X$ and $Y$, with entries $X_\sigma$ and $Y_\sigma$.

A *gate* is a fixed linear map on some wires, and the other wires keep their values. A *scratch wire* has an arbitrary starting value, which the network must restore. The network is built within the framework of [Linear networks and frames](linear-network-frames.md): each wire is a role, and a common representation on the wires of a gate lets the gate act on arrays, pointwise. <cite data-source="paper">When the values are replaced by arrays, a common representation on all wires at a gate lets that gate act pointwise without disturbing the representation.</cite>

The network changes one coordinate of $\sigma$ at a time. <cite data-source="paper">At stage j, fix the other two coordinates and operate on the v values in each bank obtained by varying coordinate j.</cite> For each invocation write $\xi$ for the source vector and $\eta$ for the target vector, so that $\xi_T$ and $\eta_S$ are their entries. These letters change meaning here: on [Bilinear form](bilinear-form.md) they name vectors of a bilinear space. A *forward invocation* from $\xi$ to $\eta$ applies the gates below.

## Side wires, central wires and gates

Distinct triples are *neighbours* when they share exactly one element. <cite data-source="paper">S, T are neighbors when |S ∩ T | = 1.</cite> Each ordered neighbouring pair $(S,T)$ has a *side wire* $A_{ST}$, and each $\ell\in[h]$ has a *central wire* $C_\ell$. <cite data-source="paper">In the bit construction, scalars lie in F2</cite>, so signs vanish and addition is exclusive or.

The four gates are:

- *copy*: adds $\xi_T$ to $A_{ST}$ for each neighbouring pair $(S,T)$;
- *side injection*: adds $\sum_{T \text{ neighbour of } S} A_{ST}$ to $\eta_S$;
- *gather*: adds $\sum_{T\ni \ell}\xi_T$ to $C_\ell$, for each $\ell\in[h]$;
- *scatter*: adds $\sum_{\ell\in S}C_\ell$ to $\eta_S$.

A forward invocation applies these eight rows in order.

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

Rows 0 and 1 remove the starting scratch values. Rows 2 to 5 bring in the source values and add their effect to the target. Rows 6 and 7 restore the scratch wires. <cite data-source="paper">Each update leaves its control wires unchanged.</cite> Copy and gather write only scratch wires and read the unchanged $\xi$, so repeating either one cancels its effect over $\mathbb F_2$. That is why rows 6 and 7 undo rows 3 and 2.

## Why the scratch values cancel

Let $a$ and $c$ be the starting values of the side wires and central wires. Over $\mathbb F_2$, subtraction is addition. Rows 0 and 1 add the side injection of $a$ and the scatter of $c$ to $\eta$. Rows 2 and 3 change the side wires to $a$ plus copy and the central wires to $c$ plus gather. Rows 4 and 5 then add the scatter of the new central wires and the side injection of the new side wires to $\eta$. The terms in $a$ and $c$ each appear twice and cancel, and rows 6 and 7 restore them. So the net change to $\eta$ is "copy, then side injection" plus "gather, then scatter", whatever the scratch values were.

The coefficient of $\xi_T$ in $\eta_S$ has two routes. The central route contributes $|S\cap T|$ modulo 2. <cite data-source="paper">In the bit case, the central coefficient from xT to yS is |S ∩ T | mod 2.</cite> The side route contributes $1$ exactly when $T$ is a neighbour of $S$, that is, when $|S\cap T|=1$. Three cases cover every $T$:

- $T=S$: the central route gives $3 \bmod 2=1$ and the side route gives $0$, since $S$ is not its own neighbour. Total $1$.
- $|S\cap T|=1$: both routes give $1$. Total $0$.
- $|S\cap T|\in\{0,2\}$: both routes give $0$. Total $0$.

So $\eta_S\leftarrow\eta_S+\xi_S$ for every $S$, and no $\xi_T$ with $T\neq S$ reaches $\eta_S$. The side route is what <cite data-source="paper">cancels exactly the intersection-one cases;</cite>

For example, let $h=5$ and $S=\{1,2,3\}$. The triple $\{1,2,3\}$ has total $1$, the triple $\{1,4,5\}$ (one common element) has total $0$, and $\{1,2,4\}$ (two common elements) has total $0$.

## Exchanging the banks

<cite data-source="paper">For arbitrary initial values of its auxiliary wires, a forward invocation changes yS to</cite> <cite data-source="paper">yS + xS and leaves every other value unchanged.</cite> Over $\mathbb F_2$ this is $\eta\leftarrow\eta+\xi$. Each line of the banks then goes through three stages, with $\xi$ the $X$-entries and $\eta$ the $Y$-entries.

1. Stage 1, a forward invocation from $X$ to $Y$: $(\xi,\eta)\mapsto(\xi,\ \xi+\eta)$.
2. Stage 2, the inverse schedule from $Y$ to $X$: $(\xi,\ \xi+\eta)\mapsto(\eta,\ \xi+\eta)$, since $\xi+(\xi+\eta)=\eta$.
3. Stage 3, a forward invocation from $X$ to $Y$: $(\eta,\ \xi+\eta)\mapsto(\eta,\ \xi)$, since $(\xi+\eta)+\eta=\xi$.

The inverse schedule runs the rows in reverse order with the banks renamed. This is valid because each row writes only wires it does not read, so over $\mathbb F_2$ each row is its own inverse. <cite data-source="paper">The inverse schedule with logical source Y and target X effects X ← X − Y .</cite> The paper states the result, with signs, as <cite data-source="paper">(Xa , Ya ) 7−→ (−Ya , Xa )</cite>; over $\mathbb F_2$ the signs disappear, so the banks are swapped.

## Labels and their cost

Each wire carries an array, and changing an array's representation along an edge costs work. The network labels its wires with [subspace labels](subspace-labels.md): nondegenerate subspaces of a fixed bilinear space $E$. A subspace is *nondegenerate* when the form restricted to it has no nonzero vector orthogonal to all of it. <cite data-source="paper">On every edge one label will contain the other.</cite> <cite data-source="paper">Every edge joins comparable nondegenerate labels.</cite> For an edge with labels $U'\subseteq U$, the residual is <cite data-source="paper">the orthogonal complement of the smaller label inside the larger one</cite>, namely $U\cap U'^{\perp}$, and the cost of the edge is its dimension: <cite data-source="paper">its dimension is the absolute change in label dimension.</cite>

The residual has the expected dimension. If $U'$ is nondegenerate, then $U=U'\oplus(U\cap U'^{\perp})$ and $\dim(U\cap U'^{\perp})=\dim U-\dim U'$. Edge residuals are computed through the [dual space](dual-space.md) $U'^{*}$, the linear functionals on $U'$. The map $u\mapsto\langle u,\cdot\rangle|_{U'}$ sends $U$ onto $U'^{*}$, because nondegeneracy of $U'$ makes every functional on $U'$ of the form $\langle w,\cdot\rangle$ with $w\in U'\subseteq U$. Its kernel is $U\cap U'^{\perp}$, so rank-nullity gives the dimension. Also $U'\cap U'^{\perp}=\{0\}$, so the two pieces add up to $U$.

The total cost is the sum of residual dimensions over all edges, and it is small only if the decreasing edges lose little. <cite data-source="paper">The saving will come from keeping the total dimension lost on decreasing</cite> edges small. The decreasing edges are the central-wire edges, and <cite data-source="paper">central-wire edges from time 3 to time 4; their dimension loss is h.</cite>

## The bit construction's labels

For the bit network take $E=\mathbb Q^h$ with the form $\langle\mathbf p,\mathbf q\rangle=\mathbf p^{\mathsf T}(I-J/9)\mathbf q$, where $\mathbf p,\mathbf q$ are vectors of $E$ and $J$ is the all-ones matrix. The labels' orthogonality and nondegeneracy are tested with the [bilinear form](bilinear-form.md) of $E$. Let $t_T$ be the $0/1$ indicator vector of $T$. Then $t_S^{\mathsf T}t_T=|S\cap T|$ and $t_S^{\mathsf T}Jt_T=9$, so

$$\langle t_S,t_T\rangle=|S\cap T|-1.$$

Hence $\langle t_T,t_T\rangle=2\neq 0$, and neighbours satisfy $\langle t_S,t_T\rangle=0$.

Nondegeneracy is checked through the [eigenvalues](eigenvalue.md) of the form matrix $I-J/9$. The matrix $J$ has eigenvalue $h$ on the all-ones vector $\mathbf 1$ and $0$ on vectors whose entries sum to zero. So $I-J/9$ has eigenvalues $1$ and $1-h/9$. For $h=100$ the second is $-91/9\neq 0$, so the form is nondegenerate. <cite data-source="paper">This form has eigenvalues 1 and 1−h/9 = −91/9, so it is nondegenerate.</cite>

On a side wire joining neighbours $S$ and $T$, the smaller label is $\langle t_S\rangle$, and the larger is $t_T^{\perp}$. Since $\langle t_S,t_T\rangle=0$, we have $\langle t_S\rangle\subseteq t_T^{\perp}$, the nesting that the change of frame needs. <cite data-source="paper">The first inclusion is possible because tX ⊥ tY</cite>. Both labels are nondegenerate, and the residual $t_T^{\perp}\cap t_S^{\perp}$ has dimension $(h-1)-1=h-2$. <cite data-source="paper">Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal</cite>.

## The complex variant

The complex variant keeps the schedule and changes the scalars and the neighbour rule. <cite data-source="paper">In the complex construction, scalars lie in Z[i, 1/2], and neighbors are distinct triples with</cite> even intersection. Its central coefficient is $(|S\cap T|-1)/2$, which is meaningful only over these dyadic scalars. See the [complex construction](complex-construction.md) page.
