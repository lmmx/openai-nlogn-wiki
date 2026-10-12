Packed selected-bit addition is a fixed multitape procedure that performs many binary row additions in one pass, and it supplies the binary basis changes for the [simultaneous butterfly layer](simultaneous-butterfly-layer.md), whose exact computation needs them. Its time bound is one term of the cost table, and a compatible choice of rational parameters makes every term fit the bound of Theorem 1.

A binary row addition XORs one address chunk into another. Here only the selected bit positions change, and the procedure performs all the XORs of one such addition together rather than one bit position at a time.

The record's address is split into three chunks. The procedure XORs selected bits of the source chunk $\xi$ into the target chunk $\eta$, leaving $\zeta$ as it is. Here $\mu$ is the number of selected positions in each chunk, and $\nu$ indexes them. The letter $K$ is the spacing between selected positions here, not the chunk width of the transform layout page. Each chunk has $L$ bits, the chunk width, and $L = \mu K$. The first selected position is at offset $\rho$, with $0 \le \rho < K$, and the $\nu$-th one is $\rho + \nu K$ for $0 \le \nu < \mu$, counted from the least significant bit. The procedure computes

$$\eta_{\rho+\nu K} \leftarrow \eta_{\rho+\nu K} \oplus \xi_{\rho+\nu K} \qquad (0 \le \nu < \mu),$$

where $\eta_{\rho+\nu K}$ and $\xi_{\rho+\nu K}$ are the bits at that position, and $\oplus$ is exclusive or.

For example, take $\mu=2$, $K=6$, $L=12$ and $\rho=1$, so the selected positions are $1$ and $7$. If the $\xi$ bits there are $1$ and $0$, and the $\eta$ bits are $1$ and $1$, the procedure leaves the $\eta$ bits as $0$ and $1$.

Packed selected-bit addition is built from three streaming operations, fixed multitape procedures whose time grows with the volume they process: an [address-field interchange](address-interchange.md) of equal-width chunks, cyclic shifts of chunk ranges, and a fixed permutation of two-bit values. A coordinate range is the finite set of values one address coordinate takes, and a cyclic shift of a chunk range adds an offset, set by the other chunks, to that chunk's value modulo $2^L$. Packed selected-bit addition is a restricted form of the [address shear](address-shear.md) that changes only the selected positions.

Each record has $E$ bits, a count of the bits in one record. Let $\lambda_0,\dots,\lambda_3$ be the sizes of the four other coordinate ranges. Write $M = 2^{3L}\lambda_0\lambda_1\lambda_2\lambda_3$ for the number of records, since each of the three chunks takes $2^L$ values. $V = ME$ is the total number of bits.

The construction first applies a constant number of cyclic shifts, whose composition is $\sigma$. Let $T$ be the exact map that performs the XORs on every record, and let $Z$ be the set of exceptional addresses, where $\sigma$ and $T$ disagree. The fraction $\delta = \min\{1, 80(\mu-1)2^{-K}\}$ is small when $K$ is large. So $|Z| \le \delta M$ <cite data-source="paper">|B| ≤ δbad M</cite>.

The exact map $T$ preserves $Z$ <cite data-source="paper">The ideal map T0 preserves all guard values and therefore preserves B</cite>. Since $T$ preserves $Z$, it also maps addresses outside $Z$ to addresses outside $Z$. As $\sigma$ and $T$ agree outside $Z$ and both are bijections, the correction $T\sigma^{-1}$ fixes every address outside $Z$ and permutes $Z$. Applying the correction after the shifts therefore gives $T$ exactly.

Under the asymptotic conditions of the lemma, the time is $O(V(L^\tau+1))$ <cite data-source="paper">When Arect = O(p), R exceeds every fixed polynomial in p, f ≤ d ≤ p, and K/ log p → ∞, this is O(V (Lτ + 1))</cite>, where $\tau$ is the cost exponent of the field interchange.
