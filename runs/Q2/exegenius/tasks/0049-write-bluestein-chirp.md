# exegenius task 0049-write-bluestein-chirp

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

Concept: Bluestein chirp identity
Gloss: The identity writing a Fourier transform (here including its frequency permutation) as pointwise multiplication by a chirp, a cyclic convolution with the chirp, and another chirp multiplication.

## This page in the argument

The step: With the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$, $QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$, so the target permutation is absorbed by the chirp.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet multitape Turing machine computes $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$ for all $n$-bit inputs in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in that model.; how: build two sub-logarithmic tape procedures (address-chunk interchange and simultaneous butterfly layers) from finite linear networks with a rank saving, insert them into the Harvey--van der Hoeven reduction of multiplication to convolution over $\mathbb C[y]/(y^r+1)$ via a Chinese-remainder map, Gaussian resampling, chirps and a phase twist, recover the integer coefficients exactly, and sum the normalized cost table (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- The permuted multidimensional source transform $RF_{\boldsymbol s}$ on distinct prime axes equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with power-of-two axes, its middle factor $QF_{\boldsymbol t}$ is a chirp-wrapped cyclic convolution, and the retained permutation $R$ cancels in a convolution.; how: apply Gaussian resampling linewise while keeping the source and target permutations inside the identity, evaluate the middle factor by Bluestein's chirp identity, and show the source permutation cancels

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Normalized discrete Fourier transform](dft.md): The maps (F_q u)_k = (1/q) Σ_j u_j e^{∓2πijk/q} and their tensor products over several axes, which are contractions and turn cyclic convolution into pointwise multiplication.
  Shown as: Bluestein chirp identity *<predicate>* Normalized discrete Fourier transform
- [Cyclic convolution](cyclic-convolution.md): The product of two arrays indexed modulo their lengths, (u∗v)_k = Σ_j u_j v_{k−j}, equivalently multiplication of polynomials modulo x^S − 1 (or modulo xᵢ^{sᵢ} − 1 on several axes).
  Shown as: Bluestein chirp identity *<predicate>* Cyclic convolution
- [Retained source and target permutations](retained-permutations.md): Keeping the coordinate permutations of Gaussian resampling inside the transform identity instead of sorting, since the target permutation is absorbed by the chirp step and the source permutation cancels in the convolution.
  Shown as: Bluestein chirp identity *<predicate>* Retained source and target permutations

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
- [Radix-digit reduction to convolution](radix-digit-convolution.md)
- [Coefficient phase twist](phase-twist.md)
- [Decimation-in-frequency FFT and bit-reversed order](decimation-in-frequency.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Synthetic transform tape layout](transform-layout.md)
- [Contractions and error accounting](contraction-error.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Convolution over the polynomial ring](synthetic-convolution.md)
- [Exact coefficient recovery](exact-recovery.md)
- [Distinct prime axis lengths](prime-axis-lengths.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Parameter choice and cost table](parameter-cost-table.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution." (paper)

  > Next, Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections~\ref{sec:synthetic-layouts} and~\ref{sec:exact-ring-products} compute convolution on the remaining axes over this polynomial ring. The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order. Their polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.

- "The chirp identity below performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array." (paper)

  > The factor $QF_{\boldsymbol t}$ in \eqref{eq:no-sort-tensor} can be computed from a cyclic convolution and two pointwise phase multiplications. The chirp identity below performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array. The second identity shows how the retained source permutation $R$ cancels when computing a convolution. Here $*$ denotes cyclic convolution on the product of the coordinate groups and a dot denotes coordinatewise multiplication.


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

Write the body to `exegenius/tasks/0049-write-bluestein-chirp.answer.md` and the JSON to `exegenius/tasks/0049-write-bluestein-chirp.answer.json`, then run `exegenius submit 0049-write-bluestein-chirp` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0049-write-bluestein-chirp`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
