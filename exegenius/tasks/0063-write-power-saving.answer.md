A power saving in the logarithmic factor is a worst-case time bound $n(\lg n)^{1-\kappa}$ for multiplying two $n$-bit integers, where $\kappa$ is a fixed number with $\kappa > 0$ that sets the size of the saving. The main result achieves this bound in place of the $n\lg n$ rate.

The bound is smaller than $n\lg n$ by the factor $(\lg n)^{\kappa}$, which grows without bound as $n$ grows, so the bound is $o(n\lg n)$. For example, take $\kappa = 1/2$ and $n = 2^{16}$. Then $\lg n = 16$, so $n(\lg n)^{1/2} = 4n$ while $n\lg n = 16n$: a saving by a factor of $4$.

Because $\kappa$ is fixed rather than depending on $n$, one algorithm achieves the same saving for every input length. The conjecture concerns multitape Turing machines, and a machine with a fixed number of tapes is one of them, so a bound for such a machine is a bound for multitape machines. The paper's claim is exactly such a saving. <cite data-source="paper">We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model.</cite>

A power saving therefore undercuts the [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md), since the conjecture says no multitape machine has a time bound of smaller order than $n\lg n$.
