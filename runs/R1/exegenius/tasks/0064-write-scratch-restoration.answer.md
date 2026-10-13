Restoring auxiliary scratch values is a way to use spare registers during a computation while leaving their contents unchanged at the end, so that the result does not depend on their starting contents. A register may be overwritten along the way, but its starting content is arbitrary.

Let $\alpha$ denote the initial value of an auxiliary register, which may be any value. The procedure has four stages:

1. Subtract $\alpha$ from the register, so that it holds $0$.
2. Compute the intended operation, using the register as scratch space. The computation starts from $0$ whatever $\alpha$ was, so the value $\gamma$ it leaves in the register depends only on the data, not on $\alpha$.
3. Add $\gamma$ back into the register. This changes only the register, so the data that stage 2 touched is not disturbed.
4. Reverse the operations of stage 2. Each operation of stage 2 has an inverse, so the reversal undoes the scratch changes and leaves the data in its intended state.

Since the data's result is computed from the same cleared register whatever $\alpha$ was, the final result does not depend on $\alpha$. <cite data-source="paper">The final permutation is exact for arbitrary initial auxiliary values.</cite>

The procedure is applied to a [Finite linear network with roles and frames](linear-network-roles.md), whose wires include the auxiliary registers.
