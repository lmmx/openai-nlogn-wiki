# exegenius task 0034-write-transform-layout

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
- Synthetic polynomial transform
- Decimation-in-frequency butterflies and bit-reversed frequency order
- Bluestein chirp identity
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

Concept: Transform layout and cost
Gloss: A positional permutation moves selected bits of the d−1 axes to a common offset in K-bit chunks so each transform round is one simultaneous layer, giving a forward and opposite synthetic transform costing O(T p [dK + p K^{τ−1} + ℓ d^{λ'}]).

## This page in the argument

The step: A positional permutation moves selected bits of the $d-1$ axes to a common offset in $K$-bit chunks so that each transform round is one simultaneous layer, giving a forward and an opposite synthetic transform each costing $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.
How: Run radix-two decimation-in-frequency rounds over the negacyclic ring, group the rounds of all axes into one parallel butterfly plus one monomial, and lay out the bits so that every round is a simultaneous layer.
Why: Each round pairs entries differing in one address bit on every axis, and the simultaneous layer applies only when those bits sit at a common offset of consecutive chunks. (the sources say so: "To apply Proposition~\ref{prop:simultaneous-layer} in a transform round, we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks." (paper))

Its sub-steps, in order:

- With $\omega_t=y^{2r/t}$ the transforms satisfy $F_t^+F_t^-=t^{-1}I$ although the ring has zero divisors, because shifting $k$ multiplies the sum by $y^{rj_0}=-1$. (on [Synthetic polynomial transform](synthetic-transform.md))
- Decimation-in-frequency rounds leave the entry of frequency $j$ in the slot with the bit-reversed address, and the opposite transform consumes that order. (on [Decimation-in-frequency butterflies and bit-reversed frequency order](butterfly-recursion.md))
- The steps of all axes in one round group into a parallel butterfly $\mathcal H$ followed by one recordwise monomial multiplication $J_E$.
- Moving the at most $D(b+1)=O(dK)$ listed bit slots to a prefix costs $O(TpdK)$.
- At most $Dq-1$ exchanges of width-$K$ chunks bring the remaining bits into consecutive chunks of equal offset, costing $O(Tp\cdot pK^{\tau-1})$.
- Each simultaneous round applies with cost $O(Tpd^{\lambda'})$, so the at most $\ell$ rounds cost $O(Tp\ell d^{\lambda'})$ in total.
- The at most $b+1\le K$ rounds on prefix slots are done by individual kernels, giving cost $O(TpdK)$.
- Contractions and one truncation per round give total error below $\sqrt2\,\ell\,2^{-p}$ and keep the disk grid.
- The forward entry of frequency address $j$ is stored at $L(Bj)$, and the opposite procedure consumes that retained order.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, using fast address interchange and fast simultaneous butterfly layers inside a Gaussian-resampling, chirp and synthetic-transform reduction.; how: Reduce the product to a convolution evaluated through Gaussian-resampled, chirped synthetic transforms, make the two costly tape operations (address movement and butterfly layers) cheaper by a power of the logarithm using networks with a rank saving, and then assemble the algorithm and add up its costs. (on [Integer multiplication below n log n](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S6.3, S6.4, S6.5, S6.6, S6.7, S6.8, S6.9). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S6.3**: The steps of all axes in one round group into a parallel butterfly $\mathcal H$ followed by one recordwise monomial multiplication $J_E$.
Source: "Consequently the individual axis steps may be grouped as a parallel butterfly $\mathcal H$, followed by one recordwise monomial operation" (paper)
> For $D$ axes of lengths $t_1,\ldots,t_D$, put \[ M=\prod_{i=1}^D t_i,\qquad F_{\boldsymbol t}^\pm=\bigotimes_{i=1}^D F_{t_i}^\pm, \qquad B=\bigotimes_{i=1}^D B_{t_i}. \] A round applies one current $H_0$ on each participating axis. The twiddle for axis $i$ depends only on that axis's address bits. The two entries paired by another axis's butterfly have the same axis-$i$ address, so that twiddle commutes with the other butterfly. Consequently the individual axis steps may be grouped as a parallel butterfly $\mathcal H$, followed by one recordwise monomial operation $J_E$. At each address, $J_E$ multiplies the record by \begin{equation} y^{E},\qquad E=-\sum_{i\ \mathrm{participating}} \frac{2r}{u_i}\,b_i k_i\pmod{2r}. \label{eq:combined-twiddle} \end{equation} Here $u_i$ is that axis's current recursive length, $b_i$ its newly written branch bit, and $0\leq k_i<u_i/2$ is encoded by its still unprocessed named slots. The exponent depends on the address, not on coefficient values. In the opposite direction the grouped round is $\mathcal HJ_E^{-1}$: apply $y^{-E}$ first and the parallel butterfly second. Each $\mathcal H$ is a contraction and each $J_E$ is an isometry, so every completed round is a contraction.

**S6.4**: Moving the at most $D(b+1)=O(dK)$ listed bit slots to a prefix costs $O(TpdK)$.
Source: "listed slots, so the moves cost $O(TpdK)$." (paper)
> long if $a_i=\ell$ and short if $a_i=\ell-1$. Name the original bit slots of axis $i$ by $(i,h)$, $a_i-1\geq h\geq0$. Initially these slots are in axis order and, within each axis, in decreasing $h$. The coefficients of each polynomial form a contiguous suffix. Put \[ b=(\ell-1)\bmod K, \qquad q=\lfloor(\ell-1)/K\rfloor. \] Form a list of the slots to move to a prefix. First list $(i,\ell-1)$ for the length-$2^\ell$ axes in increasing $i$. Then list $(i,h)$ for $h=b-1,\ldots,0$, and within each $h$ in increasing $i$; this second list is empty if $b=0$. Move each listed slot immediately after the prefix already formed, leaving all other slots in their relative order. There are at most $D(b+1)=O(dK)$ listed slots, so the moves cost $O(TpdK)$. A descriptor records the physical position of every named slot. The part of each axis left outside the prefix now consists of $q$ consecutive $K$-bit chunks.

**S6.5**: At most $Dq-1$ exchanges of width-$K$ chunks bring the remaining bits into consecutive chunks of equal offset, costing $O(Tp\cdot pK^{\tau-1})$.
Source: "This uses at most $Dq-1$ exchanges of width-$K$ address chunks, even when the chunks are nonadjacent." (paper)
> Number the axes by $i$ and their chunks, from high to low, by $j$. The remaining physical order changes from \[ (1,1),(1,2),\ldots,(1,q),(2,1),\ldots,(D,q) \quad\hbox{to}\quad (1,1),(2,1),\ldots,(D,1),(1,2),\ldots,(D,q). \] To obtain this order, scan its target positions from left to right. At each position except the last, exchange the chunk currently there with the required chunk if they differ. This uses at most $Dq-1$ exchanges of width-$K$ address chunks, even when the chunks are nonadjacent. Each costs $O(TpK^\tau)$, so all these exchanges cost \[ O\bigl(Tp\,DqK^\tau\bigr) =O\bigl(Tp\,pK^{\tau-1}\bigr). \] These prefix moves and chunk exchanges define $L$. We use the same letter for its induced record permutation: a record at address $x$ moves to address $Lx$, while its polynomial suffix stays intact. Recording the inverse operations in reverse order gives $L^{-1}$ with the same cost.

**S6.6**: Each simultaneous round applies with cost $O(Tpd^{\lambda'})$, so the at most $\ell$ rounds cost $O(Tp\ell d^{\lambda'})$ in total.
Source: "The simultaneous-layer procedure therefore applies at cost $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total." (paper)
> For a position $h$ in the remaining chunks, the selected bit has offset $(h-b)\bmod K$, counted from the least significant bit, in each of the $D$ consecutive chunks with the same chunk index $j$. Let $n_P$ and $n_S$ be the numbers of record-address bits before and after that group. Every combination of those bits occurs, so the layer sees the complete address set \[ [P]\times[2^K]^D\times[S],\qquad P=2^{n_P},\quad S=2^{n_S},\quad n_P+DK+n_S=\sum_i a_i\leq D\ell=O(p). \] Thus its record count is $PS2^{DK}=M$ and $\log_2(2M)\leq(C_\ell+1)p=C_Mp$. The current transform parameters supply $p,d,r,K,w$, and the round determines $D,P,S$ and the selected offset $\rho$. Encode these values as the header $\mathcal E$ of Proposition~\ref{prop:simultaneous-layer}. The same fixed descriptor bound covers every axis choice and round. Indeed $|\Gamma(v)|\leq2\log_2v+1$, and $\ell+n_P+n_S\leq d\ell\leq C_\ell p$. Also $d,D\leq\max\{C_\ell,1\}p$, $K,\rho+1\leq p$, and $w\leq C_wp$. Adding the nine code lengths therefore gives \[ |\mathcal E| \leq 2C_\ell p+12\log_2p+ 4\log_2\max\{C_\ell,1\}+2\log_2C_w+9 \leq C_{\rm desc}p. \] The last inequality uses $p\geq1$, $\log_2p\leq p$, and $\log_2x\leq x$ for $x\geq1$. This is the descriptor passed to the layer; the longer table locating named slots remains separate for the transform's address calculations. The simultaneous-layer procedure therefore applies at cost $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.

**S6.7**: The at most $b+1\le K$ rounds on prefix slots are done by individual kernels, giving cost $O(TpdK)$.
Source: "There are at most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$." (paper)
> In a round on prefix slots, process the participating bits individually. Temporarily move one such bit immediately before the polynomial suffix. In each now adjacent pair, buffer the first record and scan it with the second, writing the half-sums and half-differences to two work tapes. Append the half-sum record and then the half-difference record, and reverse the bit move after all pairs are processed. Including head returns, the work is $O(rp)$ per pair and $O(Tp)$ for the moves and scans at coefficient width $O(p)$. That width suffices without truncating between axes: after $s\leq D$ individual $H_0$ factors, the coefficients are exact dyadics on the $2^{-(p+s)}$ grid and still lie in the disk. A temporary sum has modulus at most two and needs only a constant number of extra integer bits. Hence $p+D+O(1)=O(p)$ bits per component suffice, since $D\leq d$ and $d\ell=O(p)$. Complete the combined monomial exactly and apply $Q_p$ once at the end of the round. Write the resulting disk-grid numerators in the supplied $w$-bit component format. Their magnitudes are at most $2^p$, so this takes one linear scan within the same bound. In an opposite round on prefix slots the inverse monomial comes first and preserves the grid and disk, so the same width bound holds for its individual factors. There are at most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$.

**S6.8**: Contractions and one truncation per round give total error below $\sqrt2\,\ell\,2^{-p}$ and keep the disk grid.
Source: "Starting with zero error, at most $\ell$ rounds therefore give the claimed error and disk bounds." (paper)
> For a forward round on a group of $D$ chunks, the layer call returns $Q_p(\mathcal H z)$ and the next operation is $J_E$. Truncation toward zero is odd and acts separately on every real and imaginary part. Since $J_E$ is a signed coefficient permutation, it follows that \[ J_EQ_p(\mathcal H z)=Q_p(J_E\mathcal H z). \] Thus the actual forward call sequence returns exactly the result of truncating once after the exact contraction round. In the opposite direction, $J_E^{-1}$ first preserves the disk grid, and the layer call returns $Q_p(\mathcal HJ_E^{-1}z)$ directly. The rounds on prefix slots have the same forms, with one truncation, by their exact evaluation above. A contraction does not increase the norm of the difference between the computed and exact arrays; the single truncation then adds less than $\sqrt2\,2^{-p}$ by \eqref{eq:transform-truncate}. Both the contraction and truncation preserve the disk. Starting with zero error, at most $\ell$ rounds therefore give the claimed error and disk bounds. The layout permutations are isometries and add no numerical error.

**S6.9**: The forward entry of frequency address $j$ is stored at $L(Bj)$, and the opposite procedure consumes that retained order.
Source: "In particular, the forward entry with frequency address $j$ is stored at $L(Bj)$." (paper)
> It remains to identify the order of the full procedures. Before relocating slots, write $\mathcal D_-=BF_{\boldsymbol t}^-$ and $\mathcal D_+=F_{\boldsymbol t}^+B^{-1}$ for the exact logical forward and opposite procedures. Executing each operation on named slots after $L$ conjugates it by $L$. The forward procedure first moves the records by $L$, whereas the opposite procedure restores them by $L^{-1}$ after its reverse arithmetic. Their full exact operators are \[ (L\mathcal D_-L^{-1})L=LB F_{\boldsymbol t}^-, \qquad L^{-1}(L\mathcal D_+L^{-1}) =F_{\boldsymbol t}^+B^{-1}L^{-1}. \] In particular, the forward entry with frequency address $j$ is stored at $L(Bj)$. The reverse arithmetic consumes the frequency branch coordinates and outputs the normalized opposite transform indexed by the original axis coordinates, which are still in layout $L$. The factor $B^{-1}$ is realized by that arithmetic; the final charged movement $L^{-1}$ restores axis-major physical order. \end{proof}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S6.1 (on [Synthetic polynomial transform](synthetic-transform.md)): With $\omega_t=y^{2r/t}$ the transforms satisfy $F_t^+F_t^-=t^{-1}I$ although the ring has zero divisors, because shifting $k$ multiplies the sum by $y^{rj_0}=-1$.
- S6.2 (on [Decimation-in-frequency butterflies and bit-reversed frequency order](butterfly-recursion.md)): Decimation-in-frequency rounds leave the entry of frequency $j$ in the slot with the bit-reversed address, and the opposite transform consumes that order.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): One H₀ butterfly applied at the same bit offset in D ≤ d address chunks at once, computed exactly via the phase network with recursive calls on 1/m of the axes and a single final truncation, in O(V d^{λ'}) time with λ' < 1.
  Shown as: Transform layout and cost *<predicate>* Simultaneous butterfly layer
- [Decimation-in-frequency butterflies and bit-reversed frequency order](butterfly-recursion.md): The transform is computed by log t rounds each pairing entries z_k and z_{k+t/2}, applying the two-point butterfly and a twiddle shift, which leaves frequency j stored at its bit-reversed position; the opposite transform consumes that order.
  Shown as: Transform layout and cost *<predicate>* Decimation-in-frequency butterflies and bit-reversed frequency order
- [Fast interchange of address chunks](chunk-interchange.md): Two disjoint address chunks of u bits in an array with complete Cartesian address set can be exchanged in O(V u^τ) time for a fixed τ < 1, although the intermediate steps form XOR combinations of the data.
  Shown as: Transform layout and cost *<predicate>* Fast interchange of address chunks
- [Synthetic polynomial transform](synthetic-transform.md): A Fourier transform over the negacyclic ring in which the roots of unity are powers of y, ω_t = y^{2r/t}, so every twiddle multiplication is a signed shift of a coefficient list (Nussbaumer–Quandalle).
  Shown as: Transform layout and cost *<predicate>* Synthetic polynomial transform
- [Arrays, address fields and logical volume](array-layout.md): Data is stored as a stream in lexicographic address order over a product of fields; the logical volume V counts stored bits and rows are consecutive blocks over a suffix field.
  Shown as: Transform layout and cost *<predicate>* Arrays, address fields and logical volume

## Pages that build on this one

- Convolution from the retained transform layout: Normalized convolution over the negacyclic ring is computed by two forward synthetic transforms, pointwise polynomial products in the retained frequency order, and the opposite transform, with explicit error bound.
- Cost table and the saving exponent κ: Dividing each cost by V = Tp, seven dominant terms have powers of p at most 1 − 2κ below one; the smallest margin 2^{-181} fixes κ = 2^{-182}, and any polylog factor is absorbed.

## Other pages you may link to

- [Two-point butterfly H₀ and the kernel C](two-point-butterfly.md)
- [Fixed-tape Turing machine model](multitape-model.md)
- [Established O(n log n) integer multiplier](nlogn-multiplier.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
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
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Multidimensional transforms and convolution on several axes](multidimensional-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Fixed-point complex arithmetic and truncation error](fixed-point-numerics.md)
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
- [The multiplication algorithm](multiplication-algorithm.md)
- [Precision and exact recovery](exact-recovery.md)
- [Cost table and the saving exponent κ](time-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The procedure constructs an explicit positional layout permutation $L$ of record addresses" (paper)

  > The procedure constructs an explicit positional layout permutation $L$ of record addresses, preserving their polynomial suffixes, and transforms disk grid arrays of $M$ contiguous degree-less-than-$r$ polynomial records. Its exact counterpart is $LB F_{\boldsymbol t}^-$. Its opposite procedure consumes that order and has exact counterpart $F_{\boldsymbol t}^+B^{-1}L^{-1}$. Each procedure has error less than $\sqrt2\ell\,2^{-p}$, returns disk grid coefficients in the same component format, and costs \begin{equation} O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right). \label{eq:synthetic-transform-cost} \end{equation} Both layout construction and final restoration are charged in this bound. The forward procedure may retain its output layout for a pointwise product and th

- "The forward procedure may retain its output layout for a pointwise product and the following opposite procedure." (paper)

  > ucts an explicit positional layout permutation $L$ of record addresses, preserving their polynomial suffixes, and transforms disk grid arrays of $M$ contiguous degree-less-than-$r$ polynomial records. Its exact counterpart is $LB F_{\boldsymbol t}^-$. Its opposite procedure consumes that order and has exact counterpart $F_{\boldsymbol t}^+B^{-1}L^{-1}$. Each procedure has error less than $\sqrt2\ell\,2^{-p}$, returns disk grid coefficients in the same component format, and costs \begin{equation} O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right). \label{eq:synthetic-transform-cost} \end{equation} Both layout construction and final restoration are charged in this bound. The forward procedure may retain its output layout for a pointwise product and the following opposite procedure. \end{lemma} \begin{proof} Put $D=d-1$ and write $a_i=\log_2t_i$. The supplied encoding has $2w=\Theta(p)$ bits per coefficient, so the logical bit volume is $\Theta(Tp)$. Call an axis long if $a_i=\ell$ and short if $a_i=\ell-1$. Name the original bit slots of axis $i$ by $(i,h)$, $a_i-1\geq h\geq0$. Initially these slots are in axis order and, within each axis, in decreasing $h$. The coefficients of each polynomial form a contiguous suffix. Put \[ b=(\ell-1)\bmod K, \qquad q=\lfloor(\ell-1)/K\rfloor. \] Form a list of the slots to move to a prefix. First list $(i,\ell-1)$ for the length-$2^\ell$ axes in increasing $i$. Then list $(i,h)$ for $h=b-1,\ldots,0$, and w


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

Write the body to `exegenius/tasks/0034-write-transform-layout.answer.md` and the JSON to `exegenius/tasks/0034-write-transform-layout.answer.json`, then run `exegenius submit 0034-write-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0034-write-transform-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
