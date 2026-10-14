# exegenius task 0036-write-multiplication-algorithm

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F4V` (paths below are relative to it)

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
- Cyclic convolution (also: convolution)
- Discrete Fourier transform (also: Fourier transform, DFT)
- Multidimensional (tensor) transform (also: tensor transform)
- Two-point butterfly (also: H₀, butterfly operation)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring, R_r)
  - $y$ (ring variable): The formal polynomial variable, whose powers y^a act as roots of unity of order 2r.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform (also: Nussbaumer polynomial transform, stored frequency order)
- Signed packing of polynomial products (also: Kronecker substitution)
- Linear exchange network with restored scratch wires (also: bank exchange, finite network, role)
- Frames on wire arrays (also: frame, common-frame identity)
- Subspace labels from three-element subsets (also: rank saving construction, orthogonal residual labels)
- Address shear and lower-triangular factorization (also: Bruhat factorization, matrix shear)
- Recursive rank saving (also: power saving recurrence)
- Fast address-chunk interchange (also: chunk swap, tape interchange)
- Phase frames and the two-point kernel C (also: binary phase interface, C kernel)
- Packed selected-bit addition (also: packed XOR, exceptional address repair)
- Fixed-point disk-grid arithmetic (also: disk grid, Gaussian dyadics, truncation Q_p)
- Fast simultaneous butterfly layer (also: simultaneous normalized butterfly layer)
- Convolution over the polynomial ring (also: synthetic convolution)
- Coefficient (phase) twist (also: twist)
- Bluestein chirp identity (also: chirp identity, chirp transform)
- Gaussian resampling (also: Gaussian gridding, resampling)
- Retained permutations and their cancellation (also: no-sort resampling)
- Chinese-remainder address map (also: CRT map, Agarwal–Cooley map)
- Integer product as digit convolution (also: radix-2^b digits)
- Rounding and carry propagation (also: exact recovery, carry propagation)
- Parameter choices and prime source lengths (also: fixed rational choice)
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

Concept: The multiplication algorithm
Gloss: The pipeline: form radix digits, apply the CRT address map Φ, run two source transforms (resampling plus chirp convolution plus resampling), multiply pointwise, run the opposite transform, rescale, round and propagate carries; inside the chirp convolution the last coordinate is twisted into C[y]/(y^r+1) and convolved with synthetic transforms.
Also called: reduction chain

## This page in the argument

The step: Two $n$-bit integers are multiplied exactly by forming radix-$2^b$ digits, mapping them to prime axes, taking two source transforms, multiplying pointwise, applying the opposite transform, and rescaling, rounding and carrying.
How: chain the reductions digit convolution, prime-axis cyclic convolution, power-of-two axes via resampling and chirps, and ring convolution after a coefficient twist
Why: Each reduction changes the problem into one the next tool handles: carries make multiplication a convolution, CRT makes the long axis a product of coprime axes, resampling and chirps make the transform lengths powers of two, and the twist makes the last axis a negacyclic ring. (the sources say so: "The arrows describe changes of problem and representation. Fast address" (paper))

Its sub-steps, in order:

- Fixed rational exponents, $b=\lceil\log_2 n\rceil$, $p=6b$, $d=\lfloor b^{\epsilon}\rfloor$, a padded size $T\in[4n/b,8n/b)$, axis lengths $t_i\in\{r/2,r\}$ and distinct primes $s_i$ just below $t_i$ with $T/2<S<T$ satisfy all hypotheses of the lemmas. (on [Parameter choices and prime source lengths](parameter-choice.md))
- The integer product is the polynomial product of the radix-$2^b$ digit lists, which has no wraparound modulo $x^S-1$ and coefficients below $2^{3b}$. (on [Integer product as digit convolution](radix-digit-convolution.md))
- The Chinese-remainder map $\Phi:\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$ preserves convolution and is implemented by triangular controlled shifts in $O(Tp\,d^2(1+\ell^{\tau}))$. (on [Chinese-remainder address map](crt-address-map.md))
- The coefficient twist $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ identifies $\mathbb C[x_d]/(x_d^r-1)$ with $\mathbb C[y]/(y^r+1)$, so complex cyclic convolution on $d$ axes is ring convolution on $d-1$ axes after twisting. (on [Coefficient (phase) twist](phase-twist.md))
- The computed chirp transform and the source transform $\widetilde{\mathscr F}=2^{\gamma}\mathcal B_0 QF_{\boldsymbol t}\mathcal A$ approximate $RF_{\boldsymbol s}$ using one complex convolution.
- The pipeline maps digits through $\Phi$, applies two source transforms, multiplies pointwise, applies the opposite transform, rescales and rounds, and its two factors $S$ undo different normalizations.
- The accumulated coefficient error before rounding is below $1/2$, so rounding recovers the exact integer coefficients, and radix-$2^b$ carry propagation yields the $2n$-bit product. (on [Rounding and carry propagation](exact-recovery.md))

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture.; how: reduce integer multiplication to convolution over a polynomial ring, and speed up the data movement and the butterfly layers of its transforms with two new tape procedures that each save a power of the logarithm (on [Integer multiplication below n log n](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (A4, A5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**A4**: The computed chirp transform and the source transform $\widetilde{\mathscr F}=2^{\gamma}\mathcal B_0 QF_{\boldsymbol t}\mathcal A$ approximate $RF_{\boldsymbol s}$ using one complex convolution.
How: form the chirp-weighted convolution of the twisted data with disk-grid chirp values and wrap it in the two resampling maps
- A4a: The chirp transform forms $x_0=Q_p(\overline{\widetilde a}\cdot x)$, convolves it with $\widetilde a$ and multiplies by $\overline{\widetilde a}$ again.
  Source: "x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x)," (paper)
  > Let $\widetilde a$ be the resulting disk-grid array, so $\|\widetilde a-a\|_\infty<2\,2^{-p}$. For a disk-grid target tensor $x$ of norm at most $.6$, the computed chirp transform forms the arrays \[ \begin{aligned} x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),\\ y_0&=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0),\\ \widetilde{\mathscr C}(x) &=Q_p(\overline{\widetilde a}\mathbin{\cdot}y_0). \end{aligned} \] Thus $\widetilde a$ is the convolution kernel and $x_0$ is the data operand after the first endpoint phase. Replacing the approximations by exact phases and exact convolution gives $\overline a\mathbin{\cdot}\mathcal M_{\mathbb C} (a,\overline a\mathbin{\cdot}x)=QF_{\boldsymbol t}x$ by \eqref{eq:permuted-chirp}. Below we show that $\|x\|_\infty\le.6$ implies $\|x_0\|_\infty\le.6$, which supplies the smaller operand required by the computed convolution.
- A4b: The source transform $\widetilde{\mathscr F}$ has exact counterpart $\mathscr F=2^{\gamma}\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.
  Source: "\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A" (paper)
  > For a source disk-grid tensor of norm at most $.5$, write $\widetilde{\mathscr F}$ for the following procedure: apply the linewise approximation to $\mathcal A$, apply the computed chirp transform $\widetilde{\mathscr C}$, apply the linewise approximation to $\mathcal B_0$, and multiply the grid numerators exactly by $2^\gamma$. Its exact counterpart is \[ \mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A =RF_{\boldsymbol s}. \] Here an exact counterpart replaces every numerical subroutine by the exact map it approximates and omits truncations. The source arrays are stored in the padded power-of-two box, with zeros outside the valid source coordinates. The compressed scalar output uses $w_{\rm c}$-bit components. Appending $\gamma$ zero bits to each word gives the exact scaled numerator in the known signed width $w_{\rm c}+\gamma$. For the stated input norm, the disk estimate below proves that every scaled coordinate still belongs to $\mathbb D_p$. Its component numerators therefore have magnitude at most $2^p$, so a scan removes only leading sign-extension bits and returns the same integers in $w_{\rm c}$ bits. This scan costs $O(T(w_{\rm c}+\gamma))=O(Tp)$ and leaves the padded zero records zero. Define the opposite-sign procedure by \[ \widetilde{\mathscr F}^{+}(z) =\overline{\widetilde{\mathscr F}(\overline z)}; \] its exact counterpart is $RF_{\boldsymbol s}^{+}$ by Lemma~\ref{lem:chirp-permutation}.

**A5**: The pipeline maps digits through $\Phi$, applies two source transforms, multiplies pointwise, applies the opposite transform, rescales and rounds, and its two factors $S$ undo different normalizations.
How: execute the pipeline in the order of the reduction and track the normalizing constants
- A5a: Step 1: the coefficient-address map $\Phi$ with padded layout produces source arrays $u,v$ of norm below $1/4$.
  Source: "Apply the coefficient-address map $\Phi$, with its padded layout, to obtain" (paper)
  > With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ ex
- A5b: Step 2: compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.
  Source: "\item Compute $\widetilde{\mathscr F}(u)$ and" (paper)
  > With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to
- A5c: Step 4: compute $\widetilde{\mathscr F}^{+}(z)$ of the truncated pointwise product $z$ and multiply the grid numerators by $S$.
  Source: "\item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid" (paper)
  > With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to the nearest integers. At each valid address, write the rounded coefficient in one signed $(3b+1)$-bit word, most significant bit first; at every padded address, write a zero word of that width. Supply this local payload width to $\Phi^{-1}$ and apply it, including removal of the address padding, to restore the ordinary coefficien
- A5d: Step 5: multiply exactly by $2^{2b+4}S$, round to integers, and apply $\Phi^{-1}$ to restore ordinary coefficient order.
  Source: "\item Multiply the grid numerators of $\widetilde w$ exactly by" (paper)
  > ficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to the nearest integers. At each valid address, write the rounded coefficient in one signed $(3b+1)$-bit word, most significant bit first; at every padded address, write a zero word of that width. Supply this local payload width to $\Phi^{-1}$ and apply it, including removal of the address padding, to restore the ordinary coefficient order. \item Propagate radix-$2^b$ carries in increasing coefficient order. Write the resulting bits from least to most significant on a work tape, then reverse that stream and output exactly $2n$ bits in most-significant-first order. \
- A5e: The first $S$ turns $(u*v)/S^2$ into $w=(u*v)/S$ and the second $S$ with $2^{2b+4}$ gives the original integer coefficient convolution.
  Source: "The two occurrences of $S$ in this algorithm undo different" (paper)
  > The two occurrences of $S$ in this algorithm undo different normalizations. By \eqref{eq:source-permutation-cancel}, the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$. The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution. The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$; it also justifies the rounding, carries, and output length.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- A0 (on [Parameter choices and prime source lengths](parameter-choice.md)): Fixed rational exponents, $b=\lceil\log_2 n\rceil$, $p=6b$, $d=\lfloor b^{\epsilon}\rfloor$, a padded size $T\in[4n/b,8n/b)$, axis lengths $t_i\in\{r/2,r\}$ and distinct primes $s_i$ just below $t_i$ with $T/2<S<T$ satisfy all hypotheses of the lemmas.
- A1 (on [Integer product as digit convolution](radix-digit-convolution.md)): The integer product is the polynomial product of the radix-$2^b$ digit lists, which has no wraparound modulo $x^S-1$ and coefficients below $2^{3b}$.
- A2 (on [Chinese-remainder address map](crt-address-map.md)): The Chinese-remainder map $\Phi:\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$ preserves convolution and is implemented by triangular controlled shifts in $O(Tp\,d^2(1+\ell^{\tau}))$.
- A3 (on [Coefficient (phase) twist](phase-twist.md)): The coefficient twist $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ identifies $\mathbb C[x_d]/(x_d^r-1)$ with $\mathbb C[y]/(y^r+1)$, so complex cyclic convolution on $d$ axes is ring convolution on $d-1$ axes after twisting.
- A6 (on [Rounding and carry propagation](exact-recovery.md)): The accumulated coefficient error before rounding is below $1/2$, so rounding recovers the exact integer coefficients, and radix-$2^b$ carry propagation yields the $2n$-bit product.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Fixed-point disk-grid arithmetic](fixed-point-truncation.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Integer product as digit convolution](radix-digit-convolution.md): Writing each n-bit input as a polynomial in 2^b with ⌈n/b⌉ digits, the integer product is the polynomial product, whose coefficients are below 2^{3b}; with enough zero padding the cyclic convolution has no wraparound, and carries recover the bits.
  Shown as: The multiplication algorithm *<predicate>* Integer product as digit convolution
- [Chinese-remainder address map](crt-address-map.md): The Agarwal–Cooley isomorphism Φ: C[x]/(x^S−1) → C[x₁..x_d]/(x_i^{s_i}−1), x ↦ ∏ x_i^{μ_i}, for pairwise coprime (prime) s_i with S = ∏ s_i, which turns one long cyclic convolution into one on distinct prime axes and is implemented by triangular controlled shifts.
  Shown as: The multiplication algorithm *<predicate>* Chinese-remainder address map
- [Gaussian resampling](gaussian-resampling.md): The Harvey–van der Hoeven reduction that expresses a Fourier transform of length s (here a prime) through a power-of-two transform of length t>s via Gaussian-weighted contractions: P_s F_s = 2^{2α²} B₀ P_t F_t A, with the two coordinate permutations P_s,P_t left inside the identity.
  Shown as: The multiplication algorithm *<predicate>* Gaussian resampling
- [Retained permutations and their cancellation](permutation-cancellation.md): Instead of executing the source and target coordinate permutations of Gaussian resampling as sorts, they stay in the transform formula; the source permutation R cancels across the two forward transforms, the pointwise product and the opposite transform: RF⁺[(RFu)(RFv)] = (u*v)/S².
  Shown as: The multiplication algorithm *<predicate>* Retained permutations and their cancellation
- [Bluestein chirp identity](bluestein-chirp.md): Writing a (permuted) transform as a chirp-weighted cyclic convolution QF_t u = ā · (a * (ā · u))/T with a_j = exp(−πi Σ s_i j_i²/t_i), so a Fourier transform with its target permutation becomes a normalized convolution.
  Shown as: The multiplication algorithm *<predicate>* Bluestein chirp identity
- [Coefficient (phase) twist](phase-twist.md): The map x_d ↦ ζy with ζ = e^{πi/r} that sends the cyclic last coordinate C[x_d]/(x_d^r−1) isomorphically to C[y]/(y^r+1) by multiplying coefficient k by ζ^k, so the negative wrap of the ring becomes the original cyclic wrap after untwisting.
  Shown as: The multiplication algorithm *<predicate>* Coefficient (phase) twist
- [Convolution over the polynomial ring](ring-convolution.md): Normalized convolution on d−1 axes of arrays with entries in C[y]/(y^r+1): two forward synthetic transforms keeping the same frequency order, pointwise polynomial products (by signed packing) divided by r, and the opposite transform, all using the fast layers and chunk swaps.
  Shown as: The multiplication algorithm *<predicate>* Convolution over the polynomial ring
- [Rounding and carry propagation](exact-recovery.md): The final steps that rescale by known factors (S, 2^{2b+4}), prove the accumulated coefficient error is below 1/2 so rounding gives the exact integer coefficients, and propagate radix-2^b carries to produce the 2n-bit product.
  Shown as: The multiplication algorithm *<predicate>* Rounding and carry propagation
- [Parameter choices and prime source lengths](parameter-choice.md): The size parameters b=⌈log₂n⌉, precision p=6b, number of axes d=⌊b^ε⌋, chunk width K=⌊d^c⌋, padded size T≈n/b, power-of-two axis lengths t_i∈{r/2,r}, and distinct primes s_i just below t_i with T/2 < ∏s_i < T, chosen so resampling hypotheses and all tape lemmas apply.
  Shown as: The multiplication algorithm *<predicate>* Parameter choices and prime source lengths

## Pages that build on this one

- Cost accounting and the saving κ: Dividing every cost by V = Tp = Θ(n) gives a table of seven dominant powers of p (layout moves, chunk exchanges, simultaneous butterfly rounds, CRT layout, Gaussian line maps, chirps, packed products), each at most 1−2κ with κ = 2^{−182}, giving total O(n (lg n)^{1−κ}).
- Integer multiplication below n log n: A single deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, disproving the n log n optimality conjecture; it works by reducing to convolution, using fast address interchange and fast simultaneous butterfly layers to save a power of the logarithm.

## Other pages you may link to

- [The n log n conjecture for integer multiplication](integer-multiplication-conjecture.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md)
- [Fixed-point disk-grid arithmetic](fixed-point-truncation.md)
- [Established n log n multiplier](established-multiplier.md)
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
- [Signed packing of polynomial products](signed-packing.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](dft.md)
- [Multidimensional (tensor) transform](multidimensional-dft.md)
- [Two-point butterfly](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Phase frames and the two-point kernel C](phase-frame-kernel.md)
- [Fast simultaneous butterfly layer](fast-butterfly-layer.md)
- [Cost accounting and the saving κ](time-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "With these streams prepared, perform the following operations." (paper)

  > With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the repres

- "The two occurrences of $S$ in this algorithm undo different" (paper)

  > The two occurrences of $S$ in this algorithm undo different normalizations. By \eqref{eq:source-permutation-cancel}, the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$. The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution. The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$; it also justifies the rounding, carries, and output length.


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

Write the body to `exegenius/tasks/0036-write-multiplication-algorithm.answer.md` and the JSON to `exegenius/tasks/0036-write-multiplication-algorithm.answer.json`, then run `exegenius submit 0036-write-multiplication-algorithm` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0036-write-multiplication-algorithm`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
