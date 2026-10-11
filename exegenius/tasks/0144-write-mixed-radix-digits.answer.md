Mixed-radix digits are the place-value digits of an integer in a positional system where each place has its own length, so the digit at each place ranges over that place's length rather than over one common base. The [Chinese-remainder map](chinese-remainder-map.md) uses these digits to give each coefficient position a coordinate on each axis.

Fix a number $\beta$ of places, a positive integer, and lengths $\lambda_1, \dots, \lambda_\beta$, each a positive integer.

The place index $j$ runs from $1$ to $\beta$ and names a place; on this page it does not carry the meaning of the index on earlier pages. Here $\lambda_j$ is the length of place $j$, the number of values its digit can take.

Let $\Lambda = \lambda_1\lambda_2\cdots\lambda_\beta$ be the product of the lengths, the number of distinct digit strings the system can write.

The place value of place $j$ is $w_j = \lambda_1\lambda_2\cdots\lambda_{j-1}$, the product of the lengths of the places below it, with $w_1 = 1$.

Let $\nu$ be an integer with $0 \le \nu < \Lambda$, the integer being written. The digit $e_j$ at place $j$ is an integer with $0 \le e_j < \lambda_j$, the digit of the expansion at that place. A mixed-radix expansion of $\nu$ is a tuple of digits $e_1, \dots, e_\beta$ such that

$$\nu = \sum_{j=1}^{\beta} e_j\, w_j.$$

Every such $\nu$ has exactly one mixed-radix expansion. The source states this for the coefficient indices of its layout: <cite data-source="paper">Every ordinary coefficient index has a unique mixed-radix expression</cite>.

The proof uses the telescoping identity $\sum_{i<j}(\lambda_i-1)w_i = w_j - 1$, which holds because $(\lambda_i-1)w_i = w_{i+1}-w_i$. Suppose two expansions differ, and let $j$ be the largest place where their digits differ. The difference of their values is $(e_j-e_j')w_j$ plus a sum over $i<j$ whose absolute value is at most $\sum_{i<j}(\lambda_i-1)w_i = w_j-1 < w_j$, so the difference is nonzero. Hence distinct digit tuples give distinct values. The largest possible value of $\sum_j e_j w_j$ is $\sum_j(\lambda_j-1)w_j = w_{\beta+1}-1 = \Lambda-1$, so the $\Lambda$ digit tuples give $\Lambda$ distinct values in $\{0,\dots,\Lambda-1\}$, and every $\nu$ in that range is reached exactly once.

For example, take $\beta = 2$, $\lambda_1 = 3$ and $\lambda_2 = 4$. Then $\Lambda = 12$, $w_1 = 1$ and $w_2 = 3$. For $\nu = 7$, the digits are $e_1 = 1$ and $e_2 = 2$, since $1\cdot 1 + 2\cdot 3 = 7$. For $\nu = 11$, the digits are $e_1 = 2$ and $e_2 = 3$, since $2 + 3\cdot 3 = 11$. When every length is $2$ this is the binary expansion, and when every length is $b$ it is the base-$b$ expansion.
