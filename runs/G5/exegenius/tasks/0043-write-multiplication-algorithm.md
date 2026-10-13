# exegenius task 0043-write-multiplication-algorithm

Project directory: `/home/user/openai-nlogn-wiki/runs/G5` (paths below are relative to it)

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

For these sources: The reader has a standard undergraduate computer science education: discrete mathematics (induction, sums, logarithms, floor and ceiling, functions and bijections, graphs and acyclic circuits), algorithms (divide and conquer, recurrences, sorting in O(n log n), grade-school multiplication and Karatsuba, Newton's method from calculus), and the basic theory of computation with Turing machines and tapes. They know complex numbers, roots of unity, polynomial arithmetic, modular arithmetic and elementary linear algebra, and have seen the FFT as an algorithm. They have not studied abstract algebra beyond modular arithmetic, number theory beyond gcd and inverses, numerical analysis of rounding errors, or any multiplication algorithm beyond the basic ones, so the wiki must explain the Fourier-transform machinery, the polynomial ring, the Harvey-van der Hoeven resampling and the linear-network constructions.

The reader already understands these concepts:

- Big-O notation
- Turing machines with tapes
- Polynomials
- Complex numbers
- Roots of unity
- Modular arithmetic
- Binary integers and XOR
- Basic linear algebra
- Fixed finite-tape Turing machine model
- Optimality conjecture for multiplication (also: n log n conjecture)
- Established n log n multiplier
- Array order and linear-time stream scans
- Controlled cyclic shifts and rational scalings
- Cyclic convolution
- Reducing integer multiplication to digit convolution
- Discrete Fourier transform and convolution theorem (also: Fourier transform, DFT)
- Radix-2 FFT butterflies (also: butterfly, decimation in frequency)
- Multidimensional transforms on power-of-two axes (also: tensor transform)
- Chinese-remainder map onto distinct prime axes (also: Chinese remainder address map)
- Gaussian resampling
- Bluestein chirp identity (also: Bluestein conversion, chirp)
- Resampling with retained permutations
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring)
  - $y$ (ring variable): The formal variable of the polynomials, subject to the relation y^r = −1.
  - $r$ (record length): The number of complex coefficients in one polynomial record, a power of two.
- Synthetic polynomial transform (also: Nussbaumer polynomial transform)
- Retained frequency order of the transforms
- Phase twist to a negacyclic wrap
- Signed Kronecker packing of polynomial products
- Disk-grid fixed-point arithmetic (also: Gaussian dyadics, truncation Q_p)
- Three-element subset gadgets
- Linear bank-exchange network with restored scratch wires
- Frames and the common-frame identity
- Nested subspace labels and orthogonal residuals
- Bit network and its rational matrix interface
- Rank saving of the finite networks (also: recursive saving)
- Two-point phase kernel C
- Binary phase interface of the complex network
- Lower-triangular factorization of a matrix (also: Bruhat factorization)
- Rank-bounded matrix shear on address fields
- Recursive power-width interchange
- Fast address-chunk interchange (also: chunk swap, arbitrary-width interchange)
- Packed selected-bit addition with repair
- Simultaneous butterfly layer (also: fast butterfly layer)
- Transform layout for parallel butterfly rounds
- Convolution from the retained transform layout
- Parameter regime for input length n
- Prime source lengths near powers of two
- Error analysis and exact recovery of the product
- Logarithms, floors and ceilings (also: lg n, log base 2, ceil, floor, rounding up, powers of two)
- Mathematical induction and recurrences (also: induction, recursion, recurrence relation, divide and conquer, recursive calls, master theorem)
- Sorting and permutation of arrays (also: merge sort, sorting in O(n log n), permutation, bijection, bit-reversal permutation)
- Schoolbook multiplication and Karatsuba (also: grade-school multiplication, long multiplication, quadratic multiplication, Karatsuba algorithm, Karatsuba-Ofman, divide-and-conquer multiplication)
- Fast Fourier transform as an algorithm (also: FFT, Cooley-Tukey, fast polynomial multiplication, Schonhage-Strassen)
- Graphs, directed acyclic graphs and circuits (also: DAG, acyclic graph, network of gates, circuit, vertices and edges, wires and gates, graph)
- Calculus and Newton's method (also: Newton iteration, Newton's method, reciprocal and square root by iteration, geometric series, exponential and trigonometric functions, Euler's formula, e^{i theta})
- Vector norms and the triangle inequality (also: sup norm, maximum norm, infinity norm, triangle inequality, absolute value, error bound)
- Primes and trial division (also: prime number, primality testing, trial division, sieve of Eratosthenes, odd primes, coprime)
- Rounding, rational numbers and fixed-point numbers (also: round to nearest integer, truncation, dyadic rational, fixed point, finite precision, rounding error)
- Worst-case time analysis of deterministic algorithms (also: worst-case running time, deterministic algorithm, asymptotic through all input lengths, decision of constants and thresholds, finite lookup table)
- Sets, Cartesian products and indexed arrays (also: Cartesian product, product set, multi-index, tuple, array indexed by tuples, lexicographic order)

## This page

Concept: The multiplication algorithm
Gloss: Digits are placed on prime axes by the CRT map, transformed by resampling, chirp and polynomial-ring convolution, multiplied pointwise, transformed back with the opposite sign, rescaled, rounded and carry-propagated to give the 2n-bit product.

## This page in the argument

The step: The algorithm, with digits placed on prime axes by the Chinese-remainder map, transformed by Gaussian resampling, chirp convolution and polynomial-ring convolution, multiplied pointwise, transformed back, rescaled, rounded and carry-propagated, outputs the exact $2n$-bit product.
How: Reduce the product to a cyclic convolution of digit lists and evaluate it with Fourier transforms, building from the fastest inner primitive (convolution over a polynomial ring) outward through the resampling, prime-axis and twist reductions, then bound the error so that rounding is exact
Why: Splitting into digits turns multiplication into convolution, and convolutions are cheap through transforms, but each transform has the wrong shape for the one below, so each reduction is added around the innermost primitive. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The normalized cyclic convolution $\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays over $\mathcal R_r$ is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda\prime}+\log(rp)])$ time. (on [Convolution from the retained transform layout](ring-convolution.md))
- The source transform $RF_{\boldsymbol s}$ on pairwise coprime axis lengths $s_i$ equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ on power-of-two lengths $t_i$ with both permutations $R,Q$ left inside the formula, the middle transform $QF_{\boldsymbol t}$ is a chirp convolution, and $R$ cancels in a convolution. (on [Resampling with retained permutations](retained-permutations.md))
- All sizes are tied to $b=\lceil\log_2 n\rceil$: $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a padded size $T$ in $[4n/b,8n/b)$ and $r=2^{\lceil\log_2 T/d\rceil}$, so that $Tp=\Theta(n)$ and $r$ exceeds every fixed power of $p$. (on [Parameter regime for input length n](parameter-regime.md))
- Distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ and $\eta=1/(4d)$ are found deterministically, so $S=\prod_i s_i$ lies in $(T/2,T)$ and each ratio $t_i/s_i$ leaves enough separation for Gaussian resampling. (on [Prime source lengths near powers of two](prime-lengths.md))
- Writing each integer as a polynomial in $2^b$ with $q=\lceil n/b\rceil$ digits turns the product into a convolution of digit lists; since the degree is below $S$, convolution modulo $x^S-1$ has no wraparound and each coefficient is below $2^{3b}$. (on [Reducing integer multiplication to digit convolution](radix-digit-reduction.md))
- A ring isomorphism sends the length-$S$ cyclic convolution to a cyclic convolution on the pairwise coprime axes $s_i$, and on tape it is a sequence of triangular controlled shifts costing $O(Tp\,d^2(1+\ell^\tau))$. (on [Chinese-remainder map onto distinct prime axes](crt-prime-axes.md))
- Multiplying coefficient $k$ by $\zeta^k$ with $\zeta=e^{\pi i/r}$ turns convolution modulo $x^r-1$ into convolution modulo $y^r+1$ on the last axis, so the complex cyclic convolution is the synthetic one conjugated by phase twists at cost $O(Tp^{1+\delta})$. (on [Phase twist to a negacyclic wrap](coefficient-twist.md))
- The middle factor $QF_{\boldsymbol t}$ is computed by multiplying by the conjugate chirp, taking the complex convolution with the chirp, and multiplying by the conjugate chirp again, at cost $O(Tdp^{1+\delta})$ for the chirps.
- The source transform expands each axis by $\mathcal A$, applies the chirp transform, compresses by $\mathcal B_0$ and scales by $2^\gamma$, exactly realizing $RF_{\boldsymbol s}$; the opposite-sign transform is obtained by conjugation.
- The algorithm reads radix-$2^b$ digits, places them by $\Phi$, transforms both operands, multiplies pointwise, applies the opposite transform, scales, rounds and propagates carries to give the $2n$-bit product.
- The two scalings by $S$ undo different normalizations: after the three transforms the exact result is $(u*v)/S^2$, and the scalings by $S$ and $2^{2b+4}$ restore the integer coefficient convolution.
- Every call returns disk-grid values with the stated error and norm margins, the final coefficient error is below $1/2$, so rounding gives the exact integer coefficients and carries give the product. (on [Error analysis and exact recovery of the product](precision-recovery.md))

It serves these steps, from the main result down:

- One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Give the multiplication algorithm and show its output is exact, then total its cost stage by stage (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.8, S1.9, S1.10, S1.11). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.8**: The middle factor $QF_{\boldsymbol t}$ is computed by multiplying by the conjugate chirp, taking the complex convolution with the chirp, and multiplying by the conjugate chirp again, at cost $O(Tdp^{1+\delta})$ for the chirps.
Source: "We next use the complex convolution to evaluate the middle factor" (paper)
> We next use the complex convolution to evaluate the middle factor $QF_{\boldsymbol t}$ in \eqref{eq:no-sort-tensor}, and then compose it with the Gaussian maps. For the chirp array $a$ in \eqref{eq:permuted-chirp}, the phase numerator at tensor address $j$ is computed modulo $2r$ as \[ -\sum_i s_i j_i^2(r/t_i)\pmod{2r}. \] All integers have $O(p)$ bits and $r/t_i\in\{1,2\}$. Scan the stored axis descriptors and compute the $d$ squares and products with the previously established integer multiplier. Additions, reductions modulo a power of two, and restarting local counters cost $O(p)$ per term; multiplication costs $O(p\log p)=O(p^{1+\delta})$. Exponential evaluation then has the same $O(p^{1+\delta})$ bound. Thus chirp construction costs $O(Td p^{1+\delta})$ in total. In particular, this cost includes the scan of the axis descriptors at every coefficient.

**S1.9**: The source transform expands each axis by $\mathcal A$, applies the chirp transform, compresses by $\mathcal B_0$ and scales by $2^\gamma$, exactly realizing $RF_{\boldsymbol s}$; the opposite-sign transform is obtained by conjugation.
Source: "For a source disk-grid tensor of norm at most $.5$, write" (paper)
> For a source disk-grid tensor of norm at most $.5$, write $\widetilde{\mathscr F}$ for the following procedure: apply the linewise approximation to $\mathcal A$, apply the computed chirp transform $\widetilde{\mathscr C}$, apply the linewise approximation to $\mathcal B_0$, and multiply the grid numerators exactly by $2^\gamma$. Its exact counterpart is \[ \mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A =RF_{\boldsymbol s}. \] Here an exact counterpart replaces every numerical subroutine by the exact map it approximates and omits truncations. The source arrays are stored in the padded power-of-two box, with zeros outside the valid source coordinates. The compressed scalar output uses $w_{\rm c}$-bit components. Appending $\gamma$ zero bits to each word gives the exact scaled numerator in the known signed width $w_{\rm c}+\gamma$. For the stated input norm, the disk estimate below proves that every scaled coordinate still belongs to $\mathbb D_p$. Its component numerators therefore have magnitude at most $2^p$, so a scan removes only leading sign-extension bits and returns the same integers in $w_{\rm c}$ bits. This scan costs $O(T(w_{\rm c}+\gamma))=O(Tp)$ and leaves the padded zero records zero. Define the opposite-sign procedure by \[ \widetilde{\mathscr F}^{+}(z) =\overline{\widetilde{\mathscr F}(\overline z)}; \] its exact counterpart is $RF_{\boldsymbol s}^{+}$ by Lemma~\ref{lem:chirp-permutation}.

**S1.10**: The algorithm reads radix-$2^b$ digits, places them by $\Phi$, transforms both operands, multiplies pointwise, applies the opposite transform, scales, rounds and propagates carries to give the $2n$-bit product.
Source: "With these streams prepared, perform the following operations." (paper)
> With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the repres

**S1.11**: The two scalings by $S$ undo different normalizations: after the three transforms the exact result is $(u*v)/S^2$, and the scalings by $S$ and $2^{2b+4}$ restore the integer coefficient convolution.
Source: "The two occurrences of $S$ in this algorithm undo different" (paper)
> The two occurrences of $S$ in this algorithm undo different normalizations. By \eqref{eq:source-permutation-cancel}, the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$. The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution. The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$; it also justifies the rounding, carries, and output length.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.1 (on [Convolution from the retained transform layout](ring-convolution.md)): The normalized cyclic convolution $\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays over $\mathcal R_r$ is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda\prime}+\log(rp)])$ time.
- S1.2 (on [Resampling with retained permutations](retained-permutations.md)): The source transform $RF_{\boldsymbol s}$ on pairwise coprime axis lengths $s_i$ equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ on power-of-two lengths $t_i$ with both permutations $R,Q$ left inside the formula, the middle transform $QF_{\boldsymbol t}$ is a chirp convolution, and $R$ cancels in a convolution.
- S1.3 (on [Parameter regime for input length n](parameter-regime.md)): All sizes are tied to $b=\lceil\log_2 n\rceil$: $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a padded size $T$ in $[4n/b,8n/b)$ and $r=2^{\lceil\log_2 T/d\rceil}$, so that $Tp=\Theta(n)$ and $r$ exceeds every fixed power of $p$.
- S1.4 (on [Prime source lengths near powers of two](prime-lengths.md)): Distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ and $\eta=1/(4d)$ are found deterministically, so $S=\prod_i s_i$ lies in $(T/2,T)$ and each ratio $t_i/s_i$ leaves enough separation for Gaussian resampling.
- S1.5 (on [Reducing integer multiplication to digit convolution](radix-digit-reduction.md)): Writing each integer as a polynomial in $2^b$ with $q=\lceil n/b\rceil$ digits turns the product into a convolution of digit lists; since the degree is below $S$, convolution modulo $x^S-1$ has no wraparound and each coefficient is below $2^{3b}$.
- S1.6 (on [Chinese-remainder map onto distinct prime axes](crt-prime-axes.md)): A ring isomorphism sends the length-$S$ cyclic convolution to a cyclic convolution on the pairwise coprime axes $s_i$, and on tape it is a sequence of triangular controlled shifts costing $O(Tp\,d^2(1+\ell^\tau))$.
- S1.7 (on [Phase twist to a negacyclic wrap](coefficient-twist.md)): Multiplying coefficient $k$ by $\zeta^k$ with $\zeta=e^{\pi i/r}$ turns convolution modulo $x^r-1$ into convolution modulo $y^r+1$ on the last axis, so the complex cyclic convolution is the synthetic one conjugated by phase twists at cost $O(Tp^{1+\delta})$.
- S1.12 (on [Error analysis and exact recovery of the product](precision-recovery.md)): Every call returns disk-grid values with the stated error and norm margins, the final coefficient error is below $1/2$, so rounding gives the exact integer coefficients and carries give the product.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Chinese-remainder map onto distinct prime axes](crt-prime-axes.md): A ring isomorphism sends a length-S cyclic convolution to a multidimensional cyclic convolution on pairwise coprime axes s_i; on tape it is a sequence of triangular controlled shifts.
  Shown as: The multiplication algorithm *<predicate>* Chinese-remainder map onto distinct prime axes
- [Resampling with retained permutations](retained-permutations.md): Instead of sorting twice per coordinate, the source and target coordinate permutations stay inside the transform formula R F_s = 2^γ B₀ Q F_t A; the source permutation then cancels across the two forward transforms and the opposite one.
  Shown as: The multiplication algorithm *<predicate>* Resampling with retained permutations
- [Bluestein chirp identity](chirp-identity.md): A phase-weighted identity that rewrites a Fourier transform, including its frequency permutation, as a cyclic convolution with a chirp array a_j = exp(−πi Σ s_i j_i²/t_i) between pointwise phase multiplications.
  Shown as: The multiplication algorithm *<predicate>* Bluestein chirp identity
- [Phase twist to a negacyclic wrap](coefficient-twist.md): Multiplying coefficient k by ζ^k with ζ = e^{πi/r} turns convolution modulo x^r − 1 into convolution modulo y^r + 1 on the last axis, and untwisting restores the cyclic wrap.
  Shown as: The multiplication algorithm *<predicate>* Phase twist to a negacyclic wrap
- [Convolution from the retained transform layout](ring-convolution.md): Two forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform, all in one retained order, give the normalized convolution (f*g)/(rM) over the polynomial ring with explicit error.
  Shown as: The multiplication algorithm *<predicate>* Convolution from the retained transform layout
- [Prime source lengths near powers of two](prime-lengths.md): Distinct odd primes s_i with (1−2η)t_i < s_i ≤ (1−η)t_i are found by deterministic search, so S = ∏s_i lies in (T/2, T) and each ratio t_i/s_i leaves enough separation for Gaussian resampling.
  Shown as: The multiplication algorithm *<predicate>* Prime source lengths near powers of two
- [Parameter regime for input length n](parameter-regime.md): All sizes are tied to b = ⌈log₂ n⌉: precision p = 6b, d = ⌊b^ε⌋ axes, K = ⌊d^c⌋, padded size T about n/b, record length r = 2^{⌈log₂T/d⌉} so that Tp = Θ(n) and r grows faster than any power of p.
  Shown as: The multiplication algorithm *<predicate>* Parameter regime for input length n
- [Error analysis and exact recovery of the product](precision-recovery.md): Every call returns disk-grid values with bounded error and norm margins; after removing the known scales the coefficient error is below 1/2, so rounding gives the exact integer coefficients and carries give the product.
  Shown as: The multiplication algorithm *<predicate>* Error analysis and exact recovery of the product
- [Reducing integer multiplication to digit convolution](radix-digit-reduction.md): Writing each integer as a polynomial in 2^b with b-bit digits turns the product into a convolution of digit lists; padding avoids wraparound, and rounding plus carry propagation recover the bits.
  Shown as: The multiplication algorithm *<predicate>* Reducing integer multiplication to digit convolution

## Pages that build on this one

- Complete time bound and the power saving: Dividing costs by Tp, the seven dominant terms (layout moves, chunk exchanges, butterfly rounds, CRT layouts, Gaussian line maps, chirps, packed products) have exponents at most 1 − 2κ of p, giving O(n (log n)^{1−κ}).
- Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-tape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, beating the n log n conjecture by a power of the logarithm.

## Other pages you may link to

- [Optimality conjecture for multiplication](nlogn-conjecture.md)
- [Cyclic convolution](convolution.md)
- [Disk-grid fixed-point arithmetic](fixed-point-disk.md)
- [Three-element subset gadgets](subset-gadgets.md)
- [Fixed finite-tape Turing machine model](fixed-tape-model.md)
- [Established n log n multiplier](nlogn-multiplier.md)
- [Array order and linear-time stream scans](stream-scans.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Linear bank-exchange network with restored scratch wires](bank-exchange-network.md)
- [Frames and the common-frame identity](frames.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Bit network and its rational matrix interface](bit-network-interface.md)
- [Rank saving of the finite networks](rank-saving.md)
- [Lower-triangular factorization of a matrix](matrix-factorization.md)
- [Rank-bounded matrix shear on address fields](matrix-shear.md)
- [Recursive power-width interchange](power-width-interchange.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Packed selected-bit addition with repair](packed-selected-bit-addition.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring.md)
- [Signed Kronecker packing of polynomial products](signed-packing.md)
- [Discrete Fourier transform and convolution theorem](dft.md)
- [Radix-2 FFT butterflies](fft-butterfly.md)
- [Multidimensional transforms on power-of-two axes](multidimensional-transform.md)
- [Two-point phase kernel C](two-point-kernel.md)
- [Binary phase interface of the complex network](phase-interface.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Retained frequency order of the transforms](stored-frequency-order.md)
- [Transform layout for parallel butterfly rounds](transform-layout.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Complete time bound and the power saving](time-bound.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The source-transform procedures now supply the three transforms needed for the radix-digit convolution." (paper)

  > The source-transform procedures now supply the three transforms needed for the radix-digit convolution. Read each stored operand backward from its least significant end in groups of $b$ bits. This produces the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order. Buffer each group on a fixed work tape and read it back most significant bit first, reversing its least-significant-first input order; pad the final short group with leading zeroes. For digit $a_j$, write the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero $w_{\rm c}$-bit imaginary word. This exponent is nonnegative because $p=6b$, and the represented value is exactly $a_j2^{-b-2}$. Append $S-q$ zero coefficient records. Buffering and ordering the groups costs $O(n)$, including the one partial group's padding, and writing the $S$ records costs $O(Sp)$. Together with the initial count and copies, this input conversion costs $O(n+Sp)=O(Tp)$; all $n$ input bits, including leading zeroes, are retained before the final group is padded.

- "Propagate radix-$2^b$ carries in increasing coefficient order." (paper)

  > exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to the nearest integers. At each valid address, write the rounded coefficient in one signed $(3b+1)$-bit word, most significant bit first; at every padded address, write a zero word of that width. Supply this local payload width to $\Phi^{-1}$ and apply it, including removal of the address padding, to restore the ordinary coefficient order. \item Propagate radix-$2^b$ carries in increasing coefficient order. Write the resulting bits from least to most significant on a work tape, then reverse that stream and output exactly $2n$ bits in most-significant-first order. \end{enumerate}


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

Write the body to `exegenius/tasks/0043-write-multiplication-algorithm.answer.md` and the JSON to `exegenius/tasks/0043-write-multiplication-algorithm.answer.json`, then run `exegenius submit 0043-write-multiplication-algorithm` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0043-write-multiplication-algorithm`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
