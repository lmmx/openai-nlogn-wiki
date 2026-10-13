# exegenius task 0086-write-crt-axis-map

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
- Linear network (also: fixed linear network, network, pointwise linear gate, wires)
- Frame of a vertex (also: frame)
- Role streams from a cyclic row split (also: roles)
- Subset-intersection finite network (also: three-element subset network, gather and scatter wires)
- Nested subspace labels
- Address shear (also: H + D shear, endpoint operator)
- Rank-saving recursion (also: recursive saving, recursive scheme, edge matrix)
- Fast interchange of address chunks (also: chunk interchange, address chunks, linear-cost address update, address fields, address field)
- Gaussian dyadic numbers (also: Gaussian dyadics, Z[i,1/2] (Gaussian dyadic numbers))
- Simultaneous butterfly layer H₀ (also: H_0 layer)
- Polynomial ring modulo yʳ + 1 (also: C[y]/(y^r+1))
  - $y$ (polynomial variable): The formal variable whose powers act as roots of unity on the remaining axes.
  - $r$ (coefficient count): The number of complex coefficients in each polynomial record, which is a power of two.
- Root of unity (also: primitive root of unity)
- Synthetic polynomial transform (also: synthetic transform, polynomial transform, twiddle multiplication)
- Discrete Fourier transform (also: Fourier transform, twiddle step)
- Multidimensional transform with power-of-two axes (also: power-of-two tensor transform)
- Gaussian resampling (also: Gaussian gridding, target permutation)
- Cyclic convolution (also: convolution modulo x^S - 1)
- Bluestein's chirp identity (also: chirp identity)
- Radix-digit convolution (also: radix-2^b digit polynomials)
- Signed coefficient packing (also: Kronecker substitution)
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
- Tensor product

## This page

Concept: Chinese-remainder axis map
Gloss: The bijection sending a coefficient index written in mixed radix with pairwise coprime lengths to coordinates on a product of cyclic axes, which turns one cyclic convolution into a multidimensional one.
Also called: Chinese-remainder address map

## This page in the argument

The step: The radix-digit coefficient list is placed on distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.

It serves these steps, from the main result down:

- The integer product is computed exactly on one fixed-tape machine in $O(n(\lg n)^{1-\kappa})$ worst-case time.; how: reduce exact multiplication to convolution of radix digits, compute the convolution by synthetic transforms on tape layouts, and bound the total tape cost with a power saving (on [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input length), bound on [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md): The number of bits in each of the two integers being multiplied.
- $n$ (input bit length), bound on [Power saving in the logarithmic factor](power-saving.md): The number of bits in each input integer.
- $\kappa$ (saving exponent), bound on [Power saving in the logarithmic factor](power-saving.md): A fixed number with $\kappa > 0$ that sets the size of the power saving.
- $z$ (Gaussian dyadic), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): A Gaussian dyadic number, a complex number whose real and imaginary parts are dyadic rationals.
- $a$ (real part), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The real part of $z$, a dyadic rational.
- $b$ (imaginary part), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The imaginary part of $z$, a dyadic rational.
- $m$ (numerator), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The integer numerator of a dyadic rational $m/2^k$.
- $k$ (denominator exponent), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The nonnegative integer exponent $k$ such that the denominator of a dyadic rational is $2^k$.
- $\mathcal{G}$ (Gaussian dyadics), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The set of all Gaussian dyadic numbers.
- $u$ (first input), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): A Gaussian dyadic number, the first input to the butterfly.
- $v$ (second input), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): A Gaussian dyadic number, the second input to the butterfly.
- $a$ (first bank value), bound on [Linear network](linear-network.md): The value of the first bank, held on one wire.
- $b$ (second bank value), bound on [Linear network](linear-network.md): The value of the second bank, held on one wire.
- $W$ (role count), bound on [Role streams from a cyclic row split](role-streams.md): The number of roles, which is the number of fixed wire places in the network.
- $V$ (node volume), bound on [Role streams from a cyclic row split](role-streams.md): The number of bits the node holds after its rows are padded.
- $u$ (tail vertex), bound on [Frame of a vertex](frame.md): The vertex at which an edge starts, a source, gate or sink of the network.
- $v$ (head vertex), bound on [Frame of a vertex](frame.md): The vertex at which an edge ends, a source, gate or sink of the network.
- $D_v$ (frame), bound on [Frame of a vertex](frame.md): The invertible linear operator that is the frame of vertex $v$, acting on arrays indexed by the common address set.
- $g$ (logical array), bound on [Frame of a vertex](frame.md): The array a role carries in the logical interpretation, before it is stored through the frame.
- $H$ (first address field), bound on [Address shear](address-shear.md): The first of the two address fields, which the shear replaces by H + D.
- $D$ (second address field), bound on [Address shear](address-shear.md): The second of the two address fields, which the shear adds to H and leaves fixed.
- $h$ (ground set size), bound on [Subset-intersection finite network](subset-network.md): The number of elements of the ground set $[h]$, so $h$ counts elements.
- $\mathcal T$ (three-element triples), bound on [Subset-intersection finite network](subset-network.md): The set of three-element subsets of $[h]$.
- $x_S$ (bank X scalar), bound on [Subset-intersection finite network](subset-network.md): The bank-$X$ scalar stored at the triple $S$.
- $y_S$ (bank Y scalar), bound on [Subset-intersection finite network](subset-network.md): The bank-$Y$ scalar stored at the triple $S$.
- $V$ (fixed space), bound on [Nested subspace labels](subspace-labels.md): The fixed space in which all labels lie.
- $m$ (space dimension), bound on [Nested subspace labels](subspace-labels.md): The dimension of V, which counts the independent directions in V.
- $L$ (vertex label), bound on [Nested subspace labels](subspace-labels.md): The subspace of V assigned to a vertex.
- $x$ (vertex), bound on [Nested subspace labels](subspace-labels.md): A gate or terminal of the network, at the tail of an edge.
- $y$ (neighbouring vertex), bound on [Nested subspace labels](subspace-labels.md): The vertex at the other end of an edge from x.
- $a$ (edge matrix rank), bound on [Rank-saving recursion](recursive-saving.md): The rank of an edge matrix, which counts the smaller calls that edge costs.
- $W$ (wire role count), bound on [Rank-saving recursion](recursive-saving.md): The number of fixed wire roles over which the recursion runs.
- $s$ (smaller call total), bound on [Rank-saving recursion](recursive-saving.md): The total number of smaller calls summed over all roles.
- $m$ (label space dimension), bound on [Rank-saving recursion](recursive-saving.md): The dimension of the fixed space that holds the subspace labels.
- $A$ (first address field), bound on [Fast interchange of address chunks](tape-interchange.md): One of the two disjoint equal-width address fields that the interchange swaps.
- $B$ (second address field), bound on [Fast interchange of address chunks](tape-interchange.md): The other of the two disjoint equal-width address fields that the interchange swaps.
- $u$ (field width), bound on [Fast interchange of address chunks](tape-interchange.md): The number of bits in each address field being swapped.
- $V$ (stored volume), bound on [Fast interchange of address chunks](tape-interchange.md): The total number of data units held in the array.
- $\tau$ (cost exponent), bound on [Fast interchange of address chunks](tape-interchange.md): The fixed exponent, below one, in the interchange's cost bound.
- $m$ (recursion parameter), bound on [Fast interchange of address chunks](tape-interchange.md): The parameter of the recursion, against which the sum of ranks is compared.
- $x$ (formal variable), bound on [Signed coefficient packing](signed-packing.md): The formal variable of the polynomial A, whose powers mark the coefficient positions.
- $m$ (coefficient count), bound on [Signed coefficient packing](signed-packing.md): The number of integer coefficients of the polynomial A, so the coefficient indices run from 0 to m-1.
- $b$ (slot width), bound on [Signed coefficient packing](signed-packing.md): The number of bits in each slot, the bit spacing between consecutive coefficients of the packed integer.
- $A$ (packed polynomial), bound on [Signed coefficient packing](signed-packing.md): The polynomial with m integer coefficients that is packed into a single integer.
- $a_i$ (coefficient), bound on [Signed coefficient packing](signed-packing.md): The i-th integer coefficient of A, bounded in absolute value by 2^(b-1).
- $N_A$ (packed integer), bound on [Signed coefficient packing](signed-packing.md): The single integer obtained from A by placing coefficient a_i at bit offset bi, equal to A evaluated at 2^b.
- $B$ (second polynomial), bound on [Signed coefficient packing](signed-packing.md): A second polynomial with integer coefficients, multiplied by A.
- $N_B$ (packed integer of B), bound on [Signed coefficient packing](signed-packing.md): The single integer obtained from B by packing its coefficients at bit offsets of b bits, equal to B evaluated at 2^b.
- $n$ (integer bit length), bound on [Established fast multiplier](multiplier-subroutine.md): The bit length of each integer being multiplied, counting the bits the running time is measured against.
- $H_0$ (simultaneous butterfly map), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The map H_0(u,v) = ((u+v)/2, (u-v)/2) on a pair of values, applied at once to a selected bit of every address chunk.
- $u$ (first input value), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The value at one of the two addresses that differ only in the selected bit.
- $v$ (second input value), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The value at one of the two addresses that differ only in the selected bit.
- $D$ (selected chunk count), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The number of address chunks in the layer, each contributing one selected bit.
- $d$ (chunk bound), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): An upper bound on the number of equal-width address chunks in a layer.
- $V$ (logical volume), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): The number of stored data bits in the array.
- $\lambda'$ (layer cost exponent), bound on [Simultaneous butterfly layer H₀](butterfly-layer.md): A fixed exponent below 1 in the cost bound of a layer.
- $x$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): A formal variable whose powers are the monomials of the polynomials being multiplied.
- $S$ (list length), bound on [Cyclic convolution](cyclic-convolution.md): The number of coefficients in each list, which is also the modulus of the exponent wraparound.
- $a$ (first coefficient list), bound on [Cyclic convolution](cyclic-convolution.md): The first input list, whose entries are the coefficients $a_0,\dots,a_{S-1}$ of $a(x)$.
- $b$ (second coefficient list), bound on [Cyclic convolution](cyclic-convolution.md): The second input list, whose entries are the coefficients $b_0,\dots,b_{S-1}$ of $b(x)$.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The output list of $S$ coefficients, the cyclic convolution of $a$ and $b$.
- $k$ (output position), bound on [Cyclic convolution](cyclic-convolution.md): An index of an output coefficient, ranging over $0,\dots,S-1$.
- $i$ (first input index), bound on [Cyclic convolution](cyclic-convolution.md): An index of a coefficient of the first list, ranging over $0,\dots,S-1$.
- $j$ (second input index), bound on [Cyclic convolution](cyclic-convolution.md): An index of a coefficient of the second list, ranging over $0,\dots,S-1$.
- $b$ (digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each radix digit.
- $m$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of digits in each input, m = ceil(n/b).
- $u_i$ (first-input digit), bound on [Radix-digit convolution](radix-digit-convolution.md): The i-th radix digit of the first input.
- $v_i$ (second-input digit), bound on [Radix-digit convolution](radix-digit-convolution.md): The i-th radix digit of the second input.
- $t$ (formal variable), bound on [Radix-digit convolution](radix-digit-convolution.md): The formal variable of the digit polynomials, whose powers index the digits.
- $U$ (first digit polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial in t whose coefficients are the digits of the first input.
- $V$ (second digit polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial in t whose coefficients are the digits of the second input.
- $W$ (product polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The product U(t)V(t) of the two digit polynomials.
- $w_k$ (product coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The k-th coefficient of W, the sum of u_i v_j over i+j=k.
- $q$ (transform length), bound on [Discrete Fourier transform](fourier-transform.md): The number of entries of the input vector $u$, which is also the number of entries of its transform.
- $u$ (input vector), bound on [Discrete Fourier transform](fourier-transform.md): The vector of complex numbers to be transformed, with entries $u_0, \dots, u_{q-1}$.
- $j$ (input index), bound on [Discrete Fourier transform](fourier-transform.md): The index running over the entries of $u$, from $0$ to $q-1$.
- $k$ (output index), bound on [Discrete Fourier transform](fourier-transform.md): The index running over the entries of the transform, from $0$ to $q-1$.
- $\omega$ (primitive root of unity), bound on [Discrete Fourier transform](fourier-transform.md): The primitive $q$-th root of unity $\exp(-2\pi i/q)$, whose powers define the transform.
- $\hat u$ (transform of u), bound on [Discrete Fourier transform](fourier-transform.md): The discrete Fourier transform of $u$, a vector of length $q$.
- $d$ (number of axes), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The number of axes of the array, which is the number of coordinates it is indexed by.
- $r_\ell$ (axis length), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The length of axis $\ell$, a power of two: the number of entries along that coordinate direction.
- $A$ (input array), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The array being transformed, with entries indexed by tuples $(j_1,\dots,j_d)$.
- $B$ (transformed array), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The result of the transform, with entries indexed by tuples $(k_1,\dots,k_d)$.
- $j_\ell$ (axis input index), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The index of an entry along axis $\ell$, ranging over $0,1,\dots,r_\ell-1$.
- $k_\ell$ (axis output index), bound on [Multidimensional transform with power-of-two axes](multidim-transform.md): The output index along axis $\ell$, ranging over $0,1,\dots,r_\ell-1$.
- $y$ (polynomial variable), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The formal variable whose powers act as roots of unity on the remaining axes.
- $r$ (coefficient count), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The number of complex coefficients in each polynomial record, which is a power of two.
- $a_i$ (coefficient), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): The i-th entry of a coefficient list, the coefficient of y^i in the polynomial.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the source transform, which is the number of coordinates it acts on.
- $t$ (target length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the target transform, an integer greater than s coprime to s.
- $F_q$ (transform of length q), bound on [Gaussian resampling](gaussian-resampling.md): The discrete Fourier transform acting on vectors of length q.
- $P_s$ (source permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation on vectors of length s that sends u to the vector with entries u_{tj}, indices taken modulo s.
- $P_t$ (target permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation on vectors of length t that sends v to the vector with entries v_{-sk}, indices taken modulo t.
- $\alpha$ (Gaussian width parameter), bound on [Gaussian resampling](gaussian-resampling.md): A fixed integer parameter that sets the width of the Gaussian weights in the resampling maps.
- $A$ (forward resampling map), bound on [Gaussian resampling](gaussian-resampling.md): A contraction from vectors of length s to vectors of length t, used in the identity.
- $B_0$ (backward resampling map), bound on [Gaussian resampling](gaussian-resampling.md): A contraction from vectors of length t back to vectors of length s, used in the identity.
- $q$ (transform length), bound on [Bluestein's chirp identity](bluestein.md): The number of entries of the vector being transformed, which the chirp and the index wrap are taken modulo.
- $u$ (input vector), bound on [Bluestein's chirp identity](bluestein.md): The vector of length $q$ whose transform is taken.
- $j$ (input index), bound on [Bluestein's chirp identity](bluestein.md): An index from $0$ to $q-1$ labelling the entries of the input vector.
- $k$ (output index), bound on [Bluestein's chirp identity](bluestein.md): An index from $0$ to $q-1$ labelling the entries of the transform.
- $c$ (chirp value), bound on [Bluestein's chirp identity](bluestein.md): The value $\exp(-\pi i m^2/q)$ of the chirp sequence at an integer index $m$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Cyclic convolution](cyclic-convolution.md): The product of two coefficient lists in the ring of polynomials modulo x^S − 1, in which exponents wrap around modulo S.
  Shown as: Chinese-remainder axis map *<predicate>* Cyclic convolution

## Pages that build on this one

- Fixed-tape integer multiplication with a power saving: A deterministic fixed-tape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1−κ)) worst-case time, for a fixed κ = 2^(−182), disproving the n log n optimality conjecture in this model.

## Other pages you may link to

- [Fixed-tape machine model](fixed-tape-model.md)
- [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Power saving in the logarithmic factor](power-saving.md)
- [Gaussian dyadic numbers](gaussian-dyadic.md)
- [Linear network](linear-network.md)
- [Role streams from a cyclic row split](role-streams.md)
- [Frame of a vertex](frame.md)
- [Address shear](address-shear.md)
- [Subset-intersection finite network](subset-network.md)
- [Nested subspace labels](subspace-labels.md)
- [Rank-saving recursion](recursive-saving.md)
- [Fast interchange of address chunks](tape-interchange.md)
- [Signed coefficient packing](signed-packing.md)
- [Established fast multiplier](multiplier-subroutine.md)
- [Tensor product](tensor-product.md)
- [Simultaneous butterfly layer H₀](butterfly-layer.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Multidimensional transform with power-of-two axes](multidim-transform.md)
- [Root of unity](roots-of-unity.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "Agarwal and Cooley used the Chinese remainder" (paper)

  > To use the source tensor, we first place the ordinary coefficient stream in its tensor order. Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution~\cite{AgarwalCooley1977}. The following map uses that algebraic split, with coordinate powers that make the change of order a sequence of controlled cyclic shifts.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "so these powers run through all $S$ target monomials once" (The reader cannot check that k mapping to the vector of residues mu_i k mod s_i is injective, because that depends on the Chinese remainder theorem, which the page does not state. The reader also needs this to conclude that the powers hit every target monomial.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "It maps $\mathbb C[x]/(x^S-1)$ to" (The page asserts that Phi sends x^S-1 to zero in the target ring. This needs Phi(x)^S = 1, which in turn needs that each s_i divides S. The page does not say this, and the reader cannot check it from the page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "so a product of two lists is computed axis by axis" (The page claims products are computed axis by axis but does not say how. The reader would need the multidimensional transform, which is not linked here, and the page does not show that the target product is computed one axis at a time.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "a sequence of controlled cyclic shifts on the axes" (The closing claim about what the split achieves uses 'controlled cyclic shifts', which the page never defines. The reader cannot check that reordering the coefficients turns into such shifts.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Say what $x_i$ denotes where it is first used (for a size or count, what it counts): "sending $x$ to $\prod_i x_i^{\mu_i}$" (The page never says what x_i denotes. The target ring C[x_1,...,x_d] is introduced without saying that x_i is the variable of axis i, so the reader can only guess it from the ring's relations x_i^{s_i}-1.)
- Explain "algebra map" in a sentence where it is first used.
- Explain "Chinese remainder theorem" in a sentence where it is first used.
- Explain "isomorphism" in a sentence where it is first used.

## Previous version (revise it)

It has 279 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 348 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The Chinese-remainder axis map is a bijection that places the coefficients of a [cyclic convolution](cyclic-convolution.md) on the axes of a product of cyclic rings, so that the convolution becomes multidimensional. The radix-digit coefficient list is laid out this way, with each axis of distinct prime length.

Let $d$ be the number of axes. Let $s_i$ be the length of axis $i$, a count of positions on that axis, and assume $s_1,\ldots,s_d$ are pairwise coprime. Let $S=s_1s_2\cdots s_d$ be the total number of coefficients. Let $x$ be the variable of the ring $\mathbb C[x]/(x^S-1)$.

Let $P_i=s_1\cdots s_{i-1}$ be the product of the lengths before axis $i$, with $P_1=1$. Let $\mu_i$ be the inverse of $P_i$ modulo $s_i$, so that $\mu_iP_i\equiv1\pmod{s_i}$; it exists because $P_i$ is coprime to $s_i$.

Let $\Phi$ be the algebra map sending $x$ to $\prod_i x_i^{\mu_i}$. It maps $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1)$. Since each $\mu_i$ is a unit modulo $s_i$, the Chinese remainder theorem makes the exponents of $\Phi(x)^0,\ldots,\Phi(x)^{S-1}$ pairwise distinct, so these powers run through all $S$ target monomials once. Hence $\Phi$ is an isomorphism. The map $\Phi$ is an isomorphism that preserves [cyclic convolution](cyclic-convolution.md), so a product of two lists is computed axis by axis.

Let $k$ be a coefficient index with $0\le k<S$. It has a unique mixed-radix expansion $k=\sum_{j=1}^d a_jP_j$ with $0\le a_j<s_j$, and $a_j$ is the mixed-radix digit of $k$ on axis $j$. Let $b_i$ be the exponent of $x_i$ in $\Phi(x^k)$, reduced so that $0\le b_i<s_i$. Then $b_i\equiv a_i+\mu_i\sum_{j<i}a_jP_j \pmod{s_i}$. This follows from $\mu_ik=\sum_j\mu_ia_jP_j$: terms with $j>i$ are multiples of $s_i$, and $\mu_iP_i\equiv1\pmod{s_i}$.

Take $S=6$, $s_1=2$, $s_2=3$. Then $P_1=1$, $P_2=2$, $\mu_1=1$, $\mu_2=2$, so $\Phi(x)=x_1x_2^2$. For $k=3=1+1\cdot2$, the digits are $a_1=1$ and $a_2=1$, giving $b_1=1$ and $b_2\equiv1+2\cdot1\equiv0\pmod 3$. Directly, $(x_1x_2^2)^3=x_1^3x_2^6=x_1$ in the target ring.

This is the Chinese-remainder split of Agarwal and Cooley <cite data-source="paper">Agarwal and Cooley used the Chinese remainder</cite>. Its point is that reordering the coefficients becomes a sequence of controlled cyclic shifts on the axes.

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

Write the body to `exegenius/tasks/0086-write-crt-axis-map.answer.md` and the JSON to `exegenius/tasks/0086-write-crt-axis-map.answer.json`, then run `exegenius submit 0086-write-crt-axis-map` in the project directory. If submit rejects the answer, fix the answer and submit again.
