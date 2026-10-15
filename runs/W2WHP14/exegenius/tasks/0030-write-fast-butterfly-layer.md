# exegenius task 0030-write-fast-butterfly-layer

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/W2WHP14` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (modular arithmetic, primes and coprimality, the Chinese remainder theorem, permutations, induction, recurrences), calculus-level analysis (logarithms, floor and ceiling, norms and rounding errors), linear algebra (vectors, matrices, invertibility, rank, over the reals, complex numbers and F2), and algorithms (asymptotic notation, schoolbook multiplication, divide and conquer, sorting) with a first look at the FFT. They know basic multitape Turing machines and tapes, polynomials and complex numbers including roots of unity. They have not met Schoenhage-Strassen or Karatsuba-level multiplication algorithms in depth, ring and group-algebra language beyond polynomials, tensor products, numerical error analysis of fixed-point transforms, or any research literature on integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n conjecture for integer multiplication (also: n log n optimality conjecture, Schönhage–Strassen conjecture)
- Established n log n multiplier
- Arrays, addresses and volume on tapes (also: address field, logical volume)
- Elementary stream operations (also: split and merge, row splitting)
- Controlled cyclic shifts (also: controlled shifts, ordered affine streams)
- Rank, subspaces and orthogonal complements (also: nondegenerate subspace, orthogonal residual)
- Cyclic convolution (also: convolution)
- Discrete Fourier transform (also: Fourier transform, DFT)
- Multidimensional (tensor) transform (also: tensor transform)
- Two-point butterfly (also: H₀, butterfly operation)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring, R_r)
  - $y$ (ring variable): The formal polynomial variable, whose powers y^a act as roots of unity of order 2r.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform (also: Nussbaumer polynomial transform, stored frequency order)
- Signed packing of polynomial products (also: Kronecker substitution)
- Linear exchange network with restored scratch wires (also: bank exchange, finite network, role)
- Frames on wire arrays (also: frame, common-frame identity)
- Subspace labels from three-element subsets (also: rank saving construction, orthogonal residual labels)
- Address shear and lower-triangular factorization (also: Bruhat factorization, matrix shear)
- Recursive rank saving (also: power saving recurrence)
- Fast address-chunk interchange (also: chunk swap, tape interchange)
- Phase frames and the two-point kernel C (also: binary phase interface, C kernel)
- Packed selected-bit addition (also: packed XOR, exceptional address repair)
- Fixed-point disk-grid arithmetic (also: disk grid, Gaussian dyadics, truncation Q_p)
- Coefficient (phase) twist (also: twist)
- Bluestein chirp identity (also: chirp identity, chirp transform)
- Integer product as digit convolution (also: radix-2^b digits)
- Rounding and carry propagation (also: exact recovery, carry propagation)
- Logarithms and iterated logarithm notation (also: log, lg, log base 2, log2, powers of the logarithm, (lg n)^c)
- Big-Omega, Theta and little-o notation (also: Omega, Theta, Ω, Θ, little-o, asymptotic lower bound, tight bound)
- Binary representation and bit operations (also: binary strings, bits, XOR, exclusive or, bitwise operations, two's complement, Hamming weight, bit length)
- Modular arithmetic (also: congruence, residues mod m, Z/mZ, integers modulo m, centered residue, mod, wraparound)
- Primes, coprimality and gcd (also: prime numbers, pairwise coprime, relatively prime, greatest common divisor, gcd, Euclidean algorithm, prime number theorem, primes just below a number)
- Chinese remainder theorem (also: CRT, Chinese remainder, residues modulo coprime moduli)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, Euler's formula, twiddle factor, ω)
- Vectors, matrices and invertibility (also: matrix multiplication, matrix inverse, invertible matrix, linear map, linear combination, lower-triangular matrix, permutation matrix, identity matrix, transpose, linear operator)
- Finite field F2 arithmetic (also: GF(2), binary field, mod 2 arithmetic, Z/2Z, F_2)
- Permutations and Cartesian products (also: bijection, permutation of indices, index set, product set, multi-index, coordinate permutation, lexicographic order, mixed-radix indexing, row-major order)
- Floor, ceiling and summation notation (also: floor function, ceiling function, ⌊x⌋, ⌈x⌉, sigma notation, geometric series, indicator vector)
- Recurrences and induction (also: recurrence relation, solving recurrences, unrolling a recurrence, proof by induction, master theorem, divide and conquer recurrence)
- Norms, absolute values and error bounds (also: max norm, sup norm, infinity norm, triangle inequality, modulus bound, rounding error, truncation error, round to nearest integer, unit disk)
- Fast Fourier transform and divide and conquer (also: FFT, Cooley-Tukey, fast Fourier transform, O(n log n) transform, convolution theorem, multiplying polynomials by FFT)
- Sorting and data movement on tapes (also: sorting, merge, scan, linear scan, stream, sequential access)
- Finite alphabet encodings and constant-factor simulation (also: alphabet, constant overhead, constant factor slowdown, encoding data as tape symbols, fixed finite state control, Turing machine simulation)
- Ring and group notions for polynomials (also: commutative ring, ring with identity, quotient ring, isomorphism, ring homomorphism, unit of a ring)

## This page

Concept: Fast simultaneous butterfly layer
Gloss: The second tape procedure: applying H₀ at the same bit offset in d address chunks of a polynomial-record array in cost O(V d^λ') with λ'<1, by evaluating the layer exactly through the phase-frame network with packed chunk moves before a single truncation.
Also called: simultaneous normalized butterfly layer

## This page in the argument

The step: Fast simultaneous butterfly layer: $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied coefficientwise at the same bit offset in $D\le d$ address chunks of a polynomial-record array costs $O(Vd^{\lambda'})$ with $\lambda'=1-2^{-54}$, evaluating the whole layer exactly before a single truncation.
How: Express the layer through the complex phase network (kernels $C$ on smaller groups of selected bits separated by binary changes of basis), implement the basis changes by whole-chunk moves and packed selected-bit additions, split complete rows among the $W$ roles for volume $V/W$ per recursive call, and bound the intermediate dyadic values.
Why: The sources contrast the layer with separate butterfly factors, which would need $D$ whole-array passes, whereas the recursion costs $O(Vd^{\lambda'})$. (the sources say so: "factors would require $D$ whole-array passes." (paper))
Striking feature: The layer is evaluated with exact Gaussian dyadic arithmetic on non-contractive intermediate operators and truncated only once at the end, so rounding error does not accumulate over the $D$ simultaneous butterflies. (explain why it holds, from the method)

Its sub-steps, in order:

- Phase frames in butterfly form: $C=H\mathsf SH=aI+bX$ satisfies $H_0=b\mathsf SC\mathsf S$, $C^2=X$, $C^4=I$, $C^{-1}=-iZCZ$; an edge change is $\mathcal P_M(\prod_jC_{e_j}^{\epsilon_j})\mathcal P_M^{-1}$ with $M\in\operatorname{GL}(m,\mathbb F_2)$; on a group of $e=mf$ axes this needs $s_{\rm c}$ child layers on $f$ axes, and $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$. (on [Phase frames and the two-point kernel C](phase-frame-kernel.md))
- Packed selected-bit addition: for $L=fK$, a binary row addition $y_{j_i}\gets y_{j_i}\oplus x_{j_i}$ ($j_i=\rho+iK$, $0\le i<f$) on chunks $x,y$ with an arbitrary third chunk $z$ restored costs $O(V(L^\tau+1))$. (on [Packed selected-bit addition](packed-selected-bit-addition.md))
- Batching a common $C$-layer on $D\le d$ chunks gives per-volume cost $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ with $F(e)=O(e)$ for $e<d^\beta$, which solves to $O(d^{\lambda'})$.
- The accelerated network can be evaluated exactly until a whole layer is complete: every intermediate coefficient needs at most $\Delta=\lceil C_0d^{C_1}\rceil$ extra fractional bits and $\Delta+3$ integer and sign bits, with $C_1=20$ and $C_0=128mB^2$, and $\Delta=o(p)$.
- Proposition (simultaneous normalized layer): for $z$ in the unit disk on the grid $2^{-p}\mathbb Z[i]$ the procedure returns $Q_p(\mathcal Hz)$ in $O(Vd^{\lambda'})$ time, evaluating the whole layer exactly before one truncation, with error $<\sqrt2\,2^{-p}$.

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.; how: Reduce the product to a convolution of short integer coefficients, evaluate the convolution through power-of-two transforms over $\mathbb C[y]/(y^r+1)$, and replace the two tape operations that each cost a factor $\log n$ (address rearrangement and butterfly layers) by procedures whose cost per bit is a power of their parameter below one; then total the costs. (on [Integer multiplication below n log n](main-theorem.md))
- Both tape procedures cost a power of their parameter below one, because each runs a fixed linear exchange network on $W$ wires whose edge changes are smaller calls on role streams of volume $V/W$, with total number of calls $s<Wm$, so that each level of recursion multiplies the cost per volume by $s/W<m^\tau$ while the parameter shrinks by $m$.; how: Build a finite linear exchange network that restores its scratch wires, give its vertices frames so that only endpoint operators matter, attach nested subspace labels so that the total rank $s$ of all edge changes is below $Wm$, and unroll the resulting recursion once with bit gates (address-chunk interchange) and once with Gaussian-dyadic phase gates (simultaneous butterfly layer). (on [Recursive rank saving](rank-saving-recurrence.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.6.3, S4.6.4, S4.6.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.6.3**: Batching a common $C$-layer on $D\le d$ chunks gives per-volume cost $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ with $F(e)=O(e)$ for $e<d^\beta$, which solves to $O(d^{\lambda'})$.
How: Take the first $q_0$ chunks as the row index (supplying a row count divisible by $W^{k_0}$), recurse with the complex network on slots of $e/m$ chunks, and sum the internal-node overhead and the leaves of the recursion, then handle general $D$ by a base-$m$ partition.
- S4.6.3.1: Applying $C$ individually on $e$ selected bits (split on the bit, combine paired records by $C(u,v)=((u+v+i(u-v))/2,(u+v-i(u-v))/2)$, merge) costs $O(Ve)$.
  Source: "Thus \(e\) individual kernels cost" (paper)
  > tion} Addition, subtraction and halving use the fixed-point conventions of Section~\ref{sec:streams}; multiplication by \(i\) swaps the real and imaginary components and changes one sign. The common guarded width makes these operations exact. The coefficient scan costs \(O(rp)\) per pair of records, linear in their guarded bit length and including any reversal of bits inside a coefficient. Write the first result to stream \(0\) and the second to stream \(1\), both in coefficient order, then merge according to the selected bit. The merge restores the original lexicographic address order. The elementary split and merge include their counters and cleanup and cost \(O(V)\); the paired arithmetic scan also costs \(O(V)\). Thus \(e\) individual kernels cost \(O(Ve)\) on any stream with these complete ranges and record format.
- S4.6.3.2: At a node with $e=m^k$ chunks, the $s$ children plus binary basis changes, scalar gates, endpoint corrections and reassembly cost $O(V((eK)^\tau+1))$ at that node.
  Source: "O\bigl(V((eK)^\tau+1)\bigr)" (paper)
  > First consider an internal node containing \(e=m^k\) consecutive active chunks, with \(k\ge1\). Split it into \(m\) consecutive slots, each containing \(e/m\) chunks. The phase construction supplies one recursive call on a slot for each vector in an edge residual basis, hence exactly \(s\) calls in one invocation of the network. If the logical volume entering this node is \(V\), binary changes of basis, their inverses, scalar gates, endpoint corrections and reassembly of the physical banks cost \[ O\bigl(V((eK)^\tau+1)\bigr) \] at this node. Each slot has \((e/m)K\) address bits, so Lemma~\ref{lem:packed-selected-bit-rectangle} gives the stated bound for a row addition. The network and all of its \(m\)-dimensional residual bases are fixed, so the total number of row additions is fixed as well. At the same guarded width, the scalar gates cost a constant number of scans of the current volume. Address and descriptor work bounded by any fixed polynomial in \(p\) per record is also absorbed: its ratio to the record's \(\Theta(rp)\) bits tends to zero.
- S4.6.3.3: Put $q_0=\lceil\log_2W\rceil\lceil\log_m(2d)\rceil$ and $k_0=\lceil\log_md\rceil$; apply $C$ individually on the first $q_0$ chunks ($O(V\log d)$) and use their bits as a row index.
  Source: "q_0=\lceil\log_2 W\rceil\," (paper)
  > \paragraph{Where the rows come from.} Put \[ q_0=\lceil\log_2 W\rceil\, \lceil\log_m(2d)\rceil, \qquad k_0=\lceil\log_m d\rceil. \] If \(D\le q_0\), use individual \(C\) kernels, at cost \(O(V\log d)\). Otherwise apply \(C\) individually on the selected bits of the first \(q_0\) chunks, in \(O(V\log d)\) time. These chunks remain a complete consecutive address block before all the remaining chunks; regard their concatenated bits as one row index. Its range has length \(R_{\rm row}=2^{q_0K}\ge W^{k_0}\), since \(K\ge1\) for sufficiently large \(p\) and \(q_0K\ge k_0\log_2W\). Within each preceding prefix, add the same number of zero rows to reach the next multiple of \(W^{k_0}\); the volume grows by a factor at most two. At any recursive depth \(j\le k_0\), the row count is divisible by \(W^{k_0-j}\).
- S4.6.3.4: The row range $R_{\rm row}=2^{q_0K}\ge W^{k_0}$; padding zero rows to a multiple of $W^{k_0}$ at most doubles the volume, and at recursive depth $j\le k_0$ the row count is divisible by $W^{k_0-j}$.
  Source: "length \(R_{\rm row}=2^{q_0K}\ge W^{k_0}\), since" (paper)
  > \paragraph{Where the rows come from.} Put \[ q_0=\lceil\log_2 W\rceil\, \lceil\log_m(2d)\rceil, \qquad k_0=\lceil\log_m d\rceil. \] If \(D\le q_0\), use individual \(C\) kernels, at cost \(O(V\log d)\). Otherwise apply \(C\) individually on the selected bits of the first \(q_0\) chunks, in \(O(V\log d)\) time. These chunks remain a complete consecutive address block before all the remaining chunks; regard their concatenated bits as one row index. Its range has length \(R_{\rm row}=2^{q_0K}\ge W^{k_0}\), since \(K\ge1\) for sufficiently large \(p\) and \(q_0K\ge k_0\log_2W\). Within each preceding prefix, add the same number of zero rows to reach the next multiple of \(W^{k_0}\); the volume grows by a factor at most two. At any recursive depth \(j\le k_0\), the row count is divisible by \(W^{k_0-j}\).
- S4.6.3.5: A row index $u=Wg+w$ goes entirely to wire role $w$, so every role stream has the same address shape and each recursive call acts on a stream of volume exactly $1/W$ of its parent's.
  Source: "one role stream with volume exactly \(1/W\) of its parent's logical" (paper)
  > At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\), and send that entire row to physical wire role \(w\), indexed there by \(g\). Every role stream has the same remaining address shape. Thus a pointwise gate reads the records with the same \(g\) and the same remaining address in its touched roles. The scalar network allows these role values to be arbitrary, so the split supplies its scratch roles from existing rows. Each recursive edge call acts on one role stream with volume exactly \(1/W\) of its parent's logical volume.
- S4.6.3.6: Fix $\beta=1/2$ and choose rational exponents $0<\tau<1$, $\max\{0,\log_m(s/W)\}\le\sigma<1$, $\max\{\tau,\sigma\}<\lambda<1$ and $\tau(1+c/\beta)<\lambda$.
  Source: "Fix \(\beta=1/2\), and choose real exponents satisfying" (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- S4.6.3.7: Stopping the recursion at $e<d^\beta$ and applying $e$ kernels individually, the cost per volume satisfies $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, $F(e)=O(e)$ for $e<d^\beta$, because the $s$ calls on volume $V/W$ cost $s(V/W)F(e/m)$.
  Source: "F(e)\le (s/W)F(e/m)+O((eK)^\tau+1)," (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- S4.6.3.8: At an internal node $e\ge d^\beta$, so $K\le d^c\le e^{c/\beta}$ and the overhead is $O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)$.
  Source: "At an internal node \(e\ge d^\beta\), hence" (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- S4.6.3.9: With $a=s/W\le m^\sigma<m^\lambda$ the internal costs sum to at most $Ce^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)$.
  Source: "C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)." (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- S4.6.3.10: Leaves after $j$ levels hold $u=e/m^j<d^\beta$ chunks and contribute $O(a^ju)\le O(e^\sigma u^{1-\sigma})\le O(e^\sigma d^{\beta(1-\sigma)})$, using $a^j\le m^{j\sigma}=(e/u)^\sigma$.
  Source: "O(a^ju)\le O(e^\sigma u^{1-\sigma})" (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- S4.6.3.11: Writing $D-q_0=\sum_ja_jm^j$ in base $m$ and handling the at most $(m-1)(1+\lfloor\log_md\rfloor)$ pieces gives total $O(\log(2d)[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1])=O(d^{\lambda'})$ for any fixed $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$.
  Source: "=O(d^{\lambda'})" (paper)
  > Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\). Partition the remaining chunks into \(a_j\) consecutive pieces containing \(m^j\) chunks for each \(j\). There are at most \((m-1)(1+\lfloor\log_m d\rfloor)\) pieces. Adding their costs and the row preprocessing gives \[ O\!\left(\log(2d) \bigl[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1\bigr]\right) =O(d^{\lambda'}) \] for any fixed \[ \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1. \] The case \(D\le q_0\), in which preprocessing would consume all active chunks, was handled by individual kernels. Thus all constants and all tape counts are independent of \(p,d,r\) and the input data.

**S4.6.4**: The accelerated network can be evaluated exactly until a whole layer is complete: every intermediate coefficient needs at most $\Delta=\lceil C_0d^{C_1}\rceil$ extra fractional bits and $\Delta+3$ integer and sign bits, with $C_1=20$ and $C_0=128mB^2$, and $\Delta=o(p)$.
How: Bound the arithmetic dependency depth $A(e)$ of a recursive layer by the recurrence $A(e)\le sA(e/m)+E$ and convert depth to magnitude and denominator growth, since each operation at most doubles the modulus or adds one denominator bit.
- S4.6.4.1: Constants: $E=64(W+m+1)^3$, $B=s+E$ and $\nu=\min\{j\ge1:m^j\ge B\}$.
  Source: "E=64(W+m+1)^3,\qquad B=s+E," (paper)
  > For the complex network, let \[ E=64(W+m+1)^3,\qquad B=s+E, \qquad \nu=\min\{j\ge1:m^j\ge B\}, \] and set \[ C_1=\max\{20,\nu+3\},\qquad C_0=128mB^2, \qquad \Delta=\lceil C_0d^{C_1}\rceil. \] For the stated \(h=100\) construction, the complex network has \[ \begin{split} m&=1{,}000{,}000,\\ W&=1{,}873{,}807{,}244{,}643{,}542{,}670{,}000,\\ s&=1{,}873{,}807{,}244{,}636{,}671{,}267{,}308{,}000{,}000. \end{split} \] These values give \(m^{10}<B<m^{11}\), hence \(\nu=11\) and \(C_1=20\). In fact the bound below needs only exponent fourteen; the choice twenty leaves an explicit additional margin.
- S4.6.4.2: $C_1=\max\{20,\nu+3\}$, $C_0=128mB^2$ and $\Delta=\lceil C_0d^{C_1}\rceil$; for the complex network $m^{10}<B<m^{11}$, hence $\nu=11$ and $C_1=20$.
  Source: "These values give \(m^{10}<B<m^{11}\), hence \(\nu=11\) and" (paper)
  > For the complex network, let \[ E=64(W+m+1)^3,\qquad B=s+E, \qquad \nu=\min\{j\ge1:m^j\ge B\}, \] and set \[ C_1=\max\{20,\nu+3\},\qquad C_0=128mB^2, \qquad \Delta=\lceil C_0d^{C_1}\rceil. \] For the stated \(h=100\) construction, the complex network has \[ \begin{split} m&=1{,}000{,}000,\\ W&=1{,}873{,}807{,}244{,}643{,}542{,}670{,}000,\\ s&=1{,}873{,}807{,}244{,}636{,}671{,}267{,}308{,}000{,}000. \end{split} \] These values give \(m^{10}<B<m^{11}\), hence \(\nu=11\) and \(C_1=20\). In fact the bound below needs only exponent fourteen; the choice twenty leaves an explicit additional margin.
- S4.6.4.3: Every physical wire occurs in at most twelve scalar gates (four per stage), so there are at most $12W$ gates; a gate has at most $W$ inputs, coefficients in $\{0,\pm1,\pm1/2\}$, and evaluating all its outputs from saved inputs takes at most $2W^2$ operations.
  Source: "physical wire occurs in at most twelve scalar gates, and there are" (paper)
  > The scalar schedule \eqref{eq:motif-schedule} touches a data wire at most four times in each of the three stages. A scratch wire belongs to one invocation and is touched at most four times there. Thus every physical wire occurs in at most twelve scalar gates, and there are at most \(12W\) gates. A gate has at most \(W\) inputs and outputs and coefficients in \(\{0,\pm1,\pm1/2\}\). One output is a sum of at most \(W\) terms, each requiring at most one halving and one addition or subtraction. Evaluating all outputs from saved inputs therefore takes at most \(2W^2\) elementary operations.
- S4.6.4.4: Inverse-child corrections need at most $4s$ operations, source, sink and bank corrections at most $4W+4$, so the per-invocation total $24W^3+4s+4W+4$ is less than $E$ because $s<Wm$.
  Source: "\(24W^3+4s+4W+4\) is less than" (paper)
  > For an inverse child, each \(Z^{\otimes f}\) is one sign chosen by the parity of the selected address bits, and the scalar fourth-root phase takes at most one sign change and one multiplication by \(i\). This gives at most \(4s\) operations for the child corrections. The source, sink and bank corrections take at most \(4W+4\) more. Calculating the address parities and phase exponents is address or descriptor work, not arithmetic on coefficients. Since \(s<Wm\), the total \(24W^3+4s+4W+4\) is less than \(E=64(W+m+1)^3\). Binary address permutations add no coefficient arithmetic at their interfaces.
- S4.6.4.5: The arithmetic depth satisfies $A(e)\le sA(e/m)+E$ at an internal node and $A(e)\le8e$ at a leaf (the depth estimate concatenates the $s$ calls, so it uses $s$, not $s/W$).
  Source: "A(e)\le sA(e/m)+E" (paper)
  > The paired evaluation in \eqref{eq:individual-C-pair} uses at most eight elementary operations: form the sum and difference, multiply the difference by \(i\), then form the two half-sums. We may therefore use \[ A(e)\le sA(e/m)+E \quad\hbox{at an internal node},\qquad A(e)\le8e \quad\hbox{at a leaf}. \] The depth estimate concatenates the \(s\) calls, so it uses \(s\). The factor \(1/W\) in the earlier time recurrence accounted for their smaller stream volumes.
- S4.6.4.6: With at most $\lceil\log_md\rceil$ levels, $sx+E\le Bx$ and $B^{k+1}\le B^2d^\nu$, so $A(e)\le8dB^{k+1}\le8B^2d^{\nu+1}$.
  Source: "A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}." (paper)
  > There are at most \(k\le\lceil\log_m d\rceil\) internal levels. For any bound \(x\ge1\), \(sx+E\le(s+E)x=Bx\). Starting with \(8e\le8d\le8dB\) at a leaf and applying this inequality through the levels gives the first bound below. For the second, use \(B\le m^\nu\) and \[ B^{k+1}\le B^{\log_m d+2} =B^2d^{\log_m B}\le B^2d^\nu. \] Thus \[ A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}. \] For the sufficiently large sizes under consideration, the earlier piece count is at most \(md\). Concatenating their depths contributes at most \(8mB^2d^{\nu+2}\). In either preprocessing branch, at most \(d\) individual kernels are used, contributing at most \(8d\). Splitting rows, padding, copying and removing padding add no coefficient arithmetic.
- S4.6.4.7: Adding the base-$m$ pieces ($\le md$ of them), at most $d$ individual kernels and the diagonal phases, the total is $<128mB^2d^{\nu+3}\le C_0d^{C_1}$.
  Source: "&<128mB^2d^{\nu+3}\le C_0d^{C_1}." (paper)
  > Each of the two outer diagonals applies a fourth-root phase and costs at most two elementary phase operations. Put \(t=\lfloor D/2\rfloor\). Since \(b^2=-i/2\), the scalar \(b^D\) is \((-i)^t2^{-t}b^{D\bmod2}\). Its phase costs at most two operations, and the possible factor \(b\) is computed as \((z-iz)/2\) in three operations. The shift by \(t\) consumes \(t\) fractional bits, so we charge it \(t\) units of denominator growth even though one tape scan performs the shift. Charging these same units to magnitude growth gives a common upper bound for both: \[ \begin{aligned} 8mB^2d^{\nu+2}+8d+t+9 &\le 8mB^2d^{\nu+2}+18d\\ &\le 26mB^2d^{\nu+2}\\ &<128mB^2d^{\nu+3}\le C_0d^{C_1}. \end{aligned} \] Here \(d\ge1\), \(mB^2\ge1\), and \(C_1\ge\nu+3\).
- S4.6.4.8: A value at depth $\ell$ lies in $2^{-(p+\ell)}\mathbb Z[i]$ with modulus at most $2^\ell$ (addition at most doubles the modulus, halving adds one denominator bit), so $p+\Delta$ fractional and $\Delta+3$ integer bits represent every intermediate coefficient exactly.
  Source: "lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most" (paper)
  > To see how this count controls numerical size, start with disk-valued coefficients in \(2^{-p}\mathbb Z[i]\). A value at depth \(\ell\) lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most \(2^\ell\). This follows by induction: addition or subtraction can at most double the maximum modulus of its operands; halving adds at most one denominator bit; and signs and multiplication by \(i\) preserve both bounds. The charge of \(t\) for the final shift is the same as \(t\) successive halvings. Thus reserving \(p+\Delta\) fractional bits and \(\Delta+3\) integer and sign bits per real component represents every intermediate coefficient exactly and prevents overflow. Shifts consume the reserved fractional zeros and discard no bits.
- S4.6.4.9: Since $\epsilon C_1<1$ and $d=\Theta(p^\epsilon)$, $\Delta=o(p)$, so the full coefficient width remains $O(p)$.
  Source: "\(\Delta=o(p)\), and the full coefficient width is \(O(p)\), as" (paper)
  > Choose \(\epsilon C_1<1\). Since \(d=\Theta(p^\epsilon)\), \(\Delta=o(p)\), and the full coefficient width is \(O(p)\), as required in the time analysis. Addition, signed shifts, copying and phase changes consequently take \(O(p)\) bit operations per coefficient.

**S4.6.5**: Proposition (simultaneous normalized layer): for $z$ in the unit disk on the grid $2^{-p}\mathbb Z[i]$ the procedure returns $Q_p(\mathcal Hz)$ in $O(Vd^{\lambda'})$ time, evaluating the whole layer exactly before one truncation, with error $<\sqrt2\,2^{-p}$.
How: Verify that the width bands make every packed child cost $O(M_{\rm child}R_{\rm g}(L^\tau+1))$ uniformly, then use that $\mathcal H$ is a contraction (rows have absolute sum one) so a single truncation adds less than $\sqrt2\,2^{-p}$.
- S4.6.5.1: Fix $\tau=\sigma=1-2^{-50}$, $\beta=\frac12$, $C_1=20$ and rational $c,\epsilon,\lambda,\lambda'$ with $\max\{\tau,\sigma\}<\lambda<1$, $\tau(1+c/\beta)<\lambda$, $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$ and $\epsilon C_1<1$ (concretely $\epsilon=2^{-75}$, $c=2^{-56}$, $\lambda=1-2^{-52}$, $\lambda'=1-2^{-54}$).
  Source: "\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad C_1=20." (paper)
  > \begin{proposition}[Simultaneous normalized butterfly layer] \label{prop:simultaneous-layer} Fix \[ \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad C_1=20. \] Let $c,\epsilon,\lambda,\lambda'$ be fixed positive rational numbers satisfying \[ \max\{\tau,\sigma\}<\lambda<1,\qquad \tau(1+c/\beta)<\lambda,\qquad \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1, \qquad \epsilon C_1<1. \] Fix positive constants $a_d\le b_d$ and $a_r\le b_r$, and fix positive constants $C_M,C_{\rm desc},C_w$ with $C_w>1$. For these fixed choices there are a cutoff $p_0$, one fixed finite-alphabet multitape procedure, and an implicit time constant with the following guarantee. The cutoff and time constant may depend on the fixed rational parameters and these constants. For every choice of positive integers $p,d,r$ with $p\ge p_0$ and \[ a_dp^\epsilon\le d\le b_dp^\epsilon,\qquad 2^
- S4.6.5.2: Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, $\Delta\le p$, so the guarded record width is $R_{\rm g}=2r(p+2\Delta+3)\le12rp$ and also $R_{\rm g}\ge2rp$.
  Source: "R_{\rm g}=2r(p+2\Delta+3)\le12rp" (paper)
  > \begin{proof} The procedure reads the current parameters and component width from $\mathcal E$. Parsing this header and forming the initial collapsed descriptors take polynomial time in $p$, already charged in the descriptor work above. The phase-frame construction reduces a group of $e$ selected bits to $s_{\rm c}$ children on $e/m$ selected bits. The row split gives each child $1/W_{\rm c}$ of the parent's logical volume. The packed selected-bit procedure supplies the binary basis changes. We verify that its cost is uniform over the displayed bands for $d,r$. Put $\Delta=\lceil C_0d^{C_1}\rceil$. Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, a common cutoff gives $\Delta\le p$. The guarded record width is then $R_{\rm g}=2r(p+2\Delta+3)\le12rp$; also $R_{\rm g}\ge2rp$. Padding at most doubles the original record count $M$, and row splitting only decreases it. Thus a packed child with $M_{\rm child}$ records has the following value $A_*$ of its rectangular width parameter: \[ \begin{split} A_* &=\lceil\log_2(2M_{\rm child}R_{\rm g})\rceil\\ &\le\lceil\log_2(4MR_{\rm g})\rceil\le C_Ap, \qquad C_A=C_M+b_r+7. \end{split} \] The last inequality uses $\log_2(2M)\le C_Mp$, $\log_2r\le b_rp/d\le b_rp$, and $\log_2p\le p$.
- S4.6.5.3: A packed child's width parameter satisfies $A_*\le\lceil\log_2(4MR_{\rm g})\rceil\le C_Ap$ with $C_A=C_M+b_r+7$.
  Source: "\le\lceil\log_2(4MR_{\rm g})\rceil\le C_Ap," (paper)
  > \begin{proof} The procedure reads the current parameters and component width from $\mathcal E$. Parsing this header and forming the initial collapsed descriptors take polynomial time in $p$, already charged in the descriptor work above. The phase-frame construction reduces a group of $e$ selected bits to $s_{\rm c}$ children on $e/m$ selected bits. The row split gives each child $1/W_{\rm c}$ of the parent's logical volume. The packed selected-bit procedure supplies the binary basis changes. We verify that its cost is uniform over the displayed bands for $d,r$. Put $\Delta=\lceil C_0d^{C_1}\rceil$. Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, a common cutoff gives $\Delta\le p$. The guarded record width is then $R_{\rm g}=2r(p+2\Delta+3)\le12rp$; also $R_{\rm g}\ge2rp$. Padding at most doubles the original record count $M$, and row splitting only decreases it. Thus a packed child with $M_{\rm child}$ records has the following value $A_*$ of its rectangular width parameter: \[ \begin{split} A_* &=\lceil\log_2(2M_{\rm child}R_{\rm g})\rceil\\ &\le\lceil\log_2(4MR_{\rm g})\rceil\le C_Ap, \qquad C_A=C_M+b_r+7. \end{split} \] The last inequality uses $\log_2(2M)\le C_Mp$, $\log_2r\le b_rp/d\le b_rp$, and $\log_2p\le p$.
- S4.6.5.4: The two additional normalized terms are $A_*^3/R_{\rm g}\le C_A^3p^2/(2r)$ and $80(f-1)2^{-K}A_*(1+A_*/R_{\rm g})\le80C_Ap^22^{-K}(1+C_A/(2r))$.
  Source: "\frac{A_*^3}{R_{\rm g}}" (paper)
  > Uniformly for large $p$, the bands give $f\le d\le p$ and \[ K\ge\tfrac12a_d^c p^{\epsilon c},\qquad r\ge2^{(a_r/b_d)p^{1-\epsilon}}. \] The first inequality follows from $K=\lfloor d^c\rfloor$ once $d^c\ge2$. In particular, $K\ge6$ and $K/\log p\to\infty$, while $r$ dominates every fixed polynomial. Substituting the common bound $A_*\le C_Ap$ into the two additional normalized terms in \eqref{eq:packed-rectangle-time} gives \[ \begin{aligned} \frac{A_*^3}{R_{\rm g}} &\le\frac{C_A^3p^2}{2r},\\ 80(f-1)2^{-K}A_*\left(1+\frac{A_*}{R_{\rm g}}\right) &\le80C_Ap^2 2^{-K}\left(1+\frac{C_A}{2r}\right). \end{aligned} \] Both bounds tend to zero uniformly over all current allowed $d,r$. Thus Lemma~\ref{lem:packed-selected-bit-rectangle} has the required $O(M_{\rm child}R_{\rm g}(L^\tau+1))$ cost for every packed call, with one common time constant. The row construction and the recurrence analysis above give total time $O(Vd^{\lambda'})$ on fixed tapes, including all padded and auxiliary streams. Equation~\eqref{eq:phase-butterfly-layer} converts the resulting exact $C$-layer to $\mathcal H$.
- S4.6.5.5: Both bounds tend to zero uniformly, since $K\ge\frac12a_d^cp^{\epsilon c}$ gives $K/\log p\to\infty$ and $r\ge2^{(a_r/b_d)p^{1-\epsilon}}$ dominates every polynomial in $p$; thus every packed call has cost $O(M_{\rm child}R_{\rm g}(L^\tau+1))$ with one constant.
  Source: "Both bounds tend to zero uniformly over all current allowed $d,r$." (paper)
  > Uniformly for large $p$, the bands give $f\le d\le p$ and \[ K\ge\tfrac12a_d^c p^{\epsilon c},\qquad r\ge2^{(a_r/b_d)p^{1-\epsilon}}. \] The first inequality follows from $K=\lfloor d^c\rfloor$ once $d^c\ge2$. In particular, $K\ge6$ and $K/\log p\to\infty$, while $r$ dominates every fixed polynomial. Substituting the common bound $A_*\le C_Ap$ into the two additional normalized terms in \eqref{eq:packed-rectangle-time} gives \[ \begin{aligned} \frac{A_*^3}{R_{\rm g}} &\le\frac{C_A^3p^2}{2r},\\ 80(f-1)2^{-K}A_*\left(1+\frac{A_*}{R_{\rm g}}\right) &\le80C_Ap^2 2^{-K}\left(1+\frac{C_A}{2r}\right). \end{aligned} \] Both bounds tend to zero uniformly over all current allowed $d,r$. Thus Lemma~\ref{lem:packed-selected-bit-rectangle} has the required $O(M_{\rm child}R_{\rm g}(L^\tau+1))$ cost for every packed call, with one common time constant. The row construction and the recurrence analysis above give total time $O(Vd^{\lambda'})$ on fixed tapes, including all padded and auxiliary streams. Equation~\eqref{eq:phase-butterfly-layer} converts the resulting exact $C$-layer to $\mathcal H$.
- S4.6.5.6: Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays; truncation toward zero cannot increase either component and changes each by less than $2^{-p}$, so the error is less than $\sqrt2\,2^{-p}$.
  Source: "absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk" (paper)
  > The guard-width calculation above bounds both denominator and magnitude growth by $\lceil C_0d^{C_1}\rceil$. Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, this is $o(p)$ uniformly over the allowed $d$, so every intermediate coefficient is represented exactly with the stated $O(p)$ width. The initial scan removes or adds only redundant leading sign bits and appends the reserved fractional zeros to put each supplied component in this guarded format. To truncate toward zero at the end, shift its absolute numerator right by the number of added fractional bits, restore its sign, and write the result in $w$ bits. These scans cost $O(V)$. Finally, every row of $\mathcal H$ has absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk arrays, and componentwise truncation preserves that disk and has error less than $\sqrt2\,2^{-p}$: truncation cannot increase the absolute value of either component, and changes each by less than $2^{-p}$. The truncated numerators have magnitude at most $2^p$, so the supplied component width can hold them. \end{proof} \section{Synthetic transforms and their tape layout} \label{sec:synthetic-layouts}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S4.6.1 (on [Phase frames and the two-point kernel C](phase-frame-kernel.md)): Phase frames in butterfly form: $C=H\mathsf SH=aI+bX$ satisfies $H_0=b\mathsf SC\mathsf S$, $C^2=X$, $C^4=I$, $C^{-1}=-iZCZ$; an edge change is $\mathcal P_M(\prod_jC_{e_j}^{\epsilon_j})\mathcal P_M^{-1}$ with $M\in\operatorname{GL}(m,\mathbb F_2)$; on a group of $e=mf$ axes this needs $s_{\rm c}$ child layers on $f$ axes, and $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$.
- S4.6.2 (on [Packed selected-bit addition](packed-selected-bit-addition.md)): Packed selected-bit addition: for $L=fK$, a binary row addition $y_{j_i}\gets y_{j_i}\oplus x_{j_i}$ ($j_i=\rho+iK$, $0\le i<f$) on chunks $x,y$ with an arbitrary third chunk $z$ restored costs $O(V(L^\tau+1))$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Phase frames and the two-point kernel C](phase-frame-kernel.md): The complex version of the network uses frames built from Hamming-weight phases i^{wt(x) mod 4}; each edge change factors into two-point kernels C = aI+bX (a=(1+i)/2, b=(1−i)/2), so a simultaneous C-layer on e=mf axes needs s smaller layers on f axes, and H₀^{⊗D} = b^D S_D C^{⊗D} S_D.
  Shown as: Fast simultaneous butterfly layer *<predicate>* Phase frames and the two-point kernel C
- [Packed selected-bit addition](packed-selected-bit-addition.md): A binary row addition y_j ← y_j ⊕ x_j on the same bit position in f address chunks at once, done with eight chunk-wide cyclic shifts whose segments cannot carry into each other except at a small explicit set of exceptional addresses, which are then repaired deterministically; it restores the third chunk's arbitrary contents.
  Shown as: Fast simultaneous butterfly layer *<predicate>* Packed selected-bit addition
- [Recursive rank saving](rank-saving-recurrence.md): Running the linear network with edge changes implemented by smaller calls on role streams of volume V/W gives a cost-per-volume recurrence F_k ≤ (s/W)F_{k−1}+O(1); because the number s of smaller calls satisfies s < Wm, this yields F_k = O(e^τ) with τ<1, a power saving in the parameter.
  Shown as: Fast simultaneous butterfly layer *<predicate>* Recursive rank saving
- [Fixed-point disk-grid arithmetic](fixed-point-truncation.md): Complex values stored as 2^{−p}(a+ib) with signed two's-complement words in the unit disk, exact Gaussian-dyadic intermediate results with guard bits, and one truncation Q_p toward zero that costs error less than √2·2^{−p} per coefficient while never increasing the norm.
  Shown as: Fast simultaneous butterfly layer *<predicate>* Fixed-point disk-grid arithmetic
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md): The ring of complex polynomials of degree < r with y^r = −1, in which multiplying by a power of y permutes the coefficients up to sign, so that powers of y serve as exact roots of unity.
  Shown as: Fast simultaneous butterfly layer *<predicate>* Polynomial ring modulo y^r + 1
- [Fast address-chunk interchange](address-chunk-interchange.md): The first tape procedure: swapping two disjoint contiguous address fields of u bits, (p,h,g,d,z) ↦ (p,d,g,h,z), in O(V u^τ) for a fixed τ<1 by building the swap from address shears executed through the bit network, with XOR combinations of intermediate data.
  Shown as: Fast simultaneous butterfly layer *<predicate>* Fast address-chunk interchange

## Pages that build on this one

- Convolution over the polynomial ring: Normalized convolution on d−1 axes of arrays with entries in C[y]/(y^r+1): two forward synthetic transforms keeping the same frequency order, pointwise polynomial products (by signed packing) divided by r, and the opposite transform, all using the fast layers and chunk swaps.
- Cost accounting and the saving κ: Dividing every cost by V = Tp = Θ(n) gives a table of seven dominant powers of p (layout moves, chunk exchanges, simultaneous butterfly rounds, CRT layout, Gaussian line maps, chirps, packed products), each at most 1−2κ with κ = 2^{−182}, giving total O(n (lg n)^{1−κ}).

## Other pages you may link to

- [The n log n conjecture for integer multiplication](integer-multiplication-conjecture.md)
- [Established n log n multiplier](established-multiplier.md)
- [Arrays, addresses and volume on tapes](tape-address-model.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Controlled cyclic shifts](controlled-shift.md)
- [Rank, subspaces and orthogonal complements](linear-algebra-basics.md)
- [Linear exchange network with restored scratch wires](linear-network.md)
- [Address shear and lower-triangular factorization](address-shear.md)
- [Frames on wire arrays](common-frame-principle.md)
- [Subspace labels from three-element subsets](subset-intersection-labels.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer product as digit convolution](radix-digit-convolution.md)
- [Coefficient (phase) twist](phase-twist.md)
- [Rounding and carry propagation](exact-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Multidimensional (tensor) transform](multidimensional-dft.md)
- [Two-point butterfly](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Convolution over the polynomial ring](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutations and their cancellation](permutation-cancellation.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Parameter choices and prime source lengths](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the saving κ](time-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "and the cost is $O(Vd^{\lambda'})$ for a" (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.

- "The procedure returns $Q_p(\mathcal H z)$ in the same array," (paper)

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

Write the body to `exegenius/tasks/0030-write-fast-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0030-write-fast-butterfly-layer.answer.json`, then run `exegenius submit 0030-write-fast-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0030-write-fast-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
