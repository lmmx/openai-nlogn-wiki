# exegenius task 0038-write-source-transform

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F2B` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: fluent in asymptotic analysis, discrete mathematics (sets, functions, modular arithmetic, primes and gcd, permutations, induction and recursion), first-course linear algebra (matrices, invertibility, rank, basis, dimension, linear maps over the rationals and the complex numbers), complex arithmetic with Euler's formula, and the basic Turing machine model with tapes and step counting. They have seen binary representation, bit operations such as XOR, and perhaps the idea of multiplying integers by divide and conquer, but have not been taught the discrete Fourier transform, the FFT, polynomial transforms, Schönhage–Strassen, abstract ring theory beyond the basic definition, tensor products, or numerical error analysis, and these are what the wiki must explain.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- The n log n optimality conjecture
- Fixed finite-tape Turing machine model
- Arrays, address fields and elementary scans
- Controlled cyclic shifts and rational scalings
- Integer multiplication as digit convolution
- Normalized DFT and cyclic convolution
- Multidimensional (tensor) Fourier transform
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Fixed-point disk-grid arithmetic and contractions
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): the formal variable of the polynomials, subject to y^r = -1.
  - $r$ (record length): the number of complex coefficients in a polynomial record, a power of two.
- Synthetic Fourier transform modulo y^r + 1
  - $y$ (ring variable): the formal variable of the polynomial ring, subject to y^r = -1.
  - $r$ (record length): the number of complex coefficients in a polynomial record, a power of two.
- Radix-2 butterfly layers and stored frequency order
- Twist from cyclic to negacyclic convolution
- Established n log n multiplier as a subroutine
- Signed Kronecker packing of polynomial products
- Bluestein's chirp identity
- Resampling with the permutations left in the transform
- Chirp identity and source-permutation cancellation
- Three-element subset intersection gadget
- Linear network that exchanges two banks and restores scratch values
- Frames and the common-frame identity
- Orthogonal complements and projections in a bilinear space
- Nested subspace labels and the rank saving
- Lower-triangular rank factorization
- Cost of a rational matrix shear
- Power-width chunk interchange in O(Ve^τ) time
  - $V$ (stored bit volume): the number of data bits stored in the array.
  - $e$ (chunk width): the number of radix digits in each of the two interchanged chunks, a power of a fixed integer m.
  - $\tau$ (interchange exponent): a fixed rational constant strictly between 0 and 1.
- Chunk interchange in O(Vu^τ) time
  - $V$ (stored bit volume): the number of data bits stored in the array.
  - $u$ (chunk width): the number of bits in each of the two interchanged address chunks.
  - $\tau$ (interchange exponent): a fixed rational constant strictly below 1, namely 1 - 2^{-50}.
- Two-point kernel C and the complex phase network
- Packed XOR of selected bits across address chunks
- Simultaneous butterfly layer in O(Vd^λ') time
  - $V$ (stored bit volume): the number of data bits stored in the array of records.
  - $d$ (axis count): the number of equal-width address chunks (transform axes) whose selected bit is butterflied simultaneously.
  - $\lambda'$ (layer exponent): a fixed rational constant strictly below 1, namely 1 - 2^{-54}.
- Layout and cost of the synthetic transform
- Convolution over the polynomial ring from the retained layout
- Choice of sizes, precision and prime axis lengths
- Modular arithmetic and residues (also: congruence, mod q, Z/qZ, integers modulo q, remainder)
- Primes, divisibility, gcd and coprimality (also: prime number, coprime, relatively prime, pairwise coprime, greatest common divisor, odd prime, units mod q, invertible residue)
- Binary representation of integers (also: bit string, radix 2, binary expansion, most significant bit, val(x), bin_k(z), padding with zeros, base-2 digits)
- Bitwise XOR (also: exclusive or, XOR combination, addition mod 2, parity)
- Logarithms, floors, ceilings and powers of two (also: lg, log base 2, floor, ceiling, power of two, exponent rules)
- Matrices, invertibility and rank (also: invertible matrix, matrix inverse, matrix product, rank of a matrix, linear map, linear transformation, Gaussian elimination, row operations)
- Vector spaces, basis and dimension (also: subspace, span, linear independence, linear combination, vector space over the rationals, dimension, standard basis, direct sum)
- Permutations and permutation matrices (also: bijection, reordering of indices, sorting by a permutation, permutation of coordinates, identity matrix)
- Lexicographic order and index tuples (also: dictionary order, Cartesian product of index sets, multi-index, mixed-radix positional notation, row-major order)
- Euler's formula and roots of unity as points on the unit circle (also: e^{i theta}, cos and sin form, unit circle, primitive root of unity, modulus of a complex number, complex conjugate, real and imaginary parts)
- Geometric series and orthogonality of sums of roots of unity (also: geometric sum, sum of powers of a root of unity vanishes, summation manipulation, Kronecker delta, indicator function)
- Norms and the triangle inequality (also: absolute value bound, sup norm, maximum norm, Euclidean norm, error bound, triangle inequality, operator norm)
- Rational numbers, dyadic rationals and exact arithmetic (also: dyadic number, dyadic rational, power-of-two denominator, Gaussian rational, Gaussian integer, rounding to nearest integer, truncation toward zero)
- Algebraic structures: groups, rings and isomorphisms (also: ring, commutative ring, algebra, ring isomorphism, group, cyclic group, zero divisor, unit, field)
- Discrete-math proof techniques (also: induction, recursion, recurrence relation, divide and conquer, proof by cases, pigeonhole principle, counting arguments)
- Schoolbook multiplication and divide-and-conquer multiplication (also: long multiplication, quadratic-time multiplication, Karatsuba, carry propagation, digit-by-digit addition)
- Multitape machine cost model and linear-time scans (also: sequential tape access, tape scan, head movement cost, one-pass copy, linear-time tape operations, sorting by merging, bit-level time complexity)
- Complex polynomial evaluation and interpolation (also: evaluating a polynomial at points, coefficient list, degree, polynomial identity, Horner's rule, coefficient extraction)
- Gaussian function (also: bell curve, exp(-x^2), normal density, Gaussian weight)
- Convolution as polynomial multiplication (also: convolution of sequences, sum over i+j=k, linear convolution, Cauchy product, coefficient of a product)
- Quantifiers, sets and basic asymptotic notation beyond big-O (also: little-o, Theta, Omega, sufficiently large n, for all n, worst-case time, lower bound versus upper bound)

## This page

Concept: Source transform via resampling, chirp and ring convolution
Gloss: The computed procedure for a source Fourier transform of prime lengths: Gaussian maps A, then a chirp transform evaluated by a twisted ring convolution, then B₀ and an exact power-of-two scale, with exact counterpart R F_s.

## This page in the argument

The step: A source Fourier transform of prime lengths is computed by Gaussian maps $\mathcal A$, a chirp transform evaluated by a twisted ring convolution, $\mathcal B_0$ and an exact scale $2^\gamma$, with exact counterpart $RF_{\boldsymbol s}$.
How: Compose the computed Gaussian expansion, the chirp transform (a convolution with the chirp array between two phase multiplications, computed by the twisted ring convolution), the Gaussian compression, and the power-of-two scale.
Why: The prime-length transform has no fast algorithm itself; resampling reduces it to a power-of-two tensor transform whose middle factor is a convolution, which is exactly what the ring convolution computes. (the sources say so: "We next use the complex convolution to evaluate the middle factor" (paper))

Its sub-steps, in order:

- Normalized complex convolution of arrays on the power-of-two axes is $D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$.
- Replacing approximations by exact phases and convolution, the computed chirp transform has exact counterpart $QF_{\boldsymbol t}x$.
- The computed source transform has exact counterpart $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.
- Conjugating input and output gives the opposite-sign procedure with exact counterpart $RF^+_{\boldsymbol s}$.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.; how: Start from the Gaussian-resampling reduction of integer multiplication to convolution; replace the two costly operations of the synthetic transforms (address rearrangement and butterfly layers) by faster procedures built from one recursive linear-network exchange, assemble the exact algorithm, and account for its cost. (on [Multiplying n-bit integers in O(n (lg n)^(1−κ)) time](main-theorem.md))
- The multiplication algorithm, run on $x\#y$, outputs exactly the $2n$-bit product of the two $n$-bit integers.; how: Split the inputs into radix digits, map them by $\Phi$ to prime axes, take two source transforms, multiply pointwise, apply the opposite-sign transform with two rescalings by $S$, round, undo $\Phi$ and propagate carries. (on [The multiplication algorithm](multiplication-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S7.4.1, S7.4.2, S7.4.3, S7.4.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S7.4.1**: Normalized complex convolution of arrays on the power-of-two axes is $D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$.
Source: "\mathcal M_r(\iota D_+f,\iota D_+g)" (paper)
> Put $M=\prod_{i<d}t_i=T/r$. For a complex array $f$ on $\prod_{i=1}^d\mathbb Z/t_i\mathbb Z$, with $t_d=r$, define \[ (\iota f)_{\boldsymbol j} =\sum_{k=0}^{r-1}f_{\boldsymbol j,k}y^k, \qquad \boldsymbol j\in\prod_{i<d}\mathbb Z/t_i\mathbb Z. \] This identifies the scalar tensor with an array of $M$ records in $\mathcal R$. As maps of values, $\iota$ and $\iota^{-1}$ preserve norms and grids. Write $(D_\pm f)_{\boldsymbol j,k}=\zeta^{\pm k}f_{\boldsymbol j,k}$. The linewise extension of $\Theta$ is $\iota D_+$, with inverse $D_-\iota^{-1}$. Consequently, with $\mathcal M_r$ from Section~\ref{sec:exact-ring-products}, normalized complex cyclic convolution is \[ \mathcal M_{\mathbb C}(f,g) :=D_-\iota^{-1} \mathcal M_r(\iota D_+f,\iota D_+g) =\frac{f*g}{T}. \] Here $\mathcal M_r$ convolves the first $d-1$ axes over $\mathcal R$, whereas $*$ on the right convolves all $d$ scalar axes. The division by $T$ is already part of $\mathcal M_r$. The maps $D_\pm$ and $\iota^{\pm1}$ are isometries, so $\mathcal M_{\mathbb C}$ is also a bilinear contraction.

**S7.4.2**: Replacing approximations by exact phases and convolution, the computed chirp transform has exact counterpart $QF_{\boldsymbol t}x$.
Source: "(a,\overline a\mathbin{\cdot}x)=QF_{\boldsymbol t}x$ by" (paper)
> Let $\widetilde a$ be the resulting disk-grid array, so $\|\widetilde a-a\|_\infty<2\,2^{-p}$. For a disk-grid target tensor $x$ of norm at most $.6$, the computed chirp transform forms the arrays \[ \begin{aligned} x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),\\ y_0&=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0),\\ \widetilde{\mathscr C}(x) &=Q_p(\overline{\widetilde a}\mathbin{\cdot}y_0). \end{aligned} \] Thus $\widetilde a$ is the convolution kernel and $x_0$ is the data operand after the first endpoint phase. Replacing the approximations by exact phases and exact convolution gives $\overline a\mathbin{\cdot}\mathcal M_{\mathbb C} (a,\overline a\mathbin{\cdot}x)=QF_{\boldsymbol t}x$ by \eqref{eq:permuted-chirp}. Below we show that $\|x\|_\infty\le.6$ implies $\|x_0\|_\infty\le.6$, which supplies the smaller operand required by the computed convolution.

**S7.4.3**: The computed source transform has exact counterpart $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.
Source: "\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A" (paper)
> For a source disk-grid tensor of norm at most $.5$, write $\widetilde{\mathscr F}$ for the following procedure: apply the linewise approximation to $\mathcal A$, apply the computed chirp transform $\widetilde{\mathscr C}$, apply the linewise approximation to $\mathcal B_0$, and multiply the grid numerators exactly by $2^\gamma$. Its exact counterpart is \[ \mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A =RF_{\boldsymbol s}. \] Here an exact counterpart replaces every numerical subroutine by the exact map it approximates and omits truncations. The source arrays are stored in the padded power-of-two box, with zeros outside the valid source coordinates. The compressed scalar output uses $w_{\rm c}$-bit components. Appending $\gamma$ zero bits to each word gives the exact scaled numerator in the known signed width $w_{\rm c}+\gamma$. For the stated input norm, the disk estimate below proves that every scaled coordinate still belongs to $\mathbb D_p$. Its component numerators therefore have magnitude at most $2^p$, so a scan removes only leading sign-extension bits and returns the same integers in $w_{\rm c}$ bits. This scan costs $O(T(w_{\rm c}+\gamma))=O(Tp)$ and leaves the padded zero records zero. Define the opposite-sign procedure by \[ \widetilde{\mathscr F}^{+}(z) =\overline{\widetilde{\mathscr F}(\overline z)}; \] its exact counterpart is $RF_{\boldsymbol s}^{+}$ by Lemma~\ref{lem:chirp-permutation}.

**S7.4.4**: Conjugating input and output gives the opposite-sign procedure with exact counterpart $RF^+_{\boldsymbol s}$.
Source: "its exact counterpart is $RF_{\boldsymbol s}^{+}$ by" (paper)
> For a source disk-grid tensor of norm at most $.5$, write $\widetilde{\mathscr F}$ for the following procedure: apply the linewise approximation to $\mathcal A$, apply the computed chirp transform $\widetilde{\mathscr C}$, apply the linewise approximation to $\mathcal B_0$, and multiply the grid numerators exactly by $2^\gamma$. Its exact counterpart is \[ \mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A =RF_{\boldsymbol s}. \] Here an exact counterpart replaces every numerical subroutine by the exact map it approximates and omits truncations. The source arrays are stored in the padded power-of-two box, with zeros outside the valid source coordinates. The compressed scalar output uses $w_{\rm c}$-bit components. Appending $\gamma$ zero bits to each word gives the exact scaled numerator in the known signed width $w_{\rm c}+\gamma$. For the stated input norm, the disk estimate below proves that every scaled coordinate still belongs to $\mathbb D_p$. Its component numerators therefore have magnitude at most $2^p$, so a scan removes only leading sign-extension bits and returns the same integers in $w_{\rm c}$ bits. This scan costs $O(T(w_{\rm c}+\gamma))=O(Tp)$ and leaves the padded zero records zero. Define the opposite-sign procedure by \[ \widetilde{\mathscr F}^{+}(z) =\overline{\widetilde{\mathscr F}(\overline z)}; \] its exact counterpart is $RF_{\boldsymbol s}^{+}$ by Lemma~\ref{lem:chirp-permutation}.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Bluestein's chirp identity](bluestein-chirp.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Resampling with the permutations left in the transform](resampling-no-sort.md): The tensor form of Gaussian resampling in which the source and target coordinate permutations R and Q stay inside the transform identity, so they need not be executed as separate sorts.
  Shown as: Source transform via resampling, chirp and ring convolution *<predicate>* Resampling with the permutations left in the transform
- [Chirp identity and source-permutation cancellation](chirp-permutation-cancel.md): A chirp-convolution formula for Q·F_t that leaves the target permutation unexecuted, together with the fact that the source permutation R cancels across the two forward transforms, the pointwise product and the opposite transform.
  Shown as: Source transform via resampling, chirp and ring convolution *<predicate>* Chirp identity and source-permutation cancellation
- [Convolution over the polynomial ring from the retained layout](ring-convolution.md): Normalized convolution of arrays over the ring modulo y^r + 1: two forward synthetic transforms, pointwise ring products by signed packing, then the opposite transform consuming the same frequency order, with error O(M ℓ 2^{-p}).
  Shown as: Source transform via resampling, chirp and ring convolution *<predicate>* Convolution over the polynomial ring from the retained layout
- [Twist from cyclic to negacyclic convolution](coefficient-twist.md): Multiplying coefficient k by ζ^k with ζ = e^{πi/r} is a ring isomorphism from the cyclic ring (x^r = 1) to the ring modulo y^r + 1, so its negative wrap yields the cyclic wrap after untwisting.
  Shown as: Source transform via resampling, chirp and ring convolution *<predicate>* Twist from cyclic to negacyclic convolution

## Pages that build on this one

- Exact recovery: scaling, rounding and carries: Removing the known normalizations S and 2^{2b+4}, showing the recovered coefficient error is below 1/2 so rounding gives exact convolution coefficients, then propagating radix-2^b carries to the 2n-bit product.
- The multiplication algorithm: Split into radix digits, map by Φ to prime axes, take two source transforms, multiply pointwise, apply the opposite-sign transform with the two scalings by S, round, undo Φ, and propagate carries to output the 2n-bit product.

## Other pages you may link to

- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Three-element subset intersection gadget](triple-gadget.md)
- [Linear network that exchanges two banks and restores scratch values](bank-exchange-network.md)
- [Fixed finite-tape Turing machine model](fixed-tape-model.md)
- [Established n log n multiplier as a subroutine](nlogn-subroutine.md)
- [Arrays, address fields and elementary scans](stream-arrays.md)
- [Frames and the common-frame identity](frames.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Orthogonal complements and projections in a bilinear space](bilinear-orthogonal.md)
- [Nested subspace labels and the rank saving](subspace-labels.md)
- [Lower-triangular rank factorization](triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Power-width chunk interchange in O(Ve^τ) time](power-width-interchange.md)
- [Chunk interchange in O(Vu^τ) time](chunk-swap.md)
- [Packed XOR of selected bits across address chunks](packed-selected-bits.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed Kronecker packing of polynomial products](signed-kronecker-packing.md)
- [Fixed-point disk-grid arithmetic and contractions](fixed-point-disk-grid.md)
- [Normalized DFT and cyclic convolution](dft-cyclic-convolution.md)
- [Multidimensional (tensor) Fourier transform](multidim-transform.md)
- [Chinese-remainder map to prime cyclic axes](crt-axis-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Synthetic Fourier transform modulo y^r + 1](synthetic-transform.md)
- [Radix-2 butterfly layers and stored frequency order](butterfly-layers.md)
- [Two-point kernel C and the complex phase network](phase-kernel-network.md)
- [Simultaneous butterfly layer in O(Vd^λ') time](simultaneous-butterfly-layer.md)
- [Layout and cost of the synthetic transform](transform-layout.md)
- [Choice of sizes, precision and prime axis lengths](parameter-choice.md)
- [Exact recovery: scaling, rounding and carries](exact-recovery.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the saving exponent κ](cost-accounting.md)
- [Multiplying n-bit integers in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "write $\widetilde{\mathscr F}$ for the following procedure: apply the linewise approximation to $\mathcal A$, apply the computed chirp transform" (paper)

  > For a source disk-grid tensor of norm at most $.5$, write $\widetilde{\mathscr F}$ for the following procedure: apply the linewise approximation to $\mathcal A$, apply the computed chirp transform $\widetilde{\mathscr C}$, apply the linewise approximation to $\mathcal B_0$, and multiply the grid numerators exactly by $2^\gamma$. Its exact counterpart is \[ \mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A =RF_{\boldsymbol s}. \] Here an exact counterpart replaces every numerical subroutine by the exact map it approximates and omits truncations. The source arrays are stored in the padded power-of-two box, with zeros outside the valid source coordinates. The compressed scalar output uses $w_{\rm c}$-bit components. Appending $\gamma$ zero bits to each word gives the exact scaled numerator in the known signed width $w_{\rm c}+\gamma$. For the stated input norm, the disk estimate below proves that every scaled coordinate still belongs to $\mathbb D_p$. Its component numerators therefore have magnitude at most $2^p$, so a scan removes only leading sign-extension bits and returns the same integers in $w_{\rm c}$ bits. This scan costs $O(T(w_{\rm c}+\gamma))=O(Tp)$ and leaves the padded zero records zero. Define the opposite-sign procedure by \[ \widetilde{\mathscr F}^{+}(z) =\overline{\widetilde{\mathscr F}(\overline z)}; \] its exact counterpart is $RF_{\boldsymbol s}^{+}$ by Lemma~\ref{lem:chirp-permutation}.

- "\mathcal M_{\mathbb C}(f,g) :=D_-\iota^{-1} \mathcal M_r(\iota D_+f,\iota D_+g)" (paper)

  > ng-convolution interface. Put $M=\prod_{i<d}t_i=T/r$. For a complex array $f$ on $\prod_{i=1}^d\mathbb Z/t_i\mathbb Z$, with $t_d=r$, define \[ (\iota f)_{\boldsymbol j} =\sum_{k=0}^{r-1}f_{\boldsymbol j,k}y^k, \qquad \boldsymbol j\in\prod_{i<d}\mathbb Z/t_i\mathbb Z. \] This identifies the scalar tensor with an array of $M$ records in $\mathcal R$. As maps of values, $\iota$ and $\iota^{-1}$ preserve norms and grids. Write $(D_\pm f)_{\boldsymbol j,k}=\zeta^{\pm k}f_{\boldsymbol j,k}$. The linewise extension of $\Theta$ is $\iota D_+$, with inverse $D_-\iota^{-1}$. Consequently, with $\mathcal M_r$ from Section~\ref{sec:exact-ring-products}, normalized complex cyclic convolution is \[ \mathcal M_{\mathbb C}(f,g) :=D_-\iota^{-1} \mathcal M_r(\iota D_+f,\iota D_+g) =\frac{f*g}{T}. \] Here $\mathcal M_r$ convolves the first $d-1$ axes over $\mathcal R$, whereas $*$ on the right convolves all $d$ scalar axes. The division by $T$ is already part of $\mathcal M_r$. The maps $D_\pm$ and $\iota^{\pm1}$ are isometries, so $\mathcal M_{\mathbb C}$ is also a bilinear contraction.


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

Write the body to `exegenius/tasks/0038-write-source-transform.answer.md` and the JSON to `exegenius/tasks/0038-write-source-transform.answer.json`, then run `exegenius submit 0038-write-source-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0038-write-source-transform`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
