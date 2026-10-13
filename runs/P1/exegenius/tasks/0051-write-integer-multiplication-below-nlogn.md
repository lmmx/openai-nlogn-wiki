# exegenius task 0051-write-integer-multiplication-below-nlogn

Project directory: `/home/user/openai-nlogn-wiki/runs/P1` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, functions, induction, summations, recurrences, basic number theory and elementary group/ring/field vocabulary), an algorithms course (recursion, divide and conquer, schoolbook and Karatsuba multiplication, the FFT at the level of the divide-and-conquer recursion, solving recurrences), single-variable calculus (limits, exponentials, logarithms) and one course in linear algebra and complex numbers. They know Turing machines and big-O at an introductory level, but have not studied fast integer multiplication beyond Karatsuba, Schönhage-Strassen or Harvey-van der Hoeven, numerical error analysis, bilinear forms over finite fields, matrix factorizations such as Bruhat decompositions, or tape-level algorithm engineering.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Matrices, rank, subspaces and orthogonality
- Modular arithmetic and the Chinese remainder theorem
- Convolution and cyclic convolution
- Discrete Fourier transform and the convolution theorem
- Butterfly and FFT recursion
- Multidimensional transform (tensor product)
- The n log n optimality conjecture
  - $n$ (input length): The number of bits in each of the two integers being multiplied.
- The established O(n log n) multiplier as a subroutine
- Fixed-point disk grid and truncation
- Contractions and error accumulation
- Exact Gaussian dyadic arithmetic and guard bits
- Arrays, addresses, rows and volume on tape
- Elementary stream operations
- Controlled shifts
- Row splitting among roles with padding
- Depth-first recursion on fixed tapes
- Linear network with roles and restored scratch
- Three-subset gather, scatter and side-wire gadget
- Frames and edge operators
- Nested subspace labels and rank deficit
- Address shear interface
- Lower triangular factorization and matrix shear cost
- Recursive power saving
- Fast address-chunk interchange
- Butterfly kernel H₀ and phase kernel C
  - $H_0$ (butterfly kernel): The two-point map (u,v) ↦ ((u+v)/2,(u−v)/2) acting on a pair of complex values.
  - $C$ (phase kernel): The 2×2 matrix aI+bX with a=(1+i)/2, b=(1−i)/2 that conjugates to the butterfly via phases.
- Binary phase interface
- Packed selected-bit addition
- Simultaneous butterfly layer
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal variable whose powers act as roots of unity in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Retained frequency order
- Transform layout for parallel layers
- Signed packing (Kronecker substitution)
- Ring convolution from the retained transform layout
- Phase twist from cyclic to negacyclic
- Gaussian resampling
- Resampling with the permutations left in the transform
- Bluestein chirp identity
- Source permutation cancellation
- Chinese-remainder address map
- Integer product as radix-digit convolution
- Parameter choices and padded box
- Prime source lengths
- Source transform pipeline
- Exact recovery by scaling, rounding and carries
- The multiplication algorithm
- Cost analysis and the exponent κ
  - $\kappa$ (power saving exponent): The fixed constant 2^{-182} by which the logarithmic factor is reduced.
- Binary representation and schoolbook arithmetic (also: binary numerals, bits, radix representation, base-b digits, carry propagation, schoolbook addition, schoolbook multiplication, most significant bit, leading zeroes)
- Floor, ceiling and logarithms (also: floor function, ceiling function, lg, log base 2, binary logarithm, iterated logarithm, log*, rounding to nearest integer)
- Exponentials and elementary inequalities (also: exp, e^x, 1+x <= e^x, limits, powers of two, real exponents, fractional powers)
- Summation, telescoping sums and geometric series (also: sigma notation, telescoping, geometric sum, partial sums)
- Recurrences and the recursion tree (also: recurrence relation, solving recurrences, master theorem, divide and conquer, recursive cost, unrolling a recurrence)
- Karatsuba and classical multiplication algorithms (also: Karatsuba multiplication, Toom-Cook, Schönhage-Strassen, O(n^2) multiplication, O(n^{log_2 3}))
- Recursion, call stack and subroutines (also: recursive call, call stack, stack data structure, program counter, subroutine, black-box call)
- Sets, functions, bijections and permutations (also: [n], index set, Cartesian product, bijection, permutation, inverse function, composition of functions, injective, surjective, partial permutation)
- Mathematical induction and proof techniques (also: proof by induction, induction on the number of steps, proof by contradiction, invariant, loop invariant, contrapositive)
- Prime numbers and trial division (also: primes, prime, odd prime, trial division, primality testing by division, coprime integers, relatively prime, prime factorization)
- Groups, rings and fields (also: algebraic structure, ring, field, group, finite field, F_2, GF(2), ring of residues Z/qZ, units of a ring, quotient ring, cyclic group)
- XOR and arithmetic over F_2 (also: exclusive or, bitwise XOR, addition mod 2, parity, bit flip, bitwise operations, bit shift)
- Special matrices and matrix algebra (also: identity matrix, diagonal matrix, permutation matrix, invertible matrix, matrix inverse, transpose, matrix product, standard basis vector, lower triangular matrix, block matrix, matrix-vector product)
- Triangle inequality and norm bounds (also: triangle inequality, modulus of a sum, |z+w| <= |z|+|w|, maximum norm, sup norm, absolute error, error bound)
- Rational numbers and dyadic fractions (also: rational numbers, fractions, dyadic rational, denominator a power of 2, numerator and denominator, lowest terms)
- Deterministic algorithms and worst-case time (also: deterministic machine, worst-case running time, time complexity, fixed finite alphabet, linear time scan)
- Entrywise operations on arrays and vectors (also: pointwise product, componentwise product, Hadamard product, vector of coefficients, coefficient list, array indexing, multi-index)

## This page

Concept: Integer multiplication in O(n (lg n)^(1−κ)) time
Gloss: The main theorem: one deterministic fixed-alphabet, fixed-tape Turing machine multiplies n-bit integers in O(n(lg n)^{1−κ}) worst-case time, refuting the n log n conjecture, via synthetic transforms accelerated by the interchange and butterfly procedures.
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits in each of the two integers being multiplied.
- $\kappa$ (power saving exponent): The fixed constant 2^{-182} by which the logarithmic factor is reduced.

## This page in the argument

The step: One deterministic fixed-alphabet, fixed-tape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$.
How: Split the integers into radix digits, compute the digit convolution with synthetic transforms whose data movement and butterfly arithmetic are accelerated by two new tape procedures, and recover the exact product by rounding and carries.
Why: Multiplication reduces to convolution of short digit lists, which Fourier-type transforms compute, but their $\Theta(\log n)$ levels each scanning $\Theta(n)$ bits already cost $\Theta(n\log n)$, so the transforms themselves must be made cheaper. (the sources say so: "Splitting the inputs into radix digits reduces multiplication to" (paper))
Striking feature: The logarithmic factor is beaten by a strict power, $(\lg n)^{-\kappa}$, although the exponent $\kappa=2^{-182}$ is astronomically small. (explain why it holds, from the method)

Its sub-steps, in order:

- Two tape procedures exist: interchanging two $u$-bit address chunks of an array of volume $V$ in $O(Vu^\tau)$ time with $\tau<1$, and applying $H_0$ at one bit position in each of $D\le d$ address chunks in $O(Vd^{\lambda'})$ time with $\lambda'<1$.
- Normalized cyclic convolution over $\mathbb C[y]/(y^r+1)$ on power-of-two axes is computed from two forward synthetic transforms, pointwise ring products by signed packing and the opposite transform, with error below $\sqrt2\,M(3\ell+1)2^{-p}$.
- A Fourier transform on pairwise coprime lengths $s_i$ is expressed through transforms on power-of-two lengths $t_i$ in which the coordinate permutations are retained, the middle transform becomes a cyclic convolution by a chirp, and the retained source permutation cancels in a convolution.
- Choosing the parameters $b,p,d,T,S$ compatibly, the radix-digit convolution is mapped onto prime-length axes, evaluated by source transforms, multiplied pointwise and inverted, and the exact $2n$-bit product is recovered by scaling, rounding and carries within time $O(n(\lg n)^{1-\kappa})$.

## Steps this page derives

The argument gives this page these sub-steps of its step (T1, T2, T3, T4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**T1**: Two tape procedures exist: interchanging two $u$-bit address chunks of an array of volume $V$ in $O(Vu^\tau)$ time with $\tau<1$, and applying $H_0$ at one bit position in each of $D\le d$ address chunks in $O(Vd^{\lambda'})$ time with $\lambda'<1$.
How: Build one fixed linear network per procedure that exchanges two banks of values with signs while restoring all scratch wires, label it with nested subspaces so that the sum $s$ of edge ranks is below $Wm$, and recurse on the edges.
- S1: Linear-time scans on arrays stored in lexicographic order on a fixed number of tapes (permuting or moving digits, splitting and merging streams, controlled cyclic shifts of a later field) supply the elementary operations of both tape procedures.
  How: Fix the array and address conventions, then prove the few linear-time scans (digit moves, stream splits and merges, controlled shifts) that every later procedure is built from.
- S2: Two fixed linear networks, one over bits and one over Gaussian dyadic values, exchange two banks of values with prescribed signs and restore every scratch wire, and carry subspace labels whose total dimension change $s$ is strictly less than $Wm$.
  How: Build a scalar network from a three-subset gadget, lift it to arrays through common frames at each gate, and choose nested subspace labels so that the frame changes on the edges have small total rank.

**T2**: Normalized cyclic convolution over $\mathbb C[y]/(y^r+1)$ on power-of-two axes is computed from two forward synthetic transforms, pointwise ring products by signed packing and the opposite transform, with error below $\sqrt2\,M(3\ell+1)2^{-p}$.
How: Transform over the ring $\mathbb C[y]/(y^r+1)$, whose roots of unity are powers of $y$, with simultaneous butterfly layers on a suitable tape layout; keep the frequency order through the pointwise product; multiply the ring elements by signed packing and the established multiplier; then apply the opposite transform.

**T3**: A Fourier transform on pairwise coprime lengths $s_i$ is expressed through transforms on power-of-two lengths $t_i$ in which the coordinate permutations are retained, the middle transform becomes a cyclic convolution by a chirp, and the retained source permutation cancels in a convolution.
How: Replace the prime-length transform by Gaussian resampling to power-of-two lengths with the permutations left in the identity, turn the middle transform into a convolution by Bluestein's chirp, and cancel the retained source permutation.

**T4**: Choosing the parameters $b,p,d,T,S$ compatibly, the radix-digit convolution is mapped onto prime-length axes, evaluated by source transforms, multiplied pointwise and inverted, and the exact $2n$-bit product is recovered by scaling, rounding and carries within time $O(n(\lg n)^{1-\kappa})$.
How: Fix one compatible set of rational exponents and sizes, reduce the integer product to a convolution on prime axes, evaluate the three transforms with the source transform, then verify the error bound for rounding and total the cost.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.1 (on [Arrays, addresses, rows and volume on tape](tape-address-arrays.md)): An array with address set $[a_1]\times\cdots\times[a_t]$ is stored in lexicographic order with the address implicit in position; its logical volume $V$ is the number of stored data bits, and a row is the complete suffix block at a fixed prefix and row index.
- S1.2 (on [Elementary stream operations](elementary-stream-operations.md)): Fixed digit permutations, moving one digit, splitting on a digit and merging, and splitting whole rows cyclically into $W$ streams each take $O(V)$ steps on a fixed number of tapes.
- S1.3 (on [Controlled shifts](controlled-shifts.md)): Updating a target field by an offset $a$ computed from earlier fields, $y\mapsto y+a \pmod{q^b}$, or multiplying it by a rational unit, takes $O(V)$ time.
- S2.1 (on [Linear network with roles and restored scratch](linear-network-roles.md)): Three stages of an invocation that adds a source bank $x$ into a target bank $y$ send $(X_a,Y_a)\mapsto(-Y_a,X_a)$ and restore every scratch wire, for arbitrary scratch contents.
- S2.2 (on [Frames and edge operators](frames.md)): Giving all wires at a gate the same invertible operator $D_v$ on their address-indexed arrays, and applying $D_vD_u^{-1}$ on each edge, makes the net operator on each routed role equal to $D_{\rm sink}D_{\rm source}^{-1}$, because a common frame commutes with pointwise linear gates.
- S2.3 (on [Nested subspace labels and rank deficit](subspace-labels-rank-deficit.md)): Nested nondegenerate subspaces of an $m$-dimensional space, built from tensor products of three-element subset lines, label the gates and terminals so that every edge joins comparable labels and the total dimension change $s$ over all edges is strictly less than $Wm$, where $W$ is the wire count.
- S2.4 (on [Address shear interface](address-shear.md)): The bit network sends its input to the role permutation and its endpoint matrices differ by $I_m$ on every input role, so its net effect on every role array is the address shear $(H,D)\mapsto(H+D,D)$, with edge matrix ranks summing to $s_{\rm b}<W_{\rm b}m$.
- S2.5 (on [Binary phase interface](binary-phase-interface.md)): In the complex network each edge's frame change is a product of translation kernels $aI+bX_v$, one per vector of an orthonormal basis of the edge residual, with $s_{\rm c}<W_{\rm c}m$ kernels in total, and telescoping gives $C^{\otimes m}$ on every role.
- S3 (on [Fast address-chunk interchange](address-chunk-interchange.md)): Two disjoint $u$-bit address chunks of an array of volume $V$ can be interchanged on a fixed number of tapes in $O(Vu^\tau)$ time, for a fixed rational $\tau<1$, with an exact permutation as final effect for arbitrary scratch contents.
- S4 (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)): A simultaneous layer applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ at bit position $\rho$ of each of $D\le d$ consecutive $K$-bit address chunks of every record runs in $O(Vd^{\lambda'})$ time with $\lambda'<1$, evaluating exactly and truncating once with error below $\sqrt2\,2^{-p}$.
- T2.1 (on [Synthetic polynomial transform](synthetic-polynomial-transform.md)): Over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ the length-$t$ transforms $F_t^\pm$ with roots $\omega_t=y^{2r/t}$ are contractions, are inverse to each other up to the factor $1/t$, and are computed by a butterfly recursion whose twiddle multiplications are signed shifts.
- T2.2 (on [Retained frequency order](frequency-order-retention.md)): The recursion writes $(F_t^-z)_j$ at slot $\operatorname{rev}_a(j)$, so the procedures $B_tF_t^-$ and $F_t^+B_t^{-1}$, with the bit reversal $B_t$ never executed, are inverse up to $1/t$ and a pointwise product can be taken between them in the stored order.
- T2.3 (on [Transform layout for parallel layers](synthetic-transform-layout.md)): A layout permutation $L$ built from single-bit moves and $O(p/K)$ exchanges of $K$-bit chunks places the selected bits of the axes at a common offset in consecutive chunks, so each transform round is one simultaneous butterfly layer and a transform costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\,\ell\,2^{-p}$.
- T2.4 (on [Signed packing (Kronecker substitution)](signed-packing.md)): Two disk-grid polynomials in $\mathcal R_r$ can be multiplied exactly, by evaluating their integer coefficient polynomials at $2^{4p}$, multiplying with the established $O(N\log N)$ multiplier and extracting centered coefficients, and the normalized product is returned in $O(rp\log(rp))$ time.
- T2.5 (on [Ring convolution from the retained transform layout](synthetic-convolution.md)): Two forward synthetic transforms in the retained $LB$ order, pointwise ring products divided by $r$, the opposite transform and an exact scaling by $M$ compute $\mathcal M_r(f,g)=(f*g)/T$ with error below $\sqrt2\,M(3\ell+1)2^{-p}$.
- T3.1 (on [Resampling with the permutations left in the transform](resampling-permutations-retained.md)): For coprime $s<t$ with $t/s-1>p/\alpha^4$ there are contractions $A$ and $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, and tensoring over $d$ axes gives $RF_{\boldsymbol s}=2^{\gamma}\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with no sorting.
- T3.2 (on [Bluestein chirp identity](bluestein-chirp.md)): For even $t_i$ and the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$, $QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}{T}$, so the target permutation $Q$ is absorbed into a cyclic convolution.
- T3.3 (on [Source permutation cancellation](permutation-cancellation.md)): The retained source permutation cancels across two forward source transforms, their pointwise product and the opposite-sign transform: $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$.
- T4.1 (on [Parameter choices and padded box](parameter-choice.md)): Put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^{\epsilon}\rfloor$, $K=\lfloor d^{c}\rfloor$, take a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$ and axis lengths $t_i\in\{r/2,r\}$ with $\prod_it_i=T$, so that $Tp=\Theta(n)$ and $d=\Theta(p^\epsilon)$.
- T4.2 (on [Prime source lengths](prime-source-lengths.md)): Distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$, $\eta=1/(4d)$, exist and are found by deterministic trial division in time $n^{o(1)}$; they give $T/2<S<T$ for $S=\prod_is_i$ and $t_i/s_i-1>\eta$ as resampling needs.
- T4.3 (on [Integer product as radix-digit convolution](integer-as-digit-convolution.md)): Writing both inputs in base $2^b$ with $q=\lceil n/b\rceil$ digits, the integer product is the convolution of the digit lists; because $2q-2<S$ padding to length $S$ causes no wraparound, and every coefficient is below $2^{3b}$.
- T4.4 (on [Chinese-remainder address map](crt-address-map.md)): The map $x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$ preserving convolution, implemented by $d$ triangular controlled shifts and axis reorders in $O(Tp\,d^2(1+\ell^\tau))$ time.
- T4.5 (on [Phase twist from cyclic to negacyclic](phase-twist.md)): Multiplying coefficient $k$ of the last cyclic axis by $\zeta^k$, $\zeta=e^{\pi i/r}$, is an isomorphism $\mathbb C[x_d]/(x_d^r-1)\to\mathbb C[y]/(y^r+1)$, so complex cyclic convolution of length $T$ is computed by ring convolution followed by the untwist.
- T4.6 (on [Source transform pipeline](source-transform.md)): The source transform applies the resampling map $A$ on each axis, the chirp transform by ring convolution, the compression $B_0$ and the scale $2^\gamma$, and approximates $RF_{\boldsymbol s}$ with error below $9\,2^{\gamma}TL\,2^{-p}$ on inputs of norm at most $.5$.
- T4.7 (on [The multiplication algorithm](multiplication-algorithm.md)): The algorithm forms the radix digits, applies the address map $\Phi$, computes two source transforms, multiplies pointwise, applies the opposite transform, rescales by $S$ and by $2^{2b+4}S$, rounds and propagates carries.
- T4.8 (on [Exact recovery by scaling, rounding and carries](exact-recovery.md)): Rescaling by $S$ and $2^{2b+4}$ undoes the normalizations, the coefficient error is below $448\,b\,2^{-3b/4}<1/2$, so rounding gives the exact integer coefficients $c_j<2^{3b}$ and radix-$2^b$ carries give the $2n$-bit product.
- T4.9 (on [Cost analysis and the exponent κ](cost-analysis.md)): Each of the seven normalized cost terms, relative to $Tp$, is at most $p^{1-2\kappa}$, with smallest margin $2^{-181}=2\kappa$, so the total is $O(n(\lg n)^{1-\kappa})$ for $\kappa=2^{-182}$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The multiplication algorithm](multiplication-algorithm.md): The six steps: form radix digits, apply the address map Φ, compute two source transforms, multiply pointwise, apply the opposite transform, rescale, round and carry.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* The multiplication algorithm
- [Cost analysis and the exponent κ](cost-analysis.md): The table of normalized costs per Tp, each at most p^{1−2κ}, with the smallest margin 2^{−181}=2κ, giving total O(n (lg n)^{1−κ}) for κ=2^{−182}.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Cost analysis and the exponent κ
- [The n log n optimality conjecture](nlogn-conjecture.md): Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of multiplication cost on multitape Turing machines; the paper refutes any eventual Ω(n log n) lower bound for a fixed machine.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* The n log n optimality conjecture

## Other pages you may link to

- [Convolution and cyclic convolution](convolution.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-y-r-plus-1.md)
- [The established O(n log n) multiplier as a subroutine](nlogn-multiplier-subroutine.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Arrays, addresses, rows and volume on tape](tape-address-arrays.md)
- [Elementary stream operations](elementary-stream-operations.md)
- [Row splitting among roles with padding](row-splitting.md)
- [Modular arithmetic and the Chinese remainder theorem](modular-arithmetic.md)
- [Controlled shifts](controlled-shifts.md)
- [Matrices, rank, subspaces and orthogonality](linear-algebra-basics.md)
- [Linear network with roles and restored scratch](linear-network-roles.md)
- [Frames and edge operators](frames.md)
- [Three-subset gather, scatter and side-wire gadget](triple-subset-gadget.md)
- [Nested subspace labels and rank deficit](subspace-labels-rank-deficit.md)
- [Address shear interface](address-shear.md)
- [Lower triangular factorization and matrix shear cost](triangular-factorization.md)
- [Depth-first recursion on fixed tapes](fixed-tape-recursion.md)
- [Recursive power saving](recursive-power-saving.md)
- [Fast address-chunk interchange](address-chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Fixed-point disk grid and truncation](fixed-point-disk-grid.md)
- [Exact Gaussian dyadic arithmetic and guard bits](guard-bits-dyadic.md)
- [Phase twist from cyclic to negacyclic](phase-twist.md)
- [Discrete Fourier transform and the convolution theorem](dft.md)
- [Multidimensional transform (tensor product)](multidimensional-transform.md)
- [Butterfly and FFT recursion](fft-butterfly.md)
- [Synthetic polynomial transform](synthetic-polynomial-transform.md)
- [Butterfly kernel H₀ and phase kernel C](butterfly-and-phase-kernels.md)
- [Retained frequency order](frequency-order-retention.md)
- [Binary phase interface](binary-phase-interface.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout for parallel layers](synthetic-transform-layout.md)
- [Contractions and error accumulation](contractions-and-error.md)
- [Ring convolution from the retained transform layout](synthetic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling with the permutations left in the transform](resampling-permutations-retained.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Source permutation cancellation](permutation-cancellation.md)
- [Parameter choices and padded box](parameter-choice.md)
- [Prime source lengths](prime-source-lengths.md)
- [Integer product as radix-digit convolution](integer-as-digit-convolution.md)
- [Exact recovery by scaling, rounding and carries](exact-recovery.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Source transform pipeline](source-transform.md)

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers
in $O(n(\lg n)^{1-\kappa})$ worst-case time" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}


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

Write the body to `exegenius/tasks/0051-write-integer-multiplication-below-nlogn.answer.md` and the JSON to `exegenius/tasks/0051-write-integer-multiplication-below-nlogn.answer.json`, then run `exegenius submit 0051-write-integer-multiplication-below-nlogn` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0051-write-integer-multiplication-below-nlogn`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
