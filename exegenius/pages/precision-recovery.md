Error tracking and exact recovery shows the error is below $1/2,$ so rounding is exact.

The computation runs on [Fixed-point Gaussian dyadic records](fixed-point.md). Let $b$ be the bits per radix digit, $p=6b$ the fractional bits, $T$ the padded array size, $S\le T$ the convolution length, $L=\log_2T,$ $\gamma$ the source scale exponent, $d$ the axis count.

Use $h_p=2^{-p}$ and the sup norm throughout; an error of $a$ means error less than $ah_p.$ Each synthetic transform has error less than $\sqrt2\ell\,2^{-p}<L2^{-p}$ with $L=\log_2T,$ where $\ell=\log_2r.$

Replacing the operands of a bilinear contraction $\mathcal B$ by $f',g'$ changes the output by at most $\|f'-f\|\|g'\|+\|f\|\|g'-g\|,$ since $\mathcal B(f',g')-\mathcal B(f,g)=\mathcal B(f'-f,g')+\mathcal B(f,g'-g).$ Hence, for disk operands, the two input errors add.

A computed phase product satisfies $\|Q_p(\widetilde ex)-ex\|<(2\|x\|+\sqrt2)h_p<4h_p$ and $\|Q_p(\widetilde ex)\|\le\|x\|,$ for unit phase $e,$ approximation $\widetilde e,$ disk operand $x.$

With $M=T/r$ the ring record count, the ring convolution error is $E_{\rm ring}:=M(3L+2)<5TL,$ and its output has norm below $.701$ when one operand has norm at most $.7.$ Here $3L+2$ is three transforms and a truncation.

The computed complex convolution has error less than $(E_{\rm ring}+4+4+4)h_p<6TLh_p:$ two input twists, the ring approximation and the output untwist. The chirp transform has error $\|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\|<(6TL+2+4+4)h_p<8TLh_p.$

The source transform (error $2dp^2+8TL$ before scaling, then multiplied by $2^\gamma$) has error less than $E_sh_p$ with $E_s=9\cdot2^\gamma TL,$ using $2dp^2<TL$ eventually.

For scaled digit arrays $u,v$ with exact transforms $U,V_1$ and computed $\widetilde U,\widetilde V_1.$ The computed product $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has $\|z-U\cdot V_1\|<(2E_s+2)h_p:$ two terms of norm below $E_sh_p$ each, plus truncation. Use $\widetilde U\cdot\widetilde V_1-U\cdot V_1=(\widetilde U-U)\cdot\widetilde V_1+U\cdot(\widetilde V_1-V_1).$ The opposite transform gives error less than $(3E_s+2)h_p$ relative to $G(U\cdot V_1)=(u*v)/S^2,$ with $G$ exact.

After the first exact multiplication by $S:$ $\widetilde w$ approximates $w=(u*v)/S$ with error less than $E_wh_p,$ $E_w:=S(3E_s+2)<28\cdot2^\gamma T^2L.$ After the second scaling by $2^{2b+4}S,$ undoing $1/S$ and the input scales, the absolute error is $2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}.$ Using $S\le T<2^b,$ $L<b$ it is less than $448b\,2^{-b+\gamma}.$ Since $\gamma\le b/4$ for $b\ge2^{24}$ it is at most $448b\,2^{-3b/4}<1/2.$ <cite data-source="paper">$b\ge2^{24}$ implies $\gamma\le b/4$</cite> With $p=6b,$ $4b$ spare bits remain; scaling spends $3b+4.$

The true coefficients are integers, so the strict error below $1/2$ makes the nearest integer to the represented value the unique correct coefficient.

We recover the coefficients $c_j$ of the [Multiplication as radix-digit convolution](radix-digit-reduction.md), which satisfy $c_j\le q(2^b-1)^2,$ with $q=\lceil n/b\rceil$ the digits in an $n$-bit input. The carries obey $k_0=0,$ $d_j=(c_j+k_j)\bmod Q_0,$ $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$ with $Q_0=2^b.$

The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2:$ if this holds at $j,$ then $c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1).$ Dividing by $Q_0$ and $q\le n\le Q_0$ finish the step.

The invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ shows the first $j$ radix digits are fixed. It holds at $j=0,$ and each step adds $c_jQ_0^j=(d_j+Q_0k_{j+1})Q_0^j;$ unprocessed terms are multiples of $Q_0^j.$

The exact product is less than $2^{2n},$ so all bits above position $2n-1$ are zero and exactly $2n$ bits are output.
