Bluestein's chirp identity rewrites the [discrete Fourier transform](fourier-transform.md) of a vector and computes it by a [cyclic convolution](cyclic-convolution.md) placed between two pointwise multiplications.

Bluestein's chirp identity acts on the middle transform of the paper's multiplication algorithm, including its [target permutation](gaussian-resampling.md). It turns the transform into normalized cyclic convolution <cite data-source="paper">Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution</cite>.

Take one coordinate of length $q$, so $\hat u_k=\frac1q\sum_j u_j\exp(-2\pi i jk/q)$. Let $\chi_\alpha=\exp(-\pi i \alpha^2/q)$ be the chirp value at an integer $\alpha$, the chirp index here. Since $2jk=j^2+k^2-(k-j)^2$,

$$\exp\left(-\frac{2\pi i\, jk}{q}\right)=\chi_j\,\chi_k\,\overline{\chi_{k-j}},$$

so $q\,\hat u_k=\chi_k\sum_j (u_j\chi_j)\,\overline{\chi_{k-j}}$. The factors $\chi_j$ and $\chi_k$ are pointwise multiplications, and the sum is a convolution in the index $k-j$.

For even $q$, $\chi_{\alpha+q}=\chi_\alpha$, so $\overline{\chi_{k-j}}$ may be read at the residue $(k-j)\bmod q$, and the sum is already a cyclic convolution.

For odd $q$, $\chi_{\alpha+q}=-\chi_\alpha$, so each wrapped term would carry a sign $-1$ that a cyclic convolution lacks. The phase twist removes it. Let $\tau_\alpha=\exp(\pi i \alpha/q)$ be the phase twist at an integer $\alpha$, which satisfies $\tau_{\alpha+q}=-\tau_\alpha$. The twisted sequences are $\mu_j=u_j\chi_j\tau_j$ and $\nu_\alpha=\overline{\chi_\alpha}\,\tau_\alpha$ for $0\le j,\alpha<q$, and the letters $\tau$, $\mu$ and $\nu$ change meaning here. Each product $\mu_j\nu_{(k-j)\bmod q}$ equals $\tau_k\,u_j\chi_j\overline{\chi_{k-j}}$: at a wrap the two sign changes cancel, and $\tau_j\tau_{k-j}=\tau_k$. Therefore

$$q\,\hat u_k=\chi_k\,\overline{\tau_k}\sum_j \mu_j\,\nu_{(k-j)\bmod q}.$$

The paper's own phase twist does this on its last cyclic coordinate, and <cite data-source="paper">its negative wrap gives precisely the original cyclic wrap after the twist is removed</cite>.
