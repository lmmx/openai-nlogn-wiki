# exegenius task 0027-write-main-result

Project directory: `/home/user/openai-nlogn-wiki/runs/D1` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: comfortable with asymptotic analysis, basic algorithm design (divide and conquer, recurrences, the idea of FFT-style multiplication at the level of knowing it exists), discrete math (modular arithmetic, primes, gcd, binary representation), and linear algebra (vectors, matrices, subspaces, rank, dimension, invertibility). They know complex numbers and polynomials, and basic multitape Turing machines. They have not studied the specialist material of the paper: Harvey-van der Hoeven machinery, Gaussian resampling, Bluestein, Chinese-remainder multidimensional reindexing, Bruhat factorization, or precise fixed-point error analysis.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Convolution and cyclic convolution
- Discrete Fourier transform and roots of unity
- Two-point butterfly and fast transform levels
- Integer product as radix-digit convolution
- Known O(n log n) multiplier and the n log n conjecture
- Address fields, streams and scans on tape
- Fixed-point Gaussian dyadic records
- Polynomial ring modulo y^r+1
  - $y$ (ring variable): The formal variable of the polynomial ring, whose powers serve as roots of unity.
  - $r$ (coefficient count): The number of complex coefficients in a record, a power of two.
- Synthetic polynomial transforms
- Signed packing (Kronecker substitution)
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein chirp identity and phase twist
- Retaining permutations in the transform
- Linear exchange networks with roles and frames
- Three-element-subset subspace construction
- Recursive rank saving gives a power saving
- Address shear and triangular factorization
- Fast address-field interchange costing O(V u^τ)
  - $V$ (bit volume): The number of stored bits of the array.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (time exponent): A fixed constant strictly less than one in the cost exponent.
- Simultaneous butterfly layer on selected bits
  - $H_0$ (half-sum butterfly): The two-point map (u,v) -> ((u+v)/2,(u-v)/2) applied coefficientwise.
  - $V$ (bit volume): The number of logical stored bits of the array.
  - $d$ (axis count): The maximum number of equal-width address chunks whose selected bit is transformed simultaneously.
  - $\lambda'$ (layer exponent): A fixed constant strictly less than one in the cost exponent.
- Precision, rounding and carry recovery
- Parameter choice and total cost accounting
- Packed selected-bit addition
- Linear algebra over a field (also: vector space, subspace, dimension, rank, linear map, invertible matrix, matrix product)
- Modular arithmetic (also: residues, congruence, mod, bmod, integers modulo m, residue ring)
- Primes, gcd and coprimality (also: greatest common divisor, gcd, distinct primes, relatively prime, prime factorization)
- Binary representation and bit operations (also: bit strings, binary expansion, XOR, bitwise exclusive or, bit position, lg n, base-2 logarithm)
- Logarithms, floor and ceiling (also: log, lg, floor, ceiling, iterated logarithm)
- Permutations (also: bijection, sorting a permutation, permutation of indices, inverse permutation)
- Mixed-radix and positional digit expansion (also: digits in base b, radix representation, index as digit tuple, lexicographic order, multi-index)
- Multidimensional arrays and tensors (also: multi-dimensional array, tensor product of transforms, axes, separable transform)
- Elementary Gaussian integers and dyadic rationals (also: dyadic rational, power-of-two denominators, Gaussian integer, fixed-point number)
- Norms, error bounds and rounding (also: triangle inequality, absolute value bound, operator norm, contraction, rounding to nearest integer, truncation error)
- Schoolbook carry addition (also: carry propagation, long multiplication, grade-school multiplication, linear-time addition)
- Geometric series and recurrences (also: recursion tree, divide and conquer recurrence, master theorem, summing powers)
- Roots of unity and Euler's formula (also: e^{2 pi i/n}, primitive n-th root, unit circle)
- Basic finite-set combinatorics (also: subsets of size three, counting subsets, binomial coefficient, intersection counting, inclusion-exclusion)
- Deterministic algorithms and tape scans (also: linear scan, copying between tapes, sorting on tape, merging)

## This page

Concept: Integer multiplication in O(n (lg n)^(1-κ))
Gloss: A deterministic multitape Turing machine multiplies n-bit integers in O(n (lg n)^(1-κ)) time with κ=2^-182, disproving the n log n optimality conjecture in this model.

## This page in the argument

The step: A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.
How: Build two fast tape procedures (address interchange and simultaneous butterfly layers) with power savings, use them in synthetic transforms, and place those in the reduction of multiplication to convolution
Why: Scanning the data at each of the log n transform levels already costs n log n, so savings are needed in both data movement and arithmetic. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))
Striking feature: The exponent $1-\kappa$ with the tiny $\kappa=2^{-182}$: a power saving over $n\log n$, however small, refuting the $n\log n$ optimality conjecture. (explain why it holds, from the method)

Its sub-steps, in order:

- A multitape machine with fixed alphabet and tapes can do elementary scans, permutations of digit pairs and controlled shifts on arrays in lexicographic order in time linear in the volume. (on [Address fields, streams and scans on tape](tape-layout-streams.md))
- Two disjoint address fields of $u$ digits in an array of volume $V$ can be exchanged in time $O(Vu^\tau)$ with $\tau<1$, the final map being an exact permutation. (on [Fast address-field interchange costing O(V u^τ)](address-interchange.md))
- Applying $H_0$ on the same bit position of up to $d$ address chunks of polynomial records costs $O(Vd^{\lambda'})$ with $\lambda'<1$, with all intermediate values exact Gaussian dyadics and a single truncation. (on [Simultaneous butterfly layer on selected bits](simultaneous-butterfly-layer.md))
- Convolution over $\mathbb C[y]/(y^r+1)$ can be computed by synthetic transforms that use the simultaneous butterfly layers. (on [Synthetic polynomial transforms](synthetic-transform.md))
- Fourier transforms of pairwise coprime lengths reduce to power-of-two tensor transforms with the permutations retained in the transform formula. (on [Gaussian resampling](gaussian-resampling.md))
- The product of two $n$-bit integers is reduced step by step to convolution over $\mathbb C[y]/(y^r+1)$, recovered exactly, and its total cost is bounded.

## Steps this page derives

The argument gives this page these sub-steps of its step (S6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S6**: The product of two $n$-bit integers is reduced step by step to convolution over $\mathbb C[y]/(y^r+1)$, recovered exactly, and its total cost is bounded.
How: Chain reductions (digits, prime axes, power-of-two axes, polynomial ring), then recover the product and account for every cost term

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Address fields, streams and scans on tape](tape-layout-streams.md)): A multitape machine with fixed alphabet and tapes can do elementary scans, permutations of digit pairs and controlled shifts on arrays in lexicographic order in time linear in the volume.
- S2 (on [Fast address-field interchange costing O(V u^τ)](address-interchange.md)): Two disjoint address fields of $u$ digits in an array of volume $V$ can be exchanged in time $O(Vu^\tau)$ with $\tau<1$, the final map being an exact permutation.
- S3 (on [Simultaneous butterfly layer on selected bits](simultaneous-butterfly-layer.md)): Applying $H_0$ on the same bit position of up to $d$ address chunks of polynomial records costs $O(Vd^{\lambda'})$ with $\lambda'<1$, with all intermediate values exact Gaussian dyadics and a single truncation.
- S4 (on [Synthetic polynomial transforms](synthetic-transform.md)): Convolution over $\mathbb C[y]/(y^r+1)$ can be computed by synthetic transforms that use the simultaneous butterfly layers.
- S5 (on [Gaussian resampling](gaussian-resampling.md)): Fourier transforms of pairwise coprime lengths reduce to power-of-two tensor transforms with the permutations retained in the transform formula.
- S6.1 (on [Integer product as radix-digit convolution](radix-digit-reduction.md)): Splitting each operand into radix-$2^b$ digits reduces the integer product to a convolution of digit lists, followed by carry propagation.
- S6.2 (on [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)): The digit list is reindexed by the Chinese remainder theorem onto cyclic axes of distinct prime lengths, preserving convolution.
- S6.3 (on [Bluestein chirp identity and phase twist](bluestein-chirp.md)): Bluestein's chirp identity and a phase twist turn the middle transform into a convolution whose last axis is negacyclic modulo $y^r+1$.
- S6.4 (on [Precision, rounding and carry recovery](precision-exact-recovery.md)): All transforms keep the coefficient error below $1/2$, so rounding and carry propagation give the exact product.
- S6.5 (on [Parameter choice and total cost accounting](parameter-cost-accounting.md)): With a fixed rational choice of exponents, including $\kappa=2^{-182}$, each cost term divided by volume is a power of $p$ below one, so the total is $O(n(\lg n)^{1-\kappa})$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Integer product as radix-digit convolution](radix-digit-reduction.md): Splitting each operand into radix-2^b digits turns the integer product into a convolution of digit lists, followed by carry propagation.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) *<predicate>* Integer product as radix-digit convolution
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md): A reindexing of the coefficient list onto a product of cyclic axes of distinct prime lengths that preserves convolution, giving a multidimensional convolution.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) *<predicate>* Chinese-remainder map to prime cyclic axes
- [Gaussian resampling](gaussian-resampling.md): Harvey-van der Hoeven technique expressing a Fourier transform of prime length through a power-of-two tensor transform, with source and target permutations.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) *<predicate>* Gaussian resampling
- [Bluestein chirp identity and phase twist](bluestein-chirp.md): Rewriting a transform as a cyclic convolution via chirps; a phase twist turns the last cyclic axis into a negacyclic polynomial modulo y^r+1.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) *<predicate>* Bluestein chirp identity and phase twist
- [Synthetic polynomial transforms](synthetic-transform.md): Fourier transforms over the ring modulo y^r+1 using powers of y as roots, computed by signed shifts and butterflies and retaining one stored frequency order for the inverse.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) *<predicate>* Synthetic polynomial transforms
- [Signed packing (Kronecker substitution)](signed-packing.md): Evaluating polynomial products over the ring as a single integer product by packing signed coefficients into one integer, then unpacking.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) *<predicate>* Signed packing (Kronecker substitution)
- [Retaining permutations in the transform](permutation-cancellation.md): The source permutation from resampling cancels across the two forward transforms, the pointwise product and the inverse transform, avoiding separate full sorts.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) *<predicate>* Retaining permutations in the transform
- [Parameter choice and total cost accounting](parameter-cost-accounting.md): A fixed rational choice of exponents (including κ=2^-182) makes each cost term, divided by volume, a power of p below one so the total is O(n (lg n)^(1-κ)).
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) *<predicate>* Parameter choice and total cost accounting
- [Known O(n log n) multiplier and the n log n conjecture](nlogn-multiplier.md): Harvey and van der Hoeven's O(n log n) multitape multiplication, used as an ordinary subroutine, and the Schönhage-Strassen conjecture that n log n is optimal.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) *<predicate>* Known O(n log n) multiplier and the n log n conjecture

## Other pages you may link to

- [Convolution and cyclic convolution](convolution.md)
- [Address fields, streams and scans on tape](tape-layout-streams.md)
- [Fixed-point Gaussian dyadic records](fixed-point-dyadic.md)
- [Linear exchange networks with roles and frames](linear-network-frames.md)
- [Address shear and triangular factorization](address-shear.md)
- [Three-element-subset subspace construction](subset-intersection-network.md)
- [Recursive rank saving gives a power saving](recursive-power-saving.md)
- [Fast address-field interchange costing O(V u^τ)](address-interchange.md)
- [Discrete Fourier transform and roots of unity](dft.md)
- [Polynomial ring modulo y^r+1](negacyclic-ring.md)
- [Two-point butterfly and fast transform levels](butterfly.md)
- [Precision, rounding and carry recovery](precision-exact-recovery.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Simultaneous butterfly layer on selected bits](simultaneous-butterfly-layer.md)

## Evidence from the sources, with the paragraph around each quote

- "Its worst-case running time satisfies
\[
 T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right),
 \qquad \kappa=2^{-182}.
\]" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}

- "disproves the $n\log n$ optimality conjecture
of Sch\"onhage and Strassen in this model" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "\begin{theorem}\label{thm:main}" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}


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

Keep any other files you make, such as scripts, in `exegenius/tasks/0027-write-main-result`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
