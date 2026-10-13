# exegenius task 0013-write-recursive-power-saving

Project directory: `/home/user/openai-nlogn-wiki/runs/M4` (paths below are relative to it)

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

For these sources: An undergraduate computer science reader who knows asymptotic notation, algorithm analysis and recursion, discrete mathematics (modular arithmetic, primes, the Chinese remainder theorem, sets, permutations, binary representation), and first-year linear algebra (matrices, rank, invertibility, subspaces). They know polynomials and complex numbers including roots of unity, and basic multitape Turing machines. They have not met the fast Fourier transform in depth, convolution theory, Gaussian analysis, fixed-point error control, or the research literature on fast multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Convolution (also: cyclic convolution)
- Discrete Fourier transform (also: Fourier transform)
- The n log n optimality conjecture and prior bounds (also: Schönhage–Strassen conjecture)
- Reduction of integer multiplication to convolution (also: radix-digit convolution)
- Polynomial ring modulo y^r + 1 (also: C[y]/(y^r+1))
  - $y$ (ring variable): The polynomial variable whose powers serve as roots of unity.
  - $r$ (ring size): The number of complex coefficients in a polynomial of the ring, a power of two.
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms)
- Butterfly map H_0 (also: two-point butterfly)
  - $H_0$ (butterfly map): The map sending a pair (u,v) to ((u+v)/2,(u-v)/2), applied coefficientwise.
- Linear networks with roles and frames (also: roles, frames)
- Finite network from three-element subsets (also: rank-saving network)
- Logarithms and floor/ceiling (also: lg, log base 2, floor, ceiling)
- Modular arithmetic (also: congruence, residues mod n, Z/nZ)
- Prime numbers and prime powers (also: primes, prime factorization, coprime)
- Chinese remainder theorem (also: CRT)
- Roots of unity (also: nth roots of unity, primitive root of unity, Euler's formula, e^{2 pi i/n})
- Binary representation and bit operations (also: bits, XOR, bit strings, binary expansion)
- Radix (base-b) representation (also: digits in base b, positional notation)
- Schoolbook multiplication and carries (also: long multiplication, carry propagation, grade-school algorithm)
- Recursion and recurrences (also: divide and conquer, recurrence relation, recursive algorithm)
- Matrices and linear maps (also: matrix multiplication, linear transformation, invertible matrix, matrix inverse)
- Rank of a matrix (also: matrix rank, linear independence)
- Triangular matrices (also: lower-triangular matrix, LU factorization)
- Vector spaces and subspaces (also: subspace, dimension, vector space over a field)
- Rational numbers and fields (also: rationals, field, finite field)
- Permutations (also: bijection, partial permutation, index reordering)
- Multidimensional arrays (also: tensors, multi-index arrays, d-dimensional array)
- Finite sets and subsets (also: intersection, union, subset, cardinality)
- Cyclic groups (also: Z_n, cyclic indices, indices modulo n, wraparound)
- Complex magnitude and conjugate (also: absolute value of a complex number, modulus, norm)
- Fixed-point and rounding error (also: rounding, approximation error, precision, bit precision)
- Gaussian function (also: Gaussian, exp(-x^2), bell curve)
- Time and space on tapes (also: tape head movement, linear-time scan, sorting on tapes)
- Inequalities and exponent arithmetic (also: power functions, polynomial in lg n, constants in exponents)

## This page

Concept: Recursive power saving
Gloss: A recursive call at parameter m·f using s<W·m calls at parameter f on volume V/W makes the cost per volume grow as a power less than linear in the parameter.

## This page in the argument

The step: A recursive call at parameter $mf$ using $s<Wm$ calls at parameter $f$ on volume $V/W$ makes the cost per volume grow as a power $m^{\tau}$ less than linear in the parameter.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time, $\kappa=2^{-182}$.; how: reduce the product through a chain of changes of representation down to convolution over a polynomial ring, speed up the transforms with two tape procedures, then recover the exact integer (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-multiplication.md))
- Address rearrangement of a stored array of volume $V$ and the butterfly layers of the transforms can each be done in time $O(V f^{\theta})$ for a fixed $\theta<1$ in the parameter $f$, instead of linear in $f$.; how: build each procedure from a fixed linear network applied on role arrays under frames, then use a recursive call that makes $s<Wm$ smaller calls to get a power saving

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Finite network from three-element subsets](subset-network.md): A network labelled by nested subspaces built from three-element subset intersections, whose number s of smaller calls is less than W·m.
  Shown as: Recursive power saving *<predicate>* Finite network from three-element subsets

## Pages that build on this one

- Fast interchange of address chunks: Exchanging two address fields of u bits by XOR-combinations (address shears) at cost O(V u^τ) with τ<1, though the final effect is an exact permutation.
- Fast simultaneous butterfly layers: Applying the butterfly map to the same bit of up to d address chunks at once on numerical arrays, at cost O(V d^λ') with λ'<1.

## Other pages you may link to

- [The n log n optimality conjecture and prior bounds](nlogn-conjecture.md)
- [Convolution](convolution.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Reduction of integer multiplication to convolution](radix-digit-reduction.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-y-r.md)
- [Butterfly map H_0](butterfly-h0.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Linear networks with roles and frames](linear-network-frames.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Phase twist to the negacyclic ring](phase-twist.md)
- [Precision and exact recovery of the product](exact-recovery.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Elementary stream operations and controlled shifts](elementary-streams.md)
- [Rational matrix shear and triangular factorization](matrix-shear.md)
- [Fast interchange of address chunks](address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "This strict inequality" (paper)

  > A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$. The parameter counts field digits for address interchange and selected axes for a numerical layer. After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving. The later tape and arithmetic estimates preserve it, including the work of changing numerical address coordinates. Those changes are implemented by whole-chunk moves and controlled shifts, followed by a deterministic correction of the explicitly identified exceptional addresses.

- "Choose a rational number $\tau\in(0,1)$ with $s/W<m^\tau$." (paper)

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

Write the body to `exegenius/tasks/0013-write-recursive-power-saving.answer.md` and the JSON to `exegenius/tasks/0013-write-recursive-power-saving.answer.json`, then run `exegenius submit 0013-write-recursive-power-saving` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0013-write-recursive-power-saving`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
