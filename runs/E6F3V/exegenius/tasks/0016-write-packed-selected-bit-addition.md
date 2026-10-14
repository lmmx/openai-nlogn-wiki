# exegenius task 0016-write-packed-selected-bit-addition

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F3V` (paths below are relative to it)

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

For these sources: The reader is an undergraduate in computer science who has taken discrete mathematics, data structures and algorithms, introductory theory of computation, and the linear algebra and calculus that accompany such a degree. They are fluent with asymptotic analysis, recurrences, binary representation and bitwise operations, modular arithmetic, matrices and rank, vector spaces over the reals, and complex numbers including roots of unity; they know the schoolbook and Karatsuba multiplication algorithms and what a Turing machine with tapes is. They have not studied abstract algebra beyond basics, the FFT's algebraic variants, number-theoretic transforms, finite fields beyond arithmetic mod 2, analytic number theory, numerical analysis of rounding error, or any bit-complexity multiplication algorithm.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Schönhage–Strassen optimality conjecture
- Harvey–van der Hoeven O(n log n) multiplier
- Arrays and elementary stream operations on tape
- Controlled shifts and rational scalings
- Bank-exchange network with restored scratch wires
- Frames on network wires
- Nested subspace labels and orthogonal residuals
- Strict rank saving
- Lower-triangular factorization of a matrix
- Cost of a matrix shear on address fields
- Power-width chunk interchange
- Address chunk interchange
  - $V$ (stored bit volume): The number of data bits stored in the array being permuted.
  - $u$ (chunk width): The number of bits in each of the two interchanged address chunks.
  - $\tau$ (interchange exponent): A fixed constant below one, 1 − 2^{−50}, bounding the power of the width in the cost.
- Asymptotic notation beyond big-O (also: Omega notation, Theta notation, little-o, o(...), Ω, Θ, asymptotically smaller, worst-case running time)
- Limits and limit inferior (also: liminf, limsup, limit of a ratio, lim inf, eventually, for all sufficiently large n)
- Logarithms, exponentials, floors and ceilings (also: log base 2, lg n, log_2, natural logarithm, floor function, ceiling function, powers of two, iterated logarithm, log star)
- Recurrences and geometric sums (also: recurrence relation, solving recurrences, geometric series, geometric sum, unrolling a recurrence, divide and conquer)
- Positional number systems and carries (also: binary representation, radix representation, base-b digits, bit string, most significant bit, carry propagation, schoolbook addition, padding with leading zeros)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba, divide-and-conquer multiplication, Toom-Cook, quadratic multiplication)
- Bitwise operations and XOR (also: exclusive or, XOR, bitwise exclusive or, addition modulo 2, bit flip, parity, bit shift, bit mask)
- Modular arithmetic (also: integers modulo q, Z/qZ, congruence, residues, units modulo q, invertible residues, arithmetic mod q, Chinese remainder theorem for integers)
- Primes, coprimality and the extended Euclidean algorithm (also: prime numbers, relatively prime, pairwise coprime, gcd, greatest common divisor, Euclid's algorithm, Bezout identity, modular inverse, odd primes, primality testing by trial division)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, unit complex numbers, complex exponential, Euler's formula, twiddle factor, N-th root of unity)
- Matrices and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, linear operator, linear transformation, identity matrix, diagonal matrix, unitary or involution matrix, matrix-vector product, linear combination)
- Vector spaces, subspaces, dimension and rank (also: subspace, span, basis, linear independence, dimension, rank of a matrix, rank-nullity, kernel, image, column space, direct sum, quotient space)
- Inner products, bilinear forms and orthogonal complements (also: bilinear form, dot product, orthogonality, orthogonal complement, orthogonal subspace, nondegenerate pairing, inner product space, pairing)
- Gaussian elimination and triangular matrices (also: row reduction, LU decomposition, lower triangular matrix, upper triangular matrix, elementary row operations, back substitution, unit triangular matrix, row echelon form)
- Permutations, bijections and permutation matrices (also: permutation, bijection, one-to-one correspondence, inverse permutation, partial permutation, reordering of an array, sorting network, transposition of indices, permutation matrix)
- Arithmetic modulo 2 and linear algebra over F_2 (also: F_2, GF(2), binary field, field with two elements, matrices over F_2, GL(m, F_2), mod 2 arithmetic, boolean linear algebra)
- Finite sets, subsets and counting (also: Cartesian product, subset intersection, set cardinality, binomial coefficient, inclusion-exclusion, product of index sets, power set, three-element subsets, pigeonhole)
- Circuits and directed acyclic graphs (also: arithmetic circuit, linear circuit, wires and gates, directed graph, DAG, network of gates, fan-in, source and sink nodes, layered network)
- Vector norms and the triangle inequality (also: sup norm, maximum norm, infinity norm, ‖·‖_∞, modulus bound, triangle inequality, operator norm, error bound, disk bound)
- Fixed-point numbers, dyadic rationals and rounding (also: fixed point arithmetic, dyadic rational, binary fraction, rounding to nearest integer, truncation, round-off error, precision in bits, numbers with p fractional bits, grid of spacing 2^{-p})
- Row-major order and matrix transposition (also: row-major layout, array layout, transposing a matrix, matrix transpose, k×k binary matrix, lexicographic address, two-dimensional array as a list)
- Subroutines and reductions between problems (also: black-box subroutine, reduction, calling a subroutine, oracle call, problem reduction, conditional lower bound, composition of algorithms, uniform algorithm)
- Convolution of sequences (also: linear convolution, polynomial multiplication as convolution, product of coefficient sequences, discrete convolution, convolution theorem)

## This page

Concept: Packed selected-bit addition
Gloss: XORing corresponding selected bits of two address chunks by constantly many cyclic shifts of whole chunk ranges plus a deterministic repair of an explicitly small set of exceptional addresses, using a third chunk as restored scratch.

## This page in the argument

The step: Given chunks $x,y,z$ of $L=fK$ bits, the $f$ XORs $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ at positions $j_i=\rho+iK$ are done by constantly many cyclic shifts of whole chunk ranges (restoring $z$) plus a deterministic repair of the exceptional addresses, a fraction at most $80(f-1)2^{-K}$, in $O(V(L^\tau+1))$ time.
How: Perform all $f$ XORs at once as eight packed additions that are correct whenever no $K$-bit segment lies near the edge of its field, then extract, sort and reinsert the few addresses where that fails.
Why: A shift of whole chunks costs linear time but can carry between neighbouring segments only when a segment is near the end of its range, which happens for a tiny, address-determined fraction of addresses; those can be fixed separately without depending on the payload. (the sources leave this for the reader to work out: spell it out)
Striking feature: The exceptional fraction $80(f-1)2^{-K}$ is exponentially small in the chunk width $K$ and depends only on addresses, never on the record contents, so the repair is cheap in the worst case. (explain why it holds, from the method)

Its sub-steps, in order:

- For a Boolean control $c$, eight conditional unit additions to integers $u,w$ flip the parity of $u$ exactly when $c=1$ and restore the auxiliary integer $w$.
- There are twenty excluded values for each of the $2(f-1)$ guards, so the exceptional set $\mathcal B$ has at most a fraction $\delta_{\rm bad}$ of the addresses, whatever the payload.
- Each rotation is a chunk swap, a controlled cyclic shift of the target chunk costing $O(V)$, and the swap undone, so the movement costs $O(V(L^\tau+1))$.
- The exceptional records are extracted with their destination ranks, stably radix-sorted and reinserted, which implements the ideal permutation $T_0$ everywhere.
- After division by $V$ the extra terms are $A^3/R$ and $80(f-1)2^{-K}A(1+A/R)$, which are $o(1)$ under the family bounds, leaving $O(V(L^\tau+1))$.

It serves these steps, from the main result down:

- One deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a convolution of short digits evaluated by Fourier transforms, speed up the two costly ingredients (moving data between addresses, and butterfly arithmetic) by a power of a block size using one recursive saving, and total every cost term. (on [Sub-n-log-n integer multiplication](main-theorem.md))
- Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ to one selected bit in each of $D\le d$ address chunks of $K$ bits, on records of $r$ complex coefficients, costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$, instead of $D$ whole-array passes, and is exact up to one final truncation.; how: Rerun the rank-saving recursion with the complex phase network: express the tensor product of $H_0$ through the kernel $C$, whose frame change on an edge is one translation kernel per residual basis vector, so each edge becomes smaller layers on slots of fewer chunks, with the binary basis changes done by packed whole-chunk moves. (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.2.1, S3.2.2, S3.2.3, S3.2.4, S3.2.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.2.1**: For a Boolean control $c$, eight conditional unit additions to integers $u,w$ flip the parity of $u$ exactly when $c=1$ and restore the auxiliary integer $w$.
Source: "Consequently the complete output is
\begin{equation}
\label{eq:eight-packed-result}
 (u',w')=
 \bigl(u+c(1-2(u\bmod2)),\ w\bigr)." (paper)
> arrow&w+c[\,u\equiv1\pmod2\,],&(5)\\ u&\leftarrow&u+c[\,w\equiv1\pmod2\,],&(6)\\ w&\leftarrow&w-c[\,u\equiv1\pmod2\,],&(7)\\ u&\leftarrow&u-c[\,w\equiv1\pmod2\,].&(8) \end{array} \end{equation} If $c=0$, these operations do nothing. If $c=1$, the first four operations induce the cycle $(00\ 01\ 10)$ in every square \[ \{2a,2a+1\}\times\{2b,2b+1\},\qquad a,b\in\mathbb Z, \] where the corner labels record the parities of $(u,w)$. The last four induce $(01\ 10\ 11)$. Applying the first cycle and then the second gives $(00\ 10)(01\ 11)$. These facts follow by substituting the four parity pairs into the displayed operations; translation by $(2a,2b)$ does not change any predicate. Consequently the complete output is \begin{equation} \label{eq:eight-packed-result} (u',w')= \bigl(u+c(1-2(u\bmod2)),\ w\bigr). \end{equation} Here $u\bmod2\in\{0,1\}$, also for negative $u$. Thus the parity of $u$ is flipped precisely when $c=1$, both quotients under division by two are preserved, and the arbitrary auxiliary integer $w$ is restored. Each coordinate is updated four times by at most one, so its displacement from its initial value is at most four, even if an intermediate point leaves its starting quotient square. The weaker bound eight will suffice below.

**S3.2.2**: There are twenty excluded values for each of the $2(f-1)$ guards, so the exceptional set $\mathcal B$ has at most a fraction $\delta_{\rm bad}$ of the addresses, whatever the payload.
Source: "There are exactly twenty excluded values for each guard in
\eqref{eq:packed-guard-interval}. Since its complete range has
$2^{K-1}$ values, the union bound over the $2(f-1)$ guards gives
\begin{equation}
\label{eq:packed-bad-fraction}
 |\mathcal B|\le\delta_{\rm bad}M." (paper)
> There are exactly twenty excluded values for each guard in \eqref{eq:packed-guard-interval}. Since its complete range has $2^{K-1}$ values, the union bound over the $2(f-1)$ guards gives \begin{equation} \label{eq:packed-bad-fraction} |\mathcal B|\le\delta_{\rm bad}M. \end{equation} Indeed, the complete $y,z$ ranges give the same guard distribution at each choice of spectator coordinates. No record value enters this count.

**S3.2.3**: Each rotation is a chunk swap, a controlled cyclic shift of the target chunk costing $O(V)$, and the swap undone, so the movement costs $O(V(L^\tau+1))$.
Source: "therefore gives an $O(V)$ rotation: its offset work is absorbed by the
$2^L$ nonempty target blocks in each fiber. Undo the swap after the
rotation." (paper)
> The equal chunk lengths leave the field-length list unchanged by a completed swap. Keep the permutation of the logical names $x,y,z$ in finite local state. With the target now after its two controls, collapse the remaining intervals to obtain \[ [\Lambda_0]\times[2^L]_{\rm control\,1}\times[\Lambda_1] \times[2^L]_{\rm control\,2}\times[\Lambda_2] \times[2^L]_{\rm target}\times[B_{\rm rot}], \] where $B_{\rm rot}$ includes the payload and every displayed spectator length is positive. Their product with the chunk lengths is $V$. Together with $K,f,\rho$ and the finite name permutation, these fixed canonical lengths form an $O(A_{\rm rect})$-bit local descriptor. The offset routine receives the two current $L$-bit logical control values. A scan of at most $f\le L$ selected positions evaluates \eqref{eq:packed-cyclic-shift} in $L^{O(1)}$ time, without reading the target or spectator values. Lemma~\ref{lem:ordered-affine-streams} therefore gives an $O(V)$ rotation: its offset work is absorbed by the $2^L$ nonempty target blocks in each fiber. Undo the swap after the rotation. The local descriptors and name permutation are updated at completed swap boundaries; the primitives use their own descriptors inside padded layouts. There are at most sixteen swaps and eight rotations in $S_0$.

**S3.2.4**: The exceptional records are extracted with their destination ranks, stably radix-sorted and reinserted, which implements the ideal permutation $T_0$ everywhere.
Source: "Hold the full stream untouched
while stable binary radix sorting scans only the extracted records and
keys, least significant key bit first. Since $T_0S_0^{-1}$ permutes
$\mathcal B$, these keys are distinct and are exactly the ranks of the
marked holes. One forward full-stream scan reinserts the sorted records.
This implements $T_0$ everywhere." (paper)
> If $q_h,q'_h$ are the current and destination values of chunk $h\in\{x,y,z\}$ and $\sigma_h$ is its record stride, the fixed spectator coordinates give \[ \operatorname{rank}(q')=\operatorname{rank}(q)+ \sum_{h\in\{x,y,z\}}(q'_h-q_h)\sigma_h. \] The differences are signed. Attach this destination rank, padded to $\lceil\log_2M\rceil\le A_{\rm rect}$ bits, to the extracted record, and mark its hole on a fixed track of the full stream. Hold the full stream untouched while stable binary radix sorting scans only the extracted records and keys, least significant key bit first. Since $T_0S_0^{-1}$ permutes $\mathcal B$, these keys are distinct and are exactly the ranks of the marked holes. One forward full-stream scan reinserts the sorted records. This implements $T_0$ everywhere.

**S3.2.5**: After division by $V$ the extra terms are $A^3/R$ and $80(f-1)2^{-K}A(1+A/R)$, which are $o(1)$ under the family bounds, leaving $O(V(L^\tau+1))$.
Source: "After division by $V=MR$, its additional terms are bounded by
$A_{\rm rect}^3/R$ and
$80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. Under the stated family bounds
the first tends to zero, and the second is
$O(p^2 2^{-K}(1+A_{\rm rect}/R))=o(1)$." (paper)
> The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans costs $O(MA_{\rm rect}^3+V)$, and the at most $A_{\rm rect}$ radix passes cost $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$; skip them when the extracted bank is empty. The initial descriptor has a fixed number of canonical integers of $O(A_{\rm rect})$ bits, so its preparation is covered by $O(MA_{\rm rect}^3)$. All counters, positioning, rewinds, and cleanup are included. Equation~\eqref{eq:packed-bad-fraction} proves \eqref{eq:packed-rectangle-time} on a fixed number of tapes. After division by $V=MR$, its additional terms are bounded by $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. Under the stated family bounds the first tends to zero, and the second is $O(p^2 2^{-K}(1+A_{\rm rect}/R))=o(1)$. This proves the final assertion. \end{proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Address chunk interchange](chunk-interchange.md): Swapping two disjoint equal-width bit chunks of an address array in O(V u^τ) steps for a fixed τ < 1, by XOR combinations whose final effect is an exact permutation.
  Shown as: Packed selected-bit addition *<predicate>* Address chunk interchange
- [Controlled shifts and rational scalings](controlled-shift.md): Adding to a later address field an offset computed from earlier control fields, or multiplying it by a rational unit, in linear time by splitting and re-merging blocks.
  Shown as: Packed selected-bit addition *<predicate>* Controlled shifts and rational scalings

## Pages that build on this one

- Simultaneous butterfly layer: Applying H₀ to one selected bit in each of D address chunks at once, on arrays of ring records, in O(V d^{λ′}) with λ′ < 1 instead of D whole-array passes, via the recursive complex network on packed bit changes.

## Other pages you may link to

- [Schönhage–Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hh-multiplier.md)
- [Arrays and elementary stream operations on tape](tape-stream-operations.md)
- [Bank-exchange network with restored scratch wires](exchange-network.md)
- [Frames on network wires](frames.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Strict rank saving](rank-saving.md)
- [Lower-triangular factorization of a matrix](matrix-factorization.md)
- [Cost of a matrix shear on address fields](matrix-shear.md)
- [Power-width chunk interchange](power-width-interchange.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Contractions and error accumulation](contraction-error.md)
- [Exact dyadic intermediates with one truncation](guard-bits.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer product as digit convolution](radix-digit-convolution.md)
- [Coefficient phase twist](phase-twist.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-two recursion](fft-butterfly.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Phase frames and the two-point kernel C](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Stored bit-reversed frequency order](bit-reversed-order.md)
- [Transform layout and cost](transform-layout.md)
- [Convolution over the polynomial ring](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutations cancel in a convolution](permutation-cancellation.md)
- [Chinese-remainder map to prime axes](crt-axis-map.md)
- [Prime axis lengths near powers of two](prime-axis-lengths.md)
- [Parameter choice for the multiplier](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound](time-bound.md)
- [Sub-n-log-n integer multiplication](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "y_{j_i}\longleftarrow y_{j_i}\mathbin\oplus x_{j_i}" (paper)

  > <K$. Let $N_0,N_1,N_2,N_3$ be positive integers, and let $(\chi_1,\chi_2,\chi_3)$ be a permutation of $(x,y,z)$. Consider $R$-bit records in lexicographic order on \[ [N_0]\times[2^L]_{\chi_1}\times[N_1]\times[2^L]_{\chi_2} \times[N_2]\times[2^L]_{\chi_3}\times[N_3]. \] The subscript names the chunk at that position. The input supplies $N_0,\ldots,N_3,R,K,f,\rho$ as a fixed number of canonical binary integers, together with the finite permutation of the chunk names, as in Section~\ref{sec:streams}. Put \[ M=2^{3L}\prod_{h=0}^3N_h,\qquad V=MR,\qquad A_{\rm rect}=\lceil\log_2(2V)\rceil. \] At the selected positions $j_i=\rho+iK$, numbered from the least significant bit, one fixed multitape procedure performs \[ y_{j_i}\longleftarrow y_{j_i}\mathbin\oplus x_{j_i} \quad(0\le i<f). \] It preserves the spectator coordinates, all other chunk bits, and every record payload; in particular, it restores the entire chunk $z$ for every initial value. With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, its time is \begin{equation} \label{eq:packed-rectangle-time} O\!\left(V(L^\tau+1)+MA_{\rm rect}^3+ \delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect})\right). \end{equation} When $A_{\rm rect}=O(p)$, $R$ exceeds every fixed polynomial in $p$, $f\le d\le p$, and $K/\log p\to\infty$, this is $O(V(L^\tau+1))$, uniformly over the permitted lengths and payloads in the fixed family. \end{lemma}

- "\begin{lemma}[Packed selected-bit addition on one rectangle]" (paper)

  > \begin{lemma}[Packed selected-bit addition on one rectangle] \label{lem:packed-selected-bit-rectangle} Let $R\ge1$, $K\ge6$, $f\ge1$, $L=fK$, and $0\le\rho<K$. Let $N_0,N_1,N_2,N_3$ be positive integers, and let $(\chi_1,\chi_2,\chi_3)$ be a permutation of $(x,y,z)$. Consider $R$-bit records in lexicographic order on \[ [N_0]\times[2^L]_{\chi_1}\times[N_1]\times[2^L]_{\chi_2} \times[N_2]\times[2^L]_{\chi_3}\times[N_3]. \] The subscript names the chunk at that position. The input supplies $N_0,\ldots,N_3,R,K,f,\rho$ as a fixed number of canonical binary integers, together with the finite permutation of the chunk names, as in Section~\ref{sec:streams}. Put \[ M=2^{3L}\prod_{h=0}^3N_h,\qquad V=MR,\qquad A_{\rm rect}=\lceil\log_2(2V)\rceil. \] At the selected positions


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

Write the body to `exegenius/tasks/0016-write-packed-selected-bit-addition.answer.md` and the JSON to `exegenius/tasks/0016-write-packed-selected-bit-addition.answer.json`, then run `exegenius submit 0016-write-packed-selected-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0016-write-packed-selected-bit-addition`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
