# exegenius task 0033-write-transform-layout

Project directory: `/home/user/openai-nlogn-wiki/runs/P3` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: fluent with big-O and basic algorithm analysis (recurrences, divide and conquer, sorting and merging, schoolbook multiplication), discrete mathematics (sets, binomial coefficients, permutations, modular arithmetic, primes, gcd), and introductory linear algebra and complex numbers including roots of unity and polynomial arithmetic. They have seen single-tape and multitape Turing machines and tapes as a cost model, but not the discrete Fourier transform, FFT, fast integer multiplication, abstract algebra beyond residues, number-theoretic estimates such as the prime number theorem, or any research-level multiplication technique.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Integer multiplication complexity and the n log n conjecture
- Subspaces, rank, orthogonal complements and bilinear forms
- Arrays on tape and elementary stream operations
- Controlled cyclic shifts and fixed rational scalings
- Discrete Fourier transform
- Cyclic convolution and the convolution theorem
- Butterfly (decimation-in-frequency) transform
- Multidimensional transforms (tensor products)
- Chinese-remainder map to distinct prime axes
- Fixed-point complex grid and truncation
- Contractions and error accumulation
- Bluestein chirp identity (also: chirp identity)
- Polynomial ring modulo yʳ + 1
  - $y$ (ring variable): The formal polynomial variable, which satisfies y^r = -1 and serves as a root of unity.
  - $r$ (record length): The number of complex coefficients in a ring element, a power of two.
  - $\mathbb C$ (complex numbers): The field of complex numbers from which the coefficients are drawn.
- Synthetic polynomial transform (also: polynomial transform)
- Phase twist from cyclic to negacyclic wrap
- Signed packing (Kronecker substitution) of ring products
- Linear exchange network with restored scratch wires (also: finite network)
- Three-element-subset gather/scatter gadget
- Frames: changing the representation along network edges
- Subspace labels and the rank saving s < Wm
  - $s$ (total rank): The sum over all network edges of the rank of the frame difference, equal to the number of smaller calls needed.
  - $W$ (wire count): The number of wires, including scratch wires, in the fixed network.
  - $m$ (label dimension): The dimension of the fixed space whose subspaces label the gates.
- Bit network and the address shear
- Lower-triangular (Bruhat) factorization (also: Bruhat factorization)
- Cost of a rational matrix shear
- Power-width chunk interchange and the recursive saving
- Chunk interchange in O(V uᵗ) time
  - $V$ (stored bit volume): The number of stored data bits in the array being rearranged.
  - $u$ (chunk width): The number of bits in each of the two address chunks being interchanged.
  - $\tau$ (interchange exponent): A fixed constant below 1, here 1-2^{-50}, controlling the saving.
- Complex phase network and the C kernel
- Phase frames reduce a butterfly layer to C kernels
- Packed addition of selected address bits
- Simultaneous butterfly layer in O(V d^λ′) time
  - $V$ (stored bit volume): The number of stored data bits in the array of polynomial records.
  - $d$ (axis count): The number of address chunks (axes) on which the butterfly acts simultaneously.
  - $\lambda'$ (layer exponent): A fixed constant below 1, here 1-2^{-54}, bounding the cost growth in d.
- Binary representation of integers (also: binary expansion, bit string, bits, radix representation, base-b digits, val(x))
- Modular arithmetic (also: congruence, residues mod m, mod, residue ring Z/mZ, centered residue, modular inverse)
- Primes, divisibility, coprimality and gcd (also: prime numbers, relatively prime, coprime, pairwise coprime, greatest common divisor, Euclidean algorithm, extended Euclidean algorithm, trial division)
- Logarithms, floors and ceilings (also: log base 2, lg, binary logarithm, floor, ceiling, natural logarithm, powers of two)
- Divide and conquer and recurrences (also: recursion, recurrence relation, master theorem, geometric series, unrolling a recurrence, induction)
- Sorting, merging and radix sort (also: merge sort, stable sort, radix sorting, counting sort, merge, sorting by keys)
- Schoolbook multiplication and carries (also: long multiplication, grade-school multiplication, carry propagation, quadratic multiplication, Karatsuba)
- Permutations (also: permutation of coordinates, bijection, reordering, partial permutation, transposition, inverse permutation)
- Sets, subsets and binomial coefficients (also: n choose k, binomial coefficient, counting subsets, cardinality, intersection of sets, indicator vector, ground set)
- XOR and mod 2 arithmetic (also: bitwise XOR, exclusive or, GF(2) addition, addition mod 2, bitwise operations, F2 arithmetic)
- Hamming weight (also: wt(x), population count, popcount, number of one bits)
- Matrices and matrix-vector products (also: matrix multiplication, identity matrix, invertible matrix, transpose, diagonal matrix, lower-triangular matrix, Gaussian elimination, block matrix)
- Vector norms and the triangle inequality (also: maximum norm, sup norm, absolute value of a complex number, modulus, triangle inequality, operator norm)
- Lexicographic order and mixed-radix indexing (also: lexicographic order, dictionary order, row-major order, multi-index, mixed radix, Cartesian product, most significant coordinate)
- Two's complement and signed integers (also: signed integer encoding, sign-magnitude, sign extension)
- Dyadic and rational numbers (also: dyadic rational, rational numbers, fractions with power-of-two denominator, exact arithmetic)
- Euler's formula and complex conjugation (also: e^{i theta}, complex conjugate, unit circle, real and imaginary parts, Gaussian integers)
- Tape-based subroutines and stacks (also: subroutine call, call stack, program counter, work tape, scanning a tape, tape copying and reversal)
- Constant factors versus asymptotic dominance (also: little-o, Theta notation, Omega notation, o(1), for sufficiently large n, polylogarithmic, dominant term)

## This page

Concept: Synthetic transform layout and retained frequency order
Gloss: Selected bits of the participating axes are brought to a common offset in K-bit chunks by chunk interchanges; the forward transform leaves frequencies in bit-reversed order B_t and layout L, which the opposite transform consumes, at cost O(Tp[dK+pK^{τ−1}+ℓd^{λ′}]).

## This page in the argument

The step: A forward synthetic transform of an array of polynomial records on $d-1$ power-of-two axes, with selected bits brought to a common offset in $K$-bit chunks, leaves frequencies in a stored order $LB$ that the opposite transform consumes, and costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.
How: lay the axes out by chunk interchanges so that each round is a simultaneous butterfly layer, and add up layout, layer, prefix-round and error costs
Why: The simultaneous layer applies only when the selected bits of the participating axes sit at a common offset in consecutive $K$-bit chunks, so such a layout must be constructed. (the sources say so: "we must place the selected bits of the participating axes at a common" (paper))

Its sub-steps, in order:

- Over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ the roots $\omega_t=y^{2r/t}$ act as signed shifts of the coefficient list, so butterfly transforms $F_t^\pm$ have cheap twiddle multiplications and satisfy $F_t^+F_t^-=I/t$. (on [Synthetic polynomial transform](synthetic-transform.md))
- The decimation-in-frequency recursion writes its outputs directly in bit-reversed order, so $(F_t^-z)_j$ occupies slot $\mathrm{rev}(j)$, a record permutation $B_t$ that the reversed procedure consumes.
- A grouped round of one butterfly per participating axis is a parallel butterfly $\mathcal H$ followed by one recordwise monomial $y^E$, so each completed round is a contraction.
- Moving at most $D(b+1)=O(dK)$ named bit slots into a prefix costs $O(TpdK)$.
- At most $Dq-1$ exchanges of width-$K$ address chunks bring the remaining chunks of all axes into the order required, at total cost $O(Tp\cdot pK^{\tau-1})$.
- Each of the $\ell$ rounds on the remaining chunks is one simultaneous-layer call costing $O(Tpd^{\lambda'})$.
- The at most $K$ rounds on prefix slots are done bit by bit, individually, at cost $O(TpdK)$.
- Each round truncates once, with error below $\sqrt2\,2^{-p}$, and contractions do not amplify earlier error, so $\ell$ rounds give error below $\sqrt2\,\ell\,2^{-p}$.
- The forward procedure has exact counterpart $LBF^-_{\boldsymbol t}$ and stores the entry with frequency address $j$ at $L(Bj)$; the opposite procedure $F^+_{\boldsymbol t}B^{-1}L^{-1}$ consumes exactly this order.

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time, with $\kappa=2^{-182}$.; how: build two fast tape procedures (address interchange and simultaneous butterfly layers), use them for a fast synthetic-transform convolution over a polynomial ring, wrap that in the Gaussian-resampling, Bluestein and CRT reduction of integer multiplication, then recover the exact product and total the cost (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.2, S3.3, S3.4, S3.5, S3.6, S3.7, S3.8, S3.9). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.2**: The decimation-in-frequency recursion writes its outputs directly in bit-reversed order, so $(F_t^-z)_j$ occupies slot $\mathrm{rev}(j)$, a record permutation $B_t$ that the reversed procedure consumes.
Source: "Let $B_t$ denote this record permutation: it moves the entry at $j$" (paper)
> After all $a$ rounds, the named slots from high to low therefore contain the frequency bits from low to high. If $\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$. Let $B_t$ denote this record permutation: it moves the entry at $j$ to $\operatorname{rev}_a(j)$. The recursion writes its outputs directly in this order; it does not move whole frequency indices.

**S3.3**: A grouped round of one butterfly per participating axis is a parallel butterfly $\mathcal H$ followed by one recordwise monomial $y^E$, so each completed round is a contraction.
Source: "Each $\mathcal H$ is a contraction and each" (paper)
> For $D$ axes of lengths $t_1,\ldots,t_D$, put \[ M=\prod_{i=1}^D t_i,\qquad F_{\boldsymbol t}^\pm=\bigotimes_{i=1}^D F_{t_i}^\pm, \qquad B=\bigotimes_{i=1}^D B_{t_i}. \] A round applies one current $H_0$ on each participating axis. The twiddle for axis $i$ depends only on that axis's address bits. The two entries paired by another axis's butterfly have the same axis-$i$ address, so that twiddle commutes with the other butterfly. Consequently the individual axis steps may be grouped as a parallel butterfly $\mathcal H$, followed by one recordwise monomial operation $J_E$. At each address, $J_E$ multiplies the record by \begin{equation} y^{E},\qquad E=-\sum_{i\ \mathrm{participating}} \frac{2r}{u_i}\,b_i k_i\pmod{2r}. \label{eq:combined-twiddle} \end{equation} Here $u_i$ is that axis's current recursive length, $b_i$ its newly written branch bit, and $0\leq k_i<u_i/2$ is encoded by its still unprocessed named slots. The exponent depends on the address, not on coefficient values. In the opposite direction the grouped round is $\mathcal HJ_E^{-1}$: apply $y^{-E}$ first and the parallel butterfly second. Each $\mathcal H$ is a contraction and each $J_E$ is an isometry, so every completed round is a contraction.

**S3.4**: Moving at most $D(b+1)=O(dK)$ named bit slots into a prefix costs $O(TpdK)$.
Source: "listed slots, so the moves cost $O(TpdK)$." (paper)
> long if $a_i=\ell$ and short if $a_i=\ell-1$. Name the original bit slots of axis $i$ by $(i,h)$, $a_i-1\geq h\geq0$. Initially these slots are in axis order and, within each axis, in decreasing $h$. The coefficients of each polynomial form a contiguous suffix. Put \[ b=(\ell-1)\bmod K, \qquad q=\lfloor(\ell-1)/K\rfloor. \] Form a list of the slots to move to a prefix. First list $(i,\ell-1)$ for the length-$2^\ell$ axes in increasing $i$. Then list $(i,h)$ for $h=b-1,\ldots,0$, and within each $h$ in increasing $i$; this second list is empty if $b=0$. Move each listed slot immediately after the prefix already formed, leaving all other slots in their relative order. There are at most $D(b+1)=O(dK)$ listed slots, so the moves cost $O(TpdK)$. A descriptor records the physical position of every named slot. The part of each axis left outside the prefix now consists of $q$ consecutive $K$-bit chunks.

**S3.5**: At most $Dq-1$ exchanges of width-$K$ address chunks bring the remaining chunks of all axes into the order required, at total cost $O(Tp\cdot pK^{\tau-1})$.
Source: "exchanges of width-$K$ address chunks, even when the chunks are" (paper)
> Number the axes by $i$ and their chunks, from high to low, by $j$. The remaining physical order changes from \[ (1,1),(1,2),\ldots,(1,q),(2,1),\ldots,(D,q) \quad\hbox{to}\quad (1,1),(2,1),\ldots,(D,1),(1,2),\ldots,(D,q). \] To obtain this order, scan its target positions from left to right. At each position except the last, exchange the chunk currently there with the required chunk if they differ. This uses at most $Dq-1$ exchanges of width-$K$ address chunks, even when the chunks are nonadjacent. Each costs $O(TpK^\tau)$, so all these exchanges cost \[ O\bigl(Tp\,DqK^\tau\bigr) =O\bigl(Tp\,pK^{\tau-1}\bigr). \] These prefix moves and chunk exchanges define $L$. We use the same letter for its induced record permutation: a record at address $x$ moves to address $Lx$, while its polynomial suffix stays intact. Recording the inverse operations in reverse order gives $L^{-1}$ with the same cost.

**S3.6**: Each of the $\ell$ rounds on the remaining chunks is one simultaneous-layer call costing $O(Tpd^{\lambda'})$.
Source: "The simultaneous-layer procedure therefore applies at cost" (paper)
> For a position $h$ in the remaining chunks, the selected bit has offset $(h-b)\bmod K$, counted from the least significant bit, in each of the $D$ consecutive chunks with the same chunk index $j$. Let $n_P$ and $n_S$ be the numbers of record-address bits before and after that group. Every combination of those bits occurs, so the layer sees the complete address set \[ [P]\times[2^K]^D\times[S],\qquad P=2^{n_P},\quad S=2^{n_S},\quad n_P+DK+n_S=\sum_i a_i\leq D\ell=O(p). \] Thus its record count is $PS2^{DK}=M$ and $\log_2(2M)\leq(C_\ell+1)p=C_Mp$. The current transform parameters supply $p,d,r,K,w$, and the round determines $D,P,S$ and the selected offset $\rho$. Encode these values as the header $\mathcal E$ of Proposition~\ref{prop:simultaneous-layer}. The same fixed descriptor bound covers every axis choice and round. Indeed $|\Gamma(v)|\leq2\log_2v+1$, and $\ell+n_P+n_S\leq d\ell\leq C_\ell p$. Also $d,D\leq\max\{C_\ell,1\}p$, $K,\rho+1\leq p$, and $w\leq C_wp$. Adding the nine code lengths therefore gives \[ |\mathcal E| \leq 2C_\ell p+12\log_2p+ 4\log_2\max\{C_\ell,1\}+2\log_2C_w+9 \leq C_{\rm desc}p. \] The last inequality uses $p\geq1$, $\log_2p\leq p$, and $\log_2x\leq x$ for $x\geq1$. This is the descriptor passed to the layer; the longer table locating named slots remains separate for the transform's address calculations. The simultaneous-layer procedure therefore applies at cost $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.

**S3.7**: The at most $K$ rounds on prefix slots are done bit by bit, individually, at cost $O(TpdK)$.
Source: "most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$." (paper)
> In a round on prefix slots, process the participating bits individually. Temporarily move one such bit immediately before the polynomial suffix. In each now adjacent pair, buffer the first record and scan it with the second, writing the half-sums and half-differences to two work tapes. Append the half-sum record and then the half-difference record, and reverse the bit move after all pairs are processed. Including head returns, the work is $O(rp)$ per pair and $O(Tp)$ for the moves and scans at coefficient width $O(p)$. That width suffices without truncating between axes: after $s\leq D$ individual $H_0$ factors, the coefficients are exact dyadics on the $2^{-(p+s)}$ grid and still lie in the disk. A temporary sum has modulus at most two and needs only a constant number of extra integer bits. Hence $p+D+O(1)=O(p)$ bits per component suffice, since $D\leq d$ and $d\ell=O(p)$. Complete the combined monomial exactly and apply $Q_p$ once at the end of the round. Write the resulting disk-grid numerators in the supplied $w$-bit component format. Their magnitudes are at most $2^p$, so this takes one linear scan within the same bound. In an opposite round on prefix slots the inverse monomial comes first and preserves the grid and disk, so the same width bound holds for its individual factors. There are at most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$.

**S3.8**: Each round truncates once, with error below $\sqrt2\,2^{-p}$, and contractions do not amplify earlier error, so $\ell$ rounds give error below $\sqrt2\,\ell\,2^{-p}$.
Source: "zero error, at most $\ell$ rounds therefore" (paper)
> For a forward round on a group of $D$ chunks, the layer call returns $Q_p(\mathcal H z)$ and the next operation is $J_E$. Truncation toward zero is odd and acts separately on every real and imaginary part. Since $J_E$ is a signed coefficient permutation, it follows that \[ J_EQ_p(\mathcal H z)=Q_p(J_E\mathcal H z). \] Thus the actual forward call sequence returns exactly the result of truncating once after the exact contraction round. In the opposite direction, $J_E^{-1}$ first preserves the disk grid, and the layer call returns $Q_p(\mathcal HJ_E^{-1}z)$ directly. The rounds on prefix slots have the same forms, with one truncation, by their exact evaluation above. A contraction does not increase the norm of the difference between the computed and exact arrays; the single truncation then adds less than $\sqrt2\,2^{-p}$ by \eqref{eq:transform-truncate}. Both the contraction and truncation preserve the disk. Starting with zero error, at most $\ell$ rounds therefore give the claimed error and disk bounds. The layout permutations are isometries and add no numerical error.

**S3.9**: The forward procedure has exact counterpart $LBF^-_{\boldsymbol t}$ and stores the entry with frequency address $j$ at $L(Bj)$; the opposite procedure $F^+_{\boldsymbol t}B^{-1}L^{-1}$ consumes exactly this order.
Source: "In particular, the forward entry with frequency address $j$ is" (paper)
> It remains to identify the order of the full procedures. Before relocating slots, write $\mathcal D_-=BF_{\boldsymbol t}^-$ and $\mathcal D_+=F_{\boldsymbol t}^+B^{-1}$ for the exact logical forward and opposite procedures. Executing each operation on named slots after $L$ conjugates it by $L$. The forward procedure first moves the records by $L$, whereas the opposite procedure restores them by $L^{-1}$ after its reverse arithmetic. Their full exact operators are \[ (L\mathcal D_-L^{-1})L=LB F_{\boldsymbol t}^-, \qquad L^{-1}(L\mathcal D_+L^{-1}) =F_{\boldsymbol t}^+B^{-1}L^{-1}. \] In particular, the forward entry with frequency address $j$ is stored at $L(Bj)$. The reverse arithmetic consumes the frequency branch coordinates and outputs the normalized opposite transform indexed by the original axis coordinates, which are still in layout $L$. The factor $B^{-1}$ is realized by that arithmetic; the final charged movement $L^{-1}$ restores axis-major physical order. \end{proof}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S3.1 (on [Synthetic polynomial transform](synthetic-transform.md)): Over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ the roots $\omega_t=y^{2r/t}$ act as signed shifts of the coefficient list, so butterfly transforms $F_t^\pm$ have cheap twiddle multiplications and satisfy $F_t^+F_t^-=I/t$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Butterfly (decimation-in-frequency) transform](butterfly-fft.md)
- [Contractions and error accumulation](contraction-error.md)
- [Arrays on tape and elementary stream operations](stream-ops.md)
- [Fixed-point complex grid and truncation](fixed-point.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Synthetic polynomial transform](synthetic-transform.md): A butterfly transform over the ring C[y]/(y^r+1) whose roots of unity ω_t=y^{2r/t} act as exact signed shifts of the coefficient list, so twiddle multiplications are cheap (Nussbaumer–Quandalle).
  Shown as: Synthetic transform layout and retained frequency order *<predicate>* Synthetic polynomial transform
- [Simultaneous butterfly layer in O(V d^λ′) time](simultaneous-layer.md): Applying H₀ to the same bit position in d address chunks of polynomial records at once, exactly in Gaussian dyadics with guard bits and one final truncation, costs O(V d^{λ′}) with λ′<1 instead of d passes.
  Shown as: Synthetic transform layout and retained frequency order *<predicate>* Simultaneous butterfly layer in O(V d^λ′) time
- [Chunk interchange in O(V uᵗ) time](chunk-interchange.md): Interchanging two disjoint u-bit address fields of an array in which all address combinations occur costs O(V u^τ) for a fixed τ<1, via XOR-style intermediate steps whose final effect is an exact permutation.
  Shown as: Synthetic transform layout and retained frequency order *<predicate>* Chunk interchange in O(V uᵗ) time

## Pages that build on this one

- Normalized convolution over the ring from the retained layout: Forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform in the same stored order compute f*g/(rM) on the remaining axes over C[y]/(y^r+1) with error below √2·M(3ℓ+1)2^{-p}.
- Cost table and the κ margin: Dividing costs by Tp=Θ(n), seven dominant terms have powers of p at most 1−2κ (smallest margin 2^{-181}), so every polylogarithmic loss is absorbed and the total is O(n (log n)^{1−κ}).

## Other pages you may link to

- [Integer multiplication complexity and the n log n conjecture](history.md)
- [Arrays on tape and elementary stream operations](stream-ops.md)
- [Controlled cyclic shifts and fixed rational scalings](controlled-shift.md)
- [Subspaces, rank, orthogonal complements and bilinear forms](linear-algebra.md)
- [Linear exchange network with restored scratch wires](linear-network.md)
- [Frames: changing the representation along network edges](frames.md)
- [Three-element-subset gather/scatter gadget](subset-gadget.md)
- [Subspace labels and the rank saving s < Wm](rank-saving.md)
- [Bit network and the address shear](bit-network-shear.md)
- [Complex phase network and the C kernel](complex-phase-network.md)
- [Lower-triangular (Bruhat) factorization](triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Power-width chunk interchange and the recursive saving](power-width-interchange.md)
- [Packed addition of selected address bits](packed-bit-addition.md)
- [Polynomial ring modulo yʳ + 1](ring-mod-yr.md)
- [Fixed-point complex grid and truncation](fixed-point.md)
- [Signed packing (Kronecker substitution) of ring products](signed-packing.md)
- [Discrete Fourier transform](dft.md)
- [Butterfly (decimation-in-frequency) transform](butterfly-fft.md)
- [Phase frames reduce a butterfly layer to C kernels](phase-frame-reduction.md)
- [Contractions and error accumulation](contraction-error.md)
- [Cyclic convolution and the convolution theorem](convolution.md)
- [Multidimensional transforms (tensor products)](multidim-transform.md)
- [Chinese-remainder map to distinct prime axes](crt-map.md)
- [Bluestein chirp identity](bluestein.md)
- [Phase twist from cyclic to negacyclic wrap](phase-twist.md)
- [Normalized convolution over the ring from the retained layout](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling with the permutations left in the transform](retained-permutations.md)
- [Integer product as convolution of radix digits](integer-as-convolution.md)
- [Exact recovery by rounding and carry propagation](exact-recovery.md)
- [Parameter choices, padded box and prime source lengths](parameters.md)
- [Complex cyclic convolution via the coefficient twist](complex-convolution-twist.md)
- [Computed source transform](source-transform.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost table and the κ margin](cost-accounting.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The procedure constructs an explicit positional" (paper)

  > The procedure constructs an explicit positional layout permutation $L$ of record addresses, preserving their polynomial suffixes, and transforms disk grid arrays of $M$ contiguous degree-less-than-$r$ polynomial records. Its exact counterpart is $LB F_{\boldsymbol t}^-$. Its opposite procedure consumes that order and has exact counterpart $F_{\boldsymbol t}^+B^{-1}L^{-1}$. Each procedure has error less than $\sqrt2\ell\,2^{-p}$, returns disk grid coefficients in the same component format, and costs \begin{equation} O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right). \label{eq:synthetic-transform-cost} \end{equation} Both layout construction and final restoration are charged in this bound. The forward procedure may retain its output layout for a po

- "entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$." (paper)

  > After all $a$ rounds, the named slots from high to low therefore contain the frequency bits from low to high. If $\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$. Let $B_t$ denote this record permutation: it moves the entry at $j$ to $\operatorname{rev}_a(j)$. The recursion writes its outputs directly in this order; it does not move whole frequency indices.


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

Write the body to `exegenius/tasks/0033-write-transform-layout.answer.md` and the JSON to `exegenius/tasks/0033-write-transform-layout.answer.json`, then run `exegenius submit 0033-write-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0033-write-transform-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
