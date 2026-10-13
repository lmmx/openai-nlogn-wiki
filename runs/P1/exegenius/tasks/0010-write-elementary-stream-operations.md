# exegenius task 0010-write-elementary-stream-operations

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
- Convolution and cyclic convolution
- The n log n optimality conjecture
  - $n$ (input length): The number of bits in each of the two integers being multiplied.
- The established O(n log n) multiplier as a subroutine
- Arrays, addresses, rows and volume on tape
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal variable whose powers act as roots of unity in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Signed packing (Kronecker substitution)
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

Concept: Elementary stream operations
Gloss: Linear-time tape scans: permuting two digit positions, moving a digit, splitting into streams and merging, and splitting whole rows cyclically into W streams.

## This page in the argument

The step: Fixed digit permutations, moving one digit, splitting on a digit and merging, and splitting whole rows cyclically into $W$ streams each take $O(V)$ steps on a fixed number of tapes.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet, fixed-tape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$.; how: Split the integers into radix digits, compute the digit convolution with synthetic transforms whose data movement and butterfly arithmetic are accelerated by two new tape procedures, and recover the exact product by rounding and carries. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](integer-multiplication-below-nlogn.md))
- Two tape procedures exist: interchanging two $u$-bit address chunks of an array of volume $V$ in $O(Vu^\tau)$ time with $\tau<1$, and applying $H_0$ at one bit position in each of $D\le d$ address chunks in $O(Vd^{\lambda'})$ time with $\lambda'<1$.; how: Build one fixed linear network per procedure that exchanges two banks of values with signs while restoring all scratch wires, label it with nested subspaces so that the sum $s$ of edge ranks is below $Wm$, and recurse on the edges.
- Linear-time scans on arrays stored in lexicographic order on a fixed number of tapes (permuting or moving digits, splitting and merging streams, controlled cyclic shifts of a later field) supply the elementary operations of both tape procedures.; how: Fix the array and address conventions, then prove the few linear-time scans (digit moves, stream splits and merges, controlled shifts) that every later procedure is built from.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Arrays, addresses, rows and volume on tape](tape-address-arrays.md): Arrays with multi-field addresses stored in lexicographic order on a tape, with address fields, row fields, prefix and suffix, spectator fields and logical volume V in bits.
  Shown as: Elementary stream operations *<predicate>* Arrays, addresses, rows and volume on tape

## Pages that build on this one

- Row splitting among roles with padding: Distributing whole rows cyclically among the W wire roles, after padding the row count to a multiple of a power of W, so each role stream has volume V/W.
- Controlled shifts: Updating a later address field by an offset computed from earlier fields (y ↦ y+a mod q^b), or multiplying it by a rational unit, in linear time.
- Depth-first recursion on fixed tapes: Running recursive calls with finitely many tapes by parking inactive role streams on a stack tape, copying the active one to the child, and restoring afterwards, at cost linear in the parent's volume.
- Packed selected-bit addition: XORing corresponding selected bits of two address chunks across many chunks at once, using a temporary third chunk, a few cyclic shifts, and a deterministic repair of a small exceptional set of addresses.

## Other pages you may link to

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Convolution and cyclic convolution](convolution.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-y-r-plus-1.md)
- [The established O(n log n) multiplier as a subroutine](nlogn-multiplier-subroutine.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
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
- [Fixed-point disk grid and truncation](fixed-point-disk-grid.md)
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
- [Contractions and error accumulation](contractions-and-error.md)
- [Ring convolution from the retained transform layout](synthetic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling with the permutations left in the transform](resampling-permutations-retained.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Source permutation cancellation](permutation-cancellation.md)
- [Parameter choices and padded box](parameter-choice.md)
- [Prime source lengths](prime-source-lengths.md)
- [Integer product as radix-digit convolution](integer-as-digit-convolution.md)
- [Exact recovery by scaling, rounding and carries](exact-recovery.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Source transform pipeline](source-transform.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost analysis and the exponent κ](cost-analysis.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](integer-multiplication-below-nlogn.md)

## Evidence from the sources, with the paragraph around each quote

- "Each of the following operations on an array of
volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes" (paper)

  > \begin{lemma}[Elementary stream operations] \label{lem:elementary-streams} Fix a radix $q\ge2$. Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes: \begin{enumerate} \item any fixed permutation of the pair of digit values at two specified radix-$q$ positions, whether or not the positions are adjacent; \item moving one specified radix-$q$ digit to another position, preserving the order of the intervening positions; \item splitting on a specified radix-$q$ digit, applying a fixed pointwise map to aligned streams, and merging them back; \item for positive integers $P,R,B$, within each prefix of an array on $[P]\times[R]\times[B]$, splitting whole rows cyclically into a fixed number $W$ of streams, and, when $W$ divides $R$, merging those streams in any fixed order of the row classes. \end{enumerate} The bounds include shape preparation, counter initialization and resets, and returning or clearing the visited portions of work tapes. Their constants may depend on the fixed radix, the fixed pointwise map, and the fixed number of row classes. \end{lemma}


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

Write the body to `exegenius/tasks/0010-write-elementary-stream-operations.answer.md` and the JSON to `exegenius/tasks/0010-write-elementary-stream-operations.answer.json`, then run `exegenius submit 0010-write-elementary-stream-operations` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0010-write-elementary-stream-operations`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
