The Iverson bracket turns a condition into the number 1 or 0, so that a count of cases becomes a sum of ordinary numbers. The [rank-saving recursion](rank-saving-recursion.md) uses it to write the number of smaller calls as such a sum, which is what makes the total number of calls bounded below the rank.

## Definition

Here $\sigma$ stands for a condition, a statement that is either true or false.

For such a condition, the bracket $[\sigma]$ is defined by

$$[\sigma]=\begin{cases}1 & \text{if } \sigma \text{ holds},\\ 0 & \text{if } \sigma \text{ fails}.\end{cases}$$

## Counting with sums

A bracket turns a yes-or-no test into an arithmetic term. Take the condition "$k$ is even" with the counter $k$ running over $1, 2, 3, 4, 5$:

$$\sum_{k=1}^{5} [k \text{ is even}] = 0+1+0+1+0 = 2.$$

The sum equals the number of values of $k$ for which the condition holds. In general, if $\sigma_k$ is a condition for each $k$ in a finite range, the number of indices $k$ with $\sigma_k$ true is $\sum_k [\sigma_k]$.

Brackets also combine by multiplication. The product $[\sigma][\tau]$ is 1 exactly when both $\sigma$ and $\tau$ hold, because it is $1 \cdot 1 = 1$ in that case and is $0$ whenever either factor is $0$.
