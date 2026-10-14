# exegenius task 0014-write-address-shear

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
- Exact integer multiplication on a multitape machine
- n log n optimality conjecture (also: Schönhage–Strassen conjecture)
  - $n$ (input bit length): The number of bits in each of the two input integers.
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

Concept: Address shear
Gloss: The array permutation Φ_M moving the entry at address (H, D) to (H + MD, D), where H and D are two chunks viewed as vectors of m fields over Z/q^b; the shear H ← H + D plus two linear-cost updates gives an interchange.

## This page in the argument

The step: Using frames $\Phi_M$ on the role streams, the network applies the shear $H\leftarrow H+D$ on every original row, including rows of scratch roles.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet multitape Turing machine computes the exact product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in that model.; how: build two sublinear-per-level tape procedures from finite linear networks with a rank deficit, then chain the known reductions from integer product to synthetic polynomial transforms and bound every cost (on [Integer multiplication below n log n](main-theorem.md))
- Interchanging $u$-bit address chunks costs $O(Vu^\tau)$ and a simultaneous butterfly layer on $d$ chunks costs $O(Vd^{\lambda'})$, with $\tau,\lambda'<1$.; how: supply linear elementary scans, build two finite networks with a rank deficit, and turn each network into a volume-normalized recursion on tape
- Two disjoint $u$-bit address chunks of an array of volume $V$ can be interchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$.; how: factor each edge shear into lower triangular maps and $a$ smaller interchanges, run the bit network recursively on power widths with rows split among the $W$ roles, then remove the width and row restrictions (on [Fast address-chunk interchange](fast-chunk-interchange.md))
- Two chunks of $e=m^k$ radix-$q$ digits can be interchanged in $O(Ve^\tau)$ time when a preceding row field has length divisible by $W^k$.; how: split rows cyclically among the $W$ roles, apply each edge shear by smaller interchanges, run gates pointwise, read off the shear $H\leftarrow H+D$, complete the interchange, and solve the volume-normalized recurrence on a depth-first fixed-tape schedule (on [Power-width interchange recursion](power-width-interchange.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Lexicographic array layout and logical volume](array-layout.md): Arrays on address sets [a₁]×…×[a_t] stored in lexicographic order with implicit addresses, address permutations acting on entry positions, rows as contiguous suffix blocks, and V the number of stored data bits.
  Shown as: Address shear *<predicate>* Lexicographic array layout and logical volume
- [Controlled shifts and rational scalings](controlled-shifts.md): Linear-time updates y ↦ y + a(controls) mod q^b of an address field by an offset computed from earlier fields, and multiplication of the field by fixed rational units, implemented by splitting and re-merging blocks.
  Shown as: Address shear *<predicate>* Controlled shifts and rational scalings

## Pages that build on this one

- Rational shear interface of the bit network: Assigning projection matrices P_U to the bit network's labels so that every routed role sees the endpoint shear I_m, while the edge differences have total rational rank s_b < W_b m.
- Cost of a rational matrix shear: A shear (H, D) ↦ (H + AD, D) by a rational matrix of rank a is performed with exactly a interchanges of field pairs plus O(V) triangular work.

## Other pages you may link to

- [Exact integer multiplication on a multitape machine](integer-multiplication-problem.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Normalized butterfly H₀](normalized-butterfly.md)
- [Gaussian dyadic numbers and fixed-point grids](gaussian-dyadics.md)
- [Signed Kronecker packing](signed-packing.md)
- [n log n optimality conjecture](nlogn-conjecture.md)
- [Elementary stream operations](elementary-streams.md)
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
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
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

- "For a matrix $M$, the frame $\Phi_M$ moves the array entry at $(H,D)$ to $(H+MD,D)$, leaving the other address fields unchanged." (paper)

  > In the tape application, two address chunks are written as vectors $H,D$ of $m$ fields. For a matrix $M$, the frame $\Phi_M$ moves the array entry at $(H,D)$ to $(H+MD,D)$, leaving the other address fields unchanged. The fields use a radix coprime to the fixed denominators, and addition is modulo their common range. Hence $\Phi_M$ is an invertible $\mathbb F_2$-linear permutation of array entries, and $\Phi_{M'}\Phi_M=\Phi_{M'+M}$. Using $D_v=\Phi_{M_v}$ in \eqref{eq:common-frame-identity}, the endpoint matrix difference on each routed role is exactly the shear applied to that role. The following identity makes it the same shear $H\gets H+D$ on every role; Section~\ref{sec:tape-interchange} turns that shear into a field interchange and implements an edge change with one smaller interchange per unit of its rational rank.

- "Two further linear-cost address updates complete their interchange." (paper)

  > For the bit procedure, that endpoint operator is an address shear: two fields, written as vectors $H,D$ over a common residue ring, are updated by $(H,D)\mapsto(H+D,D)$. Two further linear-cost address updates complete their interchange. For the numerical procedure, the endpoint operator becomes the simultaneous $H_0$ layer after diagonal phase operations and a dyadic scale. The intermediate frames are chosen so that every edge can be implemented by smaller calls to the same procedure.


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

Write the body to `exegenius/tasks/0014-write-address-shear.answer.md` and the JSON to `exegenius/tasks/0014-write-address-shear.answer.json`, then run `exegenius submit 0014-write-address-shear` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0014-write-address-shear`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
