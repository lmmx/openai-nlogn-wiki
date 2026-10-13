# exegenius task 0228-write-tensor-product

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist who has studied discrete mathematics (integers, modular arithmetic, gcd and primes at the basic level, sets, bijections, binomial coefficients), undergraduate linear algebra (vector spaces, matrices, rank, Gaussian elimination, dot products, norms), the single-variable calculus a CS degree requires (limits, convergence of sequences and series, basic integrals, logarithms and exponentials), algorithms and complexity (big-O together with Omega and Theta, recurrences, schoolbook multiplication, worst-case running time of Turing machines), and binary arithmetic with basic complex numbers. This covers the sources' integer, bit, linear-algebra, limit and asymptotic bookkeeping, but not prime-number density results, tensor products, operator norms and contractions, Gaussian integers, or the quotient-ring and Fourier machinery beyond the existing concepts.

The reader already understands these concepts:

- Big-O notation (also: O(n))
- Polynomials
- Complex numbers (also: Gaussian integers)
- Multitape Turing machine
- Fixed-tape machine model (also: fixed finite-tape model)
- Schonhage-Strassen optimality conjecture (also: n log n optimality conjecture)
- Power saving in the logarithmic factor (also: (lg n)^(1-kappa) saving)
- Linear network (also: fixed linear network, network, pointwise linear gate, wires, bank and forward invocation)
- Frame of a vertex (also: frame)
- Role streams from a cyclic row split (also: roles, wire streams)
- Subset-intersection finite network (also: three-element subset network, gather and scatter wires)
- Nested subspace labels
- Address shear (also: H + D shear, endpoint operator)
- Rank-saving recursion (also: recursive saving, recursive scheme, edge matrix)
- Fast interchange of address chunks (also: chunk interchange, address chunks, linear-cost address update, address fields, address field, bit procedure)
- Gaussian dyadic numbers (also: Gaussian dyadics, Z[i,1/2] (Gaussian dyadic numbers))
- Discrete Fourier transform (also: Fourier transform, twiddle step)
- Cyclic convolution (also: convolution modulo x^S - 1, normalized cyclic convolution)
- Radix-digit convolution (also: radix-2^b digit polynomials)
- Established fast multiplier (also: Harvey-van der Hoeven multiplier)
- Modular arithmetic (also: congruence, residue classes, integers modulo m, Z/mZ, modular inverse, division with remainder)
- Greatest common divisor and coprimality (also: gcd, relatively prime, pairwise coprime, Euclidean algorithm)
- Prime number (also: prime, primality, prime factorization)
- Binary field and exclusive or (also: F_2, GF(2), Z/2Z, XOR, exclusive or, bitwise XOR)
- Hamming weight (also: weight, popcount, number of ones)
- Two's-complement representation (also: two's complement, signed binary integer, signed fixed-width integer)
- Positional notation and binary representation (also: radix representation, base-b digits, binary representation, binary expansion, carries)
- Dyadic rational (also: dyadic fraction, binary fraction, finite binary expansion, power-of-two denominator)
- Floor and ceiling functions (also: integer part, round down, round up, floor, ceiling)
- Binomial coefficient (also: n choose k, binomial, binom(n,k))
- Finite sets, subsets and intersections (also: subset, intersection, intersection size, indicator vector, characteristic vector, k-element subset)
- Bijection and permutation (also: one-to-one correspondence, bijective function, permutation map, permutation of a set)
- Cartesian product (also: product set, direct product, product of index sets)
- Lexicographic order (also: lex order, dictionary order, row-major order)
- Logarithm and exponential function (also: lg, log base 2, natural logarithm, ln, exp, e^x)
- Limits (also: limit of a sequence, limit of a function, lim, tends to, approaches)
- Convergence of sequences and series (also: convergent sequence, convergent series, divergence, partial sums, sum of an infinite series, convergence)
- Basic integrals (also: definite integral, indefinite integral, antiderivative, Riemann integral, fundamental theorem of calculus, integration by substitution)
- Geometric series (also: geometric sum, sum of powers)
- Big-Omega, big-Theta and little-o notation (also: Omega notation, Theta notation, o-notation, asymptotic lower bound, tight bound, asymptotic equivalence)
- Worst-case running time of a Turing machine (also: time complexity, step count, worst-case time, running time)
- Recurrence relation (also: recurrence, divide-and-conquer recurrence, unrolling, T(n) recurrence)
- Schoolbook multiplication (also: grade-school multiplication, long multiplication, naive multiplication)
- Directed graph (also: digraph, vertex, edge, head and tail, directed acyclic graph, DAG, node)
- Vector space, subspace, basis and dimension (also: linear space, subspace, span, linearly independent, basis, direct sum, dimension)
- Linear map and matrix (also: linear transformation, matrix, invertible matrix, nonsingular matrix, transpose, identity matrix, diagonal matrix)
- Matrix rank (also: column rank, row rank, rational rank, rank over a field)
- Gaussian elimination and triangular matrices (also: row reduction, elementary row operations, echelon form, lower triangular matrix, upper triangular matrix)
- Dot product and orthogonal complement (also: standard inner product, scalar product, orthogonal complement, perpendicular space, U perp)
- Vector norm and maximum norm (also: norm, maximum norm, sup norm, infinity norm, max norm, triangle inequality)
- Complex conjugate, modulus and polar form (also: conjugate, modulus, absolute value of a complex number, argument, unit circle, Euler's formula, polar form)
- Source, sink and terminal of a network (also: terminal, source and sink of the network)

## This page

Concept: Tensor product
Gloss: The tensor product V ⊗ W of vector spaces is the space spanned by pairs of basis vectors, and the tensor product of linear maps acts on each factor separately, so one-dimensional operations on several coordinates combine into one operation on the product space.

## Where the argument relies on this page

- Each prime-length Fourier transform is expressed through a tensor transform with power-of-two axis lengths, keeping the source and target permutations inside the identity. (on [Gaussian resampling](gaussian-resampling.md))
- Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input length in bits), bound on [Fixed-tape machine model](fixed-tape-model.md): The count of bits in each input of the machine, the length in bits of each input.
- $\kappa$ (fixed exponent saving), bound on [Fixed-tape machine model](fixed-tape-model.md): A fixed constant equal to $2^{-182}$, the same for every input length $n$.
- $n$ (input length), bound on [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md): The number of bits in each of the two integers being multiplied, which is the length the worst-case time is measured against.
- $\kappa$ (power-saving constant), bound on [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md): A fixed constant greater than 0 that does not depend on $n$.
- $z$ (Gaussian dyadic number), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): A complex number whose real and imaginary parts are both dyadic rationals.
- $a$ (real part), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The real part of the Gaussian dyadic number $z$.
- $b$ (imaginary part), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The imaginary part of the Gaussian dyadic number $z$.
- $m$ (integer numerator), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The integer numerator of a dyadic rational written as $m/2^k$.
- $k$ (power-of-two exponent), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The exponent of the power of two in the denominator of a dyadic rational $m/2^k$.
- $\mathcal{G}$ (Gaussian dyadic set), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The set of all Gaussian dyadic numbers.
- $H_0$ (butterfly map), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The two-point map sending a pair $u, v$ to $((u+v)/2, (u-v)/2)$.
- $u$ (first input value), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The first value of an input pair to the butterfly map $H_0$.
- $v$ (second input value), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The second value of an input pair to the butterfly map $H_0$.
- $p$ (fractional bit count), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The number of fractional bits in a stored coefficient, so each stored part is a multiple of $2^{-p}$.
- $x$ (first bank value), bound on [Linear network](linear-network.md): The value of the first bank, held on one wire.
- $y$ (second bank value), bound on [Linear network](linear-network.md): The value of the second bank, held on one wire.
- $W$ (number of roles), bound on [Role streams from a cyclic row split](role-streams.md): The number of roles, the fixed wire places of the network.
- $i$ (row index), bound on [Role streams from a cyclic row split](role-streams.md): The position of a row among the rows that share its prefix, counted from 0.
- $R$ (padded row count), bound on [Role streams from a cyclic row split](role-streams.md): The number of rows of one prefix after padding, a multiple of W.
- $V$ (node volume), bound on [Role streams from a cyclic row split](role-streams.md): The number of bits the node holds once its rows are padded.
- $h$ (ground set size), bound on [Subset-intersection finite network](subset-network.md): The number of elements of the ground set $[h]$.
- $\mathcal{T}$ (triple family), bound on [Subset-intersection finite network](subset-network.md): The set of all three-element subsets of the ground set.
- $S$ (triple), bound on [Subset-intersection finite network](subset-network.md): A three-element subset of the ground set, one element of the triple family.
- $T$ (triple), bound on [Subset-intersection finite network](subset-network.md): A three-element subset of the ground set, one element of the triple family.
- $X$ (first bank), bound on [Subset-intersection finite network](subset-network.md): The bank of scalars $x_S$, one for each triple $S$.
- $Y$ (second bank), bound on [Subset-intersection finite network](subset-network.md): The bank of scalars $y_S$, one for each triple $S$.
- $g$ (ground element), bound on [Subset-intersection finite network](subset-network.md): An element of the ground set, indexing one central wire.
- $A_{ST}$ (side wire), bound on [Subset-intersection finite network](subset-network.md): The scratch wire attached to an ordered neighbouring pair of triples.
- $C_g$ (central wire), bound on [Subset-intersection finite network](subset-network.md): The scratch wire attached to ground element $g$.
- $C_\ast$ (extra central wire), bound on [Subset-intersection finite network](subset-network.md): The additional scratch wire used only in the complex version.
- $u$ (tail vertex), bound on [Frame of a vertex](frame.md): A vertex of the network, the start of an edge from u to v.
- $v$ (head vertex), bound on [Frame of a vertex](frame.md): A vertex of the network, the end of an edge from u to v.
- $D_v$ (frame of a vertex), bound on [Frame of a vertex](frame.md): The frame of vertex v, an invertible linear operator on the space of arrays indexed by the common address set.
- $g$ (logical array), bound on [Frame of a vertex](frame.md): The array on a wire at a vertex before the frame there is applied, so that the stored array is D_v g.
- $t$ (input count), bound on [Frame of a vertex](frame.md): The number of input arrays of a pointwise linear gate.
- $j$ (input index), bound on [Frame of a vertex](frame.md): The index of one input array of a gate, running from 1 to t.
- $c_j$ (input scalar), bound on [Frame of a vertex](frame.md): The fixed scalar multiplying the j-th input array of a pointwise linear gate.
- $G$ (pointwise linear gate), bound on [Frame of a vertex](frame.md): A gate whose output at every address is a fixed linear combination of its input arrays.
- $x$ (route vertex), bound on [Frame of a vertex](frame.md): The l-th vertex x_l of a route, running from the source x_0 to the sink x_r.
- $r$ (route length), bound on [Frame of a vertex](frame.md): The number of edges in a route, which is one less than the number of vertices on it.
- $l$ (edge index), bound on [Frame of a vertex](frame.md): The index of an edge of a route, running from 1 to r.
- $H$ (first address field), bound on [Address shear](address-shear.md): The first address field, a vector whose entries lie in the residue ring Z/qZ.
- $D$ (second address field), bound on [Address shear](address-shear.md): The second address field, a vector whose entries lie in the residue ring Z/qZ, which the shear leaves unchanged.
- $q$ (modulus), bound on [Address shear](address-shear.md): The fixed modulus q, whose residue ring Z/qZ contains the entries of H and D.
- $E$ (label space), bound on [Nested subspace labels](subspace-labels.md): The fixed space that contains every label, of dimension $m$.
- $m$ (label dimension), bound on [Nested subspace labels](subspace-labels.md): The dimension of the common space $E$, a count of the basis vectors of $E$; on the dyadic page $m$ means an integer numerator instead.
- $w$ (network vertex), bound on [Nested subspace labels](subspace-labels.md): A vertex of the network, a gate or a terminal, that carries a label.
- $L$ (vertex label), bound on [Nested subspace labels](subspace-labels.md): The label $L(w)$ of a vertex $w$, a subspace of $E$.
- $\sigma$ (tail vertex), bound on [Nested subspace labels](subspace-labels.md): The vertex at which an edge starts.
- $\tau$ (head vertex), bound on [Nested subspace labels](subspace-labels.md): The vertex at which an edge ends.
- $U$ (label subspace), bound on [Nested subspace labels](subspace-labels.md): A subspace of $E$ used as the label of a gate or sink.
- $P_U$ (label projection), bound on [Nested subspace labels](subspace-labels.md): The projection onto the subspace $U$ along its orthogonal complement $U^\perp$.
- $s$ (smaller-call total), bound on [Nested subspace labels](subspace-labels.md): The total number of smaller calls, the sum of the drops over all edges; the letter changes meaning here and is not the route length of the frame page.
- $e$ (network edge), bound on [Rank-saving recursion](recursive-saving.md): An edge of the network, the connection along which one vertex passes its values to another.
- $\operatorname{rk}(e)$ (edge rank), bound on [Rank-saving recursion](recursive-saving.md): The rank of the edge matrix of the edge $e$, which counts the smaller calls that edge costs.
- $s$ (smaller call count), bound on [Rank-saving recursion](recursive-saving.md): The total number of smaller calls, summed over all edges of the network.
- $u$ (field width), bound on [Fast interchange of address chunks](tape-interchange.md): The number of bits in each of the two address fields H and D.
- $V$ (stored volume), bound on [Fast interchange of address chunks](tape-interchange.md): The number of data units in the array being permuted.
- $\tau$ (saving exponent), bound on [Fast interchange of address chunks](tape-interchange.md): A fixed exponent below 1 that sets the saving in the cost per unit of width.
- $\mu$ (matrix row count), bound on [Fast interchange of address chunks](tape-interchange.md): The fixed number of rows of each vertex matrix, which is also its number of columns.
- $d$ (recursion depth), bound on [Fast interchange of address chunks](tape-interchange.md): The number of levels of recursion used to build an interchange of width $\mu^d$.
- $F_d$ (time per unit volume), bound on [Fast interchange of address chunks](tape-interchange.md): The time per unit volume of an interchange of width $\mu^d$, at recursion depth $d$.
- $\lambda$ (calls per stream), bound on [Fast interchange of address chunks](tape-interchange.md): The ratio $s/W$, the average number of smaller calls per wire stream.
- $\eta$ (relative deficit), bound on [Fast interchange of address chunks](tape-interchange.md): The relative deficit $(W\mu-s)/(W\mu)$ of the rank sum below $W\mu$.
- $x$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): The formal variable whose powers index the coefficients of a list.
- $S$ (list length), bound on [Cyclic convolution](cyclic-convolution.md): The number of coefficients in each list, which fixes the wraparound modulus.
- $i$ (first index), bound on [Cyclic convolution](cyclic-convolution.md): An index into the first list, running over 0 to S-1.
- $j$ (second index), bound on [Cyclic convolution](cyclic-convolution.md): An index into the second list, running over 0 to S-1.
- $k$ (output index), bound on [Cyclic convolution](cyclic-convolution.md): The index of an output coefficient c_k, running over 0 to S-1.
- $a$ (first coefficient list), bound on [Cyclic convolution](cyclic-convolution.md): The first input list, whose i-th coefficient is a_i.
- $b$ (second coefficient list), bound on [Cyclic convolution](cyclic-convolution.md): The second input list, whose j-th coefficient is b_j.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The cyclic convolution of a and b, a list of S coefficients.
- $\beta$ (digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each radix digit.
- $b$ (exact-recovery digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The same digit width as $\beta$ on this page, the number of bits in each radix digit.
- $m$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of radix digits in each input, the ceiling of n divided by the digit width.
- $u_i$ (first input digit), bound on [Radix-digit convolution](radix-digit-convolution.md): The $i$-th radix digit of the first input.
- $v_i$ (second input digit), bound on [Radix-digit convolution](radix-digit-convolution.md): The $i$-th radix digit of the second input.
- $t$ (formal variable), bound on [Radix-digit convolution](radix-digit-convolution.md): The formal variable whose powers mark the coefficient positions of the digit polynomials.
- $U$ (first digit polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial whose coefficients are the radix digits of the first input.
- $V$ (second digit polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial whose coefficients are the radix digits of the second input.
- $W$ (product polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The product $U(t)V(t)$ of the two digit polynomials.
- $w_k$ (product coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The $k$-th coefficient of the product polynomial $W(t)$.
- $q$ (vector length), bound on [Discrete Fourier transform](fourier-transform.md): The number of entries of u, which is the length of every vector in the transform.
- $u$ (input vector), bound on [Discrete Fourier transform](fourier-transform.md): The complex vector of length q that the transform acts on; here u is not the first input of earlier pages.
- $\omega$ (root of unity), bound on [Discrete Fourier transform](fourier-transform.md): The primitive q-th root of unity exp(-2 pi i/q) used by the transform.
- $\hat u$ (transform), bound on [Discrete Fourier transform](fourier-transform.md): The discrete Fourier transform of u, a vector of length q with entries indexed by k.
- $j$ (input index), bound on [Discrete Fourier transform](fourier-transform.md): The position of an entry of u, running from 0 to q-1 in the transform sum.
- $k$ (output index), bound on [Discrete Fourier transform](fourier-transform.md): The position of an entry of the transform, running from 0 to q-1.
- $t$ (second summation index), bound on [Discrete Fourier transform](fourier-transform.md): The position of an entry of b, running from 0 to q-1 in the convolution sum.
- $l$ (output position), bound on [Discrete Fourier transform](fourier-transform.md): The position of an entry of the cyclic convolution c, running from 0 to q-1.
- $N$ (operation count), bound on [Discrete Fourier transform](fourier-transform.md): The number of operations the FFT uses on a vector of length q.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](fourier-transform.md): The map sending a vector u of length q to the vector whose k-th entry is (1/q) times the sum over j of u_j times exp(−2πijk/q).
  Shown as: Tensor product *<predicate>* Discrete Fourier transform

## Pages that build on this one

- Multidimensional transform with power-of-two axes: A transform on an array indexed by several coordinates, each with length a power of two, obtained as a tensor product of one-dimensional Fourier transforms.
- Simultaneous butterfly layer H₀: The map H₀(u,v) = ((u+v)/2, (u−v)/2) applied at once to a selected coordinate bit of every chunk, a two-point butterfly acting coefficientwise on polynomial records.

## Other pages you may link to

- [Fixed-tape machine model](fixed-tape-model.md)
- [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Power saving in the logarithmic factor](power-saving.md)
- [Gaussian dyadic numbers](gaussian-dyadic.md)
- [Linear network](linear-network.md)
- [Role streams from a cyclic row split](role-streams.md)
- [Subset-intersection finite network](subset-network.md)
- [Established fast multiplier](multiplier-subroutine.md)
- [Source, sink and terminal of a network](network-terminal.md)
- [Frame of a vertex](frame.md)
- [Address shear](address-shear.md)
- [Nested subspace labels](subspace-labels.md)
- [Rank-saving recursion](recursive-saving.md)
- [Fast interchange of address chunks](tape-interchange.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Multidimensional transform with power-of-two axes](multidim-transform.md)
- [Simultaneous butterfly layer H₀](butterfly-layer.md)
- [Order of an element](order-of-element.md)
- [Root of unity](roots-of-unity.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Signed coefficient packing](signed-packing.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Operator norm of a linear map](operator-norm.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein.md)
- [Quotient ring by several relations](quotient-ring.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "An empty tensor product is the one-dimensional ground field" (paper)

  > At stage $j$, fix an invocation. Put \[ A=F^{\otimes(j-1)},\qquad P=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle, \qquad B=P^\perp\subset A. \] An empty tensor product is the one-dimensional ground field; thus $B=0$ at stage 1. Let $Q=\langle t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}\rangle \subset F^{\otimes(3-j)}$, again using the empty tensor product at stage 3. Since $P$ is nondegenerate, $A=B\mathbin{\perp}P$. We prescribe the following transition for each data wire in the stage, where $t$ is the indicator of that wire's $j$th triple: \[ \begin{array}{c|c|c} &\text{incoming label}&\text{outgoing label}\\ \hline X&A\otimes\langle t\rangle\otimes Q&(A\otimes F)\otimes Q\\ Y&B\otimes\langle t\rangle\otimes Q& \bigl((B\otimes F)\mathbin{\perp}(P\otimes t^\perp)\bigr)\otimes Q. \end{array} \] The outgoing $Y$ label can also be written $(P\otimes\langle t\rangle)^\perp_{A\otimes F}\otimes Q$. These transi

- "The intended operation is the tensor product" (paper)

  > We now apply the complex network to a common butterfly layer on several axes. The array has complete address set \[ [P]\times[2^K]^D\times[S],\qquad 1\le D\le d, \] with $P,S\ge1$, in lexicographic order. Its $D$ consecutive $K$-bit chunks each select the bit at one common offset $0\le\rho<K$, counted from the least significant end. Each address carries a polynomial record with $r$ complex coefficients, initially in the unit disk on the grid $2^{-p}\mathbb Z[i]$, with $\Theta(p)$ bits per real or imaginary component. The intended operation is the tensor product of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on the $D$ selected bits, acting coefficientwise and preserving all other address fields.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $A$ means linear map on E here, but input array on [Multidimensional transform with power-of-two axes](multidim-transform.md), which builds on this page: Use another letter (for example L) for the linear map on E, so A keeps its meaning as the input array of the multidimensional transform.
- $p$ means basis size of E here, but integer precision on [Gaussian resampling](gaussian-resampling.md), which builds on this page: Use another letter (for example n) for the basis size of E; p is the integer precision in the gaussian-resampling identity.

## Previous version (revise it)

It has 296 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 370 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The tensor product of two vector spaces is spanned by pairs of basis vectors, one from each factor. It turns one operation per factor into one linear map.

Let $E$ and $F$ be vector spaces over $\mathbb{C}$. Every $e\in E$ is a general vector of $E$, and every $f\in F$ a general vector of $F$. Let $e_1,\dots,e_p$ be a basis of $E$ and $f_1,\dots,f_q$ a basis of $F$, where $e_i$ is the $i$th basis vector of $E$, $f_j$ the $j$th of $F$, $p$ and $q$ are the numbers of basis vectors, and $1\le i\le p$, $1\le j\le q$.

A concrete model of $E\otimes F$ is the space of $p\times q$ complex arrays, where $e_i\otimes f_j$ has a single $1$ in row $i$, column $j$. These $pq$ arrays form a basis. Every $e$ is a unique combination of the $e_i$, and every $f$ of the $f_j$, so $e\otimes f$ has entry $(i,j)$ equal to the coefficient of $e$ on $e_i$ times the coefficient of $f$ on $f_j$. This product is bilinear: it is linear in each factor.

Let $A$ be a linear map of $E$ and $T$ of $F$. Define $A\otimes T$ on the basis by $(A\otimes T)(e_i\otimes f_j)=Ae_i\otimes Tf_j$. A linear map is fixed by its values on a basis, so this defines exactly one map. Bilinearity then gives $(A\otimes T)(e\otimes f)=Ae\otimes Tf$ for all $e\in E$ and $f\in F$.

For example, take $E=F=\mathbb{C}^2$, with standard bases $e_1,e_2$, and let $A=T$ satisfy $Ae_1=e_1+e_2$ and $Ae_2=e_1-e_2$. Then
$$(A\otimes T)(e_1\otimes e_2)=(e_1+e_2)\otimes(e_1-e_2)=e_1\otimes e_1-e_1\otimes e_2+e_2\otimes e_1-e_2\otimes e_2,$$
where the last step uses bilinearity. Two maps on two-dimensional spaces are now one map on a four-dimensional space.

Here $D$ counts the selected bits, not the address field $D$. With the other bits fixed, a selected bit carries a pair $(u,v)$ in $\mathbb{C}^2$. The butterfly $H_0$ is the $2\times 2$ matrix $\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ acting on column vectors $\begin{pmatrix}u\\v\end{pmatrix}$. Applying $H_0$ to every selected bit at once is the single linear map $H_0\otimes\cdots\otimes H_0$ with $D$ factors, rather than $D$ separate passes. <cite data-source="paper">The intended operation is the tensor product of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on the $D$ selected bits</cite>.

The tensor product of one-dimensional transforms is built from one [Discrete Fourier transform](fourier-transform.md) per axis. [Gaussian resampling](gaussian-resampling.md) uses this to express each source Fourier transform as a power-of-two tensor transform.

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
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

Write the body to `exegenius/tasks/0228-write-tensor-product.answer.md` and the JSON to `exegenius/tasks/0228-write-tensor-product.answer.json`, then run `exegenius submit 0228-write-tensor-product` in the project directory. If submit rejects the answer, fix the answer and submit again.
