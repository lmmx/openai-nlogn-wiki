# exegenius task 0276-write-transform-layout

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
- $c$ (machine constant), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A positive constant, depending on the machine, in the lower bound c n log n.
- $\kappa$ (power saving), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant by which the exponent of the logarithm is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the grid on which stored values lie.
- $k$ (depth), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations in sequence since the layer began that produced a value.
- $\Delta$ (reserved extra bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the maximal depth reached in the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.
- $h$ (ground-set size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of the ground set [h] whose three-element subsets index the data.
- $\mathcal T$ (triple set), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The set of three-element subsets of [h].
- $v$ (number of triples), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of three-element subsets of [h].
- $X$ (bank X), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The first data bank, with entries X_a.
- $Y$ (bank Y), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The second data bank, with entries Y_a.
- $a$ (bank index), bound on [Linear exchange network with restored scratch wires](exchange-network.md): A triple of three-element subsets of [h] indexing the bank entries (not a shift exponent here).
- $N$ (bank size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of entries in each data bank.
- $m$ (label dimension), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The dimension of the label space used on later pages.
- $S$ (slice index), bound on [Linear exchange network with restored scratch wires](exchange-network.md): A three-element subset of [h]: the varying coordinate of a within a slice.
- $x_S$ (source value), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The entry of the source bank at slice index S.
- $y_S$ (target value), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The entry of the target bank at slice index S.
- $C_i$ (central wire), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The central wire for the element i of [h].
- $S'$ (other triple), bound on [Linear exchange network with restored scratch wires](exchange-network.md): Another three-element subset in the same slice.
- $A_{SS'}$ (side wire), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The scratch wire for the ordered neighbour pair (S,S').
- $\sigma$ (initial side values), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The initial values of the side wires.
- $\gamma$ (initial central values), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The initial values of the central wires.
- $\mathcal V$ (copy map), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The linear map copying source values onto side wires.
- $\mathcal G$ (gather map), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The linear map gathering source values onto central wires.
- $\mathcal J$ (injection map), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The linear map injecting side wires into the target.
- $\mathcal R$ (scatter map), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The linear map scattering central wires into the target.
- $I$ (number of invocations), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of invocations in the three stages.
- $z_{\rm b}$ (bit neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the bit construction.
- $z_{\rm c}$ (complex neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the complex construction.
- $c_{\rm b}$ (bit central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the bit network.
- $W_{\rm c}$ (complex wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the complex network.
- $R$ (scalar ring), bound on [Frames on wire arrays](array-frames.md): The ring of scalars carried by the wires.
- $\Omega$ (address set), bound on [Frames on wire arrays](array-frames.md): A finite set of addresses indexing every array.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): The invertible R-linear operator on R^Omega assigned to a source, gate or sink v.
- $t$ (gate input count), bound on [Frames on wire arrays](array-frames.md): The number of input arrays of a gate.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each of the two sequences being convolved.
- $d$ (axis count), bound on [Cyclic convolution](convolution.md): The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of cyclic axis i.
- $M$ (address count), bound on [Cyclic convolution](convolution.md): The number of cyclic addresses of an array, the product of the axis lengths.
- $T$ (coefficient count), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array.
- $u$ (first input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The first of the two integers being multiplied.
- $v$ (second input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The second of the two integers being multiplied.
- $n$ (input bit length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in each input.
- $b$ (digit width), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in one radix digit.
- $T$ (padded length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): A power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The length of the cyclic convolution, a product of distinct odd primes with T/2 < S < T.
- $q$ (digit count), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of radix-2^b digits in each input.
- $u_i$ (digit of u), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The i-th radix-2^b digit of u, an integer below 2^b.
- $v_k$ (digit of v), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The k-th radix-2^b digit of v, an integer below 2^b.
- $x$ (polynomial variable), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The variable of the digit polynomials, evaluated at 2^b to recover the integers.
- $c_j$ (product coefficient), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The coefficient of x^j in the product of the digit polynomials.
- $f$ (first array), bound on [Phase twist](phase-twist.md): The first complex array being convolved.
- $g$ (second array), bound on [Phase twist](phase-twist.md): The second complex array being convolved with f.
- $d$ (axis count), bound on [Phase twist](phase-twist.md): The number of axes of the arrays.
- $x_d$ (last-axis variable), bound on [Phase twist](phase-twist.md): The variable of the last cyclic axis.
- $\mathcal R_r$ (negacyclic ring), bound on [Phase twist](phase-twist.md): The ring of polynomials modulo y^r+1.
- $\zeta$ (twist root), bound on [Phase twist](phase-twist.md): The primitive 2r-th root of unity e^{\pi i/r}, with zeta^r=-1.
- $\Theta$ (twist map), bound on [Phase twist](phase-twist.md): The ring isomorphism from the cyclic ring to the negacyclic ring sending x_d to zeta y.
- $k$ (coefficient index), bound on [Phase twist](phase-twist.md): An index of a coefficient (not an operation count).
- $l$ (second coefficient index), bound on [Phase twist](phase-twist.md): An index of a coefficient of the second factor.
- $j$ (wrapped position), bound on [Phase twist](phase-twist.md): The position k+l reduced modulo r.
- $h$ (wrap indicator), bound on [Phase twist](phase-twist.md): Zero or one according to whether k+l wrapped past r.
- $\iota$ (record reading), bound on [Phase twist](phase-twist.md): The map reading each line along the last axis as a polynomial in R_r.
- $D_\pm$ (diagonal twist), bound on [Phase twist](phase-twist.md): The maps multiplying entry k of each line by zeta^{+-k}.
- $\mathcal M_r$ (ring convolution), bound on [Phase twist](phase-twist.md): Normalized convolution of the first d-1 axes over R_r, including division by T.
- $\mathcal M_{\mathbb C}$ (complex convolution), bound on [Phase twist](phase-twist.md): The normalized complex cyclic convolution of two arrays.
- $\|f\|$ (sup norm), bound on [Phase twist](phase-twist.md): The largest modulus of a scalar coefficient of f.
- $q$ (sequence length), bound on [Discrete Fourier transform](dft.md): The number of entries of a sequence.
- $u$ (input sequence), bound on [Discrete Fourier transform](dft.md): A sequence of q complex numbers to be transformed.
- $\omega$ (primitive root), bound on [Discrete Fourier transform](dft.md): The primitive q-th root of unity e^{2\pi i/q}.
- $t$ (transform length), bound on [Butterflies and the fast transform](butterfly.md): The number of positions in the sequence being transformed, a power of two.
- $z_k$ (input value), bound on [Butterflies and the fast transform](butterfly.md): The input value at position k of the sequence being transformed.
- $m$ (output index), bound on [Butterflies and the fast transform](butterfly.md): The index of an output of the transform.
- $b$ (lowest bit), bound on [Butterflies and the fast transform](butterfly.md): The lowest bit of the output index m.
- $h$ (remaining index), bound on [Butterflies and the fast transform](butterfly.md): The output index m with its lowest bit removed.
- $t$ (transform length), bound on [Synthetic polynomial transform](synthetic-transform.md): The number of ring elements along one axis, a power of two dividing 2r.
- $e$ (two-adic exponent), bound on [Synthetic polynomial transform](synthetic-transform.md): The exponent of 2 in j when j is written as 2^e times an odd number.
- $V$ (array volume), bound on [Elementary stream operations](stream-ops.md): The number of radix-q digits an array stores.
- $q$ (radix), bound on [Elementary stream operations](stream-ops.md): The number of values one digit can take.
- $P$ (prefix values), bound on [Elementary stream operations](stream-ops.md): The number of prefix values indexing the first axis of the array.
- $R$ (row count), bound on [Elementary stream operations](stream-ops.md): The number of rows in the array of item 4.
- $B$ (entries per row), bound on [Elementary stream operations](stream-ops.md): The number of entries in each row.
- $W$ (stream count), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams the rows are dealt into.
- $\boldsymbol j$ (index tuple), bound on [Bluestein chirp identity](chirp.md): The tuple of indices (j_1,...,j_d), one per axis, locating an entry of an array.
- $\boldsymbol t$ (axis lengths), bound on [Bluestein chirp identity](chirp.md): The tuple (t_1,...,t_d) of axis lengths, where t_i is the even number of entries along axis i.
- $s_i$ (coprime multiplier), bound on [Bluestein chirp identity](chirp.md): An integer coprime to the axis length t_i.
- $F_{\boldsymbol t}$ (normalized transform), bound on [Bluestein chirp identity](chirp.md): The normalized multidimensional discrete Fourier transform with axis lengths t.
- $\boldsymbol k$ (input position), bound on [Bluestein chirp identity](chirp.md): The index tuple of an input entry.
- $\boldsymbol f$ (frequency), bound on [Bluestein chirp identity](chirp.md): The tuple of frequencies labelling an output entry of the transform.
- $Q$ (target permutation), bound on [Bluestein chirp identity](chirp.md): The permutation reordering the output so that position j holds the entry of frequency (-s_i j_i)_i.
- $a$ (chirp), bound on [Bluestein chirp identity](chirp.md): The chirp, a phase quadratic in the index.
- $N$ (factor bit length), bound on [Established O(n log n) multiplier](hvdh-multiplier.md): The number of bits in each of the two integers given to the established multiplier.
- $B_0$ (packing base), bound on [Signed packing](signed-packing.md): The base 2^{4p} at which the polynomials are evaluated.
- $A_u$ (signed evaluation integer), bound on [Signed packing](signed-packing.md): The integer obtained by evaluating the integer-coefficient polynomial u at B_0.
- $\gamma_j$ (carry), bound on [Signed packing](signed-packing.md): The carry, in {-1,0}, into block j when forming A_u.
- $d_j$ (block), bound on [Signed packing](signed-packing.md): The residue of u_j plus the carry modulo B_0, the j-th block of 4p bits of A_u.
- $h_j$ (product coefficient), bound on [Signed packing](signed-packing.md): The coefficient of y^j in the ordinary product h=ac of integer polynomials.
- $\rho_j$ (extraction carry), bound on [Signed packing](signed-packing.md): The carry into block j during extraction, in {0,1}.
- $H_j$ (reduced coefficient), bound on [Signed packing](signed-packing.md): The Gaussian integer coefficient of y^j after reduction modulo y^r+1.
- $q$ (prime modulus base), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed prime; on this page it is not a sequence length.
- $b$ (field digit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of base-$q$ digits of a field.
- $Q$ (field value count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of values a field can take, q^b.
- $a$ (offset), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The offset in [Q] added to the target field, prepared from the control values.
- $B$ (suffix bit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of bits following the target field.
- $c$ (scaling integer), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed positive integer prime to q by which the target field is multiplied; not the machine constant.
- $j$ (wrap count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The integer part of cy/Q, counting how often cy wraps past Q.
- $y'$ (new position), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The position cy-jQ to which the block at position y is sent.
- $c'$ (unit denominator), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The positive integer prime to q in the denominator of a rational unit c/c'.
- $m$ (fields per group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of fields in each of the groups H and D.
- $a$ (rank of A), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rank of the rational matrix A.
- $A$ (shear matrix), bound on [Matrix shear by triangular factorization](matrix-shear.md): A rational m by m matrix, taken from a fixed finite set, that the shear applies.
- $H$ (target group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The first group of m fields, which receives AD.
- $D$ (source group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The second group of m fields, which is left unchanged by the shear.
- $a$ (kernel coefficient a), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1+i)/2, the coefficient of the identity in C.
- $b$ (kernel coefficient b), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1-i)/2, the coefficient of the bit flip in C.
- $I$ (identity matrix), bound on [Two-point kernel C](phase-kernel.md): The 2 by 2 identity matrix.
- $X$ (bit flip), bound on [Two-point kernel C](phase-kernel.md): The 2 by 2 matrix swapping the two entries of a pair.
- $C$ (two-point kernel), bound on [Two-point kernel C](phase-kernel.md): The 2 by 2 matrix aI+bX.
- $\mathsf S$ (phase matrix), bound on [Two-point kernel C](phase-kernel.md): The diagonal matrix diag(1,i) multiplying the second entry of a pair by i.
- $H$ (normalized Hadamard matrix), bound on [Two-point kernel C](phase-kernel.md): The matrix sqrt(2) H_0, symmetric with H squared equal to the identity.
- $H_0$ (two-point butterfly), bound on [Two-point kernel C](phase-kernel.md): The matrix (1/2)[[1,1],[1,-1]] of the averaging and differencing step on a pair.
- $L$ (linear map), bound on [Contractions and bilinear contractions](contraction-maps.md): A linear map whose norm bound is being defined.
- $\mathcal M$ (bilinear map), bound on [Contractions and bilinear contractions](contraction-maps.md): A map linear in each of its two operands.
- $f$ (first operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The first operand of the bilinear map.
- $g$ (second operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The second operand of the bilinear map.
- $u'$ (computed input), bound on [Contractions and bilinear contractions](contraction-maps.md): A computed approximation replacing the exact input u.
- $f'$ (perturbed first operand), bound on [Contractions and bilinear contractions](contraction-maps.md): A perturbed replacement for the operand f.
- $g'$ (perturbed second operand), bound on [Contractions and bilinear contractions](contraction-maps.md): A perturbed replacement for the operand g.
- $F_q$ (normalized transform), bound on [Contractions and bilinear contractions](contraction-maps.md): The normalized discrete Fourier transform on sequences of q entries.
- $i$ (axis index), bound on [Multidimensional transforms](multidim-transform.md): The index of an axis of the array, from 1 to d.
- $q_i$ (axis position count), bound on [Multidimensional transforms](multidim-transform.md): The number of positions along axis i.
- $j$ (index tuple), bound on [Multidimensional transforms](multidim-transform.md): The tuple of coordinates (j_1,...,j_d) of an entry of the array.
- $k$ (output index tuple), bound on [Multidimensional transforms](multidim-transform.md): An output index tuple shaped like j.
- $G_i$ (axis operator), bound on [Multidimensional transforms](multidim-transform.md): An operator on sequences of length q_i, applied to every line along axis i.
- $\delta$ (time-bound slack), bound on [Multidimensional transforms](multidim-transform.md): A fixed constant with 0<delta<1/8 that sets the slack in the exponent 3/2+delta of p in the time bound.
- $\alpha$ (resampling parameter), bound on [Multidimensional transforms](multidim-transform.md): An integer resampling parameter with 2<=alpha<sqrt p.
- $\boldsymbol s$ (source lengths), bound on [Multidimensional transforms](multidim-transform.md): The tuple of source axis lengths (s_1,...,s_d).
- $\boldsymbol t$ (padded lengths), bound on [Multidimensional transforms](multidim-transform.md): The tuple of padded power-of-two axis lengths (t_1,...,t_d).
- $\gamma$ (scalar exponent), bound on [Multidimensional transforms](multidim-transform.md): The total exponent 2d alpha^2 of the power of two multiplying the tensored identity.
- $R$ (source permutation), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the source index permutations P_{s_i}; here not the scalar ring.
- $Q$ (padded permutation), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the index permutations P_{t_i}.
- $\mathcal A$ (input map), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the one-dimensional input maps A_i.
- $\mathcal B_0$ (output map), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the one-dimensional output maps B_{0,i}.
- $P_{s_i}$ (source axis permutation), bound on [Multidimensional transforms](multidim-transform.md): The index permutation of source axis i.
- $P_{t_i}$ (padded axis permutation), bound on [Multidimensional transforms](multidim-transform.md): The index permutation of padded axis i.
- $A_i$ (axis input map), bound on [Multidimensional transforms](multidim-transform.md): The linear input map of axis i.
- $B_{0,i}$ (axis output map), bound on [Multidimensional transforms](multidim-transform.md): The linear output map of axis i.
- $F_{q_i}$ (axis transform), bound on [Multidimensional transforms](multidim-transform.md): The one-dimensional normalized discrete Fourier transform of length q_i.
- $F_{\boldsymbol q}$ (multidimensional transform), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the axis transforms F_{q_i}.
- $X_i$ (axis operator X), bound on [Multidimensional transforms](multidim-transform.md): An operator on axis i.
- $Y_i$ (axis operator Y), bound on [Multidimensional transforms](multidim-transform.md): An operator on axis i.
- $S$ (convolution length), bound on [Chinese-remainder address map](crt-map.md): The length of the cyclic convolution, the product of the s_i.
- $d$ (number of axes), bound on [Chinese-remainder address map](crt-map.md): The number of axes of the target ring.
- $i$ (axis index), bound on [Chinese-remainder address map](crt-map.md): The index of an axis, from 1 to d.
- $s_i$ (axis source length), bound on [Chinese-remainder address map](crt-map.md): The length of axis i, pairwise coprime with the others; unrelated to the s_i of the chirp page.
- $P_i$ (prefix product), bound on [Chinese-remainder address map](crt-map.md): The product of the lengths s_j of the axes before axis i.
- $\mu_i$ (coordinate exponent), bound on [Chinese-remainder address map](crt-map.md): The inverse of P_i modulo s_i.
- $x_i$ (axis variable), bound on [Chinese-remainder address map](crt-map.md): The polynomial variable of axis i, with x_i^{s_i}=1.
- $\Phi$ (Chinese-remainder map), bound on [Chinese-remainder address map](crt-map.md): The ring isomorphism sending x to the product of x_i^{mu_i}.
- $a_j$ (mixed-radix digit), bound on [Chinese-remainder address map](crt-map.md): The j-th digit of k in mixed radix, 0 <= a_j < s_j.
- $b_i$ (axis coordinate), bound on [Chinese-remainder address map](crt-map.md): The axis-i coordinate of Phi(x^k).
- $t_i$ (padded axis length), bound on [Chinese-remainder address map](crt-map.md): The padded length of axis i, either r/2 or r.
- $\ell$ (address bits), bound on [Chinese-remainder address map](crt-map.md): The base-2 logarithm of the record length r, the number of address bits of a full-width axis.
- $V$ (stream volume), bound on [Chinese-remainder address map](crt-map.md): The volume of the stream being moved, Tp bits.
- $\tau$ (chunk-swap exponent), bound on [Chinese-remainder address map](crt-map.md): A fixed exponent below 1 in the cost of a chunk interchange.
- $T$ (padded record count), bound on [Chinese-remainder address map](crt-map.md): The number of padded records, the product of the t_i.
- $k$ (coefficient index), bound on [Chinese-remainder address map](crt-map.md): The index of a coefficient of the length-S sequence.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the Fourier transform to be replaced.
- $\alpha$ (Gaussian width parameter), bound on [Gaussian resampling](gaussian-resampling.md): An integer, with 2 <= alpha < sqrt p, that is the width parameter of the Gaussian weights.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): The relative gap t/s - 1 between the two lengths.
- $C$ (coordinate selection), bound on [Gaussian resampling](gaussian-resampling.md): The map from C^t to C^s that selects coordinate q_j into position j.
- $\delta$ (exponent slack), bound on [Gaussian resampling](gaussian-resampling.md): A fixed constant 0 < delta < 1/8 that is the slack in the exponents of the time bounds.
- $k$ (output coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A coordinate index of a vector in C^t, taken modulo t.
- $t$ (target length), bound on [Gaussian resampling](gaussian-resampling.md): The larger length, a power of two in the application, of the transform used instead of the length-s one.
- $\widetilde E$ (approximate E), bound on [Gaussian resampling](gaussian-resampling.md): The numerical approximation of E = N - I computed on D_p records.
- $\boldsymbol s$ (source length tuple), bound on [Retained permutation cancellation](retained-permutations.md): The tuple of the prime axis lengths $s_i$.
- $\boldsymbol t$ (padded length tuple), bound on [Retained permutation cancellation](retained-permutations.md): The tuple of the power-of-two axis lengths $t_i$.
- $F_q^+$ (positive-sign transform), bound on [Retained permutation cancellation](retained-permutations.md): The transform of a vector of q entries with the exponent's sign reversed and the same factor 1/q as F_q, so that F_q^+F_q=I/q.
- $z$ (vector), bound on [Retained permutation cancellation](retained-permutations.md): A vector of q complex entries being transformed.
- $c$ (unit), bound on [Retained permutation cancellation](retained-permutations.md): An integer that is a unit modulo q, used to permute coordinates by z_{cj}.
- $h$ (summation index), bound on [Retained permutation cancellation](retained-permutations.md): The index of summation in the Fourier sum, substituted by ck.
- $g$ (setup degree), bound on [Retained permutation cancellation](retained-permutations.md): A fixed exponent such that setup work per line is O(p^g).
- $t_{\max}$ (largest padded length), bound on [Retained permutation cancellation](retained-permutations.md): The largest axis length, $2^\ell$, each $t_i$ being $t_{\max}/2$ or $t_{\max}$.
- $u$ (first array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array (not an integer) in the resampling and convolution identities of this page.
- $v$ (second array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array (not an integer) in the resampling and convolution identities of this page.
- $a$ (round count), bound on [Retained frequency order](frequency-order.md): The number of rounds of the transform, a=log_2 t.
- $j$ (output index), bound on [Retained frequency order](frequency-order.md): The position of an output of the transform.
- $s$ (completed rounds), bound on [Retained frequency order](frequency-order.md): The number of rounds completed so far.
- $B_t$ (bit-reversal permutation), bound on [Retained frequency order](frequency-order.md): The permutation moving the entry at j to rev_a(j).
- $\mathcal H$ (parallel butterfly), bound on [Retained frequency order](frequency-order.md): The parallel butterfly applying H_0 on every participating axis in one round.
- $J_E$ (recordwise monomial), bound on [Retained frequency order](frequency-order.md): The recordwise operation multiplying each record by y^E.
- $h_p$ (grid spacing), bound on [Error tracking and exact recovery](precision-recovery.md): The spacing $2^{-p}$ of the fractional-bit grid, the unit in which errors are measured.
- $L$ (log of padded length), bound on [Error tracking and exact recovery](precision-recovery.md): The base-2 logarithm of the padded length $T$.
- $E_s$ (source error), bound on [Error tracking and exact recovery](precision-recovery.md): The factor $9\cdot2^\gamma TL$ such that a computed source transform has error under $E_sh_p$.
- $u$ (scaled digit array), bound on [Error tracking and exact recovery](precision-recovery.md): The array of scaled radix digits of the first input, each stored as its value times $2^{-b-2}$ (not the integer).
- $v$ (scaled digit array), bound on [Error tracking and exact recovery](precision-recovery.md): The array of scaled radix digits of the second input (not the integer).
- $Q_0$ (carry base), bound on [Error tracking and exact recovery](precision-recovery.md): The radix $2^b$ of the digits during carry propagation.
- $j$ (coefficient index), bound on [Error tracking and exact recovery](precision-recovery.md): The index of the product coefficient being processed during carry propagation.
- $k_j$ (carry), bound on [Error tracking and exact recovery](precision-recovery.md): The carry into position $j$ from the lower coefficients.
- $d_j$ (output digit), bound on [Error tracking and exact recovery](precision-recovery.md): The $j$-th radix-$2^b$ digit of the product.
- $\boldsymbol t$ (axis lengths), bound on [Error tracking and exact recovery](precision-recovery.md): The tuple of padded axis lengths of the array.
- $\tau$ (chunk-interchange exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent in the cost of a chunk interchange.
- $\sigma$ (recursion growth exponent), bound on [Parameter and prime-length choice](parameter-choice.md): An exponent bounding the growth of the number of recursive calls.
- $\beta$ (active-chunk threshold exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent in the threshold d^beta below which active chunks are handled singly.
- $\lambda$ (overhead exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The per-node overhead exponent.
- $\lambda'$ (final cost exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The final exponent of the cost V d^lambda' on bit volume V.
- $V$ (bit volume), bound on [Parameter and prime-length choice](parameter-choice.md): The number of bits of the logical array the layer acts on.
- $c$ (chunk-width exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the address-chunk width (a new meaning of c).
- $\epsilon$ (axis-count exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the axis count.
- $C_1$ (guard-bit exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the guard bits.
- $\delta$ (resampling slack), bound on [Parameter and prime-length choice](parameter-choice.md): The slack in the exponent of the resampling cost.
- $K$ (chunk width), bound on [Parameter and prime-length choice](parameter-choice.md): The width in bits of an address chunk.
- $\eta$ (prime window offset), bound on [Parameter and prime-length choice](parameter-choice.md): The smallest relative distance at which a prime s_i may lie below t_i.
- $E$ (first space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The first of the two finite-dimensional vector spaces being tensored.
- $G$ (second space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The second of the two finite-dimensional vector spaces being tensored.
- $A$ (ambient space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A finite-dimensional space with a nondegenerate form, containing the subspace P.
- $C$ (second ambient space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A finite-dimensional space with a nondegenerate form, containing the subspace Q.
- $P$ (subspace of A), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A subspace of A, later taken nondegenerate.
- $Q$ (subspace of C), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A subspace of C.
- $B$ (orthogonal complement), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The orthogonal complement of P in A.
- $F$ (base space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A space of dimension h with a nondegenerate form, whose triple power is the label space.
- $s$ (number of smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total number of smaller calls that the edges of the network cost.
- $W$ (wire count), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of wires of the network under consideration.
- $U$ (a label subspace), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A subspace of the label space, such as the label of a vertex.
- $F$ (one-factor label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
- $x$ (vector of F), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A vector of $F$, the first argument of the bilinear form.
- $y$ (vector of F), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A vector of $F$, the second argument of the bilinear form.
- $T$ (a triple), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A three-element subset of $[h]$ (not the padded size used on other pages).
- $t_T$ (triple indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator vector in $F$ of the triple $T$.
- $\mathcal F$ (ambient label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space $F^{\otimes3}$, of dimension $m=h^3$, in which all labels lie.
- $X$ (X bank), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The bank of data wires $X_a$.
- $Y$ (Y bank), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The bank of data wires $Y_a$.
- $U_a$ (terminal line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$, the source label of $X_a$.
- $L$ (total dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total number of dimensions lost on decreasing edges.
- $j$ (stage number), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
- $A$ (exposed factor space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The tensor product $F^{\otimes(j-1)}$ of the factors exposed before stage $j$.
- $P$ (earlier tensor line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
- $B$ (complement of P), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The orthogonal complement of $P$ inside $A$.
- $K$ (later tensor line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
- $A'$ (next exposed space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $A$, equal to $A\otimes F$.
- $P'$ (next earlier line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $P$, equal to $P\otimes\langle t_{a_j}\rangle$.
- $B'$ (next complement), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $B$, the orthogonal complement of $P'$ in $A'$.
- $K'$ (next later line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $K$, with $K=\langle t_{a_{j+1}}\rangle\otimes K'$.
- $t_X$ (X-bank indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator of the X-bank triple of a gate or side wire in one invocation.
- $t_Y$ (Y-bank indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator of the Y-bank triple of a gate or side wire in one invocation.
- $L_{\rm b}$ (bit dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on decreasing edges of the bit network.
- $L_{\rm c}$ (complex dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on decreasing edges of the complex network.
- $\Pi_U$ (projection onto a label), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The rational projection onto the label $U$ along $U^\perp$, the matrix of a bit-network vertex labelled $U$.
- $V$ (larger label), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A label containing the label $U$ at the other end of an edge.
- $s_{\rm b}$ (bit smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of smaller calls, the total rational rank of edge matrix differences, in the bit network.
- $s_{\rm c}$ (complex smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of smaller calls, the total number of phase kernels, in the complex network.
- $m$ (label dimension), bound on [Recursive power saving](rank-recurrence.md): The dimension of the label space, 10^6, which is also the number of slots a chunk is split into, so a parameter grows by the factor m per recursion level.
- $s$ (number of smaller calls), bound on [Recursive power saving](rank-recurrence.md): The number of calls at parameter f that one call at parameter mf makes, equal to the total rank of the frame changes over the network's edges.
- $f$ (call parameter), bound on [Recursive power saving](rank-recurrence.md): The size parameter of a call: the number of digits in each interchanged chunk, or the number of selected axes of a layer.
- $F$ (time per unit volume), bound on [Recursive power saving](rank-recurrence.md): The running time of a call at a given parameter divided by the volume of its stream.
- $j$ (recursion depth), bound on [Recursive power saving](rank-recurrence.md): The number of recursion levels between the top call and a given call.
- $\eta$ (relative deficit), bound on [Recursive power saving](rank-recurrence.md): The relative rank deficit (Wm - s)/(Wm) of a network, the fraction by which the number of smaller calls falls short of Wm.
- $u$ (chunk width), bound on [Fast address-chunk interchange](address-interchange.md): The number of bits in each of the two interchanged address chunks.
- $V$ (array volume), bound on [Fast address-chunk interchange](address-interchange.md): The number of bits stored in the array.
- $\tau$ (saving exponent), bound on [Fast address-chunk interchange](address-interchange.md): The fixed exponent below 1 in the cost, equal to 1 - 2^{-50}.
- $p$ (prefix), bound on [Fast address-chunk interchange](address-interchange.md): The part of an address before the first chunk.
- $h$ (first chunk), bound on [Fast address-chunk interchange](address-interchange.md): The first of the two address chunks being interchanged.
- $g$ (gap), bound on [Fast address-chunk interchange](address-interchange.md): The part of an address between the two chunks.
- $d$ (second chunk), bound on [Fast address-chunk interchange](address-interchange.md): The second of the two address chunks being interchanged.
- $z$ (suffix), bound on [Fast address-chunk interchange](address-interchange.md): The part of an address after the second chunk.
- $q$ (digit radix), bound on [Fast address-chunk interchange](address-interchange.md): The fixed prime that is the radix of the digits.
- $e$ (chunk digit count), bound on [Fast address-chunk interchange](address-interchange.md): The number of radix-q digits in a chunk.
- $k$ (recursion levels), bound on [Fast address-chunk interchange](address-interchange.md): The number of recursion levels, with e = m^k.
- $M$ (vertex matrix), bound on [Fast address-chunk interchange](address-interchange.md): The rational m by m matrix carried by a terminal or gate of the network.
- $A_i$ (edge matrix), bound on [Fast address-chunk interchange](address-interchange.md): The difference of the matrices at the head and tail of edge i.
- $i$ (edge index), bound on [Fast address-chunk interchange](address-interchange.md): The index of an edge of the network.
- $w$ (wire index), bound on [Fast address-chunk interchange](address-interchange.md): The index of an input wire of the network.
- $\rho$ (role map), bound on [Fast address-chunk interchange](address-interchange.md): The map sending input wire w to its output role.
- $I_m$ (identity), bound on [Fast address-chunk interchange](address-interchange.md): The m by m identity matrix.
- $\Phi_M$ (address shear), bound on [Fast address-chunk interchange](address-interchange.md): The array permutation moving the entry at address (H,D) to (H+MD,D).
- $f_w$ (wire input), bound on [Fast address-chunk interchange](address-interchange.md): The physical input array of wire w.
- $x$ (stream row), bound on [Fast address-chunk interchange](address-interchange.md): The row number within a role stream.
- $j$ (recursion level), bound on [Fast address-chunk interchange](address-interchange.md): The index of a recursion level in the unrolled recurrence.
- $k'$ (level count), bound on [Fast address-chunk interchange](address-interchange.md): The least integer with m^{k'} at least e, used for arbitrary widths.
- $\nu$ (high digit count), bound on [Fast address-chunk interchange](address-interchange.md): The number of top digits of each chunk set aside to form the row field.
- $\Lambda$ (row range), bound on [Fast address-chunk interchange](address-interchange.md): The number of values of the row field formed by the high parts of both chunks.
- $\Lambda'$ (padded row range), bound on [Fast address-chunk interchange](address-interchange.md): The row count after padding with zero rows to a multiple of W^{k'}.
- $a_j$ (piece count), bound on [Fast address-chunk interchange](address-interchange.md): The number of pieces of width m^j into which each remaining chunk is cut.
- $v$ (binary vector), bound on [Binary phase frames](phase-frames.md): A vector of F_2^m; in the main argument a basis vector of an edge residual. Here v does not mean the triple count.
- $q_U$ (phase exponent), bound on [Binary phase frames](phase-frames.md): The weight modulo four of the projection of an address x onto the label U.
- $\mathcal C_U$ (phase frame), bound on [Binary phase frames](phase-frames.md): The operator on arrays attached to the label U.
- $X_v$ (translation), bound on [Binary phase frames](phase-frames.md): The operator shifting an array by the vector v: (X_v f)(x)=f(x+v).
- $\mathcal B$ (residual basis), bound on [Binary phase frames](phase-frames.md): An orthonormal basis of the edge residual E.
- $E$ (edge residual), bound on [Binary phase frames](phase-frames.md): The subspace added to U to reach V, orthogonal to U; here E is not the first space of a tensor product.
- $\varepsilon$ (phase sign), bound on [Binary phase frames](phase-frames.md): The coefficient +1 or -1 modulo four of a basis vector's phase, including the edge direction.
- $Z$ (sign matrix), bound on [Binary phase frames](phase-frames.md): The diagonal matrix diag(1,-1).
- $Z_{a,k}$ (sign correction), bound on [Binary phase frames](phase-frames.md): The tensor product of Z on the 27 coordinates of supp(u) in every column and the identity elsewhere.
- $k$ (column count), bound on [Binary phase frames](phase-frames.md): The number of columns of an address; here k changes meaning from the fixed-point page.
- $c$ (control bit), bound on [Packed selected-bit addition](packed-bit-addition.md): A bit, 0 or 1, that gates the eight additions.
- $u$ (first integer), bound on [Packed selected-bit addition](packed-bit-addition.md): The integer updated by lines 1, 3, 6 and 8 of the eight additions.
- $w$ (second integer), bound on [Packed selected-bit addition](packed-bit-addition.md): The integer updated by lines 2, 4, 5 and 7, restored at the end.
- $R$ (record bits), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in the record at each address.
- $L$ (chunk bits), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in each of the chunks x, y, z, equal to fK.
- $K$ (segment spacing), bound on [Packed selected-bit addition](packed-bit-addition.md): The spacing between selected positions, at least 6, which is the length of each segment.
- $f$ (selected bit count), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of selected bits per chunk.
- $M$ (address count), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of addresses.
- $A_{\rm rect}$ (counter length), bound on [Packed selected-bit addition](packed-bit-addition.md): An upper bound on the number of bits of every counter, the ceiling of log2(2V).
- $\rho$ (selected-bit offset), bound on [Packed selected-bit addition](packed-bit-addition.md): The offset of the lowest selected position, 0 <= rho < K.
- $j_i$ (selected position), bound on [Packed selected-bit addition](packed-bit-addition.md): The i-th selected bit position in a chunk.
- $g$ (guard value), bound on [Packed selected-bit addition](packed-bit-addition.md): The guard value of a segment, any g_i or h_i: its high K-1 bits.
- $g_i$ (y guard), bound on [Packed selected-bit addition](packed-bit-addition.md): The guard value of the i-th segment of y, with u_i = 2 g_i + a_i.
- $h_i$ (z guard), bound on [Packed selected-bit addition](packed-bit-addition.md): The guard value of the i-th segment of z, with w_i = 2 h_i + b_i.
- $a_i$ (y segment bit), bound on [Packed selected-bit addition](packed-bit-addition.md): The lowest bit of the i-th segment of y.
- $b_i$ (z segment bit), bound on [Packed selected-bit addition](packed-bit-addition.md): The lowest bit of the i-th segment of z.
- $u_i$ (y segment), bound on [Packed selected-bit addition](packed-bit-addition.md): The value of the i-th K-bit segment of y.
- $w_i$ (z segment), bound on [Packed selected-bit addition](packed-bit-addition.md): The value of the i-th K-bit segment of z.
- $c_i$ (segment control), bound on [Packed selected-bit addition](packed-bit-addition.md): The selected bit of x at j_i that controls the i-th pair of segments.
- $S_0$ (packed map), bound on [Packed selected-bit addition](packed-bit-addition.md): The composition of the eight packed cyclic shifts.
- $T_0$ (ideal map), bound on [Packed selected-bit addition](packed-bit-addition.md): The permutation of addresses that performs the required XORs at j_0 to j_{f-2}.
- $\mathcal B$ (exceptional addresses), bound on [Packed selected-bit addition](packed-bit-addition.md): The set of addresses where some guard of y or z lies outside [10, 2^{K-1}-11].
- $\delta_{\rm bad}$ (bad fraction), bound on [Packed selected-bit addition](packed-bit-addition.md): The bound min{1, 80(f-1)2^{-K}} on the fraction of exceptional addresses.
- $q$ (address), bound on [Packed selected-bit addition](packed-bit-addition.md): An address of a record after S_0; q' is its destination T_0 S_0^{-1}(q).
- $D$ (selected chunk count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of address chunks, at most d, on which the layer acts.
- $\mathcal S_D$ (phase diagonal), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The diagonal operator multiplying the value at address x by i to the sum of the D selected bits.
- $z$ (array), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The array of records that the operators act on.
- $e$ (group axis count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of selected axes in a group, e = mf.
- $h$ (slot index), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The index of a slot and of the residual basis vector placed in it.
- $v_h$ (residual vector), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A residual basis vector of an edge, in F_2^m.
- $\eta_h$ (direction sign), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The sign +1 or -1 giving the exponent of the kernel for v_h.
- $C_v$ (translation kernel), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The kernel aI + bX_v acting along the direction v.
- $X_v$ (column shift), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The operator shifting a column by v.
- $G$ (basis-change matrix), bound on [Simultaneous butterfly layer](simultaneous-layer.md): An invertible F_2 matrix whose first columns are the residual vectors.
- $\mathcal P_G$ (address permutation), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The permutation of addresses sending x to Gx.
- $e_h$ (standard basis vector), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The h-th standard basis vector of F_2^m.
- $q_0$ (individual chunk count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of leading chunks handled by individual C kernels.
- $A$ (chain length bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A(e) bounds the number of arithmetic operations along a chain from an input to an intermediate coefficient.
- $E$ (per-invocation bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The bound 64(W+m+1)^3 on the operations added by one invocation of the network.
- $B$ (level factor), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number s+E by which each recursion level multiplies the chain bound.
- $\varphi$ (bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A bound at least 1 on a chain length.
- $\nu$ (exponent of m), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The least j at least 1 with m^j at least B.
- $C_0$ (guard constant), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The constant 128 m B^2 in the number of reserved extra bits.
- $\ell$ (depth), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The depth of a value, the number of operations in sequence that produced it.

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

- $D$ means transformed axes here, but source group on [Matrix shear by triangular factorization](matrix-shear.md), which this page builds on: Use another letter, or say that D here is not the other page's D.
- $D$ means transformed axes here, but selected chunk count on [Simultaneous butterfly layer](simultaneous-layer.md), which this page builds on: Use another letter, or say that D here is not the other page's D.
- $K$ means chunk width here, but later tensor line on [Nested subspace labels and rank deficit](subspace-labels.md), which this page builds on: Use another letter, or say that K here is not the later tensor line / segment spacing.
- $K$ means chunk width here, but segment spacing on [Packed selected-bit addition](packed-bit-addition.md), which this page builds on: Use another letter, or say that K here is not the later tensor line / segment spacing.
- $\ell$ means long-axis address bits here, but depth on [Simultaneous butterfly layer](simultaneous-layer.md), which this page builds on: Use another letter, or say that ell here is the log of the length, not the depth of a value.
- $B$ means bit reversal here, but entries per row on [Elementary stream operations](stream-ops.md), which this page builds on: Use another letter, or say on this page that B means something else here than on the other page.
- $B$ means bit reversal here, but suffix bit count on [Controlled shifts and rational scalings](controlled-shifts.md), which this page builds on: Use another letter, or say on this page that B means something else here than on the other page.
- $B$ means bit reversal here, but complement of P on [Nested subspace labels and rank deficit](subspace-labels.md), which this page builds on: Use another letter, or say on this page that B means something else here than on the other page.
- $B$ means bit reversal here, but orthogonal complement on [Tensor products of subspaces](tensor-product-of-spaces.md), which this page builds on: Use another letter, or say on this page that B means something else here than on the other page.
- $B$ means bit reversal here, but level factor on [Simultaneous butterfly layer](simultaneous-layer.md), which this page builds on: Use another letter, or say on this page that B means something else here than on the other page.
- $b$ means leftover low bits here, but lowest bit on [Butterflies and the fast transform](butterfly.md), which this page builds on: Use another letter for this quantity, or say on this page that b is not the lowest bit of the output index (butterfly page / meaning given in the binding).
- $b$ means leftover low bits here, but field digit count on [Controlled shifts and rational scalings](controlled-shifts.md), which this page builds on: Use another letter for this quantity, or say on this page that b is not the lowest bit of the output index (butterfly page / meaning given in the binding).
- $b$ means leftover low bits here, but kernel coefficient b on [Two-point kernel C](phase-kernel.md), which this page builds on: Use another letter for this quantity, or say on this page that b is not the lowest bit of the output index (butterfly page / meaning given in the binding).
- $q$ means whole chunks here, but sequence length on [Discrete Fourier transform](dft.md), which this page builds on: Say that q is a number of whole chunks here, not the other page's q, or use another letter.
- $q$ means whole chunks here, but sequence length on [Cyclic convolution](convolution.md), which this page builds on: Say that q is a number of whole chunks here, not the other page's q, or use another letter.
- $q$ means whole chunks here, but digit radix on [Fast address-chunk interchange](address-interchange.md), which this page builds on: Say that q is a number of whole chunks here, not the other page's q, or use another letter.
- $q$ means whole chunks here, but radix on [Elementary stream operations](stream-ops.md), which this page builds on: Say that q is a number of whole chunks here, not the other page's q, or use another letter.
- $q$ means whole chunks here, but prime modulus base on [Controlled shifts and rational scalings](controlled-shifts.md), which this page builds on: Say that q is a number of whole chunks here, not the other page's q, or use another letter.
- $q$ means whole chunks here, but address on [Packed selected-bit addition](packed-bit-addition.md), which this page builds on: Say that q is a number of whole chunks here, not the other page's q, or use another letter.
- $L$ means layout permutation here, but linear map on [Contractions and bilinear contractions](contraction-maps.md), which this page builds on: Use another letter, or say that L here is not the other page's L.
- $L$ means layout permutation here, but total dimension loss on [Nested subspace labels and rank deficit](subspace-labels.md), which this page builds on: Use another letter, or say that L here is not the other page's L.
- $L$ means layout permutation here, but chunk bits on [Packed selected-bit addition](packed-bit-addition.md), which this page builds on: Use another letter, or say that L here is not the other page's L.
- $z$ means round input here, but suffix on [Fast address-chunk interchange](address-interchange.md), which this page builds on: Say that z is not the other page's z here, or use another letter.

## Previous version (revise it)

It has 432 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 540 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The tape layout arranges the address bits so that each round of a [synthetic polynomial transform](synthetic-transform.md) runs as one [simultaneous butterfly layer](simultaneous-layer.md) instead of one pass per axis.

Write $\ell=\log_2 r$, the address bits of a long axis, and $D=d-1$, the number of transformed axes. $K$ is the chunk width in bits; $\tau,\lambda'<1$ are the interchange and layer exponents. Axis $i$ has length $t_i\in\{2^{\ell-1},2^\ell\}$. With $\boldsymbol t=(t_1,\dots,t_D)$, $F_{\boldsymbol t}^-$ is the forward synthetic transform along all $D$ axes and $F_{\boldsymbol t}^+$ its opposite. Records are [fixed-point Gaussian dyadic records](fixed-point.md) with $\Theta(p)$ bits per coefficient and $d\ell=O(p)$, so a pass costs $O(Tp)$. Outputs keep the bit-reversed order of [retained frequency order](frequency-order.md), written $B$ along every axis.

A simultaneous layer needs a round's selected bits at a common offset in consecutive $K$-bit chunks <cite data-source="paper">we must place the selected bits of the participating axes at a common</cite>.

Call an axis long if it has $\ell$ address bits and short if $\ell-1$. Put $b=(\ell-1)\bmod K$ and $q=\lfloor(\ell-1)/K\rfloor$, so $\ell-1=qK+b$ (new meanings: $b$ counts leftover low bits of an axis, $q$ its whole chunks). Move to a prefix one at a time the top bit of each long axis and the $b$ lowest bits of each axis. At most $D(b+1)=O(dK)$ slots move, so the moves cost $O(TpdK)$ <cite data-source="paper">listed slots, so the moves cost $O(TpdK)$.</cite>

To group chunk 1 of every axis, then chunk 2, etc., scan target positions left to right, exchanging the chunk there with the required one if different. This needs at most $Dq-1$ exchanges, each made by the [fast address-chunk interchange](address-interchange.md) at cost $O(TpK^\tau)$, even for nonadjacent chunks <cite data-source="paper">exchanges of width-$K$ address chunks, even when the chunks are</cite>. Since $DqK\le d\ell=O(p)$, the exchanges cost $O(Tp\,DqK^\tau)=O(Tp\,(DqK)K^{\tau-1})=O(Tp\,pK^{\tau-1})$. The prefix moves and exchanges define the record permutation $L$; reversing them gives $L^{-1}$.

There are $b+1$ rounds on prefix slots and $qK$ on chunks, $\ell$ in all. A chunk round's selected bits share an offset in $D$ consecutive chunks, so one layer does it at cost $O(Tpd^{\lambda'})$; the chunk rounds cost $O(Tp\ell d^{\lambda'})$ in total <cite data-source="paper">$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.</cite> A prefix round handles at most $D$ bits individually at $O(Tp)$ each, so costs $O(Tpd)$; at most $b+1\le K$ such rounds cost $O(TpdK)$.

Each round is the contraction $\mathcal H$ (norm-nonincreasing), the signed coefficient permutation $J_E$, and one truncation $Q_p$. Truncation toward zero is odd and acts separately on each real and imaginary part, so for the array $z$ entering a round $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$: one truncation follows the exact round. The exact round does not increase the norm of the computed-versus-exact difference, and truncation moves each entry by less than $\sqrt2\,2^{-p}$; the permutations in $L$ are isometries and add no error. By the triangle inequality each round raises the error by less than $\sqrt2\,2^{-p}$, so from zero error the $\ell$ rounds leave error below $\sqrt2\,\ell\,2^{-p}$ <cite data-source="paper">zero error, at most $\ell$ rounds therefore</cite>.

Arithmetic on named slots after $L$ is conjugated by it. The forward procedure moves records by $L$ and then runs $BF_{\boldsymbol t}^-$, giving $(LBF_{\boldsymbol t}^-L^{-1})L=LBF_{\boldsymbol t}^-$. The opposite procedure runs its arithmetic and restores by $L^{-1}$, giving $L^{-1}(LF_{\boldsymbol t}^+B^{-1}L^{-1})=F_{\boldsymbol t}^+B^{-1}L^{-1}$. Both cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.

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

Write the body to `exegenius/tasks/0276-write-transform-layout.answer.md` and the JSON to `exegenius/tasks/0276-write-transform-layout.answer.json`, then run `exegenius submit 0276-write-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0276-write-transform-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
