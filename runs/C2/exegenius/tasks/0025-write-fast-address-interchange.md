# exegenius task 0025-write-fast-address-interchange

Project directory: `/home/user/openai-nlogn-wiki/runs/C2` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, basic algorithm design (divide and conquer, recurrences), discrete mathematics (sets, subsets, binary representation, modular arithmetic, primes, gcd), and linear algebra (vector spaces, subspaces, matrices, rank, orthogonal projection, invertible matrices). They have met complex numbers, polynomials and basic Turing machines, but not the fast-multiplication literature, Fourier analysis beyond basics, or advanced algebra and coding theory.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Integer multiplication complexity and the n log n conjecture
- Convolution
- Discrete Fourier transform and butterflies
- Multiplication by radix-digit convolution
- Chinese-remainder map to prime cyclic axes
- Multidimensional transform
- Gaussian resampling
- Bluestein chirp identity
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The indeterminate whose powers serve as roots of unity.
  - $r$ (ring size): The power of two giving the number of coefficients in a polynomial; y^r+1 = 0.
- Last-coordinate phase twist
- Synthetic polynomial transforms
- Packed polynomial products
- Tape scans and address layout
- Address rearrangement cost
- Linear networks, roles and frames
- Finite network from three-element subsets
- Recursive saving giving a power of log
- Rational matrix shear and lower-triangular factorization
- Controlled shifts and rational scalings
- Fixed-point complex dyadics
- Precision analysis and exact recovery
- Recurrence relations and the master theorem (also: recurrence, divide and conquer recurrence, master theorem)
- Binary representation of integers (also: bits, binary expansion, bit strings, radix representation)
- Modular arithmetic (also: congruence, residues, mod, remainder)
- Chinese remainder theorem (also: CRT)
- Prime numbers, gcd and Euclidean algorithm (also: coprime, relatively prime, extended Euclidean algorithm, gcd, modular inverse)
- Vector spaces, subspaces and linear maps (also: linear algebra, subspace, basis, dimension, linear map, orthogonal complement)
- Matrices, rank and invertibility (also: matrix rank, invertible matrix, diagonal matrix, GL, projection matrix, permutation matrix, matrix product)
- Gaussian elimination (also: row reduction, row operations)
- Sets, subsets, functions and permutations (also: bijection, index set, finite set, cardinality, support)
- Floor, ceiling, logarithms and rounding (also: floor, ceiling, lg, log base 2, rounding to nearest integer)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2 pi i/n})
- Cyclic groups and products of groups (also: Z/nZ, cyclic axis, direct product, abelian group)
- Multidimensional arrays and mixed-radix indexing (also: tensor, array indexing, row-major order, index tuple)
- Basic probability and counting bounds (also: averaging argument, pigeonhole principle, counting)
- Norms, error bounds and triangle inequality (also: absolute value of complex number, modulus, max norm, error analysis, rounding error)
- Fixed-point and finite precision arithmetic (also: truncation, dyadic rationals, binary fraction)
- Integer addition, multiplication and carry propagation (also: schoolbook multiplication, carry, long multiplication, linear-time addition)
- Sorting and linear tape scans (also: tape sorting, merge sort, sequential scan)
- Constants, asymptotic functions and polylog factors (also: polylogarithm, log log n, little-o, Theta, Omega)
- XOR and bitwise operations (also: exclusive or, bitwise addition mod 2, GF(2))

## This page

Concept: Fast address-field interchange
Gloss: Interchanges two contiguous address fields via XOR combinations of data and address shears, with an exact final permutation.
Heading: Fast interchange of $u$-bit address fields at cost $O(Vu^\tau)$

The symbols in this page's heading denote (say so on the page):

- $V$ (stored bit volume): The number of stored bits in the array.
- $u$ (field width): The number of bits in each interchanged address field.
- $\tau$ (cost exponent): A fixed constant below 1 giving the power saving.

## This page in the argument

The step: Interchanging two address fields via XOR combinations of data and address shears costs $O(Vu^\tau)$ with $\tau<1$, the final effect being an exact permutation.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: reduce to convolution, accelerate transforms by two network-based tape procedures, then recover the product (on [Integer multiplication in O(n (lg n)^(1-κ)) time](main-theorem.md))
- Two tape procedures, a fast address-field interchange and a simultaneous butterfly layer, cheapen both data movement and arithmetic of the transform levels.; how: supply two fast procedures from one linear-network construction
- Two disjoint contiguous address fields of $u$ bits in an array of volume $V$ can be interchanged in time $O(Vu^\tau)$ with a fixed $\tau<1$.; how: instantiate the bit network with rational subspaces and implement edges by address shears

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Recursive saving giving a power of log](recursive-saving.md): Calling parameter mf uses s<Wm calls at parameter f on volume V/W each, so cost per volume grows by factor s/W<m per multiplication of the parameter, giving a power saving.
  Shown as: Fast address-field interchange *<predicate>* Recursive saving giving a power of log
- [Address rearrangement cost](address-interchange-bottleneck.md): Scanning Θ(n) bits at each of Θ(log n) levels costs n log n, so both movement and arithmetic must be cheapened.
  Shown as: Fast address-field interchange *<predicate>* Address rearrangement cost
- [Rational matrix shear and lower-triangular factorization](address-shear-factorization.md): Every rational matrix factors as lower-triangular times partial permutation times lower-triangular, so an address shear (H,D)->(H+D,D) costs by rank.
  Shown as: Fast address-field interchange *<predicate>* Rational matrix shear and lower-triangular factorization
- [Controlled shifts and rational scalings](controlled-shifts.md): Linear-time stream operations adding control-field-dependent offsets to a target field.
  Shown as: Fast address-field interchange *<predicate>* Controlled shifts and rational scalings

## Pages that build on this one

- Integer multiplication in O(n (lg n)^(1-κ)) time: Deterministic multitape TM multiplying n-bit integers in O(n(lg n)^{1-κ}), κ=2^{-182}, disproving the n log n conjecture in that model.

## Other pages you may link to

- [Integer multiplication complexity and the n log n conjecture](multiplication-history.md)
- [Convolution](convolution.md)
- [Polynomial ring modulo y^r + 1](poly-ring-negacyclic.md)
- [Discrete Fourier transform and butterflies](dft-fft.md)
- [Multiplication by radix-digit convolution](digit-convolution-reduction.md)
- [Multidimensional transform](multidim-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Fixed-point complex dyadics](fixed-point-dyadics.md)
- [Chinese-remainder map to prime cyclic axes](cyclic-crt-axes.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Packed polynomial products](normalized-ring-products.md)
- [Precision analysis and exact recovery](precision-exact-recovery.md)
- [Tape scans and address layout](tape-streams.md)
- [Linear networks, roles and frames](linear-network-roles.md)
- [Finite network from three-element subsets](finite-subset-network.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Simultaneous butterfly layers](fast-butterfly-layers.md)
- [Integer multiplication in O(n (lg n)^(1-κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$." (paper)

  > \begin{lemma}[Arbitrary-width interchange] \label{lem:chunk-swap} There exist fixed $0<\tau<1$ and one fixed finite-alphabet multitape procedure with the following property. For positive integers $P,G,B$ and $u\ge1$, it transforms an arbitrary bit array on \[ [P]\times[2^u]\times[G]\times[2^u]\times[B] \] by the address permutation \[ (p,h,g,d,z)\longmapsto(p,d,g,h,z) \] in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$. The integers specifying the shape are part of the input. The time includes their processing, all padding and unpadding, and fixed-tape workspace cleanup. In particular, $B=1$ is allowed. \end{lemma}

- "Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$." (paper)

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

Write the body to `exegenius/tasks/0025-write-fast-address-interchange.answer.md` and the JSON to `exegenius/tasks/0025-write-fast-address-interchange.answer.json`, then run `exegenius submit 0025-write-fast-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0025-write-fast-address-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
