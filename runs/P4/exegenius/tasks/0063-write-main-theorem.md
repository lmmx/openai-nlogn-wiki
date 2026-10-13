# exegenius task 0063-write-main-theorem

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
- Cyclic convolution and the convolution theorem
- Butterfly step and decimation-in-frequency recursion
- Integer multiplication as convolution of radix digits
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
- Transform layout and cost
- Signed Kronecker packing for ring products
- Convolution from the retained transform layout
- Coefficient twist from cyclic to negacyclic
- Gaussian resampling with retained permutations
- Tensor interface for resampling
- Bluestein chirp identity
- Cancellation of the source permutation
- Chinese-remainder map to prime cyclic axes
- Middle transform computed by chirp and complex convolution
- Source transform procedure
- Size parameters of the algorithm
- Distinct prime source lengths near powers of two
- Exact recovery by rounding and carry propagation
- The complete multiplication algorithm
- Cost analysis and the exponent κ
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

Concept: Integer multiplication in O(n (lg n)^(1−κ)) time
Gloss: A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, by reducing to convolution over the polynomial ring with fast chunk interchanges and simultaneous butterfly layers, disproving the n log n optimality conjecture.
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): the number of bits in each of the two integers being multiplied
- $\kappa$ (saving exponent): the fixed constant 2^{-182} giving the power saving in the logarithmic factor

## This page in the argument

The step: A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.
How: Reduce multiplication to convolution over $\mathbb C[y]/(y^r+1)$ through radix digits, Chinese-remainder axes, Gaussian resampling and chirps, speed up the data movement and the butterfly arithmetic with two network-based tape procedures with a strict rank saving, recover the exact product by rounding and carries, and add up the costs.
Why: Scanning the whole array at each of the logarithmically many transform levels already costs $n\log n$, so both the data movement and the arithmetic need savings. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))

Its sub-steps, in order:

- Two tape procedures exist for fixed exponents $\tau,\lambda'<1$: one interchanges two disjoint address chunks of $u$ bits in $O(Vu^\tau)$ time, and one applies a normalized butterfly layer on up to $d$ address chunks in $O(Vd^{\lambda'})$ time, where $V$ is the logical bit volume.
- Normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ over $\mathcal R_r$ on disk-grid arrays is approximated with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$. (on [Convolution from the retained transform layout](synthetic-convolution.md))
- Fourier transforms of pairwise coprime lengths $s_i$ can be replaced by transforms of power-of-two lengths $t_i$ using Gaussian resampling, with the source and target permutations retained in the identity and the middle transform computed as a chirp convolution.
- Convert the inputs to radix-$2^b$ digits, map them to the prime axes by the CRT map, compute the two source transforms, multiply pointwise, compute the opposite transform, rescale by $S$ and $2^{2b+4}$, round, undo the CRT map and propagate carries to output the exact $2n$-bit product. (on [The complete multiplication algorithm](multiplication-algorithm.md))
- The scaled computed convolution has error below $1/2$, so rounding each real part to the nearest integer gives the true integer coefficients, and carries propagated from the least significant digit produce the exact $2n$-bit product. (on [Exact recovery by rounding and carry propagation](exact-recovery.md))
- Dividing all costs by $Tp=\Theta(n)$ gives a table of seven dominant terms whose powers of $p$ are at most $1-2\kappa$ for $\kappa=2^{-182}$, so the total is $O(n(\lg n)^{1-\kappa})$, with schoolbook multiplication below a cutoff. (on [Cost analysis and the exponent κ](cost-analysis.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (G1, G3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**G1**: Two tape procedures exist for fixed exponents $\tau,\lambda'<1$: one interchanges two disjoint address chunks of $u$ bits in $O(Vu^\tau)$ time, and one applies a normalized butterfly layer on up to $d$ address chunks in $O(Vd^{\lambda'})$ time, where $V$ is the logical bit volume.
How: Obtain both from one fixed linear network that exchanges two banks of values and restores every auxiliary value, whose edge frame changes are smaller calls of the same procedure; the strict inequality $s<Wm$ on their number gives a recursion with a power saving.
- N: There are two fixed linear networks, one over bits and one over Gaussian dyadics, that exchange two banks of values while restoring every scratch wire, and whose array versions have total frame-change rank $s$ strictly below $W\cdot m$ for $W$ wires and an $m$-dimensional label space.
  How: Build the scalar exchange network first, lift it to arrays with frames, then choose nested subspace labels that make the frame changes cheap, and read off the bit and complex interfaces.
  - N6: The relative rank deficits of both networks exceed $20\cdot 2^{-50}$, so $s/W<m^\tau$ holds with the fixed exponent $\tau=1-2^{-50}$.
    Source: "Both exact deficits displayed above are greater than $20\cdot2^{-50}$." (paper)
    > The relative rank deficits are \[ \eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m} =\frac{339}{22587335000000},\qquad \eta_{\rm c}=\frac{W_{\rm c}m-s_{\rm c}}{W_{\rm c}m} =\frac{73}{19906842167500}. \] For both recurrences we may use the fixed rational exponent \begin{equation} \tau=\sigma=1-2^{-50}. \label{eq:explicit-motif-exponents} \end{equation} Both exact deficits displayed above are greater than $20\cdot2^{-50}$. Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence \[ m^{1-2^{-50}} =m\exp(-2^{-50}\log m) >m(1-20\cdot2^{-50})>m(1-\eta) \] for either $\eta=\eta_{\rm b}$ or $\eta=\eta_{\rm c}$. Consequently \[ \frac{s_{\rm b}}{W_{\rm b}}<m^\tau, \qquad \frac{s_{\rm c}}{W_{\rm c}}<m^\sigma, \qquad 0<\tau=\sigma<1. \] Here $\sigma$ is a rational upper bound for the logarithmic exponent of the complex recurrence. \section{Faster interchange of address chunks} \label{sec:tape-interchange}

**G3**: Fourier transforms of pairwise coprime lengths $s_i$ can be replaced by transforms of power-of-two lengths $t_i$ using Gaussian resampling, with the source and target permutations retained in the identity and the middle transform computed as a chirp convolution.
How: Apply Gaussian resampling along each axis with both coordinate permutations kept inside the transform identity, evaluate the middle transform by Bluestein's chirp as a cyclic convolution, and cancel the source permutation across the convolution.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- H (on [Convolution from the retained transform layout](synthetic-convolution.md)): Normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ over $\mathcal R_r$ on disk-grid arrays is approximated with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.
- A (on [The complete multiplication algorithm](multiplication-algorithm.md)): Convert the inputs to radix-$2^b$ digits, map them to the prime axes by the CRT map, compute the two source transforms, multiply pointwise, compute the opposite transform, rescale by $S$ and $2^{2b+4}$, round, undo the CRT map and propagate carries to output the exact $2n$-bit product.
- E (on [Exact recovery by rounding and carry propagation](exact-recovery.md)): The scaled computed convolution has error below $1/2$, so rounding each real part to the nearest integer gives the true integer coefficients, and carries propagated from the least significant digit produce the exact $2n$-bit product.
- K (on [Cost analysis and the exponent κ](cost-analysis.md)): Dividing all costs by $Tp=\Theta(n)$ gives a table of seven dominant terms whose powers of $p$ are at most $1-2\kappa$ for $\kappa=2^{-182}$, so the total is $O(n(\lg n)^{1-\kappa})$, with schoolbook multiplication below a cutoff.
- T1 (on [Linear-time stream operations](stream-ops.md)): Splitting on a digit, applying a fixed pointwise map to aligned streams, merging, moving one digit, and splitting rows cyclically into $W$ streams each cost $O(V)$ steps on a fixed number of tapes, for an array of volume $V$.
- T2 (on [Controlled cyclic shifts and rational scalings](controlled-shifts.md)): A target field updated by $y\mapsto y+a(\text{controls})\bmod Q$, with the controls earlier on the tape than the target, costs $O(V)$, and so does multiplication by a fixed rational unit modulo $q^b$.
- N1 (on [Linear network exchanging two banks with restored scratch](scalar-exchange-network.md)): A fixed network of copy, gather, scatter and side-injection gates on banks $X$ and $Y$ sends $(X_a,Y_a)$ to $(-Y_a,X_a)$ in three stages and restores every scratch wire to its arbitrary initial value.
- N2 (on [Frames and the common-frame identity](network-frames.md)): If each wire's scalar is replaced by an array and every gate and terminal carries an invertible frame operator, the network acts as $D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}$, so only the endpoint frames matter and each edge from $u$ to $v$ is implemented by $D_vD_u^{-1}$.
- N3 (on [Nested subspace labels and the rank deficit](subspace-labels-rank-saving.md)): Gates and terminals can be labelled by nested nondegenerate subspaces of the $m$-dimensional space $\mathcal F=F^{\otimes 3}$, built from tensor powers of triple indicator vectors, so that the total dimension change over the edges of a network with $W$ wires is below $W\cdot m$.
- N4 (on [Bit network and rational shear interface](bit-network-interface.md)): The bit network with $W_{\rm b}$ XOR-gate wires and rational projection matrices on gates and terminals sends its input to the role-permuted vector, obeys $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ for every input role $w$, and has total edge rank $s_{\rm b}<W_{\rm b}m$.
- N5 (on [Complex phase network interface](complex-network-interface.md)): In the Gaussian-dyadic network with binary-vector labels and phase frames $i^{\mathrm{wt}(P_Ux)\bmod 4}$, each edge's frame change is a product of translation kernels $aI+bX_v$ over an orthonormal basis of the residual, the lengths sum to $s_{\rm c}<W_{\rm c}m$, and telescoping gives $C^{\otimes m}$ on every role.
- C1 (on [Fast address-chunk interchange](chunk-swap.md)): There is a fixed $\tau<1$ and one fixed multitape procedure that interchanges two disjoint address chunks of $u$ bits, $(p,h,g,d,z)\mapsto(p,d,g,h,z)$, in $O(Vu^\tau)$ steps on an arbitrary bit array of volume $V$.
- L (on [Simultaneous normalized butterfly layer](simultaneous-layer.md)): The normalized butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ can be applied at once to the same bit offset of $D\le d$ address chunks of every polynomial record in $O(Vd^{\lambda'})$ time with $\lambda'<1$, exactly up to one final truncation.
- I1 (on [Gaussian resampling with retained permutations](gaussian-resampling.md)): For coprime lengths $s<t$ with $t/s-1>p/\alpha^4$ there are contractions $A$ and $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, and algorithms approximating them with error below $p^2$ in time $O(tp^{3/2+\delta}\alpha)$.
- I2 (on [Tensor interface for resampling](tensor-resampling.md)): Applying the resampling identity along each of $d$ axes of a padded power-of-two box gives $R F_{\boldsymbol s}=2^\gamma\mathcal B_0 QF_{\boldsymbol t}\mathcal A$ with line-map cost $O(dTp^{3/2+\delta}\alpha)$ and data movement $O(Tp\,d^2(1+\ell^\tau))$.
- I3 (on [Bluestein chirp identity](bluestein-chirp.md)): For the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$ one has $QF_{\boldsymbol t}u=\overline a\cdot\bigl(a*(\overline a\cdot u)\bigr)/T$, so the middle transform with its frequency permutation is a normalized cyclic convolution between two phase products.
- I4 (on [Cancellation of the source permutation](source-permutation-cancel.md)): The retained source permutation $R$ cancels across the two forward source transforms, their pointwise product and the opposite-sign transform: $(RF_{\boldsymbol s}^+)\bigl[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)\bigr]=(u*v)/S^2$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The complete multiplication algorithm](multiplication-algorithm.md): Convert the inputs to radix digits, apply the CRT map to prime axes, compute the two source transforms, multiply pointwise, compute the opposite transform, rescale by S and 2^{2b+4}, round, undo the CRT map and propagate carries to output the exact product.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* The complete multiplication algorithm
- [Cost analysis and the exponent κ](cost-analysis.md): Dividing all costs by Tp = Θ(n) gives a table of seven dominant terms whose powers of p are all at most 1 − 2κ for κ = 2^{−182}, so the total is O(n (lg n)^{1−κ}) with schoolbook multiplication for small inputs.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Cost analysis and the exponent κ
- [The n log n optimality conjecture](nlogn-conjecture.md): Schönhage and Strassen's 1971 conjecture that Θ(n log n) is the optimal time to multiply two n-bit integers on a multitape Turing machine; Harvey and van der Hoeven reached O(n log n), and this paper refutes optimality.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* The n log n optimality conjecture
- [Fixed-tape Turing machine model](multitape-model.md): The paper's cost model: one fixed finite alphabet, a fixed finite number of one-dimensional tapes, each step reads/writes one cell per tape and moves each head by at most one cell, so moving data far costs time.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Fixed-tape Turing machine model

## Other pages you may link to

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
- [Fast address-chunk interchange](chunk-swap.md)
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
- [Synthetic polynomial transform](synthetic-transform.md)
- [Retained stored frequency order](frequency-order.md)
- [Max-modulus norm, contractions and error propagation](contraction-error-budget.md)
- [Disk grid and truncation](disk-grid-truncation.md)
- [Guard width for exact intermediate values](guard-width.md)
- [Simultaneous normalized butterfly layer](simultaneous-layer.md)
- [Transform layout and cost](transform-layout.md)
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

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers
in $O(n(\lg n)^{1-\kappa})$ worst-case time, with
$\kappa=2^{-182}$" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right)," (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}


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

Write the body to `exegenius/tasks/0063-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0063-write-main-theorem.answer.json`, then run `exegenius submit 0063-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0063-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
