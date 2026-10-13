# exegenius task 0025-write-address-interchange

Project directory: `/home/user/openai-nlogn-wiki/runs/D3` (paths below are relative to it)

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

For these sources: The reader is an undergraduate in computer science who has taken discrete mathematics, algorithms and a theory-of-computation course, with linear algebra and basic probability or number theory. They know asymptotic analysis, divide-and-conquer recurrences, binary and positional number representations, modular arithmetic, and sets and functions, and have met the idea of a fast Fourier transform and the n log n multiplication story at most informally. They have not studied finite fields, abstract algebra beyond basics, numerical error analysis, or the specialist literature on multiplication algorithms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Convolution and radix-digit reduction
- Discrete Fourier transform
- Schönhage–Strassen n log n conjecture and history
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The polynomial variable whose powers serve as roots of unity.
  - $r$ (ring degree): The number of coefficients in a polynomial, a power of two.
- Synthetic polynomial transforms
- Address rearrangement cost on tapes
- Gaussian resampling
- Chinese-remainder map to prime cyclic axes
- Bluestein chirp identity
- Coefficient twist to the polynomial ring
- Signed packing (Kronecker substitution)
- Linear networks, roles and frames
- Finite network via three-element subsets and nested subspaces
- Recursive saving from s < Wm
- Elementary stream operations and controlled shifts
- Scalar gates with restored scratch wires
- Rank budget of the network labels
- Bit and complex network interfaces
- Lower triangular factorization and matrix shear
- Power-width and arbitrary-width chunk interchange
- Linear algebra over the reals and rationals (also: matrices, vector spaces, subspaces, linear maps, invertible matrix, rank, dimension, linear combination)
- Modular arithmetic and congruences (also: mod, residues, congruence classes, Z/nZ)
- Primes, coprimality and gcd (also: prime numbers, relatively prime, greatest common divisor, distinct primes)
- Binary representation and bit operations (also: bits, XOR, binary expansion, two's complement, most significant bit, bitwise exclusive or)
- Radix (base-b) positional representation (also: digits in base b, radix digits, base expansion)
- Floor, ceiling and logarithms (also: lg, log base 2, floor function, ceiling function)
- Schoolbook multiplication (also: grade-school multiplication, quadratic multiplication)
- Divide-and-conquer recurrences (also: recursion, recurrence relations, master theorem)
- Fixed-point arithmetic and rounding error (also: fixed-point numbers, rounding, approximation error, absolute error, sup norm)
- Complex exponential and unit roots (also: Euler's formula, e^{2 pi i/N}, primitive root of unity, unit circle)
- Cyclic groups and cyclic indexing (also: indices mod n, cyclic wraparound, cyclic convolution, Z_n)
- Cartesian products and multidimensional arrays (also: tensor indexing, multi-index, array axes, lexicographic order)
- Permutations (also: bijections, rearrangement of indices)
- Gaussian elimination and triangular matrices (also: lower triangular matrix, LU factorization)
- Gaussian function (also: normal density, e^{-x^2})
- Time complexity and reductions (also: worst-case running time, reduction, linear-time scan, sorting cost)
- Basic induction and proof by contradiction (also: induction, proof technique)
- Basic set notation and counting (also: subsets, cardinality, binomial coefficients, pigeonhole)
- Fast Fourier transform idea (also: FFT, Cooley-Tukey, divide-and-conquer DFT)

## This page

Concept: Fast address-field interchange
Gloss: Interchanges two address fields of u bits at cost O(V u^τ), τ<1, through XOR combinations of data, with the final result an exact permutation.

## This page in the argument

The step: Two address fields of $u$ bits are interchanged at cost $O(Vu^\tau)$ with $\tau<1$.
How: apply the recursive network to address shears, then to chunk interchange
Why: Ordinary scanning pays one pass per level; the network turns the interchange into shears whose cost obeys the strict recursion. (the sources leave this for the reader to work out: spell it out)
Striking feature: Intermediate steps form XOR combinations of data, yet the final result is an exact permutation for arbitrary auxiliary values. (explain why it holds, from the method)

Its sub-steps, in order:

- Any rational matrix of rank $a$ factors as $E_1\Pi E_2$ with lower triangular $E_1,E_2$, so the shear $(H,D)\mapsto(H+AD,D)$ needs exactly $a$ field interchanges plus linear work. (on [Lower triangular factorization and matrix shear](matrix-shear.md))
- Two address chunks of width $e=m^k$ are interchanged in $O(Ve^\tau)$, and then chunks of arbitrary width $u$ are interchanged by decomposition. (on [Power-width and arbitrary-width chunk interchange](chunk-swap.md))

It serves these steps, from the main result down:

- Two $n$-bit integers can be multiplied exactly on a fixed finite-tape machine in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.; how: reduce multiplication to convolution, build two fast tape procedures whose recursion has a strict rank saving, and assemble the transforms into an exact product (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Two tape procedures, a fast address-field interchange and fast simultaneous butterfly layers, beat the $\Theta(n\log n)$ cost of scanning.; how: show that scanning is too expensive, then build both procedures from one network

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Recursive saving from s < Wm](recursive-power-saving.md): Calls at parameter mf use s calls at parameter f on volume V/W; s/W<m strictly gives a power-saving cost.
  Shown as: Fast address-field interchange *<predicate>* Recursive saving from s < Wm
- [Address rearrangement cost on tapes](tape-address-rearrangement.md): Moving data between address fields on tapes costs a scan per level; naive scanning gives Θ(n log n) over Θ(log n) levels.
  Shown as: Fast address-field interchange *<predicate>* Address rearrangement cost on tapes
- [Power-width and arbitrary-width chunk interchange](chunk-swap.md): Recurrence on parameter e=m^k gives chunk interchange in O(V e^τ); then arbitrary width u by decomposition.
  Shown as: Fast address-field interchange *<predicate>* Power-width and arbitrary-width chunk interchange

## Pages that build on this one

- Synthetic transform layout and cost: Layout of the synthetic transform over R_r with truncation Q_p, contractions, and stored frequency order retained through pointwise product; cost via simultaneous layers.
- Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape multiplication of n-bit integers in O(n(lg n)^{1−κ}), κ=2^{-182}, disproving the n log n conjecture in this model.

## Other pages you may link to

- [Convolution and radix-digit reduction](convolution.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-y-r-1.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Coefficient twist to the polynomial ring](phase-twist.md)
- [Fixed multitape Turing machine model](multitape-model.md)
- [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md)
- [Linear networks, roles and frames](linear-network-frames.md)
- [Finite network via three-element subsets and nested subspaces](finite-network-subspaces.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Elementary stream operations and controlled shifts](elementary-streams.md)
- [Scalar gates with restored scratch wires](scalar-motifs.md)
- [Rank budget of the network labels](motif-residuals.md)
- [Bit and complex network interfaces](motif-interfaces.md)
- [Lower triangular factorization and matrix shear](matrix-shear.md)
- [Packed selected-bit addition on grouped rectangles](packed-selected-bit-addition.md)
- [Simultaneous butterfly layers](fast-butterfly-layer.md)
- [Precision and exact recovery](precision-exact-recovery.md)
- [Synthetic transform layout and cost](transform-layout-cost.md)
- [Tensor resampling with retained permutations](tensor-resampling.md)
- [Fixed rational parameter choice and cost table](parameter-choice.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The first procedure interchanges two disjoint contiguous address fields" (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.

- "The chunks can be interchanged in $O(Ve^\tau)$ time" (paper)

  > \begin{proposition}[Power-width interchange with rows] \label{prop:power-interchange} Assume the fixed circuit data satisfy \eqref{eq:finite-shear-contract}, and let $q$ be a prime as in Lemma~\ref{lem:matrix-shear} for its edge matrices, also avoiding the denominators of every assigned terminal and gate matrix $M$. Choose a rational number $\tau\in(0,1)$ with $s/W<m^\tau$. For every $e=m^k$, $k\ge0$, consider two disjoint contiguous address chunks of $e$ radix-$q$ digits each. Suppose a row field preceding both chunks has length divisible by $W^k$. There may be additional fields before and after the row field, between the chunks, and after them. The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every other address field, on a fixed number of finite-alphabet tapes. The constant is independent of all field lengths and of the data. \end{proposition}


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

Write the body to `exegenius/tasks/0025-write-address-interchange.answer.md` and the JSON to `exegenius/tasks/0025-write-address-interchange.answer.json`, then run `exegenius submit 0025-write-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0025-write-address-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
