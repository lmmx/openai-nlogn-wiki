Fast interchange of address fields is a fixed-tape procedure that swaps two disjoint contiguous address fields of an array, and it speeds up the address moves of the multiplication construction. The procedure acts on fields of an array laid out as in [Address fields and array layout on tapes](address-fields.md). Each field has $u$ bits, so $u$ counts the bits in each field. Here $V$ is the stored bit volume, the number of bits stored in the array, and $\tau$ is a fixed exponent below 1. The cost is $O(Vu^\tau)$ <cite data-source="paper">for a fixed $\tau<1$</cite>.

Write $H$ and $D$ for the two fields, each viewed as a vector of entries over a common residue ring. Swapping them takes three updates:

$$D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D.$$

Starting from $(H,D)$, the first update gives $(H,D-H)$, the second gives $(D,D-H)$, and the third gives $(D,H)$. The updates are linear combinations of entries, so the result holds for every choice of values.

The middle update is the one the network carries out. The procedure is built from the [Address shear and lower-triangular factorization](address-shear-factorization.md): the network's endpoint operator is the shear $(H,D)\mapsto(H+D,D)$ over a residue ring, which is exactly $H\leftarrow H+D$, with its rank reduced by a lower-triangular factorization.

Two further linear-cost address updates complete the interchange. They are the outer two updates, which change only $D$ and take time linear in the stored volume, so the network supplies the only expensive step.

The network's cost bound follows from [Recursive power saving from s<Wm](recursive-power-saving.md), since the middle shear is computed by recursive calls on smaller streams of the array.

The final effect is an exact permutation, although the network uses only pointwise XOR gates, so its intermediate values are XOR combinations of data. The shear is applied to every row, including rows used as scratch with arbitrary initial contents. Exactness is secured by the [Restoring auxiliary scratch values](scratch-restoration.md) schedule, which subtracts the initial register value, computes, adds the result back, and reverses. <cite data-source="paper">The final permutation is exact for arbitrary initial auxiliary values</cite>.
