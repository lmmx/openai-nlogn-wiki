Convolution over the polynomial ring is computed along the [remaining axes](transform-axis.md) as a normalized cyclic convolution of two arrays of records. It is the step of [Integer multiplication below n log n](main-theorem.md) that makes the record products integer products.

## Definitions and transforms

Convolution over the polynomial ring takes its products in the [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md), $R_r$, where $y^r=-1$. The two input arrays are $\varphi$ and $\psi$, with records $\varphi_a,\psi_b\in R_r$ at addresses $a$ and $b$. Axis $i$ has length $t_i$, and $\mu=\prod_i t_i$ is the number of records in an array. The cyclic convolution has records $(\varphi\ast\psi)_c=\sum_{a+b=c}\varphi_a\psi_b$, with $a+b$ taken modulo each axis length. The normalized convolution $\varphi\star\psi=\dfrac{\varphi\ast\psi}{r\mu}$ and the entrywise product $u\odot v=\dfrac{uv}{r}$ are used below.

On an axis of length $t$, $\omega_t=y^{2r/t}$ is a root of unity of order $t$ with $\omega_t^{t/2}=-1$. Convolution over the polynomial ring computes its transforms by [synthetic polynomial transforms](synthetic-transforms.md), whose roots of unity are powers of $y$. A frequency address $j$ is an integer index of a transform entry, with one component $j_i$ for each axis $i$. The forward transform $\hat u$ of an array $u$ has entries $\hat u_j=\frac{1}{\mu}\sum_a\omega^{j\cdot a}u_a$, where $j\cdot a=\sum_i j_ia_i$, and $\omega^{j\cdot a}=\prod_i\omega_{t_i}^{j_ia_i}$. The opposite transform $\check u$ has entries $\check u_c=\frac{1}{\mu}\sum_j\omega^{-j\cdot c}u_j$.

## Why the transforms invert

On one axis, $k$ runs over its $t$ positions, and $\sum_{k=0}^{t-1}\omega_t^{jk}$ is $t$ when $t$ divides $j$ and $0$ otherwise. When $t$ divides $j$, every term is $1$. Otherwise write $j=2^vj_0$ with $j_0$ odd, so $v+1\le\log_2 t$. <cite data-source="paper">k by k + t/2v+1 modulo t permutes the summands and multiplies their sum by y rj0 = −1.</cite> So the sum $s$ equals $-s$, hence $2s=0$, and $s=0$ because $R_r$ is a complex vector space. Summing over $j$ gives $\sum_j\omega^{j\cdot(a-c)}=\mu$ when $a=c$ and $0$ otherwise, so $\check{\hat u}=u/\mu$.

## Convolution as an entrywise product

Expanding gives $\mu^2\hat\varphi_j\hat\psi_j=\sum_{a,b}\omega^{j\cdot(a+b)}\varphi_a\psi_b$. As $\omega_t^t=1$, terms with the same $c=a+b$ regroup into $\mu\,\widehat{\varphi\ast\psi}_j$. Hence $\widehat{\varphi\star\psi}=\hat\varphi\odot\hat\psi$, and applying the opposite transform gives

$$\varphi\star\psi=\mu\,\check{(\hat\varphi\odot\hat\psi)}.$$

The product pairs frequency $j$ of $\varphi$ with frequency $j$ of $\psi$ only if both transforms store each frequency at the same position. The paper uses one layout, <cite data-source="paper">the forward entry with frequency address j is stored at L(Bj)</cite>, where the $B$ is the paper's layout map, not the base below. <cite data-source="paper">Pointwise multiplication commutes with applying the same record permutation LB to both</cite> operands, so the product is formed in stored order, and the opposite transform <cite data-source="paper">consumes that same order after a pointwise product</cite>.

## Packing the record products

Convolution over the polynomial ring computes its record products by [signed coefficient packing](signed-packing.md), which turns each polynomial product into an integer product. This works because evaluation at $B=2^{4p}$ respects products: for an integer polynomial $u=\sum_j u_jy^j$ put $u(B)=\sum_j u_jB^j$, so $(uv)(B)=u(B)\,v(B)$. One integer product then holds each coefficient as [fixed-width digit blocks](fixed-width-digit-blocks.md) in base $B$, provided the blocks do not overlap.

Each input is a disk array, which <cite data-source="paper">has norm at most one.</cite> <cite data-source="paper">A p-bit grid array has real and imaginary coefficient parts in 2−p Z.</cite> Let $\varphi_1$ and $\varphi_2$ be the real and imaginary integer polynomials of $\varphi$, and let $\psi_1$ and $\psi_2$ be those of $\psi$. Then $\varphi=2^{-p}(\varphi_1+i\varphi_2)$ and $\psi=2^{-p}(\psi_1+i\psi_2)$, with all four of degree less than $r$ and coefficients of absolute value at most $2^p$. Then $\varphi\psi=2^{-2p}N$ with $N=(\varphi_1\psi_1-\varphi_2\psi_2)+i(\varphi_1\psi_2+\varphi_2\psi_1)$. Four integer products, $\varphi_1(B)\psi_1(B)$, $\varphi_2(B)\psi_2(B)$, $\varphi_1(B)\psi_2(B)$ and $\varphi_2(B)\psi_1(B)$, give the four polynomial products. Signs are handled by <cite data-source="paper">Multiply the four pairs of absolute values using the established multiplier and restore each product’s sign.</cite>

Let $h=\varphi_1\psi_1$, with coefficients $h_j$. Each $h_j$ is a sum of at most $r$ products of integers bounded by $2^p$, so $|h_j|\le r2^{2p}$. Write $r=2^\ell$ with $\ell<p$; <cite data-source="paper">Let r = 2ℓ < 2p with integers</cite> gives $r<2^p$. A real numerator coefficient is a sum of at most $2r$ such products, so it is below $2r\cdot2^{2p}<2^{3p+1}\le2^{4p-1}=B/2$ for $p\ge2$. So the blocks of $h(B)=\sum_j h_jB^j$ do not overlap.

Convolution over the polynomial ring reads each coefficient as the [centered residue](centered-residue.md) modulo $B$ of the value left after the lower blocks are removed. Here $h_0$ is the centered residue of $h(B)$, since $h_0\equiv h(B)\pmod B$ and $|h_0|<B/2$. Convolution over the polynomial ring extracts its blocks by a [carry scan](carry-propagation.md): it takes each centered residue, subtracts it, and divides by $B$. This leaves $\sum_{j\ge1}h_jB^{j-1}$, whose lowest block is $h_1$.

Since $y^r=-1$, the coefficient at $j+r$ wraps to position $j$ with a minus sign. So <cite data-source="paper">subtract the coefficient at j + r from the one at j</cite> for $0\le j<r$. This reduces $N$ modulo $y^r+1$, and dividing its coefficients by $r2^{2p}$ gives $\varphi\psi/r$ exactly. Then $Q_p$ truncates the real and imaginary part of each coefficient toward zero to $2^{-p}\mathbb Z$, so the output lies on the $2^{-p}$ grid that the next step reads in fixed width.

Example: take $r=2$, $\varphi_1=1+2y$, $\psi_1=3+y$, and a toy base $100$ in place of $B$. Then $201\cdot103=20703$, whose base-100 blocks $03$, $07$, $2$ give $\varphi_1\psi_1=3+7y+2y^2$, each coefficient below $50$. Modulo $y^2+1$, this is $(3-2)+7y=1+7y$.
