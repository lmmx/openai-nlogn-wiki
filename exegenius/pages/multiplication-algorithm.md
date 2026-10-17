The multiplication algorithm chains the earlier reductions to turn two $n$-bit integers into their exact $2n$-bit product.

It takes its sizes from [Parameter and prime-length choice](parameter-choice.md). Here $b=\lceil\log_2 n\rceil$ is the digit width in bits and $p=6b$ is the number of fractional bits kept. Axis lengths are primes $s_i$ with product $S$, and padded lengths $t_i$ with product $T$.

Each input splits into $q=\lceil n/b\rceil$ radix-$2^b$ digits $a_j$, and the product is their convolution modulo $x^S-1$, as in [Multiplication as radix-digit convolution](radix-digit-reduction.md). The convolution is addressed on the prime axes by the [Chinese-remainder address map](crt-map.md) $\Phi$.

Let $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$ be the chirp array. The [Bluestein chirp identity](chirp.md) gives $QF_{\boldsymbol t}x=\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)$: phase, convolution with the chirp, phase. Here $F_{\boldsymbol t}$ is the transform on the axes $t_i$, and $\mathcal M_{\mathbb C}(f,g)=f*g/T$ is computed through the [Phase twist](phase-twist.md) and [Convolution from the retained transform layout](ring-convolution.md). With $\widetilde a$ the approximation of $a$ and $Q_p$ truncation to $p$ fractional bits, the computed version forms $x_0=Q_p(\overline{\widetilde a}\cdot x)$, the data operand after the first endpoint phase. The computed chirp transform is $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$ with $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$. The source transform $\widetilde{\mathscr F}$ applies the [Gaussian resampling](gaussian-resampling.md) map $\mathcal A$, then $\widetilde{\mathscr C}$, then the resampling map $\mathcal B_0$, then multiplies exactly by $2^\gamma$, where $\gamma$ counts the zero bits appended to each word. Replacing each numerical subroutine by the exact map it approximates, the exact counterpart is $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, with $R$ a retained permutation.

Digit $a_j$ is stored as the exact grid numerator $a_j2^{p-b-2}$ in a signed real word, representing $a_j2^{-b-2}$; $S-q$ zero records are appended. Then:

1. Apply $\Phi$ to obtain source arrays $u,v$ of norm less than $1/4$.
2. Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.
3. Multiply corresponding coefficients and truncate to $p$ fractional bits, obtaining $z$.
4. Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators by $S$, obtaining $\widetilde w$.
5. Multiply by $2^{2b+4}S$, round to the nearest integers, and apply $\Phi^{-1}$.
6. Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits <cite data-source="paper">Propagate radix-$2^b$ carries in increasing coefficient order.</cite>

The two scalings by $S$ undo different normalizations <cite data-source="paper">The two occurrences of $S$ in this algorithm undo different normalizations.</cite>. By [Retained permutation cancellation](retained-permutations.md), $R$ is never executed as a sort and the counterpart after the three transforms is $(u*v)/S^2$. So after the first scale it is $w=(u*v)/S$, and the second scale gives $2^{2b+4}(u*v)$, cancelling the factor $2^{-b-2}$.

Exactness is justified by [Error tracking and exact recovery](precision-recovery.md): the error on the recovered integer coefficients is below $1/2$.
