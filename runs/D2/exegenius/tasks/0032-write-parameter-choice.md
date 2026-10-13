# exegenius task 0032-write-parameter-choice

Project directory: `/home/user/openai-nlogn-wiki/runs/D2` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, basic algorithms (divide and conquer, sorting, recurrences, schoolbook integer arithmetic), discrete mathematics, and introductory linear algebra, abstract algebra (groups, rings, fields, modular arithmetic) and probability. They know Turing machines and tapes at a basic level, but not the multitape fixed-alphabet cost model in detail, nor Fourier-analytic multiplication, FFT variants, or specialist algebra such as bilinear forms over F_2 and matrix factorizations like Bruhat.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Roots of unity
- Schönhage–Strassen n log n conjecture and history
- Fixed-tape machine model and cost of scans
- Elementary stream operations and controlled shifts
- Discrete Fourier transform (also: Fourier transform)
  - $F_q$ (transform): The normalized Fourier transform acting on vectors of length q.
  - $q$ (transform length): The number of coordinates of the vector being transformed.
- Cyclic convolution
- Two-point butterfly H₀
  - $H_0$ (butterfly map): The map sending a pair (u,v) to ((u+v)/2,(u-v)/2).
- Multiplication as convolution of radix digits
- Established O(n log n) multiplier as a subroutine
- Fixed-point grids, contractions and error
- Polynomial ring modulo y^r + 1
  - $\mathcal R_r$ (ring): The ring of complex polynomials in y of degree below r with y^r identified with -1.
  - $r$ (record length): The number of complex coefficients in a polynomial record; a power of two.
  - $y$ (ring variable): The polynomial variable, whose powers act as roots of unity.
- Synthetic polynomial transform
  - $F_t^{\pm}$ (synthetic transform): The forward (+) or opposite (−) sign transform of length t over the ring.
  - $t$ (transform length): The number of ring entries along an axis; a power of two dividing 2r.
  - $\mathcal R_r$ (ring): The polynomial ring modulo y^r+1.
  - $r$ (record length): The number of complex coefficients in a record.
- Chirp identity and permutation cancellation (also: Bluestein)
- Gaussian resampling
- Resampling with the permutations left in the transform
- Chinese-remainder address map to prime cyclic axes
- Coefficient twist to the negacyclic ring
- Signed packing of polynomial records
- Linear network with roles, frames and restored scratch
- Restoring scratch values (transparent computation)
- Three-element subsets and nested subspace labels
- Total smaller calls below W m
  - $s$ (total smaller calls): The number of smaller calls summed over all network edges.
  - $W$ (number of roles): The number of wire roles among which rows are distributed.
  - $m$ (network dimension): The dimension of the label space, equal to the factor by which the parameter grows per recursion level.
- Lower-triangular factorization and address shear
- Fast interchange of address chunks
  - $V$ (bit volume): The number of stored bits in the array.
  - $u$ (chunk width): The number of address bits (digits) in each interchanged chunk.
  - $\tau$ (saving exponent): A fixed exponent strictly below 1 in the cost bound.
- Phase kernel C and complex network
- Packed selected-bit addition
- Simultaneous butterfly layer
  - $V$ (bit volume): The number of stored bits in the logical array.
  - $d$ (selected axes): The number of address chunks whose selected bit gets a butterfly simultaneously.
  - $\lambda'$ (layer exponent): A fixed exponent strictly below 1 in the layer cost.
- Convolution from the retained transform layout
- Precision, rounding and carries
- Matrices and linear maps (also: linear algebra, matrix multiplication, invertible matrix, lower triangular matrix, linear transformation, basis)
- Modular arithmetic (also: congruences, residues, Z/nZ, integers modulo n)
- Chinese remainder theorem (also: CRT, Chinese remainder)
- Prime numbers and coprimality (also: primes, gcd, coprime, relatively prime, prime number theorem)
- Groups, rings and fields (also: abstract algebra, ring, finite field, F_2, GF(2), cyclic group, group homomorphism, direct product)
- Binary representation and bit operations (also: bits, XOR, binary expansion, two's complement, radix representation, base-b digits)
- Schoolbook and divide-and-conquer multiplication (also: Karatsuba, long multiplication, grade-school multiplication, quadratic multiplication)
- Fast Fourier transform (also: FFT, Cooley-Tukey, radix-2 FFT)
- Floor, ceiling, logarithms and exponents (also: lg, log base 2, floor function, ceiling function, iterated logarithm)
- Recurrences and amortized cost accounting (also: recurrence relation, master theorem, summing cost over levels, geometric series)
- Sorting and permutations (also: permutation, comparison sort, merge sort, bit-reversal permutation)
- Norms and inequalities (also: max norm, triangle inequality, sup norm, absolute value bound, Euclidean norm)
- Rounding and floating or fixed point error (also: truncation error, round to nearest integer, fixed-point arithmetic, approximation error)
- Gaussian integers and dyadic rationals (also: Z[i], dyadic numbers, Gaussian dyadic)
- Multidimensional arrays and product index sets (also: tensor indexing, array of dimension d, product of cyclic groups)
- Sums and product notation, Euler's formula (also: summation, e^{i theta}, Euler formula, complex exponential)
- Graphs and networks (also: directed graph, vertices and edges, circuit, gates, bipartite graph)
- Subsets and counting (also: binomial coefficient, indicator vector, inclusion-exclusion, 3-subsets, combinatorics)
- Basic probability and combinatorial bounds (also: union bound, pigeonhole principle, counting argument)

## This page

Concept: Parameter choice and cost table
Gloss: With b=⌈log₂n⌉, p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log₂T/d⌉}, every term of the normalized cost table is p^{1−margin}, so the total is O(Tp·p^{1−g}) = O(n (lg n)^{1−κ}).

## This page in the argument

The step: With $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $K=\lfloor d^c\rfloor$, every term of the normalized cost table is at most $p^{1-2\kappa}$, so the total is $O(n(\lg n)^{1-\kappa})$.
How: choose compatible parameters and bound each cost-table row
Why: Each procedure saves only a small power, so the parameters must balance all rows of the cost table to leave a positive margin. (the sources leave this for the reader to work out: spell it out)
Striking feature: All seven dominant powers of p in the cost table have a positive margin below one, and the smallest margin is 2^-181 = 2 kappa. (explain why it holds, from the method)

Its sub-steps, in order:

- The total cost is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.; how: reduce integer multiplication to a Fourier convolution evaluated with two fast tape procedures, then bound error and cost (on [Integer multiplication in O(n (lg n)^{1−κ})](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S7.1). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S7.1**: The total cost is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.
Source: "O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})." (paper)
> Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Convolution from the retained transform layout](synthetic-convolution.md): Convolution over R_r on a multi-axis array: two forward synthetic transforms keep the same frequency order, multiply pointwise by signed packing, and the opposite transform consumes that order, using layers on a layout built from chunk swaps.
  Shown as: Parameter choice and cost table *<predicate>* Convolution from the retained transform layout
- [Resampling with the permutations left in the transform](retained-permutations.md): Instead of sorting twice per coordinate, the source and target coordinate permutations stay inside the transform identity and cancel, so no separate full sorts are executed.
  Shown as: Parameter choice and cost table *<predicate>* Resampling with the permutations left in the transform
- [Chinese-remainder address map to prime cyclic axes](crt-prime-axes.md): A convolution-preserving map Φ places the radix-digit list on a product of distinct prime cyclic axes, implemented by triangular controlled shifts and axis moves.
  Shown as: Parameter choice and cost table *<predicate>* Chinese-remainder address map to prime cyclic axes
- [Coefficient twist to the negacyclic ring](coefficient-twist.md): Scaling coefficient k by ζ^k with ζ=e^{πi/r} maps cyclic convolution in the last coordinate to polynomial multiplication modulo y^r+1, with the negative wrap undoing to the cyclic wrap.
  Shown as: Parameter choice and cost table *<predicate>* Coefficient twist to the negacyclic ring

## Pages that build on this one

- The multiplication algorithm pipeline: Digits, Φ to prime axes, two source transforms via Gaussian resampling and chirp convolution, pointwise product, opposite transform, scale, round, Φ⁻¹, carry.

## Other pages you may link to

- [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md)
- [Established O(n log n) multiplier as a subroutine](harvey-hoeven-multiplier.md)
- [Fixed-tape machine model and cost of scans](fixed-tape-model.md)
- [Elementary stream operations and controlled shifts](elementary-streams.md)
- [Linear network with roles, frames and restored scratch](linear-network.md)
- [Restoring scratch values (transparent computation)](transparent-restoration.md)
- [Three-element subsets and nested subspace labels](triple-subspace-labels.md)
- [Total smaller calls below W m](rank-saving.md)
- [Lower-triangular factorization and address shear](bruhat-shear.md)
- [Fast interchange of address chunks](chunk-interchange.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Polynomial ring modulo y^r + 1](ring-y-r-plus-1.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly H₀](butterfly.md)
- [Phase kernel C and complex network](phase-frames.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as convolution of radix digits](radix-digit-convolution.md)
- [Chirp identity and permutation cancellation](bluestein-chirp.md)
- [Fixed-point grids, contractions and error](fixed-point-contraction.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Precision, rounding and carries](exact-recovery.md)
- [Signed packing of polynomial records](signed-packing.md)
- [The multiplication algorithm pipeline](multiplication-algorithm.md)
- [Integer multiplication in O(n (lg n)^{1−κ})](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The seven dominant powers in Table~\ref{tab:costs} have the following" (paper)

  > The seven dominant powers in Table~\ref{tab:costs} have the following margins below one: \begin{equation}\label{eq:margin-list} \begin{split} g_1&=1-\epsilon(1+c),\qquad g_2=\epsilon c(1-\tau),\qquad g_3=\epsilon(1-\lambda'),\\ g_4&=1-\tau-\epsilon(2-\tau),\qquad g_5=1/4-\delta-3\epsilon/2,\\ g_6&=1-\delta-\epsilon,\qquad g_7=\epsilon. \end{split} \end{equation} Direct substitution gives \[ g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}. \] Thus $\min_i g_i=2^{-181}=2\kappa$. This explicit slack will cover any remaining fixed power of $\log p$.

- "\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16}" (paper)

  > The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.


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

Write the body to `exegenius/tasks/0032-write-parameter-choice.answer.md` and the JSON to `exegenius/tasks/0032-write-parameter-choice.answer.json`, then run `exegenius submit 0032-write-parameter-choice` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0032-write-parameter-choice`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
