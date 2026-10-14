# exegenius task 0034-write-parameter-regime

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

Concept: Parameter regime for the multiplier
Gloss: The choice of precision p=6b, dimension d≈p^ε, record length r=2^Θ(p^(1−ε)), power-of-two axis lengths t_i and distinct prime source lengths s_i just below them, so that Tp=Θ(n) and all hypotheses hold.

## This page in the argument

The step: Parameters $p=6b$, $d\approx p^\epsilon$, $T\in[4n/b,8n/b)$, $r=2^{\Theta(p^{1-\epsilon})}$, axis lengths $t_i\in\{r/2,r\}$ and distinct odd primes $s_i$ just below $t_i$ give $Tp=\Theta(n)$, $T/2<S<T$ and all the hypotheses of the lemmas.
How: Fix rational exponents once and for all, derive the sizes from $b=\lceil\log_2n\rceil$, and choose primes in disjoint intervals $((1-2\eta)t_i,(1-\eta)t_i]$ using a prime-counting estimate.
Why: The prime lengths must be close to the powers of two: their product must fill a fixed fraction of the padded box, while each ratio $t_i/s_i$ leaves enough separation for resampling. (the sources say so: "their product must occupy a fixed fraction of the padded box," (paper))

Its sub-steps, in order:

- The fixed rational exponents include $\epsilon=2^{-75}$ and $\kappa=2^{-182}$.
- With $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$ one has $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$ and $r=2^{\Theta(p^{1-\epsilon})}$.
- There are distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$, each coprime to $t_i$.
- The product $S=\prod_is_i$ satisfies $T/2<S<T$.
- Every hypothesis of the resampling lemma holds for all sufficiently large input lengths.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Build two faster tape procedures (address chunk interchange and simultaneous butterfly layers) from rank-saving linear networks, use them in synthetic polynomial transforms and resampled source transforms for a convolution, reduce integer multiplication to that convolution, then prove exactness and add up costs. (on [Integer multiplication below n log n](main-theorem.md))
- The pieces assemble into a multiplier that is correct for every input and whose cost table fits the theorem.; how: Choose compatible parameters, set up digits, the CRT layout, the twist and the source transforms, state the algorithm, verify precision and add up the costs.

## Steps this page derives

The argument gives this page these sub-steps of its step (G.1.1, G.1.2, G.1.3, G.1.4, G.1.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**G.1.1**: The fixed rational exponents include $\epsilon=2^{-75}$ and $\kappa=2^{-182}$.
Source: "C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}." (paper)
> The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.

**G.1.2**: With $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$ one has $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$ and $r=2^{\Theta(p^{1-\epsilon})}$.
Source: "b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor," (paper)
> After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $

**G.1.3**: There are distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$, each coprime to $t_i$.
Source: "(1-2\eta)t_i<s_i\leq(1-\eta)t_i." (paper)
> east $\eta x/(2\log x)$ primes. Here $\log$ is the natural logarithm. The size bounds in \eqref{eq:sizes} give $d=\Theta(p^\epsilon)$ and $\log r=\Theta(p/d)$. For large $n$ we have $d\geq2$, so $0<\eta<1/4$, and \[ \frac{\log(r/2)}d=\Theta(p^{1-2\epsilon})\longrightarrow\infty. \] Thus both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$. For either choice, the stated lower bound for the number of primes is $x/(8d\log x)$ and exceeds $d$: indeed, $\log x=\Theta(p^{1-\epsilon})$, whereas $\log(8d^2\log x)=O(\log p)=o(\log x)$, so $x>8d^2\log x$ eventually. The two intervals are disjoint because $(1-\eta)r/2<(1-2\eta)r$ for $\eta<1/4$, and both intervals lie above $2$. We may therefore choose distinct odd primes satisfying \[ (1-2\eta)t_i<s_i\leq(1-\eta)t_i. \] Every $\gcd(s_i,t_i)$ equals one because $t_i$ is a power of two. Put $S=\prod_i s_i$. Multiplying the lower bounds on $s_i$ and applying strict Bernoulli inequality gives \[ \frac ST> \left(1-\frac1{2d}\right)^d>\frac12 \qquad(d\geq2). \] Together with $s_i<t_i$, this gives $T/2<S<T$. Writing $\theta_i=t_i/s_i-1$, the upper bound on $s_i$ gives $\theta_i\geq\eta/(1-\eta)>\eta$. Therefore \[ \alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p. \] The choice of $\alpha$ gives $\alpha=\Theta(p^{1/4+\epsilon/2})$, and \eqref{eq:gamma} already ensures $2\leq\alpha<\sqrt p$ for large $n$. We also have $t_i\leq r\leq T<8n/b<2^{6b}=2^p$. Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for all sufficiently large

**G.1.4**: The product $S=\prod_is_i$ satisfies $T/2<S<T$.
Source: "Together with $s_i<t_i$, this gives $T/2<S<T$." (paper)
> us both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$. For either choice, the stated lower bound for the number of primes is $x/(8d\log x)$ and exceeds $d$: indeed, $\log x=\Theta(p^{1-\epsilon})$, whereas $\log(8d^2\log x)=O(\log p)=o(\log x)$, so $x>8d^2\log x$ eventually. The two intervals are disjoint because $(1-\eta)r/2<(1-2\eta)r$ for $\eta<1/4$, and both intervals lie above $2$. We may therefore choose distinct odd primes satisfying \[ (1-2\eta)t_i<s_i\leq(1-\eta)t_i. \] Every $\gcd(s_i,t_i)$ equals one because $t_i$ is a power of two. Put $S=\prod_i s_i$. Multiplying the lower bounds on $s_i$ and applying strict Bernoulli inequality gives \[ \frac ST> \left(1-\frac1{2d}\right)^d>\frac12 \qquad(d\geq2). \] Together with $s_i<t_i$, this gives $T/2<S<T$. Writing $\theta_i=t_i/s_i-1$, the upper bound on $s_i$ gives $\theta_i\geq\eta/(1-\eta)>\eta$. Therefore \[ \alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p. \] The choice of $\alpha$ gives $\alpha=\Theta(p^{1/4+\epsilon/2})$, and \eqref{eq:gamma} already ensures $2\leq\alpha<\sqrt p$ for large $n$. We also have $t_i\leq r\leq T<8n/b<2^{6b}=2^p$. Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for all sufficiently large input lengths. The superpolynomial growth of $r$ established above also supplies the setup condition in Lemma~\ref{lem:tensor-resampling}.

**G.1.5**: Every hypothesis of the resampling lemma holds for all sufficiently large input lengths.
Source: "Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for" (paper)
> hoose distinct odd primes satisfying \[ (1-2\eta)t_i<s_i\leq(1-\eta)t_i. \] Every $\gcd(s_i,t_i)$ equals one because $t_i$ is a power of two. Put $S=\prod_i s_i$. Multiplying the lower bounds on $s_i$ and applying strict Bernoulli inequality gives \[ \frac ST> \left(1-\frac1{2d}\right)^d>\frac12 \qquad(d\geq2). \] Together with $s_i<t_i$, this gives $T/2<S<T$. Writing $\theta_i=t_i/s_i-1$, the upper bound on $s_i$ gives $\theta_i\geq\eta/(1-\eta)>\eta$. Therefore \[ \alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p. \] The choice of $\alpha$ gives $\alpha=\Theta(p^{1/4+\epsilon/2})$, and \eqref{eq:gamma} already ensures $2\leq\alpha<\sqrt p$ for large $n$. We also have $t_i\leq r\leq T<8n/b<2^{6b}=2^p$. Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for all sufficiently large input lengths. The superpolynomial growth of $r$ established above also supplies the setup condition in Lemma~\ref{lem:tensor-resampling}.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): Applying H₀ to the same bit position in each of D≤d address chunks at once, on polynomial records of complex fixed-point coefficients, in O(V d^{λ'}) time with one final truncation.
  Shown as: Parameter regime for the multiplier *<predicate>* Simultaneous butterfly layer
- [Gaussian resampling](gaussian-resampling.md): Harvey–van der Hoeven's way to compute a Fourier transform of prime length s from one of power-of-two length t>s using Gaussian-weighted linear maps A and B₀ that are contractions.
  Shown as: Parameter regime for the multiplier *<predicate>* Gaussian resampling
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md): Complex polynomials of degree less than r with y^r=−1, in which powers of y are roots of unity and multiplication by y^a is a signed shift of the coefficient list.
  Shown as: Parameter regime for the multiplier *<predicate>* Polynomial ring modulo y^r + 1
- [Chinese-remainder address map](crt-axis-map.md): An algebra isomorphism sending the radix-digit coefficient list onto a product of pairwise coprime cyclic axes while preserving convolution, implemented by triangular controlled shifts and axis reorderings.
  Shown as: Parameter regime for the multiplier *<predicate>* Chinese-remainder address map

## Pages that build on this one

- The multiplication algorithm: Digit conversion, the CRT map Φ, two forward source transforms, a pointwise product, one opposite transform, two scalings by S, rounding, inverse Φ and carry propagation to output the 2n-bit product.
- Cost accounting and the exponent κ: Dividing every cost by V=Tp gives normalized costs that are at most p^(1−2κ), the smallest margin 2^−181 coming from the chunk-exchange term, giving total time O(n(log n)^(1−κ)).

## Other pages you may link to

- [The n log n barrier](n-log-n-barrier.md)
- [Convolution](convolution.md)
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
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Fixed-point complex grid and truncation](fixed-point-complex-arithmetic.md)
- [Complex phase network](phase-frame-network.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Fast Fourier transform with butterflies](fft-butterflies.md)
- [Synthetic polynomial transform](synthetic-polynomial-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Retained frequency order](stored-frequency-order.md)
- [Transform layout on tape](transform-tape-layout.md)
- [Contractions and error accounting](contraction-error-propagation.md)
- [Retained permutation cancellation](permutation-cancellation.md)
- [Normalized convolution over the polynomial ring](normalized-ring-convolution.md)
- [Radix-digit convolution](radix-digit-reduction.md)
- [Source transform on the padded box](tensor-source-transform.md)
- [Precision and exact recovery](precision-exact-recovery.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "p=6b,\quad d=\lfloor b^\epsilon\rfloor" (paper)

  > After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $b$, the bounds

- "The distinct prime lengths $s_i$ must be close to the powers of two $t_i$" (paper)

  > The distinct prime lengths $s_i$ must be close to the powers of two $t_i$: their product must occupy a fixed fraction of the padded box, while each ratio $t_i/s_i$ must leave enough separation for resampling. We verify both requirements for the parameters just chosen.


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

Write the body to `exegenius/tasks/0034-write-parameter-regime.answer.md` and the JSON to `exegenius/tasks/0034-write-parameter-regime.answer.json`, then run `exegenius submit 0034-write-parameter-regime` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0034-write-parameter-regime`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
