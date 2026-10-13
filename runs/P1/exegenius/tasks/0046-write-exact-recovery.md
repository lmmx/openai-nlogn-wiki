# exegenius task 0046-write-exact-recovery

Project directory: `/home/user/openai-nlogn-wiki/runs/P1` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, functions, induction, summations, recurrences, basic number theory and elementary group/ring/field vocabulary), an algorithms course (recursion, divide and conquer, schoolbook and Karatsuba multiplication, the FFT at the level of the divide-and-conquer recursion, solving recurrences), single-variable calculus (limits, exponentials, logarithms) and one course in linear algebra and complex numbers. They know Turing machines and big-O at an introductory level, but have not studied fast integer multiplication beyond Karatsuba, Schönhage-Strassen or Harvey-van der Hoeven, numerical error analysis, bilinear forms over finite fields, matrix factorizations such as Bruhat decompositions, or tape-level algorithm engineering.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Matrices, rank, subspaces and orthogonality
- Modular arithmetic and the Chinese remainder theorem
- Convolution and cyclic convolution
- Discrete Fourier transform and the convolution theorem
- Butterfly and FFT recursion
- Multidimensional transform (tensor product)
- The n log n optimality conjecture
  - $n$ (input length): The number of bits in each of the two integers being multiplied.
- The established O(n log n) multiplier as a subroutine
- Fixed-point disk grid and truncation
- Contractions and error accumulation
- Exact Gaussian dyadic arithmetic and guard bits
- Arrays, addresses, rows and volume on tape
- Elementary stream operations
- Controlled shifts
- Row splitting among roles with padding
- Depth-first recursion on fixed tapes
- Linear network with roles and restored scratch
- Three-subset gather, scatter and side-wire gadget
- Frames and edge operators
- Nested subspace labels and rank deficit
- Address shear interface
- Lower triangular factorization and matrix shear cost
- Recursive power saving
- Fast address-chunk interchange
- Butterfly kernel H₀ and phase kernel C
  - $H_0$ (butterfly kernel): The two-point map (u,v) ↦ ((u+v)/2,(u−v)/2) acting on a pair of complex values.
  - $C$ (phase kernel): The 2×2 matrix aI+bX with a=(1+i)/2, b=(1−i)/2 that conjugates to the butterfly via phases.
- Binary phase interface
- Packed selected-bit addition
- Simultaneous butterfly layer
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal variable whose powers act as roots of unity in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Retained frequency order
- Transform layout for parallel layers
- Signed packing (Kronecker substitution)
- Ring convolution from the retained transform layout
- Phase twist from cyclic to negacyclic
- Gaussian resampling
- Resampling with the permutations left in the transform
- Bluestein chirp identity
- Source permutation cancellation
- Integer product as radix-digit convolution
- Parameter choices and padded box
- Prime source lengths
- Binary representation and schoolbook arithmetic (also: binary numerals, bits, radix representation, base-b digits, carry propagation, schoolbook addition, schoolbook multiplication, most significant bit, leading zeroes)
- Floor, ceiling and logarithms (also: floor function, ceiling function, lg, log base 2, binary logarithm, iterated logarithm, log*, rounding to nearest integer)
- Exponentials and elementary inequalities (also: exp, e^x, 1+x <= e^x, limits, powers of two, real exponents, fractional powers)
- Summation, telescoping sums and geometric series (also: sigma notation, telescoping, geometric sum, partial sums)
- Recurrences and the recursion tree (also: recurrence relation, solving recurrences, master theorem, divide and conquer, recursive cost, unrolling a recurrence)
- Karatsuba and classical multiplication algorithms (also: Karatsuba multiplication, Toom-Cook, Schönhage-Strassen, O(n^2) multiplication, O(n^{log_2 3}))
- Recursion, call stack and subroutines (also: recursive call, call stack, stack data structure, program counter, subroutine, black-box call)
- Sets, functions, bijections and permutations (also: [n], index set, Cartesian product, bijection, permutation, inverse function, composition of functions, injective, surjective, partial permutation)
- Mathematical induction and proof techniques (also: proof by induction, induction on the number of steps, proof by contradiction, invariant, loop invariant, contrapositive)
- Prime numbers and trial division (also: primes, prime, odd prime, trial division, primality testing by division, coprime integers, relatively prime, prime factorization)
- Groups, rings and fields (also: algebraic structure, ring, field, group, finite field, F_2, GF(2), ring of residues Z/qZ, units of a ring, quotient ring, cyclic group)
- XOR and arithmetic over F_2 (also: exclusive or, bitwise XOR, addition mod 2, parity, bit flip, bitwise operations, bit shift)
- Special matrices and matrix algebra (also: identity matrix, diagonal matrix, permutation matrix, invertible matrix, matrix inverse, transpose, matrix product, standard basis vector, lower triangular matrix, block matrix, matrix-vector product)
- Triangle inequality and norm bounds (also: triangle inequality, modulus of a sum, |z+w| <= |z|+|w|, maximum norm, sup norm, absolute error, error bound)
- Rational numbers and dyadic fractions (also: rational numbers, fractions, dyadic rational, denominator a power of 2, numerator and denominator, lowest terms)
- Deterministic algorithms and worst-case time (also: deterministic machine, worst-case running time, time complexity, fixed finite alphabet, linear time scan)
- Entrywise operations on arrays and vectors (also: pointwise product, componentwise product, Hadamard product, vector of coefficients, coefficient list, array indexing, multi-index)

## This page

Concept: Exact recovery by scaling, rounding and carries
Gloss: Removing the known normalizations S and 2^{2b+4}, proving the coefficient error is below 1/2, rounding to integers and propagating radix-2^b carries to the exact 2n-bit product.

## This page in the argument

The step: Rescaling by $S$ and $2^{2b+4}$ undoes the normalizations, the coefficient error is below $448\,b\,2^{-3b/4}<1/2$, so rounding gives the exact integer coefficients $c_j<2^{3b}$ and radix-$2^b$ carries give the $2n$-bit product.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet, fixed-tape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$.; how: Split the integers into radix digits, compute the digit convolution with synthetic transforms whose data movement and butterfly arithmetic are accelerated by two new tape procedures, and recover the exact product by rounding and carries. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](integer-multiplication-below-nlogn.md))
- Choosing the parameters $b,p,d,T,S$ compatibly, the radix-digit convolution is mapped onto prime-length axes, evaluated by source transforms, multiplied pointwise and inverted, and the exact $2n$-bit product is recovered by scaling, rounding and carries within time $O(n(\lg n)^{1-\kappa})$.; how: Fix one compatible set of rational exponents and sizes, reduce the integer product to a convolution on prime axes, evaluate the three transforms with the source transform, then verify the error bound for rounding and total the cost.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Contractions and error accumulation](contractions-and-error.md): A linear map is a contraction if it does not increase the maximum-modulus norm; approximate algorithms for contractions compose with errors that add.
  Shown as: Exact recovery by scaling, rounding and carries *<predicate>* Contractions and error accumulation
- [Integer product as radix-digit convolution](integer-as-digit-convolution.md): Writing both inputs in base 2^b with q digits, the integer product is the convolution of the digit lists; padding to length S exceeds the degree so no wraparound occurs and coefficients stay below 2^{3b}.
  Shown as: Exact recovery by scaling, rounding and carries *<predicate>* Integer product as radix-digit convolution
- [Fixed-point disk grid and truncation](fixed-point-disk-grid.md): Complex numbers of modulus at most 1 whose real and imaginary parts are multiples of 2^{−p}, stored as signed two's-complement numerators, with Q_p truncating toward zero.
  Shown as: Exact recovery by scaling, rounding and carries *<predicate>* Fixed-point disk grid and truncation

## Pages that build on this one

- The multiplication algorithm: The six steps: form radix digits, apply the address map Φ, compute two source transforms, multiply pointwise, apply the opposite transform, rescale, round and carry.

## Other pages you may link to

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Convolution and cyclic convolution](convolution.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-y-r-plus-1.md)
- [The established O(n log n) multiplier as a subroutine](nlogn-multiplier-subroutine.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Arrays, addresses, rows and volume on tape](tape-address-arrays.md)
- [Elementary stream operations](elementary-stream-operations.md)
- [Row splitting among roles with padding](row-splitting.md)
- [Modular arithmetic and the Chinese remainder theorem](modular-arithmetic.md)
- [Controlled shifts](controlled-shifts.md)
- [Matrices, rank, subspaces and orthogonality](linear-algebra-basics.md)
- [Linear network with roles and restored scratch](linear-network-roles.md)
- [Frames and edge operators](frames.md)
- [Three-subset gather, scatter and side-wire gadget](triple-subset-gadget.md)
- [Nested subspace labels and rank deficit](subspace-labels-rank-deficit.md)
- [Address shear interface](address-shear.md)
- [Lower triangular factorization and matrix shear cost](triangular-factorization.md)
- [Depth-first recursion on fixed tapes](fixed-tape-recursion.md)
- [Recursive power saving](recursive-power-saving.md)
- [Fast address-chunk interchange](address-chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Exact Gaussian dyadic arithmetic and guard bits](guard-bits-dyadic.md)
- [Phase twist from cyclic to negacyclic](phase-twist.md)
- [Discrete Fourier transform and the convolution theorem](dft.md)
- [Multidimensional transform (tensor product)](multidimensional-transform.md)
- [Butterfly and FFT recursion](fft-butterfly.md)
- [Synthetic polynomial transform](synthetic-polynomial-transform.md)
- [Butterfly kernel H₀ and phase kernel C](butterfly-and-phase-kernels.md)
- [Retained frequency order](frequency-order-retention.md)
- [Binary phase interface](binary-phase-interface.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout for parallel layers](synthetic-transform-layout.md)
- [Ring convolution from the retained transform layout](synthetic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling with the permutations left in the transform](resampling-permutations-retained.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Source permutation cancellation](permutation-cancellation.md)
- [Parameter choices and padded box](parameter-choice.md)
- [Prime source lengths](prime-source-lengths.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Source transform pipeline](source-transform.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost analysis and the exponent κ](cost-analysis.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](integer-multiplication-below-nlogn.md)

## Evidence from the sources, with the paragraph around each quote

- "proves that the recovered
coefficient error is strictly below $1/2$, and propagates carries to
obtain the exact binary product" (paper)

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

Write the body to `exegenius/tasks/0046-write-exact-recovery.answer.md` and the JSON to `exegenius/tasks/0046-write-exact-recovery.answer.json`, then run `exegenius submit 0046-write-exact-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0046-write-exact-recovery`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
