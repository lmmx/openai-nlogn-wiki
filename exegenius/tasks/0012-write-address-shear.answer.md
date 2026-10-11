An address shear is the map that adds one address field to another and leaves the second unchanged. It is the operation to which the tape procedure for interchanging two address chunks reduces, so the cost of an interchange is the cost of its shears.

An address field is a block of consecutive digits of an array address, and an address chunk is a contiguous block of digits made of equal-width address fields. Here $q$ is a fixed odd prime, chosen so that the denominators of the rational matrices used below are invertible modulo $q$. Here $m$ is the number of fields in each vector. The address field $H$ is a vector of $m$ fields $H_1, \ldots, H_m$. The address field $D$ is a vector of $m$ fields $D_1, \ldots, D_m$. Each field is a block of $b$ radix-$q$ digits (digits in base $q$), so its values form the residue ring $\mathbb{Z}/q^b\mathbb{Z}$, the integers modulo $q^b$.

On a pair of address fields, the shear maps $(H, D)$ to $(H + D, D)$: the first field is increased by the second, and the second is left unchanged.

For a fixed rational $m \times m$ matrix $M$, the shear with matrix $M$ sends $(H, D)$ to $(H + MD, D)$, where $MD$ is the matrix-vector product. Taking $M$ to be the identity matrix gives the map in the first sentence. The number of interchanges for the shear is $a$, the rational rank of $M$, which is its rank as a matrix over the rational numbers. The shear with matrix $M$ <cite data-source="paper">can be performed with exactly a interchanges of pairs of b-digit fields and O(V ) further work</cite>. Here $V$ denotes the stored bit volume of the array.

So an address shear of rank $a$ is implemented by $a$ uses of one [Address-field interchange](address-interchange.md).

When $m = 1$, write $h$ for the current value of $H$ and $d$ for the current value of $D$. One unit of rank is then a single interchange between $H$ and $D$, with one addition before it and one subtraction after it: $D \leftarrow D + H$, then interchange $H$ and $D$, then $D \leftarrow H - D$. <cite data-source="paper">On an initial pair (h, d) this sequence yields (h + d, d).</cite>

For example, take $q = 3$ and $b = 2$, so the fields are residues modulo $9$, and let $h = 3$ and $d = 5$. The addition gives $D = 8$, the interchange leaves $H = 8$ and $D = 3$, and the subtraction gives $D = 5$. The pair $(3, 5)$ has become $(8, 5)$, which is $(h + d, d)$.

The shear is computed by the [Linear networks and frames](linear-network-frames.md) of the bit procedure: on every role, the endpoint operator is this shear. <cite data-source="paper">For the bit procedure, that endpoint operator is an address shear</cite>.

The shears are counted by rank for the saving it gives. <cite data-source="paper">Because the sum of these ranks is less than the number of wires</cite> times $m$, <cite data-source="paper">the resulting recurrence saves a power of the chunk width.</cite>

Interchanging two whole chunks uses the same shear in its middle step: $D \leftarrow D - H$, then $H \leftarrow H + D$, then $D \leftarrow H - D$, componentwise. <cite data-source="paper">Only the middle shear uses the circuit.</cite> Here the circuit is the fixed linear network of the bit procedure. <cite data-source="paper">The transformation sends (H, D) to (D, H).</cite>
