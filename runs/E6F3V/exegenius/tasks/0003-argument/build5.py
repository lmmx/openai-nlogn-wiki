# ---------------- S6: the multiplication algorithm ----------------
S611 = show("S6.1.1",
  r"Distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ exist, have product $S$ with $T/2<S<T$, and ratios $t_i/s_i$ large enough that $\alpha^4\theta_i>p$ for $\theta_i=t_i/s_i-1$.",
  r"Apply the explicit prime-count lower bound to an interval just below each power of two, check the two intervals are disjoint and hold more than $d$ primes, then multiply the lower bounds on the $s_i$ using Bernoulli's inequality.",
  mot("explicit", "The primes must be close to the powers of two so that their product fills a fixed fraction of the padded box, while each ratio must leave enough separation for resampling.",
      Q(4104, 4109, "The distinct prime lengths $s_i$ must be close to the powers of two", "leave enough separation for resampling.")),
  [
   infer("S6.1.1.1",
     r"For $0<\eta<1/4$ and $x>e^{2/\eta}$, the interval $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes.",
     Q(4112, 4118, r"$0<\eta<1/4$ and $x>e^{2/\eta}$, the interval", "primes.")),
   infer("S6.1.1.2",
     r"Hence distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ can be chosen, each coprime to $t_i$.",
     Q(4133, 4137, "We may therefore choose distinct odd primes satisfying", r"(1-\eta)t_i.")),
   infer("S6.1.1.3",
     r"Multiplying the lower bounds with strict Bernoulli gives $S/T>(1-1/(2d))^d>1/2$, so $T/2<S<T$.",
     Q(4138, 4146, r"Put $S=\prod_i s_i$.", r"$T/2<S<T$.")),
   infer("S6.1.1.4",
     r"The upper bound on $s_i$ gives $\theta_i>\eta$ and so $\alpha^4\theta_i>3db\ge p$.",
     Q(4146, 4151, r"Writing $\theta_i=t_i/s_i-1$", r"\geq6b=p.")),
   infer("S6.1.1.5",
     r"Scanning the two intervals and testing by trial division takes $n^{o(1)}=o(n)$ time.",
     Q(4169, 4172, r"Since $p=6\lceil\log_2 n\rceil=\Theta(\log n)$", r"=o(n)$ time.")),
  ],
  page="prime-axis-lengths",
  frm=["primes-coprimality-and-the-extended-euclidean-algorithm", "logarithms-exponentials-floors-and-ceilings", "limits-and-limit-inferior"],
  ad=adds(
   ("\\eta", "relative gap", "The relative distance 1/(4d) below each power of two within which the prime is sought.", "direct"),
   ("\\alpha", "Gaussian width", "The Gaussian width parameter for resampling, about (12 d^2 b)^(1/4).", "direct")))

S61 = show("S6.1",
  r"Fixed rational exponents $(\tau,\sigma,\lambda',c,\epsilon,\delta,\kappa)$ and sizes $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, $T\in[4n/b,8n/b)$ a power of two, $r=2^\ell$ with axis lengths $t_i\in\{r/2,r\}$, and prime lengths $s_i<t_i$, make $Tp=\Theta(n)$ and satisfy every condition of the earlier procedures.",
  r"Fix all exponents as explicit rationals, then define the sizes from $n$ so that the padded array holds $\Theta(n)$ bits, the number of axes $d$ grows like $p^\epsilon$, and the record length $r$ grows faster than every fixed power of $p$.",
  mot("explicit", "The procedures proved earlier each need conditions on their parameters, so compatible parameters must be chosen before the integer coefficients can be recovered and the remaining tape operations accounted for.",
      Q(3998, 4003, "We choose compatible parameters", "remaining tape operations.")),
  [
   infer("S6.1.2",
     r"Take $\tau=\sigma=1-2^{-50}$, $\beta=1/2$, $\delta=1/16$, $\lambda=1-2^{-52}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $C_1=20$, $\epsilon=2^{-75}$, $\kappa=2^{-182}$.",
     Q(4009, 4014, r"\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},", r"\kappa=2^{-182}.")),
   infer("S6.1.3",
     r"For large $n$ put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $K=\lfloor d^c\rfloor$.",
     Q(4053, 4058, r"b=\lceil\log_2n\rceil,\quad p=6b,", r"K=\lfloor d^c\rfloor.")),
   infer("S6.1.4",
     r"Take the power of two $T$ in $[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$, and choose axis lengths in $\{r/2,r\}$ with product $T$ and $t_d=r$.",
     Q(4057, 4063, "Take the power of two $T$ in $[4n/b,8n/b)$, and let", "the others to be $r$.")),
   infer("S6.1.5",
     r"These give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$.",
     Q(4068, 4073, r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),", r"r=2^{\Theta(p^{1-\epsilon})}.")),
   S611,
  ],
  page="parameter-choice",
  frm=["logarithms-exponentials-floors-and-ceilings", "limits-and-limit-inferior", "asymptotic-notation-beyond-big-o"],
  salient="The exponents are astronomically small ($\\epsilon=2^{-75}$, $c=2^{-56}$) but fixed: they keep $d$ growing slowly while $r=2^{\\Theta(p^{1-\\epsilon})}$ still dominates every polynomial in $p$.")

S62 = show("S6.2",
  r"Splitting $x$ and $y$ into $q=\lceil n/b\rceil$ radix-$2^b$ digits turns the product into a convolution of digit sequences with degree below $S$, so cyclic convolution of length $S$ has no wraparound, and every coefficient is below $2^{3b}$.",
  r"Write each input as a polynomial in $2^b$, bound the degree of the product by the transform size, and bound each coefficient by the digit count times the squared digit size.",
  mot("explicit", "Splitting the inputs into radix digits reduces multiplication to a convolution of short integer coefficients.",
      Q(75, 78, "Splitting the inputs into radix digits reduces multiplication to", "short integer coefficients.")),
  [
   infer("S6.2.1",
     r"The product of the two digit polynomials has degree at most $2q-2<2n/b\le T/2<S$, so convolution modulo $x^S-1$ has no nonzero wraparound.",
     Q(4182, 4189, "Write the two inputs as polynomials in $2^b$", "no nonzero wraparound.")),
   infer("S6.2.2",
     r"Every product coefficient obeys $0\le c_j\le q(2^b-1)^2<2^{3b}$ since $q\le n\le2^b$.",
     Q(4190, 4194, r"0\le c_j\le q(2^b-1)^2<2^{3b},", r"since $q\le n\le2^b$.")),
  ],
  page="radix-digit-convolution",
  frm=["positional-number-systems-and-carries", "convolution-of-sequences", "schoolbook-and-karatsuba-multiplication", "polynomials", "cyclic-convolution"])

S63 = show("S6.3",
  r"The assignment $x\mapsto\prod_ix_i^{\mu_i}$ with $\mu_i=P_i^{-1}\bmod s_i$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$, carrying cyclic convolution of length $S=s_1\cdots s_d$ to convolution on the product of cyclic axes, and its action on padded addresses is a sequence of triangular controlled shifts costing $O(Tp\,d^2(1+\ell^\tau))$.",
  r"Use the Chinese-remainder (Agarwal–Cooley) map with coordinate powers $\mu_i$ chosen so that the new coordinate of axis $i$ depends only on lower-index digits, making the change of order triangular, then implement it by controlled cyclic shifts and axis exchanges.",
  mot("explicit", "The coordinate powers are chosen so that the change of order becomes a sequence of controlled cyclic shifts.",
      Q(4199, 4203, "The following map uses that algebraic split,", "controlled cyclic shifts.")),
  [
   infer("S6.3.1",
     r"The map respects $x^S=1$, its image of $x$ has order $S$ because each $\mu_i$ is a unit and the $s_i$ are coprime, so it is an isomorphism preserving cyclic convolution.",
     Q(4216, 4221, r"$\Phi$ is an isomorphism and preserves cyclic convolution.")),
   infer("S6.3.2",
     r"For $k=\sum_ja_jP_j$ the coordinate of $\Phi(x^k)$ in axis $i$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j \pmod{s_i}$, depending only on lower-index digits.",
     Q(4226, 4231, "The coordinate of $\\Phi(x^k)$ in axis $i$ is", r"\pmod{s_i}.")),
   infer("S6.3.3",
     r"After reordering the axes to $(a_1,\dots,a_d)$, update the targets in the order $i=d,d-1,\dots,1$ so each offset is computed from still-unchanged lower-index digits.",
     Q(4252, 4256, "Update the targets in the order", r"required by the formula.")),
   infer("S6.3.4",
     r"Each triangular update is a prefix-controlled cyclic shift: prepare the offset, split the valid target interval into two pieces and merge them in the opposite order.",
     Q(4273, 4277, "Each triangular update is a prefix-controlled cyclic shift.", "opposite order.")),
   infer("S6.3.5",
     r"Reversing the $d$ axes uses $O(d^2)$ exchanges of unequal-width chunks, so $\Phi$, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$.",
     Q(4287, 4293, r"Therefore the map $\Phi$, its inverse, and", r"(1+\ell^\tau)\bigr).")),
  ],
  page="crt-axis-map",
  frm=["controlled-shift", "chunk-interchange", "cyclic-convolution", "modular-arithmetic", "primes-coprimality-and-the-extended-euclidean-algorithm", "polynomials"])

S64 = show("S6.4",
  r"With $\zeta=e^{\pi i/r}$, the map $x_d\mapsto\zeta y$ multiplies coefficient $k$ by $\zeta^k$ and is an isomorphism $\mathbb C[x_d]/(x_d^r-1)\to\mathbb C[y]/(y^r+1)$; the negative wrap of the negacyclic product gives exactly the cyclic wrap once the twist is removed.",
  r"Check that the substitution is well defined, observe that it is diagonal in the coefficient bases, and check on a wrapped product term that the extra sign is absorbed by the factor $\zeta^r=-1$.",
  mot("explicit", "The power-of-two complex convolution needed by the chirp identity is obtained from the synthetic convolution over the polynomial ring by a coefficient twist.",
      Q(4299, 4303, "The power-of-two complex convolution used in the chirp identity", "by a coefficient twist.")),
  [
   infer("S6.4.1",
     r"The substitution $x_d\mapsto\zeta y$ is well defined because $(\zeta y)^r=(-1)(-1)=1$.",
     Q(4307, 4309, "is well defined, since", r"$(\zeta y)^r=(-1)(-1)=1$.")),
   infer("S6.4.2",
     r"On the monomial bases the map is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$, so it is an isomorphism with inverse multiplying by $\zeta^{-k}$.",
     Q(4309, 4313, "On the bases", r"$\zeta^{-k}$.")),
   infer("S6.4.3",
     r"For $k+l=j+hr$ with $h\in\{0,1\}$, a twisted negacyclic product term has factor $\zeta^{k+l}(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
     Q(4313, 4319, "For an explicit check on the wrap", r"(-1)^h=\zeta^j.")),
  ],
  page="phase-twist",
  frm=["negacyclic-ring", "cyclic-convolution", "roots-of-unity", "complex-numbers"])

S65 = infer("S6.5",
  r"Complex cyclic convolution on the padded box is computed by twisting both operands by $\zeta^k$, convolving the first $d-1$ axes over $\mathbb C[y]/(y^r+1)$ with the ring procedure, and untwisting.",
  Q(4384, 4392, r"f'&=Q_p(\widetilde\theta^+", r"\iota^{-1}h'\right)."),
  frm=["ring-convolution", "phase-twist"])

S66 = infer("S6.6",
  r"The middle transform $QF_{\boldsymbol t}$ is computed as a chirp multiplication, the complex convolution with the kernel $\widetilde a$, and a second chirp multiplication.",
  Q(4437, 4445, r"x_0&=Q_p(\overline{\widetilde a}", r"y_0)."),
  frm=["chirp-identity", "permutation-cancellation"])

S67 = infer("S6.7",
  r"The source transform applies the linewise Gaussian approximation $\mathcal A$, the computed chirp transform, the approximation $\mathcal B_0$, and an exact scaling by $2^\gamma$, with exact counterpart $RF_{\boldsymbol s}$.",
  Q(4455, 4462, "For a source disk-grid tensor of norm at most $.5$", r"by $2^\gamma$."),
  frm=["gaussian-resampling", "permutation-cancellation"])

S68 = infer("S6.8",
  r"Place the digits by $\Phi$, transform both operands, multiply pointwise and truncate, apply the opposite-sign transform, scale by $S$ and by $2^{2b+4}S$, round, undo $\Phi$ and propagate carries to output the $2n$-bit product.",
  Q(4506, 4510, "With these streams prepared, perform the following operations.", r"source arrays $u,v$."),
  frm=["crt-axis-map", "permutation-cancellation"])

S69 = infer("S6.9",
  r"After the three transforms the exact result is $(u*v)/S^2$, so after the first scale it is $(u*v)/S$ and after the second scale $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the integer coefficient convolution.",
  Q(4536, 4542, r"By \eqref{eq:source-permutation-cancel}, the exact", "integer coefficient convolution."),
  frm=["permutation-cancellation", "crt-axis-map"])

S610 = show("S6.10",
  r"Removing the known normalisations $S$ and $2^{2b+4}$, the recovered coefficient error is below $1/2$, so rounding gives the exact integer coefficients and radix carries give the exact $2n$-bit product.",
  r"Propagate errors through each procedure (exact maps are contractions, bilinear maps add the input errors) starting from the source-transform error $E_s$, then show the error after scaling by $2^{2b+4}S$ is below $1/2$, so rounding is exact, and finish with carries.",
  mot("explicit", "The next subsection verifies the disk bounds needed by every call and proves the final error is below one half, which justifies the rounding, the carries and the output length.",
      Q(4541, 4545, "The next subsection verifies the", "length.")),
  [
   infer("S6.10.1",
     r"The computed source transform has error less than $E_sh_p$ with $E_s=9\cdot2^\gamma TL$ (where $h_p=2^{-p}$ and $L=\log_2T$).",
     Q(4650, 4654, r"which is bounded by $E_sh_p$ with", r"E_s=9\,2^\gamma TL,")),
   infer("S6.10.2",
     r"The pointwise product satisfies $\|z-U\cdot V_1\|<(2E_s+2)h_p$.",
     Q(4687, 4688, r"Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$.")),
   infer("S6.10.3",
     r"After the first scale by $S$ the error is below $E_wh_p$ with $E_w=S(3E_s+2)<28\cdot2^\gamma T^2L$.",
     Q(4708, 4710, r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L.")),
   infer("S6.10.4",
     r"The final absolute error is below $448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<1/2$.",
     Q(4722, 4728, r"Since $S\le T<2^b$ and $L<b$ eventually", r"<\frac12.")),
   infer("S6.10.5",
     r"The strict error below $1/2$ makes the nearest integer the unique correct coefficient, and it lies in $[0,2^{3b})$.",
     Q(4730, 4733, r"The strict error below $1/2$ makes", "correct coefficient.")),
   infer("S6.10.6",
     r"Propagate radix-$2^b$ carries by $d_j=(c_j+k_j)\bmod Q_0$ and $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$, with $0\le k_j<Q_0^2$.",
     Q(4774, 4779, r"use the recurrence for $0\le j<S$:", r"\right\rfloor.")),
   infer("S6.10.7",
     r"The exact product is below $2^{2n}$, so removing zero padding bits and keeping leading zeros outputs exactly $2n$ bits.",
     Q(4802, 4806, "The exact product is less than $2^{2n}$;", r"exactly $2n$ bits.")),
  ],
  page="exact-recovery",
  frm=["radix-digit-convolution", "contraction-error", "fixed-point-numbers-dyadic-rationals-and-rounding", "positional-number-systems-and-carries", "vector-norms-and-the-triangle-inequality"],
  salient="Despite the loss of $2^\\gamma$ in resampling and the rescaling by $2^{2b+4}S$, the final error $448\\,b\\,2^{-3b/4}$ is far below $1/2$: the precision $p=6b$ leaves room because $\\gamma=o(b)$ and $S\\le T<2^b$.")

S6 = show("S6",
  r"Digits of $x$ and $y$ are placed on prime cyclic axes by the Chinese-remainder map, transformed by Gaussian resampling around a chirp convolution over $\mathbb C[y]/(y^r+1)$, multiplied pointwise, transformed with opposite sign, rescaled, rounded and carried to give the exact $2n$-bit product.",
  r"Follow the chain of reductions: radix-digit convolution, then cyclic convolution on distinct prime axes, then normalised convolution on power-of-two axes, then convolution over the polynomial ring, and account for every change of representation and its error.",
  mot("explicit", "The earlier procedures must be placed inside the multiplication reduction, and every change of representation has to be accounted for.",
      Q(183, 186, "The remaining proof places these procedures inside the multiplication", "change of representation.")),
  [S61, S62, S63, S64, S65, S66, S67, S68, S69, S610],
  page="multiplication-algorithm",
  frm=["cyclic-convolution", "hh-multiplier", "dft"],
  ad=adds(
   ("b", "digit width", "The number of bits in each radix digit, the ceiling of log2 n.", "count"),
   ("p", "precision", "The number of fractional bits of working precision, equal to 6b.", "count"),
   ("d", "axis count", "The number of cyclic axes on which the digits are laid out.", "count"),
   ("T", "box size", "The number of entries of the padded power-of-two box, a power of two near n/b.", "count"),
   ("S", "valid size", "The product of the pairwise coprime prime axis lengths, the number of valid source positions.", "count"),
   ("r", "record length", "The length of the polynomial in the last axis, a power of two.", "count")))

# ---------------- S7: time bound ----------------
S71 = infer("S7.1",
  r"Costs divided by $V=Tp$ are listed in a table whose rows are the prefix-slot moves, chunk exchanges, simultaneous rounds, CRT and axis layouts, Gaussian line maps, chirps and twists, and packed polynomial products.",
  Q(4821, 4828, "Prefix-slot moves and individual butterfly rounds", r"$\epsilon+\delta$\\"))

S72 = show("S7.2",
  r"The seven dominant powers of $p$ have margins $g_i$ below one that are all at least $2^{-181}$, so $\min_ig_i=2\kappa$.",
  r"Name the margin of each dominant term as an explicit rational expression in the fixed exponents and compare them by direct substitution.",
  mot("reconstructed", "Each dominant term is a power of $p$ whose exponent is $1$ minus a margin, so the total is $O(Tp\\cdot p^{1-\\min g_i})$ and only the smallest margin matters."),
  [
   infer("S7.2.1",
     r"The margins are $g_1=1-\epsilon(1+c)$, $g_2=\epsilon c(1-\tau)$, $g_3=\epsilon(1-\lambda')$, $g_4=1-\tau-\epsilon(2-\tau)$, $g_5=1/4-\delta-3\epsilon/2$, $g_6=1-\delta-\epsilon$, $g_7=\epsilon$.",
     Q(4840, 4848, r"g_1&=1-\epsilon(1+c)", r"g_7=\epsilon.")),
   infer("S7.2.2",
     r"Direct substitution gives $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$, so $\min g_i=2^{-181}=2\kappa$.",
     Q(4849, 4856, "Direct substitution gives", r"=2\kappa$.")),
  ],
  frm=["limits-and-limit-inferior"],
  salient="The binding margin is $g_2=\\epsilon c(1-\\tau)=2^{-181}$, from the chunk exchanges of the transform layout; $\\kappa=2^{-182}$ is half of it, which leaves slack to absorb any fixed power of $\\log p$.",
  ad=adds(("g_i", "margin", "The amount by which the power of p of the i-th dominant cost term falls below one.", "direct")))

S73 = show("S7.3",
  r"Each of the dominant rows is bounded by the cost of the procedure behind it: the transform layout and layers, the axis moves, the Gaussian line maps, and the packed polynomial products.",
  r"Take each row's normalised cost directly from the proposition or lemma that bounds the corresponding procedure, dividing by $V=Tp$.",
  mot("recoverable", "Every row of the table is the cost bound of one of the earlier procedures, divided by the volume $Tp$."),
  [
   infer("S7.3.1",
     r"Placing the chunk exchanges, there are $O(p/K)$ exchanges of width-$K$ chunks at cost $O(VK^\tau)$ each, so the normalised total is $O(pK^{\tau-1})$.",
     Q(4864, 4868, r"O(p/K)\,K^\tau=O(pK^{\tau-1}).")),
   infer("S7.3.2",
     r"The at most $\ell$ simultaneous rounds cost $O(Vd^{\lambda'})$ each, including basis changes, repair, row padding and cleanup.",
     Q(4868, 4873, "For the at most $\\ell$ simultaneous rounds,", "fixed-tape cleanup.")),
   infer("S7.3.3",
     r"Axis exposure and restoration need $O(d^2)$ adjacent axis moves, each costing $O(V(1+\ell^\tau))$.",
     Q(4874, 4876, "Axis exposure and restoration require", r"$O(V(1+\ell^\tau))$")),
   infer("S7.3.4",
     r"Dividing the Gaussian line costs by $V=Tp$ gives the fifth row, with the factor $\alpha=\Theta(p^{1/4+\epsilon/2})$ explaining its power of $p$.",
     Q(4888, 4890, r"Dividing by $V=Tp$ gives the fifth row.", r"power of $p$.")),
   infer("S7.3.5",
     r"There are $T/r$ polynomial records in each pointwise ring product, and four integer products on $O(rp)$ bits per record cost $O(Tp\log(rp))$ in total.",
     Q(4900, 4904, r"There are $T/r$ polynomial records in each pointwise ring product.", r"in total.")),
  ],
  frm=["simultaneous-butterfly-layer", "transform-layout", "chunk-interchange", "gaussian-resampling", "ring-convolution", "crt-axis-map"])

S74 = infer("S7.4",
  r"The compact sorting of exceptional streams over all calls sums to $O(Vp^{A'}2^{-K})=o(V)$, a deterministic worst-case bound.",
  Q(4965, 4974, "the compact sorting costs sum to at most", r"=o(V)"))

S75 = infer("S7.5",
  r"Each of the seven displayed powers is at most $1-2\kappa$ and any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
  Q(4983, 4988, "Each of the seven displayed powers is at most", r"(\log n)^{1-\kappa})."))

S76 = infer("S7.6",
  r"Below a fixed cutoff use schoolbook multiplication; the single fixed-alphabet, fixed-tape deterministic machine then has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and outputs the exact $2n$-bit product.",
  Q(4989, 4996, "Fix one cutoff beyond all the size,", r"required $2n$-bit product."))

S7 = show("S7",
  r"With $V=Tp=\Theta(n)$, the costs divided by $V$ are seven dominant terms $p^{1-g_i}$ with margins $g_i>0$ whose smallest is $2\kappa$, so the total time is $O(n(\lg n)^{1-\kappa})$.",
  r"Tabulate every operation's cost divided by $Tp$ as a power of $p$, check that each dominant power is at most $1-2\kappa$ by direct substitution of the fixed exponents, and absorb setup, repair and powers of $\log p$.",
  mot("explicit", "Every array holds $\\Theta(Tp)=\\Theta(n)$ stored bits, so each cost can be compared with $V$ and listed as a power of $p$.",
      Q(4809, 4813, "For the cost calculation put $V=Tp=\\Theta(n)$.", r"$\Theta(V)$ stored bits.")),
  [S71, S72, S73, S74, S75, S76],
  page="time-bound",
  frm=["simultaneous-butterfly-layer", "transform-layout", "chunk-interchange", "ring-convolution", "gaussian-resampling", "crt-axis-map", "parameter-choice", "multiplication-algorithm", "exact-recovery", "limits-and-limit-inferior"],
  salient="The smallest margin $g_2=2^{-181}$ is exactly $2\\kappa$: the exponent $\\kappa=2^{-182}$ is half of it, so the saving is a genuine power of $\\log n$ but astronomically small.")

# ---------------- root ----------------
ROOT = show("S0",
  r"One deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.",
  r"Reduce the product to a convolution of short digits evaluated by Fourier transforms, speed up the two costly ingredients (moving data between addresses, and butterfly arithmetic) by a power of a block size using one recursive saving, and total every cost term.",
  mot("explicit", "A plain transform scans $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ levels, which already costs $n\\log n$, so both the data movement and the arithmetic must be made cheaper than a full scan per level.",
      Q(90, 93, "Scanning an array of $\\Theta(n)$ stored bits at each of", "savings in both movement and arithmetic.")),
  [S1, S2, S3, S4, S5, S6, S7],
  page="main-theorem",
  frm=["schonhage-strassen-conjecture", "multitape-turing-machine", "big-o-notation", "asymptotic-notation-beyond-big-o", "limits-and-limit-inferior", "subroutines-and-reductions-between-problems"],
  salient="The saving $\\kappa=2^{-182}$ is astronomically small, yet it is a genuine power of $\\log n$: the running time is $o(n\\log n)$ through all input lengths, which refutes an eventual $\\Omega(n\\log n)$ lower bound.")
