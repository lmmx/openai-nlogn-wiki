# exegenius task 0029-write-precision-recovery

Project directory: `/home/user/openai-nlogn-wiki/runs/C3` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science degree: algorithm analysis with big-O and recurrences, discrete mathematics (sets, modular arithmetic, primes, induction, permutations), and the linear algebra and complex numbers of the first years (matrices, rank, invertibility, subspaces, norms). They know basic Turing machines with tapes and binary and two's-complement number representation. They have not studied Fourier transforms over rings, FFT-based multiplication, algebraic complexity, or the history of fast multiplication, and have not seen finite-field linear algebra beyond XOR as a bitwise operation.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape machine model and tape streams
- The n log n conjecture and history of multiplication
- Convolution
- Discrete Fourier transform
- Reduction of integer multiplication to digit convolution
- Fixed-point complex values and Gaussian dyadics
- Harvey–van der Hoeven O(n log n) multiplier as subroutine
- Polynomial ring modulo y^r + 1 (also: synthetic roots of unity)
  - $y$ (ring variable): The indeterminate of the polynomial ring, with y^r equal to -1.
  - $r$ (record length): The number of complex coefficients in a record, a power of two.
- Synthetic polynomial transform (also: polynomial transform)
- Two-point butterfly H₀
- Array addresses, fields and chunks
- Linear exchange network with roles and frames
- Three-element-subset network with rank saving
- Recursive power saving from s < Wm
- Lower triangular factorization of address shears
- Fast interchange of address chunks
- Fast simultaneous butterfly layers
- Synthetic transform on a retained-order layout
- Signed packing (Kronecker substitution)
- Normalized convolution over the polynomial ring
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein's chirp identity
- Resampling with permutations left in the transform
- Phase twist to the negacyclic last coordinate
- Linear algebra over the reals and complex numbers (also: matrices, matrix product, invertible matrix, linear map, vector space, subspace, rank, linear combination, basis, dimension)
- Linear algebra over GF(2) (also: F_2 vectors, XOR, bitwise exclusive or, binary vector space, mod 2 arithmetic)
- Triangular matrices and Gaussian elimination (also: lower triangular matrix, upper triangular matrix, row reduction, elementary matrices, unit diagonal)
- Modular arithmetic and prime numbers (also: congruence, residues mod m, coprime, gcd, distinct primes, cyclic group Z/m, divisibility)
- Binary and two's-complement representation (also: bit string, binary expansion, two's complement, signed integers, most significant bit, radix-b digits, padding)
- Floor, ceiling, rounding and logarithms (also: lg n, log base 2, floor, ceiling, nearest integer rounding, truncation toward zero)
- Permutations and sorting (also: bijection, reordering, transposition of data, permutation of indices)
- Cartesian products and mixed-radix indexing (also: multi-index, lexicographic order, multidimensional array, row-major order, tuples of indices)
- Vector norms and inequalities (also: sup norm, maximum norm, triangle inequality, modulus bound, contraction)
- Geometric series and recurrences (also: recurrence relation, summing a series, induction, master theorem, telescoping)
- Schoolbook multiplication and carries (also: long multiplication, carry propagation, grade-school multiplication)
- Roots of unity and Euler's formula (also: e^{2 pi i/k}, primitive root of unity, unit circle, cyclic sums of roots of unity)
- Asymptotic conventions (also: Theta, Omega, little-o, for sufficiently large n, fixed constant)
- Finite-state and constant-size alphabets (also: fixed finite alphabet, finite control, encoding symbols as bit blocks)

## This page

Concept: Precision and exact recovery
Gloss: Parameters are chosen so accumulated error in the recovered coefficients is below 1/2, so rounding returns the exact integer convolution, and carries yield the product.

## This page in the argument

The step: With the chosen parameters the accumulated error in the recovered coefficients is below $1/2$, so rounding gives the exact integer convolution and carries give the product.

It serves these steps, from the main result down:

- A deterministic fixed-tape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce multiplication to digit convolution computed by Fourier transforms, and speed up the two bottlenecks, address rearrangement and butterfly layers, by a recursion with a strict rank saving (on [Integer multiplication below n log n](main-theorem.md))
- The exact product of two $n$-bit integers is obtained by CRT address map, two source transforms, pointwise product, inverse transform, scaling, rounding and carries, in total cost $O(n(\lg n)^{1-\kappa})$.; how: Compose the preceding procedures into one pipeline, prove exact recovery by an error bound below $1/2$, and total the cost table for a fixed rational parameter choice (on [The multiplication algorithm and its cost](multiplication-algorithm.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Reduction of integer multiplication to digit convolution](radix-digit-reduction.md): Split each operand into radix-2^b digits, take the convolution of the digit lists with scaled fixed-point values, round the coefficients and propagate carries.
  Shown as: Precision and exact recovery *<predicate>* Reduction of integer multiplication to digit convolution
- [Fixed-point complex values and Gaussian dyadics](fixed-point-dyadics.md): Complex numbers stored as pairs of two's-complement integers over a power-of-two denominator 2^p, truncated toward zero, with contractive (norm ≤ 1) linear maps and error accumulation.
  Shown as: Precision and exact recovery *<predicate>* Fixed-point complex values and Gaussian dyadics
- [Resampling with permutations left in the transform](retained-permutations.md): The source and target coordinate permutations of resampling are kept inside the transform identity and cancel across the two forward transforms, product and inverse, so no separate sorts are run.
  Shown as: Precision and exact recovery *<predicate>* Resampling with permutations left in the transform

## Pages that build on this one

- The multiplication algorithm and its cost: Digits are mapped by the CRT address map, transformed by two source transforms, multiplied pointwise, inverse transformed, scaled, rounded and carried; the cost table totals O(n(lg n)^{1-κ}) for a fixed rational parameter choice.

## Other pages you may link to

- [Convolution](convolution.md)
- [Fixed-tape machine model and tape streams](tape-streams.md)
- [The n log n conjecture and history of multiplication](nlogn-conjecture.md)
- [Array addresses, fields and chunks](address-fields.md)
- [Linear exchange network with roles and frames](linear-network.md)
- [Three-element-subset network with rank saving](subset-network.md)
- [Recursive power saving from s < Wm](recursive-power-saving.md)
- [Harvey–van der Hoeven O(n log n) multiplier as subroutine](hvdh-multiplier.md)
- [Lower triangular factorization of address shears](shear-factorization.md)
- [Fast interchange of address chunks](fast-interchange.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Discrete Fourier transform](dft.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein.md)
- [Phase twist to the negacyclic last coordinate](phase-twist.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Two-point butterfly H₀](butterfly.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Synthetic transform on a retained-order layout](transform-layout.md)
- [Normalized convolution over the polynomial ring](ring-convolution.md)
- [The multiplication algorithm and its cost](multiplication-algorithm.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "proves that the recovered
coefficient error is strictly below $1/2$" (paper)

  > Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform. Section~\ref{sec:assembly} removes the known normalizations and digit scales, proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product. A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}. Figure~\ref{fig:multiplication-flow} summarizes these reductions.


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

Write the body to `exegenius/tasks/0029-write-precision-recovery.answer.md` and the JSON to `exegenius/tasks/0029-write-precision-recovery.answer.json`, then run `exegenius submit 0029-write-precision-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0029-write-precision-recovery`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
