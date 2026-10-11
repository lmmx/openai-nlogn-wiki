Convolution is the operation that takes two finite sequences and returns a third in which each entry sums the products of the pairs of input entries that combine to it. It is the computation that exact multiplication is reduced to, and the [discrete Fourier transform](discrete-fourier-transform.md) is the tool that evaluates it quickly.

Let $a$ and $b$ be the two input sequences, each of length $n$, where $n$ is the number of entries in each input sequence. Write $a=(a_0,\dots,a_{n-1})$ and $b=(b_0,\dots,b_{n-1})$. Here $k$ is the position of an output entry, and $i$ and $j$ are the positions of the input entries that combine to it. The convolution $c=a*b$ is the sequence of length $2n-1$ whose $k$-th entry is

$$c_k=\sum_{\substack{i+j=k\\ 0\le i,j\le n-1}} a_i\,b_j,\qquad 0\le k\le 2n-2.$$

Each product $a_i\,b_j$ pairs one entry of $a$ with one entry of $b$, and the entry $c_k$ collects all such pairs whose positions add to $k$.

Take $n=2$, $a=(1,2)$ and $b=(3,4)$. Then

$$c_0=a_0b_0=3,\qquad c_1=a_0b_1+a_1b_0=4+6=10,\qquad c_2=a_1b_1=8,$$

so $c=(3,10,8)$. If the positions are instead added modulo $n$, the result is the [cyclic convolution](cyclic-convolution.md) of the same sequences, here $(11,10)$, because $c_0=a_0b_0+a_1b_1=3+8=11$.

The method of the paper uses this operation to multiply integers: <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.</cite>
