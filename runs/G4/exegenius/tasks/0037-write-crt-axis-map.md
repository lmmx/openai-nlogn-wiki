# exegenius task 0037-write-crt-axis-map

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
- Gaussian resampling
- Multidimensional resampling on a padded box
- Bluestein chirp identity
- Source permutation cancellation
- Exact recovery of the integer product
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

Concept: Chinese-remainder axis map
Gloss: Mapping a cyclic convolution of length S = ∏ s_i with pairwise coprime s_i to a multidimensional cyclic convolution via x ↦ ∏ x_i^{μ_i}, implemented by triangular controlled shifts and axis moves.

## This page in the argument

The step: The map $x\mapsto\prod_ix_i^{\mu_i}$ with $\mu_i=P_i^{-1}\bmod s_i$ and $P_i=\prod_{j<i}s_j$ takes cyclic convolution of length $S=\prod_is_i$ to multidimensional cyclic convolution, and is implemented by triangular controlled shifts and axis moves in $O(Tp\,d^2(1+\ell^\tau))$ time.
How: Use the Chinese remainder theorem as an algebra isomorphism, write each index in mixed radix, and see that axis $i$ depends only on lower digits, so the change of order is a sequence of prefix-controlled cyclic shifts.
Why: The assignment respects $x^S=1$ and sends the powers of $x$ bijectively onto the basis monomials, so it preserves convolution; the choice of coordinate powers makes the change of order triangular. (the sources say so: "sequence of controlled cyclic shifts." (paper))
Striking feature: The image coordinate $b_i$ of an index depends only on its own digit and the lower digits, which is why the whole change of order is a sequence of controlled shifts with controls placed before their targets. (explain why it holds, from the method)

Its sub-steps, in order:

- The map is an algebra isomorphism that preserves cyclic convolution.
- Update the targets in the order $i=d,d-1,\ldots,1$, so the lower-index controls still hold their original digits.
- Each triangular update is a prefix-controlled cyclic shift, preserving zero padding.
- Reordering the axes of widths $\ell$ or $\ell-1$ uses $O(d^2)$ chunk swaps, so $\Phi$ and its inverse cost $O(Tp\,d^2(1+\ell^\tau))$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in that model.; how: Reduce the product to a cyclic convolution of radix digits evaluated by Fourier-type transforms, make the two costly ingredients of those transforms (address rearrangement and butterfly arithmetic) cost a power of the logarithm less than a full scan per level by two rank-saving tape procedures, then assemble the algorithm, prove exactness and total the cost. (on [Sub-n log n integer multiplication](sub-nlogn-multiplication.md))
- The algorithm maps the digit polynomials by the Chinese-remainder map to prime axes, transforms them by resampling plus chirp convolution, multiplies pointwise, applies the opposite transform, rescales, rounds and propagates carries.; how: Use the convolution theorem on the prime-axis tensor: the digit convolution equals $F^+(Fu\cdot Fv)$ up to known scales, with the middle transform $QF_{\boldsymbol t}$ computed as a chirp convolution through the twist and synthetic convolution. (on [The multiplication algorithm](multiplication-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S6.2.1, S6.2.2, S6.2.3, S6.2.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S6.2.1**: The map is an algebra isomorphism that preserves cyclic convolution.
Source: "$\Phi$ is an isomorphism and preserves cyclic convolution." (paper)
> Let $s_1,\ldots,s_d$ be the pairwise coprime source lengths, let $S=\prod_i s_i$, and put \[ P_i=\prod_{j<i}s_j,\qquad \mu_i=P_i^{-1}\pmod{s_i}. \] Here $P_i$ denotes an integer prefix product, not a Fourier-coordinate permutation. The assignment \[ \Phi:\mathbb C[x]/(x^S-1)\longrightarrow \mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1), \qquad x\longmapsto\prod_i x_i^{\mu_i} \] respects $x^S=1$, so it defines an algebra map. The target monomial group has size $S$, and the image of $x$ has order $S$, because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime. Its powers therefore run through all target basis monomials exactly once. Hence $\Phi$ is an isomorphism and preserves cyclic convolution.

**S6.2.2**: Update the targets in the order $i=d,d-1,\ldots,1$, so the lower-index controls still hold their original digits.
Source: "order $i=d,d-1,\ldots,1$ using \eqref{eq:triangular-crt}." (paper)
> Now reorder the complete padded axes to $(a_1,\ldots,a_d)$. In this physical order, the coordinates with indices below $i$ precede coordinate $i$. Update the targets in the order $i=d,d-1,\ldots,1$ using \eqref{eq:triangular-crt}. When target $i$ is updated, none of its lower-index controls has yet changed, so the offset is computed from the original digits $a_j$ required by the formula.

**S6.2.3**: Each triangular update is a prefix-controlled cyclic shift, preserving zero padding.
Source: "Each triangular update is a prefix-controlled cyclic shift." (paper)
> Each triangular update is a prefix-controlled cyclic shift. The controls precede its target in the current physical order. For each prefix, prepare the offset, split the valid target interval into its two consecutive pieces, and merge those pieces in the opposite order. Every target position carries its full spectator suffix as a block; the invalid interval is copied unchanged. There are at most $T/t_i$ control prefixes for target $i$. For any fixed setup degree $C$, all offsets therefore cost $O(dTp^C/r)=o(Tp)$ to prepare, since $t_i\ge r/2$ and $r$ exceeds every fixed power of $p$.

**S6.2.4**: Reordering the axes of widths $\ell$ or $\ell-1$ uses $O(d^2)$ chunk swaps, so $\Phi$ and its inverse cost $O(Tp\,d^2(1+\ell^\tau))$.
Source: "The axis widths are $\ell$ or $\ell-1$." (paper)
> The axis widths are $\ell$ or $\ell-1$. To exchange two adjacent axes of unequal width, move the longer axis's leading bit outside their equal-width pair, swap that pair by the proved chunk-swap procedure, and put the leading bit at its new position. This adds a fixed number of linear passes to the equal-width swap cost. Reversing all axes uses $O(d^2)$ such moves. Therefore the map $\Phi$, its inverse, and their padding operations cost \[ O\bigl(Tp\,d^2(1+\ell^\tau)\bigr). \] This construction describes payload movement from address $a$ to its new address. It is distinct from the operator convention $(R_cz)_j=z_{cj}$ used for Fourier dilations, which moves a payload from address $j$ to $c^{-1}j$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Convolution](convolution.md): The product of two coefficient lists, cyclic when indices wrap around modulo the length, equal to polynomial multiplication modulo x^S − 1.
  Shown as: Chinese-remainder axis map *<predicate>* Convolution
- [Controlled shifts and rational scalings](controlled-shift.md): An O(V) tape operation that adds an offset computed from earlier fields to a later field modulo q^b (a cyclic shift), or multiplies it by a fixed rational unit.
  Shown as: Chinese-remainder axis map *<predicate>* Controlled shifts and rational scalings
- [Fast chunk interchange](chunk-interchange.md): Exchanging two equal-width address fields of u bits in an arbitrary array in O(V u^τ) time for a fixed τ < 1, even though intermediate steps XOR data together.
  Shown as: Chinese-remainder axis map *<predicate>* Fast chunk interchange

## Pages that build on this one

- Parameter choices: Choosing b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, power-of-two axis lengths t_i near r and distinct primes s_i just below them, so Tp = Θ(n) and all hypotheses hold.
- The multiplication algorithm: Digit polynomials are mapped by the CRT map to prime axes, transformed by resampling plus chirp-convolution (via the twist and synthetic convolution), multiplied pointwise, inverse transformed, rescaled, rounded and carried.

## Other pages you may link to

- [Recursive power saving from a rank deficit](recursive-power-saving.md)
- [Fixed-tape Turing machine model](fixed-tape-model.md)
- [Established O(n log n) integer multiplier](nlogn-multiplier.md)
- [Elementary stream operations on tape arrays](elementary-stream-ops.md)
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
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Synthetic transform layout and cost](synthetic-transform-layout.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Source permutation cancellation](permutation-cancellation.md)
- [Multidimensional resampling on a padded box](tensor-resampling.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Exact recovery of the integer product](exact-recovery.md)
- [Parameter choices](parameter-choices.md)
- [Coefficient twist to the negacyclic ring](convolution-twist.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound](cost-accounting.md)
- [Sub-n log n integer multiplication](sub-nlogn-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "x\longmapsto\prod_i x_i^{\mu_i}" (paper)

  > Let $s_1,\ldots,s_d$ be the pairwise coprime source lengths, let $S=\prod_i s_i$, and put \[ P_i=\prod_{j<i}s_j,\qquad \mu_i=P_i^{-1}\pmod{s_i}. \] Here $P_i$ denotes an integer prefix product, not a Fourier-coordinate permutation. The assignment \[ \Phi:\mathbb C[x]/(x^S-1)\longrightarrow \mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1), \qquad x\longmapsto\prod_i x_i^{\mu_i} \] respects $x^S=1$, so it defines an algebra map. The target monomial group has size $S$, and the image of $x$ has order $S$, because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime. Its powers therefore run through all target basis monomials exactly once. Hence $\Phi$ is an isomorphism and preserves cyclic convolution.

- "Agarwal and Cooley used the Chinese remainder" (paper)

  > To use the source tensor, we first place the ordinary coefficient stream in its tensor order. Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution~\cite{AgarwalCooley1977}. The following map uses that algebraic split, with coordinate powers that make the change of order a sequence of controlled cyclic shifts.


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

Write the body to `exegenius/tasks/0037-write-crt-axis-map.answer.md` and the JSON to `exegenius/tasks/0037-write-crt-axis-map.answer.json`, then run `exegenius submit 0037-write-crt-axis-map` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0037-write-crt-axis-map`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
