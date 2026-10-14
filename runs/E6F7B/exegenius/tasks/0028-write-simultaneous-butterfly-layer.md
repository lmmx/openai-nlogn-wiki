# exegenius task 0028-write-simultaneous-butterfly-layer

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F7B` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, functions, permutations, modular arithmetic, primes and gcd), calculus-level analysis (limits, sums, Newton's method), first-course linear algebra (matrices, inverses, Gaussian elimination, vectors) and complex numbers up to roots of unity, algorithm analysis (recursion, recurrences, big-O with its relatives Omega, Theta, little-o) and basic Turing machines. The reader knows binary representation and bitwise operations, and the textbook schoolbook multiplication. The reader has not studied abstract algebra beyond what the existing concepts introduce (rings and quotient rings, zero divisors, group characters), number-theory estimates on primes, numerical analysis of rounding errors, fast multiplication algorithms beyond the basics, or any coding-theory or quantum-computing notation, so those are explained in the wiki.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Multiplication complexity and the n log n conjecture
- Fixed finite-alphabet multitape model
- Established O(n log n) multiplier (subroutine)
- Array order and elementary stream operations
- Controlled shifts
- Discrete Fourier transform
- Fixed-point complex coefficients and truncation
- Contractions and error accounting
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The formal variable of the polynomials, satisfying y^r = −1.
  - $r$ (coefficient count): The number of complex coefficients of each polynomial, a power of two.
- Two-point butterfly
- Signed packing of ring products
- Subspaces, orthogonality and rank
- Linear network exchanging two banks with restored scratch values
- Frames: changing the representation along a network
- Subspace labels from three-element subsets
- Rank deficit s < W m
- Recursive power saving from the rank deficit
- Lower-triangular (Bruhat) factorization
- Address shear from the bit network
- Cost of a rational matrix shear
- Recursive power-width address interchange
- Address-chunk interchange in time O(V u^τ)
  - $V$ (stored bit volume): The number of data bits stored in the array being rearranged.
  - $u$ (chunk width): The number of bits in each of the two interchanged address chunks.
  - $\tau$ (interchange exponent): A fixed constant strictly below one (1 − 2^{−50}) bounding the growth of the cost with the chunk width.
- Complex phase network and two-point kernels
- Packed selected-bit addition
- Asymptotic notation beyond big-O (also: Omega, Theta, little-o, Ω(f), Θ(f), o(f), liminf, limit of a ratio, asymptotic lower bound, asymptotic equivalence)
- Logarithms, exponentials, floor and ceiling (also: lg, log base 2, log2, natural logarithm, ln, floor, ceiling, ⌊x⌋, ⌈x⌉, powers of two, iterated logarithm)
- Binary representation and bitwise operations (also: binary numbers, positional notation, radix representation, base-b digits, most significant bit, bit string, XOR, exclusive or, bitwise addition mod 2, two's complement, leading zeroes, carry)
- Schoolbook integer arithmetic (also: grade-school multiplication, long multiplication, long division, quadratic-time multiplication, integer division with remainder, quotient and remainder, Euclidean division)
- Modular arithmetic (also: congruence, residues, mod q, integers modulo n, ℤ/qℤ, units modulo q, modular inverse, multiplicative inverse mod q, residue ring)
- Primes, coprimality and gcd (also: prime numbers, pairwise coprime, relatively prime, greatest common divisor, gcd, extended Euclidean algorithm, Euclid's algorithm, trial division, odd prime, divisibility, prime to q)
- Sets, functions, Cartesian products and bijections (also: index set, [n] = {0,...,n-1}, product set, Cartesian product, injective surjective bijective, inverse map, indexing, lexicographic order, mixed-radix index)
- Permutations (also: permutation of positions, bit-reversal permutation, involution, composition of permutations, permutation matrix, cyclic shift, swap, partial permutation)
- Matrices and linear maps (also: matrix multiplication, identity matrix, invertible matrix, matrix inverse, transpose, matrix transposition, Gaussian elimination, row operations, linear operator, diagonal matrix, lower triangular matrix, GL(m), row-major order, linearity)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2πi/n}, character sum, sum of roots of unity vanishes, geometric sum of roots of unity)
- Summation, geometric series and products (also: sigma notation, geometric sum, geometric series, arithmetic series, sum of a geometric progression, product notation, telescoping sum, telescoping)
- Recursion and divide-and-conquer recurrences (also: recurrence relation, master theorem, recursion depth, solving recurrences, recursive call, unrolling a recurrence, divide and conquer)
- Worst-case running time and subroutines (also: deterministic algorithm, worst-case time, black box, subroutine call, reduction, time complexity, exact computation, bit complexity, depth-first schedule)
- Triangle inequality and norms (also: triangle inequality, absolute value of a sum, max norm, sup norm, operator norm, |z+w| ≤ |z|+|w|, error bound, absolute error)
- Rational numbers and rounding (also: fractions, dyadic rational, rounding to nearest integer, truncation toward zero, denominator, reals, real and imaginary parts)
- Newton's method (also: Newton iteration, Newton-Raphson, quadratic convergence, reciprocal iteration, square root iteration)
- Tapes, scanning and sorting as basic machine procedures (also: scan a tape, linear scan, copying a tape, merge, sorting, work tape, head movement, tape reversal)

## This page

Concept: Simultaneous butterfly layer in time O(V d^λ′)
Gloss: Applying H₀ at once to the same bit position of D ≤ d address chunks of every polynomial record in O(V d^{λ'}) for fixed λ' < 1, via H₀^{⊗D} = b^D S_D C^{⊗D} S_D, the recursive phase network, packed bit moves, exact Gaussian dyadic arithmetic and one final truncation.
Heading: Simultaneous butterfly layer in time $O(Vd^{\lambda'})$

The symbols in this page's heading denote (say so on the page):

- $V$ (stored bit volume): The number of data bits stored in the array of polynomial records.
- $d$ (axis count): The upper bound on the number of address chunks (transform axes) whose selected bits are butterflied together.
- $\lambda'$ (layer exponent): A fixed constant strictly below one (1 − 2^{−54}) bounding the growth of the cost with the number of axes.

## This page in the argument

The step: The map $H_0(u,v)=((u+v)/2,(u-v)/2)$ is applied at once to the same bit position of $D\le d$ address chunks of every polynomial record, with one final truncation, in $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$.
How: Write $H_0^{\otimes D}$ as phase factors around the tensor power $C^{\otimes D}$ of the two-point kernel, evaluate $C^{\otimes D}$ by the complex phase network with smaller layers as children, implement the binary changes of basis by packed selected-bit additions, bound the intermediate dyadic widths, and solve the recurrence.
Why: Applying the $D$ butterfly factors separately would cost $D$ passes over the whole array, so the factors must be done together. (the sources say so: "factors would require $D$ whole-array passes." (paper))
Striking feature: The cost is a fixed power $d^{\lambda'}$ with $\lambda'<1$ of the number of chunks, rather than the factor $D$ of separate passes, and the exponent mirrors the strict gap $s<Wm$ of the complex network. (explain why it holds, from the method)

Its sub-steps, in order:

- The recursive network on $e=mf$ selected axes makes exactly $s$ child calls on streams of volume $V/W$ and yields $C^{\otimes e}$ on every role.
- The normalized butterfly layer is $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$ with $\mathcal S_D$ a diagonal phase operator, so a $C$ layer gives an $H_0$ layer by exact Gaussian dyadic operations.
- A binary row addition on selected bits of two address chunks is done by a constant number of whole-chunk cyclic shifts, using a third chunk of arbitrary contents as temporary storage, plus a repair of an explicitly bounded set of exceptional addresses. (on [Packed selected-bit addition](packed-selected-bit-addition.md))
- Splitting the cost into overhead $O((eK)^\tau+1)$ per node and the factor $s/W$ gives $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, which unrolls to $O(d^{\lambda'})$ after base-$m$ partition of the $D$ chunks.
- The accelerated network is evaluated exactly until the whole layer is complete, and explicit guard widths bound denominator and magnitude growth of all intermediate Gaussian dyadics by $o(p)$ bits.
- The row construction and recurrence give total time $O(Vd^{\lambda'})$ on fixed tapes, and one final truncation yields a disk array with error below $\sqrt2\,2^{-p}$.

It serves these steps, from the main result down:

- One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.; how: Keep the transform-based multiplication of Harvey and van der Hoeven (Gaussian resampling, Bluestein chirp, synthetic polynomial transforms) but replace its two costly tape operations, address rearrangement and butterfly layers, by faster procedures obtained from rank-saving linear networks, then check exactness and total cost. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Two tape procedures cost $O(Vu^\tau)$ for interchanging two address fields of $u$ bits and $O(Vd^{\lambda'})$ for a butterfly layer on at most $d$ chunks, where $V$ is the stored bit volume, $\tau<1$ and $\lambda'<1$.; how: Derive both procedures from the same device: a fixed linear network whose edge changes are cheaper smaller calls of the same procedure, on top of elementary linear-time stream operations.

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.5.1, S1.5.2, S1.5.4, S1.5.5, S1.5.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.5.1**: The recursive network on $e=mf$ selected axes makes exactly $s$ child calls on streams of volume $V/W$ and yields $C^{\otimes e}$ on every role.
Source: "Apply the finite network with these column frames to a group of" (paper)
> \paragraph{The exact recursive contract.} Apply the finite network with these column frames to a group of $e=mf$ selected axes. Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot. The source and sink $Z_{a,f}$ signs, together with the scalar $i^{27f}$ at each affected sink, turn every endpoint kernel into a forward one. Negating the prescribed physical bank and undoing its exchange returns each result to its original role. Proposition~\ref{prop:complex-motif-interface} therefore gives $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary. Formula~\eqref{eq:phase-inverse-child} supplies each inverse child from one forward call, and none of the corrections adds a child. The remaining operations are a fixed number of binary row additions and coefficientwise scalar operations.

**S1.5.2**: The normalized butterfly layer is $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$ with $\mathcal S_D$ a diagonal phase operator, so a $C$ layer gives an $H_0$ layer by exact Gaussian dyadic operations.
Source: "H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D" (paper)
> \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.

**S1.5.4**: Splitting the cost into overhead $O((eK)^\tau+1)$ per node and the factor $s/W$ gives $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, which unrolls to $O(d^{\lambda'})$ after base-$m$ partition of the $D$ chunks.
Source: "F(e)\le (s/W)F(e/m)+O((eK)^\tau+1)," (paper)
> \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).

**S1.5.5**: The accelerated network is evaluated exactly until the whole layer is complete, and explicit guard widths bound denominator and magnitude growth of all intermediate Gaussian dyadics by $o(p)$ bits.
Source: "The accelerated network is evaluated exactly until an entire" (paper)
> The accelerated network is evaluated exactly until an entire normalized butterfly layer is complete. Its intermediate operators need not be contractions. We now give explicit constants that bound denominator and magnitude growth within one layer.

**S1.5.6**: The row construction and recurrence give total time $O(Vd^{\lambda'})$ on fixed tapes, and one final truncation yields a disk array with error below $\sqrt2\,2^{-p}$.
Source: "The row construction and the recurrence analysis" (paper)
> Uniformly for large $p$, the bands give $f\le d\le p$ and \[ K\ge\tfrac12a_d^c p^{\epsilon c},\qquad r\ge2^{(a_r/b_d)p^{1-\epsilon}}. \] The first inequality follows from $K=\lfloor d^c\rfloor$ once $d^c\ge2$. In particular, $K\ge6$ and $K/\log p\to\infty$, while $r$ dominates every fixed polynomial. Substituting the common bound $A_*\le C_Ap$ into the two additional normalized terms in \eqref{eq:packed-rectangle-time} gives \[ \begin{aligned} \frac{A_*^3}{R_{\rm g}} &\le\frac{C_A^3p^2}{2r},\\ 80(f-1)2^{-K}A_*\left(1+\frac{A_*}{R_{\rm g}}\right) &\le80C_Ap^2 2^{-K}\left(1+\frac{C_A}{2r}\right). \end{aligned} \] Both bounds tend to zero uniformly over all current allowed $d,r$. Thus Lemma~\ref{lem:packed-selected-bit-rectangle} has the required $O(M_{\rm child}R_{\rm g}(L^\tau+1))$ cost for every packed call, with one common time constant. The row construction and the recurrence analysis above give total time $O(Vd^{\lambda'})$ on fixed tapes, including all padded and auxiliary streams. Equation~\eqref{eq:phase-butterfly-layer} converts the resulting exact $C$-layer to $\mathcal H$.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.5.3 (on [Packed selected-bit addition](packed-selected-bit-addition.md)): A binary row addition on selected bits of two address chunks is done by a constant number of whole-chunk cyclic shifts, using a third chunk of arbitrary contents as temporary storage, plus a repair of an explicitly bounded set of exceptional addresses.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Complex phase network and two-point kernels](phase-frame-network.md): The same network over Gaussian dyadic values with binary labels and phase frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m}; each edge change is a product of two-point kernels C = aI+bX (a=(1+i)/2, b=(1−i)/2), and telescoping gives C^{⊗m} on every role with s_c < W_c·m kernel factors.
  Shown as: Simultaneous butterfly layer in time O(V d^λ′) *<predicate>* Complex phase network and two-point kernels
- [Packed selected-bit addition](packed-selected-bit-addition.md): A binary row addition (XOR) of selected bits across many address chunks at once, done by a constant number of whole-chunk cyclic shifts using a third chunk of arbitrary contents as temporary storage, followed by a deterministic repair of an explicitly bounded set of exceptional addresses.
  Shown as: Simultaneous butterfly layer in time O(V d^λ′) *<predicate>* Packed selected-bit addition
- [Address-chunk interchange in time O(V u^τ)](arbitrary-width-interchange.md): Exchanging two disjoint contiguous address fields of u bits (any width, any gaps, even one-bit payload) in O(V u^τ) for a fixed τ = 1 − 2^{−50} < 1, by peeling off high digits to make rows, padding, and splitting the width in base m; the intermediate steps are XOR combinations though the result is an exact permutation.
  Shown as: Simultaneous butterfly layer in time O(V d^λ′) *<predicate>* Address-chunk interchange in time O(V u^τ)
- [Fixed-point complex coefficients and truncation](fixed-point-disk.md): Complex numbers stored as 2^{−p}(a+ib) with integer a, b inside the unit disk, written as signed two's-complement words; Q_p truncates real and imaginary parts toward zero to this grid, with error below √2·2^{−p} and no increase of norm.
  Shown as: Simultaneous butterfly layer in time O(V d^λ′) *<predicate>* Fixed-point complex coefficients and truncation
- [Recursive power saving from the rank deficit](power-saving-recurrence.md): A call at parameter m·f makes s calls at parameter f on streams of volume V/W, giving F_k ≤ (s/W)F_{k−1}+O(1) with s/W < m, so the normalized cost is O(parameter^τ) for some τ < 1.
  Shown as: Simultaneous butterfly layer in time O(V d^λ′) *<predicate>* Recursive power saving from the rank deficit
- [Two-point butterfly](butterfly.md): The map H₀(u,v) = ((u+v)/2, (u−v)/2) on a pair of values, the basic step of a radix-2 fast Fourier transform; applied to a coordinate bit it is a halving contraction.
  Shown as: Simultaneous butterfly layer in time O(V d^λ′) *<predicate>* Two-point butterfly

## Pages that build on this one

- Transform layout and cost: A positional layout permutation L places the selected bits of all axes at a common offset in consecutive K-bit chunks (prefix moves plus chunk exchanges), so each round is one simultaneous layer; the forward and opposite transforms cost O(Tp[dK + pK^{τ−1} + ℓ d^{λ'}]) with error below √2 ℓ 2^{−p}.
- Complete time bound and power margins: Dividing costs by V = Tp gives seven dominant terms (butterfly rounds, chunk exchanges, simultaneous layers, CRT layouts, Gaussian lines, chirps, packed products) each at most p^{1−2κ}; the smallest margin is 2^{−181} = 2κ, which absorbs log factors and gives O(n(log n)^{1−κ}).

## Other pages you may link to

- [Multiplication complexity and the n log n conjecture](nlogn-history.md)
- [Fixed finite-alphabet multitape model](fixed-tape-model.md)
- [Established O(n log n) multiplier (subroutine)](established-multiplier.md)
- [Array order and elementary stream operations](stream-operations.md)
- [Controlled shifts](controlled-shifts.md)
- [Subspaces, orthogonality and rank](linear-algebra-prelims.md)
- [Linear network exchanging two banks with restored scratch values](xor-linear-network.md)
- [Subspace labels from three-element subsets](subset-labels.md)
- [Frames: changing the representation along a network](frames.md)
- [Rank deficit s < W m](rank-deficit.md)
- [Address shear from the bit network](bit-shear-interface.md)
- [Lower-triangular (Bruhat) factorization](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Recursive power-width address interchange](power-width-interchange.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed packing of ring products](signed-packing-product.md)
- [Contractions and error accounting](error-accounting.md)
- [Discrete Fourier transform](dft.md)
- [Cyclic convolution and the convolution theorem](cyclic-convolution.md)
- [Multidimensional transforms and convolutions](multidimensional-dft.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Retained (bit-reversed) frequency order](retained-frequency-order.md)
- [Transform layout and cost](transform-layout.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Tensor resampling on the padded box](padded-box-tensor-resampling.md)
- [Retained permutations and their cancellation](permutation-cancellation.md)
- [Integer multiplication as radix-digit convolution](radix-digit-convolution.md)
- [Chinese-remainder map to prime cyclic axes](crt-map.md)
- [Parameter choices and prime axis lengths](prime-axis-parameters.md)
- [Coefficient twist from cyclic to negacyclic](phase-twist.md)
- [Computed source transform](source-transform.md)
- [Precision budget and exact recovery](exact-recovery.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound and power margins](cost-accounting.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D." (paper)

  > \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.

- "The procedure returns $Q_p(\mathcal H z)$ in the same array," (paper)

  > The procedure returns $Q_p(\mathcal H z)$ in the same array, coefficient order, and component format in $O(Vd^{\lambda'})$ time, uniformly over all these choices of $p,d,r,D,P,S,\rho,w$ and $z$. Every returned coefficient belongs to the complex unit disk, and, in the maximum coefficient norm, \[ \|Q_p(\mathcal H z)-\mathcal H z\|_\infty <\sqrt2\,2^{-p}. \] The procedure evaluates the entire layer exactly before this final truncation. Put \[ C_0=128m\bigl(s_{\rm c}+64(W_{\rm c}+m+1)^3\bigr)^2, \] where $m,W_{\rm c},s_{\rm c}$ are the fixed constants of Proposition~\ref{prop:complex-motif-interface}. The procedure uses at most $p+\lceil C_0d^{C_1}\rceil$ fractional bits and $\lceil C_0d^{C_1}\rceil+3$ integer and sign bits per real component internally; these widths are $O(p)$. The time includes address changes, deterministic repair, row padding and its removal, and fixed-tape workspace cleanup. Its tape count is fixed, and its time constant is independent of the allowed array lengths and coefficient values. \end{proposition}

- "The second procedure applies" (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.


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

Write the body to `exegenius/tasks/0028-write-simultaneous-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0028-write-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0028-write-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0028-write-simultaneous-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
