The ceiling function is the rounding-up operation that the argument needs before it can turn recovered integer coefficients into a binary product through carry propagation. It is the least whole number that is not smaller than a given real number.

Here $\kappa$ denotes the real number being rounded up, such as $2.3$ or $-1.5$. The **ceiling** of $\kappa$, written $\lceil \kappa \rceil$, is the least integer that is not less than $\kappa$.

Some values:

$$\lceil 2.3 \rceil = 3, \qquad \lceil 4 \rceil = 4, \qquad \lceil -1.5 \rceil = -1.$$

An integer is its own ceiling, so $\lceil k \rceil = k$ whenever $k$ is an integer. For a real number that is not an integer, the ceiling is the next integer above it. Counting groups is a typical use: $7$ values grouped into pairs need $\lceil 7/2 \rceil = 4$ pairs, the last of which holds a single value.
