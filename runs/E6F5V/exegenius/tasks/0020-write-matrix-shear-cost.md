# exegenius task 0020-write-matrix-shear-cost

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F5V` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, counting, induction, primes, gcd), a first algorithms course (divide and conquer, recurrences, sorting, Karatsuba multiplication, schoolbook arithmetic) and complexity (big-O family, single- and multitape Turing machines), together with calculus (exponentials, logarithms, series), linear algebra over the reals and complex numbers, and polynomials. They have not met Fourier transforms or the FFT in depth, finite fields beyond arithmetic mod 2, bilinear forms over arbitrary fields, number-theoretic estimates such as prime density, or any research-level multiplication algorithm; those are what the wiki must explain.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Binary integers
- Modular arithmetic
- Matrices, rank and linear maps
- Fixed-tape Turing machine model
- Arrays, address fields and logical volume
- Elementary stream operations
- Controlled cyclic shifts and rational scalings
- Established O(n log n) integer multiplier
- The n log n optimality conjecture
- Role networks and frames
- Restoring arbitrary scratch values
- Three-subset gather and scatter network
- Nondegenerate subspaces and orthogonal residuals
- Subspace labels and the rank budget
- Rank saving and the power-saving recurrence
- Lower-triangular factorization of a matrix
- Bit network as an address shear
- Two-point butterfly H₀ and the kernel C
- Binary phase frames
- Big-Theta, big-Omega and little-o notation (also: Theta, Omega, Θ, Ω, little-o, o(1), asymptotic notation)
- Divide-and-conquer recurrences (also: recurrence relation, master theorem, recursion tree, solving recurrences)
- Schoolbook and Karatsuba multiplication (also: long multiplication, Karatsuba, Toom-Cook, grade-school multiplication)
- Positional notation in any radix and mixed radix (also: radix-q digits, base-q representation, mixed-radix expansion, digit string, most significant digit)
- Bitwise operations, XOR and Hamming weight (also: XOR, exclusive or, addition mod 2, bit parity, wt, popcount, Hamming weight)
- Floor, ceiling and rounding (also: ⌊x⌋, ⌈x⌉, round to nearest integer, integer part)
- Exponential and logarithm functions (also: log base 2, lg, natural logarithm, ln, exp, e^x, Gaussian function)
- Convergent series and the geometric series (also: absolutely convergent sum, infinite sum, geometric series, tail bound, series convergence)
- Prime numbers, coprimality and trial division (also: relatively prime, pairwise coprime, gcd, odd prime, primality by trial division, unique factorization)
- Extended Euclidean algorithm (also: Euclid's algorithm, Bezout identity, computing modular inverses)
- Counting subsets and binomial coefficients (also: n choose k, binomial coefficient, k-subsets, inclusion-exclusion, ground set)
- Permutations and permutation matrices (also: bijection of indices, reordering of coordinates, involution, permutation of positions, partial permutation)
- Lexicographic order and Cartesian products of index sets (also: lexicographic order, product of ranges, multi-index, tuple addressing, row-major order)
- Vector norms, inner products and orthogonality (also: maximum norm, sup norm, infinity norm, triangle inequality, dot product, orthonormal basis, orthogonal complement, isometry)
- Gaussian elimination (also: row reduction, row operations, elementary matrices, echelon form)
- Dyadic rationals and binary fractions (also: dyadic numbers, numbers m/2^k, binary point, fixed-point numbers, Gaussian dyadics, Gaussian integers)
- Stable radix sort and counting sort (also: bit sorting, stable sorting, radix sorting, sorting by a key digit)
- Mathematical induction (also: induction on k, proof by induction, recursive construction)

## This page

Concept: Cost of a rational matrix shear
Gloss: The address map (H,D) ↦ (H + A D, D) over Z/q^b is performed with exactly rank(A) interchanges of b-digit fields plus linear work, using triangular steps and the trick that three updates turn H+D into a swap.

## This page in the argument

The step: The address map $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ is performed with exactly $\operatorname{rank}(A)$ interchanges of $b$-digit fields plus $O(V)$ further work.
How: Factor $A=E_1\Pi E_2$, perform the triangular factors by controlled shifts, and turn each one of $\Pi$ into a single interchange.
Why: Lower triangular changes of coordinates update each later field from earlier ones, which is the direction in which controlled shifts run in linear time. (the sources say so: "Lower triangular changes of coordinates can be performed entirely in this direction." (paper))

Its sub-steps, in order:

- A lower triangular transformation of the fields $H$ or $D$ costs $O(V)$ by updating coordinates in descending order.
- For $A=E_1\Pi E_2$ transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$, and undo the transformations.
- The sequence $D_j\leftarrow D_j+H_i$, swap, $D_j\leftarrow H_i-D_j$ yields $(h+d,d)$ with just one interchange.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, using fast address interchange and fast simultaneous butterfly layers inside a Gaussian-resampling, chirp and synthetic-transform reduction.; how: Reduce the product to a convolution evaluated through Gaussian-resampled, chirped synthetic transforms, make the two costly tape operations (address movement and butterfly layers) cheaper by a power of the logarithm using networks with a rank saving, and then assemble the algorithm and add up its costs. (on [Integer multiplication below n log n](main-theorem.md))
- Two disjoint address chunks of $u$ bits in an array with complete Cartesian address set can be exchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$, although the intermediate steps form XOR combinations of the data.; how: Realize the exchange as a shear $H\leftarrow H+D$ run through the bit network on $W$ role streams, with each edge shear done by smaller interchanges, and then remove the restrictions on width and rows. (on [Fast interchange of address chunks](chunk-interchange.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.2.1, S4.2.2, S4.2.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.2.1**: A lower triangular transformation of the fields $H$ or $D$ costs $O(V)$ by updating coordinates in descending order.
Source: "A lower triangular transformation of $H$, or of $D$, costs $O(V)$:" (paper)
> A lower triangular transformation of $H$, or of $D$, costs $O(V)$: update coordinates in descending physical order. At coordinate $i$, multiply by its diagonal unit and add a fixed linear combination of earlier coordinates. These earlier coordinates still have their original values. Apply Lemma~\ref{lem:ordered-affine-streams}; the number of coordinates is the fixed number $m$. Inverses are also lower triangular.

**S4.2.2**: For $A=E_1\Pi E_2$ transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$, and undo the transformations.
Source: "For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$," (paper)
> For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, then add $\Pi D$ to $H$, and finally transform $H$ by $E_1$ and $D$ by $E_2^{-1}$. Each one in position $(i,j)$ of $\Pi$ calls for $H_i\leftarrow H_i+D_j$. Implement it by \[ D_j\leftarrow D_j+H_i,\qquad (H_i,D_j)\leftarrow(D_j,H_i),\qquad D_j\leftarrow H_i-D_j. \] The first and last updates target a later field controlled by an earlier field. On an initial pair $(h,d)$ this sequence yields $(h+d,d)$. It uses just one interchange. There are $a$ ones, which proves the claim. In particular, the number of recursive calls is the rational rank $a$; temporary tapes used for the other operations do not multiply that count. \end{proof}

**S4.2.3**: The sequence $D_j\leftarrow D_j+H_i$, swap, $D_j\leftarrow H_i-D_j$ yields $(h+d,d)$ with just one interchange.
Source: "On an initial pair $(h,d)$ this sequence yields $(h+d,d)$." (paper)
> For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, then add $\Pi D$ to $H$, and finally transform $H$ by $E_1$ and $D$ by $E_2^{-1}$. Each one in position $(i,j)$ of $\Pi$ calls for $H_i\leftarrow H_i+D_j$. Implement it by \[ D_j\leftarrow D_j+H_i,\qquad (H_i,D_j)\leftarrow(D_j,H_i),\qquad D_j\leftarrow H_i-D_j. \] The first and last updates target a later field controlled by an earlier field. On an initial pair $(h,d)$ this sequence yields $(h+d,d)$. It uses just one interchange. There are $a$ ones, which proves the claim. In particular, the number of recursive calls is the rational rank $a$; temporary tapes used for the other operations do not multiply that count. \end{proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Lower-triangular factorization of a matrix](lower-triangular-factorization.md): Every rational matrix A of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones (a Bruhat-type factorization in reversed coordinate order).
  Shown as: Cost of a rational matrix shear *<predicate>* Lower-triangular factorization of a matrix
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md): A later target field can be shifted cyclically by an offset computed from earlier control fields, or multiplied by a unit modulo q^b, in linear time by splitting and merging blocks.
  Shown as: Cost of a rational matrix shear *<predicate>* Controlled cyclic shifts and rational scalings

## Pages that build on this one

- Power-width address interchange: Two chunks of m^k radix-q digits are interchanged by splitting rows into W role streams, running the bit network with each edge shear done by recursive interchanges of chunks of 1/m the width, in O(V e^τ) time on fixed tapes.

## Other pages you may link to

- [Two-point butterfly H₀ and the kernel C](two-point-butterfly.md)
- [Fixed-tape Turing machine model](multitape-model.md)
- [Established O(n log n) integer multiplier](nlogn-multiplier.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Arrays, address fields and logical volume](array-layout.md)
- [Role networks and frames](gate-network-frames.md)
- [Elementary stream operations](elementary-streams.md)
- [Restoring arbitrary scratch values](scratch-restoration.md)
- [Three-subset gather and scatter network](subset-intersection-network.md)
- [Nondegenerate subspaces and orthogonal residuals](nondegenerate-subspaces.md)
- [Subspace labels and the rank budget](subspace-labels.md)
- [Rank saving and the power-saving recurrence](rank-saving-recurrence.md)
- [Bit network as an address shear](bit-network-interface.md)
- [Binary phase frames](phase-interface.md)
- [Power-width address interchange](power-width-interchange.md)
- [Fast interchange of address chunks](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Multidimensional transforms and convolution on several axes](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Decimation-in-frequency butterflies and bit-reversed frequency order](butterfly-recursion.md)
- [Fixed-point complex arithmetic and truncation error](fixed-point-numerics.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout and cost](transform-layout.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Cancellation of the retained source permutation](permutation-cancellation.md)
- [Tensor resampling on a padded box](tensor-resampling-box.md)
- [Choosing prime source lengths](prime-lengths.md)
- [Size parameters of the multiplication](size-parameters.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Phase twist from cyclic to negacyclic](coefficient-twist.md)
- [Source Fourier transform procedure](source-transform.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Precision and exact recovery](exact-recovery.md)
- [Cost table and the saving exponent κ](time-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work." (paper)

  > \begin{lemma}[The cost of a rational matrix shear] \label{lem:matrix-shear} Let $\mathcal A$ be a fixed finite collection of rational $m\times m$ matrices. There is a fixed odd prime $q$ such that the following holds. Let $H=(H_1,\ldots,H_m)$ and $D=(D_1,\ldots,D_m)$ be two ordered groups of fields, every field ranging over $[q^b]$, with every $H_i$ before every $D_j$. For $A\in\mathcal A$ of rational rank $a$, the permutation \[ (H,D)\longmapsto(H+AD,D) \quad\text{over }\mathbb Z/q^b\mathbb Z \] can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work. Every interchange is between an $H$ field and a $D$ field. Spectators between any of the formal fields are allowed. \end{lemma}

- "D_j\leftarrow D_j+H_i,\qquad" (paper)

  > For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, then add $\Pi D$ to $H$, and finally transform $H$ by $E_1$ and $D$ by $E_2^{-1}$. Each one in position $(i,j)$ of $\Pi$ calls for $H_i\leftarrow H_i+D_j$. Implement it by \[ D_j\leftarrow D_j+H_i,\qquad (H_i,D_j)\leftarrow(D_j,H_i),\qquad D_j\leftarrow H_i-D_j. \] The first and last updates target a later field controlled by an earlier field. On an initial pair $(h,d)$ this sequence yields $(h+d,d)$. It uses just one interchange. There are $a$ ones, which proves the claim. In particular, the number of recursive calls is the rational rank $a$; temporary tapes used for the other operations do not multiply that count. \end{proof}


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

Write the body to `exegenius/tasks/0020-write-matrix-shear-cost.answer.md` and the JSON to `exegenius/tasks/0020-write-matrix-shear-cost.answer.json`, then run `exegenius submit 0020-write-matrix-shear-cost` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0020-write-matrix-shear-cost`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
