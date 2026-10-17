# exegenius task 0092-write-frequency-order

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
- Schönhage–Strassen optimality conjecture (also: n log n conjecture)
- Cyclic convolution
- Multiplication as radix-digit convolution
- Discrete Fourier transform (also: Fourier transform, DFT)
- Butterflies and the fast transform (also: transform levels)
- Bluestein chirp identity (also: chirp transform)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Fixed-point Gaussian dyadic records (also: Z[i,1/2])
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
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

## This page

Concept: Retained frequency order
Gloss: The forward synthetic transform writes its outputs in bit-reversed order, the pointwise product keeps that order, and the opposite transform consumes it, so no reordering is executed.

## This page in the argument

The step: The synthetic transform $F_t^-$ over $\mathcal R_r=\mathbb C[y]/(y^r+1)$, with roots of unity $\omega_t=y^{2r/t}$, is computed by decimation in frequency with outputs written in bit-reversed order, $B_tF_t^-$; the pointwise product keeps this order and the reverse procedure computes $F_t^+B_t^{-1}$, so no reordering is executed.
How: Prove character cancellation directly (the ring has zero divisors), derive the decimation-in-frequency recursion with twiddles $\omega_t^{-k}$, track which named slots hold frequency bits after each round, and run the recursion in reverse for the opposite transform.
Why: The ring has zero divisors, so inverting the transform cannot divide by $\omega_t^j-1$ and orthogonality of characters must be checked by a direct pairing argument; writing outputs where the recursion leaves them (bit-reversed) avoids a sort. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- For $t$ a power of two dividing $2r$ define $\omega_t=y^{2r/t}$; every power of $\omega_t$ is an isometry, so the normalized transforms are contractions.
- Character cancellation: $\sum_{k=0}^{t-1}\omega_t^{jk}$ equals $t$ if $t\mid j$ and $0$ otherwise, hence $F_t^+F_t^-=t^{-1}I$.
- For $t\nmid j$, writing $j=2^vj_0$ with $j_0$ odd, replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies the sum by $y^{rj_0}=-1$.
- Hence the sum is zero, since the additive group of $\mathcal R_r$ has no two-torsion.
- Decimation in frequency pairs $z_k$ with $z_{k+t/2}$: $(F_t^-z)_{2h+b}=\frac1{t/2}\sum_k(\omega_t^2)^{-hk}\omega_t^{-bk}\frac{z_k+(-1)^bz_{k+t/2}}2$, i.e. apply $H_0$, multiply the $b=1$ output by $\omega_t^{-k}$, and recurse on the two branches.
- After all $a$ rounds the named slots from high to low hold the frequency bits from low to high, so $(F_t^-z)_j$ is stored at slot $\operatorname{rev}_a(j)$ ($B_t$ moves the entry at $j$ to $\operatorname{rev}_a(j)$), without moving whole frequency indices.
- The reverse procedure runs the levels backwards; as $H_0^2=I/2$ each reversed level is half the inverse of the forward level, over $a=\log_2t$ levels.
- The reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$, so it equals $F_t^+B_t^{-1}$ by character cancellation.
- The two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.
- For several axes the individual steps group into one parallel butterfly $\mathcal H$ followed by one recordwise monomial $J_E$ that multiplies the record by $y^E$.
- The combined exponent is $E=-\sum_i\frac{2r}{u_i}b_ik_i\pmod{2r}$, depending on the address (current length $u_i$, new branch bit $b_i$, encoded $k_i$), not on coefficient values.
- Each $\mathcal H$ is a contraction and each $J_E$ an isometry, so every completed round is a contraction.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- Synthetic transforms over $\mathcal R_r$ on $d-1$ axes of lengths $t_i\in\{2^{\ell-1},2^\ell\}$ with outputs kept in a retained layout $LB$ cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error less than $\sqrt2\ell\,2^{-p}$.; how: Use the radix-two synthetic (Nussbaumer) transform, whose twiddles are signed shifts, and lay out the selected bits of all participating axes at a common offset in $K$-bit chunks so that every round is one simultaneous butterfly layer, with fewer than $\log t$ passes. (on [Tape layout for synthetic transforms](transform-layout.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.1.1, S2.1.2, S2.1.3, S2.1.4, S2.1.5, S2.1.6, S2.1.7, S2.1.8, S2.1.9, S2.1.10, S2.1.11, S2.1.12). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.1.1**: For $t$ a power of two dividing $2r$ define $\omega_t=y^{2r/t}$; every power of $\omega_t$ is an isometry, so the normalized transforms are contractions.
Source: "For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$." (paper)
> For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$. For $z\in\mathcal R_r^t$ and $0\leq j<t$, set \[ (F_t^-z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{-jk}z_k, \qquad (F_t^+z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{jk}z_k. \] Every power of $\omega_t$ is an isometry, and each transform entry is an average of $t$ such images. Thus both transforms are contractions. The ring has zero divisors, so we verify character cancellation directly instead of dividing by $\omega_t^j-1$.

**S2.1.2**: Character cancellation: $\sum_{k=0}^{t-1}\omega_t^{jk}$ equals $t$ if $t\mid j$ and $0$ otherwise, hence $F_t^+F_t^-=t^{-1}I$.
Source: "=\begin{cases}t,&t\mid j,\\0,&t\nmid j.\end{cases}" (paper)
> \begin{lemma}[Synthetic character cancellation] \label{lem:synthetic-characters} If $j$ is an integer, then \[ \sum_{k=0}^{t-1}\omega_t^{jk} =\begin{cases}t,&t\mid j,\\0,&t\nmid j.\end{cases} \qquad F_t^+F_t^-=t^{-1}I. \] \end{lemma} \begin{proof} Only the second case needs proof. Write $j=2^v j_0$ with $j_0$ odd and $0\leq v<\log_2t$. Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies their sum by $y^{rj_0}=-1$. Hence the sum is zero, since the additive group of $\mathcal R_r$ has no two-torsion. Expanding the composite transforms and applying this identity proves the final formula. \end{proof}

**S2.1.3**: For $t\nmid j$, writing $j=2^vj_0$ with $j_0$ odd, replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies the sum by $y^{rj_0}=-1$.
Source: "Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes" (paper)
> \begin{lemma}[Synthetic character cancellation] \label{lem:synthetic-characters} If $j$ is an integer, then \[ \sum_{k=0}^{t-1}\omega_t^{jk} =\begin{cases}t,&t\mid j,\\0,&t\nmid j.\end{cases} \qquad F_t^+F_t^-=t^{-1}I. \] \end{lemma} \begin{proof} Only the second case needs proof. Write $j=2^v j_0$ with $j_0$ odd and $0\leq v<\log_2t$. Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies their sum by $y^{rj_0}=-1$. Hence the sum is zero, since the additive group of $\mathcal R_r$ has no two-torsion. Expanding the composite transforms and applying this identity proves the final formula. \end{proof}

**S2.1.4**: Hence the sum is zero, since the additive group of $\mathcal R_r$ has no two-torsion.
Source: "$y^{rj_0}=-1$.  Hence the sum is zero, since the additive group of" (paper)
> \begin{lemma}[Synthetic character cancellation] \label{lem:synthetic-characters} If $j$ is an integer, then \[ \sum_{k=0}^{t-1}\omega_t^{jk} =\begin{cases}t,&t\mid j,\\0,&t\nmid j.\end{cases} \qquad F_t^+F_t^-=t^{-1}I. \] \end{lemma} \begin{proof} Only the second case needs proof. Write $j=2^v j_0$ with $j_0$ odd and $0\leq v<\log_2t$. Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies their sum by $y^{rj_0}=-1$. Hence the sum is zero, since the additive group of $\mathcal R_r$ has no two-torsion. Expanding the composite transforms and applying this identity proves the final formula. \end{proof}

**S2.1.5**: Decimation in frequency pairs $z_k$ with $z_{k+t/2}$: $(F_t^-z)_{2h+b}=\frac1{t/2}\sum_k(\omega_t^2)^{-hk}\omega_t^{-bk}\frac{z_k+(-1)^bz_{k+t/2}}2$, i.e. apply $H_0$, multiply the $b=1$ output by $\omega_t^{-k}$, and recurse on the two branches.
Source: "\frac{z_k+(-1)^b z_{k+t/2}}2." (paper)
> Write \[ H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}. \] The length-one procedure is the identity. For $t\geq2$, the decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for $0\leq k<t/2$. The two outputs of $H_0$ occupy these same slots, whose high address bit is $b=0$ or $b=1$, respectively. Multiply the $b=1$ output by $\omega_t^{-k}$, and then apply the length-$t/2$ procedure separately within the two branches. This computes $F_t^-$ because, for $b\in\{0,1\}$, \begin{equation} (F_t^-z)_{2h+b} =\frac1{t/2}\sum_{k=0}^{t/2-1} (\omega_t^2)^{-hk}\omega_t^{-bk} \frac{z_k+(-1)^b z_{k+t/2}}2. \label{eq:synthetic-dif} \end{equation} To follow the recursion, name the original address-bit slots of an axis of length $t=2^a$ by $a-1,\ldots,0$, from most to least significant. For $0\leq s\leq a$, after $s$ levels the values of the first $s$ named slots are branch bits $b_0,\ldots,b_{s-1}$. Equation~\eqref{eq:synthetic-dif} identifies these as frequency bits $0,\ldots,s-1$, numbered from the least significant bit. The remaining slots encode an index in $[0,u)$, where $u=t/2^s$. When $s<a$, the next level uses slot $h=a-1-s$ to distinguish the paired inputs and then to hold $b_s$. Writing $x_v$ for the bit in a still unprocessed slot $v$, the index used by its twiddle is \[ k=\sum_{v=0}^{h-1}2^v x_v,\qquad 0\l

**S2.1.6**: After all $a$ rounds the named slots from high to low hold the frequency bits from low to high, so $(F_t^-z)_j$ is stored at slot $\operatorname{rev}_a(j)$ ($B_t$ moves the entry at $j$ to $\operatorname{rev}_a(j)$), without moving whole frequency indices.
Source: "$\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the" (paper)
> After all $a$ rounds, the named slots from high to low therefore contain the frequency bits from low to high. If $\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$. Let $B_t$ denote this record permutation: it moves the entry at $j$ to $\operatorname{rev}_a(j)$. The recursion writes its outputs directly in this order; it does not move whole frequency indices.

**S2.1.7**: The reverse procedure runs the levels backwards; as $H_0^2=I/2$ each reversed level is half the inverse of the forward level, over $a=\log_2t$ levels.
Source: "of the corresponding forward level.  There are $a=\log_2t$ levels," (paper)
> The procedure consuming this stored order traverses the recursion in reverse: first process the two smaller branches, then apply the inverse monomial to the second branch, and finally apply $H_0$. Each forward level is invertible, since both its butterfly and its monomial are invertible. As $H_0^2=I/2$, the reversed level is half the inverse of the corresponding forward level. There are $a=\log_2t$ levels, so the reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$. Lemma~\ref{lem:synthetic-characters} gives the same composite for $F_t^+B_t^{-1}$ with $B_tF_t^-$. The forward procedure is invertible, so these two reverse operators agree. Thus the two exact procedures implement \begin{equation} B_tF_t^-,\qquad F_t^+B_t^{-1}, \label{eq:stored-opposite} \end{equation} respectively.

**S2.1.8**: The reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$, so it equals $F_t^+B_t^{-1}$ by character cancellation.
Source: "so the reverse procedure composed with $B_tF_t^-$ is" (paper)
> The procedure consuming this stored order traverses the recursion in reverse: first process the two smaller branches, then apply the inverse monomial to the second branch, and finally apply $H_0$. Each forward level is invertible, since both its butterfly and its monomial are invertible. As $H_0^2=I/2$, the reversed level is half the inverse of the corresponding forward level. There are $a=\log_2t$ levels, so the reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$. Lemma~\ref{lem:synthetic-characters} gives the same composite for $F_t^+B_t^{-1}$ with $B_tF_t^-$. The forward procedure is invertible, so these two reverse operators agree. Thus the two exact procedures implement \begin{equation} B_tF_t^-,\qquad F_t^+B_t^{-1}, \label{eq:stored-opposite} \end{equation} respectively.

**S2.1.9**: The two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.
Source: "B_tF_t^-,\qquad F_t^+B_t^{-1}," (paper)
> The procedure consuming this stored order traverses the recursion in reverse: first process the two smaller branches, then apply the inverse monomial to the second branch, and finally apply $H_0$. Each forward level is invertible, since both its butterfly and its monomial are invertible. As $H_0^2=I/2$, the reversed level is half the inverse of the corresponding forward level. There are $a=\log_2t$ levels, so the reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$. Lemma~\ref{lem:synthetic-characters} gives the same composite for $F_t^+B_t^{-1}$ with $B_tF_t^-$. The forward procedure is invertible, so these two reverse operators agree. Thus the two exact procedures implement \begin{equation} B_tF_t^-,\qquad F_t^+B_t^{-1}, \label{eq:stored-opposite} \end{equation} respectively.

**S2.1.10**: For several axes the individual steps group into one parallel butterfly $\mathcal H$ followed by one recordwise monomial $J_E$ that multiplies the record by $y^E$.
Source: "butterfly $\mathcal H$, followed by one recordwise monomial operation" (paper)
> For $D$ axes of lengths $t_1,\ldots,t_D$, put \[ M=\prod_{i=1}^D t_i,\qquad F_{\boldsymbol t}^\pm=\bigotimes_{i=1}^D F_{t_i}^\pm, \qquad B=\bigotimes_{i=1}^D B_{t_i}. \] A round applies one current $H_0$ on each participating axis. The twiddle for axis $i$ depends only on that axis's address bits. The two entries paired by another axis's butterfly have the same axis-$i$ address, so that twiddle commutes with the other butterfly. Consequently the individual axis steps may be grouped as a parallel butterfly $\mathcal H$, followed by one recordwise monomial operation $J_E$. At each address, $J_E$ multiplies the record by \begin{equation} y^{E},\qquad E=-\sum_{i\ \mathrm{participating}} \frac{2r}{u_i}\,b_i k_i\pmod{2r}. \label{eq:combined-twiddle} \end{equation} Here $u_i$ is that axis's current recursive length, $b_i$ its newly written branch bit, and $0\leq k_i<u_i/2$ is encoded by its still unprocessed named slots. The exponent depends on the address, not on coefficient values. In the opposite direction the grouped round is $\mathcal HJ_E^{-1}$: apply $y^{-E}$ first and the parallel butterfly second. Each $\mathcal H$ is a contraction and each $J_E$ is an isometry, so every completed round is a contraction.

**S2.1.11**: The combined exponent is $E=-\sum_i\frac{2r}{u_i}b_ik_i\pmod{2r}$, depending on the address (current length $u_i$, new branch bit $b_i$, encoded $k_i$), not on coefficient values.
Source: "E=-\sum_{i\ \mathrm{participating}}" (paper)
> For $D$ axes of lengths $t_1,\ldots,t_D$, put \[ M=\prod_{i=1}^D t_i,\qquad F_{\boldsymbol t}^\pm=\bigotimes_{i=1}^D F_{t_i}^\pm, \qquad B=\bigotimes_{i=1}^D B_{t_i}. \] A round applies one current $H_0$ on each participating axis. The twiddle for axis $i$ depends only on that axis's address bits. The two entries paired by another axis's butterfly have the same axis-$i$ address, so that twiddle commutes with the other butterfly. Consequently the individual axis steps may be grouped as a parallel butterfly $\mathcal H$, followed by one recordwise monomial operation $J_E$. At each address, $J_E$ multiplies the record by \begin{equation} y^{E},\qquad E=-\sum_{i\ \mathrm{participating}} \frac{2r}{u_i}\,b_i k_i\pmod{2r}. \label{eq:combined-twiddle} \end{equation} Here $u_i$ is that axis's current recursive length, $b_i$ its newly written branch bit, and $0\leq k_i<u_i/2$ is encoded by its still unprocessed named slots. The exponent depends on the address, not on coefficient values. In the opposite direction the grouped round is $\mathcal HJ_E^{-1}$: apply $y^{-E}$ first and the parallel butterfly second. Each $\mathcal H$ is a contraction and each $J_E$ is an isometry, so every completed round is a contraction.

**S2.1.12**: Each $\mathcal H$ is a contraction and each $J_E$ an isometry, so every completed round is a contraction.
Source: "$J_E$ is an isometry, so every completed round is a contraction." (paper)
> For $D$ axes of lengths $t_1,\ldots,t_D$, put \[ M=\prod_{i=1}^D t_i,\qquad F_{\boldsymbol t}^\pm=\bigotimes_{i=1}^D F_{t_i}^\pm, \qquad B=\bigotimes_{i=1}^D B_{t_i}. \] A round applies one current $H_0$ on each participating axis. The twiddle for axis $i$ depends only on that axis's address bits. The two entries paired by another axis's butterfly have the same axis-$i$ address, so that twiddle commutes with the other butterfly. Consequently the individual axis steps may be grouped as a parallel butterfly $\mathcal H$, followed by one recordwise monomial operation $J_E$. At each address, $J_E$ multiplies the record by \begin{equation} y^{E},\qquad E=-\sum_{i\ \mathrm{participating}} \frac{2r}{u_i}\,b_i k_i\pmod{2r}. \label{eq:combined-twiddle} \end{equation} Here $u_i$ is that axis's current recursive length, $b_i$ its newly written branch bit, and $0\leq k_i<u_i/2$ is encoded by its still unprocessed named slots. The exponent depends on the address, not on coefficient values. In the opposite direction the grouped round is $\mathcal HJ_E^{-1}$: apply $y^{-E}$ first and the parallel butterfly second. Each $\mathcal H$ is a contraction and each $J_E$ is an isometry, so every completed round is a contraction.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $y$ (ring variable), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The indeterminate of the polynomials, satisfying y^r = -1 in the ring.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The number of complex coefficients in a polynomial of the ring, always a power of two.
- $n$ (bit length), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): The number of bits in each of the two integers being multiplied.
- $\kappa$ (saving exponent), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant by which the exponent of the logarithm in the running time is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the stored grid, so values are integers divided by 2^p.
- $k$ (operation count), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations applied since the layer began.
- $\Delta$ (extra reserved bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the number of operations charged to the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The single truncation that drops the bits below 2^{-p} in each real and imaginary part.
- $h$ (ground-set size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of the ground set $[h]$ whose three-element subsets index the banks.
- $v$ (number of triples), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of three-element subsets of $[h]$.
- $N$ (bank size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of wires in each data bank.
- $m$ (label-space dimension), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The dimension of the label space used later.
- $I$ (invocation count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of invocations.
- $z_{\rm b}$ (bit neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the bit construction.
- $z_{\rm c}$ (complex neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the complex construction.
- $c_{\rm b}$ (bit central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the bit network.
- $W_{\rm c}$ (complex wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the complex network.
- $R$ (scalar ring), bound on [Frames on wire arrays](array-frames.md): The ring of scalars carried by the wires.
- $\Omega$ (address set), bound on [Frames on wire arrays](array-frames.md): A finite set of addresses indexing every wire's array.
- $\mathsf S_\Omega$ (pointwise network), bound on [Frames on wire arrays](array-frames.md): The network obtained by applying every scalar gate pointwise at each address, acting on all wire arrays together.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): An invertible R-linear operator on R^Omega assigned to a source, gate or sink v.
- $D_{\rm in}$ (input frame), bound on [Frames on wire arrays](array-frames.md): The direct sum of the source frames over the input roles.
- $D_{\rm out}$ (output frame), bound on [Frames on wire arrays](array-frames.md): The direct sum of the sink frames over the output roles.
- $\rho$ (role permutation), bound on [Frames on wire arrays](array-frames.md): The map sending each input role to its output role in a signed role permutation.
- $\varepsilon_w$ (route sign), bound on [Frames on wire arrays](array-frames.md): The scalar sign of the route from input role w.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each of the two sequences being convolved.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of axis i of the array.
- $M$ (cyclic addresses), bound on [Cyclic convolution](convolution.md): The number of cyclic addresses on the first d-1 axes, the product of t_i for i<d.
- $T$ (total coefficients), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array, rM.
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
- $x_d$ (last-axis variable), bound on [Phase twist](phase-twist.md): The variable of the last cyclic axis, with x_d^r = 1.
- $\zeta$ (twist phase), bound on [Phase twist](phase-twist.md): The number e^{\pi i/r}, a primitive 2r-th root of unity with \zeta^r = -1.
- $\Theta$ (twist map), bound on [Phase twist](phase-twist.md): The ring isomorphism from C[x_d]/(x_d^r-1) to the negacyclic ring sending x_d to \zeta y.
- $d$ (number of axes), bound on [Phase twist](phase-twist.md): The number of axes of the array f.
- $T$ (total entries), bound on [Phase twist](phase-twist.md): The number of entries of the array f in all.
- $M$ (number of records), bound on [Phase twist](phase-twist.md): The number of lines along the last axis, T/r.
- $\iota$ (record identification), bound on [Phase twist](phase-twist.md): Reads each line along the last axis as a polynomial in the negacyclic ring.
- $D_\pm$ (diagonal twist), bound on [Phase twist](phase-twist.md): Multiplies entry k of each line by \zeta^{\pm k}.
- $\mathcal M_r$ (ring convolution), bound on [Phase twist](phase-twist.md): The ring convolution that convolves the first d-1 axes over the negacyclic ring and includes the division by T.
- $\mathcal M_{\mathbb C}$ (normalized cyclic convolution), bound on [Phase twist](phase-twist.md): The composite D_-\iota^{-1}\mathcal M_r(\iota D_+ f,\iota D_+ g), equal to f*g/T.
- $q$ (sequence length), bound on [Discrete Fourier transform](dft.md): The number of complex entries in the sequences the transform acts on.
- $u$ (input sequence), bound on [Discrete Fourier transform](dft.md): A sequence of q complex numbers to which the transform is applied.
- $\omega$ (root of unity), bound on [Discrete Fourier transform](dft.md): The primitive q-th root of unity e^{2 pi i/q} whose powers are the transform weights.
- $t$ (transform length), bound on [Butterflies and the fast transform](butterfly.md): The number of values in the transform, a power of two.
- $z_k$ (input values), bound on [Butterflies and the fast transform](butterfly.md): The input value at position k, for 0 <= k < t.
- $k$ (input position), bound on [Butterflies and the fast transform](butterfly.md): The position of an input value, 0 <= k < t.
- $\omega_t$ (root of unity), bound on [Butterflies and the fast transform](butterfly.md): The primitive t-th root of unity e^{2 pi i/t}.
- $b$ (lowest output bit), bound on [Butterflies and the fast transform](butterfly.md): The lowest bit of the output index, 0 or 1.
- $h$ (remaining output index), bound on [Butterflies and the fast transform](butterfly.md): The output index with its lowest bit removed.
- $t$ (transform length), bound on [Synthetic polynomial transform](synthetic-transform.md): The number of ring elements along one axis of the transform, a power of two dividing 2r.
- $\omega_t$ (ring root of unity), bound on [Synthetic polynomial transform](synthetic-transform.md): The power y^{2r/t} of the ring variable, used as the root of unity of the length-t synthetic transform.
- $V$ (array volume), bound on [Elementary stream operations](stream-ops.md): The number of radix-q digits stored in the array.
- $q$ (radix), bound on [Elementary stream operations](stream-ops.md): The number of values one digit can take.
- $W$ (number of streams), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams into which whole rows are dealt cyclically.
- $d$ (number of axes), bound on [Bluestein chirp identity](chirp.md): The number of axes (coordinates) of an index.
- $t_i$ (axis length), bound on [Bluestein chirp identity](chirp.md): The even number of entries along axis i.
- $s_i$ (coprime integer), bound on [Bluestein chirp identity](chirp.md): An integer coprime to t_i, scaling the frequency read along axis i.
- $T$ (total entries), bound on [Bluestein chirp identity](chirp.md): The total number of entries, the product of the t_i.
- $Q$ (target permutation), bound on [Bluestein chirp identity](chirp.md): The target permutation, reading frequency (-s_i j_i)_i at output position j.
- $a$ (chirp), bound on [Bluestein chirp identity](chirp.md): The chirp, a quadratic-phase array exp(-pi i sum s_i j_i^2/t_i).

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Synthetic polynomial transform](synthetic-transform.md): A transform over the ring modulo y^r + 1 whose roots of unity are powers of y, so every twiddle multiplication is a signed shift of a coefficient list.
  Shown as: Retained frequency order *<predicate>* Synthetic polynomial transform

## Pages that build on this one

- Tape layout for synthetic transforms: Placing the selected bits of the participating axes at a common offset in K-bit chunks so each round of the synthetic transform is one simultaneous layer, costing less than log t passes.
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

- "Let $B_t$ denote this record permutation: it moves the entry at $j$ to $\operatorname{rev}_a(j)$." (paper)

  > After all $a$ rounds, the named slots from high to low therefore contain the frequency bits from low to high. If $\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$. Let $B_t$ denote this record permutation: it moves the entry at $j$ to $\operatorname{rev}_a(j)$. The recursion writes its outputs directly in this order; it does not move whole frequency indices.

- "retain the same frequency order through their pointwise product" (paper)

  > Next, Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections~\ref{sec:synthetic-layouts} and~\ref{sec:exact-ring-products} compute convolution on the remaining axes over this polynomial ring. The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order. Their polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "every power of $\omega_t$ is an isometry" (The page never says which norm on R_r is meant (the paper, line 2779-2784, uses the max of coefficient moduli, under which multiplication by y^a permutes coefficients and flips signs). Without it the reader cannot check that powers of omega_t are isometries, that averaging gives contractions, or that H_0 and J_E are a contraction and an isometry.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "After all $a$ rounds the named slots from high to low hold the frequency bits from low to high" (Slots and address bits are never introduced on this page, and the induction over rounds (paper lines 2846-2862) that shows each round writes the next-lowest frequency bit into the high slots is not given. The reader cannot check this claim, which the bit-reversal and B_t rest on.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "the two reverse operators agree" (Both reverse operators composed with B_tF_t^- give I/t, but that equates them only if B_tF_t^- is invertible. The paper (line 2880-2881) states this hypothesis ('The forward procedure is invertible, so these two reverse operators agree'). The page omits it and never says the forward procedure is invertible.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "$k_i$ the index encoded by its unprocessed slots" (The page does not say how k_i is read off from the address bits, nor that 0<=k_i<u_i/2, nor why the combined exponent is that sum. The formula for E is given without derivation and relies on the undefined slot encoding.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Say what $\mathcal R_r$ denotes where it is first used (for a size or count, what it counts): "over $\mathcal R_r$" (The page never names $\mathcal R_r$ as the ring modulo y^r+1 with complex coefficients; the notation is not bound by any listed page or concept.)
- Say what $i$ denotes where it is first used: the page uses it before saying so in "Here $u_i$ is axis $i$'s current length"
- Explain "no two-torsion" in a sentence where it is first used.

## Previous version (revise it)

It has 349 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 436 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Retained frequency order is the bit-reversed order in which the forward transform leaves its outputs, kept by the pointwise product and consumed by the opposite transform, so no reordering is executed.

It orders the outputs of the [synthetic polynomial transform](synthetic-transform.md) $F_t^-$ over $\mathcal R_r$, where $t$ is the transform length and $a=\log_2t$ the number of rounds. For $z\in\mathcal R_r^t$,

$$(F_t^-z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{-jk}z_k,\qquad (F_t^+z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{jk}z_k.$$

For $t$ a power of two dividing $2r$, define $\omega_t=y^{2r/t}$; every power of $\omega_t$ is an isometry, so each entry is an average of $t$ isometric images and both normalized transforms are contractions.

The ring has zero divisors, so one cannot divide by $\omega_t^j-1$; instead $\sum_{k=0}^{t-1}\omega_t^{jk}$ equals $t$ if $t\mid j$ and $0$ otherwise. Hence $F_t^+F_t^-=t^{-1}I$. For $t\nmid j$, write $j=2^vj_0$ with $j_0$ odd. Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies the sum $S$ by $y^{rj_0}=-1$. Hence the sum is zero, since the additive group of $\mathcal R_r$ has no two-torsion <cite data-source="paper">Hence the sum is zero, since the additive group of</cite>.

Decimation in frequency pairs $z_k$ with $z_{k+t/2}$. Writing the output index as $2h+b$, $b\in\{0,1\}$, and using $\omega_t^{t/2}=-1$,

$$(F_t^-z)_{2h+b}=\frac1{t/2}\sum_{k=0}^{t/2-1}(\omega_t^2)^{-hk}\,\omega_t^{-bk}\,\frac{z_k+(-1)^bz_{k+t/2}}2 .$$

With $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ the two-point butterfly, apply $H_0$ to each pair, multiply the $b=1$ output by $\omega_t^{-k}$, and recurse on the two length-$t/2$ branches.

After all $a$ rounds the named slots from high to low hold the frequency bits from low to high, so $(F_t^-z)_j$ is stored at slot $\operatorname{rev}_a(j)$, where $\operatorname{rev}_a$ reverses the $a$ binary digits. Let $B_t$ be the permutation moving the entry at $j$ to $\operatorname{rev}_a(j)$ <cite data-source="paper">Let $B_t$ denote this record permutation: it moves the entry at $j$ to $\operatorname{rev}_a(j)$.</cite> The pointwise product acts slotwise, keeping this order <cite data-source="paper">retain the same frequency order through their pointwise product</cite>.

The opposite procedure runs the levels backwards; since $H_0^2=I/2$, each reversed level is half the inverse of the forward level, over $a=\log_2t$ levels. The reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$, and as $F_t^+B_t^{-1}B_tF_t^-=F_t^+F_t^-=I/t$ by character cancellation, the two reverse operators agree. So the two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.

With several axes, a round applies $H_0$ on every axis at once, one parallel butterfly $\mathcal H$. Each axis's twiddle depends only on its own address bits, so twiddles commute with the other axes' butterflies and group into one recordwise monomial $J_E$ that multiplies the record by $y^E$, with

$$E=-\sum_i\frac{2r}{u_i}\,b_ik_i\pmod{2r}.$$

Here $u_i$ is axis $i$'s current length, $b_i$ its new branch bit and $k_i$ the index encoded by its unprocessed slots, so $E$ depends on the address, not on coefficient values. Each $\mathcal H$ is a contraction and each $J_E$ an isometry, so every completed round is a contraction.

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

Write the body to `exegenius/tasks/0092-write-frequency-order.answer.md` and the JSON to `exegenius/tasks/0092-write-frequency-order.answer.json`, then run `exegenius submit 0092-write-frequency-order` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0092-write-frequency-order`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
