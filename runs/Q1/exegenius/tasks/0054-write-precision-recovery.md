# exegenius task 0054-write-precision-recovery

Project directory: `/home/user/openai-nlogn-wiki/runs/Q1` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, binomial counting, permutations, induction, graphs, the union bound, and elementary number theory with gcd, primes, modular inverses and the Chinese remainder theorem), an algorithms course (asymptotic notation, recurrences and geometric sums, divide and conquer including Karatsuba, sorting including radix sort, stacks, amortized counters, the RAM model and worst-case running time), and an introductory theory course with Turing machines and multitape tapes. From computer organization they know binary and two's-complement encodings, bit order, XOR and binary arithmetic; from calculus and a first linear-algebra course they know logarithms, exponentials, Newton's method, simple inequalities, complex numbers with conjugates, polynomials, matrices, Gaussian elimination, rank, dot products, projections and eigenvalues over the real or rational numbers. They have not studied abstract algebra (rings, quotient rings, finite fields, tensor products, bilinear forms over 𝔽₂), Fourier analysis, numerical error analysis, or the research literature on fast integer multiplication, so the FFT machinery, resampling and all of the paper's constructions are new to them.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine (also: fixed finite-tape model)
- Modular arithmetic and finite fields (also: F_2, residue ring)
- Linear maps, matrices and rank (also: rational rank)
- Tensor products (also: tensor power)
- Nondegenerate bilinear forms and orthogonal complements (also: orthogonal complement, orthonormal basis)
- The n log n conjecture (also: Schönhage–Strassen conjecture, n log n optimality conjecture)
- Harvey–van der Hoeven O(n log n) multiplier (also: established multiplier)
- Cyclic convolution
- Normalized discrete Fourier transform (also: DFT, normalized Fourier transform, multidimensional transform)
- Radix-digit reduction (also: radix-digit polynomials, carry propagation)
- Lexicographic array layout and logical volume (also: address field, logical volume, row)
- Elementary stream operations
- Controlled shifts and rational scalings (also: prefix-controlled cyclic shift, triangular update)
- Gaussian dyadic fixed-point arithmetic (also: disk grid, Q_p truncation, Gaussian dyadics)
- Contractions and error accounting
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring, R_r)
  - $y$ (polynomial variable): The indeterminate of the ring, whose powers act as roots of unity of order 2r.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Normalized butterfly H₀ (also: butterfly, Hadamard butterfly)
  - $H_0$ (normalized butterfly): The 2×2 matrix ½[[1, 1], [1, −1]] sending a pair (u, v) to ((u + v)/2, (u − v)/2).
- Two-point kernel C (also: translation kernel, aI+bX)
  - $C$ (two-point kernel): The 2×2 complex matrix aI + bX with a = (1 + i)/2, b = (1 − i)/2 and X the coordinate swap.
- Linear network with wire roles (also: role, wire, gate, scalar network)
- Restoring scratch values (also: transparent computation, scratch wires)
- Three-element subset construction (also: Frankl–Wilson construction, triple indicators)
- Three-stage bank exchange (also: gather, scatter, side injection, forward invocation)
- Frames and the common-frame identity (also: frame, endpoint operator)
- Nested subspace labels and orthogonal residuals (also: label, orthogonal residual, dimension loss)
- Rank deficit s < Wm (also: rank saving, relative rank deficit)
  - $s$ (number of smaller calls): The total number of smaller recursive calls the network's edges require, summed over all edges.
  - $W$ (wire count): The number of wires (roles) in the finite network, including scratch wires.
  - $m$ (label dimension): The dimension of the label space, which is the factor by which each smaller call shrinks the recursion parameter.
- Rational matrix interface of the bit network
- Binary phase interface of the complex network (also: phase frame, complex network)
- Address shear
- Lower triangular (Bruhat) factorization
- Matrix shear by rank-many interchanges
- Row splitting among wire roles
- Volume-normalized recursion and the power saving (also: recursive saving)
- Fixed-tape depth-first schedule (also: parking stack)
- Power-width interchange
- Fast address-chunk interchange (also: chunk swap, address interchange, arbitrary-width interchange)
- Packed selected-bit addition (also: binary change of basis, deterministic repair, guard values)
- Recursive C-layer via phase frames
- Simultaneous butterfly layer (also: parallel butterfly layer, normalized butterfly layer)
- Synthetic polynomial transform (also: Nussbaumer transform, decimation in frequency, bit-reversed order)
- Transform layout and cost
- Signed Kronecker packing (also: Kronecker substitution)
- Ring convolution from the retained layout (also: normalized convolution, synthetic convolution)
- Coefficient twist (also: phase twist)
- Gaussian resampling
- Resampling with retained permutations
- Tensor resampling interface
- Bluestein's chirp identity (also: chirp transform, chirp)
- Source permutation cancellation
- Computed source transform
- Chinese-remainder convolution map (also: Agarwal–Cooley map, CRT map)
- Size parameters and prime source lengths (also: fixed rational choice, prime source lengths)
- Binary representation of integers (also: base-2 representation, bin_k, val, positional notation, radix-2^b digits)
- Two's-complement representation (also: two's complement, signed w-bit word, sign extension)
- Bit order and endianness (also: most significant bit first, least significant bit first, MSB first, LSB first)
- Bitwise exclusive or (also: XOR, ⊕, bitwise operations)
- Hamming weight (also: wt, popcount, number of ones)
- Logarithms and exponent rules (also: log, log₂, lg, natural logarithm)
- Floor, ceiling and rounding (also: ⌊x⌋, ⌈x⌉, nearest integer, truncation toward zero)
- Worst-case running time (also: time complexity, T_A(n), worst-case cost)
- RAM model of computation (also: unit-cost RAM, random-access machine, word RAM)
- Recurrences and recursion trees (also: recurrence relation, divide and conquer, master theorem, unrolling a recurrence)
- Geometric series (also: geometric sum, Σ a^j)
- Telescoping sums (also: telescoping)
- Karatsuba multiplication (also: Karatsuba–Ofman algorithm, n^{log₂ 3} multiplication)
- Stacks (also: LIFO, push and pop, call stack)
- Binary counter and amortized increment cost (also: binary counter, amortized analysis, ripple counting)
- Radix sort and stable sorting (also: stable sort, LSD radix sort, binary radix sort)
- Row-major order and matrix transposition (also: row-major layout, transpose)
- Directed graphs (also: vertices and edges, head and tail of an edge, path)
- Sets, Cartesian products and indicator vectors (also: [a] = {0,…,a−1}, Cartesian product, characteristic vector, indicator vector, subset intersection)
- Binomial coefficients (also: n choose k, C(n,k))
- Permutations and cycle notation (also: bijection, involution, cycle (a b c), inverse permutation)
- Union bound (also: Boole's inequality, counting bad cases)
- Greatest common divisor and Euclid's algorithm (also: gcd, coprime, relatively prime, extended Euclidean algorithm, modular inverse)
- Prime numbers and trial division (also: primes, primality testing by trial division, odd prime)
- Chinese remainder theorem (also: CRT)
- Matrix operations (also: identity matrix, diagonal matrix, permutation matrix, triangular matrix, lower triangular, block diagonal, direct sum of maps)
- Gaussian elimination (also: row reduction, elementary row operations, row addition, row swap, pivot)
- Dot product and orthogonality (also: inner product, x·y, orthogonal vectors)
- Projection onto a subspace (also: projection matrix, P_U)
- Eigenvalues of a matrix (also: eigenvalue, eigenvector)
- Complex conjugate (also: conjugation, z̄)
- Triangle inequality (also: |a + b| ≤ |a| + |b|)
- Bernoulli's inequality (also: (1 + x)^n ≥ 1 + nx)
- Newton's method (also: Newton iteration, Newton–Raphson)
- Proof by induction (also: induction, inductive invariant, loop invariant)

## This page

Concept: Precision analysis and exact recovery
Gloss: The error bookkeeping showing that after undoing the normalizations S and the digit scales, every recovered convolution coefficient is within 1/2 of the true integer, so rounding and carry propagation give the exact product.

## This page in the argument

The step: Every recovered convolution coefficient is within less than $1/2$ of the true integer, so rounding gives the exact coefficients and carry propagation gives exactly the $2n$-bit product.
How: Track absolute errors through every stage, using that contractions do not amplify errors, that bilinear contractions add the errors of their operands, and that every computed array keeps a disk margin; then undo the scales and propagate carries.
Why: A linear contraction propagates an input error without increasing it, so the error of the whole pipeline is a sum of the stage errors, scaled only by the known exact normalizations. (the sources say so: "A linear contraction propagates an input error without increasing it." (paper))
Striking feature: Although every transform is computed only approximately with $O(\log n)$-bit numbers, the accumulated error ends strictly below $1/2$, so the output is exact. (explain why it holds, from the method)

Its sub-steps, in order:

- The returned ring convolution has error below $E_{\rm ring}=M(3L+2)<5TL$ and keeps the disk margin $\|\cdot\|<.701$.
- The computed chirp transform has error below $8TL\,2^{-p}$ against $QF_{\boldsymbol t}x$.
- The computed source transform has error below $E_s2^{-p}$ with $E_s=9\cdot2^\gamma TL$.
- The truncated pointwise product $z$ satisfies $\|z-U\cdot V_1\|<(2E_s+2)2^{-p}$.
- After both scalings the final error is below $448b\,2^{-3b/4}<1/2$, so the nearest integer is the correct coefficient.
- Radix-$2^b$ carry propagation in increasing index fixes the radix digits of the full product one by one.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet, fixed-tape Turing machine computes the exact $2n$-bit product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ conjecture in this model.; how: Reduce the product to radix-digit convolution, move it by a Chinese-remainder map, Gaussian resampling, chirps and a phase twist to convolution over $\mathbb C[y]/(y^r+1)$ computed by synthetic transforms; speed up the transforms' address movement and butterfly layers with two network-based tape procedures; then prove exact recovery and total the costs. (on [Integer multiplication in O(n (lg n)^{1−κ}) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S12.1, S12.2, S12.3, S12.4, S12.5, S12.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S12.1**: The returned ring convolution has error below $E_{\rm ring}=M(3L+2)<5TL$ and keeps the disk margin $\|\cdot\|<.701$.
Source: "Thus the error of the returned normalized
convolution is bounded by" (paper)
> For disk-grid ring arrays $f,g$, put $M=T/r$. Two normalized synthetic forwards, pointwise polynomial multiplication divided by $r$, and the normalized opposite transform give $(f*g)/(rM^2)$. The exact multiplication by $M$ in Proposition~\ref{prop:synthetic-convolution} then gives $\mathcal M_r(f,g)=(f*g)/T$. Before that multiplication, the three transform errors and the polynomial-product truncation total less than $3L+2$. Thus the error of the returned normalized convolution is bounded by \[ E_{\rm ring}:=M(3L+2)<5TL. \] If one operand has norm at most $.7$, bilinear contraction gives $\|\mathcal M_r(f,g)\|\le.7$. Its computed grid output consequently has norm less than $.7+5TLh_p<.701$ for large $n$. This proves the disk margin after the scale $M$, without clipping the output.

**S12.2**: The computed chirp transform has error below $8TL\,2^{-p}$ against $QF_{\boldsymbol t}x$.
Source: "Equation~\eqref{eq:permuted-chirp} identifies the exact result, so" (paper)
> For its error, the exact operands $a$ and $\overline a\cdot x$ are in the disk because every entry of $a$ has modulus one. The kernel approximation contributes less than $2$ and the first endpoint multiplication contributes less than $4$ when inserted into the exact bilinear contraction $\mathcal M_{\mathbb C}$. The computed convolution contributes less than $6TL$, and the last endpoint multiplication less than $4$. Equation~\eqref{eq:permuted-chirp} identifies the exact result, so \[ \|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\| <(6TL+2+4+4)h_p<8TLh_p. \]

**S12.3**: The computed source transform has error below $E_s2^{-p}$ with $E_s=9\cdot2^\gamma TL$.
Source: "because $2dp^2<TL$ eventually." (paper)
> Finally let the input to a source transform have norm at most $.5$. The computed expansion has error less than $dp^2$ and norm less than $.5+dp^2h_p<.51$. It is therefore a permitted chirp input. The chirp output is in the disk by the preceding argument, so each compression call is defined and returns another disk-grid array. Insert the exact contractions $\mathcal A$, $QF_{\boldsymbol t}$, and $\mathcal B_0$ at the computed inputs. The error before the source scale is less than $2dp^2+8TL$. Multiplication by $2^\gamma$ therefore gives error less than $2^\gamma(2dp^2+8TL)h_p$, which is bounded by $E_sh_p$ with \begin{equation}\label{eq:source-error} E_s=9\,2^\gamma TL, \end{equation} because $2dp^2<TL$ eventually. The exact source transform $RF_{\boldsymbol s}$ is a contraction, so the scaled approximation has norm at most $.5+E_sh_p<.501$. Its exact numerator scaling therefore also leaves a disk-grid output without clipping. Conjugation preserves the grid and norm, so the opposite procedure has the same error and disk guarantee. All these margins may be enforced by one fixed cutoff. For example, $b\ge2^{24}$, together with the other eventual construction conditions, makes $dp^2h_p$, $8TLh_p$, $E_sh_p$ and $28\,2^\gamma T^2Lh_p$ smaller than $10^{-3}$.

**S12.4**: The truncated pointwise product $z$ satisfies $\|z-U\cdot V_1\|<(2E_s+2)2^{-p}$.
Source: "Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$." (paper)
> The scaled radix digits in $u,v$ are exact $p$-bit grid values of norm strictly less than $1/4$. Put \[ \begin{aligned} U&=RF_{\boldsymbol s}u,&\qquad V_1&=RF_{\boldsymbol s}v,\\ \widetilde U&=\widetilde{\mathscr F}(u),& \widetilde V_1&=\widetilde{\mathscr F}(v). \end{aligned} \] The exact arrays have norm less than $1/4$, and the computed arrays have norm less than $1/4+E_sh_p<.26$. Hence $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has norm at most $.26^2<.5$. To estimate its error, write \[ \widetilde U\cdot\widetilde V_1-U\cdot V_1 =(\widetilde U-U)\cdot\widetilde V_1 +U\cdot(\widetilde V_1-V_1). \] The factors $\widetilde V_1$ and $U$ are in the disk. The two terms have total norm less than $2E_sh_p$, and truncation adds less than $2h_p$. Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$.

**S12.5**: After both scalings the final error is below $448b\,2^{-3b/4}<1/2$, so the nearest integer is the correct coefficient.
Source: "The strict error below $1/2$ makes the nearest integer to
that value the unique correct coefficient." (paper)
> In tensor order, the unscaled integer coefficient array is $2^{2b+4}S w$. This second occurrence of $S$ reverses the normalization still present in $w$, and $2^{2b+4}$ reverses the two input scales. Both multiplications act exactly on grid numerators. Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than \begin{equation}\label{eq:final-error} 2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b} <448b\,2^{-b+\gamma} \le448b\,2^{-3b/4}<\frac12. \end{equation} The true coefficients are real integers. If $H_j$ is the real numerator after the second scaling, its represented value is $H_j/2^p$. The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.

**S12.6**: Radix-$2^b$ carry propagation in increasing index fixes the radix digits of the full product one by one.
Source: "The unprocessed terms are multiples of $Q_0^j$, so the identity fixes
the first $j$ radix digits of the full product." (paper)
> To propagate carries, let $Q_0=2^b$. The recovered ordinary coefficients are the $c_j$ in \eqref{eq:capacity}; they are zero for $2q-2<j<S$. With $q=\lceil n/b\rceil$ as above, use the recurrence for $0\le j<S$: \[ k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad k_{j+1}=\left\lfloor\frac{c_j+k_j}{Q_0}\right\rfloor. \] The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$. If this holds at $j$, then \[ c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1), \] which proves the next carry bound. The defining relation $c_j+k_j=d_j+Q_0k_{j+1}$ also gives the exact invariant \[ \sum_{h<j}c_hQ_0^h =\sum_{h<j}d_hQ_0^h+k_jQ_0^j. \] It holds for $j=0$, and the defining relation proves its next instance. The unprocessed terms are multiples of $Q_0^j$, so the identity fixes the first $j$ radix digits of the full product. The value $k_j$ is the carry from the processed coefficients into the remaining positions.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Contractions and error accounting](contraction-errors.md): Linear maps of operator norm at most one do not amplify errors, so errors of approximate algorithms for contractions (and bilinear contractions) simply add when composed.
  Shown as: Precision analysis and exact recovery *<predicate>* Contractions and error accounting
- [Computed source transform](source-transform.md): The procedure approximating RF_s on the prime-axis array by composing the Gaussian expansion A, the chirp transform (via twisted ring convolution), the compression B₀, and an exact scale 2^γ.
  Shown as: Precision analysis and exact recovery *<predicate>* Computed source transform
- [Source permutation cancellation](source-perm-cancel.md): The identity RF⁺[(RFu)·(RFv)] = (u ∗ v)/S², showing that the source permutation R kept from resampling cancels between the two forward transforms and the opposite transform.
  Shown as: Precision analysis and exact recovery *<predicate>* Source permutation cancellation
- [Radix-digit reduction](radix-reduction.md): Writing each n-bit input as a polynomial in 2ᵇ with b-bit digits, so the product is recovered from the integer convolution of the digit lists followed by carry propagation.
  Shown as: Precision analysis and exact recovery *<predicate>* Radix-digit reduction
- [Size parameters and prime source lengths](parameters.md): The choices b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, power-of-two box T ≈ 4n/b split into d axes of length r or r/2, distinct odd primes sᵢ just below each tᵢ, and the fixed rational exponents ending in κ = 2^{−182}.
  Shown as: Precision analysis and exact recovery *<predicate>* Size parameters and prime source lengths

## Pages that build on this one

- Integer multiplication in O(n (lg n)^{1−κ}) time: One deterministic fixed-alphabet, fixed-tape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n·(lg n)^{1−κ}) worst-case time with κ = 2^{−182}, disproving the n log n conjecture in that model.

## Other pages you may link to

- [The n log n conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Polynomial ring modulo yʳ + 1](negacyclic-ring.md)
- [Normalized butterfly H₀](normalized-butterfly.md)
- [Gaussian dyadic fixed-point arithmetic](fixed-point.md)
- [Signed Kronecker packing](signed-packing.md)
- [Lexicographic array layout and logical volume](array-layout.md)
- [Elementary stream operations](elementary-streams.md)
- [Modular arithmetic and finite fields](modular-arithmetic.md)
- [Address shear](address-shear.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Linear maps, matrices and rank](linear-algebra.md)
- [Linear network with wire roles](linear-network.md)
- [Row splitting among wire roles](row-splitting.md)
- [Frames and the common-frame identity](frames.md)
- [Restoring scratch values](scratch-restoration.md)
- [Lower triangular (Bruhat) factorization](bruhat.md)
- [Nondegenerate bilinear forms and orthogonal complements](bilinear-forms.md)
- [Three-element subset construction](triple-construction.md)
- [Three-stage bank exchange](bank-exchange.md)
- [Tensor products](tensor-product.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank deficit s < Wm](rank-deficit.md)
- [Volume-normalized recursion and the power saving](power-saving-recursion.md)
- [Rational matrix interface of the bit network](bit-interface.md)
- [Matrix shear by rank-many interchanges](matrix-shear.md)
- [Fixed-tape depth-first schedule](fixed-tape-schedule.md)
- [Power-width interchange](power-width-interchange.md)
- [Fast address-chunk interchange](chunk-swap.md)
- [Two-point kernel C](kernel-c.md)
- [Binary phase interface of the complex network](phase-interface.md)
- [Packed selected-bit addition](packed-addition.md)
- [Recursive C-layer via phase frames](recursive-c-layer.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Chinese-remainder convolution map](crt-map.md)
- [Normalized discrete Fourier transform](dft.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein's chirp identity](bluestein.md)
- [Resampling with retained permutations](resampling-retained.md)
- [Transform layout and cost](transform-layout.md)
- [Ring convolution from the retained layout](synthetic-convolution.md)
- [Coefficient twist](coefficient-twist.md)
- [Tensor resampling interface](tensor-resampling.md)
- [Cost table and the exponent κ](cost-accounting.md)
- [Integer multiplication in O(n (lg n)^{1−κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient." (paper)

  > In tensor order, the unscaled integer coefficient array is $2^{2b+4}S w$. This second occurrence of $S$ reverses the normalization still present in $w$, and $2^{2b+4}$ reverses the two input scales. Both multiplications act exactly on grid numerators. Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than \begin{equation}\label{eq:final-error} 2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b} <448b\,2^{-b+\gamma} \le448b\,2^{-3b/4}<\frac12. \end{equation} The true coefficients are real integers. If $H_j$ is the real numerator after the second scaling, its represented value is $H_j/2^p$. The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.

- "proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product." (paper)

  > Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform. Section~\ref{sec:assembly} removes the known normalizations and digit scales, proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product. A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}. Figure~\ref{fig:multiplication-flow} summarizes these reductions.


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

Write the body to `exegenius/tasks/0054-write-precision-recovery.answer.md` and the JSON to `exegenius/tasks/0054-write-precision-recovery.answer.json`, then run `exegenius submit 0054-write-precision-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0054-write-precision-recovery`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
