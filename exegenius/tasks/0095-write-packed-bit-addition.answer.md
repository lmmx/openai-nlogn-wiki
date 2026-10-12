Packed selected-bit addition is a fixed multitape procedure that performs many binary row additions in one pass. Packed selected-bit addition supplies the binary basis changes for the [simultaneous butterfly layer](simultaneous-butterfly-layer.md), whose exact computation needs them.

A binary row addition adds one row of a matrix into another in every column, so it changes the selected bits of two whole address chunks at once. The procedure performs all the XORs of one such addition together rather than one bit position at a time.

The record's address is split into three chunks named $x$, $y$, and $z$; here these letters name chunks, so $y$ no longer means the polynomial variable. Here $f$ is the number of selected positions in each chunk. $K$ is the spacing between them, not the chunk width used on the transform layout page. Each chunk has $L$ bits, the chunk width, with $L = fK$.

The selected positions start at offset $\rho$, with $0 \le \rho < K$. Here $i$ indexes selected positions, not the convolution indices of earlier pages. The $i$-th selected position is $j_i = \rho + iK$ for $0 \le i < f$, counted from the least significant bit. The procedure computes

$$y_{j_i} \leftarrow y_{j_i} \oplus x_{j_i} \qquad (0 \le i < f),$$

so the selected bits of $x$ are XORed into the same positions of $y$, where $\oplus$ is exclusive or.

For example, take $f=2$, $K=6$, $L=12$ and $\rho=1$, so $j_0=1$ and $j_1=7$. If the $x$ bits there are $1$ and $0$, and the $y$ bits are $1$ and $1$, the procedure leaves the $y$ bits as $0$ and $1$.

Packed selected-bit addition is built from three streaming operations: an [address-field interchange](address-interchange.md) of equal-width chunks, cyclic shifts of chunk ranges, and a fixed permutation of two-bit values. A streaming operation is a fixed multitape procedure whose time grows with the volume it processes. A coordinate range is the finite set of values one address coordinate takes, and a cyclic shift of a chunk range adds an offset, set by the other chunks, to that chunk's value modulo $2^L$. Packed selected-bit addition is a restricted form of the [address shear](address-shear.md) that changes only the selected positions.

Each record has $R$ bits, a bit count, not the orthogonal residual $R$ of earlier pages. Let $N_0,\dots,N_3$ be the sizes of the four other coordinate ranges, so $M = 2^{3L}N_0N_1N_2N_3$ counts the records, and $V = MR$ is the total number of bits.

The construction first applies a constant number of cyclic shifts, whose composition is $S_0$. Outside a set $B$ of exceptional addresses, $S_0$ agrees with the exact map $T_0$ that performs the XORs. The fraction $\delta_{\text{bad}} = \min\{1, 80(f-1)2^{-K}\}$ is small when $K$ is large. The exceptions are few: $|B| \le \delta_{\text{bad}} M$ <cite data-source="paper">|B| ≤ δbad M</cite>.

The exact map $T_0$ preserves $B$ <cite data-source="paper">The ideal map T0 preserves all guard values and therefore preserves B</cite>. Since $S_0$ and $T_0$ agree outside $B$ and both are bijections, $T_0S_0^{-1}$ fixes every address outside $B$ and permutes $B$. Applying this correction after the shifts therefore gives $T_0$ exactly.

Under the asymptotic conditions of the lemma, the time is $O(V(L^\tau+1))$ <cite data-source="paper">When Arect = O(p), R exceeds every fixed polynomial in p, f ≤ d ≤ p, and K/ log p → ∞, this is O(V (Lτ + 1))</cite>.
