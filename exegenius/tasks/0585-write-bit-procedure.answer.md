The bit procedure is the first of the two [tape procedures](tape-procedure.md) that move address fields of an array. It performs an [Address-field interchange](address-interchange.md) by a shear over the binary field, and the recursion in [Rank-saving recursion](rank-saving-recursion.md) uses it as a cheap field interchange.

## The task

An array is indexed by addresses, and each address is a tuple of fields. A field is a block of $u$ bits at the same position in every address. Given two disjoint fields $H$ and $D$, the procedure must leave each address holding the $D$ block where it held the $H$ block, and the reverse. <cite data-source="paper">The first procedure interchanges two disjoint contiguous address fields of u bits in an array</cite>.

The cost of the procedure is measured by its [running time cost](running-time-cost.md). <cite data-source="paper">Its cost is O(V uτ ) for a fixed τ < 1.</cite> Here $V$ is the stored bit volume, so the cost is $V u^{\tau}$: a power of the field width below linear. The transform needs this: <cite data-source="paper">Θ(log n) transform levels already costs Θ(n log n).</cite> A linear-cost interchange would save nothing, so the recursion needs a power of $u$ below linear.

## The shear

Over the binary field, addition is exclusive or ($\oplus$), taken bit by bit. The shear $(H,D)\mapsto(H\oplus D,\,D)$ adds $D$ into $H$ and leaves $D$ unchanged. <cite data-source="paper">For the bit procedure, that endpoint operator is an address shear: two fields, written as vectors</cite>.

A shear takes three steps, one of which is an interchange:

1. $D\leftarrow D\oplus H$.
2. Swap $H$ and $D$. This is the one interchange.
3. $D\leftarrow H\oplus D$.

<cite data-source="paper">The first and last updates target a later field controlled by an earlier field.</cite> After step 1, $D=d\oplus h$. The swap gives $H=d\oplus h$ and $D=h$. Step 3 gives $D=(d\oplus h)\oplus h=d$. So $(h,d)$ becomes $(h\oplus d,\,d)$, the shear, and <cite data-source="paper">It uses just one interchange.</cite>

Worked example, with $u=2$, $H=01$ and $D=10$:

1. $D\leftarrow 10\oplus 01=11$.
2. Swap: $H=11$, $D=01$.
3. $D\leftarrow 11\oplus 01=10$.

The result is $(H,D)=(11,10)$, which is $(H\oplus D,\,D)$. The full interchange is the exclusive-or swap: $D\leftarrow D\oplus H$, then the shear $H\leftarrow H\oplus D$, then $D\leftarrow H\oplus D$. <cite data-source="paper">Only the middle shear uses the circuit.</cite>

## The network

The middle shear is computed by a [bit network](bit-network.md), a fixed circuit of wires and gates. <cite data-source="paper">Its fixed, pointwise bit gates induce a permutation</cite> of the inputs. Each vertex has an invertible frame $\Phi_M$, which moves the entry at $(H,D)$ to $(H+MD,\,D)$. Since $\Phi_{M'}\Phi_M=\Phi_{M'+M}$, the frames along a route telescope, <cite data-source="paper">Thus the intermediate frames cancel</cite>, and the route acts only through its endpoint matrices. The construction supplies endpoint matrices with <cite data-source="paper">Mout(ρ(w)) − Min(w) = Im</cite>, so every route acts as $\Phi_I$, the shear.

## Cost as a power of the width

Each edge $e$ has a matrix $A_e$, the difference of its endpoint matrices. A shear by a matrix of rank $a$ <cite data-source="paper">can be performed with exactly a interchanges of pairs of b-digit fields</cite>, where $b$ is the number of digits in each field. The bit procedure counts its interchanges by the [matrix rank](matrix-rank.md) of each edge matrix.

Let $W$ be the number of wires and $s=\sum_e \operatorname{rank}A_e$. <cite data-source="paper">The number of recursive calls is the sum of the edge ranks, exactly s.</cite> Each call acts on one of the $W$ role streams, <cite data-source="paper">stream of volume V /W</cite>. The construction gives <cite data-source="paper">s < W m</cite>, where $m$ is the recursion base. Neither $s$ nor $W$ depends on $u$.

Take $u=m^k$, so $k$ is the number of levels. Each level divides the field width by $m$, multiplies the number of calls by $s$, and divides each volume by $W$. After $k$ levels there are $s^k$ calls on volume $V/W^k$, so the leaf volume is $V(s/W)^k$. Since $s/W<m$, <cite data-source="paper">Choose a rational number τ ∈ (0, 1) with s/W < mτ</cite>. Then $\log_m(s/W)<\tau$, and
$$
V\left(\frac{s}{W}\right)^{k}=V\,u^{\log_m(s/W)}\le V\,u^{\tau},
$$
using $u\ge 1$.

Each call's other work is linear in its volume: <cite data-source="paper">triangular operations have total cost O(V ) because their number is fixed.</cite> Level $j$ has $s^j$ calls of volume $V/W^j$, so it costs $O(V(s/W)^j)$. Let $\theta=\max(0,\log_m(s/W))$ be the capped logarithm of $s/W$, which is below $\tau$. Summing over $k$ levels gives $O(Vk\max(1,s/W)^k)=O(V\log u\cdot u^{\theta})$. Since $\log u=O(u^{\tau-\theta})$, the total is $O(Vu^{\tau})$.
