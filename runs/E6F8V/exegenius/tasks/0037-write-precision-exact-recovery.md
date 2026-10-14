# exegenius task 0037-write-precision-exact-recovery

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F8V` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: algorithm analysis with big-O, divide and conquer and sorting, discrete mathematics (sets, permutations, modular arithmetic, primes, induction), and introductory linear algebra (matrices, linear maps, invertibility, triangular and permutation matrices). They know polynomials and complex numbers including roots of unity and Euler's formula, basic calculus functions, and basic Turing machines with several tapes and head movements. They have probably met schoolbook and Karatsuba multiplication and the idea of the FFT, but have not studied abstract algebra beyond basics, finite-field theory, numerical analysis of error, multidimensional Fourier methods, or the Schönhage–Strassen line of fast multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n barrier
- Convolution
- Radix-digit convolution
- Discrete Fourier transform
- Fast Fourier transform with butterflies
- Fixed-point complex grid and truncation
- Contractions and error accounting
- Subspaces, rank and orthogonal complements
- Arrays as address fields on tape
- Controlled cyclic shift
- Scratch-restoring bank exchange
- Frames: changing representation along a network
- Triple-subset labels and the rank budget
- Address shear and triangular factorization
- Recursive rank saving
- Power-width chunk interchange
- Address chunk interchange
- Complex phase network
- Packed selected-bit addition
- Simultaneous butterfly layer
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal polynomial variable whose powers act as roots of unity because y^r=−1.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Retained frequency order
- Transform layout on tape
- Signed packing (Kronecker substitution)
- Normalized convolution over the polynomial ring
- Cyclic-to-negacyclic coefficient twist
- Bluestein chirp identity
- Gaussian resampling
- Retained permutation cancellation
- Chinese-remainder address map
- Source transform on the padded box
- Parameter regime for the multiplier
- Binary numerals and bit strings (also: binary representation, bit string, binary expansion, most significant bit, bits)
- Positional notation in any radix (also: base-b representation, radix, digits in base b, mixed radix)
- Integer division with remainder, floor and ceiling (also: Euclidean division, quotient and remainder, floor function, ceiling function, rounding to nearest integer)
- Modular arithmetic (also: congruence, residues mod m, integers mod m, Z/mZ, clock arithmetic)
- Arithmetic modulo 2 and XOR (also: XOR, exclusive or, bitwise XOR, parity, F_2, GF(2), addition mod 2)
- Primes, coprimality and gcd (also: prime number, relatively prime, greatest common divisor, pairwise coprime, Euclid's algorithm)
- Roots of unity and Euler's formula (also: e^{i theta}, primitive root of unity, nth roots of unity, unit circle, complex exponential)
- Exponential, logarithm and Gaussian function (also: exp, log base 2, lg, natural logarithm, e^{-x^2}, bell curve)
- Asymptotic notation beyond big-O (also: Omega, Theta, little-o, liminf, limit inferior, omega notation)
- Geometric series and sums (also: geometric sum, geometric progression, summation, telescoping)
- Divide and conquer and recurrences (also: recursion, recurrence relation, master theorem, recursion tree, T(n)=aT(n/b)+f(n))
- Schoolbook and Karatsuba multiplication (also: long multiplication, grade-school multiplication, Karatsuba algorithm, O(n^2) multiplication, integer multiplication)
- Sorting and its cost (also: merge sort, comparison sorting, O(n log n) sorting, sorting algorithms)
- Permutations and bijections (also: permutation, bijection, one-to-one correspondence, inverse permutation, reordering)
- Sets, subsets and Cartesian products (also: subset, Cartesian product, indicator vector, characteristic vector, tuples, set intersection, intersection size)
- Multidimensional arrays and row-major order (also: lexicographic order, row-major order, array indexing, nested loops, matrix as array)
- Matrices, vectors and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, linear transformation, linear operator, linear combination, vector space, linear independence, basis, dimension)
- Triangular and permutation matrices (also: lower-triangular matrix, upper-triangular matrix, permutation matrix, LU decomposition, identity matrix, diagonal matrix)
- Dot product, inner product and orthogonality (also: inner product, scalar product, orthogonal vectors, orthonormal, bilinear form)
- Dyadic rationals and fixed-width numerators (also: dyadic fraction, binary fraction, number over a power of two, binary point)
- Matrix transposition (also: transpose, row-major to column-major, transposing an array)
- Triangle inequality and norms (also: maximum norm, sup norm, modulus inequality, |a+b|<=|a|+|b|, error bound)
- Mathematical induction and proof by contradiction (also: induction, inductive proof, proof techniques)
- Cyclic shifts and rotations of lists (also: circular shift, rotation of array, wrap-around shift, cyclic rotation)
- Subroutines and composition of algorithms (also: calling a procedure, black box subroutine, reduction, algorithm composition)

## This page

Concept: Precision and exact recovery
Gloss: Disk-margin and error bounds showing the recovered convolution coefficients are within error below 1/2 of integers below 2^{3b}, so rounding and carry propagation give the exact product.

## This page in the argument

The step: The recovered convolution coefficients are within error below $1/2$ of integers below $2^{3b}$, so rounding and carry propagation give the exact product.
How: Track disk membership and errors of each computed map by contraction bounds, accumulate $E_{\rm ring}$, the chirp, source and scaled errors, and compare the final error with $1/2$.
Why: The disk bounds needed by every call must be verified, and the final error must be shown to be less than $1/2$. (the sources say so: "disk bounds needed by every call and proves that the final error is" (paper))
Striking feature: Working precision $p=6b$ against scale factors of about $2^{3b+o(b)}$ leaves a final error of about $2^{-b+\gamma}$ with $\gamma=o(b)$, so it is far below $1/2$. (explain why it holds, from the method)

Its sub-steps, in order:

- The error of the normalized ring convolution is $E_{\rm ring}=M(3L+2)<5TL$ with $L=\log_2T$, and the output stays in the disk.
- The computed chirp transform has error below $8TL\,2^{-p}$.
- The source transform has error at most $E_s\,2^{-p}$ with $E_s=9\cdot2^\gamma TL$.
- After the first scale, the array $\widetilde w$ approximates $w=(u*v)/S$ with error below $E_w2^{-p}$, $E_w=S(3E_s+2)<28\cdot2^\gamma T^2L$.
- After the second scaling the absolute error is below $448b\,2^{-3b/4}<1/2$, so the nearest integer is the correct coefficient.
- The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$ with $Q_0=2^b$, so carry propagation yields the exact radix digits of the product.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Build two faster tape procedures (address chunk interchange and simultaneous butterfly layers) from rank-saving linear networks, use them in synthetic polynomial transforms and resampled source transforms for a convolution, reduce integer multiplication to that convolution, then prove exactness and add up costs. (on [Integer multiplication below n log n](main-theorem.md))
- The pieces assemble into a multiplier that is correct for every input and whose cost table fits the theorem.; how: Choose compatible parameters, set up digits, the CRT layout, the twist and the source transforms, state the algorithm, verify precision and add up the costs.

## Steps this page derives

The argument gives this page these sub-steps of its step (G.7.1, G.7.2, G.7.3, G.7.4, G.7.5, G.7.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**G.7.1**: The error of the normalized ring convolution is $E_{\rm ring}=M(3L+2)<5TL$ with $L=\log_2T$, and the output stays in the disk.
Source: "E_{\rm ring}:=M(3L+2)<5TL." (paper)
> For disk-grid ring arrays $f,g$, put $M=T/r$. Two normalized synthetic forwards, pointwise polynomial multiplication divided by $r$, and the normalized opposite transform give $(f*g)/(rM^2)$. The exact multiplication by $M$ in Proposition~\ref{prop:synthetic-convolution} then gives $\mathcal M_r(f,g)=(f*g)/T$. Before that multiplication, the three transform errors and the polynomial-product truncation total less than $3L+2$. Thus the error of the returned normalized convolution is bounded by \[ E_{\rm ring}:=M(3L+2)<5TL. \] If one operand has norm at most $.7$, bilinear contraction gives $\|\mathcal M_r(f,g)\|\le.7$. Its computed grid output consequently has norm less than $.7+5TLh_p<.701$ for large $n$. This proves the disk margin after the scale $M$, without clipping the output.

**G.7.2**: The computed chirp transform has error below $8TL\,2^{-p}$.
Source: "<8TLh_p." (paper)
> For its error, the exact operands $a$ and $\overline a\cdot x$ are in the disk because every entry of $a$ has modulus one. The kernel approximation contributes less than $2$ and the first endpoint multiplication contributes less than $4$ when inserted into the exact bilinear contraction $\mathcal M_{\mathbb C}$. The computed convolution contributes less than $6TL$, and the last endpoint multiplication less than $4$. Equation~\eqref{eq:permuted-chirp} identifies the exact result, so \[ \|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\| <(6TL+2+4+4)h_p<8TLh_p. \]

**G.7.3**: The source transform has error at most $E_s\,2^{-p}$ with $E_s=9\cdot2^\gamma TL$.
Source: "E_s=9\,2^\gamma TL," (paper)
> Finally let the input to a source transform have norm at most $.5$. The computed expansion has error less than $dp^2$ and norm less than $.5+dp^2h_p<.51$. It is therefore a permitted chirp input. The chirp output is in the disk by the preceding argument, so each compression call is defined and returns another disk-grid array. Insert the exact contractions $\mathcal A$, $QF_{\boldsymbol t}$, and $\mathcal B_0$ at the computed inputs. The error before the source scale is less than $2dp^2+8TL$. Multiplication by $2^\gamma$ therefore gives error less than $2^\gamma(2dp^2+8TL)h_p$, which is bounded by $E_sh_p$ with \begin{equation}\label{eq:source-error} E_s=9\,2^\gamma TL, \end{equation} because $2dp^2<TL$ eventually. The exact source transform $RF_{\boldsymbol s}$ is a contraction, so the scaled approximation has norm at most $.5+E_sh_p<.501$. Its exact numerator scaling therefore also leaves a disk-grid output without clipping. Conjugation preserves the grid and norm, so the opposite procedure has the same error and disk guarantee. All these margins may be enforced by one fixed cutoff. For example, $b\ge2^{24}$, together with the other eventual construction conditions, makes $dp^2h_p$, $8TLh_p$, $E_sh_p$ and $28\,2^\gamma T^2Lh_p$ smaller than $10^{-3}$.

**G.7.4**: After the first scale, the array $\widetilde w$ approximates $w=(u*v)/S$ with error below $E_w2^{-p}$, $E_w=S(3E_s+2)<28\cdot2^\gamma T^2L$.
Source: "E_w:=S(3E_s+2)<28\,2^\gamma T^2L." (paper)
> Let $G:=RF_{\boldsymbol s}^+$ be the exact opposite contraction. Lemma~\ref{lem:chirp-permutation}, applied to $U=RF_{\boldsymbol s}u$ and $V_1=RF_{\boldsymbol s}v$, gives \[ G(U\cdot V_1)=(u*v)/S^2. \] The computed opposite transform may be applied to $z$ because $\|z\|<.5$. Insert $G$ at that computed input: \[ \begin{aligned} \|\widetilde{\mathscr F}^{+}(z)-G(U\cdot V_1)\| &\le \|\widetilde{\mathscr F}^{+}(z)-Gz\|\\ &\qquad+\|G(z-U\cdot V_1)\|\\ &<(3E_s+2)h_p. \end{aligned} \] The first exact numerator multiplication by $S$ gives $\widetilde w$, approximating $w=(u*v)/S$ with error less than $E_wh_p$, where \[ E_w:=S(3E_s+2)<28\,2^\gamma T^2L. \] Each coefficient of $w$ is an average of $S$ products of coefficients of $u$ and $v$, so $\|w\|<1/16$. The earlier cutoff therefore gives \[ \|\widetilde w\|<1/16+E_wh_p<1/16+10^{-3}<1. \] This proves the disk bound for the computed first scaled result.

**G.7.5**: After the second scaling the absolute error is below $448b\,2^{-3b/4}<1/2$, so the nearest integer is the correct coefficient.
Source: "\le448b\,2^{-3b/4}<\frac12." (paper)
> In tensor order, the unscaled integer coefficient array is $2^{2b+4}S w$. This second occurrence of $S$ reverses the normalization still present in $w$, and $2^{2b+4}$ reverses the two input scales. Both multiplications act exactly on grid numerators. Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than \begin{equation}\label{eq:final-error} 2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b} <448b\,2^{-b+\gamma} \le448b\,2^{-3b/4}<\frac12. \end{equation} The true coefficients are real integers. If $H_j$ is the real numerator after the second scaling, its represented value is $H_j/2^p$. The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.

**G.7.6**: The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$ with $Q_0=2^b$, so carry propagation yields the exact radix digits of the product.
Source: "The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$." (paper)
> To propagate carries, let $Q_0=2^b$. The recovered ordinary coefficients are the $c_j$ in \eqref{eq:capacity}; they are zero for $2q-2<j<S$. With $q=\lceil n/b\rceil$ as above, use the recurrence for $0\le j<S$: \[ k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad k_{j+1}=\left\lfloor\frac{c_j+k_j}{Q_0}\right\rfloor. \] The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$. If this holds at $j$, then \[ c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1), \] which proves the next carry bound. The defining relation $c_j+k_j=d_j+Q_0k_{j+1}$ also gives the exact invariant \[ \sum_{h<j}c_hQ_0^h =\sum_{h<j}d_hQ_0^h+k_jQ_0^j. \] It holds for $j=0$, and the defining relation proves its next instance. The unprocessed terms are multiples of $Q_0^j$, so the identity fixes the first $j$ radix digits of the full product. The value $k_j$ is the carry from the processed coefficients into the remaining positions.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Contractions and error accounting](contraction-error-propagation.md): Linear maps that do not increase the maximum-modulus norm; composing approximations adds their errors, which is how the accumulated numerical error is bounded.
  Shown as: Precision and exact recovery *<predicate>* Contractions and error accounting
- [Source transform on the padded box](tensor-source-transform.md): The approximate source Fourier transform formed by linewise Gaussian maps A, the chirp convolution of length T on the padded power-of-two box, linewise B₀ and an exact 2^γ scale, equal to R F_s on the prime-length source.
  Shown as: Precision and exact recovery *<predicate>* Source transform on the padded box
- [Radix-digit convolution](radix-digit-reduction.md): Writing each n-bit integer as a polynomial in 2^b with b-bit digits, so the integer product is the digit convolution followed by carry propagation.
  Shown as: Precision and exact recovery *<predicate>* Radix-digit convolution

## Pages that build on this one

- The multiplication algorithm: Digit conversion, the CRT map Φ, two forward source transforms, a pointwise product, one opposite transform, two scalings by S, rounding, inverse Φ and carry propagation to output the 2n-bit product.

## Other pages you may link to

- [The n log n barrier](n-log-n-barrier.md)
- [Convolution](convolution.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Cyclic-to-negacyclic coefficient twist](coefficient-twist.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Arrays as address fields on tape](tape-address-model.md)
- [Controlled cyclic shift](controlled-cyclic-shift.md)
- [Scratch-restoring bank exchange](scratch-restoring-exchange.md)
- [Frames: changing representation along a network](array-frames.md)
- [Subspaces, rank and orthogonal complements](rank-and-orthogonal-subspaces.md)
- [Triple-subset labels and the rank budget](subset-intersection-labels.md)
- [Address shear and triangular factorization](address-shear-factorization.md)
- [Recursive rank saving](rank-saving-recurrence.md)
- [Power-width chunk interchange](power-width-interchange.md)
- [Address chunk interchange](address-chunk-interchange.md)
- [Chinese-remainder address map](crt-axis-map.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Fixed-point complex grid and truncation](fixed-point-complex-arithmetic.md)
- [Complex phase network](phase-frame-network.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Fast Fourier transform with butterflies](fft-butterflies.md)
- [Synthetic polynomial transform](synthetic-polynomial-transform.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Retained frequency order](stored-frequency-order.md)
- [Transform layout on tape](transform-tape-layout.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](permutation-cancellation.md)
- [Normalized convolution over the polynomial ring](normalized-ring-convolution.md)
- [Parameter regime for the multiplier](parameter-regime.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product" (paper)

  > Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform. Section~\ref{sec:assembly} removes the known normalizations and digit scales, proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product. A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}. Figure~\ref{fig:multiplication-flow} summarizes these reductions.

- "The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient." (paper)

  > In tensor order, the unscaled integer coefficient array is $2^{2b+4}S w$. This second occurrence of $S$ reverses the normalization still present in $w$, and $2^{2b+4}$ reverses the two input scales. Both multiplications act exactly on grid numerators. Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than \begin{equation}\label{eq:final-error} 2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b} <448b\,2^{-b+\gamma} \le448b\,2^{-3b/4}<\frac12. \end{equation} The true coefficients are real integers. If $H_j$ is the real numerator after the second scaling, its represented value is $H_j/2^p$. The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.


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

Write the body to `exegenius/tasks/0037-write-precision-exact-recovery.answer.md` and the JSON to `exegenius/tasks/0037-write-precision-exact-recovery.answer.json`, then run `exegenius submit 0037-write-precision-exact-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0037-write-precision-exact-recovery`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
