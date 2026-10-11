Big-Theta notation says that two functions grow at the same rate, up to constant factors, once the input is large. It is the two-sided counterpart of big-O, which gives only an upper bound. On the way to the theorem, the parameters are chosen so that every term of a cost table, which lists the running time cost of each operation of the algorithm, is bounded by the theorem's expression, and Big-Theta states those comparisons.

Here $f$ is the function being bounded, and $h$ is the comparison function; both map input sizes to nonnegative real numbers. Here $c_1$ is the lower factor, a positive real constant, and $c_2$ is the upper factor, a positive real constant. The threshold $n_0$ is an input size from which both inequalities hold.

We write $f(n)=\Theta(h(n))$ when

$$c_1\,h(n)\le f(n)\le c_2\,h(n)\qquad\text{for all } n\ge n_0.$$

The right inequality is the upper bound $f(n)=O(h(n))$. The left inequality is the lower bound $h(n)=O(f(n))$. Both are needed: $1=O(n)$ holds, but $1$ is not of the order of $n$, so the upper bound alone does not exclude $f$ being much smaller than $h$.

Worked example. Let $f(n)=3n^2+5n$ and $h(n)=n^2$. For $n\ge 1$ we have $5n\le 5n^2$, so

$$3n^2\le 3n^2+5n\le 8n^2 .$$

This gives $f(n)=\Theta(h(n))$ with $c_1=3$, $c_2=8$ and $n_0=1$. The converse fails: $n^2$ is not $\Theta(n)$, since $n^2\le c_2 n$ fails once $n>c_2$, for any $c_2$.

Product rule. If each of two functions is $\Theta$ of a second function, their product is $\Theta$ of the product of the second functions. Multiply the two pairs of inequalities; all functions are nonnegative.

Cost argument. A running time cost counts the steps of a Turing machine. A pass that reads every stored bit takes at least one step per bit, since a head moves one cell per step. So such a pass costs at least a constant times the number of stored bits.

The paper motivates its savings by a count of this kind. A transform level is one stage of the transform, and each stage scans the whole stored array. The paper states that <cite data-source="paper">Θ(log n) transform levels already costs Θ(n log n)</cite>. Here the array has $\Theta(n)$ stored bits and there are $\Theta(\log n)$ levels, so by the product rule the total is of order $n\lg n$, not merely bounded by it. Such order statements compare orders built from the [Base-2 logarithm](base-two-logarithm.md).

Here $V$ is the number of stored bits, which is $\Theta(n)$. Table 1 is the cost table: each row gives an operation's cost divided by $V$, as a power of $p$. The precision parameter $p$ is set by <cite data-source="paper">p = 6⌈log2 n⌉ = Θ(log n)</cite>. <cite data-source="paper">Table 1 lists costs after division by V</cite>. The margin of a row is one minus its power of $p$. The paper fixes <cite data-source="paper">κ = 2−182</cite>, and the smallest margin among the seven dominant rows is <cite data-source="paper">Thus mini gi = 2−181 = 2κ</cite>. So each dominant row has a power of $p$ at most $1-2\kappa$. Since $V=\Theta(n)$ and $p=\Theta(\lg n)$, such a row costs $O(n(\lg n)^{1-2\kappa})$, which lies within $O(n(\lg n)^{1-\kappa})$ for $\lg n\ge 1$.

The main theorem claims that the algorithm <cite data-source="paper">multiplies two n-bit integers in O(n(lg n)1−κ ) worstcase time</cite>. Every term of the cost table is therefore $O(n(\lg n)^{1-\kappa})$, which gives that bound.
