# exegenius task 0011-write-subset-network

Project directory: `/home/user/openai-nlogn-wiki/runs/B1` (paths below are relative to it)

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

For these sources: The reader has done an undergraduate computer science degree: asymptotic analysis and recurrences, basic algorithms (including schoolbook and Karatsuba multiplication and the idea of the FFT), discrete mathematics (modular arithmetic, primes, the Chinese remainder theorem, permutations, bit operations), and first-year linear algebra (matrices, rank, invertibility, subspaces). They know complex numbers, polynomials and basic Turing machines with tapes. They have not studied abstract algebra beyond rings as a name, tensor products, Nussbaumer or Schönhage–Strassen transforms, or any research-level multiplication algorithm.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Schönhage–Strassen n log n optimality conjecture
  - $n$ (input length): The number of bits in each input integer.
- Multiplication as convolution of digit lists
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The indeterminate of the polynomials.
  - $r$ (ring degree): The number of complex coefficients in a polynomial, a power of two.
- Chinese-remainder address map onto prime axes
- Linear networks with roles and frames
- Elementary scans and controlled shifts
- Logarithms and iterated logarithms (also: lg, log base 2, log n, lg n)
- Binary representation and bit operations (also: bits, XOR, bit position, binary expansion, radix representation)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, quadratic multiplication, Karatsuba)
- Fast Fourier transform algorithm (also: FFT, Cooley-Tukey, fast Fourier transform)
- Convolution (also: cyclic convolution, product of coefficient sequences, polynomial multiplication as convolution)
- Modular arithmetic and congruences (also: mod, residues, congruence classes, cyclic group Z/n)
- Primes and coprimality (also: distinct primes, relatively prime, gcd, greatest common divisor, prime number theorem)
- Chinese remainder theorem (also: CRT)
- Matrices, rank and invertibility (also: linear maps, matrix product, invertible matrix, lower triangular matrix, matrix rank, identity matrix)
- Vector spaces and subspaces (also: change of basis, linear subspace, linear independence, basis)
- Permutations (also: permutation matrix, partial permutation, bijection of indices)
- Floor, ceiling and rounding (also: nearest integer, floor function, integer part)
- Recursion and recurrence relations (also: divide and conquer, recurrence, master theorem, recursive calls)
- Fixed-point and dyadic arithmetic (also: fixed-point numbers, dyadic rationals, truncation error, rounding error)
- Complex conjugate and modulus (also: conjugate, absolute value of complex number, Gaussian integers)
- Cartesian products and multi-indexing (also: multidimensional array, tuple indices, product of index sets)
- Linear-time scans and tape sorting (also: sorting on tapes, copying a tape, linear scan, tape reversal)
- Deterministic computation and time complexity classes (also: deterministic algorithm, running time, step count, worst-case time)
- Geometric and power-of-two parameter manipulation (also: powers of two, geometric series, exponent inequalities)

## This page

Concept: Three-element-subset finite networks
Gloss: Finite networks built from three-element subsets with nested subspaces at gates; gather/scatter and auxiliary wires cancel unwanted coefficients, giving s<Wm smaller calls.
Heading: Finite network with $s<Wm$ calls

The symbols in this page's heading denote (say so on the page):

- $s$ (number of calls): The number of smaller calls the network makes.
- $W$ (number of roles): The number of wires (roles) of the network.
- $m$ (space dimension): The dimension of the fixed space whose subspaces label the network.

## This page in the argument

The step: Three-element-subset networks with nested subspaces at the gates have total edge rank $s<Wm$ for $W$ wires and dimension $m$.

It serves these steps, from the main result down:

- Integer multiplication of $n$-bit integers takes $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$ on one fixed multitape machine.; how: reduce to digit convolution, build the fast tape and ring-transform tools bottom up, then assemble reductions, precision and cost (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- The two tape procedures, fast address interchange and simultaneous butterfly layers, exist with power savings.; how: construct each procedure from its own fixed linear network, after the elementary scans
- Two disjoint address fields of $u$ bits are interchanged in $O(Vu^\tau)$ steps for a fixed $\tau<1$ (fast address interchange).; how: build a linear network that exchanges two banks of values with restored auxiliaries, turn each edge into smaller interchanges, and recurse (on [Fast address-field interchange](address-interchange.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear networks with roles and frames](linear-network-frames.md): A fixed linear network of gates exchanging banks of values with signs, restoring auxiliary values; each wire is a role and each gate has an invertible frame so intermediate frames cancel.
  Shown as: Three-element-subset finite networks *<predicate>* Linear networks with roles and frames

## Pages that build on this one

- Recursive power saving: Recursing at parameter mf with s calls of parameter f on volume V/W adds s/W<m per level, a strict inequality that gives a power saving.
- Scratch-restoring exchange network: Eight-row schedule of copy, gather, scatter and side-injection gates adding x_S to y_S for arbitrary initial scratch values; three stages give the exchange (X,Y) → (−Y,X).

## Other pages you may link to

- [Multiplication as convolution of digit lists](convolution-reduction.md)
- [Polynomial ring modulo y^r + 1](polyring-mod.md)
- [Chinese-remainder address map onto prime axes](chinese-remainder-map.md)
- [Fixed multitape Turing machine model](multitape-model.md)
- [Schönhage–Strassen n log n optimality conjecture](nlogn-conjecture.md)
- [Elementary scans and controlled shifts](controlled-shifts.md)
- [Recursive power saving](recursive-saving.md)
- [Scratch-restoring exchange network](scalar-motif-network.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Rational matrix shear of address fields](matrix-shear.md)
- [Fast address-field interchange](address-interchange.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Established O(n log n) multiplier as subroutine](hvdh-subroutine.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Multidimensional transform](multidim-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Two-point butterfly H₀](butterfly.md)
- [Phase frames for the butterfly layer](phase-frames.md)
- [Simultaneous butterfly layers](fast-butterfly-layer.md)
- [Fixed-point precision and exact recovery](exact-recovery.md)
- [Synthetic character cancellation](synthetic-character-cancellation.md)
- [Retained frequency order and transform layout](transform-layout.md)
- [Normalized convolution over the ring](normalized-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling without executing permutations](resampling-lemma.md)
- [Tensor interface for growing dimension](tensor-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Chirp and permutation cancellation](chirp-permutation-cancellation.md)
- [Fixed rational parameter choice](parameter-choice.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Let $\mathcal T$ be the set of three-element subsets of $[h]$." (paper)

  > Put \[ h=100,\qquad v=\binom h3=161700,\qquad N=v^3=4227952113000000,\qquad m=h^3=1000000. \] Let $\mathcal T$ be the set of three-element subsets of $[h]$. There are two data banks $X_a,Y_a$, indexed by $a=(a_1,a_2,a_3)\in\mathcal T^3$. A wire carries one scalar. A gate is a fixed linear map on a specified set of wires; untouched wires retain their values. The vertices on a wire are its source, the gates that touch it in time order, and its sink; its edges join consecutive vertices. We call the name of a wire its \emph{role}, so that we can distinguish a fixed place in the network from the value currently carried there.

- "The decisive property is that the total
number $s$ of smaller calls satisfies $s<Wm$." (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.


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

Write the body to `exegenius/tasks/0011-write-subset-network.answer.md` and the JSON to `exegenius/tasks/0011-write-subset-network.answer.json`, then run `exegenius submit 0011-write-subset-network` in the project directory. If submit rejects the answer, fix the answer and submit again.
