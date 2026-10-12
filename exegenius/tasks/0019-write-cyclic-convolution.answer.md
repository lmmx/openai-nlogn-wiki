Cyclic convolution is the product of two sequences in which indices wrap around modulo the sequence length, and it is the operation the permutation step below works with.

For vectors $u$ and $v$ of length $s$, index the entries by $i,j,m \in \mathbb{Z}/s\mathbb{Z}$, that is, by $0,\dots,s-1$ with sums taken modulo $s$. Here $u$ and $v$ are any vectors, not necessarily digit vectors. The cyclic convolution of $u$ and $v$, written $u\ast v$, has entries

$$(u\ast v)_m=\sum_{i+j\equiv m \pmod s} u_i v_j .$$

Cyclic convolution is the wrap-around form of the [convolution of digit vectors](radix-digit-convolution.md), in which an index $i+j \ge s$ is reduced to $i+j-s$.

For example, take $s=3$, $u=(1,2,0)$ and $v=(0,1,1)$. The ordinary convolution has entries $(0,1,3,2,0)$ at indices $0$ to $4$. The entries at indices $3$ and $4$ wrap onto $0$ and $1$, so $u\ast v=(2,1,3)$.

For arrays indexed by tuples $(i_1,\dots,i_d)$ with $i_k\in\mathbb{Z}/s_k\mathbb{Z}$, the wrap-around applies in each axis separately, and the source uses $\ast$ this way <cite data-source="paper">denote cyclic convolution in the displayed axes</cite>. Let $S=s_1s_2\cdots s_d$, the number of entries of such an array (so $S=s$ when $d=1$). Here $S$ means this product, not the Gaussian map $S$ of the earlier page.

Cyclic convolution is turned into pointwise products by the [discrete Fourier transform](discrete-fourier-transform.md), which is the normalized convolution rule:

$$F_s(u\ast v)=S\,(F_su)\cdot(F_sv),$$

where $F_s$ is the normalized Fourier transform, and $\cdot$ is the entrywise product. The inverse transform $F_s^{+}$ satisfies $F_s^{+}F_s=I/S$.

Write $R$ for the retained source permutation, the $P_s$ of the resampling identity, with inverse $R^{-1}$. The claim $RF_s^{+}R(F_su\cdot F_sv)=(u\ast v)/S^2$ follows in three steps:

- $F_s^{+}R=R^{-1}F_s^{+}$, so $RF_s^{+}R=F_s^{+}$.
- A permutation commutes with pointwise products, so $(RF_su)\cdot(RF_sv)=R(F_su\cdot F_sv)$. This moves $R$ through the product, so the two copies of $R$ can meet across the inverse transform.
- By the convolution rule and $F_s^{+}F_s=I/S$, we get $S\,F_s^{+}(F_su\cdot F_sv)=F_s^{+}F_s(u\ast v)=(u\ast v)/S$, hence $F_s^{+}(F_su\cdot F_sv)=(u\ast v)/S^2$.

The permutation $R$ disappears exactly because the inverse transform carries $R$ to $R^{-1}$, so the two copies cancel. Nothing remains to reorder the result, because permuting before or after a pointwise product gives the same output. The output is $u\ast v$ in its own order, so no sort is executed.
