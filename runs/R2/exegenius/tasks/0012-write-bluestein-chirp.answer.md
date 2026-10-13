Bluestein's chirp identity rewrites a [discrete Fourier transform](dft-fft.md) as a cyclic [convolution](convolution.md), so that the transform can be computed by the convolution machinery used later on this path. It is the step that converts the middle transform of the argument into cyclic convolution.

Let $n$ be the number of points in the transform. Let $\omega$ be a primitive $n$th root of unity. Let $\zeta$ be a primitive $2n$th root of unity with $\zeta^2=\omega$. The index $j$ runs over the outputs and $k$ over the inputs. Write $x_k$ for the $k$th input and $X_j$ for the $j$th output. The transform is
$$X_j=\sum_{k=0}^{n-1}x_k\,\omega^{jk}.$$

Since $\zeta^2=\omega$ and $2jk=j^2+k^2-(j-k)^2$, the power $\omega^{jk}$ splits into three chirp phases:
$$\omega^{jk}=\zeta^{j^2}\,\zeta^{k^2}\,\zeta^{-(j-k)^2}.$$
Pulling $\zeta^{j^2}$ out of the sum gives
$$X_j=\zeta^{j^2}\sum_{k=0}^{n-1}\left(x_k\zeta^{k^2}\right)\zeta^{-(j-k)^2}.$$
Write $a_k=x_k\zeta^{k^2}$ for the premultiplied inputs and $b_m=\zeta^{-m^2}$ for the chirp, with index $m$. The sum is a convolution of $a$ with $b$, read at index $j-k$.

Reading $b$ at $j-k$ modulo $n$ would make this sum cyclic, but for odd $n$ we have $b_{m+n}=-b_m$, because $\zeta^n=-1$. The wrap is therefore negative. The [last-coordinate phase twist](phase-twist-convolution.md) handles this: the negative wrap is the original cyclic wrap <cite data-source="paper">after the twist is removed</cite>. So the identity computes its transform by a cyclic [convolution](convolution.md) on the twisted coordinates. This matters because the later steps compute convolutions over the polynomial ring.

For $n=2$, take $\zeta=i$, so $\omega=-1$. The identity gives $X_1=i\,(-i\,x_0+i\,x_1)=x_0-x_1$, which is the direct value $x_0+(-1)\,x_1$.
