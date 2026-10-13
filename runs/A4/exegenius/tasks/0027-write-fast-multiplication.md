# exegenius task 0027-write-fast-multiplication

Project directory: `/home/user/openai-nlogn-wiki/runs/A4` (paths below are relative to it)

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

For these sources: An undergraduate computer science reader who knows asymptotic notation, basic discrete mathematics, linear algebra over the reals and complex numbers, elementary algebra (groups, rings, modular arithmetic, polynomials), elementary number theory (primes, CRT) and basic probability/combinatorics. They know basic Turing machines and tapes and the schoolbook and Karatsuba multiplication, and probably the FFT as an algorithm. They have not studied multitape-machine algorithm engineering, Schönhage–Strassen or later multiplication algorithms, or specialist linear-algebra constructions such as Bruhat factorizations.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Array order and elementary tape scans
- Convolution and Fourier transforms
- Multiplication as convolution of radix digits
- Established O(n log n) multiplication and history
- Signed coefficient packing (Kronecker substitution)
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The formal indeterminate of the polynomials, whose powers serve as roots of unity.
  - $r$ (ring degree): The number of complex coefficients in a record, a power of two; y^r = -1 in the ring.
- Synthetic polynomial transforms
- Two-point butterfly H₀
  - $u$ (first operand): The first of the two input values (a polynomial record).
  - $v$ (second operand): The second of the two input values.
- Multidimensional transform with power-of-two axes
- Chinese-remainder map to distinct prime cyclic axes
- Gaussian resampling
- Bluestein's chirp identity
- Last-coordinate phase twist
- Fixed-point complex coefficients and exact recovery
- Linear networks, roles and frames
- Finite networks from three-element subsets
- Recursive power saving from s < Wm
- Address shear and restoration of scratch values
- Fast interchange of address chunks
  - $V$ (stored bit volume): The total number of stored bits in the array.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (address exponent): A fixed constant below 1 in the interchange cost.
- Fast simultaneous butterfly layers
  - $V$ (stored bit volume): The total number of stored bits in the numerical arrays.
  - $d$ (chunk count): The number of equal-width address chunks in which a bit position is selected.
  - $\lambda'$ (layer exponent): A fixed constant below 1 in the layer cost.
- Synthetic transforms on tape layouts
- Exact polynomial-ring products
- Binary representation and bit operations (also: bit strings, binary expansion, XOR, bitwise exclusive or, Hamming weight)
- Modular arithmetic and congruences (also: residue ring, integers mod m, Z/mZ)
- Primes and divisibility (also: gcd, coprime, relatively prime, prime number theorem)
- Linear algebra over fields (also: vector space, subspace, rank, invertible matrix, linear map, GL, diagonal matrix)
- Permutations and bijections (also: permutation, index permutation, bit reversal, bijection)
- Groups and rings (basic algebra) (also: group, cyclic group, ring, abelian group, subgroup)
- Finite sets and elementary combinatorics (also: subsets, counting arguments, binomial coefficients, intersection sizes)
- Floating and fixed-point approximation and rounding (also: rounding error, error bounds, triangle inequality)
- Recurrences and divide-and-conquer analysis (also: recursion, master theorem, recursion tree, geometric series)
- Logarithms and exponentials (also: lg, log base 2, iterated logarithm, powers of two)
- Fast Fourier transform algorithm (also: FFT, Cooley-Tukey, DFT)
- Schoolbook and Karatsuba multiplication (also: long multiplication, Karatsuba)
- Floor, ceiling and big-omega notation (also: floor, ceiling, Omega, Theta, little-o)

## This page

Concept: Integer multiplication in O(n (lg n)^(1−κ)) time
Gloss: Deterministic fixed-tape algorithm: digit convolution, CRT prime axes, Gaussian resampling, Bluestein chirps, phase twist, synthetic transforms with fast interchanges and butterfly layers, then rounding and carries; time O(n (lg n)^(1−κ)), κ=2^−182, disproving the n log n conjecture in this model.
Heading: Integer multiplication in time $O(n(\lg n)^{1-\kappa})$

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits in each of the two integers.
- $\kappa$ (power saving): The fixed constant 2^-182 in the exponent of the logarithm.
- $\lg n$ (binary logarithm): max of ceil(log2 n) and 1.

## This page in the argument

The step: Integer multiplication of $n$-bit integers takes $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$ on a fixed multitape Turing machine.
How: reduce to digit convolution, supply two fast tape procedures, chain reductions, then total the cost
Why: The known O(n log n) algorithm already spends a log factor on transform levels, so beating it needs a cheaper transform in movement and arithmetic, placed inside the standard convolution reduction. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Splitting inputs into radix digits reduces multiplication to convolution of short integer coefficients. (on [Multiplication as convolution of radix digits](radix-digit-reduction.md))
- Two tape procedures, a fast address interchange and fast simultaneous butterfly layers, save over one scan per transform level.
- The digit convolution is carried through four reductions down to convolution over $\mathbb C[y]/(y^r+1)$, then rescaled, rounded and carried.
- A compatible choice of rational parameters makes all terms of the cost table fit the bound $O(n(\lg n)^{1-\kappa})$.

## Steps this page derives

The argument gives this page these sub-steps of its step (S2, S3, S4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2**: Two tape procedures, a fast address interchange and fast simultaneous butterfly layers, save over one scan per transform level.
How: give two tape procedures, each from a linear network with recursive saving

**S3**: The digit convolution is carried through four reductions down to convolution over $\mathbb C[y]/(y^r+1)$, then rescaled, rounded and carried.
How: chain of reductions of problem and representation
- S3.6: The source permutation retained during resampling cancels across the two forward transforms, their product and the opposite transform.
  Source: "Finally, the source permutation retained during resampling cancels" (paper)
  > Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform. Section~\ref{sec:assembly} removes the known normalizations and digit scales, proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product. A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}. Figure~\ref{fig:multiplication-flow} summarizes these reductions.

**S4**: A compatible choice of rational parameters makes all terms of the cost table fit the bound $O(n(\lg n)^{1-\kappa})$.
Source: "parameters makes all terms in its cost table fit Theorem~\ref{thm:main}." (paper)
> Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform. Section~\ref{sec:assembly} removes the known normalizations and digit scales, proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product. A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}. Figure~\ref{fig:multiplication-flow} summarizes these reductions.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Multiplication as convolution of radix digits](radix-digit-reduction.md)): Splitting inputs into radix digits reduces multiplication to convolution of short integer coefficients.
- S2.1 (on [Fast interchange of address chunks](address-interchange.md)): Two disjoint address fields of $u$ bits can be interchanged at cost $O(Vu^\tau)$ with $\tau<1$.
- S2.2 (on [Fast simultaneous butterfly layers](fast-butterfly-layers.md)): $H_0$ can be applied simultaneously on one bit in each of $d$ address chunks at cost $O(Vd^{\lambda'})$ with $\lambda'<1$.
- S2.3 (on [Linear networks, roles and frames](linear-network-frames.md)): Both tape procedures come from a fixed linear network of gates with frames, whose endpoint operator is the desired update and whose smaller calls satisfy $s<Wm$.
- S3.1 (on [Chinese-remainder map to distinct prime cyclic axes](crt-prime-axes.md)): The digit list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map preserving convolution.
- S3.2 (on [Gaussian resampling](gaussian-resampling.md)): Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform.
- S3.3 (on [Bluestein's chirp identity](bluestein-chirp.md)): Bluestein's chirp identity converts the middle transform with its target permutation into normalized cyclic convolution.
- S3.4 (on [Last-coordinate phase twist](phase-twist.md)): A phase twist turns the last cyclic coordinate into a polynomial modulo $y^r+1$ whose negative wrap equals the original cyclic wrap after untwisting.
- S3.5 (on [Synthetic transforms on tape layouts](synthetic-layout.md)): Convolution on the remaining axes over the polynomial ring is computed by synthetic transforms and ring products.
- S3.7 (on [Fixed-point complex coefficients and exact recovery](fixed-point-precision.md)): Known normalizations are removed, the coefficient error is below $1/2$, so rounding and carries give the exact binary product.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fixed multitape Turing machine model](multitape-model.md): Deterministic Turing machine with a fixed finite alphabet and fixed finite number of one-dimensional tapes; the model in which time is measured.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Fixed multitape Turing machine model
- [Multiplication as convolution of radix digits](radix-digit-reduction.md): Split each integer into digits in a radix, so the product becomes a convolution of short integer coefficient lists followed by carry propagation.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Multiplication as convolution of radix digits
- [Chinese-remainder map to distinct prime cyclic axes](crt-prime-axes.md): Re-index the digit list over a product of cyclic axes of distinct prime lengths by the Chinese remainder theorem, preserving convolution; implemented by triangular controlled shifts and axis moves.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Chinese-remainder map to distinct prime cyclic axes
- [Gaussian resampling](gaussian-resampling.md): Harvey–van der Hoeven technique expressing a Fourier transform over prime axes via a power-of-two tensor transform, with source and target permutations kept inside the identity.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Gaussian resampling
- [Bluestein's chirp identity](bluestein-chirp.md): Rewrites a DFT of arbitrary length as a cyclic convolution with a chirp sequence, here converting the middle transform and its permutation into normalized cyclic convolution.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Bluestein's chirp identity
- [Last-coordinate phase twist](phase-twist.md): Multiply by roots-of-unity phases so a cyclic coordinate becomes a polynomial modulo y^r+1, whose negative wrap equals the original cyclic wrap after untwisting.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Last-coordinate phase twist
- [Synthetic transforms on tape layouts](synthetic-layout.md): Layout storing roots, butterflies and frequency order so that the two forward transforms keep the same frequency order through the pointwise product and the opposite transform consumes it.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Synthetic transforms on tape layouts
- [Exact polynomial-ring products](ring-products.md): Products in the ring modulo y^r+1 computed by signed packing and the established O(n log n) multiplier as subroutine, giving normalized convolution.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Exact polynomial-ring products
- [Fixed-point complex coefficients and exact recovery](fixed-point-precision.md): Numerical records use complex fixed-point numbers (Gaussian dyadics); with total error below 1/2, rounding recovers exact integer coefficients and carries give the binary product.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Fixed-point complex coefficients and exact recovery
- [Established O(n log n) multiplication and history](known-nlogn.md): Schönhage–Strassen O(n log n log log n), Fürer, and Harvey–van der Hoeven O(n log n) multiplication on multitape machines, with n log n conjectured optimal; the O(n log n) multiplier is used as a subroutine.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Established O(n log n) multiplication and history

## Other pages you may link to

- [Convolution and Fourier transforms](convolution-dft.md)
- [Polynomial ring modulo y^r + 1](ring-mod-yr.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Array order and elementary tape scans](elementary-scans.md)
- [Two-point butterfly H₀](butterfly-h0.md)
- [Multidimensional transform with power-of-two axes](multidim-transform.md)
- [Linear networks, roles and frames](linear-network-frames.md)
- [Address shear and restoration of scratch values](address-shear.md)
- [Finite networks from three-element subsets](subset-finite-network.md)
- [Recursive power saving from s < Wm](recursive-saving.md)
- [Fast interchange of address chunks](address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Signed coefficient packing (Kronecker substitution)](kronecker-packing.md)

## Evidence from the sources, with the paragraph around each quote

- "There is one deterministic Turing machine $A$, with a fixed finite" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}

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

Write the body to `exegenius/tasks/0027-write-fast-multiplication.answer.md` and the JSON to `exegenius/tasks/0027-write-fast-multiplication.answer.json`, then run `exegenius submit 0027-write-fast-multiplication` in the project directory. If submit rejects the answer, fix the answer and submit again.
