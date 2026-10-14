from lib import *
from t_s1 import s0_1
from t_s1b import chunk_interchange
from t_s2 import simultaneous_layer
from t_s3 import ring_convolution
from t_s4 import mult_algorithm

# ---------------------------------------------------------------- parameter balance (S5)
def parameter_balance():
    rows = show(
        'S5.5',
        r"""The first six rows of the table are the costs established earlier, each divided by $V=Tp$: the transform layout gives $dK$, $pK^{\tau-1}$ and $\ell d^{\lambda'}$, the CRT and axis layouts $d^2(1+\ell^\tau)$, the Gaussian line maps $dp^{1/2+\delta}\alpha$, and the chirps, twists and packed products $dp^\delta$ and $\log(rp)$.""",
        r"""Take each row from the lemma that bounds the corresponding operation, divide by $V=Tp$, and express it as a power of $p$ using $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $\alpha=\Theta(p^{1/4+\epsilon/2})$.""",
        r"""Each row must be traced to the lemma that bounds its operation, so that the table is a faithful account of every change of representation in the algorithm.""",
        'recoverable',
        frm=['transform-layout', 'chunk-interchange', 'simultaneous-layer', 'crt-axis-map', 'gaussian-resampling', 'kronecker-packing', 'ring-convolution', 'nlogn-multiplier'],
        children=[
            infer('S5.5.1',
                  r"""The first three rows are the terms of the transform-layout bound: the $O(dK)$ prefix scans, $O(p/K)$ exchanges of $K$-bit chunks each costing $O(VK^\tau)$ because $d\ell=O(p)$, giving $O(pK^{\tau-1})$, and at most $\ell$ simultaneous rounds of $O(Vd^{\lambda'})$ each.""",
                  Q(r"Here $d^2$ is absorbed by $d^2\ell^\tau$, and", r"and fixed-tape cleanup.")),
            infer('S5.5.2',
                  r"""Axis exposure and restoration need $O(d^2)$ adjacent axis moves each costing $O(V(1+\ell^\tau))$ by peeling a single excess bit, the $d$ CRT rotations copy intervals in $O(dV)$, and their offset setup is $O(dTp^C/r)=o(Tp)$.""",
                  Q(r"Axis exposure and restoration require $O(d^2)$ adjacent axis moves.", r"using at most $T/t_i$ control prefixes for target $i$.")),
            infer('S5.5.3',
                  r"""For Gaussian resampling axis $i$ has at most $T/t_i$ lines, whose line machines sum to $\sum_i\frac T{t_i}O(t_ip^{3/2+\delta}\alpha)=O(dTp^{3/2+\delta}\alpha)$, and dividing by $V=Tp$ with $\alpha=\Theta(p^{1/4+\epsilon/2})$ gives the displayed power of $p$.""",
                  Q(r"For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines.", r"explains its displayed power of $p$.")),
            infer('S5.5.4',
                  r"""Chirp numerators, twists and scalar products use a fixed number of exact products on $O(p)$-bit numerators costing $O(dp^{1+\delta})$ per entry, the two final scalings by the product of the prime lengths cost $O(p^\delta)$, the $T/r$ ring products cost $O(Tp\log(rp))$ from four integer products on $O(rp)$ bits, and these calls use only the established multiplier on records of length $O(rp)=o(n)$, never the improved algorithm itself.""",
                  Q(r"Chirp numerators have $O(p)$ bits and can be computed modulo $2r$ as", r"within the listed scan costs.")),
        ])
    return show(
        'S5',
        r"""With the fixed rational exponents ($\tau=\sigma=1-2^{-50}$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\epsilon=2^{-75}$, $\delta=1/16$) every one of the seven dominant rows of the cost table has normalized power of $p$ at most $1-2\kappa$, so the total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ for $\kappa=2^{-182}$.""",
        r"""Divide each operation's cost by $V=Tp$ via the lemma that bounds it, write it as a power of $p$, compute the seven margins $g_i$ and their minimum $2^{-181}=2\kappa$, let that slack absorb fixed powers of $\log p$, and use schoolbook multiplication below a cutoff.""",
        r"""The minimum margin $2^{-181}=2\kappa$ is an explicit slack that covers any remaining fixed power of $\log p$ left over from the setup and exceptional-stream costs.""",
        'explicit',
        mot_quote=Q(r"Thus $\min_i g_i=2^{-181}=2\kappa$.", r"fixed power of $\log p$."),
        page='parameter-balance',
        frm=['chunk-interchange', 'simultaneous-layer', 'ring-convolution', 'crt-axis-map', 'prime-lengths', 'gaussian-resampling', 'source-transform', 'exact-recovery', 'mult-algorithm', 'nlogn-multiplier', 'logarithms-and-exponentials', 'asymptotic-notation-beyond-big-o'],
        adds=adds_(
            (r'\epsilon', 'dimension exponent', r'The fixed exponent $2^{-75}$ in $d=\lfloor b^\epsilon\rfloor$, so the number of axes is $\Theta(p^\epsilon)$.', 'direct'),
            (r'c', 'chunk exponent', r'The fixed exponent $2^{-56}$ in $K=\lfloor d^c\rfloor$ giving the chunk size.', 'direct'),
            (r'\delta', 'multiplier slack', r'The fixed constant $1/16$ in the cost exponents of the Gaussian line maps and the short multiplications.', 'direct'),
            (r'T', 'padded array size', r'The number of complex coefficients of the padded transform array, a power of two in $[4n/b,8n/b)$, so $Tp=\Theta(n)$.', 'count'),
            (r'\ell', 'ring exponent', r'The base-2 logarithm of $r$, so $r=2^\ell=2^{\Theta(p^{1-\epsilon})}$.', 'direct'),
            (r't_i', 'axis length', r'The power of two $r/2$ or $r$ that is the length of the $i$-th of the $d$ axes, with $\prod_it_i=T$.', 'count'),
            (r'\alpha', 'Gaussian parameter', r'The integer $\lceil(12d^2b)^{1/4}\rceil=\Theta(p^{1/4+\epsilon/2})$ controlling the width of the Gaussian weights.', 'direct'),
            (r'g_i', 'margin', r'The amount by which the power of $p$ of the $i$-th dominant row of the cost table lies below one.', 'direct'),
        ),
        salient=r"""$\kappa=2^{-182}$ is exactly half of the smallest margin $g_2=\epsilon c(1-\tau)=2^{-75-56-50}=2^{-181}$, the margin of the chunk exchanges for the transform layout, so the saving is limited by the product of three tiny exponents.""",
        children=[
            infer('S5.1',
                  r"""The fixed rational numbers are $\tau=\sigma=1-2^{-50}$, $\beta=\frac12$, $\delta=\frac1{16}$, $\lambda=1-2^{-52}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$, deliberately conservative with no optimization claimed.""",
                  Q(r"Take the following fixed rational numbers:", r"no optimization is claimed."),
                  deferred=True),
            infer('S5.2',
                  r"""The layer conditions hold with room to spare: $\max\{\tau,\sigma\}<\lambda<1$, $\tau(1+c/\beta)<1-31\cdot2^{-55}<\lambda$, $\sigma+\beta(1-\sigma)=1-2^{-51}<\lambda<\lambda'<1$, and the dimension exponent satisfies $\epsilon<\frac1{12}$, $\epsilon C_1<1$, $\epsilon(2-\tau)<1-\tau$, $\frac34+\delta+\frac32\epsilon<1$, $\epsilon(1+c)<1$ and $\epsilon+\delta<1$.""",
                  Q(r"The layer conditions hold with room to spare:", r"\epsilon+\delta<1."),
                  deferred=True),
            infer('S5.3',
                  r"""With $V=Tp=\Theta(n)$ and $\Theta(p)$ bits per coefficient a full padded array has $\Theta(V)$ stored bits, and the table lists the cost of each operation after division by $V$, a fixed number of repeated transforms and convolutions being absorbed in the constants.""",
                  Q(r"For the cost calculation put $V=Tp=\Theta(n)$.", r"is included in its constants.")),
            infer('S5.4',
                  r"""The seven dominant powers have margins $g_1=1-\epsilon(1+c)>\frac12$, $g_2=\epsilon c(1-\tau)=2^{-181}$, $g_3=\epsilon(1-\lambda')=2^{-129}$, $g_4=1-\tau-\epsilon(2-\tau)>2^{-51}$, $g_5=\frac14-\delta-\frac32\epsilon>\frac18$, $g_6=1-\delta-\epsilon>\frac12$ and $g_7=\epsilon=2^{-75}$, so $\min_ig_i=2^{-181}=2\kappa$.""",
                  Q(r"The seven dominant powers in Table~\ref{tab:costs} have the following", r"any remaining fixed power of $\log p$.")),
            rows,
            infer('S5.6',
                  r"""Setup at recursion nodes and per record or Gaussian line is polynomial in $p$: with at most $p^A$ visits and $p^C$ setup per visit, and $O(p^C)$ per record or per line over $O(T/r)$ records or $\le2dT/r$ lines, the total is $o(Tp)$ because $r$ exceeds every fixed power of $p$.""",
                  Q(r"We next separate setup at recursion nodes from work repeated for every", r"fixed power of $p$.", line=4913)),
            infer('S5.7',
                  r"""For one-bit payloads the descriptor estimate of the power-width proposition, $(\log2V_0)^{O(1)}=O(V_j)$ at every child, still applies, and the chirp computation scans the axis descriptors at every coefficient, already charged in its row.""",
                  Q(r"The general address-swap subroutine also covers one-bit payloads,", r"its $O(Tdp^{1+\delta})$ cost was included in the chirp row.")),
            infer('S5.8',
                  r"""The exceptional records of a packed change of basis number a fraction $O(d2^{-K})$ of the records independently of the payload, so the compact exceptional stream has length $O(V_{\rm call}d2^{-K})$, its stable bit sorting costs $O(V_{\rm call}dp2^{-K})$ per call, and summed over at most $p^A$ visits it is $O(Vp^{A'}2^{-K})=o(V)$ in the worst case.""",
                  Q(r"For one packed change of basis, let $V_{\rm call}$ be its current", r"This is a deterministic worst-case bound.")),
            infer('S5.9',
                  r"""All role, arithmetic and stack tapes form fixed finite families, a child parks and restores only its parent's streams, no operation scans parked ancestors, growing lists are stored data rather than tapes or alphabet symbols, and global setup and prime search cost $o(V)$.""",
                  Q(r"Finally, all role, arithmetic, and stack tapes form fixed finite", r"as proved earlier.")),
            infer('S5.10',
                  r"""Each of the seven powers is at most $1-2\kappa$ and any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the large-input bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$, and using schoolbook multiplication below one cutoff gives a single fixed-alphabet, fixed-tape deterministic machine with worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length that outputs the exact $2n$-bit product.""",
                  Q(r"Each of the seven displayed powers is at most $1-2\kappa$ by", r"produces precisely the required $2n$-bit product.")),
        ])

# ---------------------------------------------------------------- root
def root():
    return show(
        'S0',
        r"""There is one deterministic fixed-alphabet, fixed-tape Turing machine that multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time, with $\kappa=2^{-182}$, which disproves the $n\log n$ optimality conjecture in this model.""",
        r"""Reduce the refutation to the upper bound, then build the algorithm bottom-up: the two power-saving tape procedures (address-chunk interchange and simultaneous butterfly layers), the exact ring convolution that uses them, the multiplication algorithm with its exactness proof, and the parameter balance.""",
        r"""A transform-based multiplier pays $\Theta(n)$ per level over $\Theta(\log n)$ levels, which is already $n\log n$, so going below it needs savings in both data movement and arithmetic; the proof therefore builds the two procedures that supply them first and assembles the multiplication on top.""",
        'explicit',
        mot_quote=Q(r"Scanning an array of", r"savings in both movement and arithmetic."),
        page='main-theorem',
        frm=['nlogn-conjecture', 'nlogn-multiplier', 'fixed-tape-model', 'chunk-interchange', 'simultaneous-layer', 'ring-convolution', 'mult-algorithm', 'parameter-balance', 'tape-machines', 'big-o', 'asymptotic-notation-beyond-big-o', 'logarithms-and-exponentials', 'determinism-and-exact-versus-approximate-computation'],
        adds=adds_(
            (r'V', 'stored bit volume', r'The number of data bits stored in the array a tape procedure acts on, temporary work tapes not counted.', 'count'),
            (r'p', 'working precision', r'The number of fractional bits kept for each real or imaginary part of a complex coefficient, $p=6\lceil\log_2n\rceil=\Theta(\log n)$.', 'count'),
            (r'd', 'axis count', r'The number of power-of-two axes of the transform array, $d=\Theta(p^\epsilon)$ for a fixed small $\epsilon>0$.', 'count'),
            (r'K', 'chunk size', r'The number of address bits in one chunk, $K=\Theta(p^{\epsilon c})$ for a fixed small $c>0$.', 'count'),
            (r'r', 'ring dimension', r'The number of complex coefficients in a polynomial record modulo $y^r+1$, a power of two with $r=2^{\Theta(p/d)}$.', 'count'),
            (r'\tau', 'interchange exponent', r'A fixed constant $0<\tau<1$, here $1-2^{-50}$, in the cost $O(Vu^\tau)$ of interchanging two $u$-bit address chunks.', 'direct'),
            (r"\lambda'", 'layer exponent', r"A fixed constant $0<\lambda'<1$, here $1-2^{-54}$, in the cost $O(Vd^{\lambda'})$ of one simultaneous butterfly layer.", 'direct'),
        ),
        children=[s0_1(), chunk_interchange(), simultaneous_layer(), ring_convolution(), mult_algorithm(), parameter_balance()])
