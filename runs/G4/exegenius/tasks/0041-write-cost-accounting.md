# exegenius task 0041-write-cost-accounting

Project directory: `/home/user/openai-nlogn-wiki/runs/G4` (paths below are relative to it)

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

For these sources: The reader has done an undergraduate computer science degree: discrete mathematics (modular arithmetic, primes and gcd, sets, induction, recurrences and asymptotics), basic linear algebra over the reals and complex numbers (matrices, inverses, norms), polynomials and complex roots of unity, and algorithms including divide and conquer and Karatsuba multiplication. On the machine side they know basic single- and multi-tape Turing machines and the idea of counting steps. They have not studied the Fourier transform, FFT-based multiplication, Schonhage-Strassen, Harvey-van der Hoeven, numerical error analysis, abstract algebra beyond rings of residues, finite-field linear algebra, or any lower-bound or advanced tape-algorithm technique, so those must be explained.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape Turing machine model
- Elementary stream operations on tape arrays
- Controlled shifts and rational scalings
- Convolution
- Integer multiplication as digit convolution
- Discrete Fourier transform
- Radix-2 butterflies and FFT
- Subspaces, rank and orthogonal complements
- Fixed-point disk arithmetic and truncation error
- Established O(n log n) integer multiplier
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The polynomial variable, which satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Signed packing of polynomial products
- Two-point kernel C and phase frames
- Frames on pointwise linear networks
- Subset-intersection exchange network
- Subspace labels and the rank budget
- Recursive power saving from a rank deficit
- Bit network shear interface
- Lower triangular (Bruhat-type) factorization
- Cost of a rational matrix shear
- Power-width address interchange
- Fast chunk interchange
- Complex phase network
- Packed selected-bit addition
- Simultaneous butterfly layer
- Synthetic transform layout and cost
- Convolution from the retained transform layout
- Coefficient twist to the negacyclic ring
- Gaussian resampling
- Multidimensional resampling on a padded box
- Bluestein chirp identity
- Source permutation cancellation
- Chinese-remainder axis map
- Parameter choices
- Exact recovery of the integer product
- The multiplication algorithm
- Modular arithmetic and residue rings (also: congruence, Z/qZ, integers mod q, residue classes, modular inverse)
- Primes, coprimality and the Euclidean algorithm (also: gcd, greatest common divisor, relatively prime, extended Euclidean algorithm, coprime)
- Positional (radix) number representation (also: base-b expansion, binary representation, digits, binary integers, mixed radix)
- Signed binary numbers and rounding (also: two's complement, sign-magnitude, floor, ceiling, rounding to nearest integer, truncation toward zero)
- Dyadic rationals (also: binary fractions, fractions with power-of-two denominator, fixed-point binary fractions)
- Bitwise operations and Hamming weight (also: XOR, exclusive or, bit string, popcount, Hamming weight, parity)
- Permutations and bijections (also: permutation of indices, bijection, inverse permutation, bit-reversal permutation, transposition)
- Lexicographic order and multi-index addressing (also: row-major order, dictionary order, multidimensional array indexing, mixed-radix address, tuple indices)
- Matrix algebra (also: matrix multiplication, matrix inverse, identity matrix, transpose, invertible matrix, 2x2 matrices, diagonal matrix, matrix-vector product)
- Vector norms and the triangle inequality (also: sup norm, max norm, infinity norm, absolute value bound, modulus bound, triangle inequality)
- Logarithms, exponentials and floor/ceiling in analysis (also: log base 2, lg, powers of two, exponent laws, iterated logarithm, real exponent)
- Theta, Omega and little-o notation (also: big-Theta, big-Omega, little-o, liminf, asymptotic lower bound, tight bound)
- Summations and geometric series (also: geometric sum, telescoping sum, sum of powers, series bound)
- Recurrence relations and divide and conquer (also: recurrence, unrolling a recurrence, master theorem, recursion tree, recursive algorithm, divide-and-conquer)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba, quadratic multiplication)
- Stacks and call stacks (also: stack, recursion stack, call stack, program counter, subroutine call)
- Pointwise operations on lists and vectors (also: componentwise product, Hadamard product, elementwise map, coordinatewise operation)
- Sets, subsets and counting (also: subset, cardinality, intersection, binomial coefficient, ground set, indicator vector, power set)
- Mathematical induction and proof by contradiction (also: induction, inductive proof, contradiction, proof techniques)
- Euler's formula and complex exponentials (also: e^{i theta}, Euler formula, unit circle, phase factor, twiddle factor, modulus of e^{i theta})

## This page

Concept: Complete time bound
Gloss: Summing the normalized costs of layouts, butterfly rounds, resampling, chirps and packed products, each at most p^{1−2κ}, to get O(n (log n)^{1−κ}).

## This page in the argument

The step: Summing the normalized costs of layouts, butterfly rounds, resampling, chirps and packed products, each at most $p^{1-2\kappa}$ per unit of volume $Tp$, gives the total time $O(n(\log n)^{1-\kappa})$.
How: Tabulate each operation's cost divided by $V=Tp$ as a power of $p$, bound the setup and exceptional streams, check that all seven dominant powers have margin at least $2\kappa$ below one, and absorb fixed powers of $\log p$.
Why: Every ingredient costs $O(V)$ times a power of $p$ that is strictly less than 1, and the largest power determines the total. (the sources leave this for the reader to work out: spell it out)
Striking feature: The exponent $\kappa$ is exactly half the smallest of the seven margins, $2^{-181}$, which comes from the chunk-exchange row $\epsilon c(1-\tau)$; this slack absorbs any remaining fixed power of $\log p$. (explain why it holds, from the method)

Its sub-steps, in order:

- The seven dominant margins $g_i$ below one have minimum $2^{-181}=2\kappa$.
- The first three rows of the cost table are the three terms of the synthetic transform cost.
- Axis exposure and restoration require $O(d^2)$ adjacent axis moves, each costing $O(V(1+\ell^\tau))$.
- The Gaussian line machines sum to $O(dTp^{3/2+\delta}\alpha)$.
- Chirp numerators and the scalar products cost $O(dp^{1+\delta})$ per entry, and the packed polynomial products cost $O(Tp\log(rp))$.
- Global setup and prime search cost $o(V)$, and setup per record or line is $o(Tp)$ since $r$ exceeds every fixed power of $p$.
- Each of the seven powers is at most $1-2\kappa$ and fixed powers of $\log p$ are at most $p^\kappa$, giving the bound $O(n(\log n)^{1-\kappa})$; schoolbook multiplication handles lengths below a cutoff.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in that model.; how: Reduce the product to a cyclic convolution of radix digits evaluated by Fourier-type transforms, make the two costly ingredients of those transforms (address rearrangement and butterfly arithmetic) cost a power of the logarithm less than a full scan per level by two rank-saving tape procedures, then assemble the algorithm, prove exactness and total the cost. (on [Sub-n log n integer multiplication](sub-nlogn-multiplication.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S8.1, S8.2, S8.3, S8.4, S8.5, S8.6, S8.7). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S8.1**: The seven dominant margins $g_i$ below one have minimum $2^{-181}=2\kappa$.
Source: "Thus $\min_i g_i=2^{-181}=2\kappa$." (paper)
> The seven dominant powers in Table~\ref{tab:costs} have the following margins below one: \begin{equation}\label{eq:margin-list} \begin{split} g_1&=1-\epsilon(1+c),\qquad g_2=\epsilon c(1-\tau),\qquad g_3=\epsilon(1-\lambda'),\\ g_4&=1-\tau-\epsilon(2-\tau),\qquad g_5=1/4-\delta-3\epsilon/2,\\ g_6&=1-\delta-\epsilon,\qquad g_7=\epsilon. \end{split} \end{equation} Direct substitution gives \[ g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}. \] Thus $\min_i g_i=2^{-181}=2\kappa$. This explicit slack will cover any remaining fixed power of $\log p$.

**S8.2**: The first three rows of the cost table are the three terms of the synthetic transform cost.
Source: "The first three rows are the terms in" (paper)
> Here $d^2$ is absorbed by $d^2\ell^\tau$, and $\log(rp)=O(p^{1-\epsilon}+\log p)=O(p^{1-\epsilon})$. The first three rows are the terms in \eqref{eq:synthetic-transform-cost}. The prefix-slot moves and individual butterfly rounds in Lemma~\ref{lem:synthetic-transform-cost} use $O(dK)$ linear scans. Its positional layout uses $O(p/K)$ exchanges of width-$K$ chunks, because $d\ell=O(p)$. Each exchange costs $O(VK^\tau)$ by Lemma~\ref{lem:chunk-swap}, so the normalized total is \[ O(p/K)\,K^\tau=O(pK^{\tau-1}). \] For the at most $\ell$ simultaneous rounds, Proposition~\ref{prop:simultaneous-layer} supplies $O(Vd^{\lambda'})$ per round. Its bound already includes the binary basis changes, deterministic repair, row padding and removal, all base-$m$ groups, and fixed-tape cleanup.

**S8.3**: Axis exposure and restoration require $O(d^2)$ adjacent axis moves, each costing $O(V(1+\ell^\tau))$.
Source: "Axis exposure and restoration require $O(d^2)$ adjacent axis moves." (paper)
> Axis exposure and restoration require $O(d^2)$ adjacent axis moves. Each costs $O(V(1+\ell^\tau))$: peel a single excess bit when widths differ by one, exchange their equal-width parts, and restore the bit. The $d$ CRT rotations copy valid and invalid intervals in $O(dV)$ time. Their offset setup was bounded above by $O(dTp^C/r)=o(Tp)$, using at most $T/t_i$ control prefixes for target $i$.

**S8.4**: The Gaussian line machines sum to $O(dTp^{3/2+\delta}\alpha)$.
Source: "For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines." (paper)
> For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines. The line-machine costs therefore sum to \[ \sum_{i=1}^d\frac{T}{t_i} O(t_i p^{3/2+\delta}\alpha) =O(dTp^{3/2+\delta}\alpha). \] Dividing by $V=Tp$ gives the fifth row. The factor $\alpha=\Theta(p^{1/4+\epsilon/2})$ explains its displayed power of $p$.

**S8.5**: Chirp numerators and the scalar products cost $O(dp^{1+\delta})$ per entry, and the packed polynomial products cost $O(Tp\log(rp))$.
Source: "Chirp numerators have $O(p)$ bits and can be computed modulo $2r$ as" (paper)
> Chirp numerators have $O(p)$ bits and can be computed modulo $2r$ as sums of $d$ terms $s_i j_i^2(r/t_i)$. Computing their squares and products with the previously established $O(N\log(2N))$ multiplier on $N$-bit inputs, then generating the exponentials, costs $O(dp^{1+\delta})$ per entry. The smaller twist and scalar pointwise-product costs fit the same row: they use a fixed number of exact products on $O(p)$-bit component numerators, followed by linear truncation scans. The two final products by $S$ also cost $O(p\log p)$ per entry, so their normalized cost is $O(\log p)=O(p^\delta)$ as listed separately. There are $T/r$ polynomial records in each pointwise ring product. Four integer products on $O(rp)$ bits per record therefore cost $O(Tp\log(rp))$ in total. Signed packing, centered extraction, negacyclic wrapping, and copying are linear stream passes. These calls use the previously established multiplier on records of length $O(rp)=o(n)$; they do not call the improved algorithm being constructed. The exact source scaling by $2^\gamma$ is a shift of $O(p)$-bit numerators by $\gamma=O(p)$ places, so it is a linear scan per entry and fits the final-scaling row. The scalar-format adapters and the exact removal of sign-extension bits after the ring and source scales also use linear scans of their $O(p)$-bit components, within the listed scan costs.

**S8.6**: Global setup and prime search cost $o(V)$, and setup per record or line is $o(Tp)$ since $r$ exceeds every fixed power of $p$.
Source: "Global setup and prime search cost $o(V)$, as" (paper)
> Finally, all role, arithmetic, and stack tapes form fixed finite families. A child parks and restores only its parent's streams, with the stack head at the active top; copying and cleanup are charged to that logical volume. No operation repeatedly scans parked ancestors. Growing axis lists and call states are stored data, not extra tapes or alphabet symbols. Global setup and prime search cost $o(V)$, as proved earlier.

**S8.7**: Each of the seven powers is at most $1-2\kappa$ and fixed powers of $\log p$ are at most $p^\kappa$, giving the bound $O(n(\log n)^{1-\kappa})$; schoolbook multiplication handles lengths below a cutoff.
Source: "The complete large-input bound is consequently" (paper)
> Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The multiplication algorithm](multiplication-algorithm.md): Digit polynomials are mapped by the CRT map to prime axes, transformed by resampling plus chirp-convolution (via the twist and synthetic convolution), multiplied pointwise, inverse transformed, rescaled, rounded and carried.
  Shown as: Complete time bound *<predicate>* The multiplication algorithm
- [Fast chunk interchange](chunk-interchange.md): Exchanging two equal-width address fields of u bits in an arbitrary array in O(V u^τ) time for a fixed τ < 1, even though intermediate steps XOR data together.
  Shown as: Complete time bound *<predicate>* Fast chunk interchange
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): Applying H_0 to the same bit position in up to d address chunks at once, exactly in dyadic arithmetic and truncating once, in O(V d^λ') time for λ' < 1.
  Shown as: Complete time bound *<predicate>* Simultaneous butterfly layer
- [Convolution from the retained transform layout](synthetic-convolution.md): Normalized convolution over the polynomial ring by two forward synthetic transforms, pointwise ring products via signed packing, and the opposite transform consuming the same stored order.
  Shown as: Complete time bound *<predicate>* Convolution from the retained transform layout
- [Multidimensional resampling on a padded box](tensor-resampling.md): Applying the one-dimensional resampling maps along each axis of the padded power-of-two box, exposing each axis by chunk interchanges, with permutations left inside the transform.
  Shown as: Complete time bound *<predicate>* Multidimensional resampling on a padded box

## Pages that build on this one

- Sub-n log n integer multiplication: A deterministic multitape Turing machine multiplies two n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in that model.

## Other pages you may link to

- [Convolution](convolution.md)
- [Recursive power saving from a rank deficit](recursive-power-saving.md)
- [Fixed-tape Turing machine model](fixed-tape-model.md)
- [Established O(n log n) integer multiplier](nlogn-multiplier.md)
- [Elementary stream operations on tape arrays](elementary-stream-ops.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Subspaces, rank and orthogonal complements](linear-subspaces.md)
- [Frames on pointwise linear networks](frames-on-arrays.md)
- [Subset-intersection exchange network](exchange-network.md)
- [Subspace labels and the rank budget](subspace-labels.md)
- [Bit network shear interface](bit-network-interface.md)
- [Lower triangular (Bruhat-type) factorization](triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Power-width address interchange](power-width-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](synthetic-ring.md)
- [Fixed-point disk arithmetic and truncation error](fixed-point-precision.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Discrete Fourier transform](dft.md)
- [Radix-2 butterflies and FFT](fft-butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Two-point kernel C and phase frames](phase-kernel-c.md)
- [Complex phase network](complex-phase-network.md)
- [Synthetic transform layout and cost](synthetic-transform-layout.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Source permutation cancellation](permutation-cancellation.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Exact recovery of the integer product](exact-recovery.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Parameter choices](parameter-choices.md)
- [Coefficient twist to the negacyclic ring](convolution-twist.md)
- [Sub-n log n integer multiplication](sub-nlogn-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "Thus $\min_i g_i=2^{-181}=2\kappa$." (paper)

  > The seven dominant powers in Table~\ref{tab:costs} have the following margins below one: \begin{equation}\label{eq:margin-list} \begin{split} g_1&=1-\epsilon(1+c),\qquad g_2=\epsilon c(1-\tau),\qquad g_3=\epsilon(1-\lambda'),\\ g_4&=1-\tau-\epsilon(2-\tau),\qquad g_5=1/4-\delta-3\epsilon/2,\\ g_6&=1-\delta-\epsilon,\qquad g_7=\epsilon. \end{split} \end{equation} Direct substitution gives \[ g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}. \] Thus $\min_i g_i=2^{-181}=2\kappa$. This explicit slack will cover any remaining fixed power of $\log p$.

- "O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})." (paper)

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

Write the body to `exegenius/tasks/0041-write-cost-accounting.answer.md` and the JSON to `exegenius/tasks/0041-write-cost-accounting.answer.json`, then run `exegenius submit 0041-write-cost-accounting` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0041-write-cost-accounting`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
