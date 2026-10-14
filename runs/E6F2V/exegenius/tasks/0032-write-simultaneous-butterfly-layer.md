# exegenius task 0032-write-simultaneous-butterfly-layer

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F2V` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: fluent in asymptotic analysis, discrete mathematics (sets, functions, modular arithmetic, primes and gcd, permutations, induction and recursion), first-course linear algebra (matrices, invertibility, rank, basis, dimension, linear maps over the rationals and the complex numbers), complex arithmetic with Euler's formula, and the basic Turing machine model with tapes and step counting. They have seen binary representation, bit operations such as XOR, and perhaps the idea of multiplying integers by divide and conquer, but have not been taught the discrete Fourier transform, the FFT, polynomial transforms, Schönhage–Strassen, abstract ring theory beyond the basic definition, tensor products, or numerical error analysis, and these are what the wiki must explain.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- The n log n optimality conjecture
- Fixed finite-tape Turing machine model
- Arrays, address fields and elementary scans
- Controlled cyclic shifts and rational scalings
- Integer multiplication as digit convolution
- Normalized DFT and cyclic convolution
- Multidimensional (tensor) Fourier transform
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Fixed-point disk-grid arithmetic and contractions
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): the formal variable of the polynomials, subject to y^r = -1.
  - $r$ (record length): the number of complex coefficients in a polynomial record, a power of two.
- Synthetic Fourier transform modulo y^r + 1
  - $y$ (ring variable): the formal variable of the polynomial ring, subject to y^r = -1.
  - $r$ (record length): the number of complex coefficients in a polynomial record, a power of two.
- Radix-2 butterfly layers and stored frequency order
- Twist from cyclic to negacyclic convolution
- Established n log n multiplier as a subroutine
- Signed Kronecker packing of polynomial products
- Bluestein's chirp identity
- Three-element subset intersection gadget
- Linear network that exchanges two banks and restores scratch values
- Frames and the common-frame identity
- Orthogonal complements and projections in a bilinear space
- Nested subspace labels and the rank saving
- Lower-triangular rank factorization
- Cost of a rational matrix shear
- Power-width chunk interchange in O(Ve^τ) time
  - $V$ (stored bit volume): the number of data bits stored in the array.
  - $e$ (chunk width): the number of radix digits in each of the two interchanged chunks, a power of a fixed integer m.
  - $\tau$ (interchange exponent): a fixed rational constant strictly between 0 and 1.
- Chunk interchange in O(Vu^τ) time
  - $V$ (stored bit volume): the number of data bits stored in the array.
  - $u$ (chunk width): the number of bits in each of the two interchanged address chunks.
  - $\tau$ (interchange exponent): a fixed rational constant strictly below 1, namely 1 - 2^{-50}.
- Two-point kernel C and the complex phase network
- Packed XOR of selected bits across address chunks
- Modular arithmetic and residues (also: congruence, mod q, Z/qZ, integers modulo q, remainder)
- Primes, divisibility, gcd and coprimality (also: prime number, coprime, relatively prime, pairwise coprime, greatest common divisor, odd prime, units mod q, invertible residue)
- Binary representation of integers (also: bit string, radix 2, binary expansion, most significant bit, val(x), bin_k(z), padding with zeros, base-2 digits)
- Bitwise XOR (also: exclusive or, XOR combination, addition mod 2, parity)
- Logarithms, floors, ceilings and powers of two (also: lg, log base 2, floor, ceiling, power of two, exponent rules)
- Matrices, invertibility and rank (also: invertible matrix, matrix inverse, matrix product, rank of a matrix, linear map, linear transformation, Gaussian elimination, row operations)
- Vector spaces, basis and dimension (also: subspace, span, linear independence, linear combination, vector space over the rationals, dimension, standard basis, direct sum)
- Permutations and permutation matrices (also: bijection, reordering of indices, sorting by a permutation, permutation of coordinates, identity matrix)
- Lexicographic order and index tuples (also: dictionary order, Cartesian product of index sets, multi-index, mixed-radix positional notation, row-major order)
- Euler's formula and roots of unity as points on the unit circle (also: e^{i theta}, cos and sin form, unit circle, primitive root of unity, modulus of a complex number, complex conjugate, real and imaginary parts)
- Geometric series and orthogonality of sums of roots of unity (also: geometric sum, sum of powers of a root of unity vanishes, summation manipulation, Kronecker delta, indicator function)
- Norms and the triangle inequality (also: absolute value bound, sup norm, maximum norm, Euclidean norm, error bound, triangle inequality, operator norm)
- Rational numbers, dyadic rationals and exact arithmetic (also: dyadic number, dyadic rational, power-of-two denominator, Gaussian rational, Gaussian integer, rounding to nearest integer, truncation toward zero)
- Algebraic structures: groups, rings and isomorphisms (also: ring, commutative ring, algebra, ring isomorphism, group, cyclic group, zero divisor, unit, field)
- Discrete-math proof techniques (also: induction, recursion, recurrence relation, divide and conquer, proof by cases, pigeonhole principle, counting arguments)
- Schoolbook multiplication and divide-and-conquer multiplication (also: long multiplication, quadratic-time multiplication, Karatsuba, carry propagation, digit-by-digit addition)
- Multitape machine cost model and linear-time scans (also: sequential tape access, tape scan, head movement cost, one-pass copy, linear-time tape operations, sorting by merging, bit-level time complexity)
- Complex polynomial evaluation and interpolation (also: evaluating a polynomial at points, coefficient list, degree, polynomial identity, Horner's rule, coefficient extraction)
- Gaussian function (also: bell curve, exp(-x^2), normal density, Gaussian weight)
- Convolution as polynomial multiplication (also: convolution of sequences, sum over i+j=k, linear convolution, Cauchy product, coefficient of a product)
- Quantifiers, sets and basic asymptotic notation beyond big-O (also: little-o, Theta, Omega, sufficiently large n, for all n, worst-case time, lower bound versus upper bound)

## This page

Concept: Simultaneous butterfly layer in O(Vd^λ') time
Gloss: Applies the normalized butterfly H₀ to one bit position in each of d address chunks of polynomial records in one pass, exactly in Gaussian dyadics followed by a single truncation, in O(V d^λ') for a fixed λ' < 1 instead of d whole-array passes.
Heading: Simultaneous butterfly layer in $O(Vd^{\lambda'})$ time

The symbols in this page's heading denote (say so on the page):

- $V$ (stored bit volume): the number of data bits stored in the array of records.
- $d$ (axis count): the number of equal-width address chunks (transform axes) whose selected bit is butterflied simultaneously.
- $\lambda'$ (layer exponent): a fixed rational constant strictly below 1, namely 1 - 2^{-54}.

## This page in the argument

The step: The tensor product $\mathcal H$ of $H_0$ on one selected bit in each of $D\le d$ address chunks of polynomial records is applied in $O(Vd^{\lambda'})$ time with $\lambda'<1$, exactly up to one final truncation.
How: express $H_0^{\otimes D}$ through the Gaussian-dyadic kernel $C^{\otimes D}$, realize $C^{\otimes e}$ by the rank-saving complex network recursively on slots using packed binary basis changes, and bound guard bits
Why: A layer on $D$ axes done one axis at a time costs $D$ passes; the network does all $D$ at once with a per-volume cost $d^{\lambda'}$. (the sources say so: "whereas separate butterfly" (paper))
Striking feature: One layer on all $D$ axes costs only a power $d^{\lambda'}$ with $\lambda'<1$ of the axis count per unit volume, instead of $D$ whole-array passes. (explain why it holds, from the method)

Its sub-steps, in order:

- The kernel $C=H\mathsf SH=aI+bX$ satisfies $H_0=b\mathsf SC\mathsf S$, and the complex bank-exchange network with binary labels makes $C^{\otimes m}$ on every role from translation kernels, one per residual basis vector. (on [Two-point kernel C and the complex phase network](phase-kernel-network.md))
- A layer of $C^{\otimes e}$ on $e=mf$ selected bits reduces to $s$ children on $f$ selected bits each, plus a fixed number of binary row additions and constant phases.
- A row addition $y\gets y\oplus x$ on the selected bit of each of $f$ chunks is done at once, using a third chunk $z$ as temporary space restored for every initial value. (on [Packed XOR of selected bits across address chunks](packed-selected-bits.md))
- The cost per volume of a $C^{\otimes e}$ layer satisfies $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, which sums to $O(d^{\lambda'})$ for $d$ chunks.
- The whole layer is evaluated exactly in Gaussian dyadics with $o(p)$ guard bits, and only one truncation follows.
- The procedure returns $Q_p(\mathcal Hz)$ in $O(Vd^{\lambda'})$ time, in the unit disk and with error below $\sqrt2\,2^{-p}$.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.; how: start from the Gaussian-resampling reduction of multiplication to transforms, make the transforms cheaper by two tape procedures that each save a power of the logarithm, then recover the product exactly and add up all costs (on [Multiplying n-bit integers in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Two tape procedures cost a power of the width less than one per unit volume: interchange of two $u$-bit address chunks in $O(Vu^\tau)$ and a simultaneous butterfly layer on $d$ chunks in $O(Vd^{\lambda'})$.; how: build the elementary scans and one fixed linear exchange network whose edges have total rank $s<Wm$, and derive from it two recursions in which each level multiplies the cost per volume by $s/W<m$

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.5.2, S1.5.4, S1.5.5, S1.5.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.5.2**: A layer of $C^{\otimes e}$ on $e=mf$ selected bits reduces to $s$ children on $f$ selected bits each, plus a fixed number of binary row additions and constant phases.
How: write each edge's residual basis as the first columns of an invertible binary matrix, apply it by packed row additions, run one child kernel per basis vector, and undo the change of basis
- S1.5.2.1: Apply the inverse change of basis to each column, one child $(C^{\epsilon_h})^{\otimes f}$ per residual direction on the $f$ bits in slot $h$, then the change of basis.
  Source: "To implement \eqref{eq:phase-edge-coordinate} on the group, first apply" (paper)
  > To implement \eqref{eq:phase-edge-coordinate} on the group, first apply $\mathcal P_M^{-1}$ separately to each column. For each $1\le h\le\rho_{\rm edge}$, apply $(C^{\epsilon_h})^{\otimes f}$ to the $f$ bits $x_{h,0},\ldots,x_{h,f-1}$. This is one child operation on the $f$ axes in slot $h$. Finally apply $\mathcal P_M$ to every column. A negative directional kernel still requires only one forward child, because \begin{equation}\label{eq:phase-inverse-child} (C^{-1})^{\otimes f} =(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}. \end{equation} The rightmost phase is applied first. All inverse wrappers are address signs and constant fourth-root phases, so they add no recursive calls.
- S1.5.2.2: Any invertible binary matrix of fixed order is a product of a fixed number of elementary row additions.
  Source: "Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$" (paper)
  > Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$ as a product of at most $m(m-1)+3m$ elementary row additions: one clears at most $m-1$ other entries per pivot, and each row swap is three row additions. Reversing the elimination gives the required product since each row addition is an involution. The number is a constant because $m$ is fixed. Adding row $h'$ to row $h$ in every column applies $x_{h,j}\leftarrow x_{h,j}\mathbin\oplus x_{h',j}$ for every $0\le j<f$. Thus one row addition changes corresponding selected positions in two whole slots. The packed address operation proved below performs all of these XORs together.
- S1.5.2.3: The network on $e=mf$ axes uses exactly $s$ child calls, each on the $f=e/m$ axes of one slot.
  Source: "$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot." (paper)
  > \paragraph{The exact recursive contract.} Apply the finite network with these column frames to a group of $e=mf$ selected axes. Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot. The source and sink $Z_{a,f}$ signs, together with the scalar $i^{27f}$ at each affected sink, turn every endpoint kernel into a forward one. Negating the prescribed physical bank and undoing its exchange returns each result to its original role. Proposition~\ref{prop:complex-motif-interface} therefore gives $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary. Formula~\eqref{eq:phase-inverse-child} supplies each inverse child from one forward call, and none of the corrections adds a child. The remaining operations are a fixed number of binary row additions and coefficientwise scalar operations.
- S1.5.2.4: The normalized layer is $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$, with exact Gaussian dyadic phases and scalar.
  Source: "H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D." (paper)
  > \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.

**S1.5.4**: The cost per volume of a $C^{\otimes e}$ layer satisfies $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, which sums to $O(d^{\lambda'})$ for $d$ chunks.
How: split the rows among the $W$ roles, count $s$ children on streams of volume $V/W$, stop at $e<d^{1/2}$ and sum the recurrence, then cut $D$ chunks into base-$m$ groups
- S1.5.4.1: An individual $C$ kernel on a selected bit costs $O(V)$, so $e$ individual kernels cost $O(Ve)$.
  Source: "To apply one \(C\) kernel, use the split from" (paper)
  > To apply one \(C\) kernel, use the split from Lemma~\ref{lem:elementary-streams} at the selected address bit. Call the two streams \(0\) and \(1\) according to that bit. Because that bit has its complete two-element range, the two streams have the same remaining address set in the same order. Their aligned record addresses therefore differ only in the selected bit, and their coefficients are still ordered by the same polynomial index. Scan each pair of records in that order. For corresponding complex coefficients \(u\) from stream \(0\) and \(v\) from stream \(1\), compute \begin{equation}\label{eq:individual-C-pair} C(u,v)= \left(\frac{u+v+i(u-v)}2,\, \frac{u+v-i(u-v)}2\right). \end{equation} Addition, subtraction and halving use the fixed-point con
- S1.5.4.2: The phase construction supplies one recursive call on a slot per residual basis vector, hence exactly $s$ calls.
  Source: "The phase construction supplies one recursive call on a slot for each" (paper)
  > First consider an internal node containing \(e=m^k\) consecutive active chunks, with \(k\ge1\). Split it into \(m\) consecutive slots, each containing \(e/m\) chunks. The phase construction supplies one recursive call on a slot for each vector in an edge residual basis, hence exactly \(s\) calls in one invocation of the network. If the logical volume entering this node is \(V\), binary changes of basis, their inverses, scalar gates, endpoint corrections and reassembly of the physical banks cost \[ O\bigl(V((eK)^\tau+1)\bigr) \] at this node. Each slot has \((e/m)K\) address bits, so Lemma~\ref{lem:packed-selected-bit-rectangle} gives the stated bound for a row addition. The network and all of its \(m\)-dimensional residual bases are fixed, so the total number of row additions is fixed as well. At the same guarded width, the scalar gates cost a constant number of scans of the current volume. Address and descriptor work bounded by any fixed polynomial in \(p\) per record is also absorbed: its ratio to the record's \(\Theta(rp)\) bits tends to zero.
- S1.5.4.3: Splitting row index $u=Wg+w$ across roles gives every role stream the same address shape and volume $V/W$.
  Source: "At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\)," (paper)
  > At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\), and send that entire row to physical wire role \(w\), indexed there by \(g\). Every role stream has the same remaining address shape. Thus a pointwise gate reads the records with the same \(g\) and the same remaining address in its touched roles. The scalar network allows these role values to be arbitrary, so the split supplies its scratch roles from existing rows. Each recursive edge call acts on one role stream with volume exactly \(1/W\) of its parent's logical volume.
- S1.5.4.4: Stopping at $e<d^{\beta}$ with $\beta=1/2$, the cost per volume satisfies $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$.
  Source: "F(e)\le (s/W)F(e/m)+O((eK)^\tau+1)," (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- S1.5.4.5: With $a=s/W\le m^\sigma<m^\lambda$ the internal costs sum to $O(e^\lambda)$.
  Source: "Put \(a=s/W\).  Since \(a\le m^\sigma<m^\lambda\), the internal" (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- S1.5.4.6: Write $D-q_0$ in base $m$ and treat the pieces separately.
  Source: "Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\)." (paper)
  > Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\). Partition the remaining chunks into \(a_j\) consecutive pieces containing \(m^j\) chunks for each \(j\). There are at most \((m-1)(1+\lfloor\log_m d\rfloor)\) pieces. Adding their costs and the row preprocessing gives \[ O\!\left(\log(2d) \bigl[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1\bigr]\right) =O(d^{\lambda'}) \] for any fixed \[ \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1. \] The case \(D\le q_0\), in which preprocessing would consume all active chunks, was handled by individual kernels. Thus all constants and all tape counts are independent of \(p,d,r\) and the input data.
- S1.5.4.7: Adding the pieces and row preprocessing gives $O(d^{\lambda'})$ for any fixed $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$.
  Source: "=O(d^{\lambda'})" (paper)
  > Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\). Partition the remaining chunks into \(a_j\) consecutive pieces containing \(m^j\) chunks for each \(j\). There are at most \((m-1)(1+\lfloor\log_m d\rfloor)\) pieces. Adding their costs and the row preprocessing gives \[ O\!\left(\log(2d) \bigl[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1\bigr]\right) =O(d^{\lambda'}) \] for any fixed \[ \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1. \] The case \(D\le q_0\), in which preprocessing would consume all active chunks, was handled by individual kernels. Thus all constants and all tape counts are independent of \(p,d,r\) and the input data.

**S1.5.5**: The whole layer is evaluated exactly in Gaussian dyadics with $o(p)$ guard bits, and only one truncation follows.
How: bound the depth of additions and halvings along any chain in the recursion, which bounds both denominator and magnitude growth
- S1.5.5.1: The accelerated network is evaluated exactly until an entire normalized butterfly layer is complete; intermediate operators need not be contractions.
  Source: "The accelerated network is evaluated exactly until an entire" (paper)
  > The accelerated network is evaluated exactly until an entire normalized butterfly layer is complete. Its intermediate operators need not be contractions. We now give explicit constants that bound denominator and magnitude growth within one layer.
- S1.5.5.2: Reserving $p+\Delta$ fractional bits and $\Delta+3$ integer bits represents every intermediate coefficient exactly, where $\Delta=\lceil C_0d^{C_1}\rceil$.
  Source: "Thus reserving \(p+\Delta\)" (paper)
  > To see how this count controls numerical size, start with disk-valued coefficients in \(2^{-p}\mathbb Z[i]\). A value at depth \(\ell\) lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most \(2^\ell\). This follows by induction: addition or subtraction can at most double the maximum modulus of its operands; halving adds at most one denominator bit; and signs and multiplication by \(i\) preserve both bounds. The charge of \(t\) for the final shift is the same as \(t\) successive halvings. Thus reserving \(p+\Delta\) fractional bits and \(\Delta+3\) integer and sign bits per real component represents every intermediate coefficient exactly and prevents overflow. Shifts consume the reserved fractional zeros and discard no bits.
- S1.5.5.3: With $\epsilon C_1<1$ the guard width is $o(p)$ and the full coefficient width is $O(p)$.
  Source: "Choose \(\epsilon C_1<1\).  Since \(d=\Theta(p^\epsilon)\)," (paper)
  > Choose \(\epsilon C_1<1\). Since \(d=\Theta(p^\epsilon)\), \(\Delta=o(p)\), and the full coefficient width is \(O(p)\), as required in the time analysis. Addition, signed shifts, copying and phase changes consequently take \(O(p)\) bit operations per coefficient.

**S1.5.6**: The procedure returns $Q_p(\mathcal Hz)$ in $O(Vd^{\lambda'})$ time, in the unit disk and with error below $\sqrt2\,2^{-p}$.
Source: "coefficient order, and component format in $O(Vd^{\lambda'})$ time," (paper)
> The procedure returns $Q_p(\mathcal H z)$ in the same array, coefficient order, and component format in $O(Vd^{\lambda'})$ time, uniformly over all these choices of $p,d,r,D,P,S,\rho,w$ and $z$. Every returned coefficient belongs to the complex unit disk, and, in the maximum coefficient norm, \[ \|Q_p(\mathcal H z)-\mathcal H z\|_\infty <\sqrt2\,2^{-p}. \] The procedure evaluates the entire layer exactly before this final truncation. Put \[ C_0=128m\bigl(s_{\rm c}+64(W_{\rm c}+m+1)^3\bigr)^2, \] where $m,W_{\rm c},s_{\rm c}$ are the fixed constants of Proposition~\ref{prop:complex-motif-interface}. The procedure uses at most $p+\lceil C_0d^{C_1}\rceil$ fractional bits and $\lceil C_0d^{C_1}\rceil+3$ integer and sign bits per real component internally; these widths are $O(p)$. The time includes address changes, deterministic repair, row padding and its removal, and fixed-tape workspace cleanup. Its tape count is fixed, and its time constant is independent of the allowed array lengths and coefficient values. \end{proposition}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.5.1 (on [Two-point kernel C and the complex phase network](phase-kernel-network.md)): The kernel $C=H\mathsf SH=aI+bX$ satisfies $H_0=b\mathsf SC\mathsf S$, and the complex bank-exchange network with binary labels makes $C^{\otimes m}$ on every role from translation kernels, one per residual basis vector.
- S1.5.3 (on [Packed XOR of selected bits across address chunks](packed-selected-bits.md)): A row addition $y\gets y\oplus x$ on the selected bit of each of $f$ chunks is done at once, using a third chunk $z$ as temporary space restored for every initial value.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Two-point kernel C and the complex phase network](phase-kernel-network.md): The Gaussian-dyadic two-point kernel C = H S H = aI + bX (a = (1+i)/2, b = (1−i)/2) satisfies H₀ = b S C S; the complex bank-exchange network with binary labels makes C^{⊗m} on every role from products of translation kernels, one per residual basis vector.
  Shown as: Simultaneous butterfly layer in O(Vd^λ') time *<predicate>* Two-point kernel C and the complex phase network
- [Packed XOR of selected bits across address chunks](packed-selected-bits.md): A binary row addition y ← y ⊕ x on the selected bit of each of f chunks at once, done by a constant number of cyclic shifts of whole chunk ranges followed by deterministic repair of a small explicit set of bad addresses, using a third chunk as restored temporary space.
  Shown as: Simultaneous butterfly layer in O(Vd^λ') time *<predicate>* Packed XOR of selected bits across address chunks
- [Fixed-point disk-grid arithmetic and contractions](fixed-point-disk-grid.md): Complex numbers stored as signed two's-complement integers scaled by 2^{-p} inside the unit disk; truncation Q_p toward zero costs error below √2·2^{-p}, and contractions never increase the sup norm so errors add up predictably.
  Shown as: Simultaneous butterfly layer in O(Vd^λ') time *<predicate>* Fixed-point disk-grid arithmetic and contractions
- [Radix-2 butterfly layers and stored frequency order](butterfly-layers.md): Decimation in frequency: each level combines entries k and k+t/2 by the two-point butterfly H₀ and a twiddle monomial, leaving frequencies stored in bit-reversed order, which the opposite transform consumes directly.
  Shown as: Simultaneous butterfly layer in O(Vd^λ') time *<predicate>* Radix-2 butterfly layers and stored frequency order
- [Power-width chunk interchange in O(Ve^τ) time](power-width-interchange.md): Recursively interchanges two chunks of e = m^k digits by running the bank-exchange network on W role streams of volume V/W, each edge costing rank-many smaller interchanges; since s/W < m^τ the cost per volume is O(e^τ).
  Shown as: Simultaneous butterfly layer in O(Vd^λ') time *<predicate>* Power-width chunk interchange in O(Ve^τ) time

## Pages that build on this one

- Layout and cost of the synthetic transform: A positional layout permutation puts the selected bits of all axes at a common offset in K-bit chunks so each transform round is one simultaneous layer; the forward transform keeps its output order for the pointwise product and the opposite transform.
- Cost accounting and the saving exponent κ: A table of costs divided by Tp, each at most p^{1−2κ} thanks to the slack in the chosen exponents (seven dominant margins, the smallest 2^{-181} = 2κ), giving O(n (log n)^{1−κ}) overall.

## Other pages you may link to

- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Three-element subset intersection gadget](triple-gadget.md)
- [Linear network that exchanges two banks and restores scratch values](bank-exchange-network.md)
- [Fixed finite-tape Turing machine model](fixed-tape-model.md)
- [Established n log n multiplier as a subroutine](nlogn-subroutine.md)
- [Arrays, address fields and elementary scans](stream-arrays.md)
- [Frames and the common-frame identity](frames.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Orthogonal complements and projections in a bilinear space](bilinear-orthogonal.md)
- [Nested subspace labels and the rank saving](subspace-labels.md)
- [Lower-triangular rank factorization](triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Chunk interchange in O(Vu^τ) time](chunk-swap.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed Kronecker packing of polynomial products](signed-kronecker-packing.md)
- [Normalized DFT and cyclic convolution](dft-cyclic-convolution.md)
- [Multidimensional (tensor) Fourier transform](multidim-transform.md)
- [Chinese-remainder map to prime cyclic axes](crt-axis-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Twist from cyclic to negacyclic convolution](coefficient-twist.md)
- [Synthetic Fourier transform modulo y^r + 1](synthetic-transform.md)
- [Layout and cost of the synthetic transform](transform-layout.md)
- [Convolution over the polynomial ring from the retained layout](ring-convolution.md)
- [Resampling with the permutations left in the transform](resampling-no-sort.md)
- [Chirp identity and source-permutation cancellation](chirp-permutation-cancel.md)
- [Choice of sizes, precision and prime axis lengths](parameter-choice.md)
- [Source transform via resampling, chirp and ring convolution](source-transform.md)
- [Exact recovery: scaling, rounding and carries](exact-recovery.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the saving exponent κ](cost-accounting.md)
- [Multiplying n-bit integers in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "coefficient order, and component format in $O(Vd^{\lambda'})$ time" (paper)

  > The procedure returns $Q_p(\mathcal H z)$ in the same array, coefficient order, and component format in $O(Vd^{\lambda'})$ time, uniformly over all these choices of $p,d,r,D,P,S,\rho,w$ and $z$. Every returned coefficient belongs to the complex unit disk, and, in the maximum coefficient norm, \[ \|Q_p(\mathcal H z)-\mathcal H z\|_\infty <\sqrt2\,2^{-p}. \] The procedure evaluates the entire layer exactly before this final truncation. Put \[ C_0=128m\bigl(s_{\rm c}+64(W_{\rm c}+m+1)^3\bigr)^2, \] where $m,W_{\rm c},s_{\rm c}$ are the fixed constants of Proposition~\ref{prop:complex-motif-interface}. The procedure uses at most $p+\lceil C_0d^{C_1}\rceil$ fractional bits and $\lceil C_0d^{C_1}\rceil+3$ integer and sign bits per real component internally; these widths are $O(p)$. The time includes address changes, deterministic repair, row padding and its removal, and fixed-tape workspace cleanup. Its tape count is fixed, and its time constant is independent of the allowed array lengths and coefficient values. \end{proposition}

- "whereas separate butterfly factors would require $D$ whole-array passes" (paper)

  > The parameters will satisfy \[ d=\Theta(p^\epsilon),\qquad K=\lfloor d^c\rfloor, \qquad r=2^{\Theta(p/d)},\qquad c>0,\quad 0<\epsilon<1. \] The exponents and comparison constants are fixed, and we impose their further restrictions in Proposition~\ref{prop:simultaneous-layer}. Two consequences explain the layout. The polynomial length $r$ grows faster than every fixed power of $p$, so a scan of a record pays for polynomial work on its address. Also $K/\log p\to\infty$, which will make the exceptional set in a packed change of address bits small enough to repair by sorting. We will obtain cost $O(Vd^{\lambda'})$, with $\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly factors would require $D$ whole-array passes.

- "The procedure evaluates the entire layer exactly before this final truncation." (paper)

  > The procedure returns $Q_p(\mathcal H z)$ in the same array, coefficient order, and component format in $O(Vd^{\lambda'})$ time, uniformly over all these choices of $p,d,r,D,P,S,\rho,w$ and $z$. Every returned coefficient belongs to the complex unit disk, and, in the maximum coefficient norm, \[ \|Q_p(\mathcal H z)-\mathcal H z\|_\infty <\sqrt2\,2^{-p}. \] The procedure evaluates the entire layer exactly before this final truncation. Put \[ C_0=128m\bigl(s_{\rm c}+64(W_{\rm c}+m+1)^3\bigr)^2, \] where $m,W_{\rm c},s_{\rm c}$ are the fixed constants of Proposition~\ref{prop:complex-motif-interface}. The procedure uses at most $p+\lceil C_0d^{C_1}\rceil$ fractional bits and $\lceil C_0d^{C_1}\rceil+3$ integer and sign bits per real component internally; these widths are $O(p)$. The time includes address changes, deterministic repair, row padding and its removal, and fixed-tape workspace cleanup. Its tape count is fixed, and its time constant is independent of the allowed array lengths and coefficient values. \end{proposition}


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

Write the body to `exegenius/tasks/0032-write-simultaneous-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0032-write-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0032-write-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0032-write-simultaneous-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
