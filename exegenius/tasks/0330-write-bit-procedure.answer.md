The bit procedure is the first of the two [tape procedures](tape-procedure.md) that move address fields of an array. It performs an [Address-field interchange](address-interchange.md) by a shear over the binary field, and the rest of the argument uses it as a cheap field interchange.

## What the procedure must do

An array is indexed by addresses, and each address is a tuple of fields, where a field is a block of $u$ bits at matching positions in every address. Given two disjoint fields $a$ and $b$, the procedure must leave each address holding the $b$ block where it held $a$, and the reverse. <cite data-source="paper">The first procedure interchanges two disjoint contiguous address fields of u bits in an array</cite>.

The cost of the procedure is measured by its [running time cost](running-time-cost.md), and it is bounded as follows. <cite data-source="paper">Its cost is O(V uτ ) for a fixed τ < 1.</cite> Here $V$ is the stored bit volume, so the cost is $V u^{\tau}$: a power of the field width below linear, which is the saving the rest of the argument needs.

## The shear

Work over the binary field, where addition is exclusive or ($\oplus$). A shear on two fields adds the second into the first and leaves the second unchanged: $(a,b)\mapsto(a\oplus b,\,b)$. <cite data-source="paper">For the bit procedure, that endpoint operator is an address shear: two fields, written as vectors</cite>, where each field is a vector of bits and the addition is taken bit by bit.

The shear is computed by a [bit network](bit-network.md). <cite data-source="paper">Its fixed, pointwise bit gates induce a permutation</cite>: each gate XORs the values on its input wires separately at every address, and the number of wires does not depend on the array. Each wire carries an array that is changed by an invertible frame at each gate. <cite data-source="paper">Thus the intermediate frames cancel</cite>, so a route from an input wire to an output wire acts only through its two endpoints. Those endpoints differ by exactly the shear on that route, and the network therefore computes the shear.

## Shears as interchanges

Each shear is turned into field interchanges. The total number of interchanges is governed by the [matrix rank](matrix-rank.md) of the shears, not by the full width. <cite data-source="paper">can be performed with exactly a interchanges of pairs of b-digit fields</cite>, and each of the remaining operations is a [linear-cost](running-time-cost.md) update.

For a single shear the sequence is: add the first field into the second, swap the two fields, then add the first field into the second again. On $(a,b)$ this gives $(a\oplus b,\,b)$, and <cite data-source="paper">It uses just one interchange.</cite>

The full interchange of $a$ and $b$ is then the XOR swap, with the shear as its middle step.

## Worked example

Take $u=2$, $a=01$ and $b=10$:

1. $b \leftarrow b \oplus a = 10 \oplus 01 = 11$.
2. $a \leftarrow a \oplus b = 01 \oplus 11 = 10$ (the shear, realized by one interchange).
3. $b \leftarrow b \oplus a = 11 \oplus 10 = 01$.

The result is $(a,b)=(10,01)$, so the two blocks have exchanged places. Steps 1 and 3 are [linear-cost](running-time-cost.md) updates of the later field from the earlier one: <cite data-source="paper">The first and last updates target a later field controlled by an earlier field.</cite>

## Why the cost is a power of the width

Let $s$ be the total number of smaller calls that the network makes, and let $W$ be its number of wires. <cite data-source="paper">Because the sum of these ranks is less than the number of wires</cite> times $m$, so $s < Wm$. The rank count gives $s/W < m^{\tau}$ for a fixed $\tau<1$, where $m$ is the recursion base.

Each call on width $u$ makes $s$ calls on width $u/m$, and each level divides the volume among the $W$ roles. After $k=\log_m u$ levels there are $s^k$ leaf calls, each on volume $V/W^k$. The total leaf volume is therefore
$$
V\left(\frac{s}{W}\right)^{k} = V\,u^{\log_m (s/W)} \le V\,u^{\tau},
$$
because $\log_m(s/W) < \tau$. The linear-cost work at each level adds $O(V)$ per level, which is $O(V\log u)$ in all and is absorbed into $O(V u^{\tau})$.
