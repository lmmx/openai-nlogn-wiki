A power saving in the logarithmic factor is a worst-case time bound $n(\lg n)^{1-\kappa}$ for multiplying two $n$-bit integers, where $\kappa > 0$ is a fixed constant that sets the size of the saving. It is the form a result takes when it beats the $n\lg n$ rate.

The bound is smaller than $n\lg n$ by the factor $(\lg n)^{\kappa}$, which grows without bound as $n$ grows, so the bound is $o(n\lg n)$. Since $\kappa$ does not depend on $n$, the bound is a single function of $n$. For example, take $\kappa = 1/2$ and $n = 2^{16}$. Then $\lg n = 16$, so $n(\lg n)^{1/2} = 4n$ while $n\lg n = 16n$: a saving by a factor of $4$.

The paper reports such a machine in the fixed-tape model. <cite data-source="paper">We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model.</cite> A fixed-tape machine is a multitape machine with a fixed number of tapes, so its time bound is a case of the claim the conjecture makes about multitape machines.

A power saving therefore undercuts the [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md). That conjecture says $n\lg n$ is the optimal order of growth for multitape Turing machines, so one machine with worst-case time $o(n\lg n)$ is a counterexample to it.
