# exegenius task 0039-write-cost-accounting

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
- Radix-digit convolution
- Discrete Fourier transform
- Fast Fourier transform with butterflies
- Fixed-point complex grid and truncation
- Contractions and error accounting
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
- Transform layout on tape
- Signed packing (Kronecker substitution)
- Normalized convolution over the polynomial ring
- Cyclic-to-negacyclic coefficient twist
- Bluestein chirp identity
- Gaussian resampling
- Retained permutation cancellation
- Chinese-remainder address map
- Source transform on the padded box
- Parameter regime for the multiplier
- Precision and exact recovery
- The multiplication algorithm
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

Concept: Cost accounting and the exponent κ
Gloss: Dividing every cost by V=Tp gives normalized costs that are at most p^(1−2κ), the smallest margin 2^−181 coming from the chunk-exchange term, giving total time O(n(log n)^(1−κ)).

## This page in the argument

The step: Dividing every cost by $V=Tp$ gives normalized costs at most $p^{1-2\kappa}$, so the total time is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ with $\kappa=2^{-182}$.
How: List the normalized cost of each operation as a power of $p$, take the seven dominant powers, and compare their margins below one with $2\kappa$.
Why: Each of the seven displayed powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the slack of $\kappa$ in the exponent absorbs the remaining logarithmic factors. (the sources say so: "Each of the seven displayed powers is at most $1-2\kappa$ by" (paper))

Its sub-steps, in order:

- The seven margins below one are $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$, so the smallest is $2^{-181}=2\kappa$.
- The first three rows of the table, from layout chunk exchanges, individual and simultaneous butterfly rounds, are the terms of the transform cost bound.
- Hence the complete large-input bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce the product to a convolution of radix digits evaluated by approximate Fourier transforms over a polynomial ring, make the transform's address movement and arithmetic cheaper with two new tape procedures, then show the result is exact and add up the cost. (on [Integer multiplication below n log n](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S14.1, S14.2, S14.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S14.1**: The seven margins below one are $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$, so the smallest is $2^{-181}=2\kappa$.
Source: "Thus $\min_i g_i=2^{-181}=2\kappa$." (paper)
> The seven dominant powers in Table~\ref{tab:costs} have the following margins below one: \begin{equation}\label{eq:margin-list} \begin{split} g_1&=1-\epsilon(1+c),\qquad g_2=\epsilon c(1-\tau),\qquad g_3=\epsilon(1-\lambda'),\\ g_4&=1-\tau-\epsilon(2-\tau),\qquad g_5=1/4-\delta-3\epsilon/2,\\ g_6&=1-\delta-\epsilon,\qquad g_7=\epsilon. \end{split} \end{equation} Direct substitution gives \[ g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}. \] Thus $\min_i g_i=2^{-181}=2\kappa$. This explicit slack will cover any remaining fixed power of $\log p$.

**S14.2**: The first three rows of the table, from layout chunk exchanges, individual and simultaneous butterfly rounds, are the terms of the transform cost bound.
Source: "The first three rows are the terms in" (paper)
> Here $d^2$ is absorbed by $d^2\ell^\tau$, and $\log(rp)=O(p^{1-\epsilon}+\log p)=O(p^{1-\epsilon})$. The first three rows are the terms in \eqref{eq:synthetic-transform-cost}. The prefix-slot moves and individual butterfly rounds in Lemma~\ref{lem:synthetic-transform-cost} use $O(dK)$ linear scans. Its positional layout uses $O(p/K)$ exchanges of width-$K$ chunks, because $d\ell=O(p)$. Each exchange costs $O(VK^\tau)$ by Lemma~\ref{lem:chunk-swap}, so the normalized total is \[ O(p/K)\,K^\tau=O(pK^{\tau-1}). \] For the at most $\ell$ simultaneous rounds, Proposition~\ref{prop:simultaneous-layer} supplies $O(Vd^{\lambda'})$ per round. Its bound already includes the binary basis changes, deterministic repair, row padding and removal, all base-$m$ groups, and fixed-tape cleanup.

**S14.3**: Hence the complete large-input bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.
Source: "O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})." (paper)
> Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Transform layout on tape](transform-tape-layout.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The multiplication algorithm](multiplication-algorithm.md): Digit conversion, the CRT map Φ, two forward source transforms, a pointwise product, one opposite transform, two scalings by S, rounding, inverse Φ and carry propagation to output the 2n-bit product.
  Shown as: Cost accounting and the exponent κ *<predicate>* The multiplication algorithm
- [Address chunk interchange](address-chunk-interchange.md): Interchanging two disjoint contiguous address fields of u bits of an array in O(V u^τ) time for a fixed τ<1, using XOR combinations of intermediate data although the final effect is an exact permutation.
  Shown as: Cost accounting and the exponent κ *<predicate>* Address chunk interchange
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): Applying H₀ to the same bit position in each of D≤d address chunks at once, on polynomial records of complex fixed-point coefficients, in O(V d^{λ'}) time with one final truncation.
  Shown as: Cost accounting and the exponent κ *<predicate>* Simultaneous butterfly layer
- [Parameter regime for the multiplier](parameter-regime.md): The choice of precision p=6b, dimension d≈p^ε, record length r=2^Θ(p^(1−ε)), power-of-two axis lengths t_i and distinct prime source lengths s_i just below them, so that Tp=Θ(n) and all hypotheses hold.
  Shown as: Cost accounting and the exponent κ *<predicate>* Parameter regime for the multiplier

## Pages that build on this one

- Integer multiplication below n log n: A deterministic multitape Turing machine multiplying two n-bit integers in O(n(lg n)^(1−κ)) time with κ=2^−182, disproving the n log n optimality conjecture in this model.

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
- [Synthetic polynomial transform](synthetic-polynomial-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Retained frequency order](stored-frequency-order.md)
- [Transform layout on tape](transform-tape-layout.md)
- [Contractions and error accounting](contraction-error-propagation.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](permutation-cancellation.md)
- [Normalized convolution over the polynomial ring](normalized-ring-convolution.md)
- [Radix-digit convolution](radix-digit-reduction.md)
- [Source transform on the padded box](tensor-source-transform.md)
- [Precision and exact recovery](precision-exact-recovery.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Thus $\min_i g_i=2^{-181}=2\kappa$." (paper)

  > The seven dominant powers in Table~\ref{tab:costs} have the following margins below one: \begin{equation}\label{eq:margin-list} \begin{split} g_1&=1-\epsilon(1+c),\qquad g_2=\epsilon c(1-\tau),\qquad g_3=\epsilon(1-\lambda'),\\ g_4&=1-\tau-\epsilon(2-\tau),\qquad g_5=1/4-\delta-3\epsilon/2,\\ g_6&=1-\delta-\epsilon,\qquad g_7=\epsilon. \end{split} \end{equation} Direct substitution gives \[ g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}. \] Thus $\min_i g_i=2^{-181}=2\kappa$. This explicit slack will cover any remaining fixed power of $\log p$.

- "Each of the seven displayed powers is at most $1-2\kappa$" (paper)

  > Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}


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

Write the body to `exegenius/tasks/0039-write-cost-accounting.answer.md` and the JSON to `exegenius/tasks/0039-write-cost-accounting.answer.json`, then run `exegenius submit 0039-write-cost-accounting` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0039-write-cost-accounting`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
