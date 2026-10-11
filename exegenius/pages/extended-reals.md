The extended real numbers are the real numbers with two added values, positive infinity and negative infinity. The main argument's cost table, with every term $O(n(\lg n)^{1-\kappa})$, uses limit inferiors. A limit inferior is the limit of the infima of the tails of a sequence, where a tail is what remains from some position on.

Here $+\infty$ exceeds every real number and $-\infty$ is below every real number. Let $\mathbb{R}$ denote the set of real numbers, and let $\overline{\mathbb{R}}$ denote the set $\mathbb{R}\cup\{-\infty,+\infty\}$ of extended real numbers. Here $\sigma$ denotes a real number, not a term of a sequence. The order extends with $-\infty < \sigma < +\infty$ for every real number $\sigma$, and $-\infty < +\infty$.

Let $S$ denote any set of extended real numbers. Its infimum is the greatest extended real number at most every element of $S$, and its supremum the least at least every element of $S$.

Let $F$ be the set of real elements of $S$. If $S$ contains $+\infty$, or $F$ has no real upper bound, the supremum is $+\infty$. If $F$ is empty, it is $-\infty$. Otherwise $F$ has a least real upper bound $b$, because the reals are complete. Every extended upper bound of $S$ is at least $b$, so $b$ is the supremum. The infimum is $\inf S = -\sup(-S)$, where $-S$ negates each element of $S$.

A sequence of extended real numbers has terms $\tau_\delta$ for $\delta = 1,2,3,\dots$, where $\delta$ is the position of a term in the sequence. The sequence is nondecreasing when each term is at least the one before it. Here $L$ is a point of $\overline{\mathbb{R}}$. A sequence has limit $L$ when, for every real $\sigma < L$, the terms eventually exceed $\sigma$, and for every real $\sigma > L$, they eventually fall below $\sigma$.

Every nondecreasing sequence has a limit, and that limit is its supremum. Let $L$ be the supremum of the terms. Every term is at most $L$. For a real $\sigma < L$, $\sigma$ is not an upper bound of the terms, so some term exceeds $\sigma$, and every later term does too.

The limit inferior of a sequence $\tau_\delta$ is the limit of its tail infima as $\delta$ grows. Here $\delta'$ is a dummy position index that ranges over the positions at or after $\delta$, so the tail infimum is $\inf\{\tau_{\delta'} : \delta' \ge \delta\}$. Tail infima do not decrease as $\delta$ grows, so their limit exists.

For example, take $\tau_\delta = \delta$. The tail infima equal $\delta$, which grows without bound, so their limit is $+\infty$. Now take $\tau_\delta = (-1)^\delta \delta$. Every tail reaches arbitrarily large negative odd positions, so every tail infimum is $-\infty$, and the limit is $-\infty$.

Sums and products extend in the obvious way, except that $(+\infty) + (-\infty)$ and $0 \cdot (+\infty)$ are left undefined.
