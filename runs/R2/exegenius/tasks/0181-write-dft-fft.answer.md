The discrete Fourier transform (DFT) evaluates a coefficient list at powers of a root of unity, reducing [Convolution](convolution.md) to a pointwise product.

Let $a=(a_0,\dots,a_{n-1})$ have $n$ entries, a power of two. For $0\le m<n$, the letter $m$ is the frequency index (the letter $m$ changes meaning here, from the tape position on the earlier address-fields page). Let $\omega$ be a primitive $n$-th root of unity: $\omega^n=1$ and $\omega^m\ne1$ for $0<m<n$. The transform of $a$ is the list $A=(A_0,\dots,A_{n-1})$ with

$$A_m=\sum_{i=0}^{n-1} a_i\,\omega^{im}.$$

Here the letter $A$ changes meaning from the machine $A$ of the earlier pages.

A butterfly is the two-point operation $(u,v)\mapsto(u+\omega^s v,\;u-\omega^s v)$, where $u$, $v$ are its inputs and $s$ its exponent (these letters change meaning here: on the earlier address-fields page, $u$ is a field width).

Since $\omega^{n/2}=-1$, splitting $a$ by the parity of $i$ gives $A_m=E_m+\omega^mO_m$ and $A_{m+n/2}=E_m-\omega^mO_m$ for $0\le m<n/2$, where $E$ and $O$ are the transforms with root $\omega^2$ of the even- and odd-indexed entries.

Let $h$ be the number of entries in a block, and $t$, $0\le t<h/2$, an offset in it. With bit-reversed input, a block of size $h$ computes a transform with root $\omega^{n/h}$ from two halves that are transforms with root $\omega^{2n/h}$. The split above, with $\omega^{n/h}$ in place of $\omega$, pairs offsets $t$ and $t+h/2$ into a butterfly with exponent $s=tn/h$. The levels $h=2,4,\dots,n$ leave $A_0,\dots,A_{n-1}$ in order.

On tapes, the transform is built from butterflies and the address rearrangements of [Address fields and array layout on tapes](address-fields.md). Each level is one rearrangement that makes partners $t$ and $t+h/2$ adjacent, then one scan of butterflies. The paper's tape-level transform uses the same kinds of operation <cite data-source="paper">address rearrangements, signed shifts, and two-point butterfly operations</cite>.

Let $c_k=\sum_i a_i\,b_{(k-i)\bmod n}$ be the convolution, with transforms $B$ of $b$ and $C$ of $c$. Let $l=(k-i)\bmod n$ be the index into $b$ paired with $i$ at output $k$. Since $\omega^{km}=\omega^{(i+l)m}$ and $l$ runs over all indices for fixed $i$, $C_m=\sum_i a_i\omega^{im}\sum_l b_l\omega^{lm}=A_mB_m$.
