# exegenius task 0032-write-kronecker-packing

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
- The established O(N log N) multiplier
- Subspaces, bilinear forms and orthogonal complements
- Linear network with restored scratch wires (also: motif network, restoration schedule)
- Triple-subset intersection gadgets
- Frames on wire arrays
- Nested subspace labels and the rank deficit (also: s<Wm)
- Recursive power saving from the rank deficit
- Lower triangular factorization
- Matrix shear on address fields
- Fast interchange of address chunks
- Binary phase frames and the two-point kernel C
- Packed selected-bit addition
- Simultaneous butterfly layer
- Synthetic transform tape layout
- Last-coordinate phase twist
- Gaussian resampling
- Error bounds and exact recovery
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

Concept: Signed packing for ring products
Gloss: Multiplying two polynomials in the ring by packing signed coefficients into big integers (Kronecker substitution) and calling an O(N log N) integer multiplier.

## This page in the argument

The step: Two disk-grid polynomials $f,g$ in $\mathcal R_r$ with $p$-bit components can be multiplied exactly and returned as $Q_p(fg/r)$ in time $O(r p\log(r p))$, by packing signed coefficients into big integers (Kronecker substitution) and calling an $O(N\log N)$ integer multiplier on four pairs.
How: Evaluate the real and imaginary numerator polynomials at the base $B_0=2^{4p}$ with signed carries, multiply the four pairs of evaluation integers with the established integer multiplier, extract each product coefficient from its centered residue, and reduce modulo $y^r+1$ and truncate.
Why: A polynomial product is an integer product when the coefficients are packed in blocks wide enough that no coefficient of the product can spill into the next block. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- With base $B_0=2^{4p}$ the evaluation integers $A_u=u(B_0)$ of the numerator polynomials fit in $4pr$ bits, and four products of absolute values give $ac,be,ae,bc$ evaluated at $B_0$.
- Since every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<B_0/2$, centered residues with a carry in $\{0,1\}$ recover each coefficient exactly from the product integer.
- The real and imaginary numerator streams are $ac-be$ and $ae+bc$; reduction modulo $y^r+1$ subtracts the coefficient at $j+r$ from the one at $j$.
- Shifting each numerator magnitude right by $p+\ell$ bits and restoring the sign yields $Q_p(fg/r)$ with error below $\sqrt2\,2^{-p}$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a convolution over a polynomial ring computed by Fourier-type transforms; supply the two fast tape procedures that remove the logarithmic factor from address movement and from butterfly arithmetic, both obtained from linear networks that save a power; then assemble the algorithm and tally every cost. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- On disk-grid arrays over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ indexed by a product of cyclic axes with $T$ coefficients in all and $M=T/r$ records, the normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ is approximated with error below $\sqrt2 M(3\ell+1)2^{-p}$ in time $O(T p[d K+p K^{\tau-1}+\ell d^{\lambda'}+\log(r p)])$, where $\ell=\log_2 r$.; how: Compute the convolution as the scaled opposite transform of the pointwise product of two forward transforms kept in the same frequency order, evaluating the transforms by synthetic radix-2 layers on a layout where the simultaneous butterfly layers apply, and the pointwise polynomial products by signed packing into integer products. (on [Normalized convolution over the ring](synthetic-convolution.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.3.1, S4.3.2, S4.3.3, S4.3.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.3.1**: With base $B_0=2^{4p}$ the evaluation integers $A_u=u(B_0)$ of the numerator polynomials fit in $4pr$ bits, and four products of absolute values give $ac,be,ae,bc$ evaluated at $B_0$.
Source: "Set $B_0=2^{4p}$" (paper)
> fix $C_w>1$. Let $w$ be an integer with $p+2\leq w\leq C_wp$. The input supplies $\Gamma(p)\Gamma(r)\Gamma(w)$ and two disk grid polynomials $f,g\in\mathcal R_r$ in the component format of Proposition~\ref{prop:simultaneous-layer} with width $w$. One can compute the exact Gaussian integer numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\log(rp))$ on a fixed number of tapes. The output is a disk grid polynomial with error less than $\sqrt2\,2^{-p}$ from $fg/r$. \end{lemma} \begin{proof} The supplied power of two $r$ determines $\ell=\log_2r$. Write \[ f=2^{-p}(a+ib),\qquad g=2^{-p}(c+ie), \] where $a,b,c,e\in\mathbb Z[y]$ have degree less than $r$ and coefficients of absolute value at most $2^p$. Set $B_0=2^{4p}$ and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values using the established multiplier and restore each product's sign. The resulting integers are $A_aA_c,A_bA_e,A_aA_e,A_bA_c$. For example, if $h=ac$ is the ordinary product in $\mathbb Z[y]$, then \[ A_aA_c=(ac)(B_0)=\sum_{j=0}^{2r-2}h_jB_0^j. \] The other three evaluation products have the same form. Every coefficient in any of these ordinary polynomial products satisfies \begin{equation} |h_j|\leq r2^{2p}<2^{3p}<B_0/2. \label{eq:packing-separation} \end{eq

**S4.3.2**: Since every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<B_0/2$, centered residues with a carry in $\{0,1\}$ recover each coefficient exactly from the product integer.
Source: "Now let $Z$ be one of the four signed product integers, and let $h$" (paper)
> Now let $Z$ be one of the four signed product integers, and let $h$ be its corresponding ordinary polynomial product. Put $J=2r$ and pad that product by $h_{J-1}=0$. The bound on the evaluation integers gives $|Z|<B_0^J/4$, so $Z$ fits in $J$ blocks of width $4p$. Convert its sign and magnitude to sign-extended two's complement: \[ Z=\sum_{j=0}^{J-1}q_jB_0^j+\varepsilon B_0^J, \qquad 0\leq q_j<B_0,\quad \varepsilon\in\{-1,0\}. \] Zero-fill the unused high blocks; for a negative sign, complement and increment within this fixed width. These conversions take a constant number of scans. Put $\rho_0=0$. At block $j$, let $\widehat h_j$ be the unique integer in $[-B_0/2,B_0/2)$ congruent to $q_j+\rho_j$ modulo $B_0$, and put \[ \rho_{j+1}= \frac{q_j+\rho_j-\widehat h_j}{B_0}. \] The carry belongs to $\{0,1\}$: if $\rho_j$ has this property, then $0\leq q_j+\rho_j\leq B_0$, and centering either leaves this value unchanged or subtracts $B_0$.

**S4.3.3**: The real and imaginary numerator streams are $ac-be$ and $ae+bc$; reduction modulo $y^r+1$ subtracts the coefficient at $j+r$ from the one at $j$.
Source: "The real and imaginary numerator streams are respectively" (paper)
> The real and imaginary numerator streams are respectively $ac-be$ and $ae+bc$. To reduce them modulo $y^r+1$, subtract the coefficient at $j+r$ from the one at $j$ for $0\leq j<r$, treating a missing coefficient as zero. Splitting the two halves to tapes aligns these terms in one further scan. For each first input index $j_1\in\{0,\ldots,r-1\}$, exactly one second index $j_2$ in that range satisfies $j_1+j_2\equiv j\pmod r$. Its sign is positive when $j_1+j_2=j$ and negative when $j_1+j_2=j+r$. Thus each resulting Gaussian integer coefficient $H_j$ is a sum of exactly $r$ signed products of Gaussian integer input coefficients of modulus at most $2^p$. Consequently \[ |H_j|\leq r2^{2p}. \] The same triangle inequality before imposing the disk bound gives $\|fg/r\|_\infty\leq\|f\|_\infty\|g\|_\infty$; in particular the normalized product of disk polynomials lies in the disk. All intermediate coefficient additions fit in $O(p)$ bits. The width-$4p$ packing fields and the exact multiplier output prevent overflow or ambiguity between adjacent fields.

**S4.3.4**: Shifting each numerator magnitude right by $p+\ell$ bits and restoring the sign yields $Q_p(fg/r)$ with error below $\sqrt2\,2^{-p}$.
Source: "Finally the $p$-bit grid numerator of the normalized product is" (paper)
> Finally the $p$-bit grid numerator of the normalized product is \[ \operatorname{trunc}_0\left(\frac{\Re H_j}{2^{p+\ell}}\right) +i\operatorname{trunc}_0\left(\frac{\Im H_j}{2^{p+\ell}}\right). \] To implement it, shift the absolute magnitude right by $p+\ell$ bits and restore its sign, at cost $O(p)$ per coefficient. The returned coefficient is $2^{-p}$ times this numerator, namely $Q_p(2^{-2p}H_j/r)$; \eqref{eq:transform-truncate} proves its error and disk bounds. Each returned component numerator has magnitude at most $2^p$, so write it as a signed $w$-bit two's-complement word, most significant bit first, with the real word before the imaginary word and coefficient indices in increasing order. This costs $O(rw)=O(rp)$ and supplies the format used by the opposite transform. Four exact integer products dominate the linear packing, extraction, combination, wrapping, and truncation costs. \end{proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Polynomial ring modulo y^r + 1](ring-mod-y-r-plus-1.md): The ring of complex polynomials of degree below r in which y^r = −1, so powers of y are roots of unity and multiplying by y^a is a signed cyclic shift of coefficients.
  Shown as: Signed packing for ring products *<predicate>* Polynomial ring modulo y^r + 1
- [The established O(N log N) multiplier](nlogn-multiplier.md): The Harvey–van der Hoeven fixed-tape multiplier with cost O(N log 2N) on N-bit inputs, used only as an ordinary subroutine on short inputs.
  Shown as: Signed packing for ring products *<predicate>* The established O(N log N) multiplier

## Pages that build on this one

- Normalized convolution over the ring: Convolution of arrays over ℂ[y]/(y^r+1) as inverse transform of the pointwise product of forward transforms in the same frequency order, scaled by 1/T, with polynomial products done by signed packing.

## Other pages you may link to

- [The n log n conjecture and prior bounds](nlogn-conjecture.md)
- [Linear network with restored scratch wires](linear-network.md)
- [Frames on wire arrays](frames.md)
- [Arrays as tape streams and elementary scans](tape-streams.md)
- [Fixed-point and Gaussian dyadic arithmetic](fixed-point-dyadics.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Subspaces, bilinear forms and orthogonal complements](linear-algebra-orthogonality.md)
- [Triple-subset intersection gadgets](triple-subset-gadgets.md)
- [Nested subspace labels and the rank deficit](rank-deficit-labels.md)
- [Recursive power saving from the rank deficit](recursive-power-saving.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Matrix shear on address fields](matrix-shear.md)
- [Fast interchange of address chunks](fast-chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly layer](two-point-butterfly.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Multiplication as convolution of radix digits](multiplication-as-convolution.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Error bounds and exact recovery](error-and-exact-recovery.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Binary phase frames and the two-point kernel C](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Synthetic transform tape layout](synthetic-transform-layout.md)
- [Normalized convolution over the ring](synthetic-convolution.md)
- [Resampling with permutations left in the transform](resampling-without-sorting.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Parameter choice and cost table](parameter-choice.md)
- [Chinese-remainder address map](crt-address-map.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "reduction is a signed form of Kronecker substitution" (paper)

  > To multiply the polynomial records, we use the fixed-tape integer multiplier of Harvey and van der Hoeven~\cite[Theorem~1.1]{HarveyHoeven2021}, with cost $O(N\log(2N))$ on $N$-bit inputs. This is an independent subroutine. Its inputs below have $O(rp)$ bits, and we include the conversions between coefficient streams and signed integers in the cost. The reduction is a signed form of Kronecker substitution; compare \cite[Lemma~2.5]{HarveyHoeven2021}. We specify the packing and recovery of coefficients to include negative values and the required tape format.

- "Signed packing and normalized ring multiplication" (paper)

  > \begin{lemma}[Signed packing and normalized ring multiplication] \label{lem:signed-ring-product} Let $r=2^\ell<2^p$ with integers $\ell\geq1$ and $p\geq2$, and fix $C_w>1$. Let $w$ be an integer with $p+2\leq w\leq C_wp$. The input supplies $\Gamma(p)\Gamma(r)\Gamma(w)$ and two disk grid polynomials $f,g\in\mathcal R_r$ in the component format of Proposition~\ref{prop:simultaneous-layer} with width $w$. One can compute the exact Gaussian integer numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\log(rp))$ on a fixed number of tapes. The output is a disk grid polynomial with error less than $\sqrt2\,2^{-p}$ from $fg/r$. \end{lemma} \begin{proof} The supplied power of two $r$ determines $\ell=\log_2r$. Write \[ f=2^{-p}(a+ib),\qquad g=2^{-p}(c+ie


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

Write the body to `exegenius/tasks/0032-write-kronecker-packing.answer.md` and the JSON to `exegenius/tasks/0032-write-kronecker-packing.answer.json`, then run `exegenius submit 0032-write-kronecker-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0032-write-kronecker-packing`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
