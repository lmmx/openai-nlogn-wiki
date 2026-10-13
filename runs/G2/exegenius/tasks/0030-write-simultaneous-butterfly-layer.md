# exegenius task 0030-write-simultaneous-butterfly-layer

Project directory: `/home/user/openai-nlogn-wiki/runs/G2` (paths below are relative to it)

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

For these sources: Undergraduate computer science: algorithms and complexity through big-O analysis, recurrences and divide-and-conquer (Karatsuba, FFT-based polynomial multiplication, usually met at the level of the standard recursive FFT), discrete mathematics (modular arithmetic, primes and gcd, sets, functions and permutations, induction), and introductory linear algebra (matrices, rank, bases, inner products, Gaussian elimination, over the reals and probably F_2). Also the basics of complex numbers and Turing machines with multiple tapes. The reader has not studied abstract algebra such as quotient rings or tensor products, finite-field theory beyond F_2, numerical analysis of rounding errors, or the research literature on integer multiplication (Schönhage–Strassen, Fürer, Harvey–van der Hoeven), and has not seen Bluestein, Nussbaumer polynomial transforms or Gaussian resampling.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Bit XOR
- The n log n conjecture and prior bounds (also: Schönhage–Strassen conjecture)
- Arrays as tape streams and elementary scans
- Controlled shifts and rational scalings
- Fixed-point and Gaussian dyadic arithmetic
- Discrete Fourier transform
- Cyclic convolution
- Multiplication as convolution of radix digits
- Multidimensional transform
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Two-point butterfly layer (also: butterfly, H₀)
- Synthetic polynomial transform (also: Nussbaumer polynomial transform)
- The established O(N log N) multiplier
- Subspaces, bilinear forms and orthogonal complements
- Linear network with restored scratch wires (also: motif network, restoration schedule)
- Triple-subset intersection gadgets
- Frames on wire arrays
- Nested subspace labels and the rank deficit (also: s<Wm)
- Recursive power saving from the rank deficit
- Lower triangular factorization
- Matrix shear on address fields
- Fast interchange of address chunks
- Binary phase frames and the two-point kernel C
- Packed selected-bit addition
- Last-coordinate phase twist
- Gaussian resampling
- Error bounds and exact recovery
- Asymptotic notation beyond big-O (also: Omega notation, Theta notation, little-o, Ω, Θ, o(n log n))
- Logarithms and binary logarithm (also: lg, log base 2, log_2, ceiling of log)
- Floor and ceiling functions (also: floor, ceiling, ⌊x⌋, ⌈x⌉, integer part)
- Binary representation of integers (also: n-bit integer, bit string, binary expansion, two's complement, signed binary)
- Radix representation and digits (also: base-b expansion, positional notation, radix digits, leading zeroes)
- Schoolbook multiplication and carries (also: grade-school multiplication, long multiplication, quadratic multiplication, carry propagation, addition with carry)
- Divide-and-conquer and recurrences (also: recurrence relation, master theorem, Karatsuba multiplication, recursion, geometric series, geometric sum)
- Fast Fourier transform and FFT multiplication (also: FFT, Cooley-Tukey, radix-2 FFT, O(n log n) polynomial multiplication, evaluation and interpolation)
- Mathematical induction and proof by cases (also: induction, inductive proof, proof by contradiction)
- Sets, subsets and Cartesian products (also: set intersection, cardinality, subset of size three, product set, tuples, indicator vector)
- Functions, bijections and permutations (also: permutation, bijection, inverse function, composition, involution, partial permutation)
- Modular arithmetic and congruences (also: mod, residues, congruence, ℤ/nℤ, integers modulo n, remainder, units modulo n)
- Primes, divisibility and coprimality (also: gcd, greatest common divisor, relatively prime, prime power, coprime, trial division, prime factorization)
- Rational numbers and exact fractions (also: rationals, ℚ, denominator, numerator, dyadic rational)
- Finite fields and the field F_2 (also: GF(2), 𝔽_2, binary field, arithmetic modulo 2, parity)
- Vectors, matrices and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, identity matrix, linear transformation, diagonal matrix, linear combination)
- Rank, basis and dimension (also: linear independence, span, vector space, subspace dimension, rank of a matrix, rank-nullity)
- Gaussian elimination (also: row reduction, row operations, elementary matrices, triangular matrix, lower triangular, upper triangular)
- Inner product, norm and orthonormal basis (also: dot product, orthogonal vectors, orthonormal, unit vector, vector norm, max norm, sup norm, l-infinity norm, unit disk, absolute value of complex number, modulus)
- Roots of unity and Euler's formula (also: e^{iθ}, primitive root of unity, n-th roots of unity, unit circle, geometric series of roots)
- Summation and product notation (also: sigma notation, Σ, Π, indices, Kronecker delta)
- Newton's method (also: Newton iteration, Newton-Raphson, reciprocal by Newton, square root by Newton, quadratic convergence)
- Integer division with remainder (also: quotient and remainder, floor division, integer square root, division algorithm)
- Lexicographic order (also: dictionary order, row-major order, most significant first, mixed radix address)
- Arrays, records and matrix transposition (also: row-major, column-major, transpose, matrix layout, indexing)
- Turing machine running time and model conventions (also: worst-case time, time complexity, unit-cost RAM, random access machine, input and output tapes, finite alphabet, tape heads, scanning and sorting on tapes, linear-time scan, simulation)

## This page

Concept: Simultaneous butterfly layer
Gloss: One H₀ butterfly at the same bit offset in up to d address chunks applied to all polynomial records at cost O(V d^{λ'}) for fixed λ'<1, evaluated exactly in dyadics with one final truncation.

## This page in the argument

The step: The map $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied at one common bit offset in each of $D\le d$ equal-width $K$-bit address chunks of an array of records, each a polynomial with $r$ complex coefficients on the grid $2^{-p}\mathbb Z[i]$, of total volume $V$, with a single final truncation, costs $O(V d^{\lambda'})$ for a fixed $\lambda'<1$.
How: Rewrite $H_0^{\otimes D}$ as phase-diagonal conjugates of $C^{\otimes D}$, compute $C^{\otimes e}$ on $e=mf$ selected bits with the complex network (each of the $s<W m$ calls acts on $f$ bits, and the binary changes of basis are packed selected-bit additions), unroll the resulting recurrence, and bound the exact intermediate dyadics so that one truncation suffices.
Why: The phase frames express a tensor power of the kernel $C$ through smaller groups of selected bits, separated by binary changes of basis, and the whole layer can then be evaluated exactly before one truncation. (the sources say so: "frames express a $C$ tensor product using smaller groups of" (paper))
Striking feature: The exponent $\lambda'$ is below 1, so applying the butterfly on $d$ chunks at once beats the $D$ whole-array passes that separate butterfly factors would need. (explain why it holds, from the method)

Its sub-steps, in order:

- An invertible binary change of basis of fixed order $m$ is a product of at most $m(m-1)+3m$ row additions, each adding the selected bits $x_{h,j}\leftarrow x_{h,j}\oplus x_{h',j}$ of two slots of $f$ chunks.
- Applying the network with these column frames to a group of $e=mf$ selected axes gives exactly $s$ child calls on the $f$ axes of one slot and yields $C^{\otimes e}$ on every role, each inverse child coming from one forward call.
- Since $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$ with the diagonal phase operator $\mathcal S_D$, a layer of $H_0$ follows from a layer of $C$ exactly in Gaussian dyadics.
- Under the stated growth of the parameters, the selected-bit additions $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ at positions $j_i=\rho+i K$, $0\le i<f$, of two chunks of $L=f K$ bits can be performed, with a third chunk lent as temporary and restored, in time $O(V(L^\tau+1))$. (on [Packed selected-bit addition](packed-selected-bit-addition.md))
- One $C$ kernel on one selected bit costs $O(V)$ by splitting on that bit and scanning aligned record pairs, so $e$ kernels cost $O(V e)$.
- At an internal node of $e=m^k$ active chunks, the $s$ recursive calls act on slots of $e/m$ chunks and the binary changes of basis, scalar gates and reassembly cost $O(V((e K)^\tau+1))$ at the node.
- The first chunks supply a row index $u=Wg+w$; sending row $u$ to role $w$ gives each child exactly $1/W$ of the parent's volume while every row keeps its full polynomial suffix of $r$ coefficients.
- The recurrence $F(e)\le(s/W)F(e/m)+O((e K)^\tau+1)$ for the cost per unit volume unrolls to $O(d^{\lambda'})$ for a fixed $\lambda'<1$, because $s/W<m$ strictly.
- The number of extra guard bits needed to keep every intermediate coefficient of one layer exact grows only like a fixed power of $d$, which is $o(p)$ for $d$ a small enough power of $p$, so coefficients keep width $O(p)$.
- Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays and the final truncation $Q_p$ changes each coefficient by less than $\sqrt2\,2^{-p}$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a convolution over a polynomial ring computed by Fourier-type transforms; supply the two fast tape procedures that remove the logarithmic factor from address movement and from butterfly arithmetic, both obtained from linear networks that save a power; then assemble the algorithm and tally every cost. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.1, S3.2, S3.3, S3.5, S3.6, S3.7, S3.8, S3.9, S3.10). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.1**: An invertible binary change of basis of fixed order $m$ is a product of at most $m(m-1)+3m$ row additions, each adding the selected bits $x_{h,j}\leftarrow x_{h,j}\oplus x_{h',j}$ of two slots of $f$ chunks.
Source: "Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$" (paper)
> Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$ as a product of at most $m(m-1)+3m$ elementary row additions: one clears at most $m-1$ other entries per pivot, and each row swap is three row additions. Reversing the elimination gives the required product since each row addition is an involution. The number is a constant because $m$ is fixed. Adding row $h'$ to row $h$ in every column applies $x_{h,j}\leftarrow x_{h,j}\mathbin\oplus x_{h',j}$ for every $0\le j<f$. Thus one row addition changes corresponding selected positions in two whole slots. The packed address operation proved below performs all of these XORs together.

**S3.2**: Applying the network with these column frames to a group of $e=mf$ selected axes gives exactly $s$ child calls on the $f$ axes of one slot and yields $C^{\otimes e}$ on every role, each inverse child coming from one forward call.
Source: "Apply the finite network with these column frames to a group of" (paper)
> \paragraph{The exact recursive contract.} Apply the finite network with these column frames to a group of $e=mf$ selected axes. Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot. The source and sink $Z_{a,f}$ signs, together with the scalar $i^{27f}$ at each affected sink, turn every endpoint kernel into a forward one. Negating the prescribed physical bank and undoing its exchange returns each result to its original role. Proposition~\ref{prop:complex-motif-interface} therefore gives $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary. Formula~\eqref{eq:phase-inverse-child} supplies each inverse child from one forward call, and none of the corrections adds a child. The remaining operations are a fixed number of binary row additions and coefficientwise scalar operations.

**S3.3**: Since $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$ with the diagonal phase operator $\mathcal S_D$, a layer of $H_0$ follows from a layer of $C$ exactly in Gaussian dyadics.
Source: "For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its" (paper)
> \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.

**S3.5**: One $C$ kernel on one selected bit costs $O(V)$ by splitting on that bit and scanning aligned record pairs, so $e$ kernels cost $O(V e)$.
Source: "To apply one \(C\) kernel, use the split from" (paper)
> To apply one \(C\) kernel, use the split from Lemma~\ref{lem:elementary-streams} at the selected address bit. Call the two streams \(0\) and \(1\) according to that bit. Because that bit has its complete two-element range, the two streams have the same remaining address set in the same order. Their aligned record addresses therefore differ only in the selected bit, and their coefficients are still ordered by the same polynomial index. Scan each pair of records in that order. For corresponding complex coefficients \(u\) from stream \(0\) and \(v\) from stream \(1\), compute \begin{equation}\label{eq:individual-C-pair} C(u,v)= \left(\frac{u+v+i(u-v)}2,\, \frac{u+v-i(u-v)}2\right). \end{equation} Addition, subtraction and halving use the fixed-point con

**S3.6**: At an internal node of $e=m^k$ active chunks, the $s$ recursive calls act on slots of $e/m$ chunks and the binary changes of basis, scalar gates and reassembly cost $O(V((e K)^\tau+1))$ at the node.
Source: "First consider an internal node containing \(e=m^k\) consecutive" (paper)
> First consider an internal node containing \(e=m^k\) consecutive active chunks, with \(k\ge1\). Split it into \(m\) consecutive slots, each containing \(e/m\) chunks. The phase construction supplies one recursive call on a slot for each vector in an edge residual basis, hence exactly \(s\) calls in one invocation of the network. If the logical volume entering this node is \(V\), binary changes of basis, their inverses, scalar gates, endpoint corrections and reassembly of the physical banks cost \[ O\bigl(V((eK)^\tau+1)\bigr) \] at this node. Each slot has \((e/m)K\) address bits, so Lemma~\ref{lem:packed-selected-bit-rectangle} gives the stated bound for a row addition. The network and all of its \(m\)-dimensional residual bases are fixed, so the total number of row additions is fixed as well. At the same guarded width, the scalar gates cost a constant number of scans of the current volume. Address and descriptor work bounded by any fixed polynomial in \(p\) per record is also absorbed: its ratio to the record's \(\Theta(rp)\) bits tends to zero.

**S3.7**: The first chunks supply a row index $u=Wg+w$; sending row $u$ to role $w$ gives each child exactly $1/W$ of the parent's volume while every row keeps its full polynomial suffix of $r$ coefficients.
Source: "At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\)," (paper)
> At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\), and send that entire row to physical wire role \(w\), indexed there by \(g\). Every role stream has the same remaining address shape. Thus a pointwise gate reads the records with the same \(g\) and the same remaining address in its touched roles. The scalar network allows these role values to be arbitrary, so the split supplies its scratch roles from existing rows. Each recursive edge call acts on one role stream with volume exactly \(1/W\) of its parent's logical volume.

**S3.8**: The recurrence $F(e)\le(s/W)F(e/m)+O((e K)^\tau+1)$ for the cost per unit volume unrolls to $O(d^{\lambda'})$ for a fixed $\lambda'<1$, because $s/W<m$ strictly.
Source: "Indeed, the \(s\) child calls are executed on streams of volume" (paper)
> \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).

**S3.9**: The number of extra guard bits needed to keep every intermediate coefficient of one layer exact grows only like a fixed power of $d$, which is $o(p)$ for $d$ a small enough power of $p$, so coefficients keep width $O(p)$.
Source: "For the complex network, let" (paper)
> For the complex network, let \[ E=64(W+m+1)^3,\qquad B=s+E, \qquad \nu=\min\{j\ge1:m^j\ge B\}, \] and set \[ C_1=\max\{20,\nu+3\},\qquad C_0=128mB^2, \qquad \Delta=\lceil C_0d^{C_1}\rceil. \] For the stated \(h=100\) construction, the complex network has \[ \begin{split} m&=1{,}000{,}000,\\ W&=1{,}873{,}807{,}244{,}643{,}542{,}670{,}000,\\ s&=1{,}873{,}807{,}244{,}636{,}671{,}267{,}308{,}000{,}000. \end{split} \] These values give \(m^{10}<B<m^{11}\), hence \(\nu=11\) and \(C_1=20\). In fact the bound below needs only exponent fourteen; the choice twenty leaves an explicit additional margin.

**S3.10**: Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays and the final truncation $Q_p$ changes each coefficient by less than $\sqrt2\,2^{-p}$.
Source: "Finally, every row of $\mathcal H$ has" (paper)
> The guard-width calculation above bounds both denominator and magnitude growth by $\lceil C_0d^{C_1}\rceil$. Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, this is $o(p)$ uniformly over the allowed $d$, so every intermediate coefficient is represented exactly with the stated $O(p)$ width. The initial scan removes or adds only redundant leading sign bits and appends the reserved fractional zeros to put each supplied component in this guarded format. To truncate toward zero at the end, shift its absolute numerator right by the number of added fractional bits, restore its sign, and write the result in $w$ bits. These scans cost $O(V)$. Finally, every row of $\mathcal H$ has absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk arrays, and componentwise truncation preserves that disk and has error less than $\sqrt2\,2^{-p}$: truncation cannot increase the absolute value of either component, and changes each by less than $2^{-p}$. The truncated numerators have magnitude at most $2^p$, so the supplied component width can hold them. \end{proof} \section{Synthetic transforms and their tape layout} \label{sec:synthetic-layouts}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S3.4 (on [Packed selected-bit addition](packed-selected-bit-addition.md)): Under the stated growth of the parameters, the selected-bit additions $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ at positions $j_i=\rho+i K$, $0\le i<f$, of two chunks of $L=f K$ bits can be performed, with a third chunk lent as temporary and restored, in time $O(V(L^\tau+1))$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Nested subspace labels and the rank deficit](rank-deficit-labels.md)
- [Two-point butterfly layer](two-point-butterfly.md)
- [Arrays as tape streams and elementary scans](tape-streams.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Binary phase frames and the two-point kernel C](phase-frames.md): Frames C_U=H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} over Gaussian dyadics, whose edge changes are products of translation kernels aI+bX, composing to C^{⊗m} on every role.
  Shown as: Simultaneous butterfly layer *<predicate>* Binary phase frames and the two-point kernel C
- [Packed selected-bit addition](packed-selected-bit-addition.md): Adding corresponding selected bits of two address chunks using a third temporary chunk, via cyclic whole-chunk shifts plus a deterministic correction of an explicit small set of exceptional addresses.
  Shown as: Simultaneous butterfly layer *<predicate>* Packed selected-bit addition
- [Recursive power saving from the rank deficit](recursive-power-saving.md): A call at parameter m·f uses s calls at parameter f on streams of volume V/W, so cost per volume grows like m^τ rather than m, with τ<1 because s/W<m.
  Shown as: Simultaneous butterfly layer *<predicate>* Recursive power saving from the rank deficit
- [Synthetic polynomial transform](synthetic-transform.md): A Fourier transform over the ring ℂ[y]/(y^r+1) using ω_t = y^{2r/t} as root of unity, so multiplications by roots are exact signed shifts and only butterflies remain.
  Shown as: Simultaneous butterfly layer *<predicate>* Synthetic polynomial transform
- [Fixed-point and Gaussian dyadic arithmetic](fixed-point-dyadics.md): Complex numbers stored as signed two's-complement grid numerators over 2^p, added and scaled exactly with guard bits and truncated once toward zero.
  Shown as: Simultaneous butterfly layer *<predicate>* Fixed-point and Gaussian dyadic arithmetic

## Pages that build on this one

- Synthetic transform tape layout: A tape layout placing the selected bits of the participating axes at a common offset in consecutive K-bit chunks so that parallel layers apply, with the frequency order retained.
- Parameter choice and cost table: Fixed rational exponents (τ=σ=1−2^{−50}, ε=2^{−75}, κ=2^{−182}, …) and sizes p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log₂T/d⌉} making every cost term a power of p below one.

## Other pages you may link to

- [The n log n conjecture and prior bounds](nlogn-conjecture.md)
- [Linear network with restored scratch wires](linear-network.md)
- [Frames on wire arrays](frames.md)
- [Arrays as tape streams and elementary scans](tape-streams.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Subspaces, bilinear forms and orthogonal complements](linear-algebra-orthogonality.md)
- [Triple-subset intersection gadgets](triple-subset-gadgets.md)
- [Nested subspace labels and the rank deficit](rank-deficit-labels.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Matrix shear on address fields](matrix-shear.md)
- [Fast interchange of address chunks](fast-chunk-interchange.md)
- [Polynomial ring modulo y^r + 1](ring-mod-y-r-plus-1.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly layer](two-point-butterfly.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Multiplication as convolution of radix digits](multiplication-as-convolution.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Error bounds and exact recovery](error-and-exact-recovery.md)
- [Last-coordinate phase twist](phase-twist.md)
- [The established O(N log N) multiplier](nlogn-multiplier.md)
- [Synthetic transform tape layout](synthetic-transform-layout.md)
- [Signed packing for ring products](kronecker-packing.md)
- [Normalized convolution over the ring](synthetic-convolution.md)
- [Resampling with permutations left in the transform](resampling-without-sorting.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Parameter choice and cost table](parameter-choice.md)
- [Chinese-remainder address map](crt-address-map.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "We will obtain cost $O(Vd^{\lambda'})$, with" (paper)

  > The parameters will satisfy \[ d=\Theta(p^\epsilon),\qquad K=\lfloor d^c\rfloor, \qquad r=2^{\Theta(p/d)},\qquad c>0,\quad 0<\epsilon<1. \] The exponents and comparison constants are fixed, and we impose their further restrictions in Proposition~\ref{prop:simultaneous-layer}. Two consequences explain the layout. The polynomial length $r$ grows faster than every fixed power of $p$, so a scan of a record pays for polynomial work on its address. Also $K/\log p\to\infty$, which will make the exceptional set in a packed change of address bits small enough to repair by sorting. We will obtain cost $O(Vd^{\lambda'})$, with $\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly factors would require $D$ whole-array passes.

- "Simultaneous normalized butterfly layer" (paper)

  > \begin{proposition}[Simultaneous normalized butterfly layer] \label{prop:simultaneous-layer} Fix \[ \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad C_1=20. \] Let $c,\epsilon,\lambda,\lambda'$ be fixed positive rational numbers satisfying \[ \max\{\tau,\sigma\}<\lambda<1,\qquad \tau(1+c/\beta)<\lambda,\qquad \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1, \qquad \epsilon C_1<1. \] Fix positive constants $a_d\le b_d$ and $a_r\le b_r$, and fix positive constants $C_M,C_{\rm desc},C_w$ with $C_w>1$. For these fixed choices there are a cutoff $p_0$, one fixed finite-alphabet multitape procedure, and an implicit time constant with the following guarantee. The cutoff and time constant may depend on the fixed rational parameters and these constants. For every choice of positi


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

Write the body to `exegenius/tasks/0030-write-simultaneous-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0030-write-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0030-write-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0030-write-simultaneous-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
