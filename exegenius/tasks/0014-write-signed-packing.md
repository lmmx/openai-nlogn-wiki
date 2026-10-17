# exegenius task 0014-write-signed-packing

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
- Schönhage–Strassen optimality conjecture (also: n log n conjecture)
- Established O(n log n) multiplier
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Fixed-point Gaussian dyadic records
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
- Recursive power saving
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
- Cartesian products and multi-index arrays (also: multidimensional arrays, row-major order, lexicographic order, mixed-radix index, index tuples, array stored on a tape)
- Directed acyclic graphs and networks of gates (also: circuit, DAG, wire, gate, edges and vertices, fan-in)
- Summation, geometric series and induction (also: geometric sum, proof by induction, summation notation, telescoping sum)
- Rounding to the nearest integer and exactness (also: rounding, truncation, round to nearest, rational numbers, dyadic rational)
- Multitape Turing machine running time (also: tape head movement, scanning a tape, linear-time pass over a tape, time complexity of a Turing machine, worst-case running time)
- Integer exponentials and tuple notation (also: powers of two, tensor power notation, exponent of a constant, fixed rational exponents)

## This page

Concept: Signed packing
Gloss: A signed Kronecker substitution that evaluates polynomials with signed coefficients at 2^{4p} to form large integers, multiplies them with the O(n log n) multiplier, and recovers the product coefficients.
Also called: Kronecker substitution

## This page in the argument

The step: For disk-grid polynomials $f,g\in\mathcal R_r$ the exact Gaussian-integer numerators of $fg$, and then $Q_p(fg/r)$, are computed in $O(rp\log(rp))$ time using four integer products by the established multiplier at packing base $B_0=2^{4p}$.
How: Use signed Kronecker substitution: evaluate the integer-coefficient polynomials at $B_0=2^{4p}$ to signed integers of $4pr$ bits, multiply the four pairs (real/imaginary parts), recover coefficients by centered residues modulo $B_0$ with a carry, and reduce modulo $y^r+1$.
Why: The ordinary polynomial product has coefficients of size at most $r2^{2p}<2^{3p}<B_0/2$, so evaluating at $B_0=2^{4p}$ keeps coefficient blocks separated and each is the unique centered residue modulo $B_0$ once lower blocks are removed. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Write $f=2^{-p}(a+ib)$, $g=2^{-p}(c+ie)$ with integer-coefficient polynomials of degree below $r$ and coefficients of absolute value at most $2^p$; set $B_0=2^{4p}$.
- Each evaluation satisfies $|A_u|\le2^p(B_0^r-1)/(B_0-1)<B_0^r/2$, so its magnitude fits in $4pr$ bits.
- Multiply the four pairs of absolute values by the established multiplier and restore each sign, obtaining $A_aA_c,A_bA_e,A_aA_e,A_bA_c$; each is $(ac)(B_0)=\sum_jh_jB_0^j$ etc.
- Every coefficient of any ordinary product satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so after removing lower coefficients the next is identified by its centered residue modulo $B_0$.
- Forming $A_u$ from signed coefficients: the carry stays in $\{-1,0\}$ because $-B_0<u_j+\gamma_j<B_0$, giving a fixed-width two's-complement encoding.
- Extraction: $\widehat h_j$ is the unique integer in $[-B_0/2,B_0/2)$ congruent to $q_j+\rho_j$ modulo $B_0$, with carry $\rho_{j+1}\in\{0,1\}$; by the separation bound $\widehat h_j=h_j$.
- The real and imaginary numerator streams are $ac-be$ and $ae+bc$; reduce modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$.
- Each resulting Gaussian integer coefficient $H_j$ is a sum of exactly $r$ signed products of coefficients of modulus at most $2^p$, so $|H_j|\le r2^{2p}$; the normalized product $fg/r$ of disk polynomials lies in the disk.
- Four exact integer products dominate the linear packing, extraction, combination, wrapping and truncation costs, giving $O(rp\log(rp))$ with error less than $\sqrt2\,2^{-p}$ from $fg/r$.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- Normalized cyclic convolution over the polynomial ring $\mathbb C[y]/(y^r+1)$ on the remaining $d-1$ axes is computed from two forward synthetic transforms in retained order, $M$ pointwise polynomial products and the opposite transform, in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ time with error less than $\sqrt2\,M(3\ell+1)2^{-p}$.; how: Convolve by transform, pointwise product, inverse transform, using the established $O(N\log N)$ multiplier as an ordinary subroutine for the polynomial products via signed Kronecker substitution, and keep the transforms' frequency order between the forward and opposite passes. (on [Convolution from the retained transform layout](ring-convolution.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.1.1, S3.1.2, S3.1.3, S3.1.4, S3.1.5, S3.1.6, S3.1.7, S3.1.8, S3.1.9). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.1.1**: Write $f=2^{-p}(a+ib)$, $g=2^{-p}(c+ie)$ with integer-coefficient polynomials of degree below $r$ and coefficients of absolute value at most $2^p$; set $B_0=2^{4p}$.
Source: "and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer" (paper)
> p+2\leq w\leq C_wp$. The input supplies $\Gamma(p)\Gamma(r)\Gamma(w)$ and two disk grid polynomials $f,g\in\mathcal R_r$ in the component format of Proposition~\ref{prop:simultaneous-layer} with width $w$. One can compute the exact Gaussian integer numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\log(rp))$ on a fixed number of tapes. The output is a disk grid polynomial with error less than $\sqrt2\,2^{-p}$ from $fg/r$. \end{lemma} \begin{proof} The supplied power of two $r$ determines $\ell=\log_2r$. Write \[ f=2^{-p}(a+ib),\qquad g=2^{-p}(c+ie), \] where $a,b,c,e\in\mathbb Z[y]$ have degree less than $r$ and coefficients of absolute value at most $2^p$. Set $B_0=2^{4p}$ and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values using the established multiplier and restore each product's sign. The resulting integers are $A_aA_c,A_bA_e,A_aA_e,A_bA_c$. For example, if $h=ac$ is the ordinary product in $\mathbb Z[y]$, then \[ A_aA_c=(ac)(B_0)=\sum_{j=0}^{2r-2}h_jB_0^j. \] The other three evaluation products have the same form. Every coefficient in any of these ordinary polynomial products satisfies \begin{equation} |h_j|\leq r2^{2p}<2^{3p}<B_0/2. \label{eq:packing-separation} \end{equation} After the lower coefficients have

**S3.1.2**: Each evaluation satisfies $|A_u|\le2^p(B_0^r-1)/(B_0-1)<B_0^r/2$, so its magnitude fits in $4pr$ bits.
Source: "|A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2" (paper)
> r$ in the component format of Proposition~\ref{prop:simultaneous-layer} with width $w$. One can compute the exact Gaussian integer numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\log(rp))$ on a fixed number of tapes. The output is a disk grid polynomial with error less than $\sqrt2\,2^{-p}$ from $fg/r$. \end{lemma} \begin{proof} The supplied power of two $r$ determines $\ell=\log_2r$. Write \[ f=2^{-p}(a+ib),\qquad g=2^{-p}(c+ie), \] where $a,b,c,e\in\mathbb Z[y]$ have degree less than $r$ and coefficients of absolute value at most $2^p$. Set $B_0=2^{4p}$ and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values using the established multiplier and restore each product's sign. The resulting integers are $A_aA_c,A_bA_e,A_aA_e,A_bA_c$. For example, if $h=ac$ is the ordinary product in $\mathbb Z[y]$, then \[ A_aA_c=(ac)(B_0)=\sum_{j=0}^{2r-2}h_jB_0^j. \] The other three evaluation products have the same form. Every coefficient in any of these ordinary polynomial products satisfies \begin{equation} |h_j|\leq r2^{2p}<2^{3p}<B_0/2. \label{eq:packing-separation} \end{equation} After the lower coefficients have been removed from an evaluation, this strict bound identifies the next coefficient by its centered residue modulo $B

**S3.1.3**: Multiply the four pairs of absolute values by the established multiplier and restore each sign, obtaining $A_aA_c,A_bA_e,A_aA_e,A_bA_c$; each is $(ac)(B_0)=\sum_jh_jB_0^j$ etc.
Source: "pairs of absolute values using the established multiplier and restore" (paper)
> nteger numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\log(rp))$ on a fixed number of tapes. The output is a disk grid polynomial with error less than $\sqrt2\,2^{-p}$ from $fg/r$. \end{lemma} \begin{proof} The supplied power of two $r$ determines $\ell=\log_2r$. Write \[ f=2^{-p}(a+ib),\qquad g=2^{-p}(c+ie), \] where $a,b,c,e\in\mathbb Z[y]$ have degree less than $r$ and coefficients of absolute value at most $2^p$. Set $B_0=2^{4p}$ and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values using the established multiplier and restore each product's sign. The resulting integers are $A_aA_c,A_bA_e,A_aA_e,A_bA_c$. For example, if $h=ac$ is the ordinary product in $\mathbb Z[y]$, then \[ A_aA_c=(ac)(B_0)=\sum_{j=0}^{2r-2}h_jB_0^j. \] The other three evaluation products have the same form. Every coefficient in any of these ordinary polynomial products satisfies \begin{equation} |h_j|\leq r2^{2p}<2^{3p}<B_0/2. \label{eq:packing-separation} \end{equation} After the lower coefficients have been removed from an evaluation, this strict bound identifies the next coefficient by its centered residue modulo $B_0$.

**S3.1.4**: Every coefficient of any ordinary product satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so after removing lower coefficients the next is identified by its centered residue modulo $B_0$.
Source: "|h_j|\leq r2^{2p}<2^{3p}<B_0/2." (paper)
> oefficients of absolute value at most $2^p$. Set $B_0=2^{4p}$ and, for $u\in\{a,b,c,e\}$, define the signed evaluation integer \[ A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j. \] The bound \[ |A_u|\leq2^p\frac{B_0^r-1}{B_0-1}<B_0^r/2 \] shows that each magnitude fits in $4pr$ bits. Multiply the four pairs of absolute values using the established multiplier and restore each product's sign. The resulting integers are $A_aA_c,A_bA_e,A_aA_e,A_bA_c$. For example, if $h=ac$ is the ordinary product in $\mathbb Z[y]$, then \[ A_aA_c=(ac)(B_0)=\sum_{j=0}^{2r-2}h_jB_0^j. \] The other three evaluation products have the same form. Every coefficient in any of these ordinary polynomial products satisfies \begin{equation} |h_j|\leq r2^{2p}<2^{3p}<B_0/2. \label{eq:packing-separation} \end{equation} After the lower coefficients have been removed from an evaluation, this strict bound identifies the next coefficient by its centered residue modulo $B_0$.

**S3.1.5**: Forming $A_u$ from signed coefficients: the carry stays in $\{-1,0\}$ because $-B_0<u_j+\gamma_j<B_0$, giving a fixed-width two's-complement encoding.
Source: "Since $-B_0<u_j+\gamma_j<B_0$ whenever" (paper)
> To form $A_u$, start with carry $\gamma_0=0$ and write \[ d_j\equiv u_j+\gamma_j\pmod{B_0},\quad 0\leq d_j<B_0, \qquad \gamma_{j+1}=\frac{u_j+\gamma_j-d_j}{B_0}. \] Since $-B_0<u_j+\gamma_j<B_0$ whenever $\gamma_j\in\{-1,0\}$, the carry stays in $\{-1,0\}$. Telescoping the recurrence gives \[ A_u=\sum_{j=0}^{r-1}d_jB_0^j+\gamma_rB_0^r. \] The $r$ blocks are therefore a fixed-width two's-complement encoding of $A_u$, with $\gamma_r=-1$ exactly when $A_u<0$. In that case complement and increment the blocks to obtain $|A_u|$; otherwise retain them. Every block has $4p$ bits and every carry has constant size, so a constant number of scans costs $O(rp)$. Endianness changes required by the multiplier are linear-time reversals on a work tape.

**S3.1.6**: Extraction: $\widehat h_j$ is the unique integer in $[-B_0/2,B_0/2)$ congruent to $q_j+\rho_j$ modulo $B_0$, with carry $\rho_{j+1}\in\{0,1\}$; by the separation bound $\widehat h_j=h_j$.
Source: "integer in $[-B_0/2,B_0/2)$ congruent to $q_j+\rho_j$ modulo $B_0$," (paper)
> Now let $Z$ be one of the four signed product integers, and let $h$ be its corresponding ordinary polynomial product. Put $J=2r$ and pad that product by $h_{J-1}=0$. The bound on the evaluation integers gives $|Z|<B_0^J/4$, so $Z$ fits in $J$ blocks of width $4p$. Convert its sign and magnitude to sign-extended two's complement: \[ Z=\sum_{j=0}^{J-1}q_jB_0^j+\varepsilon B_0^J, \qquad 0\leq q_j<B_0,\quad \varepsilon\in\{-1,0\}. \] Zero-fill the unused high blocks; for a negative sign, complement and increment within this fixed width. These conversions take a constant number of scans. Put $\rho_0=0$. At block $j$, let $\widehat h_j$ be the unique integer in $[-B_0/2,B_0/2)$ congruent to $q_j+\rho_j$ modulo $B_0$, and put \[ \rho_{j+1}= \frac{q_j+\rho_j-\widehat h_j}{B_0}. \] The carry belongs to $\{0,1\}$: if $\rho_j$ has this property, then $0\leq q_j+\rho_j\leq B_0$, and centering either leaves this value unchanged or subtracts $B_0$.

**S3.1.7**: The real and imaginary numerator streams are $ac-be$ and $ae+bc$; reduce modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$.
Source: "The real and imaginary numerator streams are respectively" (paper)
> The real and imaginary numerator streams are respectively $ac-be$ and $ae+bc$. To reduce them modulo $y^r+1$, subtract the coefficient at $j+r$ from the one at $j$ for $0\leq j<r$, treating a missing coefficient as zero. Splitting the two halves to tapes aligns these terms in one further scan. For each first input index $j_1\in\{0,\ldots,r-1\}$, exactly one second index $j_2$ in that range satisfies $j_1+j_2\equiv j\pmod r$. Its sign is positive when $j_1+j_2=j$ and negative when $j_1+j_2=j+r$. Thus each resulting Gaussian integer coefficient $H_j$ is a sum of exactly $r$ signed products of Gaussian integer input coefficients of modulus at most $2^p$. Consequently \[ |H_j|\leq r2^{2p}. \] The same triangle inequality before imposing the disk bound gives $\|fg/r\|_\infty\leq\|f\|_\infty\|g\|_\infty$; in particular the normalized product of disk polynomials lies in the disk. All intermediate coefficient additions fit in $O(p)$ bits. The width-$4p$ packing fields and the exact multiplier output prevent overflow or ambiguity between adjacent fields.

**S3.1.8**: Each resulting Gaussian integer coefficient $H_j$ is a sum of exactly $r$ signed products of coefficients of modulus at most $2^p$, so $|H_j|\le r2^{2p}$; the normalized product $fg/r$ of disk polynomials lies in the disk.
Source: "|H_j|\leq r2^{2p}." (paper)
> The real and imaginary numerator streams are respectively $ac-be$ and $ae+bc$. To reduce them modulo $y^r+1$, subtract the coefficient at $j+r$ from the one at $j$ for $0\leq j<r$, treating a missing coefficient as zero. Splitting the two halves to tapes aligns these terms in one further scan. For each first input index $j_1\in\{0,\ldots,r-1\}$, exactly one second index $j_2$ in that range satisfies $j_1+j_2\equiv j\pmod r$. Its sign is positive when $j_1+j_2=j$ and negative when $j_1+j_2=j+r$. Thus each resulting Gaussian integer coefficient $H_j$ is a sum of exactly $r$ signed products of Gaussian integer input coefficients of modulus at most $2^p$. Consequently \[ |H_j|\leq r2^{2p}. \] The same triangle inequality before imposing the disk bound gives $\|fg/r\|_\infty\leq\|f\|_\infty\|g\|_\infty$; in particular the normalized product of disk polynomials lies in the disk. All intermediate coefficient additions fit in $O(p)$ bits. The width-$4p$ packing fields and the exact multiplier output prevent overflow or ambiguity between adjacent fields.

**S3.1.9**: Four exact integer products dominate the linear packing, extraction, combination, wrapping and truncation costs, giving $O(rp\log(rp))$ with error less than $\sqrt2\,2^{-p}$ from $fg/r$.
Source: "Four exact integer products dominate the linear" (paper)
> Finally the $p$-bit grid numerator of the normalized product is \[ \operatorname{trunc}_0\left(\frac{\Re H_j}{2^{p+\ell}}\right) +i\operatorname{trunc}_0\left(\frac{\Im H_j}{2^{p+\ell}}\right). \] To implement it, shift the absolute magnitude right by $p+\ell$ bits and restore its sign, at cost $O(p)$ per coefficient. The returned coefficient is $2^{-p}$ times this numerator, namely $Q_p(2^{-2p}H_j/r)$; \eqref{eq:transform-truncate} proves its error and disk bounds. Each returned component numerator has magnitude at most $2^p$, so write it as a signed $w$-bit two's-complement word, most significant bit first, with the real word before the imaginary word and coefficient indices in increasing order. This costs $O(rw)=O(rp)$ and supplies the format used by the opposite transform. Four exact integer products dominate the linear packing, extraction, combination, wrapping, and truncation costs. \end{proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Polynomial ring modulo y^r + 1](ring-y.md): Polynomials of degree below r over the complex numbers with y^r = −1, so multiplying by a power of y is a signed shift of the coefficient list.
  Shown as: Signed packing *<predicate>* Polynomial ring modulo y^r + 1
- [Established O(n log n) multiplier](hvdh-multiplier.md): The earlier Harvey–van der Hoeven multitape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine.
  Shown as: Signed packing *<predicate>* Established O(n log n) multiplier

## Pages that build on this one

- Convolution from the retained transform layout: Convolution over the ring modulo y^r + 1 on the remaining axes by two forward synthetic transforms, pointwise polynomial products and the opposite transform, normalized by 1/(rM).

## Other pages you may link to

- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Elementary stream operations](stream-ops.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Multidimensional transforms](multidim-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](chirp.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Retained frequency order](frequency-order.md)
- [Two-point kernel C](phase-kernel.md)
- [Binary phase frames](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "Signed coefficient" (paper)

  > More specifically, the proof adapts Harvey and van der Hoeven's Gaussian-resampling identity, contraction bounds, and short-convolution procedures~\cite[Theorem~4.2, Proposition~4.7 and Lemmas~4.8--4.12]{HarveyHoeven2021}. Their framework already permits arbitrary dimension. Here the source and target permutations remain in the transform identity, while the faster tape procedures perform the required axis movements. Bluestein's conversion to convolution~\cite{Bluestein1970} and the synthetic-root convolution algorithm are retained; the latter follows the polynomial-transform construction in~\cite[Section~2.4 and Section~3]{HarveyHoeven2021}. Signed coefficient packing is a form of Kronecker substitution, with the fixed-tape version of~\cite[Lemma~2.5]{HarveyHoeven2021} as a direct antecedent. Calls to the established $O(n\log n)$ multiplier are ordinary subroutine calls; they do not invoke the improved theorem recursively.

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

Write the body to `exegenius/tasks/0014-write-signed-packing.answer.md` and the JSON to `exegenius/tasks/0014-write-signed-packing.answer.json`, then run `exegenius submit 0014-write-signed-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0014-write-signed-packing`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
