The tensor product of two matrices is the block matrix formed by scaling copies of one by the entries of the other. It lets one operator act on several address coordinates at once, which is the step the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) relies on.

The tensor product is built from matrices, the basic objects of [Linear algebra basics](linear-algebra-basics.md). Let $P=(p_{ij})$ be a matrix, with $p_{ij}$ its entry in row $i$ and column $j$, where $i$ and $j$ index rows and columns here. Let $Q$ be a second matrix (here $Q$ is a matrix, not the ring of other pages). The tensor product $P\otimes Q$, also called the Kronecker product, is the block matrix whose block in block-row $i$ and block-column $j$ is $p_{ij}Q$. Each entry of $P$ scales a full copy of $Q$.

For example, take $P=\begin{array}{rr}1&1\\1&-1\end{array}$. Then

$$P\otimes P=\begin{array}{rrrr}1&1&1&1\\1&-1&1&-1\\1&1&-1&-1\\1&-1&-1&1\end{array}.$$

Here $m$ is the number of factors in a tensor power, which is also the number of coordinates the operator acts on. The power is defined by $P^{\otimes 1}=P$ and $P^{\otimes m}=P\otimes P^{\otimes(m-1)}$. An address on $m$ coordinates is a bit string $t=(t_1,\dots,t_m)\in\{0,1\}^m$, where $t_i$ is the bit at coordinate $i$. For a function $f$ on such addresses (here $f$ is not the modulus polynomial), $P^{\otimes m}$ maps $f$ to the function whose value at an output address $s=(s_1,\dots,s_m)\in\{0,1\}^m$, with bit $s_i$ at coordinate $i$, is

$$(P^{\otimes m}f)(s)=\sum_{t\in\{0,1\}^m}\Big(\prod_{i=1}^{m}p_{s_i t_i}\Big)f(t).$$

Each factor $p_{s_i t_i}$ involves only coordinate $i$, so $P^{\otimes m}$ transforms each coordinate by $P$ independently.

The mixed-product rule turns this into a sequence of single-coordinate steps. For matrices of compatible sizes,

$$(P\otimes Q)(P'\otimes Q')=(PP')\otimes(QQ').$$

To check it, the entry in row $(a,b)$ and column $(c,d)$ of the left side is $\sum_e\sum_g p_{ae}q_{bg}\,p'_{ec}q'_{gd}=\big(\sum_e p_{ae}p'_{ec}\big)\big(\sum_g q_{bg}q'_{gd}\big)$, where $e$ and $g$ are summation indices. This is the entry of the right side. If $P$ and $Q$ are invertible, taking $P'=P^{-1}$ and $Q'=Q^{-1}$ gives $(P\otimes Q)(P^{-1}\otimes Q^{-1})=I\otimes I=I$, so $(P\otimes Q)^{-1}=P^{-1}\otimes Q^{-1}$.

Let $P_{(i)}$ apply $P$ to coordinate $i$ and the identity to the others. Repeated use of the rule gives $P_{(1)}P_{(2)}\cdots P_{(m)}=P^{\otimes m}$. So $P^{\otimes m}$ is the same as applying $P$ to coordinate 1, then to coordinate 2, and so on, one coordinate at a time.

The paper uses the same construction. On $k$ columns (its $k$ counts the columns), each frame and edge operator is <cite data-source="paper">then the tensor product of its one-column version over these k coordinates.</cite> It states the product rule as <cite data-source="paper">Taking tensor products preserves their product</cite>.

The tensor product takes its one-coordinate factor from the [two-point butterfly map](butterfly.md) $H_0$, whose matrix is $\tfrac12 P$. So a two-point operator on a selected bit is $\tfrac12 P$ acting on that bit, with the other bits left fixed. The paper states the layer as <cite data-source="paper">The intended operation is the tensor product of</cite> this operator on each selected bit. The whole layer is therefore the single operator $(\tfrac12 P)^{\otimes m}$, applied in one pass rather than one bit at a time.
