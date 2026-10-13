# exegenius task 0027-write-parameter-choice

Project directory: `/home/user/openai-nlogn-wiki/runs/B4` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: asymptotic analysis, algorithms (including divide and conquer, sorting, and the basic idea of fast multiplication), basic Turing machines, and the supporting mathematics of linear algebra, discrete math, probability-free basics, and complex numbers. They have not studied the FFT in depth, algebraic complexity, polynomial rings modulo relations, number theory beyond modular arithmetic and CRT basics, or numerical error analysis, and they know nothing of the research literature on fast multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Schönhage–Strassen n log n conjecture and history
- Discrete Fourier transform and convolution
- Multiplication as convolution of radix digits
- Established O(n log n) multiplier (subroutine)
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Resampling with permutations left in the transform
- Bluestein's chirp identity
- Polynomial ring modulo y^r + 1
  - $r$ (ring size): A power of two giving the number of complex coefficients in a polynomial of the ring.
  - $y$ (ring variable): The indeterminate of the polynomials, satisfying y^r = -1.
- Coefficient twist from cyclic to negacyclic
- Synthetic polynomial transform
- Two-point butterfly H₀
- Signed packing (Kronecker substitution)
- Exact normalized convolution over the polynomial ring
- Tape streams, array order and elementary scans
- Linear network with roles and frames
- Subset-intersection subspace labels
- Recursive power saving from rank deficit
- Lower triangular (Bruhat-type) factorization and matrix shear
- Fast interchange of address chunks
  - $V$ (stored bit volume): The number of stored bits in the array.
  - $u$ (field width): The number of bits in each of the two address fields being interchanged.
  - $\tau$ (saving exponent): A fixed constant below 1 giving the power of u in the cost.
- Simultaneous butterfly layer
  - $V$ (stored bit volume): The number of stored bits in the numerical arrays.
  - $d$ (chunk count): The number of equal-width address chunks in which the same bit position is selected.
  - $\lambda'$ (layer exponent): A fixed constant below 1 giving the power of d in the cost.
- Fixed-point dyadic precision and exact recovery
- Linear algebra basics (also: vectors, matrices, linear maps, rank, invertible matrix, tensor-free linear algebra)
- Modular arithmetic (also: congruences, mod n, residues, remainder)
- Prime numbers and coprimality (also: primes, gcd, coprime, relatively prime, prime number theorem)
- Binary representation and radix expansion (also: base 2, bits, radix 2^b, binary digits, positional notation)
- Schoolbook multiplication and carries (also: long multiplication, quadratic multiplication, carry propagation, O(n^2) multiplication)
- Divide and conquer and recurrences (also: recurrence relations, master theorem, recursion, Karatsuba)
- Sorting and its cost (also: sort, permuting data, comparison sort, O(n log n) sorting)
- Logarithms and exponentials (also: lg, log base 2, log log, iterated logarithm)
- Cartesian product and mixed-radix indexing (also: multi-dimensional array, tensor index, row-major order, axes of an array)
- Cyclic groups and roots of unity (also: Z/mZ, cyclic group, additive group of integers mod m)
- Euclidean norm and unit disk (also: modulus, absolute value of complex number, unit disk, norm, triangle inequality)
- Fixed-point and rounding arithmetic (also: truncation, rounding error, floor and ceiling, dyadic rationals)
- Proof by induction and summation (also: geometric series, induction, telescoping sums)
- Subsets, indicator vectors and set intersection (also: characteristic vector, binomial coefficient, k-element subsets)
- Permutation matrices (also: permutations, partial permutation, bijection)
- Euler's formula and trigonometry (also: e^{i theta}, cos and sin, pi)
- Gaussian function (also: Gaussian, bell curve, e^{-x^2})
- Big-endian bit strings and Boolean operations (also: XOR, bitwise exclusive or, bit position)
- Rational numbers and field arithmetic (also: Q, rational field, fractions)

## This page

Concept: Fixed rational parameter choice
Gloss: The conservative constants (τ, λ, λ′, ε, δ, κ = 2^{-182}) chosen compatibly so all terms in the cost table fit the main bound.

## This page in the argument

The step: Rational parameters $\tau,\lambda,\lambda',\epsilon,\delta,\kappa=2^{-182}$ are chosen compatibly.

It serves these steps, from the main result down:

- There is a deterministic fixed multitape Turing machine multiplying $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: build two fast tape procedures, use them for synthetic and resampled transforms, and assemble the exact product through convolution (on [Multiplication in O(n (lg n)^{1-κ}) time](main-theorem.md))
- The full algorithm turns the integer product into digit convolution, runs the transforms, and recovers the exact product in $O(n(\lg n)^{1-\kappa})$ time.; how: digits, then CRT address map, transforms and pointwise product, then rescale, round and carry, with error and cost accounting (on [Complete multiplication algorithm and cost](multiplication-algorithm.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fast interchange of address chunks](fast-address-interchange.md): Interchanging two contiguous address fields of u bits in a Cartesian-product array, by XOR/shear combinations through the bit network, at cost O(V u^τ) for fixed τ < 1.
  Shown as: Fixed rational parameter choice *<predicate>* Fast interchange of address chunks
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): Applying H₀ at the same bit position of up to d address chunks at once on records of complex fixed-point polynomials, using the complex phase network, at cost O(V d^λ′).
  Shown as: Fixed rational parameter choice *<predicate>* Simultaneous butterfly layer
- [Resampling with permutations left in the transform](resampling-keep-permutations.md): Keeping the source and target coordinate permutations inside the transform identity so they cancel across the forward and inverse transforms instead of being executed as sorts.
  Shown as: Fixed rational parameter choice *<predicate>* Resampling with permutations left in the transform
- [Exact normalized convolution over the polynomial ring](ring-convolution.md): Convolution on the remaining axes via forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform consuming the same frequency order.
  Shown as: Fixed rational parameter choice *<predicate>* Exact normalized convolution over the polynomial ring
- [Fixed-point dyadic precision and exact recovery](fixed-point-precision.md): Coefficients stored as p-bit grid values on the unit disk, with truncation errors tracked through contractions so the final integer coefficient error is below 1/2.
  Shown as: Fixed rational parameter choice *<predicate>* Fixed-point dyadic precision and exact recovery

## Pages that build on this one

- Complete multiplication algorithm and cost: Digits → CRT address map → forward synthetic Gaussian-resampled transforms of both operands → pointwise product → inverse transform → rescale, round and carry to get the exact product.

## Other pages you may link to

- [Fixed multitape Turing machine model](multitape-model.md)
- [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md)
- [Discrete Fourier transform and convolution](dft-convolution.md)
- [Multiplication as convolution of radix digits](radix-digit-reduction.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring.md)
- [Two-point butterfly H₀](butterfly-h0.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Chinese-remainder map to prime cyclic axes](cyclic-crt.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein.md)
- [Coefficient twist from cyclic to negacyclic](coefficient-twist.md)
- [Established O(n log n) multiplier (subroutine)](hvdh-multiplier.md)
- [Tape streams, array order and elementary scans](stream-operations.md)
- [Linear network with roles and frames](linear-network-frames.md)
- [Subset-intersection subspace labels](subset-intersection-labels.md)
- [Recursive power saving from rank deficit](recursive-saving.md)
- [Lower triangular (Bruhat-type) factorization and matrix shear](lower-triangular-factorization.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Complete multiplication algorithm and cost](multiplication-algorithm.md)
- [Multiplication in O(n (lg n)^{1-κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "These constants are deliberately conservative; no optimization is claimed." (paper)

  > The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.


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

Write the body to `exegenius/tasks/0027-write-parameter-choice.answer.md` and the JSON to `exegenius/tasks/0027-write-parameter-choice.answer.json`, then run `exegenius submit 0027-write-parameter-choice` in the project directory. If submit rejects the answer, fix the answer and submit again.
