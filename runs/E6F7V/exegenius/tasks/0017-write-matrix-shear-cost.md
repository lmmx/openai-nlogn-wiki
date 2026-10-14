# exegenius task 0017-write-matrix-shear-cost

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F7V` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, functions, permutations, modular arithmetic, primes and gcd), calculus-level analysis (limits, sums, Newton's method), first-course linear algebra (matrices, inverses, Gaussian elimination, vectors) and complex numbers up to roots of unity, algorithm analysis (recursion, recurrences, big-O with its relatives Omega, Theta, little-o) and basic Turing machines. The reader knows binary representation and bitwise operations, and the textbook schoolbook multiplication. The reader has not studied abstract algebra beyond what the existing concepts introduce (rings and quotient rings, zero divisors, group characters), number-theory estimates on primes, numerical analysis of rounding errors, fast multiplication algorithms beyond the basics, or any coding-theory or quantum-computing notation, so those are explained in the wiki.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Multiplication complexity and the n log n conjecture
- Fixed finite-alphabet multitape model
- Established O(n log n) multiplier (subroutine)
- Array order and elementary stream operations
- Controlled shifts
- Subspaces, orthogonality and rank
- Linear network exchanging two banks with restored scratch values
- Frames: changing the representation along a network
- Subspace labels from three-element subsets
- Rank deficit s < W m
- Recursive power saving from the rank deficit
- Lower-triangular (Bruhat) factorization
- Address shear from the bit network
- Asymptotic notation beyond big-O (also: Omega, Theta, little-o, Ω(f), Θ(f), o(f), liminf, limit of a ratio, asymptotic lower bound, asymptotic equivalence)
- Logarithms, exponentials, floor and ceiling (also: lg, log base 2, log2, natural logarithm, ln, floor, ceiling, ⌊x⌋, ⌈x⌉, powers of two, iterated logarithm)
- Binary representation and bitwise operations (also: binary numbers, positional notation, radix representation, base-b digits, most significant bit, bit string, XOR, exclusive or, bitwise addition mod 2, two's complement, leading zeroes, carry)
- Schoolbook integer arithmetic (also: grade-school multiplication, long multiplication, long division, quadratic-time multiplication, integer division with remainder, quotient and remainder, Euclidean division)
- Modular arithmetic (also: congruence, residues, mod q, integers modulo n, ℤ/qℤ, units modulo q, modular inverse, multiplicative inverse mod q, residue ring)
- Primes, coprimality and gcd (also: prime numbers, pairwise coprime, relatively prime, greatest common divisor, gcd, extended Euclidean algorithm, Euclid's algorithm, trial division, odd prime, divisibility, prime to q)
- Sets, functions, Cartesian products and bijections (also: index set, [n] = {0,...,n-1}, product set, Cartesian product, injective surjective bijective, inverse map, indexing, lexicographic order, mixed-radix index)
- Permutations (also: permutation of positions, bit-reversal permutation, involution, composition of permutations, permutation matrix, cyclic shift, swap, partial permutation)
- Matrices and linear maps (also: matrix multiplication, identity matrix, invertible matrix, matrix inverse, transpose, matrix transposition, Gaussian elimination, row operations, linear operator, diagonal matrix, lower triangular matrix, GL(m), row-major order, linearity)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2πi/n}, character sum, sum of roots of unity vanishes, geometric sum of roots of unity)
- Summation, geometric series and products (also: sigma notation, geometric sum, geometric series, arithmetic series, sum of a geometric progression, product notation, telescoping sum, telescoping)
- Recursion and divide-and-conquer recurrences (also: recurrence relation, master theorem, recursion depth, solving recurrences, recursive call, unrolling a recurrence, divide and conquer)
- Worst-case running time and subroutines (also: deterministic algorithm, worst-case time, black box, subroutine call, reduction, time complexity, exact computation, bit complexity, depth-first schedule)
- Triangle inequality and norms (also: triangle inequality, absolute value of a sum, max norm, sup norm, operator norm, |z+w| ≤ |z|+|w|, error bound, absolute error)
- Rational numbers and rounding (also: fractions, dyadic rational, rounding to nearest integer, truncation toward zero, denominator, reals, real and imaginary parts)
- Newton's method (also: Newton iteration, Newton-Raphson, quadratic convergence, reciprocal iteration, square root iteration)
- Tapes, scanning and sorting as basic machine procedures (also: scan a tape, linear scan, copying a tape, merge, sorting, work tape, head movement, tape reversal)

## This page

Concept: Cost of a rational matrix shear
Gloss: For a rational matrix A of rank a, the shear (H,D) ↦ (H+AD,D) over ℤ/q^bℤ is done with exactly a interchanges of b-digit fields and O(V) other work, using triangular updates as controlled shifts.

## This page in the argument

The step: For a rational matrix $A$ of rank $a$, the shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ is performed with exactly $a$ interchanges of $b$-digit fields and $O(V)$ other work.
How: Factor $A=E_1\Pi E_2$, apply the triangular factors as controlled shifts in descending physical order, and turn each one in $\Pi$ into three updates around a single field interchange.
Why: A lower triangular change of coordinates updates each field from earlier fields only, which is exactly the direction in which a controlled shift is linear time on tape; so everything except the pivots is linear, and the pivots are the only recursive calls. (the sources say so: "earlier fields in linear time.  Lower triangular changes of coordinates" (paper))

Its sub-steps, in order:

- A lower triangular transformation of $H$, or of $D$, costs $O(V)$ by controlled shifts in descending physical order.
- Each one in $\Pi$ is realised by $D_j\leftarrow D_j+H_i$, an interchange of $H_i$ and $D_j$, and $D_j\leftarrow H_i-D_j$, giving $H_i\leftarrow H_i+D_j$.
- The sequence uses just one interchange per one of $\Pi$, so the number of recursive calls is the rational rank $a$.

It serves these steps, from the main result down:

- One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Build the two accelerated tape procedures (address interchange and simultaneous butterfly layers), use them inside synthetic transforms and Gaussian resampling to compute a convolution, assemble the multiplication algorithm with exact recovery, and total the cost. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Two tape procedures cost less than a pass per level: interchanging two disjoint $u$-bit address fields of a volume-$V$ array costs $O(Vu^\tau)$ and a simultaneous butterfly layer on $D\le d$ chunks costs $O(Vd^{\lambda'})$, for fixed $\tau,\lambda'<1$.; how: Give each procedure its own fixed linear network that exchanges two banks of values and restores all scratch values, with total number $s$ of smaller calls below $Wm$, then run the network recursively on role streams of volume $V/W$ (interchange of address fields first, numerical layers second).
- Two disjoint contiguous address fields of $u$ bits (any width, any gaps, even one-bit payload) in an array of volume $V$ are interchanged in $O(Vu^\tau)$ time for a fixed $\tau=1-2^{-50}<1$; the intermediate steps are XOR combinations although the result is an exact permutation.; how: Interchange fields of power width $m^k$ recursively by the bit network with shears as edges, then reduce arbitrary widths to power widths by peeling off high digits to make rows, padding the row count, and splitting the width in base $m$. (on [Address-chunk interchange in time O(V u^τ)](arbitrary-width-interchange.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.2.1, S2.2.2, S2.2.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.2.1**: A lower triangular transformation of $H$, or of $D$, costs $O(V)$ by controlled shifts in descending physical order.
Source: "A lower triangular transformation of $H$, or of $D$, costs $O(V)$:" (paper)
> A lower triangular transformation of $H$, or of $D$, costs $O(V)$: update coordinates in descending physical order. At coordinate $i$, multiply by its diagonal unit and add a fixed linear combination of earlier coordinates. These earlier coordinates still have their original values. Apply Lemma~\ref{lem:ordered-affine-streams}; the number of coordinates is the fixed number $m$. Inverses are also lower triangular.

**S2.2.2**: Each one in $\Pi$ is realised by $D_j\leftarrow D_j+H_i$, an interchange of $H_i$ and $D_j$, and $D_j\leftarrow H_i-D_j$, giving $H_i\leftarrow H_i+D_j$.
Source: "D_j\leftarrow D_j+H_i,\qquad" (paper)
> For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, then add $\Pi D$ to $H$, and finally transform $H$ by $E_1$ and $D$ by $E_2^{-1}$. Each one in position $(i,j)$ of $\Pi$ calls for $H_i\leftarrow H_i+D_j$. Implement it by \[ D_j\leftarrow D_j+H_i,\qquad (H_i,D_j)\leftarrow(D_j,H_i),\qquad D_j\leftarrow H_i-D_j. \] The first and last updates target a later field controlled by an earlier field. On an initial pair $(h,d)$ this sequence yields $(h+d,d)$. It uses just one interchange. There are $a$ ones, which proves the claim. In particular, the number of recursive calls is the rational rank $a$; temporary tapes used for the other operations do not multiply that count. \end{proof}

**S2.2.3**: The sequence uses just one interchange per one of $\Pi$, so the number of recursive calls is the rational rank $a$.
Source: "It uses just one interchange.  There are $a$ ones, which proves the" (paper)
> For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, then add $\Pi D$ to $H$, and finally transform $H$ by $E_1$ and $D$ by $E_2^{-1}$. Each one in position $(i,j)$ of $\Pi$ calls for $H_i\leftarrow H_i+D_j$. Implement it by \[ D_j\leftarrow D_j+H_i,\qquad (H_i,D_j)\leftarrow(D_j,H_i),\qquad D_j\leftarrow H_i-D_j. \] The first and last updates target a later field controlled by an earlier field. On an initial pair $(h,d)$ this sequence yields $(h+d,d)$. It uses just one interchange. There are $a$ ones, which proves the claim. In particular, the number of recursive calls is the rational rank $a$; temporary tapes used for the other operations do not multiply that count. \end{proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Lower-triangular (Bruhat) factorization](lower-triangular-factorization.md): Every rational matrix of rank a factors as E₁ΠE₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.
  Shown as: Cost of a rational matrix shear *<predicate>* Lower-triangular (Bruhat) factorization
- [Controlled shifts](controlled-shifts.md): A target address field is cyclically shifted (or multiplied by a fixed unit modulo q^b) by an offset computed from control fields that precede it, in O(V) time by splitting each fibre in two pieces and merging them in reverse order.
  Shown as: Cost of a rational matrix shear *<predicate>* Controlled shifts
- [Address shear from the bit network](bit-shear-interface.md): Using the permutation frame Φ_M that moves the entry at (H,D) to (H+MD,D), the bit network's endpoint matrices differ by the identity, so it implements the shear H ← H+D on every role, with total edge rank s_b < W_b·m.
  Shown as: Cost of a rational matrix shear *<predicate>* Address shear from the bit network

## Pages that build on this one

- Recursive power-width address interchange: Two address chunks of m^k digits are interchanged in O(V e^τ) by splitting rows into W role streams, running the bit network whose edges are shears (smaller interchanges), and finishing with D←D−H, H←H+D, D←H−D; a depth-first schedule on fixed tapes realizes the recursion.

## Other pages you may link to

- [Multiplication complexity and the n log n conjecture](nlogn-history.md)
- [Fixed finite-alphabet multitape model](fixed-tape-model.md)
- [Established O(n log n) multiplier (subroutine)](established-multiplier.md)
- [Array order and elementary stream operations](stream-operations.md)
- [Subspaces, orthogonality and rank](linear-algebra-prelims.md)
- [Linear network exchanging two banks with restored scratch values](xor-linear-network.md)
- [Subspace labels from three-element subsets](subset-labels.md)
- [Frames: changing the representation along a network](frames.md)
- [Rank deficit s < W m](rank-deficit.md)
- [Recursive power saving from the rank deficit](power-saving-recurrence.md)
- [Recursive power-width address interchange](power-width-interchange.md)
- [Address-chunk interchange in time O(V u^τ)](arbitrary-width-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Fixed-point complex coefficients and truncation](fixed-point-disk.md)
- [Signed packing of ring products](signed-packing-product.md)
- [Contractions and error accounting](error-accounting.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly](butterfly.md)
- [Complex phase network and two-point kernels](phase-frame-network.md)
- [Simultaneous butterfly layer in time O(V d^λ′)](simultaneous-butterfly-layer.md)
- [Cyclic convolution and the convolution theorem](cyclic-convolution.md)
- [Multidimensional transforms and convolutions](multidimensional-dft.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Retained (bit-reversed) frequency order](retained-frequency-order.md)
- [Transform layout and cost](transform-layout.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Tensor resampling on the padded box](padded-box-tensor-resampling.md)
- [Retained permutations and their cancellation](permutation-cancellation.md)
- [Integer multiplication as radix-digit convolution](radix-digit-convolution.md)
- [Chinese-remainder map to prime cyclic axes](crt-map.md)
- [Parameter choices and prime axis lengths](prime-axis-parameters.md)
- [Coefficient twist from cyclic to negacyclic](phase-twist.md)
- [Computed source transform](source-transform.md)
- [Precision budget and exact recovery](exact-recovery.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound and power margins](cost-accounting.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "(H,D)\longmapsto(H+AD,D)" (paper)

  > \begin{lemma}[The cost of a rational matrix shear] \label{lem:matrix-shear} Let $\mathcal A$ be a fixed finite collection of rational $m\times m$ matrices. There is a fixed odd prime $q$ such that the following holds. Let $H=(H_1,\ldots,H_m)$ and $D=(D_1,\ldots,D_m)$ be two ordered groups of fields, every field ranging over $[q^b]$, with every $H_i$ before every $D_j$. For $A\in\mathcal A$ of rational rank $a$, the permutation \[ (H,D)\longmapsto(H+AD,D) \quad\text{over }\mathbb Z/q^b\mathbb Z \] can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work. Every interchange is between an $H$ field and a $D$ field. Spectators between any of the formal fields are allowed. \end{lemma}

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

Write the body to `exegenius/tasks/0017-write-matrix-shear-cost.answer.md` and the JSON to `exegenius/tasks/0017-write-matrix-shear-cost.answer.json`, then run `exegenius submit 0017-write-matrix-shear-cost` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0017-write-matrix-shear-cost`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
