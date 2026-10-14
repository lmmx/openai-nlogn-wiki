# exegenius task 0036-write-recursive-c-layer

Project directory: `/home/user/openai-nlogn-wiki/runs/Q1` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, binomial counting, permutations, induction, graphs, the union bound, and elementary number theory with gcd, primes, modular inverses and the Chinese remainder theorem), an algorithms course (asymptotic notation, recurrences and geometric sums, divide and conquer including Karatsuba, sorting including radix sort, stacks, amortized counters, the RAM model and worst-case running time), and an introductory theory course with Turing machines and multitape tapes. From computer organization they know binary and two's-complement encodings, bit order, XOR and binary arithmetic; from calculus and a first linear-algebra course they know logarithms, exponentials, Newton's method, simple inequalities, complex numbers with conjugates, polynomials, matrices, Gaussian elimination, rank, dot products, projections and eigenvalues over the real or rational numbers. They have not studied abstract algebra (rings, quotient rings, finite fields, tensor products, bilinear forms over 𝔽₂), Fourier analysis, numerical error analysis, or the research literature on fast integer multiplication, so the FFT machinery, resampling and all of the paper's constructions are new to them.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine (also: fixed finite-tape model)
- Modular arithmetic and finite fields (also: F_2, residue ring)
- Linear maps, matrices and rank (also: rational rank)
- Tensor products (also: tensor power)
- Nondegenerate bilinear forms and orthogonal complements (also: orthogonal complement, orthonormal basis)
- The n log n conjecture (also: Schönhage–Strassen conjecture, n log n optimality conjecture)
- Harvey–van der Hoeven O(n log n) multiplier (also: established multiplier)
- Lexicographic array layout and logical volume (also: address field, logical volume, row)
- Elementary stream operations
- Controlled shifts and rational scalings (also: prefix-controlled cyclic shift, triangular update)
- Gaussian dyadic fixed-point arithmetic (also: disk grid, Q_p truncation, Gaussian dyadics)
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring, R_r)
  - $y$ (polynomial variable): The indeterminate of the ring, whose powers act as roots of unity of order 2r.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Normalized butterfly H₀ (also: butterfly, Hadamard butterfly)
  - $H_0$ (normalized butterfly): The 2×2 matrix ½[[1, 1], [1, −1]] sending a pair (u, v) to ((u + v)/2, (u − v)/2).
- Two-point kernel C (also: translation kernel, aI+bX)
  - $C$ (two-point kernel): The 2×2 complex matrix aI + bX with a = (1 + i)/2, b = (1 − i)/2 and X the coordinate swap.
- Linear network with wire roles (also: role, wire, gate, scalar network)
- Restoring scratch values (also: transparent computation, scratch wires)
- Three-element subset construction (also: Frankl–Wilson construction, triple indicators)
- Three-stage bank exchange (also: gather, scatter, side injection, forward invocation)
- Frames and the common-frame identity (also: frame, endpoint operator)
- Nested subspace labels and orthogonal residuals (also: label, orthogonal residual, dimension loss)
- Rank deficit s < Wm (also: rank saving, relative rank deficit)
  - $s$ (number of smaller calls): The total number of smaller recursive calls the network's edges require, summed over all edges.
  - $W$ (wire count): The number of wires (roles) in the finite network, including scratch wires.
  - $m$ (label dimension): The dimension of the label space, which is the factor by which each smaller call shrinks the recursion parameter.
- Rational matrix interface of the bit network
- Binary phase interface of the complex network (also: phase frame, complex network)
- Address shear
- Lower triangular (Bruhat) factorization
- Matrix shear by rank-many interchanges
- Row splitting among wire roles
- Volume-normalized recursion and the power saving (also: recursive saving)
- Fixed-tape depth-first schedule (also: parking stack)
- Power-width interchange
- Fast address-chunk interchange (also: chunk swap, address interchange, arbitrary-width interchange)
- Packed selected-bit addition (also: binary change of basis, deterministic repair, guard values)
- Signed Kronecker packing (also: Kronecker substitution)
- Binary representation of integers (also: base-2 representation, bin_k, val, positional notation, radix-2^b digits)
- Two's-complement representation (also: two's complement, signed w-bit word, sign extension)
- Bit order and endianness (also: most significant bit first, least significant bit first, MSB first, LSB first)
- Bitwise exclusive or (also: XOR, ⊕, bitwise operations)
- Hamming weight (also: wt, popcount, number of ones)
- Logarithms and exponent rules (also: log, log₂, lg, natural logarithm)
- Floor, ceiling and rounding (also: ⌊x⌋, ⌈x⌉, nearest integer, truncation toward zero)
- Worst-case running time (also: time complexity, T_A(n), worst-case cost)
- RAM model of computation (also: unit-cost RAM, random-access machine, word RAM)
- Recurrences and recursion trees (also: recurrence relation, divide and conquer, master theorem, unrolling a recurrence)
- Geometric series (also: geometric sum, Σ a^j)
- Telescoping sums (also: telescoping)
- Karatsuba multiplication (also: Karatsuba–Ofman algorithm, n^{log₂ 3} multiplication)
- Stacks (also: LIFO, push and pop, call stack)
- Binary counter and amortized increment cost (also: binary counter, amortized analysis, ripple counting)
- Radix sort and stable sorting (also: stable sort, LSD radix sort, binary radix sort)
- Row-major order and matrix transposition (also: row-major layout, transpose)
- Directed graphs (also: vertices and edges, head and tail of an edge, path)
- Sets, Cartesian products and indicator vectors (also: [a] = {0,…,a−1}, Cartesian product, characteristic vector, indicator vector, subset intersection)
- Binomial coefficients (also: n choose k, C(n,k))
- Permutations and cycle notation (also: bijection, involution, cycle (a b c), inverse permutation)
- Union bound (also: Boole's inequality, counting bad cases)
- Greatest common divisor and Euclid's algorithm (also: gcd, coprime, relatively prime, extended Euclidean algorithm, modular inverse)
- Prime numbers and trial division (also: primes, primality testing by trial division, odd prime)
- Chinese remainder theorem (also: CRT)
- Matrix operations (also: identity matrix, diagonal matrix, permutation matrix, triangular matrix, lower triangular, block diagonal, direct sum of maps)
- Gaussian elimination (also: row reduction, elementary row operations, row addition, row swap, pivot)
- Dot product and orthogonality (also: inner product, x·y, orthogonal vectors)
- Projection onto a subspace (also: projection matrix, P_U)
- Eigenvalues of a matrix (also: eigenvalue, eigenvector)
- Complex conjugate (also: conjugation, z̄)
- Triangle inequality (also: |a + b| ≤ |a| + |b|)
- Bernoulli's inequality (also: (1 + x)^n ≥ 1 + nx)
- Newton's method (also: Newton iteration, Newton–Raphson)
- Proof by induction (also: induction, inductive invariant, loop invariant)

## This page

Concept: Recursive C-layer via phase frames
Gloss: Computing C^{⊗e} on e selected address bits by running the complex network on row-split streams, implementing each edge's frame change by a binary change of basis and one recursive C^{⊗e/m} call per residual vector.

## This page in the argument

The step: The tensor product $C^{\otimes D}$ of the kernel $C$ on the selected bits of $D\le d$ chunks is computed exactly in $O(Vd^{\lambda'})$ time, by recursion in which a group of $e$ selected axes uses $s_{\rm c}$ children on $e/m$ axes, each on a stream of volume $V/W$.
How: Run the complex network on row-split role streams with column phase frames, implement each edge's frame change by a binary change of basis (packed row additions) and one recursive $C^{\otimes e/m}$ call per residual vector, and unroll the volume-normalized recurrence.
Why: Phase frames express a $C$ tensor product through smaller groups of selected bits separated by binary changes of basis, so the rank deficit $s<Wm$ becomes a power saving in $d$. (the sources say so: "Its phase
frames express a $C$ tensor product using smaller groups of
selected bits, separated by binary changes of basis." (paper))

Its sub-steps, in order:

- With phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{q_U(x)})H^{\otimes m}$, each edge's frame change of the complex network is a product of one translation kernel $aI+bX_v$ (or its inverse) per orthonormal residual vector, these total $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$, and after diagonal corrections every role receives $C^{\otimes m}$. (on [Binary phase interface of the complex network](phase-interface.md))
- Conjugating by an address permutation $\mathcal P_M$ whose first columns are the residual basis turns each directional kernel into $C^{\pm1}$ on coordinate slot $h$, i.e. one child operation on the $f$ axes of that slot.
- An inverse kernel needs only one forward child, since $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$.
- The change of basis $\mathcal P_M$ is a fixed number of row additions, each XORing corresponding selected positions of two whole slots.
- Applying the network with these column frames to $e=mf$ selected axes gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and yields $C^{\otimes e}$ on every role.
- For three $L$-bit chunks $x,y,z$ with $L=fK$, the XORs $y_{j_i}\gets y_{j_i}\oplus x_{j_i}$ at positions $j_i=\rho+iK$ are performed while restoring $z$, in time $O(V(L^\tau+1))$ under the layer's parameter growth. (on [Packed selected-bit addition](packed-addition.md))
- Each binary change of basis and its inverse cost $O(V((eK)^\tau+1))$ on a stream of volume $V$.
- Applying $C$ individually to the first $q_0$ chunks lets their bits serve as a row index of range at least $W^{k_0}$, padded to a multiple of $W^{k_0}$.
- The normalized cost satisfies $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, because the $s$ children run on streams of volume $V/W$.
- Summing over the base-$m$ pieces and the row preprocessing gives normalized cost $O(d^{\lambda'})$ for $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet, fixed-tape Turing machine computes the exact $2n$-bit product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ conjecture in this model.; how: Reduce the product to radix-digit convolution, move it by a Chinese-remainder map, Gaussian resampling, chirps and a phase twist to convolution over $\mathbb C[y]/(y^r+1)$ computed by synthetic transforms; speed up the transforms' address movement and butterfly layers with two network-based tape procedures; then prove exact recovery and total the costs. (on [Integer multiplication in O(n (lg n)^{1−κ}) time](main-theorem.md))
- Two tape procedures save over plain scanning: address chunks of width $u$ are interchanged in $O(Vu^\tau)$ time, and a simultaneous normalized butterfly layer on $D\le d$ chunks costs $O(Vd^{\lambda'})$, with fixed $\tau,\lambda'<1$.; how: Build each procedure from its own fixed linear network that exchanges two banks and restores scratch wires, apply the network pointwise to row-split role streams with frames chosen so every edge is a few smaller calls, and solve the volume-normalized recurrence.
- The simultaneous butterfly layer: on an array of polynomial records with $D\le d$ consecutive $K$-bit chunks, $H_0$ applied to one common bit position of every chunk, followed by truncation $Q_p$, is computed in $O(Vd^{\lambda'})$ time with error below $\sqrt2\,2^{-p}$.; how: Write $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, compute $C^{\otimes D}$ recursively with the complex network, keep every intermediate value exact in a guarded fixed-point format, and truncate once at the end. (on [Simultaneous butterfly layer](simultaneous-layer.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.1.2, S3.1.3, S3.1.4, S3.1.5, S3.1.7, S3.1.8, S3.1.9, S3.1.10). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.1.2**: Conjugating by an address permutation $\mathcal P_M$ whose first columns are the residual basis turns each directional kernel into $C^{\pm1}$ on coordinate slot $h$, i.e. one child operation on the $f$ axes of that slot.
Source: "This is one child operation
on the $f$ axes in slot $h$." (paper)
> To implement \eqref{eq:phase-edge-coordinate} on the group, first apply $\mathcal P_M^{-1}$ separately to each column. For each $1\le h\le\rho_{\rm edge}$, apply $(C^{\epsilon_h})^{\otimes f}$ to the $f$ bits $x_{h,0},\ldots,x_{h,f-1}$. This is one child operation on the $f$ axes in slot $h$. Finally apply $\mathcal P_M$ to every column. A negative directional kernel still requires only one forward child, because \begin{equation}\label{eq:phase-inverse-child} (C^{-1})^{\otimes f} =(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}. \end{equation} The rightmost phase is applied first. All inverse wrappers are address signs and constant fourth-root phases, so they add no recursive calls.

**S3.1.3**: An inverse kernel needs only one forward child, since $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$.
Source: "A negative directional kernel still requires only one
forward child, because" (paper)
> To implement \eqref{eq:phase-edge-coordinate} on the group, first apply $\mathcal P_M^{-1}$ separately to each column. For each $1\le h\le\rho_{\rm edge}$, apply $(C^{\epsilon_h})^{\otimes f}$ to the $f$ bits $x_{h,0},\ldots,x_{h,f-1}$. This is one child operation on the $f$ axes in slot $h$. Finally apply $\mathcal P_M$ to every column. A negative directional kernel still requires only one forward child, because \begin{equation}\label{eq:phase-inverse-child} (C^{-1})^{\otimes f} =(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}. \end{equation} The rightmost phase is applied first. All inverse wrappers are address signs and constant fourth-root phases, so they add no recursive calls.

**S3.1.4**: The change of basis $\mathcal P_M$ is a fixed number of row additions, each XORing corresponding selected positions of two whole slots.
Source: "Thus one row addition changes corresponding selected
positions in two whole slots." (paper)
> Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$ as a product of at most $m(m-1)+3m$ elementary row additions: one clears at most $m-1$ other entries per pivot, and each row swap is three row additions. Reversing the elimination gives the required product since each row addition is an involution. The number is a constant because $m$ is fixed. Adding row $h'$ to row $h$ in every column applies $x_{h,j}\leftarrow x_{h,j}\mathbin\oplus x_{h',j}$ for every $0\le j<f$. Thus one row addition changes corresponding selected positions in two whole slots. The packed address operation proved below performs all of these XORs together.

**S3.1.5**: Applying the network with these column frames to $e=mf$ selected axes gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and yields $C^{\otimes e}$ on every role.
Source: "Summing its residual dimensions gives exactly
$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot." (paper)
> \paragraph{The exact recursive contract.} Apply the finite network with these column frames to a group of $e=mf$ selected axes. Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot. The source and sink $Z_{a,f}$ signs, together with the scalar $i^{27f}$ at each affected sink, turn every endpoint kernel into a forward one. Negating the prescribed physical bank and undoing its exchange returns each result to its original role. Proposition~\ref{prop:complex-motif-interface} therefore gives $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary. Formula~\eqref{eq:phase-inverse-child} supplies each inverse child from one forward call, and none of the corrections adds a child. The remaining operations are a fixed number of binary row additions and coefficientwise scalar operations.

**S3.1.7**: Each binary change of basis and its inverse cost $O(V((eK)^\tau+1))$ on a stream of volume $V$.
Source: "the complete change of basis and its inverse therefore cost
$O(V((eK)^\tau+1))$ on a stream of volume $V$." (paper)
> Under the asymptotic hypotheses in the final assertion of that lemma, the complete change of basis and its inverse therefore cost $O(V((eK)^\tau+1))$ on a stream of volume $V$. Here $e$ counts axis chunks, while $eK$ counts address bits; the fixed factor $m$ between $eK$ and the slot width does not affect the bound. The same conclusion holds after the row padding and splitting below, because every role stream retains a complete suffix with the same fixed field lengths in every row.

**S3.1.8**: Applying $C$ individually to the first $q_0$ chunks lets their bits serve as a row index of range at least $W^{k_0}$, padded to a multiple of $W^{k_0}$.
Source: "Otherwise apply \(C\) individually on the selected bits of the first
\(q_0\) chunks, in \(O(V\log d)\) time." (paper)
> \paragraph{Where the rows come from.} Put \[ q_0=\lceil\log_2 W\rceil\, \lceil\log_m(2d)\rceil, \qquad k_0=\lceil\log_m d\rceil. \] If \(D\le q_0\), use individual \(C\) kernels, at cost \(O(V\log d)\). Otherwise apply \(C\) individually on the selected bits of the first \(q_0\) chunks, in \(O(V\log d)\) time. These chunks remain a complete consecutive address block before all the remaining chunks; regard their concatenated bits as one row index. Its range has length \(R_{\rm row}=2^{q_0K}\ge W^{k_0}\), since \(K\ge1\) for sufficiently large \(p\) and \(q_0K\ge k_0\log_2W\). Within each preceding prefix, add the same number of zero rows to reach the next multiple of \(W^{k_0}\); the volume grows by a factor at most two. At any recursive depth \(j\le k_0\), the row count is divisible by \(W^{k_0-j}\).

**S3.1.9**: The normalized cost satisfies $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, because the $s$ children run on streams of volume $V/W$.
Source: "Dividing by
the current volume \(V\) gives the factor \(s/W\)." (paper)
> \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).

**S3.1.10**: Summing over the base-$m$ pieces and the row preprocessing gives normalized cost $O(d^{\lambda'})$ for $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$.
Source: "Adding their costs and the row preprocessing gives" (paper)
> Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\). Partition the remaining chunks into \(a_j\) consecutive pieces containing \(m^j\) chunks for each \(j\). There are at most \((m-1)(1+\lfloor\log_m d\rfloor)\) pieces. Adding their costs and the row preprocessing gives \[ O\!\left(\log(2d) \bigl[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1\bigr]\right) =O(d^{\lambda'}) \] for any fixed \[ \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1. \] The case \(D\le q_0\), in which preprocessing would consume all active chunks, was handled by individual kernels. Thus all constants and all tape counts are independent of \(p,d,r\) and the input data.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S3.1.1 (on [Binary phase interface of the complex network](phase-interface.md)): With phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{q_U(x)})H^{\otimes m}$, each edge's frame change of the complex network is a product of one translation kernel $aI+bX_v$ (or its inverse) per orthonormal residual vector, these total $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$, and after diagonal corrections every role receives $C^{\otimes m}$.
- S3.1.6 (on [Packed selected-bit addition](packed-addition.md)): For three $L$-bit chunks $x,y,z$ with $L=fK$, the XORs $y_{j_i}\gets y_{j_i}\oplus x_{j_i}$ at positions $j_i=\rho+iK$ are performed while restoring $z$, in time $O(V(L^\tau+1))$ under the layer's parameter growth.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Linear maps, matrices and rank](linear-algebra.md)
- [Row splitting among wire roles](row-splitting.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Binary phase interface of the complex network](phase-interface.md): Using phase frames 𝒞_U = H^{⊗m}·diag(i^{q_U(x)})·H^{⊗m} on the complex network so that each edge's frame change is a product of one translation kernel aI + bX_v per orthonormal residual vector and the whole network yields C^{⊗m} on every role.
  Shown as: Recursive C-layer via phase frames *<predicate>* Binary phase interface of the complex network
- [Packed selected-bit addition](packed-addition.md): XORing the selected bits of one address chunk into the corresponding bits of another using eight packed cyclic shifts guarded by a third chunk, then deterministically repairing the small set of addresses where guards overflow.
  Shown as: Recursive C-layer via phase frames *<predicate>* Packed selected-bit addition
- [Volume-normalized recursion and the power saving](power-saving-recursion.md): The recurrence F(mf) ≤ (s/W)·F(f) + overhead for cost divided by volume, which, because s/W < m, gives cost O(V·e^τ) with τ < 1 instead of O(V·e) for a parameter e.
  Shown as: Recursive C-layer via phase frames *<predicate>* Volume-normalized recursion and the power saving
- [Fixed-tape depth-first schedule](fixed-tape-schedule.md): Running the recursion on a fixed set of tapes by parking the inactive role streams on a stack tape before each child call and restoring them afterward, at O(V) cost per node.
  Shown as: Recursive C-layer via phase frames *<predicate>* Fixed-tape depth-first schedule

## Pages that build on this one

- Simultaneous butterfly layer: The procedure applying H₀ on the same bit position in up to d address chunks of an array of polynomial records at once in O(V·d^{λ′}) time, λ′ < 1, evaluating exactly with guard bits and truncating once.

## Other pages you may link to

- [The n log n conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Polynomial ring modulo yʳ + 1](negacyclic-ring.md)
- [Normalized butterfly H₀](normalized-butterfly.md)
- [Gaussian dyadic fixed-point arithmetic](fixed-point.md)
- [Signed Kronecker packing](signed-packing.md)
- [Lexicographic array layout and logical volume](array-layout.md)
- [Elementary stream operations](elementary-streams.md)
- [Modular arithmetic and finite fields](modular-arithmetic.md)
- [Address shear](address-shear.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Linear maps, matrices and rank](linear-algebra.md)
- [Linear network with wire roles](linear-network.md)
- [Row splitting among wire roles](row-splitting.md)
- [Frames and the common-frame identity](frames.md)
- [Restoring scratch values](scratch-restoration.md)
- [Lower triangular (Bruhat) factorization](bruhat.md)
- [Nondegenerate bilinear forms and orthogonal complements](bilinear-forms.md)
- [Three-element subset construction](triple-construction.md)
- [Three-stage bank exchange](bank-exchange.md)
- [Tensor products](tensor-product.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank deficit s < Wm](rank-deficit.md)
- [Rational matrix interface of the bit network](bit-interface.md)
- [Matrix shear by rank-many interchanges](matrix-shear.md)
- [Power-width interchange](power-width-interchange.md)
- [Fast address-chunk interchange](chunk-swap.md)
- [Two-point kernel C](kernel-c.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit reduction](radix-reduction.md)
- [Chinese-remainder convolution map](crt-map.md)
- [Normalized discrete Fourier transform](dft.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein's chirp identity](bluestein.md)
- [Contractions and error accounting](contraction-errors.md)
- [Resampling with retained permutations](resampling-retained.md)
- [Source permutation cancellation](source-perm-cancel.md)
- [Transform layout and cost](transform-layout.md)
- [Ring convolution from the retained layout](synthetic-convolution.md)
- [Coefficient twist](coefficient-twist.md)
- [Tensor resampling interface](tensor-resampling.md)
- [Size parameters and prime source lengths](parameters.md)
- [Computed source transform](source-transform.md)
- [Precision analysis and exact recovery](precision-recovery.md)
- [Cost table and the exponent κ](cost-accounting.md)
- [Integer multiplication in O(n (lg n)^{1−κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Its phase frames express a $C$ tensor product using smaller groups of selected bits, separated by binary changes of basis." (paper)

  > We first construct tensor products of the auxiliary two-point kernel $C$ from Proposition~\ref{prop:complex-motif-interface}. Its phase frames express a $C$ tensor product using smaller groups of selected bits, separated by binary changes of basis. We implement those changes by moving whole address chunks. Splitting complete rows among the network's wire roles then reduces the volume of each recursive call. Finally, we bound the intermediate dyadic values and convert the completed $C$ layer to the normalized $H_0$ layer. The entire layer is evaluated exactly before one final truncation.

- "Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot." (paper)

  > \paragraph{The exact recursive contract.} Apply the finite network with these column frames to a group of $e=mf$ selected axes. Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot. The source and sink $Z_{a,f}$ signs, together with the scalar $i^{27f}$ at each affected sink, turn every endpoint kernel into a forward one. Negating the prescribed physical bank and undoing its exchange returns each result to its original role. Proposition~\ref{prop:complex-motif-interface} therefore gives $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary. Formula~\eqref{eq:phase-inverse-child} supplies each inverse child from one forward call, and none of the corrections adds a child. The remaining operations are a fixed number of binary row additions and coefficientwise scalar operations.


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

Write the body to `exegenius/tasks/0036-write-recursive-c-layer.answer.md` and the JSON to `exegenius/tasks/0036-write-recursive-c-layer.answer.json`, then run `exegenius submit 0036-write-recursive-c-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0036-write-recursive-c-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
