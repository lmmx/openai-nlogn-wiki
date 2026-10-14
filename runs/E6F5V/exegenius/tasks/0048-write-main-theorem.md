# exegenius task 0048-write-main-theorem

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F5V` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, counting, induction, primes, gcd), a first algorithms course (divide and conquer, recurrences, sorting, Karatsuba multiplication, schoolbook arithmetic) and complexity (big-O family, single- and multitape Turing machines), together with calculus (exponentials, logarithms, series), linear algebra over the reals and complex numbers, and polynomials. They have not met Fourier transforms or the FFT in depth, finite fields beyond arithmetic mod 2, bilinear forms over arbitrary fields, number-theoretic estimates such as prime density, or any research-level multiplication algorithm; those are what the wiki must explain.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Binary integers
- Modular arithmetic
- Matrices, rank and linear maps
- Fixed-tape Turing machine model
- Arrays, address fields and logical volume
- Elementary stream operations
- Controlled cyclic shifts and rational scalings
- Cyclic convolution
- Normalized discrete Fourier transform
- Multidimensional transforms and convolution on several axes
- Fixed-point complex arithmetic and truncation error
- Integer multiplication as digit convolution
- Established O(n log n) integer multiplier
- The n log n optimality conjecture
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal variable of the polynomials, which satisfies y^r = −1 in the quotient.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Signed packing (Kronecker substitution)
- Phase twist from cyclic to negacyclic
- Synthetic polynomial transform
- Decimation-in-frequency butterflies and bit-reversed frequency order
- Chinese-remainder map to prime cyclic axes
- Bluestein chirp identity
- Cancellation of the retained source permutation
- Gaussian resampling
- Tensor resampling on a padded box
- Choosing prime source lengths
- Size parameters of the multiplication
- Role networks and frames
- Restoring arbitrary scratch values
- Three-subset gather and scatter network
- Nondegenerate subspaces and orthogonal residuals
- Subspace labels and the rank budget
- Rank saving and the power-saving recurrence
- Lower-triangular factorization of a matrix
- Cost of a rational matrix shear
- Bit network as an address shear
- Power-width address interchange
- Fast interchange of address chunks
- Two-point butterfly H₀ and the kernel C
- Binary phase frames
- Packed selected-bit addition
- Simultaneous butterfly layer
- Transform layout and cost
- Convolution from the retained transform layout
- Source Fourier transform procedure
- The multiplication algorithm
- Precision and exact recovery
- Cost table and the saving exponent κ
- Big-Theta, big-Omega and little-o notation (also: Theta, Omega, Θ, Ω, little-o, o(1), asymptotic notation)
- Divide-and-conquer recurrences (also: recurrence relation, master theorem, recursion tree, solving recurrences)
- Schoolbook and Karatsuba multiplication (also: long multiplication, Karatsuba, Toom-Cook, grade-school multiplication)
- Positional notation in any radix and mixed radix (also: radix-q digits, base-q representation, mixed-radix expansion, digit string, most significant digit)
- Bitwise operations, XOR and Hamming weight (also: XOR, exclusive or, addition mod 2, bit parity, wt, popcount, Hamming weight)
- Floor, ceiling and rounding (also: ⌊x⌋, ⌈x⌉, round to nearest integer, integer part)
- Exponential and logarithm functions (also: log base 2, lg, natural logarithm, ln, exp, e^x, Gaussian function)
- Convergent series and the geometric series (also: absolutely convergent sum, infinite sum, geometric series, tail bound, series convergence)
- Prime numbers, coprimality and trial division (also: relatively prime, pairwise coprime, gcd, odd prime, primality by trial division, unique factorization)
- Extended Euclidean algorithm (also: Euclid's algorithm, Bezout identity, computing modular inverses)
- Counting subsets and binomial coefficients (also: n choose k, binomial coefficient, k-subsets, inclusion-exclusion, ground set)
- Permutations and permutation matrices (also: bijection of indices, reordering of coordinates, involution, permutation of positions, partial permutation)
- Lexicographic order and Cartesian products of index sets (also: lexicographic order, product of ranges, multi-index, tuple addressing, row-major order)
- Vector norms, inner products and orthogonality (also: maximum norm, sup norm, infinity norm, triangle inequality, dot product, orthonormal basis, orthogonal complement, isometry)
- Gaussian elimination (also: row reduction, row operations, elementary matrices, echelon form)
- Dyadic rationals and binary fractions (also: dyadic numbers, numbers m/2^k, binary point, fixed-point numbers, Gaussian dyadics, Gaussian integers)
- Stable radix sort and counting sort (also: bit sorting, stable sorting, radix sorting, sorting by a key digit)
- Mathematical induction (also: induction on k, proof by induction, recursive construction)

## This page

Concept: Integer multiplication below n log n
Gloss: A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{-182}, using fast address interchange and fast simultaneous butterfly layers inside a Gaussian-resampling, chirp and synthetic-transform reduction.
Heading: Integer multiplication below $n\log n$

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits in each of the two integers being multiplied.

## This page in the argument

The step: A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, using fast address interchange and fast simultaneous butterfly layers inside a Gaussian-resampling, chirp and synthetic-transform reduction.
How: Reduce the product to a convolution evaluated through Gaussian-resampled, chirped synthetic transforms, make the two costly tape operations (address movement and butterfly layers) cheaper by a power of the logarithm using networks with a rank saving, and then assemble the algorithm and add up its costs.
Why: Scanning $\Theta(n)$ bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$, so beating $n\log n$ requires cheaper address movement and cheaper arithmetic. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))

Its sub-steps, in order:

- If a network of $W$ wires has total edge rank $s<Wm$, a call at parameter $e=mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$, so the cost per unit volume obeys $F_k\le(s/W)F_{k-1}+O(1)$ and grows only like $e^{\tau}$ with $\tau<1$. (on [Rank saving and the power-saving recurrence](rank-saving-recurrence.md))
- Moving a digit, splitting a stream on a digit, cyclically splitting rows among $W$ streams and merging them, and cyclically shifting or rescaling a later field by control fields all take $O(V)$ steps on a fixed number of tapes.
- There are two fixed linear networks, a bit network over $\mathbb F_2$ and a complex network over $\mathbb Z[i,1/2]$, that exchange two banks of values with prescribed signs, restore every scratch wire, and have total edge rank $s<Wm$.
- Two disjoint address chunks of $u$ bits in an array with complete Cartesian address set can be exchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$, although the intermediate steps form XOR combinations of the data. (on [Fast interchange of address chunks](chunk-interchange.md))
- One $H_0$ butterfly applied at the same bit offset in $D\le d$ address chunks at once is computed exactly, with a single final truncation, in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$. (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md))
- A positional permutation moves selected bits of the $d-1$ axes to a common offset in $K$-bit chunks so that each transform round is one simultaneous layer, giving a forward and an opposite synthetic transform each costing $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$. (on [Transform layout and cost](transform-layout.md))
- Normalized convolution over the negacyclic ring is computed by two forward synthetic transforms, pointwise polynomial products in the retained frequency order, and the opposite transform, with error below $\sqrt2\,M(3\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$. (on [Convolution from the retained transform layout](ring-convolution.md))
- The Fourier transform of coprime source lengths $s_i$ is expressed, with its two coordinate permutations left inside the identity, through transforms on the padded power-of-two box of lengths $t_i$, using linewise Gaussian maps, a Bluestein chirp convolution, and a cancellation of the retained source permutation across a convolution.
- Choosing compatible parameters, the radix-digit convolution is mapped to prime axes, transformed, multiplied pointwise, inverted, rescaled, rounded and carried to give the exact binary product in time $O(n(\lg n)^{1-\kappa})$.

## Steps this page derives

The argument gives this page these sub-steps of its step (S2, S3, S8, S9). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2**: Moving a digit, splitting a stream on a digit, cyclically splitting rows among $W$ streams and merging them, and cyclically shifting or rescaling a later field by control fields all take $O(V)$ steps on a fixed number of tapes.
How: Prove two lemmas on single scans with counters, splitting into streams and merging.

**S3**: There are two fixed linear networks, a bit network over $\mathbb F_2$ and a complex network over $\mathbb Z[i,1/2]$, that exchange two banks of values with prescribed signs, restore every scratch wire, and have total edge rank $s<Wm$.
How: Build a scalar exchange network from subset-intersection gates, attach nested nondegenerate subspaces to its gates so that an edge costs only its dimension change, and count the dimension changes.
- S3.6: Both networks satisfy $s/W<m^{\tau}$ with the explicit rational exponent $\tau=1-2^{-50}$.
  Source: "\frac{s_{\rm b}}{W_{\rm b}}<m^\tau," (paper)
  > The relative rank deficits are \[ \eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m} =\frac{339}{22587335000000},\qquad \eta_{\rm c}=\frac{W_{\rm c}m-s_{\rm c}}{W_{\rm c}m} =\frac{73}{19906842167500}. \] For both recurrences we may use the fixed rational exponent \begin{equation} \tau=\sigma=1-2^{-50}. \label{eq:explicit-motif-exponents} \end{equation} Both exact deficits displayed above are greater than $20\cdot2^{-50}$. Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence \[ m^{1-2^{-50}} =m\exp(-2^{-50}\log m) >m(1-20\cdot2^{-50})>m(1-\eta) \] for either $\eta=\eta_{\rm b}$ or $\eta=\eta_{\rm c}$. Consequently \[ \frac{s_{\rm b}}{W_{\rm b}}<m^\tau, \qquad \frac{s_{\rm c}}{W_{\rm c}}<m^\sigma, \qquad 0<\tau=\sigma<1. \] Here $\sigma$ is a rational upper bound for the logarithmic exponent of the complex recurrence. \section{Faster interchange of address chunks} \label{sec:tape-interchange}

**S8**: The Fourier transform of coprime source lengths $s_i$ is expressed, with its two coordinate permutations left inside the identity, through transforms on the padded power-of-two box of lengths $t_i$, using linewise Gaussian maps, a Bluestein chirp convolution, and a cancellation of the retained source permutation across a convolution.
How: Apply Gaussian resampling line by line along each axis of the padded box, rewrite the middle power-of-two transform as a convolution with a chirp, and show that the leftover permutation cancels in a product.

**S9**: Choosing compatible parameters, the radix-digit convolution is mapped to prime axes, transformed, multiplied pointwise, inverted, rescaled, rounded and carried to give the exact binary product in time $O(n(\lg n)^{1-\kappa})$.
How: Fix the parameters, place the digits on a product of prime cyclic axes, run the source transform on each operand, multiply and invert, then bound the error to round exactly and add up the costs.
- S9.0: The exponents are fixed rationally, for instance $\tau=\sigma=1-2^{-50}$, $\lambda=1-2^{-52}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $\epsilon=2^{-75}$, $\kappa=2^{-182}$, and satisfy every layer condition with room to spare.
  Source: "These constants are deliberately conservative; no optimization is claimed." (paper)
  > The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Rank saving and the power-saving recurrence](rank-saving-recurrence.md)): If a network of $W$ wires has total edge rank $s<Wm$, a call at parameter $e=mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$, so the cost per unit volume obeys $F_k\le(s/W)F_{k-1}+O(1)$ and grows only like $e^{\tau}$ with $\tau<1$.
- S4 (on [Fast interchange of address chunks](chunk-interchange.md)): Two disjoint address chunks of $u$ bits in an array with complete Cartesian address set can be exchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$, although the intermediate steps form XOR combinations of the data.
- S5 (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)): One $H_0$ butterfly applied at the same bit offset in $D\le d$ address chunks at once is computed exactly, with a single final truncation, in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$.
- S6 (on [Transform layout and cost](transform-layout.md)): A positional permutation moves selected bits of the $d-1$ axes to a common offset in $K$-bit chunks so that each transform round is one simultaneous layer, giving a forward and an opposite synthetic transform each costing $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.
- S7 (on [Convolution from the retained transform layout](ring-convolution.md)): Normalized convolution over the negacyclic ring is computed by two forward synthetic transforms, pointwise polynomial products in the retained frequency order, and the opposite transform, with error below $\sqrt2\,M(3\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.
- S2.1 (on [Elementary stream operations](elementary-streams.md)): Four basic stream operations (permuting two digit values, moving one digit, split-map-merge on a digit, and cyclic row splitting into $W$ streams) each cost $O(V)$.
- S2.2 (on [Controlled cyclic shifts and rational scalings](controlled-shifts.md)): A later target field $y\in[Q]$, $Q=q^b$, can be shifted cyclically by an offset computed from earlier control fields, or multiplied by a rational unit modulo $Q$, in $O(V)$ time.
- S3.1 (on [Three-subset gather and scatter network](subset-intersection-network.md)): Three stages of copy, gather, scatter and side-injection gates, whose net coefficient depends on the intersection size of two 3-subsets and is cancelled by scratch wires, realize $(X,Y)\mapsto(-Y,X)$ and restore every scratch wire.
- S3.2 (on [Role networks and frames](gate-network-frames.md)): If every vertex of the network carries an invertible frame $D_v$ on its wire arrays, the network implements $D_{\rm out}\mathsf S D_{\rm in}^{-1}$, so only the changes of frame $D_vD_u^{-1}$ along edges cost work.
- S3.3 (on [Subspace labels and the rank budget](subspace-labels.md)): Attaching to each gate and terminal a nondegenerate subspace of an $m$-dimensional space, nested along every edge, makes an edge cost its dimension change; only the central wires lose dimension, with total loss $L<N/2$, so the sum of absolute dimension changes is $Wm-2N+2L$.
- S3.4 (on [Bit network as an address shear](bit-network-interface.md)): Using the projection matrices of the labels as frames, the XOR network turns the role exchange into the shear $H\leftarrow H+D$ on every role, with total rational edge rank $s<Wm$.
- S3.5 (on [Binary phase frames](phase-interface.md)): With binary labels and the phase frame $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{\operatorname{wt}(P_Ux)})H^{\otimes m}$, every edge changes by a product of two-point kernels $aI+bX_v$, one per residual basis vector, and the whole complex network equals $C^{\otimes m}$ on every role, with total edge rank $s<Wm$.
- S8.1 (on [Gaussian resampling](gaussian-resampling.md)): For coprime $s_i<t_i$ with $t_i/s_i-1>p/\alpha^4$ there are linear contractions $A$ and $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computable with error below $p^2$ in time $O(t_ip^{3/2+\delta}\alpha)$.
- S8.2 (on [Tensor resampling on a padded box](tensor-resampling-box.md)): The one-dimensional resampling maps are applied line by line along each axis of a zero-padded power-of-two box, with axes exposed by chunk interchanges, giving error below $dp^2$ and cost $O(dTp^{3/2+\delta}\alpha)$ plus $O(Tp\,d^2(1+\ell^\tau))$ for movement.
- S8.3 (on [Bluestein chirp identity](bluestein-chirp.md)): A Fourier transform including its target permutation equals a pointwise chirp phase, a cyclic convolution with the chirp, and another pointwise chirp phase: $QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$.
- S8.4 (on [Cancellation of the retained source permutation](permutation-cancellation.md)): The coordinate permutation $R$ left inside the resampled transform cancels across two forward transforms, their pointwise product and the opposite transform: $RF_{\boldsymbol s}^+[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=u*v/S^2$.
- S9.1 (on [Size parameters of the multiplication](size-parameters.md)): From $n$ set $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, box size $T\approx n/b$ and axis lengths $t_i\in\{r/2,r\}$ with $r=2^\ell$, so that $Tp=\Theta(n)$, $r$ exceeds every fixed power of $p$, and the radix-$2^b$ digit product has no wraparound modulo $x^S-1$.
- S9.2 (on [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)): A cyclic convolution of length $S=s_1\cdots s_d$ with pairwise coprime $s_i$ becomes a convolution on the product of cyclic axes of lengths $s_i$ via $x\mapsto\prod_ix_i^{\mu_i}$, implemented by triangular controlled shifts and axis moves in time $O(Tp\,d^2(1+\ell^\tau))$.
- S9.3 (on [Phase twist from cyclic to negacyclic](coefficient-twist.md)): Multiplying coefficient $k$ by $\zeta^k$ with $\zeta=e^{\pi i/r}$ maps $\mathbb C[x]/(x^r-1)$ isomorphically onto the polynomial ring modulo $y^r+1$, so cyclic convolution is computed over the ring and untwisted.
- S9.4 (on [Source Fourier transform procedure](source-transform.md)): The computed source transform $\widetilde{\mathscr F}$ applies the linewise Gaussian map $A$, the chirp transform done by complex convolution through the phase twist, the linewise map $B_0$ and an exact $2^\gamma$ rescale, and approximates $RF_{\boldsymbol s}$.
- S9.5 (on [The multiplication algorithm](multiplication-algorithm.md)): Split the operands into radix digits, map them by $\Phi$ to the prime axes, apply the source transform to each, multiply pointwise, apply the opposite transform, rescale by $S$ and $2^{2b+4}$, round to integers, undo $\Phi$ and propagate carries.
- S9.6 (on [Precision and exact recovery](exact-recovery.md)): Disk-margin and error bookkeeping shows the error in each recovered coefficient is below $1/2$, so rounding gives the exact integer convolution coefficients and carries give the exact binary product.
- S9.7 (on [Cost table and the saving exponent κ](time-accounting.md)): Dividing each cost by $V=Tp$, seven dominant terms have powers of $p$ at most $1-2\kappa$ below one; the smallest margin $2^{-181}$ fixes $\kappa=2^{-182}$, and any polylog factor is absorbed.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Arrays, address fields and logical volume](array-layout.md)
- [Fixed-tape Turing machine model](multitape-model.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Multidimensional transforms and convolution on several axes](multidimensional-transform.md)
- [Fixed-point complex arithmetic and truncation error](fixed-point-numerics.md)
- [Established O(n log n) integer multiplier](nlogn-multiplier.md)
- [Transform layout and cost](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Cancellation of the retained source permutation](permutation-cancellation.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Cost table and the saving exponent κ](time-accounting.md): Dividing each cost by V = Tp, seven dominant terms have powers of p at most 1 − 2κ below one; the smallest margin 2^{-181} fixes κ = 2^{-182}, and any polylog factor is absorbed.
  Shown as: Integer multiplication below n log n *<predicate>* Cost table and the saving exponent κ
- [Precision and exact recovery](exact-recovery.md): Disk-margin and error bookkeeping shows the recovered coefficient error stays below 1/2, so rounding gives the exact integer convolution coefficients and carries give the exact binary product.
  Shown as: Integer multiplication below n log n *<predicate>* Precision and exact recovery
- [The multiplication algorithm](multiplication-algorithm.md): Split the operands into radix digits, map them by Φ to prime axes, apply the source transform to each, multiply pointwise, apply the opposite transform, rescale by S and 2^{2b+4}, round to integers, undo Φ and propagate carries.
  Shown as: Integer multiplication below n log n *<predicate>* The multiplication algorithm
- [The n log n optimality conjecture](nlogn-conjecture.md): Schönhage and Strassen's 1971 proposal that n log n is the optimal order of growth for multitape multiplication, which a power saving in the log factor refutes.
  Shown as: Integer multiplication below n log n *<predicate>* The n log n optimality conjecture

## Other pages you may link to

- [Two-point butterfly H₀ and the kernel C](two-point-butterfly.md)
- [Fixed-tape Turing machine model](multitape-model.md)
- [Established O(n log n) integer multiplier](nlogn-multiplier.md)
- [Arrays, address fields and logical volume](array-layout.md)
- [Role networks and frames](gate-network-frames.md)
- [Elementary stream operations](elementary-streams.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Restoring arbitrary scratch values](scratch-restoration.md)
- [Three-subset gather and scatter network](subset-intersection-network.md)
- [Nondegenerate subspaces and orthogonal residuals](nondegenerate-subspaces.md)
- [Subspace labels and the rank budget](subspace-labels.md)
- [Rank saving and the power-saving recurrence](rank-saving-recurrence.md)
- [Bit network as an address shear](bit-network-interface.md)
- [Binary phase frames](phase-interface.md)
- [Lower-triangular factorization of a matrix](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Power-width address interchange](power-width-interchange.md)
- [Fast interchange of address chunks](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Multidimensional transforms and convolution on several axes](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Decimation-in-frequency butterflies and bit-reversed frequency order](butterfly-recursion.md)
- [Fixed-point complex arithmetic and truncation error](fixed-point-numerics.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout and cost](transform-layout.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Cancellation of the retained source permutation](permutation-cancellation.md)
- [Tensor resampling on a padded box](tensor-resampling-box.md)
- [Choosing prime source lengths](prime-lengths.md)
- [Size parameters of the multiplication](size-parameters.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Phase twist from cyclic to negacyclic](coefficient-twist.md)
- [Source Fourier transform procedure](source-transform.md)

## Evidence from the sources, with the paragraph around each quote

- "There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes," (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}

- "T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right)," (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}


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

Write the body to `exegenius/tasks/0048-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0048-write-main-theorem.answer.json`, then run `exegenius submit 0048-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0048-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
