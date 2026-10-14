# exegenius task 0029-write-transform-tape-layout

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F8B` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: algorithm analysis with big-O, divide and conquer and sorting, discrete mathematics (sets, permutations, modular arithmetic, primes, induction), and introductory linear algebra (matrices, linear maps, invertibility, triangular and permutation matrices). They know polynomials and complex numbers including roots of unity and Euler's formula, basic calculus functions, and basic Turing machines with several tapes and head movements. They have probably met schoolbook and Karatsuba multiplication and the idea of the FFT, but have not studied abstract algebra beyond basics, finite-field theory, numerical analysis of error, multidimensional Fourier methods, or the Schönhage–Strassen line of fast multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n barrier
- Convolution
- Discrete Fourier transform
- Fast Fourier transform with butterflies
- Fixed-point complex grid and truncation
- Subspaces, rank and orthogonal complements
- Arrays as address fields on tape
- Controlled cyclic shift
- Scratch-restoring bank exchange
- Frames: changing representation along a network
- Triple-subset labels and the rank budget
- Address shear and triangular factorization
- Recursive rank saving
- Power-width chunk interchange
- Address chunk interchange
- Complex phase network
- Packed selected-bit addition
- Simultaneous butterfly layer
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal polynomial variable whose powers act as roots of unity because y^r=−1.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Retained frequency order
- Signed packing (Kronecker substitution)
- Cyclic-to-negacyclic coefficient twist
- Bluestein chirp identity
- Chinese-remainder address map
- Binary numerals and bit strings (also: binary representation, bit string, binary expansion, most significant bit, bits)
- Positional notation in any radix (also: base-b representation, radix, digits in base b, mixed radix)
- Integer division with remainder, floor and ceiling (also: Euclidean division, quotient and remainder, floor function, ceiling function, rounding to nearest integer)
- Modular arithmetic (also: congruence, residues mod m, integers mod m, Z/mZ, clock arithmetic)
- Arithmetic modulo 2 and XOR (also: XOR, exclusive or, bitwise XOR, parity, F_2, GF(2), addition mod 2)
- Primes, coprimality and gcd (also: prime number, relatively prime, greatest common divisor, pairwise coprime, Euclid's algorithm)
- Roots of unity and Euler's formula (also: e^{i theta}, primitive root of unity, nth roots of unity, unit circle, complex exponential)
- Exponential, logarithm and Gaussian function (also: exp, log base 2, lg, natural logarithm, e^{-x^2}, bell curve)
- Asymptotic notation beyond big-O (also: Omega, Theta, little-o, liminf, limit inferior, omega notation)
- Geometric series and sums (also: geometric sum, geometric progression, summation, telescoping)
- Divide and conquer and recurrences (also: recursion, recurrence relation, master theorem, recursion tree, T(n)=aT(n/b)+f(n))
- Schoolbook and Karatsuba multiplication (also: long multiplication, grade-school multiplication, Karatsuba algorithm, O(n^2) multiplication, integer multiplication)
- Sorting and its cost (also: merge sort, comparison sorting, O(n log n) sorting, sorting algorithms)
- Permutations and bijections (also: permutation, bijection, one-to-one correspondence, inverse permutation, reordering)
- Sets, subsets and Cartesian products (also: subset, Cartesian product, indicator vector, characteristic vector, tuples, set intersection, intersection size)
- Multidimensional arrays and row-major order (also: lexicographic order, row-major order, array indexing, nested loops, matrix as array)
- Matrices, vectors and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, linear transformation, linear operator, linear combination, vector space, linear independence, basis, dimension)
- Triangular and permutation matrices (also: lower-triangular matrix, upper-triangular matrix, permutation matrix, LU decomposition, identity matrix, diagonal matrix)
- Dot product, inner product and orthogonality (also: inner product, scalar product, orthogonal vectors, orthonormal, bilinear form)
- Dyadic rationals and fixed-width numerators (also: dyadic fraction, binary fraction, number over a power of two, binary point)
- Matrix transposition (also: transpose, row-major to column-major, transposing an array)
- Triangle inequality and norms (also: maximum norm, sup norm, modulus inequality, |a+b|<=|a|+|b|, error bound)
- Mathematical induction and proof by contradiction (also: induction, inductive proof, proof techniques)
- Cyclic shifts and rotations of lists (also: circular shift, rotation of array, wrap-around shift, cyclic rotation)
- Subroutines and composition of algorithms (also: calling a procedure, black box subroutine, reduction, algorithm composition)

## This page

Concept: Transform layout on tape
Gloss: Placing the selected bit of each participating axis at a common offset in consecutive K-bit chunks, using bit moves and chunk interchanges, so that each transform round is one simultaneous butterfly layer.

## This page in the argument

The step: The forward synthetic transform of $d-1$ axes over $\mathcal R_r$ and its opposite run in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ time with error below $\sqrt2\,\ell\,2^{-p}$, and the forward outputs are kept in a retained layout order.
How: Define the transform by radix-two butterflies with signed-shift twiddles, track where each output lands, and arrange the bits on tape so that each round is one simultaneous butterfly layer.
Why: The cheap roots of unity make the arithmetic free of real multiplications, so the remaining cost is address movement and butterflies; the work is to place each round's selected bits where the simultaneous layer can use them. (the sources say so: "The work here is to apply the simultaneous layers on a suitable tape" (paper))

Its sub-steps, in order:

- In $\mathcal R_r=\mathbb C[y]/(y^r+1)$ the powers of $\omega_t=y^{2r/t}$ are signed shifts, so the transforms $F_t^\pm$ are contractions and satisfy $F_t^+F_t^-=t^{-1}I$. (on [Synthetic polynomial transform](synthetic-polynomial-transform.md))
- The forward procedure writes frequency $j$ at the bit-reversed slot, and the opposite procedure consumes that same order, so the permutation $B_t$ is never executed. (on [Retained frequency order](stored-frequency-order.md))
- Placing the selected bit of every participating axis at a common offset in consecutive $K$-bit chunks by bit moves and chunk interchanges makes each round a simultaneous layer, with all layout and restoration charged in the stated cost.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce the product to a convolution of radix digits evaluated by approximate Fourier transforms over a polynomial ring, make the transform's address movement and arithmetic cheaper with two new tape procedures, then show the result is exact and add up the cost. (on [Integer multiplication below n log n](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.3**: Placing the selected bit of every participating axis at a common offset in consecutive $K$-bit chunks by bit moves and chunk interchanges makes each round a simultaneous layer, with all layout and restoration charged in the stated cost.
Source: "Both layout construction and final restoration are charged in this" (paper)
> The procedure constructs an explicit positional layout permutation $L$ of record addresses, preserving their polynomial suffixes, and transforms disk grid arrays of $M$ contiguous degree-less-than-$r$ polynomial records. Its exact counterpart is $LB F_{\boldsymbol t}^-$. Its opposite procedure consumes that order and has exact counterpart $F_{\boldsymbol t}^+B^{-1}L^{-1}$. Each procedure has error less than $\sqrt2\ell\,2^{-p}$, returns disk grid coefficients in the same component format, and costs \begin{equation} O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right). \label{eq:synthetic-transform-cost} \end{equation} Both layout construction and final restoration are charged in this bound. The forward procedure may retain its output layout for a pointwise product and the following opposite procedure. \end{lemma} \begin{proof} Put $D=d-1$ and write $a_i=\log_2t_i$. The supplied encoding has $2w=\Theta(p)$ bits per coefficient, so the logical bit volume is $\Theta(Tp)$. Call an axis long if $a_i=\ell$ and short if $a_i=\ell-1$. Name the original bit slots of axis $i$ by $(i,h)$, $a_i-1\geq h\geq0$. Initially these slots are in axis order and, within each axis, in decreasing $h$. The coefficients of each polynomial form a contiguous suffix. Put \[ b=(\ell-1)\bmod K, \qquad q=\lfloor(\ell-1)/K\rfloor. \] Form a list of the slots to move to a prefix. First list $(i,\ell

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S3.1 (on [Synthetic polynomial transform](synthetic-polynomial-transform.md)): In $\mathcal R_r=\mathbb C[y]/(y^r+1)$ the powers of $\omega_t=y^{2r/t}$ are signed shifts, so the transforms $F_t^\pm$ are contractions and satisfy $F_t^+F_t^-=t^{-1}I$.
- S3.2 (on [Retained frequency order](stored-frequency-order.md)): The forward procedure writes frequency $j$ at the bit-reversed slot, and the opposite procedure consumes that same order, so the permutation $B_t$ is never executed.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Arrays as address fields on tape](tape-address-model.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Synthetic polynomial transform](synthetic-polynomial-transform.md): A Fourier-type transform over the negacyclic ring whose roots of unity ω_t=y^{2r/t} are signed coefficient shifts, so each twiddle multiplication is free of real arithmetic.
  Shown as: Transform layout on tape *<predicate>* Synthetic polynomial transform
- [Address chunk interchange](address-chunk-interchange.md): Interchanging two disjoint contiguous address fields of u bits of an array in O(V u^τ) time for a fixed τ<1, using XOR combinations of intermediate data although the final effect is an exact permutation.
  Shown as: Transform layout on tape *<predicate>* Address chunk interchange
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): Applying H₀ to the same bit position in each of D≤d address chunks at once, on polynomial records of complex fixed-point coefficients, in O(V d^{λ'}) time with one final truncation.
  Shown as: Transform layout on tape *<predicate>* Simultaneous butterfly layer

## Pages that build on this one

- Normalized convolution over the polynomial ring: Convolving arrays of ring elements by two forward synthetic transforms, a pointwise polynomial product divided by r, and the opposite transform, giving (f*g)/T with a bounded error.

## Other pages you may link to

- [The n log n barrier](n-log-n-barrier.md)
- [Convolution](convolution.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Cyclic-to-negacyclic coefficient twist](coefficient-twist.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Arrays as address fields on tape](tape-address-model.md)
- [Controlled cyclic shift](controlled-cyclic-shift.md)
- [Scratch-restoring bank exchange](scratch-restoring-exchange.md)
- [Frames: changing representation along a network](array-frames.md)
- [Subspaces, rank and orthogonal complements](rank-and-orthogonal-subspaces.md)
- [Triple-subset labels and the rank budget](subset-intersection-labels.md)
- [Address shear and triangular factorization](address-shear-factorization.md)
- [Recursive rank saving](rank-saving-recurrence.md)
- [Power-width chunk interchange](power-width-interchange.md)
- [Chinese-remainder address map](crt-axis-map.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Fixed-point complex grid and truncation](fixed-point-complex-arithmetic.md)
- [Complex phase network](phase-frame-network.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Fast Fourier transform with butterflies](fft-butterflies.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Retained frequency order](stored-frequency-order.md)
- [Contractions and error accounting](contraction-error-propagation.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](permutation-cancellation.md)
- [Normalized convolution over the polynomial ring](normalized-ring-convolution.md)
- [Parameter regime for the multiplier](parameter-regime.md)
- [Radix-digit convolution](radix-digit-reduction.md)
- [Source transform on the padded box](tensor-source-transform.md)
- [Precision and exact recovery](precision-exact-recovery.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks" (paper)

  > To apply Proposition~\ref{prop:simultaneous-layer} in a transform round, we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks. We now construct that layout, keeping each polynomial's coefficients in a contiguous suffix. The layout uses the single-bit moves of Lemma~\ref{lem:elementary-streams} and the chunk interchanges of Lemma~\ref{lem:chunk-swap}; each movement is included in the transform cost. The layer then supplies one truncated contraction per round, and its temporary rows and work streams are removed before the next round begins.


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

Write the body to `exegenius/tasks/0029-write-transform-tape-layout.answer.md` and the JSON to `exegenius/tasks/0029-write-transform-tape-layout.answer.json`, then run `exegenius submit 0029-write-transform-tape-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0029-write-transform-tape-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
