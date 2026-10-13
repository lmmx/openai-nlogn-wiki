Bluestein's chirp identity rewrites the [discrete Fourier transform](fourier-transform.md) of a vector and computes it by a [cyclic convolution](cyclic-convolution.md) placed between two pointwise multiplications.

Bluestein's chirp identity acts on the middle transform of the paper's multiplication algorithm, including its [target permutation](gaussian-resampling.md). The identity performs that permutation inside its multiplications, so no separate pass is needed, and it turns the transform into <cite data-source="paper">normalized cyclic convolution</cite>.

Take one coordinate of length $q$, so $\hat u_k=\frac1q\sum_j u_j\exp(-2\pi i jk/q)$. Let $\chi_p=\exp(-\pi i p^2/q)$ be the chirp value at an integer $p$. Since $2jk=j^2+k^2-(k-j)^2$,

$$\exp\left(-\frac{2\pi i\, jk}{q}\right)=\chi_j\,\chi_k\,\overline{\chi_{k-j}},$$

so $q\,\hat u_k=\chi_k\sum_j (u_j\chi_j)\,\overline{\chi_{k-j}}$. The factors $\chi_j$ and $\chi_k$ are pointwise multiplications, and the sum is a convolution in the index $k-j$.

For even $q$, $\chi_{p+q}=\chi_p$, so $\overline{\chi_{k-j}}$ may be read at the residue $(k-j)\bmod q$, and the sum is already a cyclic convolution.

For odd $q$, $\chi_{p+q}=-\chi_p$, so each wrapped term would carry a sign $-1$ that a cyclic convolution lacks. The phase twist removes it. Let $\tau_p=\exp(\pi i p/q)$ be the phase twist at an integer $p$, which satisfies $\tau_{p+q}=-\tau_p$. The twisted sequences are $\mu_j=u_j\chi_j\tau_j$ and $\nu_p=\overline{\chi_p}\,\tau_p$ for $0\le j,p<q$. Each product $\mu_j\nu_{(k-j)\bmod q}$ equals $\tau_k\,u_j\chi_j\overline{\chi_{k-j}}$: at a wrap the two sign changes cancel, and $\tau_j\tau_{k-j}=\tau_k$. Therefore

$$q\,\hat u_k=\chi_k\,\overline{\tau_k}\sum_j \mu_j\,\nu_{(k-j)\bmod q}.$$

The paper's own phase twist does this on its last cyclic coordinate, and <cite data-source="paper">its negative wrap gives precisely the original cyclic wrap after the twist is removed</cite>.
