# exegenius task 0042-write-main-theorem

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F3V` (paths below are relative to it)

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

For these sources: The reader is an undergraduate in computer science who has taken discrete mathematics, data structures and algorithms, introductory theory of computation, and the linear algebra and calculus that accompany such a degree. They are fluent with asymptotic analysis, recurrences, binary representation and bitwise operations, modular arithmetic, matrices and rank, vector spaces over the reals, and complex numbers including roots of unity; they know the schoolbook and Karatsuba multiplication algorithms and what a Turing machine with tapes is. They have not studied abstract algebra beyond basics, the FFT's algebraic variants, number-theoretic transforms, finite fields beyond arithmetic mod 2, analytic number theory, numerical analysis of rounding error, or any bit-complexity multiplication algorithm.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Schönhage–Strassen optimality conjecture
- Harvey–van der Hoeven O(n log n) multiplier
- Cyclic convolution
- Integer product as digit convolution
- Discrete Fourier transform (also: Fourier transform, F_q)
- Multidimensional transform
- Two-point butterfly and radix-two recursion (also: H₀, butterfly layer)
- Contractions and error accumulation
- Chinese-remainder map to prime axes
- Prime axis lengths near powers of two
- Gaussian resampling
- Bluestein chirp identity
- Retained permutations cancel in a convolution
- Polynomial ring modulo y^r + 1 (also: negacyclic ring, R_r)
  - $y$ (ring variable): The formal polynomial variable, satisfying y^r = −1 in the ring.
  - $r$ (ring length): The number of complex coefficients in a ring element, a power of two.
- Coefficient phase twist
- Synthetic polynomial transform
- Stored bit-reversed frequency order
- Signed Kronecker packing
- Convolution over the polynomial ring
- Arrays and elementary stream operations on tape
- Controlled shifts and rational scalings
- Bank-exchange network with restored scratch wires
- Frames on network wires
- Nested subspace labels and orthogonal residuals
- Strict rank saving
- Lower-triangular factorization of a matrix
- Cost of a matrix shear on address fields
- Power-width chunk interchange
- Address chunk interchange
  - $V$ (stored bit volume): The number of data bits stored in the array being permuted.
  - $u$ (chunk width): The number of bits in each of the two interchanged address chunks.
  - $\tau$ (interchange exponent): A fixed constant below one, 1 − 2^{−50}, bounding the power of the width in the cost.
- Phase frames and the two-point kernel C
- Packed selected-bit addition
- Exact dyadic intermediates with one truncation
- Simultaneous butterfly layer
- Transform layout and cost
- Parameter choice for the multiplier
- Exact recovery by rounding and carries
- The multiplication algorithm
- Complete time bound
- Asymptotic notation beyond big-O (also: Omega notation, Theta notation, little-o, o(...), Ω, Θ, asymptotically smaller, worst-case running time)
- Limits and limit inferior (also: liminf, limsup, limit of a ratio, lim inf, eventually, for all sufficiently large n)
- Logarithms, exponentials, floors and ceilings (also: log base 2, lg n, log_2, natural logarithm, floor function, ceiling function, powers of two, iterated logarithm, log star)
- Recurrences and geometric sums (also: recurrence relation, solving recurrences, geometric series, geometric sum, unrolling a recurrence, divide and conquer)
- Positional number systems and carries (also: binary representation, radix representation, base-b digits, bit string, most significant bit, carry propagation, schoolbook addition, padding with leading zeros)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba, divide-and-conquer multiplication, Toom-Cook, quadratic multiplication)
- Bitwise operations and XOR (also: exclusive or, XOR, bitwise exclusive or, addition modulo 2, bit flip, parity, bit shift, bit mask)
- Modular arithmetic (also: integers modulo q, Z/qZ, congruence, residues, units modulo q, invertible residues, arithmetic mod q, Chinese remainder theorem for integers)
- Primes, coprimality and the extended Euclidean algorithm (also: prime numbers, relatively prime, pairwise coprime, gcd, greatest common divisor, Euclid's algorithm, Bezout identity, modular inverse, odd primes, primality testing by trial division)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, unit complex numbers, complex exponential, Euler's formula, twiddle factor, N-th root of unity)
- Matrices and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, linear operator, linear transformation, identity matrix, diagonal matrix, unitary or involution matrix, matrix-vector product, linear combination)
- Vector spaces, subspaces, dimension and rank (also: subspace, span, basis, linear independence, dimension, rank of a matrix, rank-nullity, kernel, image, column space, direct sum, quotient space)
- Inner products, bilinear forms and orthogonal complements (also: bilinear form, dot product, orthogonality, orthogonal complement, orthogonal subspace, nondegenerate pairing, inner product space, pairing)
- Gaussian elimination and triangular matrices (also: row reduction, LU decomposition, lower triangular matrix, upper triangular matrix, elementary row operations, back substitution, unit triangular matrix, row echelon form)
- Permutations, bijections and permutation matrices (also: permutation, bijection, one-to-one correspondence, inverse permutation, partial permutation, reordering of an array, sorting network, transposition of indices, permutation matrix)
- Arithmetic modulo 2 and linear algebra over F_2 (also: F_2, GF(2), binary field, field with two elements, matrices over F_2, GL(m, F_2), mod 2 arithmetic, boolean linear algebra)
- Finite sets, subsets and counting (also: Cartesian product, subset intersection, set cardinality, binomial coefficient, inclusion-exclusion, product of index sets, power set, three-element subsets, pigeonhole)
- Circuits and directed acyclic graphs (also: arithmetic circuit, linear circuit, wires and gates, directed graph, DAG, network of gates, fan-in, source and sink nodes, layered network)
- Vector norms and the triangle inequality (also: sup norm, maximum norm, infinity norm, ‖·‖_∞, modulus bound, triangle inequality, operator norm, error bound, disk bound)
- Fixed-point numbers, dyadic rationals and rounding (also: fixed point arithmetic, dyadic rational, binary fraction, rounding to nearest integer, truncation, round-off error, precision in bits, numbers with p fractional bits, grid of spacing 2^{-p})
- Row-major order and matrix transposition (also: row-major layout, array layout, transposing a matrix, matrix transpose, k×k binary matrix, lexicographic address, two-dimensional array as a list)
- Subroutines and reductions between problems (also: black-box subroutine, reduction, calling a subroutine, oracle call, problem reduction, conditional lower bound, composition of algorithms, uniform algorithm)
- Convolution of sequences (also: linear convolution, polynomial multiplication as convolution, product of coefficient sequences, discrete convolution, convolution theorem)

## This page

Concept: Sub-n-log-n integer multiplication
Gloss: A single deterministic multitape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in this model.
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits in each of the two integers being multiplied.
- $\kappa$ (saving exponent): The fixed constant 2^{−182} giving the power of lg n saved.

## This page in the argument

The step: One deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.
How: Reduce the product to a convolution of short digits evaluated by Fourier transforms, speed up the two costly ingredients (moving data between addresses, and butterfly arithmetic) by a power of a block size using one recursive saving, and total every cost term.
Why: A plain transform scans $\Theta(n)$ bits at each of $\Theta(\log n)$ levels, which already costs $n\log n$, so both the data movement and the arithmetic must be made cheaper than a full scan per level. (the sources say so: "Scanning an array of $\Theta(n)$ stored bits at each of
$\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$.
We therefore need savings in both movement and arithmetic." (paper))
Striking feature: The saving $\kappa=2^{-182}$ is astronomically small, yet it is a genuine power of $\log n$: the running time is $o(n\log n)$ through all input lengths, which refutes an eventual $\Omega(n\log n)$ lower bound. (explain why it holds, from the method)

Its sub-steps, in order:

- All later procedures are built from linear-time tape scans: splitting and merging on a digit, distributing whole rows among a fixed number of streams, and shifting a target field by an offset computed from earlier fields.
- Two disjoint equal-width bit chunks of $u$ bits in an address array of volume $V$ can be interchanged in $O(Vu^\tau)$ steps for a fixed $\tau<1$, by XOR combinations whose final effect is an exact permutation. (on [Address chunk interchange](chunk-interchange.md))
- Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ to one selected bit in each of $D\le d$ address chunks of $K$ bits, on records of $r$ complex coefficients, costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$, instead of $D$ whole-array passes, and is exact up to one final truncation. (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md))
- For arrays on $\prod_i\mathbb Z/t_i\mathbb Z$ with entries in $\mathcal R_r$, the normalised convolution $\mathcal M_r(f,g)=(f*g)/T$ is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ by two forward synthetic transforms, pointwise polynomial products by Kronecker packing, and the opposite transform on the retained order. (on [Convolution over the polynomial ring](ring-convolution.md))
- The source Fourier transform $RF_{\boldsymbol s}$ on prime-length axes equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with cheap Gaussian contractions $\mathcal A,\mathcal B_0$ between the prime axes and the power-of-two axes, and the retained coordinate permutations never need to be executed.
- Digits of $x$ and $y$ are placed on prime cyclic axes by the Chinese-remainder map, transformed by Gaussian resampling around a chirp convolution over $\mathbb C[y]/(y^r+1)$, multiplied pointwise, transformed with opposite sign, rescaled, rounded and carried to give the exact $2n$-bit product. (on [The multiplication algorithm](multiplication-algorithm.md))
- With $V=Tp=\Theta(n)$, the costs divided by $V$ are seven dominant terms $p^{1-g_i}$ with margins $g_i>0$ whose smallest is $2\kappa$, so the total time is $O(n(\lg n)^{1-\kappa})$. (on [Complete time bound](time-bound.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1, S5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1**: All later procedures are built from linear-time tape scans: splitting and merging on a digit, distributing whole rows among a fixed number of streams, and shifting a target field by an offset computed from earlier fields.
How: State the elementary scans once, each costing $O(V)$ on a fixed number of tapes, so later sections can cite them.

**S5**: The source Fourier transform $RF_{\boldsymbol s}$ on prime-length axes equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with cheap Gaussian contractions $\mathcal A,\mathcal B_0$ between the prime axes and the power-of-two axes, and the retained coordinate permutations never need to be executed.
How: Use Gaussian resampling for the change of length, keep both permutations inside the transform identity, evaluate the middle transform by a chirp convolution, and cancel the source permutation across the pair of forward transforms and the opposite transform.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2 (on [Address chunk interchange](chunk-interchange.md)): Two disjoint equal-width bit chunks of $u$ bits in an address array of volume $V$ can be interchanged in $O(Vu^\tau)$ steps for a fixed $\tau<1$, by XOR combinations whose final effect is an exact permutation.
- S3 (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)): Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ to one selected bit in each of $D\le d$ address chunks of $K$ bits, on records of $r$ complex coefficients, costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$, instead of $D$ whole-array passes, and is exact up to one final truncation.
- S4 (on [Convolution over the polynomial ring](ring-convolution.md)): For arrays on $\prod_i\mathbb Z/t_i\mathbb Z$ with entries in $\mathcal R_r$, the normalised convolution $\mathcal M_r(f,g)=(f*g)/T$ is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ by two forward synthetic transforms, pointwise polynomial products by Kronecker packing, and the opposite transform on the retained order.
- S6 (on [The multiplication algorithm](multiplication-algorithm.md)): Digits of $x$ and $y$ are placed on prime cyclic axes by the Chinese-remainder map, transformed by Gaussian resampling around a chirp convolution over $\mathbb C[y]/(y^r+1)$, multiplied pointwise, transformed with opposite sign, rescaled, rounded and carried to give the exact $2n$-bit product.
- S7 (on [Complete time bound](time-bound.md)): With $V=Tp=\Theta(n)$, the costs divided by $V$ are seven dominant terms $p^{1-g_i}$ with margins $g_i>0$ whose smallest is $2\kappa$, so the total time is $O(n(\lg n)^{1-\kappa})$.
- S1.1 (on [Arrays and elementary stream operations on tape](tape-stream-operations.md)): Moving or permuting digit values at specified radix positions, splitting on a digit and merging after a pointwise map, and splitting whole rows cyclically into a fixed number of streams each take $O(V)$ steps on an array of volume $V$.
- S1.2 (on [Controlled shifts and rational scalings](controlled-shift.md)): Adding to a later field $y\in[Q]$, $Q=q^b$, an offset computed from earlier control fields, or multiplying it by a rational unit, costs $O(V)$ by splitting blocks and re-merging them.
- S5.1 (on [Gaussian resampling](gaussian-resampling.md)): For coprime $s<t$ with $t/s-1>p/\alpha^4$ there are contractions $A,B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, each computed with error below $p^2$ in $O(tp^{3/2+\delta}\alpha)$ time; tensoring over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ in $O(dTp^{3/2+\delta}\alpha)$.
- S5.2 (on [Retained permutations cancel in a convolution](permutation-cancellation.md)): The factor $QF_{\boldsymbol t}$ equals $\overline a\cdot(a*(\overline a\cdot u))/T$ for the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$, and the retained source permutation cancels: $(RF^+_{\boldsymbol s})[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$ with $S=\prod_is_i$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Discrete Fourier transform](dft.md)
- [Cyclic convolution](cyclic-convolution.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Complete time bound](time-bound.md): Dividing costs by the volume Tp, seven dominant terms with powers of p below one (margins g₁,…,g₇) show total time O(n (lg n)^{1−κ}); the smallest margin is 2κ.
  Shown as: Sub-n-log-n integer multiplication *<predicate>* Complete time bound
- [The multiplication algorithm](multiplication-algorithm.md): Digits are placed on prime axes by the CRT map, transformed by resampling plus chirp convolution over the polynomial ring for both operands, multiplied pointwise, transformed with opposite sign, rescaled, rounded and carried.
  Shown as: Sub-n-log-n integer multiplication *<predicate>* The multiplication algorithm
- [Schönhage–Strassen optimality conjecture](schonhage-strassen-conjecture.md): The 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine; the best earlier bound was the unconditional O(n log n) of Harvey and van der Hoeven.
  Shown as: Sub-n-log-n integer multiplication *<predicate>* Schönhage–Strassen optimality conjecture

## Other pages you may link to

- [Harvey–van der Hoeven O(n log n) multiplier](hh-multiplier.md)
- [Arrays and elementary stream operations on tape](tape-stream-operations.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Bank-exchange network with restored scratch wires](exchange-network.md)
- [Frames on network wires](frames.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Strict rank saving](rank-saving.md)
- [Lower-triangular factorization of a matrix](matrix-factorization.md)
- [Cost of a matrix shear on address fields](matrix-shear.md)
- [Power-width chunk interchange](power-width-interchange.md)
- [Address chunk interchange](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Contractions and error accumulation](contraction-error.md)
- [Exact dyadic intermediates with one truncation](guard-bits.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer product as digit convolution](radix-digit-convolution.md)
- [Coefficient phase twist](phase-twist.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-two recursion](fft-butterfly.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Phase frames and the two-point kernel C](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Stored bit-reversed frequency order](bit-reversed-order.md)
- [Transform layout and cost](transform-layout.md)
- [Convolution over the polynomial ring](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutations cancel in a convolution](permutation-cancellation.md)
- [Chinese-remainder map to prime axes](crt-axis-map.md)
- [Prime axis lengths near powers of two](prime-axis-lengths.md)
- [Parameter choice for the multiplier](parameter-choice.md)

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers." (paper)

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

Write the body to `exegenius/tasks/0042-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0042-write-main-theorem.answer.json`, then run `exegenius submit 0042-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0042-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
