The bit construction is a specialization of the [Subset-intersection network](subset-intersection-network.md) to scalars in $\mathbb F_2$, in which two triples are neighbours when they share exactly one element. It is the first of the two networks in the paper's Section 3 that exchange two banks of values while restoring every scratch wire, and the [Rank-saving recursion](rank-saving-recursion.md) depends on its wire count.

## The neighbour rule

Let $[h]=\{1,\dots,h\}$ be the ground set, with $h=100$, and let $\mathcal K$ be the set of three-element subsets of $[h]$. For $T\in\mathcal K$, let $t_T$ be its indicator vector. The neighbour rule is stated in terms of [indicator vectors](indicator-vector.md): for $S,T\in\mathcal K$, the intersection size is the dot product $|S\cap T| = t_S\cdot t_T$, so the rule is a condition on that dot product.

An ordered pair $(S,T)$ is a *neighbour pair* when $|S\cap T|=1$. A triple is never its own neighbour, since $|T\cap T|=3$. The bit construction has its scalars in the [Binary field](binary-field.md) $\mathbb{F}_2$, where addition is exclusive or and multiplication is AND, so every scalar is a single bit.

For a fixed triple $T$, let $z_b$ be the number of triples meeting $T$ in exactly one element, which are the neighbours of $T$. Choose the shared element in 3 ways and the other two elements from the 97 elements outside $T$:

$$z_b = 3\binom{97}{2} = 3\cdot 4656 = 13968.$$

## Wires and updates

One invocation works on a source bank with entries $\xi_T$ and a target bank with entries $\eta_S$, both indexed by triples. A bank is simply a family of scalars with one entry per triple. The invocation also has scratch wires: a side wire $W_{ST}$ for each neighbour pair $(S,T)$, and a central wire $C_\ell$ for each ground element $\ell\in[h]$. Scratch wires start at arbitrary values, so the construction has to cancel their contents.

Four linear updates, all over $\mathbb F_2$, act on these wires:

- *Copy* sets $W_{ST} \leftarrow W_{ST} + \xi_T$ for every neighbour pair. The paper states it as <cite data-source="paper">map adds xT to AST for each neighbor pair.</cite>
- *Gather* sets $C_\ell \leftarrow C_\ell + \sum_{T\ni \ell}\xi_T$. The paper states it as <cite data-source="paper">The gather adds T ∋i xT to Ci</cite>.
- *Side injection* sets $\eta_S \leftarrow \eta_S + \sum_{T:\,|S\cap T|=1} W_{ST}$. The paper states it as <cite data-source="paper">The side injection adds T : |S∩T |=1 AST to yS</cite>.
- *Scatter* sets $\eta_S \leftarrow \eta_S + \sum_{\ell\in S} C_\ell$, where the paper's form is <cite data-source="paper">the scatter adds i∈S Ci to yS</cite>.

## What one invocation computes

Follow a value $\xi_T$ to $\eta_S$ by two routes. Along gather and then scatter, $\xi_T$ is added to $C_\ell$ for each $\ell\in T$, and each $C_\ell$ with $\ell\in S$ is added to $\eta_S$. The number of such paths is $|S\cap T|$. Along copy and then side injection, $\xi_T$ reaches $\eta_S$ only when $(S,T)$ is a neighbour pair. Over $\mathbb F_2$, the coefficient of $\xi_T$ in $\eta_S$ is therefore

$$|S\cap T| + [\,|S\cap T|=1\,] \pmod 2.$$

Checking the cases:

- If $|S\cap T|=1$, the two routes give $1+1\equiv 0$.
- If $|S\cap T|\in\{0,2\}$, the central route gives an even count and there is no side route, so the coefficient is $0$.
- If $S=T$, the central route gives $|S\cap S|=3\equiv 1$ and there is no side route, so the coefficient is $1$.

Hence one invocation adds $\xi_S$ to $\eta_S$ and changes nothing else, once the scratch wires are cleared. The paper states the same computation: <cite data-source="paper">In the bit case, the central coefficient from xT to yS is |S ∩ T | mod 2.</cite> <cite data-source="paper">The side contribution cancels exactly the intersection-one cases</cite>, so the side wires must follow intersection size one. The central term is odd for intersection one and for the diagonal $S=T$. The side route must cancel the first case and leave the diagonal, which is wanted, so the neighbour rule excludes $S=T$.

For a small example, let the ground elements be $1,\dots,5$ and compare three pairs. For $S=\{1,2,3\}$ and $T=\{3,4,5\}$, the intersection is $\{3\}$, the central route contributes $1$ through $C_3$, and the side route contributes $1$ through $W_{ST}$, so the total is $0$. For $S=\{1,2,3\}$ and $T=\{2,3,4\}$, the intersection has two elements, the central route contributes $2\equiv 0$, and the pair is not a neighbour pair, so the total is $0$. For $S=T=\{1,2,3\}$, the central route contributes $3\equiv 1$, which is the diagonal term.

## Exchanging the banks

The scratch wires are cleared by the schedule rather than assumed zero. A forward invocation first subtracts whatever the side and central wires hold, then loads $\xi$ into them with copy and gather, adds their effect to $\eta$ with scatter and side injection, and finally unloads them. The effect on the target does not depend on the starting scratch values, which is why <cite data-source="paper">For arbitrary initial values of its auxiliary wires, a forward invocation changes yS to</cite> yS + xS.

Three invocations in sequence then exchange the banks. A forward invocation from $X$ to $Y$, followed by the inverse schedule from $Y$ to $X$, followed by a forward invocation from $X$ to $Y$, sends $(X,Y)$ to $(-Y,X)$ and restores every scratch wire. Over $\mathbb F_2$ we have $-1=1$, so the sign disappears and the result is the exchange $(X,Y)\mapsto(Y,X)$. The paper states this as <cite data-source="paper">In the bit construction this is the permutation exchanging Xa</cite> and Ya.
