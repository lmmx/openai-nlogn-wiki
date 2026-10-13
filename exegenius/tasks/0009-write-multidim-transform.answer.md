A multidimensional transform with power-of-two axes is the Fourier transform applied along every coordinate of an array when each coordinate has a power-of-two length. It is the object that [Gaussian resampling](gaussian-resampling.md) uses in place of prime-length transforms, so the rest of the argument deals only with power-of-two sizes. The Gaussian-resampling reduction of Harvey and van der Hoeven replaces the Fourier transforms needed for convolution by multidimensional transforms <cite data-source="paper">whose axis lengths are powers of two</cite>.

Let $d$ be the number of axes. Let $r_\ell$ be the length of axis $\ell$, a power of two, that is, the number of entries along that coordinate direction. Let $A$ be the input array, with entries $A_{j_1\cdots j_d}$. Let $B$ be the transformed array, with entries $B_{k_1\cdots k_d}$. Here $j_\ell$ is the index along axis $\ell$, ranging over $0,1,\dots,r_\ell-1$, and $k_\ell$ is the output index along that axis.

The whole transform is a tensor product of one [Discrete Fourier transform](fourier-transform.md) per axis, the one of length $r_\ell$ on axis $\ell$. Its entries are

$$B_{k_1\cdots k_d}=\frac{1}{r_1\cdots r_d}\sum_{j_1=0}^{r_1-1}\cdots\sum_{j_d=0}^{r_d-1}A_{j_1\cdots j_d}\prod_{\ell=1}^{d}\exp\Big(-\frac{2\pi\mathrm{i}\,j_\ell k_\ell}{r_\ell}\Big).$$

Each factor of the product depends on one axis only, so the sum over $j_1$ can be taken first, then $j_2$, and so on. Each step is the one-dimensional transform of length $r_\ell$ applied to every line of entries along axis $\ell$. The axes can therefore be processed one at a time, in any order.

Take $d=2$ and $r_1=r_2=2$. The length-2 transform sends $(u_0,u_1)$ to $((u_0+u_1)/2,(u_0-u_1)/2)$, since $\exp(-\pi\mathrm{i})=-1$. For $A_{00}=1$, $A_{01}=2$, $A_{10}=3$, $A_{11}=4$, the formula gives $B_{00}=5/2$, $B_{01}=-1/2$, $B_{10}=-1$ and $B_{11}=0$.
