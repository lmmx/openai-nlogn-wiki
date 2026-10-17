# exegenius task 0008-write-rank-recurrence

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
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
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

Concept: Recursive power saving
Gloss: Each call at parameter m·f makes s calls at parameter f on streams of 1/W the volume, so cost per unit volume grows by s/W < m per factor m, giving a power saving.

## This page in the argument

The step: Both tape primitives (the interchange of two address chunks of $u$ digits and the simultaneous butterfly layer on up to $d$ axes) cost the volume times a power below one of their width, because a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$, so the cost per unit volume grows by $s/W<m$ per factor $m$ of the parameter.
How: Build a fixed finite linear network of $W$ wires that exchanges two banks and restores all scratch values, make the representation of each wire's array vary along the network through frames so that an edge costs one smaller call per unit of rank, show the total rank $s$ is below $Wm$, fix an exponent, and solve the recurrence in the bit variant (interchange) and the complex variant (butterfly layer).
Why: Dividing cost by volume, passing from parameter $f$ to $mf$ multiplies the recursive contribution by $s/W$, which is strictly less than the factor $m$ by which the parameter grew when $s<Wm$; so the recursion's solution is a power of the parameter below the first power. (the sources say so: "is the source of the power saving" (paper))
Striking feature: The saving is tiny but strictly positive: $s/W=m(1-\eta)$ with $\eta\approx10^{-11}$, so the resulting exponent is $1-2^{-50}$, only just below 1; the whole power saving rests on the strict inequality $s<Wm$. (explain why it holds, from the method)

Its sub-steps, in order:

- A recursive call at parameter $mf$ uses $s$ calls at parameter $f$, each on a stream of volume $V/W$.
- There is a fixed linear network of $W$ wires on two banks $X_a,Y_a$ ($a\in\mathcal T^3$, $\mathcal T$ the three-element subsets of $[h]$) that sends $(X_a,Y_a)\mapsto(-Y_a,X_a)$ and restores every scratch wire whatever its initial value, in a bit version (wires $W_{\rm b}$) and a complex version (wires $W_{\rm c}$). (on [Linear exchange network with restored scratch wires](exchange-network.md))
- If every scalar wire value is replaced by an array over a finite address set $\Omega$ and every gate acts pointwise, then assigning an invertible operator $D_v$ (a frame) to each source, gate and sink, with the same $D_v$ on all incidences of a gate, makes the network apply $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$: a route from input role $w$ to output role $\rho(w)$ applies only the endpoint frames $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ and its scalar sign. (on [Frames on wire arrays](array-frames.md))
- Attaching to the gates nondegenerate subspaces of an $m$-dimensional space, nested along every edge, the number of smaller calls (the total rank of the edge changes) is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$ for the bit network and $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$ for the complex network, both strictly less than $Wm$, because $L/N<1/2$. (on [Nested subspace labels and rank deficit](subspace-labels.md))
- With $\tau=\sigma=1-2^{-50}$ one has $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$, so $0<\tau=\sigma<1$ are admissible exponents for both recurrences.
- Bit variant: two disjoint address chunks of $u$ bits can be interchanged on a fixed number of tapes in $O(Vu^\tau)$ time, $\tau=1-2^{-50}$, although the intermediate steps form XOR combinations of data. (on [Fast address-chunk interchange](address-interchange.md))
- Complex variant: the tensor product of $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ on one bit of each of $D\le d$ address chunks (each of $K$ bits, selected at a common offset), acting coefficientwise on polynomial records with $r$ complex $p$-bit coefficients, is computed exactly followed by one truncation $Q_p$, in $O(Vd^{\lambda'})$ time with $\lambda'<1$, rather than $D$ whole-array passes. (on [Simultaneous butterfly layer](simultaneous-layer.md))

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.0, S1.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.0**: A recursive call at parameter $mf$ uses $s$ calls at parameter $f$, each on a stream of volume $V/W$.
Source: "A recursive call at parameter $mf$ therefore uses $s$ calls at parameter" (paper)
> A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$. The parameter counts field digits for address interchange and selected axes for a numerical layer. After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving. The later tape and arithmetic estimates preserve it, including the work of changing numerical address coordinates. Those changes are implemented by whole-chunk moves and controlled shifts, followed by a deterministic correction of the explicitly identified exceptional addresses.

**S1.4**: With $\tau=\sigma=1-2^{-50}$ one has $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$, so $0<\tau=\sigma<1$ are admissible exponents for both recurrences.
How: Compare the relative deficit $\eta$ with $20\cdot2^{-50}$ and bound $m^{1-2^{-50}}$ from below by the chain $m^{1-2^{-50}}=m\exp(-2^{-50}\log m)>m(1-20\cdot2^{-50})>m(1-\eta)=s/W$.
- S1.4.1: The relative deficits are $\eta_{\rm b}=(W_{\rm b}m-s_{\rm b})/(W_{\rm b}m)=339/22587335000000$ and $\eta_{\rm c}=73/19906842167500$.
  Source: "\eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m}" (paper)
  > The relative rank deficits are \[ \eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m} =\frac{339}{22587335000000},\qquad \eta_{\rm c}=\frac{W_{\rm c}m-s_{\rm c}}{W_{\rm c}m} =\frac{73}{19906842167500}. \] For both recurrences we may use the fixed rational exponent \begin{equation} \tau=\sigma=1-2^{-50}. \label{eq:explicit-motif-exponents} \end{equation} Both exact deficits displayed above are greater than $20\cdot2^{-50}$. Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence \[ m^{1-2^{-50}} =m\exp(-2^{-50}\log m) >m(1-20\cdot2^{-50})>m(1-\eta) \] for either $\eta=\eta_{\rm b}$ or $\eta=\eta_{\rm c}$. Consequently \[ \frac{s_{\rm b}}{W_{\rm b}}<m^\tau, \qquad \frac{s_{\rm c}}{W_{\rm c}}<m^\sigma, \qquad 0<\tau=\sigma<1. \] Here $\sigma$ is a rational upper bound for the logarithmic exponent of the complex recurrence. \section{Faster interchange of address chunks} \label{sec:tape-interchange}
- S1.4.2: Both exact deficits exceed $20\cdot2^{-50}$.
  Source: "Both exact deficits displayed above are greater than $20\cdot2^{-50}$." (paper)
  > The relative rank deficits are \[ \eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m} =\frac{339}{22587335000000},\qquad \eta_{\rm c}=\frac{W_{\rm c}m-s_{\rm c}}{W_{\rm c}m} =\frac{73}{19906842167500}. \] For both recurrences we may use the fixed rational exponent \begin{equation} \tau=\sigma=1-2^{-50}. \label{eq:explicit-motif-exponents} \end{equation} Both exact deficits displayed above are greater than $20\cdot2^{-50}$. Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence \[ m^{1-2^{-50}} =m\exp(-2^{-50}\log m) >m(1-20\cdot2^{-50})>m(1-\eta) \] for either $\eta=\eta_{\rm b}$ or $\eta=\eta_{\rm c}$. Consequently \[ \frac{s_{\rm b}}{W_{\rm b}}<m^\tau, \qquad \frac{s_{\rm c}}{W_{\rm c}}<m^\sigma, \qquad 0<\tau=\sigma<1. \] Here $\sigma$ is a rational upper bound for the logarithmic exponent of the complex recurrence. \section{Faster interchange of address chunks} \label{sec:tape-interchange}
- S1.4.3: Since $m<2^{20}$ and $\log2<1$ we have $\log m<20$.
  Source: "Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence" (paper)
  > The relative rank deficits are \[ \eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m} =\frac{339}{22587335000000},\qquad \eta_{\rm c}=\frac{W_{\rm c}m-s_{\rm c}}{W_{\rm c}m} =\frac{73}{19906842167500}. \] For both recurrences we may use the fixed rational exponent \begin{equation} \tau=\sigma=1-2^{-50}. \label{eq:explicit-motif-exponents} \end{equation} Both exact deficits displayed above are greater than $20\cdot2^{-50}$. Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence \[ m^{1-2^{-50}} =m\exp(-2^{-50}\log m) >m(1-20\cdot2^{-50})>m(1-\eta) \] for either $\eta=\eta_{\rm b}$ or $\eta=\eta_{\rm c}$. Consequently \[ \frac{s_{\rm b}}{W_{\rm b}}<m^\tau, \qquad \frac{s_{\rm c}}{W_{\rm c}}<m^\sigma, \qquad 0<\tau=\sigma<1. \] Here $\sigma$ is a rational upper bound for the logarithmic exponent of the complex recurrence. \section{Faster interchange of address chunks} \label{sec:tape-interchange}
- S1.4.4: Therefore $m^{1-2^{-50}}=m\exp(-2^{-50}\log m)>m(1-20\cdot2^{-50})>m(1-\eta)$ for either $\eta=\eta_{\rm b}$ or $\eta_{\rm c}$.
  Source: "=m\exp(-2^{-50}\log m)" (paper)
  > The relative rank deficits are \[ \eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m} =\frac{339}{22587335000000},\qquad \eta_{\rm c}=\frac{W_{\rm c}m-s_{\rm c}}{W_{\rm c}m} =\frac{73}{19906842167500}. \] For both recurrences we may use the fixed rational exponent \begin{equation} \tau=\sigma=1-2^{-50}. \label{eq:explicit-motif-exponents} \end{equation} Both exact deficits displayed above are greater than $20\cdot2^{-50}$. Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence \[ m^{1-2^{-50}} =m\exp(-2^{-50}\log m) >m(1-20\cdot2^{-50})>m(1-\eta) \] for either $\eta=\eta_{\rm b}$ or $\eta=\eta_{\rm c}$. Consequently \[ \frac{s_{\rm b}}{W_{\rm b}}<m^\tau, \qquad \frac{s_{\rm c}}{W_{\rm c}}<m^\sigma, \qquad 0<\tau=\sigma<1. \] Here $\sigma$ is a rational upper bound for the logarithmic exponent of the complex recurrence. \section{Faster interchange of address chunks} \label{sec:tape-interchange}
- S1.4.5: Consequently $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$ with $0<\tau=\sigma<1$.
  Source: "\frac{s_{\rm b}}{W_{\rm b}}<m^\tau," (paper)
  > The relative rank deficits are \[ \eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m} =\frac{339}{22587335000000},\qquad \eta_{\rm c}=\frac{W_{\rm c}m-s_{\rm c}}{W_{\rm c}m} =\frac{73}{19906842167500}. \] For both recurrences we may use the fixed rational exponent \begin{equation} \tau=\sigma=1-2^{-50}. \label{eq:explicit-motif-exponents} \end{equation} Both exact deficits displayed above are greater than $20\cdot2^{-50}$. Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence \[ m^{1-2^{-50}} =m\exp(-2^{-50}\log m) >m(1-20\cdot2^{-50})>m(1-\eta) \] for either $\eta=\eta_{\rm b}$ or $\eta=\eta_{\rm c}$. Consequently \[ \frac{s_{\rm b}}{W_{\rm b}}<m^\tau, \qquad \frac{s_{\rm c}}{W_{\rm c}}<m^\sigma, \qquad 0<\tau=\sigma<1. \] Here $\sigma$ is a rational upper bound for the logarithmic exponent of the complex recurrence. \section{Faster interchange of address chunks} \label{sec:tape-interchange}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.1 (on [Linear exchange network with restored scratch wires](exchange-network.md)): There is a fixed linear network of $W$ wires on two banks $X_a,Y_a$ ($a\in\mathcal T^3$, $\mathcal T$ the three-element subsets of $[h]$) that sends $(X_a,Y_a)\mapsto(-Y_a,X_a)$ and restores every scratch wire whatever its initial value, in a bit version (wires $W_{\rm b}$) and a complex version (wires $W_{\rm c}$).
- S1.2 (on [Frames on wire arrays](array-frames.md)): If every scalar wire value is replaced by an array over a finite address set $\Omega$ and every gate acts pointwise, then assigning an invertible operator $D_v$ (a frame) to each source, gate and sink, with the same $D_v$ on all incidences of a gate, makes the network apply $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$: a route from input role $w$ to output role $\rho(w)$ applies only the endpoint frames $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ and its scalar sign.
- S1.3 (on [Nested subspace labels and rank deficit](subspace-labels.md)): Attaching to the gates nondegenerate subspaces of an $m$-dimensional space, nested along every edge, the number of smaller calls (the total rank of the edge changes) is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$ for the bit network and $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$ for the complex network, both strictly less than $Wm$, because $L/N<1/2$.
- S1.5 (on [Fast address-chunk interchange](address-interchange.md)): Bit variant: two disjoint address chunks of $u$ bits can be interchanged on a fixed number of tapes in $O(Vu^\tau)$ time, $\tau=1-2^{-50}$, although the intermediate steps form XOR combinations of data.
- S1.6 (on [Simultaneous butterfly layer](simultaneous-layer.md)): Complex variant: the tensor product of $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ on one bit of each of $D\le d$ address chunks (each of $K$ bits, selected at a common offset), acting coefficientwise on polynomial records with $r$ complex $p$-bit coefficients, is computed exactly followed by one truncation $Q_p$, in $O(Vd^{\lambda'})$ time with $\lambda'<1$, rather than $D$ whole-array passes.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Nested subspace labels and rank deficit](subspace-labels.md): Assigning nondegenerate subspaces of an m-dimensional space to gates so adjacent labels are nested; the total dimension change over edges, the number s of smaller calls, is strictly less than W·m.
  Shown as: Recursive power saving *<predicate>* Nested subspace labels and rank deficit

## Pages that build on this one

- Fast address-chunk interchange: The first tape procedure: exchanging two disjoint equal-width address fields of u digits in time O(V·u^τ) for a fixed τ < 1, using XOR combinations of intermediate data.
- Simultaneous butterfly layer: The second tape procedure: applying H₀ coefficientwise on the same bit of up to d address chunks in time O(V·d^λ′) for a fixed λ′ < 1, instead of d passes.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
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
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](chirp.md)
- [Retained permutation cancellation](retained-permutations.md)
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

- "This strict inequality" (paper)

  > A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$. The parameter counts field digits for address interchange and selected axes for a numerical layer. After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving. The later tape and arithmetic estimates preserve it, including the work of changing numerical address coordinates. Those changes are implemented by whole-chunk moves and controlled shifts, followed by a deterministic correction of the explicitly identified exceptional addresses.

- "A recursive call at parameter $mf$ therefore uses $s$ calls at parameter" (paper)

  > A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$. The parameter counts field digits for address interchange and selected axes for a numerical layer. After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving. The later tape and arithmetic estimates preserve it, including the work of changing numerical address coordinates. Those changes are implemented by whole-chunk moves and controlled shifts, followed by a deterministic correction of the explicitly identified exceptional addresses.


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

Write the body to `exegenius/tasks/0008-write-rank-recurrence.answer.md` and the JSON to `exegenius/tasks/0008-write-rank-recurrence.answer.json`, then run `exegenius submit 0008-write-rank-recurrence` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0008-write-rank-recurrence`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
