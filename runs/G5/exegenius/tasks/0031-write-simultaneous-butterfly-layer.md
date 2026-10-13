# exegenius task 0031-write-simultaneous-butterfly-layer

Project directory: `/home/user/openai-nlogn-wiki/runs/G5` (paths below are relative to it)

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

For these sources: The reader has a standard undergraduate computer science education: discrete mathematics (induction, sums, logarithms, floor and ceiling, functions and bijections, graphs and acyclic circuits), algorithms (divide and conquer, recurrences, sorting in O(n log n), grade-school multiplication and Karatsuba, Newton's method from calculus), and the basic theory of computation with Turing machines and tapes. They know complex numbers, roots of unity, polynomial arithmetic, modular arithmetic and elementary linear algebra, and have seen the FFT as an algorithm. They have not studied abstract algebra beyond modular arithmetic, number theory beyond gcd and inverses, numerical analysis of rounding errors, or any multiplication algorithm beyond the basic ones, so the wiki must explain the Fourier-transform machinery, the polynomial ring, the Harvey-van der Hoeven resampling and the linear-network constructions.

The reader already understands these concepts:

- Big-O notation
- Turing machines with tapes
- Polynomials
- Complex numbers
- Roots of unity
- Modular arithmetic
- Binary integers and XOR
- Basic linear algebra
- Fixed finite-tape Turing machine model
- Optimality conjecture for multiplication (also: n log n conjecture)
- Established n log n multiplier
- Array order and linear-time stream scans
- Controlled cyclic shifts and rational scalings
- Cyclic convolution
- Discrete Fourier transform and convolution theorem (also: Fourier transform, DFT)
- Radix-2 FFT butterflies (also: butterfly, decimation in frequency)
- Multidimensional transforms on power-of-two axes (also: tensor transform)
- Bluestein chirp identity (also: Bluestein conversion, chirp)
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring)
  - $y$ (ring variable): The formal variable of the polynomials, subject to the relation y^r = −1.
  - $r$ (record length): The number of complex coefficients in one polynomial record, a power of two.
- Phase twist to a negacyclic wrap
- Signed Kronecker packing of polynomial products
- Disk-grid fixed-point arithmetic (also: Gaussian dyadics, truncation Q_p)
- Three-element subset gadgets
- Linear bank-exchange network with restored scratch wires
- Frames and the common-frame identity
- Nested subspace labels and orthogonal residuals
- Bit network and its rational matrix interface
- Rank saving of the finite networks (also: recursive saving)
- Two-point phase kernel C
- Binary phase interface of the complex network
- Lower-triangular factorization of a matrix (also: Bruhat factorization)
- Rank-bounded matrix shear on address fields
- Recursive power-width interchange
- Fast address-chunk interchange (also: chunk swap, arbitrary-width interchange)
- Packed selected-bit addition with repair
- Logarithms, floors and ceilings (also: lg n, log base 2, ceil, floor, rounding up, powers of two)
- Mathematical induction and recurrences (also: induction, recursion, recurrence relation, divide and conquer, recursive calls, master theorem)
- Sorting and permutation of arrays (also: merge sort, sorting in O(n log n), permutation, bijection, bit-reversal permutation)
- Schoolbook multiplication and Karatsuba (also: grade-school multiplication, long multiplication, quadratic multiplication, Karatsuba algorithm, Karatsuba-Ofman, divide-and-conquer multiplication)
- Fast Fourier transform as an algorithm (also: FFT, Cooley-Tukey, fast polynomial multiplication, Schonhage-Strassen)
- Graphs, directed acyclic graphs and circuits (also: DAG, acyclic graph, network of gates, circuit, vertices and edges, wires and gates, graph)
- Calculus and Newton's method (also: Newton iteration, Newton's method, reciprocal and square root by iteration, geometric series, exponential and trigonometric functions, Euler's formula, e^{i theta})
- Vector norms and the triangle inequality (also: sup norm, maximum norm, infinity norm, triangle inequality, absolute value, error bound)
- Primes and trial division (also: prime number, primality testing, trial division, sieve of Eratosthenes, odd primes, coprime)
- Rounding, rational numbers and fixed-point numbers (also: round to nearest integer, truncation, dyadic rational, fixed point, finite precision, rounding error)
- Worst-case time analysis of deterministic algorithms (also: worst-case running time, deterministic algorithm, asymptotic through all input lengths, decision of constants and thresholds, finite lookup table)
- Sets, Cartesian products and indexed arrays (also: Cartesian product, product set, multi-index, tuple, array indexed by tuples, lexicographic order)

## This page

Concept: Simultaneous butterfly layer
Gloss: The butterfly H₀ applied at once to the same bit position of up to d address chunks of polynomial-record arrays, computed via C^{⊗D} on the phase network, at cost O(V d^{λ'}) instead of d passes.
Also called: fast butterfly layer

## This page in the argument

The step: The butterfly $H_0$ applied at once to the same bit position of $D\le d$ address chunks of polynomial-record arrays, followed by one truncation, costs $O(Vd^{\lambda\prime})$ for a fixed $\lambda\prime<1$ instead of $D$ passes.
How: Compute the equivalent tensor power of the two-point kernel with the complex phase network, by the same recursion as the address interchange, performing its binary changes of basis by packed XORs, then convert back to the normalized butterfly and truncate once
Why: Separate butterfly factors would need $D$ whole-array passes, so the layer is done through a network whose rank saving makes the cost per volume a power of $d$ below 1. (the sources say so: "factors would require $D$ whole-array passes." (paper))
Striking feature: The cost per volume grows only like $d^{\lambda\prime}$ with $\lambda\prime<1$, while $D$ separate passes would cost a factor $d$. (explain why it holds, from the method)

Its sub-steps, in order:

- On the complex network with binary labels, each edge frame change is a product of translation kernels $aI+bX_v$, one per residual basis vector, and telescoping the frames gives $C^{\otimes m}$ on every role, scratch roles included. (on [Binary phase interface of the complex network](phase-interface.md))
- Moving the residual directions of an edge into coordinate positions by a binary change of basis turns the edge into one child call per direction on the $f$ axes of one slot.
- The normalized butterfly layer is $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$, an exact Gaussian-dyadic rescaling and phase change of the layer $C^{\otimes D}$.
- XORing the selected bit of $f$ chunks of one range into another range, with a third chunk restored to its arbitrary initial value, costs $O(V(L^\tau+1))$ in the family of parameters used. (on [Packed selected-bit addition with repair](packed-selected-bit-addition.md))
- A fixed binary change of basis on $e$ axis chunks is a fixed number of packed row additions and costs $O(V((eK)^\tau+1))$.
- Splitting complete rows among the $W$ roles, after padding, makes each child call run on a stream of exactly $1/W$ of the parent volume.
- The recursion $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, stopped at $e<d^{\beta}$, unrolls to a cost per volume $O(d^{\lambda\prime})$ with $\lambda\prime<1$.
- Evaluating the whole layer exactly in Gaussian dyadics needs only $o(p)$ guard bits, so every intermediate value fits in $O(p)$ bits.
- The procedure returns $Q_p(\mathcal H z)$ in $O(Vd^{\lambda\prime})$ time with a single truncation, coefficientwise error below $\sqrt2\,2^{-p}$, and a result still in the unit disk.

It serves these steps, from the main result down:

- One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Give the multiplication algorithm and show its output is exact, then total its cost stage by stage (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- The algorithm, with digits placed on prime axes by the Chinese-remainder map, transformed by Gaussian resampling, chirp convolution and polynomial-ring convolution, multiplied pointwise, transformed back, rescaled, rounded and carry-propagated, outputs the exact $2n$-bit product.; how: Reduce the product to a cyclic convolution of digit lists and evaluate it with Fourier transforms, building from the fastest inner primitive (convolution over a polynomial ring) outward through the resampling, prime-axis and twist reductions, then bound the error so that rounding is exact (on [The multiplication algorithm](multiplication-algorithm.md))
- The normalized cyclic convolution $\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays over $\mathcal R_r$ is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda\prime}+\log(rp)])$ time.; how: Take two forward synthetic transforms, multiply pointwise in the retained order using signed packing, apply the opposite transform to that same order, and rescale by $M$ (on [Convolution from the retained transform layout](ring-convolution.md))
- A forward synthetic transform of $M$ polynomial records, with error below $\sqrt2\,\ell 2^{-p}$, costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda\prime}])$ and leaves its output in a retained layout order that the opposite transform consumes.; how: Use address interchanges to put the selected bits of all axes at a common offset in consecutive $K$-bit chunks so that each of the $\ell$ rounds is one simultaneous butterfly layer, and add the movement, exchange and layer costs (on [Transform layout for parallel butterfly rounds](transform-layout.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.1.1.2.2, S1.1.1.2.3, S1.1.1.2.5, S1.1.1.2.6, S1.1.1.2.7, S1.1.1.2.8, S1.1.1.2.9). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.1.1.2.2**: Moving the residual directions of an edge into coordinate positions by a binary change of basis turns the edge into one child call per direction on the $f$ axes of one slot.
Source: "The number of directional kernels is precisely" (paper)
> Consider an edge from label $U_-$ to label $U_+$, and choose an orthonormal basis $v_1,\ldots,v_{\rho_{\rm edge}}$ of its residual. Proposition~\ref{prop:complex-motif-interface} gives the frame change \[ \mathcal C_{U_+}\mathcal C_{U_-}^{-1} =\prod_{j=1}^{\rho_{\rm edge}}(aI+bX_{v_j})^{\epsilon_j}, \qquad \epsilon_j\in\{1,-1\}. \] Here $(X_vf)(x)=f(x+v)$, and we write $C_v=aI+bX_v$. The number of directional kernels is precisely $\rho_{\rm edge}$, including on decreasing edges. The next step puts those directions into coordinate positions without performing a general transpose.

**S1.1.1.2.3**: The normalized butterfly layer is $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$, an exact Gaussian-dyadic rescaling and phase change of the layer $C^{\otimes D}$.
Source: "H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D." (paper)
> \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.

**S1.1.1.2.5**: A fixed binary change of basis on $e$ axis chunks is a fixed number of packed row additions and costs $O(V((eK)^\tau+1))$.
Source: "An invertible matrix over $\mathbb F_2$ of fixed order $m\ge3$ is a" (paper)
> \paragraph{Application to a fixed binary change of basis.} An invertible matrix over $\mathbb F_2$ of fixed order $m\ge3$ is a product of a fixed number of elementary row additions; a row exchange is three such additions. In one invocation of the finite network on $e=mf$ axes, slot $h$ consists of $f$ consecutive $K$-bit axis chunks. It therefore has address-bit width $L=fK$, and its selected bits $x_{h,j}$ occupy positions $\rho+jK$ for $0\le j<f$. To add row $h'$ to row $h$, use slot $h'$ as $x$, slot $h$ as $y$, and any third, distinct slot as $z$ in Lemma~\ref{lem:packed-selected-bit-rectangle}. The lemma performs $x_{h,j}\leftarrow x_{h,j}\mathbin\oplus x_{h',j}$ for every $j$ in one operation and restores the third slot, whatever its initial address value.

**S1.1.1.2.6**: Splitting complete rows among the $W$ roles, after padding, makes each child call run on a stream of exactly $1/W$ of the parent volume.
Source: "\paragraph{Where the rows come from.}" (paper)
> \paragraph{Where the rows come from.} Put \[ q_0=\lceil\log_2 W\rceil\, \lceil\log_m(2d)\rceil, \qquad k_0=\lceil\log_m d\rceil. \] If \(D\le q_0\), use individual \(C\) kernels, at cost \(O(V\log d)\). Otherwise apply \(C\) individually on the selected bits of the first \(q_0\) chunks, in \(O(V\log d)\) time. These chunks remain a complete consecutive address block before all the remaining chunks; regard their concatenated bits as one row index. Its range has length \(R_{\rm row}=2^{q_0K}\ge W^{k_0}\), since \(K\ge1\) for sufficiently large \(p\) and \(q_0K\ge k_0\log_2W\). Within each preceding prefix, add the same number of zero rows to reach the next multiple of \(W^{k_0}\); the volume grows by a factor at most two. At any recursive depth \(j\le k_0\), the row count is divisible by \(W^{k_0-j}\).

**S1.1.1.2.7**: The recursion $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, stopped at $e<d^{\beta}$, unrolls to a cost per volume $O(d^{\lambda\prime})$ with $\lambda\prime<1$.
Source: "F(e)\le (s/W)F(e/m)+O((eK)^\tau+1)," (paper)
> \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).

**S1.1.1.2.8**: Evaluating the whole layer exactly in Gaussian dyadics needs only $o(p)$ guard bits, so every intermediate value fits in $O(p)$ bits.
Source: "The accelerated network is evaluated exactly until an entire" (paper)
> The accelerated network is evaluated exactly until an entire normalized butterfly layer is complete. Its intermediate operators need not be contractions. We now give explicit constants that bound denominator and magnitude growth within one layer.

**S1.1.1.2.9**: The procedure returns $Q_p(\mathcal H z)$ in $O(Vd^{\lambda\prime})$ time with a single truncation, coefficientwise error below $\sqrt2\,2^{-p}$, and a result still in the unit disk.
Source: "The procedure returns $Q_p(\mathcal H z)$ in the same array," (paper)
> The procedure returns $Q_p(\mathcal H z)$ in the same array, coefficient order, and component format in $O(Vd^{\lambda'})$ time, uniformly over all these choices of $p,d,r,D,P,S,\rho,w$ and $z$. Every returned coefficient belongs to the complex unit disk, and, in the maximum coefficient norm, \[ \|Q_p(\mathcal H z)-\mathcal H z\|_\infty <\sqrt2\,2^{-p}. \] The procedure evaluates the entire layer exactly before this final truncation. Put \[ C_0=128m\bigl(s_{\rm c}+64(W_{\rm c}+m+1)^3\bigr)^2, \] where $m,W_{\rm c},s_{\rm c}$ are the fixed constants of Proposition~\ref{prop:complex-motif-interface}. The procedure uses at most $p+\lceil C_0d^{C_1}\rceil$ fractional bits and $\lceil C_0d^{C_1}\rceil+3$ integer and sign bits per real component internally; these widths are $O(p)$. The time includes address changes, deterministic repair, row padding and its removal, and fixed-tape workspace cleanup. Its tape count is fixed, and its time constant is independent of the allowed array lengths and coefficient values. \end{proposition}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.1.1.2.1 (on [Binary phase interface of the complex network](phase-interface.md)): On the complex network with binary labels, each edge frame change is a product of translation kernels $aI+bX_v$, one per residual basis vector, and telescoping the frames gives $C^{\otimes m}$ on every role, scratch roles included.
- S1.1.1.2.4 (on [Packed selected-bit addition with repair](packed-selected-bit-addition.md)): XORing the selected bit of $f$ chunks of one range into another range, with a third chunk restored to its arbitrary initial value, costs $O(V(L^\tau+1))$ in the family of parameters used.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Binary phase interface of the complex network](phase-interface.md): With Gaussian-dyadic scalars and binary labels, each edge's frame change is a product of translation kernels aI + bX_v, one per residual basis vector, and telescoping the frames yields C^{⊗m} on every role.
  Shown as: Simultaneous butterfly layer *<predicate>* Binary phase interface of the complex network
- [Packed selected-bit addition with repair](packed-selected-bit-addition.md): XORing one selected bit position of f chunks into another chunk is done by a few cyclic shifts of whole chunk ranges, followed by a deterministic repair of the small set of addresses where guard values fail.
  Shown as: Simultaneous butterfly layer *<predicate>* Packed selected-bit addition with repair
- [Disk-grid fixed-point arithmetic](fixed-point-disk.md): Complex values in the unit disk stored as 2^{-p} times Gaussian-integer numerators in two's complement; layers are computed exactly in Gaussian dyadics with guard bits and then truncated toward zero by Q_p.
  Shown as: Simultaneous butterfly layer *<predicate>* Disk-grid fixed-point arithmetic
- [Two-point phase kernel C](two-point-kernel.md): The 2×2 kernel C = H S H = aI + bX with a = (1+i)/2, b = (1−i)/2, satisfying C² = X and C⁴ = I and related to the butterfly by H₀ = b S C S.
  Shown as: Simultaneous butterfly layer *<predicate>* Two-point phase kernel C
- [Rank saving of the finite networks](rank-saving.md): The sum s of edge ranks is strictly less than the wire count W times the dimension m, so a recursive call on width m·f uses s calls on volume V/W each and the cost per volume grows by s/W < m, which gives the power saving.
  Shown as: Simultaneous butterfly layer *<predicate>* Rank saving of the finite networks
- [Polynomial ring modulo yʳ + 1](polynomial-ring.md): Complex polynomials of degree below r with y^r = −1, so that multiplying by a power of y is a signed shift of the coefficient list; powers of y serve as roots of unity.
  Shown as: Simultaneous butterfly layer *<predicate>* Polynomial ring modulo yʳ + 1

## Pages that build on this one

- Transform layout for parallel butterfly rounds: A positional address permutation moves the selected bits of all axes into common-offset consecutive K-bit chunks so each transform round is one simultaneous butterfly layer; it costs O(Tp[dK + pK^{τ−1} + ℓ d^{λ'}]).
- Complete time bound and the power saving: Dividing costs by Tp, the seven dominant terms (layout moves, chunk exchanges, butterfly rounds, CRT layouts, Gaussian line maps, chirps, packed products) have exponents at most 1 − 2κ of p, giving O(n (log n)^{1−κ}).

## Other pages you may link to

- [Optimality conjecture for multiplication](nlogn-conjecture.md)
- [Cyclic convolution](convolution.md)
- [Three-element subset gadgets](subset-gadgets.md)
- [Fixed finite-tape Turing machine model](fixed-tape-model.md)
- [Established n log n multiplier](nlogn-multiplier.md)
- [Array order and linear-time stream scans](stream-scans.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Linear bank-exchange network with restored scratch wires](bank-exchange-network.md)
- [Frames and the common-frame identity](frames.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Bit network and its rational matrix interface](bit-network-interface.md)
- [Lower-triangular factorization of a matrix](matrix-factorization.md)
- [Rank-bounded matrix shear on address fields](matrix-shear.md)
- [Recursive power-width interchange](power-width-interchange.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Phase twist to a negacyclic wrap](coefficient-twist.md)
- [Signed Kronecker packing of polynomial products](signed-packing.md)
- [Discrete Fourier transform and convolution theorem](dft.md)
- [Radix-2 FFT butterflies](fft-butterfly.md)
- [Multidimensional transforms on power-of-two axes](multidimensional-transform.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Retained frequency order of the transforms](stored-frequency-order.md)
- [Transform layout for parallel butterfly rounds](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling with retained permutations](retained-permutations.md)
- [Reducing integer multiplication to digit convolution](radix-digit-reduction.md)
- [Error analysis and exact recovery of the product](precision-recovery.md)
- [Chinese-remainder map onto distinct prime axes](crt-prime-axes.md)
- [Parameter regime for input length n](parameter-regime.md)
- [Prime source lengths near powers of two](prime-lengths.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound and the power saving](time-bound.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "simultaneously on selected coordinate bits of the numerical arrays" (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.

- "the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$." (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.

- "H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D" (paper)

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

Write the body to `exegenius/tasks/0031-write-simultaneous-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0031-write-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0031-write-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0031-write-simultaneous-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
