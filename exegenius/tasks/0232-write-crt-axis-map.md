# exegenius task 0232-write-crt-axis-map

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
- Gaussian resampling (also: Gaussian gridding, target permutation)
- Cyclic convolution (also: convolution modulo x^S - 1, normalized cyclic convolution)
- Bluestein's chirp identity (also: chirp identity)
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
- Quotient ring by several relations
- Source, sink and terminal of a network (also: terminal, source and sink of the network)

## This page

Concept: Chinese-remainder axis map
Gloss: The bijection sending a coefficient index written in mixed radix with pairwise coprime lengths to coordinates on a product of cyclic axes, which turns one cyclic convolution into a multidimensional one.
Also called: Chinese-remainder address map

## This page in the argument

The step: The radix-digit coefficient list is placed on distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.

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
- $E$ (first vector space), bound on [Tensor product](tensor-product.md): The first of the two vector spaces being tensored.
- $F$ (second vector space), bound on [Tensor product](tensor-product.md): The second of the two vector spaces being tensored.
- $e$ (general vector of E), bound on [Tensor product](tensor-product.md): A general vector of the space E.
- $f$ (general vector of F), bound on [Tensor product](tensor-product.md): A general vector of the space F.
- $e_i$ (basis vector of E), bound on [Tensor product](tensor-product.md): The i-th vector of a fixed basis of E.
- $f_j$ (basis vector of F), bound on [Tensor product](tensor-product.md): The j-th vector of a fixed basis of F.
- $p$ (basis size of E), bound on [Tensor product](tensor-product.md): The number of basis vectors of E, which counts the vectors e_1 through e_p.
- $q$ (basis size of F), bound on [Tensor product](tensor-product.md): The number of basis vectors of F, which counts the vectors f_1 through f_q.
- $i$ (basis index of E), bound on [Tensor product](tensor-product.md): An index of the basis vectors e_i of E, running from 1 to p.
- $j$ (basis index of F), bound on [Tensor product](tensor-product.md): An index of the basis vectors f_j of F, running from 1 to q.
- $A$ (linear map on E), bound on [Tensor product](tensor-product.md): A linear map of the space E, one factor of the tensor product of maps.
- $T$ (linear map on F), bound on [Tensor product](tensor-product.md): A linear map of the space F, the second factor of the tensor product of maps.
- $D$ (selected bit count), bound on [Tensor product](tensor-product.md): The number of selected bits on which the butterfly acts, one factor per bit.
- $d$ (number of axes), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The number of axes of the array, which counts the coordinates each entry is indexed by.
- $\ell$ (axis index), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The position of an axis, running from 1 to d.
- $r_\ell$ (axis length), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The number of entries along axis ℓ, a power of two.
- $j_\ell$ (input index), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The input index along axis ℓ, running over 0 to r_ℓ − 1.
- $k_\ell$ (output index), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The output index along axis ℓ, running over 0 to r_ℓ − 1.
- $A$ (input array), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The array whose entries A_{j_1…j_d} are the input to the transform.
- $B$ (transformed array), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The array whose entries B_{k_1…k_d} are the output of the transform.
- $B_d$ (simultaneous butterfly layer), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The map that applies the two-point butterfly $H_0$ to the selected bit of each of the $d$ chunks at once.
- $d$ (chunk count), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The number of address chunks the layer acts on, which counts the chunks, not the axes of the transform.
- $M$ (record length), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The number of complex coefficients in each polynomial record stored at an address.
- $\lambda'$ (layer exponent), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): A fixed exponent below 1 that sets the cost $O(Vd^{\lambda'})$ of the layer.
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
- $i$ (coefficient index), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The index of a coefficient, running from 0 to r-1.
- $a_i$ (coefficient), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The complex coefficient of y^i in the coefficient list of an element of the ring.
- $h$ (shift count), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The number of places a coefficient is shifted by multiplication with a power of y, with 0 <= h < r.
- $\sigma$ (twiddle exponent), bound on [Synthetic polynomial transform](synthetic-transform.md): The exponent of a twiddle factor $y^\sigma$, an integer from 0 to 2r-1 that counts the places a coefficient moves.
- $\theta$ (primitive root), bound on [Synthetic polynomial transform](synthetic-transform.md): A primitive $S$-th root of unity, the base root whose powers index the transform.
- $\xi$ (input list), bound on [Synthetic polynomial transform](synthetic-transform.md): A list of $S$ coefficients, the input of the transform and the first input of the convolution.
- $\eta$ (second input list), bound on [Synthetic polynomial transform](synthetic-transform.md): A second list of $S$ coefficients, the second input of the convolution.
- $\psi$ (normalized convolution), bound on [Synthetic polynomial transform](synthetic-transform.md): The normalized cyclic convolution of $\xi$ and $\eta$, a list of $S$ coefficients.
- $\hat\xi$ (transform of a list), bound on [Synthetic polynomial transform](synthetic-transform.md): The transform of a list $\xi$, with entries given by the transform formula with the root $\theta$.
- $\beta$ (layer count), bound on [Synthetic polynomial transform](synthetic-transform.md): The number of butterfly layers in the transform, which counts the layers applied in succession.
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
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the source transform, which is the number of its coordinates.
- $t$ (target length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the longer target transform, a count of its coordinates, with s < t.
- $p$ (integer precision), bound on [Gaussian resampling](gaussian-resampling.md): The integer precision in the hypotheses of the identity, a count of bits.
- $\sigma$ (Gaussian width), bound on [Gaussian resampling](gaussian-resampling.md): The integer width of the Gaussian factors, with sigma at least 2.
- $F_q$ (normalized transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized transform of length q, the map sending u to its transform with a factor 1/q.
- $K$ (first Gaussian map), bound on [Gaussian resampling](gaussian-resampling.md): The map from C^s to C^t given by the first Gaussian sum, with factor 1/sigma.
- $M$ (second Gaussian map), bound on [Gaussian resampling](gaussian-resampling.md): The map from C^s to C^t given by the second Gaussian sum, without a prefactor.
- $P_s$ (source permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation of length-s vectors sending u to the vector with entries u_{tj}.
- $P_t$ (target permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation of length-t vectors sending v to the vector with entries v_{-sk}.
- $v$ (target-length vector), bound on [Gaussian resampling](gaussian-resampling.md): A vector of length t, the argument of the target permutation P_t.
- $\theta$ (length excess ratio), bound on [Gaussian resampling](gaussian-resampling.md): The ratio t/s minus 1, by which the target length exceeds the source length.
- $\rho_j$ (nearest integer), bound on [Gaussian resampling](gaussian-resampling.md): The integer nearest tj/s, with ties rounded up, for each input index j.
- $\delta_j$ (rounding error), bound on [Gaussian resampling](gaussian-resampling.md): The difference tj/s minus rho_j, whose modulus is at most 1/2.
- $\Lambda$ (coordinate selection), bound on [Gaussian resampling](gaussian-resampling.md): The map from C^t to C^s that selects coordinate rho_j for each entry j.
- $\Delta$ (Gaussian diagonal), bound on [Gaussian resampling](gaussian-resampling.md): The diagonal map multiplying entry j by e^{pi sigma^2 delta_j^2}.
- $\Gamma$ (near-identity map), bound on [Gaussian resampling](gaussian-resampling.md): The map Lambda M Delta from C^s to itself, which is close to the identity.
- $I$ (identity map), bound on [Gaussian resampling](gaussian-resampling.md): The identity map, which leaves every vector unchanged.
- $J$ (partial sum length), bound on [Gaussian resampling](gaussian-resampling.md): The number of terms in a partial sum of the Neumann series, a count that tends to infinity.
- $\nu$ (power exponent), bound on [Gaussian resampling](gaussian-resampling.md): The positive integer exponent with t = 2 to the power nu.
- $A$ (first contraction), bound on [Gaussian resampling](gaussian-resampling.md): Half of K, one of the two contractions in the rewriting.
- $B$ (second contraction), bound on [Gaussian resampling](gaussian-resampling.md): The scaled map 2 to the power 1 minus 2 sigma squared times Delta Gamma inverse Lambda, the second contraction.
- $\chi_p$ (chirp value), bound on [Bluestein's chirp identity](bluestein.md): The chirp value $\exp(-\pi i p^2/q)$ at the integer $p$.
- $\tau_p$ (phase twist), bound on [Bluestein's chirp identity](bluestein.md): The phase twist $\exp(\pi i p/q)$ at the integer $p$, which satisfies $\tau_{p+q}=-\tau_p$.
- $\mu_j$ (first twisted sequence), bound on [Bluestein's chirp identity](bluestein.md): The $j$-th entry of the first twisted sequence, $u_j\chi_j\tau_j$.
- $\nu_p$ (second twisted sequence), bound on [Bluestein's chirp identity](bluestein.md): The $p$-th entry of the second twisted sequence, $\overline{\chi_p}\,\tau_p$.
- $p$ (chirp index), bound on [Bluestein's chirp identity](bluestein.md): An integer index at which the chirp and the phase twist are evaluated.
- $\mathcal{P}$ (polynomial ring), bound on [Quotient ring by several relations](quotient-ring.md): The ring of complex polynomials in the formal variables θ_1 to θ_M.
- $\theta$ (formal variable), bound on [Quotient ring by several relations](quotient-ring.md): A formal variable of the polynomial ring, indexed from 1 to M.
- $M$ (variable count), bound on [Quotient ring by several relations](quotient-ring.md): The number of formal variables θ_1 to θ_M.
- $f$ (relation), bound on [Quotient ring by several relations](quotient-ring.md): The i-th relation, a polynomial in the polynomial ring that is set to zero in the quotient.
- $K$ (relation count), bound on [Quotient ring by several relations](quotient-ring.md): The number of relations f_1 to f_K.
- $J$ (ideal of relations), bound on [Quotient ring by several relations](quotient-ring.md): The ideal generated by the relations, the set of all sums of the relations multiplied by polynomials.
- $\lambda$ (multiplier), bound on [Quotient ring by several relations](quotient-ring.md): The polynomial multiplier of the i-th relation in a sum that belongs to the ideal.
- $\phi$ (polynomial), bound on [Quotient ring by several relations](quotient-ring.md): A polynomial in the polynomial ring, identified with another when their difference lies in the ideal.
- $\psi$ (polynomial), bound on [Quotient ring by several relations](quotient-ring.md): A second polynomial in the polynomial ring, identified with another when their difference lies in the ideal.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Cyclic convolution](cyclic-convolution.md): The product of two coefficient lists in the ring of polynomials modulo x^S − 1, in which exponents wrap around modulo S.
  Shown as: Chinese-remainder axis map *<predicate>* Cyclic convolution
- [Quotient ring by several relations](quotient-ring.md): The quotient ring of a polynomial ring by several relations is the ring obtained by identifying two polynomials whenever their difference lies in the ideal generated by those relations.
  Shown as: Chinese-remainder axis map *<predicate>* Quotient ring by several relations

## Pages that build on this one

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
- [Radix-digit convolution](radix-digit-convolution.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Tensor product](tensor-product.md)
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
- [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "Agarwal and Cooley used the Chinese remainder" (paper)

  > To use the source tensor, we first place the ordinary coefficient stream in its tensor order. Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution~\cite{AgarwalCooley1977}. The following map uses that algebraic split, with coordinate powers that make the change of order a sequence of controlled cyclic shifts.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $\lambda$ means coefficient index here, but multiplier on [Quotient ring by several relations](quotient-ring.md), which this page builds on: On crt-axis-map, rename the coefficient index (for example κ), since lambda is the polynomial multiplier of the relations on quotient-ring.

## Previous version (revise it)

It has 409 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 511 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The Chinese-remainder axis map is a bijection that places the coefficients of a [Cyclic convolution](cyclic-convolution.md) on the axes of a product of cyclic rings, so that the convolution becomes multidimensional.

Let $d$ be the number of axes, with $\alpha$ and $\beta$ running from $1$ to $d$ as axis indices (not list positions), and let $s_\alpha$ be the length of axis $\alpha$, with $s_1,\ldots,s_d$ pairwise coprime. Let $S=s_1\cdots s_d$ be the number of coefficients, and let $x$ be the variable of $\mathbb C[x]/(x^S-1)$. Let $x_\alpha$ be the variable of axis $\alpha$, and let $\mathcal R=\mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1)$ be the target ring.

Let $P_\alpha=s_1\cdots s_{\alpha-1}$, so $P_1=1$. Since $P_\alpha$ is coprime to $s_\alpha$, it has an inverse $\mu_\alpha$ modulo $s_\alpha$, so $\mu_\alpha P_\alpha\equiv1\pmod{s_\alpha}$.

Let $\Phi$ be the algebra map (respecting sums, products and scalars) with $\Phi(x)=\prod_\alpha x_\alpha^{\mu_\alpha}$ that maps $\mathbb C[x]/(x^S-1)$ into the [Quotient ring by several relations](quotient-ring.md) $\mathcal R$. A map sending $x$ to an element $g$ of a ring kills $x^S-1$, and so descends to the quotient, exactly when $g^S=1$. Here $\Phi(x)^S=\prod_\alpha x_\alpha^{\mu_\alpha S}=1$, because each $s_\alpha$ divides $S$.

For a coefficient index $\lambda$ with $0\le\lambda<S$ (the position of a coefficient in the list), $\Phi(x^\lambda)=\prod_\alpha x_\alpha^{\mu_\alpha\lambda}$ is a monomial whose exponent on $x_\alpha$ is $b_\alpha$, where $0\le b_\alpha<s_\alpha$ and $b_\alpha\equiv\mu_\alpha\lambda\pmod{s_\alpha}$. The monomials $x_1^{e_1}\cdots x_d^{e_d}$ with $0\le e_\alpha<s_\alpha$ are a basis of $\mathcal R$, and there are $S$ of them. If $\lambda$ and $\lambda'$ (another index with $0\le\lambda'<S$) give the same $b_\alpha$ for every $\alpha$, then each $s_\alpha$ divides $\lambda-\lambda'$. The Chinese remainder theorem says that congruences with pairwise coprime moduli combine into one modulo their product, so $S\mid\lambda-\lambda'$ and $\lambda=\lambda'$. Thus the $S$ powers $\Phi(x)^0,\ldots,\Phi(x)^{S-1}$ reach $S$ distinct basis monomials, which are all of them. So $\Phi$ is a bijective algebra map, an isomorphism.

Because $\Phi$ is an isomorphism, it preserves [Cyclic convolution](cyclic-convolution.md): products of lists map to products of images. In $\mathcal R$, multiplying monomials adds exponents on each axis modulo $s_\alpha$, so the convolution becomes a $d$-dimensional cyclic convolution.

Each $\lambda$ has a unique expansion $\lambda=\sum_{\beta=1}^d\delta_\beta P_\beta$ with $0\le\delta_\beta<s_\beta$. Here $\delta_\beta$ is the digit of $\lambda$ on axis $\beta$, and $\delta_\alpha$ means the same with $\alpha$ in place of $\beta$. Then
$$b_\alpha\equiv\delta_\alpha+\mu_\alpha\sum_{\beta<\alpha}\delta_\beta P_\beta\pmod{s_\alpha},$$
since $\mu_\alpha\lambda=\sum_\beta\mu_\alpha\delta_\beta P_\beta$, the terms with $\beta>\alpha$ are multiples of $s_\alpha$, and $\mu_\alpha P_\alpha\equiv1$.

So for fixed earlier digits, $\delta_\alpha\mapsto b_\alpha$ is a cyclic shift of axis $\alpha$ by an amount that depends only on axes $\beta<\alpha$. The shifts must run from axis $d$ down to axis $1$. A shift of axis $\alpha$ reads the digits $\delta_\beta$ with $\beta<\alpha$, which stay unchanged until their own shift. Shifting axis $1$ first would change $\delta_1$ before the shift on axis $2$ reads it. The result moves the coefficient at $(\delta_1,\ldots,\delta_d)$ to position $(b_1,\ldots,b_d)$.

Take $S=6$, $s_1=2$, $s_2=3$. Then $\mu_1=1$, $\mu_2=2$, and $\Phi(x)=x_1x_2^2$. For $\lambda=3=1\cdot1+1\cdot2$, the digits are $\delta_1=1$ and $\delta_2=1$, giving $b_1=1$ and $b_2\equiv1+2\cdot1\equiv0\pmod 3$. Directly, $(x_1x_2^2)^3=x_1^3x_2^6=x_1$ in $\mathcal R$.

This is the Chinese-remainder split used by <cite data-source="paper">Agarwal and Cooley used the Chinese remainder</cite>.

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

Write the body to `exegenius/tasks/0232-write-crt-axis-map.answer.md` and the JSON to `exegenius/tasks/0232-write-crt-axis-map.answer.json`, then run `exegenius submit 0232-write-crt-axis-map` in the project directory. If submit rejects the answer, fix the answer and submit again.
