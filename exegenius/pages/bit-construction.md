The bit construction is a specialization of the [Subset-intersection network](subset-intersection-network.md) to scalars in $\mathbb F_2$, in which two triples are neighbours when they share exactly one element. It is the first of the two networks in Section 3 of the paper that exchange two banks of values while restoring every scratch wire, and the [Rank-saving recursion](rank-saving-recursion.md) depends on its wire count.

Some letters below take new meanings here; each is defined where it is introduced.

## Setting

A linear network is made of wires, each carrying one scalar, and gates. <cite data-source="paper">A gate is a fixed linear map on a specified set of</cite> wires, and untouched wires keep their values.

Let $[h]=\{1,\dots,h\}$ be the ground set, with $h=100$, and let $\mathcal K$ be the set of three-element subsets of $[h]$, whose members $S$ and $T$ are called triples. For $T\in\mathcal K$, let $t_T$ be the $0$-$1$ vector of length $h$ that is $1$ exactly at the elements of $T$.

An ordered pair $(S,T)$ is a *neighbour pair* when $|S\cap T|=1$. The neighbour rule is stated in terms of the [Indicator vector](indicator-vector.md) $t_T$: for $S,T\in\mathcal K$, the intersection size is the dot product $|S\cap T| = t_S\cdot t_T$, so the rule is a condition on that dot product.

The bit construction has its scalars in the [Binary field](binary-field.md) $\mathbb{F}_2$, where addition is exclusive or and multiplication is AND, so every scalar is a single bit.

## Counting neighbours

The binomial coefficient $\binom{n}{k}$ counts the $k$-element subsets of an $n$-element set. For a fixed triple $T$, let $z_b$ be the number of triples meeting $T$ in exactly one element, which are the neighbours of $T$. Such a triple is fixed by its shared element of $T$ (3 choices) and its two other elements, taken from the 97 elements outside $T$ ($\binom{97}{2}$ choices). Since $\binom{97}{2}=\frac{97\cdot 96}{2}=4656$,

$$z_b = 3\binom{97}{2} = 3\cdot 4656 = 13968.$$

## Wires and updates

One invocation works on a source bank $X$ with entries $\xi_T$ and a target bank $Y$ with entries $\eta_S$, both indexed by triples. The invocation also has scratch wires: a side wire $W_{ST}$ for each neighbour pair $(S,T)$, and a central wire $C_\ell$ for each $\ell\in[h]$. Scratch wires start at arbitrary values, so the construction must cancel their contents.

- *Copy*: $W_{ST}\leftarrow W_{ST}+\xi_T$ for every neighbour pair. <cite data-source="paper">map adds xT to AST for each neighbor pair.</cite>
- *Gather*: $C_\ell\leftarrow C_\ell+\sum_{T\ni\ell}\xi_T$. <cite data-source="paper">The gather adds T ∋i xT to Ci</cite>.
- *Side injection*: $\eta_S\leftarrow\eta_S+\sum_{T:\,|S\cap T|=1}W_{ST}$. <cite data-source="paper">The side injection adds T : |S∩T |=1 AST to yS</cite>.
- *Scatter*: $\eta_S\leftarrow\eta_S+\sum_{\ell\in S}C_\ell$. <cite data-source="paper">the scatter adds i∈S Ci to yS</cite>.

## The schedule

A forward invocation is carried out by a [Schedule](schedule.md) of eight rows, applied in order:

0. $\eta_S\leftarrow\eta_S-\sum_{T:\,|S\cap T|=1}W_{ST}$ (side injection, subtracted)
1. $\eta_S\leftarrow\eta_S-\sum_{\ell\in S}C_\ell$ (scatter, subtracted)
2. copy
3. gather
4. scatter
5. side injection
6. undo gather: $C_\ell\leftarrow C_\ell-\sum_{T\ni\ell}\xi_T$
7. undo copy: $W_{ST}\leftarrow W_{ST}-\xi_T$

Rows 0 and 1 cancel the starting scratch contents, rows 2 to 5 load $\xi$ and apply it to the target, and rows 6 and 7 unload the scratch wires.

Let $W^0_{ST}$ and $C^0_\ell$ be the starting values. After rows 0 and 1, the target entry is $\eta_S-\sum_{T:|S\cap T|=1}W^0_{ST}-\sum_{\ell\in S}C^0_\ell$. After rows 2 and 3, $W_{ST}=W^0_{ST}+\xi_T$ and $C_\ell=C^0_\ell+\sum_{T\ni\ell}\xi_T$. Rows 4 and 5 add $\sum_{\ell\in S}C_\ell+\sum_{T:|S\cap T|=1}W_{ST}$, which equals $\sum_{\ell\in S}C^0_\ell+\sum_{T:|S\cap T|=1}W^0_{ST}+\sum_{\ell\in S}\sum_{T\ni\ell}\xi_T+\sum_{T:|S\cap T|=1}\xi_T$. The starting values $W^0$ and $C^0$ cancel, so the net change to the target does not depend on them:

$$\eta_S\ \leftarrow\ \eta_S+\sum_{T}\bigl(|S\cap T|+[\,|S\cap T|=1\,]\bigr)\,\xi_T \pmod 2,$$

where the middle sum uses $\sum_{\ell\in S}\sum_{T\ni\ell}\xi_T=\sum_T|S\cap T|\,\xi_T$, because each $\xi_T$ is counted once for each element of $S\cap T$. The side route is counted with the [Iverson bracket](iverson-bracket.md) $[\,|S\cap T|=1\,]$, which is $1$ when the condition holds and $0$ otherwise.
Taking the coefficient of $\xi_T$ in $\eta_S$ mod 2:

- If $|S\cap T|=1$, the two routes give $1+1\equiv 0$.
- If $S\neq T$ and $|S\cap T|\in\{0,2\}$, the count is even and there is no side route, so the coefficient is $0$.
- If $S=T$, the count is $|S\cap S|=3\equiv 1$ and there is no side route, so the coefficient is $1$.

So one invocation changes each target entry by its own source entry, $\eta_S\leftarrow\eta_S+\xi_S$, and leaves the source bank unchanged.

The paper gives the central coefficient as <cite data-source="paper">In the bit case, the central coefficient from xT to yS is |S ∩ T | mod 2.</cite> That parity is odd for intersection one and for $S=T$, and even for intersections zero and two. The side route must cancel the odd off-diagonal case, and it does so because it <cite data-source="paper">cancels exactly the intersection-one cases</cite>.

For example, take $S=\{1,2,3\}$ and $T=\{3,4,5\}$. The intersection is $\{3\}$: the central route contributes $1$ through $C_3$, the side route contributes $1$ through $W_{ST}$, and the total is $0$. For $S=\{1,2,3\}$ and $T=\{2,3,4\}$, the central route contributes $2\equiv 0$ and there is no side route, so the total is $0$.

## Exchanging the banks

The paper's lemma for one forward invocation is <cite data-source="paper">For arbitrary initial values of its auxiliary wires, a forward invocation changes yS to</cite> $\eta_S+\xi_S$, the result derived above, and it <cite data-source="paper">restores every auxiliary value.</cite>

Three invocations in sequence exchange the banks $X$ and $Y$:

1. A forward invocation from $X$ to $Y$ gives $(X,\,Y)\mapsto(X,\,Y+X)$.
2. The [inverse schedule](schedule.md) from $Y$ to $X$ has $Y$ as its logical source and $X$ as its target. The paper states its effect as <cite data-source="paper">The inverse schedule with logical source Y and target X effects X ← X − Y</cite>. Hence $(X,\,Y+X)\mapsto(-Y,\,Y+X)$, since $X-(Y+X)=-Y$.
3. A forward invocation from $X$ to $Y$ gives $(-Y,\,Y+X)\mapsto(-Y,\,(Y+X)+(-Y))=(-Y,\,X)$.

Each invocation restores its auxiliary wires, so the scratch wires end at their starting values. Over $\mathbb F_2$ we have $-1=1$, so the result is $(X,Y)\mapsto(Y,X)$, the exchange of the two banks. The paper states this as <cite data-source="paper">In the bit construction this is the permutation exchanging Xa</cite> and Ya.
