# exegenius task 0308-write-phase-frames

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

Concept: Binary phase frames
Gloss: Frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} whose edge differences are products of translation kernels aI + bX_v, one per vector of an orthonormal residual basis.

## This page in the argument

The step: Complex network: with binary labels and the phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{\operatorname{wt}(P_Ux)\bmod 4})H^{\otimes m}$, every edge difference is a product of one translation kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal basis of the edge residual; the total number of kernels is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$ and, after endpoint corrections, the network applies $C^{\otimes m}$ on every role.
How: Use Hamming weight modulo 4 as the phase: on orthogonal binary vectors weights add modulo 4, so a frame difference along an orthonormal residual basis is a sum of single-vector phases, each of which is a translation kernel; the one pair $X_a\to Y_a$ with an inverse kernel on 27 coordinates is repaired using $C=iZC^{-1}Z$.
Why: Binary orthonormal bases turn a frame difference into independent two-point kernels, one per basis vector, so that each residual dimension is one smaller call of the same butterfly-type operation, as the recursion needs. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- For a label $U$ put $q_U(x)=\operatorname{wt}(P_Ux)\bmod 4$, with the projection taken over $\mathbb F_2$.
- The phase frame is $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$, with Gaussian-dyadic entries.
- The number of translation-kernel factors over the network is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}=1873807244636671267308000000<W_{\rm c}m$.
- For binary vectors $\operatorname{wt}(z+w)=\operatorname{wt}(z)+\operatorname{wt}(w)-2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|$.
- If $z\cdot w=0$ the intersection cardinality is even, so weight is additive modulo four on orthogonal vectors.
- For $V=U\perp E$ with orthonormal basis $\mathcal B$ of $E$: $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\operatorname{wt}(v)[v\cdot x]\pmod 4$ (negated on a decreasing edge), and each $\operatorname{wt}(v)$ is odd.
- The function $i^{\varepsilon[v\cdot x]}$ with $\varepsilon=\pm1$ equals $\frac{1+i^\varepsilon}2+\frac{1-i^\varepsilon}2(-1)^{v\cdot x}$.
- Since $H\operatorname{diag}(1,-1)H=X$, the character $(-1)^{v\cdot x}$ becomes the translation $X_v$, so the phase becomes $aI+bX_v$ or its inverse.
- The deficit of $s_{\rm c}$ from $W_{\rm c}m$ is $2N-2L_{\rm c}>0$.
- For the one exceptional pair $X_a\to Y_a$, with $u=u_a$ of binary norm one and weight $27$: $q_{U_a^\perp}-q_{U_a}=\operatorname{wt}(x)+2[u\cdot x]\pmod 4$, so the operator is $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u)$ and $C$ elsewhere.
- The identity $C=iZC^{-1}Z$ (with $Z=\operatorname{diag}(1,-1)$) turns each of the $27k$ inverse factors into $C$ after applying $Z_{a,k}$ before and $i^{27k}Z_{a,k}$ after, so every role, including scratch roles, receives $C^{\otimes mk}$.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- Both tape primitives (the interchange of two address chunks of $u$ digits and the simultaneous butterfly layer on up to $d$ axes) cost the volume times a power below one of their width, because a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$, so the cost per unit volume grows by $s/W<m$ per factor $m$ of the parameter.; how: Build a fixed finite linear network of $W$ wires that exchanges two banks and restores all scratch values, make the representation of each wire's array vary along the network through frames so that an edge costs one smaller call per unit of rank, show the total rank $s$ is below $Wm$, fix an exponent, and solve the recurrence in the bit variant (interchange) and the complex variant (butterfly layer). (on [Recursive power saving](rank-recurrence.md))
- Attaching to the gates nondegenerate subspaces of an $m$-dimensional space, nested along every edge, the number of smaller calls (the total rank of the edge changes) is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$ for the bit network and $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$ for the complex network, both strictly less than $Wm$, because $L/N<1/2$.; how: Choose labels in $\mathcal F=F^{\otimes3}$ built from the triple indicator vectors, with terminal labels $U_a\to\mathcal F$ on $X_a$ and $0\to U_a^\perp$ on $Y_a$; expose one tensor factor per stage; tabulate dimension changes edge by edge to find that all decreases are the central wires' return from time 3 to 4; then convert the dimension count into rational rank (bit) and Gaussian-dyadic phase kernels (complex). (on [Nested subspace labels and rank deficit](subspace-labels.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.3.8.1, S1.3.8.2, S1.3.8.3, S1.3.8.4, S1.3.8.5, S1.3.8.6, S1.3.8.7, S1.3.8.8, S1.3.8.9, S1.3.8.10, S1.3.8.11). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.3.8.1**: For a label $U$ put $q_U(x)=\operatorname{wt}(P_Ux)\bmod 4$, with the projection taken over $\mathbb F_2$.
Source: "q_U(x)=\operatorname{wt}(P_Ux)\pmod4." (paper)
> Use the complex scalar network and binary labels. For a binary vector $x$, let $\operatorname{wt}(x)$ denote its integer Hamming weight, and write $[b]\in\{0,1\}$ for the integer representative of $b\in\mathbb F_2$. For a label $U$, let \[ q_U(x)=\operatorname{wt}(P_Ux)\pmod4. \] The projection here is over $\mathbb F_2$. Let \[ H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad C=H\begin{pmatrix}1&0\\0&i\end{pmatrix}H =aI+bX,\qquad a=\frac{1+i}{2},\quad b=\frac{1-i}{2}, \] where $X$ interchanges the two coordinates. On functions of $x\in\mathbb F_2^m$ define \[ \mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}. \] The use of $H$ in this definition is an identity of matrices. Each entry of $\mathcal C_U$ and its inverse is a Gaussian integer divided by $2^m$, so both preserve arrays over $\mathbb Z[i,1/2]$. The kernels implemented below have Gaussian dyadic coefficients.

**S1.3.8.2**: The phase frame is $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$, with Gaussian-dyadic entries.
Source: "\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}." (paper)
> Use the complex scalar network and binary labels. For a binary vector $x$, let $\operatorname{wt}(x)$ denote its integer Hamming weight, and write $[b]\in\{0,1\}$ for the integer representative of $b\in\mathbb F_2$. For a label $U$, let \[ q_U(x)=\operatorname{wt}(P_Ux)\pmod4. \] The projection here is over $\mathbb F_2$. Let \[ H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad C=H\begin{pmatrix}1&0\\0&i\end{pmatrix}H =aI+bX,\qquad a=\frac{1+i}{2},\quad b=\frac{1-i}{2}, \] where $X$ interchanges the two coordinates. On functions of $x\in\mathbb F_2^m$ define \[ \mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}. \] The use of $H$ in this definition is an identity of matrices. Each entry of $\mathcal C_U$ and its inverse is a Gaussian integer divided by $2^m$, so both preserve arrays over $\mathbb Z[i,1/2]$. The kernels implemented below have Gaussian dyadic coefficients.

**S1.3.8.3**: The number of translation-kernel factors over the network is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}=1873807244636671267308000000<W_{\rm c}m$.
Source: "s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}" (paper)
> \begin{proposition}\label{prop:complex-motif-interface} For each edge of the complex network, write $U,V$ for its tail and head labels. Its phase-frame difference $\mathcal C_V\mathcal C_U^{-1}$ is a product of one translation kernel $aI+bX_v$, or its inverse, per vector in an orthonormal basis of the edge residual. Here $(X_vf)(x)=f(x+v)$. The sum of these basis lengths is \[ s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c} =1873807244636671267308000000<W_{\rm c}m. \] After source and sink diagonal corrections, and undoing the signed bank exchange, telescoping these phase frames gives $C^{\otimes m}$ on every role, including auxiliary roles. The same assertion holds on any positive number of columns by taking tensor products over columns. \end{proposition}

**S1.3.8.4**: For binary vectors $\operatorname{wt}(z+w)=\operatorname{wt}(z)+\operatorname{wt}(w)-2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|$.
Source: "=\operatorname{wt}(z)+\operatorname{wt}(w)" (paper)
> \begin{proof} For binary vectors $z,w$, \[ \operatorname{wt}(z+w) =\operatorname{wt}(z)+\operatorname{wt}(w) -2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|. \] If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four. If $V=U\mathbin{\perp}E$ and $\mathcal B$ is an orthonormal basis of $E$, it follows that \[ q_V(x)-q_U(x)=\sum_{v\in\mathcal B} \operatorname{wt}(v)[v\cdot x]\pmod4. \] For a decreasing edge the right side is negated. Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd. Its coefficient in the phase, including the sign for the edge direction, is therefore some $\varepsilon\in\{1,-1\}$ modulo four. The function $i^{\varepsilon[v\cdot x]}$ equals \[ \frac{1+i^\varepsilon}{2} +\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}. \] The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the coordinates in $\operatorname{supp}(v)$, sends the diagonal character $(-1)^{v\cdot x}$ to translation $X_v$. The displayed phase therefore becomes $aI+bX_v$ or its inverse. The nonzero residuals have such bases by Lemma~\ref{lem:motif-residuals}; for a zero residual use the empty basis. The same lemma gives the count $s_{\rm c}$. The deficit is $2N-2L_{\rm c}>0$.

**S1.3.8.5**: If $z\cdot w=0$ the intersection cardinality is even, so weight is additive modulo four on orthogonal vectors.
Source: "If $z\cdot w=0$, the intersection cardinality is even, so weight is" (paper)
> \begin{proof} For binary vectors $z,w$, \[ \operatorname{wt}(z+w) =\operatorname{wt}(z)+\operatorname{wt}(w) -2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|. \] If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four. If $V=U\mathbin{\perp}E$ and $\mathcal B$ is an orthonormal basis of $E$, it follows that \[ q_V(x)-q_U(x)=\sum_{v\in\mathcal B} \operatorname{wt}(v)[v\cdot x]\pmod4. \] For a decreasing edge the right side is negated. Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd. Its coefficient in the phase, including the sign for the edge direction, is therefore some $\varepsilon\in\{1,-1\}$ modulo four. The function $i^{\varepsilon[v\cdot x]}$ equals \[ \frac{1+i^\varepsilon}{2} +\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}. \] The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the coordinates in $\operatorname{supp}(v)$, sends the diagonal character $(-1)^{v\cdot x}$ to translation $X_v$. The displayed phase therefore becomes $aI+bX_v$ or its inverse. The nonzero residuals have such bases by Lemma~\ref{lem:motif-residuals}; for a zero residual use the empty basis. The same lemma gives the count $s_{\rm c}$. The deficit is $2N-2L_{\rm c}>0$.

**S1.3.8.6**: For $V=U\perp E$ with orthonormal basis $\mathcal B$ of $E$: $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\operatorname{wt}(v)[v\cdot x]\pmod 4$ (negated on a decreasing edge), and each $\operatorname{wt}(v)$ is odd.
Source: "q_V(x)-q_U(x)=\sum_{v\in\mathcal B}" (paper)
> \begin{proof} For binary vectors $z,w$, \[ \operatorname{wt}(z+w) =\operatorname{wt}(z)+\operatorname{wt}(w) -2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|. \] If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four. If $V=U\mathbin{\perp}E$ and $\mathcal B$ is an orthonormal basis of $E$, it follows that \[ q_V(x)-q_U(x)=\sum_{v\in\mathcal B} \operatorname{wt}(v)[v\cdot x]\pmod4. \] For a decreasing edge the right side is negated. Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd. Its coefficient in the phase, including the sign for the edge direction, is therefore some $\varepsilon\in\{1,-1\}$ modulo four. The function $i^{\varepsilon[v\cdot x]}$ equals \[ \frac{1+i^\varepsilon}{2} +\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}. \] The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the coordinates in $\operatorname{supp}(v)$, sends the diagonal character $(-1)^{v\cdot x}$ to translation $X_v$. The displayed phase therefore becomes $aI+bX_v$ or its inverse. The nonzero residuals have such bases by Lemma~\ref{lem:motif-residuals}; for a zero residual use the empty basis. The same lemma gives the count $s_{\rm c}$. The deficit is $2N-2L_{\rm c}>0$.

**S1.3.8.7**: The function $i^{\varepsilon[v\cdot x]}$ with $\varepsilon=\pm1$ equals $\frac{1+i^\varepsilon}2+\frac{1-i^\varepsilon}2(-1)^{v\cdot x}$.
Source: "$i^{\varepsilon[v\cdot x]}$ equals" (paper)
> \begin{proof} For binary vectors $z,w$, \[ \operatorname{wt}(z+w) =\operatorname{wt}(z)+\operatorname{wt}(w) -2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|. \] If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four. If $V=U\mathbin{\perp}E$ and $\mathcal B$ is an orthonormal basis of $E$, it follows that \[ q_V(x)-q_U(x)=\sum_{v\in\mathcal B} \operatorname{wt}(v)[v\cdot x]\pmod4. \] For a decreasing edge the right side is negated. Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd. Its coefficient in the phase, including the sign for the edge direction, is therefore some $\varepsilon\in\{1,-1\}$ modulo four. The function $i^{\varepsilon[v\cdot x]}$ equals \[ \frac{1+i^\varepsilon}{2} +\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}. \] The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the coordinates in $\operatorname{supp}(v)$, sends the diagonal character $(-1)^{v\cdot x}$ to translation $X_v$. The displayed phase therefore becomes $aI+bX_v$ or its inverse. The nonzero residuals have such bases by Lemma~\ref{lem:motif-residuals}; for a zero residual use the empty basis. The same lemma gives the count $s_{\rm c}$. The deficit is $2N-2L_{\rm c}>0$.

**S1.3.8.8**: Since $H\operatorname{diag}(1,-1)H=X$, the character $(-1)^{v\cdot x}$ becomes the translation $X_v$, so the phase becomes $aI+bX_v$ or its inverse.
Source: "The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the" (paper)
> \begin{proof} For binary vectors $z,w$, \[ \operatorname{wt}(z+w) =\operatorname{wt}(z)+\operatorname{wt}(w) -2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|. \] If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four. If $V=U\mathbin{\perp}E$ and $\mathcal B$ is an orthonormal basis of $E$, it follows that \[ q_V(x)-q_U(x)=\sum_{v\in\mathcal B} \operatorname{wt}(v)[v\cdot x]\pmod4. \] For a decreasing edge the right side is negated. Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd. Its coefficient in the phase, including the sign for the edge direction, is therefore some $\varepsilon\in\{1,-1\}$ modulo four. The function $i^{\varepsilon[v\cdot x]}$ equals \[ \frac{1+i^\varepsilon}{2} +\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}. \] The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the coordinates in $\operatorname{supp}(v)$, sends the diagonal character $(-1)^{v\cdot x}$ to translation $X_v$. The displayed phase therefore becomes $aI+bX_v$ or its inverse. The nonzero residuals have such bases by Lemma~\ref{lem:motif-residuals}; for a zero residual use the empty basis. The same lemma gives the count $s_{\rm c}$. The deficit is $2N-2L_{\rm c}>0$.

**S1.3.8.9**: The deficit of $s_{\rm c}$ from $W_{\rm c}m$ is $2N-2L_{\rm c}>0$.
Source: "The deficit is $2N-2L_{\rm c}>0$." (paper)
> \begin{proof} For binary vectors $z,w$, \[ \operatorname{wt}(z+w) =\operatorname{wt}(z)+\operatorname{wt}(w) -2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|. \] If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four. If $V=U\mathbin{\perp}E$ and $\mathcal B$ is an orthonormal basis of $E$, it follows that \[ q_V(x)-q_U(x)=\sum_{v\in\mathcal B} \operatorname{wt}(v)[v\cdot x]\pmod4. \] For a decreasing edge the right side is negated. Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd. Its coefficient in the phase, including the sign for the edge direction, is therefore some $\varepsilon\in\{1,-1\}$ modulo four. The function $i^{\varepsilon[v\cdot x]}$ equals \[ \frac{1+i^\varepsilon}{2} +\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}. \] The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the coordinates in $\operatorname{supp}(v)$, sends the diagonal character $(-1)^{v\cdot x}$ to translation $X_v$. The displayed phase therefore becomes $aI+bX_v$ or its inverse. The nonzero residuals have such bases by Lemma~\ref{lem:motif-residuals}; for a zero residual use the empty basis. The same lemma gives the count $s_{\rm c}$. The deficit is $2N-2L_{\rm c}>0$.

**S1.3.8.10**: For the one exceptional pair $X_a\to Y_a$, with $u=u_a$ of binary norm one and weight $27$: $q_{U_a^\perp}-q_{U_a}=\operatorname{wt}(x)+2[u\cdot x]\pmod 4$, so the operator is $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u)$ and $C$ elsewhere.
Source: "=\operatorname{wt}(x)+2[u\cdot x]\pmod4." (paper)
> l C_{U_{\mathrm{sink}(\rho(w))}} \mathcal C_{U_{\mathrm{source}(w)}}^{-1}$. For $k$ columns, use $D_v=\mathcal C_{U_v}^{\otimes k}$ on the joint address set in the same identity. The route operator is then the $k$th tensor power of the displayed address operator, multiplied by its scalar route sign once. The zero label has frame $I$, while the full label has frame $C^{\otimes m}$ because $q_{\mathcal F}(x)=\operatorname{wt}(x)$. Every pair except $X_a\to Y_a$ has these zero and full labels. For the remaining pair, write $u=u_a$. Its binary norm is one and its weight is $3^3=27$. Orthogonal weight additivity yields \begin{align*} q_{U_a^\perp}(x)-q_{U_a}(x) &=\operatorname{wt}(x)-2\operatorname{wt}(u)[u\cdot x]\\ &=\operatorname{wt}(x)+2[u\cdot x]\pmod4. \end{align*} Since $2[u\cdot x]\equiv2\sum_{j\in\operatorname{supp}(u)}x_j \pmod4$, the operator on $X_a\to Y_a$ is the tensor of $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u)$ and $C$ elsewhere. Put $Z=\operatorname{diag}(1,-1)$. Direct multiplication gives \[ C=iZC^{-1}Z,\qquad C^{-1}=-iZCZ. \] For $k$ columns, let $Z_{a,k}$ be the tensor product of $Z$ on those 27 coordinates in every column and the identity elsewhere. Apply $Z_{a,k}$ before the network at $X_a$, and apply $i^{27k}Z_{a,k}$ after the network at $Y_a$; the latter scalar is applied once to the whole role. There are $27k$ inverse factors, so the identity $C=iZC^{-1}Z$ turns each of them into $C$. The operator on this pair is therefore $C^

**S1.3.8.11**: The identity $C=iZC^{-1}Z$ (with $Z=\operatorname{diag}(1,-1)$) turns each of the $27k$ inverse factors into $C$ after applying $Z_{a,k}$ before and $i^{27k}Z_{a,k}$ after, so every role, including scratch roles, receives $C^{\otimes mk}$.
Source: "C=iZC^{-1}Z,\qquad C^{-1}=-iZCZ." (paper)
> ero label has frame $I$, while the full label has frame $C^{\otimes m}$ because $q_{\mathcal F}(x)=\operatorname{wt}(x)$. Every pair except $X_a\to Y_a$ has these zero and full labels. For the remaining pair, write $u=u_a$. Its binary norm is one and its weight is $3^3=27$. Orthogonal weight additivity yields \begin{align*} q_{U_a^\perp}(x)-q_{U_a}(x) &=\operatorname{wt}(x)-2\operatorname{wt}(u)[u\cdot x]\\ &=\operatorname{wt}(x)+2[u\cdot x]\pmod4. \end{align*} Since $2[u\cdot x]\equiv2\sum_{j\in\operatorname{supp}(u)}x_j \pmod4$, the operator on $X_a\to Y_a$ is the tensor of $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u)$ and $C$ elsewhere. Put $Z=\operatorname{diag}(1,-1)$. Direct multiplication gives \[ C=iZC^{-1}Z,\qquad C^{-1}=-iZCZ. \] For $k$ columns, let $Z_{a,k}$ be the tensor product of $Z$ on those 27 coordinates in every column and the identity elsewhere. Apply $Z_{a,k}$ before the network at $X_a$, and apply $i^{27k}Z_{a,k}$ after the network at $Y_a$; the latter scalar is applied once to the whole role. There are $27k$ inverse factors, so the identity $C=iZC^{-1}Z$ turns each of them into $C$. The operator on this pair is therefore $C^{\otimes mk}$ as well. Only the physical $X$ outputs still carry the minus sign of the scalar exchange. Negate those outputs and send output role $\rho(w)$ back to role $w$. Every role, including every scratch role, now has the required forward tensor product. \end{proof}

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
- $\mathsf S_\Omega$ (array network), bound on [Frames on wire arrays](array-frames.md): The network obtained by applying every gate pointwise on arrays over the address set, acting on all wire arrays together.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): The invertible R-linear operator on R^Omega assigned to a source, gate or sink v.
- $t$ (gate fan-in), bound on [Frames on wire arrays](array-frames.md): The number of input arrays of a gate.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each of the two sequences being convolved.
- $d$ (axis count), bound on [Cyclic convolution](convolution.md): The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of cyclic axis i.
- $M$ (address count), bound on [Cyclic convolution](convolution.md): The number of cyclic addresses of an array, the product of the axis lengths.
- $T$ (coefficient count), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array.
- $u$ (first input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The first of the two integers being multiplied.
- $v$ (second input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The second of the two integers being multiplied.
- $b$ (digit bits), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in one radix-2^b digit.
- $T$ (padded length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): A power of two with 4n/b <= T < 8n/b, the padded length from parameter choice.
- $S$ (convolution length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The length of the cyclic convolution, a product of distinct odd primes with T/2 < S < T.
- $q$ (digit count), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of digits in each input.
- $u_i$ (digit of u), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The digit of u of weight 2^{bi}, an integer below 2^b.
- $v_k$ (digit of v), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The digit of v of weight 2^{bk}, an integer below 2^b.
- $x$ (polynomial variable), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The indeterminate of the digit polynomials.
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
- $q$ (radix), bound on [Elementary stream operations](stream-ops.md): The radix: the number of values one digit can take (not a sequence length here).
- $P$ (prefix count), bound on [Elementary stream operations](stream-ops.md): The number of prefix values in the array indexed by [P]x[R]x[B].
- $R$ (row count), bound on [Elementary stream operations](stream-ops.md): The number of rows in each prefix (not the scalar ring).
- $B$ (row length), bound on [Elementary stream operations](stream-ops.md): The number of entries per row.
- $W$ (stream count), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams into which rows are dealt.
- $j$ (digit value), bound on [Elementary stream operations](stream-ops.md): A value of the chosen digit in the splitting example.
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
- $q$ (prime radix), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The prime radix of the stored digits.
- $b$ (field digit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of base-q digits of a field.
- $Q$ (field size), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of values a field can take, q^b.
- $y$ (field value), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The value of the target field, between 0 and Q-1.
- $a$ (offset), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The offset added to the target field, prepared from the control values.
- $B$ (suffix digit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of digits that follow the target field.
- $c$ (scaling integer), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed positive integer prime to q, by which the field is multiplied.
- $j$ (wrap count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of times cy wraps past Q.
- $m$ (fields per group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of fields in each of the groups H and D.
- $a$ (rank of A), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rank of the rational matrix A.
- $b$ (digits per field), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of base-q digits in each field.
- $q$ (fixed odd prime), bound on [Matrix shear by triangular factorization](matrix-shear.md): The fixed odd prime modulus base of the fields.
- $H$ (target group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The first group of m fields, which receives AD.
- $D$ (source group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The second group of m fields, which is left unchanged.
- $A$ (shear matrix), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rational m by m matrix whose shear is performed.
- $E_1$ (left triangular factor), bound on [Matrix shear by triangular factorization](matrix-shear.md): The invertible lower triangular matrix on the left of the factorization of A; E_2 is the one on the right.
- $\Pi$ (partial permutation), bound on [Matrix shear by triangular factorization](matrix-shear.md): The matrix with exactly a ones, at most one per row and column, in the factorization of A.
- $a$ (kernel coefficient), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1+i)/2, a coefficient of the kernel.
- $b$ (kernel coefficient), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1-i)/2, a coefficient of the kernel; not a bit index.
- $I$ (identity matrix), bound on [Two-point kernel C](phase-kernel.md): The 2 by 2 identity matrix.
- $X$ (bit flip), bound on [Two-point kernel C](phase-kernel.md): The 2 by 2 matrix swapping the two entries of a pair.
- $C$ (two-point kernel), bound on [Two-point kernel C](phase-kernel.md): The two-point kernel aI + bX.
- $\mathsf S$ (phase matrix), bound on [Two-point kernel C](phase-kernel.md): The diagonal matrix diag(1,i) multiplying the second entry of a pair by i.
- $H_0$ (averaging step matrix), bound on [Two-point kernel C](phase-kernel.md): The matrix of the two-point averaging and differencing step.
- $H$ (normalized Hadamard), bound on [Two-point kernel C](phase-kernel.md): The Hadamard matrix sqrt(2) H_0.
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
- $s_i$ (axis length), bound on [Chinese-remainder address map](crt-map.md): The length of cyclic axis i of the source; the lengths are pairwise coprime.
- $P_i$ (prefix product), bound on [Chinese-remainder address map](crt-map.md): The product of the lengths s_j with j<i.
- $\mu_i$ (axis exponent), bound on [Chinese-remainder address map](crt-map.md): The inverse of P_i modulo s_i, used as the exponent of x_i.
- $\Phi$ (Chinese-remainder map), bound on [Chinese-remainder address map](crt-map.md): The algebra isomorphism from the cyclic ring of length S to the product of cyclic axes.
- $x_i$ (axis variable), bound on [Chinese-remainder address map](crt-map.md): The polynomial variable of axis i, with x_i^{s_i}=1.
- $k$ (coefficient index), bound on [Chinese-remainder address map](crt-map.md): A single coefficient index, an exponent of x, not an index tuple.
- $a_j$ (mixed-radix digit), bound on [Chinese-remainder address map](crt-map.md): The digit of k in position j of its mixed-radix expression, with 0 <= a_j < s_j.
- $b_i$ (axis coordinate), bound on [Chinese-remainder address map](crt-map.md): The coordinate in axis i of the image of x^k.
- $\ell$ (address bits), bound on [Chinese-remainder address map](crt-map.md): The number of address bits of an axis of length r, with r = 2^ell.
- $T$ (padded record count), bound on [Chinese-remainder address map](crt-map.md): The number of padded records, the product of the axis lengths t_i.
- $\tau$ (interchange exponent), bound on [Chinese-remainder address map](crt-map.md): A fixed exponent below 1 in the chunk-interchange time bound.
- $i$ (axis index), bound on [Chinese-remainder address map](crt-map.md): The index of an axis, from 1 to d.
- $t_i$ (padded axis length), bound on [Chinese-remainder address map](crt-map.md): The length of axis i after zero padding, either r/2 or r.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the prime-length Fourier transform being re-expressed.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): The relative excess t/s-1 of the padded length over the source length.
- $\mathsf S$ (input resampling), bound on [Gaussian resampling](gaussian-resampling.md): The Gaussian-weighted map from length-s to length-t complex vectors applied before the power-of-two transform.
- $\mathsf T$ (output resampling), bound on [Gaussian resampling](gaussian-resampling.md): The Gaussian-weighted map from length-s to length-t complex vectors on the transform side of the identity.
- $q_j$ (nearest coordinate), bound on [Gaussian resampling](gaussian-resampling.md): The integer nearest tj/s, the coordinate of the length-t vector selected for index j.
- $\beta_j$ (rounding offset), bound on [Gaussian resampling](gaussian-resampling.md): The difference tj/s-q_j between tj/s and its nearest integer.
- $C$ (selection map), bound on [Gaussian resampling](gaussian-resampling.md): The map from length-t to length-s vectors that picks coordinate q_j for each j.
- $\mathsf D$ (Gaussian diagonal), bound on [Gaussian resampling](gaussian-resampling.md): The diagonal map multiplying coordinate j by e^{pi alpha^2 beta_j^2}.
- $N$ (approximate identity), bound on [Gaussian resampling](gaussian-resampling.md): The map C T D on length-s vectors, close to the identity.
- $k$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A single coordinate index of a vector, not an index tuple.
- $j$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A single coordinate index of a vector, not an index tuple.
- $\alpha$ (width parameter), bound on [Gaussian resampling](gaussian-resampling.md): An integer with 2<=alpha<sqrt p setting the width of the Gaussian weights.
- $t$ (padded length), bound on [Gaussian resampling](gaussian-resampling.md): The nearby larger transform length, a power of two, into which the length-s transform is resampled.
- $z$ (input vector), bound on [Retained permutation cancellation](retained-permutations.md): A vector of q complex entries to which the transform is applied.
- $F_q^+$ (opposite transform), bound on [Retained permutation cancellation](retained-permutations.md): The discrete Fourier transform of length q with the sign of the exponent reversed.
- $\beta$ (unit), bound on [Retained permutation cancellation](retained-permutations.md): A unit modulo q, used to define the index permutation R_beta.
- $w$ (summation index), bound on [Retained permutation cancellation](retained-permutations.md): The summation index in the Fourier sum.
- $w'$ (new summation index), bound on [Retained permutation cancellation](retained-permutations.md): The summation index obtained as beta times w.
- $\nu$ (setup exponent), bound on [Retained permutation cancellation](retained-permutations.md): The fixed exponent of p bounding the setup work per line.
- $u$ (first array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array, not an integer, transformed along the axes.
- $v$ (second array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array, not an integer, transformed along the axes.
- $a$ (round count), bound on [Retained frequency order](frequency-order.md): The number of rounds of the transform, a=log_2 t.
- $j$ (output index), bound on [Retained frequency order](frequency-order.md): The position of an output of the transform.
- $s$ (completed rounds), bound on [Retained frequency order](frequency-order.md): The number of rounds completed so far.
- $B_t$ (bit-reversal permutation), bound on [Retained frequency order](frequency-order.md): The permutation moving the entry at j to rev_a(j).
- $\mathcal H$ (parallel butterfly), bound on [Retained frequency order](frequency-order.md): The parallel butterfly applying H_0 on every participating axis in one round.
- $J_E$ (recordwise monomial), bound on [Retained frequency order](frequency-order.md): The recordwise operation multiplying each record by y^E.
- $h_p$ (grid spacing), bound on [Error tracking and exact recovery](precision-recovery.md): The spacing $2^{-p}$ of the fixed-point grid.
- $L$ (log of padded length), bound on [Error tracking and exact recovery](precision-recovery.md): The base-2 logarithm of the padded length $T$; not the linear map $L$ of the contractions page.
- $a$ (error size), bound on [Error tracking and exact recovery](precision-recovery.md): The size of an error, counted in grid spacings $h_p$.
- $e$ (unit phase), bound on [Error tracking and exact recovery](precision-recovery.md): A phase of modulus one that multiplies an array.
- $\widetilde e$ (phase approximation), bound on [Error tracking and exact recovery](precision-recovery.md): A grid approximation of the unit phase $e$ within $2h_p$.
- $x$ (disk operand), bound on [Error tracking and exact recovery](precision-recovery.md): An array in the unit disk to which a phase or chirp transform is applied; not the digit-polynomial variable.
- $E_{\rm ring}$ (ring convolution error), bound on [Error tracking and exact recovery](precision-recovery.md): The error bound $M(3L+2)$ of the returned ring convolution, in units of $h_p$.
- $E_s$ (source transform error), bound on [Error tracking and exact recovery](precision-recovery.md): The error bound $9\cdot2^\gamma TL$ of the computed source transform, in units of $h_p$.
- $\widetilde{\mathscr C}$ (computed chirp transform), bound on [Error tracking and exact recovery](precision-recovery.md): The computed chirp transform built from phase products and a complex convolution.
- $\widetilde{\mathscr F}$ (computed source transform), bound on [Error tracking and exact recovery](precision-recovery.md): The computed source transform: expansion, chirp transform, compression, then scaling by $2^\gamma$.
- $u$ (scaled digit array), bound on [Error tracking and exact recovery](precision-recovery.md): The array of scaled radix digits of the first input, each digit stored as its value times $2^{-b-2}$; not the integer.
- $v$ (scaled digit array), bound on [Error tracking and exact recovery](precision-recovery.md): The array of scaled radix digits of the second input, each digit stored as its value times $2^{-b-2}$; not the integer.
- $U$ (exact first transform), bound on [Error tracking and exact recovery](precision-recovery.md): The exact source transform of the first digit array.
- $V_1$ (exact second transform), bound on [Error tracking and exact recovery](precision-recovery.md): The exact source transform of the second digit array.
- $\widetilde U$ (computed first transform), bound on [Error tracking and exact recovery](precision-recovery.md): The computed source transform of the first digit array.
- $\widetilde V_1$ (computed second transform), bound on [Error tracking and exact recovery](precision-recovery.md): The computed source transform of the second digit array.
- $z$ (truncated product), bound on [Error tracking and exact recovery](precision-recovery.md): The truncated pointwise product of the two computed source transforms.
- $G$ (exact opposite transform), bound on [Error tracking and exact recovery](precision-recovery.md): The exact opposite-sign source transform $RF_{\boldsymbol s}^+$, a contraction.
- $w$ (first scaled result), bound on [Error tracking and exact recovery](precision-recovery.md): The convolution $(u*v)/S$ of the digit arrays divided by $S$, whose scaling by $2^{2b+4}S$ gives the integer coefficients.
- $\widetilde w$ (computed first scaled result), bound on [Error tracking and exact recovery](precision-recovery.md): The computed approximation of $w$ after exact multiplication by $S$.
- $E_w$ (scaled error), bound on [Error tracking and exact recovery](precision-recovery.md): The error bound $S(3E_s+2)$ of $\widetilde w$, in units of $h_p$.
- $Q_0$ (radix), bound on [Error tracking and exact recovery](precision-recovery.md): The radix $2^b$ of the digits used in carry propagation.
- $k_j$ (carry), bound on [Error tracking and exact recovery](precision-recovery.md): The carry into position $j$ in carry propagation.
- $d_j$ (output digit), bound on [Error tracking and exact recovery](precision-recovery.md): The $j$-th radix-$2^b$ digit of the product.
- $\tau$ (chunk-interchange exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent in the cost of a chunk interchange.
- $\sigma$ (recursion growth exponent), bound on [Parameter and prime-length choice](parameter-choice.md): An upper bound on the growth exponent of recursive calls (a new meaning of sigma).
- $\beta$ (handling threshold exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent setting the threshold d^beta below which active chunks are handled singly.
- $\lambda$ (overhead exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The per-node overhead exponent.
- $\lambda'$ (layer-cost exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The final exponent of the layer cost V d^{lambda'}.
- $V$ (bit volume), bound on [Parameter and prime-length choice](parameter-choice.md): The bit volume on which the layer cost is measured.
- $c$ (chunk-width exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the address-chunk width (a new meaning of c).
- $\epsilon$ (axis-count exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the axis count.
- $C_1$ (guard exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the guard bits.
- $\delta$ (resampling slack), bound on [Parameter and prime-length choice](parameter-choice.md): The slack in the resampling cost exponent.
- $K$ (chunk width), bound on [Parameter and prime-length choice](parameter-choice.md): The width in bits of an address chunk.
- $\eta$ (prime offset), bound on [Parameter and prime-length choice](parameter-choice.md): The smallest relative distance at which a prime s_i may lie below t_i.
- $x$ (interval scale), bound on [Parameter and prime-length choice](parameter-choice.md): A real number above e^{2/eta} scaling the interval searched for primes.
- $q$ (interval integer), bound on [Parameter and prime-length choice](parameter-choice.md): An integer in the interval (1-2eta)x < q <= (1-eta)x.
- $a_d$ (d lower constant), bound on [Parameter and prime-length choice](parameter-choice.md): Fixed positive constant in the lower bound on d.
- $b_d$ (d upper constant), bound on [Parameter and prime-length choice](parameter-choice.md): Fixed positive constant in the upper bound on d.
- $a_r$ (r lower constant), bound on [Parameter and prime-length choice](parameter-choice.md): Fixed positive constant in the lower bound on r.
- $b_r$ (r upper constant), bound on [Parameter and prime-length choice](parameter-choice.md): Fixed positive constant in the upper bound on r.
- $C_\ell$ (d-ell constant), bound on [Parameter and prime-length choice](parameter-choice.md): Fixed positive constant in the bound d l <= C_l p.
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
- $F$ (time per unit volume), bound on [Recursive power saving](rank-recurrence.md): The running time of a call at a given parameter, divided by the volume of its stream.
- $j$ (recursion depth), bound on [Recursive power saving](rank-recurrence.md): The number of recursion levels below the top call, indexing the terms of the unrolled sum.
- $\eta$ (relative rank deficit), bound on [Recursive power saving](rank-recurrence.md): The relative deficit (Wm-s)/(Wm) by which the number of smaller calls falls short of Wm.
- $u$ (chunk width), bound on [Fast address-chunk interchange](address-interchange.md): The number of bits in each of the two chunks.
- $V$ (array volume), bound on [Fast address-chunk interchange](address-interchange.md): The number of bits stored in the array.
- $\tau$ (saving exponent), bound on [Fast address-chunk interchange](address-interchange.md): The fixed exponent below 1 in the cost of the interchange.
- $p$ (address prefix), bound on [Fast address-chunk interchange](address-interchange.md): The prefix part of an address, before the first chunk.
- $h$ (first chunk), bound on [Fast address-chunk interchange](address-interchange.md): The first of the two address chunks to be interchanged.
- $d$ (second chunk), bound on [Fast address-chunk interchange](address-interchange.md): The second of the two address chunks to be interchanged.
- $g$ (gap), bound on [Fast address-chunk interchange](address-interchange.md): The part of the address between the two chunks.
- $z$ (suffix), bound on [Fast address-chunk interchange](address-interchange.md): The part of the address after the second chunk.
- $q$ (digit radix), bound on [Fast address-chunk interchange](address-interchange.md): The fixed prime radix of the digits.
- $H$ (first chunk value), bound on [Fast address-chunk interchange](address-interchange.md): The value of the first chunk, the target of the shear.
- $D$ (second chunk value), bound on [Fast address-chunk interchange](address-interchange.md): The value of the second chunk, the source of the shear.
- $e$ (chunk digit count), bound on [Fast address-chunk interchange](address-interchange.md): The number of digits in each chunk.
- $k$ (recursion levels), bound on [Fast address-chunk interchange](address-interchange.md): The number of recursion levels, with e = m^k.
- $M$ (vertex matrix), bound on [Fast address-chunk interchange](address-interchange.md): The rational m by m matrix carried by a vertex of the network.
- $i$ (edge index), bound on [Fast address-chunk interchange](address-interchange.md): The index of an edge of the network.
- $w$ (wire index), bound on [Fast address-chunk interchange](address-interchange.md): The index of an input wire of the network.
- $\rho$ (output role map), bound on [Fast address-chunk interchange](address-interchange.md): The map sending input wire w to its output role rho(w).
- $I_m$ (identity matrix), bound on [Fast address-chunk interchange](address-interchange.md): The m by m identity matrix.
- $\Phi$ (address-shear permutation), bound on [Fast address-chunk interchange](address-interchange.md): The array permutation moving the entry at address (H,D) to (H+MD,D) for a matrix M.
- $x$ (stream row number), bound on [Fast address-chunk interchange](address-interchange.md): The row number within a role stream.
- $f_w$ (input array), bound on [Fast address-chunk interchange](address-interchange.md): The physical input array of wire w.
- $F_k$ (time per unit volume), bound on [Fast address-chunk interchange](address-interchange.md): The running time divided by the volume for chunks of m^k digits.
- $j$ (level index), bound on [Fast address-chunk interchange](address-interchange.md): An index of recursion levels in the unrolled sum.
- $k'$ (levels needed), bound on [Fast address-chunk interchange](address-interchange.md): The number of recursion levels needed for chunks of e digits.
- $\nu$ (set-aside digit count), bound on [Fast address-chunk interchange](address-interchange.md): The number of top digits of each chunk set aside to form the row field.
- $h^+$ (top digits of h), bound on [Fast address-chunk interchange](address-interchange.md): The top digits of h after splitting each chunk into its top digits and rest.
- $h^-$ (rest of h), bound on [Fast address-chunk interchange](address-interchange.md): The rest of h after splitting each chunk into its top digits and rest.
- $d^+$ (top digits of d), bound on [Fast address-chunk interchange](address-interchange.md): The top digits of d after splitting each chunk into its top digits and rest.
- $d^-$ (rest of d), bound on [Fast address-chunk interchange](address-interchange.md): The rest of d after splitting each chunk into its top digits and rest.
- $\Lambda$ (row field range), bound on [Fast address-chunk interchange](address-interchange.md): The range of the row field formed by the two sets of top digits.
- $\Lambda'$ (padded row count), bound on [Fast address-chunk interchange](address-interchange.md): The row count after padding with zero rows to a multiple of W^{k'}.
- $a_j$ (piece count), bound on [Fast address-chunk interchange](address-interchange.md): The number of pieces of width m^j into which each remaining chunk is cut, a base-m digit.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Nested subspace labels and rank deficit](subspace-labels.md): Assigning nondegenerate subspaces of an m-dimensional space to gates so adjacent labels are nested; the total dimension change over edges, the number s of smaller calls, is strictly less than W·m.
  Shown as: Binary phase frames *<predicate>* Nested subspace labels and rank deficit
- [Two-point kernel C](phase-kernel.md): The matrix C = aI + bX with a = (1+i)/2, b = (1−i)/2, a square root of the bit flip, linked to the butterfly by H₀ = b·S·C·S with S = diag(1, i).
  Shown as: Binary phase frames *<predicate>* Two-point kernel C

## Pages that build on this one

- Simultaneous butterfly layer: The second tape procedure: applying H₀ coefficientwise on the same bit of up to d address chunks in time O(V·d^λ′) for a fixed λ′ < 1, instead of d passes.

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
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Contractions and bilinear contractions](contraction-maps.md)
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Retained frequency order](frequency-order.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [Tensor products of subspaces](tensor-product-of-spaces.md)
- [Recursive power saving](rank-recurrence.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}" (paper)

  > Use the complex scalar network and binary labels. For a binary vector $x$, let $\operatorname{wt}(x)$ denote its integer Hamming weight, and write $[b]\in\{0,1\}$ for the integer representative of $b\in\mathbb F_2$. For a label $U$, let \[ q_U(x)=\operatorname{wt}(P_Ux)\pmod4. \] The projection here is over $\mathbb F_2$. Let \[ H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad C=H\begin{pmatrix}1&0\\0&i\end{pmatrix}H =aI+bX,\qquad a=\frac{1+i}{2},\quad b=\frac{1-i}{2}, \] where $X$ interchanges the two coordinates. On functions of $x\in\mathbb F_2^m$ define \[ \mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}. \] The use of $H$ in this definition is an identity of matrices. Each entry of $\mathcal C_U$ and its inverse is a Gaussian integer divided by $2^m$, so both preserve arrays over $\mathbb Z[i,1/2]$. The kernels implemented below have Gaussian dyadic coefficients.

- "The binary phase interface" (paper)

  > \subsection{The binary phase interface}


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $v$ means binary vector here, but number of triples on [Linear exchange network with restored scratch wires](exchange-network.md), which this page builds on: On this page $v$ means a binary vector, but the exchange-network page uses $v$ for the number of triples. Use another letter here, or say that $v$ means a binary vector here, not the number of triples as on the exchange-network page.
- $E$ means edge residual here, but first space on [Tensor products of subspaces](tensor-product-of-spaces.md), which this page builds on: On this page $E$ means the edge residual, but the tensor-product page uses $E$ for the first tensor factor. Use another letter here, or say that $E$ means the edge residual here, not the first tensor factor as on the tensor-product page.
- $k$ means column count here, but depth on [Fixed-point Gaussian dyadic records](fixed-point.md), which this page builds on: On this page $k$ means the column count, but the fixed-point page uses $k$ for the depth of a value. Use another letter here, or say that $k$ means the column count here, not the depth of a value as on the fixed-point page.
- $u$ means binary vector here, but input sequence on [Discrete Fourier transform](dft.md), which this page builds on: On this page $u$ means a binary vector, but the discrete Fourier transform page uses $u$ for the input sequence. Use another letter here, or say that $u$ means a binary vector here, not the input sequence as on the discrete Fourier transform page.

## Previous version (revise it)

It has 540 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 675 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Binary phase frames are operators attached to the labels of [Nested subspace labels and rank deficit](subspace-labels.md) in the complex network, chosen so that every edge difference splits into one two-point kernel per dimension of change, which makes each residual dimension one smaller call of a butterfly-type operation, as the recursion needs.

Several letters change meaning on this page: $v$ is a binary vector (not a number of triples), $E$ is an edge residual (not a tensor factor), and $k$ counts columns of data (not a depth). Labels are subspaces of $\mathbb F_2^m$ ($m$ the label dimension), and $u,v,w,z$ are vectors of $\mathbb F_2^m$ here. The support $\operatorname{supp}(z)$ of a vector is the set of coordinates where it is $1$. Write $\operatorname{wt}(x)=|\operatorname{supp}(x)|$ for the Hamming weight, $[b]\in\{0,1\}$ for the integer representative of $b\in\mathbb F_2$, $P_U$ for projection onto a label $U$, and $z\cdot w$ for the dot product, both over $\mathbb F_2$. A vector $v$ has binary norm one when $v\cdot v=1$, equivalently $\operatorname{wt}(v)$ is odd; a basis is orthonormal when its vectors have norm one and are pairwise orthogonal. Let $X_v$ be the translation $(X_vf)(x)=f(x+v)$, and $C=H\operatorname{diag}(1,i)H=aI+bX$ with $a=\frac{1+i}{2}$, $b=\frac{1-i}{2}$, where $H=\tfrac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$.

For a label $U$ put $q_U(x)=\operatorname{wt}(P_Ux)\bmod 4$, with the projection taken over $\mathbb F_2$. The phase frame is $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$, with Gaussian-dyadic entries. <cite data-source="paper">Each entry of $\mathcal C_U$ and its inverse is a Gaussian integer divided by $2^m$</cite>

## Weight modulo four

For binary vectors $z,w$, $\operatorname{wt}(z+w)=\operatorname{wt}(z)+\operatorname{wt}(w)-2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|$, since a coordinate in both supports holds $1+1=0$. If $z\cdot w=0$ the intersection cardinality is even, so weight is additive modulo four on orthogonal vectors.

Take an edge from $U$ to $V=U\perp E$, where $E$, the edge residual, has orthonormal basis $\mathcal B$. Then $P_Vx=P_Ux+\sum_{v\in\mathcal B}[v\cdot x]\,v$, a sum of pairwise orthogonal vectors. So $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\operatorname{wt}(v)[v\cdot x]\pmod 4$, negated on a decreasing edge, and each $\operatorname{wt}(v)$ is odd. Each term is therefore $\varepsilon[v\cdot x]$ with $\varepsilon=\pm1$ modulo four, the sign including the edge direction. The function $i^{\varepsilon[v\cdot x]}$ equals $\frac{1+i^\varepsilon}2+\frac{1-i^\varepsilon}2(-1)^{v\cdot x}$, as checking $v\cdot x=0,1$ shows.

## From phases to kernels

Since $H^2=I$, $\mathcal C_V\mathcal C_U^{-1}=H^{\otimes m}\operatorname{diag}(i^{q_V-q_U})H^{\otimes m}$, a product over $\mathcal B$. The character $(-1)^{v\cdot x}$ is $\operatorname{diag}(1,-1)$ on the coordinates in $\operatorname{supp}(v)$. Since $H\operatorname{diag}(1,-1)H=X$, the character $(-1)^{v\cdot x}$ becomes the translation $X_v$, so the phase becomes $aI+bX_v$ or its inverse. For $\varepsilon=-1$ the coefficients swap, giving $bI+aX_v$, the inverse because $a^2+b^2=0$ and $2ab=1$. Each edge factor is a translate $aI+bX_v$ of [Two-point kernel C](phase-kernel.md), one per basis vector.

Let $L_{\rm c}$ be the total dimension lost on decreasing edges, $N$ the bank size and $W_{\rm c}$ the wire count. The number of translation-kernel factors over the network is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}=1873807244636671267308000000<W_{\rm c}m$. <cite data-source="paper">s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}</cite> The deficit of $s_{\rm c}$ from $W_{\rm c}m$ is $2N-2L_{\rm c}>0$, since $L_{\rm c}/N<\frac12$.

## Terminal pairs

Source and sink labels are $U_a\to\mathcal F$ on $X_a$, $0\to U_a^\perp$ on $Y_a$ and $0\to\mathcal F$ on scratch, with $U_a$ the line spanned by $u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$. For $k$ columns (an address is a $k$-tuple), [Frames on wire arrays](array-frames.md) gives each role the $k$th tensor power of the sink frame times the inverse source frame, with $X_a,Y_a$ exchanged. Label $0$ has frame $I$. For $\mathcal F$, $q_{\mathcal F}(x)=\operatorname{wt}(x)$ and $i^{\operatorname{wt}(x)}=\prod_ji^{x_j}$, so its frame is $C^{\otimes m}$. Only $X_a\to Y_a$ differs.

For it take $u=u_a$, with $3^3=27$ ones, so $u\cdot u=1$ and $P_{U_a}x=[u\cdot x]u$. Orthogonality of $P_{U_a}x$ and $P_{U_a^\perp}x$ gives $\operatorname{wt}(x)\equiv q_{U_a}+q_{U_a^\perp}$, hence $q_{U_a^\perp}-q_{U_a}=\operatorname{wt}(x)-2\operatorname{wt}(u)[u\cdot x]=\operatorname{wt}(x)+2[u\cdot x]\pmod 4$. As $2[u\cdot x]\equiv2\sum_{j\in\operatorname{supp}(u)}x_j$, the phase per coordinate is $i^{-x_j}$ on the 27 coordinates of $\operatorname{supp}(u)$ and $i^{x_j}$ elsewhere, so the operator is $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u)$ and $C$ elsewhere.

With $Z=\operatorname{diag}(1,-1)$ we have $ZXZ=-X$ and $C^{-1}=bI+aX$; since $ib=a$ and $ia=-b$, $C=iZC^{-1}Z$. Let $Z_{a,k}$ be $Z$ on those 27 coordinates in every column. Apply $Z_{a,k}$ before the network at $X_a$ and $i^{27k}Z_{a,k}$ after it at $Y_a$. The identity $C=iZC^{-1}Z$ turns each of the $27k$ inverse factors into $C$, so every role, including scratch roles, receives $C^{\otimes mk}$ once the physical $X$ outputs, which carry the minus sign of the scalar exchange, are negated and outputs are renamed to input roles.

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

Write the body to `exegenius/tasks/0308-write-phase-frames.answer.md` and the JSON to `exegenius/tasks/0308-write-phase-frames.answer.json`, then run `exegenius submit 0308-write-phase-frames` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0308-write-phase-frames`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
