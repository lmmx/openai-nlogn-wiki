# exegenius task 0376-write-retained-permutations

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
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records (also: Z[i,1/2])
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Two-point kernel C (also: phase network kernel)
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

## This page

Concept: Retained permutation cancellation
Gloss: Leaving the coordinate permutations of resampling inside the transform identity, so the source permutation cancels across the two forward transforms and the opposite one and none is executed as a sort.

## This page in the argument

The step: The Fourier transforms of pairwise coprime prime lengths $s_i$ that the integer product needs are computed through power-of-two lengths $t_i$ by Gaussian resampling and Bluestein chirps, with the source and target coordinate permutations left inside the transform identities, so that none is executed as a sort.
How: Retain both permutations of Gaussian resampling in the transform formula: the target permutation $Q$ is absorbed by the chirp convolution, and the source permutation $R$ cancels across the two forward transforms, their pointwise product and the opposite transform.
Why: The usual implementation of Gaussian resampling sorts twice on each coordinate; keeping the permutations in the formula avoids the sorts, which would cost $\Theta(tp\log t)$ per line. (the sources say so: "connects these two shapes. Its usual implementation sorts twice on each" (paper))
Striking feature: No coordinate permutation is ever executed: the source permutation $R$ appears on both forward transforms and the opposite one and cancels, and the target permutation $Q$ is absorbed by the chirp convolution. (explain why it holds, from the method)

Its sub-steps, in order:

- For coprime $s<t$ with $\theta=t/s-1>p/\alpha^4$ and permutations $(P_su)_j=u_{tj}$, $(P_tv)_k=v_{-sk}$ there are linear contractions $A$, $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computed with error less than $p^2$ in time $O(tp^{3/2+\delta}\alpha)$ without executing $P_s$ or $P_t$. (on [Gaussian resampling](gaussian-resampling.md))
- Applied one coordinate line at a time to a padded box of $T=\prod_it_i$ entries, with $\gamma=2d\alpha^2$, $R F_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$, both $\mathcal A$ and $\mathcal B_0$ are contractions with error less than $dp^2$, computed in $O(dTp^{3/2+\delta}\alpha)$ plus $O(Tp\,d^2(1+\ell^\tau))$ for exposing lines.
- For even $t_i$ and the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$ one has $QF_{\boldsymbol t}u=\overline a\cdot\bigl(a*(\overline a\cdot u)\bigr)/T$, so the target permutation $Q$ is absorbed into a cyclic convolution of length $T$ and never executed. (on [Bluestein chirp identity](chirp.md))
- The retained source permutation cancels: $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=u*v/S^2$ with $S=\prod_is_i$, so no source permutation is executed across the two forward transforms, their pointwise product and the opposite transform.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.2, S4.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.2**: Applied one coordinate line at a time to a padded box of $T=\prod_it_i$ entries, with $\gamma=2d\alpha^2$, $R F_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$, both $\mathcal A$ and $\mathcal B_0$ are contractions with error less than $dp^2$, computed in $O(dTp^{3/2+\delta}\alpha)$ plus $O(Tp\,d^2(1+\ell^\tau))$ for exposing lines.
How: Tensor the one-dimensional identity over the $d$ axes, process axes one at a time keeping the padded box and zero lines, and expose each axis as the innermost field by adjacent axis interchanges using the chunk-interchange procedure.
- S4.2.1: Tensoring the one-dimensional identity gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$.
  Source: "=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A," (paper)
  > \begin{lemma}[Tensor interface] \label{lem:tensor-resampling} Suppose every pair $(s_i,t_i)$, $1\leq i\leq d$, satisfies Lemma~\ref{lem:no-sort-resampling} with the same $p,\alpha,\delta$. Put $T=\prod_i t_i$, $\gamma=2d\alpha^2$, and \[ R=\bigotimes_iP_{s_i},\quad Q=\bigotimes_iP_{t_i},\quad \mathcal A=\bigotimes_i A_i,\quad \mathcal B_0=\bigotimes_i B_{0,i}. \] Then \begin{equation} RF_{\boldsymbol s} =2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A, \qquad F_{\boldsymbol q}:=\bigotimes_iF_{q_i}. \label{eq:no-sort-tensor} \end{equation} Also write $F_{\boldsymbol q}^+=\bigotimes_iF_{q_i}^+$. Both $\mathcal A$ and $\mathcal B_0$ are contractions. The linewise implementations of $\mathcal A$ and $\mathcal B_0$ each have error less than $dp^2$. The total time spent in the one-dimensional algorithms for both maps is $O(dTp^{3/2+\delta}\alpha)$, with a constant independent of $d$.
- S4.2.2: The total time in the one-dimensional algorithms for both maps is $O(dTp^{3/2+\delta}\alpha)$ with a constant independent of $d$.
  Source: "$O(dTp^{3/2+\delta}\alpha)$, with a constant independent of $d$." (paper)
  > \begin{lemma}[Tensor interface] \label{lem:tensor-resampling} Suppose every pair $(s_i,t_i)$, $1\leq i\leq d$, satisfies Lemma~\ref{lem:no-sort-resampling} with the same $p,\alpha,\delta$. Put $T=\prod_i t_i$, $\gamma=2d\alpha^2$, and \[ R=\bigotimes_iP_{s_i},\quad Q=\bigotimes_iP_{t_i},\quad \mathcal A=\bigotimes_i A_i,\quad \mathcal B_0=\bigotimes_i B_{0,i}. \] Then \begin{equation} RF_{\boldsymbol s} =2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A, \qquad F_{\boldsymbol q}:=\bigotimes_iF_{q_i}. \label{eq:no-sort-tensor} \end{equation} Also write $F_{\boldsymbol q}^+=\bigotimes_iF_{q_i}^+$. Both $\mathcal A$ and $\mathcal B_0$ are contractions. The linewise implementations of $\mathcal A$ and $\mathcal B_0$ each have error less than $dp^2$. The total time spent in the one-dimensional algorithms for both maps is $O(dTp^{3/2+\delta}\alpha)$, with a constant independent of $d$.
- S4.2.3: Exposing and restoring all lines costs $O(Tp\,d^2(1+\ell^\tau))$ using the equal-width chunk-swap bound $O(Vu^\tau)$ and the fixed-digit movement primitive.
  Source: "then exposing and restoring all the lines costs" (paper)
  > If each $t_i\in\{r/2,r\}$ with $r=2^\ell$, the array is kept in the full padded box of $T$ entries, and each entry occupies $O(p)$ bits, then exposing and restoring all the lines costs \[ O\bigl(Tp\,d^2(1+\ell^\tau)\bigr) \] using the equal-width chunk-swap bound $O(Vu^\tau)$ and the fixed-digit movement primitive. Any fixed polynomial in $p$ of setup per line is negligible compared with $Tp$ when $r$ grows faster than every such polynomial and $d$ is polynomially bounded in $p$. \end{lemma}
- S4.2.4: Since $t_i\ge r/2$, each tensor map invokes at most $\sum_iT/t_i\le2dT/r$ lines, so setup of $O(p^c)$ per line is $o(Tp)$ because $r$ exceeds every power of $p$.
  Source: "Since $t_i\geq r/2$, each tensor map invokes at most" (paper)
  > Since $t_i\geq r/2$, each tensor map invokes at most $\sum_iT/t_i\leq2dT/r$ lines. For any fixed setup degree $c$, work $O(p^c)$ per line totals $O(dTp^c/r)=o(Tp)$: after division by $Tp$, the ratio is $O(dp^{c-1}/r)$, which tends to zero under the stated growth assumptions. This estimate includes local descriptor copying, validity tests per line, and preparing line boundaries. \end{proof}

**S4.4**: The retained source permutation cancels: $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=u*v/S^2$ with $S=\prod_is_i$, so no source permutation is executed across the two forward transforms, their pointwise product and the opposite transform.
How: Show $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$ by substituting $h=ck$ in the Fourier sum (each $t_i$ is a unit modulo $s_i$), use that permutations commute with pointwise products, then apply the convolution rule and $F^+F=I/S$.
- S4.4.1: For a unit $c$ modulo $q$ let $(R_cz)_j=z_{cj}$; substituting $h=ck$ in the Fourier sum gives $F_q^+R_c=R_c^{-1}F_q^+$.
  Source: "For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$. Substituting $h=ck$" (paper)
  > For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$. Substituting $h=ck$ in the Fourier sum gives \[ (F_q^+R_cz)_j =\frac1q\sum_{h=0}^{q-1}z_h e^{2\pi i h c^{-1}j/q} =(R_c^{-1}F_q^+z)_j. \] Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives $F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$. Also $(RF_{\boldsymbol s}u)\mathbin{\cdot}(RF_{\boldsymbol s}v) =R(F_{\boldsymbol s}u\mathbin{\cdot}F_{\boldsymbol s}v)$, because a coordinate permutation commutes with pointwise products. Therefore \[ RF_{\boldsymbol s}^+\bigl[R(F_{\boldsymbol s}u\mathbin{\cdot} F_{\boldsymbol s}v)\bigr] =F_{\boldsymbol s}^+(F_{\boldsymbol s}u\mathbin{\cdot}
- S4.4.2: Each $t_i$ is a unit modulo $s_i$, so tensoring gives $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.
  Source: "$RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$. Also" (paper)
  > For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$. Substituting $h=ck$ in the Fourier sum gives \[ (F_q^+R_cz)_j =\frac1q\sum_{h=0}^{q-1}z_h e^{2\pi i h c^{-1}j/q} =(R_c^{-1}F_q^+z)_j. \] Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives $F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$. Also $(RF_{\boldsymbol s}u)\mathbin{\cdot}(RF_{\boldsymbol s}v) =R(F_{\boldsymbol s}u\mathbin{\cdot}F_{\boldsymbol s}v)$, because a coordinate permutation commutes with pointwise products. Therefore \[ RF_{\boldsymbol s}^+\bigl[R(F_{\boldsymbol s}u\mathbin{\cdot} F_{\boldsymbol s}v)\bigr] =F_{\boldsymbol s}^+(F_{\boldsymbol s}u\mathbin{\cdot} F_{\boldsymbol s}v). \] The normalized convolution rule is $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\mathbin{\cdot} (F_{\boldsymbol s}v)$, while $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$. The two normalizations give \[ F_{\boldsymbol s}^+ (F_{\boldsymbol s}u\mathbin{\cdot}F_{\boldsymbol s}v) =
- S4.4.3: The normalized convolution rule is $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$, and $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$.
  Source: "The normalized convolution rule is" (paper)
  > ourier sum gives \[ (F_q^+R_cz)_j =\frac1q\sum_{h=0}^{q-1}z_h e^{2\pi i h c^{-1}j/q} =(R_c^{-1}F_q^+z)_j. \] Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives $F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$. Also $(RF_{\boldsymbol s}u)\mathbin{\cdot}(RF_{\boldsymbol s}v) =R(F_{\boldsymbol s}u\mathbin{\cdot}F_{\boldsymbol s}v)$, because a coordinate permutation commutes with pointwise products. Therefore \[ RF_{\boldsymbol s}^+\bigl[R(F_{\boldsymbol s}u\mathbin{\cdot} F_{\boldsymbol s}v)\bigr] =F_{\boldsymbol s}^+(F_{\boldsymbol s}u\mathbin{\cdot} F_{\boldsymbol s}v). \] The normalized convolution rule is $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\mathbin{\cdot} (F_{\boldsymbol s}v)$, while $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$. The two normalizations give \[ F_{\boldsymbol s}^+ (F_{\boldsymbol s}u\mathbin{\cdot}F_{\boldsymbol s}v) =\frac1S F_{\boldsymbol s}^+F_{\boldsymbol s}(u*v) =\frac{u*v}{S^2}, \] proving \eqref{eq:source-permutation-cancel}. Finally, conjugation changes the negative Fourier sign to the positive one and commutes with the real permutation $R$. It preserves both the disk grid and the norm, so conjugating the input and output also preserves an algorithm's error bound. \end{proof} \section{Exact integer multiplication and its cost} \label{sec:assembly}
- S4.4.4: The two normalizations give $F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=\frac1SF^+F(u*v)=u*v/S^2$.
  Source: "=\frac{u*v}{S^2}," (paper)
  > ot}(RF_{\boldsymbol s}v) =R(F_{\boldsymbol s}u\mathbin{\cdot}F_{\boldsymbol s}v)$, because a coordinate permutation commutes with pointwise products. Therefore \[ RF_{\boldsymbol s}^+\bigl[R(F_{\boldsymbol s}u\mathbin{\cdot} F_{\boldsymbol s}v)\bigr] =F_{\boldsymbol s}^+(F_{\boldsymbol s}u\mathbin{\cdot} F_{\boldsymbol s}v). \] The normalized convolution rule is $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\mathbin{\cdot} (F_{\boldsymbol s}v)$, while $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$. The two normalizations give \[ F_{\boldsymbol s}^+ (F_{\boldsymbol s}u\mathbin{\cdot}F_{\boldsymbol s}v) =\frac1S F_{\boldsymbol s}^+F_{\boldsymbol s}(u*v) =\frac{u*v}{S^2}, \] proving \eqref{eq:source-permutation-cancel}. Finally, conjugation changes the negative Fourier sign to the positive one and commutes with the real permutation $R$. It preserves both the disk grid and the norm, so conjugating the input and output also preserves an algorithm's error bound. \end{proof} \section{Exact integer multiplication and its cost} \label{sec:assembly}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S4.1 (on [Gaussian resampling](gaussian-resampling.md)): For coprime $s<t$ with $\theta=t/s-1>p/\alpha^4$ and permutations $(P_su)_j=u_{tj}$, $(P_tv)_k=v_{-sk}$ there are linear contractions $A$, $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computed with error less than $p^2$ in time $O(tp^{3/2+\delta}\alpha)$ without executing $P_s$ or $P_t$.
- S4.3 (on [Bluestein chirp identity](chirp.md)): For even $t_i$ and the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$ one has $QF_{\boldsymbol t}u=\overline a\cdot\bigl(a*(\overline a\cdot u)\bigr)/T$, so the target permutation $Q$ is absorbed into a cyclic convolution of length $T$ and never executed.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Multidimensional transforms](multidim-transform.md)
- [Elementary stream operations](stream-ops.md)
- [Discrete Fourier transform](dft.md)
- [Cyclic convolution](convolution.md)

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
- $\Omega$ (address set), bound on [Frames on wire arrays](array-frames.md): A finite set of addresses indexing every array.
- $\mathsf S_\Omega$ (pointwise network), bound on [Frames on wire arrays](array-frames.md): The network acting on all the wire arrays together, each gate applied at every address separately.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): The invertible R-linear operator on R^Omega assigned to the source, gate or sink v.
- $t$ (gate input count), bound on [Frames on wire arrays](array-frames.md): The number of input arrays of the gate G.
- $\rho$ (role permutation), bound on [Frames on wire arrays](array-frames.md): The map sending each input role w to its output role rho(w) in a signed role permutation.
- $\varepsilon_w$ (role sign), bound on [Frames on wire arrays](array-frames.md): The scalar sign carried by the route from input role w.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each of the two sequences being convolved.
- $d$ (axis count), bound on [Cyclic convolution](convolution.md): The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of cyclic axis i.
- $M$ (address count), bound on [Cyclic convolution](convolution.md): The number of cyclic addresses of an array, the product of the axis lengths.
- $T$ (coefficient count), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array.
- $u$ (first input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The first of the two n-bit integers being multiplied.
- $v$ (second input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The second of the two n-bit integers being multiplied (not the number of triples).
- $b$ (digit bits), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in one radix-2^b digit.
- $T$ (padded length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The padded length, a power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The length of the cyclic convolution, with T/2<S<T.
- $q$ (digit count), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of digits in each input, not the sequence length of the convolution page.
- $x$ (polynomial variable), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The indeterminate of the digit polynomials, evaluated at 2^b to recover the integers.
- $c_j$ (product coefficient), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The coefficient of x^j in the product of the two digit polynomials.
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
- $V$ (array volume), bound on [Elementary stream operations](stream-ops.md): The number of digits stored in the array.
- $\beta$ (radix), bound on [Elementary stream operations](stream-ops.md): The number of values one digit can take.
- $W$ (stream count), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams into which rows are dealt.
- $P$ (prefix count), bound on [Elementary stream operations](stream-ops.md): The number of prefix values of the array in item 4.
- $R$ (row count), bound on [Elementary stream operations](stream-ops.md): The number of rows in item 4; here R is not the scalar ring.
- $B$ (row length), bound on [Elementary stream operations](stream-ops.md): The number of entries per row in item 4.
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
- $d$ (axis count), bound on [Chinese-remainder address map](crt-map.md): The number of prime cyclic axes, with no coefficient axis counted.
- $s_i$ (axis length), bound on [Chinese-remainder address map](crt-map.md): The length of prime cyclic axis i; the s_i are pairwise coprime.
- $P_i$ (prefix product), bound on [Chinese-remainder address map](crt-map.md): The product of the axis lengths s_j with j<i.
- $\mu_i$ (coordinate exponent), bound on [Chinese-remainder address map](crt-map.md): The inverse of P_i modulo s_i, the exponent of x_i in the image of x.
- $\Phi$ (address map), bound on [Chinese-remainder address map](crt-map.md): The ring isomorphism sending x to the product of x_i^{mu_i}.
- $x_i$ (axis variable), bound on [Chinese-remainder address map](crt-map.md): The variable of axis i in the multi-axis ring.
- $k$ (coefficient index), bound on [Chinese-remainder address map](crt-map.md): A single coefficient index, an exponent of x; not an output index tuple as on the multidimensional-transform page.
- $a_j$ (mixed-radix digit), bound on [Chinese-remainder address map](crt-map.md): The digit of k of weight P_j, with 0<=a_j<s_j.
- $j$ (digit index), bound on [Chinese-remainder address map](crt-map.md): The index of an axis before axis i, in the product defining P_i, and later the index of a mixed-radix digit.
- $b_i$ (axis coordinate), bound on [Chinese-remainder address map](crt-map.md): The axis-i coordinate of Phi(x^k).
- $\ell$ (address bits), bound on [Chinese-remainder address map](crt-map.md): The number of address bits of an axis of length r.
- $T$ (padded record count), bound on [Chinese-remainder address map](crt-map.md): The number of padded records, the product of the padded axis lengths t_i.
- $\tau$ (interchange exponent), bound on [Chinese-remainder address map](crt-map.md): A fixed exponent below 1 in the chunk-interchange cost.
- $i$ (axis index), bound on [Chinese-remainder address map](crt-map.md): The index of a prime cyclic axis, from 1 to d.
- $t_i$ (padded axis length), bound on [Chinese-remainder address map](crt-map.md): The length of axis i after zero padding, a power of two between r/2 and r.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the Fourier transform being re-expressed, coprime to t.
- $t$ (transform length), bound on [Gaussian resampling](gaussian-resampling.md): The larger length, a power of two, of the transform through which the length-s transform is expressed.
- $\alpha$ (width parameter), bound on [Gaussian resampling](gaussian-resampling.md): The integer width parameter of the Gaussian weights, with 2<=alpha<sqrt p.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): The relative gap t/s-1 between the target and source lengths.
- $j$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A single integer coordinate index.
- $k$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A single integer coordinate index.
- $q_j$ (nearest coordinate), bound on [Gaussian resampling](gaussian-resampling.md): The integer nearest to tj/s.
- $\beta_j$ (rounding offset), bound on [Gaussian resampling](gaussian-resampling.md): The signed distance tj/s-q_j from tj/s to the nearest integer.
- $E$ (Neumann error), bound on [Gaussian resampling](gaussian-resampling.md): The map N-I, whose norm is small.
- $K$ (series term count), bound on [Gaussian resampling](gaussian-resampling.md): The number of terms of the Neumann series that are kept.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Gaussian resampling](gaussian-resampling.md): Re-expressing a Fourier transform of prime length s through a transform of nearby power-of-two length t using Gaussian weights, so that only power-of-two transforms are needed.
  Shown as: Retained permutation cancellation *<predicate>* Gaussian resampling
- [Bluestein chirp identity](chirp.md): An identity that rewrites a (permuted) Fourier transform as a pointwise chirp phase, a cyclic convolution, and another chirp phase.
  Shown as: Retained permutation cancellation *<predicate>* Bluestein chirp identity

## Pages that build on this one

- The multiplication algorithm: Digits, then the CRT map, two forward transforms with resampling and chirps, a pointwise product, the opposite transform, rescaling, rounding and carry propagation yield the exact 2n-bit product.

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
- [Synthetic polynomial transform](synthetic-transform.md)
- [Elementary stream operations](stream-ops.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Two-point kernel C](phase-kernel.md)
- [Contractions and bilinear contractions](contraction-maps.md)
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Retained frequency order](frequency-order.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [Tensor products of subspaces](tensor-product-of-spaces.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Binary phase frames](phase-frames.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "retains the source and target coordinate permutations in the transform identity" (paper)

  > The remaining proof places these procedures inside the multiplication reduction and accounts for every change of representation. First, the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. Section~\ref{sec:assembly} implements this map through triangular controlled shifts and charged axis moves. Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform. Section~\ref{sec:resampling} retains the source and target coordinate permutations in the transform identity, so they need not be executed as separate full sorts.

- "The second identity shows how the retained source permutation $R$ cancels when computing a convolution." (paper)

  > The factor $QF_{\boldsymbol t}$ in \eqref{eq:no-sort-tensor} can be computed from a cyclic convolution and two pointwise phase multiplications. The chirp identity below performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array. The second identity shows how the retained source permutation $R$ cancels when computing a convolution. Here $*$ denotes cyclic convolution on the product of the coordinate groups and a dot denotes coordinatewise multiplication.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- A simulated reader (reader) trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" got stuck at "Its usual implementation sorts twice on each coordinate.": The page says the usual implementation sorts but never says what a sort costs on a Turing machine tape or why it is expensive enough to avoid. I could not connect a permutation of array positions to any cost I know, so the motivation for the whole question rests on this unexplained claim. (stuck at the beyond level)
- A simulated reader (reader) trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" got stuck at "$B_0$ is not the packing base": I could not decode 'packing base', and the page gives no definition. I did not need it for the permutation argument, but it is an undefined term in the sentence that introduces B_0. (stuck at the symbol level)
- A simulated reader (reader) trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" got stuck at "$(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=u*v/S^2$": I followed the algebra: F^+ R_beta = R_beta^{-1} F^+ and R commutes with pointwise products give the cancellation. But the page never says why the opposite transform is written with R in front (RF^+) in the first place. I got past this by accepting the formula as stated, without seeing why the output of the convolution should be read in the permuted order. (the reader followed the steps but not why they lead where they do: say what this step is for)
- A simulated reader (reader) trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" got stuck at "Its usual implementation sorts twice on each coordinate.": The page says the usual implementation sorts and that the new method does not, but nowhere I opened says what a sort costs on the tape machine, so I could not see why leaving the permutations inside the identity is worth doing. I accepted the avoidance of sorting on trust. (stuck at the beyond level)
- A simulated reader (reader) trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" got stuck at "The target permutation $Q$ is absorbed by the": The word absorbed is used without a definition on this page. I took it to mean that the permutation is folded into a convolution, which the Bluestein chirp identity page confirms, but the word itself was new. (stuck at the symbol level)
- Simulated readers trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" could not work out: Executing the permutations would mean sorting data on a tape, costing about t p log t per line, which would cancel the power saving.. A reader with the stated background should be able to get this from this page and the pages it builds on.

## Previous version (revise it)

It has 450 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 562 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Retained permutation cancellation computes the prime-length Fourier transforms of the integer product through power-of-two ones without executing any coordinate permutation as a sort: the permutations of Gaussian resampling stay inside the transform identity, where one is absorbed by a convolution and the other cancels.

Take $d$ axes with pairwise coprime prime lengths $s_i$ and power-of-two lengths $t_i>s_i$ (so $\gcd(s_i,t_i)=1$ for odd $s_i$). Write $\boldsymbol s=(s_1,\dots,s_d)$, $\boldsymbol t=(t_1,\dots,t_d)$, $S=\prod_is_i$, $T=\prod_it_i$. For operators $X_i$ acting on vectors of length $q_i$, $\bigotimes_iX_i$ applies $X_i$ along every line of axis $i$. Operators on different axes touch different indices, so $\bigl(\bigotimes_iX_i\bigr)\bigl(\bigotimes_iY_i\bigr)=\bigotimes_iX_iY_i$ for further operators $Y_i$.

For a vector $z$ of $q$ complex entries, the normalized [discrete Fourier transform](dft.md) is $(F_qz)_k=\frac1q\sum_{j=0}^{q-1}z_je^{-2\pi ijk/q}$, and $F_q^+$, the opposite transform, is the same with the exponent's sign reversed. Since $\sum_k e^{2\pi i k(j-j')/q}$ is $q$ if $j=j'$ and $0$ otherwise, $F_q^+F_q=I/q$. For axis lengths $\boldsymbol q$, $F_{\boldsymbol q}=\bigotimes_iF_{q_i}$ and $F_{\boldsymbol q}^+=\bigotimes_iF_{q_i}^+$, so $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$.

Each prime-length transform is computed through a power-of-two one by [Gaussian resampling](gaussian-resampling.md). Its usual implementation sorts twice on each coordinate <cite data-source="paper">Its usual implementation sorts twice on each</cite>. For one axis, with $p$, $\alpha$, $\delta$ as there, let $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$ ($u,v$ are complex arrays here, not integers). That page gives linear contractions $A$, $B_0$ ($B_0$ is not the packing base) with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computed in time $O(tp^{3/2+\delta}\alpha)$ without executing $P_s$ or $P_t$.

Tensor this identity over the axes. Put $R=\bigotimes_iP_{s_i}$ (a permutation, not a ring), $Q=\bigotimes_iP_{t_i}$, $\mathcal A=\bigotimes_iA_i$, $\mathcal B_0=\bigotimes_iB_{0,i}$. By the product rule the left sides combine to $RF_{\boldsymbol s}$ and the right sides to $\mathcal B_0QF_{\boldsymbol t}\mathcal A$ times $d$ factors $2^{2\alpha^2}$, so $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$. Both $\mathcal A$ and $\mathcal B_0$ are contractions, applied one line at a time in a padded box of $T$ entries. Errors and times add over the $d$ passes: error below $dp^2$, time $O(dTp^{3/2+\delta}\alpha)$ with a constant independent of $d$.

Each axis is exposed as the innermost field by the [fast address-chunk interchange](address-interchange.md). With $\ell$ the number of address bits of an axis of length $r=2^\ell$, $\tau<1$ the interchange exponent, each $t_i\in\{r/2,r\}$ and each entry of $O(p)$ bits, exposing and restoring all lines of the padded box costs $O\bigl(Tp\,d^2(1+\ell^\tau)\bigr)$ <cite data-source="paper">If each $t_i\in\{r/2,r\}$ with $r=2^\ell$, the array is kept in the
full padded box of $T$ entries, and each entry occupies $O(p)$ bits,
then exposing and restoring all the lines costs</cite>. Since $t_i\ge r/2$, each tensor map invokes at most $\sum_iT/t_i\le 2dT/r$ lines, so setup work $O(p^\nu)$ per line, with $\nu$ a fixed exponent, totals $O(dTp^\nu/r)$. Dividing by $Tp$ gives $O(dp^{\nu-1}/r)\to0$ when $r$ outgrows every power of $p$ and $d$ is polynomially bounded in $p$, so setup is $o(Tp)$.

The target permutation $Q$ is absorbed by the [Bluestein chirp identity](chirp.md). For even $t_i$ and $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$ one has $QF_{\boldsymbol t}u=\overline a\cdot\bigl(a*(\overline a\cdot u)\bigr)/T$, with $*$ the [cyclic convolution](convolution.md) and a dot coordinatewise multiplication. So $Q$ is part of a convolution of length $T$ and never executed.

The source permutation $R$ cancels: $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=u*v/S^2$. For a unit $\beta$ modulo $q$, let $(R_\beta z)_j=z_{\beta j}$. Then $(F_q^+R_\beta z)_j=\frac1q\sum_w z_{\beta w}e^{2\pi i wj/q}$, where $w$ is the summation index. Substituting $w'=\beta w$, with $w'$ the new summation index, gives $\frac1q\sum_{w'}z_{w'}e^{2\pi i w'\beta^{-1}j/q}$, which is $(R_\beta^{-1}F_q^+z)_j$. Hence $F_q^+R_\beta=R_\beta^{-1}F_q^+$. Each $t_i$ is a unit modulo $s_i$, and $R$ applies $R_{t_i}$ on axis $i$, so tensoring gives $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$. A permutation commutes with pointwise products, so the left side equals $F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)$. The normalized convolution rule is $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$, and $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$, so this equals $\frac1SF_{\boldsymbol s}^+F_{\boldsymbol s}(u*v)=u*v/S^2$.

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

Write the body to `exegenius/tasks/0376-write-retained-permutations.answer.md` and the JSON to `exegenius/tasks/0376-write-retained-permutations.answer.json`, then run `exegenius submit 0376-write-retained-permutations` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0376-write-retained-permutations`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
