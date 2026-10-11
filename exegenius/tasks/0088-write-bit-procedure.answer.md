The bit procedure is the first of the two tape procedures that move address fields in an array. It is the step that realizes the interchange of two address fields with a shear computed by a fixed network of XOR gates, so the rest of the argument can use it as a cheap field interchange. The concept is built on [Address-field interchange](address-interchange.md), the operation it performs.

The bit procedure realizes an [Address-field interchange](address-interchange.md) of two disjoint contiguous address fields, and it does so with a shear computed by a fixed network of XOR gates.

## What the procedure must do

An array is indexed by addresses, and each address is a tuple of fields, where a field is a block of $u$ bits at matching positions in every address. Given two such fields $x$ and $y$, the procedure must leave the array so that each address holds the $y$ block where it held $x$, and the reverse. <cite data-source="paper">The first procedure interchanges two disjoint contiguous address fields of u bits in an array</cite> <cite data-source="paper">Its cost is O(V uτ ) for a fixed τ < 1.</cite> The cost bound is what the rest of the argument needs: an interchange costs time that grows like a power of $u$, less than linear.

## The shear

Work over the binary field, the two-element set $\{0,1\}$ in which addition is XOR ($\oplus$). A shear on two fields is the map $(x,y)\mapsto(x\oplus y,\,y)$: it adds the second field into the first and leaves the second unchanged. <cite data-source="paper">For the bit procedure, that endpoint operator is an address shear: two fields, written as vectors</cite> The shear is the only part of the work that is not a linear-cost update, and it is computed by a network whose gates are all XOR: <cite data-source="paper">uses only pointwise XOR gates</cite>.

The procedure produces the full interchange from the shear with two cheaper updates. <cite data-source="paper">Two further linear-cost address updates complete their interchange.</cite> The two outer updates change a later field from an earlier one, $y \leftarrow y \oplus x$, which is the linear-cost direction: <cite data-source="paper">The first and last updates target a later field controlled by an earlier field.</cite>

## Worked example

Take $u=2$, with the fields $x=01$ and $y=10$. The three steps are:

1. $y \leftarrow y \oplus x = 10 \oplus 01 = 11$ (linear-cost update of the later field).
2. $x \leftarrow x \oplus y = 01 \oplus 11 = 10$ (the shear).
3. $y \leftarrow y \oplus x = 11 \oplus 10 = 01$ (linear-cost update of the later field).

The result is $(x,y) = (10,01)$, so the two blocks have exchanged places. The three updates are the standard XOR swap; the paper uses the shear as its middle step.

## Why the shear is what the recursion saves on

A single shear on one pair of fields is itself a field interchange. <cite data-source="paper">On an initial pair (h, d) this sequence yields (h + d, d). It uses just one interchange.</cite> A shear that is a sum of several such pieces is carried out by one interchange per unit of rank, so the cost of the whole procedure depends on the total rank of the shears, not on the full width. <cite data-source="paper">Because the sum of these ranks is less than the number of wires times m, the resulting recurrence saves a power of the chunk width.</cite> Each level of the recursion therefore makes fewer smaller interchanges than the width it started with, which is what yields the bound $O(V u^{\tau})$ with $\tau < 1$.
