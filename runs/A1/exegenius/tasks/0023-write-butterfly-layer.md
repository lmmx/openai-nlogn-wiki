# exegenius task 0023-write-butterfly-layer

Project directory: `/home/user/openai-nlogn-wiki/runs/A1` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: asymptotic analysis, recursion and divide-and-conquer recurrences, basic discrete mathematics (modular arithmetic, primes, Chinese remainder theorem, permutations, sets), and introductory linear algebra (vectors, matrices, invertible maps, subspaces, triangular matrices, Gaussian elimination). They know binary arithmetic, schoolbook and Karatsuba multiplication, and basic Turing machines with tapes. They have not studied abstract algebra beyond basics, the FFT in depth, Schönhage-Strassen, Nussbaumer transforms, or fast multitape tape-programming techniques; those are explained by the wiki.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Convolution and cyclic convolution
- Fourier transform and roots of unity
- The n log n optimality conjecture
- Multiplication as radix-digit convolution
- Arrays on tapes, scans and stored bit volume
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The formal variable of the polynomials; its powers serve as roots of unity.
  - $r$ (coefficient count): The number of complex coefficients in a record, a power of two.
- Synthetic polynomial transforms
- Controlled shifts and carries by packing
- Signed coefficient packing (Kronecker substitution) and the n log n subroutine
- Chinese-remainder map onto prime cyclic axes
- Gaussian resampling
- Bluestein chirp conversion
- Last-coordinate phase twist
- Linear networks with roles and frames
- Restoring auxiliary values
- Finite network from three-element subsets
- Recursive power saving
- Address shear and lower triangular factorization
- Fast address-field interchange
  - $V$ (stored bit volume): The total number of bits stored in the array.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (interchange exponent): A fixed constant below 1 giving the power saving in the field width.
- Logarithms and iterated logarithms (also: lg, log base 2, log n, lg lg n)
- Binary representation of integers (also: bits, n-bit integer, binary expansion, base 2)
- Positional radix notation (also: base-b digits, radix, digit expansion)
- Schoolbook and Karatsuba multiplication (also: long multiplication, quadratic multiplication, Karatsuba)
- Recursion and divide-and-conquer recurrences (also: master theorem, recurrence relation, recursive algorithm, recursion depth)
- Modular arithmetic (also: congruence, mod n, residues, cyclic group Z/n)
- Primes and coprimality (also: prime numbers, pairwise coprime, gcd, distinct primes, prime factorization)
- Chinese remainder theorem (also: CRT, Chinese remainder)
- Permutations and bijections (also: permutation of indices, bijective map, rearrangement, sorting)
- Vectors, matrices and linear maps (also: matrix-vector product, linear operator, linear transformation, invertible matrix, operator composition)
- Subspaces, dimension and linear independence (also: vector subspace, span, rank, nested subspaces, ground set)
- Triangular matrices and Gaussian elimination (also: lower triangular matrix, row reduction, LU factorization, elementary row operations)
- Bitwise operations and XOR (also: exclusive or, bit string, bit field, bit position, addition mod 2)
- Cartesian products and multidimensional arrays (also: product of sets, tuples, multi-index, array indexing, d-dimensional array)
- Sets and subsets (also: three-element subsets, finite set, set cardinality)
- Rationals, rounding and error bounds (also: floor and ceiling, rounding to nearest integer, absolute error, triangle inequality, fixed-point approximation)
- Dyadic rationals and fixed-point numbers (also: binary fractions, truncation, fixed-precision arithmetic, dyadic numbers)
- Two's complement and signed integers (also: signed integers, sign bit, negative numbers in binary, sign and magnitude)
- Basic ring and group structure (also: ring, commutative ring, quotient by a polynomial, homomorphism, algebraic identity)
- Euler's formula and primitive roots of unity (also: e^{2 pi i/N}, primitive N-th root of unity, unit circle, complex exponential)
- Fast Fourier transform for power-of-two length (also: FFT, Cooley-Tukey, radix-2 FFT, butterfly, O(n log n) transform)
- Gaussian function (also: Gaussian, exp(-x^2), bell curve, Gaussian decay)
- Time and space as functions of input size (also: linear time, running time, worst-case complexity, deterministic algorithm, subroutine call)
- Tape head movement and sequential access (also: tape scan, head moves, sequential access, copying between tapes, sorting on tapes)

## This page

Concept: Simultaneous butterfly layer
Gloss: The map H₀(u,v)=((u+v)/2,(u−v)/2) applied coefficientwise to polynomial records at one chosen bit position in each of d address chunks at cost O(V d^λ′), using exact Gaussian dyadic intermediates and one truncation afterward.
Heading: Simultaneous butterfly layers in cost $O(Vd^{\lambda'})$

The symbols in this page's heading denote (say so on the page):

- $V$ (stored bit volume): The total number of bits stored in the numerical arrays.
- $d$ (chunk count): The number of equal-width address chunks in which one bit position is selected.
- $\lambda'$ (butterfly exponent): A fixed constant below 1 giving the power saving in the number of selected chunks.

## This page in the argument

The step: The map $H_0(u,v)=((u+v)/2,(u-v)/2)$ is applied on one bit position in each of $d$ address chunks at cost $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce the product to a convolution over the polynomial ring through a chain of representation changes, and make the transforms there cheap with two fast tape procedures that save a power of the logarithmic factor. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Two tape procedures cost less than a scan per level: interchanging address fields and applying butterfly layers both save a power.; how: State the two procedures with their costs, each obtained from its own fixed linear network.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Recursive power saving](recursive-power-saving.md): A recursive call at parameter mf uses s<Wm calls at parameter f on streams of volume V/W, so dividing by volume the cost grows by factor s/W<m per multiplication of the parameter by m, giving a power rather than a logarithmic saving.
  Shown as: Simultaneous butterfly layer *<predicate>* Recursive power saving
- [Synthetic polynomial transforms](synthetic-transforms.md): Fourier-type transforms over the ring modulo y^r+1 that use powers of y as roots of unity, so each transform consists of address rearrangements, signed shifts and butterflies (Nussbaumer; Quandalle and Nussbaumer).
  Shown as: Simultaneous butterfly layer *<predicate>* Synthetic polynomial transforms
- [Arrays on tapes, scans and stored bit volume](tape-arrays-and-streams.md): Data is stored as arrays addressed by fields of bits in a fixed order on tapes; elementary scans and stream operations cost time linear in the stored bit volume.
  Shown as: Simultaneous butterfly layer *<predicate>* Arrays on tapes, scans and stored bit volume

## Pages that build on this one

- Synthetic transform layout and convolution: Forward synthetic transforms keep the same frequency order through the pointwise product and the opposite transform consumes it, so convolution over the ring is computed on the retained layout using fast butterfly layers and address interchanges.
- Precision, rounding and carry propagation: After removing known normalizations and digit scales, the recovered coefficient error is shown strictly below 1/2, so rounding gives exact integer coefficients and carries yield the binary product.

## Other pages you may link to

- [Convolution and cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-convolution.md)
- [Polynomial ring modulo y^r + 1](ring-mod-yr.md)
- [Fourier transform and roots of unity](dft.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Linear networks with roles and frames](linear-networks-frames.md)
- [Controlled shifts and carries by packing](controlled-shifts.md)
- [Address shear and lower triangular factorization](address-shear.md)
- [Chinese-remainder map onto prime cyclic axes](chinese-remainder-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp conversion](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Signed coefficient packing (Kronecker substitution) and the n log n subroutine](signed-packing.md)
- [Restoring auxiliary values](restoring-auxiliary-values.md)
- [Finite network from three-element subsets](finite-subset-network.md)
- [Fast address-field interchange](address-interchange.md)
- [Synthetic transform layout and convolution](transform-layout-convolution.md)
- [Precision, rounding and carry propagation](precision-exact-recovery.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The second procedure applies
\[
 H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr)
\]" (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.

- "the cost is $O(Vd^{\lambda'})$ for a
fixed $\lambda'<1$" (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.


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

Write the body to `exegenius/tasks/0023-write-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0023-write-butterfly-layer.answer.json`, then run `exegenius submit 0023-write-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.
