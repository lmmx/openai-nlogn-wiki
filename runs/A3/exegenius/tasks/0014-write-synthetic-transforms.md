# exegenius task 0014-write-synthetic-transforms

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
- Bluestein chirp identity
- Last-coordinate phase twist
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

Concept: Synthetic polynomial transforms
Gloss: Fourier-type transforms over the polynomial ring where powers of y serve as roots of unity, built from address rearrangements, signed shifts and two-point butterflies (Nussbaumer).

## This page in the argument

The step: Synthetic Fourier transforms over the ring with powers of $y$ as roots of unity are contractions, and inverse each other up to scale.

It serves these steps, from the main result down:

- A fixed deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: supply two faster tape procedures, then insert them into a chain of reductions from integer product to ring convolution (on [Integer multiplication below n log n](main-result.md))
- Two $n$-bit integers are multiplied exactly by chaining digits, prime axes, resampling and chirps, a phase twist and ring convolution, then rescaling, rounding and carries.; how: build the ring-convolution engine, then the reductions onto it, then the layout and exact recovery, and total the costs (on [Multiplication algorithm and its cost](main-algorithm.md))
- Convolution over $\mathbb C[y]/(y^r+1)$ can be computed exactly enough in near-linear time.; how: transform, multiply pointwise, transform back, with the polynomial products done by packing (on [Exact normalized polynomial products](exact-ring-products.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Polynomial ring modulo y^r + 1](poly-ring-mod-yr1.md): Polynomials in y with complex coefficients reduced using y^r = −1; powers of y act as roots of unity and multiplying by one is a signed cyclic shift of the coefficient list.
  Shown as: Synthetic polynomial transforms *<predicate>* Polynomial ring modulo y^r + 1
- [Convolution and the discrete Fourier transform](convolution-dft.md): Convolution of coefficient lists is computed by transforming, multiplying pointwise, and transforming back using roots of unity.
  Shown as: Synthetic polynomial transforms *<predicate>* Convolution and the discrete Fourier transform
- [Elementary stream operations on tapes](stream-operations.md): Array order, scans, controlled shifts and rational scalings that a fixed-tape machine performs in linear time.
  Shown as: Synthetic polynomial transforms *<predicate>* Elementary stream operations on tapes

## Pages that build on this one

- Simultaneous butterfly layer H₀: Applying H_0(u,v)=((u+v)/2,(u−v)/2) coefficientwise on selected address bits of numerical arrays of complex fixed-point polynomial records, via the recursive network, in O(V d^λ') time.
- Exact normalized polynomial products: Convolution over the ring using the forward synthetic transforms, pointwise polynomial products via signed packing and the O(n log n) multiplier, and the opposite transform.

## Other pages you may link to

- [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md)
- [Multiplication as digit convolution](radix-digit-reduction.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Established O(n log n) multiplier as subroutine](hh-nlogn-multiplier.md)
- [Linear networks, roles and frames](linear-networks-frames.md)
- [Restoring auxiliary values](restoring-auxiliary.md)
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

- "These are the
synthetic polynomial transforms of Nussbaumer and Quandalle and
Nussbaumer" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.

- "the transform calculation consists of address
rearrangements, signed shifts, and two-point butterfly operations" (paper)

  > In this representation, the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations. Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$. We therefore need savings in both movement and arithmetic. Two tape procedures supply them; in both bounds, $V$ denotes the stored bit volume.


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

Write the body to `exegenius/tasks/0014-write-synthetic-transforms.answer.md` and the JSON to `exegenius/tasks/0014-write-synthetic-transforms.answer.json`, then run `exegenius submit 0014-write-synthetic-transforms` in the project directory. If submit rejects the answer, fix the answer and submit again.
