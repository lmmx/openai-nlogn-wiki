The discrete Fourier transform (DFT) evaluates a coefficient list at powers of a root of unity, reducing [Convolution](convolution.md) to a pointwise product.

Let $a=(a_0,\dots,a_{n-1})$ have $n$ entries, a power of two. Let $\omega$ be a primitive $n$-th root of unity: $\omega^n=1$, and $\omega^m\ne1$ for each frequency index $m$ with $0<m<n$. The transform of $a$ is the list $A=(A_0,\dots,A_{n-1})$ with

$$A_m=\sum_{i=0}^{n-1} a_i\,\omega^{im},$$

where $m$, $0\le m<n$, is the frequency index.

A butterfly is the two-point operation $(u,v)\mapsto(u+\omega^s v,\;u-\omega^s v)$; $u$, $v$ are its inputs and $s$ the exponent of its power.

Split the sum by the parity of $i$. Let $E$ and $O$ be the transforms with root $\omega^2$ of the even- and odd-indexed entries of $a$. Since $\omega^{n/2}=-1$, $A_m=E_m+\omega^mO_m$ and $A_{m+n/2}=E_m-\omega^mO_m$ for $0\le m<n/2$, a butterfly with $s=m$. Recursing gives $\log_2 n$ levels. Here $h$ is the number of entries in a block and $t$ an offset in the block. Each level combines two transforms of length $h/2$ into one of length $h$: the pair at offsets $t$ and $t+h/2$ uses $s=tn/h$. With bit-reversed input, the last level leaves $A_0,\dots,A_{n-1}$ in order.

On tapes, the transform is built from butterflies and the rearrangements and shifts of [Address fields and array layout on tapes](address-fields.md). The source builds its tape-level transform the same way, from <cite data-source="paper">two-point butterfly operations</cite>.

Let $B$ and $C$ be the transforms of $b$ and of $c_k=\sum_i a_i\,b_{(k-i)\bmod n}$. With $l=(k-i)\bmod n$, the index into $b$ paired with $i$ at output $k$: as $\omega^n=1$, $\omega^{km}=\omega^{(i+l)m}$, and $l$ ranges over all indices, so $C_m=\sum_i a_i\omega^{im}\sum_l b_l\omega^{lm}=A_mB_m$. The inverse $c_k=\frac1n\sum_m C_m\omega^{-km}$ recovers $c$, since $\sum_m\omega^{dm}$ is $n$ if $d\equiv0$ and $0$ otherwise, for an integer $d$. So transforming, multiplying entrywise and transforming back gives $c$.
