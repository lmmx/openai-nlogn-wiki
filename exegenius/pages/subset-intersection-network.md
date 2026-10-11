A *subset-intersection network* is a fixed linear network that exchanges two banks of scalars indexed by triples of a ground set, and restores every auxiliary wire to its starting value. It is the exchange step that [Integer multiplication below n log n](main-theorem.md) uses to swap its two data banks, and its wire labels control how cheaply the arrays it carries change representation.

## Triples, banks and gates

Let $[h]=\{1,\dots,h\}$ be the ground set, whose size is $h$. The letters $S$ and $T$ always denote three-element subsets of $[h]$, called *triples*. Let $\mathcal T$ be the set of all triples. A *bank* is a family of scalars indexed by $\Psi=(\Psi_1,\Psi_2,\Psi_3)\in\mathcal T^3$. The network has two banks $X$ and $Y$, with entries $X_\Psi$ and $Y_\Psi$. It changes one coordinate of $\Psi$ at a time: each of its three stages fixes two coordinates and varies the third. Within a stage, an invocation therefore sees a source vector $(X_T)_{T\in\mathcal T}$ and a target vector $(Y_S)_{S\in\mathcal T}$, and a *forward invocation* applies the gates below to them.

A *gate* is a fixed linear map on some wires; the other wires keep their values. A *scratch wire* has an arbitrary starting value, which the network must restore. The network is built within the framework of [Linear networks and frames](linear-network-frames.md), in which each wire is a role and each vertex carries a frame. A common representation on all wires at a gate lets that gate act pointwise on arrays, <cite data-source="paper">gate lets that gate act pointwise without disturbing the representation.</cite>

## Side wires, central wires and gates

Distinct triples are *neighbours* when they share exactly one element: <cite data-source="paper">S, T are neighbors when |S ∩ T | = 1.</cite> Each ordered neighbouring pair $(S,T)$ has a *side wire* $A_{ST}$, and each ground element $\Upsilon\in[h]$ has a *central wire* $C_\Upsilon$. The letters $A$ and $C$ name wires here. In the bit construction <cite data-source="paper">In the bit construction, scalars lie in F2</cite>, so signs vanish and addition is exclusive or.

The four gates are:

- *copy*: adds $X_T$ to $A_{ST}$ for each neighbouring pair $(S,T)$;
- *side injection*: adds $\sum_{T \text{ neighbour of } S} A_{ST}$ to $Y_S$;
- *gather*: adds $\sum_{T\ni \Upsilon}X_T$ to $C_\Upsilon$, for each $\Upsilon\in[h]$;
- *scatter*: adds $\sum_{\Upsilon\in S}C_\Upsilon$ to $Y_S$.

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

Rows 0 and 1 remove the starting scratch values. Rows 2 to 5 bring in the source values and add their effect to the target. Rows 6 and 7 restore the scratch wires. <cite data-source="paper">Each update leaves its control wires unchanged.</cite> Copy and gather write only scratch wires and read the unchanged $X$, so repeating either one cancels its effect over $\mathbb F_2$. That is why rows 6 and 7 undo rows 3 and 2.

## Why the scratch values cancel

Let $A^0$ and $C^0$ be the starting values of the side wires and the central wires. Over $\mathbb F_2$ subtraction is addition. Rows 0 and 1 add the side injection of $A^0$ and the scatter of $C^0$ to $Y$. Rows 2 and 3 change the side wires to $A^0$ plus copy and the central wires to $C^0$ plus gather. Rows 4 and 5 then add the scatter of the new central wires and the side injection of the new side wires to $Y$. The terms in $A^0$ and $C^0$ each appear twice and cancel, and rows 6 and 7 restore them. So the net change to $Y$ is "copy, then side injection" plus "gather, then scatter", whatever the scratch values were.

The coefficient of $X_T$ in $Y_S$ has two routes. The central route contributes $|S\cap T|$ modulo 2: <cite data-source="paper">In the bit case, the central coefficient from xT to yS is |S ∩ T | mod 2.</cite> The side route contributes $1$ exactly when $T$ is a neighbour of $S$, that is, when $|S\cap T|=1$. Three cases cover every $T$:

- $T=S$: the central route gives $3 \bmod 2=1$ and the side route gives $0$, since $S$ is not its own neighbour. Total $1$.
- $|S\cap T|=1$: both routes give $1$. Total $0$.
- $|S\cap T|\in\{0,2\}$: both routes give $0$. Total $0$.

So $Y_S\leftarrow Y_S+X_S$ for every $S$, and no $X_T$ with $T\neq S$ reaches $Y_S$. The side route is what <cite data-source="paper">cancels exactly the intersection-one cases;</cite> when $|S\cap T|=1$ it cancels the central contribution of $1$.

For example, let $h=5$ and $S=\{1,2,3\}$. The coefficient of $X_S$ in $Y_S$ is $1$, while $\{1,4,5\}$ (one common element) and $\{1,2,4\}$ (two common elements) both contribute $0$.

## Exchanging the banks

<cite data-source="paper">For arbitrary initial values of its auxiliary wires, a forward invocation changes yS to</cite> <cite data-source="paper">yS + xS and leaves every other value unchanged.</cite> Over $\mathbb F_2$ this is $Y\leftarrow Y+X$. Each pair of banks then goes through three stages, written as $(X,Y)\mapsto(\cdot,\cdot)$:

1. Stage 1, a forward invocation from $X$ to $Y$: $(X,\,Y)\mapsto(X,\,X+Y)$.
2. Stage 2, the inverse schedule from $Y$ to $X$: $(X,\,X+Y)\mapsto(Y,\,X+Y)$, since $X+(X+Y)=Y$.
3. Stage 3, a forward invocation from $X$ to $Y$: $(Y,\,X+Y)\mapsto(Y,\,X)$, since $(X+Y)+Y=X$.

The inverse schedule runs the rows in reverse order with the banks renamed. <cite data-source="paper">The inverse schedule with logical source Y and target X effects X ← X − Y .</cite> This is valid because each row writes only wires it does not read, so over $\mathbb F_2$ each row is its own inverse. The paper states the result with signs as <cite data-source="paper">(Xa , Ya ) 7−→ (−Ya , Xa )</cite>; over $\mathbb F_2$ the signs disappear, so the banks are swapped.

## Labels and their cost

Each wire carries an array, and changing an array's representation along an edge costs work. The network labels its wires with [subspace labels](subspace-labels.md): nondegenerate subspaces of a fixed bilinear space $E$. A subspace is *nondegenerate* when the form restricted to it has no nonzero vector orthogonal to all of it. <cite data-source="paper">On every edge one label will contain the other.</cite> <cite data-source="paper">Every edge joins comparable nondegenerate labels.</cite> For an edge with labels $U'\subseteq U$, the residual is <cite data-source="paper">the orthogonal complement of the smaller label inside the larger one</cite>, namely $U\cap U'^{\perp}$. Its dimension is the cost of the edge, since the cost is the <cite data-source="paper">change in label dimension.</cite>

The residual has the expected dimension. If $U'$ is nondegenerate, then $U'\cap U'^{\perp}=\{0\}$, so $U'$ and $U\cap U'^{\perp}$ meet only in zero. Edge residuals are computed through the [Dual space](dual-space.md) $U'^{*}$, the linear functionals on $U'$. The map $u\mapsto\langle u,\cdot\rangle|_{U'}$ sends $U$ onto $U'^{*}$, because nondegeneracy of $U'$ makes every functional on $U'$ of the form $\langle w,\cdot\rangle$ with $w\in U'\subseteq U$. Its kernel is $U\cap U'^{\perp}$, so rank-nullity gives $\dim(U\cap U'^{\perp})=\dim U-\dim U'$, and the two pieces add up to $U$.

The total cost is the sum of residual dimensions over all edges. <cite data-source="paper">The saving will come from keeping the total dimension lost on decreasing</cite> edges small. The only decreasing edges are the central-wire edges: <cite data-source="paper">central-wire edges from time 3 to time 4; their dimension loss is h.</cite>

## The bit construction's labels

For the bit network take $E=\mathbb Q^h$ with the form $\langle\mathbf p,\mathbf q\rangle=\mathbf p^{\mathsf T}(I-J/9)\mathbf q$, where $\mathbf p,\mathbf q$ are vectors of $E$ and $J$ is the all-ones matrix. The labels' orthogonality and nondegeneracy are tested with the [bilinear form](bilinear-form.md) of $E$. Let $t_T$ be the $0/1$ indicator vector of $T$. Then $t_S^{\mathsf T}t_T=|S\cap T|$ and $t_S^{\mathsf T}Jt_T=9$, so

$$\langle t_S,t_T\rangle=|S\cap T|-1.$$

Hence $\langle t_T,t_T\rangle=2\neq 0$, and neighbours satisfy $\langle t_S,t_T\rangle=0$.

Nondegeneracy is checked through the [Eigenvalue](eigenvalue.md)s of the form matrix $I-J/9$. The matrix $J$ has eigenvalue $h$ on the all-ones vector $\mathbf 1$ and $0$ on vectors whose entries sum to zero. So $I-J/9$ has eigenvalues $1$ and $1-h/9$. For $h=100$ the second is $-91/9\neq 0$. <cite data-source="paper">This form has eigenvalues 1 and 1−h/9 = −91/9, so it is nondegenerate.</cite>

On a side wire joining neighbours $S$ and $T$, the smaller label is the line $\langle t_S\rangle$ and the larger is $t_T^{\perp}$. Since $\langle t_S,t_T\rangle=0$, the vector $t_S$ lies in $t_T^{\perp}$, so $\langle t_S\rangle\subseteq t_T^{\perp}$: orthogonality of the indicator vectors gives exactly the nesting that the change of frame needs. <cite data-source="paper">The first inclusion is possible because tX ⊥ tY</cite>. Both labels are nondegenerate, and the residual $t_T^{\perp}\cap t_S^{\perp}$ has dimension $(h-1)-1=h-2$. <cite data-source="paper">Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal</cite>.

## The complex variant

The complex variant keeps the schedule and changes the scalars and the neighbour rule. <cite data-source="paper">In the complex construction, scalars lie in Z[i, 1/2], and neighbors are distinct triples with</cite> <cite data-source="paper">even intersection.</cite> In the complex case the central coefficient is $(|S\cap T|-1)/2$, which is meaningful only over these dyadic scalars. See the [complex construction](complex-construction.md) page.
