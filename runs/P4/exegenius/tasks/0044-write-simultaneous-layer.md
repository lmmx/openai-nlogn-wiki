# exegenius task 0044-write-simultaneous-layer

Project directory: `/home/user/openai-nlogn-wiki/runs/P4` (paths below are relative to it)

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

For these sources: The reader has finished a standard undergraduate computer science degree: discrete mathematics (induction, counting, modular arithmetic, primes, gcd, permutations, basic graphs), algorithms (asymptotic notation, divide and conquer, recurrences, sorting including radix sort, the idea of the FFT and Karatsuba multiplication at survey level), calculus and basic real analysis (limits, logarithms, exponentials, floors and ceilings, inequalities), introductory linear algebra and probability, and the basics of Turing machines and complexity. They have not studied abstract algebra beyond arithmetic mod n, coding theory, or number-theoretic transforms in depth, and have not met the multitape fast-multiplication literature (Schönhage–Strassen, Fürer, Harvey–van der Hoeven), Gaussian resampling, or Nussbaumer polynomial transforms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape Turing machine model
- The n log n optimality conjecture
- Established near-linear integer multiplier
- Matrices, rank, subspaces and projections
- Tensor products of vectors, spaces and operators
- Binary vectors, XOR and Hamming weight
- Nondegenerate bilinear forms and orthogonal complements
- Discrete Fourier transform
- Multidimensional transform and cyclic convolution on a product of axes
- Butterfly step and decimation-in-frequency recursion
- Max-modulus norm, contractions and error propagation
- Disk grid and truncation
  - $p$ (precision bits): the number of fractional bits kept in each real or imaginary part
  - $\mathbb D_p$ (p-bit disk grid): the set of complex numbers 2^{-p}(a+ib) with integers a,b lying in the closed unit disk
  - $Q_p$ (truncation operator): the map that truncates the real and imaginary parts of each coefficient toward zero to multiples of 2^{-p}
- Streaming fixed-point and Gaussian dyadic arithmetic
- Arrays, address fields, rows and logical volume
- Linear-time stream operations
- Controlled cyclic shifts and rational scalings
- Depth-first recursion schedule on fixed tapes
- Triple-intersection pairing formulas
- Linear network exchanging two banks with restored scratch
- Frames and the common-frame identity
- Nested subspace labels and the rank deficit
- Address shear
- Bit network and rational shear interface
- Phase kernel C = aI + bX
  - $C$ (phase kernel): the two-by-two matrix H S H acting on one selected bit
  - $a$ (kernel coefficient a): the complex number (1+i)/2 multiplying the identity
  - $b$ (kernel coefficient b): the complex number (1−i)/2 multiplying the bit flip
  - $I$ (identity matrix): the two-by-two identity matrix
  - $X$ (bit-flip matrix): the two-by-two matrix interchanging the two coordinates
- Complex phase network interface
- Lower-triangular factorization of a matrix
- Cost of a rational matrix shear
- Strict rank deficit gives a power saving
- Rows distributed cyclically among wire roles
- Power-width interchange with rows
- Fast address-chunk interchange
- Carry-free packed controlled rotations
- Deterministic repair of exceptional addresses
- Packed selected-bit addition on one rectangle
- Guard width for exact intermediate values
- Recursive phase-frame layer on slots
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): the indeterminate of the polynomial ring, satisfying y^r = −1
  - $r$ (polynomial length): the number of complex coefficients in a record, a power of two
- Synthetic root of unity ω_t = y^{2r/t}
  - $\omega_t$ (synthetic root): the element y^{2r/t} acting as a primitive t-th root of unity in the ring
  - $t$ (transform length): the length of the axis, a power of two dividing 2r
  - $y$ (ring variable): the indeterminate of the polynomial ring, satisfying y^r = −1
  - $r$ (polynomial length): the number of complex coefficients in a record, a power of two
- Synthetic polynomial transform
- Retained stored frequency order
- Asymptotic notation beyond big-O (also: Theta, Omega, little-o, Θ, Ω, o(1), liminf, eventual lower bound)
- Logarithms, exponentials, floors and ceilings (also: log base 2, lg n, floor, ceiling, change of base, iterated logarithm)
- Binary and radix-b representation of integers (also: positional notation, base-b digits, mixed radix, bit length, val(x))
- Schoolbook multiplication and Karatsuba (also: grade-school multiplication, long multiplication, quadratic multiplication, Karatsuba-Ofman, Toom-Cook)
- Divisibility, primes and gcd (also: coprime, relatively prime, greatest common divisor, Euclidean algorithm, trial division, prime number)
- Modular arithmetic and residue classes (also: integers mod n, Z/nZ, congruence, mod Q, remainder, division with remainder, residue ring)
- Roots of unity (also: primitive root of unity, n-th roots of unity, e^{2πi/n}, twiddle factors)
- Recurrences and geometric series (also: divide-and-conquer recurrence, master theorem, solving recurrences, geometric sum, T(n) = aT(n/b) + f(n))
- Induction and elementary proof technique (also: proof by induction, structural induction, contradiction, pigeonhole principle)
- Elementary counting and the union bound (also: binomial coefficients, counting subsets, inclusion–exclusion, union bound, fraction of a finite set, Boole's inequality)
- Sorting and radix sort (also: stable sort, radix sort, counting sort, sorting by key, bucket sort)
- Permutations and bijections (also: index permutation, bit reversal, inverse permutation, permutation matrix, one-to-one correspondence)
- Sets, products of ranges and lexicographic order (also: Cartesian product, index set [n], multi-index, lexicographic order, row-major order)
- Matrix transposition and row-major storage (also: transpose, k×k binary matrix, row-major matrix)
- Triangle inequality and error bounds (also: absolute error, rounding error, approximation error, supremum, modulus inequality, rounding to nearest integer)
- Boolean and arithmetic circuits as networks (also: logic gates, XOR gate, circuit, wires and gates, directed acyclic graph, fan-in and fan-out)
- Graphs, paths and neighbors (also: directed graph, edges and vertices, adjacent vertices, route in a graph)
- Stacks and recursion (also: call stack, LIFO, push and pop, depth-first traversal, recursive procedure)
- Fast Fourier transform and Karatsuba as survey knowledge (also: FFT multiplication, Schönhage–Strassen, polynomial multiplication via evaluation, evaluation and interpolation)
- Real and imaginary parts, rounding and truncation (also: Re and Im, truncate toward zero, nearest integer, fixed-point numbers)
- Dot product, vectors over the rationals and orthonormal bases (also: inner product, orthogonal vectors, standard basis, Gram–Schmidt, bilinear pairing)

## This page

Concept: Simultaneous normalized butterfly layer
Gloss: H₀ is applied at once to the same bit offset of D ≤ d address chunks of every polynomial record in O(V d^{λ'}) time with λ'<1, via H₀^{⊗D} = b^D S_D C^{⊗D} S_D, the recursive phase-frame layer on rows split among wire roles, exact evaluation and one final truncation.

## This page in the argument

The step: The normalized butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ can be applied at once to the same bit offset of $D\le d$ address chunks of every polynomial record in $O(Vd^{\lambda'})$ time with $\lambda'<1$, exactly up to one final truncation.
How: Write $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, compute $C^{\otimes D}$ by the recursive phase-frame layer on rows split among the wire roles, evaluate everything exactly with guard bits and truncate once at the end.
Why: Applying the $D$ butterfly factors one after another would need $D$ whole-array passes, whereas one pass through the recursive layer costs only a power of $D$. (the sources say so: "factors would require $D$ whole-array passes." (paper))

Its sub-steps, in order:

- To apply $C^{\otimes e}$ on $e=mf$ selected bits, group them into $m$ slots of $f$ chunks, change the binary basis by packed row additions, apply the $f$-fold forward child on each of the $s_{\rm c}$ residual-basis slots, and change back; inverse children cost no extra call because $C^{-1}=-iZCZ$. (on [Recursive phase-frame layer on slots](phase-frame-layer.md))
- At an internal node with $e=m^k$ chunks the basis changes, scalar gates and reassembly cost $O(V((eK)^\tau+1))$, with $s$ child calls on streams of volume $V/W$.
- The rows come from the first $q_0$ chunks, padded to a multiple of $W^{k_0}$; a row index $u=Wg+w$ sends the whole row to role $w$.
- With exponents $\tau,\sigma,\lambda$ chosen so that $a=s/W<m^\lambda$, the recurrence $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ sums to $O(e^\lambda)$.
- Splitting $D-q_0$ in base $m$ and adding the piece costs and the row preprocessing gives $O(d^{\lambda'})$ per unit volume.
- The whole recursive $C$-layer is evaluated exactly with $p+\Delta$ fractional bits and $\Delta+3$ integer bits, where $\Delta=\lceil C_0d^{C_1}\rceil$ bounds the arithmetic depth through $A(e)\le sA(e/m)+E$; since $\epsilon C_1<1$, $\Delta=o(p)$ and all widths stay $O(p)$. (on [Guard width for exact intermediate values](guard-width.md))
- The phase-frame construction reduces a group of $e$ selected bits to $s_{\rm c}$ children on $e/m$ bits, each with a $1/W_{\rm c}$ share of the volume, and the packed procedure supplies the basis changes with a common time constant.
- Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays and the single truncation has error below $\sqrt2\,2^{-p}$.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce multiplication to convolution over $\mathbb C[y]/(y^r+1)$ through radix digits, Chinese-remainder axes, Gaussian resampling and chirps, speed up the data movement and the butterfly arithmetic with two network-based tape procedures with a strict rank saving, recover the exact product by rounding and carries, and add up the costs. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Two tape procedures exist for fixed exponents $\tau,\lambda'<1$: one interchanges two disjoint address chunks of $u$ bits in $O(Vu^\tau)$ time, and one applies a normalized butterfly layer on up to $d$ address chunks in $O(Vd^{\lambda'})$ time, where $V$ is the logical bit volume.; how: Obtain both from one fixed linear network that exchanges two banks of values and restores every auxiliary value, whose edge frame changes are smaller calls of the same procedure; the strict inequality $s<Wm$ on their number gives a recursion with a power saving.

## Steps this page derives

The argument gives this page these sub-steps of its step (L2.1, L2.2, L2.3, L2.4, L4.1, L4.2). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**L2.1**: At an internal node with $e=m^k$ chunks the basis changes, scalar gates and reassembly cost $O(V((eK)^\tau+1))$, with $s$ child calls on streams of volume $V/W$.
Source: "First consider an internal node containing \(e=m^k\) consecutive" (paper)
> First consider an internal node containing \(e=m^k\) consecutive active chunks, with \(k\ge1\). Split it into \(m\) consecutive slots, each containing \(e/m\) chunks. The phase construction supplies one recursive call on a slot for each vector in an edge residual basis, hence exactly \(s\) calls in one invocation of the network. If the logical volume entering this node is \(V\), binary changes of basis, their inverses, scalar gates, endpoint corrections and reassembly of the physical banks cost \[ O\bigl(V((eK)^\tau+1)\bigr) \] at this node. Each slot has \((e/m)K\) address bits, so Lemma~\ref{lem:packed-selected-bit-rectangle} gives the stated bound for a row addition. The network and all of its \(m\)-dimensional residual bases are fixed, so the total number of row additions is fixed as well. At the same guarded width, the scalar gates cost a constant number of scans of the current volume. Address and descriptor work bounded by any fixed polynomial in \(p\) per record is also absorbed: its ratio to the record's \(\Theta(rp)\) bits tends to zero.

**L2.2**: The rows come from the first $q_0$ chunks, padded to a multiple of $W^{k_0}$; a row index $u=Wg+w$ sends the whole row to role $w$.
Source: "At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\)," (paper)
> At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\), and send that entire row to physical wire role \(w\), indexed there by \(g\). Every role stream has the same remaining address shape. Thus a pointwise gate reads the records with the same \(g\) and the same remaining address in its touched roles. The scalar network allows these role values to be arbitrary, so the split supplies its scratch roles from existing rows. Each recursive edge call acts on one role stream with volume exactly \(1/W\) of its parent's logical volume.

**L2.3**: With exponents $\tau,\sigma,\lambda$ chosen so that $a=s/W<m^\lambda$, the recurrence $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ sums to $O(e^\lambda)$.
Source: "Fix \(\beta=1/2\), and choose real exponents satisfying" (paper)
> \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).

**L2.4**: Splitting $D-q_0$ in base $m$ and adding the piece costs and the row preprocessing gives $O(d^{\lambda'})$ per unit volume.
Source: "Adding their costs and the row preprocessing gives" (paper)
> Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\). Partition the remaining chunks into \(a_j\) consecutive pieces containing \(m^j\) chunks for each \(j\). There are at most \((m-1)(1+\lfloor\log_m d\rfloor)\) pieces. Adding their costs and the row preprocessing gives \[ O\!\left(\log(2d) \bigl[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1\bigr]\right) =O(d^{\lambda'}) \] for any fixed \[ \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1. \] The case \(D\le q_0\), in which preprocessing would consume all active chunks, was handled by individual kernels. Thus all constants and all tape counts are independent of \(p,d,r\) and the input data.

**L4.1**: The phase-frame construction reduces a group of $e$ selected bits to $s_{\rm c}$ children on $e/m$ bits, each with a $1/W_{\rm c}$ share of the volume, and the packed procedure supplies the basis changes with a common time constant.
Source: "The phase-frame construction reduces a group of $e$ selected bits to" (paper)
> \begin{proof} The procedure reads the current parameters and component width from $\mathcal E$. Parsing this header and forming the initial collapsed descriptors take polynomial time in $p$, already charged in the descriptor work above. The phase-frame construction reduces a group of $e$ selected bits to $s_{\rm c}$ children on $e/m$ selected bits. The row split gives each child $1/W_{\rm c}$ of the parent's logical volume. The packed selected-bit procedure supplies the binary basis changes. We verify that its cost is uniform over the displayed bands for $d,r$. Put $\Delta=\lceil C_0d^{C_1}\rceil$. Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, a common cutoff gives $\Delta\le p$. The guarded record width is then $R_{\rm g}=2r(p+2\Delta+3)\le12rp$; also $R_{\rm g}\ge2rp$. Padding at most doubles the original record count $M$, and row splitting only decreases it. Thus a packed child with $M_{\rm child}$ records has the following value $A_*$ of its rectangular width parameter: \[ \begin{split} A_* &=\lceil\log_2(2M_{\rm child}R_{\rm g})\rceil\\ &\le\lceil\log_2(4MR_{\rm g})\rceil\le C_Ap, \qquad C_A=C_M+b_r+7. \end{split} \] The last inequality uses $\log_2(2M)\le C_Mp$, $\log_2r\le b_rp/d\le b_rp$, and $\log_2p\le p$.

**L4.2**: Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays and the single truncation has error below $\sqrt2\,2^{-p}$.
Source: "Finally, every row of $\mathcal H$ has" (paper)
> The guard-width calculation above bounds both denominator and magnitude growth by $\lceil C_0d^{C_1}\rceil$. Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, this is $o(p)$ uniformly over the allowed $d$, so every intermediate coefficient is represented exactly with the stated $O(p)$ width. The initial scan removes or adds only redundant leading sign bits and appends the reserved fractional zeros to put each supplied component in this guarded format. To truncate toward zero at the end, shift its absolute numerator right by the number of added fractional bits, restore its sign, and write the result in $w$ bits. These scans cost $O(V)$. Finally, every row of $\mathcal H$ has absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk arrays, and componentwise truncation preserves that disk and has error less than $\sqrt2\,2^{-p}$: truncation cannot increase the absolute value of either component, and changes each by less than $2^{-p}$. The truncated numerators have magnitude at most $2^p$, so the supplied component width can hold them. \end{proof} \section{Synthetic transforms and their tape layout} \label{sec:synthetic-layouts}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- L1 (on [Recursive phase-frame layer on slots](phase-frame-layer.md)): To apply $C^{\otimes e}$ on $e=mf$ selected bits, group them into $m$ slots of $f$ chunks, change the binary basis by packed row additions, apply the $f$-fold forward child on each of the $s_{\rm c}$ residual-basis slots, and change back; inverse children cost no extra call because $C^{-1}=-iZCZ$.
- L3 (on [Guard width for exact intermediate values](guard-width.md)): The whole recursive $C$-layer is evaluated exactly with $p+\Delta$ fractional bits and $\Delta+3$ integer bits, where $\Delta=\lceil C_0d^{C_1}\rceil$ bounds the arithmetic depth through $A(e)\le sA(e/m)+E$; since $\epsilon C_1<1$, $\Delta=o(p)$ and all widths stay $O(p)$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Recursive phase-frame layer on slots](phase-frame-layer.md): To apply C^{⊗e} on e = m·f selected bits, group the bits into m slots of f chunks, change binary basis by packed row additions, apply the f-fold inverse or forward child on each residual-basis slot (s_c children in total), and change back; inverses cost no extra child since C⁻¹ = −iZCZ.
  Shown as: Simultaneous normalized butterfly layer *<predicate>* Recursive phase-frame layer on slots
- [Rows distributed cyclically among wire roles](row-splitting-roles.md): To run the network on an array, whole rows are dealt cyclically into W role streams (padding the row count to a multiple of W per prefix), each of volume V/W with identical remaining shape, and gates act pointwise on matching addresses.
  Shown as: Simultaneous normalized butterfly layer *<predicate>* Rows distributed cyclically among wire roles
- [Guard width for exact intermediate values](guard-width.md): The whole recursive C-layer is evaluated exactly with p + Δ fractional bits and Δ + 3 integer bits, where Δ = ⌈C₀ d^{C₁}⌉ bounds the arithmetic depth via A(e) ≤ sA(e/m)+E; since ε·C₁<1, Δ = o(p) and widths stay O(p).
  Shown as: Simultaneous normalized butterfly layer *<predicate>* Guard width for exact intermediate values
- [Strict rank deficit gives a power saving](rank-deficit-recurrence.md): If a call at parameter m·f makes s calls at parameter f, each on a stream of volume V/W, then normalized cost obeys F_k ≤ (s/W)F_{k−1}+O(1); since s/W < m^τ with τ<1 the solution is O(e^τ), a power-of-the-width saving.
  Shown as: Simultaneous normalized butterfly layer *<predicate>* Strict rank deficit gives a power saving
- [Depth-first recursion schedule on fixed tapes](fixed-tape-dfs-schedule.md): Recursive calls on W role streams are run on one fixed set of tapes by parking the inactive streams on a stack, copying the active stream to the child, and restoring afterwards, costing O(V) per node.
  Shown as: Simultaneous normalized butterfly layer *<predicate>* Depth-first recursion schedule on fixed tapes
- [Disk grid and truncation](disk-grid-truncation.md): Fixed-point complex numbers with p fractional bits inside the unit disk, and the operator that truncates real and imaginary parts toward zero to that grid, never increasing norm and causing error below √2·2^{−p}.
  Shown as: Simultaneous normalized butterfly layer *<predicate>* Disk grid and truncation
- [Polynomial ring modulo y^r + 1](polynomial-ring-negacyclic.md): Polynomials with complex coefficients of degree below r, with y^r = −1; multiplying by a power y^a is an exact signed cyclic shift of the coefficient list (an isometry), and the wrap-around carries a minus sign (negacyclic).
  Shown as: Simultaneous normalized butterfly layer *<predicate>* Polynomial ring modulo y^r + 1
- [Butterfly step and decimation-in-frequency recursion](fft-butterfly.md): The two-point step H₀(u,v) = ((u+v)/2,(u−v)/2) paired with a twiddle multiplication; applying it recursively on halves computes a length-2^a transform in a levels.
  Shown as: Simultaneous normalized butterfly layer *<predicate>* Butterfly step and decimation-in-frequency recursion

## Pages that build on this one

- Transform layout and cost: A positional permutation L moves chosen bit slots to a prefix and groups the remaining bits into K-bit chunks so each transform round is a simultaneous butterfly layer; cost O(Tp[dK + pK^{τ−1} + ℓ d^{λ'}]) with error below √2·ℓ·2^{−p}.
- Size parameters of the algorithm: From the input length n: b = ⌈log₂ n⌉, working precision p = 6b, number of axes d = ⌊b^ε⌋, chunk width K = ⌊d^c⌋, padded box size T ≈ n/b, axis lengths r or r/2, resampling parameter α, with fixed tiny rationals ε, c, τ, λ', δ.
- Cost analysis and the exponent κ: Dividing all costs by Tp = Θ(n) gives a table of seven dominant terms whose powers of p are all at most 1 − 2κ for κ = 2^{−182}, so the total is O(n (lg n)^{1−κ}) with schoolbook multiplication for small inputs.

## Other pages you may link to

- [Fixed-tape Turing machine model](multitape-model.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Streaming fixed-point and Gaussian dyadic arithmetic](fixed-point-arithmetic.md)
- [Established near-linear integer multiplier](established-multiplier.md)
- [Arrays, address fields, rows and logical volume](address-fields-volume.md)
- [Linear-time stream operations](stream-ops.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Matrices, rank, subspaces and projections](linear-algebra-basics.md)
- [Tensor products of vectors, spaces and operators](tensor-products.md)
- [Address shear](address-shear.md)
- [Binary vectors, XOR and Hamming weight](f2-vectors.md)
- [Nondegenerate bilinear forms and orthogonal complements](bilinear-orthogonality.md)
- [Triple-intersection pairing formulas](subset-pairing-formulas.md)
- [Linear network exchanging two banks with restored scratch](scalar-exchange-network.md)
- [Frames and the common-frame identity](network-frames.md)
- [Nested subspace labels and the rank deficit](subspace-labels-rank-saving.md)
- [Bit network and rational shear interface](bit-network-interface.md)
- [Lower-triangular factorization of a matrix](lower-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Power-width interchange with rows](power-width-interchange.md)
- [Fast address-chunk interchange](chunk-swap.md)
- [Carry-free packed controlled rotations](packed-rotations.md)
- [Deterministic repair of exceptional addresses](exceptional-address-repair.md)
- [Packed selected-bit addition on one rectangle](packed-selected-bit-addition.md)
- [Discrete Fourier transform](dft.md)
- [Synthetic root of unity ω_t = y^{2r/t}](synthetic-roots.md)
- [Phase kernel C = aI + bX](phase-kernel.md)
- [Complex phase network interface](complex-network-interface.md)
- [Multidimensional transform and cyclic convolution on a product of axes](multidim-dft.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Retained stored frequency order](frequency-order.md)
- [Max-modulus norm, contractions and error propagation](contraction-error-budget.md)
- [Transform layout and cost](transform-layout.md)
- [Signed Kronecker packing for ring products](signed-packing.md)
- [Gaussian resampling with retained permutations](gaussian-resampling.md)
- [Tensor interface for resampling](tensor-resampling.md)
- [Cyclic convolution and the convolution theorem](cyclic-convolution.md)
- [Integer multiplication as convolution of radix digits](multiplication-as-convolution.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Cancellation of the source permutation](source-permutation-cancel.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Size parameters of the algorithm](parameter-choice.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Distinct prime source lengths near powers of two](prime-lengths.md)
- [Coefficient twist from cyclic to negacyclic](coefficient-twist.md)
- [Middle transform computed by chirp and complex convolution](chirp-transform.md)
- [Source transform procedure](source-transform.md)
- [Exact recovery by rounding and carry propagation](exact-recovery.md)
- [The complete multiplication algorithm](multiplication-algorithm.md)
- [Cost analysis and the exponent κ](cost-analysis.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Simultaneous normalized butterfly layer" (paper)

  > \begin{proposition}[Simultaneous normalized butterfly layer] \label{prop:simultaneous-layer} Fix \[ \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad C_1=20. \] Let $c,\epsilon,\lambda,\lambda'$ be fixed positive rational numbers satisfying \[ \max\{\tau,\sigma\}<\lambda<1,\qquad \tau(1+c/\beta)<\lambda,\qquad \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1, \qquad \epsilon C_1<1. \] Fix positive constants $a_d\le b_d$ and $a_r\le b_r$, and fix positive constants $C_M,C_{\rm desc},C_w$ with $C_w>1$. For these fixed choices there are a cutoff $p_0$, one fixed finite-alphabet multitape procedure, and an implicit time constant with the following guarantee. The cutoff and time constant may depend on the fixed rational parameters and these constants. For every choice of positi

- "H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D." (paper)

  > \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.


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

Write the body to `exegenius/tasks/0044-write-simultaneous-layer.answer.md` and the JSON to `exegenius/tasks/0044-write-simultaneous-layer.answer.json`, then run `exegenius submit 0044-write-simultaneous-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0044-write-simultaneous-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
