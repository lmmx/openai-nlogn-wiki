# exegenius task 0045-write-contraction-error

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
- Coefficient phase twist
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

Concept: Contractions and error accounting
Gloss: Bookkeeping in which every exact step is a norm-nonincreasing linear (or bilinear) map, so computed approximations compose by simply adding their errors.

## Where the argument relies on this page

- Normalized cyclic convolution of arrays of $\mathbb C[y]/(y^r+1)$ records on power-of-two axes of total size $T$ can be approximated within $\sqrt2\,M(3\ell+1)2^{-p}$ at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$. (on [Convolution over the polynomial ring](synthetic-convolution.md))
- Since all exact steps are contractions, the errors of the three transforms and the product add, and the final exact scaling by $M$ gives total error below $\sqrt2\,M(3\ell+1)2^{-p}$.
- For coprime $s<t$ with enough separation, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ for contractions $A,B_0$ built from Gaussian kernels, approximable with error below $p^2$ in $O(tp^{3/2+\delta}\alpha)$ time. (on [Gaussian resampling](gaussian-resampling.md))
- The composed procedure (CRT map, two source transforms, pointwise product, opposite transform, rescaling) returns every product coefficient within less than $1/2$, so rounding and carry propagation give exactly $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$. (on [Exact coefficient recovery](exact-recovery.md))
- For contractions errors propagate without growth, and for bilinear contractions on disk operands the two input errors add.
- The final absolute error is below $448b\,2^{-3b/4}<1/2$, so rounding gives the unique correct integer coefficient.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Disk grid and truncation](disk-grid-truncation.md): Fixed-point storage of complex values in the unit disk on the grid 2^{−p}ℤ[i], with Q_p truncating real and imaginary parts toward zero, an error below √2·2^{−p} that never increases the norm.
  Shown as: Contractions and error accounting *<predicate>* Disk grid and truncation

## Pages that build on this one

- Gaussian resampling: The Harvey–van der Hoeven identity expressing a Fourier transform of prime length s through one of power-of-two length t > s, sandwiched between contractions built from Gaussian kernels, with a scale factor 2^{2α²}.
- Convolution over the polynomial ring: Normalized cyclic convolution of arrays of ℂ[y]/(yʳ+1) records computed by two forward synthetic transforms kept in their stored order, packed pointwise polynomial products, and one opposite transform.
- Exact coefficient recovery: Undoing the known scalings, showing the computed convolution coefficients are within 1/2 of the true integers, rounding them, and propagating carries to obtain the exact binary product.

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
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit reduction to convolution](radix-digit-convolution.md)
- [Coefficient phase twist](phase-twist.md)
- [Normalized discrete Fourier transform](dft.md)
- [Decimation-in-frequency FFT and bit-reversed order](decimation-in-frequency.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Synthetic transform tape layout](transform-layout.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Convolution over the polynomial ring](synthetic-convolution.md)
- [Retained source and target permutations](retained-permutations.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Exact coefficient recovery](exact-recovery.md)
- [Distinct prime axis lengths](prime-axis-lengths.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Parameter choice and cost table](parameter-cost-table.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Composing such algorithms adds their errors" (paper)

  > 2+b^2\leq 2^{2p}\}. \] For storage between completed scalar routines, put $w_{\rm c}=p+2$. Represent $2^{-p}(a+ib)\in\mathbb D_p$ by a signed $w_{\rm c}$-bit two's-complement word for $a$, followed by one for $b$, with each word written most significant bit first. A coordinate list is the concatenation of these fixed-length records in its stated order. Since $|a|,|b|\leq2^p<2^{w_{\rm c}-1}$, this format includes both signs of every permitted numerator, including $-2^p$ and $2^p$. An approximation $\widetilde L:\mathbb D_p^a\to\mathbb D_p^b$ to a linear contraction $L:\mathbb C^a\to\mathbb C^b$ has error $E$ if $2^p\|\widetilde L u-Lu\|<E$ for every input in $\mathbb D_p^a$. The approximation itself need not be linear. Composing such algorithms adds their errors: at each step, insert the exact map at the computed input and use its contraction bound on the accumulated input error.

- "A linear contraction propagates an input error without increasing it." (paper)

  > Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this subsection. An error of $a$ will mean absolute error less than $ah_p$. A linear contraction propagates an input error without increasing it. For a bilinear contraction $\mathcal M$, replacing its operands gives \[ \|\mathcal M(f',g')-\mathcal M(f,g)\| \le \|f'-f\|\,\|g'\|+\|f\|\,\|g'-g\|. \] When all four operands are in the disk, their two errors therefore add.


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

Write the body to `exegenius/tasks/0045-write-contraction-error.answer.md` and the JSON to `exegenius/tasks/0045-write-contraction-error.answer.json`, then run `exegenius submit 0045-write-contraction-error` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0045-write-contraction-error`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
