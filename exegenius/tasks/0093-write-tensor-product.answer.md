Here $m$ is the number of factors in a tensor power, which is also the number of coordinates that the operator acts on.

The tensor product combines linear maps on separate coordinates into one linear map on their joint address space. The page uses it to apply one two-point operator to several selected bits in a single pass, which is the step that the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) relies on.

The tensor product is built from matrices, the basic objects of [Linear algebra basics](linear-algebra-basics.md). Let $P=(p_{ij})$ be a matrix, with $p_{ij}$ its entry in row $i$ and column $j$. Let $Q$ be a second matrix. The tensor product $P\otimes Q$, also called the Kronecker product, is the block matrix whose block in block-row $i$ and block-column $j$ is $p_{ij}Q$. Each entry of $P$ scales a full copy of $Q$.

For example, take $P=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$. Then

$$P\otimes P=\begin{pmatrix}1&1&1&1\\1&-1&1&-1\\1&1&-1&-1\\1&-1&-1&1\end{pmatrix}.$$

The upper-left $2\times 2$ block is $1\cdot P$, and the lower-right block is $-1\cdot P$.

The $m$-fold tensor power $P^{\otimes m}$ is the product of $m$ copies of $P$, defined by $P^{\otimes 1}=P$ and $P^{\otimes m}=P\otimes P^{\otimes(m-1)}$. Each coordinate of an address is an element of the binary field, so an $m$-coordinate address is a bit string $t=(t_1,\dots,t_m)\in\{0,1\}^m$. For the $2\times 2$ matrix $P$ above, $P^{\otimes m}$ is a $2^m\times 2^m$ matrix, and it acts on a function $f$ on addresses by

$$(P^{\otimes m}f)(s)=\sum_{t\in\{0,1\}^m}\Big(\prod_{i=1}^{m}p_{s_i t_i}\Big)f(t).$$

The product over $i$ shows that coordinate $i$ of the address is transformed by $P$ and that the coordinates do not interact. One application of $P^{\otimes m}$ therefore gives the same result as applying $P$ to coordinate 1, then to coordinate 2, and so on up to coordinate $m$, but as a single operator.

This is the form in which the paper writes operators on several coordinates: <cite data-source="paper">then the tensor product of its one-column version over these k coordinates.</cite>

Two standard facts are used repeatedly. The product of two tensor products is the tensor product of the two products, and the inverse of an invertible tensor product is the tensor product of the inverses. The paper states the first in the form <cite data-source="paper">Taking tensor products preserves their product</cite>, so a product of such operators on several coordinates can be computed one coordinate-wise factor at a time.

The butterfly layer on several selected bits has this form. Its intended operation is <cite data-source="paper">The intended operation is the tensor product of</cite> the two-point butterfly map on each selected bit, so the whole layer is one operator $P^{\otimes m}$ on the selected coordinates, applied in one pass.
