# exegenius task 0038-write-multiplication-algorithm

Project directory: `/home/user/openai-nlogn-wiki/runs/G2` (paths below are relative to it)

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

For these sources: Undergraduate computer science: algorithms and complexity through big-O analysis, recurrences and divide-and-conquer (Karatsuba, FFT-based polynomial multiplication, usually met at the level of the standard recursive FFT), discrete mathematics (modular arithmetic, primes and gcd, sets, functions and permutations, induction), and introductory linear algebra (matrices, rank, bases, inner products, Gaussian elimination, over the reals and probably F_2). Also the basics of complex numbers and Turing machines with multiple tapes. The reader has not studied abstract algebra such as quotient rings or tensor products, finite-field theory beyond F_2, numerical analysis of rounding errors, or the research literature on integer multiplication (Schönhage–Strassen, Fürer, Harvey–van der Hoeven), and has not seen Bluestein, Nussbaumer polynomial transforms or Gaussian resampling.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Bit XOR
- The n log n conjecture and prior bounds (also: Schönhage–Strassen conjecture)
- Arrays as tape streams and elementary scans
- Controlled shifts and rational scalings
- Fixed-point and Gaussian dyadic arithmetic
- Discrete Fourier transform
- Cyclic convolution
- Multiplication as convolution of radix digits
- Multidimensional transform
- Chinese-remainder address map (also: Φ)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Two-point butterfly layer (also: butterfly, H₀)
- Synthetic polynomial transform (also: Nussbaumer polynomial transform)
- Signed packing for ring products
- The established O(N log N) multiplier
- Subspaces, bilinear forms and orthogonal complements
- Linear network with restored scratch wires (also: motif network, restoration schedule)
- Triple-subset intersection gadgets
- Frames on wire arrays
- Nested subspace labels and the rank deficit (also: s<Wm)
- Recursive power saving from the rank deficit
- Lower triangular factorization
- Matrix shear on address fields
- Fast interchange of address chunks
- Binary phase frames and the two-point kernel C
- Packed selected-bit addition
- Simultaneous butterfly layer
- Synthetic transform tape layout
- Normalized convolution over the ring
- Last-coordinate phase twist
- Gaussian resampling
- Resampling with permutations left in the transform
- Bluestein chirp identity
- Error bounds and exact recovery
- Parameter choice and cost table
- Asymptotic notation beyond big-O (also: Omega notation, Theta notation, little-o, Ω, Θ, o(n log n))
- Logarithms and binary logarithm (also: lg, log base 2, log_2, ceiling of log)
- Floor and ceiling functions (also: floor, ceiling, ⌊x⌋, ⌈x⌉, integer part)
- Binary representation of integers (also: n-bit integer, bit string, binary expansion, two's complement, signed binary)
- Radix representation and digits (also: base-b expansion, positional notation, radix digits, leading zeroes)
- Schoolbook multiplication and carries (also: grade-school multiplication, long multiplication, quadratic multiplication, carry propagation, addition with carry)
- Divide-and-conquer and recurrences (also: recurrence relation, master theorem, Karatsuba multiplication, recursion, geometric series, geometric sum)
- Fast Fourier transform and FFT multiplication (also: FFT, Cooley-Tukey, radix-2 FFT, O(n log n) polynomial multiplication, evaluation and interpolation)
- Mathematical induction and proof by cases (also: induction, inductive proof, proof by contradiction)
- Sets, subsets and Cartesian products (also: set intersection, cardinality, subset of size three, product set, tuples, indicator vector)
- Functions, bijections and permutations (also: permutation, bijection, inverse function, composition, involution, partial permutation)
- Modular arithmetic and congruences (also: mod, residues, congruence, ℤ/nℤ, integers modulo n, remainder, units modulo n)
- Primes, divisibility and coprimality (also: gcd, greatest common divisor, relatively prime, prime power, coprime, trial division, prime factorization)
- Rational numbers and exact fractions (also: rationals, ℚ, denominator, numerator, dyadic rational)
- Finite fields and the field F_2 (also: GF(2), 𝔽_2, binary field, arithmetic modulo 2, parity)
- Vectors, matrices and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, identity matrix, linear transformation, diagonal matrix, linear combination)
- Rank, basis and dimension (also: linear independence, span, vector space, subspace dimension, rank of a matrix, rank-nullity)
- Gaussian elimination (also: row reduction, row operations, elementary matrices, triangular matrix, lower triangular, upper triangular)
- Inner product, norm and orthonormal basis (also: dot product, orthogonal vectors, orthonormal, unit vector, vector norm, max norm, sup norm, l-infinity norm, unit disk, absolute value of complex number, modulus)
- Roots of unity and Euler's formula (also: e^{iθ}, primitive root of unity, n-th roots of unity, unit circle, geometric series of roots)
- Summation and product notation (also: sigma notation, Σ, Π, indices, Kronecker delta)
- Newton's method (also: Newton iteration, Newton-Raphson, reciprocal by Newton, square root by Newton, quadratic convergence)
- Integer division with remainder (also: quotient and remainder, floor division, integer square root, division algorithm)
- Lexicographic order (also: dictionary order, row-major order, most significant first, mixed radix address)
- Arrays, records and matrix transposition (also: row-major, column-major, transpose, matrix layout, indexing)
- Turing machine running time and model conventions (also: worst-case time, time complexity, unit-cost RAM, random access machine, input and output tapes, finite alphabet, tape heads, scanning and sorting on tapes, linear-time scan, simulation)

## This page

Concept: The multiplication algorithm
Gloss: Digit extraction, the Chinese-remainder map, two forward source transforms, pointwise product, opposite transform, rescaling, rounding and carry propagation yielding the exact 2n-bit product.

## This page in the argument

The step: The procedure that extracts radix-$2^b$ digits, applies the Chinese-remainder address map $\Phi$, computes two forward source transforms, a pointwise product and the opposite transform with exact rescalings, rounds, and propagates carries outputs the exact $2n$-bit product.
How: Choose the parameters, place the digits on a product of distinct prime cyclic axes by the Chinese-remainder map, compute the cyclic convolution through resampled transforms in which the middle transform is a chirp convolution evaluated over the polynomial ring after a phase twist, undo the known normalizations, bound the error below $1/2$, round, and propagate carries.
Why: The remaining proof places the fast tape procedures inside the multiplication reduction and accounts for every change of representation. (the sources say so: "The remaining proof places these procedures inside the multiplication" (paper))

Its sub-steps, in order:

- With fixed rational exponents $\tau=\sigma=1-2^{-50}$, $\epsilon=2^{-75}$, $\kappa=2^{-182}$ and sizes $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$ and $r=2^{\lceil\log_2T/d\rceil}$, every layer and resampling hypothesis holds, $T p=\Theta(n)$, every cost term is a power of $p$ below one, and there are distinct odd primes $s_i$ just below the axis lengths $t_i\in\{r/2,r\}$ with $T/2<S<T$ for $S=\prod_i s_i$. (on [Parameter choice and cost table](parameter-choice.md))
- With $P_i=\prod_{j<i}s_j$ and $\mu_i=P_i^{-1}\bmod s_i$, the map $\Phi:x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\ldots,x_d]/(x_i^{s_i}-1)$ that turns cyclic convolution of length $S$ into convolution on the product of cyclic axes, and it and its inverse are implemented by triangular controlled shifts in time $O(T p\,d^2(1+\ell^\tau))$. (on [Chinese-remainder address map](crt-address-map.md))
- The map $\Theta:x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ is a norm-preserving algebra isomorphism from $\mathbb C[x_d]/(x_d^r-1)$ onto $\mathbb C[y]/(y^r+1)$, diagonal in the coefficient bases, so a cyclic wrap on the last axis becomes a negacyclic wrap and back. (on [Last-coordinate phase twist](phase-twist.md))
- Normalized complex cyclic convolution on the power-of-two axes is $D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$, obtained from the ring convolution with twists applied linewise.
- The chirp transform $\overline{\widetilde a}\cdot\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,\overline{\widetilde a}\cdot x)$ evaluates $QF_{\boldsymbol t}x$ by a chirp multiplication, a complex convolution with the chirp kernel and a second chirp multiplication.
- The source transform applies the Gaussian expansion $\mathcal A$, the chirp transform, the Gaussian compression $\mathcal B_0$ and an exact scaling by $2^\gamma$, and has exact counterpart $RF_{\boldsymbol s}$.
- The procedure applies $\Phi$, two source transforms, a pointwise product truncated to $p$ fractional bits, the opposite source transform scaled by $S$, a second scaling by $2^{2b+4}S$, rounding, $\Phi^{-1}$ and carry propagation, and outputs exactly $2n$ bits.
- By the permutation-cancellation identity the exact result of the three transforms is $(u*v)/S^2$, so the first scale by $S$ gives $(u*v)/S$ and the second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the integer coefficient convolution.
- Every computed step approximates a contraction with bounded error and every scaling is known, so the recovered coefficients lie within error less than $1/2$ of the true integers, rounding to the nearest integer gives them exactly, and carry propagation gives the exact $2n$-bit product. (on [Error bounds and exact recovery](error-and-exact-recovery.md))

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a convolution over a polynomial ring computed by Fourier-type transforms; supply the two fast tape procedures that remove the logarithmic factor from address movement and from butterfly arithmetic, both obtained from linear networks that save a power; then assemble the algorithm and tally every cost. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S7.4, S7.5, S7.6, S7.7, S7.7b). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S7.4**: Normalized complex cyclic convolution on the power-of-two axes is $D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$, obtained from the ring convolution with twists applied linewise.
Source: "The linewise extension of $\Theta$ is $\iota D_+$, with inverse" (paper)
> negacyclic reduction has factor \[ \zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j. \] Untwisting therefore recovers the cyclic coefficient with the correct sign. We next specify how this linewise map meets the ring-convolution interface. Put $M=\prod_{i<d}t_i=T/r$. For a complex array $f$ on $\prod_{i=1}^d\mathbb Z/t_i\mathbb Z$, with $t_d=r$, define \[ (\iota f)_{\boldsymbol j} =\sum_{k=0}^{r-1}f_{\boldsymbol j,k}y^k, \qquad \boldsymbol j\in\prod_{i<d}\mathbb Z/t_i\mathbb Z. \] This identifies the scalar tensor with an array of $M$ records in $\mathcal R$. As maps of values, $\iota$ and $\iota^{-1}$ preserve norms and grids. Write $(D_\pm f)_{\boldsymbol j,k}=\zeta^{\pm k}f_{\boldsymbol j,k}$. The linewise extension of $\Theta$ is $\iota D_+$, with inverse $D_-\iota^{-1}$. Consequently, with $\mathcal M_r$ from Section~\ref{sec:exact-ring-products}, normalized complex cyclic convolution is \[ \mathcal M_{\mathbb C}(f,g) :=D_-\iota^{-1} \mathcal M_r(\iota D_+f,\iota D_+g) =\frac{f*g}{T}. \] Here $\mathcal M_r$ convolves the first $d-1$ axes over $\mathcal R$, whereas $*$ on the right convolves all $d$ scalar axes. The division by $T$ is already part of $\mathcal M_r$. The maps $D_\pm$ and $\iota^{\pm1}$ are isometries, so $\mathcal M_{\mathbb C}$ is also a bilinear contraction.

**S7.5**: The chirp transform $\overline{\widetilde a}\cdot\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,\overline{\widetilde a}\cdot x)$ evaluates $QF_{\boldsymbol t}x$ by a chirp multiplication, a complex convolution with the chirp kernel and a second chirp multiplication.
Source: "$x$ of norm at most $.6$, the computed chirp transform forms the arrays" (paper)
> Let $\widetilde a$ be the resulting disk-grid array, so $\|\widetilde a-a\|_\infty<2\,2^{-p}$. For a disk-grid target tensor $x$ of norm at most $.6$, the computed chirp transform forms the arrays \[ \begin{aligned} x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),\\ y_0&=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0),\\ \widetilde{\mathscr C}(x) &=Q_p(\overline{\widetilde a}\mathbin{\cdot}y_0). \end{aligned} \] Thus $\widetilde a$ is the convolution kernel and $x_0$ is the data operand after the first endpoint phase. Replacing the approximations by exact phases and exact convolution gives $\overline a\mathbin{\cdot}\mathcal M_{\mathbb C} (a,\overline a\mathbin{\cdot}x)=QF_{\boldsymbol t}x$ by \eqref{eq:permuted-chirp}. Below we show that $\|x\|_\infty\le.6$ implies $\|x_0\|_\infty\le.6$, which supplies the smaller operand required by the computed convolution.

**S7.6**: The source transform applies the Gaussian expansion $\mathcal A$, the chirp transform, the Gaussian compression $\mathcal B_0$ and an exact scaling by $2^\gamma$, and has exact counterpart $RF_{\boldsymbol s}$.
Source: "For a source disk-grid tensor of norm at most $.5$, write" (paper)
> For a source disk-grid tensor of norm at most $.5$, write $\widetilde{\mathscr F}$ for the following procedure: apply the linewise approximation to $\mathcal A$, apply the computed chirp transform $\widetilde{\mathscr C}$, apply the linewise approximation to $\mathcal B_0$, and multiply the grid numerators exactly by $2^\gamma$. Its exact counterpart is \[ \mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A =RF_{\boldsymbol s}. \] Here an exact counterpart replaces every numerical subroutine by the exact map it approximates and omits truncations. The source arrays are stored in the padded power-of-two box, with zeros outside the valid source coordinates. The compressed scalar output uses $w_{\rm c}$-bit components. Appending $\gamma$ zero bits to each word gives the exact scaled numerator in the known signed width $w_{\rm c}+\gamma$. For the stated input norm, the disk estimate below proves that every scaled coordinate still belongs to $\mathbb D_p$. Its component numerators therefore have magnitude at most $2^p$, so a scan removes only leading sign-extension bits and returns the same integers in $w_{\rm c}$ bits. This scan costs $O(T(w_{\rm c}+\gamma))=O(Tp)$ and leaves the padded zero records zero. Define the opposite-sign procedure by \[ \widetilde{\mathscr F}^{+}(z) =\overline{\widetilde{\mathscr F}(\overline z)}; \] its exact counterpart is $RF_{\boldsymbol s}^{+}$ by Lemma~\ref{lem:chirp-permutation}.

**S7.7**: The procedure applies $\Phi$, two source transforms, a pointwise product truncated to $p$ fractional bits, the opposite source transform scaled by $S$, a second scaling by $2^{2b+4}S$, rounding, $\Phi^{-1}$ and carry propagation, and outputs exactly $2n$ bits.
Source: "With these streams prepared, perform the following operations." (paper)
> With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the repres

**S7.7b**: By the permutation-cancellation identity the exact result of the three transforms is $(u*v)/S^2$, so the first scale by $S$ gives $(u*v)/S$ and the second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the integer coefficient convolution.
Source: "The two occurrences of $S$ in this algorithm undo different" (paper)
> The two occurrences of $S$ in this algorithm undo different normalizations. By \eqref{eq:source-permutation-cancel}, the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$. The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution. The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$; it also justifies the rounding, carries, and output length.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S7.1 (on [Parameter choice and cost table](parameter-choice.md)): With fixed rational exponents $\tau=\sigma=1-2^{-50}$, $\epsilon=2^{-75}$, $\kappa=2^{-182}$ and sizes $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$ and $r=2^{\lceil\log_2T/d\rceil}$, every layer and resampling hypothesis holds, $T p=\Theta(n)$, every cost term is a power of $p$ below one, and there are distinct odd primes $s_i$ just below the axis lengths $t_i\in\{r/2,r\}$ with $T/2<S<T$ for $S=\prod_i s_i$.
- S7.2 (on [Chinese-remainder address map](crt-address-map.md)): With $P_i=\prod_{j<i}s_j$ and $\mu_i=P_i^{-1}\bmod s_i$, the map $\Phi:x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\ldots,x_d]/(x_i^{s_i}-1)$ that turns cyclic convolution of length $S$ into convolution on the product of cyclic axes, and it and its inverse are implemented by triangular controlled shifts in time $O(T p\,d^2(1+\ell^\tau))$.
- S7.3 (on [Last-coordinate phase twist](phase-twist.md)): The map $\Theta:x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ is a norm-preserving algebra isomorphism from $\mathbb C[x_d]/(x_d^r-1)$ onto $\mathbb C[y]/(y^r+1)$, diagonal in the coefficient bases, so a cyclic wrap on the last axis becomes a negacyclic wrap and back.
- S7.8 (on [Error bounds and exact recovery](error-and-exact-recovery.md)): Every computed step approximates a contraction with bounded error and every scaling is known, so the recovered coefficients lie within error less than $1/2$ of the true integers, rounding to the nearest integer gives them exactly, and carry propagation gives the exact $2n$-bit product.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Gaussian resampling](gaussian-resampling.md)
- [Parameter choice and cost table](parameter-choice.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Multiplication as convolution of radix digits](multiplication-as-convolution.md): Splitting both integers into radix-2^b digits makes the product a convolution of the digit coefficient lists, followed by carry propagation.
  Shown as: The multiplication algorithm *<predicate>* Multiplication as convolution of radix digits
- [Chinese-remainder address map](crt-address-map.md): An algebra isomorphism Φ sending x to Π x_i^{μ_i} that turns cyclic convolution of length S=Πs_i (pairwise coprime) into convolution on the product of cyclic axes, implemented by triangular controlled shifts.
  Shown as: The multiplication algorithm *<predicate>* Chinese-remainder address map
- [Bluestein chirp identity](bluestein-chirp.md): A Fourier transform (with its permutation) rewritten as a pointwise chirp multiplication, a cyclic convolution with the chirp, and another chirp multiplication; the source permutation cancels across the product of two transforms.
  Shown as: The multiplication algorithm *<predicate>* Bluestein chirp identity
- [Last-coordinate phase twist](phase-twist.md): The isomorphism x_d→ζy, ζ=e^{πi/r}, from ℂ[x_d]/(x_d^r−1) to ℂ[y]/(y^r+1) that turns cyclic wrap into negacyclic wrap and back.
  Shown as: The multiplication algorithm *<predicate>* Last-coordinate phase twist
- [Normalized convolution over the ring](synthetic-convolution.md): Convolution of arrays over ℂ[y]/(y^r+1) as inverse transform of the pointwise product of forward transforms in the same frequency order, scaled by 1/T, with polynomial products done by signed packing.
  Shown as: The multiplication algorithm *<predicate>* Normalized convolution over the ring
- [Error bounds and exact recovery](error-and-exact-recovery.md): Contraction-based accumulation of approximation errors through all steps, removal of known normalizations and scales, showing the coefficient error is below 1/2 so rounding gives exact integers.
  Shown as: The multiplication algorithm *<predicate>* Error bounds and exact recovery
- [Resampling with permutations left in the transform](resampling-without-sorting.md): The identity P_s F_s = 2^{2α²} B₀ P_t F_t A (and its tensor form) keeping both coordinate permutations inside the formula instead of sorting twice on each coordinate.
  Shown as: The multiplication algorithm *<predicate>* Resampling with permutations left in the transform

## Pages that build on this one

- Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic multitape Turing machine multiplying two n-bit integers in O(n(lg n)^{1−κ}) time with κ=2^{−182}, refuting the n log n optimality conjecture in this model.

## Other pages you may link to

- [The n log n conjecture and prior bounds](nlogn-conjecture.md)
- [Linear network with restored scratch wires](linear-network.md)
- [Frames on wire arrays](frames.md)
- [Arrays as tape streams and elementary scans](tape-streams.md)
- [Fixed-point and Gaussian dyadic arithmetic](fixed-point-dyadics.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Subspaces, bilinear forms and orthogonal complements](linear-algebra-orthogonality.md)
- [Triple-subset intersection gadgets](triple-subset-gadgets.md)
- [Nested subspace labels and the rank deficit](rank-deficit-labels.md)
- [Recursive power saving from the rank deficit](recursive-power-saving.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Matrix shear on address fields](matrix-shear.md)
- [Fast interchange of address chunks](fast-chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](ring-mod-y-r-plus-1.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly layer](two-point-butterfly.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [The established O(N log N) multiplier](nlogn-multiplier.md)
- [Binary phase frames and the two-point kernel C](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Synthetic transform tape layout](synthetic-transform-layout.md)
- [Signed packing for ring products](kronecker-packing.md)
- [Parameter choice and cost table](parameter-choice.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "\item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain" (paper)

  > With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$

- "The source-transform procedures now supply the three transforms needed" (paper)

  > The source-transform procedures now supply the three transforms needed for the radix-digit convolution. Read each stored operand backward from its least significant end in groups of $b$ bits. This produces the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order. Buffer each group on a fixed work tape and read it back most significant bit first, reversing its least-significant-first input order; pad the final short group with leading zeroes. For digit $a_j$, write the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero $w_{\rm c}$-bit imaginary word. This exponent is nonnegative because $p=6b$, and the represented value is exactly $a_j2^{-b-2}$. Append $S-q$ zero coefficient records. Buffering and ordering the groups costs $O(n)$, including the one partial group's padding, and writing the $S$ records costs $O(Sp)$. Together with the initial count and copies, this input conversion costs $O(n+Sp)=O(Tp)$; all $n$ input bits, including leading zeroes, are retained before the final group is padded.


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

Write the body to `exegenius/tasks/0038-write-multiplication-algorithm.answer.md` and the JSON to `exegenius/tasks/0038-write-multiplication-algorithm.answer.json`, then run `exegenius submit 0038-write-multiplication-algorithm` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0038-write-multiplication-algorithm`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
