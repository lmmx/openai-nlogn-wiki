# exegenius task 0022-write-main-result

Project directory: `/home/user/openai-nlogn-wiki/runs/A6` (paths below are relative to it)

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

For these sources: An undergraduate computer science reader who has studied discrete mathematics, algorithms (divide and conquer, fast multiplication such as Karatsuba, the FFT at a basic level), linear algebra, and elementary number theory and probability. They know asymptotic notation, binary and positional number representation, polynomials and complex numbers, and basic Turing machines. They have not studied multitape complexity details, advanced harmonic analysis, algebraic number theory, or the research literature on integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Basic Turing machines and tapes
- Fixed multitape Turing machine model
- Multiplication history and the n log n conjecture
- Multiplication as convolution of radix digits
- Fourier transforms and butterfly operations
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The polynomial indeterminate whose powers act as roots of unity.
  - $r$ (coefficient count): The number of complex coefficients in a record, a power of two.
- Synthetic polynomial transforms
- Gaussian resampling
- Chinese-remainder map to prime cyclic axes
- Bluestein chirp conversion
- Phase twist to the polynomial ring
- Signed packing of polynomial products
- Array order, streams and controlled shifts
- Linear networks with roles and frames
- Finite networks from three-element subsets
- Recursive power saving
- Fast interchange of address chunks
- Fast simultaneous butterfly layers
- Precision, error bound and exact recovery
- Binary representation and radix digits (also: base-b expansion, positional notation, bit strings, most significant bit)
- Modular arithmetic and congruences (also: mod, residues, congruence classes, remainder)
- Prime numbers and coprimality (also: distinct primes, gcd, relatively prime, prime factorization)
- Logarithms and powers of two (also: lg, log base 2, ceiling and floor)
- Schoolbook multiplication and convolution of sequences (also: discrete convolution, polynomial multiplication, Cauchy product)
- Karatsuba and divide-and-conquer multiplication (also: Karatsuba, Toom-Cook, divide and conquer)
- Fast Fourier transform basics (also: FFT, Cooley-Tukey, roots of unity)
- Linear algebra over the reals and complex numbers (also: vector space, matrix, linear map, invertible matrix, subspace, dimension, linear combination)
- Direct product of sets and multidimensional arrays (also: Cartesian product, tensor array, index tuple, multi-index)
- Permutations and bijections (also: rearrangement, bijection, identity permutation, involution)
- Cyclic groups and Z/mZ (also: cyclic group, integers modulo m, cyclic index)
- Fixed-point and rounding arithmetic (also: fixed point, rounding error, truncation, dyadic rationals)
- Error bounds and the triangle inequality (also: sup norm, max norm, absolute value bound, norm)
- Binary XOR and bitwise operations (also: xor, exclusive or, bit shift, bit masks)
- Basic counting and combinatorics (also: binomial coefficient, subsets, inclusion-exclusion, pigeonhole)
- Induction and recurrences (also: recurrence relation, recursion, master theorem, mathematical induction)
- Real analysis basics: inequalities and exponentials (also: Taylor series, exponential function, Euler's formula, Gaussian function)
- Ring and group axioms (also: commutative ring, algebra, ring homomorphism, quotient ring)

## This page

Concept: Integer multiplication in O(n (lg n)^{1-κ}) time
Gloss: Deterministic multitape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}) time, κ=2^{-182}, by chaining digit convolution, prime axes, Gaussian resampling, chirps, a polynomial-ring twist, synthetic transforms accelerated by fast address interchanges and butterfly layers, then exact recovery.
Heading: Integer multiplication in $O(n (\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (bit length): The number of bits in each input integer.
- $\kappa$ (saving exponent): The fixed constant 2^{-182} giving the power saving in the log factor.

## This page in the argument

The step: A multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.
How: chain reductions from the integer product to a convolution over $\mathbb C[y]/(y^r+1)$, compute it with accelerated synthetic transforms, then recover the exact product
Why: Each stage changes the problem into one whose transform uses only shifts, address rearrangements and butterflies, which the two fast tape procedures speed up; precision analysis then gives exactness. (the sources leave this for the reader to work out: spell it out)
Striking feature: The logarithmic factor has the strict power (lg n)^{1-kappa} with a tiny fixed kappa, below the conjectured n log n. (explain why it holds, from the method)

Its sub-steps, in order:

- Splitting both integers into radix digits turns the product into a convolution of short digit lists followed by carry propagation. (on [Multiplication as convolution of radix digits](convolution-reduction.md))
- A Chinese-remainder address map places the digit list on distinct prime cyclic axes, preserving convolution. (on [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md))
- Gaussian resampling expresses each Fourier transform of arbitrary axis length through a power-of-two tensor transform, keeping permutations in the identity. (on [Gaussian resampling](gaussian-resampling.md))
- Bluestein's chirp identity converts the middle transform with its target permutation into normalized cyclic convolution. (on [Bluestein chirp conversion](bluestein-chirp.md))
- A phase twist makes the last cyclic coordinate a polynomial modulo $y^r+1$ whose negative wrap restores the cyclic wrap after untwisting. (on [Phase twist to the polynomial ring](phase-twist.md))
- Convolution over $\mathbb C[y]/(y^r+1)$ on the remaining axes is computed exactly and fast. (on [Synthetic polynomial transforms](synthetic-transforms.md))
- Fixed-point error of the recovered coefficients is below $1/2$, so rounding, rescaling and carry propagation give the exact product. (on [Precision, error bound and exact recovery](precision-exact-recovery.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Multiplication history and the n log n conjecture](nlogn-conjecture-history.md): Schönhage–Strassen gave O(n log n log log n) and conjectured n log n optimal; Fürer and others improved the factor; Harvey–van der Hoeven reached O(n log n).
  Shown as: Integer multiplication in O(n (lg n)^{1-κ}) time *<predicate>* Multiplication history and the n log n conjecture
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md): Placing the digit list on a product of distinct prime cyclic axes by a Chinese-remainder address map that preserves convolution.
  Shown as: Integer multiplication in O(n (lg n)^{1-κ}) time *<predicate>* Chinese-remainder map to prime cyclic axes
- [Gaussian resampling](gaussian-resampling.md): Harvey–van der Hoeven reduction expressing a Fourier transform of arbitrary axis length through a transform with power-of-two axes, with source and target permutations kept in the identity.
  Shown as: Integer multiplication in O(n (lg n)^{1-κ}) time *<predicate>* Gaussian resampling
- [Bluestein chirp conversion](bluestein-chirp.md): Bluestein's identity rewrites a transform (with its target permutation) as a normalized cyclic convolution via chirp factors.
  Shown as: Integer multiplication in O(n (lg n)^{1-κ}) time *<predicate>* Bluestein chirp conversion
- [Phase twist to the polynomial ring](phase-twist.md): A twist on the last cyclic coordinate makes its wraparound negative, turning it into a polynomial modulo y^r+1 whose negative wrap restores the cyclic wrap after untwisting.
  Shown as: Integer multiplication in O(n (lg n)^{1-κ}) time *<predicate>* Phase twist to the polynomial ring
- [Signed packing of polynomial products](signed-packing.md): Kronecker-style packing of signed coefficients into integers so ring products are computed with the established O(n log n) multiplier as an ordinary subroutine.
  Shown as: Integer multiplication in O(n (lg n)^{1-κ}) time *<predicate>* Signed packing of polynomial products
- [Synthetic polynomial transforms](synthetic-transforms.md): Nussbaumer-style transforms using powers of y as roots of unity so twiddle multiplications are signed shifts, computed by address rearrangements, shifts and butterflies.
  Shown as: Integer multiplication in O(n (lg n)^{1-κ}) time *<predicate>* Synthetic polynomial transforms
- [Fast interchange of address chunks](address-interchange.md): Interchanges two disjoint contiguous address fields of u bits in a Cartesian-product array in O(V u^τ) with τ<1, via XOR combinations and address shears, yielding an exact permutation.
  Shown as: Integer multiplication in O(n (lg n)^{1-κ}) time *<predicate>* Fast interchange of address chunks
- [Fast simultaneous butterfly layers](simultaneous-butterfly.md): Applies H0(u,v)=((u+v)/2,(u-v)/2) on the same bit of at most d address chunks of polynomial records of complex fixed-point numbers in O(V d^λ'), λ'<1, using exact Gaussian dyadics and one final truncation.
  Shown as: Integer multiplication in O(n (lg n)^{1-κ}) time *<predicate>* Fast simultaneous butterfly layers
- [Precision, error bound and exact recovery](precision-exact-recovery.md): Fixed-point precision analysis showing the recovered coefficient error is below 1/2 so rounding, rescaling and carry propagation give the exact integer product.
  Shown as: Integer multiplication in O(n (lg n)^{1-κ}) time *<predicate>* Precision, error bound and exact recovery

## Other pages you may link to

- [Fixed multitape Turing machine model](multitape-model.md)
- [Multiplication as convolution of radix digits](convolution-reduction.md)
- [Polynomial ring modulo y^r + 1](poly-ring-mod.md)
- [Fourier transforms and butterfly operations](fourier-transform-butterflies.md)
- [Array order, streams and controlled shifts](tape-streams.md)
- [Linear networks with roles and frames](linear-network-frames.md)
- [Finite networks from three-element subsets](subset-intersection-network.md)
- [Recursive power saving](recursive-power-saving.md)

## Evidence from the sources, with the paragraph around each quote

- "in $O(n(\lg n)^{1-\kappa})$ worst-case time, with" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "disproves the $n\log n$ optimality conjecture" (paper)

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

Write the body to `exegenius/tasks/0022-write-main-result.answer.md` and the JSON to `exegenius/tasks/0022-write-main-result.answer.json`, then run `exegenius submit 0022-write-main-result` in the project directory. If submit rejects the answer, fix the answer and submit again.
