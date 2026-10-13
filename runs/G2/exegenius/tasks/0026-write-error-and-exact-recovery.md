# exegenius task 0026-write-error-and-exact-recovery

Project directory: `/home/user/openai-nlogn-wiki/runs/G2` (paths below are relative to it)

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

For these sources: Undergraduate computer science: algorithms and complexity through big-O analysis, recurrences and divide-and-conquer (Karatsuba, FFT-based polynomial multiplication, usually met at the level of the standard recursive FFT), discrete mathematics (modular arithmetic, primes and gcd, sets, functions and permutations, induction), and introductory linear algebra (matrices, rank, bases, inner products, Gaussian elimination, over the reals and probably F_2). Also the basics of complex numbers and Turing machines with multiple tapes. The reader has not studied abstract algebra such as quotient rings or tensor products, finite-field theory beyond F_2, numerical analysis of rounding errors, or the research literature on integer multiplication (Schönhage–Strassen, Fürer, Harvey–van der Hoeven), and has not seen Bluestein, Nussbaumer polynomial transforms or Gaussian resampling.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Bit XOR
- The n log n conjecture and prior bounds (also: Schönhage–Strassen conjecture)
- Arrays as tape streams and elementary scans
- Controlled shifts and rational scalings
- Fixed-point and Gaussian dyadic arithmetic
- Discrete Fourier transform
- Cyclic convolution
- Multiplication as convolution of radix digits
- Multidimensional transform
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Two-point butterfly layer (also: butterfly, H₀)
- Synthetic polynomial transform (also: Nussbaumer polynomial transform)
- Subspaces, bilinear forms and orthogonal complements
- Linear network with restored scratch wires (also: motif network, restoration schedule)
- Triple-subset intersection gadgets
- Frames on wire arrays
- Nested subspace labels and the rank deficit (also: s<Wm)
- Recursive power saving from the rank deficit
- Lower triangular factorization
- Matrix shear on address fields
- Fast interchange of address chunks
- Packed selected-bit addition
- Gaussian resampling
- Asymptotic notation beyond big-O (also: Omega notation, Theta notation, little-o, Ω, Θ, o(n log n))
- Logarithms and binary logarithm (also: lg, log base 2, log_2, ceiling of log)
- Floor and ceiling functions (also: floor, ceiling, ⌊x⌋, ⌈x⌉, integer part)
- Binary representation of integers (also: n-bit integer, bit string, binary expansion, two's complement, signed binary)
- Radix representation and digits (also: base-b expansion, positional notation, radix digits, leading zeroes)
- Schoolbook multiplication and carries (also: grade-school multiplication, long multiplication, quadratic multiplication, carry propagation, addition with carry)
- Divide-and-conquer and recurrences (also: recurrence relation, master theorem, Karatsuba multiplication, recursion, geometric series, geometric sum)
- Fast Fourier transform and FFT multiplication (also: FFT, Cooley-Tukey, radix-2 FFT, O(n log n) polynomial multiplication, evaluation and interpolation)
- Mathematical induction and proof by cases (also: induction, inductive proof, proof by contradiction)
- Sets, subsets and Cartesian products (also: set intersection, cardinality, subset of size three, product set, tuples, indicator vector)
- Functions, bijections and permutations (also: permutation, bijection, inverse function, composition, involution, partial permutation)
- Modular arithmetic and congruences (also: mod, residues, congruence, ℤ/nℤ, integers modulo n, remainder, units modulo n)
- Primes, divisibility and coprimality (also: gcd, greatest common divisor, relatively prime, prime power, coprime, trial division, prime factorization)
- Rational numbers and exact fractions (also: rationals, ℚ, denominator, numerator, dyadic rational)
- Finite fields and the field F_2 (also: GF(2), 𝔽_2, binary field, arithmetic modulo 2, parity)
- Vectors, matrices and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, identity matrix, linear transformation, diagonal matrix, linear combination)
- Rank, basis and dimension (also: linear independence, span, vector space, subspace dimension, rank of a matrix, rank-nullity)
- Gaussian elimination (also: row reduction, row operations, elementary matrices, triangular matrix, lower triangular, upper triangular)
- Inner product, norm and orthonormal basis (also: dot product, orthogonal vectors, orthonormal, unit vector, vector norm, max norm, sup norm, l-infinity norm, unit disk, absolute value of complex number, modulus)
- Roots of unity and Euler's formula (also: e^{iθ}, primitive root of unity, n-th roots of unity, unit circle, geometric series of roots)
- Summation and product notation (also: sigma notation, Σ, Π, indices, Kronecker delta)
- Newton's method (also: Newton iteration, Newton-Raphson, reciprocal by Newton, square root by Newton, quadratic convergence)
- Integer division with remainder (also: quotient and remainder, floor division, integer square root, division algorithm)
- Lexicographic order (also: dictionary order, row-major order, most significant first, mixed radix address)
- Arrays, records and matrix transposition (also: row-major, column-major, transpose, matrix layout, indexing)
- Turing machine running time and model conventions (also: worst-case time, time complexity, unit-cost RAM, random access machine, input and output tapes, finite alphabet, tape heads, scanning and sorting on tapes, linear-time scan, simulation)

## This page

Concept: Error bounds and exact recovery
Gloss: Contraction-based accumulation of approximation errors through all steps, removal of known normalizations and scales, showing the coefficient error is below 1/2 so rounding gives exact integers.

## This page in the argument

The step: Every computed step approximates a contraction with bounded error and every scaling is known, so the recovered coefficients lie within error less than $1/2$ of the true integers, rounding to the nearest integer gives them exactly, and carry propagation gives the exact $2n$-bit product.
How: Measure errors in units of $2^{-p}$, bound each computed step against its exact counterpart by inserting the exact map at the computed input, accumulate through the pipeline while keeping all norms inside the disk with margins, then multiply by the known scales and compare with $1/2$.
Why: Composing approximations adds their errors, provided at each step the exact contraction is inserted at the computed input. (the sources say so: "adds their errors: at each step, insert the exact map at the computed" (paper))

Its sub-steps, in order:

- A linear contraction propagates an input error without increasing it, and for a bilinear contraction with all operands in the disk the two operand errors add.
- The normalized ring convolution has error less than $5TL2^{-p}$ with $L=\log_2T$, the chirp transform less than $8TL2^{-p}$, and the source transform less than $9\cdot2^\gamma TL\,2^{-p}$ while keeping norm below $.501$.
- The computed opposite transform of the truncated product of the two forward transforms differs from the exact value $(u*v)/S^2$ by less than $(3E_s+2)2^{-p}$.
- After the two exact scalings by $S$ and $2^{2b+4}S$ the final absolute error is below $448b\,2^{-3b/4}<1/2$.
- The true coefficients are integers in $[0,2^{3b})$, so the nearest integer to the represented value is the unique correct coefficient.
- Propagating radix-$2^b$ carries from the least significant coefficient keeps $0\le k_j<Q_0^2$ and the invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$, giving the exact product bits.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a convolution over a polynomial ring computed by Fourier-type transforms; supply the two fast tape procedures that remove the logarithmic factor from address movement and from butterfly arithmetic, both obtained from linear networks that save a power; then assemble the algorithm and tally every cost. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- The procedure that extracts radix-$2^b$ digits, applies the Chinese-remainder address map $\Phi$, computes two forward source transforms, a pointwise product and the opposite transform with exact rescalings, rounds, and propagates carries outputs the exact $2n$-bit product.; how: Choose the parameters, place the digits on a product of distinct prime cyclic axes by the Chinese-remainder map, compute the cyclic convolution through resampled transforms in which the middle transform is a chirp convolution evaluated over the polynomial ring after a phase twist, undo the known normalizations, bound the error below $1/2$, round, and propagate carries. (on [The multiplication algorithm](multiplication-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S7.8.1, S7.8.2, S7.8.3, S7.8.4, S7.8.5, S7.8.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S7.8.1**: A linear contraction propagates an input error without increasing it, and for a bilinear contraction with all operands in the disk the two operand errors add.
Source: "A linear contraction propagates an input error without increasing it." (paper)
> Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this subsection. An error of $a$ will mean absolute error less than $ah_p$. A linear contraction propagates an input error without increasing it. For a bilinear contraction $\mathcal M$, replacing its operands gives \[ \|\mathcal M(f',g')-\mathcal M(f,g)\| \le \|f'-f\|\,\|g'\|+\|f\|\,\|g'-g\|. \] When all four operands are in the disk, their two errors therefore add.

**S7.8.2**: The normalized ring convolution has error less than $5TL2^{-p}$ with $L=\log_2T$, the chirp transform less than $8TL2^{-p}$, and the source transform less than $9\cdot2^\gamma TL\,2^{-p}$ while keeping norm below $.501$.
Source: "For disk-grid ring arrays $f,g$, put $M=T/r$.  Two normalized synthetic" (paper)
> For disk-grid ring arrays $f,g$, put $M=T/r$. Two normalized synthetic forwards, pointwise polynomial multiplication divided by $r$, and the normalized opposite transform give $(f*g)/(rM^2)$. The exact multiplication by $M$ in Proposition~\ref{prop:synthetic-convolution} then gives $\mathcal M_r(f,g)=(f*g)/T$. Before that multiplication, the three transform errors and the polynomial-product truncation total less than $3L+2$. Thus the error of the returned normalized convolution is bounded by \[ E_{\rm ring}:=M(3L+2)<5TL. \] If one operand has norm at most $.7$, bilinear contraction gives $\|\mathcal M_r(f,g)\|\le.7$. Its computed grid output consequently has norm less than $.7+5TLh_p<.701$ for large $n$. This proves the disk margin after the scale $M$, without clipping the output.

**S7.8.3**: The computed opposite transform of the truncated product of the two forward transforms differs from the exact value $(u*v)/S^2$ by less than $(3E_s+2)2^{-p}$.
Source: "Let $G:=RF_{\boldsymbol s}^+$ be the exact opposite contraction." (paper)
> Let $G:=RF_{\boldsymbol s}^+$ be the exact opposite contraction. Lemma~\ref{lem:chirp-permutation}, applied to $U=RF_{\boldsymbol s}u$ and $V_1=RF_{\boldsymbol s}v$, gives \[ G(U\cdot V_1)=(u*v)/S^2. \] The computed opposite transform may be applied to $z$ because $\|z\|<.5$. Insert $G$ at that computed input: \[ \begin{aligned} \|\widetilde{\mathscr F}^{+}(z)-G(U\cdot V_1)\| &\le \|\widetilde{\mathscr F}^{+}(z)-Gz\|\\ &\qquad+\|G(z-U\cdot V_1)\|\\ &<(3E_s+2)h_p. \end{aligned} \] The first exact numerator multiplication by $S$ gives $\widetilde w$, approximating $w=(u*v)/S$ with error less than $E_wh_p$, where \[ E_w:=S(3E_s+2)<28\,2^\gamma T^2L. \] Each coefficient of $w$ is an average of $S$ products of coefficients of $u$ and $v$, so $\|w\|<1/16$. The earlier cutoff therefore gives \[ \|\widetilde w\|<1/16+E_wh_p<1/16+10^{-3}<1. \] This proves the disk bound for the computed first scaled result.

**S7.8.4**: After the two exact scalings by $S$ and $2^{2b+4}S$ the final absolute error is below $448b\,2^{-3b/4}<1/2$.
Source: "Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than" (paper)
> In tensor order, the unscaled integer coefficient array is $2^{2b+4}S w$. This second occurrence of $S$ reverses the normalization still present in $w$, and $2^{2b+4}$ reverses the two input scales. Both multiplications act exactly on grid numerators. Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than \begin{equation}\label{eq:final-error} 2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b} <448b\,2^{-b+\gamma} \le448b\,2^{-3b/4}<\frac12. \end{equation} The true coefficients are real integers. If $H_j$ is the real numerator after the second scaling, its represented value is $H_j/2^p$. The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.

**S7.8.5**: The true coefficients are integers in $[0,2^{3b})$, so the nearest integer to the represented value is the unique correct coefficient.
Source: "The true coefficients are real integers.  If $H_j$ is the real" (paper)
> In tensor order, the unscaled integer coefficient array is $2^{2b+4}S w$. This second occurrence of $S$ reverses the normalization still present in $w$, and $2^{2b+4}$ reverses the two input scales. Both multiplications act exactly on grid numerators. Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than \begin{equation}\label{eq:final-error} 2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b} <448b\,2^{-b+\gamma} \le448b\,2^{-3b/4}<\frac12. \end{equation} The true coefficients are real integers. If $H_j$ is the real numerator after the second scaling, its represented value is $H_j/2^p$. The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.

**S7.8.6**: Propagating radix-$2^b$ carries from the least significant coefficient keeps $0\le k_j<Q_0^2$ and the invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$, giving the exact product bits.
Source: "To propagate carries, let $Q_0=2^b$." (paper)
> To propagate carries, let $Q_0=2^b$. The recovered ordinary coefficients are the $c_j$ in \eqref{eq:capacity}; they are zero for $2q-2<j<S$. With $q=\lceil n/b\rceil$ as above, use the recurrence for $0\le j<S$: \[ k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad k_{j+1}=\left\lfloor\frac{c_j+k_j}{Q_0}\right\rfloor. \] The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$. If this holds at $j$, then \[ c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1), \] which proves the next carry bound. The defining relation $c_j+k_j=d_j+Q_0k_{j+1}$ also gives the exact invariant \[ \sum_{h<j}c_hQ_0^h =\sum_{h<j}d_hQ_0^h+k_jQ_0^j. \] It holds for $j=0$, and the defining relation proves its next instance. The unprocessed terms are multiples of $Q_0^j$, so the identity fixes the first $j$ radix digits of the full product. The value $k_j$ is the carry from the processed coefficients into the remaining positions.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Discrete Fourier transform](dft.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fixed-point and Gaussian dyadic arithmetic](fixed-point-dyadics.md): Complex numbers stored as signed two's-complement grid numerators over 2^p, added and scaled exactly with guard bits and truncated once toward zero.
  Shown as: Error bounds and exact recovery *<predicate>* Fixed-point and Gaussian dyadic arithmetic
- [Multiplication as convolution of radix digits](multiplication-as-convolution.md): Splitting both integers into radix-2^b digits makes the product a convolution of the digit coefficient lists, followed by carry propagation.
  Shown as: Error bounds and exact recovery *<predicate>* Multiplication as convolution of radix digits

## Pages that build on this one

- The multiplication algorithm: Digit extraction, the Chinese-remainder map, two forward source transforms, pointwise product, opposite transform, rescaling, rounding and carry propagation yielding the exact 2n-bit product.

## Other pages you may link to

- [The n log n conjecture and prior bounds](nlogn-conjecture.md)
- [Linear network with restored scratch wires](linear-network.md)
- [Frames on wire arrays](frames.md)
- [Arrays as tape streams and elementary scans](tape-streams.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Subspaces, bilinear forms and orthogonal complements](linear-algebra-orthogonality.md)
- [Triple-subset intersection gadgets](triple-subset-gadgets.md)
- [Nested subspace labels and the rank deficit](rank-deficit-labels.md)
- [Recursive power saving from the rank deficit](recursive-power-saving.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Matrix shear on address fields](matrix-shear.md)
- [Fast interchange of address chunks](fast-chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](ring-mod-y-r-plus-1.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly layer](two-point-butterfly.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Last-coordinate phase twist](phase-twist.md)
- [The established O(N log N) multiplier](nlogn-multiplier.md)
- [Binary phase frames and the two-point kernel C](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Synthetic transform tape layout](synthetic-transform-layout.md)
- [Signed packing for ring products](kronecker-packing.md)
- [Normalized convolution over the ring](synthetic-convolution.md)
- [Resampling with permutations left in the transform](resampling-without-sorting.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Parameter choice and cost table](parameter-choice.md)
- [Chinese-remainder address map](crt-address-map.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "coefficient error is strictly below $1/2$" (paper)

  > Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform. Section~\ref{sec:assembly} removes the known normalizations and digit scales, proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product. A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}. Figure~\ref{fig:multiplication-flow} summarizes these reductions.

- "Precision and exact recovery" (paper)

  > \subsection{Precision and exact recovery}


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

Write the body to `exegenius/tasks/0026-write-error-and-exact-recovery.answer.md` and the JSON to `exegenius/tasks/0026-write-error-and-exact-recovery.answer.json`, then run `exegenius submit 0026-write-error-and-exact-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0026-write-error-and-exact-recovery`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
