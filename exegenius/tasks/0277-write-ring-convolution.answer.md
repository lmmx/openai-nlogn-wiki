Convolution over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ on the remaining $d-1$ axes is computed by transforming both operands, multiplying records pointwise and transforming back; the multiplication algorithm uses it as its convolution step.

Arrays are indexed by $\prod_i\mathbb Z/t_i\mathbb Z$ over the $d-1$ remaining axes, with values in $\mathcal R_r$, and $*$ is cyclic convolution ([Cyclic convolution](convolution.md)). Let $\|\cdot\|_\infty$ be the largest coefficient modulus in an array. A disk array has norm at most $1$; a disk grid array also has real and imaginary parts that are multiples of $2^{-p}$. Multiplying by a power of $y$ permutes coefficients and changes signs, so it preserves the norm.

Some letters have local meanings here. $P$ is the pointwise product (not a prefix count or a subspace), $L$ the layout permutation of records (not a linear map or a loss), $B$ the bit-reversal order (not a complement or a row length), $K$ the layout chunk width (not a tensor line or a spacing), $\ell=\log_2r$ (not a depth), and $\delta,\eta$ error bounds (not a slack or a relative deficit).

## Normalization

For arrays over $\mathcal R_r$ define $\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}$. A fixed output coefficient averages $rM$ signed scalar products <cite data-source="paper">$rM$ signed scalar products, and $\mathcal M_r$ is a bilinear</cite>: each of the $M$ first addresses fixes one second address, each of the $r$ first polynomial indices fixes one second index modulo $r$, and the negacyclic wrap supplies the sign. So $\mathcal M_r$ is a bilinear contraction, $\|\mathcal M_r(f,g)\|_\infty\le\|f\|_\infty\|g\|_\infty$ ([Contractions and bilinear contractions](contraction-maps.md)).

Let $F^-$ and $F^+$ be the forward and opposite synthetic transforms ([Synthetic polynomial transform](synthetic-transform.md)). Each output is an average of images of the inputs under powers of $y$, so both are contractions <cite data-source="paper">Thus both transforms are contractions.</cite> Expansion of the finite sums gives $F^-(f*g)=M(F^-f)(F^-g)$. With $F^+F^-=I/M$, as for the [Discrete Fourier transform](dft.md), it follows that $MF^+\bigl((F^-f)(F^-g)/r\bigr)=\frac{f*g}{rM}$. Write $P(u,v)=uv/r$ for the pointwise product in $\mathcal R_r$. Each coefficient of $uv$ is a signed sum of $r$ products of coefficients, so $P$ is bilinear with $\|P(u,v)\|_\infty\le\|u\|_\infty\|v\|_\infty$.

## Retained order

The transforms are laid out as in [Tape layout for synthetic transforms](transform-layout.md). Perform both forward transforms and retain their common $LB$ order. Their exact counterparts are $LBF^-$ and the opposite map $\mathcal T_+=F^+B^{-1}L^{-1}$, a contraction because permuting records preserves the norm. Each procedure maps disk grid arrays to disk grid arrays with error less than $\delta=\sqrt2\ell\,2^{-p}$ <cite data-source="paper">$\sqrt2\ell\,2^{-p}$, returns disk grid coefficients in the same</cite>.

Since $LB$ permutes records and leaves polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$. So the opposite transform $\mathcal T_+$ applied to the pointwise product of the stored forward outputs equals $F^+P(F^-f,F^-g)$, and no reordering is needed, as in [Retained frequency order](frequency-order.md). Multiplying by $M$ exactly gives $\mathcal M_r(f,g)$.

## Cost

Each record product is formed by [Signed packing](signed-packing.md) in $O(rp\log(rp))$ time, then truncated by $Q_p$, which changes it by less than $\eta=\sqrt2\,2^{-p}$ without raising the norm. There are $M=T/r$ products, so they cost $O(Tp\log(rp))$ in total. Each transform and the final linear scaling cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$, with $\tau,\lambda'$ the exponents of the layout page. The total is $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.

## Error

Let $u,v$ be the exact stored forward outputs and $\widetilde u,\widetilde v$ the returned ones, all disk arrays. By bilinearity, $P(\widetilde u,\widetilde v)-P(u,v)=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v)$. Each term is less than $\delta$, using the contraction bound for $P$ and norm at most $1$ of $\widetilde v$ and $u$, so $\|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty<2\delta$. With $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$, truncation gives $\|\widetilde z-z_*\|_\infty<2\delta+\eta$. The opposite procedure returns $\widetilde h$ with $\|\widetilde h-\mathcal T_+\widetilde z\|_\infty<\delta$, and $\|\mathcal T_+(\widetilde z-z_*)\|_\infty\le\|\widetilde z-z_*\|_\infty$ since $\mathcal T_+$ is a contraction. The triangle inequality gives $\|\widetilde h-\mathcal T_+z_*\|_\infty<3\delta+\eta$. The exact multiplication by $M$ gives total error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$ <cite data-source="paper">$M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed.</cite>
