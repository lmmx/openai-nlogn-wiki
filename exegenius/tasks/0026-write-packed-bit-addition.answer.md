Packed selected-bit addition is a fixed multitape procedure that performs many binary row additions in one pass. It supplies the binary basis changes for the [simultaneous butterfly layer](simultaneous-butterfly-layer.md), whose exact computation needs them.

A binary row addition adds one row of a matrix into another in every column, so it changes the selected bits of two whole address chunks at once. The procedure performs the XORs of one such addition together, rather than one bit position at a time.

The record's address is split into three chunks, named $x$, $y$, and $z$; in this page these letters name chunks, so $y$ no longer means the polynomial variable. Each chunk is $L$ bits wide, with $L = fK$, where $f$ is the number of selected positions in each chunk and $K$ is the spacing between them.

The selected positions start at offset $\rho$, with $0 \le \rho < K$. The $i$-th selected position is $j_i = \rho + iK$ for $0 \le i < f$, counted from the least significant bit. The procedure computes

$$y_{j_i} \leftarrow y_{j_i} \oplus x_{j_i} \qquad (0 \le i < f),$$

so the selected bits of $x$ are XORed into the same positions of $y$, where $\oplus$ is exclusive or.

For example, take $f=2$, $K=6$, $L=12$ and $\rho=1$, so the selected positions are $j_0=1$ and $j_1=7$. If the $x$ bits there are $1$ and $0$, and the $y$ bits are $1$ and $1$, the procedure leaves the $y$ bits as $0$ and $1$.

The construction applies a constant number of cyclic shifts of whole chunk ranges, and these shifts have the required effect away from a small set of addresses. The procedure then corrects exactly that set. The construction is built from three streaming operations: an [address-field interchange](address-interchange.md) of equal-width chunks, cyclic shifts of chunk ranges, and a fixed permutation of two-bit values. It is a restricted form of the [address shear](address-shear.md) that changes only the selected positions.

The correction term in the time is scaled by $\delta_{\text{bad}} = \min\{1, 80(f-1)2^{-K}\}$, which is small when $K$ is large.

Each record has $R$ bits, a bit count distinct from the coefficient count $r$. Let $N_0,\dots,N_3$ be the sizes of the four other coordinate ranges, so $M = 2^{3L}N_0N_1N_2N_3$ counts the records, and $V = MR$ is the total number of bits. Here $\tau$ is a fixed exponent with $0<\tau<1$. Under the asymptotic conditions of the lemma, the time is $O(V(L^\tau+1))$ <cite data-source="paper">When Arect = O(p), R exceeds every fixed polynomial in p, f ≤ d ≤ p, and K/ log p → ∞, this is O(V (Lτ + 1))</cite>.
