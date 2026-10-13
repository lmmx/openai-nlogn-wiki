# exegenius task 0042-write-sub-nlogn-multiplication

Project directory: `/home/user/openai-nlogn-wiki/runs/G1` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: asymptotic analysis and recurrences, discrete mathematics (sets, functions, permutations, modular arithmetic, primes, gcd), a first course in linear algebra (vectors, matrices, rank, bases, subspaces, orthogonality, dot products), complex numbers and polynomial algebra, and basic multitape Turing machine computation including binary arithmetic. They have seen schoolbook multiplication and basic divide-and-conquer, but not the FFT's number-theoretic refinements, abstract algebra beyond rings of polynomials, tensor products, bilinear forms over finite fields, or the analytic number theory used for prime estimates.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machines
- The n log n conjecture and multiplication history (also: Schönhage–Strassen conjecture)
- Harvey–van der Hoeven O(n log n) multiplier
- Discrete Fourier transform (also: Fourier transform)
- Cyclic convolution (also: convolution)
- Convolution theorem
- FFT butterflies (decimation in frequency) (also: butterfly, two-point butterfly)
- Integer multiplication as radix-digit convolution
- Multidimensional (tensor) transform (also: tensor transform)
- Chinese-remainder address map (also: Agarwal–Cooley map)
- Fixed-point and Gaussian dyadic arithmetic (also: disk grid array, Gaussian dyadics)
- Linear contractions and error accumulation
- Gaussian resampling (also: Gaussian resampling without sorting)
- Bluestein chirp identity (also: chirp)
- Cancellation of the retained source permutation
- Prime source lengths near powers of two
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials, subject to the relation y^r + 1 = 0.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic roots of unity
- Synthetic polynomial transform (also: polynomial transform)
- Coefficient phase twist
- Signed Kronecker packing of polynomial products (also: Kronecker substitution)
- Array layout and elementary tape streams (also: address fields)
- Controlled cyclic shifts of an address field
- Three-element subset gates (copy, gather, scatter, side wires)
- Scratch-restoring bank-exchange network
- Frames: changing representation along a network (also: frame, role)
- Subspace labels and the rank deficit (also: rank saving)
- Recursive power saving
- Lower triangular (Bruhat-type) factorization
- Cost of a rational matrix shear
- Address-chunk interchange (also: chunk swap, address rearrangement)
- Phase frames and the C kernel (also: complex phase network)
- Packed selected-bit addition
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Tape layout of synthetic transforms (also: retained frequency order)
- Convolution over the polynomial ring
- Exact recovery by rounding and carries
- Parameter choice and time bound
- The multiplication algorithm
- Logarithms and exponents (also: log, lg, log base 2, powers of two, iterated logarithm, exponent laws)
- Floor and ceiling functions (also: floor, ceiling, rounding up, rounding down, integer part)
- Binary and radix integer representation (also: positional notation, base-B digits, bit strings, binary expansion, radix, digits in base B, carries)
- Schoolbook multiplication (also: grade-school multiplication, long multiplication, quadratic multiplication, naive multiplication)
- Modular arithmetic and congruences (also: residues, mod, congruence modulo q, residue ring, integers mod q, remainder)
- Primes, gcd and coprimality (also: prime numbers, greatest common divisor, relatively prime, pairwise coprime, extended Euclidean algorithm, modular inverse, trial division, divisibility)
- Sets, functions, bijections and permutations (also: bijection, permutation, injective map, index set, Cartesian product, subset, finite sets, partial permutation)
- Counting and binomial coefficients (also: combinations, n choose k, subset counting, Hamming weight, popcount, number of ones in a bit string)
- XOR and mod 2 arithmetic (also: exclusive or, addition mod 2, bitwise XOR, F_2, GF(2), parity, bitwise operations)
- Vectors, matrices and linear maps (also: matrix multiplication, matrix-vector product, identity matrix, invertible matrix, linear transformation, standard basis vector, linear combination, transpose)
- Rank, bases and subspaces (also: matrix rank, linear independence, basis, span, dimension, subspace, vector space, Gaussian elimination, row reduction, elementary matrices, nested subspaces)
- Dot product and orthogonality (also: inner product, orthogonal vectors, orthonormal basis, orthogonal complement, norm of a vector, orthogonal projection, indicator vector)
- Special matrices: triangular, diagonal and permutation matrices (also: lower triangular matrix, upper triangular matrix, diagonal matrix, permutation matrix, diag, projection matrix)
- Rational numbers and the number systems Q, R, C (also: rationals, real numbers, rational matrices, denominators, integers Z)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2 pi i / n}, unit circle, Euler's formula, complex exponential)
- Triangle inequality and absolute value (also: modulus bound, maximum norm, sup norm, infinity norm, disk bound, error bound, |a+b| <= |a|+|b|)
- Geometric series and recurrences (also: geometric sum, recurrence relation, solving recurrences, unrolling a recurrence, master theorem, divide and conquer, recursion tree)
- Induction and proof by contradiction (also: mathematical induction, inductive proof, proof technique, lemma, pigeonhole principle)
- Tape scans and constant-factor simulation on Turing machines (also: linear-time scan, tape head sweep, work tape, tape reversal, copying a tape, finite control with counter, multitape simulation)
- Schoolbook and Karatsuba-style divide-and-conquer multiplication (also: Karatsuba, Toom-Cook, splitting integers into halves)
- Polynomial evaluation and interpolation (also: evaluation at points, Horner's rule, coefficient list, degree of a polynomial, polynomial division with remainder, polynomial modulo x^q - 1)
- Newton iteration for reciprocals (also: Newton's method, Newton reduction, reciprocal approximation, division by Newton iteration)

## This page

Concept: Integer multiplication below n log n
Gloss: A deterministic fixed-tape Turing machine that multiplies n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture by replacing address rearrangement and Fourier layers with faster recursive tape procedures.
Also called: main theorem

## This page in the argument

The step: A deterministic fixed-tape Turing machine multiplies $n$-bit integers in $T_A(n)=O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.
How: reduce the product to a digit convolution computed by synthetic transforms, replace the address rearrangement and butterfly layers inside those transforms by two faster recursive tape procedures, then assemble, round and bound the cost
Why: The source starts from the reduction of multiplication to convolution and says that both movement and arithmetic need savings. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))
Striking feature: The exponent $1-\kappa$ with $\kappa=2^{-182}$ is astronomically close to one, yet strictly below it, which is what refutes the $n\log n$ conjecture. (explain why it holds, from the method)

Its sub-steps, in order:

- Two recursive tape procedures, an address-chunk interchange and a simultaneous butterfly layer, run faster than the naive costs of address rearrangement and Fourier layers by a power of the width.
- Convolution of two arrays over $\mathbb C[y]/(y^r+1)$ is approximated with small error by two forward synthetic transforms, polynomial products and the opposite transform in cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$. (on [Convolution over the polynomial ring](synthetic-convolution.md))
- The product of two $n$-bit integers is computed exactly by placing radix digits on distinct prime axes, transforming them by resampled, chirped synthetic transforms, multiplying pointwise, transforming back, rescaling, rounding and carrying, within the stated time bound. (on [The multiplication algorithm](multiplication-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1**: Two recursive tape procedures, an address-chunk interchange and a simultaneous butterfly layer, run faster than the naive costs of address rearrangement and Fourier layers by a power of the width.
How: build the elementary tape tools, derive a general recursive power saving from a fixed linear network, and instantiate it twice, once for bits and once for complex values

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2 (on [Convolution over the polynomial ring](synthetic-convolution.md)): Convolution of two arrays over $\mathbb C[y]/(y^r+1)$ is approximated with small error by two forward synthetic transforms, polynomial products and the opposite transform in cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.
- S3 (on [The multiplication algorithm](multiplication-algorithm.md)): The product of two $n$-bit integers is computed exactly by placing radix digits on distinct prime axes, transforming them by resampled, chirped synthetic transforms, multiplying pointwise, transforming back, rescaling, rounding and carrying, within the stated time bound.
- S1.1 (on [Array layout and elementary tape streams](stream-operations.md)): Elementary scans on an array of volume $V$ (digit-pair permutations, digit moves, split-map-merge, row splitting into streams) each take $O(V)$ steps on a fixed number of tapes.
- S1.2 (on [Controlled cyclic shifts of an address field](controlled-shifts.md)): A target address field can be cyclically shifted by an offset computed from earlier control fields in $O(V)$ time, which also multiplies a field by fixed units modulo $q^b$.
- S1.3 (on [Recursive power saving](recursive-power-saving.md)): A fixed linear network that exchanges two banks of values, restores its scratch wires and has total edge rank $s<Wm$ yields a recursion whose cost per volume grows only like a fixed power $m^\tau$ with $\tau<1$ per multiplication of the parameter by $m$.
- S1.4 (on [Address-chunk interchange](address-interchange.md)): Two disjoint address chunks of $u$ bits in a complete array of volume $V$ can be interchanged in time $O(Vu^\tau)$ for a fixed $\tau<1$, although intermediate steps form XOR combinations of data.
- S1.5 (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)): The layer $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied to one selected bit in each of up to $d$ address chunks of polynomial records takes $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The multiplication algorithm](multiplication-algorithm.md): Digits are placed on prime axes by the CRT map, transformed by Gaussian-resampled, chirped, synthetic transforms, multiplied pointwise, transformed back, rescaled, rounded and carried to give the exact product.
  Shown as: Integer multiplication below n log n *<predicate>* The multiplication algorithm
- [Parameter choice and time bound](parameter-choice.md): Fixed rational exponents and sizes (p = 6⌈log n⌉, d ≈ p^ε, T ≈ n/log n, κ = 2^{−182}) make every cost row of the table a power of p below 1, so the total is O(n (lg n)^{1−κ}).
  Shown as: Integer multiplication below n log n *<predicate>* Parameter choice and time bound
- [The n log n conjecture and multiplication history](nlogn-conjecture.md): Schönhage and Strassen conjectured that n log n is the optimal multiplication cost on multitape Turing machines; Schönhage–Strassen, Fürer and Harvey–van der Hoeven gave successively better upper bounds down to O(n log n).
  Shown as: Integer multiplication below n log n *<predicate>* The n log n conjecture and multiplication history

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Fixed-point and Gaussian dyadic arithmetic](fixed-point-arithmetic.md)
- [Three-element subset gates (copy, gather, scatter, side wires)](subset-intersection-gates.md)
- [Scratch-restoring bank-exchange network](bank-exchange-network.md)
- [Frames: changing representation along a network](frames-network.md)
- [Subspace labels and the rank deficit](subspace-rank-saving.md)
- [Recursive power saving](recursive-power-saving.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Signed Kronecker packing of polynomial products](kronecker-packing.md)
- [Array layout and elementary tape streams](stream-operations.md)
- [Controlled cyclic shifts of an address field](controlled-shifts.md)
- [Phase frames and the C kernel](binary-phase-interface.md)
- [Lower triangular (Bruhat-type) factorization](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Address-chunk interchange](address-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Discrete Fourier transform](dft.md)
- [Synthetic roots of unity](synthetic-roots.md)
- [FFT butterflies (decimation in frequency)](fft-butterfly.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer multiplication as radix-digit convolution](integer-mult-as-convolution.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Coefficient phase twist](phase-twist.md)
- [Convolution theorem](convolution-theorem.md)
- [Multidimensional (tensor) transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Chinese-remainder address map](crt-axis-map.md)
- [Tape layout of synthetic transforms](synthetic-transform-layout.md)
- [Convolution over the polynomial ring](synthetic-convolution.md)
- [Linear contractions and error accumulation](contraction-error.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Cancellation of the retained source permutation](permutation-cancellation.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Prime source lengths near powers of two](prime-axis-lengths.md)

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time" (paper)

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

Write the body to `exegenius/tasks/0042-write-sub-nlogn-multiplication.answer.md` and the JSON to `exegenius/tasks/0042-write-sub-nlogn-multiplication.answer.json`, then run `exegenius submit 0042-write-sub-nlogn-multiplication` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0042-write-sub-nlogn-multiplication`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
