# exegenius task 0023-write-kronecker-packing

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1V` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: asymptotic analysis (O, Theta, Omega), recursion and induction, discrete mathematics (sets, functions, permutations, graphs, modular arithmetic, primes and gcd, elementary combinatorics), and single-variable calculus. They have taken linear algebra at the level of vectors, matrices, bases, dimension and dot products, and have met complex numbers, polynomials, binary representation, Boolean gates and basic multitape Turing machines. They have not studied abstract algebra beyond residues and the two-element field, Fourier analysis, the FFT, fast integer multiplication, tensor products, or any research-level algorithms or complexity.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed finite-tape machine model
- The n log n optimality conjecture
- Established O(n log n) multiplier (Harvey–van der Hoeven)
- Arrays in lexicographic tape order with address fields
- Elementary stream operations
- Controlled cyclic shifts and rational scalings
- Matrix rank, subspaces and orthogonal complements
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The polynomial variable, which satisfies y^r = −1 and serves as a root of unity.
  - $r$ (coefficient count): The number of complex coefficients in a polynomial record, a power of two.
- Linear exchange network with restored scratch wires
- Frames and the common-frame identity
- Three-element-subset subspace labels
- Rank deficit s < Wm
- Bit exchange network with shear interface
- Lower-triangular factorization of matrices
- Rational matrix shear as field interchanges
- Power-saving recurrence
- Power-width address interchange with rows
- Fast interchange of address chunks
  - $u$ (chunk width): The number of bits in each of the two address chunks being interchanged.
  - $V$ (stored bit volume): The number of data bits stored in the array.
  - $\tau$ (interchange exponent): A fixed constant with 0 < τ < 1 (here 1 − 2^{-50}) in the exponent of the cost.
- Packed selected-bit addition with deterministic repair
- Asymptotic notation beyond big-O (also: Theta notation, Omega notation, little-o, Big-Theta, Big-Omega, Θ, Ω, o(1))
- Logarithms and exponentials (also: lg, log base 2, log n, log log n, powers of two, exponent laws)
- Floor, ceiling and rounding (also: floor function, ceiling function, round to nearest integer, truncation toward zero, integer part)
- Proof by induction and recursion (also: mathematical induction, recursive definition, recurrence relation, geometric series, divide and conquer)
- Sets, subsets and basic combinatorics (also: subset, intersection of sets, cardinality, binomial coefficient, counting, indicator vector, characteristic vector, pigeonhole)
- Functions, bijections and permutations (also: permutation, bijection, composition of functions, inverse function, permutation matrix, one-to-one correspondence)
- Graphs (also: vertices and edges, graph, neighbors, adjacency, directed edge, path in a graph)
- Modular arithmetic (also: residues, congruence, integers mod n, Z/nZ, mod q, remainder, cyclic group of residues)
- Primes, coprimality and gcd (also: prime number, relatively prime, coprime, greatest common divisor, Euclidean algorithm, modular inverse, Chinese remainder theorem, prime factorization)
- Binary field F2 and XOR (also: GF(2), F_2, exclusive or, XOR, mod 2 arithmetic, bitwise xor, parity)
- Positional number representation and carries (also: radix, base-b digits, binary representation, digit expansion, carry propagation, schoolbook multiplication, bit length, most significant digit)
- Dyadic rationals and binary fractions (also: dyadic numbers, binary fraction, fixed-point number, fixed-point arithmetic, scaling by a power of two, shift)
- Exponential function and Gaussian function (also: e^x, Euler's formula, Gaussian function, e^{-x^2}, bell curve, exponential decay, calculus bounds, Taylor series)
- Vectors, matrices and linear maps (also: matrix multiplication, invertible matrix, linear transformation, dot product, inner product, linear independence, basis, dimension, identity matrix, diagonal matrix, transpose, lower triangular matrix, linear combination)
- Vector norms and error bounds (also: norm, Euclidean norm, triangle inequality, operator norm, contraction, sup norm, absolute error, modulus of a complex number)
- Boolean gates and circuits (also: logic gate, wire, circuit, XOR gate, AND gate, fan-out, gate network)
- Determinism and exact versus approximate computation (also: deterministic algorithm, exact arithmetic, rational arithmetic, approximation error, worst-case running time, constant-factor overhead)

## This page

Concept: Signed packing (Kronecker substitution)
Gloss: Multiplies two ring polynomials by evaluating them at B₀=2^{4p} as signed integers, multiplying with the O(N log N) integer multiplier, extracting centered coefficients and wrapping negacyclically.

## This page in the argument

The step: Two ring polynomials with $O(p)$-bit Gaussian-integer coefficients are multiplied exactly by evaluating at $B_0=2^{4p}$ as signed integers, using the $O(N\log N)$ integer multiplier, extracting centered coefficients and wrapping negacyclically, in $O(rp\log(rp))$ time.
How: Use Kronecker substitution with signed packing: evaluate at a large power of two, multiply the evaluation integers, and read the coefficients back.
Why: Evaluating at $B_0$ turns polynomial multiplication into integer multiplication, and the coefficients can be read back because every product coefficient is smaller than $B_0/2$ in absolute value. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Writing $f,g$ with integer numerators of degree below $r$, set $B_0=2^{4p}$ and form the signed evaluation integers $A_u=u(B_0)$.
- The four products of evaluation integers are computed with the established multiplier on their absolute values, restoring signs.
- Every product coefficient satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so a centered residue identifies each coefficient in turn.
- The real and imaginary parts are reduced modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$.
- Four exact integer products dominate the linear packing, extraction and truncation costs.

It serves these steps, from the main result down:

- There is one deterministic fixed-alphabet, fixed-tape Turing machine multiplying $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce the product to a digit convolution computed with Fourier-type transforms on power-of-two axes, and accelerate the transforms' address rearrangements and butterfly layers by a power of the logarithm. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- The normalized convolution over power-of-two axes needed by the multiplication is available, with every cost and error bound, from the synthetic transforms.; how: Build the polynomial-ring convolution from the retained-order synthetic transforms and the signed packing multiplication.
- The normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\mathbb C[y]/(y^r+1)$ is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ time.; how: Transform both operands forward, multiply pointwise in the stored order using signed packing, and apply the opposite transform to that order. (on [Convolution over the polynomial ring from the retained layout](ring-convolution.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (R4.1.1, R4.1.2, R4.1.3, R4.1.4, R4.1.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**R4.1.1**: Writing $f,g$ with integer numerators of degree below $r$, set $B_0=2^{4p}$ and form the signed evaluation integers $A_u=u(B_0)$.
Source: "coefficients of absolute value at most $2^p$.  Set $B_0=2^{4p}$" (paper)
> eq1$ and $p\geq2$, and fix $C_w>1$. Let $w$ be an integer with $p+2\leq w\leq C_wp$. The input supplies $\Gamma(p)\Gamma(r)\Gamma(w)$ and two disk grid polynomials $f,g\in\mathcal R_r$ in the component format of Proposition~\ref{prop:simultaneous-layer} with width $w$. One can compute the exact Gaussian integer numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\log(rp))$ on a fixed number of tapes. The output is a disk grid polynomial with error less than $\sqrt2\,2^{-p}$ from $fg/r$. \end{lemma} \begin{proof} The supplied power of two $r$ determines $\ell=\log_2r$. Write \[ f=2^{-p}(a+ib),\qquad g=2^{-p}(c+ie), \] where $a,b,c,e\in\mathbb Z[y]$ have degree less than $r$ and coefficients of absolute value at most $2^p$. Set $B_0=2^{4p}$ and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values using the established multiplier and restore each product's sign. The resulting integers are $A_aA_c,A_bA_e,A_aA_e,A_bA_c$. For example, if $h=ac$ is the ordinary product in $\mathbb Z[y]$, then \[ A_aA_c=(ac)(B_0)=\sum_{j=0}^{2r-2}h_jB_0^j. \] The other three evaluation products have the same form. Every coefficient in any of these ordinary polynomial products satisfies \begin{equation} |h_j|\leq r2^{2p}<2^{3p}<B_0/2. \label{eq:pac

**R4.1.2**: The four products of evaluation integers are computed with the established multiplier on their absolute values, restoring signs.
Source: "pairs of absolute values using the established multiplier and restore" (paper)
> nteger numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\log(rp))$ on a fixed number of tapes. The output is a disk grid polynomial with error less than $\sqrt2\,2^{-p}$ from $fg/r$. \end{lemma} \begin{proof} The supplied power of two $r$ determines $\ell=\log_2r$. Write \[ f=2^{-p}(a+ib),\qquad g=2^{-p}(c+ie), \] where $a,b,c,e\in\mathbb Z[y]$ have degree less than $r$ and coefficients of absolute value at most $2^p$. Set $B_0=2^{4p}$ and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values using the established multiplier and restore each product's sign. The resulting integers are $A_aA_c,A_bA_e,A_aA_e,A_bA_c$. For example, if $h=ac$ is the ordinary product in $\mathbb Z[y]$, then \[ A_aA_c=(ac)(B_0)=\sum_{j=0}^{2r-2}h_jB_0^j. \] The other three evaluation products have the same form. Every coefficient in any of these ordinary polynomial products satisfies \begin{equation} |h_j|\leq r2^{2p}<2^{3p}<B_0/2. \label{eq:packing-separation} \end{equation} After the lower coefficients have been removed from an evaluation, this strict bound identifies the next coefficient by its centered residue modulo $B_0$.

**R4.1.3**: Every product coefficient satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so a centered residue identifies each coefficient in turn.
Source: "|h_j|\leq r2^{2p}<2^{3p}<B_0/2." (paper)
> oefficients of absolute value at most $2^p$. Set $B_0=2^{4p}$ and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values using the established multiplier and restore each product's sign. The resulting integers are $A_aA_c,A_bA_e,A_aA_e,A_bA_c$. For example, if $h=ac$ is the ordinary product in $\mathbb Z[y]$, then \[ A_aA_c=(ac)(B_0)=\sum_{j=0}^{2r-2}h_jB_0^j. \] The other three evaluation products have the same form. Every coefficient in any of these ordinary polynomial products satisfies \begin{equation} |h_j|\leq r2^{2p}<2^{3p}<B_0/2. \label{eq:packing-separation} \end{equation} After the lower coefficients have been removed from an evaluation, this strict bound identifies the next coefficient by its centered residue modulo $B_0$.

**R4.1.4**: The real and imaginary parts are reduced modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$.
Source: "The real and imaginary numerator streams are respectively" (paper)
> The real and imaginary numerator streams are respectively $ac-be$ and $ae+bc$. To reduce them modulo $y^r+1$, subtract the coefficient at $j+r$ from the one at $j$ for $0\leq j<r$, treating a missing coefficient as zero. Splitting the two halves to tapes aligns these terms in one further scan. For each first input index $j_1\in\{0,\ldots,r-1\}$, exactly one second index $j_2$ in that range satisfies $j_1+j_2\equiv j\pmod r$. Its sign is positive when $j_1+j_2=j$ and negative when $j_1+j_2=j+r$. Thus each resulting Gaussian integer coefficient $H_j$ is a sum of exactly $r$ signed products of Gaussian integer input coefficients of modulus at most $2^p$. Consequently \[ |H_j|\leq r2^{2p}. \] The same triangle inequality before imposing the disk bound gives $\|fg/r\|_\infty\leq\|f\|_\infty\|g\|_\infty$; in particular the normalized product of disk polynomials lies in the disk. All intermediate coefficient additions fit in $O(p)$ bits. The width-$4p$ packing fields and the exact multiplier output prevent overflow or ambiguity between adjacent fields.

**R4.1.5**: Four exact integer products dominate the linear packing, extraction and truncation costs.
Source: "Four exact integer products dominate the linear" (paper)
> Finally the $p$-bit grid numerator of the normalized product is \[ \operatorname{trunc}_0\left(\frac{\Re H_j}{2^{p+\ell}}\right) +i\operatorname{trunc}_0\left(\frac{\Im H_j}{2^{p+\ell}}\right). \] To implement it, shift the absolute magnitude right by $p+\ell$ bits and restore its sign, at cost $O(p)$ per coefficient. The returned coefficient is $2^{-p}$ times this numerator, namely $Q_p(2^{-2p}H_j/r)$; \eqref{eq:transform-truncate} proves its error and disk bounds. Each returned component numerator has magnitude at most $2^p$, so write it as a signed $w$-bit two's-complement word, most significant bit first, with the real word before the imaginary word and coefficient indices in increasing order. This costs $O(rw)=O(rp)$ and supplies the format used by the opposite transform. Four exact integer products dominate the linear packing, extraction, combination, wrapping, and truncation costs. \end{proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md): Complex polynomials of degree below r with y^r = −1, so multiplication by a power of y is a signed cyclic shift of the coefficient list (negacyclic wraparound).
  Shown as: Signed packing (Kronecker substitution) *<predicate>* Polynomial ring modulo y^r + 1
- [Established O(n log n) multiplier (Harvey–van der Hoeven)](nlogn-multiplier.md): The known fixed-tape integer multiplier running in O(N log N) time on N-bit inputs, used here only as an ordinary subroutine on short records.
  Shown as: Signed packing (Kronecker substitution) *<predicate>* Established O(n log n) multiplier (Harvey–van der Hoeven)

## Pages that build on this one

- Convolution over the polynomial ring from the retained layout: Computes normalized convolution of arrays of ring polynomials by two forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform consuming the same stored order.

## Other pages you may link to

- [Fixed finite-tape machine model](fixed-tape-model.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Arrays in lexicographic tape order with address fields](array-order.md)
- [Elementary stream operations](stream-ops.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Matrix rank, subspaces and orthogonal complements](matrix-basics.md)
- [Linear exchange network with restored scratch wires](network.md)
- [Frames and the common-frame identity](frames.md)
- [Three-element-subset subspace labels](subset-labels.md)
- [Rank deficit s < Wm](rank-saving.md)
- [Bit exchange network with shear interface](bit-network.md)
- [Lower-triangular factorization of matrices](lower-triangular.md)
- [Rational matrix shear as field interchanges](matrix-shear.md)
- [Power-saving recurrence](power-saving-recurrence.md)
- [Power-width address interchange with rows](power-interchange.md)
- [Fast interchange of address chunks](chunk-interchange.md)
- [Packed selected-bit addition with deterministic repair](packed-bit-addition.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer multiplication as digit convolution](int-as-convolution.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-2 FFT order](butterfly-fft.md)
- [Complex phase network](phase-network.md)
- [Fixed-point disk grid and error propagation](fixed-point-disk-grid.md)
- [Coefficient twist to negacyclic ring](negacyclic-twist.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Convolution theorem for normalized transforms](convolution-theorem.md)
- [Multidimensional (tensor) transforms](multidim-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling with retained permutations](gaussian-resampling.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Source-permutation cancellation](permutation-cancellation.md)
- [Synthetic transform layout and stored frequency order](transform-layout.md)
- [Convolution over the polynomial ring from the retained layout](ring-convolution.md)
- [Chinese-remainder address map](crt-axis-map.md)
- [Choice of prime source lengths](prime-lengths.md)
- [Complex cyclic convolution by coefficient twist](complex-convolution.md)
- [Source transform procedure](source-transform.md)
- [Rounding and carry propagation to the exact product](exact-recovery.md)
- [The multiplication algorithm](mult-algorithm.md)
- [Parameter choice and cost balance](parameter-balance.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The reduction is a signed form of Kronecker substitution" (paper)

  > To multiply the polynomial records, we use the fixed-tape integer multiplier of Harvey and van der Hoeven~\cite[Theorem~1.1]{HarveyHoeven2021}, with cost $O(N\log(2N))$ on $N$-bit inputs. This is an independent subroutine. Its inputs below have $O(rp)$ bits, and we include the conversions between coefficient streams and signed integers in the cost. The reduction is a signed form of Kronecker substitution; compare \cite[Lemma~2.5]{HarveyHoeven2021}. We specify the packing and recovery of coefficients to include negative values and the required tape format.


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

Write the body to `exegenius/tasks/0023-write-kronecker-packing.answer.md` and the JSON to `exegenius/tasks/0023-write-kronecker-packing.answer.json`, then run `exegenius submit 0023-write-kronecker-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0023-write-kronecker-packing`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
