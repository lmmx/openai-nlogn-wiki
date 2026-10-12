Fast address interchange is a tape procedure that swaps two disjoint contiguous address fields of an array, and its cost bound lets the recursion in [Recursive power saving](recursive-power-saving.md) save a power. An address field is a block of consecutive address bits.

$V$ is the stored bit volume: the number of data bits the array holds. $u$ is the width of each field: the number of address bits in one field. The letter $u$ changes meaning here. $\tau$ is a fixed exponent with $0<\tau<1$. <cite data-source="paper">Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$.</cite>

The procedure is applied to each [Address shear](address-shear.md) that a layer produces. A shear $(H,D)\mapsto(H+AD,D)$ adds to $H$ a combination of $D$ given by the rational matrix $A$. Write $A=E_1\Pi E_2$ with $E_1,E_2$ invertible and lower-triangular, and $\Pi$ a partial permutation matrix. Invertible factors preserve rank, so $\Pi$ has $\operatorname{rank} A$ ones. Lower-triangular updates cost $O(V)$. Each one of $\Pi$ is an interchange of an $H$ field with a $D$ field, so a shear takes as many interchanges as its rank.

It runs the [Linear network with restored auxiliary values](linear-network-exchange.md), whose gates act on the stored array and restore every auxiliary value. <cite data-source="paper">The final permutation is exact for arbitrary initial auxiliary values.</cite>

Each level divides the field width by a fixed integer $c\ge 2$. The swap is three updates, $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$, sending $(H,D)$ to $(D,H)$. Only the middle one is a shear. The network has $W$ wires and total edge rank $s$, the sum of its edge matrix ranks. <cite data-source="paper">An edge matrix of rank $a$ will require $a$ smaller interchanges.</cite> So each level makes $s$ recursive calls, each on volume $V/W$.

Each level's time per stored bit is at most $s/W$ times the previous level's plus a constant. After $t$ levels, $u=c^t$. The geometric sum $1+s/W+\cdots+(s/W)^t$ is $O(c^{t\tau})$ when $s/W<c^\tau$, so the cost is $O(Vu^\tau)$.
