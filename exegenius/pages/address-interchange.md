Fast address interchange is a tape procedure that swaps two disjoint contiguous address fields of an array, and its cost bound lets [Recursive power saving](recursive-power-saving.md) save a power. An address field is a block of consecutive address bits.

$V$ is the stored bit volume, the number of data bits the array holds. $u$ is the width of each field, the number of address bits in one field; the letter $u$ changes meaning here. $\tau$ is a fixed exponent with $0<\tau<1$. The cost is $O(Vu^\tau)$ time <cite data-source="paper">Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$.</cite>

Swapping fields $H$ and $D$ takes three updates, $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$, which send $(H,D)$ to $(D,H)$. The outer two are lower-triangular changes of $D$, each costing $O(V)$ <cite data-source="paper">A lower triangular transformation of $H$, or of $D$, costs $O(V)$</cite>. The middle one is a shear $(H,D)\mapsto(H+D,D)$.

The procedure is applied to each [Address shear](address-shear.md) that a layer (one stage of the transform) produces. Write $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower-triangular and $\Pi$ a partial permutation matrix. So $\Pi$ has $\operatorname{rank}A$ ones. Each one is one swap, so the shear takes $\operatorname{rank}A$ interchanges.

The shear is realized by running the [Linear network with restored auxiliary values](linear-network-exchange.md), whose gates act pointwise on the array. Its $W$ wires, scratch wires included, each carry rows of volume $V/W$. Gates commute with a common shear, so they run on sheared streams. Each edge $e$ changes that shear by $G_e$, the difference of its end-vertex matrices, by the interchanges above. <cite data-source="paper">The final permutation is exact for arbitrary initial auxiliary values.</cite>

Let $d\ge2$ be the size of the network's matrices; a field splits into $d$ pieces of width $u/d$. Each edge needs $\operatorname{rank}G_e$ of these interchanges <cite data-source="paper">An edge matrix of rank $a$ will require $a$ smaller interchanges.</cite>

Summing over edges, one level makes $R=\sum_e\operatorname{rank}G_e$ calls, each on volume $V/W$ and width $u/d$.

Let $\varphi(u)$ be the time per stored bit at width $u$. Each level's own work is $CV$ for a constant $C$, so dividing by $V$ gives $\varphi(u)\le\gamma\varphi(u/d)+C$, with $\gamma=R/W$. The condition $R<dW$ gives $\gamma<d$, so a fixed $\tau\in(0,1)$ with $\gamma<d^\tau$ exists.

Let $\ell=\log_d u$ be the number of levels; $\ell$ levels reach width 1, where a single-digit swap gives $\varphi(1)=O(1)$. Unrolling gives $\varphi(u)\le\gamma^\ell\varphi(1)+C\,(\gamma^0+\gamma^1+\dots+\gamma^{\ell-1})$. Here $\gamma^\ell<d^{\ell\tau}=u^\tau$; the sum is geometric if $\gamma>1$, and at most $\ell=O(u^\tau)$ otherwise. So $\varphi(u)=O(u^\tau)$.
