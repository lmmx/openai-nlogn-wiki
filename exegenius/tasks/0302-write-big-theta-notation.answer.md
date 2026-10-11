Big-Theta notation says that two functions grow at the same rate, up to constant factors, once the input is large. It is the two-sided counterpart of big-O notation: big-O gives only an upper bound, while Big-Theta also gives a matching lower bound. On the way to the theorem, the parameters are chosen so that every term of the cost table is bounded by the theorem's expression, and this page gives the notation in which such order statements are made. The guard-width bound page builds on it.

Let $u$ be a function from input sizes to nonnegative real numbers, and let $h$ be a second function of the same kind. Write $N$ for the input size, the number of bits in the input. Here $C_1$ is the lower factor, a positive real constant, and $C_2$ is the upper factor, a positive real constant. The threshold $N_0$ is an input size from which both inequalities hold.

We write $u(N)=\Theta(h(N))$ when there are constants $C_1>0$ and $C_2>0$ and a threshold $N_0$ such that

$$C_1\,h(N)\le u(N)\le C_2\,h(N)\qquad\text{for all } N\ge N_0.$$

The right inequality is the upper bound $u(N)=O(h(N))$. The left inequality is the lower bound. Both are needed. The upper bound alone does not exclude $u$ being much smaller than $h$: $1=O(N)$ holds, but $1$ is not of the order of $N$. The lower bound alone does not exclude $u$ being much larger than $h$.

Worked example. Let $u(N)=3N^2+5N$ and $h(N)=N^2$. For $N\ge 1$ we have $5N\le 5N^2$, so

$$3N^2\le 3N^2+5N\le 8N^2 .$$

This gives $u(N)=\Theta(h(N))$ with $C_1=3$, $C_2=8$ and $N_0=1$. The linear term $5N$ does not change the order, because it is at most a constant multiple of $N^2$ once $N\ge 1$.

The converse fails. The function $N^2$ is not $\Theta(N)$: for any constant $C_2$, the inequality $N^2\le C_2 N$ fails once $N>C_2$, so no upper factor exists.

The paper's own uses are of the same kind. It motivates its savings by counting: scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels <cite data-source="paper">already costs Θ(n log n)</cite>. Both factors are Θ-statements, an array of order $n$ bits and order $\log n$ levels, so the total cost is of order $n\log n$ and not merely bounded by it.

Here $\lg$ is the base-2 logarithm (see [Base-2 logarithm](base-two-logarithm.md)), and $\kappa$ is the fixed positive exponent saving in the bound, equal to $2^{-182}$ in the paper. The method for the main claim is to bound each term above by a constant times $n(\lg n)^{1-\kappa}$, so that the total cost is bounded by the same expression. The paper states its result as <cite data-source="paper">multiplies two n-bit integers in O(n(lg n)1−κ ) worstcase time</cite>.
