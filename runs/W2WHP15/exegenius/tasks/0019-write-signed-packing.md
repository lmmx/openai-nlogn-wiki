# exegenius task 0019-write-signed-packing

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/W2WHP15` (paths below are relative to it)

Write one page of an explanatory wiki. The wiki explains a target result from source documents to a specific reader, one concept per page, in reading order.

- Write for this reader's next uncertainty: at each point, give what they need to follow, and no more. The task lists the step of the argument this page presents, its motivations, and the pages around it. They are material for deciding what to say, not a list to cover: explain the transitions this reader would find hard, and leave familiar ones to ordinary sentences.
- Open with a sentence that says what the concept is and what it is for on the way to the target.
- If the page presents a step of the argument, say how its method shows its claim, and give its main motivation in a sentence. Add another motivation only if the reader would be stuck without it.
- Explain the page's concept so that this reader can follow it using only what they already understand (listed below), what this page itself explains, and the linked prerequisite pages.
- Define any other technical term on this page, where it is first used.
- Say what each symbol denotes where you introduce it: what it stands for, and for a size or count, what it counts ("$r$, the number of complex coefficients in a record", not "a power of two $r$"). A use in an example ("take $r = 4$") does not say what $r$ denotes. Symbols listed as already bound can be used without restating them: the page shows the reader their meanings. Using one of those letters with another meaning confuses readers: pick another letter, or say on the page that the letter changes meaning here.
- Link each prerequisite page the first time you rely on it, using the exact markdown link given. You may also link the other pages listed. Submit rejects links to anything else in the wiki; external URLs are allowed.
- For each prerequisite page, give a relation: the prerequisite's id, a predicate, and the sentence that links or names it, copied exactly. Use the sentence where the page relies on it; do not add a sentence for the purpose. The page shows the relation as "<this page's concept> *<predicate>* <prerequisite>", so pick a predicate that makes that a true sentence, with this page's concept as subject: "is reduced to", "computes its transforms by", "is based on", "follows from", "bounds the cost of". Build the predicate from the sentence's own words (other forms of a word count: "reduces" for "reduced"), and pick one that says what the prerequisite does for this page: "uses" says little.
- Stay accurate to the sources. The paragraphs around the evidence are given below; read further in the sources only if they are not enough. State only what the sources support or what is standard background; do not invent results, constants or attributions.
- Cite the results and constants a reader may want to check, right after the claim: `<cite data-source="id">text copied word for word from that source</cite>`. Readers see these as "(see p. 5)"-style references, hidden until they ask for them, so the sentence must read complete without the quoted words: write "the cost is $O(n \log n)$ <cite …>…</cite>", not "the paper states the cost as <cite …>…</cite>". Submit rejects a citation right after "that", "as", "states", "says", "is", "gives", "reads" or a colon, and text not found in the named source. Do not cite common background.
- A citation says where a claim comes from; it does not explain it. If the page's concept is an identity, a construction or a definition, state it. Explain how the concept works and how it shows its claim. For a result the page uses from prior work, say what the result states and why it applies here, and cite the source for its proof: the page need not reproduce it.
- Keep the page short. The task gives its word limit, counted without mathematics and citations, and submit rejects a longer page. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: discrete mathematics (modular arithmetic, primes and coprimality, the Chinese remainder theorem, permutations, induction, recurrences), calculus-level analysis (logarithms, floor and ceiling, norms and rounding errors), linear algebra (vectors, matrices, invertibility, rank, over the reals, complex numbers and F2), and algorithms (asymptotic notation, schoolbook multiplication, divide and conquer, sorting) with a first look at the FFT. They know basic multitape Turing machines and tapes, polynomials and complex numbers including roots of unity. They have not met Schoenhage-Strassen or Karatsuba-level multiplication algorithms in depth, ring and group-algebra language beyond polynomials, tensor products, numerical error analysis of fixed-point transforms, or any research literature on integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n conjecture for integer multiplication (also: n log n optimality conjecture, Schönhage–Strassen conjecture)
- Established n log n multiplier
- Arrays, addresses and volume on tapes (also: address field, logical volume)
- Elementary stream operations (also: split and merge, row splitting)
- Controlled cyclic shifts (also: controlled shifts, ordered affine streams)
- Rank, subspaces and orthogonal complements (also: nondegenerate subspace, orthogonal residual)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring, R_r)
  - $y$ (ring variable): The formal polynomial variable, whose powers y^a act as roots of unity of order 2r.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Linear exchange network with restored scratch wires (also: bank exchange, finite network, role)
- Frames on wire arrays (also: frame, common-frame identity)
- Subspace labels from three-element subsets (also: rank saving construction, orthogonal residual labels)
- Address shear and lower-triangular factorization (also: Bruhat factorization, matrix shear)
- Recursive rank saving (also: power saving recurrence)
- Fast address-chunk interchange (also: chunk swap, tape interchange)
- Packed selected-bit addition (also: packed XOR, exceptional address repair)
- Fixed-point disk-grid arithmetic (also: disk grid, Gaussian dyadics, truncation Q_p)
- Logarithms and iterated logarithm notation (also: log, lg, log base 2, log2, powers of the logarithm, (lg n)^c)
- Big-Omega, Theta and little-o notation (also: Omega, Theta, Ω, Θ, little-o, asymptotic lower bound, tight bound)
- Binary representation and bit operations (also: binary strings, bits, XOR, exclusive or, bitwise operations, two's complement, Hamming weight, bit length)
- Modular arithmetic (also: congruence, residues mod m, Z/mZ, integers modulo m, centered residue, mod, wraparound)
- Primes, coprimality and gcd (also: prime numbers, pairwise coprime, relatively prime, greatest common divisor, gcd, Euclidean algorithm, prime number theorem, primes just below a number)
- Chinese remainder theorem (also: CRT, Chinese remainder, residues modulo coprime moduli)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, Euler's formula, twiddle factor, ω)
- Vectors, matrices and invertibility (also: matrix multiplication, matrix inverse, invertible matrix, linear map, linear combination, lower-triangular matrix, permutation matrix, identity matrix, transpose, linear operator)
- Finite field F2 arithmetic (also: GF(2), binary field, mod 2 arithmetic, Z/2Z, F_2)
- Permutations and Cartesian products (also: bijection, permutation of indices, index set, product set, multi-index, coordinate permutation, lexicographic order, mixed-radix indexing, row-major order)
- Floor, ceiling and summation notation (also: floor function, ceiling function, ⌊x⌋, ⌈x⌉, sigma notation, geometric series, indicator vector)
- Recurrences and induction (also: recurrence relation, solving recurrences, unrolling a recurrence, proof by induction, master theorem, divide and conquer recurrence)
- Norms, absolute values and error bounds (also: max norm, sup norm, infinity norm, triangle inequality, modulus bound, rounding error, truncation error, round to nearest integer, unit disk)
- Fast Fourier transform and divide and conquer (also: FFT, Cooley-Tukey, fast Fourier transform, O(n log n) transform, convolution theorem, multiplying polynomials by FFT)
- Sorting and data movement on tapes (also: sorting, merge, scan, linear scan, stream, sequential access)
- Finite alphabet encodings and constant-factor simulation (also: alphabet, constant overhead, constant factor slowdown, encoding data as tape symbols, fixed finite state control, Turing machine simulation)
- Ring and group notions for polynomials (also: commutative ring, ring with identity, quotient ring, isomorphism, ring homomorphism, unit of a ring)

## This page

Concept: Signed packing of polynomial products
Gloss: A signed form of Kronecker substitution: evaluate polynomial coefficients at 2^{4p} to get integers, multiply with the established multiplier, and read the product coefficients back by centered residues and carries.
Also called: Kronecker substitution

## This page in the argument

The step: Signed packing: for disk-grid polynomials $f,g\in\mathcal R_r$ one computes the exact Gaussian-integer numerators of $fg$ and returns $Q_p(fg/r)$ in $O(rp\log(rp))$ time with four products of $4pr$-bit integers by the established multiplier.
How: Evaluate the integer coefficient polynomials at $B_0=2^{4p}$ (signed Kronecker substitution), multiply, and read the coefficients back by centered residues, since each product coefficient is below $B_0/2$.
Why: The sources describe the reduction as a signed form of Kronecker substitution. (the sources say so: "reduction is a signed form of Kronecker substitution; compare" (paper))

Its sub-steps, in order:

- Write $f=2^{-p}(a+ib)$, $g=2^{-p}(c+ie)$ with integer polynomials of coefficients at most $2^p$; set $B_0=2^{4p}$ and $A_u=u(B_0)$, so $|A_u|<B_0^r/2$ fits in $4pr$ bits.
- Every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so each coefficient is identified by its centered residue modulo $B_0$ once lower ones are removed.
- Forming $A_u$ from signed coefficients: with carry $\gamma_j\in\{-1,0\}$ ($d_j\equiv u_j+\gamma_j\pmod{B_0}$), the blocks form a two's-complement encoding of $A_u$ computed by a constant number of linear scans.
- Extraction: at block $j$ let $\widehat h_j\in[-B_0/2,B_0/2)$ be congruent to $q_j+\rho_j$ and $\rho_{j+1}=(q_j+\rho_j-\widehat h_j)/B_0\in\{0,1\}$; the residual identity $\sum_{k\ge j}h_kB_0^{k-j}=\sum_{k\ge j}q_kB_0^{k-j}+\rho_j+\varepsilon B_0^{J-j}$ shows $\widehat h_j=h_j$ by induction.
- Reduction modulo $y^r+1$ (subtracting coefficient $j+r$ from $j$) gives each coefficient $H_j$ as a sum of exactly $r$ signed products, so $|H_j|\le r2^{2p}$ and the normalized product $fg/r$ lies in the disk.
- The output numerator is $\operatorname{trunc}_0(\Re H_j/2^{p+\ell})+i\operatorname{trunc}_0(\Im H_j/2^{p+\ell})$, implemented by a right shift of $p+\ell$ bits, with error less than $\sqrt2\,2^{-p}$ from $fg/r$.
- Four exact integer products of $O(rp)$ bits each, at cost $O(rp\log(rp))$, dominate the linear packing, extraction, combination, wrapping and truncation costs.

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.; how: Reduce the product to a convolution of short integer coefficients, evaluate the convolution through power-of-two transforms over $\mathbb C[y]/(y^r+1)$, and replace the two tape operations that each cost a factor $\log n$ (address rearrangement and butterfly layers) by procedures whose cost per bit is a power of their parameter below one; then total the costs. (on [Integer multiplication below n log n](main-theorem.md))
- Convolution over $\mathbb C[y]/(y^r+1)$: the normalized convolution of arrays on $d-1$ power-of-two axes with ring entries is computed in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ time with error less than $\sqrt2\,M(3\ell+1)2^{-p}$.; how: Apply two synthetic forward transforms keeping the same frequency order, multiply pointwise by signed packing divided by $r$, and apply the opposite transform, using the fast layers and chunk swaps for the transforms. (on [Convolution over the polynomial ring](ring-convolution.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S5.3.1, S5.3.2, S5.3.3, S5.3.4, S5.3.5, S5.3.6, S5.3.7). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S5.3.1**: Write $f=2^{-p}(a+ib)$, $g=2^{-p}(c+ie)$ with integer polynomials of coefficients at most $2^p$; set $B_0=2^{4p}$ and $A_u=u(B_0)$, so $|A_u|<B_0^r/2$ fits in $4pr$ bits.
Source: "Set $B_0=2^{4p}$" (paper)
> fix $C_w>1$. Let $w$ be an integer with $p+2\leq w\leq C_wp$. The input supplies $\Gamma(p)\Gamma(r)\Gamma(w)$ and two disk grid polynomials $f,g\in\mathcal R_r$ in the component format of Proposition~\ref{prop:simultaneous-layer} with width $w$. One can compute the exact Gaussian integer numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\log(rp))$ on a fixed number of tapes. The output is a disk grid polynomial with error less than $\sqrt2\,2^{-p}$ from $fg/r$. \end{lemma} \begin{proof} The supplied power of two $r$ determines $\ell=\log_2r$. Write \[ f=2^{-p}(a+ib),\qquad g=2^{-p}(c+ie), \] where $a,b,c,e\in\mathbb Z[y]$ have degree less than $r$ and coefficients of absolute value at most $2^p$. Set $B_0=2^{4p}$ and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values using the established multiplier and restore each product's sign. The resulting integers are $A_aA_c,A_bA_e,A_aA_e,A_bA_c$. For example, if $h=ac$ is the ordinary product in $\mathbb Z[y]$, then \[ A_aA_c=(ac)(B_0)=\sum_{j=0}^{2r-2}h_jB_0^j. \] The other three evaluation products have the same form. Every coefficient in any of these ordinary polynomial products satisfies \begin{equation} |h_j|\leq r2^{2p}<2^{3p}<B_0/2. \label{eq:packing-separation} \end{eq

**S5.3.2**: Every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so each coefficient is identified by its centered residue modulo $B_0$ once lower ones are removed.
Source: "|h_j|\leq r2^{2p}<2^{3p}<B_0/2." (paper)
> oefficients of absolute value at most $2^p$. Set $B_0=2^{4p}$ and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values using the established multiplier and restore each product's sign. The resulting integers are $A_aA_c,A_bA_e,A_aA_e,A_bA_c$. For example, if $h=ac$ is the ordinary product in $\mathbb Z[y]$, then \[ A_aA_c=(ac)(B_0)=\sum_{j=0}^{2r-2}h_jB_0^j. \] The other three evaluation products have the same form. Every coefficient in any of these ordinary polynomial products satisfies \begin{equation} |h_j|\leq r2^{2p}<2^{3p}<B_0/2. \label{eq:packing-separation} \end{equation} After the lower coefficients have been removed from an evaluation, this strict bound identifies the next coefficient by its centered residue modulo $B_0$.

**S5.3.3**: Forming $A_u$ from signed coefficients: with carry $\gamma_j\in\{-1,0\}$ ($d_j\equiv u_j+\gamma_j\pmod{B_0}$), the blocks form a two's-complement encoding of $A_u$ computed by a constant number of linear scans.
Source: "Since $-B_0<u_j+\gamma_j<B_0$ whenever" (paper)
> To form $A_u$, start with carry $\gamma_0=0$ and write \[ d_j\equiv u_j+\gamma_j\pmod{B_0},\quad 0\leq d_j<B_0, \qquad \gamma_{j+1}=\frac{u_j+\gamma_j-d_j}{B_0}. \] Since $-B_0<u_j+\gamma_j<B_0$ whenever $\gamma_j\in\{-1,0\}$, the carry stays in $\{-1,0\}$. Telescoping the recurrence gives \[ A_u=\sum_{j=0}^{r-1}d_jB_0^j+\gamma_rB_0^r. \] The $r$ blocks are therefore a fixed-width two's-complement encoding of $A_u$, with $\gamma_r=-1$ exactly when $A_u<0$. In that case complement and increment the blocks to obtain $|A_u|$; otherwise retain them. Every block has $4p$ bits and every carry has constant size, so a constant number of scans costs $O(rp)$. Endianness changes required by the multiplier are linear-time reversals on a work tape.

**S5.3.4**: Extraction: at block $j$ let $\widehat h_j\in[-B_0/2,B_0/2)$ be congruent to $q_j+\rho_j$ and $\rho_{j+1}=(q_j+\rho_j-\widehat h_j)/B_0\in\{0,1\}$; the residual identity $\sum_{k\ge j}h_kB_0^{k-j}=\sum_{k\ge j}q_kB_0^{k-j}+\rho_j+\varepsilon B_0^{J-j}$ shows $\widehat h_j=h_j$ by induction.
Source: "At block $j$, let $\widehat h_j$ be the unique" (paper)
> Now let $Z$ be one of the four signed product integers, and let $h$ be its corresponding ordinary polynomial product. Put $J=2r$ and pad that product by $h_{J-1}=0$. The bound on the evaluation integers gives $|Z|<B_0^J/4$, so $Z$ fits in $J$ blocks of width $4p$. Convert its sign and magnitude to sign-extended two's complement: \[ Z=\sum_{j=0}^{J-1}q_jB_0^j+\varepsilon B_0^J, \qquad 0\leq q_j<B_0,\quad \varepsilon\in\{-1,0\}. \] Zero-fill the unused high blocks; for a negative sign, complement and increment within this fixed width. These conversions take a constant number of scans. Put $\rho_0=0$. At block $j$, let $\widehat h_j$ be the unique integer in $[-B_0/2,B_0/2)$ congruent to $q_j+\rho_j$ modulo $B_0$, and put \[ \rho_{j+1}= \frac{q_j+\rho_j-\widehat h_j}{B_0}. \] The carry belongs to $\{0,1\}$: if $\rho_j$ has this property, then $0\leq q_j+\rho_j\leq B_0$, and centering either leaves this value unchanged or subtracts $B_0$.

**S5.3.5**: Reduction modulo $y^r+1$ (subtracting coefficient $j+r$ from $j$) gives each coefficient $H_j$ as a sum of exactly $r$ signed products, so $|H_j|\le r2^{2p}$ and the normalized product $fg/r$ lies in the disk.
Source: "|H_j|\leq r2^{2p}." (paper)
> The real and imaginary numerator streams are respectively $ac-be$ and $ae+bc$. To reduce them modulo $y^r+1$, subtract the coefficient at $j+r$ from the one at $j$ for $0\leq j<r$, treating a missing coefficient as zero. Splitting the two halves to tapes aligns these terms in one further scan. For each first input index $j_1\in\{0,\ldots,r-1\}$, exactly one second index $j_2$ in that range satisfies $j_1+j_2\equiv j\pmod r$. Its sign is positive when $j_1+j_2=j$ and negative when $j_1+j_2=j+r$. Thus each resulting Gaussian integer coefficient $H_j$ is a sum of exactly $r$ signed products of Gaussian integer input coefficients of modulus at most $2^p$. Consequently \[ |H_j|\leq r2^{2p}. \] The same triangle inequality before imposing the disk bound gives $\|fg/r\|_\infty\leq\|f\|_\infty\|g\|_\infty$; in particular the normalized product of disk polynomials lies in the disk. All intermediate coefficient additions fit in $O(p)$ bits. The width-$4p$ packing fields and the exact multiplier output prevent overflow or ambiguity between adjacent fields.

**S5.3.6**: The output numerator is $\operatorname{trunc}_0(\Re H_j/2^{p+\ell})+i\operatorname{trunc}_0(\Im H_j/2^{p+\ell})$, implemented by a right shift of $p+\ell$ bits, with error less than $\sqrt2\,2^{-p}$ from $fg/r$.
Source: "Finally the $p$-bit grid numerator of the normalized product is" (paper)
> Finally the $p$-bit grid numerator of the normalized product is \[ \operatorname{trunc}_0\left(\frac{\Re H_j}{2^{p+\ell}}\right) +i\operatorname{trunc}_0\left(\frac{\Im H_j}{2^{p+\ell}}\right). \] To implement it, shift the absolute magnitude right by $p+\ell$ bits and restore its sign, at cost $O(p)$ per coefficient. The returned coefficient is $2^{-p}$ times this numerator, namely $Q_p(2^{-2p}H_j/r)$; \eqref{eq:transform-truncate} proves its error and disk bounds. Each returned component numerator has magnitude at most $2^p$, so write it as a signed $w$-bit two's-complement word, most significant bit first, with the real word before the imaginary word and coefficient indices in increasing order. This costs $O(rw)=O(rp)$ and supplies the format used by the opposite transform. Four exact integer products dominate the linear packing, extraction, combination, wrapping, and truncation costs. \end{proof}

**S5.3.7**: Four exact integer products of $O(rp)$ bits each, at cost $O(rp\log(rp))$, dominate the linear packing, extraction, combination, wrapping and truncation costs.
Source: "Four exact integer products dominate the linear" (paper)
> Finally the $p$-bit grid numerator of the normalized product is \[ \operatorname{trunc}_0\left(\frac{\Re H_j}{2^{p+\ell}}\right) +i\operatorname{trunc}_0\left(\frac{\Im H_j}{2^{p+\ell}}\right). \] To implement it, shift the absolute magnitude right by $p+\ell$ bits and restore its sign, at cost $O(p)$ per coefficient. The returned coefficient is $2^{-p}$ times this numerator, namely $Q_p(2^{-2p}H_j/r)$; \eqref{eq:transform-truncate} proves its error and disk bounds. Each returned component numerator has magnitude at most $2^p$, so write it as a signed $w$-bit two's-complement word, most significant bit first, with the real word before the imaginary word and coefficient indices in increasing order. This costs $O(rw)=O(rp)$ and supplies the format used by the opposite transform. Four exact integer products dominate the linear packing, extraction, combination, wrapping, and truncation costs. \end{proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md): The ring of complex polynomials of degree < r with y^r = −1, in which multiplying by a power of y permutes the coefficients up to sign, so that powers of y serve as exact roots of unity.
  Shown as: Signed packing of polynomial products *<predicate>* Polynomial ring modulo y^r + 1
- [Established n log n multiplier](established-multiplier.md): The known fixed-tape integer multiplier of Harvey and van der Hoeven running in O(N log N) on N-bit inputs, used here only as an ordinary subroutine on short operands (never recursively on the improved algorithm).
  Shown as: Signed packing of polynomial products *<predicate>* Established n log n multiplier

## Pages that build on this one

- Convolution over the polynomial ring: Normalized convolution on d−1 axes of arrays with entries in C[y]/(y^r+1): two forward synthetic transforms keeping the same frequency order, pointwise polynomial products (by signed packing) divided by r, and the opposite transform, all using the fast layers and chunk swaps.

## Other pages you may link to

- [The n log n conjecture for integer multiplication](integer-multiplication-conjecture.md)
- [Fixed-point disk-grid arithmetic](fixed-point-truncation.md)
- [Arrays, addresses and volume on tapes](tape-address-model.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Controlled cyclic shifts](controlled-shift.md)
- [Rank, subspaces and orthogonal complements](linear-algebra-basics.md)
- [Linear exchange network with restored scratch wires](linear-network.md)
- [Address shear and lower-triangular factorization](address-shear.md)
- [Frames on wire arrays](common-frame-principle.md)
- [Subspace labels from three-element subsets](subset-intersection-labels.md)
- [Recursive rank saving](rank-saving-recurrence.md)
- [Fast address-chunk interchange](address-chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer product as digit convolution](radix-digit-convolution.md)
- [Coefficient (phase) twist](phase-twist.md)
- [Rounding and carry propagation](exact-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Multidimensional (tensor) transform](multidimensional-dft.md)
- [Two-point butterfly](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Phase frames and the two-point kernel C](phase-frame-kernel.md)
- [Fast simultaneous butterfly layer](fast-butterfly-layer.md)
- [Convolution over the polynomial ring](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutations and their cancellation](permutation-cancellation.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Parameter choices and prime source lengths](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the saving κ](time-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The reduction is a signed form of Kronecker substitution" (paper)

  > To multiply the polynomial records, we use the fixed-tape integer multiplier of Harvey and van der Hoeven~\cite[Theorem~1.1]{HarveyHoeven2021}, with cost $O(N\log(2N))$ on $N$-bit inputs. This is an independent subroutine. Its inputs below have $O(rp)$ bits, and we include the conversions between coefficient streams and signed integers in the cost. The reduction is a signed form of Kronecker substitution; compare \cite[Lemma~2.5]{HarveyHoeven2021}. We specify the packing and recovery of coefficients to include negative values and the required tape format.

- "After the lower coefficients have been removed from an evaluation," (paper)

  > ne the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values using the established multiplier and restore each product's sign. The resulting integers are $A_aA_c,A_bA_e,A_aA_e,A_bA_c$. For example, if $h=ac$ is the ordinary product in $\mathbb Z[y]$, then \[ A_aA_c=(ac)(B_0)=\sum_{j=0}^{2r-2}h_jB_0^j. \] The other three evaluation products have the same form. Every coefficient in any of these ordinary polynomial products satisfies \begin{equation} |h_j|\leq r2^{2p}<2^{3p}<B_0/2. \label{eq:packing-separation} \end{equation} After the lower coefficients have been removed from an evaluation, this strict bound identifies the next coefficient by its centered residue modulo $B_0$.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Length

At most 350 words, not counting mathematics and citations: submit rejects a longer page.

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
    "Derivation": {
      "additionalProperties": false,
      "description": "Where the page derives one of the steps the argument gives it.",
      "properties": {
        "quote": {
          "description": "The passage on this page that derives the step, copied exactly: a sentence or more,\noutside citations.",
          "type": "string"
        },
        "step": {
          "description": "The step's id, as listed under \"Steps this page derives\".",
          "type": "string"
        }
      },
      "required": [
        "step",
        "quote"
      ],
      "type": "object"
    },
    "Edge": {
      "additionalProperties": false,
      "description": "What this page uses one prerequisite page for.",
      "properties": {
        "predicate": {
          "description": "A short predicate built from the sentence's own words, such that \"<this page's\nconcept> <predicate> <prerequisite>\" is a true sentence: \"is reduced to\", \"computes\nits transforms by\", \"is based on\".",
          "type": "string"
        },
        "prerequisite": {
          "description": "Id of the prerequisite page.",
          "type": "string"
        },
        "quote": {
          "description": "The sentence on this page that states it, copied exactly. It must link or name the\nprerequisite and contain the predicate's words.",
          "type": "string"
        }
      },
      "required": [
        "prerequisite",
        "predicate",
        "quote"
      ],
      "type": "object"
    },
    "PageBinding": {
      "additionalProperties": false,
      "description": "What a symbol a page introduces denotes, and where the page says so.",
      "properties": {
        "meaning": {
          "description": "One sentence saying what the symbol denotes; for a count, what it counts.",
          "type": "string"
        },
        "name": {
          "description": "Display name of one to four words, e.g. \"record length\".",
          "type": "string"
        },
        "quote": {
          "description": "The sentence on the page that says what the symbol denotes, copied exactly. A use\nin an example (\"take $r = 4$\") does not say what a symbol denotes.",
          "type": "string"
        },
        "relation": {
          "$ref": "#/$defs/Relation"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the page's mathematics, without dollar signs,\ne.g. `r` or `\\kappa`.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "name",
        "meaning",
        "relation",
        "quote"
      ],
      "type": "object"
    },
    "Relation": {
      "oneOf": [
        {
          "const": "direct",
          "description": "The symbol denotes a thing: \"ω, a primitive root of unity\".",
          "type": "string"
        },
        {
          "const": "count",
          "description": "The symbol is the number of instances of something: \"r, the number of complex\ncoefficients in a record\".",
          "type": "string"
        }
      ]
    }
  },
  "additionalProperties": false,
  "description": "The structured part of a write answer; the body is the markdown answer file.",
  "properties": {
    "derivations": {
      "default": [],
      "description": "For each step listed under \"Steps this page derives\", the passage on the page that\nderives it. Empty if the task lists none.",
      "items": {
        "$ref": "#/$defs/Derivation"
      },
      "type": "array"
    },
    "relations": {
      "description": "One relation for each prerequisite page: what this page uses it for. Empty if the\npage has no prerequisite pages.",
      "items": {
        "$ref": "#/$defs/Edge"
      },
      "type": "array"
    },
    "symbols": {
      "description": "Every symbol the page binds: each symbol it introduces and says what it denotes.\nLeave out symbols listed as already bound, unless the page gives them a new meaning.\nEmpty if the page introduces no symbols.",
      "items": {
        "$ref": "#/$defs/PageBinding"
      },
      "type": "array"
    }
  },
  "required": [
    "symbols",
    "relations"
  ],
  "title": "WriteAnswer",
  "type": "object"
}
```

Write the body to `exegenius/tasks/0019-write-signed-packing.answer.md` and the JSON to `exegenius/tasks/0019-write-signed-packing.answer.json`, then run `exegenius submit 0019-write-signed-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0019-write-signed-packing`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
