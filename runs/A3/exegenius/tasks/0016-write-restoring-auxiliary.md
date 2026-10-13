# exegenius task 0016-write-restoring-auxiliary

Project directory: `/home/user/openai-nlogn-wiki/runs/A3` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science background: asymptotic analysis, discrete mathematics (binary numbers, modular arithmetic, primes, XOR, subsets), introductory linear algebra (matrices, invertibility, vector subspaces, dimension), and basic complex numbers and polynomials. They know basic Turing machines with tapes, and have seen the standard FFT idea at most as an algorithm, not the Nussbaumer, Bluestein or Harvey-van der Hoeven machinery. They have not studied algebraic number theory, advanced algebra such as Bruhat factorization, or numerical error analysis in depth.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Schönhage–Strassen n log n conjecture and history
- Convolution and the discrete Fourier transform
- Multiplication as digit convolution
- Signed coefficient packing (Kronecker substitution)
- Established O(n log n) multiplier as subroutine
- Elementary stream operations on tapes
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The indeterminate of the polynomials, with y^r = -1.
  - $r$ (number of coefficients): The number of coefficients in a polynomial, a power of two.
- Synthetic polynomial transforms
- Bluestein chirp identity
- Last-coordinate phase twist
- Linear networks, roles and frames
- Fixed-point precision and exact recovery
- Binary representation of integers (also: bit strings, binary numerals, most significant bit, bits)
- Logarithms and ceiling/floor (also: lg, log base 2, ceiling, floor)
- Modular arithmetic (also: residues, congruence, integers mod m, Z/mZ)
- Prime numbers and coprimality (also: distinct primes, relatively prime, gcd)
- Bitwise XOR (also: exclusive or, xor, addition mod 2)
- Matrices and linear maps (also: linear transformations, matrix-vector product, invertible matrix, triangular matrix, lower-triangular)
- Vector subspaces and dimension (also: linear subspace, span, linear independence, basis)
- Cartesian product and index sets (also: product of sets, multidimensional array, tuple indices, coordinates)
- Permutations (also: bijection, rearrangement, reordering)
- Fixed-point and rounding (also: truncation, rounding to nearest integer, dyadic rationals, fixed-point numbers)
- Absolute value, modulus and sup norm (also: max norm, infinity norm, triangle inequality, magnitude of a complex number)
- Schoolbook multiplication and carries (also: long multiplication, carry propagation, radix-b digits)
- Divide and conquer recursion (also: recurrence relation, recursion, master theorem)
- Induction and proof by contradiction (also: mathematical induction, contradiction, inductive step)
- Linear-time scanning of tape data (also: sequential tape access, copying a tape, head movement)
- Euclidean division and floor division (also: quotient and remainder, division with remainder, mod operator)
- Geometric series and exponent rules (also: powers of two, exponentiation, summing a geometric sum)

## This page

Concept: Restoring auxiliary values
Gloss: Scratch registers with arbitrary initial contents are subtracted, used, re-added and the computation reversed so the final effect is exact for any initial auxiliary values.

## This page in the argument

The step: A fixed network of gates with scratch wires changes $y_S$ to $y_S+x_S$ for arbitrary initial auxiliary values, which are restored.

It serves these steps, from the main result down:

- A fixed deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: supply two faster tape procedures, then insert them into a chain of reductions from integer product to ring convolution (on [Integer multiplication below n log n](main-result.md))
- Two tape procedures, an address-field interchange and a simultaneous butterfly layer, run in $O(Vu^\tau)$ and $O(Vd^{\lambda'})$ time with exponents below 1.; how: build both from fixed linear networks with a rank saving, using elementary stream operations
- Recursing a fixed network with $s<Wm$ gives a cost per unit volume that is a power of the parameter below the first power.; how: build the finite network (restored scratch values, frames, three-element-subset labels), then solve the recursion it induces (on [Recursive power saving s < Wm](recursive-saving.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear networks, roles and frames](linear-networks-frames.md): A fixed linear network exchanging two banks of values with signs and restoring auxiliary values; roles are wire positions and invertible frames D_v change the stored representation so intermediate frames cancel and only an endpoint operator remains.
  Shown as: Restoring auxiliary values *<predicate>* Linear networks, roles and frames

## Pages that build on this one

- Fast interchange of address fields: Exchanging two disjoint contiguous u-bit address fields of an array with volume V in O(V u^τ) time for fixed τ<1, using XOR combinations of intermediate data though the final effect is an exact permutation.

## Other pages you may link to

- [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md)
- [Convolution and the discrete Fourier transform](convolution-dft.md)
- [Multiplication as digit convolution](radix-digit-reduction.md)
- [Polynomial ring modulo y^r + 1](poly-ring-mod-yr1.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Established O(n log n) multiplier as subroutine](hh-nlogn-multiplier.md)
- [Elementary stream operations on tapes](stream-operations.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Address shear and triangular factorization](address-shear.md)
- [Finite network from three-element subsets](subset-network-construction.md)
- [Recursive power saving s < Wm](recursive-saving.md)
- [Fast interchange of address fields](address-interchange.md)
- [Simultaneous butterfly layer H₀](butterfly-layer.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Exact normalized polynomial products](exact-ring-products.md)
- [Transform layout with retained frequency order and permutations](transform-layout.md)
- [Multiplication algorithm and its cost](main-algorithm.md)
- [Integer multiplication below n log n](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "The final permutation is
exact for arbitrary initial auxiliary values." (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.


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

Write the body to `exegenius/tasks/0016-write-restoring-auxiliary.answer.md` and the JSON to `exegenius/tasks/0016-write-restoring-auxiliary.answer.json`, then run `exegenius submit 0016-write-restoring-auxiliary` in the project directory. If submit rejects the answer, fix the answer and submit again.
