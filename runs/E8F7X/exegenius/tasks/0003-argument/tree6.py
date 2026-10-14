from lib import *


def prime_axes():
    return show(
        r"Take $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$, axes $t_i\in\{r/2,r\}$ with $\prod_it_i=T$ and distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$; then $Tp=\Theta(n)$ and every hypothesis of Gaussian resampling holds.",
        "Choose every parameter as an explicit power of $b$, then verify the bands for $d,\\ell$, the existence of enough primes in two disjoint intervals, the size bound $T/2<S<T$, and the separation $\\alpha^4\\theta_i>p$.",
        mot("The prime lengths must be close to the powers of two: their product must fill a fixed fraction of the padded box, while each ratio $t_i/s_i$ must leave enough separation for resampling.",
            "explicit", (4105, r"The distinct prime lengths $s_i$ must be close to the powers of two", r"enough separation for resampling.")),
        [
            infer(r"The fixed rational parameters are $\tau=\sigma=1-2^{-50}$, $\beta=\frac12$, $\delta=\frac1{16}$, $\lambda=1-2^{-52}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $C_1=20$, $\epsilon=2^{-75}$, $\kappa=2^{-182}$.",
                  4010, r"\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\", r"\epsilon=2^{-75},\qquad \kappa=2^{-182}."),
            infer(r"For large $n$ put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, take a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$, and make $d\ell-\log_2T$ of the axes of length $r/2$ and the rest $r$.",
                  4054, r"b=\lceil\log_2n\rceil,\quad p=6b,", r"others to be $r$."),
            infer(r"Since $d\ell-\log_2T$ is an integer in $[0,d)$, at least one axis has length $r$, and the last axis is chosen to be one.",
                  4065, r"Indeed $d\ell-\log_2T$ is an integer in $[0,d)$,", r"choose it as the last axis."),
            infer(r"The bounds on $n,T$ give $b/2\le\log_2T\le b$, hence $\frac1{12}p^\epsilon\le d\le p^\epsilon$ and $\frac p{12d}\le\ell\le\frac p{3d}$, so the comparison constants $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$ hold at once for every input length.",
                  4074, r"For sufficiently large $b$, the bounds on $n,T$ give", r"\frac{p}{12d}\leq\ell\leq\frac{p}{3d}."),
            infer(r"Set $\alpha=\lceil(12d^2b)^{1/4}\rceil$, $\gamma=2d\alpha^2$, $\eta=1/(4d)$; then $\gamma<28d^2\sqrt b\le28b^{2/3}$, so $2\le\alpha<\sqrt p$ and $\gamma=o(b)$.",
                  4091, r"\alpha=\left\lceil(12d^2b)^{1/4}\right\rceil,", r"$\gamma=o(b)$."),
            infer(r"For $0<\eta<1/4$ and $x>e^{2/\eta}$ the interval $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes.",
                  4113, r"$0<\eta<1/4$ and $x>e^{2/\eta}$, the interval", r"primes."),
            infer(r"Both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$, and the number of primes $x/(8d\log x)$ exceeds $d$ because $x>8d^2\log x$ eventually.",
                  4126, r"Thus both $x=r/2$ and $x=r$ satisfy", r"$x>8d^2\log x$ eventually."),
            infer(r"The two intervals are disjoint because $(1-\eta)r/2<(1-2\eta)r$ for $\eta<1/4$, so distinct odd primes with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ exist, and $\gcd(s_i,t_i)=1$ because $t_i$ is a power of two.",
                  4131, r"The two intervals are disjoint because", r"because $t_i$ is a power of two."),
            infer(r"Multiplying the lower bounds on $s_i$ and applying the strict Bernoulli inequality gives $S/T>(1-\frac1{2d})^d>\frac12$, so with $s_i<t_i$ we get $T/2<S<T$.",
                  4138, r"Multiplying the lower bounds on $s_i$ and", r"this gives $T/2<S<T$."),
            infer(r"The upper bound on $s_i$ gives $\theta_i\ge\eta/(1-\eta)>\eta$, so $\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\ge6b=p$, the hypothesis of the resampling lemma.",
                  4146, r"Writing $\theta_i=t_i/s_i-1$, the upper bound on $s_i$ gives", r"=3db\geq6b=p."),
            infer(r"A deterministic search by trial division costs $O(dr^{3/2}\operatorname{poly}(p))$, whose logarithm is $o(p)$, so the search takes $n^{o(1)}=o(n)$ time.",
                  4160, r"The machine finds these primes by scanning the two intervals", r"$n^{o(1)}=o(n)$ time."),
        ],
        page="prime-axis-parameters",
        frm=["gaussian-resampling", "primes-coprimality-and-gcd", "logarithms-exponentials-floor-and-ceiling", "summation-geometric-series-and-products", "padded-box-tensor-resampling"],
        salient="The exponents are astonishingly small ($\\epsilon=2^{-75}$, $c=2^{-56}$) yet enough: $d$ grows like a tiny power of $\\log n$ while $r$ stays superpolynomial in $p$, which is all the setup costs need.")


def radix_digits():
    return show(
        r"Writing the inputs in radix $2^b$ with $q=\lceil n/b\rceil$ digits turns the product into a convolution of digit polynomials with no wraparound modulo $x^S-1$ and coefficients below $2^{3b}$.",
        "Bound the degree of the product of the two digit polynomials by $S$ and each coefficient by the number of digit pairs times the largest digit square.",
        mot("A cyclic convolution of length $S$ equals the ordinary product only if the product's degree is below $S$, and exact recovery later needs a bound on the coefficient size.", "reconstructed"),
        [
            infer(r"Each input has $q=\lceil n/b\rceil$ nonnegative radix-$2^b$ digits, so the product has degree at most $2q-2<2n/b\le T/2<S$.",
                  4183, r"Write the two inputs as polynomials in $2^b$, each with", r"2q-2<2n/b\le T/2<S."),
            infer(r"Hence convolution modulo $x^S-1$ has no wraparound, and each product coefficient obeys $0\le c_j\le q(2^b-1)^2<2^{3b}$ since $q\le n\le2^b$.",
                  4186, r"Thus convolution modulo $x^S-1$ has no nonzero wraparound.", r"since $q\le n\le2^b$."),
        ],
        page="radix-digit-convolution",
        frm=["schoolbook-integer-arithmetic", "polynomials", "cyclic-convolution"])


def crt_map():
    return show(
        r"For pairwise coprime $s_i$ with product $S$, the map $\Phi:x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism turning cyclic convolution of length $S$ into $d$-dimensional cyclic convolution, and on tape it is a sequence of prefix-controlled cyclic shifts costing $O(Tpd^2(1+\ell^\tau))$.",
        "Send $x$ to $\\prod x_i^{\\mu_i}$ with $\\mu_i=P_i^{-1}\\bmod s_i$, check it is a bijection on monomials, and observe that the image of a mixed-radix coefficient index has coordinates triangular in the digits, so each axis update is a controlled shift applied in descending axis order.",
        mot("The coordinate powers are chosen so that the change of order is a sequence of controlled cyclic shifts.", "explicit",
            (4201, r"algebraic split, with coordinate powers that make the change of order a", r"sequence of controlled cyclic shifts.")),
        [
            infer(r"$\Phi$ respects $x^S=1$, and the image of $x$ has order $S$ because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all target monomials once; $\Phi$ is an isomorphism preserving cyclic convolution.",
                  4216, r"respects $x^S=1$, so it defines an algebra map.", r"preserves cyclic convolution."),
            infer(r"A coefficient $k=\sum_ja_jP_j$ goes to axis coordinate $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, because terms with $j>i$ are divisible by $s_i$ and $\mu_iP_i\equiv1$.",
                  4226, r"The coordinate of $\Phi(x^k)$ in axis $i$ is", r"modulo $s_i$."),
            infer(r"After reordering the padded axes to $(a_1,\dots,a_d)$ the targets are updated in the order $i=d,\dots,1$, so lower-index controls still have their original digits when each offset is computed.",
                  4252, r"Update the targets in the", r"required by the formula."),
            infer(r"On padded addresses each step rotates the valid interval $[0,s_i)$ by the offset, fixes $[s_i,t_i)$, and is the identity if a control is invalid; this is a bijection preserving the valid set, so zero padding stays zero.",
                  4261, r"rotate the valid target interval $[0,s_i)$ by the offset in", r"remains zero after every step."),
            infer(r"Each triangular update is a prefix-controlled cyclic shift: prepare the offset, split the valid target interval into two pieces and merge them in the opposite order.",
                  4273, r"Each triangular update is a prefix-controlled cyclic shift.", r"in the opposite order."),
            infer(r"Reversing all axes uses $O(d^2)$ unequal-width exchanges, so $\Phi$, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$.",
                  4287, r"uses $O(d^2)$ such moves.", r"O\bigl(Tp\,d^2(1+\ell^\tau)\bigr)."),
        ],
        page="crt-map",
        frm=["cyclic-convolution", "multidimensional-dft", "controlled-shifts", "arbitrary-width-interchange", "modular-arithmetic",
             "primes-coprimality-and-gcd", "radix-digit-convolution"],
        adds=[bind(r"\Phi", "address map", "the algebra isomorphism sending $x$ to $\\prod_ix_i^{\\mu_i}$, which re-addresses coefficients onto the prime axes", "direct"),
              bind(r"\mu_i", "axis exponent", "the inverse of the prefix product $P_i=\\prod_{j<i}s_j$ modulo $s_i$", "direct"),
              bind(r"P_i", "prefix product", "the integer product $\\prod_{j<i}s_j$ of the earlier axis lengths", "direct")])


def phase_twist():
    return show(
        r"The map $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ is an isomorphism $\mathbb C[x_d]/(x_d^r-1)\to\mathcal R_r$ that multiplies coefficient $k$ by $\zeta^k$, so a cyclic convolution on the last axis becomes a negacyclic one and untwisting restores the cyclic wrap.",
        "Check the map is well defined, diagonal and invertible in the coefficient bases, and verify directly that the extra negative wrap cancels against the phase.",
        mot("The power-of-two complex convolution needed for the chirp identity is obtained from the synthetic convolution by a coefficient twist.", "explicit",
            (4300, r"The power-of-two complex convolution used in the chirp identity is", r"obtained from the synthetic convolution by a coefficient twist.")),
        [
            infer(r"The map is well defined because $(\zeta y)^r=(-1)(-1)=1$.",
                  4308, r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."),
            infer(r"On the coefficient bases it is diagonal, multiplying coefficient $k$ by the nonzero $\zeta^k$, so it is an isomorphism with inverse multiplying by $\zeta^{-k}$.",
                  4310, r"multiplying coefficient $k$ by the nonzero number $\zeta^k$.", r"$\zeta^{-k}$."),
            infer(r"Writing $k+l=j+hr$ with $h\in\{0,1\}$, a product term after twisting and negacyclic reduction has factor $\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
                  4313, r"For an explicit check on the wrap, write", r"with the correct sign."),
            infer(r"Hence the normalized complex cyclic convolution is $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$.",
                  4339, r":=D_-\iota^{-1}", r"=\frac{f*g}{T}."),
        ],
        page="phase-twist",
        frm=["negacyclic-ring", "synthetic-convolution", "cyclic-convolution", "roots-of-unity", "complex-numbers"],
        adds=[bind(r"\zeta", "twist root", "the primitive $2r$-th root of unity $e^{\\pi i/r}$ whose powers twist the coefficients", "direct")])


def source_transform():
    return show(
        r"The source transform $RF_{\boldsymbol s}$ is computed as $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$: Gaussian expansion on each line, the chirp transform (a twisted synthetic convolution), Gaussian compression, then a power-of-two scaling.",
        "Compose the already established procedures along the identity $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, realising $QF_{\\boldsymbol t}$ by two phase multiplications around a complex convolution with the chirp, with disk margins tracked.",
        mot("The chirp identity turns the middle factor into a complex convolution, which the twisted synthetic convolution supplies.", "recoverable"),
        [
            infer(r"The chirp phase numerator at tensor address $j$ is $-\sum_is_ij_i^2(r/t_i)\pmod{2r}$, with $O(p)$-bit integers and $r/t_i\in\{1,2\}$.",
                  4422, r"-\sum_i s_i j_i^2(r/t_i)\pmod{2r}.", r"$r/t_i\in\{1,2\}$."),
            infer(r"Computing the squares and products with the established multiplier and the exponentials costs $O(dp^{1+\delta})$ per entry, so chirp construction costs $O(Tdp^{1+\delta})$.",
                  4429, r"construction costs $O(Td p^{1+\delta})$ in total."),
            infer(r"The computed chirp transform forms $x_0=Q_p(\overline{\widetilde a}\cdot x)$, $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$ and $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$.",
                  4439, r"x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),\\", r"&=Q_p(\overline{\widetilde a}\mathbin{\cdot}y_0)."),
            infer(r"Replacing the approximations by exact phases and exact convolution gives $\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)=QF_{\boldsymbol t}x$ by the chirp identity.",
                  4446, r"Replacing the approximations", r"\eqref{eq:permuted-chirp}."),
            infer(r"The source transform applies the linewise approximation to $\mathcal A$, the chirp transform, the linewise approximation to $\mathcal B_0$ and an exact scaling by $2^\gamma$; its exact counterpart is $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.",
                  4456, r"For a source disk-grid tensor of norm at most $.5$, write", r"=RF_{\boldsymbol s}."),
            infer(r"The opposite-sign procedure conjugates input and output, $\widetilde{\mathscr F}^+(z)=\overline{\widetilde{\mathscr F}(\overline z)}$, with exact counterpart $RF^+_{\boldsymbol s}$.",
                  4478, r"Define the opposite-sign procedure by", r"Lemma~\ref{lem:chirp-permutation}."),
        ],
        page="source-transform",
        frm=["gaussian-resampling", "padded-box-tensor-resampling", "bluestein-chirp", "phase-twist", "synthetic-convolution",
             "permutation-cancellation", "error-accounting"])


def exact_recovery():
    return show(
        r"With $h_p=2^{-p}$ and $L=\log_2T$, the scale bookkeeping and the error chain show that every recovered coefficient has error below $448\,b\,2^{-b+\gamma}<\tfrac12$, so it rounds to the true integer, which is below $2^{3b}$.",
        "Propagate norms and errors through each stage in the max-modulus norm using that a linear contraction does not enlarge an input error and a bilinear contraction adds the two operand errors, then undo the scales and compare with $1/2$.",
        mot("A linear contraction propagates an input error without increasing it, and for a bilinear contraction on disk operands the two errors add.", "explicit",
            (4559, r"A linear contraction propagates an input error without increasing it.", r"their two errors therefore add.")),
        [
            infer(r"Every synthetic transform has error below $\sqrt2\,\ell2^{-p}<L2^{-p}$ for large $n$.",
                  4550, r"Lemma~\ref{lem:synthetic-transform-cost} therefore applies to every", r"sufficiently large $n$."),
            infer(r"The three transform errors and the product truncation total below $3L+2$ before the scale $M$, so the normalized convolution has error $E_{\rm ring}:=M(3L+2)<5TL$.",
                  4586, r"the three transform errors and the polynomial-product truncation total", r"<5TL."),
            infer(r"If one operand has norm at most $.7$, bilinear contraction keeps the computed output below $.7+5TLh_p<.701$ without clipping.",
                  4593, r"If one operand has norm at most $.7$, bilinear contraction gives", r"for large $n$."),
            infer(r"The two input twists (each below $4h_p$), the convolution ($E_{\rm ring}$) and the output untwist (below $4h_p$) give $\|\widetilde{\mathcal M}_{\mathbb C}-\mathcal M_{\mathbb C}\|<6TLh_p$.",
                  4611, r"Its bilinear contraction bound propagates the two input twist errors,", r"(E_{\rm ring}+4+4+4)h_p<6TLh_p."),
            infer(r"Adding the kernel approximation (2), first phase (4), convolution ($6TL$) and last phase (4) gives $\|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\|<8TLh_p$.",
                  4633, r"The computed convolution contributes less", r"(6TL+2+4+4)h_p<8TLh_p."),
            infer(r"Inserting the exact contractions $\mathcal A,QF_{\boldsymbol t},\mathcal B_0$, the error before the source scale is below $2dp^2+8TL$, and after the scale $2^\gamma$ it is below $E_sh_p$ with $E_s=9\,2^\gamma TL$.",
                  4646, r"Insert the exact contractions $\mathcal A$, $QF_{\boldsymbol t}$,", r"because $2dp^2<TL$ eventually."),
            infer(r"The computed transforms have norm below $1/4+E_sh_p<.26$, so $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has norm at most $.26^2<.5$.",
                  4676, r"The exact arrays have norm less than $1/4$, and the computed arrays", r"$.26^2<.5$."),
            infer(r"Splitting $\widetilde U\widetilde V_1-UV_1$ into two terms each below $E_sh_p$ and adding truncation $2h_p$ gives $\|z-U\cdot V_1\|<(2E_s+2)h_p$.",
                  4685, r"The factors $\widetilde V_1$ and $U$ are in the disk.", r"<(2E_s+2)h_p$."),
            infer(r"Since $G(U\cdot V_1)=(u*v)/S^2$ for the exact opposite contraction $G=RF^+_{\boldsymbol s}$, inserting $G$ at the computed input gives $\|\widetilde{\mathscr F}^+(z)-G(U\cdot V_1)\|<(3E_s+2)h_p$.",
                  4695, r"The computed opposite transform may be applied to $z$ because", r"<(3E_s+2)h_p."),
            infer(r"The first scale by $S$ gives $\widetilde w$ approximating $w=(u*v)/S$ with error below $E_wh_p$, where $E_w:=S(3E_s+2)<28\,2^\gamma T^2L$.",
                  4705, r"The first exact numerator multiplication by $S$ gives", r"<28\,2^\gamma T^2L."),
            infer(r"Each coefficient of $w$ averages $S$ products of coefficients of $u$ and $v$, so $\|w\|<1/16$ and $\|\widetilde w\|<1/16+E_wh_p<1$.",
                  4711, r"Each coefficient of $w$ is an average of $S$ products of coefficients", r"1/16+10^{-3}<1."),
            infer(r"The second scale by $2^{2b+4}S$ returns the integer coefficients, and since $S\le T<2^b$, $L<b$, $\gamma\le b/4$, the final error is below $2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b}<448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<\tfrac12$.",
                  4722, r"Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than", r"\le448b\,2^{-3b/4}<\frac12."),
            infer(r"The true coefficients are integers, so an error strictly below $1/2$ makes the nearest integer to $H_j/2^p$ the unique correct coefficient.",
                  4728, r"The true coefficients are real integers.", r"correct coefficient."),
            infer(r"By the capacity bound the correct coefficient lies in $[0,2^{3b})$ and fits in one signed $(3b+1)$-bit word.",
                  4751, r"bound makes the result the correct nonnegative coefficient, and", r"two's-complement word"),
        ],
        page="exact-recovery",
        frm=["error-accounting", "fixed-point-disk", "synthetic-convolution", "source-transform", "permutation-cancellation",
             "radix-digit-convolution", "triangle-inequality-and-norms", "rational-numbers-and-rounding"],
        adds=[bind(r"h_p", "grid step", "the grid spacing $2^{-p}$ of the stored coefficients, the unit in which errors are measured", "direct"),
              bind(r"L", "log of box size", "the base-2 logarithm $\\log_2T$ of the number of box entries", "direct"),
              bind(r"E_s", "source error", "the error bound $9\\,2^\\gamma TL$, in units of $h_p$, of the scaled source transform", "direct")],
        salient="Despite scales up to $2^\\gamma S T^2$ and $2^{2b+4}$, the final error $448\\,b\\,2^{-b+\\gamma}$ still falls like $2^{-b}$, because the working precision $6b$ outweighs the rescaling.")


def carries():
    return show(
        r"Radix-$2^b$ carry propagation turns the recovered coefficients $c_j<2^{3b}$ into exactly $2n$ product bits.",
        "Run the carry recurrence $c_j+k_j=d_j+Q_0k_{j+1}$ from low to high index, bound the carries by induction, and check the digit invariant.",
        mot("The coefficients may exceed one digit, but the carry stays bounded, so a left-to-right scan with $O(b)$-bit carry suffices.", "recoverable"),
        [
            infer(r"With $Q_0=2^b$ the carries obey $k_0=0$, $d_j=(c_j+k_j)\bmod Q_0$, $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$, and the coefficients are zero for $2q-2<j<S$.",
                  4771, r"To propagate carries, let $Q_0=2^b$.", r"\right\rfloor."),
            infer(r"The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$: if this holds at $j$ then $c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1)$, which proves the bound at $j+1$.",
                  4779, r"The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$.", r"which proves the next carry bound."),
            infer(r"The defining relation gives the invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$, which fixes the first $j$ radix digits of the full product.",
                  4784, r"The defining relation $c_j+k_j=d_j+Q_0k_{j+1}$ also gives the exact invariant", r"of the full product."),
            infer(r"The exact product is below $2^{2n}$, so all bits above position $2n-1$ are zero; removing only those padding bits yields exactly $2n$ output bits.",
                  4803, r"than $2^{2n}$; all bits above position $2n-1$ are therefore zero.", r"exactly $2n$ bits."),
        ],
        frm=["schoolbook-integer-arithmetic", "recursion-and-divide-and-conquer-recurrences"])


def mult_algorithm():
    return show(
        r"Digit extraction, the address map $\Phi$, two source transforms, a truncated pointwise product, the opposite-sign transform, rescaling by $S$ and $2^{2b+4}$, rounding, the inverse map and carry propagation produce the $2n$-bit product.",
        "Run the listed steps in order, noting that the two scales by $S$ undo different normalisations, and then prove the recovered coefficients exact.",
        mot("The recovery subsection verifies the disk bounds needed by every call, proves the final error is below $1/2$, and justifies the rounding, carries and output length.", "explicit",
            (4542, r"The next subsection verifies the disk bounds needed by every call and proves that the final error is", r"less than $1/2$;")),
        [
            infer(r"Each operand is read backward in groups of $b$ bits, giving the radix-$2^b$ digits $a_0,\dots,a_{q-1}$ in increasing coefficient order.",
                  4489, r"Read each stored operand backward from its least significant end in groups of $b$ bits.", r"in increasing coefficient order."),
            infer(r"Digit $a_j$ is written as the exact grid numerator $a_j2^{p-b-2}$, the value $a_j2^{-b-2}$, with a zero imaginary word, and $S-q$ zero records are appended.",
                  4495, r"For digit $a_j$, write the exact grid numerator", r"$a_j2^{-b-2}$."),
            infer(r"Step 1: apply the address map $\Phi$ with its padded layout to obtain source arrays $u,v$ of exact $p$-bit grid values of norm below $1/4$.",
                  4508, r"Apply the coefficient-address map $\Phi$, with its padded layout, to obtain", r"less than $1/4$."),
            infer(r"Step 2: compute the two source transforms $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.",
                  4511, r"Compute $\widetilde{\mathscr F}(u)$ and", r"$\widetilde{\mathscr F}(v)$."),
            infer(r"Step 3: multiply corresponding coefficients exactly and truncate each part toward zero to $p$ fractional bits, giving the source array $z$.",
                  4513, r"Multiply corresponding complex coefficients exactly and truncate", r"Denote the resulting source array by $z$."),
            infer(r"Step 4: compute $\widetilde{\mathscr F}^+(z)$ and multiply its numerators exactly by $S$, giving the dyadic array $\widetilde w$.",
                  4517, r"Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid", r"by $\widetilde w$."),
            infer(r"Step 5: multiply by $2^{2b+4}S$, round the real values to nearest integers as signed $(3b+1)$-bit words (zero at padded addresses), and apply $\Phi^{-1}$ to restore coefficient order.",
                  4521, r"Multiply the grid numerators of $\widetilde w$ exactly by", r"ordinary coefficient order."),
            infer(r"The two occurrences of $S$ undo different normalisations: after the three transforms the exact result is $(u*v)/S^2$, the first scale gives $w=(u*v)/S$ and the second, with $2^{2b+4}$, gives the original integer coefficient convolution.",
                  4536, r"The two occurrences of $S$ in this algorithm undo different", r"integer coefficient convolution."),
            exact_recovery(),
            carries(),
        ],
        page="multiplication-algorithm",
        frm=["radix-digit-convolution", "crt-map", "prime-axis-parameters", "phase-twist", "source-transform", "permutation-cancellation",
             "exact-recovery", "established-multiplier"],
        salient="The scale $S$ is applied twice for different reasons: once to cancel the $1/S$ lost by the three transforms, and once, together with $2^{2b+4}$, to undo the input scaling and return the integer coefficients.")


def cost_accounting():
    margins = show(
        r"The seven dominant normalized terms have powers of $p$ equal to $1-g_i$ with margins $g_1>\tfrac12$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>\tfrac18$, $g_6>\tfrac12$, $g_7=2^{-75}$, so $\min_ig_i=2^{-181}=2\kappa$.",
        "Express each term as a power of $p$ in the fixed exponents $\\epsilon,c,\\tau,\\lambda',\\delta$ and substitute.",
        mot("Direct substitution of the fixed rational exponents gives the margins.", "recoverable"),
        [
            infer(r"The margins are $g_1=1-\epsilon(1+c)$, $g_2=\epsilon c(1-\tau)$, $g_3=\epsilon(1-\lambda')$, $g_4=1-\tau-\epsilon(2-\tau)$, $g_5=1/4-\delta-3\epsilon/2$, $g_6=1-\delta-\epsilon$, $g_7=\epsilon$.",
                  4841, r"g_1&=1-\epsilon(1+c),\qquad", r"g_7=\epsilon."),
            infer(r"Direct substitution gives $g_1>\frac12$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>\frac18$, $g_6>\frac12$, $g_7=2^{-75}$, thus $\min_ig_i=2^{-181}=2\kappa$.",
                  4851, r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad", r"$\min_i g_i=2^{-181}=2\kappa$."),
        ],
        frm=["logarithms-exponentials-floor-and-ceiling"])
    return show(
        r"Dividing the costs by $V=Tp=\Theta(n)$ gives seven dominant terms (butterfly rounds, chunk exchanges, simultaneous layers, CRT layouts, Gaussian lines, chirps, packed products), each at most $p^{1-2\kappa}$, so the total is $O(n(\log n)^{1-\kappa})$.",
        "Tabulate each operation's normalized cost as a power of $p$, justify each row from its lemma, check that every power is at most $1-2\\kappa$, absorb the setup and exceptional streams, and absorb powers of $\\log p$ into $p^\\kappa$.",
        mot("The explicit slack between the smallest margin $2^{-181}$ and $\\kappa=2^{-182}$ will cover any remaining fixed power of $\\log p$.", "explicit",
            (4854, r"This explicit slack will cover", r"any remaining fixed power of $\log p$.")),
        [
            infer(r"Put $V=Tp=\Theta(n)$; each coefficient has $\Theta(p)$ bits, so a full padded array has $\Theta(V)$ stored bits.",
                  4810, r"For the cost calculation put $V=Tp=\Theta(n)$.", r"$\Theta(V)$ stored bits."),
            margins,
            infer(r"The transform layout uses $O(p/K)$ exchanges of width-$K$ chunks, each costing $O(VK^\tau)$, so the normalized total is $O(p/K)K^\tau=O(pK^{\tau-1})$, a power $1-\epsilon c(1-\tau)$ of $p$.",
                  4861, r"Its positional layout uses $O(p/K)$ exchanges", r"O(pK^{\tau-1})."),
            infer(r"The at most $\ell$ simultaneous rounds each cost $O(Vd^{\lambda'})$, already including basis changes, repair, row padding and cleanup.",
                  4868, r"For the at most $\ell$ simultaneous rounds,", r"fixed-tape cleanup."),
            infer(r"Axis exposure and restoration need $O(d^2)$ adjacent axis moves, each costing $O(V(1+\ell^\tau))$ by peeling the excess bit, exchanging equal-width parts and restoring the bit.",
                  4874, r"Axis exposure and restoration require $O(d^2)$ adjacent axis moves.", r"restore the bit."),
            infer(r"Axis $i$ has at most $T/t_i$ Gaussian lines, so the line costs sum to $O(dTp^{3/2+\delta}\alpha)$ and, with $\alpha=\Theta(p^{1/4+\epsilon/2})$, the normalized power is $3/4+\delta+3\epsilon/2$.",
                  4881, r"For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines.", r"displayed power of $p$."),
            infer(r"Chirp numerators are computed with the established multiplier and the exponentials generated at cost $O(dp^{1+\delta})$ per entry.",
                  4894, r"then generating the exponentials, costs $O(dp^{1+\delta})$ per entry."),
            infer(r"There are $T/r$ polynomial records in each pointwise ring product, and four integer products on $O(rp)$ bits per record cost $O(Tp\log(rp))$ in total.",
                  4900, r"polynomial records in each pointwise ring product.", r"in total."),
            infer(r"These calls use the established multiplier on records of length $O(rp)=o(n)$ and do not invoke the improved algorithm recursively.",
                  4905, r"use the previously established multiplier on records of length", r"being constructed."),
            infer(r"The recursion and layout visits number at most $p^A$ with setup $p^C$ each, so setup costs at most $p^{A+C}=o(Tp)$.",
                  4922, r"Choose a fixed exponent $A$ so that their", r"$p^{A+C}=o(Tp)$."),
            infer(r"The compact sorting of exceptional records totals $O(dp2^{-K}\sum V_{\rm call})=O(Vp^{A'}2^{-K})=o(V)$ in the worst case.",
                  4961, r"Stable bit sorting makes $O(p)$ scans of this stream, for one-call", r"=O(Vp^{A'}2^{-K})=o(V)"),
            infer(r"Each of the seven powers is at most $1-2\kappa$ and any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
                  4983, r"Each of the seven displayed powers is at most $1-2\kappa$ by", r"=O(n(\log n)^{1-\kappa})."),
            infer(r"Below a fixed cutoff beyond all size, precision, margin and layout conditions schoolbook multiplication is used, and the finitely many smaller lengths are absorbed in the constant.",
                  4989, r"Fix one cutoff beyond all the size, precision, margin and layout", r"implicit constant."),
        ],
        page="cost-accounting",
        frm=["simultaneous-butterfly-layer", "arbitrary-width-interchange", "transform-layout", "synthetic-convolution",
             "padded-box-tensor-resampling", "prime-axis-parameters", "multiplication-algorithm", "established-multiplier",
             "signed-packing-product", "logarithms-exponentials-floor-and-ceiling", "asymptotic-notation-beyond-big-o"],
        adds=[bind(r"V", "stored volume", "the number of stored bits $Tp$ of a full padded array, of order $n$", "count"),
              bind(r"g_i", "margin", "the amount by which the power of $p$ in the $i$-th dominant normalized cost term falls below one", "direct")],
        salient="The smallest margin $2^{-181}$ comes from the chunk-exchange term, $\\epsilon c(1-\\tau)=2^{-75}\\cdot2^{-56}\\cdot2^{-50}$, and $\\kappa=2^{-182}$ is exactly half of it, which pays for every logarithmic factor.")
