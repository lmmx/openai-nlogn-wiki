# exegenius task 0027-write-main-result

Project directory: `/home/user/openai-nlogn-wiki/runs/B3` (paths below are relative to it)

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

For these sources: An undergraduate computer scientist who has taken discrete mathematics, linear algebra, algorithms and introductory theory of computation. They know asymptotic notation, divide-and-conquer recurrences, basic number theory (divisibility, gcd, modular arithmetic, primes, Chinese remainder theorem statement), matrices and linear maps, complex numbers and roots of unity, and simple multitape Turing machines. They have not studied the FFT-based multiplication literature in depth, Nussbaumer or Bluestein transforms, fine tape-machine permutation tricks, or finite-ring and numerical-error analysis beyond basics.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Schönhage–Strassen n log n conjecture and history
- Convolution and the discrete Fourier transform
- Multiplication as digit convolution
- Signed coefficient packing (Kronecker substitution)
- Established O(n log n) multiplier as subroutine
- Elementary stream operations on tapes
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The indeterminate of the polynomials, with y^r = -1.
  - $r$ (number of coefficients): The number of coefficients in a polynomial, a power of two.
- Synthetic polynomial transforms
- Exact normalized polynomial products
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein chirp identity
- Coefficient twist to the polynomial ring
- Linear networks, roles and frames
- Finite networks from three-element subsets
- Recursive power saving s < Wm
  - $s$ (number of smaller calls): The total number of smaller calls the network makes.
  - $W$ (number of roles): The number of roles (wires) in the network, among which rows are distributed.
  - $m$ (parameter multiplier): The dimension of the fixed space and the factor by which the recursive parameter grows per level.
- Restoring auxiliary values
- Address shear and triangular factorization
- Fast interchange of address fields
  - $V$ (stored bit volume): The number of bits stored in the array.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (exponent): A fixed constant strictly less than 1.
- Fixed-point precision and exact recovery
- Simultaneous butterfly layer H₀
  - $H_0$ (butterfly map): The map sending (u,v) to ((u+v)/2,(u-v)/2).
  - $u$ (first value): The first input value of the two-point butterfly.
  - $v$ (second value): The second input value of the two-point butterfly.
- Transform layout with retained frequency order
- Multiplication algorithm and its cost
- Modular arithmetic (also: congruence, residues mod m, bmod, remainder)
- Greatest common divisor and coprimality (also: gcd, coprime, relatively prime)
- Prime numbers (also: primes, distinct primes, prime factorization)
- Floor and ceiling functions (also: floor, ceiling, lceil, rounding)
- Binary logarithm (also: lg, log base 2, log n)
- Binary representation and bit strings (also: n-bit integers, bits, binary expansion, dyadic rationals)
- Exclusive or (also: XOR, oplus, bitwise xor)
- Matrices and linear maps (also: linear transformation, matrix product, invertible matrix, linear algebra)
- Permutations (also: bijection, permutation matrix, reordering)
- Subspaces, dimension and rank (also: rank, vector subspace, linear independence)
- Cyclic groups and rings (also: Z/mZ, integers mod m, cyclic group, ring, commutative ring)
- Cartesian products and tuples (also: product of sets, multi-index, coordinates, array indexing)
- Subsets and combinatorial counting (also: binomial coefficient, k-element subsets, triples)
- Recurrences and geometric series (also: recursion cost, telescoping sum, geometric sum)
- Inequalities and error bounds (also: triangle inequality, absolute value bound, norm, rounding error)
- Gaussian integers (also: Z[i], complex integers, integers a+bi)
- Exponents and powers (also: exponential, power of two, fractional exponent)
- Sorting and scanning arrays (also: linear scan, array order, merge sort)
- Schoolbook multiplication (also: long multiplication, grade-school multiplication, quadratic multiplication)
- Fast Fourier transform (also: FFT, Cooley-Tukey)

## This page

Concept: Integer multiplication below n log n
Gloss: A fixed deterministic multitape Turing machine multiplies two n-bit integers in O(n (lg n)^(1−κ)) worst-case time with κ = 2^−182, refuting the n log n optimality conjecture in this model.
Heading: Integer multiplication in time $n(\lg n)^{1-\kappa}$

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits in each of the two integers being multiplied.
- $\kappa$ (power saving): The fixed constant 2^{-182} giving the saving in the logarithmic factor.

## This page in the argument

The step: A fixed deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.
How: build two fast tape procedures, use them in synthetic transforms for ring convolution, then chain the reductions from integer multiplication
Why: Scanning $\Theta(n)$ bits at each of $\Theta(\log n)$ transform levels costs $n\log n$, so savings in movement and arithmetic are needed. (the sources say so: "We therefore need savings in both movement and arithmetic. Two tape" (paper))
Striking feature: The saving is a power $(\lg n)^{-\kappa}$ with the astronomically small $\kappa=2^{-182}$, forced by the strict inequality $s<Wm$ for a very large fixed network. (explain why it holds, from the method)

Its sub-steps, in order:

- Schönhage and Strassen conjectured that $n\log n$ is the optimal order of growth for multiplication, the conjecture the new bound refutes. (on [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md))
- Two tape procedures, an address interchange and a simultaneous butterfly layer, cost a power of their parameter below the first power times the volume.
- Normalized convolution over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ is computed exactly enough from synthetic transforms and packed polynomial products. (on [Exact normalized polynomial products](exact-ring-products.md))
- Chaining the reductions from integer multiplication to ring convolution, with exact recovery, multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$. (on [Multiplication algorithm and its cost](main-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2**: Two tape procedures, an address interchange and a simultaneous butterfly layer, cost a power of their parameter below the first power times the volume.
How: build both from fixed linear networks that restore scratch values, and recurse on their rank saving
- S2.2: A fixed linear network exchanging two banks of values with $W$ wires in a label space of dimension $m$ makes $s<Wm$ smaller calls, each on volume $V/W$, and so saves a power of the parameter.
  How: restore scratch values, change representation by frames, build the subset network with rank budget, then solve the recurrence

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md)): Schönhage and Strassen conjectured that $n\log n$ is the optimal order of growth for multiplication, the conjecture the new bound refutes.
- S3 (on [Exact normalized polynomial products](exact-ring-products.md)): Normalized convolution over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ is computed exactly enough from synthetic transforms and packed polynomial products.
- S4 (on [Multiplication algorithm and its cost](main-algorithm.md)): Chaining the reductions from integer multiplication to ring convolution, with exact recovery, multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$.
- S2.1 (on [Elementary stream operations on tapes](stream-operations.md)): Fixed-radix digit moves, splits, merges and row splitting on an array of volume $V$ take $O(V)$ steps on a fixed number of tapes.
- S2.2.1 (on [Restoring auxiliary values](restoring-auxiliary.md)): For arbitrary initial values of the scratch wires, a forward invocation adds the source to the target and leaves everything else, scratch included, unchanged; three stages exchange the two banks.
- S2.2.2 (on [Linear networks, roles and frames](linear-networks-frames.md)): Giving every wire a role and every vertex an invertible frame $D_v$, the common frame commutes with pointwise linear gates, so intermediate frames cancel and only the endpoint operator remains on each role.
- S2.2.3 (on [Finite networks from three-element subsets](subset-network-construction.md)): Gather, scatter, copy and side-injection maps indexed by triples of three-element subsets admit nested subspace labels whose decreasing edges lose only $h$ dimensions each, so edge ranks total less than $Wm$.
- S2.2.4 (on [Recursive power saving s < Wm](recursive-saving.md)): The number $s$ of smaller calls satisfies $s/W<m^\tau$ for a fixed $\tau<1$, so recursing at parameter $mf$ with $s$ calls on volume $V/W$ gives cost per volume a power of the parameter below the first power.
- S2.3 (on [Fast interchange of address fields](address-interchange.md)): Two disjoint contiguous $u$-bit address fields of an array of volume $V$ can be interchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$.
- S2.4 (on [Simultaneous butterfly layer H₀](butterfly-layer.md)): Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ simultaneously on selected bits of at most $d$ address chunks of arrays of complex fixed-point polynomial records costs $O(Vd^{\lambda'})$ with a fixed $\lambda'<1$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Multiplication algorithm and its cost](main-algorithm.md): Chain the reductions: digits, prime axes, resampling and chirps, phase twist, ring convolution with fast interchanges and butterfly layers, then rescaling, rounding and carries; the cost table fits n(lg n)^(1−κ).
  Shown as: Integer multiplication below n log n *<predicate>* Multiplication algorithm and its cost
- [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md): Schönhage and Strassen multiplied n-bit integers in O(n log n log log n) on a multitape machine and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n).
  Shown as: Integer multiplication below n log n *<predicate>* Schönhage–Strassen n log n conjecture and history

## Other pages you may link to

- [Convolution and the discrete Fourier transform](convolution-dft.md)
- [Polynomial ring modulo y^r + 1](poly-ring-mod-yr1.md)
- [Established O(n log n) multiplier as subroutine](hh-nlogn-multiplier.md)
- [Elementary stream operations on tapes](stream-operations.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Linear networks, roles and frames](linear-networks-frames.md)
- [Finite networks from three-element subsets](subset-network-construction.md)
- [Restoring auxiliary values](restoring-auxiliary.md)
- [Recursive power saving s < Wm](recursive-saving.md)
- [Address shear and triangular factorization](address-shear.md)
- [Fast interchange of address fields](address-interchange.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Coefficient twist to the polynomial ring](phase-twist.md)
- [Multiplication as digit convolution](radix-digit-reduction.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Exact normalized polynomial products](exact-ring-products.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Simultaneous butterfly layer H₀](butterfly-layer.md)
- [Transform layout with retained frequency order](transform-layout.md)

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers
in $O(n(\lg n)^{1-\kappa})$ worst-case time" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}


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

Write the body to `exegenius/tasks/0027-write-main-result.answer.md` and the JSON to `exegenius/tasks/0027-write-main-result.answer.json`, then run `exegenius submit 0027-write-main-result` in the project directory. If submit rejects the answer, fix the answer and submit again.
