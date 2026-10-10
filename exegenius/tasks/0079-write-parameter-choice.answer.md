The algorithm has several size parameters that depend on the input length $n$. They are chosen so that every term in the cost table fits the target bound. Here $\lg n = \log_2 n$ is the base-2 logarithm. The cost table lists the normalized cost of each operation, as explained on the [normalized cost](normalized-cost.md) page, and the [cost accounting](cost-accounting.md) page checks it. The rules, for sufficiently large $n$, are:

- $b = \lceil \log_2 n \rceil$ and $p = 6b$, so $p = \Theta(\lg n)$ is the working precision.
- $d = \lfloor b^{\epsilon} \rfloor$ and $K = \lfloor d^{c} \rfloor$, where $\epsilon$ and $c$ are fixed rational constants.
- $T$ is the power of two in $[4n/b,\ 8n/b)$, and $r = 2^{\lceil (\log_2 T)/d \rceil}$.
- The $d$ axis lengths $t_i \in \{r/2, r\}$ satisfy $\prod_i t_i = T$, with the last axis $t_d = r$.

The fixed constants are $\epsilon = 2^{-75}$, $c = 2^{-56}$, $\tau = \sigma = 1 - 2^{-50}$, $\lambda = 1 - 2^{-52}$, $\lambda' = 1 - 2^{-54}$, $\delta = 1/16$, and $\kappa = 2^{-182}$. The paper calls these deliberately conservative and claims no optimization.

Because $\epsilon$ is so small, the choice of $d$ has a striking consequence. $d = \lfloor b^{\epsilon} \rfloor$ is at least $2$ only when $b^{\epsilon} \ge 2$, that is, when $b \ge 2^{1/\epsilon} = 2^{2^{75}}$. For all smaller inputs the algorithm uses $d = 1$. This does not contradict the theorem, which is asymptotic, but it shows that the stated constants only take effect for astronomically large $n$.

The paper's key estimates are $T p = \Theta(n)$, $d = \Theta(p^{\epsilon})$, and $r = 2^{\Theta(p^{1-\epsilon})}$. These are what let the cost accounting hold.

The sizes $T$ and $r$ are the transform lengths used by the [multiplication algorithm](multiplication-algorithm.md). The axis lengths $t_i$ are the lengths produced by the [Chinese-remainder address map](chinese-remainder-map.md), and the precision $p$ is the one whose rounding errors are bounded in [precision and exact recovery](precision-and-rounding.md). The number of axes of length $r/2$ is set so that the $t_i$ multiply to exactly $T$.
