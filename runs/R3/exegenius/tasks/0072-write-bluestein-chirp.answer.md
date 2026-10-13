Bluestein's chirp identity rewrites a [discrete Fourier transform](dft-fft.md) as a cyclic convolution, so that the later convolution machinery can compute it.

Let $\zeta$ be a primitive $2n$th root of unity with $\zeta^2=\omega$. The transform of $a_0,\dots,a_{n-1}$ is
$$A_j=\sum_{k=0}^{n-1}a_k\,\omega^{jk},$$
where $j$ and $k$ index outputs and inputs here.

Since $\zeta^2=\omega$ and $2jk=j^2+k^2-(j-k)^2$, the power splits into chirp phases:
$$\omega^{jk}=\zeta^{j^2}\,\zeta^{k^2}\,\zeta^{-(j-k)^2}.$$
Define $g_k=a_k\zeta^{k^2}$ and $z_t=\zeta^{-t^2}$, the chirp at integer index $t$. Pulling $\zeta^{j^2}$ out of the sum gives
$$A_j=\zeta^{j^2}\sum_{k=0}^{n-1}g_k\,z_{j-k},$$
a convolution of $g$ with $z$ read at index $j-k$.

Reading $z$ at $j-k$ modulo $n$ would make the sum cyclic, but the wrap carries a sign. Since $\zeta^n$ squares to $\omega^n=1$ and is not $1$ (as $\zeta$ has order $2n$), $\zeta^n=-1$. Expanding $(t+n)^2=t^2+2tn+n^2$ gives
$$z_{t+n}=\zeta^{-t^2}\,\omega^{-tn}\,(\zeta^{n})^{-n}=(-1)^n z_t,$$
using $\omega^{-tn}=1$. For odd $n$, $z_{t+n}=-z_t$.

For odd $n$, the phase twist turns this negative wrap into the original cyclic wrap <cite data-source="paper">after the twist is removed</cite>. Let $k$ and $l$ run over $\{0,\dots,n-1\}$, and multiply each $g_k$ by $\zeta^k$ and each $z_l$ by $\zeta^l$. Let $v_j$ be the cyclic convolution of these twisted lists at index $j$:
$$v_j=\sum_{k+l\equiv j \pmod n}\left(\zeta^k g_k\right)\left(\zeta^l z_l\right).$$
Each pair has $k+l=j+hn$ with $h\in\{0,1\}$, so its factor is $\zeta^{k+l}=\zeta^j(-1)^h$. If $h=1$, then $l=j-k+n$ and $(-1)^h z_l=z_{j-k}$; if $h=0$, then $l=j-k$. So every pair contributes $\zeta^j g_k z_{j-k}$, and $A_j=\zeta^{j^2-j}v_j$.

So the identity computes its transform by a cyclic convolution, with the phase $\zeta^{j^2-j}$ applied to each output.

For $n=2$, take $\zeta=i$, so $\omega=-1$. The chirp form gives $A_1=i\,(-i\,a_0+i\,a_1)=a_0-a_1$. Since $n$ is even, $z_{t+n}=z_t$ and no twist is needed.
