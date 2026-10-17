# exegenius task 0317-goals

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Write goal questions for testing whether an explanatory wiki teaches its reader. Simulated readers with the reader's background will each try to answer one question using only the wiki, and a grader will check their answers against your key points. The questions are never shown in the wiki.

- Write the number of goals the task asks for: at least one about the target result itself, the rest about the main steps on the way to it.
- `kind`: one of the kinds in the schema, each a kind of understanding a reader of a proof can show (after Mejía-Ramos et al.'s assessment model of proof comprehension, and Hamami and Morris on why a proof proceeds as it does). `meaning` and `status` test single statements; the rest test how statements fit together. Make at least half of the goals of the other kinds, include at least one `summary`, `structure`, `transfer` or `example` goal, and at least one `motivation` goal. Use the argument's steps below for `motivation`, `structure` and `summary` goals. A motivation the argument marks as not stated by the sources is a good test of whether the wiki supplies it, and each striking feature listed there calls for a `justification` goal asking why it holds.
- `key_points`: 2 to 5 short, checkable statements that a full answer must make, accurate to the sources, each with a `role`: the `claim` asserted, the `reason` it holds, the `conclusion` that follows, or the `background` it rests on. A goal about why something holds needs at least one `reason`. Phrase key points of the kinds other than `meaning` and `status` in your own words: submit rejects such a key point if it appears word for word on a page, since a reader could copy it without understanding.
- `pages`: the ids of the pages a reader needs to answer the question.
- Ask what this reader could answer after reading those pages well, not trivia.

## Goals

Write 3 to 6 goals.

## Target

Power-saving integer multiplication: A deterministic fixed-tape Turing machine multiplying two n-bit integers exactly in O(n(lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is a computer science undergraduate: they have taken discrete mathematics, an algorithms course (asymptotics, divide and conquer, schoolbook and Karatsuba multiplication, sorting), a first linear algebra course (vector spaces, subspaces, dimension, rank, matrices as linear maps, inverses, triangular matrices, orthogonality, bilinear forms at a basic level), calculus, elementary number theory (primes, gcd, modular arithmetic) and basic machine-level binary representation (XOR, two's complement). They have seen Turing machines with tapes only at an introductory level. They have not been taught the discrete Fourier transform or FFT as such, abstract algebra beyond basic definitions (quotient rings, finite fields as a theory), tensor products, numerical error analysis, or the specific literature on fast integer multiplication.

## Pages, in reading order

- `ring-y`: Polynomial ring modulo y^r + 1 — Polynomials of degree below r over the complex numbers with y^r = −1, so multiplying by a power of y is a signed shift of the coefficient list.
- `machine-model`: Fixed finite-tape machine model — The computation model of the main theorem: one fixed finite alphabet and a fixed number of one-dimensional tapes, each head moving at most one cell per step.
- `conjecture`: Schönhage–Strassen optimality conjecture — The 1971 proposal that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.
- `fixed-point`: Fixed-point Gaussian dyadic records — Complex values stored as signed two's-complement integers over a power-of-two denominator 2^{-p}; intermediate values are exact and one truncation Q_p rounds back to the p-bit grid.
- `exchange-network`: Linear exchange network with restored scratch wires — A fixed network of linear gates on wires holding values that swaps two banks with a prescribed sign while undoing the effect of arbitrary initial scratch values, built from three-element subsets.
- `array-frames`: Frames on wire arrays — Replacing each wire scalar by an array and assigning an invertible operator D_v (a frame) at each gate so the pointwise gate commutes with the frame and only the endpoint frames matter.
- `convolution`: Cyclic convolution — The product of two sequences (or elements of a polynomial quotient ring) where indices wrap around: (f∗g)_k = Σ f_j g_{k−j}.
- `radix-digit-reduction`: Multiplication as radix-digit convolution — Splitting each integer into radix-2^b digits turns the product into a convolution of short integer coefficients, which carry propagation turns back into a binary number.
- `phase-twist`: Phase twist — Multiplying coefficient k by e^{πik/r}, which converts the cyclic coordinate modulo x^r − 1 into the negacyclic ring modulo y^r + 1 and is removed afterwards.
- `dft`: Discrete Fourier transform — The normalized transform (F_q u)_k = (1/q) Σ u_j e^{−2πi jk/q}, which turns convolution into pointwise multiplication.
- `butterfly`: Butterflies and the fast transform — A two-point averaging/differencing step H₀(u,v) = ((u+v)/2, (u−v)/2) whose repeated use over address bits, with twiddle multiplications, computes a transform in log t layers.
- `synthetic-transform`: Synthetic polynomial transform — A transform over the ring modulo y^r + 1 whose roots of unity are powers of y, so every twiddle multiplication is a signed shift of a coefficient list.
- `stream-ops`: Elementary stream operations — Linear-time scans on arrays stored in lexicographic order: swapping two digits, moving a digit, splitting into streams, applying a pointwise map and merging back.
- `chirp`: Bluestein chirp identity — An identity that rewrites a (permuted) Fourier transform as a pointwise chirp phase, a cyclic convolution, and another chirp phase.
- `hvdh-multiplier`: Established O(n log n) multiplier — The earlier Harvey–van der Hoeven multitape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine.
- `signed-packing`: Signed packing — A signed Kronecker substitution that evaluates polynomials with signed coefficients at 2^{4p} to form large integers, multiplies them with the O(n log n) multiplier, and recovers the product coefficients.
- `controlled-shifts`: Controlled shifts and rational scalings — Updating a target address field by an offset computed from earlier control fields, or multiplying it by a unit, in time linear in the array volume.
- `matrix-shear`: Matrix shear by triangular factorization — Factoring a rational matrix as A = E₁ΠE₂ with lower triangular E₁, E₂ and partial permutation Π lets the shear (H,D)→(H+AD,D) be done with exactly rank(A) field interchanges.
- `phase-kernel`: Two-point kernel C — The matrix C = aI + bX with a = (1+i)/2, b = (1−i)/2, a square root of the bit flip, linked to the butterfly by H₀ = b·S·C·S with S = diag(1, i).
- `contraction-maps`: Contractions and bilinear contractions — A linear map that never increases the norm of a vector, and a bilinear map whose output norm is at most the product of the input norms, so errors in the inputs do not grow beyond a controlled bound.
- `multidim-transform`: Multidimensional transforms — A transform over several axes at once, the tensor product of one-dimensional transforms, applied to an array one axis at a time.
- `crt-map`: Chinese-remainder address map — An isomorphism that places a cyclic convolution of length S = s₁⋯s_d on pairwise coprime prime axes, implemented as triangular controlled shifts.
- `gaussian-resampling`: Gaussian resampling — Re-expressing a Fourier transform of prime length s through a transform of nearby power-of-two length t using Gaussian weights, so that only power-of-two transforms are needed.
- `retained-permutations`: Retained permutation cancellation — Leaving the coordinate permutations of resampling inside the transform identity, so the source permutation cancels across the two forward transforms and the opposite one and none is executed as a sort.
- `frequency-order`: Retained frequency order — The forward synthetic transform writes its outputs in bit-reversed order, the pointwise product keeps that order, and the opposite transform consumes it, so no reordering is executed.
- `precision-recovery`: Error tracking and exact recovery — Each normalized transform and product is a contraction with a bounded rounding error, and the total error on the recovered convolution coefficients is below 1/2, so rounding gives exact integers.
- `parameter-choice`: Parameter and prime-length choice — Fixed rational exponents and sizes (precision p = 6b, d axes, K = d^c, T and r powers of two, prime lengths s_i just below t_i) making every hypothesis of the lemmas hold.
- `tensor-product-of-spaces`: Tensor products of subspaces — The space built from two spaces whose dimension is the product of their dimensions, in which operators and bilinear forms act factorwise.
- `subspace-labels`: Nested subspace labels and rank deficit — Assigning nondegenerate subspaces of an m-dimensional space to gates so adjacent labels are nested; the total dimension change over edges, the number s of smaller calls, is strictly less than W·m.
- `rank-recurrence`: Recursive power saving — Each call at parameter m·f makes s calls at parameter f on streams of 1/W the volume, so cost per unit volume grows by s/W < m per factor m, giving a power saving.
- `address-interchange`: Fast address-chunk interchange — The first tape procedure: exchanging two disjoint equal-width address fields of u digits in time O(V·u^τ) for a fixed τ < 1, using XOR combinations of intermediate data.
- `phase-frames`: Binary phase frames — Frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} whose edge differences are products of translation kernels aI + bX_v, one per vector of an orthonormal residual basis.
- `packed-bit-addition`: Packed selected-bit addition — XORing selected bits between two address chunks (with a third chunk as restored scratch) using cyclic shifts of whole chunk ranges plus a repair of explicitly bounded exceptional addresses.
- `simultaneous-layer`: Simultaneous butterfly layer — The second tape procedure: applying H₀ coefficientwise on the same bit of up to d address chunks in time O(V·d^λ′) for a fixed λ′ < 1, instead of d passes.
- `transform-layout`: Tape layout for synthetic transforms — Placing the selected bits of the participating axes at a common offset in K-bit chunks so each round of the synthetic transform is one simultaneous layer, costing less than log t passes.
- `ring-convolution`: Convolution from the retained transform layout — Convolution over the ring modulo y^r + 1 on the remaining axes by two forward synthetic transforms, pointwise polynomial products and the opposite transform, normalized by 1/(rM).
- `multiplication-algorithm`: The multiplication algorithm — Digits, then the CRT map, two forward transforms with resampling and chirps, a pointwise product, the opposite transform, rescaling, rounding and carry propagation yield the exact 2n-bit product.
- `cost-accounting`: Cost accounting and the exponent κ — Dividing each cost by V = Tp, the dominant terms are powers of p below one with minimum margin 2^{-181} = 2κ, giving total time O(n(lg n)^{1−κ}).
- `main-result`: Power-saving integer multiplication — A deterministic fixed-tape Turing machine multiplying two n-bit integers exactly in O(n(lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model.

## The argument's steps

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. (`main-result`)
  - How: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved.
  - Striking feature: The power saving $\kappa=2^{-182}$ is astronomically small, yet strictly positive, so the algorithm's running time is $o(n\log n)$ through all input lengths.
  - Why (stated by the sources): Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$, so the logarithmic factor can only be beaten by cheaper address movement and cheaper butterfly arithmetic.
  - Both tape primitives (the interchange of two address chunks of $u$ digits and the simultaneous butterfly layer on up to $d$ axes) cost the volume times a power below one of their width, because a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$, so the cost per unit volume grows by $s/W<m$ per factor $m$ of the parameter. (`rank-recurrence`)
    - How: Build a fixed finite linear network of $W$ wires that exchanges two banks and restores all scratch values, make the representation of each wire's array vary along the network through frames so that an edge costs one smaller call per unit of rank, show the total rank $s$ is below $Wm$, fix an exponent, and solve the recurrence in the bit variant (interchange) and the complex variant (butterfly layer).
    - Striking feature: The saving is tiny but strictly positive: $s/W=m(1-\eta)$ with $\eta\approx10^{-11}$, so the resulting exponent is $1-2^{-50}$, only just below 1; the whole power saving rests on the strict inequality $s<Wm$.
    - Why (stated by the sources): Dividing cost by volume, passing from parameter $f$ to $mf$ multiplies the recursive contribution by $s/W$, which is strictly less than the factor $m$ by which the parameter grew when $s<Wm$; so the recursion's solution is a power of the parameter below the first power.
    - There is a fixed linear network of $W$ wires on two banks $X_a,Y_a$ ($a\in\mathcal T^3$, $\mathcal T$ the three-element subsets of $[h]$) that sends $(X_a,Y_a)\mapsto(-Y_a,X_a)$ and restores every scratch wire whatever its initial value, in a bit version (wires $W_{\rm b}$) and a complex version (wires $W_{\rm c}$). (`exchange-network`)
      - How: Build one forward invocation $y_S\gets y_S+x_S$ from three-element subsets of $[h]$: a central route through gather and scatter wires whose coefficient depends on the intersection size, plus side wires that cancel the unwanted coefficients, bracketed by subtract and undo rows; then chain three stages, the middle one run inverted.
      - Why (stated by the sources): Gather and scatter through a few central wires give a low-rank route, but their coefficient depends on how two triples intersect; the side wires correct exactly the unwanted intersection sizes, and the subtract and undo rows make the result independent of the arbitrary scratch contents.
      - For arbitrary initial scratch values, one forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.
        - How: Compute the net change of the target as (side injection)(copy) + (scatter)(gather) applied to $x$, showing it does not depend on the initial side and central values $a,c$, then compare its coefficients with the identity case by case (bit and complex).
        - Why (recoverable from the sources): The eight-row schedule first subtracts the effect of the unknown old scratch values, then adds the source's effect, then restores the scratch values, so the net map is a fixed matrix in $x$ alone; reading off its coefficients shows what must cancel.
    - If every scalar wire value is replaced by an array over a finite address set $\Omega$ and every gate acts pointwise, then assigning an invertible operator $D_v$ (a frame) to each source, gate and sink, with the same $D_v$ on all incidences of a gate, makes the network apply $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$: a route from input role $w$ to output role $\rho(w)$ applies only the endpoint frames $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ and its scalar sign. (`array-frames`)
      - How: Maintain the invariant 'stored array = $D_v$ applied to the logical array' at every vertex, checking it at sources by definition, along edges by applying $D_vD_u^{-1}$, and across gates by linearity.
      - Why (stated by the sources): A linear pointwise gate commutes with any operator applied identically to all its input arrays, so the frames telescope along each route and only the two endpoint frames matter, leaving the intermediate frames free to be chosen so that each edge change is cheap.
    - Attaching to the gates nondegenerate subspaces of an $m$-dimensional space, nested along every edge, the number of smaller calls (the total rank of the edge changes) is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$ for the bit network and $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$ for the complex network, both strictly less than $Wm$, because $L/N<1/2$. (`subspace-labels`)
      - How: Choose labels in $\mathcal F=F^{\otimes3}$ built from the triple indicator vectors, with terminal labels $U_a\to\mathcal F$ on $X_a$ and $0\to U_a^\perp$ on $Y_a$; expose one tensor factor per stage; tabulate dimension changes edge by edge to find that all decreases are the central wires' return from time 3 to 4; then convert the dimension count into rational rank (bit) and Gaussian-dyadic phase kernels (complex).
      - Striking feature: The saving is minuscule but strictly positive: $s_{\rm b}/W_{\rm b}=m(1-\eta_{\rm b})$ with relative deficit $\eta_{\rm b}=339/22587335000000\approx1.5\cdot10^{-11}$, because $L_{\rm b}/N=100/539<1/2$.
      - Why (stated by the sources): Total dimension is conserved by telescoping at gates, so the sum of changes is fixed by the terminal labels; the saving is whatever the unavoidable decreases $L$ leave of the budget $N$, so the labels are designed to confine every decrease to one small edge.
      - Every edge joins comparable nondegenerate labels, the only decreasing edges are the central-wire edges from time 3 to time 4 (each losing dimension $h$), so $L=Ic\,h$ and the sum of absolute dimension changes is $Wm-2N+2L$.
        - How: Tabulate the orthogonal residual of every edge type of the gate schedule and its dimension, observe that dimension is nondecreasing except on centre wires from time 3 to 4, then sum signed changes by telescoping at each gate and convert signed to absolute changes.
        - Why (recoverable from the sources): Each edge joins a smaller label inside a larger one, so its cost is governed by the dimension of the orthogonal residual; listing the residual of each edge type shows exactly where dimension is lost, and telescoping converts the terminal dimensions into a total.
      - Bit network: assigning the projection $P_U$ to each vertex with label $U$ and $-P_{U_a}$ to the source of $X_a$ gives endpoint difference $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ on every input role, and total rational rank $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.
        - How: Use projections along the labels as the rational frames: an edge between nested labels changes the matrix by a projection difference of rank equal to the dimension change, except at the $N$ negative source projections, which cost one extra rank each.
        - Why (recoverable from the sources): A frame matrix $P_U$ makes the shear on an edge a map of rank equal to the dimension change of the label, so counting dimensions counts recursive calls; the source projection $-P_{U_a}$ is what makes the endpoint difference exactly the identity.
      - Complex network: with binary labels and the phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{\operatorname{wt}(P_Ux)\bmod 4})H^{\otimes m}$, every edge difference is a product of one translation kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal basis of the edge residual; the total number of kernels is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$ and, after endpoint corrections, the network applies $C^{\otimes m}$ on every role. (`phase-frames`)
        - How: Use Hamming weight modulo 4 as the phase: on orthogonal binary vectors weights add modulo 4, so a frame difference along an orthonormal residual basis is a sum of single-vector phases, each of which is a translation kernel; the one pair $X_a\to Y_a$ with an inverse kernel on 27 coordinates is repaired using $C=iZC^{-1}Z$.
        - Why (recoverable from the sources): Binary orthonormal bases turn a frame difference into independent two-point kernels, one per basis vector, so that each residual dimension is one smaller call of the same butterfly-type operation, as the recursion needs.
    - With $\tau=\sigma=1-2^{-50}$ one has $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$, so $0<\tau=\sigma<1$ are admissible exponents for both recurrences.
      - How: Compare the relative deficit $\eta$ with $20\cdot2^{-50}$ and bound $m^{1-2^{-50}}$ from below by the chain $m^{1-2^{-50}}=m\exp(-2^{-50}\log m)>m(1-20\cdot2^{-50})>m(1-\eta)=s/W$.
      - Why (recoverable from the sources): The recursion needs a rational exponent strictly between $\log_m(s/W)$ and 1; since $s/W=m(1-\eta)$ with $\eta$ tiny but explicit, a power of the form $m^{1-\epsilon'}$ is just above it, and integer comparisons suffice to check it.
    - Bit variant: two disjoint address chunks of $u$ bits can be interchanged on a fixed number of tapes in $O(Vu^\tau)$ time, $\tau=1-2^{-50}$, although the intermediate steps form XOR combinations of data. (`address-interchange`)
      - How: Run the bit network on the digits of the chunks: an edge whose matrix has rank $a$ costs $a$ interchanges of fields of $1/m$ the width (matrix shear), the $W$ role streams carry $1/W$ of the volume each, so the cost per unit volume satisfies $F_k\le(s/W)F_{k-1}+O(1)$; then remove the restrictions on width and rows.
      - Striking feature: The saving is a power $u^\tau$ with $\tau=1-2^{-50}$ only barely below 1, although the interchange has no data-dependent arithmetic.
      - Why (stated by the sources): The sum of the edge ranks is less than the number of wires times $m$, so the recurrence saves a power of the chunk width.
      - For a rational $m\times m$ matrix $A$ of rank $a$ and fields over $\mathbb Z/q^b\mathbb Z$, the shear $(H,D)\mapsto(H+AD,D)$ can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work. (`matrix-shear`)
        - How: Factor $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with exactly $a$ ones; do the triangular parts by linear-time controlled shifts in descending physical order and realise each one of $\Pi$ as $H_i\gets H_i+D_j$ by two controlled shifts and one interchange.
        - Why (recoverable from the sources): A lower triangular change of coordinates only updates a later field from earlier fields, which a controlled shift does in linear time, so all the rank of $A$ is concentrated in the partial permutation $\Pi$, and each of its $a$ ones needs only one genuine interchange.
      - Power-width interchange: if the circuit data satisfy the shear contract with $s<Wm$ and $s/W<m^\tau$, two disjoint chunks of $e=m^k$ radix-$q$ digits each (with a row field of length divisible by $W^k$ before both) can be interchanged in $O(Ve^\tau)$ time.
        - How: Reduce the interchange to the shear $H\gets H+D$, implement the shear by the bit network run on $W$ role streams of volume $V/W$ with frame $\Phi_{A_e}$ on each edge, each edge being $\operatorname{rank}(A_e)$ smaller interchanges, obtain the recurrence $F_k\le(s/W)F_{k-1}+O(1)$ and solve it.
        - Why (recoverable from the sources): The network performs the shear on every row by routing rows through $W$ roles, and each role's edge operator is a shear of lower width by the matrix-shear lemma; the number of smaller calls is the total rank $s$ but each call touches only $1/W$ of the volume, which is exactly the recursion that $s<Wm$ makes sub-linear.
        - From $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$ with $s/W<m^\tau$ it follows that $F_k=O(e^\tau)$ for $e=m^k$.
          - How: Unroll the recurrence to a geometric sum $\sum_{j=0}^{k}a^j$ with $a=s/W$ and bound it separately for $a\le1$ and $a>1$.
          - Why (recoverable from the sources): Each level contributes a constant times the $j$-th power of the ratio $a=s/W$ of work to volume; a geometric sum is dominated by its largest term when $a>1$ and by its length when $a\le1$, and both are at most the power $m^{k\tau}=e^\tau$ because $a<m^\tau$.
      - For arbitrary widths $u$, prefixes, gaps and suffixes (including one-bit payloads) the interchange $(p,h,g,d,z)\mapsto(p,d,g,h,z)$ of two $u$-bit chunks costs $O(Vu^\tau)$.
        - How: Supply the required rows from the chunks' own $\rho=O(\log e)$ high digits, pad the rows to a multiple of $W^k$, split the remaining width $e-\rho$ in base $m$ into $a_j$ pieces of width $m^j$, interchange each piece by the power-width case, and sum the geometric series.
        - Why (recoverable from the sources): The power-width case needs a row field divisible by $W^k$, which a general array need not have; taking a few high digits of the chunks as row index costs only $O(V\rho)$, and an arbitrary width is a sum of at most $(m-1)(k+1)=O(\log e)$ power widths whose costs $m^{j\tau}$ sum to $e^\tau$.
    - Complex variant: the tensor product of $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ on one bit of each of $D\le d$ address chunks (each of $K$ bits, selected at a common offset), acting coefficientwise on polynomial records with $r$ complex $p$-bit coefficients, is computed exactly followed by one truncation $Q_p$, in $O(Vd^{\lambda'})$ time with $\lambda'<1$, rather than $D$ whole-array passes. (`simultaneous-layer`)
      - How: Rewrite $H_0^{\otimes D}$ as $b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ with the kernel $C$, apply $C^{\otimes e}$ to a group of $e=mf$ axes by the complex network with column phase frames (the binary changes of basis done by packed selected-bit additions), so that each of the $s_{\rm c}$ edge-residual vectors is one child on $f=e/m$ axes of volume $V/W$, and unroll the resulting recurrence with an exact-width guard bound.
      - Striking feature: The cost is $O(Vd^{\lambda'})$ with $\lambda'=1-2^{-54}$, only barely below the $D\le d$ separate passes, and the saving comes from $s_{\rm c}/W_{\rm c}<m^\sigma$.
      - Why (stated by the sources): Separate butterfly factors would require $D$ whole-array passes; the network's phase frames let one $C^{\otimes e}$ layer be expressed by $s_{\rm c}<W_{\rm c}m$ smaller layers on streams of volume $V/W_{\rm c}$, which is the same recursion as for the interchange.
      - A group of $e=mf$ axes is handled by the complex network: each edge residual vector is one child on $f$ axes, an arbitrary residual basis is moved into coordinate position by binary changes of basis (products of at most $m(m-1)+3m$ row additions), and inverse children use forward ones, so there are exactly $s_{\rm c}$ children.
        - How: Conjugate the edge identity by a basis change $\mathcal P_M$ so that the residual vectors become the first coordinate vectors, apply one child $(C^{\epsilon_h})^{\otimes f}$ per residual vector to the $f$ bits of slot $h$, and use $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$ to avoid inverse children.
        - Why (recoverable from the sources): A residual basis need not consist of coordinate vectors; since $\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}$, conjugation by an invertible binary change of basis (a fixed product of row additions) moves it into coordinate position without a general transpose.
      - Selected bits of two chunks can be XORed (with a third chunk as restored scratch) by eight cyclic shifts of whole chunk ranges plus a repair of an explicitly bounded exceptional set of addresses, in time $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$. (`packed-bit-addition`)
        - How: Apply eight packed parity-conditioned additions (a composition of two three-cycles) simultaneously to $f-1$ disjoint $K$-bit segments, so it equals the ideal XORs away from addresses where a guard value is too close to a segment boundary, then repair those addresses by extracting them and sorting.
        - Why (recoverable from the sources): Parity-conditioned additions flip the target parity and restore the auxiliary integer, and they can be applied to all segments at once as one cyclic shift of a whole chunk range, costing linear time per rotation; carries between packed segments only occur at a small, address-determined set of exceptional addresses.
      - A group of $e$ selected axes (with $D$ axes in all and $q_0$ of them handled individually) is processed in $O(V\,d^{\lambda'})$ time by the recurrence $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ stopped at $e<d^\beta$.
        - How: Use the first $q_0$ chunks as the row index so the rows split into $W$ role streams of volume $1/W$ at each level, bound the overhead of each node by the cost of the binary basis changes, stop the recursion when $e<d^\beta$ and sum internal nodes and leaves separately, then combine the base-$m$ groups.
        - Why (recoverable from the sources): Splitting rows into $W$ streams is what makes each of the $s$ children cost only $1/W$ of the parent, so the normalized recursion has branching factor $s/W<m^\sigma$; the overhead $(eK)^\tau$ is a power of $e$ only because $K=\lfloor d^c\rfloor\le e^{c/\beta}$ for $e\ge d^\beta$.
      - The whole layer can be evaluated exactly: with $\Delta=\lceil C_0d^{C_1}\rceil$, reserving $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits per real component represents every intermediate coefficient exactly, and this width is $O(p)$ because $\epsilon C_1<1$.
        - How: Bound the number $A(e)$ of arithmetic operations on any chain from an input coefficient to an intermediate one by a recurrence over the recursion, solve it, and note that each operation at most doubles the modulus and adds one denominator bit.
        - Why (recoverable from the sources): Exactness requires bounding the denominator growth and the magnitude growth of values computed by many additions and halvings; both are controlled by the depth of the arithmetic dependency chains, which follows a simple recurrence with $s$ children per node.
  - Synthetic transforms over $\mathcal R_r$ on $d-1$ axes of lengths $t_i\in\{2^{\ell-1},2^\ell\}$ with outputs kept in a retained layout $LB$ cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error less than $\sqrt2\ell\,2^{-p}$. (`transform-layout`)
    - How: Use the radix-two synthetic (Nussbaumer) transform, whose twiddles are signed shifts, and lay out the selected bits of all participating axes at a common offset in $K$-bit chunks so that every round is one simultaneous butterfly layer, with fewer than $\log t$ passes.
    - Why (stated by the sources): To apply the simultaneous layer in a transform round, the selected bits of the participating axes must sit at a common offset in consecutive $K$-bit chunks.
    - The synthetic transform $F_t^-$ over $\mathcal R_r=\mathbb C[y]/(y^r+1)$, with roots of unity $\omega_t=y^{2r/t}$, is computed by decimation in frequency with outputs written in bit-reversed order, $B_tF_t^-$; the pointwise product keeps this order and the reverse procedure computes $F_t^+B_t^{-1}$, so no reordering is executed. (`frequency-order`)
      - How: Prove character cancellation directly (the ring has zero divisors), derive the decimation-in-frequency recursion with twiddles $\omega_t^{-k}$, track which named slots hold frequency bits after each round, and run the recursion in reverse for the opposite transform.
      - Why (recoverable from the sources): The ring has zero divisors, so inverting the transform cannot divide by $\omega_t^j-1$ and orthogonality of characters must be checked by a direct pairing argument; writing outputs where the recursion leaves them (bit-reversed) avoids a sort.
    - On a layout $L$ that places the selected bits of all participating axes of an array of $M=T/r$ polynomial records at a common offset in consecutive $K$-bit chunks, a forward synthetic transform (exact counterpart $LBF_{\boldsymbol t}^-$) and its opposite (exact counterpart $F_{\boldsymbol t}^+B^{-1}L^{-1}$) have error less than $\sqrt2\ell\,2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.
      - How: Move $O(dK)$ selected slots to a prefix one by one, exchange $Dq-1$ chunks of width $K$ by the chunk-interchange procedure to bring equal-offset chunks together, then run $\ell$ rounds, each a simultaneous layer, plus $\le K$ individual rounds on the prefix, and add errors one truncation per round.
      - Why (recoverable from the sources): Each round needs its $D$ selected bits in consecutive chunks at the same offset, so that the simultaneous butterfly layer applies; this fixes the layout, and its cost is that of the moves, of the individual prefix rounds, and of $\ell$ layers.
  - Normalized cyclic convolution over the polynomial ring $\mathbb C[y]/(y^r+1)$ on the remaining $d-1$ axes is computed from two forward synthetic transforms in retained order, $M$ pointwise polynomial products and the opposite transform, in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ time with error less than $\sqrt2\,M(3\ell+1)2^{-p}$. (`ring-convolution`)
    - How: Convolve by transform, pointwise product, inverse transform, using the established $O(N\log N)$ multiplier as an ordinary subroutine for the polynomial products via signed Kronecker substitution, and keep the transforms' frequency order between the forward and opposite passes.
    - Why (stated by the sources): Pointwise multiplication commutes with applying the same record permutation to both operands, so the product can be formed in the retained order and handed directly to the opposite procedure.
    - For disk-grid polynomials $f,g\in\mathcal R_r$ the exact Gaussian-integer numerators of $fg$, and then $Q_p(fg/r)$, are computed in $O(rp\log(rp))$ time using four integer products by the established multiplier at packing base $B_0=2^{4p}$. (`signed-packing`)
      - How: Use signed Kronecker substitution: evaluate the integer-coefficient polynomials at $B_0=2^{4p}$ to signed integers of $4pr$ bits, multiply the four pairs (real/imaginary parts), recover coefficients by centered residues modulo $B_0$ with a carry, and reduce modulo $y^r+1$.
      - Why (recoverable from the sources): The ordinary polynomial product has coefficients of size at most $r2^{2p}<2^{3p}<B_0/2$, so evaluating at $B_0=2^{4p}$ keeps coefficient blocks separated and each is the unique centered residue modulo $B_0$ once lower blocks are removed.
    - Normalized convolution $\mathcal M_r(f,g)=f*g/(rM)=f*g/T$ on arrays over $\mathcal R_r$ is approximated with error less than $\sqrt2\,M(3\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ time.
      - How: Do both forward transforms keeping their common $LB$ order, multiply the $M$ pairs of polynomial records pointwise by signed packing, apply the opposite transform to that order, and scale exactly by $M$; check the normalization from $F^-(f*g)=M(F^-f)(F^-g)$ and add the errors of the three transforms and one truncation.
      - Why (recoverable from the sources): Pointwise multiplication commutes with a record permutation applied to both operands, so the permuted order can be kept between the forward and opposite transforms; exact scaling by the power of two $M$ then restores the normalization.
  - The Fourier transforms of pairwise coprime prime lengths $s_i$ that the integer product needs are computed through power-of-two lengths $t_i$ by Gaussian resampling and Bluestein chirps, with the source and target coordinate permutations left inside the transform identities, so that none is executed as a sort. (`retained-permutations`)
    - How: Retain both permutations of Gaussian resampling in the transform formula: the target permutation $Q$ is absorbed by the chirp convolution, and the source permutation $R$ cancels across the two forward transforms, their pointwise product and the opposite transform.
    - Striking feature: No coordinate permutation is ever executed: the source permutation $R$ appears on both forward transforms and the opposite one and cancels, and the target permutation $Q$ is absorbed by the chirp convolution.
    - Why (stated by the sources): The usual implementation of Gaussian resampling sorts twice on each coordinate; keeping the permutations in the formula avoids the sorts, which would cost $\Theta(tp\log t)$ per line.
    - For coprime $s<t$ with $\theta=t/s-1>p/\alpha^4$ and permutations $(P_su)_j=u_{tj}$, $(P_tv)_k=v_{-sk}$ there are linear contractions $A$, $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computed with error less than $p^2$ in time $O(tp^{3/2+\delta}\alpha)$ without executing $P_s$ or $P_t$. (`gaussian-resampling`)
      - How: Use the two Gaussian resampling maps $\mathsf S$, $\mathsf T$ of Harvey and van der Hoeven with $\mathsf TP_sF_s=P_tF_t\mathsf S$ and $N=C\mathsf T\mathsf D\approx I$, invert $N$ by a Neumann series, and normalise so that $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$ are contractions.
      - Why (stated by the sources): The Fourier transform of prime length $s$ must be expressed through transforms of power-of-two length $t$; Gaussian resampling does this approximately, and the transform identity can hold exactly once the resampling is inverted through a convergent Neumann series.
      - The three ordered numerical maps $\widetilde{\mathsf S}'$, $\widetilde{\mathsf J}'$, $\widetilde{\mathsf D}'$ have errors $16p$, $3p^2/4$, $4$ and times $O(tp^{3/2+\delta}\alpha)$, $O(tp^{3/2+\delta}\alpha)$, $O(tp^{1+\delta})$.
        - How: Quote the guarantees of the cited Gaussian-resampling algorithms (Harvey and van der Hoeven's Lemmas 4.8, 4.9, 4.12) row by row and compose them with the exact selection $C$.
        - Why (recoverable from the sources): Each of the three maps has its own error and cost; the tape cost of the whole resampling is dominated by the first two, and the errors add by contraction.
    - Applied one coordinate line at a time to a padded box of $T=\prod_it_i$ entries, with $\gamma=2d\alpha^2$, $R F_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$, both $\mathcal A$ and $\mathcal B_0$ are contractions with error less than $dp^2$, computed in $O(dTp^{3/2+\delta}\alpha)$ plus $O(Tp\,d^2(1+\ell^\tau))$ for exposing lines.
      - How: Tensor the one-dimensional identity over the $d$ axes, process axes one at a time keeping the padded box and zero lines, and expose each axis as the innermost field by adjacent axis interchanges using the chunk-interchange procedure.
      - Why (recoverable from the sources): A tensor product of contractions is applied by applying each factor along its own axis; exposing an axis costs $O(d)$ adjacent interchanges, each costing $O(Tp(1+\ell^\tau))$ by the power saving.
    - For even $t_i$ and the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$ one has $QF_{\boldsymbol t}u=\overline a\cdot\bigl(a*(\overline a\cdot u)\bigr)/T$, so the target permutation $Q$ is absorbed into a cyclic convolution of length $T$ and never executed. (`chirp`)
      - How: Expand the coefficient of $u_{\boldsymbol k}$ in the right side using $(j-k)^2=j^2-2jk+k^2$, so that the three chirp phases combine to $\exp(2\pi i\sum s_ij_ik_i/t_i)$, which is the coefficient of $QF_{\boldsymbol t}$ because $Q$ reads frequency $-s_ij_i$.
      - Why (recoverable from the sources): Bluestein's identity turns a (permuted) discrete Fourier transform into pointwise phases around a convolution; the phases depend on $s_ij_i^2/t_i$ and the permutation $Q$ merely changes which frequency is read, which the identity already includes.
    - The retained source permutation cancels: $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=u*v/S^2$ with $S=\prod_is_i$, so no source permutation is executed across the two forward transforms, their pointwise product and the opposite transform.
      - How: Show $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$ by substituting $h=ck$ in the Fourier sum (each $t_i$ is a unit modulo $s_i$), use that permutations commute with pointwise products, then apply the convolution rule and $F^+F=I/S$.
      - Why (recoverable from the sources): A dilation by a unit permutes the frequencies of the Fourier sum, so the permutation $R$ attached to each forward transform is undone by the permutation inside the opposite transform; pointwise products commute with coordinate permutations.
  - The exact $2n$-bit product of the two inputs is obtained from the radix-digit convolution by the chain: radix digits, Chinese-remainder address map to a product of prime cyclic axes, two forward source transforms (resampling and chirps), pointwise product, opposite transform, rescaling, rounding, and carry propagation, with total error below $1/2$. (`multiplication-algorithm`)
    - How: Reduce the integer product to a cyclic convolution of $S$ short coefficients and compute it through the chain of reductions (digits, CRT address map, Gaussian resampling with chirps, twist to the polynomial ring, synthetic-transform convolution); recover exact integers because the accumulated error is below $1/2$.
    - Why (stated by the sources): Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.
    - Fixed rational exponents and sizes make every hypothesis of the lemmas hold: $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$, axis lengths $t_i\in\{r/2,r\}$ with $\prod t_i=T$, $t_d=r$, and distinct odd primes $s_i\in((1-2\eta)t_i,(1-\eta)t_i]$. (`parameter-choice`)
      - How: Fix concrete rational exponents with explicit slack and verify the inequalities among them by integer comparisons; choose the sizes so that $Tp=\Theta(n)$ and every needed asymptotic comparison holds with fixed constants; find the primes by the prime-interval lemma and a deterministic search of cost $n^{o(1)}$.
      - Why (stated by the sources): The layer, transform, chirp and resampling lemmas each impose inequalities among the exponents ($\tau,\sigma,\lambda,\lambda',c,\epsilon,\delta$) and the sizes; these are constants deliberately conservative so that all can be checked by exact comparisons, and the primes must lie close below the powers of two so that $S$ fills a fixed fraction of the padded box while $t_i/s_i$ leaves enough separation.
    - Writing the two inputs in radix $2^b$ with $q=\lceil n/b\rceil$ digits each, the product polynomial has degree at most $2q-2<2n/b\le T/2<S$, so convolution modulo $x^S-1$ has no wraparound, and every coefficient $c_j\le q(2^b-1)^2<2^{3b}$. (`radix-digit-reduction`)
      - How: Count degrees and bound the coefficients: a product of two polynomials with $q$ digits below $2^b$ has degree $2q-2$ and coefficients that are sums of at most $q$ products.
      - Why (recoverable from the sources): Splitting an integer into radix digits turns the product into a convolution of short integer coefficients; the cyclic convolution of length $S$ equals the ordinary product as long as the degree stays below $S$, and the coefficient bound shows rounding errors below 1/2 will identify them.
    - The Chinese-remainder map $\Phi:\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$, $x\mapsto\prod_ix_i^{\mu_i}$, is an isomorphism preserving cyclic convolution, and it (with its inverse and padding) is implemented by triangular controlled shifts in $O(Tp\,d^2(1+\ell^\tau))$ time. (`crt-map`)
      - How: Choose the exponents $\mu_i=P_i^{-1}\bmod s_i$ so that the coordinate of a coefficient index in axis $i$ is $a_i+\mu_i\sum_{j<i}a_jP_j$, i.e. it depends only on lower-index digits: a triangular system implemented as prefix-controlled cyclic shifts in descending axis order after reversing the axis order.
      - Why (recoverable from the sources): A triangular dependence means each target axis is updated from controls that precede it on tape, so each update is a controlled cyclic shift of linear cost (Lemma on controlled shifts); the only expensive part is reordering the axes, which uses the fast chunk interchange.
    - With $\zeta=e^{\pi i/r}$ the map $\Theta:\mathbb C[x_d]/(x_d^r-1)\to\mathcal R_r$, $x_d\mapsto\zeta y$, is an isomorphism multiplying coefficient $k$ by $\zeta^k$; hence normalized complex cyclic convolution is $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=f*g/T$. (`phase-twist`)
      - How: Twist the last cyclic coordinate by powers of $\zeta$, so that the negative wrap of $y^r=-1$ cancels against the factor $\zeta^r=-1$; untwist afterwards.
      - Why (recoverable from the sources): The last cyclic axis of length $r$ must become the polynomial coordinate of $\mathbb C[y]/(y^r+1)$; since $(\zeta y)^r=(-1)(-1)=1$, a diagonal change of basis turns the cyclic wrap into a negative wrap, and the factor $\zeta^{k+l}$ undoes the sign.
    - The computed chirp transform $\widetilde{\mathscr C}$ and the source transform $\widetilde{\mathscr F}$ (apply $\mathcal A$, the chirp transform, $\mathcal B_0$, then multiply by $2^\gamma$) have exact counterparts $QF_{\boldsymbol t}$ and $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.
      - How: Evaluate $QF_{\boldsymbol t}$ by the chirp identity: pointwise phase, complex convolution with the chirp, pointwise phase; compose with the Gaussian maps and the exact scale $2^\gamma$.
      - Why (recoverable from the sources): The middle factor of the resampling identity is a permuted Fourier transform, which the chirp identity turns into one cyclic convolution of power-of-two length, available from the twisted ring convolution.
    - The algorithm: read radix digits, apply $\Phi$, compute the source transforms $\widetilde{\mathscr F}(u)$, $\widetilde{\mathscr F}(v)$, multiply pointwise, apply the opposite transform, rescale by $S$ and $2^{2b+4}S$, round, undo $\Phi$ and propagate carries to output exactly $2n$ bits.
      - How: Write each radix digit $a_j$ as the exact grid value $a_j2^{-b-2}$ so inputs have norm below $1/4$, and run six explicit operations whose exact counterpart is $(u*v)/S^2$ scaled back to the integer coefficient convolution.
      - Why (recoverable from the sources): The scale factors undo different normalizations: the first $S$ and the second $S$ and $2^{2b+4}$ restore the factors $1/S^2$ from the three transforms and $2^{-2b-4}$ from the two input scalings.
    - The error on the recovered integer coefficients is below $1/2$, so rounding gives the exact integer coefficients, and carry propagation yields the exact binary product. (`precision-recovery`)
      - How: Track errors in units of $h_p=2^{-p}$ through every contraction and bilinear map (each computed array also stays in the disk), obtain $E_{\rm ring}<5TL$, chirp error $<8TLh_p$, source error $E_s=9\cdot2^\gamma TL$, product error $(2E_s+2)$, opposite error $(3E_s+2)$, scaled error $E_w<28\cdot2^\gamma T^2L$, and finally the coefficient error $<448b\,2^{-3b/4}<1/2$.
      - Why (recoverable from the sources): Each normalized transform and product is a contraction, so errors add rather than multiply; the final multiplication by the factors $2^{2b+4}S$ amplifies the error by at most $2^{2b+4}S\cdot2^{-p}$ which stays small only because $p=6b$ leaves $4b$ spare bits.
  - The total time of the machine is $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$: after dividing each cost by $V=Tp=\Theta(n)$ the dominant terms are powers of $p$ below one, with minimum margin $2^{-181}=2\kappa$. (`cost-accounting`)
    - How: Divide each cost by the volume, list the dominant terms with their powers of $p$, compute their margins below one from the fixed rational parameters, justify each row from the lemmas, show setup is negligible, and add.
    - Striking feature: The final exponent is only $2^{-182}$ below one: it is set by the least of seven margins, the chunk-exchange row $g_2=\epsilon c(1-\tau)=2^{-181}$.
    - Why (stated by the sources): Taking the margin to be twice $\kappa$ leaves room for any remaining fixed power of $\log p$.
    - Dividing each cost by $V=Tp=\Theta(n)$, seven operations dominate, each a power of $p$ with exponent $1-g_i$ for a margin $g_i>0$ listed row by row.
      - How: Tabulate the normalized cost of each operation of the algorithm and read off its power of $p$ from the sizes $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$, $\alpha=\Theta(p^{1/4+\epsilon/2})$; the last two rows (final scaling, input and output) are absorbed.
      - Why (recoverable from the sources): A common unit of volume $V=Tp$ makes the costs comparable, and writing each as a power of $p$ converts the final bound into a comparison of seven exponents with $1$.
    - The seven margins are $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$, so the minimum is $2^{-181}=2\kappa$.
      - How: Substitute the fixed rational parameters $\epsilon=2^{-75}$, $c=2^{-56}$, $1-\tau=2^{-50}$, $1-\lambda'=2^{-54}$, $\delta=1/16$ into the seven margin expressions.
      - Striking feature: The minimum margin $2^{-181}=2\kappa$ comes from the single row of chunk exchanges, where the saving is the product of three tiny exponents $\epsilon c(1-\tau)=2^{-75}2^{-56}2^{-50}$; so $\kappa=2^{-182}$ is half of it.
      - Why (stated by the sources): Taking the margin to be twice $\kappa$ leaves room for any fixed power of $\log p$ to be absorbed.
    - Each of the seven normalized costs is justified from the lemmas: the layout exchanges cost $O(pK^{\tau-1})$, axis moves $O(d^2(1+\ell^\tau))$, Gaussian lines $O(dp^{1/2+\delta}\alpha)$, chirps $O(dp^{1+\delta})$ per entry, and polynomial products $O(Tp\log(rp))$ in total.
      - How: Combine the costs of the lemmas: $O(p/K)$ exchanges each costing $O(VK^\tau)$, $O(d^2)$ axis moves each $O(V(1+\ell^\tau))$, at most $T/t_i$ lines per axis, per-entry chirp arithmetic, and $T/r$ ring products of $O(rp)$ bits each.
      - Why (recoverable from the sources): Each row is the number of repetitions of a primitive times the cost per repetition given by the corresponding lemma, divided by the volume.
    - Setup at recursion nodes, exceptional-address repair, global setup and prime search together cost $o(V)$.
      - How: Separate per-visit setup from per-record work: the recursions have constant branching and depth $O(\log p)$ with polynomially many visits ($\le p^A$ visits each of cost $p^C$), per-record or per-line polynomial work is $o(Tp)$ because $r$ exceeds every power of $p$, and exceptional streams are a fraction $O(d2^{-K})$ of the volume.
      - Why (recoverable from the sources): Polynomial work in $p$ per node, record or line is negligible against $\Theta(Tp)$ stored bits because $r$ and $T/r$ grow faster than any fixed power of $p$ and $K\to\infty$ makes the exceptional fraction $d2^{-K}$ tiny.
    - Each of the seven displayed powers is at most $1-2\kappa$, any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$, and with schoolbook multiplication below a fixed cutoff the single machine runs in $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.
      - How: Combine the margin bound $\min g_i=2\kappa$ with the absorption of logarithmic factors into one margin $\kappa$, and absorb finitely many small lengths into the constant.
      - Why (recoverable from the sources): A margin of $2\kappa$ leaves a factor $p^\kappa$ to spare for fixed powers of $\log p$, so the total exponent is at most $1-\kappa$.

The page bodies are in `exegenius/pages/<id>.md`.

## Sources

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Goal": {
      "additionalProperties": false,
      "properties": {
        "key_points": {
          "description": "Short checkable statements a full answer must make, each with its role.",
          "items": {
            "$ref": "#/$defs/KeyPoint"
          },
          "type": "array"
        },
        "kind": {
          "$ref": "#/$defs/GoalKind"
        },
        "pages": {
          "description": "Ids of the pages needed to answer.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "question": {
          "type": "string"
        }
      },
      "required": [
        "question",
        "kind",
        "key_points",
        "pages"
      ],
      "type": "object"
    },
    "GoalKind": {
      "description": "What a goal question asks of the reader.",
      "oneOf": [
        {
          "const": "meaning",
          "description": "What a symbol or term denotes: \"What does r count?\"",
          "type": "string"
        },
        {
          "const": "status",
          "description": "What part a statement plays: a definition, an assumption, a condition, a claim.",
          "type": "string"
        },
        {
          "const": "justification",
          "description": "Why a step or claim holds.",
          "type": "string"
        },
        {
          "const": "summary",
          "description": "Summarise an argument or construction in a few sentences.",
          "type": "string"
        },
        {
          "const": "structure",
          "description": "How parts of the argument relate: what one step contributes to another.",
          "type": "string"
        },
        {
          "const": "transfer",
          "description": "Apply or extend: what changes in a new case, what a result implies.",
          "type": "string"
        },
        {
          "const": "example",
          "description": "Work a small example through.",
          "type": "string"
        },
        {
          "const": "motivation",
          "description": "Why the argument takes this route: why this method or construction.",
          "type": "string"
        },
        {
          "const": "non-routine",
          "description": "Where the argument stops being routine.",
          "type": "string"
        },
        {
          "const": "obvious-fails",
          "description": "Why the obvious approach fails.",
          "type": "string"
        }
      ]
    },
    "KeyPoint": {
      "additionalProperties": false,
      "description": "A short checkable statement a full answer must make.",
      "properties": {
        "point": {
          "type": "string"
        },
        "role": {
          "$ref": "#/$defs/Role"
        }
      },
      "required": [
        "point",
        "role"
      ],
      "type": "object"
    },
    "Role": {
      "description": "The part a key point plays in a full answer.",
      "oneOf": [
        {
          "const": "claim",
          "description": "What is asserted.",
          "type": "string"
        },
        {
          "const": "reason",
          "description": "Why it holds.",
          "type": "string"
        },
        {
          "const": "conclusion",
          "description": "What follows from it.",
          "type": "string"
        },
        {
          "const": "background",
          "description": "What it rests on.",
          "type": "string"
        }
      ]
    }
  },
  "additionalProperties": false,
  "properties": {
    "goals": {
      "items": {
        "$ref": "#/$defs/Goal"
      },
      "type": "array"
    }
  },
  "required": [
    "goals"
  ],
  "title": "GoalsAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0317-goals.answer.json`, then run `exegenius submit 0317-goals` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0317-goals`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
