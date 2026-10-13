# exegenius task 0026-write-ring-products

Project directory: `/home/user/openai-nlogn-wiki/runs/A4` (paths below are relative to it)

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

For these sources: An undergraduate computer science reader who knows asymptotic notation, basic discrete mathematics, linear algebra over the reals and complex numbers, elementary algebra (groups, rings, modular arithmetic, polynomials), elementary number theory (primes, CRT) and basic probability/combinatorics. They know basic Turing machines and tapes and the schoolbook and Karatsuba multiplication, and probably the FFT as an algorithm. They have not studied multitape-machine algorithm engineering, Schönhage–Strassen or later multiplication algorithms, or specialist linear-algebra constructions such as Bruhat factorizations.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Array order and elementary tape scans
- Convolution and Fourier transforms
- Multiplication as convolution of radix digits
- Established O(n log n) multiplication and history
- Signed coefficient packing (Kronecker substitution)
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The formal indeterminate of the polynomials, whose powers serve as roots of unity.
  - $r$ (ring degree): The number of complex coefficients in a record, a power of two; y^r = -1 in the ring.
- Synthetic polynomial transforms
- Two-point butterfly H₀
  - $u$ (first operand): The first of the two input values (a polynomial record).
  - $v$ (second operand): The second of the two input values.
- Multidimensional transform with power-of-two axes
- Chinese-remainder map to distinct prime cyclic axes
- Gaussian resampling
- Bluestein's chirp identity
- Last-coordinate phase twist
- Fixed-point complex coefficients and exact recovery
- Linear networks, roles and frames
- Finite networks from three-element subsets
- Recursive power saving from s < Wm
- Address shear and restoration of scratch values
- Fast interchange of address chunks
  - $V$ (stored bit volume): The total number of stored bits in the array.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (address exponent): A fixed constant below 1 in the interchange cost.
- Fast simultaneous butterfly layers
  - $V$ (stored bit volume): The total number of stored bits in the numerical arrays.
  - $d$ (chunk count): The number of equal-width address chunks in which a bit position is selected.
  - $\lambda'$ (layer exponent): A fixed constant below 1 in the layer cost.
- Synthetic transforms on tape layouts
- Binary representation and bit operations (also: bit strings, binary expansion, XOR, bitwise exclusive or, Hamming weight)
- Modular arithmetic and congruences (also: residue ring, integers mod m, Z/mZ)
- Primes and divisibility (also: gcd, coprime, relatively prime, prime number theorem)
- Linear algebra over fields (also: vector space, subspace, rank, invertible matrix, linear map, GL, diagonal matrix)
- Permutations and bijections (also: permutation, index permutation, bit reversal, bijection)
- Groups and rings (basic algebra) (also: group, cyclic group, ring, abelian group, subgroup)
- Finite sets and elementary combinatorics (also: subsets, counting arguments, binomial coefficients, intersection sizes)
- Floating and fixed-point approximation and rounding (also: rounding error, error bounds, triangle inequality)
- Recurrences and divide-and-conquer analysis (also: recursion, master theorem, recursion tree, geometric series)
- Logarithms and exponentials (also: lg, log base 2, iterated logarithm, powers of two)
- Fast Fourier transform algorithm (also: FFT, Cooley-Tukey, DFT)
- Schoolbook and Karatsuba multiplication (also: long multiplication, Karatsuba)
- Floor, ceiling and big-omega notation (also: floor, ceiling, Omega, Theta, little-o)

## This page

Concept: Exact polynomial-ring products
Gloss: Products in the ring modulo y^r+1 computed by signed packing and the established O(n log n) multiplier as subroutine, giving normalized convolution.

## This page in the argument

The step: Products in the ring modulo $y^r+1$ are computed exactly by signed packing and the established $O(n\log n)$ multiplier.
How: pack polynomials into integers and call the known multiplier
Why: Pointwise products of synthetic-transform records are ring products; Kronecker packing turns them into integer products the known O(n log n) multiplier handles. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Signed coefficient packing (Kronecker substitution) turns a polynomial product into an integer product. (on [Signed coefficient packing (Kronecker substitution)](kronecker-packing.md))
- The polynomial products use signed packing and the established multiplier as an ordinary subroutine.

It serves these steps, from the main result down:

- Integer multiplication of $n$-bit integers takes $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$ on a fixed multitape Turing machine.; how: reduce to digit convolution, supply two fast tape procedures, chain reductions, then total the cost (on [Integer multiplication in O(n (lg n)^(1−κ)) time](fast-multiplication.md))
- The digit convolution is carried through four reductions down to convolution over $\mathbb C[y]/(y^r+1)$, then rescaled, rounded and carried.; how: chain of reductions of problem and representation
- Convolution on the remaining axes over the polynomial ring is computed by synthetic transforms and ring products.; how: forward synthetic transforms, pointwise product, opposite transform (on [Synthetic transforms on tape layouts](synthetic-layout.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.5.2.2). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.5.2.2**: The polynomial products use signed packing and the established multiplier as an ordinary subroutine.
Source: "use signed packing and the established $O(n\log n)$ multiplier as an" (paper)
> Next, Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections~\ref{sec:synthetic-layouts} and~\ref{sec:exact-ring-products} compute convolution on the remaining axes over this polynomial ring. The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order. Their polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S3.5.2.1 (on [Signed coefficient packing (Kronecker substitution)](kronecker-packing.md)): Signed coefficient packing (Kronecker substitution) turns a polynomial product into an integer product.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Signed coefficient packing (Kronecker substitution)](kronecker-packing.md): Encode a polynomial with bounded integer coefficients as one integer by evaluating at a power of two with signed digits, so a polynomial product becomes an integer product.
  Shown as: Exact polynomial-ring products *<predicate>* Signed coefficient packing (Kronecker substitution)
- [Established O(n log n) multiplication and history](known-nlogn.md): Schönhage–Strassen O(n log n log log n), Fürer, and Harvey–van der Hoeven O(n log n) multiplication on multitape machines, with n log n conjectured optimal; the O(n log n) multiplier is used as a subroutine.
  Shown as: Exact polynomial-ring products *<predicate>* Established O(n log n) multiplication and history
- [Polynomial ring modulo y^r + 1](ring-mod-yr.md): Complex polynomials in y reduced modulo y^r+1, so y^r = −1; multiplying by a power of y is a signed cyclic shift of the coefficient list and powers of y act as roots of unity.
  Shown as: Exact polynomial-ring products *<predicate>* Polynomial ring modulo y^r + 1

## Pages that build on this one

- Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape algorithm: digit convolution, CRT prime axes, Gaussian resampling, Bluestein chirps, phase twist, synthetic transforms with fast interchanges and butterfly layers, then rounding and carries; time O(n (lg n)^(1−κ)), κ=2^−182, disproving the n log n conjecture in this model.

## Other pages you may link to

- [Fixed multitape Turing machine model](multitape-model.md)
- [Convolution and Fourier transforms](convolution-dft.md)
- [Multiplication as convolution of radix digits](radix-digit-reduction.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Array order and elementary tape scans](elementary-scans.md)
- [Two-point butterfly H₀](butterfly-h0.md)
- [Multidimensional transform with power-of-two axes](multidim-transform.md)
- [Linear networks, roles and frames](linear-network-frames.md)
- [Address shear and restoration of scratch values](address-shear.md)
- [Finite networks from three-element subsets](subset-finite-network.md)
- [Recursive power saving from s < Wm](recursive-saving.md)
- [Fast interchange of address chunks](address-interchange.md)
- [Chinese-remainder map to distinct prime cyclic axes](crt-prime-axes.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Fixed-point complex coefficients and exact recovery](fixed-point-precision.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Synthetic transforms on tape layouts](synthetic-layout.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](fast-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "Their polynomial products" (paper)

  > Next, Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections~\ref{sec:synthetic-layouts} and~\ref{sec:exact-ring-products} compute convolution on the remaining axes over this polynomial ring. The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order. Their polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.

- "use signed packing and the established $O(n\log n)$ multiplier as an" (paper)

  > Next, Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections~\ref{sec:synthetic-layouts} and~\ref{sec:exact-ring-products} compute convolution on the remaining axes over this polynomial ring. The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order. Their polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.


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

Write the body to `exegenius/tasks/0026-write-ring-products.answer.md` and the JSON to `exegenius/tasks/0026-write-ring-products.answer.json`, then run `exegenius submit 0026-write-ring-products` in the project directory. If submit rejects the answer, fix the answer and submit again.
