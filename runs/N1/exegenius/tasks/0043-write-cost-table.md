# exegenius task 0043-write-cost-table

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N1` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science background: asymptotic analysis of algorithms and solving simple cost recurrences, basic Turing machines and multitape simulation, binary representation of integers and machine arithmetic (carries, two's complement, XOR, fixed-point rounding), and the discrete mathematics taught to everyone (induction, modular arithmetic, gcd, primes, the Chinese remainder theorem, permutations, binomial coefficients, lexicographic order). From the required mathematics they have a first course in linear algebra (vectors, matrices, rank, invertibility, triangular and diagonal matrices, linear maps over Q and C) and basic complex numbers and polynomials. They have not studied tensor products of operators, bilinear forms, Hadamard or Bruhat-type factorizations, FFT variants beyond a textbook mention, or research-level integer multiplication algorithms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
  - $n$ (input bit length): The number of bits in each of the two integers being multiplied.
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
  - $n$ (input bit length): The number of bits in each input of the subroutine multiplication.
  - $O$ (big-O bound): Asymptotic upper bound up to a constant factor.
- Cyclic convolution
- Radix-digit convolution (also: Kronecker splitting into digits)
- Normalized discrete Fourier transform (also: Fourier transform, DFT)
- Array streams and logical volume (also: logical volume, address field, row)
- Elementary stream operations
- Controlled shifts (also: prefix-controlled cyclic shift)
- Chinese-remainder address map (also: CRT map, prime source lengths)
- Gaussian resampling
- Resampling with retained permutations (also: no-sort resampling, permutation cancellation)
- Tensor resampling interface
- Bluestein's chirp identity (also: chirp transform)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring indeterminate): The polynomial variable whose powers act as synthetic roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Coefficient phase twist (also: coefficient twist)
- Normalized butterfly H₀ (also: H0)
  - $H_0$ (normalized butterfly): The two-point linear map sending (u, v) to ((u+v)/2, (u−v)/2).
- Gaussian dyadics and fixed-point truncation (also: disk grid, Q_p truncation, guard bits)
- Synthetic polynomial transform (also: Nussbaumer transform, synthetic transform)
- Linear bank-exchange network (also: finite network, role, wire)
- Restoration of arbitrary scratch values (also: transparent computation)
- Three-element-subset gather and scatter (also: index-code decoding, Frankl–Wilson construction)
- Frames and the common-frame identity (also: frame)
- Nested subspace labels (also: orthogonal residual, labels)
- Rank deficit of the network (also: s < Wm)
- Address shear (also: shear)
- Rational matrix interface (also: bit network)
- Lower triangular factorization (also: Bruhat factorization)
- Cost of a rational matrix shear
- Row splitting among roles
- Volume-normalized recurrence (also: recursive saving)
- Fast address chunk interchange (also: chunk swap, address interchange)
- Binary phase frames (also: kernel C, phase kernel)
- Binary phase interface (also: complex network)
- Packed selected-bit addition (also: binary change of basis, deterministic repair)
- Simultaneous butterfly layer (also: fast butterfly layer, parallel butterfly)
- Transform layout
- Signed coefficient packing (also: Kronecker substitution)
- Convolution from the retained transform layout
- Exact recovery by rounding and carries
- Binary representation of integers (also: n-bit integer, base-2 expansion, binary digits, bits)
- Carry propagation (also: carries, ripple carry, radix carries, positional addition)
- Two's complement (also: sign-extended two's complement, signed binary integers, sign extension)
- Exclusive or (also: XOR, addition modulo 2, bitwise XOR)
- Schoolbook multiplication (also: long multiplication, grade-school multiplication, quadratic multiplication)
- Floor and ceiling (also: floor function, ceiling function, integer part, ⌊x⌋, ⌈x⌉)
- Rounding to the nearest integer (also: rounding, truncation toward zero, round-off error)
- Fixed-point numbers (also: fixed-point arithmetic, binary fractions, dyadic fractions in a word)
- Binary logarithm (also: lg, log base 2, logarithm, log n)
- Modular arithmetic (also: congruence modulo m, residues, mod, a ≡ b (mod m), centered residue)
- Greatest common divisor (also: gcd, coprime, relatively prime)
- Prime numbers (also: primes, prime factorization)
- Chinese remainder theorem (also: CRT, Chinese remaindering)
- Mathematical induction (also: induction, proof by induction, inductive argument)
- Recurrence relations for running time (also: recurrence, divide-and-conquer recurrence, unrolling a recurrence)
- Geometric series (also: geometric sum, sum of a geometric progression)
- Permutations (also: permutation, bijection of a finite set, reordering, inverse permutation)
- Binomial coefficients (also: n choose k, binom, k-element subsets)
- Lexicographic order (also: lex order, dictionary order, row-major order)
- Vectors and matrices (also: matrix, vector, matrix multiplication, identity matrix, transpose)
- Vector spaces, subspaces and dimension (also: linear subspace, basis, dimension, span, linear map)
- Matrix rank (also: rank, column rank, full rank)
- Invertible matrices (also: nonsingular matrix, inverse matrix, determinant nonzero)
- Triangular and diagonal matrices (also: lower triangular matrix, upper triangular, diagonal matrix, diag, unit triangular)
- Permutation matrices (also: permutation matrix, partial permutation matrix)
- Gaussian elimination (also: row reduction, elimination, LU decomposition)
- Rational numbers (also: Q, fractions, rational matrix)
- Maximum norm (also: infinity norm, sup norm, ‖·‖∞, max absolute entry)
- Triangle inequality (also: |a + b| ≤ |a| + |b|)
- Exponential function and Euler's formula (also: e^{iθ}, Euler's formula, Gaussian function e^{-x^2})

## This page

Concept: Parameter choice and cost table
Gloss: Fixed rational parameters (τ = 1 − 2^{-50}, ε = 2^{-75}, κ = 2^{-182}, …) under which every term of the cost per bit is at most p^{1−2κ}.

## This page in the argument

The step: With $\tau=1-2^{-50}$, $\epsilon=2^{-75}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $\delta=1/16$, every row of the cost table divided by $Tp$ is at most $p^{1-2\kappa}$, so the total time is $O(n(\lg n)^{1-\kappa})$.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet multitape Turing machine computes the exact $2n$-bit product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.; how: build two tape procedures that beat a scan per level (fast chunk interchange and simultaneous butterfly layers) from finite linear networks with a rank deficit, place them in the Gaussian-resampling and synthetic-transform reduction of multiplication to convolution, recover the product exactly, and total the costs (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fast address chunk interchange](chunk-interchange.md): A fixed-tape procedure that exchanges two equal-width contiguous address chunks of u bits in O(Vu^τ) time with τ < 1, via XOR combinations of data driven by the bit network.
  Shown as: Parameter choice and cost table *<predicate>* Fast address chunk interchange
- [Simultaneous butterfly layer](simultaneous-layer.md): Applying H₀ on the same bit position in up to d address chunks at once in O(Vd^{λ'}) time, λ' < 1, by recursing through the complex network and evaluating the layer exactly before one truncation.
  Shown as: Parameter choice and cost table *<predicate>* Simultaneous butterfly layer
- [Transform layout](transform-layout.md): A positional permutation of address bits placing the bits used in each transform round at a common offset in consecutive K-bit chunks, so simultaneous layers apply and the frequency order is retained.
  Shown as: Parameter choice and cost table *<predicate>* Transform layout
- [Tensor resampling interface](tensor-resampling.md): Applying the one-dimensional resampling maps line by line along each of d axes of a padded power-of-two box, with axis exposure done by chunk interchanges.
  Shown as: Parameter choice and cost table *<predicate>* Tensor resampling interface
- [Chinese-remainder address map](crt-address-map.md): The isomorphism x ↦ ∏ x_i^{μ_i} that turns one cyclic convolution of length S = ∏ s_i into a multidimensional cyclic convolution on distinct prime axes, implemented by triangular controlled shifts and axis moves.
  Shown as: Parameter choice and cost table *<predicate>* Chinese-remainder address map
- [Convolution from the retained transform layout](synthetic-convolution.md): Normalized convolution over the polynomial ring computed by two forward synthetic transforms, pointwise packed products in the stored order, and the opposite transform consuming that order.
  Shown as: Parameter choice and cost table *<predicate>* Convolution from the retained transform layout

## Pages that build on this one

- Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-alphabet multitape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{-182}, refuting the n log n lower-bound conjecture in this model.

## Other pages you may link to

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Normalized butterfly H₀](butterfly.md)
- [Gaussian dyadics and fixed-point truncation](gaussian-dyadics.md)
- [Linear bank-exchange network](linear-network.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Array streams and logical volume](stream-array-layout.md)
- [Frames and the common-frame identity](frame-invariant.md)
- [Address shear](address-shear.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Row splitting among roles](row-splitting.md)
- [Controlled shifts](controlled-shifts.md)
- [Restoration of arbitrary scratch values](scratch-restoration.md)
- [Three-element-subset gather and scatter](triple-gadget.md)
- [Nested subspace labels](subspace-labels.md)
- [Rank deficit of the network](rank-deficit.md)
- [Volume-normalized recurrence](volume-recurrence.md)
- [Rational matrix interface](bit-motif-interface.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Binary phase frames](phase-frames.md)
- [Binary phase interface](complex-motif-interface.md)
- [Packed selected-bit addition](packed-selected-bit.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed coefficient packing](signed-packing.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Coefficient phase twist](phase-twist.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Normalized discrete Fourier transform](dft.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transform](synthetic-fft.md)
- [Resampling with retained permutations](retained-permutations.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}." (paper)

  > Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform. Section~\ref{sec:assembly} removes the known normalizations and digit scales, proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product. A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}. Figure~\ref{fig:multiplication-flow} summarizes these reductions.

- "Thus $\min_i g_i=2^{-181}=2\kappa$." (paper)

  > The seven dominant powers in Table~\ref{tab:costs} have the following margins below one: \begin{equation}\label{eq:margin-list} \begin{split} g_1&=1-\epsilon(1+c),\qquad g_2=\epsilon c(1-\tau),\qquad g_3=\epsilon(1-\lambda'),\\ g_4&=1-\tau-\epsilon(2-\tau),\qquad g_5=1/4-\delta-3\epsilon/2,\\ g_6&=1-\delta-\epsilon,\qquad g_7=\epsilon. \end{split} \end{equation} Direct substitution gives \[ g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}. \] Thus $\min_i g_i=2^{-181}=2\kappa$. This explicit slack will cover any remaining fixed power of $\log p$.


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

Write the body to `exegenius/tasks/0043-write-cost-table.answer.md` and the JSON to `exegenius/tasks/0043-write-cost-table.answer.json`, then run `exegenius submit 0043-write-cost-table` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0043-write-cost-table`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
