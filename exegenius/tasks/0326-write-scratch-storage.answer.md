Scratch storage is auxiliary storage that a procedure may overwrite during its work but must restore to its starting contents, whatever those contents were. The side and central wires of the [subset-intersection network](subset-intersection-network.md) are scratch storage that is restored by that network. The address-field interchange, which swaps two address fields, and the packed selected-bit addition, which adds a bit position across address chunks, both depend on it.

A tape machine reuses its work space, so scratch wires may hold old values. The paper therefore states: <cite data-source="paper">We call all these auxiliary wires scratch wires; their initial values may be arbitrary.</cite> In the bit construction, <cite data-source="paper">scalars lie in F2 , and S, T are neighbors when |S ∩ T | = 1.</cite>

Several letters below change meaning here, since earlier pages use them otherwise. The letters $S$ and $T$ denote triples, three-element subsets of the ground set, and two triples are neighbours when they share exactly one element. Write $x$ for the control vector, with entries $x_T$, and $y$ for the target vector, with entries $y_S$. Each neighbouring pair $(S,T)$ has a side wire $W_{ST}$, and each element $\ell$ of the ground set has a central wire $C_\ell$. Write $a$ for the starting values of the side wires and $c$ for those of the central wires.

$V$ is copy, which adds $x_T$ to $W_{ST}$. $J$ is side injection, which adds to $y_S$ the side wires $W_{ST}$ over the neighbours $T$ of $S$. $G$ is gather, which adds $x_T$ to each $C_\ell$ with $\ell\in T$. $R$ is scatter, which adds to $y_S$ the central wires $C_\ell$ with $\ell\in S$.

The eight-row forward schedule starts with rows 0 and 1, which subtract $Ja+Rc$ from the target $y$, cancelling the effect of the starting values. Rows 2 and 3 copy and gather, so the side wires hold $a+Vx$ and the central wires hold $c+Gx$. Rows 4 and 5 scatter and side-inject these into the target. Rows 6 and 7 undo gather and copy. <cite data-source="paper">Rows 6 and 7 restore c, a.</cite>

Adding the rows gives $-Ja-Rc+R(c+Gx)+J(a+Vx)$. The terms in $a$ and $c$ cancel, leaving $(JV+RG)x$. The paper's count: <cite data-source="paper">net target change is (J V + RG)x, independently of a, c.</cite>

The coefficient of $x_T$ in $RG$ at $y_S$ is $|S\cap T| \bmod 2$, as $x_T$ reaches $y_S$ once per element of $S\cap T$. In $JV$ it is 1 exactly when $|S\cap T|=1$. Their sum mod 2 is 1 for $T=S$ and 0 otherwise, so $JV+RG$ is the identity: <cite data-source="paper">For arbitrary initial values of its auxiliary wires, a forward invocation changes yS to</cite> $y_S+x_S$ and <cite data-source="paper">leaves every other value unchanged.</cite>

Worked example. In a toy with no side wires, $R$ reads one central wire $C_\ell$ for $y_S$, and $G$ adds 3 to $C_\ell$. If $c=7$, row 1 subtracts 7, row 3 makes $C_\ell=10$, row 4 adds 10, and row 6 restores $C_\ell$ to 7: the net change is $-7+10=3$. If $c=0$, the net change is again 3.

On arrays, gates act pointwise: <cite data-source="paper">apply each scalar gate pointwise at every address</cite>. Scratch storage restores values at every address of the [address field](address-field.md) it occupies.

It is a linear version of a construction by Buhrman, Cleve, Koucký, Loff and Speelman: <cite data-source="paper">Our scratch schedule is the linear-readout version of that construction.</cite>
