# exegenius task 0032-write-fixed-point-errors

Project directory: `/home/user/openai-nlogn-wiki/runs/B5` (paths below are relative to it)

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

For these sources: An undergraduate computer science reader who has studied algorithm analysis (big-O, recurrences, sorting, divide and conquer including Karatsuba-style multiplication), discrete mathematics (modular arithmetic, gcd and coprimality, the Chinese remainder theorem in its basic form, permutations, binary representation), and calculus and linear algebra through matrices, Gaussian elimination and basic vector spaces. They know complex numbers and polynomials, and have seen simple Turing machines with tapes. They have not met the fast Fourier transform in depth beyond its name, finite-field or group-theoretic structure beyond Z/n, Kronecker products, or any research-level multiplication algorithms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n conjecture and its history
  - $n$ (input length): The number of bits in each of the two integers being multiplied.
- Arrays on tape, address fields and volume
- Elementary stream operations
- Controlled shifts and rational scalings
- Rank, subspaces and orthogonal complements
- Cyclic convolution
- Discrete Fourier transform
- Two-point butterfly
- Integer product as digit convolution
- Bank-exchanging linear network with restored scratch
- Frames and the common-frame invariant
- Subspace labels from triple indicator vectors
- Rank deficit and the recursive power saving
  - $s$ (total smaller calls): The number of smaller recursive calls, equal to the sum of ranks of edge differences.
  - $W$ (wire count): The number of wires in the fixed network.
  - $m$ (label dimension): The number of coordinates of the fixed label space.
- Bit network and rational shear interface
- Phase frames and the kernel C=aI+bX
- Lower triangular factorization
- Cost of a rational matrix shear
- Power-width chunk interchange
- Fast interchange of address chunks
  - $V$ (bit volume): The number of stored data bits in the array.
  - $u$ (chunk width): The number of bits in each interchanged chunk.
  - $\tau$ (exponent): A fixed rational constant below 1, namely 1−2^{-50}.
- Packed selected-bit addition
- Polynomial ring modulo y^r+1
  - $y$ (indeterminate): The polynomial variable, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a record, a power of two.
- Synthetic polynomial transform
- Simultaneous butterfly layer
  - $V$ (bit volume): The number of stored data bits.
  - $d$ (axis count): The maximum number of axes whose chunks are transformed together.
  - $\lambda'$ (exponent): A fixed rational constant below 1.
- Transform layout and cost
- Signed packing for ring products
- Convolution from retained transform layout
- Chinese-remainder address map
- Coefficient phase twist
- Logarithms and exponentials (also: lg, log base 2, log n, exp, powers of two)
- Floor and ceiling (also: floor function, ceiling function, rounding to nearest integer)
- Modular arithmetic (also: congruence, Z/nZ, integers modulo q, residues, remainder)
- Greatest common divisor and coprimality (also: gcd, relatively prime, pairwise coprime, units modulo q)
- Prime numbers (also: primes, prime factorization, odd prime, distribution of primes)
- Chinese remainder theorem (also: CRT)
- Binary representation and bit operations (also: bits, XOR, exclusive or, two's complement, bitwise operations, carries)
- Positional radix representation (also: base b digits, digit expansion, radix)
- Permutations (also: bijections, partial permutation, permutation matrix, transposition)
- Matrices and matrix products (also: matrix multiplication, invertible matrix, identity matrix, triangular matrix, transpose, Gaussian elimination)
- Vector spaces and linear maps (also: linear independence, dimension, kernel, image, basis, dot product)
- Finite field F2 (also: GF(2), integers mod 2, binary field)
- Euler's formula and complex exponentials (also: e^{i theta}, roots of unity, modulus, unit circle, Euler identity)
- Geometric series (also: sum of powers, geometric sum, sum of roots of unity)
- Gaussian function (also: Gaussian, bell curve, exp(-x^2), Gaussian weights)
- Basic calculus and inequalities (also: Taylor series, triangle inequality, Cauchy-Schwarz, limits, bounds on error)
- Fixed-point and rounding arithmetic (also: approximation error, truncation, precision bits, numerical error)
- Cartesian product and tuples (also: product of index sets, multi-index, d-dimensional array, lexicographic order)
- Cyclic groups and direct products (also: Z/n, additive group, group isomorphism, cyclic shift)
- Sorting (also: merge sort, sorting by key, comparison sort, O(N log N) sorting)
- Divide and conquer recurrences (also: master theorem, recurrence relation, recursion tree, induction)
- Karatsuba and schoolbook multiplication (also: long multiplication, grade-school multiplication, O(n^2) multiplication, Karatsuba algorithm)
- Fast Fourier transform idea (also: FFT, Cooley-Tukey, fast polynomial multiplication, evaluation and interpolation)
- Sums and indexed notation (also: summation, product notation, indicator function, Kronecker delta, subsets and set notation)

## This page

Concept: Fixed-point error control
Gloss: Complex values on a grid of spacing 2^{-p} in the unit disk, linear contractions that do not enlarge error, truncation, and additive error bookkeeping.

## This page in the argument

The step: The error in the recovered coefficients is strictly below $1/2$ under additive error bookkeeping with contractions and truncation, so rounding gives the exact integer coefficients.

It serves these steps, from the main result down:

- Integer multiplication of $n$-bit integers takes $O(n(\lg n)^{1-\kappa})$ time on one deterministic fixed-tape machine, disproving the $n\log n$ conjecture.; how: build the fast tape primitives (address interchange and simultaneous butterfly layers), then the synthetic transform and convolution machinery, then the resampling reductions and the assembly with its cost table (on [Integer multiplication in O(n (lg n)^(1−κ))](main-theorem.md))
- The integer product is assembled from digit convolution, the CRT axis map, the chirp and resampled transforms, the coefficient twist, synthetic convolution and rounding.; how: chain the reductions in order, accounting for each change of representation and recovering exact coefficients from approximations

## Pages that build on this one

- Gaussian resampling: Gaussian-weighted contractions A and B0 that relate a Fourier transform of length s to one of length t slightly larger, with the two coordinate permutations kept inside the identity.
- Integer multiplication in O(n (lg n)^(1−κ)): A deterministic fixed-tape machine multiplies n-bit integers by digit convolution, CRT axes, resampling, chirps, twisting, synthetic convolution and rounding, disproving the n log n conjecture.

## Other pages you may link to

- [The n log n conjecture and its history](nlogn-conjecture.md)
- [Cyclic convolution](convolution.md)
- [Integer product as digit convolution](radix-digit-mult.md)
- [Arrays on tape, address fields and volume](array-layout.md)
- [Elementary stream operations](stream-ops.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Rank, subspaces and orthogonal complements](linear-algebra.md)
- [Bank-exchanging linear network with restored scratch](scalar-network.md)
- [Frames and the common-frame invariant](frames.md)
- [Subspace labels from triple indicator vectors](labels.md)
- [Rank deficit and the recursive power saving](rank-deficit.md)
- [Bit network and rational shear interface](bit-interface.md)
- [Lower triangular factorization](bruhat.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Power-width chunk interchange](power-interchange.md)
- [Fast interchange of address chunks](chunk-swap.md)
- [Packed selected-bit addition](packed-addition.md)
- [Polynomial ring modulo y^r+1](synthetic-ring.md)
- [Signed packing for ring products](signed-packing.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly](butterfly.md)
- [Phase frames and the kernel C=aI+bX](phase-interface.md)
- [Simultaneous butterfly layer](butterfly-layer.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Transform layout and cost](transform-layout.md)
- [Convolution from retained transform layout](synthetic-convolution.md)
- [Chinese-remainder address map](crt-map.md)
- [Coefficient phase twist](coefficient-twist.md)
- [Gaussian resampling](resampling.md)
- [Multidimensional resampling](tensor-resampling.md)
- [Bluestein chirp and permutation cancellation](chirp.md)
- [Parameter choices and cost table](parameters-cost.md)
- [Integer multiplication in O(n (lg n)^(1−κ))](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "\subsection{Precision and exact recovery}" (paper)

  > \subsection{Precision and exact recovery}


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

Write the body to `exegenius/tasks/0032-write-fixed-point-errors.answer.md` and the JSON to `exegenius/tasks/0032-write-fixed-point-errors.answer.json`, then run `exegenius submit 0032-write-fixed-point-errors` in the project directory. If submit rejects the answer, fix the answer and submit again.
