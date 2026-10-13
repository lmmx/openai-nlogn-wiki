# exegenius task 0025-write-gaussian-resampling

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

Concept: Gaussian resampling
Gloss: The Harvey–van der Hoeven method that expresses a Fourier transform of length s (coprime lengths) through a transform whose axis lengths are powers of two, via contractive Gaussian maps.

## This page in the argument

The step: For coprime $s_i<t_i$ with $\theta=t_i/s_i-1>p/\alpha^4$, the Gaussian maps $\mathsf S,\mathsf T$ satisfy $\mathsf TP_{s_i}F_{s_i}=P_{t_i}F_{t_i}\mathsf S$ and $N=C\mathsf T\mathsf D$ is within $2^{-\alpha^2\theta}$ of the identity, which gives contractions $A,B_0$ with $P_{s_i}F_{s_i}=2^{2\alpha^2}B_0P_{t_i}F_{t_i}A$.
How: Express the length-$s_i$ transform through Gaussian-weighted resampling onto a grid of length $t_i$, invert the near-identity selection $N$ by a Neumann series, and normalize the resulting maps so that both are contractions.
Why: Gaussian resampling connects the pairwise coprime lengths needed for the integer product to the powers of two used by the synthetic transforms. (the sources say so: "whereas the synthetic transforms use powers of two. Gaussian resampling" (paper))

Its sub-steps, in order:

- The Gaussian maps $\mathsf S,\mathsf T:\mathbb C^{s_i}\to\mathbb C^{t_i}$ are sums of Gaussians centred at the rescaled points $s_ik/t_i$ and $t_ij/s_i$, and $C$ selects the coordinates nearest $t_ij/s_i$.
- The diagonal map $\mathsf D$ cancels the Gaussian factor at the selected coordinate, so $N-I$ collects only the other summands, $\|N-I\|<2^{-\alpha^2\theta}$, and $N$ is invertible by a Neumann series.
- Setting $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$ with $\mathsf J'=N^{-1}/2$ gives contractions with $B_0P_{t_i}F_{t_i}A=2^{-2\alpha^2}P_{s_i}F_{s_i}$.
- The ordered numerical algorithms for the Gaussian maps run in time $O(t_ip^{3/2+\delta}\alpha)$ with errors below $p^2$, and $C$ is a linear scan selecting an ordered subsequence.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a convolution over a polynomial ring computed by Fourier-type transforms; supply the two fast tape procedures that remove the logarithmic factor from address movement and from butterfly arithmetic, both obtained from linear networks that save a power; then assemble the algorithm and tally every cost. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- For coprime $s_i<t_i$ with enough separation, the tensor Fourier transform $RF_{\boldsymbol s}$ together with its source permutation $R$ equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ for contractions $\mathcal A,\mathcal B_0$ computed line by line on a padded box of $T$ entries in time $O(d T p^{3/2+\delta}\alpha)$ plus axis movements $O(T p\,d^2(1+\ell^\tau))$, with both coordinate permutations left inside the formula.; how: Use Gaussian resampling on each axis but keep the permutations $P_{s_i}$ and $P_{t_i}$ in the identity instead of sorting twice, tensor the one-dimensional identity over $d$ axes, and implement the expansion and compression line by line on the padded box, moving axes into the innermost position with chunk interchanges. (on [Resampling with permutations left in the transform](resampling-without-sorting.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S5.1.1, S5.1.2, S5.1.3, S5.1.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S5.1.1**: The Gaussian maps $\mathsf S,\mathsf T:\mathbb C^{s_i}\to\mathbb C^{t_i}$ are sums of Gaussians centred at the rescaled points $s_ik/t_i$ and $t_ij/s_i$, and $C$ selects the coordinates nearest $t_ij/s_i$.
Source: "The Gaussian resampling argument uses two maps" (paper)
> \begin{proof} The Gaussian resampling argument uses two maps $\mathsf S,\mathsf T:\mathbb C^s\to\mathbb C^t$. For $0\leq k<t$, they are \[ (\mathsf S u)_k=\frac1\alpha\sum_{j\in\mathbb Z} e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j, \qquad (\mathsf T u)_k=\sum_{j\in\mathbb Z} e^{-\pi\alpha^2(tj/s-k)^2}u_j. \] Both sums converge absolutely. For $0\leq j<s$, define \[ q_j=\left\lfloor\frac{tj}{s}+\frac12\right\rfloor, \qquad \beta_j=\frac{tj}{s}-q_j. \] Thus $q_j$ is an integer nearest to $tj/s$, with ties rounded upward. Let $C:\mathbb C^t\to\mathbb C^s$ select these coordinates, and let $\mathsf D:\mathbb C^s\to\mathbb C^s$ be the diagonal map \[ (Cv)_j=v_{q_j},\qquad (\mathsf D u)_j=e^{\pi\alpha^2\beta_j^2}u_j. \] Set $N=C\mathsf T\mathsf D$. In $(Nu)_j$, the summand with index

**S5.1.2**: The diagonal map $\mathsf D$ cancels the Gaussian factor at the selected coordinate, so $N-I$ collects only the other summands, $\|N-I\|<2^{-\alpha^2\theta}$, and $N$ is invertible by a Neumann series.
Source: "Set $N=C\mathsf T\mathsf D$. In $(Nu)_j$, the summand with index $j$" (paper)
> proof} The Gaussian resampling argument uses two maps $\mathsf S,\mathsf T:\mathbb C^s\to\mathbb C^t$. For $0\leq k<t$, they are \[ (\mathsf S u)_k=\frac1\alpha\sum_{j\in\mathbb Z} e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j, \qquad (\mathsf T u)_k=\sum_{j\in\mathbb Z} e^{-\pi\alpha^2(tj/s-k)^2}u_j. \] Both sums converge absolutely. For $0\leq j<s$, define \[ q_j=\left\lfloor\frac{tj}{s}+\frac12\right\rfloor, \qquad \beta_j=\frac{tj}{s}-q_j. \] Thus $q_j$ is an integer nearest to $tj/s$, with ties rounded upward. Let $C:\mathbb C^t\to\mathbb C^s$ select these coordinates, and let $\mathsf D:\mathbb C^s\to\mathbb C^s$ be the diagonal map \[ (Cv)_j=v_{q_j},\qquad (\mathsf D u)_j=e^{\pi\alpha^2\beta_j^2}u_j. \] Set $N=C\mathsf T\mathsf D$. In $(Nu)_j$, the summand with index $j$ is exactly $u_j$: the factor in $\mathsf D$ cancels the Gaussian factor at the selected coordinate $q_j$. The other summands form $((N-I)u)_j$. The exact Gaussian identity and inverse estimate proved in \cite[Theorem~4.2 and Lemma~4.6]{HarveyHoeven2021} give \begin{equation} \mathsf T P_sF_s=P_tF_t\mathsf S, \qquad \|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}. \label{eq:gaussian-public-facts} \end{equation} The first identity uses the negative Fourier sign in our definition of $F_q$; its right-hand permutation is consequently multiplication of the frequency by $-s$. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have $\alpha^2\theta>p/\alpha^2>1$. Thus $\|N-I\|<1/2$, so $N$ is invertible by

**S5.1.3**: Setting $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$ with $\mathsf J'=N^{-1}/2$ gives contractions with $B_0P_{t_i}F_{t_i}A=2^{-2\alpha^2}P_{s_i}F_{s_i}$.
Source: "Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$." (paper)
> uation} \mathsf T P_sF_s=P_tF_t\mathsf S, \qquad \|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}. \label{eq:gaussian-public-facts} \end{equation} The first identity uses the negative Fourier sign in our definition of $F_q$; its right-hand permutation is consequently multiplication of the frequency by $-s$. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have $\alpha^2\theta>p/\alpha^2>1$. Thus $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series. Put \[ \mathsf S'=\mathsf S/2,\qquad \mathsf J'=N^{-1}/2,\qquad \mathsf D'=2^{-(2\alpha^2-2)}\mathsf D. \] The proof of Proposition~4.7(i) in the cited paper gives \[ \|\mathsf S'\|<\frac34,\qquad \|\mathsf J'\|<\frac78,\qquad \|\mathsf D'\|<1. \] Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$. Because $\|C\|=1$, both are contractions. The diagonal map $\mathsf D$ is invertible, and $C\mathsf T=N\mathsf D^{-1}$, so \[ (\mathsf D N^{-1}C)\mathsf T =\mathsf D N^{-1}(N\mathsf D^{-1})=I. \] Applying this left inverse to the first identity in \eqref{eq:gaussian-public-facts} gives $\mathsf D N^{-1}CP_tF_t\mathsf S=P_sF_s$. The normalizations in $\mathsf D'$, $\mathsf J'$, and $\mathsf S'$ have product $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$. Hence \[ B_0P_tF_tA =2^{-2\alpha^2}\mathsf D N^{-1}CP_tF_t\mathsf S =2^{-2\alpha^2}P_sF_s, \] which is \eqref{eq:no-sort-one-dimensional}.

**S5.1.4**: The ordered numerical algorithms for the Gaussian maps run in time $O(t_ip^{3/2+\delta}\alpha)$ with errors below $p^2$, and $C$ is a linear scan selecting an ordered subsequence.
Source: "Lemmas~4.8, 4.9 and 4.12 of" (paper)
> \paragraph{Ordered numerical maps.} Lemmas~4.8, 4.9 and 4.12 of \cite{HarveyHoeven2021} supply the following algorithms. Their inputs and outputs are in increasing coordinate order, and every output is in the disk grid. The record conversions and tape movement needed to use these routines in our format are accounted for below. Their numerical guarantees are \[ \begin{array}{c|c|c} \text{map}&\text{error bound}&\text{time bound}\\ \hline \widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)\\ \widetilde{\mathsf J}'&3p^2/4&O(tp^{3/2+\delta}\alpha)\\ \widetilde{\mathsf D}'&4&O(tp^{1+\delta}). \end{array} \] For $C$, observe that $q_0=0$, $q_{s-1}<t$, and $q_{j+1}>q_j$, because $t/s>1$. Thus $C$ selects an ordered subsequence. A forward scan, with the current input coordinate stored on a work tape, copies a record exactly when that coordinate equals the next $q_j$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Discrete Fourier transform](dft.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Multidimensional transform](multidimensional-transform.md): The tensor product of one-dimensional Fourier transforms along several axes, computing convolution on a product of cyclic groups.
  Shown as: Gaussian resampling *<predicate>* Multidimensional transform
- [Fixed-point and Gaussian dyadic arithmetic](fixed-point-dyadics.md): Complex numbers stored as signed two's-complement grid numerators over 2^p, added and scaled exactly with guard bits and truncated once toward zero.
  Shown as: Gaussian resampling *<predicate>* Fixed-point and Gaussian dyadic arithmetic

## Pages that build on this one

- Resampling with permutations left in the transform: The identity P_s F_s = 2^{2α²} B₀ P_t F_t A (and its tensor form) keeping both coordinate permutations inside the formula instead of sorting twice on each coordinate.
- Parameter choice and cost table: Fixed rational exponents (τ=σ=1−2^{−50}, ε=2^{−75}, κ=2^{−182}, …) and sizes p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log₂T/d⌉} making every cost term a power of p below one.

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
- [Multiplication as convolution of radix digits](multiplication-as-convolution.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Error bounds and exact recovery](error-and-exact-recovery.md)
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

- "Gaussian resampling
connects these two shapes." (paper)

  > The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two. Gaussian resampling connects these two shapes. Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and compute that formula directly. This section proves the resulting interface, including its tape cost when the number of coordinates grows.

- "power-of-two tensor transform" (paper)

  > The remaining proof places these procedures inside the multiplication reduction and accounts for every change of representation. First, the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. Section~\ref{sec:assembly} implements this map through triangular controlled shifts and charged axis moves. Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform. Section~\ref{sec:resampling} retains the source and target coordinate permutations in the transform identity, so they need not be executed as separate full sorts.


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

Write the body to `exegenius/tasks/0025-write-gaussian-resampling.answer.md` and the JSON to `exegenius/tasks/0025-write-gaussian-resampling.answer.json`, then run `exegenius submit 0025-write-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0025-write-gaussian-resampling`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
