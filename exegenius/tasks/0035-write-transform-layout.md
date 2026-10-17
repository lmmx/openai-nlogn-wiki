# exegenius task 0035-write-transform-layout

Project directory: `/home/user/e2e-run` (paths below are relative to it)

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

For these sources: The reader is a computer science undergraduate: they have taken discrete mathematics, an algorithms course (asymptotics, divide and conquer, schoolbook and Karatsuba multiplication, sorting), a first linear algebra course (vector spaces, subspaces, dimension, rank, matrices as linear maps, inverses, triangular matrices, orthogonality, bilinear forms at a basic level), calculus, elementary number theory (primes, gcd, modular arithmetic) and basic machine-level binary representation (XOR, two's complement). They have seen Turing machines with tapes only at an introductory level. They have not been taught the discrete Fourier transform or FFT as such, abstract algebra beyond basic definitions (quotient rings, finite fields as a theory), tensor products, numerical error analysis, or the specific literature on fast integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed finite-tape machine model (also: multitape Turing machine, fixed-tape model)
- Elementary stream operations
- Controlled shifts and rational scalings
- Schönhage–Strassen optimality conjecture (also: n log n conjecture)
- Established O(n log n) multiplier
- Cyclic convolution
- Multiplication as radix-digit convolution
- Discrete Fourier transform (also: Fourier transform, DFT)
- Butterflies and the fast transform
- Multidimensional transforms
- Chinese-remainder address map (also: Agarwal–Cooley map)
- Gaussian resampling
- Bluestein chirp identity
- Retained permutation cancellation
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Retained frequency order
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records
- Error tracking and exact recovery
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
- Recursive power saving
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Fast address-chunk interchange (also: chunk swap, tape interchange)
- Two-point kernel C (also: phase network kernel)
- Binary phase frames
- Packed selected-bit addition
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Schoolbook and Karatsuba multiplication (also: long multiplication, grade-school multiplication, Karatsuba, O(n^2) multiplication, n^{log_2 3} multiplication)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Binary and radix representation (also: base-b digits, positional notation, binary expansion, bit string, most significant bit, padding with leading zeros, carry propagation)
- Two's complement integers (also: two's-complement, signed binary integers, signed fixed-width addition)
- Bitwise XOR and arithmetic mod 2 (also: XOR, exclusive or, addition in F_2, GF(2), parity, bit flip)
- Logarithms and floors/ceilings (also: lg, log base 2, ceiling, floor, iterated logarithm, log log n)
- Modular arithmetic and primes (also: congruence, residues mod n, gcd, coprime, relatively prime, prime numbers, Z/nZ, modular inverse, units mod n)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n}, Euler's formula)
- Vector spaces, subspaces, dimension and rank (also: linear subspace, basis, span, linear independence, dimension, matrix rank, kernel, linear map, linear operator, direct sum)
- Matrices and linear operators (also: matrix multiplication, invertible matrix, matrix inverse, identity matrix, commuting operators, diagonal matrix, triangular matrix, lower triangular, permutation matrix)
- Gaussian elimination and triangular factorization (also: row reduction, LU decomposition, back substitution)
- Orthogonality and inner products (also: orthonormal basis, dot product, orthogonal complement, bilinear form, nondegenerate form, Euclidean norm)
- Norms and the triangle inequality (also: sup norm, max norm, infinity norm, modulus bounds, absolute value bounds)
- Permutations and bijections (also: permutation of indices, sorting a permutation, bit-reversal permutation, bijective map, inverse permutation)
- Cartesian products and multi-index arrays (also: multidimensional arrays, row-major order, lexicographic order, mixed-radix index, index tuples, array stored on a tape)
- Directed acyclic graphs and networks of gates (also: circuit, DAG, wire, gate, edges and vertices, fan-in)
- Summation, geometric series and induction (also: geometric sum, proof by induction, summation notation, telescoping sum)
- Rounding to the nearest integer and exactness (also: rounding, truncation, round to nearest, rational numbers, dyadic rational)
- Multitape Turing machine running time (also: tape head movement, scanning a tape, linear-time pass over a tape, time complexity of a Turing machine, worst-case running time)
- Integer exponentials and tuple notation (also: powers of two, tensor power notation, exponent of a constant, fixed rational exponents)

## This page

Concept: Tape layout for synthetic transforms
Gloss: Placing the selected bits of the participating axes at a common offset in K-bit chunks so each round of the synthetic transform is one simultaneous layer, costing less than log t passes.

## This page in the argument

The step: Synthetic transforms over $\mathcal R_r$ on $d-1$ axes of lengths $t_i\in\{2^{\ell-1},2^\ell\}$ with outputs kept in a retained layout $LB$ cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error less than $\sqrt2\ell\,2^{-p}$.
How: Use the radix-two synthetic (Nussbaumer) transform, whose twiddles are signed shifts, and lay out the selected bits of all participating axes at a common offset in $K$-bit chunks so that every round is one simultaneous butterfly layer, with fewer than $\log t$ passes.
Why: To apply the simultaneous layer in a transform round, the selected bits of the participating axes must sit at a common offset in consecutive $K$-bit chunks. (the sources say so: "we must place the selected bits of the participating axes at a common" (paper))

Its sub-steps, in order:

- The synthetic transform $F_t^-$ over $\mathcal R_r=\mathbb C[y]/(y^r+1)$, with roots of unity $\omega_t=y^{2r/t}$, is computed by decimation in frequency with outputs written in bit-reversed order, $B_tF_t^-$; the pointwise product keeps this order and the reverse procedure computes $F_t^+B_t^{-1}$, so no reordering is executed. (on [Retained frequency order](frequency-order.md))
- On a layout $L$ that places the selected bits of all participating axes of an array of $M=T/r$ polynomial records at a common offset in consecutive $K$-bit chunks, a forward synthetic transform (exact counterpart $LBF_{\boldsymbol t}^-$) and its opposite (exact counterpart $F_{\boldsymbol t}^+B^{-1}L^{-1}$) have error less than $\sqrt2\ell\,2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.2). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.2**: On a layout $L$ that places the selected bits of all participating axes of an array of $M=T/r$ polynomial records at a common offset in consecutive $K$-bit chunks, a forward synthetic transform (exact counterpart $LBF_{\boldsymbol t}^-$) and its opposite (exact counterpart $F_{\boldsymbol t}^+B^{-1}L^{-1}$) have error less than $\sqrt2\ell\,2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.
How: Move $O(dK)$ selected slots to a prefix one by one, exchange $Dq-1$ chunks of width $K$ by the chunk-interchange procedure to bring equal-offset chunks together, then run $\ell$ rounds, each a simultaneous layer, plus $\le K$ individual rounds on the prefix, and add errors one truncation per round.
- S2.2.1: Call an axis long if it has $\ell$ address bits and short if $\ell-1$; put $b=(\ell-1)\bmod K$ and $q=\lfloor(\ell-1)/K\rfloor$.
  Source: "Call an axis long if $a_i=\ell$ and short if" (paper)
  > Its opposite procedure consumes that order and has exact counterpart $F_{\boldsymbol t}^+B^{-1}L^{-1}$. Each procedure has error less than $\sqrt2\ell\,2^{-p}$, returns disk grid coefficients in the same component format, and costs \begin{equation} O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right). \label{eq:synthetic-transform-cost} \end{equation} Both layout construction and final restoration are charged in this bound. The forward procedure may retain its output layout for a pointwise product and the following opposite procedure. \end{lemma} \begin{proof} Put $D=d-1$ and write $a_i=\log_2t_i$. The supplied encoding has $2w=\Theta(p)$ bits per coefficient, so the logical bit volume is $\Theta(Tp)$. Call an axis long if $a_i=\ell$ and short if $a_i=\ell-1$. Name the original bit slots of axis $i$ by $(i,h)$, $a_i-1\geq h\geq0$. Initially these slots are in axis order and, within each axis, in decreasing $h$. The coefficients of each polynomial form a contiguous suffix. Put \[ b=(\ell-1)\bmod K, \qquad q=\lfloor(\ell-1)/K\rfloor. \] Form a list of the slots to move to a prefix. First list $(i,\ell-1)$ for the length-$2^\ell$ axes in increasing $i$. Then list $(i,h)$ for $h=b-1,\ldots,0$, and within each $h$ in increasing $i$; this second list is empty if $b=0$. Move each listed slot immediately after the prefix already formed, leaving all other slots in their relative order. There are at most $D(b+1)=O(dK)$ listed slots, so the moves cos
- S2.2.2: At most $D(b+1)=O(dK)$ listed slots are moved to a prefix, so the moves cost $O(TpdK)$.
  Source: "listed slots, so the moves cost $O(TpdK)$." (paper)
  > long if $a_i=\ell$ and short if $a_i=\ell-1$. Name the original bit slots of axis $i$ by $(i,h)$, $a_i-1\geq h\geq0$. Initially these slots are in axis order and, within each axis, in decreasing $h$. The coefficients of each polynomial form a contiguous suffix. Put \[ b=(\ell-1)\bmod K, \qquad q=\lfloor(\ell-1)/K\rfloor. \] Form a list of the slots to move to a prefix. First list $(i,\ell-1)$ for the length-$2^\ell$ axes in increasing $i$. Then list $(i,h)$ for $h=b-1,\ldots,0$, and within each $h$ in increasing $i$; this second list is empty if $b=0$. Move each listed slot immediately after the prefix already formed, leaving all other slots in their relative order. There are at most $D(b+1)=O(dK)$ listed slots, so the moves cost $O(TpdK)$. A descriptor records the physical position of every named slot. The part of each axis left outside the prefix now consists of $q$ consecutive $K$-bit chunks.
- S2.2.3: The remaining slots form $q$ consecutive $K$-bit chunks per axis; reordering them to put equal-index chunks of all axes together takes at most $Dq-1$ exchanges of width-$K$ chunks, each costing $O(TpK^\tau)$.
  Source: "exchanges of width-$K$ address chunks, even when the chunks are" (paper)
  > Number the axes by $i$ and their chunks, from high to low, by $j$. The remaining physical order changes from \[ (1,1),(1,2),\ldots,(1,q),(2,1),\ldots,(D,q) \quad\hbox{to}\quad (1,1),(2,1),\ldots,(D,1),(1,2),\ldots,(D,q). \] To obtain this order, scan its target positions from left to right. At each position except the last, exchange the chunk currently there with the required chunk if they differ. This uses at most $Dq-1$ exchanges of width-$K$ address chunks, even when the chunks are nonadjacent. Each costs $O(TpK^\tau)$, so all these exchanges cost \[ O\bigl(Tp\,DqK^\tau\bigr) =O\bigl(Tp\,pK^{\tau-1}\bigr). \] These prefix moves and chunk exchanges define $L$. We use the same letter for its induced record permutation: a record at address $x$ moves to address $Lx$, while its polynomial suffix stays intact. Recording the inverse operations in reverse order gives $L^{-1}$ with the same cost.
- S2.2.4: Since $DqK\le d\ell=O(p)$, the exchanges cost $O(Tp\,DqK^\tau)=O(Tp\,pK^{\tau-1})$.
  Source: "=O\bigl(Tp\,pK^{\tau-1}\bigr)." (paper)
  > Number the axes by $i$ and their chunks, from high to low, by $j$. The remaining physical order changes from \[ (1,1),(1,2),\ldots,(1,q),(2,1),\ldots,(D,q) \quad\hbox{to}\quad (1,1),(2,1),\ldots,(D,1),(1,2),\ldots,(D,q). \] To obtain this order, scan its target positions from left to right. At each position except the last, exchange the chunk currently there with the required chunk if they differ. This uses at most $Dq-1$ exchanges of width-$K$ address chunks, even when the chunks are nonadjacent. Each costs $O(TpK^\tau)$, so all these exchanges cost \[ O\bigl(Tp\,DqK^\tau\bigr) =O\bigl(Tp\,pK^{\tau-1}\bigr). \] These prefix moves and chunk exchanges define $L$. We use the same letter for its induced record permutation: a record at address $x$ moves to address $Lx$, while its polynomial suffix stays intact. Recording the inverse operations in reverse order gives $L^{-1}$ with the same cost.
- S2.2.5: The simultaneous-layer procedure applies at cost $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.
  Source: "$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total." (paper)
  > For a position $h$ in the remaining chunks, the selected bit has offset $(h-b)\bmod K$, counted from the least significant bit, in each of the $D$ consecutive chunks with the same chunk index $j$. Let $n_P$ and $n_S$ be the numbers of record-address bits before and after that group. Every combination of those bits occurs, so the layer sees the complete address set \[ [P]\times[2^K]^D\times[S],\qquad P=2^{n_P},\quad S=2^{n_S},\quad n_P+DK+n_S=\sum_i a_i\leq D\ell=O(p). \] Thus its record count is $PS2^{DK}=M$ and $\log_2(2M)\leq(C_\ell+1)p=C_Mp$. The current transform parameters supply $p,d,r,K,w$, and the round determines $D,P,S$ and the selected offset $\rho$. Encode these values as the header $\mathcal E$ of Proposition~\ref{prop:simultaneous-layer}. The same fixed descriptor bound covers every axis choice and round. Indeed $|\Gamma(v)|\leq2\log_2v+1$, and $\ell+n_P+n_S\leq d\ell\leq C_\ell p$. Also $d,D\leq\max\{C_\ell,1\}p$, $K,\rho+1\leq p$, and $w\leq C_wp$. Adding the nine code lengths therefore gives \[ |\mathcal E| \leq 2C_\ell p+12\log_2p+ 4\log_2\max\{C_\ell,1\}+2\log_2C_w+9 \leq C_{\rm desc}p. \] The last inequality uses $p\geq1$, $\log_2p\leq p$, and $\log_2x\leq x$ for $x\geq1$. This is the descriptor passed to the layer; the longer table locating named slots remains separate for the transform's address calculations. The simultaneous-layer procedure therefore applies at cost $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.
- S2.2.6: There are at most $b+1\le K$ individual rounds on prefix slots, each $O(Tpd)$, giving $O(TpdK)$.
  Source: "most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$." (paper)
  > In a round on prefix slots, process the participating bits individually. Temporarily move one such bit immediately before the polynomial suffix. In each now adjacent pair, buffer the first record and scan it with the second, writing the half-sums and half-differences to two work tapes. Append the half-sum record and then the half-difference record, and reverse the bit move after all pairs are processed. Including head returns, the work is $O(rp)$ per pair and $O(Tp)$ for the moves and scans at coefficient width $O(p)$. That width suffices without truncating between axes: after $s\leq D$ individual $H_0$ factors, the coefficients are exact dyadics on the $2^{-(p+s)}$ grid and still lie in the disk. A temporary sum has modulus at most two and needs only a constant number of extra integer bits. Hence $p+D+O(1)=O(p)$ bits per component suffice, since $D\leq d$ and $d\ell=O(p)$. Complete the combined monomial exactly and apply $Q_p$ once at the end of the round. Write the resulting disk-grid numerators in the supplied $w$-bit component format. Their magnitudes are at most $2^p$, so this takes one linear scan within the same bound. In an opposite round on prefix slots the inverse monomial comes first and preserves the grid and disk, so the same width bound holds for its individual factors. There are at most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$.
- S2.2.7: Truncation is odd and acts separately on each real and imaginary part, so $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$ and each round truncates once after the exact contraction.
  Source: "J_EQ_p(\mathcal H z)=Q_p(J_E\mathcal H z)." (paper)
  > For a forward round on a group of $D$ chunks, the layer call returns $Q_p(\mathcal H z)$ and the next operation is $J_E$. Truncation toward zero is odd and acts separately on every real and imaginary part. Since $J_E$ is a signed coefficient permutation, it follows that \[ J_EQ_p(\mathcal H z)=Q_p(J_E\mathcal H z). \] Thus the actual forward call sequence returns exactly the result of truncating once after the exact contraction round. In the opposite direction, $J_E^{-1}$ first preserves the disk grid, and the layer call returns $Q_p(\mathcal HJ_E^{-1}z)$ directly. The rounds on prefix slots have the same forms, with one truncation, by their exact evaluation above. A contraction does not increase the norm of the difference between the computed and exact arrays; the single truncation then adds less than $\sqrt2\,2^{-p}$ by \eqref{eq:transform-truncate}. Both the contraction and truncation preserve the disk. Starting with zero error, at most $\ell$ rounds therefore give the claimed error and disk bounds. The layout permutations are isometries and add no numerical error.
- S2.2.8: Starting with zero error, at most $\ell$ rounds, each adding less than $\sqrt2\,2^{-p}$ through a contraction, give error less than $\sqrt2\ell\,2^{-p}$; layout permutations add no error.
  Source: "zero error, at most $\ell$ rounds therefore" (paper)
  > For a forward round on a group of $D$ chunks, the layer call returns $Q_p(\mathcal H z)$ and the next operation is $J_E$. Truncation toward zero is odd and acts separately on every real and imaginary part. Since $J_E$ is a signed coefficient permutation, it follows that \[ J_EQ_p(\mathcal H z)=Q_p(J_E\mathcal H z). \] Thus the actual forward call sequence returns exactly the result of truncating once after the exact contraction round. In the opposite direction, $J_E^{-1}$ first preserves the disk grid, and the layer call returns $Q_p(\mathcal HJ_E^{-1}z)$ directly. The rounds on prefix slots have the same forms, with one truncation, by their exact evaluation above. A contraction does not increase the norm of the difference between the computed and exact arrays; the single truncation then adds less than $\sqrt2\,2^{-p}$ by \eqref{eq:transform-truncate}. Both the contraction and truncation preserve the disk. Starting with zero error, at most $\ell$ rounds therefore give the claimed error and disk bounds. The layout permutations are isometries and add no numerical error.
- S2.2.9: The exact forward operator is $LBF_{\boldsymbol t}^-$ and the exact opposite operator is $F_{\boldsymbol t}^+B^{-1}L^{-1}$.
  Source: "(L\mathcal D_-L^{-1})L=LB F_{\boldsymbol t}^-," (paper)
  > It remains to identify the order of the full procedures. Before relocating slots, write $\mathcal D_-=BF_{\boldsymbol t}^-$ and $\mathcal D_+=F_{\boldsymbol t}^+B^{-1}$ for the exact logical forward and opposite procedures. Executing each operation on named slots after $L$ conjugates it by $L$. The forward procedure first moves the records by $L$, whereas the opposite procedure restores them by $L^{-1}$ after its reverse arithmetic. Their full exact operators are \[ (L\mathcal D_-L^{-1})L=LB F_{\boldsymbol t}^-, \qquad L^{-1}(L\mathcal D_+L^{-1}) =F_{\boldsymbol t}^+B^{-1}L^{-1}. \] In particular, the forward entry with frequency address $j$ is stored at $L(Bj)$. The reverse arithmetic consumes the frequency branch coordinates and outputs the normalized opposite transform indexed by the original axis coordinates, which are still in layout $L$. The factor $B^{-1}$ is realized by that arithmetic; the final charged movement $L^{-1}$ restores axis-major physical order. \end{proof}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.1 (on [Retained frequency order](frequency-order.md)): The synthetic transform $F_t^-$ over $\mathcal R_r=\mathbb C[y]/(y^r+1)$, with roots of unity $\omega_t=y^{2r/t}$, is computed by decimation in frequency with outputs written in bit-reversed order, $B_tF_t^-$; the pointwise product keeps this order and the reverse procedure computes $F_t^+B_t^{-1}$, so no reordering is executed.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Fixed-point Gaussian dyadic records](fixed-point.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Synthetic polynomial transform](synthetic-transform.md): A transform over the ring modulo y^r + 1 whose roots of unity are powers of y, so every twiddle multiplication is a signed shift of a coefficient list.
  Shown as: Tape layout for synthetic transforms *<predicate>* Synthetic polynomial transform
- [Simultaneous butterfly layer](simultaneous-layer.md): The second tape procedure: applying H₀ coefficientwise on the same bit of up to d address chunks in time O(V·d^λ′) for a fixed λ′ < 1, instead of d passes.
  Shown as: Tape layout for synthetic transforms *<predicate>* Simultaneous butterfly layer
- [Fast address-chunk interchange](address-interchange.md): The first tape procedure: exchanging two disjoint equal-width address fields of u digits in time O(V·u^τ) for a fixed τ < 1, using XOR combinations of intermediate data.
  Shown as: Tape layout for synthetic transforms *<predicate>* Fast address-chunk interchange
- [Retained frequency order](frequency-order.md): The forward synthetic transform writes its outputs in bit-reversed order, the pointwise product keeps that order, and the opposite transform consumes it, so no reordering is executed.
  Shown as: Tape layout for synthetic transforms *<predicate>* Retained frequency order

## Pages that build on this one

- Convolution from the retained transform layout: Convolution over the ring modulo y^r + 1 on the remaining axes by two forward synthetic transforms, pointwise polynomial products and the opposite transform, normalized by 1/(rM).

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Elementary stream operations](stream-ops.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](chirp.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Two-point kernel C](phase-kernel.md)
- [Binary phase frames](phase-frames.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "Transform layout and cost" (paper)

  > \begin{lemma}[Transform layout and cost] \label{lem:synthetic-transform-cost} Fix the rational parameters and positive comparison constants $a_d\leq b_d$, $a_r\leq b_r$ of Proposition~\ref{prop:simultaneous-layer}. Fix constants $C_\ell>0$ and $C_w>1$, and choose the layer constants once as \[ C_M=C_\ell+1,\qquad C_{\rm desc}=32(C_\ell+C_w+1). \] Use these constants and $C_w$ in Proposition~\ref{prop:simultaneous-layer}. These fixed choices determine a cutoff $p_1$, one fixed-tape procedure, and an implicit time constant with the following guarantee. For every choice of positive integers $p,d,r$ with $p\geq p_1$ and \[ a_dp^\epsilon\leq d\leq b_dp^\epsilon,\qquad 2^{a_rp/d}\leq r\leq2^{b_rp/d}, \] suppose $d\geq2$ and $r=2^\ell$ with an integer $2\leq\ell<p$, and require \[ d\ell\leq C_\ell p,\qquad 1\leq K=\lfloor d^c\rfloor\leq\ell-1. \] Let $t_i\in\{2^{\ell-1},2^\ell\}$ for $1\leq i\leq d-1$, put $M=\prod_{i=1}^{d-1}t_i$ and $T=rM$, and let $w$ be an integer with $p+2\leq w\leq C_wp$. The cutoff and time constant are independent of $p,d,r$, these axis choices, the round headers constructed from them, and $w$ within the displayed bounds.

- "A layout on which the parallel layers apply" (paper)

  > \subsection{A layout on which the parallel layers apply}


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

Write the body to `exegenius/tasks/0035-write-transform-layout.answer.md` and the JSON to `exegenius/tasks/0035-write-transform-layout.answer.json`, then run `exegenius submit 0035-write-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0035-write-transform-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
