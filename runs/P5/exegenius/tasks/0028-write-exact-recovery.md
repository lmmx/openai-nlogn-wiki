# exegenius task 0028-write-exact-recovery

Project directory: `/home/user/openai-nlogn-wiki/runs/P5` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: comfortable with asymptotic notation, recurrences and divide-and-conquer, binary and two's-complement arithmetic, integer division with remainder, modular arithmetic, primes and coprimality, sets, bijections and functions, basic vector and matrix algebra, polynomials and complex numbers (including roots of unity), and basic multitape Turing machines with linear scans. The reader has seen schoolbook and Karatsuba multiplication and probably an introductory FFT in an algorithms course, but has not studied abstract algebra (rings, groups, tensor products), finite fields beyond bit arithmetic, numerical analysis of rounding, or the specialist theory of fast integer multiplication, so the wiki must explain those.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Basic Turing machines and tapes
- Fixed finite-tape Turing machine model
- The n log n conjecture and the history of multiplication
- Established O(n log n) multiplier as a subroutine
- Cyclic convolution
- Polynomial ring modulo y^r+1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate with y^r = −1; its powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record; a power of two.
- Fixed-point grid arrays with precision p
  - $p$ (precision): The number of fractional bits kept in each real or imaginary component.
- Exact Gaussian dyadic evaluation of a layer
- Array streams, address fields and elementary scans
- Controlled shifts and fixed rational scalings
- Subspaces, rank and orthogonal complements
- Triple indicator vectors and intersection pairings
- Scalar exchange network with restored scratch wires
- Frames and the common-frame identity
- Subspace labels and the rank saving s<Wm
  - $s$ (total edge rank): The number of smaller calls needed, equal to the sum of the ranks of all edge differences.
  - $W$ (wire count): The number of wires, including scratch wires, in the network.
  - $m$ (label dimension): The dimension of the ambient label space.
- Bit network and its shear interface
- Lower-triangular factorization of a matrix
- Address shear costing rank-many interchanges
- Power saving from a rank-deficit recursion
- Address-chunk interchange in O(Vu^τ) time
  - $V$ (stored volume): The number of stored data bits in the array.
  - $u$ (chunk width): The number of bits in each of the two address fields being interchanged.
  - $\tau$ (interchange exponent): A fixed constant below 1, namely 1−2^{-50}.
- Packed selected-bit addition
- Signed packing of polynomial products
- Multiplication as radix-digit convolution
- Chinese-remainder map to prime cyclic axes (also: Agarwal–Cooley)
- Coefficient twist from cyclic to negacyclic
- Logarithms, floors and ceilings (also: log, lg, log base 2, floor, ceiling, ⌊x⌋, ⌈x⌉)
- Binary representation and integer arithmetic (also: binary numerals, bit strings, radix representation, base-b digits, bits, carries)
- Division with remainder (also: quotient and remainder, Euclidean division, integer division)
- Modular arithmetic (also: congruences, residues, mod q, integers modulo q, Z/qZ, residue classes)
- Primes, divisibility and coprimality (also: prime numbers, relatively prime, pairwise coprime, gcd, greatest common divisor, coprime)
- Sets, functions and permutations (also: bijection, permutation of a set, subsets, intersection, cardinality, indicator vector, Cartesian product)
- Matrices and linear maps (also: matrix-vector product, identity matrix, permutation matrix, matrix inverse, linear transformation, vector spaces)
- XOR and arithmetic over F₂ (also: exclusive or, mod 2 addition, bitwise XOR, GF(2), parity, Hamming weight, popcount)
- Asymptotic notation beyond big-O (also: Θ, Ω, little-o, Theta notation, polylogarithmic factor, poly log)
- Recurrences and divide and conquer (also: recurrence relation, master theorem, recursion tree, geometric series, divide-and-conquer)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, quadratic multiplication, Karatsuba, O(n^2) multiplication)
- Fast Fourier transform as an algorithm (also: FFT, Cooley–Tukey, Cooley-Tukey algorithm, fast polynomial multiplication by FFT, evaluation and interpolation)
- Inequalities for error bounds (also: triangle inequality, absolute value bounds, modulus bound, error accumulation, rounding error)
- Lexicographic order and mixed-radix indices (also: row-major order, multi-dimensional arrays, array indexing, mixed radix, lexicographic address order)
- Two's-complement and truncation (also: signed integers, round toward zero, truncate, fixed-point numbers)

## This page

Concept: Exact recovery by rounding and carry propagation
Gloss: Undoing known scales S and 2^{2b+4}, showing the coefficient error is below 1/2, rounding to integers, and propagating radix-2^b carries to obtain the exact 2n-bit product.

## This page in the argument

The step: Undoing the known scales shows every recovered coefficient has error below $1/2$, so rounding and radix-$2^b$ carry propagation give the exact $2n$-bit product.
How: bound the accumulated numerical error against the integrality of the coefficients, then recover the digits
Why: The true coefficients are integers, so once the computed value is within $1/2$ of it, rounding is exact; the carries then only convert the coefficients into binary digits. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The accumulated error of all transforms, scales $S$ and $2^{2b+4}$ is below $448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<1/2$.
- The strict error bound makes the nearest integer to each computed coefficient the unique correct one, and it lies in $[0,2^{3b})$.
- Carries $k_{j+1}=\lfloor(c_j+k_j)/2^b\rfloor$ stay below $2^{2b}$, and propagating them in increasing order yields the radix digits of the product.

It serves these steps, from the main result down:

- A deterministic fixed-tape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: build two tape procedures that save a power of the width, use them inside the Harvey and van der Hoeven Gaussian-resampling multiplication with polynomial transforms and retained permutations, then choose parameters, prove exactness and sum the costs (on [Integer multiplication in O(n (lg n)^{1−κ}) time](main-theorem.md))
- The sizes, the assembled algorithm with exact recovery, and the cost bound complete the multiplication.; how: choose parameters compatible with all earlier interfaces, run the pipeline, prove exactness, and sum the costs
- The assembled algorithm places the radix digits on prime axes by the Chinese-remainder map, applies two source transforms, a pointwise product and one opposite transform, then rescales, rounds and carries to give the exact product.; how: reduce the integer product to a convolution, move it step by step to the ring convolution of the earlier sections, and recover the integer by rounding (on [The assembled multiplication algorithm](multiplication-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (D2.6.1, D2.6.2, D2.6.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**D2.6.1**: The accumulated error of all transforms, scales $S$ and $2^{2b+4}$ is below $448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<1/2$.
Source: "448b\,2^{-b+\gamma}" (paper)
> In tensor order, the unscaled integer coefficient array is $2^{2b+4}S w$. This second occurrence of $S$ reverses the normalization still present in $w$, and $2^{2b+4}$ reverses the two input scales. Both multiplications act exactly on grid numerators. Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than \begin{equation}\label{eq:final-error} 2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b} <448b\,2^{-b+\gamma} \le448b\,2^{-3b/4}<\frac12. \end{equation} The true coefficients are real integers. If $H_j$ is the real numerator after the second scaling, its represented value is $H_j/2^p$. The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.

**D2.6.2**: The strict error bound makes the nearest integer to each computed coefficient the unique correct one, and it lies in $[0,2^{3b})$.
Source: "The strict error below $1/2$ makes the nearest integer to" (paper)
> In tensor order, the unscaled integer coefficient array is $2^{2b+4}S w$. This second occurrence of $S$ reverses the normalization still present in $w$, and $2^{2b+4}$ reverses the two input scales. Both multiplications act exactly on grid numerators. Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than \begin{equation}\label{eq:final-error} 2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b} <448b\,2^{-b+\gamma} \le448b\,2^{-3b/4}<\frac12. \end{equation} The true coefficients are real integers. If $H_j$ is the real numerator after the second scaling, its represented value is $H_j/2^p$. The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.

**D2.6.3**: Carries $k_{j+1}=\lfloor(c_j+k_j)/2^b\rfloor$ stay below $2^{2b}$, and propagating them in increasing order yields the radix digits of the product.
Source: "To propagate carries, let $Q_0=2^b$." (paper)
> To propagate carries, let $Q_0=2^b$. The recovered ordinary coefficients are the $c_j$ in \eqref{eq:capacity}; they are zero for $2q-2<j<S$. With $q=\lceil n/b\rceil$ as above, use the recurrence for $0\le j<S$: \[ k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad k_{j+1}=\left\lfloor\frac{c_j+k_j}{Q_0}\right\rfloor. \] The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$. If this holds at $j$, then \[ c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1), \] which proves the next carry bound. The defining relation $c_j+k_j=d_j+Q_0k_{j+1}$ also gives the exact invariant \[ \sum_{h<j}c_hQ_0^h =\sum_{h<j}d_hQ_0^h+k_jQ_0^j. \] It holds for $j=0$, and the defining relation proves its next instance. The unprocessed terms are multiples of $Q_0^j$, so the identity fixes the first $j$ radix digits of the full product. The value $k_j$ is the carry from the processed coefficients into the remaining positions.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Multiplication as radix-digit convolution](digit-convolution.md): Writing both inputs in radix 2^b with q=⌈n/b⌉ digits, the product coefficients are a convolution with capacity below 2^{3b}, and padding to length S avoids wraparound.
  Shown as: Exact recovery by rounding and carry propagation *<predicate>* Multiplication as radix-digit convolution
- [Fixed-point grid arrays with precision p](fixed-point.md): Complex numbers of modulus at most 1 stored as signed two's-complement integers scaled by 2^{-p}, with truncation toward zero after each completed step and error tracked as multiples of 2^{-p}.
  Shown as: Exact recovery by rounding and carry propagation *<predicate>* Fixed-point grid arrays with precision p

## Pages that build on this one

- The assembled multiplication algorithm: Digits are placed on prime axes by the CRT map, two source transforms (Gaussian resampling with chirp convolution over the ring via twist, using synthetic convolution) and one opposite transform give the digit convolution, then rescale, round and carry.

## Other pages you may link to

- [Exact Gaussian dyadic evaluation of a layer](dyadic-exact.md)
- [Fixed finite-tape Turing machine model](fixed-tape-model.md)
- [The n log n conjecture and the history of multiplication](nlogn-conjecture.md)
- [Established O(n log n) multiplier as a subroutine](hvdh-multiplier.md)
- [Array streams, address fields and elementary scans](streams.md)
- [Controlled shifts and fixed rational scalings](controlled-shifts.md)
- [Subspaces, rank and orthogonal complements](linear-algebra.md)
- [Triple indicator vectors and intersection pairings](three-subset-pairing.md)
- [Scalar exchange network with restored scratch wires](scalar-exchange-network.md)
- [Frames and the common-frame identity](frames.md)
- [Subspace labels and the rank saving s<Wm](subspace-labels.md)
- [Power saving from a rank-deficit recursion](power-saving-recursion.md)
- [Bit network and its shear interface](bit-network.md)
- [Lower-triangular factorization of a matrix](lower-triangular-factorization.md)
- [Address shear costing rank-many interchanges](address-shear.md)
- [Address-chunk interchange in O(Vu^τ) time](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bits.md)
- [Polynomial ring modulo y^r+1](ring-mod-yr-plus-1.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Cyclic convolution](convolution.md)
- [Chinese-remainder map to prime cyclic axes](crt-cyclic-axes.md)
- [Coefficient twist from cyclic to negacyclic](phase-twist.md)
- [Normalized discrete Fourier transform F_q](dft.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Two-point butterfly H₀ and the radix-two recursion](butterfly.md)
- [Synthetic polynomial transforms](synthetic-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Retained bit-reversed frequency order](stored-order.md)
- [Retaining resampling permutations in the transform](retained-permutations.md)
- [Binary phase frames and the two-point kernel C](phase-frames.md)
- [Simultaneous butterfly layer in O(Vd^λ') time](simultaneous-layer.md)
- [Synthetic transform layout and cost](transform-layout.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Size parameters and prime source lengths](size-parameters.md)
- [The assembled multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Integer multiplication in O(n (lg n)^{1−κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product" (paper)

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

Write the body to `exegenius/tasks/0028-write-exact-recovery.answer.md` and the JSON to `exegenius/tasks/0028-write-exact-recovery.answer.json`, then run `exegenius submit 0028-write-exact-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0028-write-exact-recovery`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
