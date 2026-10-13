# exegenius task 0032-write-gaussian-resampling

Project directory: `/home/user/openai-nlogn-wiki/runs/G4` (paths below are relative to it)

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

For these sources: The reader has done an undergraduate computer science degree: discrete mathematics (modular arithmetic, primes and gcd, sets, induction, recurrences and asymptotics), basic linear algebra over the reals and complex numbers (matrices, inverses, norms), polynomials and complex roots of unity, and algorithms including divide and conquer and Karatsuba multiplication. On the machine side they know basic single- and multi-tape Turing machines and the idea of counting steps. They have not studied the Fourier transform, FFT-based multiplication, Schonhage-Strassen, Harvey-van der Hoeven, numerical error analysis, abstract algebra beyond rings of residues, finite-field linear algebra, or any lower-bound or advanced tape-algorithm technique, so those must be explained.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape Turing machine model
- Elementary stream operations on tape arrays
- Controlled shifts and rational scalings
- Convolution
- Discrete Fourier transform
- Radix-2 butterflies and FFT
- Subspaces, rank and orthogonal complements
- Fixed-point disk arithmetic and truncation error
- Established O(n log n) integer multiplier
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The polynomial variable, which satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Signed packing of polynomial products
- Two-point kernel C and phase frames
- Frames on pointwise linear networks
- Subset-intersection exchange network
- Subspace labels and the rank budget
- Recursive power saving from a rank deficit
- Bit network shear interface
- Lower triangular (Bruhat-type) factorization
- Cost of a rational matrix shear
- Power-width address interchange
- Fast chunk interchange
- Complex phase network
- Packed selected-bit addition
- Simultaneous butterfly layer
- Synthetic transform layout and cost
- Convolution from the retained transform layout
- Bluestein chirp identity
- Modular arithmetic and residue rings (also: congruence, Z/qZ, integers mod q, residue classes, modular inverse)
- Primes, coprimality and the Euclidean algorithm (also: gcd, greatest common divisor, relatively prime, extended Euclidean algorithm, coprime)
- Positional (radix) number representation (also: base-b expansion, binary representation, digits, binary integers, mixed radix)
- Signed binary numbers and rounding (also: two's complement, sign-magnitude, floor, ceiling, rounding to nearest integer, truncation toward zero)
- Dyadic rationals (also: binary fractions, fractions with power-of-two denominator, fixed-point binary fractions)
- Bitwise operations and Hamming weight (also: XOR, exclusive or, bit string, popcount, Hamming weight, parity)
- Permutations and bijections (also: permutation of indices, bijection, inverse permutation, bit-reversal permutation, transposition)
- Lexicographic order and multi-index addressing (also: row-major order, dictionary order, multidimensional array indexing, mixed-radix address, tuple indices)
- Matrix algebra (also: matrix multiplication, matrix inverse, identity matrix, transpose, invertible matrix, 2x2 matrices, diagonal matrix, matrix-vector product)
- Vector norms and the triangle inequality (also: sup norm, max norm, infinity norm, absolute value bound, modulus bound, triangle inequality)
- Logarithms, exponentials and floor/ceiling in analysis (also: log base 2, lg, powers of two, exponent laws, iterated logarithm, real exponent)
- Theta, Omega and little-o notation (also: big-Theta, big-Omega, little-o, liminf, asymptotic lower bound, tight bound)
- Summations and geometric series (also: geometric sum, telescoping sum, sum of powers, series bound)
- Recurrence relations and divide and conquer (also: recurrence, unrolling a recurrence, master theorem, recursion tree, recursive algorithm, divide-and-conquer)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba, quadratic multiplication)
- Stacks and call stacks (also: stack, recursion stack, call stack, program counter, subroutine call)
- Pointwise operations on lists and vectors (also: componentwise product, Hadamard product, elementwise map, coordinatewise operation)
- Sets, subsets and counting (also: subset, cardinality, intersection, binomial coefficient, ground set, indicator vector, power set)
- Mathematical induction and proof by contradiction (also: induction, inductive proof, contradiction, proof techniques)
- Euler's formula and complex exponentials (also: e^{i theta}, Euler formula, unit circle, phase factor, twiddle factor, modulus of e^{i theta})

## This page

Concept: Gaussian resampling
Gloss: Relating a Fourier transform of coprime length s to one of larger power-of-two length t via Gaussian-weighted contractions A and B_0, as P_sF_s = 2^{2α²} B_0 P_t F_t A.

## This page in the argument

The step: For coprime $s<t$ with $t/s-1>p/\alpha^4$ there are linear contractions $A,B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computable to error below $p^2$ in time $O(tp^{3/2+\delta}\alpha)$.
How: Gaussian resampling: combine the exact Gaussian identity $\mathsf T P_sF_s=P_tF_t\mathsf S$ with an invertible approximate left inverse $N^{-1}$ of the sampling, normalized so that both maps become contractions.
Why: A Fourier transform of length $s$ is related to one of larger length $t$ by Gaussian weights, which are smooth enough that the sampling error is tiny and the maps can be inverted by a Neumann series. (the sources leave this for the reader to work out: spell it out)
Striking feature: Both $A$ and $B_0$ are contractions even though the Gaussian weights alone are not, because the normalizations contribute exactly the factor $2^{-2\alpha^2}$ that is moved to the left side of the identity. (explain why it holds, from the method)

Its sub-steps, in order:

- The exact Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$ holds, with $\|N-I\|<2^{-\alpha^2\theta}$.
- Since $\alpha^2\theta>1$, $\|N-I\|<1/2$ and $N$ is invertible by the Neumann series.
- Set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$; after normalizing, both are contractions.
- Applying the left inverse to the Gaussian identity gives $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in that model.; how: Reduce the product to a cyclic convolution of radix digits evaluated by Fourier-type transforms, make the two costly ingredients of those transforms (address rearrangement and butterfly arithmetic) cost a power of the logarithm less than a full scan per level by two rank-saving tape procedures, then assemble the algorithm, prove exactness and total the cost. (on [Sub-n log n integer multiplication](sub-nlogn-multiplication.md))
- The source transform of pairwise coprime lengths $s_i$ equals $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ for power-of-two lengths $t_i$, with $\mathcal A,\mathcal B_0$ contractions applied along each axis of the padded box in $O(dTp^{3/2+\delta}\alpha)$ time, plus $O(Tp\,d^2(1+\ell^\tau))$ to expose axes.; how: Tensor the one-dimensional resampling identity over the axes, apply the maps line by line on the padded power-of-two box, expose each axis by chunk interchanges, and leave the permutations $R,Q$ inside the transform. (on [Multidimensional resampling on a padded box](tensor-resampling.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S5.1.1, S5.1.2, S5.1.3, S5.1.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S5.1.1**: The exact Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$ holds, with $\|N-I\|<2^{-\alpha^2\theta}$.
Source: "The exact Gaussian identity and inverse estimate proved in" (paper)
> )^2}u_j, \qquad (\mathsf T u)_k=\sum_{j\in\mathbb Z} e^{-\pi\alpha^2(tj/s-k)^2}u_j. \] Both sums converge absolutely. For $0\leq j<s$, define \[ q_j=\left\lfloor\frac{tj}{s}+\frac12\right\rfloor, \qquad \beta_j=\frac{tj}{s}-q_j. \] Thus $q_j$ is an integer nearest to $tj/s$, with ties rounded upward. Let $C:\mathbb C^t\to\mathbb C^s$ select these coordinates, and let $\mathsf D:\mathbb C^s\to\mathbb C^s$ be the diagonal map \[ (Cv)_j=v_{q_j},\qquad (\mathsf D u)_j=e^{\pi\alpha^2\beta_j^2}u_j. \] Set $N=C\mathsf T\mathsf D$. In $(Nu)_j$, the summand with index $j$ is exactly $u_j$: the factor in $\mathsf D$ cancels the Gaussian factor at the selected coordinate $q_j$. The other summands form $((N-I)u)_j$. The exact Gaussian identity and inverse estimate proved in \cite[Theorem~4.2 and Lemma~4.6]{HarveyHoeven2021} give \begin{equation} \mathsf T P_sF_s=P_tF_t\mathsf S, \qquad \|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}. \label{eq:gaussian-public-facts} \end{equation} The first identity uses the negative Fourier sign in our definition of $F_q$; its right-hand permutation is consequently multiplication of the frequency by $-s$. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have $\alpha^2\theta>p/\alpha^2>1$. Thus $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series. Put \[ \mathsf S'=\mathsf S/2,\qquad \mathsf J'=N^{-1}/2,\qquad \mathsf D'=2^{-(2\alpha^2-2)}\mathsf D. \] The proof of Proposition~4.7(i) in the cited paper gives \[ \|\mathsf S'\|<\

**S5.1.2**: Since $\alpha^2\theta>1$, $\|N-I\|<1/2$ and $N$ is invertible by the Neumann series.
Source: "Thus $\|N-I\|<1/2$, so $N$ is invertible" (paper)
> thsf T\mathsf D$. In $(Nu)_j$, the summand with index $j$ is exactly $u_j$: the factor in $\mathsf D$ cancels the Gaussian factor at the selected coordinate $q_j$. The other summands form $((N-I)u)_j$. The exact Gaussian identity and inverse estimate proved in \cite[Theorem~4.2 and Lemma~4.6]{HarveyHoeven2021} give \begin{equation} \mathsf T P_sF_s=P_tF_t\mathsf S, \qquad \|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}. \label{eq:gaussian-public-facts} \end{equation} The first identity uses the negative Fourier sign in our definition of $F_q$; its right-hand permutation is consequently multiplication of the frequency by $-s$. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have $\alpha^2\theta>p/\alpha^2>1$. Thus $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series. Put \[ \mathsf S'=\mathsf S/2,\qquad \mathsf J'=N^{-1}/2,\qquad \mathsf D'=2^{-(2\alpha^2-2)}\mathsf D. \] The proof of Proposition~4.7(i) in the cited paper gives \[ \|\mathsf S'\|<\frac34,\qquad \|\mathsf J'\|<\frac78,\qquad \|\mathsf D'\|<1. \] Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$. Because $\|C\|=1$, both are contractions. The diagonal map $\mathsf D$ is invertible, and $C\mathsf T=N\mathsf D^{-1}$, so \[ (\mathsf D N^{-1}C)\mathsf T =\mathsf D N^{-1}(N\mathsf D^{-1})=I. \] Applying this left inverse to the first identity in \eqref{eq:gaussian-public-facts} gives $\mathsf D N^{-1}CP_tF_t\mathsf S=P_sF_s$. The normalizations in $\mathsf D'$, $\mathsf J'$, and $\mathsf S

**S5.1.3**: Set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$; after normalizing, both are contractions.
Source: "Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$." (paper)
> uation} \mathsf T P_sF_s=P_tF_t\mathsf S, \qquad \|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}. \label{eq:gaussian-public-facts} \end{equation} The first identity uses the negative Fourier sign in our definition of $F_q$; its right-hand permutation is consequently multiplication of the frequency by $-s$. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have $\alpha^2\theta>p/\alpha^2>1$. Thus $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series. Put \[ \mathsf S'=\mathsf S/2,\qquad \mathsf J'=N^{-1}/2,\qquad \mathsf D'=2^{-(2\alpha^2-2)}\mathsf D. \] The proof of Proposition~4.7(i) in the cited paper gives \[ \|\mathsf S'\|<\frac34,\qquad \|\mathsf J'\|<\frac78,\qquad \|\mathsf D'\|<1. \] Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$. Because $\|C\|=1$, both are contractions. The diagonal map $\mathsf D$ is invertible, and $C\mathsf T=N\mathsf D^{-1}$, so \[ (\mathsf D N^{-1}C)\mathsf T =\mathsf D N^{-1}(N\mathsf D^{-1})=I. \] Applying this left inverse to the first identity in \eqref{eq:gaussian-public-facts} gives $\mathsf D N^{-1}CP_tF_t\mathsf S=P_sF_s$. The normalizations in $\mathsf D'$, $\mathsf J'$, and $\mathsf S'$ have product $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$. Hence \[ B_0P_tF_tA =2^{-2\alpha^2}\mathsf D N^{-1}CP_tF_t\mathsf S =2^{-2\alpha^2}P_sF_s, \] which is \eqref{eq:no-sort-one-dimensional}.

**S5.1.4**: Applying the left inverse to the Gaussian identity gives $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$.
Source: "Applying this left inverse to the first identity in" (paper)
> permutation is consequently multiplication of the frequency by $-s$. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have $\alpha^2\theta>p/\alpha^2>1$. Thus $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series. Put \[ \mathsf S'=\mathsf S/2,\qquad \mathsf J'=N^{-1}/2,\qquad \mathsf D'=2^{-(2\alpha^2-2)}\mathsf D. \] The proof of Proposition~4.7(i) in the cited paper gives \[ \|\mathsf S'\|<\frac34,\qquad \|\mathsf J'\|<\frac78,\qquad \|\mathsf D'\|<1. \] Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$. Because $\|C\|=1$, both are contractions. The diagonal map $\mathsf D$ is invertible, and $C\mathsf T=N\mathsf D^{-1}$, so \[ (\mathsf D N^{-1}C)\mathsf T =\mathsf D N^{-1}(N\mathsf D^{-1})=I. \] Applying this left inverse to the first identity in \eqref{eq:gaussian-public-facts} gives $\mathsf D N^{-1}CP_tF_t\mathsf S=P_sF_s$. The normalizations in $\mathsf D'$, $\mathsf J'$, and $\mathsf S'$ have product $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$. Hence \[ B_0P_tF_tA =2^{-2\alpha^2}\mathsf D N^{-1}CP_tF_t\mathsf S =2^{-2\alpha^2}P_sF_s, \] which is \eqref{eq:no-sort-one-dimensional}.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](dft.md): The normalized transform (F_q u)_k = (1/q) Σ u_j e^{−2πijk/q}, which turns convolution into pointwise multiplication.
  Shown as: Gaussian resampling *<predicate>* Discrete Fourier transform
- [Fixed-point disk arithmetic and truncation error](fixed-point-precision.md): Storing complex numbers of modulus at most 1 as signed binary numerators over 2^p, truncating toward zero, and tracking how contractions and bilinear maps propagate the errors.
  Shown as: Gaussian resampling *<predicate>* Fixed-point disk arithmetic and truncation error
- [Established O(n log n) integer multiplier](nlogn-multiplier.md): The Harvey–van der Hoeven fixed-tape multiplier with cost O(N log N) on N-bit inputs, used only as an ordinary subroutine on short records.
  Shown as: Gaussian resampling *<predicate>* Established O(n log n) integer multiplier

## Pages that build on this one

- Source permutation cancellation: The coordinate permutation retained from resampling cancels across the two forward transforms, their pointwise product and the opposite-sign transform, leaving (u*v)/S².
- Multidimensional resampling on a padded box: Applying the one-dimensional resampling maps along each axis of the padded power-of-two box, exposing each axis by chunk interchanges, with permutations left inside the transform.
- Parameter choices: Choosing b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, power-of-two axis lengths t_i near r and distinct primes s_i just below them, so Tp = Θ(n) and all hypotheses hold.

## Other pages you may link to

- [Convolution](convolution.md)
- [Recursive power saving from a rank deficit](recursive-power-saving.md)
- [Fixed-tape Turing machine model](fixed-tape-model.md)
- [Elementary stream operations on tape arrays](elementary-stream-ops.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Subspaces, rank and orthogonal complements](linear-subspaces.md)
- [Frames on pointwise linear networks](frames-on-arrays.md)
- [Subset-intersection exchange network](exchange-network.md)
- [Subspace labels and the rank budget](subspace-labels.md)
- [Bit network shear interface](bit-network-interface.md)
- [Lower triangular (Bruhat-type) factorization](triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Power-width address interchange](power-width-interchange.md)
- [Fast chunk interchange](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](synthetic-ring.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Radix-2 butterflies and FFT](fft-butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Two-point kernel C and phase frames](phase-kernel-c.md)
- [Complex phase network](complex-phase-network.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Synthetic transform layout and cost](synthetic-transform-layout.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Source permutation cancellation](permutation-cancellation.md)
- [Multidimensional resampling on a padded box](tensor-resampling.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Exact recovery of the integer product](exact-recovery.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Parameter choices](parameter-choices.md)
- [Coefficient twist to the negacyclic ring](convolution-twist.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound](cost-accounting.md)
- [Sub-n log n integer multiplication](sub-nlogn-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "P_sF_s=2^{2\alpha^2}B_0P_tF_tA." (paper)

  > \begin{lemma}[Resampling without executing the two permutations] \label{lem:no-sort-resampling} Fix $0<\delta<1/8$. Let $p>100$, $2\leq s<t<2^p$ and $2\leq\alpha<\sqrt p$ be integers, with $\gcd(s,t)=1$ and \[ \theta:=t/s-1>p/\alpha^4. \] Define coordinate permutations by \[ (P_su)_j=u_{tj},\qquad (P_tv)_k=v_{-sk}. \] There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ satisfying \begin{equation} P_sF_s=2^{2\alpha^2}B_0P_tF_tA. \label{eq:no-sort-one-dimensional} \end{equation} There are fixed multitape algorithms for approximations $\widetilde A:\mathbb D_p^s\to\mathbb D_p^t$ and $\widetilde B_0:\mathbb D_p^t\to\mathbb D_p^s$, each with error less than $p^2$ and time \[ O(tp^{3/2+\delta}\alpha). \] The constant is uniform in $p,s,t,\alpha$. Inputs and outputs use the scalar component format above and occur in increasing coordinate order. \end{lemma}

- "Gaussian resampling
connects these two shapes." (paper)

  > The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two. Gaussian resampling connects these two shapes. Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and compute that formula directly. This section proves the resulting interface, including its tape cost when the number of coordinates grows.


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

Write the body to `exegenius/tasks/0032-write-gaussian-resampling.answer.md` and the JSON to `exegenius/tasks/0032-write-gaussian-resampling.answer.json`, then run `exegenius submit 0032-write-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0032-write-gaussian-resampling`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
