The multiplication algorithm chains the earlier reductions into one procedure that turns two $n$-bit integers into their exact $2n$-bit product.

Sizes come from [Parameter and prime-length choice](parameter-choice.md): $b=\lceil\log_2 n\rceil$ is the digit width in bits, $p=6b$ is the number of fractional bits kept, $s_i$ are distinct odd prime axis lengths with product $S$, and $t_i$ are padded power-of-two axis lengths near them, with product $T$. Each input splits into $q=\lceil n/b\rceil$ radix-$2^b$ digits $a_j$, and the product is their convolution modulo $x^S-1$, as in [Multiplication as radix-digit convolution](radix-digit-reduction.md). The [Chinese-remainder address map](crt-map.md) $\Phi$ lays this convolution out on the prime axes.

## The source transform

Let $F_{\boldsymbol s}$ be the discrete Fourier transform on the axes $s_i$, each axis normalized by its length, so the whole carries $1/S$. $F_{\boldsymbol s}^+$ is the same with the opposite sign in the exponent, and $F_{\boldsymbol t}$ is the transform on the axes $t_i$, carrying $1/T$. Prime lengths are not powers of two, so $F_{\boldsymbol s}$ is reached through power-of-two transforms.

Let $\mathcal M_{\mathbb C}(f,g)=f*g/T$ be the normalized cyclic convolution, computed through the [Phase twist](phase-twist.md) and [Convolution from the retained transform layout](ring-convolution.md). With the chirp array $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$ and the target permutation $Q$, the [Bluestein chirp identity](chirp.md) gives $QF_{\boldsymbol t}x=\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)$: phase, convolution with the chirp, phase. The computed version stores an approximation $\widetilde a$ of $a$ and truncates to $p$ fractional bits with $Q_p$. It forms the data operand $x_0=Q_p(\overline{\widetilde a}\cdot x)$ after the first phase, then $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$, the computed (approximate) convolution, and returns $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$. Replacing the approximations by exact phases and exact convolution gives back $QF_{\boldsymbol t}x$.

The source transform $\widetilde{\mathscr F}$ applies the [Gaussian resampling](gaussian-resampling.md) map $\mathcal A$, then $\widetilde{\mathscr C}$, then the resampling map $\mathcal B_0$, then multiplies exactly by $2^\gamma$, where $\gamma$ is the exponent of the resampling scale. Its exact counterpart $\mathscr F$ replaces each numerical routine by the exact map it approximates: $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, where $R$ is a retained coordinate permutation. So $\widetilde{\mathscr F}$ approximates a prime-length transform up to a permutation. The opposite-sign procedure is $\widetilde{\mathscr F}^{+}(z)=\overline{\widetilde{\mathscr F}(\overline z)}$; $R$ is real and conjugation flips the exponent sign, so its exact counterpart is $RF_{\boldsymbol s}^{+}$.

## The algorithm

Digit $a_j$ is stored as the exact grid value $a_j2^{-b-2}$, with $S-q$ zero records appended. Then:

1. Apply $\Phi$ to obtain source arrays $u,v$ (not the integers) of norm below $1/4$.
2. Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.
3. Multiply corresponding coefficients and truncate to $p$ fractional bits, obtaining $z$.
4. Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply by $S$, obtaining $\widetilde w$.
5. Multiply by $2^{2b+4}S$, round to the nearest integers, and apply $\Phi^{-1}$.
6. Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits <cite data-source="paper">Propagate radix-$2^b$ carries in increasing coefficient order.</cite>

The two scalings by $S$ undo different normalizations <cite data-source="paper">The two occurrences of $S$ in this algorithm undo different normalizations.</cite>. Each of $F_{\boldsymbol s}$ and $F_{\boldsymbol s}^{+}$ carries $1/S$, so $F_{\boldsymbol s}(u*v)=S\,F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v$ and $F_{\boldsymbol s}^{+}F_{\boldsymbol s}$ is the identity divided by $S$; hence $F_{\boldsymbol s}^{+}(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=(u*v)/S^2$. The permutations do not interfere: they commute with pointwise products and $RF_{\boldsymbol s}^{+}R=F_{\boldsymbol s}^{+}$, by [Retained permutation cancellation](retained-permutations.md). So steps 2 to 4 have exact counterpart $(u*v)/S^2$, and after the scale in step 4 it is $w=(u*v)/S$, with $w$ the exact array that $\widetilde w$ approximates. Step 5 gives $2^{2b+4}(u*v)$. Each stored operand carries $2^{-b-2}$, so $u*v$ carries $2^{-2b-4}$, and the factor $2^{2b+4}$ cancels it. Since $\Phi$ preserves convolution, $\Phi^{-1}$ returns the integer digit convolution.

[Error tracking and exact recovery](precision-recovery.md) shows that the error on these coefficients is below $1/2$, so rounding is exact and the carries give the exact product.
