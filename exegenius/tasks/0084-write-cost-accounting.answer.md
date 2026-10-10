Cost accounting checks that the [multiplication algorithm](multiplication-algorithm.md) meets the claimed time bound. The paper writes every cost as a multiple of the stored volume $V = Tp = \Theta(n)$, using the [normalized cost](normalized-cost.md) of each operation. Each normalized cost is a fixed constant times a power of $p$ with an exponent depending on $\epsilon$, $c$, $\tau$, $\lambda'$, $\delta$.

Table 1 of the paper lists these normalized costs for the operations in the algorithm: prefix-slot moves and butterfly rounds, chunk exchanges for the transform layout, simultaneous butterfly rounds, CRT and axis layouts, Gaussian line maps, chirps and twists, packed polynomial products, final scaling, and input and output. Most rows are a power of $p$ with an exponent less than one, and two rows are logarithmic or constant.

The bound holds because every dominant exponent in the table falls below one by a margin. The paper names seven dominant margins $g_1, \dots, g_7$:

$$g_1 = 1 - \epsilon(1+c), \quad g_2 = \epsilon c (1-\tau), \quad g_3 = \epsilon(1 - \lambda'), \quad g_4 = 1 - \tau - \epsilon(2-\tau), \quad g_5 = \tfrac14 - \delta - \tfrac32\epsilon, \quad g_6 = 1 - \delta - \epsilon, \quad g_7 = \epsilon.$$

With the chosen constants, $g_2 = 2^{-75} \cdot 2^{-56} \cdot 2^{-50} = 2^{-181}$ and $g_3 = 2^{-129}$, and the others are larger. So the smallest margin is $2^{-181} = 2\kappa$.

The paper states that this explicit slack covers any remaining fixed power of $\log p$. Since $V = \Theta(n)$ and $p = \Theta(\lg n)$, where $\lg n = \log_2 n$, the total cost is $O(n(\lg n)^{1-\kappa})$, which is the stated bound.

The exponents come from the operations themselves. For example, the chunk exchanges use the [address-field interchange](address-interchange.md) cost $O(V u^{\tau})$, and the simultaneous rounds use the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) cost $O(V d^{\lambda'})$. The [recursive rank saving](rank-saving-recursion.md) is what keeps the recursive rows below the trivial bound. The choice of constants in the [parameter choice](parameter-choice.md) is what makes each margin positive.
