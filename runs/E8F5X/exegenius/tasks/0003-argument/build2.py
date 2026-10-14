exec(open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E8F5X/exegenius/tasks/0003-argument/build.py').read())

S6_1 = show("S6.1",
    "From $n$ set $b=\\lceil\\log_2n\\rceil$, precision $p=6b$, number of axes $d=\\lfloor b^\\epsilon\\rfloor$, chunk width $K=\\lfloor d^c\\rfloor$, box size $T\\in[4n/b,8n/b)$ and axis lengths $t_i\\in\\{r/2,r\\}$ with $r=2^\\ell$, so that $Tp=\\Theta(n)$ and $r$ exceeds every fixed power of $p$.",
    "Fix rational exponents once, then derive every size from $n$ and check the comparison bands that the layer and transform lemmas need",
    mot("The layer and transform interfaces need $d=\\Theta(p^\\epsilon)$, $r=2^{\\Theta(p/d)}$ and $Tp=\\Theta(n)$ with explicit constants, so the sizes are defined from $b$ and the constants $a_d,b_d,a_r,b_r$ are checked against them.", "recoverable"),
    [
        inf("S6.1.1",
            "The fixed exponents include $C_1=20$, $\\epsilon=2^{-75}$ and $\\kappa=2^{-182}$ (with $\\tau=\\sigma=1-2^{-50}$, $c=2^{-56}$, $\\lambda'=1-2^{-54}$), chosen with room to spare in all layer conditions.",
            r"C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}."),
        inf("S6.1.2",
            "For large $n$: $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, $T$ a power of two in $[4n/b,8n/b)$, $r=2^{\\lceil(\\log_2T)/d\\rceil}$, with $d\\ell-\\log_2T$ axes of length $r/2$ and the rest of length $r$.",
            r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,"),
        inf("S6.1.3",
            "These give $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$ and $r=2^{\\Theta(p^{1-\\epsilon})}$.",
            r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad"),
        inf("S6.1.4",
            "From $b/2\\le\\log_2T\\le b$ and $p=6b$: $\\frac1{12}p^\\epsilon\\le d\\le p^\\epsilon$ and $\\frac p{12d}\\le\\ell\\le\\frac p{3d}$, so the comparison constants $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$ work for all input lengths.",
            r"\frac1{12}p^\epsilon\leq d\leq p^\epsilon,"),
    ],
    page="size-parameters",
    frm=["big-theta-big-omega-and-little-o-notation", "exponential-and-logarithm-functions", "floor-ceiling-and-rounding", "fixed-point-numerics"])

S6_2 = show("S6.2",
    "Distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$, where $\\eta=1/(4d)$, are found by trial division, so $T/2<S=\\prod s_i<T$ and each ratio $t_i/s_i$ leaves the separation $\\alpha^4\\theta_i>p$ that resampling needs.",
    "Count primes in the two disjoint intervals with an explicit prime-density bound, pick distinct ones, then bound their product by Bernoulli's inequality and the separation by the upper limit on $s_i$",
    mot("Resampling needs the ratio $t_i/s_i$ bounded away from one, while the product of the $s_i$ must fill at least half the padded box, so each $s_i$ is taken from a thin interval just below $t_i$.", "recoverable"),
    [
        inf("S6.2.1",
            "Each interval contains more than $d$ primes (at least $x/(8d\\log x)$ with $x\\in\\{r/2,r\\}$, since $\\log x=\\Theta(p^{1-\\epsilon})$), and the two intervals are disjoint, so distinct odd primes $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ exist; $\\gcd(s_i,t_i)=1$ as $t_i$ is a power of two.",
            r"(1-2\eta)t_i<s_i\leq(1-\eta)t_i."),
        inf("S6.2.2",
            "Multiplying the lower bounds and applying Bernoulli's inequality gives $S/T>(1-1/(2d))^d>1/2$, and $s_i<t_i$ gives $S<T$.",
            r"Together with $s_i<t_i$, this gives $T/2<S<T$."),
        inf("S6.2.3",
            "With $\\theta_i=t_i/s_i-1>\\eta$, one gets $\\alpha^4\\theta_i>\\frac{12d^2b}{4d}=3db\\ge6b=p$, so every hypothesis of the resampling lemma holds.",
            r"\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p."),
        inf("S6.2.4",
            "Trial division over both intervals costs $O(dr^{3/2}\\mathrm{poly}(p))$, whose logarithm is $o(p)$, so the search takes $n^{o(1)}=o(n)$ time.",
            r"$n^{o(1)}=o(n)$ time."),
        inf("S6.2.5",
            "The digit polynomials have product degree $2q-2<2n/b\\le T/2<S$, so convolution modulo $x^S-1$ has no wraparound.",
            r"Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
    ],
    page="prime-lengths",
    frm=["prime-numbers-coprimality-and-trial-division", "gaussian-resampling"])

S6_3 = show("S6.3",
    "A cyclic convolution of length $S=s_1\\cdots s_d$ with pairwise coprime $s_i$ becomes a convolution on the product of cyclic axes of lengths $s_i$ via $x\\mapsto\\prod_ix_i^{\\mu_i}$, implemented by triangular controlled shifts and axis moves in $O(Tp\\,d^2(1+\\ell^\\tau))$.",
    "Define the algebra isomorphism $\\Phi$ by the Chinese remainder theorem with $\\mu_i=P_i^{-1}\\bmod s_i$, express its action as a lower-triangular update of mixed-radix digits, and perform it by controlled shifts after reordering the axes",
    mot("With the powers $\\mu_i$ chosen as inverses of prefix products, the new coordinate $b_i$ depends only on lower-index digits, so every update is a shift controlled by fields that precede the target on tape.", "recoverable"),
    [
        inf("S6.3.1",
            "Since the image of $x$ has order $S$ (each $\\mu_i$ is a unit and the $s_i$ are coprime), its powers run through all basis monomials once, so $\\Phi$ is an isomorphism preserving cyclic convolution.",
            r"$\Phi$ is an isomorphism and preserves cyclic convolution."),
        inf("S6.3.2",
            "Writing $k=\\sum_ja_jP_j$ in mixed radix, the axis-$i$ coordinate of $\\Phi(x^k)$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}$, a triangular formula.",
            r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}."),
        inf("S6.3.3",
            "Terms with $j>i$ vanish modulo $s_i$ and $\\mu_iP_i=1$ modulo $s_i$, which is why only lower-index digits and $a_i$ itself enter.",
            r"Indeed terms with $j>i$ are divisible by $s_i$, and $\\mu_iP_i=1$ modulo".replace("\\\\", "\\")),
        inf("S6.3.4",
            "Updating targets in the order $i=d,d-1,\\dots,1$ means every lower-index control still holds its original digit; each step rotates the valid interval $[0,s_i)$ and fixes $[s_i,t_i)$, so zero padding stays zero (exception: an invalid control gives the identity).",
            r"order $i=d,d-1,\ldots,1$ using \eqref{eq:triangular-crt}.  When target"),
        inf("S6.3.5",
            "The $O(d^2)$ axis moves, each costing $O(V(1+\\ell^\\tau))$ by the chunk swap, dominate; the $d$ rotations cost $O(dV)$, so $\\Phi$, its inverse and the padding cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
            r"O\bigl(Tp\,d^2(1+\ell^\tau)\bigr)."),
    ],
    page="crt-prime-axes",
    frm=["prime-numbers-coprimality-and-trial-division", "modular-arithmetic", "extended-euclidean-algorithm", "controlled-shifts", "chunk-interchange", "cyclic-convolution", "positional-notation-in-any-radix-and-mixed-radix"],
    salient="The CRT map $x\\mapsto\\prod_ix_i^{\\mu_i}$ is triangular in the mixed-radix digits, so it needs only controlled shifts rather than a general permutation of the stream.")

S6_4 = show("S6.4",
    "Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ maps the cyclic coordinate $\\mathbb C[x]/(x^r-1)$ isomorphically onto $\\mathbb C[y]/(y^r+1)$, so complex cyclic convolution is computed over the ring and untwisted.",
    "Define $\\Theta:x_d\\mapsto\\zeta y$, check it is a diagonal isomorphism and that the negacyclic sign cancels the cyclic wrap, then conjugate the ring convolution by the twists",
    mot("The synthetic convolution works over $y^r+1$ while the chirp identity needs a cyclic axis; a diagonal phase twist converts the negative wrap into the cyclic one.", "recoverable"),
    [
        inf("S6.4.1",
            "$\\Theta$ is diagonal on the monomial bases, multiplying coefficient $k$ by the nonzero number $\\zeta^k$, so it is an isomorphism with inverse $\\zeta^{-k}$ and preserves the sup norm.",
            r"multiplying coefficient $k$ by the nonzero number $\zeta^k$."),
        inf("S6.4.2",
            "For $k+l=j+hr$ with $h\\in\\{0,1\\}$ the twisted negacyclic term has factor $\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j$.",
            r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j."),
        inf("S6.4.3",
            "Untwisting therefore recovers the cyclic coefficient with the correct sign, so $\\mathcal M_{\\mathbb C}(f,g)=D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=f*g/T$.",
            r"Untwisting therefore recovers the cyclic coefficient with the correct"),
    ],
    page="coefficient-twist",
    frm=["negacyclic-ring", "ring-convolution", "complex-numbers", "cyclic-convolution"])

S6_5 = show("S6.5",
    "The computed source transform $\\widetilde{\\mathscr F}$ for a coprime-length source (linewise Gaussian map $\\mathcal A$, chirp transform by complex convolution through the phase twist, linewise map $\\mathcal B_0$, exact $2^\\gamma$ rescale) approximates $RF_{\\boldsymbol s}$ and has an opposite-sign version $\\widetilde{\\mathscr F}^+$ by conjugation.",
    "Compose the tensor resampling, the chirp identity evaluated by the twisted ring convolution, and the compression map, and rescale exactly",
    mot("The identity $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ gives the source transform as three factors, the middle of which the chirp turns into convolution.", "recoverable"),
    [
        inf("S6.5.1",
            "The computed chirp transform forms $x_0=Q_p(\\overline{\\widetilde a}\\cdot x)$, convolves with the kernel $\\widetilde a$ through the twisted ring convolution, and applies the last endpoint phase.",
            r"x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),\\"),
        inf("S6.5.2",
            "Replacing approximations by exact phases and convolution gives $\\overline a\\cdot\\mathcal M_{\\mathbb C}(a,\\overline a\\cdot x)=QF_{\\boldsymbol t}x$ by the chirp identity.",
            r"\overline a\mathbin{\cdot}\mathcal M_{\mathbb C}"),
        inf("S6.5.3",
            "Applying $\\mathcal A$, then the chirp transform, then $\\mathcal B_0$, then an exact multiplication by $2^\\gamma$ has exact counterpart $\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$.",
            r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A"),
        inf("S6.5.4",
            "The opposite-sign procedure $\\widetilde{\\mathscr F}^+(z)=\\overline{\\widetilde{\\mathscr F}(\\overline z)}$ has exact counterpart $RF^+_{\\boldsymbol s}$ because conjugation turns the negative sign into the positive one and commutes with the real permutation $R$.",
            r"=\overline{\widetilde{\mathscr F}(\overline z)};"),
    ],
    page="source-transform",
    frm=["gaussian-resampling", "bluestein-chirp", "permutation-cancellation", "coefficient-twist", "tensor-resampling-box", "fixed-point-numerics"])

S6_6 = [
    inf("S6.6.1",
        "Step 1: apply the coefficient-address map $\\Phi$ with its padded layout to the scaled digit streams, obtaining source arrays $u,v$ of exact $p$-bit grid values of norm below $1/4$.",
        r"\item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain"),
    inf("S6.6.2",
        "Step 2: compute the source transforms $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$.",
        r"\item Compute $\widetilde{\mathscr F}(u)$ and"),
    inf("S6.6.3",
        "Step 3: multiply corresponding coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, giving $z$.",
        r"\item Multiply corresponding complex coefficients exactly and truncate"),
    inf("S6.6.4",
        "Step 4: compute $\\widetilde{\\mathscr F}^+(z)$ and multiply its grid numerators exactly by $S$, giving $\\widetilde w\\approx(u*v)/S$.",
        r"\item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid"),
    inf("S6.6.5",
        "Step 5: multiply the numerators of $\\widetilde w$ exactly by $2^{2b+4}S$, round the real parts to nearest integers, write them in $(3b+1)$-bit words (zero at padded addresses) and apply $\\Phi^{-1}$.",
        r"\item Multiply the grid numerators of $\widetilde w$ exactly by"),
    inf("S6.6.6",
        "Step 6: propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits, most significant first.",
        r"\item Propagate radix-$2^b$ carries in increasing coefficient order."),
    inf("S6.6.7",
        "The two occurrences of $S$ undo different normalizations: after the three transforms the exact counterpart is $(u*v)/S^2$ by permutation cancellation, so the first scale gives $(u*v)/S$ and the second, with $2^{2b+4}$ undoing the two input scales, gives the original integer coefficient convolution.",
        r"The two occurrences of $S$ in this algorithm undo different"),
]

S6_7 = show("S6.7",
    "Disk-margin and error bookkeeping shows each computed array stays in the disk and the recovered coefficient error is below $1/2$, so rounding gives the exact integer convolution coefficients and carries give the exact binary product.",
    "Track the norm and absolute error of every stage through contractions and bilinear contractions, which add errors, then scale the final error by $2^{2b+4}S$ against $2^{-6b}$ and check it is below $1/2$",
    mot("A linear contraction passes an error through unchanged and a bilinear contraction on disk operands adds the two errors, so the accumulated error is a sum of per-stage errors, each of which is small compared with $2^{-p}$ scaled up.", "explicit", r"A linear contraction propagates an input error without increasing it."),
    [
        inf("S6.7.1",
            "A computed phase product satisfies $\\|Q_p(\\widetilde ex)\\|\\le\\|x\\|$, so smaller operand norms such as $.6$ or $.7$ are preserved through twists and endpoint phases.",
            r"\|Q_p(\widetilde e x)\|\le\|x\|."),
        inf("S6.7.2",
            "The ring convolution has error $E_{\\rm ring}:=M(3L+2)<5TL$ (three transforms plus the product truncation, scaled by $M$), and norm below $.701$.",
            r"E_{\rm ring}:=M(3L+2)<5TL."),
        inf("S6.7.3",
            "Adding two twist errors and the output untwist error (each below $4$) gives $\\|\\widetilde{\\mathcal M}_{\\mathbb C}-\\mathcal M_{\\mathbb C}\\|<(E_{\\rm ring}+4+4+4)h_p<6TLh_p$.",
            r"<(E_{\rm ring}+4+4+4)h_p<6TLh_p."),
        inf("S6.7.4",
            "The chirp output has error $<(6TL+2+4+4)h_p<8TLh_p$ (kernel $2$, first phase $4$, convolution $6TL$, last phase $4$).",
            r"<(6TL+2+4+4)h_p<8TLh_p."),
        inf("S6.7.5",
            "A source transform has error $<2dp^2+8TL$ before the rescale, so after multiplication by $2^\\gamma$ the error is below $E_sh_p$ with $E_s=9\\,2^\\gamma TL$.",
            r"E_s=9\,2^\gamma TL,"),
        inf("S6.7.6",
            "Writing $\\widetilde U\\cdot\\widetilde V_1-U\\cdot V_1=(\\widetilde U-U)\\cdot\\widetilde V_1+U\\cdot(\\widetilde V_1-V_1)$ and adding the truncation gives $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$.",
            r"Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$."),
        inf("S6.7.7",
            "Inserting the exact contraction $G=RF^+_{\\boldsymbol s}$ at the computed input gives $\\|\\widetilde{\\mathscr F}^+(z)-G(U\\cdot V_1)\\|<(3E_s+2)h_p$, with $G(U\\cdot V_1)=(u*v)/S^2$.",
            r"<(3E_s+2)h_p."),
        inf("S6.7.8",
            "The first scale by $S$ gives $\\widetilde w$ with error below $E_wh_p$, where $E_w:=S(3E_s+2)<28\\,2^\\gamma T^2L$, and $\\|\\widetilde w\\|<1/16+10^{-3}<1$.",
            r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
        inf("S6.7.9",
            "The unscaled coefficient array is $2^{2b+4}Sw$, so the final absolute error is below $2^{2b+4}S\\cdot28\\,2^\\gamma T^2L\\cdot2^{-6b}$.",
            r"2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b}"),
        inf("S6.7.10",
            "Using $S\\le T<2^b$, $L<b$ and $\\gamma\\le b/4$, this is $<448b\\,2^{-b+\\gamma}\\le448b\\,2^{-3b/4}<\\frac12$.",
            r"\le448b\,2^{-3b/4}<\frac12.",
            salient="The final error decays like $2^{-3b/4}$ even though the scale $2^{2b+4}S\\,2^\\gamma T^2L$ is large, because the precision $p=6b$ leaves $2^{-6b}$ to absorb it."),
        inf("S6.7.11",
            "Because the true coefficients are integers and the error is below $1/2$, the nearest integer to the recovered value is the unique correct coefficient.",
            r"that value the unique correct coefficient."),
        inf("S6.7.12",
            "Radix-$2^b$ carries obey $0\\le k_j\\le q(Q_0-1)<Q_0^2$ by induction, since $c_j+k_j\\le qQ_0(Q_0-1)$ for $c_j\\le q(Q_0-1)^2$.",
            r"The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$.  If this holds at"),
        inf("S6.7.13",
            "The relation $c_j+k_j=d_j+Q_0k_{j+1}$ gives the invariant $\\sum_{h<j}c_hQ_0^h=\\sum_{h<j}d_hQ_0^h+k_jQ_0^j$, which fixes the first $j$ radix digits of the product.",
            r"=\sum_{h<j}d_hQ_0^h+k_jQ_0^j."),
    ],
    page="exact-recovery",
    frm=["multiplication-algorithm", "source-transform", "fixed-point-numerics", "floor-ceiling-and-rounding", "vector-norms-inner-products-and-orthogonality"],
    adds=[B("L", "transform depth", "The base-two logarithm $\\log_2T$ of the box size, an upper bound on the number of transform rounds.", "count")])

S6_8 = show("S6.8",
    "Dividing each cost by $V=Tp$, seven dominant terms have powers of $p$ at most $1-2\\kappa$ below one; the smallest margin $2^{-181}$ fixes $\\kappa=2^{-182}$, and any polylogarithmic factor is absorbed, giving $O(n(\\lg n)^{1-\\kappa})$.",
    "List every cost row of the algorithm normalized by $Tp$, derive each row from the earlier lemmas, read off the margins $g_1,\\dots,g_7$ below one, and take the minimum",
    mot("A total of the form $V\\cdot p^{1-\\kappa}$ follows once every normalized row is at most $p^{1-2\\kappa}$, and the factor $p^{\\kappa}$ left over absorbs fixed powers of $\\log p$.", "recoverable"),
    [
        inf("S6.8.1",
            "The seven margins are $g_1=1-\\epsilon(1+c)$, $g_2=\\epsilon c(1-\\tau)$, $g_3=\\epsilon(1-\\lambda')$, $g_4=1-\\tau-\\epsilon(2-\\tau)$, $g_5=1/4-\\delta-3\\epsilon/2$, $g_6=1-\\delta-\\epsilon$ and $g_7=\\epsilon$, each the distance of a table row's power of $p$ below one.",
            r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad"),
        inf("S6.8.2",
            "Direct substitution of the fixed parameters gives $g_2=2^{-75}\\cdot2^{-56}\\cdot2^{-50}=2^{-181}$ as the smallest, so $\\min_ig_i=2^{-181}=2\\kappa$.",
            r"Thus $\min_i g_i=2^{-181}=2\kappa$.  This explicit slack will cover",
            salient="The binding row is the chunk exchanges for the transform layout, $pK^{\\tau-1}$, whose margin $\\epsilon c(1-\\tau)$ is a product of three tiny exponents; all other rows have far more slack."),
        inf("S6.8.3",
            "The layout exchanges cost $O(p/K)$ exchanges of width-$K$ chunks at $O(VK^\\tau)$ each, normalized $O(p/K)\\,K^\\tau=O(pK^{\\tau-1})$.",
            r"O(p/K)\,K^\tau=O(pK^{\tau-1})."),
        inf("S6.8.4",
            "Axis exposure costs $O(d^2)$ adjacent moves of $O(V(1+\\ell^\\tau))$ each, giving the CRT and axis layout row $d^2(1+\\ell^\\tau)$.",
            r"Each costs $O(V(1+\ell^\tau))$: peel a single excess bit when widths"),
        inf("S6.8.5",
            "Gaussian line maps give $O(dTp^{3/2+\\delta}\\alpha)$ and $\\alpha=\\Theta(p^{1/4+\\epsilon/2})$ explains the power $3/4+\\delta+3\\epsilon/2$ of the normalized row.",
            r"$\alpha=\Theta(p^{1/4+\epsilon/2})$ explains its displayed power of $p$."),
        inf("S6.8.6",
            "There are $T/r$ polynomial records, and four integer products on $O(rp)$ bits each cost $O(Tp\\log(rp))$ in total, a normalized row $\\log(rp)=O(p^{1-\\epsilon})$; these call the established multiplier on records of length $o(n)$.",
            r"products on $O(rp)$ bits per record therefore cost"),
        inf("S6.8.7",
            "Each of the seven displayed powers is at most $1-2\\kappa$ and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually.",
            r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
        inf("S6.8.8",
            "Consequently the large-input bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
            r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})."),
        inf("S6.8.9",
            "Below a fixed cutoff beyond all size, precision, margin and layout conditions, schoolbook multiplication is used and the finitely many smaller lengths are absorbed in the implicit constant, giving one fixed machine with worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every $n$.",
            r"conditions, and use schoolbook multiplication below it."),
    ],
    page="time-accounting",
    frm=["exact-recovery", "transform-layout", "tensor-resampling-box", "size-parameters", "crt-prime-axes", "ring-convolution", "big-o"],
    salient="The smallest of the seven margins is $2^{-181}=2\\kappa$, so the astronomically small saving $\\kappa=2^{-182}$ is dictated by one product of tiny exponents, $\\epsilon c(1-\\tau)$.")

S6 = show("S6",
    "Splitting the operands into radix digits, mapping them by $\\Phi$ to prime axes, applying the source transform to each, multiplying pointwise, applying the opposite transform, rescaling by $S$ and $2^{2b+4}$, rounding, undoing $\\Phi$ and propagating carries yields the exact $2n$-bit product within the cost table.",
    "Fix parameters compatible with all the procedures, implement each stage of the reduction chain, prove the error is below $1/2$ so rounding is exact, and total the costs",
    mot("Each reduction (digits to prime axes, prime axes to power-of-two axes, power-of-two axes to the ring) changes only the representation, so the algorithm is the composition of the reductions with exact known rescalings undone at the end.", "recoverable"),
    [S6_1, S6_2, S6_3, S6_4, S6_5] + S6_6 + [S6_7, S6_8],
    page="multiplication-algorithm",
    frm=["source-transform", "crt-prime-axes", "coefficient-twist", "prime-lengths", "size-parameters", "radix-digit-convolution", "cyclic-convolution"],
    adds=[B("p", "precision", "Number of fractional bits of the fixed-point grid, $p=6b$.", "count"),
          B("T", "box size", "Number of entries in the padded power-of-two box, a power of two near $n/b$.", "count"),
          B("r", "record length", "Number of complex coefficients in a polynomial record, a power of two $r=2^\\ell$.", "count"),
          B("\\ell", "log record length", "Base-two logarithm of $r$.", "direct"),
          B("S", "source size", "Product $s_1\\cdots s_d$ of the pairwise coprime prime source lengths.", "direct")])

ROOT = show("S0",
    "A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
    "Reduce the product to a convolution of radix-digit coefficients, evaluate that convolution by Gaussian-resampling, chirp and synthetic transforms whose address moves and butterfly layers are accelerated by a rank-saving recursion, then recover the exact product and total the cost",
    mot("Scanning an array of $\\Theta(n)$ stored bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so savings are needed in both address movement and arithmetic; the two tape procedures supply them inside the transform pipeline.", "explicit", r"We therefore need savings in both movement and arithmetic."),
    [S1, S2, S3, S4, S5, S6],
    page="main-theorem",
    frm=["nlogn-conjecture", "multitape-model", "nlogn-multiplier", "big-o"],
    salient="The saving is a power of the logarithm, $(\\lg n)^{1-\\kappa}$ with $\\kappa=2^{-182}$: astronomically small but strictly positive, which refutes the $n\\log n$ optimality conjecture.")

# --------------------------------------------------------------- finalize
def renumber(node, newid):
    node["id"] = newid
    for i, c in enumerate(node.get("children", []), 1):
        renumber(c, newid + "." + str(i) if newid != "S0" else "S" + str(i))

renumber(ROOT, "S0")

# check
infers = []
def walk(n):
    if n["intention"] == "infer":
        infers.append(n)
    for c in n.get("children", []):
        walk(c)
walk(ROOT)
pos = -1
ok = True
for n in infers:
    q = n["quote"]["quote"]
    cnt = SRC.count(q)
    p = SRC.find(q)
    if cnt != 1:
        print("COUNT", cnt, n["id"], q[:70]); ok = False
    if p <= pos and not n.get("deferred"):
        print("ORDER", n["id"], q[:70], p, pos); ok = False
    pos = max(pos, p) if p > pos else pos
# motivation quotes
def walk2(n):
    m = n.get("motivation")
    if m and m.get("quote"):
        q = m["quote"]["quote"]
        if SRC.count(q) < 1:
            print("MOTQ", n["id"], q[:70]); 
    for c in n.get("children", []):
        walk2(c)
walk2(ROOT)
ids = []
def walk3(n):
    ids.append(n["id"])
    for c in n.get("children", []): walk3(c)
walk3(ROOT)
assert len(ids) == len(set(ids))
# pages
pages = []
def walk4(n):
    if n.get("page"): pages.append(n["page"])
    for c in n.get("children", []): walk4(c)
walk4(ROOT)
import collections
print([p for p, c in collections.Counter(pages).items() if c > 1])
print(len(infers), "infers", len(ids), "nodes", "OK" if ok else "FAIL")
json.dump({"root": ROOT}, open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E8F5X/exegenius/tasks/0003-argument.answer.json', 'w'), indent=1)
