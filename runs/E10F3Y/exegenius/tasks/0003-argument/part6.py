from lib import *

# ---------------------------------------------------------------- S5.1 CRT map
s51 = show(
    "S5.1",
    r"With pairwise coprime $s_i$, $P_i=\prod_{j<i}s_j$ and $\mu_i=P_i^{-1}\bmod s_i$, the assignment $\Phi:x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism $\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\ldots,x_d]/(x_i^{s_i}-1)$ preserving cyclic convolution, and it and its inverse are implemented by triangular controlled shifts on the padded box in $O\bigl(Tp\,d^2(1+\ell^\tau)\bigr)$.",
    r"Use the Chinese remainder theorem in the form $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$ for the mixed-radix index $k=\sum_ja_jP_j$: coordinate $i$ depends only on lower-index digits, so after ordering the axes $(a_1,\ldots,a_d)$ each coordinate is a controlled cyclic shift whose controls precede it on the tape.",
    mot("Agarwal and Cooley's Chinese-remainder split is used with coordinate powers chosen so that the change of order is a sequence of controlled cyclic shifts.", "explicit",
        r"with coordinate powers that make the change of order a"),
    [
        infer("S5.1a",
              r"The map respects $x^S=1$, and the image of $x$ has order $S$ because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so the powers of the image run through all $S$ target monomials exactly once; hence $\Phi$ is an isomorphism and preserves cyclic convolution.",
              r"group has size $S$, and the image of $x$ has order $S$, because each"),
        infer("S5.1b",
              r"For $k=\sum_{j=1}^da_jP_j$ with $0\le a_j<s_j$ the coordinate of $\Phi(x^k)$ in axis $i$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, since terms with $j>i$ are divisible by $s_i$ and $\mu_iP_i\equiv1$.",
              r"Indeed terms with $j>i$ are divisible by $s_i$, and $\mu_iP_i=1$ modulo"),
        infer("S5.1c",
              r"Insert the zero padding in one nested scan of the box $\prod[0,t_i)$ (copy the next coefficient where every $a_i<s_i$, write a zero record elsewhere), reorder the axes to $(a_1,\ldots,a_d)$ and update the targets in the order $i=d,d-1,\ldots,1$, so that when target $i$ is updated none of its lower-index controls has yet changed.",
              r"order $i=d,d-1,\ldots,1$ using \eqref{eq:triangular-crt}.  When target"),
        infer("S5.1d",
              r"On a fixed control prefix rotate the valid target interval $[0,s_i)$ by the offset and fix $[s_i,t_i)$ (identity if any lower control is invalid); this is a bijection of the padded box preserving the valid set and its complement, so zero padding stays zero, and the inverse processes $i=1,\ldots,d$ subtracting the same expression.",
              r"permutation of the valid target interval and the identity elsewhere."),
        infer("S5.1e",
              r"Each triangular update is a prefix-controlled cyclic shift: split the valid target interval into two consecutive pieces and merge them in opposite order, with at most $T/t_i$ control prefixes so offsets cost $O(dTp^C/r)=o(Tp)$; reversing the axes uses $O(d^2)$ unequal-width adjacent swaps, so $\Phi$, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$.",
              r"Each triangular update is a prefix-controlled cyclic shift.  The"),
    ],
    page="crt-axis-map",
    frm=["controlled-shift", "chunk-interchange", "tape-stream-operations", "cyclic-convolution", "modular-arithmetic", "primes-coprimality-and-the-extended-euclidean-algorithm", "positional-number-systems-and-carries", "convolution-of-sequences"],
    adds=[
        add(r"P_i", "prefix product", "The integer product $\\prod_{j<i}s_j$ of the lengths of the lower axes (not a Fourier permutation).", "count"),
        add(r"\mu_i", "CRT exponent", "The inverse of $P_i$ modulo $s_i$.", "count"),
        add(r"\Phi", "CRT algebra map", "The algebra isomorphism sending $x$ to $\\prod_ix_i^{\\mu_i}$.", "direct"),
    ])

# ---------------------------------------------------------------- S5.2 twist
s52 = show(
    "S5.2",
    r"With $\zeta=e^{\pi i/r}$ the map $\Theta:\mathbb C[x_d]/(x_d^r-1)\to\mathcal R_r$, $x_d\mapsto\zeta y$ multiplies coefficient $k$ by $\zeta^k$ and is an isomorphism preserving the sup norm, so $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$ is a normalized complex cyclic convolution computed by the ring convolution.",
    r"Show that $\Theta$ is well defined because $(\zeta y)^r=(-1)(-1)=1$, that it is diagonal in the coefficient bases with nonzero entries, and that the wrap sign $(-1)^h$ of the negacyclic product is exactly cancelled by $\zeta^{rh}=(-1)^h$; then compute twist and untwist with approximate phases and one truncation each.",
    mot("The power-of-two complex convolution needed in the chirp identity is obtained from the synthetic convolution by a coefficient twist.", "explicit",
        r"The power-of-two complex convolution used in the chirp identity is"),
    [
        infer("S5.2a",
              r"$\Theta$ is well defined since $(\zeta y)^r=(-1)(-1)=1$; on the bases $(x_d^k)$ and $(y^k)$ it is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$, hence an isomorphism with inverse multiplying by $\zeta^{-k}$, and both preserve the coefficient sup norm.",
              r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."),
        infer("S5.2b",
              r"For $k+l=j+hr$ with $h\in\{0,1\}$ a product term after twisting and negacyclic reduction has factor $\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
              r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j."),
        infer("S5.2c",
              r"Identify $f$ with an array of $M=T/r$ records by $\iota$ (a change of shape descriptor only, since the last coordinate is the contiguous polynomial suffix and $w_{\rm c}=p+2$ matches the synthetic width); the computed convolution twists by $Q_p(\widetilde\theta^+\cdot f)$, applies $\widetilde{\mathcal M}_r$ and untwists by $Q_p(\widetilde\theta^-\cdot\iota^{-1}h')$, so that $\mathcal M_{\mathbb C}(f,g)$ is approximated, with the $2r$th roots of unity from the cited exponential routine at cost $O(p^{1+\delta})$ per factor.",
              r"For $0\le k<r$, obtain disk-grid approximations"),
    ],
    page="phase-twist",
    frm=["negacyclic-ring", "cyclic-convolution", "roots-of-unity", "complex-numbers", "polynomials", "convolution-of-sequences", "contraction-error"],
    adds=[
        add(r"\zeta", "twist root", "The root of unity $e^{\\pi i/r}$ with $\\zeta^r=-1$.", "direct"),
        add(r"\Theta", "twist isomorphism", "The algebra isomorphism $x_d\\mapsto\\zeta y$ from $\\mathbb C[x_d]/(x_d^r-1)$ to $\\mathcal R_r$.", "direct"),
        add(r"\mathcal M_{\mathbb C}", "complex normalized convolution", "The normalized cyclic convolution $(f*g)/T$ of complex arrays on the $d$ axes.", "direct"),
    ])

# ---------------------------------------------------------------- S5.3 chirp and source transform (unpaged)
s53 = show(
    "S5.3",
    r"The computed chirp transform $\widetilde{\mathscr C}$ and the computed source transform $\widetilde{\mathscr F}=2^\gamma\widetilde{\mathcal B}_0\widetilde{\mathscr C}\widetilde{\mathcal A}$ have exact counterparts $QF_{\boldsymbol t}$ and $RF_{\boldsymbol s}$, with the opposite-sign procedure obtained by conjugation.",
    r"Evaluate the chirp identity numerically as phase multiplication, complex convolution with the kernel $\widetilde a$, and another phase multiplication, then wrap it between the computed expansion $\widetilde{\mathcal A}$ and compression $\widetilde{\mathcal B}_0$ and scale exactly by $2^\gamma$.",
    mot("The chirp identity turns the middle transform together with its target permutation into a convolution, which the complex convolution procedure already supplies.", "recoverable"),
    [
        infer("S5.3a",
              r"With $\widetilde a$ the disk-grid chirp, $x_0=Q_p(\overline{\widetilde a}\cdot x)$, $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$ and $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$; replacing the approximations by exact phases and exact convolution gives $\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)=QF_{\boldsymbol t}x$, and the phase numerators are computed modulo $2r$ as $-\sum_is_ij_i^2(r/t_i)$ at cost $O(dp^{1+\delta})$ per entry.",
              r"Thus $\widetilde a$ is the convolution kernel and $x_0$ is the data"),
        infer("S5.3b",
              r"For a source disk-grid tensor of norm at most $.5$, $\widetilde{\mathscr F}$ applies the linewise expansion $\widetilde{\mathcal A}$, the chirp transform $\widetilde{\mathscr C}$, the linewise compression $\widetilde{\mathcal B}_0$ and an exact scaling of the grid numerators by $2^\gamma$ (appending $\gamma$ zero bits), with exact counterpart $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$; the opposite-sign procedure is $\widetilde{\mathscr F}^+(z)=\overline{\widetilde{\mathscr F}(\overline z)}$.",
              r"For a source disk-grid tensor of norm at most $.5$, write"),
    ])

# ---------------------------------------------------------------- S5.4 algorithm (unpaged)
s54 = show(
    "S5.4",
    r"The algorithm places the radix-$2^b$ digits $a_j2^{-b-2}$ on the prime axes by $\Phi$, computes $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$, multiplies pointwise with one truncation, applies $\widetilde{\mathscr F}^+$, rescales by $S$ and $2^{2b+4}S$, rounds, inverts $\Phi$ and propagates carries to output exactly $2n$ bits.",
    r"Compose the preceding procedures in the order of the convolution theorem: two forward source transforms, a pointwise product, one opposite-sign source transform, and undo the two known normalizations.",
    mot("The source-transform procedures supply the three transforms needed for the radix-digit convolution.", "explicit",
        r"The source-transform procedures now supply the three transforms needed"),
    [
        infer("S5.4a",
              r"Read each operand backward in groups of $b$ bits to get the digits $a_0,\ldots,a_{q-1}$, write $a_j2^{p-b-2}$ as a signed $w_{\rm c}$-bit real word with a zero imaginary word (exactly $a_j2^{-b-2}$), append $S-q$ zero records, then: (1) apply $\Phi$; (2) compute $\widetilde{\mathscr F}(u)$, $\widetilde{\mathscr F}(v)$; (3) multiply exactly and truncate to $z$; (4) compute $\widetilde{\mathscr F}^+(z)$ times $S$; (5) multiply by $2^{2b+4}S$, round, apply $\Phi^{-1}$ with padding removal; (6) propagate carries and output $2n$ bits.",
              r"With these streams prepared, perform the following operations."),
        infer("S5.4b",
              r"By the cancellation identity the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$ and the second scale by $2^{2b+4}S$ gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution.",
              r"The two occurrences of $S$ in this algorithm undo different"),
    ],
    frm=["crt-axis-map", "permutation-cancellation", "phase-twist", "radix-digit-convolution", "ring-convolution", "dft"])

# ---------------------------------------------------------------- S5.5 exact recovery
s55 = show(
    "S5.5",
    r"All computed arrays stay in the disk, the error of the recovered scaled coefficients is below $448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<\frac12$, so rounding to the nearest integer gives the exact product coefficients $c_j\in[0,2^{3b})$ and carry propagation outputs the exact $2n$-bit product.",
    r"Track the norms (operands at most $.5$, $.6$, $.7$) and errors through each procedure by contraction and bilinear-contraction bounds in units of $h_p=2^{-p}$, then undo the scales $S$ and $2^{2b+4}$ exactly; since the true coefficients are integers an error below $\frac12$ identifies them.",
    mot("The true coefficients are integers, so once the error is strictly below $1/2$ the nearest integer is the unique correct coefficient.", "explicit",
        r"The strict error below $1/2$ makes the nearest integer to"),
    [
        infer("S5.5a",
              r"For a phase $e$ with disk-grid approximation $|\widetilde e-e|<2h_p$ and disk operand $x$, $\|Q_p(\widetilde ex)-ex\|<(2\|x\|+\sqrt2)h_p<4h_p$ and $\|Q_p(\widetilde ex)\|\le\|x\|$; for a bilinear contraction, $\|\mathcal M(f',g')-\mathcal M(f,g)\|\le\|f'-f\|\|g'\|+\|f\|\|g'-g\|$, so errors of disk operands add.",
              r"We also need the norm as well as the error of a computed phase product."),
        infer("S5.5b",
              r"The ring convolution error before the scale is below $3L+2$ units (three transforms and the product truncation), so after the scale $M$ the error is $E_{\rm ring}:=M(3L+2)<5TL$, where $L=\log_2T$; if one operand has norm at most $.7$ the output norm is below $.7+5TLh_p<.701$.",
              r"E_{\rm ring}:=M(3L+2)<5TL."),
        infer("S5.5c",
              r"The computed complex convolution differs from $\mathcal M_{\mathbb C}$ by less than $(E_{\rm ring}+4+4+4)h_p<6TLh_p$ (two input twists, the ring approximation and the output untwist), and its output has norm below $.701$.",
              r"<6TLh_p."),
        infer("S5.5d",
              r"For the chirp transform of an input of norm at most $.6$ the errors add up as $\|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\|<(6TL+2+4+4)h_p<8TLh_p$ (kernel approximation $2$, first phase $4$, convolution $6TL$, last phase $4$), with output norm below $.701$.",
              r"<(6TL+2+4+4)h_p<8TLh_p."),
        infer("S5.5e",
              r"For a source tensor of norm at most $.5$ the expansion has error below $dp^2$ and norm below $.51$, and inserting the exact contractions $\mathcal A$, $QF_{\boldsymbol t}$, $\mathcal B_0$ gives error below $2dp^2+8TL$ before the scale, hence $E_s:=9\cdot2^\gamma TL$ after multiplying by $2^\gamma$ (using $2dp^2<TL$), with output norm below $.501$.",
              r"E_s=9\,2^\gamma TL,"),
        infer("S5.5f",
              r"For the scaled radix digits $u,v$ (norm below $1/4$) the exact transforms $U,V_1$ have norm below $1/4$ and the computed ones below $.26$, so $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has norm at most $.26^2<.5$ and $\|z-U\cdot V_1\|<(2E_s+2)h_p$; then, inserting $G=RF_{\boldsymbol s}^+$, $\|\widetilde{\mathscr F}^+(z)-G(U\cdot V_1)\|<(3E_s+2)h_p$.",
              r"\|z-U\cdot V_1\|<(2E_s+2)h_p$."),
        infer("S5.5g",
              r"After the first exact scale by $S$ the array $\widetilde w$ approximates $w=(u*v)/S$ with error below $E_wh_p$, $E_w:=S(3E_s+2)<28\cdot2^\gamma T^2L$, and $\|w\|<1/16$ (each coefficient averages $S$ products), so $\|\widetilde w\|<1/16+10^{-3}<1$.",
              r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
        infer("S5.5h",
              r"The unscaled integer coefficient array is $2^{2b+4}Sw$, so its error is below $2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}<448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<\frac12$, using $S\le T<2^b$, $L<b$ and $\gamma\le b/4$ ($p=6b$).",
              r"<448b\,2^{-b+\gamma}"),
        infer("S5.5i",
              r"Rounding the represented value $H_j/2^p$ to the nearest integer therefore recovers the true coefficient $c_j$, which lies in $[0,2^{3b})$ by the capacity bound and so fits a signed $(3b+1)$-bit word; the exact record widths $w_{\rm c}+b$, $w_{\rm c}+2b$ and $w_{\rm c}+4b+4$ of the scalings are $O(p)$.",
              r"The true coefficients are real integers."),
        infer("S5.5j",
              r"With $Q_0=2^b$, $k_0=0$, $d_j=(c_j+k_j)\bmod Q_0$, $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$ the carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$ (since $c_j+k_j\le qQ_0(Q_0-1)$) and the invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ holds; the stream of $O(Sb)=O(Tp)$ bits is reversed once and exactly $2n$ bits are output, the product being less than $2^{2n}$.",
              r"To propagate carries, let $Q_0=2^b$."),
    ],
    page="exact-recovery",
    frm=["contraction-error", "radix-digit-convolution", "fixed-point-numbers-dyadic-rationals-and-rounding", "positional-number-systems-and-carries", "kronecker-packing", "guard-bits", "vector-norms-and-the-triangle-inequality", "convolution-of-sequences"],
    adds=[
        add(r"h_p", "grid unit", "The grid spacing $2^{-p}$; an error of $a$ means absolute error less than $ah_p$.", "direct"),
        add(r"L", "log of entry count", "The integer $\\log_2T$.", "count"),
        add(r"E_s", "source error", "The error bound $9\\cdot2^\\gamma TL$ (in units of $h_p$) of the computed source transform.", "direct"),
        add(r"E_w", "scaled error", "The error bound $S(3E_s+2)<28\\cdot2^\\gamma T^2L$ of the first scaled result $\\widetilde w$.", "direct"),
    ],
    salient=r"The final error is exponentially small in $b$, below $448b\,2^{-3b/4}$, although each intermediate step loses a factor like $2^\gamma TL$: the precision $p=6b$ leaves room for the scales $S$, $2^{2b+4}$ and $2^\gamma$ with $\gamma=o(b)$ to be undone and still keep the error below $\frac12$.")

s5 = show(
    "S5",
    r"The multiplication algorithm: place the digits on the prime axes by $\Phi$, apply the source transform to both operands, multiply pointwise, apply the opposite-sign transform, rescale, round and carry, producing the exact $2n$-bit product.",
    r"Reduce the product to the convolution of the radix-digit coefficient lists, compute the cyclic convolution by the convolution theorem using transforms of prime-product length evaluated through resampling, chirp convolution and the polynomial-ring convolution, and prove by a norm and error budget that rounding recovers the exact coefficients.",
    mot("The precision budget is what links the numerical transforms to an exact integer answer.", "recoverable"),
    [s51, s52, s53, s54, s55],
    page="multiplication-algorithm",
    frm=["crt-axis-map", "phase-twist", "exact-recovery", "permutation-cancellation", "ring-convolution", "gaussian-resampling", "chirp-identity", "dft", "parameter-choice", "radix-digit-convolution", "cyclic-convolution", "convolution-of-sequences"],
    adds=[])

# ---------------------------------------------------------------- S6 time bound
rows = [
    ("S6.1a", r"Prefix-slot moves and individual butterfly rounds: normalized cost $dK$, a power $p^{\epsilon(1+c)}$ of $p$, with margin $g_1=1-\epsilon(1+c)$.",
     r"Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\"),
    ("S6.1b", r"Chunk exchanges for the transform layout: normalized cost $pK^{\tau-1}$, a power $p^{1-\epsilon c(1-\tau)}$, with margin $g_2=\epsilon c(1-\tau)$.",
     r"Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\"),
    ("S6.1c", r"Simultaneous butterfly rounds: normalized cost $\ell d^{\lambda'}$, a power $p^{1-\epsilon(1-\lambda')}$, with margin $g_3=\epsilon(1-\lambda')$.",
     r"Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\"),
    ("S6.1d", r"CRT and axis layouts: normalized cost $d^2(1+\ell^\tau)$, a power $p^{\tau+\epsilon(2-\tau)}$, with margin $g_4=1-\tau-\epsilon(2-\tau)$.",
     r"CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\"),
    ("S6.1e", r"Gaussian line maps: normalized cost $dp^{1/2+\delta}\alpha$, a power $p^{3/4+\delta+3\epsilon/2}$, with margin $g_5=\frac14-\delta-\frac32\epsilon$.",
     r"Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\"),
    ("S6.1f", r"Chirps, twists and scalar products: normalized cost $dp^\delta$, a power $p^{\epsilon+\delta}$, with margin $g_6=1-\delta-\epsilon$.",
     r"Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\"),
    ("S6.1g", r"Packed polynomial products: normalized cost $\log(rp)$, a power $p^{1-\epsilon}$, with margin $g_7=\epsilon$ (final scaling and rounding cost $p^\delta$, and input, padding, carries and output cost $1$, both absorbed).",
     r"Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\"),
]
s61 = show(
    "S6.1",
    r"After division by the volume $V=Tp=\Theta(n)$, seven dominant normalized costs have powers of $p$ strictly below one, with margins $g_1,\ldots,g_7$ below one.",
    r"List the cost of each operation of the algorithm divided by $V=Tp$ in a table (a fixed number of repeated transforms and convolutions is absorbed in the constants) and read off the power of $p$ it contributes.",
    mot("Dividing by $Tp$ turns each cost into a power of $p$, and a power saving is a power strictly below one.", "recoverable"),
    [infer(i, c, q) for (i, c, q) in rows],
    adds=[
        add(r"g_1", "first margin", "The margin $1-\\epsilon(1+c)>\\frac12$ of the prefix-slot and individual-butterfly term below one.", "direct"),
        add(r"g_2", "second margin", "The margin $\\epsilon c(1-\\tau)=2^{-181}$ of the chunk-exchange term below one.", "direct"),
        add(r"g_3", "third margin", "The margin $\\epsilon(1-\\lambda')=2^{-129}$ of the simultaneous-butterfly term below one.", "direct"),
        add(r"g_4", "fourth margin", "The margin $1-\\tau-\\epsilon(2-\\tau)>2^{-51}$ of the CRT and axis-layout term below one.", "direct"),
        add(r"g_5", "fifth margin", "The margin $\\frac14-\\delta-\\frac32\\epsilon>\\frac18$ of the Gaussian line-map term below one.", "direct"),
        add(r"g_6", "sixth margin", "The margin $1-\\delta-\\epsilon>\\frac12$ of the chirp, twist and scalar-product term below one.", "direct"),
        add(r"g_7", "seventh margin", "The margin $\\epsilon=2^{-75}$ of the packed polynomial product term below one.", "direct"),
    ])

s62 = infer(
    "S6.2",
    r"Direct substitution gives $g_1>\frac12$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>\frac18$, $g_6>\frac12$, $g_7=2^{-75}$, so $\min_ig_i=2^{-181}=2\kappa$, which leaves explicit slack for any fixed power of $\log p$.",
    r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad",
    salient=r"The smallest margin is $g_2=\epsilon c(1-\tau)=2^{-75}\cdot2^{-56}\cdot2^{-50}=2^{-181}$, from the chunk-exchange term $pK^{\tau-1}$, and $\kappa=2^{-182}$ is exactly half of it: the final saving is limited by how little the chunk width $K=\Theta(p^{\epsilon c})$ grows.")

s63 = show(
    "S6.3",
    r"Each of the seven rows follows from the earlier cost lemmas: the first three are the three terms of the synthetic transform cost, the fourth from $O(d^2)$ axis moves, the fifth from the line maps over $\sum_iT/t_i$ lines, the sixth and seventh from exact products on $O(p)$-bit numerators and four integer products per polynomial record.",
    r"Substitute the size relations $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$, $\alpha=\Theta(p^{1/4+\epsilon/2})$ into the cost of each lemma.",
    mot("The row costs are stated for the lemmas but the table needs them as powers of $p$, which the size relations convert.", "recoverable"),
    [
        infer("S6.3a",
              r"Row 2: the positional layout uses $O(p/K)$ exchanges of width-$K$ chunks (because $d\ell=O(p)$), each costing $O(VK^\tau)$ by the chunk-swap lemma, so the normalized total is $O(p/K)K^\tau=O(pK^{\tau-1})$; row 3 is the $\ell$ simultaneous rounds at $O(Vd^{\lambda'})$ each, and row 1 the $O(dK)$ linear scans of prefix slots, so $\ell d^{\lambda'}=\Theta(p^{1-\epsilon+\epsilon\lambda'})$ and $pK^{\tau-1}=\Theta(p^{1-\epsilon c(1-\tau)})$.",
              r"Its positional layout uses $O(p/K)$ exchanges"),
        infer("S6.3b",
              r"Row 4: axis exposure and restoration need $O(d^2)$ adjacent axis moves, each $O(V(1+\ell^\tau))$ (peel a single excess bit when widths differ by one, exchange the equal parts, restore the bit), and the $d$ CRT rotations cost $O(dV)$ with offset setup $o(Tp)$.",
              r"Axis exposure and restoration require $O(d^2)$ adjacent axis moves."),
        infer("S6.3c",
              r"Row 5: axis $i$ has at most $T/t_i$ lines, so the line machines cost $\sum_{i=1}^d\frac T{t_i}O(t_ip^{3/2+\delta}\alpha)=O(dTp^{3/2+\delta}\alpha)$, and dividing by $V=Tp$ with $\alpha=\Theta(p^{1/4+\epsilon/2})$ gives $dp^{1/2+\delta}\alpha=\Theta(p^{3/4+\delta+3\epsilon/2})$.",
              r"Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines."),
        infer("S6.3d",
              r"Rows 6 and 7: chirp numerators $-\sum_is_ij_i^2(r/t_i)\bmod2r$ are sums of $d$ terms computed with the established multiplier in $O(dp^{1+\delta})$ per entry, the smaller twist and scalar products fit the same row, the two final products by $S$ cost $O(p^\delta)$ normalized, and there are $T/r$ pointwise ring products, each four integer products on $O(rp)$ bits, totalling $O(Tp\log(rp))$ with $\log(rp)=O(p^{1-\epsilon})$; these calls use the previously established multiplier on records of length $O(rp)=o(n)$, not the algorithm being constructed.",
              r"Chirp numerators have $O(p)$ bits and can be computed modulo $2r$ as"),
    ],
    frm=["transform-layout", "chunk-interchange", "ring-convolution", "kronecker-packing", "permutation-cancellation", "crt-axis-map", "hh-multiplier"])

s64 = show(
    "S6.4",
    r"Setup, descriptor and exceptional-stream work over all calls totals $o(Tp)$: there are at most $p^A$ visits of layer and layout nodes with setup $p^C$ each, $O(p^C)$ work per polynomial record or Gaussian line is $O(dTp^C/r)=o(Tp)$, and the sorting of exceptional records costs $O(Vp^{A'}2^{-K})=o(V)$.",
    r"Separate the work done once per recursion node, per polynomial record, per Gaussian line and per exceptional record, and bound each by a power of $p$ against the super-polynomial $r$ or the factor $2^{-K}$.",
    mot("These costs are not in the table but would break a power saving if they were comparable to $Tp$.", "reconstructed"),
    [
        infer("S6.4a",
              r"Layer and address-layout recursions have constant branching and depth $O(\log p)$, with polynomially many rounds and base-$m$ groups, so there are at most $p^A$ visits and descriptor setup $p^C$ per visit costs $p^{A+C}=o(Tp)$; per-record descriptor or address work over these visits is at most $O(Tp^{A+C}/r)=o(Tp)$ and setup per Gaussian line is $O(dTp^C/r)=o(Tp)$ since $r$ exceeds every fixed power of $p$.",
              r"At a layer or synthetic-transform visit that processes polynomial"),
        infer("S6.4b",
              r"For a packed change of basis the bad-address fraction is $O(d2^{-K})$ independently of payload, so the compact exceptional stream has length $O(V_{\rm call}d2^{-K})$ and stable bit sorting makes $O(p)$ scans of it, for total cost $O(dp2^{-K}\sum_{\rm calls}V_{\rm call})=O(Vp^{A'}2^{-K})=o(V)$ because $K=\Theta(p^{\epsilon c})$ with $\epsilon c>0$; this is a deterministic worst-case bound.",
              r"The bad-address fraction is"),
        infer("S6.4c",
              r"All role, arithmetic and stack tapes form fixed finite families: a child parks and restores only its parent's streams with the stack head at the active top, copying and cleanup are charged to that logical volume and no operation rescans parked ancestors; global setup and prime search cost $o(V)$.",
              r"Finally, all role, arithmetic, and stack tapes form fixed finite"),
    ],
    frm=["tape-stream-operations", "packed-selected-bit-addition", "chunk-interchange", "prime-axis-lengths"])

s65 = infer(
    "S6.5",
    r"Each of the seven powers is at most $1-2\kappa$ and any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the cost is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ for large $n$.",
    r"Each of the seven displayed powers is at most $1-2\kappa$ by")

s66 = infer(
    "S6.6",
    r"Below one fixed cutoff beyond all the size, precision, margin and layout conditions use schoolbook multiplication, absorbing the finitely many smaller lengths into the implicit constant; with $\lg n=\max\{\lceil\log_2n\rceil,1\}$ the single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ and outputs exactly the $2n$-bit product.",
    r"Fix one cutoff beyond all the size, precision, margin and layout",
    frm=["schoolbook-and-karatsuba-multiplication", "big-o-notation"])

s6 = show(
    "S6",
    r"The total time is $O(Tp\cdot p^{1-\kappa})=O(n(\lg n)^{1-\kappa})$: divided by $V=Tp$, seven dominant terms have powers of $p$ below one with smallest margin $2\kappa$, all other work is $o(V)$, and powers of $\log p$ are absorbed in the slack.",
    r"Tabulate the normalized cost of every operation in the algorithm, bound the exponent of $p$ of each of the seven dominant terms by a margin $g_i$ computed from the fixed rational exponents, show that setup and exceptional work is $o(Tp)$, and absorb any remaining fixed power of $\log p$ in the smallest margin $2\kappa$.",
    mot("This explicit slack will cover any remaining fixed power of $\\log p$.", "explicit",
        r"This explicit slack will cover"),
    [s61, s62, s63, s64, s65, s66],
    page="time-bound",
    frm=["multiplication-algorithm", "parameter-choice", "transform-layout", "simultaneous-butterfly-layer", "chunk-interchange", "permutation-cancellation", "crt-axis-map", "ring-convolution", "kronecker-packing", "logarithms-exponentials-floors-and-ceilings", "big-o-notation", "asymptotic-notation-beyond-big-o"],
    salient=r"Seven different costs, each from a different lemma, are all pushed below $p^{1}$ by margins that are tiny powers of $2$; the cost is therefore not a single recurrence but the smallest of seven margins, and it is the one coming from the chunk exchanges, $\epsilon c(1-\tau)$.")

# ---------------------------------------------------------------- S7 refutation (deferred)
s7 = infer(
    "S7",
    r"Since $T_A(n)/(n\lg n)\to0$ through all input lengths, one machine $A$ has $\liminf_{n\to\infty}T_A(n)/(n\lg n)=0$, which negates an eventual lower bound $T_A(n)\ge c_An\lg n$ for every fixed multiplication machine; so the Sch\\\"onhage-Strassen $n\log n$ optimality conjecture fails in this model.",
    r"The power saving proved here gives a limit of zero through all input lengths,",
    frm=["schonhage-strassen-conjecture", "limits-and-limit-inferior", "asymptotic-notation-beyond-big-o"],
    deferred=True)
