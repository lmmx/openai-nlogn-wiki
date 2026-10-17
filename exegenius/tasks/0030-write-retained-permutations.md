# exegenius task 0030-write-retained-permutations

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
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records
- Error tracking and exact recovery
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
- Recursive power saving
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Fast address-chunk interchange (also: chunk swap, tape interchange)
- Packed selected-bit addition
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
- [Fast address-chunk interchange](address-interchange.md)
- [Elementary stream operations](stream-ops.md)
- [Discrete Fourier transform](dft.md)
- [Cyclic convolution](convolution.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Gaussian resampling](gaussian-resampling.md): Re-expressing a Fourier transform of prime length s through a transform of nearby power-of-two length t using Gaussian weights, so that only power-of-two transforms are needed.
  Shown as: Retained permutation cancellation *<predicate>* Gaussian resampling
- [Bluestein chirp identity](chirp.md): An identity that rewrites a (permuted) Fourier transform as a pointwise chirp phase, a cyclic convolution, and another chirp phase.
  Shown as: Retained permutation cancellation *<predicate>* Bluestein chirp identity

## Pages that build on this one

- The multiplication algorithm: Digits, then the CRT map, two forward transforms with resampling and chirps, a pointwise product, the opposite transform, rescaling, rounding and carry propagation yield the exact 2n-bit product.

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
- [Fast address-chunk interchange](address-interchange.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Multidimensional transforms](multidim-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Retained frequency order](frequency-order.md)
- [Two-point kernel C](phase-kernel.md)
- [Binary phase frames](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Parameter and prime-length choice](parameter-choice.md)
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

Write the body to `exegenius/tasks/0030-write-retained-permutations.answer.md` and the JSON to `exegenius/tasks/0030-write-retained-permutations.answer.json`, then run `exegenius submit 0030-write-retained-permutations` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0030-write-retained-permutations`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
