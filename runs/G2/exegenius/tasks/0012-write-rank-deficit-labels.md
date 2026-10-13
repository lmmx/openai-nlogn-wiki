# exegenius task 0012-write-rank-deficit-labels

Project directory: `/home/user/openai-nlogn-wiki/runs/G2` (paths below are relative to it)

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

For these sources: Undergraduate computer science: algorithms and complexity through big-O analysis, recurrences and divide-and-conquer (Karatsuba, FFT-based polynomial multiplication, usually met at the level of the standard recursive FFT), discrete mathematics (modular arithmetic, primes and gcd, sets, functions and permutations, induction), and introductory linear algebra (matrices, rank, bases, inner products, Gaussian elimination, over the reals and probably F_2). Also the basics of complex numbers and Turing machines with multiple tapes. The reader has not studied abstract algebra such as quotient rings or tensor products, finite-field theory beyond F_2, numerical analysis of rounding errors, or the research literature on integer multiplication (Schönhage–Strassen, Fürer, Harvey–van der Hoeven), and has not seen Bluestein, Nussbaumer polynomial transforms or Gaussian resampling.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Bit XOR
- The n log n conjecture and prior bounds (also: Schönhage–Strassen conjecture)
- Arrays as tape streams and elementary scans
- Controlled shifts and rational scalings
- Fixed-point and Gaussian dyadic arithmetic
- Subspaces, bilinear forms and orthogonal complements
- Linear network with restored scratch wires (also: motif network, restoration schedule)
- Triple-subset intersection gadgets
- Frames on wire arrays
- Asymptotic notation beyond big-O (also: Omega notation, Theta notation, little-o, Ω, Θ, o(n log n))
- Logarithms and binary logarithm (also: lg, log base 2, log_2, ceiling of log)
- Floor and ceiling functions (also: floor, ceiling, ⌊x⌋, ⌈x⌉, integer part)
- Binary representation of integers (also: n-bit integer, bit string, binary expansion, two's complement, signed binary)
- Radix representation and digits (also: base-b expansion, positional notation, radix digits, leading zeroes)
- Schoolbook multiplication and carries (also: grade-school multiplication, long multiplication, quadratic multiplication, carry propagation, addition with carry)
- Divide-and-conquer and recurrences (also: recurrence relation, master theorem, Karatsuba multiplication, recursion, geometric series, geometric sum)
- Fast Fourier transform and FFT multiplication (also: FFT, Cooley-Tukey, radix-2 FFT, O(n log n) polynomial multiplication, evaluation and interpolation)
- Mathematical induction and proof by cases (also: induction, inductive proof, proof by contradiction)
- Sets, subsets and Cartesian products (also: set intersection, cardinality, subset of size three, product set, tuples, indicator vector)
- Functions, bijections and permutations (also: permutation, bijection, inverse function, composition, involution, partial permutation)
- Modular arithmetic and congruences (also: mod, residues, congruence, ℤ/nℤ, integers modulo n, remainder, units modulo n)
- Primes, divisibility and coprimality (also: gcd, greatest common divisor, relatively prime, prime power, coprime, trial division, prime factorization)
- Rational numbers and exact fractions (also: rationals, ℚ, denominator, numerator, dyadic rational)
- Finite fields and the field F_2 (also: GF(2), 𝔽_2, binary field, arithmetic modulo 2, parity)
- Vectors, matrices and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, identity matrix, linear transformation, diagonal matrix, linear combination)
- Rank, basis and dimension (also: linear independence, span, vector space, subspace dimension, rank of a matrix, rank-nullity)
- Gaussian elimination (also: row reduction, row operations, elementary matrices, triangular matrix, lower triangular, upper triangular)
- Inner product, norm and orthonormal basis (also: dot product, orthogonal vectors, orthonormal, unit vector, vector norm, max norm, sup norm, l-infinity norm, unit disk, absolute value of complex number, modulus)
- Roots of unity and Euler's formula (also: e^{iθ}, primitive root of unity, n-th roots of unity, unit circle, geometric series of roots)
- Summation and product notation (also: sigma notation, Σ, Π, indices, Kronecker delta)
- Newton's method (also: Newton iteration, Newton-Raphson, reciprocal by Newton, square root by Newton, quadratic convergence)
- Integer division with remainder (also: quotient and remainder, floor division, integer square root, division algorithm)
- Lexicographic order (also: dictionary order, row-major order, most significant first, mixed radix address)
- Arrays, records and matrix transposition (also: row-major, column-major, transpose, matrix layout, indexing)
- Turing machine running time and model conventions (also: worst-case time, time complexity, unit-cost RAM, random access machine, input and output tapes, finite alphabet, tape heads, scanning and sorting on tapes, linear-time scan, simulation)

## This page

Concept: Nested subspace labels and the rank deficit
Gloss: Subspaces attached to gates and terminals so that adjacent labels are nested and the total rank s of all edge changes is strictly below the wire count times dimension, s < Wm.
Also called: s<Wm

## This page in the argument

The step: The bit network can be given nested nondegenerate subspace labels on its gates and terminals such that the endpoint matrices of every route differ by the identity $I_m$ and the total rank of all edge differences is $s<W m$.
How: Label each wire's data by tensor products of the indicator lines of the three triples and their orthogonal complements; tabulate the orthogonal residual of every edge; observe that only the central wires lose dimension; and read off the rank sum, in which the source projections contribute $N$ extra ranks.
Why: The labels are chosen so that each change of frame costs only as much as the dimension of its orthogonal residual. (the sources say so: "choose its intermediate labels to make the changes of frame inexpensive." (paper))
Striking feature: Dimension never decreases on any edge except the central-wire edges from time 3 to time 4, and their total loss is less than half of $N$, which is exactly what pushes the rank sum strictly below $W m$. (explain why it holds, from the method)

Its sub-steps, in order:

- Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$, so the sum of absolute dimension changes is $W m-2N+2L$ with $L<N/2$.
- With the projections $P_U$ as matrices and a negated projection at each source $X_a$, the endpoint difference is $I_m$ on every route and the sum of the rational ranks of all edge differences is $s<W m$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a convolution over a polynomial ring computed by Fourier-type transforms; supply the two fast tape procedures that remove the logarithmic factor from address movement and from butterfly arithmetic, both obtained from linear networks that save a power; then assemble the algorithm and tally every cost. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- There are two fixed linear networks of $W$ wires, one over bits and one over Gaussian dyadic numbers, each exchanging two banks of values with a sign while restoring every scratch wire, whose frames can be chosen so that the edge changes have total rank $s<W m$.; how: Construct the scalar exchange network, lift it to arrays with frames, then attach nested subspace labels to its gates and terminals and count the dimension changes, once for bits and once for phases.

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.3.1, S1.3.2). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.3.1**: Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$, so the sum of absolute dimension changes is $W m-2N+2L$ with $L<N/2$.
Source: "Every edge joins comparable nondegenerate labels.  The only decreasing" (paper)
> \begin{lemma}\label{lem:motif-residuals} Every edge joins comparable nondegenerate labels. The only decreasing edges are the central-wire edges from time 3 to time 4; their dimension loss is $h$. Consequently, if $c$ is the number of central wires per invocation and $W$ the total number of wires, then \begin{equation} L=Ich,\qquad \sum_{e}\bigl|\dim U_{\mathrm{head}(e)}- \dim U_{\mathrm{tail}(e)}\bigr| =Wm-2N+2L. \label{eq:rank-budget-labels} \end{equation} For the binary label space, every nonzero orthogonal residual of an edge has an orthonormal basis. \end{lemma}

**S1.3.2**: With the projections $P_U$ as matrices and a negated projection at each source $X_a$, the endpoint difference is $I_m$ on every route and the sum of the rational ranks of all edge differences is $s<W m$.
Source: "The sum of the rational ranks of all edge differences is" (paper)
> \begin{proposition}\label{prop:bit-motif-interface} The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates, and sends its input vector to the permutation $\rho$ of that vector. Its rational matrices are common to all incidences of a gate and obey \[ M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m \quad\text{for every input role }w. \] The sum of the rational ranks of all edge differences is \begin{align} s_{\rm b} &=\sum_{e}\operatorname{rank}_{\mathbb Q} (M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)})\\ &=W_{\rm b}m-N+2L_{\rm b} =177176569088785861287000000<W_{\rm b}m. \end{align} \end{proposition}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Triple-subset intersection gadgets](triple-subset-gadgets.md): Gather, scatter and side-injection gates indexed by three-element subsets of a 100-element set, whose coefficients depend on intersection size and whose side wires cancel the unwanted terms.
  Shown as: Nested subspace labels and the rank deficit *<predicate>* Triple-subset intersection gadgets
- [Frames on wire arrays](frames.md): Invertible linear operators D_v on each wire's address-indexed array so that stored array = D_v applied to the logical array, commuting with pointwise gates so only edge changes D_v D_u^{-1} cost anything.
  Shown as: Nested subspace labels and the rank deficit *<predicate>* Frames on wire arrays
- [Subspaces, bilinear forms and orthogonal complements](linear-algebra-orthogonality.md): A subspace of a vector space with a nondegenerate bilinear form, its orthogonal complement, the projection onto it, and the dimension (rank) of the difference of two nested subspaces.
  Shown as: Nested subspace labels and the rank deficit *<predicate>* Subspaces, bilinear forms and orthogonal complements

## Pages that build on this one

- Recursive power saving from the rank deficit: A call at parameter m·f uses s calls at parameter f on streams of volume V/W, so cost per volume grows like m^τ rather than m, with τ<1 because s/W<m.
- Binary phase frames and the two-point kernel C: Frames C_U=H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} over Gaussian dyadics, whose edge changes are products of translation kernels aI+bX, composing to C^{⊗m} on every role.

## Other pages you may link to

- [The n log n conjecture and prior bounds](nlogn-conjecture.md)
- [Linear network with restored scratch wires](linear-network.md)
- [Arrays as tape streams and elementary scans](tape-streams.md)
- [Fixed-point and Gaussian dyadic arithmetic](fixed-point-dyadics.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Recursive power saving from the rank deficit](recursive-power-saving.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Matrix shear on address fields](matrix-shear.md)
- [Fast interchange of address chunks](fast-chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](ring-mod-y-r-plus-1.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly layer](two-point-butterfly.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Multiplication as convolution of radix digits](multiplication-as-convolution.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Error bounds and exact recovery](error-and-exact-recovery.md)
- [Last-coordinate phase twist](phase-twist.md)
- [The established O(N log N) multiplier](nlogn-multiplier.md)
- [Binary phase frames and the two-point kernel C](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Synthetic transform tape layout](synthetic-transform-layout.md)
- [Signed packing for ring products](kronecker-packing.md)
- [Normalized convolution over the ring](synthetic-convolution.md)
- [Resampling with permutations left in the transform](resampling-without-sorting.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Parameter choice and cost table](parameter-choice.md)
- [Chinese-remainder address map](crt-address-map.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The decisive property is that the total
number $s$ of smaller calls satisfies $s<Wm$." (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.

- "The only decreasing
edges are the central-wire edges from time 3 to time 4" (paper)

  > \begin{lemma}\label{lem:motif-residuals} Every edge joins comparable nondegenerate labels. The only decreasing edges are the central-wire edges from time 3 to time 4; their dimension loss is $h$. Consequently, if $c$ is the number of central wires per invocation and $W$ the total number of wires, then \begin{equation} L=Ich,\qquad \sum_{e}\bigl|\dim U_{\mathrm{head}(e)}- \dim U_{\mathrm{tail}(e)}\bigr| =Wm-2N+2L. \label{eq:rank-budget-labels} \end{equation} For the binary label space, every nonzero orthogonal residual of an edge has an orthonormal basis. \end{lemma}


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

Write the body to `exegenius/tasks/0012-write-rank-deficit-labels.answer.md` and the JSON to `exegenius/tasks/0012-write-rank-deficit-labels.answer.json`, then run `exegenius submit 0012-write-rank-deficit-labels` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0012-write-rank-deficit-labels`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
