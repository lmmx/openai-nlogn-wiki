# exegenius task 0037-write-main-theorem

Project directory: `/home/user/openai-nlogn-wiki/runs/B5` (paths below are relative to it)

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

For these sources: An undergraduate computer science reader who has studied algorithm analysis (big-O, recurrences, sorting, divide and conquer including Karatsuba-style multiplication), discrete mathematics (modular arithmetic, gcd and coprimality, the Chinese remainder theorem in its basic form, permutations, binary representation), and calculus and linear algebra through matrices, Gaussian elimination and basic vector spaces. They know complex numbers and polynomials, and have seen simple Turing machines with tapes. They have not met the fast Fourier transform in depth beyond its name, finite-field or group-theoretic structure beyond Z/n, Kronecker products, or any research-level multiplication algorithms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n conjecture and its history
  - $n$ (input length): The number of bits in each of the two integers being multiplied.
- Arrays on tape, address fields and volume
- Elementary stream operations
- Controlled shifts and rational scalings
- Rank, subspaces and orthogonal complements
- Cyclic convolution
- Discrete Fourier transform
- Two-point butterfly
- Integer product as digit convolution
- Bank-exchanging linear network with restored scratch
- Frames and the common-frame invariant
- Subspace labels from triple indicator vectors
- Rank deficit and the recursive power saving
  - $s$ (total smaller calls): The number of smaller recursive calls, equal to the sum of ranks of edge differences.
  - $W$ (wire count): The number of wires in the fixed network.
  - $m$ (label dimension): The number of coordinates of the fixed label space.
- Bit network and rational shear interface
- Phase frames and the kernel C=aI+bX
- Lower triangular factorization
- Cost of a rational matrix shear
- Power-width chunk interchange
- Fast interchange of address chunks
  - $V$ (bit volume): The number of stored data bits in the array.
  - $u$ (chunk width): The number of bits in each interchanged chunk.
  - $\tau$ (exponent): A fixed rational constant below 1, namely 1−2^{-50}.
- Packed selected-bit addition
- Polynomial ring modulo y^r+1
  - $y$ (indeterminate): The polynomial variable, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a record, a power of two.
- Synthetic polynomial transform
- Simultaneous butterfly layer
  - $V$ (bit volume): The number of stored data bits.
  - $d$ (axis count): The maximum number of axes whose chunks are transformed together.
  - $\lambda'$ (exponent): A fixed rational constant below 1.
- Transform layout and cost
- Signed packing for ring products
- Convolution from retained transform layout
- Chinese-remainder address map
- Fixed-point error control
- Gaussian resampling
- Multidimensional resampling
- Bluestein chirp and permutation cancellation
- Coefficient phase twist
- Parameter choices and cost table
- Logarithms and exponentials (also: lg, log base 2, log n, exp, powers of two)
- Floor and ceiling (also: floor function, ceiling function, rounding to nearest integer)
- Modular arithmetic (also: congruence, Z/nZ, integers modulo q, residues, remainder)
- Greatest common divisor and coprimality (also: gcd, relatively prime, pairwise coprime, units modulo q)
- Prime numbers (also: primes, prime factorization, odd prime, distribution of primes)
- Chinese remainder theorem (also: CRT)
- Binary representation and bit operations (also: bits, XOR, exclusive or, two's complement, bitwise operations, carries)
- Positional radix representation (also: base b digits, digit expansion, radix)
- Permutations (also: bijections, partial permutation, permutation matrix, transposition)
- Matrices and matrix products (also: matrix multiplication, invertible matrix, identity matrix, triangular matrix, transpose, Gaussian elimination)
- Vector spaces and linear maps (also: linear independence, dimension, kernel, image, basis, dot product)
- Finite field F2 (also: GF(2), integers mod 2, binary field)
- Euler's formula and complex exponentials (also: e^{i theta}, roots of unity, modulus, unit circle, Euler identity)
- Geometric series (also: sum of powers, geometric sum, sum of roots of unity)
- Gaussian function (also: Gaussian, bell curve, exp(-x^2), Gaussian weights)
- Basic calculus and inequalities (also: Taylor series, triangle inequality, Cauchy-Schwarz, limits, bounds on error)
- Fixed-point and rounding arithmetic (also: approximation error, truncation, precision bits, numerical error)
- Cartesian product and tuples (also: product of index sets, multi-index, d-dimensional array, lexicographic order)
- Cyclic groups and direct products (also: Z/n, additive group, group isomorphism, cyclic shift)
- Sorting (also: merge sort, sorting by key, comparison sort, O(N log N) sorting)
- Divide and conquer recurrences (also: master theorem, recurrence relation, recursion tree, induction)
- Karatsuba and schoolbook multiplication (also: long multiplication, grade-school multiplication, O(n^2) multiplication, Karatsuba algorithm)
- Fast Fourier transform idea (also: FFT, Cooley-Tukey, fast polynomial multiplication, evaluation and interpolation)
- Sums and indexed notation (also: summation, product notation, indicator function, Kronecker delta, subsets and set notation)

## This page

Concept: Integer multiplication in O(n (lg n)^(1−κ))
Gloss: A deterministic fixed-tape machine multiplies n-bit integers by digit convolution, CRT axes, resampling, chirps, twisting, synthetic convolution and rounding, disproving the n log n conjecture.
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits in each integer.
- $\kappa$ (saving exponent): The fixed constant 2^{-182}.

## This page in the argument

The step: Integer multiplication of $n$-bit integers takes $O(n(\lg n)^{1-\kappa})$ time on one deterministic fixed-tape machine, disproving the $n\log n$ conjecture.
How: build the fast tape primitives (address interchange and simultaneous butterfly layers), then the synthetic transform and convolution machinery, then the resampling reductions and the assembly with its cost table
Why: Scanning $\Theta(n)$ bits at each of $\Theta(\log n)$ transform levels costs $n\log n$, so savings are needed in both movement and arithmetic, and each primitive must exist before the transforms that use it. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))
Striking feature: The exponent kappa=2^{-182} is a fixed positive constant, so the saving is a power of lg n, uniform through all input lengths, rather than a log* or constant-factor gain. (explain why it holds, from the method)

Its sub-steps, in order:

- An array on a product of ranges is stored in lexicographic order, so address fields, rows and the bit volume $V$ are positions in the tape stream. (on [Arrays on tape, address fields and volume](array-layout.md))
- Splitting an array into streams by a digit or by cyclic rows, applying a pointwise map, and merging cost $O(V)$ tape steps. (on [Elementary stream operations](stream-ops.md))
- A target field can be cyclically shifted or multiplied by a unit modulo $q^b$ by an offset computed from earlier fields in $O(V)$ time. (on [Controlled shifts and rational scalings](controlled-shifts.md))
- Two fixed linear networks exchange two banks of values with signs and restore every auxiliary wire, and their edge residual dimensions sum to $s<Wm$, which gives the recursive power saving. (on [Rank deficit and the recursive power saving](rank-deficit.md))
- Two disjoint address chunks of $u$ bits can be interchanged in $O(Vu^\tau)$ tape steps for a fixed $\tau<1$, although the intermediate steps form XOR combinations of data. (on [Fast interchange of address chunks](chunk-swap.md))
- Applying $H_0$ to the same bit of up to $d$ address chunks at once costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$ with one final truncation. (on [Simultaneous butterfly layer](butterfly-layer.md))
- The synthetic Fourier transform over $\mathbb C[y]/(y^r+1)$ on a product of power-of-two axes can be stored and computed with butterfly layers in the stated cost. (on [Transform layout and cost](transform-layout.md))
- Convolution over $\mathbb C[y]/(y^r+1)$ is two forward synthetic transforms, pointwise ring products and the opposite transform, keeping one frequency order. (on [Convolution from retained transform layout](synthetic-convolution.md))
- The transforms of pairwise coprime lengths needed for the integer product are rewritten as power-of-two ring convolutions without separate permutation sorts.
- The integer product is assembled from digit convolution, the CRT axis map, the chirp and resampled transforms, the coefficient twist, synthetic convolution and rounding.
- With $p=6b$, $d\approx b^\epsilon$ and $K\approx d^c$, every normalized term of the cost table is at most $p^{1-2\kappa}$, so the total is $O(n(\lg n)^{1-\kappa})$. (on [Parameter choices and cost table](parameters-cost.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S7, S8). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S7**: The transforms of pairwise coprime lengths needed for the integer product are rewritten as power-of-two ring convolutions without separate permutation sorts.
How: resample each coprime length to a slightly larger power-of-two length in tensor form keeping the permutations inside the identity, then turn the middle transform into a chirp convolution

**S8**: The integer product is assembled from digit convolution, the CRT axis map, the chirp and resampled transforms, the coefficient twist, synthetic convolution and rounding.
How: chain the reductions in order, accounting for each change of representation and recovering exact coefficients from approximations
- S8.4: The multiplication algorithm applies the coefficient map, two source transforms, a pointwise product, the opposite transform and the two scalings, then rounds and propagates carries.
  Source: "The source-transform procedures now supply the three transforms needed" (paper)
  > The source-transform procedures now supply the three transforms needed for the radix-digit convolution. Read each stored operand backward from its least significant end in groups of $b$ bits. This produces the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order. Buffer each group on a fixed work tape and read it back most significant bit first, reversing its least-significant-first input order; pad the final short group with leading zeroes. For digit $a_j$, write the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero $w_{\rm c}$-bit imaginary word. This exponent is nonnegative because $p=6b$, and the represented value is exactly $a_j2^{-b-2}$. Append $S-q$ zero coefficient records. Buffering and ordering the groups costs $O(n)$, including the one partial group's padding, and writing the $S$ records costs $O(Sp)$. Together with the initial count and copies, this input conversion costs $O(n+Sp)=O(Tp)$; all $n$ input bits, including leading zeroes, are retained before the final group is padded.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- T1 (on [Arrays on tape, address fields and volume](array-layout.md)): An array on a product of ranges is stored in lexicographic order, so address fields, rows and the bit volume $V$ are positions in the tape stream.
- T2 (on [Elementary stream operations](stream-ops.md)): Splitting an array into streams by a digit or by cyclic rows, applying a pointwise map, and merging cost $O(V)$ tape steps.
- T3 (on [Controlled shifts and rational scalings](controlled-shifts.md)): A target field can be cyclically shifted or multiplied by a unit modulo $q^b$ by an offset computed from earlier fields in $O(V)$ time.
- S1 (on [Rank deficit and the recursive power saving](rank-deficit.md)): Two fixed linear networks exchange two banks of values with signs and restore every auxiliary wire, and their edge residual dimensions sum to $s<Wm$, which gives the recursive power saving.
- S3 (on [Fast interchange of address chunks](chunk-swap.md)): Two disjoint address chunks of $u$ bits can be interchanged in $O(Vu^\tau)$ tape steps for a fixed $\tau<1$, although the intermediate steps form XOR combinations of data.
- S4 (on [Simultaneous butterfly layer](butterfly-layer.md)): Applying $H_0$ to the same bit of up to $d$ address chunks at once costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$ with one final truncation.
- S5 (on [Transform layout and cost](transform-layout.md)): The synthetic Fourier transform over $\mathbb C[y]/(y^r+1)$ on a product of power-of-two axes can be stored and computed with butterfly layers in the stated cost.
- S6 (on [Convolution from retained transform layout](synthetic-convolution.md)): Convolution over $\mathbb C[y]/(y^r+1)$ is two forward synthetic transforms, pointwise ring products and the opposite transform, keeping one frequency order.
- S9 (on [Parameter choices and cost table](parameters-cost.md)): With $p=6b$, $d\approx b^\epsilon$ and $K\approx d^c$, every normalized term of the cost table is at most $p^{1-2\kappa}$, so the total is $O(n(\lg n)^{1-\kappa})$.
- S7.1 (on [Gaussian resampling](resampling.md)): Gaussian-weighted contractions $A,B_0$ satisfy $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ for coprime $s<t$, with both coordinate permutations kept inside the identity.
- S7.2 (on [Multidimensional resampling](tensor-resampling.md)): The tensor product of the one-dimensional identities over $d$ axes, applied one line at a time with chunk interchange for axis movement, gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$.
- S7.3 (on [Bluestein chirp and permutation cancellation](chirp.md)): A chirp identity writes $QF_{\boldsymbol t}u$ as a cyclic convolution with pointwise phases, and the source permutation $R$ cancels between the forward transforms and the opposite one.
- S8.1 (on [Integer product as digit convolution](radix-digit-mult.md)): Splitting each integer into radix-$2^b$ digits turns the product into a convolution modulo $x^S-1$ with no wraparound and coefficients below $2^{3b}$.
- S8.2 (on [Chinese-remainder address map](crt-map.md)): A map $x\mapsto\prod_i x_i^{\mu_i}$ sends convolution on $S=\prod s_i$ points to convolution on pairwise coprime cyclic axes, implemented by triangular controlled shifts.
- S8.3 (on [Coefficient phase twist](coefficient-twist.md)): Mapping $x_d$ to $\zeta y$ with $\zeta=e^{\pi i/r}$ turns cyclic wrap of the last axis into the negative wrap of the ring modulo $y^r+1$.
- S8.5 (on [Fixed-point error control](fixed-point-errors.md)): The error in the recovered coefficients is strictly below $1/2$ under additive error bookkeeping with contractions and truncation, so rounding gives the exact integer coefficients.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The n log n conjecture and its history](nlogn-conjecture.md): Schönhage and Strassen conjectured n log n is the optimal multiplication cost on multitape Turing machines; Harvey and van der Hoeven reached O(n log n), which also serves here as an ordinary subroutine multiplier.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) *<predicate>* The n log n conjecture and its history
- [Integer product as digit convolution](radix-digit-mult.md): Splitting each integer into radix-2^b digits turns multiplication into a convolution of short coefficients; carries are propagated afterwards.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) *<predicate>* Integer product as digit convolution
- [Chinese-remainder address map](crt-map.md): An isomorphism of cyclic convolution on S=∏s_i points onto a product of pairwise coprime cyclic axes, implemented by triangular controlled shifts.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) *<predicate>* Chinese-remainder address map
- [Multidimensional resampling](tensor-resampling.md): The tensor product of the one-dimensional resampling identities over d axes, applied one line at a time, with axis movement done by chunk interchange.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) *<predicate>* Multidimensional resampling
- [Bluestein chirp and permutation cancellation](chirp.md): A chirp identity turns the permuted middle transform into a cyclic convolution with pointwise phases, and the source permutation cancels between forward transforms and the opposite one.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) *<predicate>* Bluestein chirp and permutation cancellation
- [Coefficient phase twist](coefficient-twist.md): Mapping x_d to ζy, ζ=e^{πi/r}, turns cyclic wrap of the last axis into the negative wrap of the ring modulo y^r+1.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) *<predicate>* Coefficient phase twist
- [Convolution from retained transform layout](synthetic-convolution.md): Convolution over the ring: two forward synthetic transforms, pointwise ring products, and the opposite transform, keeping the same frequency order throughout.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) *<predicate>* Convolution from retained transform layout
- [Fixed-point error control](fixed-point-errors.md): Complex values on a grid of spacing 2^{-p} in the unit disk, linear contractions that do not enlarge error, truncation, and additive error bookkeeping.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) *<predicate>* Fixed-point error control
- [Parameter choices and cost table](parameters-cost.md): Choice p=6b, d≈b^ε, K≈d^c and the rational exponents, with a cost table whose every normalized term is at most p^{1−2κ}.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) *<predicate>* Parameter choices and cost table
- [Fast interchange of address chunks](chunk-swap.md): Swapping two disjoint address chunks of u bits in O(V u^τ) tape time for a fixed τ<1, by padding to power widths and base-m pieces.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) *<predicate>* Fast interchange of address chunks
- [Simultaneous butterfly layer](butterfly-layer.md): Applying H0 to the same bit of up to d address chunks at once, using the phase network and packed bit additions, at cost O(V d^λ′) with one final truncation.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) *<predicate>* Simultaneous butterfly layer

## Other pages you may link to

- [Cyclic convolution](convolution.md)
- [Arrays on tape, address fields and volume](array-layout.md)
- [Elementary stream operations](stream-ops.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Rank, subspaces and orthogonal complements](linear-algebra.md)
- [Bank-exchanging linear network with restored scratch](scalar-network.md)
- [Frames and the common-frame invariant](frames.md)
- [Subspace labels from triple indicator vectors](labels.md)
- [Rank deficit and the recursive power saving](rank-deficit.md)
- [Bit network and rational shear interface](bit-interface.md)
- [Lower triangular factorization](bruhat.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Power-width chunk interchange](power-interchange.md)
- [Packed selected-bit addition](packed-addition.md)
- [Polynomial ring modulo y^r+1](synthetic-ring.md)
- [Signed packing for ring products](signed-packing.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly](butterfly.md)
- [Phase frames and the kernel C=aI+bX](phase-interface.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Transform layout and cost](transform-layout.md)
- [Gaussian resampling](resampling.md)

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "\subsection{The multiplication algorithm}" (paper)

  > \subsection{The multiplication algorithm}


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

Write the body to `exegenius/tasks/0037-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0037-write-main-theorem.answer.json`, then run `exegenius submit 0037-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
