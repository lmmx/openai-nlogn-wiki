Bluestein's chirp identity rewrites a [discrete Fourier transform](dft-fft.md) as a cyclic [Convolution](convolution.md), so that later convolution machinery can compute it.

Let $\zeta$ be a primitive $2n$th root of unity with $\zeta^2=\omega$. Here $j$ indexes outputs and $k$ indexes inputs, both in $\{0,\dots,n-1\}$. The transform of $a_0,\dots,a_{n-1}$ is
$$A_j=\sum_{k=0}^{n-1}a_k\,\omega^{jk}.$$

Since $2jk=j^2+k^2-(j-k)^2$, the power splits:
$$\omega^{jk}=\zeta^{j^2}\,\zeta^{k^2}\,\zeta^{-(j-k)^2}.$$
Define $g_k=a_k\zeta^{k^2}$ and $z_t=\zeta^{-t^2}$, the chirp at integer index $t$. Then
$$A_j=\zeta^{j^2}\sum_{k=0}^{n-1}g_k\,z_{j-k}.$$

Reading $z$ at $j-k$ modulo $n$ makes the sum cyclic, but the wrap carries a sign. Since $\zeta^n$ squares to $\omega^n=1$ and is not $1$, $\zeta^n=-1$. Expanding $(t+n)^2=t^2+2tn+n^2$ gives $z_{t+n}=(-1)^n z_t$, using $\omega^{tn}=1$. For odd $n$, $z_{t+n}=-z_t$, and the phase twist below turns this wrap into the original cyclic wrap <cite data-source="paper">after the twist is removed</cite>.

Multiply each $g_k$ by $\zeta^k$ and each $z_l$ by $\zeta^l$, for $k,l\in\{0,\dots,n-1\}$. Let $v_j$ be the cyclic convolution of these twisted lists at output $j$, for $j\in\{0,\dots,n-1\}$:
$$v_j=\sum_{k+l\equiv j \pmod n}\left(\zeta^k g_k\right)\left(\zeta^l z_l\right).$$

Since $k$, $l$ and $j$ lie in $\{0,\dots,n-1\}$, $k+l-j$ lies between $-(n-1)$ and $2n-2$, whose only multiples of $n$ are $0$ and $n$, so $k+l=j+hn$ with $h\in\{0,1\}$. Then $\zeta^{k+l}=\zeta^j(-1)^h$. If $h=1$, then $l=(j-k)+n$ and $z_l=-z_{j-k}$, so $(-1)^h z_l=z_{j-k}$. If $h=0$, then $l=j-k$. Either way it contributes $\zeta^j g_k z_{j-k}$. Each $k$ gives one pair, so $v_j=\zeta^j\sum_k g_k z_{j-k}$ and $A_j=\zeta^{j^2-j}v_j$.

So the identity computes its transform by a cyclic [Convolution](convolution.md), with the phase $\zeta^{j^2-j}$ applied to each output.

For $n=2$, take $\zeta=i$, so $\omega=-1$. Then $A_1=i\,(-i\,a_0+i\,a_1)=a_0-a_1$. For even $n$, $z_{t+n}=z_t$ and no twist is needed.
