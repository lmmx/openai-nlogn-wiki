The tensor product of two matrices is the block matrix formed by scaling copies of one by the entries of the other. Its $J$-fold power, where $J$ is the number of factors, applies one operator to $J$ coordinates at once, which is the step the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) relies on.

The tensor product is built from matrices, the basic objects of [Linear algebra basics](linear-algebra-basics.md). Let $P$ be a matrix, with row index $\xi$ and column index $\sigma$, so $p_{\xi\sigma}$ is its entry in row $\xi$ and column $\sigma$. Let $Q$ be a second matrix, with row index $\upsilon$ and column index $\zeta$, so $q_{\upsilon\zeta}$ is its entry in row $\upsilon$ and column $\zeta$. The tensor product $P\otimes Q$, also called the Kronecker product, is the block matrix whose block in block-row $\xi$ and block-column $\sigma$ is $p_{\xi\sigma}Q$. Its rows are indexed by pairs $(\xi,\upsilon)$ and its columns by pairs $(\sigma,\zeta)$, so the entry in row $(\xi,\upsilon)$ and column $(\sigma,\zeta)$ is $p_{\xi\sigma}q_{\upsilon\zeta}$.

For example, with $P=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$,

$$P\otimes P=\begin{pmatrix}1&1&1&1\\1&-1&1&-1\\1&1&-1&-1\\1&-1&-1&1\end{pmatrix}.$$

For $J\ge 1$, the $J$-fold tensor power is defined by $P^{\otimes 1}=P$ and $P^{\otimes J}=P\otimes P^{\otimes(J-1)}$, where $J$ is the number of factors and of coordinates acted on. For $2\times 2$ matrices, indices run over $0$ and $1$. Here an address on $J$ coordinates is a bit string $\sigma=(\sigma_1,\dots,\sigma_J)\in\{0,1\}^J$ whose bit at coordinate $l$ is $\sigma_l$, with $l$ running from $1$ to $J$, and $\xi=(\xi_1,\dots,\xi_J)$ is an output address of the same form. For a function $\Psi:\{0,1\}^J\to\mathbb{C}$ on addresses, $P^{\otimes J}$ maps $\Psi$ to the function whose value at $\xi$ is

$$(P^{\otimes J}\Psi)(\xi)=\sum_{\sigma\in\{0,1\}^J}\Big(\prod_{l=1}^{J}p_{\xi_l\sigma_l}\Big)\Psi(\sigma).$$

Each factor $p_{\xi_l\sigma_l}$ involves only coordinate $l$, so $P^{\otimes J}$ transforms each coordinate by $P$ independently.

For second matrices $P'$ and $Q'$ of compatible sizes, with entries $p'_{W\sigma}$ and $q'_{Y\zeta}$ in rows $W$ and $Y$, the mixed-product rule is

$$(P\otimes Q)(P'\otimes Q')=(PP')\otimes(QQ').$$

The entry in row $(\xi,\upsilon)$ and column $(\sigma,\zeta)$ of the left side, summing over the middle indices $W$ and $Y$, is

$$\sum_{W}\sum_{Y}p_{\xi W}\,q_{\upsilon Y}\,p'_{W\sigma}\,q'_{Y\zeta}=\Big(\sum_{W}p_{\xi W}p'_{W\sigma}\Big)\Big(\sum_{Y}q_{\upsilon Y}q'_{Y\zeta}\Big),$$

matching the entry of $(PP')\otimes(QQ')$. If $P$ and $Q$ are invertible, taking $P'=P^{-1}$ and $Q'=Q^{-1}$ gives $(P\otimes Q)(P^{-1}\otimes Q^{-1})=I\otimes I=I$, so $(P\otimes Q)^{-1}=P^{-1}\otimes Q^{-1}$.

Let $P_{(l)}$ apply $P$ to coordinate $l$ and the identity to the others, so $P_{(l)}=I\otimes\cdots\otimes P\otimes\cdots\otimes I$ with $P$ in place $l$. Then $P_{(1)}P_{(2)}\cdots P_{(J)}=P^{\otimes J}$. By induction on $J$, the product $P_{(2)}\cdots P_{(J)}$ equals $I\otimes P^{\otimes(J-1)}$. Since $P_{(1)}=P\otimes I^{\otimes(J-1)}$, the mixed-product rule gives $(P\otimes I^{\otimes(J-1)})(I\otimes P^{\otimes(J-1)})=P\otimes P^{\otimes(J-1)}=P^{\otimes J}$.

The paper uses the same construction for an operator on several columns: <cite data-source="paper">the tensor product of its one-column version</cite>, taken over the coordinates of those columns. It states the product rule as <cite data-source="paper">Taking tensor products preserves their product</cite>, which is the mixed-product rule above.

The tensor product takes its one-coordinate factor from the [Butterfly](butterfly.md) map $H_0$, which replaces a pair of values by its half-sum and half-difference. Its matrix is $\tfrac12 P$. The paper states the layer as <cite data-source="paper">The intended operation is the tensor product of</cite> this operator on each selected bit. Here $J$ is the number of selected bits. Applying $\tfrac12 P$ to bit $l$ gives $\tfrac12 P_{(l)}$, so the layer is $(\tfrac12 P)_{(1)}\cdots(\tfrac12 P)_{(J)}$, which equals $(\tfrac12 P)^{\otimes J}$ by the identity above. This single operator acts on the $J$ selected bits and leaves the others fixed, and the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) applies it in one pass rather than one bit at a time.
