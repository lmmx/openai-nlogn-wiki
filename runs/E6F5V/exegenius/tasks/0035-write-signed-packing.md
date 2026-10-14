# exegenius task 0035-write-signed-packing

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F5V` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, counting, induction, primes, gcd), a first algorithms course (divide and conquer, recurrences, sorting, Karatsuba multiplication, schoolbook arithmetic) and complexity (big-O family, single- and multitape Turing machines), together with calculus (exponentials, logarithms, series), linear algebra over the reals and complex numbers, and polynomials. They have not met Fourier transforms or the FFT in depth, finite fields beyond arithmetic mod 2, bilinear forms over arbitrary fields, number-theoretic estimates such as prime density, or any research-level multiplication algorithm; those are what the wiki must explain.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Binary integers
- Modular arithmetic
- Matrices, rank and linear maps
- Fixed-tape Turing machine model
- Arrays, address fields and logical volume
- Elementary stream operations
- Controlled cyclic shifts and rational scalings
- Cyclic convolution
- Normalized discrete Fourier transform
- Multidimensional transforms and convolution on several axes
- Fixed-point complex arithmetic and truncation error
- Integer multiplication as digit convolution
- Established O(n log n) integer multiplier
- The n log n optimality conjecture
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal variable of the polynomials, which satisfies y^r = −1 in the quotient.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Decimation-in-frequency butterflies and bit-reversed frequency order
- Bluestein chirp identity
- Role networks and frames
- Restoring arbitrary scratch values
- Three-subset gather and scatter network
- Nondegenerate subspaces and orthogonal residuals
- Subspace labels and the rank budget
- Rank saving and the power-saving recurrence
- Lower-triangular factorization of a matrix
- Cost of a rational matrix shear
- Bit network as an address shear
- Power-width address interchange
- Fast interchange of address chunks
- Two-point butterfly H₀ and the kernel C
- Binary phase frames
- Packed selected-bit addition
- Simultaneous butterfly layer
- Transform layout and cost
- Big-Theta, big-Omega and little-o notation (also: Theta, Omega, Θ, Ω, little-o, o(1), asymptotic notation)
- Divide-and-conquer recurrences (also: recurrence relation, master theorem, recursion tree, solving recurrences)
- Schoolbook and Karatsuba multiplication (also: long multiplication, Karatsuba, Toom-Cook, grade-school multiplication)
- Positional notation in any radix and mixed radix (also: radix-q digits, base-q representation, mixed-radix expansion, digit string, most significant digit)
- Bitwise operations, XOR and Hamming weight (also: XOR, exclusive or, addition mod 2, bit parity, wt, popcount, Hamming weight)
- Floor, ceiling and rounding (also: ⌊x⌋, ⌈x⌉, round to nearest integer, integer part)
- Exponential and logarithm functions (also: log base 2, lg, natural logarithm, ln, exp, e^x, Gaussian function)
- Convergent series and the geometric series (also: absolutely convergent sum, infinite sum, geometric series, tail bound, series convergence)
- Prime numbers, coprimality and trial division (also: relatively prime, pairwise coprime, gcd, odd prime, primality by trial division, unique factorization)
- Extended Euclidean algorithm (also: Euclid's algorithm, Bezout identity, computing modular inverses)
- Counting subsets and binomial coefficients (also: n choose k, binomial coefficient, k-subsets, inclusion-exclusion, ground set)
- Permutations and permutation matrices (also: bijection of indices, reordering of coordinates, involution, permutation of positions, partial permutation)
- Lexicographic order and Cartesian products of index sets (also: lexicographic order, product of ranges, multi-index, tuple addressing, row-major order)
- Vector norms, inner products and orthogonality (also: maximum norm, sup norm, infinity norm, triangle inequality, dot product, orthonormal basis, orthogonal complement, isometry)
- Gaussian elimination (also: row reduction, row operations, elementary matrices, echelon form)
- Dyadic rationals and binary fractions (also: dyadic numbers, numbers m/2^k, binary point, fixed-point numbers, Gaussian dyadics, Gaussian integers)
- Stable radix sort and counting sort (also: bit sorting, stable sorting, radix sorting, sorting by a key digit)
- Mathematical induction (also: induction on k, proof by induction, recursive construction)

## This page

Concept: Signed packing (Kronecker substitution)
Gloss: A product of two disk-grid polynomials is computed exactly by evaluating their integer parts at a large base 2^{4p}, multiplying the resulting integers with the O(N log N) multiplier, and reading centered coefficients back out, then wrapping modulo y^r + 1.

## This page in the argument

The step: A product of two disk-grid polynomials is computed exactly by evaluating their integer parts at the base $2^{4p}$, multiplying the resulting integers with the $O(N\log N)$ multiplier, reading centered coefficients back out, and wrapping modulo $y^r+1$, in time $O(rp\log(rp))$.
How: Use Kronecker substitution with signs: pack each coefficient list into one integer, multiply, and extract each product coefficient as the centered residue modulo the base.
Why: The established integer multiplier is the only fast product available on the fixed-tape model, so polynomial products are turned into integer products. (the sources say so: "To multiply the polynomial records, we use the fixed-tape integer multiplier of Harvey and van der Hoeven" (paper))

Its sub-steps, in order:

- The four products of the absolute values of the packed integers are computed with the established multiplier and their signs restored.
- Every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<B_0/2$, so coefficients cannot collide at base $B_0=2^{4p}$.
- Reading blocks with a bounded carry and centering modulo $B_0$ recovers each coefficient $h_j$ exactly.
- The product is reduced modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$.
- Four exact integer products dominate all the linear packing, extraction and truncation costs.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, using fast address interchange and fast simultaneous butterfly layers inside a Gaussian-resampling, chirp and synthetic-transform reduction.; how: Reduce the product to a convolution evaluated through Gaussian-resampled, chirped synthetic transforms, make the two costly tape operations (address movement and butterfly layers) cheaper by a power of the logarithm using networks with a rank saving, and then assemble the algorithm and add up its costs. (on [Integer multiplication below n log n](main-theorem.md))
- Normalized convolution over the negacyclic ring is computed by two forward synthetic transforms, pointwise polynomial products in the retained frequency order, and the opposite transform, with error below $\sqrt2\,M(3\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.; how: Transform both operands keeping the layout $LB$, multiply the records pointwise in that order using signed packing and the $O(N\log N)$ multiplier, and apply the opposite transform to the retained order. (on [Convolution from the retained transform layout](ring-convolution.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S7.1.1, S7.1.2, S7.1.3, S7.1.4, S7.1.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S7.1.1**: The four products of the absolute values of the packed integers are computed with the established multiplier and their signs restored.
Source: "Multiply the four pairs of absolute values using the established multiplier and restore each product's sign." (paper)
> teger numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\log(rp))$ on a fixed number of tapes. The output is a disk grid polynomial with error less than $\sqrt2\,2^{-p}$ from $fg/r$. \end{lemma} \begin{proof} The supplied power of two $r$ determines $\ell=\log_2r$. Write \[ f=2^{-p}(a+ib),\qquad g=2^{-p}(c+ie), \] where $a,b,c,e\in\mathbb Z[y]$ have degree less than $r$ and coefficients of absolute value at most $2^p$. Set $B_0=2^{4p}$ and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values using the established multiplier and restore each product's sign. The resulting integers are $A_aA_c,A_bA_e,A_aA_e,A_bA_c$. For example, if $h=ac$ is the ordinary product in $\mathbb Z[y]$, then \[ A_aA_c=(ac)(B_0)=\sum_{j=0}^{2r-2}h_jB_0^j. \] The other three evaluation products have the same form. Every coefficient in any of these ordinary polynomial products satisfies \begin{equation} |h_j|\leq r2^{2p}<2^{3p}<B_0/2. \label{eq:packing-separation} \end{equation} After the lower coefficients have been removed from an evaluation, this strict bound identifies the next coefficient by its centered residue modulo $B_0$.

**S7.1.2**: Every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<B_0/2$, so coefficients cannot collide at base $B_0=2^{4p}$.
Source: "|h_j|\leq r2^{2p}<2^{3p}<B_0/2." (paper)
> oefficients of absolute value at most $2^p$. Set $B_0=2^{4p}$ and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values using the established multiplier and restore each product's sign. The resulting integers are $A_aA_c,A_bA_e,A_aA_e,A_bA_c$. For example, if $h=ac$ is the ordinary product in $\mathbb Z[y]$, then \[ A_aA_c=(ac)(B_0)=\sum_{j=0}^{2r-2}h_jB_0^j. \] The other three evaluation products have the same form. Every coefficient in any of these ordinary polynomial products satisfies \begin{equation} |h_j|\leq r2^{2p}<2^{3p}<B_0/2. \label{eq:packing-separation} \end{equation} After the lower coefficients have been removed from an evaluation, this strict bound identifies the next coefficient by its centered residue modulo $B_0$.

**S7.1.3**: Reading blocks with a bounded carry and centering modulo $B_0$ recovers each coefficient $h_j$ exactly.
Source: "Thus $\widehat h_j=h_j$." (paper)
> The meaning of the carry is the following residual identity, after coefficients below $j$ have been correctly extracted: \[ \sum_{k=j}^{J-1}h_kB_0^{k-j} =\sum_{k=j}^{J-1}q_kB_0^{k-j} +\rho_j+\varepsilon B_0^{J-j}. \] At $j=0$ this is the equality between the two representations of $Z=h(B_0)$, with $\rho_0=0$. For $j<J$, reduction modulo $B_0$ gives $h_j\equiv q_j+\rho_j\pmod{B_0}$. By \eqref{eq:packing-separation}, including the padded value $h_{J-1}=0$, the unique centered representative is $h_j$ itself. Thus $\widehat h_j=h_j$. Subtracting this coefficient and dividing the residual identity by $B_0$ gives the next identity, with exactly the displayed update for $\rho_{j+1}$. At $j=J$ the identity is $0=\rho_J+\varepsilon$. Hence a negative product has final carry $1$, canceled by its sign extension $\varepsilon=-1$; a nonnegative product has final carry zero. The machine implements the induction by reading one block and updating this constant-size carry at each step, so extraction costs $O(rp)$.

**S7.1.4**: The product is reduced modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$.
Source: "To reduce them modulo $y^r+1$, subtract the coefficient at $j+r$ from the one at $j$ for $0\leq j<r$," (paper)
> The real and imaginary numerator streams are respectively $ac-be$ and $ae+bc$. To reduce them modulo $y^r+1$, subtract the coefficient at $j+r$ from the one at $j$ for $0\leq j<r$, treating a missing coefficient as zero. Splitting the two halves to tapes aligns these terms in one further scan. For each first input index $j_1\in\{0,\ldots,r-1\}$, exactly one second index $j_2$ in that range satisfies $j_1+j_2\equiv j\pmod r$. Its sign is positive when $j_1+j_2=j$ and negative when $j_1+j_2=j+r$. Thus each resulting Gaussian integer coefficient $H_j$ is a sum of exactly $r$ signed products of Gaussian integer input coefficients of modulus at most $2^p$. Consequently \[ |H_j|\leq r2^{2p}. \] The same triangle inequality before imposing the disk bound gives $\|fg/r\|_\infty\leq\|f\|_\infty\|g\|_\infty$; in particular the normalized product of disk polynomials lies in the disk. All intermediate coefficient additions fit in $O(p)$ bits. The width-$4p$ packing fields and the exact multiplier output prevent overflow or ambiguity between adjacent fields.

**S7.1.5**: Four exact integer products dominate all the linear packing, extraction and truncation costs.
Source: "Four exact integer products dominate the linear packing, extraction, combination, wrapping, and truncation costs." (paper)
> Finally the $p$-bit grid numerator of the normalized product is \[ \operatorname{trunc}_0\left(\frac{\Re H_j}{2^{p+\ell}}\right) +i\operatorname{trunc}_0\left(\frac{\Im H_j}{2^{p+\ell}}\right). \] To implement it, shift the absolute magnitude right by $p+\ell$ bits and restore its sign, at cost $O(p)$ per coefficient. The returned coefficient is $2^{-p}$ times this numerator, namely $Q_p(2^{-2p}H_j/r)$; \eqref{eq:transform-truncate} proves its error and disk bounds. Each returned component numerator has magnitude at most $2^p$, so write it as a signed $w$-bit two's-complement word, most significant bit first, with the real word before the imaginary word and coefficient indices in increasing order. This costs $O(rw)=O(rp)$ and supplies the format used by the opposite transform. Four exact integer products dominate the linear packing, extraction, combination, wrapping, and truncation costs. \end{proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Polynomial ring modulo y^r + 1](negacyclic-ring.md): The ring of complex polynomials of degree below r with y^r = −1, where multiplying by y^a only permutes coefficients and flips some signs, so powers of y act as exact roots of unity.
  Shown as: Signed packing (Kronecker substitution) *<predicate>* Polynomial ring modulo y^r + 1
- [Established O(n log n) integer multiplier](nlogn-multiplier.md): The Harvey–van der Hoeven multitape algorithm multiplying N-bit integers in O(N log N), used here only as a black-box subroutine on short records.
  Shown as: Signed packing (Kronecker substitution) *<predicate>* Established O(n log n) integer multiplier
- [Fixed-point complex arithmetic and truncation error](fixed-point-numerics.md): Complex values are stored as pairs of signed integers over a 2^p grid inside the unit disk, truncated toward zero by Q_p; contractions pass errors through unchanged and errors of composed steps add.
  Shown as: Signed packing (Kronecker substitution) *<predicate>* Fixed-point complex arithmetic and truncation error

## Pages that build on this one

- Convolution from the retained transform layout: Normalized convolution over the negacyclic ring is computed by two forward synthetic transforms, pointwise polynomial products in the retained frequency order, and the opposite transform, with explicit error bound.

## Other pages you may link to

- [Two-point butterfly H₀ and the kernel C](two-point-butterfly.md)
- [Fixed-tape Turing machine model](multitape-model.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Arrays, address fields and logical volume](array-layout.md)
- [Role networks and frames](gate-network-frames.md)
- [Elementary stream operations](elementary-streams.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Restoring arbitrary scratch values](scratch-restoration.md)
- [Three-subset gather and scatter network](subset-intersection-network.md)
- [Nondegenerate subspaces and orthogonal residuals](nondegenerate-subspaces.md)
- [Subspace labels and the rank budget](subspace-labels.md)
- [Rank saving and the power-saving recurrence](rank-saving-recurrence.md)
- [Bit network as an address shear](bit-network-interface.md)
- [Binary phase frames](phase-interface.md)
- [Lower-triangular factorization of a matrix](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Power-width address interchange](power-width-interchange.md)
- [Fast interchange of address chunks](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Multidimensional transforms and convolution on several axes](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Decimation-in-frequency butterflies and bit-reversed frequency order](butterfly-recursion.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout and cost](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Cancellation of the retained source permutation](permutation-cancellation.md)
- [Tensor resampling on a padded box](tensor-resampling-box.md)
- [Choosing prime source lengths](prime-lengths.md)
- [Size parameters of the multiplication](size-parameters.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Phase twist from cyclic to negacyclic](coefficient-twist.md)
- [Source Fourier transform procedure](source-transform.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Precision and exact recovery](exact-recovery.md)
- [Cost table and the saving exponent κ](time-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The reduction is a signed form of Kronecker substitution" (paper)

  > To multiply the polynomial records, we use the fixed-tape integer multiplier of Harvey and van der Hoeven~\cite[Theorem~1.1]{HarveyHoeven2021}, with cost $O(N\log(2N))$ on $N$-bit inputs. This is an independent subroutine. Its inputs below have $O(rp)$ bits, and we include the conversions between coefficient streams and signed integers in the cost. The reduction is a signed form of Kronecker substitution; compare \cite[Lemma~2.5]{HarveyHoeven2021}. We specify the packing and recovery of coefficients to include negative values and the required tape format.

- "One can compute the exact Gaussian integer numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\log(rp))$ on a fixed number of tapes." (paper)

  > \begin{lemma}[Signed packing and normalized ring multiplication] \label{lem:signed-ring-product} Let $r=2^\ell<2^p$ with integers $\ell\geq1$ and $p\geq2$, and fix $C_w>1$. Let $w$ be an integer with $p+2\leq w\leq C_wp$. The input supplies $\Gamma(p)\Gamma(r)\Gamma(w)$ and two disk grid polynomials $f,g\in\mathcal R_r$ in the component format of Proposition~\ref{prop:simultaneous-layer} with width $w$. One can compute the exact Gaussian integer numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\log(rp))$ on a fixed number of tapes. The output is a disk grid polynomial with error less than $\sqrt2\,2^{-p}$ from $fg/r$. \end{lemma} \begin{proof} The supplied power of two $r$ determines $\ell=\log_2r$. Write \[ f=2^{-p}(a+ib),\qquad g=2^{-p}(c+ie), \] where $a,b,c,e\in\mathbb Z[y]$ have degree less than $r$ and coefficients of absolute value at most $2^p$. Set $B_0=2^{4p}$ and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values using the established multiplier and restore each produ


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

Write the body to `exegenius/tasks/0035-write-signed-packing.answer.md` and the JSON to `exegenius/tasks/0035-write-signed-packing.answer.json`, then run `exegenius submit 0035-write-signed-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0035-write-signed-packing`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
