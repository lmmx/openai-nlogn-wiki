# exegenius task 0383-write-ring-convolution

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
- Nested subspace labels and rank deficit (also: rank saving)
- Recursive power saving
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Fast address-chunk interchange (also: chunk swap, tape interchange, costly recursive primitive)
- Two-point kernel C (also: phase network kernel)
- Binary phase frames
- Packed selected-bit addition (also: exceptional addresses)
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Tape layout for synthetic transforms
- Parameter and prime-length choice
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
- Tensor products of subspaces (also: tensor product of subspaces, tensor product)

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
- $\tau$ (interchange exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent in the cost of a chunk interchange.
- $\sigma$ (growth exponent bound), bound on [Parameter and prime-length choice](parameter-choice.md): An exponent bounding the growth of recursive calls.
- $\beta$ (threshold exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent setting the threshold d^beta below which active chunks are handled singly.
- $\lambda$ (overhead exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The per-node overhead exponent.
- $\lambda'$ (final cost exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The final exponent of the layer cost V d^lambda' on bit volume V.
- $V$ (bit volume), bound on [Parameter and prime-length choice](parameter-choice.md): The bit volume of the data on which the layer acts.
- $c$ (chunk-width exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the address-chunk width; not the scaling integer of controlled shifts.
- $\epsilon$ (axis-count exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the axis count.
- $C_1$ (guard-bit exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the guard bits.
- $\delta$ (resampling slack), bound on [Parameter and prime-length choice](parameter-choice.md): The resampling-cost slack.
- $K$ (address-chunk width), bound on [Parameter and prime-length choice](parameter-choice.md): The width in bits of an address chunk, floor of d^c.
- $\eta$ (relative prime distance), bound on [Parameter and prime-length choice](parameter-choice.md): The smallest relative distance at which a prime s_i may lie below t_i.
- $q$ (interval integer), bound on [Parameter and prime-length choice](parameter-choice.md): An integer in the prime-interval lemma, not a radix or sequence length.
- $a_d$ (a_d constant), bound on [Parameter and prime-length choice](parameter-choice.md): Lower constant in the bound a_d p^epsilon <= d.
- $b_d$ (b_d constant), bound on [Parameter and prime-length choice](parameter-choice.md): Upper constant in the bound d <= b_d p^epsilon.
- $a_r$ (a_r constant), bound on [Parameter and prime-length choice](parameter-choice.md): Lower constant in the bound 2^(a_r p/d) <= r.
- $b_r$ (b_r constant), bound on [Parameter and prime-length choice](parameter-choice.md): Upper constant in the bound r <= 2^(b_r p/d).
- $C_\ell$ (C_ell constant), bound on [Parameter and prime-length choice](parameter-choice.md): Constant in the bound d ell <= C_ell p.
- $E$ (first space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The first of the two finite-dimensional vector spaces being tensored.
- $G$ (second space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The second of the two finite-dimensional vector spaces being tensored.
- $A$ (ambient space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A finite-dimensional space with a nondegenerate form, containing the subspace P.
- $C$ (second ambient space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A finite-dimensional space with a nondegenerate form, containing the subspace Q.
- $P$ (subspace of A), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A subspace of A, later taken nondegenerate.
- $Q$ (subspace of C), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A subspace of C.
- $B$ (orthogonal complement), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The orthogonal complement of P in A.
- $F$ (base space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A space of dimension h with a nondegenerate form, whose triple power is the label space.
- $s$ (number of smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total number of smaller calls that the edges of the network cost.
- $W$ (wire count), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of wires of the network under consideration.
- $U$ (a label subspace), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A subspace of the label space, such as the label of a vertex.
- $F$ (one-factor label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
- $x$ (vector of F), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A vector of $F$, the first argument of the bilinear form.
- $y$ (vector of F), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A vector of $F$, the second argument of the bilinear form.
- $t_S$ (triple indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator vector in $F$ of the triple $S$.
- $\mathcal F$ (ambient label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space $F^{\otimes3}$, of dimension $m=h^3$, in which all labels lie.
- $X$ (X bank), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The bank of data wires $X_a$.
- $Y$ (Y bank), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The bank of data wires $Y_a$.
- $U_a$ (terminal line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$, the source label of $X_a$.
- $L$ (total dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total number of dimensions lost on decreasing edges.
- $j$ (stage number), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
- $A$ (exposed factor space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The tensor product $F^{\otimes(j-1)}$ of the factors exposed before stage $j$.
- $P$ (earlier tensor line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
- $B$ (complement of P), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The orthogonal complement of $P$ inside $A$.
- $K$ (later tensor line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
- $A'$ (next exposed space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $A$, equal to $A\otimes F$.
- $P'$ (next earlier line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $P$, equal to $P\otimes\langle t_{a_j}\rangle$.
- $B'$ (next complement), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $B$, the orthogonal complement of $P'$ in $A'$.
- $K'$ (next later line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $K$, with $K=\langle t_{a_{j+1}}\rangle\otimes K'$.
- $t_X$ (X-bank indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator of the X-bank triple of a gate or side wire in one invocation.
- $t_Y$ (Y-bank indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator of the Y-bank triple of a gate or side wire in one invocation.
- $L_{\rm b}$ (bit dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on decreasing edges of the bit network.
- $L_{\rm c}$ (complex dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on decreasing edges of the complex network.
- $\Pi_U$ (projection onto a label), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The rational projection onto the label $U$ along $U^\perp$, the matrix of a bit-network vertex labelled $U$.
- $V$ (larger label), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A label containing the label $U$ at the other end of an edge.
- $s_{\rm b}$ (bit smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of smaller calls, the total rational rank of edge matrix differences, in the bit network.
- $s_{\rm c}$ (complex smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of smaller calls, the total number of phase kernels, in the complex network.
- $f$ (call parameter), bound on [Recursive power saving](rank-recurrence.md): The parameter of a recursive call: the number of digits per interchanged chunk, or the number of selected axes of a layer.
- $\mathcal C$ (time per unit volume), bound on [Recursive power saving](rank-recurrence.md): The running time of a call at a given parameter, divided by the volume of its stream.
- $j$ (recursion depth), bound on [Recursive power saving](rank-recurrence.md): The number of recursion levels below the top call, indexing the terms of the unrolled sum; here not the stage number of the subspace-labels page.
- $\eta$ (relative rank deficit), bound on [Recursive power saving](rank-recurrence.md): The relative deficit (Wm-s)/(Wm) by which the number of smaller calls falls short of Wm.
- $u$ (chunk width), bound on [Fast address-chunk interchange](address-interchange.md): The number of bits in each of the two address chunks.
- $p$ (address prefix), bound on [Fast address-chunk interchange](address-interchange.md): The prefix field of an address, before the first chunk.
- $h$ (first chunk), bound on [Fast address-chunk interchange](address-interchange.md): The first of the two address chunks being interchanged.
- $d$ (second chunk), bound on [Fast address-chunk interchange](address-interchange.md): The second of the two address chunks being interchanged.
- $g$ (gap), bound on [Fast address-chunk interchange](address-interchange.md): The address field between the two chunks.
- $z$ (suffix), bound on [Fast address-chunk interchange](address-interchange.md): The address field after the second chunk.
- $q$ (digit radix), bound on [Fast address-chunk interchange](address-interchange.md): The fixed prime radix of the stored digits.
- $\tau$ (saving exponent), bound on [Fast address-chunk interchange](address-interchange.md): The exponent below 1 in the interchange cost, equal to 1 - 2^{-50}.
- $e$ (digit count), bound on [Fast address-chunk interchange](address-interchange.md): The number of radix-q digits in each chunk.
- $k$ (recursion levels), bound on [Fast address-chunk interchange](address-interchange.md): The number of recursion levels, with e = m^k.
- $M$ (vertex matrix), bound on [Fast address-chunk interchange](address-interchange.md): The rational m by m matrix carried by a terminal or gate of the network.
- $A_i$ (edge matrix), bound on [Fast address-chunk interchange](address-interchange.md): The difference of the matrices at the two ends of edge i.
- $\rho$ (output role), bound on [Fast address-chunk interchange](address-interchange.md): The output role to which input wire w is routed.
- $w$ (wire index), bound on [Fast address-chunk interchange](address-interchange.md): The index of an input wire of the network.
- $\Phi_M$ (address shear), bound on [Fast address-chunk interchange](address-interchange.md): The array permutation moving the entry at address (H,D) to (H+MD,D).
- $f_w$ (wire input), bound on [Fast address-chunk interchange](address-interchange.md): The physical input array of wire w.
- $x$ (stream row number), bound on [Fast address-chunk interchange](address-interchange.md): The row number within a role stream.
- $j$ (recursion level index), bound on [Fast address-chunk interchange](address-interchange.md): An index of a recursion level in the unrolled sum.
- $k'$ (levels needed), bound on [Fast address-chunk interchange](address-interchange.md): The number of recursion levels needed for chunks of e digits.
- $\nu$ (set-aside digits), bound on [Fast address-chunk interchange](address-interchange.md): The number of top digits of each chunk set aside to form the row field.
- $\Lambda$ (row range), bound on [Fast address-chunk interchange](address-interchange.md): The range of the row field formed by the top digits of both chunks.
- $\Lambda'$ (padded row count), bound on [Fast address-chunk interchange](address-interchange.md): The row count after padding with zero rows to a multiple of W^{k'}.
- $a_j$ (piece count), bound on [Fast address-chunk interchange](address-interchange.md): The number of pieces of width m^j into which each remaining chunk is cut.
- $v$ (binary vector), bound on [Binary phase frames](phase-frames.md): A binary vector in F_2^m (not the number of triples).
- $E$ (edge residual), bound on [Binary phase frames](phase-frames.md): The edge residual of an edge: the orthogonal summand added going from U to V (not a tensor factor).
- $k$ (column count), bound on [Binary phase frames](phase-frames.md): The number of columns of data, so that an address is a k-tuple (not a depth).
- $u$ (binary vector), bound on [Binary phase frames](phase-frames.md): A binary vector in F_2^m (not an input sequence).
- $w$ (binary vector), bound on [Binary phase frames](phase-frames.md): A binary vector in F_2^m.
- $z$ (binary vector), bound on [Binary phase frames](phase-frames.md): A binary vector in F_2^m.
- $\operatorname{supp}$ (support), bound on [Binary phase frames](phase-frames.md): The set of coordinates where a binary vector is 1.
- $\operatorname{wt}$ (Hamming weight), bound on [Binary phase frames](phase-frames.md): The Hamming weight: the number of coordinates where a binary vector is 1.
- $P_U$ (projection), bound on [Binary phase frames](phase-frames.md): The projection onto a label U over F_2.
- $X_v$ (translation by v), bound on [Binary phase frames](phase-frames.md): The translation of functions of x by the binary vector v.
- $q_U$ (weight phase exponent), bound on [Binary phase frames](phase-frames.md): The Hamming weight of P_U x, modulo four.
- $\mathcal C_U$ (phase frame), bound on [Binary phase frames](phase-frames.md): The phase frame of the label U.
- $\mathcal B$ (orthonormal basis), bound on [Binary phase frames](phase-frames.md): An orthonormal basis of the edge residual E.
- $\varepsilon$ (edge phase sign), bound on [Binary phase frames](phase-frames.md): The sign, plus or minus one modulo four, of one basis vector's phase term, including the edge direction.
- $Z$ (sign matrix), bound on [Binary phase frames](phase-frames.md): The diagonal matrix diag(1,-1).
- $Z_{a,k}$ (sign operator), bound on [Binary phase frames](phase-frames.md): Z on the 27 coordinates of supp(u) in every column, the identity elsewhere.
- $c$ (control bit), bound on [Packed selected-bit addition](packed-bit-addition.md): A control bit, equal to 0 or 1, that gates each addition.
- $u$ (first integer), bound on [Packed selected-bit addition](packed-bit-addition.md): One of the two integers whose parities the eight additions act on.
- $w$ (second integer), bound on [Packed selected-bit addition](packed-bit-addition.md): The other integer, an arbitrary auxiliary value that is restored.
- $R$ (record bits), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in the record stored at each address.
- $L$ (chunk width), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in each of the chunks x, y, z, equal to fK.
- $K$ (segment spacing), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits between consecutive selected positions, at least 6.
- $f$ (selected-bit count), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of selected bits.
- $M$ (address count), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of addresses.
- $V$ (array volume), bound on [Packed selected-bit addition](packed-bit-addition.md): The total number of bits M times R.
- $A_{\rm rect}$ (counter length), bound on [Packed selected-bit addition](packed-bit-addition.md): An upper bound on the bits of the counters, the ceiling of log2(2V).
- $\rho$ (offset), bound on [Packed selected-bit addition](packed-bit-addition.md): The offset of the first selected position within a segment spacing.
- $j_i$ (selected position), bound on [Packed selected-bit addition](packed-bit-addition.md): The i-th selected bit position, rho plus iK.
- $\mathcal B$ (exceptional set), bound on [Packed selected-bit addition](packed-bit-addition.md): The set of addresses at which some guard value falls outside the safe interval.
- $S_0$ (packed map), bound on [Packed selected-bit addition](packed-bit-addition.md): The composition of the eight packed cyclic shifts.
- $T_0$ (ideal map), bound on [Packed selected-bit addition](packed-bit-addition.md): The ideal permutation that performs the required XORs and fixes all other coordinates.
- $D$ (selected chunk count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of selected address chunks.
- $e$ (selected axis count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of selected axes in a group.
- $z$ (array), bound on [Simultaneous butterfly layer](simultaneous-layer.md): An array acted on by the diagonal operator.
- $\mathcal S_D$ (diagonal phase operator), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The diagonal operator multiplying the value at address x by i to the sum of the selected bits.
- $\Gamma$ (basis-change matrix), bound on [Simultaneous butterfly layer](simultaneous-layer.md): An invertible F_2 matrix whose first columns are the residual basis vectors.
- $\mathcal P_\Gamma$ (address permutation), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The address permutation moving the value at x to Gamma x.
- $\xi$ (residual basis index), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The index of the residual basis vectors.
- $\eta_\xi$ (edge sign), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The sign plus or minus one of the xi-th residual basis vector's exponent.
- $\mathbf 1_\xi$ (standard basis vector), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The xi-th standard basis vector.
- $q_0$ (individual chunk count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of leading chunks given individual C kernels.
- $\chi$ (operation-chain bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A bound on the arithmetic operations on a chain from an input to an intermediate coefficient.
- $E$ (invocation operation bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The bound on arithmetic operations in one invocation of the network.
- $\Psi$ (level growth factor), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The sum s plus E, the factor by which each internal level multiplies the chain bound.
- $\varphi$ (chain bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): Any bound on a chain's operation count that is at least one.
- $\vartheta$ (exponent), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The least positive exponent j with m to the j at least Psi.
- $C_0$ (guard constant), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The constant 128 m Psi squared in the reserved extra bits Delta.
- $D$ (transformed axis count), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of transformed axes, d-1.
- $b$ (leftover low bits), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of leftover low bits of an axis.
- $q$ (whole chunks), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of whole K-bit chunks of an axis.
- $B$ (bit reversal), bound on [Tape layout for synthetic transforms](transform-layout.md): The bit-reversal permutation applied along every axis.
- $L$ (layout permutation), bound on [Tape layout for synthetic transforms](transform-layout.md): The record permutation defined by the prefix moves and chunk exchanges.
- $z$ (round input), bound on [Tape layout for synthetic transforms](transform-layout.md): The array entering a round of the transform.
- $\tau$ (interchange exponent), bound on [Tape layout for synthetic transforms](transform-layout.md): The fixed exponent below 1 in the chunk interchange cost.
- $\lambda'$ (layer exponent), bound on [Tape layout for synthetic transforms](transform-layout.md): The fixed exponent below 1 in the simultaneous layer cost.

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
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
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
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Two-point kernel C](phase-kernel.md)
- [Contractions and bilinear contractions](contraction-maps.md)
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [Tensor products of subspaces](tensor-product-of-spaces.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Binary phase frames](phase-frames.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
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

## Problems a reader audit found in the previous version (fix all of them)

- A simulated reader (reader) trying to answer "Explain how the algorithm turns a product of two integers into transforms of power-of-two length, in order: what each stage in the chain (radix digits, address map, resampling with chirps, twist to the polynomial ring, synthetic-transform convolution) accomplishes and why it is needed for the next stage." got stuck at "Expansion of the finite sums gives": The identity F^-(f*g) = M (F^-f)(F^-g) is asserted without the expansion. I could only check it by analogy with the length-q identity on page kur. (stuck at the step level)
- A simulated reader (reader) trying to answer "Explain how the algorithm turns a product of two integers into transforms of power-of-two length, in order: what each stage in the chain (radix digits, address map, resampling with chirps, twist to the polynomial ring, synthetic-transform convolution) accomplishes and why it is needed for the next stage." got stuck at "Their exact counterparts are $LBF^-$ and the opposite map": L and B (layout permutation and bit reversal) are defined on the mov page, which I did not open, so I could not say what they reorder. I treated them as bookkeeping because the page says no reordering is executed. (stuck at the symbol level)

## Previous version (revise it)

It has 544 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 680 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Convolution over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ on the remaining axes is computed by transforming both operands, multiplying records pointwise and transforming back.

Arrays are indexed by $\prod_i\mathbb Z/t_i\mathbb Z$ over the $d-1$ remaining axes, with values in $\mathcal R_r$. Let $M=\prod_i t_i$ be the number of records, $T=rM$ the number of complex coefficients, and $*$ cyclic convolution. $\|\cdot\|_\infty$ is the largest coefficient modulus in the array. A disk array has norm at most $1$; a disk grid array also has parts that are multiples of $2^{-p}$. Multiplying by a power of $y$ permutes coefficients and changes signs, so it preserves the norm.

For arrays over $\mathcal R_r$ define $\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}$. A fixed output coefficient averages $rM$ signed scalar products <cite data-source="paper">$rM$ signed scalar products, and $\mathcal M_r$ is a bilinear</cite>, so $\mathcal M_r$ is a bilinear contraction, $\|\mathcal M_r(f,g)\|_\infty\le\|f\|_\infty\|g\|_\infty$.

Let $F^-$, $F^+$ be the forward and opposite synthetic transforms. Each output entry is an average of images of the inputs under powers of $y$, so both are contractions <cite data-source="paper">Thus both transforms are contractions.</cite> Expansion of the finite sums gives $F^-(f*g)=M(F^-f)(F^-g)$. With $F^+F^-=I/M$ ([Discrete Fourier transform](dft.md)), it follows that $MF^+\bigl((F^-f)(F^-g)/r\bigr)=f*g/(rM)$. Write $P(u,v)=uv/r$ for the pointwise product; here $P$ means this product, not the number of prefix values of the stream-operations page, the earlier tensor line of the subspace-labels page, or a subspace of $A$ as on the tensor-product page. Each coefficient of $uv$ in $\mathcal R_r$ is a signed sum of $r$ products of coefficients, so $\|P(u,v)\|_\infty\le\|u\|_\infty\|v\|_\infty$, and $P$ is bilinear.

The transforms are laid out as in [Tape layout for synthetic transforms](transform-layout.md). Perform both forward transforms and retain their common $LB$ order, with $L$ the layout permutation of records (here not the linear map of the contraction page, nor the total dimension loss of the subspace-labels page) and $B$ the bit-reversal order (here not the row length of the stream-operations page, the suffix digit count of the controlled-shifts page, or an orthogonal complement as on the subspace-labels and tensor-product pages). Their exact counterparts are $LBF^-$ and the opposite map $\mathcal T_+=F^+B^{-1}L^{-1}$; permuting records preserves the norm, so $\mathcal T_+$ is a contraction. With $\ell=\log_2r$ (here $\ell$ is not a depth), each procedure maps disk grid arrays to disk grid arrays with error less than $\delta=\sqrt2\ell\,2^{-p}$ <cite data-source="paper">$\sqrt2\ell\,2^{-p}$, returns disk grid coefficients in the same</cite>. Multiply the $M$ record pairs pointwise there, apply the opposite procedure to that order, and multiply by $M$. Since $LB$ permutes records and leaves polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$, so $\mathcal T_+$ applied to the pointwise product of the stored forward outputs equals $F^+P(F^-f,F^-g)$; its scaling by $M$ is $\mathcal M_r(f,g)$. The procedure keeps the retained order of [Retained frequency order](frequency-order.md), passing the product to the opposite transform without reordering.

Each record product is formed by [Signed packing](signed-packing.md) in $O(rp\log(rp))$ time, truncated by $Q_p$ to $p$ bits of precision, which changes it by less than $\eta=\sqrt2\,2^{-p}$ (here $\eta$ is a truncation error bound, not the relative rank deficit of the recursive power saving page) without raising the norm. There are $M=T/r$ products, so their total cost is $O(Tp\log(rp))$. Each transform, and the final linear scaling, costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$, with $K$ the layout chunk width in bits (here not the later tensor line of the subspace-labels page) and $\tau,\lambda'$ exponents from the cost lemma.

Let $u,v$ be the exact stored forward outputs and $\widetilde u,\widetilde v$ the returned ones, all disk arrays. By bilinearity, $P(\widetilde u,\widetilde v)-P(u,v)=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v)$. By the contraction bound for $P$, and norm at most $1$ of $\widetilde v$ and $u$, each term is less than $\delta$, so $\|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty<2\delta$. With $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$, truncation gives $\|\widetilde z-z_*\|_\infty<2\delta+\eta$, and $\widetilde z$ is a disk grid array. The opposite procedure returns $\widetilde h$ with $\|\widetilde h-\mathcal T_+\widetilde z\|_\infty<\delta$, and $\|\mathcal T_+(\widetilde z-z_*)\|_\infty\le\|\widetilde z-z_*\|_\infty$ since $\mathcal T_+$ is a contraction. The triangle inequality gives $\|\widetilde h-\mathcal T_+z_*\|_\infty<3\delta+\eta$. The exact multiplication by $M$ gives total error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$ <cite data-source="paper">$M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed.</cite>

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

Write the body to `exegenius/tasks/0383-write-ring-convolution.answer.md` and the JSON to `exegenius/tasks/0383-write-ring-convolution.answer.json`, then run `exegenius submit 0383-write-ring-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0383-write-ring-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
