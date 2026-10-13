# exegenius task 0211-write-gaussian-resampling

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
- Simultaneous butterfly layer H₀ (also: H_0 layer)
- Polynomial ring modulo yʳ + 1 (also: C[y]/(y^r+1), reduced polynomial)
  - $y$ (polynomial variable): The formal variable whose powers act as roots of unity on the remaining axes.
  - $r$ (coefficient count): The number of complex coefficients in each polynomial record, which is a power of two.
- Root of unity (also: primitive root of unity)
- Synthetic polynomial transform (also: synthetic transform, polynomial transform, twiddle multiplication, transform method)
- Discrete Fourier transform (also: Fourier transform, twiddle step)
- Multidimensional transform with power-of-two axes (also: power-of-two tensor transform)
- Cyclic convolution (also: convolution modulo x^S - 1, normalized cyclic convolution)
- Radix-digit convolution (also: radix-2^b digit polynomials)
- Signed coefficient packing (also: Kronecker substitution)
- Established fast multiplier (also: Harvey-van der Hoeven multiplier)
- Exact recovery by rounding and carries (also: carry propagation)
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
- Tensor product
- Operator norm of a linear map
- Order of an element
- Source, sink and terminal of a network (also: terminal, source and sink of the network)

## This page

Concept: Gaussian resampling
Gloss: A rewriting of a Fourier transform of prime length as a transform with power-of-two axis lengths, with source and target coordinate permutations kept inside the transform identity.
Also called: Gaussian gridding, target permutation

## This page in the argument

The step: Each prime-length Fourier transform is expressed through a tensor transform with power-of-two axis lengths, keeping the source and target permutations inside the identity.
How: Gaussian resampling, computing the transform formula directly with both permutations retained
Why: The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two; Gaussian resampling connects these two shapes. (the sources say so: "The transform lengths needed for the integer product are pairwise coprime,
whereas the synthetic transforms use powers of two. Gaussian resampling
connects these two shapes." (paper))

Its sub-steps, in order:

- Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform.
- The source and target coordinate permutations stay inside the transform identity, so they need not be executed as separate sorts.

It serves these steps, from the main result down:

- The integer product is computed exactly on one fixed-tape machine in $O(n(\lg n)^{1-\kappa})$ worst-case time, for $\kappa=2^{-182}$.; how: reduce exact multiplication to convolution of radix digits on distinct prime axes, compute the convolution by synthetic transforms on tape layouts, and bound the total tape cost with a power saving (on [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md))

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
- $\mathcal T$ (triple set), bound on [Subset-intersection finite network](subset-network.md): The set of all three-element subsets of $[h]$.
- $S$ (triple), bound on [Subset-intersection finite network](subset-network.md): A three-element subset of $[h]$, one element of $\mathcal T$.
- $T$ (second triple), bound on [Subset-intersection finite network](subset-network.md): A three-element subset of $[h]$ indexing the same families as $S$, one element of $\mathcal T$.
- $X$ (first bank), bound on [Subset-intersection finite network](subset-network.md): The bank holding the scalar $x_S$ for each triple $S$.
- $Y$ (second bank), bound on [Subset-intersection finite network](subset-network.md): The bank holding the scalar $y_S$ for each triple $S$.
- $A_{ST}$ (side wire), bound on [Subset-intersection finite network](subset-network.md): The scratch wire for an ordered neighbouring pair $(S,T)$, which copy fills with $x_T$.
- $g$ (ground element), bound on [Subset-intersection finite network](subset-network.md): An element of the ground set $[h]$, whose central wire gathers the $x_T$ with $g\in T$.
- $C_g$ (central wire), bound on [Subset-intersection finite network](subset-network.md): The scratch wire of the element $g$ of $[h]$, which gather fills with the $x_T$ for triples $T$ containing $g$.
- $C_\ast$ (total wire), bound on [Subset-intersection finite network](subset-network.md): The extra scratch wire of the complex version, which gather fills with the sum of all $x_T$.
- $D_v$ (frame of a vertex), bound on [Frame of a vertex](frame.md): The frame of vertex $v$, the invertible linear operator that sets how arrays at $v$ are stored.
- $g$ (logical array), bound on [Frame of a vertex](frame.md): The logical array on a wire at a vertex, before the frame is applied to it.
- $u$ (tail vertex), bound on [Frame of a vertex](frame.md): The vertex at which an edge starts, so that the frame change $D_vD_u^{-1}$ starts from its frame $D_u$.
- $v$ (head vertex), bound on [Frame of a vertex](frame.md): The vertex at which an edge ends, whose frame $D_v$ gives the stored form after the change.
- $G$ (pointwise linear gate), bound on [Frame of a vertex](frame.md): A gate that outputs a fixed linear combination of its input arrays at every address.
- $t$ (input count), bound on [Frame of a vertex](frame.md): The number of input arrays of a pointwise linear gate.
- $j$ (input index), bound on [Frame of a vertex](frame.md): The position of an input array of a gate, counted from 1.
- $c_j$ (gate coefficient), bound on [Frame of a vertex](frame.md): The fixed scalar by which a gate multiplies its input array $g_j$.
- $x_l$ (route vertex), bound on [Frame of a vertex](frame.md): The vertex at position $l$ on a route, where $x_0$ is the source and $x_s$ is the sink.
- $s$ (route length), bound on [Frame of a vertex](frame.md): The number of edges in a route, so that the route has $s+1$ vertices.
- $l$ (edge index), bound on [Frame of a vertex](frame.md): The position of an edge along a route, counted from 1.
- $H$ (first address field), bound on [Address shear](address-shear.md): The first address field, a vector whose entries lie in the residue ring Z/qZ.
- $D$ (second address field), bound on [Address shear](address-shear.md): The second address field, a vector whose entries lie in the residue ring Z/qZ, which the shear leaves unchanged.
- $q$ (modulus), bound on [Address shear](address-shear.md): The fixed modulus q, whose residue ring Z/qZ contains the entries of H and D.
- $E$ (label space), bound on [Nested subspace labels](subspace-labels.md): The fixed space that every label is a subspace of.
- $m$ (space dimension), bound on [Nested subspace labels](subspace-labels.md): The dimension of the space E, which counts the basis vectors of E.
- $x$ (tail vertex), bound on [Nested subspace labels](subspace-labels.md): A vertex of the network, a gate or terminal; it is the tail of an edge from x to y.
- $y$ (head vertex), bound on [Nested subspace labels](subspace-labels.md): A vertex at the head of the edge from x, the vertex the edge enters.
- $L$ (vertex label), bound on [Nested subspace labels](subspace-labels.md): The subspace of E attached to a vertex x, written L(x).
- $U$ (label subspace), bound on [Nested subspace labels](subspace-labels.md): A subspace of E serving as the label of a gate or sink.
- $P_U$ (label projection), bound on [Nested subspace labels](subspace-labels.md): The projection onto the subspace U along its orthogonal complement.
- $s$ (smaller call count), bound on [Nested subspace labels](subspace-labels.md): The total number of smaller calls, which counts the smaller operations over all edges.
- $a$ (edge rank), bound on [Rank-saving recursion](recursive-saving.md): The rank of one edge matrix, which is summed over all edges to give the total number of smaller calls.
- $s$ (smaller call count), bound on [Rank-saving recursion](recursive-saving.md): The total number of smaller calls, counted as the sum of the edge ranks over all edges.
- $u$ (field width), bound on [Fast interchange of address chunks](tape-interchange.md): The number of bits in each of the two address fields, their common width.
- $V$ (stored volume), bound on [Fast interchange of address chunks](tape-interchange.md): The number of data units in the array, the stored volume.
- $\tau$ (saving exponent), bound on [Fast interchange of address chunks](tape-interchange.md): A fixed number below 1 that sets the size of the saving in the cost bound.
- $m$ (matrix size), bound on [Fast interchange of address chunks](tape-interchange.md): The number of rows of each rational matrix held at a vertex of the network, and the parameter of the recursion.
- $d$ (recursion depth), bound on [Fast interchange of address chunks](tape-interchange.md): The number of levels of recursion below the top call, so that the width of the interchange is m^d.
- $F_d$ (time per unit volume), bound on [Fast interchange of address chunks](tape-interchange.md): The time per unit of stored volume of an interchange of width m^d at recursion depth d.
- $\lambda$ (calls per stream ratio), bound on [Fast interchange of address chunks](tape-interchange.md): The ratio s/W of the total number of smaller calls to the number of wire streams.
- $\eta$ (relative rank deficit), bound on [Fast interchange of address chunks](tape-interchange.md): The fraction of the bound Wm by which the total rank s falls short, so that s/W = m(1 - eta).
- $x$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): The formal variable whose powers index the coefficients of a list.
- $S$ (list length), bound on [Cyclic convolution](cyclic-convolution.md): The number of coefficients in each list, which fixes the wraparound modulus.
- $i$ (first index), bound on [Cyclic convolution](cyclic-convolution.md): An index into the first list, running over 0 to S-1.
- $j$ (second index), bound on [Cyclic convolution](cyclic-convolution.md): An index into the second list, running over 0 to S-1.
- $k$ (output index), bound on [Cyclic convolution](cyclic-convolution.md): The index of an output coefficient c_k, running over 0 to S-1.
- $a$ (first coefficient list), bound on [Cyclic convolution](cyclic-convolution.md): The first input list, whose i-th coefficient is a_i.
- $b$ (second coefficient list), bound on [Cyclic convolution](cyclic-convolution.md): The second input list, whose j-th coefficient is b_j.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The cyclic convolution of a and b, a list of S coefficients.
- $b$ (digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each radix digit.
- $m$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of radix digits in each input, $\lceil n/b \rceil$.
- $u_i$ (first input digit), bound on [Radix-digit convolution](radix-digit-convolution.md): The $i$-th radix digit of the first input, an integer in $\{0,\dots,2^b-1\}$.
- $v_i$ (second input digit), bound on [Radix-digit convolution](radix-digit-convolution.md): The $i$-th radix digit of the second input, an integer in $\{0,\dots,2^b-1\}$.
- $t$ (formal variable), bound on [Radix-digit convolution](radix-digit-convolution.md): A formal variable whose powers mark the coefficient positions of the digit polynomials.
- $U$ (first digit polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial $U(t)$ whose coefficients are the digits of the first input.
- $V$ (second digit polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial $V(t)$ whose coefficients are the digits of the second input.
- $W$ (product polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The product $U(t)V(t)$, whose value at $t = 2^b$ is the integer product of the inputs.
- $w_k$ (product coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The $k$-th coefficient of $W$, the sum of $u_i v_j$ over $i+j=k$.
- $u$ (input vector), bound on [Discrete Fourier transform](fourier-transform.md): A complex vector of length q, the input of the transform.
- $q$ (transform length), bound on [Discrete Fourier transform](fourier-transform.md): The number of entries of u, which is the length of the transform.
- $\omega$ (root of unity), bound on [Discrete Fourier transform](fourier-transform.md): The primitive q-th root of unity exp(-2 pi i/q), whose q-th power is 1 and whose smaller positive powers are not 1.
- $\hat u$ (transform of u), bound on [Discrete Fourier transform](fourier-transform.md): The vector of Fourier coefficients of u, with entries given by the transform formula.
- $j$ (input index), bound on [Discrete Fourier transform](fourier-transform.md): An index running over the entries of u, from 0 to q-1.
- $k$ (output index), bound on [Discrete Fourier transform](fourier-transform.md): An index running over the entries of the transform, from 0 to q-1.
- $a$ (first vector), bound on [Discrete Fourier transform](fourier-transform.md): A vector of length q, the first input of the convolution.
- $b$ (second vector), bound on [Discrete Fourier transform](fourier-transform.md): A vector of length q, the second input of the convolution.
- $c$ (cyclic product), bound on [Discrete Fourier transform](fourier-transform.md): The cyclic convolution of a and b, a vector of length q.
- $l$ (convolution index), bound on [Discrete Fourier transform](fourier-transform.md): An index running over the entries of the cyclic product c, from 0 to q-1.
- $r$ (summation index), bound on [Discrete Fourier transform](fourier-transform.md): A second summation index running over the entries of b, from 0 to q-1.
- $\hat a$ (transform of a), bound on [Discrete Fourier transform](fourier-transform.md): The transform of a, defined by the transform formula.
- $\hat b$ (transform of b), bound on [Discrete Fourier transform](fourier-transform.md): The transform of b, defined by the transform formula.
- $\hat c$ (transform of c), bound on [Discrete Fourier transform](fourier-transform.md): The transform of c, defined by the transform formula.
- $N$ (operation count), bound on [Discrete Fourier transform](fourier-transform.md): The number of operations the FFT uses on a vector of length q.
- $E$ (first space), bound on [Tensor product](tensor-product.md): The vector space $E$ over $\mathbb{C}$.
- $F$ (second space), bound on [Tensor product](tensor-product.md): The vector space $F$ over $\mathbb{C}$.
- $e$ (general vector of E), bound on [Tensor product](tensor-product.md): A general vector of $E$.
- $f$ (general vector of F), bound on [Tensor product](tensor-product.md): A general vector of $F$.
- $e_i$ (basis vector of E), bound on [Tensor product](tensor-product.md): The $i$th basis vector of $E$.
- $f_j$ (basis vector of F), bound on [Tensor product](tensor-product.md): The $j$th basis vector of $F$.
- $p$ (basis count of E), bound on [Tensor product](tensor-product.md): The number of basis vectors of $E$, its dimension.
- $q$ (basis count of F), bound on [Tensor product](tensor-product.md): The number of basis vectors of $F$, its dimension.
- $i$ (basis index of E), bound on [Tensor product](tensor-product.md): The index of a basis vector $e_i$, running from $1$ to $p$.
- $j$ (basis index of F), bound on [Tensor product](tensor-product.md): The index of a basis vector $f_j$, running from $1$ to $q$.
- $S$ (map on E), bound on [Tensor product](tensor-product.md): A linear map of $E$.
- $T$ (map on F), bound on [Tensor product](tensor-product.md): A linear map of $F$.
- $D$ (selected-bit count), bound on [Tensor product](tensor-product.md): The number of selected address bits that the layer acts on.
- $H_0$ (butterfly), bound on [Tensor product](tensor-product.md): The two-point butterfly map, given by a $2\times 2$ matrix on $(u,v)$.
- $d$ (number of axes), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The number of axes of the array, which counts the coordinates each entry is indexed by.
- $\ell$ (axis index), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The index of an axis, running from 1 to d.
- $r_\ell$ (axis length), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): A power of two, the number of entries along axis ℓ.
- $j_\ell$ (input index), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The input index along axis ℓ, running over 0 to r_ℓ − 1.
- $k_\ell$ (output index), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The output index along axis ℓ, running over 0 to r_ℓ − 1.
- $A$ (input array), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The array to be transformed, with entries A indexed by one input index per axis.
- $B$ (transformed array), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The result of the transform, with entries B indexed by one output index per axis.
- $H_0$ (simultaneous butterfly layer), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The map applied at once to one selected bit of each of d chunks, acting as a two-point butterfly on each selected bit.
- $d$ (chunk count), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The number of equal-width chunks, each with one selected bit, on which the layer acts.
- $r$ (record length), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The number of complex coefficients in each polynomial record stored at an address.
- $e$ (chunk length), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The number of positions in each of the two chunks being interchanged.
- $\lambda'$ (layer cost exponent), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): A fixed exponent below 1 that sets the power of d in the cost bound of the layer.
- $\gamma$ (element), bound on [Order of an element](order-of-element.md): An element of the group whose order is taken; in the argument, the product $\prod_\eta y_\eta^{\mu_\eta}$.
- $N$ (order), bound on [Order of an element](order-of-element.md): The least positive integer with $\gamma^N=1$, which counts the distinct powers of $\gamma$ before the identity repeats.
- $G$ (monomial group), bound on [Order of an element](order-of-element.md): The set of monomials of the target ring, which is a multiplicative group with $S$ elements.
- $\nu$ (number of lengths), bound on [Order of an element](order-of-element.md): The number of pairwise coprime lengths $s_1,\dots,s_\nu$ of the source, a count.
- $s_\eta$ (length), bound on [Order of an element](order-of-element.md): The $\eta$-th of the pairwise coprime lengths, a positive integer.
- $\mu_\eta$ (inverse of prefix product), bound on [Order of an element](order-of-element.md): The inverse, modulo $s_\eta$, of the product of the earlier lengths; it is coprime to $s_\eta$.
- $y_\eta$ (target variable), bound on [Order of an element](order-of-element.md): The $\eta$-th variable of the ring of the target monomials.
- $\theta_\eta$ (monomial exponent), bound on [Order of an element](order-of-element.md): The exponent of $y_\eta$ in a monomial of $G$, lying between $0$ and $s_\eta-1$.
- $\rho$ (exponent), bound on [Order of an element](order-of-element.md): A positive integer exponent of $\gamma$.
- $y$ (polynomial variable), bound on [Root of unity](roots-of-unity.md): The formal variable of the polynomial ring modulo y^r+1, whose powers are the roots used here.
- $r$ (reduced length), bound on [Root of unity](roots-of-unity.md): The number of complex coefficients of a reduced polynomial, a power of two.
- $\zeta$ (root of unity), bound on [Root of unity](roots-of-unity.md): The primitive q-th root of unity y^(2r/q) in the polynomial ring, for a power of two q dividing 2r.
- $p$ (exponent of y), bound on [Root of unity](roots-of-unity.md): The exponent with 0 <= p < r such that a power of y equals plus or minus y^p.
- $y$ (polynomial variable), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The formal variable of the ring, whose powers act as roots of unity on the remaining axes.
- $r$ (coefficient count), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The number of complex coefficients in each polynomial record, which is a power of two.
- $i$ (coefficient position), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The position of a coefficient in a coefficient list, running from 0 to r-1.
- $a_i$ (coefficient), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The complex coefficient of y^i in an element of the ring.
- $k$ (shift count), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The number of places a coefficient is shifted when the element is multiplied by y^k, with 0 \le k < r.
- $\mu$ (twiddle exponent), bound on [Synthetic polynomial transform](synthetic-transform.md): The exponent of the twiddle factor $y^\mu$, an integer from 0 to 2r-1.
- $\rho$ (primitive root of unity), bound on [Synthetic polynomial transform](synthetic-transform.md): A primitive $S$-th root of unity, the root by which the transform's powers are taken.
- $\xi$ (first input list), bound on [Synthetic polynomial transform](synthetic-transform.md): A list of $S$ coefficients, the first input whose transform is taken.
- $\eta$ (second input list), bound on [Synthetic polynomial transform](synthetic-transform.md): A list of $S$ coefficients, the second input of the convolution.
- $\hat\xi$ (transform of a list), bound on [Synthetic polynomial transform](synthetic-transform.md): The transform of the list $\xi$, whose $k$-th entry is $\hat\xi_k$.
- $\zeta$ (normalized cyclic product), bound on [Synthetic polynomial transform](synthetic-transform.md): The normalized cyclic convolution of $\xi$ and $\eta$, a list of $S$ coefficients.
- $L$ (layer count), bound on [Synthetic polynomial transform](synthetic-transform.md): The number of butterfly layers in the transform.
- $P$ (polynomial), bound on [Signed coefficient packing](signed-packing.md): The polynomial whose coefficients are packed into one integer.
- $M$ (coefficient count), bound on [Signed coefficient packing](signed-packing.md): The number of coefficients of $P$, which counts its slots in the packed integer.
- $\gamma_i$ (coefficient), bound on [Signed coefficient packing](signed-packing.md): The integer coefficient of $x^i$ in $P$.
- $\sigma$ (slot width), bound on [Signed coefficient packing](signed-packing.md): The number of bits each slot holds, so each coefficient occupies a slot of this many bits.
- $N_P$ (packed integer of P), bound on [Signed coefficient packing](signed-packing.md): The single integer that encodes the polynomial $P$ at bit offsets of $\sigma$ bits per coefficient.
- $Q$ (second polynomial), bound on [Signed coefficient packing](signed-packing.md): The second polynomial, whose product with $P$ is computed by one integer product.
- $N_Q$ (packed integer of Q), bound on [Signed coefficient packing](signed-packing.md): The single integer that encodes the polynomial $Q$ in the same way as $N_P$ encodes $P$.
- $z_k$ (computed coefficient value), bound on [Exact recovery by rounding and carries](exact-recovery.md): The computed Gaussian dyadic value that approximates the k-th coefficient w_k of W.
- $Q$ (exact product), bound on [Exact recovery by rounding and carries](exact-recovery.md): The exact integer product of the two n-bit inputs.
- $M$ (position count), bound on [Exact recovery by rounding and carries](exact-recovery.md): The number of radix-2^b positions over which the carries are propagated, a count of positions.
- $\sigma_k$ (carry into a position), bound on [Exact recovery by rounding and carries](exact-recovery.md): The carry added to the coefficient at position k, which is passed up from position k-1.
- $e_k$ (radix digit), bound on [Exact recovery by rounding and carries](exact-recovery.md): The k-th radix-2^b digit of the exact product, an integer in {0,...,2^b-1}.
- $\Phi$ (linear map), bound on [Operator norm of a linear map](operator-norm.md): A linear map from one finite-dimensional complex vector space to another, whose operator norm is taken.
- $\xi$ (input vector), bound on [Operator norm of a linear map](operator-norm.md): A vector in the domain of the linear map, over which the supremum defining the operator norm ranges.
- $\Psi$ (second linear map), bound on [Operator norm of a linear map](operator-norm.md): A linear map whose output can be fed into the linear map Φ, used in the composition bound.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](fourier-transform.md): The map sending a vector u of length q to the vector whose k-th entry is (1/q) times the sum over j of u_j times exp(−2πijk/q).
  Shown as: Gaussian resampling *<predicate>* Discrete Fourier transform
- [Multidimensional transform with power-of-two axes](multidim-transform.md): A transform on an array indexed by several coordinates, each with length a power of two, obtained as a tensor product of one-dimensional Fourier transforms.
  Shown as: Gaussian resampling *<predicate>* Multidimensional transform with power-of-two axes
- [Operator norm of a linear map](operator-norm.md): The operator norm of a linear map T is the largest factor by which T stretches a vector, the supremum of ‖Tv‖ over all vectors v with ‖v‖ ≤ 1, for a chosen vector norm.
  Shown as: Gaussian resampling *<predicate>* Operator norm of a linear map

## Pages that build on this one

- Bluestein's chirp identity: An identity writing a Fourier transform as a cyclic convolution sandwiched between pointwise multiplications by chirp sequences exp(−πi s j² / t).
- Fixed-tape integer multiplication with a power saving: A deterministic fixed-tape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1−κ)) worst-case time, for a fixed κ = 2^(−182), disproving the n log n optimality conjecture in this model.

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
- [Tensor product](tensor-product.md)
- [Simultaneous butterfly layer H₀](butterfly-layer.md)
- [Order of an element](order-of-element.md)
- [Root of unity](roots-of-unity.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Signed coefficient packing](signed-packing.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Bluestein's chirp identity](bluestein.md)
- [Quotient ring by several relations](quotient-ring.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "Gaussian resampling then expresses each source Fourier transform through a" (paper)

  > The remaining proof places these procedures inside the multiplication reduction and accounts for every change of representation. First, the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. Section~\ref{sec:assembly} implements this map through triangular controlled shifts and charged axis moves. Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform. Section~\ref{sec:resampling} retains the source and target coordinate permutations in the transform identity, so they need not be executed as separate full sorts.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The quotation does not support the claim it is attached to (unsupported): "The usual implementation sorts twice on each coordinate; the sources keep both permutations in the identity and" cites "compute that formula directly.": The quotation says to compute a formula directly; it does not mention sorting, permutations, or the identity map that the claim asserts. Say only what the source supports, or cite the passage that supports the claim.
- $N$ means near-identity map here, but operation count on [Discrete Fourier transform](fourier-transform.md), which this page builds on: Rename the near-identity map (for example to M), since N on the Fourier transform page is an operation count.

## Previous version (revise it)

It has 362 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 452 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Gaussian resampling rewrites a [Discrete Fourier transform](fourier-transform.md) of length $s$, the number of its coordinates, as a transform of a longer length $t$, keeping both coordinate permutations inside the transform identity. The integer product needs pairwise coprime transform lengths, while the synthetic transforms use powers of two; this rewriting joins the two.

Let $F_q$ be the normalized transform of length $q$: $(F_q u)_k=\frac1q\sum_{j=0}^{q-1}u_j e^{-2\pi i jk/q}$. The norm $\|u\|$ of a vector is its largest entry modulus. Gaussian resampling is measured by the [operator norm of a linear map](operator-norm.md), $\|L\|=\sup_{\|u\|\le1}\|Lu\|$, so a linear map $L$ is a *contraction* when $\|L\|\le1$.

Fix an integer width $\sigma\ge2$, the Gaussian width. Let $K$ and $M$ map $\mathbb C^s$ to $\mathbb C^t$ by
$$(Ku)_k=\frac1\sigma\sum_{j\in\mathbb Z}e^{-\pi\sigma^{-2}(j-sk/t)^2}u_j,\qquad (Mu)_k=\sum_{j\in\mathbb Z}e^{-\pi\sigma^{2}(tj/s-k)^2}u_j,$$
with $u_j$ read modulo $s$. Let $P_s$ and $P_t$ be the coordinate permutations $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$, with $v$ of length $t$ (here $v$ is new). Since $\gcd(s,t)=1$, both only rearrange coordinates. Harvey and van der Hoeven prove $MP_sF_s=P_tF_tK$ (their Theorem 4.2). The hypotheses are $p>100$, $2\le\sigma<\sqrt p$, $s<t<2^p$ and $\theta>p/\sigma^4$, where $p$ is the integer precision and $\theta=t/s-1$.

Let $\rho_j=\lfloor tj/s+\tfrac12\rfloor$ be the integer nearest $tj/s$, with ties rounded up. Let $\delta_j=tj/s-\rho_j$, so $|\delta_j|\le\tfrac12$. Let $\Lambda:\mathbb C^t\to\mathbb C^s$ select coordinate $\rho_j$, $(\Lambda v)_j=v_{\rho_j}$. Let $\Delta$ multiply entry $j$ by $e^{\pi\sigma^2\delta_j^2}$. Let $N=\Lambda M\Delta$ be the map from $\mathbb C^s$ to itself.

In $(Nu)_j$ the term with index $j$ is exactly $u_j$, because $e^{\pi\sigma^2\delta_j^2}$ cancels the Gaussian factor at $k=\rho_j$. The other terms form $((N-I)u)_j$, where $I$ is the identity map. Their size is bounded by $\|I-N\|<2^{-\sigma^2\theta}$, <cite data-source="paper">The exact Gaussian identity and inverse estimate proved in</cite> their Theorem 4.2 and Lemma 4.6.

Since $\sigma^2<p$ and $\theta>p/\sigma^4$, we get $\sigma^2\theta>p/\sigma^2>1$, so $\|I-N\|<\tfrac12$. The Neumann series $\sum_{m\ge0}(I-N)^m$ converges, since $\|(I-N)^m\|\le\|I-N\|^m$, by submultiplicativity of the operator norm. It inverts $N$, because $N$ times the partial sum $\sum_{m<M}(I-N)^m$ equals $I-(I-N)^M$, which tends to $I$. Hence $\|N^{-1}\|\le\frac1{1-\|I-N\|}<2$.

The norm of a diagonal map is its largest diagonal modulus, so $\|\Delta\|\le e^{\pi\sigma^2/4}\le2^{2\sigma^2-2}$ for $\sigma\ge2$. The map $\Lambda$ only copies coordinates, so $\|\Lambda\|\le1$.

Since $\Lambda M=N\Delta^{-1}$, the product $\Delta N^{-1}\Lambda M$ is the identity. Multiplying $MP_sF_s=P_tF_tK$ on the left by $\Delta N^{-1}\Lambda$ gives $P_sF_s=\Delta N^{-1}\Lambda P_tF_tK$. Put $A=\tfrac12K$ and $B=2^{1-2\sigma^2}\Delta N^{-1}\Lambda$. Then $P_sF_s=2^{2\sigma^2}BP_tF_tA$.

Both are contractions. The proof of Harvey and van der Hoeven's Proposition 4.7(i) gives $\|K\|<\tfrac32$, so $\|A\|<\tfrac34$. Also $\|B\|\le2^{1-2\sigma^2}\cdot2^{2\sigma^2-2}\cdot2\cdot1=1$.

The usual implementation sorts twice on each coordinate; the sources keep both permutations in the identity and <cite data-source="paper">compute that formula directly.</cite>

In the application $t=2^{\nu}$, where $\nu$ is a positive integer, so $F_t$ has power-of-two length. Thus Gaussian resampling expresses each source transform through a [Multidimensional transform with power-of-two axes](multidim-transform.md).

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

Write the body to `exegenius/tasks/0211-write-gaussian-resampling.answer.md` and the JSON to `exegenius/tasks/0211-write-gaussian-resampling.answer.json`, then run `exegenius submit 0211-write-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
