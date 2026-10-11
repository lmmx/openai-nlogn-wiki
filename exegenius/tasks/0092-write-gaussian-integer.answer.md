Here $i$ is the imaginary unit, the number with $i^2=-1$.

A Gaussian integer is a complex number $a+bi$ whose real part $a$ and imaginary part $b$ are both integers. The later steps of the argument take their exact intermediate arrays over this number system, so the butterfly layers and transforms that act on those arrays keep exact values. Write $\mathbb{Z}[i]$ for the set of all Gaussian integers.

Every integer is a Gaussian integer, with imaginary part $0$: $5=5+0i$. The number $3+4i$ is a Gaussian integer because $3$ and $4$ are integers. The number $\tfrac12+i$ is not, because its real part $\tfrac12$ is not an integer.

Sums and products of Gaussian integers are again Gaussian integers, since the integers are closed under addition and multiplication and $i^2=-1$ is an integer. For example, $(1+2i)(3-i) = 3 - i + 6i - 2i^2 = 5+5i$.

The source keeps its entries in $\mathbb{Z}[i, 1/2]$, which allows division by powers of two on top of the Gaussian integers. It states that its inverse operations preserve these arrays: <cite data-source="paper">Gaussian integer divided by 2m , so both preserve arrays over Z[i, 1/2].</cite>. Each coefficient of a transform output is itself an exact sum of products of Gaussian integers: <cite data-source="paper">Gaussian integer coefficient Hj is a sum of exactly r signed products of Gaussian integer input</cite>.
