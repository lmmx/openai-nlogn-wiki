# exegenius task 0019-write-crt-prime-axes

Project directory: `/home/user/openai-nlogn-wiki/runs/B6` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, basic algorithms, discrete mathematics (modular arithmetic, primes, counting, induction), linear algebra over the reals and complex numbers including matrices, rank, invertibility, subspaces and inner products, and elementary Turing machines. They have seen the idea of the FFT and polynomial multiplication, but not Schönhage–Strassen-style multiplication, Nussbaumer transforms, Harvey–van der Hoeven techniques, or specialist tensor and finite-field matrix factorization material.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Schönhage–Strassen conjecture and prior bounds (also: n log n conjecture)
- Convolution and the discrete Fourier transform
- Radix-digit reduction of integer multiplication to convolution
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal variable of the polynomials, whose powers serve as roots of unity.
  - $r$ (coefficient count): The number of complex coefficients of a polynomial record, a power of two.
- Synthetic polynomial transforms
- Coefficient twist to negacyclic convolution
- Fixed-point Gaussian dyadic numerics
- Array order and elementary tape scans
- Fixed linear network exchanging two banks with restored auxiliaries
- Three-element subset construction with nested subspaces
- Frames and pointwise gates on arrays
- Recursive rank saving
- Address shear and Bruhat factorization
- Fast interchange of address chunks
  - $V$ (stored bit volume): The number of stored bits in the array.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (saving exponent): A fixed constant less than 1 giving the power saving.
- Simultaneous butterfly layers
  - $V$ (stored bit volume): The number of stored bits of the numerical array.
  - $d$ (chunk count): The number of equal-width address chunks in which one bit position is selected.
  - $\lambda'$ (saving exponent): A fixed constant less than 1.
- Modular arithmetic and congruences (also: mod, residue ring, Z/mZ, congruence)
- Prime numbers and coprimality (also: pairwise coprime, gcd, distinct primes)
- Floor and ceiling functions (also: floor, ceiling, rounding to nearest integer)
- Binary representation of integers (also: bits, binary expansion, bit strings, two's complement)
- Hamming weight (also: wt, popcount, number of ones)
- Logarithms and exponentials (also: lg, log base 2, iterated logarithm)
- Matrices and linear maps (also: matrix product, invertible matrix, matrix inverse, linear operator, basis vectors)
- Rank, subspaces and orthogonal complements (also: rank deficit, nullspace, kernel, span, dimension, perp)
- Linear algebra over the field F_2 (also: binary vector space, GL(m,F_2), XOR, mod 2 arithmetic, binary matrices)
- Gaussian elimination (also: row reduction, elementary row operations, elementary matrices)
- Triangular and permutation matrices (also: upper triangular, lower triangular, permutation, coordinate permutation)
- Tensor (Kronecker) product of vectors and matrices (also: otimes, Kronecker product, tensor power, multidimensional array)
- Gaussian integers (also: Z[i], a+bi with integer a,b)
- Dyadic rationals (also: dyadic numbers, fixed-point numbers, binary fractions)
- Complex modulus and norms (also: absolute value, Euclidean norm, max norm, disk, triangle inequality)
- Euler's formula and complex exponentials (also: e^{i theta}, unit circle, cos and sin)
- Abstract algebra basics: rings and fields (also: ring, field, group, commutative ring, units)
- Fast Fourier transform divide-and-conquer idea (also: FFT, Cooley–Tukey, butterfly, radix-2 FFT)
- Binomial coefficients and counting (also: choose, subsets, combinatorial counting, pigeonhole)
- Recurrences and recursion analysis (also: recursion tree, master theorem, induction, amortized cost)
- Little-o, Theta and Omega asymptotics (also: o, Theta, Omega, polylogarithmic factors)
- Sorting and permutation routing on tapes (also: merge sort, sorting, table lookup)
- Schoolbook and Karatsuba multiplication (also: long multiplication, grade-school multiplication, O(n^2) multiplication, divide and conquer multiplication)
- Finite-state machine and constant-size alphabet (also: finite control, state transitions, finite alphabet)

## This page

Concept: Chinese-remainder map to prime cyclic axes
Gloss: Places the digit coefficient list on a product of distinct prime-length cyclic axes in a way preserving convolution.

## This page in the argument

The step: A Chinese-remainder map places the digit coefficient list on a product of distinct prime-length cyclic axes, preserving convolution.

It serves these steps, from the main result down:

- Show that $n$-bit integers can be multiplied exactly on a fixed deterministic multitape Turing machine in $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.; how: reduce multiplication to convolution over a negacyclic ring, compute it with synthetic transforms whose address movement and butterflies are accelerated by two linear-network tape procedures, then recover the exact product (on [Sub-n log n integer multiplication algorithm](main-theorem.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Radix-digit reduction of integer multiplication to convolution](integer-to-convolution.md): Splitting integers into radix digits turns the product into a convolution of short integer coefficient lists, followed by carry propagation.
  Shown as: Chinese-remainder map to prime cyclic axes *<predicate>* Radix-digit reduction of integer multiplication to convolution

## Pages that build on this one

- Gaussian resampling: Harvey–van der Hoeven technique expressing a Fourier transform of coprime-length axes through a multidimensional power-of-two tensor transform, with source and target permutations.

## Other pages you may link to

- [Schönhage–Strassen conjecture and prior bounds](multiplication-history.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Fixed-point Gaussian dyadic numerics](fixed-point-gaussian-dyadics.md)
- [Coefficient twist to negacyclic convolution](coefficient-twist.md)
- [Array order and elementary tape scans](tape-streams.md)
- [Fixed linear network exchanging two banks with restored auxiliaries](bank-exchange-network.md)
- [Frames and pointwise gates on arrays](frames.md)
- [Three-element subset construction with nested subspaces](subset-intersection-labels.md)
- [Recursive rank saving](recursive-power-saving.md)
- [Address shear and Bruhat factorization](address-shear.md)
- [Fast interchange of address chunks](fast-address-interchange.md)
- [Convolution and the discrete Fourier transform](convolution-dft.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Simultaneous butterfly layers](simultaneous-butterfly-layers.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Synthetic transform tape layout](synthetic-layout.md)
- [Precision and exact recovery](exact-recovery.md)
- [Signed Kronecker packing](kronecker-signed-packing.md)
- [Harvey–van der Hoeven O(n log n) multiplier as subroutine](hh-subroutine.md)
- [Exact normalized ring products](normalized-polynomial-products.md)
- [Resampling with permutations left in the transform](resampling-permutations-in-transform.md)
- [Sub-n log n integer multiplication algorithm](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "the radix-digit coefficient list is placed on a product of
distinct prime cyclic axes by a Chinese-remainder map that preserves
convolution" (paper)

  > The remaining proof places these procedures inside the multiplication reduction and accounts for every change of representation. First, the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. Section~\ref{sec:assembly} implements this map through triangular controlled shifts and charged axis moves. Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform. Section~\ref{sec:resampling} retains the source and target coordinate permutations in the transform identity, so they need not be executed as separate full sorts.


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

Write the body to `exegenius/tasks/0019-write-crt-prime-axes.answer.md` and the JSON to `exegenius/tasks/0019-write-crt-prime-axes.answer.json`, then run `exegenius submit 0019-write-crt-prime-axes` in the project directory. If submit rejects the answer, fix the answer and submit again.
