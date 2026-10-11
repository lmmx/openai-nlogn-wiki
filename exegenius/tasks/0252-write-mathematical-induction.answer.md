Mathematical induction is a proof method that establishes a statement for every nonnegative [integer](integer.md) $t$, the step index, which counts the recursion levels passed, by proving two facts. The base case shows that the statement holds for $t=0$. The inductive step shows that if the statement holds for some $t$, it also holds for $t+1$.

The method matters for the target because the [rank-saving recursion](rank-saving-recursion.md) bounds the cost of one level, and a bound must hold at every level before it yields a saving over the whole recursion. Induction over the level index is what carries the per-level bound through all levels.

Let $q>0$ be a fixed real number, the ratio by which one level may multiply a bound. Let $g_t \ge 0$ be a bound on the cost after $t$ levels, with $g_0=1$ and $g_{t+1} \le q\,g_t$ for every $t\ge 0$. The claim is $g_t \le q^t$ for every $t \ge 0$.

Base case: $g_0 = 1 = q^0$.

Inductive step: assume $g_t \le q^t$. Then $g_{t+1} \le q\,g_t \le q \cdot q^t = q^{t+1}$. The second inequality multiplies the assumed bound by $q>0$, which preserves the inequality. So the claim holds for $t+1$. By induction, it holds for every $t \ge 0$.

In the paper, the ratio is the one defined on the rank-saving recursion page: the recursive contribution is scaled by a fixed ratio at each level, <cite data-source="paper">recursive contribution by s/W < m.</cite> With the toy values from that page, the ratio is $q=1.5$, so the bound after three levels is $g_3 \le 1.5^3 = 3.375$. The example drops the linear work per level, so it shows only the ratio step of the argument.
