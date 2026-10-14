# exegenius task 0019-write-scratch-restoration

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
- The n log n conjecture (also: Schönhage–Strassen conjecture, n log n optimality conjecture)
- Harvey–van der Hoeven O(n log n) multiplier (also: established multiplier)
- Lexicographic array layout and logical volume (also: address field, logical volume, row)
- Elementary stream operations
- Controlled shifts and rational scalings (also: prefix-controlled cyclic shift, triangular update)
- Gaussian dyadic fixed-point arithmetic (also: disk grid, Q_p truncation, Gaussian dyadics)
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring, R_r)
  - $y$ (polynomial variable): The indeterminate of the ring, whose powers act as roots of unity of order 2r.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Normalized butterfly H₀ (also: butterfly, Hadamard butterfly)
  - $H_0$ (normalized butterfly): The 2×2 matrix ½[[1, 1], [1, −1]] sending a pair (u, v) to ((u + v)/2, (u − v)/2).
- Linear network with wire roles (also: role, wire, gate, scalar network)
- Frames and the common-frame identity (also: frame, endpoint operator)
- Address shear
- Row splitting among wire roles
- Signed Kronecker packing (also: Kronecker substitution)
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

Concept: Restoring scratch values
Gloss: A gate schedule that first subtracts the effect of the arbitrary initial scratch values, then injects the data, then undoes its own auxiliary updates, so every scratch wire ends with its arbitrary initial value.
Also called: transparent computation, scratch wires

## Where the argument relies on this page

- A scalar linear network of $W$ wires, built from three stages of copy, gather, scatter and side-injection gates on triples, sends the two banks $(X_a,Y_a)$ to $(-Y_a,X_a)$ (a plain swap over $\mathbb F_2$) and returns every scratch wire to its arbitrary initial value. (on [Three-stage bank exchange](bank-exchange.md))
- For arbitrary initial scratch values a forward invocation adds $x_S$ to $y_S$ and changes nothing else, because the central coefficient ($|S\cap T|\bmod 2$, or $(|S\cap T|-1)/2$) and the side coefficient cancel for all neighbouring distinct triples.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear network with wire roles](linear-network.md): A fixed finite circuit of wires each carrying one scalar, with gates that apply fixed linear maps to the wires they touch; a wire's fixed place in the network is its role.
  Shown as: Restoring scratch values *<predicate>* Linear network with wire roles

## Pages that build on this one

- Three-stage bank exchange: The scalar network that, using copy, gather, scatter and side-injection gates per coordinate stage, maps two banks (X, Y) to (−Y, X) (a pure swap over 𝔽₂) while restoring all scratch wires.

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
- [Row splitting among wire roles](row-splitting.md)
- [Frames and the common-frame identity](frames.md)
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
- [Radix-digit reduction](radix-reduction.md)
- [Chinese-remainder convolution map](crt-map.md)
- [Normalized discrete Fourier transform](dft.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein's chirp identity](bluestein.md)
- [Contractions and error accounting](contraction-errors.md)
- [Resampling with retained permutations](resampling-retained.md)
- [Source permutation cancellation](source-perm-cancel.md)
- [Transform layout and cost](transform-layout.md)
- [Ring convolution from the retained layout](synthetic-convolution.md)
- [Coefficient twist](coefficient-twist.md)
- [Tensor resampling interface](tensor-resampling.md)
- [Size parameters and prime source lengths](parameters.md)
- [Computed source transform](source-transform.md)
- [Precision analysis and exact recovery](precision-recovery.md)
- [Cost table and the exponent κ](cost-accounting.md)
- [Integer multiplication in O(n (lg n)^{1−κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "This cancellation of arbitrary initial scratch values is a linear instance of the restoration construction for transparent computation" (paper)

  > scatter adds $\sum_{i\in S}C_i$ to $y_S$. \item In the complex construction, scalars lie in $\mathbb Z[i,1/2]$, and neighbors are distinct triples with even intersection. Copy is unchanged. Side injection adds \[ -\sum_{T\text{ neighboring }S}\frac{|S\cap T|-1}{2}A_{ST} \] to $y_S$. Gather adds $\sum_{T\ni i}x_T$ to $C_i$ and $\sum_Tx_T$ to $C_\ast$. Scatter adds $(\sum_{i\in S}C_i-C_\ast)/2$ to $y_S$. \end{itemize} Each update leaves its control wires unchanged. The first two rows of the following schedule remove the effect of the old scratch values; the next four introduce the source values and add their effect to the target; the last two restore the scratch values. This cancellation of arbitrary initial scratch values is a linear instance of the restoration construction for transparent computation in Buhrman, Cleve, Kouck\'y, Loff and Speelman~\cite[Section~3]{BuhrmanCleveKouckyLoffSpeelman2014}. The forward schedule is \begin{equation} \begin{array}{c|l|l} \text{row}&\text{operation}&\text{gate grouping}\\ \hline 0&\text{subtract side injection}&\text{one gate per target}\\ 1&\text{subtract scatter}&\text{one gate on targets and center}\\ 2&\text{copy}&\text{one gate per source}\\ 3&\text{gather}&\text{one gate on sources and center}\\ 4&\text{scatter}&\text{one gate on targets and center}\\ 5&\text{side injection}&\text{one gate per target}\\ 6&\text{undo gather}&\text{one gate on sources and center}\\ 7&\text{undo copy}&\text{one gate per source}. \end{array} \lab

- "Our scratch schedule is the linear-readout version of that construction." (paper)

  > Restoring scratch registers with arbitrary initial contents also has a precise precedent. The transparent-computation construction of Buhrman, Cleve, Kouck\'y, Loff and Speelman subtracts an initial register value, performs a computation, adds the resulting value, and reverses the computation~\cite[Section~3]{BuhrmanCleveKouckyLoffSpeelman2014}. Our scratch schedule is the linear-readout version of that construction. The rank reduction used for address shears is a singular-matrix Bruhat factorization: after reversing the coordinate order, Grigor'ev's upper-triangular factors become the two lower-triangular factors needed here~\cite[Appendix~A.2, Proposition~14(c)]{Grigoriev1982}.


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

Write the body to `exegenius/tasks/0019-write-scratch-restoration.answer.md` and the JSON to `exegenius/tasks/0019-write-scratch-restoration.answer.json`, then run `exegenius submit 0019-write-scratch-restoration` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0019-write-scratch-restoration`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
