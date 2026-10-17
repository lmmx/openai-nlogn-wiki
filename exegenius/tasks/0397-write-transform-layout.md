# exegenius task 0397-write-transform-layout

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
- Butterflies and the fast transform (also: transform levels)
- Multidimensional transforms
- Chinese-remainder address map (also: Agarwal–Cooley map)
- Gaussian resampling
- Bluestein chirp identity (also: chirp transform)
- Retained permutation cancellation
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Retained frequency order
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records (also: Z[i,1/2])
- Error tracking and exact recovery (also: synthetic transform error, source transform error)
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
- Recursive power saving
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Fast address-chunk interchange (also: chunk swap, tape interchange, costly recursive primitive)
- Two-point kernel C (also: phase network kernel)
- Binary phase frames
- Packed selected-bit addition (also: exceptional addresses)
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Parameter and prime-length choice
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
- Cartesian products and multi-index arrays (also: multidimensional arrays, row-major order, lexicographic order, mixed-radix index, index tuples, array stored on a tape, rectangle, columns)
- Directed acyclic graphs and networks of gates (also: circuit, DAG, wire, gate, edges and vertices, fan-in)
- Summation, geometric series and induction (also: geometric sum, proof by induction, summation notation, telescoping sum)
- Rounding to the nearest integer and exactness (also: rounding, truncation, round to nearest, rational numbers, dyadic rational)
- Multitape Turing machine running time (also: tape head movement, scanning a tape, linear-time pass over a tape, time complexity of a Turing machine, worst-case running time)
- Integer exponentials and tuple notation (also: powers of two, tensor power notation, exponent of a constant, fixed rational exponents)
- Contractions and bilinear contractions (also: contraction, bilinear contraction)
- Tensor products of subspaces (also: tensor product of subspaces, tensor product)

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

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $y$ (ring variable), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The indeterminate of the polynomials; it satisfies y^r = -1 in the ring.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The number of complex coefficients in a polynomial of the ring, always a power of two.
- $n$ (bit length), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): The number of bits in each of the two integers being multiplied.
- $\kappa$ (power saving), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant, the amount by which the exponent of the logarithm is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the grid on which stored values lie.
- $k$ (depth), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations in sequence since the layer began that produced a value.
- $\Delta$ (reserved extra bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the maximal depth reached in the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.
- $X$ (first data bank), bound on [Linear exchange network with restored scratch wires](exchange-network.md): One of the two data banks, with entries X_a.
- $Y$ (second data bank), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The other data bank, with entries Y_a.
- $a$ (bank index), bound on [Linear exchange network with restored scratch wires](exchange-network.md): A triple of three-element subsets of [h] indexing the entries of the banks.
- $h$ (ground-set size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of the ground set [h] whose three-element subsets index the banks.
- $\mathcal T$ (triple set), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The set of three-element subsets of [h].
- $v$ (number of triples), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of three-element subsets of [h].
- $N$ (bank size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of values in each data bank.
- $m$ (label-space dimension), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The dimension of the label space used on later pages.
- $I$ (invocation count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of invocations over all three stages.
- $z_{\rm b}$ (bit neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the bit construction.
- $z_{\rm c}$ (complex neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the complex construction.
- $c_{\rm b}$ (bit central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the bit network.
- $W_{\rm c}$ (complex wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the complex network.
- $R$ (scalar ring), bound on [Frames on wire arrays](array-frames.md): The ring of scalars carried by the wires.
- $\Omega$ (address set), bound on [Frames on wire arrays](array-frames.md): The finite set of addresses indexing every array.
- $\mathsf S_\Omega$ (pointwise network), bound on [Frames on wire arrays](array-frames.md): The network acting on all the wire arrays together, applying every gate at each address.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): The invertible R-linear operator on arrays assigned to a source, gate or sink v.
- $D_{\rm in}$ (input frame), bound on [Frames on wire arrays](array-frames.md): The direct sum of the source frames over the input roles.
- $D_{\rm out}$ (output frame), bound on [Frames on wire arrays](array-frames.md): The direct sum of the sink frames over the output roles.
- $\rho$ (role permutation), bound on [Frames on wire arrays](array-frames.md): The map sending each input role to its output role.
- $\varepsilon_w$ (route sign), bound on [Frames on wire arrays](array-frames.md): The scalar sign of the route from input role w.
- $t$ (gate fan-in), bound on [Frames on wire arrays](array-frames.md): The number of input arrays of a gate.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each sequence being convolved.
- $d$ (axis count), bound on [Cyclic convolution](convolution.md): The number of axes of the underlying cyclic convolution.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The number of addresses along cyclic axis i.
- $M$ (address count), bound on [Cyclic convolution](convolution.md): The number of addresses of an array, the product of the axis lengths.
- $T$ (coefficient count), bound on [Cyclic convolution](convolution.md): The number of complex coefficients in an array.
- $\pi$ (index permutation), bound on [Cyclic convolution](convolution.md): A permutation of the indices of an array.
- $F$ (Fourier transform), bound on [Cyclic convolution](convolution.md): The normalized discrete Fourier transform of length q.
- $F^+$ (opposite transform), bound on [Cyclic convolution](convolution.md): The Fourier transform with the opposite sign in the exponent.
- $u$ (first input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The first of the two n-bit integers being multiplied.
- $u'$ (second input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The second of the two n-bit integers being multiplied.
- $b$ (digit bits), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in one radix-2^b digit.
- $S$ (convolution length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The length of the cyclic convolution, between T/2 and T, a product of distinct odd primes.
- $x$ (polynomial variable), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The variable of the digit polynomials, evaluated at 2^b to recover the integers.
- $u_i$ (digit of u), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The i-th radix-2^b digit of u, an integer from 0 to 2^b-1.
- $u'_k$ (digit of u'), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The k-th radix-2^b digit of u', an integer from 0 to 2^b-1.
- $c_j$ (product coefficient), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The coefficient of x^j in the product of the two digit polynomials.
- $T$ (padded length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of coefficients of the padded array, a power of two between 4n/b and 8n/b.
- $q$ (digit count), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of radix-2^b digits in each input.
- $d$ (axis count), bound on [Phase twist](phase-twist.md): The number of axes of the arrays f and g.
- $f$ (first array), bound on [Phase twist](phase-twist.md): A complex array with d axes, the last of length r.
- $g$ (second array), bound on [Phase twist](phase-twist.md): The second complex array, with the same shape as f.
- $x_d$ (last axis variable), bound on [Phase twist](phase-twist.md): The variable of the last cyclic axis.
- $\mathcal R_r$ (negacyclic ring), bound on [Phase twist](phase-twist.md): The ring of polynomials in y modulo y^r+1 over the complex numbers.
- $\zeta$ (twist phase), bound on [Phase twist](phase-twist.md): The complex number e^{\pi i/r}, with \zeta^r=-1.
- $\Theta$ (twist map), bound on [Phase twist](phase-twist.md): The ring isomorphism from C[x_d]/(x_d^r-1) to R_r sending x_d to \zeta y.
- $k$ (coefficient index), bound on [Phase twist](phase-twist.md): The index of a coefficient along the last axis (here not a depth).
- $l$ (second coefficient index), bound on [Phase twist](phase-twist.md): The index of a second coefficient along the last axis.
- $j$ (wrapped position), bound on [Phase twist](phase-twist.md): The position in 0..r-1 of a product term after reduction.
- $h$ (wrap indicator), bound on [Phase twist](phase-twist.md): Zero or one, the number of times the index k+l wraps past r.
- $M$ (line count), bound on [Phase twist](phase-twist.md): The number of lines along the last axis, T/r.
- $\iota$ (line-to-record map), bound on [Phase twist](phase-twist.md): Reads each line along the last axis as a polynomial in y, giving an array of M records in R_r.
- $D_\pm$ (twist and untwist), bound on [Phase twist](phase-twist.md): Multiplication of entry k of each line by \zeta^{\pm k}.
- $\mathcal M_r$ (ring convolution), bound on [Phase twist](phase-twist.md): The normalized convolution of the first d-1 axes over R_r, dividing by T.
- $\mathcal M_{\mathbb C}$ (complex convolution), bound on [Phase twist](phase-twist.md): The normalized complex cyclic convolution, equal to f*g/T.
- $\|f\|$ (sup norm), bound on [Phase twist](phase-twist.md): The largest modulus of a scalar coefficient of f.
- $q$ (sequence length), bound on [Discrete Fourier transform](dft.md): The number of entries of a sequence.
- $u$ (input sequence), bound on [Discrete Fourier transform](dft.md): A sequence of q complex numbers.
- $\omega$ (primitive root), bound on [Discrete Fourier transform](dft.md): The primitive q-th root of unity e^{2 pi i/q}.
- $v$ (second sequence), bound on [Discrete Fourier transform](dft.md): A second sequence of length q (not an integer input).
- $t$ (transform length), bound on [Butterflies and the fast transform](butterfly.md): The length of the transform, a power of two.
- $z_k$ (input value), bound on [Butterflies and the fast transform](butterfly.md): The input value at position k.
- $\omega_t$ (twiddle root), bound on [Butterflies and the fast transform](butterfly.md): The primitive t-th root of unity e^{2 pi i/t}.
- $m$ (output index), bound on [Butterflies and the fast transform](butterfly.md): The index of an output of the transform.
- $j$ (input position), bound on [Butterflies and the fast transform](butterfly.md): The summation index running over input positions.
- $b$ (lowest bit), bound on [Butterflies and the fast transform](butterfly.md): The lowest bit of the output index m.
- $H_0$ (butterfly), bound on [Butterflies and the fast transform](butterfly.md): The two-point averaging and differencing step.
- $h$ (remaining index), bound on [Butterflies and the fast transform](butterfly.md): The index m with its lowest bit removed.
- $t$ (transform length), bound on [Synthetic polynomial transform](synthetic-transform.md): The number of ring elements along one axis, a power of two dividing 2r.
- $e$ (two-adic exponent), bound on [Synthetic polynomial transform](synthetic-transform.md): The exponent of 2 in j when j is written as 2^e times an odd number.
- $V$ (volume), bound on [Elementary stream operations](stream-ops.md): The number of digits an array stores.
- $\beta$ (radix), bound on [Elementary stream operations](stream-ops.md): The number of values one digit can take.
- $W$ (stream count), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams that rows are dealt into.
- $P$ (prefix count), bound on [Elementary stream operations](stream-ops.md): The number of prefix values in the array indexed by [P]x[R]x[B].
- $R$ (row count), bound on [Elementary stream operations](stream-ops.md): The number of rows in the array indexed by [P]x[R]x[B].
- $B$ (row length), bound on [Elementary stream operations](stream-ops.md): The number of entries per row.
- $\boldsymbol j$ (position), bound on [Bluestein chirp identity](chirp.md): A position in an array, one index per axis.
- $\boldsymbol t$ (axis lengths), bound on [Bluestein chirp identity](chirp.md): The tuple of the even axis lengths.
- $s_i$ (coprime multiplier), bound on [Bluestein chirp identity](chirp.md): An integer coprime to the axis length t_i.
- $\boldsymbol k$ (input position), bound on [Bluestein chirp identity](chirp.md): An input position of the transform.
- $\boldsymbol f$ (frequency), bound on [Bluestein chirp identity](chirp.md): The frequency labelling an output entry.
- $F_{\boldsymbol t}$ (normalized transform), bound on [Bluestein chirp identity](chirp.md): The normalized discrete Fourier transform with axis lengths t.
- $Q$ (target permutation), bound on [Bluestein chirp identity](chirp.md): The permutation of the output that puts at position j the entry of frequency (-s_i j_i)_i.
- $a$ (chirp), bound on [Bluestein chirp identity](chirp.md): The chirp, a phase quadratic in the position.
- $N$ (factor bit length), bound on [Established O(n log n) multiplier](hvdh-multiplier.md): The number of bits in each of the two integers given to the established multiplier.
- $B_0$ (packing base), bound on [Signed packing](signed-packing.md): The base 2^{4p} at which the polynomials are evaluated.
- $A_u$ (signed evaluation integer), bound on [Signed packing](signed-packing.md): The integer obtained by evaluating the integer-coefficient polynomial u at B_0.
- $\gamma_j$ (carry), bound on [Signed packing](signed-packing.md): The carry, in {-1,0}, into block j when forming A_u.
- $d_j$ (block), bound on [Signed packing](signed-packing.md): The residue of u_j plus the carry modulo B_0, the j-th block of 4p bits of A_u.
- $h_j$ (product coefficient), bound on [Signed packing](signed-packing.md): The coefficient of y^j in the ordinary product h=ac of integer polynomials.
- $\rho_j$ (extraction carry), bound on [Signed packing](signed-packing.md): The carry into block j during extraction, in {0,1}.
- $H_j$ (reduced coefficient), bound on [Signed packing](signed-packing.md): The Gaussian integer coefficient of y^j after reduction modulo y^r+1.
- $q$ (prime radix), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The radix of the stored digits, a prime (not a sequence length).
- $b$ (field digit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of base-q digits of a field.
- $Q$ (field value count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of values a field can take.
- $y$ (field value), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The value of the target field, an integer from 0 to Q-1 (not the ring variable).
- $a$ (offset), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The offset added to the target field, prepared from the control values.
- $B$ (suffix digit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of digits following the target field.
- $c$ (scaling multiplier), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed positive integer prime to q by which the field is multiplied.
- $j$ (wrap count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of times cy wraps past Q.
- $y'$ (scaled position), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The position cy - jQ to which the block at position y is sent.
- $c'$ (unit denominator), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The positive integer denominator of a rational unit, prime to q.
- $q$ (field base), bound on [Matrix shear by triangular factorization](matrix-shear.md): A fixed odd prime, the base of the digits.
- $b$ (digits per field), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of base-q digits in one field.
- $a$ (rank), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rank of the matrix A.
- $m$ (fields per group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of fields in each of the groups H and D.
- $I$ (identity matrix), bound on [Two-point kernel C](phase-kernel.md): The 2x2 identity matrix.
- $X$ (bit flip), bound on [Two-point kernel C](phase-kernel.md): The 2x2 matrix swapping the two entries of a pair.
- $a$ (kernel constant), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1+i)/2.
- $b$ (kernel coefficient), bound on [Two-point kernel C](phase-kernel.md): The complex coefficient (1-i)/2 of the bit flip in the kernel.
- $C$ (two-point kernel), bound on [Two-point kernel C](phase-kernel.md): The matrix aI + bX.
- $\mathsf S$ (phase matrix), bound on [Two-point kernel C](phase-kernel.md): The diagonal matrix diag(1, i) multiplying the second entry of a pair by i.
- $H_0$ (averaging step), bound on [Two-point kernel C](phase-kernel.md): The matrix of the two-point averaging and differencing step.
- $H$ (Hadamard matrix), bound on [Two-point kernel C](phase-kernel.md): The normalized Hadamard matrix sqrt(2) H_0.
- $L$ (linear map), bound on [Contractions and bilinear contractions](contraction-maps.md): A linear map whose norm bound is being defined.
- $\mathcal M$ (bilinear map), bound on [Contractions and bilinear contractions](contraction-maps.md): A map linear in each of its two operands.
- $u'$ (computed input), bound on [Contractions and bilinear contractions](contraction-maps.md): The computed input that replaces the exact input u.
- $f'$ (computed first operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The computed operand replacing f.
- $g'$ (computed second operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The computed operand replacing g.
- $F_q$ (normalized transform), bound on [Contractions and bilinear contractions](contraction-maps.md): The normalized discrete Fourier transform on sequences of q entries.
- $f$ (first operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The first operand of the bilinear map.
- $g$ (second operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The second operand of the bilinear map.
- $i$ (axis index), bound on [Multidimensional transforms](multidim-transform.md): An index of one axis of the array, between 1 and d.
- $q_i$ (positions along axis), bound on [Multidimensional transforms](multidim-transform.md): The number of positions along axis i.
- $s_i$ (prime axis length), bound on [Multidimensional transforms](multidim-transform.md): The source length of axis i, a prime length of the integer product.
- $p$ (fractional bits), bound on [Multidimensional transforms](multidim-transform.md): The number of fractional bits of the stored values.
- $\alpha$ (resampling parameter), bound on [Multidimensional transforms](multidim-transform.md): An integer resampling parameter with 2 <= alpha < sqrt p.
- $\delta$ (exponent slack), bound on [Multidimensional transforms](multidim-transform.md): A fixed constant with 0 < delta < 1/8 that sets the slack in the exponent of p in the time bound.
- $P_{s_i}$ (source permutation), bound on [Multidimensional transforms](multidim-transform.md): The index permutation of the source axis i.
- $A_i$ (input map), bound on [Multidimensional transforms](multidim-transform.md): The linear input map of axis i in the resampling identity.
- $\boldsymbol s$ (source axis lengths), bound on [Multidimensional transforms](multidim-transform.md): The tuple of source axis lengths.
- $\gamma$ (scalar exponent), bound on [Multidimensional transforms](multidim-transform.md): The total exponent of the scalar power of two in the tensored identity.
- $\boldsymbol t$ (padded axis lengths), bound on [Multidimensional transforms](multidim-transform.md): The tuple of padded power-of-two axis lengths.
- $R$ (source permutation tensor), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the source index permutations P_{s_i} (not the scalar ring).
- $Q$ (padded permutation tensor), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the padded index permutations P_{t_i}.
- $\mathcal A$ (input contraction), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the axis input maps A_i.
- $\mathcal B_0$ (output contraction), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the axis output maps B_{0,i}.
- $d$ (axis count), bound on [Chinese-remainder address map](crt-map.md): The number of prime cyclic axes, with no coefficient axis counted.
- $i$ (axis index), bound on [Chinese-remainder address map](crt-map.md): The index of an axis, from 1 to d.
- $s_i$ (axis length), bound on [Chinese-remainder address map](crt-map.md): The length of source axis i, pairwise coprime with the other axis lengths.
- $P_i$ (prefix product), bound on [Chinese-remainder address map](crt-map.md): The product of the lengths of the axes before axis i.
- $\mu_i$ (exponent), bound on [Chinese-remainder address map](crt-map.md): The inverse of P_i modulo s_i, the exponent of x_i in the image of x.
- $\Phi$ (address map), bound on [Chinese-remainder address map](crt-map.md): The algebra isomorphism from the cyclic ring of length S to the product of cyclic rings on the axes, sending x to the product of x_i^{mu_i}.
- $x_i$ (axis variable), bound on [Chinese-remainder address map](crt-map.md): The polynomial variable of axis i.
- $a_j$ (mixed-radix digit), bound on [Chinese-remainder address map](crt-map.md): The digit of the coefficient index k in position j, with 0 <= a_j < s_j.
- $b_i$ (axis coordinate), bound on [Chinese-remainder address map](crt-map.md): The coordinate along axis i of the image of x^k.
- $\ell$ (address bits), bound on [Chinese-remainder address map](crt-map.md): The number of address bits of an axis of length r.
- $T$ (padded record count), bound on [Chinese-remainder address map](crt-map.md): The number of padded records, the product of the padded axis lengths.
- $\tau$ (interchange exponent), bound on [Chinese-remainder address map](crt-map.md): A fixed exponent below 1 in the cost of the chunk interchange.
- $L$ (address width), bound on [Chinese-remainder address map](crt-map.md): The number of address bits of each of two equal-width axes being interchanged.
- $t_i$ (padded axis length), bound on [Chinese-remainder address map](crt-map.md): The length of axis i after padding with zero records, a power of two between r/2 and r.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The number of entries of the sequence whose transform is re-expressed.
- $\theta$ (length gap), bound on [Gaussian resampling](gaussian-resampling.md): The relative gap t/s-1 between the padded and source lengths.
- $P_s$ (source permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation (P_s u)_j = u_{tj} of length-s vectors.
- $P_t$ (target permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation (P_t v)_k = v_{-sk} of length-t vectors.
- $A$ (input contraction), bound on [Gaussian resampling](gaussian-resampling.md): The linear contraction from length-s to length-t vectors in the resampling identity.
- $B_0$ (output contraction), bound on [Gaussian resampling](gaussian-resampling.md): The linear contraction from length-t to length-s vectors in the resampling identity.
- $\mathsf S$ (source resampling map), bound on [Gaussian resampling](gaussian-resampling.md): Harvey and van der Hoeven's Gaussian map from length-s to length-t vectors with wide smear.
- $\mathsf T$ (target resampling map), bound on [Gaussian resampling](gaussian-resampling.md): Harvey and van der Hoeven's Gaussian map from length-s to length-t vectors with narrow smear.
- $q_j$ (nearest index), bound on [Gaussian resampling](gaussian-resampling.md): The integer nearest tj/s.
- $\beta_j$ (rounding offset), bound on [Gaussian resampling](gaussian-resampling.md): The offset tj/s - q_j from the nearest integer.
- $C$ (coordinate selection), bound on [Gaussian resampling](gaussian-resampling.md): The map from length-t to length-s vectors that selects coordinates q_j.
- $\mathsf D$ (Gaussian rescaling), bound on [Gaussian resampling](gaussian-resampling.md): The diagonal map multiplying u_j by e^{pi alpha^2 beta_j^2}.
- $N$ (near-identity map), bound on [Gaussian resampling](gaussian-resampling.md): The map C T D, whose diagonal entries are exactly 1.
- $E$ (off-diagonal part), bound on [Gaussian resampling](gaussian-resampling.md): The map N - I.
- $K$ (series terms), bound on [Gaussian resampling](gaussian-resampling.md): The number of Neumann series terms kept.
- $\mathbb D_p$ (p-bit grid), bound on [Gaussian resampling](gaussian-resampling.md): The grid of fixed-point Gaussian dyadic records with p fractional bits.
- $t$ (padded length), bound on [Gaussian resampling](gaussian-resampling.md): The nearby larger power-of-two length through which the transform is computed.
- $\alpha$ (width parameter), bound on [Gaussian resampling](gaussian-resampling.md): The integer width parameter of the Gaussian weights, with 2 <= alpha < sqrt p.
- $S$ (source entry count), bound on [Retained permutation cancellation](retained-permutations.md): The number of entries of the source array, the product of the source axis lengths.
- $T$ (padded entry count), bound on [Retained permutation cancellation](retained-permutations.md): The number of entries of the padded box, the product of the padded axis lengths.
- $R$ (source permutation), bound on [Retained permutation cancellation](retained-permutations.md): The tensor product of the source axis permutations; it is a permutation, not the scalar ring.
- $B_0$ (output map), bound on [Retained permutation cancellation](retained-permutations.md): The linear contraction applied after the power-of-two transform in the one-axis resampling identity; unrelated to the packing base.
- $\beta$ (unit), bound on [Retained permutation cancellation](retained-permutations.md): A unit modulo q, used to define the index permutation R_beta.
- $w$ (summation index), bound on [Retained permutation cancellation](retained-permutations.md): The index of summation in the Fourier sum.
- $\nu$ (setup exponent), bound on [Retained permutation cancellation](retained-permutations.md): A fixed exponent such that the setup work per line is O(p^nu).
- $u$ (first array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array, not an integer being multiplied.
- $v$ (second array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array, not an integer being multiplied.
- $a$ (round count), bound on [Retained frequency order](frequency-order.md): The number of rounds of the transform, a=log_2 t.
- $j$ (output index), bound on [Retained frequency order](frequency-order.md): The position of an output of the transform.
- $s$ (completed rounds), bound on [Retained frequency order](frequency-order.md): The number of rounds completed so far.
- $B_t$ (bit-reversal permutation), bound on [Retained frequency order](frequency-order.md): The permutation moving the entry at j to rev_a(j).
- $\mathcal H$ (parallel butterfly), bound on [Retained frequency order](frequency-order.md): The parallel butterfly applying H_0 on every participating axis in one round.
- $J_E$ (recordwise monomial), bound on [Retained frequency order](frequency-order.md): The recordwise operation multiplying each record by y^E.
- $h_p$ (grid spacing), bound on [Error tracking and exact recovery](precision-recovery.md): The grid spacing 2^{-p} of the fixed-point records.
- $L$ (log of padded length), bound on [Error tracking and exact recovery](precision-recovery.md): The base-2 logarithm of the padded length T.
- $a$ (error size), bound on [Error tracking and exact recovery](precision-recovery.md): The size of an error in grid spacings.
- $x$ (disk array), bound on [Error tracking and exact recovery](precision-recovery.md): An array in the unit disk to which a phase or chirp transform is applied.
- $u$ (scaled first digits), bound on [Error tracking and exact recovery](precision-recovery.md): The scaled digit array of the first input.
- $v$ (scaled second digits), bound on [Error tracking and exact recovery](precision-recovery.md): The scaled digit array of the second input.
- $\tau$ (interchange exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent in the cost of a chunk interchange.
- $\sigma$ (recursion growth exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The bound on the growth exponent of recursive calls.
- $\beta$ (threshold exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the threshold d^beta below which active chunks are handled singly.
- $\lambda$ (overhead exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The per-node overhead exponent of the layer.
- $\lambda'$ (layer exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The final exponent of the layer cost V d^{lambda'}.
- $c$ (chunk-width exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the address-chunk width K=floor(d^c).
- $\epsilon$ (axis-count exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the axis count d=floor(b^epsilon).
- $\delta$ (resampling slack), bound on [Parameter and prime-length choice](parameter-choice.md): The fixed slack in the exponent of the resampling cost, delta=1/16.
- $C_1$ (guard-bit exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the guard bits.
- $V$ (bit volume), bound on [Parameter and prime-length choice](parameter-choice.md): The number of stored bits on which the layer cost is measured.
- $K$ (chunk width), bound on [Parameter and prime-length choice](parameter-choice.md): The width in bits of an address chunk.
- $\eta$ (prime gap fraction), bound on [Parameter and prime-length choice](parameter-choice.md): The smallest relative distance at which a prime s_i may lie below t_i.
- $E$ (first space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The first of the two finite-dimensional vector spaces being tensored.
- $G$ (second space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The second of the two finite-dimensional vector spaces being tensored.
- $A$ (ambient space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A finite-dimensional space with a nondegenerate form, containing the subspace P.
- $C$ (second ambient space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A finite-dimensional space with a nondegenerate form, containing the subspace Q.
- $P$ (subspace of A), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A subspace of A, later taken nondegenerate.
- $Q$ (subspace of C), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A subspace of C.
- $B$ (orthogonal complement), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The orthogonal complement of P in A.
- $F$ (base space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A space of dimension h with a nondegenerate form, whose triple power is the label space.
- $W$ (wire count), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of wires of the network under consideration, W_b for the bit network or W_c for the complex one (not a stream count).
- $s$ (smaller-call count), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total number of smaller calls made by the edges of the network under consideration.
- $U$ (subspace), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A subspace of a space with a symmetric bilinear form; later a label.
- $x$ (first vector), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A vector of F, the first argument of the bit form (not the polynomial variable).
- $y$ (second vector), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A vector of F, the second argument of the bit form (not the ring variable).
- $\mathbf 1$ (all-ones vector), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The vector of F whose entries are all 1.
- $S$ (triple), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A three-element subset of [h], an element of the triple set (not a convolution length).
- $S'$ (second triple), bound on [Nested subspace labels and rank deficit](subspace-labels.md): Another three-element subset of [h].
- $t_S$ (indicator vector), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator vector in F of the triple S.
- $E$ (first factor subspace), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A subspace of a tensor power of F; in the bracket notation, a subspace of F.
- $E'$ (second factor subspace), bound on [Nested subspace labels and rank deficit](subspace-labels.md): Another subspace of a tensor power of F; in the bracket notation, a subspace of F containing E.
- $G$ (other factor subspace), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A subspace of a tensor power of F; in the bracket notation, a subspace of F.
- $\mathcal F$ (label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The label space F tensor F tensor F, of dimension m.
- $U_a$ (data line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by the tensor product of the indicators of the three triples of the data index a.
- $L$ (total loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on the decreasing edges of the network under consideration.
- $L_{\rm b}$ (bit loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on the decreasing edges of the bit network.
- $L_{\rm c}$ (complex loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on the decreasing edges of the complex network.
- $s_{\rm b}$ (bit smaller-call count), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of smaller calls made by the edges of the bit network.
- $s_{\rm c}$ (complex smaller-call count), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of smaller calls made by the edges of the complex network.
- $j$ (stage index), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The index 1, 2 or 3 of the stage, which varies the coordinate a_j.
- $A$ (earlier tensor space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The tensor power of F with j-1 factors, of dimension h^{j-1}.
- $P$ (earlier line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line in A spanned by the tensor product of the indicators of the earlier triples a_1,...,a_{j-1}.
- $B$ (complement of P), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The orthogonal complement of P in A.
- $G'$ (larger subspace), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A subspace of F containing G.
- $A'$ (next earlier space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space A of the next stage, A tensor F.
- $P'$ (next earlier line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line P of the next stage, P tensor the line of t_{a_j}.
- $B'$ (next complement), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The orthogonal complement of P' in A', the B of the next stage.
- $Q'$ (next later line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line Q of the next stage, spanned by the tensor product of the indicators of the triples after a_{j+1}.
- $t_X$ (X-side indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator of the j-th triple of the X-entry a wire serves.
- $t_Y$ (Y-side indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator of the j-th triple of the Y-entry a wire serves.
- $\Pi_U$ (projection), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The projection onto U along its orthogonal complement, the matrix at a vertex labelled U.
- $U'$ (larger subspace), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A nondegenerate subspace containing U.
- $f$ (call parameter), bound on [Recursive power saving](rank-recurrence.md): The parameter of a recursive call: the number of digits per interchanged chunk, or the number of selected axes of a layer.
- $\mathcal C$ (time per unit volume), bound on [Recursive power saving](rank-recurrence.md): The running time of a call at a given parameter, divided by the volume of its stream.
- $j$ (recursion depth), bound on [Recursive power saving](rank-recurrence.md): The number of recursion levels below the top call, indexing the terms of the unrolled sum; here not a stage number.
- $\eta$ (relative rank deficit), bound on [Recursive power saving](rank-recurrence.md): The relative amount (Wm-s)/(Wm) by which the number of smaller calls falls short of Wm; here not the prime distance of the parameter-choice page.
- $u$ (chunk width), bound on [Fast address-chunk interchange](address-interchange.md): The number of bits in each of the two address chunks.
- $p$ (prefix), bound on [Fast address-chunk interchange](address-interchange.md): The address field before the first chunk.
- $h$ (first chunk), bound on [Fast address-chunk interchange](address-interchange.md): The first of the two address chunks being interchanged.
- $g$ (gap), bound on [Fast address-chunk interchange](address-interchange.md): The address field between the two chunks.
- $d$ (second chunk), bound on [Fast address-chunk interchange](address-interchange.md): The second of the two address chunks being interchanged.
- $z$ (suffix), bound on [Fast address-chunk interchange](address-interchange.md): The address field after the second chunk.
- $q$ (digit radix), bound on [Fast address-chunk interchange](address-interchange.md): The fixed prime radix of the stored digits.
- $e$ (chunk digits), bound on [Fast address-chunk interchange](address-interchange.md): The number of radix-$q$ digits in each chunk, a power of $m$.
- $m$ (fields per chunk), bound on [Fast address-chunk interchange](address-interchange.md): The number of fields into which a chunk is cut.
- $k$ (recursion levels), bound on [Fast address-chunk interchange](address-interchange.md): The number of recursion levels, with $e=m^k$.
- $b$ (digits per field), bound on [Fast address-chunk interchange](address-interchange.md): The number of digits in one field of a chunk, $e/m$.
- $H$ (first chunk vector), bound on [Fast address-chunk interchange](address-interchange.md): The vector of the $m$ fields of the first chunk, over the integers mod $q^b$.
- $D$ (second chunk vector), bound on [Fast address-chunk interchange](address-interchange.md): The vector of the $m$ fields of the second chunk, over the integers mod $q^b$.
- $M$ (vertex matrix), bound on [Fast address-chunk interchange](address-interchange.md): The rational $m\times m$ matrix carried by a vertex of the network.
- $i$ (edge index), bound on [Fast address-chunk interchange](address-interchange.md): The index of an edge of the network.
- $A_i$ (edge matrix), bound on [Fast address-chunk interchange](address-interchange.md): The difference of the vertex matrices at the head and tail of edge $i$.
- $w$ (wire index), bound on [Fast address-chunk interchange](address-interchange.md): The index of an input wire of the network, also naming its role stream.
- $I_m$ (identity matrix), bound on [Fast address-chunk interchange](address-interchange.md): The $m\times m$ identity matrix.
- $\Phi_M$ (address shear), bound on [Fast address-chunk interchange](address-interchange.md): The array permutation moving the entry at address $(H,D)$ to $(H+MD,D)$.
- $x$ (stream row), bound on [Fast address-chunk interchange](address-interchange.md): The row number within a role stream.
- $f_w$ (physical input), bound on [Fast address-chunk interchange](address-interchange.md): The array physically stored on input wire $w$.
- $f'_{\rho(w)}$ (physical output), bound on [Fast address-chunk interchange](address-interchange.md): The array physically stored on output role $\rho(w)$.
- $F_k$ (time per volume), bound on [Fast address-chunk interchange](address-interchange.md): The time per unit volume of an interchange of width $m^k$.
- $c$ (call ratio), bound on [Fast address-chunk interchange](address-interchange.md): The number of calls $s$ times the volume fraction $1/W$ of each, $c=s/W$.
- $\tau$ (interchange exponent), bound on [Fast address-chunk interchange](address-interchange.md): The fixed exponent below $1$ in the cost $O(Vu^\tau)$ of the interchange.
- $j$ (recursion level), bound on [Fast address-chunk interchange](address-interchange.md): The index of a recursion level, indexing the terms of the unrolled sum; also the exponent of a piece width $m^j$.
- $\nu$ (top digit count), bound on [Fast address-chunk interchange](address-interchange.md): The number of top digits of each chunk set aside to form the row field.
- $h^+$ (first chunk top), bound on [Fast address-chunk interchange](address-interchange.md): The top $\nu$ digits of the first chunk.
- $h^-$ (first chunk rest), bound on [Fast address-chunk interchange](address-interchange.md): The remaining digits of the first chunk.
- $d^+$ (second chunk top), bound on [Fast address-chunk interchange](address-interchange.md): The top $\nu$ digits of the second chunk.
- $d^-$ (second chunk rest), bound on [Fast address-chunk interchange](address-interchange.md): The remaining digits of the second chunk.
- $\Lambda$ (row field range), bound on [Fast address-chunk interchange](address-interchange.md): The number of values of the row field, $q^{2\nu}$.
- $\Lambda'$ (padded rows), bound on [Fast address-chunk interchange](address-interchange.md): The number of rows after padding with zero rows.
- $a_j$ (piece count), bound on [Fast address-chunk interchange](address-interchange.md): The base-$m$ digit of $e-\nu$ giving the number of pieces of width $m^j$.
- $v$ (binary vector), bound on [Binary phase frames](phase-frames.md): A binary vector in F_2^m (not the number of triples).
- $E$ (edge residual), bound on [Binary phase frames](phase-frames.md): The edge residual of an edge: the orthogonal summand added going from U to V (not a tensor factor).
- $k$ (column count), bound on [Binary phase frames](phase-frames.md): The number of columns of data, so that an address is a k-tuple (not a depth).
- $u$ (binary vector), bound on [Binary phase frames](phase-frames.md): A binary vector in F_2^m (not an input sequence).
- $w$ (binary vector), bound on [Binary phase frames](phase-frames.md): A binary vector in F_2^m.
- $z$ (binary vector), bound on [Binary phase frames](phase-frames.md): A binary vector in F_2^m.
- $\operatorname{supp}$ (support), bound on [Binary phase frames](phase-frames.md): The set of coordinates where a binary vector is 1.
- $\operatorname{wt}$ (Hamming weight), bound on [Binary phase frames](phase-frames.md): The Hamming weight: the number of coordinates where a binary vector is 1.
- $P_U$ (projection), bound on [Binary phase frames](phase-frames.md): The projection onto a label U over F_2.
- $X_v$ (translation by v), bound on [Binary phase frames](phase-frames.md): The translation of functions of x by the binary vector v.
- $q_U$ (weight phase exponent), bound on [Binary phase frames](phase-frames.md): The Hamming weight of P_U x, modulo four.
- $\mathcal C_U$ (phase frame), bound on [Binary phase frames](phase-frames.md): The phase frame of the label U.
- $\mathcal B$ (orthonormal basis), bound on [Binary phase frames](phase-frames.md): An orthonormal basis of the edge residual E.
- $\varepsilon$ (edge phase sign), bound on [Binary phase frames](phase-frames.md): The sign, plus or minus one modulo four, of one basis vector's phase term, including the edge direction.
- $Z$ (sign matrix), bound on [Binary phase frames](phase-frames.md): The diagonal matrix diag(1,-1).
- $Z_{a,k}$ (sign operator), bound on [Binary phase frames](phase-frames.md): Z on the 27 coordinates of supp(u) in every column, the identity elsewhere.
- $c$ (control bit), bound on [Packed selected-bit addition](packed-bit-addition.md): A control bit, equal to 0 or 1, that gates each addition.
- $u$ (first integer), bound on [Packed selected-bit addition](packed-bit-addition.md): One of the two integers whose parities the eight additions act on.
- $w$ (second integer), bound on [Packed selected-bit addition](packed-bit-addition.md): The other integer, an arbitrary auxiliary value that is restored.
- $R$ (record bits), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in the record stored at each address.
- $L$ (chunk width), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in each of the chunks x, y, z, equal to fK.
- $K$ (segment spacing), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits between consecutive selected positions, at least 6.
- $f$ (selected-bit count), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of selected bits.
- $M$ (address count), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of addresses.
- $V$ (array volume), bound on [Packed selected-bit addition](packed-bit-addition.md): The total number of bits M times R.
- $A_{\rm rect}$ (counter length), bound on [Packed selected-bit addition](packed-bit-addition.md): An upper bound on the bits of the counters, the ceiling of log2(2V).
- $\rho$ (offset), bound on [Packed selected-bit addition](packed-bit-addition.md): The offset of the first selected position within a segment spacing.
- $j_i$ (selected position), bound on [Packed selected-bit addition](packed-bit-addition.md): The i-th selected bit position, rho plus iK.
- $\mathcal B$ (exceptional set), bound on [Packed selected-bit addition](packed-bit-addition.md): The set of addresses at which some guard value falls outside the safe interval.
- $S_0$ (packed map), bound on [Packed selected-bit addition](packed-bit-addition.md): The composition of the eight packed cyclic shifts.
- $T_0$ (ideal map), bound on [Packed selected-bit addition](packed-bit-addition.md): The ideal permutation that performs the required XORs and fixes all other coordinates.
- $D$ (selected chunk count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of selected address chunks (axes), at most d.
- $e$ (group axis count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of selected axes in a group, e=mf.
- $f$ (slot width), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of axes in each of the m slots of a group.
- $\Gamma$ (basis-change matrix), bound on [Simultaneous butterfly layer](simultaneous-layer.md): An invertible matrix over F_2 whose first columns are the residual basis vectors.
- $\xi$ (residual index), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The index of a residual basis vector of an edge.
- $\mathcal P_\Gamma$ (address permutation), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The address permutation sending x to Gamma x.
- $\mathcal S_D$ (phase diagonal), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The diagonal operator multiplying the value at x by i to the power x_1+...+x_D.
- $q_0$ (individual chunk count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of leading chunks to which C is applied individually and whose bits form the row index.
- $\Xi$ (time per unit volume), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The time for e axes divided by their stream volume, as a function of e.
- $\chi$ (chain operation bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A bound on the number of arithmetic operations on a chain from an input coefficient to an intermediate one.
- $E$ (operation bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A bound on the operations of one network invocation, 64(W+m+1)^3.
- $\Psi$ (chain growth factor), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The sum s+E, the factor by which each recursion level multiplies the chain bound.
- $\vartheta$ (exponent of m), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The least j at least 1 with m^j at least Psi.
- $C_0$ (guard constant), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The constant 128 m Psi^2 in the guard width.

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
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Elementary stream operations](stream-ops.md)
- [Bluestein chirp identity](chirp.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Two-point kernel C](phase-kernel.md)
- [Contractions and bilinear contractions](contraction-maps.md)
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [Tensor products of subspaces](tensor-product-of-spaces.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Binary phase frames](phase-frames.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Convolution from the retained transform layout](ring-convolution.md)
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

## Problems a reader audit found in the previous version (fix all of them)

- The quotation does not support the claim it is attached to (unsupported): "Every later round is then a single layer" cites "we must place the selected bits of the participating axes at a common": The quotation only says the selected bits of the axes must be placed at a common (location); it does not say that later rounds are each a single layer. Say only what the source supports, or cite the passage that supports the claim.

## Previous version (revise it)

It has 691 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 863 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The tape layout reorders the address bits of an array so that each round of a [synthetic polynomial transform](synthetic-transform.md) on several axes runs as one [simultaneous butterfly layer](simultaneous-layer.md) instead of one pass per axis, which is where the transform's cost drops below the standard pass count.

Write $\ell=\log_2 r$, the number of address bits of a long axis, and $D=d-1$, the number of transformed axes (not a chunk or a chunk count from the other pages). Axis $i$ has length $t_i\in\{2^{\ell-1},2^\ell\}$. $K$ is the chunk width in bits, and $\tau,\lambda'<1$ are the interchange and layer exponents. With $\boldsymbol t=(t_1,\dots,t_D)$, $F_{\boldsymbol t}^-$ is the forward transform on all $D$ axes and $F_{\boldsymbol t}^+$ its opposite. By [retained frequency order](frequency-order.md) the forward transform leaves its outputs in bit-reversed order, written $B$ here (the bit-reversal permutation on all axes), and the opposite transform consumes that order, so no reordering is executed.

## Why a layout is needed

[Fixed-point Gaussian dyadic records](fixed-point.md) use $\Theta(p)$ bits per coefficient, so the $T$ coefficients occupy $\Theta(Tp)$ bits and one pass of a tape machine over them costs $O(Tp)$. The transform has $\ell$ rounds, and each round applies the two-point averaging and differencing step to one address bit of every axis. Done axis by axis this is about $D\ell$ passes, and since $d\ell=O(p)$ that is $O(Tp\cdot p)$. The layer does a round on $D$ axes in $O(Tpd^{\lambda'})$ rather than $D$ passes, but it acts on the same bit of $D$ consecutive $K$-bit chunks. Axis-major storage does not provide this: the bits of different axes are far apart. The record permutation $L$, built below, moves them together once. Every later round is then a single layer <cite data-source="paper">we must place the selected bits of the participating axes at a common</cite>.

## Building the layout

Call an axis long if it has $\ell$ address bits and short if $\ell-1$. Put $b=(\ell-1)\bmod K$, the number of leftover low bits of an axis, and $q=\lfloor(\ell-1)/K\rfloor$, its number of whole chunks. Move to a prefix, one at a time, the top bit of each long axis and the $b$ lowest bits of each axis. What remains of each axis is exactly $q$ consecutive $K$-bit chunks. At most $D(b+1)=O(dK)$ bits move, so the moves cost $O(TpdK)$ <cite data-source="paper">listed slots, so the moves cost $O(TpdK)$.</cite>

Label each chunk by its axis and its rank from the high end of the axis, so the first chunk of axis 2 is $(2,1)$. The chunks are stored as $(1,1),\dots,(1,q),(2,1),\dots,(D,q)$ and must become $(1,1),(2,1),\dots,(D,1),(1,2),\dots,(D,q)$, so that the chunks of equal rank in all axes are adjacent. Scan the target positions from left to right and, at each one except the last, exchange the chunk there with the required one if they differ. This is at most $Dq-1$ exchanges, each done by the [fast address-chunk interchange](address-interchange.md) in $O(TpK^\tau)$ even for nonadjacent chunks <cite data-source="paper">exchanges of width-$K$ address chunks, even when the chunks are</cite>. Since $DqK\le d\ell=O(p)$, the total is $O(Tp\,DqK^\tau)=O(Tp\,pK^{\tau-1})$. The prefix moves and exchanges define the record permutation $L$; recording them in reverse gives $L^{-1}$ at the same cost.

## Running the rounds

There are $qK$ rounds on chunk bits and $b+1$ on prefix bits, $\ell$ in all. In a chunk round the selected bit has the same offset in the $D$ consecutive chunks of equal rank, so one layer performs it. The cost is $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total <cite data-source="paper">$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.</cite> A prefix round processes at most $D\le d$ bits individually, each in $O(Tp)$. There are at most $b+1\le K$ such rounds, so they cost $O(TpdK)$.

Adding the three costs, the moves, exchanges and rounds give $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$. Here $K^{\tau-1}<1$ and $d^{\lambda'}<d$ are the savings over $D\ell$ passes.

## Error

Each round is the exact contraction $\mathcal H$ (which does not increase the norm of an error), the signed coefficient permutation $J_E$, and one truncation $Q_p$. Truncation toward zero is odd and acts separately on each real and imaginary part, so for the array $z$ entering the round $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$: the computed round equals one truncation after the exact round. That truncation moves each entry by less than $\sqrt2\,2^{-p}$, so by the triangle inequality each round adds less than $\sqrt2\,2^{-p}$ to the error. The permutations in $L$ are isometries and add none. Starting from zero error, the $\ell$ rounds leave error less than $\sqrt2\,\ell\,2^{-p}$ <cite data-source="paper">zero error, at most $\ell$ rounds therefore</cite>.

## Which operator is computed

Arithmetic executed on named slots after $L$ is the logical operation conjugated by $L$. The forward procedure first moves records by $L$ and then runs $BF_{\boldsymbol t}^-$, so its operator is $(LBF_{\boldsymbol t}^-L^{-1})L=LBF_{\boldsymbol t}^-$. The opposite procedure runs its arithmetic and then restores the order by $L^{-1}$, so its operator is $L^{-1}(LF_{\boldsymbol t}^+B^{-1}L^{-1})=F_{\boldsymbol t}^+B^{-1}L^{-1}$. Both therefore have error less than $\sqrt2\,\ell\,2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$, including building and undoing the layout.

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

Write the body to `exegenius/tasks/0397-write-transform-layout.answer.md` and the JSON to `exegenius/tasks/0397-write-transform-layout.answer.json`, then run `exegenius submit 0397-write-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0397-write-transform-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
