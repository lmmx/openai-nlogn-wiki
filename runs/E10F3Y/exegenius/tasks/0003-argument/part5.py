from lib import *

# ---------------------------------------------------------------- S3 resampling
s31 = show(
    "S3.1",
    r"For coprime integers $2\le s<t<2^p$ and $2\le\alpha<\sqrt p$ with $\theta=t/s-1>p/\alpha^4$, and $(P_su)_j=u_{tj}$, $(P_tv)_k=v_{-sk}$, there are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, and approximations of $A,B_0$ with error below $p^2$ run in time $O(tp^{3/2+\delta}\alpha)$ for fixed $0<\delta<1/8$.",
    r"Take the Harvey-van der Hoeven Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$ and the estimate $\|N-I\|<2^{-\alpha^2\theta}$ for $N=C\mathsf T\mathsf D$; invert $N$ by a Neumann series, normalize $A=\mathsf S/2$ and $B_0=\mathsf D'\mathsf J'C$ with $\mathsf J'=N^{-1}/2$, $\mathsf D'=2^{-(2\alpha^2-2)}\mathsf D$, and keep $P_s$ and $P_t$ in the identity instead of sorting.",
    mot("Their original proof implements $B$ with two label-and-sort operations for $P_t$ and $P_s^{-1}$; here these permutations remain in the transform identity.", "explicit",
        r"In \eqref{eq:no-sort-one-dimensional} these permutations remain in the"),
    [
        infer("S3.1a",
              r"The Gaussian maps are $(\mathsf Su)_k=\frac1\alpha\sum_je^{-\pi\alpha^{-2}(j-sk/t)^2}u_j$ and $(\mathsf Tu)_k=\sum_je^{-\pi\alpha^2(tj/s-k)^2}u_j$; with $q_j=\lfloor tj/s+\frac12\rfloor$, $\beta_j=tj/s-q_j$, the selection $(Cv)_j=v_{q_j}$ and the diagonal $(\mathsf Du)_j=e^{\pi\alpha^2\beta_j^2}u_j$, the diagonal of $N=C\mathsf T\mathsf D$ is exactly $1$ and the rest is $N-I$.",
              r"Set $N=C\mathsf T\mathsf D$. In $(Nu)_j$, the summand with index $j$"),
        infer("S3.1b",
              r"By Harvey and van der Hoeven's Theorem 4.2 and Lemma 4.6, $\mathsf TP_sF_s=P_tF_t\mathsf S$ and $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$; since $\alpha^2<p$ and $\theta>p/\alpha^4$ we get $\alpha^2\theta>p/\alpha^2>1$, so $\|N-I\|<1/2$ and $N$ is invertible by the Neumann series.",
              r"Thus $\|N-I\|<1/2$, so $N$ is invertible"),
        infer("S3.1c",
              r"With $\mathsf S'=\mathsf S/2$, $\mathsf J'=N^{-1}/2$ and $\mathsf D'=2^{-(2\alpha^2-2)}\mathsf D$ one has $\|\mathsf S'\|<\frac34$, $\|\mathsf J'\|<\frac78$, $\|\mathsf D'\|<1$ (Proposition 4.7(i)), so $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$ are contractions as $\|C\|=1$.",
              r"The proof of Proposition~4.7(i) in the cited paper gives"),
        infer("S3.1d",
              r"Since $C\mathsf T=N\mathsf D^{-1}$, $(\mathsf DN^{-1}C)\mathsf T=I$, so applying this left inverse to the Gaussian identity gives $\mathsf DN^{-1}CP_tF_t\mathsf S=P_sF_s$; the normalizations multiply to $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$, hence $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$.",
              r"$2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$. Hence"),
        infer("S3.1e",
              r"The ordered numerical maps of Lemmas 4.8, 4.9 and 4.12 give errors $16p$ for $\widetilde{\mathsf S}'$, $3p^2/4$ for $\widetilde{\mathsf J}'$ and $4$ for $\widetilde{\mathsf D}'$, with times $O(tp^{3/2+\delta}\alpha)$, $O(tp^{3/2+\delta}\alpha)$ and $O(tp^{1+\delta})$.",
              r"\widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)\\"),
        infer("S3.1f",
              r"$C$ selects an ordered subsequence ($q_0=0$, $q_{s-1}<t$, $q_{j+1}>q_j$ since $t/s>1$) generated with $O(p)$ work per index by maintaining $tj=sf_j+e_j$ with $0\le e_j<s$, $q_j=f_j+\mathbf 1_{2e_j\ge s}$ and the carry $c_j=\mathbf 1_{e_j+\rho\ge s}$; so $C$ is exact and costs $O(tp)$, and with $\widetilde A=\widetilde{\mathsf S}'$, $\widetilde B_0=\widetilde{\mathsf D}'\widetilde{\mathsf J}'C$ the errors are below $16p<p^2$ and $4+3p^2/4<p^2$.",
              r"For $C$, observe that $q_0=0$, $q_{s-1}<t$, and $q_{j+1}>q_j$,"),
        infer("S3.1g",
              r"The Neumann evaluation $\widetilde{\mathsf J}'u=\sum_{j<k}(-1)^j\widetilde v^{(j)}$ with $k=\lceil p/(\alpha^2\theta)\rceil\le\alpha^2+1$ terms, each iterate $\widetilde E=\widetilde N-I$ kept in $\mathbb D_p$ (norm below $0.42\|z\|+(p/3)2^{-p}<1$) and windows of radius $\lceil\sqrt p/(2\alpha)\rceil$, costs $O((\alpha^2+1)tp(1+\sqrt p/\alpha))=O(tp\sqrt p\,\alpha)$ using $2\le\alpha<\sqrt p$.",
              r"O\bigl((\alpha^2+1)tp(1+\sqrt p/\alpha)\bigr)"),
    ],
    page="gaussian-resampling",
    frm=["dft", "contraction-error", "hh-multiplier", "vector-norms-and-the-triangle-inequality", "fixed-point-numbers-dyadic-rationals-and-rounding", "complex-numbers", "primes-coprimality-and-the-extended-euclidean-algorithm"],
    adds=[
        add(r"s", "source length", "The prime length of a source axis, $2\\le s<t$.", "count"),
        add(r"t", "target length", "The power-of-two length of the corresponding padded axis, coprime to $s$.", "count"),
        add(r"\alpha", "Gaussian width", "The integer $2\\le\\alpha<\\sqrt p$ controlling the width of the Gaussian window; the algorithm takes $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$.", "direct"),
        add(r"\theta", "length gap", "The ratio gap $t/s-1$, required to exceed $p/\\alpha^4$.", "direct"),
        add(r"\delta", "multiplication exponent", "The fixed exponent $0<\\delta<1/8$ in the cost $O(\\max(p,\\log k)^{1+\\delta})$ of the cited exponential routine; the parameter choice takes $\\delta=1/16$.", "direct"),
        add(r"P_s", "source permutation", "The coordinate permutation $(P_su)_j=u_{tj}$ of $\\mathbb C^s$.", "direct"),
        add(r"P_t", "target permutation", "The coordinate permutation $(P_tv)_k=v_{-sk}$ of $\\mathbb C^t$.", "direct"),
        add(r"A", "expansion contraction", "The linear contraction $\\mathbb C^s\\to\\mathbb C^t$ equal to $\\mathsf S/2$ with $\\mathsf S$ the Gaussian resampling map.", "direct"),
        add(r"B_0", "compression contraction", "The linear contraction $\\mathbb C^t\\to\\mathbb C^s$ equal to $\\mathsf D'\\mathsf J'C$.", "direct"),
    ],
    salient=r"The identity carries the factor $2^{2\alpha^2}$ explicitly: normalizing both Gaussian maps into contractions costs a known power of two, and it is this scale that later forces the guard $\gamma=2d\alpha^2=o(b)$ bits.")

s32 = show(
    "S3.2",
    r"Tensoring over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$; the linewise implementations have error below $dp^2$ and total time $O(dTp^{3/2+\delta}\alpha)$, and exposing and restoring all lines of the padded box costs $O(Tpd^2(1+\ell^\tau))$.",
    r"Apply the one-dimensional maps along one axis at a time on the full padded box (zero outside the valid coordinates), bring each axis in turn to the innermost position by adjacent equal-width chunk swaps, and sum the line costs over axes.",
    mot("Each axis map acts independently on its valid lines and is zero on the others, so its norm and error are those of the one-dimensional map and the errors of the $d$ axes add.", "recoverable"),
    [
        infer("S3.2a",
              r"Tensoring the one-dimensional identity gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $R=\bigotimes P_{s_i}$, $Q=\bigotimes P_{t_i}$ and $\gamma=2d\alpha^2$; expansion and compression are done axis by axis in the padded box, the max over lines gives a contraction per axis and error below $p^2$, hence below $dp^2$ for $d$ axes.",
              r"Tensoring \eqref{eq:no-sort-one-dimensional} proves"),
        infer("S3.2b",
              r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$, so the cost is $\sum_{i=1}^d\frac T{t_i}O(t_ip^{3/2+\delta}\alpha)=O(dTp^{3/2+\delta}\alpha)$.",
              r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$,"),
        infer("S3.2c",
              r"Exposing an axis needs $O(d)$ adjacent interchanges of $\ell$- or $(\ell-1)$-bit fields (for unequal widths the leading bit of the longer is moved out, the equal parts swapped, then the bit moved back), each $O(Tp(1+\ell^\tau))$, so exposing and restoring all axes costs $O(Tpd^2(1+\ell^\tau))$; since $t_i\ge r/2$ any fixed polynomial in $p$ of setup per line totals $O(dTp^c/r)=o(Tp)$.",
              r"$O(d)$ adjacent interchanges, hence all axes need $O(d^2)$. These are"),
    ],
    frm=["multidimensional-transform", "chunk-interchange", "gaussian-resampling", "tape-stream-operations", "contraction-error"],
    adds=[
        add(r"R", "source permutation tensor", "The tensor product $\\bigotimes_iP_{s_i}$ of the source coordinate permutations.", "direct"),
        add(r"Q", "target permutation tensor", "The tensor product $\\bigotimes_iP_{t_i}$ of the target coordinate permutations.", "direct"),
        add(r"\gamma", "resampling scale", "The exponent $2d\\alpha^2$ of the power of two by which the tensor resampling identity is scaled.", "count"),
    ])

s33 = infer(
    "S3.3",
    r"For even $t_i$ and $a_{\boldsymbol j}=\exp\bigl(-\pi i\sum_is_ij_i^2/t_i\bigr)$, which has period $t_i$ in coordinate $i$, Bluestein's identity gives $QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}T$: the coefficient of $u_{\boldsymbol k}$ is $\frac1T\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}=\frac1T\exp(2\pi i\sum_is_ij_ik_i/t_i)$, exactly the entry of $QF_{\boldsymbol t}$ since $Q$ reads frequency $(-s_ij_i)_i$ of the negative-sign transform.",
    r"The coefficient of $u_{\boldsymbol k}$ in the right side of",
    frm=["chirp-identity", "dft", "cyclic-convolution", "multidimensional-transform"])

s34 = show(
    "S3.4",
    r"The retained source permutation $R$ cancels: $(RF_{\boldsymbol s}^+)\bigl[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)\bigr]=\frac{u*v}{S^2}$ with $S=\prod_is_i$, so no sort is executed for $R$.",
    r"Show that dilation by a unit commutes through the opposite transform so that $RF^+R=F^+$, that pointwise products commute with the permutation $R$, and then apply the convolution theorem.",
    mot("A coordinate permutation commutes with pointwise products and, for a unit dilation, conjugates the opposite Fourier transform into its inverse dilation, so the two copies of $R$ meet and cancel.", "recoverable"),
    [
        infer("S3.4a",
              r"For a unit $c$ modulo $q$ and $(R_cz)_j=z_{cj}$, substituting $h=ck$ gives $(F_q^+R_cz)_j=(R_c^{-1}F_q^+z)_j$; each $t_i$ is a unit modulo $s_i$, so tensoring gives $F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$, hence $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$, and $(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)=R(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)$.",
              r"Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives"),
        infer("S3.4b",
              r"With $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$ and $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$, $F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=\frac1SF_{\boldsymbol s}^+F_{\boldsymbol s}(u*v)=\frac{u*v}{S^2}$; conjugating input and output of an algorithm for $RF_{\boldsymbol s}$ gives one for $RF_{\boldsymbol s}^+$ with the same error and disk guarantee.",
              r"The normalized convolution rule is"),
    ],
    frm=["dft", "cyclic-convolution", "multidimensional-transform", "modular-arithmetic", "permutations-bijections-and-permutation-matrices"],
    adds=[
        add(r"S", "source length product", "The product $\\prod_is_i$ of the pairwise coprime prime source lengths.", "count"),
    ])

s3 = show(
    "S3",
    r"The Fourier transforms of prime-product length needed for the digit convolution are reduced to power-of-two tensor transforms without executing full sorts: $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$, the target permutation $Q$ is absorbed by a chirp convolution, and the source permutation $R$ cancels across two forward transforms, a pointwise product and an opposite-sign transform.",
    r"Use Gaussian resampling with both coordinate permutations kept in the identity, apply it axis by axis on the padded box, evaluate the middle factor $QF_{\boldsymbol t}$ by Bluestein's chirp identity as a cyclic convolution with two pointwise phase multiplications, and let $R$ cancel by $RF^+R=F^+$ and the convolution theorem.",
    mot("Its usual implementation sorts twice on each coordinate; retaining both permutations in the transform formula and computing that formula directly avoids the sorts, which would cost $O(tp\\log t)$ per line.", "explicit",
        r"Its usual implementation sorts twice on each"),
    [s31, s32, s33, s34],
    page="permutation-cancellation",
    frm=["gaussian-resampling", "chirp-identity", "multidimensional-transform", "dft", "cyclic-convolution", "chunk-interchange", "synthetic-transform", "ring-convolution" if False else "dft"],
    salient=r"Neither the source permutation $R$ nor the target permutation $Q$ is ever applied to the data: $Q$ disappears into the chirp identity, and $R$ cancels because the same permutation sits on both forward transforms and on the opposite one.")

# ---------------------------------------------------------------- S4 parameter choice
s44 = show(
    "S4.4",
    r"One can choose distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$, so that $\gcd(s_i,t_i)=1$, $T/2<S<T$, $\alpha^4\theta_i>p$ for $\theta_i=t_i/s_i-1$, all hypotheses of the resampling lemma hold, and a deterministic search finds them in $n^{o(1)}$ time.",
    r"Use the prime-interval lemma of Harvey and van der Hoeven (based on Rosser-Schoenfeld) in the two disjoint intervals below $r/2$ and below $r$, check that each has more than $d$ primes, then bound the product $S/T$ by Bernoulli's inequality and the gaps $\theta_i$ from the upper end of the interval.",
    mot("The primes must lie close to the powers of two so their product fills a fixed fraction of the padded box, while each ratio $t_i/s_i$ must leave enough room for resampling.", "explicit",
        r"The distinct prime lengths $s_i$ must be close to the powers of two"),
    [
        infer("S4.4a",
              r"For $0<\eta<1/4$ and $x>e^{2/\eta}$ the interval $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes (Harvey-van der Hoeven Lemma 5.1, from Rosser-Schoenfeld).",
              r"contains at least $\eta x/(2\log x)$ primes."),
        infer("S4.4b",
              r"With $\eta=1/(4d)$ both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$ because $\log(r/2)/d=\Theta(p^{1-2\epsilon})\to\infty$; the bound is $x/(8d\log x)>d$ since $\log x=\Theta(p^{1-\epsilon})$ while $\log(8d^2\log x)=O(\log p)=o(\log x)$.",
              r"Thus both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$."),
        infer("S4.4c",
              r"The two intervals are disjoint because $(1-\eta)r/2<(1-2\eta)r$ for $\eta<1/4$, so $d$ distinct odd primes with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ exist; every $\gcd(s_i,t_i)=1$ because $t_i$ is a power of two.",
              r"The two intervals are disjoint because"),
        infer("S4.4d",
              r"Multiplying the lower bounds and applying strict Bernoulli gives $S/T>(1-\frac1{2d})^d>\frac12$ for $d\ge2$, and $s_i<t_i$ gives $S<T$, so $T/2<S<T$.",
              r"applying strict Bernoulli inequality gives"),
        infer("S4.4e",
              r"The upper bound on $s_i$ gives $\theta_i=t_i/s_i-1\ge\eta/(1-\eta)>\eta$, hence $\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\ge6b=p$; also $2\le\alpha<\sqrt p$ and $t_i\le r\le T<8n/b<2^{6b}=2^p$, so Lemma resampling applies.",
              r"Writing $\theta_i=t_i/s_i-1$, the upper bound on $s_i$ gives"),
        infer("S4.4f",
              r"The machine scans the two intervals and tests each candidate by trial division through its square root, in time $O(dr^{3/2}\mathrm{poly}(p))$ whose logarithm is $O(\log p+p/d)=o(p)$, i.e. $n^{o(1)}=o(n)$; all primes and parameters are generated by the machine, not given as advice.",
              r"The machine finds these primes by scanning the two intervals"),
    ],
    page="prime-axis-lengths",
    frm=["gaussian-resampling", "primes-coprimality-and-the-extended-euclidean-algorithm", "logarithms-exponentials-floors-and-ceilings", "limits-and-limit-inferior", "finite-sets-subsets-and-counting"],
    adds=[
        add(r"s_i", "prime axis length", "The $i$th chosen odd prime, $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$, the length of the $i$th source axis.", "count"),
        add(r"S", "prime product", "The product $\\prod_{i=1}^ds_i$, the length of the cyclic convolution being computed.", "count"),
    ],
    salient=r"The product of the primes still fills more than half of the padded box, $T/2<S<T$, although each prime has been pushed below its power of two by a factor $1-\eta$ with $\eta=1/(4d)$: $d$ factors of size $1-\frac1{2d}$ cost at most a factor $\frac12$ in total.")

s43 = show(
    "S4.3",
    r"The sizes are $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$, $r=2^\ell$ with $\ell=\lceil(\log_2T)/d\rceil$, and axis lengths $t_i\in\{r/2,r\}$ with $\prod t_i=T$ and $t_d=r$; they satisfy $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $\alpha=\lceil(12d^2b)^{1/4}\rceil$ with $\gamma=o(b)$.",
    r"Compute the sizes from $n$ with exact integer comparisons for the fixed rational powers, and verify the stated comparison bands and the growth conditions required by the layer, transform and resampling lemmas.",
    mot("The tape lemmas are stated for families of parameters in fixed comparison bands, so the sizes must be shown to stay in those bands for every large input length at once.", "recoverable"),
    [
        infer("S4.3a",
              r"Take the power of two $T$ in $[4n/b,8n/b)$ and $r=2^{\lceil(\log_2T)/d\rceil}$; then $d\ell-\log_2T$ is an integer in $[0,d)$, so choose that many of the $d$ axis lengths to be $r/2$ and the others $r$, with the last axis of length $r$, giving $t_i\in\{r/2,r\}$, $\prod_it_i=T$ and $t_d=r$.",
              r"Take the power of two $T$ in $[4n/b,8n/b)$, and let"),
        infer("S4.3b",
              r"These give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$.",
              r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad"),
        infer("S4.3c",
              r"For large $b$, $b/2\le\log_2T\le b$ gives $\frac1{12}p^\epsilon\le d\le p^\epsilon$ and $\frac p{12d}\le\ell\le\frac p{3d}$, so one fixes $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$ and $C_\ell=1$; in particular $r$ exceeds every fixed power of $p$, $K/\log p\to\infty$ and $\ell/K\to\infty$.",
              r"Thus we fix $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, and $C_\ell=1$"),
        infer("S4.3d",
              r"With $\alpha=\lceil(12d^2b)^{1/4}\rceil$, $\gamma=2d\alpha^2$ and $\eta=1/(4d)$ one has $\alpha\le2(12d^2b)^{1/4}$ and $\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}$, so $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$ (e.g. $\gamma\le b/4$ for $b\ge2^{24}$).",
              r"\alpha=\left\lceil(12d^2b)^{1/4}\right\rceil,"),
    ])

s45 = infer(
    "S4.5",
    r"Writing the inputs as polynomials in $2^b$ with $q=\lceil n/b\rceil$ digits each, the product has degree at most $2q-2<2n/b\le T/2<S$, so convolution modulo $x^S-1$ has no wraparound, and every product coefficient satisfies $0\le c_j\le q(2^b-1)^2<2^{3b}$ since $q\le n\le2^b$.",
    r"Write the two inputs as polynomials in $2^b$, each with",
    frm=["radix-digit-convolution", "positional-number-systems-and-carries", "convolution-of-sequences"])

s4 = show(
    "S4",
    r"Conservative fixed rational exponents and sizes make every hypothesis of the tape, transform and resampling lemmas hold for all large $n$: $\tau=\sigma=1-2^{-50}$, $\beta=\frac12$, $\delta=\frac1{16}$, $\lambda=1-2^{-52}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $C_1=20$, $\epsilon=2^{-75}$, $\kappa=2^{-182}$, with sizes $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, $Tp=\Theta(n)$, axis lengths $t_i$ and primes $s_i<t_i$.",
    r"Fix the exponents by exact rational comparisons so that all strict inequalities between them hold with room to spare, derive the sizes and their comparison bands from $n$, and select prime axis lengths slightly below the powers of two.",
    mot("These constants are deliberately conservative and no optimization is claimed, so every inequality needed later can be checked by direct substitution.", "explicit",
        r"These constants are deliberately conservative; no optimization is claimed."),
    [
        infer("S4.1",
              r"The fixed rational numbers are $\tau=\sigma=1-2^{-50}$, $\beta=\frac12$, $\delta=\frac1{16}$, $\lambda=1-2^{-52}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$.",
              r"\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\"),
        infer("S4.2",
              r"The layer conditions hold with room to spare: $\max\{\tau,\sigma\}<\lambda<1$, $\tau(1+c/\beta)<1-31\cdot2^{-55}<\lambda$ and $\sigma+\beta(1-\sigma)=1-2^{-51}<\lambda<\lambda'<1$, and the dimension exponent satisfies $\epsilon<\frac1{12}$, $\epsilon C_1<1$, $\epsilon(2-\tau)<1-\tau$, $\frac34+\delta+\frac32\epsilon<1$, $\epsilon(1+c)<1$, $\epsilon+\delta<1$.",
              r"The layer conditions hold with room to spare:"),
        s43,
        s44,
        s45,
    ],
    page="parameter-choice",
    frm=["prime-axis-lengths", "gaussian-resampling", "transform-layout", "simultaneous-butterfly-layer", "rank-saving", "chunk-interchange", "radix-digit-convolution", "logarithms-exponentials-floors-and-ceilings", "limits-and-limit-inferior"],
    adds=[
        add(r"b", "digit size", "The radix exponent $\\lceil\\log_2n\\rceil$: the integers are split into digits of $b$ bits.", "count"),
        add(r"\alpha", "Gaussian width", "The integer $\\lceil(12d^2b)^{1/4}\\rceil$ used in every resampling line, with $2\\le\\alpha<\\sqrt p$.", "direct"),
        add(r"\gamma", "resampling scale exponent", "The integer $2d\\alpha^2<28b^{2/3}$ by which the source transform is scaled by $2^\\gamma$.", "count"),
        add(r"\eta", "prime gap fraction", "The fraction $1/(4d)$ below the power of two $t_i$ within which the prime $s_i$ is chosen.", "direct"),
    ],
    salient=r"All the exponents are astronomically close to $1$ or $0$ ($\tau=1-2^{-50}$, $c=2^{-56}$, $\epsilon=2^{-75}$), yet every constraint among them holds; the final saving $\kappa=2^{-182}$ is a product of three such tiny numbers, $2\kappa=\epsilon c(1-\tau)$.")
