The running time cost of a machine is the number of steps it takes on an input, written as a function of the input length $n$, the number of cells that hold the input, and taken in the worst case over all inputs of that length. It is the quantity that the [main theorem](main-theorem.md) bounds.

The [main theorem](main-theorem.md), *Integer multiplication below n log n*, is a statement about this quantity: it gives one machine $A$ that multiplies two $n$-bit integers exactly. The bound on its running time has the form $O(n(\lg n)^{1-\kappa})$, where $\kappa = 2^{-182}$ is a fixed constant. <cite data-source="paper">Its worst-case running time satisfies</cite> that bound.

Running time cost is defined on a [fixed-tape machine](fixed-tape-model.md). In this model, <cite data-source="paper">A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes.</cite> The alphabet is the finite set of symbols that any cell may hold. A tape is a row of cells, and each tape has a head that sits on one cell at a time. The inputs on this page are binary strings: each cell holds $0$ or $1$.

One step is one local move: <cite data-source="paper">A step reads and writes at most one cell on each tape and moves each head by at most one cell.</cite> A head that must cross $5$ cells therefore needs at least $5$ steps.

For a machine $A$ and an input length $n$, the running time cost is $T_A(n)$, the largest number of steps $A$ takes on any input of length $n$. The maximum is needed because a machine may stop early on some inputs.

Take the machine $M$ that starts on the first cell. In each step it reads the cell under its head. If that cell holds $1$, or is the last cell, $M$ halts in that step; otherwise it moves one cell right. Each step reads one new cell, so $M$ takes at most $4$ steps on an input of length $4$. On $0001$ it reads cells $1$, $2$, $3$ (each holds $0$) and halts in step $4$ on the $1$ in cell $4$. On $0000$ it reads all four cells and halts in step $4$. Both inputs take $4$ steps and none takes more, so $T_M(4) = 4$, the maximum over the $16$ binary inputs of length $4$.

Every intermediate bound concerns the same machine: each bound counts steps of the theorem's single machine $A$ on inputs of the same length. The steps of a computation are the sum of the steps of its parts, so a bound on each term of the [cost table](cost-table.md), summed, bounds $T_A(n)$.
