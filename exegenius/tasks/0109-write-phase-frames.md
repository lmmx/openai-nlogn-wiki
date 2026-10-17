# exegenius task 0109-write-phase-frames

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
- [Retained frequency order](frequency-order.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Contractions and bilinear contractions](contraction-maps.md)
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
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

- The reader cannot follow this step: "For the pair $X_a\to Y_a$, take $u=u_a$ of binary norm one and weight $27$." (The page does not say what X_a, Y_a, u_a are, why this pair is different from the others, why u_a has weight 27 (paper line 1291: 3^3=27), or that the edge runs from the label U_a to U_a^perp. The reader cannot check these from the page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Orthogonal additivity gives $\operatorname{wt}(x)-2\operatorname{wt}(u)[u\cdot x]$" (The page never states that x splits as P_{U_a}x plus P_{U_a^perp}x with orthogonal parts, so wt(x)=q_U+q_{U^perp} mod 4 and q_{U^perp}-q_U=wt(x)-2q_U with q_U(x)=wt(u)[u.x]. The single-edge computation was done for V=U perp E, not this setting, so the formula does not follow from what the page gives.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "so every role, scratch roles included, receives $C^{\otimes mk}$" (The page never says what the other roles receive (zero label has frame I, full label has frame C^{\otimes m} since q_F(x)=wt(x); source and sink corrections; undoing the signed exchange and the minus sign on X outputs; paper lines 1280-1310). The conclusion for scratch roles is asserted without these steps.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Say what $w$ denotes where it is first used: the page uses it before saying so in "For binary vectors $z,w$"
- Say what $L_{\rm c}$ denotes where it is first used (for a size or count, what it counts): "$N$, $L_{\rm c}$ are constants of the labels page" (The page only says it is a constant of the labels page; it does not say what it counts (the total dimension loss on decreasing edges of the complex network).)
- Say what $d$ denotes where it is first used: the page uses it before saying so in "A residual of dimension $d$ costs $d$ such calls"
- Say what $u$ denotes where it is first used (for a size or count, what it counts): "For the pair $X_a\to Y_a$, take $u=u_a$ of binary norm one and weight $27$." (The page never says what u_a is (a vector generating the line U_a, presumably), nor how it is obtained.)
- Say what $X_a$ denotes where it is first used (for a size or count, what it counts): "For the pair $X_a\to Y_a$" (X_a is not defined on this page; it names a role of the network, not explained here.)
- Say what $Y_a$ denotes where it is first used (for a size or count, what it counts): "For the pair $X_a\to Y_a$" (Y_a is not defined on this page; it names a role of the network, not explained here.)

## Previous version (revise it)

It has 349 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 436 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

A binary phase frame attaches to each label of [Nested subspace labels and rank deficit](subspace-labels.md) a basis for arrays of binary addresses, so that the change of basis along an edge is a product of two-point kernels. Here $m$ is the number of binary coordinates of an address $x$, and a label $U$ is a subspace of $\mathbb F_2^m$.

Write $\operatorname{wt}(x)$ for Hamming weight, $[b]\in\{0,1\}$ for the integer representative of $b\in\mathbb F_2$, and $P_U$ for the projection onto $U$ over $\mathbb F_2$. Put $q_U(x)=\operatorname{wt}(P_Ux)\bmod 4$. With $H=\tfrac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, the phase frame is $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$, with Gaussian-dyadic entries. <cite data-source="paper">Each entry of $\mathcal C_U$ and its inverse is a Gaussian integer divided by $2^m$</cite> Let $C=H\operatorname{diag}(1,i)H=aI+bX$, with $a=\frac{1+i}{2}$, $b=\frac{1-i}{2}$, $X$ the coordinate swap, and $X_v$ the translation $(X_vf)(x)=f(x+v)$.

## One edge

For binary vectors $z,w$, $\operatorname{wt}(z+w)=\operatorname{wt}(z)+\operatorname{wt}(w)-2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|$. The dot product $z\cdot w$ is that intersection size mod $2$. If $z\cdot w=0$ the intersection cardinality is even, so weight is additive modulo four on orthogonal vectors.

Take an edge from $U$ to $V=U\perp E$, with residual $E$ orthogonal to $U$ and orthonormal basis $\mathcal B$ (distinct vectors have dot product $0$, and $v\cdot v=1$). Then $P_Vx=P_Ux+\sum_{v\in\mathcal B}[v\cdot x]\,v$ so $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\operatorname{wt}(v)[v\cdot x]\pmod 4$, negated on a decreasing edge, and each $\operatorname{wt}(v)$ is odd.

Odd weight is $\pm1$ modulo four, so each term is $\varepsilon[v\cdot x]$, $\varepsilon=\pm1$. The function $i^{\varepsilon[v\cdot x]}$ with $\varepsilon=\pm1$ equals $\frac{1+i^\varepsilon}2+\frac{1-i^\varepsilon}2(-1)^{v\cdot x}$.

Since $H^2=I$, $\mathcal C_V\mathcal C_U^{-1}=H^{\otimes m}\operatorname{diag}(i^{q_V-q_U})H^{\otimes m}$, one phase per $v$. The character $(-1)^{v\cdot x}$ is $\operatorname{diag}(1,-1)$ on $\operatorname{supp}(v)$. Since $H\operatorname{diag}(1,-1)H=X$, the character $(-1)^{v\cdot x}$ becomes the translation $X_v$, so the phase becomes $aI+bX_v$ or its inverse ($\varepsilon=-1$).

Each edge factor is built as a translate $aI+bX_v$ of [Two-point kernel C](phase-kernel.md), combining only $f(x)$ and $f(x+v)$, a butterfly-type operation. A residual of dimension $d$ costs $d$ such calls, one smaller call per dimension, as the recursion needs.

## Counting

Here $W_{\rm c}$ is the number of wires of the complex network, and $N$, $L_{\rm c}$ are constants of the labels page. Over the network the number of translation-kernel factors is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}=1873807244636671267308000000<W_{\rm c}m$. <cite data-source="paper">s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}</cite> The deficit of $s_{\rm c}$ from $W_{\rm c}m$ is $2N-2L_{\rm c}>0$. <cite data-source="paper">The deficit is $2N-2L_{\rm c}>0$.</cite>

## The exceptional pair

For the pair $X_a\to Y_a$, take $u=u_a$ of binary norm one and weight $27$. Orthogonal additivity gives $\operatorname{wt}(x)-2\operatorname{wt}(u)[u\cdot x]$, and $27$ is odd, so $q_{U_a^\perp}-q_{U_a}=\operatorname{wt}(x)+2[u\cdot x]\pmod 4$, so the operator is $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u)$ and $C$ elsewhere.

Let $Z=\operatorname{diag}(1,-1)$; then $C=iZC^{-1}Z$. For $k$ columns, let $Z_{a,k}$ be $Z$ on those 27 coordinates in every column. The identity $C=iZC^{-1}Z$ turns each of the $27k$ inverse factors into $C$ after applying $Z_{a,k}$ before and $i^{27k}Z_{a,k}$ after, so every role, scratch roles included, receives $C^{\otimes mk}$.

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

Write the body to `exegenius/tasks/0109-write-phase-frames.answer.md` and the JSON to `exegenius/tasks/0109-write-phase-frames.answer.json`, then run `exegenius submit 0109-write-phase-frames` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0109-write-phase-frames`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
