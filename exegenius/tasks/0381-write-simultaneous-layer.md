# exegenius task 0381-write-simultaneous-layer

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

Concept: Simultaneous butterfly layer
Gloss: The second tape procedure: applying H₀ coefficientwise on the same bit of up to d address chunks in time O(V·d^λ′) for a fixed λ′ < 1, instead of d passes.
Also called: parallel butterfly layer

## This page in the argument

The step: Complex variant: the tensor product of $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ on one bit of each of $D\le d$ address chunks (each of $K$ bits, selected at a common offset), acting coefficientwise on polynomial records with $r$ complex $p$-bit coefficients, is computed exactly followed by one truncation $Q_p$, in $O(Vd^{\lambda'})$ time with $\lambda'<1$, rather than $D$ whole-array passes.
How: Rewrite $H_0^{\otimes D}$ as $b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ with the kernel $C$, apply $C^{\otimes e}$ to a group of $e=mf$ axes by the complex network with column phase frames (the binary changes of basis done by packed selected-bit additions), so that each of the $s_{\rm c}$ edge-residual vectors is one child on $f=e/m$ axes of volume $V/W$, and unroll the resulting recurrence with an exact-width guard bound.
Why: Separate butterfly factors would require $D$ whole-array passes; the network's phase frames let one $C^{\otimes e}$ layer be expressed by $s_{\rm c}<W_{\rm c}m$ smaller layers on streams of volume $V/W_{\rm c}$, which is the same recursion as for the interchange. (the sources say so: "factors would require $D$ whole-array passes." (paper))
Striking feature: The cost is $O(Vd^{\lambda'})$ with $\lambda'=1-2^{-54}$, only barely below the $D\le d$ separate passes, and the saving comes from $s_{\rm c}/W_{\rm c}<m^\sigma$. (explain why it holds, from the method)

Its sub-steps, in order:

- The kernel $C=aI+bX$ satisfies $H_0=b\,\mathsf SC\mathsf S$ (with $\mathsf S=\operatorname{diag}(1,i)$), $C^2=X$ and $C^4=I$.
- A group of $e=mf$ axes is handled by the complex network: each edge residual vector is one child on $f$ axes, an arbitrary residual basis is moved into coordinate position by binary changes of basis (products of at most $m(m-1)+3m$ row additions), and inverse children use forward ones, so there are exactly $s_{\rm c}$ children.
- Hence $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ with $(\mathcal S_Dz)(x)=i^{x_1+\dots+x_D}z(x)$, an exact Gaussian dyadic operation.
- Selected bits of two chunks can be XORed (with a third chunk as restored scratch) by eight cyclic shifts of whole chunk ranges plus a repair of an explicitly bounded exceptional set of addresses, in time $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$. (on [Packed selected-bit addition](packed-bit-addition.md))
- Therefore the complete binary change of basis and its inverse on $e$ axis chunks cost $O(V((eK)^\tau+1))$ on a stream of volume $V$.
- A group of $e$ selected axes (with $D$ axes in all and $q_0$ of them handled individually) is processed in $O(V\,d^{\lambda'})$ time by the recurrence $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ stopped at $e<d^\beta$.
- The whole layer can be evaluated exactly: with $\Delta=\lceil C_0d^{C_1}\rceil$, reserving $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits per real component represents every intermediate coefficient exactly, and this width is $O(p)$ because $\epsilon C_1<1$.
- Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays.
- Componentwise truncation toward zero keeps the disk and changes each component by less than $2^{-p}$, so $\|Q_p(\mathcal Hz)-\mathcal Hz\|_\infty<\sqrt2\,2^{-p}$.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- Both tape primitives (the interchange of two address chunks of $u$ digits and the simultaneous butterfly layer on up to $d$ axes) cost the volume times a power below one of their width, because a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$, so the cost per unit volume grows by $s/W<m$ per factor $m$ of the parameter.; how: Build a fixed finite linear network of $W$ wires that exchanges two banks and restores all scratch values, make the representation of each wire's array vary along the network through frames so that an edge costs one smaller call per unit of rank, show the total rank $s$ is below $Wm$, fix an exponent, and solve the recurrence in the bit variant (interchange) and the complex variant (butterfly layer). (on [Recursive power saving](rank-recurrence.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.6.1, S1.6.2, S1.6.2b, S1.6.3b, S1.6.4, S1.6.5, S1.6.6, S1.6.7). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.6.1**: The kernel $C=aI+bX$ satisfies $H_0=b\,\mathsf SC\mathsf S$ (with $\mathsf S=\operatorname{diag}(1,i)$), $C^2=X$ and $C^4=I$.
Source: "H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad" (paper)
> Put \[ H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad H=\sqrt2 H_0,\qquad \mathsf S=\operatorname{diag}(1,i),\qquad Z=\operatorname{diag}(1,-1). \] For the bit-flip matrix $X=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$, define \begin{equation}\label{eq:phase-C} C=H\mathsf SH=aI+bX,\qquad a=\frac{1+i}{2},\quad b=\frac{1-i}{2}. \end{equation} Direct multiplication gives \begin{equation}\label{eq:phase-basic-identities} H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad C^{-1}=bI+aX=-iZCZ. \end{equation} In particular, $C=iZC^{-1}Z$. These identities use only Gaussian dyadic coefficients. The Hadamard matrices in the definition of $\mathcal C_U$ are used to prove identities; they need not be executed by the machine.

**S1.6.2**: A group of $e=mf$ axes is handled by the complex network: each edge residual vector is one child on $f$ axes, an arbitrary residual basis is moved into coordinate position by binary changes of basis (products of at most $m(m-1)+3m$ row additions), and inverse children use forward ones, so there are exactly $s_{\rm c}$ children.
How: Conjugate the edge identity by a basis change $\mathcal P_M$ so that the residual vectors become the first coordinate vectors, apply one child $(C^{\epsilon_h})^{\otimes f}$ per residual vector to the $f$ bits of slot $h$, and use $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$ to avoid inverse children.
- S1.6.2.1: Conjugation by $\mathcal P_M$ (moving the value at $x$ to $Mx$) satisfies $\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}$, which uses only that $M$ is invertible.
  Source: "\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}." (paper)
  > \paragraph{Implementing an arbitrary residual basis.} For $M\in\operatorname{GL}(m,\mathbb F_2)$, let $\mathcal P_M$ be the address permutation that moves the value at $x$ to $Mx$. Thus $(\mathcal P_Mf)(x)=f(M^{-1}x)$, and \begin{equation}\label{eq:phase-conjugation} \mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}. \end{equation} Extend $v_1,\ldots,v_{\rho_{\rm edge}}$ to a basis of $\mathbb F_2^m$ and take these vectors as the first $\rho_{\rm edge}$ columns of $M$. The displayed edge identity then becomes \begin{equation}\label{eq:phase-edge-coordinate} \mathcal C_{U_+}\mathcal C_{U_-}^{-1} =\mathcal P_M\left(\prod_{j=1}^{\rho_{\rm edge}}C_{e_j}^{\epsilon_j}\right) \mathcal P_M^{-1}, \end{equation} where $e_j$ is the $j$th standard basis vector. The matrix $M$ need not preserve the dot product: equation~\eqref{eq:phase-conjugation} only uses its invertibility.
- S1.6.2.2: After applying $\mathcal P_M^{-1}$ to each column, for each $1\le h\le\rho_{\rm edge}$ one applies $(C^{\epsilon_h})^{\otimes f}$ to the $f$ bits of slot $h$: one child operation on $f$ axes per residual vector.
  Source: "$1\le h\le\rho_{\rm edge}$, apply $(C^{\epsilon_h})^{\otimes f}$ to the" (paper)
  > To implement \eqref{eq:phase-edge-coordinate} on the group, first apply $\mathcal P_M^{-1}$ separately to each column. For each $1\le h\le\rho_{\rm edge}$, apply $(C^{\epsilon_h})^{\otimes f}$ to the $f$ bits $x_{h,0},\ldots,x_{h,f-1}$. This is one child operation on the $f$ axes in slot $h$. Finally apply $\mathcal P_M$ to every column. A negative directional kernel still requires only one forward child, because \begin{equation}\label{eq:phase-inverse-child} (C^{-1})^{\otimes f} =(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}. \end{equation} The rightmost phase is applied first. All inverse wrappers are address signs and constant fourth-root phases, so they add no recursive calls.
- S1.6.2.3: A negative kernel still requires one forward child: $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$, where the wrappers are address signs and fourth-root phases.
  Source: "=(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}." (paper)
  > To implement \eqref{eq:phase-edge-coordinate} on the group, first apply $\mathcal P_M^{-1}$ separately to each column. For each $1\le h\le\rho_{\rm edge}$, apply $(C^{\epsilon_h})^{\otimes f}$ to the $f$ bits $x_{h,0},\ldots,x_{h,f-1}$. This is one child operation on the $f$ axes in slot $h$. Finally apply $\mathcal P_M$ to every column. A negative directional kernel still requires only one forward child, because \begin{equation}\label{eq:phase-inverse-child} (C^{-1})^{\otimes f} =(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}. \end{equation} The rightmost phase is applied first. All inverse wrappers are address signs and constant fourth-root phases, so they add no recursive calls.
- S1.6.2.4: Gaussian elimination writes any $M\in\operatorname{GL}(m,\mathbb F_2)$ as a product of at most $m(m-1)+3m$ row additions (each row swap is three additions).
  Source: "as a product of at most $m(m-1)+3m$ elementary row additions: one clears" (paper)
  > Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$ as a product of at most $m(m-1)+3m$ elementary row additions: one clears at most $m-1$ other entries per pivot, and each row swap is three row additions. Reversing the elimination gives the required product since each row addition is an involution. The number is a constant because $m$ is fixed. Adding row $h'$ to row $h$ in every column applies $x_{h,j}\leftarrow x_{h,j}\mathbin\oplus x_{h',j}$ for every $0\le j<f$. Thus one row addition changes corresponding selected positions in two whole slots. The packed address operation proved below performs all of these XORs together.
- S1.6.2.5: Applying the network to $e=mf$ axes, summing the residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot.
  Source: "$e=mf$ selected axes.  Summing its residual dimensions gives exactly" (paper)
  > \paragraph{The exact recursive contract.} Apply the finite network with these column frames to a group of $e=mf$ selected axes. Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot. The source and sink $Z_{a,f}$ signs, together with the scalar $i^{27f}$ at each affected sink, turn every endpoint kernel into a forward one. Negating the prescribed physical bank and undoing its exchange returns each result to its original role. Proposition~\ref{prop:complex-motif-interface} therefore gives $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary. Formula~\eqref{eq:phase-inverse-child} supplies each inverse child from one forward call, and none of the corrections adds a child. The remaining operations are a fixed number of binary row additions and coefficientwise scalar operations.
- S1.6.2.6: Each such child call is on $f=e/m$ axes of one slot, and all corrections add no further children.
  Source: "$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot." (paper)
  > \paragraph{The exact recursive contract.} Apply the finite network with these column frames to a group of $e=mf$ selected axes. Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot. The source and sink $Z_{a,f}$ signs, together with the scalar $i^{27f}$ at each affected sink, turn every endpoint kernel into a forward one. Negating the prescribed physical bank and undoing its exchange returns each result to its original role. Proposition~\ref{prop:complex-motif-interface} therefore gives $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary. Formula~\eqref{eq:phase-inverse-child} supplies each inverse child from one forward call, and none of the corrections adds a child. The remaining operations are a fixed number of binary row additions and coefficientwise scalar operations.

**S1.6.2b**: Hence $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ with $(\mathcal S_Dz)(x)=i^{x_1+\dots+x_D}z(x)$, an exact Gaussian dyadic operation.
Source: "H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D." (paper)
> \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.

**S1.6.3b**: Therefore the complete binary change of basis and its inverse on $e$ axis chunks cost $O(V((eK)^\tau+1))$ on a stream of volume $V$.
Source: "$O(V((eK)^\tau+1))$ on a stream of volume $V$." (paper)
> Under the asymptotic hypotheses in the final assertion of that lemma, the complete change of basis and its inverse therefore cost $O(V((eK)^\tau+1))$ on a stream of volume $V$. Here $e$ counts axis chunks, while $eK$ counts address bits; the fixed factor $m$ between $eK$ and the slot width does not affect the bound. The same conclusion holds after the row padding and splitting below, because every role stream retains a complete suffix with the same fixed field lengths in every row.

**S1.6.4**: A group of $e$ selected axes (with $D$ axes in all and $q_0$ of them handled individually) is processed in $O(V\,d^{\lambda'})$ time by the recurrence $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ stopped at $e<d^\beta$.
How: Use the first $q_0$ chunks as the row index so the rows split into $W$ role streams of volume $1/W$ at each level, bound the overhead of each node by the cost of the binary basis changes, stop the recursion when $e<d^\beta$ and sum internal nodes and leaves separately, then combine the base-$m$ groups.
- S1.6.4.1: Individually applied kernels cost $O(Ve)$ for $e$ selected bits.
  Source: "\(O(Ve)\) on any stream with these complete ranges and record format." (paper)
  > -point conventions of Section~\ref{sec:streams}; multiplication by \(i\) swaps the real and imaginary components and changes one sign. The common guarded width makes these operations exact. The coefficient scan costs \(O(rp)\) per pair of records, linear in their guarded bit length and including any reversal of bits inside a coefficient. Write the first result to stream \(0\) and the second to stream \(1\), both in coefficient order, then merge according to the selected bit. The merge restores the original lexicographic address order. The elementary split and merge include their counters and cleanup and cost \(O(V)\); the paired arithmetic scan also costs \(O(V)\). Thus \(e\) individual kernels cost \(O(Ve)\) on any stream with these complete ranges and record format.
- S1.6.4.2: At an internal node the binary changes of basis, scalar gates and reassembly cost $O(V((eK)^\tau+1))$, from a fixed number of packed row additions.
  Source: "O\bigl(V((eK)^\tau+1)\bigr)" (paper)
  > First consider an internal node containing \(e=m^k\) consecutive active chunks, with \(k\ge1\). Split it into \(m\) consecutive slots, each containing \(e/m\) chunks. The phase construction supplies one recursive call on a slot for each vector in an edge residual basis, hence exactly \(s\) calls in one invocation of the network. If the logical volume entering this node is \(V\), binary changes of basis, their inverses, scalar gates, endpoint corrections and reassembly of the physical banks cost \[ O\bigl(V((eK)^\tau+1)\bigr) \] at this node. Each slot has \((e/m)K\) address bits, so Lemma~\ref{lem:packed-selected-bit-rectangle} gives the stated bound for a row addition. The network and all of its \(m\)-dimensional residual bases are fixed, so the total number of row additions is fixed as well. At the same guarded width, the scalar gates cost a constant number of scans of the current volume. Address and descriptor work bounded by any fixed polynomial in \(p\) per record is also absorbed: its ratio to the record's \(\Theta(rp)\) bits tends to zero.
- S1.6.4.3: Put $q_0=\lceil\log_2W\rceil\lceil\log_m(2d)\rceil$ and $k_0=\lceil\log_md\rceil$.
  Source: "\qquad k_0=\lceil\log_m d\rceil." (paper)
  > \paragraph{Where the rows come from.} Put \[ q_0=\lceil\log_2 W\rceil\, \lceil\log_m(2d)\rceil, \qquad k_0=\lceil\log_m d\rceil. \] If \(D\le q_0\), use individual \(C\) kernels, at cost \(O(V\log d)\). Otherwise apply \(C\) individually on the selected bits of the first \(q_0\) chunks, in \(O(V\log d)\) time. These chunks remain a complete consecutive address block before all the remaining chunks; regard their concatenated bits as one row index. Its range has length \(R_{\rm row}=2^{q_0K}\ge W^{k_0}\), since \(K\ge1\) for sufficiently large \(p\) and \(q_0K\ge k_0\log_2W\). Within each preceding prefix, add the same number of zero rows to reach the next multiple of \(W^{k_0}\); the volume grows by a factor at most two. At any recursive depth \(j\le k_0\), the row count is divisible by \(W^{k_0-j}\).
- S1.6.4.4: The first $q_0$ chunks form a row index of range $R_{\rm row}=2^{q_0K}\ge W^{k_0}$; padding to a multiple of $W^{k_0}$ at most doubles the volume.
  Source: "length \(R_{\rm row}=2^{q_0K}\ge W^{k_0}\), since \(K\ge1\) for sufficiently" (paper)
  > \paragraph{Where the rows come from.} Put \[ q_0=\lceil\log_2 W\rceil\, \lceil\log_m(2d)\rceil, \qquad k_0=\lceil\log_m d\rceil. \] If \(D\le q_0\), use individual \(C\) kernels, at cost \(O(V\log d)\). Otherwise apply \(C\) individually on the selected bits of the first \(q_0\) chunks, in \(O(V\log d)\) time. These chunks remain a complete consecutive address block before all the remaining chunks; regard their concatenated bits as one row index. Its range has length \(R_{\rm row}=2^{q_0K}\ge W^{k_0}\), since \(K\ge1\) for sufficiently large \(p\) and \(q_0K\ge k_0\log_2W\). Within each preceding prefix, add the same number of zero rows to reach the next multiple of \(W^{k_0}\); the volume grows by a factor at most two. At any recursive depth \(j\le k_0\), the row count is divisible by \(W^{k_0-j}\).
- S1.6.4.5: At recursive depth $j\le k_0$ the row count is divisible by $W^{k_0-j}$.
  Source: "row count is divisible by \(W^{k_0-j}\)." (paper)
  > \paragraph{Where the rows come from.} Put \[ q_0=\lceil\log_2 W\rceil\, \lceil\log_m(2d)\rceil, \qquad k_0=\lceil\log_m d\rceil. \] If \(D\le q_0\), use individual \(C\) kernels, at cost \(O(V\log d)\). Otherwise apply \(C\) individually on the selected bits of the first \(q_0\) chunks, in \(O(V\log d)\) time. These chunks remain a complete consecutive address block before all the remaining chunks; regard their concatenated bits as one row index. Its range has length \(R_{\rm row}=2^{q_0K}\ge W^{k_0}\), since \(K\ge1\) for sufficiently large \(p\) and \(q_0K\ge k_0\log_2W\). Within each preceding prefix, add the same number of zero rows to reach the next multiple of \(W^{k_0}\); the volume grows by a factor at most two. At any recursive depth \(j\le k_0\), the row count is divisible by \(W^{k_0-j}\).
- S1.6.4.6: Each recursive edge call acts on one role stream of volume exactly $1/W$ of its parent's.
  Source: "one role stream with volume exactly \(1/W\) of its parent's logical" (paper)
  > At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\), and send that entire row to physical wire role \(w\), indexed there by \(g\). Every role stream has the same remaining address shape. Thus a pointwise gate reads the records with the same \(g\) and the same remaining address in its touched roles. The scalar network allows these role values to be arbitrary, so the split supplies its scratch roles from existing rows. Each recursive edge call acts on one role stream with volume exactly \(1/W\) of its parent's logical volume.
- S1.6.4.7: Choose rational exponents $0<\tau<1$, $\max\{0,\log_m(s/W)\}\le\sigma<1$, $\max\{\tau,\sigma\}<\lambda<1$ and $\tau(1+c/\beta)<\lambda$.
  Source: "0<\tau<1,\qquad" (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- S1.6.4.8: Let $F(e)$ be time divided by current volume: $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ for $e\ge d^\beta$ and $F(e)=O(e)$ for $e<d^\beta$.
  Source: "F(e)\le (s/W)F(e/m)+O((eK)^\tau+1)," (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- S1.6.4.9: The $s$ child calls are executed on streams of volume $V/W$, so their total cost is $s(V/W)F(e/m)$, giving the factor $s/W$ after dividing by $V$.
  Source: "Indeed, the \(s\) child calls are executed on streams of volume" (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- S1.6.4.10: At an internal node $e\ge d^\beta$, so $K\le d^c\le e^{c/\beta}$ and the overhead is $O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)$.
  Source: "O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)" (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- S1.6.4.11: With $a=s/W\le m^\sigma<m^\lambda$ the internal costs sum to at most $Ce^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)$.
  Source: "Put \(a=s/W\).  Since \(a\le m^\sigma<m^\lambda\), the internal" (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- S1.6.4.12: The geometric series converges because $a/m^\lambda<1$, so the internal contribution is $O(e^\lambda)$.
  Source: "C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)." (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- S1.6.4.13: The leaves, after $j$ levels with $u=e/m^j<d^\beta$ chunks each, contribute at most $O(a^ju)\le O(e^\sigma u^{1-\sigma})\le O(e^\sigma d^{\beta(1-\sigma)})$, using $a^j\le m^{j\sigma}=(e/u)^\sigma$ (also valid for $a<1$ since $\sigma\ge0$).
  Source: "O(a^ju)\le O(e^\sigma u^{1-\sigma})" (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- S1.6.4.14: Write $D-q_0=\sum_ja_jm^j$ in base $m$ with $0\le a_j<m$ and partition the remaining chunks into $a_j$ pieces of $m^j$ chunks (at most $(m-1)(1+\lfloor\log_md\rfloor)$ pieces).
  Source: "Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\)." (paper)
  > Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\). Partition the remaining chunks into \(a_j\) consecutive pieces containing \(m^j\) chunks for each \(j\). There are at most \((m-1)(1+\lfloor\log_m d\rfloor)\) pieces. Adding their costs and the row preprocessing gives \[ O\!\left(\log(2d) \bigl[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1\bigr]\right) =O(d^{\lambda'}) \] for any fixed \[ \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1. \] The case \(D\le q_0\), in which preprocessing would consume all active chunks, was handled by individual kernels. Thus all constants and all tape counts are independent of \(p,d,r\) and the input data.
- S1.6.4.15: Adding the pieces and the row preprocessing gives $O(\log(2d)[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1])=O(d^{\lambda'})$ for any fixed $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$ (the strict inequality absorbs the logarithmic number of groups).
  Source: "=O(d^{\lambda'})" (paper)
  > Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\). Partition the remaining chunks into \(a_j\) consecutive pieces containing \(m^j\) chunks for each \(j\). There are at most \((m-1)(1+\lfloor\log_m d\rfloor)\) pieces. Adding their costs and the row preprocessing gives \[ O\!\left(\log(2d) \bigl[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1\bigr]\right) =O(d^{\lambda'}) \] for any fixed \[ \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1. \] The case \(D\le q_0\), in which preprocessing would consume all active chunks, was handled by individual kernels. Thus all constants and all tape counts are independent of \(p,d,r\) and the input data.

**S1.6.5**: The whole layer can be evaluated exactly: with $\Delta=\lceil C_0d^{C_1}\rceil$, reserving $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits per real component represents every intermediate coefficient exactly, and this width is $O(p)$ because $\epsilon C_1<1$.
How: Bound the number $A(e)$ of arithmetic operations on any chain from an input coefficient to an intermediate one by a recurrence over the recursion, solve it, and note that each operation at most doubles the modulus and adds one denominator bit.
- S1.6.5.1: For the complex network let $E=64(W+m+1)^3$, $B=s+E$, and $\nu=\min\{j\ge1:m^j\ge B\}$.
  Source: "E=64(W+m+1)^3,\qquad B=s+E," (paper)
  > For the complex network, let \[ E=64(W+m+1)^3,\qquad B=s+E, \qquad \nu=\min\{j\ge1:m^j\ge B\}, \] and set \[ C_1=\max\{20,\nu+3\},\qquad C_0=128mB^2, \qquad \Delta=\lceil C_0d^{C_1}\rceil. \] For the stated \(h=100\) construction, the complex network has \[ \begin{split} m&=1{,}000{,}000,\\ W&=1{,}873{,}807{,}244{,}643{,}542{,}670{,}000,\\ s&=1{,}873{,}807{,}244{,}636{,}671{,}267{,}308{,}000{,}000. \end{split} \] These values give \(m^{10}<B<m^{11}\), hence \(\nu=11\) and \(C_1=20\). In fact the bound below needs only exponent fourteen; the choice twenty leaves an explicit additional margin.
- S1.6.5.2: For the stated $h=100$ construction $m^{10}<B<m^{11}$, hence $\nu=11$ and $C_1=\max\{20,\nu+3\}=20$ (the bound needs only exponent fourteen).
  Source: "These values give \(m^{10}<B<m^{11}\), hence \(\nu=11\) and" (paper)
  > For the complex network, let \[ E=64(W+m+1)^3,\qquad B=s+E, \qquad \nu=\min\{j\ge1:m^j\ge B\}, \] and set \[ C_1=\max\{20,\nu+3\},\qquad C_0=128mB^2, \qquad \Delta=\lceil C_0d^{C_1}\rceil. \] For the stated \(h=100\) construction, the complex network has \[ \begin{split} m&=1{,}000{,}000,\\ W&=1{,}873{,}807{,}244{,}643{,}542{,}670{,}000,\\ s&=1{,}873{,}807{,}244{,}636{,}671{,}267{,}308{,}000{,}000. \end{split} \] These values give \(m^{10}<B<m^{11}\), hence \(\nu=11\) and \(C_1=20\). In fact the bound below needs only exponent fourteen; the choice twenty leaves an explicit additional margin.
- S1.6.5.3: The gate, child-correction, source, sink and bank-correction operations of one invocation total $24W^3+4s+4W+4<E$ elementary operations (using $s<Wm$).
  Source: "work, not arithmetic on coefficients.  Since \(s<Wm\), the total" (paper)
  > For an inverse child, each \(Z^{\otimes f}\) is one sign chosen by the parity of the selected address bits, and the scalar fourth-root phase takes at most one sign change and one multiplication by \(i\). This gives at most \(4s\) operations for the child corrections. The source, sink and bank corrections take at most \(4W+4\) more. Calculating the address parities and phase exponents is address or descriptor work, not arithmetic on coefficients. Since \(s<Wm\), the total \(24W^3+4s+4W+4\) is less than \(E=64(W+m+1)^3\). Binary address permutations add no coefficient arithmetic at their interfaces.
- S1.6.5.4: The depth $A(e)$ of arithmetic chains satisfies $A(e)\le sA(e/m)+E$ at an internal node and $A(e)\le8e$ at a leaf (the depth recurrence uses $s$, not $s/W$, since it concatenates the calls).
  Source: "A(e)\le sA(e/m)+E" (paper)
  > The paired evaluation in \eqref{eq:individual-C-pair} uses at most eight elementary operations: form the sum and difference, multiply the difference by \(i\), then form the two half-sums. We may therefore use \[ A(e)\le sA(e/m)+E \quad\hbox{at an internal node},\qquad A(e)\le8e \quad\hbox{at a leaf}. \] The depth estimate concatenates the \(s\) calls, so it uses \(s\). The factor \(1/W\) in the earlier time recurrence accounted for their smaller stream volumes.
- S1.6.5.5: For any $x\ge1$, $sx+E\le(s+E)x=Bx$, so each of the at most $\lceil\log_md\rceil$ internal levels multiplies the bound by at most $B$.
  Source: "For any bound \(x\ge1\), \(sx+E\le(s+E)x=Bx\)." (paper)
  > There are at most \(k\le\lceil\log_m d\rceil\) internal levels. For any bound \(x\ge1\), \(sx+E\le(s+E)x=Bx\). Starting with \(8e\le8d\le8dB\) at a leaf and applying this inequality through the levels gives the first bound below. For the second, use \(B\le m^\nu\) and \[ B^{k+1}\le B^{\log_m d+2} =B^2d^{\log_m B}\le B^2d^\nu. \] Thus \[ A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}. \] For the sufficiently large sizes under consideration, the earlier piece count is at most \(md\). Concatenating their depths contributes at most \(8mB^2d^{\nu+2}\). In either preprocessing branch, at most \(d\) individual kernels are used, contributing at most \(8d\). Splitting rows, padding, copying and removing padding add no coefficient arithmetic.
- S1.6.5.6: Using $B^{k+1}\le B^{\log_md+2}=B^2d^{\log_mB}\le B^2d^\nu$ one gets $A(e)\le8dB^{k+1}\le8B^2d^{\nu+1}$.
  Source: "A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}." (paper)
  > There are at most \(k\le\lceil\log_m d\rceil\) internal levels. For any bound \(x\ge1\), \(sx+E\le(s+E)x=Bx\). Starting with \(8e\le8d\le8dB\) at a leaf and applying this inequality through the levels gives the first bound below. For the second, use \(B\le m^\nu\) and \[ B^{k+1}\le B^{\log_m d+2} =B^2d^{\log_m B}\le B^2d^\nu. \] Thus \[ A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}. \] For the sufficiently large sizes under consideration, the earlier piece count is at most \(md\). Concatenating their depths contributes at most \(8mB^2d^{\nu+2}\). In either preprocessing branch, at most \(d\) individual kernels are used, contributing at most \(8d\). Splitting rows, padding, copying and removing padding add no coefficient arithmetic.
- S1.6.5.7: A value at depth $\ell$ lies in $2^{-(p+\ell)}\mathbb Z[i]$ and has modulus at most $2^\ell$ (addition at most doubles the modulus, halving adds a denominator bit), so reserving $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits per real component, with $\Delta=\lceil C_0d^{C_1}\rceil$, represents every intermediate coefficient exactly.
  Source: "lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most" (paper)
  > To see how this count controls numerical size, start with disk-valued coefficients in \(2^{-p}\mathbb Z[i]\). A value at depth \(\ell\) lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most \(2^\ell\). This follows by induction: addition or subtraction can at most double the maximum modulus of its operands; halving adds at most one denominator bit; and signs and multiplication by \(i\) preserve both bounds. The charge of \(t\) for the final shift is the same as \(t\) successive halvings. Thus reserving \(p+\Delta\) fractional bits and \(\Delta+3\) integer and sign bits per real component represents every intermediate coefficient exactly and prevents overflow. Shifts consume the reserved fractional zeros and discard no bits.
- S1.6.5.8: Choosing $\epsilon C_1<1$ and $d=\Theta(p^\epsilon)$ makes $\Delta=o(p)$, so the full coefficient width is $O(p)$ and addition, shifts, copying and phase changes cost $O(p)$ per coefficient.
  Source: "Choose \(\epsilon C_1<1\).  Since \(d=\Theta(p^\epsilon)\)," (paper)
  > Choose \(\epsilon C_1<1\). Since \(d=\Theta(p^\epsilon)\), \(\Delta=o(p)\), and the full coefficient width is \(O(p)\), as required in the time analysis. Addition, signed shifts, copying and phase changes consequently take \(O(p)\) bit operations per coefficient.

**S1.6.6**: Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays.
Source: "absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk" (paper)
> The guard-width calculation above bounds both denominator and magnitude growth by $\lceil C_0d^{C_1}\rceil$. Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, this is $o(p)$ uniformly over the allowed $d$, so every intermediate coefficient is represented exactly with the stated $O(p)$ width. The initial scan removes or adds only redundant leading sign bits and appends the reserved fractional zeros to put each supplied component in this guarded format. To truncate toward zero at the end, shift its absolute numerator right by the number of added fractional bits, restore its sign, and write the result in $w$ bits. These scans cost $O(V)$. Finally, every row of $\mathcal H$ has absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk arrays, and componentwise truncation preserves that disk and has error less than $\sqrt2\,2^{-p}$: truncation cannot increase the absolute value of either component, and changes each by less than $2^{-p}$. The truncated numerators have magnitude at most $2^p$, so the supplied component width can hold them. \end{proof} \section{Synthetic transforms and their tape layout} \label{sec:synthetic-layouts}

**S1.6.7**: Componentwise truncation toward zero keeps the disk and changes each component by less than $2^{-p}$, so $\|Q_p(\mathcal Hz)-\mathcal Hz\|_\infty<\sqrt2\,2^{-p}$.
Source: "error less than $\sqrt2\,2^{-p}$: truncation cannot increase the" (paper)
> The guard-width calculation above bounds both denominator and magnitude growth by $\lceil C_0d^{C_1}\rceil$. Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, this is $o(p)$ uniformly over the allowed $d$, so every intermediate coefficient is represented exactly with the stated $O(p)$ width. The initial scan removes or adds only redundant leading sign bits and appends the reserved fractional zeros to put each supplied component in this guarded format. To truncate toward zero at the end, shift its absolute numerator right by the number of added fractional bits, restore its sign, and write the result in $w$ bits. These scans cost $O(V)$. Finally, every row of $\mathcal H$ has absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk arrays, and componentwise truncation preserves that disk and has error less than $\sqrt2\,2^{-p}$: truncation cannot increase the absolute value of either component, and changes each by less than $2^{-p}$. The truncated numerators have magnitude at most $2^p$, so the supplied component width can hold them. \end{proof} \section{Synthetic transforms and their tape layout} \label{sec:synthetic-layouts}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.6.3 (on [Packed selected-bit addition](packed-bit-addition.md)): Selected bits of two chunks can be XORed (with a third chunk as restored scratch) by eight cyclic shifts of whole chunk ranges plus a repair of an explicitly bounded exceptional set of addresses, in time $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Two-point kernel C](phase-kernel.md)
- [Fast address-chunk interchange](address-interchange.md)

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Binary phase frames](phase-frames.md): Frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} whose edge differences are products of translation kernels aI + bX_v, one per vector of an orthonormal residual basis.
  Shown as: Simultaneous butterfly layer *<predicate>* Binary phase frames
- [Recursive power saving](rank-recurrence.md): Each call at parameter m·f makes s calls at parameter f on streams of 1/W the volume, so cost per unit volume grows by s/W < m per factor m, giving a power saving.
  Shown as: Simultaneous butterfly layer *<predicate>* Recursive power saving
- [Packed selected-bit addition](packed-bit-addition.md): XORing selected bits between two address chunks (with a third chunk as restored scratch) using cyclic shifts of whole chunk ranges plus a repair of explicitly bounded exceptional addresses.
  Shown as: Simultaneous butterfly layer *<predicate>* Packed selected-bit addition
- [Fixed-point Gaussian dyadic records](fixed-point.md): Complex values stored as signed two's-complement integers over a power-of-two denominator 2^{-p}; intermediate values are exact and one truncation Q_p rounds back to the p-bit grid.
  Shown as: Simultaneous butterfly layer *<predicate>* Fixed-point Gaussian dyadic records

## Pages that build on this one

- Tape layout for synthetic transforms: Placing the selected bits of the participating axes at a common offset in K-bit chunks so each round of the synthetic transform is one simultaneous layer, costing less than log t passes.
- Cost accounting and the exponent κ: Dividing each cost by V = Tp, the dominant terms are powers of p below one with minimum margin 2^{-181} = 2κ, giving total time O(n(lg n)^{1−κ}).

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
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Retained frequency order](frequency-order.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [Tensor products of subspaces](tensor-product-of-spaces.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "Simultaneous normalized butterfly layer" (paper)

  > \begin{proposition}[Simultaneous normalized butterfly layer] \label{prop:simultaneous-layer} Fix \[ \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad C_1=20. \] Let $c,\epsilon,\lambda,\lambda'$ be fixed positive rational numbers satisfying \[ \max\{\tau,\sigma\}<\lambda<1,\qquad \tau(1+c/\beta)<\lambda,\qquad \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1, \qquad \epsilon C_1<1. \] Fix positive constants $a_d\le b_d$ and $a_r\le b_r$, and fix positive constants $C_M,C_{\rm desc},C_w$ with $C_w>1$. For these fixed choices there are a cutoff $p_0$, one fixed finite-alphabet multitape procedure, and an implicit time constant with the following guarantee. The cutoff and time constant may depend on the fixed rational parameters and these constants. For every choice of positi

- "simultaneously on selected coordinate bits of the numerical arrays." (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- A simulated reader (reader) trying to answer "Why can the log n factor in n log n only be beaten here by making address movement and butterfly arithmetic cheaper, rather than by some other tweak of a standard FFT-style multiplier? What accounting of a standard transform on a tape machine leads to this?" got stuck at "rather than $D$ whole-array passes": I could follow that a Simultaneous butterfly layer replaces D passes with a cost of d^lambda', but not why the frame changes on a fixed exchange network make one layer cost d^lambda' instead of V per bit. The network and frame pages were not opened. (the reader followed the steps but not why they lead where they do: say what this step is for)
- A simulated reader (reader) trying to answer "Why can the log n factor in n log n only be beaten here by making address movement and butterfly arithmetic cheaper, rather than by some other tweak of a standard FFT-style multiplier? What accounting of a standard transform on a tape machine leads to this?" got stuck at "and $\log d$ pieces give $O(d^{\lambda'}).$": The page gives the recursion F(e) <= (s/W) F(e/m) + O((eK)^tau + 1) and says the leaves and log d pieces give O(d^lambda'). I could not rebuild from this how a round over d axes comes to d^lambda' rather than d passes. (stuck at the step level)
- A simulated reader (reader) trying to answer "Summarise in a few sentences what the main theorem says about multiplying two n-bit integers, in which machine model it holds, which earlier conjecture it refutes, and the overall plan the proof follows to get there." got stuck at "Absolute row sums multiply under Tensor products of subspacess, so each row of $\mathcal H=H_0^{\otimes D}$ has absolute row sum one.": Tensor products of subspaces is not defined on any page I read. From H_0 tensored D times and the description of one bit per chunk, I guessed it is a tensor (Kronecker) product. The reader has not been taught tensor products, and I could not check the row-sum conclusion. (stuck at the symbol level)

## Previous version (revise it)

It has 610 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 762 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The simultaneous butterfly layer applies $H_0$ coefficientwise to one bit of each of $D\le d$ selected address chunks of $K$ bits, at a common offset, in time $O(Vd^{\lambda'}),$ $\lambda'<1,$ instead of $D$ passes; here $D$ is the number of selected address chunks, not the second chunk value of [Fast address-chunk interchange](address-interchange.md), and $D$ is not the source group of [Matrix shear by triangular factorization](matrix-shear.md).

With $\mathsf S=\operatorname{diag}(1,i),$ the [Two-point kernel C](phase-kernel.md) $C=aI+bX$ satisfies $H_0=b\,\mathsf SC\mathsf S,$ $C^2=X$ and $C^4=I$ <cite data-source="paper">H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad</cite>. With $x_1,\dots,x_D$ the selected bits of an address $x,$ this gives $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D,$ where the diagonal operator $\mathcal S_D$ acts on an array $z$ by $(\mathcal S_Dz)(x)=i^{x_1+\dots+x_D}z(x).$ Here $z$ is an array, not an address suffix as on [Fast address-chunk interchange](address-interchange.md), and $z$ is not a binary vector as on [Binary phase frames](phase-frames.md). Phases and $b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}$ are exact Gaussian dyadic, leaving $C^{\otimes D}.$

A group of $e=mf$ selected axes ($e$ is the number of selected axes, not the number of digits in a chunk as on [Fast address-chunk interchange](address-interchange.md)) has $m$ slots of $f$ axes; a column holds one bit per slot, in $\mathbb F_2^m.$ $C^{\otimes e}$ is computed by the network of [Binary phase frames](phase-frames.md), with $W$ wires and $s$ smaller calls. Each edge changes the frame on every column by $\prod_\xi C_{v_\xi}^{\eta_\xi},$ with residual basis vectors $v_\xi$ indexed by $\xi,$ $\eta_\xi=\pm1,$ $C_v=aI+bX_v$ and $X_v$ shifting a column by $v.$ Let $\Gamma$ be an invertible $\mathbb F_2$-matrix with first columns $v_\xi$ and $\mathcal P_\Gamma:x\mapsto\Gamma x$ an address permutation. Then $\mathcal P_\Gamma X_v\mathcal P_\Gamma^{-1}=X_{\Gamma v}$ <cite data-source="paper">\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}.</cite>, so the edge change is $\mathcal P_\Gamma(\prod_\xi C_{\mathbf 1_\xi}^{\eta_\xi})\mathcal P_\Gamma^{-1},$ $\mathbf 1_\xi$ the $\xi$-th standard basis vector. Apply $\mathcal P_\Gamma^{-1},$ then $(C^{\eta_\xi})^{\otimes f}$ to the $f$ bits of slot $\xi,$ then $\mathcal P_\Gamma:$ one child on $f=e/m$ axes per residual vector, exactly $s$ in all. Negative powers add no child: $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$ with $Z=\operatorname{diag}(1,-1).$

Elimination writes $\Gamma$ as at most $m(m-1)+3m$ row additions (a swap is three). Each XORs selected bits of one slot into another; [Packed selected-bit addition](packed-bit-addition.md) XORs selected bits by cyclic shifts of whole chunk ranges plus a repair of exceptional addresses. Their number is fixed, so the basis change and its inverse on $e$ axis chunks cost $O(V((eK)^\tau+1))$ <cite data-source="paper">O(V((eK)^\tau+1))</cite> $(\tau<1)$ on a stream of volume $V.$

Rows go to the $W$ wire roles by index mod $W,$ so children have volume $V/W$ if the row count stays divisible by $W$ through $\lceil\log_md\rceil$ levels. So the first $q_0=\lceil\log_2W\rceil\lceil\log_m(2d)\rceil$ chunks get individual $C$ kernels, in $O(V\log d),$ and their bits form a row index of range at least $W^{\lceil\log_md\rceil}.$ Zero rows pad each block to a multiple of that, making the row count at depth $j$ divisible by $W^{\lceil\log_md\rceil-j};$ fewer rows are added than the block holds, so the volume at most doubles. With $\beta=\tfrac12$ and $F(e)$ the time divided by volume,
$$F(e)\le \tfrac sW F(e/m)+O((eK)^\tau+1)\ (e\ge d^\beta),\qquad F(e)=O(e)\ (e<d^\beta),$$
The layer obeys the recursion of [Recursive power saving](rank-recurrence.md). As $s/W\le m^\sigma,$ $\sigma<1,$ internal levels sum geometrically, leaves add $O(e^\sigma d^{\beta(1-\sigma)}),$ and $\log d$ pieces give $O(d^{\lambda'}).$ The paper's choice $\lambda'=1-2^{-54}$ <cite data-source="paper">\lambda'=1-2^{-54},</cite>, barely beats $D$ passes.

The layer is evaluated in [Fixed-point Gaussian dyadic records](fixed-point.md). Let $\chi(e)$ bound the operations on a chain from an input to an intermediate coefficient ($E$ below is an operation bound, not the first tensor factor of [Tensor products of subspaces](tensor-product-of-spaces.md); $E$ is likewise not the edge residual of the phase frames page). An invocation has at most $12W$ gates, each taking at most $2W^2$ operations (each output sums at most $W$ terms); inverse-child corrections take at most $4s,$ other corrections $4W+4.$ As $s<Wm,$ the total $24W^3+4s+4W+4$ is below $E=64(W+m+1)^3.$ Chains concatenate the $s$ children; a leaf pair takes eight operations:
$$\chi(e)\le s\chi(e/m)+E,\qquad \chi(e)\le8e\ (\text{leaf}).$$
With $\Psi=s+E,$ $s\varphi+E\le\Psi\varphi$ for any bound $\varphi\ge1,$ so $\chi(e)\le8d\Psi^{\lceil\log_md\rceil+1}.$ With $\vartheta=\min\{j\ge1:m^j\ge\Psi\}$ (an exponent of $m,$ not a digit count), $\Psi^{\lceil\log_md\rceil+1}\le\Psi^{\log_md+2}=\Psi^2d^{\log_m\Psi}\le\Psi^2d^\vartheta,$ so $\chi(e)\le8\Psi^2d^{\vartheta+1}.$ The at most $md$ pieces add $8m\Psi^2d^{\vartheta+2},$ individual kernels $8d,$ diagonals and $b^D$ at most $\lfloor D/2\rfloor+9.$ The total is at most $8m\Psi^2d^{\vartheta+2}+18d<128m\Psi^2d^{\vartheta+3}\le\Delta=\lceil C_0d^{C_1}\rceil,$ with $C_0=128m\Psi^2,$ $C_1=\max\{20,\vartheta+3\}.$

A depth-$\ell$ value lies in $2^{-(p+\ell)}\mathbb Z[i]$ with modulus at most $2^\ell,$ since addition at most doubles modulus and halving adds a denominator bit. So $p+\Delta$ fractional and $\Delta+3$ integer and sign bits per real component represent every intermediate coefficient exactly <cite data-source="paper">represents every intermediate coefficient exactly and prevents overflow</cite>. As $d=\Theta(p^\epsilon)$ and $\epsilon C_1<1,$ $\Delta=o(p):$ the width is $O(p).$

Absolute row sums multiply under tensor products, so each row of $\mathcal H=H_0^{\otimes D}$ has absolute row sum one. Hence $\mathcal H$ maps disk arrays to disk arrays <cite data-source="paper">absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk</cite>. Truncation toward zero cannot increase a component's absolute value and changes it by less than $2^{-p},$ so $Q_p$ keeps the disk, with $\|Q_p(\mathcal Hz)-\mathcal Hz\|_\infty<\sqrt2\,2^{-p}$ <cite data-source="paper">truncation cannot increase the absolute value of either component</cite>.

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

Write the body to `exegenius/tasks/0381-write-simultaneous-layer.answer.md` and the JSON to `exegenius/tasks/0381-write-simultaneous-layer.answer.json`, then run `exegenius submit 0381-write-simultaneous-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0381-write-simultaneous-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
