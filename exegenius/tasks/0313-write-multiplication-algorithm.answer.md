The multiplication algorithm chains the earlier reductions to turn two $n$-bit integers into their exact $2n$-bit product. Splitting the inputs into radix digits reduces multiplication to convolving short integer coefficients, which every later step computes.

The algorithm takes its sizes from [Parameter and prime-length choice](parameter-choice.md). Here $b=\lceil\log_2n\rceil$ is the digit width in bits (not a field's digit count or a lowest bit), $p=6b$ is the number of fractional bits, the $s_i$ are distinct odd prime axis lengths with product $S$, and the $t_i$ are power-of-two axis lengths with product $T$.

The algorithm is based on [Multiplication as radix-digit convolution](radix-digit-reduction.md): each input splits into $q=\lceil n/b\rceil$ radix-$2^b$ digits $a_j$ (not mixed-radix digits), and the product is their convolution modulo $x^S-1$. The algorithm moves the convolution onto the prime axes $s_i$ by the [Chinese-remainder address map](crt-map.md) $\Phi$.

Below, $u,v$ are the source arrays (not the input integers), $z$ is the pointwise product array (not an address suffix) and $w$ is the scaled exact array (not a wire index).

## The source transform

Let $F_{\boldsymbol s}$ be the discrete Fourier transform on the axes $s_i$, normalized by $1/S$, $F_{\boldsymbol s}^+$ the same with the opposite exponent sign, and $F_{\boldsymbol t}$ the transform on the axes $t_i$ normalized by $1/T$.

The algorithm converts the convolution $\mathcal M_{\mathbb C}(f,g)=f*g/T$ to the ring modulo $y^r+1$ by the [Phase twist](phase-twist.md). It then computes the ring convolution by two forward synthetic transforms, a pointwise product and the opposite transform, as in [Convolution from the retained transform layout](ring-convolution.md).

With the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$ and the target permutation $Q$, the [Bluestein chirp identity](chirp.md) gives $QF_{\boldsymbol t}x=\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)$: a phase, a convolution with the chirp, a phase.

The computed chirp transform $\widetilde{\mathscr C}$ uses a grid approximation $\widetilde a$ of $a$ and truncation $Q_p$. For an array $x$ of norm at most $.6$ it forms $x_0=Q_p(\overline{\widetilde a}\cdot x)$, the data operand after the first phase, then $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$, and returns $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$. Replacing the approximations by exact phases and exact convolution gives $QF_{\boldsymbol t}x$.

The computed source transform $\widetilde{\mathscr F}$ applies the [Gaussian resampling](gaussian-resampling.md) input map $\mathcal A$, then $\widetilde{\mathscr C}$, then the output map $\mathcal B_0$, and multiplies the grid numerators exactly by $2^\gamma$, where $\gamma$ is the exponent of the power of two that resampling introduces. Its exact counterpart $\mathscr F$ replaces every numerical subroutine by the exact map it approximates and omits truncations, so $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$ <cite data-source="paper">Here an exact counterpart replaces every numerical subroutine by the exact map it approximates and omits truncations.</cite>. The last equality is the resampling identity, where $R$ is the retained source permutation of coordinates (not a row count or scalar ring). For an array $z$ the opposite-sign procedure is $\widetilde{\mathscr F}^{+}(z)=\overline{\widetilde{\mathscr F}(\overline z)}$, with exact counterpart $RF_{\boldsymbol s}^{+}$.

## The algorithm

Read each input in groups of $b$ bits from the least significant end, padding the last group with leading zeroes, to get the digits $a_j$. Store $a_j$ as the exact grid value $a_j2^{-b-2}$: the integer numerator $a_j2^{p-b-2}$ over the denominator $2^p$ in a signed real word followed by a zero imaginary word, with nonnegative exponent because $p=6b$. Append $S-q$ zero records. Then:

1. Apply $\Phi$ with its padded layout to obtain the arrays $u,v$ of exact $p$-bit grid values of norm below $1/4$.
2. Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.
3. Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, obtaining the array $z$.
4. Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, obtaining $\widetilde w$.
5. Multiply the numerators by $2^{2b+4}S$, round the real values to the nearest integers, write each as a signed $(3b+1)$-bit word (coefficients are below $2^{3b}$) with a zero word at padded addresses, and apply $\Phi^{-1}$, removing the padding.
6. Propagate radix-$2^b$ carries in increasing coefficient order, write the bits from least to most significant on a work tape, reverse that stream and output exactly $2n$ bits <cite data-source="paper">output exactly $2n$ bits in most-significant-first order</cite>.

The two scalings by $S$ undo different normalizations. Both $F_{\boldsymbol s}$ and $F_{\boldsymbol s}^{+}$ carry $1/S$, so $F_{\boldsymbol s}(u*v)=S\,F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v$ and $F_{\boldsymbol s}^{+}F_{\boldsymbol s}$ is the identity divided by $S$; hence $F_{\boldsymbol s}^{+}(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=(u*v)/S^2$. Since $F_{\boldsymbol s}^{+}R=R^{-1}F_{\boldsymbol s}^{+}$, by [Retained permutation cancellation](retained-permutations.md) the permutation $R$ cancels and none is executed as a sort. The exact counterpart after the three transforms is therefore $(u*v)/S^2$, and after step 4 it is $w=(u*v)/S$, which $\widetilde w$ approximates. Step 5 gives $2^{2b+4}(u*v)$: each stored operand carries $2^{-b-2}$, so $u*v$ carries $2^{-2b-4}$, which the factor $2^{2b+4}$ cancels, and $\Phi^{-1}$ returns the integer coefficient convolution <cite data-source="paper">The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution.</cite>.

Its rounding is justified by [Error tracking and exact recovery](precision-recovery.md): the error on the recovered coefficients is below $1/2$, so rounding is exact.
