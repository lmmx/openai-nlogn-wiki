# exegenius task 0040-write-main-theorem

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F8V` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: algorithm analysis with big-O, divide and conquer and sorting, discrete mathematics (sets, permutations, modular arithmetic, primes, induction), and introductory linear algebra (matrices, linear maps, invertibility, triangular and permutation matrices). They know polynomials and complex numbers including roots of unity and Euler's formula, basic calculus functions, and basic Turing machines with several tapes and head movements. They have probably met schoolbook and Karatsuba multiplication and the idea of the FFT, but have not studied abstract algebra beyond basics, finite-field theory, numerical analysis of error, multidimensional Fourier methods, or the Schönhage–Strassen line of fast multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n barrier
- Convolution
- Radix-digit convolution
- Discrete Fourier transform
- Fast Fourier transform with butterflies
- Fixed-point complex grid and truncation
- Contractions and error accounting
- Subspaces, rank and orthogonal complements
- Arrays as address fields on tape
- Controlled cyclic shift
- Scratch-restoring bank exchange
- Frames: changing representation along a network
- Triple-subset labels and the rank budget
- Address shear and triangular factorization
- Recursive rank saving
- Power-width chunk interchange
- Address chunk interchange
- Complex phase network
- Packed selected-bit addition
- Simultaneous butterfly layer
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal polynomial variable whose powers act as roots of unity because y^r=−1.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Retained frequency order
- Transform layout on tape
- Signed packing (Kronecker substitution)
- Normalized convolution over the polynomial ring
- Cyclic-to-negacyclic coefficient twist
- Bluestein chirp identity
- Gaussian resampling
- Retained permutation cancellation
- Chinese-remainder address map
- Source transform on the padded box
- Parameter regime for the multiplier
- Precision and exact recovery
- The multiplication algorithm
- Cost accounting and the exponent κ
- Binary numerals and bit strings (also: binary representation, bit string, binary expansion, most significant bit, bits)
- Positional notation in any radix (also: base-b representation, radix, digits in base b, mixed radix)
- Integer division with remainder, floor and ceiling (also: Euclidean division, quotient and remainder, floor function, ceiling function, rounding to nearest integer)
- Modular arithmetic (also: congruence, residues mod m, integers mod m, Z/mZ, clock arithmetic)
- Arithmetic modulo 2 and XOR (also: XOR, exclusive or, bitwise XOR, parity, F_2, GF(2), addition mod 2)
- Primes, coprimality and gcd (also: prime number, relatively prime, greatest common divisor, pairwise coprime, Euclid's algorithm)
- Roots of unity and Euler's formula (also: e^{i theta}, primitive root of unity, nth roots of unity, unit circle, complex exponential)
- Exponential, logarithm and Gaussian function (also: exp, log base 2, lg, natural logarithm, e^{-x^2}, bell curve)
- Asymptotic notation beyond big-O (also: Omega, Theta, little-o, liminf, limit inferior, omega notation)
- Geometric series and sums (also: geometric sum, geometric progression, summation, telescoping)
- Divide and conquer and recurrences (also: recursion, recurrence relation, master theorem, recursion tree, T(n)=aT(n/b)+f(n))
- Schoolbook and Karatsuba multiplication (also: long multiplication, grade-school multiplication, Karatsuba algorithm, O(n^2) multiplication, integer multiplication)
- Sorting and its cost (also: merge sort, comparison sorting, O(n log n) sorting, sorting algorithms)
- Permutations and bijections (also: permutation, bijection, one-to-one correspondence, inverse permutation, reordering)
- Sets, subsets and Cartesian products (also: subset, Cartesian product, indicator vector, characteristic vector, tuples, set intersection, intersection size)
- Multidimensional arrays and row-major order (also: lexicographic order, row-major order, array indexing, nested loops, matrix as array)
- Matrices, vectors and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, linear transformation, linear operator, linear combination, vector space, linear independence, basis, dimension)
- Triangular and permutation matrices (also: lower-triangular matrix, upper-triangular matrix, permutation matrix, LU decomposition, identity matrix, diagonal matrix)
- Dot product, inner product and orthogonality (also: inner product, scalar product, orthogonal vectors, orthonormal, bilinear form)
- Dyadic rationals and fixed-width numerators (also: dyadic fraction, binary fraction, number over a power of two, binary point)
- Matrix transposition (also: transpose, row-major to column-major, transposing an array)
- Triangle inequality and norms (also: maximum norm, sup norm, modulus inequality, |a+b|<=|a|+|b|, error bound)
- Mathematical induction and proof by contradiction (also: induction, inductive proof, proof techniques)
- Cyclic shifts and rotations of lists (also: circular shift, rotation of array, wrap-around shift, cyclic rotation)
- Subroutines and composition of algorithms (also: calling a procedure, black box subroutine, reduction, algorithm composition)

## This page

Concept: Integer multiplication below n log n
Gloss: A deterministic multitape Turing machine multiplying two n-bit integers in O(n(lg n)^(1−κ)) time with κ=2^−182, disproving the n log n optimality conjecture in this model.

## This page in the argument

The step: A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.
How: Build two faster tape procedures (address chunk interchange and simultaneous butterfly layers) from rank-saving linear networks, use them in synthetic polynomial transforms and resampled source transforms for a convolution, reduce integer multiplication to that convolution, then prove exactness and add up costs.
Why: Scanning an array of $\Theta(n)$ bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$, so savings are needed both in data movement and in arithmetic. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))
Striking feature: The saving is a genuine power of $\log n$, but the exponent $\kappa=2^{-182}$ is minuscule; it comes from a chain of strict inequalities ($s<Wm$, $\tau<1$, $\lambda'<1$) each only barely below its trivial value. (explain why it holds, from the method)

Its sub-steps, in order:

- The elementary tape operations that every later procedure calls cost $O(V)$ in the logical volume $V$.
- There are two fixed linear networks on $W$ wires with labels of dimension $m$ whose edge changes cost $s<Wm$ smaller operations in total, one acting by bit address shears and one by phase kernels.
- Two disjoint contiguous address fields of $u$ bits of an array of volume $V$ can be interchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$. (on [Address chunk interchange](address-chunk-interchange.md))
- Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ to the same bit position in each of $D\le d$ address chunks of $K$ bits at once, on polynomial records with complex fixed-point coefficients, costs $O(Vd^{\lambda'})$ with one final truncation. (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md))
- Normalized synthetic Fourier transforms over $\mathcal R_r$ on $d-1$ axes can be run with the opposite order retained, at tape cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.
- On arrays of ring elements, two forward synthetic transforms, a pointwise polynomial product divided by $r$, and the opposite transform followed by a scaling by $M$ compute $(f*g)/T$ with error below $\sqrt2\,M(3\ell+1)2^{-p}$. (on [Normalized convolution over the polynomial ring](normalized-ring-convolution.md))
- A source Fourier transform on pairwise coprime (prime) lengths can be computed through power-of-two transforms, with the middle transform as a chirp convolution and with the coordinate permutations cancelling rather than being executed.
- The pieces assemble into a multiplier that is correct for every input and whose cost table fits the theorem.

## Steps this page derives

The argument gives this page these sub-steps of its step (A0, A, D, F, G). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**A0**: The elementary tape operations that every later procedure calls cost $O(V)$ in the logical volume $V$.
How: State the linear-time scans (digit moves, splits, row splits) and the controlled cyclic shift that follow from them.

**A**: There are two fixed linear networks on $W$ wires with labels of dimension $m$ whose edge changes cost $s<Wm$ smaller operations in total, one acting by bit address shears and one by phase kernels.
How: Design a scalar network that exchanges banks and restores scratch, lift it to arrays through frames, then choose subspace labels so each edge change is cheap and the total rank $s$ is below $Wm$.
- A.5: The relative rank deficits of both networks exceed $20\cdot2^{-50}$, so with $\tau=\sigma=1-2^{-50}$ one has $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$.
  Source: "\frac{s_{\rm b}}{W_{\rm b}}<m^\tau," (paper)
  > The relative rank deficits are \[ \eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m} =\frac{339}{22587335000000},\qquad \eta_{\rm c}=\frac{W_{\rm c}m-s_{\rm c}}{W_{\rm c}m} =\frac{73}{19906842167500}. \] For both recurrences we may use the fixed rational exponent \begin{equation} \tau=\sigma=1-2^{-50}. \label{eq:explicit-motif-exponents} \end{equation} Both exact deficits displayed above are greater than $20\cdot2^{-50}$. Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence \[ m^{1-2^{-50}} =m\exp(-2^{-50}\log m) >m(1-20\cdot2^{-50})>m(1-\eta) \] for either $\eta=\eta_{\rm b}$ or $\eta=\eta_{\rm c}$. Consequently \[ \frac{s_{\rm b}}{W_{\rm b}}<m^\tau, \qquad \frac{s_{\rm c}}{W_{\rm c}}<m^\sigma, \qquad 0<\tau=\sigma<1. \] Here $\sigma$ is a rational upper bound for the logarithmic exponent of the complex recurrence. \section{Faster interchange of address chunks} \label{sec:tape-interchange}

**D**: Normalized synthetic Fourier transforms over $\mathcal R_r$ on $d-1$ axes can be run with the opposite order retained, at tape cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.
How: Define the transforms with signed-shift roots, record where each frequency is stored, and lay the bits out so that each round is one simultaneous butterfly layer.

**F**: A source Fourier transform on pairwise coprime (prime) lengths can be computed through power-of-two transforms, with the middle transform as a chirp convolution and with the coordinate permutations cancelling rather than being executed.
How: Use Gaussian resampling to pass from prime lengths to power-of-two lengths, Bluestein's chirp to turn the middle transform into a cyclic convolution, and an algebraic cancellation of the retained permutations.

**G**: The pieces assemble into a multiplier that is correct for every input and whose cost table fits the theorem.
How: Choose compatible parameters, set up digits, the CRT layout, the twist and the source transforms, state the algorithm, verify precision and add up the costs.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- B (on [Address chunk interchange](address-chunk-interchange.md)): Two disjoint contiguous address fields of $u$ bits of an array of volume $V$ can be interchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$.
- C (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)): Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ to the same bit position in each of $D\le d$ address chunks of $K$ bits at once, on polynomial records with complex fixed-point coefficients, costs $O(Vd^{\lambda'})$ with one final truncation.
- E (on [Normalized convolution over the polynomial ring](normalized-ring-convolution.md)): On arrays of ring elements, two forward synthetic transforms, a pointwise polynomial product divided by $r$, and the opposite transform followed by a scaling by $M$ compute $(f*g)/T$ with error below $\sqrt2\,M(3\ell+1)2^{-p}$.
- A0.1 (on [Arrays as address fields on tape](tape-address-model.md)): Fixed digit permutations, digit moves, splits on a digit and cyclic row splits of an array of logical volume $V$ stored in lexicographic order each take $O(V)$ steps on a fixed number of tapes.
- A0.2 (on [Controlled cyclic shift](controlled-cyclic-shift.md)): Adding to a target address field $y\in[Q]$ an offset computed from earlier control fields, modulo $Q=q^b$, costs $O(V)$ although the fields may be arbitrarily long.
- A.1 (on [Scratch-restoring bank exchange](scratch-restoring-exchange.md)): A fixed linear network of copy, gather, scatter and side-injection gates exchanges two banks, sending $(X_a,Y_a)$ to $(-Y_a,X_a)$ in three stages, and returns every scratch wire to its arbitrary initial value.
- A.2 (on [Frames: changing representation along a network](array-frames.md)): If each scalar wire is replaced by an array and stored as $D_vg$ for an invertible frame $D_v$, a pointwise linear gate commutes with the frame, so the implemented operator is only $D_{\rm out}\mathsf S D_{\rm in}^{-1}$.
- A.3 (on [Triple-subset labels and the rank budget](subset-intersection-labels.md)): Attaching nested nondegenerate subspaces built from indicator vectors of three-element subsets to the gates and terminals of the bit network gives a total edge rank $s_{\rm b}$ strictly less than $W_{\rm b}m$.
- A.4 (on [Complex phase network](phase-frame-network.md)): In the second network, over Gaussian dyadics with binary labels, each edge frame change is a product of translation kernels $aI+bX_v$, one per orthonormal basis vector of its residual, their total number is $s_{\rm c}<W_{\rm c}m$, and the endpoint operator is $C^{\otimes m}$ on every role.
- D.1 (on [Synthetic polynomial transform](synthetic-polynomial-transform.md)): Over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ the transforms $F_t^\pm$ with roots $\omega_t=y^{2r/t}$ are contractions with $F_t^+F_t^-=t^{-1}I$, and $F_t^-$ is computed by decimation-in-frequency butterflies whose twiddles are signed shifts.
- D.2 (on [Retained frequency order](stored-frequency-order.md)): The forward transform writes its outputs in bit-reversed order, the pointwise product and the opposite transform use that same order, so no permutation is ever executed.
- D.3 (on [Transform layout on tape](transform-tape-layout.md)): Placing the selected bit of each axis at a common offset in consecutive $K$-bit chunks makes each transform round one simultaneous layer, so a synthetic transform of $T$ records of $p$-bit coefficients costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\,\ell\,2^{-p}$.
- F.1 (on [Gaussian resampling](gaussian-resampling.md)): A Fourier transform of prime length $s$ equals $2^{2\alpha^2}B_0P_tF_tA$ for a power-of-two length $t>s$ with Gaussian contractions $A$ and $B_0$ and with the coordinate permutations kept in the formula; on $d$ axes this tensors to $RF_{\boldsymbol s}=2^{\gamma}\mathcal B_0QF_{\boldsymbol t}\mathcal A$.
- F.2 (on [Bluestein chirp identity](bluestein-chirp.md)): The middle transform with its frequency permutation is $QF_{\boldsymbol t}u=\overline a\cdot\bigl(a*(\overline a\cdot u)\bigr)/T$ for the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$: chirp phases around one cyclic convolution.
- F.3 (on [Retained permutation cancellation](permutation-cancellation.md)): With the source permutation $R$ retained, $RF^+_{\boldsymbol s}[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$: the permutation cancels between the two forward transforms, the pointwise product and the opposite transform.
- G.1 (on [Parameter regime for the multiplier](parameter-regime.md)): Parameters $p=6b$, $d\approx p^\epsilon$, $T\in[4n/b,8n/b)$, $r=2^{\Theta(p^{1-\epsilon})}$, axis lengths $t_i\in\{r/2,r\}$ and distinct odd primes $s_i$ just below $t_i$ give $Tp=\Theta(n)$, $T/2<S<T$ and all the hypotheses of the lemmas.
- G.2 (on [Radix-digit convolution](radix-digit-reduction.md)): Writing each $n$-bit integer as a polynomial in $2^b$ with $q=\lceil n/b\rceil$ digits reduces the product to a convolution modulo $x^S-1$ without wraparound, with coefficients below $2^{3b}$.
- G.3 (on [Chinese-remainder address map](crt-axis-map.md)): The map $\Phi:x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ onto the product of pairwise coprime cyclic axes that preserves convolution, and it costs $O(Tp\,d^2(1+\ell^\tau))$.
- G.4 (on [Cyclic-to-negacyclic coefficient twist](coefficient-twist.md)): The map $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ multiplies coefficient $k$ by $\zeta^k$ and carries cyclic convolution on the last axis to convolution modulo $y^r+1$; untwisting recovers the cyclic result.
- G.5 (on [Source transform on the padded box](tensor-source-transform.md)): The approximate source transform, linewise $A$, chirp convolution of length $T$ on the padded box, linewise $B_0$ and an exact scale $2^\gamma$, equals $RF_{\boldsymbol s}$ on the prime-length source.
- G.6 (on [The multiplication algorithm](multiplication-algorithm.md)): The multiplier converts the inputs to digits, applies $\Phi$, takes two forward source transforms, multiplies pointwise, applies one opposite transform, scales by $S$ twice, rounds, applies $\Phi^{-1}$ and propagates carries to output the $2n$-bit product.
- G.7 (on [Precision and exact recovery](precision-exact-recovery.md)): The recovered convolution coefficients are within error below $1/2$ of integers below $2^{3b}$, so rounding and carry propagation give the exact product.
- G.8 (on [Cost accounting and the exponent κ](cost-accounting.md)): Dividing every cost by $V=Tp$ gives normalized costs at most $p^{1-2\kappa}$, the smallest margin $2^{-181}$ coming from the chunk-exchange term, so the total time is $O(n(\log n)^{1-\kappa})$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The multiplication algorithm](multiplication-algorithm.md): Digit conversion, the CRT map Φ, two forward source transforms, a pointwise product, one opposite transform, two scalings by S, rounding, inverse Φ and carry propagation to output the 2n-bit product.
  Shown as: Integer multiplication below n log n *<predicate>* The multiplication algorithm
- [Cost accounting and the exponent κ](cost-accounting.md): Dividing every cost by V=Tp gives normalized costs that are at most p^(1−2κ), the smallest margin 2^−181 coming from the chunk-exchange term, giving total time O(n(log n)^(1−κ)).
  Shown as: Integer multiplication below n log n *<predicate>* Cost accounting and the exponent κ
- [The n log n barrier](n-log-n-barrier.md): The Schönhage–Strassen conjecture that n log n is the optimal multiplication cost on multitape Turing machines, and the Harvey–van der Hoeven O(n log n) multiplier, which is used here only as a subroutine on short inputs.
  Shown as: Integer multiplication below n log n *<predicate>* The n log n barrier

## Other pages you may link to

- [Convolution](convolution.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Cyclic-to-negacyclic coefficient twist](coefficient-twist.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Arrays as address fields on tape](tape-address-model.md)
- [Controlled cyclic shift](controlled-cyclic-shift.md)
- [Scratch-restoring bank exchange](scratch-restoring-exchange.md)
- [Frames: changing representation along a network](array-frames.md)
- [Subspaces, rank and orthogonal complements](rank-and-orthogonal-subspaces.md)
- [Triple-subset labels and the rank budget](subset-intersection-labels.md)
- [Address shear and triangular factorization](address-shear-factorization.md)
- [Recursive rank saving](rank-saving-recurrence.md)
- [Power-width chunk interchange](power-width-interchange.md)
- [Address chunk interchange](address-chunk-interchange.md)
- [Chinese-remainder address map](crt-axis-map.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Fixed-point complex grid and truncation](fixed-point-complex-arithmetic.md)
- [Complex phase network](phase-frame-network.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Fast Fourier transform with butterflies](fft-butterflies.md)
- [Synthetic polynomial transform](synthetic-polynomial-transform.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Retained frequency order](stored-frequency-order.md)
- [Transform layout on tape](transform-tape-layout.md)
- [Contractions and error accounting](contraction-error-propagation.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](permutation-cancellation.md)
- [Normalized convolution over the polynomial ring](normalized-ring-convolution.md)
- [Parameter regime for the multiplier](parameter-regime.md)
- [Radix-digit convolution](radix-digit-reduction.md)
- [Source transform on the padded box](tensor-source-transform.md)
- [Precision and exact recovery](precision-exact-recovery.md)

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}


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

Write the body to `exegenius/tasks/0040-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0040-write-main-theorem.answer.json`, then run `exegenius submit 0040-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0040-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
