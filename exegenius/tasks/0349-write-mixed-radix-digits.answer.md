Mixed-radix digits are the place-value digits of an integer in a positional system where each place has its own length, so the digit at each place ranges over that place's length rather than over one common base. The [Chinese-remainder map](chinese-remainder-map.md) uses these digits to give each coefficient position a coordinate on each axis.

Fix a positive integer $\beta$, the number of places, and positive integers $\lambda_1, \dots, \lambda_\beta$. The place index $j$ runs from $1$ to $\beta$ and names a place. Here $\lambda_j$ is the length of place $j$, the number of values the digit at place $j$ can take. Several letters on this page have other meanings on earlier pages; here each has only the meaning given in its definition.

Let $\Lambda = \lambda_1\lambda_2\cdots\lambda_\beta$ be the product of the lengths, the number of distinct digit strings the system can write. The place value of place $j$ is $w_j = \lambda_1\lambda_2\cdots\lambda_{j-1}$, the product of the lengths of the places below it, with $w_1 = 1$.

Let $\nu$ be an integer with $0 \le \nu < \Lambda$, the integer being written. The digit $e_j$ at place $j$ is an integer with $0 \le e_j < \lambda_j$, the digit of the expansion at that place. A mixed-radix expansion of $\nu$ is a tuple $(e_1, \dots, e_\beta)$, an ordered list of digits, such that

$$\nu = \sum_{j=1}^{\beta} e_j\, w_j.$$

Every such $\nu$ has exactly one mixed-radix expansion. Here $i$ is a place index that runs over the places below $j$. Uniqueness of the expansion is based on the [Telescoping identity](telescoping-identity.md), which gives $\sum_{i<j}(\lambda_i-1)w_i = w_j - 1$ for every place $j$, since $(\lambda_i-1)w_i = w_{i+1}-w_i$.

Suppose two expansions $(e_1,\dots,e_\beta)$ and $(e'_1,\dots,e'_\beta)$ of the same $\nu$ differ, where $e'_j$ is the digit at place $j$ of the second expansion, and let $j$ be the largest place where their digits differ. Each digit at place $i$ lies in $[0,\lambda_i)$, so $|e_i-e'_i| \le \lambda_i-1$. The digits agree above $j$, so the difference of the two values is $\sum_{i\le j}(e_i-e'_i)w_i$. Its term at $j$ has absolute value at least $w_j$, while the places below $j$ contribute at most $\sum_{i<j}(\lambda_i-1)w_i = w_j-1$. The difference is therefore at least $1$ in absolute value, which contradicts both expansions giving $\nu$. Distinct digit tuples give distinct values.

The largest value a tuple gives is obtained by taking $e_j = \lambda_j-1$ at every place, which gives $\sum_j(\lambda_j-1)w_j = w_{\beta+1}-w_1 = \Lambda-1$ by the same identity, since $w_{\beta+1} = \lambda_1\cdots\lambda_\beta = \Lambda$. There are $\Lambda$ digit tuples, and they give $\Lambda$ distinct values in $\{0,\dots,\Lambda-1\}$. So every $\nu$ in that range is reached by exactly one tuple.

For example, take $\beta = 2$, $\lambda_1 = 3$ and $\lambda_2 = 4$. Then $\Lambda = 12$, $w_1 = 1$ and $w_2 = 3$. For $\nu = 7$, the digits are $e_1 = 1$ and $e_2 = 2$, since $1\cdot 1 + 2\cdot 3 = 7$. For $\nu = 11$, the digits are $e_1 = 2$ and $e_2 = 3$, since $2 + 3\cdot 3 = 11$. When every length is $2$ this is the binary expansion, and when every length is $b$ it is the base-$b$ expansion.
