# Normalized cost

The normalized cost of an operation is its running time divided by the stored volume $V$ of the data it acts on. The paper writes every cost this way, because $V$ is the natural measure of the work that must be done on every stored bit.

The paper's total volume is $V = Tp = \Theta(n)$, so a normalized cost is a cost per stored bit. Table 1 of the paper lists these normalized costs for each operation. Each entry is a fixed constant times a power of $p$, so the entries can be compared directly even though the operations act on arrays of different sizes.

For example, if an operation costs $O(V d^{\lambda'})$ on an array of volume $V$, where $\lambda' < 1$ is a fixed exponent, its normalized cost is $O(d^{\lambda'})$, which is a power of $d$ with exponent less than one. Since $d = \Theta(p^{\epsilon})$, this is also a power of $p$, and this is the form in which the paper writes each operation's cost.

The normalized cost is the quantity that the [cost accounting](cost-accounting.md) page sums over the operations of the algorithm.

## Used by

- [Recursive rank saving](rank-saving-recursion.md)

## Sources

> Table 1 lists costs after division by V
>
> — Integer multiplication below n log n (OpenAI, 2026)
