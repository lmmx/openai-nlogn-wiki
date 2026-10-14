# exegenius task 0033-write-transform-layout

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F3V` (paths below are relative to it)

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

For these sources: The reader is an undergraduate in computer science who has taken discrete mathematics, data structures and algorithms, introductory theory of computation, and the linear algebra and calculus that accompany such a degree. They are fluent with asymptotic analysis, recurrences, binary representation and bitwise operations, modular arithmetic, matrices and rank, vector spaces over the reals, and complex numbers including roots of unity; they know the schoolbook and Karatsuba multiplication algorithms and what a Turing machine with tapes is. They have not studied abstract algebra beyond basics, the FFT's algebraic variants, number-theoretic transforms, finite fields beyond arithmetic mod 2, analytic number theory, numerical analysis of rounding error, or any bit-complexity multiplication algorithm.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Schönhage–Strassen optimality conjecture
- Harvey–van der Hoeven O(n log n) multiplier
- Cyclic convolution
- Integer product as digit convolution
- Discrete Fourier transform (also: Fourier transform, F_q)
- Multidimensional transform
- Two-point butterfly and radix-two recursion (also: H₀, butterfly layer)
- Contractions and error accumulation
- Bluestein chirp identity
- Polynomial ring modulo y^r + 1 (also: negacyclic ring, R_r)
  - $y$ (ring variable): The formal polynomial variable, satisfying y^r = −1 in the ring.
  - $r$ (ring length): The number of complex coefficients in a ring element, a power of two.
- Coefficient phase twist
- Synthetic polynomial transform
- Stored bit-reversed frequency order
- Signed Kronecker packing
- Arrays and elementary stream operations on tape
- Controlled shifts and rational scalings
- Bank-exchange network with restored scratch wires
- Frames on network wires
- Nested subspace labels and orthogonal residuals
- Strict rank saving
- Lower-triangular factorization of a matrix
- Cost of a matrix shear on address fields
- Power-width chunk interchange
- Address chunk interchange
  - $V$ (stored bit volume): The number of data bits stored in the array being permuted.
  - $u$ (chunk width): The number of bits in each of the two interchanged address chunks.
  - $\tau$ (interchange exponent): A fixed constant below one, 1 − 2^{−50}, bounding the power of the width in the cost.
- Phase frames and the two-point kernel C
- Packed selected-bit addition
- Exact dyadic intermediates with one truncation
- Simultaneous butterfly layer
- Exact recovery by rounding and carries
- Asymptotic notation beyond big-O (also: Omega notation, Theta notation, little-o, o(...), Ω, Θ, asymptotically smaller, worst-case running time)
- Limits and limit inferior (also: liminf, limsup, limit of a ratio, lim inf, eventually, for all sufficiently large n)
- Logarithms, exponentials, floors and ceilings (also: log base 2, lg n, log_2, natural logarithm, floor function, ceiling function, powers of two, iterated logarithm, log star)
- Recurrences and geometric sums (also: recurrence relation, solving recurrences, geometric series, geometric sum, unrolling a recurrence, divide and conquer)
- Positional number systems and carries (also: binary representation, radix representation, base-b digits, bit string, most significant bit, carry propagation, schoolbook addition, padding with leading zeros)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba, divide-and-conquer multiplication, Toom-Cook, quadratic multiplication)
- Bitwise operations and XOR (also: exclusive or, XOR, bitwise exclusive or, addition modulo 2, bit flip, parity, bit shift, bit mask)
- Modular arithmetic (also: integers modulo q, Z/qZ, congruence, residues, units modulo q, invertible residues, arithmetic mod q, Chinese remainder theorem for integers)
- Primes, coprimality and the extended Euclidean algorithm (also: prime numbers, relatively prime, pairwise coprime, gcd, greatest common divisor, Euclid's algorithm, Bezout identity, modular inverse, odd primes, primality testing by trial division)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, unit complex numbers, complex exponential, Euler's formula, twiddle factor, N-th root of unity)
- Matrices and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, linear operator, linear transformation, identity matrix, diagonal matrix, unitary or involution matrix, matrix-vector product, linear combination)
- Vector spaces, subspaces, dimension and rank (also: subspace, span, basis, linear independence, dimension, rank of a matrix, rank-nullity, kernel, image, column space, direct sum, quotient space)
- Inner products, bilinear forms and orthogonal complements (also: bilinear form, dot product, orthogonality, orthogonal complement, orthogonal subspace, nondegenerate pairing, inner product space, pairing)
- Gaussian elimination and triangular matrices (also: row reduction, LU decomposition, lower triangular matrix, upper triangular matrix, elementary row operations, back substitution, unit triangular matrix, row echelon form)
- Permutations, bijections and permutation matrices (also: permutation, bijection, one-to-one correspondence, inverse permutation, partial permutation, reordering of an array, sorting network, transposition of indices, permutation matrix)
- Arithmetic modulo 2 and linear algebra over F_2 (also: F_2, GF(2), binary field, field with two elements, matrices over F_2, GL(m, F_2), mod 2 arithmetic, boolean linear algebra)
- Finite sets, subsets and counting (also: Cartesian product, subset intersection, set cardinality, binomial coefficient, inclusion-exclusion, product of index sets, power set, three-element subsets, pigeonhole)
- Circuits and directed acyclic graphs (also: arithmetic circuit, linear circuit, wires and gates, directed graph, DAG, network of gates, fan-in, source and sink nodes, layered network)
- Vector norms and the triangle inequality (also: sup norm, maximum norm, infinity norm, ‖·‖_∞, modulus bound, triangle inequality, operator norm, error bound, disk bound)
- Fixed-point numbers, dyadic rationals and rounding (also: fixed point arithmetic, dyadic rational, binary fraction, rounding to nearest integer, truncation, round-off error, precision in bits, numbers with p fractional bits, grid of spacing 2^{-p})
- Row-major order and matrix transposition (also: row-major layout, array layout, transposing a matrix, matrix transpose, k×k binary matrix, lexicographic address, two-dimensional array as a list)
- Subroutines and reductions between problems (also: black-box subroutine, reduction, calling a subroutine, oracle call, problem reduction, conditional lower bound, composition of algorithms, uniform algorithm)
- Convolution of sequences (also: linear convolution, polynomial multiplication as convolution, product of coefficient sequences, discrete convolution, convolution theorem)

## This page

Concept: Transform layout and cost
Gloss: Placing the selected bits of all participating axes at a common offset in K-bit chunks, so each round of the synthetic transform uses the simultaneous layer, at total normalized cost dK + pK^{τ−1} + ℓd^{λ′}.

## This page in the argument

The step: With the selected bits of the $d-1$ participating axes placed at a common offset in consecutive $K$-bit chunks, the forward synthetic transform $LBF^-_{\boldsymbol t}$ of $M$ polynomial records of degree below $r=2^\ell$ runs in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ time with error below $\sqrt2\,\ell\,2^{-p}$.
How: Move the prefix slots by single-bit moves, bring the remaining chunks into aligned rounds by chunk exchanges, then run each round as one simultaneous butterfly layer followed by a signed-shift monomial and a single truncation.
Why: A round can use the simultaneous layer only if the selected bits of the participating axes sit at a common offset in consecutive $K$-bit chunks, so the layout must first be constructed. (the sources say so: "To apply Proposition~\ref{prop:simultaneous-layer} in a transform round,
we must place the selected bits of the participating axes at a common
offset in consecutive $K$-bit chunks." (paper))
Striking feature: Each of the three cost terms comes from a different tape operation: single-bit moves $dK$, chunk exchanges $pK^{\tau-1}$, and simultaneous layers $\ell d^{\lambda'}$. (explain why it holds, from the method)

Its sub-steps, in order:

- Over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ with root of unity $\omega_t=y^{2r/t}$, the transforms $F_t^{\mp}$ are contractions whose twiddle multiplications are signed shifts of coefficient lists, and $F_t^+F_t^-=t^{-1}I$, so only butterflies cost arithmetic. (on [Synthetic polynomial transform](synthetic-transform.md))
- The recursion writes entry $j$ of $F_t^-z$ at slot $\operatorname{rev}_a(j)$ (the record permutation $B_t$) and the opposite procedure reads the same order, so the two procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$ and no reordering is ever executed. (on [Stored bit-reversed frequency order](bit-reversed-order.md))
- At most $D(b+1)=O(dK)$ slots are moved to a prefix by single-bit moves, costing $O(TpdK)$.
- Reordering the remaining chunks uses at most $Dq-1$ exchanges of width-$K$ chunks, each costing $O(TpK^\tau)$, so $O(Tp\cdot pK^{\tau-1})$ in all.
- Each round on the remaining chunks is one simultaneous layer costing $O(Tpd^{\lambda'})$, so $O(Tp\ell d^{\lambda'})$ in total.
- There are at most $b+1\le K$ rounds on prefix slots, giving cost $O(TpdK)$.
- Starting with zero error, at most $\ell$ rounds each adding less than $\sqrt2\,2^{-p}$ give the error and disk bounds; the layout permutations are isometries.

It serves these steps, from the main result down:

- One deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a convolution of short digits evaluated by Fourier transforms, speed up the two costly ingredients (moving data between addresses, and butterfly arithmetic) by a power of a block size using one recursive saving, and total every cost term. (on [Sub-n-log-n integer multiplication](main-theorem.md))
- For arrays on $\prod_i\mathbb Z/t_i\mathbb Z$ with entries in $\mathcal R_r$, the normalised convolution $\mathcal M_r(f,g)=(f*g)/T$ is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ by two forward synthetic transforms, pointwise polynomial products by Kronecker packing, and the opposite transform on the retained order.; how: Transform both operands, multiply the polynomial records pointwise in the retained stored order (the same record permutation on both operands), and apply the opposite transform to that order; each ingredient is a separate procedure. (on [Convolution over the polynomial ring](ring-convolution.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.1.3, S4.1.4, S4.1.5, S4.1.6, S4.1.7). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.1.3**: At most $D(b+1)=O(dK)$ slots are moved to a prefix by single-bit moves, costing $O(TpdK)$.
Source: "There are at most $D(b+1)=O(dK)$
listed slots, so the moves cost $O(TpdK)$." (paper)
> . Call an axis long if $a_i=\ell$ and short if $a_i=\ell-1$. Name the original bit slots of axis $i$ by $(i,h)$, $a_i-1\geq h\geq0$. Initially these slots are in axis order and, within each axis, in decreasing $h$. The coefficients of each polynomial form a contiguous suffix. Put \[ b=(\ell-1)\bmod K, \qquad q=\lfloor(\ell-1)/K\rfloor. \] Form a list of the slots to move to a prefix. First list $(i,\ell-1)$ for the length-$2^\ell$ axes in increasing $i$. Then list $(i,h)$ for $h=b-1,\ldots,0$, and within each $h$ in increasing $i$; this second list is empty if $b=0$. Move each listed slot immediately after the prefix already formed, leaving all other slots in their relative order. There are at most $D(b+1)=O(dK)$ listed slots, so the moves cost $O(TpdK)$. A descriptor records the physical position of every named slot. The part of each axis left outside the prefix now consists of $q$ consecutive $K$-bit chunks.

**S4.1.4**: Reordering the remaining chunks uses at most $Dq-1$ exchanges of width-$K$ chunks, each costing $O(TpK^\tau)$, so $O(Tp\cdot pK^{\tau-1})$ in all.
Source: "This uses at most $Dq-1$
exchanges of width-$K$ address chunks, even when the chunks are
nonadjacent.  Each costs $O(TpK^\tau)$, so all these exchanges cost
\[
 O\bigl(Tp\,DqK^\tau\bigr)
       =O\bigl(Tp\,pK^{\tau-1}\bigr)." (paper)
> Number the axes by $i$ and their chunks, from high to low, by $j$. The remaining physical order changes from \[ (1,1),(1,2),\ldots,(1,q),(2,1),\ldots,(D,q) \quad\hbox{to}\quad (1,1),(2,1),\ldots,(D,1),(1,2),\ldots,(D,q). \] To obtain this order, scan its target positions from left to right. At each position except the last, exchange the chunk currently there with the required chunk if they differ. This uses at most $Dq-1$ exchanges of width-$K$ address chunks, even when the chunks are nonadjacent. Each costs $O(TpK^\tau)$, so all these exchanges cost \[ O\bigl(Tp\,DqK^\tau\bigr) =O\bigl(Tp\,pK^{\tau-1}\bigr). \] These prefix moves and chunk exchanges define $L$. We use the same letter for its induced record permutation: a record at address $x$ moves to address $Lx$, while its polynomial suffix stays intact. Recording the inverse operations in reverse order gives $L^{-1}$ with the same cost.

**S4.1.5**: Each round on the remaining chunks is one simultaneous layer costing $O(Tpd^{\lambda'})$, so $O(Tp\ell d^{\lambda'})$ in total.
Source: "The simultaneous-layer procedure therefore applies at cost
$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total." (paper)
> For a position $h$ in the remaining chunks, the selected bit has offset $(h-b)\bmod K$, counted from the least significant bit, in each of the $D$ consecutive chunks with the same chunk index $j$. Let $n_P$ and $n_S$ be the numbers of record-address bits before and after that group. Every combination of those bits occurs, so the layer sees the complete address set \[ [P]\times[2^K]^D\times[S],\qquad P=2^{n_P},\quad S=2^{n_S},\quad n_P+DK+n_S=\sum_i a_i\leq D\ell=O(p). \] Thus its record count is $PS2^{DK}=M$ and $\log_2(2M)\leq(C_\ell+1)p=C_Mp$. The current transform parameters supply $p,d,r,K,w$, and the round determines $D,P,S$ and the selected offset $\rho$. Encode these values as the header $\mathcal E$ of Proposition~\ref{prop:simultaneous-layer}. The same fixed descriptor bound covers every axis choice and round. Indeed $|\Gamma(v)|\leq2\log_2v+1$, and $\ell+n_P+n_S\leq d\ell\leq C_\ell p$. Also $d,D\leq\max\{C_\ell,1\}p$, $K,\rho+1\leq p$, and $w\leq C_wp$. Adding the nine code lengths therefore gives \[ |\mathcal E| \leq 2C_\ell p+12\log_2p+ 4\log_2\max\{C_\ell,1\}+2\log_2C_w+9 \leq C_{\rm desc}p. \] The last inequality uses $p\geq1$, $\log_2p\leq p$, and $\log_2x\leq x$ for $x\geq1$. This is the descriptor passed to the layer; the longer table locating named slots remains separate for the transform's address calculations. The simultaneous-layer procedure therefore applies at cost $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.

**S4.1.6**: There are at most $b+1\le K$ rounds on prefix slots, giving cost $O(TpdK)$.
Source: "most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$." (paper)
> In a round on prefix slots, process the participating bits individually. Temporarily move one such bit immediately before the polynomial suffix. In each now adjacent pair, buffer the first record and scan it with the second, writing the half-sums and half-differences to two work tapes. Append the half-sum record and then the half-difference record, and reverse the bit move after all pairs are processed. Including head returns, the work is $O(rp)$ per pair and $O(Tp)$ for the moves and scans at coefficient width $O(p)$. That width suffices without truncating between axes: after $s\leq D$ individual $H_0$ factors, the coefficients are exact dyadics on the $2^{-(p+s)}$ grid and still lie in the disk. A temporary sum has modulus at most two and needs only a constant number of extra integer bits. Hence $p+D+O(1)=O(p)$ bits per component suffice, since $D\leq d$ and $d\ell=O(p)$. Complete the combined monomial exactly and apply $Q_p$ once at the end of the round. Write the resulting disk-grid numerators in the supplied $w$-bit component format. Their magnitudes are at most $2^p$, so this takes one linear scan within the same bound. In an opposite round on prefix slots the inverse monomial comes first and preserves the grid and disk, so the same width bound holds for its individual factors. There are at most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$.

**S4.1.7**: Starting with zero error, at most $\ell$ rounds each adding less than $\sqrt2\,2^{-p}$ give the error and disk bounds; the layout permutations are isometries.
Source: "Starting with
zero error, at most $\ell$ rounds therefore
give the claimed error and disk bounds.  The layout permutations
are isometries and add no numerical error." (paper)
> For a forward round on a group of $D$ chunks, the layer call returns $Q_p(\mathcal H z)$ and the next operation is $J_E$. Truncation toward zero is odd and acts separately on every real and imaginary part. Since $J_E$ is a signed coefficient permutation, it follows that \[ J_EQ_p(\mathcal H z)=Q_p(J_E\mathcal H z). \] Thus the actual forward call sequence returns exactly the result of truncating once after the exact contraction round. In the opposite direction, $J_E^{-1}$ first preserves the disk grid, and the layer call returns $Q_p(\mathcal HJ_E^{-1}z)$ directly. The rounds on prefix slots have the same forms, with one truncation, by their exact evaluation above. A contraction does not increase the norm of the difference between the computed and exact arrays; the single truncation then adds less than $\sqrt2\,2^{-p}$ by \eqref{eq:transform-truncate}. Both the contraction and truncation preserve the disk. Starting with zero error, at most $\ell$ rounds therefore give the claimed error and disk bounds. The layout permutations are isometries and add no numerical error.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S4.1.1 (on [Synthetic polynomial transform](synthetic-transform.md)): Over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ with root of unity $\omega_t=y^{2r/t}$, the transforms $F_t^{\mp}$ are contractions whose twiddle multiplications are signed shifts of coefficient lists, and $F_t^+F_t^-=t^{-1}I$, so only butterflies cost arithmetic.
- S4.1.2 (on [Stored bit-reversed frequency order](bit-reversed-order.md)): The recursion writes entry $j$ of $F_t^-z$ at slot $\operatorname{rev}_a(j)$ (the record permutation $B_t$) and the opposite procedure reads the same order, so the two procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$ and no reordering is ever executed.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Synthetic polynomial transform](synthetic-transform.md): A Fourier transform over the negacyclic ring using ω_t = y^{2r/t} as root of unity, so each twiddle multiplication is a signed shift and only butterflies cost arithmetic.
  Shown as: Transform layout and cost *<predicate>* Synthetic polynomial transform
- [Stored bit-reversed frequency order](bit-reversed-order.md): The recursion writes outputs in bit-reversed order (record permutation B_t), and the opposite transform consumes that same order, so no reordering is needed between the forward transforms and the inverse.
  Shown as: Transform layout and cost *<predicate>* Stored bit-reversed frequency order
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): Applying H₀ to one selected bit in each of D address chunks at once, on arrays of ring records, in O(V d^{λ′}) with λ′ < 1 instead of D whole-array passes, via the recursive complex network on packed bit changes.
  Shown as: Transform layout and cost *<predicate>* Simultaneous butterfly layer
- [Address chunk interchange](chunk-interchange.md): Swapping two disjoint equal-width bit chunks of an address array in O(V u^τ) steps for a fixed τ < 1, by XOR combinations whose final effect is an exact permutation.
  Shown as: Transform layout and cost *<predicate>* Address chunk interchange

## Pages that build on this one

- Parameter choice for the multiplier: Fixed rational exponents (τ, σ, λ′, c, ε, δ, κ) and sizes b = ⌈log₂n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, T ≈ n/b, r = 2^ℓ, with prime axis lengths s_i < t_i.
- Complete time bound: Dividing costs by the volume Tp, seven dominant terms with powers of p below one (margins g₁,…,g₇) show total time O(n (lg n)^{1−κ}); the smallest margin is 2κ.

## Other pages you may link to

- [Schönhage–Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hh-multiplier.md)
- [Arrays and elementary stream operations on tape](tape-stream-operations.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Bank-exchange network with restored scratch wires](exchange-network.md)
- [Frames on network wires](frames.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Strict rank saving](rank-saving.md)
- [Lower-triangular factorization of a matrix](matrix-factorization.md)
- [Cost of a matrix shear on address fields](matrix-shear.md)
- [Power-width chunk interchange](power-width-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Contractions and error accumulation](contraction-error.md)
- [Exact dyadic intermediates with one truncation](guard-bits.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer product as digit convolution](radix-digit-convolution.md)
- [Coefficient phase twist](phase-twist.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-two recursion](fft-butterfly.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Phase frames and the two-point kernel C](phase-frames.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Convolution over the polynomial ring](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutations cancel in a convolution](permutation-cancellation.md)
- [Chinese-remainder map to prime axes](crt-axis-map.md)
- [Prime axis lengths near powers of two](prime-axis-lengths.md)
- [Parameter choice for the multiplier](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound](time-bound.md)
- [Sub-n-log-n integer multiplication](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks" (paper)

  > To apply Proposition~\ref{prop:simultaneous-layer} in a transform round, we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks. We now construct that layout, keeping each polynomial's coefficients in a contiguous suffix. The layout uses the single-bit moves of Lemma~\ref{lem:elementary-streams} and the chunk interchanges of Lemma~\ref{lem:chunk-swap}; each movement is included in the transform cost. The layer then supplies one truncated contraction per round, and its temporary rows and work streams are removed before the next round begins.

- "\begin{lemma}[Transform layout and cost]" (paper)

  > \begin{lemma}[Transform layout and cost] \label{lem:synthetic-transform-cost} Fix the rational parameters and positive comparison constants $a_d\leq b_d$, $a_r\leq b_r$ of Proposition~\ref{prop:simultaneous-layer}. Fix constants $C_\ell>0$ and $C_w>1$, and choose the layer constants once as \[ C_M=C_\ell+1,\qquad C_{\rm desc}=32(C_\ell+C_w+1). \] Use these constants and $C_w$ in Proposition~\ref{prop:simultaneous-layer}. These fixed choices determine a cutoff $p_1$, one fixed-tape procedure, and an implicit time constant with the following guarantee. For every choice of positive integers $p,d,r$ with $p\geq p_1$ and \[ a_dp^\epsilon\leq d\leq b_dp^\epsilon,\qquad 2^{a_rp/d}\leq r\leq2^{b_rp/d}, \] suppose $d\geq2$ and $r=2^\ell$ with an integer $2\leq\ell<p$, and require \[ d\ell\leq C_\ell p,\qquad 1\leq K=\lfloor d^c\rfloor\leq\ell-1. \] Let $t_i\in\{2^{\ell-1},2^\ell\}$ for $1\leq i\leq d-1$, put $M=\prod_{i=1}^{d-1}t_i$ and $T=rM$, and let $w$ be an integer with $p+2\leq w\leq C_wp$. The cutoff and time constant are independent of $p,d,r$, these axis choices, the round headers constructed from them, and $w$ within the displayed bounds.


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

Write the body to `exegenius/tasks/0033-write-transform-layout.answer.md` and the JSON to `exegenius/tasks/0033-write-transform-layout.answer.json`, then run `exegenius submit 0033-write-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0033-write-transform-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
