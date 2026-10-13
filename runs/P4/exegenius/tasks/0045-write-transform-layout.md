# exegenius task 0045-write-transform-layout

Project directory: `/home/user/openai-nlogn-wiki/runs/P4` (paths below are relative to it)

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

For these sources: The reader has finished a standard undergraduate computer science degree: discrete mathematics (induction, counting, modular arithmetic, primes, gcd, permutations, basic graphs), algorithms (asymptotic notation, divide and conquer, recurrences, sorting including radix sort, the idea of the FFT and Karatsuba multiplication at survey level), calculus and basic real analysis (limits, logarithms, exponentials, floors and ceilings, inequalities), introductory linear algebra and probability, and the basics of Turing machines and complexity. They have not studied abstract algebra beyond arithmetic mod n, coding theory, or number-theoretic transforms in depth, and have not met the multitape fast-multiplication literature (Schönhage–Strassen, Fürer, Harvey–van der Hoeven), Gaussian resampling, or Nussbaumer polynomial transforms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape Turing machine model
- The n log n optimality conjecture
- Established near-linear integer multiplier
- Matrices, rank, subspaces and projections
- Tensor products of vectors, spaces and operators
- Binary vectors, XOR and Hamming weight
- Nondegenerate bilinear forms and orthogonal complements
- Discrete Fourier transform
- Multidimensional transform and cyclic convolution on a product of axes
- Butterfly step and decimation-in-frequency recursion
- Max-modulus norm, contractions and error propagation
- Disk grid and truncation
  - $p$ (precision bits): the number of fractional bits kept in each real or imaginary part
  - $\mathbb D_p$ (p-bit disk grid): the set of complex numbers 2^{-p}(a+ib) with integers a,b lying in the closed unit disk
  - $Q_p$ (truncation operator): the map that truncates the real and imaginary parts of each coefficient toward zero to multiples of 2^{-p}
- Streaming fixed-point and Gaussian dyadic arithmetic
- Arrays, address fields, rows and logical volume
- Linear-time stream operations
- Controlled cyclic shifts and rational scalings
- Depth-first recursion schedule on fixed tapes
- Triple-intersection pairing formulas
- Linear network exchanging two banks with restored scratch
- Frames and the common-frame identity
- Nested subspace labels and the rank deficit
- Address shear
- Bit network and rational shear interface
- Phase kernel C = aI + bX
  - $C$ (phase kernel): the two-by-two matrix H S H acting on one selected bit
  - $a$ (kernel coefficient a): the complex number (1+i)/2 multiplying the identity
  - $b$ (kernel coefficient b): the complex number (1−i)/2 multiplying the bit flip
  - $I$ (identity matrix): the two-by-two identity matrix
  - $X$ (bit-flip matrix): the two-by-two matrix interchanging the two coordinates
- Complex phase network interface
- Lower-triangular factorization of a matrix
- Cost of a rational matrix shear
- Strict rank deficit gives a power saving
- Rows distributed cyclically among wire roles
- Power-width interchange with rows
- Fast address-chunk interchange
- Carry-free packed controlled rotations
- Deterministic repair of exceptional addresses
- Packed selected-bit addition on one rectangle
- Guard width for exact intermediate values
- Recursive phase-frame layer on slots
- Simultaneous normalized butterfly layer
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): the indeterminate of the polynomial ring, satisfying y^r = −1
  - $r$ (polynomial length): the number of complex coefficients in a record, a power of two
- Synthetic root of unity ω_t = y^{2r/t}
  - $\omega_t$ (synthetic root): the element y^{2r/t} acting as a primitive t-th root of unity in the ring
  - $t$ (transform length): the length of the axis, a power of two dividing 2r
  - $y$ (ring variable): the indeterminate of the polynomial ring, satisfying y^r = −1
  - $r$ (polynomial length): the number of complex coefficients in a record, a power of two
- Synthetic polynomial transform
- Retained stored frequency order
- Asymptotic notation beyond big-O (also: Theta, Omega, little-o, Θ, Ω, o(1), liminf, eventual lower bound)
- Logarithms, exponentials, floors and ceilings (also: log base 2, lg n, floor, ceiling, change of base, iterated logarithm)
- Binary and radix-b representation of integers (also: positional notation, base-b digits, mixed radix, bit length, val(x))
- Schoolbook multiplication and Karatsuba (also: grade-school multiplication, long multiplication, quadratic multiplication, Karatsuba-Ofman, Toom-Cook)
- Divisibility, primes and gcd (also: coprime, relatively prime, greatest common divisor, Euclidean algorithm, trial division, prime number)
- Modular arithmetic and residue classes (also: integers mod n, Z/nZ, congruence, mod Q, remainder, division with remainder, residue ring)
- Roots of unity (also: primitive root of unity, n-th roots of unity, e^{2πi/n}, twiddle factors)
- Recurrences and geometric series (also: divide-and-conquer recurrence, master theorem, solving recurrences, geometric sum, T(n) = aT(n/b) + f(n))
- Induction and elementary proof technique (also: proof by induction, structural induction, contradiction, pigeonhole principle)
- Elementary counting and the union bound (also: binomial coefficients, counting subsets, inclusion–exclusion, union bound, fraction of a finite set, Boole's inequality)
- Sorting and radix sort (also: stable sort, radix sort, counting sort, sorting by key, bucket sort)
- Permutations and bijections (also: index permutation, bit reversal, inverse permutation, permutation matrix, one-to-one correspondence)
- Sets, products of ranges and lexicographic order (also: Cartesian product, index set [n], multi-index, lexicographic order, row-major order)
- Matrix transposition and row-major storage (also: transpose, k×k binary matrix, row-major matrix)
- Triangle inequality and error bounds (also: absolute error, rounding error, approximation error, supremum, modulus inequality, rounding to nearest integer)
- Boolean and arithmetic circuits as networks (also: logic gates, XOR gate, circuit, wires and gates, directed acyclic graph, fan-in and fan-out)
- Graphs, paths and neighbors (also: directed graph, edges and vertices, adjacent vertices, route in a graph)
- Stacks and recursion (also: call stack, LIFO, push and pop, depth-first traversal, recursive procedure)
- Fast Fourier transform and Karatsuba as survey knowledge (also: FFT multiplication, Schönhage–Strassen, polynomial multiplication via evaluation, evaluation and interpolation)
- Real and imaginary parts, rounding and truncation (also: Re and Im, truncate toward zero, nearest integer, fixed-point numbers)
- Dot product, vectors over the rationals and orthonormal bases (also: inner product, orthogonal vectors, standard basis, Gram–Schmidt, bilinear pairing)

## This page

Concept: Transform layout and cost
Gloss: A positional permutation L moves chosen bit slots to a prefix and groups the remaining bits into K-bit chunks so each transform round is a simultaneous butterfly layer; cost O(Tp[dK + pK^{τ−1} + ℓ d^{λ'}]) with error below √2·ℓ·2^{−p}.

## This page in the argument

The step: A positional permutation $L$ moves chosen bit slots to a prefix and groups the remaining bits into $K$-bit chunks so that each transform round is a simultaneous butterfly layer; each transform costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\,\ell\,2^{-p}$.
How: Move the top slots of each axis to a prefix, interleave the remaining chunks of the axes by chunk interchanges so that equal chunk indices are adjacent, then run one simultaneous layer per round and individual butterflies on the prefix rounds.
Why: The simultaneous layer applies one butterfly to the same bit offset in consecutive chunks, so the participating axes' selected bits must be placed at a common offset in consecutive $K$-bit chunks. (the sources say so: "we must place the selected bits of the participating axes at a common" (paper))

Its sub-steps, in order:

- The axis steps of one round group into a parallel butterfly followed by a single recordwise monomial multiplication $J_E$ whose exponent depends only on the address.
- A list of at most $D(b+1)=O(dK)$ slots is moved to a prefix, leaving each axis as consecutive $K$-bit chunks.
- Scanning the target positions and exchanging chunks reorders the axes' chunks using at most $Dq-1$ interchanges, costing $O(Tp\,pK^{\tau-1})$.
- Each round on the remaining chunks is one call of the simultaneous layer, costing $O(Tp\,d^{\lambda'})$, hence $O(Tp\,\ell d^{\lambda'})$ in total.
- The monomial $y^E$ is a split of the coefficient list into two pieces, a negation of the tail and a merge in the other order, costing $O(rp)$ per record.
- Truncation commutes with the signed coefficient permutation, so one truncation after each exact round gives error below $\sqrt2\,\ell\,2^{-p}$ over at most $\ell$ rounds.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce multiplication to convolution over $\mathbb C[y]/(y^r+1)$ through radix digits, Chinese-remainder axes, Gaussian resampling and chirps, speed up the data movement and the butterfly arithmetic with two network-based tape procedures with a strict rank saving, recover the exact product by rounding and carries, and add up the costs. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ over $\mathcal R_r$ on disk-grid arrays is approximated with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.; how: Apply the forward synthetic transform to both operands and keep their layout, multiply the corresponding length-$r$ records pointwise by signed packing, and apply the opposite transform, which consumes the same stored order. (on [Convolution from the retained transform layout](synthetic-convolution.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (H3.1, H3.2, H3.3, H3.4, H3.5, H3.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**H3.1**: The axis steps of one round group into a parallel butterfly followed by a single recordwise monomial multiplication $J_E$ whose exponent depends only on the address.
Source: "Consequently the individual axis steps may be grouped as a parallel" (paper)
> For $D$ axes of lengths $t_1,\ldots,t_D$, put \[ M=\prod_{i=1}^D t_i,\qquad F_{\boldsymbol t}^\pm=\bigotimes_{i=1}^D F_{t_i}^\pm, \qquad B=\bigotimes_{i=1}^D B_{t_i}. \] A round applies one current $H_0$ on each participating axis. The twiddle for axis $i$ depends only on that axis's address bits. The two entries paired by another axis's butterfly have the same axis-$i$ address, so that twiddle commutes with the other butterfly. Consequently the individual axis steps may be grouped as a parallel butterfly $\mathcal H$, followed by one recordwise monomial operation $J_E$. At each address, $J_E$ multiplies the record by \begin{equation} y^{E},\qquad E=-\sum_{i\ \mathrm{participating}} \frac{2r}{u_i}\,b_i k_i\pmod{2r}. \label{eq:combined-twiddle} \end{equation} Here $u_i$ is that axis's current recursive length, $b_i$ its newly written branch bit, and $0\leq k_i<u_i/2$ is encoded by its still unprocessed named slots. The exponent depends on the address, not on coefficient values. In the opposite direction the grouped round is $\mathcal HJ_E^{-1}$: apply $y^{-E}$ first and the parallel butterfly second. Each $\mathcal H$ is a contraction and each $J_E$ is an isometry, so every completed round is a contraction.

**H3.2**: A list of at most $D(b+1)=O(dK)$ slots is moved to a prefix, leaving each axis as consecutive $K$-bit chunks.
Source: "Form a list of the slots to move to a prefix.  First list" (paper)
> on} Both layout construction and final restoration are charged in this bound. The forward procedure may retain its output layout for a pointwise product and the following opposite procedure. \end{lemma} \begin{proof} Put $D=d-1$ and write $a_i=\log_2t_i$. The supplied encoding has $2w=\Theta(p)$ bits per coefficient, so the logical bit volume is $\Theta(Tp)$. Call an axis long if $a_i=\ell$ and short if $a_i=\ell-1$. Name the original bit slots of axis $i$ by $(i,h)$, $a_i-1\geq h\geq0$. Initially these slots are in axis order and, within each axis, in decreasing $h$. The coefficients of each polynomial form a contiguous suffix. Put \[ b=(\ell-1)\bmod K, \qquad q=\lfloor(\ell-1)/K\rfloor. \] Form a list of the slots to move to a prefix. First list $(i,\ell-1)$ for the length-$2^\ell$ axes in increasing $i$. Then list $(i,h)$ for $h=b-1,\ldots,0$, and within each $h$ in increasing $i$; this second list is empty if $b=0$. Move each listed slot immediately after the prefix already formed, leaving all other slots in their relative order. There are at most $D(b+1)=O(dK)$ listed slots, so the moves cost $O(TpdK)$. A descriptor records the physical position of every named slot. The part of each axis left outside the prefix now consists of $q$ consecutive $K$-bit chunks.

**H3.3**: Scanning the target positions and exchanging chunks reorders the axes' chunks using at most $Dq-1$ interchanges, costing $O(Tp\,pK^{\tau-1})$.
Source: "To obtain this order, scan its target positions from left to right." (paper)
> Number the axes by $i$ and their chunks, from high to low, by $j$. The remaining physical order changes from \[ (1,1),(1,2),\ldots,(1,q),(2,1),\ldots,(D,q) \quad\hbox{to}\quad (1,1),(2,1),\ldots,(D,1),(1,2),\ldots,(D,q). \] To obtain this order, scan its target positions from left to right. At each position except the last, exchange the chunk currently there with the required chunk if they differ. This uses at most $Dq-1$ exchanges of width-$K$ address chunks, even when the chunks are nonadjacent. Each costs $O(TpK^\tau)$, so all these exchanges cost \[ O\bigl(Tp\,DqK^\tau\bigr) =O\bigl(Tp\,pK^{\tau-1}\bigr). \] These prefix moves and chunk exchanges define $L$. We use the same letter for its induced record permutation: a record at address $x$ moves to address $Lx$, while its polynomial suffix stays intact. Recording the inverse operations in reverse order gives $L^{-1}$ with the same cost.

**H3.4**: Each round on the remaining chunks is one call of the simultaneous layer, costing $O(Tp\,d^{\lambda'})$, hence $O(Tp\,\ell d^{\lambda'})$ in total.
Source: "The simultaneous-layer procedure therefore applies at cost" (paper)
> For a position $h$ in the remaining chunks, the selected bit has offset $(h-b)\bmod K$, counted from the least significant bit, in each of the $D$ consecutive chunks with the same chunk index $j$. Let $n_P$ and $n_S$ be the numbers of record-address bits before and after that group. Every combination of those bits occurs, so the layer sees the complete address set \[ [P]\times[2^K]^D\times[S],\qquad P=2^{n_P},\quad S=2^{n_S},\quad n_P+DK+n_S=\sum_i a_i\leq D\ell=O(p). \] Thus its record count is $PS2^{DK}=M$ and $\log_2(2M)\leq(C_\ell+1)p=C_Mp$. The current transform parameters supply $p,d,r,K,w$, and the round determines $D,P,S$ and the selected offset $\rho$. Encode these values as the header $\mathcal E$ of Proposition~\ref{prop:simultaneous-layer}. The same fixed descriptor bound covers every axis choice and round. Indeed $|\Gamma(v)|\leq2\log_2v+1$, and $\ell+n_P+n_S\leq d\ell\leq C_\ell p$. Also $d,D\leq\max\{C_\ell,1\}p$, $K,\rho+1\leq p$, and $w\leq C_wp$. Adding the nine code lengths therefore gives \[ |\mathcal E| \leq 2C_\ell p+12\log_2p+ 4\log_2\max\{C_\ell,1\}+2\log_2C_w+9 \leq C_{\rm desc}p. \] The last inequality uses $p\geq1$, $\log_2p\leq p$, and $\log_2x\leq x$ for $x\geq1$. This is the descriptor passed to the layer; the longer table locating named slots remains separate for the transform's address calculations. The simultaneous-layer procedure therefore applies at cost $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.

**H3.5**: The monomial $y^E$ is a split of the coefficient list into two pieces, a negation of the tail and a merge in the other order, costing $O(rp)$ per record.
Source: "To implement the monomial, write $E=er+s$ with $0\leq s<r$." (paper)
> To implement the monomial, write $E=er+s$ with $0\leq s<r$. Split the coefficient list before position $r-s$, put its tail before its head, negate the moved tail, and apply the common sign $(-1)^e$. This is multiplication by $y^E$ modulo $y^r+1$. There are always two pieces. Splitting them to two tapes and merging in that order costs $O(rp)$ per record, including head returns; $s=0$ is an ordinary signed copy. The inverse twiddle uses the same split and merge with exponent $-E$, and no coefficient sort is required.

**H3.6**: Truncation commutes with the signed coefficient permutation, so one truncation after each exact round gives error below $\sqrt2\,\ell\,2^{-p}$ over at most $\ell$ rounds.
Source: "Thus the actual forward call sequence returns exactly the result of" (paper)
> For a forward round on a group of $D$ chunks, the layer call returns $Q_p(\mathcal H z)$ and the next operation is $J_E$. Truncation toward zero is odd and acts separately on every real and imaginary part. Since $J_E$ is a signed coefficient permutation, it follows that \[ J_EQ_p(\mathcal H z)=Q_p(J_E\mathcal H z). \] Thus the actual forward call sequence returns exactly the result of truncating once after the exact contraction round. In the opposite direction, $J_E^{-1}$ first preserves the disk grid, and the layer call returns $Q_p(\mathcal HJ_E^{-1}z)$ directly. The rounds on prefix slots have the same forms, with one truncation, by their exact evaluation above. A contraction does not increase the norm of the difference between the computed and exact arrays; the single truncation then adds less than $\sqrt2\,2^{-p}$ by \eqref{eq:transform-truncate}. Both the contraction and truncation preserve the disk. Starting with zero error, at most $\ell$ rounds therefore give the claimed error and disk bounds. The layout permutations are isometries and add no numerical error.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Simultaneous normalized butterfly layer](simultaneous-layer.md): H₀ is applied at once to the same bit offset of D ≤ d address chunks of every polynomial record in O(V d^{λ'}) time with λ'<1, via H₀^{⊗D} = b^D S_D C^{⊗D} S_D, the recursive phase-frame layer on rows split among wire roles, exact evaluation and one final truncation.
  Shown as: Transform layout and cost *<predicate>* Simultaneous normalized butterfly layer
- [Fast address-chunk interchange](chunk-swap.md): Arbitrary-width interchange of two disjoint address chunks of u bits in O(V u^τ) with fixed τ<1: peel off top digits to supply rows, pad rows, decompose the rest in base m and apply the power-width interchange to each piece.
  Shown as: Transform layout and cost *<predicate>* Fast address-chunk interchange
- [Synthetic polynomial transform](synthetic-transform.md): The normalized transforms F_t^± over the polynomial ring using synthetic roots, computed by radix-two butterflies plus monomial twiddles (Nussbaumer–Quandalle); character cancellation gives F⁺F⁻ = I/t even though the ring has zero divisors.
  Shown as: Transform layout and cost *<predicate>* Synthetic polynomial transform
- [Retained stored frequency order](frequency-order.md): The decimation-in-frequency recursion writes frequency j in slot rev(j) (bit-reversed); the forward transform B·F⁻ keeps this order and the opposite procedure consumes it directly, so no sort is needed between the pointwise product and the inverse.
  Shown as: Transform layout and cost *<predicate>* Retained stored frequency order
- [Disk grid and truncation](disk-grid-truncation.md): Fixed-point complex numbers with p fractional bits inside the unit disk, and the operator that truncates real and imaginary parts toward zero to that grid, never increasing norm and causing error below √2·2^{−p}.
  Shown as: Transform layout and cost *<predicate>* Disk grid and truncation

## Pages that build on this one

- Convolution from the retained transform layout: Normalized convolution over the polynomial ring: two forward synthetic transforms keep their layout, records are multiplied pointwise by signed packing, and the opposite transform consumes the same order; error below √2·M(3ℓ+1)2^{−p}.
- Cost analysis and the exponent κ: Dividing all costs by Tp = Θ(n) gives a table of seven dominant terms whose powers of p are all at most 1 − 2κ for κ = 2^{−182}, so the total is O(n (lg n)^{1−κ}) with schoolbook multiplication for small inputs.

## Other pages you may link to

- [Fixed-tape Turing machine model](multitape-model.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Streaming fixed-point and Gaussian dyadic arithmetic](fixed-point-arithmetic.md)
- [Established near-linear integer multiplier](established-multiplier.md)
- [Arrays, address fields, rows and logical volume](address-fields-volume.md)
- [Linear-time stream operations](stream-ops.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Matrices, rank, subspaces and projections](linear-algebra-basics.md)
- [Tensor products of vectors, spaces and operators](tensor-products.md)
- [Address shear](address-shear.md)
- [Binary vectors, XOR and Hamming weight](f2-vectors.md)
- [Nondegenerate bilinear forms and orthogonal complements](bilinear-orthogonality.md)
- [Triple-intersection pairing formulas](subset-pairing-formulas.md)
- [Linear network exchanging two banks with restored scratch](scalar-exchange-network.md)
- [Frames and the common-frame identity](network-frames.md)
- [Rows distributed cyclically among wire roles](row-splitting-roles.md)
- [Nested subspace labels and the rank deficit](subspace-labels-rank-saving.md)
- [Strict rank deficit gives a power saving](rank-deficit-recurrence.md)
- [Bit network and rational shear interface](bit-network-interface.md)
- [Lower-triangular factorization of a matrix](lower-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Depth-first recursion schedule on fixed tapes](fixed-tape-dfs-schedule.md)
- [Power-width interchange with rows](power-width-interchange.md)
- [Carry-free packed controlled rotations](packed-rotations.md)
- [Deterministic repair of exceptional addresses](exceptional-address-repair.md)
- [Packed selected-bit addition on one rectangle](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-negacyclic.md)
- [Discrete Fourier transform](dft.md)
- [Synthetic root of unity ω_t = y^{2r/t}](synthetic-roots.md)
- [Butterfly step and decimation-in-frequency recursion](fft-butterfly.md)
- [Phase kernel C = aI + bX](phase-kernel.md)
- [Complex phase network interface](complex-network-interface.md)
- [Recursive phase-frame layer on slots](phase-frame-layer.md)
- [Multidimensional transform and cyclic convolution on a product of axes](multidim-dft.md)
- [Max-modulus norm, contractions and error propagation](contraction-error-budget.md)
- [Guard width for exact intermediate values](guard-width.md)
- [Signed Kronecker packing for ring products](signed-packing.md)
- [Gaussian resampling with retained permutations](gaussian-resampling.md)
- [Tensor interface for resampling](tensor-resampling.md)
- [Cyclic convolution and the convolution theorem](cyclic-convolution.md)
- [Integer multiplication as convolution of radix digits](multiplication-as-convolution.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Cancellation of the source permutation](source-permutation-cancel.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Size parameters of the algorithm](parameter-choice.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Distinct prime source lengths near powers of two](prime-lengths.md)
- [Coefficient twist from cyclic to negacyclic](coefficient-twist.md)
- [Middle transform computed by chirp and complex convolution](chirp-transform.md)
- [Source transform procedure](source-transform.md)
- [Exact recovery by rounding and carry propagation](exact-recovery.md)
- [The complete multiplication algorithm](multiplication-algorithm.md)
- [Cost analysis and the exponent κ](cost-analysis.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "layout permutation $L$ of record addresses" (paper)

  > The procedure constructs an explicit positional layout permutation $L$ of record addresses, preserving their polynomial suffixes, and transforms disk grid arrays of $M$ contiguous degree-less-than-$r$ polynomial records. Its exact counterpart is $LB F_{\boldsymbol t}^-$. Its opposite procedure consumes that order and has exact counterpart $F_{\boldsymbol t}^+B^{-1}L^{-1}$. Each procedure has error less than $\sqrt2\ell\,2^{-p}$, returns disk grid coefficients in the same component format, and costs \begin{equation} O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right). \label{eq:synthetic-transform-cost} \end{equation} Both layout construction and final restoration are charged in this bound. The forward procedure may retain its output layout for a pointwise product and the following opposite pro

- "Transform layout and cost" (paper)

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

Write the body to `exegenius/tasks/0045-write-transform-layout.answer.md` and the JSON to `exegenius/tasks/0045-write-transform-layout.answer.json`, then run `exegenius submit 0045-write-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0045-write-transform-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
