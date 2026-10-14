from lib import *
from build3 import *

# ---------------- root children: R1, R2a, R2b ----------------
R1 = inf("R1",
  r"Writing each $n$-bit integer as a polynomial in $2^b$ with small digit coefficients turns the product into a convolution of the two digit lists, with carries propagated afterwards.",
  76, "Splitting the inputs into radix digits reduces multiplication to",
  page="convolution-multiplication",
  frm=["radix-representation-and-carry-propagation", "polynomials", "divide-and-conquer-multiplication"])
R2a = inf("R2a",
  r"On a fixed number of tapes, splitting, merging, digit moves and row splits on a stream of volume $V$ cost $O(V)$ steps.",
  494, "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
  page="multitape-streams",
  frm=["turing-machines", "polynomial-time-and-computational-cost-on-tapes", "cartesian-products-and-lexicographic-order", "big-o"])
R2b = inf("R2b",
  r"A target field following its control fields can be shifted cyclically by an offset computed from them, or multiplied by a unit modulo $q^b$, in $O(V)$ time.",
  566, "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
  page="controlled-shifts",
  frm=["multitape-streams", "modular-arithmetic-and-congruences", "primes-coprimality-and-gcd", "euclidean-algorithm-and-modular-inverses"])

# ---------------- F1 parameter choice ----------------
F1 = show("F1",
  r"For input length $n$, the parameters $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T$ near $4n/b$ split into $d$ axis lengths $t_i\in\{r/2,r\}$, and distinct odd primes $s_i$ just below $t_i$ with $T/2<S<T$, satisfy every hypothesis of the resampling, layout and layer lemmas.",
  "Fix rational exponents once, derive size bounds from them, and obtain primes in the intervals $((1-2\\eta)t_i,(1-\\eta)t_i]$ from the prime-interval lemma, then check the resampling hypotheses.",
  "The product of the prime lengths must fill a fixed fraction of the padded box while each ratio $t_i/s_i$ stays at least $1+\\eta$, so both sides of the interval $(1-2\\eta,1-\\eta)$ matter.",
  "explicit",
  [
    inf("F1.1", r"Put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $K=\lfloor d^c\rfloor$.",
        4055, r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,", frm=["logarithms-floor-and-ceiling"]),
    inf("F1.2", r"Take the power of two $T$ in $[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$, and $d\ell-\log_2T$ axis lengths $r/2$ and the rest $r$, so $t_i\in\{r/2,r\}$, $\prod_it_i=T$ and $t_d=r$.",
        4063, r"t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r."),
    inf("F1.3", r"These give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$.",
        4069, r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad"),
    inf("F1.4", r"The prime-interval lemma gives, for $0<\eta<1/4$ and $x>e^{2/\eta}$, at least $\eta x/(2\log x)$ primes $q$ with $(1-2\eta)x<q\le(1-\eta)x$.",
        4116, r"(1-2\eta)x<q\leq(1-\eta)x", frm=["primes-coprimality-and-gcd"]),
    inf("F1.5", r"For $\eta=1/(4d)$ and $x=r/2$ or $r$ the number of such primes exceeds $d$, so distinct odd primes with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ exist and $\gcd(s_i,t_i)=1$.",
        4135, r"(1-2\eta)t_i<s_i\leq(1-\eta)t_i."),
    inf("F1.6", r"Multiplying the lower bounds with strict Bernoulli gives $S/T>(1-1/(2d))^d>1/2$.",
        4142, r"\left(1-\frac1{2d}\right)^d>\frac12"),
    inf("F1.7", r"Together with $s_i<t_i$ this gives $T/2<S<T$.",
        4145, "Together with $s_i<t_i$, this gives $T/2<S<T$."),
    inf("F1.8", r"With $\alpha=\lceil(12d^2b)^{1/4}\rceil$ and $\theta_i>\eta$, $\alpha^4\theta_i>3db\ge p$, so every hypothesis of the one-dimensional resampling lemma holds.",
        4149, r"\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p."),
    inf("F1.9", r"The machine finds the primes by deterministic scanning and trial division in $n^{o(1)}=o(n)$ time.",
        4170, "Since $p=6\\lceil\\log_2 n\\rceil=\\Theta(\\log n)$, the search takes", frm=["trial-division-and-primality-search"]),
    inf("F1.10", r"The product of the radix-digit polynomials has degree $2q-2<2n/b\le T/2<S$, so convolution modulo $x^S-1$ has no wraparound.",
        4186, r"2q-2<2n/b\le T/2<S.", frm=["polynomials"]),
    inf("F1.11", r"Every product coefficient satisfies $0\le c_j\le q(2^b-1)^2<2^{3b}$.",
        4191, r"0\le c_j\le q(2^b-1)^2<2^{3b},"),
  ],
  mline=4106, mquote="$t_i$: their product must occupy a fixed fraction of the padded box,",
  page="parameter-choice",
  frm=["synthetic-transform-layout", "gaussian-resampling", "tensor-resampling", "primes-coprimality-and-gcd", "trial-division-and-primality-search", "logarithms-floor-and-ceiling", "convolution-multiplication"],
  adds=[("b", "digit width", "the number of bits per radix digit, $\\lceil\\log_2n\\rceil$", "count"),
        ("S", "prime product", "the product of the distinct odd prime axis lengths $s_i$", "direct"),
        ("\\alpha", "Gaussian width", "the integer width parameter of Gaussian resampling, about $(12d^2b)^{1/4}$", "direct"),
        ("\\epsilon", "axis exponent", "the fixed rational exponent with $d=\\lfloor b^\\epsilon\\rfloor$ axes", "direct"),
        ("c", "chunk exponent", "the fixed rational exponent with $K=\\lfloor d^c\\rfloor$ bits per chunk", "direct")],
  salient="The prime lengths sit within a factor $(1-1/(2d))$ of the power-of-two axis lengths, so the $d$ axes together waste less than a factor two ($T/2<S<T$), yet each ratio $t_i/s_i$ exceeds $1+1/(4d)$, which is just enough separation for the resampling hypothesis $\\alpha^4\\theta_i>p$.")

# ---------------- F2 CRT ----------------
F2 = show("F2",
  r"The map $x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$ preserving cyclic convolution, and on addresses it is the triangular map $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, costing $O(Tp\,d^2(1+\ell^\tau))$.",
  "Use the Chinese remainder theorem to see that the image of $x$ has order $S$ and generates all monomials, then implement the address map by triangular controlled cyclic shifts on the padded box plus axis reorders.",
  "The classical CRT map of Agarwal and Cooley turns one long cyclic convolution into a multidimensional one over coprime axes; choosing coordinate powers $\\mu_i$ with $\\mu_iP_i\\equiv1$ makes it triangular, so it is a sequence of controlled shifts.",
  "explicit",
  [
    inf("F2.1", r"The target monomial group has size $S$ and the image of $x$ has order $S$, because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all target basis monomials exactly once.",
        4217, "group has size $S$, and the image of $x$ has order $S$, because each", frm=["primes-coprimality-and-gcd", "modular-arithmetic-and-congruences"]),
    inf("F2.2", r"Hence $\Phi$ is an isomorphism and preserves cyclic convolution.",
        4220, "$\\Phi$ is an isomorphism and preserves cyclic convolution."),
    inf("F2.3", r"For $k=\sum_ja_jP_j$ the coordinate of $\Phi(x^k)$ in axis $i$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$.",
        4228, r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}."),
    inf("F2.4", r"Terms with $j>i$ are divisible by $s_i$, and $\mu_iP_i=1$ modulo $s_i$.",
        4230, "Indeed terms with $j>i$ are divisible by $s_i$, and $\\mu_iP_i=1$ modulo", frm=["euclidean-algorithm-and-modular-inverses"]),
    inf("F2.5", r"Updating targets in the order $i=d,d-1,\ldots,1$, each lower-index control still has its original value when target $i$ is updated.",
        4252, "order $i=d,d-1,\\ldots,1$ using \\eqref{eq:triangular-crt}.  When target"),
    inf("F2.6", r"If any lower-index control is invalid (at a padded address) the step is the identity, so each step is a bijection preserving the valid set and zero padding stays zero.",
        4264, "control is invalid, use the identity.  This defines a bijection of"),
    inf("F2.7", r"The map $\Phi$, its inverse and their padding operations cost $O(Tp\,d^2(1+\ell^\tau))$ by $O(d^2)$ axis exchanges plus linear passes.",
        4291, r"O\bigl(Tp\,d^2(1+\ell^\tau)\bigr)."),
  ],
  mline=4199, mquote="theorem to convert one cyclic convolution into multidimensional cyclic",
  page="crt-cyclic-convolution",
  frm=["controlled-shifts", "chunk-interchange", "primes-coprimality-and-gcd", "euclidean-algorithm-and-modular-inverses", "modular-arithmetic-and-congruences", "polynomials"])

# ---------------- F3 twist ----------------
F3 = show("F3",
  r"With $\zeta=e^{\pi i/r}$, the map $x_d\mapsto\zeta y$ is an isomorphism from $\mathbb C[x_d]/(x_d^r-1)$ to $\mathcal R_r$ that multiplies coefficient $k$ by $\zeta^k$, so convolution over the ring on the first $d-1$ axes computes the complex cyclic convolution: $\mathcal M_{\mathbb C}(f,g)=(f*g)/T$.",
  "Check that the twist is well defined and diagonal, verify on the wrap-around terms that the negacyclic sign is exactly compensated, and compose it with the normalized ring convolution.",
  "The ring convolution wraps negatively in the last coordinate, whereas the chirp identity needs a cyclic wrap; a diagonal phase twist converts one wrap into the other.",
  "recoverable",
  [
    inf("F3.1", r"The map is well defined because $(\zeta y)^r=(-1)(-1)=1$.",
        4308, "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.  On the bases", frm=["euler-s-formula-and-roots-of-unity"]),
    inf("F3.2", r"On the bases $(x_d^k)$ and $(y^k)$ it is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$, hence an isomorphism with inverse multiplying by $\zeta^{-k}$.",
        4310, "multiplying coefficient $k$ by the nonzero number $\\zeta^k$.  It is therefore an"),
    inf("F3.3", r"For indices with $k+l=j+hr$, $h\in\{0,1\}$, the twisted product term has factor $\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
        4317, r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j."),
    inf("F3.4", r"Consequently $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$.",
        4340, r"\mathcal M_r(\iota D_+f,\iota D_+g)"),
  ],
  page="coefficient-twist",
  frm=["negacyclic-ring", "euler-s-formula-and-roots-of-unity", "complex-numbers", "polynomials"])

F3b = inf("F3b",
  r"The computed source transform applies $\mathcal A$ line by line, then the computed chirp transform $\widetilde{\mathscr C}$ (built from the complex convolution), then $\mathcal B_0$ and the exact scale $2^\gamma$, with exact counterpart $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.",
  4462, r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A",
  frm=["tensor-resampling", "bluestein-chirp", "synthetic-convolution", "coefficient-twist"])

# ---------------- F4 algorithm ----------------
F4 = show("F4",
  r"The algorithm splits the inputs into radix-$2^b$ digits, applies the address map $\Phi$, applies the source transform to both, multiplies pointwise, applies the opposite source transform, undoes the scales, rounds, applies $\Phi^{-1}$ and propagates carries into the $2n$-bit product.",
  "Compose the transforms in the order that makes the retained source permutation cancel, so that after three transforms the exact result is $(u*v)/S^2$, and undo the known scalings by exact shifts and multiplications.",
  "The product of the digit polynomials is a cyclic convolution of length $S$; after the CRT map, resampling and chirps it is computed by transforming both inputs, multiplying pointwise and applying an opposite transform.",
  "recoverable",
  [
    inf("F4.0", r"Each radix digit $a_j$ is stored as the exact grid value $a_j2^{-b-2}$ (numerator $a_j2^{p-b-2}$, nonnegative exponent because $p=6b$), followed by $S-q$ zero records.",
        4498, "because $p=6b$, and the represented value is exactly $a_j2^{-b-2}$."),
    inf("F4.1", r"Apply the coefficient-address map $\Phi$ with its padded layout to obtain the source arrays $u,v$.",
        4508, "\\item Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain"),
    inf("F4.2", r"Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.",
        4511, "\\item Compute $\\widetilde{\\mathscr F}(u)$ and"),
    inf("F4.3", r"Multiply corresponding complex coefficients exactly and truncate each part toward zero to $p$ fractional bits, obtaining $z$.",
        4513, "\\item Multiply corresponding complex coefficients exactly and truncate"),
    inf("F4.4", r"Compute $\widetilde{\mathscr F}^+(z)$ and multiply its grid numerators exactly by $S$, obtaining $\widetilde w$.",
        4517, "\\item Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid"),
    inf("F4.5", r"Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, round the real parts to integers, apply $\Phi^{-1}$ and remove the padding.",
        4521, "\\item Multiply the grid numerators of $\\widetilde w$ exactly by"),
    inf("F4.6", r"Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits.",
        4530, "\\item Propagate radix-$2^b$ carries in increasing coefficient order."),
    inf("F4.7", r"After the three transforms the exact result is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$; the second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the integer coefficient convolution.",
        4539, "counterpart after the three transforms is $(u*v)/S^2$, so after the"),
  ],
  page="multiplication-algorithm",
  frm=["crt-cyclic-convolution", "gaussian-resampling", "bluestein-chirp", "permutation-cancellation", "tensor-resampling", "synthetic-convolution", "coefficient-twist", "parameter-choice", "convolution-multiplication"])

# ---------------- F5 exact recovery ----------------
F5 = show("F5",
  r"Every intermediate array stays in the unit disk, the accumulated error in each recovered product coefficient is below $1/2$, so rounding returns the exact integer coefficients and carry propagation gives the $2n$-bit product.",
  "Track the norm and the error of each computed procedure with contraction and bilinear-contraction bounds, from the ring convolution through the chirp and the source transform to the final scalings, then round and propagate carries.",
  "Errors add through contractions and bilinear maps on disk arrays, and the total of all sources is a power of two times $TL$, while the precision $p=6b$ leaves room for the scalings $S$, $2^{2b+4}$ and $2^\\gamma$.",
  "reconstructed",
  [
    inf("F5.1", r"The returned normalized ring convolution has error $E_{\rm ring}=M(3L+2)<5TL$ in units of $2^{-p}$, with $L=\log_2T$.",
        4591, r"E_{\rm ring}:=M(3L+2)<5TL."),
    inf("F5.2", r"The computed complex convolution has error less than $(E_{\rm ring}+4+4+4)2^{-p}<6TL\,2^{-p}$, from the two input twists, the ring convolution and the output untwist.",
        4617, r"<(E_{\rm ring}+4+4+4)h_p<6TLh_p."),
    inf("F5.3", r"The chirp transform has error less than $(6TL+2+4+4)2^{-p}<8TL\,2^{-p}$.",
        4638, r"<(6TL+2+4+4)h_p<8TLh_p."),
    inf("F5.4", r"The source transform error is below $E_sh_p$ with $E_s=9\,2^\gamma TL$, and the scaled approximation stays in the disk.",
        4652, r"E_s=9\,2^\gamma TL,"),
    inf("F5.5", r"The pointwise product $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has error less than $(2E_s+2)h_p$.",
        4687, r"Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$."),
    inf("F5.6", r"The opposite transform of $z$ is within $(3E_s+2)h_p$ of $(u*v)/S^2$.",
        4702, r"&<(3E_s+2)h_p."),
    inf("F5.7", r"After the scale by $S$ the error is below $E_wh_p$ with $E_w=S(3E_s+2)<28\,2^\gamma T^2L$.",
        4709, r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
    inf("F5.8", r"After the second scale by $2^{2b+4}S$ the absolute coefficient error is less than $2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b}$.",
        4724, r"2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b}"),
    inf("F5.9", r"Using $S\le T<2^b$, $L<b$ and $\gamma\le b/4$ this is less than $448b\,2^{-3b/4}<1/2$.",
        4726, r"\le448b\,2^{-3b/4}<\frac12."),
    inf("F5.10", r"The true coefficients are integers and the error is strictly below $1/2$, so rounding to the nearest integer returns the unique correct coefficient.",
        4730, "The strict error below $1/2$ makes the nearest integer to", frm=["rounding-and-square-roots"]),
    inf("F5.11", r"Carries $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$ with $Q_0=2^b$ satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$.",
        4779, "The carries satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$.  If this holds at", frm=["radix-representation-and-carry-propagation"]),
    inf("F5.12", r"The invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ fixes the first $j$ radix digits of the full product.",
        4788, r"=\sum_{h<j}d_hQ_0^h+k_jQ_0^j."),
    inf("F5.13", r"The exact product is less than $2^{2n}$, so all bits above position $2n-1$ are zero and exactly $2n$ bits are output.",
        4803, "than $2^{2n}$; all bits above position $2n-1$ are therefore zero."),
  ],
  page="exact-recovery",
  frm=["multiplication-algorithm", "fixed-point-precision", "norms-absolute-value-and-triangle-inequality", "rounding-and-square-roots", "radix-representation-and-carry-propagation"],
  salient="The final error bound $448b\\,2^{-3b/4}$ decays exponentially in $b$ although the errors of the transforms grow like $2^\\gamma T^2L$: the precision $p=6b$ exceeds the scales $2^{2b+4}$ of the digits, the factors $S,T^2<2^{2b}$, and the growth $2^\\gamma$ with $\\gamma=o(b)$.")

# ---------------- F6 time bound ----------------
rows = [
 ("F6.1", 4822, r"Prefix-slot moves and individual butterfly rounds cost $dK$ per unit $Tp$, power $\epsilon(1+c)$ of $p$.", "Prefix-slot moves and individual butterfly rounds & $dK$ & $\\epsilon(1+c)$"),
 ("F6.2", 4823, r"Chunk exchanges for the transform layout cost $pK^{\tau-1}$, power $1-\epsilon c(1-\tau)$.", "Chunk exchanges for transform layout & $pK^{\\tau-1}$ & $1-\\epsilon c(1-\\tau)$"),
 ("F6.3", 4824, r"Simultaneous butterfly rounds cost $\ell d^{\lambda'}$, power $1-\epsilon(1-\lambda')$.", "Simultaneous butterfly rounds & $\\ell d^{\\lambda'}$ & $1-\\epsilon(1-\\lambda')$"),
 ("F6.4", 4825, r"CRT and axis layouts cost $d^2(1+\ell^\tau)$, power $\tau+\epsilon(2-\tau)$.", "CRT and axis layouts & $d^2(1+\\ell^\\tau)$ & $\\tau+\\epsilon(2-\\tau)$"),
 ("F6.5", 4826, r"Gaussian line maps cost $dp^{1/2+\delta}\alpha$, power $3/4+\delta+3\epsilon/2$.", "Gaussian line maps & $dp^{1/2+\\delta}\\alpha$ & $3/4+\\delta+3\\epsilon/2$"),
 ("F6.6", 4827, r"Chirps, twists and scalar products cost $dp^\delta$, power $\epsilon+\delta$.", "Chirps, twists and scalar products & $dp^\\delta$ & $\\epsilon+\\delta$"),
 ("F6.7", 4828, r"Packed polynomial products cost $\log(rp)$, power $1-\epsilon$.", "Packed polynomial products & $\\log(rp)$ & $1-\\epsilon$"),
]
F6rows = [inf(i, c, l, t) for (i, l, c, t) in rows]

F6 = show("F6",
  r"Dividing each phase's cost by $Tp=\Theta(n)$ gives seven dominant powers of $p$, each at most $1-2\kappa$ for the fixed rational exponents, so the total time is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ with $\kappa=2^{-182}$.",
  "Tabulate the normalized cost of every phase, compare each dominant power of $p$ with $1$ by its margin $g_i$, bound the lower-order setup and repair costs by $o(Tp)$, and absorb fixed powers of $\\log p$ into the slack.",
  "Each phase is already bounded as $Tp$ times a power of $p$; the theorem follows once every exponent is strictly below one with a common fixed margin.",
  "recoverable",
  F6rows + [
    inf("F6.8", r"The margins are $g_1=1-\epsilon(1+c)>1/2$, $g_2=\epsilon c(1-\tau)=2^{-181}$, $g_3=\epsilon(1-\lambda')=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=\epsilon=2^{-75}$.",
        4851, r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad"),
    inf("F6.9", r"The smallest margin is $\min_ig_i=2^{-181}=2\kappa$, which leaves slack for any fixed power of $\log p$.",
        4854, "Thus $\\min_i g_i=2^{-181}=2\\kappa$.  This explicit slack will cover"),
    inf("F6.10", r"The prefix-slot moves and individual rounds use $O(dK)$ scans, and the layout uses $O(p/K)$ chunk exchanges each costing $O(VK^\tau)$, normalized $O(p/K)K^\tau=O(pK^{\tau-1})$.",
        4866, r"O(p/K)\,K^\tau=O(pK^{\tau-1})."),
    inf("F6.11", r"Each of the at most $\ell$ simultaneous rounds costs $O(Vd^{\lambda'})$, including basis changes, repair, row padding and cleanup.",
        4869, r"Proposition~\ref{prop:simultaneous-layer} supplies $O(Vd^{\lambda'})$"),
    inf("F6.12", r"With $\alpha=\Theta(p^{1/4+\epsilon/2})$ the Gaussian line maps cost $dp^{1/2+\delta}\alpha$ per unit $Tp$, the fifth row.",
        4889, r"$\alpha=\Theta(p^{1/4+\epsilon/2})$ explains its displayed power of $p$."),
    inf("F6.13", r"Setup at recursion nodes costs at most $p^{A+C}=o(Tp)$ and per-record or per-line setup costs $O(Tp^{A+C}/r)=o(Tp)$ since $r$ exceeds every fixed power of $p$.",
        4925, r"costs at most $p^{A+C}=o(Tp)$."),
    inf("F6.14", r"The sorting of exceptional records over all packed calls costs $O(Vp^{A'}2^{-K})=o(V)$, a deterministic worst-case bound.",
        4968, r"=O(Vp^{A'}2^{-K})=o(V)"),
    inf("F6.15", r"Each of the seven displayed powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually.",
        4983, "Each of the seven displayed powers is at most $1-2\\kappa$ by"),
    inf("F6.16", r"The complete large-input bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$; smaller lengths use schoolbook multiplication.",
        4987, r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})."),
  ],
  page="time-bound-accounting",
  frm=["multiplication-algorithm", "parameter-choice", "simultaneous-butterfly-layer", "synthetic-transform-layout", "chunk-interchange", "big-o", "logarithms-floor-and-ceiling"],
  salient="The smallest of the seven margins below one is $g_2=\\epsilon c(1-\\tau)=2^{-75}\\cdot2^{-56}\\cdot2^{-50}=2^{-181}$, so $\\kappa=2^{-182}=g_2/2$ is dictated by the chunk-exchange row, whose exponent $1-\\epsilon c(1-\\tau)$ combines the three tiny exponents $\\epsilon$, $c$ and $1-\\tau$.")

# ---------------- root ----------------
ROOT = show("S0",
  r"A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture.",
  "Reduce the integer product to a convolution over $\\mathbb C[y]/(y^r+1)$ on a padded power-of-two box through a chain of exact reductions, evaluate its Fourier-type transforms with two tape procedures (fast address interchange and simultaneous butterfly layers) that each save a power of their parameter, and then control error and cost.",
  "Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both data movement and butterfly arithmetic must be made cheaper than one pass per level.",
  "explicit",
  [R1, R2a, R2b, K, D, E, F1, F2, F3, F3b, F4, F5, F6],
  mline=92, mquote="We therefore need savings in both movement and arithmetic.",
  page="multiplication-below-nlogn",
  frm=["big-o", "turing-machines"],
  adds=[("n", "input length", "the number of bits of each factor", "count"),
        ("\\kappa", "saving exponent", "the constant $2^{-182}$ such that the time is $O(n(\\lg n)^{1-\\kappa})$", "direct"),
        ("p", "precision", "the number of fractional bits kept for each real and imaginary part of a coefficient, $6\\lceil\\log_2n\\rceil$", "count"),
        ("d", "axis count", "the number of axes of the padded box, about $p^\\epsilon$", "count"),
        ("K", "chunk width", "the number of address bits of one chunk, about $d^c$", "count"),
        ("r", "ring length", "the number of complex coefficients of a record in $\\mathbb C[y]/(y^r+1)$", "count"),
        ("\\ell", "ring exponent", "the base-two logarithm of $r$", "direct"),
        ("T", "box size", "the number of entries of the padded power-of-two box, about $4n/\\log n$", "count")],
  salient="The saving is a power of the logarithm, $(\\lg n)^{-\\kappa}$, with $\\kappa=2^{-182}$ astronomically small; it comes from a single strict inequality $s<Wm$ in the recursion of two tape procedures, and the constants of the construction are deliberately conservative.")

import json
def strip(n):
    n = dict(n)
    for k in ("quote",):
        if n.get(k): n[k] = {kk: vv for kk, vv in n[k].items() if not kk.startswith("_")}
    if n.get("motivation") and n["motivation"].get("quote"):
        m = dict(n["motivation"]); m["quote"] = {kk: vv for kk, vv in m["quote"].items() if not kk.startswith("_")}; n["motivation"] = m
    if n.get("children"): n["children"] = [strip(c) for c in n["children"]]
    return n

if __name__ == "__main__":
    out = {"root": strip(ROOT)}
    json.dump(out, open("/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E8F6X/exegenius/tasks/0003-argument.answer.json", "w"), indent=1)
    print("written")
