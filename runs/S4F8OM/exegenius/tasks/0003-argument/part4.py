"""S5: the multiplication algorithm; S6: cost; S7: the refutation; the root."""
from tree_helpers import show, infer, mot, bind
from part1 import S1
from part2 import S2
from part3 import S3, S4

# ---------------------------------------------------------------- S5.1
S51 = show(
    "S5.1",
    r"For large $n$, the choices $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$, axis lengths $t_i\in\{r/2,r\}$ with $\prod_it_i=T$, $\alpha=\lceil(12d^2b)^{1/4}\rceil$ and distinct odd primes $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ with $\eta=1/(4d)$ give $Tp=\Theta(n)$ and $T/2<S<T$, and satisfy every hypothesis of the layer, transform and resampling interfaces.",
    r"Fix rational exponents with explicit margins, derive the size relations from them, and find the primes in two disjoint intervals by an explicit prime-counting bound and a deterministic trial-division search.",
    mot(r"The prime lengths must be close enough to the powers of two that the padded box wastes only a constant factor, yet far enough below them for the resampling condition $\alpha^4\theta>p$; the dimension $d=b^\epsilon$ makes records of length $r=2^{\Theta(p^{1-\epsilon})}$, long enough to absorb all per-record bookkeeping.",
        "explicit",
        r"The distinct prime lengths $s_i$ must be close to the powers of two $t_i$: their product must occupy a fixed fraction of the padded box, while each ratio $t_i/s_i$ must leave enough separation for resampling."),
    [
        infer("S5.1.1",
              r"The fixed choice $\tau=\sigma=1-2^{-50}$, $\lambda=1-2^{-52}$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\epsilon=2^{-75}$ and $\delta=1/16$ satisfies $\tau(1+2c)<\lambda$, $(1+\sigma)/2<\lambda<\lambda'<1$, $20\epsilon<1$ and the other required inequalities, the strict final inequality absorbing the logarithmic number of base-$m$ groups.",
              r"The strict final inequality absorbs the logarithmic number of groups in a base-$m$ partition."),
        infer("S5.1.2",
              r"These definitions give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$, with comparison constants fixed for all $n$, so $r$ exceeds every fixed power of $p$ and $K/\log p\to\infty$.",
              r"The comparison constants can be fixed for every input length at once."),
        infer("S5.1.3",
              r"Since $\alpha\le2(12d^2b)^{1/4}$, the scale exponent satisfies $\gamma=2d\alpha^2<28b^{2/3}$, so $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$.",
              r"It follows that $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$."),
        infer("S5.1.4",
              r"For $x=r/2$ and $x=r$ the interval $((1-2\eta)x,(1-\eta)x]$ contains at least $x/(8d\log x)>d$ primes by the explicit prime-interval bound, and the two intervals are disjoint, so distinct odd primes $s_i$, coprime to the powers of two $t_i$, can be chosen.",
              r"We may therefore choose distinct odd primes satisfying"),
        infer("S5.1.5",
              r"Then $S/T>(1-1/(2d))^d>1/2$, and $t_i/s_i-1>\eta$ gives $\alpha^4(t_i/s_i-1)>3db\ge p$, so every hypothesis of the one-dimensional resampling lemma holds for large $n$.",
              r"Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for all sufficiently large input lengths."),
        infer("S5.1.6",
              r"Scanning both intervals by trial division costs $O(dr^{3/2}\operatorname{poly}(p))=n^{o(1)}=o(n)$ and all other setup is polynomial in $p$, so the machine computes its parameters instead of receiving them as advice.",
              r"Since $p=6\lceil\log_2 n\rceil=\Theta(\log n)$, the search takes $n^{o(1)}=o(n)$ time."),
    ],
    page="parameter-regime",
    frm=["simultaneous-butterfly-layer", "transform-tape-layout", "gaussian-resampling", "crt-axis-map", "primes-coprimality-and-gcd", "asymptotic-notation-beyond-big-o"],
    adds=[
        bind(r"\epsilon", "dimension exponent", r"The fixed exponent $2^{-75}$ with $d=\lfloor b^\epsilon\rfloor$.", "direct"),
        bind("c", "chunk exponent", r"The fixed exponent $2^{-56}$ with $K=\lfloor d^c\rfloor$.", "direct"),
        bind(r"\eta", "prime gap ratio", r"The ratio $1/(4d)$ fixing how far below its power of two each prime length lies.", "direct"),
    ],
)

# ---------------------------------------------------------------- S5.2
S52 = show(
    "S5.2",
    r"Writing the inputs as polynomials in $2^b$ with $\lceil n/b\rceil$ nonnegative digits each, their product polynomial has degree below $S$, so its cyclic convolution modulo $x^S-1$ has no wraparound, every coefficient satisfies $0\le c_j<2^{3b}$, and the integer product is $\sum_jc_j2^{bj}$.",
    r"Evaluate the digit polynomials at $2^b$ and bound the degree and the coefficients of their product.",
    mot(r"The integer product is the product of the digit polynomials evaluated at $2^b$, and the product's coefficients form a convolution of short digit lists, which fast Fourier methods compute; carries then perform the evaluation.",
        "explicit",
        r"Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients."),
    [
        infer("S5.2.1",
              r"The product has degree at most $2\lceil n/b\rceil-2<2n/b\le T/2<S$, so convolution modulo $x^S-1$ has no nonzero wraparound.",
              r"Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
        infer("S5.2.2",
              r"Each coefficient is a sum of at most $\lceil n/b\rceil\le n\le2^b$ products of digits below $2^b$, so $0\le c_j\le\lceil n/b\rceil(2^b-1)^2<2^{3b}$.",
              r"since $q\le n\le2^b$."),
    ],
    page="radix-digit-reduction",
    frm=["convolution", "positional-notation-in-any-radix", "polynomials", "schoolbook-and-karatsuba-multiplication"],
    adds=[
        bind("c_j", "product coefficient", r"The $j$th coefficient of the product of the two digit polynomials, an integer below $2^{3b}$.", "direct"),
    ],
)

# ---------------------------------------------------------------- S5.3
S53 = show(
    "S5.3",
    r"For pairwise coprime $s_1,\ldots,s_d$ with product $S$, the map $\Phi:x\mapsto\prod_ix_i^{\mu_i}$ with $\mu_i=(\prod_{j<i}s_j)^{-1}\bmod s_i$ is an algebra isomorphism $\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1)$ that preserves cyclic convolution, and on the zero-padded box it and its inverse are performed by triangular controlled shifts and axis reorderings in $O(Tp\,d^2(1+\ell^\tau))$ time.",
    r"Choose the exponents so that each new coordinate is the old mixed-radix digit plus a function of earlier digits, which makes the reindexing a sequence of cyclic shifts of one axis controlled by the preceding axes.",
    mot(r"A general Chinese-remainder reindexing scatters the coefficients and would need sorting; with these exponents each target coordinate depends only on earlier digits, so it is a controlled cyclic shift costing linear time, and only axis reorderings remain.",
        "explicit",
        r"The following map uses that algebraic split, with coordinate powers that make the change of order a sequence of controlled cyclic shifts."),
    [
        infer("S5.3.1",
              r"$\Phi$ respects $x^S=1$, and the image of $x$ has order $S$ because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all $S$ target monomials and $\Phi$ is an isomorphism preserving cyclic convolution.",
              r"Hence $\Phi$ is an isomorphism and preserves cyclic convolution."),
        infer("S5.3.2",
              r"For $k=\sum_ja_jP_j$ in mixed radix with prefix products $P_j=\prod_{h<j}s_h$, the coordinate of $\Phi(x^k)$ on axis $i$ is $a_i+\mu_i\sum_{j<i}a_jP_j\bmod s_i$, because terms with $j>i$ vanish modulo $s_i$ and $\mu_iP_i\equiv1$.",
              r"Indeed terms with $j>i$ are divisible by $s_i$, and $\mu_iP_i=1$ modulo $s_i$."),
        infer("S5.3.3",
              r"After the padded axes are reordered to $(a_1,\ldots,a_d)$ so that controls precede their target, updating the targets in the order $i=d,\ldots,1$ computes each offset from the still original lower digits.",
              r"When target $i$ is updated, none of its lower-index controls has yet changed, so the offset is computed from the original digits $a_j$ required by the formula."),
        infer("S5.3.4",
              r"On each control prefix the update rotates the valid interval $[0,s_i)$ and fixes $[s_i,t_i)$, and it is the identity when a control is invalid, a bijection that preserves the valid set, so zero padding stays zero.",
              r"Consequently zero padding remains zero after every step."),
        infer("S5.3.5",
              r"Each rotation is a prefix-controlled cyclic shift costing $O(Tp)$ with offset setup $o(Tp)$, and reversing the axes takes $O(d^2)$ adjacent swaps by chunk interchange at $O(Tp(1+\ell^\tau))$ each, so $\Phi$, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$.",
              r"Therefore the map $\Phi$, its inverse, and their padding operations cost"),
    ],
    page="crt-axis-map",
    frm=["convolution", "controlled-cyclic-shift", "address-chunk-interchange", "tape-address-model", "primes-coprimality-and-gcd", "modular-arithmetic"],
    adds=[
        bind(r"\mu_i", "CRT exponent", r"The inverse modulo $s_i$ of the product of the earlier source lengths.", "direct"),
    ],
)

# ---------------------------------------------------------------- S5.4.1
S541 = show(
    "S5.4.1",
    r"With $\zeta=e^{\pi i/r}$, the map $x_d\mapsto\zeta y$ is an isomorphism $\mathbb C[x_d]/(x_d^r-1)\to\mathbb C[y]/(y^r+1)$ that multiplies coefficient $k$ by $\zeta^k$, so normalized complex cyclic convolution on all $d$ axes equals the twisted ring convolution on the first $d-1$ axes: $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$.",
    r"Check that the twist respects $x_d^r=1$ and that every wrapped product term picks up the factor $\zeta^r(-1)=1$.",
    mot(r"The synthetic transforms need the last coordinate to be a polynomial modulo $y^r+1$, so that powers of $y$ supply the roots of unity; the twist converts the cyclic last axis into that form without changing the convolution.",
        "explicit",
        r"A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed."),
    [
        infer("S5.4.1.1",
              r"The assignment $x_d\mapsto\zeta y$ is well defined since $(\zeta y)^r=(-1)(-1)=1$, and it is diagonal on the monomial bases with nonzero factors $\zeta^k$, hence an isomorphism that preserves the coefficient sup norm.",
              r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."),
        infer("S5.4.1.2",
              r"Writing $k+l=j+hr$ with $h\in\{0,1\}$, a product term after twisting and negacyclic reduction has factor $\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
              r"Untwisting therefore recovers the cyclic coefficient with the correct sign."),
        infer("S5.4.1.3",
              r"Identifying the last axis with polynomial records ($\iota$) and twisting ($D_\pm$) are isometries, so $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$ is again a bilinear contraction.",
              r"The maps $D_\pm$ and $\iota^{\pm1}$ are isometries, so $\mathcal M_{\mathbb C}$ is also a bilinear contraction."),
    ],
    page="coefficient-twist",
    frm=["negacyclic-ring", "convolution", "roots-of-unity-and-euler-s-formula", "polynomials"],
    salient=r"The minus sign of the negacyclic wrap $y^r=-1$ is cancelled exactly by $\zeta^r=-1$, so untwisting returns the cyclic coefficient with the correct sign.",
    adds=[
        bind(r"\zeta", "twist root", r"The root of unity $e^{\pi i/r}$, of order $2r$, with $\zeta^r=-1$.", "direct"),
    ],
)

# ---------------------------------------------------------------- S5.4
S54 = show(
    "S5.4",
    r"For a source tensor of norm at most $1/2$ in the zero-padded power-of-two box, the procedure $\widetilde{\mathscr F}$ that applies the linewise approximation of $\mathcal A$, the computed chirp transform built on the complex cyclic convolution of length $T$, the linewise approximation of $\mathcal B_0$ and an exact scaling by $2^\gamma$ has exact counterpart $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, and conjugation gives $\widetilde{\mathscr F}^+$ for $RF_{\boldsymbol s}^+$.",
    r"Obtain the complex cyclic convolution of length $T$ from the ring convolution by twisting the last axis, wrap it in chirp phases to get $QF_{\boldsymbol t}$, and compose with the Gaussian line maps.",
    mot(r"Resampling reduces $RF_{\boldsymbol s}$ to $QF_{\boldsymbol t}$ between two contractions, the chirp identity reduces $QF_{\boldsymbol t}$ to a cyclic convolution on the power-of-two box, and the twist turns that into a convolution over $\mathcal R_r$ on the first $d-1$ axes, which the synthetic machinery computes.",
        "explicit",
        r"We next use the complex convolution to evaluate the middle factor $QF_{\boldsymbol t}$ in \eqref{eq:no-sort-tensor}, and then compose it with the Gaussian maps."),
    [
        S541,
        infer("S5.4.2",
              r"With disk-grid approximations $\widetilde\theta^\pm_k$ of $\zeta^{\pm k}$, the computed convolution twists both operands with one truncation each, calls the ring convolution and untwists with one truncation, costing $O(Tp^{1+\delta})$ beyond the ring convolution, while $\iota$ moves no payload because both formats store the last axis as the contiguous coefficient suffix.",
              r"Generating every factor anew therefore still gives total twist cost $O(Tp^{1+\delta})$.",
              frm=["fixed-point-complex-arithmetic", "normalized-ring-convolution"]),
        infer("S5.4.3",
              r"The chirp phases are computed from the numerators $-\sum_is_ij_i^2(r/t_i)\bmod2r$ in $O(dp^{1+\delta})$ time per entry, and the computed chirp transform $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,Q_p(\overline{\widetilde a}\cdot x)))$ has exact counterpart $QF_{\boldsymbol t}x$.",
              r"Thus chirp construction costs $O(Td p^{1+\delta})$ in total.",
              frm=["bluestein-chirp", "fixed-point-complex-arithmetic"]),
        infer("S5.4.4",
              r"The source transform $\widetilde{\mathscr F}$ applies linewise $\widetilde{\mathcal A}$, then $\widetilde{\mathscr C}$, then linewise $\widetilde{\mathcal B}_0$, then appends $\gamma$ zero bits to every numerator, all on the zero-padded power-of-two box, and $\widetilde{\mathscr F}^+(z)=\overline{\widetilde{\mathscr F}(\overline z)}$.",
              r"The source arrays are stored in the padded power-of-two box, with zeros outside the valid source coordinates.",
              frm=["gaussian-resampling", "permutation-cancellation"]),
    ],
    page="tensor-source-transform",
    frm=["gaussian-resampling", "bluestein-chirp", "normalized-ring-convolution", "permutation-cancellation", "coefficient-twist", "fixed-point-complex-arithmetic"],
    adds=[
        bind(r"\widetilde{\mathscr F}", "computed source transform", r"The numerical procedure that approximates $RF_{\boldsymbol s}$ on disk-grid source tensors.", "direct"),
    ],
)

# ---------------------------------------------------------------- S5.5
S55 = infer(
    "S5.5",
    r"By the permutation-cancellation identity the exact counterpart after the three transforms is $(u*v)/S^2$, so the first scaling by $S$ gives $w=(u*v)/S$ and the second, by $2^{2b+4}S$, gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the integer digit convolution, the factor $2^{2b+4}$ undoing the two input scales $2^{-b-2}$.",
    r"The two occurrences of $S$ in this algorithm undo different normalizations.",
    frm=["permutation-cancellation", "crt-axis-map", "radix-digit-reduction"],
)

# ---------------------------------------------------------------- S5.6
S56 = show(
    "S5.6",
    r"Every computed array stays in the unit disk without clipping, each source transform errs by less than $E_s=9\cdot2^\gamma T\log_2T$ grid units, and the final coefficient error is below $448b\,2^{-3b/4}<1/2$, so rounding returns the exact coefficients $0\le c_j<2^{3b}$ and carry propagation gives the exact $2n$-bit product.",
    r"Propagate errors through contractions and bilinear contractions so that they add rather than multiply, keep explicit norm margins so that every call receives disk inputs, and compare the scaled final error with $1/2$.",
    mot(r"The true coefficients are integers, so any approximation within less than $1/2$ determines them; contractions keep errors additive, so the final error is a sum of per-stage errors multiplied only by the known exact scales $S$, $2^{2b+4}$ and $2^\gamma$.",
        "explicit",
        r"The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient."),
    [
        infer("S5.6.1",
              r"With one operand of norm at most $0.7$, the returned ring convolution errs by less than $M(3\log_2T+2)<5T\log_2T$ grid units and has norm below $0.701$, so it is a disk array without clipping.",
              r"This proves the disk margin after the scale $M$, without clipping the output."),
        infer("S5.6.2",
              r"The computed complex convolution errs by less than $6T\log_2T$ grid units, and the computed chirp transform of an input of norm at most $0.6$ by less than $8T\log_2T$, each stage inserting the exact contraction at the computed input.",
              r"Equation~\eqref{eq:permuted-chirp} identifies the exact result, so"),
        infer("S5.6.3",
              r"For a source input of norm at most $1/2$, the errors below $dp^2$ of each Gaussian map and $8T\log_2T$ of the chirp give less than $2^\gamma(2dp^2+8T\log_2T)<E_s$ after the exact scale, and the output norm stays below $0.501$.",
              r"because $2dp^2<TL$ eventually."),
        infer("S5.6.4",
              r"The pointwise product $z$ of the two computed transforms errs by less than $2E_s+2$, the opposite-sign transform adds $E_s$, and the exact scale by $S$ gives $\widetilde w$ within $E_w=S(3E_s+2)<28\cdot2^\gamma T^2\log_2T$ grid units of $w=(u*v)/S$.",
              r"The first exact numerator multiplication by $S$ gives $\widetilde w$, approximating $w=(u*v)/S$ with error less than $E_wh_p$, where"),
        infer("S5.6.5",
              r"After the second exact scale, $S\le T<2^b$, $\log_2T<b$ and $\gamma\le b/4$ bound the final error by $2^{2b+4}S\cdot28\cdot2^\gamma T^2\log_2T\cdot2^{-6b}<448b\,2^{-3b/4}<1/2$, so rounding gives each integer coefficient exactly.",
              r"Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than"),
        infer("S5.6.6",
              r"Propagating radix-$2^b$ carries in increasing order keeps each carry below $2^{2b}$ and maintains $\sum_{h<j}c_h2^{bh}=\sum_{h<j}d_h2^{bh}+k_j2^{bj}$, which fixes the product's digits; since the product is below $2^{2n}$, exactly $2n$ bits are output.",
              r"The unprocessed terms are multiples of $Q_0^j$, so the identity fixes the first $j$ radix digits of the full product."),
    ],
    page="precision-exact-recovery",
    frm=["contraction-error-propagation", "fixed-point-complex-arithmetic", "tensor-source-transform", "radix-digit-reduction", "normalized-ring-convolution", "triangle-inequality-and-norms"],
    salient=r"A computation built from truncated fixed-point Fourier transforms returns the product exactly, because with precision $p=6b$ the final error $448b\,2^{-3b/4}$ is far below $1/2$.",
    adds=[
        bind("E_s", "source transform error", r"The bound $9\cdot2^\gamma T\log_2T$, in units of $2^{-p}$, on the error of a computed source transform.", "direct"),
    ],
)

# ---------------------------------------------------------------- S5
S5 = show(
    "S5",
    r"For all sufficiently large $n$, the algorithm that forms the radix-$2^b$ digits scaled by $2^{-b-2}$, applies $\Phi$, computes the two source transforms, multiplies them pointwise with one truncation, applies the opposite-sign source transform, rescales exactly by $S$ and then by $2^{2b+4}S$, rounds, applies $\Phi^{-1}$ and propagates carries outputs exactly $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$.",
    r"Fix the parameters, reduce to the digit convolution, move it to prime axes by $\Phi$, evaluate it with the source transforms and the permutation-cancellation identity, undo the two normalizations exactly, and show that the total error is below $1/2$, so that rounding and carries recover the product.",
    mot(r"Every stage is an exact algebraic identity or a contraction approximated on a fixed-point grid, so only known scale factors and bounded errors separate the computed array from the true integer coefficients, and an error below $1/2$ lets rounding and carries return the exact product.",
        "explicit",
        r"Known rescalings, rounding, and carry propagation then recover the exact integer product."),
    [S51, S52, S53, S54, S55, S56],
    page="multiplication-algorithm",
    frm=["radix-digit-reduction", "crt-axis-map", "tensor-source-transform", "precision-exact-recovery", "parameter-regime", "permutation-cancellation"],
    adds=[
        bind("b", "digit width", r"The number of bits per radix digit, $\lceil\log_2n\rceil$.", "count"),
        bind(r"\Phi", "CRT address map", r"The Chinese-remainder isomorphism from cyclic convolution of length $S$ to cyclic convolution on the prime axes.", "direct"),
    ],
)

# ---------------------------------------------------------------- S6
S6 = show(
    "S6",
    r"With $V=Tp=\Theta(n)$, each stage costs $O(V)$ times $dK$, $pK^{\tau-1}$, $\ell d^{\lambda'}$, $d^2(1+\ell^\tau)$, $dp^{1/2+\delta}\alpha$, $dp^\delta$, $\log(rp)$ or a smaller term, each at most $p^{1-2\kappa}$, so the machine runs in $O(Tp\cdot p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ time for every input length.",
    r"Divide every cost by $V$, write each normalized cost as a power of $p$ through the size relations, take the smallest margin below one, and absorb setup, exceptional-address repair and logarithmic factors.",
    mot(r"Since $V=\Theta(n)$ and $p=\Theta(\log n)$, a bound $p^{1-\kappa}$ on every cost per stored bit is exactly the claimed $O(n(\log n)^{1-\kappa})$; fixing all exponents as rationals makes each term an explicit power of $p$ whose margin below one can be read off.",
        "explicit",
        r"A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}."),
    [
        infer("S6.1",
              r"Divided by $V=Tp$, the costs are $dK$ for prefix moves and individual butterfly rounds, $pK^{\tau-1}$ for the layout's chunk exchanges, $\ell d^{\lambda'}$ for simultaneous rounds, $d^2(1+\ell^\tau)$ for CRT and axis layouts, $dp^{1/2+\delta}\alpha$ for the Gaussian line maps, $dp^\delta$ for chirps, twists and scalar products, and $\log(rp)$ for packed polynomial products, with smaller terms for scaling, rounding, input and output.",
              r"Table~\ref{tab:costs} lists costs after division by $V$; a fixed number of repeated transforms and convolutions is included in its constants."),
        infer("S6.2",
              r"As powers of $p$ these rows fall below one by the margins $g_1=1-\epsilon(1+c)$, $g_2=\epsilon c(1-\tau)$, $g_3=\epsilon(1-\lambda')$, $g_4=1-\tau-\epsilon(2-\tau)$, $g_5=1/4-\delta-3\epsilon/2$, $g_6=1-\delta-\epsilon$ and $g_7=\epsilon$, and substitution gives $\min_ig_i=g_2=2^{-181}=2\kappa$.",
              r"Thus $\min_i g_i=2^{-181}=2\kappa$."),
        infer("S6.3",
              r"The binding row comes from the transform layout's $O(p/K)$ exchanges of $K$-bit chunks at $O(VK^\tau)$ each, normalized cost $pK^{\tau-1}$, while each simultaneous round costs $O(Vd^{\lambda'})$ with its basis changes, repair and padding included.",
              r"Each exchange costs $O(VK^\tau)$ by Lemma~\ref{lem:chunk-swap}, so the normalized total is"),
        infer("S6.4",
              r"Descriptor setup over at most $p^A$ recursion visits, polynomial address work per record or per Gaussian line, and the sorting of exceptional records in packed changes of basis, a fraction $O(d2^{-K})$ of the volume, all cost $o(V)$, deterministically in the worst case.",
              r"This is a deterministic worst-case bound."),
        infer("S6.5",
              r"Each of the seven dominant powers is at most $1-2\kappa$ and every fixed power of $\log p$ is eventually at most $p^\kappa$, so the total is $O(Tp\cdot p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
              r"Any fixed power of $\log p$ is at most $p^\kappa$ eventually."),
        infer("S6.6",
              r"Below one fixed cutoff beyond all size, precision, margin and layout conditions the machine uses schoolbook multiplication, and the finitely many small lengths only enlarge the constant, giving $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.",
              r"The finitely many smaller lengths are included by enlarging the implicit constant."),
    ],
    page="cost-accounting",
    frm=["multiplication-algorithm", "parameter-regime", "address-chunk-interchange", "simultaneous-butterfly-layer", "transform-tape-layout", "asymptotic-notation-beyond-big-o"],
    salient=r"The exponent $\kappa=2^{-182}$ is half the smallest margin $g_2=\epsilon c(1-\tau)=2^{-75}\cdot2^{-56}\cdot2^{-50}=2^{-181}$, which belongs to the chunk exchanges of the transform layout: the interchange saving $1-\tau$ is diluted by the tiny dimension and chunk-width exponents.",
    adds=[
        bind("g_2", "binding margin", r"The smallest gap, $\epsilon c(1-\tau)=2^{-181}$, between a normalized cost exponent and one.", "direct"),
    ],
)

# ---------------------------------------------------------------- S7
S7 = infer(
    "S7",
    r"Because the bound holds through all input lengths, the constructed machine $A$ has $T_A(n)/(n\lg n)\to0$, more than the $\liminf$ equal to zero needed to refute an eventual lower bound $T_A(n)\ge c_An\lg n$ for every fixed machine, so the Schönhage–Strassen $n\log n$ conjecture fails for multitape Turing machines.",
    r"The power saving proved here gives a limit of zero through all input lengths, which is a stronger conclusion.",
    frm=["n-log-n-barrier", "asymptotic-notation-beyond-big-o"],
    deferred=True,
)

# ---------------------------------------------------------------- root
ROOT = show(
    "S0",
    r"One deterministic Turing machine with a fixed finite alphabet and a fixed number of one-dimensional tapes outputs the exact $2n$-bit product of any two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, so in this model the Schönhage–Strassen conjecture that $n\log n$ is the optimal order of multiplication cost fails.",
    r"Build two new tape procedures that save a power in address movement and in butterfly arithmetic; use them to compute convolution over $\mathbb C[y]/(y^r+1)$ by synthetic transforms; reach that convolution from the digit convolution by exact changes of representation (Gaussian resampling with retained permutations and chirps, a Chinese-remainder map to prime axes, a phase twist); recover the product exactly by rounding and carries; and bound every cost per stored bit by $p^{1-2\kappa}$.",
    mot(r"A transform-based multiplier that touches its $\Theta(n)$ stored bits once per transform level already spends $\Theta(n\log n)$, so going below $n\log n$ requires saving both on rearranging addresses and on butterfly arithmetic; the two tape procedures supply these savings, and the reductions place them inside an exact multiplication.",
        "explicit",
        r"Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$. We therefore need savings in both movement and arithmetic."),
    [S1, S2, S3, S4, S5, S6, S7],
    page="main-theorem",
    frm=["n-log-n-barrier", "multitape-turing-machine", "big-o-notation", "convolution", "tape-address-model"],
    salient=r"The time goes below $n\log n$ although one pass over the $\Theta(n)$ stored bits at each of the $\Theta(\log n)$ transform levels would already cost $\Theta(n\log n)$; the gain is a power of the logarithm, with the minute exponent $\kappa=2^{-182}$.",
    adds=[
        bind("n", "input length", "The number of bits of each of the two integers being multiplied.", "count"),
        bind(r"\kappa", "saving exponent", r"The fixed exponent $2^{-182}$ by which the power of the logarithm in the running time drops below one.", "direct"),
        bind("V", "logical volume", "The number of data bits stored in the array being processed, not counting work tapes.", "count"),
        bind("p", "working precision", r"The number of fractional bits of every fixed-point coefficient, $6\lceil\log_2n\rceil$ in the multiplier.", "count"),
        bind("d", "axis count", r"The number of power-of-two transform axes, about $p^\epsilon$ for a tiny fixed exponent $\epsilon$; it also bounds the chunks one butterfly layer handles.", "count"),
        bind("r", "record length", r"The number of complex coefficients of each polynomial record in $\mathbb C[y]/(y^r+1)$, a power of two.", "count"),
        bind("T", "box size", "The number of entries of the padded power-of-two box, the product of the axis lengths.", "count"),
    ],
)

ANSWER = {"root": ROOT}
