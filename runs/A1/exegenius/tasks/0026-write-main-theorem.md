# exegenius task 0026-write-main-theorem

Project directory: `/home/user/openai-nlogn-wiki/runs/A1` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: asymptotic analysis, recursion and divide-and-conquer recurrences, basic discrete mathematics (modular arithmetic, primes, Chinese remainder theorem, permutations, sets), and introductory linear algebra (vectors, matrices, invertible maps, subspaces, triangular matrices, Gaussian elimination). They know binary arithmetic, schoolbook and Karatsuba multiplication, and basic Turing machines with tapes. They have not studied abstract algebra beyond basics, the FFT in depth, Schönhage-Strassen, Nussbaumer transforms, or fast multitape tape-programming techniques; those are explained by the wiki.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Convolution and cyclic convolution
- Fourier transform and roots of unity
- The n log n optimality conjecture
- Multiplication as radix-digit convolution
- Arrays on tapes, scans and stored bit volume
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The formal variable of the polynomials; its powers serve as roots of unity.
  - $r$ (coefficient count): The number of complex coefficients in a record, a power of two.
- Synthetic polynomial transforms
- Controlled shifts and carries by packing
- Signed coefficient packing (Kronecker substitution) and the n log n subroutine
- Chinese-remainder map onto prime cyclic axes
- Gaussian resampling
- Bluestein chirp conversion
- Last-coordinate phase twist
- Linear networks with roles and frames
- Restoring auxiliary values
- Finite network from three-element subsets
- Recursive power saving
- Address shear and lower triangular factorization
- Fast address-field interchange
  - $V$ (stored bit volume): The total number of bits stored in the array.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (interchange exponent): A fixed constant below 1 giving the power saving in the field width.
- Simultaneous butterfly layer
  - $V$ (stored bit volume): The total number of bits stored in the numerical arrays.
  - $d$ (chunk count): The number of equal-width address chunks in which one bit position is selected.
  - $\lambda'$ (butterfly exponent): A fixed constant below 1 giving the power saving in the number of selected chunks.
- Synthetic transform layout and convolution
- Precision, rounding and carry propagation
- Logarithms and iterated logarithms (also: lg, log base 2, log n, lg lg n)
- Binary representation of integers (also: bits, n-bit integer, binary expansion, base 2)
- Positional radix notation (also: base-b digits, radix, digit expansion)
- Schoolbook and Karatsuba multiplication (also: long multiplication, quadratic multiplication, Karatsuba)
- Recursion and divide-and-conquer recurrences (also: master theorem, recurrence relation, recursive algorithm, recursion depth)
- Modular arithmetic (also: congruence, mod n, residues, cyclic group Z/n)
- Primes and coprimality (also: prime numbers, pairwise coprime, gcd, distinct primes, prime factorization)
- Chinese remainder theorem (also: CRT, Chinese remainder)
- Permutations and bijections (also: permutation of indices, bijective map, rearrangement, sorting)
- Vectors, matrices and linear maps (also: matrix-vector product, linear operator, linear transformation, invertible matrix, operator composition)
- Subspaces, dimension and linear independence (also: vector subspace, span, rank, nested subspaces, ground set)
- Triangular matrices and Gaussian elimination (also: lower triangular matrix, row reduction, LU factorization, elementary row operations)
- Bitwise operations and XOR (also: exclusive or, bit string, bit field, bit position, addition mod 2)
- Cartesian products and multidimensional arrays (also: product of sets, tuples, multi-index, array indexing, d-dimensional array)
- Sets and subsets (also: three-element subsets, finite set, set cardinality)
- Rationals, rounding and error bounds (also: floor and ceiling, rounding to nearest integer, absolute error, triangle inequality, fixed-point approximation)
- Dyadic rationals and fixed-point numbers (also: binary fractions, truncation, fixed-precision arithmetic, dyadic numbers)
- Two's complement and signed integers (also: signed integers, sign bit, negative numbers in binary, sign and magnitude)
- Basic ring and group structure (also: ring, commutative ring, quotient by a polynomial, homomorphism, algebraic identity)
- Euler's formula and primitive roots of unity (also: e^{2 pi i/N}, primitive N-th root of unity, unit circle, complex exponential)
- Fast Fourier transform for power-of-two length (also: FFT, Cooley-Tukey, radix-2 FFT, butterfly, O(n log n) transform)
- Gaussian function (also: Gaussian, exp(-x^2), bell curve, Gaussian decay)
- Time and space as functions of input size (also: linear time, running time, worst-case complexity, deterministic algorithm, subroutine call)
- Tape head movement and sequential access (also: tape scan, head moves, sequential access, copying between tapes, sorting on tapes)

## This page

Concept: Integer multiplication in O(n (lg n)^(1−κ)) time
Gloss: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time with κ=2^−182, by chaining digit convolution, Chinese-remainder map, Gaussian resampling, chirps, twist, and synthetic transforms accelerated by fast interchanges and butterfly layers.
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (bit length): The number of bits of each input integer.
- $\lg$ (binary logarithm): The base-2 logarithm rounded up, at least 1.
- $\kappa$ (saving exponent): The fixed constant 2^-182 giving the power saving in the logarithmic factor.

## This page in the argument

The step: A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.
How: Reduce the product to a convolution over the polynomial ring through a chain of representation changes, and make the transforms there cheap with two fast tape procedures that save a power of the logarithmic factor.
Why: Plain transform layers cost a scan of the data at each of the log n levels, giving n log n; so both address movement and butterfly arithmetic must be made cheaper than a scan per level, and the reductions must route all transforms through those cheaper layers. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))
Striking feature: The saving is a strict power of the logarithm, (lg n)^(-kappa) with an astronomically small kappa, rather than a log log or log-star factor, so it refutes the n log n conjecture. (explain why it holds, from the method)

Its sub-steps, in order:

- Splitting the inputs into radix digits reduces the product to a convolution of short integer coefficients, and carries then give the exact product. (on [Multiplication as radix-digit convolution](radix-digit-convolution.md))
- Two tape procedures cost less than a scan per level: interchanging address fields and applying butterfly layers both save a power.
- Each procedure arises from a fixed linear network with a rank deficit $s<Wm$, which makes the recursion save a power.
- The convolution of the radix digits is reduced through representation changes to convolution over $\mathbb C[y]/(y^r+1)$, evaluated by synthetic transforms, and exact recovery follows.

## Steps this page derives

The argument gives this page these sub-steps of its step (S2, S3, S4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2**: Two tape procedures cost less than a scan per level: interchanging address fields and applying butterfly layers both save a power.
How: State the two procedures with their costs, each obtained from its own fixed linear network.

**S3**: Each procedure arises from a fixed linear network with a rank deficit $s<Wm$, which makes the recursion save a power.
How: Apply a fixed linear network to row streams with frames, count the smaller calls its edges need, and show the count is strictly below the trivial bound.

**S4**: The convolution of the radix digits is reduced through representation changes to convolution over $\mathbb C[y]/(y^r+1)$, evaluated by synthetic transforms, and exact recovery follows.
How: Chain the reductions of the multiplication flow figure: Chinese-remainder map, Gaussian resampling and chirps, phase twist, then synthetic ring convolution, then rounding and carries.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Multiplication as radix-digit convolution](radix-digit-convolution.md)): Splitting the inputs into radix digits reduces the product to a convolution of short integer coefficients, and carries then give the exact product.
- S2.1 (on [Fast address-field interchange](address-interchange.md)): Two disjoint address fields of $u$ bits in a Cartesian-product array are interchanged at cost $O(Vu^\tau)$ for a fixed $\tau<1$.
- S2.2 (on [Simultaneous butterfly layer](butterfly-layer.md)): The map $H_0(u,v)=((u+v)/2,(u-v)/2)$ is applied on one bit position in each of $d$ address chunks at cost $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$.
- S3.1 (on [Linear networks with roles and frames](linear-networks-frames.md)): With frames at each vertex, intermediate frames cancel and each route applies only an endpoint operator.
- S3.2 (on [Address shear and lower triangular factorization](address-shear.md)): For the bit procedure the endpoint operator is the address shear $(H,D)\mapsto(H+D,D)$, cheap by lower-triangular factorization.
- S3.3 (on [Finite network from three-element subsets](finite-subset-network.md)): A fixed network from three-element subsets with nested subspaces has total number of smaller calls $s<Wm$.
- S3.4 (on [Recursive power saving](recursive-power-saving.md)): A call at parameter $mf$ uses $s$ calls at parameter $f$ on volume $V/W$, so the cost per volume grows by $s/W<m$ and the saving is a power.
- S4.1 (on [Chinese-remainder map onto prime cyclic axes](chinese-remainder-address-map.md)): The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.
- S4.2 (on [Gaussian resampling](gaussian-resampling.md)): Gaussian resampling expresses each prime-length source transform through a power-of-two tensor transform, keeping the permutations inside the identity.
- S4.3 (on [Bluestein chirp conversion](bluestein-chirp.md)): Bluestein's chirp identity converts the middle transform with its target permutation into normalized cyclic convolution.
- S4.4 (on [Last-coordinate phase twist](phase-twist.md)): A phase twist makes the last cyclic coordinate a polynomial modulo $y^r+1$ whose negative wrap gives the original cyclic wrap once the twist is removed.
- S4.5 (on [Synthetic polynomial transforms](synthetic-transforms.md)): Synthetic transforms over the ring use powers of $y$ as roots of unity and compute convolution on the remaining axes.
- S4.6 (on [Synthetic transform layout and convolution](transform-layout-convolution.md)): The forward transforms keep the same frequency order through the pointwise product and the opposite transform consumes it, using fast butterfly layers and interchanges.
- S4.7 (on [Signed coefficient packing (Kronecker substitution) and the n log n subroutine](signed-packing.md)): Polynomial products over the ring are computed by signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.
- S4.8 (on [Precision, rounding and carry propagation](precision-exact-recovery.md)): After removing known normalizations and digit scales the recovered coefficient error is below $1/2$, so rounding and carries give the exact product.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The n log n optimality conjecture](nlogn-conjecture.md): Schönhage and Strassen's 1971 O(n log n log log n) multitape multiplication and their proposal that n log n is optimal; Harvey and van der Hoeven later reached O(n log n).
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* The n log n optimality conjecture
- [Multiplication as radix-digit convolution](radix-digit-convolution.md): Split each integer into short radix digits so the product becomes a convolution of integer coefficient lists; carries then give the exact product.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Multiplication as radix-digit convolution
- [Chinese-remainder map onto prime cyclic axes](chinese-remainder-address-map.md): A map placing the radix-digit coefficient list on a product of distinct prime cyclic axes that preserves convolution, implemented by triangular controlled shifts and axis moves.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Chinese-remainder map onto prime cyclic axes
- [Gaussian resampling](gaussian-resampling.md): Harvey and van der Hoeven's identity expressing each Fourier transform of prime length through a multidimensional transform with power-of-two axis lengths; source and target permutations stay inside the identity instead of being executed as sorts.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Gaussian resampling
- [Bluestein chirp conversion](bluestein-chirp.md): Bluestein's chirp identity rewrites a Fourier transform as a convolution with chirp factors, so the middle transform with its target permutation becomes a normalized cyclic convolution.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Bluestein chirp conversion
- [Last-coordinate phase twist](phase-twist.md): A phase twist changes the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap gives the original cyclic wrap once the twist is removed.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Last-coordinate phase twist
- [Synthetic transform layout and convolution](transform-layout-convolution.md): Forward synthetic transforms keep the same frequency order through the pointwise product and the opposite transform consumes it, so convolution over the ring is computed on the retained layout using fast butterfly layers and address interchanges.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Synthetic transform layout and convolution
- [Precision, rounding and carry propagation](precision-exact-recovery.md): After removing known normalizations and digit scales, the recovered coefficient error is shown strictly below 1/2, so rounding gives exact integer coefficients and carries yield the binary product.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Precision, rounding and carry propagation

## Other pages you may link to

- [Convolution and cyclic convolution](convolution.md)
- [Polynomial ring modulo y^r + 1](ring-mod-yr.md)
- [Fourier transform and roots of unity](dft.md)
- [Arrays on tapes, scans and stored bit volume](tape-arrays-and-streams.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Linear networks with roles and frames](linear-networks-frames.md)
- [Controlled shifts and carries by packing](controlled-shifts.md)
- [Address shear and lower triangular factorization](address-shear.md)
- [Signed coefficient packing (Kronecker substitution) and the n log n subroutine](signed-packing.md)
- [Restoring auxiliary values](restoring-auxiliary-values.md)
- [Finite network from three-element subsets](finite-subset-network.md)
- [Recursive power saving](recursive-power-saving.md)
- [Fast address-field interchange](address-interchange.md)
- [Simultaneous butterfly layer](butterfly-layer.md)

## Evidence from the sources, with the paragraph around each quote

- "disproves the $n\log n$ optimality conjecture
of Sch\"onhage and Strassen in this model" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "We obtain a strict power saving in the
logarithmic factor, in the same fixed finite-tape model." (paper)

  > Sch\"onhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in $O(n\log n\log\log n)$ time on a multitape Turing machine, and proposed $n\log n$ as the optimal order of growth \cite[Section~1]{SchonhageStrassen1971}. After a sequence of improvements, Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper bound~\cite{HarveyHoeven2021}. We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model. The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers.


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

Write the body to `exegenius/tasks/0026-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0026-write-main-theorem.answer.json`, then run `exegenius submit 0026-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
