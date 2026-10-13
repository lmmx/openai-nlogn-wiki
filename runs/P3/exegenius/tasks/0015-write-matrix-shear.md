# exegenius task 0015-write-matrix-shear

Project directory: `/home/user/openai-nlogn-wiki/runs/P3` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: fluent with big-O and basic algorithm analysis (recurrences, divide and conquer, sorting and merging, schoolbook multiplication), discrete mathematics (sets, binomial coefficients, permutations, modular arithmetic, primes, gcd), and introductory linear algebra and complex numbers including roots of unity and polynomial arithmetic. They have seen single-tape and multitape Turing machines and tapes as a cost model, but not the discrete Fourier transform, FFT, fast integer multiplication, abstract algebra beyond residues, number-theoretic estimates such as the prime number theorem, or any research-level multiplication technique.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Integer multiplication complexity and the n log n conjecture
- Subspaces, rank, orthogonal complements and bilinear forms
- Arrays on tape and elementary stream operations
- Controlled cyclic shifts and fixed rational scalings
- Linear exchange network with restored scratch wires (also: finite network)
- Three-element-subset gather/scatter gadget
- Frames: changing the representation along network edges
- Subspace labels and the rank saving s < Wm
  - $s$ (total rank): The sum over all network edges of the rank of the frame difference, equal to the number of smaller calls needed.
  - $W$ (wire count): The number of wires, including scratch wires, in the fixed network.
  - $m$ (label dimension): The dimension of the fixed space whose subspaces label the gates.
- Bit network and the address shear
- Lower-triangular (Bruhat) factorization (also: Bruhat factorization)
- Complex phase network and the C kernel
- Binary representation of integers (also: binary expansion, bit string, bits, radix representation, base-b digits, val(x))
- Modular arithmetic (also: congruence, residues mod m, mod, residue ring Z/mZ, centered residue, modular inverse)
- Primes, divisibility, coprimality and gcd (also: prime numbers, relatively prime, coprime, pairwise coprime, greatest common divisor, Euclidean algorithm, extended Euclidean algorithm, trial division)
- Logarithms, floors and ceilings (also: log base 2, lg, binary logarithm, floor, ceiling, natural logarithm, powers of two)
- Divide and conquer and recurrences (also: recursion, recurrence relation, master theorem, geometric series, unrolling a recurrence, induction)
- Sorting, merging and radix sort (also: merge sort, stable sort, radix sorting, counting sort, merge, sorting by keys)
- Schoolbook multiplication and carries (also: long multiplication, grade-school multiplication, carry propagation, quadratic multiplication, Karatsuba)
- Permutations (also: permutation of coordinates, bijection, reordering, partial permutation, transposition, inverse permutation)
- Sets, subsets and binomial coefficients (also: n choose k, binomial coefficient, counting subsets, cardinality, intersection of sets, indicator vector, ground set)
- XOR and mod 2 arithmetic (also: bitwise XOR, exclusive or, GF(2) addition, addition mod 2, bitwise operations, F2 arithmetic)
- Hamming weight (also: wt(x), population count, popcount, number of one bits)
- Matrices and matrix-vector products (also: matrix multiplication, identity matrix, invertible matrix, transpose, diagonal matrix, lower-triangular matrix, Gaussian elimination, block matrix)
- Vector norms and the triangle inequality (also: maximum norm, sup norm, absolute value of a complex number, modulus, triangle inequality, operator norm)
- Lexicographic order and mixed-radix indexing (also: lexicographic order, dictionary order, row-major order, multi-index, mixed radix, Cartesian product, most significant coordinate)
- Two's complement and signed integers (also: signed integer encoding, sign-magnitude, sign extension)
- Dyadic and rational numbers (also: dyadic rational, rational numbers, fractions with power-of-two denominator, exact arithmetic)
- Euler's formula and complex conjugation (also: e^{i theta}, complex conjugate, unit circle, real and imaginary parts, Gaussian integers)
- Tape-based subroutines and stacks (also: subroutine call, call stack, program counter, work tape, scanning a tape, tape copying and reversal)
- Constant factors versus asymptotic dominance (also: little-o, Theta notation, Omega notation, o(1), for sufficiently large n, polylogarithmic, dominant term)

## This page

Concept: Cost of a rational matrix shear
Gloss: The shear (H,D)↦(H+AD,D) for a rank-a rational matrix A is done with exactly a interchanges of b-digit fields plus O(V) work, using triangular factors and three controlled updates per pivot.

## This page in the argument

The step: The shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ for a rank-$a$ rational matrix $A$ takes exactly $a$ interchanges of $b$-digit fields plus $O(V)$ work.
How: factor $A$ into lower-triangular pieces and a partial permutation, so the triangular parts become controlled shifts and each pivot costs one interchange
Why: Controlled shifts update a later field from earlier ones in linear time, so only changes of coordinates that are lower triangular in tape order are cheap; the factorization puts the whole rank into the partial permutation. (the sources say so: "can be performed entirely in this direction." (paper))

Its sub-steps, in order:

- Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with exactly $a$ ones. (on [Lower-triangular (Bruhat) factorization](triangular-factorization.md))
- Transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$ using one interchange per one of $\Pi$ between two controlled updates, and undo the triangular changes; this uses exactly $a$ interchanges and $O(V)$ further work.

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time, with $\kappa=2^{-182}$.; how: build two fast tape procedures (address interchange and simultaneous butterfly layers), use them for a fast synthetic-transform convolution over a polynomial ring, wrap that in the Gaussian-resampling, Bluestein and CRT reduction of integer multiplication, then recover the exact product and total the cost (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Interchanging two disjoint $u$-bit address fields of an array whose addresses form a complete product costs $O(Vu^\tau)$ for a fixed $\tau<1$, where $V$ is the stored volume.; how: recursion on the chunk width through the bit network's shear, first for power widths with enough rows and then for arbitrary widths (on [Chunk interchange in O(V uᵗ) time](chunk-interchange.md))
- For $e=m^k$, two disjoint chunks of $e$ radix-$q$ digits can be interchanged in $O(Ve^\tau)$ time when the row field is divisible by $W^k$, where $\tau<1$ satisfies $s/W<m^\tau$.; how: run the bit network on $W$ row-split role streams with each edge done as a matrix shear by smaller interchanges, and solve the resulting recurrence (on [Power-width chunk interchange and the recursive saving](power-width-interchange.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.1.1.2). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.1.1.2**: Transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$ using one interchange per one of $\Pi$ between two controlled updates, and undo the triangular changes; this uses exactly $a$ interchanges and $O(V)$ further work.
Source: "can be performed with exactly $a$ interchanges of pairs of $b$-digit" (paper)
> \begin{lemma}[The cost of a rational matrix shear] \label{lem:matrix-shear} Let $\mathcal A$ be a fixed finite collection of rational $m\times m$ matrices. There is a fixed odd prime $q$ such that the following holds. Let $H=(H_1,\ldots,H_m)$ and $D=(D_1,\ldots,D_m)$ be two ordered groups of fields, every field ranging over $[q^b]$, with every $H_i$ before every $D_j$. For $A\in\mathcal A$ of rational rank $a$, the permutation \[ (H,D)\longmapsto(H+AD,D) \quad\text{over }\mathbb Z/q^b\mathbb Z \] can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work. Every interchange is between an $H$ field and a $D$ field. Spectators between any of the formal fields are allowed. \end{lemma}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.1.1.1 (on [Lower-triangular (Bruhat) factorization](triangular-factorization.md)): Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with exactly $a$ ones.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Lower-triangular (Bruhat) factorization](triangular-factorization.md): Every rational m×m matrix of rank a factors as E₁ΠE₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with exactly a ones, matching the tape order of controlled shifts.
  Shown as: Cost of a rational matrix shear *<predicate>* Lower-triangular (Bruhat) factorization
- [Controlled cyclic shifts and fixed rational scalings](controlled-shift.md): Updating a later address field y by y+a(controls) mod q^b, or multiplying it by a fixed rational unit, costs O(V) on tape by splitting each fibre in two pieces and merging them in swapped order.
  Shown as: Cost of a rational matrix shear *<predicate>* Controlled cyclic shifts and fixed rational scalings

## Pages that build on this one

- Power-width chunk interchange and the recursive saving: For chunks of e=m^k digits, running the bit network on W row-split role streams, with each edge done by smaller interchanges, gives F_k ≤ (s/W)F_{k−1}+O(1); because s/W<m^τ this yields cost O(V e^τ).

## Other pages you may link to

- [Integer multiplication complexity and the n log n conjecture](history.md)
- [Arrays on tape and elementary stream operations](stream-ops.md)
- [Subspaces, rank, orthogonal complements and bilinear forms](linear-algebra.md)
- [Linear exchange network with restored scratch wires](linear-network.md)
- [Frames: changing the representation along network edges](frames.md)
- [Three-element-subset gather/scatter gadget](subset-gadget.md)
- [Subspace labels and the rank saving s < Wm](rank-saving.md)
- [Bit network and the address shear](bit-network-shear.md)
- [Complex phase network and the C kernel](complex-phase-network.md)
- [Power-width chunk interchange and the recursive saving](power-width-interchange.md)
- [Chunk interchange in O(V uᵗ) time](chunk-interchange.md)
- [Packed addition of selected address bits](packed-bit-addition.md)
- [Polynomial ring modulo yʳ + 1](ring-mod-yr.md)
- [Fixed-point complex grid and truncation](fixed-point.md)
- [Signed packing (Kronecker substitution) of ring products](signed-packing.md)
- [Discrete Fourier transform](dft.md)
- [Butterfly (decimation-in-frequency) transform](butterfly-fft.md)
- [Phase frames reduce a butterfly layer to C kernels](phase-frame-reduction.md)
- [Simultaneous butterfly layer in O(V d^λ′) time](simultaneous-layer.md)
- [Contractions and error accumulation](contraction-error.md)
- [Cyclic convolution and the convolution theorem](convolution.md)
- [Multidimensional transforms (tensor products)](multidim-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Chinese-remainder map to distinct prime axes](crt-map.md)
- [Bluestein chirp identity](bluestein.md)
- [Phase twist from cyclic to negacyclic wrap](phase-twist.md)
- [Synthetic transform layout and retained frequency order](transform-layout.md)
- [Normalized convolution over the ring from the retained layout](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling with the permutations left in the transform](retained-permutations.md)
- [Integer product as convolution of radix digits](integer-as-convolution.md)
- [Exact recovery by rounding and carry propagation](exact-recovery.md)
- [Parameter choices, padded box and prime source lengths](parameters.md)
- [Complex cyclic convolution via the coefficient twist](complex-convolution-twist.md)
- [Computed source transform](source-transform.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost table and the κ margin](cost-accounting.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "can be performed with exactly $a$ interchanges of pairs of $b$-digit" (paper)

  > \begin{lemma}[The cost of a rational matrix shear] \label{lem:matrix-shear} Let $\mathcal A$ be a fixed finite collection of rational $m\times m$ matrices. There is a fixed odd prime $q$ such that the following holds. Let $H=(H_1,\ldots,H_m)$ and $D=(D_1,\ldots,D_m)$ be two ordered groups of fields, every field ranging over $[q^b]$, with every $H_i$ before every $D_j$. For $A\in\mathcal A$ of rational rank $a$, the permutation \[ (H,D)\longmapsto(H+AD,D) \quad\text{over }\mathbb Z/q^b\mathbb Z \] can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work. Every interchange is between an $H$ field and a $D$ field. Spectators between any of the formal fields are allowed. \end{lemma}


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

Write the body to `exegenius/tasks/0015-write-matrix-shear.answer.md` and the JSON to `exegenius/tasks/0015-write-matrix-shear.answer.json`, then run `exegenius submit 0015-write-matrix-shear` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0015-write-matrix-shear`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
