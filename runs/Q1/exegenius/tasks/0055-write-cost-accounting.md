# exegenius task 0055-write-cost-accounting

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
- Precision analysis and exact recovery
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

Concept: Cost table and the exponent κ
Gloss: The accounting that bounds every stage's cost divided by Tp = Θ(n) by a power of p at most 1 − 2κ, so the whole algorithm runs in O(n·(log n)^{1−κ}).
Also called: complete time bound

## This page in the argument

The step: Every stage's cost divided by $Tp=\Theta(n)$ is at most a power $p^{1-2\kappa}$, so the machine runs in $O(n(\lg n)^{1-\kappa})$ time for every $n$.
How: Tabulate the normalized cost of each stage as a power of $p$, compute the margins of the seven dominant powers below one, and absorb setup, exceptional-set sorting and small inputs.
Why: The smallest margin is $2\kappa$, and that explicit slack covers any remaining fixed power of $\log p$. (the sources say so: "This explicit slack will cover
any remaining fixed power of $\log p$." (paper))
Striking feature: The saving $\kappa=2^{-182}$ is astronomically small but strictly positive, which is all that is needed to beat $n\log n$. (explain why it holds, from the method)

Its sub-steps, in order:

- The seven dominant powers have margins $g_1,\ldots,g_7$ below one with $\min_ig_i=2^{-181}=2\kappa$.
- Descriptor setup over the at most $p^A$ recursion visits costs $p^{A+C}=o(Tp)$.
- Sorting the exceptional records of all packed basis changes costs $o(V)$ deterministically in the worst case.
- Since every power is at most $1-2\kappa$ and fixed powers of $\log p$ are eventually below $p^\kappa$, the bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.
- Below a fixed cutoff schoolbook multiplication is used, and the finitely many small lengths only enlarge the constant.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet, fixed-tape Turing machine computes the exact $2n$-bit product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ conjecture in this model.; how: Reduce the product to radix-digit convolution, move it by a Chinese-remainder map, Gaussian resampling, chirps and a phase twist to convolution over $\mathbb C[y]/(y^r+1)$ computed by synthetic transforms; speed up the transforms' address movement and butterfly layers with two network-based tape procedures; then prove exact recovery and total the costs. (on [Integer multiplication in O(n (lg n)^{1−κ}) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S13.1, S13.2, S13.3, S13.4, S13.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S13.1**: The seven dominant powers have margins $g_1,\ldots,g_7$ below one with $\min_ig_i=2^{-181}=2\kappa$.
Source: "Thus $\min_i g_i=2^{-181}=2\kappa$." (paper)
> The seven dominant powers in Table~\ref{tab:costs} have the following margins below one: \begin{equation}\label{eq:margin-list} \begin{split} g_1&=1-\epsilon(1+c),\qquad g_2=\epsilon c(1-\tau),\qquad g_3=\epsilon(1-\lambda'),\\ g_4&=1-\tau-\epsilon(2-\tau),\qquad g_5=1/4-\delta-3\epsilon/2,\\ g_6&=1-\delta-\epsilon,\qquad g_7=\epsilon. \end{split} \end{equation} Direct substitution gives \[ g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}. \] Thus $\min_i g_i=2^{-181}=2\kappa$. This explicit slack will cover any remaining fixed power of $\log p$.

**S13.2**: Descriptor setup over the at most $p^A$ recursion visits costs $p^{A+C}=o(Tp)$.
Source: "This setup then
costs at most $p^{A+C}=o(Tp)$." (paper)
> \paragraph{Setup and exceptional streams across all calls.} We next separate setup at recursion nodes from work repeated for every polynomial record or every Gaussian line. Here a visit means a node of the layer or address-layout recursions, or one of their round and group invocations. The internal recursion of the established integer multiplier and the iterations of the quoted Gaussian algorithms are already included in their separately charged running times. The layer and address-layout recursions have constant branching and depth $O(\log p)$, and the number of their rounds and base-$m$ groups is polynomial in $p$. Choose a fixed exponent $A$ so that their total number of visits is at most $p^A$, and a fixed $C$ bounding descriptor setup performed once per visit by $p^C$ steps. This setup then costs at most $p^{A+C}=o(Tp)$.

**S13.3**: Sorting the exceptional records of all packed basis changes costs $o(V)$ deterministically in the worst case.
Source: "This is
a deterministic worst-case bound." (paper)
> For one packed change of basis, let $V_{\rm call}$ be its current logical volume. The bad-address fraction is $O(d2^{-K})$, independently of the payload. Each polynomial record has $\Theta(rp)$ payload bits, and an exceptional record adds an $O(p)$-bit destination key. Thus the compact exceptional stream has length \[ O\!\left(\frac{V_{\rm call}}{rp}\,d2^{-K}(rp+p)\right) =O(V_{\rm call}d2^{-K}). \] Stable bit sorting makes $O(p)$ scans of this stream, for one-call cost $O(V_{\rm call}dp2^{-K})$. Extraction and reinsertion use a constant number of scans of the full current volume; those scans are already in the node overhead. Since there are at most $p^A$ visits, each of volume $O(V)$, the compact sorting costs sum to at most \[ O\!\left(dp2^{-K}\sum_{\rm calls}V_{\rm call}\right) =O(Vp^{A'}2^{-K})=o(V) \] for another fixed exponent $A'$. Here $d=O(p^\epsilon)$ and $K=\Theta(p^{\epsilon c})$ with $\epsilon c>0$. Predicate and key arithmetic is the polynomial work per record counted above. This is a deterministic worst-case bound.

**S13.4**: Since every power is at most $1-2\kappa$ and fixed powers of $\log p$ are eventually below $p^\kappa$, the bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.
Source: "The complete large-input bound is consequently" (paper)
> Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}

**S13.5**: Below a fixed cutoff schoolbook multiplication is used, and the finitely many small lengths only enlarge the constant.
Source: "The finitely
many smaller lengths are included by enlarging the implicit constant." (paper)
> Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Size parameters and prime source lengths](parameters.md): The choices b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, power-of-two box T ≈ 4n/b split into d axes of length r or r/2, distinct odd primes sᵢ just below each tᵢ, and the fixed rational exponents ending in κ = 2^{−182}.
  Shown as: Cost table and the exponent κ *<predicate>* Size parameters and prime source lengths
- [Simultaneous butterfly layer](simultaneous-layer.md): The procedure applying H₀ on the same bit position in up to d address chunks of an array of polynomial records at once in O(V·d^{λ′}) time, λ′ < 1, evaluating exactly with guard bits and truncating once.
  Shown as: Cost table and the exponent κ *<predicate>* Simultaneous butterfly layer
- [Transform layout and cost](transform-layout.md): Rearranging the address bits of a multidimensional synthetic transform so that each round's selected bits sit at a common offset in consecutive K-bit chunks, letting every round use the simultaneous butterfly layer.
  Shown as: Cost table and the exponent κ *<predicate>* Transform layout and cost
- [Fast address-chunk interchange](chunk-swap.md): The tape procedure that interchanges two disjoint u-bit address fields of any array in O(V·u^τ) time with fixed τ = 1 − 2^{−50}, computing XOR combinations of data along the way.
  Shown as: Cost table and the exponent κ *<predicate>* Fast address-chunk interchange
- [Tensor resampling interface](tensor-resampling.md): Applying the one-dimensional resampling maps line by line on every axis of a padded power-of-two box, moving axes into position with the fast chunk interchange.
  Shown as: Cost table and the exponent κ *<predicate>* Tensor resampling interface
- [Signed Kronecker packing](signed-packing.md): Multiplying two polynomials with signed Gaussian-integer coefficients by evaluating them at B₀ = 2^{4p} into single integers, multiplying with the established multiplier, and extracting centered coefficients before reducing modulo yʳ + 1.
  Shown as: Cost table and the exponent κ *<predicate>* Signed Kronecker packing
- [Chinese-remainder convolution map](crt-map.md): The Agarwal–Cooley isomorphism ℂ[x]/(x^S − 1) → ⊗ᵢ ℂ[xᵢ]/(xᵢ^{sᵢ} − 1) for pairwise coprime sᵢ, placing the digit list on a product of prime cyclic axes and implemented on tape by triangular controlled shifts and axis moves.
  Shown as: Cost table and the exponent κ *<predicate>* Chinese-remainder convolution map

## Pages that build on this one

- Integer multiplication in O(n (lg n)^{1−κ}) time: One deterministic fixed-alphabet, fixed-tape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n·(lg n)^{1−κ}) worst-case time with κ = 2^{−182}, disproving the n log n conjecture in that model.

## Other pages you may link to

- [The n log n conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Polynomial ring modulo yʳ + 1](negacyclic-ring.md)
- [Normalized butterfly H₀](normalized-butterfly.md)
- [Gaussian dyadic fixed-point arithmetic](fixed-point.md)
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
- [Two-point kernel C](kernel-c.md)
- [Binary phase interface of the complex network](phase-interface.md)
- [Packed selected-bit addition](packed-addition.md)
- [Recursive C-layer via phase frames](recursive-c-layer.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit reduction](radix-reduction.md)
- [Normalized discrete Fourier transform](dft.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein's chirp identity](bluestein.md)
- [Contractions and error accounting](contraction-errors.md)
- [Resampling with retained permutations](resampling-retained.md)
- [Source permutation cancellation](source-perm-cancel.md)
- [Ring convolution from the retained layout](synthetic-convolution.md)
- [Coefficient twist](coefficient-twist.md)
- [Computed source transform](source-transform.md)
- [Precision analysis and exact recovery](precision-recovery.md)
- [Integer multiplication in O(n (lg n)^{1−κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Thus $\min_i g_i=2^{-181}=2\kappa$." (paper)

  > The seven dominant powers in Table~\ref{tab:costs} have the following margins below one: \begin{equation}\label{eq:margin-list} \begin{split} g_1&=1-\epsilon(1+c),\qquad g_2=\epsilon c(1-\tau),\qquad g_3=\epsilon(1-\lambda'),\\ g_4&=1-\tau-\epsilon(2-\tau),\qquad g_5=1/4-\delta-3\epsilon/2,\\ g_6&=1-\delta-\epsilon,\qquad g_7=\epsilon. \end{split} \end{equation} Direct substitution gives \[ g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}. \] Thus $\min_i g_i=2^{-181}=2\kappa$. This explicit slack will cover any remaining fixed power of $\log p$.

- "Any fixed power of $\log p$ is at most $p^\kappa$ eventually." (paper)

  > Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}


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

Write the body to `exegenius/tasks/0055-write-cost-accounting.answer.md` and the JSON to `exegenius/tasks/0055-write-cost-accounting.answer.json`, then run `exegenius submit 0055-write-cost-accounting` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0055-write-cost-accounting`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
