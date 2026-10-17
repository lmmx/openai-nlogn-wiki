# exegenius task 0036-write-ring-convolution

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
- Butterflies and the fast transform
- Multidimensional transforms
- Chinese-remainder address map (also: Agarwal–Cooley map)
- Gaussian resampling
- Bluestein chirp identity
- Retained permutation cancellation
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Retained frequency order
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records
- Error tracking and exact recovery
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
- Recursive power saving
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Fast address-chunk interchange (also: chunk swap, tape interchange)
- Two-point kernel C (also: phase network kernel)
- Binary phase frames
- Packed selected-bit addition
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Tape layout for synthetic transforms
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

Concept: Convolution from the retained transform layout
Gloss: Convolution over the ring modulo y^r + 1 on the remaining axes by two forward synthetic transforms, pointwise polynomial products and the opposite transform, normalized by 1/(rM).

## This page in the argument

The step: Normalized cyclic convolution over the polynomial ring $\mathbb C[y]/(y^r+1)$ on the remaining $d-1$ axes is computed from two forward synthetic transforms in retained order, $M$ pointwise polynomial products and the opposite transform, in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ time with error less than $\sqrt2\,M(3\ell+1)2^{-p}$.
How: Convolve by transform, pointwise product, inverse transform, using the established $O(N\log N)$ multiplier as an ordinary subroutine for the polynomial products via signed Kronecker substitution, and keep the transforms' frequency order between the forward and opposite passes.
Why: Pointwise multiplication commutes with applying the same record permutation to both operands, so the product can be formed in the retained order and handed directly to the opposite procedure. (the sources say so: "Pointwise multiplication commutes with applying the same record" (paper))

Its sub-steps, in order:

- For disk-grid polynomials $f,g\in\mathcal R_r$ the exact Gaussian-integer numerators of $fg$, and then $Q_p(fg/r)$, are computed in $O(rp\log(rp))$ time using four integer products by the established multiplier at packing base $B_0=2^{4p}$. (on [Signed packing](signed-packing.md))
- Normalized convolution $\mathcal M_r(f,g)=f*g/(rM)=f*g/T$ on arrays over $\mathcal R_r$ is approximated with error less than $\sqrt2\,M(3\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ time.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.2). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.2**: Normalized convolution $\mathcal M_r(f,g)=f*g/(rM)=f*g/T$ on arrays over $\mathcal R_r$ is approximated with error less than $\sqrt2\,M(3\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ time.
How: Do both forward transforms keeping their common $LB$ order, multiply the $M$ pairs of polynomial records pointwise by signed packing, apply the opposite transform to that order, and scale exactly by $M$; check the normalization from $F^-(f*g)=M(F^-f)(F^-g)$ and add the errors of the three transforms and one truncation.
- S3.2.1: For arrays over $\mathcal R_r$ define $\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}$.
  Source: "\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}." (paper)
  > For arrays on $\prod_i\mathbb Z/t_i\mathbb Z$ with values in $\mathcal R_r$, let $*$ denote cyclic convolution in the displayed axes and define \[ \mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}. \] For a fixed output coefficient, each of the $M$ first cyclic addresses determines one second address, and each of the $r$ first polynomial indices determines one second index modulo $r$. The negacyclic wrap supplies the sign. Thus that coefficient averages $rM$ signed scalar products, and $\mathcal M_r$ is a bilinear contraction: \[ \|\mathcal M_r(f,g)\|_\infty \leq\|f\|_\infty\|g\|_\infty. \] If the other operand is a disk array, replacing one operand changes the output by at most the norm distance between its two values.
- S3.2.2: A fixed output coefficient averages $rM$ signed scalar products (one second address per first address, one second index modulo $r$ with the negacyclic sign), so $\mathcal M_r$ is a bilinear contraction.
  Source: "$rM$ signed scalar products, and $\mathcal M_r$ is a bilinear" (paper)
  > For arrays on $\prod_i\mathbb Z/t_i\mathbb Z$ with values in $\mathcal R_r$, let $*$ denote cyclic convolution in the displayed axes and define \[ \mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}. \] For a fixed output coefficient, each of the $M$ first cyclic addresses determines one second address, and each of the $r$ first polynomial indices determines one second index modulo $r$. The negacyclic wrap supplies the sign. Thus that coefficient averages $rM$ signed scalar products, and $\mathcal M_r$ is a bilinear contraction: \[ \|\mathcal M_r(f,g)\|_\infty \leq\|f\|_\infty\|g\|_\infty. \] If the other operand is a disk array, replacing one operand changes the output by at most the norm distance between its two values.
- S3.2.3: Perform both forward transforms and retain their common $LB$ order, multiply pairs of polynomial records by the product lemma, apply the opposite procedure, and multiply by $M=T/r$.
  Source: "Perform both forward transforms and retain their common $LB$ order." (paper)
  > \begin{proposition}[Convolution from the retained transform layout] \label{prop:synthetic-convolution} Under the hypotheses of Lemma~\ref{lem:synthetic-transform-cost}, $\mathcal M_r$ on disk grid operands has an approximation with error less than \begin{equation} \sqrt2\,M(3\ell+1)2^{-p} \label{eq:synthetic-convolution-error} \end{equation} and cost \[ O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'} +\log(rp)\right]\right). \] Put $m_M=\log_2M$ and $w_M=w+m_M$. The returned grid array is in the original array and coefficient order, with the same two's-complement component format at width $w_M$. The procedure supplies $\Gamma(w_M)$ on the output descriptor tape, so the caller knows every component boundary from this width and the retained shape parameters. If one operand has norm at most $\rho<1$ and the bound in \eqref{eq:synthetic-convolution-error} is at most $1-\rho$, the returned grid array is a disk array. \end{proposition} \begin{proof} Perform both forward transforms and retain their common $LB$ order. Pass the supplied $p,r,w$ to Lemma~\ref{lem:signed-ring-product} for corresponding polynomial records. Its output keeps that record order and uses the component format required by the opposite procedure. Apply the opposite procedure to that order, and multiply its result exactly by $M=T/r$.
- S3.2.4: Expansion of the finite sums gives $F_{\boldsymbol t}^-(f*g)=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)$.
  Source: "=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)." (paper)
  > To check normalization, expansion of the finite sums gives \[ F_{\boldsymbol t}^-(f*g) =M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g). \] As $F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$, it follows that \[ M F_{\boldsymbol t}^+ \left(\frac{(F_{\boldsymbol t}^-f) (F_{\boldsymbol t}^-g)}r\right) =\frac{f*g}{rM}. \] Let $P(u,v)$ denote the exact pointwise product $uv/r$, and put $\mathcal T_+=F_{\boldsymbol t}^+B^{-1}L^{-1}$. Since $LB$ permutes records and leaves their polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$. Thus $\mathcal T_+$ applied to the pointwise product of the exact stored forward outputs equals $F_{\boldsymbol t}^+P(F_{\boldsymbol t}^-f,F_{\boldsymbol t}^-g)$. The displayed normalization identity identifies its exact scaling by $M$ with $\mathcal M_r(f,g)$.
- S3.2.5: With $F^+F^-=I/M$ it follows that $MF^+_{\boldsymbol t}\bigl((F^-f)(F^-g)/r\bigr)=f*g/(rM)$.
  Source: "M F_{\boldsymbol t}^+" (paper)
  > To check normalization, expansion of the finite sums gives \[ F_{\boldsymbol t}^-(f*g) =M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g). \] As $F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$, it follows that \[ M F_{\boldsymbol t}^+ \left(\frac{(F_{\boldsymbol t}^-f) (F_{\boldsymbol t}^-g)}r\right) =\frac{f*g}{rM}. \] Let $P(u,v)$ denote the exact pointwise product $uv/r$, and put $\mathcal T_+=F_{\boldsymbol t}^+B^{-1}L^{-1}$. Since $LB$ permutes records and leaves their polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$. Thus $\mathcal T_+$ applied to the pointwise product of the exact stored forward outputs equals $F_{\boldsymbol t}^+P(F_{\boldsymbol t}^-f,F_{\boldsymbol t}^-g)$. The displayed normalization identity identifies its exact scaling by $M$ with $\mathcal M_r(f,g)$.
- S3.2.6: Since $LB$ permutes records and leaves polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$, so the opposite transform applied to the pointwise product of the stored forward outputs equals $F^+P(F^-f,F^-g)$.
  Source: "intact, $P(LBu,LBv)=LBP(u,v)$.  Thus $\mathcal T_+$ applied to the" (paper)
  > To check normalization, expansion of the finite sums gives \[ F_{\boldsymbol t}^-(f*g) =M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g). \] As $F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$, it follows that \[ M F_{\boldsymbol t}^+ \left(\frac{(F_{\boldsymbol t}^-f) (F_{\boldsymbol t}^-g)}r\right) =\frac{f*g}{rM}. \] Let $P(u,v)$ denote the exact pointwise product $uv/r$, and put $\mathcal T_+=F_{\boldsymbol t}^+B^{-1}L^{-1}$. Since $LB$ permutes records and leaves their polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$. Thus $\mathcal T_+$ applied to the pointwise product of the exact stored forward outputs equals $F_{\boldsymbol t}^+P(F_{\boldsymbol t}^-f,F_{\boldsymbol t}^-g)$. The displayed normalization identity identifies its exact scaling by $M$ with $\mathcal M_r(f,g)$.
- S3.2.7: Put $\delta=\sqrt2\ell\,2^{-p}$ for each forward transform error and $\eta=\sqrt2\,2^{-p}$ for one truncation.
  Source: "$\delta=\sqrt2\ell\,2^{-p}$ and $\eta=\sqrt2\,2^{-p}$." (paper)
  > For the error estimate, put $\delta=\sqrt2\ell\,2^{-p}$ and $\eta=\sqrt2\,2^{-p}$. Let $u,v$ be the exact stored forward outputs and $\widetilde u,\widetilde v$ the returned ones. All four are disk arrays, and each forward error is less than $\delta$. The exact map $P$ is bilinear and satisfies $\|P(x,y)\|_\infty\leq\|x\|_\infty\|y\|_\infty$ by the coefficient bound in Lemma~\ref{lem:signed-ring-product}. Hence \[ \begin{split} P(\widetilde u,\widetilde v)-P(u,v) &=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v),\\ \|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty &<2\delta, \end{split} \] where the first term uses the disk bound on $\widetilde v$ and the second uses it on $u$. Write $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$. The product lemma makes $\widetilde z$ a disk grid array and gives $\|\widetilde z-z_*\|_\infty<2\delta+\eta$. If $\widetilde h$ is the returned opposite output, its approximation bound applies to $\widetilde z$. Since $\mathcal T_+$ is a contraction, \[ \|\widetilde h-\mathcal T_+ z_*\|_\infty \leq\|\widetilde h-\mathcal T_+\widetilde z\|_\infty +\|\mathcal T_+(\widetilde z-z_*)\|_\infty <3\delta+\eta. \] The final exact multiplication by $M$ therefore gives error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed. If one original operand has norm at most $\rho$, then $\|\mathcal M_r(f,g)\|_\infty\leq\rho$. Under the stated error margin, the returned norm is less than $\rho+(1-\rho)=1$.
- S3.2.8: By bilinearity of the pointwise product and the disk bound on both operands, $\|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty<2\delta$.
  Source: "&<2\delta," (paper)
  > For the error estimate, put $\delta=\sqrt2\ell\,2^{-p}$ and $\eta=\sqrt2\,2^{-p}$. Let $u,v$ be the exact stored forward outputs and $\widetilde u,\widetilde v$ the returned ones. All four are disk arrays, and each forward error is less than $\delta$. The exact map $P$ is bilinear and satisfies $\|P(x,y)\|_\infty\leq\|x\|_\infty\|y\|_\infty$ by the coefficient bound in Lemma~\ref{lem:signed-ring-product}. Hence \[ \begin{split} P(\widetilde u,\widetilde v)-P(u,v) &=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v),\\ \|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty &<2\delta, \end{split} \] where the first term uses the disk bound on $\widetilde v$ and the second uses it on $u$. Write $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$. The product lemma makes $\widetilde z$ a disk grid array and gives $\|\widetilde z-z_*\|_\infty<2\delta+\eta$. If $\widetilde h$ is the returned opposite output, its approximation bound applies to $\widetilde z$. Since $\mathcal T_+$ is a contraction, \[ \|\widetilde h-\mathcal T_+ z_*\|_\infty \leq\|\widetilde h-\mathcal T_+\widetilde z\|_\infty +\|\mathcal T_+(\widetilde z-z_*)\|_\infty <3\delta+\eta. \] The final exact multiplication by $M$ therefore gives error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed. If one original operand has norm at most $\rho$, then $\|\mathcal M_r(f,g)\|_\infty\leq\rho$. Under the stated error margin, the returned norm is less than $\rho+(1-\rho)=1$.
- S3.2.9: After truncation, $\|\widetilde z-z_*\|_\infty<2\delta+\eta$.
  Source: "$\|\widetilde z-z_*\|_\infty<2\delta+\eta$." (paper)
  > For the error estimate, put $\delta=\sqrt2\ell\,2^{-p}$ and $\eta=\sqrt2\,2^{-p}$. Let $u,v$ be the exact stored forward outputs and $\widetilde u,\widetilde v$ the returned ones. All four are disk arrays, and each forward error is less than $\delta$. The exact map $P$ is bilinear and satisfies $\|P(x,y)\|_\infty\leq\|x\|_\infty\|y\|_\infty$ by the coefficient bound in Lemma~\ref{lem:signed-ring-product}. Hence \[ \begin{split} P(\widetilde u,\widetilde v)-P(u,v) &=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v),\\ \|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty &<2\delta, \end{split} \] where the first term uses the disk bound on $\widetilde v$ and the second uses it on $u$. Write $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$. The product lemma makes $\widetilde z$ a disk grid array and gives $\|\widetilde z-z_*\|_\infty<2\delta+\eta$. If $\widetilde h$ is the returned opposite output, its approximation bound applies to $\widetilde z$. Since $\mathcal T_+$ is a contraction, \[ \|\widetilde h-\mathcal T_+ z_*\|_\infty \leq\|\widetilde h-\mathcal T_+\widetilde z\|_\infty +\|\mathcal T_+(\widetilde z-z_*)\|_\infty <3\delta+\eta. \] The final exact multiplication by $M$ therefore gives error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed. If one original operand has norm at most $\rho$, then $\|\mathcal M_r(f,g)\|_\infty\leq\rho$. Under the stated error margin, the returned norm is less than $\rho+(1-\rho)=1$.
- S3.2.10: Since the opposite transform $\mathcal T_+$ is a contraction with its own error $\delta$, the output error is less than $3\delta+\eta$.
  Source: "<3\delta+\eta." (paper)
  > For the error estimate, put $\delta=\sqrt2\ell\,2^{-p}$ and $\eta=\sqrt2\,2^{-p}$. Let $u,v$ be the exact stored forward outputs and $\widetilde u,\widetilde v$ the returned ones. All four are disk arrays, and each forward error is less than $\delta$. The exact map $P$ is bilinear and satisfies $\|P(x,y)\|_\infty\leq\|x\|_\infty\|y\|_\infty$ by the coefficient bound in Lemma~\ref{lem:signed-ring-product}. Hence \[ \begin{split} P(\widetilde u,\widetilde v)-P(u,v) &=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v),\\ \|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty &<2\delta, \end{split} \] where the first term uses the disk bound on $\widetilde v$ and the second uses it on $u$. Write $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$. The product lemma makes $\widetilde z$ a disk grid array and gives $\|\widetilde z-z_*\|_\infty<2\delta+\eta$. If $\widetilde h$ is the returned opposite output, its approximation bound applies to $\widetilde z$. Since $\mathcal T_+$ is a contraction, \[ \|\widetilde h-\mathcal T_+ z_*\|_\infty \leq\|\widetilde h-\mathcal T_+\widetilde z\|_\infty +\|\mathcal T_+(\widetilde z-z_*)\|_\infty <3\delta+\eta. \] The final exact multiplication by $M$ therefore gives error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed. If one original operand has norm at most $\rho$, then $\|\mathcal M_r(f,g)\|_\infty\leq\rho$. Under the stated error margin, the returned norm is less than $\rho+(1-\rho)=1$.
- S3.2.11: The exact multiplication by $M$ gives total error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$.
  Source: "$M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed." (paper)
  > For the error estimate, put $\delta=\sqrt2\ell\,2^{-p}$ and $\eta=\sqrt2\,2^{-p}$. Let $u,v$ be the exact stored forward outputs and $\widetilde u,\widetilde v$ the returned ones. All four are disk arrays, and each forward error is less than $\delta$. The exact map $P$ is bilinear and satisfies $\|P(x,y)\|_\infty\leq\|x\|_\infty\|y\|_\infty$ by the coefficient bound in Lemma~\ref{lem:signed-ring-product}. Hence \[ \begin{split} P(\widetilde u,\widetilde v)-P(u,v) &=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v),\\ \|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty &<2\delta, \end{split} \] where the first term uses the disk bound on $\widetilde v$ and the second uses it on $u$. Write $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$. The product lemma makes $\widetilde z$ a disk grid array and gives $\|\widetilde z-z_*\|_\infty<2\delta+\eta$. If $\widetilde h$ is the returned opposite output, its approximation bound applies to $\widetilde z$. Since $\mathcal T_+$ is a contraction, \[ \|\widetilde h-\mathcal T_+ z_*\|_\infty \leq\|\widetilde h-\mathcal T_+\widetilde z\|_\infty +\|\mathcal T_+(\widetilde z-z_*)\|_\infty <3\delta+\eta. \] The final exact multiplication by $M$ therefore gives error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed. If one original operand has norm at most $\rho$, then $\|\mathcal M_r(f,g)\|_\infty\leq\rho$. Under the stated error margin, the returned norm is less than $\rho+(1-\rho)=1$.
- S3.2.12: There are $M=T/r$ pointwise polynomial products, with total cost $O(Tp\log(rp))$; the three transform costs are as stated and the final scaling is linear.
  Source: "There are $M=T/r$ pointwise polynomial products.  Their total cost" (paper)
  > There are $M=T/r$ pointwise polynomial products. Their total cost is $O(Tp\log(rp))$; the three transform costs are as stated, and the last exact scaling is linear in $Tp$. All data movement uses the previously specified scans, swaps, and layout restoration. \end{proof} \section{Resampling with the permutations left in the transform} \label{sec:resampling}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S3.1 (on [Signed packing](signed-packing.md)): For disk-grid polynomials $f,g\in\mathcal R_r$ the exact Gaussian-integer numerators of $fg$, and then $Q_p(fg/r)$, are computed in $O(rp\log(rp))$ time using four integer products by the established multiplier at packing base $B_0=2^{4p}$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Cyclic convolution](convolution.md)
- [Discrete Fourier transform](dft.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Tape layout for synthetic transforms](transform-layout.md): Placing the selected bits of the participating axes at a common offset in K-bit chunks so each round of the synthetic transform is one simultaneous layer, costing less than log t passes.
  Shown as: Convolution from the retained transform layout *<predicate>* Tape layout for synthetic transforms
- [Signed packing](signed-packing.md): A signed Kronecker substitution that evaluates polynomials with signed coefficients at 2^{4p} to form large integers, multiplies them with the O(n log n) multiplier, and recovers the product coefficients.
  Shown as: Convolution from the retained transform layout *<predicate>* Signed packing
- [Retained frequency order](frequency-order.md): The forward synthetic transform writes its outputs in bit-reversed order, the pointwise product keeps that order, and the opposite transform consumes it, so no reordering is executed.
  Shown as: Convolution from the retained transform layout *<predicate>* Retained frequency order

## Pages that build on this one

- The multiplication algorithm: Digits, then the CRT map, two forward transforms with resampling and chirps, a pointwise product, the opposite transform, rescaling, rounding and carry propagation yield the exact 2n-bit product.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Elementary stream operations](stream-ops.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
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
- [Two-point kernel C](phase-kernel.md)
- [Binary phase frames](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "Convolution from the retained transform layout" (paper)

  > \begin{proposition}[Convolution from the retained transform layout] \label{prop:synthetic-convolution} Under the hypotheses of Lemma~\ref{lem:synthetic-transform-cost}, $\mathcal M_r$ on disk grid operands has an approximation with error less than \begin{equation} \sqrt2\,M(3\ell+1)2^{-p} \label{eq:synthetic-convolution-error} \end{equation} and cost \[ O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'} +\log(rp)\right]\right). \] Put $m_M=\log_2M$ and $w_M=w+m_M$. The returned grid array is in the original array and coefficient order, with the same two's-complement component format at width $w_M$. The procedure supplies $\Gamma(w_M)$ on the output descriptor tape, so the caller knows every component boundary from this width and the retained shape parameters. If one operand has norm at most $\rho<1$ and the bound in \eqref{eq:synthetic-convolution-error} is at most $1-\rho$, the returned grid array is a disk array. \end{proposition} \begin{proof} Perform both forward transforms and retain their common $LB$ order. Pass the supplied $p,r,w$ to Lemma~\ref{lem:signed-ring-product} for corresponding polynomial records. Its output keeps that record order and uses the component format required by the opposite procedure. Apply the opposite procedure to that order, and multiply its result exactly by $M=T/r$.

- "The normalized convolution interface" (paper)

  > \subsection{The normalized convolution interface}


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

Write the body to `exegenius/tasks/0036-write-ring-convolution.answer.md` and the JSON to `exegenius/tasks/0036-write-ring-convolution.answer.json`, then run `exegenius submit 0036-write-ring-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0036-write-ring-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
