Mathematical induction is a proof method that establishes a statement for every nonnegative [integer](integer.md) $t$, the step index, which counts the recursion levels passed, by proving two facts. The base case shows that the statement holds for $t=0$. The inductive step shows that if the statement holds for some $t$, it also holds for $t+1$.

The method is used for the target, the main theorem of the paper *Integer multiplication below n log n* (OpenAI, 2026), which bounds the running time of exact multiplication below $n\log n$. The paper's [rank-saving recursion](rank-saving-recursion.md) multiplies the recursive contribution by a fixed factor at each level. The paper calls that factor $s/W$, where $s$ is the number of smaller calls and $W$ is the wire count: <cite data-source="paper">recursive contribution by s/W < m.</cite> The strict inequality $s/W<m$ gives the power saving. Each level's bound must be carried to the next level, and induction over the level index does this.

Let $q>0$ be a fixed real number, the ratio by which one level may multiply a bound. Let $g_t \ge 0$ be a bound on the cost after $t$ levels, with $g_0=1$ and $g_{t+1} \le q\,g_t$ for every $t\ge 0$. The claim is $g_t \le q^t$ for every $t \ge 0$.

Base case: $g_0 = 1 = q^0$.

Inductive step: assume $g_t \le q^t$. Then $g_{t+1} \le q\,g_t \le q \cdot q^t = q^{t+1}$. The second inequality multiplies the assumed bound by $q>0$, which preserves the inequality. So the claim holds for $t+1$. By induction, it holds for every $t \ge 0$.

For example, take $q=1.5$. Then $g_1 \le 1.5$, $g_2 \le 1.5^2 = 2.25$, and $g_3 \le 1.5^3 = 3.375$. Each bound follows from the previous one by one application of $g_{t+1} \le q\,g_t$.
