# exegenius task 0035-write-parameter-choice

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/W2WOP15R` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (modular arithmetic, primes and coprimality, the Chinese remainder theorem, permutations, induction, recurrences), calculus-level analysis (logarithms, floor and ceiling, norms and rounding errors), linear algebra (vectors, matrices, invertibility, rank, over the reals, complex numbers and F2), and algorithms (asymptotic notation, schoolbook multiplication, divide and conquer, sorting) with a first look at the FFT. They know basic multitape Turing machines and tapes, polynomials and complex numbers including roots of unity. They have not met Schoenhage-Strassen or Karatsuba-level multiplication algorithms in depth, ring and group-algebra language beyond polynomials, tensor products, numerical error analysis of fixed-point transforms, or any research literature on integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n conjecture for integer multiplication (also: n log n optimality conjecture, Schönhage–Strassen conjecture)
- Established n log n multiplier
- Arrays, addresses and volume on tapes (also: address field, logical volume)
- Elementary stream operations (also: split and merge, row splitting)
- Controlled cyclic shifts (also: controlled shifts, ordered affine streams)
- Rank, subspaces and orthogonal complements (also: nondegenerate subspace, orthogonal residual)
- Cyclic convolution (also: convolution)
- Discrete Fourier transform (also: Fourier transform, DFT)
- Multidimensional (tensor) transform (also: tensor transform)
- Two-point butterfly (also: H₀, butterfly operation)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring, R_r)
  - $y$ (ring variable): The formal polynomial variable, whose powers y^a act as roots of unity of order 2r.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform (also: Nussbaumer polynomial transform, stored frequency order)
- Signed packing of polynomial products (also: Kronecker substitution)
- Linear exchange network with restored scratch wires (also: bank exchange, finite network, role)
- Frames on wire arrays (also: frame, common-frame identity)
- Subspace labels from three-element subsets (also: rank saving construction, orthogonal residual labels)
- Address shear and lower-triangular factorization (also: Bruhat factorization, matrix shear)
- Recursive rank saving (also: power saving recurrence)
- Fast address-chunk interchange (also: chunk swap, tape interchange)
- Phase frames and the two-point kernel C (also: binary phase interface, C kernel)
- Packed selected-bit addition (also: packed XOR, exceptional address repair)
- Fixed-point disk-grid arithmetic (also: disk grid, Gaussian dyadics, truncation Q_p)
- Fast simultaneous butterfly layer (also: simultaneous normalized butterfly layer)
- Convolution over the polynomial ring (also: synthetic convolution)
- Coefficient (phase) twist (also: twist)
- Bluestein chirp identity (also: chirp identity, chirp transform)
- Gaussian resampling (also: Gaussian gridding, resampling)
- Retained permutations and their cancellation (also: no-sort resampling)
- Chinese-remainder address map (also: CRT map, Agarwal–Cooley map)
- Integer product as digit convolution (also: radix-2^b digits)
- Rounding and carry propagation (also: exact recovery, carry propagation)
- Logarithms and iterated logarithm notation (also: log, lg, log base 2, log2, powers of the logarithm, (lg n)^c)
- Big-Omega, Theta and little-o notation (also: Omega, Theta, Ω, Θ, little-o, asymptotic lower bound, tight bound)
- Binary representation and bit operations (also: binary strings, bits, XOR, exclusive or, bitwise operations, two's complement, Hamming weight, bit length)
- Modular arithmetic (also: congruence, residues mod m, Z/mZ, integers modulo m, centered residue, mod, wraparound)
- Primes, coprimality and gcd (also: prime numbers, pairwise coprime, relatively prime, greatest common divisor, gcd, Euclidean algorithm, prime number theorem, primes just below a number)
- Chinese remainder theorem (also: CRT, Chinese remainder, residues modulo coprime moduli)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, Euler's formula, twiddle factor, ω)
- Vectors, matrices and invertibility (also: matrix multiplication, matrix inverse, invertible matrix, linear map, linear combination, lower-triangular matrix, permutation matrix, identity matrix, transpose, linear operator)
- Finite field F2 arithmetic (also: GF(2), binary field, mod 2 arithmetic, Z/2Z, F_2)
- Permutations and Cartesian products (also: bijection, permutation of indices, index set, product set, multi-index, coordinate permutation, lexicographic order, mixed-radix indexing, row-major order)
- Floor, ceiling and summation notation (also: floor function, ceiling function, ⌊x⌋, ⌈x⌉, sigma notation, geometric series, indicator vector)
- Recurrences and induction (also: recurrence relation, solving recurrences, unrolling a recurrence, proof by induction, master theorem, divide and conquer recurrence)
- Norms, absolute values and error bounds (also: max norm, sup norm, infinity norm, triangle inequality, modulus bound, rounding error, truncation error, round to nearest integer, unit disk)
- Fast Fourier transform and divide and conquer (also: FFT, Cooley-Tukey, fast Fourier transform, O(n log n) transform, convolution theorem, multiplying polynomials by FFT)
- Sorting and data movement on tapes (also: sorting, merge, scan, linear scan, stream, sequential access)
- Finite alphabet encodings and constant-factor simulation (also: alphabet, constant overhead, constant factor slowdown, encoding data as tape symbols, fixed finite state control, Turing machine simulation)
- Ring and group notions for polynomials (also: commutative ring, ring with identity, quotient ring, isomorphism, ring homomorphism, unit of a ring)

## This page

Concept: Parameter choices and prime source lengths
Gloss: The size parameters b=⌈log₂n⌉, precision p=6b, number of axes d=⌊b^ε⌋, chunk width K=⌊d^c⌋, padded size T≈n/b, power-of-two axis lengths t_i∈{r/2,r}, and distinct primes s_i just below t_i with T/2 < ∏s_i < T, chosen so resampling hypotheses and all tape lemmas apply.
Also called: fixed rational choice

## This page in the argument

The step: Parameter choices: $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$, axis lengths $t_i\in\{r/2,r\}$ with $\prod t_i=T$, $t_d=r$, and distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$, $\eta=1/(4d)$, so that $T/2<S<T$ and every Gaussian-resampling hypothesis holds.
How: Fix conservative rational exponents, then verify by direct estimates that the prime intervals contain enough primes, that the product of the primes occupies more than half the box, and that $\alpha^4\theta_i>p$.
Why: The sources say the primes must be close to the powers of two so that their product fills a fixed fraction of the padded box while each ratio leaves enough separation for resampling. (the sources say so: "$t_i$: their product must occupy a fixed fraction of the padded box," (paper))
Striking feature: Every exponent is a power of two with an enormous negative exponent ($\epsilon=2^{-75}$, $c=2^{-56}$, $1-\tau=2^{-50}$), chosen to make all hypotheses hold with room to spare rather than to optimize $\kappa$. (explain why it holds, from the method)

Its sub-steps, in order:

- Fixed rational exponents: $\tau=\sigma=1-2^{-50}$, $\beta=\frac12$, $\delta=\frac1{16}$.
- $\lambda=1-2^{-52}$ and $c=2^{-56}$.
- $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$ (and $\lambda'=1-2^{-54}$), chosen deliberately conservative with no optimization claimed.
- Sizes: $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$.
- Take the power of two $T\in[4n/b,8n/b)$ and $r=2^{\lceil(\log_2T)/d\rceil}$, $\ell=\log_2r$.
- Choose $d\ell-\log_2T$ axis lengths equal to $r/2$ and the rest equal to $r$, so $t_i\in\{r/2,r\}$, $\prod t_i=T$ and the last axis has $t_d=r$.
- Set $\alpha=\lceil(12d^2b)^{1/4}\rceil$, $\gamma=2d\alpha^2$ and $\eta=1/(4d)$.
- Then $\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}$, so $2\le\alpha<\sqrt p$ and $\gamma=o(b)$ (for $b\ge2^{24}$, $\gamma\le b/4$).
- Primes in $((1-2\eta)x,(1-\eta)x]$: for $0<\eta<1/4$ and $x>e^{2/\eta}$ there are at least $\eta x/(2\log x)$ primes (Rosser–Schoenfeld), which exceeds $d$ for $x\in\{r/2,r\}$.
- Choose distinct odd primes with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$; $\gcd(s_i,t_i)=1$ since $t_i$ is a power of two.
- Multiplying the lower bounds with strict Bernoulli gives $S/T>(1-\frac1{2d})^d>\frac12$, so $T/2<S<T$ with $S=\prod s_i$.
- With $\theta_i=t_i/s_i-1>\eta$: $\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\ge6b=p$, so the resampling hypothesis $\theta>p/\alpha^4$ holds, and $t_i\le T<2^p$.
- The primes are found by deterministic trial division in time $O(dr^{3/2}\operatorname{poly}(p))=n^{o(1)}=o(n)$.

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.; how: Reduce the product to a convolution of short integer coefficients, evaluate the convolution through power-of-two transforms over $\mathbb C[y]/(y^r+1)$, and replace the two tape operations that each cost a factor $\log n$ (address rearrangement and butterfly layers) by procedures whose cost per bit is a power of their parameter below one; then total the costs. (on [Integer multiplication below n log n](main-theorem.md))
- The multiplication algorithm: form base-$2^b$ digits, place them on distinct prime cyclic axes by the Chinese-remainder map $\Phi$, run two source transforms (Gaussian resampling plus chirp convolution through a twisted ring convolution), multiply pointwise, run the opposite transform, rescale, round and propagate carries, obtaining the exact $2n$-bit product in $O(Tp)$ steps beyond the layer costs.; how: Choose compatible parameters, reduce the product to a cyclic convolution of digit coefficients, evaluate the convolution through Gaussian-resampled transforms with all permutations left in the formulas, and recover exact integer coefficients from the approximations by an error bound below one half. (on [The multiplication algorithm](multiplication-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S8.1.1, S8.1.2, S8.1.3, S8.1.4, S8.1.5, S8.1.6, S8.1.7, S8.1.8, S8.1.9, S8.1.10, S8.1.11, S8.1.12, S8.1.13). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S8.1.1**: Fixed rational exponents: $\tau=\sigma=1-2^{-50}$, $\beta=\frac12$, $\delta=\frac1{16}$.
Source: "\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\" (paper)
> The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.

**S8.1.2**: $\lambda=1-2^{-52}$ and $c=2^{-56}$.
Source: "\lambda=1-2^{-52},\qquad c=2^{-56},\qquad" (paper)
> The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.

**S8.1.3**: $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$ (and $\lambda'=1-2^{-54}$), chosen deliberately conservative with no optimization claimed.
Source: "C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}." (paper)
> The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.

**S8.1.4**: Sizes: $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$.
Source: "b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor," (paper)
> After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $

**S8.1.5**: Take the power of two $T\in[4n/b,8n/b)$ and $r=2^{\lceil(\log_2T)/d\rceil}$, $\ell=\log_2r$.
Source: "Take the power of two $T$ in $[4n/b,8n/b)$, and let" (paper)
> After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $b$, the bounds on $n,T$ give $b/2\leq\log_2T\leq b$. Since $p=6b$, $d=\lfloor b^\epsilon\rfl

**S8.1.6**: Choose $d\ell-\log_2T$ axis lengths equal to $r/2$ and the rest equal to $r$, so $t_i\in\{r/2,r\}$, $\prod t_i=T$ and the last axis has $t_d=r$.
Source: "t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r." (paper)
> After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $b$, the bounds on $n,T$ give $b/2\leq\log_2T\leq b$. Since $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $d\leq b$, they imply \[ \frac1{12}p^\epsilon\leq d\leq p^\epsilon, \qquad \frac{p}{12d}\leq\ell\leq\frac{p}{3d}. \] Thus we fix $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, and $C_\ell=1$ in the layer an

**S8.1.7**: Set $\alpha=\lceil(12d^2b)^{1/4}\rceil$, $\gamma=2d\alpha^2$ and $\eta=1/(4d)$.
Source: "\alpha=\left\lceil(12d^2b)^{1/4}\right\rceil," (paper)
> Set \[ \alpha=\left\lceil(12d^2b)^{1/4}\right\rceil, \qquad \gamma=2d\alpha^2,\qquad \eta=\frac1{4d}. \] The ceiling does not affect the needed bounds: for $A\ge1$, $\lceil A\rceil\le2A$, and hence \begin{equation}\label{eq:gamma} \alpha\le2(12d^2b)^{1/4},\qquad \gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}. \end{equation} It follows that $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$. For example $b\ge2^{24}$ implies $\gamma\le b/4$.

**S8.1.8**: Then $\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}$, so $2\le\alpha<\sqrt p$ and $\gamma=o(b)$ (for $b\ge2^{24}$, $\gamma\le b/4$).
Source: "\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}." (paper)
> Set \[ \alpha=\left\lceil(12d^2b)^{1/4}\right\rceil, \qquad \gamma=2d\alpha^2,\qquad \eta=\frac1{4d}. \] The ceiling does not affect the needed bounds: for $A\ge1$, $\lceil A\rceil\le2A$, and hence \begin{equation}\label{eq:gamma} \alpha\le2(12d^2b)^{1/4},\qquad \gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}. \end{equation} It follows that $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$. For example $b\ge2^{24}$ implies $\gamma\le b/4$.

**S8.1.9**: Primes in $((1-2\eta)x,(1-\eta)x]$: for $0<\eta<1/4$ and $x>e^{2/\eta}$ there are at least $\eta x/(2\log x)$ primes (Rosser–Schoenfeld), which exceeds $d$ for $x\in\{r/2,r\}$.
Source: "contains at least $\eta x/(2\log x)$ primes." (paper)
> The prime-interval result \cite[Lemma~5.1]{HarveyHoeven2021}, based on explicit estimates of Rosser and Schoenfeld~\cite{RosserSchoenfeld1962}, gives the following bound: for $0<\eta<1/4$ and $x>e^{2/\eta}$, the interval \[ (1-2\eta)x<q\leq(1-\eta)x \] contains at least $\eta x/(2\log x)$ primes. Here $\log$ is the natural logarithm. The size bounds in \eqref{eq:sizes} give $d=\Theta(p^\epsilon)$ and $\log r=\Theta(p/d)$. For large $n$ we have $d\geq2$, so $0<\eta<1/4$, and \[ \frac{\log(r/2)}d=\Theta(p^{1-2\epsilon})\longrightarrow\infty. \] Thus both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$. For either choice, the stated lower bound for the number of primes is $x/(8d\log x)$ and exceeds $d$: indeed, $\log x=\Theta(p^{1-\epsilon})$, whereas $\log(8d^2\log x)=O(\log p)=o(\log x)$, so $x>8d^2\log x$ eventually. The two intervals are disjoint because $(1-\eta)r/2<(1-2\eta)r$ for $\eta<1/4$, and both intervals lie above $2$. We may therefore choose distinct odd primes satisfying \[ (1-2\eta)t_i<s_i\leq(1-\e

**S8.1.10**: Choose distinct odd primes with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$; $\gcd(s_i,t_i)=1$ since $t_i$ is a power of two.
Source: "(1-2\eta)t_i<s_i\leq(1-\eta)t_i." (paper)
> east $\eta x/(2\log x)$ primes. Here $\log$ is the natural logarithm. The size bounds in \eqref{eq:sizes} give $d=\Theta(p^\epsilon)$ and $\log r=\Theta(p/d)$. For large $n$ we have $d\geq2$, so $0<\eta<1/4$, and \[ \frac{\log(r/2)}d=\Theta(p^{1-2\epsilon})\longrightarrow\infty. \] Thus both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$. For either choice, the stated lower bound for the number of primes is $x/(8d\log x)$ and exceeds $d$: indeed, $\log x=\Theta(p^{1-\epsilon})$, whereas $\log(8d^2\log x)=O(\log p)=o(\log x)$, so $x>8d^2\log x$ eventually. The two intervals are disjoint because $(1-\eta)r/2<(1-2\eta)r$ for $\eta<1/4$, and both intervals lie above $2$. We may therefore choose distinct odd primes satisfying \[ (1-2\eta)t_i<s_i\leq(1-\eta)t_i. \] Every $\gcd(s_i,t_i)$ equals one because $t_i$ is a power of two. Put $S=\prod_i s_i$. Multiplying the lower bounds on $s_i$ and applying strict Bernoulli inequality gives \[ \frac ST> \left(1-\frac1{2d}\right)^d>\frac12 \qquad(d\geq2). \] Together with $s_i<t_i$, this gives $T/2<S<T$. Writing $\theta_i=t_i/s_i-1$, the upper bound on $s_i$ gives $\theta_i\geq\eta/(1-\eta)>\eta$. Therefore \[ \alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p. \] The choice of $\alpha$ gives $\alpha=\Theta(p^{1/4+\epsilon/2})$, and \eqref{eq:gamma} already ensures $2\leq\alpha<\sqrt p$ for large $n$. We also have $t_i\leq r\leq T<8n/b<2^{6b}=2^p$. Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for all sufficiently large

**S8.1.11**: Multiplying the lower bounds with strict Bernoulli gives $S/T>(1-\frac1{2d})^d>\frac12$, so $T/2<S<T$ with $S=\prod s_i$.
Source: "\left(1-\frac1{2d}\right)^d>\frac12" (paper)
> og(r/2)}d=\Theta(p^{1-2\epsilon})\longrightarrow\infty. \] Thus both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$. For either choice, the stated lower bound for the number of primes is $x/(8d\log x)$ and exceeds $d$: indeed, $\log x=\Theta(p^{1-\epsilon})$, whereas $\log(8d^2\log x)=O(\log p)=o(\log x)$, so $x>8d^2\log x$ eventually. The two intervals are disjoint because $(1-\eta)r/2<(1-2\eta)r$ for $\eta<1/4$, and both intervals lie above $2$. We may therefore choose distinct odd primes satisfying \[ (1-2\eta)t_i<s_i\leq(1-\eta)t_i. \] Every $\gcd(s_i,t_i)$ equals one because $t_i$ is a power of two. Put $S=\prod_i s_i$. Multiplying the lower bounds on $s_i$ and applying strict Bernoulli inequality gives \[ \frac ST> \left(1-\frac1{2d}\right)^d>\frac12 \qquad(d\geq2). \] Together with $s_i<t_i$, this gives $T/2<S<T$. Writing $\theta_i=t_i/s_i-1$, the upper bound on $s_i$ gives $\theta_i\geq\eta/(1-\eta)>\eta$. Therefore \[ \alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p. \] The choice of $\alpha$ gives $\alpha=\Theta(p^{1/4+\epsilon/2})$, and \eqref{eq:gamma} already ensures $2\leq\alpha<\sqrt p$ for large $n$. We also have $t_i\leq r\leq T<8n/b<2^{6b}=2^p$. Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for all sufficiently large input lengths. The superpolynomial growth of $r$ established above also supplies the setup condition in Lemma~\ref{lem:tensor-resampling}.

**S8.1.12**: With $\theta_i=t_i/s_i-1>\eta$: $\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\ge6b=p$, so the resampling hypothesis $\theta>p/\alpha^4$ holds, and $t_i\le T<2^p$.
Source: "\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p." (paper)
> ndeed, $\log x=\Theta(p^{1-\epsilon})$, whereas $\log(8d^2\log x)=O(\log p)=o(\log x)$, so $x>8d^2\log x$ eventually. The two intervals are disjoint because $(1-\eta)r/2<(1-2\eta)r$ for $\eta<1/4$, and both intervals lie above $2$. We may therefore choose distinct odd primes satisfying \[ (1-2\eta)t_i<s_i\leq(1-\eta)t_i. \] Every $\gcd(s_i,t_i)$ equals one because $t_i$ is a power of two. Put $S=\prod_i s_i$. Multiplying the lower bounds on $s_i$ and applying strict Bernoulli inequality gives \[ \frac ST> \left(1-\frac1{2d}\right)^d>\frac12 \qquad(d\geq2). \] Together with $s_i<t_i$, this gives $T/2<S<T$. Writing $\theta_i=t_i/s_i-1$, the upper bound on $s_i$ gives $\theta_i\geq\eta/(1-\eta)>\eta$. Therefore \[ \alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p. \] The choice of $\alpha$ gives $\alpha=\Theta(p^{1/4+\epsilon/2})$, and \eqref{eq:gamma} already ensures $2\leq\alpha<\sqrt p$ for large $n$. We also have $t_i\leq r\leq T<8n/b<2^{6b}=2^p$. Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for all sufficiently large input lengths. The superpolynomial growth of $r$ established above also supplies the setup condition in Lemma~\ref{lem:tensor-resampling}.

**S8.1.13**: The primes are found by deterministic trial division in time $O(dr^{3/2}\operatorname{poly}(p))=n^{o(1)}=o(n)$.
Source: "$O(dr^{3/2}\operatorname{poly}(p))$" (paper)
> The machine finds these primes by scanning the two intervals deterministically and testing each candidate by trial division through its square root. Testing every candidate would visit $O(r)$ candidates and at most $O(\sqrt r)$ trial divisors per candidate. Elementary division on $O(\log r)$-bit integers and management of a list of at most $d$ selected primes give the conservative bound $O(dr^{3/2}\operatorname{poly}(p))$. Its logarithm is \[ O(\log p+\log r)=O(\log p+p/d)=o(p). \] Since $p=6\lceil\log_2 n\rceil=\Theta(\log n)$, the search takes $n^{o(1)}=o(n)$ time. All remaining scalar setup, including comparisons for fixed rational powers, modular inverses, prime products and shape descriptors, has cost polynomial in $p$. For example, $d=\lfloor b^{2^{-75}}\rfloor$ is found by binary search using exact comparisons $d^{2^{75}}\le b$; the exponent is fixed. The same procedure computes $K$ and all other fixed rational powers. All primes and length parameters are therefore generated by the machine; they are not advice.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Chinese-remainder address map](crt-address-map.md): The Agarwal–Cooley isomorphism Φ: C[x]/(x^S−1) → C[x₁..x_d]/(x_i^{s_i}−1), x ↦ ∏ x_i^{μ_i}, for pairwise coprime (prime) s_i with S = ∏ s_i, which turns one long cyclic convolution into one on distinct prime axes and is implemented by triangular controlled shifts.
  Shown as: Parameter choices and prime source lengths *<predicate>* Chinese-remainder address map
- [Gaussian resampling](gaussian-resampling.md): The Harvey–van der Hoeven reduction that expresses a Fourier transform of length s (here a prime) through a power-of-two transform of length t>s via Gaussian-weighted contractions: P_s F_s = 2^{2α²} B₀ P_t F_t A, with the two coordinate permutations P_s,P_t left inside the identity.
  Shown as: Parameter choices and prime source lengths *<predicate>* Gaussian resampling
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md): The ring of complex polynomials of degree < r with y^r = −1, in which multiplying by a power of y permutes the coefficients up to sign, so that powers of y serve as exact roots of unity.
  Shown as: Parameter choices and prime source lengths *<predicate>* Polynomial ring modulo y^r + 1
- [Integer product as digit convolution](radix-digit-convolution.md): Writing each n-bit input as a polynomial in 2^b with ⌈n/b⌉ digits, the integer product is the polynomial product, whose coefficients are below 2^{3b}; with enough zero padding the cyclic convolution has no wraparound, and carries recover the bits.
  Shown as: Parameter choices and prime source lengths *<predicate>* Integer product as digit convolution

## Pages that build on this one

- The multiplication algorithm: The pipeline: form radix digits, apply the CRT address map Φ, run two source transforms (resampling plus chirp convolution plus resampling), multiply pointwise, run the opposite transform, rescale, round and propagate carries; inside the chirp convolution the last coordinate is twisted into C[y]/(y^r+1) and convolved with synthetic transforms.
- Cost accounting and the saving κ: Dividing every cost by V = Tp = Θ(n) gives a table of seven dominant powers of p (layout moves, chunk exchanges, simultaneous butterfly rounds, CRT layout, Gaussian line maps, chirps, packed products), each at most 1−2κ with κ = 2^{−182}, giving total O(n (lg n)^{1−κ}).

## Other pages you may link to

- [The n log n conjecture for integer multiplication](integer-multiplication-conjecture.md)
- [Fixed-point disk-grid arithmetic](fixed-point-truncation.md)
- [Established n log n multiplier](established-multiplier.md)
- [Arrays, addresses and volume on tapes](tape-address-model.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Controlled cyclic shifts](controlled-shift.md)
- [Rank, subspaces and orthogonal complements](linear-algebra-basics.md)
- [Linear exchange network with restored scratch wires](linear-network.md)
- [Address shear and lower-triangular factorization](address-shear.md)
- [Frames on wire arrays](common-frame-principle.md)
- [Subspace labels from three-element subsets](subset-intersection-labels.md)
- [Recursive rank saving](rank-saving-recurrence.md)
- [Fast address-chunk interchange](address-chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Coefficient (phase) twist](phase-twist.md)
- [Rounding and carry propagation](exact-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Multidimensional (tensor) transform](multidimensional-dft.md)
- [Two-point butterfly](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Phase frames and the two-point kernel C](phase-frame-kernel.md)
- [Fast simultaneous butterfly layer](fast-butterfly-layer.md)
- [Convolution over the polynomial ring](ring-convolution.md)
- [Retained permutations and their cancellation](permutation-cancellation.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the saving κ](time-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor," (paper)

  > After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $

- "The distinct prime lengths $s_i$ must be close to the powers of two" (paper)

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

Write the body to `exegenius/tasks/0035-write-parameter-choice.answer.md` and the JSON to `exegenius/tasks/0035-write-parameter-choice.answer.json`, then run `exegenius submit 0035-write-parameter-choice` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0035-write-parameter-choice`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
