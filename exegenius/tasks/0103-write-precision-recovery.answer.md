Error tracking and exact recovery shows the computed coefficients lie within $1/2$ of the true integers, so rounding is exact.

The computation runs on [Fixed-point Gaussian dyadic records](fixed-point.md) with $p=6b$ fractional bits; $b=\lceil\log_2n\rceil$ is the digit width. Let $h_p=2^{-p}$, $L=\log_2T$, $S\le T$; for large $n$, $T<8n/b$ gives $T<2^b$ and $L<b$. Error $a$ means sup-norm error under $ah_p$; every array stays in the disk (norm at most $1$). By the paper's cost lemma each [Synthetic polynomial transform](synthetic-transform.md) has error below $L$ <cite data-source="paper">$\sqrt2\ell\,2^{-p}<L2^{-p}$</cite>.

It adds errors through the [Contractions and bilinear contractions](contraction-maps.md) making up each normalized transform and product: linear ones keep an input error, and a bilinear $\mathcal M$ with $\|\mathcal M(f,g)\|\le\|f\|\|g\|$ satisfies
$$\|\mathcal M(f',g')-\mathcal M(f,g)\|=\|\mathcal M(f'-f,g')+\mathcal M(f,g'-g)\|\le\|f'-f\|\|g'\|+\|f\|\|g'-g\|.$$
For disk operands the two input errors add.

Take a unit phase $e$, a disk-grid approximation $\widetilde e$ with $|\widetilde e-e|<2h_p$, and a disk operand $x$. Truncation $Q_p$ adds under $\sqrt2h_p$, so $\|Q_p(\widetilde ex)-ex\|<(2\|x\|+\sqrt2)h_p<4h_p$; and $|\widetilde e|\le1$ gives $\|Q_p(\widetilde ex)\|\le\|x\|$.

The ring convolution $\mathcal M_r$ of [Phase twist](phase-twist.md) returns $(f*g)/T$. Its transforms and truncation err by under $3L+2$ before a final exact multiplication by $M=T/r$, scaling the error:
$$E_{\rm ring}:=M(3L+2)<5TL.$$
If an operand has norm at most $.7$, contraction bounds the exact output by $.7$; adding the error $5TLh_p<10^{-3}$ gives norm below $.701$. The complex convolution adds two input twists and an output untwist, each under $4$: error under $(E_{\rm ring}+4+4+4)h_p<6TLh_p$.

The chirp transform $\widetilde{\mathscr C}$ evaluates the [Bluestein chirp identity](chirp.md) as phase product, convolution, phase product. Let $\boldsymbol t$ be the axis lengths, $F_{\boldsymbol t}$ the exact Fourier transform and $Q$ the target permutation. The kernel adds $2$, the first phase $4$, the convolution $6TL$, the last phase $4$:
$$\|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\|<(6TL+2+4+4)h_p<8TLh_p.$$

A source transform applies [Gaussian resampling](gaussian-resampling.md) maps and a chirp transform (error under $2dp^2+8TL$), then scales exactly by $2^\gamma$ ($b\ge2^{24}$ gives $\gamma\le b/4$ <cite data-source="paper">$b\ge2^{24}$ implies $\gamma\le b/4$</cite>). As $2dp^2<TL$ eventually, its error is under $E_sh_p$, $E_s=9\cdot2^\gamma TL$.

Now $u,v$ denote the scaled digit arrays (the letters change meaning): a digit $a$ is stored as $a2^{-b-2}$, norm under $1/4$. Let $U,V_1$ be their exact source transforms and $\widetilde U,\widetilde V_1$ the computed ones, of norm under $.26$. Then $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has norm under $.5$, and
$$\widetilde U\cdot\widetilde V_1-U\cdot V_1=(\widetilde U-U)\cdot\widetilde V_1+U\cdot(\widetilde V_1-V_1)$$
has two terms under $E_sh_p$; truncation adds under $2h_p$. So $\|z-U\cdot V_1\|<(2E_s+2)h_p$.

Let $G$ be the exact opposite source transform. Both source transforms carry $1/S$, so $F(u*v)=S\,Fu\cdot Fv$ and $F^+F=I/S$; the retained permutation cancels ([Retained permutation cancellation](retained-permutations.md)), giving $G(U\cdot V_1)=(u*v)/S^2$ <cite data-source="paper">=\frac{u*v}{S^2}.</cite> The computed opposite transform accepts $z$ and is within $E_sh_p$ of $Gz$, while $G$ is a contraction, so the total is under $(3E_s+2)h_p$. Multiplying exactly by $S$, $\widetilde w$ approximates $w=(u*v)/S$ with error under $E_wh_p$:
$$E_w:=S(3E_s+2)<28\cdot2^\gamma T^2L.$$

The integer coefficients are $2^{2b+4}Sw$, undoing the digit scales and the $1/S$. With $S\le T<2^b$ and $L<b$ the absolute error is under
$$2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}<448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<\tfrac12.$$
Here $p=6b$ leaves margin $2^{-b}$ against an amplification up to $2^{5b+4}$. The coefficients are integers, so this strict error makes the nearest integer to the represented value the unique correct one.

Carry propagation rebuilds the binary product from the coefficients $c_j$ of the [Multiplication as radix-digit convolution](radix-digit-reduction.md), where $c_j\le q(2^b-1)^2$ and $q=\lceil n/b\rceil\le2^b$. With $Q_0=2^b$ and $k_0=0$,
$$d_j=(c_j+k_j)\bmod Q_0,\qquad k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$$
($d_j$ the output digit, $k_j$ the carry). Then $0\le k_j\le q(Q_0-1)<Q_0^2$: if so at $j$, then $c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1)$. As $c_j+k_j=d_j+Q_0k_{j+1}$, adding $c_jQ_0^j$ carries the invariant
$$\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$$
from $j$ to $j+1$. Unprocessed terms are multiples of $Q_0^j$, so the first $j$ radix digits are fixed. The product is below $2^{2n}$, so bits above position $2n-1$ are zero and $2n$ bits are output.
