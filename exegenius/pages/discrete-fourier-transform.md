The discrete Fourier transform is built as a [Linear map](linear-map.md) that sends a vector of complex numbers to another vector of the same length. It reduces [Radix-digit convolution](radix-digit-convolution.md) to pointwise products of transformed vectors.

Let $q$ be the number of values in each vector, and let $\omega$ be a primitive $q$-th root of unity, meaning $\omega^q=1$ and $\omega^m\neq 1$ for each integer exponent $m$ with $0<m<q$.

Let $a=(a_0,\dots,a_{q-1})$ and $b$ be vectors of $q$ complex numbers, with input positions $j$ and output positions $p$ running from $0$ to $q-1$. The transform $F_q$ sends $a$ to the vector with entries

$$(F_q a)_p=\frac{1}{q}\sum_{j=0}^{q-1}\omega^{jp}a_j,$$

and the opposite transform $F_q^+$ uses $\omega^{-1}$ in place of $\omega$.

For an integer exponent $e$, the sum $\sum_{s=0}^{q-1}\omega^{es}$ over the frequency index $s$ equals $q$ if $q$ divides $e$, and $0$ otherwise. If $q$ divides $e$, every term is $1$. Otherwise $\omega^e\neq 1$ by primitivity (reduce $e$ modulo $q$), and the geometric sum is $\frac{(\omega^e)^q-1}{\omega^e-1}=0$, because $(\omega^e)^q=1$.

Applying $F_q^+$ after $F_q$ gives $a/q$, since $(F_q^+F_q a)_p=\frac{1}{q^2}\sum_j a_j\sum_s\omega^{s(j-p)}$, and the inner sum is $q$ when $j=p$ and $0$ otherwise.

For vectors $a$ and $b$, the cyclic convolution $a*b$ has entries $(a*b)_p=\sum_{j=0}^{q-1}a_j\,b_{(p-j)\bmod q}$. Let $c=(F_qa)\cdot(F_qb)$ be the entrywise product, and write $h$ for an input position of $b$. Then

$$(F_q^+c)_p=\frac{(a*b)_p}{q^2}.$$

Expanding both transforms gives $(F_q^+c)_p=\frac{1}{q^3}\sum_{j,h}a_jb_h\sum_s\omega^{s(j+h-p)}$. The inner sum is $q$ when $j+h\equiv p \pmod q$ and $0$ otherwise. The three factors $1/q$ (two from $F_q$, one from $F_q^+$) and the full-period sum leave $1/q^2$, and the surviving pairs have $h=(p-j)\bmod q$.

The paper fixes where each transformed entry is stored <cite data-source="paper">We also specify where each frequency entry is stored, because the opposite transform consumes that same order after a pointwise product</cite>, and the opposite transform reads entries in that same order.
