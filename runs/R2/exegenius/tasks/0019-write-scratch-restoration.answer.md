Restoring auxiliary scratch values is a way to use spare registers during a computation while leaving their contents unchanged at the end. Such a register may be overwritten along the way, but its starting content is arbitrary and the final result must not depend on it.

Let $a$ denote the initial value of an auxiliary register, which may be any value. The procedure has four stages:

1. Subtract $a$ from the register.
2. Compute the intended operation, using the register as scratch space.
3. Add the computed result back into the register.
4. Reverse the operations of stage 2, so that the data they touched is in its intended state.

Because stage 1 subtracts $a$ and stage 3 adds the result back, the register's final content does not depend on $a$. For example, if $a = 5$ and the computed result is $3$, the register is left at $5$ and the data is unchanged apart from the intended operation. <cite data-source="paper">The final permutation is exact for arbitrary initial auxiliary values.</cite>

The procedure is applied to a [Finite linear network with roles and frames](linear-network-roles.md), whose wires include the auxiliary registers.
