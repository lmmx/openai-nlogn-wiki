# exegenius task 0009-write-synthetic-transforms

Project directory: `/home/user/openai-nlogn-wiki/runs/A5` (paths below are relative to it)

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

For these sources: An undergraduate computer science reader who has studied algorithms and data structures (divide and conquer, recurrences, sorting, basic complexity), discrete mathematics (modular arithmetic, primes, binary representation, sets, permutations, induction), and linear algebra (vector spaces, subspaces, dimension, rank, invertible matrices, Gaussian elimination, triangular matrices) at an introductory level. They know the basics of Fourier analysis and probability/real analysis only as far as complex numbers and elementary calculus. They have not studied algebraic number theory, advanced finite-field theory, Lie groups or specialist FFT/multiplication literature.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Multiplication history and the n log n conjecture
- Convolution and multiplication
- Discrete Fourier transform
- FFT and two-point butterflies
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers act as roots of unity.
  - $r$ (ring size): The number of coefficients in a polynomial record, a power of two.
- Recurrences and divide and conquer (also: recursion, master theorem, recurrence relation)
- Modular arithmetic (also: congruences, mod n, remainders)
- Prime numbers and coprimality (also: distinct primes, relatively prime, gcd)
- Chinese remainder theorem (also: CRT)
- Binary representation and bit operations (also: bits, base-2 expansion, bit fields, XOR, exclusive or, carries)
- Radix (base) expansion (also: digits in base B, positional notation, splitting into digits)
- Permutations (also: bijections of a finite set, reordering, sorting network)
- Vector spaces, subspaces and dimension (also: linear subspace, span, basis, linear independence)
- Finite field F_2 (also: GF(2), binary field, integers mod 2)
- Matrices, rank and invertibility (also: linear maps, matrix product, invertible matrix, rank of a matrix, identity matrix)
- Gaussian elimination (also: row reduction, triangular matrix, lower-triangular, upper-triangular)
- Cartesian product of sets (also: product set, multi-index, tuples, multidimensional array)
- Cyclic groups and roots of unity (also: Z/nZ, cyclic shift, primitive root of unity, n-th roots of unity, Euler's formula)
- Real and complex analysis basics (also: absolute value, modulus, norm, triangle inequality, Gaussian function, exponential)
- Rounding, floor and ceiling (also: floor, ceiling, nearest integer, truncation)
- Logarithms and exponents (also: lg, log base 2, binary logarithm, iterated logarithm, powers of two)
- Schoolbook multiplication and Karatsuba (also: long multiplication, quadratic multiplication, Karatsuba algorithm)
- Sorting and merging (also: sort, merge sort, sorting on tapes)
- Pigeonhole principle and counting arguments (also: union bound, counting subsets, binomial coefficients, combinatorics)
- Lower and upper bound asymptotics (also: Theta notation, little-o, Omega notation, asymptotic)
- Constants and parameters in complexity bounds (also: fixed constant, polylogarithmic, sub-logarithmic factor)

## This page

Concept: Synthetic polynomial transforms
Gloss: Nussbaumer-style transforms over the polynomial ring where roots of unity are powers of y, so root multiplication is a signed shift.

## This page in the argument

The step: The convolution over $\mathbb C[y]/(y^r+1)$ on the remaining axes is computed by synthetic transforms and packed polynomial products.
How: transform over the ring where roots of unity are powers of $y$, multiply pointwise, and invert
Why: Powers of y act as roots of unity so root multiplications are signed shifts, and the ring products reduce to integer products. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Two forward synthetic transforms keep the same frequency order through the pointwise product, and the opposite transform consumes it.
- Ring products are computed exactly by signed packing into one integer and calling the established $O(n\log n)$ multiplier as a subroutine. (on [Signed packing (Kronecker substitution)](signed-packing.md))

It serves these steps, from the main result down:

- A deterministic fixed-tape machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time, $\kappa=2^{-182}$.; how: reduce multiplication through a chain of representation changes down to ring convolution, using the fast tape procedures, then recover the product (on [Integer multiplication in O(n (lg n)^(1−κ)) time](target.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S6.1). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S6.1**: Two forward synthetic transforms keep the same frequency order through the pointwise product, and the opposite transform consumes it.
Source: "The two forward synthetic transforms" (paper)
> Next, Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections~\ref{sec:synthetic-layouts} and~\ref{sec:exact-ring-products} compute convolution on the remaining axes over this polynomial ring. The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order. Their polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S6.2 (on [Signed packing (Kronecker substitution)](signed-packing.md)): Ring products are computed exactly by signed packing into one integer and calling the established $O(n\log n)$ multiplier as a subroutine.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Discrete Fourier transform](dft.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Polynomial ring modulo y^r + 1](poly-ring-mod.md): Polynomials in y with complex coefficients reduced using y^r = -1; powers of y are roots of unity and multiplying by one is a signed cyclic shift of the coefficient list.
  Shown as: Synthetic polynomial transforms *<predicate>* Polynomial ring modulo y^r + 1
- [FFT and two-point butterflies](butterfly-fft.md): Fast Fourier transform levels built from address rearrangements, root multiplications and two-point butterfly operations; each of Θ(log n) levels scanning Θ(n) bits costs Θ(n log n).
  Shown as: Synthetic polynomial transforms *<predicate>* FFT and two-point butterflies

## Pages that build on this one

- Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic fixed-tape machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time, κ=2^−182, disproving the n log n conjecture in this model; chain: digit convolution, prime axes, resampling and chirps, polynomial ring transforms with fast tape procedures, then rounding and carries.

## Other pages you may link to

- [Multiplication history and the n log n conjecture](nlogn-conjecture.md)
- [Convolution and multiplication](convolution.md)
- [Discrete Fourier transform](dft.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Prime cyclic axes and the Chinese remainder map](multidim-crt.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Tape arrays, scans and elementary streams](tape-streams.md)
- [Linear networks, roles and frames](linear-network-frames.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Address shear and triangular factorization](matrix-shear.md)
- [Fast interchange of address fields](address-interchange.md)
- [Finite networks from three-element subsets](finite-subset-networks.md)
- [Recursive power saving](recursive-saving.md)
- [Resampling with permutations retained in the transform](retained-permutations.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](target.md)

## Evidence from the sources, with the paragraph around each quote

- "These are the
synthetic polynomial transforms of Nussbaumer and Quandalle and
Nussbaumer" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.


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

Write the body to `exegenius/tasks/0009-write-synthetic-transforms.answer.md` and the JSON to `exegenius/tasks/0009-write-synthetic-transforms.answer.json`, then run `exegenius submit 0009-write-synthetic-transforms` in the project directory. If submit rejects the answer, fix the answer and submit again.
