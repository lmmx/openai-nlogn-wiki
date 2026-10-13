# exegenius task 0029-write-simultaneous-butterfly-layer

Project directory: `/home/user/openai-nlogn-wiki/runs/G4` (paths below are relative to it)

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

For these sources: The reader has done an undergraduate computer science degree: discrete mathematics (modular arithmetic, primes and gcd, sets, induction, recurrences and asymptotics), basic linear algebra over the reals and complex numbers (matrices, inverses, norms), polynomials and complex roots of unity, and algorithms including divide and conquer and Karatsuba multiplication. On the machine side they know basic single- and multi-tape Turing machines and the idea of counting steps. They have not studied the Fourier transform, FFT-based multiplication, Schonhage-Strassen, Harvey-van der Hoeven, numerical error analysis, abstract algebra beyond rings of residues, finite-field linear algebra, or any lower-bound or advanced tape-algorithm technique, so those must be explained.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape Turing machine model
- Elementary stream operations on tape arrays
- Controlled shifts and rational scalings
- Convolution
- Discrete Fourier transform
- Radix-2 butterflies and FFT
- Subspaces, rank and orthogonal complements
- Fixed-point disk arithmetic and truncation error
- Established O(n log n) integer multiplier
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The polynomial variable, which satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Signed packing of polynomial products
- Two-point kernel C and phase frames
- Frames on pointwise linear networks
- Subset-intersection exchange network
- Subspace labels and the rank budget
- Recursive power saving from a rank deficit
- Bit network shear interface
- Lower triangular (Bruhat-type) factorization
- Cost of a rational matrix shear
- Power-width address interchange
- Fast chunk interchange
- Complex phase network
- Packed selected-bit addition
- Bluestein chirp identity
- Modular arithmetic and residue rings (also: congruence, Z/qZ, integers mod q, residue classes, modular inverse)
- Primes, coprimality and the Euclidean algorithm (also: gcd, greatest common divisor, relatively prime, extended Euclidean algorithm, coprime)
- Positional (radix) number representation (also: base-b expansion, binary representation, digits, binary integers, mixed radix)
- Signed binary numbers and rounding (also: two's complement, sign-magnitude, floor, ceiling, rounding to nearest integer, truncation toward zero)
- Dyadic rationals (also: binary fractions, fractions with power-of-two denominator, fixed-point binary fractions)
- Bitwise operations and Hamming weight (also: XOR, exclusive or, bit string, popcount, Hamming weight, parity)
- Permutations and bijections (also: permutation of indices, bijection, inverse permutation, bit-reversal permutation, transposition)
- Lexicographic order and multi-index addressing (also: row-major order, dictionary order, multidimensional array indexing, mixed-radix address, tuple indices)
- Matrix algebra (also: matrix multiplication, matrix inverse, identity matrix, transpose, invertible matrix, 2x2 matrices, diagonal matrix, matrix-vector product)
- Vector norms and the triangle inequality (also: sup norm, max norm, infinity norm, absolute value bound, modulus bound, triangle inequality)
- Logarithms, exponentials and floor/ceiling in analysis (also: log base 2, lg, powers of two, exponent laws, iterated logarithm, real exponent)
- Theta, Omega and little-o notation (also: big-Theta, big-Omega, little-o, liminf, asymptotic lower bound, tight bound)
- Summations and geometric series (also: geometric sum, telescoping sum, sum of powers, series bound)
- Recurrence relations and divide and conquer (also: recurrence, unrolling a recurrence, master theorem, recursion tree, recursive algorithm, divide-and-conquer)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba, quadratic multiplication)
- Stacks and call stacks (also: stack, recursion stack, call stack, program counter, subroutine call)
- Pointwise operations on lists and vectors (also: componentwise product, Hadamard product, elementwise map, coordinatewise operation)
- Sets, subsets and counting (also: subset, cardinality, intersection, binomial coefficient, ground set, indicator vector, power set)
- Mathematical induction and proof by contradiction (also: induction, inductive proof, contradiction, proof techniques)
- Euler's formula and complex exponentials (also: e^{i theta}, Euler formula, unit circle, phase factor, twiddle factor, modulus of e^{i theta})

## This page

Concept: Simultaneous butterfly layer
Gloss: Applying H_0 to the same bit position in up to d address chunks at once, exactly in dyadic arithmetic and truncating once, in O(V d^λ') time for λ' < 1.

## This page in the argument

The step: Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ to the same bit position of up to $d$ address chunks of $K$ bits at once, exactly in dyadic arithmetic with a single final truncation, takes $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$.
How: Write the layer as a phase-conjugated tensor power of the two-point kernel $C$, realize $C^{\otimes e}$ with the complex phase network recursively, with each child on $e/m$ axes and volume $V/W$, implement the binary basis changes by packed selected-bit addition, and bound coefficient growth with guard bits.
Why: Separate butterfly factors would require $D$ whole-array passes; the network replaces them by $s_{\rm c}$ calls on streams a factor $W_{\rm c}$ smaller, and $s_{\rm c}<W_{\rm c}m$ again gives a power saving. (the sources say so: "factors would require $D$ whole-array passes." (paper))
Striking feature: The layer on $d$ chunks costs $d^{\lambda'}$ per bit with $\lambda'<1$, although applying one butterfly per chunk would cost $d$ passes; the saving again rests on $s_{\rm c}<W_{\rm c}m$. (explain why it holds, from the method)

Its sub-steps, in order:

- An edge's frame change is $\mathcal P_M\bigl(\prod_j C_{e_j}^{\epsilon_j}\bigr)\mathcal P_M^{-1}$; apply $\mathcal P_M^{-1}$ to each column, one $C^{\otimes f}$ child per residual basis vector in slot $h$, then $\mathcal P_M$.
- A group of $e=mf$ selected axes needs exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and returns $C^{\otimes e}$ on every role.
- The normalized layer is recovered exactly from the $C$-layer by $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$.
- Adding corresponding selected bits of two address chunks $x,y$ (a binary row addition $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$), while restoring a third chunk $z$, costs $O(V(L^\tau+1))$ by a constant number of cyclic shifts of whole chunk ranges plus a deterministic repair of a small exceptional address set. (on [Packed selected-bit addition](packed-selected-bit-addition.md))
- A row addition between slots $h'$ and $h$ uses a third slot as scratch; the complete binary change of basis and its inverse cost $O(V((eK)^\tau+1))$.
- Rows are taken from the first $q_0$ chunks and padded; a row index $u=Wg+w$ sends the whole row to role $w$, so each child has volume exactly $V/W$.
- The recurrence $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ unrolls to $O(d^{\lambda'})$ for a fixed $\lambda'<1$.
- Explicit guard widths bound denominator and magnitude growth within one layer by $\lceil C_0d^{C_1}\rceil=o(p)$ bits, so all intermediate values are exact.
- Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps the disk to itself and the single truncation has error below $\sqrt2\,2^{-p}$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in that model.; how: Reduce the product to a cyclic convolution of radix digits evaluated by Fourier-type transforms, make the two costly ingredients of those transforms (address rearrangement and butterfly arithmetic) cost a power of the logarithm less than a full scan per level by two rank-saving tape procedures, then assemble the algorithm, prove exactness and total the cost. (on [Sub-n log n integer multiplication](sub-nlogn-multiplication.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.1, S3.2, S3.3, S3.5, S3.6, S3.7, S3.8, S3.9). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.1**: An edge's frame change is $\mathcal P_M\bigl(\prod_j C_{e_j}^{\epsilon_j}\bigr)\mathcal P_M^{-1}$; apply $\mathcal P_M^{-1}$ to each column, one $C^{\otimes f}$ child per residual basis vector in slot $h$, then $\mathcal P_M$.
Source: "To implement \eqref{eq:phase-edge-coordinate} on the group, first apply" (paper)
> To implement \eqref{eq:phase-edge-coordinate} on the group, first apply $\mathcal P_M^{-1}$ separately to each column. For each $1\le h\le\rho_{\rm edge}$, apply $(C^{\epsilon_h})^{\otimes f}$ to the $f$ bits $x_{h,0},\ldots,x_{h,f-1}$. This is one child operation on the $f$ axes in slot $h$. Finally apply $\mathcal P_M$ to every column. A negative directional kernel still requires only one forward child, because \begin{equation}\label{eq:phase-inverse-child} (C^{-1})^{\otimes f} =(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}. \end{equation} The rightmost phase is applied first. All inverse wrappers are address signs and constant fourth-root phases, so they add no recursive calls.

**S3.2**: A group of $e=mf$ selected axes needs exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and returns $C^{\otimes e}$ on every role.
Source: "Summing its residual dimensions gives exactly" (paper)
> \paragraph{The exact recursive contract.} Apply the finite network with these column frames to a group of $e=mf$ selected axes. Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot. The source and sink $Z_{a,f}$ signs, together with the scalar $i^{27f}$ at each affected sink, turn every endpoint kernel into a forward one. Negating the prescribed physical bank and undoing its exchange returns each result to its original role. Proposition~\ref{prop:complex-motif-interface} therefore gives $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary. Formula~\eqref{eq:phase-inverse-child} supplies each inverse child from one forward call, and none of the corrections adds a child. The remaining operations are a fixed number of binary row additions and coefficientwise scalar operations.

**S3.3**: The normalized layer is recovered exactly from the $C$-layer by $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$.
Source: "on all selected coordinates gives" (paper)
> \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.

**S3.5**: A row addition between slots $h'$ and $h$ uses a third slot as scratch; the complete binary change of basis and its inverse cost $O(V((eK)^\tau+1))$.
Source: "To add row $h'$ to row $h$, use slot $h'$ as $x$," (paper)
> \paragraph{Application to a fixed binary change of basis.} An invertible matrix over $\mathbb F_2$ of fixed order $m\ge3$ is a product of a fixed number of elementary row additions; a row exchange is three such additions. In one invocation of the finite network on $e=mf$ axes, slot $h$ consists of $f$ consecutive $K$-bit axis chunks. It therefore has address-bit width $L=fK$, and its selected bits $x_{h,j}$ occupy positions $\rho+jK$ for $0\le j<f$. To add row $h'$ to row $h$, use slot $h'$ as $x$, slot $h$ as $y$, and any third, distinct slot as $z$ in Lemma~\ref{lem:packed-selected-bit-rectangle}. The lemma performs $x_{h,j}\leftarrow x_{h,j}\mathbin\oplus x_{h',j}$ for every $j$ in one operation and restores the third slot, whatever its initial address value.

**S3.6**: Rows are taken from the first $q_0$ chunks and padded; a row index $u=Wg+w$ sends the whole row to role $w$, so each child has volume exactly $V/W$.
Source: "At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\)," (paper)
> At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\), and send that entire row to physical wire role \(w\), indexed there by \(g\). Every role stream has the same remaining address shape. Thus a pointwise gate reads the records with the same \(g\) and the same remaining address in its touched roles. The scalar network allows these role values to be arbitrary, so the split supplies its scratch roles from existing rows. Each recursive edge call acts on one role stream with volume exactly \(1/W\) of its parent's logical volume.

**S3.7**: The recurrence $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ unrolls to $O(d^{\lambda'})$ for a fixed $\lambda'<1$.
Source: "Indeed, the \(s\) child calls are executed on streams of volume" (paper)
> \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).

**S3.8**: Explicit guard widths bound denominator and magnitude growth within one layer by $\lceil C_0d^{C_1}\rceil=o(p)$ bits, so all intermediate values are exact.
Source: "The accelerated network is evaluated exactly until an entire" (paper)
> The accelerated network is evaluated exactly until an entire normalized butterfly layer is complete. Its intermediate operators need not be contractions. We now give explicit constants that bound denominator and magnitude growth within one layer.

**S3.9**: Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps the disk to itself and the single truncation has error below $\sqrt2\,2^{-p}$.
Source: "absolute row sum one." (paper)
> The guard-width calculation above bounds both denominator and magnitude growth by $\lceil C_0d^{C_1}\rceil$. Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, this is $o(p)$ uniformly over the allowed $d$, so every intermediate coefficient is represented exactly with the stated $O(p)$ width. The initial scan removes or adds only redundant leading sign bits and appends the reserved fractional zeros to put each supplied component in this guarded format. To truncate toward zero at the end, shift its absolute numerator right by the number of added fractional bits, restore its sign, and write the result in $w$ bits. These scans cost $O(V)$. Finally, every row of $\mathcal H$ has absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk arrays, and componentwise truncation preserves that disk and has error less than $\sqrt2\,2^{-p}$: truncation cannot increase the absolute value of either component, and changes each by less than $2^{-p}$. The truncated numerators have magnitude at most $2^p$, so the supplied component width can hold them. \end{proof} \section{Synthetic transforms and their tape layout} \label{sec:synthetic-layouts}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S3.4 (on [Packed selected-bit addition](packed-selected-bit-addition.md)): Adding corresponding selected bits of two address chunks $x,y$ (a binary row addition $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$), while restoring a third chunk $z$, costs $O(V(L^\tau+1))$ by a constant number of cyclic shifts of whole chunk ranges plus a deterministic repair of a small exceptional address set.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Complex phase network](complex-phase-network.md): The complex-scalar version of the exchange network with binary labels whose phase frames i^{wt(Px)} reduce to translation kernels aI + bX_v, giving C^{⊗m} on every role with s_c < W_c m.
  Shown as: Simultaneous butterfly layer *<predicate>* Complex phase network
- [Packed selected-bit addition](packed-selected-bit-addition.md): Adding corresponding selected bits of two address chunks (a binary row addition) by a constant number of cyclic shifts of whole chunk ranges plus a deterministic repair of a small exceptional address set.
  Shown as: Simultaneous butterfly layer *<predicate>* Packed selected-bit addition
- [Recursive power saving from a rank deficit](recursive-power-saving.md): If a call at parameter mf is made from s calls at parameter f on streams of volume V/W with s < Wm, the normalized cost grows like m^τ per level with τ < 1.
  Shown as: Simultaneous butterfly layer *<predicate>* Recursive power saving from a rank deficit
- [Fixed-point disk arithmetic and truncation error](fixed-point-precision.md): Storing complex numbers of modulus at most 1 as signed binary numerators over 2^p, truncating toward zero, and tracking how contractions and bilinear maps propagate the errors.
  Shown as: Simultaneous butterfly layer *<predicate>* Fixed-point disk arithmetic and truncation error
- [Fast chunk interchange](chunk-interchange.md): Exchanging two equal-width address fields of u bits in an arbitrary array in O(V u^τ) time for a fixed τ < 1, even though intermediate steps XOR data together.
  Shown as: Simultaneous butterfly layer *<predicate>* Fast chunk interchange
- [Radix-2 butterflies and FFT](fft-butterfly.md): Computing a power-of-two transform by repeated two-point butterflies (u,v) ↦ ((u+v)/2,(u−v)/2) followed by twiddle multiplications and smaller transforms (decimation in frequency).
  Shown as: Simultaneous butterfly layer *<predicate>* Radix-2 butterflies and FFT

## Pages that build on this one

- Synthetic transform layout and cost: Placing the selected bits of all axes at a common offset in K-bit chunks so each transform round is a simultaneous layer, with the output frequency order retained for reuse.
- Complete time bound: Summing the normalized costs of layouts, butterfly rounds, resampling, chirps and packed products, each at most p^{1−2κ}, to get O(n (log n)^{1−κ}).

## Other pages you may link to

- [Convolution](convolution.md)
- [Fixed-tape Turing machine model](fixed-tape-model.md)
- [Established O(n log n) integer multiplier](nlogn-multiplier.md)
- [Elementary stream operations on tape arrays](elementary-stream-ops.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Subspaces, rank and orthogonal complements](linear-subspaces.md)
- [Frames on pointwise linear networks](frames-on-arrays.md)
- [Subset-intersection exchange network](exchange-network.md)
- [Subspace labels and the rank budget](subspace-labels.md)
- [Bit network shear interface](bit-network-interface.md)
- [Lower triangular (Bruhat-type) factorization](triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Power-width address interchange](power-width-interchange.md)
- [Polynomial ring modulo y^r + 1](synthetic-ring.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Discrete Fourier transform](dft.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Two-point kernel C and phase frames](phase-kernel-c.md)
- [Synthetic transform layout and cost](synthetic-transform-layout.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Source permutation cancellation](permutation-cancellation.md)
- [Multidimensional resampling on a padded box](tensor-resampling.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Exact recovery of the integer product](exact-recovery.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Parameter choices](parameter-choices.md)
- [Coefficient twist to the negacyclic ring](convolution-twist.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound](cost-accounting.md)
- [Sub-n log n integer multiplication](sub-nlogn-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "The procedure returns $Q_p(\mathcal H z)$ in the same array," (paper)

  > The procedure returns $Q_p(\mathcal H z)$ in the same array, coefficient order, and component format in $O(Vd^{\lambda'})$ time, uniformly over all these choices of $p,d,r,D,P,S,\rho,w$ and $z$. Every returned coefficient belongs to the complex unit disk, and, in the maximum coefficient norm, \[ \|Q_p(\mathcal H z)-\mathcal H z\|_\infty <\sqrt2\,2^{-p}. \] The procedure evaluates the entire layer exactly before this final truncation. Put \[ C_0=128m\bigl(s_{\rm c}+64(W_{\rm c}+m+1)^3\bigr)^2, \] where $m,W_{\rm c},s_{\rm c}$ are the fixed constants of Proposition~\ref{prop:complex-motif-interface}. The procedure uses at most $p+\lceil C_0d^{C_1}\rceil$ fractional bits and $\lceil C_0d^{C_1}\rceil+3$ integer and sign bits per real component internally; these widths are $O(p)$. The time includes address changes, deterministic repair, row padding and its removal, and fixed-tape workspace cleanup. Its tape count is fixed, and its time constant is independent of the allowed array lengths and coefficient values. \end{proposition}

- "whereas separate butterfly
factors would require $D$ whole-array passes." (paper)

  > The parameters will satisfy \[ d=\Theta(p^\epsilon),\qquad K=\lfloor d^c\rfloor, \qquad r=2^{\Theta(p/d)},\qquad c>0,\quad 0<\epsilon<1. \] The exponents and comparison constants are fixed, and we impose their further restrictions in Proposition~\ref{prop:simultaneous-layer}. Two consequences explain the layout. The polynomial length $r$ grows faster than every fixed power of $p$, so a scan of a record pays for polynomial work on its address. Also $K/\log p\to\infty$, which will make the exceptional set in a packed change of address bits small enough to repair by sorting. We will obtain cost $O(Vd^{\lambda'})$, with $\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly factors would require $D$ whole-array passes.


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

Write the body to `exegenius/tasks/0029-write-simultaneous-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0029-write-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0029-write-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0029-write-simultaneous-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
