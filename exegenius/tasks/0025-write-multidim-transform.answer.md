A multidimensional transform is the Fourier transform of an array indexed by several coordinates, computed one axis at a time. The argument needs it because the long Fourier transforms of the integer product are replaced by "multidimensional transforms whose axis lengths are powers of two" <cite data-source="paper">multidimensional transforms whose axis lengths are powers of two</cite>, which butterflies can compute.

Let $d$ be the number of axes and $q_i$ the number of positions along axis $i$, so $\boldsymbol q=(q_1,\dots,q_d)$. Let $N=\prod_i q_i$ be the number of entries. An entry of the array $u$ has an index tuple $j=(j_1,\dots,j_d)$ with $0\le j_i<q_i$; the output has index tuples $k$ of the same shape. Define

$$(F_{\boldsymbol q}u)_k=\frac1N\sum_j u_j\,e^{-2\pi i\sum_i j_ik_i/q_i}.$$

The exponential of a sum is a product of exponentials, so the kernel is a product of one-dimensional kernels. Each factor is a one-dimensional [Discrete Fourier transform](dft.md), so $F_{\boldsymbol q}$ is their tensor product $F_{\boldsymbol q}:=\bigotimes_iF_{q_i}$ <cite data-source="paper">F_{\boldsymbol q}:=\bigotimes_iF_{q_i}</cite>. This means that on an array of the form $u_j=\prod_i u^{(i)}_{j_i}$ it transforms each factor $u^{(i)}$ by its own $F_{q_i}$, and every array is a sum of such arrays.

## One axis at a time

A line along axis $i$ is the set of $q_i$ entries obtained by fixing all other coordinates. The sum over $j$ splits into $d$ nested sums, and $1/N=\prod_i 1/q_i$, so applying $F_{q_i}$ to every line along axis $i$, for $i=1,\dots,d$ in any order, gives $F_{\boldsymbol q}u$. Each line transform is computed by the [Butterflies and the fast transform](butterfly.md) in $O(q_i\log q_i)$ operations. Axis $i$ has $N/q_i$ lines, so all passes together cost $O(N\log N)$.

For $\boldsymbol q=(2,2)$, the pass on a line $(u,v)$ is $((u+v)/2,(u-v)/2)$. Applying it to rows and then columns gives $(F_{(2,2)}u)_{(1,1)}=(u_{00}-u_{01}-u_{10}+u_{11})/4$.

## Lifting one-dimensional identities

Tensor products satisfy $(A\otimes B)(C\otimes D)=AC\otimes BD$, so an identity between one-dimensional operators holds for their tensor products, with scalar factors multiplied. In [Gaussian resampling](gaussian-resampling.md), a prime length $s_i$ is handled through a power of two $t_i$ by an identity with permutations $P_{s_i},P_{t_i}$, contractions $A_i,B_{0,i}$ and scalar $2^{2\alpha^2}$, where $\alpha$ and the precision $p$ are parameters fixed on that page. Put $T=\prod_i t_i$, $\gamma=2d\alpha^2$, $R=\bigotimes_iP_{s_i}$, $Q=\bigotimes_iP_{t_i}$, $\mathcal A=\bigotimes_i A_i$ and $\mathcal B_0=\bigotimes_i B_{0,i}$. Then
$$RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A,$$
where $\boldsymbol s=(s_1,\dots,s_d)$ and $\boldsymbol t=(t_1,\dots,t_d)$. Both $\mathcal A$ and $\mathcal B_0$ are contractions <cite data-source="paper">Both $\mathcal A$ and $\mathcal B_0$ are contractions.</cite>, and the errors of the $d$ passes add, giving error less than $dp^2$.
