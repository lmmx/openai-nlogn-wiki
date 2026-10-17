# exegenius task 0377-write-parameter-choice

Project directory: `/home/user/e2e-run` (paths below are relative to it)

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

For these sources: The reader is a computer science undergraduate: they have taken discrete mathematics, an algorithms course (asymptotics, divide and conquer, schoolbook and Karatsuba multiplication, sorting), a first linear algebra course (vector spaces, subspaces, dimension, rank, matrices as linear maps, inverses, triangular matrices, orthogonality, bilinear forms at a basic level), calculus, elementary number theory (primes, gcd, modular arithmetic) and basic machine-level binary representation (XOR, two's complement). They have seen Turing machines with tapes only at an introductory level. They have not been taught the discrete Fourier transform or FFT as such, abstract algebra beyond basic definitions (quotient rings, finite fields as a theory), tensor products, numerical error analysis, or the specific literature on fast integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed finite-tape machine model (also: multitape Turing machine, fixed-tape model)
- Elementary stream operations
- Controlled shifts and rational scalings
- Schönhage–Strassen optimality conjecture (also: n log n conjecture)
- Established O(n log n) multiplier
- Cyclic convolution
- Multiplication as radix-digit convolution
- Discrete Fourier transform (also: Fourier transform, DFT)
- Butterflies and the fast transform (also: transform levels)
- Multidimensional transforms
- Chinese-remainder address map (also: Agarwal–Cooley map)
- Gaussian resampling
- Bluestein chirp identity (also: chirp transform)
- Retained permutation cancellation
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Retained frequency order
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records (also: Z[i,1/2])
- Error tracking and exact recovery (also: synthetic transform error, source transform error)
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Two-point kernel C (also: phase network kernel)
- Schoolbook and Karatsuba multiplication (also: long multiplication, grade-school multiplication, Karatsuba, O(n^2) multiplication, n^{log_2 3} multiplication)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Binary and radix representation (also: base-b digits, positional notation, binary expansion, bit string, most significant bit, padding with leading zeros, carry propagation)
- Two's complement integers (also: two's-complement, signed binary integers, signed fixed-width addition)
- Bitwise XOR and arithmetic mod 2 (also: XOR, exclusive or, addition in F_2, GF(2), parity, bit flip)
- Logarithms and floors/ceilings (also: lg, log base 2, ceiling, floor, iterated logarithm, log log n)
- Modular arithmetic and primes (also: congruence, residues mod n, gcd, coprime, relatively prime, prime numbers, Z/nZ, modular inverse, units mod n)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n}, Euler's formula)
- Vector spaces, subspaces, dimension and rank (also: linear subspace, basis, span, linear independence, dimension, matrix rank, kernel, linear map, linear operator, direct sum)
- Matrices and linear operators (also: matrix multiplication, invertible matrix, matrix inverse, identity matrix, commuting operators, diagonal matrix, triangular matrix, lower triangular, permutation matrix)
- Gaussian elimination and triangular factorization (also: row reduction, LU decomposition, back substitution)
- Orthogonality and inner products (also: orthonormal basis, dot product, orthogonal complement, bilinear form, nondegenerate form, Euclidean norm)
- Norms and the triangle inequality (also: sup norm, max norm, infinity norm, modulus bounds, absolute value bounds)
- Permutations and bijections (also: permutation of indices, sorting a permutation, bit-reversal permutation, bijective map, inverse permutation)
- Cartesian products and multi-index arrays (also: multidimensional arrays, row-major order, lexicographic order, mixed-radix index, index tuples, array stored on a tape, rectangle, columns)
- Directed acyclic graphs and networks of gates (also: circuit, DAG, wire, gate, edges and vertices, fan-in)
- Summation, geometric series and induction (also: geometric sum, proof by induction, summation notation, telescoping sum)
- Rounding to the nearest integer and exactness (also: rounding, truncation, round to nearest, rational numbers, dyadic rational)
- Multitape Turing machine running time (also: tape head movement, scanning a tape, linear-time pass over a tape, time complexity of a Turing machine, worst-case running time)
- Integer exponentials and tuple notation (also: powers of two, tensor power notation, exponent of a constant, fixed rational exponents)
- Contractions and bilinear contractions (also: contraction, bilinear contraction)

## This page

Concept: Parameter and prime-length choice
Gloss: Fixed rational exponents and sizes (precision p = 6b, d axes, K = d^c, T and r powers of two, prime lengths s_i just below t_i) making every hypothesis of the lemmas hold.

## This page in the argument

The step: Fixed rational exponents and sizes make every hypothesis of the lemmas hold: $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$, axis lengths $t_i\in\{r/2,r\}$ with $\prod t_i=T$, $t_d=r$, and distinct odd primes $s_i\in((1-2\eta)t_i,(1-\eta)t_i]$.
How: Fix concrete rational exponents with explicit slack and verify the inequalities among them by integer comparisons; choose the sizes so that $Tp=\Theta(n)$ and every needed asymptotic comparison holds with fixed constants; find the primes by the prime-interval lemma and a deterministic search of cost $n^{o(1)}$.
Why: The layer, transform, chirp and resampling lemmas each impose inequalities among the exponents ($\tau,\sigma,\lambda,\lambda',c,\epsilon,\delta$) and the sizes; these are constants deliberately conservative so that all can be checked by exact comparisons, and the primes must lie close below the powers of two so that $S$ fills a fixed fraction of the padded box while $t_i/s_i$ leaves enough separation. (the sources say so: "These constants are deliberately conservative; no optimization is claimed." (paper))

Its sub-steps, in order:

- Take $\tau=\sigma=1-2^{-50}$, $\beta=1/2$ and $\delta=1/16$.
- Take $\lambda=1-2^{-52}$ and $c=2^{-56}$.
- Take $\lambda'=1-2^{-54}$.
- Take $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$.
- The layer conditions hold with room to spare: $\tau(1+c/\beta)<1-31\cdot2^{-55}<\lambda$.
- Also $\sigma+\beta(1-\sigma)=1-2^{-51}<\lambda<\lambda'<1$.
- For large $n$ put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$.
- Put $K=\lfloor d^c\rfloor$.
- Take the power of two $T$ in $[4n/b,8n/b)$.
- Let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$; choose $d\ell-\log_2T\in[0,d)$ of the axis lengths to be $r/2$ and the others $r$, with the last axis of length $r$.
- Thus $t_i\in\{r/2,r\}$, $\prod_it_i=T$ and $t_d=r$.
- These choices give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$, $r=2^{\Theta(p^{1-\epsilon})}$, so the comparison constants $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, $C_\ell=1$ can be fixed for all lengths at once.
- Put $\alpha=\lceil(12d^2b)^{1/4}\rceil$.
- Put $\gamma=2d\alpha^2$ and $\eta=1/(4d)$.
- Then $\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}$, so $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$.
- By the prime-interval lemma, for $0<\eta<1/4$ and $x>e^{2/\eta}$ the interval $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes; both $x=r/2$ and $x=r$ qualify since $\log x>8d=2/\eta$, and the count $x/(8d\log x)$ exceeds $d$.
- Choose distinct odd primes with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$; $\gcd(s_i,t_i)=1$ as $t_i$ is a power of two.
- Multiplying the lower bounds and applying strict Bernoulli gives $S/T>(1-1/(2d))^d>1/2$ for $d\ge2$.
- With $s_i<t_i$ this gives $T/2<S<T$.
- With $\theta_i=t_i/s_i-1\ge\eta/(1-\eta)>\eta$ we get $\alpha^4\theta_i>12d^2b/(4d)=3db\ge6b=p$, the separation hypothesis of the resampling lemma; also $t_i\le r\le T<2^p$.
- The deterministic search for the primes takes $n^{o(1)}=o(n)$ time, since its logarithm is $o(p)$ and $p=\Theta(\log n)$; all primes and length parameters are generated by the machine, not given as advice.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- The exact $2n$-bit product of the two inputs is obtained from the radix-digit convolution by the chain: radix digits, Chinese-remainder address map to a product of prime cyclic axes, two forward source transforms (resampling and chirps), pointwise product, opposite transform, rescaling, rounding, and carry propagation, with total error below $1/2$.; how: Reduce the integer product to a cyclic convolution of $S$ short coefficients and compute it through the chain of reductions (digits, CRT address map, Gaussian resampling with chirps, twist to the polynomial ring, synthetic-transform convolution); recover exact integers because the accumulated error is below $1/2$. (on [The multiplication algorithm](multiplication-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S5.1.1, S5.1.2, S5.1.3, S5.1.4, S5.1.5, S5.1.6, S5.1.7, S5.1.8, S5.1.9, S5.1.10, S5.1.11, S5.1.12, S5.1.13, S5.1.14, S5.1.15, S5.1.16, S5.1.17, S5.1.18, S5.1.19, S5.1.20, S5.1.21). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S5.1.1**: Take $\tau=\sigma=1-2^{-50}$, $\beta=1/2$ and $\delta=1/16$.
Source: "\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16}," (paper)
> The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.

**S5.1.2**: Take $\lambda=1-2^{-52}$ and $c=2^{-56}$.
Source: "\lambda=1-2^{-52},\qquad c=2^{-56},\qquad" (paper)
> The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.

**S5.1.3**: Take $\lambda'=1-2^{-54}$.
Source: "\lambda'=1-2^{-54}," (paper)
> The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.

**S5.1.4**: Take $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$.
Source: "C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}." (paper)
> The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.

**S5.1.5**: The layer conditions hold with room to spare: $\tau(1+c/\beta)<1-31\cdot2^{-55}<\lambda$.
Source: "\tau(1+c/\beta)<1-31\cdot2^{-55}<\lambda," (paper)
> The layer conditions hold with room to spare: \[ \max\{\tau,\sigma\}<\lambda<1,\qquad \tau(1+c/\beta)<1-31\cdot2^{-55}<\lambda, \] and \[ \sigma+\beta(1-\sigma)=1-2^{-51}<\lambda<\lambda'<1. \] The strict final inequality absorbs the logarithmic number of groups in a base-$m$ partition. The dimension exponent also satisfies \[ \begin{gathered} \epsilon<\frac1{12},\quad \epsilon C_1<1,\quad \epsilon(2-\tau)<1-\tau,\quad \frac34+\delta+\frac32\epsilon<1,\\ \epsilon(1+c)<1,\qquad \epsilon+\delta<1. \end{gathered} \]

**S5.1.6**: Also $\sigma+\beta(1-\sigma)=1-2^{-51}<\lambda<\lambda'<1$.
Source: "\sigma+\beta(1-\sigma)=1-2^{-51}<\lambda<\lambda'<1." (paper)
> The layer conditions hold with room to spare: \[ \max\{\tau,\sigma\}<\lambda<1,\qquad \tau(1+c/\beta)<1-31\cdot2^{-55}<\lambda, \] and \[ \sigma+\beta(1-\sigma)=1-2^{-51}<\lambda<\lambda'<1. \] The strict final inequality absorbs the logarithmic number of groups in a base-$m$ partition. The dimension exponent also satisfies \[ \begin{gathered} \epsilon<\frac1{12},\quad \epsilon C_1<1,\quad \epsilon(2-\tau)<1-\tau,\quad \frac34+\delta+\frac32\epsilon<1,\\ \epsilon(1+c)<1,\qquad \epsilon+\delta<1. \end{gathered} \]

**S5.1.7**: For large $n$ put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$.
Source: "b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor," (paper)
> After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $

**S5.1.8**: Put $K=\lfloor d^c\rfloor$.
Source: "\quad K=\lfloor d^c\rfloor." (paper)
> After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $b$, the bounds on $n,T$ give $b/2\leq\log_2T\leq

**S5.1.9**: Take the power of two $T$ in $[4n/b,8n/b)$.
Source: "Take the power of two $T$ in $[4n/b,8n/b)$, and let" (paper)
> After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $b$, the bounds on $n,T$ give $b/2\leq\log_2T\leq b$. Since $p=6b$, $d=\lfloor b^\epsilon\rfl

**S5.1.10**: Let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$; choose $d\ell-\log_2T\in[0,d)$ of the axis lengths to be $r/2$ and the others $r$, with the last axis of length $r$.
Source: "$r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$.  Choose" (paper)
> After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $b$, the bounds on $n,T$ give $b/2\leq\log_2T\leq b$. Since $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $d\leq b$, they imply \[ \frac1{12}p^\epsilon\

**S5.1.11**: Thus $t_i\in\{r/2,r\}$, $\prod_it_i=T$ and $t_d=r$.
Source: "t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r." (paper)
> After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $b$, the bounds on $n,T$ give $b/2\leq\log_2T\leq b$. Since $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $d\leq b$, they imply \[ \frac1{12}p^\epsilon\leq d\leq p^\epsilon, \qquad \frac{p}{12d}\leq\ell\leq\frac{p}{3d}. \] Thus we fix $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, and $C_\ell=1$ in the layer an

**S5.1.12**: These choices give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$, $r=2^{\Theta(p^{1-\epsilon})}$, so the comparison constants $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, $C_\ell=1$ can be fixed for all lengths at once.
Source: "Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad" (paper)
> After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $b$, the bounds on $n,T$ give $b/2\leq\log_2T\leq b$. Since $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $d\leq b$, they imply \[ \frac1{12}p^\epsilon\leq d\leq p^\epsilon, \qquad \frac{p}{12d}\leq\ell\leq\frac{p}{3d}. \] Thus we fix $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, and $C_\ell=1$ in the layer and transform interfaces. Their pointwise bounds cover every computed pair $(d,r)$, including all choices arising at the same $p$. These bounds also give that $r$ exceeds every fixed power of $p$, $K/\log p\to\infty$, and $\

**S5.1.13**: Put $\alpha=\lceil(12d^2b)^{1/4}\rceil$.
Source: "\alpha=\left\lceil(12d^2b)^{1/4}\right\rceil," (paper)
> Set \[ \alpha=\left\lceil(12d^2b)^{1/4}\right\rceil, \qquad \gamma=2d\alpha^2,\qquad \eta=\frac1{4d}. \] The ceiling does not affect the needed bounds: for $A\ge1$, $\lceil A\rceil\le2A$, and hence \begin{equation}\label{eq:gamma} \alpha\le2(12d^2b)^{1/4},\qquad \gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}. \end{equation} It follows that $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$. For example $b\ge2^{24}$ implies $\gamma\le b/4$.

**S5.1.14**: Put $\gamma=2d\alpha^2$ and $\eta=1/(4d)$.
Source: "\qquad \gamma=2d\alpha^2,\qquad \eta=\frac1{4d}." (paper)
> Set \[ \alpha=\left\lceil(12d^2b)^{1/4}\right\rceil, \qquad \gamma=2d\alpha^2,\qquad \eta=\frac1{4d}. \] The ceiling does not affect the needed bounds: for $A\ge1$, $\lceil A\rceil\le2A$, and hence \begin{equation}\label{eq:gamma} \alpha\le2(12d^2b)^{1/4},\qquad \gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}. \end{equation} It follows that $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$. For example $b\ge2^{24}$ implies $\gamma\le b/4$.

**S5.1.15**: Then $\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}$, so $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$.
Source: "\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}." (paper)
> Set \[ \alpha=\left\lceil(12d^2b)^{1/4}\right\rceil, \qquad \gamma=2d\alpha^2,\qquad \eta=\frac1{4d}. \] The ceiling does not affect the needed bounds: for $A\ge1$, $\lceil A\rceil\le2A$, and hence \begin{equation}\label{eq:gamma} \alpha\le2(12d^2b)^{1/4},\qquad \gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}. \end{equation} It follows that $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$. For example $b\ge2^{24}$ implies $\gamma\le b/4$.

**S5.1.16**: By the prime-interval lemma, for $0<\eta<1/4$ and $x>e^{2/\eta}$ the interval $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes; both $x=r/2$ and $x=r$ qualify since $\log x>8d=2/\eta$, and the count $x/(8d\log x)$ exceeds $d$.
Source: "(1-2\eta)x<q\leq(1-\eta)x" (paper)
> The prime-interval result \cite[Lemma~5.1]{HarveyHoeven2021}, based on explicit estimates of Rosser and Schoenfeld~\cite{RosserSchoenfeld1962}, gives the following bound: for $0<\eta<1/4$ and $x>e^{2/\eta}$, the interval \[ (1-2\eta)x<q\leq(1-\eta)x \] contains at least $\eta x/(2\log x)$ primes. Here $\log$ is the natural logarithm. The size bounds in \eqref{eq:sizes} give $d=\Theta(p^\epsilon)$ and $\log r=\Theta(p/d)$. For large $n$ we have $d\geq2$, so $0<\eta<1/4$, and \[ \frac{\log(r/2)}d=\Theta(p^{1-2\epsilon})\longrightarrow\infty. \] Thus both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$. For either choice, the stated lower bound for the number of primes is $x/(8d\log x)$ and exceeds $d$: indeed, $\log x=\Theta(p^{1-\epsilon})$, whereas $\log(8d^2\log x)=O(\log p)=o(\log x)$, so $x>8d^2\log x$ eventually. The two intervals are disjoint because $(1-\eta)r/2<(1-2\eta)r$ for $\eta<1/4$, and both intervals lie above $2$. We may therefore choose distinct odd primes s

**S5.1.17**: Choose distinct odd primes with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$; $\gcd(s_i,t_i)=1$ as $t_i$ is a power of two.
Source: "(1-2\eta)t_i<s_i\leq(1-\eta)t_i." (paper)
> east $\eta x/(2\log x)$ primes. Here $\log$ is the natural logarithm. The size bounds in \eqref{eq:sizes} give $d=\Theta(p^\epsilon)$ and $\log r=\Theta(p/d)$. For large $n$ we have $d\geq2$, so $0<\eta<1/4$, and \[ \frac{\log(r/2)}d=\Theta(p^{1-2\epsilon})\longrightarrow\infty. \] Thus both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$. For either choice, the stated lower bound for the number of primes is $x/(8d\log x)$ and exceeds $d$: indeed, $\log x=\Theta(p^{1-\epsilon})$, whereas $\log(8d^2\log x)=O(\log p)=o(\log x)$, so $x>8d^2\log x$ eventually. The two intervals are disjoint because $(1-\eta)r/2<(1-2\eta)r$ for $\eta<1/4$, and both intervals lie above $2$. We may therefore choose distinct odd primes satisfying \[ (1-2\eta)t_i<s_i\leq(1-\eta)t_i. \] Every $\gcd(s_i,t_i)$ equals one because $t_i$ is a power of two. Put $S=\prod_i s_i$. Multiplying the lower bounds on $s_i$ and applying strict Bernoulli inequality gives \[ \frac ST> \left(1-\frac1{2d}\right)^d>\frac12 \qquad(d\geq2). \] Together with $s_i<t_i$, this gives $T/2<S<T$. Writing $\theta_i=t_i/s_i-1$, the upper bound on $s_i$ gives $\theta_i\geq\eta/(1-\eta)>\eta$. Therefore \[ \alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p. \] The choice of $\alpha$ gives $\alpha=\Theta(p^{1/4+\epsilon/2})$, and \eqref{eq:gamma} already ensures $2\leq\alpha<\sqrt p$ for large $n$. We also have $t_i\leq r\leq T<8n/b<2^{6b}=2^p$. Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for all sufficiently large

**S5.1.18**: Multiplying the lower bounds and applying strict Bernoulli gives $S/T>(1-1/(2d))^d>1/2$ for $d\ge2$.
Source: "\left(1-\frac1{2d}\right)^d>\frac12" (paper)
> og(r/2)}d=\Theta(p^{1-2\epsilon})\longrightarrow\infty. \] Thus both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$. For either choice, the stated lower bound for the number of primes is $x/(8d\log x)$ and exceeds $d$: indeed, $\log x=\Theta(p^{1-\epsilon})$, whereas $\log(8d^2\log x)=O(\log p)=o(\log x)$, so $x>8d^2\log x$ eventually. The two intervals are disjoint because $(1-\eta)r/2<(1-2\eta)r$ for $\eta<1/4$, and both intervals lie above $2$. We may therefore choose distinct odd primes satisfying \[ (1-2\eta)t_i<s_i\leq(1-\eta)t_i. \] Every $\gcd(s_i,t_i)$ equals one because $t_i$ is a power of two. Put $S=\prod_i s_i$. Multiplying the lower bounds on $s_i$ and applying strict Bernoulli inequality gives \[ \frac ST> \left(1-\frac1{2d}\right)^d>\frac12 \qquad(d\geq2). \] Together with $s_i<t_i$, this gives $T/2<S<T$. Writing $\theta_i=t_i/s_i-1$, the upper bound on $s_i$ gives $\theta_i\geq\eta/(1-\eta)>\eta$. Therefore \[ \alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p. \] The choice of $\alpha$ gives $\alpha=\Theta(p^{1/4+\epsilon/2})$, and \eqref{eq:gamma} already ensures $2\leq\alpha<\sqrt p$ for large $n$. We also have $t_i\leq r\leq T<8n/b<2^{6b}=2^p$. Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for all sufficiently large input lengths. The superpolynomial growth of $r$ established above also supplies the setup condition in Lemma~\ref{lem:tensor-resampling}.

**S5.1.19**: With $s_i<t_i$ this gives $T/2<S<T$.
Source: "Together with $s_i<t_i$, this gives $T/2<S<T$." (paper)
> us both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$. For either choice, the stated lower bound for the number of primes is $x/(8d\log x)$ and exceeds $d$: indeed, $\log x=\Theta(p^{1-\epsilon})$, whereas $\log(8d^2\log x)=O(\log p)=o(\log x)$, so $x>8d^2\log x$ eventually. The two intervals are disjoint because $(1-\eta)r/2<(1-2\eta)r$ for $\eta<1/4$, and both intervals lie above $2$. We may therefore choose distinct odd primes satisfying \[ (1-2\eta)t_i<s_i\leq(1-\eta)t_i. \] Every $\gcd(s_i,t_i)$ equals one because $t_i$ is a power of two. Put $S=\prod_i s_i$. Multiplying the lower bounds on $s_i$ and applying strict Bernoulli inequality gives \[ \frac ST> \left(1-\frac1{2d}\right)^d>\frac12 \qquad(d\geq2). \] Together with $s_i<t_i$, this gives $T/2<S<T$. Writing $\theta_i=t_i/s_i-1$, the upper bound on $s_i$ gives $\theta_i\geq\eta/(1-\eta)>\eta$. Therefore \[ \alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p. \] The choice of $\alpha$ gives $\alpha=\Theta(p^{1/4+\epsilon/2})$, and \eqref{eq:gamma} already ensures $2\leq\alpha<\sqrt p$ for large $n$. We also have $t_i\leq r\leq T<8n/b<2^{6b}=2^p$. Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for all sufficiently large input lengths. The superpolynomial growth of $r$ established above also supplies the setup condition in Lemma~\ref{lem:tensor-resampling}.

**S5.1.20**: With $\theta_i=t_i/s_i-1\ge\eta/(1-\eta)>\eta$ we get $\alpha^4\theta_i>12d^2b/(4d)=3db\ge6b=p$, the separation hypothesis of the resampling lemma; also $t_i\le r\le T<2^p$.
Source: "\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p." (paper)
> ndeed, $\log x=\Theta(p^{1-\epsilon})$, whereas $\log(8d^2\log x)=O(\log p)=o(\log x)$, so $x>8d^2\log x$ eventually. The two intervals are disjoint because $(1-\eta)r/2<(1-2\eta)r$ for $\eta<1/4$, and both intervals lie above $2$. We may therefore choose distinct odd primes satisfying \[ (1-2\eta)t_i<s_i\leq(1-\eta)t_i. \] Every $\gcd(s_i,t_i)$ equals one because $t_i$ is a power of two. Put $S=\prod_i s_i$. Multiplying the lower bounds on $s_i$ and applying strict Bernoulli inequality gives \[ \frac ST> \left(1-\frac1{2d}\right)^d>\frac12 \qquad(d\geq2). \] Together with $s_i<t_i$, this gives $T/2<S<T$. Writing $\theta_i=t_i/s_i-1$, the upper bound on $s_i$ gives $\theta_i\geq\eta/(1-\eta)>\eta$. Therefore \[ \alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p. \] The choice of $\alpha$ gives $\alpha=\Theta(p^{1/4+\epsilon/2})$, and \eqref{eq:gamma} already ensures $2\leq\alpha<\sqrt p$ for large $n$. We also have $t_i\leq r\leq T<8n/b<2^{6b}=2^p$. Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for all sufficiently large input lengths. The superpolynomial growth of $r$ established above also supplies the setup condition in Lemma~\ref{lem:tensor-resampling}.

**S5.1.21**: The deterministic search for the primes takes $n^{o(1)}=o(n)$ time, since its logarithm is $o(p)$ and $p=\Theta(\log n)$; all primes and length parameters are generated by the machine, not given as advice.
Source: "Since $p=6\lceil\log_2 n\rceil=\Theta(\log n)$, the search takes" (paper)
> The machine finds these primes by scanning the two intervals deterministically and testing each candidate by trial division through its square root. Testing every candidate would visit $O(r)$ candidates and at most $O(\sqrt r)$ trial divisors per candidate. Elementary division on $O(\log r)$-bit integers and management of a list of at most $d$ selected primes give the conservative bound $O(dr^{3/2}\operatorname{poly}(p))$. Its logarithm is \[ O(\log p+\log r)=O(\log p+p/d)=o(p). \] Since $p=6\lceil\log_2 n\rceil=\Theta(\log n)$, the search takes $n^{o(1)}=o(n)$ time. All remaining scalar setup, including comparisons for fixed rational powers, modular inverses, prime products and shape descriptors, has cost polynomial in $p$. For example, $d=\lfloor b^{2^{-75}}\rfloor$ is found by binary search using exact comparisons $d^{2^{75}}\le b$; the exponent is fixed. The same procedure computes $K$ and all other fixed rational powers. All primes and length parameters are therefore generated by the machine; they are not advice.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $y$ (ring variable), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The indeterminate of the polynomials; it satisfies y^r = -1 in the ring.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The number of complex coefficients in a polynomial of the ring, always a power of two.
- $n$ (bit length), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): The number of bits in each of the two integers being multiplied.
- $\kappa$ (power saving), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant, the amount by which the exponent of the logarithm is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the grid on which stored values lie.
- $k$ (depth), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations in sequence since the layer began that produced a value.
- $\Delta$ (reserved extra bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the maximal depth reached in the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.
- $X$ (first data bank), bound on [Linear exchange network with restored scratch wires](exchange-network.md): One of the two data banks, with entries X_a.
- $Y$ (second data bank), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The other data bank, with entries Y_a.
- $a$ (bank index), bound on [Linear exchange network with restored scratch wires](exchange-network.md): A triple of three-element subsets of [h] indexing the entries of the banks.
- $h$ (ground-set size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of the ground set [h] whose three-element subsets index the banks.
- $\mathcal T$ (triple set), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The set of three-element subsets of [h].
- $v$ (number of triples), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of three-element subsets of [h].
- $N$ (bank size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of values in each data bank.
- $m$ (label-space dimension), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The dimension of the label space used on later pages.
- $I$ (invocation count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of invocations over all three stages.
- $z_{\rm b}$ (bit neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the bit construction.
- $z_{\rm c}$ (complex neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the complex construction.
- $c_{\rm b}$ (bit central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the bit network.
- $W_{\rm c}$ (complex wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the complex network.
- $R$ (scalar ring), bound on [Frames on wire arrays](array-frames.md): The ring of scalars carried by the wires.
- $\Omega$ (address set), bound on [Frames on wire arrays](array-frames.md): A finite set of addresses indexing every array.
- $\mathsf S_\Omega$ (pointwise network), bound on [Frames on wire arrays](array-frames.md): The network acting on all the wire arrays together, each gate applied at every address separately.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): The invertible R-linear operator on R^Omega assigned to the source, gate or sink v.
- $t$ (gate input count), bound on [Frames on wire arrays](array-frames.md): The number of input arrays of the gate G.
- $\rho$ (role permutation), bound on [Frames on wire arrays](array-frames.md): The map sending each input role w to its output role rho(w) in a signed role permutation.
- $\varepsilon_w$ (role sign), bound on [Frames on wire arrays](array-frames.md): The scalar sign carried by the route from input role w.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each of the two sequences being convolved.
- $d$ (axis count), bound on [Cyclic convolution](convolution.md): The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of cyclic axis i.
- $M$ (address count), bound on [Cyclic convolution](convolution.md): The number of cyclic addresses of an array, the product of the axis lengths.
- $T$ (coefficient count), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array.
- $u$ (first input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The first of the two n-bit integers being multiplied.
- $v$ (second input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The second of the two n-bit integers being multiplied (not the number of triples).
- $b$ (digit bits), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in one radix-2^b digit.
- $T$ (padded length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The padded length, a power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The length of the cyclic convolution, with T/2<S<T.
- $q$ (digit count), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of digits in each input, not the sequence length of the convolution page.
- $x$ (polynomial variable), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The indeterminate of the digit polynomials, evaluated at 2^b to recover the integers.
- $c_j$ (product coefficient), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The coefficient of x^j in the product of the two digit polynomials.
- $f$ (first array), bound on [Phase twist](phase-twist.md): The first complex array being convolved.
- $g$ (second array), bound on [Phase twist](phase-twist.md): The second complex array being convolved with f.
- $d$ (axis count), bound on [Phase twist](phase-twist.md): The number of axes of the arrays.
- $x_d$ (last-axis variable), bound on [Phase twist](phase-twist.md): The variable of the last cyclic axis.
- $\mathcal R_r$ (negacyclic ring), bound on [Phase twist](phase-twist.md): The ring of polynomials modulo y^r+1.
- $\zeta$ (twist root), bound on [Phase twist](phase-twist.md): The primitive 2r-th root of unity e^{\pi i/r}, with zeta^r=-1.
- $\Theta$ (twist map), bound on [Phase twist](phase-twist.md): The ring isomorphism from the cyclic ring to the negacyclic ring sending x_d to zeta y.
- $k$ (coefficient index), bound on [Phase twist](phase-twist.md): An index of a coefficient (not an operation count).
- $l$ (second coefficient index), bound on [Phase twist](phase-twist.md): An index of a coefficient of the second factor.
- $j$ (wrapped position), bound on [Phase twist](phase-twist.md): The position k+l reduced modulo r.
- $h$ (wrap indicator), bound on [Phase twist](phase-twist.md): Zero or one according to whether k+l wrapped past r.
- $\iota$ (record reading), bound on [Phase twist](phase-twist.md): The map reading each line along the last axis as a polynomial in R_r.
- $D_\pm$ (diagonal twist), bound on [Phase twist](phase-twist.md): The maps multiplying entry k of each line by zeta^{+-k}.
- $\mathcal M_r$ (ring convolution), bound on [Phase twist](phase-twist.md): Normalized convolution of the first d-1 axes over R_r, including division by T.
- $\mathcal M_{\mathbb C}$ (complex convolution), bound on [Phase twist](phase-twist.md): The normalized complex cyclic convolution of two arrays.
- $\|f\|$ (sup norm), bound on [Phase twist](phase-twist.md): The largest modulus of a scalar coefficient of f.
- $q$ (sequence length), bound on [Discrete Fourier transform](dft.md): The number of entries of a sequence.
- $u$ (input sequence), bound on [Discrete Fourier transform](dft.md): A sequence of q complex numbers to be transformed.
- $\omega$ (primitive root), bound on [Discrete Fourier transform](dft.md): The primitive q-th root of unity e^{2\pi i/q}.
- $t$ (transform length), bound on [Butterflies and the fast transform](butterfly.md): The number of positions in the sequence being transformed, a power of two.
- $z_k$ (input value), bound on [Butterflies and the fast transform](butterfly.md): The input value at position k of the sequence being transformed.
- $m$ (output index), bound on [Butterflies and the fast transform](butterfly.md): The index of an output of the transform.
- $b$ (lowest bit), bound on [Butterflies and the fast transform](butterfly.md): The lowest bit of the output index m.
- $h$ (remaining index), bound on [Butterflies and the fast transform](butterfly.md): The output index m with its lowest bit removed.
- $t$ (transform length), bound on [Synthetic polynomial transform](synthetic-transform.md): The number of ring elements along one axis, a power of two dividing 2r.
- $e$ (two-adic exponent), bound on [Synthetic polynomial transform](synthetic-transform.md): The exponent of 2 in j when j is written as 2^e times an odd number.
- $V$ (array volume), bound on [Elementary stream operations](stream-ops.md): The number of digits stored in the array.
- $\beta$ (radix), bound on [Elementary stream operations](stream-ops.md): The number of values one digit can take.
- $W$ (stream count), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams into which rows are dealt.
- $P$ (prefix count), bound on [Elementary stream operations](stream-ops.md): The number of prefix values of the array in item 4.
- $R$ (row count), bound on [Elementary stream operations](stream-ops.md): The number of rows in item 4; here R is not the scalar ring.
- $B$ (row length), bound on [Elementary stream operations](stream-ops.md): The number of entries per row in item 4.
- $\boldsymbol j$ (index tuple), bound on [Bluestein chirp identity](chirp.md): The tuple of indices (j_1,...,j_d), one per axis, locating an entry of an array.
- $\boldsymbol t$ (axis lengths), bound on [Bluestein chirp identity](chirp.md): The tuple (t_1,...,t_d) of axis lengths, where t_i is the even number of entries along axis i.
- $s_i$ (coprime multiplier), bound on [Bluestein chirp identity](chirp.md): An integer coprime to the axis length t_i.
- $F_{\boldsymbol t}$ (normalized transform), bound on [Bluestein chirp identity](chirp.md): The normalized multidimensional discrete Fourier transform with axis lengths t.
- $\boldsymbol k$ (input position), bound on [Bluestein chirp identity](chirp.md): The index tuple of an input entry.
- $\boldsymbol f$ (frequency), bound on [Bluestein chirp identity](chirp.md): The tuple of frequencies labelling an output entry of the transform.
- $Q$ (target permutation), bound on [Bluestein chirp identity](chirp.md): The permutation reordering the output so that position j holds the entry of frequency (-s_i j_i)_i.
- $a$ (chirp), bound on [Bluestein chirp identity](chirp.md): The chirp, a phase quadratic in the index.
- $N$ (factor bit length), bound on [Established O(n log n) multiplier](hvdh-multiplier.md): The number of bits in each of the two integers given to the established multiplier.
- $B_0$ (packing base), bound on [Signed packing](signed-packing.md): The base 2^{4p} at which the polynomials are evaluated.
- $A_u$ (signed evaluation integer), bound on [Signed packing](signed-packing.md): The integer obtained by evaluating the integer-coefficient polynomial u at B_0.
- $\gamma_j$ (carry), bound on [Signed packing](signed-packing.md): The carry, in {-1,0}, into block j when forming A_u.
- $d_j$ (block), bound on [Signed packing](signed-packing.md): The residue of u_j plus the carry modulo B_0, the j-th block of 4p bits of A_u.
- $h_j$ (product coefficient), bound on [Signed packing](signed-packing.md): The coefficient of y^j in the ordinary product h=ac of integer polynomials.
- $\rho_j$ (extraction carry), bound on [Signed packing](signed-packing.md): The carry into block j during extraction, in {0,1}.
- $H_j$ (reduced coefficient), bound on [Signed packing](signed-packing.md): The Gaussian integer coefficient of y^j after reduction modulo y^r+1.
- $q$ (prime radix), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The radix of the stored digits, a prime (not a sequence length).
- $b$ (field digit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of base-q digits of a field.
- $Q$ (field value count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of values a field can take.
- $y$ (field value), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The value of the target field, an integer from 0 to Q-1 (not the ring variable).
- $a$ (offset), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The offset added to the target field, prepared from the control values.
- $B$ (suffix digit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of digits following the target field.
- $c$ (scaling multiplier), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed positive integer prime to q by which the field is multiplied.
- $j$ (wrap count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of times cy wraps past Q.
- $y'$ (scaled position), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The position cy - jQ to which the block at position y is sent.
- $c'$ (unit denominator), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The positive integer denominator of a rational unit, prime to q.
- $q$ (field base), bound on [Matrix shear by triangular factorization](matrix-shear.md): A fixed odd prime, the base of the digits.
- $b$ (digits per field), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of base-q digits in one field.
- $a$ (rank), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rank of the matrix A.
- $m$ (fields per group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of fields in each of the groups H and D.
- $I$ (identity matrix), bound on [Two-point kernel C](phase-kernel.md): The 2x2 identity matrix.
- $X$ (bit flip), bound on [Two-point kernel C](phase-kernel.md): The 2x2 matrix swapping the two entries of a pair.
- $a$ (kernel constant), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1+i)/2.
- $b$ (kernel coefficient), bound on [Two-point kernel C](phase-kernel.md): The complex coefficient (1-i)/2 of the bit flip in the kernel.
- $C$ (two-point kernel), bound on [Two-point kernel C](phase-kernel.md): The matrix aI + bX.
- $\mathsf S$ (phase matrix), bound on [Two-point kernel C](phase-kernel.md): The diagonal matrix diag(1, i) multiplying the second entry of a pair by i.
- $H_0$ (averaging step), bound on [Two-point kernel C](phase-kernel.md): The matrix of the two-point averaging and differencing step.
- $H$ (Hadamard matrix), bound on [Two-point kernel C](phase-kernel.md): The normalized Hadamard matrix sqrt(2) H_0.
- $L$ (linear map), bound on [Contractions and bilinear contractions](contraction-maps.md): A linear map whose norm bound is being defined.
- $\mathcal M$ (bilinear map), bound on [Contractions and bilinear contractions](contraction-maps.md): A map linear in each of its two operands.
- $u'$ (computed input), bound on [Contractions and bilinear contractions](contraction-maps.md): The computed input that replaces the exact input u.
- $f'$ (computed first operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The computed operand replacing f.
- $g'$ (computed second operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The computed operand replacing g.
- $F_q$ (normalized transform), bound on [Contractions and bilinear contractions](contraction-maps.md): The normalized discrete Fourier transform on sequences of q entries.
- $f$ (first operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The first operand of the bilinear map.
- $g$ (second operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The second operand of the bilinear map.
- $i$ (axis index), bound on [Multidimensional transforms](multidim-transform.md): The index of an axis of the array, from 1 to d.
- $q_i$ (axis position count), bound on [Multidimensional transforms](multidim-transform.md): The number of positions along axis i.
- $j$ (index tuple), bound on [Multidimensional transforms](multidim-transform.md): The tuple of coordinates (j_1,...,j_d) of an entry of the array.
- $k$ (output index tuple), bound on [Multidimensional transforms](multidim-transform.md): An output index tuple shaped like j.
- $G_i$ (axis operator), bound on [Multidimensional transforms](multidim-transform.md): An operator on sequences of length q_i, applied to every line along axis i.
- $\delta$ (time-bound slack), bound on [Multidimensional transforms](multidim-transform.md): A fixed constant with 0<delta<1/8 that sets the slack in the exponent 3/2+delta of p in the time bound.
- $\alpha$ (resampling parameter), bound on [Multidimensional transforms](multidim-transform.md): An integer resampling parameter with 2<=alpha<sqrt p.
- $\boldsymbol s$ (source lengths), bound on [Multidimensional transforms](multidim-transform.md): The tuple of source axis lengths (s_1,...,s_d).
- $\boldsymbol t$ (padded lengths), bound on [Multidimensional transforms](multidim-transform.md): The tuple of padded power-of-two axis lengths (t_1,...,t_d).
- $\gamma$ (scalar exponent), bound on [Multidimensional transforms](multidim-transform.md): The total exponent 2d alpha^2 of the power of two multiplying the tensored identity.
- $R$ (source permutation), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the source index permutations P_{s_i}; here not the scalar ring.
- $Q$ (padded permutation), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the index permutations P_{t_i}.
- $\mathcal A$ (input map), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the one-dimensional input maps A_i.
- $\mathcal B_0$ (output map), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the one-dimensional output maps B_{0,i}.
- $P_{s_i}$ (source axis permutation), bound on [Multidimensional transforms](multidim-transform.md): The index permutation of source axis i.
- $P_{t_i}$ (padded axis permutation), bound on [Multidimensional transforms](multidim-transform.md): The index permutation of padded axis i.
- $A_i$ (axis input map), bound on [Multidimensional transforms](multidim-transform.md): The linear input map of axis i.
- $B_{0,i}$ (axis output map), bound on [Multidimensional transforms](multidim-transform.md): The linear output map of axis i.
- $F_{q_i}$ (axis transform), bound on [Multidimensional transforms](multidim-transform.md): The one-dimensional normalized discrete Fourier transform of length q_i.
- $F_{\boldsymbol q}$ (multidimensional transform), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the axis transforms F_{q_i}.
- $X_i$ (axis operator X), bound on [Multidimensional transforms](multidim-transform.md): An operator on axis i.
- $Y_i$ (axis operator Y), bound on [Multidimensional transforms](multidim-transform.md): An operator on axis i.
- $d$ (axis count), bound on [Chinese-remainder address map](crt-map.md): The number of prime cyclic axes, with no coefficient axis counted.
- $s_i$ (axis length), bound on [Chinese-remainder address map](crt-map.md): The length of prime cyclic axis i; the s_i are pairwise coprime.
- $P_i$ (prefix product), bound on [Chinese-remainder address map](crt-map.md): The product of the axis lengths s_j with j<i.
- $\mu_i$ (coordinate exponent), bound on [Chinese-remainder address map](crt-map.md): The inverse of P_i modulo s_i, the exponent of x_i in the image of x.
- $\Phi$ (address map), bound on [Chinese-remainder address map](crt-map.md): The ring isomorphism sending x to the product of x_i^{mu_i}.
- $x_i$ (axis variable), bound on [Chinese-remainder address map](crt-map.md): The variable of axis i in the multi-axis ring.
- $k$ (coefficient index), bound on [Chinese-remainder address map](crt-map.md): A single coefficient index, an exponent of x; not an output index tuple as on the multidimensional-transform page.
- $a_j$ (mixed-radix digit), bound on [Chinese-remainder address map](crt-map.md): The digit of k of weight P_j, with 0<=a_j<s_j.
- $j$ (digit index), bound on [Chinese-remainder address map](crt-map.md): The index of an axis before axis i, in the product defining P_i, and later the index of a mixed-radix digit.
- $b_i$ (axis coordinate), bound on [Chinese-remainder address map](crt-map.md): The axis-i coordinate of Phi(x^k).
- $\ell$ (address bits), bound on [Chinese-remainder address map](crt-map.md): The number of address bits of an axis of length r.
- $T$ (padded record count), bound on [Chinese-remainder address map](crt-map.md): The number of padded records, the product of the padded axis lengths t_i.
- $\tau$ (interchange exponent), bound on [Chinese-remainder address map](crt-map.md): A fixed exponent below 1 in the chunk-interchange cost.
- $i$ (axis index), bound on [Chinese-remainder address map](crt-map.md): The index of a prime cyclic axis, from 1 to d.
- $t_i$ (padded axis length), bound on [Chinese-remainder address map](crt-map.md): The length of axis i after zero padding, a power of two between r/2 and r.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the Fourier transform being re-expressed, coprime to t.
- $t$ (transform length), bound on [Gaussian resampling](gaussian-resampling.md): The larger length, a power of two, of the transform through which the length-s transform is expressed.
- $\alpha$ (width parameter), bound on [Gaussian resampling](gaussian-resampling.md): The integer width parameter of the Gaussian weights, with 2<=alpha<sqrt p.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): The relative gap t/s-1 between the target and source lengths.
- $j$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A single integer coordinate index.
- $k$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A single integer coordinate index.
- $q_j$ (nearest coordinate), bound on [Gaussian resampling](gaussian-resampling.md): The integer nearest to tj/s.
- $\beta_j$ (rounding offset), bound on [Gaussian resampling](gaussian-resampling.md): The signed distance tj/s-q_j from tj/s to the nearest integer.
- $E$ (Neumann error), bound on [Gaussian resampling](gaussian-resampling.md): The map N-I, whose norm is small.
- $K$ (series term count), bound on [Gaussian resampling](gaussian-resampling.md): The number of terms of the Neumann series that are kept.
- $\beta$ (unit), bound on [Retained permutation cancellation](retained-permutations.md): A unit modulo q, an integer coprime to q, used as the multiplier of the index permutation R_beta.
- $R_\beta$ (index scaling), bound on [Retained permutation cancellation](retained-permutations.md): The permutation of a length-q vector sending z to the vector with entries z_{beta j}.
- $w$ (summation index), bound on [Retained permutation cancellation](retained-permutations.md): The index of the sum defining the transform of R_beta z.
- $w'$ (new summation index), bound on [Retained permutation cancellation](retained-permutations.md): The summation index after the substitution w' = beta w.
- $\nu$ (setup degree), bound on [Retained permutation cancellation](retained-permutations.md): A fixed exponent such that setup work per line is O(p^nu).
- $F_q^+$ (opposite transform), bound on [Retained permutation cancellation](retained-permutations.md): The discrete Fourier transform of length q with the sign of the exponent reversed.
- $z$ (transformed vector), bound on [Retained permutation cancellation](retained-permutations.md): A vector of q complex entries.
- $A$ (axis input contraction), bound on [Retained permutation cancellation](retained-permutations.md): The linear contraction applied to the input of one axis in the resampling identity.
- $B_0$ (axis output contraction), bound on [Retained permutation cancellation](retained-permutations.md): The linear contraction applied to the output of one axis in the resampling identity.
- $P_s$ (source permutation), bound on [Retained permutation cancellation](retained-permutations.md): The permutation (P_s u)_j = u_{tj} of a length-s vector.
- $P_t$ (target permutation), bound on [Retained permutation cancellation](retained-permutations.md): The permutation (P_t v)_k = v_{-sk} of a length-t vector.
- $u$ (first array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array, not an integer here.
- $v$ (second array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array, not an integer here.
- $a$ (round count), bound on [Retained frequency order](frequency-order.md): The number of rounds of the transform, a=log_2 t.
- $j$ (output index), bound on [Retained frequency order](frequency-order.md): The position of an output of the transform.
- $s$ (completed rounds), bound on [Retained frequency order](frequency-order.md): The number of rounds completed so far.
- $B_t$ (bit-reversal permutation), bound on [Retained frequency order](frequency-order.md): The permutation moving the entry at j to rev_a(j).
- $\mathcal H$ (parallel butterfly), bound on [Retained frequency order](frequency-order.md): The parallel butterfly applying H_0 on every participating axis in one round.
- $J_E$ (recordwise monomial), bound on [Retained frequency order](frequency-order.md): The recordwise operation multiplying each record by y^E.
- $h_p$ (grid spacing), bound on [Error tracking and exact recovery](precision-recovery.md): The grid spacing 2^{-p} of the fixed-point records.
- $L$ (log of padded length), bound on [Error tracking and exact recovery](precision-recovery.md): The base-2 logarithm of the padded length T.
- $a$ (error size), bound on [Error tracking and exact recovery](precision-recovery.md): The size of an error in grid spacings.
- $x$ (disk array), bound on [Error tracking and exact recovery](precision-recovery.md): An array in the unit disk to which a phase or chirp transform is applied.
- $u$ (scaled first digits), bound on [Error tracking and exact recovery](precision-recovery.md): The scaled digit array of the first input.
- $v$ (scaled second digits), bound on [Error tracking and exact recovery](precision-recovery.md): The scaled digit array of the second input.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Gaussian resampling](gaussian-resampling.md): Re-expressing a Fourier transform of prime length s through a transform of nearby power-of-two length t using Gaussian weights, so that only power-of-two transforms are needed.
  Shown as: Parameter and prime-length choice *<predicate>* Gaussian resampling
- [Chinese-remainder address map](crt-map.md): An isomorphism that places a cyclic convolution of length S = s₁⋯s_d on pairwise coprime prime axes, implemented as triangular controlled shifts.
  Shown as: Parameter and prime-length choice *<predicate>* Chinese-remainder address map
- [Fixed-point Gaussian dyadic records](fixed-point.md): Complex values stored as signed two's-complement integers over a power-of-two denominator 2^{-p}; intermediate values are exact and one truncation Q_p rounds back to the p-bit grid.
  Shown as: Parameter and prime-length choice *<predicate>* Fixed-point Gaussian dyadic records

## Pages that build on this one

- The multiplication algorithm: Digits, then the CRT map, two forward transforms with resampling and chirps, a pointwise product, the opposite transform, rescaling, rounding and carry propagation yield the exact 2n-bit product.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Elementary stream operations](stream-ops.md)
- [Bluestein chirp identity](chirp.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Two-point kernel C](phase-kernel.md)
- [Contractions and bilinear contractions](contraction-maps.md)
- [Multidimensional transforms](multidim-transform.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Retained frequency order](frequency-order.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Tensor products of subspaces](tensor-product-of-spaces.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Binary phase frames](phase-frames.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor," (paper)

  > After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $

- "The distinct prime lengths $s_i$ must be close to the powers of two" (paper)

  > The distinct prime lengths $s_i$ must be close to the powers of two $t_i$: their product must occupy a fixed fraction of the padded box, while each ratio $t_i/s_i$ must leave enough separation for resampling. We verify both requirements for the parameters just chosen.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- A simulated reader (reader) trying to answer "Why does kappa equal 2^-182 and not some larger constant? Which part of the cost accounting fixes it, and why is the margin taken to be twice kappa?" got stuck at "These are conservative.": The page fixes kappa = 2^-182 and calls it conservative, but does not say what conservative means or why the value is half the chunk-exchange margin and not some other value. I worked out for myself that 2 kappa must be at most 2^-181, so kappa <= 2^-182, and that 2^-182 is the largest power of two that fits. The wiki itself does not state this reasoning. (stuck at the statement level)
- A simulated reader (reader) trying to answer "Why does kappa equal 2^-182 and not some larger constant? Which part of the cost accounting fixes it, and why is the margin taken to be twice kappa?" got stuck at "These are conservative.": The page calls the exponents conservative but gives no argument for them, so I cannot tell whether 2^-182 is forced or chosen. I could not tell what conservative buys. (stuck at the statement level)

## Previous version (revise it)

It has 541 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 676 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

This page fixes every exponent and size for $n$-bit inputs so that the hypotheses of the butterfly-layer lemma and of [Gaussian resampling](gaussian-resampling.md) hold at once.

Fixed rational exponents make each inequality among them an integer comparison. In the [simultaneous butterfly layer](simultaneous-layer.md), $\tau$ is the exponent in the cost of a chunk interchange, $\sigma$ bounds the growth exponent of recursive calls, $\beta$ sets the threshold $d^\beta$ below which active chunks are handled singly, $\lambda$ is the per-node overhead exponent, $\lambda'$ is the final exponent of the cost $Vd^{\lambda'}$ (up to a constant) on bit volume $V$, $c$ is the exponent of the address-chunk width (here it is not the scaling integer of [Controlled shifts and rational scalings](controlled-shifts.md)), $\epsilon$ is the exponent of the axis count, $C_1$ is the exponent of the guard bits, and $\delta$ is the resampling-cost slack.

Take $\tau=\sigma=1-2^{-50}$, $\beta=1/2$ and $\delta=1/16$. Take $\lambda=1-2^{-52}$ and $c=2^{-56}$. Take $\lambda'=1-2^{-54}$. Take $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$. These are conservative<cite data-source="paper">These constants are deliberately conservative; no optimization is claimed.</cite>.

The layer needs $\max\{\tau,\sigma\}<\lambda<1$, $\tau(1+c/\beta)<\lambda$, $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$ and $\epsilon C_1<1$. The layer conditions hold with room to spare: $\tau(1+c/\beta)<1-31\cdot2^{-55}<\lambda$, since $\tau(1+c/\beta)=(1-2^{-50})(1+2^{-55})=1-31\cdot2^{-55}-2^{-105}$ and $\lambda=1-8\cdot2^{-55}$. Also $\sigma+\beta(1-\sigma)=1-2^{-51}<\lambda<\lambda'<1$, and $\epsilon C_1=20\cdot2^{-75}<1$.

For large $n$ put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$. Here $b$ is the digit width, $p$ sets the precision of the [Fixed-point Gaussian dyadic records](fixed-point.md), and $d$ is the axis count. Put $K=\lfloor d^c\rfloor$, the width in bits of an address chunk. Take the power of two $T$ in $[4n/b,8n/b)$, so $Tp\in[24n,48n)$.

Let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$; choose $d\ell-\log_2T\in[0,d)$ of the axis lengths to be $r/2$ and the others $r$, with the last axis of length $r$. The count lies in $[0,d)$ since $\ell$ rounds up, so some axis has length $r$; the product is $r^d/2^{d\ell-\log_2T}=T$. Thus $t_i\in\{r/2,r\}$, $\prod_it_i=T$ and $t_d=r$.

The lemmas assume $a_dp^\epsilon\le d\le b_dp^\epsilon$, $2^{a_rp/d}\le r\le2^{b_rp/d}$ and $d\ell\le C_\ell p$ for fixed constants $a_d,b_d,a_r,b_r,C_\ell$. Since $2^{b-1}<n\le2^b$, we get $b/2\le\log_2T\le b$ for large $b$; with $b^\epsilon/2\le d\le b^\epsilon\le b$ this yields $\frac1{12}p^\epsilon\le d\le p^\epsilon$ and $\frac p{12d}\le\ell\le\frac p{3d}$. These choices give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$, $r=2^{\Theta(p^{1-\epsilon})}$, so the comparison constants $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, $C_\ell=1$ can be fixed for all lengths at once.

## Primes

Put $\alpha=\lceil(12d^2b)^{1/4}\rceil$, the Gaussian width of resampling. Put $\gamma=2d\alpha^2$ and $\eta=1/(4d)$, where $\gamma$ is the exponent of the scale factor $2^\gamma$ of $d$-axis resampling, and $\eta$ is the smallest relative distance at which a prime $s_i$ may lie below $t_i$. As $\lceil A\rceil\le2A$ for real $A\ge1$ and $8\sqrt{12}<28$, then $\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}$, so $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$.

Each $s_i$ is a prime whose relative distance below $t_i$ lies in $[\eta,2\eta)$. The nearer end gives the gap resampling needs; the farther end keeps $S$ a fixed fraction of $T$.

In the prime-interval lemma below, $q$ is an integer, not a radix or a sequence length as on earlier pages. By the prime-interval lemma of Harvey and van der Hoeven (used without proof), for $0<\eta<1/4$ and real $x>e^{2/\eta}$, the interval of integers $q$ with $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes<cite data-source="paper">contains at least $\eta x/(2\log x)$ primes</cite>.

Both $x=r/2$ and $x=r$ qualify since $\log x>8d=2/\eta$, because $\log(r/2)/d=\Theta(p^{1-2\epsilon})\to\infty$; the count $x/(8d\log x)$ exceeds $d$ because $x>8d^2\log x$, as $\log(8d^2\log x)=\Theta(\log p)=o(\log x)$.

The two intervals are disjoint since $(1-\eta)r/2<(1-2\eta)r$, and lie above $2$. Choose distinct odd primes with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$; $\gcd(s_i,t_i)=1$ as $t_i$ is a power of two. This choice supplies the prime axis lengths of the [Chinese-remainder address map](crt-map.md). Put $S=\prod_is_i$.

Multiplying the lower bounds and applying strict Bernoulli gives $S/T>(1-1/(2d))^d>1/2$ for $d\ge2$, because $(1-1/(2d))^d>1-d/(2d)$. With $s_i<t_i$ this gives $T/2<S<T$.

For the separation, $s_i\le(1-\eta)t_i$ gives $t_i/s_i\ge1/(1-\eta)$. With $\theta_i=t_i/s_i-1\ge\eta/(1-\eta)>\eta$ we get $\alpha^4\theta_i>12d^2b/(4d)=3db\ge6b=p$, the separation hypothesis of the resampling lemma; also $t_i\le r\le T<2^p$.

Trial division costs $dr^{3/2}\operatorname{poly}(p)$, with logarithm $o(p)$. The deterministic search for the primes takes $n^{o(1)}=o(n)$ time, since its logarithm is $o(p)$ and $p=\Theta(\log n)$; all primes and length parameters are generated by the machine, not given as advice.<cite data-source="paper">the search takes $n^{o(1)}=o(n)$ time</cite>

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

Write the body to `exegenius/tasks/0377-write-parameter-choice.answer.md` and the JSON to `exegenius/tasks/0377-write-parameter-choice.answer.json`, then run `exegenius submit 0377-write-parameter-choice` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0377-write-parameter-choice`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
