# exegenius task 0040-write-multiplication-algorithm

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F3V` (paths below are relative to it)

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

For these sources: The reader is an undergraduate in computer science who has taken discrete mathematics, data structures and algorithms, introductory theory of computation, and the linear algebra and calculus that accompany such a degree. They are fluent with asymptotic analysis, recurrences, binary representation and bitwise operations, modular arithmetic, matrices and rank, vector spaces over the reals, and complex numbers including roots of unity; they know the schoolbook and Karatsuba multiplication algorithms and what a Turing machine with tapes is. They have not studied abstract algebra beyond basics, the FFT's algebraic variants, number-theoretic transforms, finite fields beyond arithmetic mod 2, analytic number theory, numerical analysis of rounding error, or any bit-complexity multiplication algorithm.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Schönhage–Strassen optimality conjecture
- Harvey–van der Hoeven O(n log n) multiplier
- Cyclic convolution
- Integer product as digit convolution
- Discrete Fourier transform (also: Fourier transform, F_q)
- Multidimensional transform
- Two-point butterfly and radix-two recursion (also: H₀, butterfly layer)
- Contractions and error accumulation
- Chinese-remainder map to prime axes
- Prime axis lengths near powers of two
- Gaussian resampling
- Bluestein chirp identity
- Retained permutations cancel in a convolution
- Polynomial ring modulo y^r + 1 (also: negacyclic ring, R_r)
  - $y$ (ring variable): The formal polynomial variable, satisfying y^r = −1 in the ring.
  - $r$ (ring length): The number of complex coefficients in a ring element, a power of two.
- Coefficient phase twist
- Synthetic polynomial transform
- Stored bit-reversed frequency order
- Signed Kronecker packing
- Convolution over the polynomial ring
- Arrays and elementary stream operations on tape
- Controlled shifts and rational scalings
- Bank-exchange network with restored scratch wires
- Frames on network wires
- Nested subspace labels and orthogonal residuals
- Strict rank saving
- Lower-triangular factorization of a matrix
- Cost of a matrix shear on address fields
- Power-width chunk interchange
- Address chunk interchange
  - $V$ (stored bit volume): The number of data bits stored in the array being permuted.
  - $u$ (chunk width): The number of bits in each of the two interchanged address chunks.
  - $\tau$ (interchange exponent): A fixed constant below one, 1 − 2^{−50}, bounding the power of the width in the cost.
- Phase frames and the two-point kernel C
- Packed selected-bit addition
- Exact dyadic intermediates with one truncation
- Simultaneous butterfly layer
- Transform layout and cost
- Parameter choice for the multiplier
- Exact recovery by rounding and carries
- Asymptotic notation beyond big-O (also: Omega notation, Theta notation, little-o, o(...), Ω, Θ, asymptotically smaller, worst-case running time)
- Limits and limit inferior (also: liminf, limsup, limit of a ratio, lim inf, eventually, for all sufficiently large n)
- Logarithms, exponentials, floors and ceilings (also: log base 2, lg n, log_2, natural logarithm, floor function, ceiling function, powers of two, iterated logarithm, log star)
- Recurrences and geometric sums (also: recurrence relation, solving recurrences, geometric series, geometric sum, unrolling a recurrence, divide and conquer)
- Positional number systems and carries (also: binary representation, radix representation, base-b digits, bit string, most significant bit, carry propagation, schoolbook addition, padding with leading zeros)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba, divide-and-conquer multiplication, Toom-Cook, quadratic multiplication)
- Bitwise operations and XOR (also: exclusive or, XOR, bitwise exclusive or, addition modulo 2, bit flip, parity, bit shift, bit mask)
- Modular arithmetic (also: integers modulo q, Z/qZ, congruence, residues, units modulo q, invertible residues, arithmetic mod q, Chinese remainder theorem for integers)
- Primes, coprimality and the extended Euclidean algorithm (also: prime numbers, relatively prime, pairwise coprime, gcd, greatest common divisor, Euclid's algorithm, Bezout identity, modular inverse, odd primes, primality testing by trial division)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, unit complex numbers, complex exponential, Euler's formula, twiddle factor, N-th root of unity)
- Matrices and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, linear operator, linear transformation, identity matrix, diagonal matrix, unitary or involution matrix, matrix-vector product, linear combination)
- Vector spaces, subspaces, dimension and rank (also: subspace, span, basis, linear independence, dimension, rank of a matrix, rank-nullity, kernel, image, column space, direct sum, quotient space)
- Inner products, bilinear forms and orthogonal complements (also: bilinear form, dot product, orthogonality, orthogonal complement, orthogonal subspace, nondegenerate pairing, inner product space, pairing)
- Gaussian elimination and triangular matrices (also: row reduction, LU decomposition, lower triangular matrix, upper triangular matrix, elementary row operations, back substitution, unit triangular matrix, row echelon form)
- Permutations, bijections and permutation matrices (also: permutation, bijection, one-to-one correspondence, inverse permutation, partial permutation, reordering of an array, sorting network, transposition of indices, permutation matrix)
- Arithmetic modulo 2 and linear algebra over F_2 (also: F_2, GF(2), binary field, field with two elements, matrices over F_2, GL(m, F_2), mod 2 arithmetic, boolean linear algebra)
- Finite sets, subsets and counting (also: Cartesian product, subset intersection, set cardinality, binomial coefficient, inclusion-exclusion, product of index sets, power set, three-element subsets, pigeonhole)
- Circuits and directed acyclic graphs (also: arithmetic circuit, linear circuit, wires and gates, directed graph, DAG, network of gates, fan-in, source and sink nodes, layered network)
- Vector norms and the triangle inequality (also: sup norm, maximum norm, infinity norm, ‖·‖_∞, modulus bound, triangle inequality, operator norm, error bound, disk bound)
- Fixed-point numbers, dyadic rationals and rounding (also: fixed point arithmetic, dyadic rational, binary fraction, rounding to nearest integer, truncation, round-off error, precision in bits, numbers with p fractional bits, grid of spacing 2^{-p})
- Row-major order and matrix transposition (also: row-major layout, array layout, transposing a matrix, matrix transpose, k×k binary matrix, lexicographic address, two-dimensional array as a list)
- Subroutines and reductions between problems (also: black-box subroutine, reduction, calling a subroutine, oracle call, problem reduction, conditional lower bound, composition of algorithms, uniform algorithm)
- Convolution of sequences (also: linear convolution, polynomial multiplication as convolution, product of coefficient sequences, discrete convolution, convolution theorem)

## This page

Concept: The multiplication algorithm
Gloss: Digits are placed on prime axes by the CRT map, transformed by resampling plus chirp convolution over the polynomial ring for both operands, multiplied pointwise, transformed with opposite sign, rescaled, rounded and carried.

## This page in the argument

The step: Digits of $x$ and $y$ are placed on prime cyclic axes by the Chinese-remainder map, transformed by Gaussian resampling around a chirp convolution over $\mathbb C[y]/(y^r+1)$, multiplied pointwise, transformed with opposite sign, rescaled, rounded and carried to give the exact $2n$-bit product.
How: Follow the chain of reductions: radix-digit convolution, then cyclic convolution on distinct prime axes, then normalised convolution on power-of-two axes, then convolution over the polynomial ring, and account for every change of representation and its error.
Why: The earlier procedures must be placed inside the multiplication reduction, and every change of representation has to be accounted for. (the sources say so: "The remaining proof places these procedures inside the multiplication
reduction and accounts for every change of representation." (paper))

Its sub-steps, in order:

- Fixed rational exponents $(\tau,\sigma,\lambda',c,\epsilon,\delta,\kappa)$ and sizes $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, $T\in[4n/b,8n/b)$ a power of two, $r=2^\ell$ with axis lengths $t_i\in\{r/2,r\}$, and prime lengths $s_i<t_i$, make $Tp=\Theta(n)$ and satisfy every condition of the earlier procedures. (on [Parameter choice for the multiplier](parameter-choice.md))
- Splitting $x$ and $y$ into $q=\lceil n/b\rceil$ radix-$2^b$ digits turns the product into a convolution of digit sequences with degree below $S$, so cyclic convolution of length $S$ has no wraparound, and every coefficient is below $2^{3b}$. (on [Integer product as digit convolution](radix-digit-convolution.md))
- The assignment $x\mapsto\prod_ix_i^{\mu_i}$ with $\mu_i=P_i^{-1}\bmod s_i$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$, carrying cyclic convolution of length $S=s_1\cdots s_d$ to convolution on the product of cyclic axes, and its action on padded addresses is a sequence of triangular controlled shifts costing $O(Tp\,d^2(1+\ell^\tau))$. (on [Chinese-remainder map to prime axes](crt-axis-map.md))
- With $\zeta=e^{\pi i/r}$, the map $x_d\mapsto\zeta y$ multiplies coefficient $k$ by $\zeta^k$ and is an isomorphism $\mathbb C[x_d]/(x_d^r-1)\to\mathbb C[y]/(y^r+1)$; the negative wrap of the negacyclic product gives exactly the cyclic wrap once the twist is removed. (on [Coefficient phase twist](phase-twist.md))
- Complex cyclic convolution on the padded box is computed by twisting both operands by $\zeta^k$, convolving the first $d-1$ axes over $\mathbb C[y]/(y^r+1)$ with the ring procedure, and untwisting.
- The middle transform $QF_{\boldsymbol t}$ is computed as a chirp multiplication, the complex convolution with the kernel $\widetilde a$, and a second chirp multiplication.
- The source transform applies the linewise Gaussian approximation $\mathcal A$, the computed chirp transform, the approximation $\mathcal B_0$, and an exact scaling by $2^\gamma$, with exact counterpart $RF_{\boldsymbol s}$.
- Place the digits by $\Phi$, transform both operands, multiply pointwise and truncate, apply the opposite-sign transform, scale by $S$ and by $2^{2b+4}S$, round, undo $\Phi$ and propagate carries to output the $2n$-bit product.
- After the three transforms the exact result is $(u*v)/S^2$, so after the first scale it is $(u*v)/S$ and after the second scale $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the integer coefficient convolution.
- Removing the known normalisations $S$ and $2^{2b+4}$, the recovered coefficient error is below $1/2$, so rounding gives the exact integer coefficients and radix carries give the exact $2n$-bit product. (on [Exact recovery by rounding and carries](exact-recovery.md))

It serves these steps, from the main result down:

- One deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a convolution of short digits evaluated by Fourier transforms, speed up the two costly ingredients (moving data between addresses, and butterfly arithmetic) by a power of a block size using one recursive saving, and total every cost term. (on [Sub-n-log-n integer multiplication](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S6.5, S6.6, S6.7, S6.8, S6.9). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S6.5**: Complex cyclic convolution on the padded box is computed by twisting both operands by $\zeta^k$, convolving the first $d-1$ axes over $\mathbb C[y]/(y^r+1)$ with the ring procedure, and untwisting.
Source: "f'&=Q_p(\widetilde\theta^+\mathbin{\cdot}f),\\
 g'&=Q_p(\widetilde\theta^+\mathbin{\cdot}g),\\
 h'&=\widetilde{\mathcal M}_r(\iota f',\iota g'),\\
 \widetilde{\mathcal M}_{\mathbb C}(f,g)
   &=Q_p\!\left(\widetilde\theta^-\mathbin{\cdot}
                    \iota^{-1}h'\right)." (paper)
> For $0\le k<r$, obtain disk-grid approximations $\widetilde\theta_k^+$ and $\widetilde\theta_k^-$ to $\zeta^k$ and $\zeta^{-k}$, each with error less than $2\,2^{-p}$. The exponential routine uses denominator $2r$ and costs $O(p^{1+\delta})$ per factor. Write $\widetilde{\mathcal M}_r$ for the procedure in Proposition~\ref{prop:synthetic-convolution}. For disk-grid inputs $f,g$, one of norm at most $.7$, the computed complex convolution is the following sequence, with the twist arrays repeated on every last-coordinate line: \[ \begin{aligned} f'&=Q_p(\widetilde\theta^+\mathbin{\cdot}f),\\ g'&=Q_p(\widetilde\theta^+\mathbin{\cdot}g),\\ h'&=\widetilde{\mathcal M}_r(\iota f',\iota g'),\\ \widetilde{\mathcal M}_{\mathbb C}(f,g) &=Q_p\!\left(\widetilde\theta^-\mathbin{\cdot} \iota^{-1}h'\right). \end{aligned} \] Each phase product is computed exactly as a dyadic product before $Q_p$ truncates its two components. The factors and disk operands have numerators of magnitude at most $2^p$; four signed integer products and their sums therefore use $O(p)$ bits. Truncation shifts the absolute component numerators right by $p$ places and restores their signs, then writes the resulting disk-grid value in the $w_{\rm c}$-bit component format. It costs $O(p^{1+\delta})$ per coefficient. Generating every factor anew therefore still gives total twist cost $O(Tp^{1+\delta})$. The precision calculation below proves that these calls return disk-grid arrays.

**S6.6**: The middle transform $QF_{\boldsymbol t}$ is computed as a chirp multiplication, the complex convolution with the kernel $\widetilde a$, and a second chirp multiplication.
Source: "x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),\\
 y_0&=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0),\\
 \widetilde{\mathscr C}(x)
     &=Q_p(\overline{\widetilde a}\mathbin{\cdot}y_0)." (paper)
> Let $\widetilde a$ be the resulting disk-grid array, so $\|\widetilde a-a\|_\infty<2\,2^{-p}$. For a disk-grid target tensor $x$ of norm at most $.6$, the computed chirp transform forms the arrays \[ \begin{aligned} x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),\\ y_0&=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0),\\ \widetilde{\mathscr C}(x) &=Q_p(\overline{\widetilde a}\mathbin{\cdot}y_0). \end{aligned} \] Thus $\widetilde a$ is the convolution kernel and $x_0$ is the data operand after the first endpoint phase. Replacing the approximations by exact phases and exact convolution gives $\overline a\mathbin{\cdot}\mathcal M_{\mathbb C} (a,\overline a\mathbin{\cdot}x)=QF_{\boldsymbol t}x$ by \eqref{eq:permuted-chirp}. Below we show that $\|x\|_\infty\le.6$ implies $\|x_0\|_\infty\le.6$, which supplies the smaller operand required by the computed convolution.

**S6.7**: The source transform applies the linewise Gaussian approximation $\mathcal A$, the computed chirp transform, the approximation $\mathcal B_0$, and an exact scaling by $2^\gamma$, with exact counterpart $RF_{\boldsymbol s}$.
Source: "For a source disk-grid tensor of norm at most $.5$, write
$\widetilde{\mathscr F}$ for the following procedure: apply the linewise
approximation to $\mathcal A$, apply the
computed chirp transform $\widetilde{\mathscr C}$, apply the linewise
approximation to $\mathcal B_0$, and multiply the grid numerators
exactly by $2^\gamma$." (paper)
> For a source disk-grid tensor of norm at most $.5$, write $\widetilde{\mathscr F}$ for the following procedure: apply the linewise approximation to $\mathcal A$, apply the computed chirp transform $\widetilde{\mathscr C}$, apply the linewise approximation to $\mathcal B_0$, and multiply the grid numerators exactly by $2^\gamma$. Its exact counterpart is \[ \mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A =RF_{\boldsymbol s}. \] Here an exact counterpart replaces every numerical subroutine by the exact map it approximates and omits truncations. The source arrays are stored in the padded power-of-two box, with zeros outside the valid source coordinates. The compressed scalar output uses $w_{\rm c}$-bit components. Appending $\gamma$ zero bits to each word gives the exact scaled numerator in the known signed width $w_{\rm c}+\gamma$. For the stated input norm, the disk estimate below proves that every scaled coordinate still belongs to $\mathbb D_p$. Its component numerators therefore have magnitude at most $2^p$, so a scan removes only leading sign-extension bits and returns the same integers in $w_{\rm c}$ bits. This scan costs $O(T(w_{\rm c}+\gamma))=O(Tp)$ and leaves the padded zero records zero. Define the opposite-sign procedure by \[ \widetilde{\mathscr F}^{+}(z) =\overline{\widetilde{\mathscr F}(\overline z)}; \] its exact counterpart is $RF_{\boldsymbol s}^{+}$ by Lemma~\ref{lem:chirp-permutation}.

**S6.8**: Place the digits by $\Phi$, transform both operands, multiply pointwise and truncate, apply the opposite-sign transform, scale by $S$ and by $2^{2b+4}S$, round, undo $\Phi$ and propagate carries to output the $2n$-bit product.
Source: "With these streams prepared, perform the following operations.
\begin{enumerate}
\item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain
source arrays $u,v$." (paper)
> With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the gri

**S6.9**: After the three transforms the exact result is $(u*v)/S^2$, so after the first scale it is $(u*v)/S$ and after the second scale $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the integer coefficient convolution.
Source: "By \eqref{eq:source-permutation-cancel}, the exact
counterpart after the three transforms is $(u*v)/S^2$, so after the
first scale it is $w=(u*v)/S$.  The second scale gives
$2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original
integer coefficient convolution." (paper)
> The two occurrences of $S$ in this algorithm undo different normalizations. By \eqref{eq:source-permutation-cancel}, the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$. The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution. The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$; it also justifies the rounding, carries, and output length.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S6.1 (on [Parameter choice for the multiplier](parameter-choice.md)): Fixed rational exponents $(\tau,\sigma,\lambda',c,\epsilon,\delta,\kappa)$ and sizes $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, $T\in[4n/b,8n/b)$ a power of two, $r=2^\ell$ with axis lengths $t_i\in\{r/2,r\}$, and prime lengths $s_i<t_i$, make $Tp=\Theta(n)$ and satisfy every condition of the earlier procedures.
- S6.2 (on [Integer product as digit convolution](radix-digit-convolution.md)): Splitting $x$ and $y$ into $q=\lceil n/b\rceil$ radix-$2^b$ digits turns the product into a convolution of digit sequences with degree below $S$, so cyclic convolution of length $S$ has no wraparound, and every coefficient is below $2^{3b}$.
- S6.3 (on [Chinese-remainder map to prime axes](crt-axis-map.md)): The assignment $x\mapsto\prod_ix_i^{\mu_i}$ with $\mu_i=P_i^{-1}\bmod s_i$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$, carrying cyclic convolution of length $S=s_1\cdots s_d$ to convolution on the product of cyclic axes, and its action on padded addresses is a sequence of triangular controlled shifts costing $O(Tp\,d^2(1+\ell^\tau))$.
- S6.4 (on [Coefficient phase twist](phase-twist.md)): With $\zeta=e^{\pi i/r}$, the map $x_d\mapsto\zeta y$ multiplies coefficient $k$ by $\zeta^k$ and is an isomorphism $\mathbb C[x_d]/(x_d^r-1)\to\mathbb C[y]/(y^r+1)$; the negative wrap of the negacyclic product gives exactly the cyclic wrap once the twist is removed.
- S6.10 (on [Exact recovery by rounding and carries](exact-recovery.md)): Removing the known normalisations $S$ and $2^{2b+4}$, the recovered coefficient error is below $1/2$, so rounding gives the exact integer coefficients and radix carries give the exact $2n$-bit product.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Integer product as digit convolution](radix-digit-convolution.md): Splitting two integers into radix-2^b digits turns their product into a convolution of the digit sequences followed by carry propagation.
  Shown as: The multiplication algorithm *<predicate>* Integer product as digit convolution
- [Chinese-remainder map to prime axes](crt-axis-map.md): An algebra isomorphism from cyclic convolution of length S = s_1⋯s_d (pairwise coprime) to convolution on the product of cyclic axes of lengths s_i, implemented by triangular controlled shifts.
  Shown as: The multiplication algorithm *<predicate>* Chinese-remainder map to prime axes
- [Gaussian resampling](gaussian-resampling.md): Harvey–van der Hoeven's identity expressing a Fourier transform of prime-product length s as a transform of power-of-two length t, between two cheap Gaussian-weighted linear contractions A and B₀.
  Shown as: The multiplication algorithm *<predicate>* Gaussian resampling
- [Bluestein chirp identity](chirp-identity.md): A Fourier transform of even length t can be written as pointwise multiplication by a chirp phase a, a cyclic convolution with a, and another chirp multiplication.
  Shown as: The multiplication algorithm *<predicate>* Bluestein chirp identity
- [Retained permutations cancel in a convolution](permutation-cancellation.md): The coordinate permutations left inside the resampled transform cancel across two forward transforms, a pointwise product and an opposite-sign transform, so no full sort is executed.
  Shown as: The multiplication algorithm *<predicate>* Retained permutations cancel in a convolution
- [Coefficient phase twist](phase-twist.md): Substituting x_d ↦ ζy with ζ = e^{πi/r} multiplies coefficient k by ζ^k and turns cyclic convolution of length r into negacyclic polynomial multiplication, exactly undone by untwisting.
  Shown as: The multiplication algorithm *<predicate>* Coefficient phase twist
- [Convolution over the polynomial ring](ring-convolution.md): Normalized convolution of arrays with entries in the negacyclic ring: forward synthetic transforms, pointwise polynomial products by Kronecker packing, and the opposite transform in the retained order.
  Shown as: The multiplication algorithm *<predicate>* Convolution over the polynomial ring
- [Parameter choice for the multiplier](parameter-choice.md): Fixed rational exponents (τ, σ, λ′, c, ε, δ, κ) and sizes b = ⌈log₂n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, T ≈ n/b, r = 2^ℓ, with prime axis lengths s_i < t_i.
  Shown as: The multiplication algorithm *<predicate>* Parameter choice for the multiplier
- [Exact recovery by rounding and carries](exact-recovery.md): Removing the known normalizations S and 2^{2b+4}, showing the recovered coefficient error is below 1/2, rounding to integers, and propagating radix carries to output the exact 2n-bit product.
  Shown as: The multiplication algorithm *<predicate>* Exact recovery by rounding and carries

## Pages that build on this one

- Complete time bound: Dividing costs by the volume Tp, seven dominant terms with powers of p below one (margins g₁,…,g₇) show total time O(n (lg n)^{1−κ}); the smallest margin is 2κ.
- Sub-n-log-n integer multiplication: A single deterministic multitape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in this model.

## Other pages you may link to

- [Schönhage–Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hh-multiplier.md)
- [Arrays and elementary stream operations on tape](tape-stream-operations.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Bank-exchange network with restored scratch wires](exchange-network.md)
- [Frames on network wires](frames.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Strict rank saving](rank-saving.md)
- [Lower-triangular factorization of a matrix](matrix-factorization.md)
- [Cost of a matrix shear on address fields](matrix-shear.md)
- [Power-width chunk interchange](power-width-interchange.md)
- [Address chunk interchange](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Contractions and error accumulation](contraction-error.md)
- [Exact dyadic intermediates with one truncation](guard-bits.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-two recursion](fft-butterfly.md)
- [Phase frames and the two-point kernel C](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Stored bit-reversed frequency order](bit-reversed-order.md)
- [Transform layout and cost](transform-layout.md)
- [Prime axis lengths near powers of two](prime-axis-lengths.md)
- [Complete time bound](time-bound.md)
- [Sub-n-log-n integer multiplication](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The source-transform procedures now supply the three transforms needed for the radix-digit convolution." (paper)

  > The source-transform procedures now supply the three transforms needed for the radix-digit convolution. Read each stored operand backward from its least significant end in groups of $b$ bits. This produces the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order. Buffer each group on a fixed work tape and read it back most significant bit first, reversing its least-significant-first input order; pad the final short group with leading zeroes. For digit $a_j$, write the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero $w_{\rm c}$-bit imaginary word. This exponent is nonnegative because $p=6b$, and the represented value is exactly $a_j2^{-b-2}$. Append $S-q$ zero coefficient records. Buffering and ordering the groups costs $O(n)$, including the one partial group's padding, and writing the $S$ records costs $O(Sp)$. Together with the initial count and copies, this input conversion costs $O(n+Sp)=O(Tp)$; all $n$ input bits, including leading zeroes, are retained before the final group is padded.

- "Apply the coefficient-address map $\Phi$, with its padded layout, to obtain" (paper)

  > With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ ex


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

Write the body to `exegenius/tasks/0040-write-multiplication-algorithm.answer.md` and the JSON to `exegenius/tasks/0040-write-multiplication-algorithm.answer.json`, then run `exegenius submit 0040-write-multiplication-algorithm` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0040-write-multiplication-algorithm`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
