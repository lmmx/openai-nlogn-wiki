# exegenius task 0050-write-exact-recovery

Project directory: `/home/user/openai-nlogn-wiki/runs/Q2` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education. In discrete mathematics they have sets, counting and binomial coefficients, induction, graphs, modular arithmetic, gcd and the extended Euclidean algorithm, primes and the Chinese remainder theorem. In algorithms and theory they have worst-case analysis, recurrences, sorting, stacks, binary counters, schoolbook and Karatsuba multiplication, Boolean circuits and the multitape Turing machine with its constant-factor simulations, and in computer arithmetic they have binary, two's-complement and fixed-point numbers with carries. They have also taken a first course in linear algebra over the reals (vector spaces, matrices, Gaussian elimination, triangular matrices, eigenvalues, dot products, projections) and calculus (limits, series, exponentials, Newton's method), plus complex numbers with Euler's formula. They have not studied bilinear forms over finite fields, tensor products, ring theory beyond the integers mod n, Fourier analysis or FFT internals, numerical error analysis, or the integer-multiplication literature after Karatsuba.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine (also: fixed finite-tape model)
- Exact binary multiplication problem
- Schönhage–Strassen optimality conjecture (also: n log n optimality conjecture)
- Harvey–van der Hoeven multiplier (also: established O(n log n) multiplier)
- Cyclic convolution
- Radix-digit reduction to convolution
- Matrix rank (also: rational rank)
- Tensor product of linear maps
- The binary field F₂ and XOR (also: F2, XOR combinations)
- Nondegenerate bilinear spaces and orthogonal complements
- Normalized discrete Fourier transform (also: DFT, Fourier transform)
- Normalized butterfly H₀ (also: butterfly, two-point butterfly)
  - $H_0$ (normalized butterfly): The two-point linear map sending (u, v) to ((u+v)/2, (u−v)/2), i.e. half the 2×2 Hadamard matrix.
- Decimation-in-frequency FFT and bit-reversed order (also: bit reversal, B_t)
- Polynomial ring modulo yʳ + 1 (also: R_r, negacyclic ring)
  - $y$ (polynomial variable): The indeterminate of the ring, whose powers act as roots of unity because y to the r equals −1.
  - $r$ (record length): The number of complex coefficients in each polynomial record, a power of two.
- Synthetic roots of unity
- Synthetic polynomial transform (also: Nussbaumer transform, synthetic transform)
- Gaussian dyadic numbers
- Disk grid and truncation (also: D_p, Q_p, p-bit grid)
- Contractions and error accounting
- Signed Kronecker substitution (also: signed packing)
- Lexicographic array layout and logical volume (also: logical volume, address field, row)
- Elementary stream operations
- Controlled cyclic shifts
- Linear network with wire roles (also: role, scratch wires, gate)
- Scratch restoration schedule
- Three-element subset intersection gadget (also: gather, scatter, side injection, Frankl–Wilson construction)
- Three-stage bank exchange
- Frames and the common-frame identity (also: frame, endpoint operator)
- Subspace labels and orthogonal residuals (also: labels, orthogonal residual)
- Rank saving s < Wm (also: rank deficit)
  - $s$ (number of smaller calls): The number of smaller recursive calls one network invocation makes, equal to the summed ranks or residual dimensions over all edges.
  - $W$ (number of wires): The number of wires (roles) in the fixed linear network, which is also the number of streams the rows are split into.
  - $m$ (label dimension): The dimension of the fixed label space, which is the factor by which each recursive call shrinks its parameter.
- Row splitting among wire roles
- Fixed-tape depth-first recursion schedule
- Address shear (also: rational matrix interface)
- Lower-triangular Bruhat factorization
- Matrix shear by interchanges
- Recursive power-width interchange
- Fast address-chunk interchange (also: chunk swap, address interchange)
- Phase kernel C
  - $C$ (phase kernel): The two-point matrix aI + bX with a = (1+i)/2 and b = (1−i)/2, where X swaps the two coordinates.
- Binary phase frames (also: complex phase network, complex motif interface)
- Packed selected-bit addition (also: binary change of basis, deterministic repair)
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Synthetic transform tape layout
- Convolution over the polynomial ring
- Coefficient phase twist
- Gaussian resampling
- Retained source and target permutations
- Bluestein chirp identity
- Binary representation of integers (also: base-2 representation, binary numeral, most significant bit, least significant bit, leading zeroes, bit string)
- Logarithms (also: log base 2, log_2, lg, logarithm laws)
- Floor and ceiling functions (also: floor, ceiling, rounding down, rounding up, nearest integer, integer part)
- Two's complement (also: signed binary integers, two's-complement word, sign bit)
- Fixed-point binary numbers (also: fixed-point arithmetic, dyadic fraction, fractional bits, guard bits, binary point)
- Schoolbook binary arithmetic and carry propagation (also: carry, carry propagation, ripple-carry addition, long multiplication, schoolbook multiplication, grade-school multiplication)
- Integer division with remainder (also: quotient and remainder, Euclidean division, integer square root, floor of a/b)
- Modular arithmetic (also: congruence, residues, mod, integers modulo Q, Z/QZ, residue counter, modular inverse)
- Greatest common divisor and the extended Euclidean algorithm (also: gcd, coprime, relatively prime, pairwise coprime, Euclid's algorithm, extended Euclidean algorithm, Bezout coefficients)
- Prime numbers (also: primes, odd prime, trial division)
- Chinese remainder theorem (also: CRT, Chinese remaindering)
- Sets, Cartesian products and indicator vectors (also: subset, intersection, cardinality, Cartesian product, characteristic vector, indicator vector, support)
- Binomial coefficients (also: n choose k, combinations, three-element subsets, counting subsets)
- Permutations and bijections (also: permutation, bijection, inverse permutation, composition of permutations, isomorphism, one-to-one correspondence)
- Mathematical induction (also: proof by induction, inductive argument)
- Directed graphs (also: vertices, edges, nodes, path, head and tail of an edge)
- Worst-case running time (also: time complexity, worst-case cost, deterministic algorithm, bit complexity)
- RAM model of computation (also: random-access machine, unit-cost RAM, word RAM, random access)
- Recurrence relations and divide and conquer (also: recurrence, divide-and-conquer, recursive algorithm, master theorem, solving recurrences)
- Geometric series (also: geometric sum, geometrically increasing)
- Karatsuba multiplication (also: Karatsuba's algorithm, Karatsuba–Ofman, O(n^{log₂3}) multiplication)
- Polynomial evaluation and interpolation (also: evaluation and interpolation, Lagrange interpolation, Toom-Cook idea, coefficient representation)
- Sorting (also: sort, merge sort, radix sort, O(n log n) sorting, label-and-sort)
- Stacks (also: stack, push and pop, LIFO, stack tape)
- Binary counters (also: binary counter, counter increment, amortized increment cost, ripple counting)
- Matrix transposition and row-major order (also: transpose, row-major, matrix transpose)
- Vector spaces, subspaces and dimension (also: linear subspace, span, basis, linear independence, dimension, linear combination, Q^h, ground field)
- Matrices and linear maps (also: matrix multiplication, identity matrix, invertible matrix, inverse, diagonal matrix, linear operator, all-ones matrix, change of basis, transpose of a matrix)
- Gaussian elimination and triangular matrices (also: row reduction, elementary matrices, pivot, lower triangular matrix, LU decomposition, elimination)
- Eigenvalues (also: eigenvalue, eigenvector, diagonalization)
- Dot product and orthonormal bases (also: inner product, dot product, orthogonal vectors, orthonormal basis, unit vector, norm one)
- Projections onto subspaces (also: projection matrix, orthogonal projection, projection along a complement, idempotent matrix)
- Direct sums (also: direct sum, ⊕, block-diagonal operator, complementary subspaces)
- Hamming weight (also: weight, wt(x), number of ones, population count, parity)
- Euler's formula and the complex exponential (also: e^{iθ}, Euler's formula, complex exponential, phase, e^{2πi jk/q})
- Exponential function and Gaussian function (also: exponential, e^x, Gaussian, e^{-x^2}, bell curve)
- Limits and convergent series (also: limit, limit of a sequence, infinite series, absolute convergence, convergence)
- Triangle inequality (also: |a + b| ≤ |a| + |b|, absolute value bound)
- Newton's method (also: Newton iteration, Newton–Raphson, quadratic convergence, Newton reductions)

## This page

Concept: Exact coefficient recovery
Gloss: Undoing the known scalings, showing the computed convolution coefficients are within 1/2 of the true integers, rounding them, and propagating carries to obtain the exact binary product.

## This page in the argument

The step: The composed procedure (CRT map, two source transforms, pointwise product, opposite transform, rescaling) returns every product coefficient within less than $1/2$, so rounding and carry propagation give exactly $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$.
How: identify the exact counterpart of the computed pipeline as the integer convolution, add the contraction errors of all stages, bound the final error below $1/2$, round, and propagate carries
Why: The true coefficients are integers, so any approximation with error below $1/2$ determines them by rounding, and carries then give the binary product; since every stage is a contraction, the errors can simply be summed. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- By the permutation cancellation, the exact counterpart after the three transforms is $(u*v)/S^2$, and the two scalings by $S$ and $2^{2b+4}$ recover the integer coefficient convolution.
- For contractions errors propagate without growth, and for bilinear contractions on disk operands the two input errors add.
- The final absolute error is below $448b\,2^{-3b/4}<1/2$, so rounding gives the unique correct integer coefficient.
- Propagating radix-$2^b$ carries in increasing coefficient order yields the exact binary product.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet multitape Turing machine computes $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$ for all $n$-bit inputs in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in that model.; how: build two sub-logarithmic tape procedures (address-chunk interchange and simultaneous butterfly layers) from finite linear networks with a rank saving, insert them into the Harvey--van der Hoeven reduction of multiplication to convolution over $\mathbb C[y]/(y^r+1)$ via a Chinese-remainder map, Gaussian resampling, chirps and a phase twist, recover the integer coefficients exactly, and sum the normalized cost table (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S9.1, S9.2, S9.3, S9.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S9.1**: By the permutation cancellation, the exact counterpart after the three transforms is $(u*v)/S^2$, and the two scalings by $S$ and $2^{2b+4}$ recover the integer coefficient convolution.
Source: "By \eqref{eq:source-permutation-cancel}, the exact
counterpart after the three transforms is $(u*v)/S^2$, so after the
first scale it is $w=(u*v)/S$." (paper)
> The two occurrences of $S$ in this algorithm undo different normalizations. By \eqref{eq:source-permutation-cancel}, the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$. The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution. The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$; it also justifies the rounding, carries, and output length.

**S9.2**: For contractions errors propagate without growth, and for bilinear contractions on disk operands the two input errors add.
Source: "When all four operands are in the disk, their two errors therefore add." (paper)
> Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this subsection. An error of $a$ will mean absolute error less than $ah_p$. A linear contraction propagates an input error without increasing it. For a bilinear contraction $\mathcal M$, replacing its operands gives \[ \|\mathcal M(f',g')-\mathcal M(f,g)\| \le \|f'-f\|\,\|g'\|+\|f\|\,\|g'-g\|. \] When all four operands are in the disk, their two errors therefore add.

**S9.3**: The final absolute error is below $448b\,2^{-3b/4}<1/2$, so rounding gives the unique correct integer coefficient.
Source: "The strict error below $1/2$ makes the nearest integer to
that value the unique correct coefficient." (paper)
> In tensor order, the unscaled integer coefficient array is $2^{2b+4}S w$. This second occurrence of $S$ reverses the normalization still present in $w$, and $2^{2b+4}$ reverses the two input scales. Both multiplications act exactly on grid numerators. Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than \begin{equation}\label{eq:final-error} 2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b} <448b\,2^{-b+\gamma} \le448b\,2^{-3b/4}<\frac12. \end{equation} The true coefficients are real integers. If $H_j$ is the real numerator after the second scaling, its represented value is $H_j/2^p$. The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.

**S9.4**: Propagating radix-$2^b$ carries in increasing coefficient order yields the exact binary product.
Source: "The unprocessed terms are multiples of $Q_0^j$, so the identity fixes
the first $j$ radix digits of the full product." (paper)
> To propagate carries, let $Q_0=2^b$. The recovered ordinary coefficients are the $c_j$ in \eqref{eq:capacity}; they are zero for $2q-2<j<S$. With $q=\lceil n/b\rceil$ as above, use the recurrence for $0\le j<S$: \[ k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad k_{j+1}=\left\lfloor\frac{c_j+k_j}{Q_0}\right\rfloor. \] The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$. If this holds at $j$, then \[ c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1), \] which proves the next carry bound. The defining relation $c_j+k_j=d_j+Q_0k_{j+1}$ also gives the exact invariant \[ \sum_{h<j}c_hQ_0^h =\sum_{h<j}d_hQ_0^h+k_jQ_0^j. \] It holds for $j=0$, and the defining relation proves its next instance. The unprocessed terms are multiples of $Q_0^j$, so the identity fixes the first $j$ radix digits of the full product. The value $k_j$ is the carry from the processed coefficients into the remaining positions.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Retained source and target permutations](retained-permutations.md)
- [Disk grid and truncation](disk-grid-truncation.md)
- [Convolution over the polynomial ring](synthetic-convolution.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Coefficient phase twist](phase-twist.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Contractions and error accounting](contraction-error.md): Bookkeeping in which every exact step is a norm-nonincreasing linear (or bilinear) map, so computed approximations compose by simply adding their errors.
  Shown as: Exact coefficient recovery *<predicate>* Contractions and error accounting
- [Radix-digit reduction to convolution](radix-digit-convolution.md): Splitting each input into radix-2^b digits turns the integer product into a convolution of short nonnegative coefficients, from which the binary product is recovered by carry propagation.
  Shown as: Exact coefficient recovery *<predicate>* Radix-digit reduction to convolution

## Pages that build on this one

- Integer multiplication in O(n (lg n)^(1−κ)) time: The main theorem: one deterministic fixed-alphabet multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in that model.

## Other pages you may link to

- [Exact binary multiplication problem](exact-multiplication-problem.md)
- [Schönhage–Strassen optimality conjecture](optimality-conjecture.md)
- [Polynomial ring modulo yʳ + 1](poly-ring.md)
- [Synthetic roots of unity](synthetic-roots.md)
- [Normalized butterfly H₀](fft-butterfly.md)
- [The binary field F₂ and XOR](binary-field.md)
- [Gaussian dyadic numbers](gaussian-dyadics.md)
- [Linear network with wire roles](linear-network.md)
- [Three-element subset intersection gadget](subset-intersection-gadget.md)
- [Harvey–van der Hoeven multiplier](hvdh-multiplier.md)
- [Signed Kronecker substitution](kronecker-packing.md)
- [Scratch restoration schedule](scratch-restoration.md)
- [Three-stage bank exchange](bank-exchange.md)
- [Lexicographic array layout and logical volume](lexicographic-array-layout.md)
- [Frames and the common-frame identity](frames.md)
- [Elementary stream operations](elementary-streams.md)
- [Row splitting among wire roles](row-splitting.md)
- [Controlled cyclic shifts](controlled-shifts.md)
- [Matrix rank](matrix-rank.md)
- [Lower-triangular Bruhat factorization](bruhat-factorization.md)
- [Nondegenerate bilinear spaces and orthogonal complements](bilinear-forms.md)
- [Tensor product of linear maps](tensor-product.md)
- [Subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank saving s < Wm](rank-saving.md)
- [Address shear](address-shear.md)
- [Matrix shear by interchanges](matrix-shear-cost.md)
- [Fixed-tape depth-first recursion schedule](depth-first-schedule.md)
- [Recursive power-width interchange](power-width-interchange.md)
- [Fast address-chunk interchange](chunk-swap.md)
- [Phase kernel C](phase-kernel.md)
- [Binary phase frames](phase-frames.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Disk grid and truncation](disk-grid-truncation.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Coefficient phase twist](phase-twist.md)
- [Normalized discrete Fourier transform](dft.md)
- [Decimation-in-frequency FFT and bit-reversed order](decimation-in-frequency.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Synthetic transform tape layout](transform-layout.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Convolution over the polynomial ring](synthetic-convolution.md)
- [Retained source and target permutations](retained-permutations.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Distinct prime axis lengths](prime-axis-lengths.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Parameter choice and cost table](parameter-cost-table.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "proves that the recovered coefficient error is strictly below $1/2$" (paper)

  > Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform. Section~\ref{sec:assembly} removes the known normalizations and digit scales, proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product. A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}. Figure~\ref{fig:multiplication-flow} summarizes these reductions.

- "The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient." (paper)

  > In tensor order, the unscaled integer coefficient array is $2^{2b+4}S w$. This second occurrence of $S$ reverses the normalization still present in $w$, and $2^{2b+4}$ reverses the two input scales. Both multiplications act exactly on grid numerators. Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than \begin{equation}\label{eq:final-error} 2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b} <448b\,2^{-b+\gamma} \le448b\,2^{-3b/4}<\frac12. \end{equation} The true coefficients are real integers. If $H_j$ is the real numerator after the second scaling, its represented value is $H_j/2^p$. The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.


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

Write the body to `exegenius/tasks/0050-write-exact-recovery.answer.md` and the JSON to `exegenius/tasks/0050-write-exact-recovery.answer.json`, then run `exegenius submit 0050-write-exact-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0050-write-exact-recovery`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
