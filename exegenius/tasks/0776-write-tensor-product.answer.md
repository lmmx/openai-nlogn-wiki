The tensor product is the operation that builds one large matrix out of two small ones, and its power applies one operator to several coordinates at once. The [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) needs exactly this, because it transforms several selected address bits in one pass.

The tensor product is built from matrices, the basic objects of [Linear algebra basics](linear-algebra-basics.md). Let $P$ be a matrix with rows indexed by $\upsilon$ and columns indexed by $\varrho$, so $p_{\upsilon\varrho}$ is its entry in row $\upsilon$ and column $\varrho$. Let $Q$ be a second matrix with rows indexed by $\varpi$ and columns indexed by $\varsigma$, so $q_{\varpi\varsigma}$ is its entry in row $\varpi$ and column $\varsigma$. A block matrix is a matrix cut into rectangular blocks, each of which is itself a matrix. The tensor product $P\otimes Q$, also called the Kronecker product, is the block matrix whose block in block-row $\upsilon$ and block-column $\varrho$ is $p_{\upsilon\varrho}Q$. Its rows are indexed by pairs $(\upsilon,\varpi)$ and its columns by pairs $(\varrho,\varsigma)$, so the entry in row $(\upsilon,\varpi)$ and column $(\varrho,\varsigma)$ is $p_{\upsilon\varrho}\,q_{\varpi\varsigma}$.

For example, take $P=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, whose indices run over $0$ and $1$. Then

$$P\otimes P=\begin{pmatrix}1&1&1&1\\1&-1&1&-1\\1&1&-1&-1\\1&-1&-1&1\end{pmatrix}.$$

The rows and columns are listed in the order $(0,0),(0,1),(1,0),(1,1)$. The entry in row $(1,0)$ and column $(1,1)$ is $p_{11}\,q_{00}=(-1)(1)=-1$, which is the last entry of the third row.

The $\Upsilon$-fold tensor power, where $\Upsilon\ge 1$ is a count, the number of factors and of coordinates acted on, is defined by $P^{\otimes 1}=P$ and $P^{\otimes\Upsilon}=P\otimes P^{\otimes(\Upsilon-1)}$. Each factor acts on its own coordinate, so $P^{\otimes\Upsilon}$ transforms each of the $\Upsilon$ coordinates by $P$ independently.

For second matrices $P'$ and $Q'$ of compatible sizes, let $P'$ have rows indexed by $\varrho$ and columns indexed by $\vartheta$, so $p'_{\varrho\vartheta}$ is its entry in row $\varrho$ and column $\vartheta$, and let $Q'$ have rows indexed by $\varsigma$ and columns indexed by $\Psi$, so $q'_{\varsigma\Psi}$ is its entry in row $\varsigma$ and column $\Psi$. The mixed-product rule is

$$(P\otimes Q)(P'\otimes Q')=(PP')\otimes(QQ').$$

The entry in row $(\upsilon,\varpi)$ and column $(\vartheta,\Psi)$ of the left side is a sum over the indices shared by the two products, $\varrho$ and $\varsigma$:

$$\sum_{\varrho}\sum_{\varsigma}p_{\upsilon\varrho}\,q_{\varpi\varsigma}\,p'_{\varrho\vartheta}\,q'_{\varsigma\Psi}=\Big(\sum_{\varrho}p_{\upsilon\varrho}\,p'_{\varrho\vartheta}\Big)\Big(\sum_{\varsigma}q_{\varpi\varsigma}\,q'_{\varsigma\Psi}\Big),$$

which is the entry of $(PP')\otimes(QQ')$ in the same row and column. The sum factors into one sum for each product, which is why the rule holds.

If $P$ and $Q$ are invertible, taking $P'=P^{-1}$ and $Q'=Q^{-1}$ gives $(P\otimes Q)(P^{-1}\otimes Q^{-1})=I\otimes I=I$, where $I$ is the identity matrix. Hence $(P\otimes Q)^{-1}=P^{-1}\otimes Q^{-1}$.

For a coordinate position $\phi$ with $1\le\phi\le\Upsilon$, let $P_{(\phi)}$ apply $P$ to coordinate $\phi$ and the identity to the others, so $P_{(\phi)}=I\otimes\cdots\otimes P\otimes\cdots\otimes I$ with $P$ in place $\phi$. Then

$$P_{(1)}P_{(2)}\cdots P_{(\Upsilon)}=P^{\otimes\Upsilon}.$$

By induction on $\Upsilon$, $P_{(2)}\cdots P_{(\Upsilon)}=I\otimes P^{\otimes(\Upsilon-1)}$. Since $P_{(1)}=P\otimes I^{\otimes(\Upsilon-1)}$, the mixed-product rule gives $(P\otimes I^{\otimes(\Upsilon-1)})(I\otimes P^{\otimes(\Upsilon-1)})=P\otimes P^{\otimes(\Upsilon-1)}=P^{\otimes\Upsilon}$.

The paper uses the same construction for an operator on several columns: <cite data-source="paper">the tensor product of its one-column version</cite>, taken over the coordinates of those columns. It states the product rule as <cite data-source="paper">Taking tensor products preserves their product</cite>, which is the mixed-product rule above.

The tensor product takes its one-coordinate factor from the [Butterfly](butterfly.md) map $H_0$, which replaces a pair of values by its half-sum and half-difference. Its matrix is $\tfrac12 P$, since $H_0(u,v)=\big(\tfrac12(u+v),\tfrac12(u-v)\big)$ is $\tfrac12 P$ applied to the pair $(u,v)$. The paper states the layer as <cite data-source="paper">The intended operation is the tensor product of</cite> this operator on each selected bit. Here $\Upsilon$ is the number of selected bits. Applying $\tfrac12 P$ to bit $\phi$ gives $\tfrac12 P_{(\phi)}$, so the layer is $(\tfrac12 P)_{(1)}\cdots(\tfrac12 P)_{(\Upsilon)}$, which equals $(\tfrac12 P)^{\otimes\Upsilon}$ by the factorization above with $\tfrac12 P$ in place of $P$. This single operator acts on the $\Upsilon$ selected bits and leaves the others fixed, so the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) applies it in one pass rather than one bit at a time.
