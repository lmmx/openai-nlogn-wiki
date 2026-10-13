# exegenius task 0037-write-crt-address-map

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
- Discrete Fourier transform
- Cyclic convolution
- Multiplication as convolution of radix digits
- Multidimensional transform
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Two-point butterfly layer (also: butterfly, H₀)
- Synthetic polynomial transform (also: Nussbaumer polynomial transform)
- Signed packing for ring products
- The established O(N log N) multiplier
- Subspaces, bilinear forms and orthogonal complements
- Linear network with restored scratch wires (also: motif network, restoration schedule)
- Triple-subset intersection gadgets
- Frames on wire arrays
- Nested subspace labels and the rank deficit (also: s<Wm)
- Recursive power saving from the rank deficit
- Lower triangular factorization
- Matrix shear on address fields
- Fast interchange of address chunks
- Binary phase frames and the two-point kernel C
- Packed selected-bit addition
- Simultaneous butterfly layer
- Synthetic transform tape layout
- Normalized convolution over the ring
- Last-coordinate phase twist
- Gaussian resampling
- Resampling with permutations left in the transform
- Bluestein chirp identity
- Error bounds and exact recovery
- Parameter choice and cost table
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

Concept: Chinese-remainder address map
Gloss: An algebra isomorphism Φ sending x to Π x_i^{μ_i} that turns cyclic convolution of length S=Πs_i (pairwise coprime) into convolution on the product of cyclic axes, implemented by triangular controlled shifts.
Also called: Φ

## This page in the argument

The step: With $P_i=\prod_{j<i}s_j$ and $\mu_i=P_i^{-1}\bmod s_i$, the map $\Phi:x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\ldots,x_d]/(x_i^{s_i}-1)$ that turns cyclic convolution of length $S$ into convolution on the product of cyclic axes, and it and its inverse are implemented by triangular controlled shifts in time $O(T p\,d^2(1+\ell^\tau))$.
How: Apply the Chinese remainder theorem to the exponents, so that each new axis coordinate depends only on lower-index digits and the change of order is a sequence of prefix-controlled cyclic shifts after reordering the axes by chunk interchanges.
Why: The map is chosen with coordinate powers that make the change of order a sequence of controlled cyclic shifts. (the sources say so: "algebraic split, with coordinate powers that make the change of order a" (paper))
Striking feature: The coordinate change is triangular, because axis $i$ depends only on lower-index digits, so every update is a controlled shift and no general transpose is needed. (explain why it holds, from the method)

Its sub-steps, in order:

- The assignment $x\mapsto\prod_ix_i^{\mu_i}$ respects $x^S=1$ and its image has order $S$, so it is an isomorphism preserving cyclic convolution.
- Each index $k=\sum_ja_jP_j$ has axis coordinates $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, which depend only on lower-index digits, so the change is triangular.
- After reordering the axes so that lower indices come first, updating targets $i=d,\ldots,1$ uses the original digits as controls, zero padding stays zero, and an explicit inverse exists.
- Each triangular update is a prefix-controlled cyclic shift of linear cost, and reordering the axes needs $O(d^2)$ chunk interchanges of $\ell$-bit or $(\ell-1)$-bit fields, for a total $O(T p\,d^2(1+\ell^\tau))$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a convolution over a polynomial ring computed by Fourier-type transforms; supply the two fast tape procedures that remove the logarithmic factor from address movement and from butterfly arithmetic, both obtained from linear networks that save a power; then assemble the algorithm and tally every cost. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- The procedure that extracts radix-$2^b$ digits, applies the Chinese-remainder address map $\Phi$, computes two forward source transforms, a pointwise product and the opposite transform with exact rescalings, rounds, and propagates carries outputs the exact $2n$-bit product.; how: Choose the parameters, place the digits on a product of distinct prime cyclic axes by the Chinese-remainder map, compute the cyclic convolution through resampled transforms in which the middle transform is a chirp convolution evaluated over the polynomial ring after a phase twist, undo the known normalizations, bound the error below $1/2$, round, and propagate carries. (on [The multiplication algorithm](multiplication-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S7.2.1, S7.2.2, S7.2.3, S7.2.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S7.2.1**: The assignment $x\mapsto\prod_ix_i^{\mu_i}$ respects $x^S=1$ and its image has order $S$, so it is an isomorphism preserving cyclic convolution.
Source: "respects $x^S=1$, so it defines an algebra map." (paper)
> Let $s_1,\ldots,s_d$ be the pairwise coprime source lengths, let $S=\prod_i s_i$, and put \[ P_i=\prod_{j<i}s_j,\qquad \mu_i=P_i^{-1}\pmod{s_i}. \] Here $P_i$ denotes an integer prefix product, not a Fourier-coordinate permutation. The assignment \[ \Phi:\mathbb C[x]/(x^S-1)\longrightarrow \mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1), \qquad x\longmapsto\prod_i x_i^{\mu_i} \] respects $x^S=1$, so it defines an algebra map. The target monomial group has size $S$, and the image of $x$ has order $S$, because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime. Its powers therefore run through all target basis monomials exactly once. Hence $\Phi$ is an isomorphism and preserves cyclic convolution.

**S7.2.2**: Each index $k=\sum_ja_jP_j$ has axis coordinates $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, which depend only on lower-index digits, so the change is triangular.
Source: "Every ordinary coefficient index has a unique mixed-radix expression" (paper)
> Every ordinary coefficient index has a unique mixed-radix expression \[ k=\sum_{j=1}^d a_jP_j,\qquad 0\le a_j<s_j. \] The coordinate of $\Phi(x^k)$ in axis $i$ is \begin{equation}\label{eq:triangular-crt} b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}. \end{equation} Indeed terms with $j>i$ are divisible by $s_i$, and $\mu_iP_i=1$ modulo $s_i$. Numerical order of $k$ is lexicographic order of $(a_d,\ldots,a_1)$. Insert the padding in one nested scan of the full box $\prod_i[0,t_i)$ in this lexicographic order, with $a_d$ the outermost counter and $a_1$ the innermost. At an address satisfying $a_i<s_i$ for every $i$, copy the next original coefficient record; at every other address, write a zero record. The valid addresses occur in the original coefficient order, so each record is copied to its intended mixed-radix address. To delete the padding after the inverse axis reorder, use the same enumeration, copying the record at each valid address and skipping the record at each invalid address.

**S7.2.3**: After reordering the axes so that lower indices come first, updating targets $i=d,\ldots,1$ uses the original digits as controls, zero padding stays zero, and an explicit inverse exists.
Source: "Now reorder the complete padded axes to $(a_1,\ldots,a_d)$.  In this" (paper)
> Now reorder the complete padded axes to $(a_1,\ldots,a_d)$. In this physical order, the coordinates with indices below $i$ precede coordinate $i$. Update the targets in the order $i=d,d-1,\ldots,1$ using \eqref{eq:triangular-crt}. When target $i$ is updated, none of its lower-index controls has yet changed, so the offset is computed from the original digits $a_j$ required by the formula.

**S7.2.4**: Each triangular update is a prefix-controlled cyclic shift of linear cost, and reordering the axes needs $O(d^2)$ chunk interchanges of $\ell$-bit or $(\ell-1)$-bit fields, for a total $O(T p\,d^2(1+\ell^\tau))$.
Source: "The axis widths are $\ell$ or $\ell-1$.  To exchange two adjacent axes" (paper)
> The axis widths are $\ell$ or $\ell-1$. To exchange two adjacent axes of unequal width, move the longer axis's leading bit outside their equal-width pair, swap that pair by the proved chunk-swap procedure, and put the leading bit at its new position. This adds a fixed number of linear passes to the equal-width swap cost. Reversing all axes uses $O(d^2)$ such moves. Therefore the map $\Phi$, its inverse, and their padding operations cost \[ O\bigl(Tp\,d^2(1+\ell^\tau)\bigr). \] This construction describes payload movement from address $a$ to its new address. It is distinct from the operator convention $(R_cz)_j=z_{cj}$ used for Fourier dilations, which moves a payload from address $j$ to $c^{-1}j$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Fast interchange of address chunks](fast-chunk-interchange.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Multidimensional transform](multidimensional-transform.md): The tensor product of one-dimensional Fourier transforms along several axes, computing convolution on a product of cyclic groups.
  Shown as: Chinese-remainder address map *<predicate>* Multidimensional transform
- [Controlled shifts and rational scalings](controlled-shift.md): A linear-time tape operation that adds an offset, computed from earlier control fields, to a later address field modulo a prime power, or multiplies it by a rational unit.
  Shown as: Chinese-remainder address map *<predicate>* Controlled shifts and rational scalings
- [Arrays as tape streams and elementary scans](tape-streams.md): Arrays stored in lexicographic address order on tapes, with logical volume V (number of stored bits), whose splitting, merging and digit moves cost linear time.
  Shown as: Chinese-remainder address map *<predicate>* Arrays as tape streams and elementary scans

## Pages that build on this one

- The multiplication algorithm: Digit extraction, the Chinese-remainder map, two forward source transforms, pointwise product, opposite transform, rescaling, rounding and carry propagation yielding the exact 2n-bit product.

## Other pages you may link to

- [The n log n conjecture and prior bounds](nlogn-conjecture.md)
- [Linear network with restored scratch wires](linear-network.md)
- [Frames on wire arrays](frames.md)
- [Fixed-point and Gaussian dyadic arithmetic](fixed-point-dyadics.md)
- [Subspaces, bilinear forms and orthogonal complements](linear-algebra-orthogonality.md)
- [Triple-subset intersection gadgets](triple-subset-gadgets.md)
- [Nested subspace labels and the rank deficit](rank-deficit-labels.md)
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
- [The multiplication algorithm](multiplication-algorithm.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Agarwal and Cooley used the Chinese remainder" (paper)

  > To use the source tensor, we first place the ordinary coefficient stream in its tensor order. Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution~\cite{AgarwalCooley1977}. The following map uses that algebraic split, with coordinate powers that make the change of order a sequence of controlled cyclic shifts.

- "x\longmapsto\prod_i x_i^{\mu_i}" (paper)

  > Let $s_1,\ldots,s_d$ be the pairwise coprime source lengths, let $S=\prod_i s_i$, and put \[ P_i=\prod_{j<i}s_j,\qquad \mu_i=P_i^{-1}\pmod{s_i}. \] Here $P_i$ denotes an integer prefix product, not a Fourier-coordinate permutation. The assignment \[ \Phi:\mathbb C[x]/(x^S-1)\longrightarrow \mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1), \qquad x\longmapsto\prod_i x_i^{\mu_i} \] respects $x^S=1$, so it defines an algebra map. The target monomial group has size $S$, and the image of $x$ has order $S$, because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime. Its powers therefore run through all target basis monomials exactly once. Hence $\Phi$ is an isomorphism and preserves cyclic convolution.

- "$\Phi$ is an isomorphism and preserves cyclic convolution." (paper)

  > Let $s_1,\ldots,s_d$ be the pairwise coprime source lengths, let $S=\prod_i s_i$, and put \[ P_i=\prod_{j<i}s_j,\qquad \mu_i=P_i^{-1}\pmod{s_i}. \] Here $P_i$ denotes an integer prefix product, not a Fourier-coordinate permutation. The assignment \[ \Phi:\mathbb C[x]/(x^S-1)\longrightarrow \mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1), \qquad x\longmapsto\prod_i x_i^{\mu_i} \] respects $x^S=1$, so it defines an algebra map. The target monomial group has size $S$, and the image of $x$ has order $S$, because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime. Its powers therefore run through all target basis monomials exactly once. Hence $\Phi$ is an isomorphism and preserves cyclic convolution.


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

Write the body to `exegenius/tasks/0037-write-crt-address-map.answer.md` and the JSON to `exegenius/tasks/0037-write-crt-address-map.answer.json`, then run `exegenius submit 0037-write-crt-address-map` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0037-write-crt-address-map`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
