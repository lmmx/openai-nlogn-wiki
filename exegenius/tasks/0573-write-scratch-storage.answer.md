Scratch storage is auxiliary storage that a procedure may overwrite during its work but must restore to its starting contents, whatever those contents were. The side and central wires of the [subset-intersection network](subset-intersection-network.md) are scratch storage that is restored by that network. The [address-field interchange](address-interchange.md) and the [packed selected-bit addition](packed-bit-addition.md) build on this restoration.

A tape machine reuses its work space, so a scratch wire may hold an old value. The paper accordingly allows any starting values: <cite data-source="paper">We call all these auxiliary wires scratch wires; their initial values may be arbitrary.</cite>

A triple is a three-element subset of the ground set. The paper's bit construction uses scalars in $\mathbb{F}_2$ and calls triples $S$ and $T$ neighbours when they share one element: <cite data-source="paper">scalars lie in F2 , and S, T are neighbors when |S ∩ T | = 1.</cite> Here $S\cap T$ is the set of elements in both $S$ and $T$, and $\ell\in S$ means that $\ell$ belongs to $S$.

Write $x$ for the control vector, with entries $x_T$ at triples $T$, and $y$ for the target vector, with entries $y_S$; here $x_S$ is the same entry with $T$ renamed $S$. Each neighbouring pair $(S,T)$ has a side wire $W_{ST}$, and each element $\ell$ of the ground set has a central wire $C_\ell$. Write $a$ for the vector of starting values of the side wires and $c$ for that of the central wires.

$V$ is copy, which adds $x_T$ to $W_{ST}$ for each neighbouring pair. $J$ is side injection, which adds to $y_S$ the side wires $W_{ST}$ over the neighbours $T$ of $S$. $G$ is gather, which adds $x_T$ to each $C_\ell$ with $\ell\in T$. $R$ is scatter, which adds to $y_S$ the central wires $C_\ell$ with $\ell\in S$.

The forward schedule has eight rows. Rows 0 and 1 subtract $Ja+Rc$ from $y$, cancelling the effect of the starting values. Rows 2 and 3 copy and gather, so the side wires hold $a+Vx$ and the central wires hold $c+Gx$. Rows 4 and 5 scatter and side-inject these into $y$, adding $R(c+Gx)+J(a+Vx)$. Rows 6 and 7 undo gather and copy, changing only wires, so $y$ is unchanged. <cite data-source="paper">Rows 6 and 7 restore c, a.</cite>

Rows 0 to 5 therefore change $y$ by $-Ja-Rc+R(c+Gx)+J(a+Vx)$. The terms in $a$ and $c$ cancel, leaving $(JV+RG)x$. The paper's count is <cite data-source="paper">net target change is (J V + RG)x, independently of a, c.</cite>

Consider $x_T$ in $y_S$. Under $RG$ its coefficient is $|S\cap T| \bmod 2$, since $x_T$ reaches $y_S$ once per element of $S\cap T$. Under $JV$ it is 1 exactly when $|S\cap T|=1$. Their sum mod 2 is 1 when $T=S$, since $|S\cap S|=3$ is odd and $S$ is not its own neighbour, and 0 otherwise. So $JV+RG$ is the identity, which gives the paper's lemma: <cite data-source="paper">For arbitrary initial values of its auxiliary wires, a forward invocation changes yS to</cite> $y_S+x_S$ and <cite data-source="paper">leaves every other value unchanged.</cite>

Worked example. In a toy with no side wires, scatter reads one central wire $C_\ell$ into $y_S$ and gather adds $3$ to $C_\ell$. If $c=7$, row 1 subtracts 7 from $y_S$, row 3 makes $C_\ell=10$, row 4 adds 10 to $y_S$, and row 6 restores $C_\ell$ to 7. The net change is $-7+10=3$. If $c=0$, it is again 3.

On arrays, the gates act <cite data-source="paper">pointwise at every address</cite>. Scratch storage restores values at every address of the [address field](address-field.md) it occupies.
