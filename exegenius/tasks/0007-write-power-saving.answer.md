A power saving in the logarithmic factor is a worst-case time bound $n(\lg n)^{1-\kappa}$, where $n$ is the number of bits in each input integer and $\kappa$ is a fixed number with $\kappa > 0$. The main result of the argument achieves this bound in place of the $n\lg n$ rate, and $\kappa$ sets the size of the saving.

The bound is smaller than $n\lg n$ by the factor $(\lg n)^{\kappa}$, a power of $\lg n$ that grows without bound as $n$ grows. For example, take $\kappa = 1/2$ and $n = 2^{16}$. Then $\lg n = 16$, so $n(\lg n)^{1/2} = 4n$ while $n\lg n = 16n$, and the saving is a factor of $4$. Each saving is modest, but the ratio $(\lg n)^{\kappa}$ is unbounded, so the bound is $o(n\lg n)$.

Because $\kappa$ is fixed rather than depending on $n$, one algorithm achieves the same saving for every input length. A power saving therefore undercuts the [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md), which takes $n\lg n$ to be the optimal order of growth. The paper's claim is exactly such a saving. <cite data-source="paper">We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model.</cite>

The [fixed-tape multiplication page](fixed-tape-multiplication.md) gives the algorithm that achieves this bound for a specific fixed $\kappa$.
