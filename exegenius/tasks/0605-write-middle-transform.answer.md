The middle transform is the Fourier transform of length $t$ with its outputs read in a permuted order, and it is the step of the argument that carries the computation onto the power-of-two target length $t$. The middle transform is the inner step of [Gaussian resampling](gaussian-resampling.md), which wraps it between two Gaussian maps.

The reason for the target length is the shape of the transforms. <cite data-source="paper">The transform lengths needed for the integer product are pairwise coprime</cite>, whereas the synthetic transforms use powers of two. Gaussian resampling bridges the two: it <cite data-source="paper">expresses each source Fourier transform through a power-of-two tensor transform.</cite>

Write $s$ for the source length and $t$ for the target length, with <cite data-source="paper">gcd(s, t) = 1</cite>, and let $t$ be even. Let $F_t$ be the normalized discrete Fourier transform of length $t$, with input index $j$ and output index $k$, both running over $\{0,\dots,t-1\}$:
$$(F_tu)_k=\frac1t\sum_{j=0}^{t-1}u_j\,e^{-2\pi i jk/t}.$$
A coordinate permutation is a reindexing of the entries of a vector, and the sources use the reindexing $k\mapsto -sk \bmod t$ on outputs. <cite data-source="paper">Define coordinate permutations by</cite> that map. The middle transform $\mathcal M_t$ is the operator defined by $(\mathcal M_t u)_k=(F_t u)_{-sk \bmod t}$. Since $e^{-2\pi i j(-sk)/t}=e^{2\pi i sjk/t}$, it can be written directly as
$$(\mathcal M_t u)_k=\frac1t\sum_{j=0}^{t-1}u_j\,e^{2\pi i sjk/t}.$$
So $\mathcal M_t$ is a discrete Fourier transform whose frequency is multiplied by $-s$.

The middle transform is computed through [Bluestein's chirp identity](bluestein-chirp-identity.md), which writes it as this cyclic convolution with phases. For each integer $j$, let $\varsigma_j=\exp(-\pi i s j^2/t)$ be the chirp factor. Because $t$ is even, $\varsigma_{j+t}=\varsigma_j$, and $|\varsigma_j|=1$. A pointwise phase multiplication multiplies each entry by a complex number of modulus one, so multiplying by $\varsigma_j$ or by its complex conjugate $\overline{\varsigma_j}$ is one. The identity $2jk=j^2+k^2-(j-k)^2$ gives
$$\overline{\varsigma_k}\,\varsigma_{k-j}\,\overline{\varsigma_j}=\exp\Big(\pi i s\,\frac{k^2-(k-j)^2+j^2}{t}\Big)=e^{2\pi i sjk/t},$$
and therefore
$$(\mathcal M_t u)_k=\frac{\overline{\varsigma_k}}{t}\sum_{j=0}^{t-1}\varsigma_{k-j}\,\big(\overline{\varsigma_j}\,u_j\big).$$
The sum is a cyclic convolution of $\varsigma$ with the phase-multiplied input $\overline{\varsigma_j}u_j$. The method therefore shows its claim: <cite data-source="paper">The factor QFt in (35) can be computed from a cyclic convolution and two pointwise phase</cite> multiplications. Here $\mathrm{QFt}$ is the paper's name for this operator, and the middle transform is one cyclic convolution bracketed by two phase multiplications, one before and one after.

As a small example, take $t=2$ and $s=1$. Then $\varsigma_0=1$ and $\varsigma_1=-i$, and the formula gives $(\mathcal M_2u)_0=\tfrac12(u_0+u_1)$ and $(\mathcal M_2u)_1=\tfrac12(u_0-u_1)$, the two outputs of $F_2$, since $-sk\equiv k \pmod 2$ here.

For several axes, the paper applies this one-axis operator along each coordinate and composes the results as a [tensor product](tensor-product.md). <cite data-source="paper">Tensoring (33) proves (35).</cite>
