# exegenius task 0035-write-resampling-no-sort

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F2V` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: fluent in asymptotic analysis, discrete mathematics (sets, functions, modular arithmetic, primes and gcd, permutations, induction and recursion), first-course linear algebra (matrices, invertibility, rank, basis, dimension, linear maps over the rationals and the complex numbers), complex arithmetic with Euler's formula, and the basic Turing machine model with tapes and step counting. They have seen binary representation, bit operations such as XOR, and perhaps the idea of multiplying integers by divide and conquer, but have not been taught the discrete Fourier transform, the FFT, polynomial transforms, Schönhage–Strassen, abstract ring theory beyond the basic definition, tensor products, or numerical error analysis, and these are what the wiki must explain.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- The n log n optimality conjecture
- Fixed finite-tape Turing machine model
- Arrays, address fields and elementary scans
- Controlled cyclic shifts and rational scalings
- Integer multiplication as digit convolution
- Normalized DFT and cyclic convolution
- Multidimensional (tensor) Fourier transform
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Fixed-point disk-grid arithmetic and contractions
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): the formal variable of the polynomials, subject to y^r = -1.
  - $r$ (record length): the number of complex coefficients in a polynomial record, a power of two.
- Synthetic Fourier transform modulo y^r + 1
  - $y$ (ring variable): the formal variable of the polynomial ring, subject to y^r = -1.
  - $r$ (record length): the number of complex coefficients in a polynomial record, a power of two.
- Radix-2 butterfly layers and stored frequency order
- Twist from cyclic to negacyclic convolution
- Established n log n multiplier as a subroutine
- Signed Kronecker packing of polynomial products
- Bluestein's chirp identity
- Three-element subset intersection gadget
- Linear network that exchanges two banks and restores scratch values
- Frames and the common-frame identity
- Orthogonal complements and projections in a bilinear space
- Nested subspace labels and the rank saving
- Lower-triangular rank factorization
- Cost of a rational matrix shear
- Power-width chunk interchange in O(Ve^τ) time
  - $V$ (stored bit volume): the number of data bits stored in the array.
  - $e$ (chunk width): the number of radix digits in each of the two interchanged chunks, a power of a fixed integer m.
  - $\tau$ (interchange exponent): a fixed rational constant strictly between 0 and 1.
- Chunk interchange in O(Vu^τ) time
  - $V$ (stored bit volume): the number of data bits stored in the array.
  - $u$ (chunk width): the number of bits in each of the two interchanged address chunks.
  - $\tau$ (interchange exponent): a fixed rational constant strictly below 1, namely 1 - 2^{-50}.
- Two-point kernel C and the complex phase network
- Packed XOR of selected bits across address chunks
- Simultaneous butterfly layer in O(Vd^λ') time
  - $V$ (stored bit volume): the number of data bits stored in the array of records.
  - $d$ (axis count): the number of equal-width address chunks (transform axes) whose selected bit is butterflied simultaneously.
  - $\lambda'$ (layer exponent): a fixed rational constant strictly below 1, namely 1 - 2^{-54}.
- Layout and cost of the synthetic transform
- Convolution over the polynomial ring from the retained layout
- Modular arithmetic and residues (also: congruence, mod q, Z/qZ, integers modulo q, remainder)
- Primes, divisibility, gcd and coprimality (also: prime number, coprime, relatively prime, pairwise coprime, greatest common divisor, odd prime, units mod q, invertible residue)
- Binary representation of integers (also: bit string, radix 2, binary expansion, most significant bit, val(x), bin_k(z), padding with zeros, base-2 digits)
- Bitwise XOR (also: exclusive or, XOR combination, addition mod 2, parity)
- Logarithms, floors, ceilings and powers of two (also: lg, log base 2, floor, ceiling, power of two, exponent rules)
- Matrices, invertibility and rank (also: invertible matrix, matrix inverse, matrix product, rank of a matrix, linear map, linear transformation, Gaussian elimination, row operations)
- Vector spaces, basis and dimension (also: subspace, span, linear independence, linear combination, vector space over the rationals, dimension, standard basis, direct sum)
- Permutations and permutation matrices (also: bijection, reordering of indices, sorting by a permutation, permutation of coordinates, identity matrix)
- Lexicographic order and index tuples (also: dictionary order, Cartesian product of index sets, multi-index, mixed-radix positional notation, row-major order)
- Euler's formula and roots of unity as points on the unit circle (also: e^{i theta}, cos and sin form, unit circle, primitive root of unity, modulus of a complex number, complex conjugate, real and imaginary parts)
- Geometric series and orthogonality of sums of roots of unity (also: geometric sum, sum of powers of a root of unity vanishes, summation manipulation, Kronecker delta, indicator function)
- Norms and the triangle inequality (also: absolute value bound, sup norm, maximum norm, Euclidean norm, error bound, triangle inequality, operator norm)
- Rational numbers, dyadic rationals and exact arithmetic (also: dyadic number, dyadic rational, power-of-two denominator, Gaussian rational, Gaussian integer, rounding to nearest integer, truncation toward zero)
- Algebraic structures: groups, rings and isomorphisms (also: ring, commutative ring, algebra, ring isomorphism, group, cyclic group, zero divisor, unit, field)
- Discrete-math proof techniques (also: induction, recursion, recurrence relation, divide and conquer, proof by cases, pigeonhole principle, counting arguments)
- Schoolbook multiplication and divide-and-conquer multiplication (also: long multiplication, quadratic-time multiplication, Karatsuba, carry propagation, digit-by-digit addition)
- Multitape machine cost model and linear-time scans (also: sequential tape access, tape scan, head movement cost, one-pass copy, linear-time tape operations, sorting by merging, bit-level time complexity)
- Complex polynomial evaluation and interpolation (also: evaluating a polynomial at points, coefficient list, degree, polynomial identity, Horner's rule, coefficient extraction)
- Gaussian function (also: bell curve, exp(-x^2), normal density, Gaussian weight)
- Convolution as polynomial multiplication (also: convolution of sequences, sum over i+j=k, linear convolution, Cauchy product, coefficient of a product)
- Quantifiers, sets and basic asymptotic notation beyond big-O (also: little-o, Theta, Omega, sufficiently large n, for all n, worst-case time, lower bound versus upper bound)

## This page

Concept: Resampling with the permutations left in the transform
Gloss: The tensor form of Gaussian resampling in which the source and target coordinate permutations R and Q stay inside the transform identity, so they need not be executed as separate sorts.

## This page in the argument

The step: Gaussian resampling gives $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ in one dimension and $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ on $d$ axes, with the permutations $R$ and $Q$ left inside the transform.
How: keep the coordinate permutations in the transform identity of Harvey and van der Hoeven's resampling, bound the numerical maps $A$ and $B_0$, and tensor them line by line
Why: The usual implementation sorts twice per coordinate; leaving the permutations in the identity avoids those sorts, and later they cancel or are absorbed. (the sources say so: "coordinate. We retain both permutations in the transform formula and" (paper))

Its sub-steps, in order:

- For coprime $s<t$ with $t/s-1>p/\alpha^4$ there are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$.
- They satisfy $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$.
- Their disk-grid approximations have error below $p^2$ and cost $O(tp^{3/2+\delta}\alpha)$.
- The Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$ and the estimate $\|N-I\|<2^{-\alpha^2\theta}$ give an invertible $N$.
- Setting $A=\mathsf S/2$ and $B_0=\mathsf D'\mathsf J'C$ makes both contractions.
- Tensoring the one-dimensional identity gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$.
- At most $T/t_i$ lines are processed per axis, for total time $O(dTp^{3/2+\delta}\alpha)$.
- Exposing and restoring all axes in the padded box costs $O(Tpd^2(1+\ell^\tau))$ by chunk interchanges.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.; how: start from the Gaussian-resampling reduction of multiplication to transforms, make the transforms cheaper by two tape procedures that each save a power of the logarithm, then recover the product exactly and add up all costs (on [Multiplying n-bit integers in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Convolution of the radix digits modulo $x^S-1$ is reduced to the power-of-two ring convolution by Gaussian resampling, the Bluestein chirp, the Chinese-remainder axis map and a coefficient twist.; how: retain the resampling permutations inside the transform identity, absorb the middle transform into a chirp convolution, fix all sizes, move the digit list onto prime axes, and twist the last axis into the ring

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.1.1, S3.1.2, S3.1.3, S3.1.4, S3.1.5, S3.1.6, S3.1.7, S3.1.8). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.1.1**: For coprime $s<t$ with $t/s-1>p/\alpha^4$ there are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$.
Source: "There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and" (paper)
> \begin{lemma}[Resampling without executing the two permutations] \label{lem:no-sort-resampling} Fix $0<\delta<1/8$. Let $p>100$, $2\leq s<t<2^p$ and $2\leq\alpha<\sqrt p$ be integers, with $\gcd(s,t)=1$ and \[ \theta:=t/s-1>p/\alpha^4. \] Define coordinate permutations by \[ (P_su)_j=u_{tj},\qquad (P_tv)_k=v_{-sk}. \] There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ satisfying \begin{equation} P_sF_s=2^{2\alpha^2}B_0P_tF_tA. \label{eq:no-sort-one-dimensional} \end{equation} There are fixed multitape algorithms for approximations $\widetilde A:\mathbb D_p^s\to\mathbb D_p^t$ and $\widetilde B_0:\mathbb D_p^t\to\mathbb D_p^s$, each with error less than $p^2$ and time \[ O(tp^{3/2+\delta}\alpha). \] The constant is uniform in $p,s,t,\alpha$. Inputs and outputs use the scalar component format above and occur in increasing coordinate order. \end{lemma}

**S3.1.2**: They satisfy $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$.
Source: "P_sF_s=2^{2\alpha^2}B_0P_tF_tA." (paper)
> \begin{lemma}[Resampling without executing the two permutations] \label{lem:no-sort-resampling} Fix $0<\delta<1/8$. Let $p>100$, $2\leq s<t<2^p$ and $2\leq\alpha<\sqrt p$ be integers, with $\gcd(s,t)=1$ and \[ \theta:=t/s-1>p/\alpha^4. \] Define coordinate permutations by \[ (P_su)_j=u_{tj},\qquad (P_tv)_k=v_{-sk}. \] There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ satisfying \begin{equation} P_sF_s=2^{2\alpha^2}B_0P_tF_tA. \label{eq:no-sort-one-dimensional} \end{equation} There are fixed multitape algorithms for approximations $\widetilde A:\mathbb D_p^s\to\mathbb D_p^t$ and $\widetilde B_0:\mathbb D_p^t\to\mathbb D_p^s$, each with error less than $p^2$ and time \[ O(tp^{3/2+\delta}\alpha). \] The constant is uniform in $p,s,t,\alpha$. Inputs and outputs use the scalar component format above and occur in increasing coordinate order. \end{lemma}

**S3.1.3**: Their disk-grid approximations have error below $p^2$ and cost $O(tp^{3/2+\delta}\alpha)$.
Source: "O(tp^{3/2+\delta}\alpha)." (paper)
> \begin{lemma}[Resampling without executing the two permutations] \label{lem:no-sort-resampling} Fix $0<\delta<1/8$. Let $p>100$, $2\leq s<t<2^p$ and $2\leq\alpha<\sqrt p$ be integers, with $\gcd(s,t)=1$ and \[ \theta:=t/s-1>p/\alpha^4. \] Define coordinate permutations by \[ (P_su)_j=u_{tj},\qquad (P_tv)_k=v_{-sk}. \] There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ satisfying \begin{equation} P_sF_s=2^{2\alpha^2}B_0P_tF_tA. \label{eq:no-sort-one-dimensional} \end{equation} There are fixed multitape algorithms for approximations $\widetilde A:\mathbb D_p^s\to\mathbb D_p^t$ and $\widetilde B_0:\mathbb D_p^t\to\mathbb D_p^s$, each with error less than $p^2$ and time \[ O(tp^{3/2+\delta}\alpha). \] The constant is uniform in $p,s,t,\alpha$. Inputs and outputs use the scalar component format above and occur in increasing coordinate order. \end{lemma}

**S3.1.4**: The Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$ and the estimate $\|N-I\|<2^{-\alpha^2\theta}$ give an invertible $N$.
Source: "\mathsf T P_sF_s=P_tF_t\mathsf S," (paper)
> For $0\leq j<s$, define \[ q_j=\left\lfloor\frac{tj}{s}+\frac12\right\rfloor, \qquad \beta_j=\frac{tj}{s}-q_j. \] Thus $q_j$ is an integer nearest to $tj/s$, with ties rounded upward. Let $C:\mathbb C^t\to\mathbb C^s$ select these coordinates, and let $\mathsf D:\mathbb C^s\to\mathbb C^s$ be the diagonal map \[ (Cv)_j=v_{q_j},\qquad (\mathsf D u)_j=e^{\pi\alpha^2\beta_j^2}u_j. \] Set $N=C\mathsf T\mathsf D$. In $(Nu)_j$, the summand with index $j$ is exactly $u_j$: the factor in $\mathsf D$ cancels the Gaussian factor at the selected coordinate $q_j$. The other summands form $((N-I)u)_j$. The exact Gaussian identity and inverse estimate proved in \cite[Theorem~4.2 and Lemma~4.6]{HarveyHoeven2021} give \begin{equation} \mathsf T P_sF_s=P_tF_t\mathsf S, \qquad \|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}. \label{eq:gaussian-public-facts} \end{equation} The first identity uses the negative Fourier sign in our definition of $F_q$; its right-hand permutation is consequently multiplication of the frequency by $-s$. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have $\alpha^2\theta>p/\alpha^2>1$. Thus $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series. Put \[ \mathsf S'=\mathsf S/2,\qquad \mathsf J'=N^{-1}/2,\qquad \mathsf D'=2^{-(2\alpha^2-2)}\mathsf D. \] The proof of Proposition~4.7(i) in the cited paper gives \[ \|\mathsf S'\|<\frac34,\qquad \|\mathsf J'\|<\frac78,\qquad \|\mathsf D'\|<1. \] Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C

**S3.1.5**: Setting $A=\mathsf S/2$ and $B_0=\mathsf D'\mathsf J'C$ makes both contractions.
Source: "Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$." (paper)
> uation} \mathsf T P_sF_s=P_tF_t\mathsf S, \qquad \|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}. \label{eq:gaussian-public-facts} \end{equation} The first identity uses the negative Fourier sign in our definition of $F_q$; its right-hand permutation is consequently multiplication of the frequency by $-s$. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have $\alpha^2\theta>p/\alpha^2>1$. Thus $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series. Put \[ \mathsf S'=\mathsf S/2,\qquad \mathsf J'=N^{-1}/2,\qquad \mathsf D'=2^{-(2\alpha^2-2)}\mathsf D. \] The proof of Proposition~4.7(i) in the cited paper gives \[ \|\mathsf S'\|<\frac34,\qquad \|\mathsf J'\|<\frac78,\qquad \|\mathsf D'\|<1. \] Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$. Because $\|C\|=1$, both are contractions. The diagonal map $\mathsf D$ is invertible, and $C\mathsf T=N\mathsf D^{-1}$, so \[ (\mathsf D N^{-1}C)\mathsf T =\mathsf D N^{-1}(N\mathsf D^{-1})=I. \] Applying this left inverse to the first identity in \eqref{eq:gaussian-public-facts} gives $\mathsf D N^{-1}CP_tF_t\mathsf S=P_sF_s$. The normalizations in $\mathsf D'$, $\mathsf J'$, and $\mathsf S'$ have product $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$. Hence \[ B_0P_tF_tA =2^{-2\alpha^2}\mathsf D N^{-1}CP_tF_t\mathsf S =2^{-2\alpha^2}P_sF_s, \] which is \eqref{eq:no-sort-one-dimensional}.

**S3.1.6**: Tensoring the one-dimensional identity gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$.
Source: "Tensoring \eqref{eq:no-sort-one-dimensional} proves" (paper)
> \begin{proof} Tensoring \eqref{eq:no-sort-one-dimensional} proves \eqref{eq:no-sort-tensor}. To implement $\mathcal A$, first embed its input in the padded box by writing zero outside $\prod_i[0,s_i)$. Expand the axes one at a time. After the axes in a set $I$ have been expanded, the valid entries have coordinate ranges $[0,t_i)$ for $i\in I$ and $[0,s_i)$ otherwise; every other entry is zero. Expose the next axis $i$ as the innermost address field. On a line whose other coordinates are valid, read its first $s_i$ values and apply $\widetilde A_i$, then write the resulting $t_i$ values. On every other line write $t_i$ zeros. The new valid set is the one for $I\cup\{i\}$.

**S3.1.7**: At most $T/t_i$ lines are processed per axis, for total time $O(dTp^{3/2+\delta}\alpha)$.
Source: "At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$," (paper)
> For a fixed axis, the exact map acts independently on its valid lines and is zero on the other lines. Taking the maximum over the line norms shows that this axis map is a contraction; taking the maximum of the line errors gives an error less than $p^2$ for the whole axis. Composing the $d$ axis maps gives error less than $dp^2$. At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$, so their cost is bounded by \[ \sum_{i=1}^d\frac{T}{t_i} O(t_i p^{3/2+\delta}\alpha) =O(dTp^{3/2+\delta}\alpha). \] Initial padding costs $O(Tp)$, and scanning and zeroing the remaining lines costs $O(Tp)$ per axis. Both are within the same bound. All calls reuse one fixed collection of work tapes. Loop indices and the growing shape descriptor reside on tapes; they are not extra heads.

**S3.1.8**: Exposing and restoring all axes in the padded box costs $O(Tpd^2(1+\ell^\tau))$ by chunk interchanges.
Source: "$O(Tp(1+\ell^\tau))$. Exposing and restoring one axis needs" (paper)
> The descriptor records which coordinate each physical address field holds. Thus moving fields changes their positions, but not the validity conditions above. To move an axis past its neighbor, interchange their $\ell$-bit or $(\ell-1)$-bit address fields. Equal widths use Lemma~\ref{lem:chunk-swap}. For unequal widths, write the longer field as a leading bit $e$ followed by $\ell-1$ bits. If it comes first, the order is $e\,x\,y$, with $x,y$ of equal width. Interchange $x,y$, then move $e$ between them, obtaining $y\,e\,x$. If the longer field comes second, first move its leading bit left of the shorter field, then interchange the two equal-width pieces. The bit move uses Lemma~\ref{lem:elementary-streams}. Each adjacent interchange therefore costs $O(Tp(1+\ell^\tau))$. Exposing and restoring one axis needs $O(d)$ adjacent interchanges, hence all axes need $O(d^2)$. These are exact permutations of the padded box, so they change neither norms nor errors.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Gaussian resampling](gaussian-resampling.md): Harvey and van der Hoeven's identity expressing a Fourier transform of coprime length s through a Fourier transform of a larger power-of-two length t, using Gaussian-weighted interpolation maps A and B₀.
  Shown as: Resampling with the permutations left in the transform *<predicate>* Gaussian resampling
- [Fixed-point disk-grid arithmetic and contractions](fixed-point-disk-grid.md): Complex numbers stored as signed two's-complement integers scaled by 2^{-p} inside the unit disk; truncation Q_p toward zero costs error below √2·2^{-p}, and contractions never increase the sup norm so errors add up predictably.
  Shown as: Resampling with the permutations left in the transform *<predicate>* Fixed-point disk-grid arithmetic and contractions
- [Multidimensional (tensor) Fourier transform](multidim-transform.md): The tensor product of one-dimensional transforms along several axes; a transform on an array with axis lengths t_1,…,t_d is applied axis by axis.
  Shown as: Resampling with the permutations left in the transform *<predicate>* Multidimensional (tensor) Fourier transform

## Pages that build on this one

- Chirp identity and source-permutation cancellation: A chirp-convolution formula for Q·F_t that leaves the target permutation unexecuted, together with the fact that the source permutation R cancels across the two forward transforms, the pointwise product and the opposite transform.
- Source transform via resampling, chirp and ring convolution: The computed procedure for a source Fourier transform of prime lengths: Gaussian maps A, then a chirp transform evaluated by a twisted ring convolution, then B₀ and an exact power-of-two scale, with exact counterpart R F_s.
- Cost accounting and the saving exponent κ: A table of costs divided by Tp, each at most p^{1−2κ} thanks to the slack in the chosen exponents (seven dominant margins, the smallest 2^{-181} = 2κ), giving O(n (log n)^{1−κ}) overall.

## Other pages you may link to

- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Three-element subset intersection gadget](triple-gadget.md)
- [Linear network that exchanges two banks and restores scratch values](bank-exchange-network.md)
- [Fixed finite-tape Turing machine model](fixed-tape-model.md)
- [Established n log n multiplier as a subroutine](nlogn-subroutine.md)
- [Arrays, address fields and elementary scans](stream-arrays.md)
- [Frames and the common-frame identity](frames.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Orthogonal complements and projections in a bilinear space](bilinear-orthogonal.md)
- [Nested subspace labels and the rank saving](subspace-labels.md)
- [Lower-triangular rank factorization](triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Power-width chunk interchange in O(Ve^τ) time](power-width-interchange.md)
- [Chunk interchange in O(Vu^τ) time](chunk-swap.md)
- [Packed XOR of selected bits across address chunks](packed-selected-bits.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed Kronecker packing of polynomial products](signed-kronecker-packing.md)
- [Normalized DFT and cyclic convolution](dft-cyclic-convolution.md)
- [Chinese-remainder map to prime cyclic axes](crt-axis-map.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Twist from cyclic to negacyclic convolution](coefficient-twist.md)
- [Synthetic Fourier transform modulo y^r + 1](synthetic-transform.md)
- [Radix-2 butterfly layers and stored frequency order](butterfly-layers.md)
- [Two-point kernel C and the complex phase network](phase-kernel-network.md)
- [Simultaneous butterfly layer in O(Vd^λ') time](simultaneous-butterfly-layer.md)
- [Layout and cost of the synthetic transform](transform-layout.md)
- [Convolution over the polynomial ring from the retained layout](ring-convolution.md)
- [Chirp identity and source-permutation cancellation](chirp-permutation-cancel.md)
- [Choice of sizes, precision and prime axis lengths](parameter-choice.md)
- [Source transform via resampling, chirp and ring convolution](source-transform.md)
- [Exact recovery: scaling, rounding and carries](exact-recovery.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the saving exponent κ](cost-accounting.md)
- [Multiplying n-bit integers in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ satisfying" (paper)

  > \begin{lemma}[Resampling without executing the two permutations] \label{lem:no-sort-resampling} Fix $0<\delta<1/8$. Let $p>100$, $2\leq s<t<2^p$ and $2\leq\alpha<\sqrt p$ be integers, with $\gcd(s,t)=1$ and \[ \theta:=t/s-1>p/\alpha^4. \] Define coordinate permutations by \[ (P_su)_j=u_{tj},\qquad (P_tv)_k=v_{-sk}. \] There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ satisfying \begin{equation} P_sF_s=2^{2\alpha^2}B_0P_tF_tA. \label{eq:no-sort-one-dimensional} \end{equation} There are fixed multitape algorithms for approximations $\widetilde A:\mathbb D_p^s\to\mathbb D_p^t$ and $\widetilde B_0:\mathbb D_p^t\to\mathbb D_p^s$, each with error less than $p^2$ and time \[ O(tp^{3/2+\delta}\alpha). \] The constant is uniform in $p,s,t,\alpha$. Inputs and outputs use the scalar component format above and occur in increasing coordinate order. \end{lemma}

- "RF_{\boldsymbol s} =2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A" (paper)

  > \begin{lemma}[Tensor interface] \label{lem:tensor-resampling} Suppose every pair $(s_i,t_i)$, $1\leq i\leq d$, satisfies Lemma~\ref{lem:no-sort-resampling} with the same $p,\alpha,\delta$. Put $T=\prod_i t_i$, $\gamma=2d\alpha^2$, and \[ R=\bigotimes_iP_{s_i},\quad Q=\bigotimes_iP_{t_i},\quad \mathcal A=\bigotimes_i A_i,\quad \mathcal B_0=\bigotimes_i B_{0,i}. \] Then \begin{equation} RF_{\boldsymbol s} =2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A, \qquad F_{\boldsymbol q}:=\bigotimes_iF_{q_i}. \label{eq:no-sort-tensor} \end{equation} Also write $F_{\boldsymbol q}^+=\bigotimes_iF_{q_i}^+$. Both $\mathcal A$ and $\mathcal B_0$ are contractions. The linewise implementations of $\mathcal A$ and $\mathcal B_0$ each have error less than $dp^2$. The total time spent in the one-dimensional algorithms for both maps is $O(dTp^{3/2+\delta}\alpha)$, with a constant independent of $d$.

- "We retain both permutations in the transform formula and compute that formula directly." (paper)

  > The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two. Gaussian resampling connects these two shapes. Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and compute that formula directly. This section proves the resulting interface, including its tape cost when the number of coordinates grows.


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

Write the body to `exegenius/tasks/0035-write-resampling-no-sort.answer.md` and the JSON to `exegenius/tasks/0035-write-resampling-no-sort.answer.json`, then run `exegenius submit 0035-write-resampling-no-sort` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0035-write-resampling-no-sort`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
