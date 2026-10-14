from lib import *
from rc import RC
from resample import GR, TEN, BC, PCh
from asm1 import PAR


def CRT():
    return show(
        "The Agarwal-Cooley map $\\Phi:\\mathbb C[x]/(x^S-1)\\to\\mathbb C[x_1,\\dots,x_d]/(x_i^{s_i}-1)$, $x\\mapsto\\prod_ix_i^{\\mu_i}$, is an algebra isomorphism preserving cyclic convolution, and it is realized on the padded box by $d$ prefix-controlled cyclic shifts and axis reorderings in time $O(Tp\\,d^2(1+\\ell^\\tau))$.",
        "Prove the isomorphism from the order of the image of $x$, write the new coordinates in triangular form so that each depends only on lower-index digits, and perform the updates as controlled shifts in the order of the physical axes.",
        "The following map uses the Chinese-remainder split, with coordinate powers chosen to make the change of order a sequence of controlled cyclic shifts.",
        "explicit",
        mq=r"sequence of controlled cyclic shifts.",
        page="crt-address-map",
        frm=["cyclic-convolution", "chinese-remainder-theorem", "controlled-shift", "address-chunk-interchange", "primes-coprimality-and-gcd", "modular-arithmetic", "polynomials"],
        salient="Each new coordinate $b_i$ depends only on the lower-index digits $a_j$, $j<i$, because terms with $j>i$ are multiples of $s_i$ and $\\mu_iP_i\\equiv1$; this triangularity is what turns the CRT change of order into controlled shifts with controls preceding targets.",
        adds=[("P_i", "prefix product", "The product $\\prod_{j<i}s_j$ of the earlier prime lengths.", "direct"),
              ("\\mu_i", "CRT exponent", "The inverse of $P_i$ modulo $s_i$, the exponent of $x_i$ in the image of $x$.", "direct")],
        children=[
            infer("Put $P_i=\\prod_{j<i}s_j$ and $\\mu_i=P_i^{-1}\\pmod{s_i}$.",
                  r"P_i=\prod_{j<i}s_j,\qquad \mu_i=P_i^{-1}\pmod{s_i}."),
            infer("The image of $x$ has order $S$ and its powers run through all target monomials exactly once, so $\\Phi$ is an isomorphism preserving cyclic convolution.",
                  r"$\Phi$ is an isomorphism and preserves cyclic convolution."),
            infer("The coordinate of $\\Phi(x^k)$ in axis $i$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}$ for the mixed-radix digits $k=\\sum_ja_jP_j$.",
                  r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}."),
            infer("Terms with $j>i$ are divisible by $s_i$ and $\\mu_iP_i=1$ modulo $s_i$, which makes the formula triangular.",
                  r"Indeed terms with $j>i$ are divisible by $s_i$, and $\\mu_iP_i=1$ modulo".replace("\\\\","\\")),
            infer("Updating the targets in the order $i=d,d-1,\\dots,1$ means each target's lower-index controls still hold their original digits.",
                  r"order $i=d,d-1,\ldots,1$ using"),
            infer("Each step preserves the valid box $\\prod[0,s_i)$ and its complement, so zero padding remains zero after every step.",
                  r"zero padding remains zero after every step."),
            infer("Each triangular update is a prefix-controlled cyclic shift: prepare the offset, split the valid target interval into two pieces, and merge them in opposite order.",
                  r"Each triangular update is a prefix-controlled cyclic shift."),
            infer("Reversing all axes uses $O(d^2)$ adjacent moves, each an equal-width chunk swap after peeling a leading bit when widths differ.",
                  r"uses $O(d^2)$ such moves."),
            infer("Therefore the map $\\Phi$, its inverse and the padding operations cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
                  r"their padding operations cost"),
        ])


def PT():
    return show(
        "The map $\\Theta:\\mathbb C[x_d]/(x_d^r-1)\\to\\mathbb C[y]/(y^r+1)$, $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$, is a norm-preserving isomorphism multiplying coefficient $k$ by $\\zeta^k$, and the negative wrap of the target becomes the cyclic wrap of the source after untwisting.",
        "Check well-definedness on $x_d^r-1$, observe that the map is diagonal in the monomial bases, and verify the sign of the wrapped terms directly.",
        "The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist.",
        "explicit",
        mq=r"obtained from the synthetic convolution by a coefficient twist.",
        page="phase-twist",
        frm=["polynomial-ring-mod", "cyclic-convolution", "complex-numbers", "roots-of-unity"],
        children=[
            infer("The map is well defined since $(\\zeta y)^r=(-1)(-1)=1$.",
                  r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."),
            infer("On the monomial bases it is diagonal, multiplying coefficient $k$ by the nonzero number $\\zeta^k$, hence an isomorphism with inverse multiplying by $\\zeta^{-k}$ and preserving the coefficient sup norm.",
                  r"multiplying coefficient $k$ by the nonzero number $\zeta^k$."),
            infer("For $k+l=j+hr$ with $h\\in\\{0,1\\}$ the product term has factor $\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j$, so untwisting recovers the cyclic coefficient with the right sign.",
                  r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j."),
        ])


def ER():
    return show(
        "The recovered integer coefficients have error below $1/2$ after the final rescaling, so rounding is exact, and radix-$2^b$ carries produce the $2n$-bit product.",
        "Track errors in units of $h_p=2^{-p}$ through twist, ring convolution, chirp, source transform, pointwise product and opposite transform; rescale by $2^{2b+4}S$ and compare with $1/2$ using $p=6b$; then propagate carries with an explicit invariant.",
        "Each stage is a contraction or bilinear contraction of norm at most one, so errors add; the working precision $p=6b$ leaves a margin of about $2^{-3b/4}$ against the factor $2^{2b+4}S$ that restores the integer scale.",
        "explicit",
        mq=r"disk bounds needed by every call and proves that the final error is",
        page="exact-recovery",
        frm=["radix-digit-convolution", "fixed-point-truncation", "norms-absolute-values-and-error-bounds", "binary-representation-and-bit-operations", "floor-ceiling-and-summation-notation"],
        salient="The final error bound $448b\\,2^{-b+\\gamma}$ is dominated by $2^{-3b/4}$ because the gain $2^{2b+4}S\\le2^{3b+4}$ and the Gaussian scale $2^\\gamma$ are both small against the precision margin $2^{-6b}$.",
        adds=[("h_p", "grid step", "The grid spacing $2^{-p}$ in which all errors are measured.", "direct"),
              ("L", "log of box size", "The integer $\\log_2T$, at most $b$.", "direct"),
              ("E_s", "source error", "The error bound $9\\,2^\\gamma TL$ (in units of $h_p$) of the computed source transform.", "direct")],
        children=[
            infer("For a bilinear contraction the replaced-operand difference is bounded by $\\|f'-f\\|\\|g'\\|+\\|f\\|\\|g'-g\\|$, so for disk operands the two errors add.",
                  r"\|\mathcal M(f',g')-\mathcal M(f,g)\|"),
            infer("The ring convolution error before scaling is $E_{\\rm ring}=M(3L+2)<5TL$ in units of $h_p$.",
                  r"E_{\rm ring}:=M(3L+2)<5TL."),
            infer("The computed complex convolution then has error below $(E_{\\rm ring}+4+4+4)h_p<6TLh_p$, adding two twist errors of at most four and the output untwist.",
                  r"<(E_{\rm ring}+4+4+4)h_p<6TLh_p."),
            infer("The chirp transform has error below $(6TL+2+4+4)h_p<8TLh_p$, adding the kernel and two endpoint products.",
                  r"<(6TL+2+4+4)h_p<8TLh_p."),
            infer("The source transform has error below $E_sh_p$ with $E_s=9\\,2^\\gamma TL$, after adding the expansion and compression errors $2dp^2$ and scaling by $2^\\gamma$.",
                  r"E_s=9\,2^\gamma TL,"),
            infer("The pointwise product satisfies $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$, and the opposite transform gives $\\|\\widetilde{\\mathscr F}^+(z)-G(U\\cdot V_1)\\|<(3E_s+2)h_p$.",
                  r"Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$."),
            infer("After the first scale by $S$, the error of $\\widetilde w$ against $(u*v)/S$ is below $E_wh_p$ with $E_w=S(3E_s+2)<28\\,2^\\gamma T^2L$.",
                  r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
            infer("After the second scale the absolute error is below $2^{2b+4}S\\cdot28\\,2^\\gamma T^2L\\cdot2^{-6b}<448b\\,2^{-b+\\gamma}\\le448b\\,2^{-3b/4}<\\frac12$, using $S\\le T<2^b$, $L<b$ and $\\gamma\\le b/4$.",
                  r"448b\,2^{-b+\gamma}"),
            infer("Since the true coefficients are integers and the error is strictly below $1/2$, the nearest integer to the represented value is the correct coefficient, in $[0,2^{3b})$.",
                  r"The true coefficients are real integers."),
            infer("Carries are computed by $k_0=0$, $d_j=(c_j+k_j)\\bmod Q_0$, $k_{j+1}=\\lfloor(c_j+k_j)/Q_0\\rfloor$ with $Q_0=2^b$, and $0\\le k_j\\le q(Q_0-1)<Q_0^2$.",
                  r"k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad"),
            infer("The invariant $\\sum_{h<j}c_hQ_0^h=\\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ fixes the first $j$ radix digits of the product, and the stream is reversed and cut to exactly $2n$ bits.",
                  r"\sum_{h<j}c_hQ_0^h"),
        ])


def MA():
    pipe = show(
        "Running the six steps (address map $\\Phi$, two source transforms, pointwise product, opposite source transform with two rescalings, rounding with inverse map, carry propagation) turns the radix digits into the $2n$-bit product.",
        "Read the digits into the padded array and apply the six operations in order, with the two factors of $S$ undoing different normalizations.",
        "Once the source transforms are available as black boxes with known exact counterparts, the product is the convolution theorem on the prime-axis array followed by the known rescalings.",
        "recoverable",
        children=[
            infer("Read each operand backward in groups of $b$ bits to obtain the radix-$2^b$ digits in increasing coefficient order and write them as exact grid values $a_j2^{-b-2}$, padding with zero coefficient records up to $S$.",
                  r"Read each stored operand backward from"),
            infer("Step 1: apply the coefficient-address map $\\Phi$ with its padded layout to obtain source arrays $u,v$ of norm below $1/4$.",
                  r"Apply the coefficient-address map $\Phi$, with its padded layout, to obtain"),
            infer("Step 2: compute $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$.",
                  r"Compute $\widetilde{\mathscr F}(u)$ and"),
            infer("Step 3: multiply corresponding coefficients exactly and truncate toward zero to $p$ fractional bits, obtaining $z$.",
                  r"Multiply corresponding complex coefficients exactly and truncate"),
            infer("Step 4: compute $\\widetilde{\\mathscr F}^+(z)$ and multiply its numerators exactly by $S$, giving $\\widetilde w$.",
                  r"Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid"),
            infer("Step 5: multiply by $2^{2b+4}S$, round to the nearest integers, store each in a signed $(3b+1)$-bit word, and apply $\\Phi^{-1}$ with padding removal.",
                  r"Multiply the grid numerators of $\widetilde w$ exactly by"),
            infer("Step 6: propagate radix-$2^b$ carries in increasing order and output exactly $2n$ bits most significant first.",
                  r"Propagate radix-$2^b$ carries in increasing coefficient order."),
            infer("The two occurrences of $S$ undo different normalizations: the exact counterpart after three transforms is $(u*v)/S^2$, so after the first scale it is $(u*v)/S$, and the second scale with $2^{2b+4}$ restores $2^{2b+4}(u*v)$.",
                  r"The two occurrences of $S$ in this algorithm undo different"),
        ])
    return show(
        "The pipeline of radix digits, the Chinese-remainder address map, two source transforms, a pointwise product, the opposite transform, known rescalings, rounding and carries returns exactly the $2n$-bit product of the two inputs.",
        "Assemble the engine from the inside out: first the ring convolution, then Gaussian resampling and chirps that turn prime-axis transforms into it, then the layout, parameters and twist that fit the sizes together, then run the six steps and bound the rounding error.",
        "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.",
        "explicit",
        mq=r"Splitting the inputs into radix digits reduces multiplication to",
        page="multiplication-algorithm",
        frm=["radix-digit-convolution", "crt-address-map", "gaussian-resampling", "permutation-cancellation", "bluestein-chirp", "phase-twist", "ring-convolution", "exact-recovery", "parameter-choice", "fixed-point-truncation", "cyclic-convolution"],
        adds=[("b", "digit size", "The number $\\lceil\\log_2n\\rceil$ of bits per radix digit.", "count"),
              ("p", "precision", "The number $6b$ of fractional bits of every stored real or imaginary component.", "count"),
              ("d", "axis count", "The number $\\lfloor b^\\epsilon\\rfloor$ of axes of the transform array.", "count"),
              ("K", "chunk width", "The number $\\lfloor d^c\\rfloor$ of address bits in a chunk.", "count"),
              ("r", "record length", "The power of two $2^{\\lceil(\\log_2T)/d\\rceil}$ of complex coefficients per polynomial record, also the longest axis.", "count"),
              ("\\ell", "log record length", "The integer $\\log_2r$.", "direct"),
              ("T", "padded size", "The power of two in $[4n/b,8n/b)$ equal to the product of the axis lengths $t_i\\in\\{r/2,r\\}$.", "count"),
              ("S", "prime box size", "The product of the distinct prime source lengths $s_i$, with $T/2<S<T$.", "count"),
              ("\\epsilon", "axis exponent", "The fixed exponent $2^{-75}$ with $d=\\lfloor b^\\epsilon\\rfloor$.", "direct"),
              ("c", "chunk exponent", "The fixed exponent $2^{-56}$ with $K=\\lfloor d^c\\rfloor$.", "direct")],
        children=[
            RC(),
            GR(),
            TEN(),
            BC(),
            PCh(),
            PAR(),
            CRT(),
            PT(),
            infer("Normalized complex cyclic convolution is $\\mathcal M_{\\mathbb C}(f,g)=D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$ with the twists $D_\\pm$.",
                  r"\mathcal M_r(\iota D_+f,\iota D_+g)"),
            infer("The computed version twists both operands by approximate phases $\\widetilde\\theta^+$, convolves over the ring with the synthetic convolution, and untwists.",
                  r"f'&=Q_p(\widetilde\theta^+\mathbin{\cdot}f),"),
            infer("The computed chirp transform multiplies by $\\overline{\\widetilde a}$, convolves with the kernel $\\widetilde a$ and multiplies by $\\overline{\\widetilde a}$ again.",
                  r"x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),"),
            infer("The source transform applies $\\mathcal A$, the chirp transform, $\\mathcal B_0$ and the exact scale $2^\\gamma$; its exact counterpart is $RF_{\\boldsymbol s}$.",
                  r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A"),
            pipe,
            ER(),
        ])


def TA():
    rows = [
        ("Prefix-slot moves and individual butterfly rounds cost $dK$ per unit volume, a power $\\epsilon(1+c)$ of $p$.", r"Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$"),
        ("Chunk exchanges for transform layout cost $pK^{\\tau-1}$, a power $1-\\epsilon c(1-\\tau)$ of $p$.", r"Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$"),
        ("Simultaneous butterfly rounds cost $\\ell d^{\\lambda'}$, a power $1-\\epsilon(1-\\lambda')$ of $p$.", r"Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$"),
        ("CRT and axis layouts cost $d^2(1+\\ell^\\tau)$, a power $\\tau+\\epsilon(2-\\tau)$ of $p$.", r"CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$"),
        ("Gaussian line maps cost $dp^{1/2+\\delta}\\alpha$, a power $3/4+\\delta+3\\epsilon/2$ of $p$.", r"Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$"),
        ("Chirps, twists and scalar products cost $dp^\\delta$, a power $\\epsilon+\\delta$ of $p$.", r"Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$"),
        ("Packed polynomial products cost $\\log(rp)$, a power $1-\\epsilon$ of $p$.", r"Packed polynomial products & $\log(rp)$ & $1-\epsilon$"),
    ]
    table = show(
        "Divided by $V=Tp=\\Theta(n)$, the seven dominant operations cost $p$ to the powers $\\epsilon(1+c)$, $1-\\epsilon c(1-\\tau)$, $1-\\epsilon(1-\\lambda')$, $\\tau+\\epsilon(2-\\tau)$, $3/4+\\delta+3\\epsilon/2$, $\\epsilon+\\delta$ and $1-\\epsilon$, and the remaining rows are absorbed.",
        "Charge each operation of the algorithm to a row of a cost table in units of $V$, using the cost of the lemma that performs it.",
        "Every lemma states its cost per unit volume, so the total is the sum of the costs of the operations the algorithm performs, each counted a fixed number of times.",
        "recoverable",
        children=[infer("Table row: " + c, q) for (c, q) in rows])
    margins = show(
        "The seven margins $g_i$ below one are $g_1>\\frac12$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>\\frac18$, $g_6>\\frac12$, $g_7=2^{-75}$, so $\\min_ig_i=2^{-181}=2\\kappa$.",
        "Substitute the fixed rational exponents $\\epsilon=2^{-75}$, $c=2^{-56}$, $\\tau=1-2^{-50}$, $\\lambda'=1-2^{-54}$, $\\delta=1/16$ into the seven exponents and read off the gap to one.",
        "Only the gap of each power below one matters for the final bound, so list the gaps and take the smallest.",
        "recoverable",
        salient="The minimum margin $g_2=\\epsilon c(1-\\tau)=2^{-75}\\cdot2^{-56}\\cdot2^{-50}=2^{-181}$ comes from the chunk exchanges: the saving $K^{\\tau-1}$ per exchange is weak because $K=d^c$ is tiny, and this single row dictates $\\kappa=2^{-182}$.",
        children=[
            infer("The margins are $g_1=1-\\epsilon(1+c)$, $g_2=\\epsilon c(1-\\tau)$, $g_3=\\epsilon(1-\\lambda')$, $g_4=1-\\tau-\\epsilon(2-\\tau)$, $g_5=1/4-\\delta-3\\epsilon/2$, $g_6=1-\\delta-\\epsilon$, $g_7=\\epsilon$.",
                  r"g_1&=1-\epsilon(1+c),\qquad"),
            infer("Direct substitution gives $g_1>\\frac12$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>\\frac18$, $g_6>\\frac12$, $g_7=2^{-75}$.",
                  r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad"),
            infer("Thus $\\min_ig_i=2^{-181}=2\\kappa$, explicit slack that will cover any remaining fixed power of $\\log p$.",
                  r"Thus $\min_i g_i=2^{-181}=2\kappa$."),
        ])
    return show(
        "Each cost row, divided by $V=Tp=\\Theta(n)$, is at most $p^{1-2\\kappa}$ with $\\kappa=2^{-182}$, so the complete bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\lg n)^{1-\\kappa})$.",
        "Tabulate the normalized cost of every operation as a power of $p$, compute the seven margins below one, justify each row from the lemma that performs it, bound setup and exceptional streams, and absorb powers of $\\log p$ using the slack.",
        "The tape procedures give each cost as a power of the layer parameters, so the total is a sum of powers of $p$ and only the gaps below one decide the final exponent.",
        "recoverable",
        page="time-accounting",
        frm=["multiplication-algorithm", "parameter-choice", "address-chunk-interchange", "fast-butterfly-layer", "established-multiplier", "ring-convolution", "big-o", "logarithms-and-iterated-logarithm-notation"],
        children=[
            table,
            margins,
            infer("The first three rows are the terms of the transform cost; the layout needs $O(p/K)$ exchanges of width-$K$ chunks, each costing $O(VK^\\tau)$, so the normalized total is $O(p/K)K^\\tau=O(pK^{\\tau-1})$.",
                  r"O(p/K)\,K^\tau=O(pK^{\tau-1})."),
            infer("Axis exposure and restoration require $O(d^2)$ adjacent axis moves, each costing $O(V(1+\\ell^\\tau))$.",
                  r"Axis exposure and restoration require $O(d^2)$ adjacent axis moves."),
            infer("The factor $\\alpha=\\Theta(p^{1/4+\\epsilon/2})$ gives the displayed power of $p$ for Gaussian line maps.",
                  r"$\alpha=\Theta(p^{1/4+\epsilon/2})$ explains its displayed power of $p$."),
            infer("The layer and address recursions have at most $p^A$ visits with setup $p^C$ each, so setup costs at most $p^{A+C}=o(Tp)$ because $r$ exceeds every fixed power of $p$.",
                  r"costs at most $p^{A+C}=o(Tp)$."),
            infer("Each of the seven powers is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually.",
                  r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
            infer("The complete large-input bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
                  r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})."),
            infer("Below a fixed cutoff use schoolbook multiplication; the single fixed-alphabet, fixed-tape machine then has worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every input length.",
                  r"Fix one cutoff beyond all the size, precision, margin and layout"),
        ])


def ROOT():
    return show(
        "A single deterministic multitape Turing machine with a fixed finite alphabet multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$, disproving the $n\\log n$ optimality conjecture.",
        "Reduce the product to a convolution of short digits, supply the convolution by power-of-two synthetic transforms whose tape layouts and butterfly layers are made cheap by two rank-saving tape procedures, recover the integers exactly by rounding and carries, and total the cost.",
        "We therefore need savings in both movement and arithmetic.",
        "explicit",
        mq=r"We therefore need savings in both movement and arithmetic.",
        page="main-theorem",
        frm=["integer-multiplication-conjecture", "multitape-tm", "big-o", "logarithms-and-iterated-logarithm-notation"],
        salient="The saving is a whole power $(\\lg n)^{-\\kappa}$ of the logarithm, however tiny $\\kappa=2^{-182}$ is, and it comes from a single strict inequality $s<Wm$ in two finite networks, not from any new multiplication method.",
        adds=[("n", "input length", "The common bit length of the two operands.", "count"),
              ("\\kappa", "saving exponent", "The fixed constant $2^{-182}$ with which the running time falls below $n\\log n$ by the factor $(\\lg n)^{-\\kappa}$.", "direct")],
        children=[MA(), TA()])
