from lib import *

# ---------------------------------------------------------------- Gaussian resampling (S4.1)
def gaussian_resampling():
    return show(
        'S4.1',
        r"""For coprime $s<t$ with $t/s-1>p/\alpha^4$ there are contractions $A,B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, the permutations $P_s,P_t$ staying inside the formula, computable on a line of length $t$ with error below $p^2$ in time $O(tp^{3/2+\delta}\alpha)$, and tensoring over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ at cost $O(dTp^{3/2+\delta}\alpha)$ plus $O(Tpd^2(1+\ell^\tau))$ for exposing the axes.""",
        r"""Take the exact Gaussian identity and inverse estimate of Harvey and van der Hoeven, invert $N$ by a Neumann series, rescale so $A$ and $B_0$ are contractions, keep both permutations inside the identity instead of sorting, and tensor over the axes line by line.""",
        r"""The usual implementation sorts twice on each coordinate, which would cost a full sort per axis; keeping both permutations in the formula lets the following steps absorb them.""",
        'explicit',
        mot_quote=Q(r"Its usual implementation sorts twice on each coordinate.", r"compute that formula directly."),
        page='gaussian-resampling',
        frm=['dft', 'multidim-transform', 'fixed-point-disk-grid', 'nlogn-multiplier', 'exponential-function-and-gaussian-function', 'functions-bijections-and-permutations', 'vector-norms-and-error-bounds', 'chunk-interchange'],
        adds=adds_(
            (r's', 'source length', r'The (prime) length of the vector whose Fourier transform is wanted.', 'count'),
            (r't', 'target length', r'The power-of-two length $t>s$ of the vector on which the Fourier transform is actually computed.', 'count'),
            (r'\alpha', 'Gaussian parameter', r'An integer $2\le\alpha<\sqrt p$ controlling the width of the Gaussian weights.', 'direct'),
            (r'\theta', 'relative gap', r'The excess $t/s-1$ of the target length over the source length, assumed larger than $p/\alpha^4$.', 'direct'),
            (r'A', 'expansion map', r'The linear contraction from $\mathbb C^s$ to $\mathbb C^t$ built from the Gaussian weights.', 'direct'),
            (r'B_0', 'compression map', r'The linear contraction from $\mathbb C^t$ to $\mathbb C^s$ that selects and rescales coordinates.', 'direct'),
            (r'P_s', 'source permutation', r'The coordinate permutation $(P_su)_j=u_{tj}$ of vectors of length $s$; $P_t$ is the analogous permutation $(P_tv)_k=v_{-sk}$ of vectors of length $t$.', 'direct'),
            (r'\gamma', 'scale exponent', r'The exponent $2d\alpha^2$ of the power of two by which the tensor identity is rescaled.', 'direct'),
            (r'\delta', 'multiplier slack', r'A fixed constant with $0<\delta<1/8$ in the time bounds of the cited exponential and Gaussian routines.', 'direct'),
        ),
        children=[
            infer('S4.1.1',
                  r"""With $N=C\mathsf T\mathsf D$, whose summand with index $j$ is exactly $u_j$, the exact Gaussian identity gives $\mathsf TP_sF_s=P_tF_t\mathsf S$ and $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$.""",
                  Q(r"Set $N=C\mathsf T\mathsf D$.", r"\label{eq:gaussian-public-facts} \end{equation}")),
            infer('S4.1.2',
                  r"""Since $\alpha^2<p$ and $\theta>p/\alpha^4$ we have $\alpha^2\theta>p/\alpha^2>1$, so $\|N-I\|<1/2$ and $N$ is invertible by the Neumann series.""",
                  Q(r"The first identity uses the negative Fourier sign in our definition of", r"so $N$ is invertible by the Neumann series.")),
            infer('S4.1.3',
                  r"""With $\mathsf S'=\mathsf S/2$, $\mathsf J'=N^{-1}/2$, $\mathsf D'=2^{-(2\alpha^2-2)}\mathsf D$ and $A=\mathsf S'$, $B_0=\mathsf D'\mathsf J'C$ both contractions, the left inverse $\mathsf DN^{-1}C$ of $\mathsf T$ and the normalization $2^{-2\alpha^2}$ give $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$.""",
                  Q(r"Put \[ \mathsf S'=\mathsf S/2,", r"which is \eqref{eq:no-sort-one-dimensional}.")),
            infer('S4.1.4',
                  r"""Taking $\widetilde A=\widetilde{\mathsf S}'$ and $\widetilde B_0=\widetilde{\mathsf D}'\widetilde{\mathsf J}'C$, with $C$ an ordered coordinate selection costing $O(tp)$ without error, gives errors below $16p<p^2$ and $4+3p^2/4<p^2$ and time $O(tp^{3/2+\delta}\alpha)$.""",
                  Q(r"Consequently we may take", r"The costs add to the claimed bound.")),
            infer('S4.1.5',
                  r"""The original proof sorts twice, once for $P_t$ and once for $P_s^{-1}$, each costing $O(tp\log t)$; here these permutations remain in the transform identity and the algorithms for $A$ and $B_0$ use only $C$ and the three quoted arithmetic maps.""",
                  Q(r"The original proof of Proposition~4.7(ii) implements", r"with all their original truncations.")),
            infer('S4.1.6',
                  r"""Tensoring the one-dimensional identity gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$, and $\mathcal A$ is implemented by embedding the input in the padded box with zeros and expanding the axes one at a time on the lines whose other coordinates are valid.""",
                  Q(r"Tensoring \eqref{eq:no-sort-one-dimensional} proves", r"is the one for $I\cup\{i\}$.")),
            infer('S4.1.7',
                  r"""At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$, so the cost is $\sum_{i=1}^d\frac T{t_i}O(t_ip^{3/2+\delta}\alpha)=O(dTp^{3/2+\delta}\alpha)$.""",
                  Q(r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$", r"=O(dTp^{3/2+\delta}\alpha).")),
            infer('S4.1.8',
                  r"""Moving an axis past its neighbor is an interchange of $\ell$-bit or $(\ell-1)$-bit fields costing $O(Tp(1+\ell^\tau))$, exposing and restoring one axis needs $O(d)$ of them, so all axes need $O(d^2)$ exact permutations of the padded box that change neither norms nor errors.""",
                  Q(r"The descriptor records which coordinate each physical address field", r"change neither norms nor errors.")),
            infer('S4.1.9',
                  r"""Since $t_i\ge r/2$ at most $\sum_iT/t_i\le2dT/r$ lines are invoked, so any fixed polynomial $O(p^c)$ of setup per line totals $O(dTp^c/r)=o(Tp)$ because $r$ grows faster than every fixed power of $p$.""",
                  Q(r"Since $t_i\geq r/2$, each tensor map invokes at most", r"preparing line boundaries.")),
        ])

# ---------------------------------------------------------------- chirp identity (S4.2)
def chirp_identity():
    return show(
        'S4.2',
        r"""For even $t_i$ and $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$ one has $QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}{T}$, so the frequency permutation $Q$ is absorbed into pointwise phases and a cyclic convolution with the chirp.""",
        r"""Check that $a$ has period $t_i$ in each coordinate, expand the coefficient of $u_{\boldsymbol k}$ on the right side, and use $j^2-(j-k)^2+k^2=2jk$ in each coordinate to recover the entry $\exp(2\pi i\sum_is_ij_ik_i/t_i)/T$ of $QF_{\boldsymbol t}$.""",
        r"""The factor $QF_{\boldsymbol t}$ of the resampling identity is a Fourier transform composed with a frequency permutation, and a convolution with a chirp performs the transform and the multiplication of the frequency by $-s_i$ in one cyclic convolution, so $Q$ is never applied as a separate permutation.""",
        'explicit',
        mot_quote=Q(r"The factor $QF_{\boldsymbol t}$ in", r"separate permutation of the array."),
        page='chirp-identity',
        frm=['dft', 'cyclic-convolution', 'multidim-transform', 'complex-numbers', 'exponential-function-and-gaussian-function', 'gaussian-resampling', 'modular-arithmetic'],
        children=[
            infer('S4.2.1',
                  r"""Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by $-\pi is_i(2j_i+t_i)$, an integral multiple of $2\pi i$ because $t_i$ is even, so $a$ has period $t_i$ in coordinate $i$.""",
                  Q(r"Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by", r"an integral multiple of $2\pi i$.")),
            infer('S4.2.2',
                  r"""The coefficient of $u_{\boldsymbol k}$ on the right side is $\frac1T\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}=\frac1T\exp(2\pi i\sum_is_ij_ik_i/t_i)$, precisely the coefficient in $QF_{\boldsymbol t}$ because $Q$ reads frequency $(-s_ij_i)_i$ from the negative-sign transform.""",
                  Q(r"The coefficient of $u_{\boldsymbol k}$ in the right side of", r"from the negative-sign transform.")),
        ])

# ---------------------------------------------------------------- permutation cancellation (S4.3)
def permutation_cancellation():
    return show(
        'S4.3',
        r"""With $S=\prod_is_i$, $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$: the source permutation $R$ retained by resampling cancels across the two forward transforms, their pointwise product and the opposite-sign transform, so no sort is ever executed.""",
        r"""Show $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$ from the dilation identity $F_q^+R_c=R_c^{-1}F_q^+$ for units $c$ modulo $q$, use that a coordinate permutation commutes with pointwise products, and then apply the normalized convolution rule $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$.""",
        r"""The retained permutation appears in each forward transform and in the opposite transform, so the question is whether the pointwise product in between lets the permutations meet and cancel instead of requiring a sort.""",
        'explicit',
        mot_quote=Q(r"The second identity shows how the retained source permutation", r"when computing a convolution."),
        page='permutation-cancellation',
        frm=['convolution-theorem', 'dft', 'multidim-transform', 'functions-bijections-and-permutations', 'modular-arithmetic', 'primes-coprimality-and-gcd', 'gaussian-resampling'],
        salient=r"""The permutation $R$ survives in each forward transform yet vanishes from the final result: the product of two permuted transforms, transformed back by the opposite transform with the same permutation, is the unpermuted $(u*v)/S^2$.""",
        children=[
            infer('S4.3.1',
                  r"""For a unit $c$ modulo a length $s_i$ and $(R_cz)_j=z_{cj}$, substituting $h=ck$ in the Fourier sum gives $F_{s_i}^+R_cz=R_c^{-1}F_{s_i}^+z$.""",
                  Q(r"For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$.", r"=(R_c^{-1}F_q^+z)_j.")),
            infer('S4.3.2',
                  r"""Each $t_i$ is a unit modulo $s_i$, so tensoring gives $F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$, and since a coordinate permutation commutes with pointwise products, $RF_{\boldsymbol s}^+[R(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)]=F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)$.""",
                  Q(r"Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives", r"F_{\boldsymbol s}v).")),
            infer('S4.3.3',
                  r"""By $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$ and $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$ the two normalizations give $F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=\frac1SF_{\boldsymbol s}^+F_{\boldsymbol s}(u*v)=(u*v)/S^2$, and conjugating input and output turns an algorithm for $RF_{\boldsymbol s}$ into one for $RF_{\boldsymbol s}^+$ with the same error.""",
                  Q(r"The normalized convolution rule is", r"preserves an algorithm's error bound.")),
        ])

# ---------------------------------------------------------------- sizes (S4.4)
def sizes():
    return show(
        'S4.4',
        r"""For large $n$, the sizes $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$ and axis lengths $t_i\in\{r/2,r\}$ with $\prod_it_i=T$ give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ with fixed comparison constants, and $\alpha=\lceil(12d^2b)^{1/4}\rceil$, $\gamma<28b^{2/3}$, $\eta=1/(4d)$.""",
        r"""Fix all sizes from the counted input length $n$ and check that they lie in the bands the layer and transform lemmas require, with comparison constants valid for every input length at once.""",
        r"""The earlier lemmas hold for parameters in fixed bands $a_dp^\epsilon\le d\le b_dp^\epsilon$ and $2^{a_rp/d}\le r\le2^{b_rp/d}$, so the sizes must be shown to stay in these bands for every $n$, including all choices arising at the same $p$.""",
        'explicit',
        mot_quote=Q(r"Their pointwise bounds cover every computed pair", r"arising at the same $p$."),
        frm=['floor-ceiling-and-rounding', 'logarithms-and-exponentials', 'asymptotic-notation-beyond-big-o'],
        children=[
            infer('S4.4.1',
                  r"""For large $n$, $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$; a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$; and $d\ell-\log_2T$ of the $d$ axis lengths are $r/2$, the others $r$, so $t_i\in\{r/2,r\}$, $\prod_it_i=T$ and the last axis has length $r$.""",
                  Q(r"For sufficiently large $n$, put", r"choose it as the last axis.")),
            infer('S4.4.2',
                  r"""These definitions give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$, and the bands hold with $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, $C_\ell=1$, so $r$ exceeds every fixed power of $p$, $K/\log p\to\infty$ and $\ell/K\to\infty$.""",
                  Q(r"These definitions give", r"enough bits for all work blocks.")),
            infer('S4.4.3',
                  r"""With $\alpha=\lceil(12d^2b)^{1/4}\rceil$, $\gamma=2d\alpha^2$ and $\eta=1/(4d)$ one has $\alpha\le2(12d^2b)^{1/4}$ and $\gamma<28b^{2/3}$, hence $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$, with $\gamma\le b/4$ for $b\ge2^{24}$.""",
                  Q(r"Set \[ \alpha=", r"implies $\gamma\le b/4$.")),
        ])

# ---------------------------------------------------------------- prime lengths (S4.5)
def prime_lengths():
    return show(
        'S4.5',
        r"""For the fixed sizes and $d\ge2$ axes of power-of-two lengths $t_i\in\{r/2,r\}$ there are distinct odd primes $s_i\in((1-2\eta)t_i,(1-\eta)t_i]$ with $\eta=1/(4d)$, so that $T/2<S<T$ and $\alpha^4\theta_i>p$, and they are found by deterministic trial division in $n^{o(1)}$ time.""",
        r"""Fix the sizes from $n$, apply the prime-interval lower bound of Harvey and van der Hoeven (from Rosser and Schoenfeld) to the two disjoint intervals below $r/2$ and $r$, multiply the lower bounds with Bernoulli's inequality, and search the intervals by trial division.""",
        r"""The primes must be close to the powers of two so that their product occupies a fixed fraction of the padded box, yet each ratio $t_i/s_i$ must stay separated from one for the resampling lemma.""",
        'explicit',
        mot_quote=Q(r"The distinct prime lengths $s_i$ must be close", r"enough separation for resampling."),
        page='prime-lengths',
        frm=['primes-coprimality-and-gcd', 'gaussian-resampling', 'crt-axis-map', 'logarithms-and-exponentials', 'floor-ceiling-and-rounding'],
        adds=adds_(
            (r'\alpha', 'Gaussian parameter', r'The integer $\lceil(12d^2b)^{1/4}\rceil$ controlling the width of the Gaussian weights in the resampling lemma.', 'direct'),
            (r'\gamma', 'scale exponent', r'The exponent $2d\alpha^2$ of the power of two by which the tensor resampling identity is rescaled.', 'direct'),
            (r'\eta', 'separation parameter', r'The number $1/(4d)<1/4$ fixing the intervals $((1-2\eta)t_i,(1-\eta)t_i]$ in which the primes are chosen.', 'direct'),
            (r'\theta_i', 'relative gap', r'The excess $t_i/s_i-1$ of the padded length of axis $i$ over its prime length.', 'direct'),
        ),
        salient=r"""The product $S$ of the $d$ primes is more than half of $T$ although each prime lies below its power of two by a factor $1-\eta$ with $\eta=1/(4d)$: by Bernoulli's inequality $(1-\frac1{2d})^d>\frac12$.""",
        children=[
            sizes(),
            infer('S4.5.1',
                  r"""For $0<\eta<1/4$ and $x>e^{2/\eta}$ the interval $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes.""",
                  Q(r"The prime-interval result", r"contains at least $\eta x/(2\log x)$ primes.")),
            infer('S4.5.2',
                  r"""Both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$ and have at least $x/(8d\log x)>d$ primes in their intervals, which are disjoint because $(1-\eta)r/2<(1-2\eta)r$, so distinct odd primes with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ and $\gcd(s_i,t_i)=1$ can be chosen.""",
                  Q(r"The size bounds in \eqref{eq:sizes} give", r"because $t_i$ is a power of two.")),
            infer('S4.5.3',
                  r"""Multiplying the lower bounds on $s_i$ and applying the strict Bernoulli inequality gives $S/T>(1-\frac1{2d})^d>\frac12$ for $d\ge2$, and with $s_i<t_i$ this gives $T/2<S<T$.""",
                  Q(r"Put $S=\prod_i s_i$. Multiplying the lower bounds on $s_i$", r"this gives $T/2<S<T$.")),
            infer('S4.5.4',
                  r"""Since $\theta_i=t_i/s_i-1\ge\eta/(1-\eta)>\eta$ we get $\alpha^4\theta_i>12d^2b/(4d)=3db\ge6b=p$, and $\alpha<\sqrt p$ and $t_i\le r\le T<8n/b<2^p$ hold, so every hypothesis of the resampling lemma holds for large $n$.""",
                  Q(r"Writing $\theta_i=t_i/s_i-1$, the upper bound on $s_i$ gives", r"supplies the setup condition in Lemma~\ref{lem:tensor-resampling}.")),
            infer('S4.5.5',
                  r"""The machine scans the two intervals and tests candidates by trial division, in time $O(dr^{3/2}\operatorname{poly}(p))$ whose logarithm is $O(\log p+p/d)=o(p)$, so the search takes $n^{o(1)}=o(n)$ time and nothing is advice.""",
                  Q(r"The machine finds these primes by scanning the two intervals", r"are not advice.")),
        ])

# ---------------------------------------------------------------- integer as convolution (S4.6)
def int_as_convolution():
    return infer(
        'S4.6',
        r"""With $q=\lceil n/b\rceil$ radix-$2^b$ digits per input, the product polynomial has degree at most $2q-2<2n/b\le T/2<S$, so cyclic convolution modulo $x^S-1$ has no wraparound, and every product coefficient lies in $[0,2^{3b})$.""",
        Q(r"Write the two inputs as polynomials in $2^b$, each with", r"since $q\le n\le2^b$."),
        page='int-as-convolution',
        frm=['polynomials', 'cyclic-convolution', 'positional-number-representation-and-carries', 'floor-ceiling-and-rounding'])

# ---------------------------------------------------------------- CRT axis map (S4.7)
def crt_axis_map():
    return show(
        'S4.7',
        r"""The algebra isomorphism $\Phi:\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$, $x\mapsto\prod_ix_i^{\mu_i}$ with $\mu_i=P_i^{-1}\bmod s_i$, preserves convolution and is implemented by triangular prefix-controlled cyclic shifts in time $O(Tp\,d^2(1+\ell^\tau))$.""",
        r"""Use the Chinese remainder split of Agarwal and Cooley with powers $\mu_i$ that make the new coordinate of axis $i$ depend only on lower-index digits, so the change of order is a sequence of controlled cyclic shifts.""",
        r"""The coefficient stream must be placed in the tensor order of the source arrays, and the choice of the powers $\mu_i$ is what turns that change of order into shifts the tape can do in linear time.""",
        'explicit',
        mot_quote=Q(r"The following map uses that algebraic split", r"sequence of controlled cyclic shifts."),
        page='crt-axis-map',
        frm=['cyclic-convolution', 'multidim-transform', 'controlled-shifts', 'chunk-interchange', 'modular-arithmetic', 'primes-coprimality-and-gcd', 'polynomials'],
        adds=adds_(
            (r'P_i', 'prefix product', r'The product $s_1\cdots s_{i-1}$ of the prime lengths before axis $i$.', 'count'),
            (r'\mu_i', 'inverse prefix', r'The inverse of $P_i$ modulo $s_i$.', 'direct'),
        ),
        children=[
            infer('S4.7.1',
                  r"""With $P_i=\prod_{j<i}s_j$, $\mu_i=P_i^{-1}\bmod s_i$ and $x\mapsto\prod_ix_i^{\mu_i}$, the image of $x$ has order $S$ because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all basis monomials exactly once and $\Phi$ is an isomorphism preserving cyclic convolution.""",
                  Q(r"Let $s_1,\ldots,s_d$ be the pairwise coprime", r"preserves cyclic convolution.")),
            infer('S4.7.2',
                  r"""For $k=\sum_ja_jP_j$ with $0\le a_j<s_j$ the coordinate of $\Phi(x^k)$ in axis $i$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, since terms with $j>i$ are divisible by $s_i$ and $\mu_iP_i=1$ modulo $s_i$.""",
                  Q(r"Every ordinary coefficient index has a unique mixed-radix expression", r"and $\mu_iP_i=1$ modulo $s_i$.")),
            infer('S4.7.3',
                  r"""The coefficient records are placed in the padded box $\prod_i[0,t_i)$ by one nested scan in lexicographic order, copying the next original record at each valid address and writing a zero record elsewhere, so the valid addresses occur in the original coefficient order.""",
                  Q(r"Numerical order of $k$ is lexicographic order of", r"skipping the record at each invalid address.")),
            infer('S4.7.4',
                  r"""After reordering the padded axes to $(a_1,\dots,a_d)$ the targets are updated in the order $i=d,d-1,\dots,1$, so when target $i$ is updated none of its lower-index controls has changed and the offset is computed from the original digits.""",
                  Q(r"Now reorder the complete padded axes to $(a_1,\ldots,a_d)$.", r"from the original digits $a_j$ required by the formula.")),
            infer('S4.7.5',
                  r"""On a fixed control prefix the valid target interval $[0,s_i)$ is rotated and $[s_i,t_i)$ fixed, which is a bijection of the padded box preserving the valid set and its complement, so zero padding stays zero after every step.""",
                  Q(r"To specify the action on padded addresses, let", r"Consequently zero padding remains zero after every step.")),
            infer('S4.7.6',
                  r"""Each triangular update is a prefix-controlled cyclic shift splitting the valid interval into two pieces and merging them in opposite order, with offsets costing $O(dTp^C/r)=o(Tp)$ in total, and reversing all axes uses $O(d^2)$ unequal-width moves, so $\Phi$, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$.""",
                  Q(r"Each triangular update is a prefix-controlled cyclic shift.", r"O\bigl(Tp\,d^2(1+\ell^\tau)\bigr).")),
        ])

# ---------------------------------------------------------------- negacyclic twist (S4.8.1.1)
def negacyclic_twist():
    return show(
        'S4.8.1.1',
        r"""The map $\Theta:\mathbb C[x_d]/(x_d^r-1)\to\mathcal R_r$, $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$, is an isomorphism that multiplies coefficient $k$ by $\zeta^k$, and a product term with $k+l=j+hr$ acquires the factor $\zeta^{k+l}(-1)^h=\zeta^j$, so the negative wrap of $y^r=-1$ cancels the twist.""",
        r"""Check that $\Theta$ is well defined and diagonal in the monomial bases, hence an isomorphism, and verify the wrap by computing the factor carried by a product term.""",
        r"""A cyclic convolution wraps with sign plus while the ring $\mathcal R_r$ wraps with sign minus, so the sign must be compensated by an explicit factor $\zeta^r=-1$, and the diagonal twist by $\zeta^k$ does exactly that.""",
        'explicit',
        mot_quote=Q(r"A phase twist changes the last cyclic coordinate into a polynomial", r"after the twist is removed."),
        page='negacyclic-twist',
        frm=['polynomial-ring-mod', 'cyclic-convolution', 'complex-numbers', 'fixed-point-disk-grid'],
        salient=r"""The twist by $\zeta^k$ with $\zeta^r=-1$ turns the wrap of cyclic convolution into the negative wrap of $\mathcal R_r$ and the untwist removes it again, so cyclic convolution is recovered exactly with the correct sign.""",
        children=[
            infer('S4.8.1.1.1',
                  r"""$\Theta$ is well defined since $(\zeta y)^r=(-1)(-1)=1$, and in the bases $(x_d^k)$ and $(y^k)$ it multiplies coefficient $k$ by the nonzero number $\zeta^k$, so it is an isomorphism with inverse multiplying by $\zeta^{-k}$, and both exact maps preserve the coefficient sup norm.""",
                  Q(r"Put $\mathcal R=\mathcal R_r=\mathbb C[y]/(y^r+1)$ and", r"preserve the coefficient sup norm.")),
            infer('S4.8.1.1.2',
                  r"""For $k+l=j+hr$ with $h\in\{0,1\}$ a product term after twisting and negacyclic reduction has factor $\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.""",
                  Q(r"For an explicit check on the wrap, write", r"with the correct sign.")),
        ])

# ---------------------------------------------------------------- complex convolution (S4.8.1)
def complex_convolution():
    return show(
        'S4.8.1',
        r"""Normalized cyclic convolution of complex arrays on $d$ power-of-two axes is $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=f*g/T$: twist the last axis into $\mathcal R_r$, convolve the first $d-1$ axes with the ring convolution, untwist; computed with disk-grid twist factors and truncation $Q_p$.""",
        r"""Twist the last coordinate by $\zeta^k$ to turn its cyclic wrap into the negacyclic wrap of $\mathcal R_r$, apply the ring convolution to the remaining axes, and untwist, with the twist factors approximated on the disk grid.""",
        r"""The chirp identity needs a cyclic convolution on power-of-two axes, while the synthetic transforms only convolve over the polynomial ring, so the last axis is turned into the ring by a coefficient twist.""",
        'explicit',
        mot_quote=Q(r"The power-of-two complex convolution used in the chirp identity", r"coefficient twist."),
        page='complex-convolution',
        frm=['negacyclic-twist', 'ring-convolution', 'cyclic-convolution', 'polynomial-ring-mod', 'fixed-point-disk-grid', 'nlogn-multiplier'],
        children=[
            negacyclic_twist(),
            infer('S4.8.1.2',
                  r"""With $(\iota f)_{\boldsymbol j}=\sum_kf_{\boldsymbol j,k}y^k$ and $(D_\pm f)_{\boldsymbol j,k}=\zeta^{\pm k}f_{\boldsymbol j,k}$ the linewise extension of $\Theta$ is $\iota D_+$ with inverse $D_-\iota^{-1}$, so the normalized complex cyclic convolution is $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=f*g/T$, a bilinear contraction.""",
                  Q(r"We next specify how this linewise map meets the ring-convolution", r"is also a bilinear contraction.")),
            infer('S4.8.1.3',
                  r"""The component format is the scalar format of width $w_{\rm c}=p+2$, so $\iota$ and $\iota^{-1}$ change only the shape descriptor and need no payload movement, and the transform and product headers cost $\operatorname{poly}(p)=o(Tp)$ and $O(Mp)=O(Tp)$.""",
                  Q(r"For the tape representation, use the scalar format of", r"costs $O(Mp)=O(Tp)$.")),
            infer('S4.8.1.4',
                  r"""The computed convolution twists both inputs with disk-grid approximations $\widetilde\theta^+$ of $\zeta^k$ truncated by $Q_p$, applies the ring convolution $\widetilde{\mathcal M}_r$, and untwists with $\widetilde\theta^-$ and $Q_p$, at total twist cost $O(Tp^{1+\delta})$.""",
                  Q(r"For $0\le k<r$, obtain disk-grid approximations", r"return disk-grid arrays.")),
            infer('S4.8.1.5',
                  r"""The ring-convolution output is returned after the exact scale $M$ in width $w_M=w_{\rm c}+\log_2M$, and removing only leading sign-extension bits, justified by the disk margin $\|h'\|<.701$, writes the same integers in $w_{\rm c}$ bits at cost $O(Tp)$ without any numerical truncation.""",
                  Q(r"At the $h'$ step, Proposition~\ref{prop:synthetic-convolution} returns", r"introduces no numerical truncation.")),
        ])

# ---------------------------------------------------------------- source transform (S4.8)
def source_transform():
    return show(
        'S4.8',
        r"""The procedure $\widetilde{\mathscr F}$, linewise $\widetilde{\mathcal A}$, the computed chirp transform $\widetilde{\mathscr C}$, linewise $\widetilde{\mathcal B}_0$ and an exact scale by $2^\gamma$, approximates $RF_{\boldsymbol s}$ on source tensors of norm at most $.5$ and returns disk-grid arrays.""",
        r"""Evaluate the middle factor $QF_{\boldsymbol t}$ of the Gaussian formula by the chirp identity, which needs complex cyclic convolutions of power-of-two length, each obtained from the ring convolution by a coefficient twist, and compose it with the two Gaussian maps and the exact power-of-two scale.""",
        r"""The resampling formula has three factors, the two Gaussian maps and the middle transform with its frequency permutation, and only the middle one is not already a local line map, so it is the one evaluated through the chirp identity.""",
        'recoverable',
        page='source-transform',
        frm=['gaussian-resampling', 'chirp-identity', 'complex-convolution', 'permutation-cancellation', 'fixed-point-disk-grid', 'nlogn-multiplier'],
        children=[
            complex_convolution(),
            infer('S4.8.2',
                  r"""The chirp phase numerator $-\sum_is_ij_i^2(r/t_i)\pmod{2r}$ at tensor address $\boldsymbol j$ is computed from $O(p)$-bit integers with the established multiplier in $O(dp^{1+\delta})$ per entry, so constructing the chirp costs $O(Tdp^{1+\delta})$ in total, including the descriptor scan at every coefficient.""",
                  Q(r"For the chirp array $a$ in \eqref{eq:permuted-chirp}, the phase numerator", r"cost includes the scan of the axis descriptors at every coefficient.")),
            infer('S4.8.3',
                  r"""For a disk-grid target tensor $x$ of norm at most $.6$ the computed chirp transform forms $x_0=Q_p(\overline{\widetilde a}\cdot x)$, $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$ and $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$, the exact counterpart being $QF_{\boldsymbol t}x$ by the chirp identity.""",
                  Q(r"Let $\widetilde a$ be the resulting disk-grid array, so", r"required by the computed convolution.")),
            infer('S4.8.4',
                  r"""For a source tensor of norm at most $.5$, $\widetilde{\mathscr F}$ applies $\widetilde{\mathcal A}$, then $\widetilde{\mathscr C}$, then $\widetilde{\mathcal B}_0$ and multiplies the numerators by $2^\gamma$, with exact counterpart $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, and the opposite-sign procedure is $\widetilde{\mathscr F}^+(z)=\overline{\widetilde{\mathscr F}(\overline z)}$.""",
                  Q(r"For a source disk-grid tensor of norm at most $.5$, write", r"by Lemma~\ref{lem:chirp-permutation}.")),
        ])

# ---------------------------------------------------------------- the algorithm (S4.9)
def algorithm_steps():
    return show(
        'S4.9',
        r"""The six steps place the radix-$2^b$ digits on the prime axes by $\Phi$, transform both with $\widetilde{\mathscr F}$, multiply pointwise and truncate, apply $\widetilde{\mathscr F}^+$ and scale by $S$, scale by $2^{2b+4}S$, round and apply $\Phi^{-1}$, and propagate carries; the two scalings by $S$ undo different normalizations.""",
        r"""Convert the inputs to exact grid values, run the three transforms of the convolution, and undo each normalization by an exact scaling, so that before rounding the array is exactly $2^{2b+4}(u*v)$ up to $\Phi$.""",
        r"""The source-transform procedures supply the three transforms needed for the radix-digit convolution, and the cancellation identity says what the composite of the three transforms is, from which the needed scalings follow.""",
        'explicit',
        mot_quote=Q(r"The source-transform procedures now supply the three transforms", r"for the radix-digit convolution."),
        frm=['source-transform', 'crt-axis-map', 'permutation-cancellation', 'int-as-convolution', 'fixed-point-disk-grid'],
        children=[
            infer('S4.9.1',
                  r"""Each input is read backward in groups of $b$ bits, giving the digits $a_0,\dots,a_{q-1}$, and digit $a_j$ is written as a record with real numerator $a_j2^{p-b-2}$ (value $a_j2^{-b-2}$) and zero imaginary part, with $S-q$ zero records appended, for a conversion cost $O(n+Sp)=O(Tp)$.""",
                  Q(r"Read each stored operand backward from its least significant end", r"are retained before the final group is padded.")),
            infer('S4.9.2',
                  r"""Apply $\Phi$ to get $u,v$, compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$, multiply pointwise exactly and truncate to $z$, apply $\widetilde{\mathscr F}^+(z)$ and multiply by $S$, multiply by $2^{2b+4}S$ and round, apply $\Phi^{-1}$, and propagate radix-$2^b$ carries to output exactly $2n$ bits.""",
                  Q(r"With these streams prepared, perform the following operations.", r"most-significant-first order.")),
            infer('S4.9.3',
                  r"""The exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$, and the second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution.""",
                  Q(r"The two occurrences of $S$ in this algorithm undo different normalizations.", r"carries, and output length.")),
        ])

# ---------------------------------------------------------------- exact recovery (S4.10)
def exact_recovery():
    err = show(
        'S4.10.1',
        r"""Every computed array stays in the disk and errors add along the pipeline: the ring convolution has error below $5TLh_p$, the complex convolution $6TLh_p$, the chirp transform $8TLh_p$, the source transform $E_sh_p$ with $E_s=9\,2^\gamma TL$, and the opposite-transform product gives $\widetilde w$ within $E_wh_p$ with $E_w=S(3E_s+2)<28\,2^\gamma T^2L$.""",
        r"""Insert the exact contraction at each computed input and use that a contraction does not increase an input error and that a bilinear contraction adds the errors of its two disk operands, stage by stage from the ring convolution to the scaled result.""",
        r"""A linear contraction propagates an input error without increasing it and a bilinear contraction on disk operands adds the two errors, so the errors of the successive stages can simply be added.""",
        'explicit',
        mot_quote=Q(r"A linear contraction propagates an input error without increasing it.", r"their two errors therefore add."),
        frm=['fixed-point-disk-grid', 'vector-norms-and-error-bounds', 'ring-convolution', 'complex-convolution', 'source-transform', 'permutation-cancellation'],
        adds=adds_(
            (r'h_p', 'grid step', r'The grid step $2^{-p}$; an error of $a$ means absolute error less than $ah_p$.', 'direct'),
            (r'L', 'level count', r'The base-2 logarithm $\log_2T$ of the padded box size, which bounds the number of transform rounds.', 'direct'),
            (r'E_s', 'source error', r'The error factor $9\,2^\gamma TL$ of the source transform in units of $h_p$.', 'direct'),
            (r'E_w', 'scaled error', r'The error factor $S(3E_s+2)$ of the first scaled result in units of $h_p$.', 'direct'),
        ),
        children=[
            infer('S4.10.1.1',
                  r"""Errors are counted in units $h_p=2^{-p}$ in the coefficient sup norm; a linear contraction does not increase an input error, and for a bilinear contraction $\|\mathcal M(f',g')-\mathcal M(f,g)\|\le\|f'-f\|\|g'\|+\|f\|\|g'-g\|$, so with disk operands the two errors add.""",
                  Q(r"Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this", r"their two errors therefore add.")),
            infer('S4.10.1.2',
                  r"""A computed phase product $Q_p(\widetilde ex)$ with $|\widetilde e-e|<2h_p$ has error below $(2\|x\|+\sqrt2)h_p<4h_p$ and norm at most $\|x\|$, so smaller operand norms are preserved through twists and endpoint phases.""",
                  Q(r"We also need the norm as well as the error of a computed phase product.", r"The same bounds hold coordinatewise for arrays of phases.")),
            infer('S4.10.1.3',
                  r"""For disk-grid ring arrays the three transform errors and the product truncation total less than $3L+2$ before the scale $M=T/r$, so the normalized convolution has error $E_{\rm ring}=M(3L+2)<5TL$, and with one operand of norm at most $.7$ the output has norm below $.701$, a disk-grid array without clipping.""",
                  Q(r"For disk-grid ring arrays $f,g$, put $M=T/r$.", r"without clipping the output.")),
            infer('S4.10.1.4',
                  r"""For the complex convolution the two input twist errors and the output untwist, each below $4$, plus $E_{\rm ring}$ give error below $(E_{\rm ring}+4+4+4)h_p<6TLh_p$ and norm below $.701$.""",
                  Q(r"Consider now $\widetilde{\mathcal M}_{\mathbb C}(f,g)$ for disk grid", r"<6TLh_p.")),
            infer('S4.10.1.5',
                  r"""For the chirp transform of a disk-grid input of norm at most $.6$ the kernel approximation (below $2$), the endpoint products (below $4$ each) and the convolution ($6TL$) give error below $(6TL+2+4+4)h_p<8TLh_p$ and output norm below $.701$.""",
                  Q(r"For a disk-grid chirp input $x$ with $\|x\|\le.6$", r"<8TLh_p.")),
            infer('S4.10.1.6',
                  r"""For a source input of norm at most $.5$ the expansion has error below $dp^2$, the chirp output is legal input to the compression maps, the error before the scale is below $2dp^2+8TL$, and after multiplying by $2^\gamma$ it is below $E_sh_p$ with $E_s=9\,2^\gamma TL$ and norm below $.501$; one cutoff $b\ge2^{24}$ makes all margins smaller than $10^{-3}$.""",
                  Q(r"Finally let the input to a source transform have norm at most $.5$.", r"smaller than $10^{-3}$.")),
            infer('S4.10.1.7',
                  r"""For the exact arrays $U=RF_{\boldsymbol s}u$, $V_1=RF_{\boldsymbol s}v$ of norm below $1/4$, the computed ones have norm below $.26$, $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has norm below $.5$ and error below $(2E_s+2)h_p$, and with $G=RF_{\boldsymbol s}^+$ and $G(U\cdot V_1)=(u*v)/S^2$ the opposite transform of $z$ is within $(3E_s+2)h_p$.""",
                  Q(r"The scaled radix digits in $u,v$ are exact $p$-bit grid values of norm", r"<(3E_s+2)h_p.")),
            infer('S4.10.1.8',
                  r"""Multiplying by $S$ gives $\widetilde w$ approximating $w=(u*v)/S$ within $E_wh_p$ with $E_w=S(3E_s+2)<28\,2^\gamma T^2L$, and since each coefficient of $w$ averages $S$ products, $\|w\|<1/16$ and $\|\widetilde w\|<1/16+10^{-3}<1$.""",
                  Q(r"The first exact numerator multiplication by $S$ gives", r"This proves the disk bound for the computed first scaled result.")),
        ])
    rnd = show(
        'S4.10.2',
        r"""The final error on the integer coefficients is below $448\,b\,2^{-b+\gamma}\le448\,b\,2^{-3b/4}<\frac12$, so the nearest integer to the represented real value is the unique correct coefficient, and rounding is carried out exactly in known fixed widths.""",
        r"""Multiply the error bound for $\widetilde w$ by the exact scale $2^{2b+4}S$ and convert from grid units $2^{-p}=2^{-6b}$, use $S\le T<2^b$, $L<b$ and $\gamma\le b/4$, then round the real numerators in known fixed widths.""",
        r"""The coefficients of the true convolution are integers, so an error strictly below one half identifies each of them uniquely by rounding.""",
        'explicit',
        mot_quote=Q(r"The true coefficients are real integers.", r"the unique correct coefficient."),
        frm=['floor-ceiling-and-rounding', 'dyadic-rationals-and-binary-fractions', 'positional-number-representation-and-carries'],
        children=[
            infer('S4.10.2.1',
                  r"""The unscaled coefficient array is $2^{2b+4}Sw$, so the absolute error is below $2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b}<448\,b\,2^{-b+\gamma}\le448\,b\,2^{-3b/4}<1/2$ because $S\le T<2^b$, $L<b$ and $\gamma\le b/4$, and the nearest integer to $H_j/2^p$ is the unique correct coefficient.""",
                  Q(r"In tensor order, the unscaled integer coefficient array is", r"the unique correct coefficient.")),
            infer('S4.10.2.2',
                  r"""A signed $w_0$-bit integer times $S<2^b$ fits in signed width $w_0+b$, so the exact products by $S$ and the shift by $2^{2b+4}$ are written in the known widths $w_{\rm c}+b$, $w_{\rm c}+2b$ and $w_{\rm c}+4b+4$, all $O(p)$ because $p=6b$.""",
                  Q(r"These exact operations use known fixed record widths.", r"$O(p)$ because $p=6b$.")),
            infer('S4.10.2.3',
                  r"""Rounding recovers the real magnitude, inspects its low $p$ bits and applies the rounding carry with the sign restored, giving a coefficient in $[0,2^{3b})$ by the capacity bound, written as a signed $(3b+1)$-bit word, with zero words at padded addresses, so $\Phi^{-1}$ receives a stream of known fixed-length records.""",
                  Q(r"The established integer multiplier performs the two products by $S$ in", r"so the address routine receives a stream of known fixed-length records.")),
        ])
    car = show(
        'S4.10.3',
        r"""The carry recurrence $d_j=(c_j+k_j)\bmod2^b$, $k_{j+1}=\lfloor(c_j+k_j)/2^b\rfloor$ keeps $0\le k_j\le q(2^b-1)<2^{2b}$ and, by the invariant $\sum_{h<j}c_h2^{bh}=\sum_{h<j}d_h2^{bh}+k_j2^{bj}$, outputs exactly the $2n$ bits of the product.""",
        r"""Propagate carries from the least significant coefficient with the recurrence, prove the carry bound by induction, use the invariant to show the digits are those of the product, and drop only the zero bits above position $2n-1$.""",
        r"""The recovered coefficients $c_j$ can be as large as $2^{3b}$, larger than a radix-$2^b$ digit, so carries must be propagated to turn the coefficient list into the binary digits of the product.""",
        'recoverable',
        frm=['positional-number-representation-and-carries', 'proof-by-induction-and-recursion', 'int-as-convolution'],
        children=[
            infer('S4.10.3.1',
                  r"""With $Q_0=2^b$, $k_0=0$ and $d_j=(c_j+k_j)\bmod Q_0$, $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$, induction gives $0\le k_j\le q(Q_0-1)<Q_0^2$ since $c_j+k_j\le qQ_0(Q_0-1)$, and the relation $c_j+k_j=d_j+Q_0k_{j+1}$ gives the exact invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$.""",
                  Q(r"To propagate carries, let $Q_0=2^b$.", r"the carry from the processed coefficients into the remaining positions.")),
            infer('S4.10.3.2',
                  r"""The coefficients occur in increasing index after $\Phi^{-1}$, so the carry scan runs from least to most significant with $O(b)$ bits and steps per coefficient, the stream of length $O(Sb)=O(Tp)$ is reversed once, and since the product is less than $2^{2n}$ only zero padding bits above position $2n-1$ are removed, leading zeros being kept to give exactly $2n$ bits.""",
                  Q(r"After $\Phi^{-1}$ the coefficients occur in increasing ordinary index,", r"Zero inputs obey the same invariant and output rule.")),
        ])
    return show(
        'S4.10',
        r"""The recovered coefficient error is below $1/2$, so rounding returns the integer convolution coefficients exactly, and propagating radix-$2^b$ carries outputs exactly the $2n$ product bits.""",
        r"""Bound the error of every computed stage by inserting exact contractions, add the errors along the pipeline to show the final error is below $1/2$, round to the integer coefficients, and propagate carries.""",
        r"""The algorithm computes with truncated fixed-point complex numbers, so exactness of the output rests on showing that all errors together stay below the half-integer margin at which rounding is unique.""",
        'recoverable',
        page='exact-recovery',
        frm=['int-as-convolution', 'fixed-point-disk-grid', 'vector-norms-and-error-bounds', 'floor-ceiling-and-rounding', 'positional-number-representation-and-carries', 'ring-convolution', 'source-transform', 'permutation-cancellation'],
        salient=r"""A working precision of only $p=6b$ fractional bits suffices although the pipeline amplifies errors by $2^{2b+4}S\cdot28\,2^\gamma T^2L$: the factors $S\,T^2<2^{3b}$ and $L<b$ cost about $3b$ bits and the scale $2^{2b+4}$ another $2b+4$, so with $\gamma\le b/4$ the error is below $448\,b\,2^{-b+\gamma}\le448\,b\,2^{-3b/4}$.""",
        children=[err, rnd, car])

# ---------------------------------------------------------------- mult-algorithm (S4)
def mult_algorithm():
    return show(
        'S4',
        r"""The algorithm — radix-$2^b$ digits placed on distinct prime axes by $\Phi$, source transforms of both operands, pointwise product, opposite-sign transform with the scalings $S$ and $2^{2b+4}S$, rounding, $\Phi^{-1}$ and carries — outputs exactly the $2n$-bit product.""",
        r"""Reduce the product to a cyclic convolution of digit lists on distinct prime axes, evaluate it by source transforms, a pointwise product and an opposite transform in which $R$ cancels, show the errors stay below $1/2$, and round and carry.""",
        r"""The fast procedures only pay off inside a multiplication reduction, so the reduction chain digits, prime axes, power-of-two axes, polynomial ring has to be followed down, with every change of representation accounted for, and the errors summed back up.""",
        'recoverable',
        page='mult-algorithm',
        frm=['int-as-convolution', 'crt-axis-map', 'source-transform', 'permutation-cancellation', 'exact-recovery', 'prime-lengths', 'gaussian-resampling', 'chirp-identity', 'complex-convolution', 'ring-convolution', 'fixed-point-disk-grid', 'cyclic-convolution', 'convolution-theorem', 'dft', 'multidim-transform', 'positional-number-representation-and-carries', 'nlogn-multiplier'],
        adds=adds_(
            (r'b', 'radix exponent', r'The inputs are written in radix $2^b$ with $b=\lceil\log_2n\rceil$.', 'count'),
            (r'q', 'digit count', r'The number $\lceil n/b\rceil$ of radix-$2^b$ digits of each input.', 'count'),
            (r'T', 'padded box size', r'The power of two in $[4n/b,8n/b)$ that is the number of entries of the padded array.', 'count'),
            (r'\ell', 'ring exponent', r'The base-2 logarithm of $r$, so $r=2^\ell$.', 'direct'),
            (r't_i', 'padded axis length', r'The power of two $r/2$ or $r$ that is the padded length of axis $i$, with $\prod_it_i=T$.', 'count'),
            (r's_i', 'prime length', r'The distinct odd prime length of source axis $i$, just below $t_i$.', 'count'),
            (r'S', 'source length', r'The product $\prod_is_i$ of the prime lengths, with $T/2<S<T$.', 'count'),
            (r'\Phi', 'coefficient-address map', r'The algebra isomorphism sending $x$ to $\prod_ix_i^{\mu_i}$, which places the coefficient list on the prime cyclic axes.', 'direct'),
            (r'R', 'source permutation', r'The coordinate permutation $\bigotimes_iP_{s_i}$ retained from Gaussian resampling.', 'direct'),
            (r'Q', 'target permutation', r'The coordinate permutation $\bigotimes_iP_{t_i}$ retained from Gaussian resampling.', 'direct'),
        ),
        salient=r"""The algorithm computes with approximate fixed-point complex arithmetic and truncations, yet outputs the exact integer product, because all accumulated errors are shown to stay below $1/2$ at the integer coefficients, where rounding is unique.""",
        children=[gaussian_resampling(), chirp_identity(), permutation_cancellation(), prime_lengths(), int_as_convolution(), crt_axis_map(), source_transform(), algorithm_steps(), exact_recovery()])
