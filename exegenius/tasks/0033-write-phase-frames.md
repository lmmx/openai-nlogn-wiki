# exegenius task 0033-write-phase-frames

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Nested subspace labels and rank deficit](subspace-labels.md): Assigning nondegenerate subspaces of an m-dimensional space to gates so adjacent labels are nested; the total dimension change over edges, the number s of smaller calls, is strictly less than W·m.
  Shown as: Binary phase frames *<predicate>* Nested subspace labels and rank deficit
- [Two-point kernel C](phase-kernel.md): The matrix C = aI + bX with a = (1+i)/2, b = (1−i)/2, a square root of the bit flip, linked to the butterfly by H₀ = b·S·C·S with S = diag(1, i).
  Shown as: Binary phase frames *<predicate>* Two-point kernel C

## Pages that build on this one

- Simultaneous butterfly layer: The second tape procedure: applying H₀ coefficientwise on the same bit of up to d address chunks in time O(V·d^λ′) for a fixed λ′ < 1, instead of d passes.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Recursive power saving](rank-recurrence.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Elementary stream operations](stream-ops.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
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
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Parameter and prime-length choice](parameter-choice.md)
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

Write the body to `exegenius/tasks/0033-write-phase-frames.answer.md` and the JSON to `exegenius/tasks/0033-write-phase-frames.answer.json`, then run `exegenius submit 0033-write-phase-frames` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0033-write-phase-frames`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
