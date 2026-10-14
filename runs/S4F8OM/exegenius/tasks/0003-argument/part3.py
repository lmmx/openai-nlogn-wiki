"""S3: convolution over the negacyclic ring; S4: resampling with retained permutations."""
from tree_helpers import show, infer, mot, bind

# ---------------------------------------------------------------- S3.1
S31 = show(
    "S3.1",
    r"For a power of two $t$ dividing $2r$ and $\omega_t=y^{2r/t}$, the transforms $(F_t^\mp z)_j=\frac1t\sum_k\omega_t^{\mp jk}z_k$ over $\mathcal R_r$ are contractions with $F_t^+F_t^-=t^{-1}I$, and $F_t^-$ is computed by $\log_2t$ decimation-in-frequency levels, each a butterfly $H_0$ on the pairs $(z_k,z_{k+t/2})$ followed by multiplication of the second output by the signed shift $\omega_t^{-k}$.",
    r"Check the cancellation of characters directly, since $\mathcal R_r$ has zero divisors, and split the transform by the high address bit.",
    mot(r"Because $y^{2r}=1$ and $y^r=-1$, powers of $y$ behave as roots of unity of order dividing $2r$, yet multiplying by one only moves and negates coefficients, so every twiddle factor of the fast transform costs a signed copy instead of complex multiplications.",
        "explicit",
        r"Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list."),
    [
        infer("S3.1.1",
              r"Every power of $\omega_t$ is an isometry of the coefficient sup norm and each transform entry averages $t$ such images, so $F_t^\pm$ are contractions.",
              r"Thus both transforms are contractions."),
        infer("S3.1.2",
              r"For $t\nmid j$, write $j=2^vj_0$ with $j_0$ odd; shifting the summation index by $t/2^{v+1}$ multiplies $\sum_k\omega_t^{jk}$ by $y^{rj_0}=-1$, so the sum vanishes, which gives $F_t^+F_t^-=t^{-1}I$ without dividing by $\omega_t^j-1$.",
              r"Hence the sum is zero, since the additive group of $\mathcal R_r$ has no two-torsion."),
        infer("S3.1.3",
              r"For $b\in\{0,1\}$, $(F_t^-z)_{2h+b}=\frac1{t/2}\sum_{k<t/2}(\omega_t^2)^{-hk}\omega_t^{-bk}\frac{z_k+(-1)^bz_{k+t/2}}2$, so a butterfly $H_0$, the twiddle $\omega_t^{-k}$ on the $b=1$ output and two transforms of half length compute $F_t^-$.",
              r"This computes $F_t^-$ because, for $b\in\{0,1\}$,"),
    ],
    page="synthetic-polynomial-transform",
    frm=["negacyclic-ring", "discrete-fourier-transform", "fft-butterflies", "roots-of-unity-and-euler-s-formula"],
    salient=r"Every twiddle multiplication is free of real arithmetic: it is a signed cyclic shift of a coefficient list.",
    adds=[
        bind("t", "transform length", r"The length of one synthetic transform, a power of two dividing $2r$.", "count"),
        bind(r"\omega_t", "synthetic root", r"The element $y^{2r/t}$ of $\mathcal R_r$, a root of unity of order $t$.", "direct"),
    ],
)

# ---------------------------------------------------------------- S3.2
S32 = show(
    "S3.2",
    r"The recursion writes $(F_t^-z)_j$ at the bit-reversed slot of $j$, so the forward procedure computes $B_tF_t^-$ and the reversed procedure computes $F_t^+B_t^{-1}$, and on several axes the butterflies of one round form a single parallel layer $\mathcal H$ followed by one monomial $y^E$ per record; no frequency permutation is ever executed.",
    r"Track by induction which address slots hold branch bits, and identify the reversed recursion through $H_0^2=I/2$ and $F_t^+F_t^-=I/t$.",
    mot(r"The pointwise product does not care where each frequency sits and the opposite transform can consume the order the recursion produces, so leaving outputs where they are written avoids any permutation of whole frequency indices.",
        "explicit",
        r"We also specify where each frequency entry is stored, because the opposite transform consumes that same order after a pointwise product."),
    [
        infer("S3.2.1",
              r"Each level writes its branch bit into the slot whose pair it used, and these branch bits are the frequency bits from the lowest up, so after all $\log_2t$ levels the entry $(F_t^-z)_j$ sits at the slot $\operatorname{rev}(j)$ obtained by reversing the bits of $j$.",
              r"If $\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$."),
        infer("S3.2.2",
              r"Each reversed level is half the inverse of its forward level because $H_0^2=I/2$, so the reverse procedure composed with $B_tF_t^-$ is $I/t$; since $F_t^+B_t^{-1}$ composed with $B_tF_t^-$ is also $I/t$ and the forward procedure is invertible, the reverse procedure is $F_t^+B_t^{-1}$.",
              r"The forward procedure is invertible, so these two reverse operators agree."),
        infer("S3.2.3",
              r"On several axes each axis's twiddle depends only on its own address bits and commutes with the other axes' butterflies, so a round is one parallel butterfly $\mathcal H$ followed by multiplication of each record by $y^E$ with an address-dependent exponent $E$, and every round is a contraction.",
              r"Consequently the individual axis steps may be grouped as a parallel butterfly $\mathcal H$, followed by one recordwise monomial operation $J_E$."),
    ],
    page="stored-frequency-order",
    frm=["synthetic-polynomial-transform", "fft-butterflies", "permutations-and-bijections"],
    salient=r"The bit-reversal permutation appears in both exact operators but is never performed on tape.",
    adds=[
        bind("B_t", "bit reversal", r"The record permutation moving the entry at $j$ to the slot whose $\log_2t$ bits are those of $j$ in reverse order.", "direct"),
    ],
)

# ---------------------------------------------------------------- S3.3
S33 = show(
    "S3.3",
    r"With a layout permutation $L$ of record addresses built from $O(dK)$ single-bit moves and $O(p/K)$ exchanges of $K$-bit chunks, the forward and opposite synthetic transforms on axes of lengths $t_i\in\{2^{\ell-1},2^\ell\}$ have exact counterparts $LBF_{\boldsymbol t}^-$ and $F_{\boldsymbol t}^+B^{-1}L^{-1}$, error below $\sqrt2\,\ell2^{-p}$, and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.",
    r"Move the top bit of each long axis and the lowest $(\ell-1)\bmod K$ bits of every axis to a prefix, interleave the remaining $K$-bit chunks so that equal named positions sit at a common offset in consecutive chunks, run each round on them as one simultaneous butterfly layer followed by the monomial twiddles, and truncate once per round.",
    mot(r"The fast layer acts only on the same bit offset in consecutive equal-width chunks, so the axes' address bits must first be interleaved into that pattern, and chunk interchanges make this rearrangement cost less than the rounds themselves.",
        "explicit",
        r"To apply Proposition~\ref{prop:simultaneous-layer} in a transform round, we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks."),
    [
        infer("S3.3.1",
              r"Moving at most $dK$ named slots to the prefix costs $O(TpdK)$, and interleaving the remaining $K$-bit chunks takes fewer than $d\ell/K=O(p/K)$ chunk exchanges at $O(TpK^\tau)$ each, in total $O(Tp\,pK^{\tau-1})$.",
              r"Each costs $O(TpK^\tau)$, so all these exchanges cost"),
        infer("S3.3.2",
              r"In a round on the chunks the selected bits lie at one common offset in $d-1$ consecutive chunks of a complete address set, so the simultaneous layer applies at $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ over at most $\ell$ rounds, while the at most $K$ rounds on prefix slots are done bit by bit in $O(TpdK)$.",
              r"The simultaneous-layer procedure therefore applies at cost $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total."),
        infer("S3.3.3",
              r"The monomial $y^E$ is applied to a record by splitting its coefficient list once, moving the negated tail to the front and applying a common sign, in $O(rp)$ time and without sorting coefficients.",
              r"This is multiplication by $y^E$ modulo $y^r+1$."),
        infer("S3.3.4",
              r"Because truncation is odd and acts componentwise and $J_E$ is a signed coefficient permutation, $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$, so each round is a contraction followed by one truncation adding less than $\sqrt2\,2^{-p}$, and at most $\ell$ rounds give error below $\sqrt2\,\ell2^{-p}$.",
              r"Starting with zero error, at most $\ell$ rounds therefore give the claimed error and disk bounds."),
        infer("S3.3.5",
              r"Running the rounds on named slots after $L$ conjugates them by $L$, so the forward procedure is $LBF_{\boldsymbol t}^-$, storing frequency $j$ at $L(Bj)$, and the opposite procedure, which ends by restoring the order with $L^{-1}$, is $F_{\boldsymbol t}^+B^{-1}L^{-1}$.",
              r"In particular, the forward entry with frequency address $j$ is stored at $L(Bj)$."),
    ],
    page="transform-tape-layout",
    frm=["synthetic-polynomial-transform", "stored-frequency-order", "simultaneous-butterfly-layer", "address-chunk-interchange", "fixed-point-complex-arithmetic", "tape-address-model"],
    adds=[
        bind("L", "layout permutation", "The positional permutation of record addresses that moves prefix bits and interleaves the axes' chunks.", "direct"),
        bind("B", "multi-axis bit reversal", r"The tensor product of the bit reversals $B_{t_i}$ of the separate axes.", "direct"),
    ],
)

# ---------------------------------------------------------------- S3.4
S34 = show(
    "S3.4",
    r"For disk grid polynomials $f,g\in\mathcal R_r$ with $r<2^p$, the exact numerators of $fg$ and the truncation $Q_p(fg/r)$ are computed in $O(rp\log(rp))$ time by evaluating the four integer numerator polynomials at $B_0=2^{4p}$, multiplying the resulting integers with the established $O(n\log n)$ multiplier, extracting coefficients by centered carries, and folding the wrap with a sign.",
    r"Kronecker substitution with signed coefficients: encode each signed coefficient list as one integer with $4p$-bit fields, multiply, read the product's coefficients back as centered residues modulo $B_0$, and reduce modulo $y^r+1$.",
    mot(r"The pointwise products are only $O(rp)$ bits long, short compared with $n$, so the established multiplier handles them at cost $\log(rp)=O(p^{1-\epsilon})$ per stored bit, below the factor $p$ that would mean $n\log n$; fields of $4p$ bits leave room so that signed coefficients never overlap.",
        "recoverable"),
    [
        infer("S3.4.1",
              r"Every coefficient of the ordinary integer products satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so once the lower coefficients are removed the next one is identified by its centered residue modulo $B_0$.",
              r"After the lower coefficients have been removed from an evaluation, this strict bound identifies the next coefficient by its centered residue modulo $B_0$."),
        infer("S3.4.2",
              r"Packing a signed list $u$ with carries in $\{-1,0\}$ produces $r$ blocks of $4p$ bits that form a two's-complement encoding of $u(B_0)$, negative exactly when the final carry is $-1$, in $O(rp)$ time.",
              r"The $r$ blocks are therefore a fixed-width two's-complement encoding of $A_u$, with $\gamma_r=-1$ exactly when $A_u<0$."),
        infer("S3.4.3",
              r"Reading a product's blocks from the low end and taking centered residues with a carry in $\{0,1\}$ recovers each coefficient exactly, because the residual identity forces the centered representative to be $h_j$, in $O(rp)$ time.",
              r"Thus $\widehat h_j=h_j$."),
        infer("S3.4.4",
              r"Combining the four products into real and imaginary numerators, subtracting the coefficient at $j+r$ from that at $j$ to reduce modulo $y^r+1$, and shifting right by $p+\log_2r$ bits gives $Q_p(fg/r)$ in linear time, so the four integer products dominate the cost.",
              r"Four exact integer products dominate the linear packing, extraction, combination, wrapping, and truncation costs."),
    ],
    page="signed-packing",
    frm=["n-log-n-barrier", "negacyclic-ring", "positional-notation-in-any-radix", "polynomials", "binary-numerals-and-bit-strings"],
    adds=[
        bind("B_0", "packing base", r"The evaluation point $2^{4p}$ at which coefficient lists are packed into integers.", "direct"),
    ],
)

# ---------------------------------------------------------------- S3.5, S3.6
S35 = infer(
    "S3.5",
    r"Since $F_{\boldsymbol t}^-(f*g)=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)$ and $F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$, scaling by $M$ the opposite transform of the pointwise products $uv/r$ gives $(f*g)/(rM)$, and the products may be formed in the stored order because the record permutation $LB$ commutes with the pointwise product.",
    r"Since $LB$ permutes records and leaves their polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$.",
    frm=["convolution", "discrete-fourier-transform", "stored-frequency-order"],
)
S36 = infer(
    "S3.6",
    r"Each forward transform errs by less than $\delta=\sqrt2\,\ell2^{-p}$; the bilinear product of disk arrays turns these into less than $2\delta$, truncation adds $\eta=\sqrt2\,2^{-p}$, the contracting opposite transform adds less than $\delta$, and the exact scale by $M$ gives error below $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$.",
    r"The final exact multiplication by $M$ therefore gives error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed.",
    frm=["contraction-error-propagation", "triangle-inequality-and-norms"],
)

# ---------------------------------------------------------------- S3
S3 = show(
    "S3",
    r"For arrays on $\prod_{i<d}\mathbb Z/t_i\mathbb Z$ with values in $\mathcal R_r=\mathbb C[y]/(y^r+1)$, axis lengths $t_i\in\{r/2,r\}$ and $M=\prod_{i<d}t_i=T/r$ records, the normalized cyclic convolution $\mathcal M_r(f,g)=(f*g)/T$ of disk grid operands can be computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$, where $\ell=\log_2r$, in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.",
    r"Apply the two forward synthetic transforms and keep their stored frequency order, multiply corresponding polynomial records exactly by signed packing with division by $r$ and one truncation, apply the opposite transform to that order, and scale exactly by $M$.",
    mot(r"Over $\mathcal R_r$ the roots of unity of power-of-two transforms are powers of $y$, which act as signed shifts of coefficient lists, so the transforms need only butterflies and data movement, exactly what the two tape procedures accelerate; the pointwise products that remain are short polynomial products for the established multiplier.",
        "explicit",
        r"Their entries will be short polynomials in a quotient where the required roots of unity act by exact signed permutations of coefficient lists."),
    [S31, S32, S33, S34, S35, S36],
    page="normalized-ring-convolution",
    frm=["convolution", "negacyclic-ring", "discrete-fourier-transform", "contraction-error-propagation", "n-log-n-barrier"],
    adds=[
        bind("t_i", "axis length", r"The length of transform axis $i$, a power of two equal to $r/2$ or $r$.", "count"),
        bind("M", "record count", r"The number of polynomial records, $T/r$.", "count"),
        bind(r"\ell", "record exponent", r"The number $\log_2r$, the count of radix-two levels on a long axis.", "count"),
        bind(r"\mathcal R_r", "negacyclic ring", r"The ring $\mathbb C[y]/(y^r+1)$ of complex polynomials of degree below $r$ with $y^r=-1$.", "direct"),
    ],
)

# ---------------------------------------------------------------- S4.1
S41 = show(
    "S4.1",
    r"For coprime $2\le s<t<2^p$ with $t/s-1>p/\alpha^4$ there are linear contractions $A,B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, approximable on the disk grid with error below $p^2$ in $O(tp^{3/2+\delta}\alpha)$ time; tensoring over the $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$, computed line by line in the zero-padded box with error below $dp^2$ in time $O(dTp^{3/2+\delta}\alpha)$, plus $O(Tp\,d^2(1+\ell^\tau))$ for exposing the axes.",
    r"Take the Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$, invert the nearly-identity sampling map by a Neumann series to obtain a left inverse of $\mathsf T$, and apply the resulting one-dimensional maps line by line, exposing each axis by chunk interchanges.",
    mot(r"The Chinese-remainder axes have prime lengths, but the synthetic transforms need powers of two; Gaussian resampling converts one into the other through contractions whose approximations err by only a polynomial in $p$ grid units.",
        "explicit",
        r"it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two"),
    [
        infer("S4.1.1",
              r"The map $N$ that samples the Gaussian-smoothed vector at the grid points nearest to $tj/s$ and reweights them is within $2^{-\alpha^2\theta}<1/2$ of the identity, because $\alpha^2\theta>p/\alpha^2>1$, so $N$ is invertible by a Neumann series.",
              r"Thus $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series."),
        infer("S4.1.2",
              r"Applying the resulting left inverse of $\mathsf T$ to $\mathsf TP_sF_s=P_tF_t\mathsf S$ expresses $P_sF_s$ through $P_tF_t$, and normalizing its three factors by $2^{-(2\alpha^2-2)}$, $1/2$ and $1/2$ yields contractions $A,B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$.",
              r"Applying this left inverse to the first identity in \eqref{eq:gaussian-public-facts} gives $\mathsf D N^{-1}CP_tF_t\mathsf S=P_sF_s$."),
        infer("S4.1.3",
              r"The original algorithm executes $P_t$ and $P_s^{-1}$ by two label-and-sort passes of cost $O(tp\log t)$; here both stay in the identity, and the algorithms for $A$ and $B_0$ use only an ordered selection and the three quoted numerical maps.",
              r"In \eqref{eq:no-sort-one-dimensional} these permutations remain in the transform identity."),
        infer("S4.1.4",
              r"Tensoring gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$, and applying each one-dimensional map to the valid lines of the zero-padded box keeps each axis map a contraction with error below $p^2$, so the $d$ axes give error below $dp^2$.",
              r"Composing the $d$ axis maps gives error less than $dp^2$."),
        infer("S4.1.5",
              r"Exposing an axis as the innermost field and restoring it takes $O(d)$ adjacent axis interchanges by chunk swaps, each $O(Tp(1+\ell^\tau))$, so all axes cost $O(Tp\,d^2(1+\ell^\tau))$.",
              r"Exposing and restoring one axis needs $O(d)$ adjacent interchanges, hence all axes need $O(d^2)$."),
    ],
    page="gaussian-resampling",
    frm=["discrete-fourier-transform", "contraction-error-propagation", "exponential-logarithm-and-gaussian-function", "address-chunk-interchange", "primes-coprimality-and-gcd"],
    adds=[
        bind(r"\alpha", "Gaussian width", r"The integer parameter setting the Gaussian widths, about $p^{1/4+\epsilon/2}$ in the multiplier.", "direct"),
    ],
)

# ---------------------------------------------------------------- S4.2
S42 = show(
    "S4.2",
    r"With the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$, which has period $t_i$ in coordinate $i$ because each $t_i$ is even, the permuted transform satisfies $QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}T$.",
    r"Compare the coefficient of $u_{\boldsymbol k}$ on both sides, using $2jk=j^2+k^2-(j-k)^2$ in each coordinate.",
    mot(r"Bluestein's identity writes a Fourier transform as pointwise phases around a cyclic convolution, and putting the factor $s_i$ into the chirp builds the frequency dilation $Q$ into the phases, so $Q$ never has to be performed and the convolution keeps the power-of-two lengths.",
        "explicit",
        r"The chirp identity below performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array."),
    [
        infer("S4.2.1",
              r"Replacing $j_i$ by $j_i+t_i$ changes the chirp's exponent by $-\pi is_i(2j_i+t_i)$, an integer multiple of $2\pi i$ since $t_i$ is even, so $a$ is periodic and its cyclic convolution is well defined.",
              r"Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by $-\pi i s_i(2j_i+t_i)$, an integral multiple of $2\pi i$."),
        infer("S4.2.2",
              r"The coefficient of $u_{\boldsymbol k}$ on the right is $\frac1T\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}=\frac1T\exp(2\pi i\sum_is_ij_ik_i/t_i)$, which is the coefficient of $QF_{\boldsymbol t}$ because $Q$ reads frequency $(-s_ij_i)_i$ of the negative-sign transform.",
              r"This is precisely the coefficient in $QF_{\boldsymbol t}$, because $Q$ reads frequency $(-s_i j_i)_i$ from the negative-sign transform."),
    ],
    page="bluestein-chirp",
    frm=["discrete-fourier-transform", "convolution", "roots-of-unity-and-euler-s-formula", "exponential-logarithm-and-gaussian-function"],
)

# ---------------------------------------------------------------- S4.3
S43 = show(
    "S4.3",
    r"Because each $t_i$ is a unit modulo $s_i$, $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$, so the normalized convolution rule gives $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$, and conjugating the input and output of a procedure for $RF_{\boldsymbol s}$ gives one for $RF_{\boldsymbol s}^+$ with the same error.",
    r"Substitute $h=ck$ in the Fourier sum to move a unit dilation through the transform, then apply the normalized convolution rule.",
    mot(r"A dilation by a unit only relabels Fourier coordinates, $F^+R_c=R_c^{-1}F^+$, so keeping $R$ in both forward transforms and in the opposite-sign transform makes it cancel algebraically instead of being sorted out.",
        "recoverable"),
    [
        infer("S4.3.1",
              r"For a unit $c$ modulo $q$ and $(R_cz)_j=z_{cj}$, substituting $h=ck$ gives $F_q^+R_c=R_c^{-1}F_q^+$; each $t_i$ is a unit modulo $s_i$, so tensoring gives $F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.",
              r"Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives $F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$."),
        infer("S4.3.2",
              r"With $(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)=R(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)$ and the two normalizations the product formula equals $F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=(u*v)/S^2$, and complex conjugation, which commutes with the real permutation $R$ and preserves grid and norm, turns a procedure for $RF_{\boldsymbol s}$ into one for $RF_{\boldsymbol s}^+$.",
              r"Finally, conjugation changes the negative Fourier sign to the positive one and commutes with the real permutation $R$."),
    ],
    frm=["discrete-fourier-transform", "convolution", "modular-arithmetic", "permutations-and-bijections"],
)

# ---------------------------------------------------------------- S4
S4 = show(
    "S4",
    r"For distinct odd prime source lengths $s_i$ and powers of two $t_i>s_i$, Gaussian resampling gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with contractions $\mathcal A,\mathcal B_0$ and coordinate permutations $R,Q$ that are never executed: $QF_{\boldsymbol t}$ is a chirp-weighted cyclic convolution of length $T=\prod_it_i$, and $R$ cancels because $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$ with $S=\prod_is_i$.",
    r"Keep both coordinate permutations of the Harvey–van der Hoeven resampling identity inside the transform formula, absorb the target permutation into Bluestein's chirp identity, and cancel the source permutation between the forward transforms and the opposite-sign transform.",
    mot(r"Executing either permutation would mean sorting the array on every coordinate, an extra logarithmic factor that a power saving cannot afford, whereas the identities show that neither permutation changes the final convolution.",
        "explicit",
        r"Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and compute that formula directly."),
    [S41, S42, S43],
    page="permutation-cancellation",
    frm=["discrete-fourier-transform", "convolution", "permutations-and-bijections", "sorting-and-its-cost"],
    salient=r"Neither coordinate permutation of resampling is ever performed: the target permutation disappears into the chirp phases and the source permutation cancels exactly.",
    adds=[
        bind("s_i", "source length", r"The prime length of source axis $i$, slightly below $t_i$.", "count"),
        bind("S", "source size", r"The product of the source lengths, which is the length of the cyclic convolution being computed.", "count"),
        bind("R", "source permutation", r"The coordinate permutation that reads source index $t_ij$ at position $j$ on each axis.", "direct"),
        bind("Q", "target permutation", r"The coordinate permutation that reads frequency $-s_ik$ at position $k$ on each axis.", "direct"),
        bind(r"\gamma", "resampling scale", r"The exponent $2d\alpha^2$ of the exact power-of-two factor in the resampling identity.", "count"),
    ],
)
