A synthetic polynomial transform generalizes the [discrete Fourier transform](fourier-transform.md) to a polynomial ring whose roots of unity are powers of $y$. It transforms the digit convolution that multiplication reduces to, and each of its stages needs only signed shifts and additions.

It works in the [polynomial ring modulo yʳ + 1](polynomial-ring-y.md). It is built on $y$ as a [primitive root of unity](roots-of-unity.md) of order $2r$: $y^r=-1$, so $y^{2r}=1$, and no smaller positive power of $y$ equals $1$.

For a sequence $x_0,\dots,x_{2r-1}$ of ring elements, let $t$ be the input position and $s$ the frequency index, $s=0,\dots,2r-1$. Its transform is $\hat x_s=\sum_{t=0}^{2r-1} y^{st}x_t$.

Split the inputs into the halves $t<r$ and $t+r$. Since $y^{s(t+r)}=(-1)^s y^{st}$, for $i=0,\dots,r-1$ we get $\hat x_{2i}=\sum_{t<r} y^{2it}(x_t+x_{t+r})$ and $\hat x_{2i+1}=\sum_{t<r} y^{2it}\,y^t(x_t-x_{t+r})$. So a stage replaces each pair $(x_t,x_{t+r})$ by its sum and by its difference times the twiddle factor $y^t$. Each half is a transform of length $r$ with root $y^2$, of order $r$, and the same split repeats on it.

Each twiddle factor is a power of $y$, and multiplying by a power of $y$ is a signed shift of the coefficient list <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>. A stage therefore needs only shifts and additions. For $r=4$, $y^3(1+2y)=y^3+2y^4=-2+y^3$, since $y^4=-1$, so the coefficient list $(1,2,0,0)$ becomes $(-2,0,0,1)$.

The inverse is $x_t=\frac{1}{2r}\sum_{s=0}^{2r-1} y^{-st}\hat x_s$, with $y^{-1}=y^{2r-1}$. This holds because $\sum_{s=0}^{2r-1} y^{su}$ equals $2r$ when $u\equiv 0 \pmod{2r}$ and $0$ otherwise. Since $r$ is a power of two, $y^r+1$ has distinct roots, all primitive $2r$-th roots of unity, and a ring element is zero when it vanishes at each root, where the sum is an ordinary geometric sum.

Both forward transforms use the same index convention, so their outputs share the frequency order $s=0,\dots,2r-1$. Let $z$ be a second sequence of ring elements, transformed the same way. The products $\hat x_s\hat z_s$ therefore pair equal frequencies, and the inverse reads them in that order.

Expanding, $\hat x_s\hat z_s=\sum_{t,q} y^{s(t+q)}x_tz_q$, where $q$ is a position in $z$. Since $y^{2r}=1$, the exponent depends only on $h\equiv t+q \pmod{2r}$, so $\hat x_s\hat z_s=\sum_h y^{sh}(x\ast z)_h$, where $(x\ast z)_h=\sum_{t+q\equiv h \pmod{2r}} x_tz_q$ is the cyclic convolution with output position $h$. The inverse transform therefore returns $x\ast z$.
