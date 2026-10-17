# exegenius task 0034-write-simultaneous-layer

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
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Elementary stream operations](stream-ops.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Fast address-chunk interchange](address-interchange.md)
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
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Parameter and prime-length choice](parameter-choice.md)
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

Write the body to `exegenius/tasks/0034-write-simultaneous-layer.answer.md` and the JSON to `exegenius/tasks/0034-write-simultaneous-layer.answer.json`, then run `exegenius submit 0034-write-simultaneous-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0034-write-simultaneous-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
