# exegenius task 0111-write-simultaneous-layer

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
- Fast address-chunk interchange (also: chunk swap, tape interchange)
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

- $y$ (ring variable), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The indeterminate of the polynomials, satisfying y^r = -1 in the ring.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The number of complex coefficients in a polynomial of the ring, always a power of two.
- $n$ (bit length), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): The number of bits in each of the two integers being multiplied.
- $\kappa$ (saving exponent), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant by which the exponent of the logarithm in the running time is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the stored grid, so values are integers divided by 2^p.
- $k$ (operation count), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations applied since the layer began.
- $\Delta$ (extra reserved bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the number of operations charged to the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The single truncation that drops the bits below 2^{-p} in each real and imaginary part.
- $h$ (ground-set size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of the ground set $[h]$ whose three-element subsets index the banks.
- $v$ (number of triples), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of three-element subsets of $[h]$.
- $N$ (bank size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of wires in each data bank.
- $m$ (label-space dimension), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The dimension of the label space used later.
- $I$ (invocation count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of invocations.
- $z_{\rm b}$ (bit neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the bit construction.
- $z_{\rm c}$ (complex neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the complex construction.
- $c_{\rm b}$ (bit central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the bit network.
- $W_{\rm c}$ (complex wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the complex network.
- $R$ (scalar ring), bound on [Frames on wire arrays](array-frames.md): The ring of scalars carried by the wires.
- $\Omega$ (address set), bound on [Frames on wire arrays](array-frames.md): A finite set of addresses indexing every wire's array.
- $\mathsf S_\Omega$ (pointwise network), bound on [Frames on wire arrays](array-frames.md): The network obtained by applying every scalar gate pointwise at each address, acting on all wire arrays together.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): An invertible R-linear operator on R^Omega assigned to a source, gate or sink v.
- $D_{\rm in}$ (input frame), bound on [Frames on wire arrays](array-frames.md): The direct sum of the source frames over the input roles.
- $D_{\rm out}$ (output frame), bound on [Frames on wire arrays](array-frames.md): The direct sum of the sink frames over the output roles.
- $\rho$ (role permutation), bound on [Frames on wire arrays](array-frames.md): The map sending each input role to its output role in a signed role permutation.
- $\varepsilon_w$ (route sign), bound on [Frames on wire arrays](array-frames.md): The scalar sign of the route from input role w.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each of the two sequences being convolved.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of axis i of the array.
- $M$ (cyclic addresses), bound on [Cyclic convolution](convolution.md): The number of cyclic addresses on the first d-1 axes, the product of t_i for i<d.
- $T$ (total coefficients), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array, rM.
- $u$ (first input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The first of the two integers being multiplied.
- $v$ (second input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The second of the two integers being multiplied.
- $n$ (input bit length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in each input.
- $b$ (digit width), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in one radix digit.
- $T$ (padded length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): A power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The length of the cyclic convolution, a product of distinct odd primes with T/2 < S < T.
- $q$ (digit count), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of radix-2^b digits in each input.
- $u_i$ (digit of u), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The i-th radix-2^b digit of u, an integer below 2^b.
- $v_k$ (digit of v), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The k-th radix-2^b digit of v, an integer below 2^b.
- $x$ (polynomial variable), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The variable of the digit polynomials, evaluated at 2^b to recover the integers.
- $c_j$ (product coefficient), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The coefficient of x^j in the product of the digit polynomials.
- $x_d$ (last-axis variable), bound on [Phase twist](phase-twist.md): The variable of the last cyclic axis, with x_d^r = 1.
- $\zeta$ (twist phase), bound on [Phase twist](phase-twist.md): The number e^{\pi i/r}, a primitive 2r-th root of unity with \zeta^r = -1.
- $\Theta$ (twist map), bound on [Phase twist](phase-twist.md): The ring isomorphism from C[x_d]/(x_d^r-1) to the negacyclic ring sending x_d to \zeta y.
- $d$ (number of axes), bound on [Phase twist](phase-twist.md): The number of axes of the array f.
- $T$ (total entries), bound on [Phase twist](phase-twist.md): The number of entries of the array f in all.
- $M$ (number of records), bound on [Phase twist](phase-twist.md): The number of lines along the last axis, T/r.
- $\iota$ (record identification), bound on [Phase twist](phase-twist.md): Reads each line along the last axis as a polynomial in the negacyclic ring.
- $D_\pm$ (diagonal twist), bound on [Phase twist](phase-twist.md): Multiplies entry k of each line by \zeta^{\pm k}.
- $\mathcal M_r$ (ring convolution), bound on [Phase twist](phase-twist.md): The ring convolution that convolves the first d-1 axes over the negacyclic ring and includes the division by T.
- $\mathcal M_{\mathbb C}$ (normalized cyclic convolution), bound on [Phase twist](phase-twist.md): The composite D_-\iota^{-1}\mathcal M_r(\iota D_+ f,\iota D_+ g), equal to f*g/T.
- $q$ (sequence length), bound on [Discrete Fourier transform](dft.md): The number of complex entries in the sequences the transform acts on.
- $u$ (input sequence), bound on [Discrete Fourier transform](dft.md): A sequence of q complex numbers to which the transform is applied.
- $\omega$ (root of unity), bound on [Discrete Fourier transform](dft.md): The primitive q-th root of unity e^{2 pi i/q} whose powers are the transform weights.
- $t$ (transform length), bound on [Butterflies and the fast transform](butterfly.md): The number of values in the transform, a power of two.
- $z_k$ (input values), bound on [Butterflies and the fast transform](butterfly.md): The input value at position k, for 0 <= k < t.
- $k$ (input position), bound on [Butterflies and the fast transform](butterfly.md): The position of an input value, 0 <= k < t.
- $\omega_t$ (root of unity), bound on [Butterflies and the fast transform](butterfly.md): The primitive t-th root of unity e^{2 pi i/t}.
- $b$ (lowest output bit), bound on [Butterflies and the fast transform](butterfly.md): The lowest bit of the output index, 0 or 1.
- $h$ (remaining output index), bound on [Butterflies and the fast transform](butterfly.md): The output index with its lowest bit removed.
- $t$ (transform length), bound on [Synthetic polynomial transform](synthetic-transform.md): The number of ring elements along one axis of the transform, a power of two dividing 2r.
- $\omega_t$ (ring root of unity), bound on [Synthetic polynomial transform](synthetic-transform.md): The power y^{2r/t} of the ring variable, used as the root of unity of the length-t synthetic transform.
- $V$ (array volume), bound on [Elementary stream operations](stream-ops.md): The number of radix-q digits stored in the array.
- $q$ (radix), bound on [Elementary stream operations](stream-ops.md): The number of values one digit can take.
- $W$ (number of streams), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams into which whole rows are dealt cyclically.
- $d$ (number of axes), bound on [Bluestein chirp identity](chirp.md): The number of axes (coordinates) of an index.
- $t_i$ (axis length), bound on [Bluestein chirp identity](chirp.md): The even number of entries along axis i.
- $s_i$ (coprime integer), bound on [Bluestein chirp identity](chirp.md): An integer coprime to t_i, scaling the frequency read along axis i.
- $T$ (total entries), bound on [Bluestein chirp identity](chirp.md): The total number of entries, the product of the t_i.
- $Q$ (target permutation), bound on [Bluestein chirp identity](chirp.md): The target permutation, reading frequency (-s_i j_i)_i at output position j.
- $a$ (chirp), bound on [Bluestein chirp identity](chirp.md): The chirp, a quadratic-phase array exp(-pi i sum s_i j_i^2/t_i).
- $t$ (transform length), bound on [Retained frequency order](frequency-order.md): The number of ring elements transformed along one axis, a power of two dividing 2r.
- $a$ (number of rounds), bound on [Retained frequency order](frequency-order.md): The number log_2 t of rounds of the fast algorithm.
- $\omega_t$ (root of unity), bound on [Retained frequency order](frequency-order.md): The power y^{2r/t} of the ring variable used as the t-th root of unity.
- $H_0$ (two-point butterfly), bound on [Retained frequency order](frequency-order.md): The 2x2 matrix (1/2)[[1,1],[1,-1]] applied to each pair of entries.
- $B_t$ (bit-reversal permutation), bound on [Retained frequency order](frequency-order.md): The permutation of records moving the entry at j to rev_a(j).
- $\mathcal H$ (parallel butterfly), bound on [Retained frequency order](frequency-order.md): The butterfly layer applying H_0 on every participating axis at once.
- $J_E$ (recordwise monomial), bound on [Retained frequency order](frequency-order.md): The operation multiplying the record at each address by y^E.
- $u_i$ (current length), bound on [Retained frequency order](frequency-order.md): The current recursive length of axis i.
- $b_i$ (branch bit), bound on [Retained frequency order](frequency-order.md): The newly written branch bit of axis i.
- $k_i$ (encoded index), bound on [Retained frequency order](frequency-order.md): The index encoded by the still unprocessed slots of axis i.
- $N$ (bit length), bound on [Established O(n log n) multiplier](hvdh-multiplier.md): The number of bits in each of the two integers being multiplied.
- $p$ (precision bits), bound on [Signed packing](signed-packing.md): The number of fractional bits in each coefficient component.
- $B_0$ (packing base), bound on [Signed packing](signed-packing.md): The power of two $2^{4p}$ at which the polynomials are evaluated.
- $A_u$ (evaluation integer), bound on [Signed packing](signed-packing.md): The signed integer obtained by evaluating the polynomial u at B_0.
- $H_j$ (numerator coefficient), bound on [Signed packing](signed-packing.md): The Gaussian integer coefficient of y^j after reduction modulo y^r+1.
- $q$ (prime), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The prime base of the field arithmetic.
- $b$ (field digits), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of base-$q$ digits of a field.
- $Q$ (field size), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of values a field can hold, Q = q^b.
- $V$ (array volume), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of stored data bits in the array.
- $a$ (offset), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The offset added to the target field, prepared from the control values.
- $B$ (suffix length), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of bits following the target field.
- $c$ (scaling integer), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed positive integer prime to q by which the target is multiplied.
- $A$ (shear matrix), bound on [Matrix shear by triangular factorization](matrix-shear.md): The fixed rational m by m matrix whose action AD is added to H.
- $m$ (fields per group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of fields in each of the groups H and D.
- $a$ (rank), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rank of the matrix A.
- $H$ (H group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The ordered group of m fields H_1..H_m that receives the update.
- $D$ (D group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The ordered group of m fields D_1..D_m that is added into H.
- $q$ (base prime), bound on [Matrix shear by triangular factorization](matrix-shear.md): A fixed odd prime; fields are residues modulo q^b.
- $b$ (digits per field), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of base-q digits in a field.
- $V$ (data volume), bound on [Matrix shear by triangular factorization](matrix-shear.md): The volume of data being processed.
- $E_1$ (left factor), bound on [Matrix shear by triangular factorization](matrix-shear.md): An invertible lower triangular factor of A.
- $E_2$ (right factor), bound on [Matrix shear by triangular factorization](matrix-shear.md): An invertible lower triangular factor of A.
- $\Pi$ (partial permutation), bound on [Matrix shear by triangular factorization](matrix-shear.md): A matrix with exactly a ones, at most one per row and column, and zeros elsewhere.
- $i$ (row index), bound on [Matrix shear by triangular factorization](matrix-shear.md): The row of a one of Pi.
- $j$ (column index), bound on [Matrix shear by triangular factorization](matrix-shear.md): The column of a one of Pi.
- $h$ (value of H_i), bound on [Matrix shear by triangular factorization](matrix-shear.md): The initial value of the field H_i.
- $d$ (value of D_j), bound on [Matrix shear by triangular factorization](matrix-shear.md): The initial value of the field D_j.
- $X$ (bit flip), bound on [Two-point kernel C](phase-kernel.md): The 2x2 matrix that swaps the two entries of a pair.
- $a$ (kernel coefficient a), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1+i)/2, the coefficient of I in C.
- $b$ (kernel coefficient b), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1-i)/2, the coefficient of X in C.
- $C$ (two-point kernel), bound on [Two-point kernel C](phase-kernel.md): The matrix aI + bX, a square root of the bit flip.
- $\mathsf S$ (phase matrix), bound on [Two-point kernel C](phase-kernel.md): The diagonal matrix diag(1, i) that multiplies the second entry of a pair by i.
- $H_0$ (butterfly matrix), bound on [Two-point kernel C](phase-kernel.md): The matrix of the averaging and differencing step (u,v) -> ((u+v)/2, (u-v)/2).
- $d$ (number of axes), bound on [Multidimensional transforms](multidim-transform.md): The number of axes (coordinates) of the array.
- $q_i$ (axis length), bound on [Multidimensional transforms](multidim-transform.md): The number of positions along axis i.
- $N$ (number of entries), bound on [Multidimensional transforms](multidim-transform.md): The number of entries of the array, the product of the axis lengths.
- $S$ (convolution length), bound on [Chinese-remainder address map](crt-map.md): The length of the cyclic convolution, the product of the axis lengths.
- $s_i$ (axis length), bound on [Chinese-remainder address map](crt-map.md): The length of axis i; the lengths are pairwise coprime.
- $d$ (number of axes), bound on [Chinese-remainder address map](crt-map.md): The number of axes.
- $P_i$ (prefix product), bound on [Chinese-remainder address map](crt-map.md): The product of the lengths of axes before axis i.
- $\mu_i$ (axis exponent), bound on [Chinese-remainder address map](crt-map.md): The inverse of P_i modulo s_i.
- $x_i$ (axis variable), bound on [Chinese-remainder address map](crt-map.md): The variable of axis i in the target ring.
- $a_j$ (mixed-radix digit), bound on [Chinese-remainder address map](crt-map.md): The j-th mixed-radix digit of the index k.
- $b_i$ (axis coordinate), bound on [Chinese-remainder address map](crt-map.md): The axis-i coordinate of the image of x^k.
- $t_i$ (padded length), bound on [Chinese-remainder address map](crt-map.md): The padded length of axis i, a power of two at least s_i.
- $\ell$ (axis bit width), bound on [Chinese-remainder address map](crt-map.md): The number of bits of the widest axis.
- $T$ (padded array size), bound on [Chinese-remainder address map](crt-map.md): The number of records in the padded array.
- $p$ (record precision), bound on [Chinese-remainder address map](crt-map.md): The number of bits of precision per record.
- $\tau$ (chunk-swap exponent), bound on [Chinese-remainder address map](crt-map.md): The fixed exponent in (0,1) governing the cost of a chunk interchange.
- $s$ (prime length), bound on [Gaussian resampling](gaussian-resampling.md): The prime length of the Fourier transform to be resampled, the number of complex coordinates it acts on.
- $t$ (power-of-two length), bound on [Gaussian resampling](gaussian-resampling.md): The power-of-two length of the nearby transform, the number of complex coordinates it acts on.
- $p$ (precision bits), bound on [Gaussian resampling](gaussian-resampling.md): The number of bits of precision of each real and imaginary component.
- $\alpha$ (Gaussian parameter), bound on [Gaussian resampling](gaussian-resampling.md): An integer with 2 <= alpha < sqrt p that sets the Gaussian width.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): The relative gap t/s - 1 between t and s, assumed larger than p/alpha^4.
- $k$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): An index of a coordinate of a vector in C^t, taken modulo t.
- $d$ (number of axes), bound on [Retained permutation cancellation](retained-permutations.md): The number of coordinate axes.
- $s_i$ (prime length), bound on [Retained permutation cancellation](retained-permutations.md): The prime length of axis i.
- $t_i$ (power-of-two length), bound on [Retained permutation cancellation](retained-permutations.md): The power-of-two length of axis i.
- $S$ (product of prime lengths), bound on [Retained permutation cancellation](retained-permutations.md): The product of the prime lengths.
- $T$ (padded box size), bound on [Retained permutation cancellation](retained-permutations.md): The number of entries in the padded box, the product of the power-of-two lengths.
- $p$ (bit precision), bound on [Retained permutation cancellation](retained-permutations.md): The number of bits of precision of each coordinate.
- $\alpha$ (Gaussian width), bound on [Retained permutation cancellation](retained-permutations.md): An integer width parameter of the Gaussian weights.
- $\delta$ (time exponent), bound on [Retained permutation cancellation](retained-permutations.md): A fixed exponent in the time bound.
- $R$ (source permutation), bound on [Retained permutation cancellation](retained-permutations.md): The source coordinate permutation, tensor product of the one-axis permutations P_{s_i}.
- $Q$ (target permutation), bound on [Retained permutation cancellation](retained-permutations.md): The target coordinate permutation, tensor product of the one-axis permutations P_{t_i}.
- $w$ (chunk width), bound on [Retained permutation cancellation](retained-permutations.md): The width in bits of the chunks swapped.
- $V$ (total bits), bound on [Retained permutation cancellation](retained-permutations.md): The total number of bits within which chunks are swapped.
- $\tau$ (chunk-swap exponent), bound on [Retained permutation cancellation](retained-permutations.md): The fixed exponent below 1 in the chunk-swap time bound.
- $b$ (digit width), bound on [Error tracking and exact recovery](precision-recovery.md): The number of bits in a radix digit.
- $p$ (fractional bits), bound on [Error tracking and exact recovery](precision-recovery.md): The number of fractional bits of the fixed-point grid, equal to $6b$.
- $T$ (padded array size), bound on [Error tracking and exact recovery](precision-recovery.md): The number of records in the padded array.
- $S$ (convolution length), bound on [Error tracking and exact recovery](precision-recovery.md): The length of the cyclic convolution.
- $L$ (log of T), bound on [Error tracking and exact recovery](precision-recovery.md): The base-2 logarithm of $T$.
- $\gamma$ (source scale exponent), bound on [Error tracking and exact recovery](precision-recovery.md): The exponent of the source-transform scale $2^\gamma$.
- $d$ (axis count), bound on [Error tracking and exact recovery](precision-recovery.md): The number of transform axes.
- $h_p$ (grid step), bound on [Error tracking and exact recovery](precision-recovery.md): The grid step $2^{-p}$.
- $\ell$ (log of r), bound on [Error tracking and exact recovery](precision-recovery.md): The base-2 logarithm of the record length $r$.
- $M$ (ring record count), bound on [Error tracking and exact recovery](precision-recovery.md): The ratio $T/r$, the number of ring records.
- $q$ (digit count), bound on [Error tracking and exact recovery](precision-recovery.md): The number of radix digits of an $n$-bit input.
- $Q_0$ (radix), bound on [Error tracking and exact recovery](precision-recovery.md): The radix $2^b$ of the digits.
- $n$ (input bits), bound on [Parameter and prime-length choice](parameter-choice.md): The number of bits of each of the two input integers.
- $d$ (number of axes), bound on [Parameter and prime-length choice](parameter-choice.md): The number of axes of the padded box.
- $T$ (padded box size), bound on [Parameter and prime-length choice](parameter-choice.md): The number of positions of the padded box.
- $t_i$ (axis length), bound on [Parameter and prime-length choice](parameter-choice.md): The length of axis i of the padded box.
- $\epsilon$ (axis-count exponent), bound on [Parameter and prime-length choice](parameter-choice.md): Fixed exponent setting the number of axes.
- $c$ (chunk-width exponent), bound on [Parameter and prime-length choice](parameter-choice.md): Fixed exponent setting the chunk width.
- $\lambda'$ (layer cost exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The cost exponent of a butterfly layer.
- $\kappa$ (saving exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The saving exponent of the final running time.
- $\tau$ (lemma constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed rational constant entering the lemmas inequalities.
- $\sigma$ (lemma constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed rational constant entering the lemmas inequalities.
- $\beta$ (lemma constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed rational constant entering the lemmas inequalities.
- $\delta$ (lemma constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed rational constant entering the lemmas inequalities.
- $\lambda$ (lemma constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed rational constant entering the lemmas inequalities.
- $C_1$ (lemma constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed rational constant entering the lemmas inequalities.
- $b$ (bit length), bound on [Parameter and prime-length choice](parameter-choice.md): The bit length of n.
- $K$ (chunk width), bound on [Parameter and prime-length choice](parameter-choice.md): The address-chunk width in bits.
- $\ell$ (address bits), bound on [Parameter and prime-length choice](parameter-choice.md): The number of address bits of the longest axis.
- $p$ (precision), bound on [Parameter and prime-length choice](parameter-choice.md): The precision in bits, setting the 2^{-p} grid of the fixed-point records.
- $a_d$ (comparison constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed constant with which the lemmas bound d, r and l.
- $a_r$ (comparison constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed constant with which the lemmas bound d, r and l.
- $b_d$ (comparison constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed constant with which the lemmas bound d, r and l.
- $b_r$ (comparison constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed constant with which the lemmas bound d, r and l.
- $C_\ell$ (comparison constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed constant with which the lemmas bound d, r and l.
- $\alpha$ (Gaussian width), bound on [Parameter and prime-length choice](parameter-choice.md): The width of the Gaussian weights in the resampling.
- $\gamma$ (total scaling), bound on [Parameter and prime-length choice](parameter-choice.md): The total scaling of the Gaussian weights over the axes.
- $\eta$ (relative gap), bound on [Parameter and prime-length choice](parameter-choice.md): The relative gap of each prime below its power of two.
- $x$ (interval scale), bound on [Parameter and prime-length choice](parameter-choice.md): A real number, the scale of the prime interval.
- $q$ (candidate), bound on [Parameter and prime-length choice](parameter-choice.md): An integer in the prime interval.
- $s_i$ (prime axis length), bound on [Parameter and prime-length choice](parameter-choice.md): The prime axis length of axis i near t_i.
- $S$ (convolution length), bound on [Parameter and prime-length choice](parameter-choice.md): The product of the s_i, the cyclic convolution length.
- $\theta_i$ (relative gap), bound on [Parameter and prime-length choice](parameter-choice.md): The relative gap t_i/s_i - 1 of axis i.
- $m$ (label-space dimension), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The dimension of the ambient label space, $m=h^3=10^6$.
- $W$ (wire count), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of wires of the network under consideration.
- $s$ (number of smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total number of smaller calls that the network's edges cost.
- $h$ (ground-set size), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The size of the ground set whose three-element subsets index the network, $h=100$.
- $F$ (one-factor label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space $\mathbb Q^h$ (bit network) or $\mathbb F_2^h$ (complex network) with its bilinear form.
- $t_T$ (triple indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator vector in $F$ of a triple $T$.
- $\mathcal F$ (ambient label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space $F^{\otimes3}$ of $h\times h\times h$ arrays, of dimension $m$, in which all labels lie.
- $N$ (bank size), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of index tuples $a$ of triples, so the number of wires in each data bank.
- $U_a$ (terminal line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$, the source label of $X_a$.
- $L$ (total dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on decreasing edges.
- $j$ (stage number), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The stage, 1, 2 or 3, whose invocations vary coordinate $a_j$.
- $A$ (exposed factor space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The tensor product $F^{\otimes(j-1)}$ of the factors already exposed before stage $j$.
- $P$ (earlier tensor line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
- $B$ (complement of P), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The orthogonal complement of $P$ inside $A$.
- $K$ (later tensor line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
- $I$ (invocation count), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of invocations over all three stages.
- $\gamma$ (central wires per invocation), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of central wires in one invocation: 100 in the bit network, 101 in the complex one.
- $\Pi_U$ (projection onto a label), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The rational projection onto the label $U$ along $U^\perp$, the matrix given to a bit-network vertex labelled $U$.
- $f$ (call parameter), bound on [Recursive power saving](rank-recurrence.md): The parameter of a call: the number of digits in each of the two interchanged chunks, or the number of axes the butterfly layer acts on.
- $V$ (volume), bound on [Recursive power saving](rank-recurrence.md): The volume of a call: the number of data symbols it processes.
- $m$ (block count), bound on [Recursive power saving](rank-recurrence.md): The number of size-f blocks into which a call at parameter mf cuts its parameter, equal to 10^6 (also the dimension of the label space).
- $W$ (wire count), bound on [Recursive power saving](rank-recurrence.md): The number of wires of the fixed network, and so the number of streams a call splits its data into.
- $s$ (number of smaller calls), bound on [Recursive power saving](rank-recurrence.md): The number of calls at parameter f made by a call at parameter mf: the total rank of the frame changes over all edges of the network.
- $F$ (normalized cost), bound on [Recursive power saving](rank-recurrence.md): F(f) is the running time of a call at parameter f divided by its volume.
- $k$ (recursion depth), bound on [Recursive power saving](rank-recurrence.md): The number of levels of recursion: the number of factors m in a parameter m^k.
- $\tau$ (saving exponent), bound on [Recursive power saving](rank-recurrence.md): A fixed exponent below 1 with s/W < m^tau, which makes a call cost O(V f^tau); here tau = 1 - 2^{-50}.
- $\eta$ (relative deficit), bound on [Recursive power saving](rank-recurrence.md): The fraction (Wm - s)/(Wm) by which the number of smaller calls s falls short of Wm.
- $u$ (chunk width), bound on [Fast address-chunk interchange](address-interchange.md): The number of bits in each of the two address chunks.
- $V$ (volume), bound on [Fast address-chunk interchange](address-interchange.md): The number of entries of the array.
- $\tau$ (time exponent), bound on [Fast address-chunk interchange](address-interchange.md): The fixed exponent below 1 in the time bound, 1-2^{-50}.
- $q$ (radix), bound on [Fast address-chunk interchange](address-interchange.md): The fixed prime used as digit radix.
- $H$ (first chunk), bound on [Fast address-chunk interchange](address-interchange.md): The value of the first chunk.
- $D$ (second chunk), bound on [Fast address-chunk interchange](address-interchange.md): The value of the second chunk.
- $e$ (chunk digits), bound on [Fast address-chunk interchange](address-interchange.md): The number of radix-q digits in each chunk.
- $m$ (fields per chunk), bound on [Fast address-chunk interchange](address-interchange.md): The number of fields each chunk is split into.
- $k$ (levels), bound on [Fast address-chunk interchange](address-interchange.md): The number of recursion levels, with e = m^k.
- $b$ (field width), bound on [Fast address-chunk interchange](address-interchange.md): The number of digits in each field.
- $W$ (wires), bound on [Fast address-chunk interchange](address-interchange.md): The number of wires of the exchange network.
- $A_\epsilon$ (edge matrix), bound on [Fast address-chunk interchange](address-interchange.md): The matrix attached to a network edge.
- $s$ (total edge rank), bound on [Fast address-chunk interchange](address-interchange.md): The sum of the ranks of the edge matrices.
- $\Phi_M$ (frame permutation), bound on [Fast address-chunk interchange](address-interchange.md): The address permutation moving the entry at (H,D) to (H+MD,D).
- $M$ (vertex matrix), bound on [Fast address-chunk interchange](address-interchange.md): The matrix attached to a network vertex, determining its frame.
- $f_w$ (wire input), bound on [Fast address-chunk interchange](address-interchange.md): The physical input array of wire w.
- $\sigma$ (role assignment), bound on [Fast address-chunk interchange](address-interchange.md): The map sending wire w to its role sigma(w).
- $F_k$ (cost per volume), bound on [Fast address-chunk interchange](address-interchange.md): A uniform upper bound on time divided by logical volume at width m^k.
- $k'$ (chunk level), bound on [Fast address-chunk interchange](address-interchange.md): The least integer with m^{k'} at least e, the recursion depth for width e.
- $\rho$ (high digits), bound on [Fast address-chunk interchange](address-interchange.md): The number of top digits of each chunk interchanged first.
- $R$ (row range), bound on [Fast address-chunk interchange](address-interchange.md): The range of the row field formed by the two high parts.
- $a_j$ (piece count), bound on [Fast address-chunk interchange](address-interchange.md): The number of pieces of width m^j in the base-m expansion of e minus rho.
- $m$ (address length), bound on [Binary phase frames](phase-frames.md): The number of binary coordinates of an address.
- $U$ (label), bound on [Binary phase frames](phase-frames.md): A subspace of the binary address space.
- $W_{\rm c}$ (complex wire count), bound on [Binary phase frames](phase-frames.md): The number of wires of the complex network.
- $k$ (column count), bound on [Binary phase frames](phase-frames.md): The number of columns, parallel copies of the array.
- $d$ (chunk bound), bound on [Packed selected-bit addition](packed-bit-addition.md): Maximum number of chunks a layer acts on.
- $c$ (control), bound on [Packed selected-bit addition](packed-bit-addition.md): Boolean control of the eight additions.
- $u$ (target integer), bound on [Packed selected-bit addition](packed-bit-addition.md): Integer whose parity is flipped by the eight additions.
- $w$ (auxiliary integer), bound on [Packed selected-bit addition](packed-bit-addition.md): Arbitrary auxiliary integer restored by the eight additions.
- $L$ (bits per chunk), bound on [Packed selected-bit addition](packed-bit-addition.md): Number of bits in each address chunk.
- $f$ (selected bits), bound on [Packed selected-bit addition](packed-bit-addition.md): Number of selected bits in each chunk.
- $K$ (spacing), bound on [Packed selected-bit addition](packed-bit-addition.md): Spacing between consecutive selected positions, which is also the bit length of a segment.
- $\rho$ (offset), bound on [Packed selected-bit addition](packed-bit-addition.md): Offset of the lowest selected position.
- $M$ (address count), bound on [Packed selected-bit addition](packed-bit-addition.md): Number of addresses.
- $R$ (record length), bound on [Packed selected-bit addition](packed-bit-addition.md): Number of bits in a record.
- $V$ (volume), bound on [Packed selected-bit addition](packed-bit-addition.md): Total number of bits, M times R.
- $A_{\rm rect}$ (counter length), bound on [Packed selected-bit addition](packed-bit-addition.md): Bit length of counters.
- $\tau$ (interchange exponent), bound on [Packed selected-bit addition](packed-bit-addition.md): Fixed exponent below one in the cost of the chunk interchange.
- $\mathcal B$ (exceptional set), bound on [Packed selected-bit addition](packed-bit-addition.md): Set of addresses where some guard fails the interval test.
- $S_0$ (packed map), bound on [Packed selected-bit addition](packed-bit-addition.md): Composition of the eight packed cyclic-shift lines.
- $\delta_{\rm bad}$ (bad fraction), bound on [Packed selected-bit addition](packed-bit-addition.md): Upper bound on the fraction of exceptional addresses.
- $p$ (coefficient precision), bound on [Packed selected-bit addition](packed-bit-addition.md): Bit precision of the record coefficients.

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
- [Retained frequency order](frequency-order.md)
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

- The reader cannot follow this step: "the overhead is $O(e^\lambda)$ for fixed $\max\{\tau,\sigma\}<\lambda<1.$" (The overhead is O((eK)^tau+1) with K<=d^c<=e^{c/beta}, i.e. O(e^{tau(1+c/beta)}). That is O(e^lambda) only if tau(1+c/beta)<lambda, which the paper requires (lines 2398-2399 and 2414-2415) but the page omits; max{tau,sigma}<lambda<1 alone does not give it. The page also never states K=floor(d^c).). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "So apply $\mathcal P_M^{-1}$ per column" (The page never states the edge identity that this recipe implements (frame change = P_M (prod C_{e_j}^{eta_j}) P_M^{-1}, paper eq. phase-edge-coordinate, lines 1855-1862), never defines X_v or C_v = aI+bX_v, and never explains the column vectors (x_{1,j},...,x_{m,j}) of the m slots on which P_M acts. The cited conjugation identity is thus not tied to the claim that follows.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Applying $C$ individually to the first $q_0=\lceil\log_2W\rceil\lceil\log_m(2d)\rceil$ chunks makes their bits a row index" (This requires D>q_0; the paper (lines 2313-2316) treats D<=q_0 separately by applying individual C kernels throughout, at cost O(V log d). The page states the row construction without that hypothesis and never explains why the row index range is large enough or why the cost of this preprocessing is within the bound.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "leaves add $O(\gamma^ju)\le O(e^\sigma u^{1-\sigma})\le O(e^\sigma d^{\beta(1-\sigma)}).$" (u and j are not defined on the page (paper lines 2421-2430: u=e/m^j<d^beta active chunks per leaf after j levels), so the reader cannot check the two inequalities, which use gamma^j<=m^{j sigma}=(e/u)^sigma and u<d^beta.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Base-$m$ pieces give" (The page never says that the remaining D-q_0 chunks are written in base m and split into at most (m-1)(1+floor(log_m d)) consecutive pieces of m^j chunks (paper lines 2432-2436), which is where the log(2d) factor comes from. The cited result cannot be followed without it.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "the saving is slight: $\lambda'=1-2^{-54}$ (cited)" (The value lambda'=1-2^{-54} depends on the fixed choices tau=sigma=1-2^{-50}, beta=1/2, c=2^{-56}, lambda=1-2^{-52} (paper lines 4010-4026), none of which except beta appears on the page, so the reader cannot check that max{lambda,sigma+beta(1-sigma)}<lambda'<1 holds. 's/W<m^sigma' alone does not give this value.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Chains satisfy $A(e)\le sA(e/m)+E,\ E=64(W+m+1)^3,$" (The page never says what A(e) or a chain is, nor derives the recurrence: the constant E=64(W+m+1)^3 comes from counting scalar gates (at most 12W gates, 2W^2 operations each), inverse-child and bank corrections (4s+4W+4) in paper lines 2490-2509, none of which is given. The recurrence has to be taken on trust.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "since $sx+E\le Bx$ for $B=s+E,$" (sx+E<=(s+E)x holds only for x>=1 (paper line 2524); the page omits the hypothesis. The step to A(e)<=8B^2 d^{nu+1} also needs the depth k<=ceil(log_m d) of the recursion, e<=d, and B^{k+1}<=B^2 d^{log_m B}<=B^2 d^nu (paper lines 2523-2534), none of which is given.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "So with $\Delta=\lceil C_0d^{C_1}\rceil,$ reserving" (C_0 and C_1 are never given. The bound A(e)<=8B^2 d^{nu+1} covers one group of e axes only; the paper (lines 2536-2560) adds the concatenated pieces (8mB^2 d^{nu+2}), preprocessing kernels, the outer diagonals and the scalar b^D to reach C_0=128mB^2, C_1=max{20,nu+3}. The page's Delta is therefore not shown to dominate the operation count.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "After $\ell$ operations a value lies in $2^{-(p+\ell)}\mathbb Z[i]$ with modulus at most $2^\ell$" (This holds only for values obtained from inputs in the unit disk lying on the grid 2^{-p}Z[i] (paper lines 2562-2565, by induction on depth); the page states it with no starting hypothesis and for 'operations' rather than depth along a dependency chain.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "row sums multiply under tensor products" (The conclusion is about absolute row sums. Ordinary row sums also multiply under tensor products, but the second row of H_0 has sum 0, so they would not give 1. The correct statement is that the absolute row sum of H_0 is 1 for each row (|1/2|+|+-1/2|) and absolute row sums multiply, so every row of H_0^{(x)D} has absolute row sum one (paper line 2751).). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Say what $u$ denotes where it is first used (for a size or count, what it counts): "leaves add $O(\gamma^ju)\le O(e^\sigma u^{1-\sigma})" (In the leaf bound u is used without saying what it denotes (in the paper it is e/m^j, the number of active chunks in a leaf after j levels); only in H_0(u,v) is it a dummy argument.)
- Say what $z$ denotes where it is first used (for a size or count, what it counts): "(\mathcal S_Dz)(x)=i^{x_1+\dots+x_D}z(x)" (The page never says z is the array of stored records (a function of the address) that the layer acts on.)
- Say what $X_v$ denotes where it is first used (for a size or count, what it counts): "$\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}$" (The page defines only X(u,v)=(v,u); it never says what X_v (the shift of the address by v, (X_v f)(x)=f(x+v)) is.)
- Say what $X_{Mv}$ denotes where it is first used (for a size or count, what it counts): "$\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}$" (Same as X_v: the operator X indexed by a vector is never defined.)
- Say what $g$ denotes where it is first used (for a size or count, what it counts): "row $Wg+w$" (The page does not say that g is the quotient and w the remainder (0<=w<W) of the row index modulo W, so the row-to-wire rule is not fully specified.)
- Say what $\lambda$ denotes where it is first used: the page uses it before saying so in "for fixed $\max\{\tau,\sigma\}<\lambda<1.$"
- Say what $\sigma$ denotes where it is first used (for a size or count, what it counts): "$\max\{\tau,\sigma\}<\lambda<1.$" (sigma is never introduced; the reader is not told it is a fixed exponent below 1 with s/W <= m^sigma.)
- Say what $c$ denotes where it is first used (for a size or count, what it counts): "As $K\le d^c\le e^{c/\beta},$" (The exponent c (K = floor(d^c)) is never introduced; the page does not even say K is tied to d.)
- Say what $G$ denotes where it is first used (for a size or count, what it counts): "$Ge^\lambda\sum_{j\ge0}" (G is never said to be a constant (the implied constant of the overhead).)
- Say what $A$ denotes where it is first used (for a size or count, what it counts): "Chains satisfy $A(e)\le sA(e/m)+E," (A(e) and the word chains are never defined (in the paper A(e) bounds the number of arithmetic operations on a dependency chain).)
- Say what $C_0$ denotes where it is first used (for a size or count, what it counts): "\Delta=\lceil C_0d^{C_1}\rceil" (C_0 is never given a value or role.)
- Say what $C_1$ denotes where it is first used (for a size or count, what it counts): "\Delta=\lceil C_0d^{C_1}\rceil" (C_1 is never given a value or role (paper: C_1=max{20,nu+3}, equal to 20 here).)
- Say what $\epsilon$ denotes where it is first used (for a size or count, what it counts): "For $d=\Theta(p^\epsilon),\ \epsilon C_1<1$" (epsilon is never introduced (paper: a fixed exponent with 0<epsilon<1 relating d to p).)

## Previous version (revise it)

It has 328 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 410 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

On a stream of $V$ bits, with address chunks of $K$ bits and coefficients of $p$ fractional bits, the simultaneous butterfly layer applies $H_0(u,v)=\bigl(\tfrac{u+v}2,\tfrac{u-v}2\bigr)$ to one bit in each of $D\le d$ chunks in time $O(Vd^{\lambda'}),\ \lambda'<1,$ instead of $D$ whole-array passes.

For $X(u,v)=(v,u),\ \mathsf S=\operatorname{diag}(1,i),$ the [two-point kernel](phase-kernel.md) is $C=aI+bX,\ a=\frac{1+i}2,\ b=\frac{1-i}2.$ Direct multiplication, using $\mathsf SI\mathsf S=\operatorname{diag}(1,-1),\ \mathsf SX\mathsf S=iX,\ ab=ib^2=\frac12,$ gives $H_0=b\,\mathsf SC\mathsf S,\ C^2=X,\ C^4=I$ <cite data-source="paper">H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad</cite>. For selected address bits $x_1,\dots,x_D,$ $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ and $(\mathcal S_Dz)(x)=i^{x_1+\dots+x_D}z(x),$ where phases and $b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}$ are exact Gaussian dyadic operations.

On $e=mf$ axes in $m$ slots of $f$ bits, $C^{\otimes e}$ is applied by the network of [Binary phase frames](phase-frames.md), whose edges are products of kernels $C^{\eta_h}$ along residual vectors $v_h\in\mathbb F_2^m,\ \eta_h=\pm1.$ For invertible $M$ with first columns $v_h,$ the address permutation $\mathcal P_M:x\mapsto Mx$ gives $\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}$ <cite data-source="paper">\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}.</cite> So apply $\mathcal P_M^{-1}$ per column, $(C^{\eta_h})^{\otimes f}$ to the $f$ bits of slot $h,$ then $\mathcal P_M$: one child per residual vector. Since $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f},\ Z=\operatorname{diag}(1,-1),$ negative kernels need no inverse child. Summing residual dimensions gives exactly $s$ children, each on $f=e/m$ axes.

Gaussian elimination writes $M$ as at most $m(m-1)+3m$ row additions, each XORing selected bits of two slots, done by [Packed selected-bit addition](packed-bit-addition.md). So the basis change and its inverse cost $O(V((eK)^\tau+1))$ <cite data-source="paper">O(V((eK)^\tau+1))</cite> for an exponent $\tau<1.$

Let $W$ be the network's wire count and $F(e)$ the time divided by volume. Applying $C$ individually to the first $q_0=\lceil\log_2W\rceil\lceil\log_m(2d)\rceil$ chunks makes their bits a row index; row $Wg+w$ goes to wire $w,$ so each child has volume $V/W.$ The recurrence, solved as in [Recursive power saving](rank-recurrence.md), is $F(e)\le\tfrac sWF(e/m)+O((eK)^\tau+1)\ (e\ge d^\beta),\ F(e)=O(e)\ (e<d^\beta),\ \beta=\frac12.$ As $K\le d^c\le e^{c/\beta},$ the overhead is $O(e^\lambda)$ for fixed $\max\{\tau,\sigma\}<\lambda<1.$ With $\gamma=s/W\le m^\sigma<m^\lambda,$ internal levels sum to $Ge^\lambda\sum_{j\ge0}(\gamma/m^\lambda)^j=O(e^\lambda)$ and leaves add $O(\gamma^ju)\le O(e^\sigma u^{1-\sigma})\le O(e^\sigma d^{\beta(1-\sigma)}).$ Base-$m$ pieces give $O(\log(2d)[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1])=O(d^{\lambda'})$ <cite data-source="paper">=O(d^{\lambda'})</cite> for $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1.$ As $s/W<m^\sigma,$ the saving is slight: $\lambda'=1-2^{-54}$ <cite data-source="paper">\lambda'=1-2^{-54},</cite>.

Chains satisfy $A(e)\le sA(e/m)+E,\ E=64(W+m+1)^3,$ and $A(e)\le8e$ at leaves; since $sx+E\le Bx$ for $B=s+E,$ $A(e)\le8B^2d^{\nu+1},\ \nu=\min\{j\ge1:m^j\ge B\}.$ After $\ell$ operations a value lies in $2^{-(p+\ell)}\mathbb Z[i]$ with modulus at most $2^\ell$: addition doubles modulus, halving adds a denominator bit. So with $\Delta=\lceil C_0d^{C_1}\rceil,$ reserving $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits per real component, as in [Fixed-point Gaussian dyadic records](fixed-point.md), represents every intermediate coefficient exactly. For $d=\Theta(p^\epsilon),\ \epsilon C_1<1$ gives $\Delta=o(p),$ so the width is $O(p).$

Rows of $H_0$ have entries $\pm\frac12$ and row sums multiply under tensor products, so every row of $\mathcal H=H_0^{\otimes D}$ has absolute row sum one and $\mathcal H$ maps disk arrays (coefficients in the unit disk) to disk arrays <cite data-source="paper">absolute row sum one.</cite> $Q_p$ truncates each real component toward zero, keeping the disk and changing each component by less than $2^{-p},$ so $\|Q_p(\mathcal Hz)-\mathcal Hz\|_\infty<\sqrt2\,2^{-p}$ <cite data-source="paper">truncation cannot increase the absolute value of either component</cite>.

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

Write the body to `exegenius/tasks/0111-write-simultaneous-layer.answer.md` and the JSON to `exegenius/tasks/0111-write-simultaneous-layer.answer.json`, then run `exegenius submit 0111-write-simultaneous-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0111-write-simultaneous-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
