# exegenius task 0033-write-synthetic-transform

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N3` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science degree: discrete mathematics (sets, subsets and binomial coefficients, induction, modular arithmetic, gcd and the Chinese remainder theorem, primes), a first course in linear algebra (matrices, Gaussian elimination, rank, dot products, possibly over GF(2)), calculus (exponentials, logarithms, Newton's method, simple inequalities), and algorithms and computation theory (asymptotic notation, recurrences and geometric sums, sorting including radix sort, binary search, schoolbook and Karatsuba multiplication, amortized binary counters, Turing machines and worst-case running time). They know binary and two's-complement representation of integers and XOR, but have not studied abstract algebra beyond what these courses use, the fast Fourier transform in depth, quotient polynomial rings, or the research literature on fast integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine (also: fixed finite-tape model)
- Linear maps, subspaces and rank
- Exact integer multiplication on a multitape machine
- n log n optimality conjecture (also: Schönhage–Strassen conjecture)
  - $n$ (input bit length): The number of bits in each of the two input integers.
- Normalized discrete Fourier transform
- Harvey–van der Hoeven O(n log n) multiplier (also: established multiplier)
  - $n$ (operand bit length): The number of bits in each integer given to the multiplier.
- Lexicographic array layout and logical volume (also: logical volume, row)
- Elementary stream operations
- Controlled shifts and rational scalings
- Polynomial ring modulo y^r + 1 (also: R_r, negacyclic polynomial ring)
  - $y$ (ring variable): The polynomial indeterminate whose powers act as synthetic roots of unity.
  - $r$ (record length): The number of complex coefficients in each polynomial record, a power of two.
- Gaussian dyadic numbers and fixed-point grids (also: disk grid array, Q_p)
- Normalized butterfly H₀ (also: butterfly)
  - $H_0$ (normalized butterfly): The two-point linear map sending (u, v) to ((u+v)/2, (u−v)/2).
- Linear network with roles and scratch wires (also: role, scratch wire)
- Restoring arbitrary scratch values (also: transparent computation)
- Triple-intersection pairings (also: Frankl–Wilson construction)
- Nondegenerate bilinear forms and orthogonal residuals
- Three-stage bank exchange (also: gather and scatter, side injection)
- Frames and the common-frame identity (also: frame)
- Nested subspace labels and rank budget (also: labels)
- Recursive saving from s < Wm (also: power saving)
  - $s$ (smaller-call count): The total number of smaller recursive calls made by one use of the finite network.
  - $W$ (wire count): The number of wires (roles) in the finite network.
  - $m$ (label dimension): The dimension of the label space, equal to the factor by which the parameter shrinks per recursion level.
- Address shear
- Lower triangular factorization (also: Bruhat factorization)
- Cost of a rational matrix shear
- Rational shear interface of the bit network
- Power-width interchange recursion
- Fast address-chunk interchange (also: chunk swap, address interchange)
- Binary phase frames (also: binary phase interface, complex network)
- Packed selected-bit addition
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Signed Kronecker packing (also: Kronecker substitution)
- Binary representation of integers (also: binary expansion, bit string value, most significant bit, least significant bit, bin_k, val, radix-2 representation, base-2 digits)
- Positional number systems with a general radix (also: base q digits, radix-q digits, base 2^b digits, radix, digit expansion)
- Two's complement (also: two's-complement integers, signed binary words, sign extension, signed w-bit integer)
- Binary addition with carry propagation (also: carry propagation, ripple-carry addition, carries, schoolbook addition)
- Schoolbook multiplication (also: long multiplication, grade-school multiplication, quadratic multiplication, O(n^2) multiplication)
- Karatsuba multiplication (also: Karatsuba's algorithm, Karatsuba–Ofman, O(n^{log_2 3}) multiplication)
- Integer division with remainder (also: quotient and remainder, Euclidean division, div and mod, integer square root)
- Floor and ceiling (also: ⌊x⌋, ⌈x⌉, rounding down, rounding up, truncation toward zero, integer part)
- Logarithms and exponentials (also: log_2, lg, natural logarithm, log, exp, e^x, logarithmic factor)
- Asymptotic notation beyond big-O (also: Theta notation, Omega notation, little-o, Θ, Ω, o(1), n^{o(1)}, eventually, for sufficiently large n)
- Worst-case running time (also: time complexity, worst-case time, T(n), step count, bit complexity)
- Deterministic computation (also: deterministic Turing machine, deterministic algorithm, no advice, uniform algorithm)
- Polynomial time and polylogarithmic cost (also: polynomial cost, poly(p), b^{O(1)}, polylog)
- Recurrence relations (also: recurrences, divide-and-conquer recurrence, recursion tree, master theorem)
- Geometric series (also: geometric sum, Σ a^k, geometric progression)
- Mathematical induction (also: induction, proof by induction, inductive argument)
- Sets, subsets and Cartesian products (also: Cartesian product, [a] = {0,...,a−1}, set intersection, cardinality, three-element subsets, indicator vector, characteristic vector)
- Binomial coefficients (also: n choose k, C(n,k), combinations, k-subsets)
- Permutations (also: bijection, permutation, inverse permutation, composition of permutations, reordering)
- Lexicographic order (also: row-major order, dictionary order, lexicographic layout, most significant coordinate first)
- Matrix transposition (also: transpose, row-major to column-major, A^T)
- Modular arithmetic (also: congruence, mod, residues, Z/qZ, ≡ (mod q), residue ring, modular inverse)
- Greatest common divisor and the extended Euclidean algorithm (also: gcd, Euclid's algorithm, extended Euclid, coprime, relatively prime, Bézout)
- Prime numbers and trial division (also: primes, odd primes, primality testing, trial division)
- Chinese remainder theorem (also: CRT, Chinese remaindering)
- Exclusive or and arithmetic modulo 2 (also: XOR, ⊕, GF(2), F_2, binary field, parity, bitwise XOR)
- Hamming weight (also: weight, wt(x), popcount, number of ones)
- Gaussian elimination (also: row reduction, elimination, elementary row operations)
- Dot product and orthogonality (also: inner product, orthogonal vectors, orthonormal basis, z·w)
- Special matrices (also: identity matrix, diagonal matrix, triangular matrix, permutation matrix, Kronecker product of matrices, block matrix)
- Triangle inequality (also: |a+b| ≤ |a|+|b|, absolute error bound)
- Bernoulli's inequality (also: (1+x)^n ≥ 1+nx)
- Newton's method (also: Newton iteration, Newton–Raphson)
- Binary search (also: bisection search)
- Radix sort and stable sorting (also: stable sort, binary radix sort, counting sort, merge, merge sort)
- Amortized cost of a binary counter (also: binary counter, incrementing a counter, ripple counting, amortized analysis)
- Stacks (also: stack, push, pop, last-in first-out, LIFO)
- Fixed-point binary numbers (also: fixed-point, fractional bits, binary point, guard bits, precision p)

## This page

Concept: Synthetic polynomial transform
Gloss: Nussbaumer's transform F_t^± over C[y]/(y^r+1) using ω_t = y^{2r/t} as root of unity, computed by decimation-in-frequency levels of butterflies and signed shifts, with outputs stored in bit-reversed frequency order.
Also called: Nussbaumer transform, synthetic roots of unity

## This page in the argument

The step: The decimation-in-frequency recursion with $\omega_t=y^{2r/t}$ computes $B_tF_t^-$ and the reverse procedure computes $F_t^+B_t^{-1}$.
How: check character cancellation directly, then follow the recursion's branch bits into bit-reversed slots
Why: The ring has zero divisors, so the usual geometric-sum cancellation must be checked by a shift argument, and recording where outputs land avoids moving frequency indices. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- $\sum_k\omega_t^{jk}$ is $t$ or $0$ according as $t\mid j$, so $F_t^+F_t^-=t^{-1}I$.
- The outputs are written in bit-reversed order $B_t$ without moving whole frequency indices.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet multitape Turing machine computes the exact product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in that model.; how: build two sublinear-per-level tape procedures from finite linear networks with a rank deficit, then chain the known reductions from integer product to synthetic polynomial transforms and bound every cost (on [Integer multiplication below n log n](main-theorem.md))
- Exact multiplication of two $n$-bit integers reduces to synthetic transforms and packed ring products whose total cost is $O(n(\lg n)^{1-\kappa})$.; how: compute synthetic transforms with the fast layers, build normalized ring convolution, express prime-length transforms by resampling with retained permutations and chirps, then assemble radix digits, the CRT map, the twist, precision and parameters
- Normalized synthetic transforms $F_{\boldsymbol t}^\pm$ over $\mathcal R_r$ on $d-1$ power-of-two axes are computed in a retained stored order at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.; how: decimation-in-frequency with polynomial roots of unity in stored bit-reversed order, grouped into simultaneous rounds on a chunked layout

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.1.1.1, S2.1.1.2). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.1.1.1**: $\sum_k\omega_t^{jk}$ is $t$ or $0$ according as $t\mid j$, so $F_t^+F_t^-=t^{-1}I$.
Source: "The ring has zero divisors, so we verify character cancellation" (paper)
> For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$. For $z\in\mathcal R_r^t$ and $0\leq j<t$, set \[ (F_t^-z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{-jk}z_k, \qquad (F_t^+z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{jk}z_k. \] Every power of $\omega_t$ is an isometry, and each transform entry is an average of $t$ such images. Thus both transforms are contractions. The ring has zero divisors, so we verify character cancellation directly instead of dividing by $\omega_t^j-1$.

**S2.1.1.2**: The outputs are written in bit-reversed order $B_t$ without moving whole frequency indices.
Source: "directly in this order; it does not move whole frequency indices." (paper)
> After all $a$ rounds, the named slots from high to low therefore contain the frequency bits from low to high. If $\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$. Let $B_t$ denote this record permutation: it moves the entry at $j$ to $\operatorname{rev}_a(j)$. The recursion writes its outputs directly in this order; it does not move whole frequency indices.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Polynomial ring modulo y^r + 1](negacyclic-ring.md): The ring 𝓡_r = C[y]/(y^r + 1) with r a power of two, where multiplying by a power of y is a signed cyclic shift of the coefficient list and the wrap is negacyclic.
  Shown as: Synthetic polynomial transform *<predicate>* Polynomial ring modulo y^r + 1
- [Normalized butterfly H₀](normalized-butterfly.md): The two-point map H₀(u, v) = ((u+v)/2, (u−v)/2), a contraction applied coefficientwise on polynomial records along one address bit; it is the arithmetic step of each radix-two transform level.
  Shown as: Synthetic polynomial transform *<predicate>* Normalized butterfly H₀
- [Normalized discrete Fourier transform](discrete-fourier-transform.md): The map (F_q u)_k = (1/q) Σ_j u_j e^{−2πijk/q} (and its opposite-sign version F_q^+), a contraction in the max-modulus norm; tensor products F_q over several axes give multidimensional transforms.
  Shown as: Synthetic polynomial transform *<predicate>* Normalized discrete Fourier transform

## Pages that build on this one

- Transform layout on K-bit chunks: The tape layout placing the selected address bits of all participating axes at a common offset in consecutive K-bit chunks, with polynomial coefficients in a contiguous suffix, so that each transform round is one simultaneous layer.
- Normalized convolution over the polynomial ring: Computing 𝓜_r(f, g) = (f*g)/(rM) for arrays over 𝓡_r by two forward synthetic transforms kept in the same stored frequency order, packed pointwise ring products, and the opposite transform consuming that order.

## Other pages you may link to

- [Exact integer multiplication on a multitape machine](integer-multiplication-problem.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Gaussian dyadic numbers and fixed-point grids](gaussian-dyadics.md)
- [Signed Kronecker packing](signed-packing.md)
- [n log n optimality conjecture](nlogn-conjecture.md)
- [Lexicographic array layout and logical volume](array-layout.md)
- [Elementary stream operations](elementary-streams.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Address shear](address-shear.md)
- [Linear maps, subspaces and rank](linear-algebra.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Linear network with roles and scratch wires](linear-network.md)
- [Frames and the common-frame identity](frames.md)
- [Restoring arbitrary scratch values](scratch-restoration.md)
- [Nondegenerate bilinear forms and orthogonal residuals](bilinear-forms.md)
- [Triple-intersection pairings](triple-intersection.md)
- [Three-stage bank exchange](bank-exchange.md)
- [Nested subspace labels and rank budget](subspace-labels.md)
- [Recursive saving from s < Wm](rank-deficit-recursion.md)
- [Rational shear interface of the bit network](rational-shear-interface.md)
- [Binary phase frames](phase-frames.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Power-width interchange recursion](power-width-interchange.md)
- [Fast address-chunk interchange](fast-chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling with retained permutations](no-sort-resampling.md)
- [Transform layout on K-bit chunks](transform-layout.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit reduction to convolution](radix-digit-convolution.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Coefficient twist](coefficient-twist.md)
- [Normalized convolution over the polynomial ring](synthetic-convolution.md)
- [Source permutation cancellation](source-permutation-cancellation.md)
- [Error below 1/2 and exact recovery](exact-recovery.md)
- [Parameter choice and cost table](parameter-choice.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.

- "For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$." (paper)

  > For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$. For $z\in\mathcal R_r^t$ and $0\leq j<t$, set \[ (F_t^-z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{-jk}z_k, \qquad (F_t^+z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{jk}z_k. \] Every power of $\omega_t$ is an isometry, and each transform entry is an average of $t$ such images. Thus both transforms are contractions. The ring has zero divisors, so we verify character cancellation directly instead of dividing by $\omega_t^j-1$.

- "the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$." (paper)

  > After all $a$ rounds, the named slots from high to low therefore contain the frequency bits from low to high. If $\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$. Let $B_t$ denote this record permutation: it moves the entry at $j$ to $\operatorname{rev}_a(j)$. The recursion writes its outputs directly in this order; it does not move whole frequency indices.


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

Write the body to `exegenius/tasks/0033-write-synthetic-transform.answer.md` and the JSON to `exegenius/tasks/0033-write-synthetic-transform.answer.json`, then run `exegenius submit 0033-write-synthetic-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0033-write-synthetic-transform`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
