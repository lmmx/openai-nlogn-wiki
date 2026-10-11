Convolution is the operation that takes two finite sequences and returns a third, in which each entry sums the products of the pairs of input entries that combine to it. Convolution is the computation behind [Exact integer multiplication](exact-integer-multiplication.md), which the method below relies on. The [discrete Fourier transform](discrete-fourier-transform.md) computes it quickly.

Let $u$ and $v$ be two input sequences, and let $L$ be the number of entries in each, so $u=(u_0,\dots,u_{L-1})$ and $v=(v_0,\dots,v_{L-1})$. Here $i$ and $h$ are positions in $u$ and $v$, and $p$ is the position of an output entry. The convolution $w=u*v$ has $2L-1$ entries, $w_0$ through $w_{2L-2}$, and its $p$-th entry is given by the formula below.

$$w_p=\sum_{\substack{i+h=p\\ 0\le i,h\le L-1}} u_i\,v_h,\qquad 0\le p\le 2L-2.$$

Each product $u_i\,v_h$ pairs one entry of $u$ with one entry of $v$, and $w_p$ collects all pairs whose positions add to $p$.

Take $L=2$, $u=(1,2)$ and $v=(3,4)$. Then $w_0=u_0v_0=3$, $w_1=u_0v_1+u_1v_0=4+6=10$, and $w_2=u_1v_1=8$, so $w=(3,10,8)$. If the positions are instead added modulo $L$, the result is the [cyclic convolution](cyclic-convolution.md) of the same sequences, here $(11,10)$, because $w_0=u_0v_0+u_1v_1=3+8=11$.

The method of the paper "Integer multiplication below n log n" (OpenAI, 2026) uses this operation to multiply integers, after splitting each input into radix digits (the digits of the input in a fixed base): <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.</cite>
